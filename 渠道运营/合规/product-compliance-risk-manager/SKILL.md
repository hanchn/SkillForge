---
name: product-compliance-risk-manager
description: Screen and manage cross-border product compliance, safety, labeling, documentation, restricted-product, marketplace, claim, testing, recall, and evidence risks by target market and sales channel. Use when an AI needs to determine what must be verified before sourcing, listing, advertising, importing, or selling a product on Amazon or an owned storefront. This skill supports issue spotting and evidence management, not licensed legal or laboratory certification.
---

# 跨境商品合规风险管理器

先按市场、产品和声明建立适用性，再核验证据；供应商说合规不等于可销售。

## Load resources

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/compliance-evidence-checklist.md before analysis or execution.
- Use assets/compliance-risk-register.md for the final plan and handoff.

## Workflow

1. 确认目标国家/地区、销售渠道、产品类型、材料、用途、用户、年龄、能源或化学属性和所有营销声明
2. 建立适用性问题清单，区分法律、海关、产品安全、标签、平台政策、广告声明和自愿认证
3. 优先查询当前官方监管和平台来源，记录规则名称、版本、日期、范围和责任主体
4. 建立证据台账，核对测试报告、证书、实验室、样品/BOM、型号、工厂、有效期和目标市场是否一致
5. 将每项声明映射到证据和允许表述，删除超出样品、方法、地域或有效期的结论
6. 检查产品、包装、说明书、警告、语言、追踪标识、进口方和线上详情页的一致性
7. 评估缺证、限制、召回、下架、库存处置、账户健康和产品责任影响
8. 按阻塞、需专业确认、可整改和已满足分类，指定责任人与截止时间
9. 在变更材料、工厂、型号、市场、声明或规则后重新验证

## Guardrails

- 不得宣布产品合法、合规或已认证，除非有适用且可验证的当前证据
- 不得替代律师、海关顾问、认证机构或实验室
- 不得用一个市场或型号的证据覆盖其他市场和变体
- 高风险儿童、医疗、电气、食品接触、化学品等必须升级专业审查



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。

## Output contract

Return the decision context, evidence and assumptions, analysis or plan, prioritized actions, owners and dependencies, acceptance or decision thresholds, risks, and the next review point. Keep observed facts separate from estimates and recommendations.
