# NestJS 架构

## 分类定位

处理 module、provider、请求管道和集成边界。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [NestJS 后端架构师](nestjs-backend-architecture/README.md)：围绕 module、provider、边界契约和请求管道设计模块化 NestJS 系统。适用于NestJS 企业 API、模块边界和依赖治理、单体到服务化演进，交付NestJS 模块架构、provider 与请求管道设计、测试和部署方案。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
