# Is Hermes Bot Mode Worth It? 🧠 My Best Practices (So Far)

## Source
- Original: https://www.youtube.com/watch?v=3RoK0rrOHCA
- Type: youtube
- Creator: {'displayName': 'Wanderloots'}
- Published: 2026-09-06T00:00:00.000Z

## Tags
Hermes, multi-agent systems, agent orchestration, bot mode, research workflow, tool permissions, agent memory, human-in-the-loop, LLM wiki, local models

## Derived summary
## [00:00:00] Purpose and framing
- [00:00:00] Callum, also known as Waterloots, introduces a test of Hermes "bot mode," a feature in which specialist agents can communicate and coordinate work rather than requiring the user to manually pass work among separate chats.
- [00:00:35] The stated learning goals are to create specialist bots, assign only necessary capabilities, configure efficiency-related settings, and combine bots in a shared conversation for a research experiment.
- [00:00:53] The demonstrated team consists of an orchestrator, a researcher, and an existing librarian, though the presenter says the approach can apply to specialist workflows such as coding, writing, and finance.

## [00:01:15] Team model, specialization, and efficiency
- [00:01:15] The presenter analogizes each bot to a specialist with its own workstation: its profile contains instructions, model, tools, skills, and memory.
- [00:01:23] Rather than supplying one universal bot with every capability, work can be distributed to agents that each do what they do best and coordinate with one another.
- [00:01:31] Removing unnecessary capabilities is presented as an efficiency measure because excess capabilities can lead to extra tool calls, longer runs, more tokens, and greater quota or budget consumption.
- [00:01:44] In the example workflow, the orchestrator coordinates, the researcher investigates, and the librarian organizes approved knowledge; reports can return for revision and the human decides when to proceed.
- [00:01:59] The experiment asks whether delegating specific jobs and capabilities to specialist agents, then coordinating them in one team, improves the presenter's workflow and efficiency.

## [00:02:24] Bot mode versus standard sessions
- [00:02:24] Standard Hermes sessions are ordinary conversations stored under projects and profiles.
- [00:02:37] A bot is described as a Hermes profile rather than a separate primitive to learn.
- [00:02:48] With ordinary profile use, profiles can work in parallel, but the user must manually switch among them to conduct separate chats.
- [00:03:08] In bot mode, each profile has a dedicated bot chat. Opening a bot chat differs from starting a new conventional chat, and the bot chat describes the bot profile's capabilities.
- [00:03:33] Bot mode enables agent-to-agent communication: the user can mention a bot, such as `@librarian`, from another profile to ask it to perform work.
- [00:03:53] Bots can also be placed in group chats, allowing specialized individual agents to communicate as a team rather than functioning as one universal agent.

## [00:04:29] Creating the orchestrator
- [00:04:29] A newly created bot is a named teammate with its own memory, skills, and chat, and it can message other agents.
- [00:04:39] The creation interface permits generating, uploading, or selecting an avatar; the presenter treats avatar selection as cosmetic customization.
- [00:05:11] The bot's displayed name and its `@` mention name are configured separately: one appears in the interface and the other is used for tagging.
- [00:05:23] The "soul" is described as the bot persona: it defines behavior and communicates the bot's understood capabilities. If left blank, Hermes generates it from the bot's name, title, and description.
- [00:06:04] The orchestrator's requested role is to clarify outcome and acceptance criteria, delegate research, review work for relevance, completeness, citations, uncertainty, and unresolved gaps, request at most one focused revision, and hand accepted work to the librarian only with user approval.
- [00:06:37] The presenter gives the orchestrator access to external memory while limiting the researcher from doing so, intending that only one agent write approved memories.
- [00:06:50] The presenter clones the default configuration, explaining that the profile is configuration while the provider is the connected model, and chooses bundled skills rather than an empty system.
- [00:07:22] Bots may be connected to different devices, such as a laptop and desktop, while passing information between their separate locations.
- [00:07:52] The automatically created orchestrator claims it can clarify outcomes, delegate research, quality-control work, coordinate knowledge, and use tools; the presenter identifies its implied independent research ability as undesirable duplication of the researcher role. This behavior is a source-reported product output, not independently verified.
- [00:08:25] A bot chat is characterized as a canonical, persistent or "forever" chat. In bot mode, `/new` or reset compacts it rather than creating another bot chat; the sessions tab remains available for dedicated work with that profile.

