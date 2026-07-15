# Codex Adapter

- 先读取 `SKILL.md`、`INVOCATION.md`、`BASE_PROMPT.md`
- 把 skill 当作可单独分发的项目能力包
- 优先调用已有脚本，不要再生成另一份解析脚本
- 如果用户给的是目录，直接面向目录执行
- 输出里包含生成文件绝对路径
