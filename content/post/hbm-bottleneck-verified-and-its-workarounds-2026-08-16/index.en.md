---
title: "AI's Bottleneck Really Is HBM, Not the GPU: But Bottlenecks Invite Workarounds"
slug: "hbm-bottleneck-verified-and-its-workarounds-2026-08-16"
date: 2026-08-16T14:30:00+09:00
description: "This piece verifies the claim that AI's bottleneck has moved from the GPU to HBM. Morgan Stanley's report frames the bottleneck as moving along the supply chain, from chips to power, memory, networking, and cooling, but the figure of roughly 50 billion Gb in 2027 HBM demand that circulates alongside it does not come from that document. It comes from Korean brokerages and research aggregation, and three separate estimates converge on the same range. The core of the claim holds up: compute grows three to four times per generation while bandwidth grows more slowly, agent inference occupies memory through the KV cache, and HBM consumes three times the wafers per bit while yield at 16 layers falls below half, so 2027 supply is effectively locked in by physics. But the same arithmetic is moving buyers too. NVIDIA cut module capacity in half once memory cost reached 29% of system cost, reports say the next flagship's HBM specification will be set below the prior generation, and prefill-only chips skip HBM entirely. It lays out the bottleneck's reality alongside the workarounds it is provoking, and where that leaves the profits of Korean memory makers in between."
categories: ["Exclusive Analysis", "Korea-Semiconductor", "Macro-Analysis"]
tags:
  - "HBM"
  - "Memory Wall"
  - "NVIDIA"
  - "SK Hynix"
  - "Samsung Electronics"
  - "Micron"
  - "KV Cache"
  - "AI Agents"
  - "Morgan Stanley"
  - "HBM4"
  - "Korean Semiconductors"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Series context: over the course of August, this series has covered in turn the deceleration in memory prices, the gap between confirmed demand and the stock price, and the conditions for a rebound. This piece verifies the physical foundation beneath all of that: how far the claim that AI's bottleneck has moved from the GPU to HBM actually holds, what profit that bottleneck guarantees suppliers and for how long, and what countervailing force the bottleneck itself is generating.

## TL;DR

- Start with where the claim and its numbers come from. Morgan Stanley's June report offers the frame that <strong>"the bottleneck moves along the supply chain: first chips, then power, then memory, then networking, then cooling"</strong>, along with the judgment that "memory will be in shortage through the end of 2026." [Fact: Morgan Stanley, June 9] But <strong>the roughly 50 billion Gb of 2027 HBM demand often cited alongside it is a figure absent from that document</strong>. The real sources are Kiwoom Securities (53.4 billion Gb) and Korean research aggregation (6.20 exabytes, about 49.6 billion Gb converted), and working backward from TrendForce's bit-share forecast lands in the same range. Because three separate lines converge, the number is usable, but its attribution needs to be corrected.
- The first basis for the bottleneck is the gap in growth rates between compute and bandwidth. A single GPU's compute has grown three to four times per generation, but HBM capacity is <strong>the same 288GB for both GB300 and the next-generation Rubin</strong>. What did grow is bandwidth, from the 8 terabyte class to the 20 terabyte class, and even that falls short of the roughly 3.5x growth in compute. [Fact: NVIDIA specifications, SemiAnalysis] When memory cannot keep up, buying more chips just means compute sits and waits.
- The second basis is a change in the nature of inference. When an agent works for an extended stretch while holding a long context, <strong>the KV cache, an intermediate memory, occupies memory for the whole session</strong>. Field data shows the processing cost of a cached token versus an uncached one differs by a factor of 10, and NVIDIA thought the problem large enough to launch a dedicated cache storage tier as a separate product line earlier this year. [Fact: industry data] That said, no published quantitative estimate yet exists for how many gigabytes of additional HBM demand agent workloads generate. [Blocked: no public estimate]
- The third basis is the arithmetic of supply. Producing the same capacity in HBM uses <strong>roughly three times the wafers of ordinary DRAM</strong>, and even if a single die's yield is 95%, cumulative yield falls to 66% at 8 layers of stacking and 44% at 16 layers. A fab takes three to five years from groundbreaking to volume production, and new capacity does not contribute meaningfully until 2028. [Fact: industry data, TrendForce] That is why 2027 tightness looks less like a forecast and more like physics. Micron said it cannot fill even half of data center demand and that <strong>"2027 will be tighter than 2026"</strong>, and SK Hynix CEO Kwak Noh-jung described 2027, from a supply standpoint, as the tightest year in the industry's history. [Fact: company statements]
- But the same arithmetic is moving buyers too. Once memory cost reached 29% of system cost, NVIDIA <strong>cut the CPU-side memory module on Vera Rubin in half</strong>, reports say Rubin Ultra's HBM will be set at 192GB, below the prior generation's 288GB, and the prefill-only chip (Rubin CPX) uses GDDR7 instead of HBM. The High Bandwidth Flash that SanDisk and SK Hynix standardized builds a cheaper capacity tier beneath HBM. [Fact: TrendForce, company announcements] <strong>The deeper the bottleneck, the bigger the reward for working around it.</strong>
- Where the bottleneck's profit ends up is a matter of contracts. Micron has locked in roughly half its revenue through contracts with 16 strategic customers running to around 2030, "several-fold" increases in 2027 HBM contract prices are being discussed, and custom base dies tailored to individual customers (custom HBM) lock supplier and customer to each other. [Fact: company data, TrendForce] The rent is being fixed in the form of multi-year contracts rather than a spike in spot prices.
- The implication for Korea. Two of the three oligopoly players are Korean, and SK Hynix's HBM share sits in the mid-to-high 50% range. Profit visibility through 2027 is backed by the physics of the bottleneck. What remains open is 2028. New capacity lands that year, and CXMT's HBM also arrives around then, still carrying yield problems. That is also when the workaround technologies described above accumulate enough effect to matter. The bottleneck claim is correct, but it is <strong>a claim that holds through 2027</strong>, and beyond that it becomes a matter of contract structure and supply discipline.

