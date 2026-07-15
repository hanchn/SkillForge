---
name: inventory-replenishment-planner
description: Plan multi-channel ecommerce inventory and replenishment using demand, seasonality, promotions, lead-time distributions, safety stock, service levels, inbound stages, channel allocation, storage constraints, cash limits, and stockout or overstock risk. Use when an AI needs to decide what, when, and how much to reorder for Amazon FBA, FBM, 3PL, or owned storefront inventory.
---

# 多渠道库存补货规划师

补货不是销售均值乘交期，而是需求和供应不确定性下的资金配置。

## Load resources

- Read references/replenishment-method.md before analysis or execution.
- Use assets/replenishment-plan-template.md for the final plan and handoff.

## Workflow

1. 锁定 SKU、地点、渠道、可售与不可售库存、在途阶段、预留、历史区间和计划窗口
2. 清洗缺货截断、异常促销、批量订单、退货和新品冷启动影响
3. 建立基准需求并分离趋势、季节、活动、价格和渠道迁移
4. 用实际生产、质检、干线、清关、预约和入仓分布建模补货提前期
5. 设定服务水平、安全库存、订货点、目标库存天数和最大资金/仓储约束
6. 按库存位置和渠道需求分配现货与在途，处理 FBA、3PL、FBM 和独立站共享库存
7. 生成基准、上行、下行情景以及加急、延迟、活动超卖和供应中断方案
8. 列出下单量、最晚下单日、运输方式、预计到货、缺货概率和过量风险
9. 定义每周滚动更新、预测偏差、sell-through、库存年龄和例外告警

## Guardrails

- 不得把采购在途、海运在途、入仓中和可售库存混为一体
- 不得用缺货期的销量直接代表真实需求
- 不得在没有资金、仓储和生命周期约束时只追求零缺货
- 预测必须提供误差或情景，不给单点伪精确答案

## Output contract

Return the decision context, evidence and assumptions, analysis or plan, prioritized actions, owners and dependencies, acceptance or decision thresholds, risks, and the next review point. Keep observed facts separate from estimates and recommendations.
