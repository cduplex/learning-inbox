# Run Your AI Software Factory Like a Real Engineering Org (Here's How)

## Source
- Original: https://www.youtube.com/watch?v=tNKmMhiOw9w
- Type: youtube
- Creator: {'displayName': 'Cole Medin'}
- Published: 2026-10-23T00:00:00.000Z

## Tags
AI software factory, agentic engineering, software delivery, human in the loop, agent registry, skill registry, context lake, repository readiness, CI, governance, Port

## Learning guide
**The arc**
Cole Medin starts from a problem: an autonomous AI software factory works for one app, but at enterprise scale or across many applications it needs a surrounding wrapper for guardrails, context and observability. His central idea is to keep your custom engineering harness unchanged and wrap it with four components: an agent and skill registry, a context lake, standards applied to every factory, and controls that keep factories aligned. He moves from the core loop, through ownership, context and readiness scorecards, to a CI self-repair workflow, and concludes that maximum autonomy should always keep a human in the loop.

**1. Build the core loop first**
- **Start simple:** If you are new to this, run only the core loop and skip the enterprise layers. A registry and context layer become important later, once you scale to many factories.
- **Plan a release with an agent:** Humans and an agent create planning context, such as a PRD, before anything enters the factory. For greenfield work, plan a proof of concept; for brownfield work, plan the next epic or task set.
- **Size releases at 10 to 20 tickets:** Plan work that can generally be split into that many tickets. This keeps each release manageable for the loop.
- **Split work and map dependencies:** Have an agent turn the plan into tasks and map which can run in parallel and which must wait. Use roles like a planner that builds the release plan and a backlog splitter that converts it into tickets.
- **Trigger the loop with a cron job:** A scheduled job picks the next issue by priority and dependency mapping. Each ticket then runs through plan, implement, validate.
- **Validate through a user journey:** Test each feature by asking how a user would test it, not just with unit checks. This makes validation reflect real application behavior.
- **Use a separate review agent:** A different agent reviews each pull request. Merge only when both CI checks and that review are green.
- **Drive every stage with a skill:** Write each stage as an elaborate skill defining the exact process, not a short prompt. Trust in the factory comes from investing effort in the harness, skills and agents.

**2. Ship through staging, not straight to production**
- **Merge to a staging branch:** Never merge factory output directly to production; merge to a branch deployed to staging. The whole release is assembled there across many ticket loops.
- **Validate the release in batch:** Review and test the assembled release in staging instead of reviewing every individual issue. This saves human time while keeping oversight.
- **Feed problems back as issues:** Submit anything wrong in staging as new issues so the factory picks them up. Expect a couple of iterations, then ship to production when staging looks good.

**3. Establish ownership with registries**
- **Give agents their own identities:** Agents running on an engineer's GitHub account make it ambiguous who is responsible when a production problem traces to a commit. Assign each agent its own identity.
- **Centralize skills in one registry:** Store every skill used in any factory in one place, with an owner and version control. Watch the count of distinct versions: a high number signals skill drift, so aim for one version of each skill distributed from the registry.
- **Govern the skill lifecycle:** Track ownership and publish status, recertify skills after updates, reject publication when needed, and deprecate old skills over time.
- **Inventory every agent role:** For each agent, record its runtime platform (for example Claude Code, Codex, Pi, or enterprise runtimes like GCP Vertex AI and AWS Bedrock), model, permissions and approval status. Permissions should state what the agent may touch and what it may not do.
- **Assign organizational owners:** Have owners manage creating agents, promoting them and updating permissions for different factories. Factories then pull common skills and agents from the registry while you keep control of how they are defined.

**4. Feed business context through a context lake**
- **Connect factories to business systems:** Skills and agents define a process but carry no business context. Link factories to GitHub repositories, CI, Jira, Slack, SharePoint and application or feature ownership data.
- **Use context to decide when humans step in:** Service tier, business domain, blast radius and the right owner for an approval request are not knowable from code alone. Use this context so high-risk work requires human merge approval while low-risk work runs more autonomously.
- **Pull context into release planning:** Use an MCP server (here, the Port MCP server) during the planning conversation to retrieve repository ownership, available starting templates and repository readiness. Tune what it searches and which systems (GitHub, Jira, Slack) it connects to, then use that context to build the PRD.
- **Track codebase status centrally:** Keep pull requests, factory status and CI status visible in one place. In the demo, a team knowledge base RAG app with source citations produced 20 pull requests from one PRD, all trackable.

