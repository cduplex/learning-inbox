# 15 NEW Hermes Agent Skills You Need To Install Today

## Source
- Original: https://www.youtube.com/watch?v=pKNbTQMAc7I
- Type: youtube
- Creator: {'displayName': 'Dubibubi'}
- Published: 2026-10-22T00:00:00.000Z

## Tags
Hermes agent, AI agents, agent skills, automation, coding, email triage, research workflows, privacy, price monitoring, computer use

## Learning guide
**The arc**
A fresh Hermes agent install ships with 58 local skills while the official directory holds over 200, so the question is which ones are actually worth installing. The creator tested them and ranks a personal top 15, moving from app-shipping and media tools through everyday-life, research and automation skills, up to delegating coding work. Along the way he warns that every installed skill costs context on every message, so install deliberately and prune what you do not use.

**1. Understand and find skills**
- **Know what a skill is:** A skill is a small plain-English instruction manual in the agent's inventory that it pulls out when a task needs it. Type `/skills` to see what you have.
- **Look beyond the defaults:** Nous removes skills from default installs when they see no regular use, so older installs had skills new ones lack. Install extras with a command or by pasting the skill link into Hermes.
- **Write clear instructions:** Because skills are plain English, clearer communication makes them more useful. Design workflows so the AI asks the right questions before answering instead of chasing one perfect prompt.

**2. Ship and test your apps**
- **Make a launch video with `/brag`:** Point it at a project folder and it reads the code, picks an angle, writes a storyboard and renders a 15 to 25 second launch video with music and sound effects. Choose a tone: cinematic, App Store, deadpan or YC parody.
- **QA before customers do with Dogfood:** Message the agent "dog food my app" plus the link. It acts like a new user, clicking buttons, filling forms and screenshotting failures, then returns a bug report ranked from critical to minor.
- **Copy real design systems with Popular Web Designs:** It packages 54 design systems such as Stripe, Linear and Vercel, including colors, fonts, spacing and components. Replace vague prompts like "make it modern" with the brand whose look you want.

**3. Create media**
- **Turn clips into text art with ASCII Video:** Feed it a video and get a Matrix-like version rebuilt from colored characters, which can react to music. It runs on a normal computer with no graphics card or API key; use it for reels, short-form video or animated websites.
- **Make a handwriting font with Draw Your Font:** Photograph your handwriting and get an installable font, handy for handwritten-looking thumbnail text.

**4. Handle everyday life**
- **Find your stuff with Find My:** Ask via Telegram where your AirPods are; the agent opens Find My on a Mac, screenshots it and reads the map, and can track an AirTag over a day. It only works when Hermes runs on a Mac; on a VPS all four Apple-only skills are hidden.
- **Shop through Shop:** Search Shopify stores for a size and color, get shipping rates, track orders, start returns, or search by photo, and compare open tabs to find the cheapest supplier. The agent must confirm item, price and address before checkout, and autonomous payment needs a spending budget set in the Shop app.
- **Give the agent a phone with Telephony:** It buys a real number through Twilio, sends and reads texts, and calls you with an AI voice via Bland or Vapi. Twilio and voice providers cost real money; use it for app-break alerts and morning briefings, never spam.
- **Remove your data with Unbroker:** It has playbooks for 22 data-broker sites including Spokeo, WhitePages and BeenVerified. It finds listings, sends opt-outs, clicks verification emails and rescans on a schedule because listings reappear.
- **Find places free with Mouse:** It uses OpenStreetMap for places and directions with no API key. Drop a Telegram location pin and ask for the best open coffee within 500 m.

**5. Research and organize knowledge**
- **Get past blocked pages with Blocked Page Recovery:** When research hits a 403, Cloudflare wall or paywall, it tries Wayback Machine, then Archive.today, then the Gena reader service, then the site's own API. Only if all fail does it open a real browser.
- **Build an LLM Wiki:** Based on Andrej Karpathy's note, the agent reads documents once and maintains linked wiki pages per person, idea and topic instead of rereading sources for every question. Feed it podcasts, transcripts, PDFs and meeting notes, ask where sources disagree, and open the Markdown files in Obsidian.
- **Watch rivals with Competitor News Monitor:** Give it a company list and get a Monday digest of meaningful changes with source links.

