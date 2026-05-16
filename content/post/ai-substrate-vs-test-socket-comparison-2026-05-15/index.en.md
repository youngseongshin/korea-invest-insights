---
title: "Two Betas of AI Back-End — Substrates Are a 'Volume Beta,' Test Sockets Are a 'Consumables Beta.' Same AI Tailwind, Completely Different Structures"
date: 2026-05-15
description: "Who actually makes money when AI silicon sells? It is not just the GPU and HBM makers. The 'back end' also has major winners. Two regions matter — substrates and test sockets. Both are grouped under 'AI back-end,' but the investment structures are completely different. Substrates are a direct CAPEX beta on AI-server build-out. Volumes rise, packages get bigger, ASPs lift. Short-term momentum is strong: Daeduck Electronics 1Q26 OPM 14.8%, Samsung Electro-Mechanics package solutions revenue +45%. Test sockets are a high-margin consumables beta on chip complexity. As chips get more complex, testing gets harder, and the sockets have to be remade. ISC 1Q26 OPM 35%, AI revenue 81% of total. LEENO Industrial OPM 47%. Same AI tailwind, but the margin structures differ by ~3x. Don't lump the two as one 'AI theme.' For 3–6 month momentum, substrates. For 1–2 year holding, test sockets."
categories: ["Industry-Analysis"]
tags:
  - "AI silicon"
  - "substrate"
  - "test socket"
  - "FC-BGA"
  - "AI back-end"
  - "Korea stocks"
slug: ai-substrate-vs-test-socket-comparison-2026-05-15
---

> 📚 AI back-end series
> Previously: Samsung Electro-Mechanics MLCC and FC-BGA deep dive, Jeju Semiconductor legacy-memory thesis

*Who actually makes money when AI silicon sells? Nvidia (GPU) and SK hynix (HBM) are the names that come to mind first. But the "back end" of the supply chain has major winners too. We call it AI back-end. Two regions matter most: substrates and test sockets. Both are parts that an AI chip passes through before completion — but the investment structures are completely different. Substrates are a bet on "AI server units." Test sockets are a bet on "AI chip complexity." Margins are roughly 3x higher in test sockets, and momentum is faster in substrates. Which is the better investment depends on how long you plan to hold.*

---

## Key takeaways

* **Two regions in AI back-end**: substrates and test sockets.
* **Substrate essence**: a "direct CAPEX beta" on AI-server build-out. More units → more revenue; larger packages → higher ASP.
* **Test-socket essence**: a "high-margin consumables beta" on chip complexity. More complex chips → harder testing → more / harder sockets.
* **Profitability gap**: on 1Q26, Daeduck Electronics 14.8% vs ISC 35% vs LEENO Industrial 47.4%. **Test sockets dominate**.
* **Momentum gap**: substrate earnings revisions are faster — ASP hikes, new big-tech LTAs, capacity tightness are all near-term catalysts.
* **Cycle risk**: substrates are a CAPEX cycle (shortage → CAPEX → glut). Test sockets, being consumables, run with lower cyclicality.
* **Bottom line**: short-term momentum trades → substrates (Daeduck Electronics, Samsung Electro-Mechanics). 1–2 year compounding → test sockets (LEENO Industrial, ISC). These are not the same "AI theme."

---

## 1. Setup — what substrates and test sockets actually are

### 1.1 How AI silicon gets made

```
Production flow of AI silicon:

1. Design (Nvidia, AMD, Google, Meta, etc.)
2. Wafer fab (TSMC, Samsung Foundry)
3. Dicing
4. Packaging (HBM, interposer, package substrate join)
   ← "substrates" used here
5. Test (performance / reliability / burn-in)
   ← "test sockets" used here
6. Shipment

Substrate     = "the pedestal the chip sits on"
Test socket   = "the slot a chip plugs into briefly for testing"

Both are parts AI silicon passes through before completion,
but their roles and usage patterns are completely different.
```

### 1.2 Substrate — what is it

```
A substrate connects the microscopic circuitry inside a chip
(nanometer scale) to the outside world (millimeter scale).

What it does:
1. Electrical connection (thousands of pins → board)
2. Mechanical support (stable mounting of large packages)
3. Thermal management (heat-flow path away from the chip)
4. Signal integrity (high-speed signals without loss)

Why AI matters:
- AI chips are much larger than typical silicon
  (Nvidia H100 = 814 mm², 2–3x a typical CPU)
- Thousands to tens of thousands of pins
- High-speed data movement
- Heavy heat budget (700W+)

→ Specialized substrates (FC-BGA) are required
→ Harder to make and more expensive than ordinary substrates
→ Korean players: Samsung Electro-Mechanics, Daeduck Electronics,
  Isu Petasys.
```

