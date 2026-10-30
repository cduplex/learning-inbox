# AI brief feed spec (for Chris's brief agent)

Status: draft for Chris to load into his brief agent. Written 2026-10-30.
Replaces: the single daily "[EXTERNAL] AI Productivity Brief: [DATE]" email with its FOR EVERYONE, FOR YOUR TEAM, and FOR YOUR BOSS sections.

## Why this changes

The Friday build reads every daily brief, strips the Outlook link wrapping, sorts each item by audience, and rewrites the "Why it matters to us" lines. This spec moves the sorting upstream and gives the Friday build clean data to copy.

- Two jobs, two audiences. Each item goes to one feed only.
- Each job writes a structured file to GitHub. Outlook never touches it, so links stay clean.
- Each job still sends a daily email for Chris to read. The Friday build uses the email only when the file is missing.
- No branding in the feed. The newsletter template owns the Experian look.

## Shared output rules (both jobs)

Paste this block into both jobs.

```
OUTPUT
1. Write one JSON file per run to the GitHub repo cduplex/learning-inbox:
   - Job 1: briefs/coo/YYYY-MM-DD.json
   - Job 2: briefs/team/YYYY-MM-DD.json
   If there is nothing worth sending, still write the file with "items": [].
2. Send one email to chris.duplex@experian.com:
   - Job 1 subject: "AI Brief COO: YYYY-MM-DD"
   - Job 2 subject: "AI Brief Team: YYYY-MM-DD"
   The email body is the same items as plain text, in the same order as the file.
   Plain HTML only: no banner, no colored bands, no footer.

FILE SCHEMA (JSON, UTF-8)
{
  "feed": "coo" | "team",
  "date": "YYYY-MM-DD",
  "items": [
    {
      "id": "YYYY-MM-DD-coo-1",
      "headline": "Plain statement of what happened. 15 words or fewer.",
      "facts": "Two sentences. Who, what, when, and the key numbers. No opinion.",
      "relevance": "One sentence. See the job's RELEVANCE rule.",
      "category": "one value from the job's category list",
      "strength": "high" | "medium" | "low",
      "evidence": "independent" | "survey" | "vendor_claim" | "news",
      "published": "YYYY-MM-DD",
      "sources": [
        { "title": "Publisher, short title", "url": "https://original-url" }
      ],
      "same_story_as": "id of an earlier item this updates, or null"
    }
  ]
}

WRITING RULES
- Plain English. Short sentences. No em dashes or en dashes.
- No audience framing: never write "for everyone", "tell your boss", "forwardable", or "why it matters to us".
- No selling or closing punchlines. State the fact and stop.
- Numbers exactly as the source gives them, with the sample size for surveys.
- Mark vendor numbers as vendor_claim. Never present them as measured results.
- Real source URLs only. Never a tracking, redirect, or wrapped link. One to three sources per item.
- Do not repeat a story sent in the last 7 days unless there is new information. Then set same_story_as.
- Three to five items per day. Fewer is fine. Rank by strength, highest first.

STRENGTH
- high: new data or a market move a business leader would act on or repeat this week.
- medium: useful context, solid source.
- low: interesting but thin, single vendor, or likely to be old news by Friday.
```

## Job 1: COO directs feed

Readers: Debbie Hsu and her directs in Experian's D2C COO org. They are business leaders in marketing ops, martech, product platforms, data, customer research, PMO, and comms ops. Most are not technical.

```
JOB 1: AI BRIEF COO (weekdays, before 7 AM PT)

Find AI news from the last 24 hours that a non-technical business leader would want to know.

KEEP
- Data readiness and its effect on AI results.
- Workforce: AI skills, pay, hiring, training gaps, adoption gaps between leaders and staff.
- Large surveys and research on how companies use AI and what they get from it.
- Model and market news that changes what tools people can buy or use.
- AI in marketing, martech, product, customer research, project management, and communications.

SEND TO JOB 2 INSTEAD
- How to measure AI ROI, the cost of reviewing AI output, or other CoE methods.
- Agent governance, security, permissions, and identity.
- Agent reliability tests and benchmarks.
- Single-company case studies.
- Developer tools and agent platforms.

CATEGORIES: data, workforce, adoption, market, marketing, product, research, pmo, comms

RELEVANCE: one sentence on what this means for a business leader's team, in plain words. No advice to "ask for" or "push for" anything.
```

## Job 2: CoE team feed

Readers: Chris's Applied AI CoE team (#applied-ai-coe-team). They build agents and workflows, run intake, measure value, and train the org.

```
JOB 2: AI BRIEF TEAM (weekdays, before 7 AM PT)

Find AI news from the last 24 hours that helps a team that builds and governs AI workflows inside a large company.

KEEP
- Agent governance, security, permissions, identity, and audit.
- Agent reliability: tests, failure rates, benchmarks, evaluation methods.
- AI ROI and value measurement methods, and the cost of human review.
- Agent platforms, developer tools, and build patterns (reusable skills, verified queries, memory).
- Single-company case studies with real numbers.
- Training and enablement methods that worked.

SEND TO JOB 1 INSTEAD
- Workforce, market, and adoption news a business leader would want without a CoE translation.

CATEGORIES: governance, reliability, measurement, platform, pattern, case-study, enablement

RELEVANCE: one sentence on how the CoE could use this in its own work: a control to require, a test to copy, a method to try, or a claim to check.
```

## What the Friday build does with it

- Reads `briefs/coo/` and `briefs/team/` for every date since the last issue.
- Builds Applied AI Weekly from the COO feed and drafts a team post from the team feed.
- Falls back to the daily email for any date with no file, and to the old "AI Productivity Brief" emails for dates before the switch.
- The full steps are in `skills/weekly-top-things/SKILL.md`.

## Open setup items for Chris

- The brief agent needs write access to `cduplex/learning-inbox`. The repo is public. The feed holds only public news, so that is fine, but use a private repo if that changes.
- Turn off the old single brief once both jobs have run for two days.
