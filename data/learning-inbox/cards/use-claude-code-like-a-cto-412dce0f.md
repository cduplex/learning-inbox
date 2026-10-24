# Use Claude Code Like a CTO

## Source
- Original: https://www.youtube.com/watch?v=6lfC9W5J-0Y
- Type: youtube
- Creator: {'displayName': 'Patrick Ellis'}
- Published: 2026-10-09T00:00:00.000Z

## Tags
AI coding agents, Claude Code, Codex, agent orchestration, long-horizon tasks, software engineering, verification, developer workflows, infrastructure as code, Terraform, gcloud, task management

## Derived summary
## [00:00:00] Thesis: leverage comes from orchestration
- [00:00:00] Patrick claims many engineers use Claude Code and Codex incorrectly and therefore lose substantial leverage.
- [00:00:08] He says frontier labs are building toward long-horizon autonomous work, but workflows have not broadly adapted to that shift.
- [00:00:21] His central claim is that 10x, 20x, and 100x-plus leverage comes less from smarter models than from the surrounding orchestration layer.
- [00:00:31] He defines that layer as context, tools, workflows, and verification that permit code-generation agents to operate for hours with less human intervention.
- [00:00:38] He asserts that teams investing in this layer gain compounding advantages, while teams that do not fall behind. These are the speaker's claims and are not independently verified.
- [00:00:46] Patrick identifies himself as CTO and co-founder of an AI-native startup and says it has worked with brands including Disney, Google, Coca-Cola, and FIFA.
- [00:00:57] He says his team has used AI-native tooling, including Claude Code and Codex, in production for more than a year.
- [00:01:05] He reports that in the prior week, his team shipped an end-to-end, production-scale analytics platform involving Pub/Sub, Cloud Run, and BigQuery within one week using the described workflow.
- [00:01:16] The video presents a four-pillar mental model, tactical practices, and purported real-world evidence intended to make future model releases increase productivity rather than anxiety.

## [00:01:29] Long-horizon-agent direction
- [00:01:29] Patrick says Anthropic and OpenAI appear to be converging on very long-horizon tasks.
- [00:01:43] He characterizes the goal as giving a model extensive direction, understanding, and context upfront so it can operate as long as possible before needing more input.
- [00:01:49] A task ends or pauses when the model lacks task clarity, tool access, or knowledge of the appropriate solution.
- [00:02:03] Referring to an earlier OpenAI podcast interview with Greg Brockman, Patrick says Brockman described Codex's technical vision.
- [00:02:18] Patrick says OpenAI initially made Codex a CLI tool but viewed that interaction pattern as too iterative, then moved toward cloud-hosted long-running tasks through the Codex web tool and eventually desktop app.
- [00:02:34] He describes the envisioned future Codex workflow as setting a task that runs for hours, potentially days or weeks, then returns a completed result.
- [00:02:48] Patrick contrasts Codex and GPT models, which he says have emphasized academic or higher-level tasks, with the messy realities of many company codebases.
- [00:03:01] He describes Claude Sonnet, Opus, and Claude Code as more scrappy: searching codebases extensively with Bash and tools to discover relevant context.
- [00:03:20] He contrasts this with Codex, which he characterizes as systematic, academically oriented, and precise when editing and executing a plan.
- [00:03:30] In his experience, Codex needed more information in advance but performed strongly when given a complete plan.
- [00:03:38] Patrick says version 5.5 seems to move OpenAI somewhat toward Claude Code's messy real-world-code behavior.
- [00:03:49] He says Opus is moving toward the long-horizon Codex vision, where up-front orchestration allows it to iterate for long durations without becoming stuck.
- [00:04:02] He frames this as a new industry and model-development paradigm.

## [00:04:08] Onboarding analogy and bottleneck
- [00:04:08] Patrick compares a model to a capable college student who is new to the team, company, project, and manager.
- [00:04:16] Under that analogy, the engineer must explicitly provide resources, code-quality expectations, accessible tools, and project context, anticipating questions asked during employee onboarding.
- [00:04:31] He argues that teams should invest in the orchestration layer now because labs are moving in this direction.
- [00:04:35] His stated bottleneck is no longer the model itself but the orchestration layer around it.
- [00:04:38] For each new model release, he tests capability by assigning the most ambitious project he can imagine.
- [00:04:46] His example starts from a meeting transcript, mocks, and assets, then asks the model to create sophisticated PRDs.
- [00:05:00] He also references the company's second-brain wiki and internal tooling to test how well the model can formulate a plan.
- [00:05:08] He says the models are excellent at this planning task.

