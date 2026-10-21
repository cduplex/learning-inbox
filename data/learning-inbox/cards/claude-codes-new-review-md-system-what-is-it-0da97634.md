# Claude Codes New REVIEW.md System, What is it?

## Source
- Original: https://www.youtube.com/watch?v=bls8ZJ_INMQ
- Type: youtube
- Creator: {'displayName': 'Rob Shocks'}
- Published: 2026-10-19T00:00:00.000Z

## Tags
AI-assisted development, code review, software delivery, automated testing, risk-based approvals, rollback, feature flags, agent evaluation, merge queue

## Derived summary
The source describes a reported AI-assisted software-development workflow attributed to Anthropic/Claude Code: code production and merge volume allegedly rose while reversions fell, prompting a shift from end-of-PR human reading toward continuous automated verification, AI review, risk-scaled human approval, merge-queue checks, staged releases, and rapid rollback. It presents review as a system for both defect detection and knowledge sharing, reframing the operational question as which human or automated check can best catch each risk. The source also notes limits: intensive AI review can loop on old or low-value findings, so review-round caps, diff-focused re-review, and incident-derived evaluations are described as mitigations. Several performance, product, and infrastructure statements are presented as reported claims rather than independently verified facts.

## Practical applications
- Suggestion: Treat automated verification as evidence-producing work before review—for example, require runnable tests, builds, end-to-end checks, and recorded outputs for an agent-generated change. (p0151-p0163)
- Suggestion: Use risk tiers based on the change and its potential blast radius, with lighter paths for low-risk changes and additional human approvals for higher-risk changes. (p0247-p0255, p0264-p0277)
- Suggestion: Preserve explicit human accountability for agent-authored pull requests; the source says an agent approval does not fill a human approval slot and assigns responsibility to the person directing the change. (p0273-p0291)
- Suggestion: Pair faster automated review with outcome guardrails such as reversion and incident rates, so apparent review-time savings are not merely shifted into later remediation. (p0124-p0137)
- Suggestion: Add staged rollout, feature flags, fast detection, and rollback capability before expanding autonomous changes, limiting customer impact when checks miss problems. (p0307-p0325)
- Suggestion: Cap repetitive AI-review cycles and switch later passes to reviewing only the new diff; convert confirmed historical incidents into a recurring evaluation set for the reviewer. (p0394-p0416)

## Evidence anchors
- [00:00:00.080] So claw code now writes about 90% of its
- [00:00:03.120] own code and things are really speeding
- [00:00:13.840] merged pull requests that's work being
- [00:00:15.440] done more than doubled. But the key
- [00:00:17.680] thing here is the code that was being

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
