# Pi Durable PROACTIVE Agents: Jev Triggers My ON-CALL Pi Agent

## Source
- Original: https://www.youtube.com/watch?v=DNDYYHsypZg
- Type: youtube
- Creator: {'displayName': 'IndyDevDan'}
- Published: 2026-10-12T00:00:00.000Z

## Tags
Pi Durable, durable agents, agentic engineering, proactive agents, incident response, shared application state, durable tasks, multi-client agents, agent harnesses, human near the loop

## Learning guide
**The arc**
IndyDevDan starts from a question: why does durability matter beyond an agent's ordinary `/resume`? His answer is that durable agents, which persist work, conversations, and application state across failures, clients, and change, let you run proactive agents that start work before you arrive and wait for your review. He walks from a live incident-response demo through sessions, shared state, phased tasks, multi-client access, live reconfiguration, and safety extensions, and concludes that engineers should own this harness and measure success by how many agents do useful work without a human kickoff.

**1. Own the foundation**
- **Own your agent stack:** Control your agent, harness, and durable-agent infrastructure instead of only renting intelligence. Outsourcing it makes you dependent on technology others can change. Prefer open-source, extensible, controllable tooling like Pi and Pi Durable.
- **Aim past `/resume`:** Durability means state survives failures, clients, and change, not just reopening a conversation. A standalone stuck session (default Pi, Claude Code, Codex) cannot serve a phone, a website, and a terminal at once.

**2. Build a proactive incident agent**
- **Classify events cheaply, then trigger:** Stream live events into a cheap classifier model (the demo uses Jev) that detects incidents and triggers an agent with the issue payload, location, and error. The demo reports hundreds of events classified for pennies, which makes always-on watching affordable.
- **Encode the on-call SOP:** Give the agent the conventional sequence: detect, investigate, find root cause, fix, present for review, deploy. Equip it with tools to update the incident, read logs, and query previous events.
- **Review before shipping:** Ask the agent for an issue summary and code diff before approving, even when it says it is ready. In the demo a checkout API applying loyalty discounts and taking 100% of traffic failed on a bad null check; avoid a bang/non-null assertion and prefer null coalescing or an explicit safe `if`.
- **Make deploys run once:** Treat production deployment as a safe, non-replayable operation that can be called only once, so a resumed or retried agent never double-deploys.
- **Simplify the template when you can:** Skip the classifier and string-check status, or inspect only 4xx and 5xx errors.

**3. Give agents compute, context, and shared state**
- **Dedicate a machine or sandbox:** Run agents on their own device (he uses an M6 Mac Mini exclusively for agents) or cloud sandboxes like exe.dev. Agents need the same tools as you, potentially a whole computer, to work end to end with high autonomy.
- **Let compaction run in the background:** Pi Durable forks and compacts the session in the background, and crossing a reserve threshold stops the agent. Tune those thresholds so multiple background activities keep running.
- **Share durable application state:** Use the `read state` and `update state` tools to keep one shared JSON object across every agent session on a device. Many agents can then debug one issue together, and updates can also render a UI for humans.
- **Organize by device, workspace, agent:** Use this hierarchy so any device can connect to any agent.

**4. Run durable tasks with a human near the loop**
- **Package repeatable jobs as tasks:** Tasks are durable jobs made of raw code or code plus agents, such as a workspace snapshot that saves its result to application state, or a "change watch" that sets a folder baseline and loops until stopped manually.
- **Split long work into phases:** Engineering work naturally falls into chunks, phases, and steps, so build tasks with phases you can rerun individually when one fails. Model incident response this way too: find, approve, then run tests and update state.
- **Ask for approval, not presence:** In a release check, have a subagent request human approval instead of keeping you continuously in the loop. Observe workflows and intervene only when needed, keeping shipping control through approvals and some review.
- **Track job status:** Have the agent list durable jobs and check one, showing states like completed, aborted, and last phase.
- **Test the survival claim yourself:** Close the laptop, refresh, kill the process, or restart the machine and confirm agents return from their last checkpoint.

