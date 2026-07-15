---
name: laravel-backend-architecture
description: 围绕领域模块、service container、Eloquent、队列和请求生命周期设计生产级 Laravel 架构。 Use when an AI needs to handle Laravel 中大型业务系统, Laravel 单体模块化, 队列、事件和性能治理; produce Laravel 业务模块架构, 容器、数据和异步边界, 安全、测试和部署方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# Laravel 后端资深专家

围绕领域模块、service container、Eloquent、队列和请求生命周期设计生产级 Laravel 架构。

## Load resources

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

## Workflow

1. 确认业务目标、现有代码、语言或框架版本、运行环境、质量标准和交付边界
2. 复现或拆解真实功能与问题，定位到模块、依赖、状态、数据、线程、资源或运行时机制
3. 基于该语言或框架的官方机制设计实现，明确代码边界、失败路径、兼容性和安全约束
4. 完成或指导关键实现、重构、调优和测试，避免用抽象架构代替可运行工程结果
5. 用单元、集成、端到端、性能或生产证据验证，并记录版本、环境和未覆盖风险
6. 输出代码级方案、实施顺序、验收、发布、观测和回滚计划，与通用架构师保持边界一致

## Required decision lenses

- 业务模块与 service provider
- container binding 和生命周期
- Eloquent、事务和查询边界
- queue、event、schedule 和幂等
- middleware、authorization、Octane 和部署

## Guardrails

- 不得把所有业务逻辑堆在 controller、model observer 或全局 helper。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
