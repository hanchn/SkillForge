---
name: fullstack-developer-weekly-report
description: Create evidence-backed full-stack development weekly reports from tickets, requirements, Git commits, pull requests, reviews, frontend and backend changes, database migrations, deployments, incidents, and project notes. Use when an AI needs to summarize a developer or full-stack team's weekly delivery, separate completed and in-progress work, explain technical impact in business-readable language, report risks and release status, or prepare next-week priorities without fabricating progress.
---

# 全栈开发资深专家周报

周报按已验证交付结果组织，不按提交数量堆砌，也不把进行中包装成已完成。

## Load resources

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/weekly-evidence-checklist.md before drafting.
- Use assets/developer-weekly-template.md for the final report.

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

## Output contract

Return a concise weekly conclusion, verified completed work, in-progress and blocked work, delivery or quality evidence, risks and decisions, next-week priorities with acceptance, and an evidence appendix. If comparison is requested, keep the same period length and metric definitions.
