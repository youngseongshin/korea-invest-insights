---
title: "AIインフラのマルチプル地図：なぜSamsung Electronicsは安く、Samsung Electro-Mechanicsは高く見えるのか"
date: 2026-05-31T09:00:00+09:00
description: "GPU、HBM、CPU、MLCC、FC-BGAは同じAIインフラサイクルに属するが、同じマルチプルを受けるわけではない。価格決定力、長期契約、顧客ロックイン、capex負担、ピーク利益疑念で分解する。"
categories: ["Market-Outlook"]
tags:
  - "AIインフラ"
  - "バリュエーション"
  - "HBM"
  - "GPU"
  - "MLCC"
  - "FC-BGA"
  - "Samsung Electronics"
  - "Samsung Electro-Mechanics"
  - "SK hynix"
  - "Nvidia"
  - "韓国半導体"
slug: ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31
valley_cashtags:
  - 삼성전자
  - 삼성전기
  - SK하이닉스
draft: false
---

> 文脈
> 本稿は、[Samsung Electronicsのメモリ・スーパーサイクル論](/ja/post/samsung-electronics-stock-bonus-supercycle-buyback-2026-05-27/)と、[Samsung Electro-MechanicsのMurata / Ibiden比プレミアム論](/ja/post/samsung-electro-mechanics-market-cap-murata-ibiden-premium-2026-05-28/)をつなぐ記事です。同じAIサイクルの中で、なぜ各レイヤーのマルチプルが違うのかを整理します。

## TL;DR

市場は単なる「AIエクスポージャー」には同じマルチプルを払いません。重要なのは<strong>利益の持続性、価格決定力、顧客ロックイン、供給能力リスク、ピーク利益への疑念</strong>です。

現在のリスクは、MLCC / FC-BGAのボトルネック銘柄をGPU/HBMのような構造的独占として評価してしまうことです。ボトルネックであることと、NVIDIA型のプラットフォーム・マルチプルを受けることは別です。

相対価値で最も強いアイデアは<strong>Samsung Electronics</strong>です。HBMキャッチアップ、メモリ価格、ファウンドリ・オプションを持ちながら、入力資料の2026年5月29-30日公開データではforward P/E約7.8倍、P/B約4.4倍です。一方、Samsung Electro-Mechanicsは論理は正しいものの、株価はすでにかなり先を織り込んでいます。([Yahoo Finance][1])

## 1. 基本式

```text
マルチプル・プレミアム
= 価格決定力 × 需要の持続性 × 顧客ロックイン × FCF転換率

マルチプル・ディスカウント
= 増設capex負担 × 供給過剰リスク × ピーク利益疑念 × 顧客集中
```

| レイヤー | プレミアム要因 | 上限要因 | 重要な問い |
|---|---|---|---|
| GPU / platform | CUDA、rack-scale system、software、asset-light | custom ASIC、中国規制、hyperscaler交渉力 | 顧客は時間を買うのか、チップを買うのか |
| HBM | HBM4、sold-out、LTA、搭載量増加 | メモリサイクル疑念、capex、供給多様化 | 契約型フランチャイズか、循環利益か |
| CPU | AIサーバー増加、orchestration | ARM / 自社CPUによる代替 | 主ボトルネックか、補助部品か |
| FC-BGA | 大面積・多層基板、認証難度 | capex、減価償却、ABF過剰供給の記憶 | capexはLTA/前払いで支えられるか |
| MLCC / Si-Cap | 電源安定性、高信頼部品 | 汎用MLCCサイクル、競争 | 出荷阻害要因か、単なる受動部品か |

## 2. レイヤー別の読み方

NVIDIAの高マルチプルはGPU単体ではなく、GPU、networking、software、参照アーキテクチャ、AI factory全体を握っている点にあります。FY2027 Q1売上は816億ドル、Data Centerは752億ドル、Q2ガイダンスは910億ドルでした。([NVIDIA Investor Relations][2])

HBMは非常に強い利益を出していますが、まだメモリ循環株として割り引かれています。LTAが価格・数量・capex回収を固定するほど、commodity DRAMではなくhigh-value memory franchiseとして評価されます。

CPUは必要ですが、主ボトルネックではありません。AMDはData Centerで伸びていますが、高いマルチプルにはEPYCとInstinctの同時成功が必要です。Intelは実行証拠が先です。

FC-BGAとMLCCは正しいテーマです。Samsung Electro-MechanicsはQ1 2026でAIサーバーMLCCとAI accelerator / server CPU向けFC-BGAを成長要因に挙げ、2027-2028年の約1.5兆ウォンSi-Cap契約も発表しました。([Samsung Electro-Mechanics][7], [Samsung Electro-Mechanics][8])

ただし価格は重要です。ResearchAndMarketsはFC-BGA市場を2026年24.6億ドルから2032年37.4億ドル、CAGR 7.1%と見ています。この成長率だけで100倍P/Eを正当化するのは難しいです。([Research and Markets][9])

## 3. Samsung Electronics vs Samsung Electro-Mechanics

Samsung ElectronicsはHBM4E、DDR5、SOCAMM2、eSSD / KV-cache、Samsung Foundryを持つため、AI推論のmemory hierarchy全体へのオプションです。

Samsung Electro-MechanicsはMLCC + FC-BGA + Si-Capを同時に持つ希少企業です。ただし現在の株価を支えるには、新規Si-Cap顧客、Si-Cap margin、AI向けMLCC ASP、FC-BGA稼働率、LTAの証拠が必要です。

## 4. 実践的判断

| 銘柄 | 判断 | 理由 |
|---|---|---|
| Samsung Electronics | Under / 買い候補 | HBM catch-upとメモリoptionに対して低マルチプル |
| NVIDIA | Fairから相対的under | 成長とmarginがまだ支える |
| SK hynix | fundamental under、タイミング待ち | HBM純度は高いがP/Bと上昇後リスク |
| Samsung Electro-Mechanics | over / 追いかけない | thesisは正しいが価格が先行 |
| Murata / Ibiden | over | ボトルネックは本物だが独占級評価 |

最大のミスは、NVIDIAサプライチェーンに入ったという理由だけで全ての部品株にプラットフォーム・マルチプルを与えることです。

[1]: https://finance.yahoo.com/quote/005930.KS/key-statistics/ "Samsung Electronics valuation"
[2]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx "NVIDIA FY2027 Q1 results"
[7]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Q1 2026"
[8]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics silicon capacitor contract"
[9]: https://www.researchandmarkets.com/reports/6128754/fc-bga-market-global-forecast "FC-BGA market forecast"
