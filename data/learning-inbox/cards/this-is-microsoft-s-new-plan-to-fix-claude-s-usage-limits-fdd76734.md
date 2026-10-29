# This Is Microsoft's New Plan To Fix Claude's Usage Limits

## Source
- Original: https://www.youtube.com/watch?v=1kQ_1_QL5Es
- Type: youtube
- Creator: {'displayName': 'AI LABS'}
- Published: 2026-10-28T00:00:00.000Z

## Tags
Token Economizer, AI coding agents, token optimization, Claude Code, prompt injection, tool pruning

## Learning guide
**The arc**
AI agents like Claude Code burn through usage limits because every request carries old context, unused tool descriptions and repeated mistakes. Microsoft's Token Economizer plugin tackles this by watching your sessions per project and stripping that waste from later ones. The guide moves from where tokens go, to how the plugin responds, to installing and configuring it safely, fixing its cold start by seeding it from past sessions, and inspecting what it did.

**1. Understand where your tokens go**
- **Count the hidden payload:** Each request sends persistent instructions, available tools, added MCP tools and skills, and the whole conversation, not just your latest prompt. Context you no longer need still costs tokens every message.
- **Spot recurring waste:** Agents often rediscover in each new session that a command fails, and unused tool descriptions ride along with every message. These two repeat costs are what the plugin targets.
- **Know how it differs from mappers:** Tools like Graft map files in advance to cut searching, while Token Economizer observes sessions and commands, then removes waste from later sessions.

**2. Know what the plugin does**
- **Micro skills:** It records recurring project-specific mistakes as candidate facts, confirms them over further sessions, and feeds accepted facts at session start so the agent stops repeating failures.
- **Tool pruning:** If a tool goes unused across 10 messages spanning at least two sessions, it is turned off for that project so its description stops being sent. This is the biggest source of savings, but it happens silently without asking or notifying you.
- **Stuck detection:** When work runs much longer than usual for the project, a model checks whether the agent is truly stuck and, if so, tells it once to try another approach. If it stays stuck, the plugin tells you to press Escape; it never stops the agent itself.
- **Expected payoff:** Microsoft's test used 277 real bugs from six GitHub projects across five setups (Claude Code, Codex, GitHub Copilot), and all five cost less. Claude Code costs dropped 23.6% with Sonnet 5 and 30.9% with Opus 4.8, with Sonnet fixing one more bug per 100.

**3. Install and configure it**
- **Install per agent:** Find your agent's command in the install section of the GitHub repository, run it in a terminal, then confirm it appears in Claude Code's plugin list. It works with Claude Code, Codex and other agents.
- **Know the hooks:** A session-start hook supplies micro skills, a post-tool-use hook checks for stuck behavior, and an end-of-session review learns facts and counts unused tools.
- **Turn on micro skills deliberately:** Run the Token Economizer config command and set micro skills to on; it is off by default while other features start enabled. Do this for your own projects to get the extra savings.
- **Accept the micro-skill costs:** When on, a model reads recent sessions and writes facts every three sessions, using some of your limit. Project commands can also print attacker-supplied instructions that become false facts Claude trusts later, so avoid enabling it on untrusted projects and edit bad facts.

**4. Fix the cold start**
- **Expect early sessions to cost more:** A fresh install knows nothing, even on a long-running project, and learning is per project with no transfer. In Microsoft's tests almost every project cost more at first and became cheaper by the sixth task.
- **Seed from existing history:** Claude Code keeps sessions in the main.claude folder for 30 days. Give Claude Code the plugin repository and ask it to modify startup so the first session after install launches a background task that reads earlier sessions for the same folder and uses them as the starting point.
- **Install the modified version globally if needed:** Ask Claude to install it for use everywhere. Brand-new projects still start blank since they have no history.

