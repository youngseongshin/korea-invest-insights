---
title: "Weekly Semiconductor Deep Dive: Strong Earnings, Compressed Multiples, and the 2028 Inflection"
slug: "weekly-semiconductor-deep-dive-strong-earnings-lower-multiple-2028-pivot-2026-07-19"
date: 2026-07-19T15:53:00+09:00
description: "A weekly synthesis connecting TSMC and ASML earnings, DRAM and NAND contract prices, HBM long-term supply agreements, Chinese memory and Kimi K3, and the sharp sell-off in Korean semiconductor stocks onto a single timeline from July 13–19, 2026. Earnings in 2026–2027 are strong, but the market is already discounting 2028 supply expansion, efficiency improvements, and customer profitability."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags:
  - "Semiconductors"
  - "Memory"
  - "HBM"
  - "Samsung Electronics"
  - "SK Hynix"
  - "Micron"
  - "TSMC"
  - "ASML"
  - "CXMT"
  - "Kimi K3"
  - "AI CAPEX"
  - "Valuation"
  - "2028"
series: ["exclusive-analysis", "ai-hbm-2026"]
valley_cashtags:
  - 삼성전자
  - SK하이닉스
draft: false
---

On July 13, KOSPI fell 9.05% and SK Hynix dropped 15.37%. Yet in the same week, TSMC reported Q2 revenue of $40.2 billion and a gross margin of 67.7%, while ASML raised its annual revenue outlook to €43–45 billion. Commodity DRAM and NAND contract prices also rose sharply. It was a week in which physical orders and stock prices moved in opposite directions.

This divergence is less a signal that the semiconductor boom is over, and more a sign that the market's question has changed. Investors are no longer looking only at how much will be earned in 2026 and 2027. They are first calculating how much supply will expand in 2028, whether customers can sustain high memory prices and data center capex, and how much inference efficiency gains will erode the scarcity premium of HBM.

> Connected Context
> This post consolidates [Five Clocks of the Semiconductor Bull and Bear Case](/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/), [Memory Fair Value via FCFE and Normalized Earnings](/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/), [Samsung Electronics and SK Hynix: 2027–2028 Scenarios](/post/samsung-sk-hynix-2027-2028-integrated-scenarios-risk-adjusted-valuation-2026-07-13/), and [HBM 2030 Supply-Demand Model Cross-Check (26.7 EB)](/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/) into a weekly synthesis updated with new data from the third week of July. Related posts are available at the [AI HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/) and the [Exclusive Analysis Hub](/page/exclusive-analysis-hub/).

## TL;DR

* Official data confirmed from July 13–19 does not support the claim that AI semiconductor demand has peaked. TSMC and ASML results and guidance, DRAM and NAND prices, and server memory demand all reinforce the earnings-strength thesis for 2026–2027.
* The same data also amplifies 2028 supply risk. ASML's capacity expansion plans and TSMC's heavy capex are evidence of current orders — and simultaneously a reservation of future supply and depreciation.
* HBM long-term contracts can raise the floor on volume and earnings, but may slow the pace at which spot price spikes translate into blended ASPs. Volume stability and a cap on price upside coexist.
* China plays three roles simultaneously: an end-demand destination, a competitor in commodity memory, and a market that could be politically decoupled. Its larger impact is on 2028 commodity DRAM and NAND price ceilings and global supply discipline, not on near-term HBM substitution.
* Efficiency gains from open models such as Kimi K3 do not simply eliminate semiconductor demand. They can shift the value of some HBM toward server DRAM, eSSD, networking, and power. The key question is not whether cost-per-task falls, but how much total workload expands and what share is deployed on self-built infrastructure.
* Current base-case scenario probabilities: Extended Scarcity 25%, Strong Earnings / Compressed Multiple 40%, Efficiency and Supply Normalization 25%, Financial / Demand Dislocation 10%. The most probable path is one where strong earnings in 2026–2027 and duration discounting for 2028 coexist.

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Key Statement of the Week</div>
  <div class="thesis-callout__body">
    The physical evidence underpinning the memory supercycle passed its first full-scale stress test. Stock prices, however, have begun asking not about the magnitude of scarcity but about how long excess earnings will last. 2026–2027 is the period for earnings delivery; 2028 is the period that simultaneously tests supply, efficiency, and customer profitability.
  </div>
</div>

---

## 1. Scope and Evidence Rules

The analysis covers July 13–19, 2026. Company IR materials, government and congressional filings, industry data, broker estimates, and market supply-demand figures drawn from two weekly analysis documents were re-categorized. Where multiple posts cited the same underlying source, the confirmation count was not incremented.

