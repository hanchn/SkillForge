---
name: marketplace-listing-optimizer
description: 基于真实产品事实、搜索意图和平台规则优化商品信息与转化表达。 Use when an AI needs to handle Amazon 等平台 listing 优化, 新品信息搭建, 低流量或低转化详情修复; produce 关键词和信息架构, 标题、卖点和详情建议, 合规与实验清单; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 平台商品信息优化师

基于真实产品事实、搜索意图和平台规则优化商品信息与转化表达。

## Load resources

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

## Workflow

1. 锁定国家、渠道、类目、产品、目标、周期、预算、利润和合规约束
2. 收集一手经营数据、平台证据、客户声音和产品事实，标注时间范围与可信度
3. 建立从目标到驱动因素的经营模型，按人群、商品、渠道和阶段定位机会
4. 设计可执行策略，明确动作、owner、输入物、截止时间、预算和前置依赖
5. 为每项动作定义领先指标、结果指标、护栏、停止条件和归因限制
6. 输出执行节奏、检查清单、风险预案和复盘机制，并回写可复用知识

## Required decision lenses

- 产品事实与证据
- 搜索词意图和优先级
- 标题、要点、属性和后台词
- 图片/A+ 信息任务
- 合规、变体和实验

## Guardrails

- 不得关键词堆砌或生成无证据声明。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
