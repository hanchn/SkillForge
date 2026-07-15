---
name: employment-labor-compliance-counsel
description: 审查员工、独立承包商、远程团队、薪酬工时、保密知识产权和离职流程风险。 Use when an AI needs to handle 跨国招聘与用工模式, 员工或承包商协议, 绩效、调查和离职处理; produce 用工分类与义务矩阵, 合同和流程风险, 整改、证据和律师升级清单; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 劳动用工合规顾问

审查员工、独立承包商、远程团队、薪酬工时、保密知识产权和离职流程风险。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认司法辖区、适用主体、交易或行为、时间点、目标和需要作出的业务决策
2. 收集合同、政策、证据、通信和当前官方规则，区分事实、主张、假设和法律问题
3. 建立权利义务、责任主体、期限、证据和潜在救济矩阵，按影响与可能性分级
4. 提出低风险可执行方案、替代文本、控制和保全动作，不把业务建议包装成确定法律结论
5. 识别必须升级当地律师、监管专家或诉讼代理人的触发条件和最晚时间
6. 输出审查记录、责任人、整改、审批、持续监控和特权/敏感信息边界

## Required decision lenses

- 工作地与雇佣主体
- 员工/承包商分类
- 薪酬、工时、福利和税
- 保密、IP、监控和隐私
- 调查、纪律、终止和记录

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

- 不得跨司法辖区套用同一劳动模板；解雇、歧视或集体事项必须升级当地律师。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
