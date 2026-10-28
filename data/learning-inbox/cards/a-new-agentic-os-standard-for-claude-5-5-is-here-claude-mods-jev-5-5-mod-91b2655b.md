# A NEW Agentic OS Standard for Claude 5.5 is here (Claude Mods, Jev, 5.5 Models)

## Source
- Original: https://www.youtube.com/watch?v=s_1GPN-NXA0
- Type: youtube
- Creator: {'displayName': 'Jay E | RoboNuggets'}
- Published: 2026-10-20T00:00:00.000Z

## Tags
agentic operating system, Claude, AI agents, skills, routines, memory, apps, model routing, prompt cache, workflow automation, micro-apps, Chrome extensions

## Learning guide
**The arc**
The creator starts from a growing personal agentic operating system where files, contacts and tasks pile up and become slow and costly for Claude to handle. The central idea is ARMS: organize the system as **Apps, Routines, Memory, Skills**, each improved across three levels. The guide moves bottom-up from skills to apps, ending with a system built on searchable workspace maps, measured token use, feedback-driven improvement and task-specific interfaces.

**1. Skills: choose the right type**
- **Build database skills for reused knowledge:** A skill can hold knowledge instead of SOP steps, like `/tone` with voice principles, examples and guidelines so agents draft emails and posts consistently. Create one whenever you repeatedly produce or reference the same output type during the week. It also works for non-text assets, like `/thumb` storing file paths to published and inspirational thumbnails.
- **Add wildcards to avoid overfitting:** A fixed reference set makes the agent imitate it and suppress fresh ideas. Make wildcards a default: for 10 article titles, generate eight from references and two without them, and add good wildcard results back as new references. Define a short `/wildcard` skill so every skill means the same thing when requesting wildcards.
- **Use artifact skills for non-chat outputs:** Infographics, slide decks and PDFs fit poorly in chat, so create them as HTML, which agents handle well, then export to PDF. Connect the skill to an HTML brand book with colors and fonts for consistency, as `/robo` does as a design system.
- **Keep an artifact inbox:** Park finished artifacts in one searchable place and search it yourself. This avoids spending tokens asking the model to find an old client deck.
- **Create self-triggered skills:** Some skills should run outside chat, like `/cleanup` launched when leftover temporary files slow the computer. Trigger Claude with a background prompt (Claude-P), pick model and effort level at launch, and have it return a simple report of fixes.

**2. Skills: route and improve**
- **Route each skill to the right model:** Do not leave frequent skills on large, expensive models. Send `/grammar`, which only checks spelling, to Haiku for speed and cost, or use a fast classifier model like Jev to decide which model gets each prompt.
- **Watch a usage dashboard:** Track most-used and highest-spending skills so you can inspect costly ones, like `/animate` which produces many videos.
- **Make high-use skills self-improving:** In a review tool, pin comments on clips with timestamp and location, copy all comments to Claude, and toggle an instruction that the feedback must update `/cut` and `/animate`. Every review then improves the skill, a simple form of reinforcement learning.

**3. Routines: scheduled work**
- **Prefer passive routines where possible:** Active routines produce output to review, like a daily inbox digest sent to Telegram; passive ones alert only on findings, like a weekly brand watch for unapproved use of your brand. Fifty active routines means fifty reviews, so make domain scouting, old-file clearing and slow-app flagging passive.
- **Monitor and cap routine costs:** Every scheduled task uses plan usage or API credits. Sort routines by weekly token use, then ask Claude to optimize an expensive one and set a cap, like cutting a $10 per week routine to $4 by removing unnecessary work.
- **Let a routine propose routines:** The best candidates are jobs you already do manually without noticing. Run a Friday-morning routine that reviews your sessions, lists repeated jobs as routine ideas in a local micro-app, then before usage resets add good ones to a cart and send the selection to Claude to apply.

**4. Memory: long-term maps**
- **Judge memory by retrieval speed and cost:** Your second brain is just your workspace files; at around 420,000 files, retrieval structure becomes necessary. A visual graph is optional; the shared principle is giving Claude a map of the whole workspace.
- **Use `memory.md` as a card catalog:** Claude maintains short remembered items and loads them every chat, so it consults the map before searching the shelves.
- **Turn `Claude.md` into a router:** Instead of only rules, make it route to departmental files like `business.md`, which route further into subfolders. Put core rules in one central `agents.md` that Claude Code and other AI tools read.
- **Stick to plain text routing:** Plain-text maps work without vector embeddings or RAG databases. Add metadata for visual assets, and let database skills act as routers to current client info and dashboards.

