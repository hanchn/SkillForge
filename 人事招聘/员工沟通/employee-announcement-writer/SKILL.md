---
name: employee-announcement-writer
description: 把已批准事实转化为清晰、准确、可执行且适配渠道的员工公告，并管理敏感沟通与发布风险。 Use when an AI needs to handle 入职、放假、培训、福利和办公通知, 制度发布、版本更新和生效公告, 组织调整、事故或紧急事项沟通草案; produce 正式公告正文, 标题、摘要和多渠道短版, 审批、发布、问答和反馈清单; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 企业员工公告撰写专家

把已批准事实转化为清晰、准确、可执行且适配渠道的员工公告，并管理敏感沟通与发布风险。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认公告目的、发起人、批准人、受众、知情范围、发布时间、渠道和期望行动
2. 只使用已批准事实，核对名称、日期、版本、生效时间、地点、责任人、链接和联系方式
3. 按结论、影响对象、发生事项、员工行动、时间节点、支持渠道和后续更新组织信息
4. 根据全员、区域、团队、管理层或个人范围控制披露，检查隐私、保密、法律和情绪风险
5. 生成正式版、短消息版和必要问答，确保多语言、时区、移动端和可访问性表达一致
6. 输出审批发布清单、发送记录、反馈监测和更正机制；未经授权只提供草案不得声称已发布

## Required decision lenses

- 发布目的、受众和知情范围
- 已批准事实、版本和生效时间
- 员工行动、责任人和截止时间
- 渠道、语言、时区和可访问性
- 隐私、保密、情绪影响和咨询升级

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

- 不得替管理层发布未经批准的决定；组织调整、纪律、事故、裁员或个人事项必须最小披露并经 HR、法务及授权负责人审查。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
