---
title: "AI Infrastructure Multiple Map: Why Samsung Electronics Looks Cheap and Samsung Electro-Mechanics Looks Expensive"
date: 2026-05-31T09:00:00+09:00
description: "GPU, HBM, CPU, MLCC and FC-BGA all sit inside the same AI infrastructure cycle, but they do not deserve the same multiple. This note decomposes the spread through pricing power, LTAs, customer lock-in, capex burden and peak-earnings doubt, then links Samsung Electronics and Samsung Electro-Mechanics in one relative-value frame."
categories: ["Market-Outlook"]
tags:
  - "AI infrastructure"
  - "valuation multiples"
  - "HBM"
  - "GPU"
  - "CPU"
  - "MLCC"
  - "FC-BGA"
  - "Samsung Electronics"
  - "005930"
  - "Samsung Electro-Mechanics"
  - "009150"
  - "SK hynix"
  - "000660"
  - "Nvidia"
  - "Broadcom"
  - "AMD"
  - "Intel"
  - "Murata"
  - "Ibiden"
  - "Korean semiconductors"
slug: ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31
valley_cashtags:
  - 삼성전자
  - 삼성전기
  - SK하이닉스
draft: false
---

> Context
> This post bridges the [Samsung Electronics stock-bonus / memory-supercycle note](/post/samsung-electronics-stock-bonus-supercycle-buyback-2026-05-27/) and the [Samsung Electro-Mechanics KRW 138T peer-premium note](/post/samsung-electro-mechanics-market-cap-murata-ibiden-premium-2026-05-28/). The first asked whether Samsung's DS profit duration is being re-rated. The second asked whether SEMCO deserves Murata / Ibiden-like AI component premiums. This note asks the connecting question: inside one AI infrastructure cycle, why do different layers deserve different multiples? Related hubs: [AI HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/), [AI PCB & Substrate Hub](/page/korea-ai-pcb-substrate-hub/), and [Korea Semiconductor Value Chain Hub](/page/korea-semiconductor-equipment-ip-hub/).

## TL;DR

Inside the same AI infrastructure cycle, the market does not assign the same multiple to every supplier. Multiples are not a simple function of "AI exposure." They are a function of <strong>earnings duration, pricing power, customer lock-in, capacity risk and peak-earnings doubt</strong>.

The most dangerous area today is re-rating MLCC / FC-BGA bottleneck stocks as if they were GPU/HBM-style structural monopolies. They are real bottlenecks, but not every bottleneck deserves an NVIDIA-style platform multiple.

The strongest relative-value idea is <strong>Samsung Electronics</strong>. It has HBM catch-up, memory pricing and foundry optionality, yet the user-provided 2026-05-29/30 public finance-data snapshot shows roughly 7.8x forward P/E and 4.4x P/B. Samsung Electro-Mechanics has the right thesis, but the price already demands several years of successful execution. ([Yahoo Finance][1])

---

## 1. The Core Formula

The multiple spread inside AI infrastructure is not about "who is exposed to the same demand cycle." It is about <strong>who can capture excess profit for longer, with less reinvestment, under more certain customer contracts</strong>.

```text
Multiple Premium
= pricing power × demand duration × customer lock-in × FCF conversion

Multiple Discount
= capacity capex burden × oversupply risk × peak-earnings doubt × customer concentration
```

That formula turns GPU, HBM, CPU, MLCC and FC-BGA into different assets, even though they all sit inside the same AI capex cycle.

| Layer | What Lifts the Multiple | What Caps the Multiple | Key Question |
|---|---|---|---|
| GPU / platform | CUDA, rack-scale systems, software lock-in, asset-light structure | custom ASICs, China controls, hyperscaler bargaining power | Is the customer buying time-to-market or just a chip? |
| HBM / memory | HBM4, sold-out supply, LTAs, rising HBM content per accelerator | memory peak-earnings doubt, capex, supplier diversification | Is this a cycle profit or a contracted franchise? |
| CPU | AI server attach, orchestration demand | substitutability, ARM / custom CPU, lower scarcity | Primary choke point or necessary helper? |
| FC-BGA | large high-layer substrates, qualification, long lead times | capex-heavy, depreciation, ABF oversupply memory | Is capex underwritten by LTAs / prepayments? |
| MLCC / Si-Cap | power-integrity bottleneck, high-reliability parts, low customer price resistance | generic MLCC cycle, low AI revenue purity, competition | Shipment blocker or commodity passive? |