| Grade | Source | How Used in This Report |
|---|---|---|
| A | Company IR, government / congressional / regulatory filings, SEC disclosures | Baseline for facts and official plans |
| B | Industry research such as TrendForce, primary broker reports | Supporting evidence for pricing, share, and company-level estimates |
| C | Cross-referenced press reports, channel check summaries | Used for directional confirmation only; not used as standalone investment signals |
| D | Social media, circulating summary images | Used only to identify questions requiring further verification |

Orders from TSMC, ASML, and memory manufacturers can reflect the same hyperscaler capex plan multiple times. Official plans signal demand intent but do not guarantee actual utilization or cash flow. The sharp stock price declines were not attributed solely to technical supply-demand dynamics. Flow imbalances can amplify drawdowns, but they cannot eliminate a fundamental re-rating of earnings duration.

## 2. A Map of the Week's Events

| Date | Confirmed Developments | Questions the Market Began Asking | Current Assessment |
|---|---|---|---|
| July 13 | HBM 2030 demand model at 26.7 EB re-verified; SK Hynix Q2 earnings estimate cut; KOSPI sharp decline | Long-term shortage, or excessive extrapolation? | 2027 shortage has strong support; 2030 shortage magnitude carries low conviction |
| July 14 | SK Hynix estimates adjusted to reflect HBM long-term contracts; IBM and Ericsson flagging memory cost burden; reports of Apple testing CXMT chips | Are long-term contracts an earnings floor or a price ceiling? | Volume visibility is high, but ASP upside constraints and customer cost burden emerge alongside |
| July 15 | ASML Q2 results and 2027–2028 capacity expansion plans | Strong orders, or the start of a supply response? | Both are correct — simultaneously reinforces current demand and amplifies 2028 supply risk |
| July 16 | TSMC Q2 results and Q3 guidance; U.S. House letter requesting restrictions on Chinese memory procurement | AI demand is strong — why is memory stock price weak? | Debate centers on earnings attribution, supply, and cost of capital — not demand collapse |
| July 17 | Kimi K3 launch; Chinese open-model efficiency gains and API pricing repricing | Does efficiency reduce semiconductor demand? | Cost-per-task falls, but aggregate usage and self-built deployments may expand |
| July 18 | China AI API cost analysis; review of memory trio's China exposure | Is China a customer or a competitor? | Both roles simultaneously; impacts 2028 normalized value more than 2026 EPS |
| July 19 | Channel checks circulating claiming strong server DRAM and HBM4 orders | Did the sell-off price in a Q3 earnings collapse? | Probability appears lower, but primary source unconfirmed — maintained at Grade C |

The most significant shift in this table is not the direction of individual events, but the time horizon. Until early July, the debate centered on whether H2 2026 earnings would beat expectations. It has since shifted to whether 2028 earnings represent a normalized earnings level, and how long elevated prices and margins can be sustained.

## 3. Evidence Strengthened This Week

### 3.1 TSMC and ASML Showed That AI Orders Have Translated into Real Activity

TSMC's Q2 results demonstrate that AI demand has moved beyond the planning stage.

| Item | TSMC Q2 2026 and Q3 2026 Outlook |
|---|---:|
| Q2 revenue | $40.2 billion |
| Q2 gross margin | 67.7% |
| Q2 operating margin | 60.3% |
| Q3 revenue guidance | $44.6–$45.8 billion |
| Q3 gross margin guidance | 65–67% |

