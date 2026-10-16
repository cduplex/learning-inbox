# Learning Inbox Knowledgebase

A private, Git-backed library of concise learning notes from videos and webpages.

Each note preserves the useful layer of an intake: a canonical source link, derived summary, tags, practical applications, and a small set of evidence anchors. This repository intentionally does **not** contain raw transcripts, full webpages, SQLite databases, message-delivery state, runtime logs, or credentials.

## Use it

- Start at [`data/INDEX.md`](data/INDEX.md) to choose a collection.
- Browse Learning Inbox notes in [`data/learning-inbox/cards/`](data/learning-inbox/cards/).
- Muse's Reel pipeline uses [`data/muse-instagram/`](data/muse-instagram/) under the contract in [`MUSE-PUBLISHING.md`](MUSE-PUBLISHING.md).
- Use GitHub search for topics, tools, or tags.
- Treat every note as a derived aid. Open the original source before relying on a consequential claim.

## Automatic synchronization

A Hermes no-agent job runs once per minute. When a saved evidence record or its derived summary changes, it exports the safe knowledge layer into a dedicated worktree, opens a `sync/learning-inbox-*` pull request, squash-merges it into `main`, and removes the branch. Idle runs do nothing. If a prior automation PR is still open, the next run resumes that PR rather than creating a duplicate.

The synchronizer can only stage `data/learning-inbox/INDEX.md` and `data/learning-inbox/cards/*`; it rejects any other changed path. Before merging, it re-reads the pull request, requires the expected repository, `main` base, owner-created branch, a successful `validate` GitHub Actions check for the exact head commit, and the data-only file list. It passes that same validated head commit to GitHub's merge API. Its source is [`scripts/sync_from_learning_inbox.py`](scripts/sync_from_learning_inbox.py). The installed scheduler wrapper supplies the profile-local archive and isolated worktree paths.

## Updating the library

The checked-in exporter turns saved Learning Inbox evidence records into safe, readable cards. It reads raw records from a path outside this repository and emits only the curated layer described above:

```bash
python3 scripts/export_from_learning_inbox.py \
  --source-records /path/to/private/library/records \
  --output data/learning-inbox
```

Review the generated diff before committing. The exporter skips credential-bearing source URLs and redacts token-shaped strings from generated text. Cards must stay at or below 10,000 characters, which keeps raw transcript-scale material outside this repository. Run `python3 scripts/validate_collections.py` before opening any PR; the same validation runs in GitHub Actions for pull requests.

## Data boundary

GitHub is the versioned knowledge layer, not the raw archive. Keep original evidence and the live search database in their protected local backup location.
