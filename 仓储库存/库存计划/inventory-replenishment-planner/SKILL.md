---
name: inventory-replenishment-planner
description: Plan and monitor multi-channel ecommerce replenishment end to end, including demand, lead time, safety stock, alert thresholds, exception queues, order timing, channel allocation, cash and storage constraints. Use when an AI needs to detect replenishment risk and decide what, when, and how much to reorder for Amazon FBA, FBM, 3PL, or owned storefront inventory.
---

# 库存补货与分级告警规划师

从库存监测、风险告警到补货建议与处置复盘一次完成。补货不是销售均值乘交期，而是需求和供应不确定性下的资金配置。

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/replenishment-method.md before analysis or execution.
- Use assets/replenishment-plan-template.md for the final plan and handoff.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：SKU 级销量、库存状态和在途。建议补充：生产、质检、运输、清关和入仓交期、活动、季节、价格、服务水平、资金和仓储约束。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. 锁定 SKU、地点、渠道、可售与不可售库存、在途阶段、预留、历史区间和计划窗口
2. 清洗缺货截断、异常促销、批量订单、退货和新品冷启动影响
3. 建立基准需求并分离趋势、季节、活动、价格和渠道迁移
4. 用实际生产、质检、干线、清关、预约和入仓分布建模补货提前期
5. 设定服务水平、安全库存、订货点、目标库存天数和最大资金/仓储约束
6. 建立覆盖天数、销量突变、在途延期和供应异常告警，定义去重、抑制、严重度、通知、认领和关闭规则
7. 按库存位置和渠道需求分配现货与在途，处理 FBA、3PL、FBM 和独立站共享库存
8. 生成基准、上行、下行情景以及加急、延迟、活动超卖和供应中断方案
9. 列出风险队列、下单量、最晚下单日、运输方式、预计到货、缺货概率和过量风险
10. 定义滚动更新、处置 SLA、采购交接、预测偏差、sell-through、库存年龄和告警复盘

## Guardrails

- 不得把采购在途、海运在途、入仓中和可售库存混为一体
- 不得用缺货期的销量直接代表真实需求
- 不得在没有资金、仓储和生命周期约束时只追求零缺货
- 预测必须提供误差或情景，不给单点伪精确答案
- 告警只生成风险和补货建议，不得绕过预算、MOQ、供应和审批自动形成采购承诺



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
