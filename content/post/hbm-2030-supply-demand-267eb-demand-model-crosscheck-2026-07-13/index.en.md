---
title: "HBM 2030 Supply-Demand Deep Research: Dissecting the 26.7EB Demand Model Against the Capacity Schedule"
slug: "hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13"
date: 2026-07-13T11:00:00+09:00
description: "We independently reproduce the 2030 HBM claim of 26.7EB demand versus 10.6EB supply (a 2.5x shortage) from the published formula, then cross-check it against Goldman's 24x token forecast, DeepSeek MLA and TurboQuant efficiency counter-evidence, and the Big 3 capacity schedule. The conclusion separates direction from magnitude: tight through 2027 and supply relief from 2028 are supported by data, but a precise 2.5x shortage in 2030 is a bull scenario requiring many demand assumptions to hold at once. This is supply-demand structure analysis, not investment advice."
categories: ["Exclusive Analysis", "Tech-Analysis", "Market-Outlook"]
tags:
  - "HBM"
  - "Memory Supply-Demand"
  - "AI Memory"
  - "SK Hynix"
  - "Samsung Electronics"
  - "Micron"
  - "KV Cache"
  - "AI Infrastructure"
  - "Semiconductor Capacity"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Context
> If [HBM, HBF, and HBC: A Memory Technology Comparison](/post/hbm-hbf-hbc-ai-memory-comparison-2026-06-22/) covered what these technologies are, this piece is a deep dive into <strong>how demand and supply for that technology converge by 2030</strong>. It pairs well with [AI Token Value and Memory's Value-Add](/post/ai-token-value-memory-value-added-2026-07-09/), [Late-July Big Tech Earnings Calls and the Memory Thesis](/post/big-tech-july-earnings-call-memory-thesis-scenarios-2026-07-07/), and [Who Pays for the 2027 Semiconductor Consensus](/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/). Related hubs: the [AI HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/) and the [Exclusive Analysis Hub](/page/exclusive-analysis-hub/).

## TL;DR

* We independently reproduced, using the published formula, the narrative circulating in the market that <strong>2030 HBM demand will reach 26.7EB against supply of 10.6EB, a 2.5x shortage</strong>. The arithmetic itself reproduces cleanly. The question is what assumptions that number rests on.
* 26.7EB is not the product of a stock-versus-flow error. Both demand and supply are converted into <strong>installed and running HBM stock</strong> before being compared. That said, the figure only emerges if several bullish assumptions all hold simultaneously: a 24x increase in tokens, a 5x model footprint, a 4x context multiplier, and a 70% KV retention rate.
* We cross-checked the claim through three lenses: (1) the structure of the demand model, (2) the bullish evidence behind the demand assumptions together with the technical-efficiency counter-evidence, and (3) the Big 3 capacity expansion schedule. All three lenses converge on <strong>one consistent conclusion</strong>.
* The conclusion <strong>separates direction from magnitude</strong>. `Tight through 2027` is high-confidence, `supply improving from 2028` is consistent with the official expansion schedules, and `a precise 2.5x shortage still in 2030` is a bull-skewed scenario.
* This piece does not make a buy or hold call on any specific stock. It dissects the supply-demand structure of the industry. \[Analysis scope\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Key Framing</div>
  <div class="thesis-callout__body">
    The real question in HBM supply-demand is not whether 2030 brings a 2.5x shortage, but whether the direction of that shortage is robust even though its magnitude is sensitive to assumptions. Tightness through 2027 and supply improvement starting in 2028 are supported by the data. The 2.5x figure is a bull scenario that only holds if several demand assumptions align at once.
  </div>
</div>

---

## 1. Framing the Question: What This Deep Research Verifies

A powerful narrative is circulating in the AI memory market: that 2030 HBM demand will reach 26.7EB (exabytes) while supply tops out at 10.6EB, leaving a <strong>structural shortage of roughly 2.5x</strong>. The figure originated from an independent analytical model (Memory Analyst) and spread widely through YouTube videos and research notes.

This deep research answers four questions. \[Verification\]

1. Is the `26.7EB versus 10.6EB` formula internally consistent?
2. Are the demand assumptions justified by public evidence and by the model's own structure?
3. Does a shortage still remain in 2030 once Samsung Electronics, SK Hynix, and Micron's capacity expansions are factored in?
4. How does the market actually clear this number in practice?

To keep the conclusion from getting blurred, one thing should be nailed down first: this piece does not recompute current share prices or fair-value multiples. It addresses only <strong>the reliability of supply-demand's direction and magnitude</strong>.

---

## 2. First Lens: Dissecting the 26.7EB Demand Model

### 2.1 A Stock-to-Stock Comparison (Clearing Up a Common Misconception)

The first misconception to clear away is the claim that "26.7EB of demand versus 10.6EB of supply wrongly compares annual consumption to annual production." Verification shows <strong>this is not an error.</strong> The original model compares two stock measures. \[Fact\]

- <strong>Need</strong>: the HBM stock that must be installed and powered on to handle that year's AI inference workload
- <strong>Serving fleet</strong>: the stock of HBM produced over roughly the trailing five years that has been allocated to inference, adjusted for aging efficiency, and has not yet been retired

In other words, both figures are stocks, not flows. The original model's structure, `fleet = trailing ~5-year output × inference share - friction`, makes this conversion explicit. On a stock-flow basis, it is internally consistent. \[Inference\] That said, the inference allocation ratio, the five-year lifespan, and the generation-by-generation efficiency used to convert flow into stock are not independently verified industry standards. They are <strong>model assumptions</strong>.

### 2.2 Reproducing the 26.7EB Demand Formula As-Is

We independently reproduced the calculation by plugging the original model's published simplified formula and its 2030 base-case inputs directly in.

```text
traffic = 24  (24x versus 2026, monthly tokens of 120 quadrillion)
replicaIndex = 24^0.90 / 11 = 1.5878

weights = 1.75 × 1.5878 × 5 / 1.75 = 7.939EB
contextBucket = 4 × 1.5 / 4 × 0.70 = 1.05
kv = 1.27 × 24^0.55 × 1.05 = 7.658EB
scratch = (7.939 + 7.658) × 0.15 = 2.340EB

need = (7.939 + 7.658 + 2.340) × 1.10 / 0.74 = 26.66EB ≈ 26.7EB
```

Breaking demand down by component:

| 2030 Demand Component | EB | Share |
|---|---:|---:|
| Resident weights | 7.94 | 44.3% |
| KV cache | 7.66 | 42.7% |
| Scratch (temporary working memory) | 2.34 | 13.0% |
| Subtotal (before redundancy/utilization) | 17.94 | 100.0% |
| Final installed requirement (×1.10 / 0.74) | 26.66 | - |

\[Fact\] The 26.7EB arithmetic reproduces cleanly from the published formula. What matters is that resident weights and KV cache account for 44% and 43% of demand respectively, together making up the bulk of the total. These are precisely the two line items that later become the direct targets of technical efficiency gains.

\[Blocked\] However, the calculator includes a separate input, `frontier/HBM-served share 70%`, and it is not clear from the published simplified formula how this value feeds into the weights calculation. Until a code-level audit is possible, we do not certify 26.7EB as a fully independent, verified model.

### 2.3 Reading the Growth Rate Correctly

The `5-year CAGR` commonly cited elsewhere is a period-counting error. From 2026 to 2030 there are five data points, but <strong>only four compounding periods</strong>.

| Item | 2026 | 2030 | Multiple | Correct 4-Period CAGR |
|---|---:|---:|---:|---:|
| Installed HBM requirement | 4.8EB | 26.7EB | 5.56x | <strong>53.6%</strong> |
| Serving fleet | 3.75EB | 10.6EB | 2.83x | <strong>29.7%</strong> |

Also, the original model's annual HBM output path, `from 2.8EB in 2024 to 7.6EB in 2030`, implies a 6-period CAGR of <strong>18.1%</strong>. The `10.6EB serving fleet` is not annual output. It is a stock that accumulates and depreciates multiple years of production, so the two figures should not be conflated. \[Fact\]

If demand is growing at 53.6% a year while the supply stock grows at 29.7% a year, the direction in which the gap widens is arithmetically self-evident. The question is how robust the input assumptions behind these two growth rates really are.

---

## 3. Second Lens: Upside Evidence and Counter-Evidence for the Demand Assumptions

### 3.1 Confirmed Upside Evidence for Demand

Real evidence supports strong demand. \[Fact\]

- Goldman Sachs Research projected that monthly token consumption would grow <strong>24x</strong> between 2026 and 2030, reaching 120 quadrillion.
- The same report expects daily LLM queries to grow at roughly 40% annually, reaching 11 billion per day by 2030.
- HBM capacity per accelerator has increased with each successive NVIDIA generation.
- As of June 2026, Micron guided that DRAM and NAND demand would substantially exceed supply, with tightness <strong>persisting into 2027 and beyond</strong>.
- Micron disclosed 16 Strategic Customer Agreements (SCAs), with the minimum-price-based cumulative revenue across 14 of those agreements at roughly $100 billion and related cash deposits and financing commitments at $22 billion. Note that HBM is only part of these agreements; not all of it is HBM-specific.

### 3.2 Counter-Evidence Within the Same Source

Interestingly, the very same Goldman report used as bullish evidence also contains counter-evidence. \[Fact\]

- Goldman anticipates a near-term chip shortage but explicitly states that <strong>once new capacity comes online, the industry could catch up within about two years</strong>.
- Goldman explains that the cost per inference token is falling 60-70% annually. Lower prices boost usage, but they also reduce the physical memory burden of the same workload.
- Crucially, Goldman's 24x figure is a forecast of <strong>token traffic</strong>, not of HBM bit demand. Every step of the conversion from `tokens to concurrent sessions, to context, to KV and weights, to HBM residency` is a separate, independent model assumption.

\[Inference\] The Goldman forecast therefore supports rising AI usage, but it does not directly support a `2.5x HBM shortage in 2030`. This distinction is frequently dropped when the bull narrative cites Goldman.

### 3.3 Model-Structure and Efficiency Counter-Evidence

Weights and KV cache, the core of the demand formula, are the direct targets of technical improvement. \[Fact\]

- The original model's example of `roughly 504KB per token` of KV cache comes from <strong>Llama 3.1 405B</strong>. It is not a universal figure across all frontier models.
- The DeepSeek-V3/R1 family substantially improves KV and compute efficiency through Multi-head Latent Attention (MLA) and Mixture-of-Experts (MoE).
- Google Research's TurboQuant demonstrated, in public benchmarks, a reduction in KV memory of <strong>at least 6x</strong>.

\[Inference\] TurboQuant, however, is a research result specific to KV cache. It does not deliver a 6x reduction across weights, scratch, and redundancy as well, nor is it a verified industry-average figure that accounts for latency, throughput, and quality at large-scale production.

The honest conclusion, then, rules out both extremes. `504KB per token × every future workload` overstates demand, while `6x KV compression × the entire HBM footprint` understates it. Future demand sits somewhere between the two extremes, and the key variable is <strong>how the composition of weights and KV shifts</strong>.

---

## 4. Third Lens: Cross-Checking the Big 3 Capacity Expansion Schedule

### 4.1 Fab Capacity and Effective HBM Supply Are Not the Same Thing

A common mistake when assessing supply is converting fab groundbreaking and completion news directly into sellable HBM. Five gaps sit between the two. \[Fact/Inference\]

1. <strong>Rising die intensity</strong>: when dies per stack increase from 12-high to 16-high, the number of dies required for the same stack count rises by about 33%. Even as wafer volume grows, the growth rate of sellable stacks can end up lower.
2. <strong>HBM trade ratio</strong>: HBM consumes more wafer and process resources than commodity DRAM. Micron itself has stated that this ratio rises with each generation, squeezing non-HBM supply.
3. <strong>Back-end processing, yield, and qualification</strong>: good die, TSV stacking, base die, advanced packaging, thermal and power specs, and customer qualification all have to be cleared before volume counts as effective supply.
4. <strong>Ramp lag</strong>: a cleanroom opening or a first wafer is different from qualified volume that can actually be recognized as revenue.
5. <strong>Opportunity cost across product lines</strong>: expanding HBM output can cannibalize commodity DRAM wafers. Even as HBM volume rises, there is no guarantee that overall DRAM pricing stabilizes right away.

### 4.2 Official Capacity Expansion Schedule

The schedule below is confirmed from public primary sources for the Big 3 and for the industry overall.

| Company / Item | Officially Confirmed Details | Interpretation of Actual Supply Contribution |
|---|---|---|
| SK Hynix M15X | Targeted for completion in November 2025; produces next-generation DRAM and HBM | The fastest-moving expansion track for 2026-27. Ramp could be quick given the use of existing infrastructure |
| SK Hynix Yongin Phase 1 | 21.6 trillion won in equipment investment; first cleanroom now planned to open early, in February 2027 | Installation begins in 2027, with the supply effect potentially expanding from 2028 onward |
| SK Hynix Yongin (full complex) | First cleanroom for the fourth phase is targeted for 2033 | The assumption that all four Yongin fabs enter 2030 supply is incorrect |
| Samsung Electronics HBM4 | Mass production and commercial shipment begin February 2026; 2026 HBM revenue expected to more than triple | Samsung's return as a second source in 2026-27 is the single biggest supply-relief variable |
| Samsung Electronics long-term investment | Roughly 2,100 trillion won in semiconductors for 2026-2040, about 1,650 trillion won for Yongin and existing complexes, plus HBM fabs at Onyang and Cheonan | Directionally strong, but this is a spending envelope through 2040. It cannot be translated directly into a 2030 supply figure |
| Micron ID1 | First wafer in mid-2027 | Given customer qualification lead times, meaningful sales fall in late 2027 to 2028 |
| Micron ID2 | First wafer in late 2028 | Contributes to supply relief from 2029 onward |
| Micron Tongluo / packaging | Tongluo reaches meaningful shipments in FY2028; HBM packaging expansion begins in H1 2027 | Eases both front-end and back-end bottlenecks together |
| SEMI, memory industry-wide | 300mm memory capacity projected to rise from 4.1m WPM in 2026 to 4.2m WPM in 2027 | Overall wafer capacity growth is a modest ~2.4%. The HBM mix shift and node bit growth matter more |

### 4.3 Supply-Side Verdict

- \[Fact\] All three of the Big 3 are in the middle of large-scale investment.
- \[Fact\] 2027 is the year cleanrooms and first wafers start to multiply, not the year all of that volume converts into qualified output.
- \[Inference\] Supply relief is likely to become visible starting in 2028 and to strengthen further in 2029-30.
- \[Blocked\] Public data alone cannot confirm whether the 2030 serving fleet will be 10.6EB or 15EB. Exact WPM, product mix, yield, and packaging capacity are not disclosed.

---

## 5. A Sensitivity Analysis Combining All Three Lenses

The direction indicated by all three lenses is consolidated into a single sensitivity table. Supply, the serving fleet, is held fixed at 10.6EB, and only the demand assumptions are independently recalculated using the published formula.

| Scenario | Changed Assumption | 2030 Demand | Demand/Supply | Verdict |
|---|---|---:|---:|---|
| Original model base | Tokens 24x, model 5x, KV efficiency 4x, retention rate 70% | 26.7EB | 2.52x | Severe shortage |
| Model footprint eased | Model multiple from 5x to 2x | 18.5EB | 1.75x | Shortage |
| KV efficiency improved | KV efficiency from 4x to 6x | 22.3EB | 2.10x | Shortage |
| HBM retention rate lower | From 70% to 50% | 22.9EB | 2.16x | Shortage |
| Token growth halved | From 24x to 12x | 16.2EB | 1.53x | Shortage |
| Composite bear | Tokens 12x, model 2x, KV efficiency 6x, retention 50%, throughput 14x | 6.5EB | 0.62x | Supply surplus |
| Composite bull | Tokens 36x, model 8x, KV efficiency 3x, retention 80%, throughput 8x | 67.9EB | 6.41x | Extreme shortage |

The composite bear and bull cases are not official scenarios from the original model. They are independent stress tests designed to examine the covariance among assumptions.

How this table is interpreted is the heart of this deep research.

<strong>First, changing any single variable on its own does not make the shortage disappear easily.</strong> Even lowering the model multiple from 5x to 2x, or halving token growth, still leaves a shortage of 1.5-1.75x. This is the basis for the bull narrative's claim that "the shortage survives no matter which single assumption you shake."

<strong>Second, however, the variables are not independent of one another.</strong> Slower token growth, a shift toward smaller models and MoE, KV compression, HBM offload, and throughput improvement all tend to move <strong>together, several at once, whenever technical efficiency improves</strong>. That is why, in the composite bear case, demand falls to 6.5EB and the picture flips to a supply surplus.

<strong>Third, 2.5x therefore carries the label "base case" but should actually be treated as a bull-skewed scenario.</strong> A one-way sensitivity that moves a single variable to its limit cannot prove the robustness of 2.5x. The real risk lies in the covariance of assumptions collapsing together.

---

## 6. A Market-Clearing Perspective: How to Read the 2.5x Figure

`26.7EB of demand against 10.6EB of supply` should not be read literally as 16.1EB of unfilled orders. In practice, the market clears in this sequence:

```text
Potential AI workload growth
→ Qualified HBM bottleneck
→ Price increases, long-term contracts, prepayments
→ Per-customer allocation and delay of low-ROI workloads
→ Expansion of SLM, MoE, quantization, KV reuse, and offload
→ Additional capex and second-source qualification
→ Realized shipments and cleared demand converge
```

\[Inference\] In other words, the 2.5x figure is more accurately read not as a precise forecast of the physical shortfall that will actually materialize, but as a scenario expressing the <strong>intensity of pricing power and rationing pressure</strong>. A large shortage does not mean "16EB will never be filled." It means that gap comes under strong clearing pressure through price, contracts, and technological substitution.

From this perspective, what a supply-demand analysis should actually watch is not the EB figure itself, but the following. \[Watch points\]

1. Whether price floors in multi-year contracts hold
2. Whether the HBM4/4E ASP premium persists long enough
3. Whether a rising HBM mix also tightens commodity DRAM supply
4. Whether yield and advanced-packaging improvements let the margin on incremental revenue accrue to suppliers
5. How much profit and cash flow accumulate before new 2028 supply normalizes pricing

---

## 7. Outlook by Time Horizon: Base / Bull / Bear

Laying the three lenses and the sensitivity analysis onto a timeline produces the following:

| Period | Base | Bull | Bear |
|---|---|---|---|
| 2026-2027 | HBM4 ramp and AI demand outpace new greenfield supply. Tightness continues | Samsung qualification delays, packaging bottlenecks persist, token and ASIC demand exceed expectations | Samsung's HBM4 volume supply and customer-mix diversification arrive faster than expected |
| 2028 | SK Yongin Phase 1 and Micron ID1/Tongluo/packaging effects begin. Shortage narrows | Supply impact stays limited due to early yield and qualification delays | New capacity stabilizes quickly, with KV and routing efficiency improving at the same time |
| 2029-2030 | Even if a shortage remains, relief is more likely than widening. Pricing power lasts longer than in past cycles | Model footprint and agent concurrency overwhelm efficiency gains; long-term contracts and scarcity premiums persist | Micron ID2, Samsung, and SK expansions ramp simultaneously; efficiency and offload combine to normalize the HBM premium |

### Final Time-Horizon Verdict

- `Tight through 2027`: <strong>high probability</strong>
- `Supply improving from 2028`: <strong>moderately high probability</strong>
- `Shortage easing in 2029-30`: <strong>medium probability</strong>
- `2.5x gap still widening in 2030`: <strong>low probability / bull scenario</strong>

---

## 8. What to Watch: Re-Rating Triggers

Setting out in advance the signals that would confirm whether the supply-demand narrative is strengthening or weakening helps avoid getting whipsawed by headlines.

<strong>Signals that the supply-demand bull case is strengthening</strong>

1. Suppliers officially confirm being sold out, or maintaining long-term contracts and price floors, even beyond 2028
2. HBM4/4E yield and packaging capacity improve while the ASP premium and margins hold
3. Industry tightness guidance extends past 2028 even as Samsung and Micron expand capacity
4. Actual tokens, resident context, and concurrency from agentic workloads track close to the 24x path

<strong>Signals that the supply-demand bull case is weakening</strong>

1. A combined reduction of 6x or more in KV and weight memory becomes commonplace in production environments
2. More than half of incremental inference shifts to memory-light SLM, ASIC, or offload architectures
3. Samsung's HBM4E and Micron's new capacity achieve volume qualification faster than expected
4. Suppliers withdraw their `tight beyond 2027` guidance and customer contract floors weaken
5. HBM ASP premiums, contract pricing, and DRAM margins decline structurally alongside rising supply

---

## Closing: The Direction Is Robust, the Magnitude Should Stay Humble

This deep research boils down to one line: <strong>`HBM tight through 2027, supply improving from 2028` is supported by the data and by official schedules, but `a 2.5x shortage in 2030` is a bull scenario that requires several demand assumptions to hold true at the same time.</strong>

The number 26.7EB reproduces with precision, but that precision is not the same as certainty. It is a value that only emerges if tokens at 24x, models at 5x, context at 4x, and KV retention at 70% all hold <strong>simultaneously</strong>, and these assumptions tend to collapse together as technical efficiency improves. Supply, by contrast, converts into qualified output far more slowly than fab headlines suggest. The point where these two forces meet is the inflection point of 2028.

The useful frame for reading supply-demand is not to trust a single number, but to <strong>separate the confidence of the direction from the uncertainty of the magnitude</strong>. The direction is robust. The magnitude should stay humble.

---

_This post synthesizes public primary sources (Goldman Sachs, SK Hynix, Samsung Electronics, Micron, SEMI, Google Research, and DeepSeek technical reports) together with a secondary model (Memory Analyst) into an independently reproduced and cross-checked supply-demand structure analysis. The stocks mentioned are examples used to illustrate industry structure, not investment recommendations. Figures such as 26.7EB, 10.6EB, and 2.5x are, in large part, model assumptions and scenarios, not official company forecasts. This is a fast-moving field, so we recommend confirming against the latest primary sources._

---

### Related Posts

- [HBM, HBF, HBC: How to Correctly Distinguish the Three AI Memory Technologies](/post/hbm-hbf-hbc-ai-memory-comparison-2026-06-22/)
- [The Present and Future of AI Token Value: Analyzing Memory Makers' Value-Add](/post/ai-token-value-memory-value-added-2026-07-09/)
- [Late-July Big Tech Earnings Calls: Memory Thesis Scenario Analysis](/post/big-tech-july-earnings-call-memory-thesis-scenarios-2026-07-07/)
- [Who Pays for the 2027 Semiconductor Consensus](/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/)
- [Samsung Electronics and SK Hynix 2028E Profit Valuation: Cheap-Looking Numbers and Cycle Verification](/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/)
