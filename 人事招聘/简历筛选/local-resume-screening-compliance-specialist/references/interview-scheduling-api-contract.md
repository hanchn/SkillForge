# 面试预约 API 契约

## 连接器

分别登记招聘平台、日历、会议室、视频会议和邮件服务的官方 API 文档、环境、租户、owner、认证引用、权限范围、限流、超时和回调验签方式。没有真实接口资料时只生成 adapter mapping，不猜测 URL 或字段。

## 标准操作

| 操作 | 必需输入 | 必需输出 | 幂等/补偿 |
|---|---|---|---|
| 读取候选人状态 | request_id、candidate_id | application_status、contact_ref | 不写入 |
| 查询可用时段 | interviewer_ids、room_policy、timezone、duration | slots | 缓存短时有效 |
| 创建临时占位 | slot、participants、expires_at、idempotency_key | booking_id、event_id、room_id | 可释放 |
| 发送面试官通知 | event_id、interviewer_ids | delivery_ids | 可补发不重建会议 |
| 发送候选人确认邮件 | booking_id、candidate_contact_ref、confirm/cancel links | message_id、delivery_status | 同一 booking 只发一次有效邀请 |
| 确认预约 | booking_id、candidate_response | confirmed status | 重复回调幂等 |
| 释放/改期 | booking_id、reason | cancellation/reschedule ids | 对账所有下游资源 |

## 状态机

`SHORTLIST_READY → SLOT_MATCHED → HOLD_CREATED → AWAITING_CANDIDATE_CONFIRMATION → INTERVIEW_CONFIRMED`

异常进入 `SCHEDULING_EXCEPTION`。候选人拒绝或超时进入 `RESCHEDULE_OR_CLOSE`，释放会议室和日历占位；不得因邮件发送失败重复创建会议。

## 成功判定

只有招聘平台、日历事件、会议室和候选人确认状态能够按平台 ID 对账时，才可写 `INTERVIEW_CONFIRMED`。HTTP 2xx、排队成功或邮件 API 接受请求不等于候选人已确认。
