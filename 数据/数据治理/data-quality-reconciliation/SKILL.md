---
name: data-quality-reconciliation
description: 验证完整性、唯一性、及时性、一致性并解释跨系统差异。 Use when an AI needs to handle 平台与财务对账, 看板数据验收, 异常数据和口径争议; produce 数据质量报告, 差异桥和根因, 修复、监控和责任清单; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 业务数据质量与对账专家

验证完整性、唯一性、及时性、一致性并解释跨系统差异。

## Load resources

- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

## Workflow

1. 先确认业务问题、决策人、比较口径、日期范围、时区、币种、订单状态和分析粒度
2. 建立数据来源清单，检查完整性、唯一性、迟到、回补、抽样和跨系统可对账性
3. 写出指标公式、维度 scope、过滤和去重规则；不一致时先做差异桥
4. 按总量到分层、相关到驱动、现象到反证推进分析，保留可复算过程
5. 量化不确定性、样本限制、归因偏差和不可比项，区分事实、推断和建议
6. 输出结论先行报告、证据表、影响规模、优先动作、owner 与后续监控

## Required decision lenses

- 来源、抽取时间和范围
- 主键、重复和缺失
- 状态、时区、币种和税
- 迟到、回补和快照
- 容差、证据和 owner

## Guardrails

- 不得用手工调平掩盖未解释差异。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
