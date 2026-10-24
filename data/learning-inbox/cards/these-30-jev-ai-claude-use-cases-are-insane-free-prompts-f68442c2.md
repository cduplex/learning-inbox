# These 30 Jev AI + Claude Use Cases Are INSANE (free prompts)

## Source
- Original: https://www.youtube.com/watch?v=MT9uNomIvgk
- Type: youtube
- Creator: {'displayName': 'Kev Builds Apps'}
- Published: 2026-10-07T00:00:00.000Z

## Tags
AI agents, system-one models, lead scoring, computer use, knowledge graphs, RAG, content moderation, marketing automation, agentic routing

## Derived summary
## Source framing [00:00:00]
- [00:00:00] The speaker says the AI field was recently surprised by a wave of "system one" models that do not converse, instead making decisions by ranking items, returning yes/no answers, or selecting from options.
- [00:00:15] The speaker claims that connecting "Jev" with Claude and other frontier LLMs unlocks many use cases. Claims about speed, cost, capabilities, and demonstrations are the speaker's claims and are not independently verified here.
- [00:00:29] The speaker says they examined Jev use cases for four weeks, selected a top 30, and intends to show an example or demo for each.
- [00:00:48] The stated workflow benefits sought from Jev are speed increases, scoring different outputs, and obtaining quick answers.
- [00:01:04] The speaker lists eight business pillars: lead and prospect intelligence; social and customer communication; real-time moderation and live operations; custom scoring and evaluation models; agent orchestration and routing; knowledge graphs and workflow memory; computer and browser use; and marketing. The remainder specifically discusses lead intelligence, browser/computer use, RAG, real-time operations, marketing, and coding.

## Lead and prospect intelligence [00:01:31]
### Intent detection across inbound channels [00:01:35]
- [00:01:35] Use case 1 is intent detection for warm inbound leads arriving through websites, social direct messages, WhatsApp, text messages, or voicemails.
- [00:01:54] For website activity, the proposed workflow connects PostHog to Jev so Jev evaluates what a user clicks on a checkout page.
- [00:02:02] If that behavior suggests high checkout intent, the workflow can tag that person as a warm lead.
- [00:02:11] For social DMs, the speaker says the system can scan thousands of inbound messages simultaneously and rank them by intent.
- [00:02:23] The proposed scoring compares what a prospect says with what typical customers say; the same pattern is said to apply to SMS and voicemail.

### Inbox tagging and filtering [00:02:36]
- [00:02:36] Use case 2 extends intent detection to tagging and filtering an entire inbox.
- [00:02:46] The speaker's email example contains sponsorship inquiries, lead inquiries, and spam; a Jev workflow would tag and filter each newly received email.

### Lead, influencer, and sponsor scoring [00:03:04]
- [00:03:04] Use case 3 is lead scoring for a scraped list of 1,000 leads that includes metadata such as profile information, location, follower information, and occupation.
- [00:03:18] The workflow compares the lead metadata against an ICP, or ideal customer profile, provided to Jev.
- [00:03:28] The speaker says this information enables lead scoring, heavy filtering, and processing before creating personalized outreach messages.
- [00:03:43] The same ranking workflow is proposed for influencer discovery, sponsorship discovery, and lead scoring.
- [00:03:54] For influencers, candidates are ranked against the characteristics of an ideal sponsored influencer; for channel sponsors, potential AI sponsors are screened against desired sponsor characteristics.

### CRM updates and outbound messaging [00:04:06]
- [00:04:06] Jev can, according to the speaker, update a CRM based on earlier tagging rather than responding to or filtering messages itself.
- [00:04:12] The claimed inputs can include PostHog, DMs, SMS, voicemails, and Gmail.
- [00:04:28] Example: if a person named Daniel in DMs appears likely to be a warm lead, the workflow tags Daniel as a warm lead in the CRM so the remaining sales pipeline continues from that status.
- [00:04:40] The final use case in this pillar is sending outreach.
- [00:04:47] The speaker frames outbound delivery as a token-saving division of labor: finding a user, locating the user's inbox, and sending through a computer-use tool are automated steps.
- [00:05:00] Once intent detection and lead scoring mark someone as a warm lead fitting the ICP, the workflow can prepare outbound messaging.
- [00:05:11] The speaker claims 99% of this workflow can use Jev, while an LLM is needed only for copywriting the outbound message.
- [00:05:33] A yes/no trigger can evaluate social DMs, SMS, emails, and phone calls immediately.
- [00:05:42] When warm intent is detected and lead details are complete, Jev can trigger the next skill that sends the DM.

