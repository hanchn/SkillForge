#!/usr/bin/env python3
"""Evaluate a screening funnel against machine-readable alert thresholds."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def ratio(numerator: int, denominator: int) -> float | None:
    return round(numerator / denominator, 6) if denominator else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("metrics", type=Path)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    metrics = json.loads(args.metrics.read_text(encoding="utf-8"))
    policy = json.loads(args.policy.read_text(encoding="utf-8"))["thresholds"]
    required = ["request_id", "batch_id", "received", "parseable", "unique_parseable", "job_family_match", "must_have_pass", "shortlist"]
    missing = [field for field in required if field not in metrics]
    if missing:
        raise SystemExit("missing metrics: " + ", ".join(missing))
    if any(not isinstance(metrics[field], int) or metrics[field] < 0 for field in required[2:]):
        raise SystemExit("funnel counts must be non-negative integers")
    funnel = [metrics[field] for field in required[2:]]
    if any(left < right for left, right in zip(funnel, funnel[1:])):
        raise SystemExit("funnel counts must be non-increasing")

    parse_rate = ratio(metrics["parseable"], metrics["received"])
    family_rate = ratio(metrics["job_family_match"], metrics["unique_parseable"])
    shortlist_rate = ratio(metrics["shortlist"], metrics["unique_parseable"])
    alerts = []

    if parse_rate is not None and parse_rate < policy["parse_success_rate_alert_below"]:
        alerts.append({"reason_code": "PARSE_QUALITY_LOW", "stage": "SCREENING", "severity": "P2", "observed": parse_rate})
    if family_rate is not None and family_rate < policy["job_family_match_rate_alert_below"]:
        alerts.append({"reason_code": "SOURCE_MISMATCH", "stage": "SCREENING", "severity": "P3", "observed": family_rate})

    low_yield = policy["low_shortlist_yield"]
    if metrics["unique_parseable"] >= low_yield["minimum_unique_parseable_resumes"] and metrics["shortlist"] < low_yield["minimum_shortlist_count"]:
        alerts.append({
            "reason_code": "LOW_SHORTLIST_YIELD",
            "stage": "SCREENING",
            "severity": "P2",
            "observed": {"unique_parseable": metrics["unique_parseable"], "shortlist": metrics["shortlist"], "rate": shortlist_rate},
        })

    for criterion_id, drop_rate in metrics.get("criterion_drop_rates", {}).items():
        if drop_rate > policy["single_criterion_drop_rate_alert_above"]:
            alerts.append({
                "reason_code": "CRITERION_OVER_FILTERING",
                "stage": "SCREENING",
                "severity": "P2",
                "criterion_id": criterion_id,
                "observed": drop_rate,
            })

    result = {
        "request_id": metrics["request_id"],
        "batch_id": metrics["batch_id"],
        "status": "REVIEW_REQUIRED" if alerts else "AUTOMATION_CONTINUE",
        "rates": {"parse_success": parse_rate, "job_family_match": family_rate, "shortlist_yield": shortlist_rate},
        "alerts": alerts,
    }
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
