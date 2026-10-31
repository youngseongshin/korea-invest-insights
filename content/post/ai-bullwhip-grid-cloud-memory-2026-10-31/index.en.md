---
title: "The AI Bullwhip Map: Grid Requests Are the Most Inflated, Memory Holds the Risk"
date: 2026-10-31T11:56:00+09:00
categories: ["semiconductors", "market-analysis"]
tags: ["AI Infrastructure", "Bullwhip Effect", "Power Grid", "Data Centers", "Cloud", "DRAM", "ERCOT", "PJM", "GE Vernova", "TrendForce"]
series: ["Korea Semiconductor Watch"]
slug: "ai-bullwhip-grid-cloud-memory-2026-10-31"
description: "Excess AI demand looks different at every stage. Grid requests are inflated more than 4x but cost nothing to cancel. Cloud commitments are the largest but get renegotiated. Paid-for memory inventory is the real risk."
draft: false
---

The most inflated number in the AI supply chain is grid connection requests. ERCOT, the Texas grid operator, projects 2032 peak demand of 367.8 GW, about 4.3 times its all-time record of 85.5 GW (Texas Tribune, June 17, 2026).

The most inflated stage is not the most dangerous one. Cancelling a grid request costs no one anything. DRAM that buyers have already paid for and stockpiled shows up in supplier revenue as if it were real demand, and it can replace new orders once the server CPU shortage eases in the second half of 2027.

Yesterday's post, [Part of the DRAM Shortage Is Inventory](/post/dram-shortage-part-inventory-buyers-stop-when-cpus-arrive-2026-10-30/), went deep on buyer memory inventory. This post widens the view to the stages before and after it: where the inflation sits across the AI supply chain, how large it is, and which part can turn into real losses.

<strong>Our view: by inflation, grid requests rank first. By dollars, cloud commitments are the largest. By real risk, buyer memory inventory ranks first. What separates them is not the inflation multiple but the cost of cancelling, how much is already paid, and whether the unwind coincides with new supply.</strong>

## The bullwhip takes a different form at each stage

The bullwhip effect is the way order swings grow as you move up a supply chain. Each stage reads the orders below it as demand and adds a safety margin. The classic study (Lee, Padmanabhan and Whang, 1997) names four causes: trusting demand signals at face value, inflating requests when supply is rationed, batching several years of volume into one contract, and buying ahead of price increases.

The AI chain adds two more. One is complement bottlenecks. A server needs GPUs, CPUs, memory, substrates and power, so when one is short, buyers stockpile the rest. The other is supplier financing. When suppliers fund customer purchases or repurchase unused capacity, demand appears beyond what buyers can pay for.

The table below shows what kind of inflation sits at each stage and what it costs to cancel.

| Stage | Kind of inflation | Representative figure | Cost to cancel |
|---|---|---|---|
| Grid connection requests | Duplicate filings across sites and utilities | ERCOT 2032 peak forecast at 4.3x the record | Almost none |
| Generation equipment | Reserving production slots | GE Vernova slot reservations of 58 GW | Low for reservations, deposits for orders |
| Cloud commitments | Contracting years of compute against future revenue | Microsoft and Oracle obligations above $600 billion each | High on paper, renegotiated in practice |
| GPUs (China) | Inflated requests under rationing | 6 million units ordered vs. an estimated 0.3 to 0.6 million delivered | Almost none |
| Memory | Stockpiling while waiting for complements, buying ahead of price rises | Dell purchase commitments up 67% in one quarter | Already paid |

The pattern is simple. The more inflated a stage is, the cheaper it usually is to cancel, and the stage that is expensive to unwind is memory.

![Inflation versus real risk by stage of the AI supply chain. Grid requests are the most inflated but low risk; buyer memory inventory is moderately inflated but the highest risk. Qualitative assessment.](/post-assets/ai-bullwhip-grid-cloud-memory-2026-10-31/bullwhip-stages.en.svg)

## Grid requests are the most inflated, and already being filtered

Bernstein views only 33 to 35 percent of the 456 GW U.S. data center power pipeline as credible (as reported in the press). The same project is filed with several sites and utilities. Roughly two-thirds of the pipeline is likely never to be built.

That inflation does not turn into losses. Filing costs almost nothing and creates no inventory. Regulators are filtering it too. Texas added fees for large-load applications, and PJM tightened large-load reviews, cutting its 2026 summer peak forecast by 1.6 percent and its 2028 forecast by 2.6 percent (Power Magazine, January 15, 2026).

