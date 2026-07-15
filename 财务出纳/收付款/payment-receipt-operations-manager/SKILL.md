---
name: payment-receipt-operations-manager
description: 建立从业务申请、单据校验、授权审批、支付执行、回单归档到状态回写的收付款闭环。 Use when an AI needs to handle 供应商和物流付款, 客户、平台和渠道收款认领, 批量付款与失败重试; produce 收付款 SOP 与权限矩阵, 支付批次和状态台账, 回单、异常和升级记录; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# 收付款执行管理员

建立从业务申请、单据校验、授权审批、支付执行、回单归档到状态回写的收付款闭环。

## Load resources

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

## Workflow

1. 确认付款或收款主体、账户、币种、金额、用途、日期、交易对手和授权边界
2. 核验申请、合同、发票或收据、预算、审批、收款信息和防重复标识，缺项即暂停
3. 按申请、审批、执行、记账、对账分离原则检查权限、限额、双人复核和敏感凭证保管
4. 执行或编排收付款、回单、日记账、状态回写和档案留存，完整记录失败、退回与在途
5. 将银行流水、支付平台、业务单据和余额相互勾稽，建立未达账、异常和关闭证据
6. 输出可复核台账、异常升级、责任人、截止时间和资金安全检查，不暴露任何密钥凭证

## Required decision lenses

- 付款主体、账户和币种
- 申请、合同、发票与审批
- 收款识别和核销线索
- 支付状态、回单和在途
- 重复支付、篡改和欺诈拦截

## Guardrails

- 不得在授权或单据不完整时执行付款；付款执行、账务确认与独立复核必须分离。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
