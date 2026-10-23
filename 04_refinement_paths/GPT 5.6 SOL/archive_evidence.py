# -*- coding: utf-8 -*-
"""Create and CRC-check a ZIP archive from a frozen evidence directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("archive", type=Path)
    args = parser.parse_args()
    source = args.source.resolve()
    archive = args.archive.resolve()
    if archive.exists():
        raise SystemExit(f"refusing to overwrite {archive}")
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED) as handle:
        for path in sorted(item for item in source.rglob("*") if item.is_file()):
            handle.write(path, arcname=path.relative_to(source).as_posix())
    with zipfile.ZipFile(archive, "r") as handle:
        bad = handle.testzip()
        if bad is not None:
            raise RuntimeError(f"CRC check failed: {bad}")
    print(
        json.dumps(
            {
                "archive": str(archive),
                "bytes": archive.stat().st_size,
                "sha256": sha256_file(archive),
                "crc_check": "pass",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
