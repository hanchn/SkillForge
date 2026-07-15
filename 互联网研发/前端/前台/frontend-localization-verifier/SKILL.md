---
name: frontend-localization-verifier
description: Verify frontend internationalization and localization across supported locales, including translation coverage, key drift, ICU messages, variables, plurals, gender, dates, numbers, currency, units, time zones, Unicode, collation, locale routing, persistence, layout expansion, RTL, fonts, accessibility, metadata, hreflang, and localized business behavior. Use when an AI needs to audit multilingual pages, test a new locale, diagnose untranslated or malformed content, or build a repeatable locale QA matrix.
---

# 前端多语言查验师

多语言查验不是逐句看翻译，而是验证语言、格式、布局、路由和业务语义在每个 locale 都成立。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/localization-checklist.md before verification or diagnosis.
- Use assets/locale-qa-matrix.md for the final evidence record.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：支持 locale 与市场规则。建议补充：前端代码、翻译资源和运行页面、关键页面、设备、状态和业务流程。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. 确认支持 locale、默认与回退语言、市场、货币、时区、路由策略、内容来源和目标用户旅程
2. 扫描源码与运行页面中的硬编码文本、缺失 key、孤儿 key、重复 key、回退泄漏和动态拼接
3. 比较所有 locale 的变量、占位符、富文本标签、复数/性别分支和 ICU 语法，防止翻译破坏运行时
4. 验证日期、时间、时区、数字、货币、百分比、单位、电话号码、地址和排序规则
5. 用伪本地化和长文本测试截断、换行、按钮、表格、弹层、图片内文字和响应式布局
6. 对 RTL locale 验证方向、逻辑属性、图标、焦点、动画、滚动和混合双向文本
7. 检查 locale 检测、选择、URL、持久化、回退、跨页面导航和服务端/客户端 hydration 一致性
8. 验证 title、description、canonical、hreflang、结构化数据、站点地图和语言内容一致性
9. 检查字体字形、Unicode 规范化、输入、搜索、复制粘贴、读屏语言和错误提示
10. 建立 locale × 页面 × 状态 × 设备矩阵，记录证据、严重度、owner 和复测结果

## Guardrails

- 不得把机器翻译通顺度当成完整本地化验收
- 不得通过字符串拼接构造需要语法变化的句子
- 不得把国家、语言、货币和时区视为同一个概念
- 不熟悉目标语言时必须标记语言质量需母语或专业复核



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

Return scope and environment, evidence, findings with severity and confidence, root causes, prioritized fixes, acceptance criteria, before/after verification where applicable, owners, and remaining specialist review.
