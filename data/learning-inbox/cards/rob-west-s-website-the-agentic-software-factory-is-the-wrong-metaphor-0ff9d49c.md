# Rob West's Website - The Agentic Software Factory is the Wrong Metaphor

## Source
- Original: https://robwest.info/articles/the-agentic-software-factory-is-the-wrong-metaphor/
- Type: webpage

## Tags
AI-assisted software development, coding agents, design engineering, engineering leadership, software delivery, organizational learning, productivity metrics

## Learning guide
**The arc**
Why organize coding agents as a software factory if software development is primarily design work? The central idea is that agents create and revise designs, while software already has a production system in its build and deployment pipelines. The argument moves from the limits of factory-style management to a practical alternative: automate repetitive work and use agents to turn uncertain assumptions into tested designs.

**1. Put the factory boundary in the right place**
- **Treat code as design:** Organize programming, testing, and debugging as work that develops and validates a design, not as manufacturing output. Source code is the design; compilers and linkers perform the build, so generating more code does not by itself establish that the design is better.
- **Separate design from production:** Locate the production system in the path from source code through compiler, package, and deployment. Standardize that path, but manage agents that create and revise source code as design collaborators working through hypothesis, implementation, test, and revision.
- **Choose management goals deliberately:** Avoid making utilization, output counts, and reduced variation the governing goals for discovery work. Those factory goals reward repeatability, whereas understanding problems and designing solutions requires learning and exploring alternatives.

**2. Keep uncertainty visible instead of hiding it in tickets**
- **Treat tickets as incomplete designs:** Work out desired behavior, system structure, and tradeoffs rather than assuming a ticket settles them. A ticket is not an engineering drawing; treating it as one hides the design decisions that still need to be made.
- **Use requirements as hypotheses:** Revise specifications as implementation reveals ambiguity, mistaken assumptions, and gaps. Building software produces information about what was actually wanted, so keep that learning connected to requirements rather than treating specifications as fixed raw material.
- **Preserve useful variation:** Compare, test, and select among alternative approaches instead of forcing every agent toward identical output. If ten agents produce ten different approaches, their differences can provide design value rather than represent process defects.
- **Resist premature certainty:** Do not make tickets appear fully specified just to keep agents busy. Expose unresolved assumptions before implementation, because an agent can fill an ambiguous input with a plausible guess and produce a confident, well-tested implementation of the wrong thing.

**3. Measure whether acceleration creates value**
- **Improve the surrounding system:** Address organizational friction and value-stream management alongside agent adoption. Individual speed gains need a system that turns them into organizational gains; faster output alone does not create innovation or reclaim capacity for new features.
- **Measure outcomes, not generated volume:** Ask whether the product performs better, customers receive more value, risk decreases, and the organization learns faster. If agents generate ten times as many changes, pull requests, story points, feature counts, and automated-change counts become less informative about productivity; this is a hypothetical illustration, not a benchmark.
- **Connect changes to feedback and architecture:** Evaluate code through design quality, feedback about whether changes were right, and architecture that limits the blast radius when they were not. Code is an intermediate artifact, so increasing its production without these checks can accelerate the wrong work.
- **Keep automation metrics in their place:** Use the percentage of changes shipped automatically and their cost to understand automation, not as substitutes for customer outcomes. These measures describe production efficiency without establishing whether the changes were worth making.

**4. Automate the work that really is repetitive**
- **Build factories for settled work:** Standardize build pipelines, environment provisioning, test-suite execution, dependency upgrades, routine migrations, formatting, static analysis, and appropriate remediation. These are useful automation targets when the design question is largely settled and the remaining work is repetitive.
- **Distinguish discovery within the workflow:** Separate requirements refinement, architecture, technical spikes, and exploratory testing from builds, configuration management, regression testing, and coding to established patterns. Software development interleaves discovery and production, so apply the appropriate management approach to each rather than labeling the whole process a factory.
- **Protect the design loop:** Treat intent definition, trace review, and release approval as substantive design work, not merely throughput constraints. They help determine what should happen and whether it did, so preserve that judgment while automating the surrounding repetitive work.

