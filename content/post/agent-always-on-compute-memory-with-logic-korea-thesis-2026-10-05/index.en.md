---
title: "Compute Gets Cheaper While Memory Accumulates: Why Korean Memory Is Adding Logic in the Agent Era"
date: 2026-10-05T22:20:00+09:00
categories: ["Exclusive Analysis", "AI Infrastructure", "Korean-Equities"]
tags: ["Memory", "Samsung Electronics", "SK hynix", "HBM", "Custom HBM", "Agents", "KV cache", "Enterprise SSD", "HBF", "CXL", "Long-term supply agreements"]
slug: "agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05"
description: "As more AI agents take on entire tasks, compute becomes cheaper while context and knowledge accumulate. This analysis examines the split between batch and real-time workloads, demand for CPUs and networks, HBM and SSD products with embedded logic, long-term contracts and deposits, then calculates how much earnings durability current Korean memory share prices require."
image: "cover.png"
draft: false
---

The same question sent to the same AI model can cost very different amounts depending on how it is processed. Anthropic's price list charges half the standard rate for batch processing that can return an answer within a day, and twice the rate for a fast mode that guarantees a quicker response. Re-reading context that has already been processed costs one-twentieth of the standard rate.[^anthropic-pricing]

This price list compresses the direction of AI infrastructure into a few lines. Non-urgent work is handled cheaply; urgent work is expensive. The cheapest task is not calculating something new, but retrieving something already remembered.

<strong>As delegated agents that take on entire tasks become more common, compute becomes more efficient while context and knowledge accumulate. The memory and storage that hold this accumulation are shifting from standardized components toward products with embedded logic. The key question for Korean memory investment is less how large this year's earnings are than how long they can last.</strong>

The links to verify run in sequence: whether infrastructure is shifting to always-on computing; whether compute is actually becoming more efficient; what is accumulating; whether embedding logic in memory is translating into revenue; and whether Korean companies retain that value. The final section calculates how much earnings durability the current share prices of Samsung Electronics and SK hynix require.

The analysis is dated October 5, 2026. Share prices are the October 2 closes; no Korean regular-session trade record was available for October 5. Company statements, research-firm forecasts, and this article's calculation assumptions are identified separately. The sensitivity tables below are calculations for testing the thesis, not price targets.

<link rel="stylesheet" href="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/thesis.css">

## Infrastructure is shifting from answering prompts to running toward goals

A chatbot calculates only when a question arrives. A delegated agent works differently. Once a user assigns it a goal, it makes a plan, uses tools, checks the result, and tries again if needed. The work continues even after the user closes the screen.

That changes the unit of workload. In the chatbot era, workload was close to the number of users connected at the same time. In the agent era, it is closer to the number of users multiplied by the number of goals assigned per user and the time each goal remains active. This is goal-oriented, always-on computing.

Products and price lists already show signs of this shift. Anthropic's Managed Agents charges $0.08 per hour for the time a session remains active, in addition to token charges. Its documentation says the session retains state, which is why batch discounts do not apply.[^anthropic-pricing][^managed-agents]

At its developer event in May 2026, Google introduced a personal agent that runs all day on a dedicated virtual machine. In the same presentation, it said monthly processed tokens had risen from about 480 trillion in May 2025 to more than 3.2 quadrillion in May 2026, or roughly sevenfold in a year. These are company-reported figures; Google did not disclose the agent share.[^google-io]

Task duration is also increasing. In METR's January 2026 measurement, the task length Claude Opus 4.5 could complete with a 50% success rate was 320 minutes of human work. Since 2024, this duration had doubled about every 89 days. METR also acknowledges uncertainty at the upper end of its task set.[^metr]

The figure below lays out this article's full logic chain. Each arrow is a link to test, not an established fact.

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/chain.svg" alt="Logic chain from delegated agents to always-on computing, more efficient compute and accumulated state, memory with embedded logic, and earnings durability"><figcaption>Conceptual diagram. Growing demand and memory manufacturers retaining the resulting value are separate links. On mobile, swipe horizontally to read the figure.</figcaption></figure>

## Prices for urgent and non-urgent work now differ by as much as four times

Always-on work is not all urgent. There is no reason to use the same infrastructure for organizing documents overnight and answering a user who is waiting. Model companies have separated these workloads through pricing.

| Company and model | Batch or low-speed | Standard | Fast or priority | Cached-context read |
|---|---:|---:|---:|---:|
| Anthropic Opus 5.5 | 0.5x | 1x | 2x | 0.05x |
| OpenAI gpt-6-astra | 0.5x | 1x | 2x | 0.1x |
| Google Gemini 3.1 Pro Preview | 0.5x | 1x | 1.8x | Separate storage fee |

