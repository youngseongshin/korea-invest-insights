---
title: "Korea Invest Insights Thesis Check: What 207 Korean Articles Say About Our Edge"
slug: "kii-investment-thesis-performance-mid-review-2026-05-26"
date: 2026-05-26T12:30:00+09:00
description: "A mid-cycle performance review of 207 Korea Invest Insights Korean-language articles and 593 article-stock pairs. AI infrastructure, semiconductors, power and smart-money screening worked best; gaming, biotech, K-beauty, listed VC and some idiosyncratic deep dives were more mixed."
categories: ["Korea Market", "Research Process"]
tags:
  - "Korea Invest Insights"
  - "investment thesis"
  - "performance review"
  - "research feedback"
  - "Korean equities"
  - "AI infrastructure"
  - "semiconductors"
  - "smart money"
  - "PEAD"
series: ["korea-rerating-2026", "research-process"]
valley_body_mode: teaser
---

> This is a meta follow-up to the [Korea Daily Market Hub](/page/korea-daily-market-hub/) and [Why Korea Part 5](/post/why-korea-market-cap-global-six-ai-memory-rerating-2026-05-24/). The goal is not to claim portfolio performance. It is to ask which investment theses published on Korea Invest Insights lined up with subsequent price action, and where the process needs correction.

## TL;DR

- We collected all <strong>207 Korean-language `/ko/post/` articles</strong> from the Korea Invest Insights sitemap and mapped them to <strong>593 article-stock pairs</strong>.
- Using primary mentions only, 527 pairs had calculable performance. The win rate was <strong>54.1%</strong>, +10% outcomes were <strong>29.4%</strong>, +20% outcomes were <strong>21.1%</strong>, and -10% outcomes were <strong>24.3%</strong>.
- The strongest cluster was <strong>AI infrastructure, semiconductors, HBM and substrates</strong>. Across 305 primary pairs, the average return was <strong>+15.5%</strong>, the median was <strong>+7.8%</strong>, and the win rate was <strong>67.9%</strong>.
- A separate thesis map compresses the corpus into <strong>14 investment theses plus 53 operating logs</strong>. Roughly <strong>39%</strong> of non-operating posts sat inside a broad Korea growth / AI-semiconductor risk-on cluster. That was a source of performance, but also a correlation risk.
- The weakest areas were <strong>gaming, parts of biotech and medtech, K-beauty / consumer, listed VC proxies and some idiosyncratic deep dives</strong>. These cases often had good narratives but weaker price bridges.
- The core lesson: KII's edge was strongest when <strong>theme diffusion + flows + bottleneck logic</strong> aligned. It was weaker when product narratives, binary events or low-liquidity themes were stretched into structural equity theses too early.

This is not investment advice and not an actual portfolio return. It does not include position sizing, execution price, stops, taxes, transaction costs, publication-time effects or realized trading decisions.

## What Was Measured

The purpose was to test research signals, not writing quality. The question was: <strong>which types of thesis were followed by positive price action?</strong>

| Item | Basis |
|---|---|
| Article source | Korean sitemap, Korean index.json, LLM guide |
| Articles | 207 |
| Article-stock pairs | 593 |
| Successful performance calculations | 557 |
| Primary-mention successful calculations | 527 |
| Primary-mention ticker count | 166 |
| Price source | Research OS local DB, KR prices_daily + Kiwoom open fallback, US_Crawler prices_daily |
| Latest price date | 2026-05-22 |
| Entry price | Publication-date open, or next trading-day open if the publication date was a market holiday |
| Latest price | 2026-05-22 close |

Primary mentions were based on `tag_code`, `tag_name` and `tag_alias`. Title or description aliases were excluded from the core interpretation because they create more false positives.

## Overall Scorecard

| Metric | Result |
|---|---:|
| Positive-return share | 54.1% |
| +10% or better | 29.4% |
| +20% or better | 21.1% |
| -10% or worse | 24.3% |
| Average return | +7.9% |
| Median return | +0.6% |
| 25th percentile | -9.3% |
| 75th percentile | +13.9% |

