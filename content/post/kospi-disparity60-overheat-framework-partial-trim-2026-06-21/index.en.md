---
title: "KOSPI 60-Day Disparity At +28.6%: Not A Top Call, But A Partial Risk-Reduction Signal"
date: 2026-06-21T02:35:00+09:00
description: "A reproduced KOSPI disparity framework showing why +28.6% above the 60-day moving average is better read as a partial rebalancing signal than an outright market-top call."
categories: ["Exclusive Analysis", "Market-Outlook", "Risk-Management"]
tags: ["KOSPI", "disparity", "market breadth", "risk management", "RSI", "ATR", "Samsung Electronics", "SK Hynix", "narrow market"]
series: ["exclusive-analysis", "korea-market-flow", "risk-management"]
slug: "kospi-disparity60-overheat-framework-partial-trim-2026-06-21"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Context
> This is a follow-up to [How Rare Is It To Beat The Pure KOSPI Benchmark?](/post/kospi-benchmark-hard-to-beat-narrow-market-monte-carlo-2026-06-20/), [ETF Flow Is Leading The Korean Market](/post/korea-etf-flow-led-market-volatility-strategy-2026-06-13/), [Korea Has Liquidity, But Breadth Has Broken](/post/korea-market-liquidity-foreign-reallocation-adr-narrow-leadership-2026-06-03/) and [Have Foreign Investors Returned?](/post/foreign-return-after-24-day-kospi-selling-memory-rebalance-2026-06-12/). Related hubs: [Exclusive Analysis](/page/exclusive-analysis-hub/) and [Korea Daily Market Hub](/page/korea-daily-market-hub/).

## TL;DR

- As of June 19, 2026, KOSPI closed at **9,052**, its 60-day moving average was **7,039**, and its 60-day disparity was **+28.6%**. That is clear medium-term overspeed.
- But disparity overheat is not automatically a market top. Reproducing 355 trading days from January 2, 2025 to June 19, 2026 shows that 20/60/120-day overheat signals were followed by positive average 5-day and 20-day returns. In a strong trend, overheat can first mean acceleration.
- However, when 60-day disparity rises above +20%, the probability of a -5% drawdown within the next 10 trading days rises from a 16% baseline to **63%**.
- That 63% must be handled carefully. The 41 signal days are not 41 independent observations. They compress into **8 episodes**, and only 6 had completed forward windows.
- The current read is therefore: **partial risk reduction is justified, but this is not a top call.** Disparity and volatility gates are on; the 20-day moving-average slope is still rising.

<div class="thesis-callout">
  <div class="thesis-callout__label">Core Point</div>
  <div class="thesis-callout__body">
    KOSPI's +28.6% 60-day disparity does not say <strong>"this is the top"</strong>. It says <strong>the trend has become fast enough that investors should reduce chase risk, harvest part of the risk budget, and prepare for a pullback window</strong>.
  </div>
</div>

## 1. What was tested

The analysis independently reproduced a KOSPI disparity framework. The questions were:

1. Do the current KOSPI disparity numbers tie out?
2. Did disparity overheat historically raise correction probability?
3. Should the current reading be treated as a sell signal?

| Item | Setting |
|---|---|
| Index | KOSPI, `^KS11` |
| Period | 2025-01-02 to 2026-06-19 |
| Sample | 355 trading days |
| Price | Close |
| Disparity | `close / N-day moving average - 1` |
| Windows | 20, 60, 120 days |
| Correction definition | A -5% or worse low within the next 10 trading days |
| Baseline | Same correction frequency across all valid days |

This is a market-risk framework, not a trading instruction.

## 2. Current state: the core numbers tie out

