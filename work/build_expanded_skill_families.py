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
    spec("互联网研发/前端/框架/Angular/angular-frontend-architecture", "angular-frontend-architecture", "Angular 前端架构师", "architecture", "围绕 standalone components、signals、依赖注入、路由和混合渲染设计大型 Angular 应用。", ["Angular 企业应用架构", "NgModule 到 standalone 演进", "大型团队前端平台治理"], ["Angular 功能域架构", "依赖注入与状态边界", "渲染、测试和升级方案"], ["standalone component 与 feature 边界", "signals、RxJS 和状态 ownership", "DI scope 与 provider", "routing、forms 和 HTTP", "SSR、hydration、测试和 ng update"], "不得用根级 provider 和共享模块消解所有领域边界。"),
    spec("互联网研发/前端/框架/SvelteKit/sveltekit-frontend-architecture", "sveltekit-frontend-architecture", "SvelteKit 前端架构师", "architecture", "围绕文件路由、load、form actions、服务端边界和 adapter 设计生产级 SvelteKit 应用。", ["SvelteKit 新项目", "SSR/SSG/SPA 混合架构", "SvelteKit 数据与部署治理"], ["SvelteKit 路由和渲染架构", "数据、表单与状态边界", "adapter、观测和部署方案"], ["route、layout 与项目结构", "load、form actions 和 remote functions", "server-only 模块与 secrets", "SSR、prerender 和客户端状态", "hooks、errors、adapter 和 observability"], "不得把服务端私密数据引入客户端 bundle，也不得忽略 adapter 的运行环境约束。"),
    spec("互联网研发/后端/架构/backend-architecture-designer", "backend-architecture-designer", "后端通用架构设计师", "architecture", "从领域边界、质量属性、数据 ownership 和演进路线设计语言无关的后端系统架构。", ["企业后端总体架构", "单体、模块化和服务化选型", "跨团队系统演进评审"], ["后端总体架构蓝图", "质量属性与边界决策", "技术路线和分阶段演进计划"], ["领域与系统上下文", "一致性、可用性和延迟目标", "数据 ownership 与集成契约", "安全、韧性和可观测性", "部署拓扑、容量和演进"], "不替代单个服务的详细设计，不因潮流默认微服务。"),
    spec("互联网研发/后端/语言/Java/java-backend-architecture", "java-backend-architecture", "Java 后端架构师", "architecture", "利用 Java 类型、并发、JVM 和模块生态设计长期可维护的后端系统。", ["Java 服务平台架构", "大型 Java 单体模块化", "JVM 性能和升级治理"], ["Java 模块架构", "并发与资源模型", "JVM 运行和演进方案"], ["package/module 依赖", "线程、虚拟线程和阻塞边界", "异常、空值和领域类型", "JVM 内存、GC 和观测", "构建、依赖和版本升级"], "不把框架注解当作领域架构，也不在未测量前做 JVM 调优。"),
    spec("互联网研发/后端/语言/Go/go-backend-architecture", "go-backend-architecture", "Go 后端架构师", "architecture", "按 Go 的显式依赖、并发模型和简洁包边界设计可靠后端。", ["Go API 或任务服务", "高并发 Go 服务治理", "Go 单仓多服务架构"], ["Go 包与服务架构", "并发和取消模型", "错误、测试和部署方案"], ["package 责任与依赖方向", "context、goroutine 和背压", "错误语义与接口最小化", "配置、资源池和优雅停机", "测试、profile 和发布"], "不得滥用 goroutine、全局状态或过度抽象接口。"),
    spec("互联网研发/后端/语言/Python/python-backend-architecture", "python-backend-architecture", "Python 后端架构师", "architecture", "围绕包结构、类型边界、同步异步模型和运行环境设计可维护 Python 后端。", ["Python Web 或任务平台", "脚本向服务化演进", "同步与异步混合系统治理"], ["Python 包与层次架构", "执行和并发模型", "依赖、测试和部署方案"], ["package、module 和 import 边界", "typing 与运行时校验", "asyncio、线程和进程选择", "依赖与虚拟环境", "测试、性能和可观测性"], "不得把动态便利性变成隐式全局依赖或无法验证的字典契约。"),
    spec("互联网研发/后端/语言/Node.js/nodejs-backend-architecture", "nodejs-backend-architecture", "Node.js 后端架构师", "architecture", "按事件循环、模块格式、异步失败和资源限制设计可靠 Node.js 后端。", ["Node.js API 和 BFF", "高 I/O 服务架构", "CommonJS 到 ESM 迁移"], ["Node.js 模块架构", "异步与资源模型", "可靠性和部署方案"], ["ESM/CommonJS 与 package 边界", "事件循环和阻塞工作", "Promise、取消和错误传播", "连接池、流和背压", "进程模型、观测和安全"], "不得在主线程执行未受控 CPU 重任务，也不得吞掉异步错误。"),
    spec("互联网研发/后端/语言/PHP/php-backend-architecture", "php-backend-architecture", "PHP 后端架构师", "architecture", "围绕 namespace、Composer、请求生命周期和显式模块边界设计可维护 PHP 后端。", ["PHP 业务系统架构", "遗留 PHP 模块化重构", "PHP 运行和依赖治理"], ["PHP 模块与包架构", "请求和资源生命周期", "依赖、测试和部署方案"], ["namespace、PSR 和 Composer", "请求生命周期与共享状态", "领域类型、异常和校验", "数据库事务、队列和缓存", "静态分析、测试和运行模式"], "不得让全局函数、服务定位器和动态数组成为跨模块隐式契约。"),
    spec("互联网研发/后端/语言/Rust/rust-backend-architecture", "rust-backend-architecture", "Rust 后端架构师", "architecture", "利用 ownership、类型系统、错误模型和 async runtime 设计安全可预测的 Rust 后端。", ["Rust API 或系统服务", "高可靠高性能服务", "Rust workspace 和 crate 架构"], ["Rust crate 与领域架构", "并发和资源模型", "错误、测试和部署方案"], ["crate、module 和 feature 边界", "ownership、borrowing 和领域类型", "Result、错误分层和恢复", "async runtime、Send/Sync 和取消", "unsafe 边界、测试和性能测量"], "不得为绕过编译器随意扩大 clone、Arc/Mutex 或 unsafe 使用范围。"),
    spec("互联网研发/后端/语言/C#/csharp-backend-architecture", "csharp-backend-architecture", "C# 后端架构师", "architecture", "围绕 solution/project、类型、async/await、依赖注入和 .NET 运行时设计稳健后端。", ["C# 企业后端架构", ".NET 单体模块化", "异步、资源和版本升级治理"], ["C# solution 与模块架构", "异步和资源生命周期", "依赖、测试和部署方案"], ["solution、project 和 namespace 边界", "nullable、record 和领域类型", "async/await、CancellationToken 和线程池", "IDisposable、DI scope 和配置", "测试、诊断和 .NET 版本策略"], "不得用共享项目、静态服务或同步阻塞破坏模块和异步边界。"),
    spec("互联网研发/后端/框架/Spring Boot/spring-boot-backend-architecture", "spring-boot-backend-architecture", "Spring Boot 后端架构师", "architecture", "围绕业务模块、依赖注入、事务、安全和 Actuator 设计生产级 Spring Boot 架构。", ["Spring Boot 服务新建或重构", "模块化单体与服务拆分", "生产可观测和升级治理"], ["Spring Boot 模块架构", "事务与集成边界", "生产运行和迁移方案"], ["业务模块和 bean 边界", "配置、profiles 和 secrets", "事务、持久化和事件", "Security 与接口授权", "Actuator、测试和版本升级"], "不得形成 controller-service-repository 的空洞分层或跨模块任意注入。"),
    spec("互联网研发/后端/框架/FastAPI/fastapi-backend-architecture", "fastapi-backend-architecture", "FastAPI 后端架构师", "architecture", "围绕 APIRouter、依赖注入、Pydantic 契约和异步边界设计生产级 FastAPI 服务。", ["FastAPI 中大型应用", "Python API 模块化", "异步 API 性能和可靠性治理"], ["FastAPI 包与路由架构", "依赖和数据契约", "运行、测试和部署方案"], ["APIRouter 与业务模块", "Depends 生命周期和授权", "Pydantic 输入输出契约", "async/sync 与阻塞依赖", "异常、OpenAPI、测试和部署"], "不得把业务逻辑堆入 route handler，也不得假设 async 自动提升性能。"),
    spec("互联网研发/后端/框架/NestJS/nestjs-backend-architecture", "nestjs-backend-architecture", "NestJS 后端架构师", "architecture", "围绕 module、provider、边界契约和请求管道设计模块化 NestJS 系统。", ["NestJS 企业 API", "模块边界和依赖治理", "单体到服务化演进"], ["NestJS 模块架构", "provider 与请求管道设计", "测试和部署方案"], ["module 导入导出边界", "provider scope 与依赖注入", "pipe、guard、interceptor 和 filter", "DTO、验证和 API 契约", "队列、微服务适配器和观测"], "不得创建全局万能模块或循环依赖来掩盖领域边界问题。"),
    spec("互联网研发/后端/框架/Gin/gin-backend-architecture", "gin-backend-architecture", "Gin 后端架构师", "architecture", "围绕路由、middleware、显式依赖和 Go 运行模型设计精简可靠的 Gin 服务。", ["Gin API 新建或重构", "高吞吐 Go HTTP 服务", "middleware 和安全治理"], ["Gin 路由与模块架构", "middleware 和依赖方案", "性能、安全和部署计划"], ["route group 与业务模块", "middleware 顺序和短路", "请求绑定、验证和错误", "context、超时和资源释放", "安全 headers、测试和 profile"], "不得让 handler 直接承担持久化、业务和外部集成全部职责。"),
    spec("互联网研发/后端/框架/Laravel/laravel-backend-architecture", "laravel-backend-architecture", "Laravel 后端架构师", "architecture", "围绕领域模块、service container、Eloquent、队列和请求生命周期设计生产级 Laravel 架构。", ["Laravel 中大型业务系统", "Laravel 单体模块化", "队列、事件和性能治理"], ["Laravel 业务模块架构", "容器、数据和异步边界", "安全、测试和部署方案"], ["业务模块与 service provider", "container binding 和生命周期", "Eloquent、事务和查询边界", "queue、event、schedule 和幂等", "middleware、authorization、Octane 和部署"], "不得把所有业务逻辑堆在 controller、model observer 或全局 helper。"),
    spec("互联网研发/后端/框架/ASP.NET Core/aspnet-core-backend-architecture", "aspnet-core-backend-architecture", "ASP.NET Core 后端架构师", "architecture", "围绕 host、依赖注入、middleware、endpoint、配置和可观测性设计生产级 ASP.NET Core 架构。", ["ASP.NET Core API", "模块化 .NET 后端", "Minimal API 与 Controller 架构评审"], ["ASP.NET Core 模块架构", "DI 与请求管道", "数据、安全和生产运行方案"], ["host、configuration 和 options", "DI lifetime 与 module registration", "middleware 顺序和 endpoint", "EF Core 事务和后台服务", "认证授权、health、logging 和部署"], "不得混淆 Singleton、Scoped、Transient 生命周期或让 middleware 顺序依赖隐含。"),
    # Cross-border operating and marketing roles.
    spec("精准营销/市场策略/cross-border-market-intelligence", "cross-border-market-intelligence", "跨境市场情报分析师", "operations", "把国家、类目、消费者、竞品和渠道证据转化为可验证的市场机会。", ["进入新国家或类目", "竞品与价格带扫描", "季度市场机会更新"], ["市场情报简报", "机会评分和证据表", "验证计划与预警项"], ["需求与搜索信号", "竞争格局和价格带", "消费者场景与障碍", "法规、季节和渠道差异", "证据新鲜度与反证"], "不得用单一平台热度直接证明真实利润机会。"),
    spec("精准营销/品牌营销/brand-positioning-strategist", "brand-positioning-strategist", "跨境品牌定位策略师", "operations", "以目标人群、真实差异、品类语境和跨文化表达建立可执行品牌定位。", ["新品牌定位", "品牌升级或多市场适配", "产品线信息架构统一"], ["定位陈述", "价值支柱与证据", "品牌信息和禁用表达"], ["目标人群和使用场景", "竞争参照与差异", "功能到利益的证据链", "品牌个性和语气", "国家文化与合规表达"], "不得创造产品不具备的卖点或空泛价值观。"),
    spec("精准营销/市场策略/go-to-market-launch-planner", "go-to-market-launch-planner", "跨境上市规划师", "operations", "把产品、市场、渠道、库存、内容和投放组织成有门槛条件的上市计划。", ["新品上市", "新站点或新国家启动", "重大版本或季节发布"], ["GTM 计划", "阶段门和责任矩阵", "预算、指标与复盘设计"], ["市场与产品准备度", "渠道和库存 readiness", "内容、评价和广告冷启动", "里程碑、依赖和 owner", "领先指标、止损和复盘"], "不得只做营销日历而忽略供货、合规和客服准备。"),
    spec("渠道运营/平台运营/channel-portfolio-strategist", "channel-portfolio-strategist", "跨境渠道组合策略师", "operations", "按渠道角色、客户 ownership、利润和运营复杂度配置平台与独立站组合。", ["Amazon、Shopify、TikTok 等渠道组合", "新渠道评估", "渠道冲突和资源分配"], ["渠道角色地图", "进入与退出评分", "资源和治理方案"], ["客群和购买任务", "流量 ownership 与数据可得性", "毛利、费用和现金周期", "价格、库存和内容冲突", "组织能力和试点门槛"], "不得只按 GMV 评价渠道价值。"),
    spec("精准营销/内容营销/content-marketing-planner", "content-marketing-planner", "跨境内容营销规划师", "operations", "把搜索需求、用户旅程、产品事实和商业目标组织成可复用内容系统。", ["博客和指南规划", "季度内容矩阵", "SEO、社媒、邮件内容协同"], ["内容战略", "主题集群和编辑日历", "分发、转化与衡量方案"], ["受众问题和意图", "主题支柱与内容缺口", "产品证据和内链", "渠道再利用", "转化动作和内容指标"], "不得批量制造同模板低价值内容。"),
    spec("精准营销/社媒营销/social-media-operations-manager", "social-media-operations-manager", "跨境社媒运营经理", "operations", "建立平台适配的内容、互动、增长、风险和复盘机制。", ["TikTok、Instagram、YouTube、Pinterest 运营", "账号冷启动", "社媒内容和社区增长"], ["平台运营方案", "内容栏目和发布节奏", "互动 SOP 与周度复盘"], ["平台人群和内容语法", "栏目、节奏和素材供给", "社区互动和舆情", "自然流量到商业转化", "账号健康和实验指标"], "不得跨平台原样搬运或追逐与品牌无关的热点。"),
    spec("精准营销/达人联盟/influencer-affiliate-manager", "influencer-affiliate-manager", "达人与联盟营销经理", "operations", "管理达人发现、筛选、邀约、寄样、内容授权、佣金和增量效果。", ["达人种草和带货", "联盟计划搭建", "UGC 采购与授权"], ["达人分层池", "合作 brief 与跟进管道", "佣金、授权和效果复盘"], ["人群与内容匹配", "真实性和历史表现", "合作模式与单位经济", "寄样、交付和授权", "归因、增量和合规披露"], "不得按粉丝量单点筛选，也不得遗漏广告披露和内容权利。"),
    spec("精准营销/用户运营/email-lifecycle-marketer", "email-lifecycle-marketer", "邮件生命周期营销师", "operations", "按同意、用户阶段和行为信号设计可衡量的邮件与自动化流程。", ["欢迎、弃购、购后、召回流程", "Newsletter 运营", "邮件收入和送达率治理"], ["生命周期流程图", "分群、触发与内容方案", "实验和送达健康看板"], ["同意、偏好和退订", "触发、频控和冲突", "分群与个性化", "内容、优惠和落地页", "送达、增量收入和实验"], "不得用群发频率代替用户价值，也不得绕过同意规则。"),
    spec("精准营销/活动营销/promotion-calendar-manager", "promotion-calendar-manager", "跨境活动营销经理", "operations", "统筹国家节日、平台节点、库存和利润，形成跨渠道活动经营日历。", ["黑五网一和节日大促", "季度促销规划", "多渠道活动冲突治理"], ["年度/季度活动日历", "活动机制和资源表", "上线检查与复盘模板"], ["市场节点和提前期", "活动目标与目标人群", "折扣、毛利和库存", "渠道规则与价格一致性", "素材、技术、客服和复盘"], "不得默认每个节日都打折，也不得在库存或毛利不支持时硬上活动。"),
    spec("创拍视觉/创意策略/creative-strategy-producer", "creative-strategy-producer", "跨境广告创意策略师", "creative-production", "从人群洞察和产品证据建立可拍摄、可批量测试、可归因的创意生产系统。", ["广告素材策略", "UGC brief 和脚本矩阵", "创意疲劳治理"], ["创意策略地图", "角度、钩子和脚本矩阵", "测试编码与复盘规则"], ["人群问题和欲望", "产品证据与演示", "角度、钩子、格式和 CTA", "平台原生表达", "变量隔离、标签和疲劳"], "不得虚构效果、评价或前后对比；策略必须能够转化为明确镜头和制作要求。"),
    spec("渠道运营/商品运营/marketplace-listing-optimizer", "marketplace-listing-optimizer", "平台商品信息优化师", "operations", "基于真实产品事实、搜索意图和平台规则优化商品信息与转化表达。", ["Amazon 等平台 listing 优化", "新品信息搭建", "低流量或低转化详情修复"], ["关键词和信息架构", "标题、卖点和详情建议", "合规与实验清单"], ["产品事实与证据", "搜索词意图和优先级", "标题、要点、属性和后台词", "图片/A+ 信息任务", "合规、变体和实验"], "不得关键词堆砌或生成无证据声明。"),
    spec("渠道运营/平台运营/亚马逊/amazon-store-operations-manager", "amazon-store-operations-manager", "亚马逊店铺运营经理", "operations", "统筹 Amazon 账户健康、目录、流量、转化、广告、库存、价格和复盘。", ["Amazon 日常经营", "新品启动", "店铺问题诊断和周月度复盘"], ["Amazon 经营计划", "问题优先级与执行清单", "店铺经营复盘"], ["账户与合规健康", "目录、搜索和转化", "广告和促销", "FBA 库存与补货", "利润、评价和竞争态势"], "不得通过违规评价、误导声明或破坏价格逻辑换取短期增长。"),
    spec("渠道运营/平台运营/独立站/shopify-store-operations-manager", "shopify-store-operations-manager", "Shopify 独立站运营经理", "operations", "统筹商品、内容、流量、转化、订单、客户和技术健康的独立站经营。", ["Shopify 日常运营", "新品与活动上线", "独立站增长和问题排查"], ["独立站经营计划", "上线与健康检查表", "渠道和站内经营复盘"], ["商品、集合和内容", "流量、落地页和转化", "促销、结账和支付", "订单、履约和客服", "数据、应用、性能和隐私"], "不得只看主题页面而忽略数据、履约和客户体验闭环。"),
    spec("渠道运营/平台运营/TikTok Shop/tiktok-shop-operations-manager", "tiktok-shop-operations-manager", "TikTok Shop 运营经理", "operations", "联动商品、短视频、直播、达人、广告、履约和店铺健康运营 TikTok Shop。", ["TikTok Shop 冷启动", "内容电商日常经营", "GMV 波动诊断"], ["TikTok Shop 经营计划", "内容达人商品协同表", "店铺健康和复盘"], ["店铺和商品健康", "短视频与直播供给", "达人联盟和授权", "广告、活动与转化", "库存、履约、退款和评分"], "不得用高 GMV 掩盖高退款、低毛利或违规风险。"),
    spec("客服售前/客服运营/customer-service-voice-manager", "customer-service-voice-manager", "跨境客服售前运营专家", "customer-presales", "端到端完成跨渠道购买前咨询、需求澄清、商品推荐、多语言回复、FAQ 沉淀、线索分级、质检培训和销售交接。", ["邮件、聊天和平台消息售前接待", "商品推荐、异议处理与多语言沟通", "客服知识库、线索交接和质量改进"], ["售前答复与商品推荐方案", "客服 SOP、FAQ、话术和权限矩阵", "线索、质检、培训与 VOC 改进报告"], ["客户场景、预算和硬约束", "商品、价格、库存、履约与政策事实", "语言、文化、隐私和品牌语气", "意向、异议、线索分级和销售交接", "知识版本、抽样质检、培训和 VOC 闭环"], "不得为转化虚构功能、现货、折扣、送达或保修承诺；不得机械直译、过度采集个人数据或仅以响应时长评价服务。"),
    spec("渠道运营/客户体验/review-reputation-manager", "review-reputation-manager", "评价与品牌声誉经理", "operations", "合规监控评价、识别根因、回复客户并推动产品和履约改进。", ["平台评价治理", "差评和舆情响应", "评分下降根因分析"], ["评价健康报告", "合规回复和升级方案", "根因与改进闭环"], ["评价来源和真实性", "主题、严重度和趋势", "公开回复与私下解决", "产品、包装、物流和预期根因", "平台政策和效果追踪"], "不得操纵评价、诱导只留好评或披露客户隐私。"),
    spec("精准营销/用户运营/customer-retention-loyalty-manager", "customer-retention-loyalty-manager", "客户留存与忠诚度经理", "operations", "按客户价值和复购周期设计购后体验、会员、召回与忠诚机制。", ["复购率提升", "会员或积分计划", "流失客户召回"], ["留存策略", "客户分层和触达旅程", "会员经济模型与实验"], ["复购周期和流失信号", "cohort、RFM 和 LTV", "购后教育与服务", "积分、权益和推荐", "增量留存和毛利"], "不得用无差别优惠制造虚假留存。"),
    spec("渠道运营/商业化/pricing-promotion-optimizer", "pricing-promotion-optimizer", "定价与促销优化经理", "operations", "综合消费者价值、竞争、成本、渠道规则和需求弹性制定定价促销方案。", ["新品定价", "跨国家跨渠道价格治理", "折扣和优惠机制优化"], ["价格架构", "促销方案和利润模拟", "实验、监控与退出规则"], ["成本和最低可接受贡献", "价值与竞争价格带", "税费、汇率和渠道费用", "折扣结构与参照价", "弹性、蚕食和库存"], "不得用虚假参照价或只看转化不看贡献利润。"),
    spec("精准营销/增长营销/marketing-attribution-planner", "marketing-attribution-planner", "跨渠道营销归因规划师", "operations", "建立口径透明、可解释并能支持预算决策的跨渠道归因体系。", ["广告平台与 GA4 对数", "多触点归因治理", "预算分配和增量评估"], ["归因测量方案", "渠道数据和 UTM 规范", "模型差异、实验与决策规则"], ["业务问题和转化窗口", "用户、会话和平台口径", "身份、UTM 和事件质量", "模型偏差和不可观测触点", "增量实验与预算决策"], "不得把平台自报收入相加后当作公司真实收入。"),
    spec("精准营销/增长营销/cross-border-growth-operator", "cross-border-growth-operator", "跨境全链路增长负责人", "operations", "把获客、转化、客单、复购和毛利组织为有约束的跨职能增长系统。", ["季度增长规划", "GMV 或利润增长诊断", "跨团队增长实验组合"], ["增长模型和机会树", "实验组合与责任矩阵", "周度经营节奏和复盘"], ["增长方程和北极星指标", "获客质量与转化", "客单、复购和毛利", "库存、履约和体验约束", "实验优先级和组织 cadence"], "不得以不可持续投放或折扣换取表面增长。"),
    # Business-side analytics.
    spec("数据看板/业务分析/business-metrics-governance", "business-metrics-governance", "业务指标治理师", "analytics", "建立跨平台可复算的指标、维度、时间、币种和责任人标准。", ["经营指标字典", "多系统口径统一", "看板和周报上线前治理"], ["指标字典", "维度与数据血缘", "变更、认证和争议处理机制"], ["业务定义与公式", "粒度、去重和状态", "时区、币种和税口径", "来源、owner 和刷新", "版本、测试和认证"], "不得在定义未统一时直接比较或汇总指标。"),
    spec("数据看板/业务分析/executive-business-review", "executive-business-review", "经营分析与周月报专家", "analytics", "把可靠数据转化为结论先行、驱动清晰、可决策的 WBR/MBR/QBR。", ["跨境经营周报月报", "管理层业务复盘", "目标差距和行动跟踪"], ["经营摘要", "KPI 与驱动分析", "风险、决策和责任闭环"], ["目标、同比和环比口径", "收入利润和现金", "商品渠道客户驱动", "异常、置信度和反证", "决策、owner 和截止时间"], "不得罗列数据代替结论，也不得在口径不一致时强行解释。"),
    spec("数据看板/业务分析/sales-profitability-analyst", "sales-profitability-analyst", "销售与利润分析师", "analytics", "拆解销售、毛利、贡献利润和现金驱动，定位真正创造或消耗价值的业务单元。", ["销售和利润波动", "国家渠道 SKU 盈利分析", "利润改善机会评估"], ["收入利润桥", "分层盈利矩阵", "驱动、风险和改善测算"], ["销量、价格和组合", "退款、折扣和税费", "平台、支付、物流和广告成本", "固定与变动成本", "币种、时点和贡献层级"], "不得只按销售额评价业务，也不得混用毛利和贡献利润。"),
    spec("数据看板/业务分析/product-portfolio-analyst", "product-portfolio-analyst", "商品组合分析师", "analytics", "从需求、转化、利润、库存和生命周期评估 SKU 角色与动作。", ["SKU 分层", "新品和长尾评估", "淘汰、补货与资源分配"], ["商品组合矩阵", "SKU 诊断与动作", "新品、保留和退出规则"], ["流量、转化和销量", "毛利和贡献", "库存周转和缺货", "评价退货和生命周期", "替代、互补和蚕食"], "不得只用销量做 ABC 分类后直接决策。"),
    spec("数据看板/业务分析/traffic-acquisition-analyst", "traffic-acquisition-analyst", "流量与获客分析师", "analytics", "区分用户级与会话级来源，评估流量规模、质量、成本和下游价值。", ["渠道流量波动", "自然与付费获客质量", "UTM 和来源口径排查"], ["流量来源分析", "质量与成本矩阵", "归因限制和优化建议"], ["user/session scope", "source、medium、campaign 规范", "新客、参与和落地页", "转化、收入和 LTV", "bot、direct 和跨域污染"], "不得比较不同 scope 的同名指标或把相关性写成增量贡献。"),
    spec("数据看板/业务分析/conversion-funnel-analyst", "conversion-funnel-analyst", "电商转化漏斗分析师", "analytics", "按一致人群、事件和时间窗定位从曝光到购买的转化损失。", ["商品或结账转化下降", "设备国家渠道漏斗比较", "改版和实验效果诊断"], ["漏斗诊断", "流失分层和证据", "实验与修复优先级"], ["漏斗定义和可比 cohort", "曝光、查看、加购、结账和购买", "设备、页面、国家和渠道", "性能、错误、支付和库存", "统计不确定性和实验"], "不得把不同人群的阶段比率拼成伪漏斗。"),
    spec("数据看板/业务分析/advertising-performance-analyst", "advertising-performance-analyst", "广告效果分析师", "analytics", "统一平台口径、公司收入和利润，分析广告效率、创意、受众和增量。", ["广告周报和预算复盘", "ROAS/ACOS 波动", "创意和投放结构诊断"], ["广告表现报告", "驱动拆解与预算建议", "增量验证和测试计划"], ["spend、delivery 和归因窗口", "CTR、CVR、CPA、ROAS 与 TACOS", "新客、毛利和回收期", "campaign、audience 和 creative", "平台偏差、饱和和增量"], "不得把平台归因 ROAS 等同于真实增量利润。"),
    spec("数据看板/业务分析/customer-cohort-ltv-analyst", "customer-cohort-ltv-analyst", "客户 Cohort 与 LTV 分析师", "analytics", "按获客 cohort、复购周期和贡献利润评估客户留存与长期价值。", ["复购和留存分析", "渠道客户质量比较", "CAC 回收和 LTV 预测"], ["cohort 留存表", "LTV/CAC 和回收期", "分层策略与不确定性"], ["客户身份与 cohort 定义", "复购、留存和间隔", "收入、毛利和贡献 LTV", "渠道、国家和首购商品", "截尾、退款和预测偏差"], "不得用尚未成熟 cohort 的短期收入直接外推长期 LTV。"),
    spec("数据看板/业务分析/inventory-supply-chain-analyst", "inventory-supply-chain-analyst", "库存与供应链分析师", "analytics", "量化可售、在途、缺货、周转、交期和履约，平衡服务水平与现金占用。", ["缺货和积压诊断", "库存健康周报", "供应商和物流绩效分析"], ["库存健康矩阵", "供需与交期驱动", "补货、处置和风险建议"], ["库存状态和位置", "需求、覆盖和安全库存", "供应商交期和波动", "入库、履约和缺货损失", "现金占用、老化和情景"], "不得把在途或不可售库存当成当前可售。"),
    spec("数据看板/业务分析/pricing-promotion-analyst", "pricing-promotion-analyst", "价格与促销分析师", "analytics", "评估价格、折扣和促销对销量、收入、利润、客户和库存的真实影响。", ["大促复盘", "价格调整效果", "优惠券和捆绑机制比较"], ["价格促销效果报告", "增量和蚕食测算", "机制优化建议"], ["基线和对照", "价格、折扣和实际成交价", "销量、转化和弹性", "毛利、补贴和贡献", "提前购买、蚕食和新客质量"], "不得用活动期同比增长直接宣称促销增量。"),
    spec("数据看板/业务分析/forecast-scenario-planner", "forecast-scenario-planner", "经营预测与情景规划师", "analytics", "用透明假设、驱动模型和区间管理销售、利润、库存和现金预测。", ["月度滚动预测", "预算和目标拆解", "乐观基准悲观情景"], ["驱动型预测模型", "情景和敏感性分析", "假设、预警和更新机制"], ["历史基线和结构变化", "流量、转化、价格和复购驱动", "季节、活动和供给约束", "区间、敏感性和误差", "版本、实际差异和滚动更新"], "不得提供没有假设、区间和回测的单点预测。"),
    spec("数据看板/数据治理/data-quality-reconciliation", "data-quality-reconciliation", "业务数据质量与对账专家", "analytics", "验证完整性、唯一性、及时性、一致性并解释跨系统差异。", ["平台与财务对账", "看板数据验收", "异常数据和口径争议"], ["数据质量报告", "差异桥和根因", "修复、监控和责任清单"], ["来源、抽取时间和范围", "主键、重复和缺失", "状态、时区、币种和税", "迟到、回补和快照", "容差、证据和 owner"], "不得用手工调平掩盖未解释差异。"),
    spec("数据看板/业务分析/marketplace-channel-comparison-analyst", "marketplace-channel-comparison-analyst", "跨平台渠道对比分析师", "analytics", "统一订单、收入、费用、广告和客户口径后比较平台与独立站真实表现。", ["Amazon、Shopify、TikTok 横向比较", "渠道资源分配", "渠道利润和客户质量评估"], ["渠道可比口径", "规模效率利润矩阵", "渠道角色和资源建议"], ["订单状态与收入确认", "平台费、履约、广告和退款", "新客、复购和数据 ownership", "库存和现金周期", "渠道特有价值与不可比项"], "不得直接比较平台后台同名指标或忽略不可比价值。"),
    # Enterprise product architecture by system.
    spec("互联网研发/产品/系统产品架构/公共/commerce-systems-product-architecture", "commerce-systems-product-architecture", "跨系统产品边界设计师", "product-system", "为贵司 OMS、IMS、OFS、CMS、WMS、TMS、CRM、PLM 建立业务能力分工、主数据归属、系统接口和端到端协作边界。", ["跨系统业务流程设计", "系统职责重叠与空白治理", "新系统接入和系统边界调整"], ["业务能力与系统责任地图", "主数据、状态与 source of truth 矩阵", "跨系统流程、交接契约与异常闭环"], ["端到端业务旅程", "系统负责与不负责范围", "主数据和 source of truth", "跨系统命令、事件与状态", "交接、SLA、对账、补偿和审计"], "只负责跨系统边界和协作，不替代 OMS、IMS、OFS 等单系统产品架构 Skill；不得先按现有菜单或部门直接划分系统。"),
    spec("互联网研发/产品/系统产品架构/OMS/oms-product-architecture", "oms-product-architecture", "OMS 产品架构师", "product-system", "围绕订单聚合、校验、路由、拆合、状态和售后设计订单管理产品架构。", ["全渠道 OMS 规划", "订单状态和异常治理", "OMS 与渠道、库存、履约集成"], ["OMS 能力地图", "订单域模型与状态机", "路由、异常和集成契约"], ["订单来源和统一模型", "价格、支付、风控和校验", "拆单、合单和路由", "取消、退款、退换和逆向", "OMS 与 IMS/OFS/CRM/财务边界"], "OMS 不直接替代库存台账、仓内作业或运输执行。"),
    spec("互联网研发/产品/系统产品架构/IMS/ims-product-architecture", "ims-product-architecture", "IMS 产品架构师", "product-system", "围绕库存台账、状态、位置、预占、释放和可售承诺设计库存管理产品架构。", ["多仓多渠道库存中心", "库存预占和超卖治理", "库存对账与可售计算"], ["IMS 能力地图", "库存账本和状态模型", "预占、同步、对账和异常方案"], ["SKU、库存位置和批次", "现货、在途、锁定和不可售", "预占、扣减、释放和补偿", "ATP/ATS 与渠道同步", "IMS 与 OMS/OFS/WMS 边界"], "IMS 不直接承担订单编排、仓内拣配或运输执行。"),
    spec("互联网研发/产品/系统产品架构/OFS/ofs-product-architecture", "ofs-product-architecture", "OFS 产品架构师", "product-system", "围绕履约承诺、履约单、节点编排、异常补偿和逆向设计订单履约产品架构。", ["跨仓跨渠道履约平台", "订单到交付编排", "履约异常和补偿治理"], ["OFS 能力地图", "履约单与状态机", "节点编排、SLA 和异常方案"], ["履约意图和履约单", "仓、店、供应商节点选择", "波次外部编排和状态推进", "缺货、超时、取消和补偿", "OFS 与 OMS/IMS/WMS/TMS 边界"], "OFS 不复制 OMS 交易订单，也不下沉承担仓库具体作业。"),
    spec("互联网研发/产品/系统产品架构/CMS/cms-product-architecture", "cms-product-architecture", "CMS 产品架构师", "product-system", "按贵司口径设计商品内容或通用内容的建模、版本、审批、本地化和渠道发布架构。", ["商品内容中台", "多语言多渠道内容治理", "内容版本审批和发布"], ["CMS 能力地图", "内容模型与版本机制", "审批、本地化和分发契约"], ["先确认 CMS 缩写和业务边界", "内容类型、字段和资产关系", "版本、草稿、审批和审计", "语言、市场和渠道覆盖", "CMS 与 PLM/PIM/渠道前台边界"], "不得在未确认贵司 CMS 含义时假定它只等于网页内容管理。"),
    spec("互联网研发/产品/系统产品架构/TMS/tms-product-architecture", "tms-product-architecture", "TMS 产品架构师", "product-system", "围绕承运商、线路、运价、运单、轨迹、费用和异常设计运输管理产品架构。", ["头程或尾程运输管理", "承运商和运费治理", "轨迹、异常和运费对账"], ["TMS 能力地图", "运输订单与状态机", "承运商、轨迹、费用和异常方案"], ["运输需求和运输订单", "承运商、服务和线路", "询价、比价、面单和交接", "轨迹、时效和异常", "计费、对账与 OMS/OFS/WMS 边界"], "TMS 不承担交易订单或仓内库存账本的主责。"),
    spec("互联网研发/产品/系统产品架构/CRM/crm-product-architecture", "crm-product-architecture", "CRM 产品架构师", "product-system", "围绕统一客户、同意偏好、互动、服务、分群和生命周期运营设计 CRM 产品架构。", ["跨渠道客户中心", "营销与客服 CRM", "客户 360 和生命周期运营"], ["CRM 能力地图", "客户身份与同意模型", "互动、分群、任务和集成方案"], ["客户身份合并与冲突", "同意、偏好和隐私请求", "订单、互动和服务视图", "分群、旅程和任务", "CRM 与 CDP/OMS/客服/营销工具边界"], "不得把无法证明为同一人的身份强行合并，也不得绕过同意使用数据。"),
    spec("互联网研发/产品/系统产品架构/PLM/plm-product-architecture", "plm-product-architecture", "PLM 产品架构师", "product-system", "围绕产品企划、设计、BOM、样品、成本、合规和版本门禁设计产品生命周期架构。", ["新品研发数字化", "款式/BOM/样品协同", "产品版本和上市门禁"], ["PLM 能力地图", "产品版本和阶段门模型", "BOM、样品、成本、合规与集成方案"], ["产品概念、款式和规格", "BOM、材料和供应商", "样品、测试和变更", "成本、合规和上市门禁", "PLM 与 CMS/PIM/ERP/供应链边界"], "PLM 不替代渠道商品内容发布或库存订单执行。"),
    spec("互联网研发/产品/系统产品架构/WMS/wms-product-architecture", "wms-product-architecture", "WMS 产品架构师", "product-system", "围绕入库、上架、库位、波次、拣选、复核、包装、盘点和仓内异常设计仓储管理产品架构。", ["多仓 WMS 规划", "仓内作业数字化", "库存差异和履约效率治理"], ["WMS 能力地图", "仓内任务与状态机", "作业、设备、异常和集成方案"], ["仓库、库区、库位和容器", "预约、收货、质检和上架", "波次、拣选、复核和包装", "移库、盘点、冻结和差异", "WMS 与 IMS/OFS/TMS/自动化设备边界"], "WMS 负责仓内实物作业，不成为企业级库存可售或交易订单的唯一事实源。"),
]