## [00:05:10] Four pillars of the orchestration layer
- [00:05:10] Patrick introduces a four-pillar framework after asking what becomes the bottleneck when the model is not.
- [00:05:16] His prior framing covered context, tools, and verification; he adds workflows, or standard operating procedures, as a fourth pillar.
- [00:05:30] **Context** includes company and product information, application goals and scope, design language, performance requirements, and adjacent codebases.
- [00:05:45] For multi-repository systems, he includes microservices, third-party APIs, documentation, and Slack history as relevant context.
- [00:05:52] **Tools** include grep, web search, Playwright MCP, GCP or Terraform tooling, and the Supabase CLI.
- [00:05:52] He views tools as ways for an agent to proactively gather information, access infrastructure and data, import context, and take repository actions.
- [00:06:12] **Workflows and SOPs** can package engineering reviews, design reviews, end-to-end PR review, and bug discovery and triage through Sentry.
- [00:06:29] He also includes security reviews, gstack, and skill libraries in the workflow pillar.

## [00:06:35] gstack as packaged review workflows
- [00:06:35] Patrick says gstack packages Y Combinator office-hours material and best practices, including critical UX/UI thinking and security audits.
- [00:06:57] He describes these materials as workflows.
- [00:07:00] He notes that workflows can be large or bloated, but says they force a model to consider multiple perspectives.
- [00:07:13] He describes an SOP as a sequence of considerations, judgments, taste, earned knowledge, and industry practices.
- [00:07:23] His intended use is to force agents through those steps rather than relying on an unstructured response.
- [00:07:28] He says gstack had about 109,000 stars despite having been made only months earlier. This reported figure is not independently verified.
- [00:07:37] He cites `/office-hours` as an intake command for company, product, and objective information, intended to resemble early-stage YC office hours.
- [00:07:55] He describes a plan CEO review as a product review focused on desired features, customer validation, and appropriately scoped work.
- [00:08:08] He describes engineering review as a technical and architectural review and says he uses it most in daily work.
- [00:08:17] He describes plan design review as useful for UI-heavy work.
- [00:08:22] He says design review should consider edge cases, polish, and small interaction details, not merely visual appearance.
- [00:08:40] His preferred handoff is for the model to reach roughly 80% completion through structured consideration, after which he adds his own knowledge.
- [00:08:59] He says the question sets can also function as an interview mechanism to elicit needed information from the user.
- [00:09:09] In his example, gstack asks a series of questions, and he can choose a recommended answer or write his own.
- [00:09:21] He says he accepts the recommendation about half the time, then proceeds through additional questions as the system runs.
- [00:09:35] He cites DevEx, or developer experience, planning as particularly useful for agentic-orchestration tooling because it also stands in for the agent's experience.
- [00:09:49] The stated DevEx goal is to make systems as simple as possible.

## [00:09:52] Planning, execution, and adversarial review
- [00:09:52] Patrick separates planning and review capabilities: agents execute plans, then return for a robust review process.
- [00:10:06] He says he uses gstack review as part of that process.
- [00:10:10] An adversarial review can invoke CLI Codex from Claude Code to conduct a full review.
- [00:10:20] Conversely, a Codex workflow can invoke Claude Code through the CLI.
- [00:10:24] Patrick says cross-model review provides broader tests, including browser use and incorporated skills.
- [00:10:34] He built custom skills on top of gstack workflows.
- [00:10:41] One custom skill is named `review-and-push`.
- [00:10:43] He invokes it in Claude, Codex, or another environment and supplies a PR identifier such as `PR 1000`.
- [00:10:54] The command starts a workflow built on gstack skills.
- [00:11:05] First, it performs pre-flight checks, such as confirming the correct branch, identifying the PR, and running basic checks.
- [00:11:13] During PR setup, it invokes gstack's `/ship` command to prepare local code for CI/CD and create a mergeable PR.
- [00:11:29] It then performs a full gstack review and a full Codex challenge.
- [00:11:36] Patrick favors using multiple models because their training data, post-training workflows, and embedded behaviors differ.
- [00:11:48] He says cross-model diversity is particularly helpful for architecture, critical reviews, debates, and code review.
- [00:11:56] He also incorporates CodeRabbit, linters, and automated tests.
- [00:12:01] His intent is to supply the review process with as much contextual evidence and as many error-detection vectors as possible.
- [00:12:18] The workflow fetches GitHub comments, including comments from people and automated bots.
- [00:12:26] He says CodeRabbit is typically a source of those automated comments.
- [00:12:28] The workflow reads and triages comments, applies fixes, pushes changes, and watches CI/CD.
- [00:12:35] Tests, linters, dead-code analysis, and other tools are intended to catch issues.
- [00:12:45] It ends with a report of what changed so engineers remain informed about what is being pushed.

