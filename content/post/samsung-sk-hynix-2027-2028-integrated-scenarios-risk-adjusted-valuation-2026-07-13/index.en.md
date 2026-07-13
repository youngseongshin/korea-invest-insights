---
title: "2028 Matters More Than the 2027 Boom: Integrated Scenarios for Samsung Electronics & SK Hynix"
description: "Starting from a 2027 memory boom base case, this analysis layers in 2028 supply expansion, inference efficiency gains, and AI infrastructure refinancing risk. We compare Samsung Electronics and SK Hynix on a probability-weighted basis across scenario EPS, fair-value PER, and present value, and examine how HBM long-term contracts and Chinese memory capacity expansion reshape earnings duration."
date: 2026-07-13T20:39:17+09:00
lastmod: 2026-07-13T20:39:17+09:00
categories: ["Exclusive Analysis", "Semiconductors", "Macro"]
tags:
  - "Samsung Electronics"
  - "SK Hynix"
  - "HBM"
  - "Memory Semiconductors"
  - "AI Infrastructure"
  - "Scenario Analysis"
  - "Valuation"
  - "CXMT"
  - "YMTC"
series: ["exclusive-analysis", "ai-hbm-2026"]
slug: "samsung-sk-hynix-2027-2028-integrated-scenarios-risk-adjusted-valuation-2026-07-13"
image: "/images/posts/samsung-hynix-2027-2028-scenario-map-2026-07-13.png"
valley_cashtags:
  - 삼성전자
  - SK하이닉스
draft: false
---

> Related context: This post is a follow-up to the [HBM 2030 Supply-Demand Model Cross-Check](/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/), [Samsung Electronics & SK Hynix Valuation Through 2028E Earnings](/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/), and the [July 13 AI Hardware Selloff Analysis](/post/kospi-9pct-selloff-ai-hardware-derating-korea-leverage-2026-07-13/). Accepting 2027's boom as the baseline, it quantifies the probability that supply, efficiency, and financing conditions shift simultaneously beginning in 2028.

## TL;DR

- HBM supply/demand is likely to remain tight through 2027. However, the projection of `2030 demand 26.7EB vs. supply 10.6EB, 2.52× deficit` is not a base-case forecast — it requires multiple bullish assumptions to hold simultaneously.
- The most important year is not 2027 but <strong>2028</strong>. Supply expansion from Samsung Electronics, SK Hynix, and Micron, inference efficiency gains, and refinancing verification across AI data centers all converge in the same window.
- HBM long-term supply contracts extend earnings duration but do not eliminate the cycle. They convert price risk into contract renewal risk, customer credit risk, product-mix risk, and repricing risk.
- Conditional probabilities: P1 sustained excess demand 35%, P2 localized credit stress with hyperscaler re-concentration 40%, P3 efficiency gains and supply normalization 15%, P4 systemic credit seizure 10%.
- Probability-weighted EPS for 2027: Samsung Electronics 60,750원, SK Hynix 393,000원. For 2028: Samsung 49,900원, SK Hynix 316,000원.
- Present value of 2028 terminal values discounted at 11% annually: Samsung Electronics 317,246원, SK Hynix 1,956,316원 — implying 24.7% and 6.0% upside respectively to the July 13 KRX closing prices. Once 2028 normalization risk is incorporated, Samsung's margin of safety is wider; SK Hynix is more sensitive to whether P1 holds.

<div class="thesis-callout">
  <div class="thesis-callout__label">Bottom Line</div>
  <div class="thesis-callout__body">
    The 2027 boom is relatively visible. The harder question is <strong>whether high HBM pricing and earnings persist through 2028 and beyond</strong>. Current prices discount the duration of earnings well beyond the 2027 peak.
  </div>
</div>

![Integrated 2027–2028 Scenario Map for Samsung Electronics and SK Hynix](/images/posts/samsung-hynix-2027-2028-scenario-map-2026-07-13.png)

## 1. Analytical Questions and Evidence Quality

This analysis ties three questions together in a single framework.

1. How much confidence can we place in the view that HBM supply/demand will remain tight through 2027?
2. If supply, efficiency, and financing conditions change simultaneously in 2028, how do Samsung Electronics' and SK Hynix's earnings differ across scenarios?
3. Given those changes, at what implied earnings level does the current share price trade?

The numbers in this report must be read by category.

| Category | Definition | Example in This Report |
|---|---|---|
| Fact | Verified from public filings or market data | July 13 KRX closing prices, Oracle FCF, CoreWeave borrowings |
| Consensus | Aggregated market estimates | 2027–2028 EPS and net income |
| Broker estimate | Individual broker forecast | Korea Investment & Securities and BNK Investment & Securities SK Hynix EPS |
| Model output | Derived from disclosed formulas and assumptions | P1–P4 probability-weighted EPS and present values |
| Analyst judgment | Non-statistical analytical judgment | Scenario probabilities, fair PER, 11% required return |
| Blocked | Cannot be determined from public sources alone | HBM contract-level pricing, customer-by-customer volumes, actual production yield |

