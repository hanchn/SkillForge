---
name: seo-optimizer
description: Research, plan, write, and audit search-engine content using verified business facts, search intent, query evidence, SERP patterns, information architecture, on-page metadata, internal links, structured data opportunities, and measurement plans. Use when an AI needs to create or improve landing pages, product pages, collection pages, articles, titles, descriptions, content briefs, keyword maps, or SEO audits without keyword stuffing or invented claims.
---

# SEO Optimizer

Optimize for the user's search task and the page's business job. Do not promise rankings.

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/content-audit.md before research or revision.
- Use assets/seo-content-brief.md for a new page or major rewrite.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：page_or_content_goal。建议补充：target_market、business_facts、url、keyword_or_serp_data、performance_data。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. Establish market, language, audience, page type, conversion goal, current URL, product facts, and available performance data.
2. Preserve a source ledger for product claims, policies, prices, specifications, and expert statements. Mark anything unverified.
3. Identify the primary search intent and adjacent intents. If live search or keyword data is unavailable, call proposed phrases hypotheses rather than measured keywords.
4. Inspect the current SERP when browsing is available: result types, dominant page formats, recurring subtopics, freshness, authority, and intent mismatches. Do not copy competitors.
5. Select one primary topic and a limited set of supporting concepts. Prevent multiple pages from targeting the same job without a consolidation plan.
6. Design the page structure to answer the main question early, then supply evidence, comparison, objections, decision help, and a next action.
7. Write title, H1, meta description, headings, body, alt-text guidance, internal-link targets, and structured-data recommendations appropriate to the page.
8. Check technical prerequisites that can invalidate content work: indexability, canonical, status code, duplicate variants, rendering, mobile behavior, localization, pagination, and performance.
9. Compare before and after for intent coverage, factual accuracy, information gain, readability, accessibility, and conversion alignment.
10. Define measurement: query and landing-page impressions, clicks, qualified engagement, conversions, cannibalization, and an observation window.

## Guardrails

- Do not fabricate keyword volume, difficulty, competitor traffic, rankings, reviews, certifications, or product facts.
- Avoid keyword density targets, hidden text, doorway pages, mass near-duplicates, and irrelevant schema.
- Keep title and metadata within practical display constraints without treating pixel or character limits as universal guarantees.
- Use internal links because the destination helps the reader, not only to move authority.
- Keep SEO recommendations separate from changes that require engineering, legal, merchandising, or analytics validation.



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

Return evidence and assumptions, intent and query map, current gaps, content brief or optimized copy, metadata, internal-link plan, technical blockers, validation checklist, and measurement plan. For rewrites, preserve important factual content and show material changes.
