# Vercel's CEO Just Unveiled The Greatest AI Coding Workflow Ever

## Source
- Original: https://www.youtube.com/watch?v=y2ifUC9_zuU
- Type: youtube
- Creator: {'displayName': 'AI LABS'}
- Published: 2026-10-19T00:00:00.000Z

## Tags
AI agents, AI-assisted software development, product management, MVP validation, requirements drift, security debt, quality gates, adversarial testing, user experience testing, customer feedback, MCP

## Derived summary
## Overview [00:00:00]
- [00:00:00] AI Labs presents seven tips attributed to the CEO of Vercel for working with AI agents. The video’s claims and tool descriptions are source-reported and not independently verified.
- [00:00:06] The central premise is that measures such as token use or volume of shipped changes indicate how much work is being done, but not whether the work is moving toward the intended product outcome.
- [00:00:21] The presenter says the video turns this idea into a reusable `direction` command and explains how viewers could set up each of the seven practices.

## Tip 1: Validate ideas with a disposable MVP [00:00:51]
- [00:00:51] The first tip is to test an idea before committing to it.
- [00:00:55] The CEO is described as creating a new project for each idea and using an agent to check from scratch whether it actually works.
- [00:01:03] This approach rejects relying solely on what others say about a tool or model.
- [00:01:08] The video criticizes judging models “off vibes”: it gives an example of someone adopting an Astra prompting style from a guide without checking whether the claimed improvement was true.
- [00:01:21] The stated benefit of testing personally is learning what works and what does not in the relevant setting.
- [00:01:27] AI Labs says its own projects begin with a `specs` folder containing a PRD file.
- [00:01:30] The PRD is said to list the application’s planned main features and to be the first document created for each project.
- [00:01:38] The video warns that building a complete application directly from a PRD may reveal fundamental idea problems only late in the process.
- [00:01:44] Early incorrect decisions can propagate because later work is built on them; fixing an invalid premise may require revisiting the entire application.
- [00:01:54] The proposed workflow is to ask Claude Code, or another agent, to build an MVP containing the prompt’s basic features.
- [00:02:02] The video defines an MVP as a first working version that implements features quickly so the builder can see what the idea is like when built.
- [00:02:11] The MVP is used to decide whether the application is worth pursuing.
- [00:02:14] If it is not worthwhile, the idea can be dropped after relatively little effort.

## Tip 2: Check product direction, not just output [00:02:18]
- [00:02:18] The second tip is to ensure that implementation continues moving the application in the intended direction.
- [00:02:22] Tokens spent and changes shipped are presented as acceptable activity metrics, but insufficient direction metrics.
- [00:02:30] These numbers indicate volume of work rather than where that work is taking the product.
- [00:02:33] Consequently, a team can continue shipping while making no meaningful progress toward its plan.
- [00:02:37] The video argues this is especially important with agents because implementation is comparatively cheap.
- [00:02:39] It gives the example that Claude can produce a working new feature in a few minutes.
- [00:02:42] Easy implementation can turn every new idea into a feature, making each addition feel like progress.
- [00:02:48] The presenter says an agent will build whatever it is asked to build and does not inherently know which features matter to the product.
- [00:02:56] Requirement documents and the PRD in the `specs` folder are presented as the existing source of intended direction.
- [00:03:00] During implementation, an application can gradually drift into features that do not matter to the original plan.
- [00:03:08] The proposed control is a custom agent command named `direction` that checks whether built work is drifting or still matches the plan.
- [00:03:16] The command must be told where the plan folder is stored.
- [00:03:20] The video says the setup places the generated command in the `commands` folder inside the Claude folder.
- [00:03:26] In Claude Code, running the reload-plugin command is said to load that command into the current session.
- [00:03:33] When run, `direction` reviews requirement documents, using a separate agent for each document.
- [00:03:39] The main agent then independently checks for changes that do not appear in any plan.
- [00:03:44] The reported output is a full off-course assessment, a scorecard, and a list of needed actions.
- [00:03:52] The team can accept intentional drift and update requirement documents, or remove changes that have strayed too far from the plan.

### Sponsor aside [00:04:03]
- [00:04:03] The video includes a sponsor message for Victor, described by the presenter as an AI employee operating through Slack and Microsoft Teams with a cloud computer.
- [00:04:26] The presenter reports asking it to build a small web application for collecting video ideas with a database, approving deployment, and receiving a working link 10 minutes later.
- [00:04:40] The sponsor claims connections to more than 3,200 tools, memory of setup across tasks, and $100 in free credits; these promotional claims are not independently verified.

