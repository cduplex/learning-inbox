# "Jev for Images" Just Changed Visual Automations Forever

## Source
- Original: https://www.youtube.com/watch?v=0SFKD0xkdR8
- Type: youtube
- Creator: {'displayName': 'Jay E | RoboNuggets'}
- Published: 2026-10-28T00:00:00.000Z

## Tags
image classification, decision models, business automation, confidence-based routing, human review, image localization, document classification, video cropping, Jev, Typesafe

## Learning guide
**The arc**
How can a business check large batches of images without the cost and delay of asking a large model to analyze each one? Jev for images centers the workflow on small, structured decisions rather than generated paragraphs. The guide moves from setup and simple sorting to confidence-based review, then to visual checks that support more advanced automations alongside LLMs.

**1. Define the decision and connect the model**
- **Ask small questions:** Use Jev for yes/no answers, selection from a supplied list, or a score on a scale rather than paragraph generation. Write plain-English checks that return the decisions your automation needs.
- **Locate what matters:** Use the **box** feature when presence alone is not enough. For parcel damage, ask both whether damage exists and where it appears so a reviewer can go straight to the relevant area.
- **Connect through an agent:** Start in a coding or AI agent, visit Typesafe's website, and obtain an API key to connect the agent to your account and Jev. This gives the agent access to the model for your workflow.
- **Prepare supported inputs:** Supply PNG or JPEG images no larger than **16 megabytes each**. Convert document pages to images, and extract still frames when working with video because Jev does not directly accept video or audio.

**2. Start with repeatable sorting tasks**
- **Sort receipts with three checks:** For a batch such as **1,000 receipts**, ask whether each image is actually a receipt, which category it belongs to, and whether it exceeds the business's dollar limit. Use the results to organize the paper trail and flag large expenditures, supplying your own categories and spending threshold.
- **Categorize a photo folder:** Point the workflow at a shoot's folder and supply the categories you want. For **1,000 event photos**, categories such as product shots, theme photos, and blurry images to discard replace repeated manual sorting with structured decisions.

**3. Route uncertainty before taking action**
- **Bundle checks and use confidence:** Send an image with several small questions and use the returned confidence scores to determine its next step. Yes/no questions include confidence, and categorization provides confidence for each category, so answers need not all receive the same treatment.
- **Separate automation from review:** Set routing thresholds rather than treating every answer as equally reliable. The example sends an answer at **80% confidence** into an automated process and routes a blurry image with **20% confidence** to a person.
- **Assist refund reviewers:** Check customer photos for parcel damage and use **box** to mark its location. Keep a person responsible for reviewing the refund, using the marked area to make that review faster.

**4. Put visual checks where they prevent delays**
- **Check delivery photos immediately:** Build the driver's application to ask whether a parcel is present and assess image sharpness as soon as a photo is taken. If either check fails, request another photo before the driver leaves rather than discovering the problem after a complaint.
- **Route screenshot-based tickets:** Check which application screen a support screenshot shows, whether an error message appears, and whether it concerns checkout or payment. Route the ticket to the appropriate person or department, and use the customer's email contents as well to prioritize urgent issues.

**5. Extend image decisions into larger workflows**
- **Guide face-aware video cropping:** Have Claude extract still frames **every second or so** using a tool such as **FFmpeg**, retaining each frame's position in the video. Send the frames to Jev and use **box** to locate the face, giving Claude the location information needed to crop a vertical version while keeping the subject in frame.
- **Trigger replenishment alerts:** Build a workflow in which a camera photographs a vending machine **every hour** and Jev checks for empty slots and missing products. Send an alert identifying the empty slots and connect it to the larger replenishment process.
- **Classify document pages visually:** Convert pages to images and classify them without reading every word when the task is organizing a collection. Apply this pattern to construction-plan sheets, client documents for accountants and bookkeepers, or loan-application packs for mortgage brokers, comparing the image-based approach with passing the material through an LLM.
- **Keep decision models alongside LLMs:** Assign narrow visual checks to Jev and use their results inside a broader workflow. The video-cropping example follows this division: Jev locates faces in frames, while Claude uses those locations to guide the crop.

**Try this first:** Define your receipt categories and business dollar limit, then write the three checks: “Is this actually a receipt?”, “Which category does it belong to?”, and “Is it above the business's dollar limit?”

**Caveat:** The speed, cost, and performance claims are not independently verified, including the demonstration of 100 receipt photos for about 1 cent and comparisons of up to 200 times faster and 400 times cheaper than frontier models; the delivery-app and stock-monitoring integrations are proposed workflows, not demonstrated deployments.

