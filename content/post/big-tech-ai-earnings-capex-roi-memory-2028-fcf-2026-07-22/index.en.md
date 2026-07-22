---
title: "Big Tech AI Earnings: 2027 Demand Is Contracted, but 2028 Free Cash Flow Is the Real Test"
slug: "big-tech-ai-earnings-capex-roi-memory-2028-fcf-2026-07-22"
date: 2026-07-22T17:30:00+09:00
description: "A four-quarter review of Amazon, Microsoft, and Alphabet tests how long AI demand can outgrow expectations, whether $570-580 billion of 2026 capital spending can earn an adequate return, and what it means for HBM, server DRAM, and enterprise SSD demand beyond 2028."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags:
  - "Amazon"
  - "Microsoft"
  - "Alphabet"
  - "AWS"
  - "Azure"
  - "Google Cloud"
  - "AI CAPEX"
  - "Free Cash Flow"
  - "HBM"
  - "DRAM"
  - "NAND"
  - "Hyperscaler Credit"
series: ["exclusive-analysis", "hbm", "macro-gates-2026"]
valley_cashtags:
  - Samsung Electronics
  - SK hynix
draft: false
---

Amazon, Microsoft, and Alphabet plan to spend roughly $570-580 billion on capital investment in 2026. Their latest reported cloud growth rates were 28%, 39% in constant currency, and 63%, respectively. The market is no longer debating whether current AI demand is strong. It is asking whether the data centers built now will be well utilized, whether revenue can outrun depreciation and power costs, and whether memory profits can survive the supply response expected from 2028.

The last four quarters suggest that much of the demand through 2027 is already supported by contracts, reservations, and supply constraints. Beyond 2028, scarcity is no longer enough. Utilization, inference revenue, customer concentration, and cash collection become the decisive variables.

> Related context
> This is a follow-up to the [July Big Tech earnings and memory thesis preview](/en/post/big-tech-july-earnings-call-memory-thesis-scenarios-2026-07-07/). The financing side is covered in [Hyperscaler financing and the memory bottleneck](/en/post/hyperscaler-financing-race-ai-capex-memory-bottleneck-2026-07-07/), while the semiconductor supply response is developed in the [weekly semiconductor deep dive](/en/post/weekly-semiconductor-deep-dive-strong-earnings-lower-multiple-2028-pivot-2026-07-19/).

## Summary

* AI demand is likely to remain stronger than expected through 2027. Backlogs, long-term commitments, supply shortages, and customer expansion point in the same direction.
* The most durable demand is likely to come from enterprise inference, agents, coding, search, and data services rather than one-off frontier training runs.
* The three companies plan approximately $570-580 billion of 2026 capital spending. Spending can grow again in 2027, although the growth rate should slow from an unusually high base.
* Return on investment should be measured through incremental cloud gross profit and first-party revenue or cost savings, less depreciation, power, and financing costs.
* Current evidence supports the highest probability of post-2028 free cash flow recovery at Alphabet, followed by Microsoft and Amazon. Alphabet shows the clearest combination of monetization and unit-cost improvement. Microsoft has the strongest contracted visibility but more concentration and lease complexity. Amazon has the largest rebound option but the greatest current cash-flow pressure.
* Memory purchases should continue across HBM, server DRAM, and enterprise SSDs. Custom accelerators change the product mix but do not remove the need for memory.
* The principal risk after 2028 is price rather than bit demand. New capacity can reduce average selling prices and margins even if memory shipments keep rising.
* Credit conditions are cautionary, not distressed. Bond books remain covered, but lower cover ratios and wider long-end spreads show that capital markets are beginning to impose discipline.

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Core judgment</div>
  <div class="thesis-callout__body">
    Through 2027, supply constraints and contracted demand support continued spending. From 2028, the decisive variables shift to utilization, cash collection, and returns after depreciation. For memory, strong volume and normalizing prices can coexist.
  </div>
</div>

---

## 1. The three earnings calls and the questions that matter

Alphabet reports at 5:30 a.m. KST on July 23, Microsoft at 6:30 a.m. KST on July 30, and Amazon at 6:00 a.m. KST on July 31, based on company investor-relations announcements.

