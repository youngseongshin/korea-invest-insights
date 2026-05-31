---
title: "Is FADU Korea's Sandisk Beta? Foreign Flows and the AI Storage Bottleneck"
date: 2026-05-31T13:20:00+09:00
description: "A Korea AI-storage read-through comparing FADU, Sandisk, Jeju Semiconductor and Western Digital across price beta, foreign flows, eSSD controllers and NAND scarcity."
categories: ["Market-Outlook"]
tags:
  - "FADU"
  - "440110"
  - "Sandisk"
  - "SNDK"
  - "Jeju Semiconductor"
  - "080220"
  - "AI storage"
  - "NAND"
  - "eSSD"
  - "enterprise SSD"
  - "Korean semiconductors"
  - "foreign flows"
  - "Western Digital"
  - "WDC"
slug: fadu-sandisk-ai-storage-korea-beta-jeju-semiconductor-2026-05-31
valley_cashtags:
  - 파두
  - 제주반도체
  - SK하이닉스
  - 삼성전자
draft: false
---

> Context
> This note follows [SK Hynix vs Micron](/post/sk-hynix-vs-micron-hbm-premium-ai-memory-platform-2026-05-31/) and the [AI Infrastructure Multiple Map](/post/ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31/). Those notes focused on HBM and mega-cap memory. This one moves down the stack into <strong>AI storage, NAND and eSSD controllers</strong>. Related hubs: [AI HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/) and [Korea Semiconductor Value Chain Hub](/page/korea-semiconductor-equipment-ip-hub/).

## TL;DR

FADU is starting to behave like a Korean high-beta proxy for Sandisk, but the relationship is still early. The strongest evidence is not daily price correlation; it is foreign flow. Since May 2026, foreigners net bought about <strong>KRW 445.1bn</strong> of FADU while domestic institutions net sold about <strong>KRW 215.2bn</strong>. Over the same period, FADU rose +38.1% and Sandisk rose +35.0%.

The price beta is weaker than the SK Hynix-Micron pair. Sandisk's prior-U.S.-session return versus FADU's next Korea-session return correlation is +0.16 since May and +0.42 over the latest 10-14 trading days. Micron-to-Hynix is +0.57 and +0.55. Translation: <strong>foreign flow says yes, domestic institutions say no, and the broader market pair is still forming</strong>.

The conclusion: <strong>FADU is a candidate Korean beta for AI storage/NAND</strong>, but valuation is already demanding. Structurally, FADU is cleaner. Numerically, Jeju Semiconductor looks cheaper. Globally, Sandisk screens as the cleaner conditional buy candidate for FY2027, while Western Digital already prices in much of the HDD bottleneck.

---

## Data Basis and Coverage

The analysis covers <strong>2026-01-01 to 2026-05-29</strong>. FADU and SK Hynix prices and investor flows use Research OS local DB tables `prices_daily` and `investor_flow_daily`. Sandisk and Micron prices use Yahoo Finance/yfinance.

Coverage limits matter. Some May FADU individual flow and detailed institution-subtype fields are blank in the local DB, so this note judges FADU mainly through foreign and institution totals. U.S. names do not have Korean-style investor-flow data.

![FADU vs Sandisk YTD price and rolling correlation](2026-05-31_fadu_sndk_ytd_normalized_rollingcorr.png)

![FADU and SK Hynix cumulative foreign/institution flow comparison](2026-05-31_fadu_sndk_flow_cumulative_hynix_comp.png)

---

## 1. Is FADU Following Sandisk?

On price level, yes. FADU rose from KRW 21,250 to KRW 112,100 year-to-date, up about +427.5%. Sandisk also rallied sharply. Both are being repriced around AI storage and NAND scarcity.

But daily return linkage is still modest.

| Item | Sandisk → FADU | Micron → SK Hynix | Interpretation |
|---|---:|---:|---|
| YTD price-level correlation | +0.91 | high | Same broad uptrend |
| Prior U.S. day → next Korea day return | +0.12 | +0.46 | FADU pair still weak |
| Since May | +0.16 | +0.57 | Hynix-Micron is much more structural |
| Latest 10-14 sessions | +0.42 | +0.55 | FADU beta has recently strengthened |

The key distinction is that "both went up" is not the same as "FADU mechanically tracks Sandisk." FADU is not yet a mature pair trade. But the recent correlation jump suggests investors are beginning to map the relationship.

---

## 2. The Real Signal Is Foreign Flow

