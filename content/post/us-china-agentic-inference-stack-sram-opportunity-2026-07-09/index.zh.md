---
title: "中美智能体推理基础设施分化与SRAM机会"
date: 2026-07-09T17:20:00+09:00
description: "梳理美国和中国AI推理基础设施为何走向分化，以及电力、HBM、SRAM/LPU、先进封装和韩国上市公司的投资映射。"
categories: ["Theme-Analysis", "Korea Semiconductors", "AI Infrastructure"]
tags: ["AI推理", "智能体AI", "SRAM", "LPU", "HBM", "Vera Rubin", "LPX", "Samsung Electronics", "SK hynix", "HD Hyundai Electric", "Hanmi Semiconductor"]
slug: us-china-agentic-inference-stack-sram-opportunity-2026-07-09
series: ["hbm", "exclusive-analysis"]
valley_cashtags: ["005930.KS", "000660.KS", "267260.KS", "010120.KS", "298040.KS", "042700.KS", "NVDA"]
draft: false
---

## 摘要

美国和中国都在扩大AI推理基础设施，但两边解决的瓶颈并不相同。美国的核心约束是电力、机架密度、HBM、先进封装和每兆瓦token吞吐。中国的核心约束是先进逻辑芯片和HBM获取，因此更可能依赖Ascend、光互连、并行扩展和国产存储层级。

对韩国上市公司来说，最清晰的机会不是简单押注中国光模块。更直接的落点在美国式AI factory瓶颈: HBM4/HBM4E、电力设备、HBM封装设备，以及三星电子在SRAM/LPU代工、AI存储和存储层级上的低估期权。

## 1. 哪些判断可以验证

本文从YS-VC关于中美AI推理堆栈分化的文章出发。核心判断大体成立: AI推理已经不是简单的GPU故事，而是不同地区在解决不同物理约束。

| 判断 | 评估 | 投资含义 |
|---|---|---|
| 中美AI推理堆栈正在分化 | 基本正确 | 美国优化电力和机架效率，中国绕开先进逻辑和HBM限制 |
| 美国走向GPU/HBM/SRAM的rack-scale推理 | 正确 | Vera Rubin、LPX、HBM4、SRAM/LPU进入同一系统 |
| 中国使用Ascend、光互连和自有存储层级 | 部分正确 | 方向合理，但CloudMatrix性能仍需独立验证 |
| 美国出口管制限制中国获得NVIDIA数据中心compute | 正确 | 中国难以稳定获得最高端GPU和HBM |
| HBM仍是关键控制点 | 正确 | BIS将HBM视为大规模AI训练和推理的重要品类 |

## 2. 为什么两套基础设施会分化

智能体AI会显著增加token数量。代码智能体、研究智能体、语音智能体和企业流程智能体会读取长上下文、调用工具、解释结果并再次生成回答。因此prefill、decode、KV cache、存储、网络和电力都会成为瓶颈。

| 项目 | 美国 | 中国 |
|---|---|---|
| 主要约束 | 电力、机架密度、变压器、HBM4、先进封装 | 先进逻辑、HBM获取、出口管制 |
| 架构方向 | Vera Rubin、LPX/LPU、HBM4、高功率AI机架 | Huawei Ascend、光互连、并行扩展 |
| 优势 | 最高端GPU、HBM和封装生态 | 电力扩张较快、国家主导基础设施 |
| 弱点 | 电网接入、供电时间、变压器交期 | 缺乏EUV先进逻辑、HBM受限 |
| 韩国股票映射 | HBM、电力设备、HBM设备、代工 | 若无供应商证据则有限 |

IEA预计数据中心电力需求到2030年可能达到约945TWh。([IEA][1]) Energy Connects引用BloombergNEF称，中国未来五年可能新增超过3.4TW发电能力，接近美国的六倍。([Energy Connects][2]) 所以美国更需要优化每MW token吞吐，而中国更容易通过基础设施扩张来缓冲。

## 3. 美国堆栈: HBM加SRAM/LPU

