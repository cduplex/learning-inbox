# Can a Mac Mini run local AI? (shocking)

## Source
- Original: https://www.youtube.com/watch?v=dFTXOt0GBx4
- Type: youtube
- Creator: {'displayName': 'Alex Finn'}
- Published: 2026-10-10T00:00:00.000Z

## Tags
local AI, Mac Mini, Apple silicon, Hermes Desktop, Hermes Agent, local language models, privacy, offline AI, coding agents, LoRA

## Learning guide
**The arc**
Alex Finn starts from his prediction that the Mac Mini would become the king of local AI and asks whether a 32 GB Mac Mini can really run a useful model without technical skills. The central idea is that Apple's integrated memory lets an $800 to $900 machine load surprisingly large models for free. He installs Hermes Desktop, downloads a local model, checks chat speed, then escalates to coding tests, and concludes the setup is fast enough to be worth it for cost, privacy, control and learning.

**1. Install the agent**
- **Use Hermes Desktop as your setup path:** Hermes Agent is a free, open-source agent that runs on your computer as a personal assistant and supports both cloud and local models. It removes the technical work of finding and loading a model. Download Hermes, move the app into the macOS Applications folder, then open it.
- **Let it prepare itself:** On first launch it downloads and prepares the needed components automatically. Expect this to take about 45 seconds before Hermes Agent opens.

**2. Pick and download a local model**
- **Go to the local-model setting:** Navigate to **Settings → Providers → Run models locally**. This is where Hermes handles local models for you.
- **Accept the automatic pick:** Hermes selects what it considers the best model for your machine; on the 32 GB Mac Mini it chose the model transcribed as "Quen 3635B". 32 GB is adequate but not large, and it can run this model.
- **Click Set up for me:** This starts the download and setup. Free up about 21 GB of disk space and allow roughly 4 minutes.
- **Know what you get:** Once installed, the model runs without internet access, a cloud subscription or ongoing payment.

**3. Understand the Apple tradeoff**
- **Count on integrated memory:** Apple's memory is shared between general computing and graphics, so all 32 GB can go toward loading models. That lets bigger models fit than would otherwise, even on a lower-cost computer.
- **Run AI beside your daily work:** A Mac you already work on can run local AI alongside that work, such as generating images on-device during creative work.
- **Accept slower speed than Nvidia:** An RTX 5090 setup runs local models extremely quickly, and Apple chips are somewhat slower. The Mac Mini's advantage is price, around $800 to $900.

**4. Load the model and check responsiveness**
- **Select the local model in the chat:** Pick the local "Quen 3635B" entry from the model selector. Hermes can then answer questions, chat, build things and control the computer using only the local model.
- **Expect a slow first prompt:** The first prompt takes longer because the model must load into memory. Later prompts are faster.
- **Let it build memory:** The model offered to create a user profile to become more useful, showed its thinking, and saved information to memory. Answer its follow-up questions so it learns your context.
- **Measure speed honestly:** Check the timestamps on prompt and answer; in the demo both read 12:34, under a minute, and felt comparable to cloud AI.

**5. Test real capability with coding tasks**
- **Start with a simple single-file app:** Prompt "build a Snake game in a single HTML file", then open it in a browser. The demo produced 78 lines of working code where the snake collects cookies, grows and shows a score.
- **Fix flaws with a follow-up prompt:** The Snake title stayed on screen during play. Send another prompt to correct small defects like this.
- **Escalate to something harder:** Ask for a single-file HTML 3D first-person shooter. The result had a 3D engine, enemies, shooting, reloading, muzzle flash, experience points and a map in the upper right, playable though not pretty.
- **Read the visible reasoning:** Local models let you inspect their thinking, which cloud models often hide. Use it to see how the model plans the task.
- **Set expectations:** A modest local model will not match a frontier cloud model, but it is advanced AI running entirely on your desk.

**6. Decide why local is worth it for you**
- **Run the cost math:** Compare upfront hardware against subscriptions. At $200 per month for ChatGPT, an $800 to $900 Mac Mini pays for itself in about four months if this level of intelligence meets your needs.
- **Keep sensitive work private:** Cloud prompts travel to data centers, while a local model stays on the device and works offline. Use it for private details and data you do not want in the cloud.
- **Customize the model:** You can customize a local model or train a LoRA to give it your personal voice.
- **Value fun and learning, not only ROI:** Owning a private local intelligence is enjoyable and is hands-on education about AI. Running it yourself is a direct way to learn.

**Try this first:** Install Hermes Desktop, go to Settings → Providers → Run models locally, click Set up for me, then ask the model to build a Snake game in a single HTML file and open it in your browser.

