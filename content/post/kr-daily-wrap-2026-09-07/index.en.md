---
title: "Korea Quality Re-Rating Watch 2026-09-07: Data Refresh Pending — Regime Inputs Blocked"
date: 2026-09-07T16:30:00+09:00
categories: ["daily-wrap"]
tags: ["KOSPI", "Korea stocks", "Quality Compounder", "Smart Money", "Cycle Rerating", "Korea market", "data gap"]
series: ["korea-quality-rerating-watch"]
slug: "kr-daily-wrap-2026-09-07"
description: "Korea market wrap for Sep 7 2026: macro regime inputs blocked, close briefing unavailable. Screener refresh pending. (131 chars)"
draft: false
---

## Macro Dashboard

| Indicator | Value | Status |
|-----------|-------|--------|
| KOSPI | — | source unavailable |
| KOSDAQ | — | source unavailable |
| USD/KRW | — | source unavailable |
| VIX | — | source unavailable |
| Brent | — | source unavailable |
| US 10Y | — | source unavailable |

**KR Regime:** UNKNOWN · **US Regime:** UNKNOWN

The macro-regime pipeline flagged a data-quality block before generating today's verdict. Three inputs failed validation: the Korea screener snapshot, the US screener snapshot, and the 10-day Korea derivatives/passive flow gauge. The pipeline correctly withheld the regime call rather than publish a verdict on stale inputs. Once the source screeners and derivatives snapshot are refreshed, the pipeline will re-run.

---

## Market Wrap — Sep 7, 2026

*Close-briefing source: unavailable for this date. The section below is limited accordingly.*

No same-day Korea close briefing was present in today's data package. The KR Close Briefing feed is the primary source for KOSPI and KOSDAQ session narratives, sector rotation detail, and foreign/institutional flow data. Without it, publishing fabricated or estimated session color would violate this series' data-integrity rule.

If you are monitoring Korea markets in real time, primary reference points remain the Korea Exchange (KRX) official close data and the Financial Supervisory Service investor-type trading figures, both published after the 3:30 p.m. KST close.

The next edition will incorporate a full session recap once the briefing pipeline is restored.

---

## Today's Quality Re-Rating Candidates

*KR Meta Screener source: unavailable for this date. No ranked candidates can be confirmed.*

The Quality Re-Rating candidate table requires three converging data layers to be meaningful:

1. **Quality Compounder screen** — filters for businesses with durable return profiles (ROE, operating margin, capital efficiency) before any flow or timing signal is considered.
2. **Smart Money Quality / Smart Money Earnings** — checks whether institutional and foreign money is actually moving into those names, not just whether the financials look good on paper.
3. **Cycle Rerating / PEAD** — adds the timing dimension: is the earnings cycle being re-priced, and is there post-announcement drift still unfolding?

Today's screener composite did not produce a validated output. Running the candidate table on incomplete inputs risks false positives — names that appear to hit multiple screeners only because one layer is stale — which is precisely the noise this framework is designed to filter out.

When the screener data is refreshed, the standard candidate ranking logic applies:
- **Tier 1** (highest priority): names hitting Quality Compounder + Smart Money Quality + Cycle Rerating simultaneously
- **Tier 2**: Quality Compounder + Smart Money Quality, or Quality Compounder + Cycle Rerating
- **Tier 3**: Smart Money Quality paired with Smart Money Earnings or PEAD

Single-screener names are not elevated unless the session's market character provides exceptional corroborating context — and that context requires a valid close briefing, which is also absent today.

---

*Data gaps: macro-regime verdict withheld (pipeline block); KR close briefing absent; KR meta screener absent. All three gaps trace to the same upstream screener and derivatives snapshot refresh. No numbers have been estimated or back-filled. This edition will be updated if a same-day data refresh becomes available.*