# SkillForge Project Governance Base Prompt

你正在处理 `SkillForge` 项目本身，而不是某一个单独业务 skill。

## 目标

- 先理解项目定位与架构设计
- 再判断当前需求应该落在哪一层
- 保证所有业务 skill 继续沿统一标准演进

## 必须遵守

- 这是一个跨平台业务 skill 蒸馏仓库
- 业务 skill 必须放业务目录，不放 `.trae`
- 只有“生成 skill 的 skill”才属于工具平台自身
- `README.md` 维护中文产品说明和版本记录，但不承担 skill 本体
- 每个业务 skill 必须尽量做到整包可单独分发
- 项目级规则与架构说明应集中在项目级 skill 中持续升级

## 决策顺序

1. 先判断需求是“项目级”还是“业务级”
2. 如果是项目级，优先更新 `skillforge-project-governance/`
3. 如果是业务级，优先复用标准 skill 包模板
4. 修改后同步考虑是否需要更新全局索引、schema 或模板
