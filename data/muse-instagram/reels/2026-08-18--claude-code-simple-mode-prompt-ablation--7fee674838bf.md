# Claude Code's hidden simple mode: delete the system prompts and the model gets smarter

## Source
- Original: https://www.instagram.com/reel/DcMSk7Rxcdu/
- Platform: Instagram Reel
- Creator: @foundedceo (FOUNDED CEO)
- Published: 2026-08-18T11:47:42
- Processed: 2026-10-16T23:38:21Z

## Tags
claude-code, system-prompts, prompt-engineering, ablation-testing, ai-tools

## Core components
- The "simple=1" environment variable, shown deleting all system prompts including tool prompts
- Ablation testing as a method: strip prompts to check whether they earn their keep
- The distinction between prompts that add intelligence and prompts that shape product behavior

## Derived summary
In this clip from Y Combinator Startup School 2026, posted by the curator account FOUNDED CEO, Claude Code creator Boris Cherny demonstrates that running Claude Code with the environment variable "simple=1" deletes all system prompts, including those from tools. Cherny says his team uses this as an ablation test to see whether prompts are actually useful, and reports a surprising finding: the model is slightly more intelligent without them. He clarifies that Claude Code as a consumer product still keeps some prompts, because they help users interact with the product and keep the model behaving as intended. The comment discussion is divided: some developers call Claude Code bloated and welcome lighter prompting, while others distinguish system prompts from user prompts and defend them. The core claim is Cherny's own report, not independently verified evidence, and the digest provides no test methodology or timestamps.

## Practical takeaways
- Run a prompt ablation on your own AI workflows: strip system prompts and compare output quality before assuming they help.
- Separate prompts that add capability from prompts that shape product behavior; the latter may still earn their place even if they cost some raw intelligence.
- Treat tool bloat as a design problem: every prompt token should have a measurable reason to exist.

## Notes
This card is derived from a private Muse processing record. Verify important claims against the original source.
