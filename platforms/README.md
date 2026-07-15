# Platforms

这里存放 `SkillForge` 项目的平台级适配原则。

## 统一约定

- 所有业务 skill 都放在业务目录中，不放 `.trae`
- 每个 skill 都应优先支持跨平台复用
- 平台差异只放在 skill 包的 `platforms/` 中，不污染核心逻辑
- `README.md` 是中文产品文档和版本记录，不是平台专属 skill 入口

## 当前目标平台

- Claude
- Codex
- GPT
- Manus
- Trae
- Qorder
