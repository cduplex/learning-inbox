# Build Your Own AI Software Factory with Claude Code

## Source
- Original: https://www.youtube.com/watch?v=ctoaIC4LHmI
- Type: youtube
- Creator: {'displayName': 'ZazenCodes'}
- Published: 2026-10-07T00:00:00.000Z

## Tags
software factory, Claude Code, agent orchestration, subagents, code review, Git worktrees, Markdown state, human-in-the-loop, CI/CD, developer productivity

## Learning guide
**The arc**
The video starts from a practical question: can you build a simple but effective AI software factory inside an existing project, so a feature request becomes merged code with little human effort? The central idea is a repository-local, skill-driven team of Claude Code agents (spec writer, builder, reviewers, approver) whose state lives in Markdown files, with a human approval gate at the end. It moves from the factory concept to a single build prompt, a first live job, parallel jobs with Git worktrees, fixes for real failures, and finally future extensions and cost.

**1. Understand the factory model**
- **Think in loops:** The basic loop is trigger, agent, pull request, human merge. AI lets you automate the unstructured cognitive work, including code writing, between deterministic stages like CI/CD and GitHub Actions.
- **Define the agent pipeline:** Use the flow feature, spec writer, builder, review agents, possible rework loop, approver, then automatic merge or human review. An Opus spec writer produces the spec, a builder implements the full feature, and separate security, UX, UI-design and code-review agents assess it.
- **Close the review loop:** Feed review output back to the builder until the code is satisfactory. A separate Opus approval agent then decides between auto-merge to main and escalation to a human.

**2. Write the build prompt and set up Claude Code**
- **Build inside a real repo:** Add the factory to an existing, complex project rather than a clean demo repo, so it fits your actual codebase.
- **Pick permissions and model deliberately:** The demo ran Claude Code with bypass permissions, which lets Claude do anything, so choose your own permission level. Use Opus at high effort so the agent follows the prompt's details and aims for quality.
- **State the spec in one sentence:** Ask for a visual software factory in the repository using Claude skills, subagents and Markdown files, with Markdown controlling application state. Make Claude Code the orchestrator, using whatever model is selected, with a factory skill that starts the system.
- **Plan for future intake:** Write the prompt so jobs can later come from external data sources or triggers, not only direct feature requests.
- **Specify structure and examples:** Follow the agent-skill convention, add a `factory` folder in the app, and include example files showing the subagent syntax and style you want. Define commands like invoking `factory` with a feature description, plus a dashboard for visibility.

**3. Review and configure the generated factory**
- **Know what gets generated:** Expect approval, builder and reviewer subagents, an orchestrator skill, a Markdown backlog of unbuilt jobs, a dashboard, and small edits to agent and ignore files. The orchestrator skill sits in the project's Claude skills location, so Claude Code indexes it and documents patterns like `factory /feature`.
- **Set rework limits and a branch:** The generated settings used a maximum of two rounds, a `factory` checkout/branch for the builder, and a rework method that sends failed work through again.
- **Add repo-specific escalation rules:** Tell the approver which changes always need a human, such as billing-related changes and course-access changes.
- **Restart to load agents:** Restart Claude Code after generation so the new agents load. Check the backlog, since it may contain unexpected starter items.

**4. Run your first job**
- **Commit before starting:** The factory requires a clean working tree, so commit and push the factory code first.
- **Watch the phases on the dashboard:** A job gets a name, the spec writer writes a spec file, the builder writes a build file, then the system returns to main and launches all reviewers. A "needs human" phase catches stuck work or items needing review.
- **Approve escalated work by ID:** When the approver escalates, read the escalation details and acceptance criteria on the dashboard, find the feature ID, and run `factory approve`. The builder branches off, makes several commits, and merges only after your approval.
- **Expect loose approval input:** `factory approve` invokes the factory skill, but the approval text is free-form, not a strict schema.

**5. Manage Markdown state**
- **Keep metadata as plain text:** The dashboard reads Markdown files in the `factory` directory, which you, agents, future agents or other systems can inspect directly.
- **Decide on committing vs backup:** Committing metadata can clutter fuzzy file search. If the directory is Git-ignored, it is transient and vanishes on a fresh clone, so set up a custom backup such as agent-managed cloud storage.