**6. Automate and delegate**
- **Track prices with Product Price Monitor:** Give an exact product and the price you would pay; it checks now and sets a cron job to recheck every 6 hours, messaging only when the target hits. Example: Sydney to Nepal return flights, Telegram alert below $1,500.
- **Control no-API apps with Computer Use:** It reads the screen and clicks in the background without moving your mouse or switching windows, so you can write an email while it fills a spreadsheet. Run `Hermes tools`, choose Computer Use and allow installation; any tool-capable model works.
- **Create your own skills with `/learn`:** Point it at a website, folder, PDF or book, or do a process once and run `/learn how I just did that`. Expect drafts that still need editing, like the creator's script-writing skill.
- **Triage email in your voice:** Email Inbox Triage reads 20 to 50 of your sent emails to learn openings, sign-offs, length and refusals, sorts mail into urgent, needs a reply, waiting on someone and noise, and drafts replies without sending. Prompt: "Triage my inbox and draft replies in my voice. Don't send anything." then batch-review and send yourself.
- **Delegate coding with the Claude Code and Codex skill:** Message Hermes from your phone; it opens Claude Code on a server, assigns and monitors the job and reports back, for example fixing a broken stop button and opening a pull request to review on your phone. It needs a Claude or Codex plan on top of Hermes, so you pay for two agents.

**7. Keep the skill index lean**
- **Measure and prune:** Every session pays the index, meaning each installed skill's name and one-line description is sent with every message; cutting defaults from 82 to 58 dropped it from about 1,900 to 1,400 tokens. Check with `Hermes prompt size` and disable truly unused skills with `Hermes skills config`.

**Try this first:** Run `Hermes prompt size`, disable unused skills with `Hermes skills config`, then send "Triage my inbox and draft replies in my voice. Don't send anything." and review the drafts.

## Derived summary
## Overview [00:00:00]
- [00:00:00] The presenter says a new Hermes agent installation has **58 unique skills** available locally, while the official directory has **over 200**; the presenter reviewed them and selected a personal top 15.
- [00:00:47] Presenter attribution: Duby says they build apps daily with Hermes, have earned **over $51,000 in less than 90 days** from apps, and have tested hundreds of skills. These personal and product-performance claims are not independently verified.
- [00:01:06] A skill is described as a small instruction manual held in the agent inventory and used when a task requires it; `/skills` shows available skills.
- [00:01:20] The presenter says Nous removes skills from default installations when they see no regular use, noting older installs included skills that new installs no longer receive.

## #15: Brag launch-video generator [00:01:42]
- [00:01:42] `/brag` is presented as a new skill for people who have shipped an AI-built app.
- [00:01:56] Workflow: point Brag at a project folder, after which it reads the code, chooses an angle, writes a storyboard, and renders a **15-to-25-second** app-launch video.
- [00:02:06] The generated video is said to include music and sound effects; listed tone options are cinematic, App Store, deadpan, and YC parody.
- [00:02:17] The presenter says the originating repository had existed only since June and had passed **11,000 GitHub stars**. This popularity claim is not independently verified.
- [00:02:22] Installation can be done through a command or by pasting the skill link into Hermes, according to the presenter.

## #14: ASCII Video [00:02:33]
- [00:02:35] ASCII Video accepts a video clip and returns a version rebuilt from colored text characters, which the presenter compares to a Matrix-like visual effect.
- [00:02:45] It is said to run on a normal computer without a graphics card or API key.
- [00:02:52] The text can react to music; the presenter suggests potential use in short-form video, reels, and animated websites.

