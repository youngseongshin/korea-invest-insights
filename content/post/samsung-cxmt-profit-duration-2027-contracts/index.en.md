---
title: "CXMT 4F²: Bypassing EUV Does Not Remove Yield and Good-Die Cost Challenges"
date: 2026-10-14T06:00:00+09:00
lastmod: 2026-10-14T06:30:26+09:00
categories: ["company-deep-dive", "semiconductors"]
tags: ["CXMT", "4F2", "DRAM", "Vertical Transistors", "Hybrid Bonding", "Samsung Electronics", "SK hynix"]
series: ["Korea Semiconductor Watch"]
slug: "samsung-cxmt-profit-duration-2027-contracts"
description: "This article breaks down CXMT's 4F² approach by cell area, vertical devices, wafer bonding, and good-bit cost. It compares the basis for G5 productivity claims, the research stages at Samsung and SK hynix, and the evidence needed to verify server reliability and the year-end product."
draft: false
---

For CXMT's 4F², the number to watch beyond cell area is total cost per good bit. Higher storage density changes its economic competition with Samsung Electronics and SK hynix only if it can repeatedly ship qualified output that meets server requirements for speed, power, and reliability.

On October 10, CXMT said it plans to unveil a server DDR5 RDIMM based on a 4F² structure by year-end. Evidence remains insufficient on speed, capacity, yield, repeat shipments, and customer qualification. Comparing that unveiling target with another company's production target cannot establish a two-year lead.

Changing the cell structure can create a path to the same storage density with a wider feature size. That matters to China because it could partly offset restrictions on access to EUV lithography equipment. <strong>The test is whether area gains translate into yield and cost gains.</strong>

## Reducing lithography constraints does not remove manufacturing challenges

- Moving from 6F² to 4F² reduces cell area by 33.3% and raises cell-array density by 50% at the same F. It does not improve good-die output or cost for the finished chip by the same percentages.
- G5 mass production is progress in a current product line. 4F² DDR5 is a separate announcement. G5's 11.95nm active-area half-pitch cannot be used as the actual F of a 4F² cell or as the same metric as Samsung's 1b or 1c nodes.
- Samsung's ISSCC 16Gb test chip, CXMT's IEDM device and array research, and SK hynix's roadmap are each substantive. Research operation, product unveiling, customer qualification, and economically viable mass production are different stages.
- 4F² does not replace HBM. Higher shipments of conventional DRAM can change customer choice and pricing power before CXMT catches up with HBM4.

The reference date for technology and market data is October 13, 2026. CXMT's listed entity is ChangXin Technology (688825.SH), listed on July 27. The article distinguishes official research, company announcements, reported news, inference, and unknowns. Yield and cost examples are illustrative assumptions.

## 4F², VCT, IGZO, and bonding are not interchangeable terms

A DRAM cell consists of a capacitor that stores charge and a transistor that controls access to it. A wordline carries the signal that opens the cell, while a bitline provides the path for reading and writing data. Shrinking the cell still requires managing stored charge, read signals, leakage, and interference.

Bundling technologies from different levels under one name can distort the competitive picture.

| Term | What it changes | What the term alone does not tell us |
|---|---|---|
| 6F² or 4F² | Planar area occupied by one cell | Finished-chip density, cost, or yield |
| VCT, VG, VSG | Arrangement of the vertical channel and gate | Channel material or actual electrical behavior |
| Oxide channel such as IGZO | Material through which current flows | Whether every supplier uses the same material |
| COP, or cell-on-peripheral | Placement of cells and control circuits | Bonding method or process cost |
| Wafer hybrid bonding | Connection between dielectric and metal on two wafers | Bond yield, throughput, or total cost |
| 3D DRAM | Stacking the cell array in multiple layers | Whether it is the same product as HBM |
| HBM | Stacking finished DRAM die and connecting them to an accelerator | A cost advantage in making a single cell |

