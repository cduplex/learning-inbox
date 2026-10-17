# Why AI coding agents fail: horizontal plans need tracer-bullet vertical slices

## Source
- Original: https://www.instagram.com/reel/Dc4UOaozcpA/
- Platform: Instagram Reel
- Creator: @thedailyai.news (The Daily AI)
- Published: 2026-09-04T14:08:37
- Processed: 2026-10-16T23:38:21Z

## Tags
ai-agents, coding-workflows, software-practices, prompt-strategy, pragmatism

## Core components
- The failure mode: horizontal plans (database layer first, then API, then frontend) with no integrated feedback loop
- Tracer bullets / vertical slices from The Pragmatic Programmer: thin slices that cross every layer
- The payoff mechanism: proving the whole flow works end to end early, enabling early testing and iteration

## Derived summary
This is a clip from a conference talk by Matt Pocock, reposted by the curator account The Daily AI under the title "WHY YOUR AI AGENT KEEPS FAILING." Pocock argues that AI coding agents usually fail not because tasks are too hard, but because they are handed horizontal plans: build the database layer first, then the API, then the frontend, without an integrated feedback loop. He reaches for the classic software concept of "tracer bullets," or vertical slices, from The Pragmatic Programmer. Instead of coding layer by layer, agents should be tasked with thin vertical slices that cross all layers (database, service/API, frontend) to prove the whole flow works end to end. Horizontal coding delays feedback until late phases, while vertical slices allow early testing and iteration, which he argues makes them the better workflow for AI agents. Commenters mostly ask for the full-length talk. This is a well-established software practice applied to agents, presented as practitioner advice rather than new research.

## Practical takeaways
- When tasking a coding agent, spec thin vertical slices that touch every layer, and demand a working end-to-end flow before expanding scope.
- Build the feedback loop into the plan itself: the first slice should be testable, not just structural.
- If an agent keeps failing, check the plan shape before the task difficulty; a horizontal plan is a likely culprit.
- Use vertical slices for iteration speed: each completed slice is real evidence the approach works.

## Notes
This card is derived from a private Muse processing record. Verify important claims against the original source.