All three companies differentiate prices for the same model by response speed. The gap between the cheapest and most expensive tier is 3.6 to 4 times. Google also charges for the time context remains stored in its cache. Context storage has become a separate product.[^anthropic-pricing][^openai-pricing][^google-pricing]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/pricing.svg" alt="Bar chart of batch, fast, and cached-read price multiples relative to the standard input price for Anthropic Opus 5.5"><figcaption>Based on Anthropic's official price list, accessed October 5, 2026. Multiples use the standard input price as 1. Cached reads are input prices for reusing context that has already been processed.</figcaption></figure>

This split matters to investors because it affects infrastructure utilization. Facilities serving only real-time demand have large differences in utilization between day and night. If non-urgent work is priced cheaply during idle hours, the same infrastructure runs throughout the day. Always-on computing does not only increase demand; it also reduces idle time.

## Repetitive tasks move to smaller models and code

If an agent performs the same kind of task tens of thousands of times a day, there is no reason to call the largest model each time. Repetitive subtasks can move in two directions: to a small model specialized for that task, or to code that runs without a model.

The price list supports the case for smaller models. OpenAI charges $10 per million input tokens for gpt-6-astra and $0.10 for gpt-6-luna, a 100-fold difference within the same company. NVIDIA researchers estimated in a 2025 paper that specialized small models could replace 40–70% of agent calls. That is a paper estimate, not a measured share.[^openai-pricing][^nvidia-slm]

Product documentation supports the case for code. Anthropic's Agent Skills documentation says scripts within a skill run in a shell, and only their results enter the model's context. The script code itself does not. This turns a procedure the model would otherwise reason through each time into code that is written once and reused.[^agent-skills]

Web automation company Skyvern reported results from converting a task performed once by an agent into code and replaying it without a model. Execution time fell from 279 seconds to 120 seconds, and cost per run fell from $0.11 to $0.04. These are the company's own measurements.[^skyvern]

A key distinction follows. Compute per task declines. But the fixed code, specialized model weights, and execution records must be stored somewhere. Efficiency comes from using less compute while reusing more stored information.

## The work does not end with GPUs

An agent's task consists of several stages. GPUs handle reasoning. CPUs run tools, handle files, and execute code in isolated environments. Networks move data between stages.

Comments on CPU demand from several companies have pointed in the same direction this year. Amazon CEO Andy Jassy said in the July earnings call that most agent tool use runs on CPUs rather than AI accelerators. AMD CEO Lisa Su forecast in August that the server CPU market would reach $220 billion by 2030, with agents and isolated execution environments as its largest segment. Both statements are management commentary and forecasts.[^amzn-call][^amd-call]

There are also physical signals. TrendForce reported in April that server CPU prices had risen 10–20% since March and lead times had extended from 1–2 weeks to 8–12 weeks. This was secondary reporting citing Taiwanese and Japanese media. NVIDIA has shipped its 88-core Vera CPU, explicitly designed for isolated agent execution.[^tf-cpu][^nvda-vera]

Networking also involves more than one type. Connections within a rack link chips; Ethernet connects racks; CXL expands memory capacity. At its September earnings call, Broadcom said AI networking revenue had more than doubled from a year earlier and demand for optical communications lasers greatly exceeded supply.[^avgo-call]

Data processing units are also emerging as a separate category. In March, NVIDIA announced a BlueField-4-based design that manages context data in front of storage, and said partner products would arrive in the second half of 2026. As of October 5, I found no material confirming actual shipment and operation.[^nvda-stx]

The conclusion is not that GPUs are becoming less important. GPUs, CPUs, data processing units, and several types of networks are needed together. All of these devices also require memory.

## Compute can be reused, but context and knowledge accumulate

The flow so far can be reduced to one sentence: agent infrastructure expands memory so it does not have to perform the same computation twice.

Language models generate intermediate calculations when they read long context. These are called KV cache. If the cache is retained, the model can reuse the same context without calculating it from scratch. That is why cached context in the opening price list costs one-twentieth of the standard rate.

The cache can be large. In a technical document published in June, IBM estimated that one request's KV cache could be about 3–10 GB for a medium-sized model and 40–80 GB for a large model. It reported that reusing the cache cut time to first response for a 130,000-token input by a factor of 56. This is the company's own measurement.[^ibm-kv]

NVIDIA has defined a new storage tier for this cache. It places an Ethernet-connected flash tier below GPU HBM, server memory, and in-server SSDs, and calls it CMX. NVIDIA also released software that decides which tier should hold the cache.[^nvda-cmx][^nvda-dynamo]

The same theme appeared in memory companies' earnings releases. On September 30, Micron said data center SSD revenue was nearly $10 billion for the quarter, more than 10 times the year-earlier figure. It cited context storage, which moves KV cache to lower tiers, as one reason.[^mu-remarks]

SK hynix said in its July earnings release that enterprise SSD revenue had doubled from the prior quarter, citing KV cache storage and storage placed close to GPUs as new use cases. Samsung Electronics expects server SSDs to account for more than 60% of NAND revenue in 2026. These two statements were checked against earnings-call transcripts republished by media outlets.[^skh-call][^sec-call]

In August, the CEO of hard-drive maker Western Digital described the distinction this way: compute cycles can be reused, but data compounds. Agents leave records at every step, and those records become inputs for later tasks.[^wdc-call]

