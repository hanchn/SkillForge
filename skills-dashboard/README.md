# Skills Dashboard

- 用途：可视化展示 `SkillForge` 中的所有 skill
- 形式：零依赖静态 HTML 页面
- 入口：`index.html`

## 使用方式

- 建议在项目根目录启动本地 HTTP 服务后访问

```bash
python3 -m http.server 4173
```

- 然后打开：

```text
http://localhost:4173/skills-dashboard/
```

## 数据来源

- `registry/project-index.json`
- `registry/skills-index.json`
- 各 skill 包中的 `skill.json`
