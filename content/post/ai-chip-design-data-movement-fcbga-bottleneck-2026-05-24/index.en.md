---
title: "After NVIDIA, the AI Semiconductor Bottleneck Is Data Movement, HBM, FC-BGA and Power Integrity"
date: 2026-05-24T19:20:00+09:00
description: "A synthesis of Dwarkesh Patel's Reiner Pope chip-design interview, All-In's NVIDIA and AI infrastructure discussion, and 20VC's Anthropic, Cerebras and SpaceX capital-market debate. The key point is that AI infrastructure is no longer just a GPU story. Investors need to track data movement, HBM, package substrates, Ethernet and optical links, power integrity and testing. In Korea, the read-through runs from Samsung Electronics and SK Hynix memory to Samsung Electro-Mechanics FC-BGA and silicon capacitors, then into Daeduck, Isu Petasys, Simmtech, Korea Circuit, TLB and test sockets."
categories: ["Market-Outlook"]
tags:
  - "NVIDIA"
  - "Marvell"
  - "Samsung Electro-Mechanics"
  - "Samsung Electronics"
  - "SK Hynix"
  - "HBM"
  - "FC-BGA"
  - "AI substrates"
  - "AI infrastructure"
  - "Semiconductor value chain"
slug: ai-chip-design-data-movement-fcbga-bottleneck-2026-05-24
valley_cashtags:
  - NVIDIA
  - Marvell
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - 대덕전자
  - 이수페타시스
  - 심텍
  - 코리아써키트
  - 티엘비
draft: false
---

