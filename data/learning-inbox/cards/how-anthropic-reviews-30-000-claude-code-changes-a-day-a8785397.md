# How Anthropic Reviews 30,000 Claude Code Changes a Day

## Source
- Original: https://www.youtube.com/watch?v=0M7EXtYko04
- Type: youtube
- Creator: {'displayName': 'Owain Lewis'}
- Published: 2026-10-26T00:00:00.000Z

## Tags
AI code review, Claude Code, software engineering, security review, risk-based approval, automation, incident response

## Derived summary
## 00:00:00 | Scale and the review bottleneck

- [00:00:00] Owen introduces a discussion of how Anthropic reviews code at scale, including for Claude Code. The figures and operational claims in these notes are reported by the speaker and are not independently verified.
- [00:00:04] He says Anthropic increased merged changes from 2,500 per day to more than 30,000 per day in four months, a 12× increase.
- [00:00:47] He reports that AI writes 90% of Claude Code’s own codebase.
- [00:01:02] His concern is that developers who did not write generated code may understand it less intimately, even as the volume needing review grows.
- [00:01:20] He invokes the theory of constraints: a process moves only as fast as its slowest part.
- [00:01:37] Agents may generate code in minutes, but slow review can prevent faster generation from improving overall output.
- [00:01:53] He says traditional reviews can take multiple days because reviewers are busy and must become acquainted with changes they lack background on.
- [00:02:11] He predicts that increased code production will worsen this bottleneck if teams rely on the same review methods.

## 00:02:20 | Review goals, risk, and measurement

- [00:02:20] Owen identifies two jobs of review: finding and fixing bugs before production, and building shared understanding of the codebase.
- [00:02:31] Both humans and agents make mistakes, so he argues that checking the first output raises a team’s quality bar.
- [00:02:48] Shared understanding remains important when agents write code: developers still need a high-level view of what their software does.
- [00:02:59] He highlights the article’s framing: ask what could go wrong and whether an automated check or human review is best placed to catch it, rather than merely asking whether a human read the code.
- [00:03:19] Changes have different risk levels and blast radii. He describes a documentation change as relatively low risk.
- [00:03:31] Database or payment infrastructure errors could cause a major outage or prevent customers accessing services, so their potential impact is much higher.
- [00:03:52] Human attention is limited, so Owen argues for concentrating human review where it is most needed instead of treating every change identically.
- [00:04:17] He proposes measuring time from opening a change to merging it, alongside revert rate or defect rate, to assess speed and quality as the process changes.

## 00:04:46 | Overview of the layered process

- [00:04:46] Owen introduces what he calls six steps, though later he separately numbers fast detection and rollback as a seventh step.
- [00:04:52] Before opening a change, the described local process includes tests, build checks, linting, type checking, and review by an agent with a fresh context window.
- [00:05:08] After opening the change, he describes static checks, AI code review, and security review.
- [00:05:22] His risk-based approval example assigns low-risk changes to possible auto-merge, medium-risk changes to one human reviewer, and high-risk changes to two.
- [00:05:41] He also describes internal feedback, gradual rollout, and the ability to roll back production changes.
- [00:05:53] The reason for rollback is that review is imperfect and does not eliminate production bugs.

## 00:06:03 | Local review and project-specific instructions

- [00:06:03] After an agent writes code, Owen describes asking a subagent or fresh agent to review it locally.
- [00:06:11] The reviewer can use a different agent: for example, Codex can review code produced with Claude Code, or vice versa.
- [00:06:28] He compares agent-generated first drafts to human first drafts: both can contain bugs or opportunities for improvement.
- [00:06:44] Owen attributes to Claude Code creator Boris a claim that local iteration makes the final result two to three times better; no measurement method is supplied in the captions.
- [00:07:07] A `review.md` file can direct reviewers toward concerns specific to the application instead of treating every review as generic.
- [00:07:22] For a payments application, his examples are security and correct authorization.
- [00:07:31] For a web application, examples include the user interface and database performance.
- [00:07:45] The file lives in the codebase and agents are asked to read it during review.
- [00:07:56] Example instructions can specify how to present findings, exclude linting or formatting and particular folders, and pay attention to email addresses or user information in logs.
- [00:08:30] In his own project, Owen says the file includes definitions for low-, medium-, and high-risk classifications plus codebase-specific review guidance.

