# SkillForge

`SkillForge` 是一个专门用于蒸馏各类业务 skill 的跨平台仓库。

## 项目目标

- 按业务维度沉淀可复用 skill
- 让 skill 可以在 `Claude`、`Codex`、`GPT`、`Trae`、`Qorder` 等平台复用
- 让每个 skill 都能单独拎出整个文件夹发送给别人使用
- 给 AI 提供统一索引入口，方便全量搜索与项目理解

## 当前能力规模

- 95 个正式 Skill 包，其中 94 个在可视化管理页展示。
- 研发架构采用“通用架构 → 语言架构 → 框架架构 → 交付专项”分层。
- 跨境业务覆盖市场、选品、供应链、品牌、内容、渠道、广告、客户、增长和经营分析。
- 企业系统覆盖 OMS、IMS、OFS、CMS、WMS、TMS、CRM、PLM 及跨系统总架构。
- 业务数据覆盖指标治理、数据质量、经营、利润、商品、流量、漏斗、广告、客户、库存、价格、渠道和预测。

## 能力地图

- [前后端架构 Skill 地图](互联网研发/ARCHITECTURE_SKILLS_MAP.md)
- [跨境运营营销 Skill 地图](跨境运营/OPERATIONS_MARKETING_SKILLS_MAP.md)
- [业务数据分析 Skill 地图](数据/BUSINESS_ANALYTICS_SKILLS_MAP.md)
- [企业业务系统产品架构地图](项目管理/SYSTEM_PRODUCT_ARCHITECTURE_MAP.md)

## 架构原则

- 业务目录是浏览层，用于按职业与场景查找 skill
- 每个 skill 都是一个独立 skill 包
- `README.md` 是面向人的中文产品文档，持续记录能力说明与版本升级，但不承担 skill 身份
- skill 必须优先以“整包可分发”为目标设计

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
- 业务目录：如 `跨境运营/`、`互联网研发/`、`项目管理/`

## 当前要求

- 不要把业务 skill 放进 `.trae`
- 只有“生成 skill 的 skill”才属于工具平台自身
- 每个业务 skill 必须可单独打包和分发
- 每次实质升级 skill，都必须同步 README 当前能力说明与版本记录

## 项目版本记录

| 版本 | 日期 | 更新内容 |
|---|---|---|
| 4.0.0 | 2026-07-15 | 扩展前后端三层架构、跨境运营营销、业务数据分析和八类企业系统产品架构。 |
