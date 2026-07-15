# Project Rules

## Core Identity

- `SkillForge` 是跨平台业务 skill 蒸馏仓库
- 目标是让 skill 可被不同 AI 平台理解与复用

## Hard Rules

- 业务 skill 不放 `.trae`
- 只有“生成 skill 的 skill”才属于平台自身
- 每个业务 skill 必须尽量可整包单独分发
- `README.md` 只是说明文件
- 新增业务 skill 时优先使用标准模板
- `SKILL.md` 必须使用仅含 name 与 description 的 YAML frontmatter
- description 必须同时说明能力范围和明确触发场景
- 不得用空泛步骤、占位验收或不存在的脚本伪装成完整 skill
- 关键判断必须说明证据门槛、失败边界和输出合同

## Naming Rules

- 业务浏览目录可以使用中文
- skill 包目录优先使用稳定英文 `skill id`
- `display_name` 放在 `skill.json` 中保存中文展示名

## File Responsibility

- `README.md`：说明文档
- `SKILL.md`：统一入口
- `skill.json`：机器可读元数据
- `INVOCATION.md`：调用协议
- `BASE_PROMPT.md`：通用提示词
- `agents/openai.yaml`：Codex 等支持平台的界面元数据，不改变跨平台核心行为
- `references/`：按需加载的专业方法、规范与检查表
- `assets/`：输出模板、词表、配置和其他可复用静态资源
- `eval/acceptance.md`：可判定的通过条件与直接失败条件

## Evolution Rules

- 项目级规则变化，更新 `skillforge-project-governance/`
- skill 包结构变化，更新 `templates/` 与 `schemas/`
- 新增 skill，更新 `registry/skills-index.json`
- 同步 `PROJECT_INDEX.md` 与 `registry/project-index.json`
- 声明了脚本就必须真实存在并经过代表性运行测试；纯判断型 skill 应将 script 设为空字符串
- 升级旧 skill 时检查触发元数据、输入输出、资源路径、示例、验收和注册表是否一致