<div class="thesis-callout">
<div class="thesis-callout__label">Key Framing</div>

The diagnosis that AI's bottleneck has moved from the GPU to HBM passes verification. The gap between compute and bandwidth, the memory occupied by agent inference, three times the wafers for half the yield, and a three-year lead time are all measured facts. But the bottleneck is not static. Once memory reached three-tenths of system cost, the largest buyer began stripping memory out of its designs, and the owners of the bottleneck are themselves fixing prices through multi-year contracts to narrow the swing of the next downturn. The profit coming out of the bottleneck is real, but its size is set by contract terms rather than market price, and its lifespan runs only until new supply arrives in 2028. What investors should ask is not whether the bottleneck exists, but whose books the bottleneck's rent lands on, and in what form.

</div>

## 1. Where the Claim and Its Numbers Come From

Morgan Stanley Investment Management's June report, "Big Picture: Ten Truths About Investing in AI," is the document cited as the origin of this claim. What the document actually argues is this. The bottleneck in AI infrastructure does not stay in one place; it moves along the supply chain. It was chips first, then power, now memory, and next comes networking and cooling. Memory will be in shortage through the end of 2026, and incremental memory demand in 2027 will run 75 to 100 exabytes, doubling again in 2028. Agentic AI requires roughly a million times the compute of the original conversational models, and token consumption grew more than tenfold in 2025 alone. [Fact: Morgan Stanley, June 9, 2026]

