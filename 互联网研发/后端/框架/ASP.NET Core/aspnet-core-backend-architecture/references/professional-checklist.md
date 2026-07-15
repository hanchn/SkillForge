# ASP.NET Core 后端架构师专业检查表

## 执行前

- [ ] 目标、范围、国家/渠道/系统、周期和责任人明确
- [ ] 已区分事实、假设、缺失数据和待确认口径
- [ ] 已读取一手资料，并记录来源时间与适用版本

## 核心维度

- [ ] host、configuration 和 options 已定义、验证或标记为未知
- [ ] DI lifetime 与 module registration 已定义、验证或标记为未知
- [ ] middleware 顺序和 endpoint 已定义、验证或标记为未知
- [ ] EF Core 事务和后台服务 已定义、验证或标记为未知
- [ ] 认证授权、health、logging 和部署 已定义、验证或标记为未知

## 官方基线资料

- [ASP.NET Core Fundamentals](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0)
- [ASP.NET Core Architecture Tests](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/test-asp-net-core-mvc-apps)


## 失败模式

- 只有最佳实践，没有结合当前证据和约束。
- 只覆盖顺利路径，没有异常、补偿、回滚和人工介入。
- 指标同名但 scope、状态、时区、币种或归因窗口不同。
- 动作没有 owner、投入、依赖、验收或停止条件。

## 交付前

- [ ] 关键结论能追溯到证据或计算
- [ ] 备选方案、取舍和不做事项清楚
- [ ] 计划可分阶段执行并有验证与恢复路径
