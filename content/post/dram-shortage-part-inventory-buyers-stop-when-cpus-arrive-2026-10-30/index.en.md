---
title: "Part of the DRAM Shortage Is Inventory. The Day CPUs Arrive, Buyers Stop Buying."
date: 2026-10-30T11:29:00+09:00
categories: ["semiconductors", "market-analysis"]
tags: ["DRAM", "Memory Cycle", "Bullwhip Effect", "Inventory", "Samsung Electronics", "SK hynix", "Micron", "Nvidia", "Dell", "HPE", "TrendForce"]
series: ["Korea Semiconductor Watch"]
slug: "dram-shortage-part-inventory-buyers-stop-when-cpus-arrive-2026-10-30"
description: "Buyers are stockpiling DRAM while they wait for CPUs and substrates. 8-13% of 2027 DRAM shipments may be one-off buffer refill. In 2021 the same setup ended in DRAM price cuts once parts arrived. Commodity DRAM, not HBM, carries the risk."
image: "cover.en.png"
draft: false
---

The market story is simple. DRAM stays short through 2028, and the three memory makers have locked 2027-28 volume into long-term agreements. On its call, SK hynix said customers asked for more than twice the volume it can supply (call transcript, secondary source). [KII, Oct 29](/post/samsung-sk-hynix-lta-volume-locked-terms-flexible-2026-10-29/)

We think part of that shortage is buyers building inventory, not end consumption. A server needs a CPU, DRAM and a substrate. Right now CPUs and substrates are short, so the DRAM that arrived first sits in a warehouse waiting for assembly. Yesterday Intel named the substrate shortage as a limit on server CPU output and said most of its substrate suppliers' new capacity arrives in the second half of 2027. [KII, today's substrate post](/post/substrate-shortage-longer-stocks-fell-daeduck-readthrough-2026-10-30/) That is when DRAM buyers start using what they stockpiled and cut new orders.

