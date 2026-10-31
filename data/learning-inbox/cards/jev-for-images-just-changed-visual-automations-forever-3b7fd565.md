# "Jev for Images" Just Changed Visual Automations Forever

## Source
- Original: https://www.youtube.com/watch?v=0SFKD0xkdR8
- Type: youtube
- Creator: {'displayName': 'Jay E | RoboNuggets'}
- Published: 2026-10-28T00:00:00.000Z

## Tags
Jev for images, Typesafe, decision models, image classification, bounding boxes, confidence-based routing, business automation, document classification, support-ticket routing, video reframing

## Learning guide
**The arc**
The starting question is how to make fast, cheap visual decisions across hundreds or thousands of images without sending each one to a large model like Claude. The central idea is that Jev, Typesafe's tiny decision model, now accepts images and can answer yes-or-no, categorize, score, and locate things with a feature called Box. The video moves from what Jev does, to setup and pricing, to confidence-based routing, then through eight business use cases arranged from easy to advanced, ending with the view that non-LLM model types open new business uses.

**1. Know what Jev is for**
- **Use it for decisions, not writing:** Jev is built to make decisions rather than write paragraphs, which is why it is far faster and cheaper than frontier models (up to 200 times faster and 400 times cheaper). Reach for it when you need many small judgments on many inputs.
- **Pick one of three decision formats:** Ask a yes-or-no question, have it select from a list you supply for categorization, or have it return a score on a scale. Frame every check you want as one of these.
- **Feed it images:** Inputs can now be photographs, screenshots, scanned receipts, and document pages converted to images, not just text.
- **Use Box to show where:** Box locates something within a picture instead of only saying whether it is present, such as where damage appears on a parcel. Marking the area lets a human reviewer jump straight to it and decide faster.

**2. Set it up**
- **Let an agent connect you:** Start in a coding assistant or AI agent with a setup prompt and let it guide you through connecting to Typesafe and Jev.
- **Get an API key:** Obtain an API key from Typesafe's website so your assistant can access your account and reach Jev.
- **Respect the input limits:** Send PNG or JPEG files up to 16 megabytes each. Jev does not take video or audio, so extract still frames from video first.
- **Know the cost model:** Input costs about 4 cents per million tokens and output tokens are free, which keeps batch jobs cheap (the demo sorted 100 receipts for about 1 cent total).

**3. Design checks and route by confidence**
- **Bundle small questions per image:** Send one image with several small questions and get all answers back together in a fraction of a second. Describe the checks in plain English and apply them across the whole batch.
- **Read the confidence scores:** Every answer, including yes-or-no, comes with a confidence score, and categorization returns a score for each category.
- **Set a threshold:** Let high-confidence answers (for example 80%) flow into automated processing, and send low-confidence ones (like a blurry image at 20%) to a person. Lean on this especially when using Box.

**4. Starter use cases**
- **Sort receipts and flag spending:** For a pile like 1,000 receipts, ask three things per image: is this a receipt, which category does it belong to, and does it exceed your dollar limit. You get categorized records plus flags for large expenses, for your business or a client's.
- **Clean up a photo folder:** Point Jev at a folder such as 1,000 event photos with your own categories (product shots, themed photos) and have it flag blurry images to discard. A shared build reportedly sorted about 900 images in 40 seconds.
- **Spot parcel damage for refunds:** Send customer photos of damaged parcels to Jev to check for damage almost in real time, then use Box to mark the damaged area. A person still approves the refund but can decide in seconds.
- **Check proof-of-delivery at the door:** Have the driver's app ask whether the parcel is in the shot and whether the photo is sharp, and prompt a retake before the driver leaves. This catches problems immediately instead of after a complaint.
- **Route tickets from screenshots:** Classify bug screenshots by which app screen is shown, whether an error message is present, and whether it shows checkout or payment. Route to the right person or department and use the email content to decide urgency.

**5. Advanced use cases**
- **Keep a face in frame for vertical clips:** Have Claude extract a still frame about every second with FFmpeg, keep each frame's timestamp, and use Box to locate the face. Use those positions to guide where to crop when converting long videos to vertical shorts, avoiding manual crop dragging and heavy large-model token use.
- **Add stock alerts with a camera:** Photograph a vending machine or product display every hour and ask Jev for empty slots and which product is missing. Trigger alerts and feed them into your restocking workflow; the broader lesson is to add quick, cheap visual checks to existing systems.
- **Classify document pages as pictures:** Treat pages as images to label a pile without reading every word, as in a construction-plan set reportedly labeled in 2.9 seconds for about half a cent. Apply it to accountants organizing client documents or mortgage brokers sorting loan packs, and favor it for visually rich material like architectural drawings over text parsing by an LLM.

**Try this first:** Get a Typesafe API key, connect it through your coding assistant, and run a folder of receipts through three questions (is it a receipt, which category, over your limit) with an 80% confidence threshold that sends the rest to you for review.

**Caveat:** The speed, cost, and third-party results come from the creator's narration without benchmark methodology, so test on your own images before building a workflow around them.

## Derived summary
## [00:00] Opening demonstration: fast image decisions

