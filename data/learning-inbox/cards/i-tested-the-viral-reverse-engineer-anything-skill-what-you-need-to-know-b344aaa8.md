# I Tested the Viral Reverse Engineer Anything Skill. What You Need to Know.

## Source
- Original: https://www.youtube.com/watch?v=rL5tw6h78zo
- Type: youtube
- Creator: {'displayName': 'Nate Herk | AI Automation'}
- Published: 2026-10-13T00:00:00.000Z

## Tags
reverse engineering, AI agents, software development, product requirements, feature analysis, testing, Claude Code, workflow design

## Learning guide
**The arc**
Nate Herk starts from the viral GitHub repo Reverse Engineer Anything (REA) and asks what it really adds, since reverse engineering is not new. His central idea is that AI executes well when given a clear vision, and an existing example of the result you want acts as a highly specific PRD you never had to write. He moves from everyday examples (video editing, reports, apps) to REA's five-step workflow, then to legal and model limits, and ends with a general principle for any workflow.

**1. Show the output instead of describing it**
- **Feed real examples, not a generic request:** A generic goal produces a generic result, so give the agent strong examples of what you want and let it infer the recipe. For a Friday report, provide five good Friday reports; for an editing skill, he supplied about 30 of his best-performing Instagram Reels.
- **Ask for frame-by-frame analysis:** Have the model break down what happens under the hood (B-roll, font colors, shimmers, animations, overall vibe) before building anything. He gave Opus a downloaded motion edit by Jordan Watkins and asked for frame-by-frame analysis plus a reusable editing skill.
- **Turn the analysis into a reusable skill:** Ask the agent to package what it learned as a skill you can run again. The result may still trail the original in polish (motion and sound design), but it clearly improves once the AI has a concrete creative reference.
- **Use a reference app as your PRD:** Pointing at an existing product gives the agent detailed specs without you writing every requirement. Compare "make me a cake" with a target that specifies taste, density, frosting type and number of layers.

**2. Clone behavior, and scope it tightly**
- **Copy functionality, not presentation:** Take inspiration from elements, animations or behaviors, then build your own look and choices. His Loom-inspired "Herk Recorder" kept a recording countdown, a movable and resizable camera bubble and window selection, but used a different interface and stored files locally in its own folder instead of a cloud.
- **Adapt features to your own setup:** He rebuilt Sand Castles-style functionality as a personal version that uses his own API key for analyzing Instagram and his content, and used Langfuse to inform the core features of his eval studio without making a carbon copy.
- **Pick features, not whole products:** "Reverse engineer Loom" is too broad, so isolate specific features. Ask which Loom features are most valuable, or which Salesforce or CRM features are worth bringing into a custom app.
- **Frame the request around one mechanism:** Ask the agent to investigate how a single thing works, for example how Loom's camera bubble works, so you can add equivalent functionality to a different app.
- **Reverse engineer the tool itself:** He used Claude Code with REA to analyze the REA repo, which taught him how to instruct it better. Do the same with any tool you want to master.

**3. Run the REA five-step workflow**
- **Step 1, pick a feature:** Start from a specific behavior rather than pointing the agent at an entire app.
- **Step 2, route by build:** Consider what the target app is built with and choose or adjust analysis tools accordingly. If you do not know the stack details yourself, explicitly tell the agent to consider the app's technology stack.
- **Step 3, summary first:** Let REA analyze the app and produce a short summary of what works, how it works and what it could not determine before diving into modules and traces. The Loom analysis exceeded 1 GB, so do not rerun the full summary repeatedly; it is already saved locally in your project files.
- **Step 4, label findings seen, inferred or unknown:** Seen means the model actually found and cited it (for example, Loom having 11 custom native add-ons); inferred means the code or data suggests it; unknown means it could not be observed. Never build on inferred points as if they were facts, because that creates messy outcomes.
- **Step 5, rebuild and test:** This is the most important stage. Build from the findings, run test cases against real behavior and iterate, instead of shipping because the build merely looks complete.
- **Expect slower but better results:** In his test, two coding agents got the same prompt and only one used REA; the plain agent finished first, but the REA agent produced better results because of stronger decomposition.

**4. Respect the boundaries and limits**
- **Stay legal:** Do not copy exact code or assets. Only analyze what is observable in local files or available through an API; never access private source code or hack a company's servers.
- **Plan setup per app:** Different apps need different environments depending on where they run and their tech stack.
- **Use a strong model for inspection:** Results depend on the model doing the analysis and coding; REA does not build things automatically. To save cost, you can try letting a stronger model investigate and a cheaper model build from the saved findings.

**5. Apply it beyond software**
- **Work backward from proven results:** Use the same approach for processes, skills and daily or business workflows. Find someone who has demonstrably done something well, figure out why it worked, and adapt that mechanism to your own context.

