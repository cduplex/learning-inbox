# I've Set Up 500+ AI Second Brains. Here's The Only 18 Things You Need to Know

## Source
- Original: https://www.youtube.com/watch?v=pXHpUyC54uQ
- Type: youtube
- Creator: {'displayName': 'Ben AI'}
- Published: 2026-10-28T00:00:00.000Z

## Tags
AI second brain, knowledge management, AI agents, Markdown, team collaboration, context management, automation

## Derived summary
## 00:00 Introduction: What an AI second brain is
- [00:00] The presenter describes an AI second brain as context that helps chats, skills, agents, and AI tools understand a person and their business. The presenter’s performance, product, and experience claims throughout these notes are not independently verified.
- [00:00:17] The presenter says common failures include becoming overwhelmed during setup, allowing information to become outdated, and failing to secure team adoption.
- [00:01:02] The basic system is described as a computer folder containing text files that an AI tool can consult for current context.
- [00:01:12] The presenter’s example includes strategy, team information, YouTube videos, and sales-lead history, among thousands of files.
- [00:01:22] The proposed benefit is more relevant output because the AI can retrieve task-specific business context rather than relying only on a generic prompt.
- [00:01:33] The presenter says the same folder can be used across AI tools and, when shared, can provide a common context for a team.
- [00:01:46] Obsidian is presented as a way to visualize files and their connections in a graph, which helps explain the ‘second brain’ name.

## 00:02 Setup: Start small and use local files
### 00:02:04 Tip 1: Begin with a brain dump
- [00:02:15] The presenter estimates that a 30-minute brain dump can provide around 80% of the value of a second brain.
- [00:02:21] In the presenter’s own system, 5 to 10 files reportedly provide 80% of the value, including strategy, ideal customer profile, brand voice, and offer documents.
- [00:02:34] The reason given is that these core files are relevant to almost any task, unlike many more specialized files.
- [00:02:40] The proposed workflow is to use Claude and a voice-dictation tool, then speak freely about identity, business, customers, goals, strategy, writing preferences, and team.
- [00:02:55] The presenter says the unstructured material can be turned into 5 to 10 clean files.
- [00:03:04] A presenter-built setup skill is described as asking questions individually and creating files after Claude is given access to an empty folder.
- [00:03:34] For later chats, the presenter says to select the same folder so the AI can retrieve context and save new information back into it.

### 00:03:51 Tip 2: Set up locally
- [00:03:57] The presenter contrasts a local folder with built-in AI memory and existing data in Notion or Google Drive.
- [00:04:05] The presenter characterizes built-in memory as limited to a few facts and tied to one provider.
- [00:04:17] The presenter claims connectors to other software can make reading and saving context slower, less accurate, more expensive, and more token-intensive than local files.
- [00:04:37] In the proposal example, a client subfolder supplies context directly rather than requiring searches across a CRM, Drive, email, and meeting transcripts.
- [00:04:55] The presenter emphasizes ownership and portability: the files remain on the computer and the same folder can be selected with different AI tools.

### 00:05:11 Tip 3: Visualize the folder
- [00:05:14] Markdown files become harder for a person to find, read, and check as the folder grows.
- [00:05:26] Obsidian is described as a free visual layer over a local folder, including a graph of file connections.
- [00:05:37] The presenter says this layer helps people manage the files without changing how the AI accesses the underlying folder.
- [00:05:49] The presenter’s app, Balda, is also described as a visualization layer with team-sharing and synchronization features; both tools can be opened on the same folder.

