#!/usr/bin/env python3
"""Render reviewable platform payloads. This script never sends network requests."""
import argparse, json
from pathlib import Path

REQUIRED = {"event_id", "dedup_key", "title", "summary", "severity", "status", "occurred_at", "source", "owner"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("event", type=Path)
    ap.add_argument("platform", choices=["feishu", "dingtalk", "wecom", "enterprise-qq"])
    ap.add_argument("--output", type=Path, required=True)
    ns = ap.parse_args()
    event = json.loads(ns.event.read_text(encoding="utf-8"))
    missing = sorted(REQUIRED - set(event))
    if missing: raise SystemExit("missing required event fields: " + ", ".join(missing))
    text = f"[{event['severity']}] {event['title']}\n{event['summary']}\n状态: {event['status']}\nOwner: {event['owner']}\n时间: {event['occurred_at']}"
    if event.get("action_url"): text += f"\n处理链接: {event['action_url']}"
    if ns.platform == "feishu":
        result = {"platform": "feishu", "send_authorized": False, "payload": {"msg_type": "text", "content": {"text": text}}}
    elif ns.platform == "dingtalk":
        result = {"platform": "dingtalk", "send_authorized": False, "payload": {"msgtype": "markdown", "markdown": {"title": event["title"], "text": text}, "at": {"isAtAll": False}}}
    elif ns.platform == "wecom":
        result = {"platform": "wecom", "send_authorized": False, "payload": {"msgtype": "markdown", "markdown": {"content": text}}}
    else:
        result = {"platform": "enterprise-qq", "send_authorized": False, "status": "REVIEW_REQUIRED", "reason": "requires current official or company gateway contract", "normalized_event": event}
    ns.output.parent.mkdir(parents=True, exist_ok=True)
    ns.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"DRY_RUN_ONLY platform={ns.platform} output={ns.output}")

if __name__ == "__main__": main()
