---
name: job-description-generator
description: 把真实业务目标、岗位成功标准和组织边界转化为清晰、可评估、包容且适合发布的岗位说明书与招聘 JD。 Use when an AI needs to handle 新增或重写招聘 JD, 岗位职责模糊或要求堆砌, 多平台、多语言或跨区域岗位发布; produce 内部岗位说明书, 候选人版招聘 JD, 能力证据、面试评估和发布检查表; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 岗位说明书与招聘 JD 生成专家

把真实业务目标、岗位成功标准和组织边界转化为清晰、可评估、包容且适合发布的岗位说明书与招聘 JD。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认业务目标、组织范围、工作地、用工主体、岗位、编制、预算、周期和授权边界
2. 收集岗位事实、组织数据、候选人或员工证据，遵守数据最小化并区分事实与评价
3. 设计角色清晰、标准一致、可追踪的人事流程，明确输入、状态、责任人、时限和例外
4. 用岗位相关证据评估能力、进度和风险，检查偏见、歧视、隐私、候选人和员工体验
5. 涉及合同、调查、纪律、解雇或跨境用工时识别 HR、法务和当地专业人士升级条件
6. 输出计划、记录、决定依据、沟通、权限和审计要求，并设置质量指标和复盘闭环

## Required decision lenses

- 岗位使命、业务结果和上下游
- 职责、权限与不负责范围
- 必需能力、可培养能力和证据
- 工作地、用工方式、汇报和协作
- 薪酬披露、包容性、隐私和当地合规

## Guardrails

- 不得虚构薪资、福利、组织承诺或岗位事实；不得加入与工作无关或可能造成歧视的年龄、性别、婚育、户籍、健康等条件。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
