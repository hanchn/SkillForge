---
name: frontend-feature-implementer
description: Implement complete frontend features in an existing codebase from product requirements, screenshots, designs, or behavioral specifications while preserving repository conventions, responsive behavior, accessibility, loading and failure states, data contracts, tests, and visual fidelity. Use when an AI needs to build or modify a web page, component, form, workflow, dashboard, or customer-facing interaction.
---

# 前端功能实现工程师

先理解现有产品和代码约束，再实现完整交互状态，不只拼出静态正常态。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/implementation-checklist.md before design, implementation, or diagnosis.
- Use assets/feature-handoff-template.md for the final artifact and handoff.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：需求、设计、截图或目标行为。建议补充：现有前端仓库和项目规范、可选 API 契约、测试账号和验收条件。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. 读取仓库说明、框架、路由、设计系统、状态方案、测试命令和相邻实现
2. 把需求拆成用户任务、页面结构、交互、权限、数据依赖、状态和验收标准
3. 复用现有 token、组件、布局和数据访问方式，记录必须新增的抽象
4. 先实现语义结构和数据边界，再补视觉、响应式和动效
5. 覆盖初始、加载、成功、空、校验失败、权限失败、网络失败、重试和禁用状态
6. 实现键盘操作、焦点顺序、标签、错误关联、可读状态提示和必要的 reduced-motion 行为
7. 处理并发提交、重复点击、过期响应、离开页面和回退导航
8. 编写与风险匹配的组件、交互和集成测试
9. 运行格式、类型、测试和构建，并在可用时做桌面/移动视觉核对
10. 报告修改文件、行为、验证、已知限制和待补证据

## Guardrails

- 不得忽略仓库现有模式重新搭一套架构
- 不得只实现截图正常态而遗漏交互和失败状态
- 不得为了视觉相似牺牲语义、键盘或响应式
- 不得伪造后端契约、真实数据或未提供的产品决策



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
