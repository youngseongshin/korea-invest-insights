---
title: "Can Microsoft Earnings Break the OpenAI-Centered AI CapEx Circularity?"
slug: "microsoft-openai-ai-capex-circularity-earnings-scenarios-2026-07-29"
date: 2026-07-29T01:10:00+09:00
description: "A deep analysis of the OpenAI-centered AI CapEx loop linking equity funding, Azure purchase commitments, Microsoft infrastructure spending, and semiconductor orders. The report explains what Microsoft's FY26 Q4 earnings can and cannot prove about OpenAI revenue growth and loss reduction, corrects the HLBV accounting misconception, and sets bold forecasts for Azure, AI revenue, RPO, OpenAI cash burn, and FY27 CapEx."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags:
  - "Microsoft"
  - "OpenAI"
  - "AI CAPEX"
  - "circular financing"
  - "Azure"
  - "RPO"
  - "HLBV"
  - "Nvidia"
  - "hyperscalers"
  - "memory semiconductors"
  - "Samsung Electronics"
  - "SK hynix"
valley_cashtags: ["Samsung Electronics", "SK hynix"]
draft: false
---

> Context: [The Nvidia-OpenAI backstop analysis](/en/post/nvidia-openai-250bn-backstop-anatomy-two-lenses-2026-07-29/) examined how guarantees and chip financing could support AI demand with credit. [Rebound or terminal point](/en/post/ai-capex-eight-doubts-rebound-or-terminal-48hours-2026-07-29/) identified Microsoft's OpenAI investment line as a critical market signal. This article corrects and expands that argument. The earnings report can reduce pressure on the circularity thesis, but it cannot audit OpenAI's operating loss through a single Microsoft accounting line.

## TL;DR

- The OpenAI-centered AI CapEx cycle is not one circle. It consists of four overlapping layers: **cash from genuine customers, cloud purchase commitments, equity and debt funding, and vendor financing**. It is wrong to call all subscription and API revenue circular. It is equally wrong to ignore OpenAI's $250 billion Azure commitment and its concentration in Microsoft's backlog.
- A major accounting correction is required. After OpenAI's recapitalization, Microsoft does not simply apply its roughly 27% ownership. It uses the **hypothetical liquidation at book value, or HLBV, method** because liquidation rights and priorities differ from ownership. Dividing Microsoft's reported OpenAI gain or loss by 27% no longer yields OpenAI operating loss.
- Official numbers show the discontinuity. Microsoft FY26 Q1 included a roughly $4.1 billion pre-tax OpenAI investment loss, which the CFO said entirely reflected Microsoft's share of OpenAI losses under the old setup. FY26 Q2 then produced a $7.583 billion positive net income impact after recapitalization. FY26 Q3 showed only a $19 million pre-tax loss and a $14 million net income impact. This does not mean OpenAI became profitable. The accounting measurement changed.
- The upcoming call can therefore test the **quality of external demand and cash collection**, not OpenAI net loss directly. Key metrics are Azure growth, Microsoft's AI annual revenue run rate, RPO excluding OpenAI, near-term conversion of OpenAI commitments, Microsoft Cloud gross margin, and operating cash flow.
- My bold base forecast is **41% constant-currency Azure growth**, a **$45-48 billion Microsoft AI revenue run rate**, **$670-690 billion commercial RPO**, and a **$225-240 billion FY27 CapEx and finance-lease investment pace**. I expect the reported OpenAI investment line to center near a **$0.2 billion pre-tax loss**, but assign it low information value.
- Based on reported data and usage momentum, I estimate OpenAI Q2 2026 revenue at **$7.5-8.5 billion**, cash burn at **$2.5-3.5 billion**, and June exit annualized revenue at **$32-36 billion**. Revenue is growing rapidly, but there is not enough evidence to declare that absolute losses have decisively fallen. The first gate is whether cash burn as a percentage of revenue falls from roughly 65% in Q1 to 35-45%.
- The strongest outcome combines Azure above 41%, RPO excluding OpenAI growing above 25%, AI revenue run rate above $47 billion, Cloud gross margin at or above 64%, and FY27 CapEx growth falling below AI revenue growth. That would weaken the loop's dependence on new financing. It would not resolve system-wide circularity involving guarantees, supplier receivables, and long-dated commitments. Those require Nvidia disclosures and several quarters of cash-flow evidence.

