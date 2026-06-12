---
title: "Korea Theme ETF Rebalance Flow: Semicap Redistribution Buy Pressure, Megacap Cap-Trim Risk"
date: 2026-06-12T17:40:00+09:00
description: "The first KR Theme ETF Rebalance Flow v1 run flagged Korea theme ETF cap-redistribution pressure. As of June 12, 2026, semiconductor equipment/material names such as Leeno, EO Technics, Soulbrain, DB HiTek, Hanmi Semiconductor, ISC and Wonik IPS screened as redistribution-buy candidates, while SK Hynix, Samsung Electro-Mechanics and LS ELECTRIC appeared on cap-trim watch."
categories: ["Korean-Equities", "Market-Flow", "ETF-Flow"]
tags: ["Korea ETFs", "ETF rebalance", "passive flow", "semiconductor equipment", "SK Hynix", "Samsung Electro-Mechanics", "Hanmi Semiconductor"]
series: ["korea-rerating-2026", "korea-market-flow"]
slug: "kr-theme-etf-rebalance-flow-semicap-cap-trim-2026-06-12"
draft: false
---

> Context  
> This follows [Have Foreign Investors Returned?](/post/foreign-return-after-24-day-kospi-selling-memory-rebalance-2026-06-12/), [Real Money Flow Framework](/post/real-money-flow-framework-korea-institution-quality-2026-06-03/), [Korea Has Liquidity, But Breadth Has Broken](/post/korea-market-liquidity-foreign-reallocation-adr-narrow-leadership-2026-06-03/), [Samsung C&T as a Samsung Electronics proxy](/post/samsung-ct-samsung-electronics-proxy-nav-gap-trade-2026-06-01/) and the [Korea Semiconductor / HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/).

## TL;DR

- Thesis OS added **KR Theme ETF Rebalance Flow v1**, a monitor for potential mechanical flow from Korea theme ETF periodic rebalances and constituent cap adjustments.
- The first run scanned **31 ETFs**, found **30 valid ETFs**, processed **291 constituent rows**, and produced **69 candidates**: **60 redistribution-buy** and **9 cap-trim** candidates.
- The strongest signal was not nuclear/SMR. It was **semiconductor equipment and materials redistribution**.
- Leeno Industrial, EO Technics, Soulbrain, DB HiTek, Hanmi Semiconductor, ISC and Wonik IPS screened as the strongest redistribution-buy candidates.
- SK Hynix, Samsung Electronics, Samsung Electro-Mechanics, LS ELECTRIC and Doosan Enerbility screened as cap-trim pressure candidates.

<div class="thesis-callout">
  <div class="thesis-callout__label">Core Point</div>
  <div class="thesis-callout__body">
    This is not an automatic buy list. It is a way to identify where theme ETFs may cut oversized leaders and redistribute weight into second-line constituents. As of June 12, the clearest pocket was Korean semiconductor equipment and materials.
  </div>
</div>

## 1. What The Monitor Measures

The monitor estimates a cap-redistribution proxy:

```text
ETF-level flow = ETF NAV × target weight delta
Ticker-level flow = sum of ETF-level flows
Flow intensity = estimated flow / 20-day average trading value
```

It uses Naver mobile ETF surface data, including `constituentList` and `totalNav`, plus local `prices_daily` ADV20. If a constituent is above an assumed cap, the model cuts it back to cap and redistributes the excess to under-cap constituents in proportion to current weights.

This is **not official PCF data**. Before treating it as a trade signal, investors need issuer PDFs/PCF, index methodology, actual cap rules, and closing-auction evidence.

| Item | Value |
|---|---:|
| Date | 2026-06-12 |
| ETFs scanned | 31 |
| Valid ETFs | 30 |
| Constituent rows | 291 |
| Total candidates | 69 |
| Redistribution-buy candidates | 60 |
| Cap-trim candidates | 9 |
| Confidence | medium-low |

## 2. Top Redistribution-Buy Candidates

