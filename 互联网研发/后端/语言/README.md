# 后端语言架构

## 分类定位

按 Java、Go、Python、Node.js 的运行模型和生态细化架构。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [C# 后端架构师](C#/csharp-backend-architecture/README.md)：围绕 solution/project、类型、async/await、依赖注入和 .NET 运行时设计稳健后端。适用于C# 企业后端架构、.NET 单体模块化、异步、资源和版本升级治理，交付C# solution 与模块架构、异步和资源生命周期、依赖、测试和部署方案。
- [Go 后端架构师](Go/go-backend-architecture/README.md)：按 Go 的显式依赖、并发模型和简洁包边界设计可靠后端。适用于Go API 或任务服务、高并发 Go 服务治理、Go 单仓多服务架构，交付Go 包与服务架构、并发和取消模型、错误、测试和部署方案。
- [Java 后端架构师](Java/java-backend-architecture/README.md)：利用 Java 类型、并发、JVM 和模块生态设计长期可维护的后端系统。适用于Java 服务平台架构、大型 Java 单体模块化、JVM 性能和升级治理，交付Java 模块架构、并发与资源模型、JVM 运行和演进方案。
- [Node.js 后端架构师](Node.js/nodejs-backend-architecture/README.md)：按事件循环、模块格式、异步失败和资源限制设计可靠 Node.js 后端。适用于Node.js API 和 BFF、高 I/O 服务架构、CommonJS 到 ESM 迁移，交付Node.js 模块架构、异步与资源模型、可靠性和部署方案。
- [PHP 后端架构师](PHP/php-backend-architecture/README.md)：围绕 namespace、Composer、请求生命周期和显式模块边界设计可维护 PHP 后端。适用于PHP 业务系统架构、遗留 PHP 模块化重构、PHP 运行和依赖治理，交付PHP 模块与包架构、请求和资源生命周期、依赖、测试和部署方案。
- [Python 后端架构师](Python/python-backend-architecture/README.md)：围绕包结构、类型边界、同步异步模型和运行环境设计可维护 Python 后端。适用于Python Web 或任务平台、脚本向服务化演进、同步与异步混合系统治理，交付Python 包与层次架构、执行和并发模型、依赖、测试和部署方案。
- [Rust 后端架构师](Rust/rust-backend-architecture/README.md)：利用 ownership、类型系统、错误模型和 async runtime 设计安全可预测的 Rust 后端。适用于Rust API 或系统服务、高可靠高性能服务、Rust workspace 和 crate 架构，交付Rust crate 与领域架构、并发和资源模型、错误、测试和部署方案。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
