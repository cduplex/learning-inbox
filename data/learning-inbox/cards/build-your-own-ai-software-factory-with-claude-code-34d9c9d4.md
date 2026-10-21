# Build Your Own AI Software Factory with Claude Code

## Source
- Original: https://www.youtube.com/watch?v=ctoaIC4LHmI
- Type: youtube
- Creator: {'displayName': 'ZazenCodes'}
- Published: 2026-10-07T00:00:00.000Z

## Tags
agentic software factory, Claude Code, subagents, code review, human approval, Git worktrees, parallel development, markdown state, observability, CI/CD, software engineering, token cost

## Derived summary
The video presents a simple agentic software factory built with Claude Code inside an existing project. A feature request is routed through a spec-writing agent, a builder, separate security/UX/UI/code reviewers, iterative rework when needed, and an approval stage that either merges or sends work to human review. The implementation uses Claude skills and subagents, with markdown files as job/state metadata and a dashboard for observability. In the demo, a clean working tree is required before starting; an example feature was specified, built on a branch, reviewed, escalated for human approval, and merged after approval. The presenter then adds Git worktree support to run multiple features in parallel. They identify future extensions such as GitHub Issues or Slack intake, production-monitoring inputs, and post-deployment monitoring/rollback. The presenter also notes that multi-agent coordination can increase token costs due to context passing, despite perceived quality and observability benefits.

## Practical applications
- Suggestion: Adapt the demonstrated staged workflow for an existing repository: feature intake, specification, isolated implementation, specialized review, rework, and explicit merge approval.
- Suggestion: Use repository-local markdown metadata and a dashboard when simple, inspectable job state and observability are preferred.
- Suggestion: Add Git worktree-based isolation before attempting parallel feature execution, and account for merge coordination.
- Suggestion: Define project-specific escalation rules for sensitive areas such as billing, access control, cache invalidation, or other high-impact changes.
- Suggestion: Evaluate whether the additional quality and traceability of multiple agents justify the increased token/context cost for the project.
- Suggestion: Consider future intake from tracked issues, team messaging, or production monitoring only with suitable review gates and post-deployment safeguards.

## Evidence anchors
- [00:01:05.280] is what we're going to build. It's a
- [00:01:06.880] simple agentic software factory where a
- [00:01:09.439] team of agents take a feature and pull
- [00:01:12.000] that into the main codebase by the end
- [00:01:14.080] of our factory. So, we input some

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
