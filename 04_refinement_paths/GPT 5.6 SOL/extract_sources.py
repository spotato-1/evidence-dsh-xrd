#!/usr/bin/env python3
"""Extract prompt blocks and consolidated DSH messages without editing sources."""

import argparse
import gzip
import hashlib
import json
from pathlib import Path

from docx import Document
from docx.document import Document as _Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def iter_blocks(document):
    if not isinstance(document, _Document):
        raise TypeError("document must be python-docx Document")
    parent = document.element.body
    for child in parent.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, document)
        elif isinstance(child, CT_Tbl):
            yield Table(child, document)


def extract_docx(path):
    document = Document(str(path))
    blocks = []
    plain_lines = []
    for index, block in enumerate(iter_blocks(document), 1):
        if isinstance(block, Paragraph):
            value = {
                "index": index,
                "type": "paragraph",
                "style": block.style.name if block.style is not None else None,
                "text": block.text,
            }
            blocks.append(value)
            if block.text:
                plain_lines.append(block.text)
        else:
            rows = []
            for row in block.rows:
                rows.append([cell.text for cell in row.cells])
            blocks.append({"index": index, "type": "table", "rows": rows})
            for row in rows:
                plain_lines.append("\t".join(row))
    return {
        "source": {
            "name": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        },
        "blocks": blocks,
        "plain_text": "\n".join(plain_lines),
    }


def message_text(message):
    if not isinstance(message, dict):
        return ""
    parts = []
    for item in message.get("content", []):
        if not isinstance(item, dict):
            continue
        if item.get("type") == "text" and isinstance(item.get("text"), str):
            parts.append(item["text"])
    return "\n".join(parts)


def extract_run_messages(run_dir):
    path = run_dir / "session_core.jsonl.gz"
    records = []
    invalid = []
    turn_starts = []
    with gzip.open(path, "rt", encoding="utf-8-sig", errors="strict") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                invalid.append({"line": line_number, "error": str(exc)})
                continue
            event_type = event.get("type")
            if event_type == "turn/start":
                data = event.get("data") if isinstance(event.get("data"), dict) else {}
                turn_starts.append(
                    {
                        "seq": event.get("seq", event.get("seq0")),
                        "turn": data.get("turn"),
                    }
                )
                continue
            if event_type not in {"user/message", "assistant/message"}:
                continue
            data = event.get("data") if isinstance(event.get("data"), dict) else {}
            if isinstance(data.get("message"), dict):
                message = data["message"]
            else:
                message = {
                    "role": data.get("role"),
                    "content": data.get("content", []),
                    "source": data.get("source", {}),
                }
            text = message_text(message)
            if not text:
                continue
            source = message.get("source") if isinstance(message.get("source"), dict) else {}
            records.append(
                {
                    "seq": event.get("seq", event.get("seq0")),
                    "time": event.get("time"),
                    "type": event_type,
                    "role": message.get("role"),
                    "turn": data.get("turn"),
                    "step": data.get("step"),
                    "model": source.get("model"),
                    "provider": source.get("provider"),
                    "source_kind": source.get("kind"),
                    "source_plugin": source.get("plugin"),
                    "message_id": message.get("id", data.get("id")),
                    "surface_op": event.get("surfaceOp"),
                    "text": text,
                }
            )

    for record in records:
        if record["type"] != "user/message" or record.get("turn") is not None:
            continue
        record_seq = record.get("seq")
        if not isinstance(record_seq, int):
            continue
        for marker in turn_starts:
            marker_seq = marker.get("seq")
            if isinstance(marker_seq, int) and marker_seq > record_seq:
                record["turn"] = marker.get("turn")
                break

    final_by_turn = {}
    for record in records:
        if record["type"] != "assistant/message":
            continue
        turn = record.get("turn")
        final_by_turn[str(turn)] = record

    return {
        "run_id": run_dir.name,
        "session_core": {
            "path": "runs/{}/session_core.jsonl.gz".format(run_dir.name),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        },
        "records": records,
        "final_assistant_message_by_turn": final_by_turn,
        "invalid_lines": invalid,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt-docx", required=True, type=Path)
    parser.add_argument("--evidence-root", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    if args.output_dir.exists():
        existing = list(args.output_dir.iterdir())
        if existing:
            raise RuntimeError("refusing to reuse non-empty output directory")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    prompt = extract_docx(args.prompt_docx)
    write_json(args.output_dir / "source_prompts.json", prompt)
    with (args.output_dir / "source_prompts.txt").open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(prompt["plain_text"])
        handle.write("\n")

    cases = []
    with (args.evidence_root / "cases.jsonl").open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                cases.append(json.loads(line))

    runs = []
    for run_dir in sorted((args.evidence_root / "runs").iterdir()):
        if run_dir.is_dir():
            runs.append(extract_run_messages(run_dir))
    write_json(args.output_dir / "run_messages.json", {"cases": cases, "runs": runs})

    index = []
    case_map = {}
    for row in cases:
        case_map.setdefault(row["run_id"], []).append(row["case_id"])
    for run in runs:
        user_records = [
            r
            for r in run["records"]
            if r["type"] == "user/message" and r.get("source_kind") == "user"
        ]
        assistant_records = [r for r in run["records"] if r["type"] == "assistant/message"]
        index.append(
            {
                "run_id": run["run_id"],
                "case_ids": case_map.get(run["run_id"], []),
                "user_messages": len(user_records),
                "assistant_text_messages": len(assistant_records),
                "assistant_turn_answers": len(run["final_assistant_message_by_turn"]),
                "user_text_chars": sum(len(r["text"]) for r in user_records),
                "assistant_text_chars": sum(len(r["text"]) for r in assistant_records),
                "invalid_core_lines": len(run["invalid_lines"]),
            }
        )
    write_json(args.output_dir / "message_index.json", index)
    print(json.dumps({"prompt_blocks": len(prompt["blocks"]), "runs": len(runs), "index": index}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
