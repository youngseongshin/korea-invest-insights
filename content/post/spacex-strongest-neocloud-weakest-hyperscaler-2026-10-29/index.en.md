---
title: "SpaceX Is the Strongest Neocloud and the Weakest Hyperscaler. Its 90-Day Contracts Are Why."
date: 2026-10-29T14:30:00+09:00
categories: ["Exclusive Analysis", "Tech-Analysis", "market-analysis"]
tags: ["SpaceX", "Neoclouds", "Hyperscalers", "CoreWeave", "Nebius", "Oracle", "Nscale", "Google Cloud", "AI Infrastructure", "Backlog"]
series: ["Korea Semiconductor Watch"]
slug: "spacex-strongest-neocloud-weakest-hyperscaler-2026-10-29"
description: "SpaceX's AI arm beats every neocloud on installed capacity, build speed and cost of debt. Against the hyperscalers it has the thinnest backlog, no chip of its own and cloud contracts either side can end on 90 days' notice. Its 65.5% margin is a scarcity price."
image: "cover.en.png"
draft: false
---

SpaceX now runs more installed AI compute than any neocloud. Its Superintelligence (SI) segment had 1.7 gigawatts of nameplate compute at September 30, up from 0.6GW a year earlier, and its CFO said on the third-quarter call that it reached about 2.2GW by the end of October. It builds faster than anyone in the group. It also borrows more cheaply: its $25 billion of unsecured notes carry a weighted coupon of 5.855%, while CoreWeave's unsecured bonds yield about 15%.

Compare it with the companies it is so often grouped with, and the picture flips. SpaceX's backlog is **1.08 times** its annualized revenue. CoreWeave's is 10.1 times, Oracle's 8.6 times and Google Cloud's 4.6 times. Its cloud contracts typically run three years, but **either side can end them on 90 days' notice**. In the third quarter, backlog grew $15.5 billion, and all of that growth is due within a year.

**Our judgment: SpaceX is the strongest neocloud and the weakest hyperscaler. It has a near-hyperscaler balance sheet and a neocloud's order book. Its 65.5% SI adjusted EBITDA margin is the price of renting scarce GPUs on short terms, not proof of lower costs. At long-term contract prices, the payback that management calls "under one year" stretches to 1.8 to 3.4 years.** That does not make the business weak. It means SpaceX's AI revenue should not be valued as if it carried Microsoft's or Google's contracts.

On October 25 we ranked SpaceX fifth of six AI giants overall and first in scarce physical infrastructure. [KII, October 25](/post/hyperscaler-leadership-six-company-comparison-2026-10-25/) The two results fit together. The infrastructure is scarce, and the contracts that sell it are short.

This article is dated October 29, 2026. SpaceX figures are at September 30 unless stated. CoreWeave, Nebius and Amazon figures are at June 30 because their third-quarter results are not out yet; Oracle's are at August 31. Quotes from SpaceX's October 20 call come from a third-party transcript, not a company-edited one.

## The short version

- **Neocloud test, SpaceX wins:** the most installed capacity, the fastest builds, the only investment-grade balance sheet and the highest margin.
- **Hyperscaler test, SpaceX loses:** the thinnest backlog, contracts with 90-day exits, no in-house chip, internal demand that does not yet bring in much outside cash, and a lower credit rating.
- **The margin:** 65.5% SI adjusted EBITDA comes from a short-term price band of $30–50 per watt-year. Large long-term contracts pay $20–25.
- **Concentration:** an unnamed SI customer, "Customer B," was 34.5% of consolidated third-quarter revenue, up from 19.5% a quarter earlier.
- **Funding:** the bonds are cheap, but a related-party sale-leaseback costs an estimated 10.7% a year, and a $40 billion GPU lease starts amortizing in 2027.
- **The test:** whether the first exit windows pass with renewals at higher prices. Google's contract becomes terminable on 90 days' notice after December 31, 2026, and Anthropic's after initial non-cancellable periods that end in January and March 2027.

