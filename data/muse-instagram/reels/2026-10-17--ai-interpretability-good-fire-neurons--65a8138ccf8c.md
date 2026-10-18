# AI interpretability breakthrough: reading 90% of neurons

## Source
- Original: https://www.instagram.com/reel/DenXU2Quu38/
- Platform: Instagram Reel
- Creator: Nate B. Jones (nate.b.jones)
- Published: 2026-10-17
- Processed: 2026-10-18T18:45:35Z

## Tags
ai-interpretability, ai-safety, neural-networks, good-fire, interpretability, ai-research

## Core components
- The black-box problem: models treated as opaque since before ChatGPT
- Good Fire's neuron-level analysis of a vision model
- The car-and-cat neuron finding: unexpected co-activations that encoded a shared pose or angle, not the objects
- Transfer of the same technique to large language models, reportedly reading over 90% of neurons
- Scaling interpretability tooling across all systems

## Derived summary
The creator frames recent interpretability work as the best AI news in a long time: we may finally be able to read and understand how AI models think. The key shift, in his telling, is that older interpretability attempts projected human assumptions onto models, while newer methods reveal how models represent concepts in their own terms. His central example is Good Fire's analysis of a vision model, where a single neuron fired for both cars and cats. Confusing at first, the deeper read showed the neuron encoded a shared conceptual feature, something like a pose or angle, common to those examples. This suggests models operate at a different conceptual level than human labels. The same technique reportedly worked on large language models, allowing researchers to read over 90% of neurons, which he presents as a major AI safety advance: understanding how models make decisions. The caveat he states directly is that this does not roll out to every system overnight; tools still need to be built and scaled up. The claims about the research organization and the 90% figure come from the creator's narration and should be verified against the original source before being treated as fact.

## Practical takeaways
- Interpretability may be becoming a real engineering discipline, not just a research curiosity. Watch for tooling that exposes neuron-level concepts in models your team uses.
- When evaluating model behavior, remember models may group inputs by shared internal features (poses, angles, contexts) that do not match human categories.
- For AI safety work, this kind of research is a signal to track: being able to read model internals changes what "understanding the model" can mean.

## Notes
This card is derived from a private Muse processing record. Verify important claims against the original source.
