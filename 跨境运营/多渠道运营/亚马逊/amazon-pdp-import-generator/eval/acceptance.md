# Acceptance

## Minimum Acceptance

- 能读取一个图片目录并识别图片文件
- 能按文件名归并同一商品
- 能识别主图与附图
- 能输出 `amazon_pdp_import_draft.xlsx`
- 能输出 `amazon_pdp_import_draft.csv`
- 目录无图片时能明确报错

## Evaluation Cases

- 单图商品：`hat-001-red.jpg`
- 多图商品：`hat-001-red-front.jpg` + `hat-001-red-side-2.jpg`
- 下划线命名：`cup_202_black_detail.png`
- 不带颜色词：检查 `parse_confidence`

## Manual Review

- 核对 `sku`、`parent_sku`、`color_name`
- 核对 `main_image_file` 与 `other_image_files`
- 核对输出文件可被 Excel 正常打开