**5. Detach agents from any one client**
- **Treat UIs as clients:** Keep agents in sandboxes and connect via browser, terminal UI, custom CLI, `curl`, raw authenticated HTTP, mobile, or product interfaces; some background agents need no interface.
- **Attach from the terminal:** List durable-agent-network IDs, pick a sandbox, start a terminal UI, and attach with the agent ID. Sessions created in one client (like `T002`) appear in the others instantly.
- **Go multiplayer:** Let coworkers connect to the same incident agent to review logs and prompt it together.
- **Set session policies for products:** For a front-end support chatbot, let returning users resume their session and clear it after 6 hours or another chosen policy.

**6. Control tools, safety, and branching live**
- **Reconfigure mid-session:** Switch an agent to read-only mode from one client and its tool set changes for every client while it runs; other configuration can change live too. Every model call and tool execution is its own task.
- **Use `handoff` for fresh context:** Start a new model context carrying a handoff when the current one is cluttered.
- **Gate Bash with an extension:** Pi extensions apply to Pi Durable. A damage-control extension judges every Bash call and blocks irreversible commands like `rm -rf`; it can be turned off, so keep it on for autonomous agents.
- **Shape behavior with a system-prompt extension:** Define read-only tools, communication rules, operational boundaries, and aliases, for example an alias that condenses responses.
- **`fork` to explore:** Fork an agent to try a different direction while keeping useful context; forks can retain state, start fresh, or branch from any point in time.

**7. Adopt and measure**
- **Default to durable for product work:** Build proactive agents that start before you appear and then request approval, moving from in-the-loop toward out-of-loop work ("stay out the loop").
- **Measure agents working unprompted:** Track the number of agents doing useful work at any moment that started without a human kickoff and are embedded in your work fabric.
- **Invest in planning and review:** These are the two constraints of agentic coding; attack them with prompt, context, and harness engineering, and spend your own effort deciding what is valuable to build.

**Try this first:** Put one Pi Durable agent on a dedicated machine or sandbox, attach to it from two clients, then kill the process and confirm it resumes from its last checkpoint.

**Caveat:** Pi Durable is experimental; the creator will not deploy it to production without forking and maintaining it while awaiting a stable V1, and the demo cost figures are unverified.

## Derived summary
## Source framing [00:00:00]
- [00:00:00] Indie Dev Dan introduces a discussion of Pi Durable, described as a release by Pi coding-agent creators/maintainers Mario and Armen.
- [00:00:15] The speaker defines the claimed goal as persistence of ongoing work, conversations, and application state across failures, clients, and change.
- [00:00:26] The speaker says he has durable agents running on M4 and M6 Mac Minis, an M5 MacBook Pro, and exe.dev cloud sandboxes.
- [00:00:38] The video asks why durability matters beyond an agent’s ordinary `/resume` capability.
- [00:00:56] The speaker claims Anthropic and OpenAI use durable-agent primitives for multi-client products, naming “Dots and Claw through Slack”; this attribution is not independently verified.
- [00:01:19] The speaker’s thesis is that engineers should own their agent, harness, and durable-agent infrastructure rather than merely rent intelligence.

## Durable-agent incident-response example [00:01:52]
- [00:01:52] The speaker shifts from Pi Durable specifically to the broader concept of durable agents.
- [00:02:06] Pi Durable is described as making the Pi coding agent persistent across failure, plus other capabilities.
- [00:02:14] A demo notification says a “red team” found a production issue and fix and is awaiting review.
- [00:02:29] In the demo market application, live events stream in; a “Jev classifier model” detects an incident and triggers an agent.
- [00:02:39] The triggered agent receives the issue payload, location, and error, then opens an incident response.
- [00:02:47] The speaker maps the workflow to a conventional on-call sequence: detect, investigate, find root cause, fix, present for review, then deploy.
- [00:03:00] The agent is already ready for review after Jev triggered it to investigate.
- [00:03:08] The speaker calls this a proactive agent because it works without waiting for a human, then waits for review.
- [00:03:16] Its displayed standard operating procedure is detect, investigate, and root-cause analysis; shown tool calls include updating the incident, reading logs, and querying previous events.
- [00:03:29] Although the demo agent is ready to deploy, the speaker initially declines so he can understand the issue before shipping.
- [00:03:39] Refreshing the interface preserves state, which the speaker presents as the defining durability behavior.
- [00:03:46] The speaker requests an issue summary and code diff to assess what the agent proposes for production.
- [00:03:57] The demonstrated failure affects a checkout API that applies loyalty discounts and receives 100% of traffic, making it a serious incident in the demo.
- [00:04:06] The stated root cause is a bad null check involving customer loyalty. The speaker advises against a bang/non-null assertion and favors null coalescing or an explicit safe `if` statement.
- [00:04:23] After recognizing the issue as familiar, the speaker judges the agent’s fix sufficient and approves deployment.
- [00:04:38] The speaker says Pi Durable makes the production deployment a safe, non-replayable operation that can be called only once.
- [00:04:50] The demo displays production stabilizing. The speaker says Jev classified incoming events for 1.5 pennies after hundreds of events, and says the incident was fixed agentically; these cost and performance claims are not independently verified.
- [00:05:14] The agent is described as detached from any one user interface, so any engineer can interact with it through one or more clients.
- [00:05:31] The speaker predicts that most future agents will be proactive and argues that the most valuable agent is one that does not need a human in order to ship. This is a prediction and opinion.

