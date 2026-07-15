#!/usr/bin/env python3
"""Keep every SkillForge package on a content-aware semantic version."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "registry/skill-versions.json"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
CONTENT_FILES = {"SKILL.md", "BASE_PROMPT.md", "INVOCATION.md"}
CONTENT_DIRS = {"references", "assets", "eval", "platforms"}


def parse_version(value: str) -> tuple[int, int, int]:
    match = SEMVER.fullmatch(value or "")
    if not match:
        raise ValueError(f"版本号必须是 SemVer x.y.z：{value!r}")
    return tuple(int(part) for part in match.groups())


def bump(value: str, level: str) -> str:
    major, minor, patch = parse_version(value)
    if level == "major":
        return f"{major + 1}.0.0"
    if level == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def skill_meta_paths(root: Path):
    for path in sorted(root.rglob("skill.json")):
        relative = path.relative_to(root)
        if relative.parts[0] not in {"templates", "work"}:
            yield path


def content_fingerprint(meta_path: Path, payload: dict) -> str:
    package = meta_path.parent
    normalized_meta = dict(payload)
    normalized_meta.pop("version", None)
    normalized_meta.pop("distribution", None)
    pieces = [json.dumps(normalized_meta, ensure_ascii=False, sort_keys=True)]
    for path in sorted(package.rglob("*")):
        if not path.is_file() or path.name in {"skill.json", "README.md"}:
            continue
        relative = path.relative_to(package)
        if path.name not in CONTENT_FILES and relative.parts[0] not in CONTENT_DIRS:
            continue
        pieces.append(relative.as_posix())
        pieces.append(path.read_text(encoding="utf-8"))
    return hashlib.sha256("\n".join(pieces).encode("utf-8")).hexdigest()


def update_readme(package: Path, version: str, changed: bool) -> None:
    path = package / "README.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    patterns = [
        r"(?m)^(>\s*当前版本[：:]\s*)[^\s]+\s*$",
        r"(?m)^(>\s*版本[：:]\s*)[^\s]+\s*$",
        r"(?m)^(\*\*当前版本\*\*[：:]\s*)[^\s]+\s*$",
    ]
    replaced = False
    for pattern in patterns:
        text, count = re.subn(pattern, rf"\g<1>{version}", text, count=1)
        if count:
            replaced = True
            break
    if not replaced:
        lines = text.splitlines()
        insert_at = 1 if lines and lines[0].startswith("# ") else 0
        lines[insert_at:insert_at] = ["", f"> 当前版本：{version}"]
        text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    if changed and "## 版本记录" in text:
        marker = "|---|---|---|"
        row = f"| {version} | {date.today().isoformat()} | 自动检测到 Skill 实质内容升级并同步版本。 |"
        if marker in text and row not in text:
            text = text.replace(marker, marker + "\n" + row, 1)
    path.write_text(text, encoding="utf-8")


def sync_versions(root: Path = ROOT, forced: dict[str, str] | None = None) -> dict:
    ledger_path = root / "registry/skill-versions.json"
    if ledger_path.exists():
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    else:
        ledger = {"schema_version": 1, "updated_at": date.today().isoformat(), "skills": {}}
    records = ledger.setdefault("skills", {})
    forced = forced or {}
    active = set()
    changed_count = 0

    for meta_path in skill_meta_paths(root):
        payload = json.loads(meta_path.read_text(encoding="utf-8"))
        name = payload["name"]
        active.add(name)
        declared = payload.get("version", "")
        parse_version(declared)
        fingerprint = content_fingerprint(meta_path, payload)
        previous = records.get(name)
        changed = False
        if previous is None:
            version = declared
        else:
            previous_version = previous["version"]
            parse_version(previous_version)
            if parse_version(declared) > parse_version(previous_version):
                version = declared
                changed = True
            elif fingerprint != previous.get("fingerprint"):
                version = bump(previous_version, "patch")
                changed = True
            else:
                version = previous_version
        if name in forced:
            version = bump(version, forced[name])
            changed = True
        payload["version"] = version
        meta_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        update_readme(meta_path.parent, version, changed)
        records[name] = {
            "version": version,
            "fingerprint": fingerprint,
            "package_root": meta_path.parent.relative_to(root).as_posix(),
            "updated_at": date.today().isoformat(),
        }
        changed_count += int(changed)

    for name in set(records) - active:
        records.pop(name)
    ledger["updated_at"] = date.today().isoformat()
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"skills": len(active), "changed": changed_count}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bump", action="append", default=[], metavar="SKILL:LEVEL")
    args = parser.parse_args()
    forced = {}
    for item in args.bump:
        name, separator, level = item.partition(":")
        if not separator or level not in {"patch", "minor", "major"}:
            raise SystemExit("--bump 格式为 skill-id:patch|minor|major")
        forced[name] = level
    result = sync_versions(ROOT, forced)
    print(f"Versioned {result['skills']} skills; changed {result['changed']}")


if __name__ == "__main__":
    main()
