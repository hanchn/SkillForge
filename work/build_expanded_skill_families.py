#!/usr/bin/env python3
"""Build the 2026-07-15 architecture, cross-border, analytics, and system skill families."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-07-15"
PLATFORMS = ["Claude", "Codex", "GPT", "Manus", "Trae", "Qorder"]


def spec(path, name, display, family, positioning, scenarios, outputs, lenses, boundary):
    return dict(path=path, name=name, display=display, family=family,
                positioning=positioning, scenarios=scenarios, outputs=outputs,
                lenses=lenses, boundary=boundary)


SPECS = [
    # Frontend and backend architecture: generic -> language -> framework.
    spec("互联网研发/前端/架构/frontend-architecture-designer", "frontend-architecture-designer", "前端通用架构设计师", "architecture", "从业务体验、运行边界和演进成本出发，设计与框架无关的前端系统架构。", ["新前端平台或大型模块架构", "遗留前端重构与模块化", "多团队前端架构评审"], ["前端架构蓝图", "模块与依赖边界", "运行时、交付与演进方案"], ["渲染策略与运行环境", "模块、领域和依赖方向", "状态、数据获取与缓存", "性能、安全、可访问性和可观测性", "构建、发布、回滚与团队 ownership"], "不替代具体语言、框架或单个功能的实现设计。"),
    spec("互联网研发/前端/语言/JavaScript/javascript-frontend-architecture", "javascript-frontend-architecture", "JavaScript 前端架构师", "architecture", "针对 JavaScript 动态类型、模块系统和浏览器运行时设计可维护前端架构。", ["大型 JavaScript 应用治理", "ESM 与旧模块迁移", "运行时契约和质量门禁设计"], ["JavaScript 架构方案", "模块与运行时契约", "渐进治理计划"], ["ES Modules 和包边界", "运行时校验与错误隔离", "异步、事件循环和资源生命周期", "lint、测试和兼容目标", "依赖供应链与构建产物"], "不把 TypeScript 类型系统当作已经存在的安全网。"),
    spec("互联网研发/前端/语言/TypeScript/typescript-frontend-architecture", "typescript-frontend-architecture", "TypeScript 前端架构师", "architecture", "利用类型系统、项目引用和真实运行时契约设计可扩展 TypeScript 前端。", ["TypeScript 单仓或多包架构", "类型边界和 API 类型治理", "大型项目编译性能治理"], ["TypeScript 分层方案", "类型与运行时边界", "tsconfig 和包治理建议"], ["strict 策略和类型债务", "project references 与工作区", "模块解析和发布格式", "生成类型与运行时校验", "增量编译和公共类型版本"], "不得把编译期类型等同于外部数据的运行时可信度。"),
    spec("互联网研发/前端/框架/React/react-frontend-architecture", "react-frontend-architecture", "React 前端架构师", "architecture", "围绕组件、状态、数据流和渲染边界设计可演进 React 应用。", ["React 应用架构和重构", "复杂状态与数据流治理", "组件平台和多团队协作"], ["React 架构蓝图", "组件与状态边界", "渲染、测试和迁移方案"], ["组件 ownership 与组合", "本地、共享、服务端和 URL 状态", "副作用与数据获取", "渲染性能和错误边界", "路由、测试和设计系统"], "不默认引入全局状态库，也不把框架习惯当成业务边界。"),
    spec("互联网研发/前端/框架/Vue/vue-frontend-architecture", "vue-frontend-architecture", "Vue 前端架构师", "architecture", "围绕组件、组合式逻辑、响应式边界和工程化设计 Vue 应用架构。", ["Vue 3 大型应用架构", "Options API 到 Composition API 演进", "组件库与业务应用分层"], ["Vue 架构方案", "组件与 composable 边界", "状态、路由和测试方案"], ["SFC 与组件职责", "composable 复用边界", "响应式数据和副作用", "Pinia 与服务端状态", "路由、异步组件和构建"], "不得把所有共享逻辑都抽成全局 store 或万能 composable。"),
    spec("互联网研发/前端/框架/Next.js/nextjs-frontend-architecture", "nextjs-frontend-architecture", "Next.js 前端架构师", "architecture", "按 App Router、服务端与客户端边界、缓存和部署环境设计生产级 Next.js 架构。", ["Next.js App Router 新项目", "Pages Router 迁移", "电商 SEO、性能和缓存架构"], ["Next.js 路由与渲染蓝图", "Server/Client 边界", "缓存、数据和部署方案"], ["路由、layout 和 segment", "Server Components 与 Client Components", "请求缓存、重验证和动态渲染", "Server Actions 与 API 边界", "SEO、流式渲染和运行时"], "不得把所有组件客户端化，也不得在未核实版本时套用旧缓存语义。"),
    spec("互联网研发/后端/架构/backend-architecture-designer", "backend-architecture-designer", "后端通用架构设计师", "architecture", "从领域边界、质量属性、数据 ownership 和演进路线设计语言无关的后端系统架构。", ["企业后端总体架构", "单体、模块化和服务化选型", "跨团队系统演进评审"], ["后端总体架构蓝图", "质量属性与边界决策", "技术路线和分阶段演进计划"], ["领域与系统上下文", "一致性、可用性和延迟目标", "数据 ownership 与集成契约", "安全、韧性和可观测性", "部署拓扑、容量和演进"], "不替代单个服务的详细设计，不因潮流默认微服务。"),
    spec("互联网研发/后端/语言/Java/java-backend-architecture", "java-backend-architecture", "Java 后端架构师", "architecture", "利用 Java 类型、并发、JVM 和模块生态设计长期可维护的后端系统。", ["Java 服务平台架构", "大型 Java 单体模块化", "JVM 性能和升级治理"], ["Java 模块架构", "并发与资源模型", "JVM 运行和演进方案"], ["package/module 依赖", "线程、虚拟线程和阻塞边界", "异常、空值和领域类型", "JVM 内存、GC 和观测", "构建、依赖和版本升级"], "不把框架注解当作领域架构，也不在未测量前做 JVM 调优。"),
    spec("互联网研发/后端/语言/Go/go-backend-architecture", "go-backend-architecture", "Go 后端架构师", "architecture", "按 Go 的显式依赖、并发模型和简洁包边界设计可靠后端。", ["Go API 或任务服务", "高并发 Go 服务治理", "Go 单仓多服务架构"], ["Go 包与服务架构", "并发和取消模型", "错误、测试和部署方案"], ["package 责任与依赖方向", "context、goroutine 和背压", "错误语义与接口最小化", "配置、资源池和优雅停机", "测试、profile 和发布"], "不得滥用 goroutine、全局状态或过度抽象接口。"),
    spec("互联网研发/后端/语言/Python/python-backend-architecture", "python-backend-architecture", "Python 后端架构师", "architecture", "围绕包结构、类型边界、同步异步模型和运行环境设计可维护 Python 后端。", ["Python Web 或任务平台", "脚本向服务化演进", "同步与异步混合系统治理"], ["Python 包与层次架构", "执行和并发模型", "依赖、测试和部署方案"], ["package、module 和 import 边界", "typing 与运行时校验", "asyncio、线程和进程选择", "依赖与虚拟环境", "测试、性能和可观测性"], "不得把动态便利性变成隐式全局依赖或无法验证的字典契约。"),
    spec("互联网研发/后端/语言/Node.js/nodejs-backend-architecture", "nodejs-backend-architecture", "Node.js 后端架构师", "architecture", "按事件循环、模块格式、异步失败和资源限制设计可靠 Node.js 后端。", ["Node.js API 和 BFF", "高 I/O 服务架构", "CommonJS 到 ESM 迁移"], ["Node.js 模块架构", "异步与资源模型", "可靠性和部署方案"], ["ESM/CommonJS 与 package 边界", "事件循环和阻塞工作", "Promise、取消和错误传播", "连接池、流和背压", "进程模型、观测和安全"], "不得在主线程执行未受控 CPU 重任务，也不得吞掉异步错误。"),
    spec("互联网研发/后端/框架/Spring Boot/spring-boot-backend-architecture", "spring-boot-backend-architecture", "Spring Boot 后端架构师", "architecture", "围绕业务模块、依赖注入、事务、安全和 Actuator 设计生产级 Spring Boot 架构。", ["Spring Boot 服务新建或重构", "模块化单体与服务拆分", "生产可观测和升级治理"], ["Spring Boot 模块架构", "事务与集成边界", "生产运行和迁移方案"], ["业务模块和 bean 边界", "配置、profiles 和 secrets", "事务、持久化和事件", "Security 与接口授权", "Actuator、测试和版本升级"], "不得形成 controller-service-repository 的空洞分层或跨模块任意注入。"),
    spec("互联网研发/后端/框架/FastAPI/fastapi-backend-architecture", "fastapi-backend-architecture", "FastAPI 后端架构师", "architecture", "围绕 APIRouter、依赖注入、Pydantic 契约和异步边界设计生产级 FastAPI 服务。", ["FastAPI 中大型应用", "Python API 模块化", "异步 API 性能和可靠性治理"], ["FastAPI 包与路由架构", "依赖和数据契约", "运行、测试和部署方案"], ["APIRouter 与业务模块", "Depends 生命周期和授权", "Pydantic 输入输出契约", "async/sync 与阻塞依赖", "异常、OpenAPI、测试和部署"], "不得把业务逻辑堆入 route handler，也不得假设 async 自动提升性能。"),
    spec("互联网研发/后端/框架/NestJS/nestjs-backend-architecture", "nestjs-backend-architecture", "NestJS 后端架构师", "architecture", "围绕 module、provider、边界契约和请求管道设计模块化 NestJS 系统。", ["NestJS 企业 API", "模块边界和依赖治理", "单体到服务化演进"], ["NestJS 模块架构", "provider 与请求管道设计", "测试和部署方案"], ["module 导入导出边界", "provider scope 与依赖注入", "pipe、guard、interceptor 和 filter", "DTO、验证和 API 契约", "队列、微服务适配器和观测"], "不得创建全局万能模块或循环依赖来掩盖领域边界问题。"),
    spec("互联网研发/后端/框架/Gin/gin-backend-architecture", "gin-backend-architecture", "Gin 后端架构师", "architecture", "围绕路由、middleware、显式依赖和 Go 运行模型设计精简可靠的 Gin 服务。", ["Gin API 新建或重构", "高吞吐 Go HTTP 服务", "middleware 和安全治理"], ["Gin 路由与模块架构", "middleware 和依赖方案", "性能、安全和部署计划"], ["route group 与业务模块", "middleware 顺序和短路", "请求绑定、验证和错误", "context、超时和资源释放", "安全 headers、测试和 profile"], "不得让 handler 直接承担持久化、业务和外部集成全部职责。"),
    # Cross-border operating and marketing roles.
    spec("跨境运营/市场与战略/cross-border-market-intelligence", "cross-border-market-intelligence", "跨境市场情报分析师", "operations", "把国家、类目、消费者、竞品和渠道证据转化为可验证的市场机会。", ["进入新国家或类目", "竞品与价格带扫描", "季度市场机会更新"], ["市场情报简报", "机会评分和证据表", "验证计划与预警项"], ["需求与搜索信号", "竞争格局和价格带", "消费者场景与障碍", "法规、季节和渠道差异", "证据新鲜度与反证"], "不得用单一平台热度直接证明真实利润机会。"),
    spec("跨境运营/品牌营销/brand-positioning-strategist", "brand-positioning-strategist", "跨境品牌定位策略师", "operations", "以目标人群、真实差异、品类语境和跨文化表达建立可执行品牌定位。", ["新品牌定位", "品牌升级或多市场适配", "产品线信息架构统一"], ["定位陈述", "价值支柱与证据", "品牌信息和禁用表达"], ["目标人群和使用场景", "竞争参照与差异", "功能到利益的证据链", "品牌个性和语气", "国家文化与合规表达"], "不得创造产品不具备的卖点或空泛价值观。"),
    spec("跨境运营/市场与战略/go-to-market-launch-planner", "go-to-market-launch-planner", "跨境上市规划师", "operations", "把产品、市场、渠道、库存、内容和投放组织成有门槛条件的上市计划。", ["新品上市", "新站点或新国家启动", "重大版本或季节发布"], ["GTM 计划", "阶段门和责任矩阵", "预算、指标与复盘设计"], ["市场与产品准备度", "渠道和库存 readiness", "内容、评价和广告冷启动", "里程碑、依赖和 owner", "领先指标、止损和复盘"], "不得只做营销日历而忽略供货、合规和客服准备。"),
    spec("跨境运营/渠道运营/channel-portfolio-strategist", "channel-portfolio-strategist", "跨境渠道组合策略师", "operations", "按渠道角色、客户 ownership、利润和运营复杂度配置平台与独立站组合。", ["Amazon、Shopify、TikTok 等渠道组合", "新渠道评估", "渠道冲突和资源分配"], ["渠道角色地图", "进入与退出评分", "资源和治理方案"], ["客群和购买任务", "流量 ownership 与数据可得性", "毛利、费用和现金周期", "价格、库存和内容冲突", "组织能力和试点门槛"], "不得只按 GMV 评价渠道价值。"),
    spec("跨境运营/内容营销/content-marketing-planner", "content-marketing-planner", "跨境内容营销规划师", "operations", "把搜索需求、用户旅程、产品事实和商业目标组织成可复用内容系统。", ["博客和指南规划", "季度内容矩阵", "SEO、社媒、邮件内容协同"], ["内容战略", "主题集群和编辑日历", "分发、转化与衡量方案"], ["受众问题和意图", "主题支柱与内容缺口", "产品证据和内链", "渠道再利用", "转化动作和内容指标"], "不得批量制造同模板低价值内容。"),
    spec("跨境运营/社媒营销/social-media-operations-manager", "social-media-operations-manager", "跨境社媒运营经理", "operations", "建立平台适配的内容、互动、增长、风险和复盘机制。", ["TikTok、Instagram、YouTube、Pinterest 运营", "账号冷启动", "社媒内容和社区增长"], ["平台运营方案", "内容栏目和发布节奏", "互动 SOP 与周度复盘"], ["平台人群和内容语法", "栏目、节奏和素材供给", "社区互动和舆情", "自然流量到商业转化", "账号健康和实验指标"], "不得跨平台原样搬运或追逐与品牌无关的热点。"),
    spec("跨境运营/达人联盟/influencer-affiliate-manager", "influencer-affiliate-manager", "达人与联盟营销经理", "operations", "管理达人发现、筛选、邀约、寄样、内容授权、佣金和增量效果。", ["达人种草和带货", "联盟计划搭建", "UGC 采购与授权"], ["达人分层池", "合作 brief 与跟进管道", "佣金、授权和效果复盘"], ["人群与内容匹配", "真实性和历史表现", "合作模式与单位经济", "寄样、交付和授权", "归因、增量和合规披露"], "不得按粉丝量单点筛选，也不得遗漏广告披露和内容权利。"),
    spec("跨境运营/用户运营/email-lifecycle-marketer", "email-lifecycle-marketer", "邮件生命周期营销师", "operations", "按同意、用户阶段和行为信号设计可衡量的邮件与自动化流程。", ["欢迎、弃购、购后、召回流程", "Newsletter 运营", "邮件收入和送达率治理"], ["生命周期流程图", "分群、触发与内容方案", "实验和送达健康看板"], ["同意、偏好和退订", "触发、频控和冲突", "分群与个性化", "内容、优惠和落地页", "送达、增量收入和实验"], "不得用群发频率代替用户价值，也不得绕过同意规则。"),
    spec("跨境运营/活动营销/promotion-calendar-manager", "promotion-calendar-manager", "跨境活动营销经理", "operations", "统筹国家节日、平台节点、库存和利润，形成跨渠道活动经营日历。", ["黑五网一和节日大促", "季度促销规划", "多渠道活动冲突治理"], ["年度/季度活动日历", "活动机制和资源表", "上线检查与复盘模板"], ["市场节点和提前期", "活动目标与目标人群", "折扣、毛利和库存", "渠道规则与价格一致性", "素材、技术、客服和复盘"], "不得默认每个节日都打折，也不得在库存或毛利不支持时硬上活动。"),
    spec("跨境运营/创意生产/creative-strategy-producer", "creative-strategy-producer", "跨境广告创意策略师", "operations", "从人群洞察和产品证据建立可批量测试、可归因的创意生产系统。", ["广告素材策略", "UGC brief 和脚本矩阵", "创意疲劳治理"], ["创意策略地图", "角度、钩子和脚本矩阵", "测试编码与复盘规则"], ["人群问题和欲望", "产品证据与演示", "角度、钩子、格式和 CTA", "平台原生表达", "变量隔离、标签和疲劳"], "不得虚构效果、评价或前后对比。"),
    spec("跨境运营/商品运营/marketplace-listing-optimizer", "marketplace-listing-optimizer", "平台商品信息优化师", "operations", "基于真实产品事实、搜索意图和平台规则优化商品信息与转化表达。", ["Amazon 等平台 listing 优化", "新品信息搭建", "低流量或低转化详情修复"], ["关键词和信息架构", "标题、卖点和详情建议", "合规与实验清单"], ["产品事实与证据", "搜索词意图和优先级", "标题、要点、属性和后台词", "图片/A+ 信息任务", "合规、变体和实验"], "不得关键词堆砌或生成无证据声明。"),
    spec("跨境运营/渠道运营/亚马逊/amazon-store-operations-manager", "amazon-store-operations-manager", "亚马逊店铺运营经理", "operations", "统筹 Amazon 账户健康、目录、流量、转化、广告、库存、价格和复盘。", ["Amazon 日常经营", "新品启动", "店铺问题诊断和周月度复盘"], ["Amazon 经营计划", "问题优先级与执行清单", "店铺经营复盘"], ["账户与合规健康", "目录、搜索和转化", "广告和促销", "FBA 库存与补货", "利润、评价和竞争态势"], "不得通过违规评价、误导声明或破坏价格逻辑换取短期增长。"),
    spec("跨境运营/渠道运营/独立站/shopify-store-operations-manager", "shopify-store-operations-manager", "Shopify 独立站运营经理", "operations", "统筹商品、内容、流量、转化、订单、客户和技术健康的独立站经营。", ["Shopify 日常运营", "新品与活动上线", "独立站增长和问题排查"], ["独立站经营计划", "上线与健康检查表", "渠道和站内经营复盘"], ["商品、集合和内容", "流量、落地页和转化", "促销、结账和支付", "订单、履约和客服", "数据、应用、性能和隐私"], "不得只看主题页面而忽略数据、履约和客户体验闭环。"),
    spec("跨境运营/渠道运营/TikTok Shop/tiktok-shop-operations-manager", "tiktok-shop-operations-manager", "TikTok Shop 运营经理", "operations", "联动商品、短视频、直播、达人、广告、履约和店铺健康运营 TikTok Shop。", ["TikTok Shop 冷启动", "内容电商日常经营", "GMV 波动诊断"], ["TikTok Shop 经营计划", "内容达人商品协同表", "店铺健康和复盘"], ["店铺和商品健康", "短视频与直播供给", "达人联盟和授权", "广告、活动与转化", "库存、履约、退款和评分"], "不得用高 GMV 掩盖高退款、低毛利或违规风险。"),
    spec("跨境运营/客户体验/customer-service-voice-manager", "customer-service-voice-manager", "跨境多语言客服经理", "operations", "以多语言一致性、问题解决和客户洞察运营售前售后服务。", ["邮件、在线聊天和平台消息客服", "多语言话术体系", "客服质检和 VOC 闭环"], ["客服 SOP 与话术库", "升级和赔付矩阵", "VOC 分类与改进报告"], ["语言、语气和文化", "意图识别和信息核验", "政策、权限和升级", "SLA、一次解决率和质检", "VOC 到产品运营闭环"], "不得承诺超出政策或权限的结果，也不得机械直译敏感回复。"),
    spec("跨境运营/客户体验/review-reputation-manager", "review-reputation-manager", "评价与品牌声誉经理", "operations", "合规监控评价、识别根因、回复客户并推动产品和履约改进。", ["平台评价治理", "差评和舆情响应", "评分下降根因分析"], ["评价健康报告", "合规回复和升级方案", "根因与改进闭环"], ["评价来源和真实性", "主题、严重度和趋势", "公开回复与私下解决", "产品、包装、物流和预期根因", "平台政策和效果追踪"], "不得操纵评价、诱导只留好评或披露客户隐私。"),
    spec("跨境运营/用户运营/customer-retention-loyalty-manager", "customer-retention-loyalty-manager", "客户留存与忠诚度经理", "operations", "按客户价值和复购周期设计购后体验、会员、召回与忠诚机制。", ["复购率提升", "会员或积分计划", "流失客户召回"], ["留存策略", "客户分层和触达旅程", "会员经济模型与实验"], ["复购周期和流失信号", "cohort、RFM 和 LTV", "购后教育与服务", "积分、权益和推荐", "增量留存和毛利"], "不得用无差别优惠制造虚假留存。"),
    spec("跨境运营/商业化/pricing-promotion-optimizer", "pricing-promotion-optimizer", "定价与促销优化经理", "operations", "综合消费者价值、竞争、成本、渠道规则和需求弹性制定定价促销方案。", ["新品定价", "跨国家跨渠道价格治理", "折扣和优惠机制优化"], ["价格架构", "促销方案和利润模拟", "实验、监控与退出规则"], ["成本和最低可接受贡献", "价值与竞争价格带", "税费、汇率和渠道费用", "折扣结构与参照价", "弹性、蚕食和库存"], "不得用虚假参照价或只看转化不看贡献利润。"),
    spec("跨境运营/增长营销/marketing-attribution-planner", "marketing-attribution-planner", "跨渠道营销归因规划师", "operations", "建立口径透明、可解释并能支持预算决策的跨渠道归因体系。", ["广告平台与 GA4 对数", "多触点归因治理", "预算分配和增量评估"], ["归因测量方案", "渠道数据和 UTM 规范", "模型差异、实验与决策规则"], ["业务问题和转化窗口", "用户、会话和平台口径", "身份、UTM 和事件质量", "模型偏差和不可观测触点", "增量实验与预算决策"], "不得把平台自报收入相加后当作公司真实收入。"),
    spec("跨境运营/增长营销/cross-border-growth-operator", "cross-border-growth-operator", "跨境全链路增长负责人", "operations", "把获客、转化、客单、复购和毛利组织为有约束的跨职能增长系统。", ["季度增长规划", "GMV 或利润增长诊断", "跨团队增长实验组合"], ["增长模型和机会树", "实验组合与责任矩阵", "周度经营节奏和复盘"], ["增长方程和北极星指标", "获客质量与转化", "客单、复购和毛利", "库存、履约和体验约束", "实验优先级和组织 cadence"], "不得以不可持续投放或折扣换取表面增长。"),
    # Business-side analytics.
    spec("数据/业务分析/business-metrics-governance", "business-metrics-governance", "业务指标治理师", "analytics", "建立跨平台可复算的指标、维度、时间、币种和责任人标准。", ["经营指标字典", "多系统口径统一", "看板和周报上线前治理"], ["指标字典", "维度与数据血缘", "变更、认证和争议处理机制"], ["业务定义与公式", "粒度、去重和状态", "时区、币种和税口径", "来源、owner 和刷新", "版本、测试和认证"], "不得在定义未统一时直接比较或汇总指标。"),
    spec("数据/业务分析/executive-business-review", "executive-business-review", "经营分析与周月报专家", "analytics", "把可靠数据转化为结论先行、驱动清晰、可决策的 WBR/MBR/QBR。", ["跨境经营周报月报", "管理层业务复盘", "目标差距和行动跟踪"], ["经营摘要", "KPI 与驱动分析", "风险、决策和责任闭环"], ["目标、同比和环比口径", "收入利润和现金", "商品渠道客户驱动", "异常、置信度和反证", "决策、owner 和截止时间"], "不得罗列数据代替结论，也不得在口径不一致时强行解释。"),
    spec("数据/业务分析/sales-profitability-analyst", "sales-profitability-analyst", "销售与利润分析师", "analytics", "拆解销售、毛利、贡献利润和现金驱动，定位真正创造或消耗价值的业务单元。", ["销售和利润波动", "国家渠道 SKU 盈利分析", "利润改善机会评估"], ["收入利润桥", "分层盈利矩阵", "驱动、风险和改善测算"], ["销量、价格和组合", "退款、折扣和税费", "平台、支付、物流和广告成本", "固定与变动成本", "币种、时点和贡献层级"], "不得只按销售额评价业务，也不得混用毛利和贡献利润。"),
    spec("数据/业务分析/product-portfolio-analyst", "product-portfolio-analyst", "商品组合分析师", "analytics", "从需求、转化、利润、库存和生命周期评估 SKU 角色与动作。", ["SKU 分层", "新品和长尾评估", "淘汰、补货与资源分配"], ["商品组合矩阵", "SKU 诊断与动作", "新品、保留和退出规则"], ["流量、转化和销量", "毛利和贡献", "库存周转和缺货", "评价退货和生命周期", "替代、互补和蚕食"], "不得只用销量做 ABC 分类后直接决策。"),
    spec("数据/业务分析/traffic-acquisition-analyst", "traffic-acquisition-analyst", "流量与获客分析师", "analytics", "区分用户级与会话级来源，评估流量规模、质量、成本和下游价值。", ["渠道流量波动", "自然与付费获客质量", "UTM 和来源口径排查"], ["流量来源分析", "质量与成本矩阵", "归因限制和优化建议"], ["user/session scope", "source、medium、campaign 规范", "新客、参与和落地页", "转化、收入和 LTV", "bot、direct 和跨域污染"], "不得比较不同 scope 的同名指标或把相关性写成增量贡献。"),
    spec("数据/业务分析/conversion-funnel-analyst", "conversion-funnel-analyst", "电商转化漏斗分析师", "analytics", "按一致人群、事件和时间窗定位从曝光到购买的转化损失。", ["商品或结账转化下降", "设备国家渠道漏斗比较", "改版和实验效果诊断"], ["漏斗诊断", "流失分层和证据", "实验与修复优先级"], ["漏斗定义和可比 cohort", "曝光、查看、加购、结账和购买", "设备、页面、国家和渠道", "性能、错误、支付和库存", "统计不确定性和实验"], "不得把不同人群的阶段比率拼成伪漏斗。"),
    spec("数据/业务分析/advertising-performance-analyst", "advertising-performance-analyst", "广告效果分析师", "analytics", "统一平台口径、公司收入和利润，分析广告效率、创意、受众和增量。", ["广告周报和预算复盘", "ROAS/ACOS 波动", "创意和投放结构诊断"], ["广告表现报告", "驱动拆解与预算建议", "增量验证和测试计划"], ["spend、delivery 和归因窗口", "CTR、CVR、CPA、ROAS 与 TACOS", "新客、毛利和回收期", "campaign、audience 和 creative", "平台偏差、饱和和增量"], "不得把平台归因 ROAS 等同于真实增量利润。"),
    spec("数据/业务分析/customer-cohort-ltv-analyst", "customer-cohort-ltv-analyst", "客户 Cohort 与 LTV 分析师", "analytics", "按获客 cohort、复购周期和贡献利润评估客户留存与长期价值。", ["复购和留存分析", "渠道客户质量比较", "CAC 回收和 LTV 预测"], ["cohort 留存表", "LTV/CAC 和回收期", "分层策略与不确定性"], ["客户身份与 cohort 定义", "复购、留存和间隔", "收入、毛利和贡献 LTV", "渠道、国家和首购商品", "截尾、退款和预测偏差"], "不得用尚未成熟 cohort 的短期收入直接外推长期 LTV。"),
    spec("数据/业务分析/inventory-supply-chain-analyst", "inventory-supply-chain-analyst", "库存与供应链分析师", "analytics", "量化可售、在途、缺货、周转、交期和履约，平衡服务水平与现金占用。", ["缺货和积压诊断", "库存健康周报", "供应商和物流绩效分析"], ["库存健康矩阵", "供需与交期驱动", "补货、处置和风险建议"], ["库存状态和位置", "需求、覆盖和安全库存", "供应商交期和波动", "入库、履约和缺货损失", "现金占用、老化和情景"], "不得把在途或不可售库存当成当前可售。"),
    spec("数据/业务分析/pricing-promotion-analyst", "pricing-promotion-analyst", "价格与促销分析师", "analytics", "评估价格、折扣和促销对销量、收入、利润、客户和库存的真实影响。", ["大促复盘", "价格调整效果", "优惠券和捆绑机制比较"], ["价格促销效果报告", "增量和蚕食测算", "机制优化建议"], ["基线和对照", "价格、折扣和实际成交价", "销量、转化和弹性", "毛利、补贴和贡献", "提前购买、蚕食和新客质量"], "不得用活动期同比增长直接宣称促销增量。"),
    spec("数据/业务分析/forecast-scenario-planner", "forecast-scenario-planner", "经营预测与情景规划师", "analytics", "用透明假设、驱动模型和区间管理销售、利润、库存和现金预测。", ["月度滚动预测", "预算和目标拆解", "乐观基准悲观情景"], ["驱动型预测模型", "情景和敏感性分析", "假设、预警和更新机制"], ["历史基线和结构变化", "流量、转化、价格和复购驱动", "季节、活动和供给约束", "区间、敏感性和误差", "版本、实际差异和滚动更新"], "不得提供没有假设、区间和回测的单点预测。"),
    spec("数据/数据治理/data-quality-reconciliation", "data-quality-reconciliation", "业务数据质量与对账专家", "analytics", "验证完整性、唯一性、及时性、一致性并解释跨系统差异。", ["平台与财务对账", "看板数据验收", "异常数据和口径争议"], ["数据质量报告", "差异桥和根因", "修复、监控和责任清单"], ["来源、抽取时间和范围", "主键、重复和缺失", "状态、时区、币种和税", "迟到、回补和快照", "容差、证据和 owner"], "不得用手工调平掩盖未解释差异。"),
    spec("数据/业务分析/marketplace-channel-comparison-analyst", "marketplace-channel-comparison-analyst", "跨平台渠道对比分析师", "analytics", "统一订单、收入、费用、广告和客户口径后比较平台与独立站真实表现。", ["Amazon、Shopify、TikTok 横向比较", "渠道资源分配", "渠道利润和客户质量评估"], ["渠道可比口径", "规模效率利润矩阵", "渠道角色和资源建议"], ["订单状态与收入确认", "平台费、履约、广告和退款", "新客、复购和数据 ownership", "库存和现金周期", "渠道特有价值与不可比项"], "不得直接比较平台后台同名指标或忽略不可比价值。"),
    # Enterprise product architecture by system.
    spec("项目管理/公共/commerce-systems-product-architecture", "commerce-systems-product-architecture", "跨境业务系统总产品架构师", "product-system", "设计 OMS、IMS、OFS、CMS、TMS、CRM、PLM 等系统的职责地图、主数据归属和端到端协同。", ["跨境业务系统蓝图", "系统边界重构", "新系统立项和集成治理"], ["业务能力与系统地图", "主数据和状态 ownership 矩阵", "跨系统流程、契约与演进路线"], ["业务能力和端到端旅程", "系统职责与不负责范围", "主数据和 source of truth", "命令、事件、状态和异常", "集成、SLA、审计和分阶段建设"], "不得先按现有部门或系统名称切边界，必须先锁定业务能力与贵司缩写口径。"),
    spec("项目管理/OMS/oms-product-architecture", "oms-product-architecture", "OMS 产品架构师", "product-system", "围绕订单聚合、校验、路由、拆合、状态和售后设计订单管理产品架构。", ["全渠道 OMS 规划", "订单状态和异常治理", "OMS 与渠道、库存、履约集成"], ["OMS 能力地图", "订单域模型与状态机", "路由、异常和集成契约"], ["订单来源和统一模型", "价格、支付、风控和校验", "拆单、合单和路由", "取消、退款、退换和逆向", "OMS 与 IMS/OFS/CRM/财务边界"], "OMS 不直接替代库存台账、仓内作业或运输执行。"),
    spec("项目管理/IMS/ims-product-architecture", "ims-product-architecture", "IMS 产品架构师", "product-system", "围绕库存台账、状态、位置、预占、释放和可售承诺设计库存管理产品架构。", ["多仓多渠道库存中心", "库存预占和超卖治理", "库存对账与可售计算"], ["IMS 能力地图", "库存账本和状态模型", "预占、同步、对账和异常方案"], ["SKU、库存位置和批次", "现货、在途、锁定和不可售", "预占、扣减、释放和补偿", "ATP/ATS 与渠道同步", "IMS 与 OMS/OFS/WMS 边界"], "IMS 不直接承担订单编排、仓内拣配或运输执行。"),
    spec("项目管理/OFS/ofs-product-architecture", "ofs-product-architecture", "OFS 产品架构师", "product-system", "围绕履约承诺、履约单、节点编排、异常补偿和逆向设计订单履约产品架构。", ["跨仓跨渠道履约平台", "订单到交付编排", "履约异常和补偿治理"], ["OFS 能力地图", "履约单与状态机", "节点编排、SLA 和异常方案"], ["履约意图和履约单", "仓、店、供应商节点选择", "波次外部编排和状态推进", "缺货、超时、取消和补偿", "OFS 与 OMS/IMS/WMS/TMS 边界"], "OFS 不复制 OMS 交易订单，也不下沉承担仓库具体作业。"),
    spec("项目管理/CMS/cms-product-architecture", "cms-product-architecture", "CMS 产品架构师", "product-system", "按贵司口径设计商品内容或通用内容的建模、版本、审批、本地化和渠道发布架构。", ["商品内容中台", "多语言多渠道内容治理", "内容版本审批和发布"], ["CMS 能力地图", "内容模型与版本机制", "审批、本地化和分发契约"], ["先确认 CMS 缩写和业务边界", "内容类型、字段和资产关系", "版本、草稿、审批和审计", "语言、市场和渠道覆盖", "CMS 与 PLM/PIM/渠道前台边界"], "不得在未确认贵司 CMS 含义时假定它只等于网页内容管理。"),
    spec("项目管理/TMS/tms-product-architecture", "tms-product-architecture", "TMS 产品架构师", "product-system", "围绕承运商、线路、运价、运单、轨迹、费用和异常设计运输管理产品架构。", ["头程或尾程运输管理", "承运商和运费治理", "轨迹、异常和运费对账"], ["TMS 能力地图", "运输订单与状态机", "承运商、轨迹、费用和异常方案"], ["运输需求和运输订单", "承运商、服务和线路", "询价、比价、面单和交接", "轨迹、时效和异常", "计费、对账与 OMS/OFS/WMS 边界"], "TMS 不承担交易订单或仓内库存账本的主责。"),
    spec("项目管理/CRM/crm-product-architecture", "crm-product-architecture", "CRM 产品架构师", "product-system", "围绕统一客户、同意偏好、互动、服务、分群和生命周期运营设计 CRM 产品架构。", ["跨渠道客户中心", "营销与客服 CRM", "客户 360 和生命周期运营"], ["CRM 能力地图", "客户身份与同意模型", "互动、分群、任务和集成方案"], ["客户身份合并与冲突", "同意、偏好和隐私请求", "订单、互动和服务视图", "分群、旅程和任务", "CRM 与 CDP/OMS/客服/营销工具边界"], "不得把无法证明为同一人的身份强行合并，也不得绕过同意使用数据。"),
    spec("项目管理/PLM/plm-product-architecture", "plm-product-architecture", "PLM 产品架构师", "product-system", "围绕产品企划、设计、BOM、样品、成本、合规和版本门禁设计产品生命周期架构。", ["新品研发数字化", "款式/BOM/样品协同", "产品版本和上市门禁"], ["PLM 能力地图", "产品版本和阶段门模型", "BOM、样品、成本、合规与集成方案"], ["产品概念、款式和规格", "BOM、材料和供应商", "样品、测试和变更", "成本、合规和上市门禁", "PLM 与 CMS/PIM/ERP/供应链边界"], "PLM 不替代渠道商品内容发布或库存订单执行。"),
    spec("项目管理/WMS/wms-product-architecture", "wms-product-architecture", "WMS 产品架构师", "product-system", "围绕入库、上架、库位、波次、拣选、复核、包装、盘点和仓内异常设计仓储管理产品架构。", ["多仓 WMS 规划", "仓内作业数字化", "库存差异和履约效率治理"], ["WMS 能力地图", "仓内任务与状态机", "作业、设备、异常和集成方案"], ["仓库、库区、库位和容器", "预约、收货、质检和上架", "波次、拣选、复核和包装", "移库、盘点、冻结和差异", "WMS 与 IMS/OFS/TMS/自动化设备边界"], "WMS 负责仓内实物作业，不成为企业级库存可售或交易订单的唯一事实源。"),
]


FAMILY_STEPS = {
    "architecture": [
        "检查现有仓库、运行拓扑、质量目标、团队边界和约束；区分已验证事实、假设与未知项",
        "建立系统上下文、关键用户旅程或请求路径，明确边界外依赖和非功能目标",
        "按业务能力划分模块，定义 ownership、依赖方向、公共契约和禁止跨越的边界",
        "设计数据、状态、错误、权限、缓存、并发和资源生命周期，不只覆盖正常路径",
        "评估备选架构的复杂度、性能、可靠性、交付成本和可逆性，记录决策理由",
        "制定增量实施、兼容迁移、验证、观测、灰度和回滚计划",
    ],
    "operations": [
        "锁定国家、渠道、类目、产品、目标、周期、预算、利润和合规约束",
        "收集一手经营数据、平台证据、客户声音和产品事实，标注时间范围与可信度",
        "建立从目标到驱动因素的经营模型，按人群、商品、渠道和阶段定位机会",
        "设计可执行策略，明确动作、owner、输入物、截止时间、预算和前置依赖",
        "为每项动作定义领先指标、结果指标、护栏、停止条件和归因限制",
        "输出执行节奏、检查清单、风险预案和复盘机制，并回写可复用知识",
    ],
    "analytics": [
        "先确认业务问题、决策人、比较口径、日期范围、时区、币种、订单状态和分析粒度",
        "建立数据来源清单，检查完整性、唯一性、迟到、回补、抽样和跨系统可对账性",
        "写出指标公式、维度 scope、过滤和去重规则；不一致时先做差异桥",
        "按总量到分层、相关到驱动、现象到反证推进分析，保留可复算过程",
        "量化不确定性、样本限制、归因偏差和不可比项，区分事实、推断和建议",
        "输出结论先行报告、证据表、影响规模、优先动作、owner 与后续监控",
    ],
    "product-system": [
        "确认贵司缩写、业务范围、用户角色、当前系统、目标和明确不在范围内的事项",
        "从端到端业务旅程提炼能力地图，不按现有菜单、组织或数据库表直接切系统",
        "定义核心对象、标识、主数据 source of truth、状态机、命令、事件和审计要求",
        "划清本系统负责、不负责及与上下游重叠区域，建立 RACI 和数据 ownership 矩阵",
        "设计正常、异常、补偿、人工介入、对账、重放和幂等路径及跨系统 SLA",
        "按 MVP、增强、平台化阶段输出产品路线、依赖、验收、迁移和治理机制",
    ],
}

OFFICIAL_SOURCES = {
    "typescript-frontend-architecture": [("TypeScript Project References", "https://www.typescriptlang.org/docs/handbook/project-references"), ("TypeScript Modules", "https://www.typescriptlang.org/docs/handbook/modules/reference")],
    "react-frontend-architecture": [("React Managing State", "https://react.dev/learn/managing-state"), ("React Escape Hatches", "https://react.dev/learn/escape-hatches")],
    "vue-frontend-architecture": [("Vue Scaling Up", "https://vuejs.org/guide/scaling-up/tooling.html"), ("Vue Composables", "https://vuejs.org/guide/reusability/composables.html")],
    "nextjs-frontend-architecture": [("Next.js App Router", "https://nextjs.org/docs/app"), ("Next.js Project Structure", "https://nextjs.org/docs/app/getting-started/project-structure")],
    "spring-boot-backend-architecture": [("Spring Boot Core Features", "https://docs.spring.io/spring-boot/reference/features/"), ("Spring Boot Production-ready Features", "https://docs.spring.io/spring-boot/reference/actuator/")],
    "fastapi-backend-architecture": [("FastAPI Bigger Applications", "https://fastapi.tiangolo.com/tutorial/bigger-applications/"), ("FastAPI Dependencies", "https://fastapi.tiangolo.com/tutorial/dependencies/")],
    "nestjs-backend-architecture": [("NestJS Modules", "https://docs.nestjs.com/modules"), ("NestJS Providers", "https://docs.nestjs.com/providers")],
    "gin-backend-architecture": [("Gin Middleware", "https://gin-gonic.com/en/docs/middleware/"), ("Gin Security Guide", "https://gin-gonic.com/en/docs/middleware/security-guide/")],
    "amazon-store-operations-manager": [("Amazon Seller University", "https://sell.amazon.com/learn/seller-university/"), ("Amazon Manage Your Compliance", "https://sell.amazon.com/blog/manage-your-compliance")],
    "shopify-store-operations-manager": [("Shopify Products", "https://help.shopify.com/en/manual/products"), ("Shopify Analytics", "https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports")],
    "tiktok-shop-operations-manager": [("TikTok Business Center", "https://ads.tiktok.com/business/en/business-center"), ("TikTok Creative Center", "https://ads.tiktok.com/business/en-US/creativecenter")],
    "traffic-acquisition-analyst": [("GA4 Acquisition Scope", "https://support.google.com/analytics/answer/14731736"), ("GA4 Reports Overview", "https://support.google.com/analytics/answer/9212670")],
    "conversion-funnel-analyst": [("GA4 Life Cycle Reports", "https://support.google.com/analytics/answer/12924233"), ("GA4 Ecommerce Metrics", "https://support.google.com/analytics/answer/13428834")],
    "customer-cohort-ltv-analyst": [("GA4 Retention Overview", "https://support.google.com/analytics/answer/11004084"), ("GA4 Data Retention", "https://support.google.com/analytics/answer/7667196")],
}


def q(values):
    return "、".join(values)


def write_skill(s):
    base = ROOT / s["path"]
    base.mkdir(parents=True, exist_ok=True)
    for folder in ["agents", "references", "assets", "examples", "eval", "platforms"]:
        (base / folder).mkdir(exist_ok=True)
    desc = f"{s['positioning']} Use when an AI needs to handle {', '.join(s['scenarios'])}; produce {', '.join(s['outputs'])}; and apply evidence, explicit boundaries, validation, and rollback instead of generic advice."
    steps = FAMILY_STEPS[s["family"]]
    skill = f"""---
