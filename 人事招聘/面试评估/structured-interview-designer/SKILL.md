---
name: structured-interview-designer
description: 按岗位成功标准设计结构化面试、工作样本、评分锚点和独立评估机制。 Use when an AI needs to handle 岗位面试方案设计, 面试官培训和校准, 候选人评审争议治理; produce 能力与证据矩阵, 面试题和评分锚点, 面试流程、校准和决策记录; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 结构化面试与评估设计师

按岗位成功标准设计结构化面试、工作样本、评分锚点和独立评估机制。

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

- 岗位成功结果和关键能力
- 问题、追问和行为证据
- 工作样本与一致评分
- 面试官分工和独立记录
- 偏见控制、候选人体验和数据最小化

## Guardrails

- 不得设计与岗位无关、侵犯隐私或歧视性的提问；AI 评分不得作为未经人工复核的唯一录用依据。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