## 00:08:52 | Pull-request review and security demonstration

- [00:08:52] The next described layer is an automated AI review after a change is pushed to a pull request, such as on GitHub.
- [00:09:05] Owen names CodeRabbit, Greptile, Claude Code, and Codex as options for reviewing a change.
- [00:09:22] He demonstrates a general `/code review` command and a separate security-review command in Claude Code.
- [00:09:38] Additional context can focus the security review on particular files, uncommitted changes, an area, or a topic.
- [00:09:53] In the demonstration, he says he deliberately added an SQL vulnerability to see whether review would catch it.
- [00:10:02] He reports findings including SQL injection, an endpoint without authentication, logical correctness concerns, and quality issues.
- [00:10:17] His proposed iteration is to have an agent fix findings and then run review again, potentially more than once.
- [00:10:30] A general review can also be focused on a topic such as documentation.
- [00:10:44] The security feedback assigns the SQL injection finding 9 out of 10 confidence. Owen says it provides more detail than the general review, which also found the issue.
- [00:11:01] He mentions feedback about listening on loopback at a predictable port, SQL statement recommendations, and a path-traversal vulnerability.
- [00:11:15] His comparison is that the general review catches many errors, while the specialized security review goes deeper; he recommends running both.

## 00:11:26 | Repeatable factory workflow

- [00:11:26] Owen’s factory analogy addresses forgetfulness and fatigue: run each task through the same repeatable sequence rather than relying on ad hoc prompting.
- [00:11:49] He describes his own plugin as using separate agents for implementation, code review, security review, and UX review.
- [00:12:07] The UX role can include browser testing of a web application; other agents handle triage and classification.
- [00:12:17] He says the classifier changes a ticket’s risk level and adds a GitHub issue label according to the change.
- [00:12:25] The roles can be sequenced so a single command receives a task and runs the configured steps.
- [00:12:50] He argues the setup need not be complex: the goal is repeatability and predictability rather than many installed skills.
- [00:13:07] The motivation is to consistently include code review, security review, linting, and needed tooling.
- [00:13:23] His Software Factory example chains Claude Code subagents; a review command combines general and security review and can accept optional context.
- [00:14:07] At a higher level, he describes passing in a task for planning, building, testing, and reviewing as a sequence.
- [00:14:22] In the example, a change classified as medium risk requires one human approval.
- [00:14:37] He passes ticket `NEO-345` to the factory, describing a flow from ticket triage to implementation and review by different subagents.
- [00:15:08] He says encoding the workflow makes the checks systematic instead of requiring him to remember each review and classification step.

## 00:15:41 | Triage, specifications, and acceptance checks

- [00:15:41] Owen describes triage as turning a rough or vague problem description into a detailed specification with an agent.
- [00:16:08] His example adds labels and a specification that a person can review before the agent builds the code.
- [00:16:23] The resulting code then goes through automated checks and code review.
- [00:16:28] He says the review should reference acceptance checks from the original plan, including cases identified for testing.
- [00:16:41] The central questions are whether the code does what it is meant to do and meets the requirements and acceptance criteria.

## 00:17:02 | Security review and deterministic checks

- [00:17:02] Owen labels security review the third step and describes a built-in Claude Code security-review command.
- [00:17:17] Here he suggests running security review periodically rather than on every change and automating it so it is not forgotten. This differs from his earlier examples of running it on every change.
- [00:17:33] Security-review targets include SQL injection, cross-site scripting, authentication and authorization flaws, insecure data handling, missing validation, and vulnerable dependencies.
- [00:17:44] He labels deterministic automated checks the fourth step, including linting and type checking to find obvious errors.
- [00:17:58] Tooling depends on the programming language; he describes asking an agent to configure checks locally and on GitHub.
- [00:18:14] His examples also include verifying that the code builds and running language-specific formatters on changes.

## 00:18:24 | Risk-based approval and accountability