**5. Use agents to investigate and refine designs**
- **Run an experimentation loop:** Form a solution hypothesis, implement it, run tests, inspect behavior, revise the design, and repeat. Use agent assistance to reduce the effort of producing candidate designs while retaining behavioral inspection as the basis for revision.
- **Give agents discovery tasks:** Ask agents to investigate unfamiliar codebases, question requirements assumptions, or prototype two alternative designs and report how each behaves. This makes their work part of discovery rather than limiting it to converting tickets into pull requests; compare the reported behavior before selecting an approach.
- **Invest in engineering judgment:** Give domain understanding, clear intent, architecture, tradeoffs, behavioral verification, and customer problems sustained attention. As implementation becomes cheaper, these decisions become proportionally more important, not just preliminary inputs or a final quality gate.
- **Manage for learning under constraints:** Replace the question of how to keep agents supplied with tickets with questions about converting assumptions into evidence, exploring alternatives cheaply, discovering errors quickly, and learning about customers each iteration. Keep that exploration within architectural and safety constraints, because faster investigation does not remove product-development uncertainty.

**Try this first:** Take one ticket, identify an unresolved assumption about its desired behavior, and turn it into a solution hypothesis to implement, test, inspect, and revise rather than treating the ticket as a finished design.

**Caveat:** The cited organizational findings and claims about agent discovery capabilities and speed are not independently verified in the supplied notes; establish their applicability before relying on them for consequential organizational changes.

## Derived summary
## Article context and central argument

Timestamps are absent. All evidence references use the supplied passage ID. These notes summarize Rob West’s article, published 19 September 2026. Its arguments, cited research findings, and descriptions of agent capabilities are source claims, not independently verified.

- West revisits his 2019 argument that coders are creatives rather than factory workers: software development involves understanding problems and designing solutions. He argues that production-line management produces worse software and drives away strong developers.
- The article’s central thesis is that coding agents strengthen software engineering’s identity as design engineering. West predicts that organizations benefiting most will use agents to design better, rather than simply manufacture more output.
- He identifies a resurgence of factory language: Factory’s June 2026 announcement describes outside signals flowing through autonomous agents; Warp describes agents performing triage, specification, implementation, review, verification, CI/CD, and monitoring; BCG Platinion describes agents building, testing, and shipping around the clock while humans define intent and review outcomes.
- West acknowledges that the underlying technology is genuinely new and some implementations are impressive. His objection concerns the management model used to explain and organize that technology.

## Metaphors shape management behavior

- A factory metaphor implies a theory of work: inputs pass through repeatable processes to become outputs, and improvement means higher throughput, less variation, and more automation.
- That theory encourages leaders to optimize utilization, standardize inputs, count outputs, eliminate variability, and treat specifications as raw material. West argues that practices appropriate for production can harm a system whose purpose is design and discovery.

## Software already has a factory

### Source code is the design

- West traces the distinction to Jack Reeves’s 1992 essay, *What Is Software Design?*: source code is the software design, while compilers and linkers perform the build. Programming therefore belongs to design rather than manufacturing.
- In Reeves’s framing, testing and debugging also constitute design work because they validate and refine the design. Software construction, unlike physical construction, is so cheap as to be almost free.
- Martin Fowler’s *The New Methodology* draws an organizational consequence: when construction is effectively free, the effort lies in creative design, whose predictability may not match traditional engineering methodologies’ promises.
- Dave Farley’s *Modern Software Engineering* similarly characterizes software development as discovery, learning, and design. The bridge analogy separates determining which bridge will work from the expensive, slow, risky task of physically constructing it; software, in this framing, primarily faces the first problem.

### The automation boundary

- West locates software’s existing factory in the sequence from source code to compiler, package, and deployment. Build systems, continuous integration, infrastructure as code, and deployment pipelines have automated that sequence over the last two decades.
- This production system should be repeatable and standardized. Coding agents operate on the other side of its boundary: they create and revise source code, and therefore create and revise designs.
- The alternative analogy is an additional designer working through hypothesis, implementation, test, and revision. West contrasts this with BCG Platinion’s labeling of code and test generation as “Construction,” which conflicts with Reeves’s distinction.

## Where the factory metaphor breaks

### Manufacturing presumes a solved design problem

- Manufacturing begins with a sufficiently precise design of what should be made. In software, determining desired behavior, system structure, and tradeoffs among constraints is itself much of the work. A ticket is not an engineering drawing; treating it as one hides design work rather than eliminating it.

### Requirements are hypotheses

- Requirements contain ambiguity, mistaken assumptions, and gaps. Building software produces information that changes the understanding of what was wanted, so specifications need to evolve with learning rather than function as fixed raw materials.
- West connects this to his distinction between complicated code and complex people and problem domains. His argument is that a “spec in, software out” process cannot resolve that underlying complexity merely through process control.

### Variation can create value

