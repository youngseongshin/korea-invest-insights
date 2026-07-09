---
title: "The US-China Split in Agentic Inference Infrastructure and the SRAM Opportunity"
date: 2026-07-09T17:20:00+09:00
description: "A structured look at why US and Chinese AI inference infrastructure is diverging, and how power, HBM, SRAM/LPU, packaging, and Korean listed companies fit into the map."
categories: ["Theme-Analysis", "Korea Semiconductors", "AI Infrastructure"]
tags: ["AI inference", "agentic AI", "SRAM", "LPU", "HBM", "Vera Rubin", "LPX", "Samsung Electronics", "SK hynix", "HD Hyundai Electric", "Hanmi Semiconductor", "power equipment", "China AI", "US AI"]
slug: us-china-agentic-inference-stack-sram-opportunity-2026-07-09
series: ["hbm", "exclusive-analysis"]
valley_cashtags: ["005930.KS", "000660.KS", "267260.KS", "010120.KS", "298040.KS", "042700.KS", "NVDA"]
draft: false
---

> Related reading:
> [NVIDIA Vera Rubin inference stack](/en/post/nvidia-vera-rubin-lpx-cmx-inference-stack-samsung-hbm-2026-05-28/) /
> [AI token value and memory value capture](/en/post/ai-token-value-memory-value-added-2026-07-09/) /
> [AI data center power bottleneck map](/en/post/ai-datacenter-power-bottleneck-korea-value-chain-screen-2026-07-04/)

## TL;DR

The United States and China are both scaling AI inference, but they are solving different constraints. The US bottleneck is power, rack density, HBM, advanced packaging, and token-per-watt efficiency. China’s bottleneck is access to leading-edge logic and HBM, so it is more likely to push Ascend-based clusters, optical mesh, parallel scaling, and domestic memory hierarchy workarounds.

For Korean listed equities, the investable landing zone is not China optical modules by default. The cleaner landing is the US-style AI factory bottleneck: HBM4/HBM4E, power equipment, HBM packaging equipment, and a less appreciated Samsung Electronics option around SRAM/LPU foundry, AI storage, and memory hierarchy.

The business winner and the best stock setup are not the same thing. SK hynix has the cleanest HBM4 leadership but is already a crowded winner. HD Hyundai Electric has high purity to US data center power bottlenecks, but order momentum is widely recognized. Hanmi Semiconductor is a real HBM tool bottleneck but needs repeat orders and customer diversification. The most asymmetric candidate is Samsung Electronics, if HBM4E, SRAM/LPU foundry, and AI storage start to show up in numbers.

## 1. What Is Being Verified

This note starts from YS-VC’s article <a href="https://www.ys-vc.com/blog/us-china-ai-inference-stack-divergence">“Power or Chips: Why US and Chinese AI Inference Stacks Are Diverging”</a>. The core argument is directionally right: inference scaling is no longer a generic GPU story, and the US and China face different binding constraints.

The adjustment is in the Korean equity landing. A China optical-mesh story does not automatically translate into Korean optical component revenue. China’s AI infrastructure supply chain is strategically closed and increasingly domestic. Korean equity exposure is more direct through components sold into the US-style AI infrastructure bottleneck.

| Claim | Assessment | Investor read-through |
|---|---|---|
| US and China AI inference stacks are diverging | Mostly true | The US optimizes power and rack efficiency; China works around logic and HBM limits |
| The US stack is moving toward GPU/HBM/SRAM rack-scale inference | True | Vera Rubin, LPX, HBM4, and SRAM/LPU become one system |
| China is using Ascend, optical mesh, and memory hierarchy workarounds | Partly true | Directionally plausible, but CloudMatrix performance and reliability need independent evidence |
| US export controls limit China’s NVIDIA data-center compute access | True | China cannot count on steady access to top-end GPUs and HBM |
| HBM is still a key control point | True | BIS has explicitly treated HBM as important for AI training and inference at scale |
| Korean opportunity equals China optical modules | Too aggressive | The cleaner Korean landing is HBM, power, packaging, and Samsung foundry optionality |

## 2. Why The Stacks Are Diverging

Agentic AI increases token volume. Coding agents, research agents, voice agents, and enterprise workflow agents do not just answer once. They read long context, call tools, interpret tool output, and generate new tokens repeatedly. That makes prefill, decode, KV cache, storage, network, and power all matter.

The bottleneck differs by country.

| Area | United States | China |
|---|---|---|
| Binding constraint | Power, rack density, transformers, HBM4, advanced packaging | Leading-edge logic, HBM access, export controls, software optimization |
| Architecture direction | Vera Rubin, LPX/LPU, HBM4, high-power AI racks | Huawei Ascend, optical mesh, parallel scaling, domestic memory hierarchy |
| Strength | Access to the best GPUs, HBM, and packaging ecosystem | Faster power buildout, state-led infrastructure, domestic cloud demand |
| Weakness | Time-to-power, grid interconnection, transformer lead times | No EUV-based leading logic, HBM limits, closed ecosystem |
| Korean equity landing | HBM, power equipment, HBM tools, foundry optionality | Limited unless direct suppliers are verified |

