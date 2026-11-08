---
title: "AI is raising the price of every ad: Meta's 14% and AppLovin's 55% come from the same law, and agents decide the next round"
date: 2026-11-08T19:45:00+09:00
lastmod: 2026-11-08T19:45:00+09:00
categories: ["Tech-Analysis", "market-analysis"]
tags: ["Meta", "META", "AppLovin", "APP", "Unity", "Alphabet", "Digital Advertising", "AI Advertising", "Recommendation Systems", "GEM", "Agentic Commerce", "Q3 2026"]
series: ["exclusive-analysis"]
slug: "ad-ai-scaling-law-price-per-ad-meta-applovin-agents-2026-11-08"
description: "Ad engines at Meta, AppLovin and Unity got more accurate because recommendation models now scale with compute, generalize to sparse data and take over advertiser decisions. Where ad money goes next, and what agents change."
image: "cover.en.png"
draft: false
---

In the third quarter, Meta served 10% more ad impressions than a year earlier, and the average price per ad rose <strong>14%</strong>. This is the first time since 3Q25 that price growth beat impression growth. In the same quarter AppLovin's installs grew 2% while its net revenue per install grew <strong>55%</strong>. Unity's ad model, Vector, grew 40% from the prior quarter.

The companies that grew fastest did not sell many more ads. They sold each ad for more. Advertisers pay more because the ads fit better. In an October engineering post, Meta said its ads foundation model GEM raised conversions by 18.9% and click-through rate by 12% across its ad surfaces.

Our [AppLovin and Unity earnings post](/post/applovin-unity-3q26-prediction-model-step-up-price-per-install-2026-11-08/) traced both beats to a step up in their prediction models. This follow-up uses Meta's primary sources to explain why these models became more accurate now, and judges what that means for the ad industry.

<strong>Our view: ad prediction models got more accurate because model size, the ability to reuse what a model learns, and the decisions advertisers hand over all grew at once. Before 2024, adding compute to recommendation models did little. Now accuracy rises predictably as the models grow. In advertising, AI therefore raises the value of each ad more than the number of ads, and money gathers in a few engines that run the auction and see the conversion outcome. Compute can be bought; outcome data cannot. The size of outcome data decides the winners in 2027 and 2028. The variable that could overturn this view is agents. If the purchase decision moves from feeds and search to personal agents, outcome data changes owner.</strong>

## A short glossary

| Term | Plain meaning |
|---|---|
| Prediction model (ad engine) | The AI that estimates, for each ad slot, how likely this person is to act on this ad, and sets the bid. Meta's GEM, AppLovin's Axon and Unity's Vector are examples. |
| Conversion | The action the advertiser wants after the ad: an install, a purchase, a sign-up. |
| Scaling law | The rule that performance improves at a predictable rate as compute, model size and data grow. It was first shown for large language models (LLMs). |
| Foundation model | A large central model that teaches many smaller task models. GEM is Meta's foundation model for ads. |
| Knowledge transfer (distillation) | Moving what a large model learned into small, fast, cheap models. |
| Outcome data | The record of whether an install or purchase actually happened after the ad. The model learns again only when this record comes back. |
| Annual run-rate | Recent quarterly or monthly revenue scaled up to a full year. |
| Agentic commerce | AI agents that find, compare and pay for products on a person's behalf. |

## Growth came from the value of each ad, not the number of ads

Ad revenue is the number of ads times the value of each ad. Meta discloses the growth of both every quarter. Set the quarters since 3Q25 side by side and the weight of growth moves toward price.

| Meta | 3Q25 | 4Q25 | 1Q26 | 2Q26 | 3Q26 |
|---|---:|---:|---:|---:|---:|
| Ad revenue | $50.1B | $58.1B | $55.0B | $59.4B | $63.1B |
| Ad revenue growth | +26% | +24% | +33% | +27% | +26% |
| Ad impression growth | +14% | +18% | +19% | +14% | +10% |
| Price per ad growth | +10% | +6% | +12% | +12% | +14% |
| Share of growth from price (our calculation) | 42% | 26% | 39% | 46% | 58% |

