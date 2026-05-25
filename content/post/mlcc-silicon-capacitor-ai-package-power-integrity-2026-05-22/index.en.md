---
title: "Understanding MLCCs and Silicon Capacitors — What Samsung Electro-Mechanics' ₩1.5 Trillion Contract Reveals About the AI Package Power Bottleneck"
date: 2026-05-22
description: "An MLCC is an ultra-compact ceramic component used in almost every electronic device to stabilize power. A silicon capacitor is a high-performance component placed inside or immediately adjacent to AI GPU and HBM packages to suppress instantaneous power fluctuations. The critical insight is not that silicon capacitors replace MLCCs, but that the battlefield for passive components is expanding from the PCB surface into the interior of AI semiconductor packages. Samsung Electro-Mechanics' ₩1.5 trillion supply contract signals that MLCC and substrate companies may be re-classified as AI package power-integrity supply chain players. That said, the three core MLCC names surged an average of +35.6% this week and Samsung Electro-Mechanics now trades at 73x 2026E PER. A compelling industry shift and a compelling new entry price are two different things."
categories: ["Stock-Analysis"]
tags:
  - "MLCC"
  - "Silicon Capacitor"
  - "Samsung Electro-Mechanics"
  - "009150"
  - "AI Packaging"
  - "Power Integrity"
  - "Semiconductor Value Chain"
  - "Substrate"
slug: mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22
---