| Company | Earnings time | Primary question |
|---|---|---|
| Alphabet | July 23, 05:30 KST | How quickly do 63% cloud growth and a $462.3 billion backlog convert into revenue and cash? |
| Microsoft | July 30, 06:30 KST | When does Azure supply improve, and does backlog growth reaccelerate outside OpenAI? |
| Amazon | July 31, 06:00 KST | Can AWS protect margins and restore free cash flow while Amazon spends about $200 billion? |

The market is trying to answer three questions. How long can AI demand grow above expectations, and from which customers and workloads? How much longer can capital spending rise, and can the investments earn adequate returns? Will that spending translate into recurring purchases of HBM, server DRAM, and enterprise SSDs?

The last four quarters provide a constructive answer to the first question. The second and third require company-specific analysis because a dollar spent on accelerators has a different return profile from a dollar spent on land, power, networking, or long-lived buildings.

## 2. Four quarters of operating evidence

### 2.1 Amazon: AWS accelerated while cash left first

| Quarter | AWS revenue | YoY growth | AWS operating income | Cash-flow signal |
|---|---:|---:|---:|---|
| Q2 2025 | $30.9B | +17.5% | $10.2B | TTM FCF $18.2B |
| Q3 2025 | $33.0B | +20% | $11.4B | AI infrastructure spending kept rising |
| Q4 2025 | $35.6B | +24% | $12.4B | Amazon signaled about $200B of 2026 investment |
| Q1 2026 | $37.6B | +28% | $14.2B | TTM FCF fell to $1.2B |

AWS growth accelerated for four consecutive quarters. Its Q1 operating margin reached 37.8%, showing that revenue and profit expanded despite supply constraints.

The cash profile moved in the opposite direction. Amazon generated $148.5 billion of trailing operating cash flow, but net property and equipment spending reached $147.3 billion. AWS-centered long-term commitments stood at $364 billion with a weighted-average remaining life of 5.5 years. Revenue visibility is high, but spending occurs before the associated revenue arrives.

Amazon's 2025 shareholder letter stated that the company was not spending $200 billion on a hunch and had substantial customer commitments. Graviton, Trainium, and Nitro together exceeded a $20 billion annual revenue run rate and were growing at a triple-digit rate. Custom silicon is both a cost-control tool and a way to keep workloads inside AWS.

Amazon can produce the largest cash-flow rebound if the new assets fill quickly, but it also has the widest gap to close. AWS needs to maintain growth around the high-20% range and defend margins in the mid-to-high 30s while 2026 investments begin monetizing in 2027 and 2028.

Sources: [Amazon Q1 2026 results](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/default.aspx), [Amazon 2025 shareholder letter](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2025-letter-to-shareholders), [Amazon Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/amzn-20260331.htm)

### 2.2 Microsoft: the strongest contract visibility and the largest concentration question

| Quarter | Revenue | Azure growth, constant currency | RPO | Capital spending | Free cash flow |
|---|---:|---:|---:|---:|---:|
| FY25 Q4 | $76.4B | about +39% | $368B | $24.2B | $25.6B |
| FY26 Q1 | $77.7B | +39% | $392B | $34.9B | $25.7B |
| FY26 Q2 | $81.3B | +38% | $625B | $37.5B | $5.9B |
| FY26 Q3 | $82.9B | +39% | $627B | $31.9B | $15.8B |

Azure grew 40% as reported and 39% in constant currency in the latest quarter. Microsoft's AI business exceeded a $37 billion annual revenue run rate and grew 123%. Commercial RPO reached $627 billion with an average duration of 2.5 years, and roughly 25% is expected to convert to revenue over the next 12 months.

Contract quality needs to be separated from contract size. OpenAI accounted for approximately 45% of commercial RPO in FY26 Q2, while RPO excluding OpenAI grew 26% in FY26 Q3. A major strategic customer and a broader enterprise expansion are both present.

Microsoft also has the most complex capital-spending definition. Q3 cash property and equipment spending was $30.9 billion, while spending including finance leases reached $31.9 billion. Management said roughly two-thirds of capital spending went to shorter-lived assets such as GPUs and CPUs, with one-third allocated to land and buildings. Short-lived assets monetize earlier but also return to the replacement cycle sooner.

