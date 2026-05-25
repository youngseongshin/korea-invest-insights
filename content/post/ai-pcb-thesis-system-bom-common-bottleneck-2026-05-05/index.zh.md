---
title: "AI PCB与基板投资逻辑：GPU、CPU、NIC与CCL需求同属一个系统瓶颈"
slug: ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05
date: 2026-05-05T23:15:00+09:00
description: "市场通常将AI硬件描述为一条线性轨迹：先是GPU，再是内存，然后才轮到基板。这种说法只对了一半。AI基础设施如今已是机架级系统，由GPU、CPU、DPU、NIC、交换机ASIC、内存模块、电源板和低损耗CCL共同构成。每一颗芯片的扩张都需要一块电路板。本文从行业视角将Samsung Electro-Mechanics、Daeduck Electronics、Doosan Electronic BG、Kolon Industries与Pamicell连接到同一个系统级瓶颈之上。"
categories: ["Sector-Deep-Dive", "Korea Market"]
tags:
  - "AI PCB"
  - "AI基板"
  - "FC-BGA"
  - "MLB"
  - "CCL"
  - "智能体AI"
  - "具身AI"
  - "CPU需求"
  - "NVIDIA Vera Rubin"
  - "机架级AI"
  - "Samsung Electro-Mechanics"
  - "Daeduck Electronics"
  - "Doosan"
  - "Kolon Industries"
  - "Pamicell"
  - "韩国股票"
series: ["ai-pcb-substrate-thesis-2026"]
---

> <strong>行业地图：</strong> 本文是Pamicell系列研究的上层AI PCB与基板行业逻辑。建议结合 [AI PCB专题页](/page/korea-ai-pcb-substrate-hub/)、[Pamicell第一篇](/post/pamicell-doosan-electro-bg-proxy-rediscovery-2026-04-30/)、[Pamicell第二篇](/post/pamicell-four-layer-progress-and-fifth-cycle-layer-2026-05-03/) 以及此前的 [Samsung Electro-Mechanics AI基础设施重估报告](/post/samsung-electro-mechanics-ai-infrastructure-rerating-2026-04-21/) 一同阅读。

此前的公司层面研究聚焦于一个较窄的问题：哪些韩国标的在AI PCB、FC-BGA和低损耗材料供应中具备最佳位置？本文将视角上移一层，探讨为何资本应当首先进入这整个生态系统。

答案并非"基板是GPU之后的下一个主题"——这个逻辑过于线性。AI基础设施已不再是一张GPU卡，而是一套机架级系统。一台现代AI机架包含GPU、CPU、DPU、NIC、交换机ASIC、内存模块、电源管理、散热控制和高速电路板。每一个层级都在增加硅片，每一颗硅片都需要封装基板、模块板、主板、交换机板或低损耗材料叠层。

这正是核心所在：PCB与基板层不是简单轮动中的下一站，而是整个AI系统物料清单（BOM）的最大公约数。

---

## 核心摘要

1. 市场习惯的"GPU→内存→基板"轮动路径方向上没错，但不够完整。更准确的框架是同步系统扩张：GPU、HBM、CPU、DPU、NIC、交换机ASIC和内存模块同步增长，且全部需要基板或电路板。
2. NVIDIA Vera Rubin NVL72将这一逻辑具象化。该平台集成72颗Rubin GPU、36颗Vera CPU、NVLink 6交换、ConnectX-9 SuperNIC、BlueField-4 DPU以及Spectrum-X / Spectrum-6以太网扩展。CPU与GPU之比为0.5，即每两颗GPU对应一颗CPU。这已不再是单芯片故事。
3. 智能体AI（Agentic AI）提升了推理阶段的CPU强度。工具编排、检索、代码执行、数据库访问、内存管理与安全隔离均依赖CPU、DRAM、NIC和DPU。若CPU内容占比上升，服务器CPU的FC-BGA、内存模块板、SoCAMM、主板与低损耗CCL将全部受益。
4. 具身AI（Physical AI）将投资逻辑延伸至数据中心之外。自动驾驶车辆、人形机器人、工业机器人与航天电子均使用更多电路板、更多传感器、更多边缘AI模块以及更高可靠性要求的PCB材料。时间轴上，数据中心优先，自动驾驶其次，人形机器人较慢，航天作为高可靠性溢价赛道长期存在。
5. 对于韩国市场，可投资版图呈现出层次结构。Samsung Electro-Mechanics是高端FC-BGA与MLCC节点；Daeduck Electronics是FC-BGA / MLB / SoCAMM的因子候选；Doosan Electronic BG是CCL供应链锚点；Kolon Industries与Pamicell处于低介电材料的上游。Pamicell不只是一个独立标的，它是更大AI基板系统中的一个压缩代理。