## [00:12:56] Verification pillar
- [00:12:56] Patrick identifies verification as the fourth pillar.
- [00:12:58] For UI work, he proposes Playwright screenshots of model output compared against screenshots from UI mocks in the specification.
- [00:13:10] The model can inspect its rendered frontend for overlap problems or critique its own design.
- [00:13:18] He recommends pairing that feedback with style guides, initial mocks, and other relevant references.
- [00:13:23] He calls static analysis and deterministic linters, formatters, and unit tests especially valuable verification methods.
- [00:13:34] His criterion is any CLI-runnable tool that can audit code for defined properties.
- [00:13:40] Examples include ESLint and unit tests.
- [00:13:43] He says models are strong at writing tests and argues there is little reason not to move toward a near test-driven-development process, especially for backend verification.
- [00:13:55] He also recommends tools that find abandoned dead code and unused variables.
- [00:14:02] His causal model is that agents need both strong kickoff context and clear examples of the finished state so they know what must change to reach it.
- [00:14:13] He warns that without explicit dead-code detection, models will not necessarily audit and remove dead code comprehensively.
- [00:14:21] His rule is to incorporate any existing deterministic developer tooling to unlock long-horizon work.

## [00:14:29] Tool access and infrastructure context
- [00:14:29] Patrick recommends exposing the `gh` CLI so agents can use GitHub, inspect old PRs, and gather history.
- [00:14:45] He uses Sentry to inspect and resolve issues and created an automated command named `sentry-fixes`.
- [00:14:53] `sentry-fixes` finds Sentry bugs, triages and fixes them, obtains a second opinion and review, then watches CI/CD through merge and passing checks.
- [00:15:10] His two favorite tools to expose are Terraform and `gcloud`.
- [00:15:17] At his GCP-based organization, he uses `gcloud` mostly in a read-only mode.
- [00:15:17] That read-only access lets agents gather logs, infrastructure configuration, server specifications, failed-deployment information, telemetry, and performance data.
- [00:15:41] He says this provides extensive infrastructure context during rollouts and production-issue triage.
- [00:15:51] He describes Terraform as a CLI tool for infrastructure as code.
- [00:15:55] In his description, infrastructure as code expresses infrastructure in standardized code.
- [00:16:03] One benefit is that the Terraform configuration provides agents extensive information about the infrastructure's current state.
- [00:16:11] For changes, Terraform can track what resources changed, why, and when, and support comparison between production state and Terraform configuration.
- [00:16:25] He says platform CLIs such as Supabase, GCP, or AWS can compare current cloud state with Terraform to identify infrastructure differences that should be applied to configuration.

## [00:16:40] Reducing interruptions and managing multiple agents
- [00:16:40] Patrick's target is to reduce questions requiring human answers from 100 to 5.
- [00:16:46] He says achieving that requires preliminary work to set direction and provide verification and test resources.
- [00:16:54] He presents this as necessary both for agents running while the user is unavailable and for orchestrating eight agents simultaneously.
- [00:17:04] He says context switching among eight or ten agents overwhelms his short-term memory.
- [00:17:10] His remedy is to reduce the number of questions agents need to ask and let work return only after QA and related processes.
- [00:17:20] He says engineers must systematically abstract themselves up one layer rather than constantly answering questions.
- [00:17:25] He warns that inattentively clicking through agent prompts can be dangerous, giving `rm -rf` of an entire code repository as an example.
- [00:17:35] In the displayed example, he says the deletion target was demo files that should be removed.
- [00:17:38] He returns to gstack's question prompts as a mechanism for surfacing the core areas where he should contribute expertise.
- [00:17:55] He characterizes planning and context gathering as the up-front first 10% of the work.
- [00:18:07] He acknowledges the up-front phase can be inconvenient but says it eliminates much later question-answering during execution.

