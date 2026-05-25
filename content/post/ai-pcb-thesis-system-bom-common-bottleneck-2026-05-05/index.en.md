---
title: "AI PCB and Substrate Thesis: GPU, CPU, NIC and CCL Demand Are One System Bottleneck"
slug: ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05
date: 2026-05-05T23:15:00+09:00
description: "The market often frames AI hardware as a sequence: GPU first, then memory, then substrates. That is only partly right. AI infrastructure is now a rack-scale system made of GPUs, CPUs, DPUs, NICs, switch ASICs, memory modules, power boards and low-loss CCL. Every chip expansion needs a board. This sector thesis connects Samsung Electro-Mechanics, Daeduck Electronics, Doosan Electronic BG, Kolon Industries and Pamicell to the same system-level bottleneck."
categories: ["Sector-Deep-Dive", "Korea Market"]
tags:
  - "AI PCB"
  - "AI substrates"
  - "FC-BGA"
  - "MLB"
  - "CCL"
  - "Agentic AI"
  - "Physical AI"
  - "CPU demand"
  - "NVIDIA Vera Rubin"
  - "rack-scale AI"
  - "Samsung Electro-Mechanics"
  - "Daeduck Electronics"
  - "Doosan"
  - "Kolon Industries"
  - "Pamicell"
  - "Korea stocks"
series: ["ai-pcb-substrate-thesis-2026"]
---

> <strong>Sector map:</strong> This is the upper-layer AI PCB and substrate thesis behind the Pamicell work. The company comparison continues in [Korea AI PCB Ecosystem: 10 Companies](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/), and the full reading path sits in the [AI PCB hub](/page/korea-ai-pcb-substrate-hub/). Read it together with [Pamicell Part 1](/post/pamicell-doosan-electro-bg-proxy-rediscovery-2026-04-30/), [Pamicell Part 2](/post/pamicell-four-layer-progress-and-fifth-cycle-layer-2026-05-03/), and the [Samsung Electro-Mechanics AI infrastructure re-rating note](/post/samsung-electro-mechanics-ai-infrastructure-rerating-2026-04-21/).

The company-level question is narrower: which Korean names have the best position in AI PCB, FC-BGA and low-loss material supply? This note moves one level up. It asks why capital should enter the whole ecosystem in the first place.

The answer is not "substrates are the next theme after GPUs." That is too linear. AI infrastructure is no longer a GPU card. It is a rack-scale system. A modern AI rack has GPUs, CPUs, DPUs, NICs, switch ASICs, memory modules, power delivery, cooling control and high-speed boards. Each layer adds silicon. Each piece of silicon needs a package substrate, a module board, a motherboard, a switch board or a low-loss material stack.

That is the core point: the PCB and substrate layer is not the next stop in a simple rotation. It is the common denominator of the entire AI system bill of materials.

---

## TL;DR

1. The market's "GPU to memory to substrate" sequence is directionally useful, but incomplete. The better frame is simultaneous system expansion: GPU, HBM, CPU, DPU, NIC, switch ASIC and memory modules all rise together, and all require substrates or boards.
2. NVIDIA Vera Rubin NVL72 makes the point concrete. The platform combines 72 Rubin GPUs, 36 Vera CPUs, NVLink 6 switching, ConnectX-9 SuperNICs, BlueField-4 DPUs and Spectrum-X / Spectrum-6 Ethernet scaling. The CPU:GPU ratio is 0.5, or one CPU for every two GPUs. This is no longer a single-chip story.
3. Agentic AI raises the CPU intensity of inference. Tool orchestration, retrieval, code execution, database access, memory management and security isolation all lean on CPUs, DRAM, NICs and DPUs. If CPU content rises, server CPU FC-BGA, memory module boards, SoCAMM, motherboards and low-loss CCL all get pulled along.
4. Physical AI expands the thesis outside the data center. Autonomous vehicles, humanoids, industrial robots and space electronics all use more boards, more sensors, more edge AI modules and more reliability-sensitive PCB material. The time curve differs: data center first, autonomous driving second, humanoids later, space as a high-reliability margin premium.
5. For Korea, the investable map becomes layered. Samsung Electro-Mechanics is the high-end FC-BGA plus MLCC node. Daeduck Electronics is the FC-BGA / MLB / SoCAMM factor candidate. Doosan Electronic BG is the CCL anchor. Kolon Industries and Pamicell sit upstream in low-dielectric materials. Pamicell is not just a standalone stock idea; it is one compressed proxy inside a larger AI substrate system.