---

## 2. GPU: Why It Gets the Highest Multiple

GPU is not just a semiconductor component. NVIDIA controls GPUs, networking, rack-scale systems, CUDA, the software stack and reference architectures. Customers are not merely buying chips. They are buying time to build an AI factory.

NVIDIA FY2027 Q1 revenue was $81.6B, Data Center revenue was $75.2B, and Q2 revenue guidance was $91.0B. With that growth rate and margin structure, the company's large market cap alone is not enough to call it a bubble. ([NVIDIA Investor Relations][2])

The GPU multiple is about:

| Variable | Interpretation |
|---|---|
| P | GPU / rack / system-level ASP can be defended or raised |
| Q | AI datacenter capex maps directly into accelerator demand |
| C | fabless structure and platform premium push much of the capex burden into the supply chain |

The Red Team matters. Hyperscaler custom ASICs, power / land / cooling constraints, China export controls and customer bargaining power are all real risks. Broadcom's AI revenue is also scaling fast: Q1 AI revenue was $8.4B and Q2 AI semiconductor revenue guidance was $10.7B. ([Broadcom Inc.][3])

Still, the GPU platform is the highest-quality layer in AI infrastructure. The reason is not "GPU." The reason is <strong>control over the AI factory operating system</strong>.

---

## 3. HBM: Hot Earnings, Peak-Earnings Discount

HBM is the memory-bandwidth bottleneck that determines GPU and custom ASIC performance. Without HBM, GPUs cannot ship properly. Yet HBM companies such as SK hynix and Micron screen at much lower forward P/Es than NVIDIA or Broadcom.

That is not because demand is weak. It is because the market still discounts HBM earnings as potential memory-cycle peak earnings, not fully as structural franchise earnings.

| Variable | Interpretation |
|---|---|
| P | HBM ASP carries a strong premium to commodity DRAM |
| Q | HBM content per GPU / ASIC, stack count and HBM4 / HBM4E transitions drive growth |
| C | TSV, stacking, packaging, yield and wafer allocation create heavy execution cost |

The key is the LTA. Traditional DRAM is exposed to spot prices and inventory cycles. HBM increasingly relies on customer qualification, allocation, long-term agreements and fixed volume / pricing structures. The stronger the LTA, the more the market can treat HBM as a <strong>contracted high-value memory franchise</strong> rather than commodity DRAM.

But P/B must be checked alongside P/E. In the input snapshot, SK hynix and Micron screen at low forward P/Es, but their P/B ratios already look structurally re-rated. "Cheap" and "peak-earnings doubt" coexist. ([Yahoo Finance][4], [Yahoo Finance][5])

---

## 4. CPU: Essential, But Not the Primary Choke Point

CPUs are necessary in AI servers. Host CPUs, orchestration, storage/network control, preprocessing and inference serving all need them. AMD's Q1 data-center revenue was $5.8B, up 57% year over year. ([Advanced Micro Devices, Inc.][6])

But the primary AI infrastructure bottlenecks are more clearly GPU, HBM, networking and advanced packaging. CPUs are necessary, but substitutable. Customers can choose across x86, ARM, hyperscaler internal CPUs, NVIDIA Vera CPU, Intel Xeon and AMD EPYC.

So CPU multiples require discipline.

| Company | Interpretation |
|---|---|
| AMD | Server CPU share gain is real, but a high forward P/E requires both EPYC share gains and Instinct GPU ramp success |
| Intel | The turnaround option exists, but foundry, process or AI accelerator execution must be proven first |

CPU benefits from the AI cycle, but a standalone CPU thesis has weaker alpha than GPU, HBM, FC-BGA or high-value power-integrity parts.

---

## 5. FC-BGA and MLCC: Right Theme, But Bottleneck Is Not Monopoly

The reason Samsung Electro-Mechanics, Murata and Ibiden matter is clear. As AI accelerators, server CPUs and networking ASICs grow larger, demand rises for large high-layer FC-BGA and high-reliability MLCCs. AI servers run higher power spikes, lower voltage margins and tighter power-integrity requirements.

Samsung Electro-Mechanics reported Q1 2026 revenue of KRW 3.209T and operating profit of KRW 280.6B, citing higher supply of AI-server MLCC and AI accelerator / server-CPU FC-BGA. ([Samsung Electro-Mechanics][7])

