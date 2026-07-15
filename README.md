# SkillForge

`SkillForge` 是一个专门用于蒸馏各类业务 skill 的跨平台仓库。

## 项目目标

- 按业务维度沉淀可复用 skill
- 让 skill 可以在 `Claude`、`Codex`、`GPT`、`Trae`、`Qorder` 等平台复用
- 让每个 skill 都能单独拎出整个文件夹发送给别人使用
- 给 AI 提供统一索引入口，方便全量搜索与项目理解

## 当前能力规模

- 183 个正式 Skill 包，其中 182 个在可视化管理页展示。
- 后端研发采用“通用架构 → 语言架构 → 框架架构 → 交付专项”；前端收敛为通用架构加 React/Vue3 资深专家。
- 跨境业务覆盖市场、选品、供应链、品牌、内容、渠道、广告、客户、增长和经营分析。
- 企业系统覆盖 OMS、IMS、OFS、CMS、WMS、TMS、CRM、PLM 及跨系统总架构。
- 业务数据覆盖指标治理、数据质量、经营、利润、商品、流量、漏斗、广告、客户、库存、价格、渠道和预测。

## 能力地图

- [前后端架构 Skill 地图](互联网研发/ARCHITECTURE_SKILLS_MAP.md)
- [渠道运营 Skill 地图](渠道运营/CHANNEL_OPERATIONS_SKILLS_MAP.md)
- [客服售前 Skill 地图](客服售前/CUSTOMER_PRESALES_SKILLS_MAP.md)
- [精准营销 Skill 地图](精准营销/PRECISION_MARKETING_SKILLS_MAP.md)
- [创拍视觉 Skill 地图](创拍视觉/CREATIVE_VISUAL_SKILLS_MAP.md)
- [市场采购 Skill 地图](市场采购/MARKET_PROCUREMENT_SKILLS_MAP.md)
- [仓储库存 Skill 地图](仓储库存/WAREHOUSE_INVENTORY_SKILLS_MAP.md)
- [业务数据分析 Skill 地图](数据看板/BUSINESS_ANALYTICS_SKILLS_MAP.md)
- [跨境法律 Skill 地图](法律政务/LEGAL_SKILLS_MAP.md)
- [跨境财务与出纳 Skill 地图](财务出纳/FINANCE_SKILLS_MAP.md)
- [人事招聘 Skill 地图](人事招聘/HR_RECRUITING_SKILLS_MAP.md)
- [企业业务系统产品架构地图](互联网研发/产品/系统产品架构/SYSTEM_PRODUCT_ARCHITECTURE_MAP.md)

## 架构原则

- 业务目录是浏览层，用于按职业与场景查找 skill
- 每个 skill 都是一个独立 skill 包
- `README.md` 是面向人的中文产品文档，持续记录能力说明与版本升级，但不承担 skill 身份
- skill 必须优先以“整包可分发”为目标设计
- 一个 Skill 默认完成一个可验收的完整业务结果，能够升级现有 Skill 时不再拆动作级 Skill
- 所有 Skill 按[深度标准](SKILL_DEPTH_STANDARD.md)覆盖业务理解、场景变体、上下游、决策、异常、工具、交付与复盘，并生成[深度审计](SKILL_DEPTH_AUDIT.md)
- 所有 Skill 在项目内优先读取[公司上下文](公司上下文/README.md)，使用贵司已确认的系统、组织和业务口径
- 每个 Skill 使用 SemVer 版本号；内容指纹发生实质变化时自动升级，并在卡片、详情、索引和中文 README 展示
- 每个 Skill 必须携带分类化合规基线并执行 `ALLOW / REVIEW_REQUIRED / COMPLIANCE_REJECTED` 门禁，详见[全库合规治理](COMPLIANCE_GOVERNANCE.md)
- 主角色统一命名：产研决策型为“架构师”，产研实现型为“资深专家”，业务经营型为“资深经理”；周报独立标记

## 标准 skill 包结构

```text
<business-path>/<skill-id>/
├── README.md
├── SKILL.md
├── skill.json
├── INVOCATION.md
├── BASE_PROMPT.md
├── platforms/
├── examples/
├── eval/
├── scripts/
└── assets/
```

## 文件职责