Core formulas are as follows.

```text
Scenario Terminal Value = Scenario EPS × Scenario Fair PER
Probability-Weighted EPS = Σ(Scenario Probability × Scenario EPS)
Probability-Weighted Terminal Value = Σ(Scenario Probability × Scenario Terminal Value)
Present Value = Terminal Value ÷ (1 + 11%)^Remaining Years
HBM Need/Fleet = Installed and active HBM demand stock ÷ supply capacity that can be served by installed fleet
```

Scenario probabilities are not derived from historical frequency distributions. They are conditional judgments reflecting currently observable demand, supply, efficiency, and financing conditions. Fair PER values are likewise not mechanically observed from the market but are analytical estimates incorporating earnings durability, business concentration, financial structure, and long-term risk.

## 2. Current Price and Market Consensus

July 13 KRX closing prices and consensus estimates aggregated on the same date are used throughout.

| Item | Samsung Electronics | SK Hynix |
|---|---:|---:|
| 2026-07-13 KRX Closing Price | 254,500원 | 1,845,000원 |
| 2027 Consensus EPS | 65,802원 | 444,359원 |
| 2028 Consensus EPS | 65,907원 | 433,625원 |
| 2027 Consensus Net Income | 44.3조원 | 32.4조원 |
| 2028 Consensus Net Income | 44.1조원 | 31.9조원 |
| Current Price / 2027 Consensus EPS | 3.87× | 4.15× |
| Current Price / 2028 Consensus EPS | 3.86× | 4.25× |

On the surface, both companies look remarkably cheap. But these low PER multiples do not mean the market is unaware of 2027 earnings — they are more likely a signal that the market doubts the durability of earnings beyond 2028.

The dispersion among SK Hynix estimates illustrates this clearly.

| Source | 2027 EPS | 2028 EPS | Interpretation |
|---|---:|---:|---|
| Market Consensus | 444,359원 | 433,625원 | Moderate 2028 normalization |
| Korea Investment & Securities | 415,254원 | 495,696원 | Earnings growth continues through 2028 |
| BNK Investment & Securities | 214,642원 | 66,989원 | Rapid peak passage after 2027 |

For the same company, 2028 EPS estimates range from 66,989원 to 495,696원. The divergence stems not from 2026 demand forecasts but from differing assumptions on <strong>2028 HBM average selling prices, the pace of supply expansion, and the duration of AI capex</strong>.

Recalculating current PER using this report's probability-weighted EPS:

| Year | Samsung Electronics | SK Hynix |
|---|---:|---:|
| 2027 | 4.19× | 4.69× |
| 2028 | 5.10× | 5.84× |

Applying the probability-weighted fair PER in reverse to the current share price, the implied EPS the market is pricing in is approximately 31,700원 for Samsung and approximately 245,000원 for SK Hynix — roughly 52% and 45% below the respective 2027 consensus. The market is discounting not 2027 earnings per se, but how long those earnings will last.

## 3. What Has Changed in the Memory Cycle — and What Hasn't

### What Has Changed

1. AI servers, HBM, and enterprise SSDs have raised the share of enterprise and data-center demand in the total mix.
2. HBM requires customer qualification, advanced packaging, yield ramps, and long-term contracts, making short-run supply response slower than for commodity DRAM.
3. As HBM absorbs a growing share of wafer starts, commodity DRAM output from the same fabs declines, which can support commodity DRAM pricing.
4. Financing by large cloud providers and AI data center operators front-loads actual memory orders, acting as an accelerant.
5. Conversely, when credit problems emerge, demand does not fade gradually — it can step down abruptly through contract renegotiations and investment deferrals.

### What Has Not Changed

1. High prices ultimately invite new fabs, yield improvement, process-node transitions, and competitor capacity additions.
2. High HBM pricing and margins increase the incentive for a second-source supplier to enter and for customers to apply cost-reduction pressure.
3. Long-term contracts do not eliminate price risk — they convert it into renewal pricing and customer credit risk.
4. Simultaneously applying peak EPS to a high PER is a double-optimism error that counts both earnings and multiples at their most favorable.

The claim that HBM has made memory a better business than legacy DRAM, and the claim that the memory cycle has been abolished, are not the same assertion.

## 4. HBM Supply-Demand Model and the 2028 Inflection

In the [HBM 2030 Supply-Demand Model Cross-Check](/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/), we reproduced the original model's `demand 26.7EB, supply 10.6EB, 2.52× deficit` in consistent units. The formula itself does not incorrectly compare a demand flow against a supply stock. The issue is that long-horizon assumptions multiply together in series.

These include:
- Monthly token consumption growth
- Model size, context length, and agent state expansion
- KV cache and memory residency ratios
- Throughput, quantization, and routing efficiency
- HBM service life and migration of inference workloads to other memory types
- Achievable production volumes and packaging yield across the three major memory makers

