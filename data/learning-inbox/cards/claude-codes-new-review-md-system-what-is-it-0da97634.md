# Claude Codes New REVIEW.md System, What is it?

## Source
- Original: https://www.youtube.com/watch?v=bls8ZJ_INMQ
- Type: youtube
- Creator: {'displayName': 'Rob Shocks'}
- Published: 2026-10-19T00:00:00.000Z

## Tags
AI-assisted software engineering, code review, agent workflows, CI/CD, risk-based approvals, feature flags, rollback, merge queues, software delivery, Anthropic, Claude Code

## Derived summary
## [00:00:00] Reported acceleration and the review bottleneck

- [00:00:00] The presenter says Claude Code now writes about **90% of its own code**, and characterizes the web app's rate of change as very fast.
- [00:00:11] He reports that merged pull requests more than doubled between June and September, while code that was reverted or had gone wrong fell by **40%**. These reported figures are not independently verified in the source.
- [00:00:23] The video aims to reconstruct Anthropic's process from several sources, distinguish marketing claims from practical practices, and extract lessons for developers.
- [00:00:40] The presenter frames the constraint in agent-heavy engineering as review rather than code generation: organizations can run many agents, but then must review and validate a large incoming volume of code.
- [00:00:55] A quoted Claude Code team principle is that review was not removed; rather, most reading was moved to machines while the process was optimized for human time and attention, fast reversibility, limited blast radius, and recovery.
- [00:01:42] Caveat: Anthropic has substantial inference capacity and sells inference and a broader vision, so its workflow may not map directly to every team. The presenter nevertheless considers it directionally useful.
- [00:02:05] The presenter reports that Anthropic monorepo changes landing per day rose from roughly **2,500 in May** to more than **30,000 in September**. At that throughput, manual line-by-line review is described as extremely difficult or impossible.

## [00:02:28] Reframing the purpose and timing of review

- [00:02:28] The source defines two historical purposes of code review: catch problems before shipping, and distribute knowledge of the codebase and colleagues' working practices across the team.
- [00:02:46] Instead of asking whether a human reviewed a change, the proposed first-principles question is what could go wrong with the submitted code and which check, automated or human, is appropriate to catch it.
- [00:03:11] The presenter interprets this not as replacing developers, but as moving developers to a different, potentially higher-value point in the process. This is his interpretation rather than a verified outcome.
- [00:03:22] Review shifts from a single pre-merge event to continuous checking from the first prompt through merge, compared to spell-check operating while someone writes.
- [00:03:40] The stated goal for Claude Code repositories is for most PRs to merge with at most one human in the loop, where that human may be the author.
- [00:03:54] The process tracks human approvals per PR, PR comments, and time a PR waits for a person. The presenter suggests these may supplement or replace traditional DORA metrics.
- [00:04:11] Reversion and incident rates are the guardrails: if they rise, human work may merely have shifted downstream into customer-facing breakage or later fixes rather than being saved.

## [00:04:40] Six-layer checking model and rollback foundation

- [00:04:40] The system is summarized as **six layers of checks** supported by rollbacks. The intended model is to permit agents to operate within constraints while containing failures before they affect customers.
- [00:05:06] **Layer 1, verification before human review:** automated checks include browser tests and related verification, meaning much review occurs before a PR exists.
- [00:05:15] Claude is described as running tests, building, taking screenshots, and performing end-to-end tests. Rather than asserting completion, it is expected to show evidence of completion.
- [00:05:26] A subagent then reviews the diff with a fresh context window. The presenter attributes an estimate to Claude Code creator Boris Cherny that verification makes final results **two to three times better**; this estimate is not independently verified.
- [00:05:44] Recurring findings are addressed at their source through short project-instruction files such as `CLAUDE.md` or `AGENTS.md`, which describe stack, conventions, and goals, plus owner-authored `review.md` files describing what reviewers should prioritize.
- [00:05:59] The presenter warns that AI review can create excessive nitpicks and false positives. A cap is useful because low-value findings can overwhelm reviewers and may concern pre-existing code merely included in a PR rather than the actual change.