### 1.3 Test socket — what is it

```
A test socket is a slot used briefly to test a finished chip.

What it does:
1. Electrically connects every chip pin to the tester
2. Verifies the chip works under signal / power / temperature stress
3. Filters out failing units
4. Reliability validation (long-duration testing)

Analogy:
Chip          = car
Test socket   = the diagnostic port at the inspection bay
→ Connected briefly during inspection, then disconnected
→ The same port is used for many different cars
→ Ports wear out over time and have to be replaced

Why AI matters:
- AI chips are expensive (\~USD 30k for an H100)
- A single bad unit costs a lot → test intensity rises
- High-current / high-speed / high-temperature environments
  → tougher socket spec
- Each chip generation needs new sockets → recurring revenue

Korean players: LEENO Industrial, ISC, TSE.
```

### 1.4 Why they are not the same "AI theme"

```
Substrate:
- Made once, shipped with the chip (capital-good character)
- Roughly one substrate per AI server
- Revenue = volume × ASP
- Adding capacity = CAPEX burden

Test socket:
- Reused many times, then replaced (consumable character)
- Roughly 50–200 sockets to test 10,000 chips
- Revenue = chip output × test intensity × socket replacement
- Capacity additions are smaller

Margin structure:
Substrate:    OPM \~10–15% (CAPEX, depreciation drag)
Test socket:  OPM \~30–50% (custom design, consumable economics)

→ Both benefit from AI,
→ but revenue mix, margin profile, and cycle sensitivity differ.
```

---

## 2. The substrate side — "AI server volume beta"

### 2.1 What 1Q26 showed

```
Samsung Electro-Mechanics (009150) — Package Solution segment
(FC-BGA-led):
1Q26 revenue: KRW 725B
YoY:          +45%
QoQ:          +12%

Daeduck Electronics (353200):
1Q26 revenue: KRW 346.3B (YoY +61%)
1Q26 OP:      KRW 51.3B (turn-around to black)
OPM:          14.8%

Product mix:
- FCCSP (mobile-grade package substrate): 39%
- FCBGA (PC / server-grade):              23%
- CSP (memory):                            22%
- MLB (multilayer board, AI server):       16%

YoY growth:
- Package substrates: +65%
- MLB:                +43%

→ AI-server package substrates + network boards growing together
→ A direct beta on AI infrastructure.
```

### 2.2 Why substrates are short

```
Characteristics of AI-server FC-BGA:
- Surface area 2–3x a PC FC-BGA
- Multilayer (20–30 layers)
- High-speed signaling (PCIe 5.0 / 6.0)
- Strict thermal management

Companies that can make these:
- Korea: Samsung Electro-Mechanics, Daeduck, LG Innotek, Isu Petasys
- Taiwan: Unimicron, Nan Ya PCB
- Japan: Ibiden, Shinko Denki

The problem: capacity (CAPA) can't keep up with demand
- Big-tech AI-server orders have exploded
- Greenfield substrate fabs take 2–3 years to build
- Short supply → ASP hikes

Press cited:
"Samsung Electro-Mechanics FC-BGA demand exceeds capacity by \~50%;
 price-hike negotiations under way."

→ This is why substrate stocks have been strong.
```

### 2.3 Substrate cycle risk

```
Substrate is a classic CAPEX-cycle industry:

Up-cycle (today):
shortage → ASP hike → margin expansion → stock strength
→ companies announce sizable CAPEX

Build phase (2026–2027):
fabs under construction → revenue rising, CAPEX burden rising
→ stocks still trending strong

Build complete (2027–2028):
new fabs come online → supply surges
→ if demand doesn't keep up, prices fall
→ margins squeeze → stocks weaken

Historical patterns:
2017–2018 memory cycle: same shape
2021–2022 MLCC cycle:   same shape

→ For substrate investing, "where in the CAPEX cycle" is the key
→ Today: early- to mid-stage of an up-cycle
→ Until build-out completes, upside is intact.
```

---

## 3. The test-socket side — "chip-complexity beta"

### 3.1 What 1Q26 showed

