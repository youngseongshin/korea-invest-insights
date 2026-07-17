---
title: "Are Semiconductors Cyclical, and What Is Fair Value? Pricing Samsung, SK Hynix and Micron with FCFE and Normalized Earnings"
slug: "memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17"
date: 2026-07-17T20:00:00+09:00
description: "Samsung at 3.9x and SK Hynix at 4.3x on 2028 consensus means the market doubts the duration of those earnings, not their existence. This post works through whether semis are cyclical, which multiple belongs on which EPS, whether the current debate shakes 2028 EPS or only the multiple, why 2029 is not too distant, and where 2026-2028 cash actually goes, then computes probability-weighted fair values for all three names using FCFE plus a normalized terminal value."
categories: ["Exclusive Analysis", "Valuation", "Tech-Analysis"]
tags:
  - "Samsung Electronics"
  - "SK Hynix"
  - "Micron"
  - "Memory"
  - "HBM"
  - "Valuation"
  - "FCFE"
  - "Cyclical"
  - "Normalized Earnings"
  - "Fair Value"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Context
> This post follows [The Real Debate in Semiconductors](/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/), which concluded that "the industry is a bull but the stock price is a valuation bear," and is the follow-up that quantifies <strong>what fair value actually is</strong>. Where [Samsung and SK Hynix 2028E Profit Valuation](/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/) covered the "numbers that look cheap," this post derives fair value using FCFE and a normalized terminal value. It pairs well with [The Worst Case Is Already the Price](/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/) and [SK Hynix's Q2 Earnings Cut](/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/). Related hubs are the [AI HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/) and the [Exclusive Analysis Hub](/page/exclusive-analysis-hub/).

## TL;DR

* Dividing the July 17 KRX close (Samsung Electronics KRW 255,000, SK Hynix KRW 1,842,000) by the July 16 2028 consensus EPS gives a PER of <strong>3.9x and 4.3x</strong>, respectively. The market is not pricing in the disappearance of 2028 earnings; it is pricing in <strong>the possibility that those earnings will not last</strong>.
* Semiconductors cannot be treated as a single industry. Memory is still cyclical, and HBM is not a product that eliminates the cycle. It is a product that <strong>extends its duration and lowers supply elasticity</strong>.
* On the surface, the current debate shakes the multiple first. But because a falling multiple economically means pre-pricing the normalization of EPS after 2028, the multiple question and the EPS question cannot be fully separated.
* The question of "2028 basis or 2029 basis" is wrong from its premise. A stock price is <strong>the present value of the shareholder cash flow that begins in 2026 and runs in perpetuity</strong>. Applying a low PER to 2028 EPS and applying a normal PER to 2029 normalized EPS give the same answer as long as the assumptions are consistent.
* The probability-weighted fair value computed with FCFE and a normalized terminal value is <strong>KRW 385,000 (+51%) for Samsung Electronics, KRW 1,950,000 (+6%) for SK Hynix, and $1,140 (+34%) for Micron</strong>. Ranked by risk-adjusted attractiveness: Samsung Electronics, Micron, then SK Hynix. \[Inference: own calculation\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Key Framing</div>
  <div class="thesis-callout__body">
    The premise that a stock price should be pinned to either 2028 EPS or 2029 EPS is not accurate to begin with. The correct approach adds 2026-2028 FCFE to a 2029 normalized terminal value, and computed this way, the margin of safety across the three stocks widens in the order Samsung Electronics, Micron, then SK Hynix.
  </div>
</div>

---

## 1. Are Semiconductors Cyclical?

There is no single answer. Cycle intensity differs by segment.

| Segment | Cycle Character | Reason |
|---|---|---|
| Commodity DRAM/NAND | Very strong | Product homogeneity, inventory, and swings in capacity expansion and ASP |
| HBM | Moderate to strong | Qualification, stacking and LTAs are entry barriers, but high margins invite expansion and multi-sourcing |
| Foundry/equipment | Moderate to strong | Customer CAPEX and process-transition cycles |
| Fabless/platforms | Wide variance by product | Moats exist but exposure to generational shifts and customer CAPEX remains |

The most accurate description is <strong>"an industry that grows structurally, but whose prices and profits are cyclical."</strong>

Exposure differs by stock. SK Hynix has the purest exposure to memory and HBM. Samsung Electronics has high earnings sensitivity during memory upcycles, but mobile, display, foundry and its cash position cushion part of the downside.

### What the Companies Themselves Say

This judgment rests not on an observer's interpretation but on <strong>the companies' own official filings</strong>. \[Fact: SEC filings\]

SK Hynix defined the memory industry as <strong>highly cyclical</strong> in its US F-1. Micron stated in its 10-Q that while HBM requires more wafers and cleanroom capacity than commodity DRAM to produce the same number of bits, <strong>if HBM demand weakens and that capacity reverts to commodity DRAM, DRAM supply could surge</strong>.

Put those two statements together and the conclusion follows. HBM only delays the supply response; it does not remove the cycle. \[Inference: synthesis of both filings\]

---

## 2. What Is the Right Multiple?

Discussing the right PER requires first deciding <strong>which EPS it applies to</strong>. The same 8x is expensive when applied to peak earnings and reasonable when applied to normalized earnings.

| Earnings Base | Samsung Electronics | SK Hynix | Interpretation |
|---|---:|---:|---|
| 2027-2028 peak EPS | 5.5-7.5x | 5-7x | Discounts subsequent earnings normalization |
| Normalized EPS | 8-10x | 7-9x | Applied to 3-5 year average earnings |
| Confirmed structural plateau | 9-11x | 8-10x | Allowed only if earnings hold up past 2029 |

For Samsung Electronics, a multiple above 9x requires confirmation of both an HBM share recovery and a narrower foundry loss. For SK Hynix, 8-10x requires HBM4E share, LTA repricing, shareholder returns, and margin defense after supply expands.

So <strong>applying 9-12x directly to the 2028 consensus is a strongly bullish scenario that combines peak earnings with a structural multiple at the same time</strong>. For a cyclical company, the PER is lowest at the peak and highest, or simply not computable, in a downturn. Continuing value should be calculated on normalized earnings, not on the peak or the trough. \[Fact: McKinsey cyclical valuation methodology\]

---

## 3. Does the Current Debate Shake EPS, or Only the Multiple?

Broken out debate by debate, the answer diverges.

| Debate | Immediate Impact | Condition That Would Also Damage EPS |
|---|---|---|
| Single-stock leverage unwind | Multiple, supply-demand flow | None; it is a technical factor |
| Rate/AI-debt/ROI concerns | Multiple first | Two or more big tech names cut CAPEX |
| Buyer price resistance | Multiple plus EPS risk | Contract price declines and order cuts happen together |
| Capacity expansion by the three memory makers | 2028 EPS and multiple | Actual qualified output and bit supply rise |
| CXMT/YMTC | Long-term multiple first | Global qualification, mass shipment and price pressure |
| HBM LTA/packaging bottleneck | EPS/multiple defense | Price floors and contract volumes hold |

### The Analyst Numbers Have Not Moved Yet

On local WiseReport data, Samsung Electronics' 2028 EPS was unchanged at KRW 65,907 on both July 13 and July 16. SK Hynix was cut <strong>1.5%</strong>, from KRW 433,625 to KRW 427,332. \[Fact: WiseReport consensus\]

In other words, the analyst numbers barely moved, and <strong>the stock price moved first</strong>.

### But It Isn't Only the Multiple That Came Down

Back-solving from a normalized PER of 8x gives the EPS the market is actually allowing.

| Stock | EPS Implied by 8x | 2028 Consensus | Gap |
|---|---:|---:|---:|
| Samsung Electronics | KRW 31,875 | KRW 65,907 | -52% |
| SK Hynix | KRW 230,250 | KRW 427,332 | -46% |

The market is pricing in a blend of two cases.

1. 2028 EPS lands close to consensus but falls quickly starting in 2029.
2. 2028 EPS itself comes down because of expanding supply and buyer price resistance.

The data confirmed so far leans <strong>closer to case 1</strong>. CAPEX cancellations, falling contract prices, rising inventory and LTA renegotiation have not yet been confirmed together. That said, capacity expansion and buyer resistance are real variables that could tip the picture toward case 2. \[Inference: data interpretation\]

The current correction is not yet an earnings-downgrade market; it is <strong>a repricing of earnings duration</strong>. But the underlying object of the anxiety the market is expressing through the multiple is post-2028 EPS, and if contract prices, inventory and CAPEX deteriorate, it converts into a 2028 EPS-downgrade market.

---

## 4. Is the Basis 2028, or 2029?

The premise of this question is not accurate to begin with. A stock price is not set by either one. It is <strong>the present value of the shareholder cash flow that begins in 2026 and runs in perpetuity</strong>.

```text
Present value
= present value of 2026-2028 FCFE
+ present value of the terminal value at year-end 2028

Terminal value at year-end 2028 ≈ 2029 normalized EPS × normalized PER
```

Using 2028 EPS does not mean ignoring 2029 and beyond. It is a way of <strong>compressing the post-2029 downside risk into the low PER attached to 2028 EPS</strong>. Using 2029 normalized EPS directly instead allows a more normal PER to be applied. As long as the assumptions are consistent, the two methods should arrive at similar answers.

The two are often just saying the same thing in different words, yet debate frequently breaks out over which one is correct.

---

## 5. Is 2029 Too Distant a Future?

Three years is not distant in equity valuation. At a required return of 11%, one won in 2029 is worth about 0.73 won today.

```text
1 / (1.11)^3 = 0.731
```

Even if an investor sells the stock a year from now, <strong>the buyer at that point is looking at cash flow from 2029 onward</strong>. Because the eventual sale price is itself determined by future cash flow, a short holding period cannot escape long-term earnings. Damodaran's FCFE model likewise values equity as the sum of FCFE over an explicit forecast horizon plus the terminal value that follows it. \[Fact: NYU Stern FCFE model\]

---

## 6. Is 2026-2028 Cash Not Being Considered?

It is considered. But <strong>EPS and the cash that actually returns to shareholders are different things</strong>.

Summing the July 16 WiseReport consensus gives the following. \[Fact: consensus aggregate\]

| Stock | 2026E EPS | 2027E EPS | 2028E EPS | 3-Year Cumulative EPS | Vs. Current Price |
|---|---:|---:|---:|---:|---:|
| Samsung Electronics | KRW 46,664 | KRW 65,802 | KRW 65,907 | KRW 178,373 | 70% |
| SK Hynix | KRW 314,787 | KRW 438,114 | KRW 427,332 | KRW 1,180,233 | 64% |

If the consensus is realized, three-year cumulative earnings equal 64-70% of the current price, a scale too large to dismiss.

The problem is that accounting profit is not, as-is, cash to shareholders.

```text
FCFE = Net income - Net CAPEX - Increase in working capital + Net borrowing
```

Memory companies sharply increase fab, EUV and packaging investment during upcycles. If 60 out of 100 in net income goes into capacity expansion, only 40 accrues as immediate cash. The other 60 does not disappear either, but <strong>it only becomes value if the new capacity earns a return above the cost of capital</strong>.

2026-2028 earnings feed into the stock price through dividends and buybacks, rising net cash, falling debt, rising book value, and high-return capacity expansion. Conversely, if oversupply arrives right after capacity expands, that cash converts into equipment and even lowers future ROE. This is why the market does not value one won of upcycle net income at one won.

### The Two Paths the Current Price Reflects

On the 2028 consensus, the current price sits at 3.9x for Samsung Electronics and 4.3x for SK Hynix. The market is pricing in a blend of the following.

1. A substantial share of 2026-2028 earnings is reinvested into capacity expansion.
2. ASP and margin normalize starting in 2029.

So the variable that matters is not "does 2029 EPS shrink," but <strong>how much it shrinks by</strong> and <strong>what share of 2026-2028 earnings actually remains as FCFE or net cash</strong>.

| 2029 Path | Valuation Approach |
|---|---|
| EPS -10% to -20%, then stabilizes | Explicit FCFE plus normalized PER of 8-10x |
| EPS -30% to -50%, then recovers | Explicit FCFE plus normalized EPS multiple of 7-9x |
| EPS -50% or worse, oversupply persists | Normalized PBR, net cash and curtailment value rather than PER |

McKinsey likewise holds that for cyclical companies, the normal-cycle and structural-change scenarios should be probability-weighted, and the terminal value should be calculated on normalized cash flow rather than the peak or the trough. \[Fact: McKinsey methodology\]

---

## 7. What Is Fair Value, Calculated Rigorously?

The framework above was run through actual numbers. The probability-weighted fair value as of July 17, 2026 is as follows. \[Inference: own calculation, assumptions stated below\]

### Calculation Method

```text
Fair value = Remaining 2026 FCF + 2027 FCF + 2028 FCF + terminal value at year-end 2028
Terminal value = 2029 normalized EPS × fair PER
```

- <strong>Discount rate</strong>: 10.5% for Samsung Electronics, 11.5% for SK Hynix, 10.5% for Micron
- <strong>Probability</strong>: 30% excess demand, 40% order vacuum/re-concentration, 20% supply normalization, 10% credit short-circuit
- <strong>Terminal PER</strong>: 7.5-8.5x for Samsung Electronics, 6-9x for SK Hynix, 7-9.5x for Micron
- <strong>Downcycle treatment</strong>: 45-90% of the earnings decline is reflected in FCF, applying both fixed CAPEX and the possibility of cuts

### Results

| Stock | Current Price | Probability-Weighted Fair Value | Upside | Sensitivity Range |
|---|---:|---:|---:|---:|
| Samsung Electronics | KRW 255,000 | <strong>KRW 385,000</strong> | +51% | KRW 316,000-461,000 |
| SK Hynix | KRW 1,842,000 | <strong>KRW 1,950,000</strong> | +6% | KRW 1,480,000-2,480,000 |
| Micron | $853.20 | <strong>$1,140</strong> | +34% | $905-1,410 |

The sensitivity range is the result of simultaneously shifting the excess-demand and supply-normalization probabilities by 10 percentage points, the discount rate by ±1.5 percentage points, and the terminal PER by ±1x.

### Present Value by Scenario

| Scenario | Probability | Samsung Electronics | SK Hynix | Micron |
|---|---:|---:|---:|---:|
| Excess demand persists | 30% | KRW 548,000 | KRW 3,415,000 | $1,735 |
| Order vacuum, re-concentration | 40% | KRW 347,000 | KRW 1,581,000 | $1,086 |
| Supply/efficiency normalization | 20% | KRW 283,000 | KRW 1,064,000 | $674 |
| Systemic credit short-circuit | 10% | KRW 241,000 | KRW 732,000 | $505 |

This table reveals the difference in character across the three stocks. <strong>Samsung Electronics stays above the current price even in the supply-normalization scenario (KRW 283,000).</strong> SK Hynix, by contrast, <strong>already falls below the current price starting from the second scenario (KRW 1,581,000)</strong>. That means SK Hynix's current expected return depends most heavily on excess demand persisting.

---

## 8. The Difference FCF Makes

Even if 2029 earnings slow, the cash generated over the preceding three years does not disappear. The size of that cushion differs by stock.

| Stock | 2026F FCF | 2027F FCF | 2028F FCF | 3-Year FCF Share of Probability-Weighted Value |
|---|---:|---:|---:|---:|
| Samsung Electronics | KRW 158.2tn | KRW 385.0tn | KRW 412.7tn | <strong>26%</strong> |
| SK Hynix | KRW 74.7tn | KRW 177.4tn | KRW 172.0tn | 17% |
| Micron | $50.6B | $124.3B | $145.9B | 18% |

\[Fact: Samsung Securities report (Samsung), Korea Investment & Securities report (SK Hynix), FactSet estimates (Micron)\]

<strong>For Samsung Electronics, 26% of probability-weighted value comes from 2026-2028 FCF.</strong> In other words, even if the post-2029 scenario deteriorates, it has the largest share of cash already secured. SK Hynix is lowest at 17%, meaning most of its value depends on the post-2029 terminal value.

---

## 9. Final Ranking

<strong>1st, Samsung Electronics</strong>: The largest margin of safety. The current price sits close to the hard-bear scenario value. Net cash and business diversification cushion the downside of the terminal value, and the 26% three-year FCF share adds further cushion.

<strong>2nd, Micron</strong>: Attractive on the central fair-value estimate, but sensitive to new 2028 supply. It is also worth noting that Morningstar's fair value, an external bear anchor, is $850, close to the current price. \[Fact: Morningstar\]

<strong>3rd, SK Hynix</strong>: The strongest business momentum, but the thinnest price margin of safety. A fresh call requires confirming HBM4E pricing, yield and the 2028 LTA.

At current prices, then, <strong>risk-adjusted attractiveness ranks Samsung Electronics, Micron, then SK Hynix</strong>. The key finding of this calculation is that the ranking by business quality (SK Hynix is strongest given its pure HBM exposure) runs opposite to the ranking by price attractiveness. \[Inference: overall judgment\]

---

## 10. Summary: How to Value Each Stock

- <strong>Samsung Electronics</strong>: Add 2026-2028 FCFE separately, then discount a 2029 normalized EPS with 8-10x applied. Net cash and business diversification cushion the downside of the terminal value.
- <strong>SK Hynix</strong>: Add 2026-2028 FCFE while reflecting capacity expansion and dilution, then apply 7-9x to 2029 normalized EPS. The upper end is allowed only once an HBM plateau is confirmed.

Valuing the 2028 consensus at a flat 4x is incomplete, and so is mechanically applying 9-12x. The correct approach is <strong>adding 2026-2028 FCFE to a 2029 normalized terminal value and summing across scenarios</strong>.

---

## Closing

Summarizing the answers to each question, line by line.

Are semiconductors cyclical? Memory is. HBM has not eliminated the cycle, only extended it, and SK Hynix's F-1 and Micron's 10-Q say so themselves.

What is the right multiple? Which EPS it is applied to must be decided first. 5-7x at peak, 7-10x normalized.

What does the current debate shake? On the surface, the multiple, but what that multiple expresses is post-2028 EPS. The analyst numbers have moved only about 1.5% so far, and the stock price moved first.

2028 or 2029? Neither. Add 2026-2028 FCFE to a 2029 normalized terminal value.

Is 2029 a distant future? One won three years out is 0.73 won today. Even if you sell a year from now, the buyer at that point is looking at 2029.

Is 2026-2028 cash reflected? It is, but not as EPS as-is. What goes out to capacity expansion has to be subtracted, and that capacity only becomes value if it earns above the cost of capital.

So what is it worth? KRW 385,000 for Samsung Electronics, KRW 1,950,000 for SK Hynix, $1,140 for Micron. The stock with the strongest business momentum and the stock with the largest price margin of safety are not the same one.

---

_This post is independently calculated analysis based on KIS KRX quotes (2026-07-17), WiseReport consensus (2026-07-16), SEC filings (SK Hynix F-1, Micron 10-Q), broker FCF estimates, and the publicly available valuation methodologies of McKinsey and NYU Stern. The probability-weighted fair values, scenario probabilities, terminal PERs and discount rates are all estimates based on assumptions made at the time of writing, not company guidance or consensus. Analyst estimate revisions following the July 17 sell-off are not yet reflected. Cumulative EPS is a sum of accounting profit, not an FCFE estimate. The stocks mentioned are examples used to illustrate the valuation methodology, not a recommendation to buy or sell any specific stock. Investment decisions and their outcomes are the sole responsibility of the investor._

---

### Related Posts

- [The Real Debate in Semiconductors: Four Physical Clocks and One Stock-Price Clock](/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [Samsung and SK Hynix 2028E Profit Valuation: Cheap-Looking Numbers and Cycle Tests](/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/)
- [Are Samsung Electronics and SK Hynix Really Oversold Versus the 2027 Consensus?](/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/)
- [SK Hynix Q2 Earnings Cut but Target Prices Held](/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/)
- [Why IBM's Earnings Miss Is Evidence of Memory Strength](/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/)
