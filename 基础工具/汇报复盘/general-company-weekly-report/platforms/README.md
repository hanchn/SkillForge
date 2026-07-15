# 平台适配

该 Skill 以 Markdown 和 JSON 作为可移植契约。在支持文件读取的平台加载整个目录；在只支持提示词的平台至少加载 `SKILL.md`、reference 与 asset。涉及仓库、数据源或外部系统时，按平台权限先读后写并保留验证证据。
