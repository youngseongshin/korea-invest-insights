---
title: "Samsung Foundry Customer List 2026 — Who Uses Samsung Foundry? Tesla, Tenstorrent, Qualcomm, Google, Ambarella, and the Rest of the Confirmed Stack"
slug: samsung-foundry-customer-list-tesla-tenstorrent-2026-05-03
date: 2026-05-03T11:00:00+09:00
description: "Samsung Foundry customers in 2026 — confirmed via earnings calls, customer disclosures, and supply-chain reporting — include Tesla (HW5/Dojo successor at SF2), Tenstorrent (Wormhole/Blackhole at SF4X), Qualcomm (selected modem and Snapdragon nodes), Google (TPU successors and Pixel SoC at SF4LPP/SF3), Ambarella (CV3-AD ADAS), and Samsung's own System LSI (Exynos). The honest answer is that Samsung Foundry remains a credible #2 to TSMC at advanced nodes, with the customer roster heavily weighted toward AI accelerators, automotive/ADAS SoCs, and customers willing to take a calculated yield-risk premium for capacity availability or sovereign-supply reasons."
categories: ["Sector-Deep-Dive", "Korea Market", "AI Infrastructure"]
tags:
  - "Samsung Foundry"
  - "005930"
  - "Samsung Electronics"
  - "Tesla"
  - "Tenstorrent"
  - "Qualcomm"
  - "Google"
  - "Ambarella"
  - "TSMC"
  - "AI chip"
  - "foundry"
  - "semiconductor"
  - "SF2"
  - "SF3"
  - "SF4"
  - "Korean equities"
---

> 🔗 **Related reads**: [SK hynix HBM market share](/post/sk-hynix-hbm-market-share-ai-memory-demand-2026/) · [OpenEdges Technology — LPDDR6/5X data-center IP alpha](/post/openedges-lpddr-datacenter-ip-alpha-thesis-2026-04-30/) · [Big Tech 1Q26 → Samsung Electronics vs Samsung Electro-Mechanics](/post/bigtech-1q26-samsung-electronics-vs-electro-mechanics-2026-04-30/)

*This post answers the direct question — "Who uses Samsung Foundry in 2026?" — and then explains why each customer is there, what node they sit on, and what the customer composition tells you about Samsung Foundry's positioning vs TSMC.*

---

## TL;DR

**The short answer.** Samsung Foundry's confirmed 2026 customer list, weighted by economic relevance, includes:

- **Tesla** — multi-generation customer (HW3 → HW4 prep work), with the next-generation autonomous-vehicle SoC and Dojo-related accelerators at advanced Samsung nodes (SF4 / SF3 / SF2 reported in trade press).
- **Tenstorrent** — Wormhole and Blackhole AI accelerator families on Samsung Foundry advanced nodes, including the 4nm-class SF4X. The Jim Keller-led ASIC house is a public Samsung Foundry partner.
- **Qualcomm** — split sourcing across Samsung Foundry and TSMC; certain modem (5G/6G) and selected Snapdragon SoC variants have historically been built at Samsung's advanced nodes.
- **Google** — Pixel Tensor SoCs (G3/G4-class) at Samsung's 4nm-class nodes; selected TPU-related production work has historically used Samsung capacity, with TSMC also prominent in the latest TPU generations.
- **Ambarella** — CV3-AD ADAS automotive SoCs at Samsung's 5nm-class node.
- **Samsung System LSI** — Exynos 2400 / Exynos Auto / image-sensor logic, the captive workload anchoring Samsung Foundry capacity.
- **NVIDIA-adjacent and AI-startup work** — selected accelerator and networking chips have used Samsung capacity historically.
- **Korean and Japanese fabless** — Rebellions, FuriosaAI (next-gen Renegade), DB HiTek-tier customers, and Asian AI-ASIC houses use Samsung Foundry's 4 / 5 / 8 / 12nm production lines.

