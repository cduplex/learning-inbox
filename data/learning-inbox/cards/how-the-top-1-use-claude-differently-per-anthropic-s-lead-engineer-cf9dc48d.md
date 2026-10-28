# How the Top 1% Use Claude Differently (per Anthropic's Lead Engineer)

## Source
- Original: https://www.youtube.com/watch?v=NarezKh3w4o
- Type: youtube
- Creator: {'displayName': 'Jay E | RoboNuggets'}
- Published: 2026-10-17T00:00:00.000Z

## Tags
AI agents, Claude, prompting, agentic AI, business workflows, outcome-oriented prompting, expert validation, multi-agent systems, self-efficacy

## Learning guide
**The arc**
Most people use Claude for small, narrow tasks while a few are "flying" with it, and Felix Rieseberg (lead engineer on the Claude app) says the difference is being more ambitious, like the student who solved two unsolved statistics problems because he thought they were homework. The video breaks ambition into three types: altitude (ask for the outcome), depth (work like a top expert), and range (pull in perspectives from other fields). It closes by tying all three to self-efficacy, plus a reminder to pace yourself and keep a clear why.

**1. Altitude: ask for the outcome, not the task**
- **Ask what the task is for:** Before handing Claude a task, ask what you actually want to happen next, or the goal beyond the immediate goal. A task prompt only makes Claude execute your current best guess at reaching the real goal.
- **Turn one-off fixes into durable workflows:** Instead of asking Claude to fix app crashes one at a time, ask it to keep the apps crash-free. This builds a durable workflow that takes you out of the loop instead of assigning tasks one by one.
- **Let the goal choose the format:** For a client pitch deck, filling in your slide template works, but if the real goal is to impress the client, ask for that. Claude might then build an explorable 3D world of a venue the client can walk through, or interactive HTML slides that animate and clearly show the planned delivery.
- **Use altitude for definable outcomes:** It works best when the end state is clear and checkable, like crash-free apps. Goals needing creativity, such as "go make money and not make any mistakes", still need substantial human creativity, though more capable models may handle higher abstraction over time.

**2. Depth: make the work match expert practice**
- **Don't settle for "act like a professional":** That prompt often changes only vocabulary, adding jargon without changing methods. Push for how experts actually work instead.
- **Insist on the tools the best practitioners use:** For a company like Acme losing customers to churn before a quarterly review, think of the experts involved: a customer-success manager, a pricing strategist, and for large-scale churn reduction, a data scientist. If Claude jumps to a simple table in chat, challenge it on whether that is really the toolset the best people in the field would use; you don't need to know the toolset yourself, since the model usually does.
- **Set targets that sound unreasonable:** If a site loads in 10 seconds and the target is 5, ask whether Claude can hit 1 second or even 200 milliseconds. If it says that's impossible, tell it the problem is solvable and to keep going.
- **Use an outside judge for important work:** Don't let the model grade its own output, because many models are agreeable and can be talked into agreeing with you after a few prompts. Ideally give it a tool to call, like running a speed test after every change; for creative work, use a sub-agent acting as a judge to refine the final output.
- **Use one prompt to get most of the depth:** Before work begins, ask Claude: what would a top professional do here that I didn't request? What is the rawest material they would start from, and what methods and tools would they use? What, other than me or you, would demonstrate the result is correct? Then have Claude rewrite your original prompt to include those elements.

