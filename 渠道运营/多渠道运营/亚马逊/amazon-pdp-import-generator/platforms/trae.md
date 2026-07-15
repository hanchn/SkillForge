# Trae Adapter

- 先读取 `SKILL.md`、`INVOCATION.md`、`BASE_PROMPT.md`
- 不要把这个业务 skill 放进 `.trae/skills/`
- 只有“生成 skill 的 skill”才属于 Trae 自身 skill
- 当前 skill 必须留在业务目录中复用
- 执行时调用 `scripts/generate_pdp_import.py`