**The honest read.** Samsung Foundry in 2026 is **not** TSMC's equal at the bleeding edge — TSMC still wins the highest-volume bleeding-edge AI accelerator work (NVIDIA, AMD, Apple silicon). What Samsung Foundry **is** in 2026 is a credible #2 with a customer roster heavily weighted toward (a) AI accelerators that need capacity outside TSMC, (b) automotive / ADAS SoCs, (c) customers willing to take a yield-risk premium for capacity, sovereign-supply, or pricing reasons. The customer composition is exactly what you'd expect of a "challenger foundry with real advanced-node capability and persistent yield questions."

---

## 1. Why "Who Uses Samsung Foundry?" Is the Right Question to Ask

Samsung Foundry's positioning has been the subject of more conflicting trade-press coverage than almost any other topic in semiconductors. One week the headline is "Samsung wins Tesla / Qualcomm / Google" — the next week it is "Samsung loses [X] to TSMC."

Cutting through the noise requires a different question. Not "is Samsung Foundry winning?" — that question can't be answered cleanly because it depends on whose model you take. Instead: **who actually uses Samsung Foundry in 2026, and what does the customer mix tell you?**

The customer mix is the only honest read of foundry-positioning, because:

1. **Capacity allocation is observable.** Customer disclosures, earnings-call references, and trade-press supply-chain reporting reveal who is actually printing wafers at which fab.
2. **Customer composition encodes yield, capacity, and pricing tradeoffs.** A foundry that wins a customer at an advanced node either has that node's yield problem solved, has a capacity advantage TSMC can't match, or is pricing aggressively. The customer mix tells you which.
3. **Customer mix predicts 2027–2028 utilization.** Samsung Foundry's 2026 customer roster largely defines its 2027 production volumes. The customers visible today *are* the next two years of revenue.

---

## 2. The Confirmed Customer Stack — Who, Where, and Why

### 2.1 Tesla — The Multi-Generation Anchor

**Status.** Tesla has been a Samsung Foundry customer across multiple generations. The Hardware 3 (HW3) FSD chip was built at Samsung's 14nm node. The Hardware 4 (HW4) chip moved to Samsung's 7nm-class node. The Hardware 5 / next-generation autonomous-vehicle SoC has been associated in trade-press reporting with Samsung's SF4 and forward-roadmap nodes (SF3 / SF2), with continued Samsung capacity use through 2026 and beyond.

**Why Samsung.** Tesla has consistently operated dual-vendor wafer sourcing — TSMC for Dojo-class GPU/AI accelerator production, Samsung for the FSD/HW SoC. The Samsung commitment likely reflects a combination of (a) capacity availability TSMC could not match for Tesla's volume, (b) pricing leverage Tesla extracted from Samsung's challenger position, and (c) the multi-year FSD-platform continuity built into the relationship since HW3.

**What it means for Samsung.** Tesla is the closest thing Samsung Foundry has to a "trophy customer" — a high-profile US-listed name whose vehicles depend on Samsung-fabbed silicon. Losing Tesla to TSMC would be one of the most damaging signals available; keeping Tesla through HW5 is one of the strongest positive signals.

### 2.2 Tenstorrent — Jim Keller's Public Samsung Bet

**Status.** Tenstorrent's Wormhole AI accelerator and the next-generation Blackhole are publicly disclosed as Samsung Foundry production. Tenstorrent's CEO Jim Keller has given multiple public interviews discussing the Samsung Foundry partnership, with the company moving advanced-node production work to Samsung's 4nm-class SF4X.

**Why Samsung.** Tenstorrent's positioning is "the AI accelerator startup that bets against the NVIDIA/CUDA stack." Choosing Samsung over TSMC for advanced-node production is consistent with that contrarian positioning. Samsung's capacity availability and a more flexible engagement model than TSMC's tier-1-customer-priority framework are believed to be material factors.

**What it means for Samsung.** Tenstorrent is the most public AI-accelerator endorsement Samsung Foundry has. As Tenstorrent shipments scale, Samsung Foundry's revenue exposure to non-NVIDIA AI accelerators increases. This is a meaningful diversification away from "Samsung Foundry = Samsung System LSI captive workload."

