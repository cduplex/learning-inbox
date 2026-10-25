# Claude 2.0 is Insane (All Updates Explained)

## Source
- Original: https://www.youtube.com/watch?v=J5EbL1UaqG8
- Type: youtube
- Creator: {'displayName': 'Ben AI'}
- Published: 2026-10-25T00:00:00.000Z

## Tags
Claude Code, AI productivity, desktop app, projects, nested sessions, side chats, split view, artifacts, slash commands, mods

## Derived summary
## Overview [00:00:00]
- [00:00:00] The presenter says Anthropic rebuilt the Claude Code desktop app and added projects, threads, mods, side panels, multitasking, and other features.
- [00:00:11] The video’s stated purpose is to demonstrate the new features, explain how to use them, and argue that users of “Code Work” should consider switching to Claude Code.
- [00:00:20] The presenter identifies himself as Ben, a three-time founder who runs an AI agency, an AI second-brain app, and an AI community.
- [00:00:32] **Source-attribution note:** product capabilities, availability, performance effects, and personal results below are claims made by the presenter or attributed to Anthropic, and are not independently verified here.

## Desktop layout and chat organization [00:00:32]
- [00:00:32] The presenter characterizes the Claude Code desktop layout as substantially improved.
- [00:00:37] He says he had previously preferred Code Work’s layout and UI, but now strongly recommends considering the Claude Code tab instead.
- [00:00:46] His stated reasons are an improved layout, a belief that Anthropic launches newer features there first, and the practical value of the new features.
- [00:00:59] He says Claude Code is not only for coders, describing it as essentially the same backend tool as Code Work but with more functionality.
- [00:01:06] The presenter claims Claude Code can work with files on the computer, has CLI access, and includes the newly discussed features.
- [00:01:13] He also argues that the layout now appears less intimidating.
- [00:01:18] The earlier appeal of Code Work’s side panel, according to the presenter, was its visibility into Claude’s to-do list and into connector skills and files used in each chat.
- [00:01:30] He says Claude Code now provides the same information and more.
- [00:01:33] When Claude makes a plan, a to-do list appears in the chat; the user can watch tasks be checked off as work progresses.
- [00:01:42] A set of cards appears beside the chat.
- [00:01:44] The environment card indicates which folder the chat runs in and whether the chat is local or cloud-based.
- [00:01:51] A remote-control switch can move a local chat into the cloud, which the presenter says allows continuation from a phone.
- [00:01:59] The context card shows how full the chat is and which material occupies context-window space.
- [00:02:05] The context card includes a shortcut to compact the chat. The presenter explains compaction as Claude summarizing the chat after it reaches a certain context-token amount, freeing space so the conversation can continue at high performance.
- [00:02:18] Connectors and outputs cards show files the chat made or used.
- [00:02:25] Chats can be organized into category-based sections.
- [00:02:30] To create a section: use the three-dot menu next to a chat, choose **move to new section**, name it, and create it.
- [00:02:37] Existing chats can then be moved into the section by drag and drop.
- [00:02:42] The presenter says this improved his ability to find old chats because he found the prior grouping feature inadequate.

