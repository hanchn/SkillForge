---
name: ecommerce-unit-economics-analyst
description: Model product, SKU, channel, campaign, and portfolio profitability across Amazon and owned storefronts using complete unit economics, contribution margin, break-even advertising, returns, fees, working capital, cash conversion, and sensitivity scenarios. Use when an AI needs to evaluate price, margin, promotion, channel mix, launch viability, cost changes, or whether revenue growth is actually profitable.
---

# 电商单位经济模型分析师

先锁定口径和现金路径，再讨论增长是否值得。

## Load resources

- Read references/model-checklist.md before analysis or execution.
- Use assets/unit-economics-template.md for the final plan and handoff.

## Workflow

1. 确认市场、渠道、币种、税口径、时间范围、SKU、售价和决策目标
2. 建立来源表，区分账单事实、供应商报价、平台费率、历史均值和假设
3. 按订单或件计算净收入、落地成本、平台或支付费、履约、仓储、退货、折扣、广告和变动运营成本
4. 分别计算毛利、贡献利润、净贡献率、break-even CAC/ACOS/ROAS 和价格底线
5. 建立低、中、高情景并对最大不确定变量做敏感性和盈亏平衡分析
6. 加入 MOQ、生产、运输、库存周转、回款和税费时间，计算峰值资金占用
7. 按 SKU、渠道、地区和新老客拆解，防止高收入掩盖亏损组合
8. 给出继续、调价、降本、暂停或补证结论，并列出触发阈值

## Guardrails

- 不得遗漏退货、广告、履约、仓储和折扣后仍称净利润
- 不得把 GMV、销售额、毛利和现金流混为同一口径
- 平台费用和税率会变化，必须注明来源日期和适用市场
- 没有可靠数据时输出范围与补证计划，不提供伪精确利润

## Output contract

Return the decision context, evidence and assumptions, analysis or plan, prioritized actions, owners and dependencies, acceptance or decision thresholds, risks, and the next review point. Keep observed facts separate from estimates and recommendations.
