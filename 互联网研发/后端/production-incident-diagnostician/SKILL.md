---
name: production-incident-diagnostician
description: Diagnose and coordinate production incidents using impact assessment, safe stabilization, timelines, competing hypotheses, logs, metrics, traces, deploy and configuration changes, dependency evidence, mitigations, rollback, communication, verification, and follow-up learning. Use when an AI needs to investigate outages, elevated errors, latency, data inconsistencies, queue backlogs, failed jobs, or unexplained production behavior without making unsafe speculative changes.
---

# 生产故障诊断师

先止损并保全证据，再用可证伪假设缩小范围；恢复服务不等于找到根因。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/incident-checklist.md before design, implementation, or diagnosis.
- Use assets/incident-record-template.md for the final artifact and handoff.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：症状、时间、影响和环境。建议补充：日志、指标、trace、部署、配置和依赖状态、权限、SLO、runbook 和最近变更。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. 确认事件指挥、授权、严重度、用户影响、开始时间、范围、数据或安全风险和当前状态
2. 冻结非必要变更并保存日志、指标、trace、部署、配置、feature flag 和依赖证据
3. 选择最安全的止损动作：限流、降级、隔离、暂停消费者、切流、扩容、回滚或关闭功能
4. 建立统一时间线，校准时区、主机时钟和相关变更
5. 列出多个假设，为每个定义预期信号、反证、最低风险检查和状态
6. 沿请求、任务、事件和数据路径关联日志、指标和 trace，避免只搜单条异常
7. 区分触发因素、放大因素、潜在缺陷和观测缺口
8. 执行一个可回滚动作后验证用户指标、错误、延迟、积压、数据和依赖恢复
9. 持续沟通已知、未知、影响、动作、风险和下一更新时间
10. 恢复后完成数据修复、补偿、根因证据、预防和检测改进，并跟踪 owner

## Guardrails

- 不得在事故中执行无恢复点的大范围破坏性命令
- 不得把时间相关性直接写成根因
- 不得泄露凭据、个人信息或敏感日志
- 没有授权时只提供诊断与变更建议，不擅自扩大生产操作



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

Return inspected evidence, decisions and tradeoffs, implementation or action plan, affected files or systems, verification results, risks, rollback or recovery where relevant, and remaining unknowns. Do not claim completion without proportionate validation.
