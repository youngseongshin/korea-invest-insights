---
title: "What Hyperscaler Earnings Proved, and What They Didn't: Three Explanations for the Memory Sell-Off"
slug: "hyperscaler-proof-memory-selling-three-hypotheses-2026-08-04"
date: 2026-08-04T18:50:00+09:00
description: "Microsoft and Amazon have, for the first time, shown convincing evidence that AI capital spending is converting into real revenue and profit. Azure grew 43% and topped $100bn in annual revenue. AWS grew 36.7%, with an operating margin of 39.4%. All of the $51bn net increase in Microsoft's commercial backlog came from customers outside the frontier model companies. Yet over the same period, foreign investors sold more than 11tn won of Samsung Electronics and SK Hynix alone while net buying the rest of the Korean market. Demand was proven, so why did memory get sold? This piece lays out three hypotheses, a timing lag, a pricing regime shift, and supply arrival, and scores each one. It then examines how NVIDIA's move to cut Vera Rubin's module capacity in half over memory costs changes that scoring."
categories: ["Exclusive Analysis", "Market-Outlook", "Korea-Semiconductor"]
tags:
  - "Microsoft"
  - "Amazon"
  - "NVIDIA"
  - "Rubin"
  - "HBM"
  - "Samsung Electronics"
  - "SK Hynix"
  - "Foreign Investor Flows"
  - "Deleveraging"
  - "CXMT"
  - "Korean Semiconductors"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Related context: In [the August 3 Plunge and Contract Price Deceleration](/post/memory-price-deceleration-p-holds-thesis-2026-08-03/), I wrote that the pace of memory price increases had broken and the investment question had shifted from further price gains to whether prices would hold. This piece looks at a different axis. In the same week, Microsoft and Amazon produced evidence that AI investment is converting into real revenue, and at the very moment demand was confirmed, foreign investors concentrated their selling in the two memory makers. This is the point where the demand axis and the supply axis diverge, and it is what now explains Korean memory stock prices.

## TL;DR

- What Microsoft and Amazon changed is not the fact that capital spending is continuing, but <strong>the strength of the evidence that this spending is converting into revenue, profit, and backlog</strong>. Azure grew 43% for the quarter, and on a fiscal-year basis, annual revenue topped $100bn for the first time (41% annual growth). AWS grew 36.7%, with an operating margin of 39.4% and operating profit up 64%. [Fact: company statements and earnings calls]
- The single strongest line came from Microsoft's CFO. Commercial backlog rose 84% to $678bn, and <strong>the full $51bn net increase came from customers outside the frontier model companies</strong>. Backlog growth excluding OpenAI was still 25%. [Fact: earnings call] This is a concrete data point that directly cuts against the suspicion that backlog is mostly circular contracting with a handful of AI companies.
- Backlog should not be read as if it were cash, though. The same call disclosed the structure behind it: <strong>a weighted average duration of 2.3 years, with about 30% due to be recognized within the next 12 months</strong>. The number that actually matters is that the 12-month portion rose 37% year over year. [Fact: earnings call]
- Yet in the same week that demand was confirmed, Korean memory stocks sold off. Over the month of July, foreign investors net sold more than 11tn won of Samsung Electronics and SK Hynix combined, while <strong>net buying other Korean stocks over the same period</strong>. They bought semiconductor parts, materials and equipment names led by LG Innotek, along with autos. [Fact: aggregated from press reports; figures vary by source] This was not an exit from Korea. It was a reduction in memory specifically.
- Domestic leverage unwinding compounded this. The margin loan balance fell from 38.6tn won at the end of June to 28.9tn won on July 31, with that single day's decline the largest on record. Net assets in single-stock leveraged ETFs fell from about 16tn won at the end of June to about 5.7tn won on July 30. [Fact: Korea Financial Investment Association and press reports] <strong>The record 7.2tn won of foreign net buying on July 31 is interpreted as the trade that absorbed that forced selling</strong>.
- We set up and scored three hypotheses for why memory sold off despite confirmed demand: a timing-lag hypothesis (how long confirmation takes to reach earnings), a pricing-regime hypothesis (pricing power shifting even as demand grows), and a supply-arrival hypothesis (2028 capacity additions overlapping). <strong>What governs price right now is not the first of these but the second and third</strong>, which is why good demand news alone does not resolve it.
- The clearest evidence for the second hypothesis came this week. After memory cost rose to 29% of system cost, above NVIDIA's preferred 20% ceiling, the company <strong>is cutting Vera Rubin's module capacity in half</strong>. LPDDR5X per rack falls from about 55TB to about 28TB. [Fact: TrendForce] Even the strongest demand source redesigns around less memory once price rises far enough.
- The KOSPI rose 1.62% today, and Samsung Electronics and SK Hynix both closed slightly higher. Both stocks, however, remain 36% and 47% below their June highs, respectively. [Fact: market data] Demand risk has fallen, and supply risk has not. That asymmetry is what today's price reflects.

