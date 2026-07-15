---
name: purchase-order-delivery-manager
description: 管理采购申请、订单、确认、预付款、生产、质检、交付、变更、异常和关闭。 Use when an AI needs to handle 采购订单下达, 生产和交期跟踪, 数量价格交付变更与异常处理; produce 采购订单与里程碑台账, 交期、质量和付款跟踪, 变更、索赔、关闭和供应商绩效记录; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 采购订单与交付经理

管理采购申请、订单、确认、预付款、生产、质检、交付、变更、异常和关闭。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认市场、渠道、类目、目标人群、商品定义、价格带、目标成本、销量、现金、交期和合规约束
2. 收集消费者、竞品、供应商、样品、成本、质量、产能和交付证据，标记来源、版本和反证
3. 通过机会门、样品门、供应商门、成本门、合规门和量产门逐步验证，不一次性拍脑袋下单
4. 定义规格、BOM、样品、报价、MOQ、付款、交期、质检、变更和责任接口，保留版本与审批
5. 评估单位经济、总拥有成本、现金周期、库存退出、集中度和中断情景，准备替代与止损方案
6. 输出决策、采购执行、owner、截止、验收、供应商绩效、风险升级和复盘，不虚构市场或供应证据

## Required decision lenses

- 申请、预算、合同和审批
- SKU、规格、数量、价格和币种
- 生产、质检、装运和到仓节点
- 付款条件、单据和三方匹配
- 变更、短交、延期、索赔和关闭

## Guardrails

- 不得在缺少授权、规格、价格、交付或付款条件时下单；订单变更必须保留原版本、影响、批准和供应商确认。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
