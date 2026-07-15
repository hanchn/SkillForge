# Invocation

## Standard Read Order

1. 读取 `../PROJECT_INDEX.md`
2. 读取 `SKILL.md`
3. 读取 `README.md`
4. 读取 `ARCHITECTURE.md`
5. 读取 `assets/project-rules.md`
6. 如有平台差异，再读取 `platforms/<platform>.md`

## Standard Use Cases

- 在修改 `SkillForge` 目录结构前先读取
- 在新增、重构、迁移任何业务 skill 前先读取
- 在不确定某个能力应放业务目录、项目根目录还是平台目录时先读取
- 在准备把某个 skill 单独发给别人时先读取

## Expected Output

- 项目定位理解
- 架构层次理解
- 当前规则与约束理解
- 对新增或修改请求的合规落点建议