**5. Inspect and correct what it did**
- **Check status:** The status command shows sessions learned from, tokens used, feature activity, pruned tool names, and how many micro-skill facts were supplied at session start.
- **Review facts:** The micro skills command lists facts supplied to Claude and those still under review, which is where you catch injected or wrong facts.
- **Audit pruning:** The tool prune command explains each pruned tool by showing sessions and messages without use; the demo had 276 tools unused across four sessions. Check here first whenever Claude can no longer do something it used to.
- **Measure savings:** The tool prune measure command compares per-message tokens with all tools versus used tools; the demo showed about 34,300 versus 24,400, roughly 29% less.
- **Restore a tool:** Run tool prune restore with the tool's name; a restored tool stays on and will not be pruned again.
- **Run your own A/B test:** After five learning sessions (303 tools pruned), the presenters ran three new tasks twice from the same code, with and without the plugin. They got 99 versus 79 steps, about 21% lower cost, with the same checks passing.

**Try this first:** Install Token Economizer for Claude Code from the repository's install section, enable micro skills via the config command on one of your own long-running projects, and after a few sessions run the status and tool prune measure commands to see your savings.

**Caveat:** The cost reductions come from Microsoft's and the presenters' own tests and are not independently verified, and the presenters sell their pre-modified cold-start version through their community, though you can build the same change yourself with Claude Code.

## Derived summary
## [00:00:00] Token Economizer and reported results

- [00:00:00] AI Labs introduces Microsoft’s Token Economizer as a tool intended to reduce an agent’s token use by learning from project sessions. The presenters also describe a modification to address its initial lack of project history. [p0001–p0020]
- [00:00:56] The presenters contrast it with project-mapping tools such as Graft: those map files in advance to reduce search, whereas Token Economizer observes sessions and commands, then attempts to remove waste from later sessions. [p0029–p0043]
- [00:01:23] Microsoft’s reported test used 277 real bugs from six GitHub projects, fixed sequentially across five setups involving Claude Code, Codex and GitHub Copilot. The presenters say all five cost less with the tool. [p0043–p0053]
- [00:01:46] The presenters report Claude Code cost reductions of 23.6% for Sonnet 5 and 30.9% for Opus 4.8. They say model performance was unaffected and Sonnet fixed one more bug per 100, attributing that improvement to a less cluttered context. These claims and the causal explanation are not independently verified. [p0053–p0061]

## [00:02:15] Where tokens go and how the plugin responds

- [00:02:25] The presenters explain that model requests contain more than the latest prompt: they also include persistent instructions, available tools, added MCP tools and skills, and the conversation so far. Context that is no longer needed still consumes tokens. [p0071–p0089]
- [00:03:00] Repeated mistakes also consume tokens: an agent may rediscover that a command fails in each new session. Unused tool descriptions are another recurring overhead. [p0089–p0095]
- [00:03:22] **Micro skills:** the plugin records recurring project-specific mistakes as candidate facts, confirms them over further sessions, and supplies accepted facts at the start of later sessions so the agent can avoid repeating failures. [p0099–p0121]
- [00:04:04] **Tool pruning:** if a tool is unused across 10 messages spanning at least two sessions, the plugin turns it off for that project so its description is no longer sent with each message. [p0121–p0128]
- [00:04:18] The presenters say Microsoft’s figures attribute the largest token savings to pruning. The tradeoff is that tools are removed without asking or notifying the user, though a later command can reveal them. [p0128–p0137]
- [00:04:35] **Stuck detection:** when work runs much longer than usual for a project, the plugin asks a model whether the agent is genuinely stuck. If confirmed, it tells the agent once to try another approach. [p0137–p0149]
- [00:04:58] If the agent remains stuck, the plugin tells the user to press Escape; the presenters say it never stops the agent itself. [p0149–p0152]
- [00:05:04] **Sponsor aside:** Data Impulse is promoted as a proxy service for making requests from different countries. [p0152–p0179]

## [00:06:04] Installation, hooks and micro-skill safety