The IEA expects data-center electricity demand to reach about 945 TWh by 2030. ([IEA][1]) Power is no longer background infrastructure. It is becoming an upper bound on AI capacity.

BloombergNEF data cited by Energy Connects says China may add more than 3.4 TW of generation capacity over five years, almost six times the US. The same article says data centers could account for 38% of US power demand growth from 2024 to 2030, versus 6% in China. ([Energy Connects][2]) This is why the US is forced to care about token throughput per MW, while China can lean more heavily on parallel infrastructure buildout.

## 3. The US Stack: HBM Plus SRAM/LPU

The key US signal is NVIDIA’s Vera Rubin and LPX architecture. NVIDIA describes LPX as an inference accelerator for Vera Rubin. It combines Rubin GPUs using HBM with Groq 3 LPX using SRAM-based LPUs. ([NVIDIA LPX][3])

| Metric | NVIDIA LPX disclosure |
|---|---:|
| Agentic token load | Up to 15x more tokens |
| Vera Rubin NVL72 + LPX | Up to 35x higher throughput per MW |
| SRAM per LPU accelerator | 500MB |
| SRAM bandwidth per LPU accelerator | 150TB/s |
| Scale-up bandwidth per LPU accelerator | 2.5TB/s |
| LPX rack | 256 LPU chips |
| SRAM per LPX rack | 128GB |
| DDR5 per LPX rack | 12TB |
| SRAM bandwidth per LPX rack | 40PB/s |

This is not an HBM replacement story. HBM remains central to the Rubin GPU. SRAM/LPU complements HBM by handling latency-sensitive decode work closer to compute.

| Inference stage | Simple description | Main bottleneck |
|---|---|---|
| Prefill | Read the prompt and documents first | GPU compute, HBM bandwidth |
| Decode | Generate answers token by token | Latency, SRAM, LPU |
| KV cache | Reuse previous context | HBM, DDR, SSD, cache hierarchy |
| Serving | Handle many users reliably | Rack network, scheduler, power |

This creates an underappreciated Samsung Electronics angle. Samsung is not only an HBM catch-up candidate. At GTC 2026, Samsung highlighted HBM4 mass production, HBM4E, SOCAMM2 mass production, PCIe 6.0 SSDs, and broader AI computing solutions. ([Samsung Newsroom][4]) If inference moves toward HBM plus SRAM/LPU plus storage hierarchy, Samsung’s combined memory, foundry, packaging, and storage position becomes more relevant.

## 4. China: Optical Mesh Is A Competitive Signal, Not A Clean Korean Equity Trade

China’s workaround is logical. If access to the latest GPUs and HBM is constrained, the system must rely on more chips, better interconnect, optical mesh, and domestic software optimization. But that is not the same as a direct Korean revenue bridge.

China’s AI supply chain is strategically local. US export controls also push the system further inward. CloudMatrix-style performance, failure rates, and total cost of ownership still need stronger independent evidence. Therefore, China optical mesh is an important competitive variable, but it is not the best first Korean equity landing.

## 5. Korean Listed Equity Map

| Layer | Bottleneck | Korean names | View |
|---|---|---|---|
| HBM4/HBM4E | Vera Rubin and AI server memory | SK hynix, Samsung Electronics | Structural beneficiaries. SK hynix leads, Samsung is the catch-up option |
| SRAM/LPU foundry | Low-latency decode accelerators | Samsung Electronics | Still not fully visible in revenue, but the option is underappreciated |
| AI storage and KV cache | Agent memory, eSSD, PCIe 6.0 | Samsung Electronics, FADU | Extends the memory hierarchy below HBM |
| HBM packaging tools | TC bonders, advanced packaging | Hanmi Semiconductor | Real bottleneck, but customer concentration and valuation matter |
| Power equipment | Transformers, switchgear, grid connection | HD Hyundai Electric, LS ELECTRIC, Hyosung Heavy Industries | Direct US AI data-center power exposure |
| China optical mesh | Optical modules for Chinese clusters | Limited direct Korean exposure | Avoid unless supplier evidence appears |

## 6. Power Equipment Is The Front-End Bottleneck

In the US, power is a binding constraint. Data centers need grid connection, transformers, switchgear, and high-voltage equipment before GPUs can be monetized.

HD Hyundai Electric is one of the clearest Korean examples. It raised its 2026 order target by 23%, from $4.222 billion to $5.185 billion, citing North American power infrastructure, 765kV transformers, North American data centers, and onshore generator demand for data centers. ([Seoul Economic Daily][5])

| Factor | Investment read |
|---|---|
| P | Power-equipment pricing, high-voltage transformer margins, North America premium |
| Q | Data centers, transmission projects, 765kV demand, replacement cycle |
| C | Raw materials, capacity, delivery timing, quality costs |
| What to watch | Book-to-bill, North America orders, margins, 2027 capacity expansion |
| Failure mode | AI capex delay, grid permitting delay, local sourcing pressure, margin compression |

