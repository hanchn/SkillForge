# SkillForge项目治理

- skill id：`skillforge-project-governance`
- 展示名：`SkillForge项目治理`
- 用途：为后续 AI 提供项目定位、架构设计、目录规则、skill 设计规范与演进约束
- 定位：整个 `SkillForge` 仓库的项目级治理 skill，直接位于项目根目录，可单独分享给他人理解仓库规则

## 适用场景

- 新 AI 首次接手 `SkillForge` 项目
- 需要理解项目定位、架构设计与 skill 包规范
- 需要基于现有规则继续新增、修改或升级业务 skill
- 需要避免把业务 skill 错放到平台私有目录中

## 包结构

- `README.md`：项目治理说明
- `SKILL.md`：统一入口
- `skill.json`：机器可读元数据
- `INVOCATION.md`：推荐阅读与执行顺序
- `BASE_PROMPT.md`：通用治理提示词
- `ARCHITECTURE.md`：项目架构设计说明
- `assets/project-rules.md`：项目级规则清单
- `platforms/`：各平台读取建议

## 核心原则

- `SkillForge` 是跨平台业务 skill 蒸馏仓库
- 业务 skill 放在业务目录，不放 `.trae`
- `README.md` 只是说明文件，不承担 skill 身份
- 每个业务 skill 都应可整包单独分发
- 新增 skill 时优先复用标准 skill 包模板
