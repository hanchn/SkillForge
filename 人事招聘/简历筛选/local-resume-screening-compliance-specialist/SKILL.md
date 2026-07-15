---
name: local-resume-screening-compliance-specialist
description: 无人值守消费招聘需求阶段生成的 screening-spec.json，批量解析授权简历、按岗位证据形成候选池、诊断筛选漏斗、触发阈值预警，并通过招聘平台 API 自动预约面试、会议室、面试官通知和候选人二次确认；异常统一发送飞书告警。Use for automated resume screening, shortlist generation, low-yield or pipeline anomaly detection, interview scheduling orchestration, and Feishu exception alerts while preserving explainability and an authorized final hiring decision.
---

# 无人值守简历筛选与面试预约

正常路径自动完成简历处理、候选池生成和面试预约；只有筛选、数据、API、候选人确认或合规异常才通知人员介入。

## Load resources

- 在 SkillForge 仓库内先读 `公司上下文/company-profile.yaml` 和 `公司上下文/README.md`。
- 必须读取 `references/compliance-baseline.md`、`references/resume-screening-compliance-method.md`、`references/interview-scheduling-api-contract.md` 和 `references/feishu-alert-contract.md`。
- 使用 JD Skill 生成的 `screening-spec.json`；先运行 `scripts/validate_screening_spec.py`，不得静默重解释已确认标准。
- 先运行 `scripts/inventory_local_resumes.py` 建立只读、默认不落全文的本地清单。
- 筛选后运行 `scripts/evaluate_screening_run.py`，按机器可读阈值输出原因码，供飞书告警消费。
- 使用 `assets/candidate-review-card-template.md` 和 `assets/screening-alert-policy.json`。

## Zero-touch prerequisites

上游是 JD Skill 生成的筛选契约和授权简历来源；下游是招聘平台候选池、面试官日历、会议室、邮件、飞书告警和最终授权决策。自动化决策只推进可逆流程状态，不替代最终录用决定。

以下条件满足时直接运行，不再向发起人或 HR 重复确认：

- `screening-spec.json` 状态为 `READY_FOR_HR`，版本和岗位一致。
- 简历来源、处理用途、保留期限和访问范围已有授权。
- 招聘平台、日历/会议室、邮件和飞书连接器已配置并通过测试环境验证。
- 凭证通过环境变量、密钥管理或授权连接器引用，不出现在 Skill、日志和交付物中。

缺失其中任一项时，继续完成安全可执行的部分，并把受影响阶段标记为 `REVIEW_REQUIRED`；不得假装 API 已调用或消息已送达。

## Data and compliant API intake gate

- 已配置连接器时直接运行。只有连接器缺失或版本不明时，才询问使用者现有数据、招聘平台/日历/会议室/邮件/飞书官方 API、测试环境和授权 owner。
- 登记每个连接器的租户、用途、权限、凭证引用、字段范围、限流、回调、数据地域、保留和删除；不收集明文凭证。
- API 文档或权限无法确认时只生成 dry-run 和 adapter mapping，不猜测端点或执行真实写入。

## Workflow

1. 验证筛选契约的 schema、`request_id`、`rubric_version`、状态、稳定标准 ID、岗位相关理由和阈值。
2. 只读扫描简历目录，跳过符号链接，记录唯一文件、重复、解析器、页数、文本长度、OCR/损坏和受控文本位置。默认清单不包含简历全文。
3. 屏蔽姓名、照片、联系方式、住址、年龄、性别、婚育、民族、宗教和健康等非必要信息；联系方式只在进入预约阶段后由授权连接器单独读取。
4. 先用关键词、同义词、缩写和工具词召回，再依据项目动作、业务结果、时间范围和替代证据判断；关键词出现次数不能单独形成匹配结论。
5. 对每个 `criterion_id` 输出直接证据、`MATCH / PARTIAL / INSUFFICIENT_EVIDENCE / CONFLICT`、置信度和核验问题。
6. 自动形成：
   - `SHORTLIST_READY`：岗位证据达到已确认候选池规则。
   - `REVIEW_REQUIRED`：规则冲突、低置信度或高风险异常。
   - `INSUFFICIENT_EVIDENCE`：简历没有足够证据，不等于永久拒绝。
   - `PROCESSING_EXCEPTION`：解析、OCR或文件异常。