**5. Memory: short-term context and cache**
- **Compact with a purpose:** Full chats suffer context rot and get costlier because the whole window is reread. When compacting, state what must survive, such as business decisions or created templates.
- **Keep the prompt cache warm:** A warm cache makes rereading cost a fraction of normal; after about an hour idle it goes cold, and a chat idle 11.5 hours may need to recache about 600,000 tokens (roughly $5 on Opus). Use a mod that shows cache status without spending tokens, and have sessions self-ping hourly for four hours to extend the cache to four hours.
- **Treat a second correction as a memory bug:** Use `/note` to log mid-task feedback to a skill-specific file via Haiku without interrupting work, then have Claude apply the backlog before usage resets. Use `/calibrate` to save important feedback, link it to related memories and update the skill, and let a suggestions app propose memory improvements.

**6. Apps: connections and interfaces**
- **Pick light integrations:** Use `/search connectors` to find options in this order: official connector, open-source CLI, API, community MCP. CLIs are lightest, APIs return lengthy responses Claude must read, and MCPs load all capabilities each new chat, so keep MCP use light.
- **Mod your daily tools:** Add a usage-bar mod showing weekly and five-hour limits plus cache info. Extend the idea to Chrome with a `/chromify` skill of extension practices, building tools like one that captures a component's code for Claude to reverse-engineer or saves YouTube titles and thumbnails into a database skill.
- **Load extensions locally:** Local extension code uses no tokens; enable Chrome Developer Mode and load the extension from your computer.
- **Move recurring heavy work into micro-apps:** When chat is no longer efficient, build local apps, like a clip review editor, a carousel review app, or a Generations app connected to image and video models.
- **Build a reusable UI component library:** Keep pre-built components in a skill like `/robo` so Claude does not recreate them and team-made interfaces stay consistent and cheaper.

**Try this first:** Rewrite your `Claude.md` as a map that routes to one departmental file such as `business.md`, and move shared rules into `agents.md`.

**Caveat:** The Claude 5.5 model, 1 million-token window, cache timings and dollar savings are the creator's unverified claims, so measure your own costs before relying on them.

## Derived summary
## Source note
- [00:00:00] The presenter describes a personal "agentic operating system" built mainly with claimed Claude 5.5 models, while saying the architecture could run on other models. Product capabilities, performance figures, and the presenter's results are source claims and are not independently verified.

## [00:01:26] Operating-system dashboard and ARMS framework
- [00:01:26] The home dashboard provides access to custom micro-apps for agent-assisted work, including a content system that generates and displays images and videos.
- [00:01:42] An Instagram carousel app holds posts for review and approval; a recommendation app tables system improvements for possible end-of-week application if usage remains.
- [00:01:55] The dashboard also shows upcoming calendar items, scheduled routines, emails Claude flags for attention or reply, and on-demand skills with selectable model and effort settings.
- [00:02:10] Completed artifacts are parked in a searchable location, allowing retrieval of a prior client deck without asking the model and consuming tokens.
- [00:02:25] The presenter calls the workspace files a "second brain," saying it contains about 400,000 files at this point; a graph view represents files as interconnected nodes to help the agent locate material.
- [00:02:58] Timeline, routines, skills, and connected-app views expose recently edited items, weekly scheduled tasks, high-token consumers, and unused integrations that may be retired.
- [00:04:04] The presenter frames the core design issue as organizing contacts and workspace, and introduces ARMS: **Apps, Routines, Memory, Skills**.
- [00:04:29] The planned learning order is bottom-up, covering each ARMS layer at three updated levels.