<div class="thesis-callout">
<div class="thesis-callout__label">Key Framing</div>

What this earnings season proved is that AI investment is returning as revenue. What it did not prove is how much of that revenue stays as margin for memory makers. Microsoft's and Amazon's income statements answered the first question. Contract structure and 2028 capacity additions will answer the second. Foreign investors selling only memory while buying parts and materials names is not an exit from Korea. It is pricing that separates these two questions. The logic of buying memory on confirmed demand alone is therefore only half right. The other half depends on where pricing power ends up.

</div>

## 1. What Was Actually Proven

Start with the numbers from both companies. Microsoft posted fiscal fourth-quarter revenue of $90bn and operating income of $40.6bn, with earnings per share up 32%. Azure grew 43% for the quarter, accelerating from 40% the prior quarter, and on a fiscal-year basis, Azure's annual revenue topped $100bn for the first time, with annual growth of 41%. Amazon's AWS revenue was $42.2bn, up 36.7%, the fastest growth rate in 18 quarters, and AWS operating income rose 64% to $16.6bn, putting the operating margin at 39.4%. [Fact: company statements and earnings calls]

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 212" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="196.0" y1="18" x2="196.0" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="196.0" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">0</text>
<line x1="282.3" y1="18" x2="282.3" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="282.3" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">25</text>
<line x1="368.6" y1="18" x2="368.6" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="368.6" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">50</text>
<line x1="454.9" y1="18" x2="454.9" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="454.9" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">75</text>
<text x="184" y="40.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Azure revenue</text>
<rect x="196" y="28.0" width="148.5" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="353.5" y="40.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+43.0%</text>
<text x="688.0" y="40.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">40% prior quarter</text>
<text x="184" y="76.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">AWS revenue</text>
<rect x="196" y="64.0" width="126.7" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="331.7" y="76.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+36.7%</text>
<text x="688.0" y="76.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">best in 18 quarters</text>
<text x="184" y="112.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">AWS operating income</text>
<rect x="196" y="100.0" width="219.6" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="424.6" y="112.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+63.6%</text>
<text x="688.0" y="112.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">39.4% margin</text>
<text x="184" y="148.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Microsoft backlog</text>
<rect x="196" y="136.0" width="290.0" height="16" rx="4" fill="var(--kii-cat-2)"/>
<text x="495.0" y="148.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+84.0%</text>
<text x="688.0" y="148.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">$678bn</text>
<line x1="196" y1="18" x2="196" y2="162.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="360.0" y="204" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">Year-on-year growth, Q2 2026 (%)</text>
</svg>
</div>
<figcaption><strong>Growth in Q2 2026.</strong> Azure and AWS both accelerated, and AWS lifted its operating margin to 39.4% while raising capital spending. Backlog growth is shown in a different colour because it measures something else.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Measure | Year on year |
|---|---|
| Azure revenue | +43% |
| AWS revenue | +36.7% |
| AWS operating income | +63.6% |
| Microsoft commercial RPO | +84% |

</details>
</figure>

What deserves more attention than the growth rate is that <strong>spending and returns moved together in the same quarter</strong>. AWS raised its operating margin from 32.9% a year earlier to 39.4% while increasing capital spending. That points to a phase where investment is generating margin, not eroding it.