Growth rates and dollar amounts still need to be kept separate. One person's personal-agent memory is not large in capacity terms. The value grows if inference services broadly shift to a design that moves cache to flash storage. That transition is still at an early stage.

## Memory is shifting from standardized components to products with embedded logic

As data accumulates, customers ask more of memory. They ask not only about capacity, but also whether data can be retrieved in time, how much power it uses, and how well it fits their chips. Meeting these needs requires logic inside memory.

SK hynix stated this shift directly in its July US listing prospectus. It wrote that memory companies had previously supplied commodity components, but memory plays a central role in performance optimization in the AI era. It described its vision as a full-stack AI memory creator. This is the company's self-description and should be distinguished from facts established by operating results.[^skh-424b4]

The most advanced example is the HBM base die. HBM stacks multiple memory dies, and the base die at the bottom handles signals and power. Earlier generations used a memory process. Starting with HBM4, the base die is made on a logic process. Samsung Electronics uses its own 4-nanometer process. In 2024, SK hynix announced a collaboration to make the HBM4 base die on TSMC's logic process.[^sec-hbm4][^skh-tsmc]

The next step is custom HBM, which puts the customer's logic on the base die. On August 26, NVIDIA announced NVHBM, which places its memory-control circuitry on the HBM base die. NVIDIA claims 30% higher bandwidth and 15% lower power than standard HBM4E. On September 30, Micron said it was developing the product with NVIDIA.[^nvda-nvhbm][^mu-remarks]

At the Hot Chips semiconductor conference in August, Samsung Electronics presented the next stages as well: moving control circuitry; putting compute elements on the base die so it can take on some processor calculations; and directly stacking memory on top of compute chips. It provided no launch schedule.[^sec-hotchips]

Products in storage and other memory categories are moving in the same direction, but their maturity varies widely.

| Product | Embedded logic | Current stage |
|---|---|---|
| HBM4 base die | Signal and power control built on a logic process | In volume production, revenue generated |
| SOCAMM2 | Low-power memory module for servers | In volume production, sales increasing |
| Enterprise SSD | Controller and firmware, with a context-storage design | In volume production, revenue surging |
| Custom HBM, NVHBM | Customer memory-control circuitry | In development, planned for next-generation GPUs |
| CXL memory module | Monitoring circuitry that identifies frequently used data | Samsung production targeted for late 2026, according to reports; delays are possible |
| HBF | High-bandwidth interface that places NAND close to compute chips | First technical specification released in August 2026; product not yet available |
| PIM, HBM with compute elements | Compute circuitry within memory | Prototypes and roadmap |

The products listed as in volume production are supported by this year's earnings materials. Samsung Electronics' second-quarter results identified rising demand for HBM base dies as a factor in foundry performance. Custom HBM and the products below it have not yet been confirmed in revenue. SK hynix said it would retain its existing bonding method through HBM4E. An industry event in September characterized CXL as a supplementary tier rather than a replacement for HBM.[^sec-ir][^skh-q2][^tf-cxl][^hbf-ocp][^sec-fms][^skh-hybrid][^tf-cxl-doubt]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/maturity.svg" alt="Diagram grouping memory products with embedded logic into three stages: revenue generation, development and samples, and roadmap"><figcaption>Stages classified from company statements and earnings materials. Products further left are visible in this year's results; products further right have less defined schedules. As of October 5, 2026.</figcaption></figure>

So the statement that memory is adding logic is directionally right, but its scope remains limited. Products with revenue confirmed today are HBM4, server modules, and enterprise SSDs. Commodity DRAM and NAND still compete on specifications and price.

## The hypothesis that memory will become central to computing is confirmed only in direction

A longer-term hypothesis is that the structure of computing itself will change. Today, compute is central and memory supplies data to it. If data grows faster than compute, moving data can cost more than processing it. In that case, it may be better to compute where the data resides.

Several initiatives point in this direction. The final stage of Samsung Electronics' roadmap stacks memory directly on top of compute chips. Qualcomm said it would put a three-dimensional combination of compute and memory in products in 2027. SK hynix and Sandisk developed a specification with Google and Tenstorrent that places NAND right next to compute chips.[^sec-hotchips][^qcom-hbc][^hbf-ocp]

At its August earnings call, Sandisk's CEO described AI as fundamentally a memory-centric and storage-intensive problem. The statement comes from the CEO of a memory company and should be considered in that context.[^sndk-call]

The assessment of this hypothesis should be clear. In 2026, memory-centric computing is an option, not an investment case. There is no independent performance validation, no volume-production schedule, and no confirmed customer adoption. It cannot explain current share prices. If the direction proves right, however, the largest beneficiaries would be companies that combine memory, logic processes, and stacking technology.

## The investment case for Korean memory is shifting from earnings size to duration

