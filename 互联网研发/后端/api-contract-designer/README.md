# API 契约设计师

从消费者行为、领域不变量和兼容性出发设计稳定接口。

## 适用场景

- 为批量创建订单设计支持幂等和部分失败的 HTTP 契约。
- 审查这份 OpenAPI，找出兼容性、分页和错误语义问题。
- 把这些领域事件整理成可重放、可演进的事件契约。

## 交付物

- api_contract.md
- schema_or_spec_skeleton
- compatibility_rollout.md

## 边界

- 不泄露内部存储与拓扑作为公共契约
- 不承诺无法保证的恰好一次语义
- 不以整理字段名为由引入破坏性变更

## 使用入口

1. 先读 SKILL.md。
2. 按 SKILL.md 指示读取 references 或 assets 中的专用资料。
3. 按 INVOCATION.md 执行并用 eval/acceptance.md 验收。

整个目录可作为独立跨平台 skill 包分发。README 只负责给人说明，不是执行入口。
