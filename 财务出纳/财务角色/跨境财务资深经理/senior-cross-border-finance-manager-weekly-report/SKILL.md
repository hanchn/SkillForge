---
name: senior-cross-border-finance-manager-weekly-report
description: 基于账务、现金、预算和税务证据生成财务周报。 Use when an AI needs to handle 财务周度复盘, 现金和营运资金预警, 关账、税务和预算事项跟踪; produce 财务周报, 现金、利润和风险摘要, 决策、责任人与下周行动; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 跨境财务资深经理周报

基于账务、现金、预算和税务证据生成财务周报。

## Load resources

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

## Workflow

1. 锁定周报周期、时区、比较口径、目标、数据截止时间和数据来源
2. 汇总本角色负责指标、关键交付、异常、决策和跨团队依赖，并验证数据完整性
3. 先写结论摘要，再按目标差距拆解规模、效率、利润、质量和风险驱动
4. 区分已完成、进行中、阻塞和待决策，所有状态绑定证据、owner 和截止时间
5. 形成下周优先级、预期影响、资源需求、护栏和需要管理层决定的事项
6. 按模板输出可持续追踪的周报，并保留口径变化、未知项和上周行动回看

## Required decision lenses

- 数据截止和关账状态
- 收入、利润和预算差异
- 现金、应收应付和库存
- 税务、汇率和申报期限
- 控制缺口与待决策事项

## Guardrails

- 不得用未关账数据冒充正式结果；必须标记预估、调整和未对账项目。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
