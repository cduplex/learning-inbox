# Jev in practice: 13 use cases from ad analysis to visitor intelligence

## Source
- Original: https://www.instagram.com/reel/DdmpM2nNRrY/
- Platform: Instagram Reel
- Creator: @angus.sewell (Angus the Nontechnical)
- Published: 2026-09-22T13:57:43
- Processed: 2026-10-16T23:38:21Z

## Tags
jev, ai-automation, sales-marketing, lead-generation, use-cases

## Core components
- Jev: an AI wrapper tool the creator is building, demonstrated across 13 use cases
- The visitor intelligence workflow: PostHog analytics detects a new site visitor, the IP address is enriched to company and location, matched to a HubSpot CRM contact, and personalized follow-up emails are generated from pages viewed
- Other demos: analyzing 724 competitor ads from 37 brands, classifying 1,500 emails, an adaptable ad-blocker browser extension, live Zoom call coaching with real-time transcripts, and matching new leads to candidate messages

## Derived summary
Angus, a self-described nontechnical builder, walks through "Jev," an AI wrapper tool he is developing, with screen recordings of multiple use cases. He shows analyzing 724 competitor ads from 37 brands, classifying 1,500 emails, building an adaptable ad-blocker browser extension, and most prominently a website visitor intelligence workflow: PostHog analytics detects new site visitors, their IP address is enriched to identify company and location, the visitor is matched to a HubSpot CRM contact, and personalized follow-up emails are generated automatically based on pages viewed. Additional demos include live Zoom call coaching with real-time transcripts and matching new leads to candidate messages. The tone is fast-paced and promotional, ending with a comment-gated offer of free prompt packs. Commenters are split: some are curious, while others argue Jev is merely a wrapper around existing models with no novel reasoning, and compare it unfavorably to alternatives. The demos use example data (a sample contact is shown), and the claims are the creator's own, not verified results.

## Practical takeaways
- The reusable pattern is enrichment plus CRM plus LLM drafting: detect a signal, enrich it, match it, and generate the outreach from behavior data.
- Distinguish the wrapper from the model: ask what Jev does that a plain LLM call would not, before committing to a dependency.
- Email classification and ad analysis at this scale are now commodity capabilities; the differentiation is in the workflow around them, not the model.
- Use sample data in demos; the reel's strongest workflow still reads well when the data is clearly illustrative.

## Notes
This card is derived from a private Muse processing record. Verify important claims against the original source.
