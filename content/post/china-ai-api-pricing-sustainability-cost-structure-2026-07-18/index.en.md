---
title: "Is China's AI API Pricing Sustainable? Verifying the Cost Structure Through Disclosures"
slug: "china-ai-api-pricing-sustainability-cost-structure-2026-07-18"
date: 2026-07-18T11:00:00+09:00
description: "DeepSeek V4-Pro's output costs 34 times less than GPT-5.6 Sol. Is that sustainable pricing, or the road to winner-take-all as in EVs? Hong Kong disclosures from Zhipu and MiniMax split the answer: paid frontier APIs have started clearing marginal inference cost, but neither recovers fully loaded cost including training. China's cost edge is not Huawei silicon or cheap electricity but the stack of model architecture, batching, caching and cloud utilization, with the power gap worth only about 2% of compute price."
categories: ["Exclusive Analysis", "AI Infrastructure", "Tech-Analysis"]
tags:
  - "China AI"
  - "DeepSeek"
  - "Zhipu"
  - "MiniMax"
  - "Alibaba"
  - "Huawei"
  - "API Pricing"
  - "Cost Structure"
  - "HBM"
  - "Samsung Electronics"
  - "SK Hynix"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Context
> This post is a follow-up to [What China's Open-Model Convergence Actually Changes](/post/china-open-model-convergence-value-chain-redistribution-2026-07-17/). Where that piece covered the <strong>value-chain implications</strong> of performance convergence, this one verifies through Hong Kong disclosures whether that low-cost API pricing is <strong>sustainable at the cost-structure level</strong>. Best read alongside [Kimi K3 Resets the AI Price Curve](/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/) and [The Real Debate in Semiconductors](/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/). Related hubs are the [AI HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/) and the [Exclusive Analysis Hub](/page/exclusive-analysis-hub/).

## TL;DR

* Current Chinese AI API pricing is <strong>a blend of structurally lower cost and strategic loss-leading competition</strong>. It is unlikely that every ultra-low price holds, and equally unlikely that prices fully revert to US frontier levels.
* Hong Kong disclosures split the answer. Zhipu's API gross margin improved to <strong>18.9%</strong> (from 3.3% a year earlier), meaning it has <strong>started clearing marginal inference cost</strong>. But its total gross profit covers only <strong>9.3%</strong> of R&D, so <strong>fully loaded cost remains unrecovered</strong>.
* China's cost edge is real, but it is not Huawei silicon or cheap electricity. The order is <strong>model architecture and reduced active parameters > batching, caching and quantization > cloud GPU utilization > low target margins > power and domestic NPUs</strong>.
* Even generously sized, the power effect amounts to only <strong>about 2%</strong> of compute price. The fact that Qwen 3.5 Flash is priced identically in Beijing, Frankfurt and Virginia backs this up.
* Unlike EVs, AI models have <strong>low switching costs</strong>. If winner-take-all emerges, it will be in the cloud and distribution layer, not the model layer. The most likely path is a <strong>low-price oligopoly (60%)</strong>. \[Analysis scope\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Key Framing</div>
  <div class="thesis-callout__body">
    Chinese API prices are low not because they are already self-sustaining at a normal price level, but because improving inference efficiency and massive capital raising are propping them up together. That is a burden on the API margins of Western model vendors, but because the capital raised flows back into training and computing infrastructure, it does not mean total semiconductor demand is falling.
  </div>
</div>

---

## 1. How Cheap Is It

Prices per 1M tokens as of July 2026. \[Fact: official pricing pages\]

| Model | Input | Output |
|---|---:|---:|
| DeepSeek V4 Flash | $0.14 | $0.28 |
| DeepSeek V4 Pro | $0.435 | $0.87 |
| Gemini 3.5 Flash | $1.50 | $9 |
| GPT-5.6 Sol | $5 | $30 |

DeepSeek V4-Pro is about <strong>11 times</strong> cheaper than GPT-5.6 Sol on input and about <strong>34 times</strong> cheaper on output. That does not, of course, mean performance, latency, SLA, security and tooling are equivalent.

### The Price Gap Is Large Even Within China

- Qwen 3.7 Max: RMB 12 input, RMB 36 output, currently 50% off
- Doubao Seed 2.1 Pro: RMB 6 input, RMB 30 output
- DeepSeek V4-Pro: far more aggressive than even its Chinese rivals

So <strong>DeepSeek's pricing should not be read as the normal price for China as a whole</strong>. \[Inference: price dispersion reading\]

---

## 2. The Sustainable Part: Marginal Cost

DeepSeek V4-Pro is an MoE architecture that <strong>activates only 49 billion</strong> of its 1.6 trillion total parameters. Combining high utilization with batch processing and caching can sharply lower the actual compute cost per token. The cache-hit price for repeated input is just <strong>$0.003625</strong> per 1M tokens. \[Fact: DeepSeek official materials\]

So for the following traffic, even current pricing can be sustainable on a marginal-cost basis.

- Batch processing
- Cache hits
- Traffic without a latency guarantee
- High-volume use that can sustain high utilization

---

## 3. The Hard-to-Sustain Part: Fully Loaded Cost

Published pricing alone struggles to recover model training cost, R&D, failed experiments, idle capacity, and security, sales and enterprise SLA costs.

Price normalization has already begun. \[Fact: company actions and reporting\]

- DeepSeek cut V4 pricing 75%, then <strong>doubled peak-hour pricing</strong>
- Alibaba also raised prices on some AI services by up to <strong>34%</strong>
- Dedicated enterprise throughput and low-latency service are priced above the public API

This is evidence that ultra-low prices do not hold across every time slot and customer segment.

| Service | Sustainability |
|---|---|
| Cache, batch and non-priority traffic | High |
| Peak hours, low latency, high concurrency | Low |
| Enterprise security and SLA | Settling into separate, higher pricing |
| Full cost recovery for a standalone API business | Difficult at current prices |

---

## 4. Verifying Through Disclosures: Zhipu and MiniMax

This is where the real analysis begins. Rather than speculate, we can check this against the <strong>disclosures of Hong Kong-listed companies</strong>.

| 2025 | Zhipu (02513) | MiniMax (00100) |
|---|---:|---:|
| Revenue | RMB 724m | $79.04m |
| API/platform revenue share | 26.3% | 32.8% |
| API or company-wide gross margin | API 18.9% | Company 25.4% |
| Prior-year gross margin | API 3.3% | Company 12.2% |
| R&D / revenue | 439% | 320% |
| Adjusted net loss / revenue | 439% | 317% |
| Gross profit / R&D | <strong>9.3%</strong> | <strong>7.9%</strong> |

\[Fact: Zhipu 2025 results, MiniMax 2025 annual report\]

### Zhipu: Marginal-Cost Recovery Is Confirmed

API and open-platform revenue rose <strong>293%, from RMB 48.48m to RMB 190.4m</strong>, and gross margin climbed from 3.3% to 18.9%. The company attributed this to inference efficiency, economies of scale and price increases.

There is a more important fact. As of March 2026, the company had raised API prices <strong>83% versus the end of the prior year, and demand still exceeded supply</strong>. GLM-5's current official price is RMB 4 input and RMB 18 output per 1M tokens. The top-tier API appears to have moved past a structure that dumps below direct inference cost. \[Inference: implication of the price hike with excess demand\]

### MiniMax: Plausible but Unconfirmed

The company has not disclosed an API-only gross margin. Company-wide gross margin improved from 12.2% to <strong>25.4%</strong>, which it attributed to model and system efficiency and optimized infrastructure allocation.

M2.5 is currently priced at $0.30 input and $1.20 output per 1M tokens, with a fast tier at $0.60/$2.40. Because M2.5 launched in 2026 while the disclosed financials run only through 2025, however, <strong>the standalone API cost ratio at current pricing has not yet been verified</strong>. \[Blocked\]

### Fully Loaded Cost Remains Unrecovered at Both Companies

Zhipu's total gross profit of RMB 297m covers only <strong>9.3%</strong> of its RMB 3.18bn in R&D. MiniMax fared similarly: gross profit of $20.08m covered only <strong>7.9%</strong> of its $253m in R&D, and operating cash outflow was $280m.

Services MiniMax purchased from the Alibaba Group in 2025 totaled <strong>$75.88m, or 96% of revenue</strong>. That figure blends training and serving cloud spend, so it cannot be read directly as API cost, but it is evidence of heavy reliance on external computing infrastructure. Alibaba holds a 17.06% stake in MiniMax.

Importantly, the disclosure states that related-party transactions were conducted <strong>on the same public pricing and terms offered to general customers</strong>. Capacity assurance and integration convenience from the strategic relationship are plausible, but <strong>there is no basis to conclude that a hidden price subsidy existed</strong>. \[Inference: reading of the disclosure language\]

Even after listing, Zhipu raised a net HK$31.375bn, and MiniMax raised a combined HK$15.957bn through new shares and convertible bonds. Most of the proceeds go into R&D and computing infrastructure. The fundraising itself is not evidence of an API loss, but <strong>frontier-model competition is not, at this stage, sustained by internal cash alone</strong>. \[Fact: disclosure\]

### Verdict

1. Marginal-cost sustainability of paid, top-tier APIs: <strong>confirmed</strong> for Zhipu, plausible but unconfirmed for MiniMax
2. Sustainability of fully loaded cost including training: <strong>unmet</strong> at both companies
3. Sustainability of the price war: <strong>high</strong>. Capital-market fundraising can keep loss-making prices in place for a long time
4. Market structure: rather than winner-take-all, more likely <strong>segment-by-segment oligopoly</strong>, for example Zhipu in Chinese enterprise and on-premises deployment, MiniMax in overseas, consumer and multimodal

---

## 5. Decomposing the Cost Advantage: What Is the Real Reason

China's cost advantage in API serving is real. But the core driver is not cheap electricity or Huawei silicon alone, it is the following combination.

```text
Small active-parameter count and quantization
+ High batch-processing rate and cache utilization
+ GPU utilization at large-scale clouds like Alibaba
+ Low target margins
+ Cheap power in western China
```

| Factor | Cost advantage | Judgment |
|---|---:|---|
| Model architecture, quantization, caching | Very large | Core of China's API price competitiveness |
| Cloud scale and utilization | Large | Alibaba's most defensible moat |
| Low target margins | Large | Why prices are cheap, but a weakness for long-run profitability |
| Huawei Ascend | Moderate, conditional | Advantageous on optimized workloads, weak on general-purpose use |
| Western China power | Moderate | Effective for batch inference, limited for global real-time APIs |
| Government subsidies and policy finance | Present | Favorable for industrial buildout, but per-service amounts are opaque |

---

## 6. Is Power Really the Deciding Factor

It is true that Chinese power is cheap. The landed power price at the Ningxia Zhongwei data center is <strong>RMB 0.36/kWh</strong> as of 2026, about 45% of the level in eastern China. The 2025 US industrial average is <strong>8.62 cents/kWh</strong>, which works out to about RMB 0.62/kWh at an assumed exchange rate of 7.2 RMB/USD. Zhongwei is about <strong>42% cheaper</strong>. \[Fact: Chinese local government data, US EIA\]

But power alone does not make API prices 5 or 10 times cheaper. <strong>Generously sizing</strong> the power effect, assuming a 1kW IT load per card and a PUE of 1.1, gives this.

```text
Zhongwei:   1kW × 1.1 × RMB 0.36 = RMB 0.40/hour
US average: 1kW × 1.1 × RMB 0.62 = RMB 0.68/hour
Difference:                        about RMB 0.29/hour
```

Alibaba's L20 on-demand price is RMB 14.4/hour, so even under this upper-bound assumption, the power difference is only <strong>about 2%</strong> of compute price. \[Inference: own calculation\]

Power matters, but it is not the main driver of the API price gap.

### The Decisive Counter-Evidence

The western-power advantage suits batch inference and training well, but low-latency APIs must be deployed in eastern or overseas regions close to users. And Alibaba's Qwen 3.5 Flash is priced <strong>identically at $0.029 input and $0.287 output per 1M tokens in Beijing as well as in Frankfurt and Virginia</strong>. \[Fact: Alibaba Model Studio pricing\]

That is the most direct evidence that low-cost APIs are not simply a result of Chinese power. \[Inference: implication of identical regional pricing\]

---

## 7. Alibaba's Real Moat Is Utilization

Alibaba Cloud's real strength lies less in power than in its <strong>ability to keep GPUs from sitting idle</strong>. \[Fact: Alibaba official documentation\]

- Batch inference: <strong>50% off</strong> list price
- L20 spot instances: typically around RMB 2.88, versus RMB 14.4 on demand, a saving of roughly <strong>80%</strong>
- Idle GPUs: $0.000007 per CU idle rate versus $0.000018 per CU active rate
- Mixing on-demand, spot and autoscaling to handle peak traffic

Spot capacity carries reclaim risk, however, so a real-time API with a strict SLA cannot run entirely on spot. The structure keeps base demand on on-demand or dedicated resources and routes only elastic demand to spot. \[Inference: operational constraint\]

---

## 8. Is Huawei Ascend Unconditionally Cheap

Strictly speaking, Ascend is not a GPU but an <strong>NPU</strong>.

Huawei makes the following claims for CloudMatrix 384. \[Fact: Huawei official materials\]

- Single-card-equivalent inference throughput of 2,300 tokens/s
- About 4x versus a non-supernode configuration
- MFU improved by more than 50%
- 3-4x average per-card inference performance versus H20

It is a system-design approach that pools resources and uses MoE expert parallelism to compensate for the weaknesses of lower-spec individual chips.

### But It Should Not Be Read as Low Cost Right Away

- Huawei has <strong>not published an externally verified TCO on a like-for-like basis of model, latency and power</strong>. \[Blocked\]
- Because CloudMatrix raises throughput by binding together many NPUs and network fabric, <strong>per-card throughput and total cluster cost are different things</strong>.
- A 2026 field study of Ascend 910 needed 12 source patches, disabling of some high-throughput features, and repeated fault-handling measures to achieve stable inference. Even if the hardware is cheap, <strong>engineering and operating costs can rise</strong>. \[Fact: Ascend field study\]

### Conditional Verdict

| Condition | Verdict |
|---|---|
| Models deeply optimized for Ascend, such as Qwen, DeepSeek and GLM | Cost competitiveness possible |
| CUDA-based models ported as-is | Cost advantage uncertain |
| Large-scale batch inference within China | Favorable |
| Global enterprise real-time service | Unconfirmed once software and SLA costs are counted |

---

## 9. How Is This Different From EVs

The similarities are a strategic industry, large-scale investment, large-enterprise subsidies, and capturing share through price cuts.

The difference is that <strong>switching costs for AI models are far lower</strong>. API specifications are similar, and customers can route across multiple models simultaneously or self-host open-source models. If one vendor raises prices, competing models and self-hosting create a price ceiling.

Platforms that combine cloud, data, security, payments, advertising and productivity tools, by contrast, have high switching costs. <strong>If winner-take-all appears, it will be in the distribution and cloud layer rather than the model layer</strong>. \[Inference: switching-cost structure\]

The most likely structure looks like this.

- Alibaba: cloud, e-commerce, enterprise customers
- ByteDance: consumer traffic, advertising, content
- Tencent: WeChat, enterprise services
- Huawei and Baidu: domestic infrastructure plus public-sector and enterprise customers
- One or two independent model companies such as DeepSeek: setting the technical reference price

---

## 10. The Expected Path

| Scenario | Assessed probability | Outcome |
|---|---:|---|
| Low-price oligopoly | <strong>60%</strong> | Consolidates to 3-5 players, base API stays cheap, peak and SLA pricing rises |
| Full commoditization | 25% | Open source, MoE and in-house chips drive further price declines |
| Large-scale normalization | 15% | Chip, power and funding burdens push prices up 2-5x |

\[Inference: scenario estimate\]

Even a 5x price increase would put DeepSeek V4-Pro's output price at about $4.35, still below US frontier models. <strong>Current pricing may not be the floor, but the direction toward lower prices is hard to reverse.</strong>

---

## 11. Semiconductor Implications

Cheap APIs raise inference usage, which favors demand for server DRAM, NAND, networking and power. At the same time, they lower compute per token and HBM intensity, which pressures the per-unit economics of premium GPUs and HBM.

| Target | Judgment |
|---|---|
| Samsung Electronics | Relatively cushioned by its large general-purpose DRAM and NAND exposure |
| SK Hynix | A long-run warning sign for the HBM scarcity premium |
| NVIDIA | Pressure on premium GPU unit pricing, offset by rising total inference volume |
| Alibaba, Tencent | Benefit from cloud and distribution ecosystem expansion rather than API margin |

The key variable is not the rate of API price decline but the <strong>growth rate of total token usage</strong>. If usage grows faster than prices fall, the Jevons effect wins; if not, the multiple compresses first for premium GPUs and HBM. \[Inference: directional judgment\]

---

## 12. The Decisive Test Is the First-Half 2026 Disclosures

- Does <strong>Zhipu's API gross margin</strong> climb above 25-30% following the 83% price increase
- Does <strong>MiniMax disclose an API cost ratio</strong>
- Does <strong>revenue growth keep outpacing computing-cost growth</strong>
- Does the gap between peak/SLA pricing and public API pricing become entrenched
- Does Huawei publish a like-for-like, externally verified TCO

These five questions separate "sustainable cost" from "prices propped up by capital."

---

## Closing

Chinese API prices are low <strong>not because they are already a self-sustaining, normal price level</strong>. It is because improving inference efficiency and massive capital raising are propping them up together.

China has a structural cost advantage in domestic, batch-oriented, optimized model serving. But the extremely low API prices observed today cannot be explained by Huawei silicon and cheap power alone. The largest cost advantages, in order, are model size and reduced active parameters, batching/caching/quantization, cloud GPU utilization, and low target margins, with power and domestic NPUs coming after those.

From an investment standpoint, China's cheap APIs do not immediately mean that "Chinese AI has secured an overwhelming cost moat." The more accurate reading is that <strong>as inference service rapidly commoditizes, model companies' margins fall, and value is increasingly likely to shift toward cloud, power and semiconductor infrastructure</strong>.

That is a burden on the API margins of Western model vendors, but because the capital raised flows back into training and computing infrastructure, it <strong>does not mean total semiconductor demand is declining</strong>.

---

_This post synthesizes Hong Kong listing disclosures (Zhipu 02513's 2025 results and share placement, MiniMax 00100's 2025 annual report and fundraising), official company pricing pages (DeepSeek, OpenAI, Google, Alibaba Model Studio, Volcano Engine, Zhipu BigModel, MiniMax Platform), Huawei official materials and CloudMatrix-related research, Chinese local government power data, and US EIA statistics. MiniMax's standalone API cost ratio and Huawei's like-for-like, externally verified TCO remain undisclosed, and the scenario probabilities and power calculations are author estimates based on assumptions at the time of writing. The stocks mentioned are examples used to illustrate cost structure and are not a recommendation to buy or sell any specific security. Prices and disclosed figures are as of the announcement date and may change afterward. Investment decisions and responsibility for them rest with the individual investor._

---

### Related Posts

- [What China's Open-Model Convergence Actually Changes: Value-Chain Redistribution, Not Demand Collapse](/post/china-open-model-convergence-value-chain-redistribution-2026-07-17/)
- [Kimi K3 Resets the AI Price Curve: From Kimi Linear to HBM and Big Tech Strategy](/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/)
- [The Real Debate in Semiconductors: Four Physical Clocks and One Stock-Price Clock](/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [Are Semiconductors Cyclical, and What Is Fair Value? Pricing Samsung, SK Hynix and Micron with FCFE and Normalized Earnings](/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [AI Token Value Today and Tomorrow: Value Added for Memory Companies](/post/ai-token-value-memory-value-added-2026-07-09/)
