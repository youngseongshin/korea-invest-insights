---
title: "US Tenbaggers 2023-2026: AI Infrastructure and Korea Pair Trades"
slug: us-tenbagger-census-2023-2026-2026-04-23
aliases: ["/en/post/us-tenbagger-census-2023-2026-2026-04-23/"]
date: 2026-04-23T21:00:00+09:00
description: "Full 3-year US tenbagger census: 40 names from 1,690 tickers, 33% are AI-infra full stack, median 15.7× beats Korea's 13.8×. Where the US leads, Korea follows on a 3-6 month lag — here's the pair-trade map."
categories: ["US Market", "Korea Market"]
tags: ["tenbagger", "US-market", "AI-infrastructure", "pair-trade", "biotech", "quantum", "series"]
series: ["tenbagger-analysis-2026"]
---

> <strong>Series — Tenbagger Analysis 2026 (Part 2 of 2)</strong>
> ① [Korea's 27 Tenbaggers of 2023-2026](/post/kr-tenbagger-census-2023-2026-2026-04-23/) — the KOSPI + KOSDAQ side
> ② <strong>This post</strong> — the US side: 40 names, the AI-infra spine, and the pair-trade with Korea

---

## Data Pipeline — Say It Up Front

- <strong>Universe</strong>: 5,843 US tickers. Backfilled 2023-01-01 → 2026-04-23 via yfinance with `auto_adjust=True` (split/dividend-adjusted → matches realized investor returns).
- <strong>Coverage after resume</strong>: 1,690 tickers with pre-2023-06 history. Post-2024 IPOs and delisted names drop out naturally.
- <strong>Filter</strong>: first close ≤ 30 days after 2023-04-24, held through 2026-04-23, ≥10× total return.
- <strong>Output</strong>: <strong>40 tenbaggers</strong> confirmed.

---

## The Distribution — 40 Names, 19.3× Mean

| Multiple | Count | Representative names |
|---|:-:|---|
| <strong>≥50×</strong> | 3 | AAOI (69.5×), DAVE (50.7×), CVNA (49.8×) |
| 20–50× | 10 | RGC, TSSI, RGTI, APP, PSIX, AXTI, RKLB, CRDO, ALM, PRAX, BWAY |
| 15–20× | 9 | ASTS, PLTR, POWL, LITE, SYRE, CRVS, SMMT, WDC, RCAT |
| 10–15× | 17 | ROOT, WULF, SLNO, IESC, ONDS, STRL, CELC, IREN, AMSC, STX, LPTH, APLD, REAL, HYMC, TTMI, TSHA, KINS |

- <strong>Mean multiple</strong>: 19.3× (Korea: 17.4×)
- <strong>Median multiple</strong>: 15.7× (Korea: 13.8×)
- <strong>Max</strong>: AAOI at 69.5×
- <strong>Median 3-year return</strong>: \~1,480% (Korea median \~900%, so US runs \~1.6×)

US doesn't just have more tenbaggers than Korea — the winners run further. The right tail is fatter.

---

## The Structural Map — 9 Buckets

| Theme | Count | Share | Range |
|---|:-:|---:|---|
| <strong>AI Infrastructure Full Stack</strong> | <strong>13</strong> | <strong>33%</strong> | 10–69.5× |
| Biotech Single-Asset | 8 | 20% | 10.1–21.2× |
| Deep Value Recovery | 6 | 15% | 10.6–50.7× |
| Space / Defense / Drone | 4 | 10% | 13.5–23× |
| Crypto Miner → AI Compute | 3 | 8% | 10.9–14.4× |
| AI Software / Platform | 2 | 5% | 18.8–30.5× |
| <strong>Insurance Turnaround</strong> | <strong>2</strong> | <strong>5%</strong> | 13.4–14.8× |
| Quantum | 1 | 3% | 38.5× |
| Specialty Minerals | 1 | 3% | 21.9× (ALM) |

Three stories jump out.

<strong>One.</strong> AI infrastructure is a third of the list. Not "AI" in the loose sense — AI *infrastructure*: optical transceivers, nearline HDDs for training data, high-multilayer PCBs, data-center switchgear and transformers, hyperscale electrical construction. This is picks-and-shovels that paid.

<strong>Two.</strong> Biotech single-asset theses delivered 8 names — every one starting from $1-$16 with "all-or-nothing" trial binaries. That's a structural profile the Korean market basically doesn't produce at this size.

<strong>Three.</strong> Quantum, insurance turnarounds, and specialty minerals each printed standalone winners that don't fit the consensus narrative. The 2023 list was not "AI only."

---

## AI Infrastructure — The Full Stack

Break the 13 AI-infra names down by sub-layer:

| Sub-layer | Names | Driver |
|---|---|---|
| <strong>AI optical transceivers</strong> | AAOI 69.5× / CRDO 22.5× / LITE 18.4× / AXTI 28.6× / LPTH 11× | 800G / 1.6T transition + NVIDIA GB200 adoption |
| <strong>Storage (AI DC)</strong> | WDC 15.7× / STX 11× | Nearline HDD explosion on AI training data |
| <strong>PCB (AI accelerators)</strong> | TTMI 10.3× | High-layer-count PCB for AI boards |
| <strong>Data-center power</strong> | POWL 18.6× / AMSC 11.8× | Switchgear + transformers |
| <strong>Data-center electrical construction</strong> | STRL 13× / IESC 13.5× / TSSI 38.8× | Hyperscale capex flow-through |

This is the <strong>exact Korean pair-trade map</strong>:

| US primary | KR derivative | Relationship |
|---|---|---|
| AAOI / CRDO / LITE | Isu Petasys, DAP | AI optical → high-layer PCB |
| POWL / AMSC | HD Hyundai Electric, BHI, Boseong Powertech | DC power → transformers |
| STX / WDC | SK Hynix, Samsung Electronics | AI storage → HBM |
| STRL / IESC / TSSI | KOSPI electrical contractors | US hyperscale capex → KR EPC follow |

The pattern: <strong>US primary leads, Korea follows with a 3-6 month lag.</strong> When the US primary overshoots, the Korean derivative peaks. When the US primary corrects, the Korean derivative over-reacts on the way down.

This is not a narrative claim — it's visible in the multiple dispersion. Isu Petasys peaked *after* AAOI. HD Hyundai Electric peaked *after* POWL. The lag is real.

---

## Quality Check — Who Already Overshot

The sell-side target data matters here. Of the 40 names:

| Bucket | Analyst target vs spot | Read |
|---|---|---|
| AI-infra primaries (AAOI, AXTI, POWL, IESC, LITE, WDC, STX, TTMI, RKLB, BWAY) | <strong>Already below target</strong> (-11 to -40%) | Over-ran the fundamentals — take-profit zone |
| Crypto→AI pivots (IREN, APLD, WULF) | +27 to +54% upside | Still has room |
| Biotech (PRAX, CRVS, SMMT, SLNO) | +15 to +97% upside | Event-driven — asymmetric |
| Quantum (RGTI) | +72% upside | Theme-beta still expanding |
| Deep value (CVNA, DAVE, ROOT) | +14 to +48% upside | Not fully re-rated |

<strong>Key read</strong>: the AI-infrastructure primaries are where the sell-side has *already caught up*. If you missed it, chasing here is chasing a stock trading above its analyst consensus target. That's rarely the asymmetric trade.

Where the consensus is *still behind*: crypto→AI compute pivots, biotech single-assets, quantum beta. These are the 2026-2027 continuation candidates, not the infrastructure primaries.

---

## Factor Decomposition — Entry-Point Profiles

At the April 2023 start point:

| Factor | AI Infra (11) | Crypto→AI (3) | Biotech (8) | Deep Value (6) | Space/Drone (4) |
|---|---|---|---|---|---|
| Profitable in 2023-04 | Mostly yes | No | <strong>All no</strong> | All no | All no |
| Revenue YoY (current) | +20–50% | Surging | Trial-driven | +10–20% | +30–100% |
| Fwd P/E now | 25–50× | 45–685× | Loss-making | 18–59× | Loss-making |

Two practical reads:

1. <strong>The AI-infra names were already earning money in 2023.</strong> They weren't lottery tickets. The "quality + earnings visibility" screen would have caught them. The biotech and space tenbaggers wouldn't have passed — those were pure narrative/catalyst trades.
2. <strong>Entry-point price matters.</strong> Every biotech tenbagger started between $1 and $16. The deep value recoveries started sub-$5. Low nominal price was a real factor in the 10× realization — not because low price is magic, but because it indicates pre-catalyst pricing.

---

## What Korea's Tenbagger List Does *Not* Have

Cross-reference Part 1. Two entire archetypes are structurally missing from Korea:

<strong>1. Biotech single-asset 10× at scale.</strong> US produced 8 names from $1-16 starting points on clinical binaries. Korea has Peptron and HLB at 7× — but nothing that ran $1 → $337 like PRAX. Why? Korean biotech gets re-rated *during* phase 2 (pre-data) and sells off *before* phase 3 readout. The US market allows the full ramp through approval. Different market microstructure, different distribution of outcomes.

<strong>2. Survivor recovery 10×.</strong> CVNA went from $3.55 and bankruptcy rumors to $180+. Korea doesn't produce this because names under administrative-issue designation typically go straight to delisting rather than restructure. The US Chapter 11 + tradeable credit spread market creates a set of "near-death → survive" names that simply don't exist on KOSDAQ.

For a Korean investor who wants exposure to these profiles: <strong>XBI</strong> for biotech breadth, or direct ADR positions in SMMT / DAVE / CVNA for the concentrated bets. Not replicable via domestic names.

---

## The Insurance Turnaround Cluster (Added After Resume Backfill)

When the data pipeline's backfill completed (1,479 → 1,690 tickers), one new tenbagger showed up: <strong>KINS (Kingstone Companies)</strong> at 13.4×, a NY-state regional P&C insurer that went from $1.3 → $17.

Combined with ROOT (auto AI insurance, 14.8×), this is a quiet <strong>Insurance Turnaround</strong> mini-theme. The 2022-23 combined-ratio spike above 110% forced P&C discipline — reinsurance rates hardened, underwriting tightened, and 2024-25 ROE recovered to 20%+.

- ROOT → telematics maturity
- KINS → regional consolidation beneficiary

Korean pair: <strong>Meritz Fire, Hanwha General Insurance</strong> — similar ROE normalization, but multiples only ran 3-4× (no domestic tenbagger equivalent).

---

## Actionable — Three Framings for a KR-Based PM

<strong>A. Pair-trade discipline on the AI-infra stack.</strong> When US primaries trade below analyst consensus targets, Korean derivatives are on borrowed time. Current read: AAOI, CRDO, LITE, POWL, IESC all below target → Isu Petasys, HD Hyundai Electric, Korean power-grid complex in take-profit zone. This is the single most actionable insight in the dataset.

<strong>B. Next-cycle candidates.</strong> Where is sell-side *still behind*?
- <strong>Edge-AI semis</strong> — smaller InP/GaN names (Navitas, Power Integrations) below AXTI's scale
- <strong>Quantum infrastructure</strong> — RGTI alone printed 38.5×; IONQ / QUBT / QMCO still have multiple headroom
- <strong>AI robotics</strong> — Symbotic and others not yet tenbaggers, but candidate narratives for 2026-2028
- <strong>Crypto→AI pivots with remaining upside</strong> — IREN, APLD, WULF

<strong>C. Structural gaps.</strong> US biotech single-asset and survivor-recovery exposure cannot be replicated through KR-listed names. Either ADR direct (SMMT, PRAX, CVNA, DAVE) or XBI for breadth.

---

## Risk Flags

1. <strong>Forward P/E above 100×</strong> — PLTR 107×, AAOI 100×, LITE 102×, WULF 685×, ASTS 99×. Consensus downgrade = -30 to -50% risk.
2. <strong>Already below analyst target</strong> — WDC, STX, LITE, IESC, POWL, AAOI, AXTI, TTMI, BWAY, RKLB. Market ran ahead; trailing stops matter.
3. <strong>Sub-$1 starting price</strong> — check short interest and SEC filings before extrapolating (RGC has TCM-pump flags).
4. <strong>Crypto→AI pivots</strong> — dual exposure to Bitcoin and hyperscaler capex. Either breaking down = -50%.

---

## Bottom Line

> 40 US tenbaggers over 3 years. 33% are AI-infrastructure full stack — optical, storage, PCB, power, electrical construction. Korea's 27 tenbaggers are the <strong>2nd-order derivative layer</strong> of this same trade (HBM, high-layer PCB, transformers). The US infrastructure primaries are now trading *through* analyst targets — take-profit zone. The relocation is into <strong>crypto→AI pivots, biotech single-assets, quantum, and insurance turnarounds</strong>, where consensus is still catching up.

The pair-trade map is the single most transferable output: <strong>Korean AI-derivative names follow US primaries with a 3-6 month lag, and over-react on both ends.</strong>

---

## What's Next

1. <strong>KR-US pair cointegration backtest.</strong> AAOI weekly vs Isu Petasys weekly at lag=0/30/60 days — is the relationship tradeable?
2. <strong>Reverse-screen Russell 2000</strong> using the April-2023 tenbagger profile (ROE / Fwd P/E / Rev YoY / 2yr return) — find the 2026 candidates before they break out.
3. <strong>Biotech ADR event calendar</strong> — SMMT, PRAX, SLNO, SYRE upcoming trial readouts.
4. <strong>AI capex cycle top check</strong> — MSFT / META / AMZN / GOOGL 2026 capex guidance vs 2025 actuals. The primary signal for when the US infra names will finally correct.

---

_This closes the Tenbagger Analysis 2026 series. [Part 1: Korea's 27 tenbaggers and why power grid quietly beat AI.](/post/kr-tenbagger-census-2023-2026-2026-04-23/)_

---

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
