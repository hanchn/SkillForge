---
name: contract-risk-reviewer
description: Review commercial contracts clause by clause to extract obligations, identify legal and operational risks, detect missing protections and internal inconsistencies, compare positions against a stated party and jurisdiction, and produce prioritized negotiation language and a risk register. Use when an AI needs first-pass review of an NDA, services agreement, procurement contract, SaaS agreement, licensing deal, data-processing terms, or contract amendment. This skill supports review and issue spotting but does not replace licensed legal advice.
---

# Contract Risk Reviewer

Review for the named party's actual obligations and operating reality. Do not present general information as legal advice.

## Load resources

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/review-matrix.md before clause review.
- Use assets/risk-register-template.md to produce a structured handoff.

## Intake gate

Identify the reviewing party, contract type, jurisdiction or governing law, transaction purpose, commercial value or criticality, term, data involved, and non-negotiable business positions. If any are missing, state the assumptions and lower confidence for jurisdiction-specific conclusions.

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

## Output contract

Return scope and assumptions, executive risk summary, clause-by-clause issue table, obligation register, missing protections, negotiation priorities, operational handoffs, counsel escalations, and residual risk. Clearly label suggested wording as drafting options for legal review.