- Manufacturing seeks identical outputs, but design benefits from alternatives. West’s example is ten agents producing ten different approaches: their differences can be useful if teams compare, test, and select among them. Forcing convergence through identical production stations can discard that value.

### Keeping the line busy can conceal uncertainty

- A factory needs a steady queue of well-defined work orders. West argues that this creates pressure to make tickets appear precise before sufficient knowledge exists.
- The resulting ambiguity remains inside the agent’s input. An agent may resolve it with a plausible guess and deliver a confident, well-tested implementation of the wrong thing. The causal problem is premature certainty, not necessarily a failure to implement the ticket.

## What the cited evidence says about acceleration

### Speed depends on the surrounding organization

- West reports that the 2025 DORA report characterizes AI as an amplifier of existing organizational strengths and weaknesses. Its interpretation is that teams have adapted for speed faster than their surrounding systems have adapted.
- According to the article’s account of DORA, organizations with mature value stream management were better able to translate individual improvements into organizational gains. Returns therefore depend on the organizational system, not just the tools.
- West interprets this as evidence that code is an intermediate artifact rather than the final product. Its value depends on design quality, feedback about whether changes were right, and architecture that limits the blast radius when they were not.
- The cited DX *State of AI Impact in Engineering Q2 2026 Report* says AI accelerates output rather than innovation. Its reported conclusion is that reclaiming capacity for new features requires removing organizational friction, rather than assuming tool-driven speed automatically creates innovation.

### Automation is not the same as customer value

- Warp proposes measuring the percentage of changes shipped automatically and their cost rather than the number of features an engineer ships. West agrees that feature counts are poor measures, but argues that the replacement measures production-line automation rather than customer outcomes.
- In West’s hypothetical example, if agents generate ten times as many changes, counts of pull requests, story points, features, or automated changes become less informative about productivity. This is an illustration, not a reported benchmark.
- His preferred economic questions concern whether the product performs better, customers receive more value, risk decreases, and the organization learns faster.

## The factories worth building

- West explicitly supports standardization and automation for genuinely production-like work: build pipelines, environment provisioning, test-suite execution, dependency upgrades, routine migrations, formatting, static analysis, and some remediation.
- He cites BCG Platinion’s reference to Spotify’s reported migration-workflow time savings as an example of automation where the design question has largely been settled and the remaining effort is repetitive. The article supplies no numerical savings figure.
- The Software Engineering Institute’s value-stream distinction separates discovery activities, including requirements refinement, architecture, technical spikes, and exploratory testing, from production activities, including builds, configuration management, regression testing, and coding to established patterns. Software development interleaves both.
- West’s boundary is therefore not “avoid factories,” but build factories for actual production without equating them with software engineering as a whole.
- He notes that Warp identifies intent definition, trace review, and release approval as throughput constraints. West interprets those constraints as the design loop, suggesting that thoughtful factory advocates partly share his underlying diagnosis.

## Agents as design collaborators

### Cheap experimentation changes the economics

- West describes an agentic experimentation loop: form a solution hypothesis, implement it, run tests, inspect behavior, revise the design, and repeat. He claims agents can execute this loop faster than a human team.
- Reeves’s nearly free build made designing through code and tests economically attractive. West argues that agents extend this advantage by reducing the cost of producing candidate designs as well.
- As implementation becomes cheaper, domain understanding, clear intent, architecture, tradeoffs, behavioral verification, and judgment about customer problems become proportionally more important. These are core work, not merely pipeline inputs or a final quality gate.

### Discovery is part of the agent’s role

- West describes capable agents as able to investigate unfamiliar codebases, question assumptions in requirements, prototype two alternative designs, and report how each behaves. These are claimed capabilities, rather than demonstrations supplied in the article.
- Treating agents solely as scalable workers converting tickets into pull requests leaves much of that potential unused. His argument is that agents can participate in discovery, not eliminate its necessity.

## Design engineering at machine speed: final recap

- West explains the appeal of factories to software funders: repeatable processes and measurable outputs promise predictability, capacity planning, and economies of scale after decades of overruns and underdelivery.
- His counterargument is that autonomous agents do not remove product-development uncertainty; they increase the speed at which teams can investigate it.
- The management questions consequently shift from keeping agents supplied with specified tickets to converting assumptions into evidence, exploring alternative designs cheaply, discovering errors quickly, learning about customers each iteration, and operating reliably within architectural and safety constraints.
- The closing thesis draws on roughly thirty years of thinking from Reeves through agile to Farley: software is design work. West argues that coding agents reinforce that lesson and should enable design engineering at machine speed, rather than a return to manufacturing-oriented management.

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
