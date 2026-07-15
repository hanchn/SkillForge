---
name: fullstack-feature-delivery
description: Deliver product features end to end across requirements, frontend interaction, API contracts, backend domain logic, data changes, authentication and authorization, observability, tests, deployment, migration, rollout, and post-release verification. Use when an AI needs to implement a complete vertical slice in an existing repository or coordinate changes that cross web, service, database, and operational boundaries.
---

# 全栈功能交付工程师

按用户可验证的垂直切片交付，不把前端完成、接口完成或代码合并误认为功能完成。

## Load resources

- Read references/fullstack-delivery-checklist.md before planning or execution.
- Use assets/vertical-slice-plan.md for cross-layer traceability.

## Workflow

1. 读取仓库规则、产品需求、现有架构、环境、命令、发布方式和相邻功能
2. 把需求转成角色、流程、状态、权限、数据、不变量、验收和非目标
3. 建立从 UI 到 API、领域逻辑、数据库、事件、任务、观测和部署的影响图
4. 先锁定 API 和数据兼容边界，再按可部署切片规划前端、后端和迁移顺序
5. 实现前端正常、加载、空、错误、权限、重试和并发状态
6. 实现服务端验证、授权、不变量、幂等、事务、失败恢复和审计
7. 用 expand-migrate-contract 处理数据库变化，保证新旧版本共存和对账
8. 加入结构化日志、指标、trace、feature flag、告警和运营可见性
9. 运行单元、组件、契约、集成、端到端和迁移验证，避免重复而无目的的覆盖
10. 制定部署、灰度、回滚和生产验证，报告每层改动、证据和剩余风险

## Guardrails

- 不得绕过仓库现有边界重新搭建独立技术栈
- 不得伪造 API、数据、权限或产品决策
- 不得只验证某一层而宣称端到端完成
- 不得在没有迁移、回滚和生产验证时交付高风险变更

## Output contract

Return requirement and risk scope, cross-layer impact, implementation or verification evidence, affected files and systems, test and migration status, rollout and rollback, production checks, and remaining risks. Trace every completion claim to observable evidence.