name: {s['name']}
description: {desc}
---

# {s['display']}

{s['positioning']}

## Load resources

- Read `references/professional-checklist.md` before making decisions.
- Use `assets/delivery-template.md` for the final durable artifact.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.

## Workflow

""" + "\n".join(f"{i}. {step}" for i, step in enumerate(steps, 1)) + f"""

## Required decision lenses

""" + "\n".join(f"- {x}" for x in s["lenses"]) + f"""

## Guardrails

- {s['boundary']}
- 不得把假设写成事实；缺少关键数据时标注未知项、影响和最低验证动作。
- 不得只给原则或清单；必须给出优先级、责任、依赖、验收和风险控制。
- 不得声称已实施、已验证或已产生效果，除非有对应证据。

## Output contract

交付必须包含：目标与范围、已检查证据、关键定义、现状诊断、方案与备选、决策理由、执行或演进计划、指标与验收、风险与恢复、未知项。结论与数字必须能够追溯到来源或计算过程。
"""
    (base / "SKILL.md").write_text(skill, encoding="utf-8")

    readme = f"""# {s['display']}

> skill id：{s['name']}  
> 当前版本：1.0.0  
> 产品状态：可用  
> 所属分类：{' / '.join(Path(s['path']).parts[:-1])}

## 产品定位

