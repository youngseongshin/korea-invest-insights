---
title: "AI ROI Clears the Bar Through Volume and Other Ledgers, Not Token Prices"
date: 2026-10-31T23:00:00+09:00
lastmod: 2026-10-31T23:00:00+09:00
categories: ["ai", "market-analysis"]
tags: ["AI ROI", "token pricing", "open weights", "agents", "Meta", "Alphabet", "Ramp"]
series: ["Korea Semiconductor Watch"]
slug: "ai-roi-beyond-token-price-2026-10-31"
description: "In the Ramp index, the token unit price fell 42%, volume rose 65%, and spend rose 1.5%. AI ROI measured as token revenue divided by capex comes out low. The payback comes from volume that grows faster than prices fall and from enabler revenue that never shows up as tokens. The money lands first on compute owners and incumbent platforms, not on the labs."
draft: false
---

The consensus says: "Token prices keep falling, so AI capex will not be recovered through token revenue."

Public numbers undercut the premise. In the Ramp AI Index, which uses corporate card data, the token unit-price measure fell from 1.10 to 0.64 (−42%) between August 2 and October 11, 2026. Over the same period, volume rose 65% and corporate AI spend rose 1.5% (Ramp AI Index, raw CSV not verified). The price collapsed. Total spend did not. In the same quarter, Alphabet disclosed that its first-party model APIs process nearly 32 billion tokens per minute, up 40% QoQ and more than 4x YoY ([Alphabet 8-K Exhibit 99.1, Q3 2026](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm)). Meta sold no tokens, yet grew Q3 ad revenue 26%, with average price per ad up 14% ([Meta Q3 results](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx)).

<strong>Our view: The path past current AI ROI is not token price (P). It is volume (Q) that grows faster than unit prices fall, plus enabler revenue that never shows up as tokens. We are wrong if, by June 2027, corporate AI spend growth in the Ramp data fails to beat the token unit-price decline for two consecutive quarters (elasticity stuck at or below 1), and Meta's price-per-ad growth drops below +5% YoY for two quarters.</strong>

If this holds, the money lands first on the books of compute owners and incumbent platforms, not frontier labs. That is why "AI revenue ÷ capex" understates the payback, and also why it cannot block overstated claims: AI-driven ad revenue is not disclosed separately.

## The P×Q scissors: growth-rate gaps, not price levels, decide ROI

The condition is one line. Growth in token spend (P×Q) must beat growth in capex. A falling P is not the problem by itself.

| Metric | Value | Period / definition | Source |
|---|---:|---|---|
| Token unit-price measure | 1.10 → 0.64 (−42%) | 2026-08-02 → 10-11, corporate spend | Ramp AI Index (not verified) |
| Token volume | +65% | Same period | Ramp AI Index |
| Corporate AI spend | +1.5% | Same period | Ramp AI Index |
| Alphabet first-party API tokens | ~32B per minute | Q3 2026, +40% QoQ, >4x YoY | Alphabet 8-K (primary) |
| Top-5 hyperscaler ROIC | 27.8% → 20.1% | 2024-12 → 2026-03, chart read ±0.5pp | Apollo chart (secondary) |

Simple multiplication gives 0.58 × 1.65 ≈ 0.96, so spend should have fallen about 4%. Actual spend rose 1.5%. The gap may be a mix shift toward pricier models, but public data does not confirm it. What is clear is that price elasticity is about 1: volume barely offsets the price decline. If that sticks, revenue stalls while capex grows, and ROIC falls. The ROIC decline above shows that denominator effect.

So the volume paths matter most. Long-horizon work is the example. At a 99% per-step success rate, the chance of finishing a 100-step task is 0.99¹⁰⁰ ≈ 36.6%. At 99.5%, it is 60.6% (assumed formula). A 0.5pp gain per step makes completion 1.7x as likely. When more work can be delegated, tokens per task and the number of tasks rise together. This path lifts Q regardless of price declines.

## Path-by-path verdict: which routes clear the ROI bar

