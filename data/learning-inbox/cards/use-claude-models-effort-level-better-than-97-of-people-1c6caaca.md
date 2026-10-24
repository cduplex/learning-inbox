# Use Claude Models & Effort Level Better Than 97% of People

## Source
- Original: https://www.youtube.com/watch?v=BZluE67z1MA
- Type: youtube
- Creator: {'displayName': 'Austin Marchese'}
- Published: 2026-10-23T00:00:00.000Z

## Tags
Claude, AI models, model selection, effort levels, compute cost, parameters, transformers, automation, AI planning, distillation, Jevons paradox, video notes

## Derived summary
# Study Notes

## 00:00–03:03 : Model lineup, size, parameters, and compute

- **[00:00:00]** The presenter frames Claude as a configurable host of models rather than one AI, claiming effective use depends on selecting an appropriate model and effort level. *This framing is the presenter's claim and is not independently verified.*
- **[00:00:21]** The presenter says the video will first establish the four-model lineup, their origin story, and how they work.
- **[00:00:28]** The presenter identifies four Claude models: **Haiku, Sonnet, Opus, and Fable**. *The lineup and names are source claims, not independently verified.*
- **[00:00:32]** The stated main distinction is model size: each model is characterized as a different-sized “brain,” from smallest to largest.
- **[00:00:40]** The presenter interprets the names as size-related Easter eggs: a haiku has **three lines**, a sonnet has **14 lines**, an opus is described as a whole book, and Fable is linked to a supposed Mythos class meaning a world of stories.
- **[00:01:03]** The presenter introduces an office-building analogy for model size.
- **[00:01:06]** In that analogy, every sentence travels through a building; everyone on every floor reads it and adds a note before output.
- **[00:01:12]** Haiku is compared with a **10-person office**, while Fable is compared with a skyscraper.
- **[00:01:19]** The presenter says passing the same sentence through a larger building means more “people” work on it.
- **[00:01:26]** Haiku is analogized to a sharp intern: fast, cheap, and good at clearly defined tasks.
- **[00:01:32]** Fable is analogized to a senior expert: it supposedly knows more and catches omissions, but has a much higher hourly rate.
- **[00:01:44]** The presenter equates the people in the building analogy with **parameters**.
- **[00:01:48]** Parameters are said to determine what a model knows.
- **[00:01:52]** Training and fine-tuning are explained through a knob analogy: each parameter is a knob that can be adjusted to alter output.
- **[00:02:00]** Smaller models are said to have fewer knobs to tune, while bigger models have more.
- **[00:02:07]** Training example: show the model “the cat sat on the blank”; if it guesses incorrectly, nudge a parameter toward the right answer.
- **[00:02:16]** The presenter says this adjustment process is repeated trillions of times across billions of scenarios to train and fine-tune parameters.
- **[00:02:24]** The presenter says a larger model does **not** necessarily use more tokens for the same sentence.
- **[00:02:30]** Instead, the stated difference is compute cost per token; the same text is roughly the same token count across models.
- **[00:02:40]** Usage limits are characterized as compute-budget limits rather than purely token limits.
- **[00:02:44]** The presenter offers the mental formula: **compute used = tokens × model**.
- **[00:02:50]** Citing an Anthropic price sheet, the presenter claims Haiku is about **40× cheaper than Opus** and about **100× cheaper than Fable**. *Pricing and comparative figures are source claims, not independently verified.*
- **[00:02:56]** The building analogy is restated: processing through the Fable “skyscraper” costs more compute than processing through the Haiku “10-person office.”

## 03:03–06:36 : Haiku, Sonnet, Opus, and release types

