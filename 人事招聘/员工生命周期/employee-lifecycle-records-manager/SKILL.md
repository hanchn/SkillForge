---
name: employee-lifecycle-records-manager
description: 管理入职、异动、假勤、合同、证明、离职和员工档案的完整性、权限、保留与审计。 Use when an AI needs to handle 员工主档维护, 转岗晋升和合同变更, 离职交接与权限回收; produce 员工生命周期状态与清单, 档案完整性和权限台账, 异动、离职和审计记录; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 员工生命周期与档案管理员

管理入职、异动、假勤、合同、证明、离职和员工档案的完整性、权限、保留与审计。

## Load resources

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

- 员工唯一标识和数据 owner
- 合同、职位、汇报和成本中心
- 假勤、证明和变更证据
- 离职、资产和账号回收
- 最小权限、保留、删除和审计日志

## Guardrails

- 不得在普通协作空间暴露身份证件、银行、健康等敏感信息；删除和保留必须遵守适用规则和诉讼保全。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
