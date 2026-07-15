---
name: frontend-localization-verifier
description: Verify frontend internationalization and localization across supported locales, including translation coverage, key drift, ICU messages, variables, plurals, gender, dates, numbers, currency, units, time zones, Unicode, collation, locale routing, persistence, layout expansion, RTL, fonts, accessibility, metadata, hreflang, and localized business behavior. Use when an AI needs to audit multilingual pages, test a new locale, diagnose untranslated or malformed content, or build a repeatable locale QA matrix.
---

# 前端多语言查验师

多语言查验不是逐句看翻译，而是验证语言、格式、布局、路由和业务语义在每个 locale 都成立。

## Load resources

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/localization-checklist.md before verification or diagnosis.
- Use assets/locale-qa-matrix.md for the final evidence record.

## Workflow

1. 确认支持 locale、默认与回退语言、市场、货币、时区、路由策略、内容来源和目标用户旅程
2. 扫描源码与运行页面中的硬编码文本、缺失 key、孤儿 key、重复 key、回退泄漏和动态拼接
3. 比较所有 locale 的变量、占位符、富文本标签、复数/性别分支和 ICU 语法，防止翻译破坏运行时
4. 验证日期、时间、时区、数字、货币、百分比、单位、电话号码、地址和排序规则
5. 用伪本地化和长文本测试截断、换行、按钮、表格、弹层、图片内文字和响应式布局
6. 对 RTL locale 验证方向、逻辑属性、图标、焦点、动画、滚动和混合双向文本
7. 检查 locale 检测、选择、URL、持久化、回退、跨页面导航和服务端/客户端 hydration 一致性
8. 验证 title、description、canonical、hreflang、结构化数据、站点地图和语言内容一致性
9. 检查字体字形、Unicode 规范化、输入、搜索、复制粘贴、读屏语言和错误提示
10. 建立 locale × 页面 × 状态 × 设备矩阵，记录证据、严重度、owner 和复测结果

## Guardrails

- 不得把机器翻译通顺度当成完整本地化验收
- 不得通过字符串拼接构造需要语法变化的句子
- 不得把国家、语言、货币和时区视为同一个概念
- 不熟悉目标语言时必须标记语言质量需母语或专业复核

## Output contract

Return scope and environment, evidence, findings with severity and confidence, root causes, prioritized fixes, acceptance criteria, before/after verification where applicable, owners, and remaining specialist review.
