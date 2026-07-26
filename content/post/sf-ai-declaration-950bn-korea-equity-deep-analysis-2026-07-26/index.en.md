---
title: "Dissecting $950 Billion: Three Things the San Francisco AI Declaration Changed, and One It Did Not"
slug: "sf-ai-declaration-950bn-korea-equity-deep-analysis-2026-07-26"
date: 2026-07-26T21:00:00+09:00
description: "We break the San Francisco AI Declaration and the $950 billion of Korea-US AI cooperation into contracts versus intent, then calculate what is already in Korean share prices and what is genuinely new. Roughly 20-25% of every AI capex dollar accrues to Korea, and almost all of it is memory. The real weight of this week lies in locking that share through 2030, in Samsung Foundry winning Broadcom as an anchor tenant, and in Korea joining NVIDIA's circular financing loop. That none of the declaration's four pillars claims the model layer is what caps the multiple."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["San Francisco AI Declaration", "Samsung Electronics", "SK Hynix", "Naver", "Broadcom", "NVIDIA", "Samsung Foundry", "HBM", "Sovereign AI", "Korean Semiconductors", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스", "네이버"]
draft: false
---

> Context: Three days ago, in [Oil Is the Trigger, Rates Are the Gun](/post/oil-war-premium-rates-ai-multiple-korea-memory-2026-07-23/), we identified Brent above $100 as the pivot point that would force the Fed into a hawkish turn, and wrote that under an escalation scenario even a low multiple would stop working as a shield. That level was realized within 24 hours. On Friday, July 24, renewed Middle East tensions pushed Brent above $100, and KOSPI closed down 5.72% at 6,690.62, with Samsung Electronics falling 7.59% and SK Hynix falling 8.34%. Then, that same night, after the Korean market had closed, San Francisco hosted the announcement of $950 billion in Korea-US AI cooperation. This piece calculates what actually changed where those two events collided.

## TL;DR

- The facts need straightening out first. The San Francisco AI Declaration is not a declaration by the US government or by industry; it is <strong>a declaration by the Korean government, delivered by President Lee Jae-myung</strong>. The Korean government hosted the summit as well, and the confirmed attendee list includes no officials from the US federal government, the State of California, or the City of San Francisco. This was an event where Korea declared its own position in the middle of Silicon Valley, not a bilateral agreement.
- The $950 billion figure is not something to analyze but something to take apart. It is the sum of $750 billion from the SK Group and $200 billion from Samsung Electronics-Broadcom. The former is a letter of intent (LOI), and Reuters and Fortune both specified that the latter is <strong>a statement of intent, not a binding contract</strong>. The presidential policy chief also explained it as being "in the nature of an MOU and a cooperation framework."
- For a sense of scale: the 2026 global memory market forecast stands at $889.3 billion. The total cooperation announced this week <strong>exceeds a full year of the entire global memory market</strong>. That does not mean the number is wrong; it means it is a multi-year cumulative nominal figure, and annualization and conversion rate are the whole of the analysis.
- Here is the value calculation. HBM makes up 35-55% of an accelerator's manufacturing cost, and Korea holds about 79% of global HBM revenue and about 67% of DRAM. Memory accounts for about 30% of hyperscaler capex in 2026. Multiply them together and <strong>roughly 20-25% of every AI capex dollar accrues to Korea, and almost all of it is memory</strong>. GPU logic, CoWoS packaging, power and land, networking, and construction carry almost no Korean share.
- Three things actually changed this week: that 20-25% share was locked into contract form through 2030; <strong>Samsung Foundry landed Broadcom as a second anchor tenant</strong>; and Korea was folded into the circular financing structure in which NVIDIA invests in Naver and Naver uses that money to buy NVIDIA. The market has priced in the second of these the least.
- One thing did not change. None of the declaration's four pillars covers the model and platform layer. Naver's HyperCLOVA X failed the government's first-round evaluation this past January because it was built on Alibaba's Qwen weights, and it is now being rebuilt on NVIDIA's Nemotron. <strong>Moving from Chinese open weights to American open weights is the substance of Korea's sovereign AI</strong>.
- The timing is unusual. The summit fell on a local Friday, early Saturday morning in Korea time. <strong>Korean equities have not priced this news even once</strong>. The first reaction comes on Monday, July 27, and the market will meet this news from the low ground it hit right after the oil-driven 5.72% plunge.

<div class="thesis-callout">
<div class="thesis-callout__label">Key Framing</div>

This week, Korea formally declared itself the arms dealer of the AI era. The declaration's four pillars are a supply-chain hub, a lead-adopter nation, a cooperation network, and domestic social policy. None of them says anything about building models. This is not a defeat; it is a calculation. Reliably capturing 20-25% of AI capex through memory, foundry, and power equipment is something most countries cannot do. But an arms dealer's profit tracks the scale of the war, not who wins it. So this week's announcements extended Korean companies' revenue visibility through 2030, but left the ceiling on the multiple exactly where it was.

</div>

## 1. What Happened: Start With What the Declaration Actually Is

In Korean media and on social media, this event is often consumed as if it were a joint US-Korea declaration. The actual structure is different.

[Fact: Reuters and Korea government policy briefing] President Lee Jae-myung delivered the San Francisco AI Declaration on July 24 local time at The Midway in San Francisco's Dogpatch neighborhood. The Korean government hosted the summit, and the attendee list compiled by Reuters includes no officials from the US federal government, the State of California, or the City of San Francisco. [Blocked: US government attendance] This has not been confirmed by exhausting every possibility, but none of the reporting gathered shows any US government attendance.

The declaration's four pillars are as follows. First, to become a core nation in the global supply chain as a trusted AI semiconductor production base and supply-chain partner. Second, to become the country that adopts AI fastest and most effectively, a global AI testbed. Third, to build a horizontal cooperation network that includes developing countries. Fourth, to build a human-centered AI foundation society, grounded in the AI Framework Act that took effect this past January. [Fact: policy briefing]

The attendee roster sums up the character of the event. From Korea came Samsung Electronics Chairman Lee Jae-yong, SK Chairman Chey Tae-won, Hyundai Motor Group Chair Chung Euisun, and Naver Chairman Lee Hae-jin. From the US came NVIDIA's Jensen Huang, OpenAI's Sam Altman, Anthropic's Dario Amodei, and Broadcom's Hock Tan, while Microsoft was represented instead by its head of Azure hardware. [Fact: company and press reports] In other words, this was a meeting between Korean capital and American technology vendors, with no regulators or policymakers present. This composition also decided the nature of what came out of it. What emerged was not a treaty but purchase intentions and supply commitments.

## 2. Taking Apart the $950 Billion: What Is a Contract and What Is Intent

Let's break down the announced cooperation item by item.

| Korean Side | Counterparty | Content | Amount | Nature |
|---|---|---|---|---|
| Samsung Electronics | Broadcom | HBM4/HBM4E supply, sub-2nm foundry, advanced packaging | $200 billion+, through 2030 | Strategic MOU |
| SK Telecom / SK Hynix | NVIDIA | 2GW-class AI factory, priority allocation of Vera Rubin, joint next-gen HBM development | $500 billion+ | Letter of Intent (LOI) |
| SK Hynix | Microsoft | Long-term server memory supply | Undisclosed | Letter of Intent |
| SK Telecom / SK Hynix | Anthropic | 5GW-class AI data center cooperation, through 2029 | Undisclosed | MOU |
| Naver | NVIDIA | Strategic equity investment, GPU and technology cooperation | $1 billion | Investment agreement |
| Naver | Brookfield | Sejong AI factory infrastructure financing | Up to $9 billion | Non-binding term sheet |
| Samsung SDS | Anthropic | Claude-based enterprise AI, workforce training | Undisclosed | MOU |
| Hyundai Motor Group | NVIDIA | Robotics reference platform, 50,000 Blackwell GPUs | Undisclosed | Partnership |
| National Pension Service | Six Silicon Valley VC firms | Investment cooperation | Undisclosed | MOU |

[Fact: company announcements, disclosures and press]

A few things stand out here.

First, effectively only one item is a binding contract: the Naver-NVIDIA equity investment. Everything else is a letter of intent, an MOU, or a non-binding term sheet. Fortune and Reuters both wrote explicitly that the Samsung-Broadcom deal is a statement of intent rather than a binding contract, and presidential policy chief Kim Yong-beom explained it as being "in the nature of an MOU and a cooperation framework." [Fact: press and briefing] This is not a flaw; it is the normal form for a deal at this stage. But the market needs to price in that these documents sit at a different layer from revenue recognition.

Second, the definition of the dollar figures differs by source. SK Hynix's official newsroom, CNBC, and NVIDIA all label the $500 billion-plus figure as the NVIDIA deal alone, while most Korean media reported $750 billion by combining in Microsoft and Anthropic. [Fact: figures defined differently by source] Citing the number without also stating its definition produces double counting.

Third, the scale needs to be put in perspective. TrendForce's 2026 global memory market forecast is $889.3 billion. The $950 billion total cooperation announced this week exceeds a full year of the entire global memory market. [Inference: scale comparison] That does not mean the number is wrong; it means it is a multi-year cumulative nominal figure. Dividing Samsung-Broadcom over five years works out to $40 billion a year, which is meaningful set against Samsung Electronics' semiconductor-division annual revenue but not a scale that redefines the company. The SK deal carries the same character, a total-project-cost figure that mixes data center construction cost, GPU purchases, and memory supply value.

The analytical payoff lies not in the headline total but in the annualized figure and the conversion rate. And this week is the first window onto that conversion rate.

## 3. What's Already in the Price: Korea's 20-25% Share of Every AI Capex Dollar

Calculating how much Korea actually captures from AI capex reveals what this week's announcement adds at the margin.

HBM's share of accelerator manufacturing cost runs, by product, at about 41% for the H100, 35% for the H200, 45% for the B200, and 43% for the GB200 superchip. [Fact: semiconductor analysis, single-source directional] And as of Q1 2026, Korea holds about 79% of global HBM revenue (SK Hynix 58%, Samsung Electronics 21%), about 67% of DRAM (Samsung 38.5%, SK 28.8%), and about 47% of NAND. [Fact: Counterpoint and TrendForce]

Layer on top of that memory's share of hyperscaler capex. SemiAnalysis puts it at about 30% in 2026, up from roughly 8% in 2023-2024. Morgan Stanley sees memory's share of cloud capex rising from 12% in 2023 to 40% in 2027. [Fact: house estimates]

Multiply them together and the answer falls out. <strong>Korean memory's share of every AI capex dollar is roughly 20-25%</strong>. [Inference: own calculation] This is both the quantitative skeleton of the Korean semiconductor investment case and, at the same time, its ceiling. Where does the remaining 75-80% go? To GPU logic designed by NVIDIA and built by TSMC, to CoWoS advanced packaging that TSMC all but monopolizes, and to power and land, networking, construction, and labor. Korea's share of that remainder is limited to a slice of power-equipment exports and a just-now-growing slice of advanced packaging.

This share is already in the earnings. Samsung Electronics' preliminary Q2 2026 results show revenue of KRW 171 trillion and operating profit of KRW 89.4 trillion, with the semiconductor (DS) division at KRW 89.6 trillion (DRAM KRW 71 trillion, NAND KRW 21.3 trillion). SK Hynix is expected to post revenue of KRW 84.1 trillion and operating profit of KRW 64.1 trillion, an operating margin near 76%. Combined, the two companies' quarterly operating profit exceeds KRW 150 trillion. [Fact: preliminary results and consensus] Korea's semiconductor exports in the first half came to $192.4 billion, up 162.6% year on year, already surpassing last year's full-year record.

In other words, what this week's announcement newly creates is not volume itself. The volume is already on the income statement. What it newly creates is <strong>documented extension of that volume's duration through 2030</strong>. In the volume-versus-margin-duration distinction this series has repeated, this week added weight to the duration side.

## 4. What's New, Part One: Samsung Foundry Lands an Anchor Tenant

This is the item the market has priced in the least. Reading the Broadcom deal purely as a memory supply contract misses half the story.

Samsung Electronics' Q2 2026 was a record quarter overall, but within it, the System LSI and Foundry division posted a quarterly operating loss of about KRW 2.8 trillion. June alone, however, was its first monthly profit since 2023. [Fact: preliminary results and broker estimates] Foundry's global market share stood at 6.5% in Q1 2026, an 11-fold gap versus TSMC's 72.3%. 2nm yield is reported in the 50-60% range, with an internal target of 70% by year-end; reports diverge between 55% and above 60%. [Fact: TrendForce and others, figures disputed]

Against that backdrop, here is what it means for Broadcom to show up. Broadcom is the number-one player in custom AI chip design, with Google's TPU and Meta's MTIA among its clients, and OpenAI is designing its own chip with Broadcom too. That same Broadcom has now said it will bundle memory, sub-2nm foundry, and advanced packaging together and hand them to Samsung through 2030. Samsung has already begun producing Tesla's AI5 at 2nm at its Taylor fab, and Taylor is being upgraded so its entire line runs at 2nm, at a scale of 50,000 wafers a month, double the original plan. [Fact: companies and press]

<strong>Samsung Foundry landed a second anchor tenant this week.</strong> The first was Tesla ($16.5 billion, through 2033), and the second is Broadcom. In foundry, an anchor tenant is both the volume that turns the yield learning curve and the reference case that persuades other customers. The sequencing matters given that Qualcomm is currently weighing Samsung's 2nm process for a portion of its 2027 Snapdragon volume.

Why does this matter for valuation? Right now, foundry is effectively priced as a negative in Samsung Electronics' stock, because it is a division running a quarterly loss of KRW 2.8 trillion. If Broadcom's volume converts into actual wafer starts and yield reaches 70%, this division flips sign from value destruction to value creation. The memory boom is already in the price; a foundry turnaround is not. [Inference: segment valuation] The timing of that turnaround, though, is disputed even internally. Some reports point to a Q4 target, the foundry division head has said profitability within 2026 is unlikely and 2028 is more realistic, and other views point to 2027. [Fact: reports differ]

Set alongside reports that TSMC is effectively sold out through 2028, and the fact that its 3nm lead time now exceeds a year, this makes it likely that Broadcom's volume is not business taken away from TSMC but excess demand TSMC cannot accommodate. [Inference: supply-demand structure] TSMC announced the same week that it would invest an additional $100 billion in Arizona. Both companies are in expansion mode at once, which is a negative signal for the 2028 supply-discipline debate.

## 5. What's New, Part Two: Circular Financing Lands in Korea

For the Naver deal, structure matters more than the dollar figure.

NVIDIA is investing $1 billion in Naver. Brookfield is providing up to $9 billion in infrastructure financing under a non-binding term sheet. With that money, Naver will expand its Sejong data center from 55MW to 200MW by 2028 and buy roughly 100,000 NVIDIA GPUs. [Fact: NVIDIA newsroom and companies]

Reduced to one sentence, the structure is this: NVIDIA funds the customer, and the customer uses that capital to buy NVIDIA's product. It is the exact structure that has drawn circular-financing criticism around OpenAI and CoreWeave over the past year. This week, Korea became a participant in that structure, which means it imported the upside and the downside together.

The upside is clear. Before this announcement, Naver was the large-cap stock most left behind by the AI rally. Its share price stood at KRW 185,900 as of July 20, 28% below the KRW 250,000 level of a month earlier and nowhere near its past peak of KRW 450,000. Union-related risk and delayed AI monetization were the reasons. Overnight, that company gained a roughly $10 billion infrastructure financing pathway and NVIDIA as an equity partner. This is material that could shift its standing from laggard to infrastructure holder. [Inference: change in standing]

The downside is equally clear. First, Brookfield's $9 billion is non-binding. Second, the capital burden of 200MW and 100,000 GPUs is by no means light for a company of Naver's size. Third, there is timing. Hyperscaler bond coverage ratios have fallen from about 5x in February this year to below 2x in July, and 2026 AI-related bond issuance is forecast at $570 billion, of which $236 billion had already been absorbed by the end of May, roughly four times the pace of the same period last year. [Fact: Morgan Stanley estimate and press] Korea is entering the infrastructure financing market exactly as that market is tightening. The 2.95% real yield and the rising term premium covered in the piece three days ago are precisely the price of this money.

There was one more contrasting scene the same week. At an AMD event on July 22-23, Anthropic announced deployment of up to 2GW of AMD MI455X, hedging its NVIDIA dependence. [Fact: AMD announcement] Korea's announcements this week ran the other way: SK, Naver, and Hyundai Motor all converged on a single NVIDIA roadmap. In terms of supply security, that secures priority allocation; in terms of vendor concentration, it is a bet with no hedge.

## 6. What Didn't Change: The Missing Model Layer

Look again at the declaration's four pillars: supply-chain hub, lead-adopter nation, cooperation network, AI foundation society. Taken apart one by one, they translate to component supplier, consumer, distributor, and domestic regulation. <strong>None of them is a pillar about building a model or a platform.</strong>

Evidence that this is a matter of substance rather than rhetoric sits inside this week's own announcements. Naver's HyperCLOVA X is being upgraded on top of NVIDIA's Nemotron open model. Yet HyperCLOVA X failed the government's first national AI model evaluation this past January, because it had built its multimodal vision encoder on top of Chinese company Alibaba's Qwen 2.5 weights, and the government judged that reusing external weights could not count as a proprietary model. [Fact: Korean press, January 2026] In other words, Korea's flagship sovereign AI model has simply moved its foundation from Chinese open weights to American open weights.

The performance gap also shows up in the numbers. On the Artificial Analysis Intelligence Index, LG AI Research's EXAONE 4.0 32B scores 43, the highest global ranking of any Korean model at 7th place, while Google's Gemini 3 Pro and OpenAI's GPT-5.0 each score 73. [Fact: benchmark] That is a gap of roughly 40%.

The ecosystem indicators are colder still. Korea ranks first in the world for AI patents registered per 100,000 people. Yet the number of unicorns fell from 10 in 2022 to zero in 2023, and to just one each in 2024 and 2025. Korea has the fourth-worst net AI talent outflow among the OECD's 38 members, and Seoul National University failed to fill 75% of its STEM graduate program quota for the 2025 academic year. [Fact: various statistics] It is a structure with world-class engineering density but a broken capacity to spin up companies and hold on to talent.

The National Pension Service's MOU with six Silicon Valley VC firms should be read in this context. The stated purpose was to "cultivate the next Samsung or SK." That means the domestic ecosystem cannot produce the next champion on its own, so the search is being outsourced to Sand Hill Road. It is a rational choice, and at the same time a diagnosis. [Inference: policy reading]

So the conclusion comes together like this. Korea has now put its status as a component supplier capturing 20-25% of AI capex into documented form through 2030. That is a formidable asset most countries do not have. But a component supplier's profit tracks the cycle, while a platform owner's profit builds terminal value. In the earlier [piece on fair value for semiconductors](/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/), we wrote that the 2028-consensus multiples of 3.9x for Samsung Electronics and 4.3x for SK Hynix price in doubt about duration, not the disappearance of earnings. This week's announcements added to the evidence for duration but did not change the character of the multiple itself.

## 7. Timing: The Market Has Not Priced This In Yet

Checking the trading calendar reveals an unusual position.

The summit fell on Friday, July 24 in San Francisco local time, which is early Saturday morning, July 25, in Korea time. Korean equities' last trading day was Friday, July 24, and that day's close came before the news. <strong>In other words, KOSPI has never once priced the $950 billion announcement, and the first reaction comes on Monday, July 27.</strong>

What that last trading day looked like matters.

| Item | Thu, Jul 23 | Fri, Jul 24 | Change |
|---|---|---|---|
| KOSPI | 7,096.89 (+4.40%) | 6,690.62 (-5.72%) | Reclaimed 7,000 after five sessions, gave it back in a day |
| KOSDAQ | 790.28 (+5.22%) | 748.22 (-5.32%) | Fell in tandem |
| Samsung Electronics | ~KRW 270,000 (+3.65%) | KRW 249,500 (-7.59%) | Gave back most of three days of gains |
| SK Hynix | ~KRW 1,918,000 (+4.86%) | KRW 1,759,000 (-8.34%) | Fell below the 1.8 million-won line |
| USD/KRW | 1,466.80 | 1,466.6 | FX stable despite the equity plunge |

[Fact: exchange data and market close reports]

Friday's plunge was driven by Brent breaking above $100 on renewed Middle East tensions, the AI-capex-versus-cash-flow debate that followed big tech earnings, and Thursday's weakness in US tech stocks. Foreign investors net sold KRW 3.283 trillion on KOSPI, selling KRW 1.7568 trillion of SK Hynix and KRW 873.0 billion of Samsung Electronics. The two stocks that had ranked first and second in net buying just a day earlier flipped to first and second in net selling. [Fact: flow data] On a weekly basis, however, foreigners were still net buyers of KRW 2.0695 trillion. That leaves open the possibility that Friday was a sharp reversal rather than a change in direction.

So Monday's question is not whether the rally extends, but whether <strong>the largest supply-deal announcement on record can reverse an oil-driven 5.72% plunge</strong>. These two forces act on different variables. Oil and rates act on the discount rate; contracts act on the size and duration of earnings. The principle from the piece three days ago is put to an exact test this week. Selling memory on rates is a confusion of variables, but Brent breaking above $100 is the threshold of that piece's Scenario C, the range where even a low multiple stops working as a shield. Because both propositions hold at once, direction is hard to call outright, which is why the readout table below is needed.

## 8. A Layer-by-Layer Read for Korean Equities

Break this week's announcements into three layers from a stock-picking perspective.

<strong>Layer one, largely already in the price.</strong> This is Samsung Electronics' and SK Hynix's HBM and DRAM volume, evidenced by their combined Q2 operating profit of over KRW 150 trillion. What this week's announcement adds at the margin is not volume but visibility through 2030, which supports the downside of the multiple but is a different thing from an immediate upward revision to earnings estimates.

<strong>Layer two, new and not yet fully priced in.</strong> Three strands. First, Samsung Foundry's capture of Broadcom as an anchor tenant, which could flip the sign on a division running a KRW 2.8 trillion quarterly loss, and is not reflected in the current share price. Second, Naver's shift into an infrastructure holder, having gained a roughly $10 billion funding pathway and NVIDIA as an equity partner while its stock sits in laggard territory. Third, the physical build-out of domestic AI data centers. Once SK Telecom's 2GW and Naver's 200MW actually break ground, orders flow down to power equipment, transformer, cooling, construction, and PCB makers. Korea's three major power-equipment firms have already logged over KRW 7 trillion in new orders in Q1 alone and a backlog exceeding KRW 32 trillion, and 2025 exports of ultra-high-voltage transformers to the US hit a record $1.3 billion. [Fact: export and order statistics]

<strong>Layer three, structurally not obtained.</strong> The model and platform layer. This absence sets the ceiling on the multiple, and this week's declaration gave that absence policy-level sign-off.

There is one contrast worth flagging from this week's action. On a weekly sector-return basis, semiconductors ranked last at -9.5%, while telecom ranked first at +6.1%. Isu Petasys, long classified as an AI beneficiary stock, is down 46% over three months. [Fact: market data] That is empirical proof that a beneficiary label does not automatically convert into performance. Whether orders actually come down, and which company's income statement they land on and when, has to be checked separately.

## 9. Stress-Testing the Counterarguments

The stronger the catalyst, the more important it is to set up the counter-case.

<strong>Power is the most concrete constraint.</strong> The 2GW SK Telecom disclosed is larger than the 1.5GW that Korea's entire data center power demand is projected to reach within three years. Data center capacity with grid-connection applications filed through 2029 totals about 49GW, equivalent to 35 reactors at 1.4GW each, and 86.3% of those applications are concentrated in the greater Seoul metropolitan area. 345kV transmission lines take about nine years to build, and more than half of planned projects are delayed by local opposition. [Fact: grid statistics and press] That said, SK's site is in the Yeongnam region and Naver's is in Sejong, both outside the Seoul-metro concentration, which lowers the degree to which this criticism applies directly to these two projects. [Blocked: no direct reporting on grid feasibility for these two projects]

<strong>Nobody yet knows the conversion rate on these letters of intent.</strong> No analysis in Korean reporting has been found that directly verifies whether the $950 billion will actually convert into binding orders. There has been political sparring over the figures, but it has not addressed the conversion rate. [Blocked: no analysis of conversion rate] If anything, the fact that the presidential office has repeatedly had to explain that the figures are not exaggerated is itself indirect evidence of market skepticism.

<strong>Single-vendor dependence on NVIDIA has deepened.</strong> The benefit of priority allocation and the risk of roadmap dependence sit inside the same contracts. This contrasts with Anthropic hedging 2GW into AMD the same week.

<strong>This is negative for supply discipline.</strong> Samsung is bundling 2nm, packaging, and HBM for Broadcom; SK is building 2GW; TSMC is putting another $100 billion into Arizona. All of it points toward capacity expansion. Earlier pieces in this series argued that the 2028 risk is normalization of ASP and margin, not demand destruction, and this week's announcements lean toward amplifying that risk rather than reducing it. Visibility on volume and duration of margin are different variables.

<strong>The financing window is narrowing.</strong> A coverage ratio below 2x, $570 billion a year in AI-related bond issuance, a 2.95% real yield. The fact that Brookfield's $9 billion is non-binding carries more weight in this environment than it would in normal times.

<strong>The macro backdrop has moved the wrong way.</strong> Brent breaking above $100 pushes up the odds of a September hike and weighs on multiples. Contracts increase earnings, but the discount rate cuts into the present value of those earnings.

## 10. Readout Table: The Next Two Weeks Will Show the Conversion Rate

- <strong>Monday, July 27 open.</strong> The first reaction. The thing to watch is not the direction of the index but the dispersion within it. Whether Samsung Electronics and SK Hynix rise together, or whether Samsung Electronics (with its foundry leverage) and Naver move differentially, will show whether the market is reading this week's announcements as volume or as structural change.
- <strong>July 29-30, Samsung Electronics and SK Hynix earnings and calls.</strong> This is the real proving ground. Watch whether Broadcom volume is discussed alongside a wafer-start schedule, whether the foundry breakeven timeline is pulled forward, and whether the Q3 contract price increase confirms the 13-18% server DRAM forecast range.
- <strong>FOMC and Chair Warsh's press conference, early morning July 30.</strong> Whether he treats Brent's move above $100 as transitory is the verdict on the discount-rate side.
- <strong>Microsoft, Meta, and Amazon earnings, July 30-31.</strong> Alphabet already proved demand, so it is now these three's turn to prove margin and cash flow. For SK Hynix's supply letter of intent with Microsoft to gain substance, Microsoft's capex guidance needs to back it up.
- <strong>KUIC's first project, sometime in August.</strong> The first execution case from the $350 billion Korea-US Investment Corporation (KUIC) will emerge. It could become the first document showing how this week's declaration connects to tariffs.
- <strong>Evidence of conversion.</strong> Watch for concrete disclosure of Broadcom's volume, conversion of Brookfield's term sheet into a binding contract, and confirmation of site and grid connection for SK Telecom's 2GW. If two or more of these appear, the $950 billion turns from a number into something real. If a quarter passes with none of them, it remains a set of letters of intent.

The discriminator does not change this time either. It is the DRAM contract price. However large the declarations and MOUs are, if the contract price rolls over, the market will discount the 2030 visibility away.

---

Stocks mentioned in this piece are examples for analysis and are not a recommendation to buy or sell any specific security. Responsibility for investment decisions and their outcomes rests with the investor. Most of the announced cooperation sits at the stage of letters of intent, MOUs, and non-binding term sheets, not binding contracts or confirmed orders. Headline totals such as $950 billion and $750 billion are defined differently by source, as standalone figures in some cases and combined figures in others, leaving room for double counting. The 20-25% figure for Korea's share of AI capex is our own calculation, multiplying HBM's cost share, Korea's memory market share, and memory's share of capex, and is not an official estimate from any institution. Memory's share of cloud capex and the size of the sovereign AI market, among other figures, vary widely across research houses. The timing of a foundry profitability turnaround and 2nm yield figures diverge across reports. Power-grid statistics are national in scope and are not data that directly verifies the feasibility of individual projects. Price and flow data are as of the July 24, 2026 close and do not reflect subsequent moves.

### Related Posts

- [AI Fundamentals Are Solid, the Problem Is Rates, the Trigger Is Oil: The Transmission Path from Brent at $94 to Korean Memory](/post/oil-war-premium-rates-ai-multiple-korea-memory-2026-07-23/)
- [Alphabet's Q2: Cloud +82% Ends the Demand Debate, Negative FCF Starts the Cash Debate](/post/alphabet-q2-2026-cloud-82-fcf-negative-memory-demand-2026-07-23/)
- [Who Burns All Those Tokens? NVIDIA's Customer Map, Sovereign AI and Codex at 9 Million Start Answering](/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/)
- [Are Semiconductors Cyclical, and What Is Fair Value? Pricing Samsung, SK Hynix and Micron with FCFE and Normalized Earnings](/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
