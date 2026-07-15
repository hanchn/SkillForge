---
name: amazon-pdp-import-generator
description: Parse structured product-image filenames into grouped Amazon product and variation drafts, choose main and supporting images, generate CSV and XLSX review files, and then draft listing content only from verified product facts. Use when an AI needs to turn an image folder into a reviewable Amazon PDP import draft, diagnose SKU and image grouping, prepare parent-child variation data, or create marketplace-specific listing copy without inventing materials, claims, certifications, dimensions, or compliance status.
---

# Amazon PDP Import Generator

Use deterministic parsing for files and evidence-controlled generation for copy.

## Workflow

1. Read skill.json, INVOCATION.md, assets/parser_config.json, and the target marketplace requirements supplied by the user.
2. Inspect a sample of filenames and confirm the naming pattern, SKU identity, variation attributes, and image-role vocabulary.
3. Run scripts/generate_pdp_import.py on the image folder. Do not manually recreate the parser output.
4. Review parse_log.csv and low-confidence rows before drafting content. Correct configuration or filenames when grouping is wrong.
5. Treat inferred product type, color, and image role as provisional until verified against source facts.
6. Build a product fact ledger from supplied specifications, packaging, test records, policies, and marketplace data. Separate facts per child variation.
7. Draft title, bullets, description, and search terms for the target marketplace and category. Keep claims within the verified ledger and requested style.
8. Validate parent-child consistency, unique child SKU, variation theme, main-image choice, prohibited duplication, field limits, and missing required attributes.
9. Return both machine files and a human review summary. State that marketplace template mapping and category compliance still require Seller Central or current official-template validation when not provided.

## Guardrails

- Do not infer material, size, performance, certification, compatibility, origin, audience, warranty, or safety claims from an image or filename.
- Do not call the generic draft upload-ready unless it has been mapped to the current marketplace and category template.
- Do not silently merge ambiguous SKUs or colors; retain parse confidence and request review.
- Do not use competitor trademarks or unsupported superlatives.
- Preserve source filenames and parsing logs so every row can be audited.

## Output contract

Return output file paths, parse summary, low-confidence and conflicting rows, missing factual attributes, content-generation status, marketplace-template caveats, and the exact human checks still required.
