---
title: "Who Burns All Those Tokens? NVIDIA's Customer Map, Sovereign AI and Codex at 9 Million Start Answering"
slug: "who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19"
date: 2026-07-19T19:00:00+09:00
description: "The question that never went away in the AI CAPEX debate was who would actually use all that infrastructure. On NVIDIA's books, non-hyperscale revenue has reached parity with hyperscale and its quarterly growth rate has already flipped ahead. Sovereign AI revenue tripled in a year, Meritz's semiconductor team pushed back on the market's narrow frame with a re-tightening server DRAM market, and Codex added three million users in three days. We cross-verify the demand-side evidence that landed right after Kioxia's limit-down and the Nasdaq slide, and map what it means for the 45/35/20 demand scenarios."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["NVIDIA", "Sovereign AI", "Codex", "AI Memory", "Server DRAM", "HBM", "Samsung Electronics", "SK Hynix", "AI CAPEX", "Agentic AI", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Context
> This post builds on [Will AI Memory Demand Exceed Expectations?](/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/), which probability-weighted demand at a base case of 45%, a beat case of 35% and a miss case of 20%, and on [SK Hynix Chairman Chey Tae-won's Two Months of Remarks](/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/), which read the words and moves of the supply side's top executive. The weak link still left is final demand. With this much GPU and HBM being deployed, who exactly is going to burn all those tokens? This piece records the week in which numbers began attaching to that question.

## TL;DR

- In NVIDIA's data center revenue, the hyperscale share has held around 50% for seven straight quarters. The share itself has not already collapsed. What has changed is the composition. In the February-April 2026 quarter, <strong>non-hyperscale (ACIE) revenue of $37bn reached near-parity with hyperscale's $38bn</strong>, and the quarterly growth rate had already flipped, 31% QoQ versus 12% QoQ. The next disclosure could be the one where the share itself flips for the first time.
- Over the same stretch, data center revenue's year-over-year growth rate re-accelerated from +56% to +66%, +75% and +92%. The share holding steady while the total sped back up means <strong>incremental growth is being pulled by everything outside hyperscale</strong>. NVIDIA itself wrote in its disclosures that growth was led by the rest of its customer base.
- Sovereign AI revenue topped $30bn for full-year FY2026, more than tripling from the prior year, and it grew more than 80% year-over-year in the most recent quarter as well. This is the buyer that the market missed while it kept watching only what the hyperscalers were saying.
- Meritz Securities' semiconductor team flagged, in a Sunday report, the start of full-scale sovereign purchasing and a renewed tightening in server DRAM supply since mid-July. TrendForce's forecast of a +13-18% rise in third-quarter server DRAM contract prices, Taiwan's Inventec testifying to lead times of over 40 weeks, and Micron's statement that it can meet only 50-66% of key-customer demand all cross-verify this externally.
- Numbers have appeared on the final-demand side too. OpenAI's Codex went from 1 million in February to over 5 million by late May, then from 6 million on July 12, right after the GPT-5.6 launch, to about 9 million around July 15, <strong>adding 3 million users in three days</strong>. This is the stretch where the unit of demand shifts from subscriber counts to agent execution time.
- The conclusion is not a premature upgrade of the probabilities. It is that, before litigating oversupply, this is the moment to re-examine <strong>whether demand was drawn too conservatively</strong>, and that the verdict will be delivered by the earnings season around July 30 and NVIDIA's disclosure at the end of August.

<div class="thesis-callout">
<div class="thesis-callout__label">Key Framing</div>

The market has been doubting the sustainability of AI CAPEX while watching only what four Big Tech companies were saying. Meanwhile, on NVIDIA's own books, non-hyperscale revenue reached parity with hyperscale, sovereign revenue tripled in a single year, and Codex added 3 million users in three days. While the stock price priced in the fear of oversupply first, the base of demand was quietly stacking up hard evidence pointing the other way. This asymmetry is the essence of the current correction.

</div>

## 1. What Kind of Week Was This: Between a Limit-Down and a Report

Let's set the stage first. On Thursday, July 16, in the US market, the Philadelphia Semiconductor Index (SOX) plunged around 4% and entered bear-market territory, down more than 20% from its high, while the Nasdaq fell 1.47%. On Friday the 17th, the Nasdaq fell a further 1.40%, bringing the weekly decline to 2.90%. [Fact: market data] The same day in Tokyo, Kioxia hit limit-down right after the open, plunging 16.1%. The stock had fallen to less than half its June 22 peak, and roughly JPY 30tn in market cap had been erased. The direct trigger was a roughly $229 million patent-infringement damages verdict that a US jury awarded to Viasat, but the fact that TSMC fell 7.29%, SK Hynix's ADR fell 13.69% and SanDisk fell 12.63% in the same session shows the real story was deleveraging across the entire AI rally. [Fact: Nikkei and Hankyung reports]

The Korean market sidestepped that Friday, because July 17 was a market holiday for Constitution Day, redesignated as a holiday for the first time in 18 years. But just before that, it had already gone through steep declines of its own: SK Hynix -15.37% and Samsung Electronics -10.70% on July 13, then SK Hynix -12.34% and Samsung Electronics -9.47% on July 16. [Fact: exchange data] The narrative the market is pricing in is clear. Supply is increasing, China is catching up, 2027 earnings are being cut, and nobody knows when Big Tech's CAPEX will turn down.

Against this backdrop, on Sunday, Meritz Securities' semiconductor team, analysts Kim Sun-woo, Yang Seung-su and Kim Dong-kwan, published a set of reports together. The timing was clearly conscious of Friday's sell-off and the Kioxia episode. The thrust runs the other way. Memory demand right now is not just hyperscalers, sovereign-camp purchasing including the Middle East is moving into full swing, and server DRAM supply has been tightening again since mid-July. Their rebuttal is that the view treating 2028 shortage relief as a foregone conclusion has not priced in this demand. [Fact: Meritz Securities report summaries, 2026-07-19]

Rather than leave this as a war of words, we break the claim into three verifiable pieces and check each against hard evidence one at a time: NVIDIA's customer mix, sovereign purchasing, and final usage.

## 2. NVIDIA's Customer Map: The Share Sits at 50%, the Growth Sits Outside

Let's start by precisely checking the claim that the hyperscaler share is shrinking. Laying NVIDIA's quarterly disclosure language out as a time series looks like this.

| Fiscal Quarter | Period | DC Revenue | YoY | Large CSP/Hyperscale Share (disclosure language) |
|---|---|---|---|---|
| FY25 Q3 | Aug-Oct 2024 | $30.77bn | +112% | ~50% |
| FY25 Q4 | Nov 2024-Jan 2025 | $35.58bn | +93% | ~50% |
| FY26 Q1 | Feb-Apr 2025 | $39.11bn | +73% | Just under 50% |
| FY26 Q2 | May-Jul 2025 | $41.10bn | +56% | ~50% |
| FY26 Q3 | Aug-Oct 2025 | $51.22bn | +66% | Not disclosed |
| FY26 Q4 | Nov 2025-Jan 2026 | $62.31bn | +75% | Slightly over 50%, growth led by the rest of the customer base |
| FY27 Q1 | Feb-Apr 2026 | $75.2bn | +92% | Hyperscale $38bn (~50%) vs. ACIE $37bn |

[Fact: NVIDIA CFO commentary and earnings calls]

Two things are visible at once. First, <strong>the share figure itself has not left the 50% band for seven straight quarters</strong>. The narrative that hyperscalers have already been pushed aside is not supported by the hard data. Second, even so, the direction of the mix has clearly shifted. The FY26 Q4 disclosure explicitly stated that growth was led by the rest of the customer base and that revenue had diversified, and starting in FY27 Q1, NVIDIA began disclosing data center revenue split between hyperscale and ACIE (AI cloud, industrial, enterprise). In that first quarter, ACIE came in at $37bn, nearly matching hyperscale's $38bn, and the quarterly growth rate flipped to <strong>ACIE +31% QoQ versus hyperscale +12% QoQ</strong>. AI cloud revenue within ACIE was up more than threefold year over year. CEO Jensen Huang stated flatly on the call that over the long run, the second category would grow faster. [Fact: earnings call]

Overlay the growth-rate re-acceleration on this and the picture is complete. Data center revenue's year-over-year growth rate bottomed at +56% in FY26 Q2 and climbed back up through +66%, +75% and +92%. The share holding steady while total growth sped up means, arithmetically, that <strong>more than half of the incremental growth is being generated outside hyperscale</strong>. [Inference: disclosure arithmetic] If this trend holds for even one more quarter, the FY27 Q2 disclosure at the end of August will print a number where ACIE overtakes hyperscale for the first time. From that moment on, the very frame of judging AI demand's sustainability by watching only four Big Tech companies' CAPEX guidance becomes outdated.

One point of confusion is worth clearing up. Direct-customer concentration in the 10-Q (Customer A at 22%, Customer B at 14%) has actually risen, but that is a distribution-stage metric that aggregates board partners, OEMs and large direct purchases, a different layer from the diversification of final demand. [Fact: 10-K] Distribution concentrating and final demand broadening are two things that hold true at the same time.

## 3. Sovereign AI: The Buyer the Market Missed While Watching Only the Talk

The largest chunk of non-hyperscale demand is sovereign. NVIDIA's CFO stated that FY2026 sovereign AI revenue more than tripled from the prior year, <strong>topping $30bn</strong>. Canada, France, the Netherlands, Singapore and the UK led the way, sovereign revenue was up more than 80% year over year in FY27 Q1 as well, and NVIDIA infrastructure is now deployed across roughly 40 countries with combined GDP of about $50tn. [Fact: NVIDIA earnings call]

Physical substance is attached to this too. Saudi Arabia's HUMAIN has finalized a plan to deploy up to 600,000 NVIDIA GPUs over three years and has received its initial shipment of 18,000 GB300 units. In the UAE, Stargate UAE is building Phase 1, a 200MW slice of a 1GW cluster, targeting activation in the third quarter of this year, with Phase 1 alone taking up to 35,000 GB300 units, and operator G42 received US export approval in mid-July. The EU has a EUR 20bn AI gigafactory program underway, India is targeting 100,000 public GPUs by year-end, and Japan's SoftBank is targeting an October commercial launch of a sovereign GPU cloud. [Fact: company and government announcements]

How does this flow through to memory? Two channels are already public. OpenAI's global Stargate program signed a letter of intent with Samsung Electronics and SK Hynix in October 2025 for <strong>up to 900,000 DRAM wafers per month</strong>, a volume equal to roughly 40% of global DRAM capacity. The limitation that this is a non-binding letter of intent clearly remains. [Fact: press reports, LOI] And in June of this year, SK Hynix formalized a multi-year HBM4 partnership with NVIDIA spanning the next-generation Vera Rubin platform. [Fact: NVIDIA announcement] On the sovereign-wealth-fund side, there has been a continuing stream of reports on cooperation between UAE capital, Mubadala, MGX, G42 and Khazna, and the SK Hynix camp.

There is a gap that also needs to be left in place honestly. No new disclosure confirming that a sovereign entity directly bought DRAM in bulk from Samsung Electronics or SK Hynix has surfaced in June or July. [Blocked: no direct contract disclosed] Sovereign memory demand flows in through server OEMs and system vendors, so it gets mixed in with hyperscalers inside the memory makers' customer disclosures. [Inference: distribution structure] Not being visible is not the same as not existing. There is no scenario where 600,000 confirmed GPUs come without memory attached, so the question is not whether it exists but how visible its scale and timing are in disclosures.

## 4. Server DRAM Re-Tightening: Meritz's Claim and External Hard Evidence

The re-tightening in server DRAM supply since mid-July that the Meritz team flagged is not a claim the house is making alone. Four pieces of external hard evidence point the same direction.

| Evidence | Detail | Source/Date |
|---|---|---|
| Contract price outlook | Q3 server DRAM contract prices projected +13-18% QoQ. Cannot be raised on US CSPs locked into long-term agreements (LTA), so the increase concentrates on non-LTA customers | TrendForce, 7/9 |
| Supply growth rate | RDIMM bit supply growth of 15-20% YoY falls short of CPU shipment growth. CSPs are stockpiling ahead of an expected 2027 shortfall. Modules are shifting down from 96/128GB to 32/64GB | TrendForce, 7/9 |
| Lead time | Server DRAM lead times exceed 40 weeks, prices are up about 90% versus late 2025, quote validity has shrunk to 1-30 days | Inventec remarks reported, 7/16 |
| Supplier testimony | Can meet only 50-66% of key customer demand, HBM is sold out through 2027, the supply shortfall persists beyond 2027 | Micron earnings call, July |

[Fact: sources as listed]

The absolute price level is already flashing an anomaly of its own. The fixed contract price for commodity PC DRAM (DDR4 8Gb) hit a record $21 in June, the highest since tracking began, and the spot price runs 72% above the contract price. There were also reports that Samsung Electronics notified Chinese customers it would raise Q3 DRAM prices by up to 20%. [Fact: industry reports] A combination of rising contract prices alongside a spot premium above 70% means demand willing to pay up for urgent volume actually exists outside the contract channel. The ones paying the high price are not the LTA-locked hyperscalers but everyone outside that circle, namely sovereigns, enterprises and second-tier clouds. TrendForce's statement that the increase is concentrated on non-LTA customers and Meritz's statement that sovereign purchasing is moving into full swing are two expressions of the same phenomenon. [Inference: cross-reading]

Analyst Kim Sun-woo goes a step further here. His view is that the market is misreading the situation, trapped inside a narrow frame of sacrificial long-term contracts and 2027 earnings downgrades, and that this misunderstanding will be dispelled quickly as events unfold, including early execution of shareholder returns and partnerships involving equity investment from Big Tech. [Fact: report claim] This is a house forecast, not a verified fact, so whether it is confirmed by actual events in this week's earnings season is the grading standard. That said, the direction is consistent with SK Hynix Chairman Chey Tae-won's Nasdaq listing proceeds and partnership moves covered in our earlier piece, and with SK Hynix's multi-year contract with NVIDIA.

## 5. Codex at 9 Million: The Numbers on Final Demand Start to Appear

The point most attacked in the AI CAPEX debate was not the infrastructure but what sits at the end of it. Data centers keep getting built, but the evidence that final usage is growing to match has been weak. Notable numbers have started to appear at exactly this weak link.

| Date | User Count | Note |
|---|---|---|
| February 2026 | 1 million | Codex-only active users |
| April 8 | 3 million | Weekly active; usage-limit reset promised at every 1 million milestone |
| April 21 | 4 million | Up 1 million in two weeks |
| Late May-early June | Over 5 million | 6x versus February |
| July 9 | GPT-5.6 general availability | Three variants, Sol, Terra and Luna; Codex merged into the ChatGPT desktop app |
| July 12 | 6 million | Metric from this point on is combined Codex + ChatGPT Work |
| Around July 15 | 9 million | Up 3 million in three days |

[Fact: OpenAI executives' public posts and press]

Two caveats need to be attached for fairness. The numbers from July 9 onward are not Codex alone but a combined metric that includes ChatGPT Work, so a strict continuous comparison with the earlier stretch is difficult. And an external extrapolation that simply extended the late-May growth pace put the 10-million mark in October, whereas the actual figure reached 9 million by mid-July. It should also be stated explicitly that this extrapolation line is not an official OpenAI projection. [Fact: extrapolation source verified] Even allowing for the change in metric definition, what remains is that an acceleration pulling the projected line forward by roughly three months was measured over the three days right after the GPT-5.6 launch.

The reason Codex matters is not the size of the number but the nature of the demand. Codex is a product that converts a person's working hours into inference time. An agent can work longer without a person staying connected any longer, and when one person runs several tasks in parallel, <strong>the volume of work grows faster than the number of users</strong>. From this point on, the unit of demand is not monthly active users (MAU) but total agent execution time. This is exactly the same structure as rewriting the ceiling of the AI memory demand model, in our earlier piece, as the number of workloads times memory per workload times execution frequency.

The efficiency debate flips here too. OpenAI itself stated that GPT-5.6 Sol is 54% more token-efficient than the prior generation. The fact that users and usage surged right after the release of a model with lower cost per token is hard evidence for the Jevons hypothesis: that in the coding-agent domain, efficiency gains do not shrink compute demand but instead <strong>widen the range of work that can be handed to AI</strong>. [Inference: Jevons effect] What we should be watching is not the rate at which token prices are falling but the volume of work that the price decline has newly unlocked.

## 6. So How Does This Translate Into Memory

Restraint is needed too. A single number like Codex's 9 million cannot explain the memory cycle on its own. For a user count to translate into memory bit demand, it has to pass through four conversion factors: concurrent execution volume, context length, memory capacity per accelerator, and the supply growth rate. [Inference: demand model] If any single one of these is weak, the headline-grabbing metric and actual demand come apart.

Still, lining up this week's hard evidence against the upside variables set out as the case for the 35% beat scenario in our earlier demand-scenario piece shows an alignment.

- The broadening base of accelerator demand now has hard evidence attached, in the form of the ACIE growth-rate reversal and the tripling of sovereign revenue.
- Always-on agentic inference produced its first numbers, in Codex's 3 million added in three days and the shift in the metric's unit.
- Spread beyond HBM has already shown up in prices, via the +13-18% forecast for server DRAM contract prices, 40-plus-week lead times, and a 72% spot premium.
- The hypothesis that usage growth beats efficiency gains got a counterintuitive piece of hard evidence: a usage surge immediately following a 54% improvement in token efficiency.

This is also where the implication for the 2028 supply-relief narrative diverges. The relief thesis's arithmetic generally treats the deceleration in hyperscaler CAPEX growth as the ceiling on the demand growth rate. But if half of the incremental demand is starting to come from outside that group, the ceiling assumption itself needs to be recalculated. This is exactly the point Meritz's rebuttal is aimed at. We are not changing the probabilities right now. We hold the base 45%, beat 35%, miss 20% framework in place, while recording the fact that hard evidence has started attaching to the beat-side argument along three separate strands. The probability gets updated once the scorecard below fills in. [Inference: scenario management]

## 7. Checking the Counterarguments

The stronger an argument looks, the more important it is to set up its opposite.

- <strong>The quality of non-hyperscale demand.</strong> ACIE includes neoclouds. Orders from second-tier clouds with fragile capital costs are the demand most likely to be cancelled first if interest rates and funding conditions tighten. A growth-rate reversal does not guarantee the durability of demand.
- <strong>Sovereign political volatility.</strong> National projects sway with elections, budgets and export controls. The EU gigafactory program has already had its call for proposals pushed back twice, and Middle East volumes hinge on a single switch: US export approval.
- <strong>The metric trap.</strong> Codex's 9 million is a number that arrived right after the definition changed to a combined metric, and the criteria for what counts as active have not been disclosed. The direction of growth is hard evidence, but the magnitude has not yet been separated from marketing.
- <strong>Price spikes are self-destructive.</strong> The server DRAM re-tightening is a bullish argument, but it also carries the risk, as seen in the IBM case, of eating into IT budgets and creating a demand vacuum after front-loaded buying. Chairman Chey himself has warned about demand destruction from excessive price surges.
- <strong>Distinguishing forecast from hard evidence.</strong> Meritz's event forecasts, early execution of shareholder returns, equity partnerships with Big Tech, are still forecasts. If they do not materialize, the narrow view turns out to have been right.

## 8. The Scorecard: What Will Settle the Answer

- Whether, in the Samsung Electronics and SK Hynix earnings calls around July 30, the magnitude of the Q3 contract-price increase confirms TrendForce's +13-18% range, and whether mentions of non-LTA customers and sovereign volumes appear.
- Whether SK Hynix's early execution of shareholder returns and equity-investment-style partnerships actually show up as disclosures. This is the direct grading item for Meritz's forecast.
- Whether ACIE overtakes hyperscale for the first time in NVIDIA's FY27 Q2 disclosure at the end of August. If it does, the broadening demand base becomes a disclosed number rather than a narrative.
- Whether a direct sovereign memory contract, or a large order routed through a server OEM, rises to the level of disclosure. Whether the Stargate letter of intent converts into a binding contract is the first candidate to watch.
- Whether usage metrics for Codex and competing agents begin to be disclosed on an execution-time basis alongside crossing 10 million.

The arbiter does not change. If DRAM contract prices roll over, the market will throw out this entire demand narrative, and if they hold, the demand curve that had been drawn too conservatively gets redrawn.

---

The stocks mentioned in this piece are examples used for analysis and are not a recommendation to buy or sell any specific stock. Investment decisions and their outcomes are the sole responsibility of the investor. The Meritz Securities report is cited as a reconstructed summary of its main points, and responsibility for the original figures and forecasts rests with that house. Codex user counts changed definition after July 9 to a combined ChatGPT Work metric, making a strict comparison with the earlier stretch difficult, and the extrapolation line projecting 10 million in October is not an official OpenAI forecast. No direct sovereign purchase of memory has been confirmed by disclosure, and Stargate-related volumes remain at the stage of a non-binding letter of intent. Stock, index and price data are as of publicly available material through July 17, 2026, and do not reflect subsequent moves.

### Related Posts

- [Will AI Memory Demand Exceed Expectations? Reading the Over-Growth Odds Through Demand Scenarios and the Supply Map](/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/)
- [SK Hynix Chairman Chey Tae-won's Two Months of Remarks: The Company Gets Stronger, the Margin Peak Passes](/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/)
- [The Real Debate in Semiconductors: Four Physical Clocks and One Stock-Price Clock](/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [Are Semiconductors Cyclical, and What Is Fair Value? Pricing Samsung, SK Hynix and Micron with FCFE and Normalized Earnings](/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
