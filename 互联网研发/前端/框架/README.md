# 前端框架架构

## 分类定位

在通用架构与语言架构之上处理具体框架的运行语义。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [Angular 前端架构师](Angular/angular-frontend-architecture/README.md)：围绕 standalone components、signals、依赖注入、路由和混合渲染设计大型 Angular 应用。适用于Angular 企业应用架构、NgModule 到 standalone 演进、大型团队前端平台治理，交付Angular 功能域架构、依赖注入与状态边界、渲染、测试和升级方案。
- [Next.js 前端架构师](Next.js/nextjs-frontend-architecture/README.md)：按 App Router、服务端与客户端边界、缓存和部署环境设计生产级 Next.js 架构。适用于Next.js App Router 新项目、Pages Router 迁移、电商 SEO、性能和缓存架构，交付Next.js 路由与渲染蓝图、Server/Client 边界、缓存、数据和部署方案。
- [React 前端架构师](React/react-frontend-architecture/README.md)：围绕组件、状态、数据流和渲染边界设计可演进 React 应用。适用于React 应用架构和重构、复杂状态与数据流治理、组件平台和多团队协作，交付React 架构蓝图、组件与状态边界、渲染、测试和迁移方案。
- [SvelteKit 前端架构师](SvelteKit/sveltekit-frontend-architecture/README.md)：围绕文件路由、load、form actions、服务端边界和 adapter 设计生产级 SvelteKit 应用。适用于SvelteKit 新项目、SSR/SSG/SPA 混合架构、SvelteKit 数据与部署治理，交付SvelteKit 路由和渲染架构、数据、表单与状态边界、adapter、观测和部署方案。
- [Vue 前端架构师](Vue/vue-frontend-architecture/README.md)：围绕组件、组合式逻辑、响应式边界和工程化设计 Vue 应用架构。适用于Vue 3 大型应用架构、Options API 到 Composition API 演进、组件库与业务应用分层，交付Vue 架构方案、组件与 composable 边界、状态、路由和测试方案。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