### 2.3 Qualcomm — Dual-Sourced Across Samsung and TSMC

**Status.** Qualcomm's flagship Snapdragon SoCs have historically been split between Samsung Foundry and TSMC across generations. The Snapdragon 8 Gen 1 was a notable Samsung 4nm-class win; subsequent flagships (Snapdragon 8 Gen 2, Gen 3, Snapdragon 8 Elite) moved primarily to TSMC. However, Qualcomm continues to produce certain modem and lower-tier Snapdragon variants at Samsung Foundry capacity.

**Why Samsung.** Dual-sourcing protects Qualcomm against TSMC capacity squeezes and pricing leverage. The Samsung relationship gives Qualcomm a credible negotiating position with TSMC. For Samsung Foundry, the Qualcomm relationship — even at sub-flagship volume — is an important reference customer that signals "Samsung's nodes are commercially production-grade."

**What it means for Samsung.** The Qualcomm volume at Samsung Foundry is not the headline-grabbing flagship-Snapdragon work; it's the steady production work that fills mid-tier capacity. Watch for Snapdragon 8 Gen 5 or future flagships returning to Samsung Foundry — that would be a major positive signal.

### 2.4 Google — Pixel Tensor SoCs and Selected TPU Work

**Status.** Google's Pixel Tensor (G1, G2, G3, G4) SoCs have been built at Samsung Foundry, leveraging Samsung's modified Exynos-derived design IP and 5nm/4nm-class production. Some TPU production (older generations, supplemental capacity) has historically used Samsung; the latest TPU generations are predominantly at TSMC.

**Why Samsung.** Pixel Tensor's design lineage from Samsung System LSI's IP makes Samsung Foundry the natural production partner. For TPU work, Samsung has been a capacity supplement rather than a primary partner.

**What it means for Samsung.** Google Pixel volume is not enormous in absolute foundry terms, but the relationship is high-profile and creates pull-through demand for Samsung's 4nm-class node. The bigger swing factor is whether next-generation TPUs ever return meaningfully to Samsung capacity.

### 2.5 Ambarella — Automotive ADAS SoCs

**Status.** Ambarella's CV3-AD family — the company's flagship automotive AI accelerator for ADAS and autonomous-driving applications — is built at Samsung Foundry's 5nm-class node. Ambarella has publicly disclosed Samsung Foundry as its 5nm partner.

**Why Samsung.** Automotive customers value (a) supply continuity — Samsung's commitment to long-term automotive-grade production, (b) capacity availability — TSMC's automotive 5nm capacity is heavily oversubscribed by Apple/AMD/NVIDIA, (c) Samsung's automotive-grade quality system credentialing.

**What it means for Samsung.** Ambarella is the cleanest "automotive 5nm" reference customer Samsung has. As ADAS / L2+ / L3 autonomy scales across global OEMs, the customer pull on Samsung's automotive-grade advanced-node capacity rises.

### 2.6 Samsung System LSI — The Captive Workload Anchor

**Status.** Samsung's own System LSI division — Exynos mobile SoCs, Exynos Auto for automotive, image-sensor logic, modem ICs — is the largest captive customer of Samsung Foundry. Exynos 2400 (Galaxy S24 series), Exynos Auto V920 (Hyundai Pleos / Kia partnerships), and image-sensor logic are all at Samsung Foundry advanced nodes.

**Why Samsung.** Captive — by definition.

**What it means for Samsung.** This is the floor. Even if every external customer disappeared tomorrow, Samsung System LSI would keep Samsung Foundry's advanced-node fabs running. The captive workload is also the source of much of Samsung Foundry's IP development, yield-learning curve, and process maturation. The honest interpretation: external customer wins matter as **upside on top of** the captive base.

### 2.7 The Korean and Asian Fabless Layer

