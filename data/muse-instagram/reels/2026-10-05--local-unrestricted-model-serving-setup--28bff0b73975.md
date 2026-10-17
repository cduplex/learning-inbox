# Running an unrestricted open model locally: llama.cpp, GGUF, and the Ajax release

## Source
- Original: https://www.instagram.com/reel/DeIrl8UJZ0V/
- Platform: Instagram Reel
- Creator: @codrkai (codrkai)
- Published: 2026-10-05T19:32:38
- Processed: 2026-10-16T23:38:21Z

## Tags
local-llms, open-weights, llama-cpp, ai-safety, model-releases

## Core components
- The release in question: Odysseus (described as PewDiePie's company) releasing an unrestricted AI model called Ajax
- The replication stack: an open "abliterated" model weight file in GGUF format (17.9 GB), installed with Homebrew and llama.cpp on a MacBook Pro, served through a local server
- The harness pattern: connecting a web UI (DeepSeek's web interface) to the local model server to interact with it

## Derived summary
The creator explains that PewDiePie's company Odysseus released an unrestricted AI model called Ajax, and shows how to replicate it with the open "Qwen 3.5 9B Abliterated" model from Hugging Face. He walks through downloading the 17.9 GB GGUF file, installing Homebrew and llama.cpp on his MacBook Pro, starting a local server with specific parameters, and connecting the DeepSeek web UI to that local server. A flag on this content: the video's demonstration centered on the model complying with a request for illicit instructions (a money-laundering scheme), and the creator reacts approvingly to that compliance. This card deliberately does not reproduce those instructions; it records only the release fact and the standard local-serving mechanics. All claims about the model, its capabilities, and the Ajax release come from the creator and are not verified here. Because of the subject matter, this card should receive a human review before any downstream use.

## Practical takeaways
- The local-serving stack pattern is standard and reusable: weight file, llama.cpp runtime, local server, web UI on top.
- Know what "abliterated" means: weights modified to remove safety alignment; running them is a deliberate choice with real consequences.
- Evaluate a model's safety posture yourself before running uncensored weights, especially if the output will touch other people or systems.
- Treat release claims from creator videos as leads to verify against the model publisher's own documentation, not as facts.

## Notes
This card is derived from a private Muse processing record. Verify important claims against the original source.