| Metric | Original | Reproduction | Read |
|---|---:|---:|---|
| KOSPI close | 9,052 | **9,052** | Matched |
| MA20 / disparity20 | 8,322 / +8.8% | **8,322 / +8.77%** | Matched |
| MA60 / disparity60 | 7,039 / +28.6% | **7,039 / +28.61%** | Matched |
| MA120 / disparity120 | 6,088 / +48.7% | **6,088 / +48.69%** | Matched |
| MA20 5-day slope | +4.25% | **+4.25%** | Matched |
| RSI(14) | 57 | **SMA 57.3 / Wilder 65.9** | Formula difference |
| ATR(20)% | 3.61% | **Wilder 4.15 / SMA 4.70** | Formula difference |

The key moving-average and disparity numbers tie out almost exactly. The RSI difference is explainable by formula choice: SMA RSI is close to 57, while Wilder RSI is 65.9. Both remain below 70. The conclusion is unchanged: this is not primarily an RSI overbought signal. It is a medium-term disparity signal.

## 3. Overheat did not predict tops well

| Signal | Signal days | Avg +5D return | Avg +20D return | Negative +20D share |
|---|---:|---:|---:|---:|
| Disparity20 ≥ 7% | 74 | +2.68% | +9.07% | 24% |
| Disparity60 ≥ 12% | 120 | +2.26% | +6.88% | 22% |
| Disparity120 ≥ 20% | 107 | +2.55% | +9.11% | 23% |
| Baseline | 335 | +1.86% | +7.83% | 19% |

This is the first uncomfortable point. In this 2025-2026 trend, overheat did not reliably identify the top. Average returns after overheat signals were still positive.

That makes sense in a strong trend. A large distance above moving averages often means money is still being forced into the leaders.

## 4. But 60-day disparity did raise pullback odds

| Condition | Signal days | -5% correction within 10 trading days |
|---|---:|---:|
| Baseline | All valid days | **16%** |
| Disparity60 ≥ 15% | 89 | **36%** |
| Disparity60 ≥ 18% | 54 | **48%** |
| Disparity60 ≥ 20% | 41 | **63%** |
| Disparity60 ≥ 22% | 33 | **67%** |
| Disparity60 ≥ 25% | 26 | **65%** |

The signal is useful, but not as a top-calling tool. It is a pullback-risk warning. Above +20% disparity60, the probability of a -5% drawdown within 10 trading days rose about fourfold versus the baseline.

## 5. The statistical caveat: 41 days are only 8 episodes

The 41 days of +20% disparity are not independent. Grouped into runs, they become 8 episodes:

| # | Episode | Signal days | Peak disparity60 | -5% correction within 10D |
|---:|---|---:|---:|---|
| 1 | 2025-11-03 | 1 | +22.3% | Yes |
| 2 | 2026-01-28 to 01-30 | 3 | +21.6% | Yes |
| 3 | 2026-02-03 to 02-04 | 2 | +22.8% | Yes |
| 4 | 2026-02-12 to 03-03 | 10 | +33.6% | Yes |
| 5 | 2026-05-04 to 05-18 | 10 | +32.1% | Yes |
| 6 | 2026-05-21 to 06-05 | 10 | +36.6% | Yes |
| 7 | 2026-06-09 | 1 | +21.6% | Not complete |
| 8 | 2026-06-15 to 06-18 | 4 | +29.9% | Not complete |

The six completed episodes all produced a -5% correction. That is strong, but the sample is tiny. The right lesson is not to hard-code exact thresholds. The right lesson is to treat extreme 60-day disparity as a risk-budget tightening signal.

## 6. Which indicators mattered?

| Indicator | Pre-correction average | Full-sample average | Difference | Signal quality |
|---|---:|---:|---:|---|
| Disparity60 | +20.35 | +11.33 | +9.02 | Strong |
| ATR%(Wilder) | +2.56 | +2.03 | +0.53 | Medium to strong |
| MA20 slope | +2.74 | +1.81 | +0.93 | Medium |
| Disparity20 | +5.06 | +3.50 | +1.56 | Weak |
| RSI(Wilder) | +64.53 | +65.46 | -0.93 | Little signal |