7. 计算筛选漏斗并运行 `scripts/evaluate_screening_run.py`：收到、解析成功、去重、岗位族相关、必须项通过、候选池、面试预约、候选人确认。
8. 若无阻断告警且策略允许，对 `SHORTLIST_READY` 候选人调用招聘平台 API 启动面试预约：读取候选人可选时段、面试官和会议室资源，创建临时占位，发送面试官通知及候选人二次确认邮件，收到确认后固化预约并写回平台。
9. 任一异常转换成标准飞书事件，按严重度、幂等键和路由发送；告警只带 Candidate ID、岗位、阶段、原因码和安全记录链接，不带简历正文或敏感信息。
10. 保存最小审计记录：输入/规则版本、证据引用、状态变化、API 请求幂等键、平台记录 ID、消息回执、重试、补偿和最终授权决定。

## Funnel and alert diagnosis

默认读取 `screening-spec.json` 的岗位级阈值；没有岗位阈值时使用 `assets/screening-alert-policy.json` 的保守默认值。

- `LOW_SHORTLIST_YIELD`：去重且成功解析达到 1000 份而候选池少于 10 人。进一步判断是 JD 硬门槛、渠道、解析、证据词库还是评分阈值问题。
- `PARSE_QUALITY_LOW`：解析成功率低于 95% 或 OCR/损坏比例异常。
- `SOURCE_MISMATCH`：岗位族相关率过低，提示招聘渠道或投放定向问题。
- `CRITERION_OVER_FILTERING`：单个必须项拦截超过 60% 的岗位族相关简历。
- `RUBRIC_DRIFT`：JD、培训文档或筛选版本不一致，或修改后候选率相对基线突变。
- `SCHEDULING_API_FAILURE`、`ROOM_UNAVAILABLE`、`INTERVIEWER_CONFLICT`、`EMAIL_DELIVERY_FAILURE`、`CANDIDATE_CONFIRMATION_TIMEOUT`：面试预约链路异常。
- 阈值是可配置默认值，不得冒充所有岗位的永久标准；按岗位、职级、地区、渠道和历史漏斗校准。

## Interview scheduling transaction

1. 使用 `request_id + candidate_id + interview_stage + proposed_start` 作为幂等键。
2. 先查询招聘平台候选人状态，避免已淘汰、已预约或已关闭候选人重复触达。
3. 获取面试官忙闲、会议室和候选人可选时段；时间统一保存时区。
4. 创建有过期时间的临时会议/会议室占位，写回 `booking_id`、`calendar_event_id`、`room_id`。
5. 通知面试官并向候选人发送二次确认邮件；邮件包含岗位、时间、时区、方式、改期/取消入口和隐私说明。
6. 候选人确认后将状态改为 `INTERVIEW_CONFIRMED`；拒绝、超时或邮件退回时释放占位并触发飞书告警。
7. 部分成功时不得重复创建会议。按平台 ID 对账，优先补发通知；无法确认状态时停止重试并转人工。

## Feishu alerts

- 使用飞书应用或机器人连接器，不保存明文 webhook、token、cookie 或私钥。
- 每个事件必须包含 `event_id`、严重度、岗位/请求 ID、阶段、原因码、影响数量、诊断、建议动作、owner、首次/最近发生时间和安全详情链接。
- 相同 `request_id + reason_code + stage` 在去重窗口内聚合；恢复后发送恢复消息并关闭事件。
- HTTP 成功只代表平台接受请求，不代表已读或问题关闭；记录 `message_id`、回执、认领和升级状态。

## Guardrails

- 不得上传未授权简历、根据敏感属性排序、把缺少关键词写成不具备能力，或把异常定性为造假。
- 自动化可以形成候选池和预约面试，但不得作为永久拒绝或最终录用的唯一依据；保留说明、纠错和授权人工决定能力。
- 未确认真实 API 文档、权限、租户、测试环境和回滚前，只生成适配契约或 dry-run，不执行真实预约和消息发送。

## Output contract

交付候选池、逐标准证据、筛选漏斗、异常归因、预约状态、飞书事件与最小审计记录。正常批次输出 `AUTOMATION_COMPLETED`；存在未恢复异常时输出 `REVIEW_REQUIRED`。
