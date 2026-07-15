---
name: fullstack-feature-delivery
description: Deliver product features end to end across requirements, frontend interaction, API contracts, backend domain logic, data changes, authentication and authorization, observability, tests, deployment, migration, rollout, and post-release verification. Use when an AI needs to implement a complete vertical slice in an existing repository or coordinate changes that cross web, service, database, and operational boundaries.
---

# 全栈开发资深专家

按用户可验证的垂直切片交付，不把前端完成、接口完成或代码合并误认为功能完成。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/fullstack-delivery-checklist.md before planning or execution.
- Use assets/vertical-slice-plan.md for cross-layer traceability.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：产品需求、仓库和目标环境。建议补充：现有 API、数据、权限与发布约束、可选设计、测试账号和验收指标。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

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