**Caveat:** The hardware naming, speed impressions and comparisons to cloud models are the creator's own claims, so test the model on your own tasks before canceling any subscription or buying hardware.

## Derived summary
## [00:00:00] Premise and test scope
- [00:00:00] The presenter says he previously predicted that the Mac Mini would become the "king" of local AI and that Apple would win the local-AI race; he says this drew social-media criticism.
- [00:00:16] He introduces a new Mac Mini described as an M6 and frames the video as a stress test of its local-AI limits.
- [00:00:26] His stated goals are to demonstrate an easy local-model setup without technical skills, test workloads, and explore whether local use could replace cloud subscriptions or ChatGPT for some users.
- [00:01:01] The tested machine is described as an M6 Mac Mini with 32 GB of RAM. Hardware naming, performance claims, and comparisons in this video are presenter claims and are not independently verified here.

## [00:01:09] Installing Hermes Desktop
- [00:01:09] The presenter chooses Hermes Desktop as the setup path for loading local models.
- [00:01:19] He describes Hermes Agent as an open-source agent that runs on the user's computer, functions as a personal assistant or AI employee, and supports both cloud and local models.
- [00:01:33] He says the software and demonstrated workflow are free and require no technical skills.
- [00:01:40] The installation workflow shown is: download Hermes, move the application into the macOS Applications folder, then open it.
- [00:01:50] He says installation downloads and prepares needed components automatically.
- [00:02:04] He claims Hermes can make it easy to load a chosen model, find an appropriate local model, and load it for the user.
- [00:02:26] He provides a brief aside that he plans to link Hermes Desktop and again calls it free.
- [00:02:30] He reports that the installation took about 45 seconds before launching Hermes Agent.

## [00:02:34] Selecting and downloading a local model
- [00:02:34] The presenter says Hermes provides a function for loading a local model.
- [00:02:49] The navigation path he demonstrates is **Settings → Providers → Run models locally**.
- [00:02:56] He says Hermes automatically selects what it considers the best local model for the computer; on his machine it selected a model transcribed as “Quen 3635B.”
- [00:03:10] He characterizes 32 GB of memory as adequate but not especially large, and says that capacity can run the selected model.
- [00:03:18] He claims people compare the selected model to “Opus 45,” while presenting that as an informal comparison rather than a verified benchmark.
- [00:03:36] The demonstrated action is clicking **Set up for me** to begin the model download.
- [00:03:39] He says the model download is about 21 GB, so roughly 21 GB of disk space is needed.
- [00:03:44] He predicts the download and setup will take about 4 minutes and says the resulting model can operate locally without internet access, a cloud subscription, or ongoing payment.

## [00:04:20] Claimed Apple local-AI advantages and tradeoffs
- [00:04:20] The presenter argues that Apple hardware is attractive for local AI because its integrated memory can be used for both general computing and graphics processing.
- [00:04:39] For the 32 GB Mac Mini in the demo, he says all 32 GB can be used to load local models.
- [00:04:49] His causal argument is that access to all system memory enables bigger models than would otherwise fit, including on a lower-cost computer.
- [00:05:19] He also cites macOS user experience: a machine already used as a daily work computer can run local AI alongside that work.
- [00:05:32] He gives on-device image generation during creative work as an example of combining work and AI use on one device.
- [00:05:41] He acknowledges Nvidia systems have separate strengths and says his RTX 5090 can run local models extremely quickly.
- [00:05:49] The tradeoff he identifies is that Apple chips are somewhat less performant on speed than his Nvidia setup.
- [00:05:55] He predicts a future M5 Ultra, 512 GB Mac Studio demonstration and says Apple may improve on speed, but this is a prediction rather than tested evidence in the source.
- [00:06:24] He cites approximate Mac Mini pricing of $800 to $900 as an additional advantage.

## [00:06:30] Loading, first-prompt behavior, and basic responsiveness
- [00:06:30] Returning to Hermes, he chooses the local “Quen 3635B” entry from the model selector and says it is loaded.
- [00:06:45] He describes Hermes as an agent that can answer questions, talk with the user, build things, and control the computer; in this demo it is powered by the local model.
- [00:06:58] He concludes that a local model can be loaded onto the Mac Mini, while noting usefulness depends on speed and quality.
- [00:07:17] He explains that the first prompt to a local model can take longer because the model must be loaded into memory.
- [00:07:28] He says prompts after the initial memory load should be faster.
- [00:07:53] The local model responds by proposing an initial user profile to become more useful.
- [00:08:07] The presenter asks it to greet his audience, and says he can see its thinking and save information to memory.
- [00:08:30] The model produces a short proposed audience message and asks where the presenter posts content.
- [00:08:45] The presenter says the exchange was unedited and real time, and judges it to be very quick, comparable in feel to cloud AI, with memory creation.
- [00:09:13] He says he is moving from a speed check to capability testing.
- [00:09:21] He points to displayed timestamps with prompt and answer both at 12:34, then characterizes the response as taking less than a minute.

