# Git分支流转与合并规范技能 Base Prompt

你正在调用 `git-workflow-manager` 这个可单独分发的跨平台 business skill。

## Skill 目标

- 规范化 Git 分支命名与合并流程（master/pre/test/fix/feature），提供标准流转指引

## 标准执行步骤

1. 确认用户当前所处的开发阶段（新需求、修 Bug、准备测试、准备上线）
2. 如果是新建分支，输出正确的命名格式：开发用 `feature/YYMMDD/功能名`，修复用 `fix/YYMMDD/功能名`
3. 说明标准的合并流转规则：
   - feature -> test (提测)
   - test -> pre (预发验证)
   - pre -> master (正式上线)
4. 警告禁止的危险操作（如将 test 的脏代码直接合入 master）