## Projects and nested sessions [00:02:51]
- [00:02:51] The presenter calls Claude Code projects, or nested sessions depending on plan, his favorite new feature.
- [00:02:58] He says rollout is gradual and may look different across accounts.
- [00:03:03] He states that projects are available on Pro and Max, while Team plans display nested sessions instead.
- [00:03:08] The underlying concept is presented as the same: supporting more efficient work on larger projects.
- [00:03:14] One main chat or project can start other chats inside itself, termed nested sessions.
- [00:03:21] The main chat can message nested sessions, inspect their work, and report results to the user.
- [00:03:24] The presenter frames the architecture as one coordinator or orchestrator managing a small team of agents or sessions instead of the user manually managing five chats.
- [00:03:33] His example is YouTube production: separate chats for thumbnails and titles, outline development, and visuals/editing.
- [00:03:47] The rationale is that creating a YouTube video contains multiple distinct tasks.
- [00:03:52] He identifies two problems with prior separate chats: they lacked awareness of changes in other chats, and the user had to keep switching sessions.
- [00:04:06] Conversely, doing every task in one chat allegedly makes it messy, overloads context quickly, and reduces performance.
- [00:04:12] With projects or nested sessions, the user talks to a main coordinator, which can create task-specific threads.
- [00:04:26] The presenter’s example task decomposition is one thread each for thumbnails/titles, outlines, and visuals/editing.
- [00:04:29] He says this enables iteration across tasks from the main chat without overloading the coordinator context, while retaining the ability to iterate inside each individual session.
- [00:04:39] He says the coordinator remains aware of progress across threads, making larger AI tasks more efficient to organize.
- [00:04:49] Threads and sessions can themselves create sub-agents.
- [00:04:56] The presenter distinguishes the hierarchy: projects/nested sessions add a coordinator-orchestrator layer above sub-agents.
- [00:05:04] He says users cannot directly iterate with sub-agents, but can directly iterate with threads or nested sessions.
- [00:05:10] Based on his experience, he recommends this approach for bigger projects.
- [00:05:15] Users with Projects access can start a new project, after which the presenter says threads are automatically created.
- [00:05:22] For Team-plan users without Projects, he says to open a blank chat and ask Claude to work on a larger project; Claude may offer to create threads, or the user can explicitly request them.
- [00:05:35] If an unrelated request arises mid-chat, Claude may offer a new thread. The presenter endorses the habit of one chat per task.
- [00:05:43] Created threads appear in a dropdown beneath the main chat, where the user can enter and continue working with the corresponding agent.
- [00:05:51] Projects and nested sessions differ in memory handling: projects reportedly use shared memory that every thread contributes to and draws from; nested sessions receive a brief and prompt from the main chat.
- [00:06:02] The presenter says project threads can run in the cloud with the laptop closed, while nested sessions run only locally.
- [00:06:10] He predicts that projects will become available to all plans “in a couple of weeks.”

## Aside: presenter promotion [00:06:16]
- [00:06:16] **Promotional aside:** the presenter advertises an AI Accelerator, claiming it includes a 30-day Claude course requiring less than one hour per day, an AI-business course, one-on-one live consulting, and a resource library.

## Side chats [00:06:43]
- [00:06:43] Side chats are introduced as a way to ask questions during a long-running task without interrupting or derailing the main work.
- [00:06:55] To open one, click the three-dot menu in the upper right and select **side chat**.
- [00:07:03] Each side chat opens in its own window, and the presenter says multiple side chats can be opened.
- [00:07:09] A side chat can read the main chat up to its creation point.
- [00:07:11] Suggested uses include asking what Claude is doing, estimating how long it might take, or reviewing work completed so far, without adding material to the main chat.
- [00:07:19] The presenter says side chats can also accommodate questions not fully related to the main task, without putting them in the main context window.
- [00:07:27] He compares them with a prior slash-based temporary side-chat function, but says side chats are persistent and saved.
- [00:07:39] Side chats can send messages to the main chat; his example is using a side chat to review main-chat output.

## Split view / multitasking [00:07:47]
- [00:07:47] Split view is presented as a solution to repeatedly hopping among chats.
- [00:07:54] It allows several chats to be visible on one screen at the same time.
- [00:07:56] One way to activate it is to drag a chat from the sidebar into the current chat and choose the split-view option.
- [00:08:03] Another route is the sidebar chat’s three-dot menu, then **open in**, then **split view**.
- [00:08:08] The presenter’s stated benefit is simultaneous work and multitasking across chats.

## Docs, Slides, Design, Dashboards, Motion, and artifacts [00:08:14]
- [00:08:14] The presenter calls Docs, Slides, Design, Dashboards, and Motion not entirely new but still useful enough to cover.
- [00:08:24] He characterizes these as Claude-native analogues of Google Docs, Google Slides, a design tool, Looker Studio, and a video-creation tool.
- [00:08:32] Outputs are called artifacts, described as editable canvases that support iterative work through comments.
- [00:08:41] Artifacts can reportedly be published as live pages accessible by link for team members or other link holders.
- [00:08:50] Dashboards can reportedly draw from connectors and show live data.
- [00:08:57] The presenter says a dashboard fetches the latest connector data whenever opened, so metrics are current.
- [00:09:02] He describes the Dashboard feature as powerful and says he plans a future full video about it.
- [00:09:06] Slides can create animated presentations and slideshows, which can be downloaded in PPT format or presented from Claude.
- [00:09:15] Claude Docs is described as Google Docs with tabs, supporting real-time collaboration by a team and AI agents; the presenter says he uses it to prepare YouTube videos.
- [00:09:25] Claude Design is described as a Figma-like board or canvas for social-media and website design.
- [00:09:33] The presenter says Design’s canvas lets him change copy, leave comments, and ask Claude to make fixes.
- [00:09:43] Claude Motion is described as a way to make animated videos or motion graphics in code.
- [00:09:50] The presenter says Motion uses code rather than a video model and is therefore cheaper than a video model; he also says its canvas enables quick iteration.