For this reason, the 2030 2.52× deficit is best treated as a bullish stress scenario rather than a base case. Re-deriving central assumptions aligned to each of P1–P4 gives the following:

| Path | Token Multiplier | Model Scale | Throughput Efficiency | KV Efficiency | HBM Residency | Demand | Need/Fleet |
|---|---:|---:|---:|---:|---:|---:|---:|
| P1 Orderly Excess Demand | 20× | 4.0× | 12× | 5.0× | 65% | 16.1EB | 1.52× |
| P2 Localized Credit Stress & Re-concentration | 18× | 3.5× | 12× | 5.5× | 60% | 12.8EB | 1.21× |
| P3 Efficiency Gains & Supply Expansion | 12× | 2.0× | 14× | 6.0× | 50% | 6.5EB | 0.62× |
| P4 Systemic Credit Seizure | 8× | 2.0× | 14× | 7.0× | 45% | 2.6EB | 0.25× |

For comparability, supply capacity is held fixed at 10.6EB. Actual HBM wafer starts, product mix, good-die yield, and packaging capacity are non-public, so absolute values cannot be confirmed.

Looking along the time axis, the judgment simplifies considerably.

| Period | Assessment | Confidence |
|---|---|---|
| 2026–2027 | HBM4 transition and AI demand outpace new-fab supply additions | High |
| 2028 | SK Hynix Yongin Line 1, Micron ID1/Tongluo, and Samsung HBM expansion begin easing supply | Medium-High |
| 2029–2030 | Remaining deficit is more likely to narrow than to deepen | Medium |
| 2030 2.5× deficit | Requires multiple bullish assumptions to hold simultaneously | Low |

The investment decision does not therefore hinge on whether the 2027 boom occurs. The pivot is whether the additional supply coming online in 2028 clears customer qualifications, and whether that timing coincides with inference efficiency gains and tighter AI data center financing.

## 5. SK Hynix Long-Term Contracts and the Earnings Curve

Korea Investment & Securities' July 13 SK Hynix report attributes the Q2 consensus miss not to demand collapse but to a timing lag in how HBM product-mix shifts and long-term supply contract pricing flow through to reported results.

| Item | 2026F | 2027F | 2028F |
|---|---:|---:|---:|
| Revenue | 32.83조원 | 48.77조원 | 58.53조원 |
| Operating Profit | 24.51조원 | 37.45조원 | 44.70조원 |
| EPS | 292,068원 | 415,254원 | 495,696원 |
| ROE | 94.5% | 65.4% | 46.5% |

HBM assumptions are also aggressive.

| HBM Metric | 2026F | 2027F |
|---|---:|---:|
| Bit Growth | +23.0% | +31.2% |
| ASP | $1.60/Gb | $2.82/Gb |
| ASP Growth | -2.5% | +76.3% |
| Revenue | 3.71조원 | 8.30조원 |
| Revenue Growth | +28.0% | +123.6% |

Key estimate adjustments within the report include:

- HBM4 sales begin in Q3 2026, but the largest earnings inflection is modeled in Q4 when HBM ASP rises `+52% QoQ`.
- Compared to the May estimates, non-HBM DRAM ASP for 2026–2027 was trimmed by approximately 16%.
- 2026 HBM revenue was raised by 17%.
- 2027 HBM shipment volume was held flat while ASP was cut by 5%.
- NAND shipment volumes and pricing were raised.

This report is not a retraction of the long-term HBM growth thesis. It is a revision that lowers short-run commodity DRAM price elasticity and pushes back the point at which HBM4 economics enter reported results.

### Why Long-Term Contracts Should Not Be Taken at Face Value

1. Contract-level price floors, ceilings, minimum purchase obligations, and prepayment terms are not publicly disclosed.
2. Reports that contracts carry "no price ceiling" cannot by themselves confirm that prices rise every year — one must know whether pricing is linked to spot rates and how often it is reset.
3. Long-term contracts lock in volumes and customer relationships but do not eliminate the risk of customer renegotiation, default, or credit deterioration.
4. Non-HBM DRAM and NAND outside those contracts remain fully exposed to the commodity price cycle.
5. If HBM4 yield is low, SK Hynix's shipments and incremental earnings may still fall short even if the market remains undersupplied.

The largest benefit of long-term contracts is not cycle elimination but <strong>extending earnings duration and converting the form of risk</strong>.

## 6. How AI Infrastructure Financing Flows Into Memory Orders

AI memory demand is not driven purely by technology pull. Data center operators' financing activity creates front-loaded orders, and when financial conditions tighten, order gaps can emerge sharply.

