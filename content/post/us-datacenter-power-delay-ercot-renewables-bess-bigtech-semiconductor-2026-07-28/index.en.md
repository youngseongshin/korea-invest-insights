---
title: "Why U.S. Data Centers Are Slipping: ERCOT's Playbook and the Timeline for Big Tech and Semiconductors"
slug: "us-datacenter-power-delay-ercot-renewables-bess-bigtech-semiconductor-2026-07-28"
date: 2026-07-28T21:45:00+09:00
description: "A source-checked analysis of U.S. data-center delays across grid interconnection, transformers, turbines, and local opposition; why ERCOT lowered risk with 40.3 GW of solar, 22.0 GW of batteries, and 5.1 GW of demand response; and what the bottleneck means for Big Tech, GPUs, HBM, memory, and power equipment stocks."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags:
  - "US data centers"
  - "AI infrastructure"
  - "power grid"
  - "ERCOT"
  - "BESS"
  - "solar"
  - "Big Tech"
  - "Nvidia"
  - "HBM"
  - "Samsung Electronics"
  - "SK hynix"
  - "power equipment"
  - "Research OS"
draft: false
---

> Context: In [Big Tech's AI earnings trilogy](/post/big-tech-ai-earnings-capex-roi-memory-2028-fcf-2026-07-22/), the critical 2028 question was whether AI capex could convert into revenue and free cash flow. Our [Korean data-center beneficiary ranking](/post/korea-ai-datacenter-beneficiaries-power-cooling-operator-flow-ranking-2026-07-23/) and [AI data-center power bottleneck map](/post/ai-datacenter-power-bottleneck-korea-value-chain-screen-2026-07-04/) argued that power, cooling, and backup-power suppliers monetize earlier than operators. This report applies that framework to the United States.

## TL;DR

- U.S. data-center delays are real, although no single national registry can produce a definitive cancellation rate. Allianz Research summarized that about 12 GW of U.S. capacity planned for 2026 could be delayed or canceled, with only about 5 GW under active construction. NERC separately confirmed that several regions cut large-load forecasts because interconnections and completions were slower than expected.[^allianz][^nerc]
- The bottleneck has four layers: <strong>grid interconnection, transformers and breakers, generation equipment, and local permitting and cost allocation</strong>. At the end of 2025, 1,312 GW of generation and 749 GW of storage were waiting in U.S. interconnection queues. Generator step-up transformer lead times exceeded 160 weeks in early 2026.[^lbl][^reuters-transformer]
- The phrase “more than half of U.S. states are under shortage warnings” overstates the official assessment. NERC found adequate resources in all areas under normal summer peak conditions, while identifying elevated risks under extreme conditions in selected regions.[^nerc]
- ERCOT is powerful evidence for the solar-plus-storage thesis. NERC lists 40.3 GW of solar and 22.0 GW of battery storage in ERCOT, with expected peak contributions of 29.7 GW and 20.7 GW. The probability of an Energy Emergency Alert in the highest-risk hour fell from 3.1% to 0.43%.[^nerc]
- But ERCOT is not a solar-and-battery-only story. Its result also reflects 5.1 GW of demand response, curtailable computational loads, faster market rules, and an existing base of gas, nuclear, and wind generation.
- Solar plus BESS is the fastest incremental supply option for the next three years, not a complete 24/7 solution. The practical architecture is <strong>solar+BESS, existing nuclear or gas PPAs, behind-the-meter gas engines or fuel cells, and flexible compute loads</strong>.
- For Big Tech, delays cap near-term growth but increase the scarcity value of already energized capacity. For semiconductors, they create both a near-term shipment timing risk and a possible extension of the 2027-2028 demand cycle.

<div class="thesis-callout">
  <div class="thesis-callout__label">Bottom line</div>
  <div class="thesis-callout__body">
    The AI bottleneck has moved from chips to power. ERCOT's lesson is not “renewables alone,” but a portfolio of fast resource additions, batteries, flexible interconnection, demand response, and firm generation. Equity effects arrive on three different clocks: a near-term growth ceiling for Big Tech, deferred semiconductor installations into 2027-2028, and direct orders for power equipment and storage suppliers.
  </div>
</div>

## 0. Fix the definitions first

Data-center “capacity” can mean IT load, total facility power, or the final announced campus size. An interconnection “queue” can refer to generation projects or large loads. Mixing them produces impressive but misleading numbers.

| Common claim | Evidence check | Working assumption |
|---|---|---|
| Current U.S. data-center capacity is 50 GW | Estimates vary by scope | Wood Mackenzie estimates roughly 24 GW currently and 110 GW by 2030.[^reuters-transformer] |
| 30-50% of 2026 projects are delayed | Industry estimate, not an official census | Use the direction, not a false point estimate. Allianz says 12 GW planned versus about 5 GW under construction.[^allianz] |
| Half of U.S. states face shortage warnings | Stronger than NERC's language | All areas have enough resources under normal conditions; selected regions face elevated extreme-weather risk.[^nerc] |
| ERCOT has already exceeded 90 GW | More than 92 GW is a forecast | ERCOT's summer forecast is above 92 GW; NERC's demand-response-adjusted planning figures are lower.[^kera][^nerc] |
| ERCOT has 35 GW solar and 12 GW BESS | Directionally right but stale | NERC lists 40.3 GW solar and 22.0 GW BESS for 2026.[^nerc] |
| The U.S. queue is 2.6 TW | Depends on date and scope | End-2025 active generation and storage queues totaled 2.061 TW. This is not the data-center load queue itself.[^lbl] |

## 1. How large is the delay?

There is no comprehensive U.S. data-center project registry. A single campus can have an announced final capacity, a smaller first-building capacity, and multiple phased energization dates. “Delayed,” “canceled,” “paused,” and “land banked without power” are not the same.

Still, three independent signals align:

1. Allianz Research says about 12 GW of U.S. capacity planned for 2026 may be delayed or canceled, with only about 5 GW under active construction.[^allianz]
2. NERC says several assessment areas revised large-load forecasts downward because interconnections and completions were slower than previously expected.[^nerc]
3. Data Center Watch, cited by media reports, counted 75 projects worth about $130 billion blocked or delayed in the first quarter of 2026.[^dcwatch]

The defensible conclusion is not that exactly half will disappear. It is that announced AI capacity is moving faster than power delivery and construction, pushing a material portion of 2026 supply into 2027 and beyond.

## 2. The four-layer bottleneck

| Layer | Verified measure | Why it matters |
|---|---:|---|
| Generation and storage interconnection | 2,061 GW active at end-2025; median time to operation above five years for 2025 completions | New load cannot scale without supply and transmission. |
| Large-load interconnection | 36-48 months in PJM data-center growth zones | A completed shell cannot monetize without an energization date. |
| Transformers and breakers | Step-up transformers above 160 weeks; high-voltage breakers around 125 weeks | One missing component can hold up an entire substation. |
| Permitting, rates, and local opposition | 75 projects and $130 billion delayed or blocked in Q1 2026 | Water, noise, land, and cost-shifting can stop construction. |

The generation and storage queue contains roughly 8,200 projects. Only 13% of capacity that applied from 2000 through 2020 had reached commercial operation by the end of 2025.[^lbl] Queue volume is therefore not the same as future supply.

Equipment is a more immediate physical constraint. Reuters reported that generator step-up transformer lead times exceeded 160 weeks in the first quarter of 2026 and high-voltage breakers reached 125 weeks. Utilities now order years ahead and sometimes prepay for manufacturing slots.[^reuters-transformer]

Gas turbines are also not an instant alternative. Mitsubishi Power said orders stretch to 2030 and installation lead times have moved to five years or more.[^gas-turbine]

## 3. The bottleneck has moved from racks to substations

The monetization chain is:

```text
AI demand and customer contract
→ land and power agreement
→ generation, transmission, and substation approval
→ transformer, switchgear, and breaker delivery
→ building, cooling, and backup power completion
→ GPU, network, and memory installation
→ commissioning
→ customer workload activation
→ cloud and AI revenue recognition
```

FERC's June 2026 orders to six regional grid operators confirm that large-load integration has become a national policy issue.[^ferc]

But “not enough generation” is only one failure mode. A region can have power plants but no transmission. It can have transmission but no transformers. It can have equipment but no agreement on who pays. And a rigid 24/7 load requires more infrastructure than a load that can shift training jobs across time or location.

## 4. What ERCOT did differently

### 4-1. Solar and batteries made a measurable contribution

NERC's 2026 assessment lists 40.3 GW of solar and 22.0 GW of battery storage in ERCOT. Expected peak contributions are 29.7 GW and 20.7 GW.

| ERCOT resource | Nameplate capacity | Expected peak contribution | Contribution rate |
|---|---:|---:|---:|
| Wind | 40.6 GW | 9.45 GW | 23% |
| Solar | 40.3 GW | 29.68 GW | 74% |
| BESS | 22.0 GW | 20.69 GW | 94% |

Texas set a 29.3 GW solar output record and a 7.2 GW battery discharge record in summer 2025. With 8.78 GW of BESS added during 2025 and another 2.68 GW through March 2026, the modeled probability of an Energy Emergency Alert in the highest-risk hour fell from 3.1% to 0.43%.[^nerc]

Batteries are not powering the entire state for days. They shift midday solar into the evening, respond to sudden imbalances, and stabilize frequency.

### 4-2. Supply was only half the answer

ERCOT has 5.1 GW of available demand response for summer 2026, up 54.9% year over year. NERC says more computational loads can be curtailed during emergencies, reducing its net internal demand forecast by 3.7 GW.[^nerc]

```text
Solar serves daytime demand
→ batteries bridge the evening ramp
→ gas, nuclear, and wind support firm and nighttime supply
→ large computational loads curtail during stress
→ fast market signals and interconnection rules attract resources
```

ERCOT's lower risk reflects a 12% increase in anticipated resources, more BESS, more demand response, and flexible large loads. It is not a one-technology story.

### 4-3. Remaining weaknesses

- The highest-risk hour is 9 p.m., after solar output fades.
- Far West Texas still faces transmission constraints.
- Simultaneous tripping of large electronic loads can destabilize frequency and voltage.
- The 92 GW figure is a summer forecast, not a realized record.
- Battery power capacity in GW says little about surviving multi-day low-wind or low-solar events without energy-duration data in GWh.

## 5. Is solar plus BESS the fastest solution?

For incremental power over the next three years, yes. For complete 24/7 supply, no.

| Option | Speed to first power | 24/7 firmness | Main constraint | Best role |
|---|---|---|---|---|
| Solar+BESS | Fast | Medium | Land, transformers, duration, nighttime | Fast incremental power and peak support |
| On-site gas engines or small turbines | Medium | High | Gas pipeline, air permits, fuel cost | Bridge power and queue bypass |
| Fuel cells+BESS | Medium | High | Fuel supply, equipment cost, service | Modular behind-the-meter supply |
| Existing nuclear or gas PPA | Fast to medium | High | Transmission and contract structure | Firm supply |
| New combined-cycle gas | Slow | High | Turbine lead time, pipelines, permits | Large long-term supply |
| New transmission | Very slow | High | Permits, land, cost allocation | Structural solution |
| SMR or new nuclear | Very slow | High | Licensing, construction cost, schedule | 2030s firm power |
| Flexible compute load | Fastest | Not a supply source | SLA and software | Faster connection with the same grid |

S&P Global modeled a 627 MW data center and found a solar-plus-storage design cost more than twice as much as a combined-cycle plant while still failing to guarantee power through multi-day low-solar periods.[^spp-solar-gas] That does not invalidate solar+BESS. It defines its role as fast incremental and peak capacity rather than a stand-alone annual solution.

The practical architecture is phased:

1. <strong>Initial energization:</strong> solar, BESS, on-site engines or fuel cells, partial grid service, and flexible batch workloads.
2. <strong>Stabilization:</strong> long-term PPAs with existing nuclear, gas, or hydro; substation and transmission upgrades; longer-duration storage.
3. <strong>Structural supply:</strong> new combined-cycle generation, transmission, nuclear restarts, geothermal, long-duration storage, and eventually advanced nuclear.

## 6. Rules and software matter as much as equipment

FERC's June orders ask PJM, MISO, SPP, CAISO, ISO-NE, and NYISO to justify or reform tariffs for large loads. The options include co-located generation, flexible transmission service, behind-the-meter generation, and temporary service from nearby generators.[^ferc]

The emerging asset is curtail-able compute.

| Workload | Power flexibility | Reason |
|---|---:|---|
| Real-time inference | Low | Latency and outage costs are high. |
| Enterprise cloud | Low to medium | Customer SLAs must be protected. |
| Training between checkpoints | Medium | Short pauses and restarts may be possible. |
| Batch training and preprocessing | High | Work can shift across time and regions. |
| Crypto mining | Very high | Curtailment is relatively simple. |

Not all AI demand is flexible. But if part of a campus can curtail, the grid no longer has to build every upgrade for a fully coincident worst-case peak before first energization.

## 7. Impact on Big Tech stocks

### 7-1. Negative channel: contracted demand converts to revenue more slowly

```text
Power delivery delay
→ data-center activation delay
→ GPU service capacity remains constrained
→ backlog and RPO convert more slowly
→ near-term cloud growth is capped
→ depreciation may begin before utilization is optimal
```

If land, buildings, and equipment deposits are paid before power arrives, free cash flow comes under pressure. The 2028 FCF question is therefore not just capex. It is energized capacity and utilization.

### 7-2. Positive channel: scarcity value of live capacity

When supply grows slower than demand, already energized GPU capacity becomes more valuable:

- Discounting can decline.
- Long-term commitments and prepayments can increase.
- High utilization absorbs depreciation.
- Operators with secured power and geographic diversification gain share.

Data-center delays are not equally negative for all hyperscalers. They hurt companies with large unpowered plans, while strengthening pricing for companies with energized capacity.

### 7-3. The new Big Tech scorecard

| Metric | Positive signal | Negative signal |
|---|---|---|
| Energized power | Specific MW/GW and dates | Only final campus size |
| Power sourcing | Multi-region PPAs, on-site power, grid contracts | One utility and a distant date |
| Customer contracts | Long-term commitments, prepayments, minimum use | Non-binding interest |
| Capex phasing | Investment aligned with energization | Buildings and chips waiting for power |
| Flexibility | Workloads shift across time and regions | Every load treated as rigid 24/7 demand |
| Cash flow | Revenue and utilization outrun depreciation | Depreciation and interest rise first |

The next earnings-call question should be: how many gigawatts can turn on, when, and how much customer revenue is attached?

## 8. Impact on semiconductor stocks

### 8-1. Near-term risk: a gap between ordering and installation

Hyperscalers can either accept GPUs and HBM before power is ready, creating customer inventory, or delay deliveries to match energization, creating quarterly shipment gaps.

Warning signs include:

- Rising customer inventory days for GPUs and servers
- Lower prepayments and longer delivery schedules
- More references to “waiting for power”
- Server ODM shipments rising faster than live cloud capacity
- HBM contracts remaining intact but quarterly delivery dates moving out

“Deferred demand” is not automatically bullish.

### 8-2. Medium-term opportunity: a longer cycle tail

If projects move rather than disappear, the demand curve can flatten and extend.

```text
2026 data-center capacity slips
→ GPU and HBM installations move into 2027-2028
→ 2026 shipment growth moderates
→ deferred installations overlap with replacement and expansion demand
→ the peak may be lower, but the cycle lasts longer
```

This requires three conditions:

1. Final AI demand does not deteriorate.
2. Hyperscaler financing capacity and credit remain intact.
3. Power solutions are under construction rather than merely announced.

Repeated delays plus weaker AI monetization would turn deferral into cancellation.

### 8-3. Performance per watt becomes more valuable

| Semiconductor layer | Effect of power scarcity |
|---|---|
| GPU and AI ASIC | Performance per watt becomes a stronger purchase criterion. |
| HBM | Reduced data-movement energy and higher accelerator utilization increase its value. |
| Server DRAM | Total cost of ownership, including power and cooling, matters more. |
| Enterprise SSD | Low-power, high-throughput storage reduces GPU idle time. |
| Networking | Faster fabrics command a premium by reducing cluster idle time. |
| Power semiconductors and substrates | High-voltage distribution and conversion become larger parts of system value. |

For SK hynix, the positive channel is HBM and high-value server DRAM's performance-per-watt advantage. Samsung Electronics combines a potential HBM recovery with a broader portfolio in low-power DRAM and enterprise SSDs. But if energization delays create server and client inventory, broader commodity exposure can also increase sensitivity.

## 9. Equity judgment by group

| Group | Next 0-6 months | Next 1-3 years | Judgment |
|---|---|---|---|
| Hyperscalers | Capacity limits growth; live capacity retains pricing | Power access becomes a moat | Wider company dispersion |
| GPU and AI ASIC | Quarterly shipment timing risk | Performance-per-watt and deferred demand | Medium-term positive, near-term volatile |
| HBM and server memory | Delivery cadence and customer inventory matter | Potential cycle extension | Conditionally positive |
| Power equipment | Backlog and pricing remain strong | Capacity expansion can create competition later | Direct beneficiary, valuation matters |
| BESS | Peak and behind-the-meter demand | Longer duration and software value | Structural beneficiary |
| Turbines and engines | Strong orders, slow delivery | Pipeline and permitting constraints | Strong backlog, delayed revenue |
| Nuclear and geothermal | Limited near-term contribution | Firm-power premium | Long duration |

Power equipment is the cleanest direct beneficiary because transformers, breakers, switchgear, cables, and batteries solve the causes of the delay. But a long backlog does not automatically mean a cheap stock. Manufacturing expansion, input costs, deposits, and post-2028 competition still matter.

Korean listed-company exposure remains:

- Grid and distribution: LS ELECTRIC, HD Hyundai Electric, Hyosung Heavy Industries
- Cables: Iljin Electric, Gaon Cable
- BESS and power quality: LG Energy Solution, Samsung SDI, Vinatech
- Cooling: LG Electronics, GST
- Firm power: Doosan Enerbility, SK Gas, GNC Energy

See the [July 23 beneficiary ranking](/post/korea-ai-datacenter-beneficiaries-power-cooling-operator-flow-ranking-2026-07-23/) for price and flow-based stock selection. This report focuses on the duration of the U.S. bottleneck.

## 10. Monthly dashboard

| Indicator | Positive interpretation | Negative interpretation |
|---|---|---|
| First-power MW for data centers | Plans become live capacity | Final size grows while dates slip |
| Large-transformer lead time | Bottleneck and pricing persist | Lead times collapse with cancellations |
| ERCOT and PJM large-load approvals | Faster power delivery | Study timelines extend again |
| BESS deployment and duration | Better evening-peak coverage | High GW but insufficient GWh |
| Demand-response enrollment | More load connects to the same grid | SLA concerns reduce participation |
| Big Tech utilization and RPO conversion | Power and customers arrive together | RPO grows but conversion slows |
| GPU and HBM customer inventory | Deferred demand remains healthy | Chips accumulate without power |
| Cloud growth versus depreciation | Revenue outruns the cost base | Depreciation outruns growth |

## 11. Red team

The constructive case fails if:

1. Delays reflect weaker AI demand rather than power timing.
2. Cloud backlogs and customer prepayments decline.
3. GPU and HBM inventory builds and contracted volumes are canceled.
4. Transformer and BESS manufacturing expansion creates a 2028 price collapse.
5. Local opposition blocks transmission, on-site generation, and renewables simultaneously.

The bearish case fails if:

1. Flexible-load and co-located-generation rules standardize quickly.
2. ERCOT-style curtailment contracts spread to PJM and MISO.
3. Hybrid solar, storage, engines, and fuel cells energize large campuses within two years.
4. Hyperscalers disclose long-term customer contracts alongside firm power dates.
5. HBM contracts and prepayments remain intact despite shifted delivery schedules.

## 12. Final view

U.S. data centers are not delayed only because the country lacks energy. The institutions and equipment required to connect, transform, curtail, and allocate the cost of power are moving more slowly than AI demand.

Solar plus BESS is the fastest incremental response. ERCOT proves that with 40.3 GW of solar, 22.0 GW of battery storage, 50.4 GW of combined expected peak contribution, and a 0.43% modeled emergency-alert probability. But the same evidence highlights 5.1 GW of demand response and curtailable computational load.

The equity implications must be separated by time:

- <strong>Big Tech, near term:</strong> power delivery caps cloud growth, while energized capacity earns scarcity value.
- <strong>Big Tech, medium term:</strong> power, utilization, and customer contracts determine whether 2028 free cash flow recovers.
- <strong>Semiconductors, near term:</strong> delivery adjustments and customer inventory create volatility.
- <strong>Semiconductors, medium term:</strong> if deferral does not become cancellation, GPU and HBM demand can spread into 2027-2028 and extend the cycle.
- <strong>Direct beneficiaries:</strong> transformers, breakers, switchgear, cables, batteries, and on-site generation address the physical cause of delay.

The decisive distinction is between projects with firm power dates and unpowered announcements, and between deferred demand backed by customer contracts and demand that disappears.

> [Fact] Public sources verify delay indicators, NERC risk classifications, ERCOT resources, interconnection queues, and equipment lead times.  
> [Inference] The cycle-extension and scarcity-pricing arguments require customer contracts and final AI demand to hold.  
> [Blocked] Project-level energization dates, behind-the-meter power economics, and exact GPU installation schedules remain largely private.

Related work is collected in the [Exclusive Analysis hub](/page/exclusive-analysis-hub/) and [AI HBM hub](/page/korea-semiconductor-hbm-kospi-hub/).

[^allianz]: [Allianz Research, Thinking fast, building slow: AI and the energy supply crunch](https://www.allianz.com/content/dam/onemarketing/azcom/Allianz_com/economic-research/publications/specials/en/2026/may/2026-05-12-ai-energy-AZ.pdf), May 12, 2026.
[^nerc]: [NERC, 2026 Summer Reliability Assessment](https://www.nerc.com/globalassets/our-work/assessments/nerc_sra_2026.pdf), May 2026.
[^lbl]: [Lawrence Berkeley National Laboratory, Queued Up: 2026 Edition](https://emp.lbl.gov/queues), July 2026.
[^reuters-transformer]: [Reuters, US power companies scramble to secure equipment as surging data center demand strains supplies](https://www.investing.com/news/stock-market-news/us-power-companies-scramble-to-secure-equipment-as-surging-data-center-demand-strains-supplies-4783319), July 9, 2026.
[^dcwatch]: [Tom's Hardware report citing Data Center Watch](https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-75-data-center-build-outs-worth-usd130-billion-have-been-successfully-blocked-in-the-first-four-months-of-2026-bipartisan-opposition-mounts-nationwide-over-fears-of-soaring-power-and-water-costs), June 13, 2026.
[^gas-turbine]: [S&P Global, Mitsubishi Power gas turbine orders stretch to 2030](https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/070326-interview-mitsubishi-power-gas-turbine-orders-stretch-to-2030-amid-ai-security-demand), July 3, 2026.
[^kera]: [KERA News, ERCOT predicts record summer energy demand](https://www.keranews.org/energy-environment/2026-06-04/ercot-predicts-record-summer-energy-demand), June 4, 2026.
[^ferc]: [FERC, FERC Launches Aggressive Targeted Action to Speed Large Load Integration](https://www.ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration), June 18, 2026.
[^spp-solar-gas]: [S&P Global Market Intelligence, Data center power: Combined-cycle plant outperforms solar plus battery](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/03/data-center-power-combined-cycle-plant-outperforms-solar-plus-battery), March 2026.

