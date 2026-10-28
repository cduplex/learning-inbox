# The NEW Way to Build a Second Brain w/ Claude (2027)

## Source
- Original: https://www.youtube.com/watch?v=LP7bfT4vOlo
- Type: youtube
- Creator: {'displayName': 'Nick Saraev'}
- Published: 2026-10-18T00:00:00.000Z

## Tags
personal knowledge base, second brain, retrieval-augmented generation, RAG, recency weighting, context rot, BM25, plain-text search, data connectors, institutional memory, AI workflow

## Learning guide
**The arc**
Nick Saraev starts from the gap between Vannevar Bush's 1945 vision of a machine that supplements memory and today's overhyped, marketing-heavy second-brain products. His central idea is that a useful personal knowledge base is simple: feed it fresh data, enrich that data so it is findable, and search it with plain text instead of vector databases. He moves from why retrieval still matters despite huge context windows, through a four-step build (connectors, summaries and atoms, BM25 search, maintenance), to the conclusion that RAG has been overcomplicated for years.

**1. Understand why retrieval still matters**
- **Know the core terms:** A personal knowledge base is a searchable collection of your own material that AI looks up before answering. The lookup is retrieval, and retrieval plus AI generation is RAG.
- **Don't dump everything into context:** Models can now hold roughly 35 to 50 books (over a million tokens), but stuffing it all in is expensive, slow because the AI must examine everything, and less accurate. More text also makes any single item harder to find, which is called context rot.
- **Weight by recency:** A model treats everything in context as equally important, so an old product price and a new one look alike and it may put the stale price in a proposal. Timestamp every incoming item, boost recent items, and lower the weight of older ones so new material wins while old material stays available.

**2. Grasp the retrieval loop**
- **Search first, then answer:** Store data outside the model, let it search, and send only the relevant results instead of all data. Plain-text search or vector embeddings both work, and advanced systems combine techniques.
- **Automate query handling:** When you ask Claude or another model a question, run a fast inference step to pick a search term, search the knowledge base, and append the best matches to your original prompt. This removes the need to decide manually where things are stored or to rely on model memory.
- **Feed it broadly and prune it:** His system, Engram, holds around 35,000 to 50,000 records including Git history, company-wide Claude sessions and video transcripts. Recency-weight incoming items and periodically sweep out material that no longer has value.

**3. Step 1: Build source connectors**
- **Prioritize the pipelines:** The system is only as good as its data, so consistent context pipelines are the most important step. Refresh them whenever an event produces company data.
- **List your sources:** Start by defining sources such as email, your website, lead conversations, company Slack messages and phone call transcripts, especially VoIP calls.
- **Write one connector per source:** Each connector is a small script that pulls only data new since its previous run. It stamps that data with the current date and time so recency weighting works later.
- **Use read-only access:** For email, use the Gmail API with read-only permission. Never grant write access, since that gives the system too much control over your life.
- **Backfill once, then go incremental:** His first email run pulled a full year from three accounts, and later runs took only new material. He runs it every 15 minutes; pick your cadence based on compute load.
- **Save your AI sessions:** Claude and ChatGPT sessions are stored locally as plain text, so they are easy to index. They are normally deleted after 30 days, so preserving them lets you retrieve months-old conversations, project ideas and context you already supplied.
- **Let an agent map the rest:** Paste the transcript of this approach into an agent and ask it to enumerate your possible sources and help build the remaining pipelines.

**4. Step 2: Enrich every item with summaries and atoms**
- **Never store raw content alone:** Keep each long item as the original plus metadata and notes about its contents, rephrased several times to capture the idea correctly. Raw text is hard to search, especially with keyword matching.
- **Generate summaries plus likely questions:** For each item, have a cheap model write a short topic summary and the question a person would likely type to find it.
- **Extract atoms:** Pull out exact error messages, exact fixes, working commands and the decisions explaining why someone acted as they did. This turns implicit company decisions into explicit institutional memory that people and agents can retrieve as workflows.
- **Pick the cheapest trusted model:** Use the cheapest model from a provider you trust with your data (he uses Claude Haiku). Give it one prompt that produces metadata, short notes and atoms every time material enters the system.
- **Search summaries, return raw:** At query time the agent searches the summaries, and a matching summary points it to the full underlying raw item.

**5. Step 3: Search with plain text (BM25)**
- **Skip vector databases and embeddings:** Use plain-text search instead. Switching from vector-database RAG cut his inference time and his vector and embedding costs by about 9/10 each.
- **Use BM25:** BM25 is a plain-text algorithm from the 1990s that scores each document by how often the query's words appear in it. It is enough because Claude infers the remaining context; Boris Cherny, initially behind Claude Code, reported plain search beat every other approach by a large margin.

**6. Step 4: Keep it fresh**
- **Run a background watchdog:** Use a script that reruns and verifies connectors continuously. If a connector fails, new data stops arriving and the system stops tracking current information.
- **Check for known failure modes:** Have scripts detect or fix rotated API keys, changed permissions and routes that no longer work.