## #13: Dogfood app QA [00:03:05]
- [00:03:07] “Dogfood” comes from “eating your own dog food,” defined here as testing a product before customers do.
- [00:03:18] Give the agent an app link and it reportedly behaves like a new user: clicking buttons, filling forms, and taking screenshots of failures.
- [00:03:27] It returns a bug report prioritized from critical to less important issues.
- [00:03:35] The presenter attributes the skill to Technium, described as a lead Hermes developer at Nous, and frames it as a free on-device QA tester for “vibe coders.”
- [00:03:43] The stated invocation is to message the agent “dog food my app” along with the app link.

## #12: Find My [00:03:49]
- [00:03:49] Find My is presented as a way to ask an agent via Telegram where AirPods are.
- [00:04:05] Because Apple allegedly does not offer a command-line Find My tool, the reported mechanism is screen-based: open Find My on a Mac, take a screenshot, and read the map from the screen.
- [00:04:17] The skill can reportedly track an AirTag over time to show where a bag has been during the day.
- [00:04:25] Caveat: it works only when Hermes runs on a Mac; on a VPS, the presenter says all four Apple-only skills are hidden.

## #11: Shop [00:04:48]
- [00:04:48] Shop is described as an official skill from Shopify’s Shop app, attributed to Shopify product lead Joe Rinaldi Johnson.
- [00:05:06] Reported shopping functions include searching Shopify stores, finding a specified size and color, retrieving shipping rates to an address, tracking orders, and starting returns.
- [00:05:16] A photo of an item can reportedly be used to search for a shop that sells it.
- [00:05:22] Checkout safeguard: the agent must confirm the item, price, and address with the user before checkout.
- [00:05:31] Autonomous payment is said to require a spending budget configured in the Shop app.
- [00:05:37] The presenter suggests using it to compare open shopping tabs and locate the cheapest supplier.

## Sponsor aside: Prompt Engineering for ChatGPT [00:05:49]
- [00:05:49] **Sponsor aside:** The presenter says skills are plain-English instructions, arguing that clearer communication with AI increases their usefulness.
- [00:06:02] Coursera sponsors the video; the promoted beginner course is “Prompt Engineering for ChatGPT,” taught by Dr. Jules White of Vanderbilt University, with **six modules** covering fundamentals through advanced patterns. Promotional claims are not independently verified.
- [00:06:23] One course concept is having AI ask the appropriate questions before generating an answer, rather than attempting one perfect prompt.
- [00:06:37] The presenter says that question-led process design can help custom workflows and skills understand the user’s requirements.

## #10: Telephony [00:06:58]
- [00:06:58] Telephony reportedly lets an agent purchase its own actual phone number through Twilio.
- [00:07:11] It can reportedly send and read texts, plus call the user through an AI voice using Bland or Vapi.
- [00:07:19] The presenter recounts examples involving agents named Henry and Hermes making calls after acquiring numbers and voices; these anecdotes are attributed claims, not independently verified.
- [00:07:47] The presenter says Nous opened an official-skill ticket on March 5 and released it **9 days** later.
- [00:07:51] Cost caveat: Twilio and voice providers charge real money.
- [00:07:58] The presenter cautions against spamming people, stating that the skill itself instructs the agent not to do so; suggested legitimate uses are app-break alerts and morning briefings.

## #9: Unbroker [00:08:13]
- [00:08:19] Unbroker addresses data-broker sites that may publicly list names, addresses, phone numbers, and relatives.
- [00:08:29] It reportedly contains playbooks for **22** large sites, including Spokeo, WhitePages, and BeenVerified.
- [00:08:38] Its stated workflow is to find listings, send opt-out requests, click email verification links, then rescan on a schedule because listings can reappear.
- [00:08:46] The presenter says it was made by the same person behind ASCII Video and that some call it a free alternative to DeleteMe. Those comparative claims are not independently verified.

## #8: Computer Use [00:09:02]
- [00:09:02] Computer Use is described as enabling the agent to operate applications with no API through screen reading and clicking.
- [00:09:11] Unlike ordinary foreground automation, the presenter says it works in the background without moving the user’s mouse, taking the keyboard, or switching windows.
- [00:09:19] Example: a user can write an email while the agent fills out a spreadsheet in another window.
- [00:09:31] The skill is attributed to work with Francesco Bonacchi and Query; the presenter says Query’s main GitHub repository has **over 26,000 stars**.
- [00:09:41] Model caveat: the presenter says any model can be used if it supports tools.
- [00:09:45] Setup instruction supplied in the video: run `Hermes tools`, choose Computer Use, and allow installation.

