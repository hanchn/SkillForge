---
name: supplier-sourcing-quality-manager
description: Plan and evaluate ecommerce supplier sourcing, RFQs, samples, factory capability, commercial terms, quality standards, inspections, defect handling, packaging, production readiness, and supplier concentration risk. Use when an AI needs to compare suppliers, prepare procurement questions, qualify samples, design QC checkpoints, negotiate MOQ or lead time, or decide whether a supplier is ready for Amazon or owned-store production.
---

# 供应商寻源与质量管理器

低价不是供应能力，样品合格也不等于量产受控。

## Load resources

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/sourcing-quality-checklist.md before analysis or execution.
- Use assets/supplier-scorecard.md for the final plan and handoff.

## Workflow

1. 确认产品规格、目标市场、销售渠道、预估量、质量底线、预算和交期
2. 将要求拆成 must-have、可协商和直接淘汰项，建立可测量规格
3. 向多个候选供应商发送一致 RFQ，收集阶梯价、MOQ、样品、模具、包装、认证、产能、交期和付款条件
4. 验证主体、工厂能力、关键工序、外包环节、质量体系和历史证据，不把平台徽章当充分证明
5. 设计盲比样品计划，记录材料、尺寸、功能、外观、气味、耐久、包装和运输测试
6. 建立黄金样、BOM、缺陷分级、AQL 或适用验收规则、检验方法和签样变更控制
7. 规划产前、首件、中期、尾期和装运前质量节点以及不合格处置
8. 比较总落地成本、现金条件、交期波动、沟通、可扩展性和单一来源风险
9. 输出首选、备选、条件性通过或淘汰结论以及试单和量产 gate

## Guardrails

- 不得把供应商自述、证书截图或平台等级当作已验证事实
- 不得只按最低单价排序
- 未经样品和生产证据不得建议大货
- 规格、缺陷和验收必须可测量，避免好、优质、差不多等模糊词



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。

## Output contract

Return the decision context, evidence and assumptions, analysis or plan, prioritized actions, owners and dependencies, acceptance or decision thresholds, risks, and the next review point. Keep observed facts separate from estimates and recommendations.
