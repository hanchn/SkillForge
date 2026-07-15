---
name: storefront-product-publishing-manager
description: Plan, execute, and verify independent-store product publishing lifecycle changes, including draft creation, activation, scheduled launch, channel and market visibility, temporary unpublishing, permanent retirement, archiving, redirects, merchandising dependencies, inventory and fulfillment readiness, rollback, and audit records. Use when an AI needs to put products online or offline on Shopify or another owned storefront, coordinate product launch or delisting, prevent broken campaigns and SEO loss, or review whether a product is safe to publish, hide, archive, or delete.
---

# Storefront Product Publishing Manager

Treat publishing as a coordinated business change, not a single status toggle.

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/lifecycle-checklist.md before recommending or executing a state change.
- Use assets/publishing-change-plan.md for approval, handoff, and audit.

## Action model

Classify the requested action before changing state:

- Publish now: make an approved product purchasable on selected markets and channels.
- Schedule: prepare all dependencies and activate at an authorized time.
- Hide temporarily: remove customer visibility while preserving a defined restoration path.
- Retire: stop selling permanently while preserving customer, support, analytics, and SEO obligations.
- Archive: remove the item from active operations without destroying history.
- Delete: irreversible or difficult-to-recover removal; use only with explicit authority and evidence that preservation is unnecessary.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：store_and_product_identifier、target_lifecycle_action。建议补充：markets_channels_and_schedule、product_facts、inventory_and_fulfillment、authorization、marketing_and_seo_dependencies。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. Identify the exact product, variants, environment, storefront, markets, languages, channels, requested state, effective time, and authorizing owner.
2. Capture the current state before mutation: product status, publication targets, URL handle, variants, inventory policy, price, media, collections, metafields, feeds, campaigns, bundles, subscriptions, redirects, and external references.
3. Run the applicable preflight from references/lifecycle-checklist.md. Separate blocking failures from warnings.
4. Determine the minimum state change. Avoid deleting when unpublishing or archiving meets the business goal.
5. Build the dependency plan: content approval, legal and claim review, inventory, fulfillment, tax, shipping, payment, localization, merchandising, search, feeds, ads, email, affiliates, support, and analytics.
6. Define the URL and SEO behavior. For retirement, choose keep-live, out-of-stock, replacement, collection redirect, or gone response based on user value and current evidence. Do not redirect every retired product to the homepage.
7. Define an execution window, owner, ordered changes, verification steps, rollback trigger, and rollback procedure.
8. Obtain explicit authorization before changing live storefront state, publishing to sales channels, deleting data, or modifying redirects and campaigns.
9. Execute only through the available official admin, API, connector, or repository workflow. Record identifiers and before/after state.
10. Verify as a customer and operator across affected market, language, device, channel, cart, checkout, feed, search, and analytics surfaces.
11. Monitor the agreed window for broken links, overselling, feed rejection, campaign mismatch, conversion anomalies, and support impact.
12. Return the audit record, unresolved warnings, and the exact restoration or follow-up action.

## Safety rules

- Do not publish from an ambiguous product name; require a stable product identifier or uniquely verified record.
- Do not infer that draft, active, archived, unpublished, out-of-stock, and deleted mean the same thing across platforms.
- Do not publish unsupported price, inventory, delivery, certification, compatibility, safety, or promotional claims.
- Do not unpublish a product without checking active ads, landing links, bundles, subscriptions, orders, feeds, support content, and replacement paths.
- Do not delete products, variants, media, redirects, or historical records without explicit authority.
- Do not claim success until live customer-facing and operational verification passes.
- If no write-capable authenticated tool is available, produce an approval-ready plan and verification checklist rather than pretending execution occurred.



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

Return action classification, product identity, current-state snapshot, blockers and warnings, dependency map, SEO and URL decision, ordered execution plan, authorization status, before/after evidence when executed, verification results, rollback path, monitoring window, and remaining work.
