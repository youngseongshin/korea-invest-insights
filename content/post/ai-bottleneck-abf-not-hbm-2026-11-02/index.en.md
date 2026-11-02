---
title: "The 2027–28 AI Bottleneck Is ABF Substrates, Not HBM"
date: 2026-11-02T14:00:00+09:00
lastmod: 2026-11-02T14:00:00+09:00
categories: ["ai", "market-analysis", "semiconductor"]
tags: ["ABF", "IC substrate", "CoWoS", "HBM", "Ibiden", "Unimicron", "memory cycle"]
series: ["Korea Semiconductor Watch"]
slug: "ai-bottleneck-abf-not-hbm-2026-11-02"
description: "An AI GPU or ASIC ships as a set of HBM, CoWoS-class packaging, and ABF substrate. From 2024 to 2028, Unimicron's stated capacity multiples are CoWoS 6.8x and hyperscaler capex 6.3x, versus IC substrate 2.0x and DRAM 1.8x. The slowest link sets the ceiling. That ceiling does not erase demand. It pushes shipments into 2028–29 and lengthens the memory cycle."
draft: false
---

The consensus says: "If AI buildout overshoots, supply will flood the market, and the bottleneck is already easing at HBM."

Public numbers move the bottleneck. At TPCA on October 20, 2026, Unimicron's chairman put 2028 capacity versus 2024 at CoWoS 6.8x, hyperscaler capex 6.3x, IC substrate 2.0x, and DRAM 1.8x ([TrendForce write-up, secondary, Delayed](https://www.trendforce.com/news/2026/10/20/news-unimicron-warns-of-ic-substrate-crunch-up-to-30-month-equipment-lead-times-20-material-gap-in-2027/)). In the same remarks, critical tool lead times stretch to 30 months, 2027 supply of key materials (low-CTE glass fiber, CCL, ABF) is short by about 20%, and a new substrate fab needs 2.5–3 years from groundbreaking to shipment, so the next capacity wave arrives no earlier than 2029.

<strong>Our view: The binding bottleneck for 2027–28 AI accelerator shipments is ABF and IC substrate, not HBM stacking. HBM, CoWoS-class packaging, and substrate ship as one set. The slowest part sets the set ceiling. A substrate ceiling does not erase AI demand. It delays shipments and lengthens the memory cycle into 2028–29. We are wrong if, by June 2027, Unimicron, Ibiden, and the three Taiwan substrate names all print two consecutive quarters of YoY revenue growth below +20%, and the Morgan Stanley (reported) ABF shortage assumption for 2027 is cut below 5%.</strong>