```text
Rising AI Expectations
  -> Cloud/AI data center investment and long-term contract expansion
  -> Front-loaded capex in GPU, HBM, power, and data centers
  -> Asset, revenue, and enterprise value appreciation
  -> Additional debt and equity financing
  -> Larger capex programs

Reverse direction
Monetization delay or higher refinancing costs
  -> Contract renegotiation / expansion delays
  -> Memory order gaps
  -> ASP and share price decline
  -> Collateral value and financing conditions deteriorate
  -> Further capex reduction
```

The numbers confirmed from public disclosures are substantial.

| Item | Confirmed Value | Interpretation |
|---|---:|---|
| Oracle FY2026 Free Cash Flow | -$23.7B | Large-scale AI capex exceeds cash generation |
| Oracle Debt Financing | $43B | Heavy external funding for AI investment |
| Oracle Equity Financing | $5B | Debt alone is insufficient to cover investment |
| Oracle RPO | $638B | Long-term contracts provide high revenue visibility |
| Oracle Customer Prepayments & Direct GPU Provision | $75B | End customers share investment risk |
| CoreWeave Total Debt (End 2025) | $21.6B | High financial leverage in AI data centers |
| CoreWeave New DDTL 4.0 | $8.5B | Additional financing to continue expansion |
| CoreWeave DSCR Threshold | Minimum 1.15× | Full refinancing verification begins no later than after June 30, 2027 |

CoreWeave's end-2025 detailed borrowings comprised DDTL 2.0 approximately $5.04B, DDTL 2.1 approximately $2.74B, DDTL 1.0 approximately $1.55B, DDTL 3.0 approximately $0.34B, and equipment/software finance leases approximately $4.17B. DDTL 4.0, signed in March 2026, totals $8.5B.

These figures do not imply that AI demand is fictitious. The contracts, GPUs, power infrastructure, and data centers are real. However, if cash flow fails to keep pace with financing costs in 2027–2028, weaker operators are likely to sell assets to be absorbed by large cloud providers.

This is why the probability assigned to <strong>P2 — localized stress followed by asset re-concentration among hyperscalers</strong> — exceeds that of P4 systemic collapse. In P2, memory orders do not disappear but a gap of one or more quarters is plausible.

## 7. P1–P4 Conditional Probability Tree

Final probabilities are derived by sequencing `real demand → financial verification → supply/efficiency → asset absorption`, not from historical memory cycle frequencies.

```text
2028 AI Monetization and Refinancing Verification
  Pass 50%
    ├─ P1 Sustained excess demand 70%        = 35%
    └─ P3 Efficiency/supply normalization 30%   = 15%
  Stress 50%
    ├─ P2 Localized stress/re-concentration 80%   = 40%
    └─ P4 Systemic credit seizure 20%        = 10%
```

The 50/50 first branch is not a statistical prior. It is a neutral starting point reflecting the fact that real demand and contracts are strong but financial verification is not yet complete. Calculating probabilities to single percentage-point precision from current data would produce false precision — adjustments are made only in 5-percentage-point increments.

### Evidence Supporting Verification Pass vs. Financial Stress

| Evidence Supporting Verification Pass | Evidence Supporting Financial Stress |
|---|---|
| HBM mass-production ramp timing lag through 2027 | Oracle FY2026 FCF -$23.7B, debt financing $43B |
| Oracle RPO $638B, customer prepayments and direct GPU provision $75B | CoreWeave total debt $21.6B, new DDTL $8.5B |
| HBM long-term contracts and prepayments raise order visibility | CoreWeave DSCR 1.15× verification after mid-2027 |
| Large cloud providers' actual data center investment | Rising risk premium on long-dated AI bonds |

The 70/30 split between P1 and P3 on the verification-pass branch reflects the fact that through 2027, qualification, yield, and packaging bottlenecks remain, while memory-side MoE, MLA, KV compression, routing, and offloading can all scale simultaneously from 2028 onward.

The 80/20 split between P2 and P4 on the stress branch is also clear. GPUs and data centers are not assets that disappear — hyperscalers with strong cash flow can acquire and redeploy them. Because simultaneous capex pullbacks, multiple covenant breaches, and HBM long-term contract impairments have not yet materialized together, P4 is treated as a tail risk at 10%.

### Evidence Ledger

| Evidence | P1 | P2 | P3 | P4 | Assessment |
|---|---:|---:|---:|---:|---|
| HBM supply lag through 2027 | ++ | + | - | -- | Shortage persists |
| Top-3 memory supply expansion post-2028 | - | 0 | ++ | 0 | P3 independent pathway |
| CXMT client DDR5/LPDDR expansion | - | - | ++ | 0 | Caps commodity price ceiling before HBM |
| YMTC high-layer NAND ramp and customer adoption | - | - | ++ | 0 | Pressure on Samsung NAND and enterprise SSD mix first |
| China HBM/server memory customer qualification | -- | - | ++ | 0 | If confirmed, shifts from P1 to P3 |
| Oracle RPO & customer-provided GPU | + | + | 0 | - | Demand is real; buffers contagion |
| Oracle negative FCF & large financing | - | ++ | 0 | + | Localized credit stress risk |
| CoreWeave debt & DSCR verification | - | ++ | 0 | + | 2027–2028 financial inflection |
| Rising AI long-dated bond risk premium | -- | ++ | 0 | + | Shifts 5pp from P1 to P2 |
| Inference efficiency gains & offloading | - | 0 | ++ | 0 | Still insufficient production-level evidence |
| Hyperscalers' asset absorption capacity | 0 | ++ | 0 | -- | Why P2 outweighs P4 |