{s['positioning']}

## 解决的问题

- 工作依赖个人经验，输入、过程和交付口径不稳定。
- 只关注局部动作，缺少边界、上下游、异常、数据和经营结果闭环。
- 建议无法追溯证据，也没有负责人、验收、止损或演进机制。

## 适用场景

""" + "\n".join(f"- {x}" for x in s["scenarios"]) + f"""

## 不适用范围与边界

- {s['boundary']}
- 关键口径或权限缺失时，本 Skill 可以完成诊断与方案，但不能虚构执行结果。

## 输入

- 必需：业务目标、范围、对象、现状证据和已知约束。
- 建议：历史数据、流程或系统资料、目标值、owner、预算、SLA、合规要求。
- 可选：竞品、用户反馈、事故、实验、财务和上下游契约。

## 输出

""" + "\n".join(f"- {x}" for x in s["outputs"]) + """
- 决策记录、执行计划、指标验收、风险与未知项。

## 工作原理

""" + "\n".join(f"{i}. {step}" for i, step in enumerate(steps, 1)) + f"""

## 专业检查维度

""" + "\n".join(f"- {x}" for x in s["lenses"]) + """

## 技能包组成

- `SKILL.md`：AI 执行入口与强制工作流。
- `references/professional-checklist.md`：专业检查表和失败模式。
- `assets/delivery-template.md`：可直接复用的交付模板。
- `examples/README.md`：调用示例。
- `eval/acceptance.md`：可判定验收标准。
- `README.md`：中文产品文档与迭代记录。

