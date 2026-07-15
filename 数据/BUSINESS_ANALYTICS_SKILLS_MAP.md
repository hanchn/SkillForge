# 跨境业务数据分析 Skill 地图

## 分析底座

先使用 `business-metrics-governance` 统一指标，再使用 `data-quality-reconciliation` 验证数据，出现异常时组合已有 `metric-diagnostics` 定位驱动。底座不可靠时，业务专项分析只能给出带限制的暂定结论。

## 专项分析

| 业务问题 | 主要 Skill | 典型产物 |
|---|---|---|
| 公司整体经营如何 | `executive-business-review` | WBR/MBR/QBR、决策和行动闭环 |
| 收入和利润为何变化 | `sales-profitability-analyst` | 收入利润桥、盈利矩阵 |
| 哪些 SKU 应加码或退出 | `product-portfolio-analyst` | 商品组合矩阵和动作 |
| 流量来自哪里、质量如何 | `traffic-acquisition-analyst` | 来源质量和成本矩阵 |
| 用户在哪个环节流失 | `conversion-funnel-analyst` | 可比漏斗与修复实验 |
| 广告是否有效 | `advertising-performance-analyst` | 效率、利润和增量分析 |
| 客户长期价值如何 | `customer-cohort-ltv-analyst` | cohort、LTV/CAC、回收期 |
| 库存和供应链是否健康 | `inventory-supply-chain-analyst` | 库存健康、交期和风险 |
| 价格和活动是否增量 | `pricing-promotion-analyst` | 弹性、增量、蚕食和利润 |
| 下月/季度会怎样 | `forecast-scenario-planner` | 驱动预测、情景和敏感性 |
| 各渠道真实表现如何 | `marketplace-channel-comparison-analyst` | 可比口径和渠道角色矩阵 |

## 强制口径

- 明确日期、时区、币种、税、退款、取消、归因窗口和订单状态。
- 区分用户、会话、事件、订单、订单行和商品粒度。
- 区分 GMV、收入、毛利、贡献利润和现金。
- 区分平台归因、观测相关和实验增量。

## 版本记录

| 版本 | 日期 | 更新内容 |
|---|---|---|
| 1.0.0 | 2026-07-15 | 建立跨境业务数据分析底座和十一类专项分析。 |
