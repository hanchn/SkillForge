# Spring Boot 架构

## 分类定位

处理模块、依赖注入、事务、安全和生产可观测。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [Spring Boot 后端架构师](spring-boot-backend-architecture/README.md)：围绕业务模块、依赖注入、事务、安全和 Actuator 设计生产级 Spring Boot 架构。适用于Spring Boot 服务新建或重构、模块化单体与服务拆分、生产可观测和升级治理，交付Spring Boot 模块架构、事务与集成边界、生产运行和迁移方案。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