| Rank | Name | Signal | Est. flow | Flow/ADV20 | Day return | Main ETFs |
|---:|---|---|---:|---:|---:|---|
| 1 | Leeno Industrial | Redistribution buy | KRW 270.4bn | +2.68x | +4.7% | TIGER Semiconductor TOP10, KODEX AI Semiconductor TOP2 Plus |
| 2 | EO Technics | Redistribution buy | KRW 197.8bn | +2.49x | +21.4% | TIGER Semiconductor TOP10 |
| 3 | Soulbrain | Redistribution buy | KRW 69.4bn | +2.44x | +24.4% | TIGER Semiconductor TOP10 |
| 4 | DB HiTek | Redistribution buy | KRW 264.3bn | +2.02x | +12.3% | TIGER Semiconductor TOP10, KODEX AI Semiconductor TOP2 Plus |
| 5 | Hanmi Semiconductor | Redistribution buy | KRW 721.0bn | +1.81x | +24.1% | TIGER Semiconductor TOP10, KODEX AI Semiconductor TOP2 Plus |
| 6 | ISC | Redistribution buy | KRW 92.0bn | +1.76x | +20.7% | TIGER Semiconductor TOP10, SOL AI Semiconductor TOP2 Plus |
| 7 | Wonik IPS | Redistribution buy | KRW 211.1bn | +1.63x | +30.0% | TIGER Semiconductor TOP10 |
| 8 | HPSP | Redistribution buy | KRW 143.7bn | +0.66x | +30.0% | TIGER Semiconductor TOP10, KODEX AI Semiconductor TOP2 Plus |

The important field is not only absolute flow. It is **flow intensity versus liquidity**. Leeno, EO Technics, Soulbrain, ISC and Wonik IPS screen as names where estimated ETF redistribution may be large relative to normal trading value.

## 3. Cap-Trim Watch

| Rank | Name | Signal | Est. flow | Flow/ADV20 | Day return |
|---:|---|---|---:|---:|---:|
| 1 | SK Hynix | Cap trim | -KRW 1.76tn | -0.15x | +2.3% |
| 2 | Samsung Electronics | Cap trim | -KRW 49.4bn | -0.00x | +7.9% |
| 3 | Samsung Electro-Mechanics | Cap trim | -KRW 514.9bn | -0.21x | -5.0% |
| 4 | LS ELECTRIC | Cap trim | -KRW 47.0bn | -0.15x | -3.0% |
| 5 | HD Hyundai Heavy Industries | Cap trim | -KRW 21.8bn | -0.06x | +0.6% |
| 6 | Hanwha Ocean | Cap trim | -KRW 7.8bn | -0.04x | +7.8% |
| 7 | Doosan Enerbility | Cap trim | -KRW 26.5bn | -0.07x | +5.1% |

Cap-trim does not mean short. Large names can absorb technical ETF selling if foreign or institutional demand is strong. The more useful interpretation is: **do not chase cap-trim names unless price action proves real demand is absorbing the mechanical supply**.

## 4. Nuclear / SMR Was Watch, Not The Main Signal

Nuclear names appeared in Priority Watch, but the signal strength was lower than semicap redistribution.

| Name | Signal | Est. flow | Flow/ADV20 | Day return |
|---|---|---:|---:|---:|
| KEPCO Engineering | Redistribution buy | KRW 2.85bn | +0.13x | +30.0% |
| Doosan Enerbility | Cap trim | -KRW 26.5bn | -0.07x | +5.1% |
| Hyundai Engineering & Construction | Redistribution buy | KRW 8.75bn | +0.06x | +28.4% |
| BHI | Redistribution buy | KRW 1.57bn | +0.06x | +30.0% |
| Woori Technology | Redistribution buy | KRW 2.91bn | +0.04x | +30.0% |

## 5. Trade Discipline

Treat this as an event screen, not a final signal.

| Step | Required confirmation |
|---|---|
| 1 | Check issuer ETF PDF/PCF and index methodology |
| 2 | Confirm closing-auction and end-of-day volume |
| 3 | Check T+1/T+3 relative strength |
| 4 | Confirm program, foreign or institutional flow alignment |
| 5 | Upgrade only the strongest names to watchlist or small event trade |

## Final View

The first KR Theme ETF Rebalance Flow run says the strongest June 12 passive-flow setup was **semiconductor second-line redistribution**, not broad Korea beta and not nuclear/SMR as the primary signal.

The signal is useful because it quantifies where ETF mechanics may redirect weight after megacap concentration. It remains a **medium-low confidence proxy** until official PCF/PDF and actual close-auction flow confirm it.

## Evidence Ledger

| Item | Source | Detail |
|---|---|---|
| Monitor | Thesis OS / Alpha | KR Theme ETF Rebalance Flow v1 |
| Local report | Vault `2026-06-12_theme_etf_rebalance_flow.md` | 31 ETFs scanned, 30 valid, 69 candidates |
| External Signal Judge input | Vault candidate file | Candidate score, flow, intensity and confidence |
| Data | Naver ETF surface + local DB | `constituentList`, `totalNav`, `prices_daily` ADV20 |

## Caveat

This is not investment advice and not a confirmed PCF-based trade instruction. It is a cap-redistribution proxy that requires issuer confirmation and post-event validation.