| Path | Verdict | Public evidence | Observation that flips it |
|---|---|---|---|
| ① P: premium model prices hold or rise | NO | No primary case of a lab list-price increase. Top-tier output price cut from $75 to $25 (2025-11) | Top-tier list price frozen 2 quarters + paid revenue accelerating |
| ① P: rising costs normalize low-end token prices | NO (near term) | B200 rental ~+39% YTD while token index −54% (end-May → Sep, Silicon Data) | 2+ low-end API list-price increases |
| ① Q: spread to office and daily work | YES (volume) | Ramp paid AI adoption 55.9% (Oct). Microsoft Copilot 30M paid seats (reported, secondary) | Adoption flat for 2 quarters |
| ① Q: token-maxing in office work | CONDITIONAL | No direct tokens-per-task data | Seat price frozen while tokens rise, squeezing only lab margins |
| ① Q: better long-horizon capability | YES (dominant) | Alphabet 32B tokens/min, >4x YoY (primary). Agent work time 6x human (Anthropic report 10-16; report withholds causality) | Completion rates flat for 2 quarters |
| ② Chinese lab ROI worsens, cheap supply shrinks | NO | Counter-evidence: Tencent, Alibaba, Baidu fund AI capex from operating cash, cash, and equity (company results). No Chinese lab P&L disclosed | Alibaba fails another raise, Baidu cash burn accelerates |
| ② Open-weight catch-up slows | NO (12 months) | Open-vs-top gap projected 12 → 3 points (AA index, Kimi K3.1 Pro); lag ~4 months (Epoch) | Gap widens on long-task benchmarks; tighter export controls |
| ③ Infra demand rises even with open weights | YES | Large open MoE weights need 1.1–1.4TB memory | Distillation and smaller models cut compute per task sharply |
| ③ Open weights + services secure ROI | CONDITIONAL | No service-provider margin disclosed | Service-provider margin disclosure |
| ④ Paid delegated agents (per task) | CONDITIONAL (2027+) | Coding agent run-rate $2.5B+ (Feb, secondary). No outcome-based billing revenue disclosed | Disclosed commercial outcome-billing revenue |
| ⑤ Free delegated agents (ads, fees) | NO (minor before 2028) | Chatbot ads ~$1B annualized (Digiday, secondary). 4% in-chat checkout fee withdrawn | Disclosed agent-routed transaction fees |
| ⑥ AI as enabler in existing services | YES (dominant) | Meta ads +26%, price per ad +14%, impressions +10% (primary) | Price per ad below +5% YoY for 2 quarters |

The table's conclusion is one line. The two axes that clear the bar are ⑥ enabler and ① long-horizon volume. Public evidence does not support the price (P) path the question hoped for.

## Enabler: the biggest payback never shows up as token revenue

Meta's Q3 total revenue was $64.6B, up 26% YoY. Ad impressions rose 10% and average price per ad rose 14% ([Meta IR, primary](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx)). Meta's engineering blog said its GEM ad-ranking model lifted conversions 18.9% (October 13, company statement). Price rising faster than impressions means advertisers paid more for the same exposure. The filings do not attribute the full price increase to AI, and we do not upgrade correlation to causation.

Counter-evidence sits in the same company. Meta's Q3 free cash flow was −$2.12B, and net cash shrank to about $1.5B (Meta 8-K). Enabler revenue is strong, but capex is growing faster. That is why Meta's price-per-ad growth is a falsification condition for this view.

## Open weights: they hit lab pricing, not infrastructure volume

Large open-weight MoE models need 1.1–1.4TB of memory just to load weights (Nemotron 3 Ultra BF16, Kimi K3 4-bit). Enterprises that self-host need the same GPUs and memory. What open weights change is who owns the profit: lab model margins shrink, compute volume stays with whoever owns the hardware.

The checkpoint is November 4, when Moonshot AI plans to release Kimi K3.1 Pro weights. If the Artificial Analysis index then confirms a 3-point open-vs-top gap, the lab premium window shortens and path ① P weakens further. China's draft revision of its technology export list (comments close November 15) excludes public open source, so it is not yet evidence that catch-up will slow.

## Delegated agents: paid and free sit on different ledgers

Paid delegation (per task) comes from corporate budgets. Some run-rates are public, such as coding agents, but <strong>no company has yet disclosed</strong> outcome-based revenue, paid only when a task is completed. Liability and incident-compensation rules are also unsettled.

Free delegation (everyday use) must cover costs with ads and transaction fees. <strong>No company discloses</strong> agent-routed transaction fees as revenue either. Some platforms, including Amazon, block outside agents (reported). Free agents add users and inference volume, but we expect little ROI contribution before 2028.

## Counter-evidence

1. <strong>Elasticity near 1:</strong> Taken at face value, Ramp shows volume barely offsetting price declines. If that persists, revenue stalls, capex grows, and ROIC keeps falling (27.8% → 20.1%).
2. <strong>Cost of capital:</strong> Reports say Anthropic's credit rating is expected in BB territory after listing (FT, October 30, secondary). Hyperscaler IG spreads are 119bp versus 86bp for the index (FRED, October 29). Capital costs in the denominator could break ROI before demand does.
3. <strong>Narrowing open gap:</strong> A 3-point gap trims the top of premium pricing and narrows the lab revenue path.

## What to check next

| When | What | Strengthening signal | Weakening signal |
|---|---|---|---|
| Nov 4 | Kimi K3.1 Pro weight release | Re-measured gap stays ≥5 points | 3-point gap confirmed |
| Nov 15 | China export-list comment deadline | Tighter limits on overseas local deployment | Draft unchanged (open source excluded) |
| November | Ramp AI Index, November edition | Spend growth > price decline | Spend flat, elasticity ≤1 |
| TBD | Anthropic amended S-1 | Improved run-rate and gross margin | Revenue slowing versus compute commitments |
| Late Jan–early Feb 2027 | Meta and Alphabet Q4 results | Price per ad holds ≥+5% YoY; tokens/min keeps rising QoQ | Price per ad <+5% YoY for two quarters; token QoQ growth slows |

## The supply-chain side lives in the bullwhip piece

Inflation in power requests, cloud commitments, and memory inventory was covered in [The AI Bullwhip Map](/post/ai-bullwhip-grid-cloud-memory-2026-10-31/). On the final-payer side, two questions remain: who pays, and on whose books the money lands.

<small>This is analysis based on public sources and not investment advice. Secondary-report figures are marked in the text.</small>