Azure is expected to remain supply constrained through 2026, with modest growth acceleration possible in the second half of the calendar year. Q4 capital spending is expected to exceed $40 billion. Calendar 2026 investment is approximately $190 billion, including about $25 billion of component inflation. Microsoft expects double-digit revenue and operating-income growth in FY27.

The company has the strongest contracted visibility, but post-2028 free cash flow depends on independent enterprise demand, Copilot and agent usage, lease-adjusted cash generation, and whether gross profit grows faster than depreciation.

Sources: [Microsoft FY26 Q3 earnings call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3), [Microsoft FY26 Q3 results](https://www.microsoft.com/en-us/investor/earnings/FY-2026-Q3/press-release-webcast)

### 2.3 Alphabet: demand, margin, and unit-cost improvement are visible together

| Quarter | Google Cloud revenue | YoY growth | Operating income | Margin | Backlog | Capital spending |
|---|---:|---:|---:|---:|---:|---:|
| Q2 2025 | $13.6B | +32% | $2.8B | 20.7% | $106B | $22.4B |
| Q3 2025 | $15.2B | +34% | $3.6B | 23.7% | $155B | $24.0B |
| Q4 2025 | $17.7B | +48% | $5.3B | 30.1% | $240B | $27.9B |
| Q1 2026 | $20.0B | +63% | $6.6B | 32.9% | $462.3B | $35.7B |

Alphabet delivered the clearest simultaneous improvement. Cloud growth accelerated from 32% to 63%, the operating margin rose from 20.7% to 32.9%, and backlog increased from $106 billion to $462.3 billion.

Q1 generative AI product revenue grew 800%. New customers doubled, deals between $100 million and $1 billion doubled, and Alphabet signed multiple deals above $1 billion. Existing customers consumed 45% more than their original commitments. Gemini Enterprise paid monthly users rose 40% quarter over quarter.

Unit economics also improved. Alphabet said the cost per AI response fell by more than 30%. Higher demand and lower unit cost are the best combination for infrastructure returns. The same infrastructure supports Search, YouTube, Workspace, and advertising, so external cloud revenue understates part of the return.

Alphabet guides to $180-190 billion of 2026 capital spending and expects another significant increase in 2027. Q1 uncommenced asset commitments were approximately $108.6 billion, and uncommenced data-center leases were $75.6 billion, scheduled to begin between 2026 and 2031. Total RPO was $467.6 billion, with just over half expected to be recognized within 24 months.

The main risk is the speed of spending itself. Q1 operating cash flow was $45.8 billion and capital spending was $35.7 billion, leaving quarterly free cash flow of $10.1 billion. Trailing free cash flow remained a substantial $64.4 billion, but another large increase in 2027 spending could delay the recovery.

Current evidence nevertheless places Alphabet first in proving AI investment returns. The next call needs to clarify how much backlog growth came from a few large contracts and how quickly new facilities are filling.

Sources: [Alphabet Q1 2026 earnings call](https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx), [Alphabet Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm)

## 3. Where AI demand can persist

AI demand should be divided into five layers with different customers and durations.

| Demand layer | Customers | Expected durability | Key evidence |
|---|---|---|---|
| Frontier training and post-training | Leading model labs and first-party models | Strong but concentrated | Cluster reservations, long-term power contracts, model roadmaps |
| Enterprise inference and agents | Finance, retail, manufacturing, healthcare, government | Most durable candidate | Paid users, calls, spend per customer, renewals |
| Development and coding | Software companies and developers | Rapid adoption, strong price competition | Seats, agent runtime, generated code, retention |
| Data, storage, and general cloud | Existing cloud customers | Stable and bundled with AI | Database, storage, networking, migrations |
| First-party services | Search, advertising, productivity, commerce, recommendations | Revenue and cost savings combined | Conversion, cost per response, productivity, gross margin |

### 3.1 Supply should remain the constraint through 2027

AWS, Azure, and Google Cloud have all described supply constraints. Alphabet customers used 45% more than their initial commitments. Microsoft expects constraints through the end of 2026. Amazon's long-term commitments have an average 5.5 years remaining.

This supports a capacity-led revenue model through at least 2027. As data centers open and power is connected, revenue should follow. Near-term spending reductions are also difficult because construction, leases, power, servers, and memory are already under contract.

### 3.2 2028 is more likely to be a change in demand quality than a demand cliff

More facilities and semiconductor supply arrive from 2028. Once scarcity eases, investors must test whether customers actually use reserved capacity, renew contracts, and increase usage fast enough to offset lower inference prices.

Demand can remain high while profitability falls. Model efficiency and custom silicon reduce cost per task, while cloud competition can lower revenue per token. If call volume grows faster than pricing declines, utilization and revenue still rise.

The useful relationship is:

`AI revenue growth = workload growth + customer growth - price decline per workload`

Enterprise agents, coding, and embedded inference have the best chance of producing high-frequency, recurring use.

### 3.3 Independent customers are the most important proof

Strategic customer contracts support early demand, but reciprocal investment and revenue commitments can overstate final demand. Confidence after 2028 requires more usage from enterprises, governments, developers, and smaller customers without financing links to the infrastructure provider.

Alphabet's doubled new-customer count, doubled large-deal count, and commitment overages are the clearest current evidence. Microsoft's 26% RPO growth excluding OpenAI is more important than total RPO alone. Amazon needs to disclose more about how much of AWS commitments comes from AI versus general cloud demand.

## 4. How much longer can capital spending grow?

### 4.1 Approximately $570-580 billion in 2026

| Company | 2026 investment plan | Definition caveat |
|---|---:|---|
| Amazon | about $200B | Primarily AI and AWS, with some spending elsewhere |
| Microsoft | about $190B | Cash spending and finance leases can both be included |
| Alphabet | $180-190B | Servers, data centers, networks, and custom silicon |
| Total | about $570-580B | Accounting definitions differ across companies |

The absolute amount can grow again, but the 60-100% growth rates seen in 2026 are difficult to repeat. The base is larger, while power, sites, transformers, networking equipment, and skilled labor remain constrained.

The following 2027 ranges are analytical scenarios, not company guidance.

| Scenario | Combined 2027 spending | Conditions |
|---|---:|---|
| Downside | $530-580B | Slower bookings, power delays, digestion of 2026 prebuys |
| Base | $630-665B | Continued constraints, slower growth rate, execution of existing commitments |
| Upside | Above $700B | Agent usage surge, additional sovereign demand, custom silicon and GPU expansion |

A slower capital-spending growth rate is not by itself a bearish signal. The warning comes when slower spending, cloud growth, and backlog appear together.

### 4.2 A simple return framework

`AI investment return = incremental cloud gross profit + first-party revenue and savings - depreciation - power - financing cost`

Capital spending hits the cash-flow statement first. Depreciation enters the income statement after servers and data centers begin operating. Cash-flow troughs and accounting-margin troughs therefore occur at different times.

Free cash flow is pressured first in 2026. Revenue and depreciation rise together in 2027-2029. Around 2030, accelerators purchased in 2026 can begin returning to the replacement cycle. Cash flow can recover before reported margins fully absorb depreciation.

### 4.3 Current evidence by company

| Company | Positive evidence | Remaining risk | Confidence in post-2028 FCF recovery |
|---|---|---|---|
| Alphabet | Cloud +63%, margin 32.9%, cost per response down more than 30% | Fast spending growth, leases, possible large-deal concentration | Highest |
| Microsoft | Azure +39%, RPO $627B, AI ARR above $37B | OpenAI concentration, finance leases, short-lived assets | Medium-high |
| Amazon | AWS +28%, margin 37.8%, commitments $364B | TTM FCF $1.2B, $200B spending, monetization lag | Medium |

## 5. The dashboard for 2028 and beyond

| Metric | Constructive signal | Warning signal |
|---|---|---|
| Independent-customer RPO | Growth outside strategically financed customers | A few customers drive most of the increase |
| Next-12-month recognition | A larger share of RPO converts soon | Contract duration rises while near-term conversion slows |
| Cash collection | Cash receipts outgrow contract assets | Receivables and contract assets grow without deposits |
| Operating cash flow | Four-quarter OCF growth exceeds capex growth by at least 10 points | OCF trails investment growth |
| Cloud economics | Gross profit growth exceeds depreciation and power growth | Revenue grows while margin falls |
| Utilization | New capacity fills rapidly | Low utilization after power connection |
| Lease-adjusted FCF | Recovery remains after finance leases | Reported FCF improves while lease obligations rise |
| Custom silicon | Lower cost and higher customer use | R&D rises without adoption |
| Memory contracts | Commitments convert to shipments and cash | Deferrals, renegotiation, or cancellations |
| Supply normalization | Shipments and utilization hold despite lower prices | ASP and utilization fall together |
| Replacement cycle | First-generation assets earn returns before replacement | Replacement begins before initial payback |

The strongest combination is independent RPO growth, new capacity going online, stable cloud margins, and OCF growth overtaking capital-spending growth. The most dangerous combination is easing supply constraints, slower growth, higher depreciation, rising customer concentration, and increasing debt or leases.

## 6. Credit markets are imposing discipline, not signaling a crisis

Apollo reports that hyperscaler bond cover ratios fell from around 5 times in February 2026 to below 2 times in July. Demand still exceeds supply, but investors have become more selective.

Amazon issued $25 billion of bonds on July 7. Orders peaked near $62 billion and ended around $41 billion after pricing. Its longest maturities offered an additional 18-21 basis points of yield. Funding remained available, but at a higher cost.

The Bank of England's July 2026 Financial Stability Report said AI-related issuance had not yet impaired broader investment-grade terms or availability. Barclays projected approximately $240 billion of 2026 investment-grade hyperscaler financing, comparable to major bank issuance.

The signal is yellow, not red. Capital markets remain open but increasingly demand backlog quality, utilization, and cash conversion. This should delay weaker projects and widen capital-cost differences rather than end AI spending outright.

Sources: [Apollo hyperscaler bond cover ratios](https://www.apollo.com/wealth/insights-news/insights/daily-spark/cover-ratios-for-hyperscaler-bonds-declining), [Bank of England July 2026 Financial Stability Report](https://www.bankofengland.co.uk/financial-stability-report/2026/july-2026), [Amazon bond demand](https://fortune.com/2026/07/08/amazons-25-billion-surprise-bond-sale-dangled-extra-yield-to-lure-in-buyers/)

## 7. Does the spending become recurring memory demand?

### 7.1 AI systems require a memory hierarchy

| Memory layer | Function | Demand direction |
|---|---|---|
| HBM | Bandwidth close to GPUs and ASICs | Strongest in HBM3E and HBM4 |
| Server DRAM | CPU work, agent orchestration, preprocessing, caches, metadata | Expands with agents and multi-model systems |
| Enterprise SSD and NAND | Checkpoints, vector databases, documents, video, long-context storage | Expands with inference volume and retention |

Training is HBM intensive. Enterprise inference and agents expand server DRAM and SSD demand alongside HBM. Multiple agents repeat tasks and preserve longer context, increasing memory outside the accelerator.

TPUs, Trainium, and Maia can displace some external GPUs but still require HBM, server DRAM, and storage. Custom silicon changes specifications, packaging, and bargaining power rather than eliminating memory demand.

### 7.2 Procurement is indirect and arrives with a lag

Hyperscalers do not purchase all HBM directly. Procurement runs through Nvidia, custom ASIC partners, server ODMs, and packaging suppliers. Capital spending therefore reaches memory-vendor revenue with a lag through design, allocation, wafer starts, packaging, server assembly, and installation.

Micron's strategic customer agreements illustrate the connection. It has 16 agreements, generally covering 2026-2030, representing roughly 20% of DRAM volume and one-third of NAND volume. Fourteen agreements contain approximately $100 billion of cumulative minimum-price revenue, supported by about $22 billion of customer deposits and financing commitments.

Long-term agreements raise the earnings floor. Take-or-pay and minimum prices reduce cancellation and downside pricing. Ceiling prices can also limit upside when spot prices surge. These contracts reduce the severity of a downturn but do not permanently lock in today's scarcity margins.

Source: [Micron FY3Q26 prepared remarks](https://investors.micron.com/static-files/631b1a32-5537-46ae-8f40-82e42fc79dfe)

### 7.3 The 2028 memory risk is price, not necessarily demand

Additional DRAM, NAND, and HBM packaging capacity should arrive from 2027 and 2028. Bit shipments can keep growing while average selling prices and margins normalize.

`Memory profit = bit shipments × price per bit - expansion, depreciation, and input costs`

In 2026 and 2027, demand is growing faster than supply, supporting both volume and price. From 2028, supply growth can reduce pricing even if bit demand stays high. Micron's current gross margin above 80% reflects scarcity and should not be treated as a steady-state margin.

The semiconductor conclusion therefore requires more than a direction for Big Tech capital spending. Utilization, memory supply growth, contract pricing, inventory, and producer capital discipline must be read together.

## 8. Company-specific earnings checklist

### Alphabet

* Cloud growth near 60%, with both new customers and usage increasing.
* Backlog rising from $462.3 billion without a deterioration in near-term recognition.
* Continued explanation for $180-190 billion of 2026 spending and the 2027 step-up.
* Cloud margin staying above 30% and cost per response falling further.
* Evidence that external TPU sales and internal usage both scale.

### Microsoft

* Azure growth near 39-40% after additional supply comes online.
* RPO growth reaccelerating outside OpenAI.
* More than $40 billion of quarterly spending converting into revenue quickly.
* Paid Copilot and agent seats accompanied by actual usage and revenue.
* Operating cash flow growing faster than capital spending and finance leases.

### Amazon

* AWS growth in the high 20s and margins in the mid-to-high 30s.
* Faster conversion of the $364 billion commitment base.
* Trainium adoption and revenue demonstrating a cost advantage over external GPUs.
* A clear 2027-2028 monetization schedule for roughly $200 billion of investment.
* Operating cash flow rising while net investment growth slows.

## 9. Three paths for 2028-2031

These probabilities are analytical judgments, not company guidance.

### Base case, 55%

Capital spending rises again in 2027 but at a slower rate. New data centers fill, and enterprise inference and agent revenue expand. Alphabet recovers free cash flow first, followed by Microsoft. Amazon recovers later because of a longer monetization lag.

Semiconductor revenue remains high, but new supply normalizes memory prices and margins from 2028. HBM and server DRAM volumes remain strong while explosive spot-price increases fade.

### Upside case, 20%

Agent, coding, search, and enterprise inference usage grows faster than unit-price declines. Sovereign and enterprise customers add demand. Combined 2027 capital spending exceeds $700 billion while operating cash flow also expands.

HBM4, advanced packaging, server DRAM, and enterprise SSD shortages persist into 2028. Memory contract volumes and prices rise, producing another round of semiconductor earnings upgrades.

### Downside case, 25%

Model efficiency and price competition reduce revenue per task quickly. Strategic contracts are renegotiated, and new data centers operate below expected utilization. Depreciation and power costs are already committed, pressuring margins and free cash flow.

Memory supply added in 2027-2029 exceeds demand growth, pushing down ASP and utilization together. Long-term agreements soften the decline but do not protect uncontracted volume and spot pricing.

## 10. Conclusion

AI demand is likely to remain stronger than expected through 2027. Cloud growth, backlogs, supply constraints, and long-term infrastructure commitments support that view. The customer base is broadening from frontier labs to enterprise inference, coding, search, and general cloud workloads.

Capital spending should remain elevated in 2027, although its growth rate can slow. A slowdown from a very high base is not a cycle break. The real warning would be simultaneous weakness in backlog, utilization, cloud margins, and operating cash flow.

Current evidence gives Alphabet the best chance of post-2028 free cash flow recovery. It has shown demand growth, margin improvement, and lower unit costs together. Microsoft has stronger contract visibility but more OpenAI concentration and finance-lease complexity. Amazon has powerful AWS economics and significant rebound potential, but it must close the gap between $200 billion of investment and trailing free cash flow of only $1.2 billion.

Memory purchases should continue, but the decisive post-2028 issue is pricing after supply expands. Custom silicon and inference efficiency change the mix across HBM, server DRAM, and enterprise SSDs rather than eliminating demand. Strategic customer agreements raise the floor but do not make current scarcity margins permanent.

The most important figures in these earnings calls are not capital spending totals alone. Independent-customer backlog, next-12-month conversion, utilization, cloud margins, and lease-adjusted free cash flow must move together. If they improve, 2028 becomes the start of cash harvesting. If customer concentration rises while utilization and cash collection lag, today's earnings strength can return as tomorrow's depreciation burden.

---

> This article is based on public company investor-relations materials, SEC filings, and industry sources. Backlogs and long-term agreements improve visibility but remain subject to usage, recognition timing, pricing, and contract terms. This is informational analysis, not a recommendation to buy or sell securities.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
