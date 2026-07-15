# Examples

## Sample File Names

- `hat-001-red.jpg`
- `hat-001-red-front.jpg`
- `hat-001-red-side-2.jpg`
- `cup_202_black_detail.png`

## Example Usage

```bash
python3 scripts/generate_pdp_import.py "/data/products" --brand "DemoBrand" --category "Apparel"
```

## Expected Outputs

- `amazon_pdp_import_draft.xlsx`
- `amazon_pdp_import_draft.csv`
- 解析日志在 Excel 的 `Parse_Log` sheet 中