## [00:06:26] Automated PR review, security gates, and baseline checks

- [00:06:26] **Layer 2, AI review before a person looks:** the reviewer examines the diff against the full repository and the PR's stated intent.
- [00:06:37] Several agents search for bugs in parallel; a separate group votes on findings; the reviewer posts a finding only when enough agents agree it is real.
- [00:06:53] **Layer 3, separate security review:** on Anthropic's repositories, a PR cannot merge while any bug-review or security-review finding remains open. This is a hard gate.
- [00:07:06] **Layer 4, conventional merge blockers:** linting, type checks, testing on every platform, and build tests continue to block merge.
- [00:07:16] The PR template asks authors both how they tested a change and how it can be undone, making verification and reversibility explicit review inputs.

## [00:07:20] Sponsor aside: agent tool-call policy product

- [00:07:20] **Sponsor aside:** the presenter describes OpenRouter Armor, a beta product said to sit before agent tool calls, evaluate calls against policy using a Typesafe model, and block out-of-bounds calls.
- [00:08:05] OpenRouter claims Armor outperforms Claude Code's autoclassifier at a fraction of the cost and improves safety without slowing agents. These are sponsor/product claims, not independently verified in the source.

## [00:08:19] Human approval scaled by risk

- [00:08:19] **Layer 5, risk-scaled human approval:** low-risk documentation, copy, or additive feature-flagged changes need no human approval once automated and security checks pass; ordinary product work needs one person; high-risk code needs two.
- [00:08:41] The rationale is blast radius: changes likely to make a larger mess if wrong should receive more human checking.
- [00:08:56] **Rule 1:** the change itself, not the author, determines its tier. One classifier selects the tier, and another checks whether human involvement is still required. CI workflow-file changes always require a person.
- [00:09:12] **Rule 2:** only trusted authors, mostly from the owning team, receive lighter approval paths.
- [00:09:17] **Rule 3:** an agent's approval never substitutes for a person's approval. Automated review can clear a low-risk change but cannot occupy a required human slot.
- [00:09:32] **Rule 4:** the person who prompted an agent-written change remains accountable and counts as reviewer. The presenter emphasizes that orchestration responsibility remains human even when many agents are used.
- [00:10:02] **Rule 5:** approval covers one specific commit. If an agent pushes a new commit, the change requires approval again.

## [00:10:09] Merge queue, staged release, and recovery operations

- [00:10:09] **Layer 6, merge queue:** all checks are rerun against the main branch with the changes applied, preventing individually passing PRs from combining into a main-branch-breaking state.
- [00:10:29] New behavior ships behind a flag, first to Anthropic's internal team, then to a wider "latest" channel that may include **about 1,000 or more** people and customers, and finally to the stable channel if earlier stages are successful.
- [00:10:51] The backbone is fast failure detection and fast rollback. Feature flags can disable behavior without a deployment, there is a weekly on-call rotation, and incident reviews ask which layer should have caught the issue.
- [00:11:14] The source acknowledges a gap: it lacks a "circuit breaker" that would tighten or halt the system when agent-generated work begins to be reverted frequently.
- [00:11:31] The presenter compares the desired circuit-breaker behavior to stopping or slowing a bottling line when a defect appears early, rather than allowing it to contaminate a large downstream batch.
- [00:11:46] Anthropic's stated preference is to detect and fix problems faster rather than slow down broadly, because slowing down lowers error rate mainly by doing less overall.

## [00:11:57] Failure mode: overnight AI-review loops

- [00:11:57] One Claude Code CLI PR reportedly underwent more than **50 rounds** of AI review and fixes overnight before its author stopped it. This reported case is not independently verified.
- [00:12:11] Using `git blame` to investigate the repeated findings, the team reportedly found that about **59%** were code present since the first pass, rather than newly introduced issues.
- [00:12:32] The failure mode is a proactive review system repeatedly discovering old or related issues, producing a loop of finding, commit, review, and another round.
- [00:12:44] A human can dismiss a nitpick or preference quickly, whereas an agent may attempt a fix, cause another commit, and trigger another review cycle. The presenter calls this a central trap of agent workflows.
- [00:13:00] The presenter characterizes software factories as moving, evolving systems that developers must design, build, and learn to operate, rather than static automation.