The result is constructive but not clean. The mean is positive, but the median is only slightly above zero. That means a relatively small number of large winners pulled up the average. The research process produced right-tail outcomes, but it also carried meaningful left-tail risk.

## Thesis Map: The Bigger Risk Is Correlation

The performance workbook answers one question: <strong>what went up after publication?</strong> The thesis map answers a different question: <strong>what were we repeatedly exposed to?</strong>

On that lens, 206 posts compress into 14 investment theses and 53 operating logs. The count differs by one from the 207-article sitemap performance run because the two exercises used slightly different grouping rules.

| Item | Value | Read |
|---|---:|---|
| Thesis-map posts | 206 | Comparable to, but not identical with, the 207-article performance dataset |
| Investment theses | 14 | Large idea buckets: stocks, sectors, macro, policy and process |
| Operating logs | 53 | Daily Wraps, weeklies and screeners; roughly 26% of the map |
| Korea growth / AI-semi risk-on cluster | 59 | Pearl Abyss 25, AI infra 18, Samsung Electro-Mechanics 8, Samsung Electronics 8 |
| Share of non-operating posts | Roughly 39% | 59 divided by roughly 150 non-operating posts |

Pearl Abyss is not a semiconductor company. The reason it appears in this correlation bucket is that the stock behaved more like a Korea growth / domestic risk-on exposure than a defensive standalone asset. In other words, the map is not a sector taxonomy. It is an exposure map.

The mid-review by thesis looks like this:

| Thesis | Posts | Residual Alpha | Mid-Review |
|---|---:|---|---|
| Pearl Abyss platform / franchise re-rating | 25 | Low | Deep tracking, but -28.1% price outcome. The market still wants a 2027 earnings bridge and next-title visibility. |
| Samsung Electro-Mechanics AI package components | 8 | Low | Thesis strongly validated by price. The remaining question is execution toward a 2028 OP path, not first-time reclassification. |
| AI semiconductor infrastructure beyond HBM | 18 | Medium | Best-performing cluster, but still exposed to an AI CapEx peak-out. |
| Samsung Electronics memory-cycle to AI-platform reclassification | 8 | Medium | Re-rating logic remains plausible, but foundry and memory-cycle risks must stay inside the thesis. |
| Why Korea / Korea discount compression | 5 | Medium | Structural frame worked, but the actual market was heavily concentrated in Samsung and SK Hynix. |
| KOSDAQ policy / smart money | 8 | Medium | Policy direction looks right; execution delays and fund-deployment risk need tracking. |
| Pamicell perception-change series | 4 | High | Clean recognition-gap thesis, but still needs direct evidence for the Doosan Electronics BG proxy logic. |
| Korean AI / sovereign AI / listed VC proxies | 6 | High | Potential information edge, but the bridge from private-market exposure to listed-stock re-rating is slow. |
| Humanoid robotics valuation skepticism | 4 | Medium | One of the few clusters with built-in valuation skepticism. That tone should be used more broadly. |
| Operating logs | 53 | System | Trust infrastructure rather than a single alpha claim; weak-side and short/risk screeners are still underbuilt. |

Combining the thesis map with the performance table produces a more balanced conclusion. The good outcomes were not random. But many of the good outcomes were also not independent. A large share of the winners sat in the same AI-memory / AI-infrastructure / Korea growth factor complex.

## What Worked

First-mention winners were concentrated in AI infrastructure and semiconductor bottlenecks.