- **[00:03:12]** Haiku is described as an “intern worker bee,” designed for speed and cost-effectiveness.
- **[00:03:19]** The stated Haiku tradeoff is depth: the presenter says it will not handle tasks requiring substantial judgment.
- **[00:03:26]** The presenter says users may not directly select Haiku often because larger models may invoke it.
- **[00:03:31]** Citing Anthropic documentation, the presenter says Haiku is suitable for **sub-agent tasks**, in which a larger model delegates a specific subtask to Haiku. *This documentation characterization is not independently verified.*
- **[00:03:40]** Haiku is framed as the model other models “hire” for specific tasks.
- **[00:03:44]** Sonnet is described as a contractor that needs a blueprint.
- **[00:03:48]** The presenter says a prior consensus was to use Sonnet by default and reserve Opus for harder tasks.
- **[00:03:54]** The presenter argues that Sonnet has become a “middle child” because Opus has improved and become more cost-effective. *This market/usefulness assessment is the presenter's opinion.*
- **[00:04:03]** The presenter says Sonnet is neither the cheapest nor, in the presenter's view, necessarily the best everyday pick.
- **[00:04:05]** The presenter attributes this split to Anthropic: Opus is for complex work requiring careful judgment.
- **[00:04:09]** Sonnet is described as strongest for well-scoped everyday work, bug fixing, and polished documents, slides, and spreadsheets.
- **[00:04:17]** The presenter emphasizes **well-scoped** as the key condition for Sonnet.
- **[00:04:23]** A quoted team member says they use “Opus 5.5” for critical thinking and planning, and “Sonnet 5.5” for the execution or legwork. *Model-version claims are not independently verified.*
- **[00:04:31]** The presenter summarizes that workflow as: Opus decides what to build; Sonnet builds it:architect versus contractor.
- **[00:04:37]** Opus is introduced as the expert model.
- **[00:04:43]** The presenter quotes alleged Anthropic documentation: if unsure which model to use, start with **Claude Opus 5.5** for most workloads. *This alleged quotation is not independently verified.*
- **[00:04:51]** The presenter claims Opus is the Claude Code default on every paid plan and says this changed after the 5.5 upgrade. *Not independently verified.*
- **[00:05:07]** The presenter distinguishes two release types: a **point release** and a **generational jump**.
- **[00:05:13]** A point release is exemplified as **5.4 → 5.5**.
- **[00:05:19]** Point releases are likened to refurbishing and restaffing the same building.
- **[00:05:24]** Technically, the presenter says a point release retains the same base model but adds more post-training.
- **[00:05:28]** Opus 5.5 is characterized as a point release.
- **[00:05:32]** A generational jump is exemplified as **4.5 → 5.5**.
- **[00:05:37]** A generational jump is likened to demolishing a building and constructing a new one with a new foundation, possibly greater height, better materials, and a smarter layout.
- **[00:05:48]** Technically, a generational jump is described as a new base model trained from scratch.
- **[00:05:52]** The presenter claims Haiku had a **4.5 → 5.5** release at the time of recording. *Not independently verified.*
- **[00:05:56]** The presenter says upgrades typically make models faster, smarter, and cheaper.
- **[00:06:01]** The presenter claims Opus 5.5 became **30% faster** and **40% cheaper**. *Not independently verified.*
- **[00:06:07]** The presenter calls the alleged updated Opus pricing/capability balance a “Goldilocks zone”: not as cheap as Haiku, but not overkill like Fable.
- **[00:06:24]** For most people, the presenter recommends using the newest open/default model rather than overthinking model selection; at recording, the cited default is Opus 5.5. *This is a presenter recommendation, not an established fact.*

## 06:36–08:30 : Transformer claim and sponsor segment

- **[00:06:43]** The presenter says every Claude model is a transformer model.
- **[00:06:46]** Transformers are simplistically described as models trained to guess the next word in a sequence.
- **[00:06:50]** The presenter claims transformer models cannot generate images. *This broad technical statement is a source claim and is not independently verified.*
- **[00:06:54]** The video transitions into a sponsorship for “AI Cohere” / “AI Coauthor”; the product name is inconsistent in the supplied captions.
- **[00:06:59]** The presenter describes short-form dramas as **60–90-second vertical episodes** ending with cliffhangers.
- **[00:07:07]** The presenter claims YouTube received **6.5 billion views** for these dramas in the first half of the year, up **50%** from the previous year. *Not independently verified.*
- **[00:07:16]** The stated problem with many AI video tools is that they produce a collection of **8-second clips**, leaving assembly into an episode to the user.
- **[00:07:23]** The sponsor’s “cinema agent” is said to have launched a “drama mode” intended to address that assembly problem. *Product capability claim, not independently verified.*
- **[00:07:29]** The presenter describes a workflow: choose **film/series**, enter a one-sentence premise, and select **short drama**.
- **[00:07:32]** The example premise is: a waitress recognizes a new regular as the man who ruined her family.
- **[00:07:39]** The presenter says the tool shows the price before generation, so users know how many credits they will spend. *Not independently verified.*
- **[00:07:44]** The presenter says one click creates a full episode and runs the production workflow.
- **[00:07:50]** Claimed production steps include creating characters and locations, splitting the story into scenes, and editing the result together. *Not independently verified.*
- **[00:08:03]** The presenter says generated videos include dialogue and sound, so characters speak rather than appearing in silent clips. *Not independently verified.*
- **[00:08:12]** The presenter says an uploaded script can run through the same pipeline. *Not independently verified.*
- **[00:08:24]** The sponsor call-to-action mentions a first description link, code **Austin**, free starting access, and **10 additional credits** at sign-up. *Promotional claim, not independently verified.*

