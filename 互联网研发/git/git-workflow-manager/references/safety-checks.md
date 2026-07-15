# Git Safety Checks

Before mutation verify: repository root; instructions; current branch; status; untracked files; staged diff; unstaged diff; remotes; upstream; ahead/behind; worktrees; target ref; commit range; protected-branch policy; relevant tests; recovery ref.

Classify an operation as low risk when it adds recoverable local state, medium risk when it changes shared integration state, and high risk when it discards work, rewrites published history, changes production refs, or combines ambiguous conflicts. High-risk operations require explicit authority.