**Try this first:** Write a read-only Gmail API connector that pulls only email new since its last run, timestamps each item, and runs every 15 minutes.

**Caveat:** The 9/10 speed and cost savings and the claim that BM25 outperforms vector approaches come from the creator's own tests and an attributed remark, so benchmark plain-text search against your own data before abandoning embeddings.

## Derived summary
## [00:00:00] Framing: the "second brain" idea
- [00:00:00] Vannevar Bush is introduced as a 1945 engineer who imagined a machine to store his books, records, and communications, described as an enlarged, intimate supplement to memory.
- [00:00:11] The speaker contrasts that aspiration with present-day "AI slop," flashy videos, and other marketing-heavy depictions of second brains.
- [00:00:18] The speaker argues that second-brain products are easy to market because they appear technically complex and promise business-productivity gains to people who may not understand the underlying systems.
- [00:00:38] The speaker's position is that personal knowledge bases can be useful. They claim to use one for a business that earns a substantial monthly amount and intend to give a practical setup approach said to take about 3 to 4 minutes. These business and time claims are not independently verified.

## [00:00:54] Definition: personal knowledge base and RAG
- [00:00:54] A personal knowledge base is defined as a searchable collection of a person's own material, with AI looking up relevant material before answering.
- [00:01:01] The speaker calls the lookup process retrieval; combining retrieval with AI generation is called retrieval-augmented generation, or RAG.
- [00:01:12] According to the speaker, RAG was especially common when models had short context windows, since broad question answering without hallucination required selectively supplying relevant information.
- [00:01:30] The speaker says open consumer models now commonly have context capacities roughly equivalent to 35 to 50 books, so a user can theoretically put all desired source material directly into a context window. This capability claim is not independently verified.
- [00:01:44] Putting roughly 35 books of content into context is discouraged by the speaker because it would probably be expensive.

## [00:01:48] Why retrieval still matters: recency and context rot
- [00:01:48] The speaker says a knowledge base remains useful for proprietary data and that the described mechanisms are intended to improve answers over that data.
- [00:02:03] When a large body of material is placed directly in a model context window, the speaker says the model treats it as equally important.
- [00:02:09] Example: an old product price and a new price may be treated alike when the model helps create a proposal, so the model may confidently return whichever text is easiest to find rather than the current price.
- [00:02:32] The proposed mitigation is **recency weighting**: timestamp each incoming item, boost more recent items, and reduce the weight of older items.
- [00:02:50] The intended result of recency weighting is that the model preferentially considers newer material while retaining older material at lower priority.
- [00:02:57] The speaker identifies a second issue: as more text is added, retrieving a particular item becomes harder.
- [00:03:04] This is called "context rot" in the video: performance supposedly declines as context-window content increases.
- [00:03:12] Even if more than a million tokens or about 35 books can theoretically fit, the speaker gives three practical drawbacks: high operating cost, slower processing because the AI must examine the material, and lower expected accuracy than the proposed retrieval workflow.

## [00:03:31] Retrieval workflow and the speaker's Engram example
- [00:03:31] Retrieval means storing data elsewhere, having the model search first, then supplying relevant results rather than sending all data.
- [00:03:39] The speaker says retrieval can use plain-text search or vector embeddings, while noting that these options only scratch the surface and that more advanced systems combine techniques.
- [00:03:54] The speaker's system, called Engram, is claimed to hold around 35,000 to 50,000 records at a time, including Git history, company-wide Claude sessions, and video transcripts. These scale and implementation claims are not independently verified.
- [00:04:12] Incoming information is reportedly recency-weighted, and the collection is periodically swept to remove material that no longer has value.
- [00:04:25] For a question to Claude or another language model, the system reportedly runs a fast inference step to choose a search term, searches the knowledge base, then returns best matches.
- [00:04:42] The matched material is appended to the user's original prompt, after which the model uses it to formulate an answer.
- [00:04:51] The speaker characterizes the experience as seamless because they do not need to manually decide where to store information or rely on model memory; they claim recency weighting usually prevents retrieval of stale conversational artifacts. This performance claim is not independently verified.

