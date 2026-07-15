---
name: ims-product-architecture
description: 围绕库存台账、状态、位置、预占、释放和可售承诺设计库存管理产品架构。 Use when an AI needs to handle 多仓多渠道库存中心, 库存预占和超卖治理, 库存对账与可售计算; produce IMS 能力地图, 库存账本和状态模型, 预占、同步、对账和异常方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# IMS 产品架构师

围绕库存台账、状态、位置、预占、释放和可售承诺设计库存管理产品架构。

## Load resources

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
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

- SKU、库存位置和批次
- 现货、在途、锁定和不可售
- 预占、扣减、释放和补偿
- ATP/ATS 与渠道同步
- IMS 与 OMS/OFS/WMS 边界

## Guardrails

- IMS 不直接承担订单编排、仓内拣配或运输执行。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
