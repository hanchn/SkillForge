# Skills Dashboard

- 用途：可视化展示 `SkillForge` 中的所有 skill
- 形式：零依赖静态 HTML 页面
- 入口：`index.html`
- 详情：`detail.html?skill=<skill-id>`
- 文档查看：项目索引、技能索引和 skill 文档默认页内展示
- 下载：只有详情页中的 ZIP 是下载动作

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
- 各 skill 包中的 `distribution.package_files`
