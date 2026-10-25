---
title: "What Naver and SK Telecom Really Earn From AI Data Centers"
date: 2026-10-25T20:20:00+09:00
categories: ["semiconductors", "market-analysis"]
tags: ["AI Data Centers", "NAVER", "SK Telecom", "SK Horizon", "SK Hyper", "GPUs", "Dunamu", "CoreWeave", "Nebius", "Token Gateway"]
series: ["Korea Semiconductor Watch"]
slug: "naver-sk-telecom-ai-data-center-profits-value-2026-10-25"
description: "Revenue is not profit, and profit is not what shareholders keep. We estimate what Naver's and SK Telecom's AI data centers could add to earnings in 2027 to 2029, and where each company's value really sits."
image: "cover.en.png"
draft: false
---

Our [last post](/post/naver-sk-telecom-ai-data-centers-gpus-funding-2026-10-25/) sorted out what Naver and SK Telecom have really secured: plans, orders, deliveries and money. This post asks the next question. If the projects work, how much profit do they add by 2029? And how much of that profit belongs to each company's shareholders?

Every number below is our own estimate from public filings and company releases up to October 25, 2026. It is not company guidance. We show earnings, shares of value and conditions to watch. We do not give price targets or buy and sell calls.

## Five things to take away

- **Naver's AI data center adds little profit before 2028.** In our base case it earns ₩32bn of operating profit in 2027, ₩314bn in 2028 and ₩558bn in 2029. That is 1.3%, 10.7% and 16.3% of Naver's total operating profit in our model.
- **A higher GPU rental price does not flow straight to profit.** Rental prices for H200 and B200 chips rose about 20% in a month. Our model has Naver pay usage fees to a separate company that holds the data center assets, so the extra price helps Naver only after those fees.[^ornn]
- **SK Telecom's AI data center revenue grows faster than the profit its shareholders keep.** In our base case, related revenue rises from ₩850bn to ₩1.85tn between 2027 and 2029. Profit that belongs to SK Telecom shareholders rises from ₩31bn to ₩154bn, only 3.7% to 8.3% of revenue.
- **Most of each company's value sits elsewhere.** The new AI data center is about a tenth of Naver's value in our base model. For SK Telecom, the telecom business, a stake in Anthropic and the existing data center unit matter more than the new GPU and gigawatt projects.
- **The US neocloud sell-off is a weak guide.** US AI cloud stocks fell 33% to 39% from September 30 to October 23. Naver and SK Telecom fell 11% to 13%. After the US stocks rose, Naver rose in the next Korean session 4 times out of 8 and SK Telecom 3 times out of 8.

## 1. How we turn plans into profit

We start from company targets and turn them into revenue in three steps. First, how many megawatts (MW) of capacity are available on average during the year. Second, how much of that capacity is used by paying outside customers. Third, how much one contracted megawatt earns in a year.

For Naver, the company's roadmap is 55MW from the first half of 2027, about 100MW by the end of 2027 and 200MW in 2028.[^naverstory][^naverroad] The monthly start dates are not public. We assume capacity averages 40MW in 2027, 150MW in 2028 and 200MW in 2029. We do not add the later 1GW expansion.

| Our base case for Naver | 2027 | 2028 | 2029 |
|---|---:|---:|---:|
| Average available capacity | 40MW | 150MW | 200MW |
| Share of capacity in use | 80% | 85% | 90% |
| Share of that use by outside paying customers | 75% | 80% | 85% |
| Outside paying capacity | 24MW | 102MW | 153MW |
| Revenue per contracted MW a year | $20m | $19m | $18m |
| Operating margin after SPV fees and running costs | 5% | 12% | 15% |
| Outside revenue | ₩648bn | ₩2.62tn | ₩3.72tn |

We use ₩1,350 per dollar. Our price path starts from a reference point. Nebius said four large contracts it signed in the second quarter yield $20 million to $25 million per megawatt a year.[^nebiusq2] That is Nebius's contract data, not Naver's price.

The margin is our assumption. Naver has not published a margin for this business or the terms of its costs. We treat 5%, 12% and 15% as the margin left after the usage fees Naver pays to the separate company that holds the data center assets (an SPV), power, staff and other running costs. We do not subtract those fees a second time. The real fee terms are not public.