**Status.** A long tail of Korean and Asian fabless customers uses Samsung Foundry at the 4 / 5 / 8 / 12 / 14nm nodes. Confirmed and publicly-discussed customers include:

- **Rebellions** — Korean AI accelerator startup (REBEL-Quad / next-generation accelerator at Samsung advanced nodes).
- **FuriosaAI** — Renegade chip on Samsung Foundry's 5nm; next-generation parts in development.
- **DeepX** — Korean edge AI startup, Samsung Foundry.
- **OpenEdges Technology** — Korean memory subsystem IP (LPDDR6/5X PHY/Controller silicon-proven on Samsung SF5A; in development on Samsung 4nm).
- **Various Japanese fabless** — automotive, image-sensor, and AI workloads.

**Why Samsung.** Geographic proximity, Korean-language IR/engineering support, Samsung SAFE IP partner ecosystem (Cadence, Synopsys, OpenEdges as Sub-License partner), and pricing accessibility for non-tier-1 customers.

**What it means for Samsung.** This layer is unsexy but durable. It is the layer that makes Samsung Foundry's volume-process utilization viable at the 4 / 5 / 8nm nodes. It is also the layer that benefits most directly from any AI ASIC startup wave originating in Korea or Asia.

### 2.8 The "Used to Be a Customer" Set

For accuracy, several major names are **no longer** primary Samsung Foundry customers despite older trade-press references:

- **NVIDIA** — A8000 / GA100-era Ampere GPUs were partially Samsung 8nm, but the market quickly moved to TSMC for Hopper, Blackwell, and Rubin. NVIDIA today is overwhelmingly TSMC.
- **Apple** — Has not been a meaningful Samsung Foundry customer for advanced-node iPhone/Mac silicon since the A9 era. All current Apple silicon is TSMC.
- **AMD** — Bleeding-edge AMD CPUs/GPUs are TSMC; some legacy AMD work used GlobalFoundries; Samsung is not a current advanced-node AMD partner of meaningful scale.

Customer turnover is real. Samsung Foundry's 2026 mix is structurally different from its 2020 mix.

---

## 3. What the Customer Composition Tells You

### 3.1 Customer-Mix Pattern Recognition

Reading the 2026 confirmed list as a single picture, four patterns emerge:

| Pattern | What it says about Samsung Foundry |
| --- | --- |
| **Heavy AI-accelerator weighting (Tenstorrent, Tesla, Rebellions, FuriosaAI, Ambarella)** | The challenger position is real. Samsung is the "AI accelerator that doesn't go to TSMC" foundry. |
| **Strong automotive/ADAS exposure (Tesla, Ambarella, Samsung Auto, Hyundai Pleos)** | Automotive is a structural advantage where Samsung's long-term commitment, capacity, and quality systems beat TSMC's automotive-tier-2 status. |
| **Captive Samsung System LSI as the floor** | The fab utilization floor is independent of external-customer wins. |
| **Mid-tier mobile (Qualcomm sub-flagship, Google Pixel, Korean/Asian fabless)** | Samsung is competitive at the 4 / 5 / 8 / 12nm "production-volume sweet spot" rather than at the bleeding edge. |

### 3.2 What Is *Not* Yet on the List (and Why It Matters)

Equally informative: who is **not** on the Samsung Foundry customer list as of 2026.

- **No bleeding-edge AI hyperscaler** — NVIDIA, AMD, Apple silicon, Microsoft Maia (TSMC), Meta MTIA (TSMC) are all TSMC. Samsung's 2nm-class effort (SF2) is yield-and-customer-uncertain into 2027.
- **No flagship Snapdragon at SF3 / SF2 reported.** Until that changes, Samsung's mobile flagship volume gap remains.

These absences are *not* failure. They are the gap Samsung's SF2 and SF1.4 nodes have to close in 2027–2028 to move from "credible #2" to "commercial parity with TSMC."

### 3.3 The Challenger-Foundry Read

Reduced to one sentence: **Samsung Foundry in 2026 is winning the customers that need capacity, want to avoid TSMC concentration, or value automotive-grade long-term commitment — and is not yet winning the bleeding-edge hyperscaler AI accelerator volume.**

