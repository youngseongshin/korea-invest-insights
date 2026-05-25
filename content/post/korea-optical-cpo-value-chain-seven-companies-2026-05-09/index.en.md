---
title: "Korea Optical & CPO Value Chain — Only OE Solutions (138080.KQ) Is Truly Close to CPO; Six of Seven Names Are Up +300–900% YTD With Earnings That Haven't Followed"
slug: korea-optical-cpo-value-chain-seven-companies-2026-05-09
date: 2026-05-09T20:00:00+09:00
description: "The next AI data-center bottleneck is moving down to optical interconnect. Tens of thousands of GPUs talking to each other require 800G and 1.6T optical modules, and Co-Packaged Optics (CPO) — placing the optical engine right next to the switch ASIC — is emerging as the architectural answer. Mapping the seven Korean listed names — OE Solutions, Optocore, Daehan Optical Communications, BWE, WooriRo, Lycom, Coset — only OE Solutions sits genuinely close to CPO via its ELSFP external laser source and in-house 100G EML laser chip. The other six are downstream beneficiaries or thematic plays. And six of seven are up +300% to +905% YTD with operating losses still in place. The price moved before the earnings did. The actionable read is: OE Solutions on the watchlist (with a wait for either pullback or 3Q ELSFP customer-sample confirmation), and the rest until overheating clears."
categories: ["Sector-Deep-Dive", "Korea Market", "Semiconductors"]
tags:
  - "optical interconnect"
  - "CPO"
  - "co-packaged optics"
  - "OE Solutions"
  - "138080"
  - "Optocore"
  - "Daehan Optical"
  - "BWE"
  - "WooriRo"
  - "Lycom"
  - "Coset"
  - "AI data center"
  - "ELSFP"
  - "external laser source"
  - "EML"
  - "Korean small-caps"
  - "optical transceiver"
  - "800G"
  - "1.6T"
---

> 🔗 <strong>Related</strong>: [AI PCB & Substrate Hub](/page/korea-ai-pcb-substrate-hub/) · [Korea AI PCB Ecosystem — 10 Companies](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) · [AI PCB & Substrate Thesis — System BOM as the Common Bottleneck](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) · [Haesung DS — Lead Frame to AI Heat-Spreader Second-Source](/post/haesung-ds-leadframe-ai-heat-spreader-second-source-2026-05-07/)

*The [substrate-thesis post](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) made a system-BOM argument: AI demand isn't bought one chip at a time, it's bought one rack at a time, and substrate demand sits across the entire BOM. The same logic now extends down to optical interconnect — and the Korean listed exposures are far less mature. Seven names sit on the optical / CPO axis. Only one (OE Solutions, 138080.KQ) is genuinely close to the new CPO architecture via its <strong>ELSFP external laser source</strong>. The other six are downstream beneficiaries or themes. And six of seven are up +300% to +905% YTD against operating losses or unverified customer wins. This is a "valid technical thesis at the wrong price" market — exactly the kind of setup where mapping the value chain by <strong>distance to the actual bottleneck</strong> is more useful than buying the most-up names.*

---

## TL;DR

* <strong>Among Korean listed names, only OE Solutions (138080.KQ) is truly close to CPO.</strong> It has disclosed an <strong>ELSFP external laser source</strong> product (CPO-compatible, OIF-standard 8-channel, 23dBm/200mW per channel, TEC-cooled, customer samples planned for 3Q26) and developed a domestic-first <strong>100G EML laser chip</strong>. The other six are not on the CPO core path. OE Solutions is also not yet named on Nvidia's or Broadcom's public CPO partner list.
* <strong>Optocore has actual AI data-center optical transceiver contracts</strong> totalling \~₩16.7bn — but the customer is undisclosed and trading is suspended on a 1Q26 going-concern audit. <strong>Not investable.</strong>
* <strong>Daehan Optical Communications is +905% YTD on a "more optical fiber for AI" narrative — not a CPO play at all.</strong> It's a vertically integrated preform-to-fiber company, not an optical engine or laser supplier. The Korea Exchange has flagged it for investment-warning escalation.
* <strong>Six of seven names are up +300%+ YTD against still-loss-making P&Ls.</strong> Daehan +905%, BWE +778%, WooriRo +616%, OE Solutions +307%. The price moved long before the earnings followed. Buying here is a bet on <strong>price catching up to its own forward expectations</strong>, not on the technology being right.
* <strong>The clean allocator read is OE Solutions watchlist with a wait, the other six on hold.</strong> OE Solutions trades at >100× 2026E OP at the current price — the entry is at the <strong>47,000–50,000 won pullback</strong> or after <strong>3Q ELSFP customer-sample confirmation</strong>, not on chase.