## 2. Naver: little profit before 2028

<div class="fig-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.4em 0"><img src="/post-assets/naver-sk-telecom-ai-data-center-profits-value-2026-10-25/naver-range.en.svg" alt="Operating profit from Naver's new AI data center in billion won under bear, base and bull scenarios. 2027: bear minus 4.9, base 32.4, bull 172.2, base case 1.3 percent of Naver's total operating profit. 2028: bear 15.4, base 314, bull 873, base case 10.7 percent. 2029: bear 78.3, base 558, bull 1,121, base case 16.3 percent. Capacity averages 40, 150 and 200MW in the base case with operating margins of 5, 12 and 15 percent. Dunamu is not included." loading="lazy" style="display:block;width:100%;min-width:720px;max-width:none;height:auto;margin:0 auto"></div>

The profit comes late for three reasons. In 2027 the average capacity is only 40MW, because the first 55MW starts in the middle of the year. The margin is thin while the business is new. And only part of the capacity serves outside customers. Naver's own use of its AI computing does not create outside revenue in this model.

By 2028 the data center adds about 10.7% to Naver's operating profit in our base case. By 2029 it adds about 16.3%, but only if 200MW runs at 90% use with a 15% margin. The bear case is a small loss of ₩5bn in 2027 and a profit of ₩78bn in 2029. The bull case has ₩1.12tn in 2029. We do not attach probabilities to these cases.

One outside estimate shows how much the margin matters. NH Investment & Securities expects AI Factory revenue of ₩0.73tn in 2027, ₩3.32tn in 2028 and ₩6.51tn in 2029, with operating margins of 5.3%, 6.9% and 8.8%.[^nh] That gives ₩575bn of operating profit in 2029, close to our ₩558bn. Its revenue is higher partly because it assumes 300MW of capacity in 2029, which is NH's assumption and not a Naver target. A higher revenue and a lower margin lead to about the same profit.

**The cost side can also turn negative.** Suppose Naver pays the SPV a fixed fee of $13m per megawatt a year, with $1.2m of variable cost and $1m of other cost, and sells at $18m. Then the business needs about 83% use just to cover its cash costs. At 60% use on 200MW, the yearly cash gap is about ₩1.06tn. This is a stress example, not a contract term. The real fee terms and minimum payments are not public.

## 3. GPU prices rose, but who keeps the gain?

Rental prices for GPUs are strong. The Ornn index of traded prices on October 24 showed a one-month rise of 20.2% for H200 and 19.5% for B200. H100 rose 3.4%, A100 5.9%, and the RTX PRO 6000 was flat.[^ornn] Investor a16z published a chart on October 23 that compares today's rental prices with a straight-line six-year depreciation line. Prices sit from 9% to 143% above that line, depending on the chip.[^a16z] That is a gap to a reference line, not a return on a chip.

<div class="fig-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.4em 0"><img src="/post-assets/naver-sk-telecom-ai-data-center-profits-value-2026-10-25/gpu-price.en.svg" alt="Left: one-month change in the Ornn GPU price index on October 24: H200 plus 20.2 percent, B200 plus 19.5, A100 plus 5.9, H100 plus 3.4, RTX PRO 6000 zero. Right: Naver AI data center operating profit in billion won. 2028: old price path 314, higher price path with the same margin 413, higher price with the operator keeping 30 percent of the uplift 562. 2029: 558, 713 and 868. The old price path is 20 to 18 million dollars per MW-year, the higher path 25 to 23 million dollars." loading="lazy" style="display:block;width:100%;min-width:720px;max-width:none;height:auto;margin:0 auto"></div>

We tested what a higher price path does. We raised revenue per contracted megawatt from $20m, $19m and $18m to $25m, $25m and $23m. If Naver kept the same margin, 2028 operating profit would rise from ₩314bn to ₩413bn. If Naver kept 30 cents of every extra revenue dollar as profit, instead of the 12 cents its margin implies, it would be ₩562bn.

