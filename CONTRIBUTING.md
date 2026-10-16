# Updating the knowledgebase

## Collection ownership

- Learning Inbox automation owns only `data/learning-inbox/**`.
- Muse owns only `data/muse-instagram/**`; follow [`MUSE-PUBLISHING.md`](MUSE-PUBLISHING.md).
- The top-level `data/INDEX.md` is a collection directory. Do not overwrite it from a pipeline exporter.

## Pull-request gate

`main` requires the GitHub Actions `validate` check for every pull request. Run `python3 scripts/validate_collections.py` locally first, then wait for the matching remote `validate` check to succeed before merging. Do not bypass the check or push directly to `main`. Changes to CI, scripts, tests, and publishing contracts also require review from the `@cduplex` code owner; routine generated collection-card updates do not.

## Learning Inbox updates

1. Keep the raw Learning Inbox archive outside this repository.
2. Run `scripts/export_from_learning_inbox.py` against the saved Markdown evidence directory with `--output data/learning-inbox`.
3. Inspect `git diff -- data/learning-inbox/` for accuracy, relevance, and accidental sensitive material.
4. Commit only the generated Learning Inbox cards and collection index after review.

Do not add transcripts, source HTML, SQLite files, message-delivery state, provider responses, `.env` files, credentials, or unredacted backups.