- [00:18:24] The fifth step is human approval scaled to risk, with a classifier assigning low, medium, or high risk.
- [00:18:38] The rationale is blast radius: requiring multiple people to review a trivial documentation change can waste limited attention.
- [00:18:47] Owen’s example allows agents to auto-merge a small, trivial change.
- [00:18:56] A medium-risk change such as a large feature receives one human reviewer in his example.
- [00:19:03] Higher-risk database or infrastructure changes receive two reviewers because their potential blast radius is greater.
- [00:19:14] He says the person responsible for a change remains accountable for its quality even if agents write the code.

## 00:19:25 | Release, rollback, and learning from incidents

- [00:19:25] The sixth step is gradual release: roll changes out to internal teams first to get feedback before public release.
- [00:19:34] Owen then labels fast detection and fast rollback as step seven.
- [00:19:39] Review cannot catch every possible error; he says some issues emerge only after production deployment.
- [00:19:53] Memory leaks and performance issues are his examples of problems that can be difficult to detect merely by reading code.
- [00:20:01] The described response is to assume review is fallible and make problematic releases quickly reversible.
- [00:20:08] He describes periodic on-call and incident reviews, including a weekly look at recent changes and problematic areas to improve the process.
- [00:20:24] He says Anthropic uses mistakes that escaped review as evaluations or feedback for future reviewers.
- [00:20:35] His example is a database change that passed review but caused a production error: the incident can become a test or context for an agent’s future attention.

## 00:20:48 | Human understanding and explainers

- [00:20:48] Owen argues that humans should remain involved because they have context agents may lack, especially for risky changes.
- [00:20:54] He says he is personally comfortable auto-merging some change types while retaining human involvement for others.
- [00:21:14] His position is that humans and agents can catch different things, making their combination valuable.
- [00:21:20] Developers should still understand a change’s purpose, impact, and effect on the overall architecture at a high level.
- [00:21:34] He describes asking an agent for an HTML explainer with a diagram of the change and its potential risk.
- [00:22:01] His demonstration request asks Claude to generate an HTML explanation and include a diagram while a code change is running.
- [00:22:19] He considers this particularly useful for large changes, context switching, or returning to work later.
- [00:22:36] He says the generated explainer can be customized and describes it as providing diagrams, a process explanation, and a way to recreate the change.

## 00:23:07 | Final recap

- [00:23:07] Before opening a change, Owen recaps running formatting and linting, potentially using a Claude Code hook or a Git pre-hook.
- [00:23:22] He recaps local general and security review, or use of a fresh subagent, which he says he personally prefers.
- [00:23:35] The `review.md` file captures project-specific priorities and recurring problems for future reviews.
- [00:23:48] After pushing, the recap calls for an AI reviewer, a tuned review file, automated security review, and review effort matched to risk.
- [00:24:06] His main tradeoff is to reserve human judgment for more important, higher-risk changes instead of spending the same attention on routine changes.
- [00:24:22] After merging, teams should learn from failures and refine the review process.
- [00:24:33] His final thesis is that quality at scale comes from iterative verification across automated checks, AI review, human review where needed, monitoring, and measurement.

## Practical applications
- Suggestion: Define project-specific review priorities and recurring failure patterns in a review.md file, and have a fresh reviewer consult it. [p0247, p0248, p0249, p0725, p0726, p0727, p0728, p0729, p0730]
- Suggestion: Establish risk categories and allocate human approval effort according to the potential impact of each change. [p0177, p0178, p0179, p0180, p0181, p0182]
- Suggestion: Track opening-to-merge time alongside revert or defect rates when evaluating review-process changes. [p0144, p0145, p0146, p0147, p0148, p0149]
- Suggestion: Include acceptance criteria in reviews and use incidents that escaped review as feedback or evaluation cases for later reviewers. [p0506, p0507, p0508, p0509, p0510, p0632, p0633, p0634, p0635]

## Evidence anchors
- [00:00:04.880] months, the anthropic team went from
- [00:00:06.160] merging 2,500 changes per day to over
- [00:00:08.559] 30,000 which is a 12x increase. And
- [00:00:47.360] really interesting is 90% of Claude
- [00:00:48.960] Code's own code base is written by AI. I

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
