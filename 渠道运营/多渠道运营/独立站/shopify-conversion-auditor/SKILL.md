---
name: shopify-conversion-auditor
description: Audit Shopify storefront conversion using page evidence, analytics context, merchandising facts, mobile behavior, trust signals, offer clarity, product detail quality, cart and checkout friction, performance, accessibility, and measurement integrity. Use when an AI needs to diagnose low conversion, review a Shopify home, collection, product, cart, or checkout journey, prioritize CRO work, compare store variants, or turn screenshots, URLs, theme code, and funnel metrics into an evidence-backed action plan.
---

# Shopify Conversion Auditor

Connect visible friction to a customer decision and a measurable funnel outcome.

## Load resources

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/audit-framework.md before scoring a store.
- Use assets/audit-scorecard.md for the final prioritized backlog.

## Evidence gate

Use the strongest available evidence in this order: observed live page and mobile interaction, analytics and session evidence, theme or app configuration, screenshots or recordings, then user description. State which surfaces and locales were inspected. Never claim an element is absent if it may be hidden by device, market, login, consent, or experiment state.

## Workflow

1. Record store goal, target market, traffic mix, device mix, product category, price point, conversion definition, and current funnel metrics when available.
2. Walk the primary journey from landing page through collection, product, cart, and checkout. Capture evidence at the point of friction.
3. Evaluate message match, product findability, offer comprehension, variant selection, sizing or fit, imagery, proof, shipping and return clarity, urgency, trust, and total-cost surprises.
4. Check mobile usability, accessibility, performance symptoms, localization, currency, inventory messaging, discount behavior, and app interference.
5. Verify analytics instrumentation before using funnel numbers. Flag duplicate events, missing steps, inconsistent definitions, consent effects, and incomplete periods.
6. Write each finding as evidence, affected customer question, expected behavior impact, affected funnel stage, confidence, and reach.
7. Score opportunity using impact, reach, confidence, effort, and reversibility. Keep quick fixes separate from structural experiments.
8. Recommend a specific change with owner, dependency, acceptance criteria, guardrail, and measurement plan.
9. Avoid simultaneous tests that contaminate the same decision point. Define primary metric, guardrails, minimum runtime logic, and segment checks.
10. End with the top three actions and the evidence needed to validate lower-confidence items.

## Audit rules

- Do not confuse aesthetic preference with conversion evidence.
- Do not recommend fake scarcity, deceptive countdowns, fabricated reviews, hidden fees, or accessibility regressions.
- Do not prescribe universal best practices when brand, category, market, or traffic intent changes the tradeoff.
- Separate acquisition-message problems from onsite conversion problems.
- Treat price, shipping, returns, payment methods, and delivery promises as factual claims that must be verified.
- Use real product and store facts; do not invent promotions, policies, certifications, or customer proof.



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。

## Output contract

Lead with the largest verified conversion obstacles. Include evidence inventory, journey findings, prioritized scorecard, recommended changes, test plans, instrumentation issues, constraints, and open questions. Tie every priority to a funnel stage and acceptance criterion.