Since May, FADU's flow profile has been unusually clear.

| Period | FADU Return | Sandisk Return | FADU Foreign Flow | FADU Institution Flow | Foreign Positive-Day Ratio |
|---|---:|---:|---:|---:|---:|
| 2026 YTD | +427.5% | strong rally | +KRW 528.2bn | -KRW 173.2bn | 46.4% |
| Since May | +38.1% | +35.0% | +KRW 445.1bn | -KRW 215.2bn | 83.3% |
| Latest 10-14 sessions | +11.7% | +9.5% | +KRW 346.4bn | -KRW 194.1bn | 85.7% |

This is not a domestic-institution-led move. It is closer to a foreign-discovery trade in a Korean high-beta proxy for AI storage/NAND.

---

## 3. Why It Is Weaker Than SK Hynix-Micron

SK Hynix and Micron are both large-cap global memory stocks tied to the same HBM/DRAM cycle. Their earnings line items, investor base and product overlap are more directly comparable.

FADU and Sandisk are different. Sandisk is a global NAND and data-center SSD company. FADU is closer to an eSSD controller, firmware and enterprise SSD solution fabless company. Both benefit from the AI storage cycle, but the economics and customer-validation risks are not identical.

The clean framing is:

> Sandisk = global AI storage/NAND thermometer
> FADU = foreign-discovered Korean high-beta proxy
> Key validation = continued foreign buying + breakout above KRW 118,500 + less institution selling

---

## 4. FADU and Jeju Through the "Next SEMCO" Lens

The Samsung Electro-Mechanics re-rating showed how a seemingly small component can be reclassified as an AI infrastructure bottleneck. Applying the same frame to memory/storage gives five tests: bottleneck, P up, Q up, customer validation and multiple reclassification.

| Company | Bottleneck | Strength | Weakness | View |
|---|---|---|---|---|
| FADU | AI eSSD controller / firmware / SSD solution | Cleanest structural AI-storage bottleneck in Korea | Valuation already rich | Watch / Wait |
| Jeju Semiconductor | LPDDR4X, MCP, legacy low-power memory | Looks much cheaper on current numbers | Needs proof that 1Q26 repeats | Tactical Watchlist |
| Sandisk | NAND / data-center SSD | Global AI storage/NAND thermometer, cheaper FY2027 setup | NAND peak-out risk | Conditional Buy candidate |
| Western Digital | HDD capacity / nearline storage | Strong HDD cash-flow bottleneck | Much of the premium reflected | Low appeal for fresh entry |

---

## 5. FADU: Strong Structure, Difficult Price

FADU's structural thesis is strong. AI data centers are not just a GPU/HBM story. KV-cache, checkpoints, training/inference pipelines, enterprise SSDs, controllers and firmware become parallel bottlenecks. FADU sits near the <strong>eSSD controller and firmware qualification</strong> layer.

Public reporting says FADU posted Q1 2026 revenue of KRW 59.5bn and operating profit of KRW 7.7bn, returning to profitability, with disclosed new orders reaching KRW 166.3bn by April. ([StorageNewsletter][1])

The issue is price. The input research cites MarketScreener estimates of KRW 323.3bn 2026E revenue and KRW 584.8bn 2027E revenue, with 2027E P/E around 38x. That is not cheap for a company that still needs to convert orders into revenue and margin.

### Upgrade Conditions

| Watch Item | Buy Upgrade Trigger |
|---|---|
| Price | Break and hold above KRW 118,500 with turnover |
| Flow | Continued foreign buying and less institution selling |
| Earnings | Q2 revenue KRW 70-80bn, OPM above 15%, ideally 20% |
| Orders | Cumulative new orders above KRW 400bn |
| Products | Gen6 / CXL / low-latency SSD design wins |

Invalidation: foreign buying stops despite Sandisk strength, FADU breaks below KRW 105,900 with foreign selling, orders fail to convert, OPM falls below 10%, or controller mix declines.

---

## 6. Jeju: Cheaper Numbers, Higher Repeatability Risk

As discussed in the [Jeju Semiconductor 1Q26 note](/post/jeju-semiconductor-1q26-earnings-legacy-memory-squeeze-2026-05-15/), Jeju is not an HBM company. It benefits from shortages in LPDDR4X, MCP and low-power memory as Samsung, SK Hynix and Micron allocate more capacity toward HBM and server DRAM.