There is one thing to correct here. The figure widely cited alongside this report, "roughly 50 billion Gb in 2027 AI-related HBM demand," <strong>does not appear in the document</strong>. The document contains no HBM-specific figures and does not name any of the three suppliers. Tracing this number to its actual source turns up two lines. Kiwoom Securities estimated 2027 HBM demand at 53.4 billion Gb, a 56% increase from the prior year, and Korean research aggregating TrendForce, McKinsey, and others put it at 6.20 exabytes, roughly 49.6 billion Gb when converted to gigabits. [Fact: Kiwoom Securities, VLSI Research Korea]

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="240.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">0.0</text>
<line x1="60" y1="196.8" x2="676.0" y2="196.8" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="200.8" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">12.0</text>
<line x1="60" y1="157.6" x2="676.0" y2="157.6" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="161.6" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">23.9</text>
<line x1="60" y1="118.4" x2="676.0" y2="118.4" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="122.4" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">35.9</text>
<line x1="60" y1="79.2" x2="676.0" y2="79.2" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="83.2" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">47.8</text>
<line x1="60" y1="40.0" x2="676.0" y2="40.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="44.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">59.8</text>
<rect x="111.3" y="61.0" width="102.7" height="175.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="162.7" y="53.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">53.4</text>
<text x="162.7" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">Kiwoom Securities</text>
<text x="162.7" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">+56% YoY</text>
<rect x="316.7" y="73.5" width="102.7" height="162.5" rx="4" fill="var(--kii-cat-1)"/>
<text x="368.0" y="65.5" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">49.6</text>
<text x="368.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">Research synthesis</text>
<text x="368.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">6.20EB converted</text>
<rect x="522.0" y="72.1" width="102.7" height="163.9" rx="4" fill="var(--kii-cat-3)"/>
<text x="573.3" y="64.1" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">50.0</text>
<text x="573.3" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">Share back-solve (own)</text>
<text x="573.3" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">13% bit share</text>
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="60" y="24" fill="var(--card-text-color-tertiary)" font-size="11.5">2027 HBM demand estimates (bn Gb). Three different methods land in the same place</text>
</svg>
</div>
<figcaption><strong>Three routes to 50 billion Gb.</strong> Kiwoom's estimate, a research synthesis converting 6.20 exabytes, and our own back-solve from a 13% bit share land in the same place. The figure does not appear in the Morgan Stanley document.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Route | 2027 HBM demand | Method |
|---|---|---|
| Kiwoom Securities | 53.4bn Gb | +56% year on year |
| Research synthesis | about 49.6bn Gb | 6.20 exabytes converted |
| Own back-solve | about 50bn Gb | TrendForce 13% bit share |

</details>
</figure>

The number itself is solid. Two estimates using different methods converge near 50 billion Gb, and a third path verifies it as well. TrendForce expects HBM to reach about 13% of total DRAM bit supply in 2027; if 50 billion Gb is 13%, total DRAM works out to roughly 380 to 440 billion Gb, which matches the industry's usual scale estimates. [Inference: our own back-calculation] The conclusion is this. The number is usable, but the source is Korean brokerages and research aggregation, not Morgan Stanley, and it should be cited that way.

## 2. Why HBM, Not the GPU: The Gap in Growth Rates

The first foundation of the bottleneck claim is the gap between how fast compute grows and how fast memory grows. Line up GPU specifications generation by generation and the gap is plain to see.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="240.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">0</text>
<line x1="60" y1="196.8" x2="676.0" y2="196.8" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="200.8" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">4.48</text>
<line x1="60" y1="157.6" x2="676.0" y2="157.6" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="161.6" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">8.96</text>
<line x1="60" y1="118.4" x2="676.0" y2="118.4" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="122.4" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">13.44</text>
<line x1="60" y1="79.2" x2="676.0" y2="79.2" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="83.2" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">17.92</text>
<line x1="60" y1="40.0" x2="676.0" y2="40.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="44.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">22.4</text>
<rect x="98.5" y="206.7" width="77.0" height="29.3" rx="4" fill="var(--kii-cat-1)"/>
<text x="137.0" y="198.7" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">3.35</text>
<text x="137.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">H100</text>
<text x="137.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">80GB HBM</text>
<rect x="252.5" y="166.0" width="77.0" height="70.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="291.0" y="158.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">8</text>
<text x="291.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">B200</text>
<text x="291.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">192GB HBM</text>
<rect x="406.5" y="166.0" width="77.0" height="70.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="445.0" y="158.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">8</text>
<text x="445.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">GB300</text>
<text x="445.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">288GB HBM</text>
<rect x="560.5" y="61.0" width="77.0" height="175.0" rx="4" fill="var(--kii-cat-3)"/>
<text x="599.0" y="53.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">20</text>
<text x="599.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">Vera Rubin</text>
<text x="599.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">288GB, capacity flat</text>
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="60" y="24" fill="var(--card-text-color-tertiary)" font-size="11.5">HBM bandwidth per GPU (TB/s). Rubin targets 22, early shipments reported near 20</text>
</svg>
</div>
<figcaption><strong>Compute jumps, capacity stalls.</strong> GB300 and Vera Rubin carry the same 288GB of HBM. The generational gain is bandwidth, and even that (about 2.75x) trails the compute gain (about 3.5x) over the same span.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| GPU | HBM capacity | Bandwidth |
|---|---|---|
| H100 | 80GB | 3.35TB/s |
| B200 | 192GB | about 8TB/s |
| GB300 | 288GB | about 8TB/s |
| Vera Rubin | 288GB | 22 targeted, about 20TB/s reported |

