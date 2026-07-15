---
name: ecommerce-product-research
description: Evaluate cross-border ecommerce product opportunities using demand evidence, customer pain, competitive structure, unit economics, supply-chain feasibility, compliance, seasonality, channel fit, differentiation, and staged validation. Use when an AI needs to research or compare products, build a product-selection scorecard, assess Amazon, Shopify, TikTok Shop, or marketplace opportunities, reject weak ideas, estimate downside, or design a low-cost validation plan before sourcing and launch.
---

# Ecommerce Product Research

Make a falsifiable investment recommendation, not a trend list.

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/research-framework.md before scoring an opportunity.
- Use assets/opportunity-scorecard.md for single-product or portfolio comparison.

## Intake

Lock the target country, channel options, budget, target landed cost, desired selling price, margin floor, launch window, team capabilities, sourcing constraints, and risk tolerance. If the user supplies only a product keyword, provide a preliminary screen and clearly identify missing investment inputs.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：candidate_product_or_category、target_market。建议补充：channel_options、budget、margin_floor、supplier_data、research_sources。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. Define the customer, job, buying occasion, current alternatives, and reason the problem remains unsolved.
2. Build a source log. Separate marketplace observations, trend data, keyword data, review evidence, supplier claims, regulatory sources, and user assumptions.
3. Assess demand quality: persistent versus event-driven, branded versus generic, repeat versus one-off, giftable, seasonal, price-sensitive, and channel-dependent.
4. Analyze competition beyond seller count: listing quality, review moat, brand concentration, ad density, price bands, feature convergence, complaint patterns, and switching barriers.
5. Mine negative reviews and community discussions for recurring unmet needs. Require frequency, severity, solvability, and willingness-to-pay evidence before calling a complaint an opportunity.
6. Model unit economics with low, base, and high cases. Include product cost, packaging, freight, duty, fulfillment, payment or marketplace fees, returns, discounts, advertising, storage, tax assumptions, and defect allowance.
7. Assess sourcing and operations: MOQ, lead time, tooling, quality control, dangerous goods, dimensional weight, breakage, expiry, variants, replenishment, seasonality, and supplier concentration.
8. Screen compliance and claim risk for the target market. Flag products needing specialist testing or counsel; never infer compliance from a supplier badge alone.
9. Score product-channel fit separately for Amazon, Shopify, TikTok Shop, and other requested channels. Do not average away a fatal channel mismatch.
10. Define defensible differentiation in product, bundle, positioning, proof, content, service, or distribution. Reject cosmetic changes that do not solve a verified need.
11. List kill criteria and run the cheapest validation sequence: source verification, landing-page or creative test, sample inspection, small order, then scaled inventory.
12. Make a decision: proceed, validate first, hold, or reject. State the evidence, sensitivity, capital at risk, and next decision gate.

## Evidence rules

- Cite live or provided sources with observation dates when browsing is available.
- Do not fabricate search volume, sales estimates, fees, supplier quotes, certifications, patents, or category restrictions.
- Label proxy data and explain why it is relevant.
- Treat third-party sales estimates as ranges, not ground truth.
- Use weighted contribution and scenario analysis; avoid false precision in composite scores.



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。



## Evidence freshness gate

- 标明数据截止、采集时间、来源、版本、适用国家/渠道/系统和刷新周期。
- 市场、价格、Rank、趋势、库存、平台规则、法律、税务、汇率、软件版本和人员信息等时效事实必须在本次任务中重新核验，不得使用模型记忆冒充实时数据。
- 单次快照不能写成历史趋势；来源冲突、过期或不可访问时保留差异并降级为调研、草案或 `REVIEW_REQUIRED`。

## Output contract

Return an executive verdict, customer problem, evidence table, demand and competition analysis, review-derived opportunities, scenario economics, supply-chain and compliance risks, channel-fit matrix, differentiation thesis, scorecard, kill criteria, and staged validation plan. For multiple candidates, show both comparable scores and product-specific fatal risks.
