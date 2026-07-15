---
name: api-contract-designer
description: Design and review stable HTTP or event API contracts, including resources, operations, schemas, validation, errors, pagination, idempotency, concurrency, compatibility, authorization boundaries, and rollout plans. Use when an AI needs to create or repair an OpenAPI-oriented contract, review backend endpoint design, define integration behavior, evolve an existing API without breaking clients, or turn product requirements into an implementation-ready interface specification.
---

# API Contract Designer

Design from consumer behavior and invariants before choosing paths or field names.

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/contract-checklist.md for HTTP and event-specific checks.
- Use assets/api-review-template.md for the final design or review record.

## Workflow

1. Inspect the domain model, consumers, trust boundaries, current conventions, existing schemas, and compatibility constraints.
2. Record invariants and lifecycle states. Distinguish commands, resource reads, searches, and asynchronous events.
3. Model the smallest stable public contract. Keep internal storage and service topology out of the interface.
4. Define each operation's authorization, request schema, validation, success response, failure responses, side effects, retry behavior, and observability correlation.
5. Specify collection semantics: filtering operators, stable sort, cursor or offset rules, page limits, and empty results.
6. Specify mutation semantics: idempotency, deduplication window, optimistic concurrency, partial failure, atomicity, and replay safety.
7. Build one canonical error envelope with stable machine codes and safe human messages. Do not leak stack traces or secrets.
8. Check schema evolution: required versus optional fields, nullable semantics, enum expansion, unknown fields, deprecation, and version negotiation.
9. Provide complete representative examples, including at least one success and each materially different failure class.
10. Finish with unresolved decisions, compatibility risks, rollout order, and consumer test obligations.

## Design rules

- Reuse repository conventions when they exist; identify inconsistency instead of silently inventing a new style.
- Use nouns for resources and explicit action endpoints only when the operation is not naturally resource-shaped.
- Treat omission, null, empty string, zero, and empty collection as distinct unless the domain declares otherwise.
- Never promise exactly-once delivery. State the deduplication or at-least-once behavior actually supported.
- Avoid breaking changes disguised as cleanup, including narrowed types, new required fields, changed defaults, reordered semantics, or removed enum values.
- Do not create fake implementation details when only a contract is requested.

## Output contract

Return assumptions and invariants first, then the operation table, schemas, validation, error catalog, examples, security and compatibility notes, and rollout plan. When requested, render an OpenAPI or AsyncAPI skeleton, but keep unresolved choices visibly marked rather than fabricating values.
