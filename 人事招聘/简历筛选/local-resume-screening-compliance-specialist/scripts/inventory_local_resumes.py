#!/usr/bin/env python3
"""Read-only local resume inventory and text extraction. No network access."""
from __future__ import annotations
import argparse, hashlib, json, os, re, zipfile
from pathlib import Path
from xml.etree import ElementTree

SUPPORTED = {".pdf", ".docx", ".txt", ".md"}

def docx_text(path):
    with zipfile.ZipFile(path) as z:
        root = ElementTree.fromstring(z.read("word/document.xml"))
    return "\n".join(t.text for t in root.iter() if t.tag.endswith("}t") and t.text)

def pdf_text(path):
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("pypdf_not_installed") from exc
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("resume_folder", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--metadata-only", action="store_true")
    ns = ap.parse_args()
    files = sorted(p for p in ns.resume_folder.rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED)
    if not files: ap.error("no supported local resume files found")
    seen = {}
    rows = []
    for path in files:
        raw = path.read_bytes(); digest = hashlib.sha256(raw).hexdigest()
        status = "READY"; reasons = []
        if digest in seen: status = "REVIEW_REQUIRED"; reasons.append("DUPLICATE_FILE")
        seen.setdefault(digest, path.as_posix())
        text = ""
        try:
            if path.suffix.lower() in {".txt", ".md"}: text = raw.decode("utf-8")
            elif path.suffix.lower() == ".docx": text = docx_text(path)
            else: text = pdf_text(path)
            text = re.sub(r"\r\n?", "\n", text).strip()
            if len(text) < 40: status = "REVIEW_REQUIRED"; reasons.append("OCR_REQUIRED" if path.suffix.lower()==".pdf" else "PARSE_FAILED")
        except Exception as exc:
            status = "REVIEW_REQUIRED"; reasons.append("PARSE_FAILED:" + type(exc).__name__)
        row = {"candidate_id": digest[:16], "relative_path": path.relative_to(ns.resume_folder).as_posix(), "sha256": digest, "size_bytes": len(raw), "parser": path.suffix.lower(), "text_length": len(text), "status": status, "reasons": reasons}
        if not ns.metadata_only: row["local_extracted_text"] = text
        rows.append(row)
    ns.output.parent.mkdir(parents=True, exist_ok=True)
    with ns.output.open("w", encoding="utf-8") as handle:
        for row in rows: handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    os.chmod(ns.output, 0o600)
    print(f"LOCAL_ONLY files={len(rows)} review_required={sum(r['status']!='READY' for r in rows)} output={ns.output}")

if __name__ == "__main__": main()
