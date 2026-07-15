---
name: go-backend-architecture
description: 按 Go 的显式依赖、并发模型和简洁包边界设计可靠后端。 Use when an AI needs to handle Go API 或任务服务, 高并发 Go 服务治理, Go 单仓多服务架构; produce Go 包与服务架构, 并发和取消模型, 错误、测试和部署方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# Go 后端资深专家

按 Go 的显式依赖、并发模型和简洁包边界设计可靠后端。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

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

- package 责任与依赖方向
- context、goroutine 和背压
- 错误语义与接口最小化
- 配置、资源池和优雅停机
- 测试、profile 和发布

## Guardrails

- 不得滥用 goroutine、全局状态或过度抽象接口。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
