# 前后端架构 Skill 地图

## 三层架构

| 层级 | 回答的问题 | 前端 | 后端 |
|---|---|---|---|
| 通用架构 | 系统边界、质量属性、依赖和演进如何设计 | `frontend-architecture-designer` | `backend-architecture-designer` |
| 语言架构 | 语言的类型、模块、并发和运行时约束如何落地 | JavaScript、TypeScript | Java、Go、Python、Node.js |
| 框架架构 | 具体框架的组件、模块、生命周期和生产能力如何组织 | React、Vue、Next.js、Angular、SvelteKit | Spring Boot、FastAPI、NestJS、Gin、Laravel、ASP.NET Core |

## 组合方式

1. 新系统先调用通用架构 Skill，形成边界、质量目标和演进约束。
2. 再调用语言 Skill，确定模块、类型、并发、依赖和构建原则。后端现覆盖 Java、Go、Python、Node.js、PHP、Rust、C#。
3. 最后调用框架 Skill，把原则映射到真实目录、运行语义和部署方式。
4. 进入具体交付后，再组合现有功能实现、API 契约、数据库迁移、测试、性能和故障诊断 Skill。

例如 Next.js + TypeScript 项目，应以通用前端架构为主，组合 TypeScript 与 Next.js 架构；不要让三个 Skill 分别重复设计整套系统。

## 边界

- 通用架构不绑定语言和框架。
- 语言架构不替代框架生命周期设计。
- 框架架构不替代业务能力和系统级边界。
- `backend-service-architect` 负责单个服务、领域工作流和故障语义；`backend-architecture-designer` 负责系统级总体架构。
- `frontend-feature-implementer` 负责具体功能交付；`frontend-architecture-designer` 负责长期结构和演进治理。

## 版本记录

| 版本 | 日期 | 更新内容 |
|---|---|---|
| 1.0.0 | 2026-07-15 | 建立通用、语言、框架三层前后端架构体系。 |
