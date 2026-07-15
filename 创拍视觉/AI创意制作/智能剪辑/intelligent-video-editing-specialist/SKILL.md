---
name: intelligent-video-editing-specialist
description: 利用镜头识别、语音转写、节奏分析、自动重构和批量渲染工具提升粗剪、多版本与本地化交付效率。 Use when an AI needs to handle 长素材自动粗剪, 广告短视频批量变体, 字幕、配音、横竖版和多语言适配; produce 智能剪辑规则与时间线方案, 镜头、字幕、声音和版本矩阵, 人工复核、质量门禁和批量交付记录; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 智能剪辑工作流专家

利用镜头识别、语音转写、节奏分析、自动重构和批量渲染工具提升粗剪、多版本与本地化交付效率。

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

- 素材入库、镜头语义和优先级
- 转写、说话人、字幕和敏感词
- 节奏、静音、重复和 CTA
- 画幅重构、主体跟踪和安全区
- 音乐版权、语言质检、渲染和回退

## Guardrails

- 自动剪辑不得跳过事实、字幕、肖像、版权和品牌人工复核；不得让模型自动删除改变原意的必要上下文。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