## Tip 3: Manage security debt and slop debt [00:04:57]
- [00:04:57] The third tip concerns security, which the CEO reportedly discussed extensively.
- [00:05:01] A major challenge is characterized as understanding “security debt.”
- [00:05:07] Security debt is defined here as security problems that accumulate while working with agents.
- [00:05:11] The video says the problem grows because agents can write more code than was previously feasible for people to inspect manually.
- [00:05:17] No individual can review all of this generated code alone for issues, according to the presentation.
- [00:05:21] The threat model includes attackers having access to agents as well.
- [00:05:26] The presenter claims models have become sufficiently capable and inexpensive at finding security holes that malicious actors can use them against an application.
- [00:05:31] The recommended response is to begin protecting code proactively.
- [00:05:36] Rule one is to run security scans after completing a feature.
- [00:05:42] The video says Vercel has a tool called DeepSseec that finds security gaps in agent-generated code.
- [00:05:53] It notes that teams can create their own security checks, while presenting DeepSseec as an easy-to-set-up option.
- [00:05:59] The stated setup begins with a `deepseec setup` command, which creates a `deepseec` folder in the project.
- [00:06:04] The setup provides a prompt to paste into Claude Code so Claude writes a short file about the application and its sign-in process.
- [00:06:12] Claude can then be asked to run the scans, after which it produces a full report of findings.
- [00:06:19] Rule two is to decide how much care is required for each component of the application.
- [00:06:23] The video calls “slop debt” the messy code deliberately accepted in exchange for faster building.
- [00:06:32] It says slop debt may be less consequential in a small app, but critical product areas demand greater care.
- [00:06:37] The reason given is that customers need confidence that their data is safe and the application is well built.
- [00:06:43] The suggested preventative measure is to set up quality checks before implementation.
- [00:06:51] The presenter recommends quality gates as the preferred form of these checks.
- [00:06:51] Tests are described as determining whether something works, whereas a quality gate also judges whether it is good enough.
- [00:06:58] A review agent that holds every change to defined standards is offered as an example of a quality gate.
- [00:07:02] No change should go live until it has passed all applicable gates, according to the video.

## Tip 4: Define non-negotiable tradeoffs [00:07:16]
- [00:07:16] The fourth tip is to identify what cannot be traded off.
- [00:07:18] Building any application involves tradeoffs: adding features consumes more time, while shipping faster may reduce polish or increase cost.
- [00:07:30] Some dimensions should not be traded away because they are essential to the product being built.
- [00:07:35] The CEO is quoted as saying agent-built work contains tradeoffs such as speed versus safety.
- [00:07:39] Since an agent cannot expend unlimited effort on every task, it must make choices.
- [00:07:43] The presenter therefore says the human and agent should agree on rules and tradeoffs before development begins.
- [00:07:49] The stated priorities for human attention are whether the application does what it is supposed to do and how fast it needs to be.
- [00:07:53] Without clear desired outcomes, the model may take the project in its own direction, according to the video.
- [00:07:59] The practical proposal is a separate “must not trade-off” section in the project’s main `claw.md` file.
- [00:08:03] This section should list essential application properties and things the builder will not give up.
- [00:08:08] The file functions as written instructions for the agent.
- [00:08:12] The presenter cautions that agents handle substantial context and can forget such rules.
- [00:08:16] Each rule should therefore include a way to test whether it is being met.
- [00:08:22] The earlier `direction` command is presented as one way to check continued alignment with the plan.
- [00:08:26] The video also suggests creating test files and committing them to Git so the agent cannot skip these rules.

## Tip 5: Use a breaker agent to attack the product safely [00:08:33]
- [00:08:33] The fifth tip is to use an agent that intentionally tries to break the application.
- [00:08:35] At a Vercel product launch, the CEO reportedly did more than verify normal functionality: he had an agent emulate pressure from many simultaneous users.
- [00:08:46] This includes performing potentially conflicting actions at once, measuring slowdown, and comparing results with other products.
- [00:08:54] The video argues that model-generated code can readily work when everything goes correctly but may fail in unanticipated conditions.
- [00:09:00] Examples of failure conditions include a person skipping a step or performing two actions at the same time.
- [00:09:06] An agent testing its own work may use the application in precisely the intended way, causing all tests to pass.
- [00:09:14] Real customers do not necessarily use the application as intended, and larger user populations expose problems the original agent did not consider.
- [00:09:22] The recommended practice is to test the application in many ways, particularly situations likely to arise after launch.
- [00:09:30] The presenter proposes creating a “breaker agent.”
- [00:09:33] A builder can ask their existing agent to create this agent and define its primary role as deliberately breaking the app and reporting every successful break.
- [00:09:42] The breaker agent is characterized as attacking the owner’s app as an outsider might, to identify weaknesses before others do.
- [00:09:48] If the internal agent finds a way to break the app, the team can repair it; if someone else finds it first, the failure may be costly.
- [00:09:55] The video raises the risk that testing could damage real data.
- [00:09:57] Its stated safeguard is to create copies of application data, leaving production data safe during breaker-agent tests.
- [00:10:06] Claude can be asked to run the breaker agent in a separate context window to stress-test the application.
- [00:10:12] When it completes, the breaker agent reports its findings.
- [00:10:14] The proposed remediation loop is to ask the agent to fix reported issues and rerun tests to confirm they do not recur.
- [00:10:20] The video also suggests a review loop in which the breaker agent continually finds problems and the other agent fixes them.

