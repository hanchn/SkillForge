# 前后端开发核心 Skills 地图

> 版本：1.0.0
> 日期：2026-07-15

## 核心组合

| 排名 | Skill | 主要职责 |
|---:|---|---|
| 1 | frontend-feature-implementer | 在现有仓库中实现完整前端功能和全部交互状态 |
| 2 | frontend-architecture-designer | 统一管理模块边界、URL、服务端缓存、表单、本地状态与数据流 |
| 3 | frontend-localization-verifier | 验证翻译、格式、布局、RTL、路由和多语言 SEO |
| 4 | frontend-performance-analyzer | 用 RUM、trace、waterfall 和 bundle 定位性能根因 |
| 5 | web-performance-accessibility-auditor | 联合审计性能、键盘、语义、焦点和响应式体验 |
| 6 | api-contract-designer | 设计 API Schema、错误、幂等、并发和兼容 |
| 7 | backend-service-architect | 设计领域边界、数据 ownership、故障和演进架构 |
| 8 | database-migration-planner | 规划在线 schema/data 迁移、backfill、对账和恢复 |
| 9 | test-strategy-designer | 根据风险选择测试层、release gate 和生产验证 |
| 10 | production-incident-diagnostician | 用证据化假设完成止损、定位、恢复和复盘 |

## 设计原则

- 前端不能只覆盖静态正常态，必须覆盖加载、空、失败、权限、并发、键盘和响应式。
- 前端性能必须把现场数据与实验室数据分开，并从 trace 定位具体资源或主线程根因。
- 后端架构必须从领域不变量和数据 ownership 出发，不默认微服务。
- 数据库变更使用 expand-migrate-contract，并考虑锁、旧版本兼容、对账和恢复。
- 安全日志、对象授权、输入验证和敏感数据边界是后端设计的一部分。
- 测试与故障诊断必须保留真实证据，不能用“构建成功”或“服务恢复”代替完整验收。

## 研发角色组合

- `fullstack-feature-delivery`（全栈开发资深专家）：把前端、API、后端、数据库、测试、迁移和发布组合成可部署垂直切片。
- `fullstack-developer-weekly-report`：生成证据驱动的全栈开发周报。
- `fullstack-quality-engineer`（全栈测试资深专家）：跨前端、后端、数据、性能、安全和发布验证完整质量风险。
- `fullstack-qa-weekly-report`：生成风险与发布 gate 驱动的全栈测试周报。

## 官方技术依据

- [React state management guidance](https://react.dev/learn/managing-state)
- [MDN Web Performance](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [OWASP security logging and monitoring](https://devguide.owasp.org/en/04-design/02-web-app-checklist/09-logging-monitoring/)
- [PostgreSQL data definition](https://www.postgresql.org/docs/current/ddl.html)
- [PostgreSQL ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html)