## Slash commands [00:10:08]
- [00:10:08] The presenter says Claude Code has more slash commands than Code Work, another reason he gives for switching.
- [00:10:16] A slash command is defined as a typed shortcut beginning with `/`.

### `/output-style` [00:10:22]
- [00:10:22] The first highlighted command is `/output-style`, used to control the form of Claude’s outputs.
- [00:10:30] The presenter’s team made an output style to keep responses short and simple when Claude becomes too technical.
- [00:10:42] To make a custom style, he says to ask Claude to create one, add it as an output style, then invoke it with the slash command.

### `/doctor` [00:10:51]
- [00:10:51] `/doctor` is presented as a cleanup tool for outdated or unoptimized skills and `Claude.md` files.
- [00:11:00] The presenter says it reads `Claude.md` files, which he calls the first instructions Claude reads in every chat, plus skills and other settings.
- [00:11:06] It reportedly identifies outdated or conflicting instructions that may no longer be relevant for “5.5 models.”
- [00:11:12] In his personal example, `/doctor` analyzed **404 files** and found **312 problems**, including instructions no longer needed for Opus 5.5 that consumed unnecessary tokens.
- [00:11:21] He recommends running it occasionally to clean up a Claude account.

### `/skill-doctor` [00:11:27]
- [00:11:27] The presenter says every installed skill consumes some of Claude’s context, or working memory, even when unused.
- [00:11:35] `/skill-doctor` shows the context cost and usage frequency of each skill, flags rarely or never used skills, and recommends skills for deletion.
- [00:11:46] He says this tool saved him about **20,000 tokens** that had been consumed by unused skill files.

### `/advisor` [00:11:52]
- [00:11:52] `/advisor` is described as an existing favorite, particularly with the new 5.5 models.
- [00:11:58] When operating a cheaper model such as Sonnet or Haiku, the presenter says `/advisor` can ask a stronger model such as Opus for advice at key task moments.
- [00:12:06] The intended tradeoff is stronger-model judgment where needed without paying for it throughout the entire task.
- [00:12:12] His example is inbox cleanup: Sonnet handles the work, while Opus 5.5 helps draft a response when something critical appears.

## Mods [00:12:24]
- [00:12:24] Mods are introduced as one of the presenter’s favorite new features.
- [00:12:26] A mod changes how Claude Code looks and behaves, and is described as enabling users to build features inside the desktop app.
- [00:12:36] The presenter’s example is a brain-dump mod for long spoken prompts.
- [00:12:42] He identifies issues in voice brain dumps: errors, jumping among ideas, unstructured content, and occasional contradictions.
- [00:12:48] His mod detects a long voice brain dump and converts it into a clear, structured prompt before Claude processes it.
- [00:12:56] He says a user can build a mod by telling Claude to build it and describing the required behavior.

## Final recap and closing [00:13:13]
- [00:13:13] **Recap:** the features covered are the revised desktop layout and cards, chat sections, projects/nested sessions, side chats, split view, artifact-based creation tools, slash commands, and mods.
- [00:13:13] **Promotional aside:** the presenter says a free PDF guide contains prompts and a summary of every feature, and again promotes the AI Accelerator.
- [00:13:31] The video closes with thanks and a request for likes and subscriptions.

## Practical applications
- Suggestion: For a multi-part project, separate distinct workstreams into threads or nested sessions, while using one coordinator chat to maintain overall progress.
- Suggestion: Use side chats for status checks, reviews, or tangential questions so the main task’s context remains focused.
- Suggestion: Create chat sections for recurring work categories, then move older relevant chats into them for easier retrieval.
- Suggestion: Periodically run `/doctor` and `/skill-doctor` to identify configuration conflicts and unused skills that may consume context.
- Suggestion: Define an `/output-style` suited to the desired audience, such as concise nontechnical responses.
- Suggestion: If using a cheaper model for routine work, consider `/advisor` at high-stakes decision points where stronger-model review may be useful.
- Suggestion: For long voice prompts, consider a preprocessing workflow that converts the raw brain dump into a structured prompt before task execution.

## Evidence anchors
- [00:00:00.000] And Tropic just rebuilds the Claude code
- [00:00:05.840] projects, threads, mods, side panels,
- [00:00:11.920] So, in this video, I'll show you every
- [00:00:32.119] to quickly cover is the new Claude code
- [00:01:06.080] Claude code can work with any file on

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
