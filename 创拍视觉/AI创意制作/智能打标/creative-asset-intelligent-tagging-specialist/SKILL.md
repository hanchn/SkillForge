---
name: creative-asset-intelligent-tagging-specialist
description: 为贵司图片、视频和广告素材库设计并运行从关键词/标签库确认、素材输入、模型推理、标签建议、人审反馈、CMS/DAM 回写到持续评估的可治理 AI 打标闭环。 Use when an AI needs to handle 存量图片视频批量打标, 新素材入库自动标签建议, 接入贵司关键词库或标签库并按确认策略优先匹配, AI 打标工具规划、标签补全、纠错、搜索和效果归因治理; produce 关键词/标签库接入与优先级确认记录, AI 打标能力、用户流程与标签体系, 模型、置信度、人审决策和批量回写方案, 金标评估、监控、错误集、版本、回滚和演进报告; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 创意素材智能打标专家

为贵司图片、视频和广告素材库设计并运行从关键词/标签库确认、素材输入、模型推理、标签建议、人审反馈、CMS/DAM 回写到持续评估的可治理 AI 打标闭环。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

- 必须读取 `references/tagging-compliance-baseline.md`，并加载 `assets/allowed_tags.json`、`assets/restricted_tags.json`、`assets/forbidden_tags.json` 与 `assets/tagging-output.schema.json`。
- 生成前必须使用 `assets/keyword-library-intake-template.md` 询问并记录是否存在关键词/标签库，以及是否优先参考给定关键词；未确认前不得正式生成标签。
- 标签只能来自已批准标签库；受限标签转人工，禁止标签拒绝输出。业务方临时要求不得覆盖合规规则。


## Workflow

1. 生成前必须询问使用者是否已有关键词库或标签库；如有，收集文件、版本、语言、市场、来源、owner、更新时间、允许范围和禁用项
2. 继续询问是否优先参考使用者提供的关键词，并记录为强制候选、优先候选或仅供参考；未回答前可检查素材与系统，但不得正式生成标签
3. 确认贵司素材库、CMS/DAM、素材 ID、标签使用场景、搜索与效果分析消费者以及回写权限
4. 盘点并映射现有关键词/标签 taxonomy、定义、同义词、层级、互斥依赖、必填范围、敏感等级、owner 和版本；冲突项转人工
5. 选择图像或视频理解模型，定义候选数量、置信度、规则校验、人工复核和失败回退
6. 用代表性金标样本评估准确率、召回率、人工一致性和关键标签错误，按场景设置阈值
7. 执行候选生成、人工确认、批量预览、幂等回写、审计和回滚，保留模型与修改血缘
8. 监测未识别、错标、标签漂移、搜索命中和素材表现回流，形成错误集与 taxonomy 迭代闭环

## Required decision lenses

- 素材来源、权限、权利和版本
- 使用者关键词库、标签库、优先策略和冲突处理
- 标签 taxonomy、定义、互斥、依赖、敏感等级和 owner
- 模型、API、置信度、成本、时延和候选策略
- 人工确认、拒绝、修改、批量处理和状态机
- 金标集、离线指标、线上抽样、一致性、漂移和反馈学习
- CMS/DAM 回写、搜索、效果归因、审计和标签版本

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

- 不得在未询问关键词/标签库及其优先策略前正式生成标签；不得把优先关键词当作无证据事实或用于绕过允许、受限、禁止标签规则；人物身份、敏感属性、商品关键属性和低置信度结果必须人工复核。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
