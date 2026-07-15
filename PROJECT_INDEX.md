# SkillForge Project Index

这个文件用于给 AI 提供 `SkillForge` 的全局导航入口，方便做全量搜索、定位和理解。

## First Read

- 项目总说明：[README.md](file:///Users/yuanjing/Desktop/SkillForge/README.md)
- Skills 可视化页：[skills-dashboard](file:///Users/yuanjing/Desktop/SkillForge/skills-dashboard)
- 项目基座 skill：[skillforge-project-governance](file:///Users/yuanjing/Desktop/SkillForge/skillforge-project-governance)
- 全局 skill 索引：[skills-index.json](file:///Users/yuanjing/Desktop/SkillForge/registry/skills-index.json)
- 元数据 schema：[skill.schema.json](file:///Users/yuanjing/Desktop/SkillForge/schemas/skill.schema.json)

## Search Strategy

- 先读 `skillforge-project-governance/`，理解项目定位、规则和架构
- 再读 `registry/skills-index.json`，定位已有 skill 包
- 再根据 `category_path` 或业务目录进入具体 skill
- 如果要新增 skill，先读 `templates/standard-skill-package/`

## Project Layers

- 项目规范层：
  - `README.md`
  - `PROJECT_INDEX.md`
  - `skillforge-project-governance/`
  - `schemas/`
  - `templates/`
  - `registry/`
  - `platforms/`

- 业务浏览层：
  - `跨境运营/`
  - `互联网研发/`
  - `法律政务/`
  - `work/`

## Existing Skills

- `skillforge-project-governance`
  - path: `skillforge-project-governance/`
  - type: project governance
  - purpose: 解释整个项目的规则、架构和升级方式

- `amazon-pdp-import-generator`
  - path: `跨境运营/多渠道运营/亚马逊/amazon-pdp-import-generator/`
  - type: portable business skill
  - purpose: 根据商品图片文件名生成亚马逊 PDP 导入草稿并利用 AI 扩写 SEO 字段

- `seo-optimizer`
  - path: `跨境运营/推广营销/seo-optimizer/`
  - type: portable business skill
  - purpose: 提供针对搜索引擎优化的内容改写、关键词挖掘、标题与描述优化策略

- `geo-optimizer`
  - path: `跨境运营/推广营销/geo-optimizer/`
  - type: portable business skill
  - purpose: 提供针对生成式AI引擎的内容优化策略，提升 AI 引用与推荐概率

- `git-workflow-manager`
  - path: `互联网研发/git/git-workflow-manager/`
  - type: portable business skill
  - purpose: 规范化 Git 分支命名与合并流程（master/pre/test/fix/feature）

## Top-Level Directories

- `skillforge-project-governance/`：整个项目的治理 skill
- `skills-dashboard/`：skills 可视化管理页面
- `registry/`：全局索引
- `schemas/`：skill 元数据规范
- `templates/`：标准 skill 包模板
- `platforms/`：项目级平台约定
- `跨境运营/`：跨境业务 skill 浏览层
- `互联网研发/`：研发类 skill 浏览层
- `法律政务/`：法律政务类浏览层
- `work/`：工作台与基座行为相关内容

## AI Notes

- `README.md` 只承担说明职责
- 业务 skill 不放 `.trae`
- 每个业务 skill 优先按整包可分发设计
- 对当前 Trae 项目，请优先读取 `.trae/skills/skillforge-project-governance/SKILL.md`
