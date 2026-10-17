# Fast Jev Compaction: a smarter alternative to Claude Code's compact command

## Source
- Original: https://www.instagram.com/reel/DdmkQYwk-vg/
- Platform: Instagram Reel
- Creator: @vibe_withkevin (Kevin Magnan)
- Published: 2026-09-22T13:13:41
- Processed: 2026-10-16T23:38:21Z

## Tags
claude-code, context-window, plugins, jev, productivity

## Core components
- The "fast-jev-compaction" plugin by Tamara Tran, installed through the Claude Code plugin command
- The scoring mechanism: each tool call in the session outline is scored, low-value entries are dropped, and prompts, details, and plans are kept verbatim
- The threshold tactic: set an aggressive compaction threshold (e.g., 25%) so compaction happens early, holding a "smart zone" around 250K tokens instead of letting the window fill

## Derived summary
Kevin Magnan presents a technical tip for Claude Code users: never use the built-in compact command again, and instead install a plugin called "Jev," specifically the "fast-jev-compaction" plugin by Tamara Tran. He demonstrates installing it through the terminal's plugin command and setting an aggressive threshold such as 25% so compaction happens early. The plugin's interface scores each tool call in the session outline and drops low-value entries while keeping important items like prompts, details, and plans verbatim. A graph in the video illustrates the difference: the built-in compaction quickly fills the context window, whereas Jev maintains a "smart zone" around 250K tokens, extending session length much longer without needing a new terminal or a clear command. He notes it is especially helpful for coding workflows, where most of the dropped context is tool-call noise. The video ends with a comment-gated offer to share the repo link. Performance claims are the creator's demonstration, not verified measurements.

## Practical takeaways
- Try plugin-based compaction instead of the built-in command if long sessions degrade for you; score-and-prune preserves more signal.
- Set an early compaction threshold so pruning happens while the session still has headroom, not when the window is already full.
- Keep plans and prompts verbatim in any compaction scheme; the riskiest thing to lose is intent, not tool output.
- Monitor context across sessions: the win is measured in sustained session length, not a single compact call.

## Notes
This card is derived from a private Muse processing record. Verify important claims against the original source.
