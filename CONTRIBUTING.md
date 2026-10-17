# Updating the knowledgebase

## Collection ownership

- Learning Inbox automation owns only `data/learning-inbox/**`.
- Muse owns only `data/muse-instagram/**`; follow [`MUSE-PUBLISHING.md`](MUSE-PUBLISHING.md).
- The top-level `data/INDEX.md` is a collection directory. Do not overwrite it from a pipeline exporter.

## Validation

Run `python3 scripts/validate_collections.py` locally before publishing collection changes and fix every violation. The GitHub Actions workflow provides non-blocking regression visibility; `main` has no required pull request, review, or status-check gate. Dependabot checks the pinned GitHub Actions weekly and opens a pull request when an update is available.

## Learning Inbox updates

1. Keep the raw Learning Inbox archive outside this repository.
2. Run `scripts/export_from_learning_inbox.py` against the saved Markdown evidence directory with `--output data/learning-inbox`.
3. Inspect `git diff -- data/learning-inbox/` for accuracy, relevance, and accidental sensitive material.
4. Commit only the generated Learning Inbox cards and collection index after review.

Do not add transcripts, source HTML, SQLite files, message-delivery state, provider responses, `.env` files, credentials, or unredacted backups.