## [00:05:12] Skills, level 1: choose skill types deliberately
### Database skills
- [00:05:12] Skills are defined as saved instructions Claude follows when called. The presenter distinguishes database skills from ordinary SOP-like skills with explicit process steps.
- [00:05:43] A database skill can instead hold reusable knowledge. The example `/tone` contains principles, examples, and guidelines for the presenter's writing voice, so agents can draft emails and community posts consistently.
- [00:06:16] Database skills can cover non-text assets. The example `/thumb` stores references and file paths for published and inspirational thumbnails, with a separate artifact for visually reviewing the latest references.
- [00:06:44] The stated rule of thumb is to create a database skill when repeatedly producing or referencing the same output type during the week.
- [00:06:55] The presenter warns about overfitting: giving only a fixed reference corpus can make the agent imitate those references and suppress fresh ideas.
- [00:07:22] Proposed mitigation: make wildcards a default part of a database skill. For 10 article-title ideas, generate eight based on references and two without them.
- [00:07:40] Good wildcard outputs can be added back into the database skill as new style and tone references, creating an expanding reference set.
- [00:07:59] The presenter also uses wildcard animation styles to explore options outside an established technology-focused visual style, then selects useful novel ideas.
- [00:08:21] A short `/wildcard` skill standardizes what other skills mean when they request wildcard generation.

### Artifact skills
- [00:08:38] Artifact skills address outputs that are poorly suited to a chat window, such as infographics, slide decks, and PDFs.
- [00:08:54] The presenter says many such artifacts can be created via HTML, identifying it as HyperText Markup Language and a format agents handle well.
- [00:09:10] The `/robo` artifact skill is also the presenter's design system. The cited workflow creates PDFs from HTML first, then exports them to PDF.
- [00:09:25] Consistency is attributed to connecting the skill to an HTML brand book that specifies colors, fonts, and related rules.
- [00:09:51] The presenter recommends an artifact inbox: place generated artifacts there and search it directly, rather than spending tokens asking the model to find older work.

### Self-triggered skills
- [00:10:23] Self-triggered skills are intended to run outside the chat interface. The example `/cleanup` is manually launched when temporary processes or files allegedly left by Claude slow the computer.
- [00:10:51] The OS can offer model and effort-level selection when launching a self-triggered skill.
- [00:11:00] The presenter describes a feature called Claude-P as activating Claude by sending a background prompt without opening chat; the example skill returns a simple report of fixes and output.

## [00:11:26] Skills, level 2: route work to appropriate models
- [00:11:26] Model routing means assigning each skill to the model needed for it, rather than leaving frequently used skills on unnecessarily large and expensive models.
- [00:12:05] Example: `/grammar`, used only for spelling checks, is routed to Haiku for faster and cheaper responses.
- [00:12:16] The presenter characterizes Jev as a fast classification or decision model that can choose which model should receive a prompt.
- [00:12:34] In the presenter's reported workspace results, Jev made 4,451 routing calls in recent weeks, each taking 0.6 seconds; all calls cost $0.18, and about four in 10 were routed to Haiku. These figures are unverified source claims.
- [00:13:18] A usage dashboard should identify most-used and highest-spending skills so costly ones can be inspected and optimized. The presenter cites `/animate` as token-intensive because it produces many videos.

## [00:13:53] Skills, level 3: create self-improving feedback loops
- [00:13:53] The presenter defines a self-improving skill as one that updates from repeated use and feedback.
- [00:14:08] In the Rubric Editor example, the user pins comments on video clips, including timestamp and pin location, then copies all clip comments and sends them to Claude.
- [00:14:37] A toggle can add an instruction that feedback should update `/cut` and `/animate` skills, making every review an opportunity to modify the relevant skills.
- [00:15:06] The stated takeaway is to identify high-use skills and automate their improvement so feedback progressively improves output quality. The presenter analogizes this to a simple version of reinforcement learning.

## [00:15:35] Routines, level 1: distinguish active from passive routines
- [00:15:35] Routines are tasks Claude runs on a schedule. Active routines produce an output for review; passive routines run in the background and notify only when they find something worth flagging.
- [00:15:59] A daily inbox digest that reads emails and sends a Telegram digest is the active-routine example because it produces reviewable output.
- [00:16:12] A weekly "brand watch" checks for websites or domains using the Robo Nuggets brand without approval and alerts only if it finds one, making it passive.
- [00:16:35] The reason to make suitable routines passive is review load: 50 active routines could produce 50 items to review each day or week.
- [00:16:55] Suggested passive-routine candidates include scouting relevant available domains or TLDs, clearing old files, and flagging applications slowing a device.

## [00:17:14] Routines, level 2: monitor and cap recurring costs
- [00:17:14] Every scheduled task consumes plan usage or API credits, so the presenter recommends tracking routine cost as the number of routines grows.
- [00:17:32] The example routines view displays tasks across the week, supports sorting by weekly token use, and shows scheduled times.
- [00:17:54] For an expensive routine, the proposed workflow is to ask Claude to optimize the scheduled task and establish a usage cap.
- [00:18:10] Example cap: reduce a routine allegedly costing 18 million tokens or $10 in API credits per week to $4 per week, cutting unnecessary work from the task.