> Related series
> [NVIDIA Q1 FY27 and Korean AI infrastructure](/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [Marvell and Broadcom earnings preview](/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/) / [Samsung Electro-Mechanics KRW 1.5T silicon-capacitor contract](/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [MLCC and silicon capacitors explained](/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/) / [Samsung Electronics re-rating thesis](/post/samsung-electronics-tsmc-rerating-thesis-2026-05-16/) / [AI PCB and substrate hub](/page/korea-ai-pcb-substrate-hub/)

## TL;DR

The most important of the three videos is Dwarkesh Patel's interview with Reiner Pope. It does not start with market headlines. It starts with what actually happens inside a chip: where the electricity flows, where the data sits, and how often the chip has to move that data.[^dwarkesh]

The key point is simple. AI performance is not only about FLOPS. The real bottleneck is <strong>where the data comes from, where it is stored, and how short the path is between memory and compute</strong>. In that frame, NVIDIA remains central, but the investment read-through spreads into HBM, package substrates, FC-BGA, high-layer PCBs, Ethernet, optical links, power-stability components and testing.

For Korean investors, the translation is clear. <strong>Samsung Electronics and SK Hynix are the memory core. Samsung Electro-Mechanics is the FC-BGA and silicon-capacitor power-integrity node. Daeduck, Isu Petasys, Simmtech, Korea Circuit and TLB are substrate and PCB spread candidates.</strong> This is not a market to chase a Monday gap. The key is whether turnover and foreign / institutional flow hold into the afternoon.

---

## 1. Why the Reiner Pope Interview Matters

A common mistake in AI semiconductor investing is to read chip performance as "more FLOPS equals a better chip." Reiner Pope's explanation breaks that frame from the bottom up.

Much of AI computation is repeated matrix multiplication: multiply many numbers, add them, and do it again. Making the arithmetic unit faster matters, but at chip level the bigger question is often <strong>where the numbers come from</strong>.

An AI chip has several layers of storage and movement.

| Location | Plain-English description | Investment translation |
|---|---|---|
| Registers and SRAM | The workbench inside the chip | Very fast, but area is expensive |
| HBM | The high-speed warehouse next to the GPU | Bandwidth bottleneck; SK Hynix and Samsung Electronics |
| Package substrate / interposer | The floor connecting chips and memory | FC-BGA, ABF, advanced substrates |
| Server board and network | Roads inside and outside the rack | High-layer PCB, Ethernet, optical links |
| Data-center power | Electricity for the whole system | Transformers, distribution, cooling, total operating cost |

If the arithmetic unit waits for data, the chip is underused. So the real AI-chip question is not just "can we add more compute?" It is <strong>"can we move less data, keep it closer, and feed the chip without wasting power?"</strong>

That is why HBM, FC-BGA, silicon capacitors and high-speed PCBs belong in the same discussion. They all solve the same physical problem: <strong>keep AI chips fed with data and stable power</strong>.

---

## 2. Why Low-Precision Compute Leads to Substrates and Power

Reiner Pope's point on low precision is not simply that FP8 or FP4 doubles speed. Lower precision also changes area, wire count and power. Fewer bits mean smaller circuits, less switching and lower energy per operation.

That matters for investors because lower precision is not only an NVIDIA GPU feature. If more compute gets packed into the same power envelope, the whole system must evolve.

| Technology shift | System requirement | Korean supply-chain link |
|---|---|---|
| FP8 and FP4 adoption | More compute inside the same power budget | HBM4, server DRAM, SOCAMM |
| Tensor Core / systolic-array style designs | Less data movement inside the chip | HBM and package interconnect |
| Larger GPUs and ASICs | Larger die and package formats | FC-BGA, ABF, advanced substrates |
| Rack-scale expansion | More chip-to-chip and rack-to-rack bandwidth | High-layer PCB, Ethernet, optical links |
| Higher power density | Faster response to current swings and voltage noise | MLCC, silicon capacitors |

So AI semiconductor value does not end at the GPU vendor. NVIDIA anchors the system. Marvell and Broadcom sit in custom AI chips, connectivity, Ethernet and optical links. Korean memory, substrate and power-stability components attach underneath.

---

## 3. NVIDIA's Numbers Are Strong. The Market Question Has Changed

NVIDIA reported Q1 FY27 revenue of <strong>$81.6 billion</strong>, Data Center revenue of <strong>$75.2 billion</strong>, and Q2 revenue guidance of <strong>$91.0 billion ±2%</strong>. On official numbers, AI infrastructure demand has not rolled over.[^nvidia]

But the market is no longer asking only "is NVIDIA good?" That is already known. The new questions are:

1. Does this capex return as revenue and free cash flow for cloud customers?
2. Can data-center power and cooling bottlenecks be solved?
3. Can model companies keep paying high token bills?
4. Will AI backlash and regulation slow deployment?

The All-In episode belongs in this bucket. Anthropic, Karpathy, SpaceX, NVIDIA earnings and AI regulation are all part of one larger issue: <strong>AI is not over, but it now has to prove capital efficiency</strong>.[^allin]

In market language:

| 2023-2025 frame | 2026 and beyond frame |
|---|---|
| GPUs are scarce | Rack-level data movement and power are scarce |
| HBM is scarce | HBM + substrates + power integrity + networking are scarce together |
| AI models improve | AI usage must convert into revenue and cash flow |
| Buy NVIDIA | Track the bottlenecks underneath NVIDIA |

---

## 4. Marvell and Broadcom: Connectivity Becomes the Next Test

Marvell and Broadcom are the next earnings events to watch through this frame. Neither is simply an "NVIDIA competitor." As AI data centers scale, both attach to <strong>connectivity, switching, optical signals and custom AI silicon</strong>.

For Marvell, the core question is whether custom AI silicon and optical connectivity are accelerating into actual revenue. For Broadcom, the core question is whether AI ASICs and AI Ethernet networking are scaling together. If both companies sound strong, the Korean read-through should broaden beyond pure HBM.

| U.S. signal | Korean read-through |
|---|---|
| Custom AI chip demand | HBM, package substrates, testing |
| AI Ethernet and switch growth | Isu Petasys, high-speed PCB, low-loss materials |
| Optical links and silicon photonics | Selective optical exposure; indirect substrate and power benefits |
| Rack-scale expansion | Power equipment, cooling, data-center operating cost |
| Larger packages | Samsung Electro-Mechanics FC-BGA, Daeduck, Korea Circuit |

The right translation is not "Broadcom / Marvell good means all Korean semis are good." It is: <strong>AI-chip growth benefits the bottleneck suppliers that feed, connect, stabilize and test those chips.</strong>

---

## 5. What the AT&S News Confirms

On May 21, 2026, AT&S announced a capacity expansion for high-end IC substrates used in AI, at its Chongqing site in China. The investment is in the high-double-digit million-euro range and is backed by long-term customer agreements. AT&S expects a high-double-digit million-euro positive EBIT effect in fiscal 2026/27.[^ats-capacity]

The key point is not the customer name. The key point is that <strong>AI substrate capacity is now being expanded under long-term agreements</strong>.

AT&S also framed glass-core substrates in April as a next-generation foundation for AI, high-performance computing, high-speed communications and photonics. As packages become larger and more complex, dimensional stability, signal quality, power efficiency and data movement become limiting factors.[^ats-glass]

This lines up directly with the Reiner Pope interview. If the AI bottleneck is data movement, advanced substrates and packages are no longer passive parts. They become performance infrastructure.

---

## 6. Korean Stock-Group Translation

### 6.1 Samsung Electronics and SK Hynix: The Memory Core

Reducing data-movement cost requires HBM and server memory. Whether the accelerator is a GPU or a custom ASIC, high-performance AI silicon consumes memory bandwidth.

SK Hynix is the cleanest HBM exposure. Samsung Electronics is a broader option: HBM recovery, HBM4, server DRAM, SOCAMM, eSSD and foundry optionality. But Samsung still needs execution proof: customer qualification, yield and visible AI-silicon wins.

### 6.2 Samsung Electro-Mechanics: FC-BGA plus Silicon Capacitors

Samsung Electro-Mechanics is one of the clearest Korean second-order bottlenecks in this frame.

First, FC-BGA is the package substrate that connects high-performance chips to the board. Larger GPUs, CPUs, custom AI chips and switch ASICs all need advanced substrates.

Second, silicon capacitors stabilize power inside the AI GPU / HBM package. Samsung Electro-Mechanics announced a roughly KRW 1.5 trillion silicon-capacitor supply contract with a large global customer in May 2026, and described the product as a component that improves power stability inside high-performance semiconductor packages such as AI-server GPUs and HBM.[^semco-sicap]

The point is not "more MLCC content." The point is that Samsung Electro-Mechanics could be reclassified as <strong>a substrate company with in-package power-integrity components</strong>.

### 6.3 Daeduck, Isu Petasys, Simmtech, Korea Circuit and TLB

These names should not be lumped together too loosely.

| Group | What to watch | Risk |
|---|---|---|
| Daeduck Electronics | FC-BGA, package substrates, AI chip substrates | Customer proof, yield, utilization |
| Isu Petasys | High-layer networking PCB | Flow confirmation after a strong rally |
| Simmtech / TLB | Memory modules, SoCAMM, server PCB | AI revenue mix and margin proof |
| Korea Circuit | SoCAMM and FC-BGA optionality | Qualification and actual revenue timing |

The phrase "AI server exposure" is not enough. The evidence investors need is <strong>direct supply, ASP uplift, long-term agreements and margin resilience</strong>.

---

## 7. What 20VC Shows About Capital-Market Temperature

The 20VC episode discussed Anthropic, Karpathy joining Anthropic, Cerebras, SpaceX and AI token costs.[^twentyvc] This is less about semiconductor physics and more about capital-market temperature.

The positive signal is that investors are still willing to fund AI infrastructure and AI hardware stories. Model-lab financing, AI hardware IPO appetite and mega-tech IPO expectations remain alive.

The negative signal is concentration risk. Too much capital is gathering around a small number of mega AI and infrastructure companies. Private AI model spending eventually has to pass through public-market scrutiny, big-tech capex budgets or real revenue.

So the 20VC takeaway is not "buy private AI exposure." It is: <strong>AI risk appetite is alive, but the market will increasingly demand monetization and cash-flow proof.</strong>

---

## 8. Practical Checklist

For the Korean market next week, the question is not just whether Samsung Electronics and SK Hynix rise. The better signal is whether money moves down the stack.

| Order | Checkpoint | Meaning |
|---:|---|---|
| 1 | Samsung Electronics and SK Hynix hold on volume | Memory core confirmed |
| 2 | Samsung Electro-Mechanics and Daeduck hold after the open | FC-BGA and power-integrity re-rating |
| 3 | Isu Petasys, Simmtech, TLB and Korea Circuit participate | PCB and SoCAMM spread |
| 4 | Foreign and institutional flow holds into the afternoon | Real money, not just a theme trade |
| 5 | Power equipment and data-center infrastructure join | Full AI infrastructure bottleneck spread |

Entry discipline matters.

| Condition | Read |
|---|---|
| Gap-up at the open with weak turnover | Do not chase |
| Afternoon hold with foreign / institutional buying | Broaden watchlist |
| PCB names rally while memory megas weaken | More likely thematic |
| Memory → substrates → power-equipment sequence | Bottleneck spread signal |
| "AI" label without revenue or orders | Avoid |

---

## 9. Conclusion

The three videos combine into one sentence:

<strong>The AI trade is not over. It is moving down the stack.</strong>

2023-2025 was the GPU and HBM phase. From 2026 onward, the next layers are data movement, packaging, FC-BGA, Ethernet and optical links, power integrity, testing and data-center operating cost. NVIDIA remains the center. But the investor question is now: "which Korean bottleneck turns NVIDIA's revenue growth into its own earnings?"

The current order is:

1. <strong>Memory core:</strong> Samsung Electronics, SK Hynix
2. <strong>Package and power integrity:</strong> Samsung Electro-Mechanics, Daeduck Electronics
3. <strong>High-speed PCB and modules:</strong> Isu Petasys, Simmtech, Korea Circuit, TLB
4. <strong>Testing and sockets:</strong> ISC, LEENO Industrial, TSE
5. <strong>Power and data-center operations:</strong> power equipment and cooling infrastructure

The most important investment sentence is this: <strong>AI performance competition is a data-movement-cost competition, and that cost translates into HBM, packaging, substrates, networking and power.</strong>

If that spread is confirmed by turnover and foreign / institutional flow, FC-BGA and high-speed PCB should be treated as AI infrastructure bottlenecks, not just another theme.

---

## Evidence Classification

### [Fact]

- Dwarkesh Patel's Reiner Pope interview explains AI chip design through MAC operations, data movement, low-precision arithmetic, Tensor Core / systolic-array structures and total operating cost.[^dwarkesh]
- NVIDIA reported Q1 FY27 revenue of $81.6 billion, Data Center revenue of $75.2 billion, and Q2 revenue guidance of $91.0 billion ±2%.[^nvidia]
- AT&S announced on May 21, 2026 that it would expand AI high-end IC substrate capacity based on long-term customer agreements.[^ats-capacity]
- Samsung Electro-Mechanics announced a roughly KRW 1.5 trillion silicon-capacitor supply contract and described silicon capacitors as power-stability components for AI-server GPU and HBM packages.[^semco-sicap]

### [Inference]

- The AI chip bottleneck is moving from arithmetic units into data movement and power integrity.
- NVIDIA's strong results may flow through to Korea not only through HBM, but also through FC-BGA, high-speed PCB, silicon capacitors and test sockets.
- Marvell and Broadcom earnings are key checks for whether "custom AI chips + connectivity bottlenecks" are turning into real numbers.

### [Blocked]

- AT&S's key customer name and exact product mix.
- Whether specific Korean substrate and PCB companies directly supply NVIDIA, Marvell or Broadcom programs.
- Samsung Electro-Mechanics' silicon-capacitor customer, product margin and exact package location.
- Official confirmation of several private-company valuation and funding numbers discussed in All-In and 20VC.

[^dwarkesh]: Dwarkesh Patel, “Chip design from the bottom up / Reiner Pope,” YouTube, 2026-05-22. https://www.youtube.com/watch?v=oIk3R-sMX5o
[^allin]: All-In Podcast, “SpaceX's $2T case, Nvidia's shock selloff, America turns on AI,” YouTube, 2026-05-22. https://www.youtube.com/watch?v=HGbA6ze0_3M
[^twentyvc]: 20VC, “Andrej Karpathy joins Anthropic / Cerebras / SpaceX,” YouTube, 2026-05-21. https://www.youtube.com/watch?v=z94zlbVn048
[^nvidia]: NVIDIA Investor Relations, “NVIDIA Announces Financial Results for First Quarter Fiscal 2027,” 2026-05-20. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027
[^ats-capacity]: I-Connect007, “AT&S Expands Capacity for AI Substrates,” 2026-05-21. https://iconnect007.com/article/150109/ats-expands-capacity-for-ai-substrates/150106/pcb
[^ats-glass]: AT&S, “AT&S advances glass core substrates for AI, high-performance computing and photonics,” 2026-04-22. https://ats.net/en/press/ats-advances-glass-core-substrates-for-ai-high-performance-computing-and-photonics/
[^semco-sicap]: Samsung Electro-Mechanics, “Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract with Global Large-Scale Company,” 2026-05-20. https://samsungsem.com/global/newsroom/news/view.do?id=10310

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
