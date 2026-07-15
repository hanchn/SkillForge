# Amazon PDP Import Generator

## Identity

- skill id: `amazon-pdp-import-generator`
- display name: `亚马逊PDP导入生成器`
- type: `portable-business-skill`
- scope: `cross-platform`

## What It Does

- 根据商品图片文件名自动解析商品基础信息
- 自动归并同一商品的单图或多图
- 生成亚马逊 PDP 导入草稿：
  - `amazon_pdp_import_draft.xlsx`
  - `amazon_pdp_import_draft.csv`

## When To Use

- 用户给出一个商品图片目录，希望自动生成亚马逊 PDP 导入表
- 图片文件名类似 `hat-001-red`、`hat-001-red-front`、`cup_202_black_detail`
- 需要在 `Claude`、`Codex`、`GPT`、`Trae`、`Qorder` 中复用同一 skill

## Read In Order

1. `skill.json`
2. `INVOCATION.md`
3. `BASE_PROMPT.md`
4. `platforms/<platform>.md`
5. `scripts/generate_pdp_import.py`

## Package Guarantee

- 这是一个可独立分享的 skill 文件夹
- 直接发送整个 `amazon-pdp-import-generator/` 目录即可复用
- `README.md` 只是说明文档，不是 skill 本体

## Entrypoint

```bash
python3 scripts/generate_pdp_import.py "/path/to/image-folder"
```
