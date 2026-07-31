---
title: "Who Was Buying on Non-Arbitrage Inflow Days? A 16-Stock KOSPI 200 Flow Screen"
date: 2026-07-31T12:40:00+09:00
description: "A cross-screen of foreign cash buying, single-stock program flow, investment trusts, and pensions on KOSPI non-arbitrage inflow days, combined with FY2026 operating-profit revisions."
categories: ["Exclusive Analysis", "Market Flow", "Korea Market"]
tags:
  - "KOSPI 200"
  - "non-arbitrage program"
  - "foreign flow"
  - "investment trusts"
  - "pensions"
  - "real money"
  - "HMM"
  - "Kakao"
  - "Korea Gas Corporation"
  - "Nongshim"
  - "Samyang Foods"
  - "Celltrion"
series: ["exclusive-analysis", "korea-rerating-2026", "korea-daily-market"]
slug: "kospi200-non-arbitrage-spot-real-money-cross-screen-2026-07-31"
valley_cashtags:
  - HMM
  - Kakao
  - Korea Gas Corporation
  - Nongshim
  - Samyang Foods
  - Celltrion
  - LG Electronics
  - NAVER
draft: false
---

Futures are useful for reading broad market direction, but they are noisy tools for finding individual stocks. Index futures mix directional trades, cash-market hedges, basis arbitrage, options delta adjustments, and cross-market relative value. Foreign cash buying and stock-level purchases by investment trusts and pensions provide a clearer view of actual security selection.

This screen starts from that distinction. It first identifies the ten trading days between July 1 and July 30, 2026 when KOSPI non-arbitrage program flow was positive. It then retains KOSPI 200 stocks for which foreign cash flow, single-stock program flow, investment-trust flow, and pension flow were all positive both across those ten days in aggregate and across the full July window.

Sixteen stocks passed. We then compared FY2026 operating-profit consensus on June 30 and July 30 to distinguish confirmed earnings candidates from cyclical revisions, early turnaround buying, and value or shareholder-return trades.

> Context: This is a follow-up to our [real-money flow framework](/en/post/real-money-flow-framework-korea-institution-quality-2026-06-03/), [accumulation and absorption screen](/en/post/kr-flow-accumulation-absorption-screen-2026-05-15/), and [Korean non-semiconductor breadth study](/en/post/korea-nonsemiconductor-ytd-leaders-kospi-kosdaq-breadth-2026-07-10/). Related research is available in the [Korea Daily Market hub](/en/page/korea-daily-market-hub/) and [Exclusive Analysis hub](/en/page/exclusive-analysis-hub/).

## TL;DR

* KOSPI non-arbitrage flow was positive on ten days from July 1 to July 30. Aggregate inflow on those days was approximately KRW 10.83 trillion.
* Sixteen KOSPI 200 stocks had positive foreign cash, stock-program, investment-trust, and pension flow both on those ten days in aggregate and across the full month.
* The most interesting entry asymmetries are HMM, Kakao, Korea Gas Corporation, and Nongshim. HMM had the strongest earnings revision, but it remains a freight-rate-sensitive cyclical trade.
* Celltrion, Samyang Foods, LG Electronics, Amorepacific, and Nongshim offer the best alignment between flows and fundamentals. Celltrion and Samyang Foods are strong leaders, making pullbacks preferable to chasing.
* NAVER and LG Electronics attracted substantial cumulative buying despite sharp price declines. This may be absorption, but it may also mean that existing buyers are underwater. Recent three-to-five-day re-accumulation is required.
* Single-stock program data are not separated into arbitrage and non-arbitrage components. The market-level non-arbitrage series is a gate; stock-level flow is total program flow.
* A date-format duplication was found in Kia's stock-program records. After keeping the latest observation per trading day, July program buying was approximately KRW 192.8 billion rather than KRW 177.0 billion.

<div class="thesis-callout">
  <div class="thesis-callout__label">Bottom line</div>
  <div class="thesis-callout__body">
    HMM is the strongest cyclical revision candidate, Kakao is an expectations-led setup, Korea Gas Corporation is a policy and dividend option, and Nongshim is an early earnings transition. Celltrion and Samyang Foods are higher-quality businesses, but their entry points require more patience.
  </div>