On October 30, our [note on a longer substrate shortage](https://koreainvestinsights.com/post/the-substrate-shortage-just-got-longer/) separated Ibiden, SEMCO, and Daeduck around Daeduck's Q3. Below keeps only <strong>how a set bottleneck lengthens the memory cycle</strong> in the same supply chain.

## Set ceiling: three parts must leave together

One AI GPU or ASIC roughly needs HBM, advanced packaging (CoWoS-class), and an ABF substrate. If one leg is short, finished units are capped there.

| Axis (2024→2028) | Multiple | Definition / as-of | Source |
|---|---:|---|---|
| CoWoS capacity | 6.8× | Unimicron chairman, 2026-10-20 | TrendForce path, secondary·Delayed |
| Hyperscaler capex | 6.3× | Same remarks | Same |
| IC substrate capacity | 2.0× | Same remarks | Same |
| DRAM capacity | 1.8× | Same remarks | Same |

The table answers one question: <strong>which axis throttles set buildout.</strong> When CoWoS and capex grow more than 6x, substrate grows 2x and DRAM 1.8x. HBM can be tight and substrate can still be the slower multiplier. Sold-out 2027 HBM is evidence of demand and contracts. It is not proof that HBM is the set ceiling.

One cross-path in numbers: if the largest AI substrate grows from 80mm on a side (2025) to 110mm (2028 roadmap), area scales by (110/80)² ≈ 1.89x (Ibiden roadmap assumption, fallback). If substrate "capacity" doubles on an <strong>area</strong> basis, unit supply of the largest package is about 2.0 / 1.89 ≈ 1.06x. Whether disclosed capacity is area or unit count is Missing, so treat this as an upper-bound estimate only. The point is simple. As packages grow, the same area capacity holds fewer units.

## ABF balance: shortage rates rise, prices follow

Morgan Stanley estimates (2026-10-14, via Postation, <strong>secondary·unverified</strong>) raised the ABF substrate shortage to 9.3% in 2027 (from 6.2%) and 13.7% in 2028 (from 9.4%). The same secondary path cites substrate prices up 25%+ in 2027 and an about +30% ABF film hike in 3Q26 for Ajinomoto (95%+ share) ([Postation](https://www.postation.jp/news/abf-substrate-shortage-ibiden-ajinomoto), [VLSI.kr summary](https://www.vlsi.kr/en/abf-substrate-crunch-mb-en/)).

Primary confirmation sits with suppliers.

| Observation | Value | Period / definition | Source |
|---|---|---|---|
| Ibiden electronics FY3/27 OP guidance | ¥114bn (~2.5x prior year) | Re-raised 2026-10-29 | Company IR / filings path (primary) |
| Ibiden 1H OP | +96.7% YoY | FY3/27 first half | Company disclosure path |
| Unimicron Sep revenue | +64.7% YoY | TWSE, 2026-09 | TWSE OpenAPI (primary) |
| Nanya PCB Sep revenue | +57.8% YoY | Same | TWSE (primary) |
| Kinsus Sep revenue | +44.5% YoY | Same | TWSE (primary) |

September Taiwan revenues are not ABF-only. Still, +40–65% YoY at substrate names is a physical signal that price, mix, and utilization moved together. Ibiden's 2.5x guide is primary evidence that scarcity is showing up in earnings.

## HBM is locked; packaging growth decelerates in 2028

A substrate bottleneck does not cancel HBM demand. Samsung Electronics' Q3 2026 IR shows memory revenue from KRW120.8tn to KRW140.7tn (+16.5% QoQ). On the call, DRAM ASP was about +20% and bit shipments were low- to mid-single digits ([Samsung IR](https://news.samsung.com/global/samsung-electronics-announces-third-quarter-2026-results), [conference PDF](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2026_3Q_conference_eng.pdf), primary). A log decomposition puts roughly one-quarter on bits and about three-quarters on price and mix (fallback). HBM4 was about 60% of HBM revenue, HBM4 revenue more than 3x QoQ, long-term agreements stood at 10 signed and 10 in negotiation, and 2027 HBM targets were sold out.

Packaging has a different slope. Goldman estimates via TrendForce (<strong>secondary·unverified</strong>, as_of 2026-10-27) put CoWoS capacity at 1.275m wafers in 2026 → 2.73m in 2027 (+114%) → 3.48m in 2028 (+27%). 2027 ramps hard. 2028 growth slows to about one-quarter of that rate. Reports of a 10–20% CoWoS price review and a 3–6% wafer price increase from January 2027 sit in the same bundle ([TrendForce path](https://www.trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge/)).

| Year | What binds the set | Implication for memory | Observation that flips the rank |
|---|---|---|---|
| 2027 | HBM LTAs / sell-out + substrate material and tool lead times | Shipment cap; price/mix holds | LTA renegotiation failure and substrate revenue slowdown together |
| 2028 | Lagging substrate multiples + CoWoS +27% | Deferred demand lengthens the cycle vs bit supply that outruns it | 2028 bit-supply growth far above CoWoS and substrate growth |
| 2029 | New substrate fabs ship (2.5–3 years after groundbreaking) | Possible easing of the set ceiling | Fab schedules slip by a year or more |

One line from the table: <strong>2027 is a locked-volume year. Substrate stretches shipments later more than it "upgrades" scarcity to a stronger label.</strong>

## Collision with the bubble (oversupply) story

The oversupply story says capex runs ahead of demand and product floods the market. The multiples above point the other way. When capex and CoWoS outgrow substrate and DRAM, the physical result is a queue or delayed delivery, not empty racks. Microsoft's September-quarter 2026 capex was about $45.2bn versus an internal plan near $50bn. The CFO pointed to third-party (neocloud) GPU-as-a-service delays into 1H 2027 (earnings path / secondary arithmetic). Azure still grew 48%, and commercial RPO was $677bn (+73%). The miss is procurement and delivery, not vanished demand.

Reports that NVIDIA Vera Rubin HBM4 bandwidth eased from 22 to 19.2 TB/s per GPU (about −13%). Product-page edits and coverage from 27–29 October 2026 are Delayed. That change can raise effective HBM4 supply. It is closer to one more supply-side reason to keep 2028 memory supply risk at "moderate" than a break of 2027 volume locks. Substrate need not be labeled "severe" to still push the cycle into 2028–29.

Taiwan's September export orders hit a monthly record at $114.21bn (+62.4% YoY). The ministry said ASIC servers are growing faster than GPU servers ([Taipei Times path, Delayed](https://www.taipeitimes.com/News/biz/archives/2026/10/21/2003866318)). ASIC acceleration widens HBM demand beyond one GPU vendor and still consumes the same substrate and packaging set.

## Name frame

| Name | What this thesis says | What is public | Missing / Partial |
|---|---|---|---|
| Samsung Electronics | A lid on shipment speed and high reliance of profit on price/mix | Q3'26 bits low, price high; 2027 HBM sold out and LTAs | 2028 contract price floor |
| Samsung Electro-Mechanics | Candidate beneficiary of FC-BGA / AI high-layer substrate tightness | Moves with the industry revenue and price cycle | AI high-layer share (Partial) |
| Daeduck Electronics | A price and utilization cycle bet | Tied to industry tightness | Share of top-spec AI substrates (Missing) |

Frame only. How much of any name to hold is outside this piece.

## Counter-evidence

1. <strong>HBM is still tight.</strong> Sold-out 2027 and LTAs explain why markets talk HBM first. Calling substrate binding means "slower in the set," not "HBM is loose."
2. <strong>CoWoS +114% in 2027 is a real counter to packaging scarcity.</strong> 2028's +27% and substrate's 2.0x remain. If packaging eases and substrate does not, the set stays bound.
3. <strong>If 2028 memory bit supply (greenfield, CXMT, and peers) outruns deferred demand,</strong> the outcome is price pressure, not a longer cycle. Then "lengthens the cycle" is wrong.
4. <strong>MS ABF shortage rates and the Ajinomoto +30% print are secondary and unverified.</strong> We do not paste paid primary text. If those figures are cut, they meet the falsifiers above.

## What to watch next

| Checkpoint | Signal that strengthens the view | Signal that weakens it |
|---|---|---|
| December TWSE substrate trio revenue | YoY still ≥ +40% | YoY slows below +20% |
| Second ABF film price reports | Further hikes or tighter allocation | Hike reversed; inventory builds |
| Ibiden / Unimicron guidance | OP or capacity raised | Demand cancellations; utilization cut |
| 2027 hyperscaler capex guides | Held or raised, with delivery delays named | Two or more names cut explicitly |
| 2028 memory wafers and LTAs | LTAs extended; wafer schedules slip | LTAs fail and wafer guides rise together |

## What remains in one line

To judge whether AI buildout is "too much," watch how fast the <strong>set</strong> actually ships, not only total capex. In the 2024→2028 multiples, the slowest published axis is IC substrate. That ceiling is not evidence against demand. It is evidence that shipments slip later and the memory price-and-mix window can last longer.