**6. Run jobs in parallel**
- **Add Git worktree support:** Without worktrees the factory handles concurrent features poorly, so ask Claude to add worktree integration; jobs then run without manual worktree switching. You can even use the factory to build this.
- **Launch jobs in tmux panes:** Run `factory next` in separate tmux panes to pull backlog items like a blog reading-time label, a code-block copy button and a 404 page.
- **Mix models by role:** Use a capable model like Opus for orchestration and try faster models like Sonnet at low effort elsewhere. Subagents largely set the speed, so a faster orchestrator alone may not help.
- **Own your factory:** A small in-house factory is one your team can inspect, modify and understand, instead of depending on a large third-party skill.

**7. Fix failures and tune guardrails**
- **Loosen overly strict guardrails:** If agents keep finding reasons to request manual review (for example avoiding a blog render cache invalidation), your rules may be too strict.
- **Allow backlog changes in the clean-tree check:** Auto-merge failed because main had to be clean and on `main`, but the backlog file always changes during operation. Exempt that specific backlog file from the condition.
- **Commit stray changes before merging:** When one job's changes block another's merge, commit them separately, then merge the remaining work.

**8. Extend the factory and weigh cost**
- **Add external intake:** Connect GitHub Issues, which many people can submit, are tracked, and fit GitHub workflows; Slack is another trigger.
- **Connect monitoring and metrics:** Feed production bugs and context from tools like Sentry, plus CPU and memory metrics, so the factory can undo a harmful feature after release.
- **Judge cost against quality:** Subagents cost more because context passes between agents. Decide whether the extra tokens are worth it; the demo used a Claude plan, not API tokens.

**Try this first:** In a real repo with a clean, committed working tree, paste a one-sentence prompt into Claude Code (Opus, high effort) asking for a visual software factory using Claude skills, subagents and Markdown state, then run `factory` with one small feature from your backlog.

**Caveat:** The video is sponsored by Anthropic and the whole setup depends on Claude Code; the claims about quality gains and that the general prompt transfers to other projects are untested, so measure cost and results on your own repo.

## Derived summary
## Overview and factory model [00:00:00]
- [00:00:00] **Sponsor aside:** Anthropic sponsored the video; the presenter says the build uses Claude Code with a mix of Opus and Sonnet, described as version 5.5 at filming.
- [00:00:19] The presenter frames this as a hands-on build of a deliberately simple but potentially effective software factory that can be added inside an existing project.
- [00:01:05] The target system accepts a feature request and has a team of agents bring it into the main codebase, with autonomy until a final human-approval stage.
- [00:01:23] Workflow: an Opus spec-writing agent produces a spec; a builder agent implements the full feature; separate security, UX, UI-design, and code-review agents assess it.
- [00:01:47] Review output feeds back to the builder in a loop until the code is satisfactory; a separate Opus approval agent then chooses automatic merge to main or escalation for human review.

## Background: what a software factory is [00:02:16]
- [00:02:16] The presenter says Bob Beamer at GE first described software factories in 1968 as computer-controlled programming environments with standardized development tools and historical information for management and measurement.
- [00:02:34] In the presenter's abbreviated history, early factories had activity in Japan and elsewhere; the 2000s emphasized reusable patterns, models, and frameworks; the 2010s and 2020s added CI/CD, continuous integration pipelines, and GitHub Actions.
- [00:03:02] The AI-era framing is automation of relatively unstructured cognitive work between deterministic stages, including code writing itself.
- [00:03:18] The basic loop is trigger → agent → pull request → human merge, with agents pulling in information and forming richer workflow graphs inside the loop.

