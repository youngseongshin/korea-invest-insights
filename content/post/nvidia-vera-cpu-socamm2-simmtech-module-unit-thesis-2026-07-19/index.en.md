---
title: "NVIDIA Vera CPU Production Expansion and Simmtech: SoCAMM2 is About Module Units, Not Bits"
slug: "nvidia-vera-cpu-socamm2-simmtech-module-unit-thesis-2026-07-19"
date: 2026-07-19T18:05:00+09:00
description: "As NVIDIA expands Vera CPU into NVL72 and standalone servers, we verify whether SoCAMM2 capacity reduction is negative for Simmtech. Connecting NVIDIA, TrendForce, SK Hynix, and Simmtech official materials with July 16th stock price, supply-demand, and consensus to establish module-unit-based investment logic and entry conditions."
categories: ["Exclusive Analysis", "Tech Analysis", "Stocks"]
tags:
  - "Simmtech"
  - "NVIDIA"
  - "Vera CPU"
  - "Vera Rubin"
  - "SoCAMM2"
  - "LPDDR5X"
  - "AI Servers"
  - "Memory Module PCB"
  - "Semiconductor Substrates"
  - "Supply and Demand"
series: ["exclusive-analysis", "ai-hbm-2026"]
valley_cashtags:
  - 심텍
draft: false
---

One NVIDIA Vera Rubin NVL72 contains 36 Vera CPUs and 54TB of LPDDR5X memory. That is 1.5TB per CPU. However, in June, TrendForce reported that NVIDIA would halve the capacity of its next-generation Vera SoCAMM modules while increasing total module shipments and Vera CPU production.

On the surface, reduced memory capacity appears negative for component suppliers. When measuring PCB demand purely in terms of bits, it is. However, what Simmtech manufactures is not DRAM chips but PCBs for SoCAMM modules. Simmtech's volume is more sensitive to the number of CPUs produced and the number of modules than to total memory capacity. Even if LPDDR shortage forces lower per-CPU capacity, if NVIDIA ships more Vera CPUs and modules, PCB demand may not decline.

Looking at official materials, industry research, analyst estimates, and actual stock prices and supply-demand data shows that the business logic remains intact, but the price bottom has not yet been confirmed.

> Connected Context
> This article is a follow-up to [AI substrate and PCB investment thesis: System BOM as a common bottleneck](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/), [Korean AI PCB ecosystem: ten companies](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/), [Vera Rubin VR200 bill of materials verification](/post/vera-rubin-vr200-bom-memory-pcb-mlcc-korea-alpha-2026-05-21/), and [Memory supply gap spilling beyond HBM](/post/memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14/). Related articles can be found in the [AI substrate and PCB hub](/page/korea-ai-pcb-substrate-hub/), [AI HBM hub](/page/korea-semiconductor-hbm-kospi-hub/), and [exclusive analysis hub](/page/exclusive-analysis-hub/).

## TL;DR

* NVIDIA's official specifications show Vera Rubin NVL72 uses 36 Vera CPUs and 54TB of LPDDR5X. Standalone Vera CPU racks support up to 4 nodes per 1U tray, expanding to 256 CPUs per rack maximum. Vera's evolution from a supporting CPU in GPU racks to an independent server platform is confirmed.
* TrendForce's reported SoCAMM capacity reduction is a response to LPDDR supply shortage, not slowing demand. NVIDIA intends to lower per-module capacity while increasing total module shipments and Vera CPU production.
* Simmtech lists SoCAMM PCB on its official product page. However, simultaneous supply from three memory vendors and high market share are analyst estimates, not company disclosures. Actual customer-specific revenue and market share remain undisclosed.
* On July 16th, Simmtech closed at 107,400 KRW, down 11.68% in a single day. Over 20 trading days, institutions bought 236.2 billion KRW in net, and real money (pension, mutual funds, insurance) bought 186.4 billion KRW, while foreign investors sold 161.1 billion KRW and programs sold 185.9 billion KRW. Mid-term institutional buying pressure collides with short-term selling pressure.
* The 2026E PER of 27.1x is not cheap. Applying 2027E expected EPS of 6,655 KRW yields 16.1x, but only if SoCAMM revenue and profit margins expand as planned.
* The verdict is **Conditional Buy**. A safer approach confirms support near 104,000 KRW with easing foreign and program selling, or recovery through 113,800 KRW on increased volume.

