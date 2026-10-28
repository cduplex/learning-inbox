# Andrew Ng on Coding Agents and Deciding What to Build

## Source
- Original: https://www.youtube.com/watch?v=qeMMnOiF51A
- Type: youtube
- Creator: {'displayName': 'Supabase Library'}
- Published: 2026-10-12T00:00:00.000Z

## Tags
AI engineering, coding agents, software engineering, developer skills, AI applications, product development, education, personalized learning, infrastructure, databases

## Learning guide
**The arc**
Andrew Ng starts from a practical question: as coding agents get more capable, should developers keep building skills, and what work stays human? His central idea is that AI engineering rests on four skills (build and deploy uncertain AI applications, keep software-engineering fundamentals, use coding agents, and shape the build), and that humans stay valuable wherever they hold context agents lack. He moves from that skills map through fundamentals versus fast-changing tools, into deciding what to build and when to prototype versus plan, and ends with a warning that offloading thinking to AI can undermine your own learning.

**1. Map yourself against the four AI-engineering skills**
- **Treat AI engineering as your skill set, whatever your title:** Frontend, backend, DevOps, mobile and general software engineers all benefit from these skills, and employers report they cannot find enough people who have them. Use the four skills as a checklist of your existing strengths and gaps.
- **Expect many gaps, not one:** The map came from reviewing more than 10,000 job postings plus dozens of interviews asking what separates a great developer from a less effective one. The difference spans many skills, so plan systematic progress across all four instead of chasing a single trick.

**2. Focus on work where you hold a context advantage**
- **Use the context test to predict what agents will take over:** A task stays human when humans have a fundamental context advantage. One-size-fits-all work, like crafting arcane prompt incantations or managing a swarm of agents, will increasingly be done by agents.
- **Lean on context only you have:** Remember the customer conversation, the revealing facial expression, or the market report from years ago, and bring it into key decisions. This context is hard to hand to an AI, so it keeps product, architecture and tradeoff decisions valuable.

**3. Build AI applications that manage uncertainty**
- **Plan for unknown outcomes:** When you prompt a language model or train a supervised-learning algorithm, you do not know the result in advance. This uncertainty is the defining difference from traditional software.
- **Monitor and run error-analysis loops:** Put monitoring on system performance, then use disciplined error analysis and evaluation loops to improve the system step by step. This knowledge of building, deploying, monitoring, updating and steering AI apps changes more slowly than hype suggests, so it pays to learn deeply.

**4. Keep fundamentals so you can steer coding agents**
- **Learn concepts like rewrite ratio and transactions:** Even when AI writes most of the code, people who understand engineering concepts steer coding agents better and make much better decisions.
- **Know the tradeoffs before the agent picks them:** Engineering means weighing cost, latency, speed and reliability. In vibe coding, an agent can make tradeoffs you never noticed or intended, which causes problems later, and without fundamentals you may not even know which tradeoffs exist.
- **Check agent judgment on data and engineering decisions:** Delegate data-frame and data-science work to agents, but watch for strange decisions and strange conclusions, since agents often lack reliable engineering or data-science judgment.
- **Separate fast-changing tools from stable knowledge:** Coding-agent workflows change noticeably every three to six months, so keep refreshing that skill while investing steadily in the slower-moving fundamentals.

**5. Shape the build, not just implement it**
- **Expect the bottleneck to move to deciding what to build:** As implementation gets easier, choosing the right thing becomes the constraint. Use AI to widen your coverage of the stack, for example a frontend engineer taking on more backend work.
- **Gather feedback yourself instead of waiting:** Waiting for a product manager to collect feedback is slow. Develop some product instinct, talk to a few customers or users, get feedback, and keep moving, without trying to become a product manager.
- **Choose the development approach deliberately:** Decide whether the moment calls for an MVP, robust architecture and scale, customer feedback, or researching the backend technology stack. Engineers who make some product and architecture calls steer the build end to end and contribute more.

