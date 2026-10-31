# Anthropic Just Released A New System For Using Claude Code

## Source
- Original: https://www.youtube.com/watch?v=S49gppZl8H0
- Type: youtube
- Creator: {'displayName': 'AI LABS'}
- Published: 2026-10-30T00:00:00.000Z

## Tags
AI coding agents, Claude Code, code review, evals, software testing, multi-agent workflows, risk-based verification, Git, regression recovery

## Learning guide
**The arc**
Coding agents can produce substantial code and declare completion while leaving requested behavior unfinished. The central idea is to require evidence of correctness, independent review, and a way to recover when checks miss something. The workflow progresses from defining completion to running bounded review loops, testing real use, and preserving working versions.

**1. Define completion before building**
- **Ask how failure will be caught:** Review intended behavior, not whether someone merely read the code or the agent said it finished. Ask what could go wrong with each change and what check would reveal it; run checks during construction as well as before completion.
- **Turn requirements into evals:** Put each feature in its own folder under `specs`, with requirements in `RD.md` and an eval file describing how to check implementation. Each eval must be a fixed completion check strict enough to reject bad work, including use patterns beyond the expected path; require the agent to run it and show the result.
- **Save a design reference:** For features with a design, create a simple web-page mockup before modifying the application. Use it for early design review and later screenshot comparison, inspecting different screen states and the mobile layout.
- **Approve preparation first:** Store the requirements-to-evals skill in `.claude` with a template beside it for consistent eval files. Have the agent disclose independent decisions, move preparation from draft to in review, and obtain human approval of evals and mockups before marking the feature reviewed and ready to build; use hooks to check requirements setup and block completion until evals pass.

**2. Separate implementation, verification, and review**
- **Use an independent reviewer:** Do not let the builder be its only reviewer, because it carries the assumptions behind its implementation. Run a separate reviewer before human review; the lighter Claude Code review command starts a separate agent, with low effort targeting high-confidence issues and higher effort examining more of the application.
- **Make review rules explicit:** Create `review.md` in the project root defining real failures, severity, what to ignore, reporting format, and required testing methods. Link it from `claude.md` rather than copying all rules there, and explicitly ask the local review command to read it because it does not do so by default.
- **Give specialists fresh contexts:** Use a main orchestrator with three separate agents so implementation assumptions do not carry through every check. The builder implements `RD.md`, the verifier marks each eval passed or failed, and the reviewer applies `review.md` to find problems outside eval coverage.
- **Track the loop and escalate decisions:** Start the custom review loop by naming a feature, and use `state.md` to record the current round and remaining failures. Run the builder first, then verification and review, and feed findings into later rounds; when a decision cannot be made, report progress and ask the user rather than silently choosing.

**3. Turn repeated mistakes into reviewed rules**
- **Capture recurring failures:** Keep accumulated lessons at the bottom of `review.md` so future sessions can use them. Match repeated findings to earlier ones, and treat bugs that escaped review as candidates for rules that prevent recurrence.
- **Learn from false positives too:** Record recurring nonissues as rule candidates so review improves its precision as well as bug detection. At the end of the loop, propose a one-line rule for the relevant area and add it only with human approval.

**4. Scale checks to customer harm**
- **Classify risk before implementation:** Use a classification skill to ask what happens to a customer if the feature breaks. Label appearance-only mistakes low risk, a broken feature with no loss medium risk, and lost money, lockouts, or exposure of another person's data high risk.
- **Pass risk into eval preparation:** Feed the rating to the eval-writing skill so high-risk features receive stricter checks. This directs review time and usage toward failures with more damaging consequences rather than applying the same depth everywhere.

**5. Bound the review loop**
- **Reconsider after three rounds:** After three unsuccessful fix rounds, have the reviewer tell the builder to rethink its approach. Continuing the same pattern of fixes can keep consuming usage without resolving the feature.
- **Review the latest changes:** After the first round, focus review on what the last fixes changed instead of repeatedly reviewing the whole feature and reporting old findings again. Keep unresolved failures in the loop's state so they remain visible without becoming duplicate reports.
- **Report categories of mistakes:** Explain the kind of problem, not just its single location. Have the builder fix all occurrences of that category so review does not uncover the same underlying issue one instance at a time.
- **Set explicit stopping limits:** In the custom loop, each round includes building, checking every eval in the browser, and code review, with a five-round limit. Stop earlier if the same problem remains after two rounds of fixes; successful completion requires every eval to pass and review to find nothing new, while persistent failure is a separate reason to halt.

