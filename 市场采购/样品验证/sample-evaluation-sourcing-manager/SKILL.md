---
name: sample-evaluation-sourcing-manager
description: 管理打样需求、样品版本、功能外观评估、成本、测试、用户验证和量产放行证据。 Use when an AI needs to handle 新品打样和多供应商比样, 样品改版和确认, 量产前样、封样和放行; produce 样品需求与版本台账, 比样、测试和问题矩阵, 修改、封样、量产和否决决定; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 采购样品验证经理

管理打样需求、样品版本、功能外观评估、成本、测试、用户验证和量产放行证据。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认市场、渠道、类目、目标人群、商品定义、价格带、目标成本、销量、现金、交期和合规约束
2. 收集消费者、竞品、供应商、样品、成本、质量、产能和交付证据，标记来源、版本和反证
3. 通过机会门、样品门、供应商门、成本门、合规门和量产门逐步验证，不一次性拍脑袋下单
4. 定义规格、BOM、样品、报价、MOQ、付款、交期、质检、变更和责任接口，保留版本与审批
5. 评估单位经济、总拥有成本、现金周期、库存退出、集中度和中断情景，准备替代与止损方案
6. 输出决策、采购执行、owner、截止、验收、供应商绩效、风险升级和复盘，不虚构市场或供应证据

## Required decision lenses

- 规格、BOM、外观和使用场景
- 供应商、版本、日期和样品身份
- 功能、耐久、安全和包装测试
- 目标成本、可制造性和公差
- 问题关闭、黄金样、签核和变更控制

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

- 不得凭主观外观或单个样品直接量产；关键规格、测试、缺陷和版本必须可追溯并经授权角色签核。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