---

## 1. Why optical is the next AI data-center bottleneck

### 1.1 Same logic as substrate — at the network layer

The substrate thesis was a "common-denominator" argument: every additional chip in an AI rack — GPU, CPU, DPU, NIC, switch ASIC, memory module — adds substrate demand. Optical interconnect is the same logic at the network layer. Tens of thousands of GPUs in a single training cluster require network bandwidth that electrical signaling cannot deliver at acceptable power. So the link goes optical.

```
AI data-center optical demand path:

Tens-of-thousands GPU cluster
   ↓
Switch ASICs (network connectivity)
   ↓
800G → 1.6T optical transceivers (electrical → optical → electrical)
   ↓
Optical fiber and cable plant (the path the light travels)
   ↓
Components: lasers, photodetectors, optical amplifiers, low-loss fiber
```

Broadcom has indicated that lead times on optical-transceiver PCBs have stretched from 6 weeks to 6 months — an early signal that optical components are becoming the constrained layer.

### 1.2 What CPO actually is

The legacy architecture used <strong>pluggable optical modules</strong> plugged into the front of the switch chassis. Easy to swap, but power-hungry, and the electrical signal travels a long path from the switch ASIC out to the front panel.

<strong>Co-Packaged Optics (CPO)</strong> is a different architecture: the optical engine sits <strong>right next to the switch ASIC on the same package substrate</strong>. Electrical-signal travel distance collapses. Power per bit drops sharply.

* Nvidia has stated its CPO-based switch is <strong>5× more power-efficient</strong> and offers <strong>10× better network reliability</strong> than pluggable equivalents.
* Broadcom has shown a 51.2 Tbps CPO Ethernet switch claiming <strong>>70% reduction in optical-link power consumption</strong>.

### 1.3 Why "external laser source" matters inside CPO

The hard problem inside CPO: <strong>lasers are temperature-sensitive, switch ASICs are hot.</strong> Putting the laser inside the package, next to a hot ASIC, shortens laser life and degrades performance.

Solution: <strong>separate the laser from the package.</strong> Pull the laser out to the front panel, send only the light into the package via fiber, and keep the laser body thermally isolated.

The standard form factor for that external laser is <strong>ELSFP — External Laser Small Form-factor Pluggable</strong>, defined by OIF (Optical Internetworking Forum). Once CPO scales, ELSFP becomes a core component category.

```
Where ELSFP sits inside CPO:

Switch ASIC (hot)
   ↓ (light in)
Optical engine (next to ASIC, light ↔ electrical)
   ↑ (light out)
ELSFP external laser source (front panel, thermally isolated)
   ↑
Laser (high-power, stable)
```

<strong>OE Solutions's ELSFP is exactly this part.</strong> It's the only Korean listed company with this specific product disclosed.

---

## 2. The seven Korean names — separating "true CPO exposure" from "AI optical thematic"