## Sessions, context, and shared durable state [00:06:03]
- [00:06:03] The network playground sidebar purportedly shows agents across exe.dev sandboxes, M6 and M4 Macs, and an M5 MacBook Pro.
- [00:06:19] The core interface is organized into Session, State, Tasks, Tools, and Extend tabs.
- [00:06:37] In the session demo, a ping launches an agent on the speaker’s M6 device; he says it runs “Claude Sonnet 5.5.”
- [00:06:53] Pi Durable is said to compact context in the background.
- [00:07:05] The described compaction mechanism forks a session and compacts it; crossing a reserve threshold stops the agent. The speaker says these thresholds can be adjusted.
- [00:07:17] The rationale offered is that durable agents can keep multiple background activities running around a product or tool.
- [00:07:32] The speaker uses an M6 exclusively for agents and recommends dedicated compute or sandboxing so agents can operate end to end.
- [00:07:44] His stated principle is that agents need the same tools as the engineer, potentially including an entire computer.
- [00:08:01] The state object has `read state` and `update state` tools and is described as persistent application state for a Pi Durable agent.
- [00:08:13] The speaker says other ongoing durable-agent sessions on the same M6 can access this application state.
- [00:08:28] Updating the app state renders a UI, but the speaker emphasizes that the state is also for agents rather than only human display.
- [00:08:43] A second agent in the same session/device reads and outputs the same key-value state.
- [00:08:59] The speaker characterizes this as one shared JSON object across every agent session on a device, enabling many agents to debug a single issue through shared state.
- [00:09:14] He argues that durable agents require durable application state, not just resilience to downtime and change; multiple agents can share and update it.

## Durable tasks and phased workflows [00:09:44]
- [00:09:48] Tasks are presented as repeatable durable jobs that agents can run, consisting either of raw code or code plus agents.
- [00:10:03] A workspace-snapshot task performs arbitrary work and saves its result to application state.
- [00:10:24] The speaker says tasks should be able to do whatever is needed, and says phases allow rerunning a particular phase when it fails.
- [00:10:40] Long-duration engineering work is presented as a motivating use case for multi-step durable tasks.
- [00:10:44] In a release-check example, a subagent must ask for human approval instead of requiring the human to remain continuously in the loop.
- [00:10:57] The speaker labels this operating model “human near the loop”: observe processes and agentic workflows, then intervene only when needed.
- [00:11:09] The incident workflow illustrates this model: the agent finds and resolves an issue, and a human later approves or declines it.
- [00:11:17] After approval, the agent can run tests and update app state. The speaker connects this to engineering work being naturally organized into chunks, phases, and steps.
- [00:11:34] A task can contain a subagent, and the workflow can be continued if something goes wrong.
- [00:11:44] A “change watch” task establishes a folder baseline and loops while watching it; execution can be stopped manually.
- [00:12:00] The agent can list durable-job statuses, with displayed examples including completed, aborted, and last phase.
- [00:12:13] The speaker frames control of agent technology as a strategic issue, asserting that outsourcing durable-agent infrastructure risks dependence on technology that others can change. This is the speaker’s opinion.
- [00:13:35] He suggests viewing incident response as a sequence of task phases, while noting the shown incident demo was not designed that way.
- [00:13:48] **Aside, demo economics:** the speaker says the mock product processed hundreds of mock stream events for 6 cents and praises Jev’s reliability, spend, speed, and decision time. These claims are not independently verified.

