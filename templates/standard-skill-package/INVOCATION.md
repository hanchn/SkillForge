# Invocation

## Standard Invocation Flow

1. 先读 `skill.json`
2. 再读 `BASE_PROMPT.md`
3. 如果是特定平台，再读 `platforms/<platform>.md`
4. 调用 `scripts/` 中的主脚本或核心逻辑
5. 返回输出结果与边界说明