CXMT's 2023 IEDM research used a junctionless GAA vertical device with a silicon pillar. Kioxia's OCTRAM research uses an InGaZnO oxide channel. Samsung's public abstract describes VCT, COP, and hybrid bonding, but does not specify the channel material. Comparisons such as “all 4F² uses IGZO” or “the same 4F² means the same process” do not hold. [CXMT IEDM paper](https://mys.mapyourshow.com/mys_shared/iedm23/handouts/6-2_Mon_16771.pdf), [Kioxia OCTRAM](https://www.kioxia.com/en-jp/rd/technology/topics/topics-77.html), [public abstract of Samsung's joint research](https://pure.skku.edu/en/publications/a-vertical-cell-transistor-based-4fsup2sup-dram-with-cell-on-peri/)

## The cell-area gain is real. The finished-chip gain is smaller.

F is the minimum dimension used in a geometric comparison. It is not always the same as a process-generation label such as “10a” or a half-pitch in a specific area. At the same F, the calculations are:

| Comparison | Calculation | Result |
|---|---|---:|
| Reduction in cell area | 1 − 4 ÷ 6 | 33.3% |
| Increase in cells per equal area | 6 ÷ 4 − 1 | 50.0% |
| F ratio for equal cell area | F₄ ÷ F₆ = √(6 ÷ 4) | 1.2247 |

The area of a 4F² cell with F = 15nm is 4 × 15² = 900nm². It is roughly equal to a 6F² cell with F ≈ 12.25nm. This illustrates how a wider feature size can yield the same cell area. It does not mean that CXMT's actual product has been measured at F = 15nm.

Structural changes can therefore partly offset lithography constraints. But they do not establish that CXMT's first product is equivalent to or ahead of a specific Samsung 1b or 1c product. Compare actual cell area and full-chip Gb/mm², peripheral-circuit area, speed, power, and yield on the same basis.

A finished chip also contains peripheral circuits. Under the hypothetical assumptions that the cells occupy 65% of the chip and the peripheral area remains unchanged, the new chip area is 0.35 + 0.65 × 4 ÷ 6 = 0.7833. The theoretical output increase is 1 ÷ 0.7833 − 1 = about 27.7%.

The 65% is not an estimate of the cell share at Samsung or CXMT, and the calculation omits wafer-edge losses. It shows why a 50% increase in cell density cannot be transferred directly into a 50% increase in finished-chip output.

## Do not conflate G5's two different “50% increases”

In its official announcement on September 20, CXMT described G5 mass production and SAQP. SAQP means self-aligned quadruple patterning. It subdivides patterns across multiple process steps to increase density; it is different from simply exposing the same pattern four times.

The company's figures use different comparison bases.

| Company-reported item | Actual comparison basis | What it should not be expanded to mean |
|---|---|---|
| 11.95nm active-area half-pitch | A specific pattern dimension in the memory array | Line width of every layer, F for 4F², or equivalence to a competitor's node |
| At least +50% DPW versus prior platform | Die per wafer normalized to an 8Gb baseline | +50% in good-die yield, sales, or cost improvement |
| +50% per-die capacity for 24Gb LPDDR5X | Per-die capacity versus equivalent prior-generation products | +50% total factory bit shipments |
| Mass production of two 24Gb LPDDR5X products | Production stage claimed by the company | Completion of scale sales or repeat orders |

Source: [CXMT official G5 announcement and notes](https://www.cxmt.com/en/news/info_22.html). This verifies what the company announced, not independent teardown or yield validation.

A reprint of company announcement 2026-005 says G5 products had not yet achieved sales at scale, and that yield stabilization and new-customer validation and qualification would take time. This is the warning in the filing as of September. [Reprinted G5 filing](https://stock.stockstar.com/notice/SN2026092200000007.shtml)

G5 mass production and the absence of scale sales are not contradictory. Putting products on a process line differs from repeatedly supplying enough good die for customers to buy. G5 is a near-term supply development; year-end 4F² is a separate structural transition still to be verified.

## Vertical transistors shrink cells but make device control harder

A vertical channel makes the current path stand upright to reduce its planar footprint. A gate surrounding the channel can help control current and leakage. But variations in the etched pillar's width, height, verticality, and surface condition can change device behavior.

The process and electrical characteristics below need to be checked together before a design is a product.

| Manufacturing challenge | Evidence to check | Why it matters to chips and servers |
|---|---|---|
| Pillar etch and dimension distribution | Cross-sections, width, height, verticality, and within-wafer distribution | Differences in cell current and threshold voltage |
| Gate and dielectric formation | Film thickness, uniformity, defects, and materials | Leakage, control, and long-term reliability |
| Bitline resistance and parasitics | Resistance, junctions, and parasitic capacitance | Read signal, speed, and power |
| Floating body and field-induced leakage | Electrical behavior by bias and temperature | Charge retention and errors |
| Capacitor and sensing circuit | Charge, read margin, and distribution | Whether data can be distinguished in a smaller cell |

This is a list of things to verify, not a qualification verdict for a public product. The issues vary with materials and implementation. A paper on another supplier's device is not a measurement of CXMT's product.

CXMT's IEDM 2023 paper reports that wordline-to-wordline leakage fell from 200µA to 2.5pA in a specific test structure. The ratio is 200 × 10⁻⁶ ÷ (2.5 × 10⁻¹²) = 80 million. This is a large improvement in the experiment. The measured leakage path differs from data retention, error rate, and production yield for a complete DDR5 module.

Distinguish the existence of research data from validation of a server product's 2026 economics. The 2023 paper alone cannot establish that the year-end product has the same channel material, structure, or performance.

## Wafer bonding can solve circuit placement but adds cost and defect risks

Building the cells and peripheral circuits on separate wafers can let each use different process conditions. Placing the peripheral circuits beneath the cell array can also reduce planar area. COP and wafer-to-wafer hybrid copper bonding in Samsung's ISSCC research are one such implementation.

However, 4F² defines cell area. Its definition does not require bonding two wafers. CXMT's 2023 4F² array paper and Samsung's COP-and-bonding test chip cannot be treated as using the same process flow.

For a bonded implementation, the cell wafer, peripheral-circuit wafer, and bonding process must be assessed together.

| Additional item to check | Yield and cost question |
|---|---|
| Surface planarity and contamination or particles | Interface defects and connection failure |
| Copper pads and dielectric bonding | Contact resistance, opens, and long-term stability |
| Alignment of the two wafers and warpage | Connection errors and within-wafer yield distribution |
| Annealing and material combinations | Bond stability and preservation of cell and circuit properties |
| Good-die locations and inspection on both wafers | Which defects at each stage become finished-product losses |
| Throughput, equipment, and inspection costs | Whether the area gain exceeds the added process cost |

Assume for illustration that cell-wafer yield is 95%, peripheral-wafer yield is 95%, and bonding yield is 98%, all independent. The combined yield is 0.95 × 0.95 × 0.98 = 88.445%. This is not an actual yield estimate. Defect location and correlation, inspection, and rework can change the result. The example shows why a high yield at one stage does not establish final yield.

HBM die stacking and wafer bonding between cells and peripheral circuits are not the same market. Their connection requirements, inspection, thermal management, and process integration differ. The label “bonding” alone does not confirm orders for a specific equipment supplier or CXMT's access to such equipment.

## The cost denominator is saleable good bits, not designed bits

<strong>Total cost per good bit = total cost including wafers, process steps, bonding, inspection, and depreciation ÷ saleable good bits.</strong> Looking only at a design-density improvement misses yield and customer-qualification rates in the denominator.

Assume total process cost increases 20% and pre-yield bit output increases 30%.

| Relative yield versus the baseline | Cost ratio | Result |
|---|---|---:|
| 95% | 1.20 ÷ (1.30 × 0.95) | Cost per good bit down about 2.8% |
| 85% | 1.20 ÷ (1.30 × 0.85) | Cost per good bit up about 8.6% |

Relative yield of 95% is not absolute yield of 95%. Even the same density benefit can produce lower or higher costs depending on process integration and yield. This table does not estimate actual Samsung or CXMT costs.

Samsung's ISSCC abstract reports more than a 20% increase in total die per wafer under the same design rules. This finished-chip metric uses a different comparison basis from the theoretical 50% cell-array density increase. Supply competitiveness requires area, yield, performance, and total cost for the same product.

## Compare Samsung and SK hynix at the same announcement stage

| Company and source | What was disclosed | What it does not establish |
|---|---|---|
| CXMT, IEDM 2023 | Junctionless GAA vertical device and 4F² array research | Production yield or customer qualification for 2026 DDR5 modules |
| CXMT, October 2026 remarks | Year-end server DDR5 RDIMM unveiling target combining 4F², vertical devices, and bonding | Product specifications, economics, or repeat shipments |
| Samsung co-research, ISSCC 2026 | Read/write operation of a 10nm-class 16Gb VCT/COP test chip with wafer-to-wafer copper bonding | Mass-production yield or a commercial shipment date |
| SK hynix, VLSI 2025 | Roadmap for 4F² Vertical Gate and 3D DRAM | Confirmed commercial production dates for each generation |
| Kioxia, OCTRAM research | 4F² research using an InGaZnO oxide channel | That CXMT uses the same materials or implementation |

Sources: the research papers and the [official ISSCC program, session 15.10](https://submissions.mirasmart.com/ISSCC2026/PDF/ISSCC2026AdvanceProgram.pdf), [SK hynix official VLSI announcement](https://news.skhynix.com/en/?p=1286), and [Yicai coverage of CXMT's conference remarks](https://www.yicai.com/news/103388707.html).

Samsung's 2028 production date is a target reported by some media. It should be distinguished from a confirmed company mass-production filing. Calculating a two-year lead by comparing that target with CXMT's year-end unveiling target mixes stages. [Report on the 2028 target](https://www.trendforce.com/news/2026/04/24/news-samsung-reportedly-produces-sub-10nm-10a-dram-working-die-using-4f-square-and-vct-targets-2028-production/)

The lack of public proof is not proof of failure. The accurate status is that CXMT's product unveiling, yield, and customer qualification remain to be seen. Samsung and SK hynix cannot turn research announcements into proof of mass-production economics either.

## Mobile supply, server DRAM, and HBM follow different qualification paths

| Product and customer | Stage in public evidence | Interpretation |
|---|---|---|
| G5 24Gb LPDDR5X | Company announcement of product mass production | Current process progress. Scale sales and good-bit cost remain separate |
| LPDDR6 and Xiaomi foldable phone | Reuters reports the supply arrangement confirmed by both companies | Progress with a mobile customer. Customer-level volume remains unknown |
| Tencent server DRAM | Long-term supply agreement reported by anonymous sources | Term, product scope, and actual delivery unverified. Not 4F² qualification evidence |
| 4F² DDR5 RDIMM | Year-end unveiling target | Server-platform approval and repeat deliveries still needed |
| HBM3E and Chinese accelerators | Reports of test production and customer evaluation | Not direct evidence of customer, stacking yield, or commercial shipments |

Sources: [Reuters report on LPDDR6 supply to Xiaomi, carried by MarketScreener](https://ca.marketscreener.com/news/china-s-cxmt-to-supply-memory-chip-for-xiaomi-s-upcoming-folding-phone-ce7858dcd981f12d), and [Reuters report on the Tencent deal, carried by Investing.com](https://www.investing.com/news/stock-market-news/exclusivechinas-cxmt-wins-3-billion-memory-supply-deal-with-tencent-sources-say-4764321). Direct access to the Reuters pages was limited, so these Reuters syndication copies were checked.

Do not combine other customer names, strategic investors, and listings of commercial modules with mass-production qualification. Public sources do not establish product- and customer-level revenue or CXMT's Top 1/Top 5 customer shares.

HBM requires more than smaller cells. It involves stacking die, TSV connections, packaging yield, thermal and warpage control, base-die integration, and accelerator-platform qualification. Progress in 4F² DDR5 does not imply immediate HBM4 substitution. Conversely, CXMT does not need to replace HBM4 to increase competition in conventional DRAM.

The estimate that the HBM gap is “three to five years” depends on which products, performance levels, and yields are compared. Reports that a product is under evaluation do not automatically shorten the gap to two or three years. Actual deployment in a customer product and repeat shipments are more direct signals.

## Judge the year-end product by server reliability and repeat shipments, not by a die photo

<strong>The first question about a year-end reveal is structure; the second is performance and reliability; the third is economics.</strong> Verifying one does not pass the others.

| What to check in the reveal | What it can establish | Evidence needed next |
|---|---|---|
| Cell cross-section, gate, channel, and cell area | Actual 4F² and vertical-device implementation | Full-chip density and electrical characteristics |
| Bonding interface and peripheral-circuit placement | A specific integration architecture | Bond yield, throughput, and cost |
| Die capacity and Gb/mm² | Finished-chip density | Total cost per good bit |
| Speed, voltage, and power | Performance under the stated conditions | Distribution across temperatures, loads, and wafers |
| Data retention, refresh, and error distribution | Reliability under the stated conditions | Specifications that match density and temperature, and platform validation |
| Intel, AMD, or other platform verification and customer approval | Qualification for that product and platform | Actual orders and repeat deliveries |
| Good-die shipments and costs over multiple quarters | Commercial supply and economics | Persistence of price and share effects |

Product density, temperature, and operating conditions differ, so one universal threshold should not be used as a pass line. Reverse engineering helps establish structure and area but does not directly establish manufacturing yield or long-term reliability.

The type of disclosure also limits the conclusion.

| Disclosure type | Conclusion it can support |
|---|---|
| Structure drawings and a date | Development direction and intent; not a confirmed production schedule |
| Specifications and an operating sample | Technical progress; customer qualification and economics remain unknown |
| Platform and customer approval | Stronger evidence that a specific product can be supplied |
| Repeat shipments with yield and cost | Evidence to incorporate into Samsung's and SK hynix's supply and margin models |

Do not automatically move the date to 2028 because an event reveals no specifications, or call it mass production because specifications were disclosed. A schedule estimate requires progress in manufacturing and customer approval.

## Put good-bit shipments into the capacity model

Monthly capacity of about 300,000 wafers and future paths toward 500,000–600,000 wafers appear in reports and estimates. These mix current capacity, targets, and forecasts. [SemiAnalysis' CXMT analysis](https://newsletter.semianalysis.com/p/chinas-cxmt-is-set-to-challenge-dram) is an analyst model, not a physical fab audit confirming current good-die output.

Supply should be separated into <strong>installed capacity × actual utilization × designed bits per wafer × front- and back-end yield × customer-qualified share</strong>. Doubling monthly wafer starts is not the same as doubling saleable server DRAM bits. Bit shipments can also rise through node migration and better yield.

TrendForce's reported second-quarter CXMT DRAM revenue share is 9.5%. It is not bit share or wafer share. Before averaging it with estimates from other firms, align the product, period, and revenue basis. [TrendForce report on CXMT's technology and market position](https://www.trendforce.com/news/2026/10/12/news-cxmt-accelerates-4f%C2%B2-dram-push-eyes-year-end-server-ddr5-rdimm-launch/)

For illustration, set initial non-HBM DRAM supply and demand at 100 each, CXMT's hypothetical bit share at 10%, and other suppliers' supply growth at 15%. The 10% assumption is not converted from revenue share.

| Assumed CXMT bit-supply growth | Total supply growth | Demand +15% | Demand +20% | Demand +25% |
|---|---:|---:|---:|---:|
| +30% | +16.5% | +1.3% | −2.9% | −6.8% |
| +50% | +18.5% | +3.0% | −1.3% | −5.2% |
| +70% | +20.5% | +4.8% | +0.4% | −3.6% |

The supply-demand gap is supply ÷ demand − 1. A positive value means supply is in surplus; a negative value means a shortage. Supply in the middle row is 90 × 1.15 + 10 × 1.50 = 118.5. If demand grows 20%, the market is about 1.3% short; at 15% growth, supply exceeds demand by about 3.0%. The same Chinese capacity increase has different effects depending on demand and the starting shortage.

The share of production converted to a new process also matters. If a supplier with a hypothetical 10% global bit share applies the process to 20% of output and raises good-die production there by 20%, the incremental effect on global supply is 0.4%. Do not add the process effect again if it is already included in total bit growth.

These calculations are not forecasts or price-change estimates. They assume an initially balanced market and omit differences among products. Counting Chinese import substitution both as a decline in global demand and an increase in global supply would double-count the same event.

## Policy applies to the whole process and customer markets, not only lithography

Even if structural changes ease part of the lithography burden, constraints remain in etching, deposition, bonding, inspection, and metrology. The process challenge is being redistributed, not replaced entirely by a shift from EUV to bonding. Claims that “bonding, ALD, and metrology are all uncontrolled” should not be accepted without review of the specific equipment, technology, and transaction.

BIS's December 2024 action covers manufacturing equipment, software, and HBM. Raising density without EUV does not establish that the controls have expired. [BIS official announcement](https://media.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military)

The policy lists also refer to different regimes. The Entity List's export-license framework, the DoD 1260H list, and procurement limits under NDAA 5949 and FAR should not be collapsed into a blanket ban on private-sector purchases. The February 17 proposed FAR rule discusses the December 23, 2027 statutory effective date and federal procurement. It is not a blanket restriction on all U.S. and allied private-cloud purchases. [Federal Register proposed rule](https://www.federalregister.gov/documents/2026/02/17/2026-03065/federal-acquisition-regulation-prohibition-on-certain-semiconductor-products-and-services)

Reports that additions to a policy list are under review or on hold are different from a published designation and its implementation. This article does not make a legal determination of the current status of individual designations. Technical capability, equipment access, and access to customer markets are separate risk factors.

## The nearer risk for Samsung and SK hynix is substitution in existing products

CXMT does not need to catch up with the leaders in HBM4 or the highest-end server DRAM before competition begins. If Chinese customers replace some imported products with qualified domestic parts, incumbent suppliers can lose sales channels and face different contract terms.

Policy support and Chinese customer testing and purchasing opportunities can help CXMT catch up. But there is not enough public evidence to conclude that technical moats have disappeared or that the state will absorb all losses so CXMT never cuts production. This asymmetric supply response should be considered as a downside scenario.

The funding is real. An August 29 filing reports total proceeds of about RMB 66.607 billion after the greenshoe exercise and net proceeds of about RMB 66.310 billion. These are distinct from the initial July plan of RMB 57.9 billion. Funding does not guarantee equipment installation, yield, or qualification schedules. [IPO greenshoe implementation results](https://static.cninfo.com.cn/finalpage/2026-08-29/1225529556.PDF)

CXMT's first-half revenue of RMB 150.310 billion and net profit attributable to shareholders of RMB 77.605 billion are figures reported by the financial press. Direct review of the full half-year filing and notes remains incomplete, so these are not inputs to a confirmed cost model. The figures do not establish Samsung-equivalent good-die costs. Price, volume, product mix, and subsidies would need to be separated. [CXMT financial report](https://www.nbd.com.cn/articles/2026-08-28/4564392.html)

Samsung's preliminary third-quarter operating profit of KRW 107.4 trillion shows the strength of the current boom. It does not prove how long earnings will last. Check shipments of existing products and premium products, along with minimum-purchase obligations, price floors, and renegotiation terms in future contracts. [Samsung preliminary results](https://news.samsungsemiconductor.com/global/samsung-electronics-announces-earnings-guidance-for-third-quarter-2026/)

Customer approval and repeat shipments of HBM4E, server DDR5, SOCAMM2, and enterprise SSDs support Samsung's defenses. Internal memory and foundry sourcing does not automatically guarantee lower cost, and SK hynix's external sourcing is not inherently inferior. Finished-product performance, cost, and delivery are the standards.

AI usage can keep growing while installations are delayed or customers reduce inventory, slowing order growth. If good-bit supply from China and incumbent suppliers rises at the same time, prices may normalize faster. Track technology supply paths and actual purchase demand together.

## Signals that could change the timeline are qualification, yield, and shipments—not announcements

| Event | Evidence to check first | Scope of the conclusion |
|---|---|---|
| Year-end 4F² product reveal | Cross-section, capacity, density, speed, power, and refresh | Whether the work has moved from research direction to an operating product |
| 4F² customer approval and repeat shipments | Platform, customer, and product-level approval and volumes | Commercial supply capability and timing |
| G5 scale sales | Good-die shipments by product, yield, and repeat orders | Near-term import substitution in conventional DRAM |
| HBM3E deployment at customers | Customer products, stacking yield, and repeat deliveries | HBM progress separate from conventional DRAM |
| Changes in process/equipment or market access | Official rules, designation, license scope, and effective date | Recalculate capacity, technology, and sales channels separately |
| Samsung and SK hynix 2027 contracts and product transition | Minimum purchase and price terms, cancellation rights, premium-product approvals and shipments | Whether high earnings can be defended |

Public evidence does not establish CXMT's mass-production year, the exact number of years in its HBM gap, or its 2030 bit share. Price-drop probabilities and stock-price impacts from models whose source code is unavailable are not adopted. Running a model 3,000 times does not make its input assumptions realistic.

The assessment of technology news should remain open in both directions. If CXMT's cost, yield, and qualification improve faster than expected, raise the competitive-risk assessment. If it announces a structure without demonstrating good-die costs and customer qualification, push out the schedule and reduce the estimated impact.

<strong>The path CXMT is pursuing is a path to the required density without EUV. The destination is not the smallest cell, but good die that customers buy repeatedly.</strong> Reassess the timeline for pressure on Samsung's and SK hynix's high earnings at that point.

## Evidence scope

Company announcements establish what the company claims; conference papers establish results for the reported test structures. No single source validates reverse engineering, process yield, long-term server reliability, and customer shipments. This article does not merge the stages of G5, LPDDR6, 4F², and HBM. Supply, yield, and cost calculations are illustrative assumptions, not forecasts or investment probabilities for these companies.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