## 使用方式

1. 提供目标、范围、现状证据和限制条件。
2. 要求 AI 先读 `SKILL.md` 与 reference，再检查真实资料。
3. 让 AI 使用 asset 交付，并按 eval 自检；涉及写入或上线时另行确认权限。

## 验收标准

- 范围、术语、时间和数据口径明确。
- 关键结论均有证据、公式或清晰推理支撑。
- 方案覆盖正常路径、异常路径、上下游和责任边界。
- 动作有优先级、owner、依赖、指标、护栏和停止条件。
- 未知项、不确定性、风险和恢复方案被明确记录。

## 版本记录

| 版本 | 日期 | 更新内容 |
|---|---|---|
| 1.0.0 | 2026-07-15 | 建立可执行工作流、专业检查表、交付模板和可判定验收标准。 |
"""
    (base / "README.md").write_text(readme, encoding="utf-8")

    checks = "\n".join(f"- [ ] {x} 已定义、验证或标记为未知" for x in s["lenses"])
    source_lines = "\n".join(f"- [{label}]({url})" for label, url in OFFICIAL_SOURCES.get(s["name"], []))
    source_section = f"\n## 官方基线资料\n\n{source_lines}\n" if source_lines else ""
    (base / "references/professional-checklist.md").write_text(f"""# {s['display']}专业检查表