**6. Match speed versus planning to the project stage**
- **Prototype quick and dirty early on:** Put an idea into a coding agent, build it, inspect the result, discard it when appropriate and build another to drive rapid learning. Do this safely: never leak sensitive data and guard against bad outcomes.
- **Plan carefully when the decision is a one-way door:** Use Jeff Bezos's one-way versus two-way door framing. For hard-to-reverse work, assess rewrite ratio, customer requirements, sensitive data and security infrastructure before building.
- **Shift the velocity and risk balance as the project matures:** Zero-to-one work and mature, systematic phases need different skills and speeds. Learning this stage-dependent judgment is hard, so name the stage explicitly before each piece of work.
- **Pick spec-first or overnight runs to fit the situation:** Sometimes write a long specification and fully plan the work. Other times, if you are going to sleep in 20 minutes, quickly start a coding agent, let it run for a few hours, and inspect its output in the morning.

**7. Protect your own learning**
- **Avoid cognitive offloading when the goal is learning:** Having a language model think for you gets more work done but teaches less; students using LLMs do better on homework but worse on final exams. Working adults using coding agents face the same risk.
- **Use AI in ways built for human development:** Most ways people use LLMs, like most social media use, do not produce learning. Choose learning experiences aimed at developing you, not just completing the task, and favor more personalized one-to-one formats as they appear.
- **Keep learning frontier topics and keep building:** Take courses on frontier tools such as the voice stack, generative UI and building local memory for agents, then apply them in your own projects.

**Try this first:** Write down the four AI-engineering skills, rate yourself on each, and for your next small idea start a coding agent before bed and review its output in the morning, checking which tradeoffs it chose for you.

**Caveat:** Ng leads DeepLearning.AI and is backing Learn Vector, which he promotes here, and his claims about learning research, job demand and agent capabilities are not independently verified.

## Derived summary
## [00:00:00] Infrastructure demand and agentic use
- [00:00:00] The guest says he is excited about the future of databases.
- [00:00:07] He describes a massive data-center buildout for AI training and inference.
- [00:00:18] **Prediction:** Core compute and storage infrastructure will increasingly be used by agents as well as humans.
- [00:00:27] **Prediction:** Agentic use of infrastructure will create massive additional demand.
- [00:00:38] The guest contrasts today’s databases, built largely for human use, with agents that could query far more data.
- [00:00:47] **Prediction:** Demand for core compute infrastructure will continue to skyrocket; the guest is bullish on the category.
- [00:00:57] The interviewer says builders and developers at a recent partner event were reporting that they were running out of compute.

## [00:02:17] Collaboration and the AI-engineering skills map
- [00:02:17] Asked how he keeps reinventing himself, the guest attributes his work to having collaborated with many great people across organizations.
- [00:02:55] The guest calls AI engineering one of the most exciting and rapidly growing professions at this moment.
- [00:03:03] He defines AI engineering broadly: not only people with that title, but software, frontend, backend, DevOps, and mobile practitioners who benefit from AI-engineering skills.
- [00:03:19] His team spent several months mapping the skills needed to do AI engineering well.
- [00:03:29] The team reviewed more than 10,000 job descriptions and postings.
- [00:03:34] The research also included dozens of structured interviews, surveys, and synthesized input from partners.
- [00:03:43] The resulting map identifies four key AI-engineering skills.
- [00:03:48] **Skill 1: Build and deploy AI applications.** The defining difference from non-AI applications is uncertainty.
- [00:03:54] AI engineers need to manage uncertainty in the behavior and outcomes of AI applications.
- [00:03:57] **Skill 2: Software-engineering fundamentals.**
- [00:04:01] Even when AI writes much of the code, people who understand engineering concepts can steer coding agents better.
- [00:04:07] Examples of foundational concepts named are rewrite ratio and transactions.
- [00:04:14] **Skill 3: Use coding agents.**
- [00:04:19] **Skill 4: Shape the build.** Developers increasingly help decide what to build and influence how it is built, rather than merely implementing assigned work.
- [00:04:36] The guest reports that people with AI-engineering skills, whether or not their formal title is AI engineer, are in great demand.
- [00:04:49] He says employers cannot find enough people with these skills.

