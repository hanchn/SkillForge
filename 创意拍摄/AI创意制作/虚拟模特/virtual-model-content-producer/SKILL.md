---
name: virtual-model-content-producer
description: 使用合规的人像生成、模特替换或虚拟试穿工具制作跨人群商品内容，并严格保持商品结构与真实属性。 Use when an AI needs to handle 服饰、配件和生活方式虚拟模特图, 多地区模特与场景版本, 真人素材的合规模特替换; produce 虚拟模特制作 brief, 身份、姿态、商品一致性和版本方案, 真实性、授权、偏差和交付验收报告; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 虚拟模特内容制作专家

使用合规的人像生成、模特替换或虚拟试穿工具制作跨人群商品内容，并严格保持商品结构与真实属性。

## Load resources

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

- 商品版型、纹理、颜色和遮挡
- 人物身份、年龄表达、体型和肤色覆盖
- 姿态、手部、接触点和物理合理性
- 输入人像、肖像权和训练使用授权
- 跨版本一致性、合成披露和失败样本

## Guardrails

- 不得未经授权复刻真实人物、名人或未成年人；不得改变商品版型、颜色、纹理、尺寸关系和功能效果，无法验证时必须标记为概念图。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