| Stock | First Mention | Return From First-Mention Open | Read |
|---|---:|---:|---|
| Samsung Electro-Mechanics | 2026-04-09 | +161.7% | AI MLCC, FC-BGA, silicon capacitors, power-integrity re-rating |
| Jeju Semiconductor | 2026-05-13 | +121.0% | Memory / SoCAMM / earnings-surprise diffusion |
| Opticore | 2026-05-09 | +100.0% | High-beta optical / CPO theme |
| SK Square | 2026-04-14 | +96.8% | SK Hynix NAV and holding-company discount compression |
| TES | 2026-04-09 | +89.7% | Semiconductor equipment, PEAD, smart money |
| SK Hynix | 2026-04-14 | +77.8% | HBM leader and AI-memory earnings leverage |
| Daeduck Electronics | 2026-04-20 | +61.7% | AI substrates and FC-BGA diffusion |
| Marvell | 2026-04-10 | +58.8% | Custom AI silicon and interconnect bottleneck |

The common pattern was:

1. A large theme existed: AI infrastructure, HBM, substrates, power integrity, networking, optics.
2. Flows confirmed the story: foreigners, institutions or smart-money screens showed demand.
3. The logic was bottleneck-based: these were not optional products, but components needed for the system to work.
4. The theme moved down the value chain: from Samsung Electronics and SK Hynix into Samsung Electro-Mechanics, Daeduck, Simtech, TES and Jeju Semiconductor.

The Samsung Electro-Mechanics case is the clearest example. The thesis began with AI substrates and MLCCs, then expanded into silicon capacitors, Murata comparisons and AI-server passive-component bottlenecks. That sequence worked. But it also means the easy part of the thesis may already be priced.

## What Did Not Work

The weaker cases were more idiosyncratic.

| Stock | First Mention | Return From First-Mention Open | Read |
|---|---:|---:|---|
| Pearl Abyss | 2026-04-04 | -28.1% | Gap between game data and equity re-rating |
| GigaLane | 2026-04-17 | -27.5% | Low-liquidity neglected-stock volatility |
| Next Biomedical | 2026-04-14 | -26.3% | Medtech event risk and limited earnings bridge |
| OE Solutions | 2026-05-09 | -25.1% | CPO theme proximity and valuation risk |
| Openedges Technology | 2026-04-25 | -23.9% | Long-duration IP thesis versus short-term multiple compression |
| Hyundai Rotem | 2026-05-01 | -23.7% | Late entry into a strong defense / rail theme |
| DSC Investment | 2026-04-29 | -23.2% | Listed VC exposure not yet translating into equity demand |

These cases had different stories, but similar failure modes. Product or industry narratives were often better than the near-term equity bridge. Some themes were directionally right but not directly monetized by the listed stock. Several names were small or high-multiple stocks with weak liquidity, making them more vulnerable when risk appetite softened.

Pearl Abyss is the most important negative case. The game data did not collapse. The issue was that the market wanted a bridge from Crimson Desert success to repeatable earnings: DLC, the next title, capital allocation and the 2027 earnings path. Product data can support a hold thesis. It does not automatically create a stock re-rating.

## Cluster Results

Keyword-based clusters sharpen the lesson.

| Cluster | Pairs | Tickers | Average | Median | Win Rate | +10% or Better | -10% or Worse |
|---|---:|---:|---:|---:|---:|---:|---:|
| AI infra / semis / HBM / substrates | 305 | 92 | +15.5% | +7.8% | 67.9% | 40.7% | 18.7% |
| Smart money / PEAD / quality | 138 | 59 | +11.1% | +4.6% | 60.1% | 41.3% | 23.9% |
| Power / nuclear / energy | 67 | 33 | +9.1% | +2.4% | 56.7% | 35.8% | 31.3% |
| Robotics / physical AI | 31 | 19 | +7.9% | +2.1% | 58.1% | 29.0% | 22.6% |
| Biotech / healthcare | 34 | 29 | +2.7% | -4.2% | 35.3% | 26.5% | 35.3% |
| Gaming / Pearl Abyss | 49 | 15 | +2.0% | -13.9% | 34.7% | 20.4% | 57.1% |
| Listed VC / venture proxies | 18 | 13 | -5.5% | -4.6% | 22.2% | 11.1% | 38.9% |
| K-beauty / consumer | 22 | 11 | -8.7% | -8.5% | 22.7% | 4.5% | 31.8% |

