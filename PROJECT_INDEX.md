# SkillForge Project Index

这个文件给 AI 提供全局导航、分类定位和技能检索入口。

## First Read

- 项目总说明：README.md
- 项目治理：skillforge-project-governance/SKILL.md
- 全局注册表：registry/skills-index.json
- 元数据规范：schemas/skill.schema.json
- 标准模板：templates/standard-skill-package/
- 可视化管理：skills-dashboard/
- 电商前十能力：跨境运营/ECOMMERCE_TOP10_SKILLS.md
- 前后端能力地图：互联网研发/DEVELOPMENT_SKILLS_MAP.md
- 研发角色：互联网研发/研发角色/README.md
- 公司项目浏览：项目管理/README.md

## Search Strategy

1. 新建、升级或打包 skill 前先读项目治理 skill。
2. 从 registry/skills-index.json 按 name、category_path 或 search_keywords 定位。
3. 进入技能包后先读 README.md 理解中文产品能力和版本，再读 SKILL.md 执行。
4. 按 SKILL.md 指示加载 references 与 assets。
5. 执行后使用 eval/acceptance.md 验收；声明脚本的技能还必须运行脚本测试。

## Business Browse Directories

- 跨境运营/：选品、供应链、合规、利润、库存、物流、渠道和推广营销。
- 互联网研发/：产品、前端、后端、测试、Git 和研发角色。
- 数据/：业务分析与指标诊断。
- 法律政务/：合同和法律政务辅助。
- 项目管理/：公司 IMS、TMS、OMS、OFS、WMS 项目及未来细分 skill。
- work/：工作台与基座行为资料。

## Registered Skills

### SkillForge项目治理

- skill id：skillforge-project-governance
- 路径：skillforge-project-governance/
- 分类：project-root
- 用途：描述 SkillForge 项目的定位、架构设计与治理规则，供后续 AI 持续按统一标准升级业务 skill。
- 前端展示：隐藏（项目治理基座）

### Git 安全工作流管理器

- skill id：git-workflow-manager
- 路径：互联网研发/git/git-workflow-manager/
- 分类：互联网研发 / git / 安全工作流
- 用途：基于真实仓库状态安全规划或执行分支、提交、合并、变基、发布流转、冲突处理与恢复

### 产品需求架构师

- skill id：product-requirements-architect
- 路径：互联网研发/产品/B端产品/product-requirements-architect/
- 分类：互联网研发 / 产品 / B端产品
- 用途：把模糊产品想法转成可评审、可开发、可测试、可度量的需求包

### 前端功能实现工程师

- skill id：frontend-feature-implementer
- 路径：互联网研发/前端/前台/frontend-feature-implementer/
- 分类：互联网研发 / 前端 / 前台 / 功能实现
- 用途：Implement complete frontend features in an existing codebase from product requirements, screenshots, designs, or behavioral specifications while preserving repository conventions, responsive behavior, accessibility, loading and failure states, data contracts, tests, and visual fidelity

### 前端多语言查验师

- skill id：frontend-localization-verifier
- 路径：互联网研发/前端/前台/frontend-localization-verifier/
- 分类：互联网研发 / 前端 / 前台 / 国际化与本地化
- 用途：Verify frontend internationalization and localization across supported locales, including translation coverage, key drift, ICU messages, variables, plurals, gender, dates, numbers, currency, units, time zones, Unicode, collation, locale routing, persistence, layout expansion, RTL, fonts, accessibility, metadata, hreflang, and localized business behavior

### 前端性能分析师

- skill id：frontend-performance-analyzer
- 路径：互联网研发/前端/前台/frontend-performance-analyzer/
- 分类：互联网研发 / 前端 / 前台 / 性能分析
- 用途：Diagnose frontend performance using field and laboratory evidence, Core Web Vitals, navigation and interaction traces, network waterfalls, rendering, main-thread tasks, JavaScript execution, bundles, images, fonts, caching, hydration, data fetching, third-party scripts, memory, and performance budgets

### 前端状态与数据流设计师

- skill id：frontend-state-integration-designer
- 路径：互联网研发/前端/前台/frontend-state-integration-designer/
- 分类：互联网研发 / 前端 / 前台 / 状态与数据
- 用途：Design and review predictable frontend state, URL state, form state, server cache, asynchronous queries, mutations, optimistic updates, invalidation, race handling, offline behavior, and error recovery

### Web 性能与无障碍审计师

- skill id：web-performance-accessibility-auditor
- 路径：互联网研发/前端/前台/web-performance-accessibility-auditor/
- 分类：互联网研发 / 前端 / 前台 / 质量审计
- 用途：Audit and improve web performance, Core Web Vitals, loading behavior, semantic HTML, keyboard access, focus management, screen-reader communication, contrast, motion, responsive interaction, and regression risk using measured evidence

