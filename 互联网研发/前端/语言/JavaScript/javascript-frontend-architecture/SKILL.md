---
name: javascript-frontend-architecture
description: 针对 JavaScript 动态类型、模块系统和浏览器运行时设计可维护前端架构。 Use when an AI needs to handle 大型 JavaScript 应用治理, ESM 与旧模块迁移, 运行时契约和质量门禁设计; produce JavaScript 架构方案, 模块与运行时契约, 渐进治理计划; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# JavaScript 前端架构师

针对 JavaScript 动态类型、模块系统和浏览器运行时设计可维护前端架构。

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

- ES Modules 和包边界
- 运行时校验与错误隔离
- 异步、事件循环和资源生命周期
- lint、测试和兼容目标
- 依赖供应链与构建产物

## Guardrails

- 不把 TypeScript 类型系统当作已经存在的安全网。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
