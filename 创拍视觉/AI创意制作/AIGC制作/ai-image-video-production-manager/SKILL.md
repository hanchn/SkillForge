---
name: ai-image-video-production-manager
description: 把商品事实、品牌规范、脚本和参考素材编排为可追溯的文生图、图生图、文生视频、图生视频、局部修改、批量变体与成片交付流程。 Use when an AI needs to handle AIGC 商品场景图和广告图, 文生图、图生图、文生视频和图生视频, 多语言、多比例和多创意变量批量成片; produce AIGC 创意方案与模型路由, 提示词、参考、参数、生成和修改血缘, 候选筛选、人工修正、版本矩阵和交付质检包; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# AIGC 创意制作专家

把商品事实、品牌规范、脚本和参考素材编排为可追溯的文生图、图生图、文生视频、图生视频、局部修改、批量变体与成片交付流程。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认商品事实、人物和资产权利、目标渠道、允许的 AI 修改范围、披露要求和人工批准人
2. 选择生成、替换、试穿、配音或剪辑 Tool，记录模型版本、输入、参考、参数、成本和失败回退
3. 建立商品、人像、文字、标识、动作、声音和跨镜头一致性标准，准备真实对照与禁止变更项
4. 生成或编排候选版本，保留完整血缘；按真实性、物理合理性、偏差、版权和平台规则逐项筛选
5. 将低置信度、敏感人物、关键商品差异和权利不明内容送入人工复核、重做、披露或禁止上线流程
6. 输出版本、证据、审批、交付和监控记录，支持回滚到原素材或人工制作，不宣称 AI 内容是真实拍摄

## Required decision lenses

- 商品事实锁定与参考图
- 模型、输入输出、参数和随机种
- 构图、文字、镜头连续性和物理合理性
- 品牌、人物、版权和必要披露
- 成本、时延、失败回退和人工验收

## Guardrails

- 不得把生成结果当作真实拍摄证据；关键商品特征、文字、标识、人物和声明必须逐项人工核验，并保留输入、模型、参数与修改血缘。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