## Web browsing and computer-use agents [00:05:54]
### Video-game control [00:06:03]
- [00:06:03] The first discussed computer-use example is playing video games. The speaker says a future master class will cover reverse engineering and combining games.
- [00:06:12] Jev is characterized as the "hands" of an LLM: it may not reason well enough to play an entire game alone, but it can click computer controls quickly.
- [00:06:30] The speaker claims that, with "Opus 5.5" as the reasoning brain behind Jev, the setup can play entire 2D games.
- [00:06:38] Another proposed method is to control play using probabilities of surviving, winning, or meeting another specified goal, with Snake, chess, and Subway Surfer named as examples.

### UI and application testing [00:06:54]
- [00:06:54] Use case 9 is application and user-interface testing.
- [00:07:00] The described loop is: agents click through buttons, record the screen, then submit the recording to an AI model for review.
- [00:07:08] The speaker says hundreds of Jev agents could test a UI concurrently, producing many simulated-user tests before public release and enabling faster debugging.

### Deal hunting and supplier negotiation [00:07:27]
- [00:07:27] The speaker describes a "deal hunting swarm" in which an agent with computer-use tools completes a task.
- [00:07:37] In the example, the agent was instructed to find a car on Facebook Marketplace using specified filters and reportedly did so autonomously.
- [00:07:45] Suggested variants include finding deals, negotiating, or, for a B2B supplier supporting an e-commerce brand, locating suppliers in China and negotiating for a lower price.
- [00:07:57] The proposed handoff is to give the result to a human after the negotiated price reaches the desired target.

### Desktop cleaning and inaccessible interfaces [00:08:07]
- [00:08:07] Another cited use case is desktop cleaning and file management.
- [00:08:14] The speaker says a user can provide roughly 100 filtering criteria that determine where files should go.
- [00:08:20] Jev combined with a vision model is said to filter information and place files into computer folders quickly.
- [00:08:28] The speaker says code for this has already been open sourced and that examples in the video will be linked.
- [00:08:37] For social automation, APIs, or tasks that are not API-accessible, the speaker claims Jev plus Claude is preferable because it works faster and at lower token cost.
- [00:08:55] The speaker notes that computer-use automation itself is not new, but claims the cost is now lower.

## RAG, knowledge graphs, and workflow memory [00:09:07]
### Retrieval mechanism [00:09:07]
- [00:09:07] The speaker describes RAG as storing substantial data in a knowledge graph and using Jev with a graph such as Obsidian.
- [00:09:24] The proposed mechanism is that Jev receives a question, selects Obsidian as the relevant option, and Obsidian runs the prompt as a query.
- [00:09:43] That query retrieves answers from material stored in the knowledge graph.
- [00:09:50] The analogy is an entire library of books stored in the graph.
- [00:09:59] In the example, a request for a book in a category is forwarded to Obsidian, which retrieves about 10 recommendations and returns them immediately.
- [00:10:13] The speaker claims this library-query process happens in about 1 second.

### Expense and internal-data retrieval [00:10:24]
- [00:10:24] A business use case is receipt and expense extraction.
- [00:10:28] The speaker proposes extracting, tagging, and storing every transaction from a business banking account as a business expense in the knowledge graph.
- [00:10:39] The claimed benefit is instant retrieval of expense categories together with the verified transaction.
- [00:10:46] Another use case is internal-data search, including storing all transcripts from a company's sales calls.
- [00:10:56] The organization could then study winning sales calls and identify tactics used by salespeople.

### Media-library retrieval for editing [00:11:01]
- [00:11:01] The speaker also names internal-data tagging and retrieval, video editing, and media-library retrieval.
- [00:11:10] Their example connects a Jev knowledge graph trained on different media to a video editor.
- [00:11:19] The intended result is that the editor can pull media files instantly through the Jev-plus-Obsidian combination.