## 08:30–10:16 : Fable, Mythos, stamina, and model-selection examples

- **[00:08:33]** The presenter returns to Fable and effort level after the sponsor segment.
- **[00:08:39]** Fable is characterized as a specialist that can be left to work independently.
- **[00:08:42]** The presenter says understanding Fable requires understanding a higher model class called Mythos.
- **[00:08:45]** The presenter claims Anthropic built Mythos above Opus, but its cyber capabilities were too risky for general release. *This entire Mythos/Fable account is not independently verified.*
- **[00:08:50]** The presenter says Mythos was “banned” and not allowed out.
- **[00:08:54]** The presenter says Fable was created as the generally available class instead.
- **[00:08:58]** Fable is described as having a similar underlying model plus additional safety measures around biology, cybersecurity, and AI research.
- **[00:09:04]** The presenter quotes a description of “Claude Fable 5” as a Mythos-class model made safe for general use.
- **[00:09:09]** The presenter attributes to Anthropic the claim that Mythos-class models sit above Opus-class models in capability.
- **[00:09:15]** Fable is said to be for complex, multi-step work in which early decisions affect later ones.
- **[00:09:24]** A quoted team member gives the rationale: a small error in step **two** can disrupt work at step **40**; “Fable 5.1” is said to remain reliable throughout. *Not independently verified.*
- **[00:09:32]** The presenter says the frontier-model race is shifting from intelligence toward **stamina**: how long a model can work autonomously while remaining correct.
- **[00:09:45]** The presenter says Opus can match Fable on many tasks, but Fable is preferable for the longest and hardest runs where stamina matters most.
- **[00:09:53]** The presenter gives reasons not to use Fable constantly: it is slower, consumes more usage, and may route sensitive requests to Opus.
- **[00:10:04]** Fable is framed as a premium specialist for problems that genuinely need one.
- **[00:10:25]** The presenter’s everyday rule of thumb is to use Opus by default and move to Fable for specifically complicated work. *Presenter recommendation.*
- **[00:10:35]** Technical examples of “complicated” work: full complex-system design with locked-in early decisions, and a large codebase migration.
- **[00:10:45]** Nontechnical examples: robust competitor analysis, a company roadmap, and a multi-quarter budget model where an early assumption affects downstream work.
- **[00:10:55]** The presenter attributes a task split to Anthropic: unconstrained/open-ended work versus constrained/routine work.
- **[00:11:02]** The presenter says open-ended work should bias toward larger models, while routine work should bias toward smaller models.

## 11:09–13:53 : Automation optimization, planning, and effort settings