DEPRECATED_FRONTEND_SKILLS = {
    "javascript-frontend-architecture",
    "typescript-frontend-architecture",
    "react-frontend-architecture",
    "vue-frontend-architecture",
    "nextjs-frontend-architecture",
    "angular-frontend-architecture",
    "sveltekit-frontend-architecture",
}
SPECS = [item for item in SPECS if item["name"] not in DEPRECATED_FRONTEND_SKILLS]
SPECS.extend([
    spec("互联网研发/前端/框架/React/react-senior-expert", "react-senior-expert", "React 资深专家", "development-expert", "从架构、实现、状态、渲染性能、测试和演进角度解决复杂 React 工程问题。", ["React 复杂功能和架构设计", "React 性能或状态问题诊断", "React 代码评审、重构和技术升级"], ["React 方案与代码边界", "状态、渲染和性能决策", "测试、迁移和验证计划"], ["组件组合和领域边界", "本地、URL、表单与服务端状态", "副作用、并发渲染和错误恢复", "性能、可访问性和设计系统", "测试、依赖升级和渐进重构"], "不得默认使用全局状态、memo 或客户端渲染；必须从真实瓶颈和业务边界出发。"),
    spec("互联网研发/前端/框架/Vue3/vue3-senior-expert", "vue3-senior-expert", "Vue3 资深专家", "development-expert", "从架构、实现、响应式状态、性能、测试和演进角度解决复杂 Vue 3 工程问题。", ["Vue 3 复杂功能和架构设计", "响应式、状态或性能问题诊断", "Vue 代码评审、重构和版本升级"], ["Vue 3 方案与代码边界", "响应式、状态和性能决策", "测试、迁移和验证计划"], ["SFC、组件和 feature 边界", "Composition API 与 composable 设计", "响应式陷阱、Pinia 和服务端状态", "路由、性能、可访问性和设计系统", "测试、依赖升级和渐进重构"], "不得把共享逻辑全部塞入全局 store 或万能 composable，也不得混用未经约束的 Vue 2 模式。"),
    spec("互联网研发/前端/UI交互/ui-interaction-designer", "ui-interaction-designer", "UI 交互设计与实现专家", "ui-interaction", "把业务任务和界面结构转化为状态完整、反馈明确、可访问、可实现且可测试的 UI 交互规范。", ["新页面或组件交互设计", "复杂表单、列表、弹窗和工作流改版", "交互缺失、反馈不清或前端验收争议"], ["用户流程与交互说明", "组件状态、事件和反馈矩阵", "动效、可访问性、埋点和验收清单"], ["用户目标、入口、主路径和退出", "默认、悬停、焦点、禁用、加载、空、错误和成功状态", "鼠标、键盘、触摸、拖拽和响应式行为", "反馈层级、确认、撤销、恢复和防重复", "动效、无障碍、埋点、实现约束和测试场景"], "不得只画理想路径或用动效掩盖状态问题；交互不得破坏键盘操作、焦点顺序、可读性、用户控制和错误恢复。"),
])

for item in SPECS:
    if item["name"] == "frontend-architecture-designer":
        item["display"] = "前端架构师"
    elif item["name"] == "backend-architecture-designer":
        item["display"] = "后端架构师"
    elif item["path"].startswith("互联网研发/后端/语言/"):
        technology = Path(item["path"]).parts[-2]
        item["display"] = f"{technology} 后端资深专家"
        item["family"] = "development-expert"
    elif item["path"].startswith("互联网研发/后端/框架/"):
        framework = Path(item["path"]).parts[-2]
        item["display"] = f"{framework} 后端资深专家"
        item["family"] = "development-expert"