</details>
</figure>

The H100's HBM was 80GB at 3.35 terabytes per second. B200 moved to 192GB at 8 terabytes, and GB300 raised capacity to 288GB. But the next-generation Vera Rubin's HBM4 <strong>capacity stays at the same 288GB</strong>. What grew is bandwidth, targeted at 22 terabytes per second, with actual early shipments reported around 20 terabytes, roughly 2.75 times GB300. Over the same span, GPU compute performance grew about 3.5 times. [Fact: NVIDIA specifications, SemiAnalysis, reporting] The pattern of compute outpacing bandwidth keeps repeating generation after generation, and this is the substance of what is called the memory wall.

This gap shows up as real cost during inference. Inference splits into two stages. The prefill stage, which processes the entire prompt at once, is compute-intensive, so GPU compute performance is the bottleneck there. But the decode stage, which generates tokens one at a time, has to reread the model weights and the entire intermediate memory from memory at every single token, so <strong>the bottleneck becomes memory bandwidth rather than compute</strong>. During this stage the GPU sits idle for a good share of the time, waiting on memory. That is why buying more expensive chips does not raise throughput when HBM cannot keep up.

## 3. What Agents Change: Resident Memory

The second foundation is the change in workload. Unlike a chatbot that answers one question at a time, an agent searches the web, writes code, tests it, and fixes it, over stretches that run from tens of minutes to several hours. What the model maintains to remember everything up to that point is the KV cache, an intermediate memory, and this cache grows larger the longer the context, the longer the session runs, and the more agents run at once. A single agent's task splits into multiple model calls, for routing, search, tool selection, verification, and each call holds its own cache, so the memory resident at any one time grows to a different order of magnitude than in the chatbot era.

This shift already shows up in pricing. Field data puts the processing cost of a cached input token at one-tenth that of an uncached one, and operational data also shows that a single server's DRAM ceiling (typically 1 to 2 terabytes) makes it hard to hold a cache for more than an hour. The fact that NVIDIA launched a dedicated KV cache storage tier (CMX) as a separate product line this past January is itself evidence that the problem has grown large enough to become a hardware product. [Fact: industry data, NVIDIA announcement] TrendForce says the spread of agents is shifting the CPU-to-GPU ratio in servers, with enterprise agents consuming up to four times the tokens of before, and projects the global memory market at $1.28 trillion in 2027. [Fact: TrendForce, May 29]

An honest gap is worth noting too. No published quantitative estimate yet exists for exactly how many exabytes agent workloads add to HBM demand. [Blocked: no public estimate] The direction is clear, but the magnitude still belongs to narrative rather than data.

## 4. Why Only Three Suppliers: The Arithmetic of Supply

The third foundation is a structure in which supply is hard to expand. Three numbers summarize that structure.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="240.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">0%</text>
<line x1="60" y1="196.8" x2="676.0" y2="196.8" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="200.8" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">21%</text>
<line x1="60" y1="157.6" x2="676.0" y2="157.6" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="161.6" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">43%</text>
<line x1="60" y1="118.4" x2="676.0" y2="118.4" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="122.4" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">64%</text>
<line x1="60" y1="79.2" x2="676.0" y2="79.2" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="83.2" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">85%</text>
<line x1="60" y1="40.0" x2="676.0" y2="40.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="44.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">106%</text>
<rect x="111.3" y="61.0" width="102.7" height="175.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="162.7" y="53.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">95%</text>
<text x="162.7" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">Single die</text>
<text x="162.7" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">assume 95%</text>
<rect x="316.7" y="114.4" width="102.7" height="121.6" rx="4" fill="var(--kii-cat-3)"/>
<text x="368.0" y="106.4" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">66%</text>
<text x="368.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">8-high stack</text>
<text x="368.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">0.95 to the 8th</text>
<rect x="522.0" y="154.9" width="102.7" height="81.1" rx="4" fill="var(--kii-cat-4)"/>
<text x="573.3" y="146.9" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">44%</text>
<text x="573.3" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">16-high stack</text>
<text x="573.3" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">0.95 to the 16th</text>
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="60" y="24" fill="var(--card-text-color-tertiary)" font-size="11.5">Cumulative yield (%). Illustrative maths at 95% per-die yield</text>
</svg>
</div>
<figcaption><strong>The arithmetic of stacking.</strong> A 95% die yield becomes 66% at 8-high and 44% at 16-high, and one bad via among more than 8,000 kills the stack. This arithmetic is why only three firms produce at scale and why HBM eats three times the wafers per bit.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Configuration | Cumulative yield | Calculation |
|---|---|---|
| Single die | 95% | assumption |
| 8-high stack | about 66% | 0.95 to the 8th power |
| 16-high stack | about 44% | 0.95 to the 16th power |