- **[00:11:09]** For Claude routine automations, the presenter says a matching prompt can help identify a task’s **minimum viable model**.
- **[00:11:19]** The minimum viable model is defined as the model that completes the job while saving the most tokens.
- **[00:11:27]** The presenter labels this model-matching exercise an optimization rather than a necessity.
- **[00:11:31]** Clear instructions are emphasized as valuable regardless of model selection.
- **[00:11:35]** The causal claim is: a clear plan produces fewer retries, fewer wrong turns, and fewer tokens spent guessing the user’s intent.
- **[00:11:49]** For robust planning tasks, the presenter suggests using Fable for planning and then downgrading to Opus or Sonnet for execution. *Presenter suggestion.*
- **[00:12:01]** The analogy is to use a senior employee for high-leverage planning and a more junior employee for execution/grunt work.
- **[00:12:12]** The presenter attributes to Anthropic the advice that tuning effort is often a better lever than switching models.
- **[00:12:26]** The office analogy is extended: the model is who is hired; effort is how long that worker is allowed to work.
- **[00:12:35]** The Claude Code team is quoted: low-effort Opus is like five minutes with an expert, while high-effort Sonnet is like giving a capable generalist a whole afternoon. *Not independently verified.*
- **[00:12:46]** Higher effort is said to make Claude work harder and consume tokens faster.
- **[00:12:53]** Effort is said not to alter the model itself; it changes how much activity the model may perform.
- **[00:13:04]** **Medium** is identified as the claimed Claude default and recommended for everyday tasks.
- **[00:13:08]** **High** is recommended for work where mistakes can hide, including bugs, edge cases, and work users do not want to double-check.
- **[00:13:15]** **Max** is described as allowing Claude to run a genuinely hard task end-to-end on its own.
- **[00:13:21]** The presenter says Anthropic warns max effort may have diminishing returns and can cause overthinking. *Not independently verified.*
- **[00:13:29]** “Ultra code” is distinguished from an effort level, despite appearing on the effort bar.
- **[00:13:37]** Ultra code is described as a separate Claude Code mode that distributes a large job across agents working in parallel and checking each other’s work. *Not independently verified.*
- **[00:13:46]** Suggested Ultra code use cases are auditing an entire codebase and deep research; the presenter warns it consumes substantial usage.

## 13:57–15:48 : Misconceptions, tradeoffs, and diagnostic test

- **[00:13:57]** The presenter introduces three misconceptions about effort level.
- **[00:14:05]** Misconception 1: max effort upgrades a model into a better model.
- **[00:14:10]** The correction offered is that max-effort Sonnet does not become Opus; it is compared with giving the same junior employee more time rather than replacing them with a senior employee.
- **[00:14:21]** Misconception 2: low effort makes AI “dumb.”
- **[00:14:23]** The presenter says low effort does not change what the model knows; it commits to an answer sooner and may ask for context instead of investigating independently.
- **[00:14:31]** Misconception 3: selected effort is a minimum level of work.
- **[00:14:33]** The presenter says effort is instead a **ceiling** on work.
- **[00:14:38]** Human-work analogy: telling someone not to spend more than **2 hours** does not require them to use the full two hours; they could finish in **20 minutes**.
- **[00:14:46]** Effort is described as permission to spend up to an amount of time, not an order to do so.
- **[00:14:52]** The presenter explains why max should not always be used: if someone may take up to **5 hours**, they will likely take more time than if asked to finish in **30 minutes**.
- **[00:15:02]** The equivalent claimed AI behavior is a bias toward spending more time when more effort is allowed, even when that is unnecessary.
- **[00:15:07]** Another higher-effort tradeoff is that Claude may make more assumptions on the user’s behalf.
- **[00:15:10]** Example: if there are **10** unanswered questions, higher effort may lead the model to answer them itself rather than ask for clarification.
- **[00:15:25]** The presenter offers a two-question diagnostic, attributed to Anthropic guidance, for deciding between a better model and higher effort.
- **[00:15:27]** Diagnostic question 1: did Claude have everything it needed and still get the answer wrong?
- **[00:15:32]** If yes, the presenter says the model likely did not know enough, so use a better model.
- **[00:15:35]** Diagnostic question 2: did the model skip a file, skip a test, or stop halfway through the process?
- **[00:15:39]** If yes, the presenter says it did not try hard enough, so increase effort.

## 15:50–16:22 : Channel promotion

- **[00:15:50]** The video includes an “anti-slop agreement” described as content built by humans for humans.
- **[00:15:56]** The presenter asks viewers to subscribe and enable post notifications.
- **[00:16:06]** The presenter says they give away a Claude Max subscription in every video and names “SV2 Dev” as this video’s winner. *Not independently verified.*
- **[00:16:12]** SV2 Dev is described as building an agent-first CMS sync service.
- **[00:16:15]** The presenter says viewers can enter the giveaway by commenting on what they are building and problems they face.

## 16:22–19:37 : Forecast, distillation, Jevons paradox, and recap

