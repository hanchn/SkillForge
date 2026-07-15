---
name: java-backend-architecture
description: 利用 Java 类型、并发、JVM 和模块生态设计长期可维护的后端系统。 Use when an AI needs to handle Java 服务平台架构, 大型 Java 单体模块化, JVM 性能和升级治理; produce Java 模块架构, 并发与资源模型, JVM 运行和演进方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# Java 后端资深专家

利用 Java 类型、并发、JVM 和模块生态设计长期可维护的后端系统。

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

- package/module 依赖
- 线程、虚拟线程和阻塞边界
- 异常、空值和领域类型
- JVM 内存、GC 和观测
- 构建、依赖和版本升级

## Guardrails

- 不把框架注解当作领域架构，也不在未测量前做 JVM 调优。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
