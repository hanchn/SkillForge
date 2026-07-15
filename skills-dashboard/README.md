# Skills Dashboard

- 用途：可视化展示 `SkillForge` 中的所有 skill
- 形式：零依赖静态 HTML 页面
- 入口：`index.html`
- 详情：`detail.html?skill=<skill-id>`
- 文档查看：项目索引、技能索引和 skill 文档默认页内展示
- 下载：只有详情页中的 ZIP 是下载动作
- 排序：下载计数作为内部默认排序信号，不在前端明文展示
- 类型标签：产研主角色分为架构师与资深专家，业务主角色统一为资深经理；另有周报、专项能力和项目治理，卡片与详情页同步展示
- 版本标签：卡片和详情页展示来自 `skill.json.version` 的 SemVer；内容变化由版本同步脚本自动升级

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
- `registry/download-stats.json`：服务端、发布平台或人工汇总的全局下载计数
- `registry/skill-versions.json`：Skill 内容指纹、当前版本和更新时间账本

## 下载计数机制

- 全局基线由 `registry/download-stats.json` 提供，重建索引时写入每个 Skill 的 `download_count`。
- 静态页面无法直接修改仓库文件，因此浏览器内的新下载以 `localStorage` 增量记录，并即时参与显示和排序。
- 生产环境应由下载 API、对象存储日志或分析平台汇总真实事件，再回写全局基线。
- 可用 `python3 work/update_download_counts.py <skill-id> --increment 1` 或 `--set <数量>` 安全维护计数，随后运行索引重建脚本。
