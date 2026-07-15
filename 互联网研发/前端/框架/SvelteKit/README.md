# SvelteKit 架构

## 分类定位

处理文件路由、load、form actions、服务端边界和 adapter。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [SvelteKit 前端架构师](sveltekit-frontend-architecture/README.md)：围绕文件路由、load、form actions、服务端边界和 adapter 设计生产级 SvelteKit 应用。适用于SvelteKit 新项目、SSR/SSG/SPA 混合架构、SvelteKit 数据与部署治理，交付SvelteKit 路由和渲染架构、数据、表单与状态边界、adapter、观测和部署方案。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