### API 契约设计师

- skill id：api-contract-designer
- 路径：互联网研发/后端/api-contract-designer/
- 分类：互联网研发 / 后端 / API设计
- 用途：设计一致、可演进、可测试并能直接评审的 HTTP 或事件 API 契约

### 后端服务架构师

- skill id：backend-service-architect
- 路径：互联网研发/后端/backend-service-architect/
- 分类：互联网研发 / 后端 / 服务架构
- 用途：Design and review backend service boundaries, domain invariants, workflows, data ownership, synchronous and asynchronous interactions, authorization, idempotency, consistency, failure recovery, observability, scaling, deployment, and evolutionary rollout

### 数据库变更迁移规划师

- skill id：database-migration-planner
- 路径：互联网研发/后端/database-migration-planner/
- 分类：互联网研发 / 后端 / 数据库迁移
- 用途：Plan, implement, and verify safe database schema and data migrations using dependency analysis, locking and runtime estimates, expand-migrate-contract sequencing, backfills, dual reads or writes, reconciliation, constraints, indexes, rollout gates, rollback, and recovery

### 生产故障诊断师

- skill id：production-incident-diagnostician
- 路径：互联网研发/后端/production-incident-diagnostician/
- 分类：互联网研发 / 后端 / 生产故障
- 用途：Diagnose and coordinate production incidents using impact assessment, safe stabilization, timelines, competing hypotheses, logs, metrics, traces, deploy and configuration changes, dependency evidence, mitigations, rollback, communication, verification, and follow-up learning

### 测试策略设计师

- skill id：test-strategy-designer
- 路径：互联网研发/测试/test-strategy-designer/
- 分类：互联网研发 / 测试 / 测试策略
- 用途：根据变更影响和风险设计分层覆盖、发布门槛与生产验证方案

### 全栈开发周报生成器

- skill id：fullstack-developer-weekly-report
- 路径：互联网研发/研发角色/全栈开发/fullstack-developer-weekly-report/
- 分类：互联网研发 / 研发角色 / 全栈开发 / 周报
- 用途：Create evidence-backed full-stack development weekly reports from tickets, requirements, Git commits, pull requests, reviews, frontend and backend changes, database migrations, deployments, incidents, and project notes

### 全栈功能交付工程师

- skill id：fullstack-feature-delivery
- 路径：互联网研发/研发角色/全栈开发/fullstack-feature-delivery/
- 分类：互联网研发 / 研发角色 / 全栈开发
- 用途：Deliver product features end to end across requirements, frontend interaction, API contracts, backend domain logic, data changes, authentication and authorization, observability, tests, deployment, migration, rollout, and post-release verification

### 全栈测试周报生成器

- skill id：fullstack-qa-weekly-report
- 路径：互联网研发/研发角色/全栈测试/fullstack-qa-weekly-report/
- 分类：互联网研发 / 研发角色 / 全栈测试 / 周报
- 用途：Create evidence-backed full-stack quality weekly reports from requirements, risk assessments, test plans, executions, automation, defects, regressions, environments, releases, production verification, incidents, and quality metrics

### 全栈质量工程师

- skill id：fullstack-quality-engineer
- 路径：互联网研发/研发角色/全栈测试/fullstack-quality-engineer/
- 分类：互联网研发 / 研发角色 / 全栈测试
- 用途：Verify complete product behavior across frontend, API, backend, database, jobs, events, integrations, localization, accessibility, performance, security, observability, deployment, rollback, and production monitoring using a risk-based evidence chain

### 业务指标诊断师

- skill id：metric-diagnostics
- 路径：数据/metric-diagnostics/
- 分类：数据 / 业务分析 / 指标诊断
- 用途：验证指标口径与数据质量，量化拆解异常变化并区分驱动因素和假设

### 合同风险审阅师

- skill id：contract-risk-reviewer
- 路径：法律政务/contract-risk-reviewer/
- 分类：法律政务 / 合同 / 商业合同审阅
- 用途：逐条提取合同义务、识别风险和缺失保护，并形成可谈判的优先清单

### 供应商寻源与质量管理器

- skill id：supplier-sourcing-quality-manager
- 路径：跨境运营/供应链/supplier-sourcing-quality-manager/
- 分类：跨境运营 / 供应链 / 寻源与质量
- 用途：Plan and evaluate ecommerce supplier sourcing, RFQs, samples, factory capability, commercial terms, quality standards, inspections, defect handling, packaging, production readiness, and supplier concentration risk

### 跨境商品合规风险管理器