**6. Test real use beyond passing evals**
- **Use the feature as a customer:** Exercise each new feature yourself even after the loop passes. Real use can expose escaped bugs, while familiarity with implementation can hide places where a customer gets stuck.
- **Bring in a fresh user agent:** Invoke a first-time-user skill and name the feature to check, using subagents that never observed development. Let them explore the app without reading its code, then report confusing or blocked paths with proposed fixes.
- **Isolate exploratory testing:** Give fresh-user testing a temporary database so it does not touch real data. Enforce the code-reading restriction with a hook that also blocks attempts through terminal commands, preserving the first-time-user perspective.

**7. Preserve working versions and recover**
- **Save feature work with Git:** Instruct Claude through `claude.md` to use Git, create a branch for each feature, and save every working version. These saved versions help locate the change responsible for unexpected behavior and return to an earlier working version when checks miss a problem.
- **Reproduce before fixing:** Give the custom fix-a-bug skill a reported problem and have it repeat the same steps, investigate the cause, and check whether the suspected cause is correct. Then report and fix the problem, using saved versions to trace regressions and roll back when needed.

**Try this first:** Choose one feature, write its requirements in `specs` under that feature's `RD.md`, and draft an eval file stating what the agent must run and show to prove those requirements work before building.

**Caveat:** AI Labs promotes its community as the source of the demonstrated custom skills; these are its adaptation, not the Claude Code team's implementation, and the reported productivity gains and product capabilities are not independently verified.

## Derived summary
Source attribution: These notes summarize AI Labs' narration and its account of the Claude Code team's practices. Reported outcomes, product capabilities, and workflow demonstrations are source claims, not independently verified. The narrator's custom skills are distinguished from practices attributed to the Claude Code team.

## [00:00] Why faster coding requires stronger verification
- [00:00] The opening problem is that agents can write substantial code and declare completion while omitting requested functionality. The narrator makes checking actual behavior, rather than accepting completion statements, the central requirement.
- [00:17] The narrator attributes more than twice as many changes and an over 40% reduction in the share of changes undone to the Claude Code team's setup. AI Labs presents its own workflow adaptation, not the team's implementation itself.
- [00:47] Greater autonomy increases the review burden: an agent can work through a list of features for hours without someone watching the implementation decisions.
- [01:09] Across Anthropic, the narrator says daily changes needing review rose from about 2,500 to over 30,000 in just 4 months. More generated code creates more opportunities for mistakes to escape checks.
- [01:31] Errors reaching real users become larger problems. The team is quoted as saying that skipped review can ultimately cost twice as much time, because changes still need checking and escaped bugs then need fixing.
- [01:55] The review question shifts from whether someone read the code to what could go wrong with a change and how that failure would be caught. This focuses review on intended behavior.
- [02:08] Checks run during construction rather than only at the end. The narrator says this gives humans changes that have already been checked and corrected at least once, allowing attention to concentrate on likely failure points.

## [02:41] Step 1: Define evidence of completion with evals
- [02:41] Small checks during development are not enough. Deeper checks must test whether the app works under different patterns of use, not just the expected path.
- [02:54] Before a change advances, the team reportedly asks Claude to run something that demonstrates correctness and show the result. Examples include application tests and a screenshot comparison against a design.
- [03:05] The narrator attributes to Claude Code's creator the principle that an agent works best when it has a way to prove its work is correct.
- [03:14] An eval is described as a fixed check that determines whether work is complete. It must be strict enough for bad work to fail, rather than merely confirm that something was produced.

### [03:34] AI Labs' requirements-to-evals skill
- [03:34] The demo project uses a `specs` folder containing a folder for each feature. Each feature folder contains an `RD.md` file listing its requirements.
- [03:47] The proposed skill converts each feature into an eval file containing the actual method the agent will use to check its implementation.
- [03:58] For features with a design, the workflow first creates a simple web-page mockup instead of immediately modifying the application. That page becomes the saved design reference.
- [04:06] The real application is then developed toward matching the mockup. The narrator says this also enables an early design preview without spending too many tokens.
- [04:14] Evals must receive human review before any building begins. A separate hook prevents the agent from marking the task complete before the evals pass.
- [04:28] In the demonstration, Claude writes the skill into the `.claude` folder and places a template beside it so eval files share a consistent structure.
- [04:37] For a new feature, the skill opens the feature folder, writes the requirements document and eval file, and uses the hook to check that requirements are properly set up.
- [04:49] The preparation process iterates over eval quality and creates a viewable mockup. Once preparation checks finish, the feature status changes from draft to in review.
- [05:00] The agent discloses decisions it made independently and opens the files for inspection. Review includes different application screen states and the mobile layout.
- [05:15] The person reviews both evals and mockups, requests changes if needed, or approves them. Approval marks the feature as reviewed and ready to build.
- [05:28] **Promotional aside:** AI Labs promotes its community as the place to obtain the demonstrated skills. Elsewhere it asks for subscriptions and channel support.

