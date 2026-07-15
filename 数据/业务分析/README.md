# 跨境业务数据分析

## 分类定位

覆盖指标、经营、利润、商品、流量、漏斗、广告、客户、库存和预测。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [广告效果分析师](advertising-performance-analyst/README.md)：统一平台口径、公司收入和利润，分析广告效率、创意、受众和增量。 Use when an AI needs to handle 广告周报和预算复盘, ROAS/ACOS 波动, 创意和投放结构诊断; produce 广告表现报告, 驱动拆解与预算建议, 增量验证和测试计划; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [业务指标治理师](business-metrics-governance/README.md)：建立跨平台可复算的指标、维度、时间、币种和责任人标准。 Use when an AI needs to handle 经营指标字典, 多系统口径统一, 看板和周报上线前治理; produce 指标字典, 维度与数据血缘, 变更、认证和争议处理机制; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [电商转化漏斗分析师](conversion-funnel-analyst/README.md)：按一致人群、事件和时间窗定位从曝光到购买的转化损失。 Use when an AI needs to handle 商品或结账转化下降, 设备国家渠道漏斗比较, 改版和实验效果诊断; produce 漏斗诊断, 流失分层和证据, 实验与修复优先级; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [客户 Cohort 与 LTV 分析师](customer-cohort-ltv-analyst/README.md)：按获客 cohort、复购周期和贡献利润评估客户留存与长期价值。 Use when an AI needs to handle 复购和留存分析, 渠道客户质量比较, CAC 回收和 LTV 预测; produce cohort 留存表, LTV/CAC 和回收期, 分层策略与不确定性; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [经营分析与周月报专家](executive-business-review/README.md)：把可靠数据转化为结论先行、驱动清晰、可决策的 WBR/MBR/QBR。 Use when an AI needs to handle 跨境经营周报月报, 管理层业务复盘, 目标差距和行动跟踪; produce 经营摘要, KPI 与驱动分析, 风险、决策和责任闭环; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [经营预测与情景规划师](forecast-scenario-planner/README.md)：用透明假设、驱动模型和区间管理销售、利润、库存和现金预测。 Use when an AI needs to handle 月度滚动预测, 预算和目标拆解, 乐观基准悲观情景; produce 驱动型预测模型, 情景和敏感性分析, 假设、预警和更新机制; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [库存与供应链分析师](inventory-supply-chain-analyst/README.md)：量化可售、在途、缺货、周转、交期和履约，平衡服务水平与现金占用。 Use when an AI needs to handle 缺货和积压诊断, 库存健康周报, 供应商和物流绩效分析; produce 库存健康矩阵, 供需与交期驱动, 补货、处置和风险建议; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [跨平台渠道对比分析师](marketplace-channel-comparison-analyst/README.md)：统一订单、收入、费用、广告和客户口径后比较平台与独立站真实表现。 Use when an AI needs to handle Amazon、Shopify、TikTok 横向比较, 渠道资源分配, 渠道利润和客户质量评估; produce 渠道可比口径, 规模效率利润矩阵, 渠道角色和资源建议; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [价格与促销分析师](pricing-promotion-analyst/README.md)：评估价格、折扣和促销对销量、收入、利润、客户和库存的真实影响。 Use when an AI needs to handle 大促复盘, 价格调整效果, 优惠券和捆绑机制比较; produce 价格促销效果报告, 增量和蚕食测算, 机制优化建议; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [商品组合分析师](product-portfolio-analyst/README.md)：从需求、转化、利润、库存和生命周期评估 SKU 角色与动作。 Use when an AI needs to handle SKU 分层, 新品和长尾评估, 淘汰、补货与资源分配; produce 商品组合矩阵, SKU 诊断与动作, 新品、保留和退出规则; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [销售与利润分析师](sales-profitability-analyst/README.md)：拆解销售、毛利、贡献利润和现金驱动，定位真正创造或消耗价值的业务单元。 Use when an AI needs to handle 销售和利润波动, 国家渠道 SKU 盈利分析, 利润改善机会评估; produce 收入利润桥, 分层盈利矩阵, 驱动、风险和改善测算; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [流量与获客分析师](traffic-acquisition-analyst/README.md)：区分用户级与会话级来源，评估流量规模、质量、成本和下游价值。 Use when an AI needs to handle 渠道流量波动, 自然与付费获客质量, UTM 和来源口径排查; produce 流量来源分析, 质量与成本矩阵, 归因限制和优化建议; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
