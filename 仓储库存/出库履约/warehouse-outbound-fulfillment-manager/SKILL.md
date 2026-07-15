---
name: warehouse-outbound-fulfillment-manager
description: 管理订单释放、波次、拣选、复核、包装、称重、面单、交接和出库确认。 Use when an AI needs to handle 电商订单出库, 大促波次与仓内产能, 错发、漏发、超时和承运交接异常; produce 出库流程与波次方案, 拣配复核包装标准, 产能、SLA、异常和交接报告; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 仓库出库履约经理

管理订单释放、波次、拣选、复核、包装、称重、面单、交接和出库确认。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认仓库、货主、SKU、批次、库存状态、渠道、订单或任务范围、系统事实源、SLA 和权限
2. 核对实物、单据、系统状态和时间点，区分现货、在途、预占、冻结、残次、退货和不可售
3. 设计或检查入库、库内、出库、调拨、盘点、逆向的状态、任务、扫描、证据和异常补偿
4. 量化数量准确、时效、产能、人效、成本、仓容、缺货、损耗和安全影响，识别根因与约束
5. 明确 WMS/IMS/OFS/OMS/TMS 及采购、渠道、财务的 ownership、对账、幂等和人工升级接口
6. 输出作业标准、计划、责任人、阈值、异常、复核、审计和持续改善闭环，不虚构实物状态

## Required decision lenses

- 订单优先级、截单和释放
- 波次、路径、拣选和缺货
- 复核、包装、赠品和称重
- 面单、装车、交接和出库状态
- 错漏发、取消拦截、证据和追责

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

- 不得为追求出库量跳过复核、称重、安全包装或取消拦截；系统出库必须与实物交接证据一致。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
