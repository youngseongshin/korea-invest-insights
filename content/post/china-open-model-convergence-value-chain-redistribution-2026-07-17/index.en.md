---
title: "What China's Open-Model Convergence Actually Changes: Value-Chain Redistribution, Not Demand Collapse"
slug: "china-open-model-convergence-value-chain-redistribution-2026-07-17"
date: 2026-07-17T22:00:00+09:00
description: "Chinese open models are converging on US frontier performance while being served on domestic Chinese inference infrastructure. This is value-chain redistribution rather than an AI demand collapse. The monopoly value of model APIs and leading-edge GPUs falls, while cheaper inference lifts token volume and can raise the value of memory, storage, networking, power and cloud distribution. This post maps how US AI policy and US-China tension reshape that reading, and whether Chinese model APIs can be adopted by Western enterprises."
categories: ["Exclusive Analysis", "AI Infrastructure", "Market-Outlook"]
tags:
  - "China Open Models"
  - "DeepSeek"
  - "Kimi K3"
  - "Qwen"
  - "CXMT"
  - "HBM"
  - "Samsung Electronics"
  - "SK Hynix"
  - "Micron"
  - "NVIDIA"
  - "AI Policy"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Context
> This piece is a follow-up to [Kimi K3 Resets the AI Price Curve](/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/). Where that piece verified the pricing and architecture of <strong>a single model</strong>, this one expands the lens to how <strong>the entire Chinese open-model ecosystem</strong> redistributes the semiconductor and Big Tech value chain, and how US policy and US-China tension reshape that reading. It pairs well with [The Real Debate in Semiconductors](/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/), [Are Semiconductors Cyclical, and What Is Fair Value?](/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/), and [CXMT IPO And Memory Price Risk](/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/). Related hubs are the [AI HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/) and the [Exclusive Analysis Hub](/page/exclusive-analysis-hub/).

## TL;DR

