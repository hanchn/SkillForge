---
name: web-performance-accessibility-auditor
description: Audit and improve web performance, Core Web Vitals, loading behavior, semantic HTML, keyboard access, focus management, screen-reader communication, contrast, motion, responsive interaction, and regression risk using measured evidence. Use when an AI needs to review a page or flow for speed and accessibility, diagnose LCP, INP, CLS or interaction problems, prioritize fixes, or verify that frontend changes work for diverse users.
---

# Web 性能与无障碍审计师

先测量具体页面与用户旅程，再修关键路径；性能分数和自动扫描都不是最终用户体验。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/audit-checklist.md before design, implementation, or diagnosis.
- Use assets/web-quality-report-template.md for the final artifact and handoff.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：URL、构建或页面代码。建议补充：目标设备、网络和关键旅程、可选 RUM、性能 trace、无障碍报告和用户反馈。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. 确定页面、设备、网络、用户旅程、登录状态、地区、浏览器和发布版本
2. 收集现场数据与实验室证据，分开记录 LCP、INP、CLS、资源瀑布、主线程和交互症状
3. 定位关键渲染路径、最大内容元素、输入响应、布局移动、字体、图片、脚本和第三方影响
4. 用键盘走完整流程，检查语义结构、地标、标题、表单标签、错误、焦点、弹层和动态提示
5. 检查对比度、缩放、响应式、触控目标、横竖屏、reduced motion 和高对比模式
6. 运行自动工具但手工验证关键问题，避免把无告警当合格
7. 将发现写成证据、用户影响、根因、修复、风险、owner 和验收方式
8. 按用户影响、覆盖、置信度、成本和回归风险排序
9. 实施或建议最小修复，并在同一条件下复测
10. 建立预算、监控和回归测试，防止一次性优化回退

## Guardrails

- 不得只凭 Lighthouse 单次分数下结论
- 不得用 aria 修补本可用原生语义解决的问题
- 不得通过隐藏内容、延迟交互或删除功能制造虚假性能提升
- 不得声称自动扫描已覆盖全部无障碍问题



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