</details>
</figure>

To produce the same capacity, HBM consumes roughly three times the wafers of ordinary server DRAM. This is because the dies are large, the through-silicon vias (TSVs) needed for stacking take up area, and yield losses compound. The arithmetic of yield is unforgiving. Even if a single die's yield is 95%, cumulative yield falls to 66% at 8 layers of stacking and 44% at 16 layers. A single bad via, out of the more than 8,000 through-silicon vias on one die, is enough to kill the entire stack. [Fact: industry technical data] This barrier is what turned HBM into a three-way oligopoly, and Omdia concluded that HBM is far more complex than standard DRAM, that only three companies can produce it at volume, and that the bottleneck will last at least through 2027. [Fact: Omdia, July 30]

A time barrier sits on top of that. A fab takes three to five years from groundbreaking to volume production, and lithography equipment alone has a lead time of a year to a year and a half. Qualification eats time too. It took Samsung Electronics's 12-layer HBM3E about 18 months to pass NVIDIA's qualification, and the Blackwell cycle had already passed by the time it did. [Fact: industry data] That is why capacity now under construction (SK Hynix's Cheongju M15X in mid-2027, Samsung's Pyeongtaek P5 in 2028) cannot contribute meaningful volume before 2028 at the earliest. TrendForce's supply-demand outlook points the same way. The DRAM fulfillment rate is -1% to -2% in 2026, the gap widens further in 2027, and meaningful new supply does not arrive until 2028. [Fact: TrendForce]

The result is what suppliers are saying right now. Micron's chief business officer said on August 10 that the company cannot fill even half of data center customer demand and that <strong>"2027 will be tighter than 2026"</strong>, and SK Hynix CEO Kwak Noh-jung described 2027, from a supply standpoint, as the tightest year in the industry's history. [Fact: TrendForce, press reporting] HBM's share of DRAM wafer input rises from 18% (end of 2025) to 30% (end of 2027), but on a bit basis that is only 8% to 13%. The three-times-the-wafers structure shows up here as well. [Fact: TrendForce]

That covers the core of the bottleneck claim: the gap in growth rates, resident memory, and the arithmetic of supply. All three are measured facts, and the tightness through 2027 looks less like a forecast and more like physics.

## 5. The Workarounds the Bottleneck Invites