- `README.md`：中文产品文档，说明定位、场景、边界、输入输出、工作原理、验收和版本记录
- `SKILL.md`：统一入口，优先给 AI 读取
- `skill.json`：机器可读元数据
- `INVOCATION.md`：标准调用协议
- `BASE_PROMPT.md`：跨平台通用提示词
- `platforms/`：平台差异层
- `examples/`：样例输入输出
- `eval/`：验收标准
- `scripts/`：真实执行逻辑
- `assets/`：词表、模板、配置等静态资源

## 项目级目录

- `PROJECT_INDEX.md`：给 AI 的全局导航与搜索入口
- `skills-dashboard/`：可视化 skills 管理页面
- `schemas/`：skill 元数据 schema
- `templates/`：新 skill 模板
- `registry/`：全局 skill 索引
- `platforms/`：项目级平台适配约定
- `skillforge-project-governance/`：描述整个项目定位、架构设计与规则的项目级 skill
- 业务目录：如 `渠道运营/`、`客服售前/`、`精准营销/`、`创拍视觉/`、`市场采购/`、`仓储库存/`、`互联网研发/`、`数据看板/`、`法律政务/`、`财务出纳/`、`人事招聘/`、`项目管理/`

## 当前要求

- 不要把业务 skill 放进 `.trae`
- 只有“生成 skill 的 skill”才属于工具平台自身
- 每个业务 skill 必须可单独打包和分发
- 每次实质升级 skill，都必须同步 README 当前能力说明与版本记录

## 项目版本记录

| 版本 | 日期 | 更新内容 |
|---|---|---|
| 6.1.0 | 2026-07-15 | 建立十二项 Skill 深度标准与全库自动审计；为标准化 Skill 增加场景作战手册、异常门禁和决策记录；JD Skill 新增 HR 岗位培训、近期岗位薪酬调研、预问问题和空白模板。 |
| 6.0.0 | 2026-07-15 | 一级分类“创意拍摄”升级为“创拍视觉”，覆盖创意、拍摄、视觉与广告；将产研中的 AI 视觉打标能力合并到创拍视觉智能打标 Skill，删除重复 Skill。 |
| 5.9.0 | 2026-07-15 | 为全库 Skill 建立按业务分类适配的合规基线、三态执行门禁、人工升级、机器元数据与版本联动。 |
| 5.8.0 | 2026-07-15 | 创拍视觉新增智能打标 Skill，并将 AI 图片视频成片升级为完整 AIGC 创意制作能力。 |
| 5.7.0 | 2026-07-15 | 统一角色体系：产研分为架构师和资深专家，业务主角色统一为资深经理；同步目录、周报和前端类型标签。 |
| 5.6.0 | 2026-07-15 | 取消“总产品架构师”定位，将其收敛为只负责系统责任、主数据和流程交接的跨系统产品边界设计能力。 |
| 5.5.0 | 2026-07-15 | 建立 Skill 合并治理与贵司上下文；将客服售前和补货预警收拢为完整业务 Skill；新增培训组织；上线内容指纹自动版本与前端版本展示。 |
| 5.4.0 | 2026-07-15 | 新增客服售前一级分类与七项专项能力；新增库存补货预警；删除职责重叠的前端状态与数据流设计师。 |
| 5.3.0 | 2026-07-15 | 从渠道运营拆出市场采购与仓储库存一级分类，迁移选品、供应商、库存和履约能力并补齐专业 Skill。 |
| 5.2.0 | 2026-07-15 | 将创拍视觉升级为一级分类，新增主角色、传统制作、虚拟模特、AI 成片、智能剪辑和真实性合规 Skill；新增 UI 交互能力和全局类型标签。 |
| 5.1.0 | 2026-07-15 | 新增财务出纳、人事招聘、JD 与公告、进出口及美欧合规、用户运营、拉新、素材与拍摄 Skill，并支持默认热度排序。 |
| 5.0.0 | 2026-07-15 | 拆分渠道运营与精准营销一级分类，新增主角色、法律和财务体系，并收敛前端专家结构。 |
| 4.0.0 | 2026-07-15 | 扩展前后端三层架构、跨境运营营销、业务数据分析和八类企业系统产品架构。 |
