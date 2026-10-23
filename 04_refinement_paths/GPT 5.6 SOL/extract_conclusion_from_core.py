# -*- coding: utf-8 -*-
"""Extract the final assistant text from an audit core session JSONL gzip."""

from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("core", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    last_text = None
    with gzip.open(args.core, "rt", encoding="utf-8") as handle:
        for line in handle:
            event = json.loads(line)
            if event.get("type") != "assistant/message":
                continue
            message = (event.get("data") or {}).get("message") or {}
            blocks = message.get("content") or []
            text = "\n\n".join(
                block.get("text", "")
                for block in blocks
                if isinstance(block, dict) and block.get("type") == "text"
            ).strip()
            if text:
                last_text = text
    if not last_text:
        raise SystemExit("no assistant text found")
    args.output.write_text(last_text + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