The backlog figure is more decisive. Microsoft's commercial backlog rose 84% to $678bn. What matters more than the headline number is its composition. Of the $51bn increase from $627bn the prior quarter, the CFO said the entire sequential increase came from commitments by customers outside the frontier model companies. Backlog growth excluding OpenAI was 25%, and bookings growth excluding OpenAI was 18%. [Fact: earnings call]

Why this line matters becomes clear if you recall last month's doubts. If most of a large-looking backlog were commitments from a single customer, OpenAI, it would look more like circular dealing, and it would wobble if OpenAI's finances wobbled. The fact that the entire net increase came from outside that customer means <strong>the base of demand has genuinely broadened</strong>.

## 2. How Far to Trust the Backlog

Backlog should not be read as equivalent to revenue, though. The structure the company disclosed on the same call forces that restraint. Microsoft's backlog has a weighted average duration of 2.3 years, and about 30% is scheduled to be recognized as revenue within the next 12 months. [Fact: earnings call]

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 180" xmlns="http://www.w3.org/2000/svg" role="img">
<rect x="40" y="64" width="186.0" height="44" rx="4" fill="var(--kii-cat-1)"/>
<rect x="228.0" y="64" width="432.0" height="44" rx="4" fill="var(--kii-cat-1)" fill-opacity="0.28"/>
<text x="133.0" y="91.0" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">2,03400m</text>
<text x="444.0" y="91.0" fill="var(--card-text-color-main)" font-size="13" font-weight="600" text-anchor="middle">4,74600m</text>
<text x="40" y="30" fill="var(--card-text-color-main)" font-size="13.5" font-weight="700">Commercial RPO 6,78000m</text>
<text x="40" y="50" fill="var(--card-text-color-tertiary)" font-size="11.5">Weighted average duration 2.3 years. About 30% recognised within 12 months</text>
<rect x="40" y="128" width="11" height="11" rx="3" fill="var(--kii-cat-1)"/>
<text x="56" y="138" fill="var(--card-text-color-secondary)" font-size="11.5">Recognised within 12 months</text>
<rect x="202" y="128" width="11" height="11" rx="3" fill="var(--kii-cat-1)" fill-opacity="0.28"/>
<text x="218" y="138" fill="var(--card-text-color-secondary)" font-size="11.5">Recognised later</text>
</svg>
</div>
<figcaption><strong>The term structure of the backlog.</strong> Only about 30% of the $678bn becomes revenue within 12 months. The number that matters is not the total but that this 12-month portion grew 37% year on year.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Portion | Amount | Note |
|---|---|---|
| Recognised within 12 months | about $203bn | up 37% year on year |
| Recognised later | about $475bn | weighted average duration 2.3 years |
| Total | $678bn | up 84% year on year |

</details>
</figure>

That works out to roughly $200bn of the $678bn becoming revenue within a year. The rest is recognized over the following two to three years. Reading the 84% backlog increase as an 84% increase in next year's revenue would therefore be wrong.

The number that actually matters is different: <strong>the portion due for recognition within 12 months rose 37% year over year</strong>. That is the indicator of how fast backlog is converting into near-term revenue, and it lines up with Azure's actual 43% growth rate and its 45% guidance for next quarter. Backlog and revenue are not moving independently. They are confirmed to be moving in the same direction.

It is also worth noting that the financial strain has not disappeared. Microsoft said it expects to remain free-cash-flow positive in the next fiscal year, but Amazon's trailing-12-month free cash flow was negative $7.6bn, a reversal from positive $18.2bn in the same period a year earlier. That is the result of net property and equipment purchases rising $66.1bn in a single year. [Fact: company disclosures] Even within the same cycle, financial capacity diverges across companies.

## 3. So Why Did Memory Get Sold?

