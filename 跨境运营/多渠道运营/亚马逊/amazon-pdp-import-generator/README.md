# 亚马逊 PDP 导入草稿生成器

把图片目录变成可审计的 Amazon 商品导入草稿，并严格隔离解析推断与真实商品事实。

## 典型任务

- 解析商品图片目录并检查低置信度 SKU。
- 生成颜色变体草稿并核对主图与附图。
- 基于提供的规格事实生成美国站标题、五点和 Search Terms。

## 交付物

- amazon_pdp_import_draft.xlsx
- amazon_pdp_import_draft.csv
- parse_log.csv
- review_summary.md

## 硬边界

- 不得从文件名或图片推断未经验证的商品声明
- 不得把通用草稿称为已适配 Seller Central 的可上传模板
- 目录为空或解析冲突时不得伪造结果

## 读取顺序

1. SKILL.md
2. SKILL.md 指定的 references 与 assets
3. INVOCATION.md
4. eval/acceptance.md

整个目录可以独立分发；README 只承担人类说明，不是 skill 执行入口。