## 执行前

- [ ] 目标、范围、国家/渠道/系统、周期和责任人明确
- [ ] 已区分事实、假设、缺失数据和待确认口径
- [ ] 已读取一手资料，并记录来源时间与适用版本

## 核心维度

{checks}
{source_section}

## 失败模式

- 只有最佳实践，没有结合当前证据和约束。
- 只覆盖顺利路径，没有异常、补偿、回滚和人工介入。
- 指标同名但 scope、状态、时区、币种或归因窗口不同。
- 动作没有 owner、投入、依赖、验收或停止条件。

## 交付前

- [ ] 关键结论能追溯到证据或计算
- [ ] 备选方案、取舍和不做事项清楚
- [ ] 计划可分阶段执行并有验证与恢复路径
""", encoding="utf-8")

    (base / "assets/delivery-template.md").write_text(f"""# {s['display']}交付模板

## 1. 执行摘要

- 目标与范围：
- 核心结论：
- 需要的决策：

## 2. 口径与证据

| 项目 | 定义/来源 | 时间或版本 | 可信度 | 限制 |
|---|---|---|---|---|

## 3. 现状与问题

| 问题/机会 | 影响 | 根因证据 | 优先级 |
|---|---:|---|---|

## 4. 关键设计维度

""" + "\n".join(f"### {i}. {x}\n\n- 现状：\n- 决策：\n- 理由与替代：\n" for i, x in enumerate(s["lenses"], 1)) + """
## 5. 实施计划

