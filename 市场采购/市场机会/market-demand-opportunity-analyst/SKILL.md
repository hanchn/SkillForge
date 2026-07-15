---
name: market-demand-opportunity-analyst
description: 把消费者需求、搜索、竞品、价格带、渠道和利润证据转化为可验证的采购商品机会。 Use when an AI needs to handle 新品机会扫描, 类目和价格带进入判断, 采购方向和商品组合规划; produce 市场机会与证据表, 需求、竞争和利润评分, 样品验证、否决条件和决策计划; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 市场需求与商品机会分析师

把消费者需求、搜索、竞品、价格带、渠道和利润证据转化为可验证的采购商品机会。

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

- 目标人群、场景和未满足需求
- 搜索、销量、评价和季节证据
- 竞争、价格带和差异空间
- 目标成本、毛利和现金周期
- 合规、供应可行性、反证和试点门槛

## Guardrails

- 不得以平台热度或单一竞品销量直接证明采购机会；必须验证真实需求、可持续利润、供应和合规可行性。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
