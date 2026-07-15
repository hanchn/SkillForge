# Invocation

## Standard Invocation Flow

1. 读取 `skill.json` 确认输入、输出
2. 读取 `BASE_PROMPT.md` 获取通用行为约束
3. 收集用户提供的上下文与需求
4. 执行核心优化/生成逻辑
5. 返回结果

## Failure Rules

- 需求不明确时，先索要必要背景
- 不要脱离实际业务场景凭空编造
