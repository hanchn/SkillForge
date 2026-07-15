# ASP.NET Core 架构

## 分类定位

处理 host、DI、middleware、endpoint 和生产运行。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [ASP.NET Core 后端资深专家](aspnet-core-backend-architecture/README.md)：围绕 host、依赖注入、middleware、endpoint、配置和可观测性设计生产级 ASP.NET Core 架构。适用于ASP.NET Core API、模块化 .NET 后端、Minimal API 与 Controller 架构评审，交付ASP.NET Core 模块架构、DI 与请求管道、数据、安全和生产运行方案。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