NVIDIA将LPX描述为Vera Rubin的推理加速器。Rubin GPU使用HBM，Groq 3 LPX使用基于SRAM的LPU。([NVIDIA LPX][3])

| 指标 | NVIDIA LPX披露 |
|---|---:|
| 智能体系统token负载 | 最高15倍 |
| Vera Rubin NVL72 + LPX | 每MW throughput最高35倍 |
| 每个LPU accelerator SRAM | 500MB |
| 每个LPU accelerator SRAM带宽 | 150TB/s |
| LPX rack | 256个LPU芯片 |
| 每个LPX rack SRAM | 128GB |
| 每个LPX rack DDR5 | 12TB |
| rack SRAM带宽 | 40PB/s |

这不是HBM替代逻辑。HBM仍然是Rubin GPU的核心。SRAM/LPU补充HBM，用于对延迟敏感的decode阶段。

## 4. 中国堆栈是竞争信号，不是韩国股票的直接交易

如果中国无法自由获得最高端GPU和HBM，那么连接更多芯片、强化互连、使用光互连是合理选择。但这并不自动给韩国企业带来收入。中国AI供应链正在本土化，CloudMatrix等系统的性能、故障率和总拥有成本仍需要独立证据。

## 5. 韩国上市公司映射

| 层级 | 瓶颈 | 韩国公司 | 判断 |
|---|---|---|---|
| HBM4/HBM4E | Vera Rubin和AI服务器内存 | SK hynix, Samsung Electronics | 结构受益。SK hynix领先，Samsung是追赶期权 |
| SRAM/LPU代工 | 低延迟decode加速器 | Samsung Electronics | 收入尚不清晰，但期权重要 |
| AI存储/KV cache | eSSD、PCIe 6.0、智能体记忆 | Samsung Electronics, FADU | HBM下方的存储层扩展 |
| HBM设备 | TC bonder、先进封装 | Hanmi Semiconductor | 真瓶颈，但客户和估值重要 |
| 电力设备 | 变压器、开关设备、电网连接 | HD Hyundai Electric, LS ELECTRIC, Hyosung Heavy | 直接暴露于美国数据中心电力瓶颈 |
| 中国光互连 | 中国AI集群光模块 | 韩国直接证据有限 | 无供应链证据则回避 |

## 6. 实际投资判断

| 优先级 | 暴露 | 判断 |
|---:|---|---|
| 1 | Samsung Electronics | 若HBM4E、SRAM/LPU和AI存储开始体现在数字中，则为条件型买入候选 |
| 2 | HD Hyundai Electric | 等待。质量高，但订单动能已被市场看到 |
| 3 | SK hynix | 等待。HBM领先，但交易拥挤 |
| 4 | Hanmi Semiconductor | 观察名单。需要重复订单和客户多元化 |
| 5 | 中国光互连受益股 | 无直接证据则回避 |

韩国机会不是“中国光互连”，而是美国AI factory瓶颈: 电力、HBM、SRAM/LPU、先进封装和存储层级。SK hynix可能拥有最强业务位置，HD Hyundai Electric可能拥有最纯粹的电力设备暴露。但如果市场不再只把Samsung Electronics看作HBM落后者，而开始同时定价HBM4E、SRAM/LPU代工和AI存储，那么它可能是更具不对称性的重估候选。

## 来源

- [YS-VC](https://www.ys-vc.com/blog/us-china-ai-inference-stack-divergence)
- [IEA](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
- [Energy Connects](https://www.energyconnects.com/news/renewables/2026/february/china-ramps-up-energy-boom-flagged-by-musk-as-key-to-ai-race/)
- [NVIDIA LPX](https://www.nvidia.com/en-us/data-center/lpx/)
- [Samsung Newsroom](https://news.samsung.com/global/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026)
- [BIS](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military)
- [Yonhap](https://en.yna.co.kr/view/AEN20260128002800320)
- [The Elec](https://www.thelec.net/news/articleView.html?idxno=11132)
- [Seoul Economic Daily](https://en.sedaily.com/finance/2026/07/06/hd-hyundai-electric-raises-2026-order-target-23-percent-on)