## Derived summary
## [00:00] Opening demonstration and scope

Source-attribution note: These notes summarize Jay's narration only. Product capabilities, prices, timings, comparisons, and third-party examples are source claims, not independently verified. The captions vary the product's spelling; these notes use “Jev,” and “Typesafe” for the company.

- [00:00] Jay opens with a receipt-photo demonstration, saying he sends the same four questions to Jev for images and Claude to compare response speed.
- [00:10] He describes Jev's response as very fast and substantially cheaper, and says the demonstration runs in real time rather than being sped up.
- [00:22] A second demonstration processes 100 additional receipt photos for about **1 cent total**. Jay describes the comparison model as slower and more expensive, but the narration does not provide its exact timing or cost.
- [00:40] The video introduces an image-capable update to Typesafe's decision model, followed by setup guidance and eight business use cases progressing from simple to advanced.

## [01:10] Decision model fundamentals and image localization

- [01:10] Jay describes Jev as a tiny AI model that differs from Claude or ChatGPT because its purpose is to make decisions rather than generate paragraphs.
- [01:23] He attributes its claimed efficiency to that narrower purpose: **up to 200 times faster** and **up to 400 times cheaper** than large frontier models.
- [01:32] Its three answer formats are **yes/no**, **selection from a supplied list**, and **a score on a scale**. Categorization is an example of selecting from a list.
- [01:43] Previously, inputs had to be text. The update adds images, including photos, screenshots, scanned receipts, and document pages converted to images.
- [02:04] A new feature called **box** identifies where something is located within a picture, rather than merely reporting whether it is present.
- [02:12] The introductory example is parcel damage: the model can be asked both whether damage exists and where it appears.
- [02:31] Jay explains that marking the damage location can make later manual review faster because the reviewer is directed to the relevant part of the image.
- [02:43] His broader rationale is that checking thousands of images with a large model can be costly and slow; he presents plain-English checks run through Jev as a faster, cheaper alternative.

## [03:01] Setup, supported inputs, and pricing

- [03:06] The described setup starts in a coding or AI agent. A setup prompt is intended to have that agent guide the user through connecting to Typesafe.
- [03:17] The connection workflow involves visiting the company's website, obtaining an **API key**, and using it to let the agent access the user's account and Jev model.
- [03:29] **Promotional resource aside:** Jay offers a free PDF containing the use cases, related starter prompts, and a setup prompt. The supplied captions do not contain the actual prompts.
- [03:44] The stated image formats are **PNG and JPEG**, with a maximum of **16 megabytes per image**.
- [03:51] Jev does not directly accept video or audio. Jay identifies extracting still frames from a video as a workaround for image analysis.
- [03:58] The stated input price is approximately **4 cents per million tokens**. Output tokens, described as what Jev returns, are said to be **free**, which Jay cites as part of the reason for its low cost.

## [04:22] Use case 1: Receipt sorting

- [04:25] Jay frames receipt sorting around businesses that need a paper trail, using a hypothetical batch of **1,000 receipts**.
- [04:33] The proposed checks are three small questions: **Is this actually a receipt? Which category does it belong to? Is it above the business's dollar limit?** No specific spending threshold is supplied.
- [04:40] He says the same approach can handle hundreds of receipt images quickly and inexpensively, organizing records while flagging large expenditures.

## [04:54] Use case 2: Organizing a photo folder

- [04:57] The next example is a photography business with **1,000 event photos** that need sorting into user-described categories.
- [05:10] Example categories include product shots, “theme photos” as transcribed in the captions, and blurry images to discard.
- [05:20] Jay says the demonstrated sorting takes only a few seconds. He separately reports a shared build that sorted about **900 images in 40 seconds**.
- [05:28] The described automation points Jev at a shoot's folder and categorizes its images, replacing repeated manual sorting.

## [05:35] Confidence scores and routing decisions

- [05:42] Jay describes sending an image together with several small questions and receiving all three answers together in a fraction of a second.
- [05:50] He says each question returns a **confidence score**, including yes/no questions. For categorization, the model returns a confidence score for each category.
- [06:07] These scores provide a basis for routing thresholds in an automation, rather than treating every answer identically.
- [06:11] His illustrative threshold is **80% confidence**: an answer at that level could be sent into an automated process.
- [06:16] A blurry image might instead receive **20% confidence**. Jay's example routes such uncertain cases to a person for review.
- [06:30] He emphasizes the importance of this confidence-based review pattern when introducing damage detection with the box feature.

