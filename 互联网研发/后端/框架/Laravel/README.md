# Laravel 架构

## 分类定位

处理领域模块、容器、Eloquent、队列和请求生命周期。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [Laravel 后端架构师](laravel-backend-architecture/README.md)：围绕领域模块、service container、Eloquent、队列和请求生命周期设计生产级 Laravel 架构。适用于Laravel 中大型业务系统、Laravel 单体模块化、队列、事件和性能治理，交付Laravel 业务模块架构、容器、数据和异步边界、安全、测试和部署方案。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
