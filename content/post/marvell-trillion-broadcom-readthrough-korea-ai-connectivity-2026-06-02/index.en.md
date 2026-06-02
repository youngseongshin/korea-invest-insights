---
title: "Marvell's Trillion-Dollar Story and the Broadcom Read-Through: What Does It Mean for Korea?"
date: 2026-06-02T20:45:00+09:00
description: "Jensen Huang's Marvell call-out is not about Marvell replacing NVIDIA GPUs. It is a signal that custom XPU, AI networking, optical interconnect, FC-BGA, high-speed PCB and silicon capacitors are becoming the next AI infrastructure bottlenecks. This note previews Broadcom's Q2 call and maps the read-through to Samsung Electro-Mechanics, Korea Circuit and Isu Petasys."
categories: ["Market-Outlook"]
tags:
  - "Marvell"
  - "MRVL"
  - "Broadcom"
  - "AVGO"
  - "NVLink Fusion"
  - "custom XPU"
  - "AI networking"
  - "FC-BGA"
  - "high-speed PCB"
  - "Samsung Electro-Mechanics"
  - "Korea Circuit"
  - "Isu Petasys"
  - "AI infrastructure"
slug: marvell-trillion-broadcom-readthrough-korea-ai-connectivity-2026-06-02
valley_cashtags:
  - Marvell
  - Broadcom
  - 삼성전기
  - 코리아써키트
  - 이수페타시스
  - 삼성전자
  - SK하이닉스
  - 한미반도체
draft: false
---

> Context
> This is a follow-up to [the pre-earnings Marvell/Broadcom Korea bottleneck note](/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/), [Marvell Q1 FY2027 and Korean semiconductors](/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/), and the [AI infrastructure multiple map](/post/ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31/). Related hubs: [AI PCB and Substrate Hub](/page/korea-ai-pcb-substrate-hub/), [Korea Semiconductor Value Chain Hub](/page/korea-semiconductor-equipment-ip-hub/), and [AI HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/).

## TL;DR

Jensen Huang calling Marvell a potential next "trillion-dollar company" does **not** mean Marvell replaces NVIDIA GPUs. The better interpretation is that **custom XPUs, AI networking and optical interconnects have become important enough to be pulled into the NVIDIA AI factory architecture**.

For Broadcom, this is a **70/100 positive read-through**. It is positive because Broadcom's AI business sits exactly in custom XPU, Ethernet switching, optics, SerDes, CPO and 3.5D packaging. It is not 100/100 because Marvell is the cleaner NVIDIA NVLink Fusion partner, while Broadcom is more tied to hyperscaler custom silicon and open Ethernet / UALink-style ecosystems.

For Korea, the first-order read-through is not HBM alone. The direct language is **FC-BGA, AI network PCB, silicon capacitors, high-speed substrates and power integrity**.

| Priority | Korean exposure | Why it matters | Stance |
|---:|---|---|---|
| 1 | Samsung Electro-Mechanics | FC-BGA + MLCC + silicon capacitor bundle | Cleanest structural proxy, but price discipline matters |
| 2 | Korea Circuit | Broadcom AI data-center ASIC FC-BGA qualification option | Higher beta, needs public customer / production proof |
| 3 | Isu Petasys | AI Ethernet / switch / networking PCB beta | Thematic beta, needs backlog and ASP proof |
| 4 | Samsung Electronics / SK Hynix | HBM / eSSD second-order beneficiaries | Core AI memory exposure, but not the first-order event |
| 5 | Hanmi Semiconductor | Advanced-packaging equipment derivative | Needs actual orders and customer diversification |

One-line conclusion:

> Marvell's trillion story and Broadcom's earnings checklist point to the same place: after GPU/HBM, the next AI infrastructure bottleneck is **connectivity, substrate and power integrity**. In Korea, Samsung Electro-Mechanics is the cleanest structural proxy; Korea Circuit and Isu Petasys are higher-beta translations.

---

## 1. What Happened

[Fact] Reuters reported on June 2, 2026 that Jensen Huang joined Marvell CEO Matt Murphy on stage during Computex week in Taipei and called Marvell the next "trillion-dollar company." Marvell shares rose more than 24% in U.S. premarket trading. Reuters also noted that Marvell's market cap was still below $192bn and that NVIDIA had earlier invested $2bn in Marvell. ([Reuters via Investing.com][1])

[Fact] Marvell and NVIDIA announced an NVLink Fusion partnership on March 31, 2026. Marvell will provide custom XPUs and NVLink Fusion-compatible scale-up networking, while NVIDIA will provide Vera CPU, ConnectX NICs, BlueField DPUs, NVLink interconnect, Spectrum-X switches and rack-scale AI compute. ([Marvell 8-K / EX-99.1][2])

