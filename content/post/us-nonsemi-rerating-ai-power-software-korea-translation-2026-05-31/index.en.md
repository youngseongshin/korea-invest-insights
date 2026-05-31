---
title: "US Non-Semiconductor Re-Rating Check: AI Power, Software and Stablecoin Rails Through a Korean Equity Lens"
date: 2026-05-31T16:20:00+09:00
description: "A two-month review of the strongest US non-semiconductor re-rating themes, from quantum and fuel cells to AI software, stablecoin rails and space-defense, then translated into Korean equities such as NHN KCP, Douzone Bizon, Hanwha Systems, Semyung Electric, LG CNS and NAVER."
categories: ["Market-Outlook"]
tags:
  - "US stocks"
  - "non-semiconductor re-rating"
  - "AI power"
  - "AI software"
  - "stablecoin"
  - "quantum computing"
  - "space defense"
  - "Korean equities"
  - "NHN KCP"
  - "Douzone Bizon"
  - "Hanwha Systems"
  - "Semyung Electric"
  - "LG CNS"
  - "NAVER"
slug: us-nonsemi-rerating-ai-power-software-korea-translation-2026-05-31
valley_cashtags:
  - NHN KCP
  - Douzone Bizon
  - Hanwha Systems
  - Semyung Electric
  - LG CNS
  - NAVER
draft: false
---

