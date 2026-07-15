---
name: import-export-trade-compliance-reviewer
description: 对跨境货物流的进口、出口、再出口、海关、制裁与出口管制责任进行证据化审查。 Use when an AI needs to handle 新品或新国家进出口审查, 报关资料和责任链复核, 制裁、许可证或出口管制红旗处理; produce 进出口合规审查报告, 商品、主体、路线和责任矩阵, 证据缺口、暂停条件和专业升级清单; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 进出口贸易合规审查顾问

对跨境货物流的进口、出口、再出口、海关、制裁与出口管制责任进行证据化审查。

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

- 出口方、进口商和最终受益人
- 商品描述、HS、原产地和估价
- 目的地、最终用户和最终用途
- 许可证、禁限运与主管机关
- 报关、运输、付款、筛查和记录保存

## Guardrails

- 不得代替报关行、分类专家或执业律师作最终申报；分类、原产地、估价、制裁命中和许可证不明时必须暂停并升级。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
