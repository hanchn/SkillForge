<!-- generated-by: sync-skill-depth -->
# API 契约设计师场景作战手册

本文件用于把现有专业流程扩展为完整业务结果。必须选择一个主场景，并说明是否叠加其他场景。

## 场景 1：从产品需求设计 HTTP API

- 业务理解：解释本场景的对象、术语、启动原因、结果使用者和错误后果。
- 输入与补证：必需 capability_or_existing_contract；建议补充 consumer_context、repository_conventions、security_model、compatibility_constraints；来源、日期、版本和可信度必须记录。
- 上下游：确认输入 owner、下游消费者、系统事实源、审批人、执行人和交接 SLA。
- 决策：比较维持现状、推荐方案和低风险备选，记录适用条件、反证、成本、风险与可逆性。
- 异常：覆盖缺数据、口径冲突、权限不足、依赖失败、超时、部分成功、人工升级、补偿和回滚。
- 完成：交付 api_contract.md、schema_or_spec_skeleton、compatibility_rollout.md，并附验收证据、责任人、截止、停止条件和复盘时间。

## 场景 2：审查 OpenAPI 契约的一致性和兼容性

- 业务理解：解释本场景的对象、术语、启动原因、结果使用者和错误后果。
- 输入与补证：必需 capability_or_existing_contract；建议补充 consumer_context、repository_conventions、security_model、compatibility_constraints；来源、日期、版本和可信度必须记录。
- 上下游：确认输入 owner、下游消费者、系统事实源、审批人、执行人和交接 SLA。
- 决策：比较维持现状、推荐方案和低风险备选，记录适用条件、反证、成本、风险与可逆性。
- 异常：覆盖缺数据、口径冲突、权限不足、依赖失败、超时、部分成功、人工升级、补偿和回滚。
- 完成：交付 api_contract.md、schema_or_spec_skeleton、compatibility_rollout.md，并附验收证据、责任人、截止、停止条件和复盘时间。

## 场景 3：设计事件 Schema、投递、重放和去重语义

- 业务理解：解释本场景的对象、术语、启动原因、结果使用者和错误后果。
- 输入与补证：必需 capability_or_existing_contract；建议补充 consumer_context、repository_conventions、security_model、compatibility_constraints；来源、日期、版本和可信度必须记录。
- 上下游：确认输入 owner、下游消费者、系统事实源、审批人、执行人和交接 SLA。
- 决策：比较维持现状、推荐方案和低风险备选，记录适用条件、反证、成本、风险与可逆性。
- 异常：覆盖缺数据、口径冲突、权限不足、依赖失败、超时、部分成功、人工升级、补偿和回滚。
- 完成：交付 api_contract.md、schema_or_spec_skeleton、compatibility_rollout.md，并附验收证据、责任人、截止、停止条件和复盘时间。

## 不可突破的边界

不泄露内部存储与拓扑作为公共契约；不承诺无法保证的恰好一次语义；不以整理字段名为由引入破坏性变更

## 跨场景检查

- 人员：谁提出、谁提供事实、谁决策、谁执行、谁验收、谁承担失败后果。
- 系统：source of truth、状态、版本、权限、写回、幂等、对账、日志和留存。
- 经营：收入、利润、现金、客户、质量、时效、合规和可逆性之间的取舍。
- 学习：领先指标、结果指标、护栏指标、失败样本、下次刷新和 Skill 更新 owner。