## [00:05:16] Step 1: maintain source connectors and fresh ingestion
- [00:05:16] The first and most important stated step is maintaining consistent context pipelines into the knowledge base, because the system is only as good as its data.
- [00:05:28] Pipelines should refresh whenever an event produces company data.
- [00:05:38] The workflow begins by defining sources, with examples including email, a website, lead conversations, company Slack messages, and transcripts from company phone calls, particularly VoIP calls.
- [00:05:51] For each source, build a small script called a connector that pulls only data new since its previous run.
- [00:06:00] The connector timestamps the new data with the current date and time, enabling recency weighting later.
- [00:06:03] The speaker's email example uses the Gmail API with read-only access.
- [00:06:08] The speaker warns against granting write access, arguing that it would give the system excessive control over a user's life.
- [00:06:14] On its first run, the speaker's email connector reportedly ingested one full year of email from three accounts; later runs collected only material generated since the prior run. This example is not independently verified.
- [00:06:24] The speaker runs the connector once every 15 minutes, while saying users can choose another cadence based on compute load.
- [00:06:34] The speaker recommends also ingesting Claude or ChatGPT sessions, claiming these sessions are stored locally as plain text and are therefore easy to index.
- [00:06:44] The stated reason to preserve AI sessions is that they are normally deleted after 30 days; preservation permits later retrieval of months-old conversations, project ideas, and previously supplied context. The 30-day deletion claim is not independently verified.
- [00:06:58] The speaker suggests placing the transcript into an agent and asking it to enumerate possible sources and help construct the remaining pipeline.

## [00:07:09] Step 2: create searchable summaries and atoms
- [00:07:09] The speaker says raw content should not simply be stored without transformation. Each long item is represented by the original item plus metadata and notes about its contents.
- [00:07:23] The notes are described as being rephrased several times to capture an idea correctly.
- [00:07:29] The next step is to have a cheap model write summaries.
- [00:07:34] The rationale given is that raw text is difficult to search, particularly when the retrieval system relies on keyword matching.
- [00:07:41] For each item, generate a short topic summary and include the likely question a person would enter to find that material.
- [00:07:55] Add "atoms": exact error messages, exact fixes, working commands, and the decisions explaining why someone acted as they did at that time.
- [00:08:11] The speaker says atoms make implicit company decisions explicit and turn them into organizational institutional memory.
- [00:08:24] The claimed benefit is that people or agents can retrieve workflows and processes from this explicit record.
- [00:08:30] This enrichment step uses another language model. The speaker currently uses "Claude Haiku 5.5," previously used 4.5, and predicts they may use 6.5 in the future. Model-version references and the prediction are not independently verified.
- [00:08:40] The selection criterion proposed is the cheapest model from a provider trusted with the data. Give it a prompt that produces metadata, short notes, and atoms whenever material enters the system.
- [00:08:57] At query time, the agent searches summaries rather than raw data; when a summary matches, it points the agent to the complete underlying raw item.

## [00:09:10] Step 3: use plain-text search, specifically BM25
- [00:09:10] The speaker says the final core requirement is to make the collection searchable and argues that users often overcomplicate this with vector databases and embeddings.
- [00:09:17] The recommended simpler approach is plain-text search without embeddings.
- [00:09:20] Based on the speaker's experience, replacing vector-database-based RAG with plain text reduced inference time by about 9/10 and reduced vector-database and embedding costs by about 9/10. These comparative performance and cost claims are not independently verified.
- [00:09:44] The specific proposed algorithm is BM25, described as a plain-text method from the 1990s.
- [00:09:48] The speaker describes BM25 as assigning each document a score based on the frequency of words used in the search query.
- [00:09:56] The speaker's claim is that BM25 is sufficient because Claude can infer the remaining context intelligently. This sufficiency claim is not independently verified.
- [00:10:01] The speaker attributes a claim to Boris Cherny, described as being initially behind Claude Code: plain search allegedly outperformed every other approach by a large margin. This attributed comparison is not independently verified.
- [00:10:16] The speaker concludes that RAG systems have been overcomplicated for a long time.

## [00:10:22] Step 4: operational maintenance and recap
- [00:10:22] Keep the system fresh by running a background script that reruns and verifies connectors.
- [00:10:28] If a connector fails, new data does not reach the knowledge base, causing the system's usefulness to fail because it no longer tracks current information.
- [00:10:40] The speaker names operational failure modes: rotated API keys, changed permissions, and routes that no longer work; scripts should continually update or check for these problems.
- [00:10:49] **Recap:** the speaker says this process yields the same kind of second-brain system used by them and by many multibillion-dollar companies. This adoption claim is not independently verified.
- [00:10:54] The speaker says their approach was initially informed by a Cohere second-brain ingestion pipeline and that their tests against prior RAG approaches favored this method. This attribution and test result are not independently verified.

## [00:11:17] Aside: resource promotion and closing
- [00:11:17] **Promotional aside:** The speaker says a copy-paste rebuild prompt is available through a second description link at Maker Zero, described as a free home for their AI, educational, informational, curriculum, and roadmap resources.
- [00:11:41] The speaker says users must join, navigate to the community tab, and look under recently uploaded to find the resource.
- [00:11:49] The video closes with a request to subscribe and comment with future topic ideas; the speaker says they get virtually all current video ideas from comments.

## Evidence anchors
- [00:00:00.000] In 1945, an engineer called Vannevar
- [00:00:02.200] Bush imagined a machine that could store
- [00:00:03.960] all of his books, records, and
- [00:00:05.880] communications. He called it an enlarged
- [00:00:08.520] intimate supplement to his memory. 80

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