## Detached agents and multi-client access [00:14:20]
- [00:14:27] The speaker says he has a network of durable agents working on different codebases and problems, reading incoming log streams proactively.
- [00:14:46] The central architectural claim is that multiple clients can connect to a detached agent rather than running the agent on the user’s current device.
- [00:15:20] In a terminal example, he lists durable-agent-network IDs, chooses an exe.dev cloud sandbox, starts a terminal UI, and attaches using an agent ID.
- [00:15:56] The attached terminal displays the same agent sessions as another interface, which the speaker uses to demonstrate that agents are disconnected from a particular UI.
- [00:16:09] Customer support is offered as an application example: run an agent on a website while observing it through a terminal UI, browser app, or durable-agent network application.
- [00:16:40] Creating a session named `T002` in one interface simultaneously creates it in the browser, according to the demo.
- [00:16:51] The speaker states that the UI elements are clients, while the actual agents reside in cloud sandboxes where they are isolated and operate with high autonomy.
- [00:17:05] The agent hierarchy is described as device → workspace → agent, with any device able to connect.
- [00:17:24] The speaker says a phone-connected product agent is a use case for durable agents, contrasting it with a standalone, stuck session such as default Pi, Claude Code, or Codex.

## Tools, live reconfiguration, and safety controls [00:17:53]
- [00:17:53] Listing tools reveals subagent context search, durable-job checks, application-state access, and standard agent tools.
- [00:18:06] The speaker says every tool call and harness execution, from calling a model to executing a tool, is represented as its own task.
- [00:18:25] He changes the agent to read-only mode in one client, changing the tools available to the shared agent mid-session.
- [00:18:38] The agent responds as though its prior tool list was incorrect, illustrating that the available tool set changed during execution.
- [00:18:55] The claimed implication is that an operator can change not only tools but other durable-agent configuration while the agent is live.
- [00:19:17] Named tools include listing durable jobs, checking a durable job, and `handoff`, which starts a fresh model context with a handoff.
- [00:19:32] The speaker combines configurable/restartable phased tasks, device-scoped shared state, cloud-sandbox-specific state, and background auto-compaction as the feature stack behind his preference for Pi Durable over a classic terminal session.

## Extensions and branching [00:20:16]
- [00:20:16] Pi is described as extendable via extensions, and those extensions are said to apply to Pi Durable.
- [00:20:33] The demo uses a “fix smartass opus” extension, described as system-prompt engineering for verbose/load-bearing agents, and a “Jev damage control” extension.
- [00:21:15] When Jev damage control is enabled, the speaker says every Bash tool call is judged for legitimacy.
- [00:21:22] The agent describes its enabled system prompt as having five parts: read-only tools, communication, operational boundaries, and aliases, with the transcript listing “five parts” but only four named categories.
- [00:21:36] An alias created in the system prompt is invoked to condense the agent’s response.
- [00:21:46] In the demo, `rm -rf` is blocked because deletion is irreversible.
- [00:22:04] The speaker says dangerous mode, safety controls, and the system prompt can be turned off; after doing so and reissuing the delete command, it executes.
- [00:22:28] The `fork` command creates a forked agent and supports trying a different direction while preserving useful accumulated context.
- [00:23:03] Forking can retain state, start a fresh conversation, or be launched at any point in time.
- [00:23:15] The speaker’s operational model is to put agents on their own devices, isolate them for autonomy, give them comparable tools to the engineer, and build repeatable, resumable harness workflows around them.

## Engineering judgment and release caveat [00:23:58]
- [00:23:58] A new cart-API anomaly appears in the proactive-agent demo.
- [00:24:03] The speaker urges building proactive agents and praises the Pi Durable creators’ engineering judgment.
- [00:24:46] He distinguishes coding from software engineering: his claim is that the harder work is deciding what is valuable to build and stripping a product down to what expertise identifies as essential.
- [00:25:25] Important caveat: the speaker says Pi Durable is currently experimental and that he will not deploy it to production without forking and maintaining it; he is awaiting a stable V1 release.

