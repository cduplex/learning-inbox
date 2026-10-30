# Muse Instagram publishing contract

Rewritten 2026-10-16 at Chris's direction: minimal ceremony. This is a personal knowledge base of publicly available recaps, not a secrets vault. The rules below exist to keep the data clean, not to create process.

## What Muse may write

Only these paths, ever:

```text
data/muse-instagram/INDEX.md
data/muse-instagram/reels/*.md
briefs/coo/*.json
briefs/team/*.json
```

Nothing else in the repo gets touched. Learning Inbox owns `data/learning-inbox/**` and regenerates it automatically.

## AI brief feeds

Added 2026-10-30 at Chris's direction, per `feed-spec.md` in this repo. The two daily brief jobs each publish one JSON file per weekday run, in ONE commit directly to `main` containing only that job's file:

```text
briefs/coo/YYYY-MM-DD.json
briefs/team/YYYY-MM-DD.json
```

The file schema, categories, and writing rules live in `feed-spec.md`. The feeds hold only public news. The Instagram card rules below (validation, card format, index) apply only to the `data/muse-instagram/**` paths, not to the brief feeds.

## Never commit

Raw transcripts, video/audio/image files, scraped HTML, cookies, browser state, API keys or credentials, private messages, databases, logs, or URLs with sensitive query/fragment keys. Cards are derived summaries, not archives.

## Card format

One card per Reel at:

```text
data/muse-instagram/reels/YYYY-MM-DD--short-slug--stable-id.md
```

`stable-id` is the first 12 lowercase hexadecimal characters of the SHA-256 hash of the canonical Reel URL: `https://www.instagram.com/reel/<reel-id>/`. If a card with that stable ID already exists, update it instead of creating a duplicate. Filename date is the Reel's published date when known, else the processing date.

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

Omit unavailable fields (including Evidence anchors when no real timestamps exist) rather than inventing them. Keep each card at or below 10,000 characters.

## Index

Update `data/muse-instagram/INDEX.md` with every changed card: relative link, title, up to six tags, platform, and processing status.

## Publishing

1. Run `python3 scripts/validate_collections.py` locally against the changed files and fix every violation before publishing.
2. Publish in ONE commit directly to `main` containing only the allowed Muse paths (the cards plus the index). No branches, no pull requests, no merge steps.
3. If a direct push to `main` is ever rejected by repository settings, fall back to the standing branch `sync/muse-instagram-standing`: push there, open the PR, and merge it once the `validate` check passes, without waiting on Chris.
