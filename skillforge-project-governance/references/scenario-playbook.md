<!-- generated-by: sync-skill-depth -->
# SkillForge项目治理场景作战手册

本文件用于把现有专业流程扩展为完整业务结果。必须选择一个主场景，并说明是否叠加其他场景。

## 场景 1：新增、重构或升级任何 SkillForge skill

- 业务理解：解释本场景的对象、术语、启动原因、结果使用者和错误后果。
- 输入与补证：必需 业务目标与真实证据；建议补充 target_skill_path、target_business_domain、change_request；来源、日期、版本和可信度必须记录。
- 上下游：确认输入 owner、下游消费者、系统事实源、审批人、执行人和交接 SLA。
- 决策：比较维持现状、推荐方案和低风险备选，记录适用条件、反证、成本、风险与可逆性。
- 异常：覆盖缺数据、口径冲突、权限不足、依赖失败、超时、部分成功、人工升级、补偿和回滚。
- 完成：交付 project understanding、architecture guidance、skill package constraints，并附验收证据、责任人、截止、停止条件和复盘时间。

## 场景 2：决定一个新能力应放在哪个业务分类

- 业务理解：解释本场景的对象、术语、启动原因、结果使用者和错误后果。
- 输入与补证：必需 业务目标与真实证据；建议补充 target_skill_path、target_business_domain、change_request；来源、日期、版本和可信度必须记录。
- 上下游：确认输入 owner、下游消费者、系统事实源、审批人、执行人和交接 SLA。
- 决策：比较维持现状、推荐方案和低风险备选，记录适用条件、反证、成本、风险与可逆性。
- 异常：覆盖缺数据、口径冲突、权限不足、依赖失败、超时、部分成功、人工升级、补偿和回滚。
- 完成：交付 project understanding、architecture guidance、skill package constraints，并附验收证据、责任人、截止、停止条件和复盘时间。

## 场景 3：审查 skill 是否具备真实工作流、证据边界和可判定验收

- 业务理解：解释本场景的对象、术语、启动原因、结果使用者和错误后果。
- 输入与补证：必需 业务目标与真实证据；建议补充 target_skill_path、target_business_domain、change_request；来源、日期、版本和可信度必须记录。
- 上下游：确认输入 owner、下游消费者、系统事实源、审批人、执行人和交接 SLA。
- 决策：比较维持现状、推荐方案和低风险备选，记录适用条件、反证、成本、风险与可逆性。
- 异常：覆盖缺数据、口径冲突、权限不足、依赖失败、超时、部分成功、人工升级、补偿和回滚。
- 完成：交付 project understanding、architecture guidance、skill package constraints，并附验收证据、责任人、截止、停止条件和复盘时间。

## 场景 4：准备把某个 skill 文件夹单独发给其他人或平台

- 业务理解：解释本场景的对象、术语、启动原因、结果使用者和错误后果。
- 输入与补证：必需 业务目标与真实证据；建议补充 target_skill_path、target_business_domain、change_request；来源、日期、版本和可信度必须记录。
- 上下游：确认输入 owner、下游消费者、系统事实源、审批人、执行人和交接 SLA。
- 决策：比较维持现状、推荐方案和低风险备选，记录适用条件、反证、成本、风险与可逆性。
- 异常：覆盖缺数据、口径冲突、权限不足、依赖失败、超时、部分成功、人工升级、补偿和回滚。
- 完成：交付 project understanding、architecture guidance、skill package constraints，并附验收证据、责任人、截止、停止条件和复盘时间。

## 不可突破的边界

业务 skill 不放 .trae；README.md 是中文产品文档和版本记录，但不承担 AI skill 身份；每个业务 skill 必须可整包单独分发；新增或重构 skill 时优先复用标准模板

## 跨场景检查

- 人员：谁提出、谁提供事实、谁决策、谁执行、谁验收、谁承担失败后果。
- 系统：source of truth、状态、版本、权限、写回、幂等、对账、日志和留存。
- 经营：收入、利润、现金、客户、质量、时效、合规和可逆性之间的取舍。
- 学习：领先指标、结果指标、护栏指标、失败样本、下次刷新和 Skill 更新 owner。