Korean memory stocks sold off in the very week that demand was confirmed. Who was selling can be identified down to the investor category.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 140" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="236.0" y1="18" x2="236.0" y2="90.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="236.0" y="108.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">-10</text>
<line x1="318.5" y1="18" x2="318.5" y2="90.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="318.5" y="108.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">-5</text>
<line x1="401.0" y1="18" x2="401.0" y2="90.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="401.0" y="108.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+0</text>
<line x1="483.5" y1="18" x2="483.5" y2="90.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="483.5" y="108.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+5</text>
<text x="158" y="40.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">The two memory names</text>
<rect x="214.5" y="28.0" width="186.5" height="16" rx="4" fill="var(--kii-cat-4)"/>
<text x="205.5" y="40.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="end">-11.3</text>
<text x="688.0" y="40.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">Samsung, SK Hynix</text>
<text x="158" y="76.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Rest of KOSPI</text>
<rect x="401.0" y="64.0" width="41.2" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="451.2" y="76.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+2.5</text>
<text x="688.0" y="76.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">parts, autos and others</text>
<line x1="401.0" y1="18" x2="401.0" y2="90.0" stroke="var(--kii-chart-axis)" stroke-width="1.4"/>
<text x="335.0" y="132" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">Foreign net buying, July 2026 (trn won). Approximate, partly back-solved</text>
</svg>
</div>
<figcaption><strong>Foreign net buying in July 2026.</strong> Foreign investors cut the two memory names specifically while buying the rest of the Korean market. The memory figure ranges from 11.3tn to 13.1tn won across sources, and the rest of KOSPI is back-solved.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Group | Net buying | Note |
|---|---|---|
| Samsung Electronics and SK Hynix | about -11tn won or more | 11.3tn-13.1tn across sources |
| Rest of KOSPI | about +2.5tn won | back-solved |

</details>
</figure>

Over the month of July, foreign investors net sold more than 11tn won of Samsung Electronics and SK Hynix combined. Depending on the source, the total ranges from 11.3tn won to 13.1tn won. But foreign net selling across the entire KOSPI over the same period was smaller than that figure. Strip out the two stocks and <strong>foreign investors were net buyers of other Korean stocks</strong>. [Fact: aggregated from press reports; figures vary by source] The top foreign net-buy names in July were in fact led by LG Innotek, followed by semiconductor parts, materials and equipment names such as DB HiTek, Leeno Industrial, Hanmi Semiconductor and Samsung Electro-Mechanics, along with Hyundai Motor and Naver.

This narrows the interpretation. Foreign investors did not exit Korea, and they did not abandon semiconductors. <strong>They cut large-cap memory specifically and rotated into other parts of the same industry</strong>.

Domestic leverage unwinding compounded this. The margin loan balance fell from 38.6tn won at the end of June to 28.9tn won on July 31, with that single day's drop the largest on record. Net assets in single-stock leveraged ETFs tracking Samsung Electronics and SK Hynix fell to roughly a third of their prior level, from about 16tn won at the end of June to about 5.7tn won on July 30. Average monthly returns on those funds were negative 47%. [Fact: Korea Financial Investment Association and press reports]

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="240.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">0.0</text>
<line x1="60" y1="196.8" x2="676.0" y2="196.8" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="200.8" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">8.6</text>
<line x1="60" y1="157.6" x2="676.0" y2="157.6" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="161.6" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">17.3</text>
<line x1="60" y1="118.4" x2="676.0" y2="118.4" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="122.4" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">25.9</text>
<line x1="60" y1="79.2" x2="676.0" y2="79.2" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="83.2" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">34.6</text>
<line x1="60" y1="40.0" x2="676.0" y2="40.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="44.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">43.2</text>
<rect x="98.5" y="61.0" width="77.0" height="175.0" rx="4" fill="var(--kii-cat-3)"/>
<text x="137.0" y="53.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">38.6</text>
<text x="137.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">Margin loans, end-Jun</text>
<text x="137.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">peak</text>
<rect x="252.5" y="105.0" width="77.0" height="131.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="291.0" y="97.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">28.9</text>
<text x="291.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">Margin loans, Jul 31</text>
<text x="291.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">record daily drop</text>
<rect x="406.5" y="163.5" width="77.0" height="72.5" rx="4" fill="var(--kii-cat-3)"/>
<text x="445.0" y="155.5" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">16.0</text>
<text x="445.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">Leveraged ETFs, end-Jun</text>
<text x="445.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">net assets</text>
<rect x="560.5" y="210.2" width="77.0" height="25.8" rx="4" fill="var(--kii-cat-1)"/>
<text x="599.0" y="202.2" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">5.7</text>
<text x="599.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">Leveraged ETFs, Jul 30</text>
<text x="599.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">one third left</text>
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="60" y="24" fill="var(--card-text-color-tertiary)" font-size="11.5">Size (trn won). Margin loan balance and single-stock leveraged ETF assets</text>
</svg>
</div>
<figcaption><strong>The July deleveraging.</strong> Margin loan balances and single-stock leveraged ETF assets both fell sharply within a month. The single-day drop in margin loans on 31 July was the largest on record.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Measure | End of June | End of July |
|---|---|---|
| Margin loan balance | 38.6tn won | 28.9tn won (31 Jul) |
| Single-stock leveraged ETF assets | about 16tn won | about 5.7tn won (30 Jul) |

