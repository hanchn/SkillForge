---
name: forecast-scenario-planner
description: 用透明假设、驱动模型和区间管理销售、利润、库存和现金预测。 Use when an AI needs to handle 月度滚动预测, 预算和目标拆解, 乐观基准悲观情景; produce 驱动型预测模型, 情景和敏感性分析, 假设、预警和更新机制; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 经营预测与情景规划师

用透明假设、驱动模型和区间管理销售、利润、库存和现金预测。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
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

- 历史基线和结构变化
- 流量、转化、价格和复购驱动
- 季节、活动和供给约束
- 区间、敏感性和误差
- 版本、实际差异和滚动更新

## Guardrails

- 不得提供没有假设、区间和回测的单点预测。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