**5. Enforce standards with scorecards and controls**
- **Score repository readiness before autonomy:** Define a scorecard of prerequisites a repository must meet to become an autonomous factory. Basic checks: a defined owner, a README, a pull-request template, a CI workflow, and CI passing on main.
- **Fix gaps before switching autonomy on:** Repositories below the target level (such as bronze vs gold) get a list of issues to resolve first. Note the platform cannot check everything, since your engineering loop is your own.
- **Use standards as ongoing controls:** Grade every merged pull request against the standards, not just at setup. A CI failure should be flagged immediately and drop readiness, for example from gold to silver.
- **Automate CI repair with an approval step:** When CI fails, have a workflow propose creating a GitHub issue to fix it, wait for human approval, then create it so the next factory loop picks it up. After the fix merges and CI goes green, the scorecard returns to gold.
- **Make your CI suite comprehensive:** Green CI only means something if the suite actually indicates application health. Flaky tests and breaking changes are common, so invest in CI coverage.

**6. Keep a human in the loop**
- **Avoid the dark factory:** Do not run with no human planning, no staging, direct production deploys, no approvals for CI changes and no visibility into autonomous changes. Medin moved away from that model deliberately.
- **Maximize autonomy within reason:** Embed owners, context, planning and approvals by default, then remove approval requirements only where appropriate. Aim for oversight on selected decisions, not lights-out operation.

**Try this first:** Pick one repository and check it against the readiness list: a defined owner, a README, a pull-request template, a CI workflow and passing CI on main. Fix any gaps before letting a factory loop run on it.

**Caveat:** The video was made in partnership with Port, and the registry, context lake, scorecard and workflow features shown are Port's own claims; the concepts apply generally, but the specific capabilities and the 2-day build result are not independently verified.

## Derived summary
## Source attribution
- The speaker presents personal experience and opinions about an AI software factory and a platform called Port. Product capabilities, results, and suitability claims are speaker or vendor claims and are not independently verified. [00:00:00]

## [00:00:00] Why a wrapper is needed around an AI software factory
- [00:00:00] The speaker says their AI software factory is their largest current project and that they have spent hundreds of hours refining it during the year.
- [00:00:07] They say they have begun helping companies adopt this type of system for selected teams and applications, rather than replacing all engineering work.
- [00:00:18] The speaker argues that a factory alone becomes insufficient at enterprise scale or across many applications; it needs a surrounding wrapper providing guardrails, context, and observability.
- [00:00:34] They characterize the factory as a highly autonomous form of AI coding, while retaining humans to communicate desired outcomes and plan releases with an agent.
- [00:00:43] In the described flow, an agent sends a release into a harness, which splits work into tasks and implements them in a loop.
- [00:00:46] The speaker says this is not a black box because the harness itself is engineered, but scaling still requires a harness to manage the system.
- [00:00:57] They do not want to build and maintain the wrapper themselves because it is more complex than it first appears; they prefer focusing on the engineering loop that performs development.
- [00:01:12] The stated requirement for a platform was to supply the wrapper while allowing the speaker to continue running a custom development harness.
- [00:01:22] The speaker identifies Port as the selected platform, claiming it supplies context, observability, and guardrails around factories, integrates with pull requests, monitors repository health, and leaves the custom factory in place.
- [00:01:43] The video is framed as more than a Port tutorial: it aims to extract enterprise-scale concepts such as component ownership and a central context layer across many factories.

## [00:02:01] Scope and four enterprise-scale components
- [00:02:01] The speaker says preserving the existing harness unchanged was a hard requirement because of the effort invested in it.
- [00:02:10] Their previously described architecture remains unchanged; Port is presented only as a wrapper around it.
- [00:02:18] The four topics announced are: an agent and skill registry, a context lake, standards applied to every factory, and controls to keep factories aligned as standards evolve.
- [00:02:33] The proposed lesson is what components are required to move a software factory toward enterprise scale.
- [00:03:12] For beginners, the speaker recommends keeping the system simple and using only the core loop initially.
- [00:03:20] They predict that scaling eventually makes an agent and skill registry plus a context layer important.

## [00:03:30] Core engineering loop
- [00:03:30] The process begins by planning the next release.
- [00:03:36] For greenfield work, the release plan is a proof of concept; for brownfield work, it is the next epic or task set.
- [00:03:45] The speaker suggests planning work that can generally be split into 10 to 20 tickets.
- [00:03:49] Humans work with an agent to create planning context, such as a PRD, before feeding it into the factory loop.
- [00:03:57] The agent uses the plan to split work into tasks and map dependencies, determining which loops can run in parallel and which tasks must wait.
- [00:04:12] Each ticket created from the split is sent through the core engineering loop.
- [00:04:19] A cron job usually triggers the loop on a schedule; it selects the next issue by priority and dependency mapping.
- [00:04:30] The selected issue proceeds through a plan, implementation, and validation cycle.
- [00:04:34] Validation includes planning around the described bug or feature, implementing the plan, and comprehensive testing.
- [00:04:43] The proposed testing approach validates the application through a user journey, asking how a user would test the new feature.
- [00:04:50] A separate agent performs code review on the pull request.
- [00:04:54] A merge occurs only after CI checks and the separate agent's code review are green.
- [00:05:00] The speaker rejects merging factory output directly to production; instead, work is merged to a branch deployed to staging.
- [00:05:08] The whole release is processed through many ticket loops and assembled in a staging environment.
- [00:05:16] Staging enables batch validation of the release instead of requiring humans to code-review and test every individual issue.
- [00:05:24] If validation finds problems, they are submitted as new issues so the factory can pick up feedback and implement changes.
- [00:05:36] The speaker says this usually takes a couple of iterations, after which the release is shipped to production when staging looks good.