## 1. Define the circularity before judging it

The market's concern can be drawn simply:

```text
Microsoft, SoftBank, and other investors
             ↓ equity, loans, guarantees
           OpenAI
             ↓ Azure commitments, data center leases, GPU orders
Microsoft, Oracle, cloud and data center operators
             ↓ CapEx and equipment orders
Nvidia, memory, networking, and power suppliers
             ↓ investment, financing, guarantees, supply commitments
           OpenAI ecosystem
```

This looks like money moving in a circle. Economically, however, four different layers must be separated.

| Layer | Source of funds | Economic character | Current evidence |
|---|---|---|---|
| 1. External customer cash | ChatGPT subscriptions, APIs, enterprise contracts | Genuine end demand | OpenAI says enterprise now represents more than 40% of revenue |
| 2. Commercial commitments | OpenAI's Azure and cloud purchase contracts | Future service obligations | About 45% of Microsoft's $625 billion FY26 Q2 commercial RPO came from OpenAI |
| 3. Capital funding | Equity, loans, SPVs | Funding losses and infrastructure commitments | OpenAI announced a $122 billion 2026 funding round |
| 4. Vendor financing | Chip finance, lease guarantees, advances | Suppliers supporting customer purchasing power | Reported Nvidia guarantees and financing remain unconfirmed by signed public contracts |

Layer one is not circular. It is money paid by consumers and enterprises for services. Circularity concerns begin in layer two. Microsoft invested in OpenAI; OpenAI committed to buy a very large amount of Azure; Microsoft recognizes that commitment in RPO and builds data centers; the data centers buy semiconductors; and some suppliers may help finance OpenAI.

The right questions are therefore:

1. How quickly does external customer cash catch up with OpenAI's compute cost and long-term purchase commitments?
2. Can equity, debt, and guarantees fund the gap until that happens?

The loop ends when **external customer cash flow replaces capital-market funding**, not when revenue merely appears.

## 2. Three different payments link Microsoft and OpenAI

Microsoft and OpenAI are not merely investor and investee.

Microsoft owns roughly 27% of OpenAI on an as-converted basis. It is a major cloud supplier to OpenAI. It also uses OpenAI technology in its products, while OpenAI pays Microsoft a share of revenue.

