#!/usr/bin/env python3
"""Generate a reviewable GEO bundle from an approved JSON manifest; never invent facts."""
import argparse, json
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("output")
    args = ap.parse_args()
    data = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    out = Path(args.output); out.mkdir(parents=True, exist_ok=True)
    site = data["site"]
    pages = data.get("pages", [])
    errors = []
    lines = [f"# {site['name']}", "", site.get("summary", "").strip(), ""]
    full = list(lines)
    for i, page in enumerate(pages):
        url = page.get("canonical_url", "")
        title = page.get("title", "")
        if not url.startswith(("https://", "http://")) or not title:
            errors.append({"index": i, "error": "title_or_canonical_missing"}); continue
        lines.append(f"- [{title}]({url}): {page.get('description', '').strip()}")
        full.extend([f"## {title}", "", f"Source: {url}", "", page.get("approved_markdown", "").strip(), ""])
        schema = page.get("jsonld")
        if schema:
            if schema.get("@context") != "https://schema.org" or "@type" not in schema:
                errors.append({"index": i, "url": url, "error": "invalid_jsonld_context_or_type"})
            else:
                (out / f"schema-{i:04d}.json").write_text(json.dumps(schema, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    (out / "llms.txt").write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")
    if data.get("generate_llms_full"):
        (out / "llms-full.txt").write_text("\n".join(full).rstrip()+"\n", encoding="utf-8")
    report = {"pages_received": len(pages), "errors": errors, "publishable": not errors}
    (out / "generation-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    raise SystemExit(1 if errors else 0)

if __name__ == "__main__": main()