The high gross margins and next-quarter growth guidance indicate that the quality of orders for leading-edge process nodes and advanced packaging remains intact. [TSMC Q2 2026 Official Results](https://investor.tsmc.com/english/quarterly-results/2026/q2)

ASML confirmed the same direction. Q2 revenue of €9.326 billion and net income of €2.918 billion were reported, and the 2026 revenue outlook was set at €43–45 billion. The capacity roadmap reveals the timeline at which current orders translate into future supply.

| Equipment | 2026 Capacity | 2027 Plan | 2028 Under Review |
|---|---:|---:|---:|
| Low-NA EUV | ~65 units | ~30% expansion | Additional ~30% expansion under review |
| DUV immersion | ~130 units | ~30% expansion | Additional ~30% expansion under review |

ASML stated that AI investment is driving demand for leading-edge logic and memory, and that customer capacity commitments are converting into long-term demand visibility. These figures weaken the strong bear case that AI orders consist entirely of duplicate bookings. [ASML Q2 2026 Official Results](https://www.asml.com/en/news/press-releases/2026/q2-2026-financial-results)

### 3.2 Memory Prices Remain Elevated

TrendForce projected Q2 2026 commodity DRAM contract prices to rise 58–63% quarter-over-quarter, and NAND prices to rise 70–75%. The Q3 server DRAM price growth forecast was revised to 13–18%, but the upward trajectory is maintained. [Q2 DRAM/NAND Outlook](https://www.trendforce.com/presscenter/news/20260331-12995.html), [Q3 Server DRAM Outlook](https://www.trendforce.com/presscenter/news/20260709-13140.html)

It is important to distinguish between a deceleration in the rate of price increases and an actual price decline. Given how rapidly prices rose in Q2, the quarter-over-quarter growth rate in Q3 may slow. Nonetheless, if absolute prices remain elevated, suppliers' operating income can remain strong. The risk the market is pricing is not a decline in earnings, but a deceleration in earnings growth.

### 3.3 HBM Ramp Cannibalizes Commodity DRAM Supply

HBM requires more wafer area, stacking, packaging, and testing capacity than commodity DRAM to produce the same number of bits. As the three memory manufacturers increase their HBM mix, HBM shipments expand while the effective bit supply of commodity DRAM can shrink.

As a result, the bottleneck broadens in the following sequence:

```text
GPU / ASIC
-> HBM
-> Server DRAM
-> eSSD and NAND
-> Packaging / Substrate / Test
-> Networking / Power / Cooling
```

AI agents and long-context inference do not rely solely on HBM for model weights. They also consume server DRAM and eSSD for KV cache and data serving, and consume more networking to connect multiple accelerators and sparse mixture-of-expert models. This is why aggregate memory tier volumes can continue to expand even if HBM unit pricing comes under pressure.

### 3.4 2027 Shortage Is a Strong Conclusion; 2.5× Shortage by 2030 Is a Scenario

Comparing 2030 HBM demand of 26.7 EB against supply of 10.6 EB yields demand at 2.52× supply. The arithmetic is reproducible. The issue lies not in the result but in whether the underlying assumptions hold simultaneously. The base model assumes 24× token growth, 5× model size expansion, 4× context length extension, and a 70% HBM retention rate for KV cache — all simultaneously.

| Assumption Change | 2030 HBM Demand | vs. 10.6 EB Supply |
|---|---:|---:|
| Base model | 26.7 EB | 2.52× |
| Model size 2× | 18.5 EB | 1.75× |
| KV efficiency 6× | 22.3 EB | 2.10× |
| HBM retention rate 50% | 22.9 EB | 2.16× |
| Tokens 12× | 16.2 EB | 1.53× |
| Composite bear assumptions | 6.5 EB | 0.62× |

Reducing any single variable still leaves a shortage, but if multiple bearish assumptions hold simultaneously, oversupply becomes possible. The investable statement is therefore: "The market is likely to remain tight through 2027." The statement "Supply will be definitively 2.5× short by 2030" cannot be directly plugged into a price target.

## 4. Risks Strengthened This Week

### 4.1 Earnings Growth Rate Has Become More Important Than Strong Absolute Earnings

The SK Hynix Q2 operating income estimate cut originated from adjustments to ASP assumptions rather than from a collapse in shipment volumes.

| Report | Q2 2026 Operating Income Estimate | Key Adjustment |
|---|---:|---|
| Mirae Asset Securities | From ₩70.7 trillion to ₩62.3 trillion | DRAM ASP from +40.6% to +32.9%; NAND from +55% to +50% |
| Korea Investment & Securities | ₩60.4 trillion | DRAM ASP +28.9%; NAND +50.9% |

An operating income in the ₩60 trillion range is very large in absolute terms. However, stock prices responded more to the magnitude of the revision from prior estimates than to the absolute level of earnings. The 15.37% decline in SK Hynix on July 13 is better explained by the combination of shifting expectations and concentrated technical supply-demand dynamics than by any conclusion that the upcycle has ended.

This is the central logic of the weekly analysis. Strong demand alone does not drive stock prices higher. Demand must beat market expectations, and evidence that elevated earnings persist into 2028 is required.

### 4.2 Long-Term Contracts Create Both an Earnings Floor and a Price Ceiling

HBM long-term supply agreements provide volume visibility, customer lock-in, predictability of payback periods, and downside protection when spot prices fall. On the other side, the following concerns apply:

* Even if spot prices spike, a company's blended ASP may rise only gradually.
* Pricing formulas, renegotiation mechanisms, minimum purchase commitments, and cancellation terms are not disclosed.
* Customer compliance with minimum purchase obligations and credit risk remain with the supplier.
* Up-front payments and long-term volume commitments may not flow through to accounting earnings and operating cash flow at the same pace.

Interpreting long-term contracts as an unconditional reinforcement of pricing power is only half the picture. Contracts raise the earnings floor and reduce volatility, but they may not capture the full upside of a spot price spike. The SK Hynix Q2 estimate revision was the first instance of this gap appearing in reported numbers. The detailed figures are discussed in [SK Hynix Q2 Earnings Cut and Maintained Price Targets](/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/).

### 4.3 Equipment Orders Are Both Current Demand and Future Supply

Reading ASML's capacity expansion solely as near-term bullish evidence misses the time dimension.

```text
Low-NA EUV 2027 capacity ≈ 65 units × 1.30 = 84.5 units
DUV immersion 2027 capacity ≈ 130 units × 1.30 = 169 units
```

Equipment manufacturers recognize orders as revenue in 2026–2027 first. Actual bit production at memory manufacturers can increase from 2028 onward, after equipment installation, yield stabilization, and packaging capacity additions. The same capex that initially boosts equipment and materials earnings later pressures memory prices and margins.

The metrics to watch for 2028 are therefore not the announced investment totals. They are equipment installation timing, new wafer starts, yield ramp, packaging throughput, the increase in depreciation, and actual bit output.

### 4.4 High Memory Prices Can Erode Customer Demand

When memory prices rise, customers can respond in four ways:

1. Pull forward inventory purchases before prices rise further.
2. Raise server and end-product prices.
3. Reduce memory content or downgrade specifications.
4. Delay purchases and projects.

The first behavior makes near-term orders appear stronger but simply pulls forward future demand. The other three represent pathways through which suppliers' pricing power ultimately destroys customer demand. The IBM and Ericsson examples showed that memory supply constraints have begun to affect end-customer budget allocation and margins. We are currently in a phase where pre-buying and specification adjustments are visible before large-scale order cancellations.

### 4.5 AI Capex Bottleneck Is Shifting to Cost of Capital

Even if AI demand is real, if the investing entity's cash flow cannot keep pace with depreciation and financing costs, the pace of investment will slow. Going forward, the following four items matter more than the absolute capex figure from hyperscalers:

* Whether AI and cloud gross margin growth outpaces the increase in depreciation.
* Whether data center power delivery and GPU utilization ramp according to plan.
* Whether returns on new projects, including borrowing costs, exceed the cost of capital.
* Whether the credit quality and up-front payments from customers that have signed HBM long-term contracts remain stable.

The strength of orders at TSMC and ASML means they are not evidence of current demand collapse. However, in U.S. Big Tech earnings releases at the end of July, investors should examine AI gross margins, free cash flow, and the slope of 2027 investment guidance alongside — not instead of — total capex figures.

## 5. Was the Share Price Plunge a Supply-Demand Shock or a Fundamental Repricing?

This week's sharp decline in Korean semiconductor stocks bears the hallmarks of leverage unwinding, program selling, and a market-cap structure heavily concentrated in a handful of large-cap names — all of which amplified the drawdown. Simultaneous selling by foreign and institutional investors caused single-day price moves far in excess of any change in underlying business value.

Yet concluding that "it was merely a supply-demand shock, so everything rebounds" carries its own danger. If relative strength fails to recover even after strong earnings and pricing data, it may signal that the market is actively lowering its estimates for 2028 EPS and normalized multiples.

The diagnostic framework is straightforward.

| Signals pointing toward a supply-demand shock | Signals pointing toward a fundamental repricing |
|---|---|
| Foreign and program selling decelerates quickly | Selling continues despite positive news |
| Relative strength recovers on volume | Semiconductors continue to underperform the broader market |
| 12-month forward EPS revisions remain positive | Samsung Electronics, SK Hynix, and Micron EPS all revised down simultaneously |
| Contract prices rise and inventories stabilize | Inventories build while contract prices decline simultaneously |
| Big-Tech CAPEX and AI profitability both improve | CAPEX cuts or deteriorating AI margins |

This distinction is precisely why price and earnings estimates must be tracked together. Watching only supply-demand dynamics risks missing long-term risks; watching only results risks missing the additional downside created by crowded positioning.

## 6. China Is Three Variables at Once

### 6.1 China Is a Major Demand Market

China exposure figures disclosed in company filings use different definitions, making direct comparisons difficult.

| Company | China Exposure Metric | Caveat |
|---|---:|---|
| Samsung Electronics | 30.1% | Based on standalone consolidated revenue — not memory-only share |
| SK Hynix | 1Q26 24.3%, full-year 2025 19.7% | Based on sales entity location |
| Micron | FY25 China + Hong Kong 10.1% | Based on customer headquarters location |

Samsung and SK Hynix are directly exposed if Chinese demand contracts. Micron's direct exposure is comparatively low, but it cannot escape the impact if global pricing declines. Revenue-share figures alone are insufficient to assess China risk.

### 6.2 China Is a Commodity Memory Competitor

CXMT has announced mass production of LPDDR5X at 8,533 Mbps and 9,600 Mbps, with its 10,667 Mbps product reportedly in customer qualification. Its estimated share of global DRAM revenue for Q1 2026 stands at approximately 8%. However, an Apple supply agreement, broad adoption in flagship global products, and HBM yield have not been confirmed. [CXMT LPDDR5X Official Announcement](https://www.cxmt.com/en/news/info_19.html)

The near-term threat is concentrated in two channels rather than HBM displacement:

1. Localization of commodity DRAM and NAND in Chinese smartphones and PCs.
2. Using CXMT as a fourth-supplier card in price negotiations with the established memory trio.

If volume displaced from China migrates to other markets, it could pull down global contract prices for Samsung, SK Hynix, and Micron. This price contagion may matter more as a second-order effect than a direct decline in China revenue. A detailed exposure breakdown is available in [China Memory Localization and the Big Three](/post/china-memory-localization-exposure-samsung-hynix-micron-2026-07-18/).

### 6.3 China Can Be Segmented by Policy

On July 16, members of the House Select Committee on China sent a letter to the Department of Commerce calling for tightened controls on YMTC, accelerated review of CXMT for Entity List inclusion, restrictions on Chinese DRAM and HBM procurement in AI systems, data centers, federal IT, and critical infrastructure, and coordination with South Korea, Japan, and the EU. This is a policy demand — not an implemented purchasing ban. [House Select Committee on China Official Letter](https://chinaselectcommittee.house.gov/media/letters/moolenaar-whitesides-to-secretary-lutnick-hold-firm-on-chinese-memory-chips-ban)

If enacted, the global memory market could bifurcate along the following lines:

| Market | Possible Structure |
|---|---|
| United States and allies | Verified supply chains, higher prices, market-share defense by the memory trio |
| Chinese domestic market | Localization, lower prices, medium-term oversupply risk |

Micron stands to benefit most directly from U.S. policy. Samsung and SK Hynix carry both the advantage of being allied-nation suppliers and the exposure of their China businesses. This policy factor is less a catalyst that directly lifts 2026 HBM earnings and more a variable that reduces the China-oversupply discount rate priced into 2028 valuations.

## 7. Kimi K3 and Efficiency: Demand Shifting, Not Demand Destruction

According to Kimi's official announcement, K3 has 2.8 trillion total parameters, activates 16 of 896 experts per token, and supports a 1 million-token context window. The sparse expert architecture reduces compute per request, but still requires large memory and high-bandwidth networking to store all weights and route expert selection. [Kimi K3 Official Announcement](https://www.kimi.com/blog/kimi-k3)

The semiconductor impact of efficiency gains is better understood through the following equation:

```text
Total semiconductor demand = silicon cost per task × total number of tasks × fraction self-hosted
```

* Sparse architectures, caching, and quantization reduce GPU time and HBM footprint per task.
* Falling API prices increase AI usage volumes and the number of agents.
* Open-weight models may increase self-hosted server deployments by enterprises and governments.
* Memory tiering shifts some HBM workload onto server DRAM, eSSD, and remote caches.

Current firm orders and CAPEX data suggest that volume growth is outpacing efficiency gains. Over a longer horizon, however, the volume elasticity of server DRAM, eSSD, networking, and power may prove more favorable than the pricing power of premium GPUs and HBM. Efficiency is less a variable that "reduces total semiconductor consumption" and more one that reshapes "which semiconductors capture the revenue."

Two caveats apply here. The KV-cache savings rates and theoretical throughput from Kimi's linear research models cannot be directly applied to K3 in production. Additionally, self-reported performance benchmarks should not be weighted equally with independent verification. Weights, licensing terms, independent throughput results, and actual tokens and total cost per task require confirmation.

## 8. Five Clocks — When They Are Watched Together, the Contradictions Resolve

| Clock | This Week's Observation | Investment Interpretation |
|---|---|---|
| Pricing | Sharp 2Q DRAM and NAND price increases; 3Q pace of gains decelerating | 2026 earnings look strong, but the rate of increase may slow |
| Investment | TSMC expanding investment; ASML orders and capacity growing | Current demand confirmed while 2027–2028 supply response is booked |
| Construction | Power, land, and packaging bottlenecks persist | Announced investment lags before translating into actual production ramp |
| Monetization | AI usage rising; customer costs and financing charges also rising | AI gross margin and free cash flow require scrutiny alongside revenue |
| Share price | Sluggish reaction to positive news; concentrated supply-demand shock in Korea | Market is discounting duration and positioning rather than current earnings |

The pricing and investment clocks are running fast, while the construction and monetization clocks are lagging. The share-price clock is the forward-looking reflection of whether that gap narrows or widens ahead. That is why strong results and raised CAPEX guidance can trigger selling on the same day.

The "55% industry strength / valuation weakness coexistence" from the prior piece and "P2 at 40%" below are not two different readings of the same table. The 55% was a broad category in which multiples remain compressed even as the industry stays strong. The more granular distribution here splits that category further into the early phases of P2 and P3. Because new data from TSMC and ASML confirmed current demand while simultaneously expanding the implied supply response, a portion of the long-term scarcity probability has been shifted toward supply normalization.

## 9. Scenario Update

The probabilities below are judgment values reflecting information confirmed as of July 19 — not historical base rates.

| Scenario | Probability | Conditions for Validity | Expected Market Behavior |
|---|---:|---|---|
| P1. Sustained Scarcity | 25% | AI usage, CAPEX, and utilization rates continue to overwhelm supply and efficiency gains; HBM4 pricing and orders hold | High-beta memory names such as SK Hynix and Micron, alongside packaging and equipment, outperform |
| P2. Strong Earnings, Compressed Multiples | 40% | Earnings remain strong in 2026–2027 but concerns over 2028 supply and customer profitability persist | Range-bound trading and elevated volatility despite earnings growth; Samsung Electronics carries relative advantage |
| P3. Efficiency and Supply Normalization | 25% | 2027–2028 capacity expansion, Chinese commodity supply, customer price resistance, and declining AI costs converge | HBM scarcity premium narrows; equipment and materials orders peak before memory itself |
| P4. Financial or Demand Dislocation | 10% | Big-Tech CAPEX cuts, a credit event, rising inventories, and simultaneous contract price and EPS downgrades | Sector-wide semiconductor decline; cash and non-semiconductor diversification become more important |

The previous detailed distribution was 35% / 40% / 15% / 10%. This revision moves 10 percentage points from P1 to P3. TSMC and ASML order data did not raise the probability of P4. Conversely, equipment capacity expansion and the pricing burden on customers have increased the probability of supply and efficiency normalization relative to prolonged scarcity.

## 10. Roles by Stock and Value Chain

### Samsung Electronics: Risk-Adjusted Core

Samsung absorbs commodity DRAM and NAND price appreciation across a broad market share base while retaining the option value of catching up in HBM and recovering its foundry business. It also holds relative defensive characteristics should open models and low-cost inference proliferate, shifting some HBM workload toward commodity memory and storage.

Key risks include exposure to China and commodity memory, uncertainty around HBM4 customer qualification, and the high capital burden of foundry operations. Samsung offers more defensive characteristics than SK Hynix in P2 and P3, but diversification does not equal profitability if HBM catch-up has not been validated in earnings.

### SK Hynix: Pure Beta on Sustained Scarcity

SK Hynix's leading HBM market share, co-development relationships with customers, and long-term supply agreements give it the strongest earnings leverage under P1. Conversely, it also carries the highest sensitivity to earnings and multiple compression if supply expansion and efficiency gains accelerate under P3.

Additional judgment requires tracking HBM4 and HBM4E customer qualifications, yield, average selling price terms embedded in long-term contracts, and foreign-investor and program-trading flows alongside relative strength. Business quality and price-embedded margin of safety must be assessed separately.

### Micron: Intersection of U.S. Policy and Pure-Play Memory

Micron is the most direct beneficiary of U.S.-based manufacturing, policy support, and restrictions on Chinese memory procurement. It offers a clean read-through to the HBM, DRAM, and NAND upcycle. However, its limited business diversification means it is also directly exposed to any normalization in global average selling prices. Even with a low China revenue share, Micron cannot easily avoid the impact if surplus Chinese-origin volumes depress global pricing.

### SanDisk: Tactical Beta on NAND and eSSD

SanDisk is directly exposed to NAND supply constraints and AI server eSSD demand. It stands to benefit most if low-cost inference and memory tiering shift incremental storage volumes away from HBM. At the same time, NAND exhibits greater price volatility than DRAM and carries more direct YMTC exposure, giving it a more tactical character relative to core positions.

### TSMC and ASML: Demand Validators and Leading Indicators of Future Supply

TSMC demonstrates the quality of AI demand and the depth of the leading-edge foundry moat. ASML is the earliest observable data point for customers' long-term capacity expansion intentions. Both companies' results serve as supporting evidence for the memory thesis, but they are not simple coincident indicators. High CAPEX and growing equipment supply signal not only future memory demand but also future supply expansion.

### Korean Equipment and Materials: Actual Orders and Recurring Revenue Over Published Plans

| Category | Candidate Names | Data to Confirm | Current Role |
|---|---|---|---|
| Recurring consumables | Hana Materials, Wooldex | Customer utilization rates, OEM channels, revenue and operating margin correlation | Priority research group |
| Process equipment | KC Tech, Nextin | Actual orders, customer qualification, backlog | Conditional confirmation group |
| HBM back-end | Techwing | Additional Cube Prober orders and production revenue | Event confirmation group |
| Infrastructure construction | Hanyang E&E, others | Major contract wins, order-to-revenue ratio, margins | Order-event group rather than core |

The confirmation sequence for investments is: capacity announcement → actual order placement → backlog build → revenue recognition → recurring consumables. Equipment names may peak in earnings earlier than memory production itself. Rather than buying broadly on fab plans alone, the focus should narrow to companies where actual orders and margins are confirmed.

## 11. Counter-Arguments: Where This Thesis Could Be Wrong

### Demand Evidence May Have Been Double-Counted

Orders from TSMC, ASML, and the memory trio may all originate from the same Big-Tech capital expenditure plans. Adding orders across multiple tiers of the supply chain as separate demand signals overstates actual end demand. Power connection timelines, GPU utilization, server shipments, and cloud AI gross margins are the terminal verification data points.

### The 2030 Demand Model May Underestimate Efficiency Gains

If any one of — token count, model size, context length, or HBM retention rate — is reduced, a shortage persists. But if all four decline simultaneously, a 2030 oversupply scenario becomes plausible. The directional case for long-term shortage and the numerical magnitude of that shortage must be assessed separately.

### CAPEX May Grow Faster Than Returns

Suppliers must spend more on new fabs and packaging even when order books are full. Customers must absorb data center depreciation and interest expense. If revenue growth fails to translate into free cash flow growth, high earnings may attract depressed multiples.

### China Policy May Not Be Implemented

The House Committee letter is a policy signal — not an executive order or coordinated allied action. If CXMT enters only a limited set of consumer products within China and enforcement remains loose, pricing leverage for the incumbents may erode before any meaningful market-share shift occurs.

### Open-Model Company Disclosures May Not Be Independently Reproducible

Kimi K3's official specifications are confirmed, but throughput, real-world token consumption, and total serving cost require independent verification. Conversely, if efficiency gains arrive faster than expected and usage elasticity is lower than assumed, the HBM scarcity premium could compress more severely.

### The Entire Price Decline May Have Been Attributed to Forced Liquidation

Leverage unwinding and program selling explain the magnitude of the drop. But if prices fail to recover even in the face of positive news, the market may be actively lowering its 2028 earnings and normalized-multiple assumptions. A supply-demand explanation cannot substitute for validating earnings durability.

## 12. Observable Conditions That Would Change the Thesis

Rather than any single article or a one-day bounce, the key is whether two independent data axes move together.

### Conditions That Raise the Probability of a Bullish Outcome

1. Big-Tech CAPEX growth and improvement in AI and cloud gross margins are confirmed simultaneously.
2. Data center power connections, GPU utilization rates, and server shipments all rise together.
3. HBM4, server DRAM, and eSSD prices, along with 12-month forward EPS, continue to be revised upward.
4. Samsung Electronics, SK Hynix, and Micron rally on positive news and recover relative strength versus the semiconductor index.
5. Foreign-investor and program selling decelerates, and a trend recovery accompanied by volume emerges.

### Conditions That Raise the Probability of P3 Normalization

1. 2027–2028 equipment delivery and new bit capacity come online faster than planned.
2. HBM yields and packaging productivity improve sharply while supply from all three incumbents expands simultaneously.
3. Following memory price increases, customers reduce their content per device and purchasing deferrals become widespread.
4. CXMT DDR5 and LPDDR5X customer qualifications and sales outside China increase.
5. Server DRAM and HBM contract price growth rates and 2028 EPS are simultaneously revised lower.

### P4 Warning Conditions

1. U.S. Big-Tech companies cut CAPEX or cancel or delay data center projects.
2. Credit spreads and refinancing risk for AI infrastructure customers spike sharply.
3. DRAM and NAND inventory builds and contract price declines occur simultaneously.
4. 12-month forward EPS for Samsung Electronics, SK Hynix, and Micron are all revised downward together.
5. Semiconductor relative strength and market breadth (advance-decline) both deteriorate simultaneously.

## 13. Data to Track from Late July Onward

| Timing | Data to Track | Judgment That Changes |
|---|---|---|
| Late July | U.S. Big-Tech earnings and conference calls | CAPEX, AI gross margin, free cash flow, memory price resistance |
| Late July | Additional Kimi K3 technical disclosures and independent evaluations | Which is larger — efficiency gains or usage growth |
| Late July | Samsung Electronics and SK Hynix detailed IR disclosures | HBM4, long-term contracts, DRAM and NAND ASP, shipments, CAPEX |
| August onward | 3Q contract pricing and distribution inventory levels | Whether the pace of price gains has peaked and pre-buying is normalizing |
| Quarterly | ASML bookings, TSMC CAPEX, memory equipment orders | Speed of 2027–2028 supply response |
| Ongoing | CXMT and YMTC regulatory actions and customer qualifications | Chinese supply's price contagion to global markets and market bifurcation |

## 14. Final Judgment

This week served as the first comprehensive stress test of the memory supercycle narrative. Share prices moved sharply, but TSMC and ASML results, DRAM and NAND pricing, and server memory demand all tilted the weight of evidence toward 2026–2027 physical shortages remaining intact.

At the same time, the same data made 2028 risks more clearly defined. Equipment capacity and CAPEX are expanding, long-term HBM supply agreements slow the pass-through of price increases, customers must absorb elevated memory prices alongside data center financing costs, and Chinese commodity memory and open-model efficiency gains will exert pressure on 2028 pricing and multiples.

The choice between "the boom is over" and "this is a permanent supercycle" is therefore a false one. The current base-case path is as follows:

```text
2026–2027: Physical shortage and high earnings
-> 2027–2028: Equipment, capacity, and yield response
-> Pace of price increases decelerates
-> Absolute earnings remain above historical levels, but multiples compress
-> Return dispersion across names driven by product mix, contract structure, and China exposure
```

From this point, the central task is not to re-prove that AI demand exists. It is to measure simultaneously the speed of the supply response, the monetization trajectory for customers, contract quality, 2028 earnings estimates, and how share prices react to positive news. Earnings today are speaking to 2026 and 2027. The market is already asking about 2028.

---

## Key Sources

* [TSMC Q2 2026 Official Earnings](https://investor.tsmc.com/english/quarterly-results/2026/q2)
* [ASML Q2 2026 Official Earnings and Capacity Plans](https://www.asml.com/en/news/press-releases/2026/q2-2026-financial-results)
* [TrendForce Q2 2026 DRAM and NAND Price Outlook](https://www.trendforce.com/presscenter/news/20260331-12995.html)
* [TrendForce Q3 2026 Server DRAM Outlook](https://www.trendforce.com/presscenter/news/20260709-13140.html)
* [U.S. House Select Committee on China — Letter Calling for Restrictions on Chinese Memory Procurement](https://chinaselectcommittee.house.gov/media/letters/moolenaar-whitesides-to-secretary-lutnick-hold-firm-on-chinese-memory-chips-ban)
* [U.S. Department of Commerce BIS Entity List Regulations](https://www.bis.gov/ear/title-15/subtitle-b/chapter-vii/subchapter-c/part-744/ss-74416-entity-list)
* [Kimi K3 Official Announcement](https://www.kimi.com/blog/kimi-k3)
* [CXMT LPDDR5X Official Announcement](https://www.cxmt.com/en/news/info_19.html)

## Limitations of Public Data

1. The long-term contract pricing formulas for HBM from Samsung Electronics, SK Hynix, and Micron — including floor and ceiling prices, minimum purchase volumes, cancellation clauses, and customer-specific credit terms — have not been disclosed publicly.
2. There are no reliable official figures for CXMT's HBM yield or its progress toward Apple qualification.
3. Full unit cost by model and actual per-accelerator serving costs for Chinese AI API providers are not publicly reported.
4. The 26.7 EB HBM demand figure for 2030 is not a consensus forecast but a scenario constructed by combining several bullish assumptions.
5. The July 19 channel checks on server DRAM and HBM4 could not be independently sourced from primary documents and are used solely for directional reference.
6. The information cutoff date is July 19, 2026. Scenarios should be revisited following earnings releases from U.S. large-cap tech companies and memory makers expected in late July.

> This article is an informational analysis based on publicly available sources and does not constitute a recommendation to buy or sell any specific security. Prices, supply-demand dynamics, earnings estimates, and policy conditions are subject to change; readers should verify the latest disclosures and assess findings against their own risk tolerance.
