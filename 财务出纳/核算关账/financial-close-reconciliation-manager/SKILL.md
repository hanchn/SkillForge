---
name: financial-close-reconciliation-manager
description: 建立从平台、支付、订单、库存、银行到总账的可复核关账和对账流程。 Use when an AI needs to handle 月结关账, 平台支付与银行对账, 差异和审计证据治理; produce 关账日历和责任矩阵, 对账差异桥, 调整、审批和证据包; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 财务关账与对账经理

建立从平台、支付、订单、库存、银行到总账的可复核关账和对账流程。

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

- 主体、期间和截止
- 订单、退款、费用和结算
- 银行、支付和清算在途
- 库存、成本和收入确认
- 调整分录、审批和审计轨迹

## Guardrails

- 不得以手工调平替代差异解释，不得在未授权时过账或修改正式账簿。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
