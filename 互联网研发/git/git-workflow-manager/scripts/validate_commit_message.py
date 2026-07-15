#!/usr/bin/env python3
"""Validate a commit message without installing or bypassing repository hooks."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PLACEHOLDERS = {"wip", "tmp", "test", "update", "fix", "提交", "更新", "修改"}


def fail(reason: str) -> int:
    print("FAILED_STEP: commit_message_validation", file=sys.stderr)
    print(f"RAW_ERROR: {reason}", file=sys.stderr)
    print("LIKELY_CAUSE: commit message does not meet the quality gate", file=sys.stderr)
    print("IMPACT: git commit must not be executed with this message", file=sys.stderr)
    print("SAFE_NEXT_ACTION: describe what changed, why, and how it was verified", file=sys.stderr)
    return 2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("message_file", type=Path)
    args = parser.parse_args()
    try:
        raw = args.message_file.read_text(encoding="utf-8")
    except OSError as exc:
        return fail(f"cannot read commit message: {exc}")
    lines = [line.strip() for line in raw.splitlines() if line.strip() and not line.lstrip().startswith("#")]
    message = "\n".join(lines).strip()
    meaningful = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "", message)
    if not meaningful:
        return fail("commit message is empty or whitespace-only")
    if len(meaningful) < 5:
        return fail("commit message contains fewer than 5 meaningful characters")
    if meaningful.casefold() in PLACEHOLDERS:
        return fail("commit message is a placeholder rather than a detailed record")
    print("COMMIT_MESSAGE_VALID: non-empty, length and placeholder checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
