# 飞书招聘异常告警契约

## 标准事件

```json
{
  "event_id": "stable-idempotent-id",
  "severity": "P1|P2|P3",
  "request_id": "recruitment-request-id",
  "candidate_id": "optional-pseudonymous-id",
  "stage": "SCREENING|SCHEDULING|CONFIRMATION",
  "reason_code": "LOW_SHORTLIST_YIELD",
  "summary": "可执行的一句话摘要",
  "impact_count": 0,
  "diagnosis": [],
  "recommended_actions": [],
  "owner": "role-or-user-ref",
  "first_seen_at": "ISO-8601",
  "last_seen_at": "ISO-8601",
  "secure_detail_url": "authorized-internal-link"
}
```

## 路由与隐私

- P1 发送招聘异常群并 @值班 owner；P2 发送招聘运营群；P3 聚合后发送摘要。真实群、用户和升级链由连接器配置，不硬编码。
- 飞书消息不得包含简历正文、姓名、电话、邮箱、住址、敏感属性、API 凭证或候选人评语全文。
- 相同 `request_id + stage + reason_code` 在去重窗口内更新同一事件；恢复时发送恢复卡片并关闭，不重复轰炸。
- 记录平台 `message_id`、发送状态、认领人、认领时间和关闭时间。未获授权或发送失败时写入待重放队列，不能声称已经通知。

## 卡片最低内容

显示严重度、岗位/需求 ID、异常阶段、影响数量、主要诊断、建议动作、owner、发生时间和受控详情链接。操作按钮可包含“认领”“查看详情”“重新运行”“暂停自动化”，但按钮必须调用已授权后端并校验当前状态。
