# 无人值守简历筛选方法

## 输入优先级

以状态为 `READY_FOR_HR` 的 `screening-spec.json` 为唯一筛选事实源。自然语言 JD 只用于展示和一致性校验，不得在每次运行时重新发明标准。没有有效契约时可生成草案，但批次必须标记 `REVIEW_REQUIRED`。

## 召回与证据

- 关键词、中英文同义词、缩写和工具词只扩大召回。
- 胜任证据来自项目动作、责任范围、业务结果、时间范围和可接受替代经验。
- 缺少关键词或未在简历中出现只能写 `INSUFFICIENT_EVIDENCE`。
- 学校、公司名气、姓名、照片、年龄、性别、婚育、民族、宗教、健康、户籍和外貌不得作为能力代理变量。

## 漏斗诊断

每批记录：收到、成功解析、唯一简历、岗位族相关、必须项通过、候选池、发起预约、确认面试。为每个未进入下一层的记录保存标准原因码，才能区分：

- 渠道或投放不准；
- JD/Rubric 过严；
- 单个必须项过度拦截；
- 解析/OCR 问题；
- 词库和替代证据覆盖不足；
- 候选池阈值不合理。

## 自动化边界

系统可自动形成候选池、发起面试预约并处理正常确认。最终录用、永久拒绝和重大争议必须由授权人员决定，并保留说明、纠错和改判记录。

## 原因码

- `PARSE_FAILED`、`OCR_REQUIRED`、`LOW_TEXT_VOLUME`、`DUPLICATE_FILE`、`SYMLINK_SKIPPED`
- `TIMELINE_REVIEW`、`CLAIM_EVIDENCE_GAP`、`JD_CONFLICT`、`STANDARD_BIAS_RISK`
- `LOW_SHORTLIST_YIELD`、`SOURCE_MISMATCH`、`CRITERION_OVER_FILTERING`、`RUBRIC_DRIFT`
- `SCHEDULING_API_FAILURE`、`ROOM_UNAVAILABLE`、`INTERVIEWER_CONFLICT`、`EMAIL_DELIVERY_FAILURE`、`CANDIDATE_CONFIRMATION_TIMEOUT`

原因码只说明需要核验什么，不得写“造假”“欺骗”等定性结论。
