# I Built My Own TV Operating System With Claude Code

## Source
- Original: https://www.youtube.com/watch?v=i0ytu6k8uac
- Type: youtube
- Creator: {'displayName': 'Lukas Margerie'}
- Published: 2026-10-21T00:00:00.000Z

## Tags
smart TV, Google TV, Android TV, Claude Code, custom launcher, USB debugging, Magic Path, Mobbin, Rive CLI, UI design, reverse engineering

## Learning guide
**The arc**
The video starts from posts showing smart-TV owners using AI to strip ads and build their own TV interfaces, and asks how hard that really is. The central idea is that reverse engineering with Claude Code lets you connect to an Android/Google TV and replace its home screen with your own app in a few prompts. It moves from connecting the TV, to building a basic replacement home screen, to prototyping and polishing designs in Magic Path with Mobbin and Rive CLI, and ends with how to revert everything safely.

**1. Understand what is possible**
- **Treat it as reverse engineering:** These projects come from giving an AI enough context to inspect and rebuild software, such as a GitHub repository you hand to Claude Code or Codex so it can examine an app down to its binary and explain how a feature works. The same approach produced open source, clonable clones like Photocraft (Photoshop), Vectorcraft (Illustrator) and Filmcraft (Premiere Pro).
- **Aim for small first wins:** Others removed bloatware and ads, built a minimal UI, or made a screensaver showing revenue, calendar, weather and Stripe payment notifications. The demonstrated after-state took only two or three prompts, so start simple.

**2. Connect Claude Code to your TV**
- **Use a setup prompt:** Copy a ready-made setup prompt (the creator used one from a Codilla tweet) and paste it into Claude Code. This gives the agent a full plan instead of building one from scratch.
- **Share one Wi-Fi network:** Put your computer and TV on the same Wi-Fi first. This is how Claude Code finds the TV on the local network.
- **Photograph the About screen, not the TV:** On the TV go to Settings, then About, and photograph that screen to paste alongside the prompt. It gives the agent real OS context; in the demo it identified a TCL running Android TV OS 14.
- **Be patient on the first pass:** It took about 3 to 4 minutes before Claude Code returned a list of directions. Follow them with your remote.
- **Enable and authorize USB debugging:** Turn on USB debugging, tick "always allow from this computer", and press Allow. If you cannot find the setting, search "USB debugging" plus your TV or TV OS name and look for YouTube guides.
- **Run a test command:** Have Claude Code play a YouTube video on the TV (the demo used Big Buck Bunny). The first run is slow; the second and third get faster.

**3. Speed up repeat commands (optional)**
- **Add Jev by Type Safe for fixed paths:** For specific commands like opening a particular YouTube channel, preset Claude Code to use Jev so it runs faster. Use the Type Safe skill, log in to Type Safe, copy its prompt, and give that prompt to Claude Code.

**4. Build a replacement home screen**
- **Ask if it is possible first:** Ask Claude Code whether a custom home screen can work. An Android TV app that declares itself a home screen can replace Google TV Home.
- **Get a working baseline:** Ask for a new home-screen app with no art direction. Expect it to be a bit janky but functional: you can change channels, select apps and open them.
- **Experiment boldly:** Try a playful concept to test the limits, like a home UI of a chicken laying eggs where each egg is one of your TV apps. That build took about 5 minutes.

**5. Prototype and remix in Magic Path**
- **Import the original home screen:** Ask Claude Code to add your TV's original home design into an Open Magic Path project. Magic Path is a canvas where you place designs, remix them and create variants; the import came out as a one-to-one copy you can navigate with arrow keys.
- **Connect Claude Code once:** In Magic Path, select Claude Code and follow its three or four connection steps the first time.

**6. Borrow proven layouts with Mobbin**
- **Connect the Mobbin MCP:** Mobbin is a large database of app and website screens, and its MCP lets Claude Code find relevant UI from chat context so you skip manual browsing.
- **Request remixed variants:** Prompt Claude Code to create two variants that remix the Google TV home component with Mobbin findings, drawing on references like HBO Max, Paramount Plus, Netflix and The New York Times. You can also cherry-pick, such as one feature from Paramount Plus and another from Disney Plus.
- **Compare the results:** One demo variant kept the layout but added two buttons, image switchers and a "more info" action instead of jumping straight in. The other added a preview-image banner, category selection and a new order: apps, top picks, continue watching, top-selling movies.

**7. Add motion with Rive CLI**
- **Duplicate your favorite variant first:** Pick the layout you like, duplicate it, then ask Claude Code how Rive CLI could improve the interaction design. This keeps the original safe while you experiment.
- **Apply its suggestions:** Claude Code proposed a focus frame, hero timer, transitions, Play and More Info buttons, app-launch behavior and small details. The demo got a border that moves between focused items and a text hover animation.
- **Copy a style from a link:** Paste a reference URL (the creator used community member Jerry's tweet) and ask for its glow effect, then layer extras like particles at the bottom. The result auto-cycles through channels and apps.
- **Add custom tabs:** The creator added a "cloud" tab that does not work in preview but on the TV opens a browser to log in to Claude and build with Claude on the TV. The real-TV version matched the Magic Path build.

**8. Borrow a style from an article**
- **Feed Claude Code a write-up:** Paste an article URL, such as Nathan Clark's "I gave my Samsung frame a new home screen", ask Claude Code to read it, and implement that style as a new Magic Path variant. Your earlier apps, including the cloud app, carry over.
- **Tune it in settings:** Adjust the image (the demo used "desert stars") and options like icon and text, Manro font, glass focus, soft material and text controls. Push the design to the TV whenever you are ready.

**9. Revert and remove access**
- **Restore the original:** Tell Claude Code "revert back to original home screen for my TV."
- **Turn off USB debugging:** Disable it on the TV so Claude Code can no longer access it.

**Try this first:** Put your computer and TV on the same Wi-Fi, photograph the Settings > About screen, and paste it with a setup prompt into Claude Code to get your connection directions.

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

## Evidence anchors
- [00:00:00.080] Hey guys. So recently on X, I've been
- [00:00:08.480] remove ads from their smart TV, but also
- [00:00:19.119] bloatware and ads were removed. And on
- [00:00:24.960] by Apple TV. And he says 70% less RAM
- [00:00:52.480] stems through this initial idea of

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
