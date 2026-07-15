---
name: multi-currency-treasury-manager
description: 管理多币种账户、平台结算、汇率暴露、换汇、流动性和资金权限。 Use when an AI needs to handle 多币种现金管理, 平台结算和换汇优化, 汇率风险和资金安全治理; produce 币种资金头寸, 汇率暴露与情景, 换汇、归集、权限和预警方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 多币种资金与汇率经理

管理多币种账户、平台结算、汇率暴露、换汇、流动性和资金权限。

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

- 账户、主体和币种
- 应收应付自然对冲
- 结算周期和费用
- 汇率情景与风险限额
- 付款权限、欺诈和银行连续性

## Guardrails

- 不得把预测汇率当事实，不得未经授权执行交易或提供投机建议。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