## [00:09:06] Editing role instructions and creating the researcher
- [00:09:06] Hermes generated the orchestrator's `soul.md` from the name and description, and the presenter edits this file to refine the role.
- [00:09:26] The added orchestrator protocol requires it to state outcome, acceptance criteria, owner, deliverable, and stop condition. It is also instructed not to research itself and not to write to the LLM wiki, preserving delegation and librarian boundaries.
- [00:09:57] After saving `soul.md`, the presenter restarts the gateway and asks the bot to confirm its updated understanding, including delegation, approval gating, and waiting before librarian use.
- [00:10:31] The researcher is configured to investigate current-reality questions using current and original sources, produce cited briefings, report uncertainty, counterevidence, and gaps, return results to the orchestrator, and not write to the wiki.
- [00:11:06] The researcher receives a research protocol requiring research output to be saved under `workspace/research`; its rules specify returning work to the orchestrator rather than sending files directly to the librarian.
- [00:12:06] The presenter labels the remaining dimensions of a bot as its brain, capabilities, continuity or memory, and operations.

## [00:12:19] Brain: model assignment and local models
- [00:12:19] Per-bot settings provide a view of the connected provider, model choice, limits, and default reasoning, which the presenter collectively calls the bot's brain.
- [00:12:55] Hermes is said to support choosing local models per task. Its configurator reportedly checks device specifications and suggests models suitable for the machine's GPU and workflow, including a compatible model file variant. These product capabilities are described by the presenter and are not independently verified.
- [00:13:43] The presenter lowers the researcher's assigned model from "5.6 soul" to "Terra," describing the prior choice as overkill, while suggesting a higher model for the orchestrator and lower models for researcher and librarian.

## [00:14:00] Capabilities: souls, skills, tools, and MCP
- [00:14:00] The presenter distinguishes: a soul defines role and team fit; a skill is a reusable method or workflow; and tools execute operational actions for that workflow.
- [00:14:13] More bots are not necessarily better. Each should have a clear job, responsibilities, and relationship to the wider team.
- [00:14:23] Hermes capabilities include skills, tools, and MCP, with MCP identified as external tools.
- [00:14:31] Although Hermes is said to learn skills over time, the presenter argues agents should not receive every skill and tool. He disables the researcher's LLM wiki skill because that responsibility belongs to the librarian.
- [00:14:58] The researcher retains the grounded-citations skill because it is described as generating footnote-like source tracking through research.
- [00:15:12] Skills are said to be lazy or progressively loaded only when the agent believes they are needed; tools, by contrast, are directly available operations such as writing or reading files and checking a browser.
- [00:15:41] A good bot is characterized as a narrowly scoped agent with capabilities specific to its assigned job, not a generic agent with everything enabled.
- [00:16:02] Usage counters show what bots attempted while inheriting broad defaults, but frequent tool use does not establish that each tool call was necessary.
- [00:16:21] In an earlier test, the researcher attempted sub-agent task delegation six times, which the presenter says added 20 minutes through looping. He warns that some tools can take 10, 15, or 20 minutes and slow the entire workflow.
- [00:16:55] The presenter disables the researcher's task delegation, code execution, session search, and cron jobs, while retaining vision terminal, skills discovery, file work, web search, and browser automation.
- [00:17:24] The presenter also removes web access, sub-agent delegation, browser clicking, and computer use from the orchestrator, while retaining past-conversation search, because its purpose is delegation rather than direct research.
- [00:17:56] MCP stands for Model Context Protocol and is described as a way to connect external tools; the presenter says a later video will cover specialized research tools through MCP.

