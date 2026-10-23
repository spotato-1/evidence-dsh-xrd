# -*- coding: utf-8 -*-
"""Add campaign replacement metadata to a copied run before hashing and archiving."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stats", type=Path)
    parser.add_argument("--campaign-id", required=True)
    parser.add_argument("--old-run", required=True)
    args = parser.parse_args()
    stats = json.loads(args.stats.read_text(encoding="utf-8"))
    stats["campaign_id"] = args.campaign_id
    stats["active_campaign_status"] = "primary"
    stats["supersedes_run_id"] = args.old_run
    args.stats.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(args.stats)


if __name__ == "__main__":
    main()