But this claim has another half. The deeper the bottleneck grows, the bigger the reward for designs that route around it. Over the past month, evidence of that workaround has been piling up.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 326" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="132" y1="20" x2="132" y2="282" stroke="var(--kii-chart-axis)" stroke-width="1.5"/>
<text x="116" y="30" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">January</text>
<circle cx="132" cy="26" r="6" fill="var(--kii-cat-1)"/>
<circle cx="132" cy="26" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="30" fill="var(--card-text-color-main)" font-size="13" font-weight="600">NVIDIA announces CMX</text>
<text x="152" y="48" fill="var(--card-text-color-tertiary)" font-size="11.5">a dedicated KV-cache storage tier became a product</text>
<text x="116" y="84" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Roadmap</text>
<circle cx="132" cy="80" r="6" fill="var(--kii-cat-1)"/>
<circle cx="132" cy="80" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="84" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Rubin CPX uses GDDR7</text>
<text x="152" y="102" fill="var(--card-text-color-tertiary)" font-size="11.5">the prefill chip is designed without HBM</text>
<text x="116" y="138" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">28 July</text>
<circle cx="132" cy="134" r="6" fill="var(--kii-cat-3)"/>
<circle cx="132" cy="134" r="9" fill="none" stroke="var(--kii-cat-3)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="138" fill="var(--card-text-color-main)" font-size="13" font-weight="600">SOCAMM halving reported</text>
<text x="152" y="156" fill="var(--card-text-color-tertiary)" font-size="11.5">modules cut in half as memory neared 29% of system cost</text>
<text x="116" y="192" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">3 August</text>
<circle cx="132" cy="188" r="6" fill="var(--kii-cat-3)"/>
<circle cx="132" cy="188" r="9" fill="none" stroke="var(--kii-cat-3)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="192" fill="var(--card-text-color-main)" font-size="13" font-weight="600">High Bandwidth Flash spec released</text>
<text x="152" y="210" fill="var(--card-text-color-tertiary)" font-size="11.5">SanDisk and SK Hynix, with Google in the consortium</text>
<text x="116" y="246" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Early August</text>
<circle cx="132" cy="242" r="6" fill="var(--kii-cat-4)"/>
<circle cx="132" cy="242" r="9" fill="none" stroke="var(--kii-cat-4)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="246" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Rubin Ultra reported at 192GB</text>
<text x="152" y="264" fill="var(--card-text-color-tertiary)" font-size="11.5">a flagship whose HBM would shrink below its predecessor</text>
</svg>
</div>
<figcaption><strong>The workarounds accumulate.</strong> Five confirmed this year: a dedicated cache tier, a prefill chip without HBM, module capacity halved, a flash-based capacity tier, and a flagship whose HBM may shrink. Design changes induced by price do not reverse when price falls.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| When | Event | Nature |
|---|---|---|
| January | NVIDIA announces CMX | KV cache moved to a tier outside HBM |
| Roadmap | Rubin CPX adopts GDDR7 | HBM removed from prefill |
| 28 July | SOCAMM halving reported | CPU-side memory cut |
| 3 August | High Bandwidth Flash spec | a capacity tier below HBM |
| Early August | Rubin Ultra at 192GB reported | flagship HBM under review |

</details>
</figure>

The most significant signal comes from NVIDIA itself. After memory cost climbed to 29% of Vera Rubin system cost, above the company's preferred 20% ceiling, reports emerged that the CPU-side memory module (SOCAMM) would be cut in half, from 192GB to 96GB. CPU-side memory in a single rack falls from 55 terabytes to 28 terabytes. Supply allocation is part of the reason too: even combining all three suppliers, NVIDIA can only receive about 60% of estimated demand, so lowering the specification lets the company ship more systems from the same allocation. [Fact: TrendForce, July 28] Rubin Ultra went further. The specification originally announced as 1 terabyte of HBM4E has stepped down in stages, and reports now say the flagship configuration will be <strong>set at 192GB of HBM4, below even the current Rubin's 288GB</strong>. Memory content falling as the generation rises is a direction never before seen in a flagship. [Fact: reporting, unconfirmed by NVIDIA]

The workaround is not limited to cutting specifications. Rubin CPX, designed solely for the prefill stage, skips HBM entirely and uses GDDR7 instead. The design splits prefill, a compute bottleneck, from decode, a memory bottleneck, at the hardware level, so it does not pay HBM's price where HBM is not needed. High Bandwidth Flash (HBF), for which SanDisk and SK Hynix published a standard specification in early August, stacks NAND to deliver up to 512GB of capacity with bandwidth at the low end of the HBM class, and its consortium includes Google. It lays a cheaper capacity tier beneath HBM. On the software side, techniques that compress the KV cache itself have entered commercial models. The attention architecture used by the DeepSeek family cuts cache per token to one-third to one-fifth of the conventional approach. It is still concentrated in Chinese-origin models, but the direction is clear. [Fact: company announcements, technical literature]

The supplier's own words confirm this list. SK Hynix Chairman Chey Tae-won, in a CNBC interview last week, likened demand to a war but also said <strong>prices had risen too fast</strong>. The reason the largest beneficiary of the bottleneck worries about how deep it runs is exactly the list above. Once a workaround triggered by price gets designed in, it does not reverse even if prices come back down.

## 6. Where the Bottleneck's Rent Goes

If the bottleneck is real and the workarounds keep growing, the question left standing is who captures the bottleneck's profit, and in what form. The answer is increasingly the contract.