`++` and `--` denote direction only and are not statistical likelihood ratios.

### Probability Revision History

| Step | P1 | P2 | P3 | P4 | Rationale |
|---|---:|---:|---:|---:|---|
| Initial | 40% | 35% | 15% | 10% | Physical supply shortage dominance, localized financial risk, supply/efficiency path |
| AI long-duration bond weakness reflected | 35% | 40% | 15% | 10% | P1 to P2 shift of 5pp; no contagion evidence |
| Hyperscaler capex review | 35% | 40% | 15% | 10% | Demand execution and asset concentration effects offset |
| AI long-term scenario review | 35% | 40% | 15% | 10% | 2027–2028 unchanged; only post-2030 P3 probability expands |
| China supply path review | 35% | 40% | 15% | 10% | Commodity supply risk reflected; HBM customer qualification evidence lacking |

### Probability Uncertainty Ranges and Revision Rules

| Path | Central | Uncertainty Range | Strong Signals That Would Shift the Central Estimate |
|---|---:|---:|---|
| P1 | 35% | 25–45% | Two or more hyperscalers raise capex guidance; financing costs stabilize; long-term contracts strengthened |
| P2 | 40% | 30–50% | Single weak-hand operator stress event with hyperscaler asset absorption |
| P3 | 15% | 10–25% | Top-3 or China supply expansion confirmed in volume; per-token HBM consumption declines |
| P4 | 10% | 5–15% | Multiple operator defaults, two or more capex cuts, and long-term contract impairments occur simultaneously |

- A single news article or anecdote warrants only a 0–2pp adjustment.
- A single strong signal from a company filing or earnings report warrants at most a 5pp adjustment.
- Two or more independent strong signals in the same direction warrant a 5–10pp shift.
- Localized credit stress moves probability from P1 to P2; contagion evidence moves it from P2 to P4; supply/efficiency evidence moves it from P1 to P3.

## 8. Final Scenarios and HBM Price Pressure

| Path | Prob. | 2028 State | 2030 Need/Fleet | HBM Price Pressure | Key Outcome |
|---|---:|---|---:|---:|---|
| P1 Orderly Excess Demand | 35% | Tight or balanced | 1.3–1.8× | Flat to -10% | Contract price floor holds; HBM earnings plateau |
| P2 Localized Credit Stress & Re-concentration | 40% | Order gap, modest supply slack | 0.9–1.3× | -15 to -30% | Weak operators exit; hyperscalers absorb assets |
| P3 Efficiency Gains & Supply Expansion | 15% | Growing supply surplus | 0.6–0.9× | -20 to -35% | Token usage grows but HBM premium compresses |
| P4 Systemic Credit Seizure | 10% | Capex cuts and inventory correction | 0.3–0.6× | -40 to -55% | LT contract renegotiation, output cuts, capex cancellations, policy intervention |

Holding all other variables constant, shifting 10 percentage points out of P2 changes the 2028 terminal values as follows:

| Probability Shift | Samsung Terminal Value Change | SK Hynix Terminal Value Change | Meaning |
|---|---:|---:|---|
| 10pp from P2 to P1 | +21,800원 | +227,000원 | Higher probability of sustained undersupply |
| 10pp from P2 to P3 | -7,500원 | -70,000원 | AI economy grows but HBM premium compresses |
| 10pp from P2 to P4 | -16,800원 | -132,000원 | Localized stress contagion to systemic risk |

SK Hynix is more sensitive to every probability shift. Even using the same central probabilities, SK Hynix's valuation error bars and share price volatility are larger due to its higher HBM concentration.

## 9. China Supply Expansion Is a Variable Across All Paths, Not a Separate Scenario

CXMT and YMTC capacity growth is not a fifth scenario independent of P1–P4. It is a supply variable that alters product-level pricing and market share within every path.