Now consider the Korean companies. Earnings this year are already large. Samsung Electronics' semiconductor operating profit in the second quarter was KRW 89.2 trillion, equal to 70% of revenue. SK hynix's second-quarter operating profit was KRW 60.5 trillion, or 76% of revenue.[^sec-ir][^skh-q2]

Yet share prices do not value these earnings highly. At the October 2 close, Samsung Electronics traded at 5.85 times estimated 2026 earnings and SK hynix at 5.25 times. The earnings estimates are broker averages compiled by Naver Finance.[^naver-sec][^naver-skh]

Low multiples can be read as a sign that the market still views memory as a cyclical industry. The concern is that current earnings come from tight supply and will collapse as before once capacity additions are complete. This is an interpretation, but it has a basis: SK hynix itself listed recurring memory-industry oversupply among the risk factors in its prospectus.[^skh-424b4]

This is where memory with embedded logic matters to the investment case. It does not necessarily increase this year's earnings. The key is whether it can provide a reason for earnings to decline less than before after supply normalizes. The reasons are switching costs and contract structures.

First, customers may find it harder to change suppliers. A base die designed for a customer's chip cannot easily be replaced with another company's product. Design, validation, and certification time create switching costs. The size of actual switching costs and whether they support pricing remain unverified hypotheses.

Second, contract structure matters. On September 30, Micron said it had signed 26 strategic customer agreements. Customers owe payment even if they do not purchase the volume committed to over several years. Customer financial commitments total $32 billion, mostly cash deposits. Micron said this visibility supported higher capital spending.[^mu-remarks]

The two Korean companies are moving in the same direction. SK hynix said it had completed long-term supply agreement negotiations with about 10 customers in the second quarter, and explained on its call that they included financial mechanisms such as deposits. Samsung Electronics said it planned to allocate 60–70% of capacity through long-term contracts, structured for an initial five years with annual extensions. Prices and cancellation terms for individual contracts were not disclosed.[^skh-q2][^skh-lta][^sec-lta]

An industry where customers commit to volumes and deposit money upfront behaves differently from one where standardized products are traded on the spot market. Long-term contracts cut both ways, however. TrendForce reported that price mechanisms in long-term contracts had kept some suppliers' server DRAM price increases below the market average. Suppliers gain a floor in downturns but give up some upside in expansions.[^tf-memory]

## Samsung Electronics and SK hynix occupy different positions in the same shift

The two companies have different strengths and weaknesses in the same shift toward memory with embedded logic.

| Item | Samsung Electronics | SK hynix |
|---|---|---|
| Second-quarter semiconductor operating margin | 70% | 76% |
| HBM4 base die | In-house 4-nanometer process | TSMC process |
| Where logic value accrues, this article's analysis | Could remain inside the company as foundry earnings | Cost paid externally |
| Product breadth | HBM, server modules, SSDs, foundry, packaging | HBM, server modules, SSDs, HBF specification leadership |
| Long-term contracts | Plans to allocate 60–70% of capacity | Completed negotiations with about 10 customers |
| Shareholder returns | About KRW 30 trillion in dividends planned for Q3 | KRW 40 trillion share cancellation approved |
| Share price to estimated 2026 earnings | 5.85x | 5.25x |

SK hynix's strengths are current profitability and customer relationships. Its operating margin is higher, and it has already completed long-term supply agreement negotiations with about 10 customers. Its weakness is that it pays externally for logic value. According to TrendForce, citing Korean media, TSMC-made HBM4 base dies cost three to four times as much as memory dies. The company has not confirmed this figure.[^tf-basedie]

Samsung Electronics' strength is a structure in which logic value can remain inside the company. Samsung describes itself as the only company with memory, logic design, foundry, and packaging capabilities.[^sec-fms] Its weakness is that this structure has not yet been sufficiently demonstrated in earnings. Revenue from an internally made base die must not be counted twice as if it were money earned from an external customer. The evidence must come from consolidated costs and cash flows.

Shareholder returns are a channel through which earnings reach shareholders. In August, SK hynix approved KRW 40 trillion in share repurchases and cancellation of all repurchased shares, and raised its free-cash-flow return target to at least 50%. Samsung Electronics planned about KRW 30 trillion in cash dividends in the third quarter, subject to confirmation by its board at the end of October. Both items were checked against media reports; the original filings were not cross-checked.[^skh-return][^sec-return]

My judgment is as follows. As logic becomes more deeply embedded in memory, the company structurally advantaged is the one that makes logic in-house. Based on current results and customer position, SK hynix is ahead today. SK hynix's execution may matter more in the early stage of the shift, while Samsung Electronics' integrated structure may become more valuable as custom HBM and later stages scale up. The inflection point is when base dies made by Samsung Foundry enter volume production using designs from external customers.

## Current share prices assume that only about half of this year's earnings will remain

A simple way to view a share price is as sustainable earnings multiplied by a valuation multiple. If we assume the market assigns memory companies a multiple of 10 times, we can reverse the calculation to estimate the earnings level implied by current prices.

