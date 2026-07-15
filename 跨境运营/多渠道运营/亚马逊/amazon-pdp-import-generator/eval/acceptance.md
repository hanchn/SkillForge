# Acceptance

## Parser

- [ ] Empty directories fail clearly and produce no fabricated rows.
- [ ] Hyphen, underscore, multi-image, unknown-role, and missing-color cases are covered.
- [ ] Every source image appears in the parse log and exactly one grouped SKU unless rejected.
- [ ] Main-image selection is deterministic and supporting images retain stable order.
- [ ] CSV and XLSX open correctly and contain the same product rows.
- [ ] Low-confidence rows are visible and not silently promoted as verified.

## Listing content

- [ ] Each material claim traces to supplied product facts.
- [ ] Parent and child attributes are consistent with the variation theme.
- [ ] Titles, bullets, descriptions, and search terms match the target marketplace and category constraints provided.
- [ ] No unsupported material, performance, certification, safety, warranty, origin, or compatibility claim appears.
- [ ] Generic output is described as a review draft, not guaranteed upload-ready.