## 00:06 Structure and routing
### 00:06:14 Tip 4: Create a root routing file
- [00:06:16] As files accumulate, the presenter argues that an AI needs a map of where context belongs; otherwise it may search broadly, waste tokens, or retrieve the wrong material.
- [00:06:31] The proposed root `agents.md` file tells the AI what each folder contains, when to use it, and where to save new information.
- [00:06:42] For sales-call preparation, the routing example directs the AI to client notes in sales and the offer in business, rather than opening everything.
- [00:06:55] The presenter describes `agents.md` as a provider-independent alternative to `claude.md` and claims it is read at the start of a session.
- [00:07:16] Its central element is a routing table: a map of folders and their uses, not a manual containing all business information.
- [00:07:34] The presenter attributes an under-200-line recommendation to Anthropic and says a setup skill or an AI request can generate the file from the folder.
- [00:07:55] The presenter advises renaming an existing `claude.md` rather than keeping both files, claiming Claude otherwise reads that file and skips `agents.md`.

### 00:08:07 Promotional aside
- [00:08:07] The presenter promotes an AI accelerator offering consulting, courses, community, and resources; free skills and a setup guide are also mentioned earlier. [00:03:20]

### 00:08:43 Tip 5: Use one main folder
- [00:08:45] The presenter generally favors one second-brain folder over separate folders for every project, department, client, or business.
- [00:08:58] Multiple brains create more folders to maintain and choose between, while a routing file can direct the AI to the relevant subfolder in one brain.
- [00:09:16] The presenter’s example puts businesses, clients, and departments in subfolders under the same root.
- [00:09:29] Possible exceptions are completely separate businesses with no overlapping context, or a desire to separate personal and business projects.

### 00:09:38 Tip 6: Keep the folder structure stable
- [00:09:41] The presenter says exact subfolder names matter less than maintaining a consistent structure that the AI can use to find and save files.
- [00:10:05] Moving or adding folders requires the routing file to be updated; otherwise the AI may save to an old location or fail to find needed material.
- [00:10:19] For example, splitting clients into active and past clients without updating the map can leave new notes going into the old location.

### 00:10:46 Tip 7: Add subfolder indexes
- [00:10:50] When a subfolder grows to dozens or hundreds of files, a root map may identify the right folder but not the right file within it.
- [00:11:03] The proposed solution is a small index in each subfolder listing its contents and explaining what each file covers.
- [00:11:16] The presenter attributes the approach to Andrej Karpathy: the model reads the index first, then drills into relevant pages.
- [00:11:31] Indexes must be updated as subfolders grow, even if a setup skill initially creates them.

## 00:11 Maintenance: Preserve useful, current context
### 00:11:58 Tip 8: Save insights rather than raw data
- [00:12:01] The presenter frames the second brain as a filtered layer over raw data, holding useful, broken-down insights rather than every spreadsheet, database, or software export.
- [00:12:28] Combining sources can produce takeaways that are not apparent from a single source alone.
- [00:12:35] For this video, the presenter says AI analyzed hundreds of support calls, community questions, and support tickets, then saved the resulting mistakes and tips in one Markdown file.
- [00:12:48] The claimed benefit is consulting that file instead of repeatedly using five connectors and hundreds of tool calls.
- [00:12:59] The folder can also capture knowledge held in people’s heads, such as strategy, decisions, preferences, reasons for a price increase, or lessons from an unsuccessful launch.
- [00:13:28] The presenter calls the second brain an addition to connectors and raw data, not a replacement for them.

### 00:13:38 Tip 9: Update daily
- [00:13:42] The presenter warns that a brain becomes stale when new information and changes are not incorporated.
- [00:13:57] The proposed daily scheduled task checks important connectors and sources, then saves insights from what is new or changed rather than dumping raw data.
- [00:14:16] Meeting transcripts are highlighted because decisions often appear there without being captured elsewhere.
- [00:14:23] Other example sources include the CRM, project-management software, email, and Slack.
- [00:14:32] The presenter describes an operator skill that helps select connectors and set up the scheduled update.
- [00:14:50] The same skill is said to review older files and update or delete them when new information makes them outdated.