Samsung Electronics closed at KRW 276,000 on October 2. At 10 times earnings, the share price implies earnings per share of KRW 27,600, or 58.5% of estimated 2026 EPS of KRW 47,142. SK hynix closed at KRW 1,842,000. The same calculation implies EPS of KRW 184,200, or 52.5% of estimated EPS of KRW 350,576.[^naver-sec][^naver-skh]

In other words, current prices are consistent with an assumption that only a little more than half of 2026 earnings will persist. This does not mean that it is the market's precise view. Many combinations of earnings and multiples are possible. The question is clear, though: can products with embedded logic and long-term contracts keep normalized earnings above half of this year's level?

The tables below vary the share of estimated 2026 earnings that remains and the valuation multiple. Figures in parentheses show the change from the October 2 close. Both the retained-earnings ratios and multiples are assumptions for this article's calculations, not probabilities. Dividends are excluded.

Samsung Electronics, reference share price: KRW 276,000

| Share of estimated 2026 earnings retained | 8x | 10x | 12x |
|---|---:|---:|---:|
| 40% | KRW 151,000 (-45.3%) | KRW 189,000 (-31.7%) | KRW 226,000 (-18.0%) |
| 55% | KRW 207,000 (-24.8%) | KRW 259,000 (-6.1%) | KRW 311,000 (+12.7%) |
| 70% | KRW 264,000 (-4.3%) | KRW 330,000 (+19.6%) | KRW 396,000 (+43.5%) |

SK hynix, reference share price: KRW 1,842,000

| Share of estimated 2026 earnings retained | 8x | 10x | 12x |
|---|---:|---:|---:|
| 40% | KRW 1,122,000 (-39.1%) | KRW 1,402,000 (-23.9%) | KRW 1,683,000 (-8.6%) |
| 55% | KRW 1,543,000 (-16.3%) | KRW 1,928,000 (+4.7%) | KRW 2,314,000 (+25.6%) |
| 70% | KRW 1,963,000 (+6.6%) | KRW 2,454,000 (+33.2%) | KRW 2,945,000 (+59.9%) |

The two ends of the tables show the point. If only 40% of earnings remain, the share price is below current levels even if the multiple rises to 12 times. A good industry story cannot offset a decline in earnings. Conversely, if investors believe 70% of earnings will remain, prices are 20–33% higher even at the unchanged 10-times multiple.

There is a caveat in SK hynix's figures. Second-quarter net income was KRW 93.9 trillion, higher than operating profit of KRW 60.5 trillion. I could not confirm the reason. If non-operating items drove the difference, estimated annual EPS may also include earnings that will not recur, in which case the retained-earnings ratio should be lower.[^skh-q2]

The key to re-rating is the share of earnings that remains, not the valuation multiple. Memory with embedded logic and long-term contracts could raise that share. Whether they do so will become clear as supply expands in 2027 and 2028.

## The strongest counterargument is that the value of logic goes to the designer

There is a strong counterargument to this thesis. I list the most consequential points first.

The first is who captures the value. NVIDIA designed the control circuitry placed on the base die in NVHBM. NVIDIA has said that multiple memory companies will supply the same specification. Micron will outsource production of that base die to an external foundry. In this structure, design value accrues to NVIDIA, manufacturing value to the foundry, and memory companies may again compete on the same specification.[^nvda-nvhbm][^mu-foundry]

A similar dynamic could play out in storage. In NVIDIA's context-storage design, the data-management compute sits in NVIDIA's data processing unit, not inside the SSD. NVIDIA also provides the software that decides which tier should hold the cache. Where data accumulates and where customer switching costs arise may be different places.[^nvda-cmx][^nvda-dynamo]

This counterargument challenges the article's logic most directly. Embedding logic in memory is separate from the memory company owning that logic. It is also why this article emphasizes Samsung Electronics' integrated structure. A memory company that cannot make logic itself may occupy a narrower position as products become more sophisticated.

The second counterargument is demand adaptation. When memory becomes expensive, customers look for ways to use less. On September 29, TrendForce wrote that GPU and custom-chip companies were considering lower HBM capacity per device and prioritizing eight-layer configurations for 2027. Google researchers published a compression technique in March that reduced KV cache memory use to one-sixth or less. Anthropic's documentation says accuracy declines as context grows and offers a feature that summarizes older conversations.[^tf-hbm][^turboquant][^anthropic-context]

There is no answer yet on whether accumulation will outpace technologies that reduce usage. Micron also acknowledged that price increases had somewhat slowed growth in memory per server.[^mu-remarks]

The third counterargument is supply and funding. TrendForce forecast on July 30 that NAND supply would ease in the second half of 2027, creating downward pressure on prices. According to TrendForce reporting, CXMT's DRAM revenue share rose to 9.5% in the second quarter. In a September 10 speech, the head of the Bank for International Settlements warned that major technology companies' capital spending was exceeding cash flow. If customers run short of cash, long-term commitments will also be tested.[^tf-supply][^tf-china][^bis]