That is exactly the customer profile of a credible #2 in a duopoly, with sustained challenger optionality on the next nodes.

---

## 4. Implications for Samsung Electronics Equity

This isn't a stock-recommendation post, but the customer composition has direct implications for how to read Samsung Electronics (KS: 005930):

1. **Samsung Foundry is not the bleeding-edge revenue line.** The bleeding-edge AI memory upside for Samsung Electronics flows through DS Memory (HBM4 customer expansion to NVIDIA, AI server DRAM), not through Samsung Foundry's external-customer wins. Conflating the two leads to misreads.
2. **Samsung Foundry's customer wins are durable, not explosive.** Tesla, Tenstorrent, Ambarella, Google Pixel, and the Korean/Asian fabless layer compound steadily. They don't generate a single quarter that re-rates the equity.
3. **The 2nm-class (SF2) inflection is the real swing variable.** Whether Samsung Foundry can win at least one major external AI customer at SF2 in 2027–2028 is the binary outcome that materially repositions Samsung Foundry's revenue trajectory and Samsung's overall foundry-segment margin profile.
4. **The Korean / Asian AI ASIC layer becomes meaningful with multiple customer scaling.** A single Rebellions or FuriosaAI win is small. Five-to-ten Korean / Asian AI accelerator startups simultaneously scaling on Samsung 4 / 5nm capacity becomes material.

---

## 5. FAQ

**Q: Is Samsung Foundry the same as Samsung Electronics?**
A: Samsung Foundry is the contract-chip-manufacturing division of Samsung Electronics (KOSPI: 005930). It sits inside Samsung's DS (Device Solutions) division alongside Memory and System LSI. It is not a separately listed entity.

**Q: Is Samsung Foundry publicly traded?**
A: Not separately. To get exposure, you buy Samsung Electronics (005930). Samsung Foundry's revenue and operating profit are reported as part of the DS Foundry segment within Samsung Electronics' consolidated financials.

**Q: What process nodes does Samsung Foundry currently produce on?**
A: As of 2026, Samsung Foundry is in production on 14 / 8 / 7 / 5 / 4 / 3nm-class nodes. The 3nm-class GAA (gate-all-around) node has been in production since 2022, with continued yield-and-customer ramp. The 2nm-class (SF2) is the next major node target.

**Q: Who is Samsung Foundry's biggest customer?**
A: Captive — Samsung System LSI (Exynos, image sensor, modem) is the single largest internal workload. Among external customers, Tesla and Qualcomm have historically been the highest-volume names; Tenstorrent and Google Pixel are also significant.

**Q: Does Samsung Foundry make NVIDIA chips?**
A: Not in 2026's current generation. NVIDIA's bleeding-edge AI accelerators (Hopper, Blackwell, Rubin) are at TSMC. Samsung produced NVIDIA's Ampere-generation GPUs at 8nm, but NVIDIA migrated to TSMC for subsequent generations.

**Q: Does Samsung Foundry compete with TSMC?**
A: Yes — Samsung is widely considered TSMC's #2 challenger at advanced nodes. TSMC retains the bleeding-edge AI hyperscaler customer base; Samsung competes effectively in automotive, AI accelerator startups, mobile mid-tier, and Korean/Asian fabless segments.

**Q: Is Samsung Foundry losing customers to TSMC?**
A: Customer turnover happens both ways. Samsung lost meaningful Apple / NVIDIA / AMD bleeding-edge volume through the 2018–2024 period. It has gained Tesla multi-generation continuity, Tenstorrent, Ambarella, and a growing Korean / Asian fabless customer base. The 2026 customer mix is structurally different from 2020.

**Q: What is the SF2 node?**
A: SF2 is Samsung Foundry's 2nm-class process, on the company's published roadmap for late-2025/2026 production ramp. Whether Samsung wins major external customers at SF2 — particularly any bleeding-edge AI accelerator — is the most-watched 2026–2027 inflection for Samsung Foundry's positioning.

