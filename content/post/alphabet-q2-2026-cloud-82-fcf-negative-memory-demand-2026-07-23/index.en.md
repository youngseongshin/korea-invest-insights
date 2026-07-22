---
title: "Alphabet's Q2: Cloud +82% Ends the Demand Debate, Negative FCF Starts the Cash Debate"
slug: "alphabet-q2-2026-cloud-82-fcf-negative-memory-demand-2026-07-23"
date: 2026-07-23T11:00:00+09:00
description: "Alphabet's Q2 sharply lowered the odds of a post-2028 AI demand cliff: Cloud grew 82%, backlog reached $514bn, and existing customers are consuming 50% above their commitments. The same print delivered the first negative quarterly FCF on record, a 2026 CAPEX guide raised to up to $205bn, and Alphabet renting compute from SpaceX at roughly $920M a month because its own capacity ran out. We read the end of the demand debate and the start of the cash debate in one print, translate it into HBM, server DRAM and eSSD, and set up the Microsoft and Amazon scorecards for late July."
categories: ["Exclusive Analysis", "Company-Analysis", "Market-Outlook"]
tags: ["Alphabet", "Google Cloud", "AI CAPEX", "TPU", "HBM", "Server DRAM", "AI Memory", "FCF", "Backlog", "Big Tech Earnings", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Context: [Who Burns All Those Tokens?](/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/) argued that final demand, the last weak link in the AI CAPEX debate, had started to get real numbers attached to it, and left the verdict to the earnings season around July 30. The first scorecard arrived earlier than scheduled. Alphabet reported Q2 results in the early hours of July 23 Korea time. This piece synthesizes two analysis notes that dissected the same print from different angles into one. The short version: the demand side of the debate is effectively over, and the debate has moved on to cash flow and return on capital.

## TL;DR

- Cloud revenue came in at $24.8bn, <strong>+82%</strong> (vs. consensus +64%), marking five straight quarters of accelerating growth: 32%, 34%, 48%, 63%, 82%. Backlog rose from $462bn to <strong>$514bn</strong>, a net increase of $52bn even as revenue recognition accelerated.
- Demand quality matters more. Existing Cloud customers are consuming on average <strong>50%+ above their initial commitments</strong>, and Gemini model API throughput hit 22bn tokens per minute, up 37.5% in a single quarter. With supply running short, Alphabet started, from June, <strong>paying SpaceX roughly $920M a month</strong> for AI compute. It is an unprecedented sight: a hyperscaler turning into a net buyer of compute.
- On the flip side of the same print, quarterly FCF turned <strong>negative for the first time ever, at -$5.9bn</strong>. CAPEX of $44.9bn outran operating cash flow of $39.1bn, and 2026 CAPEX guidance was raised again from $180-190bn to <strong>$195-205bn</strong>, with a large further increase flagged for 2027.
- The judgment splits three ways. The odds of a post-2028 AI demand cliff have fallen further. Alphabet's FCF turnaround has been pushed out from 2027 into the 2028-2029 window. For memory, volume demand strength was reconfirmed, but the durability of pricing and peak margins remains a separate question.
- We hold the 45/35/20 demand-scenario probabilities. But another strand of hard evidence has piled up in support of the 35% upside case, and the early-CAPEX-deceleration premise central to the 20% downside case was weakened by this print. The next scorecards are Microsoft (July 30 KST) and Amazon (July 31).

<div class="thesis-callout">
<div class="thesis-callout__label">Key Framing</div>

Cloud +82% and the first-ever negative quarterly FCF are two sides of the same print. Asked whether the demand is real, Alphabet answered with usage that exceeds commitments and with the act of paying a premium to rent someone else's servers. What arrived sooner than expected, in exchange, was the bill for serving that demand. The market's scoring criterion has now shifted from whether demand exists to the cash return after depreciation, and for memory investors this print is reinforcement for volume, not a warranty on margin.

</div>

## 1. The Numbers First: What Came Out

| Item | Q2 2026 Actual | Comparison Basis | Verdict |
|---|---|---|---|
| Total revenue | $119.8bn, +24% | Consensus ~$116.9bn | Beat |
| Google Cloud revenue | $24.8bn, +82% | Consensus $22.4bn, +64% | Large beat |
| Cloud operating income | $8.8bn (35.6% margin) | Prior year $2.8bn (20.7% margin) | Improved |
| Search revenue | $63.3bn, +17% | Consensus $63.4bn | In line |
| Total operating income | $40.8bn, +30% (34.0% margin) | Margin below consensus | Mixed |
| Adjusted EPS | ~$2.85 | Consensus ~$2.89 | Slight miss |
| Operating cash flow | $39.1bn | CAPEX $44.9bn | Reversed |
| Quarterly FCF | -$5.9bn | Prior quarter $10.1bn | First negative ever |
| Cloud backlog | $514bn | Prior quarter $462bn | +$52bn |
| 2026 CAPEX guidance | $195-205bn | Prior $180-190bn | Raised again |

[Fact: Alphabet disclosures and earnings call]

The GAAP numbers carry an optical illusion. Reported GAAP EPS was $9.11 and net income was $112.1bn, up 298% year over year, but that includes roughly $99bn (pre-tax; about $6.26 per share after tax) of unrealized gains on private stakes such as Anthropic and SpaceX. Strip out this operationally unrelated item and the underlying EPS was about $2.85, a slight miss versus market expectations. Revenue and Cloud won big, but the quality of earnings was not as strong as the headline number suggests. [Fact: recalculated from disclosures]

## 2. The Demand Debate: Why We Think It's Effectively Over

The previous piece flagged final demand as the weak link and cited Codex's three million in three days as the first hard data point. Alphabet's print adds four more strands of hard evidence on top of that.

<strong>Usage is running ahead of contracts.</strong> Gemini model API throughput rose from 16bn to 22bn tokens per minute, up 37.5% in one quarter, and monthly developers passed 9M. Existing Cloud customers are consuming on average 50%+ above their initial commitments, and the overage widened from the prior quarter. New-customer acquisition is running at twice last year's pace, and Marketplace transaction volume is up sevenfold. [Fact: CEO letter and earnings call] The hypothesis that demand rests solely on a handful of long-term frontier-lab contracts is not compatible with data showing post-contract actual consumption exceeding commitments.

<strong>The demand base has broadened.</strong> Alongside model-development demand such as large-scale Gemini 4 pretraining, the company laid out five channels at once: enterprise inference in finance, pharma, retail, telecom and manufacturing; BigQuery and security workloads; consumer services such as Search's AI Mode and the Gemini app; and outright sales of TPU systems supplied directly into customer data centers. About 90% of the Fortune 100 now use Gemini Enterprise, more than 500 Cloud customers process over 1tn tokens a year, and over 2,000 exceed 100bn tokens. [Fact: CEO letter]

<strong>Supply is still capping growth.</strong> The CFO stated flatly that the company remains in a supply-constrained environment. To fill near-term shortfalls, Alphabet is leasing third-party data center capacity at elevated prices, and management said roughly six months of inefficiency is worth accepting to win large customers. That is the backdrop for the biggest news of the call: from June, Alphabet has been paying SpaceX roughly $920M a month, about $11bn annualized, to rent AI compute. [Fact: earnings call and press] That the most calculating company in the world is paying a premium to rent someone else's servers is behavioral evidence that runs directly counter to the demand-overstatement hypothesis.

<strong>Backlog grew even while being recognized.</strong> Cloud revenue rose about 23.8% quarter over quarter, meaning large contracts are converting into revenue quickly, and yet the backlog balance still grew by another $52bn. The current backlog is about 5.2x annualized Q2 Cloud revenue, and the company said more than half will be recognized within 24 months. [Fact: disclosures and earnings call] As visibility through 2027, that is strong evidence. Customer concentration and the year-by-year recognition amounts beyond 2028, however, were not disclosed. [Blocked: backlog detail undisclosed]

The efficiency counter-argument also lost force this quarter. AI Mode's cost per response has fallen to its lowest level since launch, yet users and query volume grew even faster. AI Mode has 1bn monthly users, and the Gemini app has 950M MAU. The relationship where usage growth outruns the decline in per-unit cost has now been confirmed at Alphabet's scale too, running in the same direction as the Jevons pattern observed with Codex. [Inference: efficiency-usage relationship]

## 3. The Cash Debate: The Bill Arrived Sooner Than Expected

On the other side of the demand story, what this print confirmed is the scale and duration of spending.

Q2 CAPEX of $44.9bn, double the year-ago level, exceeded operating cash flow of $39.1bn, and quarterly capital intensity (CAPEX/OCF) came in at about 115%. The arithmetic is heavy too. With H1 CAPEX at roughly $80.6bn, hitting the top of the annual guidance range of $205bn requires an H2 quarterly average of $57.2-62.2bn, 27-38% above Q2. A meaningful FCF recovery in H2 2026 or in 2027 is unlikely. [Inference: own arithmetic]

There was a hint on 2027 as well. The CFO maintained guidance that 2027 CAPEX will rise sharply, and the market consensus sits at about $257bn. The path from $205bn to $257bn works out to roughly +25% growth. That places the company on a deceleration path, from about +76% this year to +25% next year, not yet a re-acceleration scenario toward the $300bn level. [Fact: earnings call and consensus] This distinction matters. On a deceleration path, the skeleton of the FCF-turnaround thesis stays intact; on a re-acceleration path, the skeleton itself collapses.

Running a 2028 sensitivity in advance sharpens the judgment criteria. The starting point is the current trailing-12-month operating cash flow of $185.7bn.

| 2028 CAPEX Assumption | OCF Needed for FCF = $0 | Required OCF CAGR | OCF Needed for FCF = $50bn | Required Growth |
|---|---|---|---|---|
| $200bn | $200bn | ~3.8% | $250bn | ~16.0% |
| $230bn | $230bn | ~11.3% | $280bn | ~22.8% |
| $250bn | $250bn | ~16.0% | $300bn | ~27.1% |

[Inference: own sensitivity, not company guidance]

If CAPEX stabilizes around $200bn in 2028, an FCF recovery is not difficult. If it keeps rising to $230-250bn, combined Cloud-and-Search operating cash flow needs to grow more than 20% a year to get back to prior FCF levels. That is not an impossible number if Cloud's +82% growth and 35.6% margin hold up for a while, but depreciation, power costs, external lease payments, and a sales mix increasingly weighted toward lower-margin TPU hardware all push in the opposite direction.

A shift in the capital-allocation regime was also formalized this quarter. With $242.5bn in cash and marketable securities and $185.7bn in trailing-12-month operating cash flow, Alphabet's ability to pay is not in question. But in Q2 it raised about $30.5bn in common equity and about $19.1bn in convertible preferred stock and added about $21.1bn in net debt, while buying back no stock at all. Debt rose from about $16bn to about $100bn in twelve months. [Fact: disclosures] A company that once covered both CAPEX and buybacks entirely from operating cash flow has become one that has paused buybacks for the sake of CAPEX and is now tapping debt and equity capital as well. This is not a liquidity-risk signal but a signal that the capital-allocation regime has changed, and the fact that the weight of the funding sits more with shareholders than with the credit market is the comforting part from a credit perspective.

## 4. Scoring the Three Questions

Scoring the three questions against this print comes out as follows.

<strong>Does AI demand hold up beyond 2028? The odds of a cliff have fallen further.</strong> Demand is broadening from training into inference, data, security and enterprise workflows; actual consumption is exceeding commitments; usage growth is outrunning efficiency gains; most TPU external-sales revenue is scheduled to be recognized in 2027; and supply is still short enough that CAPEX must rise sharply again in 2027. The more accurate way to read 2028 is not as the point where demand ends, but as the point where new supply capacity comes fully online and goes on trial.

<strong>Will Alphabet's FCF turn around? Yes, but the timing has slipped.</strong> The quarterly FCF crossover arrived sooner than originally expected (early 2027), but even an optimistic 2027 operating-cash-flow estimate of $230-240bn is still FCF-negative for the full year against $257bn of CAPEX. A return to positive FCF requires 2028, and even then only if 2028 CAPEX growth slows to a single digit. A strong FCF re-acceleration is a conditional scenario confined to the 2028-2029 window.

<strong>Does this translate into sustained memory purchasing? Strongly positive for volume, neutral for price and margin.</strong> We unpack this in the next section.

## 5. Translating to Memory: Reinforcement for Volume, Not a Warranty on Margin

In Q2, about 60% of technical infrastructure CAPEX went to servers and 40% to data centers and networking. Server spend bundles together TPUs, GPUs, CPUs, HBM, server DRAM, SSDs and networking silicon. [Fact: earnings call]

The items supporting HBM demand are clear-cut: the new TPU generation and the rollout of NVIDIA Vera Rubin, large-scale Gemini 4 pretraining, growing enterprise inference volume, the next-generation network fabric tying together a 1M-accelerator network, and TPU system sales to outside customers, most of which will be recognized starting in 2027. What matters is that even where in-house TPUs partly displace NVIDIA GPUs, HBM demand does not disappear, it simply shifts purchasing channels from the GPU supply chain to the TPU-system supply chain. Add third-party compute leasing on top of that, and HBM and server DRAM demand now flows through three channels: Alphabet's own data centers, TPU external sales, and leased compute. [Inference: demand-channel decomposition]

The case for server DRAM and eSSD also got thicker with this print. AI agents don't run on accelerators alone; CPU servers handle preprocessing, state management, security and orchestration. Alphabet highlighted its Axion CPU alongside growing data and security workloads. The figure of 500 Cloud customers processing over 1tn tokens a year shows that storage demand flowing into logs, checkpoints, search indices and vector databases is not confined to training. [Fact: CEO letter] This confirms, via big-tech earnings, the demand-side backdrop for the server DRAM re-tightening covered in the previous piece (Q3 contract prices forecast +13-18%, lead times of 40 weeks).

Even so, this print alone is not grounds for raising memory companies' 2028 earnings estimates. Just as equipment purchases are surging, memory supply capacity is also set to grow over 2027-2029. Broader in-house chip adoption weakens NVIDIA's pricing power at the system level, inference cost per response keeps falling fast, and once Alphabet starts tightening CAPEX efficiency, downward price pressure on components will flow down the supply chain. The high prices of HBM4 and next-generation HBM embed early-generation scarcity and a yield premium that are not permanent values. Putting it together looks like this.

| Item | Pre-Earnings View | Post-Earnings View |
|---|---|---|
| AI accelerator / HBM bit demand | High | Very high |
| Server DRAM / eSSD demand | Medium-high | High |
| Advanced packaging / networking | High | Very high |
| 2028 demand cliff | Low probability | Lower probability |
| Memory ASP durability | Uncertain | Uncertain |
| Memory peak-margin durability | Low | Low |
| Early big-tech FCF recovery | Medium | Lower |
| Incremental return on CAPEX | Unproven | Partially proven, verification ongoing |

[Inference: overall judgment]

The 2028 risk for semiconductors is not order cancellations but the normalization of ASP and margin. That is consistent with the 45/35/20 demand-scenario probabilities. This print added one more piece of hard evidence to the 35% upside case and weakened the early-big-tech-CAPEX-deceleration premise behind the 20% downside case. We will update the probabilities themselves once Microsoft and Amazon are also confirmed. From the perspective of Samsung Electronics and SK Hynix, this is a print that improves the demand backdrop heading into the 2027-vintage HBM pricing negotiations that begin in Q4.

## 6. The Stock Reaction, and Where the Two Notes Diverge

The market reaction summarizes the character of this moment. In after-hours trading, the stock opened down about 2%, briefly recovered to a modest gain, then reversed again once CAPEX guidance was raised on the call, with the decline widening to a 3-5% range. As of the morning of the 23rd Korea time, the share price sat around $342, about 1.5% below the prior close of roughly $347. [Fact: market data] In a market where beating estimates has become the baseline, the 2026 rule that CAPEX decides the reaction played out for a fifth time. Read the other way, the fact that the decline stayed this contained in the face of +82% growth is also a signal that the market will digest the spending as long as the growth keeps proving itself.

The two notes synthesized here read the same facts and reached different conclusions. One applied a structural-proof standard and chose to stay on hold. The accurate phrasing is not that return on capital has been proven but that it is now most likely to be provable, and it withheld a price target given negative FCF, the capital raises, and the flagged 2027 increase. The other maintained a buy on an entry-price basis. Taking a price already 15% off its peak as the starting point, it applied a 28-29x multiple to about $15 of ex-gains 2027E EPS to arrive at a 12-month target of $430, with a withdrawal condition attached: it will be recalculated if 2027 CAPEX is quantified near $300bn. [Fact: the two notes' conclusions]

The difference between the two judgments is not a difference in facts observed but a difference in time horizon and standard. The structural view puts the burden of proof on the company until the cash return after depreciation is confirmed in the numbers; the price view calculates how much of that risk is already reflected in a stock that has already corrected. In keeping with this blog's principle of not recommending a specific direction, we present both frames side by side, but the common denominator is clear. Either way, the next variable to be judged is not demand but cash.

## 7. Scorecard: The Next Two Weeks Will Decide

Here is a rundown of the boxes this print filled in, and the boxes it newly opened.

- Alphabet's share of the big-tech CAPEX commentary is now confirmed as a raise. What remains is Microsoft's first FY27 guidance (call in the early hours of July 30 KST) and Amazon's AWS growth rate (early hours of July 31). If Alphabet closed out the demand debate, these two will settle the margin and FCF debate.
- Whether Cloud growth holds above 50% for the next 2-4 quarters and whether margin holds above 30% are the confirming indicators for the upside case. If growth falls below 30% once supply constraints ease, the possibility of demand overestimation needs to be recalculated.
- Watch whether backlog keeps net-adding even after revenue recognition. A combination of a shrinking backlog, or one where only contract duration keeps extending, would signal deteriorating contract quality.
- The quarter in which trailing-12-month operating-cash-flow growth overtakes CAPEX growth is the starting point of the FCF turnaround. Conversely, if 2028 CAPEX exceeds $250bn while operating cash flow falls short of that pace, we will call it structural FCF impairment.
- Whether large additional equity or debt raises continue, whether SpaceX-style external leasing shrinks back in 2027-2028, and whether TPU external sales convert into recurring Cloud consumption are the checkpoints on the capital-efficiency side.
- The discriminator on the memory side is unchanged: DRAM contract pricing, and confirmation of Q3 contract prices on the Samsung Electronics and SK Hynix calls around July 30.

---

Names mentioned in this piece are examples for analysis and are not a recommendation to buy or sell any specific security. Responsibility for investment decisions and their outcomes rests with the investor. Alphabet did not provide 2028 CAPEX or Cloud revenue guidance; the customer mix, year-by-year recognition amounts and cancellation terms behind the $514bn backlog were not disclosed; and purchase volumes and supplier mix for HBM, DRAM and NAND are also not disclosed items. The 2028 FCF sensitivity and the H2 CAPEX arithmetic are our own estimates starting from current disclosures, not company guidance. The pre-tax size of the unrealized gain on private-equity stakes and its after-tax per-share effect are recalculations based on disclosures and may differ slightly due to rounding. The $430 target is the calculation of one of the notes synthesized here, not this blog's target price. Share prices and quotes are as of the morning of July 23, 2026 Korea time.

### Related Posts

- [Who Burns All Those Tokens? NVIDIA's Customer Map, Sovereign AI and Codex at 9 Million Start Answering](/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/)
- [Will AI Memory Demand Exceed Expectations? Reading the Over-Growth Odds Through Demand Scenarios and the Supply Map](/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/)
- [SK Hynix Chairman Chey Tae-won's Two Months of Remarks: The Company Gets Stronger, the Margin Peak Passes](/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/)
- [The Real Debate in Semiconductors: Four Physical Clocks and One Stock-Price Clock](/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