## [00:05:51] Scaling concerns: ownership and traceability
- [00:05:51] The speaker transitions from the core loop to problems encountered when running multiple factories at scale.
- [00:06:04] They note that scaling includes concerns beyond the four featured components, particularly ownership.
- [00:06:11] Agents may use engineers' credentials, such as a GitHub account, creating ambiguity when a production problem traces to a commit from that account.
- [00:06:27] Port is said to address this by assigning identities to agents running in factories.
- [00:06:35] The speaker describes a registry in which every agent and skill has an owner and artifacts are version-controlled for use by factories as needed.
- [00:06:46] Port describes itself, according to the speaker, as a harness for orchestration, context, governance, and measurement.

## [00:07:02] Skill registry and agent registry
- [00:07:02] The skill registry is presented as a central store for every skill used in any factory.
- [00:07:09] It reports the number of distinct versions; the speaker considers a high count undesirable because it signals skill drift across factories.
- [00:07:21] The stated goal is one version of each skill, distributed from the registry.
- [00:07:28] The speaker considers this important because every stage in their engineering loop is driven by a skill, not merely a short prompt.
- [00:07:35] A skill is described as an elaborate definition of the exact process for a stage of the workflow.
- [00:07:40] The speaker says their trust in the factory comes from investing effort in the harness, skills, and agents.
- [00:07:52] Example skill-governance capabilities described include ownership, publish status, recertification after updates, rejecting publication, and deprecating skills over time.
- [00:08:13] Skills are defined as workflows, while agents are roles in the factory.
- [00:08:18] Example roles are a planner that builds a release plan and a backlog splitter that converts the plan into tickets.
- [00:08:25] For each agent, the registry records its runtime platform, model, permissions, and approval status.
- [00:08:28] The speaker names Claude Code, Codex, and Pi as possible drivers for parts of a factory, and later mentions GCP Vertex AI and AWS Bedrock as enterprise runtime examples.
- [00:08:35] Permissions specify what an agent may touch or may not do.
- [00:08:41] The registry is presented as an inventory of what drives the underlying harness, while the speaker retains control over how agents and skills are defined.
- [00:08:48] Port's claimed role is management and reuse, allowing factories to pull common skills and agents from the registry.
- [00:09:10] An analogous agent lifecycle includes creating agents, promoting them, and updating permissions; the speaker recommends organizational owners manage these for different factories.

## [00:09:23] Context lake: business and operational context
- [00:09:23] The speaker calls the context lake an especially important component because agents and skills define a process but do not themselves provide business context.
- [00:09:45] The proposed context lake connects factories with GitHub repositories, CI, Jira, Slack, and information about ownership of applications and features.
- [00:10:03] During high-level planning and individual-ticket execution, the speaker says critical information may be unavailable from the codebase alone.
- [00:10:16] Supplemental business context can come from Slack, SharePoint, or Jira.
- [00:10:22] One decision enabled by context is whether a human must approve a merge; the speaker contrasts more autonomous work with work needing review because its blast radius may be high.
- [00:10:30] The speaker says service tier, business domain, and the appropriate owner to receive an approval request may also be unknowable from code alone.
- [00:10:39] Their objective is for the factory not to operate in isolation, but to identify when people should participate, especially for specific higher-risk work.
- [00:10:52] In addition to business context, Port is said to contain codebase information including pull requests, factory status, and CI status.

## [00:11:04] Using context during release planning
- [00:11:04] Port is said to remain involved while a human and agent establish a plan before sending it into the factory.
- [00:11:20] The speaker uses a Port MCP server to retrieve planning context from the context lake.
- [00:11:28] Examples of retrieved context are repository ownership, available starting templates, and repository readiness.
- [00:11:37] The speaker says users can tune what the MCP server retrieves or searches and choose connected systems such as GitHub, Jira, and Slack.
- [00:11:46] The claimed effect is that the agent is better positioned to plan the factory run and define what to build.
- [00:11:54] In the demonstrated planning context, the speaker identifies owners, the factory team, repositories, and a bronze readiness level for a repository.
- [00:12:03] The context is used to assist a conversation with the agent that creates a PRD, which is then sent into the factory.

