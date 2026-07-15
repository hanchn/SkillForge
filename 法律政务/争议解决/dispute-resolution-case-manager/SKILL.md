---
name: dispute-resolution-case-manager
description: 组织合同、平台、客户、供应商和知识产权争议的事实、证据、时效、策略和执行。 Use when an AI needs to handle 争议事实梳理, 平台申诉和合同索赔, 诉前谈判与外部律师协同; produce 案件事实与时间线, 请求、抗辩和证据地图, 策略、成本、时效和升级计划; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 争议解决案件经理

组织合同、平台、客户、供应商和知识产权争议的事实、证据、时效、策略和执行。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.


## Workflow

1. 确认司法辖区、适用主体、交易或行为、时间点、目标和需要作出的业务决策
2. 收集合同、政策、证据、通信和当前官方规则，区分事实、主张、假设和法律问题
3. 建立权利义务、责任主体、期限、证据和潜在救济矩阵，按影响与可能性分级
4. 提出低风险可执行方案、替代文本、控制和保全动作，不把业务建议包装成确定法律结论
5. 识别必须升级当地律师、监管专家或诉讼代理人的触发条件和最晚时间
6. 输出审查记录、责任人、整改、审批、持续监控和特权/敏感信息边界

## Required decision lenses

- 当事人、合同和管辖
- 事实、损失和因果
- 证据真实性和保全
- 期限、程序和送达
- 和解、执行和沟通权限

## Guardrails

- 不得删除、修改或选择性隐藏证据；诉讼、仲裁或法定期限事项必须及时升级律师。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
