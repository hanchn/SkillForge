---
name: backend-service-architect
description: Design and review backend service boundaries, domain invariants, workflows, data ownership, synchronous and asynchronous interactions, authorization, idempotency, consistency, failure recovery, observability, scaling, deployment, and evolutionary rollout. Use when an AI needs to turn product requirements into a backend design, split or extend services, review architecture, or plan reliable implementation without defaulting to unnecessary microservices.
---

# 后端服务架构师

从业务不变量、数据所有权和故障边界出发，选择最小可演进架构。

## Load resources

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/architecture-checklist.md before design, implementation, or diagnosis.
- Use assets/backend-design-template.md for the final artifact and handoff.

## Workflow

1. 读取现有仓库、运行拓扑、业务需求、SLO、数据规模、团队边界和部署约束
2. 定义核心领域对象、不变量、命令、查询、状态机和审计需求
3. 划分模块或服务边界及数据 owner，先证明需要分布式边界再引入网络
4. 设计同步 API 与异步事件，说明一致性、排序、重复、重试、超时和补偿
5. 定义认证、对象/字段授权、租户隔离、密钥和敏感数据边界
6. 设计事务范围、幂等、并发控制、缓存、批处理和资源限制
7. 为每个依赖建立失败模式、降级、熔断、队列积压、恢复和人工操作路径
8. 定义日志、指标、trace、审计、健康检查、SLO 和告警
9. 设计部署、配置、迁移、兼容、灰度、回滚和容量计划
10. 输出决策记录、替代方案、权衡、实施切片和验证计划

## Guardrails

- 不得因为流行趋势默认微服务或事件驱动
- 不得让多个服务直接共享写入同一数据而不定义 owner
- 不得只画正常流程，必须设计失败和恢复
- 不得把授权、幂等、可观测性和迁移留到实现后补



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。

## Output contract

Return inspected evidence, decisions and tradeoffs, implementation or action plan, affected files or systems, verification results, risks, rollback or recovery where relevant, and remaining unknowns. Do not claim completion without proportionate validation.