The clearest edge was in the AI infrastructure value chain. The second-best signal was the screener process: PEAD, quality and smart-money intersection notes were more robust than pure narrative writeups.

Power and energy were positive but volatile. K-beauty, listed VC, gaming and parts of biotech were weaker because the bridge from story to earnings, flows or timing was less direct.

## Process Lessons

### 1. Separate good thesis from good entry price

A correct thesis can become a poor entry after the market prices it. Samsung Electro-Mechanics is now a valuation question, not just a thesis question. Pearl Abyss is the reverse: product evidence may be strong, but the equity needs a clearer earnings bridge.

### 2. Make primary tags stricter

Performance attribution depends heavily on tag quality. Comparison names, risk examples and passing mentions should not become primary tags. Core thesis names should always have ticker tags.

### 3. Separate article types

A Daily Wrap, a screener note, a deep dive and an explainer are not the same product.

| Article Type | Correct Performance Lens |
|---|---|
| Daily Wrap / Screener | Short-term flow and earnings-drift validation |
| Deep Dive | One-to-three-month thesis validation |
| Hub / Explainer | Discovery, SEO/GEO and reader navigation value |

### 4. Update failures faster

Losers should not simply be called wrong. They need classification: broken thesis, delayed thesis, overpaid entry, weak liquidity, or missing catalyst. Pearl Abyss, Openedges, K-beauty and listed VC proxies deserve follow-up reviews under that framework.

## Current Judgment

The interim read is straightforward:

<strong>KII has a research edge, but it is not evenly distributed across all article types or sectors.</strong>

The edge is strongest where <strong>AI infrastructure bottlenecks, flows and earnings drift</strong> overlap. It is weaker where the analysis relies on product quality, binary events, long-duration narratives or listed proxies for private-market exposure.

The thesis map adds one more point: <strong>the best-performing posts were not independent exposures.</strong> AI memory, AI infrastructure, Samsung Electro-Mechanics, Samsung Electronics, KOSDAQ growth and parts of Pearl Abyss were all tied to Korea risk-on conditions. The next review should therefore track not just returns, but factor concentration and thesis correlation.

The operating change is therefore:

1. Keep AI infrastructure and semiconductor bottlenecks as core coverage.
2. Keep Daily Wrap and screener-driven notes, but tighten tagging and tracking.
3. Apply more price discipline to gaming, biotech, consumer and listed VC stories.
4. Repeat this performance review monthly, not as a scorecard for bragging, but as a feedback loop for the research process.
5. Track correlation risk separately. Many posts can still be one large position if they share the same factor exposure.

## Data Notes

<strong>Facts:</strong> 207 Korean articles, 593 article-stock pairs, 557 successful performance calculations, 527 successful primary-mention calculations, 166 primary-mention tickers. Latest price date: 2026-05-22.

<strong>Inference:</strong> KII's strongest historical signals came from AI infrastructure, semiconductors, power and smart-money screening. The weaker areas were more idiosyncratic and less directly tied to earnings or flows.

<strong>Limitations:</strong> This is not actual portfolio performance. It excludes sizing, execution, costs, taxes, stops, publication-time effects and post-publication judgment changes. Posts published after the latest price date are blocked from performance calculation.

## Sources

- [Korea Invest Insights Korean sitemap](https://koreainvestinsights.com/ko/sitemap.xml)
- [Korea Invest Insights Korean index.json](https://koreainvestinsights.com/ko/index.json)
- [Korea Invest Insights LLM guide](https://koreainvestinsights.com/llms-full.txt)
- Research OS local DB: KR `prices_daily` + Kiwoom open fallback, US_Crawler `prices_daily`
- Internal outputs: `kii_article_performance_workbook.xlsx`, `ticker_summary_primary_mentions.csv`, `article_stock_performance.csv`, `summary_report.md`, generated 2026-05-26 KST

*For research and information purposes only. Not investment advice. Past performance does not guarantee future results.*
