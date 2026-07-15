<!-- generated-by: sync-skill-depth -->
# 测试策略设计师场景作战手册

本文件用于把现有专业流程扩展为完整业务结果。必须选择一个主场景，并说明是否叠加其他场景。

## 场景 1：为新功能、API、迁移、事故修复或第三方集成制定测试策略

- 业务理解：解释本场景的对象、术语、启动原因、结果使用者和错误后果。
- 输入与补证：必需 change_scope_or_requirements；建议补充 architecture、incident_history、release_constraints、environments；来源、日期、版本和可信度必须记录。
- 上下游：确认输入 owner、下游消费者、系统事实源、审批人、执行人和交接 SLA。
- 决策：比较维持现状、推荐方案和低风险备选，记录适用条件、反证、成本、风险与可逆性。
- 异常：覆盖缺数据、口径冲突、权限不足、依赖失败、超时、部分成功、人工升级、补偿和回滚。
- 完成：交付 test_strategy.md、risk_coverage_matrix.md、release_gates.md，并附验收证据、责任人、截止、停止条件和复盘时间。

## 场景 2：审查现有测试计划的高风险漏测

- 业务理解：解释本场景的对象、术语、启动原因、结果使用者和错误后果。
- 输入与补证：必需 change_scope_or_requirements；建议补充 architecture、incident_history、release_constraints、environments；来源、日期、版本和可信度必须记录。
- 上下游：确认输入 owner、下游消费者、系统事实源、审批人、执行人和交接 SLA。
- 决策：比较维持现状、推荐方案和低风险备选，记录适用条件、反证、成本、风险与可逆性。
- 异常：覆盖缺数据、口径冲突、权限不足、依赖失败、超时、部分成功、人工升级、补偿和回滚。
- 完成：交付 test_strategy.md、risk_coverage_matrix.md、release_gates.md，并附验收证据、责任人、截止、停止条件和复盘时间。

## 场景 3：定义发布 gate、focused regression 和上线后验证

- 业务理解：解释本场景的对象、术语、启动原因、结果使用者和错误后果。
- 输入与补证：必需 change_scope_or_requirements；建议补充 architecture、incident_history、release_constraints、environments；来源、日期、版本和可信度必须记录。
- 上下游：确认输入 owner、下游消费者、系统事实源、审批人、执行人和交接 SLA。
- 决策：比较维持现状、推荐方案和低风险备选，记录适用条件、反证、成本、风险与可逆性。
- 异常：覆盖缺数据、口径冲突、权限不足、依赖失败、超时、部分成功、人工升级、补偿和回滚。
- 完成：交付 test_strategy.md、risk_coverage_matrix.md、release_gates.md，并附验收证据、责任人、截止、停止条件和复盘时间。

## 不可突破的边界

不按测试数量衡量质量；不默认测试环境等同生产；不为同一风险在每一层机械复制用例

## 跨场景检查

- 人员：谁提出、谁提供事实、谁决策、谁执行、谁验收、谁承担失败后果。
- 系统：source of truth、状态、版本、权限、写回、幂等、对账、日志和留存。
- 经营：收入、利润、现金、客户、质量、时效、合规和可逆性之间的取舍。
- 学习：领先指标、结果指标、护栏指标、失败样本、下次刷新和 Skill 更新 owner。
