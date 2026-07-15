# 飞书、钉钉、企业微信与企业 QQ 适配指南

## 通用边界

- 先区分群 Webhook、自定义机器人、应用机器人/企业应用和贵司内部消息网关；能力、权限、回执和审核不同。
- Webhook URL 与 token 都是秘密，不写入代码、消息、日志、截图或仓库。渲染 payload 与真实发送必须分离。
- HTTP 成功只表示平台接收请求，不表示用户已读、已认领或问题已解决；业务回执另建状态。

## 飞书

自定义机器人适合单向群推送；应用机器人经管理员审核和权限申请后可支持更丰富的会话与交互。卡片、@、外部群和消息大小按执行时官方文档核验。

## 钉钉

区分自定义机器人 Webhook、应用机器人 sessionWebhook 与服务端 API；不同方式的 @、消息类型、发布审核和权限不同。安全设置、签名、限流与错误码必须从当前文档读取。

## 企业微信

区分群机器人 Webhook 与企业自建应用。群机器人适合群内通知；定向个人、通讯录或更复杂交互需要相应企业应用权限。不得把 webhook key 打入日志。

## 企业 QQ

不假设企业 QQ 与企业微信 payload 或鉴权兼容。只有使用者提供现行官方接口文档、已授权第三方连接器或贵司内部消息网关契约后才能实施；否则只输出标准事件和 `REVIEW_REQUIRED` 适配清单。

## 当前官方入口

- [飞书机器人概述](https://open.feishu.cn/document/client-docs/bot-v3/bot-overview?lang=zh-CN)
- [钉钉机器人消息](https://open.dingtalk.com/document/dingstart/robot-reply-and-send-messages)
- [企业微信群机器人](https://developer.work.weixin.qq.com/document/path/91770)
