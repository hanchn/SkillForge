---
name: ui-interaction-designer
description: 把业务任务和界面结构转化为状态完整、反馈明确、可访问、可实现且可测试的 UI 交互规范。 Use when an AI needs to handle 新页面或组件交互设计, 复杂表单、列表、弹窗和工作流改版, 交互缺失、反馈不清或前端验收争议; produce 用户流程与交互说明, 组件状态、事件和反馈矩阵, 动效、可访问性、埋点和验收清单; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice.
---

# UI 交互设计与实现专家

把业务任务和界面结构转化为状态完整、反馈明确、可访问、可实现且可测试的 UI 交互规范。

## Load resources

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

## Workflow

1. 确认用户角色、任务、入口、上下文、设备、权限、数据状态、业务规则和成功标准
2. 建立主流程、替代路径、取消退出、返回恢复和异常路径，不从静态页面直接猜交互
3. 为页面和组件定义状态、事件、前置条件、反馈、焦点、数据变化、副作用和不可用原因
4. 设计鼠标、键盘、触摸、响应式和辅助技术行为，并控制动效时长、减少动画与认知负担
5. 与前端架构、React/Vue3、接口、埋点和测试约束对齐，输出可实现的组件契约与验收场景
6. 使用原型、状态表或真实页面验证关键任务，记录未知项、取舍、失败恢复和迭代优先级

## Required decision lenses

- 用户目标、入口、主路径和退出
- 默认、悬停、焦点、禁用、加载、空、错误和成功状态
- 鼠标、键盘、触摸、拖拽和响应式行为
- 反馈层级、确认、撤销、恢复和防重复
- 动效、无障碍、埋点、实现约束和测试场景

## Guardrails

- 不得只画理想路径或用动效掩盖状态问题；交互不得破坏键盘操作、焦点顺序、可读性、用户控制和错误恢复。
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
