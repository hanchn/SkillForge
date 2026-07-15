---
name: job-description-generator
description: 在招聘需求创建时自动生成可编辑候选人 JD、HR 精准岗位培训文档、内部岗位说明书和机器可读简历筛选规则，无需发起人与 HR 重复沟通。Use when creating or editing a recruitment request, automatically compiling a request into a recruitment package, synchronizing JD changes to screening criteria, or preparing a zero-handoff package for HR; optionally add current market and compensation research only when requested or required by policy.
---

# 招聘需求与 JD 自动生成

把招聘需求一次编译成 HR 可直接执行、简历筛选 Skill 可直接消费的招聘包。正常路径无人值守；只在关键事实冲突、合规风险或无法安全生成筛选标准时请求人工处理。

## Load resources

- 在 SkillForge 仓库内先读 `公司上下文/company-profile.yaml` 和 `公司上下文/README.md`，只使用已确认事实。
- 必须读取 `references/compliance-baseline.md` 和 `references/hr-role-training-checklist.md`。
- 使用 `assets/delivery-template.md` 生成招聘包，使用 `assets/screening-spec-template.json` 生成机器可读筛选契约。
- 只有使用者明确要求市场/薪酬调研、公司政策强制要求，或关键岗位参数确实依赖当前市场数据时，才读取 `references/job-market-research-method.md` 并使用对应调研模板。
- 存在跨团队取舍、未经批准的待遇信息或不可逆发布动作时，使用 `assets/decision-record-template.md`。

## Automation contract

上游是招聘需求、岗位模板和已确认公司上下文；下游是 HR、简历筛选、面试预约和审计。正常决策由版本化规则自动执行，只有阻断异常才交给对应 owner。

### Minimum request

优先从招聘需求表、组织岗位模板和公司上下文读取：`request_id`、岗位名称、部门、招聘人数、职级、工作地点、用工方式、招聘原因、岗位要解决的问题、主要结果、发起人和目标到岗时间。

- 输入足以形成安全草案时直接生成，不先发起通用问卷或要求 HR/发起人开会。
- 非关键缺失字段写为 `待确认`，继续生成可编辑草案。
- 只有缺失会导致岗位对象无法识别、筛选条件违法/歧视、待遇承诺失真或要求互相冲突时，才标记 `REVIEW_REQUIRED` 并列出最少修正字段。

### Required package

一次生成并保持同一 `request_id`、`package_version` 和 `rubric_version`：

1. 候选人版可编辑 JD。
2. HR 精准岗位培训文档：岗位存在原因、典型工作、上下游、工具术语、职级差异、优秀/不匹配表现和常见误解。
3. 内部岗位说明书：目标、结果、职责、权限、不负责范围、30/60/90 天预期。
4. `screening-spec.json`：筛选标准、关键词与同义词、证据、替代证据、禁用变量、阈值和版本。
5. 未确认项与异常清单；正常情况不得把“再找发起人沟通”作为交接步骤。

## Workflow

1. 读取招聘需求与已确认公司事实，生成 `request_id` 和初始版本；区分事实、发起人修改、默认值与待确认项。
2. 把岗位目标转换成结果、职责和能力，区分 `MUST_HAVE`、`TRAINABLE`、`BONUS`、`PROHIBITED`；每项分配稳定 `criterion_id`。
3. 为每项可筛选标准生成岗位相关理由、原始关键词、中英文同义词、缩写、相关工具、证据动作、结果表达、替代证据、最低证据、反证和面试核验问题。关键词只用于召回，不能单独证明胜任。
4. 同步生成候选人 JD、HR 培训文档、内部岗位说明书和 `screening-spec.json`，确保四者对同一岗位要求没有冲突。
5. 对发起人的修改执行影响分类：
   - `COPY_ONLY`：措辞、语气或公司介绍变化，只更新候选人 JD。
   - `REQUIREMENT_CHANGE`：职责、职级、必须项或工作条件变化，同时更新培训文档、内部说明和筛选规则，并递增 `rubric_version`。
   - `COMPLIANCE_CHANGE`：工作地、用工主体、待遇、敏感或无关条件变化，暂停自动流转并标记 `REVIEW_REQUIRED`。
6. 完成一致性检查。无阻断项时输出 `READY_FOR_HR`，HR 可直接发布、筛选和准备面试；有阻断项时只输出明确字段、原因和修复动作。
7. 市场和薪酬调研按需执行，不得让可选调研阻塞信息完整、已经批准的招聘需求。

## Screening-spec rules

- 每个 `MUST_HAVE` 必须能对应可观察工作证据，不得只使用学校、公司名气、年龄、性别、婚育、民族、宗教、健康、照片、住址等敏感或无关代理变量。
- 必须项数量保持最小；可入职后培养的能力不得升级为自动硬门槛。
- 阈值是岗位级可配置参数。默认预警示例为：去重且成功解析的简历达到 1000 份而候选池少于 10 人时触发低产出预警；不得把该示例冒充所有岗位的统一标准。
- 公开 JD、培训文档和筛选规则必须共享版本；规则发生实质变化后，旧筛选结果必须标记为过期。

## Data and compliant API intake gate

- 正常招聘包生成不需要额外 API 调研。只有按需市场/薪酬调研或写入招聘平台时，才询问使用者现有数据、授权连接器、官方接口和优先来源。
- 不接收或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或授权连接器。
- 当前市场、薪酬、平台规则和法律要求必须记录来源、采集日期与版本；来源不可用时保留未知项，不补造事实。

## Acceptance and recovery

- 验收要求：四份核心产物共享 request ID 和版本，内容一致，状态可判定，下游无需重新解释 JD。
- `COPY_ONLY` 可恢复为上一版公开文案；`REQUIREMENT_CHANGE` 通过旧/new rubric 版本重跑并标记旧结果过期；错误发布或规则冲突时暂停下游、恢复上一已确认版本并记录差异。
- API 或调研部分失败不得破坏已生成招聘包；隔离失败阶段，保留已确认产物和可重试输入。

## Evidence freshness gate

市场、薪酬、平台规则、法律和用工要求属于时效信息，只在本次任务从授权当前来源核验后使用；招聘需求和公司内部事实记录来源版本与确认人。

## States and handoff

- `DRAFT_GENERATED`：已生成可编辑草案，存在非阻断待确认项。
- `READY_FOR_HR`：招聘包完整一致，可零沟通交给 HR 和简历筛选 Skill。
- `REVIEW_REQUIRED`：存在关键冲突、未经批准承诺、违法/歧视风险或无法解释的硬门槛。

## Guardrails

- 不得虚构岗位事实、薪酬福利、编制、远程、签证或组织承诺。
- 不得把关键词出现次数当作能力结论，不得生成与岗位表现无关的筛选标准。
- 自动生成和自动筛选不等于自动录用或永久拒绝；重大用工决定保留可解释记录和授权人工确认。
- 未获授权不得自动发布到外部招聘平台。

## Output contract

交付招聘包、状态、版本、一致性检查结果和最少异常清单。`READY_FOR_HR` 包必须让 HR 无需再次解释岗位，并让简历筛选 Skill 无需重新解读 JD。