## Tip 6: Simulate the first-time customer and track complete flows [00:10:26]
- [00:10:26] The sixth tip is to experience the application as a new customer would.
- [00:10:30] The presenter attributes to Vercel a value of knowing the customer.
- [00:10:36] Building for oneself is described as easy because the only test is whether the builder personally likes the app.
- [00:10:42] Selling to other people introduces a different standard because those users lack the builder’s product familiarity.
- [00:10:46] A favored metric is said to be “error-free sessions.”
- [00:10:48] The video defines error-free sessions as the number of people who complete their route through the application without anything going wrong.
- [00:10:54] For new Vercel work, the CEO reportedly has an agent try it and report what could have been done better.
- [00:11:04] A builder cannot be a genuine first-time user of their own application because they already know the location and purpose of each button and page.
- [00:11:11] A new customer lacks this knowledge; a confusing signup request may be invisible to the builder but cause the customer to get stuck and leave.
- [00:11:21] The proposed test is an agent created in Claude Code that uses the application as a first-time user, without prior knowledge of the app’s purpose.
- [00:11:32] This agent should only run the application in a browser and find points at which a new user could struggle.
- [00:11:38] The intended result is a more usable application that guides people to the desired destination.
- [00:11:42] If the agent can read the code, it already knows how the application works and no longer represents a first-time user.
- [00:11:49] The video says this agent is therefore blocked from reading the application and is permitted only to run it.
- [00:11:53] A hook is said to prevent the agent from using its Bash tool for anything other than running the app.
- [00:11:59] If the agent attempts to edit the app or delete code, the hook blocks it.
- [00:12:03] This constraint is presented as a way to obtain more honest feedback on user friction.
- [00:12:08] Finding confusion is only half the task; tracking error-free sessions requires another agent that runs browser tests over every step customers must complete and reports the outcomes.
- [00:12:22] These tests can uncover slow steps, nonworking steps, and flows that fail midway.
- [00:12:28] When a flow does not work properly, the agent can identify it and write code intended to fix it.
- [00:12:30] The agent tests each customer path from start to finish and saves results in a JSON file.
- [00:12:36] The video says this helps assess application performance and should be run before every release.

## Tip 7: Reduce time from customer report to resolution [00:12:42]
- [00:12:42] The seventh and final tip is to act quickly on customer feedback.
- [00:12:46] The CEO is quoted as saying a useful indicator of agent use is what occurs after a customer reports a problem.
- [00:12:52] The process should include properly replying to the customer and investigating what went wrong.
- [00:12:55] Where the issue is clear, it should actually be fixed.
- [00:12:59] The key measurement is the elapsed time from the incoming report through that process.
- [00:13:05] Feedback differs in kind: a screenshot showing a nonworking button may be a straightforward defect requiring a rapid fix.
- [00:13:17] A customer reporting confusion cannot simply be converted into a prompt; the presenter says someone must talk with the customer and understand the issue before changing the product.
- [00:13:26] To handle both types, the video suggests connecting Claude to feedback sources through MCP servers.
- [00:13:32] Gmail MCP is given as an example for reading support emails.
- [00:13:36] Sentry MCP is given as an example for reporting every error the application encounters, including errors no customer has reported.
- [00:13:42] Once connected, Claude is said to read and sort each newly arriving report.
- [00:13:47] For a definite defect, such as a payment failure, the described workflow has Claude fix it immediately.
- [00:13:50] For matters requiring human judgment, Claude should route the report to the human for a decision.

## Closing and recap [00:13:56]
- [00:13:56] The presenter says the agents and skills shown are available through the AIABS Pro community, which is a promotional offer.
- [00:14:09] The video closes without adding further educational claims.
- [00:14:20] Recap: the seven presented practices are MVP validation, direction checking, security and quality controls, explicit non-negotiables, adversarial break testing, first-time-user and end-to-end flow testing, and fast feedback triage and resolution.

## Practical applications
- Suggestion: Before full implementation, build a minimal working version containing only the proposed core features and use its results to decide whether to continue or stop.
- Suggestion: Maintain a documented product plan and periodically compare implemented changes against it, explicitly deciding whether to update the plan or remove unintended drift.
- Suggestion: Define release gates for critical areas, including security scans, standards review, and tests for non-negotiable requirements.
- Suggestion: Isolate adversarial testing from production data by using copied or test data, then retest after fixes.
- Suggestion: Run browser-based first-time-user and complete customer-flow tests before releases, with the first-time-user tester restricted from reading or modifying source code.
- Suggestion: Separate clearly reproducible defects from feedback requiring human interpretation, and track elapsed time from report intake to response, investigation, and resolution.

## Evidence anchors
- [00:00:06.400] that most people judge how well they're
- [00:00:12.320] think. That's because the number only
- [00:00:14.080] tells you how much you're building, not
- [00:00:16.000] where it's taking you. So, what he cares
- [00:00:46.800] we're going over each of his seven tips

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