> 📚 Related Series
> [Samsung Electro-Mechanics Silicon Capacitor ₩1.5 Trillion Contract](/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [Samsung Electro-Mechanics Hybrid Challenger](/post/samsung-electro-mechanics-hybrid-challenger-2026-05-17/) / [Samsung Electro-Mechanics MLCC & FC-BGA Business Deep Dive](/post/samsung-electro-mechanics-mlcc-fcbga-ai-infrastructure-deep-dive-2026-05-15/) / [Semiconductor Value Chain Hub](/page/korea-semiconductor-equipment-ip-hub/) / [AI Substrate & PCB Hub](/page/korea-ai-pcb-substrate-hub/)

<figure>
  <img src="/img/posts/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/MLCC_Concept.png" alt="Conceptual diagram of MLCCs and silicon capacitors" loading="lazy">
</figure>

*An MLCC is one type of capacitor — an ultra-compact ceramic component found in virtually every electronic device, functioning as a power stabilizer. A silicon capacitor is placed closer to the semiconductor chip than an MLCC, in some cases inside the package itself, to suppress instantaneous power fluctuations in AI GPUs and HBM. From an investment standpoint, what matters is the signal that "passive components" are graduating from simple commodity parts to AI packaging and power-integrity bottleneck components.*

---

## Key Summary

A capacitor stores electrical charge briefly and releases it on demand. For non-engineers, think of it as a <strong>water tank, shock absorber, or noise filter for an electrical circuit</strong>. An MLCC is the highest-volume ceramic multilayer version of that capacitor. Samsung Electro-Mechanics describes MLCCs as playing the role of a "dam" — holding electricity and releasing it in controlled amounts.[^samsung-mlcc]

A silicon capacitor is also a type of capacitor. Unlike an MLCC, which stacks hundreds of ceramic layers, a silicon capacitor forms dielectric and electrode layers on a silicon wafer. According to Samsung Electro-Mechanics' product documentation, it can be thinned to under 100 micrometers, embedded inside a package, and benefits from low parasitic inductance that is favorable for power stabilization.[^samsung-sicap-product]

The essential point is <strong>not substitution but a shift in location</strong>. MLCCs are mounted primarily on the PCB surface or around the chip. Silicon capacitors can go inside the package, beneath the substrate, or directly adjacent to the die. Because AI GPUs and HBM draw sudden, large current spikes, proximity matters as much as raw capacitance — "how quickly can power be delivered" becomes as important as "how much can be stored."

Samsung Electro-Mechanics' May 20, 2026 silicon capacitor supply contract worth approximately ₩1.5 trillion is the first large-scale evidence of this structural shift. The contract runs from January 1, 2027 through December 31, 2028. The company stated that the product is embedded inside high-performance semiconductor packages — including AI server GPUs and HBM — to enhance power-supply stability.[^samsung-sicap-contract]

Investment judgment, however, must remain cold. This week (May 18–22), the three core MLCC names averaged <strong>+35.6%</strong>, handily outpacing the five core AI substrate names at <strong>+14.0%</strong>. Samsung Electro-Mechanics gained +32.7% on the week; Samwha Capacitor surged +56.4%. Theme momentum is unmistakable, but the efficiency of fresh capital deployment has diminished sharply.

The bottom line: <strong>the significance of silicon capacitors is not MLCC replacement — it is the expansion of the passive component battlefield from the PCB surface into the interior of AI semiconductor packages</strong>. Premium product lines at Samsung Electro-Mechanics and Murata may be re-classified as AI infrastructure supply chain assets. But a good industry shift and a good entry price remain entirely separate questions.

---

## 1. The Relationship Between Capacitors and MLCCs

A capacitor stores electrical charge and releases it rapidly when needed. When a semiconductor chip demands a sudden surge of current, a nearby capacitor supplies it, preventing voltage from collapsing. Conversely, when voltage spikes, the capacitor absorbs some of it, stabilizing the circuit. This is why capacitors serve the roles of energy storage, voltage smoothing, noise rejection, and power stabilization in electronic circuits.

An MLCC — <strong>Multi-Layer Ceramic Capacitor</strong> — is an ultra-compact capacitor constructed by stacking hundreds of thin ceramic dielectric layers alternating with metal electrode layers. Samsung Electro-Mechanics references production capability for high-capacitance MLCCs with up to 600 layers, noting that MLCC importance grows alongside the expansion of 5G, consumer electronics, autonomous vehicles, and the Internet of Things.[^samsung-mlcc]

The hierarchy is straightforward:

```text
Capacitor = the entire category of electrical stabilization components
MLCC = a mass-market, multilayer ceramic variant within that category
Silicon Capacitor = a high-performance, silicon-wafer-based variant optimized for ultra-close proximity
```

Both MLCCs and silicon capacitors are capacitors. They differ in where they are deployed and what performance demands they are designed to meet.

---

## 2. Capacitor vs. MLCC vs. Silicon Capacitor

| | General Capacitor | MLCC | Silicon Capacitor |
|---|---|---|---|
| Category | Broad family | One type of capacitor | One type of capacitor |
| Simple analogy | Circuit water tank | Ultra-compact ceramic water tank | Ultra-proximity water tank embedded next to or inside the chip |
| Key material | Ceramic, aluminum electrolyte, tantalum, film, silicon, etc. | Ceramic dielectric + internal metal electrodes | Silicon wafer-based structure |
| Primary role | Energy storage, voltage smoothing, noise rejection | High-frequency noise filtering, power stabilization around chips, miniaturization | Suppression of instantaneous power transients in AI GPUs, HBM, and high-performance chips |
| Typical location | Power stages, boards, modules, motors, inverters | Primarily on the PCB, around chips, around modules | Inside packages, within substrates, immediately adjacent to the die |
| Advantages | Wide selection across applications | Small, low-cost, mass-producible | Extremely thin; can be placed close to the die; favorable for power stabilization |
| Limitations | Large performance variance by type | Limited in ultra-high-speed, ultra-proximate package power stabilization | High manufacturing complexity and cost; current addressable market concentrated in high-performance semiconductors |
| Primary growth vectors | Automotive, power grid, industrial, AI server | Automotive, AI server, smartphone, 5G, IoT | AI GPU, HBM, high-performance computing, high-performance mobile chips |

Even a cursory look at TDK's capacitor product portfolio illustrates the breadth of the category: small MLCCs, high-voltage ceramic capacitors, film capacitors, aluminum electrolytic capacitors, and power capacitors all sit under the same "capacitor" umbrella.[^tdk-capacitors] "Capacitors are good" is too broad a statement. In investment terms, what matters is which capacitor, in which location, for which application.

---

## 3. Where They Are Used

### 3.1 General Capacitors

General capacitors appear in virtually every electrical circuit, from consumer electronics to power infrastructure.

| Application | Primary Capacitor Type | Role |
|---|---|---|
| Smartphone, PC | MLCC, tantalum, polymer | Power stabilization around application processors, memory, and PMIC |
| Server, AI server | MLCC, polymer, silicon capacitor | Suppression of power transients in CPUs, GPUs, and HBM |
| Automotive electronics | MLCC, film, aluminum electrolytic, tantalum | Stabilization of ECUs, ADAS, inverters, chargers, and BMS |
| EV power systems | Film, high-voltage MLCC, aluminum electrolytic | High-voltage DC link, charging, power conversion |
| Industrial, power grid | Film, aluminum electrolytic | Power factor correction, motor drives, energy storage |
| Telecom, high frequency | Ceramic, silicon capacitor | High-frequency filtering, impedance matching |

### 3.2 MLCC

The core application for MLCCs is <strong>power stabilization around chips</strong>. They appear in smartphones, automobiles, servers, network equipment, home appliances, and industrial machinery. As devices shrink, semiconductors switch faster, and the number of sensors and communication modules grows, the number of points requiring voltage stabilization increases proportionally.

MLCC importance in AI servers is also rising. TDK notes that as AI and cloud demand drives higher integration density and performance in data center servers, power density per rack and per server increases — making the performance and footprint of passive components a genuine design constraint.[^tdk-capacitors] This is why the MLCC thesis has expanded beyond a simple smartphone-cycle recovery story into AI server power stabilization.

### 3.3 Silicon Capacitors

The core application for silicon capacitors is <strong>power stabilization inside packages</strong>. Samsung Electro-Mechanics describes silicon capacitors as ultra-compact, high-performance devices built on silicon wafers, embedded inside high-performance semiconductor packages — including AI server GPUs and HBM — to enhance power-supply stability.[^samsung-sicap-contract]

The company's product documentation reinforces this: silicon capacitors form dielectric and internal electrodes on silicon, can be thinned to under 100 micrometers through wafer processing, and are well-suited for embedding inside packages. Low parasitic inductance is the key advantage for power stabilization.[^samsung-sicap-product]

To demystify the terminology:

```text
Parasitic inductance = an interference factor that delays the instantaneous response of current flow
Parasitic resistance = an interference factor that causes energy loss as current passes through
Power integrity = the ability to deliver stable, ripple-free voltage and current to a chip exactly when needed
```

AI semiconductors draw power in sudden, large spikes. A capacitor far from the die responds too slowly. The solution is to move the capacitor immediately adjacent to the chip — or inside the package itself. The investment case for silicon capacitors is not "higher capacitance" but <strong>faster response from a closer location</strong>.

---

## 4. Key Suppliers and Customer Base

### 4.1 MLCC Key Suppliers

| Region | Key Companies | Strengths |
|---|---|---|
| Japan | Murata, TDK, Taiyo Yuden | Ultra-small, high-reliability, automotive-grade MLCC leadership |
| Korea | Samsung Electro-Mechanics | High-value MLCC for IT, automotive, and AI server; expanding into silicon capacitors |
| Taiwan / Greater China | Yageo, Walsin | Commodity, industrial, and mid-to-low price passive component portfolio |
| US / Japan-affiliated | KYOCERA AVX, KEMET/Yageo, Vishay | Specialty capacitors, automotive, industrial, and high-frequency product lines |

The MLCC customer base is extremely broad: smartphone OEMs, PC and server manufacturers, automotive OEMs, Tier-1 suppliers, telecom equipment makers, and semiconductor module companies. For MLCC investing, <strong>demand mix by end-market and the share of high-value products</strong> matter more than exposure to any single customer.

### 4.2 Silicon Capacitor Key Suppliers

| | Key Companies | Positioning |
|---|---|---|
| Murata | Leader in silicon capacitors and integrated passive devices | High-performance mobile, telecom, and high-performance computing silicon capacitors |
| Samsung Electro-Mechanics | Large-scale new entrant | Secured approximately ₩1.5 trillion supply contract for 2027–2028 delivery |
| KYOCERA AVX et al. | Specialty MOS capacitors | High-frequency, microwave, and specialty industrial product lines |
| Advanced packaging ecosystem | Captive or co-design options | Linked to interposer and in-package power integrity technology |

The customer dimension is critical. MLCCs have a broad, substitutable customer base. Silicon capacitors, by contrast, must be designed into a package from the outset. They require customer qualification, integration into package architecture, and validation of power integrity. Once designed in, they are difficult to replace — the switching cost is high.

Samsung Electro-Mechanics' contract counterparty is officially disclosed only as a "large global corporation." It would therefore be incorrect to identify the customer as NVIDIA, AMD, Broadcom, Google, Meta, Microsoft, Amazon, or any other specific company. That remains unconfirmed.

---

## 5. What Silicon Capacitors Actually Signify

### 5.1 Technical Significance — The Power Bottleneck Migrates Inside the Package

As AI GPUs and HBM scale in compute intensity and data movement, instantaneous current demand has grown substantially. The problem is that power arriving from a distance is slowed by parasitic elements in the power traces, substrate, and package — degrading the transient response. The solution is to move capacitors closer to the die.

Conventional MLCCs sit primarily on the PCB or around the package perimeter. Silicon capacitors can go inside the package or immediately adjacent to the die. With capacitors of equivalent capacitance, <strong>placement determines performance</strong>.

### 5.2 Business Significance — Passive Components Re-rated as AI Packaging Components

MLCCs have traditionally been priced as cyclical components. When smartphone and PC demand weakens, inventory adjustments follow, and commodity products face price competition. Silicon capacitors, in contrast, are high-complexity components embedded inside AI GPU and HBM packages. They require customer qualification, integration into package design, and power-integrity validation.

For Samsung Electro-Mechanics, this contract carries strategic significance beyond the revenue figure. The company officially stated that it leveraged its accumulated precision process capabilities from the MLCC and package substrate businesses to enter the AI semiconductor core supply chain.[^samsung-sicap-contract]

### 5.3 Investment Significance — Possible Re-classification as "AI Server Component" Plays

The market has historically viewed Samsung Electro-Mechanics as an MLCC, camera module, and substrate company. If silicon capacitor revenue scales into mass-production levels, that classification partially changes.

| Prior Market Perception | Possible Post-Silicon-Capacitor Perception |
|---|---|
| Smartphone component play | AI server component play |
| MLCC cycle stock | High-value power integrity component stock |
| Automotive MLCC growth story | AI GPU / HBM packaging supply chain entrant |
| Exposure to commodity passives | Exposure to high-complexity in-package components |

Overclaiming risks remain, however. Silicon capacitors will not replace the entire MLCC market. Growth will come first in AI package interiors, high-performance computing, high-performance mobile chips, and select telecom and industrial applications where extreme performance is required. The vast majority of power stabilization demand in mainstream smartphones, automobiles, and home appliances will likely remain the domain of MLCCs for the foreseeable future.

---

## 6. This Week's Tape — MLCCs Outran AI Substrates

This week (May 18–22, 2026), the market aggressively re-rated the MLCC theme. The three core MLCC names averaged <strong>+35.6%</strong>; the five core AI substrate names averaged <strong>+14.0%</strong>.

### 6.1 Core MLCC Three-Name Basket

| Name | Weekly Return | 20D | 60D | 2026E PER | Foreign | Institution | Foreign + Inst. | Program |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Samwha Capacitor | <strong>+56.4%</strong> | +56.0% | +68.0% | 40.8x | -₩5.88B | +₩16.09B | +₩10.21B | N/A |
| Samsung Electro-Mechanics | <strong>+32.7%</strong> | +65.0% | +200.5% | 73.2x | -₩292.90B | +₩111.79B | -₩181.11B | +₩170.96B |
| Amotech | +17.6% | -18.4% | +55.2% | 18.9x | +₩4.91B | -₩0.87B | +₩4.05B | +₩5.10B |

Samsung Electro-Mechanics posted three consecutive sessions of strength: +7.5% on May 20, +13.5% on May 21, and +11.3% on May 22. Samwha Capacitor was more extreme: +23.0% on May 20, +29.9% on May 22. This is less a pure earnings-driven move than <strong>a re-rating of AI power-integrity components that originated with Samsung Electro-Mechanics and radiated outward into the MLCC ecosystem</strong>.

### 6.2 Core AI Substrate Five-Name Basket

| Name | Weekly Return | 20D | 60D | 2026E PER | Foreign | Institution | Foreign + Inst. | Program |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|심텍 (심텍) | <strong>+31.4%</strong> | +52.2% | +146.8% | 38.7x | -₩24.58B | +₩61.81B | +₩37.22B | -₩5.35B |
| TLB | +18.0% | +44.4% | +89.2% | 25.3x | -₩7.80B | +₩15.30B | +₩7.50B | -₩3.98B |
| Daeduck Electronics | +11.4% | +49.5% | +132.8% | 38.9x | -₩2.93B | +₩29.05B | +₩26.12B | +₩5.28B |
| Korea Circuit | +10.7% | +5.6% | +66.7% | 25.5x | -₩2.71B | -₩0.58B | -₩3.29B | +₩0.44B |
| ISU Petasys | -1.5% | -21.9% | +12.7% | 35.6x | -₩119.17B | -₩0.74B | -₩119.90B | -₩125.28B |

The AI substrate basket was not a uniformly rising tide. Simtech, TLB, and Daeduck Electronics were strong, but ISU Petasys finished the week at -1.5% amid heavy foreign and program selling. Within AI substrates, the market this week appeared to favor <strong>SoCAMM, memory module, and FC-CSP exposure over high-layer-count network boards</strong>.

### 6.3 Price Leadership to MLCCs; Flow Quality Favors Select AI Substrate Names

| Basket | Foreign | Institution | Foreign + Inst. | Retail | Program |
|---|---:|---:|---:|---:|---:|
| Core MLCC (3 names) | -₩293.86B | +₩127.01B | -₩166.85B | +₩159.40B | +₩176.05B |
| Core AI Substrate (5 names) | -₩157.19B | +₩104.84B | -₩52.35B | +₩52.05B | -₩128.89B |
| AI Substrate ex-ISU Petasys | -₩38.02B | +₩105.57B | +₩67.55B | -₩65.47B | -₩3.60B |

On price, MLCCs dominated. On flow quality, <strong>the AI substrate basket excluding ISU Petasys</strong> looks cleaner. Simtech, TLB, and Daeduck show clear institutional accumulation with retail sellers or neutral retail — a more constructive configuration. In MLCC names, the ₩292.9 billion of foreign selling in Samsung Electro-Mechanics alone is too large to ignore. The stock price was strong, but this looks more like institutional, program, and retail-driven re-rating than foreign-led accumulation.

---

## 7. Investment Assessment

| Name | View |
|---|---|
| MLCC | Strongest price momentum. Overheating risk and foreign selling overhang present. |
| AI Substrates | Lower absolute return, but institutional flow and earnings linkage are more stable. |
| Samsung Electro-Mechanics | Cross-category leader across MLCC, FC-BGA, and silicon capacitors. Holding is defensible; chasing is not. |
| Samwha Capacitor | Highest theme expansion intensity. +56% in one week makes new entry extremely difficult. |
| Daeduck Electronics | Core AI substrate holding. Valuation discount relative to Samsung Electro-Mechanics is meaningful. |
| Simtech / TLB | Led this week's AI substrate expansion. Next week, monitor for a post-heat consolidation before re-entry. |
| ISU Petasys | Relative laggard within AI substrates. Lower priority until foreign flow stabilizes. |

This week's market was one in which <strong>attention expanded from AI substrates into MLCCs</strong>. The AI substrate thesis has not been invalidated. Rather, the market is now disaggregating "the next bottleneck after memory" more finely — extending the re-rating into AI server power integrity components.

In practical terms:

```text
Hold: Samsung Electro-Mechanics, Daeduck Electronics
Do not chase: Samsung Electro-Mechanics, Samwha Capacitor
Monitor on pullback: Simtech, TLB
Await flow recovery: ISU Petasys
Key confirmation needed: Whether MLCC price increases and AI-server revenue lift 2Q–3Q earnings revisions
```

---

## 8. One-Line Takeaway

An MLCC is the electronic industry's "ultra-compact ceramic water tank." A silicon capacitor is an "ultra-proximity power stabilizer" embedded inside AI GPU and HBM packages. Silicon capacitors do not replace MLCCs. The battlefield for passive components is expanding from the PCB surface into the interior of AI semiconductor packages.

The real meaning of Samsung Electro-Mechanics' ₩1.5 trillion contract is not "selling one more type of capacitor." It is the signal that <strong>a passive component maker has entered the bottleneck component supply chain inside AI semiconductor packages</strong>. This shift can re-classify premium product lines at Samsung Electro-Mechanics and Murata into AI infrastructure value chain assets.

The market has, however, already responded quickly. The three core MLCC names averaged +35.6% this week; Samsung Electro-Mechanics is up +200.5% over 60 days and trades at 73.2x 2026E PER. The company is excellent and the industry shift is real. Whether today's price is also a good new entry point is a separate question entirely. The next catalyst to monitor is not price action but <strong>2Q–3Q earnings revisions, disaggregated AI-server revenue disclosure, follow-on silicon capacitor orders, and foreign flow recovery</strong>.

---

*This post is for research and commentary purposes only and does not constitute investment advice. Technical descriptions of capacitors, MLCCs, and silicon capacitors are based on official materials from Samsung Electro-Mechanics, TDK, Murata, and other publicly available technical sources. The Samsung Electro-Mechanics silicon capacitor supply contract (approximately ₩1.5 trillion, January 1, 2027 through December 31, 2028) reflects the company's official announcement. The customer has not been publicly disclosed; no specific GPU, ASIC, or cloud company has been identified as the counterparty. Price, flow, and valuation data for the May 18–22, 2026 period are sourced from the user's Research OS local database and may differ from official exchange or brokerage data. 2026E PER, foreign/institutional/program flow figures, and basket averages for the core MLCC three-name and core AI substrate five-name groups reflect the analyst's classification. Analysis may be wrong. Data reference date: May 22, 2026, KST.*

[^samsung-mlcc]: [Samsung Electro-Mechanics, MLCC Product Description](https://samsungsem.com/kr/product/passive-component/mlcc.do)
[^samsung-sicap-product]: [Samsung Electro-Mechanics, Silicon Capacitor Product Description](https://www.samsungsem.com/global/product/passive-component/silicon-capacitor.do)
[^samsung-sicap-contract]: [Samsung Electro-Mechanics, ₩1.5 Trillion Silicon Capacitor Supply Contract Announcement](https://samsungsem.com/global/newsroom/news/view.do?id=10310)
[^tdk-capacitors]: [TDK, Capacitor Product Portfolio and AI Server Power System Application Materials](https://product.tdk.com/en/products/capacitor/index.html)

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
