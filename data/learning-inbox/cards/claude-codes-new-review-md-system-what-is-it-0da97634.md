# Claude Codes New REVIEW.md System, What is it?

## Source
- Original: https://www.youtube.com/watch?v=bls8ZJ_INMQ
- Type: youtube
- Creator: {'displayName': 'Rob Shocks'}
- Published: 2026-10-19T00:00:00.000Z

## Tags
AI-assisted software engineering, code review, agent workflows, CI/CD, risk-based approvals, feature flags, rollback, merge queues, software delivery, Anthropic, Claude Code

## Learning guide
**The arc**
When agents write most of the code, the bottleneck shifts from generating code to reviewing it: Anthropic reports changes landing per day rising from about 2,500 in May to over 30,000 in September, which makes line-by-line human review impossible. The central idea is that review is not removed but moved: machines do most of the reading, and the process is optimized for human attention, fast reversibility, small blast radius and recovery. The video walks through six layers of checks backed by rollbacks, shows a real failure mode where AI review loops forever, and ends with a practical recap for your own team.

**1. Reframe what review is for**
- **Ask what could go wrong:** Replace "did a human review this?" with "what could go wrong with this change, and which check, automated or human, should catch it?" This keeps the two original purposes of review in view: catching problems before shipping and spreading codebase knowledge across the team.
- **Make review continuous:** Treat checking like spell-check that runs while you write, from the first prompt through merge, rather than a single pre-merge event. Developers move to a higher-value point in the process instead of reading every line.
- **Aim for one human at most:** Target most PRs merging with at most one human in the loop, and that human can be the author.
- **Track human cost:** Measure human approvals per PR, PR comments, and how long a PR waits for a person, as a supplement to or replacement for DORA metrics.
- **Watch reverts and incidents:** Use revert and incident rates as guardrails. If they rise, you did not save human work, you just pushed it downstream into customer breakage and later fixes.

**2. Layer 1: Verify before a PR exists**
- **Demand evidence, not claims:** Have the agent run tests, build, take screenshots and run end-to-end and browser tests so it shows proof of completion instead of asserting it.
- **Review the diff with a fresh subagent:** Spin up a subagent with a clean context window to review the diff. Boris Cherny estimates verification makes results two to three times better.
- **Fix recurring findings at the source:** Put stack, conventions and goals in a short `CLAUDE.md` or `AGENTS.md`, and add an owner-written `review.md` stating what reviewers should prioritize.
- **Cap nitpicks:** Limit low-value AI findings, because false positives overwhelm reviewers and often target pre-existing code that merely appears in the PR rather than the actual change.

**3. Layers 2 to 4: Automated review and hard gates**
- **Run AI review against intent:** Review the diff against the full repository and the PR's stated intent before any person looks.
- **Use voting to filter findings:** Let several agents hunt bugs in parallel, have a separate group vote, and post a finding only when enough agents agree it is real.
- **Make security a hard gate:** Run security review separately and block merge while any bug-review or security-review finding is still open.
- **Keep conventional blockers:** Linting, type checks, tests on every platform and build tests still block merge.
- **Ask two questions in the PR template:** Require authors to state how they tested the change and how it can be undone, so verification and reversibility become explicit review inputs.

**4. Layer 5: Scale human approval by risk**
- **Tier by blast radius:** Low-risk docs, copy or additive feature-flagged changes need no human once automated and security checks pass; ordinary product work needs one person; high-risk code needs two.
- **Classify the change, not the author:** One classifier picks the tier and another checks whether a human is still required. CI workflow-file changes always need a person.
- **Limit light paths to trusted authors:** Only trusted authors, mostly from the owning team, get lighter approval.
- **Never count agent approval as human:** Automated review can clear a low-risk change but can never fill a required human slot.
- **Keep the prompter accountable:** Whoever prompted an agent-written change owns it and counts as reviewer, no matter how many agents were orchestrated.
- **Approve one commit only:** Approval covers a specific commit; if an agent pushes a new commit, require approval again.

**5. Layer 6 and recovery: Contain failures**
- **Use a merge queue:** Rerun all checks against main with the changes applied, so individually passing PRs cannot combine into a broken main.
- **Release in stages behind flags:** Ship new behavior to the internal team first, then to a wider "latest" channel of about 1,000 or more people and customers, then to stable only if earlier stages go well.
- **Optimize for fast rollback:** Use feature flags to disable behavior without a deploy, run a weekly on-call rotation, and in incident reviews ask which layer should have caught the issue.
- **Prefer faster detection over slowing down:** Slowing down lowers error rate mainly by doing less. Consider adding the missing "circuit breaker" that tightens or halts the system when agent work starts getting reverted often, like stopping a bottling line at the first defect.

**6. Stop AI review loops and evaluate the reviewer**
- **Know the trap:** One PR went through more than 50 overnight rounds of AI review and fixes; `git blame` showed about 59% of findings were code present since the first pass. A human dismisses a nitpick in seconds, but an agent fixes it, commits and triggers another review.
- **Cap review rounds:** After three rounds, have the reviewer tell the author to step back and rethink the overall approach.
- **Narrow later passes:** In later rounds review only the exact new diff, flag a whole bug class instead of one line, and never repeat a finding.
- **Turn incidents into evals:** Collect PRs that caused incidents, have knowledgeable engineers validate the set, and run the reviewer against it daily to see if it is improving or worsening.
- **Treat the factory as a living system:** Expect to design, build and keep learning to operate your agent pipeline rather than setting it once.

**7. Tools for the review layer**
- **Claude Code Review:** The public version of Layer 2, available at enterprise level: parallel agents inspect the diff, a verification step filters false positives, findings are severity-ranked with inline comments and a check run. Pick quick, standard or deep mode (deeper costs more); it never approves or blocks a PR.
- **Local pre-PR pass:** Run a lighter local review in Claude Code, Cursor or similar before opening a PR, and keep security review as its own layer.
- **Decide auto-merge by context:** Whether a fully green low-risk PR merges with no human depends on your codebase and its possible blast radius.

**Try this first:** Add a `review.md` to one repository listing what reviewers should prioritize, turn on an AI reviewer there, and tune it for a couple of weeks while tracking reverts.

**Caveat:** The throughput, quality and speed figures are Anthropic's own unverified reports, and Anthropic has huge inference capacity and sells inference, so treat its workflow as directional rather than a direct fit for your team.

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

## Evidence anchors
- [00:00:00.080] So claw code now writes about 90% of its
- [00:00:11.679] working. Between June and September
- [00:00:20.720] wrong dropped by 40%. So what the heck
- [00:00:40.320] So, anyone who's been working with
- [00:00:55.600] claw code team just published how they

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
