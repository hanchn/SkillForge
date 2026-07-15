# 前后端架构 Skill 地图

## 三层架构

| 层级 | 回答的问题 | 前端 | 后端 |
|---|---|---|---|
| 通用架构 | 系统边界、质量属性、依赖和演进如何设计 | `frontend-architecture-designer` | `backend-architecture-designer` |
| 语言架构 | 语言的类型、模块、并发和运行时约束如何落地 | 不单独设 Skill，由通用架构和专家处理 | Java、Go、Python、Node.js、PHP、Rust、C# |
| 框架/专家 | 具体技术栈的架构、实现、诊断、性能和演进如何负责 | React 资深专家、Vue3 资深专家 | Spring Boot、FastAPI、NestJS、Gin、Laravel、ASP.NET Core |

## 组合方式

1. 新系统先调用通用架构 Skill，形成边界、质量目标和演进约束。
2. React 项目调用 `react-senior-expert`，Vue 3 项目调用 `vue3-senior-expert`；其他前端技术栈由通用前端架构 Skill 基于真实仓库处理。
3. 后端再调用语言和框架 Skill，把通用原则映射到真实运行语义和部署方式。
4. 进入具体交付后，再组合现有功能实现、API 契约、数据库迁移、测试、性能和故障诊断 Skill。

前端任务以通用架构 Skill 为系统 owner，React/Vue3 专家负责技术栈深度，避免多个架构 Skill 重复设计整套系统。

## 边界

- 通用架构不绑定语言和框架。
- React/Vue3 专家不替代业务能力和系统级边界。
- `backend-service-architect` 负责单个服务、领域工作流和故障语义；`backend-architecture-designer` 负责系统级总体架构。
- `frontend-feature-implementer` 负责具体功能交付；`frontend-architecture-designer` 负责长期结构和演进治理。

## 版本记录

| 版本 | 日期 | 更新内容 |
|---|---|---|
| 1.0.0 | 2026-07-15 | 建立通用、语言、框架三层前后端架构体系。 |
