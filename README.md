# SkillForge

`SkillForge` 是一个专门用于蒸馏各类业务 skill 的跨平台仓库。

## 项目目标

- 按业务维度沉淀可复用 skill
- 让 skill 可以在 `Claude`、`Codex`、`GPT`、`Trae`、`Qorder` 等平台复用
- 让每个 skill 都能单独拎出整个文件夹发送给别人使用
- 给 AI 提供统一索引入口，方便全量搜索与项目理解

## 架构原则

- 业务目录是浏览层，用于按职业与场景查找 skill
- 每个 skill 都是一个独立 skill 包
- `README.md` 只负责说明，不承担 skill 身份
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

- `README.md`：给人看，说明用途、边界、输入输出
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
- `schemas/`：skill 元数据 schema
- `templates/`：新 skill 模板
- `registry/`：全局 skill 索引
- `platforms/`：项目级平台适配约定
- `skillforge-project-governance/`：描述整个项目定位、架构设计与规则的项目级 skill
- 业务目录：如 `跨境运营/`、`互联网研发/`

## 当前要求

- 不要把业务 skill 放进 `.trae`
- 只有“生成 skill 的 skill”才属于工具平台自身
- 每个业务 skill 必须可单独打包和分发