---

## 1. 线性框架：有用，但格局太小

市场偏好线性叙事，因为轮动逻辑易于交易。

最先是GPU：加速卡稀缺，NVIDIA拿走了预算。接着是HBM：没有足够的内存带宽，GPU无法持续扩张，于是SK hynix、Samsung Electronics和Micron走向舞台中心。下一步通常被描述为基板或先进封装：GPU与HBM扩张之后，FC-BGA、interposer、MLB和CCL理应跟上。

这个框架并没有错。更大的GPU确实需要更大、更复杂的封装基板；HBM扩张会提升封装强度；服务器主板也越来越密集、速度越来越快。从这个角度看，基板确实在GPU和HBM之后才进入市场的认知周期。

但这个框架遗漏了系统架构中最重要的变化。2026年的AI基础设施已不是一堆GPU的堆砌，而是将计算、内存、网络、安全与系统控制协同设计的机架级平台。

NVIDIA Vera Rubin NVL72配置是最清晰的例证。NVIDIA公开资料描述的系统由72颗Rubin GPU与36颗Vera CPU构成，配备NVLink 6交换、ConnectX-9 SuperNIC和BlueField-4 DPU。NVIDIA自身的Rubin平台资料也将该平台定义为六芯片协同设计：Vera CPU、Rubin GPU、NVLink交换机、ConnectX-9 SuperNIC、BlueField-4 DPU以及Spectrum-6以太网交换机。

这组数字意义重大：

```text
Vera CPU  = 36
Rubin GPU = 72
CPU:GPU   = 36 / 72 = 0.5
```

每两颗GPU对应一颗CPU，绝非可以忽视的主机处理器脚注。它说明这台机架是一个系统，而非GPU货架。一旦承认这一点，基板投资逻辑就不再只是GPU需求的下游回响，而是升级为多芯片系统级命题。

---

## 2. 为何每颗芯片都会拉动一块电路板

理解基板层最直接的方式，是逐层梳理系统物料清单。

| 系统层级 | 芯片或模块 | 电路板/基板需求 |
|---|---|---|
| AI加速 | GPU、定制ASIC、TPU | 大型FC-BGA、先进封装基板、高密度电路板 |
| 主机与编排 | 服务器CPU、Vera CPU、x86 / Arm CPU | 大型FC-BGA、CPU插槽板、主板MLB |
| 内存带宽 | HBM、DDR5、基于LPDDR的服务器模块、SoCAMM | Interposer / 基板、内存模块PCB、信号完整性材料 |
| 网络互联 | NIC、SuperNIC、以太网交换机ASIC、InfiniBand交换机 | 交换机板、光模块PCB、低损耗MLB |
| 数据搬运与安全 | DPU、SmartNIC | 封装基板、加速卡PCB |
| 电源与控制 | VRM、电源模块、BMC及控制板 | 电源PCB、MLCC、高可靠性电路板 |

这正是"GPU需求"过于狭隘的原因。超大规模云厂商购买的不是一颗孤立的GPU，而是一套可运行的机架。机架中包含计算芯片、内存芯片、网络芯片、控制芯片和电源器件。系统规模越大，电路板层就需要承载越高速的信号、越高的热耗散、越大的功率和越严格的可靠性要求。

在这一框架下，韩国股票的对应关系也更为清晰：

