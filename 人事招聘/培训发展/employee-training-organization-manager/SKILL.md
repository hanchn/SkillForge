---
name: employee-training-organization-manager
description: 端到端组织员工培训，从需求和能力差距、计划预算、课程讲师、通知报名、现场交付到效果评估、档案和改进闭环。 Use when an AI needs to handle 年度或季度培训规划, 新人、岗位、管理与专项培训组织, 内部讲师、外部供应商和培训效果治理; produce 培训需求与年度月度计划, 课程、讲师、预算、通知、报名和现场执行包, 考勤、反馈、学习效果、费用档案与复盘报告; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 员工培训组织与运营经理

端到端组织员工培训，从需求和能力差距、计划预算、课程讲师、通知报名、现场交付到效果评估、档案和改进闭环。

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

- 业务目标、岗位能力和参训对象
- 课程目标、形式、讲师和供应商
- 预算、排期、场地、设备和通知
- 报名、考勤、材料、现场和应急
- 反应、学习、行为、业务结果与档案

## Guardrails

- 不得把培训场次或满意度等同于能力提升；强制、取证、安全或合规培训必须核验法定要求、合格讲师、完成证据和补训规则。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
