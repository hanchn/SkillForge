# Amazon PDP Import Generator Base Prompt

你正在调用 `amazon-pdp-import-generator` 这个项目内 skill。

## Skill 目标

- 根据商品图片文件名自动生成亚马逊 PDP 导入草稿
- 输出 `amazon_pdp_import_draft.xlsx` 与 `amazon_pdp_import_draft.csv`
- 输入通常是一个包含单图或多图商品图片的目录

## 真实实现位置

- 说明文件：`README.md`
- 执行脚本：`generate_pdp_import.py`
- 解析配置：`parser_config.json`

## 必须遵守

- `README.md` 只是说明文件，不是 skill 本体，不是执行入口
- 这是 `SkillForge` 项目内 skill，不能把它当成 Trae 私有 skill 放进 `.trae`
- 优先复用现有脚本，不要重新编写另一套生成器
- 用户未提供图片目录时，必须先索要路径或让用户确认路径
- 如果目录中没有图片文件，必须明确告知，不能伪造导出结果

## 标准执行步骤

1. 确认图片目录路径
2. 检查目录中是否存在图片文件
3. 读取用户是否提供品牌、站点、类目、变体主题
4. 调用：

```bash
python3 "generate_pdp_import.py 的绝对路径" "图片目录绝对路径"
```

5. 如有可选参数，再附加：

```bash
--brand
--marketplace
--category
--variation-theme
```

6. 返回生成文件路径
7. 必要时说明哪些字段仍需人工补全

## 文件名解析规则

- 文件名按 `-`、`_`、空格切分
- 支持可变段位
- 识别结尾角色词，例如 `main`、`front`、`side`、`back`、`detail`
- 识别结尾顺序号，例如 `1`、`2`

## 输出边界

- 当前是“PDP 导入草稿表”
- 不是某个正式类目 flat file 的最终版
- 如果用户要正式 flat file，需要补类目模板、属性字段、合规字段与图片 URL
