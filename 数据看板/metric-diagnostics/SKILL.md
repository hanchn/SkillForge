---
name: metric-diagnostics
description: Diagnose why a business or product metric changed by validating definitions and data quality, decomposing movement across segments and funnel stages, testing competing explanations, and separating observed drivers from hypotheses. Use when an AI needs to explain a spike, drop, gap, anomaly, forecast miss, cohort difference, or dashboard discrepancy and produce a decision-ready diagnostic with quantified contributions and caveats.
---

# Metric Diagnostics

Establish that the movement is real before explaining it.

## Load resources

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/diagnostic-method.md for validation and decomposition methods.
- Use assets/diagnostic-report-template.md for the final readout.

## Workflow

1. Lock the comparison: metric definition, grain, population, timezone, attribution window, current period, baseline period, and filters.
2. Reconcile the value against its source or an independent calculation. Check freshness, completeness, duplicates, joins, late arrival, instrumentation changes, and denominator drift.
3. Quantify absolute change, relative change, and uncertainty. Distinguish rate changes from volume changes.
4. Write several competing hypotheses before drilling down. Include data artifacts, mix shift, seasonality, product changes, channel changes, and operational changes when plausible.
5. Decompose by the metric's algebra first, then by funnel stage, cohort, geography, platform, acquisition source, product, and other business-relevant segments.
6. Rank segment contributions using weighted impact, not only percentage change. Guard against tiny-base outliers.
7. Align candidate drivers to timing, exposure, and expected mechanism. Use control or unexposed groups when available.
8. Classify findings as confirmed driver, contributing factor, ruled out, or unresolved hypothesis. State the evidence threshold used.
9. Run sensitivity checks for date windows, exclusions, metric definitions, and influential segments.
10. End with the operational implication and the smallest next analysis or experiment that resolves remaining uncertainty.

## Analysis rules

- Never infer causality from correlation alone.
- Do not average ratios when a ratio of sums is required.
- Do not compare incomplete current periods with complete historical periods without adjustment.
- Distinguish composition effects from within-segment performance changes.
- Show numerator and denominator whenever diagnosing a rate.
- Preserve exact query, file, dashboard, or table references when available.
- If data is insufficient, return a bounded diagnosis and an evidence acquisition plan rather than a confident story.



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。

## Output contract

Lead with a one-sentence finding calibrated to evidence. Then show metric validation, quantified movement, contribution table, hypothesis scorecard, caveats, decision implication, and next evidence. Keep confirmed observations visually separate from inference.
