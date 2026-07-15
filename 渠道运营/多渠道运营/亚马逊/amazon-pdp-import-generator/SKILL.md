---
name: amazon-pdp-import-generator
description: Parse structured product-image filenames into Amazon SKU and variation drafts, research current marketplace rank signals and search trends, build evidence-backed SEO and GEO keyword strategies, generate reviewable PDP copy and import files, and run a field-by-field self-check without inventing product facts or treating stale rank data as current. Use when an AI needs a complete Amazon PDP draft from images and verified product data, including competitor and query research, keyword placement, semantic answer readiness, variation governance, CSV/XLSX output, and pre-publish QA.
---

# Amazon PDP Import Generator

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。
- 必须读取 `references/market-rank-trend-method.md` 与 `references/seo-geo-keyword-method.md`；Rank、搜索位置、趋势和竞品页面必须在本次执行中重新获取并记录站点、类目、查询词、采集时间和来源。
- 正式生成 PDP 文案前必须使用 `assets/keyword-library-intake-template.md` 询问使用者是否已有关键词库，以及是否优先参考给定关键词；未确认前可以解析图片和调研市场，但不得定稿文案。
- 使用 `assets/market-keyword-research-template.md` 保存市场、Rank、趋势与关键词证据，并在交付前逐项执行 `assets/pdp-self-check-checklist.md`。
- 必须读取 `references/amazon-image-compliance-method.md`，先从目标站点当前 Seller Central/官方页面刷新图片规则，再运行 `scripts/audit_amazon_images.py` 生成技术检查报告并完成人工/视觉合规复核。

## Compliance gate

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

Use deterministic parsing for files and evidence-controlled generation for copy.



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. Before copy generation, ask whether the user has a keyword library. If yes, collect its file or source, marketplace, language, version, update time, metrics, prohibited terms and owner. Separately ask whether supplied keywords should be `REQUIRED_CANDIDATE`, `PREFERRED`, `REFERENCE_ONLY` or `NO_PRIORITY`; do not assume priority from the act of uploading a file.
2. Lock the target marketplace, language, category, product type, customer, price band, fulfillment model, variation theme, target launch date, and current Seller Central template version. Do not mix evidence across marketplaces or categories without labeling it.
3. Inspect filenames and verified product records; confirm SKU identity, parent-child relationship, variation attributes, image roles, factual claims, certifications, dimensions, included components, compatibility, care, warranty, and prohibited statements in a product fact ledger. Ask for the target marketplace/category image-rule snapshot when it is not accessible.
4. Run `scripts/audit_amazon_images.py` and `scripts/generate_pdp_import.py` on the image folder. Review pixel dimensions, longest side, byte size, format, animation, aspect ratio, zoom eligibility, duplicate images, role/order and low-confidence rows. Separately inspect main-image white background, product fill, focus, text/graphics/watermarks, included-product accuracy, rights and category-specific restrictions; automated technical checks cannot approve visual content by themselves.
5. Build the current market reference set. Capture relevant category Best Sellers Rank where visible, organic position for defined queries, sponsored position separately, Best Sellers/Movers & Shakers/New Releases signals where applicable, price, review count, rating, offer, content pattern, and snapshot time. Rank is evidence for comparison, not proof of causality.
6. Build a trend view using current marketplace search suggestions, available Amazon analytics supplied or authorized by the user, recent competitor pages, and other current sources. A single snapshot cannot be described as a 7/30/90-day trend; historical direction requires dated observations or a source that provides history.
7. Create a keyword universe from the confirmed user library, verified product vocabulary, customer problems, use cases, attributes, synonyms, category language, search suggestions and current market evidence. Record source, query intent, relevance, evidence, trend direction, competition proxy, user priority, target field, and exclusion reason.
8. Apply the confirmed priority policy only among factually relevant and field-compliant terms. A user-priority keyword with no product relevance, prohibited wording, competitor trademark or unsupported claim must be excluded and explained, not forced into copy.
9. Separate SEO from GEO work. SEO maps high-relevance terms to title, bullets, description/A+ inputs and backend search terms without repetition or stuffing. GEO organizes entities, attributes, use cases, comparisons and concise factual answers so retrieval and answer systems can understand the product; it must not invent unsupported Q&A or claim guaranteed ranking.
10. Draft title, bullets, description, search terms and applicable import fields only from the verified fact ledger. Maintain natural language, mobile readability, field-specific keyword placement, parent-child consistency and marketplace language.
11. Run the self-check checklist across keyword-library decisions, facts, rank freshness, keyword evidence, SEO coverage, GEO semantic coverage, prohibited terms, claims, variations, image pixel/format/size/aspect and visual compliance, spelling, localization, field limits, duplicate terms, byte limits where applicable, template mapping and missing mandatory attributes. Repair failures and rerun until passed or explicitly blocked.
12. Return CSV/XLSX drafts, parse log, market and keyword research, content rationale, self-check report, unresolved risks and exact human approvals. Never call the draft upload-ready unless it has passed the current marketplace/category template and Seller Central validation.

## Guardrails

- Do not infer material, size, performance, certification, compatibility, origin, audience, warranty, or safety claims from an image or filename.
- Do not call the generic draft upload-ready unless it has been mapped to the current marketplace and category template.
- Do not silently merge ambiguous SKUs or colors; retain parse confidence and request review.
- Do not use competitor trademarks or unsupported superlatives.
- Preserve source filenames and parsing logs so every row can be audited.
- Do not describe BSR as keyword rank, sponsored position as organic position, or a current snapshot as a historical trend.
- Do not select competitors solely because they rank highly; require product, price-band, audience and use-case relevance.
- Do not add irrelevant high-volume terms, repeat terms mechanically, hide competitor brands in backend terms, or infer search volume not present in the source.
- SEO and GEO recommendations are hypotheses supported by current evidence, not guarantees of Amazon ranking, indexing, recommendation or AI citation.
- Do not invent a mandatory image aspect ratio when the current marketplace rule does not define one. Report the actual ratio and preview/cropping risk; enforce only verified marketplace/category requirements.
- A technical image pass does not prove visual compliance, product accuracy, copyright, model release or claim substantiation. Missing current rules or unresolved visual risks require `REVIEW_REQUIRED`.



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

Return output file paths, parse summary, image technical and visual compliance report, low-confidence and conflicting rows, product fact ledger, dated market/Rank/trend evidence, SEO/GEO keyword map, PDP field rationale, self-check results, missing factual attributes, marketplace-template caveats, and the exact human checks still required.
