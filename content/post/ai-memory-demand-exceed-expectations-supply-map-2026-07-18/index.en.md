---
title: "Will AI Memory Demand Exceed Expectations? Reading the Over-Growth Odds Through Demand Scenarios and the Supply Map"
slug: "ai-memory-demand-exceed-expectations-supply-map-2026-07-18"
date: 2026-07-18T18:00:00+09:00
description: "AI memory demand is likely to meet or exceed today's high expectations, but a large upside beat is not yet the base case. We probability-weight demand into base, beat and miss scenarios (45/35/20), lay out six upside variables and six downside risks, then connect the memory-layer supply bottlenecks, the site-by-site expansion maps of Samsung, SK Hynix and Micron, and the substance of Chairman Chey's expansion argument. The conclusion is a shortage thesis through 2027 and re-verification from 2028."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags:
  - "AI Memory"
  - "HBM"
  - "DRAM"
  - "Samsung Electronics"
  - "SK Hynix"
  - "Micron"
  - "SOCAMM2"
  - "Memory Supply-Demand"
  - "Capacity Expansion"
  - "Memory Cycle"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Context
> This post takes head-on the <strong>2026-2028 supply-demand window</strong> that sits between the 2030 long-term supply-demand outlook covered in [HBM 2030 Supply-Demand Deep Research](/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/) and the valuation computed in [Are Semiconductors Cyclical, and What Is Fair Value?](/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/). It pairs well with [The Real Debate in Semiconductors](/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/) and [China's Memory Localization and Korea](/post/china-memory-localization-exposure-samsung-hynix-micron-2026-07-18/). Related hubs are the [AI HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/) and the [Exclusive Analysis Hub](/page/exclusive-analysis-hub/).

## TL;DR

* <strong>AI memory demand is likely to meet or exceed today's high expectations.</strong> But exceeding them by a wide margin is not yet the base scenario.
* The probability read is this. Meeting expectations <strong>45%</strong>, meaningfully beating <strong>35%</strong>, missing <strong>20%</strong>. The probability that strong growth continues is about <strong>80%</strong>, and the probability of significantly exceeding current expectations is about <strong>35%</strong>. \[Inference: own probability judgment\]
* The key to an upside beat is not "AI servers sell a lot." <strong>Accelerator shipment volume and memory content per accelerator both need to come in larger than expected, at the same time.</strong>
* The real asymmetric alpha is not HBM growth itself. The market already knows that. The alpha is <strong>whether demand spreads from HBM into server DDR, SOCAMM and eSSD, and whether the duration extends past 2028</strong>.
* Chairman Chey Tae-won's expansion argument is not a near-term price-cut declaration. It is a message about <strong>market-preserving expansion and staking out the post-2028 supply chain</strong>. The 2026-2027 shortage outlook is not undermined, and the real oversupply risk sits in 2028-2030, when new fabs reach normal yield at the same time. \[Analysis scope\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Key Framing</div>
  <div class="thesis-callout__body">
    AI memory grows strongly. But the condition for the stock's next leg up is not 2027 earnings growth. It is evidence that 2028 earnings do not roll over. What matters now is not HBM growth, but whether demand spreads into server DDR, SOCAMM and eSSD and continues past 2028.
  </div>
</div>

---

## 1. What the Market Already Expects

To discuss an upside beat, we first need to know what the market already expects. The current bar for expectations is already high. \[Fact: public forecast synthesis\]

- 2026 HBM demand up about 2x
- 2026 AI server shipments up more than 20%
- 2027 HBM bit demand +50-65%
- 2027 HBM wafer input share about 30%
- 2027 total DRAM bit demand around +20%

TrendForce expects HBM demand to be driven by AI ASIC in 2026, and jointly by Rubin Ultra and AI ASIC in 2027. HBM content per AI ASIC is also on a path from the current 96GB/192GB up to 216GB/288GB. \[Fact: TrendForce\]

So simply "AI servers sell a lot" does not constitute an upside beat. <strong>Accelerator shipment volume and memory content per accelerator both need to come in larger than expected, at the same time.</strong>

---

## 2. The Base Demand Model

Memory demand is best read through the following formula.

```text
HBM bit demand      = AI accelerator shipments × HBM stacks per accelerator × capacity per stack
Server DRAM demand  = server shipments × DRAM content per server
LPDDR demand        = mobile/AI server shipments × LPDDR content per device
```

### The 2027 Base Scenario

The table below is our own model connecting public forecasts to the current product roadmap. It is an estimate, not an official consensus. \[Inference: own model\]

| Category | Assumed DRAM bit share | Device/system growth | Content growth | Bit demand growth |
|---|---:|---:|---:|---:|
| HBM | 18% | AI accelerators +35% | Capacity per accelerator +15% | About +55% |
| Server DDR5/SOCAMM | 32% | Servers/CPUs +12% | Capacity per server +10% | About +23% |
| Mobile/PC/automotive | 50% | Devices +2% | Capacity per device +5% | About +7% |
| <strong>Weighted total</strong> | 100% | | | <strong>About +21%</strong> |

If accelerator shipments rise 35% and HBM capacity rises 15%, HBM bit demand is <strong>1.35 × 1.15 - 1 = +55.3%</strong>. This multiplicative structure is why HBM demand can grow more than 50% even when server shipments rise only 20%.

Micron projects industry DRAM bit shipment growth of low-to-mid 20% in 2026 and expects the supply shortage to persist beyond 2027. TrendForce likewise estimates that 2026 HBM demand will grow about 2x and that the HBM wafer input share will rise from 22% in 2026 to 30% in 2027. \[Fact: Micron·TrendForce\]

---

## 3. Three Demand Scenarios

These probabilities are not statistical probabilities. They are a subjective judgment reflecting current bookings, CAPEX and product roadmaps.

| Scenario | Probability | 2027 DRAM bit | 2028 DRAM bit | HBM demand | Supply-relief timing |
|---|---:|---:|---:|---:|---|
| Base | <strong>45%</strong> | +20-23% | +17-21% | 2027 +50-65% | Commodity DRAM 2H27, HBM 2028 |
| Demand beat | <strong>35%</strong> | +28-32% | +25-30% | 2027 +70-85% | Commodity DRAM 2028, HBM 2029-30 |
| Demand miss | <strong>20%</strong> | +12-17% | +8-14% | 2027 +30-40% | Commodity DRAM 1H27, HBM 2H27-28 |

\[Inference: scenario estimate\]

Adding the 45% probability of meeting expectations to the 35% probability of meaningfully beating them gives <strong>an approximately 80% probability that strong growth continues</strong>. But the probability of significantly exceeding current expectations is only about 35%, so an upside beat is not the base scenario.

---

## 4. Six Upside Variables That Raise the Odds of a Beat

### ① GPU and ASIC Grow Together (the Strongest Upside)

The market treats ASIC as a substitute for NVIDIA, but to memory makers <strong>both are customers</strong>. TPU and Trainium may erode GPU share, yet they still consume HBM or high-capacity server DRAM.

```text
NVIDIA GPU growth + Google TPU/AWS Trainium/Meta ASIC growth
→ HBM customer diversification
→ Expansion of total HBM bit demand
```

Add 16-hi HBM4E and custom HBM on top, and this can push past the +55% calculated earlier toward +70%. The most direct beneficiaries, in order, are <strong>SK Hynix > Samsung Electronics > Micron</strong>. Samsung has the added option of custom HBM for ASIC customers plus its own foundry base die. \[Inference: exposure structure\]

### ② The Bottleneck Spreads From HBM to the Entire Memory Stack

AI servers do not run on HBM alone.

- GPU/ASIC: HBM
- CPU/host memory: DDR5/SOCAMM2
- Cache/data storage: Enterprise SSD
- Networking/low-cost inference: GDDR/LPDDR

In July 2026, SK Hynix presented not just HBM but SOCAMM2, DDR5, GDDR7, LPDDR and eSSD together as a single AI memory portfolio. \[Fact: SK Hynix\] <strong>Even if HBM falls a bit short of expectations, SOCAMM, server DDR and eSSD can beat in its place.</strong> So we put the probability of an upside beat on total AI memory, rather than HBM alone, at a higher level of about 45%. \[Inference: portfolio diversification\]

### ③ SOCAMM2 Forms a New Demand Layer

SOCAMM2 is not a simple conversion of existing mobile LPDDR into a server form factor. It is a <strong>new segment</strong> that turns AI rack CPU/host memory into a low-power, high-capacity structure. SK Hynix has started mass production of 192GB SOCAMM2, and as adoption spreads across server CPUs and AI racks, LPDDR5X demand rises separately from HBM. \[Fact: SK Hynix SOCAMM2\]

### ④ Agentic AI Stimulates Server DRAM and eSSD at the Same Time

Training is HBM-centric, but agentic inference draws on several layers at once.

- HBM: model computation
- DDR5/SOCAMM: CPU/system memory
- eSSD: vector DB, KV cache, data storage
- Network buffer memory

When agents hold state and context over long periods, memory content per system rises along with token counts. In this case, server DDR and eSSD can turn out stronger than expected, more so than HBM. \[Inference: workload analysis\]

### ⑤ China's Low-Performance Chip Strategy Actually Increases Memory Volume

If China connects more low-performance chips instead of fewer high-performance GPUs, the same amount of compute requires more chips, servers and memory. The direct beneficiaries may concentrate less in top-tier HBM and more in <strong>DDR5, LPDDR5X, GDDR7, mid-spec HBM and eSSD</strong>. The growth of China's AI can lower the HBM mix, but it is an upside factor for total DRAM bit demand. \[Inference: China architecture\]

### ⑥ When Usage Growth Outpaces Efficiency Gains

Total memory demand is `total workload × memory usage per task`. Even if usage per task falls 40%, if AI usage doubles, that is <strong>2.0 × 0.6 - 1 = +20%</strong>. The most important variable right now is not the pace of model-efficiency improvement but <strong>the elasticity of token and agent usage in response to falling prices</strong>. This is the condition under which efficiency gains become a market-expanding factor rather than a demand-reducing one. \[Inference: Jevons effect\]

---

## 5. Six Risks of a Downside Miss

### ① AI CAPEX Fails to Prove Its ROI (the Biggest Downside)

If data center investment does not convert into AI revenue and cash flow, hyperscalers could cut orders in 2027-2028. The most dangerous point is specifically 2028, when supply actually increases.

```text
AI CAPEX slowdown + Samsung P5/Micron ID2/SK P&T7 coming online
→ Simultaneous decline in HBM ASP and commodity DRAM prices
```

### ② Inference-Efficiency Gains Overwhelm Usage Growth

Quantization, MoE, KV cache compression and reuse, small specialist models, memory tiering and speculative decoding all lower memory requirements per accelerator. If usage per task falls 60% while workload rises 30%, that is <strong>1.3 × 0.4 - 1 = -48%</strong>. In this case, even as token usage rises, new HBM and server demand comes in below expectations. \[Inference: efficiency-dominant scenario\]

### ③ Rising Accelerator Utilization and Recycled Secondhand Compute

AI data centers today are being built quickly, and utilization optimization is not yet sufficient. If scheduling and inter-cloud compute trading improve, effective compute supply rises even without new GPUs. This does not eliminate demand, but it delays the timing of new server installations.

### ④ Power, Grid and Cooling Bottlenecks

Even with chip and memory orders in hand, installation is delayed if power is not connected. This is closer to <strong>demand deferral</strong> than demand destruction, but for memory makers it shows up as rising inventory and price adjustments.

### ⑤ PC and Smartphone Demand Destruction

If memory prices rise too far, finished-product prices rise and device sales fall. This is the direct reason Chairman Chey Tae-won has argued for expanding supply. In order of impact, it runs <strong>mobile LPDDR > PC DDR > server DDR > HBM</strong>. Samsung Electronics is the most sensitive on an absolute-volume basis, while SK Hynix, with its higher HBM mix, is relatively more defensive.

### ⑥ Rising China Supply

If CXMT rapidly expands DDR5 and LPDDR5X, commodity DRAM prices come under pressure before HBM does. In order of impact, it runs <strong>DDR4/LPDDR4X > DDR5/LPDDR5X > GDDR > SOCAMM > HBM</strong>. Even if HBM demand holds up, commodity DRAM profit could slow first.

---

## 6. When Supply Actually Loosens: The Substance of Chairman Chey's Expansion Argument

Strong demand does not guarantee a rising stock price. What matters is supply and price. Chairman Chey Tae-won's expansion remarks matter precisely on this point.

### The Precise Definition of "Relief"

The `2028 supply relief` that several earlier analyses referenced <strong>does not mean falling prices or the start of oversupply</strong>. The precise definition is this.

- Lead times shorten
- Customer allocation volumes increase
- Contract-price growth decelerates
- The supply growth rate converges toward the demand growth rate

### Chey's Logic Is Market-Preserving Expansion

Chairman Chey's logic is not a price war. It is market preservation.

```text
Memory prices spike
→ PC/smartphone prices rise
→ Finished-product demand falls
→ Memory market volume shrinks
→ Customers turn to in-house chips, substitute memory and new suppliers
→ Long-term damage to the market value of the existing three companies
```

Indeed, Omdia projected that, driven partly by rising memory prices, 2026 PC shipments would fall 12% and smartphone shipments would fall 7%. \[Fact: Omdia\] The argument that pushing prices up for too long eventually costs memory makers volume is a reasonable one.

Still, two statements need to be kept separate. <strong>That 2027 supply shortages could be worse than in 2026</strong> is a fact, and <strong>that new US fabs must be built</strong> is an inference. SK Hynix CEO Kwak Noh-jung has also said that demand could exceed supply capacity into 2030 and beyond, and Omdia sees meaningful supply relief only from late 2027 onward. \[Fact: SK Hynix CEO, Omdia\]

### Supply Growth-Rate Assumptions

Converting site-by-site ramp schedules into effective bit supply gives roughly this. \[Inference: own conversion\]

| Year | Estimated DRAM bit supply growth | Key basis |
|---|---:|---|
| 2026 | +20-24% | Process shrink, M15X, Pyeongtaek, Micron 1γ |
| 2027 | +22-26% | Yongin Fab 1 early ramp, Idaho ID1, Tongluo |
| 2028 | +25-30% | Samsung P5, Micron ID2, SK P&T7/Indiana |

Under the base demand case, the 2028 supply growth rate starts to exceed the demand growth rate by roughly 5-9 percentage points. But if new-fab yield and customer qualification slip, that gap disappears. <strong>Through 2027, a window is possible in which prices stay high even though supply has expanded.</strong> That is because new DRAM wafers get absorbed first by HBM's heavy wafer consumption. \[Inference\]

---

## 7. Memory Layers Compete for the Same Wafer

This is the physical core of the issue. HBM, DDR, LPDDR and GDDR <strong>compete for use of the same leading-edge DRAM wafer capacity</strong>. NAND runs on a separate process and separate fabs.

```text
Leading-edge DRAM wafer ─┬─ HBM core die ────┐
                         ├─ Server DDR5       │
                         ├─ LPDDR5X/SOCAMM2   ├─ (HBM) TSV/stacking/packaging/test ─ Finished HBM4/4E
                         └─ GDDR7             │
Leading-edge logic process ── HBM4 base die ──┘
NAND wafer fab ── Enterprise SSD (separate track)
```

Micron has explained that, on an equal-bit basis, HBM3E consumes about <strong>3x</strong> as many wafers as DDR5, and that this ratio could rise further with HBM4. SK Hynix has likewise confirmed that TSV enlarges die area and adds yield and packaging complexity, so HBM requires more wafers than commodity DRAM. \[Fact: Micron, SK Hynix\]

### Supply and Price Impact by Layer

| Memory layer | Primary demand | Supply bottleneck | Order of capacity-expansion effect | Price resilience |
|---|---|---|---|---|
| HBM4/HBM4E | AI GPU/ASIC | Leading-edge DRAM, base die, TSV, stacking, qualification | Slowest | Highest |
| SOCAMM2 | AI server CPU memory | 1c LPDDR5X, module/server qualification | Medium | High |
| Server DDR5 | CPU/AI server systems | Leading-edge DRAM wafers | Faster than HBM | Medium-high |
| Mobile LPDDR5X | Smartphones/on-device AI | Leading-edge DRAM, mobile elasticity | Fast | Medium |
| DDR4/LPDDR4X | Legacy PC/mobile/industrial | Reduced production at all three makers | Short regardless of expansion | Polarized |
| GDDR7 | GPU/low-cost AI accelerators | Leading-edge DRAM, GPU qualification | Medium | Medium-high |
| NAND/eSSD | AI data storage/KV cache | NAND wafers, controllers | Separate from DRAM | Medium |

There is one interesting twist. TrendForce analysis found that in Q1 2026, revenue and margin per wafer for DDR5 64GB RDIMM overtook HBM's. Producing only HBM is not always optimal, and if prices rise enough, makers have an incentive to shift wafers back to DDR5. <strong>The first mechanism that brings prices down may be normalization of existing wafer allocation rather than new fabs.</strong> \[Inference: wafer-allocation logic\]

---

## 8. Company- and Site-by-Site Expansion Map

What matters is not the announced expansion figure but <strong>when, where and for which product pure DRAM wafer capacity actually increases</strong>. \[Fact: company announcements and disclosures\]

| Company/Site | Role | Schedule | Directly affected products | Investment read |
|---|---|---:|---|---|
| SK Cheongju M15X | Leading-edge DRAM front-end | 2026 ramp-up | HBM core/DDR5/LPDDR | Fastest volume increase |
| SK Cheongju M15 | TSV capacity expansion | In progress | HBM | Combines with M15X |
| SK Cheongju P&T7 | WLP/wafer test | WT October 2027, WLP February 2028 | HBM packaging | 2028 bottleneck relief |
| SK Yongin Fab 1 | New wafer fab | Target completion May 2027 | Leading-edge DRAM (estimated) | Mass production lags completion |
| SK Indiana | Advanced HBM packaging | H2 2028 | Next-generation HBM | Not a wafer capacity increase |
| SK Cheongju M17 | NAND front-end | Undisclosed | NAND/eSSD | Separate from HBM |
| Samsung Pyeongtaek (existing) | 1c DRAM/HBM4 | Currently in production | HBM4/DDR5 | Targets 3x 2026 HBM revenue |
| Samsung Pyeongtaek P5 | New HBM core site | Target start-up 2028 | HBM/leading-edge DRAM | Supply expansion from 2028 onward |
| Samsung Onyang/Cheonan | HBM packaging/test | Undisclosed | HBM4/4E | Onyang plans 5 lines |
| Micron Hiroshima | 1γ EUV DRAM | Already ramping | HBM4E/DDR5/LPDDR | Leading-edge cost improvement |
| Micron Taiwan/Tongluo | DRAM front-end | Mid-2027 | HBM/DDR/LPDDR | First meaningful new volume |
| Micron Singapore | HBM packaging | H1 2027 | HBM | Packaging bottleneck relief |
| Micron Idaho ID1/ID2 | New DRAM fab | Mid-2027 / first wafers late 2028 | Leading-edge DRAM | US supply-chain premium |
| Micron Virginia | Legacy DRAM | 2026 | DDR4 | Long-lived industrial/defense demand |

SK's P&T7 is a dedicated HBM WLP and test facility worth about KRW 19 trillion, and Indiana is a $3.87bn HBM packaging facility. Samsung has designated Pyeongtaek P5 as its 2028 HBM hub and announced 5 lines at Onyang plus modernization at Cheonan. The KRW 140 trillion figure for the Chungcheong region, however, is a <strong>group-wide total</strong> that also includes displays, batteries and substrates, so it should not be read as an HBM investment figure. \[Fact: company announcements\]

### When Supply Actually Loosens

| Period | Supply change | Price impact |
|---|---|---|
| 2026 | Existing fab conversions; M15X, Pyeongtaek and Micron leading-node ramps | Rising HBM keeps eating into DDR supply |
| 2027 | Yongin Fab 1, Idaho ID1, Tongluo, Singapore packaging | Partial DDR5/LPDDR normalization possible |
| 2028 | Samsung P5, SK P&T7/Indiana, Micron ID2 | HBM shortage relief begins |
| 2029-2030 | New fabs reach normal yield, additional US/Honam investment | Oversupply risk if AI demand slows |

<strong>The 2026-2027 memory-shortage outlook is not undermined.</strong> The real oversupply risk sits in 2028-2030, when new fabs reach normal yield at the same time.

---

## 9. Signals to Watch

These are the key indicators for judging whether demand runs above or below this framework.

| Indicator | Demand-beat signal | Demand-miss signal |
|---|---|---|
| AI server shipments | YoY +25% or more | +15% or less |
| HBM bit demand | Sustained +60% or more | +40% or less |
| HBM wafer share | Above 30% in 2027 | 27% or below |
| AI ASIC demand | TPU/Trainium/Meta ASIC all rising together | Growth limited to NVIDIA substitution |
| Hyperscaler CAPEX | Further upward revisions | Downward revisions at 2 or more companies |
| HBM contracts | Expanded 2028 volume pre-contracting | Shortened contract terms, price renegotiation |
| DDR5 RDIMM | Price and volume rising together | Two consecutive quarters of decline |
| SOCAMM2 | Adoption across multiple CSPs/CPU platforms | Dependence on a single platform |
| Power/data-center schedule | Installation accelerating | Grid connection/completion delays |
| Days of inventory | Customer inventory stable | Inventory growing faster than revenue |

---

## 10. Investment Judgment: Samsung, SK Hynix and Micron

The local-DB reference date is 2026-07-16 for Samsung Electronics and SK Hynix, and 2026-07-17 for Micron.

| Company | Current price | FY27/Next-FY PER | Positive effect of expansion | Key risk |
|---|---:|---:|---|---|
| Samsung Electronics | KRW 255,000 | 3.88x | HBM share recovery, the broadest product mix | Sensitivity to commodity DRAM prices |
| SK Hynix | KRW 1,842,000 | 4.20x | HBM/SOCAMM exposure purity and utilization leverage | Heavy CAPEX and post-2028 ROIC |
| Micron | $848.95 | 5.64x | US localization, simultaneous HBM/DDR/eSSD growth | High-cost US fabs, relative multiple premium |

\[Fact: local DB prices and consensus\]

These PERs are not a "cheap" signal. They are <strong>the market's discount for the possibility that 2027 earnings are the peak</strong>. A low 2027E PER of 4-6x means the market has already priced in peak earnings and 2028 normalization.

Ranked by capability, it looks like this. \[Inference: relative ranking\]

- 2026-2027 earnings leverage: <strong>SK Hynix > Micron > Samsung Electronics</strong>
- Room for estimate upgrades from HBM share recovery: <strong>Samsung Electronics > Micron > SK Hynix</strong>
- Defensiveness against post-2028 oversupply: <strong>Samsung Electronics > Micron > SK Hynix</strong>
- Stock-price leverage if the HBM shortage persists through 2030: <strong>SK Hynix > Micron > Samsung Electronics</strong>

### Scenario-by-Scenario Conclusion

- <strong>If demand beats</strong>: SK Hynix has the largest upside, Samsung Electronics has the largest estimate-upgrade leverage
- <strong>Base scenario</strong>: Samsung Electronics has the risk-adjusted edge, SK Hynix is a Core Hold
- <strong>If demand misses</strong>: Samsung Electronics is relatively defensive, SK Hynix and Micron see wider earnings downgrades
- <strong>Thesis-invalidation condition</strong>: if the 2027 HBM bit demand outlook drops below +40% at the same time that hyperscaler CAPEX is cut and customer inventory rises

### What the Stock Reaction Says

| Ticker | 7/15 | 7/16 | Latest close |
|---|---:|---:|---:|
| Samsung Electronics | +6.27% | -8.77% | KRW 255,000 |
| SK Hynix | +8.83% | -11.53% | KRW 1,842,000 |
| Micron | -8.02% | -5.65% | $848.95 |

Samsung and Hynix both rose on the day of Chairman Chey's remarks and then fell sharply the next day, which makes it <strong>hard to argue that his remarks were the direct catalyst for selling</strong>. The July 16 sell-off also involved Kimi K3, concerns about AI CAPEX returns, the CXMT IPO, and position unwinding after the preceding sharp rally. \[Inference: multiple factors\]

---

## Closing

Coming back to the question, the answer is this. AI memory demand is likely to meet or exceed today's high expectations (strong growth at 80%). But exceeding them by a wide margin is not yet the base scenario (a beat at 35%).

The most likely path looks like this. The HBM shortage persists through 2027, demand spreads into SOCAMM, DDR5 and eSSD, and new capacity grows in 2028 without immediately flipping into oversupply. From 2028 onward, AI CAPEX's actual profitability and the supply growth rate need to be re-verified.

The core of the investment view is not "HBM grows." The market already knows that. <strong>The real asymmetric alpha lies in whether demand spreads from HBM into server DDR, SOCAMM and eSSD, and whether its duration extends past 2028.</strong>

Chairman Chey's expansion logic makes industrial sense. Protecting the customer market and the bounds of political tolerance serves long-term corporate value better than maximizing today's price. For investors it cuts both ways. Through 2027 it is a bullish signal confirming a severe supply shortage. From 2029 onward it is a bearish signal foreshadowing the normalization of CAPEX, depreciation and ASP. That is not a reason to sell now, but it also weakens the case for valuing the three memory makers as permanently high-margin businesses.

So <strong>the current conclusion is to hold the shortage thesis through 2027 and re-verify from 2028</strong>. The condition for the stock's next leg up is not 2027 earnings growth, but evidence that 2028 earnings do not roll over.

---

_This post is a supply-demand and investment analysis compiled from public forecasts (TrendForce, Omdia), company announcements and disclosures (Micron, SK Hynix, Samsung Electronics), and local DB prices and consensus. The demand-scenario probabilities, supply growth rates and the 2027 base model are the author's own estimates as of the time of writing, not an official consensus. Per-fab monthly wafer input volumes, product-by-product wafer allocation ratios, HBM long-term contract prices and volumes, and new US fab schedules cannot be confirmed from public materials. The stocks mentioned are examples used to illustrate industry structure, not a recommendation to buy or sell any specific stock. Investment decisions and their outcomes are the sole responsibility of the investor._

---

### Related Posts

- [HBM 2030 Supply-Demand Deep Research: Dissecting the 26.7EB Demand Model Against the Capacity Schedule](/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
- [Are Semiconductors Cyclical, and What Is Fair Value? Pricing Samsung, SK Hynix and Micron with FCFE and Normalized Earnings](/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [The Real Debate in Semiconductors: Four Physical Clocks and One Stock-Price Clock](/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [China's Memory Localization and Korea: Decomposing Samsung, SK Hynix and Micron's China Exposure from Disclosures](/post/china-memory-localization-exposure-samsung-hynix-micron-2026-07-18/)
- [SK Hynix Q2 Earnings Cut but Target Prices Held: Synthesizing the Mirae Asset and KIS Reports](/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/)
