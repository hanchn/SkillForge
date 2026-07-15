# 亚马逊PDP导入生成器

- 用途：项目内跨平台 skill，根据商品图片文件名自动整理商品信息，并生成亚马逊 PDP 导入草稿表
- 输入：单图或多图商品目录，图片命名支持可变段位，例如 `hat-001-red.jpg`、`hat-001-red-front.jpg`
- 输出：`amazon_pdp_import_draft.xlsx` 与 `amazon_pdp_import_draft.csv`
- 说明：这是 `SkillForge` 项目中的业务 skill 包，不是 Trae 私有 skill；README 只负责说明，真正执行逻辑在脚本与平台适配文件中

## Skill 定位

- 这是放在业务目录里的项目内 skill
- 目标是支持多平台复用，例如 `Claude`、`Codex`、`GPT`、`Trae`、`Qorder`
- skill 元数据见 `skill.json`
- 平台适配说明见 `platforms/`
- 执行脚本是 `generate_pdp_import.py`

## 适用场景

- 你把一个商品的单图或多图放进同一个目录
- 图片文件名包含基础识别信息，如品类、SKU、颜色、角度、顺序
- 你希望先自动出一份结构化导入表，再补品牌、卖点、描述、图片 URL

## 命名规则

- 文件名按 `-`、`_`、空格切分
- 支持可变段位，不要求固定 3 段
- 默认会识别末尾的图片角色或序号，如 `main`、`front`、`side`、`1`、`2`
- 示例：
  - `hat-001-red.jpg`
  - `hat-001-red-main.jpg`
  - `hat-001-red-side-2.jpg`
  - `cup_202_black_detail.png`

## 运行方式

```bash
python3 generate_pdp_import.py "/你的图片目录"
```

可选参数：

```bash
python3 generate_pdp_import.py "/你的图片目录" \
  --brand "Your Brand" \
  --marketplace "US" \
  --category "Apparel" \
  --variation-theme "Color"
```

## 输出字段

- `sku`
- `parent_sku`
- `product_type`
- `color_name`
- `item_name`
- `brand_name`
- `marketplace`
- `category`
- `variation_theme`
- `main_image_file`
- `other_image_files`
- `main_image_url`
- `other_image_urls`
- `bullet_point_1` ~ `bullet_point_5`
- `product_description`
- `parse_confidence`
- `source_files`

## 当前边界

- 当前基于文件名做结构化推断，无法仅靠图片文件名自动得到完整亚马逊文案
- 亚马逊正式 flat file 通常还需要类目模板、品牌、属性、合规字段、图片 URL
- 所以首版先生成“导入草稿表”，适合作为人工补全或后续自动化的中间层