| 韩国产业链层级 | 重点跟踪公司 | 代表什么 |
|---|---|---|
| 高端封装基板 | Samsung Electro-Mechanics、Daeduck Electronics、Korea Circuit | FC-BGA与封装基板敞口 |
| 多层板与模块PCB | Isu Petasys、Daeduck Electronics、TLB、Simmtech、Korea Circuit | 服务器主板、交换机板、内存模块及SoCAMM敞口 |
| CCL锚点 | Doosan Electronic BG | AI服务器与网络设备用高端覆铜板 |
| 低损耗材料 | Kolon Industries、Pamicell | mPPO / 低介电树脂与固化剂原材料 |
| 电源稳定性 | Samsung Electro-Mechanics及MLCC同业 | 每台AI服务器的MLCC用量及高压元器件结构 |

Pamicell在这张地图中的位置是Doosan Electronic BG的上游材料代理；Samsung Electro-Mechanics是FC-BGA加MLCC的韩国溢价龙头；Daeduck是更宽泛的FC-BGA / MLB / SoCAMM因子候选。它们不是彼此独立的故事，而是同一张系统BOM上的不同节点。

---

## 3. 智能体AI让CPU层更加重要

传统LLM推理从硬件视角看相当简单：

```text
输入提示词
  -> GPU前向传播
  -> 输出响应
```

智能体AI改变了工作负载的性质。模型不再只是给出答案，它需要规划、调用工具、搜索信息、读取文件、执行代码、查询数据库、管理记忆、验证输出，并可能协调其他智能体。GPU依然是核心，但非GPU部分的计算量大幅增加。

| 智能体功能 | 主要硬件拉动 |
|---|---|
| LLM前向传播 | GPU + HBM |
| 工具编排 | CPU |
| 检索与搜索 | CPU + DRAM + 存储 |
| 代码执行 | CPU、沙箱、编译器/解释器 |
| 会话记忆与状态管理 | CPU + DRAM |
| 网络化工具调用 | NIC + 交换机ASIC + PCB |
| 安全与隔离 | CPU + DPU |

TrendForce对此方向表达得相当明确。其2026年4月发布的智能体AI报告及相关公开评论描述了CPU:GPU比率的结构性变化，以及Intel和AMD在服务器CPU供应偏紧与涨价方面的趋势。Tom's Hardware也从行业侧报道了同一方向：在智能体推理场景下，原本每四到八颗GPU配一颗CPU的AI服务器配置，CPU强度可能大幅提升。

具体比率因工作负载而异——代码智能体集群与视频生成集群不同，检索密集型企业级智能体与纯批量推理系统也不同。但对于基板投资者而言，方向比比率本身更重要：CPU工作量增加，意味着更多CPU封装、更多围绕CPU的内存、更多网络互联，以及更高的板级信号完整性要求。

从智能体AI到韩国基板的传导路径如下：

```text
智能体AI普及
  -> CPU编排工作负载增加
  -> 服务器CPU、DPU、NIC与交换机ASIC用量上升
  -> 服务器CPU FC-BGA与高层MLB需求上升
  -> 内存模块、SoCAMM与主板复杂度提升
  -> 低损耗CCL与低介电材料愈发关键
  -> 韩国基板与材料公司获得BOM扩张中的对应份额
```

最后一行至关重要。韩国并不掌控CPU市场，Intel、AMD、Arm、NVIDIA和云厂商自研CPU拿走了芯片价值。韩国上市公司获取的是芯片周边的电路板与材料价值。这一价值依然有意义，因为基板内容随系统增长，而非随单一产品线波动。

---

## 4. 具身AI：走出数据中心

数据中心是近期最大、最直接的驱动力。具身AI是第二条扩张路径。时间轴更长，但方向一致：当智能移入车辆、机器人、工厂和卫星，更多算力将向边缘迁移。更多边缘算力意味着更多电路板。

### 自动驾驶

自动驾驶是最现实的第二增长极，因为汽车本身已经承载了庞大的电子堆栈。一辆具备高级驾驶辅助或自动驾驶功能的车辆，包含中央计算单元、传感器融合模块、摄像头、雷达、激光雷达、车载以太网和冗余安全控制器。

