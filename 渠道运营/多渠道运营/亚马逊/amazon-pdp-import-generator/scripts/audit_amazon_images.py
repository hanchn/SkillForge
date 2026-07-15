#!/usr/bin/env python3
"""Create a technical Amazon image audit; visual and rights approval remain human gates."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from PIL import Image


EXTENSIONS = {".jpg", ".jpeg", ".tif", ".tiff", ".png", ".gif"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("image_folder", type=Path)
    parser.add_argument("--output", type=Path, default=Path("image_compliance_report.csv"))
    parser.add_argument("--min-long-side", type=int, default=500)
    parser.add_argument("--max-long-side", type=int, default=10000)
    parser.add_argument("--zoom-long-side", type=int, default=1000)
    parser.add_argument("--max-bytes", type=int, default=None, help="Set only from a verified current marketplace rule")
    args = parser.parse_args()
    paths = sorted(p for p in args.image_folder.rglob("*") if p.is_file() and p.suffix.lower() in EXTENSIONS)
    if not paths:
        parser.error("no supported image files found")
    rows = []
    blocked = False
    for path in paths:
        status = "PASS_TECHNICAL"
        reasons = []
        try:
            with Image.open(path) as image:
                width, height = image.size
                image_format = image.format or "UNKNOWN"
                animated = bool(getattr(image, "is_animated", False))
        except Exception as exc:
            width = height = 0
            image_format = "UNREADABLE"
            animated = False
            status = "BLOCK"; reasons.append(f"unreadable:{type(exc).__name__}")
        longest = max(width, height)
        size_bytes = path.stat().st_size
        ratio = round(width / height, 4) if height else ""
        if longest and not args.min_long_side <= longest <= args.max_long_side:
            status = "BLOCK"; reasons.append("long_side_out_of_verified_range")
        if animated:
            status = "BLOCK"; reasons.append("animated_image_not_allowed")
        if args.max_bytes is not None and size_bytes > args.max_bytes:
            status = "BLOCK"; reasons.append("file_size_over_verified_limit")
        if status != "BLOCK" and longest < args.zoom_long_side:
            status = "WARNING"; reasons.append("below_zoom_preference")
        reasons.append("aspect_ratio_requires_gallery_crop_review")
        blocked |= status == "BLOCK"
        rows.append({
            "path": path.as_posix(), "format": image_format, "width": width, "height": height,
            "longest_side": longest, "size_bytes": size_bytes, "aspect_ratio": ratio,
            "zoom_eligible": longest >= args.zoom_long_side, "animated": animated,
            "technical_status": status, "reasons": ";".join(reasons),
            "visual_review_required": True,
        })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    print(f"audited={len(rows)} blocked={sum(r['technical_status']=='BLOCK' for r in rows)} output={args.output}")
    return 2 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())
