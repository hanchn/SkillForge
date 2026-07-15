# Git Safety Checks

Before mutation verify: repository root; instructions; current branch; status; untracked files; staged diff; unstaged diff; remotes; upstream; ahead/behind; worktrees; target ref; commit range; protected-branch policy; relevant tests; recovery ref.

Classify an operation as low risk when it adds recoverable local state, medium risk when it changes shared integration state, and high risk when it discards work, rewrites published history, changes production refs, or combines ambiguous conflicts. High-risk operations require explicit authority.

## 贵司分支门禁

- 进入流程时记录当前开发分支为 `return_branch`；当前分支若为 `master`、`main`、`test` 或 `pre`，禁止开始编码或直接提交，应先切换或创建独立开发分支。
- `test` 只承载测试环境集成，不得合并到 `pre`、`master`、`main`、开发分支或其他任何非 `test` 分支。
- 合并前验证 source、target 和 commit set，禁止仅凭分支名猜测发布链路。
- 合并、验证或发布动作完成后返回 `return_branch`，再报告最终状态。
- 如果存在未解决冲突、未保存工作或 worktree 占用，暂停自动返回并报告阻塞；禁止 reset、clean 或丢弃改动来强行切换。
