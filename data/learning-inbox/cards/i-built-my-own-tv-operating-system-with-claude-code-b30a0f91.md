# I Built My Own TV Operating System With Claude Code

## Source
- Original: https://www.youtube.com/watch?v=i0ytu6k8uac
- Type: youtube
- Creator: {'displayName': 'Lukas Margerie'}
- Published: 2026-10-21T00:00:00.000Z

## Tags
smart TV, Google TV, Android TV, Claude Code, custom launcher, USB debugging, Magic Path, Mobbin, Rive CLI, UI design, reverse engineering

## Derived summary
## [00:00:00] Context: AI-assisted smart-TV customization
- [00:00:00] The presenter says they have seen X posts about smart-TV owners using AI both to remove ads and to create different TV interfaces.
- [00:00:15] One cited post claims its author used Claude to remove preinstalled bloatware and ads, recreate the operating system with an Apple TV-inspired design, reduce RAM use by 70%, and make the interface three times faster. These are third-party claims presented by the video and are not independently verified.
- [00:00:33] Other cited examples include making a more minimal UI and a screensaver containing revenue, calendar, weather, and Stripe-payment notifications. The cited user says they gave an AI the TV listing, asked whether it could be hacked, and received guidance.

## [00:00:52] Reverse-engineering premise and cited examples
- [00:00:52] The presenter frames these projects as stemming from reverse engineering or “reverse hacking.”
- [00:01:01] They describe a GitHub repository that can be given to Claude Code and that reportedly lets Claude Code or Codex inspect an app down to its binary and explain how a feature works. This capability description is the presenter’s claim and is not independently verified.
- [00:01:13] The presenter cites mash-up game examples combining Mario with Call of Duty, Roblox, Minecraft, and GTA.
- [00:01:23] Another cited use is recreating Adobe-like software: Photocraft as Photoshop, Vectorcraft as Illustrator, and Filmcraft as Premiere Pro. The presenter says these projects are open source, clonable, and customizable.
- [00:01:44] The presenter transitions from the general reverse-engineering principle to modifying their own Google TV’s traditional Android-based interface.
- [00:02:01] They say the demonstrated after-state was achieved with two or three prompts and characterize getting started as easy.

## [00:02:13] Aside: community promotion
- [00:02:13] **Aside, promotional:** The presenter mentions a free Discord community with weekly co-working sessions, biweekly challenges, and a stated $250 giveaway at the end of that week.

## [00:02:30] Initial TV connection and debugging workflow
- [00:02:30] The presenter uses a tweet from Codilla as a quick setup guide and copies a large prompt from it into Claude Code.
- [00:02:52] Step 1 is to put the computer and TV on the same Wi-Fi network.
- [00:02:56] The next described step is to paste the prompt into Claude Code together with a photo of the TV.
- [00:03:05] The presenter recommends photographing the TV’s operating-system information rather than merely photographing the TV: go to Settings, choose About, and photograph that screen so the agent has better OS context.
- [00:03:24] In the demonstration, Claude Code identifies the device as a TCL running Android TV OS 14 and finds it on the local network because both devices share Wi-Fi.
- [00:03:33] The presenter says it took about 3 to 4 minutes before the tool supplied a list of directions.
- [00:03:42] Following those directions on the remote, the presenter enables USB debugging, selects “always allow from this computer,” and presses Allow.
- [00:03:47] If the relevant setting cannot be found on another TV, the presenter suggests searching for “USB debugging” plus the TV or TV-operating-system name and looking for YouTube guides.
- [00:04:09] After setup, the TV begins playing a YouTube video. The first run is described as slow, while the second and third attempts become faster; the test video is Big Buck Bunny.

## [00:04:23] Optional shortcut automation with Type Safe
- [00:04:23] The presenter says others integrate “Jev” by Type Safe into this workflow for faster handling of specific decision paths.
- [00:04:40] Their example is a command such as opening a particular YouTube channel: Claude Code can reportedly be preset to use Jev so that command opens more quickly. This is a presenter claim and is not independently verified.
- [00:04:51] The stated setup is to use the Type Safe skill, log in to Type Safe, copy its prompt, and provide that prompt to Claude Code.

## [00:05:01] Building and testing a replacement Android TV home screen
- [00:05:01] The presenter asks whether a custom home-screen interface is theoretically possible. Claude Code responds that an Android TV app declaring itself a home screen can replace Google TV Home.
- [00:05:12] The presenter asks Claude Code to build a new home-screen app without providing art direction or a design style.
- [00:05:27] The resulting TV interface is characterized as somewhat “janky” but functional: the presenter can change channels, select apps, and navigate to those apps.
- [00:05:37] As an experiment, the presenter requests a TV home UI resembling a chicken laying eggs, with each egg representing an app.
- [00:05:45] The presenter says implementation of the chicken-and-eggs design took around 5 minutes and that the eggs correspond to apps on their Google TV.