| 阶段/动作 | Owner | 依赖 | 截止 | 验收 | 护栏/停止条件 |
|---|---|---|---|---|---|

## 6. 风险、恢复与未知项

| 风险/未知 | 触发信号 | 影响 | 控制/验证 | 恢复路径 |
|---|---|---|---|---|
""", encoding="utf-8")

    (base / "INVOCATION.md").write_text(f"""# 调用说明

适合调用：{q(s['scenarios'])}。

推荐指令：

> 使用 `{s['name']}`，基于我提供的真实资料完成“目标”。先确认范围和口径，检查证据，再按模板输出方案、优先级、owner、指标、风险和未知项。不要虚构已执行结果。
""", encoding="utf-8")
    (base / "BASE_PROMPT.md").write_text(f"""# Base prompt

You are the {s['display']}. Follow `SKILL.md`, read the checklist, inspect primary evidence, and use the delivery template. Separate facts, calculations, inferences, recommendations, and unknowns. Produce decision-ready work with explicit scope, ownership, acceptance criteria, guardrails, and recovery.
""", encoding="utf-8")
    (base / "examples/README.md").write_text("# 示例\n\n- 基础：基于现状资料完成一次诊断和优先级方案。\n- 进阶：比较两个备选方案，说明数据、成本、风险和可逆性。\n- 验收：对已有方案按 `eval/acceptance.md` 审核，列出未通过项和修正建议。\n", encoding="utf-8")
    (base / "eval/acceptance.md").write_text("# 验收\n\n- [ ] 使用了真实输入并标明证据来源、日期或版本\n- [ ] 定义了范围、术语、指标与不做事项\n- [ ] 覆盖关键专业维度、上下游和异常路径\n- [ ] 建议有优先级、owner、依赖、验收与护栏\n- [ ] 区分事实、推断、建议和未知项\n- [ ] 未虚构实施、验证、效果或权限\n", encoding="utf-8")
    (base / "platforms/README.md").write_text("# 平台适配\n\n该 Skill 以 Markdown 和 JSON 作为可移植契约。在支持文件读取的平台加载整个目录；在只支持提示词的平台至少加载 `SKILL.md`、reference 与 asset。涉及仓库、数据源或外部系统时，按平台权限先读后写并保留验证证据。\n", encoding="utf-8")
    yaml = f"""interface:
  display_name: "{s['display']}"
  short_description: "{s['positioning'][:60]}"
  default_prompt: "使用 ${s['name']} 基于真实证据完成可执行交付，并给出验收、风险和未知项。"
