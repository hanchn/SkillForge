---
name: frontend-performance-analyzer
description: Diagnose frontend performance using field and laboratory evidence, Core Web Vitals, navigation and interaction traces, network waterfalls, rendering, main-thread tasks, JavaScript execution, bundles, images, fonts, caching, hydration, data fetching, third-party scripts, memory, and performance budgets. Use when an AI needs a deep root-cause analysis of slow pages or interactions, to compare builds, prioritize performance work, or verify that a fix improves real user experience without breaking behavior.
---

# 前端性能分析师

从真实用户症状和 trace 根因出发，不用一个 Lighthouse 分数代替性能分析。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/performance-analysis-checklist.md before verification or diagnosis.
- Use assets/performance-report-template.md for the final evidence record.

## Workflow

1. 定义页面、用户旅程、设备、网络、地区、缓存、登录、实验和构建版本
2. 先读取 RUM/现场分布，再在匹配条件下采集可复现的实验室导航与交互 trace
3. 确认 LCP、INP、CLS 及业务关键时间点，定位受影响人群和回归时间
4. 分析网络瀑布、关键请求链、TTFB、缓存、压缩、优先级、图片、字体和第三方资源
5. 分析主线程长任务、事件处理、布局/样式、绘制、hydration、GC 和脚本解析执行
6. 检查 bundle 组成、重复依赖、动态导入、tree shaking、polyfill、source map 和路由级加载
7. 分析数据请求 waterfall、过度获取、缓存失效、串行依赖、竞态和服务端/客户端重复工作
8. 将每项发现关联到用户症状、trace 证据、根因、影响范围、修复和回归风险
9. 按影响、覆盖、信心、成本和可逆性排序；先做可证明的关键路径改善
10. 在相同环境复测现场/实验室指标、功能、SEO、可访问性和业务 guardrail，并建立预算与告警

## Guardrails

- 不得只用单次 Lighthouse 或本机高速网络结果下结论
- 不得通过延迟功能、隐藏内容或取消必要验证制造指标改善
- 不得把服务端 TTFB、第三方和客户端执行问题混成一个前端结论
- 不得声称优化有效而没有同条件 before/after 证据

## Output contract

Return scope and environment, evidence, findings with severity and confidence, root causes, prioritized fixes, acceptance criteria, before/after verification where applicable, owners, and remaining specialist review.