SPECS.extend([
    spec("互联网研发/产品/数据产品/label-governance-workflow-designer", "label-governance-workflow-designer", "标签治理与审核工作流设计师", "ai-product", "设计标签创建、修改、审核、发布、版本、回滚、权限、质量和血缘治理工作流。", ["透明计划等标签修改项目", "标签审核和发布流程", "标签冲突、版本和质量治理"], ["标签生命周期和状态机", "角色权限、审核与发布流程", "版本、审计、回滚和质量方案"], ["标签对象、taxonomy 和 owner", "草稿、审核、发布和废弃状态", "修改原因、diff 和影响范围", "权限、双人复核和批量操作", "版本、血缘、回滚和质量指标"], "不得覆盖历史标签或丢失修改证据；批量修改必须提供影响预览、审批、幂等和回滚。"),
    spec("精准营销/增长营销/拉新/customer-acquisition-growth-manager", "customer-acquisition-growth-manager", "新客获取与拉新增长经理", "operations", "围绕目标人群、获客渠道、首购路径和回收期设计可验证的新客增长系统。", ["新品或新市场拉新", "付费、自然、达人和推荐获客组合", "获客成本上升或新客质量下降诊断"], ["新客增长模型与渠道组合", "首触达到首购漏斗方案", "预算、实验、回收期和止损计划"], ["新客定义、排除和去重", "人群、需求和渠道任务", "创意、落地页和首购转化", "CAC、首单贡献和回收期", "归因、增量、欺诈和留存质量"], "不得把所有订单或平台新客直接视为增量新客，也不得用不可持续折扣和无回收期投放制造表面拉新。"),
    spec("创拍视觉/素材运营/creative-asset-operations-manager", "creative-asset-operations-manager", "创意素材运营经理", "creative-production", "建立跨商品、市场、渠道和投放场景的素材需求、生产、标签、版本、授权、分发和效果回流体系。", ["素材中台和资产库治理", "多渠道素材供给与复用", "素材版本、授权和效果复盘"], ["素材分类与需求地图", "生产排期、命名、版本和权限规范", "分发、效果标签和淘汰复用机制"], ["商品事实、市场和使用场景", "格式、尺寸、语言和渠道规格", "素材 ID、标签、版本和血缘", "肖像、音乐、字体和地域授权", "投放表现、疲劳、复用和归档"], "不得让无来源、过期授权或无法追溯产品版本的素材上线；素材效果必须按可比渠道、受众和投放条件解释。"),
    spec("创拍视觉/拍摄制作/product-photo-video-production-manager", "product-photo-video-production-manager", "商品图片与视频拍摄制作经理", "creative-production", "把营销目标、商品事实和渠道规范转化为可执行的图片与视频拍摄、后期、验收和交付计划。", ["商品主图、场景图和视频拍摄", "广告、社媒、达人和独立站素材制作", "跨市场拍摄重制与批量交付"], ["拍摄策略、shot list 和脚本", "人员、场地、样品、预算与排期", "后期、合规、质检和交付清单"], ["受众、卖点和证据镜头", "主图、细节、场景、UGC 和短视频格式", "样品、模特、场地、灯光和收音", "分镜、镜头、字幕、音乐和 CTA", "色差、真实性、授权、命名和多规格交付"], "不得通过后期改变产品关键事实、尺寸、颜色或效果；模特、场地、音乐、字体和用户内容必须有明确授权范围。"),
    spec("创拍视觉/拍摄统筹/shooting-production-coordinator", "shooting-production-coordinator", "拍摄制片与现场统筹", "creative-production", "把创意方案转化为预算、排期、样品、人员、场地、设备、通告和现场执行计划。", ["棚拍或外景拍摄筹备", "多 SKU 批量拍摄", "跨团队拍摄进度和成本治理"], ["制作预算与排期", "人员、样品、场地和设备清单", "通告单、现场流程和异常预案"], ["brief、shot list 和优先级", "样品状态、道具和物流", "摄影、导演、模特和供应商", "场地、设备、保险和安全", "call sheet、备份、成本和交付节点"], "不得在缺少场地、肖像、未成年人、安全或商业使用授权时开拍；现场变更必须记录对预算、范围和交付的影响。"),
    spec("创拍视觉/商品摄影/product-photography-director", "product-photography-director", "商品摄影导演", "creative-production", "以真实还原商品和渠道转化任务为目标，设计主图、细节、场景、模特和对比图片的摄影方案。", ["Amazon 或独立站商品摄影", "新品主图与场景图拍摄", "多颜色多款式批量摄影"], ["商品摄影 brief 与 shot list", "灯光、构图、色彩和场景方案", "选片、真实性和渠道验收清单"], ["商品结构、材质、颜色和比例", "白底、细节、尺度和使用场景", "灯光、镜头、构图和景深", "模特姿态、道具和文化语境", "色彩管理、修图边界和渠道规范"], "不得通过透视、合成或修图夸大尺寸、材质、功能和效果；关键颜色与结构必须建立实物对照和可复核标准。"),
    spec("创拍视觉/短视频制作/short-form-video-producer", "short-form-video-producer", "跨境短视频制作导演", "creative-production", "面向广告、TikTok、Reels、Shorts 和商品页设计高密度、平台原生、可测试的短视频。", ["商品广告短视频", "社媒竖屏内容", "功能演示、场景故事和口播制作"], ["视频角度与脚本矩阵", "分镜、镜头、字幕和声音方案", "版本测试、平台规格和验收清单"], ["首秒钩子和目标人群", "问题、证据、演示和 CTA", "9:16 构图、节奏和安全区", "口播、字幕、音乐和无声观看", "变量编码、版本差异和完播转化指标"], "不得伪造演示、评价或前后对比；音乐、字体、素材和人物必须具备对应平台、地域、期限和商业用途授权。"),
    spec("创拍视觉/UGC制作/ugc-content-production-manager", "ugc-content-production-manager", "UGC 与达人内容制作经理", "creative-production", "管理创作者匹配、内容 brief、寄样、脚本边界、拍摄反馈、授权和交付，生产可信的原生用户内容。", ["UGC 广告素材采购", "达人寄样内容制作", "多创作者多角度内容测试"], ["创作者画像与筛选表", "UGC brief、脚本边界和反馈流程", "授权、交付、版本和表现复盘"], ["受众与创作者匹配", "真实体验和产品证据", "自然表达、钩子和镜头要求", "寄样、时间、费用和修改轮次", "广告披露、肖像内容授权和白名单投放"], "不得要求创作者伪装未发生的体验或隐藏商业关系；必须书面明确内容所有权、使用地域、期限、渠道、剪辑和投放权限。"),
    spec("创拍视觉/后期交付/post-production-delivery-manager", "post-production-delivery-manager", "剪辑后期与素材交付经理", "creative-production", "管理选片、剪辑、调色、修图、声音、字幕、包装、多语言版本、质检和多规格交付。", ["图片精修和批量导出", "短视频剪辑与多版本适配", "跨语言跨渠道素材交付"], ["后期任务与版本矩阵", "修图剪辑、字幕和声音规范", "质检、命名、归档和交付清单"], ["原始素材、选片和时间线", "调色、修图和事实还原", "节奏、声音、字幕和图形包装", "语言、比例、码率和渠道规格", "版本、反馈、授权、质检和归档"], "不得使用后期掩盖产品缺陷或改变关键事实；生成式填充、合成和 AI 修改必须可追溯并按渠道与合规要求披露或限制。"),
    spec("创拍视觉/AI创意制作/虚拟模特/virtual-model-content-producer", "virtual-model-content-producer", "虚拟模特内容制作专家", "ai-creative-production", "使用合规的人像生成、模特替换或虚拟试穿工具制作跨人群商品内容，并严格保持商品结构与真实属性。", ["服饰、配件和生活方式虚拟模特图", "多地区模特与场景版本", "真人素材的合规模特替换"], ["虚拟模特制作 brief", "身份、姿态、商品一致性和版本方案", "真实性、授权、偏差和交付验收报告"], ["商品版型、纹理、颜色和遮挡", "人物身份、年龄表达、体型和肤色覆盖", "姿态、手部、接触点和物理合理性", "输入人像、肖像权和训练使用授权", "跨版本一致性、合成披露和失败样本"], "不得未经授权复刻真实人物、名人或未成年人；不得改变商品版型、颜色、纹理、尺寸关系和功能效果，无法验证时必须标记为概念图。"),
    spec("创拍视觉/AI创意制作/AIGC制作/ai-image-video-production-manager", "ai-image-video-production-manager", "AIGC 创意制作专家", "ai-creative-production", "把商品事实、品牌规范、脚本和参考素材编排为可追溯的文生图、图生图、文生视频、图生视频、局部修改、批量变体与成片交付流程。", ["AIGC 商品场景图和广告图", "文生图、图生图、文生视频和图生视频", "多语言、多比例和多创意变量批量成片"], ["AIGC 创意方案与模型路由", "提示词、参考、参数、生成和修改血缘", "候选筛选、人工修正、版本矩阵和交付质检包"], ["商品事实锁定与参考图", "模型、输入输出、参数和随机种", "构图、文字、镜头连续性和物理合理性", "品牌、人物、版权和必要披露", "成本、时延、失败回退和人工验收"], "不得把生成结果当作真实拍摄证据；关键商品特征、文字、标识、人物和声明必须逐项人工核验，并保留输入、模型、参数与修改血缘。"),
    spec("创拍视觉/AI创意制作/智能打标/creative-asset-intelligent-tagging-specialist", "creative-asset-intelligent-tagging-specialist", "创意素材智能打标专家", "creative-tagging", "为贵司图片、视频和广告素材库设计并运行从素材输入、模型推理、标签建议、人审反馈、CMS/DAM 回写到持续评估的可治理 AI 打标闭环。", ["存量图片视频批量打标", "新素材入库自动标签建议", "AI 打标工具规划、标签补全、纠错、搜索和效果归因治理"], ["AI 打标能力、用户流程与标签体系", "模型、置信度、人审决策和批量回写方案", "金标评估、监控、错误集、版本、回滚和演进报告"], ["素材来源、权限、权利和版本", "标签 taxonomy、定义、互斥、依赖、敏感等级和 owner", "模型、API、置信度、成本、时延和候选策略", "人工确认、拒绝、修改、批量处理和状态机", "金标集、离线指标、线上抽样、一致性、漂移和反馈学习", "CMS/DAM 回写、搜索、效果归因、审计和标签版本"], "不得把模型标签直接当作事实；人物身份、敏感属性、商品关键属性和低置信度结果必须人工复核，批量回写必须可预览、审计和回滚。"),
    spec("创拍视觉/AI创意制作/智能剪辑/intelligent-video-editing-specialist", "intelligent-video-editing-specialist", "智能剪辑工作流专家", "ai-creative-production", "利用镜头识别、语音转写、节奏分析、自动重构和批量渲染工具提升粗剪、多版本与本地化交付效率。", ["长素材自动粗剪", "广告短视频批量变体", "字幕、配音、横竖版和多语言适配"], ["智能剪辑规则与时间线方案", "镜头、字幕、声音和版本矩阵", "人工复核、质量门禁和批量交付记录"], ["素材入库、镜头语义和优先级", "转写、说话人、字幕和敏感词", "节奏、静音、重复和 CTA", "画幅重构、主体跟踪和安全区", "音乐版权、语言质检、渲染和回退"], "自动剪辑不得跳过事实、字幕、肖像、版权和品牌人工复核；不得让模型自动删除改变原意的必要上下文。"),
    spec("创拍视觉/AI创意制作/真实性合规/ai-creative-authenticity-compliance-reviewer", "ai-creative-authenticity-compliance-reviewer", "AI 创意真实性与合规审查师", "ai-creative-production", "审查 AI 生成、替换、扩展和智能剪辑内容的商品真实性、人物权利、版权、披露、平台和证据要求。", ["AI 商品图视频上线前审查", "虚拟模特和数字人风险检查", "AI 素材来源、修改和披露审计"], ["AI 创意逐项审查表", "失真、权利和平台风险分级", "修改、披露、留档和禁止上线清单"], ["商品事实与生成差异", "人像、声音、肖像和深度合成", "版权、商标、字体和训练来源", "广告声明、误导和平台政策", "内容凭证、模型版本、人工修改和审批证据"], "不得仅凭视觉自然就认定合规；无法证明商品真实性、人物授权、版权来源或必要披露的内容必须暂停上线并升级法务或平台合规人员。"),
    spec("仓储库存/入库管理/warehouse-inbound-operations-manager", "warehouse-inbound-operations-manager", "仓库入库作业经理", "warehouse-operations", "管理预约、到货、卸货、收货、质检交接、差异、上架和库存状态生效的入库闭环。", ["采购或调拨入库", "多仓预约和上架治理", "短少、破损、错货和超收异常处理"], ["入库 SOP 与状态图", "预约、收货、差异和上架任务表", "SLA、证据、异常和对账清单"], ["ASN、采购单、调拨单和到货", "箱、托、SKU、批次和序列", "计数、质检、短溢损和拒收", "暂存、上架、库位和状态生效", "IMS/WMS/采购/财务对账和证据"], "不得在未完成数量、质量和差异记录时直接转为可售；实物、单据和系统状态不一致必须隔离并升级。"),
    spec("仓储库存/出库履约/warehouse-outbound-fulfillment-manager", "warehouse-outbound-fulfillment-manager", "仓库出库履约经理", "warehouse-operations", "管理订单释放、波次、拣选、复核、包装、称重、面单、交接和出库确认。", ["电商订单出库", "大促波次与仓内产能", "错发、漏发、超时和承运交接异常"], ["出库流程与波次方案", "拣配复核包装标准", "产能、SLA、异常和交接报告"], ["订单优先级、截单和释放", "波次、路径、拣选和缺货", "复核、包装、赠品和称重", "面单、装车、交接和出库状态", "错漏发、取消拦截、证据和追责"], "不得为追求出库量跳过复核、称重、安全包装或取消拦截；系统出库必须与实物交接证据一致。"),
    spec("仓储库存/库存控制/inventory-control-cycle-count-manager", "inventory-control-cycle-count-manager", "库存控制与循环盘点经理", "warehouse-operations", "建立库存账实准确、循环盘点、冻结、差异调查、调整审批和损耗治理机制。", ["日常循环盘点", "月末或年度盘点", "库存差异、负库存和异常损耗治理"], ["盘点策略与计划", "账实差异和根因报告", "调整审批、控制和持续改善清单"], ["库存所有权、位置、状态和批次", "ABC/风险盘点频率", "冻结、盲盘、复盘和抽查", "收发、移库、退货和系统时序根因", "调整权限、证据、损耗和审计轨迹"], "不得无证据调平库存或由同一人完成保管、盘点、审批和调整；重大差异必须冻结、保全和独立复核。"),
    spec("仓储库存/库存分配/inventory-allocation-planner", "inventory-allocation-planner", "多仓多渠道库存分配规划师", "warehouse-operations", "按需求、服务水平、利润、交期、仓容和调拨成本分配多仓多渠道可用库存。", ["Amazon、独立站和 TikTok 库存分配", "多仓调拨和缺货配给", "大促、新品和区域备货"], ["库存分配规则与配额", "仓渠道调拨计划", "服务、成本、缺货和风险情景"], ["现货、在途、预占和不可售", "渠道需求、承诺和优先级", "仓网、时效、成本和容量", "安全库存、配额和公平性", "调拨、同步、超卖和回收规则"], "不得把在途、锁定、残次或未入库库存分配为可售；分配决策必须保留服务、利润与缺货取舍。"),
    spec("仓储库存/逆向物流/returns-reverse-logistics-manager", "returns-reverse-logistics-manager", "退货与逆向物流经理", "warehouse-operations", "管理退货授权、运输、收货、检验、分级、退款证据、翻新、再售、报废和供应商追偿。", ["客户退货处理", "平台退仓和批量逆向", "残次、翻新、再售与报废治理"], ["逆向流程与状态机", "检验分级和处置标准", "退款、库存、追偿和根因报告"], ["RMA、订单、原因和责任", "运输、收货、身份和完整性", "检验、分级、清洁和翻新", "退款、可售、残次、报废和销毁", "欺诈、产品安全、数据清除和根因闭环"], "不得未经检验把退货恢复可售；涉及安全、卫生、个人数据或召回的商品必须隔离并按专项规则处置。"),
    spec("仓储库存/仓容安全/warehouse-safety-capacity-manager", "warehouse-safety-capacity-manager", "仓容、现场安全与连续性经理", "warehouse-operations", "管理仓容、库位、动线、设备、人员安全、消防、危险品、峰值产能和业务连续性。", ["新仓或仓库扩容", "大促峰值仓容与人效规划", "仓库安全检查和中断应急"], ["仓容与产能模型", "现场安全和检查清单", "峰值、故障、灾害和恢复预案"], ["库位、容积、重量和周转", "收发存动线与人车分离", "设备、消防、用电和人体工学", "危险品、受控品和区域隔离", "峰值人力、停电系统故障和替代仓"], "不得用效率目标突破消防、承重、设备、劳动和危险品安全限制；具体法定要求必须由当地合格人员确认。"),
    spec("市场采购/市场机会/market-demand-opportunity-analyst", "market-demand-opportunity-analyst", "市场需求与商品机会分析师", "market-procurement", "把消费者需求、搜索、竞品、价格带、渠道和利润证据转化为可验证的采购商品机会。", ["新品机会扫描", "类目和价格带进入判断", "采购方向和商品组合规划"], ["市场机会与证据表", "需求、竞争和利润评分", "样品验证、否决条件和决策计划"], ["目标人群、场景和未满足需求", "搜索、销量、评价和季节证据", "竞争、价格带和差异空间", "目标成本、毛利和现金周期", "合规、供应可行性、反证和试点门槛"], "不得以平台热度或单一竞品销量直接证明采购机会；必须验证真实需求、可持续利润、供应和合规可行性。"),
    spec("市场采购/样品验证/sample-evaluation-sourcing-manager", "sample-evaluation-sourcing-manager", "采购样品验证经理", "market-procurement", "管理打样需求、样品版本、功能外观评估、成本、测试、用户验证和量产放行证据。", ["新品打样和多供应商比样", "样品改版和确认", "量产前样、封样和放行"], ["样品需求与版本台账", "比样、测试和问题矩阵", "修改、封样、量产和否决决定"], ["规格、BOM、外观和使用场景", "供应商、版本、日期和样品身份", "功能、耐久、安全和包装测试", "目标成本、可制造性和公差", "问题关闭、黄金样、签核和变更控制"], "不得凭主观外观或单个样品直接量产；关键规格、测试、缺陷和版本必须可追溯并经授权角色签核。"),
    spec("市场采购/商务谈判/supplier-negotiation-cost-manager", "supplier-negotiation-cost-manager", "供应商谈判与成本经理", "market-procurement", "基于成本结构、需求承诺、产能、质量、交期、付款和风险设计供应商商务谈判。", ["询价比价和成本拆解", "MOQ、价格、账期和交期谈判", "年度降本和供应商商务复盘"], ["报价可比表与成本模型", "谈判目标、底线和换项方案", "商务条款、决策和复盘记录"], ["规格、数量和报价可比性", "材料、人工、制造、包装和物流", "MOQ、阶梯价、模具和开发费", "付款、汇率、交期、赔付和质保", "替代供应、总拥有成本和关系风险"], "不得以压价替代成本、质量和交付分析；不得作出超授权数量、排他、付款或长期承诺。"),
    spec("市场采购/采购执行/purchase-order-delivery-manager", "purchase-order-delivery-manager", "采购订单与交付经理", "market-procurement", "管理采购申请、订单、确认、预付款、生产、质检、交付、变更、异常和关闭。", ["采购订单下达", "生产和交期跟踪", "数量价格交付变更与异常处理"], ["采购订单与里程碑台账", "交期、质量和付款跟踪", "变更、索赔、关闭和供应商绩效记录"], ["申请、预算、合同和审批", "SKU、规格、数量、价格和币种", "生产、质检、装运和到仓节点", "付款条件、单据和三方匹配", "变更、短交、延期、索赔和关闭"], "不得在缺少授权、规格、价格、交付或付款条件时下单；订单变更必须保留原版本、影响、批准和供应商确认。"),
    spec("市场采购/采购风险/procurement-risk-compliance-manager", "procurement-risk-compliance-manager", "采购风险与供应韧性经理", "market-procurement", "识别供应商、产地、材料、质量、合规、制裁、集中度、产能、灾害和商业连续性风险。", ["新供应商准入", "单一来源和供应中断治理", "采购合规与供应链尽调"], ["采购风险与责任矩阵", "供应商尽调和证据缺口", "替代来源、缓解、监控和升级计划"], ["主体、所有权和经营资质", "产地、材料、劳工和环境证据", "制裁、出口管制和产品合规", "产能、质量、财务和集中度", "备选供应、模具数据权利和退出连续性"], "不得把供应商自我声明当作充分证据；制裁、强迫劳动、重大质量或产品安全红旗必须暂停并升级法务与合规人员。"),
])

ROLE_DEFS = [
    ("客服售前/客服角色", "客服售前高级经理", "senior-customer-service-presales-manager", "客服售前高级经理", "统筹跨渠道售前咨询、商品推荐、多语言沟通、知识库、线索分级、质检培训和销售交接。", ["咨询量、响应和解决质量", "商品事实、推荐适配和转化", "多语言体验与合规", "知识库、质检和团队能力", "线索、销售交接和客户声音"]),
    ("渠道运营/运营角色", "跨境电商负责人", "senior-cross-border-commerce-leader", "跨境电商业务负责人", "统筹公司跨境业务战略、渠道组合、商品、增长、供应链、客户体验、利润和组织节奏。", ["战略与经营模型", "渠道和资源组合", "商品与品牌组合", "收入、利润、现金和风险", "跨团队目标、决策和复盘"]),
    ("渠道运营/运营角色", "亚马逊运营高级经理", "senior-amazon-operations-manager", "亚马逊运营高级经理", "对 Amazon 账户健康、商品、搜索、转化、广告、库存、价格、评价和利润承担端到端经营责任。", ["账户与合规健康", "目录、搜索和转化", "广告、促销和价格", "FBA 库存、补货和利润", "团队节奏和问题闭环"]),
    ("渠道运营/运营角色", "独立站运营高级经理", "senior-dtc-operations-manager", "独立站运营高级经理", "对独立站商品、内容、获客、转化、客单、复购、技术健康和贡献利润承担端到端责任。", ["商品与站点体验", "流量组合与落地页", "转化、客单和复购", "数据、技术和隐私健康", "贡献利润和增长实验"]),
    ("渠道运营/运营角色", "TikTok-Shop运营高级经理", "senior-tiktok-shop-operations-manager", "TikTok Shop 运营高级经理", "统筹 TikTok Shop 商品、内容、直播、达人、广告、活动、履约和店铺健康。", ["店铺与商品健康", "短视频和直播供给", "达人、联盟和授权", "广告、活动和 GMV 质量", "履约、退款、评分和利润"]),
    ("市场采购/采购角色", "选品与商品高级经理", "senior-merchandising-manager", "选品与商品高级经理", "统筹市场机会、选品验证、商品组合、生命周期、目标成本、上市准备和退出机制。", ["市场机会和需求证据", "选品门槛与单位经济", "SKU 组合和生命周期", "目标成本、样品和上市准备", "库存风险和退出机制"]),
    ("精准营销/营销角色", "品牌与内容高级经理", "senior-brand-content-manager", "品牌与内容高级经理", "统筹品牌定位、产品证据、内容体系、创意资产、社媒表达和多市场一致性。", ["品牌定位和信息支柱", "内容主题与用户旅程", "创意生产和资产治理", "社媒、SEO、GEO 和分发", "多语言、合规和品牌衡量"]),
    ("精准营销/营销角色", "增长营销高级经理", "senior-growth-marketing-manager", "增长营销高级经理", "统筹付费、自然、达人、邮件和活动增长，对获客质量、转化、留存和贡献利润负责。", ["增长模型和机会树", "渠道预算与获客质量", "创意、落地页和转化", "留存、LTV 和回收期", "归因、增量和实验组合"]),
    ("精准营销/营销角色", "用户运营高级经理", "senior-user-operations-manager", "用户运营高级经理", "统筹用户分层、生命周期、邮件触达、购后体验、会员、召回、推荐和客户价值增长。", ["用户身份、同意和分层", "生命周期旅程和触达编排", "购后、复购、召回和会员", "LTV、留存和贡献利润", "体验、频控、实验和跨团队协同"]),
    ("创拍视觉/创意角色", "创拍视觉高级经理", "senior-creative-production-manager", "创拍视觉高级经理", "统筹创意策略、制片、摄影、短视频、UGC、后期、素材资产、预算和生产质量。", ["创意需求和产能组合", "策略、脚本和拍摄优先级", "人员、供应商、预算和排期", "真实性、授权、品牌和质量", "素材交付、复用和效果回流"]),
    ("仓储库存/仓储角色", "供应链高级经理", "senior-supply-chain-manager", "供应链高级经理", "统筹供应商、质量、采购、库存、仓储、运输、履约和供应链现金风险。", ["供应商和质量体系", "需求、采购和补货", "库存、仓储和渠道分配", "物流、履约和异常", "成本、现金、SLA 和韧性"]),
    ("仓储库存/仓储角色", "仓储库存高级经理", "senior-warehouse-inventory-manager", "仓储库存高级经理", "统筹多仓库存准确性、入出库、库内作业、库存分配、退货逆向、仓容安全、成本和履约 SLA。", ["库存准确性与可用性", "入库、上架、拣配和出库", "库位、仓容、人效和设备", "渠道分配、缺货和老化", "安全、异常、成本和持续改善"]),
    ("市场采购/采购角色", "市场采购高级经理", "senior-market-procurement-manager", "市场采购高级经理", "统筹市场机会、选品组合、供应商、样品、目标成本、谈判、采购订单、交期、质量和采购风险。", ["市场机会与商品组合", "供应商与产能质量", "样品、成本和商务谈判", "采购订单、交期和现金", "合规、集中度和供应风险"]),
    ("渠道运营/运营角色", "客户体验高级经理", "senior-customer-experience-manager", "客户体验高级经理", "统筹多语言客服、售后、评价、声誉、VOC、留存和客户体验改进。", ["全旅程体验和服务标准", "客服 SLA、权限和质检", "退款退货和异常升级", "评价、声誉和 VOC 根因", "留存、忠诚度和改进闭环"]),
    ("渠道运营/运营角色", "业务数据分析高级经理", "senior-business-analytics-manager", "业务数据分析高级经理", "统筹指标治理、数据质量、经营分析、专项诊断、预测和管理层决策支持。", ["指标语义和数据质量", "经营、利润和现金分析", "商品、渠道和客户分析", "预测、情景和目标差距", "结论质量、决策和分析资产"]),
]

