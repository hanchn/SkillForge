---
name: message-alert-orchestration-specialist
description: 把业务、系统和运营事件编排为可去重、可升级、可回执、可关闭的多平台通知告警，并安全适配飞书、钉钉、企业微信及贵司企业 QQ 网关。 Use when an AI needs to handle 库存、订单、财务、系统和运营指标告警, 飞书、钉钉、企业微信机器人或应用接入, 企业 QQ/内部消息网关适配与多平台容灾; produce 事件与严重度模型, 平台连接器、路由、模板和权限方案, 发送预览、回执、升级、关闭和复盘记录; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 多平台消息通知与分级告警编排专家

把业务、系统和运营事件编排为可去重、可升级、可回执、可关闭的多平台通知告警，并安全适配飞书、钉钉、企业微信及贵司企业 QQ 网关。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

- 必须读取 `references/platform-adapter-guide.md` 并使用 `assets/platform-connector-intake.md`；未确认平台类型、权限、凭证引用、租户、目标会话和沙箱前，只能生成 dry-run 预览。
- 使用 `assets/normalized-alert-event.schema.json` 统一事件，使用 `assets/routing-policy-template.md` 定义去重、抑制、升级、回执和关闭，不得把平台请求成功等同于问题解决。




## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：业务目标、范围和现状证据。建议补充：历史数据、流程系统资料、目标、预算、SLA 和合规约束。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. 确认事件来源、业务影响、接收人、租户/群/会话、国家时区、严重度、SLA、值班表、静默窗口、升级 owner 和真实发送权限
2. 询问飞书、钉钉、企业微信或企业 QQ/内部网关的机器人/应用类型、官方文档、租户、权限、消息类型、限流和凭证引用；不接收明文 webhook/token
3. 定义标准事件契约、幂等键、去重窗口、关联键、状态、数据分类和 source of truth，避免同一问题跨系统重复轰炸
4. 设计严重度、阈值、持续时间、抑制、聚合、维护静默、恢复通知和动态升级；阈值必须来自业务风险和历史证据
5. 映射平台能力与限制，生成文本/卡片预览、@策略、链接和降级模板；企业 QQ 仅按已确认官方接口或贵司网关适配
6. 先在沙箱/测试群 dry-run，验证脱敏、长度、格式、链接、幂等、限流、超时、重试、熔断和跨平台部分失败，不把 HTTP 2xx 当成已读
7. 真实发送前获取授权并记录批次；采集平台响应、message_id、回执/认领、升级、恢复、关闭和失败队列，保证可重放但不重复触达
8. 复盘命中率、噪声率、响应/解决时间、漏报、误报、升级和行动完成效果，更新规则、值班、模板与连接器版本

## Required decision lenses

- 事件 source of truth、幂等和去重
- 严重度、抑制、聚合、静默和升级
- 值班、owner、SLA、回执和关闭
- 飞书/钉钉/企业微信/企业QQ能力差异
- 凭证、个人数据、消息大小、限流和失败重试
- 送达、可行动性、噪声率和复盘

## Depth requirements

- 先解释业务对象、术语、为什么要做、谁使用结果以及错误结果会造成什么后果，再进入执行。
- 覆盖当前场景及与其相邻的高频变体；不得用同一套步骤忽略国家、渠道、职级、系统状态、数据成熟度或风险等级差异。
- 明确上游输入、下游消费者、责任边界、决策权、审批人、系统事实源和人工交接点。
- 对每个关键判断给出所需证据、可选方案、选择条件、反证、停止条件和不可逆风险。
- 同时设计正常路径、缺数据、低置信度、冲突、超时、权限不足、部分成功、回滚和转人工路径。
- 工具只是执行手段；必须说明工具输入输出、权限、失败、成本、时效、版本和人工验收，不能把调用工具等同于完成业务。
- 交付物必须让下游能直接执行或审批，并包含 owner、依赖、时间、验收指标、审计证据和下一次复盘触发器。

## Scenario and exception gates

1. 从 `references/scenario-playbook.md` 选择主场景；同时检查是否命中第二场景或高风险变体。
2. 关键事实、权限、口径或 source of truth 未确认时，降级为调研、草案或 `REVIEW_REQUIRED`，不得伪装成可执行定稿。
3. 发现目标冲突时，明确收入、利润、现金、客户、质量、时效、合规和可逆性之间的取舍，记录决策人。
4. 执行中出现部分失败时，保护已确认结果，隔离未知状态，停止扩大影响，提供对账、补偿或回滚步骤。
5. 只有交付物、验证证据、责任交接和剩余风险同时清楚，任务才算完成。

## Evidence freshness gate

- 在结论中标明数据截止、采集时间、来源、版本、适用国家/渠道/系统和刷新周期。
- 市场、价格、Rank、趋势、库存、平台政策、法律、税务、汇率、软件版本和人员信息等时效事实，必须在本次任务中从授权的一手或当前来源重新核验；不得使用模型记忆冒充实时数据。
- 单次快照只能说明当前观察，不能写成历史趋势；趋势结论必须有多个时间点或提供历史序列的可靠来源。
- 来源冲突时保留差异与口径，说明裁决 owner；关键来源过期或不可访问时，降级为调研计划、草案或 `REVIEW_REQUIRED`。

## Guardrails

- 不得在 Skill、日志或消息中暴露 webhook/token；不得无授权真实发送、@全员或跨租户触达；不得把请求成功当成用户已读或问题已关闭。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