- **[00:16:22]** The presenter turns to a forecast about future model and effort controls.
- **[00:16:27]** Manual selection of model and effort is compared with manually driving a car and changing gears.
- **[00:16:35]** Automatic transmission is used as the analogy for a future system that automatically selects model and effort.
- **[00:16:45]** The presenter claims ChatGPT has already moved in this direction by merging model and effort controls. *Not independently verified.*
- **[00:16:53]** The presenter lists an alleged left-to-right ChatGPT interface sequence: “Luna high,” “Soul light,” “medium,” and “Astra light and medium.” *Not independently verified.*
- **[00:17:02]** A quoted head of ChatGPT and Codex says even they experience fatigue from model pickers, reasoning efforts, multi-agent/ultra choices, and the complexity of understanding them. *Identity, quotation, and claims are not independently verified.*
- **[00:17:23]** The presenter predicts that by **2027**, model and effort selection will be abstracted away across tools, including Claude. *Prediction, not established fact.*
- **[00:17:32]** The forecast is that tools will merge model and effort into one choice.
- **[00:17:36]** The presenter further predicts the control bar will eventually disappear, with users specifying only how conservative or aggressive token spending should be.
- **[00:17:42]** The predicted system would then route work accordingly.
- **[00:17:45]** The presenter calls the current state the manual era of AI and predicts a quick transition to an automatic era.
- **[00:17:54]** The presenter asks why models keep improving and getting cheaper, then divides the response into capability improvement and cost.
- **[00:18:00]** The presenter says labs train their biggest models and use them to help train smaller models.
- **[00:18:09]** This process is called **distillation** and is compared to a teacher-student relationship.
- **[00:18:13]** In the analogy, the large model answers a huge number of questions, and the smaller model learns to answer in the same way.
- **[00:18:20]** The presenter says this explains why upgrades usually flow down to smaller models.
- **[00:18:25]** On costs, the presenter says models will keep getting cheaper, but a user’s total bill may not fall.
- **[00:18:31]** This is labeled the **Jevons paradox**.
- **[00:18:33]** Historical analogy: when steam engines became more fuel-efficient, total coal use increased rather than decreased because cheaper use created more use.
- **[00:18:40]** Second analogy: cloud computing became cheaper per unit while total spending increased.
- **[00:18:44]** The presenter infers that lower AI cost may lead users to apply it to more and more tasks.
- **[00:18:49]** Final mental model: the model is who you hire; effort is the number of hours you approve.
- **[00:18:56]** Recap: Haiku is the fast intern for simple work.
- **[00:19:00]** Recap: Sonnet is the builder when work is clear.
- **[00:19:02]** Recap: Opus is the high-level designer and the presenter’s recommended everyday default.
- **[00:19:05]** Recap: Fable is the trusted expert for complex end-to-end work.
- **[00:19:11]** Recap: effort is a ceiling, not a floor; the presenter says medium can generally remain selected.
- **[00:19:17]** Recap diagnostic: if the model did not know enough, raise the model; if it did not try hard enough, raise effort.
- **[00:19:22]** The presenter says token limits remain a problem regardless of model and effort selection.
- **[00:19:27]** The closing promotion directs viewers to another video about free AI tools to save time, money, and tokens.

## Source-grounded recap

- **[00:19:13]** The source’s central operational distinction is between model capability (“who you hire”) and effort allowance (“hours approved”).
- **[00:19:17]** The source’s troubleshooting rule is to increase model capability for knowledge/capability shortfalls and increase effort for incomplete execution.
- **[00:19:25]** The source cautions that plan token limits remain relevant even after optimizing model and effort choices.

## Practical applications
- Suggestion: Verify all named models, versions, pricing ratios, defaults, and product capabilities against current first-party documentation; the source’s claims are not independently verified.
- Suggestion: Separate task selection into two decisions: choose capability for task complexity and choose effort for permitted execution depth, latency, and usage.
- Suggestion: Use the source’s failure test as a triage heuristic: if the system had adequate inputs but lacked capability, evaluate a stronger model; if it skipped required work, evaluate higher effort.
- Suggestion: Before escalating a model or effort setting, improve the brief with task objective, relevant context, constraints, files, tests, and required output format.
- Suggestion: For recurring workflows, benchmark a minimum viable model against defined quality criteria and real usage costs.
- Suggestion: Reserve high-effort or multi-agent approaches for tasks whose error risk and multi-step dependencies justify the additional usage and elapsed time.

## Evidence anchors
- [00:00:03.640] people get wrong. Claude isn't one AI,
- [00:00:30.280] four Claude models: Haiku, Sonnet, Opus,
- [00:00:34.000] between them is size. Each one is a
- [00:00:43.680] size. So, Haiku is a three-line poem, a
- [00:01:04.518] about it. Picture Claude as an office.

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