</details>
</figure>

The record 7.2tn won of foreign net buying on July 31 should also be read in this context. Domestic brokerages interpret it as buying that came after a large share of the forced-selling volume had already been absorbed. [Inference: aggregated from brokerage commentary] After one more round of larger selling on August 3, the KOSPI rose 1.62% today, and Samsung Electronics and SK Hynix closed up 0.21% and 0.64% respectively. Both stocks remain 36% and 47% below their June highs, respectively. [Fact: market data]

## 4. Three Explanations, Scored

There are three hypotheses that explain why memory sold off despite confirmed demand. Here is a judgment on which one is governing price right now.

| Hypothesis | Description | Implication | Current score |
|---|---|---|---|
| Timing lag | It takes two to three quarters for hyperscaler earnings visibility to pass through memory contracts and reach reported results. The market will not wait that long | If you wait, it resolves itself, so now is an opportunity | Partly true, but this alone does not explain buying parts and materials names while selling only memory |
| Pricing regime | Even as demand grows, pricing power shifting to a small number of large buyers lets volume rise while margin gets compressed | The discount is justified and will not be resolved by demand news | Dominant. Slowing contract price growth and the expansion of long-term contracts are evidence, and this week's NVIDIA case is decisive |
| Supply arrival | Korea's new fabs and CXMT's capacity additions both land in 2028 | Confirmed demand is a 2026-27 story and does not settle the 2028 debate | Dominant. The direct trigger for this morning's weakness was also a report on CXMT reviewing a new Beijing plant |

[Inference: hypothesis framing and scoring are our own judgment]

The third row has today's real-world example. The direct trigger for this morning's semiconductor weakness was a report that CXMT is reviewing construction of a new DRAM plant in Beijing. [Fact: press report] Three days after evidence of demand from U.S. big tech emerged, a single piece of Chinese capacity news pushed the sector back down. That contrast shows which axis the market is actually watching right now.

Domestic brokerages' price target cuts point to the same axis. When several brokerages recently lowered their targets, the reasons cited were falling NAND contract prices, progress in China's domestic lithography equipment, and CXMT's planned listing. It is hard to find one that cited weak demand as the reason. [Fact: aggregated from brokerage reports] That said, most of the brokerages that cut targets kept their ratings unchanged and characterized the current pullback as excessive relative to fundamentals.

## 5. NVIDIA Is Cutting Back on Memory

The clearest evidence supporting the second hypothesis came this week. It is also the strongest counterargument to the bull case.

NVIDIA is moving to cut the capacity of the SOCAMM modules used in Vera Rubin systems in half, from 192GB to 96GB per module. The reason is that memory cost rose to 29% of the roughly $2.1 million system cost, above the company's preferred 20% ceiling. If this change goes through, LPDDR5X per NVL72 rack falls from about 55TB to about 28TB, and the corresponding memory cost per rack falls from about $1.2 million to about $590,000. [Fact: TrendForce, July 28]

<strong>As price rose, the strongest demand source is redesigning its systems to use less memory.</strong> The same mechanism covered in yesterday's post, the affordability ceiling on consumer devices, is now showing up inside AI servers. This does not mean demand is disappearing. It means price is limiting itself, and it shows where the math of multiplying volume growth by rising unit prices to project revenue eventually stops.

