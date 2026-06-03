---
title: "Marvell Follow-Up: Why EML and CW-DFB Laser Sources Matter for AI Data Centers"
date: 2026-06-03T17:40:00+09:00
description: "A follow-up to the Marvell / Broadcom connectivity thesis: AI optical interconnect bottlenecks are moving deeper into EML and CW-DFB laser sources. Korea's most direct proxy is OE Solutions, but customer qualification and repeat orders matter more than product headlines."
categories: ["Market-Outlook", "Semiconductors", "Sector-Deep-Dive"]
tags:
  - "Marvell"
  - "Broadcom"
  - "AI optical interconnect"
  - "EML"
  - "CW-DFB"
  - "CPO"
  - "ELSFP"
  - "OE Solutions"
  - "Solid"
  - "RFHIC"
slug: marvell-follow-up-eml-cw-dfb-laser-source-korea-cpo-2026-06-03
valley_cashtags:
  - Marvell
  - Broadcom
  - OE Solutions
  - Optocore
  - Solid
  - RFHIC
  - Samji Electronics
  - KMW
draft: false
---

> Context
> This is a follow-up to [Marvell's trillion-dollar story and the Broadcom read-through](/post/marvell-trillion-broadcom-readthrough-korea-ai-connectivity-2026-06-02/). That note framed the bottleneck as custom AI silicon, AI networking, high-speed substrates and power integrity. This one moves one layer deeper: the laser light sources that make optical interconnect possible. Related pieces: [Marvell Q1 FY2027 and Korean semiconductors](/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/), [Korea Optical & CPO Value Chain](/post/korea-optical-cpo-value-chain-seven-companies-2026-05-09/), the [AI PCB / Substrate Hub](/page/korea-ai-pcb-substrate-hub/) and the [Korea Semiconductor Value Chain Hub](/page/korea-semiconductor-equipment-ip-hub/).

## TL;DR

- Reported TrendForce commentary points to combined 2026 monthly EML + CW-DFB laser-diode capacity of **50.7 million units**, or **608.4 million units annualized**. We treat this as a reported figure because the exact public English TrendForce table was not available for verification.
- The officially verifiable TrendForce direction is still clear: 800G+ optical transceiver shipments are expected to rise from 24 million units in 2025 to about 63 million units in 2026, while the AI optical transceiver market is expected to reach **US$26 billion** in 2026. Key bottlenecks include EML, CW-LD, optical alignment, power and thermals. ([TrendForce Dec 2025][1], [TrendForce Apr 2026][2])
- The core point is not "more optical modules." It is that the **laser light source** becomes a strategic bottleneck. Silicon photonics and CPO do not remove laser demand; they shift the bottleneck toward CW-DFB external laser sources, ELSFP modules, InP lasers and optical packaging.
- In Korea, the most direct listed exposure is **OE Solutions**: 100G EML, 1.6T transceiver and CPO ELSFP external laser source. But it is not yet confirmed as a global AI data-center mass-production supplier.
- The current trading tape is stronger in AI-RAN / telecom equipment names such as Solid, RFHIC and Samji Electronics than in pure optical-source names. OE Solutions is a structural watchlist name, not an automatic buy.

<div class="thesis-callout">
  <div class="thesis-callout__label">Core Takeaway</div>
  <div class="thesis-callout__body">
    Marvell and Broadcom point to the connectivity bottleneck. TrendForce's laser-source data points to the layer beneath it: <strong>EML and CW-DFB lasers</strong>. Korea's cleanest technical proxy is OE Solutions, but the investable signal is customer qualification, repeat orders and a clean flow turn.
  </div>
</div>

## 1. The Issue: The Bottleneck Is Moving Into Light Sources

AI data-center networks are moving toward 800G and 1.6T links. More GPUs and custom AI accelerators mean more data must move inside racks, between racks and across data centers. Electrical signaling alone becomes increasingly expensive in power and loss, so optical interconnect becomes essential.

But the important part is narrower than "optical modules." The bottleneck is moving into the **laser diode** that creates the light.

[Fact] TrendForce expects 800G+ optical transceiver shipments to rise from 24 million units in 2025 to about 63 million units in 2026. It also identifies EML and CW lasers as key light-source categories for medium- to long-reach optical modules. ([TrendForce][1])

[Fact] TrendForce expects the global AI optical transceiver market to reach US$26 billion in 2026 and identifies EML, CW-LD, optical alignment and power / thermal management as expansion bottlenecks. ([TrendForce][2])

Using the reported 50.7 million per month figure:

```text
50.7 million units / month × 12 = 608.4 million units / year
608.4 million laser diodes / 63 million 800G+ transceivers = ~9.7 laser diodes per module
```

This is not a precise bill-of-materials model. Channel count, wavelength structure and architecture vary. But it is a useful scale check: laser diodes are no longer a small hidden part.

## 2. EML vs. CW-DFB

EML is the high-performance, harder-to-make laser source for high-speed medium- and long-reach modules. It carries high signal-integrity value but is concentrated among a small set of suppliers.

CW-DFB is different. It provides a stable continuous light source, often paired with silicon photonics where modulation happens outside the laser. Silicon photonics does not eliminate laser demand. It shifts the value toward stable external light sources.

NVIDIA's CPO architecture points in the same direction: optical engines sit close to the switch ASIC, while external laser-source modules provide light to those engines. ([NVIDIA Technical Blog][3])

## 3. Korea: Directness and Tradeability Are Different

| Category | Korean name | Relation to light-source bottleneck | Read-through |
|---|---|---|---|
| Most direct | OE Solutions | 100G EML, 1.6T transceiver, CPO ELSFP external laser source | Best technical proxy, but needs qualification and repeat orders |
| Contract visibility | Optocore | AI data-center 400G/800G transceiver contracts | Real order signal, but financial / audit risk is high |
| Adjacent laser / optics | QSI, WooriRo | LD / PD / AWG / PLC exposure | Related, but not yet confirmed AI EML/CW mass supply |
| Thematic optical names | Daehan Optical, BWE | Fiber / module / trading themes | 3-4 month spikes already unwound materially |
| Current flow | Solid, RFHIC, Samji, KMW | AI-RAN / RU / telecom equipment | Better current tape, but not pure light-source exposure |

OE Solutions is the most direct Korean name. The company has announced an ELSFP external laser-source module for CPO and highlighted vertically integrated laser design and manufacturing. ([OE Solutions][4]) Newsis also reported that OE Solutions would show 100G EML, a 1.6T optical transceiver and CPO ELSFP at AI EXPO Korea 2026. ([Newsis][5])

But the wording matters:

<div class="thesis-callout">
  <div class="thesis-callout__label">OE Solutions Framing</div>
  <div class="thesis-callout__body">
    OE Solutions is Korea's most direct listed proxy for the EML / CW external-source bottleneck. It is not yet confirmed as a global AI data-center mass-production supplier. The next proof points are customer qualification, repeat purchase orders and gross-margin improvement.
  </div>
</div>

## 4. Current Tape

The 3-4 month optical / CPO winners were mostly high-beta names: BWE, Gigalane, Daehan Optical, Mercury and Woorinet. Many have already retraced 50% or more from their April highs.

As of June 2, 2026, the current flow screen is not yet a clean pure-CPO rotation:

| Name | 5D return | 20D return | 5D foreign | 5D real money | Read |
|---|---:|---:|---:|---:|---|
| RFHIC | -20.2% | -12.6% | +KRW 49.7bn | -KRW 33.2bn | Foreign-only bid; possible short-cover / program flow |
| Solid | -21.4% | -15.8% | +KRW 1.5bn | +KRW 0.0bn | Best balanced pullback candidate |
| Samji Electronics | -12.1% | +38.7% | +KRW 5.5bn | +KRW 0.6bn | Lower-noise accumulation candidate |
| OE Solutions | -16.4% | -10.9% | -KRW 0.9bn | -KRW 1.8bn | Most direct, but flow turn not confirmed |
| Daehan Optical | -30.6% | +27.4% | -KRW 90.9bn | -KRW 7.7bn | Distribution phase |
| BWE | -44.6% | -23.8% | -KRW 7.6bn | -KRW 0.5bn | Broken April leader |

## Final View

The Marvell / Broadcom story asked: what comes after HBM? The first answer was substrates, networking PCBs and power integrity. The next, more specific answer is **EML and CW-DFB laser sources**.

In Korea, OE Solutions is the best structural watchlist name. But the current trading priority is not the same as the technology map. Solid, RFHIC and Samji Electronics currently show better tactical flow, while OE Solutions needs a cleaner 36,000-38,200 won recovery and foreign + institutional co-buying before the signal improves.

[1]: https://www.trendforce.com/presscenter/news/20251208-12823.html "AI Data Centers Ignite a Laser Shortage Wave"
[2]: https://www.trendforce.com/presscenter/news/20260420-13017.html "Global AI Optical Transceiver Market to Reach US$26 Billion in 2026"
[3]: https://developer.nvidia.com/blog/how-industry-collaboration-fosters-nvidia-co-packaged-optics/ "How Industry Collaboration Fosters NVIDIA Co-Packaged Optics"
[4]: https://oesolutions.com/ko/oe-solutions-announces-new-elsfp-module-to-meet-growing-demand-for-high-speed-networking/ "OE Solutions ELSFP Module"
[5]: https://www.newsis.com/view/NISX20260506_0003618332 "OE Solutions AI EXPO coverage"
