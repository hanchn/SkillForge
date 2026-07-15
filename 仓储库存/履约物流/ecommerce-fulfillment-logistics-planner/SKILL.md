---
name: ecommerce-fulfillment-logistics-planner
description: Design and compare ecommerce freight, customs, receiving, warehousing, FBA, FBM, 3PL, direct fulfillment, returns, and delivery operations using landed cost, service level, dimensional weight, capacity, exception handling, and resilience. Use when an AI needs to choose shipping modes, plan inbound calendars, compare fulfillment networks, reduce delivery failures, or prepare Amazon and owned-store logistics operations.
---

# 电商履约物流规划师

物流方案必须同时满足成本、时效、可追踪、合规、容量和异常恢复。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/logistics-decision-checklist.md before analysis or execution.
- Use assets/fulfillment-plan-template.md for the final plan and handoff.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：产品与包装尺寸重量、起运和目的地。建议补充：渠道需求、订单结构与服务承诺、承运商、仓库、FBA/3PL 报价和限制。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. 确认产品尺寸重量、危险或特殊属性、起运地、目的市场、渠道、销量、承诺时效和退货要求
2. 建立端到端节点图：工厂、质检、提货、出口、干线、清关、仓库、FBA/3PL、最后一公里和逆向物流
3. 统一比较计费重、体积重、固定费、操作费、关税税费、仓储、退货、丢损和加急成本
4. 用低中高时效和波动评估海运、空运、快递、铁路或本地备货组合
5. 设计 FBA、FBM、3PL 和独立站订单路由、库存缓冲、分单、缺货和峰值容量
6. 定义标签、箱规、预约、ASN、追踪、POD、清关文件和数据交接责任
7. 建立延误、扣关、拒收、丢件、破损、地址错误、仓库爆仓和承运商中断 playbook
8. 输出首选、备选、验证批次、时间表、成本区间、SLA 和切换阈值
9. 用准时率、交付时长、成本/单、损坏、丢件、退款、首次投递和仓库差错复盘

## Guardrails

- 不得用基础运价代替完整落地与履约成本
- 不得忽略体积重、旺季、偏远、燃油、仓储和退货费用
- 不得承诺承运商无法保证的时效
- 涉及海关、危险品和税务时必须使用当前专业规则并标记责任人



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