---

## 6. Closing Frame

The single most informative thing you can do with the question "Who uses Samsung Foundry?" is to **let the answer change how you frame Samsung Foundry itself**. Read as a list of names, the 2026 customer roster says "Samsung Foundry is a serious foundry with serious customers." Read as a *pattern* — heavy AI accelerator + automotive + Korean / Asian fabless + captive Samsung System LSI — the same list says "Samsung Foundry is the credible challenger to TSMC, with the customer mix you'd expect of a #2 in a duopoly."

Both reads are right. Which one matters for your decision depends on whether you're asking the question for procurement, for equity allocation, or for understanding the global semiconductor map. For all three, the answer is more useful than the headline noise suggests.

---

## Appendix — Evidence Tier

### [Fact]

- Samsung Foundry is the contract-chip-manufacturing division of Samsung Electronics (KOSPI: 005930), sitting inside the DS (Device Solutions) division alongside Memory and System LSI.
- Tesla has been a multi-generation Samsung Foundry customer (HW3 at 14nm, HW4 at 7nm-class, ongoing engagement on subsequent generations).
- Tenstorrent's Wormhole and Blackhole accelerators are produced at Samsung Foundry advanced nodes including SF4X.
- Qualcomm has dual-sourced across Samsung Foundry and TSMC, with the Snapdragon 8 Gen 1 notably built at Samsung 4nm.
- Google Pixel Tensor SoCs (G1–G4) have been built at Samsung Foundry.
- Ambarella's CV3-AD ADAS family is at Samsung's 5nm-class node.
- Samsung System LSI (Exynos, image-sensor logic, modem) is the captive workload at Samsung Foundry.
- Korean fabless customers including Rebellions, FuriosaAI (Renegade), DeepX, and OpenEdges Technology use Samsung Foundry's 4 / 5 / 8 / 12nm nodes.
- NVIDIA's Hopper / Blackwell / Rubin generations are at TSMC, not Samsung.
- Apple silicon is at TSMC, not Samsung, since the A9 era.

### [Inference]

- The Tesla relationship through HW5 is Samsung Foundry's most-watched single external-customer continuity signal.
- The Tenstorrent partnership represents Samsung Foundry's clearest non-NVIDIA AI-accelerator endorsement.
- Customer-mix concentration in AI accelerators, automotive, and Korean/Asian fabless reflects Samsung's challenger positioning — capacity availability, dual-source value, and pricing flexibility — rather than bleeding-edge yield parity with TSMC.
- The SF2 (2nm) node's external-customer roster will be the single largest input into how Samsung Foundry is repositioned in the global foundry duopoly through 2027–2028.

### [Speculation]

- A flagship Snapdragon return to Samsung Foundry at SF3 or SF2 would be a major positive re-rating signal for Samsung's foundry segment.
- Continued Tesla commitment through HW5 and beyond would anchor Samsung's automotive-grade advanced-node revenue at meaningful scale through 2028.
- A Samsung Foundry win on at least one external AI hyperscaler accelerator at SF2 would shift the current "credible #2" framing materially toward "commercially competitive at the bleeding edge."

### [Blocked]

- Specific customer-by-customer wafer volume contributions to Samsung Foundry's quarterly DS Foundry revenue.
- Samsung Foundry's per-node yield curves and learning-rate trajectories.
- Confidential tier-1 customer pricing terms that would directly compare TSMC and Samsung Foundry at the same node.
- The complete external-customer list for Samsung Foundry's SF2 design starts.

---

**Disclaimer**: This post is research commentary, not investment advice. Customer-mix descriptions are based on publicly disclosed customer references, earnings-call commentary, and supply-chain trade-press reporting; specific wafer-volume allocations are not publicly disclosed. Samsung Foundry's customer list shifts continuously. Tickers cited are illustrative for the framework, not recommendations. Do your own due diligence and consult licensed advisors before any investment decision.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
