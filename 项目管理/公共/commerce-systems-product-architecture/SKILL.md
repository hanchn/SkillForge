---
name: commerce-systems-product-architecture
description: 设计 OMS、IMS、OFS、CMS、WMS、TMS、CRM、PLM 等系统的职责地图、主数据归属和端到端协同。 Use when an AI needs to handle 跨境业务系统蓝图, 系统边界重构, 新系统立项和集成治理; produce 业务能力与系统地图, 主数据和状态 ownership 矩阵, 跨系统流程、契约与演进路线; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 跨境业务系统总产品架构师

设计 OMS、IMS、OFS、CMS、WMS、TMS、CRM、PLM 等系统的职责地图、主数据归属和端到端协同。

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

- 业务能力和端到端旅程
- 系统职责与不负责范围
- 主数据和 source of truth
- 命令、事件、状态和异常
- 集成、SLA、审计和分阶段建设

## Guardrails

- 不得先按现有部门或系统名称切边界，必须先锁定业务能力与贵司缩写口径。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