**3. Range: bring in other fields' perspectives**
- **Look sideways for unknown unknowns:** Range means viewing the work through other disciplines to surface options you didn't know existed. Felix saw a colleague render interior designs in Blender (free 3D software) and realized he could have Claude build 3D environments for his own website.
- **Replace nouns with verbs:** From *The Art of Innovation*: describe the output as an action, not an object. A "PowerPoint presentation" for a quarterly review becomes "getting busy people to believe a story about cause and effect and to decide under uncertainty in 30 minutes", which clarifies the goal and reveals useful disciplines.
- **Assemble the crew:** Like a heist-movie team, tell Claude to bring multiple roles via sub-agents instead of only its own view. For a quarterly review: an analyst, a sales manager, and a graphic designer if it will be presented.
- **Add a red team:** Include a devil's-advocate perspective whose job is to find holes in the work.
- **Save crews for what matters:** Deploying many helpers is token-intensive, so reserve it for your most important work.
- **See it applied end to end:** A real-estate agent whose house sale is crucial to the yearly revenue target swaps "generate a listing" for "help a family imagine life in the house before visiting." That points to an interior designer staging each room, a 3D artist making a walkthrough, and a local who knows nearby restaurants, producing a tailored listing page instead of a generic one.

**4. Self-efficacy: believe you can pull it off**
- **Believe it's possible:** Self-efficacy is how much you believe you can succeed, and raising it improves your chances, especially with AI. Like the student who solved "homework" that was actually unsolved, start from the assumption that it can be done.
- **Watch someone else do it:** Nobody ran a sub-4-minute mile until Roger Bannister did in the 1950s, and someone else did it days later. Seek out examples of people achieving what you're attempting.
- **Give yourself permission to fail:** Ship work, put it out publicly, and improve each round until it succeeds.
- **Pace yourself and keep your why:** Abilities can now leap every few weeks, but ambition without a clear reason just means accelerating aimlessly. Remember why the work matters and pause when needed.