---

## 1. The Linear Frame: Useful, But Too Small

The market likes sequences because sequences are easy to trade.

First came GPUs: NVIDIA captured the budget because accelerators were scarce. Then came HBM: GPUs could not scale without memory bandwidth, so SK hynix, Samsung Electronics and Micron moved to the center of the discussion. The next step is usually described as substrates or advanced packaging: if GPUs and HBM scale, then FC-BGA, interposers, MLBs and CCL should follow.

That frame is not wrong. A larger GPU needs a larger and more complex package substrate. HBM expansion raises packaging intensity. Server boards become denser and faster. From that angle, substrates do come after GPUs and HBM in the recognition cycle.

But the frame misses the most important change in system architecture. AI infrastructure in 2026 is not a pile of GPUs. It is a rack-scale platform that co-designs compute, memory, networking, security and system control.

The NVIDIA Vera Rubin NVL72 configuration is the cleanest example. Public NVIDIA materials describe a system built around 72 Rubin GPUs and 36 Vera CPUs, with NVLink 6 switching, ConnectX-9 SuperNICs and BlueField-4 DPUs. NVIDIA's own Rubin platform materials also frame the platform as a six-chip co-design: Vera CPU, Rubin GPU, NVLink switch, ConnectX-9 SuperNIC, BlueField-4 DPU and Spectrum-6 Ethernet switch.

The arithmetic matters:

```text
Vera CPUs  = 36
Rubin GPUs = 72
CPU:GPU    = 36 / 72 = 0.5
```

One CPU for every two GPUs is not a trivial host-processor footnote. It says the rack is a system, not a GPU shelf. Once that is true, the substrate thesis stops being a downstream echo of GPU demand. It becomes a multi-chip system thesis.

---

## 2. Why Every Chip Pulls A Board

The easiest way to see the substrate layer is to walk the system bill of materials.

| System layer | Chip or module | Board / substrate demand |
|---|---|---|
| AI acceleration | GPU, custom ASIC, TPU | Large FC-BGA, advanced package substrate, high-density board |
| Host and orchestration | Server CPU, Vera CPU, x86 / Arm CPU | Large FC-BGA, CPU socket board, motherboard MLB |
| Memory bandwidth | HBM, DDR5, LPDDR-based server modules, SoCAMM | Interposer / substrate, memory module PCB, signal-integrity material |
| Networking | NIC, SuperNIC, Ethernet switch ASIC, InfiniBand switch | Switch board, optical module PCB, low-loss MLB |
| Data movement and security | DPU, SmartNIC | Package substrate, accelerator card PCB |
| Power and control | VRM, power modules, BMC and control boards | Power PCB, MLCC, high-reliability board |

This is why "GPU demand" is too narrow. A hyperscaler does not buy a GPU in isolation. It buys a working rack. That rack contains compute chips, memory chips, networking chips, control chips and power electronics. The more the system expands, the more the board layer is asked to carry high-speed signals, heat, power and reliability.

The Korean equity translation is also clearer under this frame:

| Korean layer | Companies to track | What they represent |
|---|---|---|
| High-end package substrate | Samsung Electro-Mechanics, Daeduck Electronics, Korea Circuit | FC-BGA and package substrate exposure |
| Multi-layer board and module PCB | Isu Petasys, Daeduck Electronics, TLB, Simmtech, Korea Circuit | Server motherboard, switch board, memory module and SoCAMM exposure |
| CCL anchor | Doosan Electronic BG | High-end copper-clad laminate for AI servers and networking |
| Low-loss materials | Kolon Industries, Pamicell | mPPO / low-dielectric resin and hardener inputs |
| Power stability | Samsung Electro-Mechanics and MLCC peers | MLCC content per AI server and high-voltage component mix |

Pamicell belongs in this map as an upstream material proxy to Doosan Electronic BG. Samsung Electro-Mechanics belongs as the premium listed Korean node in FC-BGA and MLCC. Daeduck belongs as the broader FC-BGA / MLB / SoCAMM factor candidate. These are not separate stories. They are different points on the same system BOM.

---

## 3. Agentic AI Makes The CPU Layer Bigger

Traditional LLM inference looked simple from a hardware lens:

```text
prompt
  -> GPU forward pass
  -> response
```

Agentic AI changes the workload. The model does not just answer. It plans, calls tools, searches, reads files, executes code, queries databases, manages memory, verifies output and may coordinate with other agents. The GPU is still central, but the non-GPU work becomes much heavier.