## Initial implementation prompt and architecture [00:03:46]
- [00:03:46] The presenter pastes a single build prompt into Claude Code and says its source is available with the video.
- [00:04:02] The factory is built inside the presenter’s existing website repository, described as a complex real project rather than a clean demo repository.
- [00:04:20] Claude Code is run with bypass permissions, which the presenter says lets Claude do whatever it wants; viewers are told they can choose their own permission level.
- [00:04:27] The selected configuration is Opus 5.5 at high effort so that the agent follows the prompt’s details and aims for higher-quality output.
- [00:04:50] The one-sentence specification is a visual software factory in the repository using Claude skills, subagents, and Markdown files, with Markdown controlling application state.
- [00:05:04] Claude Code is the orchestrator, using whichever model is selected at runtime; a factory skill starts the system.
- [00:05:17] The requested reusable flow is feature → spec writer → builder → review agents → possible rework loop → approver → automatic merge or human review.
- [00:05:49] The prompt anticipates future intake from external data sources or triggers other than direct feature requests.
- [00:06:02] The proposed project structure follows the agent-skill convention, adds a `factory` folder inside the app, and provides example files to indicate intended subagent syntax and style.
- [00:06:24] Intended commands include starting a job by invoking `factory` with a feature description; a dashboard provides visibility while the system runs.

## Generated factory components and operating choices [00:06:43]
- [00:06:43] The presenter claims long-running agentic tasks can capture small details, and says Opus is particularly good at propagating those details through generated code. This is the presenter’s assessment, not independently verified.
- [00:07:03] Claude generates reviewer agents as Claude subagents and then finishes by creating the factory dashboard.
- [00:07:22] Generated settings include a maximum of two rounds, a `factory` checkout/branch for the builder, and a rework method that can send failed work through the process again.
- [00:07:37] The presenter configures repository-specific escalation examples: billing-related changes and course-access changes should be escalated.
- [00:07:51] The presenter characterizes the original prompt as general rather than adapted to this website, and says a comparable setup should work for another project. This is an unverified presenter claim.
- [00:08:03] Restarting Claude Code loads the new agents; the generated backlog unexpectedly contains three starter items, and the dashboard initially shows no active work.
- [00:08:50] The generated files include approval, builder, and reviewer subagents; an orchestrator skill; little factory code; a Markdown backlog tracking unbuilt jobs; a dashboard; and small agent-file and ignore-file modifications.
- [00:09:43] The orchestrator skill documents invocation patterns, including `factory /feature`; Claude Code indexes it as a project-specific skill because it resides in the project’s Claude skills location.

## First live job: unpaywall course pages [00:10:20]
- [00:10:20] The test request is to make the presenter’s Obsidian-agent setup course pages accessible without a paywall while keeping videos paywalled, on the presenter’s production website.
- [00:10:40] The factory refuses to start because its precondition requires a clean working tree; the presenter commits and pushes the factory code before retrying.
- [00:11:02] On retry, the factory creates an “Obsidian course unpaywall” job, invokes the spec-writer background agent, writes a spec file, and starts the builder.
- [00:11:46] The dashboard shows active code edits and includes a “needs human” phase for work that gets stuck or requires human review.
- [00:12:13] The builder writes a build file into the factory; afterward the system returns to main and launches all review subagents.
- [00:12:30] UX and UI review pass; security review and code review proceed afterward.
- [00:12:57] The approval process escalates the feature to the human-review phase rather than merging automatically; the dashboard exposes details about the escalation and acceptance criteria.
- [00:13:26] Human approval is performed by identifying the feature ID and running `factory approve`; the presenter reports that the feature then merged into the actual codebase.
- [00:13:53] Git status shows the branch four commits ahead. The presenter describes the agent workflow as branching off, making several commits, and merging back only after the human approval.
- [00:14:20] `factory approve` invokes the `factory` agent skill, but the subsequent approval text is free-form rather than a strict approval schema.

## Markdown metadata and persistence tradeoff [00:14:43]
- [00:14:43] Dashboard information is populated from metadata stored as Markdown files in the project’s `factory` directory, including files for the feature just built.
- [00:15:06] The presenter values the plain-text approach because it can be inspected directly and used by agents, future agents, or other systems.
- [00:15:19] Committing factory metadata is technically possible, but the presenter warns that it could clutter fuzzy file search.
- [00:15:34] In this repository, the factory directory is ignored by Git, so this metadata is transient and disappears on a fresh clone unless backed up.
- [00:15:55] The presenter’s stated preference is custom backup, such as cloud storage managed by an agent. This is a suggestion from the presenter, not a demonstrated implementation.

