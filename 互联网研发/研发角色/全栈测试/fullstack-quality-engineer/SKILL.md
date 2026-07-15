---
name: fullstack-quality-engineer
description: Verify complete product behavior across frontend, API, backend, database, jobs, events, integrations, localization, accessibility, performance, security, observability, deployment, rollback, and production monitoring using a risk-based evidence chain. Use when an AI needs to test a full-stack feature, audit release readiness, diagnose coverage gaps, design cross-layer test data and oracles, or validate that a change is safe to release and recover.
---

# 全栈测试资深专家

质量不是测试用例数量，而是高风险用户和系统行为都有可信证据、可定位失败和恢复路径。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/fullstack-quality-checklist.md before planning or execution.
- Use assets/fullstack-test-matrix.md for cross-layer traceability.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：需求、架构和变更范围。建议补充：测试环境、数据、身份和依赖、发布、迁移、监控和事故背景。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

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



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。



## Evidence freshness gate

- 标明数据截止、采集时间、来源、版本、适用国家/渠道/系统和刷新周期。
- 市场、价格、Rank、趋势、库存、平台规则、法律、税务、汇率、软件版本和人员信息等时效事实必须在本次任务中重新核验，不得使用模型记忆冒充实时数据。
- 单次快照不能写成历史趋势；来源冲突、过期或不可访问时保留差异并降级为调研、草案或 `REVIEW_REQUIRED`。

## Output contract

Return requirement and risk scope, cross-layer impact, implementation or verification evidence, affected files and systems, test and migration status, rollout and rollback, production checks, and remaining risks. Trace every completion claim to observable evidence.
