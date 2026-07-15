---
name: test-strategy-designer
description: Create risk-based test strategies, coverage matrices, release gates, environment plans, test data plans, observability checks, and focused regression suites for product and engineering changes. Use when an AI needs to plan testing for a feature, API, migration, incident fix, release, or integration; review whether a test plan is sufficient; or convert requirements and architecture into executable verification priorities.
---

# Test Strategy Designer

Optimize for risk reduction and diagnostic value, not maximum test count.

## Load resources

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/risk-model.md before prioritizing coverage.
- Use assets/test-strategy-template.md for a shareable test plan.

## Workflow

1. Inspect requirements, changed components, architecture, dependencies, incidents, usage criticality, and release constraints.
2. Build a change-impact map from user journey to service, data, dependency, and operational effect.
3. Create a risk register. Score likelihood, impact, detectability, and blast radius; record why each score is justified.
4. Assign the cheapest reliable test layer to each risk: static, unit, component, contract, integration, end-to-end, exploratory, performance, security, resilience, or production verification.
5. Define test data, identities, permissions, clocks, locales, feature flags, and environment dependencies. Include cleanup and isolation rules.
6. Create a coverage matrix with happy path, boundaries, invalid input, state transitions, concurrency, retries, partial failure, rollback, and backward compatibility where relevant.
7. Define oracles: exact expected outputs, invariants, logs, traces, metrics, and database effects. Avoid steps that only say verify it works.
8. Separate blocking release gates from non-blocking observations. Give every gate an owner, evidence source, and stop condition.
9. Define a focused regression set based on touched contracts and shared dependencies.
10. Add post-release checks and rollback signals for risks that cannot be fully reproduced before production.

## Planning rules

- Do not repeat the same scenario at every layer without a distinct purpose.
- Do not assume a staging environment is production-equivalent; list meaningful differences.
- Use pairwise or boundary techniques for combinatorial inputs and explain the chosen reduction.
- Prefer deterministic setup and assertions. Isolate flaky external dependencies or state why they remain live.
- Mark security, privacy, financial, destructive, and irreversible paths as high impact by default.
- Trace each must-cover risk to at least one test and one observable oracle.



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。

## Output contract

Return scope and evidence, risk register, layer strategy, coverage matrix, environments and data, release gates, regression suite, production verification, exclusions, and open decisions. When reviewing an existing plan, lead with uncovered high-risk behavior and redundant low-value coverage.
