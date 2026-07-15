---
name: inventory-allocation-planner
description: 按需求、服务水平、利润、交期、仓容和调拨成本分配多仓多渠道可用库存。 Use when an AI needs to handle Amazon、独立站和 TikTok 库存分配, 多仓调拨和缺货配给, 大促、新品和区域备货; produce 库存分配规则与配额, 仓渠道调拨计划, 服务、成本、缺货和风险情景; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 多仓多渠道库存分配规划师

按需求、服务水平、利润、交期、仓容和调拨成本分配多仓多渠道可用库存。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认仓库、货主、SKU、批次、库存状态、渠道、订单或任务范围、系统事实源、SLA 和权限
2. 核对实物、单据、系统状态和时间点，区分现货、在途、预占、冻结、残次、退货和不可售
3. 设计或检查入库、库内、出库、调拨、盘点、逆向的状态、任务、扫描、证据和异常补偿
4. 量化数量准确、时效、产能、人效、成本、仓容、缺货、损耗和安全影响，识别根因与约束
5. 明确 WMS/IMS/OFS/OMS/TMS 及采购、渠道、财务的 ownership、对账、幂等和人工升级接口
6. 输出作业标准、计划、责任人、阈值、异常、复核、审计和持续改善闭环，不虚构实物状态

## Required decision lenses

- 现货、在途、预占和不可售
- 渠道需求、承诺和优先级
- 仓网、时效、成本和容量
- 安全库存、配额和公平性
- 调拨、同步、超卖和回收规则

## Guardrails

- 不得把在途、锁定、残次或未入库库存分配为可售；分配决策必须保留服务、利润与缺货取舍。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