## [00:18:16] Teams of agents and proactive work
- [00:18:16] Patrick calls team orchestration a major unlock.
- [00:18:20] His prerequisites are robust context, including mocks and UI elements, plus a locked-down workflow or SOP.
- [00:18:40] He uses custom skills for activities such as review and deep engineering or design audits.
- [00:18:52] He says he can create a team of Claude Code agents after preparing that context and workflow.
- [00:18:55] He says newer models, including Fable 5 and Opus 4.8, can often automatically spin up specialists or workers for separate code areas. This capability claim is not independently verified.
- [00:19:09] The specialists can each handle areas specified by skills and invoke sub-skills.
- [00:19:21] In his `review-and-push` example, adversarial review can run concurrently with the primary review and other tasks.
- [00:19:36] He says teams can be spawned and orchestrated in parallel, or agents can nest sub-agents, to complete more work.
- [00:19:50] He says he likes Codex but wants it to adopt more dynamic, recursive delegation and composition.
- [00:20:06] Patrick says rich deterministic requirements, company context, product knowledge, and research tooling enable agents to generate proactive ideas and suggestions.
- [00:20:24] His example is an agent detecting an issue-tracker bug, writing a test, understanding styling, fixing the regression, running QA, and opening a PR.
- [00:20:41] He argues that constraints and guardrails are creatively enabling because they help a model distinguish good proposals, identify obvious problems, and prepare changes likely to merge.

## [00:20:57] Analytics-dashboard case study
- [00:20:57] Patrick introduces the analytics dashboard as a practical example.
- [00:21:06] Inputs included rough UI mocks or sketches, several product-meeting transcripts, and CEO notes.
- [00:21:18] He combined those materials into an initial PRD-style brief, alongside a UI mock that was originally an HTML page from Claude Design.
- [00:21:34] The inputs conveyed the intended dashboard aesthetic and feature set.
- [00:21:41] He identifies the result as a finished analytics dashboard with many UI elements.
- [00:21:47] He says the system must aggregate data while handling spiky, large live-sporting-event demand, including examples involving the NFL or FIFA.
- [00:22:01] He says the dashboard supports PDF export, data visualizations, and advanced sharing options.
- [00:22:08] He characterizes the speed of building as days or hours.
- [00:22:14] He characterizes the potential as a 50x-plus range when a solid company second brain and orchestration layer are present. This is his unverified assessment.

## [00:22:26] Design systems as context
- [00:22:26] Patrick says Claude Design can supply useful context to workflows.
- [00:22:32] For his personal website, he says he uses it to create an entire design system.
- [00:22:39] The design process addresses iconography, white space, typography, and related elements, then generates samples.
- [00:22:53] His stated brand direction was a fun, creative-work, entrepreneurial space rather than a cyberpunk-themed AI aesthetic.
- [00:23:01] He explored design directions and color palettes, then converted results to design files to inspire a website redesign.
- [00:23:17] He says the analytics example followed the same design-system process.
- [00:23:26] He lists Claude Design, GPT Image 2 within ChatGPT, personal designs, and other mockups as potential ways to obtain high-quality visual context.

## [00:23:37] Task management with Beads
- [00:23:37] Before GPT-5.5, Patrick says he typically used Claude Code with Beads.
- [00:23:44] He describes Beads as an open-source project by Steve Yegge that helps models remain disciplined by working issue by issue and closing each item.
- [00:23:55] He says Beads provides a stronger task-management system for complex Claude Code tasks.
- [00:24:02] He says Claude Code's Tasks feature was modeled after Beads and acknowledged Steve Yegge at release. This historical claim is not independently verified.
- [00:24:10] He compares Beads to Linear or Jira-style task management and calls it critical for keeping long-horizon tasks on track.
- [00:24:23] He says a conventional Markdown task file may be skipped through as a model approaches its context-window limit.
- [00:24:23] He says native task structures enable models to store and save individual tasks more reliably.
- [00:24:42] He says task structure also helps enforce end-to-end SOP adherence, dependency graphs, and completion of every issue.
- [00:24:58] He calls Beads a useful framework for these purposes.
- [00:25:03] He says Beads has basic but powerful features.
- [00:25:06] A favorite tool is the open-source bead viewer, invoked with `bv`.
- [00:25:09] The viewer shows tasks, their hierarchy and relationships, and detailed information about each bead.
- [00:25:23] He describes beads as database entries that make visible what Claude Code or Codex can access.
- [00:25:30] He says that structure helps verify that long-running agents stayed on track and did not falsely report incomplete work as finished.