## [05:40] Step 2: Use a separate reviewer and explicit review rules
- [05:40] Passing implementation evals does not eliminate review. The narrator argues that the builder should not review its own work because it made the original decisions and tends to agree with them.
- [05:53] The Claude Code team's second check is described as a separate reviewer agent that checks every change before a human sees it. The narrator reports that this increased reviews that catch real issues.
- [06:04] At the time described, the fuller reviewer is said to be available on Team and Enterprise plans, while a lighter code review command comes with Claude Code.
- [06:12] The command starts a separate agent to read changes and report mistakes that would break the app. An effort setting controls depth: low effort reports high-confidence issues, while higher effort examines more of the application.
- [06:27] The narrator says Anthropic's article recommends `review.md` for application-specific rules, but cautions that the local command does not read that file by default unless asked.
- [06:38] AI Labs' proposed configuration keeps rules in a separate file and links that file from `claude.md`, rather than copying all rules directly into the main instructions. The stated goal is to load review rules in new sessions.
- [06:58] Review rules should define real failures, issue severity, what to ignore, how findings should be reported, and the required testing methods.
- [07:09] The demonstrated setup places `review.md` in the project root and links it from `claude.md` so reviews, including the code review command, start from those rules.

### [07:21] Build, verify, and review with fresh contexts
- [07:21] The next custom skill implements a build-and-review loop. Subagents receive fresh context windows so they do not inherit the main agent's implementation assumptions and simply agree with them.
- [07:43] Claude creates three agents plus an orchestrating main agent. The orchestrator manages the loop and starts each specialist in its own context window.
- [07:53] The builder implements the feature from the requirements document produced by the eval-writing skill.
- [08:01] The verifier checks the application against those evals, determines whether the covered requirements were implemented, and marks each eval passed or failed.
- [08:12] The reviewer looks for problems outside eval coverage and applies the rules in `review.md`. Verification against predefined checks and broader code review therefore serve different roles.
- [08:19] To start the custom workflow, the user runs the review loop command and names a feature. The skill writes `state.md` to track the current round and remaining failures.
- [08:31] The builder works first, while the earlier hook prevents premature completion. The verifier and reviewer then run, and later rounds address their findings.
- [08:45] When the loop encounters a decision it cannot make, it provides a progress report and asks the user. Its successful completion condition is that every eval passes and review finds nothing new; later sections add stopping limits.
- [08:54] **Sponsor aside:** Unstoppable Code is promoted as an agentic IDE combining multiple coding agents, chained workflows, and terminal, browser, and diff views. The advertisement describes review and bug-fixing automation and a free-plan option.

## [09:55] Step 3: Turn repeated mistakes into reviewed rules
- [09:55] Fixing an issue once does not prevent recurrence: the narrator says Claude does not remember mistakes from earlier sessions and may repeat them on the next feature.
- [10:03] The Claude Code team reportedly responds to recurring reviewer findings by changing the instructions Claude reads, with the aim of preventing the same mistake.
- [10:11] AI Labs puts accumulated lessons in a section at the bottom of `review.md`. A bug missed during review but discovered later becomes a candidate for a new rule.
- [10:22] Repeated false positives also become rule candidates. This feedback aims to improve both detection of real bugs and avoidance of nonissues.
- [10:30] The loop matches repeated findings to earlier ones. At the end, it proposes a one-line rule for the relevant area and adds it only with human approval.

