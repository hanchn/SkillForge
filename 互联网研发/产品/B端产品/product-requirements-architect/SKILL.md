---
name: product-requirements-architect
description: Turn ambiguous product ideas, feature requests, workflow changes, and B2B product proposals into review-ready requirement packages with problem framing, actors, scope, business rules, states, edge cases, acceptance criteria, metrics, and open decisions. Use when an AI needs to write or repair a PRD, clarify a feature before design or engineering, decompose a complex workflow, or check whether requirements are implementable and testable.
---

# Product Requirements Architect

Produce a decision-ready requirements package. Do not hide uncertainty behind polished prose.

## Load resources

- Read references/quality-gates.md before drafting or reviewing a requirements package.
- Use assets/prd-template.md when the user wants a complete PRD artifact.

## Workflow

1. Inspect the supplied brief, existing product evidence, terminology, constraints, and requested output shape.
2. Separate confirmed facts, assumptions, unresolved decisions, and exclusions. Preserve the user's business language.
3. State the problem as an observable user or business failure. Avoid using the proposed feature as the problem statement.
4. Identify actors, jobs, entry conditions, permissions, system boundaries, and the happy-path state transition.
5. Define scope with explicit in-scope, out-of-scope, dependencies, and non-goals.
6. Write numbered functional requirements. Attach business rules, data needs, error handling, permissions, audit needs, and edge cases to the relevant requirement.
7. Express acceptance criteria as externally observable outcomes. Use Given/When/Then only when it improves precision.
8. Define success metrics with baselines, targets or decision thresholds, observation windows, and guardrails. Mark missing values as decisions, not invented numbers.
9. Add a traceability table mapping each user problem to requirements, acceptance criteria, and metrics.
10. End with prioritized open decisions, named decision owners when known, and the consequence of leaving each unresolved.

## Evidence rules

- Cite source files, tickets, interviews, screenshots, or user statements beside claims when evidence exists.
- Label inference and assumption explicitly.
- Do not invent APIs, policies, deadlines, legal requirements, baselines, or stakeholder approval.
- If the request is underspecified, draft the stable sections and isolate only the decisions that truly block implementation.

## Quality bar

- Make every requirement atomic enough to review and test.
- Describe states and transitions for workflows with approval, retries, cancellation, expiry, or partial completion.
- Distinguish validation errors, permission failures, dependency failures, and empty states.
- Keep solution details out unless they are actual constraints or the user asks for a technical design.
- Reject vague acceptance language such as fast, easy, supports, optimized, or user-friendly without an observable measure.

## Output contract

Return a concise executive summary followed by the requested artifact. Include scope, actors, flow, numbered requirements, rules and edge cases, acceptance criteria, metrics, risks, traceability, and open decisions. If reviewing an existing PRD, preserve its structure and produce a gap list before proposing rewrites.

