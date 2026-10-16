# Muse Instagram publishing contract

Muse may publish **derived** Instagram Reel knowledge cards to this private repository. It must never treat this repository as a raw archive.

## Ownership boundary

Muse may create, update, or delete only these paths:

```text
data/muse-instagram/INDEX.md
data/muse-instagram/reels/*.md
```

Do not modify `data/INDEX.md`, `data/learning-inbox/**`, repository tooling, documentation, or another pipeline's files. Learning Inbox owns `data/learning-inbox/**` and regenerates it automatically.

## Never commit

Do not commit raw transcripts, video/audio/image files, scraped HTML, cookies, browser session state, API keys, credentials, private messages, databases, logs, provider responses, backups, or URLs containing userinfo or sensitive query/fragment keys.

## Card format

Create one card per Reel at:

```text
data/muse-instagram/reels/YYYY-MM-DD--short-slug--stable-id.md
```

`stable-id` must be deterministically derived from the canonical Reel URL or Instagram Reel identifier. Do not use a random ID.

```markdown
# Exact Reel title or concise descriptive title

## Source
- Original: <canonical safe Instagram Reel URL>
- Platform: Instagram Reel
- Creator: <creator handle or name, if available>
- Published: <ISO 8601 date/time if available>
- Processed: <ISO 8601 UTC timestamp>

## Tags
tag-one, tag-two, tag-three

## Core components
- <component, pattern, framework, or tactic>

## Derived summary
<Concise source-grounded summary. State uncertainty instead of guessing.>

## Practical takeaways
- <bounded, actionable takeaway>

## Evidence anchors
- [MM:SS] <brief supporting paraphrase or short quote>

## Notes
This card is derived from a private Muse processing record. Verify important claims against the original source.
```

Omit unavailable fields rather than inventing them. Keep quotations short and preserve timestamps only when available. Redact token-like strings and omit unsafe URLs.

## Index

Update `data/muse-instagram/INDEX.md` with every changed card. Each entry must include a relative link, title, up to six tags, platform, and processing status.

## Git workflow

1. Fetch `origin/main`, then create `sync/muse-instagram-<UTC timestamp>`.
2. Stage only allowed Muse paths.
3. Review the complete diff for source accuracy and sensitive material.
4. Open a PR to `main` titled `chore(data): sync Muse Instagram Reels`.
5. Merge only the exact PR created from the generated commit after confirming its changed-file list is limited to the Muse collection.
6. Squash merge, read back the merged PR, then delete the branch.

Do not push directly to `main`, resume another automation's PR, or merge a PR with files outside the Muse collection.