Jeju's Q1 2026 operating margin was 37.2% on KRW 180.4bn revenue and KRW 67.1bn operating profit. TrendForce expects 2Q26 LPDDR4X ASPs to rise +70-75% QoQ and LPDDR5X +78-83%. ([TrendForce][2])

On simple annualized Q1 numbers, Jeju looks cheaper than FADU. But the question is repeatability. If Q1 was peak margin, it is a trap. If Q2 revenue stays above KRW 180bn and OPM remains above 30%, it becomes a tactical undervaluation candidate.

---

## 7. Global Read-Through: Sandisk Screens Best, WDC Less Clean

Sandisk is the global AI storage/NAND thermometer. Fiscal Q2 2026 revenue was $3.025bn, GAAP net income was $803m and non-GAAP EPS was $6.20. The company guided fiscal Q3 revenue to $4.4-4.8bn and non-GAAP EPS to $12-14. ([Sandisk][3])

Western Digital has a strong HDD bottleneck and cash-flow story. Fiscal Q3 2026 revenue was $3.337bn, GAAP gross margin was 50.2% and operating cash flow was $1.12bn. But fresh-entry appeal is lower because much of the HDD scarcity premium is already recognized. ([Western Digital][4])

| Company | Core Exposure | View |
|---|---|---|
| Sandisk | NAND, data-center SSD | Conditional Buy candidate |
| Jeju Semiconductor | LPDDR/MCP legacy memory squeeze | Tactical Watchlist |
| FADU | AI eSSD controller / firmware | Watch / Wait |
| Western Digital | HDD capacity / cash flow | Less attractive for fresh entry |

---

## Final View

FADU is <strong>starting</strong> to be interpreted as Korea's Sandisk beta. It is not yet a mature global pair like SK Hynix-Micron. But KRW 445.1bn of foreign net buying since May is too large to dismiss.

| Setup | Action |
|---|---|
| Sandisk strong + FADU foreign buying continues + KRW 118,500 breakout | Recognize FADU as Korean AI-storage beta; conditional Buy upgrade |
| Sandisk strong but FADU foreign flow slows and institutions keep selling | Beta failure; watch for theme peak |
| Sandisk corrects but FADU foreign buying persists | Upgrade toward FADU-specific alpha |
| Break below KRW 105,900 + foreign net selling | Risk management |

One sentence:

> FADU is being discovered as Korea's high-beta proxy for AI storage/NAND, but the right stance is Watch / conditional Buy, not blind chase.

---

## Evidence Classes

### [Fact]

* FADU Q1 2026 revenue was KRW 59.5bn, operating profit was KRW 7.7bn, and disclosed new orders reached KRW 166.3bn by April. ([StorageNewsletter][1])
* TrendForce expects LPDDR4X ASP +70-75% QoQ and LPDDR5X +78-83% QoQ in 2Q26. ([TrendForce][2])
* Sandisk fiscal Q2 2026 revenue was $3.025bn, GAAP net income was $803m and non-GAAP EPS was $6.20. ([Sandisk][3])
* Western Digital fiscal Q3 2026 revenue was $3.337bn, GAAP gross margin was 50.2% and operating cash flow was $1.12bn. ([Western Digital][4])
* FADU-Sandisk flow/correlation work is based on Research OS local DB and yfinance data through 2026-05-29.

### [Inference]

* FADU is not a direct Sandisk tracker yet; it is a foreign-discovered Korean high-beta proxy for AI storage/NAND.
* Jeju is a tactical low-power memory squeeze candidate, not the cleanest structural AI-storage bottleneck.

### [Blocked]

* FADU customer-level orders, controller ASP, gross margin and Gen6/CXL design wins.
* U.S.-name investor-flow data comparable to Korean foreign/institution flow.
* Jeju 2Q26 repeatability and working-capital quality.

[1]: https://www.storagenewsletter.com/2026/05/12/fadu-fiscal-1q26-financial-results/ "FADU: Fiscal 1Q26 Financial Results - StorageNewsletter"
[2]: https://www.trendforce.com/presscenter/news/20260514-13044.html "Mobile DRAM Contract Prices Continue Rising in 2Q26, Pressuring Smartphone Production, Says TrendForce"
[3]: https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-second-quarter-2026-financial-results "Sandisk Reports Fiscal Second Quarter 2026 Financial Results"
[4]: https://www.westerndigital.com/en-ca/company/newsroom/press-releases/2026/2026-04-30-wd-reports-fiscal-third-quarter-2026-financial-results "WD Reports Fiscal Third Quarter 2026 Financial Results"