Source-attribution note: These notes summarize Jay's narration and reported demonstrations. Product capabilities, prices, timings, comparisons, and third-party results are source claims, not independently verified. The captions use several variants of the model's name; these notes use “Jev” and the company name “Typesafe” as supplied.

- [00:00] The opening demonstration uses a receipt photograph and sends the same four questions to Jev for images and Claude. Jay describes Jev's response as extremely fast and says the demonstration is running in real time, not sped up. [p0001–p0009]
- [00:18] The batch example contains 100 more receipt photographs. Jay reports that Jev sorts them quickly for about 1 cent in total, while the comparison model, transcribed as “Sonic,” would categorize the same 100 more slowly and at greater expense. [p0010–p0020]
- [00:40] The video introduces an image-capable update to Typesafe's decision model, followed by setup instructions and eight business use cases arranged from easier to more advanced. [p0021–p0030]

## [01:10] What Jev does and what image support adds

- [01:10] Jay describes Jev as a tiny AI model that differs from Claude or ChatGPT because its primary role is making decisions rather than writing paragraphs. [p0037–p0043]
- [01:23] He links this narrower role to claimed efficiency: up to 200 times faster and up to 400 times cheaper than large frontier models. The source does not provide a benchmark methodology for those figures. [p0043–p0046]
- [01:32] Jev supports three decision formats: answering yes-or-no questions, selecting from a supplied list for categorization, and returning a score on a scale. [p0047–p0052]
- [01:43] Previously, inputs had to be text. The update adds images, including photographs, screenshots, scanned receipts, and document pages converted into images. [p0053–p0061]

### [02:02] The Box feature: identifying where something is

- [02:02] The new feature called “Box” locates something within a picture rather than merely deciding whether it is present. [p0062–p0066]
- [02:12] The introductory example is parcel damage: the model can be asked both whether a parcel is damaged and where the damage appears in its photograph. [p0067–p0078]
- [02:35] The stated benefit of marking the relevant area is faster subsequent human review, because the reviewer is directed to the suspected damage. [p0078–p0081]
- [02:43] Jay frames the broader value as avoiding the cost and time of sending thousands of images to a large model individually. Instead, users describe the desired checks in plain English and apply them to an image batch. [p0082–p0090]

## [03:01] Setup, supported inputs, and pricing

- [03:01] The described setup starts with a coding assistant or AI agent and a setup prompt. Jay says the agent can guide the user through connecting to Typesafe and its Jev model. The exact prompt is not included in the supplied captions. [p0091–p0102]
- [03:22] The connection requires obtaining an API key from Typesafe's website. Jay explains that this lets the assistant access the user's Typesafe account and connect to Jev. [p0103–p0106]
- [03:29] **Resource aside:** Jay offers a free PDF containing use cases, related starter prompts, and the setup prompt. The captions describe the resource but do not supply its contents. [p0107–p0114]
- [03:44] The stated image formats are PNG and JPEG, with a limit of up to 16 megabytes per image. [p0115–p0117]
- [03:51] Jev does not directly accept video or audio. For video-related workflows, Jay proposes extracting still frames first and processing those images instead. [p0118–p0122]
- [03:58] The quoted price is about 4 cents per million input tokens. Output tokens, meaning what Jev returns, are described as free, which Jay identifies as part of the reason for the low cost. [p0122–p0127]

## [04:22] Use case 1: receipt sorting and spending flags

- [04:22] The receipt workflow is intended for businesses that need a paper trail and have many receipts to organize, with 1,000 receipts used as an example workload. [p0134–p0139]
- [04:33] Each receipt is reduced to three small decisions: whether the image is actually a receipt, which category it belongs to, and whether it exceeds the business's dollar limit. No specific dollar threshold is supplied. [p0140–p0142]
- [04:40] Jay says this can handle hundreds of receipt images quickly and cheaply, producing categorized records and flags for large expenses for either the user's business or a client's business. [p0143–p0151]

## [04:57] Use case 2: organizing a messy photo folder

- [04:57] The next example is sorting a folder such as 1,000 event photographs. Jev evaluates each image against categories described by the user. [p0152–p0158]
- [05:10] Example categories include product shots and themed photographs, alongside identifying blurry images that need to be discarded. [p0159–p0163]
- [05:20] Jay describes the demonstrated sorting as taking a few seconds and cites a separate shared build that reportedly sorted about 900 images in 40 seconds. [p0164–p0167]
- [05:28] The proposed workflow is a shoot-sorting automation that points Jev at a folder and organizes its contents, particularly for businesses or clients handling substantial photography workloads. [p0168–p0171]

## [05:35] How the responses support confidence-based routing

- [05:35] Jay pauses the use cases to explain the response behavior: an image can be sent together with several small questions, and the example returns all three answers together in a fraction of a second. [p0172–p0179]
- [05:50] He says each question produces a confidence score, including yes-or-no questions. For categorization, the model provides a confidence score for each category. [p0180–p0188]
- [06:07] These scores allow an automation to use a threshold. Jay's example routes an answer into automated processing when Jev is 80% confident. [p0189–p0193]
- [06:16] His contrasting example is a blurry image producing only 20% confidence. Such uncertain images can be routed to a person for review rather than handled entirely by the automation. [p0194–p0200]
- [06:30] Jay highlights confidence-based handling as especially important when using the image-localization feature, Box. [p0201–p0203]