## Where SpaceX ranks on each test

The table compares business structures, not expected returns.

| Test | Against neoclouds | Against hyperscalers | Deciding fact |
|---|---|---|---|
| Installed capacity and build speed | First | Not comparable; hyperscalers do not disclose total gigawatts | 1.7GW nameplate; 220MW of GB300s brought up in 64 days |
| Cost of debt | First | Last | 5.855% coupon against about 15% for CoreWeave; Baa1/BBB/BBB+ against Microsoft's AAA |
| Margin | First on adjusted EBITDA | Last on operating margin | SI adjusted EBITDA 65.5%, but SI operating margin 5.7% against 36.2% at Google Cloud |
| Contract durability | Last | Last | Backlog 1.08x revenue; 90-day mutual exits |
| Chip cost | Level; all buy Nvidia or AMD | Last | No in-house accelerator before 2028 at the earliest |
| Own demand | First; neoclouds have little | Last | Grok and Cursor, against search, Office and ads |

## Against the neoclouds, SpaceX wins on size, speed and money

### It has the most installed compute and builds the fastest

The question here is how much compute each company already runs, and how fast it adds more.

| Company | Running | Contracted or targeted | As of |
|---|---|---|---|
| SpaceX | 1.7GW nameplate; about 2.2GW at end-October (CFO, call) | 2.5–3GW by year-end; management said it would be surprised by less than 13GW at end-2027 | Sep 30 |
| CoreWeave | 1.5GW active, 51 data centers | About 4.2GW contracted; over 1.85GW active by year-end; 8GW or more by 2030 | Jun 30 |
| Nebius | Not disclosed | 0.8–1GW connected by year-end; 5GW contracted-power target | Jun 30 |
| Nscale | About 25,000 GPUs | About 1.37GW running and contracted, 461,000 GPUs | S-1, September |
| Oracle | Total not disclosed | Added 850MW in its fiscal first quarter | Aug 31 |

The definitions differ, and the difference matters. SpaceX's nameplate figure counts installed GPUs times their full power draw, excludes cooling and distribution losses, and says nothing about utilization. CoreWeave reports active power. CoreWeave also has far more capacity under contract than SpaceX runs today. "Largest" therefore means installed capacity, not secured demand.

The clearer edge is speed. According to its prospectus, SpaceX brought up the first Colossus cluster (about 100,000 H100s, about 130MW) in 122 days. Colossus II took 91 days for about 110,000 GB200s (about 210MW), then 64 days for 110,000 GB300s (220MW). The prospectus puts the industry norm for a new 100MW data center at about two years. [Prospectus](https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm)

On the October call, Elon Musk said SpaceX is turning on about 200,000 GB300s a month for the rest of the year. At roughly 2kW per GPU, that is about 0.4GW a month. Two more months at that pace would take nameplate from 2.2GW to about 3GW, the top of its year-end range.

The speed comes from owning what sits under the chips. SpaceX bought about $2 billion of mobile gas turbines in April 2026, has bought about $0.99 billion of Tesla Megapacks to date, and designed Colossus II to run on its own gas generation. Neoclouds that rent shells and wait for grid power cannot match that. The same choice carries a legal risk: a Clean Air Act suit over turbines at Southaven, Mississippi, with a pending motion for an injunction.

### It is the only investment-grade neocloud

The question here is what each company pays for money.

| | SpaceX | CoreWeave | Nebius |
|---|---|---|---|
| Ratings | Baa1 / BBB / BBB+ (June 2026, stable) | Company rating not confirmed in filings; DDTL 5.5 rated Ba2/BB+ | Not disclosed |
| Representative cost | Unsecured notes, 5.855% weighted coupon, 11.7-year weighted maturity | 2032 9.625% notes yield about 15%; DDTL 4.0 at SOFR+2.25% | $3.5bn Citi senior secured facility at SOFR+2.75–3.50% |
| Interest vs adjusted EBITDA | 7.7% (3Q, consolidated) | 42.4% (2Q, net interest) | Not comparable |
| Liquidity | $89.9bn cash and short-term securities | $5.5bn cash and securities, $10bn undrawn | $8.04bn cash |