```
ISC (095340):
1Q26 revenue: KRW 68.3B
1Q26 OP:      KRW 23.6B
OPM:          35%
Math: 23.6 / 68.3 = 34.55%

Revenue mix:
- AI revenue:           KRW 55.3B (81% of total)
- Data-center revenue:  KRW 54.2B (79% of total)
→ Already an "AI data-center company."

LEENO Industrial (058470):
1Q26 revenue: KRW 99.77B
1Q26 OP:      KRW 47.30B
OPM:          47.4%
Math: 47.30 / 99.77 = 47.41%

Revenue mix:
- IC test sockets:      64.10%
- LEENO pins (pogo):    24.65%
- Medical components:   10.46%

→ Custom-designed sockets + vertically integrated pin manufacturing
→ 47% OPM is at the top of Korean manufacturing.
```

### 3.2 Why margins are this high

```
Structural features of the test-socket industry:

1. Customer-specific designs
   → pin layout, size, signal conditions vary by chip
   → hard to standardize → pricing power

2. High qualification cost
   → each new chip requires socket design / test / qualification
   → once qualified, locked in until end-of-life of that chip
   → reliability competition, not price competition

3. Consumable nature
   → sockets wear out / degrade and need periodic replacement
   → recurring revenue

4. Refresh with every chip generation
   → new chip = new socket
   → faster chip cadence = faster revenue cadence

5. Small TAM (a few tens of USD billion)
   → too small for mega-cap entrants
   → oligopoly of specialist players

All five conditions together enable 30–50% OPM.
```

### 3.3 Why AI made test sockets more important

```
AI chip characteristics:

1. Expensive (USD 10k–30k per unit)
   → cost of a single bad unit is high
   → test intensity ↑

2. High pin count (thousands–tens of thousands)
   → more complex sockets
   → ASP ↑

3. High current / temperature / speed
   → tougher socket durability requirements
   → shorter replacement cycle

4. SLT (System-Level Test) share rising
   → from simple functional test → full system test
   → longer test times
   → more socket usage

5. New modules: HBM, SOCAMM2, etc.
   → new socket categories
   → fresh revenue lines

→ In the AI era, test-socket demand grows
   faster than chip output.
```

### 3.4 ISC vs LEENO Industrial

```
Both are "test-socket companies," but their structures differ.

ISC (rubber-socket strength):
- Core tech: silicone rubber sockets
- Strength: AI data-center mass-production testing, SLT
- Customers: global GPU / ASIC majors
- Exposure: AI data center 81%
- Profile: direct AI beta (volatility higher)
- 1Q26 OPM: 35%

LEENO Industrial (pogo-pin strength):
- Core tech: pogo pins, in-house pin manufacturing
- Strength: R&D, mobile AP, RF, ASIC development
- Customers: diversified (hundreds of accounts)
- Exposure: many chip categories (lower AI share than ISC)
- Profile: quality compounder (more stable)
- 1Q26 OPM: 47.4%

→ Don't lump them as "the same test-socket stock."
→ ISC      = AI data-center beta
→ LEENO    = diversified high-margin platform

They are complements, not substitutes.
```

---

## 4. Head-to-head

### 4.1 1Q26 operating margins

```
Same "AI back-end beneficiaries," different margin profiles:

Daeduck Electronics (substrate): 14.8%  ████
Samsung E-M Package Solutions:   \~12%   ███
ISC (test socket):               35.0%  █████████
LEENO Industrial (socket):       47.4%  ████████████

KRW 100 of revenue → OP:
Daeduck:  KRW 14.8
ISC:      KRW 35.0
LEENO:    KRW 47.4

→ Roughly 3x spread on the same revenue
→ The result of structural industry differences.
```

### 4.2 Growth pace vs margin stability

| Metric | Substrate (Daeduck) | Test socket (ISC) | Test socket (LEENO) |
| --- | ---: | ---: | ---: |
| 1Q26 revenue YoY | +61% | Strong YoY | +18% |
| 1Q26 OP YoY | turnaround | Strong YoY | +35% |
| OPM | 14.8% | 35.0% | 47.4% |
| AI exposure | Mid–high | Very high (81%) | Mid |
| Volatility | High | Mid | Low |
| Cycle sensitivity | High | Mid | Low |

```
Summary:
- Revenue growth: substrate (Daeduck) > test socket
- Margin level:   test socket > substrate
- Margin stability: LEENO > ISC > substrate
- Direct AI beta:   ISC > Daeduck > LEENO.
```

### 4.3 Cycle risk

```
Substrate cycle risk (high):
- Shortage → CAPEX → glut, in repeat
- 2–3 year build lead time
- When the cycle rolls, utilization and ASP fall together
- Depreciation pressures margin

Test-socket cycle risk (low):
- Consumable economics dampens revenue volatility
- Customer-specific design keeps pricing stable
- New chips keep being released
- Quarterly volatility still exists

Long-hold perspective:
→ Test sockets are far more stable
→ avoids the substrate CAPEX cycle

Short-momentum perspective:
→ Substrate momentum is stronger
→ ASP-hike / capacity-tight headlines are more frequent.
```

