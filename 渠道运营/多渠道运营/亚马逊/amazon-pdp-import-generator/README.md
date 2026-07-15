# 亚马逊 PDP 导入草稿生成器

> skill id：amazon-pdp-import-generator
> 当前版本：2.0.3
> 产品状态：可用
> 所属分类：渠道运营 / 多渠道运营 / 亚马逊

## 产品定位

将结构化商品图片与真实商品资料转换为可审计的 SKU、变体和图片分组，并结合当前市场 Rank、搜索趋势、SEO/GEO 关键词研究生成 Amazon PDP 草稿和上线前自检报告。

## 解决的问题

- 人工按文件名整理 SKU、父子体和主附图耗时且容易错配
- 图片解析推断与真实商品事实容易混在一起，导致不实 listing 声明
- 通用草稿经常被误认为当前站点和类目可直接上传的模板
- 标题、五点和 Search Terms 只凭经验写，没有当前关键词、搜索意图、竞品和趋势证据
- 把 BSR、关键词自然位、广告位和趋势榜混为一谈，或把单次快照写成近期趋势
- 有内容生成但缺少事实、SEO、GEO、字段限制、变体和合规的系统自检

## 适用场景

- 批量整理 Amazon 商品图片并生成 CSV/XLSX 草稿
- 检查 SKU、颜色变体、主图和附图分组
- 基于已验证商品规格生成标题、五点、描述和 Search Terms
- 新品或改版前调研当前市场 Rank、竞品结构、搜索建议与近期趋势
- 建立 SEO 关键词布局、GEO 语义与问答覆盖，并生成自检报告

## 合规与权限

- 合规配置：`channel-commerce`（渠道经营合规基线）。
- 执行前必须读取 `references/compliance-baseline.md`，完成司法辖区、数据、权限、授权、人工复核和审计检查。
- Skill 只能提供第一层规则约束，不能替代系统权限、真实授权、正式审批或专业法律意见。

## 不适用范围与边界

- 不从图片或文件名推断材质、性能、认证、尺寸、安全或兼容性
- 未映射当前 Seller Central 类目模板前，不宣称可以直接上传
- 解析冲突或低置信度行必须保留给人工复核
- 没有本次执行采集的来源和时间，不得声称 Rank 或趋势是实时、当前或近几个月数据
- 不保证关键词排名、索引、推荐或 AI 引用，不使用无关热词和竞品商标

## 输入

- 商品图片目录绝对路径
- 可选品牌、站点、类目和变体主题
- 生成内容时需要真实商品规格与声明证据
- 目标站点、类目、语言、价格带和竞争范围
- 可选 Seller Central、Brand Analytics、Search Query Performance 或第三方研究数据访问
- 可选使用者关键词库；生成前必须确认是否优先参考及优先模式

## 输出

- amazon_pdp_import_draft.xlsx
- amazon_pdp_import_draft.csv
- parse_log.csv
- 低置信度与缺失商品事实复核说明
- market_keyword_research.md
- pdp_self_check_report.md

## 工作原理

1. 按命名规则扫描并拆解图片文件名
2. 按 SKU 聚合图片并确定主图顺序
3. 生成 CSV、包含 Parse_Log 工作表的 XLSX 和独立解析日志
4. 人工确认解析推断，再加载真实商品事实
5. 获取并记录本次执行的市场 Rank、查询位置、趋势与竞品证据
6. 建立 SEO/GEO 关键词地图并映射到 PDP 字段
7. 生成 listing 草稿，执行事实、关键词、字段、变体、合规和模板自检

## 深度执行标准

- 覆盖完整业务理解、主场景与相邻变体、上下游、方案取舍、工具失败、异常、交付、验收和复盘。
- 复杂任务先读 `references/scenario-playbook.md`；存在决策或审批时使用 `assets/decision-record-template.md`。
- 不以篇幅代替深度，每项判断必须关联真实对象、证据、责任和结果。

## 技能包组成

- scripts/generate_pdp_import.py：确定性解析与表格生成
- assets/parser_config.json：文件名、图片角色和字段配置
- assets/content-guardrails.md：商品声明边界
- references/market-rank-trend-method.md：Rank 类型、竞品、趋势窗口和实时证据方法
- references/seo-geo-keyword-method.md：SEO/GEO 关键词研究与字段映射方法
- assets/market-keyword-research-template.md：市场、Rank、趋势和关键词研究模板
- assets/keyword-library-intake-template.md：生成前询问关键词库及使用者优先策略
- assets/pdp-self-check-checklist.md：PDP 上线前完整自检
- examples/：输入输出样例
- eval/acceptance.md：解析与内容验收

通用入口文件：

- SKILL.md：AI 执行入口与专业工作流
- skill.json：机器可读元数据
- INVOCATION.md：标准调用顺序与失败处理
- BASE_PROMPT.md：跨平台执行原则
- agents/openai.yaml：支持平台的界面元数据，如该文件存在
- README.md：当前中文产品文档与版本记录

## 使用方式

1. 将整个 amazon-pdp-import-generator/ 目录交给支持 skill 的 AI 或复制到对应技能目录。
2. 让 AI 先读取 SKILL.md；README.md 用于人类理解产品能力和升级历史。
3. 按任务需要提供输入证据，执行后使用 eval/acceptance.md 验收。
4. 若修改能力、边界、输入输出或资源，应同步更新 README.md 的当前说明和版本记录。

## 验收标准

- 同一输入重复运行得到稳定分组
- 每张图片都能在解析日志中追溯
- 低置信度不会被当成已确认事实
- 生成内容只使用已验证商品信息
- Rank、趋势和关键词证据记录站点、查询、类目、来源与采集时间
- 生成前已经询问关键词库及是否优先参考，采用或排除给定词均有理由
- SEO 关键词布局自然、无堆砌，GEO 语义覆盖不制造事实
- 自检失败项已经修复或明确阻塞，未把草稿误称为可直接上传

## 版本与升级规则

- 当前能力以本 README 和 skill.json 的版本为准。
- 每次能力、工作流、资源、输入输出或边界发生实质变化，必须提升版本并补充下方记录。
- 仅修正文案错字或链接时可不提升版本，但仍应保证产品说明与实际文件一致。
- 历史记录只写已发生变化，不把计划中的能力写成已经交付。

## 版本记录

| 版本 | 日期 | 更新内容 |
|---|---|---|
| 2.0.3 | 2026-07-15 | 自动检测到 Skill 实质内容升级并同步版本。 |
| 2.1.0 | 2026-07-15 | 新增当前市场 Rank 与趋势调研、SEO/GEO 关键词策略、字段映射和上线前系统自检闭环。 |
| 2.0.2 | 2026-07-15 | 自动检测到 Skill 实质内容升级并同步版本。 |
| 2.0.1 | 2026-07-15 | 自动检测到 Skill 实质内容升级并同步版本。 |
| 2.0.0 | 2026-07-15 | 补齐标准触发入口、商品事实隔离、内容声明护栏、独立 parse_log.csv 与真实脚本测试。 |
| 1.0.0 | 未记录 | 实现按图片文件名生成 Amazon PDP CSV/XLSX 基础草稿。 |
