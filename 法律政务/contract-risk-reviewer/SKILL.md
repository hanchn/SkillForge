---
name: contract-risk-reviewer
description: Review commercial contracts clause by clause to extract obligations, identify legal and operational risks, detect missing protections and internal inconsistencies, compare positions against a stated party and jurisdiction, and produce prioritized negotiation language and a risk register. Use when an AI needs first-pass review of an NDA, services agreement, procurement contract, SaaS agreement, licensing deal, data-processing terms, or contract amendment. This skill supports review and issue spotting but does not replace licensed legal advice.
---

# Contract Risk Reviewer

Review for the named party's actual obligations and operating reality. Do not present general information as legal advice.

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/review-matrix.md before clause review.
- Use assets/risk-register-template.md to produce a structured handoff.

## Intake gate

Identify the reviewing party, contract type, jurisdiction or governing law, transaction purpose, commercial value or criticality, term, data involved, and non-negotiable business positions. If any are missing, state the assumptions and lower confidence for jurisdiction-specific conclusions.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：contract_text_or_file、reviewing_party。建议补充：jurisdiction、transaction_context、risk_tolerance、negotiation_position。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. Preserve the source document's clause numbering and defined terms. Identify missing schedules, exhibits, referenced policies, and incorporated URLs.
2. Build a contract map covering parties, term, money, deliverables, acceptance, IP, confidentiality, data, warranties, indemnities, liability, insurance, compliance, termination, dispute resolution, notices, assignment, and change control.
3. Extract each material obligation with actor, action, object, deadline, trigger, dependency, evidence, and consequence of breach.
4. Review internal consistency across definitions, order of precedence, dates, cross-references, remedies, and survival clauses.
5. Classify each issue by severity and probability, then explain the concrete legal, financial, operational, security, or reputational exposure for the reviewing party.
6. Distinguish unacceptable risk, negotiable risk, business decision, drafting defect, missing information, and informational note.
7. Propose the narrowest workable fallback: preferred language, acceptable compromise, and walk-away point when the user provides negotiation posture.
8. Identify obligations requiring internal owners or operational controls, including renewal dates, notice windows, audit duties, security commitments, and deletion requirements.
9. Produce a prioritized negotiation list and an escalation list for qualified counsel.
10. Finish with missing-document requests and a concise residual-risk summary.

## Safety and precision

- Do not invent governing law, enforceability, statutory requirements, market standards, or clause text not in the source.
- Quote only the minimum text needed to locate an issue; prefer clause references and faithful paraphrase.
- Treat absence of a clause as a gap, not proof that a protection exists elsewhere.
- Flag ambiguous pronouns, undefined terms, subjective standards, unilateral discretion, and conflicting timelines.
- Escalate novel regulation, litigation strategy, criminal exposure, employment classification, tax, sanctions, regulated data, and jurisdiction-specific enforceability to licensed counsel.
- Never state that a contract is safe, compliant, or enforceable without qualified jurisdiction-specific review.



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

Return scope and assumptions, executive risk summary, clause-by-clause issue table, obligation register, missing protections, negotiation priorities, operational handoffs, counsel escalations, and residual risk. Clearly label suggested wording as drafting options for legal review.
