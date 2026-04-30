---
title: "OpenEdges Technology: Samsung 4/5/8nm LPDDR6 and LPDDR5X Memory IP Upside"
slug: semiscope-openedges-samsung-lpddr6-ip-option-2026-04-30
aliases: ["/en/post/semiscope-openedges-samsung-lpddr6-ip-option-2026-04-30/"]
date: 2026-04-30T12:00:00+09:00
description: "OpenEdges Technology (394280 KQ) offers a focused way to analyze Samsung 4/5/8nm LPDDR5X/LPDDR6 memory-subsystem IP demand. This SemiScope follow-up reviews the product moat, subsidiary structure, dilution, valuation and the milestones needed before scaling exposure."
categories: ["Korea Tech Supply Chain", "Semiconductor IP"]
tags: ["OpenEdges Technology", "394280", "SemiScope", "Samsung Foundry", "LPDDR6", "LPDDR5X", "DDR PHY", "Memory Controller", "NoC", "OpenEdges Square", "Korea Fabless", "Semiconductor IP"]
series: ["semiscope-2026"]
---

> **SemiScope follow-up.** The first OpenEdges note framed the company as Korea's rare memory-subsystem IP platform with a long royalty J-curve. This second piece narrows the investable question: OpenEdges Technology is not primarily an "NPU stock." It is a Samsung 4/5/8nm LPDDR5X/LPDDR6 memory-subsystem IP option, and the stock only deserves a larger position when license wins, revenue recognition, royalty mix and cost control start to confirm that option.

---

## Related Reading

