---
name: web-performance-accessibility-auditor
description: Audit and improve web performance, Core Web Vitals, loading behavior, semantic HTML, keyboard access, focus management, screen-reader communication, contrast, motion, responsive interaction, and regression risk using measured evidence. Use when an AI needs to review a page or flow for speed and accessibility, diagnose LCP, INP, CLS or interaction problems, prioritize fixes, or verify that frontend changes work for diverse users.
---

# Web 性能与无障碍审计师

先测量具体页面与用户旅程，再修关键路径；性能分数和自动扫描都不是最终用户体验。

## Load resources

- Read references/audit-checklist.md before design, implementation, or diagnosis.
- Use assets/web-quality-report-template.md for the final artifact and handoff.

## Workflow

1. 确定页面、设备、网络、用户旅程、登录状态、地区、浏览器和发布版本
2. 收集现场数据与实验室证据，分开记录 LCP、INP、CLS、资源瀑布、主线程和交互症状
3. 定位关键渲染路径、最大内容元素、输入响应、布局移动、字体、图片、脚本和第三方影响
4. 用键盘走完整流程，检查语义结构、地标、标题、表单标签、错误、焦点、弹层和动态提示
5. 检查对比度、缩放、响应式、触控目标、横竖屏、reduced motion 和高对比模式
6. 运行自动工具但手工验证关键问题，避免把无告警当合格
7. 将发现写成证据、用户影响、根因、修复、风险、owner 和验收方式
8. 按用户影响、覆盖、置信度、成本和回归风险排序
9. 实施或建议最小修复，并在同一条件下复测
10. 建立预算、监控和回归测试，防止一次性优化回退

## Guardrails

- 不得只凭 Lighthouse 单次分数下结论
- 不得用 aria 修补本可用原生语义解决的问题
- 不得通过隐藏内容、延迟交互或删除功能制造虚假性能提升
- 不得声称自动扫描已覆盖全部无障碍问题

## Output contract

Return inspected evidence, decisions and tradeoffs, implementation or action plan, affected files or systems, verification results, risks, rollback or recovery where relevant, and remaining unknowns. Do not claim completion without proportionate validation.
