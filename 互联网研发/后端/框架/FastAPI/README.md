# FastAPI 架构

## 分类定位

处理 APIRouter、Depends、Pydantic、异步和部署。

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

- [FastAPI 后端架构师](fastapi-backend-architecture/README.md)：围绕 APIRouter、依赖注入、Pydantic 契约和异步边界设计生产级 FastAPI 服务。适用于FastAPI 中大型应用、Python API 模块化、异步 API 性能和可靠性治理，交付FastAPI 包与路由架构、依赖和数据契约、运行、测试和部署方案。

## 迭代记录

| 日期 | 更新 |
|---|---|
| 2026-07-15 | 建立分类定位、选择原则和正式 Skill 索引。 |
