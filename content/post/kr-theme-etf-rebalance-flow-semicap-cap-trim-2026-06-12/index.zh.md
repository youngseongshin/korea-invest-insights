---
title: "韩国主题ETF再平衡资金流：半导体二线股获再分配买盘，龙头股面临权重上限压力"
date: 2026-06-12T17:40:00+09:00
description: "KR Theme ETF Rebalance Flow v1首次运行显示，韩国主题ETF定期调整和权重上限再平衡可能带来机械性资金流。2026年6月12日，最强信号集中在半导体设备和材料股。"
categories: ["Korean-Equities", "Market-Flow", "ETF-Flow"]
tags: ["韩国ETF", "ETF再平衡", "半导体", "被动资金流"]
series: ["korea-rerating-2026", "korea-market-flow"]
slug: "kr-theme-etf-rebalance-flow-semicap-cap-trim-2026-06-12"
draft: false
---

## TL;DR

- Thesis OS新增 **KR Theme ETF Rebalance Flow v1**，用于跟踪韩国主题ETF定期调整和成分股权重上限变化带来的机械性资金流。
- 首次运行扫描 **31只ETF**，其中 **30只有效**，处理 **291行成分股**，生成 **69个候选信号**。
- 其中 **60个为再分配买盘候选**，**9个为权重上限削减候选**。
- 最强信号不是核电/SMR，而是 **半导体设备和材料**。
- Leeno Industrial、EO Technics、Soulbrain、DB HiTek、Hanmi Semiconductor、ISC、Wonik IPS位居前列。

## 1. 这个监控在衡量什么

监控估算ETF内部权重再分配代理指标：

```text
ETF层面资金流 = ETF NAV × 目标权重变化
个股资金流 = 多个ETF资金流合计
强度 = 估算资金流 / 20日平均成交额
```

数据来自Naver ETF surface的`constituentList`和`totalNav`，以及本地价格数据库。如果某个成分股超过假设权重上限，模型会将其降至上限，并把超额部分按当前权重分配给低于上限的成分股。

这不是官方PCF数据。若要作为交易信号，必须核对发行方PDF/PCF、指数方法论、真实cap rule以及收盘集合竞价成交数据。

| 项目 | 数值 |
|---|---:|
| 日期 | 2026-06-12 |
| 扫描ETF | 31 |
| 有效ETF | 30 |
| 成分股行数 | 291 |
| 候选总数 | 69 |
| 再分配买盘 | 60 |
| 权重上限削减 | 9 |
| 置信度 | 中低 |

## 2. 再分配买盘候选

| 公司 | 估算资金流 | Flow/ADV20 | 当日涨跌 |
|---|---:|---:|---:|
| Leeno Industrial | 2704亿韩元 | +2.68x | +4.7% |
| EO Technics | 1978亿韩元 | +2.49x | +21.4% |
| Soulbrain | 694亿韩元 | +2.44x | +24.4% |
| DB HiTek | 2643亿韩元 | +2.02x | +12.3% |
| Hanmi Semiconductor | 7210亿韩元 | +1.81x | +24.1% |
| ISC | 920亿韩元 | +1.76x | +20.7% |
| Wonik IPS | 2111亿韩元 | +1.63x | +30.0% |

重点不是绝对金额，而是相对于流动性的强度。半导体二线股可能比大型龙头更容易受到ETF机械性资金流影响。

## 3. 权重上限削减候选

| 公司 | 估算资金流 | Flow/ADV20 | 解读 |
|---|---:|---:|---|
| SK Hynix | -1.76万亿韩元 | -0.15x | 技术性压力，不等于做空论据 |
| Samsung Electronics | -493亿韩元 | -0.00x | 相对影响有限 |
| Samsung Electro-Mechanics | -5149亿韩元 | -0.21x | 需关注技术性卖压 |
| LS ELECTRIC | -470亿韩元 | -0.15x | 未确认前不宜追高 |
| Doosan Enerbility | -265亿韩元 | -0.07x | 核电主题观察项 |

cap trim不等于自动卖出。如果价格能承受机械性卖压，反而说明真实需求较强。

## 4. 使用纪律

| 步骤 | 需要确认 |
|---|---|
| 1 | ETF官方PDF/PCF |
| 2 | 指数方法论和真实cap rule |
| 3 | 收盘成交和集合竞价成交额 |
| 4 | T+1/T+3相对强度 |
| 5 | 程序、外资或机构资金流同向 |

## 结论

首次运行显示，韩国主题ETF再平衡中最清晰的信号是 **半导体二线股再分配**。这是有用的观察列表，但在官方数据和实际成交验证前，仍应视为中低置信度的辅助信号。
