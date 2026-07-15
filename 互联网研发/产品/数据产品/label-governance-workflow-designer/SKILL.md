---
name: label-governance-workflow-designer
description: 设计标签创建、修改、审核、发布、版本、回滚、权限、质量和血缘治理工作流。 Use when an AI needs to handle 透明计划等标签修改项目, 标签审核和发布流程, 标签冲突、版本和质量治理; produce 标签生命周期和状态机, 角色权限、审核与发布流程, 版本、审计、回滚和质量方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 标签治理与审核工作流设计师

设计标签创建、修改、审核、发布、版本、回滚、权限、质量和血缘治理工作流。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认项目名称、用户角色、业务目标、标签对象、输入来源、下游消费者和不在范围内的事项
2. 定义标签 taxonomy、语义、owner、版本、互斥/依赖规则、质量标准和敏感等级
3. 设计模型建议、置信度、人工审核、修改、发布、回滚和异常处理的端到端状态机
4. 明确模型/API/脚本等 Tool 的输入输出契约、权限、成本、时延、失败和可观测要求
5. 建立金标集、离线指标、线上采样、人工一致性、漂移和错误反馈评估体系
6. 按 MVP、人审增强、自动化和规模治理输出路线、验收、审计与回滚方案

## Required decision lenses

- 标签对象、taxonomy 和 owner
- 草稿、审核、发布和废弃状态
- 修改原因、diff 和影响范围
- 权限、双人复核和批量操作
- 版本、血缘、回滚和质量指标

## Guardrails

- 不得覆盖历史标签或丢失修改证据；批量修改必须提供影响预览、审批、幂等和回滚。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