The April 2026 amended agreement makes the relationship more complex. According to [OpenAI's official announcement](https://openai.com/index/next-phase-of-microsoft-partnership/), Microsoft remains the primary cloud partner and OpenAI products generally ship first on Azure. OpenAI can also serve all products through other clouds. Microsoft's IP license lasts through 2032 but is now non-exclusive. Microsoft no longer pays revenue share to OpenAI, while **OpenAI's revenue-share payments to Microsoft continue through 2030** at the same rate, subject to an aggregate cap.

Microsoft simultaneously acts as:

- a shareholder benefiting from OpenAI's valuation;
- a cloud supplier receiving Azure payments;
- an IP licensee selling Copilot and Azure AI products;
- a revenue-share recipient benefiting from OpenAI's external sales.

This creates multiple monetization points when OpenAI grows. It also creates correlated risk. If OpenAI cannot fund its commitments, Microsoft's Azure backlog, data center utilization, and AI product positioning can all be affected.

## 3. Accounting correction: the equity-method line is no longer an OpenAI loss calculator

This is the most important correction in the report.

[Microsoft's March 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/msft-20260331.htm) states that Microsoft applies HLBV to its OpenAI equity-method investment. HLBV estimates how much Microsoft would receive if the investee's net assets were liquidated at book value. It is used because liquidation rights and priorities do not match the underlying ownership percentage.

Microsoft therefore does not recognize 27% of every quarterly operating loss. New capital, preferred rights, loss-allocation priorities, recapitalization, and dilution all affect Microsoft's hypothetical liquidation value.

The last three quarters demonstrate this:

| Microsoft fiscal quarter | OpenAI-related Microsoft result | Correct interpretation |
|---|---:|---|
| FY26 Q1 | About -$4.1B pre-tax; -$3.1B net income impact | Pre-recapitalization. CFO said the entire loss represented Microsoft's share of OpenAI losses |
| FY26 Q2 | +$7.583B net income impact | Accounting gain from recapitalization, dilution, and changes in net assets |
| FY26 Q3 | -$19M pre-tax; -$14M net income impact | Small HLBV change, not a claim that OpenAI operating loss was $19M |

Sources are Microsoft's [FY26 Q1 call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1), [FY26 Q2 release](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q2/press-release-webcast), and [FY26 Q3 release](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast).

The following calculation must be discarded:

```text
Microsoft OpenAI investment loss ÷ 27%
= OpenAI quarterly operating loss
```

It was a rough approximation in FY26 Q1 before the recapitalization. It is no longer valid. Whether Microsoft reports a $0.2 billion OpenAI loss or a $1 billion gain in FY26 Q4, that line alone cannot prove an improvement in OpenAI gross margin or cash burn.

This does not weaken the circularity concern. It means the **observable window has become less transparent**. Investors must examine contract conversion, cash collection, and additional management disclosures.

## 4. What the earnings call can and cannot resolve

Microsoft will report FY26 Q4 results after the US market close on July 29 and hold its call at 2:30 p.m. Pacific time, or 6:30 a.m. KST on July 30, according to the [official schedule](https://news.microsoft.com/source/2026/07/08/microsoft-announces-quarterly-earnings-release-date-68/).

Breaking the concern into three claims clarifies the event's reach.

| Concern | Can this call resolve it? | Evidence required |
|---|---|---|
| OpenAI cannot pay its commitments | Partly | External revenue growth, rising revenue share, conversion of commitments into Azure revenue |
| OpenAI revenue is merely recycled investor capital | Largely | Enterprise, consumer, and API usage plus cash collection and Azure growth excluding OpenAI |
| The entire AI ecosystem is inflated by reciprocal investment and guarantees | No | Supplier receivables, guarantees, SPVs, and multi-quarter cash flow |

The call cannot settle system-level circularity. Strong Microsoft numbers will not audit Nvidia guarantee risk, Oracle and neocloud credit, or vendor financing.

It can reduce the first two concerns through this path:

```text
OpenAI external customer revenue growth
  → higher revenue-share payments to Microsoft
  → higher cash collection on Azure bills
  → lower need for new OpenAI financing
  → lower credit risk in Microsoft RPO
  → shorter payback period on data center CapEx
  → lower discount applied to semiconductor order durability
```

## 5. The prior-quarter scoreboard

Microsoft FY26 Q3 provides the baseline.

| Metric | FY26 Q3 result | Question for Q4 |
|---|---:|---|
| Microsoft revenue | $82.9B, +18% | Does AI lift total growth further? |
| Microsoft AI annual revenue run rate | Above $37B, +123% | Does it exceed $45B? |
| Azure growth | +39% constant currency | Does it beat 39-40% guidance and reach 41%? |
| Microsoft Cloud gross margin | 66% | Can it hold at least the 64% Q4 guide? |
| Commercial RPO | $627B, +99% | Does ex-OpenAI growth and near-term conversion remain strong? |
| RPO growth excluding OpenAI | +26% | Does it remain above 25%? |
| CapEx | $31.9B | Q4 above $40B and the FY27 investment pace |
| Operating cash flow | $46.7B, +26% | Is collection growing faster than CapEx? |
| Free cash flow | $15.8B | Can Microsoft self-fund another investment step-up? |

RPO quality matters most. In FY26 Q2, Microsoft said OpenAI represented about 45% of $625 billion commercial RPO, or roughly $281 billion. The remaining $350 billion grew 28% across a broad customer base. In Q3, total RPO reached $627 billion and RPO excluding OpenAI grew 26%. The gap between 99% total growth and 26% ex-OpenAI growth is where circularity concerns attach.

Total RPO above $700 billion would not be enough. Three conditions should appear together:

1. RPO excluding OpenAI grows at least 25%.
2. RPO scheduled for recognition in the next 12 months grows at least 35%.
3. Cloud gross margin holds at or above 64%.

Together, they would show that long-dated commitments are turning into actual service consumption and cash.

## 6. How far can OpenAI financials be estimated?

OpenAI is private and does not publish quarterly statements. The figures below combine reported financial data with official business indicators.

[OpenAI's 2026 funding announcement](https://openai.com/index/accelerating-the-next-phase-ai/) says enterprise customers represent more than 40% of revenue and are on track to reach parity with consumer revenue by year-end. That is evidence that revenue is not solely dependent on individual subscriptions.

Cash burn remains substantial. External reporting indicates roughly $5.7 billion Q1 2026 revenue and approximately $3.7 billion cash burn. A reported net loss above $20 billion included large non-cash valuation effects, so cash burn is more useful for operating analysis. Annualized revenue reportedly exceeded $25 billion at the end of February.

My Q2 estimates are:

| OpenAI metric | Reported Q1 2026 | Q2 2026 estimate | Interpretation |
|---|---:|---:|---|
| Quarterly revenue | About $5.7B | **$7.5-8.5B** | Sequential growth of 32-49% |
| Quarterly cash burn | About $3.7B | **$2.5-3.5B** | Potential first decline, with high uncertainty |
| Cash burn as % of revenue | About 65% | **35-45%** | The most important unit-economics gate |
| Quarter-end annualized revenue | About $25B | **$32-36B** | Measures how fast external demand reduces funding dependence |

Even if correct, these numbers would not mean OpenAI is near profitability. A company aggressively increasing model training, inference, data center reservations, and talent can improve gross economics while maintaining high absolute cash burn.

But $8 billion revenue and $3 billion cash burn would matter. External annualized revenue would move into the mid-$30 billions while the cash-burn ratio falls below half of revenue. That would be the first sign that the capital-market hole is growing more slowly than revenue.

## 7. Bold forecasts before the release

These are judgment estimates, not consensus. The goal is to fix the scoring framework before the results.

| Metric | Bold estimate | Rationale |
|---|---:|---|
| FY26 Q4 Azure growth | **+41% constant currency** | Above 39-40% guidance due to capacity delivery and usage growth |
| Microsoft AI annual revenue run rate | **$45-48B** | Up from $37B with consumption, seats, and APIs all growing |
| Commercial RPO | **$670-690B** | Above $700B is the bull scenario |
| RPO growth excluding OpenAI | **+25-28%** | More important than total RPO |
| Microsoft Cloud gross margin | **64.0-64.5%** | Efficiency offsets higher AI usage |
| Q4 CapEx | **$43-46B** | Above the company's $40B guide, including component inflation |
| FY27 CapEx and finance-lease investment pace | **$225-240B** | Around $50B quarterly cash CapEx plus lease variability |
| FY27 Q1 Azure guide | **+41-43% constant currency** | Quantifies management's second-half acceleration outlook |
| OpenAI investment pre-tax result | **-$0.5B to +$1.0B**, centered near -$0.2B | Driven by HLBV, capital, and preference rights; low information value |
| OpenAI Q2 revenue | **$7.5-8.5B** | Path to $32-36B annualized revenue |
| OpenAI Q2 cash burn | **$2.5-3.5B** | Potential first meaningful decline |

The boldest forecast is not a single number. It is that **Microsoft AI revenue growth will decisively exceed AI-related CapEx growth in FY27 for the first time**.

Microsoft guided to roughly $190 billion calendar 2026 CapEx, including about $25 billion of component-price inflation. A $230 billion FY27 investment pace implies roughly 21% growth. If AI annualized revenue exits Q4 above $47 billion and grows more than 60% next year, the gap between monetization and investment growth opens materially.

That crossover is the key to reducing circularity risk. When investment grows faster than customer revenue, external funding remains essential. When revenue grows faster than investment, financing shifts from a prerequisite for growth to an option.

## 8. Four scenarios

| Scenario | Probability | Evidence | Interpretation |
|---|---:|---|---|
| S1. External cash wins | 35% | Azure 41%+, AI run rate $47B+, ex-OpenAI RPO 25%+, Cloud GM 64%+ | Concern shifts from funding to monetization; credit and semiconductors rally together |
| S2. Microsoft strong, OpenAI opaque | 40% | Azure 39-41%, total RPO up, no useful OpenAI cash disclosure | Most likely. Microsoft thesis holds, OpenAI credit concern moves to October |
| S3. CapEx again outruns monetization | 15% | Azure below 39%, Cloud GM below 63%, FY27 investment pace above $250B | Monetization gap widens; hyperscaler FCF risk rises before semiconductor demand risk |
| S4. Structural disclosure | 10% | New disclosure on revenue share, Azure collections, contract reserves, or credit support | Large volatility regardless of direction; highest information value |

Even S1 would not mean circularity disappeared. The accurate conclusion would be:

> OpenAI external revenue and Microsoft's AI cash generation have begun to grow faster than infrastructure investment, reducing dependence on new financing at the weakest point of the loop.

S2 is not failure. Because HLBV makes the investment line an incomplete window, strong Azure and broad customer demand may coexist with little quantitative OpenAI disclosure.

## 9. Equity and credit transmission

The exact reaction will depend on the same-day FOMC and positioning. These ranges are event-analysis judgments.

| Asset | S1 reaction | S3 reaction | Transmission |
|---|---:|---:|---|
| Microsoft | +6-10% | -7-12% | CapEx payback and Cloud margin |
| Nvidia | +5-9% | -4-8% | OpenAI credit risk and GPU order durability |
| Oracle and AI infrastructure credit | Equity +7-12%, CDS -10 to -25bp | Equity -8-15%, CDS +20 to +40bp | OpenAI counterparty risk |
| SOXX | +4-7% | -3-6% | Repricing of 2027-2028 demand duration |
| Samsung Electronics | Next Korea session +4-7% | -3-5% | Duration of general DRAM and HBM demand |
| SK hynix | Next Korea session +5-9% | -4-7% | HBM order durability and premium-memory mix |

There are three semiconductor channels.

First, faster OpenAI revenue reduces the concern that every incremental AI workload creates a larger loss. Inference usage can then justify GPU, HBM, server DRAM, and enterprise SSD purchases economically.

Second, if Microsoft maintains a FY27 investment pace above $200 billion while AI revenue grows faster, the discount applied to post-2028 semiconductor earnings can fall. The market begins to evaluate AI revenue per CapEx dollar, not only absolute CapEx.

Third, strong AI revenue paired with Cloud gross margin below 63% would be mixed. Chip demand would remain high, but weak customer economics could pressure future component pricing. Memory would receive a volume benefit and a pricing risk simultaneously.

## 10. The same morning as the FOMC

The [Federal Reserve calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) shows a July 28-29 meeting. The decision arrives early on July 30 KST, followed a few hours later by Microsoft.

| FOMC | Microsoft S1 | Microsoft S3 |
|---|---|---|
| Hold with an easier message | Growth and discount rate improve together; strongest risk-on combination | Rates cushion the shock, but monetization concern remains |
| Hold with a hawkish message | Earnings can rally, but long-duration valuation upside is capped | Rates and monetization pressure together; weakest combination |

The same Microsoft numbers can generate different price reactions under different rates. Microsoft's after-hours move should therefore be interpreted alongside the FOMC, the dollar, and long-term yields before projecting the Korean semiconductor response.

## 11. Questions management must answer

1. What are commercial bookings and RPO growth excluding OpenAI?
2. How much OpenAI-related RPO will convert to revenue within 12 months?
3. Are there reserves, renegotiations, or additional credit support attached to OpenAI Azure receivables?
4. How much did revenue-share payments from OpenAI to Microsoft increase?
5. How is the Microsoft AI revenue run rate split among Azure AI, Copilot, and GitHub Copilot?
6. How much did inference efficiency offset Cloud gross-margin pressure?
7. What is the FY27 CapEx mix between short-lived GPUs, CPUs, and memory versus long-lived sites and power?
8. Will FY27 CapEx growth fall below AI revenue growth?

If management avoids the first four questions while emphasizing total RPO and total AI revenue, strong earnings would still leave circularity concerns partly unresolved.

## 12. Red team and invalidation

**Counterargument 1: OpenAI revenue growth may be low-quality growth produced by discounts and high inference costs.** Revenue alone does not reduce funding dependence unless gross economics and cash burn improve.

**Counterargument 2: Microsoft's AI revenue includes OpenAI Azure payments and can double count external demand.** If OpenAI buys Azure with investor capital, Microsoft revenue grows without increasing end-system cash. Ex-OpenAI growth and operating cash flow are therefore essential.

**Counterargument 3: CapEx growth can slow while absolute investment continues to surge.** Twenty percent growth on $230 billion remains enormous. The revenue-growth crossover does not guarantee capital efficiency.

The positive base case is invalidated if:

- Azure constant-currency growth falls below 39%;
- RPO growth excluding OpenAI slows below 20%;
- Microsoft Cloud gross margin falls below 63%;
- FY27 investment pace exceeds $250 billion while AI revenue-run-rate growth falls below 50%;
- Microsoft discloses renegotiation, reserves, or added collateral on OpenAI commitments;
- OpenAI Q2 cash burn exceeds $4 billion while annualized revenue remains below $30 billion.

## Final judgment

Microsoft earnings will not be an audit report that eliminates OpenAI-centered AI CapEx circularity in one night. After recapitalization and HLBV adoption, Microsoft's OpenAI investment result is no longer a direct measurement of OpenAI operating loss. Dividing it by 27% should be abandoned.

That does not make the event less important. It makes the scoring framework more precise.

**The central question is not OpenAI's reported accounting loss. It is how quickly external cash catches up with contractual commitments.** Azure above 41%, AI annualized revenue above $47 billion, ex-OpenAI RPO growth above 25%, Cloud gross margin above 64%, and FY27 CapEx growth below AI revenue growth would demonstrate that the loop's weakest link, funding dependence, is beginning to weaken.

July 30, 2026 will not settle whether AI CapEx is circular finance. It can show whether **external customer revenue has begun to outrun infrastructure investment growth**. If that crossover appears, Microsoft and semiconductor stocks can enter a repricing of earnings duration beyond 2028, not merely a short rebound. If it does not, the market will continue to discount OpenAI's $250 billion Azure commitment and larger infrastructure promises as credit rather than revenue.

---

The OpenAI revenue, cash-burn, and market-reaction ranges in this article are judgment estimates based on limited reporting and public business indicators, not official financial results or consensus. Microsoft's OpenAI investment result is affected by HLBV, recapitalization, liquidation preferences, and new funding and does not equal OpenAI operating profit or loss. RPO is contracted future revenue, not cash or recognized revenue. This article does not recommend buying or selling any security.

### Primary sources

- [Microsoft FY26 Q3 results and call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3)
- [Microsoft FY26 Q3 earnings release](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast)
- [Microsoft FY26 Q2 call and OpenAI RPO disclosure](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2)
- [Microsoft FY26 Q1 OpenAI equity-method discussion](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1)
- [Microsoft March 2026 Form 10-Q and HLBV accounting](https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/msft-20260331.htm)
- [April 2026 amended Microsoft-OpenAI agreement](https://openai.com/index/next-phase-of-microsoft-partnership/)
- [OpenAI 2026 funding and enterprise-revenue disclosure](https://openai.com/index/accelerating-the-next-phase-ai/)
- [Microsoft FY26 Q4 earnings schedule](https://news.microsoft.com/source/2026/07/08/microsoft-announces-quarterly-earnings-release-date-68/)
- [2026 FOMC calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)

### Related posts

- [Why Nvidia May Become OpenAI's Guarantor: Anatomy of a $250 Billion Backstop](/en/post/nvidia-openai-250bn-backstop-anatomy-two-lenses-2026-07-29/)
- [Rebound or Terminal Point: Eight Doubts, Seven Variables, and a 48-Hour Verdict](/en/post/ai-capex-eight-doubts-rebound-or-terminal-48hours-2026-07-29/)
- [Big Tech AI Earnings: CapEx, ROI, Memory, and FCF Beyond 2028](/en/post/big-tech-ai-earnings-capex-roi-memory-2028-fcf-2026-07-22/)
- [US Data Center Delays and the ERCOT Power Solution](/en/post/us-datacenter-power-delay-ercot-renewables-bess-bigtech-semiconductor-2026-07-28/)
