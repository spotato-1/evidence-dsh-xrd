#!/usr/bin/env python3
"""DSH-XRD evidence bundle audit.

Computes a SHA-256 manifest for every file under the evidence bundle and writes
a small top-level structure summary. Read-only: it never modifies the inputs.

Usage:
    python audit.py
"""
import hashlib
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(ROOT, "MANIFEST.sha256")
SUMMARY = os.path.join(ROOT, "structure_summary.json")

IGNORE_DIRS = {".git", "__pycache__"}
SKIP_FILES = {"MANIFEST.sha256", "structure_summary.json", "audit.py"}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    entries = []
    top_level = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fn in filenames:
            if fn in SKIP_FILES:
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
            digest = sha256(full)
            size = os.path.getsize(full)
            entries.append({"path": rel, "sha256": digest, "bytes": size})
            top = rel.split("/")[0]
            top_level.setdefault(top, {"files": 0, "bytes": 0})
            top_level[top]["files"] += 1
            top_level[top]["bytes"] += size

    entries.sort(key=lambda e: e["path"])
    with open(MANIFEST, "w", encoding="utf-8") as f:
        for e in entries:
            f.write(f"{e['sha256']}  {e['bytes']:>10}  {e['path']}\n")

    summary = {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "root": ROOT,
        "total_files": len(entries),
        "total_bytes": sum(e["bytes"] for e in entries),
        "top_level": top_level,
    }
    with open(SUMMARY, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"Audit complete: {len(entries)} files, {summary['total_bytes']} bytes.")
    print(f"Manifest: {MANIFEST}")
    print(f"Summary:  {SUMMARY}")


if __name__ == "__main__":
    main()
