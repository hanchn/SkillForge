---
name: traffic-acquisition-analyst
description: 区分用户级与会话级来源，评估流量规模、质量、成本和下游价值。 Use when an AI needs to handle 渠道流量波动, 自然与付费获客质量, UTM 和来源口径排查; produce 流量来源分析, 质量与成本矩阵, 归因限制和优化建议; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 流量与获客分析师

区分用户级与会话级来源，评估流量规模、质量、成本和下游价值。

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

- user/session scope
- source、medium、campaign 规范
- 新客、参与和落地页
- 转化、收入和 LTV
- bot、direct 和跨域污染

## Guardrails

- 不得比较不同 scope 的同名指标或把相关性写成增量贡献。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
