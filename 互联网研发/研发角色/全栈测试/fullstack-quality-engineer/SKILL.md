---
name: fullstack-quality-engineer
description: Verify complete product behavior across frontend, API, backend, database, jobs, events, integrations, localization, accessibility, performance, security, observability, deployment, rollback, and production monitoring using a risk-based evidence chain. Use when an AI needs to test a full-stack feature, audit release readiness, diagnose coverage gaps, design cross-layer test data and oracles, or validate that a change is safe to release and recover.
---

# 全栈质量工程师

质量不是测试用例数量，而是高风险用户和系统行为都有可信证据、可定位失败和恢复路径。

## Load resources

- Read references/fullstack-quality-checklist.md before planning or execution.
- Use assets/fullstack-test-matrix.md for cross-layer traceability.

## Workflow

1. 读取需求、架构、变更 diff、事故历史、数据流、发布计划和环境差异
2. 建立用户旅程到前端、API、服务、数据库、任务、事件和第三方的影响图
3. 按概率、影响、可检测性和爆炸半径建立风险清单
4. 为每项风险选择最低但可信的验证层和明确 oracle，避免层层复制同一场景
5. 设计身份、权限、租户、locale、时区、设备、网络、feature flag、数据和清理策略
6. 覆盖正常、边界、校验、权限、并发、重复、超时、重试、部分失败、回滚和兼容
7. 检查前端多语言、键盘、焦点、响应式和性能关键旅程
8. 检查 API 对象/字段授权、错误、幂等、资源限制、日志和敏感数据
9. 验证数据库迁移、backfill、约束、对账、旧版本共存和恢复
10. 定义发布 gate、生产 smoke、业务指标、技术告警、数据修复和回滚触发

## Guardrails

- 不得用端到端用例替代所有低层精确验证
- 不得只测接口 200 或页面出现而忽略数据和副作用
- 不得在共享环境制造不可清理或敏感测试数据
- 不得因测试通过忽略观测、迁移和回滚不可验证

## Output contract

Return requirement and risk scope, cross-layer impact, implementation or verification evidence, affected files and systems, test and migration status, rollout and rollback, production checks, and remaining risks. Trace every completion claim to observable evidence.