BUSINESS_ROLE_NAMES = {
    "senior-customer-service-presales-manager": "客服售前资深经理",
    "senior-cross-border-commerce-leader": "跨境电商资深经理",
    "senior-amazon-operations-manager": "亚马逊运营资深经理",
    "senior-dtc-operations-manager": "独立站运营资深经理",
    "senior-tiktok-shop-operations-manager": "TikTok Shop 运营资深经理",
    "senior-merchandising-manager": "选品与商品资深经理",
    "senior-brand-content-manager": "品牌与内容资深经理",
    "senior-growth-marketing-manager": "增长营销资深经理",
    "senior-user-operations-manager": "用户运营资深经理",
    "senior-creative-production-manager": "创拍视觉资深经理",
    "senior-supply-chain-manager": "供应链资深经理",
    "senior-warehouse-inventory-manager": "仓储库存资深经理",
    "senior-market-procurement-manager": "市场采购资深经理",
    "senior-customer-experience-manager": "客户体验资深经理",
    "senior-business-analytics-manager": "业务数据分析资深经理",
}
ROLE_DEFS = [
    (area, BUSINESS_ROLE_NAMES.get(role_id, folder), role_id, BUSINESS_ROLE_NAMES.get(role_id, display), positioning, lenses)
    for area, folder, role_id, display, positioning, lenses in ROLE_DEFS
]

for role_area, folder, role_id, display, positioning, lenses in ROLE_DEFS:
    if role_area.startswith("创拍视觉/"):
        role_family = "creative-role"
    elif role_area.startswith("客服售前/"):
        role_family = "customer-presales-role"
    elif role_area.startswith("仓储库存/"):
        role_family = "warehouse-role"
    elif role_area.startswith("市场采购/"):
        role_family = "market-procurement-role"
    else:
        role_family = "role"
    SPECS.append(spec(
        f"{role_area}/{folder}/{role_id}", role_id, display, role_family,
        positioning,
        [f"由{display}接管复杂经营任务", "制定季度或月度计划", "跨专项协同、经营诊断和复盘"],
        ["角色经营目标与责任边界", "专项 Skill 编排与决策", "经营节奏、风险和团队行动计划"],
        lenses,
        "主角色负责目标、取舍、编排和验收，不替代专项 Skill 的深度执行，也不得越过授权直接操作生产账户。",
    ))
    SPECS.append(spec(
        f"{role_area}/{folder}/{role_id}-weekly-report", f"{role_id}-weekly-report", f"{display}周报", "weekly",
        f"基于真实经营证据生成{display}视角的结论先行周报，并跟踪目标、驱动、风险、决策和责任闭环。",
        [f"{display}本周经营复盘", "本周与上周或目标对比", "管理层同步和跨团队行动跟踪"],
        ["角色经营周报", "指标变化和驱动解释", "风险、决策与下周行动表"],
        lenses,
        "不得混淆本周对上周、同比或累计口径；不得虚构数据、成果、责任人或完成状态。",
    ))

SPECS.extend([
    spec("法律政务/法律角色/跨境法务负责人/senior-cross-border-legal-counsel", "senior-cross-border-legal-counsel", "跨境法务负责人", "role", "统筹跨境合同、监管、知识产权、隐私、营销、用工、争议和公司治理风险。", ["跨境法务体系建设", "重大项目法律风险评审", "外部律师、证据和决策协调"], ["法律风险组合与优先级", "专项法律 Skill 编排", "决策、升级律师和治理计划"], ["司法辖区和主体", "权利义务与授权", "监管、消费者和平台风险", "证据、时效和争议", "外部律师升级与整改闭环"], "本 Skill 不构成律师法律意见；高风险、争议或司法辖区不明事项必须升级合格律师。"),
    spec("法律政务/法律角色/跨境法务负责人/senior-cross-border-legal-counsel-weekly-report", "senior-cross-border-legal-counsel-weekly-report", "跨境法务负责人周报", "weekly", "基于真实案件、合同和监管证据生成法务周报。", ["法务周度复盘", "重大风险与案件升级", "合同、合规和整改跟踪"], ["法务周报", "风险与时效台账", "决策、外部律师和下周行动"], ["新增与关闭事项", "风险等级和金额暴露", "期限、证据和保全", "业务影响与整改", "待决策和外部律师事项"], "不得披露超出授权的特权或敏感信息，不得虚构案件状态或法律结论。"),
    spec("法律政务/跨境监管/cross-border-regulatory-compliance-counsel", "cross-border-regulatory-compliance-counsel", "跨境监管合规顾问", "legal", "按销售国、主体、产品、渠道和责任链识别跨境贸易与电商监管义务。", ["进入新国家或平台", "进口商、卖家和平台责任审查", "监管变化与整改"], ["适用法规和责任矩阵", "证据缺口与风险等级", "整改、监控和律师升级方案"], ["司法辖区与经营主体", "产品、进口和市场准入", "消费者、平台和信息披露", "海关、制裁和供应链证据", "更新日期、主管机关和升级门槛"], "不得用一个国家的规则外推其他市场；执行前必须核实当前官方法规。"),
    spec("法律政务/进出口合规/import-export-trade-compliance-reviewer", "import-export-trade-compliance-reviewer", "进出口贸易合规审查顾问", "legal", "对跨境货物流的进口、出口、再出口、海关、制裁与出口管制责任进行证据化审查。", ["新品或新国家进出口审查", "报关资料和责任链复核", "制裁、许可证或出口管制红旗处理"], ["进出口合规审查报告", "商品、主体、路线和责任矩阵", "证据缺口、暂停条件和专业升级清单"], ["出口方、进口商和最终受益人", "商品描述、HS、原产地和估价", "目的地、最终用户和最终用途", "许可证、禁限运与主管机关", "报关、运输、付款、筛查和记录保存"], "不得代替报关行、分类专家或执业律师作最终申报；分类、原产地、估价、制裁命中和许可证不明时必须暂停并升级。"),
    spec("法律政务/美国合规/us-market-regulatory-compliance-counsel", "us-market-regulatory-compliance-counsel", "美国市场合规顾问", "legal", "按产品、进口模式、销售州和营销行为识别美国联邦、州及主管机构合规责任。", ["产品进入美国市场", "美国进口商和平台责任审查", "Listing、标签、广告、隐私和召回流程审查"], ["美国适用规则与主管机构地图", "进口、产品和销售责任矩阵", "证据缺口、整改和美国律师升级方案"], ["Importer of Record 与海关申报", "HTS、原产地、估价和供应链", "CPSC/FDA/FCC 等产品主管机构路由", "FTC 广告、评价和消费者保护", "州级隐私、标签和执法差异"], "美国规则依产品和州而异；不得把平台准入等同于政府合规，也不得在未核实当前联邦和州规则时批准上市。"),
    spec("法律政务/欧盟合规/eu-market-regulatory-compliance-counsel", "eu-market-regulatory-compliance-counsel", "欧盟市场合规顾问", "legal", "按产品法规、经济运营商、成员国、销售渠道和数据流识别欧盟市场准入与持续合规责任。", ["产品进入欧盟市场", "欧盟责任人、进口商和平台责任审查", "CE、GPSR、标签、VAT、隐私和召回流程审查"], ["欧盟法规与角色责任地图", "技术文件、标签和线上展示证据清单", "缺口、整改、监控和欧盟专业升级方案"], ["制造商、进口商、授权代表和责任人", "GPSR、CE 与产品专项法规路由", "风险评估、技术文件、测试和追溯", "标签、语言、线上要约和召回", "VAT/IOSS、GDPR、消费者和成员国差异"], "不得以 CE 标识或单份测试报告替代完整合规评估；必须确认适用法规、经济运营商和成员国要求的当前版本。"),
    spec("法律政务/知识产权/intellectual-property-protection-counsel", "intellectual-property-protection-counsel", "知识产权保护顾问", "legal", "管理商标、版权、专利、外观设计、域名、授权链和平台侵权处置。", ["品牌和新品 IP 清查", "素材和达人内容授权", "侵权投诉、应诉和证据保全"], ["IP 资产与权利链台账", "侵权/被诉风险分析", "申请、许可、取证和处置计划"], ["权利类型与国家覆盖", "所有权、许可和使用证据", "近似、混淆和在先权利", "平台程序和反通知", "期限、保全和律师升级"], "不得在无权利证明时发起投诉，也不得把平台处理结果等同于法院结论。"),
    spec("法律政务/隐私与数据/privacy-data-protection-counsel", "privacy-data-protection-counsel", "隐私与数据保护顾问", "legal", "审查个人数据、Cookie、营销同意、供应商处理、跨境传输、数据主体请求和事件响应。", ["网站与 CRM 隐私审查", "数据出境和供应商合同", "删除访问请求或数据事件"], ["数据处理活动与角色图", "合法基础、告知和传输差距", "整改、请求和事件响应方案"], ["数据类型、目的和主体", "controller/processor 与合法基础", "同意、Cookie 和营销偏好", "保留、权限和数据主体权利", "跨境传输、供应商和事件通知"], "不得把隐私政策文本当作实际合规证明；必须核对真实数据流和当前司法辖区规则。"),
    spec("法律政务/广告与消费者保护/advertising-claims-legal-reviewer", "advertising-claims-legal-reviewer", "广告声明法律审查师", "legal", "审查产品声明、比较广告、折扣、评价、达人背书、环保和健康表达的证据与披露。", ["Listing、落地页和广告上线前审查", "达人、评价和促销机制", "高风险产品声明整改"], ["声明逐条证据矩阵", "风险等级与修改稿", "披露、审批和留档要求"], ["明示和暗示声明", "可靠证据与适用人群", "达人关系和显著披露", "评价、折扣和参照价", "健康、环保、产地和儿童声明"], "不得用免责声明修复核心误导，也不得批准缺少可靠证据的客观声明。"),
    spec("法律政务/劳动用工/employment-labor-compliance-counsel", "employment-labor-compliance-counsel", "劳动用工合规顾问", "legal", "审查员工、独立承包商、远程团队、薪酬工时、保密知识产权和离职流程风险。", ["跨国招聘与用工模式", "员工或承包商协议", "绩效、调查和离职处理"], ["用工分类与义务矩阵", "合同和流程风险", "整改、证据和律师升级清单"], ["工作地与雇佣主体", "员工/承包商分类", "薪酬、工时、福利和税", "保密、IP、监控和隐私", "调查、纪律、终止和记录"], "不得跨司法辖区套用同一劳动模板；解雇、歧视或集体事项必须升级当地律师。"),
    spec("法律政务/争议解决/dispute-resolution-case-manager", "dispute-resolution-case-manager", "争议解决案件经理", "legal", "组织合同、平台、客户、供应商和知识产权争议的事实、证据、时效、策略和执行。", ["争议事实梳理", "平台申诉和合同索赔", "诉前谈判与外部律师协同"], ["案件事实与时间线", "请求、抗辩和证据地图", "策略、成本、时效和升级计划"], ["当事人、合同和管辖", "事实、损失和因果", "证据真实性和保全", "期限、程序和送达", "和解、执行和沟通权限"], "不得删除、修改或选择性隐藏证据；诉讼、仲裁或法定期限事项必须及时升级律师。"),
    spec("法律政务/公司治理/corporate-governance-counsel", "corporate-governance-counsel", "公司治理法务顾问", "legal", "管理实体、章程、董事股东决议、授权矩阵、关联交易和法定档案。", ["新实体或治理体系", "重大合同和付款授权", "董事股东决议与档案审查"], ["实体和治理台账", "授权与审批矩阵", "决议、缺口和整改计划"], ["实体、股权和最终受益人", "章程与保留事项", "签字权和授权期限", "董事义务与利益冲突", "决议、申报和法定记录"], "不得把内部审批等同于法定授权；重大公司行动需由当地专业人士确认形式要求。"),
    spec("财务出纳/财务角色/跨境财务高级经理/senior-cross-border-finance-manager", "senior-cross-border-finance-manager", "跨境财务高级经理", "role", "统筹核算关账、管理报表、预算、现金、营运资金、税务、外汇和内部控制。", ["跨境财务体系建设", "月度经营和资金决策", "财务专项协同与风险治理"], ["财务目标与责任矩阵", "专项财务 Skill 编排", "关账、现金、预算和风险计划"], ["会计主体与账套", "收入、成本和利润口径", "现金、结算和营运资金", "预算、预测和差异", "税务、外汇、控制和审计证据"], "不得把管理口径替代法定会计和税务口径；正式申报与审计事项必须由合格专业人士确认。"),
    spec("财务出纳/财务角色/跨境财务高级经理/senior-cross-border-finance-manager-weekly-report", "senior-cross-border-finance-manager-weekly-report", "跨境财务高级经理周报", "weekly", "基于账务、现金、预算和税务证据生成财务周报。", ["财务周度复盘", "现金和营运资金预警", "关账、税务和预算事项跟踪"], ["财务周报", "现金、利润和风险摘要", "决策、责任人与下周行动"], ["数据截止和关账状态", "收入、利润和预算差异", "现金、应收应付和库存", "税务、汇率和申报期限", "控制缺口与待决策事项"], "不得用未关账数据冒充正式结果；必须标记预估、调整和未对账项目。"),
    spec("财务出纳/核算关账/financial-close-reconciliation-manager", "financial-close-reconciliation-manager", "财务关账与对账经理", "finance", "建立从平台、支付、订单、库存、银行到总账的可复核关账和对账流程。", ["月结关账", "平台支付与银行对账", "差异和审计证据治理"], ["关账日历和责任矩阵", "对账差异桥", "调整、审批和证据包"], ["主体、期间和截止", "订单、退款、费用和结算", "银行、支付和清算在途", "库存、成本和收入确认", "调整分录、审批和审计轨迹"], "不得以手工调平替代差异解释，不得在未授权时过账或修改正式账簿。"),
    spec("财务出纳/预算管理/budget-forecast-controller", "budget-forecast-controller", "预算与预测控制经理", "finance", "把战略目标转化为驱动型预算、滚动预测、差异分析和资源控制。", ["年度预算", "月度滚动预测", "预算差异和资源重配"], ["预算模型与假设", "滚动预测和差异桥", "资源、预警和决策规则"], ["目标、版本和责任中心", "销量、价格、成本和人效驱动", "汇率、税和季节情景", "预算承诺与实际", "差异 owner 和纠偏动作"], "不得用预算填数代替驱动模型，也不得覆盖原版本和审批轨迹。"),
    spec("财务出纳/资金管理/cash-flow-working-capital-manager", "cash-flow-working-capital-manager", "现金流与营运资金经理", "finance", "管理现金预测、应收应付、库存资金占用、付款优先级和流动性风险。", ["十三周现金预测", "营运资金改善", "资金缺口和付款安排"], ["现金流预测", "现金转换周期分析", "付款、融资和预警计划"], ["期初现金和可用额度", "回款、结算和应收", "采购、物流、税和应付", "库存和现金转换周期", "情景、最低现金和升级阈值"], "不得把账面利润等同于可用现金，不得未经授权安排付款或融资。"),
    spec("财务出纳/税务合规/cross-border-tax-vat-planner", "cross-border-tax-vat-planner", "跨境税务与 VAT 规划师", "finance", "按主体、交易流、货物流和销售国识别 VAT、销售税、关税、所得税和申报证据要求。", ["进入新市场税务评估", "VAT/IOSS/销售税流程", "税务申报和审计证据准备"], ["交易与税务责任图", "注册申报和证据日历", "风险、整改和专业顾问升级清单"], ["主体、常设机构和交易链", "货物所在地与税收地点", "平台代征与卖家责任", "注册、税率、发票和申报", "关税、转让定价、证据和更新日期"], "税务规则高度时效且依赖司法辖区；不得据此直接申报，必须由当地税务专业人士复核。"),
    spec("财务出纳/资金管理/multi-currency-treasury-manager", "multi-currency-treasury-manager", "多币种资金与汇率经理", "finance", "管理多币种账户、平台结算、汇率暴露、换汇、流动性和资金权限。", ["多币种现金管理", "平台结算和换汇优化", "汇率风险和资金安全治理"], ["币种资金头寸", "汇率暴露与情景", "换汇、归集、权限和预警方案"], ["账户、主体和币种", "应收应付自然对冲", "结算周期和费用", "汇率情景与风险限额", "付款权限、欺诈和银行连续性"], "不得把预测汇率当事实，不得未经授权执行交易或提供投机建议。"),
    spec("财务出纳/经营财务/management-accounting-profitability-manager", "management-accounting-profitability-manager", "经营财务与利润经理", "finance", "连接财务账、商品渠道经营和单位经济，支持定价、预算、资源和退出决策。", ["渠道和 SKU 盈利核算", "经营复盘", "定价、促销和资源决策"], ["管理利润口径", "商品渠道盈利矩阵", "差异、情景和经营建议"], ["法定与管理口径桥", "收入、退款和折扣", "采购、履约、平台和广告成本", "共同成本和分摊原则", "贡献利润、现金和决策敏感性"], "不得隐匿分摊假设或把管理贡献利润冒充法定利润。"),
])

SPECS.extend([
    spec("财务出纳/出纳角色/高级出纳/senior-cashier-treasury-specialist", "senior-cashier-treasury-specialist", "高级出纳", "cashier-role", "统筹现金、银行账户、收付款、报销票据、资金日结和支付安全，在授权范围内保证资金执行准确、及时、可追溯。", ["公司日常出纳工作统筹", "多账户多币种收付款安排", "支付异常和资金安全治理"], ["出纳责任与权限矩阵", "收付款和日结执行计划", "资金异常、复核和升级清单"], ["账户、主体与币种", "收款、付款与在途", "票据、单据与审批", "银行日记账和余额核对", "网银权限、印鉴、UKey 与反欺诈"], "出纳不得同时拥有申请、审批、付款、记账和对账的全部权限；不得代替会计确认科目、税务和正式账务处理。"),
    spec("财务出纳/出纳角色/高级出纳/senior-cashier-treasury-specialist-weekly-report", "senior-cashier-treasury-specialist-weekly-report", "高级出纳周报", "weekly", "基于银行流水、支付单据、余额和异常台账生成高级出纳周报。", ["出纳周度复盘", "账户余额与大额资金变动同步", "未达账、退票和支付风险跟踪"], ["高级出纳周报", "资金余额与收付款摘要", "异常、待复核和下周资金事项"], ["期初期末余额与可用资金", "收付款笔数、金额与完成状态", "未达账项、退款和在途", "票据、报销和单据完整性", "权限、安全事件与下周大额付款"], "不得把银行余额等同于可自由支配现金；不得遗漏未达账、受限资金、待审批和预估事项。"),
    spec("财务出纳/收付款/payment-receipt-operations-manager", "payment-receipt-operations-manager", "收付款执行管理员", "cashier", "建立从业务申请、单据校验、授权审批、支付执行、回单归档到状态回写的收付款闭环。", ["供应商和物流付款", "客户、平台和渠道收款认领", "批量付款与失败重试"], ["收付款 SOP 与权限矩阵", "支付批次和状态台账", "回单、异常和升级记录"], ["付款主体、账户和币种", "申请、合同、发票与审批", "收款识别和核销线索", "支付状态、回单和在途", "重复支付、篡改和欺诈拦截"], "不得在授权或单据不完整时执行付款；付款执行、账务确认与独立复核必须分离。"),
    spec("财务出纳/银行与对账/bank-account-reconciliation-cashier", "bank-account-reconciliation-cashier", "银行账户与出纳对账专员", "cashier", "维护银行账户台账、日记账和每日余额核对，及时识别未达账项、银行费用、退票和异常流水。", ["银行日记账维护", "每日资金余额核对", "未达账和异常流水处理"], ["账户与余额台账", "银行日记账核对表", "未达账、差异和跟进清单"], ["账户状态、用途和授权人", "账面、银行与可用余额", "流水唯一标识和交易对手", "未达账原因与账龄", "调节项证据、复核和关闭"], "不得通过修改原始流水或无证据调节来消除差异；月末总账对账仍由财务关账职责复核。"),
    spec("财务出纳/报销与票据/expense-reimbursement-cashier", "expense-reimbursement-cashier", "报销与票据出纳专员", "cashier", "按制度、预算、审批和单据完整性执行员工报销、备用金和票据交接。", ["员工费用报销", "备用金借支与核销", "发票和支付凭证归档"], ["报销校验清单", "付款与退回台账", "备用金、票据和异常跟踪表"], ["申请人、成本中心和用途", "预算与审批链", "发票、收据和重复报销", "借支、核销和逾期", "付款回单、档案和隐私"], "出纳只校验制度和执行证据，不自行批准本人或超授权报销，也不代替税务人员判断抵扣资格。"),
    spec("财务出纳/资金安全/cash-security-access-controller", "cash-security-access-controller", "资金安全与支付权限控制专员", "cashier", "设计和检查银行账户、网银、支付平台、印鉴、UKey、密码和付款指令的分权控制与应急机制。", ["支付权限和账户安全检查", "人员变动权限回收", "疑似欺诈、账户异常和支付应急"], ["资金权限矩阵", "安全检查与轮换计划", "异常冻结、取证和恢复预案"], ["申请、审批、执行和复核分离", "账户角色、限额与双人复核", "UKey、印鉴和密钥保管", "供应商账户变更验证", "日志、告警、冻结和业务连续性"], "不得索取、记录或输出真实密码、私钥、验证码和完整银行凭证；发现疑似欺诈应立即停止并按授权升级。"),
])