---

<div class="thesis-callout">
  <div class="thesis-callout__label">This Article's Verdict</div>
  <div class="thesis-callout__body">
    Directly connecting SoCAMM2 capacity reduction to Simmtech PCB demand decline uses the wrong unit. Simmtech's revenue formula approaches Vera CPU units × modules per CPU × PCBs per module × Simmtech market share more than DRAM bit counts. However, the last two items in this formula have not yet been confirmed by company disclosures.
  </div>
</div>

---

## 1. Numbers to Discard and Numbers to Keep

The 2030 server CPU market size of 170 billion dollars, 1:1 CPU-to-GPU ratio, and 2027 DRAM shortage appearing in attached analysis are already reflected in major statements from multiple brokerages and corporate presentations. They are useful for understanding industry direction but are not sources of excess returns specific to Simmtech.

Four numbers are more important when evaluating Simmtech:

| Item | Why It Matters |
|---|---|
| Vera CPUs shipped | Determines the installed base for the SoCAMM platform |
| SoCAMM modules per CPU | Direct volume variable for Simmtech module PCBs |
| Simmtech's customer-specific supply share | Determines Simmtech's portion of industry growth |
| Module PCB unit price and cost | Determines the rate at which revenue growth converts to operating profit |

Using assumptions of 5 to 6 million Vera CPUs and 8 modules per CPU yields 40 to 48 million modules annually. At 5.5 million units, that is 44 million modules. However, this calculation is not an official NVIDIA shipment plan. It is a scenario derived from analyst and industry CPU shipment estimates and publicly disclosed system configurations.

Therefore, the 44 million unit figure should not be used directly as a revenue projection. It is only an example for gauging order magnitude.

## 2. Official NVIDIA Materials Confirm Vera's Expansion Path

### 2.1 NVL72 Contains 36 Vera CPUs

NVIDIA's [official Vera Rubin NVL72 page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) presents the following configuration:

| Item | Official Specification |
|---|---:|
| Rubin GPUs | 72 |
| Vera CPUs | 36 |
| CPU Memory | LPDDR5X 54TB |
| Memory per Vera CPU | 1.5TB |
| Vera CPU Cores | 88 |

The structure is not simply one CPU per GPU. In NVL72, one Vera CPU supports two GPUs. Nevertheless, a single 72-GPU rack requires 36 CPUs. This shows that the CPU and LPDDR layers have risen to major components in AI system cost structure.

### 2.2 Vera Sells Beyond GPU Racks

