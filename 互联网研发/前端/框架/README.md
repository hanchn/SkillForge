# 前端框架架构

## 分类定位

在通用架构与语言架构之上处理具体框架的运行语义。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [Next.js 前端架构师](Next.js/nextjs-frontend-architecture/README.md)：按 App Router、服务端与客户端边界、缓存和部署环境设计生产级 Next.js 架构。 Use when an AI needs to handle Next.js App Router 新项目, Pages Router 迁移, 电商 SEO、性能和缓存架构; produce Next.js 路由与渲染蓝图, Server/Client 边界, 缓存、数据和部署方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [React 前端架构师](React/react-frontend-architecture/README.md)：围绕组件、状态、数据流和渲染边界设计可演进 React 应用。 Use when an AI needs to handle React 应用架构和重构, 复杂状态与数据流治理, 组件平台和多团队协作; produce React 架构蓝图, 组件与状态边界, 渲染、测试和迁移方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [Vue 前端架构师](Vue/vue-frontend-architecture/README.md)：围绕组件、组合式逻辑、响应式边界和工程化设计 Vue 应用架构。 Use when an AI needs to handle Vue 3 大型应用架构, Options API 到 Composition API 演进, 组件库与业务应用分层; produce Vue 架构方案, 组件与 composable 边界, 状态、路由和测试方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
