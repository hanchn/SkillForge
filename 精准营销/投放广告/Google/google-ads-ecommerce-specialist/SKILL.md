---
name: google-ads-ecommerce-specialist
description: 围绕搜索意图、商品 Feed、落地页、转化价值和贡献利润规划与优化 Google Ads。 Use when an AI needs to handle Google Search、Shopping 与 Performance Max 投放, Merchant Center、Feed 和转化跟踪诊断, 搜索词治理、预算扩量和利润止损; produce Google Ads 投放与测量方案, 关键词、搜索词、Feed、资产组和预算矩阵, 诊断、实验、自检和复盘记录; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 独立站 Google Ads 投放专家

围绕搜索意图、商品 Feed、落地页、转化价值和贡献利润规划与优化 Google Ads。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

- 正式生成前必须使用 `assets/marketing-input-intake.md` 询问现有关键词/受众/素材/数据/规则库及其版本、owner 和优先级；未确认时只能交付调研或草案。
- 必须使用 `assets/prepublish-self-check.md` 做生成后自检；任何阻断项未通过时不得声称可投放、可发布或已验证。




## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. 生成前询问使用者是否有关键词库、否定词库、搜索词历史、商品 Feed、客户名单、素材库和利润口径，并确认优先参考策略
2. 锁定国家语言、商品范围、Search/Shopping/Performance Max 角色、转化目标与价值、新客定义、预算、利润护栏和库存限制
3. 审计 Google Ads、GA4、GTM/Google tag、增强型转化、Consent Mode、Merchant Center、Feed、自动标记和订单对账质量
4. 构建 Search 关键词与意图、匹配方式、否定词、广告组、RSA 和落地页矩阵；把搜索词治理与品牌词分拆纳入日常节奏
5. 构建 Shopping 或 Performance Max 的商品分组、资产组、受众信号、搜索主题、品牌控制、URL 扩展/排除和页面 Feed 方案
6. 按花费、展示份额、搜索词、Feed 诊断、CVR、CPA/ROAS、贡献利润、新客与回收期判断修复、扩量或暂停
7. 设计预算竞价、季节性、实验和增量验证；跟踪不可信、Feed 拒登、落地页不一致或库存风险时停止自动扩量
8. 生成后自检转化、Feed、关键词、否定词、资产、URL、政策、预算、利润和回滚，并记录上线后观察窗口

## Required decision lenses

- 转化目标、价值、增强型转化和同意
- Search 关键词、搜索词和否定词
- Merchant Center Feed 与商品诊断
- Performance Max 资产组、URL 扩展和品牌控制
- 落地页质量、利润、增量和止损

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

- 不得在跟踪或商品 Feed 不可信时自动扩量，不得用品牌词和平台自报转化掩盖真实获客效率。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