| Agentic function | Main hardware pull |
|---|---|
| LLM forward pass | GPU + HBM |
| Tool orchestration | CPU |
| Retrieval and search | CPU + DRAM + storage |
| Code execution | CPU, sandbox, compiler / interpreter |
| Session memory and state | CPU + DRAM |
| Networked tool calls | NIC + switch ASIC + PCB |
| Security and isolation | CPU + DPU |

TrendForce has been explicit about this direction. Its April 2026 agentic AI report and related public commentary describe a structural change in CPU:GPU ratios, tight server CPU supply and price increases by Intel and AMD. Tom's Hardware reported the same direction from the industry side: AI server configurations that once used one CPU for four to eight GPUs can move toward much higher CPU intensity in agentic inference scenarios.

The exact ratio will vary by workload. A code-agent cluster is not the same as a video generation cluster. A retrieval-heavy enterprise agent is not the same as a pure batch inference system. But the direction is what matters for substrate investors: more CPU work means more CPU packages, more memory around the CPU, more networking, and more board-level signal integrity requirements.

The path from agentic AI to Korean substrates looks like this:

```text
Agentic AI adoption
  -> CPU orchestration workload increases
  -> server CPU, DPU, NIC and switch ASIC content rises
  -> server CPU FC-BGA and high-layer MLB demand rises
  -> memory modules, SoCAMM and motherboard complexity rise
  -> low-loss CCL and low-dielectric materials become more important
  -> Korean substrate and material companies receive a share of the BOM expansion
```

That last line is important. Korea does not own the CPU market. Intel, AMD, Arm, NVIDIA and cloud-service-provider custom CPUs capture the chip value. Korean listed companies capture the board and material content around the chip. This is still meaningful because the substrate content grows with the system, not with a single product line.

---

## 4. Physical AI: Outside The Data Center

The data center is the first and largest near-term driver. Physical AI is the second expansion path. The timing is slower, but the direction is consistent: when intelligence moves into vehicles, robots, factories and satellites, more compute moves closer to the edge. More edge compute means more boards.

### Autonomous driving

Autonomous driving is the most realistic second leg because cars already use large electronics stacks. A vehicle with advanced driver assistance or autonomous functions contains central compute, sensor fusion, camera modules, radar, lidar, vehicle Ethernet and redundant safety controllers.

| Vehicle system | PCB and material pull |
|---|---|
| Central compute | High-density board, processor package substrate |
| Sensor fusion ECU | Multi-layer PCB, high-speed signal board |
| Camera / lidar / radar | Rigid-flex, RF board, module PCB |
| Vehicle Ethernet | Low-loss CCL and high-speed communication PCB |
| Safety redundancy | More ECUs and more board area |

This does not hit earnings as quickly as AI data centers. Vehicle programs take time, qualification is slow and the revenue curve is model-cycle dependent. But the direction is not ambiguous: a smarter vehicle carries more board content than a traditional vehicle.

### Humanoid and industrial robotics

NVIDIA Jetson Thor gives the physical AI argument a concrete hardware reference point. NVIDIA positions Jetson Thor for physical AI and robotics, with up to 2,070 FP4 TFLOPS, 128GB of memory and a 40W to 130W configurable power range. That kind of edge AI module needs high-density boards, power boards, sensor interconnect and flexible PCBs.

Humanoids will not drive Korean substrate earnings tomorrow. They are not yet a mass-volume market. But they extend the option value of the thesis. If edge AI modules become standardized across robots, factories and industrial machines, board content shifts from a data-center-only story to a distributed compute story.

### Space and defense electronics

Space is different. It is not a volume story. It is a reliability and margin story. NASA and IPC-related materials for mission hardware emphasize high-reliability PCB requirements, supplier qualification and Class 3 / space-addendum type standards. For listed Korean PCB names, the relevance is not "space will absorb massive capacity." It is that harsh-environment electronics can justify higher reliability standards and potentially better margins.

The time curve looks like this:

| End market | Earnings timing | PCB intensity | Practical confidence |
|---|---|---|---|
| AI data center | Fast | Very high | High |
| Autonomous driving | Medium | High | Medium to high |
| Humanoids / robotics | Slow | Medium to high | Medium |
| Space / defense electronics | Slow | High specification, low volume | Medium |

This ordering matters. The near-term model should still be data-center led. Physical AI is not a reason to stretch every valuation today. It is a reason the terminal market may be broader than the current AI server cycle implies.

---

## 5. What This Adds To The Pamicell Thesis

