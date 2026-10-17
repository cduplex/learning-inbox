# Move the number: a three-step growth loop for stuck apps

## Source
- Original: https://www.instagram.com/reel/DeNKjDeyYIl/
- Platform: Instagram Reel
- Creator: @ayoships (Ayo Omolewa)
- Published: 2026-10-07T13:00:30
- Processed: 2026-10-16T23:38:21Z

## Tags
app-growth, analytics, metrics, ai-agents, experimentation

## Core components
- "THE NUMBER": one app-specific metric that is not downloads or engagement (examples shown: average round length in a game, matches per week for a dating app)
- OpenTelemetry: a free open-source logging standard for seeing what the app is doing and where it breaks, readable by AI agents
- Session replays: watching how people actually use the app on screen
- The 30-day loop: have an AI agent examine the data, propose one change to move the number, test it 50/50, keep the winner, and repeat for compounding returns

## Derived summary
Ayo Omolewa gives app-growth advice for the moment an app feels stuck ("Day 47, +0%"): the problem is usually that the creator does not know what to do next or why. He outlines three steps. First, identify "THE NUMBER," one app-specific metric that is not downloads or engagement, such as average round length in a game or matches per week for a dating app. Second, use OpenTelemetry, described as a free open-source standard for logging, to see what the app is doing and where it breaks; he notes AI agents are good at reading these traces. Third, use session replays to literally watch how people use the app on screen. For the next 30 days, he advises having an AI agent examine the data, propose a change to move the number (e.g., moving the upgrade prompt earlier), test it 50/50 against half of users, and keep the winner, showing a result improving from 25.9% to 32.0% on a compounding graph from day 7 to day 30. This is practitioner advice from an app developer; the numbers are the creator's own illustrations, not verified results.

## Practical takeaways
- Define one real metric that reflects the experience you want to improve; downloads and installs will not tell you what to fix.
- Instrument the app with structured logging an agent can read; OpenTelemetry is a standard starting point.
- Watch session replays regularly; aggregate metrics hide the moment users actually get confused.
- Run agent-proposed experiments as 50/50 tests and keep only the winners; the loop compounds, the single test does not.

## Notes
This card is derived from a private Muse processing record. Verify important claims against the original source.
