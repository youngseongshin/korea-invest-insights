---
title: "AI Server Passive-Component Bottlenecks: Why Tiny Power-Stability Parts Now Matter"
date: 2026-05-26
description: "AI server passive-component bottlenecks are not about a shortage of GPUs. They are about the higher-spec MLCCs, silicon capacitors, inductors, and filters needed to stabilize the huge transient power demands of GPU/HBM systems. This note explains the bottleneck and why it matters for Samsung Electro-Mechanics."
categories: ["Stock-Analysis"]
tags:
  - "Samsung Electro-Mechanics"
  - "009150"
  - "AI Server"
  - "Passive Components"
  - "MLCC"
  - "Silicon Capacitor"
  - "FC-BGA"
  - "Power Integrity"
  - "HBM"
  - "GPU"
slug: ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26
valley_body_mode: teaser
valley_cashtags:
  - 삼성전기
valley_cashtag_exclude:
  - 삼성전자
  - SK하이닉스
---

> Follow-up to the Samsung Electro-Mechanics series. See the pieces on [SEMCO at KRW 100T](/post/samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26/), [the KRW 1.5T silicon-capacitor contract](/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/), [MLCC vs silicon capacitors](/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/), and [AI chip-design bottlenecks](/post/ai-chip-design-data-movement-fcbga-bottleneck-2026-05-24/). Related hubs: [AI HBM](/page/korea-semiconductor-hbm-kospi-hub/), [AI PCB/substrate](/page/korea-ai-pcb-substrate-hub/), and [Korea semiconductor value chain](/page/korea-semiconductor-equipment-ip-hub/).

## TL;DR

- **The AI server passive-component bottleneck is not a GPU shortage.** It is the need for more and higher-spec parts that buffer, filter, and stabilize the power that GPUs consume.
- Think of an AI server as a high-performance engine. **MLCCs, silicon capacitors, and inductors are the fuel-pressure regulators, shock absorbers, and filters.**
- NVIDIA says a DGX GB200 rack consumes roughly **120kW**. Lenovo’s GB300 NVL72 guide cites **135kW TDP** and up to **155kW peak** per rack. ([NVIDIA][1], [Lenovo][2])
- The investable bottleneck is not generic MLCC. It is **high-capacitance, low-ESR, low-noise, low-profile AI server components**.
- Samsung Electro-Mechanics matters because it can connect **MLCC + FC-BGA + silicon capacitors** in one AI package power-integrity stack.

## One-Sentence Explanation

**AI server passive-component bottlenecks mean GPUs now draw such large and fast-changing currents that the small parts stabilizing voltage near the chip become a performance bottleneck.**

GPU performance is usually explained through GPUs, HBM, and networking. That is true, but those chips need a stable power base. When GPU load changes, current can swing rapidly. If voltage droops or noise spikes, the system can lose performance or stability.

## What Passive Components Do

| Component | Simple analogy | Role in an AI server |
|---|---|---|
| **MLCC / capacitor** | Water tank, shock absorber | Buffers current and absorbs voltage noise near chips and boards |
| **Silicon capacitor** | Tiny emergency battery next to the GPU | Stabilizes power inside or very near GPU/HBM packages |
| **Inductor** | Current inertia device | Smooths current in voltage conversion |
| **Resistor / filter / ferrite** | Speed limiter, noise filter | Reduces noise on high-speed signal and power lines |
| **VRM-side parts** | Power kitchen for the GPU | Converts 48V/12V rails into sub-1V GPU voltage |

TDK describes the data-center power chain as **UPS → PSU → IBC → VRM → CPU/GPU voltage**, with efficiency, ripple, heat tolerance, and long-term reliability required at every step. ([TDK][3])

## Why AI Servers Changed the Bottleneck

GPUs and CPUs can run below **1V**, while current can change by tens to hundreds of amperes depending on load. Samsung Electro-Mechanics says high-capacitance MLCCs near the GPU must act as current buffers for stable operation. ([Samsung Electro-Mechanics][4])

