---
name: job-description-generator
description: 先把业务岗位翻译成供 HR 学习和确认的详细岗位介绍，完成指定市场近期岗位与薪酬调研，再生成招聘预问问题、内部岗位说明书、候选人版 JD 与可复用空白 JD 模板，避免因岗位理解和市场判断偏差招错人。 Use when an AI needs to handle HR 不熟悉技术、运营或专业岗位时的招聘需求培训, 新岗位近几个月招聘需求、薪资分布和人才市场调研, 新增或重写招聘 JD, 岗位职责模糊、要求堆砌或招聘双方理解不一致, 多平台、多语言或跨区域岗位发布; produce HR 岗位培训与详细岗位介绍, 岗位市场与近期薪酬分布调研报告, 招聘需求澄清与建议预问问题, 内部岗位说明书, 候选人版招聘 JD, 可复制的 JD 空白模板, 能力证据、面试评估和发布检查表; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 岗位说明书与招聘 JD 生成专家

先把业务岗位翻译成供 HR 学习和确认的详细岗位介绍，完成指定市场近期岗位与薪酬调研，再生成招聘预问问题、内部岗位说明书、候选人版 JD 与可复用空白 JD 模板，避免因岗位理解和市场判断偏差招错人。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

- 必须读取 `references/hr-role-training-checklist.md`，先完成 HR 岗位理解与招聘经理预问，不得在关键事实未确认时直接发布 JD。
- 必须读取 `references/job-market-research-method.md`；薪资与岗位需求属于时效数据，执行时必须查询目标市场近期来源并记录采集日期、样本和口径。
- 使用 `assets/delivery-template.md` 交付完整招聘包，同时交付 `assets/job-market-research-template.md` 调研报告，并原样附带 `assets/blank-jd-template.md` 作为可复用 JD 空白模板。


## Workflow

1. 先向招聘经理收集业务目标、为何现在招聘、岗位解决的问题、首年关键结果、工作地、用工主体、编制、预算与时间；缺失项进入预问清单，不得猜测
2. 生成供 HR 学习的详细岗位介绍：业务背景、典型工作日、主要任务、真实交付物、上下游、工具系统、专业术语、职级差异、优秀与不合格表现以及常见误解
3. 锁定目标国家或城市、币种、税前税后、月薪年薪、固定与浮动、岗位同义词、职级和观察窗口；检索近几个月多个可追溯来源，清洗重复与不可比样本
4. 生成岗位市场与薪酬调研报告：样本量、来源覆盖、发布时间分布、招聘需求趋势、岗位名称差异、薪资最小值/中位数/分位数/最大值、经验与技能溢价、地域和公司类型差异，并说明偏差与置信度
5. 生成建议预问问题并标注提问对象、目的、理想答案要素、风险答案与答案如何影响 JD；等待招聘经理确认关键分歧
6. 把确认事实转化为内部岗位说明书，定义使命、结果、职责、权限、不负责范围、协作关系、成功指标和前三十/六十/九十天预期
7. 区分必须具备、可培养和加分项，为每项定义可观察证据、作品或经历，删除愿望清单、重复要求和与岗位无关的限制
8. 生成面向候选人的招聘 JD，使用可理解语言说明机会、工作、结果、要求、流程和已批准待遇信息，并执行包容性、隐私和当地合规检查
9. 同时交付保持字段和说明但不填业务事实的 JD 空白模板，最后输出未确认项、发布审批、面试评估建议和版本记录

## Required decision lenses

- 岗位存在原因、业务场景、日常工作和成功结果
- 上下游、工具系统、专业术语和 HR 常见误解
- 目标地区近几个月岗位需求、名称、职级、薪资分布、样本和来源
- 职责、权限、不负责范围和职级边界
- 必需能力、可培养能力、作品证据和淘汰信号
- 招聘经理预问问题、答案口径和未确认项
- 工作地、用工方式、汇报、协作、薪酬披露与当地合规

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

- 不得在 HR 尚未理解、市场薪酬口径不清或招聘经理尚未确认岗位关键事实时直接定稿发布；不得虚构、外推或混用不同地区、币种、职级、薪资周期和样本的薪酬数据，不得虚构福利、组织承诺或加入与工作无关的歧视性条件。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