"""
    (base / "agents/openai.yaml").write_text(yaml, encoding="utf-8")
    category = list(Path(s["path"]).parts[:-1])
    payload = {
        "name": s["name"], "display_name": s["display"],
        "type": "portable-business-skill", "scope": "cross-platform",
        "version": "1.0.0", "owner_project": "SkillForge", "portable": True,
        "entrypoint": "SKILL.md", "category_path": category,
        "description": f"{s['positioning']}适用于{q(s['scenarios'])}，交付{q(s['outputs'])}。",
        "search_keywords": [*s["scenarios"], *s["lenses"][:3]],
        "supported_platforms": PLATFORMS,
        "inputs": {"required": ["业务目标、范围和现状证据"], "optional": ["历史数据、流程系统资料、目标、预算、SLA 和合规约束"]},
        "outputs": [*s["outputs"], "决策、执行、验收、风险和未知项记录"],
        "implementation": {"readme": "README.md", "entry_doc": "SKILL.md", "invocation_doc": "INVOCATION.md", "script": "", "config": "", "base_prompt": "BASE_PROMPT.md", "examples_dir": "examples", "eval_dir": "eval", "platform_adapters_dir": "platforms"},
        "constraints": [s["boundary"], "不得虚构事实、数据、权限、实施或验证结果", "必须明确口径、责任、验收、风险和未知项"],
        "distribution": {"share_as_single_folder": True, "required_files": ["SKILL.md", "skill.json", "README.md", "INVOCATION.md", "BASE_PROMPT.md"], "package_files": ["SKILL.md", "skill.json", "README.md", "INVOCATION.md", "BASE_PROMPT.md", "agents/openai.yaml", "references", "assets", "examples", "eval", "platforms"]},
    }
    (base / "skill.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


for item in SPECS:
    write_skill(item)

CATEGORIES = {
    "互联网研发/前端/架构": ("前端通用架构", "沉淀与语言和框架无关的前端边界、运行时、质量属性和演进方法。"),
    "互联网研发/前端/语言": ("前端语言架构", "处理 JavaScript、TypeScript 等语言自身的模块、类型、运行时和工程约束。"),
    "互联网研发/前端/语言/JavaScript": ("JavaScript 前端架构", "治理动态类型、模块系统、异步运行时和依赖供应链。"),
    "互联网研发/前端/语言/TypeScript": ("TypeScript 前端架构", "治理类型边界、项目引用、模块解析和编译性能。"),
    "互联网研发/前端/框架": ("前端框架架构", "在通用架构与语言架构之上处理具体框架的运行语义。"),
    "互联网研发/前端/框架/React": ("React 架构", "处理 React 组件、状态、数据流、渲染和测试边界。"),
    "互联网研发/前端/框架/Vue": ("Vue 架构", "处理 Vue 组件、组合式逻辑、响应式状态和工程边界。"),
    "互联网研发/前端/框架/Next.js": ("Next.js 架构", "处理 App Router、Server/Client Components、缓存、SEO 和部署。"),
    "互联网研发/后端/架构": ("后端通用架构", "沉淀语言无关的领域边界、质量属性、数据 ownership 和演进路线。"),
    "互联网研发/后端/语言": ("后端语言架构", "按 Java、Go、Python、Node.js 的运行模型和生态细化架构。"),
    "互联网研发/后端/语言/Java": ("Java 后端架构", "处理 Java 模块、并发、JVM 和长期演进。"),
    "互联网研发/后端/语言/Go": ("Go 后端架构", "处理 Go 包边界、并发、取消、错误和资源生命周期。"),
    "互联网研发/后端/语言/Python": ("Python 后端架构", "处理 Python 包、类型、同步异步和运行环境。"),
    "互联网研发/后端/语言/Node.js": ("Node.js 后端架构", "处理事件循环、模块格式、异步失败和资源限制。"),
    "互联网研发/后端/框架": ("后端框架架构", "在通用和语言架构上处理具体框架的模块、依赖和生产能力。"),
    "互联网研发/后端/框架/Spring Boot": ("Spring Boot 架构", "处理模块、依赖注入、事务、安全和生产可观测。"),
    "互联网研发/后端/框架/FastAPI": ("FastAPI 架构", "处理 APIRouter、Depends、Pydantic、异步和部署。"),
    "互联网研发/后端/框架/NestJS": ("NestJS 架构", "处理 module、provider、请求管道和集成边界。"),
    "互联网研发/后端/框架/Gin": ("Gin 架构", "处理路由、middleware、显式依赖和 Go HTTP 运行时。"),
    "跨境运营/市场与战略": ("市场与战略", "覆盖市场情报、机会判断、上市和跨市场策略。"),
    "跨境运营/品牌营销": ("品牌营销", "覆盖品牌定位、价值证据和跨文化表达。"),
    "跨境运营/渠道运营": ("渠道运营", "覆盖渠道组合与各平台端到端经营。"),
    "跨境运营/渠道运营/亚马逊": ("亚马逊运营", "覆盖 Amazon 账户、目录、流量、广告、库存和利润。"),
    "跨境运营/渠道运营/独立站": ("独立站运营", "覆盖 Shopify 商品、流量、转化、订单和客户经营。"),
    "跨境运营/渠道运营/TikTok Shop": ("TikTok Shop 运营", "覆盖内容、直播、达人、广告、商品和履约联动。"),
    "跨境运营/内容营销": ("内容营销", "覆盖主题策略、编辑日历、分发、转化和衡量。"),
    "跨境运营/社媒营销": ("社媒营销", "覆盖平台内容、社区互动、自然增长和账号健康。"),
    "跨境运营/达人联盟": ("达人与联盟", "覆盖发现、筛选、合作、授权、佣金和增量效果。"),
    "跨境运营/用户运营": ("用户运营", "覆盖邮件生命周期、购后、召回、会员和忠诚度。"),
    "跨境运营/活动营销": ("活动营销", "覆盖跨市场促销日历、资源统筹和活动复盘。"),
    "跨境运营/创意生产": ("创意生产", "覆盖洞察、角度、脚本、素材测试和疲劳管理。"),
    "跨境运营/商品运营": ("商品运营", "覆盖平台商品信息、搜索发现和转化表达。"),
    "跨境运营/客户体验": ("客户体验", "覆盖多语言客服、评价、声誉和 VOC 改进闭环。"),
    "跨境运营/商业化": ("商业化", "覆盖定价、折扣、促销和单位经济。"),
    "跨境运营/增长营销": ("增长营销", "覆盖归因、获客、转化、留存和跨团队增长。"),
    "数据/业务分析": ("跨境业务数据分析", "覆盖指标、经营、利润、商品、流量、漏斗、广告、客户、库存和预测。"),
    "数据/数据治理": ("数据治理", "覆盖数据质量、跨系统对账、口径和责任治理。"),
    "项目管理/公共": ("业务系统公共架构", "沉淀跨系统能力地图、主数据归属和端到端协同。"),
    "项目管理/OMS": ("OMS 项目", "订单管理系统的产品架构和后续细分 Skill。"),
    "项目管理/IMS": ("IMS 项目", "库存管理系统的产品架构和后续细分 Skill。"),
    "项目管理/OFS": ("OFS 项目", "订单履约系统的产品架构和后续细分 Skill。"),
    "项目管理/CMS": ("CMS 项目", "商品/内容管理系统的产品架构和后续细分 Skill。"),
    "项目管理/TMS": ("TMS 项目", "运输管理系统的产品架构和后续细分 Skill。"),
    "项目管理/CRM": ("CRM 项目", "客户关系系统的产品架构和后续细分 Skill。"),
    "项目管理/PLM": ("PLM 项目", "产品生命周期系统的产品架构和后续细分 Skill。"),
    "项目管理/WMS": ("WMS 项目", "仓储管理系统的产品架构和后续细分 Skill。"),
}


def category_readme(relative, title, summary):
    directory = ROOT / relative
    directory.mkdir(parents=True, exist_ok=True)
    rows = []
    for meta in sorted(directory.rglob("skill.json")):
        data = json.loads(meta.read_text(encoding="utf-8"))
        skill_dir = meta.parent.relative_to(directory)
        rows.append(f"- [{data['display_name']}]({skill_dir.as_posix()}/README.md)：{data['description']}")
    body = f"""# {title}

## 分类定位

{summary}

## 选择原则

- 先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。
- 一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。
- README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。

## 当前 Skill

""" + ("\n".join(rows) if rows else "- 暂无正式 Skill，作为未来扩展入口。") + f"""

## 迭代记录

| 日期 | 更新 |
|---|---|
| {DATE} | 建立分类定位、选择原则和正式 Skill 索引。 |
"""
    (directory / "README.md").write_text(body, encoding="utf-8")


for path, (title, summary) in CATEGORIES.items():
    category_readme(path, title, summary)

print(f"Built {len(SPECS)} complete skill packages and {len(CATEGORIES)} category docs")
