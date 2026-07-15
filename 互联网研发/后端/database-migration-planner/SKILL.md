---
name: database-migration-planner
description: Plan, implement, and verify safe database schema and data migrations using dependency analysis, locking and runtime estimates, expand-migrate-contract sequencing, backfills, dual reads or writes, reconciliation, constraints, indexes, rollout gates, rollback, and recovery. Use when an AI needs to add, change, split, merge, backfill, index, constrain, or retire production database structures without corrupting data or causing avoidable downtime.
---

# 数据库变更迁移规划师

数据库迁移是跨版本协议，不是一条能在本地执行成功的 ALTER 语句。

## Load resources

- Read references/migration-safety-checklist.md before design, implementation, or diagnosis.
- Use assets/migration-runbook-template.md for the final artifact and handoff.

## Workflow

1. 确认数据库、版本、表规模、流量、复制、备份、部署模型、SLO 和变更目标
2. 读取 schema、查询、ORM、任务、报表和下游依赖，建立读写影响图
3. 评估锁、表重写、索引构建、WAL/日志、复制延迟、磁盘和运行时间
4. 将不兼容变更拆成 expand、migrate、verify、switch 和 contract 阶段
5. 为 backfill 定义批次、顺序、节流、可重入、断点、失败重试和线上负载保护
6. 设计双读/双写或兼容代码时明确 source of truth、顺序、失败和退出条件
7. 建立行数、空值、唯一性、外键、汇总、抽样和业务不变量对账
8. 为约束和索引选择安全建立与验证顺序
9. 定义发布 gate、监控、暂停、回滚或前滚恢复以及备份恢复验证
10. 删除旧字段或路径前证明所有读取、写入、任务和下游已迁移

## Guardrails

- 不得把向下迁移脚本等同于可恢复数据
- 不得在未知表规模和锁行为下直接执行生产 DDL
- 不得删除旧列、表或索引直到依赖和保留期验证完成
- 不得依赖不可重入的一次性 backfill

## Output contract

Return inspected evidence, decisions and tradeoffs, implementation or action plan, affected files or systems, verification results, risks, rollback or recovery where relevant, and remaining unknowns. Do not claim completion without proportionate validation.