---

## 5. Investment priority — different answers for different horizons

### 5.1 Short-term momentum (3–6 months) — substrates win

```
Why:
- Earnings-revision pace is faster
- Steady stream of ASP-hike headlines
- Probability of new big-tech LTA
- AI-server shipments accelerating

Order of preference:
1. Daeduck Electronics: turnaround + AI MLB / FC-BGA beta
2. Samsung Electro-Mechanics: AI FC-BGA + MLCC combo
3. Isu Petasys (complement): ultra-high-layer MLB strength

Caveats:
- Substrates have already moved a lot
- Check the CAPEX-cycle position
- Wait for the macro gate to clear (see earlier post).
```

### 5.2 Hold 1–2 years (quality growth) — test sockets win

```
Why:
- Margin structure is structurally superior
- Smaller cycle risk
- AI chip diversification = more socket categories = revenue diversification
- Active capacity expansion (new fabs)

Order of preference:
1. LEENO Industrial: highest quality, but the multiple is rich
2. ISC: direct AI data-center beta
3. TSE (complement): growth at a more reasonable price

Caveats:
- LEENO faces margin-impact risk during the new-fab move
- ISC has quarterly volatility (1Q26 QoQ -6%)
- Both trade at 30–45x PER.
```

### 5.3 A combined AI back-end portfolio

```
Aggressive (momentum tilt):
- Daeduck Electronics  40%
- ISC                  30%
- Samsung Electro-Mechanics 20%
- LEENO Industrial     10%

Balanced (growth + stability):
- LEENO Industrial     30%
- Samsung Electro-Mechanics 25%
- ISC                  25%
- Daeduck Electronics  20%

Defensive (quality tilt):
- LEENO Industrial     40%
- Samsung Electro-Mechanics 30%
- ISC                  20%
- Daeduck Electronics  10%

→ If you must pick one, by horizon and volatility tolerance:
→ 1y+ hold:   LEENO Industrial
→ 3–6 months: Daeduck Electronics
→ Direct AI data-center beta: ISC.
```

---

## 6. Four common misconceptions

### 6.1 #1: "Both are AI plays, so they're the same"

```
As shown:
- OPM differs by 3x
- Cycle sensitivity differs
- Revenue mix differs

Grouping them as one bucket weakens diversification.
→ Volatility moves together
→ Pairing with another sector is more effective.
```

### 6.2 #2: "Pogo sockets are being replaced by rubber sockets"

```
Only partially true:

Where the shift happens:
- AI GPU / ASIC large-die chips
- High-current / high-speed signal testing
- SLT (System-Level Test)
→ Rubber-socket penetration rises (ISC strength)

Where it doesn't:
- High-precision R&D testing
- Mobile APs, RF chips
- Small-batch / many-SKU production
→ Pogo retains share (LEENO strength)

→ Not "the whole market converts" — it is "market segmentation"
→ Therefore ISC and LEENO are complements
→ It is rare for only one of them to do well.
```

### 6.3 #3: "Substrate stocks have run too much"

```
The right question is not the absolute level,
it is "where in the CAPEX cycle are we."

Now:
- Shortage still in progress
- ASP-hike negotiations under way
- LTAs with big-tech under discussion
- CAPEX announcements have started, but ramps are 2–3 years away

→ Early- to mid-stage of an up-cycle
→ Price moved, but the cycle has not topped.

That said, from these levels:
- Scaled entries recommended
- Wait for the macro gate to clear
- Chasing is inefficient.
```

### 6.4 #4: "The test-socket TAM is too small"

```
True on the headline number, but the read is wrong:

Test-socket TAM:
- \~USD 3–4 billion
- Less than 2% of the memory market (\~USD 200B)
- Small in absolute terms

Why that's actually a feature:
- Too small for mega-cap entrants
- Sustains the specialist oligopoly
- Price competition stays mild
- 30–50% OPM achievable

Compare:
A USD 200B business at 5% OPM vs
a USD 4B business at 45% OPM
→ Comparable absolute OPDollars
→ The second is more stable and more predictable.

This is the structure LEENO and ISC benefit from.
```

---

## 7. The next six months — checklist

### 7.1 Substrates (cycle-intact confirmation)