There are two reasons not to push this further. First, Nebius separates its contract yield of $20m to $25m from a premium price range of $40m to $50m per megawatt, and says it had signed only the first contract in that range.[^nebiusq2] A premium for scarce new chips does not set a three-year price. Second, Naver does not own the whole stack. If the SPV raises its fee when customer prices rise, Naver's profit barely moves. The profit that counts is extra customer revenue minus extra fees and extra running cost.

## 4. Naver's other swing factors

**The existing business is the larger swing.** In the second quarter, revenue excluding the Wallapop acquisition grew 14.5%, platform revenue grew 12.3% and advertising grew 7.5%. Operating profit was flat from a year earlier, as spending on computing assets, content and data rose.[^naverir] Our base case slows the existing business to 8%, 7% and 6% growth. A faster path of 12%, 10% and 8% is reasonable but not our base case. Korea Investment & Securities pointed to delays in tenant announcements, a slower advertising and commerce quarter around the Chuseok holiday, and higher costs for payment terminals, broadcast rights and GPU depreciation.[^kis]

One more point sets the scale. In our model, one turn of the earnings multiple on Naver's existing business moves value by about ₩2.0tn. That is about 60% of the value of the whole AI data center (about ₩3.2tn). A one-turn change on the old business is worth more than half of the new project.

**Dunamu adds profit to Naver's group, but not all of it to Naver's shareholders.** Naver Financial plans to take 100% of the crypto exchange operator Dunamu in a share exchange. Naver's holding in Naver Financial would fall from 69.0% to 17.0%. Naver would hold 46.5% of the voting rights including delegated votes, and plans to keep consolidating Naver Financial and, through it, Dunamu. The final control test comes at closing. The deal values 100% of Dunamu at ₩15.1tn. That is a share value, not cash coming to Naver. The chart is dated September 30, 2025, and the holdings can change if shareholders use appraisal rights.[^naverpres]

The arithmetic for shareholders is simple. Naver's yearly gain is 17% of Dunamu's net profit minus the 52 percentage points of Naver Financial's own profit it gives up. Dunamu earned ₩708.9bn in 2025.[^dunamu25] Naver Financial's own profit is about ₩133.5bn by our proxy from a secondary summary of its audit report. With those numbers the gain is about ₩51bn a year. But Dunamu earned only ₩108.4bn in the first half of 2026.[^dunamu1h] Doubling that number turns the gain into a loss of about ₩33bn. Dunamu would need to earn about ₩408bn a year for the swap to add to Naver's profit. We did not find a confirmed closing in the filings we checked. Our model assumes the end of March 2027 and adds no synergy from stablecoins, payments or tokenization.

## 5. SK Telecom: revenue grows faster than shareholder profit

SK Telecom's AI data center business is not one business. It combines three parts. SK Horizon owns existing data centers and subsea cables, and is being split off with outside investors. GPU services rent computing to customers. SK Hyper develops new gigawatt-scale sites. SK Telecom reported AI data center revenue of ₩131.4bn in the first quarter of 2026 and ₩136.2bn in the second.[^skt2q]

<div class="fig-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.4em 0"><img src="/post-assets/naver-sk-telecom-ai-data-center-profits-value-2026-10-25/skt-funnel.en.svg" alt="SK Telecom AI data center related business in our base case, billion won. 2027: revenue 850, operating profit 146, profit to SKT shareholders 31.3, which is 3.7 percent of revenue. 2028: revenue 1,250, operating profit 230, to SKT holders 58.9, 4.7 percent. 2029: revenue 1,850, operating profit 400, to SKT holders 154, 8.3 percent. Horizon is counted at SKT's 51 percent economic stake after the deal; revenue and operating profit are shown at 100 percent." loading="lazy" style="display:block;width:100%;min-width:720px;max-width:none;height:auto;margin:0 auto"></div>

