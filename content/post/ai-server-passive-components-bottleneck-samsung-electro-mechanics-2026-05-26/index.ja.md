---
title: "AIサーバーの受動部品ボトルネック：小さな電源安定部品がなぜ重要になったのか"
date: 2026-05-26
description: "AIサーバーのボトルネックはGPU不足だけではない。GPU/HBMの急激な電力変動を安定化するMLCC、シリコンキャパシタ、インダクタ、フィルタの高性能化が重要になっている。Samsung Electro-Mechanicsへの示唆を整理する。"
categories: ["Stock-Analysis"]
tags: ["Samsung Electro-Mechanics", "009150", "AI Server", "MLCC", "Silicon Capacitor", "FC-BGA", "Power Integrity", "HBM", "GPU"]
slug: ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26
valley_body_mode: teaser
valley_cashtags: ["삼성전기"]
valley_cashtag_exclude: ["삼성전자", "SK하이닉스"]
---

> Samsung Electro-Mechanicsシリーズの続編です。[時価総額100兆ウォン分析](/ja/post/samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26/)、[シリコンキャパシタ契約](/ja/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/)、[MLCCとシリコンキャパシタ](/ja/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/)も参照してください。

## TL;DR

- AIサーバーの受動部品ボトルネックとは、GPUが必要とする電力を安定化・緩衝・フィルタリングする小型部品の高性能化です。
- NVIDIA DGX GB200ラックは約<strong>120kW</strong>、Lenovo GB300 NVL72はラックあたり<strong>135kW TDP</strong>、最大<strong>155kWピーク</strong>が示されています。([NVIDIA][1], [Lenovo][2])
- MLCC、シリコンキャパシタ、インダクタは、AIサーバーの電気的ショックアブソーバーです。
- 投資上の焦点は汎用MLCCではなく、高容量・低ESR/ESL・低ノイズ・薄型のAIサーバー向け部品です。
- Samsung Electro-Mechanicsは<strong>MLCC + FC-BGA + シリコンキャパシタ</strong>を同時に持つ点が重要です。

## やさしい説明

AIサーバーをレーシングカーのエンジンだと考えると、GPUはエンジン、HBMは高速燃料タンク、基板は道路です。MLCCとシリコンキャパシタは、エンジンが揺れないようにする精密な燃料圧制御装置です。

TDKはデータセンターの電源経路を <strong>UPS → PSU → IBC → VRM → CPU/GPU電圧</strong> と説明しています。各段階で効率、低リップル、耐熱性、長期信頼性が必要です。([TDK][3])

Samsung Electro-Mechanicsは、GPU/CPUは1V未満で動作し、電流が数十〜数百アンペア単位で急変し得るため、GPU近くの高容量MLCCが電流バッファとして必要になると説明しています。([Samsung Electro-Mechanics][4])

## MLCCとシリコンキャパシタ

| 部品 | 位置 | 役割 |
|---|---|---|
| MLCC | 基板上、チップ周辺 | 広範囲の電源安定化 |
| シリコンキャパシタ | GPU/HBMパッケージ内部または近傍 | 超近接の瞬間電力変動抑制 |

Samsung Electro-Mechanicsは2027〜2028年にかけて約<strong>1.5兆ウォン</strong>規模のシリコンキャパシタ供給契約を発表しました。同社はこの部品がAIサーバー用高性能半導体パッケージ内部の電源安定性を高めると説明しています。([Samsung Electro-Mechanics][8])

## 投資示唆

論点は「MLCC全体」ではありません。

```text
ラック電力の上昇
  → 瞬間的な電力変動の拡大
  → GPU/HBM近傍のpower integrity需要
  → 高級MLCC、FC-BGA、シリコンキャパシタの価値上昇
```

見るべき指標は、AIサーバー向けMLCCのASP、2027年以降のシリコンキャパシタ売上、追加顧客、AIサーバー/ネットワーク向けFC-BGA、全社営業利益率です。

[1]: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[2]: https://lenovopress.lenovo.com/lp2357-lenovo-nvidia-gb300-nvl72-rack-scale-ai
[3]: https://product.tdk.com/en/techlibrary/applicationnote/mlcc-solution-for-data-center-psu.html
[4]: https://product.samsungsem.com/product-news/view.do?idx=3622&language=en
[5]: https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/
[6]: https://www.thelec.net/news/articleView.html?idxno=5588
[7]: https://product.samsungsem.com/product-news/view.do?idx=3742&language=en
[8]: https://m.samsungsem.com/kr/newsroom/news/view.do?id=10309