SEMCO also signed a roughly KRW 1.5T silicon capacitor supply contract with a global large-scale company for January 1, 2027 to December 31, 2028. ([Samsung Electro-Mechanics][8])

Those are strong facts. The problem is price.

| Layer | Why It Is a Bottleneck | Why It Is Not GPU/HBM Multiple by Default |
|---|---|---|
| FC-BGA | larger chips raise area, layer count and signal-integrity difficulty | capex-heavy, depreciation burden, ABF oversupply memory |
| MLCC | tiny part, but power failure can delay full server shipments | mixed with generic MLCC cycle, lower AI revenue purity |
| Si-Cap | die-near PDN component inside AI GPU / HBM packages | customer, margin, yield and repeat-order data mostly undisclosed |

ResearchAndMarkets estimates the global FC-BGA market rising from $2.46B in 2026 to $3.74B in 2032, a 7.1% CAGR. That market growth alone does not easily justify 100x P/E for some FC-BGA-related equities. ([Research and Markets][9])

So the conclusion is not "MLCC / FC-BGA is wrong." The better conclusion is: <strong>the direction is right, but the price demands evidence of LTAs, prepayments, margin and AI revenue purity</strong>.

---

## 6. Samsung Electronics vs Samsung Electro-Mechanics: Same Cycle, Different Price

### Samsung Electronics: AI Memory Hierarchy Option, Not Just Memory Cycle

Samsung Electronics is interesting not only because of HBM. It combines HBM4E catch-up, DDR5, SOCAMM2, eSSD / KV-cache storage and Samsung Foundry optionality. As argued in the [NVIDIA Vera Rubin inference-stack note](/post/nvidia-vera-rubin-lpx-cmx-inference-stack-samsung-hbm-2026-05-28/), inference is becoming a memory hierarchy problem across HBM, SRAM, eSSD, KV-cache and networking.

The input snapshot shows Samsung Electronics at roughly 7.8x forward P/E and 4.4x P/B. Its pure HBM exposure is lower than SK hynix's, but the valuation gap and HBM catch-up option make the risk/reward more attractive. ([Yahoo Finance][1])

Key checkpoints:

| Checkpoint | Meaning |
|---|---|
| HBM4E qualification | condition for closing the SK hynix valuation gap |
| DDR5 / server DRAM pricing | duration of the broader memory supercycle |
| eSSD / KV-cache | exposure to the AI inference memory hierarchy |
| Samsung Foundry | whether the custom ASIC option remains alive |

### Samsung Electro-Mechanics: Correct Thesis, Price First

SEMCO is one of the few Korean component companies with MLCC + FC-BGA + Si-Cap at once. As covered in the [SEMCO Si-Cap and EMIB-T note](/post/samsung-electro-mechanics-silicon-capacitor-emib-t-ai-package-pdn-2026-05-28/) and the [KRW 138T peer-premium note](/post/samsung-electro-mechanics-market-cap-murata-ibiden-premium-2026-05-28/), it can be reclassified as an AI package power-integrity supplier.

But reclassification potential and current stock attractiveness are different things. The input snapshot puts SEMCO around 195x TTM P/E, 100x+ forward P/E and roughly 16x P/B. That price requires not a "good company" but a company with <strong>repeat orders, high margins and a visible 2027-2028 earnings step-up</strong>.

What matters now is evidence, not story:

| Evidence Needed | Why It Matters |
|---|---|
| additional Si-Cap customers | distinguishes one big contract from platformization |
| Si-Cap margin | tests the high-value thesis |
| AI-server MLCC ASP | separates AI MLCC from commodity MLCC |
| FC-BGA utilization / OPM | tests whether capex-heavy risk is absorbed |
| LTAs / prepayments | confirms capex payback visibility |

---

## 7. Practical View

