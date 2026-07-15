# SkillForge Architecture

## Project Positioning

`SkillForge` 不是普通资料库，也不是某个平台的插件目录，而是一个用于蒸馏各类业务 skill 的跨平台仓库。

## Architecture Layers

### 1. 浏览层

- 由业务目录组成，例如 `跨境运营/`、`互联网研发/`
- 作用是按业务或职业维度查找 skill
- 这层首先服务“找 skill”

### 2. skill 包层

- 每个业务 skill 都是一个独立 skill 包
- 推荐固定结构：

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

- 这层首先服务“用 skill”和“发 skill”

### 3. 项目规范层

- 放在根目录，例如：
  - `README.md`
  - `schemas/`
  - `templates/`
  - `registry/`
  - `platforms/`
  - `skillforge-project-governance/`

- 这层首先服务“统一规则”和“持续升级”

## Design Principles

- 中文目录可用于业务浏览
- 稳定英文 `skill id` 用于 skill 包目录名
- `README.md` 只做说明
- `SKILL.md` 是 AI 优先读取的统一入口
- `skill.json` 是机器可读元数据
- skill 必须优先按“整包可单独分发”设计

## What Belongs To Root

- 项目级规则
- 架构设计说明
- 全局 schema/template/registry
- 描述整个仓库的项目级 skill

## What Belongs To Business Folders

- 具体业务 skill
- 与某个业务场景强绑定的脚本、配置、示例和平台适配

## Upgrade Strategy

- 业务 skill 的升级先看是否影响项目级模板
- 如果某种模式被反复复用，应上收为项目级模板或规范
- 如果某个规则影响整个仓库，应优先更新 `skillforge-project-governance/`
