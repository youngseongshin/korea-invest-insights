---
title: "AI服务器被动元件瓶颈：为什么小型电源稳定部件变得重要"
date: 2026-05-26
description: "AI服务器的瓶颈不只是GPU短缺，而是稳定GPU/HBM瞬时供电所需的高规格MLCC、硅电容、电感与滤波元件。本文解释这一瓶颈及其对三星电机的意义。"
categories: ["Stock-Analysis"]
tags: ["Samsung Electro-Mechanics", "009150", "AI Server", "MLCC", "Silicon Capacitor", "FC-BGA", "Power Integrity", "HBM", "GPU"]
slug: ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26
valley_body_mode: teaser
valley_cashtags: ["삼성전기"]
valley_cashtag_exclude: ["삼성전자", "SK하이닉스"]
---

> 这是三星电机系列的后续文章。可先阅读[三星电机市值100万亿韩元](/zh/post/samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26/)、[硅电容1.5万亿韩元合同](/zh/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/)和[MLCC与硅电容](/zh/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/)。

## TL;DR

- AI服务器被动元件瓶颈不是GPU短缺，而是GPU消耗巨大且快速变化的电流后，电源稳定部件需要更高规格。
- NVIDIA DGX GB200机架约消耗**120kW**；Lenovo GB300 NVL72机架为**135kW TDP**、最高**155kW峰值**。([NVIDIA][1], [Lenovo][2])
- MLCC、硅电容、电感相当于AI服务器的电气减震器和滤波器。
- 投资重点不是普通MLCC，而是高容量、低ESR/ESL、低噪声、低高度的AI服务器高端部件。
- 三星电机的价值在于同时拥有**MLCC + FC-BGA + 硅电容**。

## 简单解释

如果AI服务器是一台赛车发动机，GPU是发动机，HBM是高速油箱，基板是道路，MLCC和硅电容就是防止发动机抖动的精密燃压控制装置。

TDK把数据中心供电链描述为 **UPS → PSU → IBC → VRM → CPU/GPU电压**，每一层都需要高效率、低纹波、耐热和长期可靠性。([TDK][3])

三星电机说明，GPU/CPU通常在1V以下运行，而电流可能随负载以数十到数百安培快速变化，因此GPU附近的高容量MLCC必须充当电流缓冲器。([Samsung Electro-Mechanics][4])

## MLCC与硅电容

| 元件 | 位置 | 作用 |
|---|---|---|
| MLCC | 主板和芯片周边 | 大范围电源稳定 |
| 硅电容 | GPU/HBM封装内部或附近 | 超近距离抑制瞬态电源波动 |

三星电机宣布了约**1.5万亿韩元**、覆盖<strong>2027-2028年</strong>的硅电容供应合同。公司称该产品用于提升AI服务器高性能半导体封装内部的供电稳定性。([Samsung Electro-Mechanics][8])

## 投资含义

核心不是“所有MLCC都上涨”，而是：

```text
机架功耗上升
  → 瞬时电流波动加大
  → GPU/HBM附近的电源完整性需求上升
  → 高端MLCC、FC-BGA、硅电容价值上升
```

需要跟踪的指标包括：AI服务器MLCC ASP、2027年后硅电容收入确认、追加客户或平台、AI服务器/网络FC-BGA增长，以及公司整体营业利润率。

[1]: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[2]: https://lenovopress.lenovo.com/lp2357-lenovo-nvidia-gb300-nvl72-rack-scale-ai
[3]: https://product.tdk.com/en/techlibrary/applicationnote/mlcc-solution-for-data-center-psu.html
[4]: https://product.samsungsem.com/product-news/view.do?idx=3622&language=en
[5]: https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/
[6]: https://www.thelec.net/news/articleView.html?idxno=5588
[7]: https://product.samsungsem.com/product-news/view.do?idx=3742&language=en
[8]: https://m.samsungsem.com/kr/newsroom/news/view.do?id=10309