> Connected context
> This post follows [AI token futures and cost per token](/post/ai-token-futures-cost-per-token-korea-semiconductor-thesis-2026-05-30/), [whether China and Hong Kong AI overheating can spill into Korea](/post/china-hong-kong-ai-overheat-korea-ai-cloud-llm-proxy-2026-05-31/), and [HD Hyundai Heavy Industries' SMR option](/post/hd-hyundai-heavy-industries-smr-terrapower-natrium-option-2026-05-27/). The question here is narrower: after the US non-semiconductor re-rating, which Korean second-line stocks can translate the same AI-infrastructure logic into actual price and flow?

## TL;DR

Over the last two months, the strongest US re-rating themes outside semiconductors were **quantum computing, onsite power and fuel cells, AI software and data apps, crypto and stablecoin rails, and second-line space-defense-drone names**.

The most investable baskets are not necessarily the highest-return baskets. My preference is **AI power/grid plus AI software/data operations**. The first reflects the shift of AI-factory bottlenecks from GPUs to electricity. The second reflects the reversal of the "AI kills SaaS seats" fear into stronger Snowflake and Datadog-style demand for data, observability, security and AI operations.

The Korean translation is different.

| US theme | Korean translation | Price reflection |
|---|---|---|
| AI power/grid | Electrical equipment, cables, busduct, HVDC, second-line grid names | Leaders already priced, second-lines only |
| AI software/data apps | ERP, AX, cloud, enterprise data, AI operations platforms | Still underpriced |
| Stablecoin/payment rails | PGs, banks, wallets, KRW stablecoin payments | Underpriced but policy-driven |
| Space/defense/drones | Defense electronics, satellites, drones, space systems | Some second-lines underpriced |
| Quantum/security | Mostly quantum security and PQC, not true quantum compute | Already overheated |
| Fuel cell/on-site power | Data-center onsite power, SOFC, PAFC | High-beta, stock selection required |

The practical Korean watchlist is short.

| Rank | Stock | View | Why |
|---:|---|---|---|
| 1 | NHN KCP | **Conditional Buy** | Stablecoin payment PoC, 1Q earnings growth, low-teens PER, recent foreign and institutional buying |
| 2 | Douzone Bizon | **Watchlist** | Korea's closest AI software/data operations translation. Price has barely moved while earnings growth is strong |
| 3 | Hanwha Systems | **Watchlist** | Space and defense-electronics option is not fully priced, but valuation and Philly Shipyard risks remain |
| 4 | Semyung Electric | **High-volatility watchlist** | Second-line grid candidate after leader correction. Lower valuation burden but liquidity risk |

There is no broad "buy now" call. This is a **second-line confirmation market**, not a late chase market. The practical trigger is a 20-day moving-average recovery, box breakout, and renewed foreign plus quality-institutional flow.

---

## 1. Data Basis

US price data is based on `yfinance` adjusted close prices, from the **March 31, 2026 close to the May 29, 2026 close**. Direct semiconductors, semiconductor equipment and memory names are excluded. SOXX and SMH are used only as benchmarks.

Korean price and flow data comes from the local Research OS database:

```text
/Users/youngseongshin/agents/Stock_Research/agents/KR_Crawler/data/screener_kr.db
```

Korean prices use the same March 31 to May 29 window. Flow data uses the most recent 20 and 5 trading days from `investor_flow_raw_daily`, with `amount_unit='million_krw'`.

[Blocked] I did not fully recompute every stock's latest forward EV/Sales, forward PER, EPS revision history or full DART line items. "Re-rating" here means price, basket performance, flow and verified public catalysts.

---

## 2. US Non-Semiconductor Re-Rating Ranking

| Rank | Sub-theme | Basket size | 2M median | 1M median | Median drawdown from high | Leaders |
|---:|---|---:|---:|---:|---:|---|
| 1 | Quantum computing | 5 | **+81.9%** | +45.9% | -2.8% | IONQ +150.0%, QBTS +108.9%, RGTI +81.9% |
| 2 | Clean hydrogen / fuel cell | 7 | **+74.8%** | +12.5% | -4.6% | FCEL +231.7%, BLDP +159.9%, BE +110.3% |
| 3 | AI software / data apps | 10 | **+34.0%** | +30.3% | 0.0% | DDOG +109.5%, CRWD +87.2%, SNOW +69.4% |
| 4 | Crypto / stablecoin / brokerage rails | 9 | **+27.5%** | -1.2% | -10.4% | RIOT +119.3%, CLSK +114.9%, MARA +76.2% |
| 5 | Space / defense / drones | 10 | **+22.6%** | +14.2% | -1.9% | LUNR +136.2%, RKLB +123.4%, PL +83.0% |
| 6 | Software broad | 8 | **+21.3%** | +14.8% | 0.0% | SKYY +32.2%, IGV +27.0%, CLOU +24.5% |
| 7 | Copper / electrification metals | 7 | **+15.4%** | +12.5% | -2.1% | TECK +27.8%, BHP +22.2%, XME +15.9% |
| 8 | Grid / electrical equipment / EPC | 10 | **+15.0%** | -4.9% | -9.9% | GNRC +42.3%, FIX +32.6%, PWR +29.7% |
| 9 | AI power / data-center electricity | 11 | **+12.3%** | -4.6% | -7.4% | BE +110.3%, OKLO +34.9%, PWR +29.7% |

Benchmarks:

| Index / ETF | 2M | 1M | Drawdown |
|---|---:|---:|---:|
| SPY | +16.3% | +5.0% | 0.0% |
| QQQ | +27.9% | +9.5% | 0.0% |
| IWM | +17.1% | +4.0% | -0.5% |
| SOXX | +73.2% | +22.2% | -0.2% |
| SMH | +56.2% | +17.5% | -0.5% |

Semiconductors remain the strongest broad complex. But outside semis, quantum and fuel cells caught up with the SOXX-style move. That does not automatically make them the best buys. The cleaner re-rating is in AI software and AI power.

---

## 3. US Theme Read-Through

### Quantum Computing

Quantum was the strongest two-month basket. IonQ's Q1 2026 filing points to revenue growth, a large cash and investment balance, and FY2026 revenue guidance. ([SEC IonQ EX-99.1](https://www.sec.gov/Archives/edgar/data/1824920/000119312526208923/ionq-ex99_1.htm))

[Inference] The market moved from "this is still a lab theme" to "commercial revenue is arriving faster than expected." But after 80% to 150% two-month moves in IONQ, QBTS and RGTI, this looks more like late-stage extension than a fresh O'Neil-style first breakout.

**View:** Watchlist. Do not chase before a new base forms.

### Clean Hydrogen and Onsite Fuel Cell Power

Bloom Energy reported Q1 2026 revenue of **$751.1 million**, up **130.4% year over year**, product revenue up **208.4%**, and operating income of **$72.2 million**. It also raised the midpoint of full-year 2026 revenue growth guidance from about 60% to about 80%. ([Bloom Energy](https://www.bloomenergy.com/news/bloom-energy-reports-record-first-quarter-2026-results-and-raises-full-year-2026-guidance/))

[Inference] This is not a generic hydrogen-economy trade. It is an AI data-center power timing trade. Grids take time. AI campuses need electricity now. Bloom is being reclassified as onsite power for AI infrastructure.

**View:** Bloom deserves separate treatment. Avoid chasing lower-quality FCEL, BLDP and PLUG after sharp moves.

### AI Software and Data Apps

Snowflake reported FY2027 Q1 product revenue of **$1.334 billion**, up **34%**, and RPO of **$9.21 billion**, up **38%**. ([Snowflake SEC filing](https://www.sec.gov/Archives/edgar/data/1640147/000164014726000027/fy2027q1earnings.htm))

Datadog reported Q1 2026 revenue of **$1.006 billion**, up **32%**, about **4,550** customers with $100k+ ARR, and GA releases for GPU Monitoring, Bits AI Security Agent and MCP Server. ([Datadog IR](https://investors.datadoghq.com/news-releases/news-release-details/datadog-announces-first-quarter-2026-financial-results/))

[Inference] The AI-software re-rating is the reversal of a fear: AI does not simply destroy software seats. It also creates more demand for data control planes, observability, security and AI operations.

**View:** Highest-quality non-semi re-rating. Wait for post-earnings digestion rather than chase.

### Crypto, Stablecoin and Brokerage Rails

Coinbase reported Q1 2026 crypto trading volume market share of **8.6%**, average USDC held in Coinbase products of about **$19 billion**, and Base processing **62%** of global onchain stablecoin transaction volume. ([Coinbase IR](https://investor.coinbase.com/news/news-details/2026/Coinbase-Q1-Financial-Results-Show-Resilient-Financial-Performance-Driven-by-New-All-Time-High-Crypto-Trading-Volume-Market-Share/default.aspx))

AP reported that the GENIUS Act was signed into law on July 18, 2025, creating a US regulatory framework for stablecoins. ([AP](https://apnews.com/article/donald-trump-stablecoins-congress-cryptocurrency-94fa3c85e32ec6fd5a55576cf46e58ea))

[Inference] The re-rating is broadening beyond Bitcoin beta into stablecoins, prediction markets and agentic commerce rails.

**View:** COIN and HOOD are higher-quality platforms. Miners remain high-beta trading instruments.

### Space, Defense and Drones

Rocket Lab reported Q1 2026 revenue of **$200.3 million**, up **63.5%**, backlog of **$2.2 billion**, and new Electron/HASTE and Neutron launch contracts. ([Rocket Lab IR PDF](https://investors.rocketlabcorp.com/node/12416/pdf))

[Inference] The theme is no longer just small launch vehicles. It is space systems, defense payloads and vertical integration.

**View:** Watch RKLB, AVAV, KTOS and ASTS selectively. Contract confirmation and backlog quality matter more than the theme label.

---

## 4. Korea Translation: What Is Priced And What Is Not?

| Korean sub-theme | Names | 2M median | 1M median | Median drawdown | 20D foreign | 20D institution | Read |
|---|---:|---:|---:|---:|---:|---:|---|
| Copper/electrification metals | 9 | **+70.2%** | -19.0% | -26.0% | -KRW 98.0bn | +KRW 19.4bn | Already re-rated, now correcting |
| Quantum/security/network | 8 | **+67.4%** | -4.3% | -26.5% | +KRW 49.8bn | -KRW 26.6bn | Overheated |
| AI power/grid/electrical | 12 | **+42.8%** | -24.3% | -26.0% | -KRW 1.44tn | -KRW 165.8bn | Leaders priced, second-lines only |
| On-site power/fuel cell/SMR | 11 | **+26.8%** | -19.3% | -23.0% | -KRW 435.6bn | -KRW 404.6bn | Some re-rating, weak flow |
| Space/defense/drones | 12 | **-0.5%** | -19.5% | -24.7% | +KRW 157.9bn | +KRW 10.2bn | Underpriced in second-lines |
| Crypto/stablecoin/payment rails | 12 | **-3.6%** | -17.3% | -25.7% | -KRW 32.6bn | -KRW 1.2bn | Underpriced, stock selection needed |
| AI software/data apps | 12 | **-3.6%** | -14.8% | -21.0% | -KRW 306.4bn | -KRW 25.4bn | Underpriced, quality filter needed |

The key translation:

> Korean power, copper and quantum-security baskets already front-ran much of the US theme. Korean AI software and stablecoin-payment rails have not.

---

## 5. Korean Candidate 1: NHN KCP

**View:** Conditional Buy
**Theme:** Stablecoin payments, PG, PAYCO, payment infrastructure

NHN KCP is the cleanest Korean stablecoin-payment read-through. Seoul Shinmun reported that the company is running an online and offline stablecoin payment PoC using an Avalanche-based payment-specific mainnet, PAYCO integration, merchant-management tools, and QR approval times of about two seconds. ([Seoul Shinmun](https://www.seoul.co.kr/news/economy/2026/05/21/20260521500054))

It also signed a digital payment partnership with NH Nonghyup Bank. ([Financial News](https://www.fnnews.com/news/202604220917147287)) Yonhap reported Q1 2026 operating profit of **KRW 13.8 billion**, up **26.4%** year over year and **4.4%** above consensus. ([Yonhap](https://www.yna.co.kr/view/AKR20260512018500527))

| Metric | Value |
|---|---:|
| Close | KRW 17,930 |
| 2M return | +14.3% |
| 1M return | -10.6% |
| Drawdown from 2M high | -15.8% |
| 20D foreign flow | +KRW 3.81bn |
| 20D quality-institution flow | +KRW 2.89bn |
| 5D foreign flow | +KRW 1.74bn |
| 5D institutional flow | +KRW 3.66bn |
| Forward PER | 13.0x |
| TTM PER | 14.0x |
| OP YoY | +24.9% |

**Why it is not fully priced:** The stock is only up 14.3% over two months and down 10.6% over one month. The market still prices it mostly as a low-margin PG stock, not as a possible KRW stablecoin payment-infrastructure option.

**Entry:** KRW 17,000 to 18,000 support with continued foreign and quality-institution buying, or a KRW 18,500 breakout with turnover expansion.

**Invalidation:** PoC fails to convert into commercialization discussion, PG operating-profit growth slows below 10%, or KRW 16,500 breaks while foreign flow disappears.

---

## 6. Korean Candidate 2: Douzone Bizon

**View:** Watchlist / breakout candidate
**Theme:** AI ERP, enterprise data, AI software operations

Douzone Bizon is the most natural Korean translation of the Snowflake and Datadog logic. Enterprise AI needs access to ERP, workflow, approval, documents, email, groupware and permissioned internal data. Douzone already sits on those surfaces.

BusinessPost reported that Douzone's Q1 2026 results were expected to improve on AI and cloud-solution revenue growth plus profitability improvement. ([BusinessPost](https://www.businesspost.co.kr/BP?command=mobile_view&num=429250))

| Metric | Value |
|---|---:|
| Close | KRW 120,000 |
| 2M return | +0.8% |
| 1M return | 0.0% |
| Drawdown from 2M high | -0.2% |
| 20D foreign flow | +KRW 24.37bn |
| 5D foreign flow | +KRW 6.11bn |
| TTM PER | 36.8x |
| OP YoY | +44.9% |

**Entry:** Hold KRW 118,000 to 120,000 with volume contraction, or break KRW 123,000 to 125,000 with continued foreign buying.

**Invalidation:** AI/cloud revenue growth slows, operating-profit growth falls below 20%, or the stock breaks KRW 115,000 with foreign buying disappearing.

---

## 7. Korean Candidate 3: Hanwha Systems

**View:** Watchlist / conditional inclusion
**Theme:** Space, defense electronics, satellites, radar, ICT

Chosun Biz reported Hanwha Systems Q1 2026 revenue of **KRW 807.1 billion**, operating profit of **KRW 34.3 billion**, and order backlog of **KRW 12.1963 trillion**. Defense exports and domestic mass-production projects supported growth. ([Chosun Biz](https://biz.chosun.com/industry/company/2026/04/27/4KHWSH5GKZAULGV5V5MVF65MSM/))

| Metric | Value |
|---|---:|
| Close | KRW 105,000 |
| 2M return | -8.0% |
| 1M return | -12.3% |
| Drawdown from 2M high | -23.4% |
| 20D foreign flow | +KRW 62.82bn |
| 5D foreign flow | +KRW 32.94bn |
| 5D quality-institution flow | +KRW 9.81bn |
| Forward PER | 82.0x |

**Why it is not fully priced:** The stock is down over two months, but foreign buyers have returned. The market is still focused on valuation and connected-loss risks rather than defense electronics, satellites, SAR and AI imagery options.

**Entry:** KRW 102,000 to 105,000 support with continued foreign buying, or KRW 112,000 breakout with institutional selling easing.

**Invalidation:** Philly Shipyard-related losses worsen in Q2, defense margin slows, or KRW 100,000 breaks with foreign buying stopping.

---

## 8. Korean Candidate 4: Semyung Electric

**View:** High-volatility watchlist
**Theme:** Second-line grid, HVDC, power equipment

| Metric | Value |
|---|---:|
| Close | KRW 9,890 |
| 2M return | +14.3% |
| 1M return | -37.3% |
| Drawdown from 2M high | -40.3% |
| 20D foreign flow | +KRW 2.04bn |
| 20D institutional flow | +KRW 0.12bn |
| TTM PER | 11.4x |
| OP YoY | +393.3% |

[Inference] Korean grid leaders have already re-rated. Semyung is a smaller, higher-volatility second-line name with a deeper one-month correction and lower valuation burden. The price setup is interesting, but liquidity risk is real.

**Entry:** KRW 9,500 to 10,000 support with turnover contraction, or KRW 11,000 recovery with foreign and institutional buying.

**Invalidation:** HVDC/grid earnings repeatability weakens, or KRW 9,000 breaks with turnover drying up.

---

## 9. What Not To Chase

| Group | Why |
|---|---|
| Xgate, Iwin Plus, Dream Security | Up 100% to 278% over two months. This is theme beta, not the same quality as US quantum commercialization |
| LS Electric, Hyosung Heavy, Sanil Electric | Good businesses, but already re-rated and now testing flow deterioration |
| Doosan Fuel Cell | Strong fuel-cell move, but valuation and loss risks remain high |
| Taihan Cable, KBI Metal, Gaon Cable | Copper/cable beta surged and then corrected deeply. Wait for a new base |

---

## 10. Execution Framework

**Buy now:** None.

**Waitlist conditions**

| Bucket | Names | Trigger |
|---|---|---|
| US AI software | SNOW, DDOG, CRWD, APP, MDB, NET | 5 to 10 trading days of post-earnings digestion, 20-day support, volume contraction then re-acceleration |
| US AI power/grid | GEV, PWR, ETN, BE, CEG, VST | 8% to 15% pullback from highs, lower volume, next order or guidance confirmation |
| Korean stablecoin rails | NHN KCP | KRW 18,500 breakout or KRW 17,000 to 18,000 support plus flow |
| Korean AI software | Douzone Bizon | KRW 123,000 to 125,000 breakout plus foreign buying |
| Korean space/defense second-line | Hanwha Systems | KRW 112,000 breakout plus easing institutional selling |
| Korean power second-line | Semyung Electric | KRW 11,000 recovery plus foreign and institutional buying |

---

## 11. Final View

The US non-semiconductor re-rating proves that AI does not end with semiconductors. But not every follow-on theme has the same quality.

The important shift is that AI-factory bottlenecks are spreading from GPUs into **power, operations software, data-center infrastructure, payment rails and space-defense networks**.

In Korea, power, copper and quantum-security leaders already moved first. What remains less priced is **stablecoin payments, AI software/data operations, and selected second-line space-defense names**.

> This is not a market for chasing yesterday's leaders. It is a market for confirming the first real flows into second-line candidates. My active Korean watchlist is NHN KCP, Douzone Bizon, Hanwha Systems and Semyung Electric.

---

## Evidence Ledger

| Item | Source | What it confirms |
|---|---|---|
| Price screens | yfinance and Research OS local DB | US and Korean theme-basket returns through May 29, 2026 |
| IonQ | [SEC EX-99.1](https://www.sec.gov/Archives/edgar/data/1824920/000119312526208923/ionq-ex99_1.htm) | Q1 2026 revenue, cash and guidance context |
| Bloom Energy | [Company IR](https://www.bloomenergy.com/news/bloom-energy-reports-record-first-quarter-2026-results-and-raises-full-year-2026-guidance/) | Q1 2026 revenue, growth and raised guidance |
| Snowflake | [SEC EX-99.1](https://www.sec.gov/Archives/edgar/data/1640147/000164014726000027/fy2027q1earnings.htm) | FY2027 Q1 product revenue and RPO |
| Datadog | [Company IR](https://investors.datadoghq.com/news-releases/news-release-details/datadog-announces-first-quarter-2026-financial-results/) | Q1 revenue, $100k+ ARR customers, GPU/MCP/AI product launches |
| Coinbase | [Company IR](https://investor.coinbase.com/news/news-details/2026/Coinbase-Q1-Financial-Results-Show-Resilient-Financial-Performance-Driven-by-New-All-Time-High-Crypto-Trading-Volume-Market-Share/default.aspx) | USDC, Base, stablecoin and agentic-commerce metrics |
| GENIUS Act | [AP](https://apnews.com/article/donald-trump-stablecoins-congress-cryptocurrency-94fa3c85e32ec6fd5a55576cf46e58ea) | US stablecoin regulatory framework |
| NHN KCP PoC | [Seoul Shinmun](https://www.seoul.co.kr/news/economy/2026/05/21/20260521500054) | Online/offline stablecoin payment PoC, PAYCO integration, QR approval time |
| NHN KCP earnings | [Yonhap](https://www.yna.co.kr/view/AKR20260512018500527) | Q1 2026 operating profit growth |
| Hanwha Systems | [Chosun Biz](https://biz.chosun.com/industry/company/2026/04/27/4KHWSH5GKZAULGV5V5MVF65MSM/) | Q1 2026 revenue, operating profit and backlog |

## Follow-Up Queue

- Compare forward EV/Sales, NTM revenue growth and FCF margins across the AI-software basket.
- Compare backlog growth and 2026/2027 EPS revisions across AI power/grid names.
- Re-run Korean 5-day and 20-day volume plus investor-flow screens on the four candidates.
- Apply late-stage filters to quantum and fuel-cell surge names.
- Track NHN KCP's commercial stablecoin timetable and whether economics accrue to banks, PGs, wallets or platforms.

*For research and information purposes only. Not investment advice.*
