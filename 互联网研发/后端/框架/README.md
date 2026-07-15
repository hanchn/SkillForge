# 后端框架架构

## 分类定位

在通用和语言架构上处理具体框架的模块、依赖和生产能力。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [ASP.NET Core 后端资深专家](ASP.NET Core/aspnet-core-backend-architecture/README.md)：围绕 host、依赖注入、middleware、endpoint、配置和可观测性设计生产级 ASP.NET Core 架构。适用于ASP.NET Core API、模块化 .NET 后端、Minimal API 与 Controller 架构评审，交付ASP.NET Core 模块架构、DI 与请求管道、数据、安全和生产运行方案。
- [FastAPI 后端资深专家](FastAPI/fastapi-backend-architecture/README.md)：围绕 APIRouter、依赖注入、Pydantic 契约和异步边界设计生产级 FastAPI 服务。适用于FastAPI 中大型应用、Python API 模块化、异步 API 性能和可靠性治理，交付FastAPI 包与路由架构、依赖和数据契约、运行、测试和部署方案。
- [Gin 后端资深专家](Gin/gin-backend-architecture/README.md)：围绕路由、middleware、显式依赖和 Go 运行模型设计精简可靠的 Gin 服务。适用于Gin API 新建或重构、高吞吐 Go HTTP 服务、middleware 和安全治理，交付Gin 路由与模块架构、middleware 和依赖方案、性能、安全和部署计划。
- [Laravel 后端资深专家](Laravel/laravel-backend-architecture/README.md)：围绕领域模块、service container、Eloquent、队列和请求生命周期设计生产级 Laravel 架构。适用于Laravel 中大型业务系统、Laravel 单体模块化、队列、事件和性能治理，交付Laravel 业务模块架构、容器、数据和异步边界、安全、测试和部署方案。
- [NestJS 后端资深专家](NestJS/nestjs-backend-architecture/README.md)：围绕 module、provider、边界契约和请求管道设计模块化 NestJS 系统。适用于NestJS 企业 API、模块边界和依赖治理、单体到服务化演进，交付NestJS 模块架构、provider 与请求管道设计、测试和部署方案。
- [Spring Boot 后端资深专家](Spring Boot/spring-boot-backend-architecture/README.md)：围绕业务模块、依赖注入、事务、安全和 Actuator 设计生产级 Spring Boot 架构。适用于Spring Boot 服务新建或重构、模块化单体与服务拆分、生产可观测和升级治理，交付Spring Boot 模块架构、事务与集成边界、生产运行和迁移方案。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