- skill id：product-compliance-risk-manager
- 路径：跨境运营/合规/product-compliance-risk-manager/
- 分类：跨境运营 / 合规 / 商品与声明
- 用途：Screen and manage cross-border product compliance, safety, labeling, documentation, restricted-product, marketplace, claim, testing, recall, and evidence risks by target market and sales channel

### 亚马逊 PDP 导入草稿生成器

- skill id：amazon-pdp-import-generator
- 路径：跨境运营/多渠道运营/亚马逊/amazon-pdp-import-generator/
- 分类：跨境运营 / 多渠道运营 / 亚马逊
- 用途：从结构化图片文件名确定性生成 SKU、变体和图片分组草稿，再基于已验证商品事实生成亚马逊内容

### Shopify 转化审计师

- skill id：shopify-conversion-auditor
- 路径：跨境运营/多渠道运营/独立站/shopify-conversion-auditor/
- 分类：跨境运营 / 多渠道运营 / 独立站 / CRO
- 用途：基于页面、数据和真实商品事实审计 Shopify 转化障碍并排序改进项

### 独立站产品上下架管理器

- skill id：storefront-product-publishing-manager
- 路径：跨境运营/多渠道运营/独立站/storefront-product-publishing-manager/
- 分类：跨境运营 / 多渠道运营 / 独立站 / 商品运营
- 用途：安全规划、执行和验证独立站产品上架、定时发布、下架、退市、归档、重定向与回滚

### 多渠道库存补货规划师

- skill id：inventory-replenishment-planner
- 路径：跨境运营/库存/inventory-replenishment-planner/
- 分类：跨境运营 / 库存 / 预测与补货
- 用途：Plan multi-channel ecommerce inventory and replenishment using demand, seasonality, promotions, lead-time distributions, safety stock, service levels, inbound stages, channel allocation, storage constraints, cash limits, and stockout or overstock risk

### 多渠道电商广告优化师

- skill id：commerce-advertising-optimizer
- 路径：跨境运营/推广营销/commerce-advertising-optimizer/
- 分类：跨境运营 / 推广营销 / 广告优化
- 用途：Diagnose and optimize Amazon Ads and owned-store paid media using business objectives, clean attribution, query and audience intent, campaign structure, bids, budgets, creative, landing-page readiness, incrementality, contribution margin, and controlled experiments

### GEO 引用就绪优化师

- skill id：geo-optimizer
- 路径：跨境运营/推广营销/geo-optimizer/
- 分类：跨境运营 / 推广营销 / GEO
- 用途：通过实体一致性、声明溯源和可抽取答案模块提升生成式答案引擎理解与准确引用的可能性

### SEO 内容优化师

- skill id：seo-optimizer
- 路径：跨境运营/推广营销/seo-optimizer/
- 分类：跨境运营 / 推广营销 / SEO
- 用途：基于真实业务事实、搜索意图、SERP 证据和技术前提规划、撰写与审计 SEO 内容

### 电商履约物流规划师

- skill id：ecommerce-fulfillment-logistics-planner
- 路径：跨境运营/物流/ecommerce-fulfillment-logistics-planner/
- 分类：跨境运营 / 物流 / 跨境履约
- 用途：Design and compare ecommerce freight, customs, receiving, warehousing, FBA, FBM, 3PL, direct fulfillment, returns, and delivery operations using landed cost, service level, dimensional weight, capacity, exception handling, and resilience

### 电商单位经济模型分析师

- skill id：ecommerce-unit-economics-analyst
- 路径：跨境运营/经营分析/ecommerce-unit-economics-analyst/
- 分类：跨境运营 / 经营分析 / 利润与现金流
- 用途：Model product, SKU, channel, campaign, and portfolio profitability across Amazon and owned storefronts using complete unit economics, contribution margin, break-even advertising, returns, fees, working capital, cash conversion, and sensitivity scenarios

### 跨境电商选品研究

- skill id：ecommerce-product-research
- 路径：跨境运营/选品/ecommerce-product-research/
- 分类：跨境运营 / 选品 / 跨渠道机会研究
- 用途：从需求、竞争、利润、供应链、合规和渠道适配评估跨境产品机会

## Architecture Notes

- 中文目录负责业务、公司项目和研发角色浏览，稳定英文目录负责 skill id。
- 每个正式 skill 优先按整个文件夹独立分发。
- README.md 是中文产品文档和版本记录；SKILL.md 是 AI 执行入口。
- 项目代号、角色和分类目录本身不等于正式 skill。
- 业务核心保持跨平台；agents 与 platforms 只适配界面或工具差异。
- 新增或升级 skill 必须同步 registry、PROJECT_INDEX 和分类 README。
- SkillForge 项目治理保留在索引中，但不在业务 Dashboard 展示。
