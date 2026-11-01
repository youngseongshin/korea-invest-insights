---
title: "The Marginal AI Dollar Is Now Debt: Ackman's 'Near-Infinite ROI' Math Is Right, His Fed-Mistake Verdict Is Not"
date: 2026-11-01T23:40:00+09:00
lastmod: 2026-11-01T23:40:00+09:00
categories: ["Macro-Insight", "market-analysis"]
tags: ["Bill Ackman", "Fed", "Kevin Warsh", "Interest Rates", "AI Capex", "Hyperscalers", "Neocloud", "Free Cash Flow", "Memory"]
series: ["macro-gates-2026"]
slug: "ackman-ai-rates-fed-mistake-marginal-dollar-is-debt-2026-11-01"
description: "Ackman says AI's near-infinite ROI made the Fed's hike a mistake. The math holds for GPUs: 50bp cuts their NPV 1-4%. But Big Tech's Q3 free cash flow summed to -$31.8B. The marginal AI dollar is now mostly debt, and debt feels rates."
image: "cover.en.png"
draft: false
---

On September 24 (US time), Pershing Square CEO Bill Ackman wrote on X that "winning the race for super intelligence has a near infinite ROI." Higher rates, he argued, would not reduce AI investment or the demand for compute. They would only push inflation higher, because interest costs are embedded in everything. His conclusion: "I think the Fed might have just made a mistake" ([Business Insider via Yahoo, Sep 26](https://finance.yahoo.com/economy/policy/articles/billionaire-investor-bill-ackman-says-160620045.html)). On September 16 the Fed had raised its policy rate by 25bp to 3.75-4.00%. It was the first hike since July 2023, and the vote was 12-0 ([Fed statement, Sep 16](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)).

In Korea the argument spread as a simpler line: if the expected return is 100%, what difference does a 5% versus 5.5% rate make? The original post contains neither 100% nor 5.5%. The logic is the same, though. When expected returns far exceed the cost of capital, a small change in that cost does not change the investment decision.

A month later, Fed Chair Kevin Warsh rejected the view at his press conference: "Interest rates get in the cracks." Who is right matters for AI capex, for memory chips, and for the stocks of companies that borrow to build data centers.

<strong>Our view: Ackman's arithmetic is right. In our hypothetical examples, a 50bp rise cuts the NPV of short-lived, high-return investments such as GPUs by only 1-4%. But the conclusion that the Fed made a mistake does not follow from that arithmetic. In Q3 2026 the combined free cash flow (FCF) of the five hyperscalers was -$31.8 billion. The marginal AI dollar now comes from outside operating cash, and the largest identified source is debt. Borrowers are sensitive to rates. Ackman himself said so about neoclouds in October. And if AI investment truly ignores rates while inflation pressure persists, the Fed has to press harder on other sectors, such as housing, autos and small business. Insensitivity alone is not a reason to stop hiking.</strong>

Data are as of November 1, 2026. The sources are the September 24 X post (as quoted in press reports), CNBC's unofficial transcript of an October 22 interview, and coverage of Warsh's October 28 press conference. Company figures are from each firm's latest quarterly results (Microsoft's September quarter, Oracle's August quarter). Rates and credit spreads are FRED values for October 29.

## The original post contains neither "100%" nor "5.5%"

Put the popular summary next to the original and the gap is clear.

| Item | Popular summary | Original and facts |
|---|---|---|
| Expected return | 100% | "winning the race for super intelligence has a near infinite ROI" (X, Sep 24) |
| Rates | 5% vs 5.5% | The Fed raised the short rate by 25bp to 3.75-4.00%. On CNBC on Oct 22, Ackman said a 5% 10-year is still a relatively low cost of capital |
| Conclusion | The rate gap is meaningless | "I think the Fed might have just made a mistake." Hikes fail to cut investment and raise inflation through pass-through of interest costs |

The "5%" probably comes from the October CNBC interview. Ackman said that since intelligence is so valuable, "you can earn an attractive return even with a risk-free rate of 5 percent" ([CNBC transcript, Oct 22](https://www.cnbc.com/2026/10/22/cnbc-exclusive-transcript-pershing-square-founder-ceo-bill-ackman-speaks-with-cnbcs-sara-eisen-on-squawk-on-the-street-today.html)). The "100%" turns "near infinite" into an example number. The numbers differ, but the logic is the same, so we test the logic of the original.

The original runs like this. If the ROI of the super-intelligence race is near infinite, higher rates will not reduce demand or investment. Because interest costs are embedded in everything, a hike then raises inflation. The more the Fed hikes, the more inflation rises and the more the Fed must hike. The old models may not apply to the current paradigm. The next day, answering critics who said the 2022-23 hikes brought inflation down, he replied: "The world has changed since 2023."

## Ackman's post stacks claims about investment, prices and policy

The post reads as one sentence, but it stacks claims that need different conditions to hold.

| Layer | Claim | What it needs |
|---|---|---|
| A. Investment ignores rates | Expected ROI overwhelms the cost of capital, so AI investment does not respond to rates | Investors fund with their own cash, and expected ROI stays unchanged as rates move |
| B. Hikes raise prices | Interest costs are in every price, so each hike pushes inflation up | The cost channel is larger and more durable than the demand channel |
| C. So the hike was a mistake | The Fed should stop hiking | A and B both hold, and the Fed's goal is to curb AI investment |

A is conditionally true. B has weak evidence. C points the other way the more A is true. We take them in order.

## 50bp is small for a GPU and large for a 15-year data center building

First, the arithmetic. We computed how much the net present value (NPV) of an investment falls when the discount rate rises from 5.0% to 5.5%, using hypothetical projects. Each invests 100 today.

<div class="fig-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.4em 0"><img src="/post-assets/ackman-ai-rates-fed-mistake-marginal-dollar-is-debt-2026-11-01/npv-50bp.en.svg" alt="NPV and equity-multiple change when the discount rate rises 50bp from 5.0% to 5.5%. 200 back in one year (IRR 100%) -1.0%; 100 a year for five years (IRR 96.6%) -1.8%; GPU server over five years (IRR 19.9%) -4.4%; data center building over 15 years (IRR 10.0%) -12.3%; perpetual-growth equity multiple (9% discount rate, 4% growth) 20.0x to 18.2x, -9.1%." loading="lazy" style="display:block;width:100%;min-width:720px;max-width:none;height:auto;margin:0 auto"></div>

| Hypothetical project (invest 100) | IRR | NPV (5.0%) | NPV (5.5%) | Change |
|---|---:|---:|---:|---:|
| 200 back in one year | 100.0% | 90.5 | 89.6 | -1.0% |
| 100 a year for five years | 96.6% | 332.9 | 327.0 | -1.8% |
| GPU server: 33.4 a year for five years | 19.9% | 44.6 | 42.6 | -4.4% |
| Data center building: 13.15 a year for 15 years | 10.0% | 36.5 | 32.0 | -12.3% |

For a project with a 100% IRR, 50bp trims NPV by 1-2%. Ackman's arithmetic holds. The direct interest cost is also small. The five hyperscalers' latest-quarter operating cash flow totals about $198.6 billion, or about $795 billion annualized. Even $500 billion of new debt at 50bp costs $2.5 billion a year, 0.3% of annual operating cash flow.

The same 50bp cuts the NPV of a 15-year data center building with a 10% IRR by 12%. Measured as the present value of its cash inflows, the drop is 3.3%. The thinner the margin over cost, the more the same rate change weighs on the decision. A perpetual-growth equity multiple, 1/(discount rate - growth), falls from 20.0x to 18.2x, or 9%, at a 9% discount rate and 4% growth. AI capex is a bundle of GPUs (short-lived, high expected return) and buildings, power and land (long-lived, lower expected return). Under these assumptions, "rates don't matter" holds only for the GPU part.

## In Q3, the marginal AI dollar became debt

Ackman's arithmetic has a hidden premise: investors fund with their own money, the cash their operations generate. In Q3 2026 that premise broke.

| Company (quarter) | Operating cash flow | Purchases of property and equipment | FCF |
|---|---:|---:|---:|
| Amazon (Q3) | 42.42 | 77.26 | -34.84 |
| Alphabet (Q3) | 42.29 | 51.36 | -9.07 |
| Microsoft (Sep quarter) | 58.00 | 39.37 | +18.63 |
| Meta (Q3) | 32.79 | 33.94 | -1.16 |
| Oracle (Aug quarter) | 23.1 | 28.5 | -5.40 |
| Total | 198.6 | 230.4 | -31.83 |

Figures are in US$ billions. FCF is operating cash flow minus purchases of property and equipment; finance-lease principal is not deducted. Amazon, Alphabet and Meta are from their 8-K earnings exhibits ([Amazon](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/amzn-20260930xex991.htm), [Alphabet](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm), [Meta](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/meta-09302026xexhibit991.htm)) and Microsoft from its [10-Q](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm). Oracle's figures come from press aggregates; we could not confirm them in the filing.

Capex is 116% of operating cash flow. Of the five, only Microsoft has positive FCF. The gap can be filled with cash on hand, share issuance or debt. The largest identified source is debt: Amazon alone raised $48.1 billion of long-term debt in Q3, more than the five companies' combined $31.8 billion shortfall. Its own-definition quarterly FCF is -$33.5 billion (net of incentives).

For a marginal investor that borrows, rates work first through access to funding. Hyperscalers borrow at investment-grade rates; neoclouds borrow at high-yield rates. The spread widening and investor selectivity Warsh described run through this channel. The second channel is equity value. For a company that funds capex with share issuance and stock compensation, a 9% lower multiple means 9% less funding capacity.

Ackman conceded the crack himself on CNBC on October 22. He compared the neocloud play to "investing in a real estate developer in a highly levered format" and said they are very sensitive to their cost of capital. In the same interview he said SpaceX and the Mag 7 are "competing with the U.S. government to issue debt, and that's kind of bearish for rates." That is an observation that the investment boom pushes rates up. In the textbook, an investment boom raises the natural rate of interest (the rate that neither heats nor cools the economy), which is a reason for a central bank to raise rates.

## The winner's ROI is not the marginal dollar's ROI

The original speaks of the ROI of "winning the race." The winner's payoff and the expected return of the marginal dollar are different things. In a race with several entrants, each one's expected ROI is the probability of winning times the winner's payoff, minus the cost.

In an arms race no one can stop first, even when the combined ROI of all entrants is negative, because stopping means losing for sure. So the observation that AI investment ignores rates is correct. But if an arms race is why it ignores rates, the risk that much of the invested capital is destroyed rises with it. US railroads in the 1870s and fiber-optic networks in 1999-2001 are the precedents.

When capital destruction begins, rates become decisive again, because rates decide how long the indebted entrants can hold on. A single cycle can contain, in sequence, a phase where rates do not matter and a phase where they decide the outcome.

## The case that interest-cost pass-through beats demand restraint is weak

Now layer B, the claim that each hike pushes prices up. Researchers do measure a short-run effect in which hikes raise firms' working-capital costs and therefore prices. Barth and Ramey named it the cost channel ([Barth & Ramey, NBER Macroeconomics Annual 2001](https://www.nber.org/books-and-chapters/nber-macroeconomics-annual-2001-volume-16/cost-channel-monetary-transmission)).

Measured, it is small. US nonfinancial corporate debt was $15.7 trillion at the end of Q2 ([FRED BCNSDODNS](https://fred.stlouisfed.org/series/BCNSDODNS)). Passing all of a 25bp increase into prices adds $39 billion a year, 0.12% of $33.0 trillion nominal GDP. If 30% of the debt reprices in the first year (floating rate and refinancing), it is 0.04%. The effect raises the price level while debt reprices at the new rate, and stops when refinancing is done.

The demand channel behaves differently. A common rough estimate is that a 100bp hike lowers inflation by 0.1-0.4 percentage points after one to two years. For 25bp that is 0.03-0.1 points, and the effect persists while rates stay high. The two figures are not estimated on the same basis, so we use them only to gauge size. Nothing in them suggests the cost channel beats the demand channel for years.

For a "hike more, get more inflation" spiral, the cost channel would have to keep beating the demand channel. The recent record points the other way. While the Fed raised rates 525bp in 2022-23, core PCE inflation fell from the 5% range to around 3%.

Another Ackman remark weakens layer B. On October 22 he said that "if we can resolve Iran and Russia-Ukraine, I think rates are coming down, inflation's coming down." That places the cause of inflation in war and energy. If the cause is a supply shock, the question is whether to look through the shock. That is a different question from whether AI has cut the transmission of rates.

## The more AI ignores rates, the harder the Fed must press elsewhere

Layer C. Suppose layer A is true. AI investment does not respond to rates and bids up power, construction labor and memory prices. Core PCE inflation was 3.1% year over year in September and has been above 2% for 67 straight months since March 2021 ([FRED PCEPILFE](https://fred.stlouisfed.org/series/PCEPILFE)).

If inflation pressure persists and current restraint is not enough, the Fed then has to press harder on rate-sensitive housing, autos and small business to free labor, power and materials for AI, or accept higher inflation. The effect Ackman criticized, that hikes hurt only the weaker industries, is what the first path looks like when it works. Monetary policy normally moves resources through the rate-sensitive sectors.

The second path has a precedent. In 1996-99 the Greenspan Fed judged that the internet was lifting productivity and, apart from one move in March 1997, held off on hikes. That path ended with 175bp of hikes from June 1999 to May 2000 and the investment bust that followed. Either way, the verdict that the Fed erred does not come from layer A. The truer layer A is, the bigger the Fed's job.

## The Fed raised the short rate; AI firms' cost of capital is set by the long rate

The "5% versus 5.5%" summary folds the Fed's short rate and the market's long rate into one variable. The Fed raised the short rate by 25bp. A hyperscaler's cost of capital is set by 10- to 30-year yields and credit spreads. The 30-year Treasury yield hit 5.67% on October 7, the highest since 2002, and was 5.32% on October 29. The 10-year was 4.98% on October 29 ([FRED DGS30](https://fred.stlouisfed.org/series/DGS30), [DGS10](https://fred.stlouisfed.org/series/DGS10)).

Long yields move with growth expectations, fiscal policy, the term premium and the volume of bond issuance. Ackman named Big Tech and SpaceX issuance as a driver of higher rates. Fed Governor Christopher Waller was reported on October 13 as citing growth expectations, fiscal concerns and competition for investor dollars from massive AI bond issuance as the main drivers of higher government yields ([Scotsman Guide, Oct 13](https://www.scotsmanguide.com/news/feds-waller-says-ai-fueled-inflation-could-persist-for-years/)). No estimate splits the contributions. Still, the Fed alone did not make the "5% versus 5.5%" gap, and AI's own bond issuance has been named as one driver.

## Ackman's portfolio is built from rate-sensitive assets

Whether a claim is right is a separate question from where its author stands, but both matter. Ackman runs Pershing Square and has an economic interest in the stocks it holds.

| Exposure | Source | Link to rates |
|---|---|---|
| Microsoft, Amazon and Meta, 31.63% combined | [13F, Jun 30](https://www.sec.gov/Archives/edgar/data/2026053/000117266126003790/xslForm13F_X02/infotable.xml) | Equity multiples built on long-dated growth |
| Uber 12.72%, Brookfield 12.58%, Howard Hughes 10.23% | Same 13F | Brookfield is real infrastructure and alternatives; Howard Hughes is real estate development |
| Fannie Mae and Freddie Mac, "well north of 200 million shares" combined | CNBC, Oct 22 | Direct exposure to mortgage rates and spreads |
| Pershing Square Holdings (PSH) NAV -6.9% year to date | [PSH weekly NAV, Oct 20](https://pershingsquareholdings.com/?p=5978) | Relative underperformance in 2026 |

On October 22 Ackman said "our relative underperformance this year in large part is driven by Fannie and Freddie." Fannie Mae fell 72%, from $11.25 on January 5 to $3.15 on October 14, and closed at $4.80 on October 30. The manager, Pershing Square (PS), listed on the NYSE on April 29 together with the closed-end fund Pershing Square USA (PSUS) ([SEC 424B4](https://www.sec.gov/Archives/edgar/data/0002026053/000114036126018103/ny20040230x30_424b4.htm)). The manager's share price is also tied to fund performance and inflows. Rate hikes press on his whole book in the same direction.

His Fed commentary has also moved with his positions.

| When | Remark | Position at the time |
|---|---|---|
| Oct 2021 | The Fed should start raising rates as soon as possible ([CNBC](https://www.cnbc.com/2021/10/29/bill-ackman-calls-for-the-fed-to-start-raising-interest-rates-as-soon-as-possible.html)) | Held hedges against rising rates; made $2.7 billion on rate trades in 2022 ([Reuters via Kitco](https://www.kitco.com/news/off-the-wire/2023-02-10/ackmans-pershing-square-reaps-27-bln-rate-trade-down-9-2022-letter)) |
| Aug 2023 | Disclosed a short in 30-year Treasuries | Long-bond short |
| Oct 2023 | Covered the short: too much risk in the world to stay short bonds ([CNBC](https://www.cnbc.com/2023/10/23/bill-ackman-covers-bet-against-treasurys-says-too-much-risk-in-the-world-to-bet-against-bonds.html)) | Covered |
| Nov 2023 | Hard-landing risk unless the Fed cuts soon ([Fortune](https://fortune.com/2023/11/28/bill-ackman-fed-interest-rate-cuts-first-quarter-hard-soft-landing)) | Long equities |
| Aug 2024 | The Fed was too slow to raise and is too slow to cut ([investinglive](https://investinglive.com/centralbank/bill-ackman-says-fed-was-too-slow-to-raise-rates-now-too-slow-to-lower-them-20240805/)) | Long equities |
| Sep 2026 | The 25bp hike might be a mistake | Long megacaps, Fannie, Freddie and real estate; behind for the year |

In the record we checked, his Fed remarks have never run against the direction of his book. That alignment alone does not make them wrong. But readers should weigh them knowing his interests. We did not check his 2025 remarks.

His worldview points the same way. On CNBC in October he said "we're asymptotically approaching superintelligence." What follows is our interpretation. Treat AI as a contest between nations and the cost of capital looks like a wartime-finance variable, with the central bank cast as an institution that should support the effort. The Fed's 1942-51 cap on Treasury yields is the historical form of that view.

The politics overlap too. Ackman endorsed Donald Trump in July 2024, and Warsh is the chair Trump nominated, confirmed by the Senate in May. Yet the Fed's center of gravity sits on the hawkish side of Warsh. The October 28 vote to hold was 10-2, and both dissenters, Governor Lisa Cook and Cleveland Fed President Beth Hammack, wanted a 25bp hike ([Fed statement, Oct 28](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm)).

## A month later, Ackman named AI capex as a cause of inflation and prescribed more supply

Line up Ackman's remarks after the September 24 post and the emphasis shifts.

| When | Venue | Gist | Versus Sep 24 |
|---|---|---|---|
| Sep 25 | X reply | Answered critics who said the 2022-23 hikes cut inflation: "The world has changed since 2023" | No change |
| Oct 22 | CNBC interview | A 5% 10-year is still a low cost of capital. Neoclouds are very sensitive to their cost of capital. Big Tech and SpaceX issuance is bearish for rates. Resolve Iran and Russia, and rates and inflation come down | Conceded that marginal investors are rate-sensitive. Placed the cause of inflation in war and energy |
| Oct 28 | [Equity Mates podcast](https://shows.acast.com/equity-mates/episodes/bill-ackman-on-building-the-next-berkshire-ai-his-next-10-ba) (chapter at 16:42) | Said the 25bp hike may have signaled resolve and may have been a mistake, without committing. Named war-driven energy and unprecedented AI infrastructure spending as causes of inflation. Proposed more supply, through cheaper housing permits and development | Added "a signal of resolve" to "may have been a mistake." Named AI investment as a cause of inflation. Moved the prescription from monetary to supply policy |

We confirmed the October 28 podcast remarks from the episode's chapter titles and a summary by a Korean listener; we did not hear the audio. If the summary is right, Ackman named AI infrastructure spending as a cause of inflation, which is the Fed hawks' premise. We found no rebuttal from Ackman after Warsh's remarks.

## The Fed hawks accepted Ackman's premise and reversed his conclusion

The reactions split on whether they accept the premise, and on what they conclude from it.

<div class="fig-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.4em 0"><img src="/post-assets/ackman-ai-rates-fed-mistake-marginal-dollar-is-debt-2026-11-01/debate-map.en.svg" alt="Map of reactions. Rebuttal: Chair Warsh says AI capex is rate-sensitive too; Cullen Roche rebuts the claim that hikes raise inflation. Accept the premise, critical of hikes: Ackman, Mark Zandi, Gregory Daco. Accept the premise, stay restrictive: Hammack, Waller, Cook. Data: Q3 nonresidential fixed investment +12.7%, equipment +24.7%, though most of Q3 predates the hike." loading="lazy" style="display:block;width:100%;min-width:720px;max-width:none;height:auto;margin:0 auto"></div>

| Camp | Who | Gist |
|---|---|---|
| Rebuttal: capex is rate-sensitive | Kevin Warsh (Fed Chair, Oct 28) | "Interest rates get in the cracks." On the new technology and the investment surge: "do interest rates matter? I believe they do," and "I don't believe that they're somehow divorced from the rest of the economy." He noted wider credit spreads for some assets after the September hike ([Yahoo live, Oct 28](https://finance.yahoo.com/economy/policy/live/fed-meeting-live-updates-interest-rates-held-steady-in-split-vote-warsh-says-politics-played-no-role-ahead-of-midterm-elections-191946928.html)) |
| Rebuttal: hikes do not raise inflation | Cullen Roche (Discipline Funds) | Cited post-2022 disinflation and Turkey as counterexamples to "hikes raise inflation" ([TipRanks, Sep 25](https://www.tipranks.com/news/bill-ackman-asks-if-the-ai-boom-is-breaking-the-feds-inflation-playbook)) |
| Accepts premise, critical of hikes | Mark Zandi (Moody's) | "AI is running on its own dynamic and expectations for future profits are quite high"; hyperscalers can pay higher rates ([Yahoo, Oct 29](https://finance.yahoo.com/economy/policy/article/is-ai-investment-sensitive-to-interest-rates-warsh-says-yes-but-others-disagree-162933738.html)) |
| Accepts premise, critical of hikes | Gregory Daco (EY-Parthenon) | More hikes "could create further strain for already constrained, interest-sensitive sectors" ([TIKR, Sep 28](https://www.tikr.com/blog/bill-ackman-ais-near-infinite-roi-could-undo-fed-strategy)) |
| Data | Joe Brusuelas (RSM) | On the idea that AI investment is rate-sensitive: "Sure does not look that way following the September rate hike." Q3 nonresidential fixed investment rose 12.7% annualized and equipment 24.7% (BEA advance, [FRED](https://fred.stlouisfed.org/series/A008RL1Q225SBEA)). Most of Q3 predates the hike, so this does not show a response to rates |
| Accepts premise, stay restrictive | Beth Hammack (Cleveland Fed, Oct 13) | "I'm under no illusion that raising interest rates will reopen the Strait of Hormuz" or materially stop data center demand. Still judges a restrictive stance appropriate; dissented for a hike in October ([Scotsman Guide](https://www.scotsmanguide.com/news/feds-waller-says-ai-fueled-inflation-could-persist-for-years/)) |
| Accepts premise, stay restrictive | Christopher Waller (Fed Governor, Oct 13) | Hyperscalers are "still planning on spending trillions of dollars over the next three years," so demand pressure may remain and "we just have to decide how we want to respond to that" ([Scotsman Guide](https://www.scotsmanguide.com/news/feds-waller-says-ai-fueled-inflation-could-persist-for-years/)) |
| Accepts premise, stay restrictive | Lisa Cook (Fed Governor) | Sees AI as already causing inflationary pressure; dissented for a hike in October ([InvestorPlace, Oct 28](https://investorplace.com/2026/10/fed-holds-ais-bigger-risk-isnt-rates/)) |

Hammack and Waller also accept that core AI capex does not move much on 25bp. The split is over the conclusion. Ackman said the hike might be a mistake; Zandi and Daco see the burden of hikes landing on other sectors more than on AI. Hammack, Waller and Cook draw the opposite conclusion from the same observation: stay restrictive. It is the same structure as layer C above.

Warsh's rebuttal aims at a different layer. He said rates get into the cracks, and in the Q3 numbers the cracks are the marginal investors who borrow. Our view takes the hawks' conclusion and Warsh's diagnosis together. We accept that core investment funded with own cash ignores rates. But in Q3 a share of capex exceeded operating cash, that share was mostly debt-funded, and it is sensitive to rates.

## Verdict: the dominant variable is where the marginal dollar comes from

| Variable | Ackman's claim | Verdict | Evidence |
|---|---|---|---|
| Core capex funded with own cash (within a year) | Ignores rates | True | In hypothetical examples, 50bp moves GPU NPV -1% to -4%; interest cost is 0.3% of operating cash flow |
| Debt-funded marginal capex | Not in the X post; on CNBC, conceded neoclouds are sensitive | Sensitive | Five-company FCF -$31.8B, capex/operating cash flow 116%, building NPV -12%, equity multiple -9% |
| Does the cost channel beat the demand channel? | Yes (spiral) | Not supported | Cost channel is 0.04-0.12% of GDP in size; inflation fell during the 525bp of hikes in 2022-23 |
| Fed's right move in a rate-insensitive boom | Stop hiking | Opposite | With insensitive investment and persistent inflation pressure, restraining rate-sensitive sectors is the normal working of policy |
| Short rate vs long rate | One variable | Must separate | Long yields move with growth, fiscal policy, the term premium and issuance; Ackman named issuance himself |

The dominant variable is the second row. If the marginal dollar is own cash, "rates don't matter" holds for all AI capex. Even then, the fourth row stops it short of "the Fed erred." If the marginal dollar is debt, "rates don't matter" breaks at the margin first, and Warsh's "cracks" are right. The Q3 2026 numbers point to debt.

What would change the verdict:

- Toward Ackman: the five-company FCF total turns positive in H1 2027, so the marginal dollar is own cash again. Or core PCE falls quickly below 2.5% without further hikes.
- Further toward Warsh: high-yield spreads move above 350bp or a neocloud bond deal fails. Or one hyperscaler lowers its 2027 capex plan. High-yield spreads widened to 340bp on October 22 and were 326bp on October 29 ([FRED](https://fred.stlouisfed.org/series/BAMLH0A0HYM2)).

## What investors keep: risk shows up in the leveraged layer before the core

A useful observation survives from Ackman's post. If the Fed's 25bp does not change hyperscaler core capex, one-year visibility for memory and AI-chip demand looks better. On Q3 calls, Amazon said it expects to "spend meaningfully more in 2027," Alphabet's CFO said capex will increase significantly in 2027 (as reported), and Microsoft said capex will accelerate in the second half of its fiscal year ([Amazon call](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/), [Microsoft call](https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/)).

Risk appears first where rates seep into the cracks: neoclouds building data centers with debt, companies that depend on equity issuance, and buildings and power tied up in long leases. The next point is inference. If the leveraged layer wobbles while core capex holds, suppliers' pricing power can weaken before demand falls, because buyers with negative FCF negotiate next year's supply prices.

| When | What to check | Link to the verdict |
|---|---|---|
| Mid-November | Pershing Square 13F as of Sep 30: weights in Fannie, Freddie and megacaps | Size of the interest |
| December FOMC | Hike or not, and the number of dissents | The Fed majority's conclusion |
| Jan-Feb 2027 | Sign of five-company FCF in Q4 results and 2027 capex totals | Does the marginal dollar return to own cash? |
| Ongoing | High-yield spreads vs 350bp; neocloud bond yields and issuance | Are the cracks widening? |

<strong>Do you expect the marginal AI dollar to return to own cash in 2027, or the debt share to keep rising? Tell us the sign you expect for the five hyperscalers' combined FCF in H1 2027, and why.</strong>

This is research and information, not investment advice. The NPV calculations use hypothetical cash flows, and the sizes of the cost and demand channels are rough estimates. We confirmed the X post through press quotes and the October 28 podcast remarks through chapter titles and a secondary summary. Ackman runs Pershing Square and has an economic interest in its holdings. We used Anthropic's Claude for research and editing. Anthropic appears here as a buyer of AI compute.
