# 测试策略设计师

用最小但可信的测试组合降低变更风险，并让失败可定位。

## 适用场景

- 为数据库迁移和双写发布设计测试策略与回滚信号。
- 审查现有测试计划，找出高风险漏测和低价值重复覆盖。
- 为第三方支付接入制定契约、异常、重试和生产验证方案。

## 交付物

- test_strategy.md
- risk_coverage_matrix.md
- release_gates.md

## 边界

- 不按测试数量衡量质量
- 不默认测试环境等同生产
- 不为同一风险在每一层机械复制用例

## 使用入口

1. 先读 SKILL.md。
2. 按 SKILL.md 指示读取 references 或 assets 中的专用资料。
3. 按 INVOCATION.md 执行并用 eval/acceptance.md 验收。

整个目录可作为独立跨平台 skill 包分发。README 只负责给人说明，不是执行入口。