| China Progress Stage | Market Affected First | Samsung Electronics | SK Hynix | Scenario Mapping |
|---|---|---|---|---|
| CXMT domestic DDR4/DDR5/LPDDR expansion | Commodity DRAM | ASP and product mix pressure | Relatively limited direct impact | EPS trimmed across all paths; probabilities unchanged |
| CXMT global PC customer qualification | Global client DDR5/LPDDR | ASP ceiling and share pressure simultaneously | Client exposure at risk | P3 upside risk |
| China low-end server RDIMM penetration | Standard server DRAM | Partial server mix pressure | DRAM outside AI servers at risk | P3 upside review |
| YMTC high-layer NAND ramp and customer adoption | Consumer NAND/enterprise SSD | Largest NAND share and margin pressure | Solidigm and enterprise SSD at risk | P3 EPS and multiple reduction |
| China HBM mass production and AI customer qualification | HBM | Partial HBM catch-up offset | Large scarcity premium and share risk | 5–10pp shift from P1 to P3 |
| China ramp and global AI capex slowdown concurrent | All memory | Commodity/NAND/HBM combined pressure | HBM/DRAM combined pressure | Monitor for P3-to-P4 contagion |

In 2026–2027, CXMT is more likely to cap the client DDR5 and LPDDR price ceiling than to directly undermine HBM pricing. YMTC may similarly intensify price competition in consumer NAND and some enterprise SSDs first.

For China to emerge as a direct HBM threat, DRAM die production alone is insufficient. TSV bonding, stacking, base-die integration, advanced packaging, and repeated mass-production qualifications by AI customers are all required.

The following signals must be confirmed before Chinese capacity expansion is incorporated numerically in meaningful quantities:

1. CXMT DDR5/LPDDR is adopted at volume by global PC makers at prices more than 20% below those of the top-3 memory suppliers.
2. CXMT secures qualification beyond consumer PCs into enterprise PCs and server RDIMM.
3. YMTC high-layer NAND is confirmed by actual shipment volumes and enterprise SSD customer wins — not just stated targets.
4. China HBM moves beyond sample qualification to repeated mass-production qualification by AI accelerator customers.
5. Supply growth and commodity DRAM/NAND price declines among the top-3 suppliers are observed together for two or more consecutive quarters.

## 10. Samsung Electronics: EPS and Fair Value by Scenario

| Year | Scenario | EPS | Fair PER | Terminal Value |
|---|---|---:|---:|---:|
| 2027 | P1 | 65,000원 | 8.5× | 552,500원 |
| 2027 | P2 | 62,000원 | 8.0× | 496,000원 |
| 2027 | P3 | 58,000원 | 7.5× | 435,000원 |
| 2027 | P4 | 45,000원 | 7.0× | 315,000원 |
| 2028 | P1 | 68,000원 | 8.5× | 578,000원 |
| 2028 | P2 | 45,000원 | 8.0× | 360,000원 |
| 2028 | P3 | 38,000원 | 7.5× | 285,000원 |
| 2028 | P4 | 24,000원 | 8.0× | 192,000원 |

A base PER above 9× is not assigned to Samsung because foundry loss reduction has not yet been confirmed. An 8.5× P1 multiple becomes achievable only if HBM share recovery, commodity DRAM/NAND pricing, and foundry normalization all operate together.

An 8.0× multiple in P4 is applied to avoid the double-discount error of multiplying a trough EPS by an also-depressed PER. In an actual recession scenario, normalized EPS, net cash, and book value must all be considered together.

## 11. SK Hynix: EPS and Fair Value by Scenario

| Year | Scenario | EPS | Fair PER | Terminal Value |
|---|---|---:|---:|---:|
| 2027 | P1 | 430,000원 | 9.0× | 3,870,000원 |
| 2027 | P2 | 405,000원 | 7.0× | 2,835,000원 |
| 2027 | P3 | 370,000원 | 6.0× | 2,220,000원 |
| 2027 | P4 | 250,000원 | 5.5× | 1,375,000원 |
| 2028 | P1 | 470,000원 | 9.0× | 4,230,000원 |
| 2028 | P2 | 280,000원 | 7.0× | 1,960,000원 |
| 2028 | P3 | 210,000원 | 6.0× | 1,260,000원 |
| 2028 | P4 | 80,000원 | 8.0× | 640,000원 |

The 9× P1 multiple presupposes HBM market share, long-term contract terms, high ROE, and a structural rerating of SK Hynix as a strategic AI asset. Maintaining this multiple through 2028 requires confirmed HBM4E share defense, long-term contract repricing, and shareholder return activity.

Korea Investment & Securities' target price of 3,800,000원 applies a 6.0× PBR to 12-month forward BPS — above the historical band peak of 5.0× cited in the same report. A 3,800,000원 target therefore requires not just earnings delivery but a structural rerating of the memory business.

In P2 and P3, HBM concentration shifts from an advantage to a vulnerability. When ASP falls, earnings and multiples can compress simultaneously.

## 12. Probability-Weighted Results and Risk-Adjusted Comparison

| Year | Company | Prob.-Weighted EPS | Blended Fair PER | Prob.-Weighted Terminal Value | PV at 11% Annual Discount | vs. Current Price |
|---|---|---:|---:|---:|---:|---:|
| 2027 | Samsung Electronics | 60,750원 | 8.04× | 488,525원 | 421,385원 | +65.6% |
| 2027 | SK Hynix | 393,000원 | 7.53× | 2,959,000원 | 2,552,333원 | +38.3% |
| 2028 | Samsung Electronics | 49,900원 | 8.18× | 408,250원 | 317,246원 | +24.7% |
| 2028 | SK Hynix | 316,000원 | 7.97× | 2,517,500원 | 1,956,316원 | +6.0% |

