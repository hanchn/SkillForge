# 前端语言架构

## 分类定位

处理 JavaScript、TypeScript 等语言自身的模块、类型、运行时和工程约束。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [JavaScript 前端架构师](JavaScript/javascript-frontend-architecture/README.md)：针对 JavaScript 动态类型、模块系统和浏览器运行时设计可维护前端架构。适用于大型 JavaScript 应用治理、ESM 与旧模块迁移、运行时契约和质量门禁设计，交付JavaScript 架构方案、模块与运行时契约、渐进治理计划。
- [TypeScript 前端架构师](TypeScript/typescript-frontend-architecture/README.md)：利用类型系统、项目引用和真实运行时契约设计可扩展 TypeScript 前端。适用于TypeScript 单仓或多包架构、类型边界和 API 类型治理、大型项目编译性能治理，交付TypeScript 分层方案、类型与运行时边界、tsconfig 和包治理建议。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