| Name | View | Reason |
|---|---|---|
| Samsung Electronics | Under / Buy-now candidate | low multiple versus HBM catch-up, memory pricing and foundry option |
| NVIDIA | Fair to relatively under | forward P/E is not extreme versus growth, but position sizing matters |
| SK hynix | Fundamental under, tactical wait | strong HBM alpha, but P/B and recent rally create entry risk |
| Micron | Fair to under, volatile | HBM / DRAM upside and P/B re-rating coexist |
| Broadcom | Fair to slightly over | strong AI ASIC visibility, already rich valuation |
| AMD | Over | CPU share gain alone struggles to defend the multiple |
| Intel | Over / avoid | turnaround expectations have run ahead of execution proof |
| Samsung Electro-Mechanics | Over / avoid chasing | thesis right, but repeat orders and high margins are already priced |
| Murata / Ibiden | Over | AI passive / substrate bottlenecks are real, but multiples already price monopoly-like outcomes |

The conclusion:

> The biggest mistake in this cycle is assigning a platform multiple to every component supplier just because it touches the NVIDIA supply chain.

GPU, HBM, MLCC and FC-BGA all matter. Their margin-capture structures differ. At current prices, Samsung Electronics and NVIDIA still have logical buy cases, while SK hynix and Micron look structurally cheap but timing-sensitive. Samsung Electro-Mechanics, Murata and Ibiden may be excellent companies, but the stocks may not be excellent at current prices.

---

## 8. Evidence Classification

### [Fact]

- NVIDIA FY2027 Q1 revenue was $81.6B, Data Center revenue was $75.2B, and Q2 revenue guidance was $91.0B. ([NVIDIA Investor Relations][2])
- Broadcom Q1 AI revenue was $8.4B, up 106% year over year, and Q2 AI semiconductor revenue guidance was $10.7B. ([Broadcom Inc.][3])
- AMD Q1 2026 data-center revenue was $5.8B, up 57% year over year. ([Advanced Micro Devices, Inc.][6])
- Samsung Electro-Mechanics Q1 2026 revenue was KRW 3.209T and operating profit was KRW 280.6B, with AI-server MLCC and AI accelerator / server-CPU FC-BGA cited as drivers. ([Samsung Electro-Mechanics][7])
- SEMCO signed an approximately KRW 1.5T silicon capacitor supply contract for January 1, 2027 to December 31, 2028. ([Samsung Electro-Mechanics][8])

### [Inference]

- NVIDIA deserves a higher multiple than normal semiconductor component suppliers because it is closer to an AI factory platform owner.
- Low forward P/Es in HBM reflect peak-memory-cycle doubt more than weak demand.
- Samsung Electronics has lower HBM purity than SK hynix but better relative risk/reward because of valuation gap plus HBM catch-up optionality.
- MLCC and FC-BGA bottlenecks have value, but without CUDA-like platform lock-in, 100x P/E requires repeat orders and margin proof.

### [Speculation]

- If HBM LTAs become fixed-price or prepayment-backed through 2027, SK hynix and Micron can deserve structurally higher memory multiples.
- If Samsung Electronics qualifies HBM4E quickly, Samsung may become the cleaner 2H26 alpha than SK hynix.
- If SEMCO's Si-Cap business expands into second and third AI ASIC customers, part of today's valuation burden may be explained after the fact.

### [Blocked]

- Vera Rubin MLCC / FC-BGA BOM, Murata versus SEMCO supply share, customer-specific LTAs / prepayments and FC-BGA pricing escalators are not public.
- SEMCO Si-Cap ASP, units, yield, OPM, customer name and take-or-pay terms are not public.
- Multiples in this post come from the 2026-05-29/30 public-data snapshot in the input, not real-time market data.

[1]: https://finance.yahoo.com/quote/005930.KS/key-statistics/ "Samsung Electronics Co., Ltd. (005930.KS) Valuation Measures & Financial Statistics"
[2]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx "NVIDIA Announces Financial Results for First Quarter Fiscal 2027"
[3]: https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-first-quarter-fiscal-year-2026-financial "Broadcom Inc. Announces First Quarter Fiscal Year 2026 Financial Results"
[4]: https://finance.yahoo.com/quote/000660.KS/key-statistics/ "SK hynix Inc. (000660.KS) Valuation Measures & Financial Statistics"
[5]: https://finance.yahoo.com/quote/MU/key-statistics/ "Micron Technology, Inc. (MU) Valuation Measures & Financial Statistics"
[6]: https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results "AMD Reports First Quarter 2026 Financial Results"
[7]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Announces Q1 2026 Business Performance"
[8]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
[9]: https://www.researchandmarkets.com/reports/6128754/fc-bga-market-global-forecast "FC BGA Market - Global Forecast 2026-2032"
