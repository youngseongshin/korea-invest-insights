---
title: "The Second Week of August in Review: AI Capital Moves to Wall Street, and Good News Starts Lasting Two Days"
slug: "weekly-wrap-wallst-financing-reaction-shift-2026-08-14"
date: 2026-08-14T11:19:00+09:00
description: "Two things became official on a single day, August 10. The SEC excluded data center securitization bonds from asset-backed securities regulation, and NVIDIA announced a $500bn third-party capital platform with six partners ranging from Apollo to KKR. The shift of AI capital expenditure financing from corporate balance sheets to capital markets was confirmed on both the regulatory and structural fronts in one day. The same week, CoreWeave and Nebius demonstrated demand through earnings, SanDisk disclosed that multi-year contracts now cover two-thirds of its NAND shipments, and SK Hynix Chairman Chey Tae-won pulled out, on camera, a supply request that Jensen Huang had handwritten on a wafer. US inflation data broke the odds of a rate hike, and the KOSPI rose for four straight days. This piece reviews a week in which all three observation items left by the previous post were filled in, and lays out what remains unresolved."
categories: ["Exclusive Analysis", "Market-Outlook", "Macro-Analysis"]
tags:
  - "Weekly Wrap"
  - "NVIDIA"
  - "SEC"
  - "CoreWeave"
  - "Nebius"
  - "SanDisk"
  - "CPI"
  - "Yen"
  - "Oil Prices"
  - "Chey Tae-won"
  - "Samsung Electronics"
  - "SK Hynix"
  - "Korean Semiconductors"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Connected context: [A Rebound Won't Come From a Single Trigger: A Verdict Calendar From Late August to Year-End](/post/memory-rebound-triggers-stacking-calendar-2026-08-09/) left three things to confirm this week: the unit price direction in the August 11 preliminary export data, US inflation and Treasury auctions from the 12th through the 14th, and whether the market would produce its first case of rising for two straight days on good news. This piece grades those three boxes to close out the week, but puts one larger event first. On August 10, the shift of AI capital expenditure financing away from corporate hands and into capital markets became official on both the regulatory and structural fronts.

## TL;DR

- The biggest structural change this week came from two announcements on a single day, August 10. The SEC issued guidance that data center securitization bonds do not qualify as asset-backed securities, removing the risk retention requirement, and on the same day NVIDIA announced it was setting up an <strong>AI compute financing platform with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs, and KKR that mobilizes more than $500bn in third-party capital</strong>. [Fact: SEC guidance, NVIDIA announcement] The financing channel widened and the safety rules governing that channel thinned out at the same time.
- Neocloud earnings demonstrated demand. CoreWeave posted revenue of $2.58bn, up 112%, with backlog reaching roughly $129bn including new contracts, while Nebius grew 454% and turned EBITDA-positive, sending its stock up 28% in a day. [Fact: company disclosures] But <strong>CoreWeave's quarterly interest expense was $640mn, which annualizes to roughly half of last year's full-year revenue</strong>, and the credit market is pricing its five-year default probability at around 50%. Equity and credit have reached opposite verdicts.
- US July inflation cleared the gate. Consumer price growth slowed to 3.4% and the producer price headline came in flat. The <strong>odds of a September rate hike collapsed from 67% at the end of July to about 34%</strong>. [Fact: Bureau of Labor Statistics, market pricing] Ten-year and thirty-year Treasury auctions, conducted at the highest yields in 25 years, were also absorbed without difficulty. Still, core services inflation accelerated and oil climbed back into the $80s, leaving the August 26 PCE reading as the remaining gate.
- The backdrop to the oil rebound is Hormuz. The strait has not reopened, daily vessel transits remain a small fraction of normal levels, and the 60-day truce expiring August 17 has only an agreement in principle on an extension. [Fact: ship tracking, news reports] The yen gave back half of the joint-intervention effect and returned to the 159 range, but net short yen positions on the Chicago futures market have fallen by more than half from late June, so the pressure for a further unwind has itself eased.
- On the memory side, disclosure of contract structures moved forward a step. At its investor day, SanDisk revealed that <strong>multi-year contracts with eight customers cover half of fiscal 2027 shipments and two-thirds of fiscal 2028 shipments, with minimum revenue guarantees exceeding $42bn</strong>. [Fact: investor day materials] The shift from raising prices to locking prices in through contracts has produced its most explicit numbers yet, in NAND.
- SK Hynix Chairman Chey Tae-won gave CNBC its first look inside the Yongin cluster, showing a 1,023tn won expansion plan alongside <strong>a note Jensen Huang had handwritten on a wafer asking for more supply</strong>. [Fact: CNBC, August 13] In the same interview, he also said prices had risen too fast. Demand validation and a supplier's own wariness about the pace of price increases showed up together in a single interview.
- Korea's market saw its reaction function change. In the August 11 preliminary export data, semiconductors rose 155.4% to a record, and the KOSPI <strong>rose for four straight days from Monday through Thursday to close at 6,813.34</strong>, recovering the 7,000 level intraday on Friday morning for the first time in 15 trading days. Foreign investors turned net buyers for four straight days starting Tuesday. [Fact: Korea Customs Service, Korea Exchange] The "two straight days of gains on good news" that the previous post flagged as the earliest signal was observed for the first time this week.
- What remains unresolved is just as clear. NVIDIA earnings and PCE land on the same day, August 26, and shareholder returns from Samsung Electronics and SK Hynix, reported to total around 200tn won combined, are still awaiting formal announcement. Oil's rebound and CXMT becoming China's largest listed company by market cap just 17 days after its listing remain variables for the next stretch.

<div class="thesis-callout">
<div class="thesis-callout__label">Key Framing</div>

July's question was who would bear the cost of AI capital expenditure. August's second week answered that capital markets would bear it, and regulation widened that path. As money moves off corporate balance sheets and into securitized bonds and private credit, spending can be sustained for longer, but the people who hold the risk and the people who sell the risk start to separate. This week the stock market cheered demand confirmed by earnings, while the credit market kept default probabilities high for the same companies. One of the two has to be wrong, and that verdict will not arrive in this cycle, but in the next downturn. What this week leaves Korean investors is simpler. The demand and flow axis has turned, while the price and supply axis remains open.

</div>

## 1. Mapping the Week's Events

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 326" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="132" y1="20" x2="132" y2="282" stroke="var(--kii-chart-axis)" stroke-width="1.5"/>
<text x="116" y="30" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Mon 10 Aug</text>
<circle cx="132" cy="26" r="6" fill="var(--kii-cat-1)"/>
<circle cx="132" cy="26" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="30" fill="var(--card-text-color-main)" font-size="13" font-weight="600">SEC guidance, NVIDIA financing platforms</text>
<text x="152" y="48" fill="var(--card-text-color-tertiary)" font-size="11.5">ABS carve-out and the $500bn consortium on the same day</text>
<text x="116" y="84" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Tue 11 Aug</text>
<circle cx="132" cy="80" r="6" fill="var(--kii-cat-1)"/>
<circle cx="132" cy="80" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="84" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Korea export data, CoreWeave results</text>
<text x="152" y="102" fill="var(--card-text-color-tertiary)" font-size="11.5">semiconductors +155.4%, revenue +112%</text>
<text x="116" y="138" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Wed 12 Aug</text>
<circle cx="132" cy="134" r="6" fill="var(--kii-cat-1)"/>
<circle cx="132" cy="134" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="138" fill="var(--card-text-color-main)" font-size="13" font-weight="600">US CPI, Nebius results</text>
<text x="152" y="156" fill="var(--card-text-color-tertiary)" font-size="11.5">inflation eased to 3.4%, Nebius +28%</text>
<text x="116" y="192" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Thu 13 Aug</text>
<circle cx="132" cy="188" r="6" fill="var(--kii-cat-1)"/>
<circle cx="132" cy="188" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="192" fill="var(--card-text-color-main)" font-size="13" font-weight="600">PPI, SanDisk investor day, CNBC interview</text>
<text x="152" y="210" fill="var(--card-text-color-tertiary)" font-size="11.5">flat headline, NAND contracts disclosed, Yongin shown</text>
<text x="116" y="246" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">Fri 14 Aug</text>
<circle cx="132" cy="242" r="6" fill="var(--kii-cat-3)"/>
<circle cx="132" cy="242" r="9" fill="none" stroke="var(--kii-cat-3)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="246" fill="var(--card-text-color-main)" font-size="13" font-weight="600">KOSPI back above 7,000 intraday; US retail sales tonight</text>
<text x="152" y="264" fill="var(--card-text-color-tertiary)" font-size="11.5">first time in 15 sessions; retail sales still ahead</text>
</svg>
</div>
<figcaption><strong>The week in sequence.</strong> The funding-structure shift came Monday, demand proof Tuesday and Wednesday, and contract disclosure plus the inflation gate on Thursday.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Day | Event |
|---|---|
| Mon 10 Aug | SEC datacenter securitization guidance, NVIDIA $500bn financing platforms, TSMC July revenue |
| Tue 11 Aug | Korea export data (semiconductors +155.4%), CoreWeave results |
| Wed 12 Aug | US CPI at 3.4%, Nebius results |
| Thu 13 Aug | Flat PPI, SanDisk investor day, SK Hynix Chairman Chey Tae-won on CNBC |
| Fri 14 Aug | KOSPI back above 7,000 intraday; US retail sales due overnight |

</details>
</figure>

The density of this week only becomes clear when sorted by day. Monday brought the SEC guidance, the NVIDIA consortium, and TSMC's July revenue. Tuesday brought Korea's preliminary export data and CoreWeave's earnings. Wednesday combined US consumer prices with Nebius earnings, and Thursday combined producer prices, SanDisk's investor day, and SK Hynix Chairman Chey Tae-won's CNBC interview. US retail sales are due Friday night. This piece works through them in that order.

## 2. August 10's Double Announcement: Financing Becomes Institutionalized

The two announcements that came out on Monday were reported separately, but they are two sides of the same event.

Start with the regulatory side. In a response to an inquiry from the law firm Latham & Watkins, SEC staff determined that <strong>data center securitization bonds do not qualify as asset-backed securities (ABS)</strong>. The reasoning is that data centers are not financial assets that amortize over time the way mortgages or auto loans do. This determination lifts bond issuance backed by data center revenue out of the risk retention requirement (the rule that obliges issuers to keep part of the risk on their own books) and out of some disclosure obligations. [Fact: SEC guidance, August 10] JPMorgan expects annual issuance in this market to grow from $27bn last year to $30bn to $40bn, while Morgan Stanley estimates 2026 AI-related debt issuance at $250bn to $300bn and puts the funding gap from 2026 through 2028 at $1.5tn. [Fact: news reports]

On the same day, NVIDIA announced it would set up an AI compute infrastructure financing platform with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs, and KKR to mobilize more than $500bn in third-party capital. Goldman Sachs's description of its role captures the essence of the structure: <strong>building a credit market backed by NVIDIA compute</strong>. [Fact: NVIDIA and company announcements] The company clarified that the arrangement takes the form of a non-binding memorandum of understanding and will not appear directly as debt on NVIDIA's balance sheet. The stock fell 2.85% on announcement day, and its credit default swap (CDS) spread narrowed to 72bp before drifting back to 79.8bp. [Fact: market data]

Placed side by side, the two announcements form a clear picture. Vendor financing, the structure discussed at the end of July in which the seller props up the buyer's credit, moved to its next stage this week. Instead of the seller guaranteeing directly, <strong>long-term Wall Street capital now takes that place, and regulation reduced the friction in that channel</strong>. BofA described this as a shift away from vendor financing and judged that the capital risk now sits with the consortium rather than with NVIDIA. [Fact: analyst commentary]

Both sides of this shift need to be stated honestly. A wider funding base raises the sustainability of spending. Under last month's calculations, with hyperscaler spending already at 100% of operating cash flow, every incremental dollar has to pass through outside capital, and the door to that outside capital has now widened institutionally. On the other hand, the risk retention exemption lets issuers sell off all of the risk and walk away. The core lesson of the 2008 securitization crisis was to make issuers keep some of the risk, and that safeguard no longer applies to this asset class. The same week saw a move in the opposite direction on the insurance side: the NAIC is investigating life insurers' exposure to AI-related private credit and will require detailed disclosure starting at year-end. [Fact: news reports] In a landscape where securities regulation is widening and insurance regulation is tightening, capital flows toward the looser rules.

## 3. Neocloud Earnings: Equity Cheers, Credit Holds Back

The first users of the new financing channel turned in their report cards this week.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 212" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="197.8" y1="18" x2="197.8" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="197.8" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+0%</text>
<line x1="290.6" y1="18" x2="290.6" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="290.6" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+10%</text>
<line x1="383.4" y1="18" x2="383.4" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="383.4" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+20%</text>
<line x1="476.2" y1="18" x2="476.2" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="476.2" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+30%</text>
<text x="158" y="40.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Nebius</text>
<rect x="197.8" y="28.0" width="259.8" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="466.6" y="40.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+28.0%</text>
<text x="688.0" y="40.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">results, 12 Aug</text>
<text x="158" y="76.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">SanDisk</text>
<rect x="197.8" y="64.0" width="139.2" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="346.0" y="76.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+15.0%</text>
<text x="688.0" y="76.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">investor day, 13 Aug</text>
<text x="158" y="112.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">CoreWeave</text>
<rect x="197.8" y="100.0" width="125.3" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="332.1" y="112.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+13.5%</text>
<text x="688.0" y="112.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">12 Aug, day after results</text>
<text x="158" y="148.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">SK Hynix ADR</text>
<rect x="197.8" y="136.0" width="83.5" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="290.3" y="148.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+9.0%</text>
<text x="688.0" y="148.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">13 Aug</text>
<line x1="197.8" y1="18" x2="197.8" y2="162.0" stroke="var(--kii-chart-axis)" stroke-width="1.4"/>
<text x="337.0" y="204" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">Share moves on announcement day. CoreWeave shown for the session after its print</text>
</svg>
</div>
<figcaption><strong>Share moves on announcement day.</strong> Each set of results or contract disclosures produced roughly double-digit gains. CoreWeave reported after the close, so its move is the following session.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Name | Move | Trigger |
|---|---|---|
| Nebius | +28% | results, 12 Aug |
| SanDisk | +15% | investor day, 13 Aug |
| CoreWeave | +13.5% | results 11 Aug, next session |
| SK Hynix ADR | +9% | 13 Aug |

</details>
</figure>

CoreWeave reported revenue of $2.58bn on Tuesday, up 112%, and its stock rose double digits on Wednesday. Backlog reached roughly $129bn, combining $104bn in existing backlog with more than $25bn in new contracts signed in the first six weeks of the third quarter. It signed a new $21bn contract with Meta running through 2032 and a multi-year agreement with Anthropic. [Fact: company disclosures] Nebius reported revenue of $580mn on Wednesday, up 454%, along with a turn to positive EBITDA, and its stock rose 28% in a day. IREN announced its first system delivery to Microsoft on Thursday. [Fact: company disclosures, news reports]

As evidence of demand, these numbers are strong. But placing the same companies' debt figures alongside them produces a different picture. CoreWeave's quarterly interest expense was $640mn, 2.4 times what it was a year earlier, and annualizes to $2.56bn, half of last year's full-year revenue of $5.13bn. Total debt stands at $35bn, and annual capital expenditure guidance was raised to a range of $35bn to $39bn. The credit market's pricing of the company's CDS, around 850bp, <strong>implies a five-year default probability of roughly 50%</strong>. Concentration also remains unchanged, with more than 60% of revenue coming from Microsoft alone. [Fact: disclosures, news reports]

The stock market bought based on backlog and growth rates, while the credit market held its premium based on interest expense and concentration. This split did not narrow at any point this week. Which side is right will be decided not by demand but by interest rates and how contracts get renegotiated. That verdict will only arrive in the next downturn, when today's contracts come up for renewal. What can be confirmed right now is just one thing: as the new financing channel opens, these companies have room for their funding costs to fall, and CoreWeave itself said its weighted average cost of debt fell by 3 percentage points over the past year. [Fact: earnings call]

## 4. Macro: Hike Odds Collapsed, Oil Came Back

The previous post flagged this week's macro data as a gate, and the result was a pass, though the composition differed from what was expected.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="240.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">0%</text>
<line x1="60" y1="196.8" x2="676.0" y2="196.8" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="200.8" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">15%</text>
<line x1="60" y1="157.6" x2="676.0" y2="157.6" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="161.6" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">30%</text>
<line x1="60" y1="118.4" x2="676.0" y2="118.4" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="122.4" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">45%</text>
<line x1="60" y1="79.2" x2="676.0" y2="79.2" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="83.2" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">60%</text>
<line x1="60" y1="40.0" x2="676.0" y2="40.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="44.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">75%</text>
<rect x="98.5" y="61.0" width="77.0" height="175.0" rx="4" fill="var(--kii-cat-4)"/>
<text x="137.0" y="53.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">67%</text>
<text x="137.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">31 Jul</text>
<text x="137.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">after the FOMC</text>
<rect x="252.5" y="121.1" width="77.0" height="114.9" rx="4" fill="var(--kii-cat-3)"/>
<text x="291.0" y="113.1" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">44%</text>
<text x="291.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">7 Aug</text>
<text x="291.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">big jobs miss</text>
<rect x="406.5" y="105.4" width="77.0" height="130.6" rx="4" fill="var(--kii-cat-3)"/>
<text x="445.0" y="97.4" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">50%</text>
<text x="445.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">11 Aug</text>
<text x="445.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">before CPI</text>
<rect x="560.5" y="147.2" width="77.0" height="88.8" rx="4" fill="var(--kii-cat-1)"/>
<text x="599.0" y="139.2" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">34%</text>
<text x="599.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">13 Aug</text>
<text x="599.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">after CPI and PPI</text>
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="60" y="24" fill="var(--card-text-color-tertiary)" font-size="11.5">Probability of a September hike (%), approximate market pricing</text>
</svg>
</div>
<figcaption><strong>The collapse in September hike odds.</strong> A 67% probability at the end of July fell to 34% after the jobs miss and the inflation prints. Approximate market pricing.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Date | Hike probability | Trigger |
|---|---|---|
| 31 Jul | about 67% | after the FOMC |
| 7 Aug | about 44% | big jobs miss |
| 11 Aug | about 50% | before CPI |
| 13 Aug | about 34% | after CPI and PPI |

</details>
</figure>

July consumer prices, released Wednesday, rose 0.1% month over month and 3.4% year over year, down from June's 3.5%, with the core reading also easing to 2.5%. Both matched consensus. Thursday's producer price headline came in flat, below the expected 0.2%. The odds of a September rate hike, which had fallen from 67% at the end of July to 44% after the jobs shock, <strong>collapsed further to about 34%</strong> as this week's inflation data came in. [Fact: Bureau of Labor Statistics, market pricing] Treasury auctions were also a gate: the ten-year sold at 4.683%, the highest since the financial crisis, and the thirty-year at 5.216%, the highest since 2001, yet demand held up well. This confirms that while yield levels are high, supply is not going unabsorbed. [Fact: Treasury Department, news reports]

Two caveats belong alongside this. First, core services in the producer price report actually accelerated, rising 0.4%, driven largely by a 6.5% jump in portfolio management fees, which track equity prices. The Fed's preferred inflation gauge, PCE, arrives August 26, the same day as NVIDIA's earnings. Second, <strong>oil came back</strong>. WTI, which had fallen to the $74 range on August 5, rose for six straight trading days into the $83 range this week before finally pulling back on Thursday. The trigger for that pullback was not the truce but the largest US crude inventory build since early 2023. [Fact: Energy Information Administration, market data]

Oil rose because Hormuz never reopened. Strait transits, which used to run dozens of vessels a day, fell to single digits. War-risk insurance premiums remain stuck at roughly 30 times normal levels. The extension of the 60-day truce expiring August 17 remains at the stage of an agreement in principle. [Fact: ship tracking, news reports] In short, the path that unlocked this week's macro gate was not oil stabilizing but a cooling labor market and inflation matching expectations. The oil axis remains an open variable.

The yen gave back half of the joint-intervention effect. The dollar-yen rate, which stood at 156.8 yen on August 3, returned to the 159.5 yen range and is testing 160 yen. There was no further intervention, and Japanese and US authorities only repeated that they stood ready. Still, leveraged funds' net short yen positions on the Chicago futures market fell by more than half, from 138,000 contracts at the end of June to 64,000. [Fact: market data, CFTC] Yen weakness itself has returned, but with fewer positions left to unwind, the fuel for an August 2024-style chain-reaction unwind has actually diminished. The won appreciated to the 1,417 range, up nearly 5% in a month.

## 5. Memory: Contract Disclosures and a Supplier's Own Words

The most important document on the memory side this week was SanDisk's investor day material, released Thursday. Last week, this company's disappointing guidance triggered the August 6 plunge in Korean memory stocks; the detailed materials that arrived a week later pointed in the opposite direction. SanDisk projected the NAND market growing from $300bn in 2026 to more than $500bn in 2027, and expects the supply shortage to persist through 2028. Most notably, it disclosed that <strong>multi-year contracts with eight customers cover half of fiscal 2027 shipments and two-thirds of fiscal 2028 shipments, with total minimum revenue guarantees exceeding $42bn</strong>. It set a long-term target of sustaining gross margin around 80%. The stock rose 15%, and SK Hynix's US-listed shares and Micron rose alongside it, by 8% and more than 5% respectively. [Fact: investor day materials, market data]

The significance of this disclosure goes beyond any single company. As covered in early August, the investment question for this cycle has shifted from whether prices will rise further to whether they will hold, and the strongest basis for holding is contracts. SanDisk's materials are the first case of that shift toward contracts appearing in NAND as the most explicit numbers yet. Two-thirds of shipments being covered means the amplitude of the next downturn is being suppressed by contract. In DRAM, reports continued that third-quarter contract negotiations have been pushed into August, with suppliers and buyers still at a standoff. [Fact: industry reports]

The same Thursday brought SK Hynix Chairman Chey Tae-won's CNBC interview. CNBC filmed inside the Yongin cluster for the first time, revealing a plan to triple production capacity by 2034 at a cost of 1,023tn won, along with the Yongin Fab 1, set to begin operation in February 2027. In the interview, he compared the current situation to a war, saying everyone wants to buy memory, and pulled out <strong>a note Jensen Huang had handwritten on a wafer asking for more supply</strong>. He also disclosed an anecdote in which NVIDIA asked to move up HBM4 supply by six months and CEO Kwak Noh-jung answered that he would try, along with the customization trend in which both NVIDIA and Google each want their own tailored HBM. [Fact: CNBC, domestic news reports, August 13]

The same interview also contained a sentence in a different register. He said <strong>prices had risen too fast</strong>. This was a supplier voicing its own wariness about the pace of prices, and it reflects exactly the same concern covered in early August: that buyers' capacity to pay is nearing its limit and the largest demand source is turning to designs that use less memory. Demand is strong enough to be compared to a war, and even the supplier finds the pace of price increases uncomfortable. These two sentences coexisting is the precise coordinate of the memory cycle right now.

The surrounding data points the same way. Micron's market capitalization climbed back above $1tn, and its chief business officer said 2027 will be tighter than 2026 and will not fill even half of data center demand. TSMC's July revenue rose 44.7% year over year. CXMT overtook Tencent to become China's largest listed company by market cap just 17 days after its listing. [Fact: company reports, news reports] That last item is not evidence of demand but a supply variable for the next stretch, and the fact that China's capital markets are pricing memory far more generously than Korea's is itself worth noting.

## 6. Korea: Grading Week One of the Verdict Calendar

The three observation items left by the previous post are graded here against this week's actual data.

First, the direction of export unit prices. In Tuesday's Korea Customs Service preliminary data, total exports for August 1 through 10 came to $21.3bn, up 45.3%, the highest on record for that ten-day period, and <strong>semiconductors came to $9.95bn, up 155.4%, accounting for 46.8% of total exports</strong>. The computer category, which carries AI-bound SSDs, also rose 139.5%. [Fact: Korea Customs Service] July's month-over-month decline turned into reacceleration in early August. Pass.

Second, the macro gate. As shown above, inflation matched expectations, hike odds collapsed, and the auctions were absorbed. A pass, with the caveats of oil's renewed rise and accelerating core services.

Third, the reaction function. This is the real story of the week.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 248" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="228.3" y1="18" x2="228.3" y2="198.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="228.3" y="216.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+0%</text>
<line x1="342.1" y1="18" x2="342.1" y2="198.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="342.1" y="216.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+2%</text>
<line x1="455.9" y1="18" x2="455.9" y2="198.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="455.9" y="216.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+4%</text>
<text x="148" y="40.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Mon 10 Aug</text>
<rect x="228.3" y="28.0" width="37.0" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="274.3" y="40.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+0.65%</text>
<text x="688.0" y="40.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">KOSDAQ led</text>
<text x="148" y="76.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Tue 11 Aug</text>
<rect x="228.3" y="64.0" width="41.5" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="278.8" y="76.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+0.73%</text>
<text x="688.0" y="76.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">export data</text>
<text x="148" y="112.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Wed 12 Aug</text>
<rect x="228.3" y="100.0" width="209.4" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="446.7" y="112.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+3.68%</text>
<text x="688.0" y="112.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">Temasek report</text>
<text x="148" y="148.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Thu 13 Aug</text>
<rect x="228.3" y="136.0" width="202.6" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="439.8" y="148.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+3.56%</text>
<text x="688.0" y="148.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">US inflation eased</text>
<text x="148" y="184.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Fri 14 Aug am</text>
<rect x="228.3" y="172.0" width="152.5" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="389.8" y="184.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+2.68%</text>
<text x="688.0" y="184.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">back above 7,000 intraday</text>
<line x1="228.3" y1="18" x2="228.3" y2="198.0" stroke="var(--kii-chart-axis)" stroke-width="1.4"/>
<text x="325.0" y="240" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">KOSPI daily change. Friday shows the morning session</text>
</svg>
</div>
<figcaption><strong>Five sessions of the KOSPI.</strong> Four consecutive up days from Monday, and back above 7,000 intraday on Friday morning for the first time in 15 sessions.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Date | Change | Main driver |
|---|---|---|
| 10 Aug | +0.65% | KOSDAQ led |
| 11 Aug | +0.73% | export data |
| 12 Aug | +3.68% | Temasek report |
| 13 Aug | +3.56% | US inflation eased |
| 14 Aug am | up 2%+ | above 7,000 intraday |

</details>
</figure>

The KOSPI's daily path ran as follows: up 0.65% Monday, 0.73% Tuesday, 3.68% Wednesday, and 3.56% Thursday, closing at 6,813.34, then opening up more than 2% on Friday morning and climbing intraday to 7,010.86, recovering the 7,000 level for the first time in 15 trading days. That is roughly 22% above the July 30 low. Wednesday's surge was attributed to reports that Singapore's sovereign wealth fund Temasek is considering direct investment in Samsung Electronics and SK Hynix, while Thursday was driven by the US inflation slowdown. SK Hynix rose 5.54% Wednesday and 5.92% Thursday, gaining more than 5% for two straight days, and Samsung Electronics climbed to 268,000 won. [Fact: Korea Exchange, news reports]

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 248" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="171.7" y1="18" x2="171.7" y2="198.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="171.7" y="216.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">-2</text>
<line x1="230.3" y1="18" x2="230.3" y2="198.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="230.3" y="216.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">-1</text>
<line x1="289.0" y1="18" x2="289.0" y2="198.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="289.0" y="216.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+0</text>
<line x1="347.6" y1="18" x2="347.6" y2="198.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="347.6" y="216.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+1</text>
<line x1="406.2" y1="18" x2="406.2" y2="198.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="406.2" y="216.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+2</text>
<line x1="464.8" y1="18" x2="464.8" y2="198.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="464.8" y="216.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+3</text>
<text x="148" y="40.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Mon 10 Aug</text>
<rect x="201.6" y="28.0" width="87.3" height="16" rx="4" fill="var(--kii-cat-4)"/>
<text x="192.6" y="40.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="end">-1.49</text>
<text x="688.0" y="40.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">net selling</text>
<text x="148" y="76.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Tue 11 Aug</text>
<rect x="289.0" y="64.0" width="2.9" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="300.9" y="76.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+0.05</text>
<text x="688.0" y="76.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">the turn</text>
<text x="148" y="112.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Wed 12 Aug</text>
<rect x="289.0" y="100.0" width="166.5" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="464.4" y="112.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+2.84</text>
<text x="688.0" y="112.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">largest of the rebound</text>
<text x="148" y="148.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Thu 13 Aug</text>
<rect x="289.0" y="136.0" width="143.6" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="441.6" y="148.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+2.45</text>
<text x="688.0" y="148.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">third day</text>
<text x="148" y="184.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">Fri 14 Aug am</text>
<rect x="289.0" y="172.0" width="25.2" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="323.2" y="184.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+0.43</text>
<text x="688.0" y="184.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">fourth day</text>
<line x1="289.0" y1="18" x2="289.0" y2="198.0" stroke="var(--kii-chart-axis)" stroke-width="1.4"/>
<text x="330.0" y="240" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">Foreign net buying on KOSPI (tn won). Friday shows the morning tally</text>
</svg>
</div>
<figcaption><strong>The foreign return.</strong> After Monday's net selling, four consecutive days of net buying. The July pattern of selling the two memory names reversed this week.</figcaption>
<details class="kii-figure__table"><summary>View as table</summary>

| Date | Foreign net buying |
|---|---|
| 10 Aug | -1.4887tn won |
| 11 Aug | +45bn won |
| 12 Aug | +2.8357tn won |
| 13 Aug | +2.4525tn won |
| 14 Aug am | +434.3bn won |

</details>
</figure>

Fund flows also changed direction. Foreign investors net sold 1.4887tn won on Monday but <strong>turned net buyers for four straight days from Tuesday through Friday morning</strong>, with Wednesday's 2.8357tn won and Thursday's 2.4525tn won the largest single-day amounts of this rebound. Retail investors net sold more than 3tn won each on Wednesday and Thursday, taking profits. Foreign investors, who had sold more than 11tn won of the two memory makers alone in July, turned into net buyers this week. [Fact: Korea Exchange data]

The previous post pointed to <strong>the first case of a two-day rally on good news</strong>, rather than a checklist of triggers, as the earliest leading signal. This week delivered not two days but four, and a fifth by Friday morning. The asymmetry that held throughout July, in which good news lasted a day and bad news lasted three, inverted for the first time this week. This is not news itself but a change in how the market digests news, meaning one necessary condition for a trend reversal has now been filled by actual data. A sense of scale should still be kept in mind: the KOSPI's all-time high was 9,114.55 at the June 22 close, and the recovery of the 7,000 level is still 23% below that peak.

What remains unresolved is listed below in chronological order.

| Timing | Open item | What to watch |
|---|---|---|
| Aug 14 (night) | US July retail sales | Pace of the consumption slowdown. If too weak, sentiment could flip toward recession fears |
| Aug 17 | US-Iran 60-day truce expires | Whether an extension is signed. A breakdown reignites the oil axis |
| Aug 21 | Aug 1-20 preliminary exports | Whether the early-month surge continues |
| Aug 26 | NVIDIA earnings and US PCE, same day | Next-quarter guidance, customer concentration, core inflation |
| Late Aug (expected) | Samsung Electronics, SK Hynix shareholder returns | Substance behind the combined 200tn won reports. Buyback/cancellation and its relation to expansion |
| Ongoing | DRAM Q3 contract negotiations | Settlement level of the delayed talks, versus the 13-18% outlook |

[Fact: schedule, news reports; the scale of shareholder returns is media speculation]

One line should be added to the shareholder returns item. This week, domestic media reported that the two companies' combined returns could exceed 200tn won and could be announced as early as late August. [Fact: news reports, unconfirmed by the companies] As noted in the previous post, the force of these returns depends not on the amount but on whether it reads as a signal of supply discipline. If the return plan arrives just a week after SK Hynix announced its $38bn expansion, the market will read it not just for the amount but for what it signals about capital allocation priorities.

## 7. Implications: What Closed and What Remains Open

Summing up the week, two of the four axes moved toward closing, and two remained open.

The closing side is demand and fund flows. On demand, every piece of hard data released this week, from neocloud earnings to preliminary export figures to Micron's and TSMC's numbers to the handwritten note on a wafer, pointed in the same direction. Fund flows were confirmed by the KOSPI's four straight days of gains, the return of foreign investors, and the reversal of the reaction asymmetry. The two axes that drove July's decline turned in the opposite direction in the second week of August.

The open side is price and supply. On the price axis, DRAM's third-quarter contract negotiations remain delayed. A supplier itself voiced caution about the pace of price increases, and SanDisk's contract disclosures are grounds for holding prices, not for further increases. The supply axis stands as follows. With CXMT now China's largest company by market cap, its capacity to raise expansion funding has become effectively unlimited. SK Hynix's $38bn expansion and Samsung's Pyeongtaek schedule both remain on the calendar for 2027 and beyond. And the new financing channel opened this week, the expansion of securitization and private credit, raises the sustainability of demand while also lowering the threshold for funding on the supply side. Fabs get built through the same channel.

So the assessment of the KOSPI and Korean memory comes down to this. The first leg of the rebound was confirmed this week. Macro provided a floor, the reaction function turned, and even after the rebound, valuations sit at 3.7x for Samsung Electronics and 3.2x for SK Hynix on estimated 2027 earnings. [Fact: domestic brokerage compilation, based on estimates] The next leg will be decided by NVIDIA's guidance on August 26 and by the shareholder return announcements expected around that date. The distinction drawn in the previous post still holds: the first leg alone is a technical rebound, and only the next leg makes it a trend. What this week changed is the probability attached to that distinction. After four straight days of gains, the market is digesting the same news differently than it was a month ago.

---

Stocks mentioned in this piece are illustrative examples for analysis and do not constitute a recommendation to buy or sell any specific security. Responsibility for investment decisions and their outcomes rests with the investor. NVIDIA's financing platform remains at the non-binding memorandum-of-understanding stage, and its detailed structure has not been disclosed. CoreWeave's default probability figure is an approximate conversion from credit default swap pricing and differs from an actual default forecast. The 200tn won shareholder return figure is media speculation and has not been confirmed by either company. Oil prices, exchange rates, and strait transit volumes vary by source and are recorded as approximations; because reports vary on SK Hynix's US-listed share gain on August 13 (6 to 9%) and Samsung Electronics's move (3.7 to 4.9%), only closing prices are treated as confirmed figures. Retail sales, released Thursday night Korean time on August 14, are not reflected in this piece. Verdicts and grading here are judgment, not statistical estimation. Prices and indicators are as of August 13, 2026 (US) and the morning of August 14 (Korea).

### Related Posts

- [A Rebound Won't Come From a Single Trigger: A Verdict Calendar From Late August to Year-End](/post/memory-rebound-triggers-stacking-calendar-2026-08-09/)
- [What Hyperscaler Earnings Proved, and What They Didn't: Three Explanations for the Memory Sell-Off](/post/hyperscaler-proof-memory-selling-three-hypotheses-2026-08-04/)
- [Memory No Longer Needs Prices to Rise Further: Anatomy of the August 3 Plunge and the Contract Price Deceleration](/post/memory-price-deceleration-p-holds-thesis-2026-08-03/)
- [Why Does NVIDIA Want to Be OpenAI's Guarantor? Anatomy of the $250 Billion Backstop](/post/nvidia-openai-250bn-backstop-anatomy-two-lenses-2026-07-29/)