## [00:05:57] Magic Path for recreating and remixing the interface
- [00:05:57] The presenter asks Claude Code to add the TV’s original home design into an Open Magic Path project.
- [00:06:07] Magic Path is described as a canvas view for Codex or ChatGPT where a user can create a file, place designs on an open canvas, remix those designs, and create new variants.
- [00:06:28] For a first-time connection to Claude Code, the presenter says to select Claude Code in Magic Path and follow its stated three or four connection steps.
- [00:06:40] The imported result is described as a one-to-one copy of the original TV UI; the presenter navigates it with arrow keys through viewing items and apps.

## [00:07:02] Mobbin-informed layout variants
- [00:07:02] The presenter introduces Mobbin as a large database of app and website screens and says its MCP can connect to Claude Code.
- [00:07:16] They say this connection means Claude Code can use chat context to find UI elements relevant to the project without the user manually browsing Mobbin’s database.
- [00:07:28] The presenter asks Claude Code to use Mobbin findings to improve the Google TV home layout. Examples mentioned include HBO Max, Paramount Plus, Netflix, and The New York Times layouts.
- [00:07:45] The workflow supports selecting components from different references, such as preferring one feature from Paramount Plus and another from Disney Plus, then combining them into new variants.
- [00:07:57] The presenter’s concrete prompt is to create two variants that remix the Google TV home component with Mobbin findings.
- [00:08:08] One resulting variant adds two buttons, retains a broadly similar layout, includes image switchers, and offers a “more info” action rather than immediately navigating to the selected item.
- [00:08:28] The other variant adds a banner with preview images, category selection, and a reordered content hierarchy: apps first, then top picks, continue watching, and top-selling movies.

## [00:08:47] Rive CLI for interaction design
- [00:08:47] A community member named Jerry is cited as testing the approach with the Rive app CLI to create more dynamic interactions.
- [00:09:05] The cited interaction example includes a background switcher with transitions and subtle button switching; the presenter says Rive CLI can be supplied to an agent in Claude Code.
- [00:09:19] The presenter selects a preferred layout variant, duplicates it, and asks Claude Code how Rive CLI could improve the interaction design.
- [00:09:30] Claude Code suggests a focus frame, hero timer, transitions, Play and More Info buttons, app-launch behavior, and small details.
- [00:09:38] The demonstrated changes include a border that moves among focused selections and a text hover animation, which the presenter attributes to Rive.
- [00:09:53] The presenter then copies Jerry’s tweet URL and requests its glow-effect style. They say the result matches that style and that they further add particles at the bottom.
- [00:10:12] The resulting switcher automatically cycles through channels and apps.
- [00:10:22] The presenter says the real-TV version is identical to the Magic Path build.
- [00:10:30] They add a “cloud” tab in the navigation bar. It does not work in the preview but works on the TV, where it opens a browser for logging in to Claude and then prompting or building with Claude on the TV.

## [00:10:47] Referencing an external Samsung Frame redesign
- [00:10:47] The presenter recommends an article by Nathan Clark titled “I gave my Samsung frame a new home screen,” saying it provides a step-by-step setup and has a clean UI style.
- [00:11:15] Their proposed workflow is to copy an article URL into Claude Code, ask it to read the article, and ask it to implement that style as a new Magic Path variant for preview.
- [00:11:28] The displayed preview retains the apps built earlier, including the cloud app.
- [00:11:37] Within settings, the presenter changes the image to “desert stars” and lists style or layout options including icon and text, Manro font, glass focus, soft material, and text controls.
- [00:11:53] The presenter says the resulting design can be brought back to the TV when desired.

## [00:12:04] Reverting and removing access
- [00:12:04] To restore the original setup and prevent Claude Code from accessing the TV, the presenter instructs viewers to tell Claude Code, “revert back to original home screen for my TV.”
- [00:12:19] The final stated step is to turn USB debugging off.

## [00:12:24] Final recap
- [00:12:24] The video’s demonstrated sequence is: connect a computer and Android/Google TV over shared Wi-Fi; enable and authorize USB debugging; use Claude Code to create or replace a home-screen app; prototype and remix layouts in Magic Path; optionally draw on Mobbin and Rive CLI for visual and interaction ideas; and revert by restoring the original home screen and disabling USB debugging. The tool behaviors and outcomes are presenter-reported demonstrations, not independently verified.

## Practical applications
- Suggestion: Use the video’s workflow as a study checklist for understanding Android TV launcher replacement: shared Wi-Fi, OS-identification screenshot, USB-debugging authorization, custom home-screen app, and final restoration steps.
- Suggestion: Prototype several home-screen information architectures before deploying one, comparing direct-launch behavior with variants that include image switchers, information pages, category navigation, and ordered content rows.
- Suggestion: Treat UI references as component-level inspiration: identify a preferred feature from each reference, then request explicitly named remixes rather than copying an entire layout.
- Suggestion: If trying the reported setup, plan a rollback path in advance by retaining the original home-screen configuration and disabling USB debugging after use.

## Evidence anchors
- [00:00:00.080] Hey guys. So recently on X, I've been
- [00:00:08.480] remove ads from their smart TV, but also
- [00:00:19.119] bloatware and ads were removed. And on
- [00:00:24.960] by Apple TV. And he says 70% less RAM
- [00:00:52.480] stems through this initial idea of

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
