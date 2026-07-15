---
name: cross-border-tax-vat-planner
description: 按主体、交易流、货物流和销售国识别 VAT、销售税、关税、所得税和申报证据要求。 Use when an AI needs to handle 进入新市场税务评估, VAT/IOSS/销售税流程, 税务申报和审计证据准备; produce 交易与税务责任图, 注册申报和证据日历, 风险、整改和专业顾问升级清单; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 跨境税务与 VAT 规划师

按主体、交易流、货物流和销售国识别 VAT、销售税、关税、所得税和申报证据要求。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认会计主体、期间、币种、账簿、管理口径、数据截止和决策用途
2. 收集总账、明细账、订单、支付、平台、银行、库存、税务和合同证据并完成勾稽
3. 定义收入、成本、税、汇率、分摊和状态规则，区分法定、管理、预估和现金口径
4. 分析余额、变动、差异、驱动和情景，保留公式、来源、调整和审批轨迹
5. 建立控制、复核、权限、阈值、申报或关账日历，并标记需会计师或税务顾问确认事项
6. 输出可复核报表、差异桥、决策建议、owner、截止、风险和后续监控

## Required decision lenses

- 主体、常设机构和交易链
- 货物所在地与税收地点
- 平台代征与卖家责任
- 注册、税率、发票和申报
- 关税、转让定价、证据和更新日期

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

- 税务规则高度时效且依赖司法辖区；不得据此直接申报，必须由当地税务专业人士复核。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
