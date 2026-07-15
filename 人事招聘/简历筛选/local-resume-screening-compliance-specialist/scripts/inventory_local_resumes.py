#!/usr/bin/env python3
"""Inventory authorized local resumes without network access or default text leakage."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree

SUPPORTED = {".pdf", ".docx", ".txt", ".md"}


def docx_text(path: Path) -> tuple[str, None]:
    with zipfile.ZipFile(path) as archive:
        info = archive.getinfo("word/document.xml")
        if info.file_size > 20_000_000:
            raise ValueError("document_xml_too_large")
        root = ElementTree.fromstring(archive.read(info))
    text = "\n".join(node.text for node in root.iter() if node.tag.endswith("}t") and node.text)
    return text, None


def pdf_text(path: Path) -> tuple[str, int]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("pypdf_not_installed") from exc
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages), len(reader.pages)


def extract(path: Path, raw: bytes) -> tuple[str, int | None]:
    suffix = path.suffix.lower()
    if suffix in {".txt", ".md"}:
        return raw.decode("utf-8-sig"), None
    if suffix == ".docx":
        return docx_text(path)
    return pdf_text(path)


def secure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    os.chmod(path, 0o700)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("resume_folder", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--text-output-dir", type=Path, help="Explicitly store extracted text as private per-candidate files")
    parser.add_argument("--max-file-mb", type=int, default=25)
    args = parser.parse_args()

    root = args.resume_folder.resolve(strict=True)
    if not root.is_dir():
        parser.error("resume_folder must be a directory")

    paths = sorted(path for path in root.rglob("*") if path.suffix.lower() in SUPPORTED)
    if not paths:
        parser.error("no supported local resume files found")

    if args.text_output_dir:
        secure_directory(args.text_output_dir)
    secure_directory(args.output.parent)

    seen: dict[str, str] = {}
    rows = []
    for path in paths:
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            rows.append({
                "candidate_id": None,
                "relative_path": relative,
                "status": "PROCESSING_EXCEPTION",
                "reasons": ["SYMLINK_SKIPPED"],
            })
            continue
        if not path.is_file():
            continue
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        candidate_id = hashlib.sha256(f"{relative}\0{digest}".encode()).hexdigest()[:16]
        status = "READY"
        reasons = []
        duplicate_of = seen.get(digest)
        if duplicate_of:
            status = "REVIEW_REQUIRED"
            reasons.append("DUPLICATE_FILE")
        else:
            seen[digest] = candidate_id

        text = ""
        page_count = None
        parser_error = None
        if len(raw) > args.max_file_mb * 1024 * 1024:
            status = "PROCESSING_EXCEPTION"
            reasons.append("FILE_TOO_LARGE")
        else:
            try:
                text, page_count = extract(path, raw)
                text = re.sub(r"\r\n?", "\n", text).strip()
                if len(text) < 40:
                    status = "REVIEW_REQUIRED"
                    reasons.append("OCR_REQUIRED" if path.suffix.lower() == ".pdf" else "LOW_TEXT_VOLUME")
            except Exception as exc:  # Keep candidate content out of error logs.
                status = "PROCESSING_EXCEPTION"
                reasons.append("PARSE_FAILED")
                parser_error = type(exc).__name__

        text_path = None
        if args.text_output_dir and text:
            destination = args.text_output_dir / f"{candidate_id}.txt"
            destination.write_text(text, encoding="utf-8")
            os.chmod(destination, 0o600)
            text_path = destination.name

        rows.append({
            "candidate_id": candidate_id,
            "relative_path": relative,
            "content_sha256": digest,
            "duplicate_of_candidate_id": duplicate_of,
            "size_bytes": len(raw),
            "parser": path.suffix.lower().lstrip("."),
            "page_count": page_count,
            "text_length": len(text),
            "controlled_text_file": text_path,
            "status": status,
            "reasons": reasons,
            "parser_error_type": parser_error,
        })

    fd, temporary_name = tempfile.mkstemp(prefix=args.output.name + ".", dir=args.output.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        os.chmod(temporary_name, 0o600)
        os.replace(temporary_name, args.output)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)

    review_count = sum(row["status"] != "READY" for row in rows)
    print(f"LOCAL_ONLY files={len(rows)} review_required={review_count} output={args.output}")


if __name__ == "__main__":
    main()
