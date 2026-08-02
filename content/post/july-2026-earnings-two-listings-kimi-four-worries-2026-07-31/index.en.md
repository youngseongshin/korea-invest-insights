---
title: "July Earnings Season Wrap: AI Demand Was Confirmed, and Memory Pricing Became an Industry-Wide Cost"
slug: "july-2026-earnings-two-listings-kimi-four-worries-2026-07-31"
date: 2026-07-31T12:40:00+09:00
description: "An independent report closing out the July earnings season. It synthesizes ten earnings reports and calls, from TSMC to Samsung Electronics, SK Hynix, Microsoft, Meta, Amazon, Apple, and IBM, two record-breaking listings (SK Hynix's Nasdaq ADR and CXMT's Shanghai debut), and the Kimi K3 shock into a single picture. The data is consistent. Cloud growth accelerated across the board and everyone talked about a supply shortfall, yet the market has started grading capital expenditure against revenue proof in the very same quarter. The least-noticed variable is memory pricing. It became Amazon's stated reason for raising capital expenditure, Apple called it a hundred-year flood, and the recipients on the other side of that flow are Korea's two memory makers. Building on this evidence, the piece sorts out what earnings actually answered for the market's four worries: token demand, frontier-lab profitability, capex ROI paired with supply expansion, and semiconductor profitability beyond 2028."
categories: ["Exclusive Analysis", "Market-Outlook", "Macro-Analysis"]
tags: ["Earnings Season", "TSMC", "Microsoft", "Meta", "Amazon", "Apple", "Alphabet", "IBM", "Samsung Electronics", "SK Hynix", "CXMT", "Kimi", "FOMC", "HBM", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Context: [Rebound or Terminal?](/post/ai-capex-eight-doubts-rebound-or-terminal-48hours-2026-07-29/) wrote that the two blank cells in the discriminator table (policy and monetization) would fill in within 48 hours. Those 48 hours have passed, and both cells are now filled. This piece carries that verdict, but more broadly closes out the month of July as an independent report. It synthesizes ten earnings reports and calls, two record-breaking listings, and one China-born model shock into a single picture, and sorts out what this earnings season actually answered for the four worries the market keeps asking about: AI token demand, frontier-lab profitability, capex ROI paired with semiconductor supply expansion, and semiconductor profitability beyond 2028.

## TL;DR

- July's earnings season played out in the middle of a rout, and the data that came out pointed in one direction. <strong>Every demand metric came in above expectations, while the price reaction was conditional</strong>. Growth at the three cloud majors (Google Cloud +82%, Azure +43%, AWS +36.7%) all accelerated, and all three said on their earnings calls that supply could not keep up with demand.
- The grammar of capital expenditure has changed. Raising the number is no longer good news by itself. <strong>Only companies that proved revenue acceleration in the same quarter as their spending increase were rewarded</strong>. Microsoft was rewarded with a +15% move, its biggest since 2008, and Amazon got a +7 to +10% after-hours pop, while Alphabet (-5 to -7%), Meta (-9.7%), and TSMC (Taiwan shares -7.3%), all of which raised spending without proof, were punished.
- July's earnings season had a least-noticed variable: memory pricing. Amazon named memory costs as the reason for raising capital expenditure to $220bn, Apple's CEO called the surge in memory prices a "hundred-year flood," and IBM saw mainframe revenue fall 42% as customer budgets shifted into pre-buying memory. <strong>Memory emerged as a cost-of-goods line item on income statements worldwide</strong>, and the recipients on the other side of that flow were Samsung Electronics (89.5tn won in quarterly operating profit) and SK Hynix (60.5tn won, a 76% margin).
- The same month produced two record-breaking memory capital raises. SK Hynix's Nasdaq ADR raised $26.5bn (the largest-ever US listing by a foreign company), and CXMT's Shanghai listing raised $8.6bn (up 466% on day one, briefly the largest market cap on the mainland board). Capital markets <strong>placed simultaneous bets, in the same month, on Korean memory's present and Chinese memory's future</strong>.
- Kimi K3 was not a rerun of DeepSeek. It erased $470bn in 72 hours, but most of that was recovered, and the question it left behind ran the opposite direction from price destruction. <strong>Bigger models use more memory</strong>. The arrival of a 2.8 trillion-parameter open-weight model was reinterpreted as upside fuel for inference infrastructure, memory demand in particular.
- Verdicts on the four worries. Token demand: the evidence disproves the fear (4 to 7 times annual volume growth overwhelms the price decline). Frontier-lab profitability: a fork in the road (Anthropic is on track for its first operating profit this quarter, OpenAI is not projected to turn a profit until 2030). Capex ROI: a paradox holds (a 95% enterprise pilot failure rate and a combined hyperscaler backlog above $1.6tn are both true at once). Profitability beyond 2028: undecided, a contest between the new structure of LTAs and prepayments and the new variable of CXMT's capacity expansion.
- The two blank cells from the previous piece's discriminator table are now filled in too. Policy: a hawkish hold (all three dissenters argued for a hike, September hike odds at 61%), so the headwind continues. Monetization: a tailwind, with Microsoft's equity-method stake in OpenAI swinging to a profit (+$0.48bn) and an Azure surprise. The market's combined answer was the KOSPI's largest-ever intraday surge on July 31 (+16.5% intraday).

<div class="thesis-callout">
<div class="thesis-callout__label">Key Framing</div>

July's share prices reflected a late-dot-com phase, but the earnings that actually arrived looked closer to the early part of a cycle. All three clouds grew faster than in the prior quarter, backlogs rose to a combined $1.7tn, and management at all four companies worried about supply rather than demand. Earnings did attach a condition, though. The market no longer accepts capital expenditure on the strength of a long-term outlook and has started grading it against revenue proof in the same quarter. And memory pricing, the central variable in that grading, appeared for the first time this quarter as a cost line at several IT companies. The supercycle's profits are real, but their durability is now re-examined every quarter.

</div>

## 1. What Happened in July

The analysis that follows only holds up if the month's events are laid out in chronological order first. The point of this map is the density of events. Two record-breaking listings, the worst day on record (IBM), and the best day on record (Microsoft's market cap, the KOSPI's rate of gain), all crowded into three weeks.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 720 582" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="122" y1="26" x2="122" y2="504" stroke="var(--kii-chart-axis)" stroke-width="1.5"/>
<text x="96" y="34" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Jul 10</text>
<circle cx="122" cy="30" r="6.5" fill="var(--kii-cat-2)"/>
<circle cx="122" cy="30" r="9.5" fill="none" stroke="var(--kii-cat-2)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="34" fill="var(--card-text-color-main)" font-size="13" font-weight="600">SK Hynix lists ADRs on Nasdaq (SKHY)</text>
<text x="144" y="51" fill="var(--card-text-color-tertiary)" font-size="11.5">$26.5bn raised, largest-ever US listing by a foreign company</text>
<text x="96" y="86" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Jul 14</text>
<circle cx="122" cy="82" r="6.5" fill="var(--kii-cat-1)"/>
<circle cx="122" cy="82" r="9.5" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="86" fill="var(--card-text-color-main)" font-size="13" font-weight="600">IBM pre-announcement</text>
<text x="144" y="103" fill="var(--card-text-color-tertiary)" font-size="11.5">-25.2% in one day, the worst day in company history</text>
<text x="96" y="138" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Jul 16</text>
<circle cx="122" cy="134" r="6.5" fill="var(--kii-cat-1)"/>
<circle cx="122" cy="134" r="9.5" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="138" fill="var(--card-text-color-main)" font-size="13" font-weight="600">TSMC results; Kimi K3 released</text>
<text x="144" y="155" fill="var(--card-text-color-tertiary)" font-size="11.5">Record results with a capex raise; a 2.8T-parameter model the same day</text>
<text x="96" y="190" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Jul 17-20</text>
<circle cx="122" cy="186" r="6.5" fill="var(--kii-cat-4)"/>
<circle cx="122" cy="186" r="9.5" fill="none" stroke="var(--kii-cat-4)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="190" fill="var(--card-text-color-main)" font-size="13" font-weight="600">The Kimi shock</text>
<text x="144" y="207" fill="var(--card-text-color-tertiary)" font-size="11.5">~$470bn of US AI and semiconductor market cap erased in 72 hours</text>
<text x="96" y="242" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Jul 22</text>
<circle cx="122" cy="238" r="6.5" fill="var(--kii-cat-1)"/>
<circle cx="122" cy="238" r="9.5" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="242" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Alphabet results</text>
<text x="144" y="259" fill="var(--card-text-color-tertiary)" font-size="11.5">Cloud +82%, yet the third capex raise sends the stock down 5-7%</text>
<text x="96" y="294" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Jul 27</text>
<circle cx="122" cy="290" r="6.5" fill="var(--kii-cat-2)"/>
<circle cx="122" cy="290" r="9.5" fill="none" stroke="var(--kii-cat-2)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="294" fill="var(--card-text-color-main)" font-size="13" font-weight="600">CXMT lists in Shanghai</text>
<text x="144" y="311" fill="var(--card-text-color-tertiary)" font-size="11.5">+466% on day one, briefly mainland China's largest cap; NVIDIA CDS hits record</text>
<text x="96" y="346" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Jul 28</text>
<circle cx="122" cy="342" r="6.5" fill="var(--kii-cat-4)"/>
<circle cx="122" cy="342" r="9.5" fill="none" stroke="var(--kii-cat-4)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="346" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Black Tuesday</text>
<text x="144" y="363" fill="var(--card-text-color-tertiary)" font-size="11.5">Samsung -13%, SK Hynix -14% intraday</text>
<text x="96" y="398" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Jul 29</text>
<circle cx="122" cy="394" r="6.5" fill="var(--kii-cat-3)"/>
<circle cx="122" cy="394" r="9.5" fill="none" stroke="var(--kii-cat-3)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="398" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Hawkish FOMC hold (9-3); earnings triple-header</text>
<text x="144" y="415" fill="var(--card-text-color-tertiary)" font-size="11.5">SK Hynix miss, Microsoft surprise, Meta shock</text>
<text x="96" y="450" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Jul 30</text>
<circle cx="122" cy="446" r="6.5" fill="var(--kii-cat-1)"/>
<circle cx="122" cy="446" r="9.5" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="450" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Samsung confirmed results; Amazon and Apple</text>
<text x="144" y="467" fill="var(--card-text-color-tertiary)" font-size="11.5">Microsoft +15%, its biggest day since 2008</text>
<text x="96" y="502" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Jul 31</text>
<circle cx="122" cy="498" r="6.5" fill="var(--kii-cat-4)"/>
<circle cx="122" cy="498" r="9.5" fill="none" stroke="var(--kii-cat-4)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="502" fill="var(--card-text-color-main)" font-size="13" font-weight="600">KOSPI's largest daily gain ever</text>
<text x="144" y="519" fill="var(--card-text-color-tertiary)" font-size="11.5">+16.5% intraday; Samsung +21.5%, SK Hynix +23.5%</text>
<circle cx="113" cy="564" r="5.5" fill="var(--kii-cat-1)"/>
<text x="124" y="568" fill="var(--card-text-color-secondary)" font-size="11.5">Earnings</text>
<circle cx="228.6" cy="564" r="5.5" fill="var(--kii-cat-2)"/>
<text x="239.6" y="568" fill="var(--card-text-color-secondary)" font-size="11.5">Listings/Capital</text>
<circle cx="433.79999999999995" cy="564" r="5.5" fill="var(--kii-cat-3)"/>
<text x="444.79999999999995" y="568" fill="var(--card-text-color-secondary)" font-size="11.5">Policy/Models</text>
<circle cx="605.4" cy="564" r="5.5" fill="var(--kii-cat-4)"/>
<text x="616.4" y="568" fill="var(--card-text-color-secondary)" font-size="11.5">Market</text>
</svg>
</div>
<figcaption><strong>July's main events.</strong> The declines (the Kimi shock, Black Tuesday) came before the earnings; the record rebound came after them. July 31 figures are intraday.</figcaption>
</figure>

Two rhythms are visible on this map. First, the selloffs came before earnings and the rebounds came after. The Kimi shock (July 17-20) and Black Tuesday (July 28) both happened before Big Tech reported, while the largest rebound on record (July 30-31) came after Microsoft's and Amazon's numbers landed. If the rout was a matter of positioning rather than information, it makes sense that earnings would reverse it, and that is exactly what happened. Second, capital and prices moved in opposite directions. In the very week stock prices were collapsing, 9.42 million accounts piled into CXMT's subscription (a 244x subscription rate), and SK Hynix's ADR climbed to a 51% premium over its Seoul common shares just four days after listing. [Fact: press reports, aggregated] Fear in the secondary market and greed in the primary market coexisted in the same week.

## 2. Demand, Measured: Growth Rates, Tokens, Backlogs

The market's first worry is AI token demand: whether volume is growing fast enough to offset the steadily falling price per token. This season is the first to answer that question with hard numbers.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 166" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="150.0" y1="16" x2="150.0" y2="118.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="150.0" y="136.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+0%</text>
<line x1="266.7" y1="16" x2="266.7" y2="118.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="266.7" y="136.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+30%</text>
<line x1="383.3" y1="16" x2="383.3" y2="118.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="383.3" y="136.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+60%</text>
<line x1="500.0" y1="16" x2="500.0" y2="118.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="500.0" y="136.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+90%</text>
<text x="138" y="37.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Google Cloud</text>
<rect x="150" y="25.0" width="318.9" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="477.9" y="37.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+82%</text>
<text x="529.9" y="37.0" fill="var(--card-text-color-tertiary)" font-size="11">operating income 3.1x</text>
<text x="138" y="71.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Azure</text>
<rect x="150" y="59.0" width="167.2" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="326.2" y="71.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+43%</text>
<text x="378.2" y="71.0" fill="var(--card-text-color-tertiary)" font-size="11">beat 39-40% guidance</text>
<text x="138" y="105.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">AWS</text>
<rect x="150" y="93.0" width="142.7" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="301.7" y="105.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+36.7%</text>
<text x="353.7" y="105.0" fill="var(--card-text-color-tertiary)" font-size="11">fastest in 18 quarters</text>
<line x1="150" y1="16" x2="150" y2="118.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="325.0" y="158" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">Q2 2026 (Apr-Jun quarter for Microsoft) revenue growth, YoY</text>
</svg>
</div>
<figcaption><strong>Growth at the three clouds.</strong> All three accelerated from the prior quarter, and all three called out supply constraints on their calls. Azure's next-quarter guide is 45%.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Business | Growth (YoY) | Note |
|---|---|---|
| Google Cloud | +82% | operating income 3.1x, backlog $513.9bn |
| Azure | +43% | beat 39-40% guidance, next quarter guided 45% |
| AWS | +36.7% | fastest in 18 quarters, backlog $496bn |

</details>
</figure>

Beneath the headline growth rates sit three more layers of evidence. First, token volume. Google disclosed that it processes 3,200 trillion tokens a month, roughly seven times what it processed a year ago. By the earnings-call metric, that is 22 billion tokens per minute, up 38% from 16 billion a quarter earlier. At Microsoft Foundry, the number of customers using more than 1 trillion tokens a year has quadrupled in a year, and throughput on the third-party tracker OpenRouter is up fivefold in six months. [Fact: company disclosures, OpenRouter data] Prices kept falling over the same period (roughly a 67% cut for Anthropic's top-tier model). If volume is growing 4 to 7 times a year while prices are falling by roughly half a year, the product of the two is still strongly positive. In gap-ratio terms, the numerator (end-market AI revenue) is growing faster than the denominator (capital expenditure).

Second, backlogs. Microsoft's commercial RPO stands at $678bn (+84%), Google Cloud's backlog at $513.9bn (up about $52bn in a single quarter), and AWS's backlog at $496bn (versus $364bn the prior quarter). Combined, the three approach $1.7tn. [Fact: company filings] One detail here matters more than any other this season. Roughly $51bn of Microsoft's net RPO increase <strong>came entirely from customers outside the frontier-model companies</strong>. RPO growth excluding OpenAI ran +25%, and bookings growth excluding OpenAI ran +18%. [Fact: CFO Amy Hood, earnings call] That is a direct rebuttal, delivered this quarter, to the circular-revenue worry, the suspicion that the backlog is a mirage built on OpenAI alone.

Third, a chorus of supply-constraint language. Pichai said, "we remain supply constrained." Hood said "demand continues to exceed available supply." Meta's Susan Li said "there are still plenty of ROI-positive places to deploy compute if we had it." And Amazon's Jassy went further still: "even $220bn won't fill 2026 demand, 2027 will be the same, and the demand already on the books for 2028 is striking." [Fact: respective earnings calls] Not one of the four was worried about demand. All four were worried about supply.

## 3. The Standard for Grading Capex Has Changed

We turn to the capex ROI worry. The real news this season is not the size of the spending, it is how differently the market reacted to it.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 720 234" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="150.0" y1="16" x2="150.0" y2="186.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="150.0" y="204.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">0</text>
<line x1="240.0" y1="16" x2="240.0" y2="186.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="240.0" y="204.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">60</text>
<line x1="330.0" y1="16" x2="330.0" y2="186.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="330.0" y="204.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">120</text>
<line x1="420.0" y1="16" x2="420.0" y2="186.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="420.0" y="204.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">180</text>
<line x1="510.0" y1="16" x2="510.0" y2="186.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="510.0" y="204.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">240</text>
<text x="138" y="37.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Amazon</text>
<rect x="150" y="25.0" width="330.0" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="489.0" y="37.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">220</text>
<text x="541.0" y="37.0" fill="var(--card-text-color-tertiary)" font-size="11">post-print +7-10%</text>
<text x="138" y="71.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Alphabet</text>
<rect x="150" y="59.0" width="300.0" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="459.0" y="71.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">200</text>
<text x="511.0" y="71.0" fill="var(--card-text-color-tertiary)" font-size="11">post-print -5-7%</text>
<text x="138" y="105.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Microsoft</text>
<rect x="150" y="93.0" width="262.5" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="421.5" y="105.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">175</text>
<text x="473.5" y="105.0" fill="var(--card-text-color-tertiary)" font-size="11">post-print +15%</text>
<text x="138" y="139.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Meta</text>
<rect x="150" y="127.0" width="206.2" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="365.2" y="139.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">137.5</text>
<text x="417.2" y="139.0" fill="var(--card-text-color-tertiary)" font-size="11">post-print -9.7%</text>
<text x="138" y="173.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">TSMC</text>
<rect x="150" y="161.0" width="93.0" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="252.0" y="173.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">62</text>
<text x="304.0" y="173.0" fill="var(--card-text-color-tertiary)" font-size="11">post-print -7.3% (Taiwan)</text>
<line x1="150" y1="16" x2="150" y2="186.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="330.0" y="226" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">2026 capex guidance ($bn) and the immediate stock reaction</text>
</svg>
</div>
<figcaption><strong>2026 capex guidance and the share-price reaction.</strong> The size of the number had nothing to do with the reaction; same-quarter revenue proof did. Microsoft's $175bn is the calendar-2026 figure after the accounting reclassification.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Company | 2026 capex guidance | Stock, post-print |
|---|---|---|
| Amazon | ~$220bn | +7-10% |
| Alphabet | $195-205bn | -5-7% |
| Microsoft | ~$175bn (calendar) | +15% |
| Meta | $130-145bn | -9.7% |
| TSMC | $60-64bn | -7.3% (Taiwan) |

</details>
</figure>

Line up the five reactions and a rule emerges. The size of the spending had nothing to do with the reaction. Amazon, the biggest spender, was rewarded; TSMC, the smallest, was punished. Only one thing separated the two groups: <strong>whether the company proved revenue acceleration and cash flow in the same quarter as its spending increase</strong>. Microsoft paired Azure growth of +43% (above its 39-40% guidance) with a 45% guide for the next quarter, and Amazon pushed AWS growth to its fastest pace in 18 quarters while posting a 39.4% operating margin. Alphabet, by contrast, posted the best growth rate of the group, cloud +82%, and still drew attention for free cash flow swinging to negative $5.8bn, while Meta saw capex consume 98% of quarterly operating cash flow, watched free cash flow collapse 91% year over year to $0.78bn, and drew more than ten price-target cuts after declining to give 2027 spending guidance. [Fact: company filings and press reports]

Two footnotes are needed. First, Microsoft's "capex cut" (from roughly $190bn to roughly $175bn for calendar 2026) is not a real reduction but an accounting reclassification. It reflects extending the useful life of data centers and buildings from 15 to 25 years and shifting some finance leases to operating leases, and the CFO said outright that "excluding this impact, our investment expectations are unchanged." [Fact: earnings call] The market rewarded the stock anyway, fully aware of this. It is worth flagging from a depreciation-debate standpoint. But because the asset in question is buildings rather than servers or GPUs, it sits in a different category from the more serious worry about stretching four-year GPU depreciation out to six years. Second, the shadow of 2027. Goldman Sachs puts base-case 2027 hyperscaler capex at $1.1tn and estimates roughly a third of it will be debt-funded. [Fact: press reports] Once spending has reached 100% of operating cash flow, every additional dollar has to pass through the capital markets. The grading will only get stricter each quarter.

The evidence on enterprise adoption remains cold. The oft-cited MIT survey found 95% of pilots fail to produce measurable ROI; BCG's 2026 survey found only 26% of companies generated meaningful financial value; and Gartner expects more than 40% of agentic AI projects to be cancelled by the end of 2027. [Fact: respective organizations] Yet the backlog stands at $1.7tn in the same season. There are only two ways to resolve this paradox: either the backlog turns out to be future cancellations, or the adoption failure rate is offset by spending concentrated among a small number of successful companies. The evidence so far (the backlog's spread beyond frontier labs, the rising enterprise share of token volume) points toward the latter, but that is a trend, not a verdict. [Inference: original synthesis]

## 4. Memory Pricing Showed Up as a Cost Line in Other Companies' Results

This is the least-reported and most important pattern of the season. Memory pricing became, for the first time, <strong>an earnings variable outside the memory companies themselves</strong>.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 720 306" xmlns="http://www.w3.org/2000/svg" role="img">
<rect x="16" y="16" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-4)" stroke-width="1.6"/>
<rect x="16" y="16" width="4" height="58" rx="2" fill="var(--kii-cat-4)"/>
<text x="30" y="37" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">Amazon</text>
<text x="30" y="54" fill="var(--card-text-color-tertiary)" font-size="11">capex $200bn to $220bn, citing memory costs</text>
<line x1="256" y1="45.0" x2="261.0" y2="153.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<rect x="16" y="88" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-4)" stroke-width="1.6"/>
<rect x="16" y="88" width="4" height="58" rx="2" fill="var(--kii-cat-4)"/>
<text x="30" y="109" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">Apple</text>
<text x="30" y="126" fill="var(--card-text-color-tertiary)" font-size="11">a “hundred-year flood”; all of next quarter's margin drop</text>
<line x1="256" y1="117.0" x2="261.0" y2="153.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<rect x="16" y="160" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-4)" stroke-width="1.6"/>
<rect x="16" y="160" width="4" height="58" rx="2" fill="var(--kii-cat-4)"/>
<text x="30" y="181" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">IBM</text>
<text x="30" y="198" fill="var(--card-text-color-tertiary)" font-size="11">client budgets diverted to memory pre-buys; Z revenue -42%</text>
<line x1="256" y1="189.0" x2="261.0" y2="153.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<rect x="16" y="232" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-4)" stroke-width="1.6"/>
<rect x="16" y="232" width="4" height="58" rx="2" fill="var(--kii-cat-4)"/>
<text x="30" y="253" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">Samsung DX</text>
<text x="30" y="270" fill="var(--card-text-color-tertiary)" font-size="11">first segment loss since 2021, -0.8tn won</text>
<line x1="256" y1="261.0" x2="261.0" y2="153.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<rect x="271.0" y="105.0" width="178" height="96" rx="10" fill="var(--kii-cat-1)" fill-opacity="0.12" stroke="var(--kii-cat-1)" stroke-width="2"/>
<text x="360.0" y="131.0" fill="var(--card-text-color-main)" font-size="13.5" font-weight="700" text-anchor="middle">Memory pricing</text>
<text x="360.0" y="152.0" fill="var(--card-text-color-secondary)" font-size="11.5" text-anchor="middle">Contract prices, QoQ</text>
<text x="360.0" y="169.0" fill="var(--card-text-color-secondary)" font-size="11.5" text-anchor="middle">DRAM +30-45%</text>
<text x="360.0" y="186.0" fill="var(--card-text-color-secondary)" font-size="11.5" text-anchor="middle">NAND +50-68%</text>
<rect x="468" y="88.0" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-1)" stroke-width="1.6"/>
<rect x="468" y="88.0" width="4" height="58" rx="2" fill="var(--kii-cat-1)"/>
<text x="482" y="109.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">Samsung DS</text>
<text x="482" y="126.0" fill="var(--card-text-color-tertiary)" font-size="11">quarterly operating profit 89.2tn won</text>
<line x1="459.0" y1="153.0" x2="462" y2="117.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<path d="M 462 117.0 l -7 -4 l 0 8 z" fill="var(--kii-chart-axis)"/>
<rect x="468" y="160.0" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-1)" stroke-width="1.6"/>
<rect x="468" y="160.0" width="4" height="58" rx="2" fill="var(--kii-cat-1)"/>
<text x="482" y="181.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">SK Hynix</text>
<text x="482" y="198.0" fill="var(--card-text-color-tertiary)" font-size="11">quarterly operating profit 60.5tn won, 76% margin</text>
<line x1="459.0" y1="153.0" x2="462" y2="189.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<path d="M 462 189.0 l -7 -4 l 0 8 z" fill="var(--kii-chart-axis)"/>
</svg>
</div>
<figcaption><strong>Where memory costs showed up.</strong> This quarter memory pricing showed up as an earnings variable for four payers, with two recipients on the other side. Contract-price gains are the quarterly ASP moves the two companies disclosed.</figcaption>
</figure>

