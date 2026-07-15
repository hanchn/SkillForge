# SkillForge Project Index

这个文件给 AI 提供全局导航、分类定位和技能检索入口。

## First Read

- 项目总说明：README.md
- 项目治理：skillforge-project-governance/SKILL.md
- 全局注册表：registry/skills-index.json
- 元数据规范：schemas/skill.schema.json
- 标准模板：templates/standard-skill-package/
- 可视化管理：skills-dashboard/

## Search Strategy

1. 新建、升级或打包 skill 前先读项目治理 skill。
2. 从 registry/skills-index.json 按 name、category_path 或 search_keywords 定位。
3. 进入技能包后先读 SKILL.md，再按指示加载 references 与 assets。
4. 执行后使用 eval/acceptance.md 验收；声明脚本的技能还必须运行脚本测试。

## Registered Skills

- skillforge-project-governance（SkillForge项目治理）\n  - 路径：skillforge-project-governance/\n  - 分类：project-root\n  - 用途：治理 SkillForge 的分类、技能包质量、索引和分发规则\n- amazon-pdp-import-generator（亚马逊 PDP 导入草稿生成器）\n  - 路径：跨境运营/多渠道运营/亚马逊/amazon-pdp-import-generator/\n  - 分类：跨境运营 / 多渠道运营 / 亚马逊\n  - 用途：从商品图片文件名生成可审计的 Amazon SKU、变体、图片和内容草稿\n- seo-optimizer（SEO 内容优化师）\n  - 路径：跨境运营/推广营销/seo-optimizer/\n  - 分类：跨境运营 / 推广营销 / SEO\n  - 用途：基于业务事实、搜索意图、SERP 和技术前提规划、撰写与审计 SEO 内容\n- geo-optimizer（GEO 引用就绪优化师）\n  - 路径：跨境运营/推广营销/geo-optimizer/\n  - 分类：跨境运营 / 推广营销 / GEO\n  - 用途：通过实体一致性、声明溯源和答案模块提升生成式引擎准确理解与引用的可能性\n- ecommerce-product-research（跨境电商选品研究）\n  - 路径：跨境运营/选品/ecommerce-product-research/\n  - 分类：跨境运营 / 选品 / 跨渠道机会研究\n  - 用途：从需求、竞争、利润、供应链、合规和渠道适配评估跨境产品机会\n- shopify-conversion-auditor（Shopify 转化审计师）\n  - 路径：跨境运营/多渠道运营/独立站/shopify-conversion-auditor/\n  - 分类：跨境运营 / 多渠道运营 / 独立站 / CRO\n  - 用途：基于页面、数据和商品事实审计 Shopify 转化障碍并排序改进项\n- git-workflow-manager（Git 安全工作流管理器）\n  - 路径：互联网研发/git/git-workflow-manager/\n  - 分类：互联网研发 / git / 安全工作流\n  - 用途：基于真实仓库状态安全规划或执行 Git 分支、集成、发布和恢复\n- product-requirements-architect（产品需求架构师）\n  - 路径：互联网研发/产品/B端产品/product-requirements-architect/\n  - 分类：互联网研发 / 产品 / B端产品\n  - 用途：把模糊产品想法转成可评审、可开发、可测试、可度量的需求包\n- api-contract-designer（API 契约设计师）\n  - 路径：互联网研发/后端/api-contract-designer/\n  - 分类：互联网研发 / 后端 / API设计\n  - 用途：设计一致、可演进、可测试并能直接评审的 HTTP 或事件 API 契约\n- test-strategy-designer（测试策略设计师）\n  - 路径：互联网研发/测试/test-strategy-designer/\n  - 分类：互联网研发 / 测试 / 测试策略\n  - 用途：根据变更影响和风险设计分层覆盖、发布门槛与生产验证方案\n- metric-diagnostics（业务指标诊断师）\n  - 路径：数据/metric-diagnostics/\n  - 分类：数据 / 业务分析 / 指标诊断\n  - 用途：验证指标口径与数据质量，量化拆解异常变化并区分驱动因素和假设\n- contract-risk-reviewer（合同风险审阅师）\n  - 路径：法律政务/contract-risk-reviewer/\n  - 分类：法律政务 / 合同 / 商业合同审阅\n  - 用途：逐条提取合同义务、识别风险和缺失保护，并形成可谈判的优先清单\n
## Architecture Notes

- 中文目录负责业务浏览，稳定英文目录负责 skill id。
- 每个业务 skill 优先按整个文件夹独立分发。
- README 只给人说明；SKILL.md 才是 AI 入口。
- 业务核心保持跨平台；agents 与 platforms 只适配界面或工具差异。
- 新增或升级 skill 必须同步两个 registry 文件与本索引。
