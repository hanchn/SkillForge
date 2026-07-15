---
name: frontend-state-integration-designer
description: Design and review predictable frontend state, URL state, form state, server cache, asynchronous queries, mutations, optimistic updates, invalidation, race handling, offline behavior, and error recovery. Use when an AI needs to decide where state belongs, integrate frontend features with APIs, repair stale or duplicated state, prevent async race bugs, or document a complex UI data flow.
---

# 前端状态与数据流设计师

每份状态只能有一个权威来源；能派生就不复制，服务端事实不伪装成本地真相。

## Load resources

- Read references/state-decision-checklist.md before design, implementation, or diagnosis.
- Use assets/state-flow-template.md for the final artifact and handoff.

## Workflow

1. 列出页面中所有状态及其所有者、生命周期、持久化和共享范围
2. 分类为 URL、服务端缓存、表单草稿、本地交互、全局客户端、环境或派生状态
3. 删除可派生副本并定义单一 source of truth 与同步边界
4. 为查询定义 key、参数、启用条件、新鲜度、缓存、失效、分页和取消
5. 为 mutation 定义验证、幂等、pending、重复提交、乐观更新、回滚、重新获取和错误呈现
6. 处理路由切换、过期响应、快速筛选、并发编辑、tab 多开和权限变化
7. 明确 loading、empty、partial、stale、error 和 retry 的 UI 语义
8. 定义敏感数据、持久化、日志和缓存清理边界
9. 绘制事件到状态再到渲染和副作用的数据流
10. 用竞态、失败、回退和恢复案例验证设计

## Guardrails

- 不得把服务端数据无理由复制进全局 store
- 不得用 effect 链修补可计算状态
- 不得把 loading 当作唯一异步状态
- 不得乐观更新不可安全回滚或高风险操作

## Output contract

Return inspected evidence, decisions and tradeoffs, implementation or action plan, affected files or systems, verification results, risks, rollback or recovery where relevant, and remaining unknowns. Do not claim completion without proportionate validation.