There is one more signal pointing the same way. What HBM4 adds is not capacity but bandwidth. The prior generation, GB300, already carried 288GB of HBM3E per GPU, and Vera Rubin's HBM4 is also 288GB, the same capacity. What changed is bandwidth, up roughly 2.75 times from 8TB/s to as much as 22TB/s. [Fact: NVIDIA technical documentation] That runs against the common assumption that moving to HBM4 automatically means more memory content per system. Total volume still rises if GPU count per rack and unit shipments increase, but the generational transition itself does not automatically lift volume.

## 6. Rubin's Timeline

Before sizing the benefit, the timing needs to be precise. Vera Rubin and Rubin Ultra are different products on different schedules.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 326" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="118" y1="20" x2="118" y2="282" stroke="var(--kii-chart-axis)" stroke-width="1.5"/>
<text x="102" y="30" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Jun 2026</text>
<circle cx="118" cy="26" r="6" fill="var(--kii-cat-1)"/>
<circle cx="118" cy="26" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="138" y="30" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Vera Rubin in full production</text>
<text x="138" y="48" fill="var(--card-text-color-tertiary)" font-size="11.5">HBM4 qualified at Samsung, SK Hynix and Micron</text>
<text x="102" y="84" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Q3 2026</text>
<circle cx="118" cy="80" r="6" fill="var(--kii-cat-1)"/>
<circle cx="118" cy="80" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="138" y="84" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Partner shipments begin</text>
<text x="138" y="102" fill="var(--card-text-color-tertiary)" font-size="11.5">eight clouds in the first wave</text>
<text x="102" y="138" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">26 Aug 2026</text>
<circle cx="118" cy="134" r="6" fill="var(--kii-cat-3)"/>
<circle cx="118" cy="134" r="9" fill="none" stroke="var(--kii-cat-3)" stroke-opacity="0.32" stroke-width="2"/>
<text x="138" y="138" fill="var(--card-text-color-main)" font-size="13" font-weight="600">NVIDIA fiscal Q2 results</text>
<text x="138" y="156" fill="var(--card-text-color-tertiary)" font-size="11.5">this print is still Blackwell-led</text>
<text x="102" y="192" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Q4 2026</text>
<circle cx="118" cy="188" r="6" fill="var(--kii-cat-3)"/>
<circle cx="118" cy="188" r="9" fill="none" stroke="var(--kii-cat-3)" stroke-opacity="0.32" stroke-width="2"/>
<text x="138" y="192" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Volume ramp</text>
<text x="138" y="210" fill="var(--card-text-color-tertiary)" font-size="11.5">Rubin revenue first appears in the November print</text>
<text x="102" y="246" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">H2 2027</text>
<circle cx="118" cy="242" r="6" fill="var(--kii-cat-4)"/>
<circle cx="118" cy="242" r="9" fill="none" stroke="var(--kii-cat-4)" stroke-opacity="0.32" stroke-width="2"/>
<text x="138" y="246" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Rubin Ultra, official schedule</text>
<text x="138" y="264" fill="var(--card-text-color-tertiary)" font-size="11.5">Kyber rack reported slipping to 2028, specs cut</text>
</svg>
</div>
<figcaption><strong>The Rubin schedule.</strong> Vera Rubin is what can be put into supply-chain numbers today; Rubin Ultra belongs in the option set rather than the base case. The 26 August print is still Blackwell-led.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| When | What |
|---|---|
| June 2026 | Vera Rubin in full production, HBM4 qualified at three suppliers |
| Q3 2026 | Partner shipments begin |
| 26 August 2026 | NVIDIA fiscal Q2 results |
| Q4 2026 | Volume ramp; Rubin revenue from the November print |
| H2 2027 | Rubin Ultra official schedule, with reported delays |

</details>
</figure>

Vera Rubin entered full production on June 1, with partner shipments in the third quarter of this year and volume ramp in the fourth quarter. All three HBM4 suppliers, Samsung Electronics, SK Hynix and Micron, were confirmed to have passed qualification and entered mass production as of early June. [Fact: NVIDIA and press reports] In other words, <strong>Vera Rubin is what can actually show up in supply chain results right now</strong>.