## [10:41] Step 4: Scale verification to customer harm
- [10:41] Thorough review consumes time and usage. The team's stated principle is to apply stronger checks when a feature failure could cause greater damage.
- [10:53] The team reportedly uses a classifier agent to sort changes rather than deciding review depth manually. The narrator reduces the classification question to what happens to a customer if the feature breaks.
- [11:06] Low risk means a mistake only makes something look wrong. Medium risk means a feature stops working but nobody loses anything, so it can be repaired later.
- [11:14] High-risk examples include customers losing money, being locked out, or seeing another person's data. The narrator emphasizes that these consequences cannot simply be taken back afterward.
- [11:24] AI Labs proposes a classification skill that assigns low, medium, or high risk before implementation. That rating is passed to the eval-writing skill so high-risk features receive stricter evals.

## [11:41] Step 5: Prevent review loops from consuming unlimited usage
- [11:41] Even worthwhile review can fail to converge when builders and reviewers keep exchanging issues without knowing when to stop.
- [11:50] The narrator describes a team change that went through more than 50 exchanges before someone manually stopped it. About 59% of the findings had reportedly existed since the first round.
- [12:08] Repeated rounds consume plan limits. The narrator says a major criticism of Anthropic's article was that its approach appeared to require unlimited tokens.

### [12:18] Three rules attributed to the Claude Code team
- [12:18] **Rethink after three rounds:** Instead of continuing to list problems, the reviewer tells the builder to reconsider its approach. The reasoning is that three unsuccessful fix rounds suggest more of the same work will not solve the feature.
- [12:33] **Review the latest changes:** After the first round, review focuses on what the last fixes changed and does not repeat previously reported findings. This avoids repeatedly reviewing the entire feature and rediscovering old problems one at a time.
- [12:45] **Report the problem category:** Findings describe the kind of mistake so the builder fixes all occurrences of that category, rather than just the single location identified.
- [12:54] The narrator reports that these rules increased the share of changes passing review on the first attempt.

### [13:00] Limits in AI Labs' custom loop
- [13:00] AI Labs says each of its rounds includes feature building, checking every eval in the browser, and code review. It sets a five-round stopping limit rather than three.
- [13:12] The custom loop can stop earlier if the same problem remains after two rounds of fixes. Passing all evals is therefore not the only possible endpoint; persistent failure can also halt the process.

## [13:19] Step 6: Find escaped bugs through real use and fresh-user testing
- [13:19] Even a finished loop with every eval passing can miss mistakes. The remaining requirements are a way to discover escaped problems and a way to undo problematic changes quickly.
- [13:27] The narrator says the Claude Code team can undo almost anything it releases within minutes, and links that recovery capability to its ability to read less code before release.
- [13:34] The team reportedly uses its own product every day and often notices problems before customers do. The equivalent practice described for viewers is to use each new feature as a customer would.
- [13:44] Familiarity with a feature can conceal usability problems. A fresh agent that never observed development is proposed as a complementary first-time-customer test.
- [13:55] The custom first-time-user skill launches subagents blocked from reading application code. They explore the app and identify places where a new user could get stuck, without implementation knowledge guiding them.
- [14:12] The demonstrated skill provides a temporary database so testing does not touch real data. A hook prevents code reading, including attempts through terminal commands.
- [14:30] The user invokes the skill and identifies the feature to check. It opens the app, launches the fresh agent, waits for completion, and reports findings with proposed fixes.

## [14:49] Step 7: Preserve working versions and investigate regressions
- [14:49] Finding problems is only half of recovery; the other half is undoing the changes responsible. The narrator introduces Git as a way to save application versions.
- [14:57] The proposed workflow gives each feature its own branch, described as its own copy of the project, so a problematic feature can later be undone through Git.
- [15:07] A custom fix-a-bug skill takes a reported problem and investigates its cause and possible correction.
- [15:17] The investigation attempts to reproduce the bug through the same steps, checks whether the suspected cause is correct, and then reports and fixes the problem.
- [15:26] The narrator says `claude.md` should instruct Claude to use Git, create a branch for each feature, and save every working version. Those saved versions support locating the responsible change and rolling back.

### [15:37] Closing recap: Recoverability completes verification
- [15:37] The final technical takeaway is that saved working versions let Claude trace unexpected behavior back to a change and return to an earlier version. This complements the earlier eval, independent review, risk classification, and fresh-user testing stages rather than assuming those stages catch everything.
- [15:45] The video ends with a brief request for channel support and a sign-off, without additional technical steps.

## Evidence anchors
- [00:00:00.080] There's a huge problem with using AI
- [00:00:01.839] agents. Whenever you give them a task,
- [00:00:03.679] they write a lot of code and then call
- [00:00:05.279] the task done. But when you actually use
- [00:00:07.200] what they built, you find they've missed

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