The ranking is intuitive. A 20-day average follows price quickly, so it gets digested fast. A 60-day average moves more slowly, so extreme 60-day disparity captures medium-term overspeed better. RSI was not the useful axis in this sample.

## 7. The current three-gate read

| Gate | Rule | Current value | Status |
|---|---|---:|---|
| Medium-term overspeed | Disparity60 ≥ 18-20% | **+28.6%** | On |
| Volatility expansion | ATR ≥ 2.2% | **4% range** | On |
| Trend deterioration | MA20 slope slowing or turning down | **+4.25% rising** | Not yet |

Two gates are on. That argues against aggressive chasing.

But the third gate is not on. The 20-day moving-average slope is still rising. Therefore the current signal is not a broad-market exit signal. It is a partial rebalancing signal.

## 8. Use dynamic levels, not fixed index levels

One common mistake is to hard-code an index level. If the 60-day moving average is 7,039 and the re-entry zone is roughly 8% above it, investors may anchor on something like KOSPI 7,600.

But moving averages move. In a strong trend, the 60-day average will keep rising.

```text
Static frame: KOSPI around 7,600
Dynamic frame: the then-current 60-day moving average plus roughly 8%
```

The dynamic frame is better because the pullback zone moves up as the trend matures.

## 9. Why this matters more in a narrow market

The current KOSPI overheat is not a broad-market overheat. It is heavily influenced by Samsung Electronics and SK Hynix.

That links directly to the [pure KOSPI benchmark analysis](/post/kospi-benchmark-hard-to-beat-narrow-market-monte-carlo-2026-06-20/). In 2026, KOSPI has behaved less like the average Korean stock and more like a concentrated AI-memory benchmark.

So the next useful test is not just KOSPI disparity. It is:

| Question | Why it matters |
|---|---|
| Is KOSPI overheated? | Index-level risk budget |
| Is KOSPI ex Samsung/SK Hynix overheated? | Broad-market versus mega-cap effect |
| Are memory mega-caps driving the signal? | Whether the signal is narrow leadership |
| Are second-line stocks also stretched? | Whether this is a broad extension |

## 10. Practical usage

| Situation | Read | Action frame |
|---|---|---|
| Disparity60 12-18% | Strong trend | Hold and verify trend |
| Disparity60 18-20% | Medium-term overspeed | Reduce new chase risk |
| Disparity60 20%+ with high ATR | Pullback probability rising | Reduce part of risk budget |
| Disparity60 20%+ and MA20 slope slows | Distribution risk rising | Consider further reduction |
| Disparity60 cools to 8-12% | Overheat easing | Re-underwrite with flow and earnings |
| Break below the 60-day average | Different regime | Stop using simple pullback-buy rules |

The one-line rule: **60-day disparity overheat is not a short signal. It is a rebalancing signal inside a strong trend.**

## Final view

KOSPI's +28.6% 60-day disparity is real overheat. But the reproduced data does not support treating it as a confirmed top.

Overheat signals were followed by positive average returns in this trend. At the same time, +20% or greater 60-day disparity materially raised the odds of a -5% pullback within 10 trading days.

The right conclusion is balanced:

**This is not the zone to abandon the bull market. It is the zone to stop chasing, harvest part of the risk budget, and wait for either trend deterioration or a cleaner pullback.**

## Coverage Health

- As of: June 19, 2026 close.
- Data: KOSPI `^KS11`, 2025-01-02 to 2026-06-19, 355 trading days.
- Reproduced: 20/60/120-day disparity, RSI 14, ATR 20%, 5-day slope of the 20-day moving average, and -5% forward-10D correction events.
- Confirmed: current disparity values, post-overheat forward returns, disparity60 threshold correction rates, RSI formula difference.
- Not yet confirmed: 2020-2022 cross-validation, KOSPI ex Samsung Electronics/SK Hynix disparity, and robustness of re-entry rules in a true bear-market transition.
- This is a market-risk framework, not investment advice.
