# I Tried 100+ Github Repos for Claude. These 6 Are the Best

## Source
- Original: https://www.youtube.com/watch?v=HhZdNYI4pJs
- Type: youtube
- Creator: {'displayName': 'Nate Herk | AI Automation'}
- Published: 2026-10-11T00:00:00.000Z

## Tags
Claude, GitHub repositories, AI agents, automation, video editing, web development, mobile apps, testing, security, SEO

## Derived summary
## Overview [00:00:00]
- [00:00:00] The speaker claims there are over 100,000 GitHub repositories built for Claude, says most are not worthwhile, and presents 10 repositories selected after personally trying more than 100.
- [00:00:09] The speaker claims the selected tools can speed up projects, replace paid tools, and replace parts of their workflow. These capability and outcome claims are not independently verified.
- [00:00:17] The stated goal is to explain what each repository solves, how to use it, and how it could support building services businesses would pay for.

## 1. Hyperframes for video generation and editing [00:00:25]
- [00:00:27] Hyperframes is identified as the first repository and attributed to Haygen.
- [00:00:30] The speaker says it has taken over a large portion of their video-editing work.
- [00:00:32] The described workflow is: state the desired result in natural language, have Claude construct the video using HTML and animations, then have Hyperframes render a real MP4 locally.
- [00:00:41] Listed output types include captions, motion graphics, title cards, and product promotions.
- [00:00:45] The speaker says they build skills on top of Hyperframes for YouTube intros, Instagram Reels, course videos, advertisements, and other formats.
- [00:00:54] Example workflow: supply a raw clip and ask for captions and a title card, or ask for conversion into an Instagram Reel; the speaker says a finished file can result within a few minutes.
- [00:01:03] The speaker compares it with Remotion, says they have had more success with Hyperframes, and states that the endorsement is not sponsored.
- [00:01:10] The speaker says Hyperframes is open source, has no per-render fees, and is completely free.
- [00:01:15] Business example: a gym wanting 20 captioned clips per month could be offered a monthly content package. The speaker says no prior video-editing experience is required to use these tools.

## 2. Google Workspace CLI for operational automation [00:01:28]
- [00:01:28] The second repository is the Google Workspace CLI, which the speaker says they use heavily.
- [00:01:32] The speaker says it lets Claude work with Google Drive, Gmail, Calendar, Docs, Sheets, and Slides, with formatting handled through the command-line interface.
- [00:01:43] The stated contrast with Claude's built-in Google connector is that the connector works only in the Claude desktop app and does not cover everything.
- [00:01:48] Because it is a CLI, the speaker says Claude Code, CodeX, or another agent can use it. It reportedly includes more than 40 skills.
- [00:01:59] Setup reportedly takes a few minutes but requires a Google Cloud project for login; Claude can guide setup step by step, while the user grants access only to desired apps.
- [00:02:09] The speaker frames weekly reports, invoices, and follow-up emails as small-business processes that could be automated faster.

## 3. Apify MCP server for inaccessible web data [00:02:16]
- [00:02:16] The third item is Apify, specifically the Apify MCP server.
- [00:02:20] The stated problem is that Claude cannot natively access some web data, including content on sites such as Instagram and Reddit that may block access or require JavaScript rendering, yielding an empty page.
- [00:02:31] The speaker says Apify connects Claude to thousands of ready-made scrapers for Instagram, TikTok, Amazon, and other sites.
- [00:02:37] Example prompt: find Chicago bakeries on Instagram, return follower counts, download videos, and identify profiles without websites in their bios. The claimed result is a spreadsheet after a couple of minutes.
- [00:02:48] The connector is said to be open source, but the scrapers run in Apify's cloud and may cost money depending on the scraper.
- [00:02:55] The speaker says the free plan includes $5 of monthly credit and that some actors may charge per result.
- [00:03:02] Firecrawl is mentioned as another open-source scraping-related option, while the speaker says Apify has been easy to use.