On the demand side, multi-year contracts lock in volume. Micron has tied up roughly half its revenue through contracts with 16 strategic customers running to around 2030, and reports keep describing the three suppliers' 2027 capacity as effectively fully allocated already. "Several-fold" increases in 2027 HBM contract prices are being discussed, though TrendForce's own wording is a qualitative description that does not specify a multiple, so reading more precision into it than that would be an overreach. [Fact: company data, TrendForce] On the pricing side, customization is changing the structure. Starting with HBM4, the base die moves to TSMC logic processes (mainly 12nm, with premium 5nm and next-generation 3nm), and as NVIDIA and Google each demand their own custom specifications, HBM is turning from a general-purpose component into a part incompatible across customers. A custom base die makes it hard for a customer to switch suppliers, while also locking the supplier to that customer. [Fact: industry data]

What this structure means matches the conclusion this series has been building toward. The bottleneck's rent is being <strong>fixed by the terms of multi-year contracts</strong> rather than a spike in spot prices. A fixed rent trims the upside in a boom in exchange for limiting the downside in a bust. The wide spread across institutions in HBM market size forecasts for 2027, from $116 billion to as much as 260 trillion won, is itself a feature of this transition, which makes the share of contract coverage a better thing to watch than any single figure. [Fact: various institutions, wide dispersion]

## 7. The Implication for Korea: 2027's Physics, 2028's Calendar

Here is what this verification means for Korean memory makers.

Ownership of the bottleneck is Korea's position. Two of the three companies capable of volume production are Korean, and SK Hynix's HBM share runs from the mid-50s to high-50s percent depending on the source. Some tallies put SK Hynix at roughly 70% of NVIDIA's next-platform initial HBM4 volume. [Fact: reporting, share varies by source] Profit visibility through 2027 is backed by the physics laid out above. Because of lead times, 2027 supply is already determined at this very moment, and a substantial share of that volume is already sold under contract.

What remains open is 2028. New fabs begin contributing volume that year (Cheongju M15X, Pyeongtaek P5). CXMT's HBM capacity, if it stays on plan, also climbs to a scale of 100,000 wafers that year, though still carrying a roughly 25% yield and a customer base limited to domestic Chinese buyers. That is also when the effects of the workaround technologies described above accumulate enough to matter. [Fact: company data, SemiAnalysis] The bottleneck claim is a matter of physics through 2027, but from 2028 on it reverts to a question of supply discipline and contract terms. The conclusion this series reached in early August, that the investment question is not whether prices rise further but whether they hold, and that holding is most solid when a contract guarantees it, survives intact even after passing through the physics of the bottleneck.

One last sentence, carried over directly from the Morgan Stanley report: "Infrastructure comes first. The applications that will justify that build-out are not yet visible." Even the strongest supporter of the bottleneck claim attached this qualifier. A bottleneck produces rent only when demand is real. This earnings season showed demand measured in fact, and its persistence gets re-verified every quarter.

---

The stocks mentioned in this piece are illustrative examples for analysis and do not constitute a recommendation to buy or sell any particular stock. Responsibility for investment decisions and their outcomes rests with the investor. The figure of roughly 50 billion Gb in 2027 HBM demand is an estimate from Kiwoom Securities and Korean research aggregation, not a figure from the Morgan Stanley document, and the back-calculated share of total DRAM is our own computation. GPU specifications and bandwidth combine announced targets with reported figures and may differ from actual shipped specifications. Yield figures are example calculations drawn from industry technical data, and actual yields are not disclosed by company. The Rubin Ultra specification adjustment and the SOCAMM reduction come from research firms and press reporting and have not been confirmed by NVIDIA. Forecasts of HBM market size vary widely across institutions. The contribution of agent workloads to HBM demand has no published quantitative estimate, so only the direction is described. Prices and outlooks are as of mid-August 2026.

### Related Posts

- [The Second Week of August in Review: AI Capital Moves to Wall Street, and Good News Starts Lasting Two Days](/post/weekly-wrap-wallst-financing-reaction-shift-2026-08-14/)
- [Memory No Longer Needs Prices to Rise Further: Anatomy of the August 3 Plunge and the Contract Price Deceleration](/post/memory-price-deceleration-p-holds-thesis-2026-08-03/)
- [What Hyperscaler Earnings Proved, and What They Didn't: Three Explanations for the Memory Sell-Off](/post/hyperscaler-proof-memory-selling-three-hypotheses-2026-08-04/)
- [July Earnings Season Wrap: AI Demand Was Confirmed, and Memory Pricing Became an Industry-Wide Cost](/post/july-2026-earnings-two-listings-kimi-four-worries-2026-07-31/)
