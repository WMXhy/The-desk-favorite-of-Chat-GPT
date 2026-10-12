#!/usr/bin/env python3
"""Check this bundle's asset hashes, sprite grids, alpha, and compatibility export."""
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image

def validate(root):
    root = root.resolve()
    manifest = json.loads((root / "pet.json").read_text(encoding="utf-8"))
    rows = manifest["frames_per_standard_row"]
    checked = []
    images = {}
    for version in ("v2", "v1"):
        item = manifest["assets"][version]
        path = (root / item["path"]).resolve()
        if not path.is_relative_to(root):
            raise ValueError("Asset path is outside the bundle")
        encoded = path.read_bytes()
        if hashlib.sha256(encoded).hexdigest() != item["sha256"]:
            raise ValueError(f"{version}: SHA-256 mismatch")
        if not 0 < len(encoded) <= 20 * 1024 * 1024:
            raise ValueError(f"{version}: unsupported encoded size")
        with Image.open(path) as opened:
            if opened.format != "PNG" or opened.mode != "RGBA":
                raise ValueError(f"{version}: expected RGBA PNG")
            image = opened.copy()
        expected_rows = 11 if version == "v2" else 9
        if image.size != (1536, expected_rows * 208):
            raise ValueError(f"{version}: wrong dimensions")
        used_counts = rows + ([8, 8] if version == "v2" else [])
        alpha = image.getchannel("A")
        if alpha.getextrema()[0] != 0:
            raise ValueError(f"{version}: no transparent background")
        for row, count in enumerate(used_counts):
            for col in range(8):
                cell = alpha.crop((col*192, row*208, (col+1)*192, (row+1)*208))
                if (cell.getbbox() is not None) != (col < count):
                    raise ValueError(f"{version}: incorrect occupancy at row {row}, cell {col}")
        images[version] = image
        checked.append({"format": version, "dimensions": list(image.size),
                        "bytes": len(encoded), "populated_cells": sum(used_counts)})
    if images["v1"].tobytes() != images["v2"].crop((0,0,1536,1872)).tobytes():
        raise ValueError("v1 does not preserve the original action pixels")
    return {"ok": True, "checked": checked, "action_pixels_preserved": True}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps(validate(args.root), ensure_ascii=False, indent=2))