## 4. Scrollcraft for custom scrolling websites [00:03:08]
- [00:03:08] Disclosure: the speaker says they built Scrollcraft.
- [00:03:13] The intended reference experience is an Apple-style site where scrolling moves the page like a movie through layered, immersive sections.
- [00:03:19] The speaker says a generic Claude request tends to produce a basic page with text fade-ins, whereas Scrollcraft provides a real scroll engine and design rules derived from the speaker's website work.
- [00:03:31] It reportedly includes a checker that screenshots scroll states and inspects positions so Claude can correct issues before the user explicitly flags them.
- [00:03:38] The speaker says they use the repository for their AI automation society site, personal site, event sites, and every site they build.
- [00:03:45] The speaker emphasizes that sites need not all be highly scroll-driven; the repository is said to address taste, depth, layering, spacing, typography, color schemes, and overall design feel.
- [00:03:59] The speaker's design rationale is that a website should feel good and convert visitors toward a desired action. They characterize basic AI-made landing pages as a commodity, while claiming online brands still pay for custom scroll experiences that are harder to produce with simple vibe coding.

## 5. Humanizer for rewriting AI-sounding copy [00:04:17]
- [00:04:19] Humanizer is described as a repository the speaker found accidentally and has used on every product since.
- [00:04:23] Its purpose is to make Claude's writing sound less like “AI slop.”
- [00:04:27] The speaker says it is built on a guide Wikipedia editors use to identify AI-generated text.
- [00:04:31] Claimed AI-writing signals include contrast constructions such as “not this, but that,” repeated groups of three, and over-hyped wording.
- [00:04:43] The workflow is to paste website copy, a cold email, or another draft, then ask Claude to humanize it using the repository.
- [00:04:49] The speaker says it retains the intended message while removing elements that can cause readers to disengage or lose trust; they argue person-written-sounding copy is easier to pitch than AI-generated content.

## 6. Agent Skills for persistent build specifications [00:04:59]
- [00:04:59] The speaker divides the list: the first five tools are framed as useful for landing a client, while the remaining tools concern building real client products.
- [00:05:07] Example client product: a cleaning company needs customers to book online and pay a deposit.
- [00:05:11] The speaker describes a long-session failure mode where Claude appears to forget prior details after one or two hours because sessions are compacted or suffer “context rot,” with earlier details summarized away.
- [00:05:22] Repository six is Agent Skills by Addy Osmani. The speaker says Osmani spent 14 years at Google and now works on Claude Code at Anthropic.
- [00:05:31] Its core mechanism is to move the plan from chat into files.
- [00:05:34] The described command workflow is: `/spec` creates a specification collaboratively; `/plan` breaks work into small tasks; `/build` executes tasks one at a time with a check for each.
- [00:05:44] When a session becomes messy, the speaker says a fresh session can resume from the saved files.
- [00:05:49] The specification is said to surface edge cases such as double bookings, refunds, and customers in different time zones, which should be incorporated before building.
- [00:05:59] The spec can be given to the client before implementation to clarify what they will receive and maintain alignment during the project.
- [00:06:06] The speaker says Superpowers remains good but considers Addy Osmani's skills easier for newcomers; Matt Pocock's skills are mentioned as especially useful for building with a developer mindset, even for non-developers.

## 7. Expo skills for mobile apps [00:06:23]
- [00:06:24] Repository seven is Expo's official skills for mobile applications.
- [00:06:26] The speaker claims these can take an idea to a real app running on an iPhone in an afternoon, including from Windows. This performance claim is not independently verified.
- [00:06:32] The skills reportedly include Expo's list of 20 indicators that make an app look AI-built, plus current rules for App Store submission.
- [00:06:40] Practical instruction: explicitly tell Claude to use Expo skills by name because they may not load automatically.
- [00:06:43] For TestFlight or App Store distribution, the speaker says an Apple Developer account costs $99 per year.
- [00:06:49] Sales framing: rather than replace a shop's existing software such as Square, sell the specific workflow that its current software does not accommodate.

## 8. Supabase and Stripe skills for backend, auth, and payments [00:07:01]
- [00:07:01] Repository eight concerns the backend of an app or software product, using Supabase and Stripe's official skills.
- [00:07:08] The speaker positions these tools for applications needing logins, databases, or payments.
- [00:07:11] The claimed benefit is that Claude can follow company-specific security rules, including restricting users to their own data and verifying that a payment actually came from Stripe.
- [00:07:18] The speaker advises installing only the Stripe skill called “Stripe best practices,” rather than the full plugin, because the full plugin might route every vendor choice through Stripe.
- [00:07:26] Suggested pre-launch safeguard: set the Supabase connector to read-only, log in as a test user, and confirm that the account cannot see another user's data.
- [00:07:34] The speaker frames these skills as support for vibe coders who find backend, payment, and security concerns confusing.