## [00:05:27] Which work remains human work
- [00:05:27] The interviewer asks whether people should keep developing skills or whether agents will become capable enough to reduce that need.
- [00:05:30] The guest expects some current human tasks to be taken over by agents.
- [00:05:36] He recalls the prompt-engineering-job hype from roughly three years earlier.
- [00:05:47] Crediting Chris Manning, he says the need for humans to know “arcane incantations” for prompting was already expected to decline because AI could learn to produce them.
- [00:06:05] He gives managing a swarm of agents as an example of work that may partly be performed by humans now but may become increasingly agent-managed.
- [00:06:15] **Prediction:** AI agents will manage other AI agents better and better in coming years for more one-size-fits-all tasks.
- [00:06:23] The guest’s criterion for whether AI will take over a task is whether humans retain a fundamental context advantage.
- [00:06:33] In application work, humans know substantial context that agents do not know.
- [00:06:39] Examples of human context include remembering a customer conversation and a revealing facial expression.
- [00:06:47] Another example is recalling a market report from years ago and using it to infer what people want.
- [00:06:53] He characterizes humans as having a vast range of context and being good at retrieving it for key decisions.
- [00:07:02] He expects humans to continue making decisions where that fundamental context advantage remains.
- [00:07:07] He notes that reproducing all such context for AI, such as capturing facial expressions from every conversation, would be difficult.
- [00:07:17] The guest therefore expects a large set of context-advantaged tasks to remain human work for a long time.
- [00:07:21] He frames the goal as giving people skills to do that valuable work while complementing coding agents.
- [00:07:36] The guest says software-engineering job postings are rising as coding agents make engineers more productive.
- [00:07:45] His causal claim is that higher productivity makes businesses want more software and AI engineers, not fewer.

## [00:08:10] What distinguishes stronger AI developers
- [00:08:10] In building the skills map, the team repeatedly asked interviewees to compare a great developer with a less effective one.
- [00:08:32] The answers were distilled into the AI-engineering skills map; the guest emphasizes that the gap involves many different skills, not one or two.
- [00:08:42] He again highlights building and deploying AI applications as the first skill.
- [00:08:51] The key difference between AI applications and traditional software, according to the guest, is uncertainty.
- [00:08:59] When prompting a language model or training a supervised-learning algorithm, developers do not know the outcome in advance.
- [00:09:06] AI developers therefore use techniques to monitor system performance.
- [00:09:14] They use disciplined error-analysis and evaluation loops to improve systems systematically.
- [00:09:22] The skills map is intended to identify the many gaps between skilled and novice developers.
- [00:09:39] Its purpose is to support systematic progress from less skilled to expert-level capability across valuable AI-engineering skills.

## [00:09:58] How to use the skills map
- [00:09:58] The guest says DeepLearning.AI’s weekly newsletter, *The Batch*, covered only the AI-engineering skills map for five consecutive weeks.
- [00:10:11] He says other companies are looking at structuring curricula around the map.
- [00:10:17] For individuals, he positions the map as a way to understand both existing strengths and areas for improvement.
- [00:10:32] DeepLearning.AI is working to create learning paths that help people become skilled at AI engineering.
- [00:10:41] He says the broader education space still needs clearer paths for developing AI-engineering skills comprehensively.

## [00:11:26] Changing experience of coding with agents
- [00:11:26] Asked whether experienced developers are slowly shifting their work to agents, the guest says he personally does not miss coding by hand.
- [00:11:43] The interviewer contrasts agentic coding with the former experience of intensely working through a problem, consulting Stack Overflow, and eventually getting a solution to click after hours.
- [00:12:04] The interviewer observes that before AI, developers had lists of projects they wanted to complete but could not finish.
- [00:12:11] He says his project list became longer after AI made him more productive.
- [00:12:18] The guest says he has many projects he wants to work on but lacks time for, and that his ambitions may have grown faster than his capabilities.
- [00:12:34] He describes a new workflow: start a coding agent before bed and inspect its work the following morning.
- [00:12:43] He contrasts this with debugging unusual JavaScript syntax and says he prefers the new mode of work.

