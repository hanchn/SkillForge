# Gin 架构

## 分类定位

处理路由、middleware、显式依赖和 Go HTTP 运行时。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [Gin 后端架构师](gin-backend-architecture/README.md)：围绕路由、middleware、显式依赖和 Go 运行模型设计精简可靠的 Gin 服务。适用于Gin API 新建或重构、高吞吐 Go HTTP 服务、middleware 和安全治理，交付Gin 路由与模块架构、middleware 和依赖方案、性能、安全和部署计划。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