</div>

## 1. Screening methodology

### Why exclude futures?

```text
Futures flow
├─ market-direction exposure
├─ cash-portfolio hedging
├─ cash-futures arbitrage
├─ options delta and gamma hedging
└─ country and sector relative value
```

A foreign futures purchase can represent a bullish view, a hedge against a short cash book, or an options adjustment. Stock-level cash and institutional data are better suited to security selection.

### Four filters

| Step | Condition | Purpose |
|---|---|---|
| 1 | Identify positive KOSPI non-arbitrage program-flow days from July 1 to July 30 | Find sessions with basket and passive inflow |
| 2 | Require positive aggregate foreign cash, stock-program, trust, and pension flow across those ten sessions | Find securities selected during inflow days |
| 3 | Require all four flows to remain positive for the full July window | Exclude one-day buying |
| 4 | Limit the universe to the July 30 KODEX 200 constituent snapshot | Improve liquidity and comparability |

“Positive on the ten sessions” means positive in aggregate across the ten dates. It does not mean that all four buyers were positive on every single date. Actual four-way positive-session counts ranged from one to seven.

### Positive non-arbitrage sessions

| Date | KOSPI non-arbitrage flow |
|---|---:|
| July 8 | +KRW 800.2B |
| July 9 | +KRW 1,247.8B |
| July 14 | +KRW 609.8B |
| July 15 | +KRW 1,818.1B |
| July 20 | +KRW 680.0B |
| July 21 | +KRW 847.9B |
| July 22 | +KRW 1,524.3B |
| July 23 | +KRW 1,800.1B |
| July 29 | +KRW 142.7B |
| July 30 | +KRW 1,354.6B |
| <strong>Total</strong> | <strong>+KRW 10,825.5B</strong> |

## 2. Data validation and corrections

The local database reproduced exactly 16 passing securities. Foreign, investment-trust, and pension data came from Kiwoom's stock-level investor series. Stock-program and market non-arbitrage data came from Kiwoom REST. The KOSPI 200 universe used the July 30 Naver KODEX 200 constituent snapshot.

Three adjustments matter:

1. Single-stock program flow is total program flow, not official stock-level non-arbitrage flow.
2. Kia had duplicated records for several early-July dates stored in two timestamp formats. Deduplication raises its July program total from KRW 177.0 billion to KRW 192.8 billion.
3. Returns were recalculated consistently from the July 1 close to the July 30 close. Five-day returns use July 23 to July 30. This changes Samyang Foods to +7.0%, Kia to -14.6%, and Nongshim to +13.5%.

July 31 intraday prices are excluded because flow and consensus data end on July 30.

## 3. Sixteen passing stocks

Flow values are in KRW 100 million.

| Stock | Foreign | Program | Trust | Pension | Jul. 1-30 | 5D | Assessment |
|---|---:|---:|---:|---:|---:|---:|---|
| SK Innovation | +67 | +420 | +796 | +2,670 | +19.0% | -11.8% | Pension-led, needs stabilization |
| LG Electronics | +1,386 | +1,872 | +93 | +405 | -23.4% | -21.1% | Absorption or damaged trend |
| Samyang Foods | +943 | +1,506 | +740 | +431 | +7.0% | +10.3% | Strong leader |
| Celltrion | +105 | +443 | +725 | +2,116 | +8.9% | +10.3% | Strong leader |
| NAVER | +208 | +968 | +659 | +1,367 | -1.4% | -11.5% | Flow not reflected in price |
| Kia | +1,324 | <strong>+1,928</strong> | +61 | +12 | -14.6% | -19.4% | Trend repair required |
| Kakao | +980 | +1,253 | +75 | +78 | +3.9% | -2.7% | Early accumulation candidate |
| HMM | +789 | +859 | +148 | +511 | +10.7% | -1.7% | Pullback candidate |
| Amorepacific | +656 | +491 | +266 | +618 | +18.0% | +12.6% | Strong but extended |
| LG H&H | +584 | +688 | +62 | +401 | +23.7% | +17.7% | Short-term overextension |
| Hyundai Glovis | +722 | +553 | +10 | +391 | -3.0% | -6.3% | Needs stabilization |
| IBK | +257 | +418 | +102 | +65 | +1.0% | -2.9% | Quiet value accumulation |
| Nongshim | +194 | +194 | +106 | +132 | +13.5% | +6.3% | Trend-transition candidate |
| Korea Gas Corp. | +184 | +191 | +12 | +18 | +5.8% | +0.1% | Low-heat accumulation |
| Pan Ocean | +85 | +168 | +66 | +24 | +2.8% | -6.9% | Needs trend recovery |
| Poongsan | +80 | +93 | +55 | +15 | -9.4% | -8.1% | Still in a downtrend |