## #7: Popular Web Designs [00:10:00]
- [00:10:00] Popular Web Designs is aimed at “vibe coders” and is said to package **54** real design systems.
- [00:10:15] The examples given are Stripe, Linear, and Vercel, with their colors, fonts, spacing, and components available for the agent to copy.
- [00:10:25] It reportedly comes from Vault Agent’s design repository, which the presenter says has nearly **118,000 GitHub stars**.
- [00:10:32] Practical prompting advice from the presenter: replace vague requests such as “make it modern” with the name of a brand whose aesthetic is desired.

## #6: Blocked Page Recovery [00:10:44]
- [00:10:44] Blocked Page Recovery targets research failures caused by **403** errors, Cloudflare walls, or paywalls.
- [00:11:03] It provides a five-step fallback sequence.
- [00:11:07] Step 1 is checking the Wayback Machine; step 2 is Archive.today; step 3 is a reader service called Gena; step 4 is the target site’s own API.
- [00:11:14] Step 5, only after the preceding methods fail, is to open a real browser.
- [00:11:20] The presenter says Nous rewrote the skill description in August so agents would remember to use it.

## #5: LLM Wiki [00:11:34]
- [00:11:34] LLM Wiki is introduced through a note by Andrej Karpathy about using AI to organize research; the presenter says that note is included in an agent with almost **250,000 GitHub stars**.
- [00:11:52] The central mechanism is to read documents once, then write and maintain an internal wiki rather than rereading the same documents from scratch for every question.
- [00:12:01] The wiki gets linked pages for each person, idea, and topic, and is kept current as more material is added.
- [00:12:14] Supported input examples are podcasts, transcripts, PDFs, and meeting notes; the presenter suggests asking where those sources disagree.
- [00:12:20] Storage is stated to be Markdown files, which can be opened in Obsidian.

## #4: Product Price Monitor [00:12:31]
- [00:12:31] Give Product Price Monitor an exact desired product, such as shoes or a flight, plus the price the user would pay.
- [00:12:42] It obtains the current price and creates a cron job, defined as a scheduled task, to check again every **6 hours**.
- [00:12:49] It messages the user only when the target price is reached, avoiding repetitive identical alerts.
- [00:12:56] The presenter’s example is return flights from Sydney to Nepal, with a Telegram alert if the price falls below **$1,500**.
- [00:13:06] The presenter analogizes the tool to paying someone to refresh Skyscanner every six hours.
- [00:13:14] The skill is attributed to contributor Ben Barclay, also credited with Hermes’ official GitHub skill.

## #3: `/learn` custom-skill creation [00:13:28]
- [00:13:28] `/learn` is ranked third even though the presenter says it is technically not a skill itself, but the feature that creates skills.
- [00:13:40] The command can be pointed at a website, folder, PDF, or a whole book; the agent reads the material and writes a new skill.
- [00:13:53] The presenter’s preferred workflow is to demonstrate a process once, then invoke `/learn how I just did that` so the agent can repeat it.
- [00:14:01] Personal example: the presenter taught the agent a script-writing process and linked it to a YouTube channel; they say the current video’s script was generated with Hermes.
- [00:14:10] Caveat: the generated script is not perfect and still requires editing, though the presenter prefers editing a draft to writing from scratch.
- [00:14:22] The presenter says the feature launched in June and cites Derek Chung calling it underrated; this is an attributed opinion.

