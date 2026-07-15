# Rust 后端架构

## 分类定位

处理 ownership、类型、错误、async runtime 和 unsafe 边界。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [Rust 后端资深专家](rust-backend-architecture/README.md)：利用 ownership、类型系统、错误模型和 async runtime 设计安全可预测的 Rust 后端。适用于Rust API 或系统服务、高可靠高性能服务、Rust workspace 和 crate 架构，交付Rust crate 与领域架构、并发和资源模型、错误、测试和部署方案。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
