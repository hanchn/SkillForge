# Requirement Quality Gates

## Problem gate

- Names an affected actor and an observable failure.
- Includes evidence or labels the claim as an assumption.
- Explains why the issue matters now without using the proposed feature as justification.

## Scope gate

- In-scope and out-of-scope behavior is explicit.
- Dependencies, permissions, lifecycle states, and migration needs are visible.
- Non-goals prevent adjacent expectations from entering unnoticed.

## Requirement gate

- Each requirement has one primary behavior and a stable identifier.
- Inputs, outputs, rules, errors, state changes, and audit effects are testable.
- Terms are defined once and used consistently.

## Acceptance gate

- Criteria are observable from the user, API, event, data, or operational surface.
- Boundaries, failure modes, and permission differences are covered.
- A tester can decide pass or fail without guessing intent.

## Decision gate

- Unknowns have owners or a clear next source.
- Metrics identify baseline, threshold, window, and guardrail.
- Traceability shows no orphan requirement or unsupported feature.