## Claimed reasons to use durable agents [00:25:39]
- [00:25:39] The first claimed reason is proactive operation: agents start work before a human arrives, leaving the human to review rather than initiate every task.
- [00:26:10] The speaker calls this direction “zero touch engineering,” where work is completed and the human primarily reviews how it was done, while occasionally fixing agent-caused issues. This is an aspirational framing.
- [00:26:32] He identifies proactive, out-of-loop agents as a way to deploy work that operates without continuous human involvement.
- [00:26:44] The speaker says that nearly an hour of log categorization in the demo cost 13 cents and triggered an incident-response workflow; this cost and capability claim is not independently verified.
- [00:27:01] He argues that investing in agent harnesses and controllable, open-source, extensible tooling can remove work from the human incident responder. This is the speaker’s view.
- [00:27:18] **Aside, promotional/self-attribution:** the speaker says he is not sponsored and does not accept channel sponsorships, while promoting his own products for mid-to-senior engineers.
- [00:27:41] His stated chain is: control the agent through an agent harness, preferably one the engineer controls; Pi Durable then enables proactive work to be nearly complete by the time the person arrives.
- [00:28:01] The speaker says planning and reviewing are the two constraints of agentic coding and claims both are solvable through agentic engineering, prompt/context/harness engineering. This claim is not independently verified.

## Multi-client, multiplayer, long-running, and human-near-the-loop [00:29:02]
- [00:29:02] The speaker presents multi-client agents as a single agent API accessible through browser, custom CLI, and `curl`.
- [00:29:34] Additional named client surfaces are raw authenticated HTTP requests, mobile devices, and product interfaces; some background engineering agents may require no interface.
- [00:30:00] “Multiplayer agents” means coworkers can connect to the same incident agent, jointly review logs, and jointly prompt it.
- [00:30:19] The speaker personally prioritizes long-running agents over multiplayer access.
- [00:30:24] He claims that closing a laptop, refreshing, killing a process, or restarting a machine does not stop the durable agents permanently: they return from their last checkpoint. He recommends testing this behavior.
- [00:30:57] “Human near the loop” is presented as an intermediate step for engineers moving from manually operating a terminal-bound agent toward more out-of-loop operation.
- [00:31:15] In this model, people retain shipping control by approving workflows and deployments and performing some review.
- [00:31:24] The speaker’s final list of durable-agent reasons is proactive agents, multi-client agents, multiplayer agents, long-running agents, and human-near-the-loop workflows.

## Adoption claims, template caveats, and recap [00:31:32]
- [00:31:32] The speaker says he plans to use durable agents by default for product work.
- [00:31:43] His concrete product example is a front-end support chatbot: a returning user could resume an existing session, while the operator could clear that session after 6 hours or use another chosen policy.
- [00:31:57] He says he is investing heavily in proactive agents that begin work before he appears and then request approval.
- [00:32:17] The source’s central operational maxim is “stay out the loop”: more autonomous work by agents means more agentic engineering rather than merely agentic coding.
- [00:32:54] The speaker says the network demo requires users to set up their own devices and asserts documentation will make this straightforward.
- [00:33:12] He frames the proactive incident demo as a concrete use case for customers and engineering organizations.
- [00:33:23] The demo dashboard reportedly shows 6,000 rows processed for 16 cents by Jev classifying log-stream events. This is a source claim, not independently verified.
- [00:33:31] The speaker says the template can be simplified by string-checking status and skipping the classifier, or by inspecting only 4xx and 5xx errors.
- [00:33:43] He calls the demo only a beginning/template and predicts proactive, out-of-loop agents will become normal. This is a prediction.
- [00:34:08] The recommended KPI is the number of agents doing useful work at any point, specifically agents that start without a human kickoff and are embedded in the work fabric.
- [00:34:30] Final recap: the speaker says durable agents increase the number of agents that can work in-loop, out-of-loop, and near-the-loop.
- [00:34:39] He predicts that the key transition at the end of 2026 and in 2027 will be from in-the-loop to out-of-the-loop work. This is a prediction.
- [00:34:56] The closing directs viewers to the Pi Durable demo and credits Mario, Armen, and viewers.

## Evidence anchors
- [00:00:00.080] What's up engineers? Indie Dev Dan here.
- [00:00:15.839] durable. Pi durable persists your
- [00:00:38.879] have to ask the question, what is a
- [00:00:56.879] Entropic and OpenAI are using durable
- [00:01:19.840] We must own our agents, our agent

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
