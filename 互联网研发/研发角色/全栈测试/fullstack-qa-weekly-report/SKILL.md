---
name: fullstack-qa-weekly-report
description: Create evidence-backed full-stack quality weekly reports from requirements, risk assessments, test plans, executions, automation, defects, regressions, environments, releases, production verification, incidents, and quality metrics. Use when an AI needs to summarize weekly testing and quality status, report release readiness, explain uncovered risks and blockers, compare quality trends with consistent definitions, or plan next-week verification without treating raw test counts as quality.
---

# 全栈测试资深专家周报

周报围绕风险是否被验证和版本是否可安全发布，不用用例执行数量制造质量感。

## Load resources

- Read references/weekly-quality-evidence.md before drafting.
- Use assets/qa-weekly-template.md for the final report.

## Workflow

1. 锁定报告周期、时区、版本/项目范围、发布节点和是否需要对比上周
2. 盘点需求、风险矩阵、测试计划、执行记录、自动化、缺陷、环境、发布和生产证据
3. 按用户旅程和风险领域聚合前端、API、后端、数据、性能、安全与兼容验证
4. 区分已覆盖、部分覆盖、未覆盖、阻塞和不适用，并记录可信 oracle
5. 汇总缺陷时保留严重度、影响、状态、归属版本和复现证据，避免只报数量
6. 评估 release gate、迁移、回归、生产 smoke、监控和回滚验证
7. 质量指标必须保留分母、口径、周期和历史可比性，说明样本不足
8. 把环境、数据、依赖和权限问题与产品缺陷分开
9. 输出当前质量结论、发布建议、剩余风险和需要决策的阻塞项
10. 下周计划以关闭高风险证据缺口和版本 gate 为主，不机械追求更多用例

## Guardrails

- 不得用通过率掩盖未覆盖高风险行为
- 不得把环境故障或数据问题自动算作产品缺陷
- 不得把缺陷关闭等同根因消除和回归完成
- 不得编造 release ready、覆盖率、缺陷趋势或生产质量结论

## Output contract

Return a concise weekly conclusion, verified completed work, in-progress and blocked work, delivery or quality evidence, risks and decisions, next-week priorities with acceptance, and an evidence appendix. If comparison is requested, keep the same period length and metric definitions.