| Our base case, ₩bn | 2027 | 2028 | 2029 |
|---|---:|---:|---:|
| Horizon revenue / operating margin | 550 / 25% | 700 / 27% | 900 / 28% |
| GPU services revenue / operating margin | 300 / 8% | 550 / 12% | 850 / 15% |
| SK Hyper fees / operating profit | 0 / −15 | 0 / −25 | 100 / 20 |
| Total revenue | 850 | 1,250 | 1,850 |
| Total operating profit | 146 | 230 | 400 |
| Profit to SK Telecom shareholders | 31 | 59 | 154 |
| Share of SK Telecom's total operating profit | 7.4% | 11.0% | 17.5% |
| Share of SK Telecom's shareholder profit | 2.3% | 4.1% | 10.0% |

Three things pull shareholder profit far below operating profit. First, Horizon's revenue and operating profit are counted in full, but after the deal SK Telecom keeps only 51% of its net profit. KKR and a group led by IMM Investment pay about ₩3.08tn for the rest. Of that, about ₩1.88tn buys existing shares from SK Telecom and about ₩1.2tn is new money for Horizon. The sale is planned for March 4, 2027, subject to conditions.[^horizon][^skt6k] Second, interest and tax come before shareholders. Third, GPU services start with a low margin, and SK Hyper starts as a cost.

Compared with our 2026 estimate of about ₩53bn of shareholder profit from this business, 2027 is lower by about ₩21bn. **Revenue can grow while the profit a shareholder can claim falls in the first year.** The ₩1.88tn from selling existing shares is cash, not profit. We treat it as capital that SK Telecom can reuse, and we do not add it to earnings.

SK Hyper is still mostly a plan. SK Telecom may invest up to ₩750bn by 2030 for sites and substations. The first 5GW is planned in phases from 2029, and the company says it plans to expand toward 15GW in 2035.[^hyper] In an October 13 filing, the company said it has no concrete plan to add another 5GW overseas, after a news report said it was considering one.[^dartclar] We include no computing revenue from the 5GW. We include only an assumed ₩100bn of development and operating fees in 2029.

## 6. A token gateway: an option, not in our base case

On October 25, ZDNet Korea reported that SK Telecom is preparing a "token gateway." The service would manage which AI model a customer uses, how much it uses and what it costs, and would set what work the AI may handle. It would use SK Telecom's identity, payment and billing capabilities. The article says the company has not set a launch date or prices.[^zdnet]

This idea deserves attention because it adds demand without owning more GPUs. It also faces a hard question. Similar services already exist. Amazon Bedrock routes requests between models in the same model family, and Cloudflare AI Gateway offers usage logs, caching, rate limits, retries and model fallback.[^aws][^cloudflare] SK Telecom would have to show an edge in business integration, access control, support and switching costs. ZDNet cites SK Telecom's 23 million subscribers as an asset. They are telecom customers, and nothing shows they will pay for AI services.

We put zero value on it in our base case. To see the size, we tested two cases. In the proof case, 500,000 consumers pay ₩120,000 a year and 1,000 companies pay ₩50m, for ₩110bn of net fee revenue. In the expansion case, 1 million consumers pay ₩180,000 and 3,000 companies pay ₩100m, for ₩480bn. At 25% to 30% margins and a 20 times earnings multiple, discounted at 12%, these cases add ₩0.29tn and ₩1.51tn. That is about 1.5% and 7.7% of our base value. These cases are not company forecasts. Token purchases that SK Telecom passes on to model makers would not count as its own revenue.

## 7. Where the value sits

<div class="fig-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.4em 0"><img src="/post-assets/naver-sk-telecom-ai-data-center-profits-value-2026-10-25/value-sits.en.svg" alt="Where the value sits in our base models. Naver: existing business 90 percent, new AI data center 10 percent; of the AI data center part, 18 percent is earnings and cash from 2027 to 2029 and 82 percent is value after 2029. SK Telecom: telecom and other business 68.9 percent, SK Horizon 51 percent stake 14.2, cash from the Horizon share sale 7.1, Anthropic stake at 65 percent of book value 11.7, GPU services net of capital minus 1.3, SK Hyper net of outlays minus 0.5. Naver's AI part is about 10 percent in the earlier model and 12 to 14 percent in the later one." loading="lazy" style="display:block;width:100%;min-width:720px;max-width:none;height:auto;margin:0 auto"></div>

