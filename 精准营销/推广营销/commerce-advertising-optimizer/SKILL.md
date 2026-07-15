---
name: commerce-advertising-optimizer
description: Diagnose and optimize Amazon Ads and owned-store paid media using business objectives, clean attribution, query and audience intent, campaign structure, bids, budgets, creative, landing-page readiness, incrementality, contribution margin, and controlled experiments. Use when an AI needs to audit Sponsored Products or other commerce campaigns, reduce wasted spend, scale profitable demand, or distinguish ad problems from listing, price, inventory, or conversion problems.
---

# 多渠道电商广告优化师

先判断流量、转化还是利润问题，再动出价；平台归因不是增量利润。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/advertising-diagnostic-checklist.md before analysis or execution.
- Use assets/advertising-action-plan.md for the final plan and handoff.

## Workflow

1. 确认市场、渠道、广告类型、目标、归因窗口、时间口径、利润底线和库存状态
2. 校验花费、点击、订单、销售、新客、退款和自然销售数据，标记平台归因与业务口径差异
3. 按漏斗定位问题：曝光不足、点击不足、详情页转化不足、客单/复购不足或利润不足
4. 拆解搜索词、关键词、商品、受众、版位、设备、地域、创意、落地页和新老客表现
5. 计算 CPC、CTR、CVR、CPA、ACOS/ROAS、TACOS、边际贡献和 break-even 阈值
6. 隔离品牌防守、类目拓展、竞品、再营销和新品学习预算，避免混合目标互相补贴
7. 制定否词、目标迁移、竞价、预算、创意、商品页和落地页动作，说明预期机制
8. 一次实验改变有限变量，定义主指标、guardrail、最小运行逻辑和停止条件
9. 检查库存、Buy Box/可售性、价格、优惠和页面质量，避免为无法转化的商品买流量
10. 输出扩量、修复、观察或暂停结论，并安排复盘窗口

## Guardrails

- 不得只用平台 ROAS 宣称盈利或增量
- 不得在低样本下频繁调价造成学习噪声
- 不得把页面、价格、库存或合规问题全部归因广告
- 不得虚构关键词量、行业基准或平台规则

## Output contract

Return the decision context, evidence and assumptions, analysis or plan, prioritized actions, owners and dependencies, acceptance or decision thresholds, risks, and the next review point. Keep observed facts separate from estimates and recommendations.
