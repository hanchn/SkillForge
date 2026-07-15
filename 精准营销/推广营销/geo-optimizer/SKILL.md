---
name: geo-optimizer
description: Improve content for accurate discovery, extraction, citation, and recommendation by generative answer engines through verified entity facts, claim provenance, clear answer passages, comparison criteria, structured evidence, consistent terminology, and source-ready publishing. Use when an AI needs to audit or rewrite brand, product, category, help-center, FAQ, or research content for AI search visibility while avoiding fabricated statistics, fake authority, spam distribution, or guaranteed citations.
---

# GEO Optimizer

Make content easier to understand and support, not easier to hallucinate from.

## Load resources

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/citation-readiness.md before auditing content.
- Use assets/claim-ledger.md to control facts and provenance.

## Workflow

1. Define the entity, market, audience questions, decision context, and desired owned source.
2. Build a claim ledger. For each material statement record source, date, geography, scope, methodology, confidence, and expiry risk.
3. Resolve entity consistency across names, product identifiers, category, authorship, organization details, and canonical URLs.
4. Map real audience questions and comparison criteria. Distinguish informational, evaluative, transactional, support, and safety intent.
5. Write answer-first passages that stand alone: direct answer, conditions, evidence, limitations, and next detail. Keep nearby context sufficient for accurate extraction.
6. Add useful tables, definitions, procedures, comparisons, and FAQs only when supported by real facts and user need.
7. Strengthen provenance with primary sources, dated methods, author or organization accountability, and clear update information.
8. Recommend valid structured data, canonicalization, indexability, feeds, sitemaps, internal links, and consistent public profiles when technically appropriate.
9. Plan legitimate distribution to relevant owned and earned surfaces. Do not recommend planted discussions, fabricated consensus, paid links disguised as editorial, or Wikipedia manipulation.
10. Measure discoverability, cited-answer accuracy, branded and non-branded referral, assisted conversion, and misinformation rate. Treat model outputs as sampled observations, not deterministic rankings.

## Guardrails

- Do not invent statistics, expert quotes, reviews, certifications, awards, research, or third-party endorsements.
- Do not claim that schema or formatting guarantees inclusion or citation.
- Do not turn FAQs into repetitive keyword blocks.
- Prefer first-party and primary evidence; disclose commercial interest.
- Keep legal, medical, safety, sustainability, and performance claims within verified scope.



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。

## Output contract

Return entity and question map, claim ledger, citation-readiness gaps, rewritten answer modules, source and structure plan, technical publishing checks, ethical distribution plan, and measurement design. Label unsupported claims for removal or evidence acquisition.
