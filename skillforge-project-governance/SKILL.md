---
name: skillforge-project-governance
description: Govern the SkillForge cross-platform skill repository, including business taxonomy, portable package structure, metadata, triggering quality, evidence boundaries, reusable resources, examples, acceptance tests, registry synchronization, and distribution checks. Use before creating, upgrading, reviewing, indexing, or packaging any SkillForge skill or when deciding where a new business capability belongs.
---

# SkillForge Project Governance

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

## Compliance gate

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

## Identity

- skill id: `skillforge-project-governance`
- display name: `SkillForge项目治理`
- type: `portable-governance-skill`
- scope: `cross-platform`

## What It Does

- 解释 `SkillForge` 项目的定位、目标与架构设计
- 约束后续 AI 如何创建、修改和分发业务 skill
- 提供统一的目录规则、文件职责与升级原则
- 要求每个 skill 具备真实专业判断链、证据边界和可执行验收，而不是只换名称的提示词模板
- 以“一个完整业务结果”为默认粒度，防止把同一工作流拆成大量动作级 Skill
- 要求 Skill 优先读取 `公司上下文/` 中的贵司事实，并围绕贵司系统与部门边界执行

## Skill Granularity Rules

- 一个 Skill 能从输入完成到可验收结果时，不再按步骤、工具、消息模板或单一动作拆分。
- 只有专业知识、触发场景、风险边界、输入输出和独立复用价值均明显不同，才建立专项 Skill。
- 主角色 Skill 负责目标、取舍、编排和验收；专项 Skill 负责完整专业结果，不按岗位人数机械建 Skill。
- 新增前先检查现有 Skill 能否升级覆盖；默认升级，例外才新增。

## Company Customization

- 在仓库内执行时先读 `公司上下文/company-profile.yaml` 和 `公司上下文/README.md`。
- 已确认公司事实优先于通用行业假设；未知内容明确询问或标记，不得虚构。
- 系统工作默认使用贵司 OMS、IMS、OFS、CMS、WMS、TMS、CRM、PLM 的业务语言，并先确认实际缩写口径和 source of truth。

## When To Use

- 新 AI 接手这个项目时
- 在新增或重构业务 skill 之前
- 在不确定某个文件该放哪里、是否该做成 skill 包时
- 在准备把 skill 单独发给别人之前

## Read In Order

1. `skill.json`
2. `README.md`
3. `ARCHITECTURE.md`
4. `assets/project-rules.md`
5. `INVOCATION.md`
6. `platforms/<platform>.md`

## Package Guarantee

- 这是一个可独立分享的项目级 skill 文件夹
- 直接发送整个 `skillforge-project-governance/` 目录即可让其他 AI 理解项目规则


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


## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：目标与真实现状。建议补充：target_skill_path、target_business_domain、change_request。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。


## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。
