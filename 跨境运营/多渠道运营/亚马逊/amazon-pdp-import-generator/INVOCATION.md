# Invocation

## Standard Invocation Flow

1. 读取 `skill.json` 确认输入、输出、平台支持与入口文件
2. 读取 `BASE_PROMPT.md` 获取通用行为约束
3. 如果是特定平台，再读取 `platforms/<platform>.md`
4. 确认用户提供的图片目录路径
5. 调用脚本生成导入草稿
6. 返回输出文件路径，并说明是否仍需补充品牌或类目字段

## Command

```bash
python3 scripts/generate_pdp_import.py "/absolute/path/to/image-folder"
```

## Optional Arguments

```bash
python3 scripts/generate_pdp_import.py "/absolute/path/to/image-folder" \
  --brand "Your Brand" \
  --marketplace "US" \
  --category "Apparel" \
  --variation-theme "Color"
```

## Failure Rules

- 未提供目录路径时，先索要路径
- 目录无图片时，直接报错，不伪造结果
- 不要跳过脚本直接手写导入表
- 不要把 `README.md` 当成执行入口