The Pamicell work started with a company-specific recognition gap. The market remembered a stem-cell company. The income statement increasingly looked like an AI CCL material supplier. The Doosan Electronic BG link, repeated supply-contract evidence, high-margin biochemicals and KRX industry reclassification all pushed in the same direction.

This sector thesis changes the question from "why Pamicell?" to "why does the upstream CCL material layer matter at all?"

The answer is that CCL and low-loss materials are not tied to one GPU generation. They sit under the system layer:

```text
GPU / CPU / DPU / NIC / switch ASIC expansion
  -> high-speed signal and thermal constraints rise
  -> low-loss CCL demand rises
  -> CCL producers need low-dielectric materials
  -> upstream suppliers such as Pamicell become compressed proxies
```

Pamicell is still not the same as Doosan Electronic BG, and it is not a PCB manufacturer. It is further upstream. That means customer concentration and qualification risk are real. But it also means the company's small size can make the same system-level demand look more powerful in percentage terms if orders keep compounding.

Put differently: Pamicell's thesis becomes more durable if the AI board cycle is not just a GPU substrate cycle, but a multi-chip system substrate cycle.

---

## 6. What This Adds To The Samsung Electro-Mechanics Thesis

Samsung Electro-Mechanics was already re-rated around two ideas: high-end FC-BGA and AI-server MLCC. That older framing still works. The system-BOM thesis makes it cleaner.

If the only driver were GPUs, Samsung Electro-Mechanics would be a high-end package-substrate story with MLCC attached. If the driver is rack-scale system expansion, the company sits in more than one lane:

| Lane | Why it matters |
|---|---|
| FC-BGA | Larger and more complex CPUs, GPUs, ASICs and networking chips need high-end package substrates |
| MLCC | AI servers, networking trays and power delivery all increase component density |
| Glass substrate option | Future large-package architecture may require new substrate materials and processes |
| Automotive and robotics electronics | Physical AI increases high-reliability component and board demand over time |

This does not remove valuation discipline. Samsung Electro-Mechanics has already been recognized by the market more than Pamicell or some smaller PCB names. The factor question is not "is this a good company?" It is "how much of the system-level substrate expansion is already in the price, and how much must be confirmed through orders, margins and guidance?"

That is why this note treats Samsung Electro-Mechanics as the premium anchor rather than the highest-beta idea. It is the cleanest Korean large-cap expression of FC-BGA plus MLCC, but its future return depends on continued estimate revisions rather than simply discovering the theme.

---

## 7. Portfolio Frame: Core, Barbell, Options

The company ranking can change with price, but the factor map is stable.

| Role | Candidate exposure | Reason |
|---|---|---|
| Premium anchor | Samsung Electro-Mechanics | FC-BGA + MLCC + customer qualification + scale |
| Core PCB factor | Daeduck Electronics | FC-BGA, MLB and potential SoCAMM / module board sensitivity |
| CCL anchor | Doosan Electronic BG inside Doosan | High-end CCL body of the domestic chain |
| Upstream material barbell | Kolon Industries and Pamicell | Low-dielectric resin / material exposure, smaller base and higher operating leverage |
| Optionality | Korea Circuit, TLB, Simmtech, Isu Petasys | Memory module, MLB, networking and broader AI PCB beta |

The point is not to force one answer. The point is to avoid treating all "AI PCB" names as the same asset. Package substrates, multi-layer boards, CCL and low-dielectric chemistry have different margin structures, qualification periods and customer risks.

A useful portfolio view is:

```text
Premium anchor:
  Samsung Electro-Mechanics

Core substrate / board factor:
  Daeduck Electronics, selected MLB names

Upstream material barbell:
  Kolon Industries + Pamicell

Higher-beta options:
  Korea Circuit, TLB, Simmtech, Isu Petasys
```

When the market says "the PCB cycle is over," the system-BOM thesis helps test whether that is true. If GPU shipments slow but CPU content, networking ASICs, DPUs and memory module complexity keep rising, the board cycle may cool in one lane while staying tight in another.

---

## 8. What Could Break The Thesis

The common-denominator frame is not a claim that the cycle lasts forever. Four risks matter.

First, hyperscaler AI capex can slow. If AWS, Microsoft, Google or Meta guide down for more than one quarter, the entire hardware supply chain will feel it.

Second, substrate technology can change. Glass substrate or other new architectures could alter the FC-BGA cycle faster than expected. This does not remove board demand, but it can shift the winners.

Third, capacity can arrive. If high-end CCL, glass fiber or low-loss material capacity enters faster than expected, pricing power can normalize before volumes fully mature.