**Try this first:** Take the next task you were about to give Claude, run the depth prompt (what would a top professional do that I didn't ask for, what raw material and tools would they use, and what outside of us would prove it correct), and have Claude rewrite your request before it starts.

## Derived summary
## Source-attribution note
- The video presents Jay's summary of ideas attributed largely to Felix Rieseberg, described as Anthropic's lead engineer for the Claude app. Claims about model behavior, research, historical anecdotes, and effectiveness are source claims and are not independently verified here. [00:00:16]

## Framing: ambition with AI [00:00:00]
- [00:00:00] The opening anecdote says that in 1939 a student copied two board problems, mistook them for homework, submitted answers the next day, and had solved two previously unsolved statistics problems because he did not know they were unsolved.
- [00:00:16] Jay attributes to Felix Rieseberg the view that this is the mindset of the top 1% of agentic-AI users.
- [00:00:24] Jay says Felix's article, *How to Be More Ambitious, a Tutorial for Humans with Models*, has over 4.5 million views on X.
- [00:00:31] The video promises three methods for becoming more ambitious with AI, contrasting typical usage with a claimed top-1% version for business use with Claude.
- [00:01:02] Jay describes Felix as having led engineering for the Claude app, Cowork, and the Claude Code desktop app, and says Felix observed that some people are "flying" with AI while others struggle to use it effectively.
- [00:01:19] Felix's concise prescription is "be more ambitious," but the video treats that as overly general and divides it into three types: altitude, depth, and range.

## Altitude: ask for the outcome rather than the task [00:01:39]
- [00:01:39] Altitude means operating at a higher abstraction level: ask for the desired outcome rather than a specific task.
- [00:01:52] The causal rationale is that a task prompt merely directs Claude to execute the user's current best guess about how to achieve the real goal.
- [00:01:58] Felix's prompting question is: what do you actually want to happen next, or what is the goal beyond the immediate goal?
- [00:02:04] Felix's example shifts from asking Claude to fix application crashes one at a time to asking it to keep the apps crash-free.
- [00:02:14] The claimed result is a "durable workflow" that more effectively removes the human from the loop, rather than requiring a sequence of individually assigned tasks.
- [00:02:25] For a business task, the suggested diagnostic is to inspect the task about to be handed to Claude and ask what the task is actually for.
- [00:02:30] Example: with a client pitch deck and an existing slide template, the conventional request is to have Claude fill in the slides.
- [00:02:39] Jay says slide filling works for many use cases, but the higher-level goal may instead be to impress the client.
- [00:02:44] Given the goal of impressing a client, the model could choose a different format, such as an explorable 3D world for a venue that the client can walk through.
- [00:02:55] Another proposed alternative is interactive HTML slides that can animate and clearly show the planned delivery, rather than a conventional PowerPoint slide pack.
- [00:03:02] Altitude is presented as working best for an ultimate, definable outcome, such as keeping applications crash-free.
- [00:03:10] The video cautions that current models work less well when the goal requires creativity.
- [00:03:16] The example "go make money and not make any mistakes" is said not to work by itself for most businesses in 2026, because substantial human creativity is still needed.
- [00:03:27] Felix predicts that more capable models may handle progressively higher abstraction levels, though the video leaves this as a future possibility.

## Depth: make the work resemble expert practice [00:03:55]
- [00:03:55] Depth concerns doing a task extremely well, in the manner of a leading expert in the relevant field.
- [00:04:07] The stated trap is that asking a model to "act like a professional" may only alter vocabulary: it uses jargon without changing its methods.
- [00:04:17] The video introduces three depth techniques through a hypothetical company, Acme, which loses customers monthly, or experiences churn, and needs to prepare for a quarterly review.

### Use the tools experts would use [00:04:31]
- [00:04:31] The first depth technique is to insist on the same tools used by the best practitioners in the industry.
- [00:04:35] For Acme's churn problem, the video argues that Claude would need access to the tools that experts themselves use.
- [00:04:42] Relevant expert perspectives for churn might include a customer-success manager, a pricing strategist, and, for large-scale churn reduction, a data scientist.
- [00:04:51] If Claude reaches immediately for a simple table in chat, the suggested response is to challenge whether that is truly the toolset that the best people in the field would use.
- [00:05:01] Jay claims users need not already know the expert toolset because models, including Claude, usually know it.

### Set more demanding performance goals [00:05:07]
- [00:05:07] The second technique is described as choosing goals that sound unreasonable, then asking the model to attempt them.
- [00:05:12] Example: if a website currently loads in 10 seconds and the stated target is 5 seconds, the video advises asking whether Claude can reach 1 second or even 200 milliseconds instead.
- [00:05:21] If Claude says that target is impossible, Felix's reported advice is to tell it the problem is solvable and to keep going.

### Use an outside judge [00:05:28]
- [00:05:28] The third technique is outside judgment: do not ask the model to judge its own work for the most important tasks.
- [00:05:36] The rationale offered is that many current AI models are agreeable and can be persuaded after relatively few prompts that a user's claim is correct.
- [00:05:45] Felix expects this weakness to be solved as models improve, but recommends external validation for now.
- [00:05:51] Ideally, the external validator is a tool the model can call. For website performance, the example is a speed test run after every change.
- [00:05:59] For more creative work, the video says a sub-agent acting as a judge has been shown by multiple independent tests to help refine final output.
- [00:06:07] Jay says much of this depth method can be achieved through a single prompt.
- [00:06:17] Felix's prompt asks, before work begins: what a top professional would do that the user did not request.
- [00:06:23] It also asks for the rawest material the professional would start from, and the methods and tools they would use.
- [00:06:28] Finally, it asks what, other than the user or Claude, would demonstrate that the result is correct; the model then rewrites the original prompt to request those elements.

### Promotional aside [00:06:42]
- [00:06:42] Jay briefly promotes the Robo Nuggets community, describing a weekly updated Claude masterclass, an "Agents as a Service" course, and a community for AI builders.

## Range: combine perspectives across fields [00:07:15]
- [00:07:15] Range is the third component. Altitude takes a high-level view and depth pushes one task toward maximum quality; range looks sideways by viewing work through other fields' perspectives.
- [00:07:31] The video says this can bring more perspectives than would previously have been practical.
- [00:07:37] A heist-movie crew serves as the analogy: several people with distinct talents are assembled, and agents can similarly split a job among several helpers.
- [00:07:52] For important tasks, the sub-agents should have varied viewpoints to expose "unknown unknowns": options or considerations the user did not know existed.
- [00:08:05] Felix says range is not easy because it requires creativity.
- [00:08:10] His example is seeing a colleague use Blender, free 3D software, to render interior designs, which led him to consider using Claude to build 3D environments for his own website.
- [00:08:20] This Blender example is framed as an unknown unknown: an option that was not considered at the outset.

### Replace nouns with verbs [00:08:26]
- [00:08:26] The first range technique, attributed to *The Art of Innovation*, is to replace nouns with verbs.
- [00:08:37] In the quarterly business review example, "PowerPoint presentation" is the noun-focused description of the output.
- [00:08:47] The corresponding verb-focused description is "getting busy people to believe a story about cause and effect and to decide under uncertainty in 30 minutes."
- [00:08:58] Framing the work as verbs is said to clarify the actual goal and reveal disciplines that might provide a distinctive, useful viewpoint.

### Assemble a crew of roles [00:09:08]
- [00:09:08] The follow-up technique is to "assemble the crew": insist that Claude bring multiple roles and viewpoints rather than relying only on its own perspective.
- [00:09:17] For a quarterly review, the proposed roles include an analyst, a sales manager, and, when the work will be presented, a graphic designer.
- [00:09:25] The video also recommends adding a red-team perspective. It defines red teaming as finding holes in the work, like a devil's-advocate group.
- [00:09:38] The stated tradeoff is that deploying helpers can be token-intensive, so this approach is positioned for the most important work.

### Real-estate example [00:09:47]
- [00:09:47] The video applies range to a real-estate agent whose sale of a house is crucial to meeting the year's revenue target.
- [00:09:55] The ordinary noun-focused request is to generate a real-estate listing.
- [00:10:01] The verb-focused goal is helping a family imagine life in the house before visiting it.
- [00:10:09] This reframing clarifies the mixture of experts to involve.
- [00:10:13] Suggested roles include an interior designer to stage each room, a 3D artist to make a walkthrough, and a local who knows nearby restaurants.
- [00:10:27] The intended result is a listing page tailored to the important project rather than a generic real-estate page.

## Self-efficacy and recap [00:10:35]
- [00:10:35] After recapping altitude, depth, and range, the video says Felix connects them to self-efficacy, defined as how much a person believes they can pull something off.
- [00:10:49] The video claims that increasing self-efficacy, especially with AI available, increases one's chances of success in a chosen field or game.
- [00:10:56] Jay says self-efficacy can be "hacked" and attributes three documented methods to more than 35 years of goal-setting studies.
- [00:11:11] First: believe an achievement is possible. The example returns to George Dantzig allegedly solving two unsolved statistics problems because he believed they were homework.
- [00:11:21] Second: watch someone else do it. The example says nobody had run a mile under 4 minutes until Roger Bannister did so in the 1950s, after which someone else did it a few days later.
- [00:11:32] Third: give yourself permission to fail. The proposed mechanism is to ship work, put it out publicly, and improve each time until eventual success.
- [00:11:42] Felix's concluding view, as relayed by Jay, is that self-efficacy is not new but is more powerful now because human abilities can make leaps every few weeks, enabling greater ambition in what people bring to the world.
- [00:11:58] Jay adds a counterpoint: AI-related ambition needs pacing and a clear "why," otherwise people may accelerate and become more ambitious without a clear reason.
- [00:12:12] Final recap: use the techniques to become more ambitious with powerful AI agents, but remember why the work matters and pause when needed.

## Evidence anchors
- [00:00:00.000] In 1939, a student turned up late to a
- [00:00:08.520] next day. They were two unsolved
- [00:00:16.840] lead engineer of the Claude app at
- [00:00:24.200] article on it called how to be more
- [00:01:00.680] communities globally. So Felix Riesberg

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