## [06:34] Use case 3: Damaged-parcel review

- [06:38] The scenario is an e-commerce business receiving customer photos of allegedly damaged parcels with refund requests.
- [06:48] Jay describes passing those photos to Jev to check for damage in almost real time, then using box to mark its location.
- [06:58] In the proposed workflow, a person still reviews the refund. The marked location is intended to help that reviewer decide in seconds.

## [07:08] Use case 4: Proof-of-delivery photo checks

- [07:08] The related delivery example starts with drivers photographing each parcel at the customer's door.
- [07:18] Two problems are highlighted: a blurry delivery photo and a photo that does not contain the parcel. Jay says these problems are often discovered only after a customer complains.
- [07:27] He proposes checking the photo immediately when the driver takes it, rather than waiting for a later complaint.
- [07:31] The integration is explicitly theoretical: the driver's application would ask whether a parcel is present and assess image sharpness.
- [07:40] If the checks fail, the application would request another photo before the driver leaves. Jay presents the model's speed as what makes this immediate feedback possible.

## [07:49] Use case 5: Routing support tickets using screenshots

- [07:51] Jay extends an existing text-based ticket-routing use case to software-support screenshots, especially those accompanying bug reports.
- [08:04] The image checks would identify which application screen is shown, whether an error message appears, and whether the screenshot concerns checkout or payment.
- [08:15] These classifications would route the ticket to the appropriate person or department.
- [08:21] Prioritization would also take the customer's email contents into account, bringing urgent tickets forward rather than relying only on the screenshot.

### [08:38] Promotional aside

- [08:38] Jay promotes his AI-builder community, a regularly updated Claude course, and an agents-as-a-service course focused on earning from AI work. This is promotional material rather than additional technical instruction.

## [09:11] Use case 6: Face-aware cropping for short videos

- [09:12] The first advanced example concerns converting longer videos into shorts while keeping the subject's face in frame.
- [09:17] Jay reiterates that Jev cannot watch video directly. His workaround has Claude extract still frames **every second or so**, using a free, open-source tool such as **FFmpeg**.
- [09:30] Those stills are sent to Jev. The workflow retains the timestamps associated with the extracted frames so their results can be related to the video.
- [09:40] The box feature locates the face in the supplied frames, giving Claude information about where to crop when producing a vertical version.
- [09:54] Jay presents this as useful for dynamic long-form footage, avoiding manual movement of a crop box or extensive LLM token expenditure on the cropping task.

## [10:08] Use case 7: Stock-monitoring alerts

- [10:08] The physical-product example involves vending machines or other displays that need replenishing.
- [10:16] In this explicitly theoretical workflow, a small camera photographs a vending machine **every hour**.
- [10:22] Jev checks the photos for empty slots and identifies which products are missing.
- [10:26] An automation would issue an alert identifying empty slots and connect to a larger replenishment workflow.
- [10:35] Jay acknowledges that this is a niche example, using it to illustrate adding relatively fast, inexpensive visual checks to existing systems.

## [10:45] Use case 8: Classifying document pages

- [10:45] The final example treats document pages as images and classifies large page collections without having to read every word.
- [10:56] Jay reports a third-party example involving a complete construction-plan set: every sheet was labeled in **2.9 seconds** for approximately **half a cent**. The narration does not state the sheet count.
- [11:06] He extends the idea to accountants and bookkeepers organizing client documents, and mortgage brokers sorting loan-application packs.
- [11:18] The stated tradeoff is to compare this image-based approach with passing the material through an LLM, since LLMs work with text.
- [11:26] For visually rich documents, such as architectural material, Jay predicts that Jev for images is likely to be applicable. This is an expectation, not a demonstrated result for every document type.

## [11:35] Closing recap

- [11:35] Jay closes by describing the image update as a sensible direction for Typesafe and welcoming developments in model types beyond large language models.
- [11:40] His concluding view is that decision-oriented models such as Jev can enable new business uses for AI alongside LLMs.

## Evidence anchors
- [00:00:00.080] So on this demo interface is a sample
- [00:00:01.920] photo of a receipt. And just to show you
- [00:00:03.520] how fast J for images is, I'll send the
- [00:00:05.759] same four questions to it and to Claude.
- [00:00:14.719] model. And that was not sped up. That is

## Notes
This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.
