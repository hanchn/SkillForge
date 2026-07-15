---
name: laravel-backend-architecture
description: 围绕领域模块、service container、Eloquent、队列和请求生命周期设计生产级 Laravel 架构。 Use when an AI needs to handle Laravel 中大型业务系统, Laravel 单体模块化, 队列、事件和性能治理; produce Laravel 业务模块架构, 容器、数据和异步边界, 安全、测试和部署方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# Laravel 后端架构师

围绕领域模块、service container、Eloquent、队列和请求生命周期设计生产级 Laravel 架构。

## Load resources

- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

## Workflow

1. 检查现有仓库、运行拓扑、质量目标、团队边界和约束；区分已验证事实、假设与未知项
2. 建立系统上下文、关键用户旅程或请求路径，明确边界外依赖和非功能目标
3. 按业务能力划分模块，定义 ownership、依赖方向、公共契约和禁止跨越的边界
4. 设计数据、状态、错误、权限、缓存、并发和资源生命周期，不只覆盖正常路径
5. 评估备选架构的复杂度、性能、可靠性、交付成本和可逆性，记录决策理由
6. 制定增量实施、兼容迁移、验证、观测、灰度和回滚计划

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