**Try this first:** Pick one recurring output you produce (like a Friday report), gather five of your best past examples, and ask your agent to analyze what makes them work and turn that into a reusable skill.

**Caveat:** The claim that REA beats a plain agent comes from a single informal test by the creator, so compare results on your own task before relying on it.

## Derived summary
## [00:00:00] Thesis: reverse engineering as an AI-building workflow
- [00:00:00] The speaker says the GitHub repository **Reverse Engineer Anything (REA)** is rapidly gaining attention; a quoted remark that “software is done” is characterized as partly joking.
- [00:00:12] The stated idea is to show an agent a feature in an existing app or piece of software, have it determine how that functionality works through the repository’s framework, and recreate it.
- [00:00:25] The speaker says REA is impressive after personal experimentation with games, software, tools, and apps, but argues that the underlying approach is not new.
- [00:00:52] The speaker’s view is that AI is not very creative or able to think outside the box, but can execute well when given a clear vision. This is the speaker’s opinion, not independently verified.

## [00:01:00] Examples: learning an output style instead of describing it generically
- [00:01:06] The speaker compares human-edited Instagram Reels with an AI editing skill intended to reproduce their style: B-roll, font colors, shimmers, animations, and overall visual “vibe.”
- [00:01:35] Rather than requesting a generic Instagram-editing skill, the speaker supplied roughly **30** best-performing Reels and asked for frame-by-frame analysis of what occurred “under the hood.”
- [00:01:52] In another example, the speaker downloaded a motion-edit video by Jordan Watkins, gave it to Opus, and requested frame-by-frame analysis plus a reusable editing skill.
- [00:02:11] The speaker judges the original motion edit as still better in motion and sound design, but says the AI output improved because it was given a concrete creative reference. This comparison is a speaker judgment, not independently verified.
- [00:02:27] The general rule offered is to reverse engineer the desired output: for a Friday report, provide **five** good Friday-report examples so the agent can infer the desired result.
- [00:02:40] The speaker argues that a generic goal produces a generic result; a reference application functions as a highly specific PRD without manually writing all specifications.

## [00:03:07] Examples: clone functionality, not exact presentation
- [00:03:07] The speaker says this reference-driven approach has been used for landing pages by taking inspiration from elements, animations, or designs, and for apps.
- [00:03:18] A Loom-inspired screen recorder reportedly included a recording countdown, a movable camera bubble, and the ability to resize it during recording.
- [00:03:51] The speaker stresses that this was not an exact Loom clone: it used a different-looking interface and focused on behavior such as moving the bubble and selecting the recording window.
- [00:04:10] The cited distinction is storage: Loom stores recordings in Loom’s cloud, whereas the speaker’s “Herk Recorder” stores files locally in its own folder.
- [00:04:19] The speaker also describes inspecting Sand Castles functionality to create a personal version requiring an API key, reportedly for analyzing Instagram and personal content.
- [00:04:34] For an “AIS eval studio,” the speaker says Langfuse informed the product’s core features and behavior, while emphasizing it was not a carbon copy.

## [00:04:54] Aside: promotional giveaway
- [00:04:54] **Sponsor/giveaway aside:** The speaker promotes a free website-design skill called ScrollCraft, claiming it covers scroll-driven animations, layering, typography, spacing, depth, and general design taste. These product claims are not independently verified.

## [00:05:20] What REA adds to an existing practice
- [00:05:20] The speaker says reverse engineering itself has existed for a long time; REA’s value is a practical, structured framework for decompiling and iterating toward a target build.
- [00:05:35] The speaker recommends showing agents the end goal and working backward, not only for app development but also for day-to-day workflows and reusable skills.
- [00:05:56] REA is summarized as helping an AI agent study something and then help build it.

## [00:06:02] Bakery analogy: decompilation and iteration
- [00:06:02] The speaker analogizes a proprietary bakery cake to a closed implementation: the bakery ships the finished cake but does not disclose its recipe because it is its intellectual property.
- [00:06:22] To infer the recipe, a person can inspect, taste, and examine the finished cake, analogous to decompiling observable behavior.
- [00:06:44] The process then becomes trial and error: build a version, compare it with the target, and iterate until the result is close.
- [00:06:52] Applied to Loom, the proposed request is to investigate how its camera bubble works so equivalent functionality can be incorporated into a different screen-recording app.
- [00:07:12] The speaker contrasts “make me a cake” with a detailed target specifying taste, density, frosting type, and number of layers; the latter is offered as the reason targeted reverse engineering yields better results.