SPECS.extend([
    spec("人事招聘/人事角色/人事招聘负责人/senior-hr-recruiting-manager", "senior-hr-recruiting-manager", "人事招聘负责人", "hr-role", "统筹组织编制、招聘、面试、录用、入离职、员工档案、绩效协同和员工关系，确保人才供给与业务目标匹配。", ["人事招聘体系建设", "年度或季度人才规划", "关键岗位招聘和员工生命周期治理"], ["人力目标与责任矩阵", "人事招聘专项 Skill 编排", "人才、组织风险和执行节奏"], ["组织目标、编制和岗位", "人才渠道、漏斗和质量", "面试、录用和入职体验", "档案、绩效和员工关系", "隐私、权限与劳动合规升级"], "不得基于受保护特征作歧视性决定；涉及劳动法、解雇、调查或跨境用工时必须升级劳动用工合规 Skill 和当地专业人士。"),
    spec("人事招聘/人事角色/人事招聘负责人/senior-hr-recruiting-manager-weekly-report", "senior-hr-recruiting-manager-weekly-report", "人事招聘负责人周报", "weekly", "基于编制、招聘漏斗、入离职和员工事项证据生成人事招聘负责人周报。", ["人事招聘周度复盘", "关键岗位和人才风险同步", "入离职、员工关系和跨团队事项跟踪"], ["人事招聘周报", "招聘漏斗与岗位进展", "人员风险、决策和下周行动"], ["编制、在岗和缺口", "候选人漏斗、时效和质量", "Offer、入职和试用期", "离职、员工关系和敏感事项", "待决策、责任人和截止时间"], "不得在周报披露非必要个人敏感信息、薪资细节或调查内容；不得把候选人数冒充招聘质量。"),
    spec("人事招聘/招聘规划/workforce-recruiting-planner", "workforce-recruiting-planner", "人力编制与招聘规划师", "hr", "把业务目标、组织能力和预算转化为可审批的编制、岗位优先级和招聘计划。", ["年度人力规划", "业务扩张或组织调整", "招聘优先级和预算配置"], ["编制与能力缺口图", "岗位优先级和招聘计划", "预算、里程碑和风险方案"], ["业务目标和工作量驱动", "现有人力、能力和产能", "岗位职责与替代方案", "薪酬预算和招聘周期", "优先级、审批和触发条件"], "不得仅按部门主观需求扩编；必须区分新增、替补、外包、自动化和内部流动方案。"),
    spec("人事招聘/人才寻访/candidate-sourcing-operator", "candidate-sourcing-operator", "候选人寻访运营专员", "hr", "设计岗位画像、人才地图、渠道组合、触达和候选人关系管理，提高合格候选人供给。", ["关键岗位人才寻访", "招聘渠道组合优化", "人才库建设和候选人触达"], ["岗位人才画像", "渠道和搜寻策略", "候选人管道与触达复盘"], ["必需与可培养能力", "行业、公司和人才地图", "渠道成本、速度和质量", "触达信息和候选人体验", "来源合规、同意和人才库保留"], "不得抓取或使用无授权的敏感个人数据，不得用学校、年龄、性别等受保护特征代替能力判断。"),
    spec("人事招聘/面试评估/structured-interview-designer", "structured-interview-designer", "结构化面试与评估设计师", "hr", "按岗位成功标准设计结构化面试、工作样本、评分锚点和独立评估机制。", ["岗位面试方案设计", "面试官培训和校准", "候选人评审争议治理"], ["能力与证据矩阵", "面试题和评分锚点", "面试流程、校准和决策记录"], ["岗位成功结果和关键能力", "问题、追问和行为证据", "工作样本与一致评分", "面试官分工和独立记录", "偏见控制、候选人体验和数据最小化"], "不得设计与岗位无关、侵犯隐私或歧视性的提问；AI 评分不得作为未经人工复核的唯一录用依据。"),
    spec("人事招聘/录用入职/offer-onboarding-manager", "offer-onboarding-manager", "录用与入职管理专员", "hr", "管理候选人审批、Offer、背景核验、合同资料、入职准备和首日到试用期交接。", ["候选人录用审批", "Offer 谈判和签署", "跨部门入职和试用期启动"], ["录用审批与 Offer 清单", "入职准备责任表", "首日、30/60/90 天交接计划"], ["岗位、职级、薪酬和预算审批", "条件、有效期和候选人沟通", "背景核验授权与必要性", "合同、账号、设备和培训", "试用目标、导师和反馈节点"], "不得在未授权时承诺薪酬、股权或用工条款；背景核验和合同必须符合工作地规则并保护候选人隐私。"),
    spec("人事招聘/员工生命周期/employee-lifecycle-records-manager", "employee-lifecycle-records-manager", "员工生命周期与档案管理员", "hr", "管理入职、异动、假勤、合同、证明、离职和员工档案的完整性、权限、保留与审计。", ["员工主档维护", "转岗晋升和合同变更", "离职交接与权限回收"], ["员工生命周期状态与清单", "档案完整性和权限台账", "异动、离职和审计记录"], ["员工唯一标识和数据 owner", "合同、职位、汇报和成本中心", "假勤、证明和变更证据", "离职、资产和账号回收", "最小权限、保留、删除和审计日志"], "不得在普通协作空间暴露身份证件、银行、健康等敏感信息；删除和保留必须遵守适用规则和诉讼保全。"),
    spec("人事招聘/员工关系/performance-employee-relations-manager", "performance-employee-relations-manager", "绩效与员工关系管理专员", "hr", "建立目标反馈、试用期、绩效改进、员工诉求、调查和沟通的公平、可记录工作流。", ["绩效周期和反馈机制", "试用期或绩效改进", "员工申诉、冲突和调查协同"], ["绩效与反馈流程", "事实、沟通和行动记录", "员工关系风险与升级方案"], ["目标、期望和证据", "持续反馈与改进支持", "一致性、公平性和反报复", "申诉、调查和保密", "决定权限、劳动法和专业升级"], "不得预设调查结论或把绩效流程作为报复工具；纪律、解雇、歧视和跨境事项必须升级合格 HR/法务人员。"),
    spec("人事招聘/公共/hr-recruitment-generalist", "hr-recruitment-generalist", "人事招聘通用执行专家", "hr", "接管日常人事与招聘需求，先识别任务类型、事实、权限和风险，再完成通用流程或路由到专项 Skill。", ["不确定该使用哪个人事 Skill", "日常招聘和员工流程执行", "跨编制、JD、寻访、面试、录用和入职的组合任务"], ["任务分类与责任边界", "端到端人事执行计划", "专项 Skill 路由、交接和验收清单"], ["业务目标、工作地与用工主体", "编制、岗位和预算授权", "招聘与员工生命周期阶段", "个人信息、敏感性和最小权限", "专项路由、证据、时限和升级条件"], "不得用通用流程替代司法辖区法律判断，也不得在缺少业务负责人、HR 或法务授权时作出录用、薪酬、纪律或解雇决定。"),
    spec("人事招聘/岗位与JD/job-description-generator", "job-description-generator", "岗位说明书与招聘 JD 生成专家", "hr", "先把业务岗位翻译成供 HR 学习和确认的详细岗位介绍，完成指定市场近期岗位与薪酬调研，再生成招聘预问问题、内部岗位说明书、候选人版 JD 与可复用空白 JD 模板，避免因岗位理解和市场判断偏差招错人。", ["HR 不熟悉技术、运营或专业岗位时的招聘需求培训", "新岗位近几个月招聘需求、薪资分布和人才市场调研", "新增或重写招聘 JD", "岗位职责模糊、要求堆砌或招聘双方理解不一致", "多平台、多语言或跨区域岗位发布"], ["HR 岗位培训与详细岗位介绍", "岗位市场与近期薪酬分布调研报告", "招聘需求澄清与建议预问问题", "内部岗位说明书", "候选人版招聘 JD", "可复制的 JD 空白模板", "能力证据、面试评估和发布检查表"], ["岗位存在原因、业务场景、日常工作和成功结果", "上下游、工具系统、专业术语和 HR 常见误解", "目标地区近几个月岗位需求、名称、职级、薪资分布、样本和来源", "职责、权限、不负责范围和职级边界", "必需能力、可培养能力、作品证据和淘汰信号", "招聘经理预问问题、答案口径和未确认项", "工作地、用工方式、汇报、协作、薪酬披露与当地合规"], "不得在 HR 尚未理解、市场薪酬口径不清或招聘经理尚未确认岗位关键事实时直接定稿发布；不得虚构、外推或混用不同地区、币种、职级、薪资周期和样本的薪酬数据，不得虚构福利、组织承诺或加入与工作无关的歧视性条件。"),
    spec("人事招聘/培训发展/employee-training-organization-manager", "employee-training-organization-manager", "员工培训组织与运营经理", "hr", "端到端组织员工培训，从需求和能力差距、计划预算、课程讲师、通知报名、现场交付到效果评估、档案和改进闭环。", ["年度或季度培训规划", "新人、岗位、管理与专项培训组织", "内部讲师、外部供应商和培训效果治理"], ["培训需求与年度月度计划", "课程、讲师、预算、通知、报名和现场执行包", "考勤、反馈、学习效果、费用档案与复盘报告"], ["业务目标、岗位能力和参训对象", "课程目标、形式、讲师和供应商", "预算、排期、场地、设备和通知", "报名、考勤、材料、现场和应急", "反应、学习、行为、业务结果与档案"], "不得把培训场次或满意度等同于能力提升；强制、取证、安全或合规培训必须核验法定要求、合格讲师、完成证据和补训规则。"),
    spec("人事招聘/员工沟通/employee-announcement-writer", "employee-announcement-writer", "企业员工公告撰写专家", "hr-communication", "把已批准事实转化为清晰、准确、可执行且适配渠道的员工公告，并管理敏感沟通与发布风险。", ["入职、放假、培训、福利和办公通知", "制度发布、版本更新和生效公告", "组织调整、事故或紧急事项沟通草案"], ["正式公告正文", "标题、摘要和多渠道短版", "审批、发布、问答和反馈清单"], ["发布目的、受众和知情范围", "已批准事实、版本和生效时间", "员工行动、责任人和截止时间", "渠道、语言、时区和可访问性", "隐私、保密、情绪影响和咨询升级"], "不得替管理层发布未经批准的决定；组织调整、纪律、事故、裁员或个人事项必须最小披露并经 HR、法务及授权负责人审查。"),
])

DISPLAY_NAME_OVERRIDES = {
    "commerce-systems-product-architecture": "跨系统产品架构师",
    "senior-cross-border-legal-counsel": "跨境法务资深经理",
    "senior-cross-border-legal-counsel-weekly-report": "跨境法务资深经理周报",
    "senior-cross-border-finance-manager": "跨境财务资深经理",
    "senior-cross-border-finance-manager-weekly-report": "跨境财务资深经理周报",
    "senior-cashier-treasury-specialist": "资金出纳资深经理",
    "senior-cashier-treasury-specialist-weekly-report": "资金出纳资深经理周报",
    "senior-hr-recruiting-manager": "人事招聘资深经理",
    "senior-hr-recruiting-manager-weekly-report": "人事招聘资深经理周报",
}
ROLE_PATH_OVERRIDES = {
    "senior-cross-border-legal-counsel": "法律政务/法律角色/跨境法务资深经理",
    "senior-cross-border-finance-manager": "财务出纳/财务角色/跨境财务资深经理",
    "senior-cashier-treasury-specialist": "财务出纳/出纳角色/资金出纳资深经理",
    "senior-hr-recruiting-manager": "人事招聘/人事角色/人事招聘资深经理",
}
for item in SPECS:
    if item["name"] in DISPLAY_NAME_OVERRIDES:
        item["display"] = DISPLAY_NAME_OVERRIDES[item["name"]]
    base_name = item["name"].removesuffix("-weekly-report")
    if base_name in ROLE_PATH_OVERRIDES:
        item["path"] = f"{ROLE_PATH_OVERRIDES[base_name]}/{item['name']}"

BUSINESS_ROLE_TERM_REPLACEMENTS = {
    "客服售前高级经理": "客服售前资深经理",
    "跨境电商业务负责人": "跨境电商资深经理",
    "亚马逊运营高级经理": "亚马逊运营资深经理",
    "独立站运营高级经理": "独立站运营资深经理",
    "TikTok Shop 运营高级经理": "TikTok Shop 运营资深经理",
    "选品与商品高级经理": "选品与商品资深经理",
    "品牌与内容高级经理": "品牌与内容资深经理",
    "增长营销高级经理": "增长营销资深经理",
    "用户运营高级经理": "用户运营资深经理",
    "创拍视觉高级经理": "创拍视觉资深经理",
    "供应链高级经理": "供应链资深经理",
    "仓储库存高级经理": "仓储库存资深经理",
    "市场采购高级经理": "市场采购资深经理",
    "客户体验高级经理": "客户体验资深经理",
    "业务数据分析高级经理": "业务数据分析资深经理",
    "跨境法务负责人": "跨境法务资深经理",
    "跨境财务高级经理": "跨境财务资深经理",
    "高级出纳": "资金出纳资深经理",
    "人事招聘负责人": "人事招聘资深经理",
}


def replace_business_role_terms(value):
    if isinstance(value, str):
        for old, new in BUSINESS_ROLE_TERM_REPLACEMENTS.items():
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [replace_business_role_terms(item) for item in value]
    return value


for item in SPECS:
    for key, value in list(item.items()):
        item[key] = replace_business_role_terms(value)