The more significant change is the standalone Vera CPU system. [NVIDIA's technical blog](https://developer.nvidia.com/blog/?p=114004) explains that Vera CPU racks can hold up to 4 nodes per 1U tray and scale to 256 Vera CPUs per rack. Single-socket and dual-socket systems support up to 1.5TB LPDDR5X per socket.

NVIDIA announced that Cisco, Dell, HPE, Lenovo, and Supermicro plan to launch Vera-based systems in the second half of 2026. If the schedule holds, Vera demand sources extend beyond NVL72 assembly volumes.

```text
Vera Demand Sources

CPU layer in Vera Rubin NVL72
+ Standalone Vera CPU servers
+ CPU racks for inference and agents
+ Single and dual-socket systems from major OEMs
```

This is why Simmtech's investment logic does not depend on GPU rack production alone. Expansion of standalone CPU systems broadens the demand base for SoCAMM modules and PCBs.

## 3. What Does SoCAMM Capacity Reduction Mean?

[TrendForce's June 10, 2026 analysis](https://www.trendforce.com/presscenter/news/20260610-13090.html) found that only about 60% of NVIDIA's 2027 LPDRAM requirements could be met with reserved allocations. To address the supply shortage, NVIDIA is reported to have chosen the following adjustments:

1. Lower the memory capacity of each SoCAMM module for Vera.
2. Increase total module shipments.
3. Produce more Vera CPUs with the same LPDRAM supply.
4. Raise market penetration of standalone Vera CPU racks.

In this structure, two types of demand can move in different directions.

| Demand Unit | Impact of Capacity Reduction |
|---|---|
| DRAM bits and GB | Per-CPU installed capacity may decline |
| SoCAMM modules | May increase if CPU shipment growth exceeds capacity reduction |
| Module PCBs | Proportional to modules, so may increase |
| Sockets, connectors, module testing | Increase with module count |

Expressing this in Simmtech terms gives the following formula:

```text
Simmtech SoCAMM PCB Volume
= Vera CPU Shipment
× SoCAMM modules per CPU
× PCBs per module
× Simmtech supply share
```

Conversely, memory vendors' SoCAMM revenue approximates CPU count × per-CPU installed GB × price per GB. The same news can have different impacts on DRAM vendors and module PCB vendors.

### Mismatch Between Official Specifications and TrendForce Reporting

NVIDIA's current official page shows a maximum 1.5TB LPDDR5X per Vera CPU. TrendForce reported next-generation module capacity reduction. With both documents existing simultaneously, it is not yet certain which case applies:

* NVIDIA's page continues to display maximum configuration or existing design
* Capacity reduction applies only to specific customers or product configurations
* Final production specifications are not yet finalized

This inconsistency is not noise to be hidden but a verification item for investment judgment. The actual per-module capacity, modules per CPU, and customer-specific configuration of production systems must be verified through launched products and company disclosures.

## 4. What Does Simmtech Supply in SoCAMM2?

### 4.1 What the Company Officially Confirms

[Simmtech's official product page](https://www.simmtech.com/product/board06.aspx) classifies SoCAMM PCB as a next-generation memory module product for AI. The key specifications presented by the company are as follows:

| Item | Simmtech Official Description |
|---|---|
| Base Memory | LPDDR |
| Application | Next-generation memory modules for AI |
| Layer Count | 10–12 layers |
| Key Requirements | Low dielectric constant and loss, low thermal expansion coefficient, impedance control |
| Surface Treatment | Selective ENIG |

Confirmation that SoCAMM PCB appears on Simmtech's product list is established. The company also manufactures general memory module PCBs and memory package substrates. When AI server LPDDR demand grows in both modules and packages, the company has a product foundation to respond.

### 4.2 What Is Only Confirmed by Analyst Estimates

The claim that Simmtech participates in SoCAMM2 production from Samsung Electronics, SK Hynix, and Micron simultaneously and holds high market share is not a company disclosure. It is an analysis and market estimate in [the brokerage report posted on Simmtech's homepage](https://www.simmtech.com/upload/media/file/639179687810021917.pdf).

Therefore, these expressions must be distinguished:

| Expression | Evidence Level |
|---|---|
| Simmtech possesses SoCAMM PCB products | Company official confirmation |
| Simmtech participates in SoCAMM2 production from three memory vendors | Analyst estimate |
| Simmtech holds #1 supply share | Analyst estimate |
| Customer-specific revenue and actual market share | Undisclosed |
| Exact timing of SoCAMM contribution to Simmtech profit | Undisclosed |

This distinction is necessary because customer qualification and production volume drive the economics of the substrate business. The ability to manufacture a product and maintaining high market share for repeat revenue are separated by stages of customer qualification, yield, unit price, and utilization rate.

### 4.3 SK Hynix's Mass Production Confirms Platform Reality

According to [SK Hynix's official announcement](https://news.skhynix.com/mass-production-socamm2-192gb/), the company began mass production of 192GB SoCAMM2 using 1cnm LPDDR5X in April 2026. The product targets the NVIDIA Vera Rubin platform.

This shows that SoCAMM2 is not a long-term research project but has entered actual mass production. However, SK Hynix's module mass production does not automatically prove Simmtech's customer-specific supply volumes. Simmtech demonstrating SoCAMM revenue, high-layer board mix, and utilization rate improvements in second and third quarter results is separately necessary.

## 5. Results Are Recovering but Still in the Stage of Proving Expectations

Simmtech recorded 1.41 trillion KRW in full-year 2025 revenue and 11.9 billion KRW in operating profit, with a net loss of 164.2 billion KRW. In the first quarter 2026, consolidated revenue recovered to approximately 422.4 billion KRW and operating profit to approximately 13.7 billion KRW. Second quarter consensus expects faster recovery pace.

| Item | 1Q26 Actual | 2Q26 Consensus | Sequential Change |
|---|---:|---:|---:|
| Revenue | \~422.4 billion KRW | 466.9 billion KRW | \~+10.5% |
| Operating Profit | \~13.7 billion KRW | 47.3 billion KRW | \~+245% |
| Operating Margin | \~3.2% | \~10.1% | +6.9 percentage points |

First quarter actuals are from [Simmtech's quarterly report](https://kind.krx.co.kr/external/2026/05/14/000890/20260514001959/11013.htm); second quarter estimates are from Naver and WiseReport consensus collected by Research OS local database on July 16th.

Operating profit growth far exceeds revenue growth. This indicates the need for simultaneous increases in high-margin product mix, factory utilization, and fixed cost absorption. Even if SoCAMM volume increases, profit margin may fall below expectations due to raw material and gold plating costs, initial yield, and customer-specific price negotiations.

### The Profit Path Demanded by Annual Consensus

| Year | Revenue | Operating Profit | Net Income | EPS | 2026E PER (July 16 close) |
|---|---:|---:|---:|---:|---:|
| 2026E | 1.932 trillion KRW | 189.6 billion KRW | 149.3 billion KRW | 3,968 KRW | 27.1x |
| 2027E | 2.289 trillion KRW | Consensus not aggregated | 251.0 billion KRW | 6,655 KRW | 16.1x |
| 2028E | 2.566 trillion KRW | Consensus not aggregated | 322.8 billion KRW | 8,588 KRW | 12.5x |

For the current stock price to look cheap, 2027 and 2028 earnings must actually materialize. The current 2026E PER of 27.1x and PBR of 5.64x substantially reflects early recovery. An average price target of 171,250 KRW is 59.5% higher than current price, but when targets are rising rapidly, they are difficult to use as a safety margin.

## 6. July 16th Stock Price: Overheating Reduced but Trend Recovery Not Yet Confirmed

Simmtech closed at 107,400 KRW on July 16th, declining 11.68% that day with an intraday low of 103,700 KRW. This is 34.6% lower than the July 1st high of 164,200 KRW.

| Period and Indicator | Value |
|---|---:|
| 1-day return | -11.68% |
| 5-day | -8.91% |
| 10-day | -13.87% |
| 20-day | -15.76% |
| 60-day | +40.94% |
| 120-day | +109.77% |
| vs. 5-day MA | -5.42% |
| vs. 20-day MA | -12.28% |
| vs. 60-day MA | -4.48% |
| vs. 120-day MA | +27.39% |
| RSI14 | 44.4 |

RSI has exited overbought territory. However, price remains below 5-day, 20-day, and 60-day moving averages. Since it is 27% above the 120-day line, all upside from the long-term move has not disappeared. Both "a sharp decline means cheap" and "the trend has recovered" cannot yet be confirmed.

On a trading basis, July 14th low of 99,600 KRW and July 16th low of 103,700 KRW represent the first support zone. The 113,800 KRW level confirms whether broken short-term support recovers; 121,600 to 124,000 KRW is a resistance zone where July 15th close and the 20-day moving average overlap.

## 7. Supply and Demand: Institutions Bought But Foreign Investors and Programs Still Sell

Cumulative net buying amounts through July 16th from Research OS local Kiwoom database are as follows. Units are in billions of KRW.

| Period | Foreign | Institutions | Individuals | Real Money | Programs |
|---|---:|---:|---:|---:|---:|
| 1 day | -9.83 | -5.88 | +15.57 | -5.91 | -11.55 |
| 5 days | -25.79 | +6.02 | +18.95 | +7.98 | -28.71 |
| 10 days | -93.39 | +80.32 | +11.79 | +75.77 | -40.78 |
| 20 days | -161.09 | +236.21 | -84.25 | +186.44 | -185.94 |

Real money is the sum of pension funds, mutual funds, and insurance. The table reveals two things simultaneously.

First, on a 20-day basis, institutional and real money buying is substantial. During the post-peak correction, domestically oriented long-term capital absorbed volume.

Second, foreign investor and program selling has continued at similar scale. On the July 16th plunge, foreign investors and institutions sold together while individuals absorbed 15.57 billion KRW. It is difficult to judge the bottom confirmed by institutional buying alone.

Short-selling transaction share also rose to 21.2% on July 16th. The 20-day average is 9.3%. Short-rebate inventory is approximately 5.48 million shares or 14.6% of issued shares, but not all short-rebate inventory is short-sale inventory. This figure should only be consulted as a reference for available selling volume.

## 8. Simmtech Revisited Through P × Q × C

### P: Unit Price of High-Layer SoCAMM PCB

SoCAMM PCB requires 10–12 layers, low dielectric loss, low thermal expansion, and precise impedance control. Higher manufacturing difficulty compared to general memory module PCB can help improve product mix. However, customer-specific unit prices and price increase structures are undisclosed.

### Q: Vera CPU and SoCAMM Module Count

Q is the largest upside variable. Beyond NVL72 mass production, standalone Vera CPU racks and major OEM servers are scheduled for the second half of 2026. If NVIDIA follows TrendForce's report in lowering per-module capacity while increasing module shipments, Simmtech's Q can grow faster than DRAM bit count.

### C: Raw Materials, Gold Plating, Yield, Utilization

The item determining whether revenue growth converts to operating profit. PCBs are sensitive to gold and copper prices, BT materials, plating costs, and initial yield. To achieve 10.1% operating margin consensus for Q2, increased high-margin products and cost pass-through must be confirmed together.

## 9. Three Scenarios

| Scenario | Conditions | Earnings and Price Interpretation |
|---|---|---|
| Bullish | Vera Rubin and standalone CPU servers ship as scheduled; total SoCAMM module count increases; Simmtech maintains three-memory-vendor market share | 2027E EPS of 6,655 KRW or higher becomes achievable and justifies leading PER of \~16x |
| Base | Vera shipments grow but LPDDR shortage and customer-specific ramps misalign; Simmtech share and margin remain at consensus levels | Business growth remains valid but stock can fluctuate widely based on earnings and supply-demand |
| Bearish | Vera or SoCAMM mass production delays; reduced per-module capacity does not lead to increased module count; Simmtech share or yield underperforms | 27x 2026E PER becomes a burden and probability of revisiting July lows increases |

In these scenarios, the most important variable is not the 170 billion dollar server CPU market. It is Simmtech's actual shipment volume, customer-specific revenue, high-layer board mix, and operating margin. Even if large industry numbers prove correct, if the portion accruing to the company is small, the stock will struggle.

## 10. Investment Verdict and Verification Sequence

### Verdict: Conditional Buy

Business logic has become clearer. NVIDIA official materials confirmed Vera's standalone server expansion, and TrendForce's report shows capacity reduction as a supply shortage response, not demand decline. Simmtech officially possesses SoCAMM PCB products.

However, the stock remains under pressure from foreign investor and program selling, and it is not cheap on 2026 earnings basis. Therefore, it is better to consider two entry paths.

| Path | Verification Condition |
|---|---|
| Support Confirmation | Hold the low between 103,700–106,000 KRW and confirm easing of foreign investor and program selling |
| Trend Confirmation | Recover through 113,800 KRW on increased volume with either institutions or foreign investors turning net buyers |

Recovery through 121,600–124,000 KRW would substantially reverse near-term trend damage. Conversely, breaking below 99,600 KRW on a closing basis without recovery would require reassessing price hypothesis.

### Catalysts

* Achievement of 466.9 billion KRW revenue and 47.3 billion KRW operating profit in 2Q26 earnings
* Company commentary on SoCAMM revenue, high-layer board mix, and utilization rate
* Actual market launch of Vera-based OEM servers in second half 2026
* NVIDIA's final production specifications and expansion of standalone Vera CPU rack shipments
* Mass production and customer qualification updates from SK Hynix, Samsung Electronics, and Micron for SoCAMM2

### Invalidation Conditions

* Repeat orders fail to follow initial SoCAMM volume
* Reduced per-module capacity does not translate to increased total module shipments
* Simmtech's customer-specific market share confirms below analyst estimates
* Q2 operating profit materially misses consensus with recurring raw material and yield burdens
* Vera Rubin or standalone Vera CPU system launch delays significantly
* 99,600 KRW breaks below support with concurrent expansion of foreign investor and program selling

## 11. Final Conclusion

Vera CPU supply expansion reinforces Simmtech's SoCAMM2 investment thesis. Particularly, the path of lowering module capacity due to LPDDR shortage while increasing total module and CPU shipments is difficult to characterize as unfavorable for substrate vendors. DRAM vendors sell bits and GB; Simmtech sells PCBs that go into each module. These are different units.

However, many items remain unconfirmed. Vera shipment volumes, final modules per CPU, Simmtech's actual customer-specific market share, SoCAMM revenue, and high-layer board profit margin cannot be finalized by public materials alone. A calculation like 44 million modules is a useful scenario but not official guidance.

Current stock price has corrected nearly 35% from peak, but there is no evidence that foreign investor and program selling has ended. Therefore, this idea should be viewed as "a conditional buy candidate requiring confirmation of both earnings and supply-demand" rather than "a growth stock that has fallen sharply." Q2 operating profit and SoCAMM revenue commentary is the first verification, and second-half 2026 Vera standalone server shipments represent the second verification.

---

## Evidence and Limitations

### Confirmed Facts

* NVIDIA official specifications present 36 Vera CPUs and 54TB LPDDR5X in NVL72.
* NVIDIA disclosed standalone CPU systems accommodating up to 256 Vera CPUs per rack and OEM launch plans for second half 2026.
* TrendForce reported adjustments to lower per-module capacity while increasing total module shipments and Vera CPU production due to LPDRAM shortage.
* SK Hynix announced mass production of 192GB SoCAMM2 for Vera Rubin.
* Simmtech lists SoCAMM PCB on its official product list.
* July 16th Simmtech close, supply-demand, and consensus have been reverified from local database.

### Estimates

* Annual calculation of 40 to 48 million modules using assumptions of 5 to 6 million Vera CPUs and 8 modules per CPU
* Claims that Simmtech supplies simultaneously to three memory vendors and maintains high market share
* Magnitude of capacity reduction impact on Simmtech revenue and profit following module count increase

### Items Not Confirmed by Public Materials

* NVIDIA's official 2027 Vera CPU shipment guidance
* Final production system modules per CPU and capacity per module
* Simmtech's customer-specific SoCAMM revenue, market share, unit price, and profit margin
* Q2 earnings announcement date and company SoCAMM revenue guidance
* Precise scope of application for TrendForce's reported capacity reduction and NVIDIA's official 1.5TB specification

Informational analysis based on public materials and local market data; not investment advice reflecting individual investor timelines, prices, or risk tolerance.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