## [00:07:26] Scope features rather than entire products
- [00:07:26] The speaker says “reverse engineer Loom” is too broad and that isolating particular features is easier.
- [00:07:43] Suggested scoping questions include: which Loom features are most valuable, or which Salesforce or CRM features are worth bringing into a custom app.
- [00:08:01] The speaker says they used Claude Code with REA to reverse engineer the REA repository itself, aiming to understand how to use and instruct it more effectively.

## [00:08:17] REA workflow: five main steps
### [00:08:17] 1. Pick a feature
- [00:08:17] The speaker lists five steps: **pick a feature, route by build, summary first, seen/inferred/unknown, and rebuild and test**.
- [00:08:28] Begin with specific behavior or functionality rather than pointing the agent at an entire app.

### [00:08:34] 2. Route by build
- [00:08:34] “Route by build” means considering what the target app is built with and selecting or adjusting analysis tools accordingly.
- [00:08:51] The speaker says they do not know this technical-routing process from memory, but would explicitly give the agent context to consider the app’s technology stack.

### [00:08:59] 3. Summary first
- [00:08:59] REA reportedly analyzes the whole app and produces a summary; the speaker says the Loom analysis exceeded **1 GB**.
- [00:09:14] The shorter summary is meant to communicate what works, how it works, and what the system could not determine, before going into modules and traces.
- [00:09:24] The speaker cautions against repeatedly rerunning the full summary because the analysis is already saved locally in the project or files.

### [00:09:36] 4. Label findings as seen, inferred, or unknown
- [00:09:36] Findings should be categorized as **seen**, **inferred**, or **unknown**.
- [00:09:45] “Seen” refers to findings the model actually located and cited; the example given is Loom having **11 custom native add-ons**. This specific factual claim is presented by the speaker and not independently verified.
- [00:09:54] “Inferred” refers to conclusions suggested by code or data but not established as fact.
- [00:10:04] The speaker warns that treating inferred assumptions as facts and building on them can create messy outcomes.
- [00:10:16] “Unknown” refers to behavior REA could not observe within the native recorder or other inspected app.
- [00:10:25] The speaker says this evidence-aware classification is what makes the repository’s process feel more structured than simply asking an AI to research and build an app.

### [00:10:43] 5. Rebuild and test
- [00:10:43] Rebuilding and testing are described as the most important stage: use findings to build, iterate, and test rather than treating initial output as final.
- [00:10:57] The proposed process includes running test cases and processing real behavior, then iterating instead of shipping once because the build merely appears complete.

## [00:11:10] Legal, access, setup, and model limitations
- [00:11:10] The speaker says not to copy exact code or assets and notes legal limits when deeply inspecting an existing product.
- [00:11:19] The stated boundary is to analyze material already observable in local files or available through an API, not to access private source code or hack into a company’s servers.
- [00:11:48] The speaker describes decompiling publicly available or personally accessible material as something humans already do, but says agents can process code and traces faster than many people can.
- [00:12:05] Different apps may require different setup based on where they run, their technology stack, and the needed environment.
- [00:12:15] The quality of results depends on the model doing the inspection and code writing; REA does not make a complete build happen automatically.
- [00:12:28] The speaker proposes a possible cost tradeoff: after a stronger model performs the investigation, a cheaper model might build from the resulting data. This is presented as a hypothetical, not a verified benchmark.

## [00:12:58] Reported experiment and tradeoff
- [00:12:58] The speaker says they gave two coding agents the same prompt, with only one using REA.
- [00:13:05] According to the speaker, the agent without REA finished first, while the REA-based agent was slower but produced better results because its framework improved decomposition. This is an anecdotal result, not independently verified.
- [00:13:27] The speaker reports that the repository had **192K stars** and appeared to rise toward **195K to 196K** after about **30 minutes**. This is a time-specific speaker observation, not independently verified.

## [00:13:37] Predictions and final recap
- [00:13:37] **Prediction:** The speaker expects coding agents to improve at reverse engineering and would not be surprised if future versions of named models incorporate more of this capability directly.
- [00:13:54] The speaker says the tool can help people without formal programming or software-engineering backgrounds create work that feels more professionally built. This is a speaker claim, not independently verified.
- [00:14:03] Recap: reverse engineering is not new; the claimed benefit is supplying a much more specific PRD by using an existing role model instead of writing every requirement manually.
- [00:14:22] The speaker broadens the idea beyond software to processes, skills, and business or daily workflows.
- [00:14:37] Final practical principle: identify someone who has demonstrably done something well, determine why it worked, and consider how the mechanism applies to one’s own context and workflows.

## Evidence anchors
- [00:00:12.639] the idea of reverse engineer Anything is
- [00:00:14.320] that you see a feature you like on some
- [00:00:16.000] sort of app or software that already
- [00:00:17.279] exists and then you can have your agents
- [00:00:19.199] using the frameworks inside of here,

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
