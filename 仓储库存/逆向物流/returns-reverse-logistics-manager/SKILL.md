---
name: returns-reverse-logistics-manager
description: 管理退货授权、运输、收货、检验、分级、退款证据、翻新、再售、报废和供应商追偿。 Use when an AI needs to handle 客户退货处理, 平台退仓和批量逆向, 残次、翻新、再售与报废治理; produce 逆向流程与状态机, 检验分级和处置标准, 退款、库存、追偿和根因报告; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 退货与逆向物流经理

管理退货授权、运输、收货、检验、分级、退款证据、翻新、再售、报废和供应商追偿。

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

- RMA、订单、原因和责任
- 运输、收货、身份和完整性
- 检验、分级、清洁和翻新
- 退款、可售、残次、报废和销毁
- 欺诈、产品安全、数据清除和根因闭环

## Guardrails

- 不得未经检验把退货恢复可售；涉及安全、卫生、个人数据或召回的商品必须隔离并按专项规则处置。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