| # | Company (ticker) | Value-chain position | AI optical relevance | YTD price | Read |
|---:|---|---|---|---:|---|
| 1 | <strong>OE Solutions (138080.KQ)</strong> | CPO ELSFP / optical transceiver / laser chip | <strong>Most direct</strong> | +307% | Core watchlist |
| 2 | Optocore | AI data-center transceivers | Contract evidence; suspended | +106% | Not investable |
| 3 | Daehan Optical Communications | Fiber and cable (upstream materials) | Downstream beneficiary, not CPO | <strong>+905%</strong> | Overheated; KRX warning escalation |
| 4 | BWE | 800G / 1.6T transceiver line-up | Product disclosed; customer unconfirmed | <strong>+778%</strong> | High-vol thematic |
| 5 | WooriRo | Photodetectors (transceiver core component) | Tech-development stage | <strong>+616%</strong> | Component option |
| 6 | Lycom | Optical amplifiers / DC connectivity | Downstream beneficiary | +98% | Event-pending |
| 7 | Coset | Optical components (TOSA/ROSA) | Small-cap option | -5% | Liquidity-inadequate |

### 2.1 What this table shows

<strong>First, true CPO exposure vs. AI optical thematic are different objects.</strong> Only OE Solutions has the ELSFP external-laser product. The rest are transceivers (Optocore, BWE), fiber (Daehan Optical), photodetectors (WooriRo), amplifiers (Lycom), or generic components (Coset). All sit somewhere in the broader AI optical value chain, but "core CPO supplier" and "thematic optical name" do not deserve the same multiple.

<strong>Second, six of seven are up several hundred percent YTD against operating losses or unverified customer wins.</strong> Daehan +905%, BWE +778%, WooriRo +616%, OE Solutions +307%. Price moved before earnings. Buying here is not "is the technology right?" — it's "did price already overshoot what the earnings can deliver?"

---

## 3. OE Solutions — the only name truly close to CPO

### 3.1 Business structure

OE Solutions makes optical transceivers and laser chips. Founded in 2003 by Bell Labs and Samsung Electronics alumni with optical-volume-manufacturing backgrounds. International footprint: New Jersey and California (US), the Netherlands, Japan.

Core capability: <strong>vertical integration from laser chip → optical sub-assembly → finished transceiver.</strong> In an optical transceiver, the laser is the "engine" — light-output stability, thermal management, and lifetime drive the product. OE Solutions develops the laser chip in-house.

### 3.2 Why ELSFP is the key product

Disclosed at OFC 2026 (March):

```
OE Solutions's CPO-compatible ELSFP:

- 23 dBm / 200 mW optical output per channel
- TEC (thermo-electric cooler) integrated → wavelength stability + laser lifetime
- 8-channel configuration
- Customer samples planned from 3Q26
```

This product directly addresses the CPO thermal isolation problem — pulling the laser away from a hot switch ASIC and locating it on the front panel. OIF defines the standard, and OE Solutions is the only Korean listed name with the disclosed product.

OE Solutions also disclosed at AI EXPO 2026 a domestic-first <strong>100G-class EML laser chip</strong>, the foundational light source for 800G/1.6T transceivers.

### 3.3 The earnings haven't caught the technology

This is the gap that defines the trade.

| Metric | 2024 | 2025 | 2026E |
|---|---:|---:|---:|
| Revenue (KRW bn) | 32.0 | 57.4 | 81.6–83.5 |
| Operating profit (KRW bn) | -30.4 | -16.0 | 6.1–6.5 |
| Operating margin | -95% | -28% | 7–8% |
| Datacom revenue mix | — | <strong>2%</strong> | still low |

2025 revenue recovered +79% YoY but stayed loss-making. 2026E flips to profit (₩6.1–6.5bn OP), but the market cap is \~₩660bn. Quick check:

* Enterprise value ≈ market cap + net debt = 660 + 20 = \~₩680bn
* On 2026E OP of ₩6.5bn → <strong>EV/EBIT ≈ 105×</strong>

<strong>At the current price you're paying \~105× 2026E OP.</strong> That is not a "2026 turn-to-profit" valuation. That is an "AI optical revenue inflection in 2027–2028" valuation.