## [00:12:13] Example application and observed factory output
- [00:12:13] The speaker says they have already built multiple applications using their software factory and Port.
- [00:12:20] The demo application is a team knowledge base intended as a central place to get answers across repositories.
- [00:12:27] The speaker says they built it in 2 days, hands-off after creating the initial PRD. This is a speaker-reported result, not independently verified.
- [00:12:37] They describe it as a RAG application that searches the central knowledge base and provides source citations.
- [00:12:46] The speaker characterizes the application as not especially elaborate, but considers its output impressive for a couple of days of autonomous work.
- [00:12:53] For that release, the speaker reports 20 pull requests created from a PRD, with their statuses visible in Port.

## [00:13:07] Scorecards and readiness standards
- [00:13:07] A scorecard represents repository readiness: the prerequisites for a repository to become an autonomous factory.
- [00:13:15] The readiness scorecard is presented as a standard that can be applied to every software factory.
- [00:13:20] The central readiness question is whether the repository is ready for the proposed degree of autonomy.
- [00:13:26] The speaker notes a limitation: Port cannot check everything because the organization supplies its own engineering loop.
- [00:13:32] The demonstrated high-level checks include a defined repository owner, a README, a pull-request template, a CI workflow, and CI passing on the main branch.
- [00:13:45] If these checks pass, the speaker treats the repository as ready to implement the factory.
- [00:13:52] Repositories that are not at the target readiness level receive a list of issues to address before autonomy is switched on.
- [00:14:05] Standards serve both as setup checklists and as ongoing controls.
- [00:14:10] The speaker says Port grades every merged pull request against these standards.
- [00:14:16] If CI fails, Port reportedly flags it and can launch a workflow that seeks approval to create a factory issue for fixing the codebase problem.

## [00:14:37] Controls workflow: CI failure to self-improvement
- [00:14:37] The speaker introduces a recorded demonstration of scorecards and controls working together.
- [00:14:47] The demonstrated workflow handles a scorecard issue.
- [00:15:02] The speaker intentionally makes CI fail to demonstrate that Port detects the failure and triggers the workflow.
- [00:15:11] The workflow proposes, rather than immediately executes, creation of an issue to resolve the failing CI; human approval is required.
- [00:15:19] The speaker says the failure is contrived for the demo but asserts that CI commonly fails in real codebases due to flaky tests and changes that break things.
- [00:15:36] A backend CI failure changes the repository readiness status from gold to silver.
- [00:15:45] The workflow then waits for approval and proposes creating a GitHub issue for the factory to pick up and fix CI.
- [00:15:57] The speaker characterizes this loop as self-improvement guided by Port.
- [00:16:01] After approval, a GitHub issue is automatically created.
- [00:16:08] The next factory loop is expected to pick up that issue and fix CI automatically.
- [00:16:16] In the demonstrated outcome, the fix is merged, CI becomes green, and the scorecard returns from silver to gold.
- [00:16:26] The workflow is described as autonomous with a human in the loop for a quick approval step.
- [00:16:32] The speaker says the system can detect CI failure and self-improve; they qualify its value by saying green CI is most meaningful when the CI suite is sufficiently comprehensive to indicate application health.

## [00:16:49] Final recap: autonomy with human oversight
- [00:16:49] The speaker recaps the four covered components as mechanisms for evolving software factories.
- [00:16:57] They identify the human in the loop as the most important principle.
- [00:17:05] The speaker contrasts the current approach with their earlier "dark factory": no human planning, no staging environment, direct production deployment, no approvals for CI changes, and no visibility into autonomous changes.
- [00:17:26] They say they deliberately moved away from that model.
- [00:17:28] Their stated position is to maximize autonomy only within reason, retaining human involvement for selected decisions.
- [00:17:36] The described Port philosophy embeds owners, context, planning, and approvals when working with standards, then removes approval requirements only when appropriate.
- [00:17:50] The speaker says the usual intent is not to run completely lights-out, unlike the earlier dark-factory approach.

## [00:18:09] Sponsored-product aside
- [00:18:09] The speaker discloses that they worked with Port on the video.
- [00:18:11] They state that Port is free for up to 15 seats with no credit card required. This promotional availability claim is not independently verified.

## Evidence anchors
- [00:00:00.160] My AI software factory is hands down my
- [00:00:08.880] to help companies incorporate this kind
- [00:00:22.640] itself is not enough. When you get to an
- [00:00:30.400] that it has all of the guardrails,
- [00:00:36.320] represents the most autonomous form of

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
