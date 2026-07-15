---
name: fullstack-qa-weekly-report
description: Create evidence-backed full-stack quality weekly reports from requirements, risk assessments, test plans, executions, automation, defects, regressions, environments, releases, production verification, incidents, and quality metrics. Use when an AI needs to summarize weekly testing and quality status, report release readiness, explain uncovered risks and blockers, compare quality trends with consistent definitions, or plan next-week verification without treating raw test counts as quality.
---

# 全栈测试资深专家周报

周报围绕风险是否被验证和版本是否可安全发布，不用用例执行数量制造质量感。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/weekly-quality-evidence.md before drafting.
- Use assets/qa-weekly-template.md for the final report.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：报告周期、版本与发布范围、风险、测试、缺陷、环境和发布证据。建议补充：可选上周周报、质量指标和下周版本计划。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

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

Return a concise weekly conclusion, verified completed work, in-progress and blocked work, delivery or quality evidence, risks and decisions, next-week priorities with acceptance, and an evidence appendix. If comparison is requested, keep the same period length and metric definitions.