### 3.4 Revenue mix is not yet AI-centric

2025 revenue mix (sell-side estimates):

| Segment | Share | Read |
|---|---:|---|
| Wireless | 48% | Legacy core; recovering after the post-5G slowdown |
| FTTH / MSO (wired access) | 23% | Tied to Japanese / US wired-access spend |
| Long-haul (Telecom) | 21% | 100G/400G long-haul transceivers |
| <strong>Datacom</strong> | <strong>2%</strong> | <strong>The AI story is not yet in revenue</strong> |
| Laser chips | 6% | Tech option, scale still constrained |

Calling this an "AI data-center CPO company" overshoots the current P&L. The accurate framing is <strong>"telecom-equipment recovery turnaround with a CPO call option attached."</strong>

### 3.5 So why is it #1?

```
What only OE Solutions has, vs. the other six:

1. Disclosed CPO ELSFP product — only one
2. In-house 100G EML laser chip — only one
3. Vertical integration: laser chip → sub-assembly → module — deepest in cohort
4. Track record with global telecom-equipment customers (Cisco, Nokia, Ciena, etc.)
5. International operations footprint (US / NL / JP)
```

The cautionary note: Nvidia's disclosed CPO partner list (TSMC, Coherent, Corning, Foxconn, Lumentum, Senko, Sumitomo, etc.) <strong>does not include OE Solutions</strong>. The accurate state is "tech is there, ecosystem inclusion not yet confirmed."

### 3.6 Track these variables

* <strong>3Q26</strong>: Did ELSFP customer samples ship on schedule?
* <strong>4Q26 → 2027</strong>: Is qualification progressing? Are customer names being mentioned?
* <strong>Datacom mix</strong>: Does it move materially above 2%?
* <strong>Gross margin</strong>: Recovery from 2025's 10.5% toward 20%+?
* <strong>Operating profit</strong>: Did the FY26 turn-to-profit actually print?

---

## 4. The other six names

### 4.1 Daehan Optical Communications — +905% YTD, KRX investment-warning escalation

Daehan is <strong>not a CPO company.</strong> It's a vertically integrated preform → fiber → cable manufacturer — upstream materials, not optical engines. AI data centers do consume more high-density fiber, but that's a downstream beneficiary thesis, not CPO core.

The price action is the issue:

```
Daehan Optical Communications:
YTD: +905%
3-month: +610%
1-week: +47%
KRX: 2026-05-08 designated as investment-caution stock; warning escalation pending
```

Foreign flow has been strong, but the regulatory layer is already flagging the move. <strong>A 10×-YTD stock buy here is not a fiber-demand bet — it's a "can the price extend further from a 10× base" bet.</strong>

### 4.2 BWE — +778%, -36% from peak

BWE disclosed an 800G / 1.6T transceiver lineup at AI EXPO. <strong>Disclosed product ≠ qualified customer.</strong> No core customer name confirmed. Up +778% YTD, down -36% from the peak (8,100 → 5,200 won). Currently in a digestion zone.

### 4.3 WooriRo — +616%, retail-led spike

Disclosed 200 Gbps photodetector technology — a potential core component for 800G / 1.6T transceivers. Still development-stage; global customer qualification unverified. Cumulative net buying skews retail. This is a thematic-momentum trade, not institutional accumulation.

### 4.4 Lycom — +98%, dead volume

Optical amplifiers for intra- and inter-data-center connectivity. Reports of overseas order growth. Closer to AI optical periphery than CPO core. Up +98% YTD (least overheated of the seven), but volume sits at 34% of the 3-month average — without a new catalyst, it sideways.

### 4.5 Optocore — trading suspended, not investable

AI data-center transceiver contracts of \~₩16.7bn aggregate are real. But trading was suspended in March 2026 on a going-concern audit qualification, with possible delisting. <strong>No action possible as a public-equity name today.</strong>