## Real-time moderation and live operations [00:11:26]
- [00:11:26] The speaker says system-one operations run in milliseconds, enabling real-time or apparently instantaneous workflows.
- [00:11:44] One example is a live-stream co-host or stream manager that removes comments containing specified keywords.
- [00:11:56] The described logic monitors the feed, asks a binary question about whether a specified word is present, and removes the comment if the answer is yes.
- [00:12:19] The same approach is proposed for a Discord or other large chat community.
- [00:12:32] The moderation rules can identify spammers and ban them, block messages containing bad content, or put rude users in a timeout.
- [00:12:39] The speaker's concrete timeout example is 30 minutes for users being rude.
- [00:12:47] The claimed tradeoff is binary speed and low token use versus an LLM that may deliberate for longer and consume thousands of tokens and credits.
- [00:12:59] A more specific binary-rule illustration is detecting the f-word and applying a five-minute timeout.

## Marketing workflows [00:13:07]
### Viral idea mining [00:13:20]
- [00:13:20] The speaker proposes viral idea mining by "doom scrolling" much faster than a person.
- [00:13:29] Jev is said to traverse a Twitter feed 1,000 times faster, search for keywords, and extract matching posts.
- [00:13:43] Hypothetical example: after a Claude Opus 6 release, the system could search for the 10,000 most recent posts about it with the most engagement and show them immediately.

### Reddit user-voice research [00:14:02]
- [00:14:02] The speaker identifies three marketing sources: Reddit for user voice, Instagram and TikTok for viral videos, and Google Search for viral blogs.
- [00:14:19] A Reddit scoring system would seek the most numerous and most recently asked questions that match the ICP.
- [00:14:32] The agent would scroll through designated subreddits, monitor their feeds, identify user voice, and score the findings.
- [00:14:55] The proposed next step is either responding with a video idea or creating a Reddit post intended to funnel people to a website.

### Viral-video scoring [00:15:04]
- [00:15:04] For Instagram and TikTok, the workflow examines what is posted in a niche and what is going viral, then applies a user-defined scoring template.
- [00:15:18] One scoring signal is whether a video's views exceed the creator's total follower count, which the speaker says suggests a strong video idea.

### Search-driven blog workflow [00:15:26]
- [00:15:26] For viral blogs, the speaker proposes using the Google Search Console API.
- [00:15:29] The setup supplies Jev with Search Console and a list of about 100 of the best niche keywords.
- [00:15:38] Each day, the workflow checks those keywords, identifies ranking content and the types of blogs being published, then scores how closely the content matches blogs the organization could recreate.
- [00:15:52] An LLM could then recreate those blogs and post them to the organization's website, according to the speaker.

## Coding and agentic routing [00:15:58]
- [00:15:58] The final pillar is coding, which the speaker predicts will grow as system-one models improve and their capabilities expand.
- [00:16:08] The first coding use case is agentic routing.
- [00:16:08] Jev is positioned as a front-door decision-maker that evaluates each incoming prompt to improve workflow speed and reduce token use.
- [00:16:24] Routing can select which model should handle a prompt or bypass a model entirely by immediately calling the requested skill.
- [00:16:36] The speaker says a linked tutorial explains agentic routing and connecting Jev to Claude Code.

## Recap [00:16:44]
- [00:16:44] The speaker concludes by characterizing the video as an overview of Jev AI use cases, centered on fast binary decisions, ranking, scoring, retrieval, computer actions, real-time moderation, marketing research, and routing to LLMs or direct skills.

## Practical applications
- Suggestion: Use a binary intent gate before expensive LLM generation, then route only qualified leads to CRM updates or human-reviewed outreach.
- Suggestion: Design UI testing as a loop of parallel browser agents, captured recordings, model-based review, and human validation before release.
- Suggestion: For real-time moderation, define explicit keyword, spam, blocking, and timeout rules, with escalation paths for ambiguous cases.
- Suggestion: Build retrieval workflows around a curated knowledge graph with tagged transactions, sales transcripts, or media assets, and validate retrieved records before relying on them.
- Suggestion: Create a marketing research scorecard for Reddit questions, short-form video performance, and ranking blog content before producing new content.
- Suggestion: Implement agentic routing so simple requests invoke deterministic skills while complex requests are sent to an appropriate LLM.

## Evidence anchors
- [00:00:00.080] So last month, the AI world got shocked
- [00:00:08.240] of three ways by ranking things,
- [00:00:29.359] that after studying the best Jev AI use
- [00:00:48.000] these Jeb AI use cases. And with Jeb
- [00:01:04.400] about the eight pillars that Jev can

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
