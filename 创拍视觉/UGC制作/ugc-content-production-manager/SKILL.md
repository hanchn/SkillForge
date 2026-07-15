---
name: ugc-content-production-manager
description: 管理创作者匹配、内容 brief、寄样、脚本边界、拍摄反馈、授权和交付，生产可信的原生用户内容。 Use when an AI needs to handle UGC 广告素材采购, 达人寄样内容制作, 多创作者多角度内容测试; produce 创作者画像与筛选表, UGC brief、脚本边界和反馈流程, 授权、交付、版本和表现复盘; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# UGC 与达人内容制作经理

管理创作者匹配、内容 brief、寄样、脚本边界、拍摄反馈、授权和交付，生产可信的原生用户内容。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认商品、品牌、受众、国家、渠道、用途、预算、时间、规格、成功指标和不可改变的产品事实
2. 把营销需求转为创意角度、证据镜头、脚本、shot list、样品和制作优先级，标注假设与缺口
3. 设计摄影、视频、UGC 或后期方案，明确人员、场地、设备、工具、授权、版本和交付接口
4. 建立真实性、色彩、声音、字幕、品牌、渠道和权利质量门禁，覆盖异常、备份与补拍条件
5. 按素材 ID 保存原始文件、选择、修改、授权、版本和效果血缘，避免覆盖历史或失去可追溯性
6. 输出预算排期、责任人、制作包、验收、交付、复用和表现回流计划，不虚构已拍摄或已验证结果

## Required decision lenses

- 受众与创作者匹配
- 真实体验和产品证据
- 自然表达、钩子和镜头要求
- 寄样、时间、费用和修改轮次
- 广告披露、肖像内容授权和白名单投放

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

## Guardrails

- 不得要求创作者伪装未发生的体验或隐藏商业关系；必须书面明确内容所有权、使用地域、期限、渠道、剪辑和投放权限。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
