#!/usr/bin/env python3
"""Safely set or increment SkillForge download counters."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATS = ROOT / "registry/download-stats.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill", help="正式 skill id")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--increment", type=int, metavar="N")
    group.add_argument("--set", type=int, dest="set_count", metavar="N")
    args = parser.parse_args()

    known = {
        json.loads(path.read_text(encoding="utf-8"))["name"]
        for path in ROOT.rglob("skill.json")
        if "templates" not in path.parts and "work" not in path.parts
    }
    if args.skill not in known:
        raise SystemExit(f"未知 skill: {args.skill}")

    data = json.loads(STATS.read_text(encoding="utf-8")) if STATS.exists() else {
        "version": "1.0.0", "updated_at": None, "counts": {}
    }
    current = data.setdefault("counts", {}).get(args.skill, 0)
    next_count = args.set_count if args.set_count is not None else current + args.increment
    if next_count < 0:
        raise SystemExit("下载计数不能小于 0")

    data["counts"][args.skill] = next_count
    data["counts"] = dict(sorted(data["counts"].items()))
    data["updated_at"] = datetime.now(timezone.utc).isoformat()
    STATS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{args.skill}: {current} -> {next_count}")


if __name__ == "__main__":
    main()
