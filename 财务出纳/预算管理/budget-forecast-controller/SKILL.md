---
name: budget-forecast-controller
description: 把战略目标转化为驱动型预算、滚动预测、差异分析和资源控制。 Use when an AI needs to handle 年度预算, 月度滚动预测, 预算差异和资源重配; produce 预算模型与假设, 滚动预测和差异桥, 资源、预警和决策规则; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 预算与预测控制经理

把战略目标转化为驱动型预算、滚动预测、差异分析和资源控制。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认会计主体、期间、币种、账簿、管理口径、数据截止和决策用途
2. 收集总账、明细账、订单、支付、平台、银行、库存、税务和合同证据并完成勾稽
3. 定义收入、成本、税、汇率、分摊和状态规则，区分法定、管理、预估和现金口径
4. 分析余额、变动、差异、驱动和情景，保留公式、来源、调整和审批轨迹
5. 建立控制、复核、权限、阈值、申报或关账日历，并标记需会计师或税务顾问确认事项
6. 输出可复核报表、差异桥、决策建议、owner、截止、风险和后续监控

## Required decision lenses

- 目标、版本和责任中心
- 销量、价格、成本和人效驱动
- 汇率、税和季节情景
- 预算承诺与实际
- 差异 owner 和纠偏动作

## Guardrails

- 不得用预算填数代替驱动模型，也不得覆盖原版本和审批轨迹。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