After its IPO and a $25 billion bond issue, SpaceX retired expensive debt inherited from X and xAI, including 12.5% secured notes. It paid $1.16 billion in prepayment premiums and booked a $1.53 billion loss on extinguishment. Third-quarter interest expense was 7.7% of consolidated adjusted EBITDA. [3Q 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)

The rating rests on Starlink, not SI. Third-quarter connectivity operating income was $2.37 billion, 5.5 times SI's $0.43 billion. Bond investors are also not paying top-tier prices. The notes were carried at a fair value of $22.9 billion against a book value of $24.9 billion, about 92%. Treating them as one bond, we estimate an implied yield of about 6.9%.

### Its margin is the highest in the group

SI revenue was $7.56 billion in the third quarter, up 830% from a year earlier. Its gross margin was 64.6% and its adjusted EBITDA margin 65.5%. CoreWeave's adjusted EBITDA margin was 58.6% with a GAAP operating loss, and Nebius's was 40.6% (49.7% in its AI cloud). [3Q 8-K](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066482/spaceexplorationtechnologi.htm), [CoreWeave 2Q](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm), [Nebius 2Q letter](https://www.sec.gov/Archives/edgar/data/1513845/000110465926094568/tm2622968d1_ex99-2.htm)

On the neocloud scorecard, then, SpaceX wins on capacity, speed, funding and margin. The trouble starts when the comparison moves to the companies whose revenue is contracted for years.

## Against the hyperscalers, SpaceX loses on the contract

### It has the thinnest order book

The chart asks one question: how many years of current revenue each company has already signed.

![Contract backlog divided by annualized latest-quarter revenue. Nebius 16.1 times, CoreWeave 10.1, Oracle 8.6, Google Cloud 4.6, AWS 2.9, Microsoft Cloud 2.6 and SpaceX 1.08. SpaceX is the lowest in the group.](/post-assets/spacex-strongest-neocloud-weakest-hyperscaler-2026-10-29/backlog-multiple.en.png)

SpaceX is below every hyperscaler, not only below the neoclouds. For investors, its AI revenue has less contracted visibility than any company in the comparison.

A low multiple is not always a weakness. Microsoft's commercial remaining performance obligation (RPO) is only 2.6 times Microsoft Cloud revenue, with a weighted remaining life of about 2.3 years. Office, search and advertising fill Microsoft's capacity without long contracts. SpaceX's equivalents are Grok and Cursor, and management aims to use about half of its capacity internally. In the third quarter, though, SI advertising brought in $538 million and Cursor $608 million, small against $7.56 billion of SI revenue. Internal demand fills capacity; it does not yet pay for it.

### All of the quarter's backlog growth is short

![SpaceX consolidated backlog by when it turns into revenue. At June 30, 2026, $26.6bn was due within one year and $20.9bn after, a total of $47.5bn. At September 30, $42.2bn was due within one year and $20.8bn after, a total of $63.0bn. The within-one-year part rose $15.6bn while the after-one-year part fell $0.1bn.](/post-assets/spacex-strongest-neocloud-weakest-hyperscaler-2026-10-29/backlog-split.en.png)

Backlog rose 32.7% in the quarter, from $47.5 billion to $63.0 billion. The share due within twelve months rose from 56% to 67%. The part due after a year did not grow at all.

The 10-Q explains why. SpaceX recognizes cloud revenue as a fixed monthly fee over the contract term, which is "typically three years," and either party can terminate on 90 days' notice. A contract that can be ended on 90 days' notice enters backlog only for the period that can be enforced. The more of these contracts SpaceX signs, the more its backlog piles up in the next twelve months. [3Q 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)

One caution: this is company-wide backlog, including government space and connectivity contracts, because SpaceX does not report AI backlog separately. What the numbers do show is that the company added no long-dated contracts on net in the quarter.

### One unnamed customer is two-thirds of SI revenue

| Item | 2Q26 | 3Q26 |
|---|---:|---:|
| Customer B share of consolidated revenue | 19.5% | 34.5% |
| Customer B revenue (our calculation) | about $1.5bn | about $5.0bn |
| Customer B share of SI revenue (our calculation) | about 60% | about 67% |
| Largest single customer's share of receivables | none above 10% at end-2025 | 27.7% |

Source: SpaceX 10-Q, note 3. Customer B is an SI customer whose name the filing does not disclose. We do not link it to any company.

### The disclosed contracts all have exits

| Customer | Size | Price and term | Exit |
|---|---|---|---|
| Google (June 5 filing) | About 110,000 Nvidia GPUs | $920m a month, October 2026 to June 2029, at a reduced fee during the ramp through September | If capacity was not delivered by September 30, Google could terminate after a one-month grace period or cut the fee. After December 31, 2026, either side on 90 days' notice |
| Anthropic (prospectus) | About 325,000 Nvidia GPUs | $1.25bn a month to May 2029 | After the first three months, either side on 90 days' notice |
| Anthropic (its S-1, October 26) | Up to $120.5bn across contracts and amendments signed May–October 2026 | About $3.1bn a month after full delivery, expected in December 2026 | After initial non-cancellable periods that end in January and March 2027, either side on 90 days' notice |
| Not named (2Q call) | $6.7bn of cloud revenue over six months, signed early in the third quarter | Ramping from October | Not disclosed |

Sources: [Google agreement filing](https://www.sec.gov/Archives/edgar/data/1181412/000162828026041150/spacexagreementfwp.htm), [prospectus](https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm), [Anthropic S-1](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm), [2Q call transcript](https://s21.q4cdn.com/184289198/files/doc_financials/2026/q2/SpaceX-Q2-2026-Earnings_Transcript-FINAL.pdf).

The Google contract implies $50–54 a year per watt of GPU power, using 1.875 to 2.0kW per GPU. That is at or above the top of the price band management describes.

### It has no chip of its own

SpaceX buys Nvidia exclusively; management said so on the second-quarter call. Its own chip effort, Terafab, targets a test chip in mid-2027 and volume production in the third quarter of 2028, a schedule Musk himself called aggressive. Google sells its TPUs to outside customers. Amazon has multi-year, gigawatt-scale Trainium commitments from Anthropic and OpenAI. Microsoft has Maia and Meta has MTIA.

A hyperscaler can lower the cost of a unit of compute by moving work onto its own silicon. SpaceX pays Nvidia's price. Its technical lead sits below the chip, in land, power, cooling and assembly.

### Its credit sits a rating class below

Microsoft is rated AAA and has issued no debt this year. Alphabet is rated Aa2/AA+ and held $265.1 billion of cash and securities. Meta is rated Aa3/AA-. SpaceX is Baa1/BBB/BBB+, and its free cash flow was negative $9.96 billion in the third quarter and negative $34.97 billion over nine months. It expects 2026 capital spending of $83–88 billion.

## The margin is a scarcity price, not a cost advantage

The chart asks how long SI's EBITDA takes to repay the capital spent on a watt of capacity, at the two price levels now visible in the market.

![Years of SI EBITDA needed to recover capex. At short-term prices of $40 to $50 per watt-year, payback is 0.9 to 1.7 years. At long-term prices of $20 to $25, it is 1.8 to 3.4 years. Nebius's disclosed payback on its second-quarter contracts, 1 year 10 months, sits at the start of the long-term range.](/post-assets/spacex-strongest-neocloud-weakest-hyperscaler-2026-10-29/payback.en.png)

The price band comes from three sources. On the October call, management said its prices were slightly above the top of the $30–50 per watt range it had given a quarter earlier, without defining the unit or the period. CoreWeave said on September 17 that its short contracts of three to six months were running at about $40 million per megawatt per year, or $40 per watt-year. [CoreWeave, September 17](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Continues-to-Contract-New-Compute-Capacity-at-Higher-Prices/default.aspx) Nebius puts its large long-term contracts at $20–25 and its short contracts at $40–50.

The capital cost is our estimate. Nine-month SI capital spending of $40.0 billion, divided by the 0.9GW of nameplate added, gives about $44 per watt. Subtracting the entire company-wide rise in construction in progress, $19.1 billion, gives about $23. Part of that rise is not SI's, and part will come online within months, so we use $30–44.

The result holds even at the bottom of the cost estimate. At $23 per watt, long-term prices still give a payback of 1.4 to 1.8 years. **A payback under one year needs short-term prices.** Nebius's disclosed payback of one year and ten months on its second-quarter contracts, which came with about 70% prepayment, sits at the start of our long-term range. SpaceX's efficiency edge comes from the price band it chooses, not from a lower cost base.

## The biggest buyers sign their long contracts with someone else

Three documents filed in the past ten days show the same pattern.

| Document | What touches SpaceX | Source quality |
|---|---|---|
| Alphabet third-quarter results (October 28) | Cloud revenue $30.71bn (+103%), operating margin 36.2%; TPU system sales contributed "meaningfully"; backlog $561bn; the CFO said Google began using third-party compute capacity from the end of the third quarter and will increase it in the fourth; 2027 capital spending to rise significantly | Filing, primary; call remarks from a third-party summary |
| Anthropic S-1 (October 26) | Long-term compute commitments sit with TPUs (Google, and Broadcom equipment leases) and at least $269.4bn of minimum commitments with three cloud providers. Only the SpaceXAI contracts can be ended by either side without cause on 90 days' notice. The cloud contracts end only on material breach, Broadcom leases only on default, and Nscale and Lambda contracts on delivery failures | Filing, primary |
| SpaceX third-quarter call (October 20) | About half of capacity for internal use, possibly 60/40; SpaceX said it rents at what is effectively spot pricing and does not sign long-term contracts; renewals at higher prices per watt | Third-party transcript, secondary |

Google's start date for third-party compute lines up with the end of the SpaceX contract's ramp in September. Google did not name its supplier, so we cannot say they are the same contract.

Meta's filing adds the scale. Its non-cancellable commitments, mostly third-party cloud capacity, reached $454.5 billion at September 30, 3.5 times the $131.1 billion at the end of 2025. [Meta 10-Q](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm) The largest buyers of outside capacity are the hyperscalers themselves.

The demand pool is deep. But the buyers lock in long commitments with TPUs, cloud providers and take-or-pay neoclouds, and keep SpaceX on terms they can exit. SpaceX says it prefers it that way, because spot pricing pays more in a shortage and leaves room to move capacity in-house. In our reading, the main substitute for SpaceX's outside revenue is the buyers' own long-term capacity, more than other neoclouds. That capacity arrives in 2027 and 2028: Google's larger 2027 capital budget, Broadcom TPU leases that start in 2027, and the extra TPU capacity in Anthropic's S-1 for 2028 to 2031. That is the first real test of SpaceX's outside contracts.

## Two books with different maturities

The chart sets the time a customer has committed for against the time SpaceX has committed for.

![Length of each commitment in years. Notice either side needs to exit a SpaceX cloud contract: 90 days. Typical cloud contract term: 3 years. Apollo GPU finance lease: 5 to 5.25 years per tranche. Server and network useful life: 5 to 6 years. Unsecured notes: 11.7-year weighted maturity.](/post-assets/spacex-strongest-neocloud-weakest-hyperscaler-2026-10-29/maturity-mismatch.en.png)

**The cost side is long.** Servers and network gear are depreciated over five to six years. On October 26 SpaceX signed a GPU finance lease with Apollo for about $40 billion, in tranches of five to five and a quarter years, paid quarterly in advance at one-twentieth of principal plus a fixed rate. The rate will be set at pricing, closing is expected within the year, and payments start in the first half of 2027. [8-K, October 26](https://www.sec.gov/Archives/edgar/data/1181412/000110465926118614/tm2628247d1_8k.htm) Non-cancellable purchase commitments reached $37.8 billion, 67.6% of them due in 2027.

**One lease is expensive.** SpaceX has a sale-leaseback with Valor, a firm linked to director Antonio Gracias. The liability was $12.9 billion at September 30, with $351 million of third-quarter interest. Dividing that interest by the average balance gives about 10.7% a year, our estimate. That is far above the 6.3% weighted fixed rate the filing gives for other financing, and the filing does not explain the gap. Valor is 34% of debt principal and 52% of third-quarter interest expense.

**The revenue side is short.** Contracts can end on 90 days' notice, and 67% of backlog runs off within a year.

In a shortage, this structure wins. Every renewal is a chance to raise prices, and management says renewals are being priced higher. When supply loosens, capacity without long contracts reprices first. In our reading, GPU supply could rise sharply in 2028 as substrate and interposer capacity expands.

There are two cushions. Grok and Cursor can absorb capacity a customer hands back, and Starlink's cash can carry the fixed payments. Internal use earns no outside cash, though, so the real cushion is connectivity cash flow, about $9.5 billion of annualized operating income on the third quarter. Debt of $38.0 billion plus the $40 billion Apollo lease comes to $78 billion, about 2.2 times annualized third-quarter adjusted EBITDA of $35.2 billion. On this rough measure, that is inside the 3.75 times leverage covenant on its revolving credit facility, though the covenant's own definition may differ.

## What it means for Korean memory

At 200,000 GB300s a month and 288GB of HBM each, SpaceX is installing about 57.6 petabytes of HBM a month. For 2027, supply caps the volume, so SpaceX's contract terms change little. For 2028, they matter more. CoreWeave and Nscale order GPUs against take-or-pay contracts. SpaceX orders against contracts that can end in 90 days. That makes SpaceX's 2028 GPU orders the more rent-sensitive part of the HBM demand that SK hynix and Samsung Electronics are planning for.

## The strongest case against our view

**Short contracts in a shortage are pricing power.** If renewals keep coming in higher, the 90-day exit works for SpaceX, not against it. CoreWeave's September release also said it was contracting new capacity at higher prices.

**Google is not a casual tenant.** Google held SpaceX shares worth $80 billion at June 30, subject to short-term sale restrictions, and Google executive Donald Harrison sits on SpaceX's board. A customer with that stake has reasons to stay.

**Internal demand is a real floor.** If Grok and Cursor grow into paying businesses, terminated capacity has somewhere to go.

We would change our view if fourth- or first-quarter filings show the after-one-year backlog rising sharply, or if the January to March 2027 exit windows pass with no terminations and higher renewal prices. Then "sells short" becomes "sells dear." A termination notice on a major cloud contract, Customer B above 40% of revenue, or an Apollo rate set 200 basis points or more above the unsecured notes would confirm the weakness.

## What to check next

| When (KST) | What | How to read it |
|---|---|---|
| October 30, 6:00 a.m. | Amazon third quarter: AWS growth, RPO, capacity, Trainium | Updates the hyperscaler side of the comparison |
| November 11, 7:00 a.m. | CoreWeave third quarter: active and contracted power, short-term prices, backlog maturity | Short-term prices holding at $40 million per MW-year or more mean SpaceX's pricing is industry-wide. A fall brings SpaceX's repricing risk forward |
| After Alphabet's 10-Q | Backlog maturity, third-party compute commitments, value of its SpaceX stake | Tests the Google link |
| December 31, 2026 | Google contract becomes terminable on 90 days' notice; Apollo lease expected to close; year-end nameplate | First exit window |
| January–March 2027 | Anthropic's SpaceXAI contracts leave their initial non-cancellable periods; any termination notices | Second exit window |
| January–February 2027, date not set | SpaceX fourth-quarter results | Scorecard below |

Our scorecard for SpaceX's fourth-quarter results. The probabilities are our subjective estimates.

| Item | Our base case | Probability | How we will judge it |
|---|---|---:|---|
| Year-end nameplate of 2.5GW or more | Achieved | 75% | 10-K key metrics. The Southaven injunction is the main downside risk |
| Fourth-quarter capital spending of $35–40 billion | In range | 65% | Cash flow statement. Below $35 billion points to supply or power limits |
| After-one-year backlog up 25% or more from $20.8 billion | Not achieved | 30% | Backlog times one minus the within-one-year share |
| Customer B below 30% of revenue | Achieved | 55% | The Google fee and the six-month contracts widen the denominator |
| Apollo lease closes with its rate disclosed | Achieved | 70% | 8-K or 10-K. A rate within 200 bp of the notes' implied 6.9% is a good result |
| No termination notice on a major cloud contract in January–March 2027 | None | 85% | 8-K or 10-Q. A notice confirms the weakness |

**Is a 90-day exit clause in a GPU shortage a weakness or an option? Tell us which renewal you would watch first.**

## Disclosure

We researched and drafted this analysis with AI models made by Anthropic. Anthropic is a SpaceX compute customer, a competitor of Grok, and the filer of an S-1 we cite. We report only Anthropic's public disclosures and do not estimate how its contracts affect SpaceX's revenue or value. We do not link SpaceX's unnamed Customer B to any company.

## Main sources

- [SpaceX 3Q26 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)
- [SpaceX 2Q26 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026052535/spcx-20260630.htm)
- [SpaceX 3Q26 results, 8-K exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066482/spaceexplorationtechnologi.htm)
- [SpaceX prospectus (424B4)](https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm)
- [SpaceX Google cloud agreement filing, June 5, 2026](https://www.sec.gov/Archives/edgar/data/1181412/000162828026041150/spacexagreementfwp.htm)
- [SpaceX 8-K, Apollo GPU finance lease, October 26, 2026](https://www.sec.gov/Archives/edgar/data/1181412/000110465926118614/tm2628247d1_8k.htm)
- [SpaceX 2Q26 company-edited call transcript](https://s21.q4cdn.com/184289198/files/doc_financials/2026/q2/SpaceX-Q2-2026-Earnings_Transcript-FINAL.pdf)
- [SpaceX 3Q26 call transcript, Motley Fool (secondary)](https://www.fool.com/earnings/call-transcripts/2026/10/20/spacex-spcx-q3-2026-earnings-call-transcript/)
- [Anthropic S-1](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm)
- [Alphabet 3Q26 results, 8-K exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm)
- [Alphabet 2Q26 10-Q](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm)
- [Alphabet 3Q26 call summary, MarketBeat (secondary)](https://www.marketbeat.com/earnings/reports/2026-10-28-alphabet-inc-stock/)
- [CoreWeave 2Q26 results](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm)
- [CoreWeave 2Q26 10-Q](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm)
- [CoreWeave release, September 17, 2026](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Continues-to-Contract-New-Compute-Capacity-at-Higher-Prices/default.aspx)
- [Nebius 2Q26 shareholder letter](https://www.sec.gov/Archives/edgar/data/1513845/000110465926094568/tm2622968d1_ex99-2.htm)
- [Oracle 1Q FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm)
- [Nscale S-1](https://www.sec.gov/Archives/edgar/data/2110365/000119312526395475/ck0002110365-20260918.htm)
- [Microsoft FY27 1Q 10-Q](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm)
- [Meta 3Q26 10-Q](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)
- [Amazon 2Q26 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm)

*Research and information only; not investment advice. Rankings compare business structures, not expected returns, and probabilities are our subjective estimates. Figures are date-bound and come from the filings listed above unless marked as our calculation or estimate. AI tools assisted research and editing; see the disclosure above.*
