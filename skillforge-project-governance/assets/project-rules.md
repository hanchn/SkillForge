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

## Evolution Rules

- 项目级规则变化，更新 `skillforge-project-governance/`
- skill 包结构变化，更新 `templates/` 与 `schemas/`
- 新增 skill，更新 `registry/skills-index.json`