## [00:13:12] Stable fundamentals versus rapidly changing agent tools
- [00:13:12] The interviewer asks how a curriculum can be designed for a rapidly changing market.
- [00:13:14] The guest says the hype is that everything in AI changes every three months.
- [00:13:18] He says the fastest-changing part of the skills map is the use of coding agents.
- [00:13:25] He says the way people code now differs from both three and six months earlier.
- [00:13:30] By contrast, he says much of the knowledge for building, deploying, monitoring, updating, and steering AI applications changes more slowly than publicity suggests.
- [00:13:52] The guest says that, at least before “Astra,” most AI systems were not very good data scientists or AI engineers; he is uncertain whether Astra changes that assessment.
- [00:14:03] He says that when asked what to do on a project, AI systems often do not provide reliable engineering or data-science judgment.
- [00:14:08] He says he no longer does much data-science work manually, such as directly coding data-frame work, and instead uses AI agents for much of it.
- [00:14:20] However, he says those agents can make strange decisions and reach strange conclusions.
- [00:14:27] He hopes frontier models will improve.
- [00:14:29] He argues that engineering requires understanding fundamental tradeoffs.
- [00:14:35] Tradeoffs named include cost, latency, speed, and reliability.
- [00:14:48] Without fundamentals, the guest says people may not even know which tradeoffs are available.
- [00:14:54] His caveat about “vibe coding” is that a coding agent can make tradeoffs the user neither recognized nor intended, which may cause problems later.
- [00:15:04] He concludes that engineers who understand fundamentals make much better decisions.
- [00:15:16] He acknowledges that AI enables useful coding by people without deep understanding, but says experienced engineers still do vastly better work.

## [00:15:38] Shaping the build
- [00:15:38] The guest says that as implementation becomes easier, the bottleneck shifts toward deciding what to build.
- [00:15:48] AI assistance lets specialists cover more of the stack: for example, frontend engineers can do more backend work.
- [00:16:07] He describes developers broadening from narrower roles toward full-stack capability.
- [00:16:14] Beyond technical breadth, he says it is slow for a developer to wait for a product manager to collect customer feedback and decide the next direction.
- [00:16:25] The faster alternative is for a developer to have some product instinct, talk with a few customers or users, obtain feedback, and keep the process moving.
- [00:16:36] He sees developers expanding from implementation into deciding what to build.
- [00:16:44] This does **not** mean engineers should become product managers.
- [00:16:50] It does mean that engineers who can make some product and architecture decisions are more productive than engineers confined to a narrower role.
- [00:17:02] The guest calls this broader contribution “shaping the build.”
- [00:17:04] Shaping the build includes influencing product decisions and bringing product judgment to them.
- [00:17:12] It also includes choosing the appropriate development approach: build an MVP, invest in robust architecture and scale, seek customer feedback, or research the backend technology stack.
- [00:17:29] The intended outcome is that developers steer the build process end to end and contribute more to the overall project.

## [00:18:02] Prototype quickly or plan carefully: a stage-dependent decision
- [00:18:02] The guest says how much time to spend on upfront design is stage dependent.
- [00:18:09] He also says the choice depends substantially on what Jeff Bezos calls one-way versus two-way doors.
- [00:18:15] In early project stages, his directional advice is to put an idea into a coding agent, build it, and inspect the result.
- [00:18:24] He qualifies this by requiring safe, responsible use: do not leak sensitive data and protect against bad outcomes.
- [00:18:32] For early-stage work, he recommends quick-and-dirty prototypes, observing what happens, discarding them when appropriate, and building another prototype to drive rapid learning.
- [00:18:50] There is also a time for careful architecture work.
- [00:18:53] Careful planning includes assessing rewrite ratio, customer requirements, sensitive data, and security infrastructure.
- [00:19:06] The guest distinguishes engineers strong at zero-to-one startup work from engineers strong in mature, systematic phases.
- [00:19:18] As a project matures, the appropriate skills, speed, and balance between velocity and downside-risk protection change.
- [00:19:27] He says the same stage dependence applies to coding agents.
- [00:19:30] Writing a long specification and fully planning the work has a place.
- [00:19:36] In other situations, if one is about to sleep in 20 minutes, it may be appropriate to quickly start work and let a coding agent run for a few hours, then inspect the output in the morning.
- [00:19:45] He says learning this stage-dependent judgment has been difficult for people.

