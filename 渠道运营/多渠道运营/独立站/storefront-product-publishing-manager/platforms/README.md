# Platform Adapters

核心生命周期、授权和验证规则位于 SKILL.md。

- 有官方后台、API 或连接器时，先读取当前状态，再执行经过授权的最小变更。
- 只有代码仓库时，修改商品源数据或同步配置，并验证部署后的真实店铺状态。
- 没有认证写入能力时，只生成审批就绪的变更计划和人工操作检查表。
- 平台术语不同，必须映射 draft、active、published、hidden、archived 和 deleted 的真实语义，不能直接套用。