### 00:15:11 Tip 10: Clean up weekly or every two weeks
- [00:15:14] As the brain grows, routing and index files can diverge from actual contents, while duplicates, contradictions, and unlinked notes accumulate.
- [00:15:32] The presenter proposes a health check every week or two and describes an optimizer skill for performing it.
- [00:15:53] The optimizer is said to update the root map and indexes, check that folders are mapped and routing still works, and keep `agents.md` under 200 lines.
- [00:16:10] It is also described as fixing broken links, duplicates, unlinked notes, and contradictions.
- [00:16:22] Further cleanup includes shortening overly long files, reducing unnecessary token costs, and clarifying filenames and missing labels.
- [00:16:36] The presenter says the tool produces a health score out of 100 and a report, fixes small issues immediately, and asks before larger changes.
- [00:16:52] The presenter recommends scheduling this deep clean weekly or every two weeks.

## 00:17 Use the knowledge base
### 00:17:00 Tip 11: Build a dashboard
- [00:17:02] The presenter says a dashboard makes information in many Markdown files easier for people to use, and identifies three dashboard types.
- [00:17:23] A general overview might show today’s priorities, this week’s decisions, team assignments, and upcoming meetings with preparation notes.
- [00:17:35] A department dashboard can focus on a business function. The presenter’s sales example shows prepared calls, deal status, and due follow-ups.
- [00:17:49] The presenter says their sales dashboard is useful enough that representatives rarely need to open the CRM for daily work.
- [00:18:05] A problem-specific dashboard can assemble relevant context around a question, such as why client onboarding is taking longer this quarter.
- [00:18:17] For that example, the AI would review meeting notes, project files, and decisions to identify where work is getting stuck.
- [00:18:25] The presenter favors simple, decision-useful information over elaborate graphs that merely show connections.
- [00:18:45] The described workflow is to ask the AI for a dashboard, specify what it should show, and schedule a morning refresh.

### 00:19:06 Tip 12: Point skills to shared reference files
- [00:19:10] The presenter says many skills need the same reference files, such as business strategy, brand voice, and offers.
- [00:19:25] Keeping ten copies of a strategy document across ten skills creates ten updates whenever the strategy changes; neglected copies can become stale.
- [00:19:40] Pointing skills to one reference file in the second brain means one update can serve all skills that use it.
- [00:19:58] Examples include a brand voice guide shared by LinkedIn, newsletter, and email skills, and an offers-and-pricing document used for proposals, call preparation, and outreach.
- [00:20:10] The presenter distinguishes reference files from the skills themselves, recommending that skills remain in the AI account because storing them in the brain becomes messy and harder to update.
- [00:20:23] When building or updating a skill, the presenter says to specify that its references should point to the appropriate second-brain files instead of copied documents.

## 00:20 Advanced operation and team rollout
### 00:20:41 Tip 13: Update while the laptop is closed
- [00:20:45] The presenter says a scheduled task using local computer files runs only while the laptop is open and the Claude app is running.
- [00:21:04] The proposed alternative is a Claude Code cloud routine: copy the daily task’s prompt into a routine and choose its schedule.
- [00:21:26] The tradeoff is that a cloud routine cannot reach files solely on the computer, so the brain must also be accessible in the cloud through a connector.
- [00:21:38] The presenter describes connecting Balda through Claude’s customization menu, logging in, and selecting the brain so routines can read and update it.
- [00:21:58] The presenter says an Obsidian-based approach is also possible but characterizes it as more technical.

### 00:22:14 Tip 14: Synchronize one brain across the team
- [00:22:19] Team sharing requires everyone to have the same files and changes to synchronize across their computers.
- [00:22:36] The presenter reports limitations with other setups, including technical complexity, simultaneous-edit conflicts, overwrites, and missing person- or department-level permissions.
- [00:23:05] Balda is presented as the presenter’s solution: open the local folder, select sync, create a cloud copy, and invite the team.
- [00:23:29] One described access method is an email invitation followed by app installation, which reportedly installs the brain locally and syncs changes in real time.
- [00:23:45] The other method is to add the connector to an AI account without installing the app; the presenter says connector access is less efficient than the local-folder option.