Micron takes the opposite view and expects supply and demand to be tighter in 2027 and 2028 than in 2026. The fact that a research firm and a supplier disagree is itself a reason not to treat the 2027 outlook as settled.[^mu-remarks]

The demand premise is also open to challenge. This article starts from the assumption that people will keep assigning work to agents. In Anthropic's company-reported usage data published in February, tasks lasting more than 45 minutes in a single session were in the top 0.1%. Most tasks are much shorter. If delegation does not become habitual or users do not grant agents authority, always-on computing will grow more slowly than this article assumes.[^anthropic-autonomy]

## Next quarter, check the evidence for earnings durability rather than the price

Future results can test this thesis. The table lists what to monitor and what would change the assessment.

| What to check | Signal supporting the thesis | Signal weakening the thesis |
|---|---|---|
| Third-quarter results, October | Higher HBM4 and enterprise SSD volumes; better product mix | Most earnings growth comes from commodity price increases |
| Long-term contracts | Disclosure of deposits and minimum purchase terms; contract renewals | Earnings surrendered under price caps; terms remain undisclosed |
| Custom HBM | Samsung Foundry base dies enter volume production for external customers | Three suppliers compete on the same standard specification |
| Context storage | CMX partner products ship; dedicated storage-server contracts | Compression spreads; shipments are delayed |
| 2027 supply | Contract prices continue to rise; customers raise investment plans | NAND prices fall; HBM capacity per device is reduced |

Samsung Electronics' preliminary third-quarter results were reported for October 8. The operating-profit consensus compiled by FnGuide was KRW 108.1 trillion. SK hynix was expected to report in late October, with an operating-profit consensus of KRW 77.2 trillion. Both figures are based on media reports as of October 5; I could not confirm official company schedule announcements.[^consensus]

The details matter more than the headline figures. If operating profit exceeds consensus only because commodity prices rose, it says little about this thesis. If operating profit misses consensus but HBM4 volumes and the quality of long-term contracts improve, the evidence for durable earnings may actually strengthen.

The condition that would change my assessment is also clear. If custom HBM settles on a single specification, the three memory suppliers compete on the same product, and 2027 contract prices begin to fall, this thesis should be downgraded. Korean memory would then be making more sophisticated products but would still be valued as a cyclical industry.

<strong>Agents use memory to save compute. Logic is entering the products that hold that memory, and some customers have begun depositing money in advance. A re-rating of Korean memory depends on whether these changes support earnings after supply expands. Current prices still imply that only a little more than half of this year's earnings will remain.</strong>

## Sources and limits of the calculations

Company statements, filings, and research-firm materials were cross-checked as of October 5, 2026. Statements verified through media republishing earnings-call transcripts are identified in the footnotes. Company-reported performance figures are not independently verified. The retained-earnings ratios and valuation multiples in the sensitivity tables are calculation assumptions, not forecasts. Estimated EPS is taken as reported by Naver Finance; I could not confirm 2027 estimates.

