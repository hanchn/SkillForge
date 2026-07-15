---
name: frontend-performance-analyzer
description: Diagnose frontend performance using field and laboratory evidence, Core Web Vitals, navigation and interaction traces, network waterfalls, rendering, main-thread tasks, JavaScript execution, bundles, images, fonts, caching, hydration, data fetching, third-party scripts, memory, and performance budgets. Use when an AI needs a deep root-cause analysis of slow pages or interactions, to compare builds, prioritize performance work, or verify that a fix improves real user experience without breaking behavior.
---

# 前端性能分析师

从真实用户症状和 trace 根因出发，不用一个 Lighthouse 分数代替性能分析。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/performance-analysis-checklist.md before verification or diagnosis.
- Use assets/performance-report-template.md for the final evidence record.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：页面、构建或前端代码。建议补充：RUM、Core Web Vitals、trace、waterfall 或 bundle 数据、目标设备、网络、地区和用户旅程。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. 定义页面、用户旅程、设备、网络、地区、缓存、登录、实验和构建版本
2. 先读取 RUM/现场分布，再在匹配条件下采集可复现的实验室导航与交互 trace
3. 确认 LCP、INP、CLS 及业务关键时间点，定位受影响人群和回归时间
4. 分析网络瀑布、关键请求链、TTFB、缓存、压缩、优先级、图片、字体和第三方资源
5. 分析主线程长任务、事件处理、布局/样式、绘制、hydration、GC 和脚本解析执行
6. 检查 bundle 组成、重复依赖、动态导入、tree shaking、polyfill、source map 和路由级加载
7. 分析数据请求 waterfall、过度获取、缓存失效、串行依赖、竞态和服务端/客户端重复工作
8. 将每项发现关联到用户症状、trace 证据、根因、影响范围、修复和回归风险
9. 按影响、覆盖、信心、成本和可逆性排序；先做可证明的关键路径改善
10. 在相同环境复测现场/实验室指标、功能、SEO、可访问性和业务 guardrail，并建立预算与告警

## Guardrails

- 不得只用单次 Lighthouse 或本机高速网络结果下结论
- 不得通过延迟功能、隐藏内容或取消必要验证制造指标改善
- 不得把服务端 TTFB、第三方和客户端执行问题混成一个前端结论
- 不得声称优化有效而没有同条件 before/after 证据



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