## [00:09:31] Coding test: single-file Snake game
- [00:09:31] The first coding task is: build a Snake game in a single HTML file.
- [00:09:50] The model’s visible reasoning states an intent to build a complete, polished version.
- [00:09:57] The presenter argues that local models allow the user to inspect their thinking, whereas cloud-model thinking is often hidden.
- [00:10:18] He says local execution means computation occurs on the user's computer rather than being sent to the internet or cloud.
- [00:10:29] He connects local execution with control over operation and with keeping private details and data out of the cloud.
- [00:10:53] He says the game is nearly finished and reports that it wrote 78 lines of code.
- [00:11:03] He opens the result in a browser to test it.
- [00:11:08] During gameplay, he reports that the Snake game works: the snake collects cookies and grows.
- [00:11:13] He notes a defect or unfinished detail: the Snake title remains on screen, though he says it could be corrected with another prompt.
- [00:11:28] After the game ends, he observes a displayed score and says the game was built entirely locally.

## [00:11:33] Coding test: single-file 3D first-person shooter
- [00:11:33] He escalates the test by requesting a single-file HTML 3D first-person shooter, again emphasizing local execution on a sub-$1,000 Mac Mini.
- [00:11:51] He says the resulting game includes a 3D engine, enemies, shooting, reloading, and muzzle flash.
- [00:11:59] He opens the game in a browser and starts it.
- [00:12:04] He says the game resembles Wolfenstein and reports that it is playable, with enemy shooting, experience points, and a map in the upper-right area.
- [00:12:14] He explicitly says it is not the prettiest or best first-person shooter, framing the purpose as demonstrating a modest local model rather than matching a frontier cloud model.
- [00:12:30] He characterizes the key result as advanced AI running entirely on the desk-sized local computer.
- [00:12:42] He claims the demo would have seemed impressive from a cloud model two years earlier, but says it is not as good as “Opus 55” today.
- [00:12:53] He treats privacy, security, and ownership of the computer as the central value of the local result.

## [00:13:00] Presenter conclusions: cost, privacy, control, and learning
- [00:13:00] The presenter concludes that the Mac Mini can run local AI, including the selected “Quen 36” model, at what he considers a good speed.
- [00:13:30] He contrasts the local setup with using ChatGPT or Opus through the cloud and asks why someone would buy hardware for local use.
- [00:13:35] His first answer is cost: there is an upfront computer cost, which he again estimates at $800 to $900, but no model subscription charge in the demonstrated setup.
- [00:13:43] He gives a hypothetical calculation: at $200 per month for ChatGPT, the computer would pay for itself in about four months if this level of intelligence met the user's needs.
- [00:13:53] His privacy argument is that cloud prompts travel to data centers and servers rather than staying on the user's computer.
- [00:14:07] He says a local model on a Mac Mini or Nvidia computer stays on the device and can work even while disconnected from the internet.
- [00:14:22] He identifies customization as another advantage: a user can customize the model or train a “LoRA” to give it a personal voice.
- [00:14:40] He argues that ROI need not be the only reason to adopt local AI.
- [00:15:04] He presents enjoyment as a valid motivation and describes owning a private local intelligence as fun.
- [00:15:42] He also presents local setup as hands-on education about AI.
- [00:15:57] He predicts AI will remain important, grow “10,000 times bigger,” and affect the world economy; these are predictions and opinions.
- [00:16:07] He recommends becoming hands-on with AI and says running it locally is a way to learn.

## [00:16:13] Closing aside and recap
- [00:16:13] **Promotional aside:** The presenter asks for engagement and promotes a newsletter called “Ship It Weekly.”
- [00:16:24] He invites audience requests for future coverage, including more local AI, coding-related material, and building projects.
- [00:16:32] **Recap:** The demonstration’s workflow was: install Hermes Desktop, use its local-model provider setting, download an approximately 21 GB selected model, load it, test chat responsiveness, then test generated single-file HTML games.
- [00:16:32] **Recap:** The presenter’s stated tradeoff is lower speed than a powerful Nvidia system, balanced against integrated-memory capacity, approximate $800 to $900 entry pricing, local operation, privacy, offline use, customization, and educational value.

## Evidence anchors
- [00:00:00.160] Back in January, I told the world that
- [00:00:16.160] the brand new Mac Mini M6, and we're
- [00:00:26.640] how to load up local AI models on a Mac
- [00:01:03.680] see the stats. It is an M6 uh with 32 GB
- [00:01:18.400] desktop. So, for those who don't know,

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
