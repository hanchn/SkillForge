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
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
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

## Depth requirements

- 先解释业务对象、术语、为什么要做、谁使用结果以及错误结果会造成什么后果，再进入执行。
- 覆盖当前场景及与其相邻的高频变体；不得用同一套步骤忽略国家、渠道、职级、系统状态、数据成熟度或风险等级差异。
- 明确上游输入、下游消费者、责任边界、决策权、审批人、系统事实源和人工交接点。
- 对每个关键判断给出所需证据、可选方案、选择条件、反证、停止条件和不可逆风险。
- 同时设计正常路径、缺数据、低置信度、冲突、超时、权限不足、部分成功、回滚和转人工路径。
- 工具只是执行手段；必须说明工具输入输出、权限、失败、成本、时效、版本和人工验收，不能把调用工具等同于完成业务。
- 交付物必须让下游能直接执行或审批，并包含 owner、依赖、时间、验收指标、审计证据和下一次复盘触发器。

## Scenario and exception gates

1. 从 `references/scenario-playbook.md` 选择主场景；同时检查是否命中第二场景或高风险变体。
2. 关键事实、权限、口径或 source of truth 未确认时，降级为调研、草案或 `REVIEW_REQUIRED`，不得伪装成可执行定稿。
3. 发现目标冲突时，明确收入、利润、现金、客户、质量、时效、合规和可逆性之间的取舍，记录决策人。
4. 执行中出现部分失败时，保护已确认结果，隔离未知状态，停止扩大影响，提供对账、补偿或回滚步骤。
5. 只有交付物、验证证据、责任交接和剩余风险同时清楚，任务才算完成。

## Guardrails

- 不得覆盖历史标签或丢失修改证据；批量修改必须提供影响预览、审批、幂等和回滚。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
