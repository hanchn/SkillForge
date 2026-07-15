---
name: crm-product-architecture
description: 围绕统一客户、同意偏好、互动、服务、分群和生命周期运营设计 CRM 产品架构。 Use when an AI needs to handle 跨渠道客户中心, 营销与客服 CRM, 客户 360 和生命周期运营; produce CRM 能力地图, 客户身份与同意模型, 互动、分群、任务和集成方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# CRM 产品架构师

围绕统一客户、同意偏好、互动、服务、分群和生命周期运营设计 CRM 产品架构。

## Load resources

- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

## Workflow

1. 确认贵司缩写、业务范围、用户角色、当前系统、目标和明确不在范围内的事项
2. 从端到端业务旅程提炼能力地图，不按现有菜单、组织或数据库表直接切系统
3. 定义核心对象、标识、主数据 source of truth、状态机、命令、事件和审计要求
4. 划清本系统负责、不负责及与上下游重叠区域，建立 RACI 和数据 ownership 矩阵
5. 设计正常、异常、补偿、人工介入、对账、重放和幂等路径及跨系统 SLA
6. 按 MVP、增强、平台化阶段输出产品路线、依赖、验收、迁移和治理机制

## Required decision lenses

- 客户身份合并与冲突
- 同意、偏好和隐私请求
- 订单、互动和服务视图
- 分群、旅程和任务
- CRM 与 CDP/OMS/客服/营销工具边界

## Guardrails

- 不得把无法证明为同一人的身份强行合并，也不得绕过同意使用数据。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
