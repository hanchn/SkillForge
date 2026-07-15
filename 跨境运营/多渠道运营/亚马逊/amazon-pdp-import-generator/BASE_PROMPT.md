# Amazon PDP Import Generator Base Prompt

你正在调用 `amazon-pdp-import-generator` 这个可单独分发的跨平台 business skill。

## Skill 目标

- 根据商品图片文件名自动生成亚马逊 PDP 导入草稿
- 输出 `amazon_pdp_import_draft.xlsx` 与 `amazon_pdp_import_draft.csv`
- 输入通常是一个包含单图或多图商品图片的目录

## 目录职责

- `README.md`：说明文档
- `SKILL.md`：统一入口
- `skill.json`：元数据
- `INVOCATION.md`：调用协议
- `scripts/generate_pdp_import.py`：执行脚本
- `assets/parser_config.json`：解析配置

## 必须遵守

- `README.md` 只是说明文件，不是 skill 本体，不是执行入口
- 这是一个可独立分享的 skill 文件夹，优先在当前目录内完成所有工作
- 优先复用现有脚本，不要重新编写另一套生成器
- 用户未提供图片目录时，必须先索要路径或让用户确认路径
- 如果目录中没有图片文件，必须明确告知，不能伪造导出结果

## 标准执行步骤

1. 先读取 `SKILL.md` 与 `INVOCATION.md`
2. 确认图片目录路径
3. 检查目录中是否存在图片文件
4. 读取用户是否提供品牌、站点、类目、变体主题
5. 调用：

```bash
python3 "scripts/generate_pdp_import.py 的绝对路径" "图片目录绝对路径"
```

6. 如有可选参数，再附加：

```bash
--brand
--marketplace
--category
--variation-theme
```

7. 核心 AI 增强动作：脚本执行完毕后，作为 AI，你必须读取生成的 CSV 草稿文件，并利用你的 LLM 能力为每个 SKU 自动生成以下亚马逊 SEO 优化的文案内容：
   - 优化后的商品标题（item_name）
   - 5个高转化卖点（bullet_point_1 到 bullet_point_5）
   - 结构化的商品描述（product_description）
   - 搜索关键词/标签（search_terms）
8. 将生成的 AI 增强内容回填至 CSV/Excel 文件中，或者在对话框中以 Markdown 表格/列表的形式直观地展示给用户确认。
9. 返回生成文件路径与识别商品数。

## 文件名解析规则

- 文件名按 `-`、`_`、空格切分
- 支持可变段位
- 识别结尾角色词，例如 `main`、`front`、`side`、`back`、`detail`
- 识别结尾顺序号，例如 `1`、`2`

## 输出边界

- 当前是“PDP 导入草稿表”
- 不是某个正式类目 flat file 的最终版
- 如果用户要正式 flat file，需要补类目模板、属性字段、合规字段与图片 URL