Reading the diagram from the left, these are the payers. Amazon raised capex from $200bn to $220bn and named rising memory costs as the reason. Apple CEO Tim Cook called the spike in memory prices a "hundred-year flood," and the CFO said more than 100% of the margin decline built into next quarter's guidance was attributable to memory costs. IBM had the worst day in its history (-25%), and one cause was that enterprise customers redirected their late-June budgets into pre-buying servers, storage, and memory ahead of price increases, pushing out mainframe purchases. In the words of IBM's CFO it was "not destruction, but deferral," but it belongs to the first wave of cases where memory has rattled someone else's earnings. Even Samsung Electronics was not exempt: its set-selling DX division posted its first loss since the division was created (-0.8tn won) on the back of rising component costs. The one segment where TSMC saw negative growth, its smartphone platform (-4%), also traced back to set demand cooling as component prices rose. [Fact: company filings and earnings calls]

On the right side of the diagram sit those receiving the payments. Samsung Electronics posted revenue of 171.5tn won and operating profit of 89.5tn won (a 52.2% margin), a record for the third straight quarter, with the DS division earning 99.7% of it. That beat consensus by 6.3%. SK Hynix posted revenue of 79.3tn won and operating profit of 60.5tn won, a 76% operating margin, a figure that does not belong in manufacturing. Net income came to 93.9tn won, but that includes a one-time 63tn won gain tied to its Kioxia stake, so operating profit is the right line to read for the core business. [Fact: both companies' filings]

And yet SK Hynix missed earnings (-4%) on these results, and the stock fell by roughly 10% on the day. The anatomy of the miss matters. The cause was not weak demand but three structural factors. Quarterly ASP gains slowed (DRAM +30% quarter over quarter, down from the 60%-plus pace of the first quarter); about 50% of revenue is locked in at LTA fixed prices, so the spot-price spike did not flow into earnings; and some HBM4 shipments were pushed into the second half. [Fact: press reports and earnings call, aggregated] None of the three is bad news. LTAs are designed precisely to protect earnings on the way down in a cycle, and giving up some upside on the way up is the symmetric price of that design. The structure confirmed on the earnings call is worth recording. SK Hynix finished typically five-year LTAs with more than ten customers and locked in half its revenue. Samsung Electronics said it is targeting 60-70% of capacity under long-term contracts, has already collected about a quarter of total prepayments, and has written price floors into its contracts. Talks on 2027 HBM volumes and prices are underway ("progressing smoothly amid solid demand"). [Fact: both companies' earnings calls] Neither company discloses the absolute size of contract liabilities, so the mid-August quarterly report is the venue to check. [Blocked: quarterly report not yet filed]

The next data point for price is the third-quarter contract round. TrendForce maintains its forecast of +13-18% for server DRAM contract prices, but expects multi-year LTAs held by US CSPs to cap the increase for those customers, concentrating the gains among non-LTA and spot customers instead. [Fact: TrendForce, July 9] In short, contract structure increasingly determines this cycle's profits, and that structure compresses earnings volatility in both directions. It is the lesson of 2018, written into the accounting this time.

## 5. Two Record Listings in the Same Month

July produced two record-breaking capital raises for the memory industry, two weeks apart.

SK Hynix came first. On July 10 it listed an ADR on Nasdaq (ticker SKHY), raising $26.5bn, the largest-ever US listing by a foreign company, surpassing Alibaba's 2014 listing. The $149 offer price closed up 13% on day one, the premium over its Seoul common shares widened to 51% within four days, and the Korea Securities Depository's ADR conversion limit (2.5% of shares outstanding) was exhausted on the listing day itself. [Fact: press reports, aggregated] The stated purpose is explicitly to fund HBM-centered AI memory investment. The mere opening of a channel for US investors to access Korean memory is itself a supply-and-demand event, and the fact that a premium formed before index inclusion (the SOX requires three months of trading history) means demand for that channel is running ahead of supply.

Seventeen days later, on the other side, CXMT listed on Shanghai's STAR Market. It raised $8.6bn in the offering (up to the equivalent of $9.8bn including the greenshoe over-allotment), rose 466% on day one, and reached a market cap of 3.66tn yuan (about $489bn), briefly the largest of any mainland-listed company. [Fact: press reports, aggregated] What matters more than how the market views this company is what the company actually is. Start with the numbers.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="150.0" y1="16" x2="150.0" y2="152.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="150.0" y="170.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">0%</text>
<line x1="264.5" y1="16" x2="264.5" y2="152.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="264.5" y="170.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">10%</text>
<line x1="379.0" y1="16" x2="379.0" y2="152.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="379.0" y="170.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">20%</text>
<line x1="493.5" y1="16" x2="493.5" y2="152.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="493.5" y="170.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">30%</text>
<line x1="608.0" y1="16" x2="608.0" y2="152.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="608.0" y="170.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">40%</text>
<text x="138" y="37.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Samsung</text>
<rect x="150" y="25.0" width="435.1" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="594.1" y="37.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">38%</text>
<text x="138" y="71.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">SK Hynix</text>
<rect x="150" y="59.0" width="332.1" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="491.1" y="71.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">29%</text>
<text x="138" y="105.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Micron</text>
<rect x="150" y="93.0" width="251.9" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="410.9" y="105.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">22%</text>
<text x="138" y="139.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">CXMT</text>
<rect x="150" y="127.0" width="91.6" height="16" rx="4" fill="var(--kii-cat-4)"/>
<text x="250.6" y="139.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">8%</text>
<text x="302.6" y="139.0" fill="var(--card-text-color-tertiary)" font-size="11">3% a year ago</text>
<line x1="150" y1="16" x2="150" y2="152.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="379.0" y="192" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">Global DRAM revenue share, Q1 2026</text>
</svg>
</div>
<figcaption><strong>Global DRAM revenue share, Q1 2026.</strong> CXMT went from 3% to 8% in a year. That this 8% coexisted with double-digit price increases is this quarter's measurement.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Company | Share |
|---|---|
| Samsung | 38% |
| SK Hynix | 29% |
| Micron | 22% |
| CXMT | 8% (3% a year ago) |

</details>
</figure>

CXMT's first quarter of 2026 brought revenue of 50.8bn yuan (+719%) and net income of 24.8bn yuan, from a company that posted a full-year loss of 7.1bn yuan as recently as 2024. The composition of that swing to profit is the key point: first-quarter bit shipments rose 11%, while ASP rose roughly 57%. [Fact: prospectus, SemiAnalysis] In other words, <strong>CXMT's profit was not made by CXMT, it was made by this cycle's prices</strong>. Korea's two memory makers took the same pricing tailwind to margins of 52-76%, while CXMT has only just turned it into a profit. That is the technology gap, expressed in accounting terms.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 290" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="54" y1="238.0" x2="682.0" y2="238.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="45" y="242.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">0</text>
<line x1="54" y1="187.0" x2="682.0" y2="187.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="45" y="191.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">150</text>
<line x1="54" y1="136.0" x2="682.0" y2="136.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="45" y="140.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">300</text>
<line x1="54" y1="85.0" x2="682.0" y2="85.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="45" y="89.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">450</text>
<line x1="54" y1="34.0" x2="682.0" y2="34.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="45" y="38.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">600</text>
<rect x="98.0" y="147.9" width="69.1" height="90.1" rx="4" fill="var(--kii-cat-1)"/>
<text x="132.5" y="141.9" fill="var(--card-text-color-main)" font-size="11.5" font-weight="600" text-anchor="middle">265</text>
<text x="132.5" y="257.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">End-2025</text>
<rect x="255.0" y="119.0" width="69.1" height="119.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="289.5" y="113.0" fill="var(--card-text-color-main)" font-size="11.5" font-weight="600" text-anchor="middle">350</text>
<text x="289.5" y="257.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">End-2026</text>
<rect x="412.0" y="95.2" width="69.1" height="142.8" rx="4" fill="var(--kii-cat-1)"/>
<text x="446.5" y="89.2" fill="var(--card-text-color-main)" font-size="11.5" font-weight="600" text-anchor="middle">420</text>
<text x="446.5" y="257.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">2027</text>
<rect x="569.0" y="51.0" width="69.1" height="187.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="603.5" y="45.0" fill="var(--card-text-color-main)" font-size="11.5" font-weight="600" text-anchor="middle">550</text>
<text x="603.5" y="257.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">2028</text>
<line x1="54" y1="238.0" x2="682.0" y2="238.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<rect x="54" y="267" width="11" height="11" rx="3" fill="var(--kii-cat-1)"/>
<text x="70" y="276" fill="var(--card-text-color-secondary)" font-size="11.5">CXMT wafer starts (k wpm)</text>
<text x="54" y="20" fill="var(--card-text-color-tertiary)" font-size="11">k wafer starts per month; 2028 shows the midpoint of 500-600</text>
</svg>
</div>
<figcaption><strong>CXMT wafer-start roadmap.</strong> Roughly 420k in 2027 is about 17% of global DRAM capacity; Micron's current starts are about 385k. Based on the SemiAnalysis roadmap; Nomura is more aggressive, Morningstar far more conservative.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Point | Wafer starts (k wpm) |
|---|---|
| End-2025 | ~265 |
| End-2026 | ~350 |
| 2027 | ~420 |
| 2028 | 500-600 |

</details>
</figure>

The expansion roadmap looks as shown above; roughly 420,000 wafers by 2027 would equal about 17% of global DRAM capacity. Its annual capacity additions (70,000-85,000 wafers) exceed the combined annual additions of the three Korean and US producers. [Fact: SemiAnalysis roadmap] Still, the limits of what CXMT actually is are just as clear. Its workhorse process remains 1z-class (G4), using DUV multi-patterning without EUV, and the prospectus itself acknowledges rising difficulty at the next node (G5). Its HBM wafer sort yield is estimated at about 35% (versus 85-90% industry-wide), accounts for under 2% of capacity, and there are even reports that the prospectus's use-of-proceeds section contains no HBM-specific line item. [Fact: press reports, some conflicting] Forecasts diverge sharply. Nomura sees an 18% share by 2028 (with a price target 12 times the offer price), SemiAnalysis sees 12% by 2027, and Morningstar puts fair value at less than a third of the market price. [Fact: respective institutions]

There are three takeaways from a Korean memory perspective. First, the threat timeline differs by product. Commodity DRAM (DDR5) is already a reality, adopted by Dell and HP at prices up to 10% below Korean supply, and Samsung Electronics carries more of that exposure. HBM is a 2027-2028 story at the earliest. Second, governance sits on the opposite side from pricing discipline. As a national strategic asset controlled by the city of Hefei and state funds, CXMT can keep expanding capacity even if prices roll over. If CXMT's profit is a function of price, then the moment its 2028 capacity landing coincides with a price downturn, the company could revert to a player expanding capacity at a loss, and that is the real tail risk for Korean memory. Third, even so, CXMT's existence has not broken prices within this cycle. An 8% share coexisting with double-digit price increases is this quarter's evidence. [Inference: original synthesis]

## 6. Kimi K3 and the Divergence in Frontier-Lab Profitability

Kimi K3, released by Moonshot AI on July 16, is the largest open-weight model to date: a 2.8 trillion-parameter MoE with a 1 million-token context window. On composite intelligence indices it landed just below (57) the top US frontier models (60, 59), took first place on some coding benchmarks, and prices its API at half to a third of the top US models. [Fact: benchmark aggregators, pricing pages] In the 72 hours after its release, roughly $470bn was wiped off US AI and semiconductor market caps, a conditioned reflex left over from the memory of DeepSeek.

This time, though, the narrative did not survive three days. The logic of the rebound is worth dwelling on. If the DeepSeek shock was a fear that efficiency would kill compute demand, K3 is not an efficiency model at all, it is a <strong>giant model</strong>. Self-hosting it requires at least 1.4TB of accelerator memory, which is why Bloomberg summed up the episode as "a memory story more than a compute story." Nvidia's Jensen Huang pushed back: "Wall Street misjudged the impact of Kimi again. Free AI is good for hardware, chips, and data centers." [Fact: press reports, interviews] The price evidence for that reinterpretation showed up the same day: Micron turned positive intraday on the day of the shock itself. The spread of open-weight models increases the total volume of inference, and the bottleneck in inference is memory. Evidence pointing the same way: Chinese-origin models account for 46% of processing volume on OpenRouter. Tokens do not check a passport before they consume memory.

The worry over frontier-lab profitability got its first two-sided evidence this season. On one side, Anthropic, with a run rate of $47bn (up from $9bn at the start of the year), moved onto a trajectory toward its first operating profit in Q2, with API margins estimated at 70-80%. On the other side, OpenAI told investors it posted Q1 revenue of $5.7bn against a net loss of $3.7bn and does not expect positive cash flow before 2030. [Fact: press reports, aggregated] In short, the claim that "frontier labs can't make money" is now false; the accurate claim is that "it depends on the frontier lab's business model." An enterprise-and-API-centered model can already be profitable, while carrying 900 million free consumer users structurally guarantees a loss. Indirect evidence from Microsoft's own books arrived this quarter too: its equity-method stake in OpenAI swung to a profit of $0.48bn (which, by the reading standard set in the previous piece, rejects the "widening losses" scenario), and separately it recognized a $3.2bn gain on its Anthropic investment. Even allowing for the noise of hypothetical-liquidation (HLBV) accounting, it is worth recording that both audited lines on the books pointed toward profit. [Fact: Microsoft earnings call]

## 7. Four Worries, Answered by Earnings

Here is the whole season laid out as an answer sheet to the four worries.

| Worry | What the earnings season measured | Verdict | Variables still open |
|---|---|---|---|
| Is AI token demand real | Google tokens up 7x in a year, Foundry customers using over 1 trillion tokens up 4x, growth accelerated at all three cloud majors, all four executives cited supply constraints | Evidence disproves the fear | Speed of per-token price decline, margin pressure on non-frontier providers |
| Are frontier labs making money | Anthropic on track for first operating profit in Q2, API margins of 70-80%, OpenAI not projected to profit until 2030, both of Microsoft's equity-method lines swung to profit | A fork in the road, the business model decides | OpenAI's IPO and fundraising, the compute cost curve |
| Capex ROI and semiconductor supply expansion | 95% pilot failure rate versus a $1.7tn backlog, the market has begun grading against quarterly proof, a third of 2027 spending projected to be debt-funded | The paradox persists, grading gets stricter | Whether revenue acceleration continues every quarter, credit spreads |
| Semiconductor profitability beyond 2028 | Five-year LTAs, 60-70% of capacity under contract, price floors, prepayments, statements that the supply shortfall "worsens in 2027 and persists through 2028," CXMT's 2028 roadmap of 500,000-600,000 wafers | Undecided, structure versus variable | CXMT's actual ramp, new fab landing timing, what AI demand looks like in 2028 |

[Inference: verdicts are original synthesis]

Only the fourth row needs elaboration. The reason profitability beyond 2028 is left undecided is that the evidence for both optimism and pessimism got stronger this season. On the optimistic side sits the structure the industry learned from 2018. Five-year LTAs, 60-70% of capacity under long-term contract, price floors, and upfront prepayments are all devices that use contracts to dampen the amplitude of the next downturn, and Samsung Electronics has formally stated that the supply shortfall "worsens in 2027 and persists through 2028." The physical lag of three and a half years from breaking ground on a new fab to volume production is also a defense on the supply side. On the pessimistic side sits a calendar problem: CXMT's expansion roadmap (500,000-600,000 wafers by 2028) lands in the same year as Korea's new fabs (Pyeongtaek P5 in the second half of 2028, Yongin Y2 in the second half of 2028). There is also pushback: Bank of America, among others, argues that SK Hynix's actual capacity delivery could come in at just a sixth of plan, so even the substance of the capacity expansion is contested. [Fact: respective institutions, earnings calls] This is not deferring the verdict; it means the material needed for a verdict arrives in sequence, starting with 2027 contract negotiations (forecasts of HBM prices doubling versus gridlock) and CXMT's next quarterly results.

Last, a watch list. Here, in chronological order, are the events that would update this piece's verdict.

| Timing | Event | What to check |
|---|---|---|
| Early August | SK Hynix expected to announce shareholder return policy | Size and form of the first return policy since the ADR listing |
| Mid-August | Both companies' quarterly reports | First confirmation of the absolute size of contract liabilities (prepayments) |
| Mid-September | FOMC (hike probability 61%) | Whether the hawkish cycle keeps executing, direction of the 30-year yield at 5.2% |
| Late September | Micron FY26 Q4 | Proof of the $50bn guidance, HBM4E progress |
| October | Q3 earnings season | Confirmation of the +13-18% server DRAM settlement, round two of capex grading |
| Late October | Microsoft FY27 Q1 | Proof of the 45% Azure guide, another look at the OpenAI equity-method line |
| Ongoing | CXMT quarterly disclosures | Whether the ASP-dependent profit structure holds up, HBM yield |

---

The names mentioned in this piece are illustrative examples for analysis and do not constitute a recommendation to buy or sell any specific security. Responsibility for investment decisions and their outcomes rests with the investor. Earnings figures are drawn from each company's filings, results releases, and earnings calls; share prices and quotes are based on press reports through intraday trading on July 31, 2026, and the July 31 figures for the KOSPI and Korea's two memory makers are intraday levels, not closing prices. SK Hynix's decline on its results day (roughly around 10%) and Samsung Electronics' reaction on July 30 are given as ranges because press reports vary. Some figures, such as Micron's gross margin, are based on aggregated press reports and may need to be checked against original disclosures. CXMT's capacity, yield, and market-share forecasts, and the combined hyperscaler capex figures, are areas where institutional estimates diverge widely, and Goldman Sachs's 2027-2028 profit forecasts for Korea's two memory makers represent a single institution's view. Backlog (RPO) figures are defined differently company by company, which limits the validity of simply adding them together. The verdicts and grading in this piece are calibration judgments, not statistical estimates.

### Related Posts

- [Rebound or Terminal? Eight Doubts, Seven Discriminators, and a 48-Hour Verdict](/post/ai-capex-eight-doubts-rebound-or-terminal-48hours-2026-07-29/)
- [Why Does NVIDIA Want to Be OpenAI's Guarantor? Anatomy of the $250 Billion Backstop](/post/nvidia-openai-250bn-backstop-anatomy-two-lenses-2026-07-29/)
- [Anatomy of Black Tuesday: Is China's DUV Mass-Production Report a Major Negative or Noise?](/post/china-duv-steelman-verdict-black-tuesday-korea-memory-2026-07-28/)
- [Cisco Did Not Die of Missing Demand: Rewriting the Dot-Com vs AI Comparison with the Monetization Gap Ratio](/post/cisco-analog-monetization-gap-ratio-1996-or-1999-2026-07-27/)