| 车载系统 | PCB与材料拉动 |
|---|---|
| 中央计算 | 高密度电路板、处理器封装基板 |
| 传感器融合ECU | 多层PCB、高速信号板 |
| 摄像头/激光雷达/雷达 | 刚挠结合板、射频板、模块PCB |
| 车载以太网 | 低损耗CCL与高速通信PCB |
| 安全冗余 | 更多ECU与更大板面积 |

这对盈利的拉动不如AI数据中心那么快速。整车项目周期长，资质认证缓慢，营收曲线依赖车型换代节奏。但方向并不模糊：一辆更智能的汽车携带的电路板价值远超传统车辆。

### 人形机器人与工业机器人

NVIDIA Jetson Thor为具身AI论点提供了具体的硬件参照。NVIDIA将Jetson Thor定位于物理AI与机器人领域，最高可提供2,070 FP4 TFLOPS算力、128GB内存，可配置功耗范围为40W至130W。这类边缘AI模块需要高密度电路板、电源板、传感器互联和柔性PCB。

人形机器人短期内不会驱动韩国基板的盈利。规模化量产尚未到来。但它扩展了这一逻辑的期权价值：若边缘AI模块在机器人、工厂与工业设备中实现标准化，电路板内容将从数据中心独家故事演变为分布式算力故事。

### 航天与国防电子

航天赛道性质不同，它不是量的故事，而是可靠性与利润率的故事。NASA及IPC相关任务硬件材料强调高可靠性PCB要求、供应商资质认证以及Class 3 / 航天附录级标准。对于韩国上市PCB企业而言，这不意味着"航天会吸纳大量产能"，而是严苛环境电子产品可能支撑更高可靠性标准，进而带来更好的利润率。

时间轴排序如下：

| 终端市场 | 盈利兑现时间 | PCB强度 | 实际置信度 |
|---|---|---|---|
| AI数据中心 | 快 | 极高 | 高 |
| 自动驾驶 | 中等 | 高 | 中高 |
| 人形机器人/工业机器人 | 慢 | 中至高 | 中等 |
| 航天/国防电子 | 慢 | 规格高、量小 | 中等 |

这一排序非常重要。近期模型仍应以数据中心为主导。具身AI不是今天拉伸所有估值的理由，而是说明终端市场的天花板可能远比当前AI服务器周期所暗示的更高。

---

## 5. 这对Pamicell论点的意义

Pamicell研究始于一个公司层面的认知错位：市场记住的是一家干细胞公司，而其损益表愈来愈像一家AI CCL材料供应商。与Doosan Electronic BG的供应合同证据、反复出现的高毛利生化产品，以及KRX行业分类重置，都指向同一方向。

行业层面的论点将问题从"为何是Pamicell？"转化为"上游CCL材料层究竟为何重要？"

答案在于：CCL与低损耗材料并不绑定于某一代GPU，它们处于系统层之下：

```text
GPU / CPU / DPU / NIC / 交换机ASIC扩张
  -> 高速信号与热管理约束提升
  -> 低损耗CCL需求上升
  -> CCL生产商需要低介电材料
  -> Pamicell等上游供应商成为压缩代理
```

Pamicell与Doosan Electronic BG终究不同，它也不是PCB制造商，而是位置更靠上游。这意味着客户集中度风险和资质认证风险是真实存在的。但这也意味着：在规模较小的基数上，如果订单持续复利增长，同样的系统级需求在百分比意义上可以显得更为强劲。

换句话说：如果AI电路板周期不只是GPU基板周期，而是多芯片系统基板周期，那么Pamicell的投资逻辑将更加持久。

---

## 6. 这对Samsung Electro-Mechanics论点的意义

Samsung Electro-Mechanics此前已围绕两个核心主题完成重估：高端FC-BGA与AI服务器MLCC。这一旧框架依然成立。系统BOM论点让逻辑更加清晰。

