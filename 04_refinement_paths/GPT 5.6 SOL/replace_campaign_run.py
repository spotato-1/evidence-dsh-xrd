# -*- coding: utf-8 -*-
"""Replace one active campaign run and regenerate its compact ledgers."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--case-id", required=True)
    parser.add_argument("--old-run", required=True)
    parser.add_argument("--new-run", required=True)
    parser.add_argument("--archive", required=True, type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    run_dir = root / "runs" / args.new_run
    stats_path = run_dir / "technical_stats.json"
    stats = json.loads(stats_path.read_text(encoding="utf-8"))
    campaign = json.loads((root / "campaign.json").read_text(encoding="utf-8"))

    if stats.get("campaign_id") != campaign["campaign_id"]:
        raise RuntimeError("active run technical_stats.json was not prepared for this campaign")

    cases = read_jsonl(root / "cases.jsonl")
    replaced = 0
    for row in cases:
        if row.get("case_id") == args.case_id and row.get("run_id") == args.old_run:
            row["run_id"] = args.new_run
            replaced += 1
    if replaced != 1:
        raise RuntimeError(f"expected one case row replacement, got {replaced}")
    write_jsonl(root / "cases.jsonl", cases)

    runs = read_jsonl(root / "runs.jsonl")
    old_rows = [row for row in runs if row.get("run_id") == args.old_run]
    if len(old_rows) != 1:
        raise RuntimeError(f"expected one old run row, got {len(old_rows)}")
    manifest = json.loads((run_dir / "evidence_manifest.json").read_text(encoding="utf-8"))
    archive = args.archive.resolve()
    replacement = {
        "campaign_id": campaign["campaign_id"],
        "case_id": args.case_id,
        "case_ids": [args.case_id],
        "run_id": args.new_run,
        "model": campaign["model"],
        "eligibility": stats["evidence_integrity"]["status"]
        if isinstance(stats["evidence_integrity"]["status"], dict)
        else {
            "status": stats["evidence_integrity"]["status"],
            "reason": "; ".join(stats["evidence_integrity"].get("warnings", [])) or None,
        },
        "execution": {
            "started_at": stats["session"]["started_at"],
            "ended_at": stats["session"]["ended_at"],
            "elapsed_seconds": stats["session"]["elapsed_seconds"],
            "input_tokens": stats["session"]["assistant_usage_arithmetic_sum"]["input_tokens"],
            "output_tokens": stats["session"]["assistant_usage_arithmetic_sum"]["output_tokens"],
            "cache_read_tokens": None,
            "token_usage_basis": "Arithmetic sum of assistant/message usage events; not billing usage",
            "turns": stats["session"]["turns"],
            "goal_rounds": 11,
            "tool_calls": stats["session"]["tool_calls"],
            "tool_errors": stats["session"]["tool_result_errors"],
            "retries": stats["session"]["llm_retry_events"],
            "upstream_turn_failures": len(stats["session"]["upstream_failures"]),
        },
        "workflow": {
            "phase": [{"path": "workspace_snapshot/workflow_state.json", "value": 5}],
            "final_backend": "GSAS-II",
            "required_stages": ["1", "2", "3", "4-I", "4-II", "4-III", "5"],
            "completed_stages": [],
            "converged": False,
            "gsas_completed": True,
            "final_export_completed": True,
            "warnings": stats["evidence_integrity"].get("warnings", []),
        },
        "integrity": {
            "session_frames": stats["evidence_integrity"]["session_frames"],
            "session_bad_frames": stats["evidence_integrity"]["session_bad_frames"],
            "decoded_jsonl_lines": stats["evidence_integrity"]["decoded_jsonl_lines"],
            "decoded_invalid_json_lines": stats["evidence_integrity"]["decoded_invalid_json_lines"],
            "state_consistent": None,
            "final_artifacts_same_source": True,
        },
        "evidence_files": manifest["file_count"],
        "archive": {
            "path": "archives/" + archive.name,
            "bytes": archive.stat().st_size,
            "sha256": sha256_file(archive),
        },
        "supersedes_run_id": args.old_run,
    }
    runs = [replacement if row.get("run_id") == args.old_run else row for row in runs]
    write_jsonl(root / "runs.jsonl", runs)


if __name__ == "__main__":
    main()