```
Positive signals:
□ FC-BGA ASP hikes continue
□ Samsung E-M / Daeduck add new big-tech customers
□ Large-die / high-layer mix lifts in revenue
□ MLB demand persists at 800G / 1.6T networking
□ Utilization stays above 90% even with CAPEX rising

Negative signals:
□ ASP hike negotiations delayed / fail
□ Big-tech AI server orders decelerate
□ Pace of new CAPEX announcements accelerates (glut concern)
□ Utilization drops below 80%

Frequency: quarterly earnings + mid-quarter IR commentary.
```

### 7.2 Test sockets (growth-intact confirmation)

```
ISC:
□ 3Q26 revenue re-acceleration (2Q may be a ramp-prep quarter)
□ New data-center infrastructure customer first-volume ramp
□ SOCAMM2 mass-production testing revenue begins
□ SLT mix stays above 70%
□ AI revenue mix stays above 80%

LEENO Industrial:
□ Progress on the new-fab move
□ No margin damage during the move (OPM 45%+ holds)
□ Customer diversification (Apple / TI / HPC / ASIC expansions)
□ Strong R&D socket demand
□ No overhang / governance issues

Frequency: quarterly earnings.
```

### 7.3 The macro backdrop

```
The macro gate from the earlier post:
- US 10-year below 4.45%
- Brent below 105
- USD/KRW below 1,480
- VIX below 18

These must clear for:
- Broad risk-asset recovery
- Back-end stocks to ride the trend
- Good earnings to translate into good price.

If the gate doesn't clear:
- Multiples stay pressured independent of fundamentals
- Wait for confirming close / turnover before scaling in.
```

---

## 8. How this connects to other posts

```
Samsung Electro-Mechanics piece:
→ MLCC + FC-BGA 1Q26 dual beneficiary
→ The most detailed stock covered in this article's substrate side
→ Scenario PERs for how far the multiple can stretch

Jeju Semiconductor piece:
→ "Commodity memory in shortage because of AI"
→ Another AI back-end shape (memory shortage beta)

Samsung Electronics strike piece:
→ Key variable for the memory supercycle
→ AI silicon → AI server → memory / substrate / test socket
→ Disruption in one ripples into the back end

KOSPI crash + macro-gate piece:
→ "Cycle before the stock"
→ Names in this post also rational only after the macro gate clears.
```

---

## 9. The one-line bottom line

When AI silicon sells, the first beneficiaries are the GPU and HBM makers. But the back end also has two big winners — **substrates and test sockets**.

Both are grouped as "AI back-end," but the structures are completely different. **Substrates are an "AI server volume beta."** Volumes rise, packages get bigger, ASPs lift — direct upside. Momentum is fast and operating margins expand from a \~12–15% base in 1Q26. But this is a CAPEX-cycle industry, and the build-out-complete date is the risk.

**Test sockets are a "chip-complexity beta."** As chips get more complex, testing gets harder, and new sockets are needed each time. OPM sits at 35% for ISC and 47% for LEENO — roughly 3x substrate margins. Consumable economics dampen cyclicality. The downsides: the TAM is small and multiples are already rich.

**Don't lump them as one "AI theme."** For short-term momentum, substrates (Daeduck Electronics, Samsung Electro-Mechanics) lead. For 1–2 year holding, test sockets (LEENO Industrial, ISC) make more sense. The best play is to hold both as complements — when substrates shake at a cycle peak, test sockets defend; when test sockets feel multiple pressure, substrates' momentum carries.

**Same AI tailwind, completely different structures — understanding just that lifts the quality of back-end investment decisions by a full step.**

---

*This article is research and commentary only and is not investment advice. Samsung Electro-Mechanics 1Q26 figures are per the company's official IR release. Daeduck Electronics 1Q26 (revenue KRW 346.3B, OP KRW 51.3B, OPM 14.8%) are per its IR materials. ISC 1Q26 (revenue KRW 68.3B, OP KRW 23.6B, OPM 35%, AI revenue mix 81%, data-center mix 79%) are per its IR materials. LEENO Industrial 1Q26 (revenue KRW 99.77B, OP KRW 47.30B, OPM 47.4%) is per preliminary disclosure reporting; product-mix figures (IC test sockets 64.10%, LEENO pins 24.65%, medical components 10.46%) are per the quarterly report. OPM uses operating profit divided by revenue, rounded to one decimal place. AI / data-center revenue shares are derived from company disclosures. The operating-margin comparison reflects a single quarter (1Q26); annual averages may differ. CAPEX-cycle risk, new-fab transition margin risk, and AI demand volatility are author judgments and not certainties. Global macro variables (US rates, oil, FX, VIX) can independently move the stocks. The analysis may be wrong. Data cut-off: May 15, 2026 KST.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