## 4. Buying on the ten inflow days

| Stock | Foreign | Program | Trust | Pension | Four-way positive days |
|---|---:|---:|---:|---:|---:|
| SK Innovation | +291 | +443 | +396 | +1,344 | 3 |
| LG Electronics | +1,137 | +1,421 | +68 | +537 | 3 |
| Samyang Foods | +167 | +456 | +414 | +79 | 1 |
| Celltrion | +236 | +572 | +305 | +692 | 3 |
| NAVER | +467 | +1,072 | +262 | +808 | 2 |
| Kia | +567 | +1,771 | +16 | +90 | 2 |
| Kakao | +496 | +808 | +35 | +74 | 3 |
| HMM | +500 | +564 | +67 | +273 | <strong>7</strong> |
| Amorepacific | +600 | +523 | +58 | +15 | 2 |
| LG H&H | +405 | +456 | +49 | +260 | 2 |
| Hyundai Glovis | +334 | +262 | +7 | +196 | 2 |
| IBK | +15 | +115 | +5 | +41 | 2 |
| Nongshim | +57 | +60 | +15 | +65 | <strong>5</strong> |
| Korea Gas Corp. | +84 | +87 | +4 | +13 | 4 |
| Pan Ocean | +72 | +123 | +15 | +8 | 3 |
| Poongsan | +67 | +67 | +17 | +9 | 4 |

HMM had seven four-way positive sessions, the highest in the group. Nongshim followed with five, while Korea Gas Corporation and Poongsan had four. This gives HMM the strongest combination of aggregate buying and repetition.

## 5. FY2026 operating-profit revisions

| Stock | June 30 | July 30 | One-month change | Interpretation |
|---|---:|---:|---:|---|
| SK Innovation | KRW 4.922T | KRW 5.460T | <strong>+10.9%</strong> | Revision aligns with pension buying |
| LG Electronics | KRW 3.888T | KRW 4.238T | <strong>+9.0%</strong> | Earnings and foreign flow align |
| Samyang Foods | KRW 726.6B | KRW 733.8B | +1.0% | High estimates maintained |
| Celltrion | KRW 1.756T | KRW 1.847T | <strong>+5.2%</strong> | Confirmed earnings improvement |
| NAVER | KRW 2.419T | KRW 2.387T | -1.3% | Flow leads earnings |
| Kia | KRW 10.129T | KRW 10.234T | +1.0% | Value and shareholder return |
| Kakao | KRW 939.8B | KRW 947.4B | +0.8% | Expectations lead |
| HMM | KRW 1.038T | KRW 1.368T | <strong>+31.8%</strong> | Strongest cyclical revision |
| Amorepacific | KRW 460.0B | KRW 465.0B | +1.1% | Global-channel growth |
| LG H&H | KRW 333.6B | KRW 344.4B | +3.2% | Early bottoming |
| Hyundai Glovis | KRW 2.182T | KRW 2.149T | -1.5% | Buying ahead of recovery |
| IBK | KRW 3.703T | KRW 3.686T | -0.5% | Dividend and value |
| Nongshim | KRW 213.3B | KRW 216.8B | +1.6% | Early overseas growth |
| Korea Gas Corp. | KRW 2.265T | KRW 2.265T | 0.0% | Policy and dividend option |
| Pan Ocean | KRW 568.9B | KRW 594.6B | <strong>+4.5%</strong> | Freight recovery |
| Poongsan | KRW 360.6B | KRW 359.5B | -0.3% | Copper and defense expectations |