### 4.6 Coset — KONEX-listed, liquidity-inadequate

Maker of 400G+ TOSA/ROSA optical components. KONEX-listed (Korea's smaller equity board); turnover is too thin for normal allocation. Watchlist only.

---

## 5. The overheating, in numbers

### 5.1 YTD performance

| Stock | YTD | 3-month | 1-week | Status |
|---|---:|---:|---:|---|
| Daehan Optical | <strong>+905%</strong> | +610% | +47% | KRX warning pending |
| BWE | <strong>+778%</strong> | +321% | +2% | -36% off peak, decelerating |
| WooriRo | <strong>+616%</strong> | +513% | +7% | Retail-led spike |
| OE Solutions | <strong>+307%</strong> | +232% | +38% | Institutional re-entry; still expensive |
| Optocore | +106% | +14% | — | Suspended |
| Lycom | +98% | +114% | +2% | No volume |
| Coset | -5% | +11% | -13% | Liquidity-inadequate |

### 5.2 The single-line read

<strong>Four of seven are up >300% YTD with effectively no earnings support.</strong> OE Solutions still posted a ₩16bn 2025 operating loss. Daehan is profitable but not profitable enough to justify a 10× YTD move. The price has moved well ahead of the fundamentals.

In this regime, the deciding question is not "is the technology right?" — it's <strong>"did the price already pull forward more than the earnings can ever deliver?"</strong>

---

## 6. OE Solutions valuation — what you're actually buying at the current price

### 6.1 What the current price requires

Assume market cap \~₩660bn, net debt \~₩20bn, EV \~₩680bn.

At an EV/EBIT exit multiple of 30×, the OP required to justify each price level:

| Price | Required OP (at 30× EV/EBIT) | Vs. 2026E OP |
|---:|---:|---|
| 53,300 (current) | <strong>\~₩22.7bn</strong> | 3.5× consensus |
| 60,000 (street TP) | \~₩25.4bn | 3.9× consensus |
| 70,000 | \~₩29.5bn | 4.5× consensus |
| 100,000 | \~₩41.9bn | 6.4× consensus |

<strong>Even the current price requires OP \~3.5× the 2026E consensus</strong> to reconcile to a 30× multiple. That isn't a 2026 number. That's a 2027–2028 AI-optical-revenue inflection.

### 6.2 Scenario fair-value bands

| Scenario | Key assumption | Operating profit | Fair-value band (KRW) |
|---|---|---:|---:|
| Bear | Telecom recovery delayed, ELSFP samples slip | ₩0–5bn | 25,000–35,000 |
| Base | FY26 turn-to-profit, ELSFP at sample stage only | ₩6.1–6.5bn | 30,000–45,000 |
| Bull 1 | 2027–2028 datacom revenue ramp | ₩20–25bn | 47,000–59,000 |
| Bull 2 | ELSFP customer adoption, GM 15%+ | ₩30–40bn | 71,000–111,000 |
| Hyper-bull | Direct inclusion in global AI CPO supply chain | ₩40bn+ | 110,000+ |

The <strong>53,300 close sits between Bull 1 and Bull 2</strong> — already pricing in meaningful CPO option value on top of the telecom-recovery base. If 3Q ELSFP customer engagement materializes, the price extends. If not, the level is exposed.

---

## 7. Position framework — how to handle the seven

| # | Name | Read | Rationale |
|---:|---|---|---|
| 1 | <strong>OE Solutions</strong> | <strong>Core watchlist, wait</strong> | Highest CPO purity; price already rich. Wait for 47,000–50,000 pullback or 3Q ELSFP confirmation |
| 2 | Lycom | Event-pending | Less overheated, but no volume — needs an order or customer-disclosure catalyst |
| 3 | Daehan Optical | <strong>No chase</strong> | +905% with KRX warning pending. Holders trim; new entries inappropriate |
| 4 | BWE | Wait for re-break | -36% off peak; pause until customer confirmation |
| 5 | WooriRo | No new entry | Retail-led; technology unverified |
| 6 | Optocore | <strong>Not investable</strong> | Trading suspended, delisting risk |
| 7 | Coset | Watch only | KONEX, liquidity-inadequate |

### 7.1 OE Solutions entry conditions

<strong>Price</strong>: First interest at 47,000–50,000 zone. Second interest at 43,000–45,000 (deeper retest).

<strong>Earnings confirmation</strong>:

* 2Q or 3Q operating-profit print (turn-to-profit confirmation)
* 3Q ELSFP customer-sample shipment disclosure
* Datacom revenue mix moving up

<strong>Flow confirmation</strong>:

* Foreign + institutional concurrent net buying ≥ 3 sessions
* Stable settlement above the 52-week high (57,900)

### 7.2 Invalidation conditions

* FY26 fails to turn to profit
* 3Q ELSFP sample timeline slips
* No customer-qualification mention through 4Q
* Datacom mix stays below 10%
* Gross margin fails to recover above 20%

---

## 8. Three things that need to be said directly

### 8.1 Most of the seven are thematic stocks

Honestly: among the seven, almost none have earnings-validated cases. OE Solutions was operating-loss in 2025, and the rest are weaker. <strong>Stocks up several hundred percent without operating profit are priced on expectation, not delivery.</strong> When expectation is not converted into earnings, the price gives back.

### 8.2 No Korean small-cap is on Nvidia's CPO partner list

Nvidia's named CPO partners: TSMC, Coherent, Corning, Foxconn, Lumentum, Senko, Sumitomo. No Korean small-caps. Asserting "Korean companies are inside the CPO supply chain" is overreach. OE Solutions is the closest but is still a <strong>candidate</strong>, not a confirmed inclusion.

### 8.3 Optical investing has long lead times

Optical-transceiver qualification cycles run like semiconductors: sample → qualification → design adoption → volume order → revenue recognition can take 1–2 years. Even if 3Q26 samples ship on time, volume revenue may be 2027–2028. Whether the share price waits patiently through that window is not knowable in advance.

---

## 9. Connecting back to the substrate series

This piece sits in the same frame as the [substrate series](/page/korea-ai-pcb-substrate-hub/). The [system-BOM thesis](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) made the structural argument that <strong>AI demand is bought as systems, not chips.</strong> That system contains substrate, optical, thermal, and power layers — all of them stretched.

```
AI system common bottlenecks:

Substrate (FC-BGA, MLB, CCL) — covered in the 5-name and 10-name pieces
Optical (800G/1.6T modules, CPO ELSFP, fiber) — this piece
Thermal (heat spreader, heat slug) — covered in the Haesung DS piece
Power (transformers, power semis) — future post candidate
Cooling (immersion, heat sinks) — future post candidate
```

The [10-companies framework](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) argued that the substrate-shortage thesis funnels back into upstream materials. The same distinction applies here — fiber and cable (Daehan Optical) is a downstream beneficiary, while laser / external-laser-source (OE Solutions) sits closer to the actual CPO bottleneck.

The crucial difference: <strong>the substrate cluster has earnings catching up with the price. The optical cluster does not.</strong> Substrate is "pick the validated names trading at acceptable prices." Optical is <strong>"separate signal from noise inside an overheated, pre-earnings rally."</strong>

[Haesung DS](/post/haesung-ds-leadframe-ai-heat-spreader-second-source-2026-05-07/) provides the same contrast on the thermal axis: there, the AI heat-spreader optionality sits on top of a real automotive-LF and DDR-substrate base. Here, five of seven optical names lack a comparable base — the optionality is essentially the entire thesis.

---

## 10. The bottom line

Optical interconnect being the next AI data-center bottleneck is structurally correct. Tens of thousands of GPUs need 800G / 1.6T optics, and CPO is the credible architectural answer. Korea has seven listed exposures.

But only <strong>one</strong> of the seven is genuinely close to CPO core. OE Solutions has the ELSFP external-laser source and the in-house 100G EML chip. The other six are downstream beneficiaries or themes. And six of seven are up +300% to +905% YTD — Daehan Optical with a KRX investment-warning escalation pending on top.

OE Solutions itself trades at \~105× 2026E OP. Datacom mix is 2%. 2025 was a loss. <strong>At the current price you are betting on 2027–2028 CPO customer adoption, not 2026 earnings.</strong> The clean entry sits behind 3Q26 ELSFP customer-sample confirmation or a 47,000–50,000 pullback — observation rather than chase.

"The technology is right" and "the price is right today" are different questions. Optical will likely prove to be a real AI-system bottleneck. But if price has already pulled forward several hundred percent, allocator return is determined by where you bought, not by whether the technology was correct.

---

## FAQ

<strong>Q: What is CPO in one sentence?</strong>
A: A new packaging architecture that places the optical engine <strong>directly next to the switch ASIC</strong> on the same package, dramatically shortening the electrical-signal path and cutting power per bit. Replaces front-panel pluggable optics in high-end AI data-center switches.

<strong>Q: Which Korean listed name is genuinely a CPO company?</strong>
A: <strong>OE Solutions (138080.KQ)</strong> is the only one with a disclosed CPO-relevant product — its ELSFP external laser source — plus an in-house 100G EML laser chip. It is <strong>not yet</strong> on Nvidia's or Broadcom's public CPO partner list, so the accurate state is "closest candidate," not "confirmed inclusion."

<strong>Q: Isn't Daehan Optical Communications a CPO play?</strong>
A: No. Daehan is a vertically integrated optical-fiber and cable manufacturer (preform → fiber → cable). AI data centers do consume more high-density fiber — that is a downstream beneficiary thesis — but Daehan does not produce CPO core components (optical engines, lasers, photonic ICs).

<strong>Q: Should I chase OE Solutions at 53,300?</strong>
A: Not for a full position. The current price is \~105× 2026E OP. The asymmetric entries are: (a) a pullback into the 47,000–50,000 zone, or (b) confirmation of 3Q26 ELSFP customer samples shipping on schedule. Chasing here is a 30–50bp pilot at most.

<strong>Q: Which name is the highest-risk in the cohort?</strong>
A: Optocore is <strong>not investable</strong> today (trading suspended on going-concern audit). Daehan Optical is +905% YTD with KRX warning escalation pending. BWE and WooriRo are up several hundred percent on unverified customer bases. None of these are appropriate new entries.

<strong>Q: How does this compare to the Korean AI substrate names?</strong>
A: The substrate cluster has <strong>earnings catching up to price</strong>, so the actionable trade is selecting validated names at acceptable multiples. The optical cluster has <strong>price ahead of earnings</strong>, so the actionable trade is filtering signal from thematic noise and waiting for verification points. Same system-BOM thesis, two different stages of the cycle.

<strong>Q: When does the case shift from "watchlist" to "core hold" for OE Solutions?</strong>
A: When <strong>two of three</strong> confirm: (1) FY26 actually turns to operating profit, (2) 3Q26 ELSFP samples ship plus a customer-qualification mention, (3) Datacom mix moves materially above 2%. Two out of three flips this from observation to position.

---

*This article is for research and informational purposes only and does not constitute investment advice. Price, flow, and earnings data for the seven names were checked against KRX, Hankyung, Alpha Square, and WiseReport. OE Solutions ELSFP and laser-chip details are sourced from official company disclosures (OFC 2026, AI EXPO 2026), the OIF standard documentation, and sell-side reports (iM Securities, Meritz, Hana). Nvidia and Broadcom CPO references are from each company's investor communications. Optocore is currently suspended on a going-concern audit and is not investable. Daehan Optical Communications is on KRX investment-caution status with warning escalation pending. Analysis can be wrong. Data cut: 2026-05-08–09 KST.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