It is not spilling into equipment either. GE Vernova converted 13 GW of gas turbine slot reservations into firm orders in the third quarter, against 8 GW of new reservations, and its reservation backlog fell from 63 GW to 58 GW. [GE Vernova Q3 earnings release](https://www.sec.gov/Archives/edgar/data/1996810/000199681026000162/gevpressrelease3q26.htm) Reservations are becoming orders backed by deposits.

So the numbers to watch at the power stage are gigawatts under construction and turbine shipments, not requested gigawatts. A headline about fewer requested gigawatts does not mean less equipment demand.

## Cloud commitments are the largest, and they unwind through renegotiation

Microsoft's remaining performance obligations are about $677 billion and Oracle's about $664 billion (as reported from company filings). In dollars, this is the largest layer of the AI chain. Adding them up counts the same end demand several times, because AI labs contract with clouds and clouds subcontract to neoclouds.

The issue here is timing, not volume. When shortages end, buyers tend to cut volumes or stretch terms rather than break contracts. There is a precedent. In February 2026, reports said OpenAI had reset its compute spending target through 2030 from about $1.4 trillion to about $600 billion (secondary source). Today all running capacity is in use and GPU rental prices are rising, so any adjustment in this layer is likely to arrive slowly over several years.

## Memory inventory is risky because it is already paid for

Memory sits in the middle on inflation. It scores worst on the other three variables.

First, it is already paid for. TrendForce said U.S. cloud providers' DRAM inventory rose in the second quarter of 2026 because server CPUs were short. [TrendForce, July 9](https://www.trendforce.com/presscenter/news/20260709-13140.html) DRAM sitting in a buyer's warehouse is a shipment and revenue for the supplier, so it looks like consumption in reported results.

Second, it replaces new orders as soon as the cause clears. Intel said substrate expansion will bring incremental server CPU supply in the second half of 2027. When CPUs arrive, waiting DRAM goes into servers and new orders shrink by that amount.

Third, the timing overlaps with new supply. Memory makers' 2028 wafer capacity is expected to grow 15 to 17 percent (industry estimates). Our estimate of the buffer's size and the 2021 precedent are in [yesterday's post](/post/dram-shortage-part-inventory-buyers-stop-when-cpus-arrive-2026-10-30/).

## Re-ranking risk on four variables

The table below shows why the inflation multiple and real risk diverge.

| Variable | Grid requests | Cloud commitments | Memory inventory |
|---|---|---|---|
| Inflation multiple | Largest (about two-thirds not credible) | Medium (double counting) | Medium (size unknown) |
| Cost to cancel | Almost none | High, renegotiated in practice | Already paid |
| In reported results | No | Partly (only used capacity is revenue) | Yes, as supplier revenue |
| Unwind overlaps new supply | Weakly | Spread over years | 2H27 CPU supply meets 2028 memory supply growth |

The inflation multiple is the most visible number, but it does not set the risk. Losses come where money is already paid, results already reflect it, and it unwinds all at once as supply grows.

## What would prove this wrong

- Memory risk shrinks if buyer DRAM inventory falls as CPU supply rises in the first half of 2027, and DRAM spot prices stay above contract prices. Then today's inventory was assembly delay, not over-ordering.
- Cloud commitments become riskier if AI lab revenue growth drops below 10 percent a quarter, or cloud contracts disclose volume cuts or term extensions.
- The power stage becomes riskier if new turbine reservations exceed conversions for two straight quarters, with cancellations or delays disclosed.

## What to watch next

| When | Item | How to read it |
|---|---|---|
| Mid-November | Nvidia October quarter | Supply commitments growing faster than revenue signal a supply-side bullwhip |
| Late November | Dell Q3 10-Q | Whether purchase commitments and raw material inventory outgrow revenue |
| November to December | PJM 2027 load forecast | Whether large-load adjustments shrink after duplicate screening |
| Mid-December | Micron November quarter | Whether supplier inventory rebounds alongside comments on customer inventory |
| Late January 2027 | GE Vernova Q4 | Whether conversions still exceed new reservations |

## Limits

We could not measure the size of memory inventory. Cloud providers do not disclose DRAM weeks of inventory. ERCOT, PJM and Bernstein figures were confirmed through press reports, not original documents. The OpenAI spending target is from a February 2026 report and the latest value is unconfirmed. The risk ratings in the tables are our qualitative judgment.

<strong>Which stage of the AI supply chain do you trust least? If a number would change your mind, tell us in the comments.</strong>

## Key sources

- [GE Vernova Q3 earnings release, 8-K](https://www.sec.gov/Archives/edgar/data/1996810/000199681026000162/gevpressrelease3q26.htm)
- [Texas Tribune, ERCOT large loads, June 17, 2026](https://www.texastribune.org/2026/06/17/texas-ercot-data-center-energy-grid/)
- [Power Magazine, PJM 2026 load forecast, January 15, 2026](https://www.powermag.com/pjm-dials-back-near-term-load-outlook-but-maintains-steep-long-term-growth-trajectory/)
- [TrendForce, U.S. cloud DRAM inventory, July 9, 2026](https://www.trendforce.com/presscenter/news/20260709-13140.html)
- [Report on OpenAI compute spending target (secondary)](https://finance.yahoo.com/news/openai-sees-compute-spend-around-223950561.html)
- [KII, Part of the DRAM Shortage Is Inventory, October 30, 2026](/post/dram-shortage-part-inventory-buyers-stop-when-cpus-arrive-2026-10-30/)

*This analysis is based on public information. Not investment advice.*