Four observations follow from these results:

1. Viewed through 2027 alone, both companies show risk-adjusted values above current prices.
2. Once 2028 normalization probability is discounted, Samsung's margin of safety is wider.
3. SK Hynix's 2028 present value is only 6% above the current share price. A large portion of expected return depends on P1 holding.
4. Samsung's commodity memory, foundry, and net cash position provide a partial downside buffer in P2 and P3.

What is already well known to the market is HBM undersupply and higher memory pricing. What may be underpriced in two directions:

- If Samsung's HBM catch-up coincides with commodity DRAM/NAND price recovery, both earnings and multiples could improve together.
- If SK Hynix's long-term contracts and HBM4E defend price floors and share even after 2028 supply additions, the current normalization discount may be excessive.

Conversely, the market may prove correct if supply, efficiency, and credit conditions all improve simultaneously in 2028, cutting peak earnings short.

## 13. How to Think About AI Long-Term Demand Beyond 2030

[AI 2040 Plan A](https://ai-2040.com/?choices=plan-a-root) presents a path from approximately 20 million H100e in 2026 to 60 billion H100e by 2034, with AI compute power consumption reaching 5TW by 2034. However, the document itself describes this as a policy scenario, not a best-estimate forecast, and notes that certain variables were adjusted alongside the narrative.

Long-term scenarios are therefore not fed directly into 2027–2028 EPS estimates.

| Period | P1 Excess Demand | P2 Re-concentration | P3 Volume Growth / Price Normalization | P4 Failure | Status |
|---|---:|---:|---:|---:|---|
| 2026–2028 | 35% | 40% | 15% | 10% | Current analysis probabilities |
| Post-2030 conditional baseline | 25% | 35% | 30% | 10% | Long-term judgment; not a statistical probability |

If AI and robotics raise the efficiency of chip design, fab construction, and production, total memory bit demand may grow while the scarcity premium on HBM specifically narrows. <strong>HBM market size expansion and long-term PER expansion must therefore be evaluated separately.</strong>

As long-term memory demand grows, the opportunity set expands not only for HBM but also for commodity DRAM, NAND, enterprise SSDs, controllers, CXL, power, cooling, and interconnects. This is a relative advantage for Samsung, with its broader product portfolio.

## 14. What Needs to Materialize for This Analysis to Hold

### Samsung Electronics

1. HBM4 and HBM4E customer qualifications must convert into actual mass-production volumes and revenue share.
2. Commodity DRAM and NAND contract price recovery must offset HBM investment costs, bonuses, and provisions.
3. Foundry losses must narrow and begin making a meaningful contribution to 2027–2028 earnings.
4. Net cash and shareholder return capacity must be maintained despite heavy capex.

### SK Hynix

1. HBM4E share and long-term contract price floors must hold even as Samsung and Micron expand supply.
2. HBM repricing beginning in Q4 2026 must track toward the 2027 average of $2.82/Gb.
3. TSV and stacking yield weakness must prove temporary and attributable to product transition costs.
4. High free cash flow must flow toward shareholder returns and capital policy, not just capacity expansion.

## 15. Risk Signals and Leading Indicators

| Risk | Leading Indicator | Samsung Impact | SK Hynix Impact | Analysis Adjustment |
|---|---|---|---|---|
| HBM long-term contract renegotiation | Price floor, prepayment, and minimum purchase weakening | Moderate | Very large | P2/P4 up |
| Hyperscaler capex guidance cut | Two or more simultaneous guidance cuts | Large | Very large | P2/P4 up |
| AI data center refinancing event | CoreWeave covenant terms/financing cost, Oracle funding | Moderate | Large | P2 up; P4 up if contagion |
| Accelerated supply expansion | Samsung/Micron volume-capable HBM output rises | Positive for HBM catch-up; negative for pricing | Very negative | P3 up |
| Sharp inference efficiency improvement | Per-token HBM bits decline | Broad product portfolio provides partial buffer | Negative | HBM multiple lower |
| China commodity supply expansion | CXMT/YMTC pricing, share, global customer qualifications | More negative for commodity DRAM/NAND | Client DRAM and Solidigm under pressure | Product-level EPS reduction |
| China HBM challenge | TSV/stacking/base die/packaging/customer qualification | Partial offset of HBM catch-up value | Very negative for scarcity premium | P1 to P3 shift |
| Foundry normalization failure | Continued losses, no yield improvement | Samsung-specific risk | Limited impact | Samsung P1 multiple reduction |

### Upside Signals

- 2028 HBM long-term contracts with higher volumes and prices and broader customer diversification
- Early stabilization of HBM4E yield and mass-production volumes
- Simultaneous confirmation of Samsung's rising HBM share and narrowing foundry losses
- AI service revenue and cash flow growing faster than compute resource contracts
- HBM lead times and allocations hold even as supply expansion lags
- SK Hynix shareholder return plan becomes concrete

### Downside Signals

- HBM ASP decline and shipment volume drop occur simultaneously
- Two or more major hyperscalers lower capex growth rates
- Long-term contract renegotiation, breach, or prepayment impairment
- Memory inventory build and spot-to-contract price inversion
- Actual AI service per-token HBM consumption falls 20%+ for two consecutive quarters
- Samsung/Micron volume supply increase coincides with HBM premium decline

On a monthly basis, the indicators to track together are: HBM4/4E contract prices and prepayments, top-3 memory producer volumes and yields, advanced packaging lead times, hyperscaler capex and cash flow, Oracle and CoreWeave financing costs, Taiwan server ODM revenue, and DRAM/NAND contract prices and inventory.

## 16. Relative Investment Interpretation

The two names are not equivalent ways to buy the same memory upcycle.

| Scenario | Samsung Electronics | SK Hynix |
|---|---|---|
| P1 Strengthening | HBM catch-up and commodity memory tailwind | Largest earnings leverage from HBM share and LT contracts |
| P2 Warning | Business diversification and net cash provide partial defense | More sensitive to order gaps and multiple compression |
| P3 Strengthening | Broad memory product range and foundry execution provide partial buffer | Direct exposure to HBM premium compression |
| P4 Warning | Absolute decline unavoidable but relative defense possible | Greatest risk of simultaneous earnings and multiple decline |

From a risk-adjusted standpoint, Samsung offers a wider and more defensive choice. SK Hynix has greater earnings leverage in P1, but its valuation shifts faster when supply, efficiency, and credit conditions change.

Equipment and materials names also should not be grouped together indiscriminately. Equipment companies exposed to order gaps must be separated from consumable and parts suppliers whose revenues track utilization rates. Equipment with confirmed purchase orders and components/materials with recurring revenue streams are a better fit for this scenario framework than a pure HBM theme basket.

## 17. Conclusion

The memory boom through 2027 can be maintained as the central path for earnings estimates. But the real test of current share prices is not 2027 EPS — it is the duration of earnings beyond 2028. The claim that the HBM supply deficit has lasted longer than past cycles, and the claim that memory companies deserve a permanently elevated scarcity multiple, are not the same argument.

Samsung Electronics holds HBM catch-up potential, commodity DRAM/NAND, foundry operations, and net cash simultaneously, offering P1 upside and relative downside defense across P2–P4. SK Hynix's HBM share and long-term contracts provide the highest earnings leverage in P1, but if supply, efficiency, and financing conditions normalize, earnings and multiples can compress together.

The current probability-weighted results say: <strong>through 2027, both companies offer meaningful upside; looking through to 2028, Samsung's risk-adjusted margin of safety is wider.</strong> For SK Hynix to see further rerating, confirmation is needed that HBM4E yield, 2028 long-term contract terms, and AI infrastructure financing continue to support P1.

## Items That Cannot Yet Be Confirmed from Public Sources

1. Samsung Electronics' segment-level EPS for 2027–2028 and foundry normalization sensitivity
2. SK Hynix long-term contract customer weighting, repricing formula, and prepayment/minimum purchase terms
3. Top-3 memory makers' HBM-dedicated wafer input, good-die and stacking yield, and customer-specific producible volumes
4. Composition of 2028 hyperscaler capex between internal cash flow, corporate bonds, and project finance
5. CoreWeave and Oracle refinancing schedules and covenant headroom
6. Per-generation HBM4E capacity, bandwidth, and memory residency rate changes per accelerator
7. CXMT/YMTC actual shipment volumes, global customer qualifications, and product-level earnings sensitivity

## Key Sources

- [Korea Investment & Securities, SK Hynix 2Q26 Preview, 2026-07-13](https://vo.la/fd9udR9)
- [Korea Investment & Securities, "The Start Begins Now," 2026-05-20](https://vo.la/jBPy7zV)
- [Korea Invest Insights, HBM 2030 Supply-Demand Model Cross-Check](/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
- [AI 2040, Plan A](https://ai-2040.com/?choices=plan-a-root)
- [AI 2040, Compute Supplement](https://ai-2040.com/supplements/compute-supplement)
- [AI 2040, Economics of Plan A](https://ai-2040.com/supplements/economics-of-plan-a)
- [Oracle FY2026 Earnings](https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/)
- [CoreWeave 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm)
- [CoreWeave DDTL 4.0 Form 8-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/crwv-20260330.htm)

The scenario probabilities and fair values in this report are analytical estimates based on publicly available information and do not constitute personalized investment advice. Actual investment decisions must separately account for price volatility, investment horizon, taxation, currency risk, and individual loss tolerance.