Rubin Ultra sits in the second half of 2027 on the official roadmap, but two separate delay signals have surfaced. Reports in early July said the Kyber rack is being pushed to 2028 because of substrate manufacturing problems, and reported HBM capacity per GPU has been revised down twice, from an initial 1TB to 384GB and then to around 192GB. NVIDIA has said its roadmap is intact, but that statement refers to the standard product shipping in the second half of this year, so both claims can be true at once. [Fact: press reports, unconfirmed by NVIDIA] Rubin Ultra and HBM4E should therefore stay in the outlook, but it is premature to treat them as the base case.

NVIDIA's next earnings report is on August 26, and that report will still be centered on Blackwell. Rubin revenue will not actually show up in the numbers until the November report. [Fact: NVIDIA disclosures] What fills that gap in between is what to watch through August and September.

## 7. Verdict and Watch List

What this earnings season lowered is demand risk. What it did not raise is supply risk, and what it newly revealed is a path by which price limits demand on its own. The judgment on memory stock prices right now comes down to this. The logic of buying memory on the strength of hyperscaler earnings is only half right. The part about confirmed demand is correct. How much of that demand turns into memory makers' margin is decided by a different axis.

Here is a record of what would need to be confirmed to rule each hypothesis in or out.

| What to confirm | Timing | Which hypothesis it moves |
|---|---|---|
| Absolute level of contract liabilities in Samsung Electronics' and SK Hynix's quarterly reports | Mid-August | A large increase in customer prepayments weakens the pricing-regime hypothesis |
| NVIDIA's fiscal Q2 results and commentary on Rubin | August 26 | An earlier ramp schedule strengthens the timing-lag hypothesis |
| Third-quarter server DRAM contract price settlement | September | Coming in above the 13-18% forecast weakens the pricing-regime hypothesis |
| Whether CXMT's Beijing plant actually breaks ground | Ongoing | Confirmation strengthens the supply-arrival hypothesis |
| Whether NVIDIA's SOCAMM capacity cut is actually implemented | Ongoing | If implemented, price elasticity is confirmed and volume forecasts should be lowered |
| Whether foreign investors turn net buyers of memory again | Ongoing | The simplest indicator that the supply-demand overhang has been worked off |

Finally, here are the conditions that would overturn this piece's verdict. If third-quarter contract prices come in well above forecast, if NVIDIA reverses the SOCAMM capacity cut, or if CXMT's capacity additions are confirmed to be delayed, the weight of the second and third hypotheses falls and the timing-lag hypothesis becomes dominant. At that point, the verdict would shift toward today's discount having been an opportunity.

---

The stocks named in this piece are examples for analysis and do not constitute a recommendation to buy or sell any specific security. Responsibility for investment decisions and their outcomes rests with the investor. Microsoft's and Amazon's earnings figures are based on each company's statements and earnings calls. The combined foreign net-selling figure for July for the two stocks ranges from 11.3tn won to 13.1tn won depending on the source, so this piece states it only as more than 11tn won; the estimate of net buying excluding memory is a derived figure and has limited precision. Margin loan and leveraged ETF figures are based on press reports, and some items show minor differences across sources. NVIDIA's SOCAMM capacity cut, the Rubin Ultra specification changes, and the Kyber rack delay come from research firms and press reports and have not been confirmed by NVIDIA. The construction and scoring of the three hypotheses is judgment, not statistical estimation. Prices and indicators are as of the close on August 4, 2026.

### Related Posts

- [Memory No Longer Needs Prices to Rise Further: Anatomy of the August 3 Plunge and the Contract Price Deceleration](/post/memory-price-deceleration-p-holds-thesis-2026-08-03/)
- [July Earnings Season Wrap: AI Demand Was Confirmed, and Memory Pricing Became an Industry-Wide Cost](/post/july-2026-earnings-two-listings-kimi-four-worries-2026-07-31/)
- [Rebound or Terminal? Eight Doubts, Seven Discriminators, and a 48-Hour Verdict](/post/ai-capex-eight-doubts-rebound-or-terminal-48hours-2026-07-29/)
- [Why Does NVIDIA Want to Be OpenAI's Guarantor? Anatomy of the $250 Billion Backstop](/post/nvidia-openai-250bn-backstop-anatomy-two-lenses-2026-07-29/)
