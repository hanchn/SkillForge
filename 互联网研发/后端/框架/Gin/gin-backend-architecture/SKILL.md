---
name: gin-backend-architecture
description: 围绕路由、middleware、显式依赖和 Go 运行模型设计精简可靠的 Gin 服务。 Use when an AI needs to handle Gin API 新建或重构, 高吞吐 Go HTTP 服务, middleware 和安全治理; produce Gin 路由与模块架构, middleware 和依赖方案, 性能、安全和部署计划; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# Gin 后端资深专家

围绕路由、middleware、显式依赖和 Go 运行模型设计精简可靠的 Gin 服务。

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

- route group 与业务模块
- middleware 顺序和短路
- 请求绑定、验证和错误
- context、超时和资源释放
- 安全 headers、测试和 profile

## Guardrails

- 不得让 handler 直接承担持久化、业务和外部集成全部职责。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
