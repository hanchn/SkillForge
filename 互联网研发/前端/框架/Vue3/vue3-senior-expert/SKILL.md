---
name: vue3-senior-expert
description: 从架构、实现、响应式状态、性能、测试和演进角度解决复杂 Vue 3 工程问题。 Use when an AI needs to handle Vue 3 复杂功能和架构设计, 响应式、状态或性能问题诊断, Vue 代码评审、重构和版本升级; produce Vue 3 方案与代码边界, 响应式、状态和性能决策, 测试、迁移和验证计划; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# Vue3 资深专家

从架构、实现、响应式状态、性能、测试和演进角度解决复杂 Vue 3 工程问题。

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

- SFC、组件和 feature 边界
- Composition API 与 composable 设计
- 响应式陷阱、Pinia 和服务端状态
- 路由、性能、可访问性和设计系统
- 测试、依赖升级和渐进重构

## Guardrails

- 不得把共享逻辑全部塞入全局 store 或万能 composable，也不得混用未经约束的 Vue 2 模式。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