## Skill-index context cost [00:14:36]
- [00:14:36] The presenter warns that installing more skills has a cost even if documentation says skills do not consume tokens until used.
- [00:14:48] The video cites source-code wording that “Every session pays the index.”
- [00:14:55] “Index” is defined as every installed skill’s name and one-line description being sent with every message.
- [00:15:02] This overhead is offered as the reason default skills have been removed: Hermes reportedly changed from **82** defaults in August to **58**, reducing the index from roughly **1,900 tokens** to around **1,400 tokens**.
- [00:15:18] The presenter recommends checking context use with `Hermes prompt size`, then using `Hermes skills config` to disable genuinely unused skills.

## #2: Email Inbox Triage [00:15:38]
- [00:15:38] Email Inbox Triage is ranked highly because the presenter says it can learn how they personally sound in email.
- [00:15:56] Before drafting, it reportedly reads **20 to 50** emails the user actually sent and extracts patterns in openings, sign-offs, length, and refusals.
- [00:16:08] Example: it can draft a polite refusal to a collaboration-call request in the user’s voice, reducing a task the presenter says might normally take 10 minutes.
- [00:16:18] It organizes mail into categories including urgent, needs a reply, waiting on someone, and noise.
- [00:16:25] It drafts needed replies but does not send by default. The skill explicitly states that handling the inbox is not permission to send.
- [00:16:36] The workflow is batch review and approval of drafts.
- [00:16:40] The presenter says they used it over the prior **48 hours** of inbox activity and that Hermes created every reply, but they still manually sent each message. This is a personal claim, not independently verified.
- [00:17:08] The stated prompt is: “Triage my inbox and draft replies in my voice. Don’t send anything.”

## Honorable mentions [00:17:16]
- [00:17:25] Pokémon Player reportedly lets an agent play Pokémon by reading game memory for HP and position, then screenshotting the map for navigation.
- [00:17:37] Draw Your Font converts a photo of handwriting into an installable font; the presenter suggests it for handwritten-looking thumbnail text.
- [00:17:48] Mouse uses OpenStreetMap to find places, directions, and nearby locations for free without an API key.
- [00:17:53] Example Mouse query: drop a Telegram location pin and ask for the best coffee within **500 m** that is currently open.
- [00:18:03] Competitor News Monitor takes a company list and sends a Monday digest of meaningful changes with source links.

## #1: Claude Code and Codex [00:18:27]
- [00:18:27] The presenter ranks the Claude Code and Codex skill first and describes it as making Hermes a manager that delegates coding jobs to Claude Code.
- [00:18:41] The stated remote workflow is: message Hermes from a phone, have it open Claude Code on a server, assign the job, monitor the work, and message back once complete.
- [00:18:54] The presenter ranks it first because it “ships” work for them, which is a personal assessment.
- [00:18:59] The skill is said to be the largest in the bundle at approximately **35,000 characters**, nearly twice the length of this video’s script, and to exceed Nous’ normal skill-size rule.
- [00:19:14] Personal example: while with friends, the presenter messaged Hermes about a broken app stop button; it allegedly had Claude Code find and fix the bug, open a pull request, and leave the presenter to review it on a phone.
- [00:19:28] Cost caveat: this requires a Claude or Codex plan in addition to Hermes, so the presenter describes it as paying for two agents; they say it is covered under their **$200 plan**.

## Final recap [00:19:41]
- [00:19:41] The presenter’s top-15 list emphasizes launch-video creation, media effects, QA, Apple tracking, shopping, telephony, privacy opt-outs, background computer control, design references, research recovery and organization, price monitoring, custom skill creation, email drafting, and remote coding delegation.
- [00:19:41] A cross-cutting tradeoff is capability versus constraints: platform requirements affect Find My, third-party services add telephony and coding-plan costs, checkout and email have human-approval safeguards, and a larger installed skill index consumes context on every session.
- [00:19:53] The presenter closes by pointing viewers to a separate video about third-party skills outside the bundled set.

## Evidence anchors
- [00:00:00.000] Did you know the second you install
- [00:00:21.760] official directory, that's over 200
- [00:01:06.680] you're new to all of this, a skill is
- [00:01:56.720] cool. You point it at your project
- [00:02:35.612] 14, ASCII video. You send your agent any

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