## [00:18:15] Continuity, memory, and operations
- [00:18:15] The researcher has persistent memory and user profile enabled. The presenter says these correspond to `memory.md` and `user.md` files where the agent can record memories and its understanding of user requests over time.
- [00:18:46] Hindsight is described as a more powerful external memory engine that can connect projects, bots, and users, extract insights, and reference old information. The presenter excludes the researcher from it because the researcher's role is internet research rather than access to all other memories.
- [00:19:16] The presenter cautions against every bot writing to the same memory system because their entries could conflict. In this setup, only the orchestrator receives the external-memory provider and can write to it.
- [00:19:41] For operational isolation, the presenter runs terminal execution backends in Docker, which he says gives each agent an isolated environment for code or browser work and helps protect his computer.
- [00:20:05] The workspace is an agent-accessible working directory. The presenter uses a root workspace but says access can be limited; the shared workspace enables bots to exchange files and ideas while mentioning one another in the group chat.
- [00:20:35] "Keep bots warm" controls how many bots stay running for instant switching. Raising it from three to five uses more RAM or memory but, according to the presenter, significantly improved inter-bot responsiveness in his setup.
- [00:21:09] The bot backend idle timeout is 10 minutes in the shown setup. The presenter suggests increasing it for long-running group chats or sessions so bots stay active as long as needed.

## [00:21:43] Communication modes and group-room limits
- [00:21:43] Individual bot chat is permanent in bot mode and can be compacted with `/new` rather than replaced with a new chat.
- [00:22:02] Bots can directly message each other for one-off tasks and progress updates, but the presenter warns that repeated exchanges can become loops that run for hours and consume a cloud-model quota.
- [00:22:30] Group rooms impose a default turn limit, requiring human input after agents have communicated for a set number of turns. The stated purpose is to prevent infinite inter-agent loops.
- [00:23:04] Kanban is mentioned as a more complex alternative for controlling ownership, revisions, approvals, and loops in complex tasks; the video instead focuses on group chat.
- [00:23:26] A group room shares the conversation but does not share memory, tools, or permissions. Each bot remains a separate profile, while the group combines the specialists' capabilities through communication.
- [00:23:50] The presenter creates a group named "research team limited tools" containing researcher, orchestrator, and librarian, with deliberately reduced tool access for the test.
- [00:24:04] In a simple color test, researcher reports deep blue, orchestrator reports emerald green, and librarian reports sunset orange; the orchestrator tracks and summarizes all three. The presenter observes that the limited-tool configuration appeared faster than an earlier run. This is an anecdotal test observation, not independently verified.
- [00:24:49] In the activity log, bots can decide they need take no further action, pause after the turn settles, and wait for user review; the orchestrator then reports the result to the user.

## [00:25:43] Research experiment workflow
- [00:25:43] The user asks the orchestrator for a report on "state-of-the-art 2026" practices for multi-agent teams across disciplines, with a maximum of 10 sources, fewer than 500 words, and tracked citations.
- [00:26:02] The orchestrator translates the request into outcome, acceptance requirements, format, and ownership, assigns the researcher, excludes the librarian initially, and states it will request at most one focused revision before asking whether to save the result.
- [00:26:30] The intended sequence is user → orchestrator → researcher → orchestrator review → at most one researcher quality-revision loop → user approval → LLM wiki ingestion.
- [00:26:45] The presenter notes the task may take minutes, recommends an idle timeout of at least 10 minutes for potentially lengthy research, and explains that the 10-source cap was intended to avoid a run lasting an hour and allowing bots to go idle.
- [00:27:28] The researcher reportedly completes the initial work in 2 minutes, writes a brief in the workspace, produces a 500-word summary with a source ledger, and uses six sources, under the requested 10-source cap. This is a source-reported experimental result, not independently verified.
- [00:28:01] The orchestrator asks to read the file so it can validate constraints such as word count; the presenter illustrates a possible failure case of a 2,000-line document despite the requested limit.
- [00:28:19] The orchestrator's review finds that the evidence base is vendor-authored and lacks a 2026 study, then requests one focused revision using the three remaining source slots.
- [00:28:34] The group reaches its round-message cap during back-and-forth revision. The presenter identifies this as both a safeguard and a drawback, speculates controllability may be added in the future, and suggests direct messaging might have been better for this case.
- [00:28:55] The user explicitly tells the researcher to continue, demonstrating human control over whether the workflow continues or ends. The presenter says the request for a 2026 study follows from the original state-of-the-art-2026 quality requirement.
- [00:29:30] After revision, the presenter reports nine sources and additional content including a 2025 item. He then states a takeaway that multi-agent advantages diminish as the underlying base model becomes stronger. This is his interpretation, not independently verified.
- [00:29:59] The orchestrator accepts the revision, says uncertainty is closed, and requests the user's approval or rejection before handing the report to the librarian for durable storage.

