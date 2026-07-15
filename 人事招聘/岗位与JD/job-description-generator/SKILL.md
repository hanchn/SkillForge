---
name: job-description-generator
description: 先把业务岗位翻译成供 HR 学习和确认的详细岗位介绍，再生成招聘预问问题、内部岗位说明书、候选人版 JD 与可复用空白 JD 模板，避免因岗位理解偏差招错人。 Use when an AI needs to handle HR 不熟悉技术、运营或专业岗位时的招聘需求培训, 新增或重写招聘 JD, 岗位职责模糊、要求堆砌或招聘双方理解不一致, 多平台、多语言或跨区域岗位发布; produce HR 岗位培训与详细岗位介绍, 招聘需求澄清与建议预问问题, 内部岗位说明书, 候选人版招聘 JD, 可复制的 JD 空白模板, 能力证据、面试评估和发布检查表; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 岗位说明书与招聘 JD 生成专家

先把业务岗位翻译成供 HR 学习和确认的详细岗位介绍，再生成招聘预问问题、内部岗位说明书、候选人版 JD 与可复用空白 JD 模板，避免因岗位理解偏差招错人。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

- 必须读取 `references/hr-role-training-checklist.md`，先完成 HR 岗位理解与招聘经理预问，不得在关键事实未确认时直接发布 JD。
- 使用 `assets/delivery-template.md` 交付完整招聘包，并原样附带 `assets/blank-jd-template.md` 作为可复用 JD 空白模板。


## Workflow

1. 先向招聘经理收集业务目标、为何现在招聘、岗位解决的问题、首年关键结果、工作地、用工主体、编制、预算与时间；缺失项进入预问清单，不得猜测
2. 生成供 HR 学习的详细岗位介绍：业务背景、典型工作日、主要任务、真实交付物、上下游、工具系统、专业术语、职级差异、优秀与不合格表现以及常见误解
3. 生成建议预问问题并标注提问对象、目的、理想答案要素、风险答案与答案如何影响 JD；等待招聘经理确认关键分歧
4. 把确认事实转化为内部岗位说明书，定义使命、结果、职责、权限、不负责范围、协作关系、成功指标和前三十/六十/九十天预期
5. 区分必须具备、可培养和加分项，为每项定义可观察证据、作品或经历，删除愿望清单、重复要求和与岗位无关的限制
6. 生成面向候选人的招聘 JD，使用可理解语言说明机会、工作、结果、要求、流程和已批准待遇信息，并执行包容性、隐私和当地合规检查
7. 同时交付保持字段和说明但不填业务事实的 JD 空白模板，最后输出未确认项、发布审批、面试评估建议和版本记录

## Required decision lenses

- 岗位存在原因、业务场景、日常工作和成功结果
- 上下游、工具系统、专业术语和 HR 常见误解
- 职责、权限、不负责范围和职级边界
- 必需能力、可培养能力、作品证据和淘汰信号
- 招聘经理预问问题、答案口径和未确认项
- 工作地、用工方式、汇报、协作、薪酬披露与当地合规

## Guardrails

- 不得在 HR 尚未理解或招聘经理尚未确认岗位关键事实时直接定稿发布；不得虚构薪资、福利、组织承诺或岗位事实，也不得加入与工作无关或可能造成歧视的年龄、性别、婚育、户籍、健康等条件。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