- [SemiScope: OpenEdges Technology - Korea's Memory Subsystem IP Platform With a Royalty J-Curve Option](/post/semiscope-openedges-technology-ip-platform-2026-04-25/)
- [SemiScope: Three Korean Memory ATE & IP Names Re-Ranked - Why Exicon is the 2026 J-Curve Trade, Not the Afterthought](/post/semiscope-neosem-exicon-openedge-rerank-2026-04-25/)

---

## TL;DR

1. **OpenEdges is better understood as a memory-subsystem IP company than as an NPU company.** The core investment lens is LPDDR5X/LPDDR6 PHY, memory controller and NoC bundled for AI ASIC, edge AI, automotive and other data-intensive chips.
2. **Samsung Foundry 4/5/8nm is the practical battleground.** The stock is not a bet that OpenEdges defeats Synopsys or Cadence at the global 2/3nm frontier. It is a bet that Samsung's mid-to-advanced mass-market nodes need credible, local, process-aware LPDDR IP.
3. **The value chain is still early: porting, license, tape-out, silicon proof, production, royalty.** OpenEdges has moved beyond pure R&D, but it is not yet a mature royalty platform.
4. **TSS and the Japan unit strengthen the technology base. OpenEdges Square is a higher-risk option.** TSS and Japan are 100% subsidiaries tied to DDR PHY and memory-controller depth. Square is more interesting but also more dilutive, because the parent owns roughly 65%.
5. **Valuation already prices in a lot.** Around KRW 530B market cap against roughly KRW 30.4B-31.8B of 2026F revenue implies about 16.7x-17.5x sales. This can work only if LPDDR6/5X wins, 2Q-3Q revenue ramp, cost discipline and royalty progress arrive.

**Bottom line:** OpenEdges remains a **Watchlist / Pilot Hold** candidate. A 0.3%-0.5% pilot position can be justified for investors who want exposure to Korea's semiconductor IP layer. Scaling above 1% should wait for repeated LPDDR6/5X wins, visible revenue ramp, lower fixed-cost burn and better visibility on OpenEdges Square.

---

## 1. What This Note Adds to the First SemiScope OpenEdges Piece

The first SemiScope note made the broad case: OpenEdges Technology (394280 KQ) is Korea's rare semiconductor IP platform, with memory controller, DDR PHY, NPU, NoC, UCIe and CXL-adjacent memory IP under one roof. That view still stands.

But the more useful follow-up is narrower.

The market often wants to label OpenEdges as an "AI semiconductor" or "NPU" stock. That is too loose. The company's most investable asset is not the NPU by itself. It is the memory path around AI compute:

`DRAM - DDR PHY - Memory Controller - NoC - NPU / CPU / Accelerator`

For an AI ASIC or edge inference chip, compute is not the only bottleneck. Data movement can be just as important. If the memory interface is slow, power-hungry or unstable, the chip's theoretical TOPS do not matter much. That is why LPDDR5X/LPDDR6 PHY and controller IP can become strategic.

The revised thesis is:

> OpenEdges is a call option on Samsung 4/5/8nm AI and edge ASIC customers needing proven LPDDR5X/LPDDR6 memory-subsystem IP.

This wording matters. It keeps the upside but removes the exaggeration. The company is not yet a global IP champion. It is not yet a high-quality earnings compounder. It is an R&D-heavy IP vendor with a credible chance to become the domestic memory-subsystem layer for a part of Samsung Foundry's customer base.

---

## 2. Correcting the Product Frame: NPU Is Not the Center

OpenEdges owns and develops several IP blocks:

| Product family | Function | Investment meaning |
|---|---|---|
| **DDR PHY** | Physical signal layer between SoC and DRAM | Highest technical barrier; node-specific hard IP; needs silicon proof |
| **DDR Memory Controller** | Controls memory access, scheduling and protocol behavior | Becomes more valuable when paired with PHY |
| **On-Chip Interconnect / NoC** | Moves data inside the SoC | More important as AI ASICs add more compute blocks |
| **NPU / ENLIGHT** | AI inference acceleration | Useful, but weaker as a standalone investment thesis |
| **UCIe / chiplet controller** | Die-to-die communication for chiplet systems | Long-term option as chiplet adoption broadens |
| **CXL-adjacent memory IP** | Memory controller and PHY blocks used by potential CXL controller-chip designers | Indirect CXL exposure, not equipment-like revenue visibility |

The strongest version of the company is not "we sell an NPU." It is "we reduce memory bottlenecks in AI chips by selling a bundled memory subsystem."

That is also where switching cost appears. A standalone soft IP block can often be swapped. A PHY plus controller plus NoC combination that has been integrated, verified and timed inside a chip is much harder to replace. The customer's tape-out schedule, verification plan, power budget and timing closure can all be affected.

This is why the stock should be separated from equipment names such as NeoSem and Exicon. Those companies can convert orders into revenue within roughly six to nine months. OpenEdges sells upstream design IP. Its payoff takes longer, but the royalty upside can be more durable if customer chips reach mass production.

---

## 3. The IP Value Chain: Do Not Confuse Porting With Royalties

The most important operating sequence is:

`Porting - license win - customer tape-out - silicon proof - production - royalty`

OpenEdges has progressed beyond "technology with no customer interest." Its 2026 IR material points to more than 30 customers, 71 cumulative license contracts, more than 20 saleable IP products and a workforce of about 170 people, including roughly 149 R&D staff. That is not a paper-company profile.

But it is equally important not to jump from "porting" to "royalty platform" too quickly.

| Stage | What it proves | What it does not yet prove |
|---|---|---|
| Porting | The IP can be adapted to a target process node | A paying customer has adopted it |
| License win | Customer has committed to use or evaluate the IP | The chip will tape out successfully |
| Tape-out | Customer design has moved to fabrication | The silicon will meet production requirements |
| Silicon proof | The IP works in real silicon | Customer will ship high volume |
| Production | The customer chip is commercial | Royalty scale still depends on unit volume |
| Royalty | The model has compounding economics | Sustainability depends on repeated design-ins |

The royalty mix is still small. Earlier OpenEdges materials and sell-side work point to royalty revenue at only a tiny share of recent sales. One 2026 forecast set royalty revenue around KRW 1.7B against KRW 30.4B of revenue, or about 5.6%.

That 5%-6% range is progress from the 1H25 level, but it is not yet the ARM-style curve investors ultimately want. For this stock to rerate into a true quality IP compounder, I would want to see royalty mix moving toward 20% of quarterly revenue and still rising.

---

## 4. Why Samsung 4/5/8nm Matters

The phrase "Samsung 4/5/8nm" should not be read as a vague Samsung ecosystem story. It is specific.

The incorrect shortcut is:

> OpenEdges has pre-ported LPDDR6 across Samsung 4-8nm.

The better version is:

> OpenEdges is expanding coverage around Samsung 4nm LPDDR6 and Samsung 4/5/8nm high-speed LPDDR5X, targeting AI, edge, automotive and other ASIC customers that need better memory interfaces on Samsung Foundry mass-market nodes.

According to the 2026 IR roadmap cited in the source material, OpenEdges already provides Samsung 5nm LPDDR5X/LPDDR5/LPDDR4X/LPDDR4 coverage. Samsung 8nm LPDDR5X was shown as a 1H26 development item, while Samsung 4nm LPDDR5X 10.7Gbps and LPDDR6 14.4Gbps were shown as 2H26 development items.

This is the right battleground for OpenEdges.

The 2/3nm frontier is where global giants dominate. Synopsys, Cadence, Arm, Rambus and other interface-IP leaders have deeper field support, broader foundry relationships and more advanced-node references. It is not realistic to underwrite OpenEdges as a near-term global winner at that layer.

The more realistic opportunity is the mid-to-advanced mass-market:

- on-device AI;
- automotive AI chips;
- robot and industrial AI controllers;
- IoT and smart-home chips;
- security-camera and vision ASICs;
- defense and special-purpose chips;
- domestic AI accelerator projects;
- design-house-led turnkey ASIC programs.

These customers may not always need the most expensive 2/3nm process. They may care more about cost, power, memory bandwidth, local support, risk reduction and Samsung-process availability. That is where a domestic memory-subsystem IP vendor can matter.

The core question is:

> Does the pool of Samsung 8nm-and-below customers needing LPDDR5X or LPDDR6 grow enough to create repeated license wins for OpenEdges?

If yes, the stock has a clear path to a higher-quality narrative. If no, the company remains a technically interesting but financially strained IP vendor.

---

## 5. Moat Inside the Samsung Value Chain

Samsung Foundry's issue is not only process technology. It also needs a thicker ecosystem: IP, EDA, design houses, verification references and customer support. OpenEdges can help strengthen one layer of that stack.

| Samsung value-chain node | Samsung's need | OpenEdges role |
|---|---|---|
| Samsung Memory | LPDDR5X/LPDDR6 DRAM adoption | Indirect beneficiary of higher LPDDR adoption |
| Samsung Foundry | More 4/5/8nm customer wins | Provides process-aware memory-interface IP |
| SAFE / IP ecosystem | Lower customer design risk | Adds domestic PHY, controller and NoC options |
| Design houses | Turnkey ASIC packages | Can be inserted into repeat design flows |
| Fabless / ASIC customers | Faster tape-out with lower memory risk | Solves high-speed low-power memory bottlenecks |

The first moat layer is **DDR PHY porting**. PHY is not generic software. It is a hard IP block with analog and mixed-signal complexity. At 8.5-14.4Gbps speeds, signal integrity, jitter, noise, voltage/temperature variation, timing margin and training algorithms matter. A simulation-only IP block is not enough. Customers want silicon proof.

The second moat layer is **PHY + controller + NoC bundling**. AI ASIC customers do not simply need an interface pinout. They need a working data-movement system. If OpenEdges can sell the memory path as a bundle, it creates a higher switching cost than any single block can create alone.

The third moat layer is **design-house channel leverage**. If a design house repeatedly uses OpenEdges IP inside Samsung-turnkey projects, OpenEdges does not need to sell every customer one by one. The IP can become part of a repeatable package.

The moat is not absolute. It is local and process-specific. But local, process-specific moats can still create attractive public-market returns when the revenue base is small.

---

## 6. Subsidiaries: What Belongs to Shareholders?

The subsidiary structure matters because OpenEdges is not only one listed entity with one clean product line. The 2026 IR material breaks the group into the parent and key subsidiaries.

| Entity | Parent stake | Main role | Investment read |
|---|---:|---|---|
| **OpenEdges Technology parent** | - | IP R&D, sales and integrated platform strategy | Core listed business |
| **The Six Semiconductor (TSS)** | 100% | DDR PHY IP R&D | Strengthens the key technical moat |
| **OpenEdges Technology Japan** | 100% | Memory Controller IP R&D and Japan-facing capability | Reinforces controller depth and regional talent access |
| **OpenEdges Square** | roughly 65% | Online IP sales platform, CC NoC and future platform options | Higher-risk option; upside is not fully owned by the parent |

TSS should be viewed as a moat asset, not dilution. DDR PHY is the hardest part of the stack. If TSS deepens high-speed PHY capability, the economics accrue to the parent because it is wholly owned.

The Japan unit is similar. Memory-controller IP is less analog-heavy than PHY, but it sits close to customer architecture and product requirements. Japan also has relevant semiconductor engineering depth and customer relationships. Again, because this unit is 100% owned, the issue is cost, not value leakage.

OpenEdges Square is different.

Square is not merely an engineering branch. It was launched around online IP sales platform ambitions and CC NoC development. CC NoC, or cache-coherent network-on-chip, can become valuable if multicore AI ASICs require more sophisticated internal data movement and cache-coherency behavior.

The option is interesting. The ownership is less clean. If the parent owns about 65.4% of Square, then an OpenEdges shareholder's look-through exposure to Square is only 65.4% of their parent-company stake.

Example:

`1.0% parent stake x 65.4% Square ownership = 0.654% look-through Square exposure`

That is not automatically bad. External capital can reduce the parent's cash burden and accelerate development. But it means Square's success does not accrue 100% to listed shareholders.

I would treat Square as a call option with two questions:

1. Can CC NoC become a real commercial product rather than a development story?
2. Can Square's cost and financing needs stay controlled enough that the option does not weaken the parent income statement?

---

## 7. Dilution and Funding: The 2026 CPS Issue

OpenEdges raised roughly KRW 20.0B in March 2026 through a third-party allotment of convertible preferred shares. The key figures in the source material are:

| Item | Figure |
|---|---:|
| New preferred shares | 1,145,278 |
| Existing common shares before issuance | 26,276,655 |
| Potential common-share increase | 1,145,278 |
| Stated share-count impact | 4.18% |
| Issue price | KRW 17,463 |
| Reference price | KRW 17,054 |
| Premium to reference price | 2.4% |
| Conversion period | Apr. 8, 2027 to Apr. 8, 2031 |
| Conversion-price floor | KRW 12,225 |

The dilution math is:

`1,145,278 / (26,276,655 + 1,145,278) = 4.18%`

This is real dilution. It should not be ignored. The softer points are that the issuance was at a premium to the reference price and the cash extends R&D runway.

The risk is refixing. If the share price falls and the conversion price adjusts down toward the floor, effective dilution can increase. For a company still funding R&D ahead of mature royalties, the cost of capital remains part of the thesis.

---

## 8. Valuation: The Stock Already Prices a Better Future

Using the source-market snapshot around Apr. 29, 2026, OpenEdges traded near KRW 20,150 with market capitalization around KRW 530.9B. Against 2026F revenue assumptions of roughly KRW 30.4B-31.8B, the sales multiple is high.

| Revenue base | Calculation | Implied PSR |
|---|---:|---:|
| 2026F revenue KRW 30.4B | KRW 530.9B / KRW 30.4B | **17.5x** |
| 2026F revenue KRW 31.8B | KRW 530.9B / KRW 31.8B | **16.7x** |

This is not a cheap cyclical small-cap. It is an expensive option on a better future business model.

The market is already underwriting several things:

- 2026 revenue moves into the KRW 30B+ range;
- the company approaches breakeven in 2H26 or 2027;
- LPDDR6/5X wins become repeatable;
- Samsung 4/5/8nm customer activity improves;
- OpenEdges Square contributes option value rather than only cost;
- royalty revenue gradually becomes visible.

That is a demanding setup. The right conclusion is not "avoid." The right conclusion is "do not scale until the company proves enough of the roadmap."

---

## 9. Investment Framework

### Idea 1 - Samsung 4/5/8nm LPDDR memory-subsystem IP

| Item | View |
|---|---|
| Core logic | Samsung Foundry 4/5/8nm customers need high-speed LPDDR5X/LPDDR6 PHY and controller IP |
| Price lever | Advanced LPDDR IP can raise ASP |
| Volume lever | Multiple new licenses or one to two large lighthouse wins |
| Cost lever | R&D fixed-cost growth must slow |
| Choke point | Process-specific PHY porting and silicon proof |
| Market error | Treating OpenEdges as only an NPU stock |
| Bear case | Samsung customer pool does not expand enough |
| Confirmation | LPDDR6/5X repeat wins, Samsung 4nm tape-out or silicon proof |

### Idea 2 - TSS and DDR PHY as the real moat

| Item | View |
|---|---|
| Core logic | PHY is the hardest part of the memory-subsystem stack |
| Price lever | Proven high-speed PHY can command better economics |
| Volume lever | Coverage across Samsung and selected TSMC nodes |
| Cost lever | High-end R&D talent must be retained without uncontrolled burn |
| Choke point | Silicon-proven PHY at target nodes |
| Market error | Treating PHY like ordinary reusable digital IP |
| Bear case | Synopsys/Cadence respond aggressively in Samsung mass-market nodes |
| Confirmation | 4nm LPDDR6 and 8nm LPDDR5X validation and customer adoption |

### Idea 3 - OpenEdges Square and CC NoC

| Item | View |
|---|---|
| Core logic | Multicore AI ASICs may need cache-coherent NoC solutions |
| Price lever | CC NoC could be a higher-value IP layer |
| Volume lever | Adoption by AI ASIC and design-house customers |
| Cost lever | Platform development expense must be controlled |
| Choke point | Commercial CC NoC launch and early design wins |
| Market error | Seeing Square only as a cost center |
| Bear case | Revenue is delayed while cost burden grows |
| Confirmation | 2026 launch, first customer, clear economics for the parent |

---

## 10. Positioning: Watchlist / Pilot Hold

For now, I would put OpenEdges in the **Watchlist / Pilot Hold** bucket.

The stock is investable as a small exploratory position because the upside path is clear and the addressable strategic layer is real. But the current valuation is too high for blind scaling. The company needs to show that its technology roadmap can turn into repeatable contracts and recognized revenue.

### Conditions to increase exposure

I would consider moving from a 0.3%-0.5% pilot position toward 0.5%-0.7% if at least two of the following occur:

1. additional LPDDR6/5X license wins;
2. 2Q26 or 3Q26 quarterly revenue above KRW 7.0B;
3. quarterly fixed costs move closer to the KRW 7.0B-8.0B range;
4. Samsung 4nm LPDDR6 tape-out or silicon proof is disclosed;
5. design-house channel wins become more visible;
6. OpenEdges Square shows cost control and a credible CC NoC launch path;
7. the share price holds KRW 20,000 and recovers through the KRW 21,500-22,000 range on real news.

I would only consider a 1%+ position after three or more of those milestones are visible.

### Catalysts

| Catalyst | Timing | Meaning |
|---|---|---|
| K-On Device or similar policy-linked project | 2Q26-3Q26 | Public-sector AI semiconductor demand becomes more concrete |
| LPDDR6/5X license disclosure | 2026 | Confirms the KRW 30B+ revenue path |
| 2Q-3Q revenue ramp | 2H26 | Shows license recognition is catching up |
| Samsung 4/5/8nm customer activity | 2026-2027 | Validates the core foundry-node thesis |
| Square CC NoC launch | 2026 target | Tests whether the subsidiary is an option or a cost drag |

### Invalidation

| Invalidation signal | Interpretation |
|---|---|
| No new LPDDR6/5X wins | Pre-porting thesis weakens |
| 2Q-3Q revenue stuck below KRW 5.0B | KRW 30B+ revenue path is impaired |
| Operating loss remains above KRW 6.0B per quarter | Cost structure is still too heavy |
| Samsung Foundry-related customer pool weakens | Core Samsung value-chain thesis is damaged |
| Square requires additional parent funding | Subsidiary dilution and cost risk rise |
| Refixing increases effective dilution | Shareholder value leakage grows |
| Royalty mix remains stuck around the mid-single digits | IP-platform quality remains unproven |

---

## 11. Final Note

OpenEdges is a good technology option. It is not yet a good earnings company.

The cleanest investment thesis is not "Korea's NPU winner." It is **LPDDR5X/LPDDR6 PHY and controller IP for Samsung 4/5/8nm AI and edge ASIC customers**. That is narrower, but also stronger. It identifies the real bottleneck, the real customer pool and the real reason OpenEdges can matter despite global IP giants.

TSS and the Japan unit strengthen the core IP base. OpenEdges Square adds a separate CC NoC and IP-platform option, but that option is only partly owned by the listed parent and must be monitored for cost discipline. The 2026 CPS financing gives the company runway, but also adds dilution risk.

At KRW 500B+ market capitalization and roughly 17x 2026F sales, the stock already assumes a better future. The job now is not to admire the technology. The job is to verify the conversion chain: LPDDR6/5X wins, tape-out, silicon proof, revenue recognition, breakeven and eventually royalties.

**My conclusion is unchanged but sharper: Watchlist / Pilot Hold. Scale only after the numbers start confirming the IP story.**

---

## Source Notes

- Company IR Book: OpenEdges Technology 2026.03 IR Book via KIND, including product roadmap, customer count, license history, employee mix and subsidiary structure.
- OpenEdges official release on OpenEdges Square launch: [OpenEdges Technology launches subsidiary OpenEdges Square](https://www.openedges.com/ko/post/news0816).
- The Bell coverage on OpenEdges and Square: [OpenEdges Technology and Square synergy story](https://www.thebell.co.kr/front/newsview.asp?key=202311301141250240104442).
- DigitalToday coverage on OpenEdges Square capital increase and ownership change: [OpenEdges Technology participates in OpenEdges Square capital increase](https://www.digitaltoday.co.kr/news/articleView.html?idxno=611992).
- Design-Reuse coverage on LPDDR6/5X commercialization: [OpenEdges advances commercialization of LPDDR6/5X Memory Subsystem IP](https://www.design-reuse.com/news/202530336-openedges-advances-commercialization-of-lpddr6-5x-memory-subsystem-ip-targeting-next-generation-ai-and-hpc-markets/).
- Market snapshot used for valuation reference: [Maeil Business stock page for OpenEdges Technology](https://stock.mk.co.kr/price/home/KR7394280002).

---

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