![Growth came from the value of each ad, not the number of ads. Meta's ad impression growth from 3Q25 was 14, 18, 19, 14 and 10%, and price per ad growth was 10, 6, 12, 12 and 14%. The share of growth from price was 42, 26, 39, 46 and 58%. AppLovin's installs grew 2% and net revenue per install 55% in 3Q26, so 96% of its growth came from price.](/post-assets/ad-ai-scaling-law-price-per-ad-meta-applovin-agents-2026-11-08/growth-from-price.en.svg)

Meta's impression growth fell from 19% in 1Q26 to 10% in 3Q26. Its ad revenue growth barely slowed, at 27% in 2Q26 and 26% in 3Q26. Price filled the gap. AppLovin is the extreme case: almost all of its revenue growth (96% by our calculation) came from the value of each install. AppLovin's two figures multiply to about 3 points more than its revenue growth, so we use this value only to read direction.

Meta named both better ad performance and better macro conditions than a year ago as reasons for the higher price, and did not split the two. The 1Q26 and 2Q26 prices also include a currency tailwind. So the whole price share cannot be read as AI's share. Still, Meta's CFO said on the 3Q25 call that value-weighted conversions were growing faster than impressions. Advertisers are getting more results from the same impressions.

Google Search looks different. In 3Q26 Google Search revenue grew 12.0%, paid clicks grew 8% and cost per click grew 4%. As our [October 30 post](/post/meta-ad-edge-google-amazon-share-shift-2026-10-30/) showed, Meta took 57% of the combined ad revenue increase of Meta, Google and Amazon in the quarter.

## Since 2024, recommendation models also get more accurate as they grow

To see why accuracy rose now, start before 2024. In a 2024 paper (HSTU), Meta researchers wrote that most industry recommendation models, trained on thousands of features, failed to scale with compute. The models were also split finely by surface and objective. Since 2023 alone, Meta has folded about 100 ad ranking models into larger ones.

The paper recast recommendation as a generative task, predicting the next action the way a language model predicts the next word. A model with 1.5 trillion parameters improved metrics by 12.4% in online tests. Model quality rose as a power law of training compute across three orders of magnitude. Another Meta paper the same year (Wukong) found the same law across two orders of magnitude of model complexity.

GEM brought this finding into ads. In November 2025 Meta introduced GEM as the industry's largest foundation model for recommendation. It trains on thousands of GPUs and, Meta said, is 4x more efficient at driving ad performance than its earlier ranking models for the same data and compute. In 2Q25 it lifted ad conversions by 5% on Instagram and 3% on Facebook Feed.

Since then Meta has changed its ad models one step every quarter.

![Meta changed its ad models one step every quarter. In 3Q25 Lattice extended to app ads and Andromeda merged stages, lifting app ad conversions about 3% and Facebook ads quality 14%. In 4Q25 GPUs for GEM training doubled and Facebook ad clicks rose 3.5%. In 1Q26 adaptive ranking lifted conversion rates on major surfaces 1.6%. In 2Q26 the Generative Recommender arrived and Facebook conversions rose 15.7%. In 3Q26 a wider GEM lifted app ad conversions 9.6%.](/post-assets/ad-ai-scaling-law-price-per-ad-meta-applovin-agents-2026-11-08/meta-model-ladder.en.svg)

In 3Q25 Meta extended its unified Lattice architecture to app ads and lifted conversions by about 3%. In 4Q25 it doubled the GPUs used to train GEM. In 2Q26 it introduced the Generative Recommender, which uses LLMs to reason over ad content and user preferences, and called it a paradigm shift in how its ads system works. Each effect applies to a specific surface and objective, so they cannot be added. The direction is clear: a few percent of conversion gains stacked up every quarter.

Meta's GEM follow-up post on October 13 puts numbers on the mechanism. Over the past 12 months Meta raised training compute 4x, and model complexity is now 2.5x that of earlier GEM versions. The new architecture delivered twice the performance of the previous one at the same compute. Meta also found that prediction quality follows a power law in the length of a user's behaviour history.