The company quality and the entry price should still be separated. The theme is visible now. Better setups come when AI capex fears pressure the stock but backlog and pricing remain intact.

## 7. HBM4/HBM4E: More Tied To The US Stack Than China

BIS has treated HBM as important for AI training and inference at scale. ([BIS][6]) If China’s access is restricted, allied AI infrastructure becomes more dependent on Korean HBM.

SK hynix is the clearest leader. Yonhap reported that SK hynix won more than two-thirds of NVIDIA’s HBM orders for a next-generation AI platform. ([Yonhap][7]) But the investment issue is crowding. The market already recognizes SK hynix as the HBM winner.

Samsung is different. The market has long treated it as an HBM laggard. If HBM4E, SOCAMM2, PCIe 6.0 SSD, foundry, and packaging are repriced as one AI memory-hierarchy platform, the discount can narrow.

| Name | Strength | Risk | Current view |
|---|---|---|---|
| SK hynix | HBM4 leadership, NVIDIA allocation, pure HBM exposure | Crowding, high expectations, 2027 supply risk | Wait |
| Samsung Electronics | HBM4E catch-up, foundry, storage, packaging option | HBM qualification delays, foundry losses, customer trust | Conditional Buy candidate |

## 8. Samsung’s SRAM/LPU Foundry Option

The non-consensus point is Samsung. If the inference stack moves from GPU-only to HBM plus SRAM/LPU plus cache storage, Samsung is no longer just a memory catch-up story. It is also a foundry and memory-hierarchy option.

The thesis strengthens if at least two of the following become visible:

| Condition | Evidence to watch |
|---|---|
| HBM4/HBM4E customer qualification and shipment | Earnings, guidance, HBM mix |
| LPU or AI ASIC foundry revenue or utilization improvement | Foundry loss reduction, HPC customers, AI accelerator production |
| AI storage and memory-hierarchy revenue | SOCAMM2, PCIe 6.0 SSD, eSSD, KV-cache demand |

It weakens if HBM4 qualification is delayed by two or more quarters, foundry losses do not narrow, or LPU/AI ASIC revenue does not accrue to Samsung in a material way.

## 9. Hanmi Semiconductor: Real Bottleneck, Price Discipline Needed

HBM4 increases packaging complexity. Hanmi Semiconductor is a real TC bonder bottleneck. The Elec reported that Hanmi received its first HBM4 TC bonder order from SK hynix. ([The Elec][8])

The thesis is sound, but equipment stocks have order-gap risk. Follow-on SK hynix orders, official Samsung or Micron orders, and margin durability matter more than the broad HBM narrative.

## 10. Practical View

| Priority | Exposure | View | Why |
|---:|---|---|---|
| 1 | Samsung Electronics | Conditional Buy candidate | HBM4E, SRAM/LPU foundry, and AI storage options may not be fully priced |
| 2 | HD Hyundai Electric | Wait | Direct US data-center power exposure, but order momentum is visible |
| 3 | SK hynix | Wait | Best HBM4 business position, but crowded winner |
| 4 | Hanmi Semiconductor | Watchlist | HBM tool bottleneck, but needs repeat orders and customer diversification |
| 5 | China optical-mesh beneficiaries | Avoid | Direct Korean supplier evidence is weak |

## Conclusion

The Korean opportunity is not “China optical mesh.” It is the US AI factory bottleneck: power, HBM, SRAM/LPU, advanced packaging, and storage hierarchy.

SK hynix may have the strongest business position. HD Hyundai Electric may have the cleanest power-equipment purity. But the most asymmetric rerating candidate is Samsung Electronics if the market stops viewing it only as an HBM laggard and starts pricing HBM4E, SRAM/LPU foundry, and AI storage together.

## Sources

- [YS-VC, Power or Chips: Why US and Chinese AI inference stacks are diverging](https://www.ys-vc.com/blog/us-china-ai-inference-stack-divergence)
- [IEA, Energy demand from AI](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
- [Energy Connects, China ramps up energy boom flagged by Musk as key to AI race](https://www.energyconnects.com/news/renewables/2026/february/china-ramps-up-energy-boom-flagged-by-musk-as-key-to-ai-race/)
- [NVIDIA, NVIDIA LPX](https://www.nvidia.com/en-us/data-center/lpx/)
- [Samsung Newsroom, Samsung unveils HBM4E and AI solutions at NVIDIA GTC 2026](https://news.samsung.com/global/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026)
- [BIS, Commerce strengthens export controls including HBM](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military)
- [Yonhap, SK hynix reportedly wins over two-thirds of Nvidia HBM orders](https://en.yna.co.kr/view/AEN20260128002800320)
- [The Elec, Hanmi Semiconductor receives first HBM4 TC bonder order](https://www.thelec.net/news/articleView.html?idxno=11132)
- [Seoul Economic Daily, HD Hyundai Electric raises 2026 order target](https://en.sedaily.com/finance/2026/07/06/hd-hyundai-electric-raises-2026-order-target-23-percent-on)