若唯一驱动力是GPU，Samsung Electro-Mechanics将只是一个附带MLCC的高端封装基板故事。若驱动力是机架级系统扩张，该公司则同时覆盖多条赛道：

| 赛道 | 为何重要 |
|---|---|
| FC-BGA | 更大、更复杂的CPU、GPU、ASIC和网络芯片需要高端封装基板 |
| MLCC | AI服务器、网络托盘与电源管理均提升元器件密度 |
| 玻璃基板选项 | 未来大封装架构可能需要新型基板材料与制程 |
| 汽车与机器人电子 | 具身AI长期提升高可靠性元器件与电路板需求 |

这并不免除估值纪律的约束。与Pamicell或部分较小的PCB标的相比，Samsung Electro-Mechanics已被市场更充分地认识。关键问题不是"这是不是一家好公司？"，而是"系统级基板扩张有多少已反映在价格中，有多少仍需通过订单、利润率和业绩指引来验证？"

这正是本文将Samsung Electro-Mechanics定位为溢价锚点而非最高弹性标的的原因。它是韩国大盘股中FC-BGA加MLCC的最清晰表达，但未来回报取决于持续的盈利预测上调，而非仅仅发现主题本身。

---

## 7. 组合框架：核心、杠铃与期权

公司排名会随股价变化，但因子地图是稳定的。

| 角色 | 候选敞口 | 理由 |
|---|---|---|
| 溢价锚点 | Samsung Electro-Mechanics | FC-BGA + MLCC + 客户资质 + 规模 |
| 核心PCB因子 | Daeduck Electronics | FC-BGA、MLB及潜在SoCAMM / 模块板敞口 |
| CCL锚点 | Doosan旗下Doosan Electronic BG | 国内产业链的高端CCL主体 |
| 上游材料杠铃 | Kolon Industries与Pamicell | 低介电树脂/材料敞口，基数小、经营杠杆高 |
| 期权价值 | Korea Circuit、TLB、Simmtech、Isu Petasys | 内存模块、MLB、网络互联及更宽泛AI PCB弹性 |

核心不在于强求唯一答案，而在于避免将所有"AI PCB"标的视为同质资产。封装基板、多层板、CCL与低介电化学品在利润率结构、认证周期和客户风险上各有不同。

一个实用的组合视角：

```text
溢价锚点：
  Samsung Electro-Mechanics

核心基板/电路板因子：
  Daeduck Electronics、部分MLB标的

上游材料杠铃：
  Kolon Industries + Pamicell

高弹性期权：
  Korea Circuit、TLB、Simmtech、Isu Petasys
```

当市场说"PCB周期结束了"，系统BOM框架有助于验证这一判断是否成立。如果GPU出货放缓，但CPU内容、网络ASIC、DPU和内存模块复杂度持续上升，电路板周期可能在某一赛道降温，同时在另一赛道保持紧张。

---

## 8. 什么可能打破这一逻辑

公约数框架并不是说周期永远持续。有四项风险值得关注。

第一，超大规模云厂商AI资本开支可能放缓。若AWS、Microsoft、Google或Meta连续超过一个季度下调指引，整条硬件供应链都将受到冲击。

第二，基板技术可能发生变革。玻璃基板或其他新型架构可能比预期更快地改变FC-BGA周期。这不会消除电路板需求，但可能改变受益者格局。

第三，产能可能集中释放。若高端CCL、玻璃纤维或低损耗材料的产能扩张快于预期，定价权可能在需求完全成熟之前提前正常化。

第四，具身AI的落地可能比市场预期更慢。自动驾驶、人形机器人和航天电子都有漫长的认证与采用周期，无法替代近期数据中心的营收贡献。

这些风险不会推翻这一逻辑，它们定义了需要持续追踪的清单。

---

## 9. 验证清单

应从系统层面跟踪论点，而非仅依赖某一家公司的单季数据。