FAMILY_STEPS = {
    "architecture": [
        "检查现有仓库、运行拓扑、质量目标、团队边界和约束；区分已验证事实、假设与未知项",
        "建立系统上下文、关键用户旅程或请求路径，明确边界外依赖和非功能目标",
        "按业务能力划分模块，定义 ownership、依赖方向、公共契约和禁止跨越的边界",
        "设计数据、状态、错误、权限、缓存、并发和资源生命周期，不只覆盖正常路径",
        "评估备选架构的复杂度、性能、可靠性、交付成本和可逆性，记录决策理由",
        "制定增量实施、兼容迁移、验证、观测、灰度和回滚计划",
    ],
    "development-expert": [
        "确认业务目标、现有代码、语言或框架版本、运行环境、质量标准和交付边界",
        "复现或拆解真实功能与问题，定位到模块、依赖、状态、数据、线程、资源或运行时机制",
        "基于该语言或框架的官方机制设计实现，明确代码边界、失败路径、兼容性和安全约束",
        "完成或指导关键实现、重构、调优和测试，避免用抽象架构代替可运行工程结果",
        "用单元、集成、端到端、性能或生产证据验证，并记录版本、环境和未覆盖风险",
        "输出代码级方案、实施顺序、验收、发布、观测和回滚计划，与通用架构师保持边界一致",
    ],
    "ui-interaction": [
        "确认用户角色、任务、入口、上下文、设备、权限、数据状态、业务规则和成功标准",
        "建立主流程、替代路径、取消退出、返回恢复和异常路径，不从静态页面直接猜交互",
        "为页面和组件定义状态、事件、前置条件、反馈、焦点、数据变化、副作用和不可用原因",
        "设计鼠标、键盘、触摸、响应式和辅助技术行为，并控制动效时长、减少动画与认知负担",
        "与前端架构、React/Vue3、接口、埋点和测试约束对齐，输出可实现的组件契约与验收场景",
        "使用原型、状态表或真实页面验证关键任务，记录未知项、取舍、失败恢复和迭代优先级",
    ],
    "operations": [
        "锁定国家、渠道、类目、产品、目标、周期、预算、利润和合规约束",
        "收集一手经营数据、平台证据、客户声音和产品事实，标注时间范围与可信度",
        "建立从目标到驱动因素的经营模型，按人群、商品、渠道和阶段定位机会",
        "设计可执行策略，明确动作、owner、输入物、截止时间、预算和前置依赖",
        "为每项动作定义领先指标、结果指标、护栏、停止条件和归因限制",
        "输出执行节奏、检查清单、风险预案和复盘机制，并回写可复用知识",
    ],
    "customer-presales": [
        "确认国家、渠道、语言、客户身份范围、咨询意图、商品、订单阶段、响应 SLA 和坐席权限",
        "核验商品、价格、优惠、库存、物流、支付、退换和保修的权威来源、版本与适用范围",
        "澄清客户场景、偏好、预算、时间和硬约束，区分咨询、推荐、异议、投诉和销售线索",
        "给出事实准确、文化自然且不过度承诺的答复，明确替代方案、风险、升级和跟进动作",
        "记录意图、未解决原因、知识缺口、转化或流失信号，按最小化原则处理个人数据",
        "输出会话、知识、质检、线索交接和 VOC 闭环，并用解决质量而非单一响应速度验收",
    ],
    "creative-production": [
        "确认商品、品牌、受众、国家、渠道、用途、预算、时间、规格、成功指标和不可改变的产品事实",
        "把营销需求转为创意角度、证据镜头、脚本、shot list、样品和制作优先级，标注假设与缺口",
        "设计摄影、视频、UGC 或后期方案，明确人员、场地、设备、工具、授权、版本和交付接口",
        "建立真实性、色彩、声音、字幕、品牌、渠道和权利质量门禁，覆盖异常、备份与补拍条件",
        "按素材 ID 保存原始文件、选择、修改、授权、版本和效果血缘，避免覆盖历史或失去可追溯性",
        "输出预算排期、责任人、制作包、验收、交付、复用和表现回流计划，不虚构已拍摄或已验证结果",
    ],
    "ai-creative-production": [
        "确认商品事实、人物和资产权利、目标渠道、允许的 AI 修改范围、披露要求和人工批准人",
        "选择生成、替换、试穿、配音或剪辑 Tool，记录模型版本、输入、参考、参数、成本和失败回退",
        "建立商品、人像、文字、标识、动作、声音和跨镜头一致性标准，准备真实对照与禁止变更项",
        "生成或编排候选版本，保留完整血缘；按真实性、物理合理性、偏差、版权和平台规则逐项筛选",
        "将低置信度、敏感人物、关键商品差异和权利不明内容送入人工复核、重做、披露或禁止上线流程",
        "输出版本、证据、审批、交付和监控记录，支持回滚到原素材或人工制作，不宣称 AI 内容是真实拍摄",
    ],
    "creative-tagging": [
        "确认贵司素材库、CMS/DAM、素材 ID、标签使用场景、搜索与效果分析消费者以及回写权限",
        "盘点现有标签 taxonomy、定义、层级、互斥依赖、必填范围、敏感等级、owner 和版本",
        "选择图像或视频理解模型，定义候选数量、置信度、规则校验、人工复核和失败回退",
        "用代表性金标样本评估准确率、召回率、人工一致性和关键标签错误，按场景设置阈值",
        "执行候选生成、人工确认、批量预览、幂等回写、审计和回滚，保留模型与修改血缘",
        "监测未识别、错标、标签漂移、搜索命中和素材表现回流，形成错误集与 taxonomy 迭代闭环",
    ],
    "warehouse-operations": [
        "确认仓库、货主、SKU、批次、库存状态、渠道、订单或任务范围、系统事实源、SLA 和权限",
        "核对实物、单据、系统状态和时间点，区分现货、在途、预占、冻结、残次、退货和不可售",
        "设计或检查入库、库内、出库、调拨、盘点、逆向的状态、任务、扫描、证据和异常补偿",
        "量化数量准确、时效、产能、人效、成本、仓容、缺货、损耗和安全影响，识别根因与约束",
        "明确 WMS/IMS/OFS/OMS/TMS 及采购、渠道、财务的 ownership、对账、幂等和人工升级接口",
        "输出作业标准、计划、责任人、阈值、异常、复核、审计和持续改善闭环，不虚构实物状态",
    ],
    "market-procurement": [
        "确认市场、渠道、类目、目标人群、商品定义、价格带、目标成本、销量、现金、交期和合规约束",
        "收集消费者、竞品、供应商、样品、成本、质量、产能和交付证据，标记来源、版本和反证",
        "通过机会门、样品门、供应商门、成本门、合规门和量产门逐步验证，不一次性拍脑袋下单",
        "定义规格、BOM、样品、报价、MOQ、付款、交期、质检、变更和责任接口，保留版本与审批",
        "评估单位经济、总拥有成本、现金周期、库存退出、集中度和中断情景，准备替代与止损方案",
        "输出决策、采购执行、owner、截止、验收、供应商绩效、风险升级和复盘，不虚构市场或供应证据",
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
    "role": [
        "确认角色目标、授权边界、国家、渠道、品类、周期、利润和关键约束",
        "建立角色经营模型和责任矩阵，识别必须亲自决策、可委派及需升级的事项",
        "读取真实经营、客户、商品、供应链和财务证据，按影响与紧迫度建立问题组合",
        "选择并编排专项 Skill，明确每项任务的输入、owner、依赖、交付物和验收接口",
        "在收入、利润、现金、客户、合规和交付约束间做取舍，记录决策及不做事项",
        "建立日周月经营节奏、仪表盘、风险预警、复盘和能力沉淀机制",
    ],
    "creative-role": [
        "确认商品、品牌、市场、渠道、使用场景、需求优先级、预算、交付时间和不可改变的事实边界",
        "建立创意需求池、制作类型、产能、人员供应商、样品、授权和项目责任矩阵",
        "读取历史素材、投放表现、客户反馈和生产数据，区分策略问题、制作问题、版位问题和疲劳问题",
        "编排创意策略、制片、摄影、视频、UGC、AI 制作、后期和素材运营 Skill，定义交接与验收",
        "在速度、成本、真实性、品牌、合规、质量和可测试性之间做取舍并记录不做事项",
        "建立日周月排期、样片评审、AI 人工门禁、交付质检、资产入库和效果回流机制",
    ],
    "warehouse-role": [
        "确认主体、仓库、库存所有权、渠道、SKU、服务范围、成本、SLA、系统和授权边界",
        "建立供应商到入库、库内、出库、运输、退货和盘点的流程、状态、责任与数据事实源",
        "读取库存准确率、缺货、老化、作业效率、差异、损耗、仓容、运输和客户异常证据",
        "编排供应商质量、补货、库存控制、入出库、分配、物流、逆向和安全专项 Skill",
        "在服务水平、库存资金、仓容、人效、成本、安全和渠道承诺间做取舍并记录决策",
        "建立日清周结、盘点、异常升级、权限复核、持续改善和跨 OMS/IMS/OFS/WMS/TMS 对账机制",
    ],
    "market-procurement-role": [
        "确认市场、渠道、类目、目标客户、价格带、目标成本、销量假设、现金、交期和合规边界",
        "建立机会、商品概念、样品、供应商、报价、谈判、采购订单、质量和退出的责任与阶段门",
        "读取市场、竞品、客户、样品、成本、产能、质量、交付和供应商集中度证据，识别反证",
        "编排市场机会、选品、寻源质量、样品验证、谈判成本、采购订单和采购风险专项 Skill",
        "在需求真实性、差异化、毛利、MOQ、现金、交期、质量、合规和库存风险间做取舍",
        "建立周月选品会、样品评审、供应商绩效、采购交付、变更审批和商品退出复盘机制",
    ],
    "customer-presales-role": [
        "确认市场、渠道、语言、服务范围、目标客户、商品组合、服务时段、SLA、权限和合规边界",
        "建立咨询、推荐、知识、线索、升级、销售交接和客户声音的流程、状态与责任矩阵",
        "读取咨询量、响应、解决、转化、流失、质检、知识命中和客户反馈证据，识别主要障碍",
        "编排售前咨询、商品推荐、多语言沟通、FAQ 知识库、线索分级和质检培训专项 Skill",
        "在客户适配、转化、利润、库存、履约、隐私、品牌和坐席效率间做取舍并记录决策",
        "建立日周月服务节奏、会话抽检、知识更新、跨班次交接、销售 SLA 和 VOC 改进闭环",
    ],
    "cashier-role": [
        "确认公司主体、账户、币种、资金范围、岗位授权、付款限额和不可兼任职责",
        "建立收付款、银行日记账、票据、备用金、余额日结和异常事项的责任矩阵",
        "检查申请、审批、执行、记账、对账分离，以及网银、UKey、印鉴和供应商账户变更控制",
        "读取银行流水、支付平台、业务单据和资金计划，识别未达账、重复支付、欺诈与流动性风险",
        "编排收付款、银行对账、报销票据和资金安全专项 Skill，明确证据、复核、截止和升级条件",
        "建立日清、周报、月结交接、权限复核、应急冻结和审计留痕机制",
    ],
    "hr-role": [
        "确认业务目标、组织范围、工作地、用工主体、编制、预算、岗位优先级和授权边界",
        "建立从编制、岗位、寻访、面试、录用、入职到异动离职的责任与状态地图",
        "读取组织、人效、招聘漏斗、候选人体验和员工事项证据，识别能力缺口、瓶颈和风险",
        "编排招聘规划、人才寻访、面试评估、录用入职、员工档案和员工关系专项 Skill",
        "在人才质量、速度、成本、公平、隐私、员工体验和劳动合规间做取舍并记录决定",
        "建立周月人才节奏、漏斗校准、试用期反馈、敏感事项升级和组织能力沉淀机制",
    ],
    "weekly": [
        "锁定周报周期、时区、比较口径、目标、数据截止时间和数据来源",
        "汇总本角色负责指标、关键交付、异常、决策和跨团队依赖，并验证数据完整性",
        "先写结论摘要，再按目标差距拆解规模、效率、利润、质量和风险驱动",
        "区分已完成、进行中、阻塞和待决策，所有状态绑定证据、owner 和截止时间",
        "形成下周优先级、预期影响、资源需求、护栏和需要管理层决定的事项",
        "按模板输出可持续追踪的周报，并保留口径变化、未知项和上周行动回看",
    ],
    "legal": [
        "确认司法辖区、适用主体、交易或行为、时间点、目标和需要作出的业务决策",
        "收集合同、政策、证据、通信和当前官方规则，区分事实、主张、假设和法律问题",
        "建立权利义务、责任主体、期限、证据和潜在救济矩阵，按影响与可能性分级",
        "提出低风险可执行方案、替代文本、控制和保全动作，不把业务建议包装成确定法律结论",
        "识别必须升级当地律师、监管专家或诉讼代理人的触发条件和最晚时间",
        "输出审查记录、责任人、整改、审批、持续监控和特权/敏感信息边界",
    ],
    "finance": [
        "确认会计主体、期间、币种、账簿、管理口径、数据截止和决策用途",
        "收集总账、明细账、订单、支付、平台、银行、库存、税务和合同证据并完成勾稽",
        "定义收入、成本、税、汇率、分摊和状态规则，区分法定、管理、预估和现金口径",
        "分析余额、变动、差异、驱动和情景，保留公式、来源、调整和审批轨迹",
        "建立控制、复核、权限、阈值、申报或关账日历，并标记需会计师或税务顾问确认事项",
        "输出可复核报表、差异桥、决策建议、owner、截止、风险和后续监控",
    ],
    "cashier": [
        "确认付款或收款主体、账户、币种、金额、用途、日期、交易对手和授权边界",
        "核验申请、合同、发票或收据、预算、审批、收款信息和防重复标识，缺项即暂停",
        "按申请、审批、执行、记账、对账分离原则检查权限、限额、双人复核和敏感凭证保管",
        "执行或编排收付款、回单、日记账、状态回写和档案留存，完整记录失败、退回与在途",
        "将银行流水、支付平台、业务单据和余额相互勾稽，建立未达账、异常和关闭证据",
        "输出可复核台账、异常升级、责任人、截止时间和资金安全检查，不暴露任何密钥凭证",
    ],
    "hr": [
        "确认业务目标、组织范围、工作地、用工主体、岗位、编制、预算、周期和授权边界",
        "收集岗位事实、组织数据、候选人或员工证据，遵守数据最小化并区分事实与评价",
        "设计角色清晰、标准一致、可追踪的人事流程，明确输入、状态、责任人、时限和例外",
        "用岗位相关证据评估能力、进度和风险，检查偏见、歧视、隐私、候选人和员工体验",
        "涉及合同、调查、纪律、解雇或跨境用工时识别 HR、法务和当地专业人士升级条件",
        "输出计划、记录、决定依据、沟通、权限和审计要求，并设置质量指标和复盘闭环",
    ],
    "hr-communication": [
        "确认公告目的、发起人、批准人、受众、知情范围、发布时间、渠道和期望行动",
        "只使用已批准事实，核对名称、日期、版本、生效时间、地点、责任人、链接和联系方式",
        "按结论、影响对象、发生事项、员工行动、时间节点、支持渠道和后续更新组织信息",
        "根据全员、区域、团队、管理层或个人范围控制披露，检查隐私、保密、法律和情绪风险",
        "生成正式版、短消息版和必要问答，确保多语言、时区、移动端和可访问性表达一致",
        "输出审批发布清单、发送记录、反馈监测和更正机制；未经授权只提供草案不得声称已发布",
    ],
    "ai-product": [
        "确认项目名称、用户角色、业务目标、标签对象、输入来源、下游消费者和不在范围内的事项",
        "定义标签 taxonomy、语义、owner、版本、互斥/依赖规则、质量标准和敏感等级",
        "设计模型建议、置信度、人工审核、修改、发布、回滚和异常处理的端到端状态机",
        "明确模型/API/脚本等 Tool 的输入输出契约、权限、成本、时延、失败和可观测要求",
        "建立金标集、离线指标、线上采样、人工一致性、漂移和错误反馈评估体系",
        "按 MVP、人审增强、自动化和规模治理输出路线、验收、审计与回滚方案",
    ],
}

OFFICIAL_SOURCES = {
    "react-senior-expert": [("React Managing State", "https://react.dev/learn/managing-state"), ("React Escape Hatches", "https://react.dev/learn/escape-hatches")],
    "vue3-senior-expert": [("Vue Composition API", "https://vuejs.org/guide/extras/composition-api-faq.html"), ("Vue Scaling Up", "https://vuejs.org/guide/scaling-up/tooling.html")],
    "typescript-frontend-architecture": [("TypeScript Project References", "https://www.typescriptlang.org/docs/handbook/project-references"), ("TypeScript Modules", "https://www.typescriptlang.org/docs/handbook/modules/reference")],
    "react-frontend-architecture": [("React Managing State", "https://react.dev/learn/managing-state"), ("React Escape Hatches", "https://react.dev/learn/escape-hatches")],
    "vue-frontend-architecture": [("Vue Scaling Up", "https://vuejs.org/guide/scaling-up/tooling.html"), ("Vue Composables", "https://vuejs.org/guide/reusability/composables.html")],
    "nextjs-frontend-architecture": [("Next.js App Router", "https://nextjs.org/docs/app"), ("Next.js Project Structure", "https://nextjs.org/docs/app/getting-started/project-structure")],
    "angular-frontend-architecture": [("Angular Overview", "https://angular.dev/overview"), ("Angular Style Guide", "https://angular.dev/style-guide")],
    "sveltekit-frontend-architecture": [("SvelteKit Introduction", "https://svelte.dev/docs/kit/introduction"), ("SvelteKit Project Structure", "https://svelte.dev/docs/kit/project-structure")],
    "spring-boot-backend-architecture": [("Spring Boot Core Features", "https://docs.spring.io/spring-boot/reference/features/"), ("Spring Boot Production-ready Features", "https://docs.spring.io/spring-boot/reference/actuator/")],
    "fastapi-backend-architecture": [("FastAPI Bigger Applications", "https://fastapi.tiangolo.com/tutorial/bigger-applications/"), ("FastAPI Dependencies", "https://fastapi.tiangolo.com/tutorial/dependencies/")],
    "nestjs-backend-architecture": [("NestJS Modules", "https://docs.nestjs.com/modules"), ("NestJS Providers", "https://docs.nestjs.com/providers")],
    "gin-backend-architecture": [("Gin Middleware", "https://gin-gonic.com/en/docs/middleware/"), ("Gin Security Guide", "https://gin-gonic.com/en/docs/middleware/security-guide/")],
    "php-backend-architecture": [("PHP Namespaces", "https://www.php.net/manual/en/language.namespaces.php"), ("Composer Documentation", "https://getcomposer.org/doc/")],
    "rust-backend-architecture": [("The Rust Programming Language", "https://doc.rust-lang.org/book/"), ("The Cargo Book", "https://doc.rust-lang.org/cargo/")],
    "csharp-backend-architecture": [("C# Guide", "https://learn.microsoft.com/en-us/dotnet/csharp/"), (".NET Architecture Guides", "https://learn.microsoft.com/en-us/dotnet/architecture/")],
    "laravel-backend-architecture": [("Laravel Service Container", "https://laravel.com/docs/container"), ("Laravel Application Structure", "https://laravel.com/docs/structure")],
    "aspnet-core-backend-architecture": [("ASP.NET Core Fundamentals", "https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0"), ("ASP.NET Core Architecture Tests", "https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/test-asp-net-core-mvc-apps")],
    "amazon-store-operations-manager": [("Amazon Seller University", "https://sell.amazon.com/learn/seller-university/"), ("Amazon Manage Your Compliance", "https://sell.amazon.com/blog/manage-your-compliance")],
    "shopify-store-operations-manager": [("Shopify Products", "https://help.shopify.com/en/manual/products"), ("Shopify Analytics", "https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports")],
    "tiktok-shop-operations-manager": [("TikTok Business Center", "https://ads.tiktok.com/business/en/business-center"), ("TikTok Creative Center", "https://ads.tiktok.com/business/en-US/creativecenter")],
    "traffic-acquisition-analyst": [("GA4 Acquisition Scope", "https://support.google.com/analytics/answer/14731736"), ("GA4 Reports Overview", "https://support.google.com/analytics/answer/9212670")],
    "conversion-funnel-analyst": [("GA4 Life Cycle Reports", "https://support.google.com/analytics/answer/12924233"), ("GA4 Ecommerce Metrics", "https://support.google.com/analytics/answer/13428834")],
    "customer-cohort-ltv-analyst": [("GA4 Retention Overview", "https://support.google.com/analytics/answer/11004084"), ("GA4 Data Retention", "https://support.google.com/analytics/answer/7667196")],
    "cross-border-regulatory-compliance-counsel": [("EU Customs Ecommerce", "https://taxation-customs.ec.europa.eu/customs/eu-customs-union-facts-and-figures/goods-bought-online_en")],
    "import-export-trade-compliance-reviewer": [("CBP Basic Importing and Exporting", "https://www.cbp.gov/trade/basic-import-export"), ("BIS Export Compliance Toolkit", "https://www.bis.gov/learn-support/export-compliance-programs/export-compliance-toolkit")],
    "us-market-regulatory-compliance-counsel": [("CBP Basic Importing and Exporting", "https://www.cbp.gov/trade/basic-import-export"), ("FTC Advertising and Marketing", "https://www.ftc.gov/business-guidance/advertising-marketing")],
    "eu-market-regulatory-compliance-counsel": [("EU General Product Safety Regulation", "https://eur-lex.europa.eu/EN/legal-content/summary/general-product-safety-regulation-2023.html"), ("European Commission Data Protection", "https://commission.europa.eu/law/law-topic/data-protection_en")],
    "privacy-data-protection-counsel": [("European Commission Data Protection", "https://commission.europa.eu/law/law-topic/data-protection_en")],
    "advertising-claims-legal-reviewer": [("FTC Advertising and Marketing", "https://www.ftc.gov/business-guidance/advertising-marketing"), ("FTC Endorsements", "https://www.ftc.gov/news-events/topics/truth-advertising/advertisement-endorsements")],
    "cross-border-tax-vat-planner": [("EU VAT Place of Taxation", "https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/place-taxation_en"), ("EU Ecommerce Customs and VAT", "https://taxation-customs.ec.europa.eu/customs/customs-procedures-import-and-export/customs-operations/customs-formalities-low-value-consignments_en")],
    "creative-asset-intelligent-tagging-specialist": [("生成式人工智能服务管理暂行办法", "https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm"), ("中华人民共和国个人信息保护法", "https://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html"), ("互联网信息服务算法推荐管理规定", "https://www.cac.gov.cn/2022-01/04/c_1642894606364259.htm")],
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
    if s["name"] == "job-description-generator":
        steps = [
            "先向招聘经理收集业务目标、为何现在招聘、岗位解决的问题、首年关键结果、工作地、用工主体、编制、预算与时间；缺失项进入预问清单，不得猜测",
            "生成供 HR 学习的详细岗位介绍：业务背景、典型工作日、主要任务、真实交付物、上下游、工具系统、专业术语、职级差异、优秀与不合格表现以及常见误解",
            "锁定目标国家或城市、币种、税前税后、月薪年薪、固定与浮动、岗位同义词、职级和观察窗口；检索近几个月多个可追溯来源，清洗重复与不可比样本",
            "生成岗位市场与薪酬调研报告：样本量、来源覆盖、发布时间分布、招聘需求趋势、岗位名称差异、薪资最小值/中位数/分位数/最大值、经验与技能溢价、地域和公司类型差异，并说明偏差与置信度",
            "生成建议预问问题并标注提问对象、目的、理想答案要素、风险答案与答案如何影响 JD；等待招聘经理确认关键分歧",
            "把确认事实转化为内部岗位说明书，定义使命、结果、职责、权限、不负责范围、协作关系、成功指标和前三十/六十/九十天预期",
            "区分必须具备、可培养和加分项，为每项定义可观察证据、作品或经历，删除愿望清单、重复要求和与岗位无关的限制",
            "生成面向候选人的招聘 JD，使用可理解语言说明机会、工作、结果、要求、流程和已批准待遇信息，并执行包容性、隐私和当地合规检查",
            "同时交付保持字段和说明但不填业务事实的 JD 空白模板，最后输出未确认项、发布审批、面试评估建议和版本记录",
        ]
    extra_load = ""
    if s["name"] == "creative-asset-intelligent-tagging-specialist":
        extra_load = """
- 必须读取 `references/tagging-compliance-baseline.md`，并加载 `assets/allowed_tags.json`、`assets/restricted_tags.json`、`assets/forbidden_tags.json` 与 `assets/tagging-output.schema.json`。
- 标签只能来自已批准标签库；受限标签转人工，禁止标签拒绝输出。业务方临时要求不得覆盖合规规则。
"""
    elif s["name"] == "job-description-generator":
        extra_load = """
- 必须读取 `references/hr-role-training-checklist.md`，先完成 HR 岗位理解与招聘经理预问，不得在关键事实未确认时直接发布 JD。
- 必须读取 `references/job-market-research-method.md`；薪资与岗位需求属于时效数据，执行时必须查询目标市场近期来源并记录采集日期、样本和口径。
- 使用 `assets/delivery-template.md` 交付完整招聘包，同时交付 `assets/job-market-research-template.md` 调研报告，并原样附带 `assets/blank-jd-template.md` 作为可复用 JD 空白模板。
"""
    skill = f"""---
name: {s['name']}
description: {desc}
---

# {s['display']}

{s['positioning']}

## Load resources

- 在 SkillForge 项目内执行时，先定位仓库根目录并读取 `公司上下文/company-profile.yaml` 与 `公司上下文/README.md`；只使用其中已确认事实，未知字段不得自行补全。
- Read `references/professional-checklist.md` before making decisions.
- Read `references/scenario-playbook.md` to select the matching scenario path, evidence, exceptions, and acceptance gates.
- Use `assets/delivery-template.md` for the final durable artifact.
- Use `assets/decision-record-template.md` when the task contains alternatives, approvals, irreversible actions, or cross-team tradeoffs.
- If local project rules or source data conflict with generic guidance, preserve the evidence and explain the decision.
{extra_load}

## Workflow

""" + "\n".join(f"{i}. {step}" for i, step in enumerate(steps, 1)) + f"""

## Required decision lenses

""" + "\n".join(f"- {x}" for x in s["lenses"]) + f"""

## Depth requirements

- 先解释业务对象、术语、为什么要做、谁使用结果以及错误结果会造成什么后果，再进入执行。
- 覆盖当前场景及与其相邻的高频变体；不得用同一套步骤忽略国家、渠道、职级、系统状态、数据成熟度或风险等级差异。
- 明确上游输入、下游消费者、责任边界、决策权、审批人、系统事实源和人工交接点。
- 对每个关键判断给出所需证据、可选方案、选择条件、反证、停止条件和不可逆风险。
- 同时设计正常路径、缺数据、低置信度、冲突、超时、权限不足、部分成功、回滚和转人工路径。
- 工具只是执行手段；必须说明工具输入输出、权限、失败、成本、时效、版本和人工验收，不能把调用工具等同于完成业务。
- 交付物必须让下游能直接执行或审批，并包含 owner、依赖、时间、验收指标、审计证据和下一次复盘触发器。

## Scenario and exception gates

1. 从 `references/scenario-playbook.md` 选择主场景；同时检查是否命中第二场景或高风险变体。
2. 关键事实、权限、口径或 source of truth 未确认时，降级为调研、草案或 `REVIEW_REQUIRED`，不得伪装成可执行定稿。
3. 发现目标冲突时，明确收入、利润、现金、客户、质量、时效、合规和可逆性之间的取舍，记录决策人。
4. 执行中出现部分失败时，保护已确认结果，隔离未知状态，停止扩大影响，提供对账、补偿或回滚步骤。
5. 只有交付物、验证证据、责任交接和剩余风险同时清楚，任务才算完成。

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

## 贵司适配

- 在本仓库内优先读取 `公司上下文/company-profile.yaml`，使用贵司已确认的组织、系统、渠道、市场和口径。
- 公司上下文未确认的内容必须列为待补充信息，不得用行业常识冒充贵司事实。
- 独立分发本 Skill 时，应随任务提供最新公司上下文快照。

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

## 深度执行标准

- 不只覆盖理想流程，还覆盖相邻场景、数据不足、权限不足、异常、部分成功、转人工、止损和回滚。
- 先让执行者理解业务对象、上下游、术语、成功结果和常见误解，再给动作。
- 每个方案必须说明适用条件、证据、备选、取舍、owner、审批、验收和复盘。
- Tool 调用不等于业务完成；以可验证交付物和下游成功接收作为完成标准。

## 技能包组成

- `SKILL.md`：AI 执行入口与强制工作流。
- `references/professional-checklist.md`：专业检查表和失败模式。
- `references/scenario-playbook.md`：按实际场景、变体和异常选择执行路径。
- `assets/delivery-template.md`：可直接复用的交付模板。
- `assets/decision-record-template.md`：方案比较、审批、异常、回滚和复盘记录。
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

    write_depth_resources(base, s)
    if s["name"] == "creative-asset-intelligent-tagging-specialist":
        write_tagging_compliance_resources(base)
    elif s["name"] == "job-description-generator":
        write_jd_generation_resources(base)


def write_depth_resources(base, s):
    scenario_sections = []
    for index, scenario in enumerate(s["scenarios"], 1):
        scenario_sections.append(f"""## 场景 {index}：{scenario}

- 触发信号：什么变化、问题或决策需要启动本 Skill。
- 先决条件：目标、范围、对象、国家/渠道/系统、时间与 owner。
- 最低证据：当前状态、历史基线、约束、事实源、权限和反证。
- 核心判断：围绕{q(s['lenses'])}逐项判断，不跳过不适用说明。
- 执行变体：标准、快速止损、数据不足、高风险审批和分阶段试点。
- 异常路径：缺数据、口径冲突、权限不足、依赖失败、部分成功、超时与回滚。
- 完成门槛：交付{q(s['outputs'])}，并给出验收证据、owner、截止和剩余风险。
""")
    (base / "references/scenario-playbook.md").write_text(
        f"# {s['display']}场景作战手册\n\n"
        "本手册用于选择真实场景路径，不能用作无证据套话。一个任务可命中多个场景，但必须指定主场景并说明组合原因。\n\n"
        + "\n".join(scenario_sections)
        + f"""\n## 跨场景深度检查

### 业务与人员

- 结果由谁使用、谁批准、谁执行、谁承担错误后果。
- 上游提供什么，下游需要什么，何处最容易误解或丢失信息。

### 数据与系统

- source of truth、数据截止、状态、版本、权限、写回、幂等、对账和留存。
- 不同系统或渠道口径不一致时的差异桥与最终裁决 owner。

### 决策与例外

- 至少比较维持现状、推荐方案和低风险备选；说明适用条件与放弃理由。
- 明确不可逆动作、审批点、止损阈值、人工升级和恢复路径。

### 结果与学习

- 领先指标、结果指标、护栏指标、观察窗口和失败定义。
- 复盘时间、错误样本、规则或模板如何更新，以及谁维护版本。
""",
        encoding="utf-8",
    )
    (base / "assets/decision-record-template.md").write_text(f"""# {s['display']}决策记录

## 1. 决策背景

- 主场景：
- 业务问题与影响对象：
- 必须决策的截止时间：
- 决策人、执行人、审批人：

## 2. 事实、口径与未知项

| 项目 | 事实/假设/未知 | 来源与版本 | 影响 | 补证 owner |
|---|---|---|---|---|

## 3. 专业维度

""" + "\n".join(f"- {lens}：" for lens in s["lenses"]) + """

## 4. 方案比较

| 方案 | 适用条件 | 收益 | 成本/依赖 | 风险 | 可逆性 | 选择/放弃理由 |
|---|---|---|---|---|---|---|

## 5. 异常与控制

| 异常/触发器 | 预防 | 检测 | 暂停范围 | 补偿/回滚 | 升级对象 |
|---|---|---|---|---|---|

## 6. 执行与验收

| 动作 | Owner | 依赖 | 截止 | 验收证据 | 护栏/停止条件 |
|---|---|---|---|---|---|

## 7. 复盘与版本

- 观察窗口：
- 领先、结果与护栏指标：
- 下次复盘：
- 需要更新的规则、数据、模板或 Skill：
""", encoding="utf-8")


def write_tagging_compliance_resources(base):
    allowed = {
        "library_version": "1.0.0",
        "policy": "模型只能从本列表选择；正式使用前由贵司素材与合规 owner 审批",
        "tags": [
            "室内", "户外", "海滩", "泳池", "纯色背景", "生活方式场景",
            "商品特写", "细节图", "正面", "背面", "侧面", "横版", "竖版",
            "单人", "多人", "无人物", "单商品", "多商品", "包含文字",
            "包含Logo", "包含水印", "蓝色", "黑色", "白色", "红色",
        ],
    }
    restricted = {
        "library_version": "1.0.0",
        "action": "REVIEW_REQUIRED",
        "tags": [
            {"name": "疑似未成年人", "reason": "涉及未成年人保护与敏感个人信息风险"},
            {"name": "人物正脸", "reason": "可能涉及肖像与生物识别处理风险"},
            {"name": "性别表达", "reason": "仅在已确认业务必要且经审批时使用"},
            {"name": "第三方Logo", "reason": "需要核验商标和商业授权"},
            {"name": "第三方文字", "reason": "需要核验版权、声明和使用范围"},
            {"name": "水印", "reason": "可能表明第三方权利或来源限制"},
        ],
    }
    forbidden = {
        "library_version": "1.0.0",
        "action": "COMPLIANCE_REJECTED",
        "tags": [
            "具体人物身份", "姓名", "人脸身份", "精确年龄", "民族", "种族", "国籍推断",
            "宗教信仰", "政治倾向", "性取向", "疾病", "残疾", "健康状态",
            "经济状况", "收入水平", "社会阶层", "精确地址", "联系方式", "证件号码",
            "美丑评价", "身材羞辱", "社会身份推断",
        ],
    }
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Creative Asset Tagging Result",
        "type": "object",
        "required": ["skill_version", "model_name", "model_version", "tag_library_version", "input_asset_id", "tags", "person_present", "risk_level", "review_required", "decision", "created_at"],
        "properties": {
            "skill_version": {"type": "string"},
            "model_name": {"type": "string"},
            "model_version": {"type": "string"},
            "tag_library_version": {"type": "string"},
            "input_asset_id": {"type": "string"},
            "tags": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["name", "confidence", "evidence", "source"],
                    "properties": {
                        "name": {"type": "string"},
                        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                        "evidence": {"type": "string"},
                        "source": {"enum": ["visual", "metadata", "human"]},
                    },
                },
            },
            "person_present": {"type": "boolean"},
            "minor_status": {"enum": ["NOT_PRESENT", "ADULT_CONFIRMED_BY_METADATA", "POSSIBLE_MINOR", "UNKNOWN"]},
            "copyright_risk": {"type": "object"},
            "risk_level": {"enum": ["LOW", "MEDIUM", "HIGH"]},
            "review_required": {"type": "boolean"},
            "decision": {"enum": ["AUTO_ACCEPTED", "REVIEW_REQUIRED", "COMPLIANCE_REJECTED"]},
            "review_result": {"type": ["string", "null"]},
            "operator": {"type": ["string", "null"]},
            "created_at": {"type": "string"},
        },
        "additionalProperties": False,
    }
    for name, value in [("allowed_tags.json", allowed), ("restricted_tags.json", restricted), ("forbidden_tags.json", forbidden), ("tagging-output.schema.json", schema)]:
        (base / "assets" / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (base / "references/tagging-compliance-baseline.md").write_text("""# 智能打标合规基线

## 能力边界

本 Skill 是第一层规则约束，不是完整合规系统。它可以限制模型能读取的业务字段、允许输出的标签、转人工条件和拒绝条件，但不能单独提供真实权限隔离、阻止原图发送给外部模型、核验授权文件真伪、阻止规则被绕过或生成不可篡改审计日志。

## 适用范围判断

- 先确认部署地点、服务对象、是否向中国境内公众提供生成式人工智能服务、是否属于互联网信息服务以及是否调用外部模型。
- 《生成式人工智能服务管理暂行办法》第二条规定其适用于向中国境内公众提供生成内容的服务；未向境内公众提供服务的企业内部研发应用不适用该办法。但个人信息、数据安全、知识产权、肖像和合同义务仍需独立评估。
- 本 Skill 不是法律意见。适用范围、敏感个人信息处理、跨境传输和未成年人事项应交由贵司法务或合格专业人士确认。

## 强制规则

1. 只识别素材中可直接观察、与检索管理或营销用途必要的客观信息。
2. 只能从 `allowed_tags.json` 选择自动标签，不得自由创造自然语言标签。
3. `restricted_tags.json` 中任何标签必须设置 `REVIEW_REQUIRED`。
4. 请求或模型候选命中 `forbidden_tags.json` 时拒绝对应标签；若任务目的本身要求敏感推断，则整单 `COMPLIANCE_REJECTED`。
5. 不得根据外貌、肤色、服装、环境、姿态或文字推断民族、国籍、宗教、政治、健康、性取向、经济状况、社会身份或具体人物身份。
6. 不做人脸识别，不输出姓名、联系方式、证件、精确地址或精确年龄。
7. 检测到人物时默认提高风险；疑似未成年人或年龄无法确定时标记 `POSSIBLE_MINOR` 或 `UNKNOWN`，不得猜测年龄，并强制人工审核。
8. Logo、水印、品牌名和第三方文字只能标记风险。授权状态必须来自素材中台的授权编号、地域、渠道、期限和权利人字段，不能从图片猜测。
9. 每个标签必须带直接证据和置信度。默认：`>=0.85` 可自动接受，`0.60-0.85` 转人工，`<0.60` 不输出；受限或高风险标签不受自动阈值豁免。
10. 输出必须通过 `tagging-output.schema.json`，并记录 Skill、模型、标签库、素材、审核、操作人与时间版本。

## 最低系统控制

- 上传前的数据分类、最小权限和外部模型出境/传输评估。
- CMS/DAM 层的标签白名单校验、审批、幂等回写和回滚。
- 授权书结构化字段与原件访问控制。
- 人工审核队列、双人复核条件、日志和留存期限。
- 定期金标抽检、错误集、模型漂移和标签库版本评审。

## 官方依据

- [生成式人工智能服务管理暂行办法](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm)
- [中华人民共和国个人信息保护法](https://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html)
- [互联网信息服务算法推荐管理规定](https://www.cac.gov.cn/2022-01/04/c_1642894606364259.htm)
""", encoding="utf-8")
    (base / "eval/acceptance.md").write_text("""# 智能打标验收

- [ ] 输入素材在授权范围内，外部模型、数据传输和保存边界已确认
- [ ] 所有自动标签均来自允许标签库，且有直接视觉或已授权元数据证据
- [ ] 受限标签全部进入人工审核，禁止标签未被输出
- [ ] 人物素材未做人脸身份、敏感属性、精确年龄或社会属性推断
- [ ] 疑似未成年人、正脸、Logo、水印和第三方文字已强制转人工
- [ ] 每个标签包含置信度、证据和来源，阈值规则执行正确
- [ ] 输出通过 JSON Schema，记录 Skill、模型、标签库、素材和审核版本
- [ ] 批量回写具备预览、幂等、审计、权限和回滚
- [ ] 明确标注 Skill 无法替代的权限、授权真实性和不可篡改审计控制
""", encoding="utf-8")


def write_jd_generation_resources(base):
    (base / "references/hr-role-training-checklist.md").write_text("""# HR 岗位理解与招聘预问检查表

## HR 必须先理解

- 这个岗位为什么存在，现在不招聘会造成什么业务后果。
- 岗位服务什么客户、商品、渠道、系统或内部流程。
- 一周中的典型工作、关键场景、真实交付物与衡量结果。
- 上游提供什么，下游依赖什么，岗位拥有什么决策权，不负责什么。
- 常用工具、系统、数据、专业术语及其业务含义。
- 初级、中级、资深和管理岗位在范围、复杂度、独立性与影响力上的区别。
- 什么表现代表优秀、勉强合格或明显不匹配。
- 哪些能力入职即需具备，哪些可以培训，哪些只是加分项。

## 建议向招聘经理预问

每个问题都必须记录：提问对象、提问目的、已知答案、理想答案要素、风险答案、对 JD 的影响和是否已确认。

1. 这个岗位入职后 6 至 12 个月必须解决的前三个问题是什么？
2. 最重要的三项可观察交付物是什么，谁验收，用什么标准验收？
3. 候选人每天、每周、每月实际会做什么，各占多少时间？
4. 岗位上下游分别是谁，最常见的协作冲突是什么？
5. 哪些决定可以独立做，哪些必须审批，预算或系统权限到什么程度？
6. 过往招聘或在岗人员最常被误解的地方是什么？
7. 哪些经历或作品能证明胜任，哪些表面关键词其实不能证明？
8. 哪些能力必须第一天具备，哪些可在 30/60/90 天内培养？
9. 什么情况属于一票否决，是否确实与岗位表现直接相关？
10. 职级、汇报线、团队规模、工作地点、用工方式、薪酬福利哪些已正式批准？

## 禁止直接发布的情况

- 岗位使命、前三项结果、汇报线或工作地尚未确认。
- 必须项无法对应可观察的工作证据。
- HR 与招聘经理对职级、职责或候选人画像仍有实质分歧。
- 薪酬、福利、远程安排或签证支持未经授权。
- 存在与岗位无关或可能构成歧视的筛选条件。
""", encoding="utf-8")
    (base / "references/job-market-research-method.md").write_text("""# 岗位市场与薪酬调研方法

## 必须锁定的口径

- 目标国家、城市或远程雇佣范围。
- 岗位族、常见同义名称、排除名称和职级。
- 观察窗口，默认优先近 3 个月，同时给出更长窗口作稳定性对照。
- 币种、税前或税后、月薪或年薪、固定薪酬、奖金、佣金、股权和福利是否包含。
- 全职、兼职、合同工、派遣或自由职业等用工方式。

## 来源与采集

1. 优先使用目标市场官方统计、主流招聘平台、专业薪酬数据库和可核验企业招聘页面。
2. 每条样本记录来源 URL、采集日期、发布日期、地点、岗位名称、职级、薪资上下限、周期、币种和备注。
3. 不得把搜索摘要、无日期聚合页或模型记忆当成当前薪资证据。
4. 去除重复职位、明显过期、地点不符、职级不明和薪资口径不可换算的样本；保留剔除数量与理由。
5. 不同来源分别统计后再综合，避免一个平台的行业、城市或企业样本偏差主导结论。

## 分布与解释

- 报告有效样本量、来源数、日期覆盖、缺失率和去重规则。
- 样本允许时给出最小值、P25、中位数、P75、最大值；样本不足时只给观察区间并降低置信度。
- 将年/月、币种和固定/浮动薪酬统一到明确口径，展示换算日期和汇率来源。
- 分析职级、经验、地区、行业、公司规模、工具技能、语言和管理职责带来的差异，但不得把相关性写成确定溢价因果。
- 将市场分布与贵司预算分开呈现；市场数据不等于薪酬决策或对候选人的承诺。

## 最低质量门槛

- 只有一个来源、样本过少或窗口过旧时，不得输出看似精确的分位数。
- 岗位名称相同但工作内容不同的样本必须拆分。
- 不能混用不同地区、币种、税前税后、月薪年薪、职级或用工方式。
- 无法取得可靠数据时交付检索记录、数据缺口和补充调研计划，不得编造分布。
""", encoding="utf-8")
    (base / "assets/delivery-template.md").write_text("""# 岗位说明书与招聘 JD 完整交付模板

## A. 招聘需求确认摘要

| 项目 | 已确认事实 | 来源/确认人 | 状态 | 对招聘的影响 |
|---|---|---|---|---|
| 招聘原因 |  |  | 已确认/待确认 |  |
| 工作地与用工主体 |  |  |  |  |
| 职级、编制与汇报线 |  |  |  |  |
| 预算与招聘时间 |  |  |  |  |

## B. 给 HR 的详细岗位培训说明

### 1. 用一句话讲清岗位

### 2. 为什么公司需要这个岗位

### 3. 业务场景与典型工作日

### 4. 主要任务与时间占比

### 5. 真实交付物、验收人与成功标准

### 6. 上下游、协作关系与决策权限

### 7. 工具、系统、数据与专业术语解释

### 8. 职级差异与 30/60/90 天预期

### 9. 优秀、合格和不匹配表现

### 10. HR 容易产生的误解及正确理解

## C. 岗位市场与薪酬调研摘要

- 目标市场与观察窗口：
- 岗位同义词与排除范围：
- 有效样本、来源与数据质量：
- 招聘需求趋势：
- 薪资分布与影响因素：
- 对职级、预算和 JD 的建议：
- 局限与待补数据：

## D. 建议预问问题

| 问题 | 提问对象 | 为什么问 | 理想答案要素 | 风险答案 | 对 JD 的影响 | 状态 |
|---|---|---|---|---|---|---|

## E. 内部岗位说明书

- 岗位名称与职级：
- 岗位使命：
- 核心业务结果：
- 职责与优先级：
- 决策权限：
- 不负责范围：
- 上下游与协作：
- 必须能力及证据：
- 可培养能力：
- 加分项：
- 成功指标：
- 风险与升级边界：

## F. 候选人版招聘 JD

- 关于团队与机会：
- 你将解决的问题：
- 你将负责的工作：
- 我们期待的业务结果：
- 必须具备：
- 可以入职后学习：
- 加分项：
- 工作地点、方式与流程：
- 已批准的薪酬福利信息：
- 包容性与隐私说明：

## G. 面试与发布建议

| 能力 | 可观察证据 | 建议问题/任务 | 评分锚点 | 风险信号 |
|---|---|---|---|---|

## H. 未确认项、审批与版本

| 未确认项/风险 | Owner | 截止时间 | 未确认前限制 |
|---|---|---|---|
""", encoding="utf-8")
    (base / "assets/job-market-research-template.md").write_text("""# 岗位市场与薪酬调研报告

## 1. 调研结论

- 目标岗位、职级与地区：
- 数据窗口与采集日期：
- 市场供需判断：
- 薪资分布结论：
- 对贵司职级、预算和招聘策略的影响：
- 结论置信度：高/中/低

## 2. 口径

| 项目 | 本报告定义 | 排除范围 |
|---|---|---|
| 岗位及同义词 |  |  |
| 地区/远程范围 |  |  |
| 职级/经验 |  |  |
| 薪资周期与币种 |  |  |
| 固定/浮动/股权 |  |  |
| 观察窗口 |  |  |

## 3. 数据来源与质量

| 来源 | URL | 采集日期 | 原始样本 | 去重后样本 | 局限 |
|---|---|---|---:|---:|---|

## 4. 招聘需求与岗位画像

| 月份/阶段 | 职位数量 | 主要地区 | 常见名称 | 常见职级 | 高频能力 |
|---|---:|---|---|---|---|

## 5. 薪资分布

| 分组 | 样本量 | 最小值 | P25 | 中位数 | P75 | 最大值 | 统一口径 |
|---|---:|---:|---:|---:|---:|---:|---|

## 6. 分层差异

| 因素 | 观察差异 | 样本证据 | 可否用于决策 | 限制 |
|---|---|---|---|---|

## 7. 对招聘方案的影响

- 建议岗位名称与职级：
- 建议预算位置及理由：
- 必须能力与可培养能力调整：
- 渠道与寻访建议：
- 需要招聘经理或财务确认：

## 8. 偏差、反证与补充计划

- 样本偏差：
- 不可比项：
- 与结论冲突的证据：
- 下一次刷新时间：
""", encoding="utf-8")
    (base / "assets/blank-jd-template.md").write_text("""# JD 空白模板

> 本模板只保留结构与填写说明，不预填任何未经确认的岗位事实。

## 岗位基本信息

- 岗位名称：
- 所属部门：
- 汇报对象：
- 工作地点：
- 用工方式：
- 职级：

## 关于团队与岗位机会

<!-- 用候选人能理解的语言说明团队做什么、为什么现在招聘，不使用内部黑话。 -->

## 岗位使命

<!-- 用一句话说明该岗位为谁解决什么问题、产生什么结果。 -->

## 你将负责

1. （填写职责）
2. （填写职责）
3. （填写职责）

## 入职后期待的结果

- 30 天：
- 60 天：
- 90 天：
- 6 至 12 个月：

## 必须具备

<!-- 每项必须能对应工作证据，不写无法解释的年限或关键词堆砌。 -->

- （填写必须能力）

## 可以入职后学习

- （填写可培养能力）

## 加分项

- （填写加分项）

## 协作关系与工作方式

- （填写协作关系）

## 薪酬、福利与招聘流程

<!-- 只填写已批准且适合当地披露的信息。 -->

- （填写已批准信息）

## 包容性与候选人隐私

<!-- 使用贵司批准文本，并按工作地要求复核。 -->
""", encoding="utf-8")
    (base / "eval/acceptance.md").write_text("""# JD 生成专家验收

- [ ] 先生成了 HR 岗位培训说明，而不是直接套模板输出 JD
- [ ] 详细解释岗位存在原因、业务场景、典型工作、交付物、上下游、工具术语、职级差异和常见误解
- [ ] 薪酬调研锁定地区、职级、币种、税前税后、周期、固定与浮动薪酬及近几个月观察窗口
- [ ] 调研报告披露来源、采集日期、有效样本、去重、分位数、偏差、置信度和无法比较项
- [ ] 市场数据与贵司预算、薪酬决策和候选人承诺明确分开
- [ ] 预问问题包含提问目的、理想答案要素、风险答案及其对 JD 的影响
- [ ] 关键事实未确认时明确暂停发布，没有自行补全
- [ ] 内部岗位说明书明确使命、结果、职责、权限、不负责范围和 30/60/90 天预期
- [ ] 候选人版 JD 区分必须具备、可培养和加分项，并为必须项提供可观察证据
- [ ] 同时交付了不含虚构事实的 `blank-jd-template.md`
- [ ] 未虚构薪酬、福利、编制、远程、签证或组织承诺
- [ ] 已检查与岗位无关的限制、歧视风险、隐私和工作地合规
- [ ] 输出包含招聘经理确认、发布审批、版本和未确认项
""", encoding="utf-8")
    readme_path = base / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    marker = "- `assets/delivery-template.md`：可直接复用的交付模板。"
    addition = marker + "\n- `assets/job-market-research-template.md`：岗位需求与近期薪酬分布调研报告模板。\n- `assets/blank-jd-template.md`：不预填岗位事实的可复制 JD 空白模板。\n- `references/hr-role-training-checklist.md`：HR 岗位培训与招聘经理预问清单。\n- `references/job-market-research-method.md`：岗位市场样本、薪资口径、分布统计与质量门槛。"
    readme_path.write_text(readme.replace(marker, addition, 1), encoding="utf-8")


for item in SPECS:
    write_skill(item)

# Keep migrated first-level business categories aligned with their physical browse path.
for business_root in [ROOT / "渠道运营", ROOT / "精准营销", ROOT / "仓储库存", ROOT / "市场采购"]:
    if not business_root.exists():
        continue
    for meta_path in business_root.rglob("skill.json"):
        data = json.loads(meta_path.read_text(encoding="utf-8"))
        data["category_path"] = list(meta_path.parent.relative_to(ROOT).parts[:-1])
        meta_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        readme_path = meta_path.parent / "README.md"
        if readme_path.exists():
            readme = readme_path.read_text(encoding="utf-8")
            category_text = " / ".join(data["category_path"])
            readme = __import__("re").sub(r"> 所属分类：[^\n]+", f"> 所属分类：{category_text}", readme, count=1)
            readme_path.write_text(readme, encoding="utf-8")

CATEGORIES = {
    "互联网研发/产品/系统产品架构": ("系统产品架构", "互联网研发产品职能下的企业业务系统产品架构，覆盖跨系统总架构和各系统专项架构。"),
    "互联网研发/前端/架构": ("前端通用架构", "沉淀与语言和框架无关的前端边界、运行时、质量属性和演进方法。"),
    "互联网研发/前端/UI交互": ("UI 交互", "设计页面组件状态、操作路径、反馈、动效、可访问性以及可供前端实现测试的交互规范。"),
    "互联网研发/前端/语言": ("前端语言架构", "处理 JavaScript、TypeScript 等语言自身的模块、类型、运行时和工程约束。"),
    "互联网研发/前端/语言/JavaScript": ("JavaScript 前端架构", "治理动态类型、模块系统、异步运行时和依赖供应链。"),
    "互联网研发/前端/语言/TypeScript": ("TypeScript 前端架构", "治理类型边界、项目引用、模块解析和编译性能。"),
    "互联网研发/前端/框架": ("前端框架架构", "在通用架构与语言架构之上处理具体框架的运行语义。"),
    "互联网研发/前端/框架/React": ("React 架构", "处理 React 组件、状态、数据流、渲染和测试边界。"),
    "互联网研发/前端/框架/Vue": ("Vue 架构", "处理 Vue 组件、组合式逻辑、响应式状态和工程边界。"),
    "互联网研发/前端/框架/Next.js": ("Next.js 架构", "处理 App Router、Server/Client Components、缓存、SEO 和部署。"),
    "互联网研发/前端/框架/Angular": ("Angular 架构", "处理 standalone components、signals、依赖注入、路由和混合渲染。"),
    "互联网研发/前端/框架/SvelteKit": ("SvelteKit 架构", "处理文件路由、load、form actions、服务端边界和 adapter。"),
    "互联网研发/后端/架构": ("后端通用架构", "沉淀语言无关的领域边界、质量属性、数据 ownership 和演进路线。"),
    "互联网研发/后端/语言": ("后端语言架构", "按 Java、Go、Python、Node.js 的运行模型和生态细化架构。"),
    "互联网研发/后端/语言/Java": ("Java 后端架构", "处理 Java 模块、并发、JVM 和长期演进。"),
    "互联网研发/后端/语言/Go": ("Go 后端架构", "处理 Go 包边界、并发、取消、错误和资源生命周期。"),
    "互联网研发/后端/语言/Python": ("Python 后端架构", "处理 Python 包、类型、同步异步和运行环境。"),
    "互联网研发/后端/语言/Node.js": ("Node.js 后端架构", "处理事件循环、模块格式、异步失败和资源限制。"),
    "互联网研发/后端/语言/PHP": ("PHP 后端架构", "处理 namespace、Composer、请求生命周期和模块边界。"),
    "互联网研发/后端/语言/Rust": ("Rust 后端架构", "处理 ownership、类型、错误、async runtime 和 unsafe 边界。"),
    "互联网研发/后端/语言/C#": ("C# 后端架构", "处理 solution、类型、异步、资源和 .NET 运行时。"),
    "互联网研发/后端/框架": ("后端框架架构", "在通用和语言架构上处理具体框架的模块、依赖和生产能力。"),
    "互联网研发/后端/框架/Spring Boot": ("Spring Boot 架构", "处理模块、依赖注入、事务、安全和生产可观测。"),
    "互联网研发/后端/框架/FastAPI": ("FastAPI 架构", "处理 APIRouter、Depends、Pydantic、异步和部署。"),
    "互联网研发/后端/框架/NestJS": ("NestJS 架构", "处理 module、provider、请求管道和集成边界。"),
    "互联网研发/后端/框架/Gin": ("Gin 架构", "处理路由、middleware、显式依赖和 Go HTTP 运行时。"),
    "互联网研发/后端/框架/Laravel": ("Laravel 架构", "处理领域模块、容器、Eloquent、队列和请求生命周期。"),
    "互联网研发/后端/框架/ASP.NET Core": ("ASP.NET Core 架构", "处理 host、DI、middleware、endpoint 和生产运行。"),
    "精准营销/市场策略": ("市场与战略", "覆盖市场情报、机会判断、上市和跨市场策略。"),
    "精准营销/品牌营销": ("品牌营销", "覆盖品牌定位、价值证据和跨文化表达。"),
    "渠道运营/平台运营": ("渠道运营", "覆盖渠道组合与各平台端到端经营。"),
    "渠道运营/平台运营/亚马逊": ("亚马逊运营", "覆盖 Amazon 账户、目录、流量、广告、库存和利润。"),
    "渠道运营/平台运营/独立站": ("独立站运营", "覆盖 Shopify 商品、流量、转化、订单和客户经营。"),
    "渠道运营/平台运营/TikTok Shop": ("TikTok Shop 运营", "覆盖内容、直播、达人、广告、商品和履约联动。"),
    "精准营销/内容营销": ("内容营销", "覆盖主题策略、编辑日历、分发、转化和衡量。"),
    "精准营销/社媒营销": ("社媒营销", "覆盖平台内容、社区互动、自然增长和账号健康。"),
    "精准营销/达人联盟": ("达人与联盟", "覆盖发现、筛选、合作、授权、佣金和增量效果。"),
    "精准营销/用户运营": ("用户运营", "覆盖邮件生命周期、购后、召回、会员和忠诚度。"),
    "精准营销/活动营销": ("活动营销", "覆盖跨市场促销日历、资源统筹和活动复盘。"),
    "渠道运营/商品运营": ("商品运营", "覆盖平台商品信息、搜索发现和转化表达。"),
    "渠道运营/客户体验": ("客户体验", "覆盖售后体验、评价、声誉、退款异常和 VOC 改进闭环；购买前咨询由客服售前负责。"),
    "渠道运营/商业化": ("商业化", "覆盖定价、折扣、促销和单位经济。"),
    "精准营销/增长营销": ("增长营销", "覆盖归因、获客、转化、留存和跨团队增长。"),
    "精准营销/增长营销/拉新": ("拉新增长", "管理新客定义、人群渠道、首购漏斗、CAC、回收期和增量验证。"),
    "数据看板/业务分析": ("跨境业务数据分析", "覆盖指标、经营、利润、商品、流量、漏斗、广告、客户、库存和预测。"),
    "数据看板/数据治理": ("数据治理", "覆盖数据质量、跨系统对账、口径和责任治理。"),
    "互联网研发/产品/系统产品架构/公共": ("跨系统产品边界", "沉淀跨系统能力分工、主数据归属、交接契约和端到端异常闭环。"),
    "互联网研发/产品/系统产品架构/OMS": ("OMS 产品架构", "订单管理系统的产品架构和后续细分 Skill。"),
    "互联网研发/产品/系统产品架构/IMS": ("IMS 产品架构", "库存管理系统的产品架构和后续细分 Skill。"),
    "互联网研发/产品/系统产品架构/OFS": ("OFS 产品架构", "订单履约系统的产品架构和后续细分 Skill。"),
    "互联网研发/产品/系统产品架构/CMS": ("CMS 产品架构", "商品/内容管理系统的产品架构和后续细分 Skill。"),
    "互联网研发/产品/系统产品架构/TMS": ("TMS 产品架构", "运输管理系统的产品架构和后续细分 Skill。"),
    "互联网研发/产品/系统产品架构/CRM": ("CRM 产品架构", "客户关系系统的产品架构和后续细分 Skill。"),
    "互联网研发/产品/系统产品架构/PLM": ("PLM 产品架构", "产品生命周期系统的产品架构和后续细分 Skill。"),
    "互联网研发/产品/系统产品架构/WMS": ("WMS 产品架构", "仓储管理系统的产品架构和后续细分 Skill。"),
    "创拍视觉": ("创拍视觉", "覆盖创意、拍摄、视觉与广告素材全链路，包括策略、制片统筹、商品摄影、短视频、UGC、后期、素材资产、智能打标与 AIGC 创意制作。参见 [创拍视觉 Skill 地图](CREATIVE_VISUAL_SKILLS_MAP.md)。"),
    "创拍视觉/创意角色": ("创拍视觉主角色", "沉淀创拍视觉资深经理及专属周报 Skill。"),
    "创拍视觉/创意策略": ("创意策略", "把人群洞察、产品证据和平台语法转化为可制作、可测试的创意方案。"),
    "创拍视觉/拍摄统筹": ("拍摄统筹", "管理预算、排期、样品、人员、供应商、场地、设备和现场安全。"),
    "创拍视觉/商品摄影": ("商品摄影", "管理主图、细节、场景、模特摄影与商品真实性。"),
    "创拍视觉/短视频制作": ("短视频制作", "管理广告、社媒和商品短视频的脚本、分镜、拍摄、声音和版本测试。"),
    "创拍视觉/UGC制作": ("UGC 与达人内容制作", "管理创作者、寄样、brief、拍摄反馈、授权和交付。"),
    "创拍视觉/拍摄制作": ("图片与视频拍摄制作", "统筹商品图片视频的整体拍摄、后期、验收和交付项目。"),
    "创拍视觉/后期交付": ("后期交付", "管理选片、剪辑、修图、调色、声音、字幕、本地化和多规格交付。"),
    "创拍视觉/素材运营": ("创意素材运营", "管理素材需求、标签、版本、授权、分发、表现回流和复用。"),
    "创拍视觉/AI创意制作": ("AI 创意制作", "以工具编排、商品真实性、生成血缘和人工质量门禁管理 AI 内容生产。"),
    "创拍视觉/AI创意制作/虚拟模特": ("虚拟模特", "管理人像生成、模特替换、虚拟试穿、授权和商品一致性。"),
    "创拍视觉/AI创意制作/AIGC制作": ("AIGC 创意制作", "管理文生图、图生图、文生视频、图生视频、局部修改、批量变体和成片交付。"),
    "创拍视觉/AI创意制作/智能打标": ("创意素材智能打标", "管理素材标签体系、模型建议、人审、批量回写、质量抽检、版本和效果标签闭环。"),
    "创拍视觉/AI创意制作/智能剪辑": ("智能剪辑", "管理镜头识别、粗剪、字幕、比例、多语言和批量版本。"),
    "创拍视觉/AI创意制作/真实性合规": ("AI 创意真实性与合规", "审查商品失真、人物权利、版权、披露、平台与生成证据。"),
    "仓储库存": ("仓储库存", "覆盖供应链与仓储主角色、库存计划、入出库、库存控制、分配、履约物流、逆向、仓容安全和跨系统对账。参见 [仓储库存 Skill 地图](WAREHOUSE_INVENTORY_SKILLS_MAP.md)。"),
    "仓储库存/仓储角色": ("仓储库存主角色", "沉淀供应链资深经理、仓储库存资深经理及各自专属周报 Skill。"),
    "仓储库存/库存计划": ("库存与补货计划", "管理需求、提前期、安全库存、订货点、在途和资金仓容约束。"),
    "仓储库存/入库管理": ("入库管理", "管理预约、到货、收货、差异、质检交接、上架和状态生效。"),
    "仓储库存/出库履约": ("出库履约", "管理释放、波次、拣选、复核、包装、称重、面单和交接。"),
    "仓储库存/库存控制": ("库存控制", "管理库存准确、盘点、冻结、差异、调整、损耗和审计。"),
    "仓储库存/库存分配": ("库存分配", "管理多仓多渠道配额、调拨、服务水平、成本和超卖风险。"),
    "仓储库存/履约物流": ("履约物流", "管理仓配、承运、时效、费用、轨迹、异常和客户承诺。"),
    "仓储库存/逆向物流": ("逆向物流", "管理退货、检验、分级、退款证据、再售、报废和追偿。"),
    "仓储库存/仓容安全": ("仓容与安全", "管理库位容量、动线、设备、人员、消防、危险品和连续性。"),
    "市场采购": ("市场采购", "覆盖市场采购主角色、市场机会、选品、样品、供应商质量、成本谈判、采购执行和采购风险。参见 [市场采购 Skill 地图](MARKET_PROCUREMENT_SKILLS_MAP.md)。"),
    "市场采购/采购角色": ("市场采购主角色", "沉淀选品与商品资深经理、市场采购资深经理及各自专属周报 Skill。"),
    "市场采购/市场机会": ("市场机会", "管理消费者需求、竞争、价格带、单位经济、供应和反证。"),
    "市场采购/选品": ("选品", "管理跨境商品机会研究、验证、评分、试点和退出。"),
    "市场采购/样品验证": ("样品验证", "管理打样、比样、测试、问题关闭、封样和量产放行。"),
    "市场采购/供应商与质量": ("供应商与质量", "管理供应商发现、准入、能力、质量、绩效和替代。"),
    "市场采购/商务谈判": ("商务谈判", "管理成本拆解、报价、MOQ、阶梯价、账期、交期和商务换项。"),
    "市场采购/采购执行": ("采购执行", "管理采购申请、订单、生产、质检、交付、付款证据、变更和关闭。"),
    "市场采购/采购风险": ("采购风险", "管理供应商合规、集中度、产能、质量、连续性和退出风险。"),
}

for deprecated_category in [
    "互联网研发/前端/语言",
    "互联网研发/前端/语言/JavaScript",
    "互联网研发/前端/语言/TypeScript",
    "互联网研发/前端/框架/Vue",
    "互联网研发/前端/框架/Next.js",
    "互联网研发/前端/框架/Angular",
    "互联网研发/前端/框架/SvelteKit",
]:
    CATEGORIES.pop(deprecated_category, None)
CATEGORIES["互联网研发/前端/框架/React"] = ("React 资深专家", "React 高级架构、实现、诊断、性能、测试和演进能力。")
CATEGORIES["互联网研发/前端/框架/Vue3"] = ("Vue3 资深专家", "Vue 3 高级架构、实现、诊断、性能、测试和演进能力。")

CATEGORIES.update({
    "互联网研发/产品/数据产品": ("数据产品", "覆盖标签、指标、数据工作流、权限、版本、质量和治理产品。"),
    "渠道运营": ("渠道运营", "以平台、店铺、商品、商业化和客户体验为核心，对渠道收入、利润和经营健康负责。参见 [渠道运营 Skill 地图](CHANNEL_OPERATIONS_SKILLS_MAP.md)。"),
    "渠道运营/运营角色": ("渠道运营主角色", "沉淀渠道经营主角色 Skill，并由主角色编排各专项执行 Skill。"),
    "客服售前": ("客服售前", "覆盖购买前咨询、商品推荐、多语言沟通、知识库、线索分级、质检培训与销售交接。参见 [客服售前 Skill 地图](CUSTOMER_PRESALES_SKILLS_MAP.md)。"),
    "客服售前/客服角色": ("客服售前主角色", "沉淀客服售前资深经理及专属周报 Skill。"),
    "客服售前/客服角色/客服售前资深经理": ("客服售前资深经理", "统筹跨渠道售前服务、知识、质量、线索与销售交接。"),
    "客服售前/客服运营": ("客服运营", "管理跨渠道、多语言客服接待、话术、权限、升级与客户声音。"),
    "精准营销": ("精准营销", "以人群、内容、触达、转化、留存和增量衡量为核心，对营销效率和客户价值负责。参见 [精准营销 Skill 地图](PRECISION_MARKETING_SKILLS_MAP.md)。"),
    "精准营销/营销角色": ("精准营销主角色", "沉淀品牌内容和增长营销主角色 Skill，并由主角色编排各专项执行 Skill。"),
    "法律政务": ("法律政务", "覆盖跨境法务主角色、合同、监管、知识产权、隐私、广告消费者保护、用工、争议和公司治理。参见 [法律 Skill 地图](LEGAL_SKILLS_MAP.md)。"),
    "法律政务/法律角色": ("法律主角色", "沉淀跨境法务资深经理及专属周报 Skill。"),
    "法律政务/法律角色/跨境法务资深经理": ("跨境法务资深经理", "统筹跨境法律风险、专项审查和外部律师升级。"),
    "法律政务/跨境监管": ("跨境监管", "识别国家、主体、产品、渠道和贸易监管责任。"),
    "法律政务/进出口合规": ("进出口合规", "审查商品、主体、路线、海关、制裁、出口管制和报关证据。"),
    "法律政务/美国合规": ("美国市场合规", "识别美国进口、产品主管机构、广告消费者保护、隐私和州级差异。"),
    "法律政务/欧盟合规": ("欧盟市场合规", "识别欧盟经济运营商、产品安全、CE、标签、VAT、数据和消费者责任。"),
    "法律政务/知识产权": ("知识产权", "管理商标、版权、专利、外观、域名和授权链。"),
    "法律政务/隐私与数据": ("隐私与数据", "管理数据处理、同意、跨境传输、请求和事件。"),
    "法律政务/广告与消费者保护": ("广告与消费者保护", "审查声明、评价、达人披露、促销和消费者规则。"),
    "法律政务/劳动用工": ("劳动用工", "审查跨区域员工、承包商和劳动流程风险。"),
    "法律政务/争议解决": ("争议解决", "管理事实、证据、时效、策略和外部律师协同。"),
    "法律政务/公司治理": ("公司治理", "管理实体、授权、决议、利益冲突和法定档案。"),
    "财务出纳": ("财务出纳", "覆盖跨境财务治理以及出纳收付款、银行对账、报销票据和资金安全。参见 [财务与出纳 Skill 地图](FINANCE_SKILLS_MAP.md)。"),
    "财务出纳/财务角色": ("财务主角色", "沉淀跨境财务资深经理及专属周报 Skill。"),
    "财务出纳/财务角色/跨境财务资深经理": ("跨境财务资深经理", "统筹会计、管理报表、预算、现金、税务、外汇和内控。"),
    "财务出纳/核算关账": ("核算关账", "管理平台、支付、银行、库存和总账关账对账。"),
    "财务出纳/预算管理": ("预算管理", "管理驱动型预算、滚动预测和差异纠偏。"),
    "财务出纳/资金管理": ("资金管理", "管理现金、营运资金、多币种头寸和汇率风险。"),
    "财务出纳/税务合规": ("税务合规", "管理跨境 VAT、销售税、关税和税务证据。"),
    "财务出纳/经营财务": ("经营财务", "连接财务账、商品渠道单位经济和经营决策。"),
    "财务出纳/出纳角色": ("出纳主角色", "沉淀资金出纳资深经理及专属周报 Skill，承担资金执行而非账务审批。"),
    "财务出纳/出纳角色/资金出纳资深经理": ("资金出纳资深经理", "统筹收付款、银行账户、票据、日结和资金安全。"),
    "财务出纳/收付款": ("收付款", "管理申请、审批、执行、回单、状态和异常闭环。"),
    "财务出纳/银行与对账": ("银行与出纳对账", "管理银行账户、日记账、余额和未达账项。"),
    "财务出纳/报销与票据": ("报销与票据", "管理报销、备用金、票据和支付凭证。"),
    "财务出纳/资金安全": ("资金安全", "管理支付分权、限额、UKey、印鉴、反欺诈和应急。"),
    "人事招聘": ("人事招聘", "覆盖人事招聘资深经理、编制规划、人才寻访、面试评估、录用入职、员工生命周期和员工关系。参见 [人事招聘 Skill 地图](HR_RECRUITING_SKILLS_MAP.md)。"),
    "人事招聘/公共": ("人事招聘公共能力", "提供日常人事招聘任务的统一接管、分类、路由和交接入口。"),
    "人事招聘/人事角色": ("人事招聘主角色", "沉淀人事招聘资深经理及专属周报 Skill。"),
    "人事招聘/人事角色/人事招聘资深经理": ("人事招聘资深经理", "统筹组织编制、招聘、入离职、档案、绩效协同和员工关系。"),
    "人事招聘/招聘规划": ("招聘规划", "把业务目标、组织能力和预算转化为编制与招聘计划。"),
    "人事招聘/岗位与JD": ("岗位与 JD", "把岗位事实和成功标准转化为内部岗位说明书、招聘 JD 与评估证据。"),
    "人事招聘/人才寻访": ("人才寻访", "管理人才画像、渠道、人才地图、触达和候选人关系。"),
    "人事招聘/面试评估": ("面试评估", "设计结构化面试、工作样本、评分锚点和校准机制。"),
    "人事招聘/录用入职": ("录用入职", "管理录用审批、Offer、背景核验和入职交接。"),
    "人事招聘/员工生命周期": ("员工生命周期", "管理员工主档、异动、合同、离职、权限和档案。"),
    "人事招聘/员工关系": ("员工关系", "管理目标反馈、绩效改进、诉求、调查和沟通流程。"),
    "人事招聘/员工沟通": ("员工沟通", "撰写和治理员工公告、政策通知、组织沟通及发布审批。"),
    "人事招聘/培训发展": ("培训发展", "端到端管理培训需求、计划预算、课程讲师、通知报名、现场执行、效果评估和学习档案。"),
})
for role_area, folder, _role_id, display, _positioning, _lenses in ROLE_DEFS:
    CATEGORIES[f"{role_area}/{folder}"] = (display, f"{display}主角色、责任边界和配套周报 Skill。")


def category_readme(relative, title, summary):
    directory = ROOT / relative
    directory.mkdir(parents=True, exist_ok=True)
    rows = []
    for meta in sorted(directory.rglob("skill.json")):
        data = json.loads(meta.read_text(encoding="utf-8"))
        skill_dir = meta.parent.relative_to(directory)
        rows.append(f"- [{data['display_name']}]({skill_dir.as_posix()}/README.md)：{data['description']}")
    top = Path(relative).parts[0]
    if top == "法律政务":
        principles = ["先确认司法辖区、主体、适用时间和授权边界。", "复杂或高风险事项以跨境法务资深经理为主 Skill，专项 Skill 提供深度审查。", "Skill 不替代正式法律意见；明确外部律师升级条件。"]
    elif top == "财务出纳":
        principles = ["先确认主体、期间、币种、账户、账簿和授权边界。", "跨境财务资深经理负责会计治理，资金出纳资深经理负责授权范围内的资金执行。", "申请、审批、付款、记账和对账必须职责分离；预估和未达账必须明确标记。"]
    elif top == "人事招聘":
        principles = ["先确认业务目标、组织范围、工作地、用工主体、编制和岗位成功标准。", "人事招聘资深经理负责目标与编排，专项 Skill 负责规划、寻访、面试、录用和员工流程。", "坚持岗位相关、数据最小化和一致标准；劳动法律事项升级法务和当地专业人士。"]
    elif top == "客服售前":
        principles = ["先确认国家、渠道、语言、商品事实源、服务阶段和坐席权限。", "客服售前负责购买前咨询、推荐和线索交接；渠道运营负责店铺经营与售后体验，市场采购和仓储库存提供商品与库存事实。", "不得为转化虚构功能、现货、折扣或送达承诺；敏感语言和高风险声明必须人工复核。"]
    elif top in {"渠道运营", "精准营销"}:
        principles = ["主角色 Skill 负责目标、取舍、协同和验收，专项 Skill 负责深度执行。", "所有增长动作同时受利润、库存、合规、履约和客户体验约束。", "数字结论必须组合数据看板或财务口径验证。"]
    elif top == "创拍视觉":
        principles = ["主角色负责需求、产能、预算、质量和交付，专项 Skill 负责策略、拍摄、AI 制作、后期或资产治理。", "所有素材必须锁定商品事实、使用范围、授权、版本和质量门禁。", "AI 生成、虚拟模特和智能剪辑必须保留模型与修改血缘，并经过人工真实性和合规复核。"]
    elif top == "仓储库存":
        principles = ["先确认货主、仓库、库存状态、实物时间点和系统事实源。", "仓储库存负责补货后的实物与库存执行，渠道运营提供需求和承诺，市场采购负责供应与采购。", "实物、单据和系统状态不一致时必须隔离、对账和留痕，不得无证据调平。"]
    elif top == "市场采购":
        principles = ["先确认市场需求、商品定义、目标成本、销量假设、现金和合规边界。", "按机会、样品、供应商、成本、合规和量产阶段门逐步验证。", "市场采购负责选品与供应，仓储库存负责入库后的库存作业，渠道运营负责销售经营。"]
    else:
        principles = ["先用上层通用 Skill 定义边界、口径和总体方案，再用语言、框架、渠道或系统 Skill 深化。", "一个任务可以组合多个 Skill，但必须指定主 Skill，避免重复 ownership。", "README 是中文产品文档；执行时先读对应 Skill 的 `SKILL.md`。"]
    principle_lines = "\n".join(f"- {line}" for line in principles)
    body = f"""# {title}

## 分类定位

{summary}

## 选择原则

{principle_lines}

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

PROJECT_LINKS = {
    "OMS": ("订单管理系统项目", "oms-product-architecture"),
    "IMS": ("库存管理系统项目", "ims-product-architecture"),
    "OFS": ("订单履约系统项目", "ofs-product-architecture"),
    "CMS": ("商品/内容管理系统项目，具体缩写口径以公司定义为准", "cms-product-architecture"),
    "WMS": ("仓储管理系统项目", "wms-product-architecture"),
    "TMS": ("运输管理系统项目", "tms-product-architecture"),
    "CRM": ("客户关系管理系统项目", "crm-product-architecture"),
    "PLM": ("产品生命周期管理系统项目", "plm-product-architecture"),
}
for code, (positioning, skill_name) in PROJECT_LINKS.items():
    target = f"../../互联网研发/产品/系统产品架构/{code}/{skill_name}/README.md"
    (ROOT / f"项目管理/{code}/README.md").write_text(f"""# {code} 项目

## 项目定位

{positioning}。本目录是公司项目浏览与未来项目资料入口，不存放研发职能 Skill。

## 对应产品架构 Skill

- [{code} 产品架构师]({target})：归属于 `互联网研发 / 产品 / 系统产品架构 / {code}`。

## 后续维护

- 在这里维护公司内部项目范围、里程碑、负责人、上下游和项目文档导航。
- 产品方法、能力地图、状态机和系统边界由产品架构 Skill 维护。

## 版本记录

| 版本 | 日期 | 更新内容 |
|---|---|---|
| 2.0.0 | {DATE} | 将产品架构 Skill 迁入互联网研发产品分类，本目录保留项目导航。 |
""", encoding="utf-8")

(ROOT / "项目管理/公共/README.md").write_text(f"""# 项目公共能力

本目录只承载跨项目管理资料和导航。跨系统产品架构 Skill 已迁至互联网研发产品职能：

- [跨系统产品边界设计师](../../互联网研发/产品/系统产品架构/公共/commerce-systems-product-architecture/README.md)
- [系统产品架构地图](../../互联网研发/产品/系统产品架构/SYSTEM_PRODUCT_ARCHITECTURE_MAP.md)

## 版本记录

| 版本 | 日期 | 更新内容 |
|---|---|---|
| 2.0.0 | {DATE} | 将产品架构能力迁至互联网研发产品分类。 |
""", encoding="utf-8")

# The browser ZIP builder can fetch files but cannot fetch a directory path.
# Normalize every formal package to an explicit, deterministic file manifest.
for meta_path in ROOT.rglob("skill.json"):
    if meta_path.relative_to(ROOT).parts[0] in {"templates", "work"}:
        continue
    data = json.loads(meta_path.read_text(encoding="utf-8"))
    distribution = data.get("distribution")
    if not isinstance(distribution, dict):
        continue
    entries = distribution.get("package_files") or distribution.get("required_files") or []
    files = []
    for relative in entries:
        candidate = meta_path.parent / relative
        if candidate.is_dir():
            files.extend(
                child.relative_to(meta_path.parent).as_posix()
                for child in candidate.rglob("*") if child.is_file()
            )
        elif candidate.is_file():
            files.append(Path(relative).as_posix())
    distribution["package_files"] = sorted(set(files))
    meta_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"Built {len(SPECS)} complete skill packages and {len(CATEGORIES)} category docs")
