# work

- 用途：work 分类资料目录
- 公共：存放该维度下的通用资料
- `build_expanded_skill_families.py`：生成标准化 Skill 家族。
- `sync_skill_versions.py`：按内容指纹自动维护每个 Skill 的 SemVer，并同步中文 README。
- `sync_skill_compliance.py`：为每个 Skill 生成按业务分类适配、可随整包分发的合规基线并注入执行门禁。
- `rebuild_skillforge_indexes.py`：先同步合规基线与版本，再重建全局索引和项目导航。