## [06:36] Use case 3: spotting damage in parcel photographs

- [06:36] The scenario is an e-commerce operation receiving customer photographs of damaged parcels as part of refund requests. [p0204–p0209]
- [06:48] The described workflow sends the photographs to Jev to check for damage in almost real time, then uses Box to mark the suspected damaged area. [p0210–p0213]
- [06:58] A person still reviews the refund in the example. The automation's contribution is to draw attention to the damage beforehand, which Jay says can let that person decide in seconds. [p0214–p0218]

## [07:08] Use case 4: checking proof-of-delivery photographs

- [07:08] For delivery operations, drivers take photographs of parcels at the door. Jay identifies two problematic cases: a blurry photograph and a photograph that does not contain the parcel at all. [p0219–p0228]
- [07:25] He contrasts discovering these problems after a customer complaint with checking immediately when the driver takes the photograph. [p0229–p0231]
- [07:31] In the proposed, explicitly theoretical integration, a driver's app asks whether a parcel is in the shot and evaluates photo sharpness. [p0232–p0236]
- [07:40] If the photograph fails those checks, the app could ask the driver to take it again before leaving. Jay attributes the feasibility of this immediate feedback to Jev's claimed response speed. [p0237–p0241]

## [07:51] Use case 5: routing support tickets using screenshots

- [07:51] Jev's existing text-based support-ticket routing is extended to screenshot inputs, particularly for software users reporting bugs. [p0242–p0250]
- [08:10] Example decisions include identifying which application screen is shown, whether an error message is present, and whether the screenshot shows checkout or payment. [p0251–p0254]
- [08:17] Those classifications can route the ticket to the appropriate person or department. The customer's email content can also inform which tickets receive urgent treatment. [p0255–p0259]

### [08:38] Promotional aside

- [08:38] Jay briefly promotes an AI-builder community, a regularly updated Claude course, and an agents-as-a-service course focused on earning from AI skills. This is promotional material rather than an additional technical workflow. [p0267–p0285]

## [09:11] Use case 6: keeping a face in frame when creating vertical clips

- [09:11] The first advanced example concerns turning longer videos into shorts while keeping the subject's face within the vertical frame. Jev cannot watch the video directly. [p0286–p0290]
- [09:22] The workaround is for Claude to extract still frames approximately every second using a free, open-source tool such as FFmpeg, then send those images to Jev. [p0291–p0296]
- [09:34] In the vlog example, the frames are associated with their timestamps. Box locates the face, giving Claude information about its position at the sampled points in the video. [p0297–p0304]
- [09:51] The face-location information then guides where to crop the footage when converting it to vertical format. [p0305–p0306]
- [09:54] Jay presents this as a way to clip dynamic long-form footage without manually dragging a crop box around or spending many large-model tokens on the cropping task. [p0307–p0313]

## [10:08] Use case 7: stock alerts for physical products

- [10:08] The next scenario involves vending machines or other product displays that need to remain stocked. [p0314–p0317]
- [10:16] In this explicitly theoretical setup, a small camera photographs the vending machine every hour. Jev checks the resulting images for empty slots and identifies which product is missing. [p0318–p0323]
- [10:28] An automation can issue alerts about empty slots and connect those findings to a larger workflow for keeping the machines stocked. [p0324–p0327]
- [10:35] Jay acknowledges that the example is niche. Its broader purpose is to illustrate adding quick, inexpensive visual checks to an existing system. [p0328–p0332]

## [10:45] Use case 8: classifying large collections of document pages

- [10:45] Document pages can be treated as pictures, allowing Jev to classify a pile of pages without reading every word. [p0333–p0338]
- [10:56] Jay reports a third-party example involving a complete construction-plan set: every sheet was reportedly labeled in 2.9 seconds for about half a cent. The captions do not specify the number of sheets. [p0338–p0342]
- [11:06] Other proposed settings include accountants or bookkeepers organizing client documents and mortgage brokers sorting loan-application packs. [p0343–p0350]
- [11:20] Jay says the image-based approach should be compared with parsing everything through an LLM, noting that LLMs work with text. He presents visually rich documents, such as architectural material, as particularly plausible candidates for Jev for images. [p0351–p0358]

## [11:35] Final recap and closing perspective

- [11:35] The closing perspective is that image support broadens the business uses of a specialized decision model beyond its earlier text-only role. Jay views the expansion as a sensible move for Typesafe. [p0359–p0361]
- [11:40] Jay welcomes development in model types other than large language models, arguing that these alternatives can enable new and better business uses of AI. The video closes with a brief invitation to follow further business-focused AI lessons. [p0362–p0372]

## Evidence anchors
- [00:00:00.080] So on this demo interface is a sample
- [00:00:01.920] photo of a receipt. And just to show you
- [00:00:03.520] how fast J for images is, I'll send the
- [00:00:05.759] same four questions to it and to Claude.
- [00:00:07.919] And if I send that prompt, you can see

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
