---
title: "The Market Missed Jensen Huang’s Bigger HBM4 Comment: All Three Vendors Are Qualified"
date: 2026-06-05T16:30:00+09:00
description: "Jensen Huang's reported comment that Samsung Electronics, SK hynix and Micron are all qualified and in production for NVIDIA Vera Rubin HBM4 shifts the debate from qualification to allocation, yield, ASP and margin."
categories: ["Market-Outlook"]
tags: ["Jensen Huang", "NVIDIA", "Vera Rubin", "HBM4", "HBM4E", "Samsung Electronics", "SK hynix", "Micron", "MU", "Hanmi Semiconductor", "AI memory"]
slug: jensen-huang-hbm4-three-vendors-qualified-market-missed-2026-06-05
valley_cashtags:
  - Samsung Electronics
  - SK hynix
  - Hanmi Semiconductor
draft: false
---

> Follow-up context: this note follows [Sam-Ha-Ma parity follow-up](/post/sam-hama-parity-follow-up-ai-chip-memory-pe-map-2026-06-05/), [Samsung and SK hynix are cheap versus Micron again](/post/samsung-hynix-micron-forward-per-parity-memory-catch-up-2026-06-03/), [Samsung HBM4E 12-high sample](/post/samsung-electronics-hbm4e-12h-sample-market-watch-hanmi-tc-bonder-2026-06-01/), and [Hanmi Semiconductor TC-bonder TAM expansion](/post/hanmi-semiconductor-ir-tc-bonder-tam-expansion-watchlist-2026-06-02/). Related hubs: [AI HBM hub](/page/korea-semiconductor-hbm-kospi-hub/), [Korea semiconductor value-chain hub](/page/korea-semiconductor-equipment-ip-hub/), and [Korea Daily Market Hub](/page/korea-daily-market-hub/).

## TL;DR

Jensen Huang's reported comment means Samsung Electronics, SK hynix and Micron have all passed qualification and entered production competition for NVIDIA Vera Rubin HBM4. Korean media quoted Huang as saying, "All three vendors have been qualified," and that all three are in production and racing to support NVIDIA. ([Daum/JoongAng][1])

The largest incremental beneficiary is Samsung Electronics because the market's main doubt was whether Samsung could enter the NVIDIA HBM socket. For SK hynix, the read-through is mixed: monopoly premium dilution, but stronger total HBM demand.

But **qualified does not mean equal allocation, equal margin or guaranteed high-volume supply**. The investment question has moved from qualification to **HBM4 allocation, yield, ASP and margin**.

<div class="thesis-callout">
  <div class="thesis-callout__label">Core Takeaway</div>
  <div class="thesis-callout__body">
    The HBM4 supply chain is moving from a single-leader narrative toward a three-vendor qualified competition for Vera Rubin. Samsung gets the largest discount-compression event. SK hynix loses some monopoly premium, but remains the leadership name in a larger TAM.
  </div>
</div>

## The Comment

According to Korean media coverage on June 5, 2026, Huang told reporters after arriving at Seoul Gimpo Business Aviation Center that all three HBM vendors were qualified and in production. The three vendors are Samsung Electronics, SK hynix and Micron. ([Daum/JoongAng][1])

This matters because the wording is different from the 2024 discussion, when Samsung's HBM qualification was still in progress and Huang said more engineering work was needed. ([Yonhap][5])

| Phrase | Investor interpretation | What not to over-read |
|---|---|---|
| All three vendors have been qualified | NVIDIA qualification has been passed | Not equal allocation |
| All three vendors are in production | HBM4 ramp has started | Not proof of mass yield or margin |
| Racing to support Vera Rubin | Three-vendor competition for Vera Rubin supply | Not the end of SK hynix leadership |

## Why Vera Rubin Matters

NVIDIA says the Vera Rubin platform has entered full production ramp across a broad supply chain. ([NVIDIA Newsroom][2]) The official Vera Rubin NVL72 spec shows why HBM4 matters: 72 Rubin GPUs, 36 Vera CPUs, 20.7TB of HBM4 and 1,580TB/s of GPU-memory bandwidth. Each Rubin GPU carries 288GB of HBM4 and 22TB/s of bandwidth. ([NVIDIA Vera Rubin NVL72][3])

The arithmetic is simple:

```text
288GB HBM4 per Rubin GPU
× 72 Rubin GPUs per NVL72 rack
= 20,736GB ≈ 20.7TB HBM4 per rack
```

This is not a small product refresh. Vera Rubin is a rack-scale AI factory platform that can pull all three HBM vendors into production competition.

## Samsung Electronics: Biggest Incremental Positive

Samsung is the largest surprise beneficiary. The market doubt was whether Samsung HBM could pass NVIDIA qualification. That doubt is now lower.

Samsung has also officially begun shipping 12-layer HBM4E samples. The company says the part reaches up to 16Gbps, 48GB capacity and up to 3.6TB/s per stack. ([Samsung Semiconductor][4])

The key checks now are:

| Checkpoint | Why it matters |
|---|---|
| HBM4 shipment start | Turns narrative into revenue |
| NVIDIA allocation | Separates qualification from real share |
| DS gross margin / OPM | Shows whether HBM mix lifts earnings |
| Base-die and packaging yield | Determines the true profitability of HBM4 |

Samsung's thesis is now HBM discount compression. It is not yet equal allocation or equal profitability versus SK hynix.

## SK hynix: From Monopoly Premium To Leadership Premium

The read-through for SK hynix is mixed.

The negative is obvious: a three-vendor qualified supply chain lowers the "NVIDIA monopoly" premium. But Vera Rubin's HBM intensity expands the total market.

Reuters reported that SK Group Chairman Chey Tae-won said SK hynix aims to double wafer capacity over the next five years and repeated his view that memory bottlenecks could persist through 2030. ([MarketScreener/Reuters][7])

The thesis moves from:

```text
NVIDIA HBM monopoly premium
```

to:

```text
leader allocation + yield + customer trust + next-generation HBM roadmap
```

So "Samsung qualified = short SK hynix" is too simple. The cleaner interpretation is that SK hynix shifts from monopoly premium to leadership premium.

## Micron: Benchmark For Korea Memory Discount

Micron is also confirmed as part of the Vera Rubin HBM4 race. For Korean investors, that is important because Micron remains the U.S.-listed AI-memory proxy.

As discussed in the [Sam-Ha-Ma parity follow-up](/post/sam-hama-parity-follow-up-ai-chip-memory-pe-map-2026-06-05/), Micron's premium is not simply a technology premium. It is a U.S. listing premium, dollar-asset premium, AI-memory scarcity premium and HBM4/SOCAMM2/data-center SSD narrative.

That keeps Micron relevant. It also strengthens the case for Samsung and SK hynix discount compression if their EPS estimates hold.

## Hanmi Semiconductor Read-Through

Hanmi Semiconductor is a positive second-order read-through. If all three memory vendors are racing to support Vera Rubin, HBM4 capacity expansion can move beyond a single SK hynix-centered narrative.

But this is not an order confirmation. Hanmi's direct upside depends on whether TC-bonder orders expand from SK hynix to Samsung, Micron, OSATs or foundry-related advanced packaging customers.

The revenue logic is:

```text
Hanmi HBM equipment revenue
= memory-vendor HBM capex
× TC bonders per line
× ASP
× replacement and upgrade demand
```

The first variable has improved. The customer-order variable is still unconfirmed.

| Customer | Current read | Hanmi implication | Confidence |
|---|---|---|---|
| SK hynix | Direct order history | Core direct customer | High |
| Micron | Relationship optionality | Overseas expansion option | Medium |
| Samsung | HBM ramp positive, direct order unconfirmed | Internal SEMES / alternative vendor risk | Low-Medium |
| OSAT / foundry | Advanced packaging TAM expansion | 2.5D and AI ASIC equipment option | Medium |

## What Not To Over-Read

Still unconfirmed:

1. NVIDIA HBM4 allocation by vendor
2. Samsung HBM4 mass-production yield
3. ASP and gross margin by product
4. 12-high / 16-high HBM4 or HBM4E split
5. Supply scope outside Vera Rubin
6. Hanmi TC-bonder orders from Samsung or Micron

The accurate wording is:

> NVIDIA's Vera Rubin HBM4 supply chain appears to have moved into a three-vendor qualified structure. The game now shifts from qualification to allocation, yield, ASP and margin.

## Bottom Line

This is positive for all three memory vendors, but the largest incremental positive is Samsung Electronics. SK hynix remains the quality leader, but the monopoly-premium language should be toned down. Micron remains the U.S. benchmark. Hanmi Semiconductor is a high-beta equipment read-through, but needs actual TC-bonder orders to turn narrative into earnings.

Practical priority:

```text
1. Samsung Electronics
- largest HBM discount-compression event

2. SK hynix
- still the quality leader, but not a monopoly story

3. HBM equipment / inspection / packaging chain
- benefits if three-vendor production competition extends capex

4. Micron
- benchmark for the Korean memory discount
```

## Sources

[1]: https://v.daum.net/v/20260605142553729 "Jensen Huang says all three HBM vendors are in production"
[2]: https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory "NVIDIA Vera Rubin Platform Enters Full Production Ramp"
[3]: https://www.nvidia.com/en-au/data-center/vera-rubin-nvl72/ "NVIDIA Vera Rubin NVL72"
[4]: https://semiconductor.samsung.com/news-events/news/samsung-electronics-begins-shipment-of-industry-first-hbm4e-samples/ "Samsung Electronics Begins Shipment of Industry-First HBM4E Samples"
[5]: https://www.yna.co.kr/view/AKR20240604153652009 "Yonhap: Jensen Huang on Samsung HBM qualification in 2024"
[6]: https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share "Counterpoint Global DRAM and HBM Market Share"
[7]: https://www.marketscreener.com/news/sk-hynix-plans-to-double-wafer-capacity-in-next-five-years-group-chairman-says-ce7f5dd9d180f721 "Reuters: SK Hynix plans to double wafer capacity in next five years"