[Fact] NVIDIA describes NVLink Fusion as a rack-scale AI infrastructure platform that enables hyperscalers and custom ASIC designers to integrate custom CPUs and XPUs with NVLink scale-up interconnect and OCP MGX rack-scale architecture. The modular portfolio includes NVIDIA GPUs, Vera CPUs, NVLink networking, CPO switches, ConnectX SuperNICs, BlueField DPUs and Mission Control software. ([NVIDIA][3])

So the point is not simply "Marvell is good." The larger point is:

> NVIDIA is not leaving custom silicon outside the AI factory. It is trying to absorb it into its rack-scale architecture.

---

## 2. What Marvell's Trillion Story Really Means

Marvell's message is straightforward: **AI scaling depends on connectivity**. Its Computex 2026 keynote was titled "The Future of AI Scaling Depends on Connectivity." The company argued that AI infrastructure is expanding beyond a single rack and even beyond a single data center, making data movement across accelerators, servers, racks, campuses and geographically distributed data centers a key bottleneck. ([Marvell][4])

Investment translation:

| Shift | Meaning | Investment read |
|---|---|---|
| GPU-only to heterogeneous compute | GPUs, custom XPUs, CPUs and DPUs coexist in the rack | Not NVIDIA versus ASIC, but ASICs entering NVIDIA fabric |
| Compute bottleneck to connectivity bottleneck | Connections between chips and racks matter more | Ethernet, NVLink, optics, SerDes and switch ASICs re-rate |
| Board-level to package-level bottleneck | Power, signal integrity and packaging drive performance | FC-BGA, high-speed PCB, Si-Cap and MLCC demand expands |

[Fact] Marvell reported FY2027 Q1 revenue of $2.418bn, up 28% year over year, and guided FY2027 Q2 revenue to a $2.7bn midpoint. Data-center revenue was $1.833bn, or 76% of total revenue. ([Marvell Q1 FY2027][5])

[Inference] Marvell is being re-rated not because of a few cents of EPS, but because it has unusually pure exposure to the AI data-center connectivity bottleneck. That still does not mean it replaces GPUs. It means custom XPUs and networking have become core pieces of the AI factory system.

---

## 3. Why the Broadcom Read-Through Is Positive, but Not Perfect

Broadcom is not the direct protagonist of the Marvell event. But the read-through is strong because Broadcom's AI franchise sits on the same layers:

1. custom AI accelerator / XPU
2. AI networking
3. Ethernet switch
4. optical DSP / CPO
5. SerDes / retimer / PCIe Gen6
6. 3.5D packaging

[Fact] Broadcom reported FY2026 Q1 revenue of $19.311bn, up 29% year over year. Q1 AI revenue was $8.4bn, up 106% year over year, and the company guided Q2 AI semiconductor revenue to $10.7bn. Q2 total revenue guidance was $22.0bn, with adjusted EBITDA margin guidance of about 68%. ([Broadcom Q1 FY2026][6])

The simple math:

```text
Broadcom Q2 AI semiconductor QoQ growth
= 10.7 / 8.4 - 1
= +27.4%

Q2 AI semiconductor share of total revenue guide
= 10.7 / 22.0
= 48.6%

Q1 AI revenue share of total revenue
= 8.4 / 19.311
= 43.5%
```

[Fact] Broadcom's Q2 FY2026 earnings call is scheduled for June 3, 2026 at 5:00 p.m. ET, or June 4, 2026 at 6:00 a.m. KST. This note is therefore a **pre-call checklist**, not a post-earnings verdict. ([Broadcom Q2 Event][7])

### What to Listen For

| Checkpoint | Strong signal | Korea read-through |
|---|---|---|
| Q2 AI semiconductor | Above $10.7bn | Confirms custom XPU / AI ASIC demand |
| Q3 AI guide | QoQ growth | Supports 2H26 substrate / package demand |
| AI networking | Ethernet switch, optics, SerDes strength | Isu Petasys, Korea Circuit, Samsung Electro-Mechanics |
| Tomahawk 6 / CPO | Production volume, lead-time or supply constraint | High-speed PCB, FC-BGA, optical ecosystem |
| EBITDA margin | Holds near 68% | Custom silicon is not low-margin outsourcing |

[Fact] At OFC 2026, Broadcom showcased a gigawatt-scale AI cluster portfolio including 3.5D XPU, 102.4T Ethernet switch with CPO, 400G/lane optical DSP, 200G/lane Ethernet retimers/AEC and PCIe Gen6 switches/retimers. ([Broadcom OFC][8])