[^anthropic-pricing]: [Anthropic official pricing](https://platform.claude.com/docs/en/about-claude/pricing), accessed 2026-10-05. Opus 5.5 standard input $4, batch $2, fast $8, and cached reads $0.20 per million tokens. Includes the Managed Agents session fee.

[^managed-agents]: [Claude Managed Agents overview documentation](https://platform.claude.com/docs/en/managed-agents/overview), accessed 2026-10-05. Documentation for a beta product.

[^google-io]: [Summary of Sundar Pichai's Google I/O 2026 keynote](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/), 2026-05. Company-reported figures.

[^metr]: [METR Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/), 2026-01-29. Time horizon at a 50% success rate.

[^openai-pricing]: [OpenAI API pricing](https://developers.openai.com/api/docs/pricing), accessed 2026-10-05. gpt-6-astra standard $10, Flex $5, Fast $20, and cached input $1. gpt-6-luna input $0.10.

[^google-pricing]: [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing), updated 2026-10-01. Gemini 3.1 Pro Preview standard $2, batch $1, Priority $3.60, plus an hourly cache-storage fee.

[^nvidia-slm]: [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153), submitted by NVIDIA researchers on 2025-06-02. The paper presents a view; 40–70% is an estimate.

[^agent-skills]: [Anthropic Agent Skills overview documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), accessed 2026-10-05.

[^skyvern]: [Code-replay measurements on the Skyvern blog](https://www.skyvern.com/blog/asking-ai-to-build-scrapers-should-be-easy-right/), published 2025-10-17, updated 2026-08-24. Company's own measurements.

[^amzn-call]: [Republished transcript of Amazon's Q2 2026 earnings call](https://www.investing.com/news/transcripts/earnings-call-transcript-amazon-tops-q2-2026-estimates-as-aws-growth-accelerates-93CH-4826442), 2026-07-30. Management statement.

[^amd-call]: [Republished transcript of AMD's Q2 2026 earnings call](https://www.fool.com/earnings/call-transcripts/2026/08/11/amd-amd-q2-2026-earnings-call-transcript/), call on 2026-08-04. Market size is a company forecast.

[^tf-cpu]: [TrendForce report on server CPU prices](https://www.trendforce.com/news/2026/04/22/news-server-cpu-prices-up-as-much-as-20-since-march-intel-may-raise-prices-another-8-10-in-2h26/), 2026-04-22. Cites Taiwanese and Japanese media.

[^nvda-vera]: [NVIDIA announcement on Vera CPU shipments](https://blogs.nvidia.com/blog/vera-cpu-delivery/), 2026-05-18.

[^avgo-call]: [Republished transcript of Broadcom's FY2026 Q3 earnings call](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/), call on 2026-09-02. Management statement.

[^nvda-stx]: [NVIDIA announcement of BlueField-4 STX storage architecture](https://nvidianews.nvidia.com/news/nvidia-launches-bluefield-4-stx-storage-architecture-with-broad-industry-adoption), 2026-03-16. Performance figures are company claims.

[^ibm-kv]: [IBM Redbooks KV cache technical document](https://www.redbooks.ibm.com/docs/MD260021/MD260021.html), published 2026-06-05. Company measurements and estimates.

[^nvda-cmx]: [NVIDIA CMX product description](https://www.nvidia.com/en-us/data-center/ai-storage/cmx/), accessed 2026-10-05. Publication date not shown.

[^nvda-dynamo]: [NVIDIA Dynamo KV cache tiering documentation](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/kv-cache-offloading), accessed 2026-10-05. The document does not provide performance figures.

[^mu-remarks]: [Micron FY2026 Q4 prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf), 2026-09-30. Data center SSD revenue is described in the original as "nearly $10 billion." Strategic customer agreements, deposits, NVHBM, and supply-demand outlook were cross-checked in this document.

[^skh-call]: [Republished transcript of SK hynix's Q2 2026 earnings call](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q2-2026-results-as-shares-fall-93CH-4818480), July 2026 call. Not the company's official transcript.

[^sec-call]: [Republished transcript of Samsung Electronics' Q2 2026 earnings call](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q2-2026-profit-as-ai-demand-surges-93CH-4822292), July 2026 call. Not the company's official transcript.

[^wdc-call]: [Summary of Western Digital FY2026 Q4 earnings call](https://finance.biggo.com/news/US_WDC_2026-08-05), 2026-08-05. Statement checked in a secondary summary.

[^skh-424b4]: [SK hynix US listing prospectus, SEC 424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm), 2026-07-09. Strategy section, Custom HBM definition, and risk factors checked against the original.

[^sec-hbm4]: [Samsung Electronics announcement of HBM4 volume shipments](https://news.samsungsemiconductor.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/), 2026-02-12. Process and performance are company descriptions.

[^skh-tsmc]: [SK hynix and TSMC announcement of HBM4 collaboration](https://www.prnewswire.com/news-releases/sk-hynix-partners-with-tsmc-to-strengthen-hbm-technological-leadership-302120755.html), 2024-04-18. Announcement of development direction at the time.

[^tf-basedie]: [TrendForce report on SK hynix HBM4E base dies](https://www.trendforce.com/news/2026/08/31/news-sk-hynix-reportedly-weighs-intel-for-hbm4e-base-dies-amid-tsmc-cost-pressure-and-supply-diversification/), 2026-08-31. Cites Korean media; not confirmed by the company.

[^nvda-nvhbm]: [NVIDIA announcement of NVHBM](https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory/), 2026-08-26. Bandwidth and power figures are company claims.

[^sec-hotchips]: [ServeTheHome summary of Samsung Electronics' Hot Chips 2026 presentation](https://www.servethehome.com/samsung-evolving-hbm-base-die-at-hot-chips-2026/), 2026-08-23. Roadmap is a company presentation; no schedule was provided.

[^sec-ir]: [Samsung Electronics Q2 2026 earnings presentation](https://images.samsung.com/kdp/ir/events/2026/2026_2Q_conference_kor.pdf), 2026-07-30. Semiconductor revenue KRW 127.5 trillion, operating profit KRW 89.2 trillion. Cites HBM base die demand as a factor in foundry performance.

[^skh-q2]: [SK hynix Q2 2026 earnings release](https://news.skhynix.com/en/q2-2026-business-results/), 2026-07-29. Revenue KRW 79.3 trillion, operating profit KRW 60.5 trillion, net income KRW 93.9 trillion, long-term supply agreements, and SOCAMM2.

[^tf-cxl]: [TrendForce report on Samsung and SK hynix CXL 3.2](https://www.trendforce.com/news/2026/07/21/news-samsung-reportedly-targets-2026-cxl-3-2-mass-production-sk-hynix-advances-new-ai-memory-architecture/), 2026-07-21. Secondary reporting.

[^hbf-ocp]: [Sandisk and SK hynix release the first HBF OCP specification](https://www.storagenewsletter.com/2026/08/05/fms-2026-sandisk-and-sk-hynix-advance-global-standardization-of-high-bandwidth-flash-with-release-of-first-ocp-technical-specification/), 2026-08-05.

[^sec-fms]: [StorageReview summary of Samsung Electronics' FMS 2026 presentation](https://www.storagereview.com/news/samsung-outlines-3d-memory-roadmap-for-ai-infrastructure-at-fms-2026), 2026-08-04. Low-power memory with PIM was shown; volume-production timing was not confirmed.

[^skh-hybrid]: [Tom's Hardware report on SK hynix's Hot Chips 2026 presentation](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling), 2026-08-24.

[^tf-cxl-doubt]: [TrendForce report from the AI Infrastructure Summit](https://www.trendforce.com/news/2026/09/18/news-openai-intel-reportedly-downplay-cxl-as-hbm-replacement-citing-use-case-and-data-transfer-limits/), 2026-09-18. Secondary reporting.

[^qcom-hbc]: [Qualcomm announcement of data center roadmap](https://www.qualcomm.com/news/releases/2026/06/qualcomm-unveils-comprehensive-data-center-roadmap-for-the-agent), 2026-06. Performance figures are company claims and have not been independently verified.

[^sndk-call]: [Republished transcript of Sandisk FY2026 Q4 earnings call](https://www.fool.com/earnings/call-transcripts/2026/08/12/sandisk-sndk-q4-2026-earnings-call-transcript/), call on 2026-08-05.

[^naver-sec]: [Naver Finance Samsung Electronics daily prices](https://m.stock.naver.com/api/stock/005930/price?pageSize=5&page=1) and [annual financial estimates](https://m.stock.naver.com/api/stock/005930/finance/annual), accessed 2026-10-05. October 2 close KRW 276,000; estimated 2026 EPS KRW 47,142.

[^naver-skh]: [Naver Finance SK hynix daily prices](https://m.stock.naver.com/api/stock/000660/price?pageSize=5&page=1) and [annual financial estimates](https://m.stock.naver.com/api/stock/000660/finance/annual), accessed 2026-10-05. October 2 close KRW 1,842,000; estimated 2026 EPS KRW 350,576.

[^skh-lta]: [NewsPim report on SK hynix's Q2 earnings call](https://www.newspim.com/news/view/20260729000198), 2026-07-29. Deposit statement checked in media reporting.

[^sec-lta]: [The Elec transcript of Samsung Electronics' Q2 earnings call](https://www.thelec.kr/news/articleView.html?idxno=60316), 2026-07-30. Long-term contract share and structure are management plans.

[^tf-memory]: [TrendForce forecast for memory contract prices in Q4 2026](https://www.trendforce.com/presscenter/news/20260930-13258.html), 2026-09-30. Forecast, not realized pricing.

[^skh-return]: [ZDNet Korea report on SK hynix share cancellation](https://zdnet.co.kr/view/?no=20260819161157), 2026-08-19. Original filing not cross-checked.

[^sec-return]: [Report on Samsung Electronics' 2026 shareholder returns](https://v.daum.net/v/20260821172850433), 2026-08-21. Plan, not an amount already paid.

[^mu-foundry]: [The Elec report on Micron outsourcing base-die production](https://www.thelec.net/news/articleView.html?idxno=14372), 2026-10-02. Micron's prepared remarks do not name the foundry.

[^tf-hbm]: [TrendForce outlook for HBM in 2027](https://www.trendforce.com/presscenter/news/20260929-13255.html), 2026-09-29. Research-firm forecast.

[^turboquant]: [Google Research introduction to TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/), 2026-03-24. Research result; scope of commercial deployment not confirmed.

[^anthropic-context]: [Anthropic context-window documentation](https://platform.claude.com/docs/en/build-with-claude/context-windows) and [compaction documentation](https://platform.claude.com/docs/en/build-with-claude/compaction), accessed 2026-10-05.

[^anthropic-autonomy]: [Anthropic research on measuring agent autonomy](https://www.anthropic.com/research/measuring-agent-autonomy), 2026-02-18. 99.9th percentile in company usage data.

[^tf-supply]: [TrendForce memory supply-demand outlook for 2026–2027](https://www.trendforce.com/presscenter/news/20260730-13158.html), 2026-07-30. Research-firm forecast.

[^tf-china]: [TrendForce report on CXMT and YMTC capacity expansion](https://www.trendforce.com/news/2026/09/24/news-cxmt-ymtc-ramp-memory-capacity-but-chinas-ai-cloud-boom-could-soak-up-new-supply-through-2027/), 2026-09-24. Secondary reporting.

[^bis]: [BIS General Manager's speech](https://www.bis.org/speeches/20260910-artificial-intelligence-growth-and-financial-stability-challenges-central-banks), 2026-09-10.

[^consensus]: [MoneyToday report on third-quarter earnings forecasts](https://www.mt.co.kr/amp/stock/2026/10/05/2026100217315021825), 2026-10-05. Cites FnGuide consensus.

*Disclaimer: This material is for research and information purposes. The companies, multiples, and scenarios are analytical examples. Readers should conduct their own review before making investment decisions.*