**Naver.** About 10% of base value comes from the new AI data center, or 12% to 14% under the higher price paths. Of that part, 82% is value after 2029. Only 18% comes from earnings and cash in 2027 to 2029. That makes the AI part sensitive to renewals, equipment replacement and whether profits last. Naver's existing business, and the multiple the market gives it, matter more.

**SK Telecom.** About 69% of base value comes from telecom and other existing business. SK Horizon accounts for about 14%, and the cash from the share sale for about 7%. The Anthropic stake adds about 12%. SK Telecom holds 3,860,330 shares, rounded to 0.2%, with a book value of ₩3.5tn at the end of June.[^dart] We count it at 65% of book value because it is unlisted, can be diluted and is hard to cash out. A book-value gain is not cash. The new GPU services and SK Hyper together are slightly negative after we subtract the capital they need.

**SK Telecom's first half gives a baseline.** Operating profit was ₩1.10tn on revenue of ₩8.75tn. Second-quarter mobile revenue fell 1.9% from a year earlier on fewer subscribers, and the strong profit growth reflects the base effect from last year's USIM replacement costs.[^sktir] The company paid a dividend of ₩830 per share in each of the first two quarters of 2026. It has not promised the same for later quarters.

## 8. Did the US neocloud sell-off drag them down?

<div class="fig-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.4em 0"><img src="/post-assets/naver-sk-telecom-ai-data-center-profits-value-2026-10-25/spillover.en.svg" alt="Price change from Sep 30 to Oct 23 close in local currency: IREN minus 39.1 percent, CoreWeave minus 37.7, Nebius minus 32.7, KOSPI minus 18.8, SK Telecom minus 13.4, Kakao minus 11.3, Naver minus 10.8, KT minus 10.5, QQQ minus 4.8, LG Uplus minus 2.5. After the US basket of CoreWeave and Nebius rose, in the last month (8 times), Naver rose in the next Korean session 4 of 8 times and SK Telecom 3 of 8." loading="lazy" style="display:block;width:100%;min-width:720px;max-width:none;height:auto;margin:0 auto"></div>

Possibly in part, but the evidence does not show it was the main cause. Reuters reported on October 14 that bets on higher US interest rates deepened concerns about the financing of AI infrastructure companies.[^reuters] On October 19, the Dong-A Ilbo tied Naver's funding plan to CoreWeave's debt worries. It reported, citing industry sources, a draft plan to raise up to $9bn (about ₩12tn) from outside investors who would earn about 9% a year over six years. Naver told the paper that the structure was still under discussion and that its fundamentals differ from CoreWeave's.[^donga] That is a plausible path from US stocks to Naver, and it is not a confirmed contract.

The prices say the link is loose. Naver fell about the same as Kakao and less than the KOSPI, so neoclouds alone do not explain the fall. Following US days when CoreWeave and Nebius rose, Naver rose in the next Korean session 4 times out of 8 and SK Telecom 3 times out of 8. On October 19 the US basket rose 1.2%, and Naver fell 2.7% on October 20. The correlation is positive, at +0.32 for Naver and +0.42 for SK Telecom in the last month. After we remove the Korean market and the Nasdaq-100 ETF (QQQ), it drops to between +0.06 and +0.26 for Naver and between +0.13 and +0.23 for SK Telecom. Eight observations cannot give a probability.

A US rebound would help only in some forms. A bounce after oversold trading proves little. A fall in interest rates and credit spreads, together with Naver's financing close and customer contracts, would prove more. Even a 20% rise in the value of Naver's AI data center would raise our total value for Naver by only about 2.4% to 2.9%, if nothing else changed.

## 9. What would change our view

| What to check | Why it matters |
|---|---|
| Nvidia's $1bn share payment for Naver (latest date October 30) and the Brookfield financing close[^kind][^brookfield] | Turns conditional money into money received |
| Naver's first outside customers, the length of the contracts, minimum payments and the SPV fee | Decides whether a higher GPU price reaches Naver's profit |
| The month Naver's first 55MW starts and Naver's next earnings | Tests our 2027 capacity and margin assumptions |
| SK Telecom's Horizon shareholder meeting, split and share sale (planned January to March 2027) | Decides the 51% stake and the cash |
| SK Hyper's outside investors, SK Telecom's guarantees and any minimum lease obligations | Shows how much risk stays with SK Telecom |
| SK Telecom's third-quarter AI data center revenue, margin and capital spending, and its 2027 shareholder return policy | Tests our ₩850bn revenue and 3.7% profit ratio |
| Whether the token gateway launches, with prices and paying customers | Turns an option into revenue |

