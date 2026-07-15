#!/usr/bin/env python3
"""Validate the JD-to-screening JSON handoff using only the Python standard library."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED_CATEGORIES = {"MUST_HAVE", "TRAINABLE", "BONUS", "PROHIBITED"}
REQUIRED_PROHIBITED = {"name", "photo", "age", "gender", "marital_or_parental_status", "ethnicity", "religion", "health"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("screening_spec", type=Path)
    parser.add_argument("--allow-draft", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.screening_spec.read_text(encoding="utf-8"))
    errors = []

    for field in ("schema_version", "request_id", "package_version", "rubric_version", "status", "job", "criteria", "screening_policy"):
        if field not in data:
            errors.append(f"missing:{field}")
    if data.get("status") != "READY_FOR_HR" and not args.allow_draft:
        errors.append("status_must_be_READY_FOR_HR")

    criteria = data.get("criteria", [])
    ids = [item.get("criterion_id") for item in criteria]
    if not criteria:
        errors.append("criteria_empty")
    if None in ids or len(ids) != len(set(ids)):
        errors.append("criterion_id_missing_or_duplicate")
    for item in criteria:
        category = item.get("category")
        if category not in ALLOWED_CATEGORIES:
            errors.append(f"invalid_category:{item.get('criterion_id')}")
        if category == "MUST_HAVE":
            for field in ("job_related_reason", "minimum_evidence"):
                if not item.get(field) or item[field] == "待填写":
                    errors.append(f"must_have_missing_{field}:{item.get('criterion_id')}")
            if not any(item.get(field) for field in ("keywords", "synonyms", "evidence_actions", "acceptable_alternatives")):
                errors.append(f"must_have_has_no_recall_or_evidence_terms:{item.get('criterion_id')}")

    prohibited = set(data.get("prohibited_variables", []))
    if not REQUIRED_PROHIBITED.issubset(prohibited):
        errors.append("prohibited_variables_incomplete")

    if errors:
        raise SystemExit("INVALID\n" + "\n".join(errors))
    print(f"VALID request_id={data['request_id']} rubric_version={data['rubric_version']} criteria={len(criteria)}")


if __name__ == "__main__":
    main()