## Parallel jobs with Git worktrees [00:16:14]
- [00:16:14] The factory initially cannot handle multiple concurrent features well because it lacks Git worktree support, so the presenter asks Claude to add that integration.
- [00:16:41] The presenter notes that the factory could itself have been used to build this worktree capability, but it was added directly in this demonstration.
- [00:16:50] Backlog examples are: show estimated reading time beside a blog date, add a copy button to code blocks, and add a 404 page.
- [00:17:16] The presenter launches `factory next` in separate tmux panes to run multiple jobs in parallel; the dashboard then shows two features entering the factory, followed by a third.
- [00:18:10] One orchestration session uses Opus 5.5, while another is switched to Sonnet 5.5 at low effort for the remaining 404-page feature.
- [00:18:36] The presenter expects Sonnet to be fast but notes that the orchestrator may not be the bottleneck because subagents, still using Opus, determine much of the speed.
- [00:18:59] The presenter’s design intuition is to use a highly capable model for orchestration and potentially faster, lower-capability models for some subagents. This is an unverified opinion.
- [00:19:21] The presenter says Git worktrees let concurrent jobs proceed without manually switching worktrees.
- [00:19:39] The stated advantage of building a small in-house factory is ownership: its team can inspect, modify, and understand it instead of depending on a large third-party skill.

## Parallel-run observations and failure handling [00:20:39]
- [00:20:39] The Sonnet-orchestrated 404 job reaches review and triggers all review agents; the blog reading-time feature also proceeds through the pipeline.
- [00:21:00] The presenter expects the reading-time feature may face greater UI/UX scrutiny because it affects the interface, unlike the other features.
- [00:21:21] The 404 feature enters “needs human.” The presenter suspects guardrails may be too strict if agents consistently find reasons to request manual review.
- [00:21:38] Another feature requires human review because Claude does not want to invalidate the blog render cache, which the presenter says would take time during merge.
- [00:21:58] A case appears approved but does not auto-merge because merge requires the main checkout to be clean and on `main`; changes to the backlog violate that condition.
- [00:22:34] The presenter changes the condition so that changes to the specific backlog file are permitted, since those changes are inevitable during factory operation.
- [00:22:56] The presenter manually approves two items. Another feature cannot merge because of changes produced by the Sonnet update, so those are updated and committed separately before merging the remaining work.

## Future extensions and post-deployment loop [00:23:58]
- [00:24:05] The presenter recaps four ways to improve the basic factory, starting with the already-demonstrated Git-worktree support for parallel jobs.
- [00:24:21] GitHub Issues could become an intake source, and Slack is another proposed trigger. The presenter says Issues are useful because many people can submit them, they are tracked in GitHub, and they integrate naturally with GitHub workflows.
- [00:24:49] Application monitoring could be connected, with Sentry given as an example, so production bugs and relevant context can enter the factory.
- [00:25:07] The presenter calls metrics access critical and links it to the original factory idea of incorporating monitoring and measurement.
- [00:25:21] Infrastructure metrics such as CPU and memory could support post-deployment monitoring. If a feature harms the software, the factory could undo it and remain part of the loop after production release.

## Cost and final recap [00:26:14]
- [00:26:14] **Sponsor aside:** Anthropic is thanked again; the presenter invites viewers to use Claude Code and follow along in their own projects.
- [00:26:14] The presenter identifies cost as the major remaining consideration: the system may provide useful observability and quality, but subagents can cost more because context must be passed among agents. These quality claims are not independently verified.
- [00:26:48] The practical tradeoff is whether added token cost is justified by quality. The presenter says this demonstration used their Claude plan rather than API tokens.
- [00:27:04] Final position: despite the cost consideration, the presenter intends to build more factories and describes the approach as their preferred direction for future work.
- [00:27:16] **Recap:** The demonstrated design is a repository-local, skill-driven agent factory with Markdown state, specialized builder and reviewer subagents, human escalation, a dashboard, optional parallel worktrees, and potential future external intake and monitoring.

## Evidence anchors
- [00:01:05.280] is what we're going to build. It's a
- [00:01:23.439] Let's walk through this. First thing we
- [00:01:47.680] fed back into the builder agent. And
- [00:02:16.400] mind map. Software factories were first
- [00:02:43.680] software factories. Then in the 2000s we

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