### 00:24:08 Tip 15: Roll out in stages and designate an owner
- [00:24:13] The presenter warns that a company-wide launch on day one can produce inconsistent file additions and a messy system.
- [00:24:26] The proposed sequence is to use the brain personally for a couple of weeks, then add one team member, one department, and finally the whole company.
- [00:24:39] The rationale is to resolve problems while they are small and give each new user a system that already works.
- [00:24:45] One owner should be responsible for ongoing care, because shared responsibility can result in nobody performing maintenance.
- [00:25:00] The owner’s described duties include weekly cleanup, approval of folder-structure and `agents.md` changes, troubleshooting, and access management.

### 00:25:18 Tip 16: Control access
- [00:25:22] The presenter identifies unrestricted visibility and editing of leadership notes, financials, client files, and HR information as a team-sharing problem.
- [00:25:42] Balda is described as supporting edit, view-only, and no-access settings for individual folders or files, across a team, department, or individual.
- [00:25:53] In the presenter’s example, the context folder and `agents.md` are view-only for everyone, while the finance folder is visible only to the co-founder.
- [00:26:06] The presenter claims file-level permissions also restrict what a user’s AI tool can access, regardless of provider.

### 00:26:15 Tip 17: Create team dashboards
- [00:26:18] The presenter describes a team dashboard as a way to expose business information such as sales, customer feedback, delayed projects, and assignments.
- [00:26:37] The brain owner may build dashboards for departments rather than expecting every employee to build one.
- [00:26:44] The sales example includes pipeline, prepared calls, and follow-ups; marketing includes content performance, customer insights, and competitors; operations includes projects, deadlines, and recent decisions.
- [00:27:03] The presenter also describes individual dashboards and sharing through a Claude artifact link or a hosted URL such as Vercel.
- [00:27:19] The presenter says a dashboard feature for Balda is in development, with templates or suggestions based on the brain’s contents. This is a future product plan, not a verified capability.
- [00:27:38] For people selling second-brain setup as a service, the presenter identifies dashboards as a visible component that clients may use daily.

### 00:27:47 Tip 18: Add a business-first rule
- [00:27:54] The presenter argues that individual AI agents may agree with the employee using them instead of checking whether a request fits the business’s interests.
- [00:28:18] The presenter cites an article contrasting institutional and individual AI, framing the aim as reinforcing business truth rather than simply reinforcing each user.
- [00:28:41] The proposed `agents.md` instruction asks the AI to act in the business’s best interest based on goals and strategy, and to say clearly when a request or output conflicts with them.
- [00:28:53] The presenter claims that placing this rule in a shared file can distribute the same business context and instruction across the team’s agents.

## 00:29:08 Closing recap and promotional aside
- [00:29:08] The presenter’s final example ties the shared rule to a common source of business goals and strategy.
- [00:29:08] The closing promotes the accelerator and Balda and points viewers to further setup material. [00:29:27]

## Practical applications
- Suggestion: Draft a small set of core context files from a voice brain dump, then organize them under one stable folder with a routing file and subfolder indexes.
- Suggestion: Design a maintenance workflow that separates daily extraction of new insights from a weekly or fortnightly review of indexes, duplicates, links, and contradictions.
- Suggestion: Pilot a shared brain with one user and then a small team, assigning an owner and defining view, edit, and no-access permissions before broader rollout.
- Suggestion: Prototype a decision-focused dashboard for one department, using shared reference files rather than duplicating them across skills.

## Evidence anchors
- [00:00:00.000] An AI second brain has become the
- [00:00:17.600] we've seen most people either get stuck
- [00:01:00.640] concept, it might sound very fancy or
- [00:01:04.239] folder on your computer with lots of
- [00:01:22.400] powerful is simple. Instead of your AI

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