* Chinese open models converging in performance looks more like <strong>value-chain redistribution than an AI demand collapse</strong>. The monopoly value of model APIs and leading-edge GPUs falls, while cheaper inference lifts usage and can raise the value of memory, storage, networking, power, and cloud distribution.
* Relative preference splits this way. Within Korean memory, <strong>Samsung Electronics > SK Hynix</strong>; within US semiconductors, <strong>Micron and SanDisk > NVIDIA</strong>; within Big Tech, <strong>Meta and Amazon > Google and Microsoft > pure model vendors</strong>. \[Inference: relative judgment\]
* Chinese open models have proven <strong>falling compute and memory cost per unit of intelligence</strong>. They have not proven <strong>a decline in total silicon spend</strong>. TSMC, if anything, raised its 2026 capex from $52 billion-$56 billion to $60 billion-$64 billion.
* In HBM, CXMT trails the leading three by <strong>1.5 to 2 product generations</strong> and by a 2- to 3-year commercialization gap. The 2028 threat is therefore a <strong>conditional option</strong>, not a present-day supply shock.
* The <strong>technical diffusion</strong> of Chinese models and the <strong>revenue diffusion</strong> of Chinese API vendors are two different things. The most realistic path is rehosting Chinese models on AWS, Azure, or enterprise VPCs and selling them through Western security and contracting frameworks. \[Analysis scope\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Key Framing</div>
  <div class="thesis-callout__body">
    Chinese models can shake the pricing of US models, but they do not immediately collapse demand for AWS, Azure, US chips, or Korean memory. The direct casualty is the margin of closed-model APIs. What survives longest is usage-based infrastructure: the cloud distribution and security layer, along with memory, networking, and power.
  </div>
</div>

---

## 1. Getting the Facts Straight First

The ecosystem direction is real, but <strong>not every new model has disclosed its training hardware</strong>. That distinction matters.

DeepSeek-V3 was trained on <strong>2,048 NVIDIA H800 GPUs</strong> using 2.788 million GPU-hours. \[Fact: DeepSeek V3 technical report\] The H800 is export-restricted, but it is not a cheap consumer GPU. Kimi K3, by contrast, has disclosed 2.8 trillion parameters, a 1M-token context window, and 2.5x higher scaling efficiency versus K2, but <strong>the full technical report and training hardware are scheduled for release on July 27</strong>. \[Fact: Kimi official announcement\]

So the claim that "Kimi K3 was also trained on cheap NVIDIA GPUs" cannot yet be confirmed. \[Blocked\]

### The Efficiency Gains Are Real

DeepSeek V4-Pro <strong>activates only 49 billion</strong> of its 1.6 trillion parameters. At the 1M-token range, per-token compute is <strong>27%</strong> and KV cache is <strong>10%</strong> of V3.2's levels. \[Fact: DeepSeek V4 model card\] That is direct evidence that GPU and HBM use per token can fall sharply while performance holds.

### But So Is the Other Side

Huawei's CloudMatrix384 pools 384 Ascend 910C chips to serve DeepSeek-R1. By JPMAM's tally, CloudMatrix uses 49TB of HBM and 599kW of power, versus 21TB and 145kW for the comparison system, GB300 NVL72. \[Fact: CloudMatrix paper, JPMAM comparison\]

It is not an apples-to-apples performance comparison, but the direction is clear: China compensates for a weaker single chip with <strong>more chips, more memory, and more power</strong>. A cheaper individual chip does not necessarily mean less total silicon, networking, or power. \[Inference: structural reading\]

---

## 2. The Core Equation: What to Actually Watch

The answer to this debate is not in benchmark scores. It is in two equations.

```text
Total compute demand = total tokens × compute per token

Total memory demand = total tokens × memory use per token
                     + model, KV, and retrieval data storage
```

If open models cut token prices 70% and usage rises 5x, <strong>total demand increases</strong> even after the efficiency gain. Conversely, if usage merely doubles while per-token HBM falls 70%, <strong>HBM demand declines</strong>.

So the indicator to watch going forward compresses into one question: <strong>by how much does the token growth rate outpace the decline rate in memory per token?</strong>

### The Verdict So Far

Total spend is determined by the following equation.

```text
Total silicon spend = number of training runs × cost per run
                     + inference tokens × cost per token
```

On its 2Q26 call, TSMC raised its 2026 capex from $52 billion-$56 billion to <strong>$60 billion-$64 billion</strong>. Microsoft, too, raised inference throughput 40%, yet large-customer token use still rose <strong>30% quarter-over-quarter</strong>, and it held roughly $190 billion in 2026 capex. \[Fact: TSMC 2Q26 call, Microsoft FY26 Q3 call\]

<strong>So far, usage growth is beating efficiency gains.</strong> \[Inference: data synthesis\]

---

## 3. Semiconductor Impact: It Diverges by Stock

| Stock / Group | Stock-Price Impact | Key Interpretation |
|---|---|---|
| Samsung Electronics | Positive | Broadest beneficiary, capturing not just HBM but server DRAM, NAND/eSSD, and general-purpose memory |
| SK Hynix | Mixed-to-positive | Token growth helps, but MoE and KV compression cut HBM per token, pressuring the scarcity multiple |
| Micron | Positive | Combined DRAM, HBM, and NAND exposure across the US supply chain; broad-memory upside similar to Samsung |
| SanDisk | Positive | Local deployment, model weights, and growing RAG/cache use flow into eSSD and NAND demand |
| NVIDIA | Negative near-term, mixed long-term | China share and top-tier GPU monopoly value decline; offset by rising total tokens and H200 shipments |
| AMD | Relatively positive | Open models make it easier to migrate across heterogeneous hardware; ROCm and actual serving share are the key variables |
| Broadcom / Marvell / Arista | Positive medium-term | Rising demand for Western custom ASICs, Ethernet, optical, and SerDes |
| TSMC | Neutral-to-positive | Training-chip demand from NVIDIA, AMD, and ASICs holds, but Chinese inference shifts to Ascend and SMIC |

### Why Samsung Has the Relative Edge Over Hynix

Among the same three memory makers, <strong>Samsung Electronics and SK Hynix diverge in direction</strong>. Cheap inference and open-model diffusion do not just lift HBM; they raise the total volume of server DRAM, NAND, and general-purpose memory. Samsung Electronics, with its broader exposure, captures more of that diffusion.

MoE and KV compression, conversely, reduce <strong>HBM per token</strong>. Hynix, with its concentrated HBM exposure, receives both the benefit of rising tokens and the burden of falling HBM per token at the same time. It is a structure where the <strong>scarcity multiple</strong>, not absolute demand, comes under pressure first. \[Inference: exposure structure analysis\]

Samsung Electronics does carry an offsetting risk, however: it is the first to be exposed to CXMT's ramp-up of general-purpose DRAM output.

### NVIDIA and H200

The US recently began shipping limited volumes of H200 to China, but the quantity is still small. It is positive for NVIDIA's near-term revenue, but not enough to reverse the shift toward Huawei-centered domestic infrastructure. \[Fact: July 2026 Reuters reporting\] \[Inference: impact judgment\]

---

## 4. Big Tech Impact

| Company | Verdict | Reason |
|---|---|---|
| Meta | Most positive | Open-ecosystem strategy is validated, and AI returns are captured through advertising and recommendation rather than APIs |
| Amazon | Positive | Sells AWS inference, storage, and networking regardless of which model wins |
| Google | Mixed-to-positive | TPU and cloud benefit, but Gemini API price premium comes under pressure |
| Microsoft | Mixed | Azure usage rises, but OpenAI model rent and capex payback are pressured |
| Apple | Positive | Cheaper small and open models lower on-device and Private Cloud costs |
| OpenAI / Anthropic | Negative | Shrinking performance gap and API price premium pressure high valuations and fundraising |

<strong>Contrary to a common misconception, Meta is not the biggest casualty.</strong> It makes money from advertising and recommendation rather than model sales, and it uses open models to cut costs, so it stands to relatively benefit. The burden falls instead on capex and depreciation. \[Inference: business model analysis\]

### The Lesson from the 2025 DeepSeek Shock

During the 2025 DeepSeek shock, NVIDIA lost <strong>17% and roughly $593 billion</strong> in market capitalization in a single day. The initial reaction was a broad sell-off across GPUs, power, and data-center infrastructure, but it partly rebounded soon after. \[Fact: 2025 market reporting\]

This time, too, <strong>near-term stock prices are likely to react to efficiency fears, while medium-term earnings react to rising usage</strong>. \[Inference: historical pattern\]

---

## 5. Verdicts on the Chinese Open-Model Thesis

Judging the claims coming from both the bull and bear sides, one by one, looks like this.

| Claim | Verdict |
|---|---|
| Frontier performance requires top-tier GPUs | Weakened, but not disproven |
| AI intelligence is a scarce resource | Largely collapsed at the level of raw model and token pricing |
| Capital scale is the moat | The pretraining moat weakens; the moat shifts to deployment, data, power, and distribution |
| Open source has zero marginal cost | Only the weight price approaches zero; inference cost is ongoing |
| A $1 billion training run has overtaken $100 billion of investment | An inaccurate claim comparing two different cost categories |

The last item is especially often misused. Training cost and total infrastructure investment are not comparable categories.

---

## 6. How Far Has CXMT's HBM Actually Gotten

This is the part of the China-threat discussion that gets exaggerated most often. Breaking it down gate by gate reveals the reality.

| Gate | Current Verdict | Basis for Judgment |
|---|---|---|
| DRAM cell process | Commercialized, improving fast | Selling DDR5 and LPDDR5X; Apple is also testing DRAM for China-market products |
| TSV stacking | Small-volume HBM2, early HBM3 | HBM2 production has been reported, but volume and yield are undisclosed |
| Packaging and base die | Under construction | The domestic ecosystem is forming, but mass-production yield, thermal, and reliability data are absent |
| Customer qualification | HBM unconfirmed | The Tencent contract and Apple testing are evidence of general DRAM capability, not HBM |
| Distance from the leaders | 1.5-2 generations | The leading three are ramping HBM4; CXMT has not even verified HBM3 mass production |

As of July 17, 2026, CXMT's official published product lineup includes only DDR5, LPDDR5/5X, DDR4, and LPDDR4X, and <strong>no HBM</strong>. TrendForce likewise classifies CXMT's HBM3 as still in early verification, and assesses that technical barriers and domestic-equipment requirements are delaying mass production. \[Fact: CXMT official materials, TrendForce\]

Capacity estimates also diverge. A plateau near 240,000 wafers per month conflicts with a year-end forecast of 350,000, and because the 350,000 figure comes from a private model rather than company guidance, it is hard to treat as a confirmed number. \[Blocked\]

### How the Legacy-DRAM Hypothesis Needs to Be Revised

- <strong>2026-2027</strong>: CXMT's HBM investment <strong>delays</strong> the easing of Chinese legacy-DRAM supply.
- <strong>2028</strong>: If HBM3/3E secures Chinese accelerator customer qualification and meaningful volume, it could begin displacing the older-generation HBM market within China first.
- <strong>2029 and beyond</strong>: Only once HBM4, base die, and packaging yield catch up does it directly pressure the global leading market and Hynix's margins.

In other words, rather than "CXMT is making legacy supply tighter right now," the more valid framing is <strong>"CXMT is not freeing up as much legacy supply as expected."</strong> \[Inference: stage-by-stage judgment\]

---

## 7. How US Policy Reshapes This Reading

The US is treating AI less as a commercial technology and more as <strong>core infrastructure for the allied bloc</strong>. That is why a purely technical analysis cannot supply the full answer.

The US AI Action Plan and Executive Order 14320 state explicitly that the US intends to export a <strong>full-stack American AI system</strong>, bundling hardware, cloud, networking, models, and applications, to allied nations, while reducing technological dependence on adversary nations. Even if a Chinese model is superior on performance and price, the US stack retains a policy advantage in allied-nation government procurement and critical industries. \[Fact: White House AI Action Plan, EO 14320\]

### Yet This Is Not a Full Decoupling

In January 2026, the US BIS moved to review H200 and MI325X exports to China case by case, under approved-customer and security conditions. It is a compromise that keeps China partly inside the US chip ecosystem while retaining control. \[Fact: BIS 2026-01-13\]

Nor is the use of Chinese models by US private companies fully banned. The `No DeepSeek on Government Devices Act` is still only at the bill-introduction stage. Australia's government, however, has ordered DeepSeek removed from government systems, and Italy's privacy authority has restricted processing of user data. \[Fact: official actions by country\]

<strong>De facto bans from procurement and security departments are likely to take effect before legislation does.</strong> \[Inference: policy sequencing\]

---

## 8. Can Western Enterprises Actually Use Chinese Model APIs?

Diffusion potential differs completely by pathway. This table is the answer to the question.

| Adoption Method | Diffusion Potential | Judgment |
|---|---|---|
| Direct calls to mainland China-hosted APIs | Low | Data, jurisdiction, and procurement risk |
| Qwen's US, EU, Japan, and Singapore APIs | Medium | Data localization is possible, but Chinese-vendor risk remains |
| Chinese models rehosted by AWS or Azure | Medium-high to high | Western cloud providers hold the contracting, security, and data control |
| Enterprise VPC or on-premises open weights | High | No need to send data to Chinese servers |
| Government, defense, and critical infrastructure | Very low | Procurement restrictions can extend even to model lineage |

The most realistic pathway looks like this.

```text
Chinese model developed
→ Rehosted on AWS, Azure, or enterprise VPC
→ Sold through Western security, contracting, and audit frameworks
```

In other words, <strong>the technical diffusion of Chinese models and the revenue diffusion of Chinese API vendors are separate matters</strong>. \[Inference: pathway analysis\]

### The Limits of Direct APIs

DeepSeek's Privacy Policy states that it <strong>collects, processes, and stores personal data, including input data, directly in China</strong>, and may use it to improve its service and models. \[Fact: DeepSeek Privacy Policy\] That is a disqualifying condition for companies handling source code, customer information, healthcare or financial data, or export-controlled technology.

Qwen is somewhat different. Alibaba Cloud Model Studio offers US, German, Japanese, and Singapore regions, can restrict data and inference to a specific region, and states explicitly that it does not use customer data for model training. \[Fact: Alibaba Cloud region and security policy\] Direct API adoption could therefore grow in non-regulated industries and in Southeast Asia, the Middle East, and Latin America.

Data localization and SOC 2, however, do not eliminate <strong>the risk of service disruption, sanctions, or procurement exposure arising from US-China tension</strong>. \[Inference: residual risk\]

---

## 9. Revising the Thesis: What Changes and What Stays

<strong>First, the case for a US hyperscaler collapse weakens.</strong> AWS and Azure directly host DeepSeek, providing data isolation, SLAs, and security assessments. US clouds can absorb the cost innovation of Chinese models and turn it into revenue. \[Fact: AWS and Azure official announcements\]

<strong>Second, pricing pressure hits closed-model APIs first.</strong> It burdens the token prices and margins of OpenAI, Anthropic, and Google, but inference volume and AWS/Azure usage can still rise. It is relatively favorable for Meta's open-model strategy.

<strong>Third, the US-China split supports total infrastructure investment.</strong> Both blocs build out <strong>duplicate</strong> accelerators, memory, networking, and power grids. That lowers the likelihood that efficiency gains translate directly into a decline in global silicon spend.

<strong>Fourth, SK Hynix's HBM premium can persist longer within the allied bloc.</strong> CXMT's HBM is more likely to penetrate Chinese accelerators and Chinese data centers first. Adoption by Western CSPs requires policy and supply-chain certification on top of technical qualification. That said, export controls accelerate China's push for self-sufficiency, which is a risk to Hynix's China-market share from 2028 onward.

<strong>Fifth, Samsung Electronics is a relative hedge.</strong> Cheap inference and open-model diffusion can raise the total volume of server DRAM, NAND, and general-purpose memory, not just HBM. On the other side is the risk of being first exposed to CXMT's ramp-up of general-purpose DRAM output.

---

## 10. The Order of Casualties and Beneficiaries

1. <strong>Greatest casualty</strong>: the excess profit of closed-model APIs, and highly leveraged GPU-leasing operators
2. <strong>Intermediate risk</strong>: heavily front-invested, customer-concentrated operators such as Oracle
3. <strong>Meta</strong>: not the biggest casualty. It uses open models to cut costs, so relative benefit is possible. The burden falls on capex and depreciation
4. <strong>NVIDIA</strong>: the multiple and product mix come under pressure before near-term EPS does. Displacement inside China is a risk, but the CUDA, networking, power-efficiency, and development-timeline moats remain
5. <strong>Memory</strong>: the base case is not a decline in absolute HBM demand, but <strong>a narrowing HBM scarcity premium plus tier expansion into DDR/CXL/eSSD</strong>

---

## 11. Scenario Update

It makes sense to provisionally revise the probabilities used in [Are Semiconductors Cyclical, and What Is Fair Value?](/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)

| Scenario | Prior | Revised |
|---|---:|---:|
| Excess demand persists | 30% | 30% |
| Asset re-concentration | 40% | 40% |
| Supply/efficiency normalization | 20% | <strong>25%</strong> |
| System demand short-circuit | 10% | <strong>5%</strong> |

Chinese model performance <strong>lowers the probability that AI demand itself disappears</strong> (the short-circuit scenario, from 10% to 5%). In exchange, efficiency gains and Chinese-made hardware lower the scarcity premium of NVIDIA and HBM (the normalization scenario, from 20% to 25%).

The timeline scenarios also hold: usage beats efficiency through 2027 at 70%, mix and pricing normalize from 2028 onward at 25%, and total capex contracts at 5%. However, <strong>the driver of the 70% scenario shifts from a single global ecosystem to dual investment across the US bloc and the China bloc.</strong> \[Inference: scenario recalibration\]

---

## 12. What Would Change This Judgment

- <strong>The Kimi K3 technical report (July 27)</strong>: once training hardware is disclosed, the truth of the "frontier training on cheap GPUs" claim will be settled
- <strong>Token growth rate versus the decline rate in memory per token</strong>: the gap between these two values is the real answer to this debate
- <strong>CXMT's HBM3E mass-production qualification and actual packaging volume</strong>: if confirmed, both Hynix's 2028 EPS and its multiple need to come down together
- <strong>Slowing HBM pricing and content growth</strong>: the first signal of a narrowing scarcity premium
- <strong>Expanding rehosting of Chinese models by Western CSPs</strong>: evidence that cloud-distribution value is rising
- <strong>Actual enforcement of US procurement and security regulation</strong>: the scope of the de facto ban that operates ahead of legislation

This is not the stage to conflate <strong>terminal risk with current-period earnings</strong>. Hynix's 2028-and-beyond outlook can be adjusted once CXMT's HBM3E mass-production qualification is confirmed. \[Inference: sequencing of judgment\]

---

## Closing

Returning to the question, the answer is this.

It is a fact that Chinese open models are converging on the US frontier, and it is a fact that cost per unit of intelligence has fallen sharply. But that does not mean total silicon spend is declining. TSMC's capex increase and Microsoft's 30% rise in tokens are the answer so far.

US policy substantially reshapes this reading. The US-China split produces <strong>duplicate investment</strong> across both blocs, supporting total infrastructure demand, and within the allied bloc, it protects the position of the US stack and Korean memory by policy.

Western enterprise adoption of Chinese model APIs must be viewed by <strong>separating the model from the vendor</strong>. The technology spreads as open weight, but the party selling it is more likely to be AWS, Azure, and enterprise VPCs than the Chinese API vendors themselves.

So the conclusion is redistribution. What collapses is the excess profit of closed-model APIs. What remains is usage-based infrastructure.

---

_This post synthesizes public papers (DeepSeek V3/V4, Huawei CloudMatrix384), official company announcements (Kimi, the TSMC 2Q26 call, the Microsoft FY26 Q3 call, CXMT, Alibaba Cloud, DeepSeek's Privacy Policy), US government materials (the AI Action Plan, EO 14320, BIS), regulatory actions by various countries, and market research (TrendForce, JPMAM). Kimi K3's training hardware remains unconfirmed until its technical report is released on July 27, and CXMT's capacity estimates and the scenario probabilities are author estimates as of the time of writing, not company guidance. The stocks mentioned are examples used to illustrate value-chain structure and are not a recommendation to buy or sell any specific security. Investment decisions and responsibility for them rest with the individual investor._

---

### Related Posts

- [Kimi K3 Resets the AI Price Curve: From Kimi Linear to HBM and Big Tech Strategy](/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/)
- [Are Semiconductors Cyclical, and What Is Fair Value? Pricing Samsung, SK Hynix and Micron with FCFE and Normalized Earnings](/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [The Real Debate in Semiconductors: Four Physical Clocks and One Stock-Price Clock](/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [CXMT IPO And Memory Price Risk: HBM Is Not The First Place To Break](/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)
- [HBM 2030 Supply-Demand Deep Research: Dissecting the 26.7EB Demand Model Against the Capacity Schedule](/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
