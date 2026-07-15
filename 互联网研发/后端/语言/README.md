# 后端语言架构

## 分类定位

按 Java、Go、Python、Node.js 的运行模型和生态细化架构。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [Go 后端架构师](Go/go-backend-architecture/README.md)：按 Go 的显式依赖、并发模型和简洁包边界设计可靠后端。 Use when an AI needs to handle Go API 或任务服务, 高并发 Go 服务治理, Go 单仓多服务架构; produce Go 包与服务架构, 并发和取消模型, 错误、测试和部署方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [Java 后端架构师](Java/java-backend-architecture/README.md)：利用 Java 类型、并发、JVM 和模块生态设计长期可维护的后端系统。 Use when an AI needs to handle Java 服务平台架构, 大型 Java 单体模块化, JVM 性能和升级治理; produce Java 模块架构, 并发与资源模型, JVM 运行和演进方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [Node.js 后端架构师](Node.js/nodejs-backend-architecture/README.md)：按事件循环、模块格式、异步失败和资源限制设计可靠 Node.js 后端。 Use when an AI needs to handle Node.js API 和 BFF, 高 I/O 服务架构, CommonJS 到 ESM 迁移; produce Node.js 模块架构, 异步与资源模型, 可靠性和部署方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
- [Python 后端架构师](Python/python-backend-architecture/README.md)：围绕包结构、类型边界、同步异步模型和运行环境设计可维护 Python 后端。 Use when an AI needs to handle Python Web 或任务平台, 脚本向服务化演进, 同步与异步混合系统治理; produce Python 包与层次架构, 执行和并发模型, 依赖、测试和部署方案; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
