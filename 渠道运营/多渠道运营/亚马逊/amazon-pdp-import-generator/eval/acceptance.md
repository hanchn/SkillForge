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

## Market Rank and trend evidence

- [ ] Target marketplace, category, language, price band, query set and collection time are explicit.
- [ ] BSR, organic query position, sponsored position and trend-list rank are recorded as different metrics.
- [ ] Competitors are relevant by product, audience, use case and price band, not selected only by rank.
- [ ] Every current or real-time claim has a source and timestamp from this execution.
- [ ] A 7/30/90-day trend is reported only when dated history exists; a single snapshot is not called a trend.

## SEO and GEO

- [ ] Before copy generation, the user was asked whether a keyword library exists and whether supplied keywords should be prioritized.
- [ ] The selected priority mode is recorded as `REQUIRED_CANDIDATE`, `PREFERRED`, `REFERENCE_ONLY`, or `NO_PRIORITY`.
- [ ] User-priority keywords were still screened for product relevance, facts, field rules, competitor marks, prohibited wording and natural readability.
- [ ] Excluded user keywords have explicit reasons instead of being silently ignored.
- [ ] Keyword candidates trace to product facts, search suggestions, authorized analytics or current market evidence.
- [ ] Each keyword has intent, relevance, evidence, target field and inclusion/exclusion decision.
- [ ] Title, bullets, description and backend terms avoid irrelevant volume terms, stuffing, mechanical repetition and competitor brands.
- [ ] GEO coverage includes verified entities, attributes, use cases and concise factual answers without promising AI citation.
- [ ] Parent and child listings use consistent vocabulary while preserving real variation differences.

## Self-check

- [ ] `assets/pdp-self-check-checklist.md` was completed after the final draft.
- [ ] Fact, SEO, GEO, field-limit, duplication, variation, image, compliance, localization and template checks passed or are explicitly blocked.
- [ ] Failed checks were repaired and rerun; unresolved items have an owner and prevent upload-ready claims.
