# Risk Model

Score each factor from 1 to 5 and preserve the rationale.

- Likelihood: probability of failure under realistic use
- Impact: harm to users, money, data, security, compliance, or operations
- Detectability: difficulty of detecting before harm; 5 means difficult
- Blast radius: number of users, tenants, records, or systems affected

Use the score to rank attention, not to manufacture certainty. A known catastrophic path can remain top priority even when likelihood is low.

## Layer selection

- Static: syntax, types, policy, dependency, and configuration defects
- Unit: pure logic, boundaries, property invariants, error mapping
- Component: service behavior with controlled dependencies
- Contract: consumer-provider schema and semantic compatibility
- Integration: real databases, queues, identity, vendors, and migrations
- End-to-end: a small number of critical user journeys
- Exploratory: unknown interaction and usability risk
- Performance, security, resilience: specialist failure modes and limits
- Production verification: environment-specific behavior and rollout safety

Choose the lowest layer that reproduces the risk and provides a trustworthy oracle.