![Recommendation models now improve as they grow. Over the past 12 months Meta raised GEM's training compute 4x, and model complexity is 2.5x that of earlier GEM versions. Bigger models make longer behaviour histories useful, and accuracy follows a power law in history length. Conversions rose 18.9% and click-through rate 12% across surfaces, and the extra ad revenue pays for the next round of compute.](/post-assets/ad-ai-scaling-law-price-per-ad-meta-applovin-agents-2026-11-08/scaling-loop.en.svg)

The two laws reinforce each other. Bigger models gain more from longer histories, and longer histories justify bigger models. This is why Meta said on its 3Q25 call that its ads business runs in a compute-starved state. On the 3Q26 call, Zuckerberg said Meta has not yet found the limit of how effectively it can apply compute to its core business.

For investors, the change reads like this. Ad accuracy has become something you can buy with compute. Gains arrive in steps each time a new model ships, and the timing of the next step moves quarterly numbers. AppLovin's weak 2Q26 and strong 3Q26 follow the same pattern.

## The models now fit small advertisers and new posts too

The second effect of large models is generalization. Meta says GEM transfers what it learns from click prediction, where data is rich, to conversion prediction, where data is sparse. Clicks pile up every day; purchases are rare. To predict rare events, a model must borrow from common ones.

Other companies show the same effect. AppLovin's CEO said the next-generation model improved most in data-sparse segments: new and small advertisers and new categories. AppLovin's install growth moved from -18% in 1Q26 and -2% in 2Q26 to +2% in 3Q26. Unity's advertiser accounts grew 27% from the prior quarter.

Meta's generative retrieval works in the same direction. In organic recommendations it labels posts with semantic representations, so the system can recommend new posts before they gather engagement. In ads, Meta applied its Generative Recommender, which uses LLMs to reason over ad content and user preferences, to the retrieval stage of Facebook Feed ads, lifting conversions by nearly 2% in targeted segments in 3Q26.

This widens the market. Small advertisers and new products that lacked the data to run efficient ads can now enter the auction. Meta estimates that at least 500 million small businesses use its apps to reach customers. Ad market growth no longer depends only on large advertisers raising budgets.

## The big model learns; small models serve each ad in real time

Large models bring a cost problem. Every ad request must be ranked in a very short time. Meta has said on several calls that it does not use large models such as GEM for live inference because they are too expensive.

Instead Meta moves what GEM learns into hundreds of small serving models. Beyond distillation, where small models learn from the big model's answers, Meta now passes the big model's internal representations and doubled the transfer effect. It also built a system that precomputes the big model's work just before a request arrives. In 1Q26 Meta extended a ranking model that assigns heavy compute only to requests likely to convert to offsite conversion ads, lifting conversion rates across major Facebook and Instagram surfaces by 1.6%.

![The big model learns; small models serve each ad in real time. The central foundation model GEM trains on thousands of GPUs but is not served live. Distillation, structured representations and precomputation move its knowledge into hundreds of serving models. Representations learned on data-rich clicks are used for data-sparse conversions, and AppLovin's new model also gained most with new and small advertisers.](/post-assets/ad-ai-scaling-law-price-per-ad-meta-applovin-agents-2026-11-08/teacher-student.en.svg)

This design keeps serving costs small relative to revenue. In 3Q26 AppLovin's cost of revenue rose only $0.06 to $0.09 for each extra dollar of revenue, and 87% of its revenue increase became adjusted EBITDA. In 4Q25 Meta made its ad retrieval engine Andromeda run on Nvidia, AMD and its own MTIA chips and nearly tripled its compute efficiency. In 3Q26 Meta began moving content-understanding models onto its own Muse models, which cut per-unit processing cost by more than 80% in offline tests.

This is why ad AI is the first AI investment to pay. Training is expensive but is spread over billions of people's ad requests, and small models serve cheaply.

## Advertisers are handing targeting and creative to the engine

The last ingredient of accuracy is the advertiser's choice. When advertisers decide whom to reach, where, and with which creative, the model has little room to choose. When advertisers hand these decisions to the engine, the model picks from many more combinations.

![Advertisers are handing targeting and creative to the engine. Advantage+ automated campaigns grew from a $60 billion annual run-rate in 3Q25 to over $75 billion in 2Q26. Advertisers using generative AI creative tools grew from over 8 million in 1Q26 to about 10 million in 3Q26. Creator partnership ads grew from a $10 billion run-rate in 1Q26 to over $15 billion in 3Q26.](/post-assets/ad-ai-scaling-law-price-per-ad-meta-applovin-agents-2026-11-08/automation-adoption.en.svg)

The annual run-rate of Meta's automated Advantage+ campaigns rose from $60 billion in 3Q25 to over $75 billion in 2Q26. Nearly 10 million advertisers used at least one generative AI creative tool in 3Q26. More creative means a better fit for each person. Meta estimates that advertisers who adopted its business AI assistant's advice got about 5% more conversions at the same cost per conversion and raised ad spend by 9% compared with similar non-adopters.

Measurement moved to the engine too. Meta's incremental attribution, described on its 4Q25 call, targets the conversions an ad actually adds. Meta said the model drove 24% more incremental conversions than its standard attribution model.

Google is moving the same way. When it added exploration to Smart Bidding in May 2025, Google said campaigns using it saw 19% more conversions on average, based on its internal data.

## Cash from ads goes into bigger AI

The money ad AI makes is large and visible. On its 3Q26 call Meta said its AI investments already deliver substantial incremental ad revenue. But the cash goes somewhere much bigger than ad models.

![Cash from ads went into bigger AI infrastructure. Meta's quarterly ad revenue grew from $50.1 billion in 3Q25 to $63.1 billion in 3Q26. Over the same period capital expenditure rose from $19.4 billion to $34.9 billion, and free cash flow fell from $10.6 billion to minus $2.1 billion.](/post-assets/ad-ai-scaling-law-price-per-ad-meta-applovin-agents-2026-11-08/meta-capex-fcf.en.svg)

Meta's quarterly capital expenditure rose from $19.4 billion to $34.9 billion in a year, and free cash flow went from $10.6 billion to minus $2.1 billion. Its 2026 capex plan is $135 billion to $145 billion. On the 2Q26 call Meta said a substantial amount of its compute goes to training models to be a leading lab. In late October it also raised outside capital by issuing common stock and mandatory convertible preferred stock.

Investors should separate two returns. The return on ad AI is already visible in the numbers. The return on frontier models and the personal agent Muse is not yet visible. The ad business funds the second bet.

The two bets also meet. On the 3Q26 call Zuckerberg said Meta built an evaluation of how well its newest model, Muse Wonder, can autonomously improve the recommendation and ads systems. He expects the rate of improvement to rise as new models arrive. If AI starts improving ad AI, the cycle between model steps could shorten. For now this is the company's expectation, not a measured result.

We also share new analyses on Telegram as they are published. You are welcome to join us at [@korea_invest_insights](https://t.me/korea_invest_insights).

## Ad money is gathering in engines that own outcome data

In its June forecast, WPP Media expected global ad revenue to grow 8.9% in 2026 to about $1.3 trillion, excluding US political ads, up from the 7.1% it forecast in December. The same report said Alphabet, Meta and Amazon control 57.6% of the market outside China, and no traditional media owner is in the global top ten.

![Growth in ad-related revenue in 3Q26: AppLovin revenue 55%, Reddit ad revenue 54%, Meta ad revenue 26%, Pinterest revenue 12%, Amazon ad revenue 11%, Google ad revenue 10.6%, Omnicom organic 7.2%, Publicis organic 5%, The Trade Desk 2Q revenue 3%, WPP net revenue minus 2.1%. Agencies and open-web buying platforms grew slowest.](/post-assets/ad-ai-scaling-law-price-per-ad-meta-applovin-agents-2026-11-08/growth-compare.en.svg)

Side by side, 3Q26 growth rates differ widely inside the ad market. Platforms that run the auction and see outcomes sit at the top. Agencies and open-web buying platforms, which buy space on behalf of advertisers, sit at the bottom. Google and Amazon trail Meta for their own reasons: Google's search clicks grew less, and Amazon's Prime Day moved into 2Q.

- Reddit's ad revenue grew 54%, and the company named both pricing and impressions as drivers. Revenue per user grew 36%.
- The Trade Desk grew revenue 3% in 2Q26 and guided 3Q revenue to at least $650 million, below its 2Q level. It reports 3Q on November 9 (US time).
- Agencies are not moving in one direction. Omnicom grew 7.2% organically and Publicis 5%. WPP's net revenue fell 2.1%, with its creative business down 5.1%.

We think creative production and manual targeting lose value first inside agency work, because engines now make the creative and pick the audience. Agencies that shifted to media buying and data are still growing. It is too early to read AI's impact from agency results alone; Omnicom's 3Q also includes World Cup and US midterm spending (per secondary reports).

Search faces structural pressure. Google said search queries grew at the fastest pace in five years while paid click growth slowed from 13% in 2Q to 8% in 3Q, and explained that AI Mode monetized at a lower rate. WPP Media expects generative search ads to grow from $5.1 billion in 2026 to over $100 billion by 2030. The place of search ads is moving inside AI answers.

AI chatbots have become ad space as well. OpenAI began a ChatGPT ads pilot in the US on February 9 and opened a self-serve ads manager to US advertisers in May. It said tests would start in the UK, Brazil, Japan, South Korea and Mexico. Ad tracker AdClarity estimated, as of early May, average monthly spend since the pilot at about $109 million. OpenAI has not published this number.

AI is moving ad money in these directions:

- From intermediaries to engines: as engines take over targeting, creative and measurement, agencies and open-web intermediaries lose share.
- From large advertisers to small ones: as ads work even with little data, more advertisers enter the auction.
- From link clicks to AI answers and agents: search clicks move into AI answers, and new ad space appears inside them.

## The variable that could flip the view is how fast purchase decisions move to agents

An ad engine's power comes from outcome data. The model learns again only when it knows whether the viewer actually bought. If agents search and pay on a person's behalf, that data lands first with whoever owns the agent.

![If agents make the purchase decision, outcome data changes owner. Today a person sees an ad in a feed or search and buys on the advertiser's site; money is paid per impression, click or conversion, and outcome data returns to the ad platform. Through agents, a personal agent connects to a business agent or authorised API and pays; money becomes transaction fees, subscriptions and ads inside agents, and outcome data goes to whoever owns the agent.](/post-assets/ad-ai-scaling-law-price-per-ad-meta-applovin-agents-2026-11-08/agent-shift.en.svg)

Meta is betting on both sides. More than 10 million people in the US and Canada set up its personal agent Muse within a month and a half of its September launch. Over 25% of weekly users shop with it, with an average purchase above $200. Zuckerberg said Meta will work on Muse monetization sooner than usual and described a model in which Meta takes a percent of the value it helps create. A transaction-fee model could sit beside the ad-fee model.

CFO Susan Li expects the market to move away from agents navigating every website like a human. She expects permissioned, structured interactions instead: authenticated APIs, approved partnerships and direct links between personal agents and business agents. Then whoever holds the standards and payment rails for those links will own the outcome data.

We think this variable is small for 2027 ad numbers and grows after 2028. Muse users are still few next to Meta's 3.6 billion daily users. ChatGPT ads are still adding countries. If the share of purchases made through agents is disclosed and transaction fees start to show up as revenue, the timeline moves forward.

## Set side by side, outcome data is the dominant variable

| Variable | Evidence now | Our view | Signal that changes the view |
|---|---|---|---|
| Size of outcome data | Meta took 57% of the three companies' 3Q ad revenue increase; top three hold 57.6% outside China | Dominant. Money keeps gathering in engines that run the auction and see outcomes. | Advertisers pull budgets after a gap appears between platform-reported conversions and real incremental sales |
| Cadence of model steps | Meta changed models every quarter; GEM training compute 4x in 12 months; AppLovin's 2Q/3Q step | Steps continue in 2027, and quarterly numbers move in steps | Meta's price growth falls below impression growth for two quarters in a row |
| Advertiser base | About 10 million advertisers on generative creative tools; Unity advertiser accounts +27%; AppLovin installs turned positive | Small advertisers support market growth | Advertiser growth stalls and growth relies only on price from existing advertisers |
| Shift of ad space | Google paid clicks +8%; ChatGPT ads adding countries; Muse shopping | Search pressure is gradual; agents are a post-2028 variable | Share of purchases through agents is disclosed, and Meta or OpenAI books transaction fees |
| Economy | Meta includes better macro among reasons for price gains | Price-led growth reacts to the economy first | Price growth turns down first as the economy slows |

Outcome data is the dominant variable. Compute can be bought: AppLovin's cost of revenue rose by less than $0.10 for each extra dollar of revenue. Auction and purchase records cannot be bought. The cadence of model steps sets how much quarterly numbers swing, and the economy sets the level of prices. Agents are the variable that could change who owns the dominant variable itself.

## Links for Korean investors

- Naver is a Korean engine that holds outcome data from both search and shopping (Smart Store). Its 3Q results, expected on November 12, will show the effect of its AI ad products and how AI Briefing affects search clicks.
- Kakao's Talk Biz revenue grew 13% in 3Q, and KakaoTalk display ads within it grew 35% (per Korean press reports).
- If ChatGPT ads begin testing in Korea, Korean search and display budgets gain a new competitor.
- For mobile game publishers such as Krafton and Netmarble, user acquisition becomes more efficient, but the price of each install rises too. Spending grows while the return target stays the same.
- For AI chips, ad models are a steady source of compute demand. GEM's training compute rose 4x in 12 months. But a substantial share of Meta's compute goes to frontier model training, so ad models alone do not explain Meta's capex.

## What to check next

![What to check next: November 9 (US) The Trade Desk 3Q, November 12 Naver 3Q, late January Meta 4Q and 2027 plan, early February Alphabet and Amazon 4Q, February AppLovin and Unity 4Q. Dates not yet confirmed are marked TBC.](/post-assets/ad-ai-scaling-law-price-per-ad-meta-applovin-agents-2026-11-08/next-checks.en.svg)

In Meta's 4Q results, check whether price growth keeps beating impression growth, whether new model gains keep coming, and how large 2027 capex will be. For Google, the test is whether paid click growth catches up with query growth. In The Trade Desk and agency results, check whether intermediaries keep slowing.

## Data limits

- Meta's per-model effects apply to specific surfaces, objectives and segments, so they cannot be added. GEM's 18.9% conversion and 12% CTR gains are company figures without a stated baseline or period.
- The price share is our calculation, splitting impression and price growth with logarithms. Meta's price includes macro and currency effects, so AI's share cannot be isolated.
- Meta figures come from official transcripts, and GEM technical details from Meta's engineering blog and arXiv papers. Google and Amazon figures follow the primary sources of our [October 30 post](/post/meta-ad-edge-google-amazon-share-shift-2026-10-30/).
- ChatGPT ad spend is a third-party (AdClarity) estimate; OpenAI has not disclosed ad revenue.
- The WPP Media figure is a forecast. One outlet reported 4.4%; we used the 8.9% in WPP Media's own release.
- Publicis and Kakao figures come from secondary reports. Naver and The Trade Desk have not yet reported 3Q.
- AppLovin's comment on data-sparse segments and Unity's advertiser account growth are call statements, not filed figures.
- We did not use broker estimates or price targets.

## Sources

- Meta official call transcripts: [3Q26](https://s21.q4cdn.com/399680738/files/content_files/META-Q3-2026-Earnings-Call-Transcript.pdf), [2Q26](https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf), [1Q26](https://s21.q4cdn.com/399680738/files/doc_financials/2026/q1/META-Q1-2026-Earnings-Call-Transcript.pdf), [4Q25](https://s21.q4cdn.com/399680738/files/doc_financials/2025/q4/META-Q4-2025-Earnings-Call-Transcript.pdf), [3Q25](https://s21.q4cdn.com/399680738/files/doc_financials/2025/q3/META-Q3-2025-Earnings-Call-Transcript.pdf)
- Meta 3Q26 filings: [press release (SEC)](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/meta-09302026xexhibit991.htm), [common stock prospectus (424B5)](https://www.sec.gov/Archives/edgar/data/1326801/000119312526436410/d94886d424b5.htm)
- Meta Engineering: [GEM introduction (2025-11-10)](https://engineering.fb.com/2025/11/10/ml-applications/metas-generative-ads-model-gem-the-central-brain-accelerating-ads-recommendation-ai-innovation/), [GEM follow-up (2026-10-13)](https://engineering.fb.com/2026/10/13/ml-applications/generative-ads-model-gem-scaling-frontier-ads-ai/)
- Papers: [HSTU, arXiv 2402.17152](https://arxiv.org/abs/2402.17152), [Wukong, arXiv 2403.02545](https://arxiv.org/abs/2403.02545)
- AppLovin and Unity: [AppLovin 3Q 10-Q](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001751008/5d38e9cf-1f99-43b1-adcc-36979436fce4.pdf), [AppLovin 3Q call transcript (secondary)](https://www.fool.com/earnings/call-transcripts/2026/11/05/applovin-app-q3-2026-earnings-call-transcript/), [Unity 3Q call transcript (secondary)](https://www.fool.com/earnings/call-transcripts/2026/11/05/unity-software-u-q3-2026-earnings-call-transcript/)
- Google: [Smart Bidding exploration (2025-05-21)](https://blog.google/products/ads-commerce/smart-bidding-exploration-ai/), [Alphabet 3Q release (SEC)](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm), [Alphabet 3Q call transcript (secondary)](https://www.fool.com/earnings/call-transcripts/2026/10/29/alphabet-googl-q3-2026-earnings-call-transcript/)
- Other platforms: [Reddit 3Q shareholder letter (SEC)](https://www.sec.gov/Archives/edgar/data/0001713445/000171344526000114/exhibit992q326.htm), [Pinterest 3Q release (SEC)](https://www.sec.gov/Archives/edgar/data/0001506293/000150629326000151/q3-26xpressrelease.htm), [The Trade Desk 2Q results](https://www.thetradedesk.com/press-room/the-trade-desk-reports-second-quarter-2026-financial-results), [The Trade Desk 3Q date](https://www.thetradedesk.com/press-room/the-trade-desk-announces-date-of-third-quarter-2026-financial-results-and-conference-call)
- Agencies: [Omnicom 3Q (SEC)](https://www.sec.gov/Archives/edgar/data/0000029989/000002998926000024/a2026q3earningsrelease.htm), [Omnicom 3Q coverage (exchange4media, secondary)](https://www.exchange4media.com/advertising-news/omnicom-q3-organic-growth-hits-72-as-adjusted-eps-climbs-22-159420.html), [WPP 3Q trading update copy](https://www.directorstalkinterviews.com/wp-content/uploads/2026/10/WPP-Third-Quarter-Trading-Update-2026.pdf), [Publicis 3Q (Adweek, secondary)](https://www.adweek.com/agencies/publicis-says-three-horse-holdco-race-is-good-for-business-as-q3-growth-hits-5/)
- Industry forecast: [WPP Media This Year Next Year 2026 midyear](https://www.wppmedia.com/news/report-this-year-next-year-midyear-2026)
- ChatGPT ads: [Digiday (secondary)](https://digiday.com/media-buying/expand-thoughtfully-openai-offers-chatgpt-ads-to-new-markets-including-the-u-k-brazil-and-japan/)
- Korea: [Kakao 3Q (Bizwatch, secondary)](https://news.bizwatch.co.kr/article/mobile/2026/11/05/0003), [Naver 3Q date (Financial News, secondary)](https://www.fnnews.com/news/202611021502551535)

<strong>As AI redistributes ad money, who loses share first? Leave A, B or C and one data point in the comments.</strong>

<strong>A. Ad agencies and open-web intermediaries: engines take over targeting and creative, and fees shrink.</strong>

<strong>B. Google Search: as AI answers grow, paid clicks grow less and search ads lose share.</strong>

<strong>C. Meta's feed ads: as purchase decisions move to agents, outcome data changes owner.</strong>

This is for research and information only and is not investment advice. Views and decision thresholds are analytical assumptions, not trading instructions or personal portfolio decisions. Figures have reference dates, and some come from secondary sources. We used Anthropic's Claude for research and editing. Alphabet and Amazon are investors in Anthropic, and Anthropic competes with Meta, OpenAI and Google in AI models, so Anthropic has interests related to several companies in this post. We did not judge the size of that effect.
