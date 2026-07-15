# Rust 后端资深专家专业检查表

## 执行前

- [ ] 目标、范围、国家/渠道/系统、周期和责任人明确
- [ ] 已区分事实、假设、缺失数据和待确认口径
- [ ] 已读取一手资料，并记录来源时间与适用版本

## 核心维度

- [ ] crate、module 和 feature 边界 已定义、验证或标记为未知
- [ ] ownership、borrowing 和领域类型 已定义、验证或标记为未知
- [ ] Result、错误分层和恢复 已定义、验证或标记为未知
- [ ] async runtime、Send/Sync 和取消 已定义、验证或标记为未知
- [ ] unsafe 边界、测试和性能测量 已定义、验证或标记为未知

## 官方基线资料

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Cargo Book](https://doc.rust-lang.org/cargo/)


## 失败模式

- 只有最佳实践，没有结合当前证据和约束。
- 只覆盖顺利路径，没有异常、补偿、回滚和人工介入。
- 指标同名但 scope、状态、时区、币种或归因窗口不同。
- 动作没有 owner、投入、依赖、验收或停止条件。

## 交付前

- [ ] 关键结论能追溯到证据或计算
- [ ] 备选方案、取舍和不做事项清楚
- [ ] 计划可分阶段执行并有验证与恢复路径