This setup has a precedent. In the fourth quarter of 2021, PC makers held 11-13 weeks of DRAM. TrendForce wrote that DRAM had become a component "in relative surplus compared to other components," and that PC makers would lower DRAM inventory as component gaps were partially resolved. It forecast first-quarter 2022 DRAM average prices 8-13% below the prior quarter. [TrendForce, Dec 13, 2021](https://www.trendforce.com/presscenter/news/20211213-11050.html)

<strong>Our view: 2027 memory profits are strong. But we estimate that 8-13% of 2027 DRAM shipments refill buyer inventory, and that share does not repeat. The risk sits in commodity server and PC DRAM more than in HBM. The trigger is CPU and substrate supply in the second half of 2027, which overlaps with new fab output from the memory makers. The size of the buffer cannot be measured precisely. There is also no evidence that it is smaller than in 2021.</strong>

## Buyers are stockpiling DRAM now

The build-up is in the filings and reports.

- <strong>Cloud:</strong> TrendForce wrote that US cloud providers' DRAM inventory rose in the second quarter of 2026 because of server CPU shortages. [TrendForce, Jul 9](https://www.trendforce.com/presscenter/news/20260709-13140.html)
- <strong>PCs:</strong> TrendForce wrote that PC makers are procuring aggressively because they expect shortages in 2027. [TrendForce, Sep 30](https://www.trendforce.com/presscenter/news/20260930-13258.html)
- <strong>Server makers:</strong> HPE's quarterly report says "our current efforts to secure memory components and SSDs in advance to meet forecasted demand may further increase our inventory levels in the medium term." Its unconditional purchase obligations are about $30.4bn, including services. [HPE 10-Q](https://www.sec.gov/Archives/edgar/data/1645590/000164559026000080/hpe-20260731.htm)
- <strong>Dell:</strong> Raw materials inventory rose 3.4 times in a year, from $4.68bn to $15.89bn. Purchase commitments rose 67% in one quarter, from $20.8bn to $34.8bn. [Dell 10-Q](https://www.sec.gov/Archives/edgar/data/1571996/000157199626000046/dell-20260731.htm)
- <strong>Apple:</strong> Components inventory rose 3.6 times in nine months, from $2.12bn to $7.65bn. Manufacturing purchase obligations are $57.0bn, with $56.2bn payable within 12 months. [Apple 10-Q](https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm)

![Latest-quarter growth in inventory and revenue for Apple, HPE, HP Inc., Lenovo and Xiaomi. Inventory: Apple +87%, HPE +65%, HP Inc. +24%, Lenovo +80%, Xiaomi +29%. Revenue: +16%, +34%, +13%, +43% and -6%. Lenovo and Xiaomi are secondary data.](/post-assets/dram-shortage-part-inventory-buyers-stop-when-cpus-arrive-2026-10-30/buyer-inventory-vs-sales.en.png)

Device and server makers' inventories grew roughly 2 to 5 times faster than their sales. Inventory value mixes in memory price increases, GPUs and finished servers, so these numbers should not be read as DRAM units. The direction is clear. Supplier inventory is near historical lows (TrendForce as cited in press reports, secondary source), and inventory has moved from suppliers to buyers. Supplier revenue is booked on shipment, so DRAM piling up in buyers' warehouses still shows up as growth in suppliers' results.

## Why it piles up: orders equal consumption plus the change in target inventory

A buyer's orders equal consumption plus the change in target inventory. Target inventory is target weeks times weekly consumption. So even with flat consumption, raising target weeks makes orders jump.

The arithmetic is simple. In a year when a buyer lifts its target from six weeks to eight, orders run about 4% above consumption even with no change in use (2 weeks ÷ 52). In the year it cuts the target back to six weeks, orders run about 4% below consumption. Without any drop in consumption, orders swing by about 8 percentage points between those two years.

| Buyer rule | How it works | What we see now |
|---|---|---|
| Kitting delay | The scarcest part sets how many servers get built; spare DRAM waits | Cloud DRAM inventory rose on CPU shortages (TrendForce, July) |
| Higher safety stock | Longer lead times and more uncertainty raise target weeks | PC makers' aggressive procurement (TrendForce, September) |
| Buying ahead of price | Buy early when next quarter's increase exceeds holding cost | Purchase obligations and inventory jumps at Apple, HPE and Dell |
| Allocation games | The lower the allocation rate, the more buyers over-request | Customer requests above twice supply (SK hynix call, secondary) |

Buyers do not cancel the DRAM that is waiting. It is tied up in long-term agreements and prepayments, they will need it when CPUs arrive, and they fear losing their allocation. So the build-up is quiet, and the unwind comes all at once.

## Size: there is no evidence it is smaller than 2021

We estimate the size as shipments minus installations. DRAM bit shipments grow 20-25% in 2026 (Micron and broker estimates, secondary). Weighting separate installation growth rates for servers, HBM, mobile, PCs and graphics gives installation growth of 6-15%. The difference stays in buyers' warehouses.

- The net build in 2026 alone equals 2-9 weeks of end-2026 consumption (center about 5 weeks).
- The excess over normal inventory is 1-5 weeks on the base path. It depends on buyers' starting inventory at end-2025, and it is near zero if installation runs fast.
- In 2021, PC makers held 11-13 weeks of DRAM in total. With a 6-8 week normal, the excess was 3-7 weeks.

![Weeks of DRAM held by buyers. 2021 PC makers: 11-13 weeks total, 3-7 weeks above a 6-8 week normal. End-2026 buyers: a 2026 net build of 2-9 weeks in our model (center 5) and 1-5 weeks above normal.](/post-assets/dram-shortage-part-inventory-buyers-stop-when-cpus-arrive-2026-10-30/buffer-weeks-vs-2021.en.png)

Today's excess may be smaller than 2021's, or about the same. There is no consistent series with the same definition, so we cannot tell. Not knowing the size is no reason for comfort.

The speed worries us more. In our model, fourth-quarter 2026 shipments run about 17% above installations. As long as that level gap remains, the buffer keeps growing every quarter in 2027 even if the two growth rates converge. The model puts about 13% of 2027 DRAM shipments into buffer refill. If installation grows 24% and server assembly speeds up, that drops to about 8%. The moment buffer building stops, that share disappears from orders even with unchanged consumption.

## This is how 2021 ended

| Stage | 2021-22 | 2026-27 |
|---|---|---|
| Scarce part | Components other than DRAM (DRAM in relative surplus) | Server CPUs and advanced EMIB substrates |
| Where DRAM piled up | PC makers, 11-13 weeks total (4Q21) | US cloud, server makers, PC makers, size undisclosed |
| Trigger | Component gaps partially resolved | Substrate suppliers add about 40%, mostly in 2H27 (Intel call, secondary) |
| Price | 1Q22 DRAM average prices forecast down 8-13% QoQ (TrendForce) | Not yet known |

In 2021, PC makers were expected to lower DRAM inventory once component gaps partially closed. Buyers first use the DRAM they stockpiled, and when they decide the shortage is over they also cut target inventory. Both moves pull orders below consumption. Today's trigger is the same kind. Intel said the industry stays supply-constrained throughout 2027 and into 2028. The second half of 2027, when substrates start to loosen, is the earliest window for the unwind.

## Commodity DRAM is riskier than HBM

Nvidia takes the HBM bullwhip first. Its supply and capacity commitments rose from $119bn to $279bn in a single quarter. 96% falls in fiscal 2027-2029, and they are "primarily memory and manufacturing facilities." [Nvidia 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) If GPU demand turns, these commitments show up first as Nvidia write-downs, before memory makers see cancelled orders. There is a precedent. In the first quarter of fiscal 2026, Nvidia took "a $4.5 billion charge associated with H20 excess inventory and purchase obligations," and it still carries a $2.1bn liability for excess inventory purchase obligations.

Commodity server and PC DRAM has no such buffer. Dell, HPE and cloud providers buy directly from the memory makers. When the buffer unwinds, that volume turns straight into fewer new orders for memory makers. The bigger a maker's commodity DRAM mix, the larger its exposure. In Korea, Samsung Electronics sits closer to this risk than SK hynix.

## When this warning would be wrong

- If server unit growth catches up with server DRAM bit growth in the first half of 2027, today's buffer was just assembly delay. The risk shrinks.
- If buyer inventory days fall while CPU supply rises and DRAM spot prices hold above contract prices, the buffer went into real servers.
- There is already a counter-signal. In September, TrendForce wrote that "improving server CPU availability has prompted CSPs and server OEMs to increase bit procurement." As CPUs loosened, DRAM procurement rose instead of falling. If that holds through 2027, the buffer was assembly delay.
- If buyer inventories rise while same-generation GPU rental rates and follow-on orders both weaken, the unwind has come early. When inventory, rental rates and follow-on orders move the same way, the warning becomes reality.

Our 2027 memory profit view stands. The warning targets the share of that profit that will not repeat, and the timing of when it disappears. Long-term agreements can lock volume, but they cannot lock buyers' inventory decisions.

## What to watch next

| When | What | How to read it |
|---|---|---|
| Early Nov | Apple and Supermicro September quarters | Whether purchase obligations and inventory keep outgrowing sales |
| Mid-Nov | Nvidia October quarter | If supply commitments and excess inventory provisions rise together, the HBM buffer is thinning |
| Late Nov | Dell third quarter | Raw materials inventory and purchase commitments |
| Early Dec | HPE October quarter | Whether inventory and unconditional purchase obligations turn down |
| Mid-Dec | Micron November quarter | Whether customer inventory adjustment comments spread to servers |
| Late Dec | TrendForce 1Q27 contract price outlook | Whether buyer accumulation language turns into inventory adjustment language |
| Late Jan 2027 | Intel fourth quarter | Whether the substrate relief moves earlier than 2H27 |

<strong>Is today's buyer DRAM inventory a sensible hedge against real demand, or a 2021-style bullwhip? Tell us which number would change your mind.</strong>

## Key sources

- [TrendForce, PC makers' DRAM inventory and 1Q22 price outlook, Dec 13, 2021](https://www.trendforce.com/presscenter/news/20211213-11050.html)
- [TrendForce, buyers' inventories still flush, Feb 17, 2022](https://www.trendforce.com/presscenter/news/20220217-11128.html)
- [Dell 10-Q, quarter ended Jul 31](https://www.sec.gov/Archives/edgar/data/1571996/000157199626000046/dell-20260731.htm)
- [Apple 10-Q, quarter ended Jun 27](https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm)
- [TrendForce, US cloud DRAM inventory, Jul 9, 2026](https://www.trendforce.com/presscenter/news/20260709-13140.html)
- [TrendForce, 4Q DRAM contract prices and buyer procurement, Sep 30, 2026](https://www.trendforce.com/presscenter/news/20260930-13258.html)
- [HPE 10-Q, quarter ended Jul 31](https://www.sec.gov/Archives/edgar/data/1645590/000164559026000080/hpe-20260731.htm)
- [Nvidia 10-Q, quarter ended Jul 26](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- [Intel CEO and CFO prepared remarks, Oct 29](https://d1io3yog0oux5.cloudfront.net/_47986fe477a6ac84fe34efbcbf38dd13/intel/db/887/9273/prepared_remarks/Q3%2726_Prepared_Remarks.pdf)
- HP Inc. SEC XBRL data; Lenovo and Xiaomi aggregator data (secondary)

For research and information only, not investment advice. Buffer sizes and shipment shares are estimates from a shipments-minus-installations model, not company guidance or trading instructions. Figures are dated. AI tools were used in research and editing.
