# Git Safety Checks

## Commit message gate

- Trim whitespace and comments, then reject an empty result.
- Reject fewer than 5 meaningful characters; issue IDs, punctuation, emoji or whitespace alone do not count as detail.
- Require the message to communicate what changed, why, and how it was verified. Use a subject plus body when one line is insufficient.
- Do not bypass the gate with `--no-verify`; installing or changing hooks requires explicit authority.

## Terminal failure and conflict visibility

- Preserve relevant stderr and identify the failed step; redact only secrets.
- After failure, use safe read-only checks to report branch, operation state, conflicts, worktree status and upstream divergence; exit non-zero.
- For every conflict list path, status code, base/ours/theirs and relevant commits, then label `EXPECTED` or `ABNORMAL` with a reason.
- Scope-external, unrelated-user-change, protected-branch, unexpected delete/rename, migration, permission, security, dependency-lock, generated, binary or ambiguous conflicts are abnormal and require review.
- Separate proven cause from hypothesis. Never resolve an abnormal conflict by automatically choosing ours or theirs.

## Test contamination audit

- Require explicit test ref, non-test target and approved development source refs; missing refs produce `WARNING/REVIEW_REQUIRED`, never `PASS`.
- Block when the test tip, a test-only commit or a merge parent unique to test is reachable from the non-test target.
- Compare patch identity when history may have been cherry-picked or squashed; same content with a different commit ID still counts as contamination unless it is traceable to an approved source.
- Inspect changed paths and content for environment-only material such as `.env.test`, test deployment manifests, test endpoints, credentials, buckets, queues or feature overrides. Never print secret values.
- Commits shared by test and an approved development source are not test-only. Preserve the compared refs, merge bases and command evidence to prevent false accusations.

Before mutation verify: repository root; instructions; current branch; status; untracked files; staged diff; unstaged diff; remotes; upstream; ahead/behind; worktrees; target ref; commit range; protected-branch policy; relevant tests; recovery ref.

Classify an operation as low risk when it adds recoverable local state, medium risk when it changes shared integration state, and high risk when it discards work, rewrites published history, changes production refs, or combines ambiguous conflicts. High-risk operations require explicit authority.

## 贵司分支门禁

- 进入流程时记录当前开发分支为 `return_branch`；当前分支若为 `master`、`main`、`test` 或 `pre`，禁止开始编码或直接提交，应先切换或创建独立开发分支。
- `test` 只承载测试环境集成，不得合并到 `pre`、`master`、`main`、开发分支或其他任何非 `test` 分支。
- 合并前验证 source、target 和 commit set，禁止仅凭分支名猜测发布链路。
- 合并、验证或发布动作完成后返回 `return_branch`，再报告最终状态。
- 如果存在未解决冲突、未保存工作或 worktree 占用，暂停自动返回并报告阻塞；禁止 reset、clean 或丢弃改动来强行切换。
