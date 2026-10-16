# Updating the knowledgebase

1. Keep the raw Learning Inbox archive outside this repository.
2. Run `scripts/export_from_learning_inbox.py` against the saved Markdown evidence directory.
3. Inspect `git diff -- data/` for accuracy, relevance, and accidental sensitive material.
4. Commit only the generated cards and index after review.

Do not add transcripts, source HTML, SQLite files, message-delivery state, provider responses, `.env` files, credentials, or unredacted backups.