## [00:18:26] Routines, level 3: let routines propose new routines
- [00:18:26] The presenter argues the best automation candidates are jobs already done manually but not recognized as repetitive.
- [00:18:39] A Friday-morning routine reviews the presenter's sessions, identifies repeatedly performed jobs, and suggests routine ideas in a micro-app called Rubric Records.
- [00:18:58] Before usage resets, the presenter reviews proposed improvements, adds reasonable ones to a cart, then copies the finalized selection to Claude for application to the setup.
- [00:19:17] Rubric Records is described as a browser-based localhost app, meaning it runs on the presenter's computer, and presents routine/task ideas worth automating.

## [00:19:45] Memory, level 1: map long-term workspace memory
- [00:19:45] Memory is defined as what Claude knows about the user and work, plus how quickly and cheaply it retrieves that information. As files accumulate, searching them repeatedly can be slow and consume usage.
- [00:20:05] Long-term memory is everything saved in the workspace. The presenter treats a "second brain" as a label for workspace files and data.
- [00:20:25] A visual workspace map can show connected applications, routines, departmental files, and skills, but the presenter says a visual map is not required for an effective system.
- [00:21:18] The main test for a second-brain system is faster retrieval, cheaper retrieval, or both. The presenter reports a workspace of roughly 420,000 files and says retrieval structure becomes necessary at that scale.
- [00:22:05] The shared principle across the presenter's three memory layers is to provide Claude with a map of the whole workspace.
- [00:22:13] First layer: `memory.md`. The presenter says Claude maintains this by default with short remembered items and loads it at the start of every chat.
- [00:22:37] `memory.md` is compared to a library card catalog: Claude can consult a map before searching individual "shelves" of the workspace.
- [00:23:09] Second layer: `Claude.md`, read at the start of every chat. Rather than making it only a rulebook, the presenter uses it as a map routing work to relevant departmental files.
- [00:23:50] The presenter says Claude Code also reads `agents.md`, allowing one central `agents.md` file to hold core operating rules shared with other AI tools.
- [00:24:03] Departmental routing files, such as `business.md`, can route further into their own subfiles and folders.
- [00:24:24] The presenter says plain-text routing works in this setup without vector embeddings, and attributes a similar preference for plain text over vector embeddings and RAG databases to Boris Cherny and Anthropic. These are source-attributed claims, not independently verified.
- [00:25:02] Third supplementary layer: database skills can act as routers to current business or client information and dashboards when invoked.
- [00:25:38] The summary guidance is to make the second brain searchable through these layers; plain text is said to work well, while metadata is especially useful for searching visual assets.

## [00:26:00] Memory, level 2: manage short-term context and cache costs
- [00:26:00] Short-term memory is what Claude can see in the current chat, technically called the context window or working memory for that conversation.
- [00:26:19] The presenter says Claude 5.5 has a 1 million-token context window, comparing it to approximately the first four Harry Potter books in one chat. This capability claim is unverified.
- [00:26:29] Two stated context problems are context rot, where recall worsens as a chat fills, and repeated rereading of the full window, which makes bloated chats more costly.
- [00:26:53] First mitigation: compact with a purpose. Automatic compaction summarizes the chat near the limit, but the presenter says users should specify what must remain, such as business decisions or created templates.
- [00:27:33] Second mitigation: monitor prompt cache. A warm cache keeps the conversation in short-term memory so rereading costs only a fraction of normal price; after roughly one hour idle, the cache becomes cold.
- [00:27:58] Example: after 11 hours 30 minutes idle, a chat would reportedly need to recache about 600,000 tokens. On Opus, the presenter estimates this at roughly $5 in API credits.
- [00:28:18] The presenter describes a custom mod as an extension-like addition for Claude Code that surfaces cache information without itself consuming tokens.
- [00:28:39] A warm-cache example contains 186K tokens after about nine idle minutes; the presenter estimates it would become cold in approximately another 51 minutes.
- [00:28:59] The proposed technique is to have sessions self-ping hourly for four hours, extending the claimed one-hour cache period to four hours.
- [00:29:14] The presenter reports that analysis of 30 days of chats estimated self-pinging could have saved about $437 at API prices. This is an unverified personal estimate.