- [00:06:04] The presenters describe Token Economizer as a plugin for Claude Code, Codex and other agents. Their installation workflow is to find the relevant agent’s command in the GitHub repository’s install section, run it in a terminal, and check Claude Code’s plugin list. [p0179–p0192]
- [00:06:31] Hooks run automatically at events such as session start and messages. A start hook supplies micro skills, another checks after tool use for stuck behavior, and an end-of-session review learns facts and counts unused tools. [p0192–p0211]
- [00:07:09] The configuration command shows that most features are enabled initially, but micro skills are off by default. [p0212–p0216]
- [00:07:16] One reason is usage cost: when enabled, a model reads recent sessions and writes facts every three sessions, consuming some of the user’s limit. [p0216–p0222]
- [00:07:28] The other reason is prompt-injection risk. Project commands can print attacker-supplied instructions, which could become supposed facts that Claude reads as true in future sessions unless edited. The presenters say Microsoft leaves activation to the user. [p0222–p0236]
- [00:07:55] The presenters recommend enabling micro skills for one’s own projects, citing reported token savings; their workflow is to run the Token Economizer config command and set micro skills to on. [p0236–p0244]

## [00:08:13] Cold start and the presenters’ modification

- [00:08:13] The presenters say a fresh installation has not yet learned from a project, including a long-running one, so benefits require further use and initial learning can cost more. [p0245–p0259]
- [00:08:40] In the reported Microsoft tests, almost every project initially cost more with the plugin and became cheaper by the sixth task. The presenters say learning is separate for each project and does not transfer between them. [p0259–p0266]
- [00:08:55] They say Claude Code retains sessions in the main .claude folder for 30 days and propose using that history to seed the plugin rather than starting blank. [p0266–p0279]
- [00:09:04] Their workflow was to give Claude Code the repository and ask it to modify startup behavior so it reads prior stored sessions. The captions mention a prompt on screen but do not provide its text. [p0270–p0285]
- [00:09:35] They say the modified version launches a background task on the first session after installation, reads earlier sessions for the same folder, and uses what it learns as the starting point. They also mention asking Claude to install it for use everywhere if needed. [p0286–p0298]
- [00:09:58] The modification cannot seed a brand-new project because it has no history, but the presenters say it can help existing projects avoid starting from zero. [p0298–p0303]

## [00:10:07] Inspection commands and demo measurements

- [00:10:07] The presenters tested their modified version on a demo project. They describe a status command that reports sessions learned from, tokens used, and feature activity. [p0303–p0314]
- [00:10:30] In that project, status reported four learned sessions, no stuck-check intervention, and a long list of tools eligible for removal; it also reported how many micro-skill facts were supplied at session start. [p0315–p0322]
- [00:10:43] The micro skills command lists both facts supplied to Claude and facts still under review. [p0322–p0327]
- [00:10:53] Status lists pruned tool names, while the tool prune command also explains each listing by showing sessions and messages without use. The presenters report 276 tools unused across all four demo sessions. [p0327–p0337]
- [00:11:16] Because pruning is silent, the presenters identify tool prune as a place to check if Claude can no longer do something it previously could. [p0338–p0341]
- [00:11:24] The tool prune measure command compares message token counts with all tools versus used tools. In the demo, the presenters report roughly 34,300 versus 24,400 tokens per message, about 29% less. [p0342–p0352]
- [00:11:46] A pruned tool remains off for that project until restored using tool prune restore with its name. The presenters say a restored tool will not be pruned again. [p0352–p0359]

## [00:12:01] Second test and recap

- [00:12:01] On another app, the presenters ran five learning sessions with the plugin, during which it turned off 303 tools. They then ran each of three new tasks twice, with and without the plugin, starting both runs from the same code. [p0360–p0368]
- [00:12:18] They report 99 total steps without the plugin versus 79 with it, approximately 21% lower cost, and the same checks passed by both versions. [p0368–p0373]
- [00:12:30] Their recap is that initial sessions cost slightly more before the plugin learned, while savings appeared later. Their expectation that the difference grows with continued use is a prediction, not an independently verified guarantee. [p0373–p0379]
- [00:12:43] **Promotional aside:** the presenters offer their modified version through their community and close with a request for channel support. [p0380–p0392]

## Evidence anchors
- [00:00:00.160] Microsoft built a tool that fixes your
- [00:00:02.560] token usage and it's called Token
- [00:00:04.560] Economizer. And interestingly, this tool
- [00:00:06.879] gets better the more you use it. So, it
- [00:00:08.800] saves you more tokens over time. It

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