The bigger issue is peak power, not only average power. NVIDIA’s GB300 NVL72 PSU with energy storage is designed to smooth AI workload power spikes and reduce peak grid demand by up to 30%. ([NVIDIA Developer][5])

That logic travels down the stack. Rack-level power smoothing matters, but chip-near smoothing matters too. The closer the component is to the GPU/HBM package, the more valuable it becomes.

## MLCC vs Silicon Capacitor

| Item | Location | Role | Analogy |
|---|---|---|---|
| MLCC | Many places on board and near chips | Broad power stabilization | Fire extinguishers placed across the building |
| Silicon capacitor | Inside or right next to GPU/HBM package | Ultra-close transient suppression | Fuel-pressure control next to the engine cylinder |

Samsung Electro-Mechanics announced a roughly **KRW 1.5 trillion** silicon-capacitor supply contract for **2027-2028**. The company says the product improves power stability inside high-performance AI server semiconductor packages and has far lower ESL/ESR than conventional MLCCs. ([Samsung Electro-Mechanics][8])

## Samsung Electro-Mechanics Read-Through

The SEMCO thesis is not “MLCC prices go up.” It is:

```text
AI rack power rises
  → transient power swings become harder to manage
  → GPU/HBM packages need better power integrity
  → high-end MLCC, FC-BGA, and silicon capacitors gain strategic value
```

That is why SEMCO’s rerating is tied to **AI package power integrity**, not only the legacy smartphone component cycle.

The KPIs to watch:

1. AI server MLCC ASP and customer qualification
2. Silicon-capacitor revenue recognition from 2027
3. Additional silicon-capacitor customers or platforms
4. AI server and networking FC-BGA growth
5. Group operating margin moving toward the high-teens or 20% path

## Bottom Line

Passive components used to look like cheap background parts. In AI servers, they are becoming part of the performance stack. The GPU is the engine, HBM is the high-speed fuel tank, the substrate is the road, and MLCC/silicon capacitors keep the engine from stuttering.

That is the technical foundation behind the Samsung Electro-Mechanics, Murata, and TDK rerating thesis. It does not make every price attractive, but it explains why the category now deserves a different lens.

## Evidence Map

**Facts:** NVIDIA GB200 rack power, Lenovo GB300 rack power, TDK power-chain architecture, Samsung Electro-Mechanics AI MLCC and silicon-capacitor disclosures.

**Inference:** The bottleneck is a combination of higher quantity, higher specification, closer placement, and harder qualification.

**Blocked:** SEMCO’s exact silicon-capacitor customer, product margins, and platform-by-platform backlog are not public.

[1]: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html "Hardware — NVIDIA DGX GB Rack Scale Systems User Guide"
[2]: https://lenovopress.lenovo.com/lp2357-lenovo-nvidia-gb300-nvl72-rack-scale-ai "Lenovo NVIDIA GB300 NVL72 Rack Scale AI Product Guide"
[3]: https://product.tdk.com/en/techlibrary/applicationnote/mlcc-solution-for-data-center-psu.html "MLCC Solutions for Data Center Power Systems | TDK"
[4]: https://product.samsungsem.com/product-news/view.do?idx=3622&language=en "MLCC: The Key Component for AI Servers | Samsung Electro-Mechanics"
[5]: https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/ "How New GB300 NVL72 Features Provide Steady Power for AI | NVIDIA"
[6]: https://www.thelec.net/news/articleView.html?idxno=5588 "Samsung Electro-Mechanics mulls MLCC price increase | The Elec"
[7]: https://product.samsungsem.com/product-news/view.do?idx=3742&language=en "The Shift of AI Server Power Architectures | Samsung Electro-Mechanics"
[8]: https://m.samsungsem.com/kr/newsroom/news/view.do?id=10309 "삼성전기, 글로벌 대형기업과 1.5조 규모 실리콘 캐패시터 공급계약 체결"