## [00:20:27] Learning, cognitive offloading, and personalized education
- [00:20:27] The interviewer asks how learning may change over the next 10 years.
- [00:20:27] The guest predicts that learning will change.
- [00:20:33] He makes the deliberately provocative claim that chatbots are terrible for learning, while also stating that he likes and frequently uses language models.
- [00:20:46] He says that in university and K-12 contexts, students using language models do better on homework but worse on final exams.
- [00:20:55] He says increasingly rigorous studies support the concern that cognitive offloading reduces learning, though this characterization of the research is not independently verified here.
- [00:21:03] He defines cognitive offloading as having a language model think for the student: more work gets done, but less is learned.
- [00:21:14] He says the problem is likely underestimated among working adults, not only students.
- [00:21:24] Speaking personally, he says coding agents enable him to get much work done while reducing the thinking he has to do.
- [00:21:34] He clarifies that there are ways to use AI that improve learning.
- [00:21:40] His analogy is that TikTok can be used well for learning, but most use of social media does not produce learning.
- [00:21:50] He similarly claims that most ways most people use language models do not result in learning.
- [00:21:56] He says there is an opportunity to do better through learning experiences aimed at human development rather than merely task completion.
- [00:22:01] He names Coursera, Udemy, DeepLearning.AI, and Learn Vector as teams working toward new learning experiences.
- [00:22:18] He contrasts Silicon Valley’s focus on accelerating AI development with his interest in accelerating human development.
- [00:22:25] He describes Learn Vector as a recently announced company, with Coursera as an initial investor, and says he is excited about its human-development focus.
- [00:22:40] He says the effort aims to operate Learn Vector as a “frontier human development lab.”
- [00:22:51] Looking back roughly 15 years, he says Coursera helped change education through one-to-many courses.
- [00:23:00] He says the one-to-many model still works: one course is created and many people take the same or similar course.
- [00:23:10] He says current technology enables more one-to-one learning experiences and predicts they will be better.
- [00:23:18] He says Learn Vector had not yet announced its exact products, but he is optimistic based on internal prototypes and expects more information in coming months.

## [00:23:32] Closing advice and workflow preferences
- [00:23:32] Asked how people should spend four weeks upskilling as AI developers, the guest says DeepLearning.AI focuses on helping developers become skilled or more skilled in AI engineering.
- [00:24:10] He says he takes DeepLearning.AI courses himself to learn frontier tools.
- [00:24:19] Topics he names include the voice stack, generative UI, and building local memory for agents.
- [00:24:27] He says he sees areas where DeepLearning.AI could improve, but that much of his own learning has been through it.
- [00:24:43] His concise closing exhortation is to keep building.
- [00:24:47] He says he sometimes wakes in the middle of the night to check on coding agents.
- [00:24:59] He says coding on a phone has been wonderful, with some hesitation about its downsides.
- [00:25:09] He says he uses text more than voice to interact with coding agents.

## [00:25:39] Closing aside
- [00:25:39] **Aside:** The guest adds that he is a proud father of two children and leaves to pick them up from school.

## [00:26:04] Recap
- [00:26:04] The guest’s central model of AI engineering has four parts: build and deploy uncertain AI applications, retain software-engineering fundamentals, use coding agents, and shape the build.
- [00:26:04] His practical principle is stage-dependent judgment: prototype quickly and safely to learn early, while applying deliberate architecture, security, requirements, and risk management when the project warrants it.
- [00:26:04] His human-complementarity argument is that people retain value where they have context agents do not, especially when making product, architecture, and tradeoff decisions.
- [00:26:04] His education warning is that task completion via cognitive offloading may undermine learning; his proposed direction is more personalized, human-development-oriented learning experiences.

*Source-attribution note: These are claims, observations, and predictions made in the interview. Research characterizations, market-demand statements, tool capabilities, and future projections are not independently verified here.*

## Evidence anchors
- [00:00:07.759] I feel like right now the world is going
- [00:00:10.480] through a massive data center buildout
- [00:00:13.120] with a lot of AI training and inference
- [00:00:22.400] future a lot of core infrastructure be
- [00:00:27.680] just by humans but by agents and that

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