[Fact] Broadcom announced that its Tomahawk 6 family switch series is shipping in production volume, and that it enables 128K-XPU networks using only two switch tiers. ([Broadcom Tomahawk 6][9])

The nuance:

> The Marvell call-out is category-positive for Broadcom, but not company-specific proof. Marvell is the cleaner NVIDIA NVLink Fusion partner; Broadcom must prove the same connectivity thesis through its own AI revenue, networking and margin numbers.

---

## 4. The Common Message: After GPU/HBM Comes Connectivity

Separate Marvell and Broadcom, and you see competition. Put them together, and you see the bottleneck migration.

| AI infrastructure layer | Old market focus | New bottleneck emphasized here |
|---|---|---|
| Compute | NVIDIA GPU | GPU + custom XPU hybrid architecture |
| Memory | HBM | HBM + eSSD + memory attach + KV/cache hierarchy |
| Interconnect | NVLink / Ethernet | Scale-up, scale-out and scale-across connectivity |
| Package | CoWoS / HBM stack | 2.5D/3.5D, FC-BGA, high-layer substrates |
| Board | Server PCB | AI networking board, low-loss materials, high-speed MLB |
| Power integrity | Rack power | Package-level Si-Cap, MLCC and PDN components |

[Inference] Reading this only as "HBM demand is stronger" misses half the point. HBM is still core. But Marvell and Broadcom are pointing to the components that move data, stabilize power and package chips together.

---

## 5. Korea Priority #1: Samsung Electro-Mechanics

Samsung Electro-Mechanics is the cleanest Korean large-cap translation of this read-through.

1. **FC-BGA:** custom XPUs, switch ASICs, server CPUs and network chips require large, high-layer, high-reliability package substrates.
2. **MLCC / silicon capacitor:** higher AI package power density makes die-near power-integrity components more important.
3. **Customer qualification:** package-internal components carry stronger certification barriers than consumer components.

[Fact] Samsung Electro-Mechanics reported Q1 2026 revenue of KRW 3.2091tn and operating profit of KRW 280.6bn. Component Solution revenue was KRW 1.4085tn, up 16% YoY. Package Solution revenue was KRW 725.0bn, up 45% YoY. The company cited MLCCs for AI servers / ADAS and FCBGAs for AI accelerators / server CPUs as growth drivers. ([Samsung Electro-Mechanics Q1][10])

[Fact] Samsung Electro-Mechanics signed a silicon capacitor supply contract worth about KRW 1.5tn with a global large-scale company. The contract runs from January 1, 2027 to December 31, 2028. The company says silicon capacitors are installed inside high-performance packages such as AI-server GPUs and HBM to improve power-supply stability. ([Samsung Electro-Mechanics Si-Cap][11])

So the company frame changes:

| Old classification | Better classification after this event |
|---|---|
| MLCC cyclical component maker | AI server / network power-integrity supplier |
| Package substrate vendor | FC-BGA platform for custom XPU / AI network ASIC |
| Smartphone component company | AI package-inside component supplier |

But this is not a "buy at any price" conclusion. Samsung Electro-Mechanics has already re-rated sharply. The evidence that matters now is Package Solution margin, AI substrate mix, Si-Cap yield, customer diversification and repeat contract visibility.

---

## 6. Higher-Beta Option: Korea Circuit

Korea Circuit has lower scale and lower certainty than Samsung Electro-Mechanics, but it may have higher beta to a Broadcom AI networking surprise.

[Inference] Based on user-provided SK Securities research, Korea Circuit has prior Broadcom communications FC-BGA supply experience, is reportedly undergoing AI data-center ASIC FC-BGA qualification in 1H26, may begin small supply in 2H26, and could see meaningful impact in 2027. P3 FC-BGA plant utilization is a key variable.

The boundary:

| Item | Current confidence |
|---|---|
| Broadcom-related communications FC-BGA experience | Research-based inference |
| AI data-center ASIC qualification | Not public official fact |
| 2H26 small supply | Speculative until confirmed |
| 2027 earnings impact | Needs evidence |

Therefore Korea Circuit is not a confirmed beneficiary. It is a **Broadcom AI DC FC-BGA option**. If Broadcom's call shows strong custom XPU and AI networking demand and Korea Circuit later confirms qualification, production or P3 utilization, the re-rating case strengthens.

---

## 7. AI Networking PCB Beta: Isu Petasys

Isu Petasys could react quickly because the event language is filled with AI Ethernet, switch ASIC, optical interconnect, 800G/1.6T and CPO/NPO.

But its investment logic is different from Samsung Electro-Mechanics:

| Item | Samsung Electro-Mechanics | Isu Petasys |
|---|---|---|
| Core exposure | FC-BGA + MLCC + Si-Cap | AI networking PCB / MLB |
| Confidence | Higher | Needs customer and mix proof |
| Stock character | Structural proxy + valuation discipline | Theme beta + earnings proof |
| Key metrics | Package revenue, OPM, Si-Cap | Backlog, high-layer MLB ASP, customer mix |

[Inference] Strong Broadcom commentary on Tomahawk 6, AI Ethernet switches and optical DSPs would be positive for high-speed networking PCB names. But "Broadcom is strong, so every PCB is strong" is too broad. Low-loss materials, layer count, yield, customer certification and ASP must show up.

---

## 8. Why HBM and Hanmi Are Second-Order Here

This event is not negative for HBM. If custom XPUs grow, HBM demand can diversify beyond NVIDIA GPUs into hyperscaler custom accelerators.

However, the first-order signal from Marvell/Broadcom is **connectivity**, not HBM.

| Layer | Directness to this event |
|---|---|
| custom XPU / AI networking | Very high |
| FC-BGA / high-speed substrate | High |
| Si-Cap / MLCC / power integrity | High |
| HBM / eSSD | Medium, second-order |
| TC bonder / advanced package equipment | Medium, order confirmation needed |

Hanmi Semiconductor is a valid derivative option, especially because its recent IR notice widened the TC-bonder TAM from HBM into 2.5D package, AI system semiconductors, OSAT and HBF. But equipment names need orders, customer names, delivery timing and margin proof. See the [Hanmi IR follow-up](/post/hanmi-semiconductor-ir-tc-bonder-tam-expansion-watchlist-2026-06-02/).

---

## 9. Post-Broadcom Scenarios

### Bull Case

Conditions:

1. Q2 AI semiconductor revenue at or above $10.7bn
2. Q3 guide shows QoQ growth
3. Strong AI networking, Tomahawk 6, optical DSP and CPO commentary
4. Better custom XPU customer or 2027 visibility
5. Adjusted EBITDA margin holds near 68%

Read:

- Samsung Electro-Mechanics is structurally reaffirmed
- Korea Circuit can be reframed as a Broadcom FC-BGA option
- Isu Petasys can react as AI networking PCB beta
- HBM and Hanmi follow as second-order extensions

### Base Case

Conditions:

1. Q2 AI semiconductor revenue near $10.7bn
2. Q3 grows but does not accelerate
3. Networking commentary positive but not supply-constrained
4. Margin stable

Read:

- Keep quality exposure centered on Samsung Electro-Mechanics
- Avoid chasing Korea Circuit / Isu Petasys without earnings proof
- Maintain the existing HBM large-cap thesis

### Bear Case

Conditions:

1. Q2 AI semiconductor below $10.7bn
2. Q3 guide slows
3. custom XPU customer ramp delays
4. AI mix hurts margin
5. Inventory or customer timing dominates the commentary

Read:

- High-beta Korean substrate names may correct first
- Samsung Electro-Mechanics remains the structural name, but valuation discipline becomes stricter
- Pause the Broadcom/Marvell read-through trade

---

## 10. Final View

Do not reduce this to "Marvell went up." Jensen Huang highlighted Marvell because custom XPU and connectivity are becoming core pieces inside the NVIDIA AI factory.

For Broadcom, this is positive but still needs proof. The June 3 U.S. post-market Q2 call has to confirm AI semiconductor revenue, Q3 growth, AI networking / optics / CPO and margin defense.

For Korea, the message is clearer:

> The first-order read-through is not just HBM. It is FC-BGA, high-speed PCB, silicon capacitors, MLCC and power integrity.

Practical priority:

| Stance | Korean exposure | Reason |
|---|---|---|
| Core watch | Samsung Electro-Mechanics | Cleanest AI package power-integrity proxy |
| High-beta watch | Korea Circuit | Broadcom AI DC FC-BGA option |
| Theme beta watch | Isu Petasys | AI networking PCB beta |
| Secondary | Samsung Electronics / SK Hynix | HBM/eSSD second-order exposure |
| Derivative | Hanmi Semiconductor | Advanced-packaging equipment orders still need proof |

One-line summary:

> Marvell's trillion story should be read in Korea not as "HBM goes higher" alone, but as "AI infrastructure's connectivity, substrate and power-integrity bottlenecks get more valuable."

---

## Evidence Classification

### [Fact]