## 9. Testing and security review before delivery [00:07:40]
- [00:07:42] Repository nine is presented as a pre-delivery step for anything handed to a client or released publicly.
- [00:07:46] The speaker cautions that Claude may say a feature works without having actually clicked through or validated it.
- [00:07:52] Playwright CLI from Microsoft is described as opening a real browser, clicking through an app as a customer would, and writing reusable tests that verify behavior repeatedly.
- [00:08:00] Because it is a CLI rather than an MCP, the speaker says it does not place the whole page into Claude's context, making it lighter on tokens and faster.
- [00:08:08] The stated use is to validate many behaviors and find edge cases.
- [00:08:12] Claude Security is identified as Anthropic's security plugin; the speaker says it uses multiple agents to look for code vulnerabilities, with separate agents attempting to challenge one another's findings.
- [00:08:22] The speaker says the output is a plain-English report of findings that remain, after which it can write and execute patches.
- [00:08:29] Client-facing priorities are framed as a working booking form and no leakage of customer data, leading the speaker to recommend building testing and security into every project.

## 10. Open SEO for discoverability [00:08:37]
- [00:08:37] The final repository is Open SEO, positioned for after a site or app goes live because people still need to find it.
- [00:08:43] The speaker says it connects Claude to keyword data, rankings, and backlinks, and can identify the exact page and keyword position instead of giving generic advice.
- [00:08:50] The speaker says agencies can use this kind of audit to win a monthly SEO retainer.
- [00:08:54] Caveats: free-trial credits are small, and data is stored on the provider's server by default unless self-hosted.

## Token-saving tools and cautions [00:08:59]
- [00:08:59] The speaker discusses token-saving repositories including Caveman, RTK, and Ponytail, citing JetBrains tests on real coding tasks.
- [00:09:07] According to the speaker's report of those tests, Caveman reduced output tokens by about 8.5%, versus an advertised 65%.
- [00:09:12] The speaker says RTK did not save anything in the tests and, at low effort, made tasks more expensive.
- [00:09:17] Ponytail reportedly saved about 10% per task, roughly half its advertised result, but has an open Windows bug that can stall each message for several seconds.
- [00:09:27] Codeburn is suggested for seeing token spending and flagging waste, such as an MCP server that is unused but loaded on every message.
- [00:09:36] The speaker retracts enthusiasm for two previously recommended tools: Claude Mem sends usage data by default, and Context Mode has an open bug that can consume usage.

## Final recap and workflow [00:09:46]
- [00:09:49] The speaker advises beginners not to install every repository at once, since troubleshooting becomes difficult when multiple additions could have caused a failure.
- [00:09:56] The recommended selection rule is to choose the repository that addresses the current biggest problem.
- [00:10:01] If uncertain, the speaker suggests starting with the Google CLI, Apify, or Scrollcraft, with Humanizer also characterized as especially simple.
- [00:10:07] The speaker's client-acquisition workflow is: identify businesses with no website, build one from a sample page, improve the copy, and send the link.
- [00:10:13] Final sales principle: repositories themselves are free and broadly installable; the service being sold is the solution built around them for the client's problem.
- [00:10:20] The speaker says links to every repository covered will be placed in the video's description.

## Practical applications
- Suggestion: Start with one repository tied to a current bottleneck, rather than installing the full set at once, and isolate changes so failures are easier to trace.
- Suggestion: For a client build, create a written specification, convert it into small tasks, and retain it in project files so a fresh agent session can resume without relying on chat context.
- Suggestion: Before launch, use browser-based tests for critical customer paths such as booking and payment, then test data isolation with a separate user account.
- Suggestion: For a service offering, package a delivered outcome such as captioned clips, a booking workflow, a custom website experience, or an operational automation, rather than selling repository access itself.
- Suggestion: Evaluate claimed token savings and hosted-service costs against actual project usage, including free-credit limits, per-result charges, data-hosting defaults, and reported platform-specific bugs.

## Evidence anchors
- [00:00:00.000] So, there are over 100,000 GitHub repos
- [00:00:07.280] than 100 repos, I found 10 that I cannot
- [00:00:32.160] editing. You basically just tell Claude
- [00:00:35.080] it builds the video out of HTML and
- [00:00:36.880] animations, and Hyperframes renders a

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