Fourth, physical AI can take longer than the market wants. Autonomous driving, humanoids and space electronics all have long qualification and adoption cycles. They are not substitutes for near-term data-center revenue.

These risks do not kill the thesis. They define the checklist.

---

## 9. Verification Checklist

The thesis should be tracked at the system level, not just through one company's quarterly number.

| Signal | Why it matters |
|---|---|
| NVIDIA rack-scale roadmap | More chip types and higher rack density extend the common-denominator substrate cycle |
| CPU:GPU ratio commentary | A higher CPU ratio strengthens the CPU FC-BGA and motherboard MLB leg |
| Hyperscaler capex guidance | The first-order demand source for AI data-center boards |
| CCL and glass-fiber lead times | Confirms whether material tightness is real or easing |
| Samsung Electro-Mechanics package and component margins | Tests whether premium substrate and MLCC pricing still hold |
| Daeduck / MLB order commentary | Tests whether broader PCB beta is converting into revenue |
| Pamicell and Doosan Electronic BG contract cadence | Tests whether upstream CCL material demand is still compounding |
| Automotive / robotics PCB comments in Korean company IR | Early sign that physical AI is moving from optionality to revenue |

If these signals stay aligned, the substrate cycle is not simply a 2025-2027 theme. It becomes a multi-year system architecture shift.

---

## FAQ

### What is the AI PCB thesis?

The AI PCB thesis argues that AI infrastructure demand is no longer limited to GPUs and HBM. Rack-scale systems need GPUs, CPUs, NICs, DPUs, switch ASICs, memory modules and power boards. Each layer requires package substrates, multi-layer boards or low-loss materials.

### Why does agentic AI increase CPU demand?

Agentic AI uses tools, retrieval, code execution, memory management and orchestration. Those tasks add CPU, DRAM, networking and DPU workload around the GPU. Higher CPU content can increase demand for server CPU FC-BGA, motherboards, memory module boards and low-loss CCL.

### Why are Samsung Electro-Mechanics and Pamicell in the same sector map?

They sit at different points in the same AI substrate chain. Samsung Electro-Mechanics is a premium FC-BGA and MLCC node. Pamicell is an upstream low-dielectric material supplier linked to Doosan Electronic BG's CCL cycle. The same system-level AI board demand can affect both, but with different risk and valuation profiles.

### Is Pamicell a PCB company?

No. Pamicell is not a PCB manufacturer. The relevant thesis is upstream material exposure: low-dielectric / low-loss inputs used by CCL producers such as Doosan Electronic BG.

### Is this investment advice?

No. This is a sector research framework. The right conclusion depends on valuation, order cadence, margin confirmation, customer concentration and each investor's risk tolerance.

---

## Selected Public Sources

- NVIDIA Vera Rubin NVL72 product page: https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/
- NVIDIA Technical Blog, Vera Rubin platform overview: https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
- TrendForce, agentic AI and CPU:GPU ratio commentary: https://insights.trendforce.com/p/agentic-ai-cpu-gpu
- TrendForce report page, 2026 Agentic AI Wave: https://www.trendforce.com/research/download/RP260408AD
- Tom's Hardware, agentic AI and CPU demand: https://www.tomshardware.com/pc-components/cpus/shifting-need-for-cpus-in-ai-workloads-drives-intensifying-shortages-price-hikes
- NVIDIA Jetson Thor product page: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- NASA quality guidance for high-reliability PCB standards: https://sma.nasa.gov/sma-disciplines/quality
- NASA GSFC-STD-8001 high-reliability PCB standard: https://standards.nasa.gov/sites/default/files/standards/GSFC/Baseline/0/gsfc-std-8001.pdf

---

## Final Note

The cleanest version of the thesis is simple:

AI does not buy GPUs alone. It buys systems.

Systems add chips. Chips need substrates, boards and low-loss materials.

That is why the substrate layer should be read as a common bottleneck rather than a late-cycle afterthought. The implication is not that every Korean PCB or material stock deserves the same multiple. It is that the ecosystem should be evaluated as a system-level supply chain: Samsung Electro-Mechanics at the premium FC-BGA / MLCC node, Daeduck and MLB names at the board layer, Doosan Electronic BG at the CCL body, and Kolon Industries and Pamicell upstream in low-dielectric materials.

The work from here is not to repeat the theme. It is to track whether the system BOM keeps getting thicker, whether CPU and networking content continue to rise, and whether Korean companies convert that complexity into orders and margins.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
