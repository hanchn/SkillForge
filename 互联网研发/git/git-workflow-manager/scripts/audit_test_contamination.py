#!/usr/bin/env python3
"""Read-only evidence audit for test-branch contamination in a non-test target."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys


TEST_PATH = re.compile(r"(^|/)(\.env\.test(?:\.|$)|config/test(?:/|$)|deploy/test(?:/|$)|test-environment(?:/|$))", re.I)


def git(*args: str, check: bool = True) -> str:
    proc = subprocess.run(["git", *args], text=True, capture_output=True)
    if check and proc.returncode:
        raise RuntimeError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


def is_ancestor(old: str, new: str) -> bool:
    return subprocess.run(["git", "merge-base", "--is-ancestor", old, new], capture_output=True).returncode == 0


def patch_id(commit: str) -> str | None:
    shown = subprocess.Popen(
        ["git", "show", "--pretty=format:", "--binary", commit], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    identified = subprocess.run(["git", "patch-id", "--stable"], stdin=shown.stdout, text=True, capture_output=True)
    if shown.stdout:
        shown.stdout.close()
    shown.wait()
    if shown.returncode or identified.returncode or not identified.stdout.strip():
        return None
    return identified.stdout.split()[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--test-ref", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--approved-source", action="append", default=[])
    ap.add_argument("--base")
    ns = ap.parse_args()
    try:
        for ref in [ns.test_ref, ns.target, *ns.approved_source]:
            git("rev-parse", "--verify", f"{ref}^{{commit}}")
        if ns.target == ns.test_ref:
            print("PASS: target is the configured test branch; non-test contamination rule does not apply")
            return 0
        if not ns.approved_source:
            print("WARNING: no approved development source was supplied; provenance audit is incomplete", file=sys.stderr)
            return 3
        blockers: list[str] = []
        warnings: list[str] = []
        if is_ancestor(ns.test_ref, ns.target):
            blockers.append(f"test tip {ns.test_ref} is an ancestor of non-test target {ns.target}")
        exclusions = [f"^{ref}" for ref in ns.approved_source]
        test_only = set(filter(None, git("rev-list", ns.test_ref, *exclusions).splitlines()))
        target_commits = set(filter(None, git("rev-list", ns.target).splitlines()))
        for commit in sorted(test_only & target_commits):
            blockers.append(f"test-only commit reachable from target: {commit}")
        approved_commits: set[str] = set()
        for source in ns.approved_source:
            approved_commits.update(filter(None, git("rev-list", source).splitlines()))
        approved_patch_ids = {pid for commit in approved_commits if (pid := patch_id(commit))}
        test_only_patch_ids = {
            pid: commit for commit in test_only if (pid := patch_id(commit)) and pid not in approved_patch_ids
        }
        target_candidates = target_commits - approved_commits
        for commit in target_candidates:
            pid = patch_id(commit)
            if pid and pid in test_only_patch_ids and commit != test_only_patch_ids[pid]:
                blockers.append(
                    f"target commit {commit} has a patch equivalent to test-only commit {test_only_patch_ids[pid]} ({pid})"
                )
        range_expr = f"{ns.base}..{ns.target}" if ns.base else ns.target
        for merge in filter(None, git("rev-list", "--merges", range_expr).splitlines()):
            parents = git("show", "-s", "--format=%P", merge).split()
            for parent in parents[1:]:
                if is_ancestor(parent, ns.test_ref) and not any(is_ancestor(parent, src) for src in ns.approved_source):
                    blockers.append(f"merge {merge} has a parent unique to test history: {parent}")
        if ns.base:
            paths = git("diff", "--name-only", f"{ns.base}..{ns.target}").splitlines()
            for path in paths:
                if TEST_PATH.search(path):
                    warnings.append(f"test-environment path requires content review: {path}")
        print(f"TARGET: {ns.target}")
        print(f"TEST_REF: {ns.test_ref}")
        print(f"APPROVED_SOURCES: {', '.join(ns.approved_source)}")
        for item in blockers:
            print(f"BLOCK: {item}", file=sys.stderr)
        for item in warnings:
            print(f"WARNING: {item}", file=sys.stderr)
        if blockers:
            print("SAFE_NEXT_ACTION: stop integration; identify the approved development source and rebuild the promotion from that source", file=sys.stderr)
            return 2
        if warnings:
            print("SAFE_NEXT_ACTION: review environment-specific files and prove they are safe before integration", file=sys.stderr)
            return 3
        print("PASS: no test-tip, test-only commit, or test-only merge-parent contamination detected")
        return 0
    except RuntimeError as exc:
        print("FAILED_STEP: test_contamination_audit", file=sys.stderr)
        print(f"RAW_ERROR: {exc}", file=sys.stderr)
        print("LIKELY_CAUSE: required refs or repository evidence are unavailable", file=sys.stderr)
        print("SAFE_NEXT_ACTION: fetch current refs and rerun with explicit test, target and approved source refs", file=sys.stderr)
        return 4


if __name__ == "__main__":
    raise SystemExit(main())
