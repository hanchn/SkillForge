# Vue 架构

## 分类定位

处理 Vue 组件、组合式逻辑、响应式状态和工程边界。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [Vue 前端架构师](vue-frontend-architecture/README.md)：围绕组件、组合式逻辑、响应式边界和工程化设计 Vue 应用架构。 Use when an AI needs to handle Vue 3 大型应用架构, Options API 到 Composition API 演进, 组件库与业务应用分层; produce Vue 架构方案, 组件与 composable 边界, 状态、路由和测试方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
