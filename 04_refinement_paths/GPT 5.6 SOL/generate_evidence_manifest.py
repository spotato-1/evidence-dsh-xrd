# -*- coding: utf-8 -*-
"""Generate a deterministic SHA-256 manifest for one frozen evidence directory."""

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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--output", default="evidence_manifest.json")
    args = parser.parse_args()
    root = args.root.resolve()
    output = root / args.output
    files = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        if path == output:
            continue
        files.append(
            {
                "path": path.relative_to(root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    output.write_text(
        json.dumps(
            {
                "schema_version": "1.0",
                "hash_algorithm": "SHA-256",
                "file_count": len(files),
                "files": files,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(output)


if __name__ == "__main__":
    main()