Consensus values are Naver aggregates stored in the local database. Analyst counts were unavailable, so revision breadth may differ materially by stock.

## 6. Five fundamental groups

### Structural earnings

* Samyang Foods
* Celltrion
* LG Electronics
* Amorepacific

Celltrion reported Q2 revenue of KRW 1.394 trillion and operating profit of KRW 451.8 billion, supported by high-margin new products and cost improvement. [Celltrion](https://www.celltrion.com/ko-kr/company/media-center/press-release/4862)

LG Electronics reported Q2 revenue growth of 14.9% and operating-profit growth of 146.9%, while continuing investment in AI data-center cooling. [LG Electronics](https://www.lge.co.kr/story/newsroom/236115)

Amorepacific's Amazon Prime Day revenue rose 20% in the U.S. and 22% in Europe. [Amorepacific](https://www.apgroup.com/int/en/news/2026-07-03-1.html)

### Rapid cyclical revisions

* HMM
* SK Innovation
* Pan Ocean

HMM is the clearest case. Its FY2026 operating-profit estimate increased 31.8% as SCFI and CCFI rose. The same operating leverage can reverse when freight rates normalize. [Korea Investment & Securities](https://www.truefriend.com/main/research/research/StrategyDetail.jsp?id=157282&jkGubun=6)

### Turnaround accumulation

* LG H&H
* Nongshim
* NAVER

Nongshim offers the clearest near-term earnings path. NAVER offers the largest optionality but also the largest gap between usage metrics and current profit. NAVER said AI Tab daily queries rose sevenfold from beta and queries per user rose 1.7 times. [NAVER](https://www.navercorp.com/media/pressReleasesDetail?seq=10034477)

### Value and shareholder return

* Kia
* IBK
* Korea Gas Corporation

The central variables are valuation, dividends, and policy normalization rather than aggressive revenue growth.

### Expectations ahead of numbers

* Kakao
* Hyundai Glovis
* Poongsan

These stocks require future earnings to catch up with current positioning. Flow can reverse quickly if AI monetization, fuel-cost pass-through, copper, or defense revenue disappoints.

## 7. Two separate rankings

### Best alignment between flow and fundamentals

1. <strong>Celltrion</strong>
2. <strong>Samyang Foods</strong>
3. <strong>LG Electronics</strong>
4. <strong>Amorepacific</strong>
5. <strong>Nongshim</strong>

This is a quality ranking, not an entry-price ranking.

### Best current asymmetry

1. <strong>HMM</strong>: strongest repetition and revision, but cyclical.
2. <strong>Kakao</strong>: large flow with limited price reflection, but profit confirmation is weak.
3. <strong>Korea Gas Corporation</strong>: low-heat accumulation and policy optionality.
4. <strong>Nongshim</strong>: repeated buying with an improving overseas earnings path.
5. <strong>Samyang Foods and Celltrion</strong>: strongest leaders, better bought on pullbacks.

## 8. Key candidates

### HMM

HMM combined positive foreign, program, trust, and pension flow with seven four-way positive sessions. The 31.8% operating-profit revision is the strongest in the screen.

The risk is duration. Freight earnings can peak quickly, and HMM should be treated as a revision trade rather than a permanent compounder.

### Kakao

Kakao attracted KRW 98.0 billion of foreign buying and KRW 125.3 billion of program buying while rising only 3.9% over the period. Its operating-profit revision was only +0.8%, and trust and pension buying were modest.

The position is buying monetization before it appears in earnings. Evidence must emerge through advertising, commerce, subscriptions, or cost efficiency.

### Korea Gas Corporation

All four flows were positive without price overextension. Earnings estimates were unchanged, making this a policy, receivables, and dividend normalization trade rather than an earnings-growth trade.

### Nongshim

Nongshim recorded five four-way positive sessions and balanced monthly buying. Overseas growth and cost control offer a clearer earnings bridge than most turnaround candidates, although the July return already reached 13.5%.

### Samyang Foods and Celltrion

These are the strongest businesses in the screen, but both gained 10.3% over the final five sessions. Pullback behavior and renewed institutional buying matter more than chasing.

## 9. Absorption or trapped buyers?

LG Electronics recorded strong foreign and program buying and a 9.0% earnings revision, yet fell 23.4% from July 1 to July 30. NAVER had strong pension and trust buying while earnings estimates fell 1.3% and the stock lost 11.5% over five sessions.

There are two possible interpretations:

```text
Bull case: institutions absorbed a large seller
Bear case: existing buyers are underwater and may sell into rebounds
```

Cumulative monthly flow cannot distinguish them. A higher low and renewed three-to-five-day foreign and real-money buying are required.

## 10. Execution framework

| Stock | Confirmation | Invalidation |
|---|---|---|
| HMM | Strong SCFI/CCFI and renewed foreign-pension buying | Freight collapse and downward revisions |
| Kakao | Renewed foreign-trust buying and AI revenue metrics | Program flow remains while real money exits |
| Korea Gas Corp. | Receivables decline, tariff and dividend normalization | Policy delays and pension selling |
| Nongshim | Buying persists on a pullback | Overseas slowdown and downward revisions |
| Samyang Foods and Celltrion | Overextension cools and institutions re-accumulate | Post-earnings distribution |

LG Electronics, NAVER, and Kia need trend repair. Amorepacific and LG H&H need to digest strong July gains. Poongsan's positive flow is too small relative to the downtrend to qualify as more than an early watch signal.

## 11. Red Team

### Non-arbitrage days may be basket days, not active selection

KOSPI 200 stocks can be bought mechanically through index and ETF baskets. Foreign and program buying does not prove that an active manager selected the business.

### Trust and pension flow are not always permanent capital

Investment trusts include index and ETF assets, while pensions rebalance and use external managers. This screen uses a narrow real-money definition of trusts plus pensions and excludes insurance and private funds.

### Monthly totals can hide late-month exits

LG Electronics, Kia, NAVER, and SK Innovation suffered substantial late-month drawdowns. Positive monthly flow does not guarantee additional future demand.

### Consensus revisions have different quality

HMM's 31.8% cyclical revision is not directly comparable with Celltrion's 5.2% post-earnings revision. Analyst counts and forecast dispersion were not available.

### July 31 is excluded

The data cutoff is July 30. A large July 31 intraday move does not validate the screen before final investor flows are collected.

## 12. Data coverage

| Data | Provider | Date | Limitation |
|---|---|---|---|
| Foreign, trust, pension flow | Kiwoom local DB | July 30, 2026 | Provider-verified, separate KRX check not available |
| Stock-program flow | Kiwoom REST `ka90013` | July 30 | Total program, not stock-level non-arbitrage |
| Market arbitrage and non-arbitrage | Kiwoom REST `ka90007` | July 30 | Used only as the market gate |
| KOSPI 200 universe | Naver KODEX 200 snapshot | July 30 | ETF-constituent proxy |
| Prices and returns | Naver domestic chart | July 30 | July 1 and July 23 close comparisons |
| FY2026 operating-profit consensus | Naver consensus local DB | June 30 and July 30 | Analyst count unavailable |

## Conclusion

This cross-screen identifies stocks where foreign cash, program, trust, and pension buying overlapped during market-level non-arbitrage inflow days. It is better suited to security selection than a screen that adds futures, but it does not convert program flow into stock-level non-arbitrage evidence.

The 16 names are not equivalent. Celltrion, Samyang Foods, LG Electronics, and Amorepacific are earnings-backed. HMM, SK Innovation, and Pan Ocean are cyclical revision trades. NAVER, Kakao, and Hyundai Glovis are expectations-led. Kia, IBK, and Korea Gas Corporation are value or policy trades.

HMM, Kakao, Korea Gas Corporation, and Nongshim offer the clearest current asymmetry. Celltrion and Samyang Foods offer higher business quality but less comfortable entry points. The main lesson is to separate the best company from the best current price.

This report is market-flow research based on public and local data. It is not a recommendation to buy or sell any security.
