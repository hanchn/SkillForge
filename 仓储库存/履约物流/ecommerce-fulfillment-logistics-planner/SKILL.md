---
name: ecommerce-fulfillment-logistics-planner
description: Design and compare ecommerce freight, customs, receiving, warehousing, FBA, FBM, 3PL, direct fulfillment, returns, and delivery operations using landed cost, service level, dimensional weight, capacity, exception handling, and resilience. Use when an AI needs to choose shipping modes, plan inbound calendars, compare fulfillment networks, reduce delivery failures, or prepare Amazon and owned-store logistics operations.
---

# 电商履约物流规划师

物流方案必须同时满足成本、时效、可追踪、合规、容量和异常恢复。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/logistics-decision-checklist.md before analysis or execution.
- Use assets/fulfillment-plan-template.md for the final plan and handoff.

## Workflow

1. 确认产品尺寸重量、危险或特殊属性、起运地、目的市场、渠道、销量、承诺时效和退货要求
2. 建立端到端节点图：工厂、质检、提货、出口、干线、清关、仓库、FBA/3PL、最后一公里和逆向物流
3. 统一比较计费重、体积重、固定费、操作费、关税税费、仓储、退货、丢损和加急成本
4. 用低中高时效和波动评估海运、空运、快递、铁路或本地备货组合
5. 设计 FBA、FBM、3PL 和独立站订单路由、库存缓冲、分单、缺货和峰值容量
6. 定义标签、箱规、预约、ASN、追踪、POD、清关文件和数据交接责任
7. 建立延误、扣关、拒收、丢件、破损、地址错误、仓库爆仓和承运商中断 playbook
8. 输出首选、备选、验证批次、时间表、成本区间、SLA 和切换阈值
9. 用准时率、交付时长、成本/单、损坏、丢件、退款、首次投递和仓库差错复盘

## Guardrails

- 不得用基础运价代替完整落地与履约成本
- 不得忽略体积重、旺季、偏远、燃油、仓储和退货费用
- 不得承诺承运商无法保证的时效
- 涉及海关、危险品和税务时必须使用当前专业规则并标记责任人

## Output contract

Return the decision context, evidence and assumptions, analysis or plan, prioritized actions, owners and dependencies, acceptance or decision thresholds, risks, and the next review point. Keep observed facts separate from estimates and recommendations.