## [00:29:41] Memory, level 3: evolve stored instructions and fixes
- [00:29:41] The presenter’s principle is that having to correct Claude twice on the same issue indicates the memory system missed something.
- [00:29:53] First method: maintain a backlog of fixes. The `/note` skill records mid-task feedback to a skill-specific file using Haiku, avoiding interruption of the current task.
- [00:30:16] When ready, or before usage resets, the presenter asks Claude to visit the backlog and apply all recorded fixes.
- [00:30:31] Second method: `/calibrate` explicitly saves important feedback, links it to related memories, and updates the relevant skill rather than relying on Claude’s default automatic memory selection.
- [00:30:52] Third method: use Rubric Records to suggest memory improvements, select useful proposals, and ask Claude to improve that part of the operating system.

## [00:31:12] Apps, level 1: connect tools with attention to integration weight
- [00:31:12] Apps include external applications Claude can reach outside chat and custom applications the user builds.
- [00:31:23] The presenter says an app without an official connector may still be connectable, and uses `/search connectors` to find options rather than manually digging through settings.
- [00:31:51] The connector-search order is: official connector, open-source CLI, API, then community MCP.
- [00:32:14] The stated rationale is that CLIs are lightweight because the model sends a short command and receives the requested answer.
- [00:32:29] APIs are described as heavier because returned responses can contain lengthy details that Claude must read even when much is unnecessary.
- [00:32:51] MCP connectors are characterized as generally heaviest because a new chat loads each MCP’s available capabilities before use; the presenter therefore recommends keeping MCP use light.

## [00:33:11] Apps, level 2: modify frequently used interfaces
- [00:33:11] A mod is defined as a small add-on, analogous to a Chrome extension, that changes how Claude Code looks or works.
- [00:33:31] The presenter's usage-bar mod shows weekly and five-hour limits plus prompt-cache information.
- [00:33:49] The broader claim is that the mod concept can apply beyond Claude Code, particularly to the browser, where the presenter reviews artifacts and runs the browser-based OS dashboard.
- [00:34:26] The `/chromify` skill stores practices for building Chrome extensions.
- [00:34:33] Robo Capture lets the presenter select a website component and collect its underlying code, then give that code to Claude to reverse-engineer the component rather than relying only on a screenshot.
- [00:34:55] Another extension lets the presenter save a YouTube title, thumbnail, or both directly into a database skill for later ideation, without leaving YouTube.
- [00:35:21] The presenter says locally run extension code does not consume tokens and gives operational steps for loading self-built extensions: enable Chrome Developer Mode and load the extension from the computer.

## [00:35:34] Apps, level 3: move recurring high-friction work into micro-apps
- [00:35:34] For recurring, substantial tasks, the presenter recommends reassessing whether chat remains the most efficient interface for working with an agent.
- [00:36:02] Rubric Editor is used to review actual video clips and place comments, which the presenter says is easier than typing direction in chat.
- [00:36:10] An Instagram-carousel micro-app lets the presenter quickly view and review carousels generated by Claude rather than searching through chat.
- [00:36:23] A "Generations" micro-app collects requested images and videos through direct connections to image and video models.
- [00:36:40] The presenter encourages building local applications with Claude, claiming recent models can build them from a few prompts. This is a source claim.
- [00:36:49] For repeated app creation, build a reusable UI-component library. The presenter's `/robo` skill uses pre-built components so Claude need not recreate them and so team-created interfaces remain consistent.
- [00:37:17] The presenter cites Stripe VP of Design Katie Dill as describing a comparable UI-library approach for creating branded materials, with the claimed benefits of cost efficiency and consistent look and feel.

## [00:37:38] Final recap
- [00:37:38] The video concludes that ARMS consists of apps, routines, memory, and skills, with the presented system emphasizing searchable workspace maps, measured token use, feedback-driven improvement, and task-specific interfaces.
- [00:37:42] **Promotional aside:** the presenter says a downloadable guide contains the prompts and resources mentioned in the video.

## Evidence anchors
- [00:01:26.720] Because from this home dashboard I can
- [00:01:42.520] much easier. An Instagram carousel app
- [00:01:55.800] as a home page, so I also see what's
- [00:02:10.119] from here. I also make a lot of
- [00:02:25.680] And finally, if I click through here, it

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