- Reuters reported Jensen Huang's Marvell "trillion-dollar company" remark and Marvell's premarket surge. ([Reuters via Investing.com][1])
- Marvell and NVIDIA announced an NVLink Fusion partnership on March 31, 2026. ([Marvell 8-K / EX-99.1][2])
- NVIDIA describes NVLink Fusion as a rack-scale AI infrastructure platform for custom CPUs/XPUs and NVLink scale-up architecture. ([NVIDIA][3])
- Marvell FY2027 Q1 revenue was $2.418bn, data center was 76% of revenue, and Q2 revenue midpoint guidance was $2.7bn. ([Marvell Q1 FY2027][5])
- Broadcom FY2026 Q1 AI revenue was $8.4bn, Q2 AI semiconductor guidance was $10.7bn, Q2 total revenue guidance was $22.0bn, and adjusted EBITDA margin guidance was about 68%. ([Broadcom Q1 FY2026][6])
- Broadcom Q2 FY2026 call is scheduled for June 3, 2026 at 5:00 p.m. ET. ([Broadcom Q2 Event][7])
- Samsung Electro-Mechanics Q1 2026 Component Solution revenue was KRW 1.4085tn and Package Solution revenue was KRW 725.0bn. ([Samsung Electro-Mechanics Q1][10])
- Samsung Electro-Mechanics signed a KRW 1.5tn silicon capacitor supply contract for 2027-2028. ([Samsung Electro-Mechanics Si-Cap][11])

### [Inference]

- Jensen Huang's Marvell call-out signals NVIDIA is absorbing custom XPU into the NVLink Fusion ecosystem rather than treating it only as an external threat.
- The read-through for Broadcom is category-positive, but Marvell has the cleaner NVIDIA ecosystem angle.
- Korea's first-order read-through is FC-BGA, high-speed PCB, silicon capacitors, MLCC and power integrity.

### [Speculation]

- Korea Circuit's AI data-center ASIC FC-BGA qualification and 2H26 supply are research-based assumptions, not public official facts.
- Whether Broadcom's call immediately re-rates Korean substrate names depends on Q3 guide, customer ramp and AI networking commentary.
- Samsung Electro-Mechanics' Si-Cap and FC-BGA mix must still prove sustained margins and repeat orders.

### [Blocked]

- Broadcom Q2 FY2026 actual results had not been released as of this note's timestamp: June 2, 2026, 20:45 KST.
- Korea Circuit customer names, ASPs and AI DC FC-BGA revenue timing are not public.
- Isu Petasys' direct Broadcom / Marvell customer exposure and AI networking revenue mix are not public.
- Samsung Electro-Mechanics' Si-Cap customer name, product margin, yield and post-2028 repeat contract status remain undisclosed.

[1]: https://www.investing.com/news/stock-market-news/marvell-technology-surges-after-nvidias-huang-calls-it-next-trilliondollar-company-4721040 "Marvell Technology surges after Nvidia’s Huang calls it 'next trillion-dollar company' | Reuters via Investing.com"
[2]: https://investor.marvell.com/sec-filings/all-sec-filings/content/0001193125-26-134462/d113606dex991.htm "NVIDIA AI Ecosystem Expands as Marvell Joins Forces Through NVLink Fusion | Marvell 8-K EX-99.1"
[3]: https://www.nvidia.com/en-us/data-center/nvlink-fusion/ "Build Semi-Custom AI Infrastructure | NVIDIA NVLink Fusion"
[4]: https://www.marvell.com/company/newsroom/marvell-keynote-computex-2026-future-of-scaling-ai-depends-on-connectivity.html "Marvell Keynote at COMPUTEX 2026: The Future of AI Scaling Depends on Connectivity"
[5]: https://investor.marvell.com/news-events/press-releases/detail/1023/marvell-technology-inc-reports-first-quarter-of-fiscal-year-2027-financial-results "Marvell Technology, Inc. Reports First Quarter of Fiscal Year 2027 Financial Results"
[6]: https://www.broadcom.com/company/news/financial-releases/63976 "Broadcom Inc. Announces First Quarter Fiscal Year 2026 Financial Results"
[7]: https://www.prnewswire.com/news-releases/broadcom-inc-to-announce-second-quarter-fiscal-year-2026-financial-results-on-wednesday-june-3-2026-302761260.html "Broadcom Inc. to Announce Second Quarter Fiscal Year 2026 Financial Results"
[8]: https://www.broadcom.com/company/news/product-releases/64036 "Broadcom Showcases Industry-Leading Solutions for Scaling AI Infrastructure at OFC 2026"
[9]: https://www.broadcom.com/company/news/product-releases/64031 "Broadcom Now Shipping World's First 102.4 Tbps Switch in Production Volume"
[10]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Announces Q1 2026 Business Performance"
[11]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