## Conclusion: profit arrives later and is smaller than revenue

Revenue from AI data centers will arrive sooner than profit. For Naver, the profit grows from 2028 and depends on prices, fees and use. For SK Telecom, the profit is diluted by the Horizon deal and early costs. For both companies, the existing business, the multiple the market pays for it and a few large assets decide most of the value.

Four things would make us more positive: signed contracts with minimum use, money actually received, margins that survive the fees, and falling credit costs. The token gateway for SK Telecom and Dunamu for Naver are options, and they count only after they show up in results.

[^ornn]: [Ornn GPU price index](https://data.ornn.com/), updated 2026-10-24 20:00 UTC: H100 SXM $3.02 an hour (+3.42% over one month), H200 $6.20 (+20.16%), B200 $9.57 (+19.48%), A100 SXM4 $1.08 (+5.88%), RTX PRO 6000 $1.55 (0.00%). A limited sample of traded prices.
[^a16z]: [a16z, Charts of the week](https://www.a16z.news/p/charts-of-the-week-attention-is-all), 2026-10-23: prices "anywhere from 9% higher to 143% higher" than a straight-line six-year depreciation baseline. An investor's reading, not a return on equipment.
[^naverstory]: [NAVER story](https://navercorp.com/en/story/storyDetail?seq=10034603), 2026-07-24: 55MW from the first half of 2027, 200MW in 2028.
[^naverroad]: [NAVER story](https://www.navercorp.com/en/story/storyDetail?seq=10034410): roadmap of 55MW, 100MW and 200MW. The monthly schedule and the 2029 level are our assumptions.
[^nebiusq2]: [Nebius second-quarter 2026 shareholder letter](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf): four large contracts at a yield of $20 to $25 million per megawatt; a "$40-50 million per MW" price opportunity, with the first such contract signed that week.
[^nh]: [NH Investment & Securities, NAVER, 2026-10-01](https://download.nhqv.com/CommFile/cis/rsh/epr/CISPPR20260930175105995.pdf), pp. 25 and 30: AI Factory revenue ₩730bn, ₩3,320bn and ₩6,510bn and operating profit ₩38.7bn, ₩228.5bn and ₩574.8bn for 2027 to 2029; data center capacity of 100, 200, 300 and 400MW for 2027 to 2030. These are NH's estimates and assumptions.
[^naverir]: [NAVER second-quarter 2026 IR presentation](https://www.navercorp.com/api/article/download/07b3b329-bbbe-481c-ac47-b3d0d7fea855): revenue excluding Wallapop +14.5%, platform +12.3%, advertising +7.5% from a year earlier; operating profit flat as costs rose on computing assets, content and data.
[^kis]: [Korea Investment & Securities, 3Q26 preview](https://m.koreainvestment.com/main/research/research/StrategyDetail.jsp?id=159813&jkGubun=6), 2026-10-01. In Korean.
[^naverpres]: [NAVER shareholder presentation on the Dunamu deal](https://navercorp.com/api/article/download/61f86393-5464-43fa-b7ae-8234c399d168): Naver's holding in Naver Financial from 69.0% to 17.0%; 46.5% of voting rights including delegation; Dunamu 100% share value ₩15.1tn; exchange ratio 3.06 to 1. The shareholding may change if appraisal rights are exercised.
[^dunamu25]: [ZDNet Korea](https://zdnet.co.kr/view/?no=20260330182616), 2026-03-30: Dunamu consolidated net income of ₩708.9bn for 2025. In Korean.
[^dunamu1h]: [Financial News](https://www.fnnews.com/news/202608141738241349), 2026-08-14: Dunamu first-half 2026 net income of ₩108.4bn. In Korean.
[^skt2q]: [SK Telecom second-quarter 2026 results](https://news.sktelecom.com/en/3218), 2026-08-05: AI data center revenue ₩136.2bn, up 92.5% from a year earlier; first quarter ₩131.4bn.
[^horizon]: [SK Telecom newsroom](https://news.sktelecom.com/en/3290), 2026-08-27: SK Horizon to be set up in the first quarter of 2027; 318MW including eight existing data centers and sites under construction; stakes of 51%, 29% and 20%.
[^skt6k]: [SK Telecom Form 6-K](https://www.sec.gov/Archives/edgar/data/1015650/000119312526369453/d120053d6k.htm), 2026-08-27: 24,481,427 existing shares sold for ₩1,881,128,369,253; 15,617,069 new shares for about ₩1.20 trillion; scheduled disposal date 2027-03-04.
[^hyper]: [SK Telecom newsroom](https://news.sktelecom.com/en/3192), 2026-07-23: SK Hyper set up; ₩750bn by 2030; phased opening of 5GW in 2029; sequential expansion toward 15GW in 2035.
[^dartclar]: [SK Telecom clarification filing on DART](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261013800718), 2026-10-13: no concrete plan at present for an overseas 5GW addition, in reply to a news report. The 15GW figure is a long-term plan under review. In Korean.
[^zdnet]: [ZDNet Korea](https://zdnet.co.kr/view/?no=20261024132650), published 2026-10-25: token gateway to manage model choice, usage, cost and the scope of work given to AI; launch date and pricing not disclosed. In Korean.
[^aws]: [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html): prompt routing between foundation models of the same family.
[^cloudflare]: [Cloudflare AI Gateway documentation](https://developers.cloudflare.com/ai-gateway/): analytics and logging, caching, rate limiting, request retries and model fallback.
[^dart]: [SK Telecom half-year report on DART](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260813001728), 2026-08-13: Anthropic 3,860,330 shares, 0.2%, book value ₩3,505,017 million. In Korean.
[^sktir]: [SK Telecom second-quarter 2026 investor briefing](https://www.sktelecom.com/img/eng/presen/2026/2Q26InvestorBriefingENG.pdf): first-half revenue ₩8,751.4bn and operating profit ₩1,103.6bn; second-quarter mobile revenue down 1.9% on fewer subscribers; dividend ₩830 per share in each of the first and second quarters.
[^reuters]: [Reuters via Investing.com](https://www.investing.com/news/economy-news/ai-infrastructure-firms-slump-as-us-rate-hike-bets-rise-4949759), 2026-10-14: AI infrastructure stocks fall as expectations of higher US rates deepen financing concerns.
[^donga]: [Dong-A Ilbo](https://www.donga.com/news/Economy/article/all/20261019/134863396/2), 2026-10-19, citing unnamed industry sources: up to $9bn (about ₩12tn) of outside funding in a draft structure; Naver said the structure is still under discussion. In Korean.
[^kind]: [NAVER disclosure of the share issue to Nvidia (KIND)](https://kind.krx.co.kr/external/2026/07/27/000002/20260727000004/11306.htm), 2026-07-27: about $1 billion, on condition that NAVER secures at least $9 billion of computing infrastructure; October 30, 2026 is the latest payment date and can be changed.
[^brookfield]: [NAVER press release](https://www.navercorp.com/en/media/pressReleasesDetail?seq=10034687), 2026-09-04: Brookfield "has committed to investing up to US$9 billion" in the 200MW first phase of a 1GW AI factory project.
[^interest]: [The Korea Economic Daily (KED Global)](https://amp.kedglobal.com/newsAmp/ked202308130002), 2023-08-13, on SK Telecom's investment in Anthropic; [OpenAI](https://openai.com/index/samsung-and-sk-join-stargate), 2025-10-01, on exploring AI data centers in Korea with SK Telecom.

*Interest note: We use AI models, including Anthropic's Claude and OpenAI's models, in our research. SK Telecom holds a stake in Anthropic, which we count in SK Telecom's base value at 65% of book value, and OpenAI has announced plans to explore AI data centers in Korea with SK Telecom. We cite public figures only and make no judgment about the effect on either company.*[^interest]

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