## [00:25:45] Manager-agent workflow, reviews, and deployment controls
- [00:25:45] Patrick says one powerful workflow is asking Claude Code to create and manage a team of other Claude Code agents, such as producing five or 20 PRs for a project.
- [00:25:59] He frames the higher-level interaction as working with an engineering-manager Codex that delegates PR-based implementation to sub-agents.
- [00:26:11] He says this depends on investing in orchestration so both workers and manager have enough context for end-to-end work and management.
- [00:26:22] The manager agent can absorb many day-to-day questions if the specification and orchestration layer have been prepared.
- [00:26:32] In one example, he ran Codex overnight for six hours to complete much of the core work, followed by additional sessions.
- [00:26:46] He then brought the implementation and PRs into Claude Code, returning to the initial gstack session for design and engineering review.
- [00:26:52] He used Codex as an adversarial reviewer in a new session to work through remaining architecture and feature issues.
- [00:27:07] He also advocates allowing models to observe and manage the deployment process.
- [00:27:13] His deployment example uses `gcloud` and Terraform to help configure environment variables and proceed through deployment.
- [00:27:20] He gives a strong warning that permissions must be structured appropriately.
- [00:27:22] He wants agents to have enough freedom to collect required information.
- [00:27:29] His own example permits access to logging infrastructure and infrastructure configuration for information gathering.
- [00:27:38] He says agents should not make changes to core infrastructure without human review.
- [00:27:44] Referring to a Cheeky Pint episode and John Collison, he says Collison praised the `gcloud` CLI.
- [00:27:53] Patrick calls safe agent-assisted infrastructure work with Terraform, `gcloud`, or equivalent cloud tooling a game changer, especially for documenting infrastructure to agents. This value claim is not independently verified.

## [00:28:12] Strategic framing and recap
- [00:28:12] Patrick says the tips and workflows compound, but only if the team and company are organized to benefit from that compounding.
- [00:28:21] He frames the final section as a strategic explanation for aggressively advancing code-generation orchestration.
- [00:28:32] His analogy is a graph with time on the x-axis and a startup's AI-compounded output on the y-axis.
- [00:28:45] He predicts that being ahead by a week or month will create exponentially increasing leverage over others.
- [00:28:54] He says the advantage may come through distribution and especially through code-generation infrastructure.
- [00:28:58] He argues that being only somewhat ahead through better processes and a few more automations compounds at an increasingly large rate.
- [00:29:09] His encouragement is that viewers need only be a little further ahead on that curve.
- [00:29:15] He says his most durable investment is documenting startup context and aggregating it into a single orchestration layer.
- [00:29:32] His reasoning is that models will not inherently know a company's specific context, tooling, verification practices, and workflows unless people explicitly provide them.
- [00:29:42] **Final recap:** Build on the expectation that models and agent harnesses will improve, and prioritize investments in context, tools, verification, and workflows that are amplified rather than replaced by improved models.

## [00:29:54] Aside: channel and newsletter promotion
- [00:29:54] **Promotional aside:** Patrick says he is returning to YouTube after a busy startup period focused on AI-native tooling.
- [00:30:07] **Promotional aside:** He says he plans to share more workflows about Claude Code, Codex, and second brains.
- [00:30:27] **Promotional aside:** He mentions a newsletter sign-up for a video summary, linked tools, and future updates.
- [00:30:39] **Promotional aside:** He points viewers to other videos, including one about getting better design from Claude Code or Codex.

## Practical applications
- Suggestion: Audit an existing agent workflow against the four source-described pillars: context, tools, workflows/SOPs, and verification. Record missing inputs rather than assuming a stronger model will compensate.
- Suggestion: Create a bounded planning intake that gathers product goals, repository context, mockups, performance requirements, and acceptance criteria before launching a long-running coding task.
- Suggestion: Add deterministic verification to agent-generated changes, such as linting, formatting, unit tests, static analysis, dead-code checks, CI/CD monitoring, and where relevant screenshot comparison against approved UI mocks.
- Suggestion: Use an adversarial or cross-model review stage for high-impact PRs, while keeping a human-readable final change report for engineer oversight.
- Suggestion: Grant cloud and infrastructure tools read-oriented access for context gathering where feasible, and require human review before agents modify core infrastructure.
- Suggestion: Represent complex work as structured tasks with dependencies rather than relying only on a Markdown checklist, then review task completion against actual artifacts and tests.
- Suggestion: When coordinating multiple agents, reduce interruptions by investing first in shared specifications, tool access, SOPs, and explicit completion criteria.

## Evidence anchors
- [00:00:00.000] Most engineers are using Claude Code and Codex wrong, and it's costing them massive leverage.
- [00:00:08.760] Every frontier lab is building for one thing, long-horizon autonomous work.
- [00:00:21.780] The 10x, 20x, and 100x-plus level leverage is not coming from the models getting smarter.
- [00:00:27.580] It's coming from the orchestration layer around the models.
- [00:00:31.240] The context, tools, workflows, and verification.

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