## [00:30:11] Librarian approval and knowledge capture
- [00:30:11] Upon user approval, the orchestrator moves the report into the library raw inbox and asks the librarian to run the LLM wiki review skill.
- [00:30:37] The presenter says the moved report includes source ledgers and inline citations generated through the grounded-citation skill, but it is initially only a report outside the connected wiki.
- [00:30:59] The librarian proposes adding a "multi-agent workflows" note based on the report and asks the user to approve, reject, revise, or defer.
- [00:31:27] After approval, the presenter observes a new Obsidian note connected to agentic memory, Hermes agent, and LLM wiki, with an inline reference to the research brief and related concepts. This is an observed demonstration result, not independently verified.

## [00:32:02] Post-run learning and recap
- [00:32:02] The presenter concludes the group chat completed the intended pipeline: orchestrator delegated research, identified inadequate initial work, required improvement, then passed approved work to the librarian for wiki ingestion.
- [00:32:30] An optional `refine` command is described as reviewing a chat and saving needed information to its own skills and memories. Instead, the presenter asks all bots to update their memories with session learning.
- [00:32:50] The orchestrator records where raw reports should be stored before librarian handoff, which the presenter says removes a future instruction step. The researcher also updates its memory, while the librarian identifies nothing to add.
- [00:33:43] Final assessment: bot mode has potential but needs work and refinement. For this particular research flow, the presenter believes one highly capable agent might perform as well as or better than the team.
- [00:34:00] The proposed path to improvement is iterative: refine instructions, tool access, skill choices, and memories; assign repeatable tasks to specialist bots; test and recalibrate until results meet the user's standard.
- [00:34:09] The presenter predicts that local models can handle much of the work while a stronger cloud orchestrator maintains quality and reduces cost, but this is presented as potential rather than a verified outcome.
- [00:34:35] The next video is announced as an effort to refine the research agent.

### Aside: promotion [00:02:11, 00:34:40]
- [00:02:11] The presenter mentions a free Patreon setup article and later invites support through YouTube or Patreon memberships; these promotional details are not part of the educational workflow.

## Practical applications
- Suggestion: Define distinct roles for a multi-agent workflow, such as coordinator, researcher, and knowledge curator, with explicit handoff and approval conditions.
- Suggestion: Limit each agent's tools, skills, external-memory access, and model tier to its role; review tool-use logs for unnecessary calls or loops.
- Suggestion: Use a group-room turn cap when human review is desirable, and use direct bot-to-bot messaging for bounded one-off work where a group cap could interrupt revision.
- Suggestion: Require the coordinator to state outcome, acceptance criteria, owner, deliverable, and stop condition before delegating a task.
- Suggestion: Use a shared workspace with designated folders for research outputs and require a human approval step before durable knowledge-base ingestion.
- Suggestion: Test whether a single capable model outperforms a multi-agent design for a given repeatable task before investing in further team refinement.

## Evidence anchors
- [00:00:00.080] I'm going to tag the orchestrator.
- [00:00:18.560] coordinate the work? Hermes has a new
- [00:00:35.920] Assembling teams of agents and bottobot
- [00:00:53.199] experiment I'm going through today
- [00:01:15.760] You can think of each bot as a

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
