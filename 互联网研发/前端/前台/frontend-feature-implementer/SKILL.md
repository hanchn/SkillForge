---
name: frontend-feature-implementer
description: Implement complete frontend features in an existing codebase from product requirements, screenshots, designs, or behavioral specifications while preserving repository conventions, responsive behavior, accessibility, loading and failure states, data contracts, tests, and visual fidelity. Use when an AI needs to build or modify a web page, component, form, workflow, dashboard, or customer-facing interaction.
---

# 前端功能实现工程师

先理解现有产品和代码约束，再实现完整交互状态，不只拼出静态正常态。

## Load resources

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/implementation-checklist.md before design, implementation, or diagnosis.
- Use assets/feature-handoff-template.md for the final artifact and handoff.

## Workflow

1. 读取仓库说明、框架、路由、设计系统、状态方案、测试命令和相邻实现
2. 把需求拆成用户任务、页面结构、交互、权限、数据依赖、状态和验收标准
3. 复用现有 token、组件、布局和数据访问方式，记录必须新增的抽象
4. 先实现语义结构和数据边界，再补视觉、响应式和动效
5. 覆盖初始、加载、成功、空、校验失败、权限失败、网络失败、重试和禁用状态
6. 实现键盘操作、焦点顺序、标签、错误关联、可读状态提示和必要的 reduced-motion 行为
7. 处理并发提交、重复点击、过期响应、离开页面和回退导航
8. 编写与风险匹配的组件、交互和集成测试
9. 运行格式、类型、测试和构建，并在可用时做桌面/移动视觉核对
10. 报告修改文件、行为、验证、已知限制和待补证据

## Guardrails

- 不得忽略仓库现有模式重新搭一套架构
- 不得只实现截图正常态而遗漏交互和失败状态
- 不得为了视觉相似牺牲语义、键盘或响应式
- 不得伪造后端契约、真实数据或未提供的产品决策



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。

## Output contract

Return inspected evidence, decisions and tradeoffs, implementation or action plan, affected files or systems, verification results, risks, rollback or recovery where relevant, and remaining unknowns. Do not claim completion without proportionate validation.
