# 亚马逊PDP内容生成技能

- skill id：`amazon-pdp-import-generator`
- 展示名：`亚马逊PDP内容生成技能`
- 用途：根据商品图片文件名自动整理商品信息，并结合 AI 生成 SEO 优化的 PDP 内容（标题、5要素、描述、Search Terms 标签），最终输出亚马逊 PDP 导入草稿表
- 定位：这是 `SkillForge` 项目中的可单独分发 skill 包，不绑定单一平台

## 包结构

- `README.md`：说明文档
- `SKILL.md`：统一 skill 入口，优先给 AI 读取
- `skill.json`：机器可读元数据
- `INVOCATION.md`：标准调用协议
- `BASE_PROMPT.md`：跨平台基座提示词
- `platforms/`：平台适配层
- `scripts/`：真实执行逻辑
- `assets/`：配置与静态资产
- `examples/`：输入输出示例
- `eval/`：验收与评测规则

## 输入输出

- 输入：单图或多图商品目录，文件名支持可变段位，如 `hat-001-red.jpg`
- 输出：`amazon_pdp_import_draft.xlsx` 与 `amazon_pdp_import_draft.csv`
- 可选参数：`brand`、`marketplace`、`category`、`variation_theme`

## 单独分发

- 可以直接把整个 `amazon-pdp-import-generator/` 文件夹发给别人使用
- 不依赖 `.trae`
- 不依赖 `SkillForge` 根目录中的其他文件
- 对方只需阅读 `SKILL.md` 或 `INVOCATION.md`，然后运行 `scripts/generate_pdp_import.py`

## 适用场景

- 用图片命名快速整理商品主图、附图和基础属性
- 先得到结构化 PDP 草稿，再进行人工补文案或接类目模板
- 需要在 `Claude`、`Codex`、`GPT`、`Trae`、`Qorder` 间复用同一 skill

## 文件名规则

- 文件名按 `-`、`_`、空格切分
- 支持可变段位，不要求固定 3 段
- 默认识别末尾角色与序号，如 `main`、`front`、`side`、`1`、`2`

## 当前边界

- 当前输出是“PDP 导入草稿表”，不是最终类目 flat file
- 只靠文件名无法自动生成完整品牌文案、属性字段与合规字段
- 如果要正式导入亚马逊类目模板，还需要补图片 URL、类目映射与属性规则