| 信号 | 为何重要 |
|---|---|
| NVIDIA机架级路线图 | 更多芯片类型与更高机架密度延续公约数基板周期 |
| CPU:GPU比率评论 | 更高的CPU比率强化CPU FC-BGA与主板MLB这条腿 |
| 超大规模云厂商资本开支指引 | AI数据中心电路板需求的一阶来源 |
| CCL与玻璃纤维交货周期 | 确认材料紧张是真实存在还是已在缓解 |
| Samsung Electro-Mechanics封装与元器件利润率 | 验证溢价基板与MLCC定价是否仍能维持 |
| Daeduck / MLB订单评论 | 验证更宽泛的PCB弹性是否正在转化为营收 |
| Pamicell与Doosan Electronic BG合同节奏 | 验证上游CCL材料需求是否仍在复利增长 |
| 韩国上市公司IR中汽车/机器人PCB相关表述 | 具身AI从期权价值走向实际营收的早期信号 |

若上述信号持续对齐，这一基板周期将不只是2025—2027年的主题，而会成为跨越多年的系统架构转型。

---

## 常见问题

### AI PCB逻辑是什么？

AI PCB逻辑认为，AI基础设施需求已不局限于GPU与HBM。机架级系统需要GPU、CPU、NIC、DPU、交换机ASIC、内存模块和电源板。每一个层级都需要封装基板、多层板或低损耗材料。

### 为何智能体AI会增加CPU需求？

智能体AI需要工具调用、检索、代码执行、内存管理与任务编排，这些任务在GPU周边叠加了CPU、DRAM、网络与DPU的工作负载。CPU内容占比上升，可能带动服务器CPU FC-BGA、主板、内存模块板和低损耗CCL的需求增长。

### 为何Samsung Electro-Mechanics与Pamicell出现在同一行业地图中？

两者位于同一AI基板产业链的不同节点。Samsung Electro-Mechanics是溢价FC-BGA与MLCC节点；Pamicell是上游低介电材料供应商，通过Doosan Electronic BG的CCL周期与下游需求相连。同样的系统级AI电路板需求可以同时作用于两者，但风险特征与估值逻辑各有不同。

### Pamicell是PCB公司吗？

不是。Pamicell不是PCB制造商。相关论点的核心是上游材料敞口：Doosan Electronic BG等CCL生产商使用的低介电/低损耗原材料投入。

### 这是投资建议吗？

不是。本文是行业研究框架。正确的结论取决于估值、订单节奏、利润率验证、客户集中度以及每位投资者自身的风险承受能力。

---

## 主要公开来源

- NVIDIA Vera Rubin NVL72产品页：https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/
- NVIDIA技术博客，Vera Rubin平台概述：https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
- TrendForce，智能体AI与CPU:GPU比率评论：https://insights.trendforce.com/p/agentic-ai-cpu-gpu
- TrendForce报告，2026年智能体AI浪潮：https://www.trendforce.com/research/download/RP260408AD
- Tom's Hardware，智能体AI与CPU需求：https://www.tomshardware.com/pc-components/cpus/shifting-need-for-cpus-in-ai-workloads-drives-intensifying-shortages-price-hikes
- NVIDIA Jetson Thor产品页：https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- NASA高可靠性PCB标准质量指引：https://sma.nasa.gov/sma-disciplines/quality
- NASA GSFC-STD-8001高可靠性PCB标准：https://standards.nasa.gov/sites/default/files/standards/GSFC/Baseline/0/gsfc-std-8001.pdf

---

## 结语

这一逻辑最简洁的表述是：

AI采购的不是GPU，而是系统。

系统增加芯片。芯片需要基板、电路板和低损耗材料。

这正是为何基板层应被视为公约数式瓶颈，而非周期末段的补涨品。这并不意味着每一家韩国PCB或材料公司都值得相同的估值倍数，而是说整个生态系统应被视为系统级供应链来评估：Samsung Electro-Mechanics处于溢价FC-BGA / MLCC节点，Daeduck与MLB标的处于电路板层，Doosan Electronic BG处于CCL主体，Kolon Industries与Pamicell处于低介电材料上游。

接下来的工作不是重复主题，而是持续追踪系统BOM是否持续增厚，CPU与网络内容是否仍在上升，以及韩国企业能否将这种复杂度转化为订单与利润率。

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
