---
name: commerce-advertising-optimizer
description: Diagnose and optimize Amazon Ads and owned-store paid media using business objectives, clean attribution, query and audience intent, campaign structure, bids, budgets, creative, landing-page readiness, incrementality, contribution margin, and controlled experiments. Use when an AI needs to audit Sponsored Products or other commerce campaigns, reduce wasted spend, scale profitable demand, or distinguish ad problems from listing, price, inventory, or conversion problems.
---

# 多渠道电商广告优化师

先判断流量、转化还是利润问题，再动出价；平台归因不是增量利润。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/advertising-diagnostic-checklist.md before analysis or execution.
- Use assets/advertising-action-plan.md for the final plan and handoff.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：广告、订单、销售和归因数据。建议补充：SKU 利润与 break-even 指标、库存、价格、促销、listing/落地页和目标。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. 确认市场、渠道、广告类型、目标、归因窗口、时间口径、利润底线和库存状态
2. 校验花费、点击、订单、销售、新客、退款和自然销售数据，标记平台归因与业务口径差异
3. 按漏斗定位问题：曝光不足、点击不足、详情页转化不足、客单/复购不足或利润不足
4. 拆解搜索词、关键词、商品、受众、版位、设备、地域、创意、落地页和新老客表现
5. 计算 CPC、CTR、CVR、CPA、ACOS/ROAS、TACOS、边际贡献和 break-even 阈值
6. 隔离品牌防守、类目拓展、竞品、再营销和新品学习预算，避免混合目标互相补贴
7. 制定否词、目标迁移、竞价、预算、创意、商品页和落地页动作，说明预期机制
8. 一次实验改变有限变量，定义主指标、guardrail、最小运行逻辑和停止条件
9. 检查库存、Buy Box/可售性、价格、优惠和页面质量，避免为无法转化的商品买流量
10. 输出扩量、修复、观察或暂停结论，并安排复盘窗口

## Guardrails

- 不得只用平台 ROAS 宣称盈利或增量
- 不得在低样本下频繁调价造成学习噪声
- 不得把页面、价格、库存或合规问题全部归因广告
- 不得虚构关键词量、行业基准或平台规则



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

Return the decision context, evidence and assumptions, analysis or plan, prioritized actions, owners and dependencies, acceptance or decision thresholds, risks, and the next review point. Keep observed facts separate from estimates and recommendations.