## [00:13:20] Loop controls and reviewer evaluation

- [00:13:20] The reported remediation added caps on review rounds. After **three rounds**, the reviewer asks the author to step back and reconsider the overall approach.
- [00:13:30] In later passes, the reviewer examines only the exact new diff, flags an entire bug class rather than one line, and avoids repeating the same finding.
- [00:13:46] The team turns past incidents into agent evaluations: it collects PRs that caused incidents, has knowledgeable engineers validate the set, then runs the reviewer against it daily to assess whether it is improving or worsening.

## [00:14:05] Claude Code Review product positioning and claimed performance

- [00:14:05] The presenter says Claude Code Review is the public version of Layer 2, AI review on every PR, and had become generally available at the enterprise level.
- [00:14:16] Its described workflow is parallel agent inspection of the diff, a verification step to filter false positives, severity ranking, inline comments, and a check run.
- [00:14:32] Anthropic claims most reviews are about **three times faster**, falling from roughly **20 minutes** to roughly **6 or 10 minutes**. This product-performance claim is not independently verified.
- [00:14:40] Repositories can choose quick, standard, or deep review modes; deeper review costs more.
- [00:14:46] The product does not approve or block a PR, consistent with the internal rule that agent approval never counts as human approval.
- [00:14:55] Local review in Claude Code, Cursor, or similar tools is described as a lighter pre-PR pass, while security review covers the separate security layer.

## [00:15:15] Seon replacement for Git and practical recap

- [00:15:15] Anthropic reportedly replaced Git for its monorepo with an in-house system called **Seon** and a review tool called **Antique**.
- [00:15:29] The stated scaling issue was a main branch with almost **100 GB** of history and CI checking it out **25 million times per day**.
- [00:15:39] A seven-person team reportedly completed the migration in about **five months**. The presenter says no outside party had tested the system to his knowledge, while Anthropic reports a **200-times smaller** footprint than its prior Git mirroring. These are unverified reported claims.
- [00:15:56] **Recap:** the presenter recommends giving agents executable checks, adding a `review.md`, deploying and tuning an AI reviewer on one repository for a couple of weeks, and classifying risk by the change's blast radius rather than by author identity.
- [00:16:15] **Recap:** never allow an agent's approval to replace a human's, and monitor reverts and failures as outcome signals.
- [00:16:23] Whether a fully green low-risk PR should merge without human approval is presented as context-dependent, particularly on the codebase and possible blast radius.

## Practical applications
- Suggestion: Define review goals in terms of failure modes to catch, then assign each failure mode to automated verification, AI review, security review, or human approval.
- Suggestion: Add a concise repository-level `review.md` that identifies critical invariants, code-owner concerns, and high-value review priorities, while capping low-value nitpicks.
- Suggestion: Pilot AI PR review on one low-risk repository and track human approval count, reviewer wait time, reverts, incidents, and repeated false positives before expanding use.
- Suggestion: Create change-based risk tiers, with stricter human approval for high-blast-radius changes and mandatory human review for CI workflow modifications.
- Suggestion: Require each PR to document how it was tested and how it can be rolled back, then use feature flags and staged channels where the deployment model supports them.
- Suggestion: Prevent review loops by setting a maximum number of automated review rounds, reviewing only newly introduced diffs on later rounds, and deduplicating previously reported findings.
- Suggestion: Build a regression evaluation set from confirmed incident-causing PRs and periodically test reviewer behavior against that set.
- Suggestion: Establish a circuit-breaker policy, such as escalating to human review or pausing an agent workflow when reversion or incident signals exceed a defined threshold.

## Evidence anchors
- [00:00:00.080] So claw code now writes about 90% of its
- [00:00:11.679] working. Between June and September
- [00:00:20.720] wrong dropped by 40%. So what the heck
- [00:00:40.320] So, anyone who's been working with
- [00:00:55.600] claw code team just published how they

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
