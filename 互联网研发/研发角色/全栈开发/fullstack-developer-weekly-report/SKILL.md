---
name: fullstack-developer-weekly-report
description: Create evidence-backed full-stack development weekly reports from tickets, requirements, Git commits, pull requests, reviews, frontend and backend changes, database migrations, deployments, incidents, and project notes. Use when an AI needs to summarize a developer or full-stack team's weekly delivery, separate completed and in-progress work, explain technical impact in business-readable language, report risks and release status, or prepare next-week priorities without fabricating progress.
---

# 全栈开发资深专家周报

周报按已验证交付结果组织，不按提交数量堆砌，也不把进行中包装成已完成。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/weekly-evidence-checklist.md before drafting.
- Use assets/developer-weekly-template.md for the final report.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：报告周期、时区和汇报范围、工单、PR、提交、部署、迁移与项目记录。建议补充：可选上周周报、指标和下周优先级。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. 锁定报告周期、时区、汇报对象、项目范围，以及是否需要本周对上周比较
2. 盘点工单、PR、提交、评审、部署、迁移、事故和项目记录，建立证据清单
3. 合并同一业务目标的多层技术改动，避免前端、后端和数据库重复计数
4. 按已上线、已合并待发布、开发中、阻塞、取消分类，状态必须符合证据
5. 把技术变化翻译为用户、业务、稳定性、效率或风险影响，同时保留必要技术定位
6. 记录接口、数据、迁移、feature flag、兼容、监控、回滚和生产验证状态
7. 只报告可复算指标，注明口径、分母、周期和数据源
8. 提炼需要协作或决策的风险，不使用夸大、推责或管理口号
9. 下周计划对应已知优先级、依赖和可验收结果，不写泛化继续优化
10. 输出简版摘要和可追溯明细，标记缺证据或待确认事项

## Guardrails

- 不得把 commit、PR 或代码行数直接等同业务产出
- 不得把已编码、已提测、已合并和已上线混为完成
- 不得编造进度百分比、发布日期、指标改善或责任归属
- 对外周报避免泄露凭据、内部敏感架构和不必要技术噪音



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
