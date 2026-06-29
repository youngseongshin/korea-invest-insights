---
title: "サムスン電子2Q26プレビュー: Micronサプライズは消え、焦点はCore OPへ"
date: 2026-06-29T14:35:00+09:00
description: "Micron FY3Q26サプライズ後のサムスン電子2Q26プレビュー。韓国メモリー株の価格反応、DRAM価格、成果給引当金、reported OPとCore OP、3Q26持続性、バリュエーション、無効化条件を整理する。"
categories: ["Exclusive Analysis", "韓国半導体", "決算"]
tags:
  - "Samsung Electronics"
  - "SK Hynix"
  - "Micron"
  - "HBM"
  - "DRAM"
  - "NAND"
  - "Core OP"
series: ["exclusive-analysis", "hbm", "sam-hama-parity"]
slug: "samsung-2q26-preview-micron-surprise-erased-core-op-hbm-2026-06-29"
draft: false
---

> 関連文脈
> 本稿は [Micron FY3Q26決算](/post/micron-fy3q26-ai-memory-sca-fcf-hold-2026-06-25/)、[NVIDIAの株価弾性から見たサムスン・SKハイニックス](/post/nvidia-earnings-elasticity-hbm-cycle-samsung-hynix-2026-06-28/)、[サムスン・ハイニックス・Micronパリティ](/post/samsung-hynix-micron-forward-per-parity-memory-catch-up-2026-06-03/)、[HBM4E 12段競争](/post/samsung-sk-hynix-hbm4e-12h-sample-allocation-battle-2026-06-18/) の続編である。

## TL;DR

サムスン電子2Q26で見るべき数字は、単純なreported OPではない。会計上のOPと、<strong>成果連動報酬のcatch-up引当金を足し戻したCore OP</strong>を分けて見る必要がある。

現時点の株価を見る限り、Micron FY3Q26サプライズは韓国メモリー株にほとんど残っていない。Micronは6月26日時点で決算前比+8.0%を維持した一方、サムスン電子は6月29日場中価格で6月24日終値比-5.9%、SKハイニックスは-0.5%だった。6月25日の反応は本物だったが、ほぼ消えた。

サムスン電子の2Q26 DRAM価格は下方修正要因ではない。Conventional DRAMは+58-63% QoQ、mobile LPDDRは+70-83% QoQと推定される。したがって、サムスンのblended DRAM ASPがQoQで50%台後半という前提は過度ではない。

2Q26 reported OPの妥当レンジは87-92兆ウォン、中心値は89.5兆ウォンと見る。成果給catch-up引当金15-17兆ウォンを足し戻すと、Core OPは104-106兆ウォンになる。つまり「100兆ウォン期待から89兆ウォンへ減益」ではなく、「メモリー本業は100兆ウォン超の利益体力に到達したが、超過利益共有コストを2Qで認識する」という解釈が近い。

判断は <strong>Watchlist / Conditional Buy</strong>。条件は、reported OPが87兆ウォン以上、Core OPが102兆ウォン以上、下方修正の理由がDRAM/NANDの価格や出荷ではなく引当金で説明できること、そして3Q26 OPが100兆ウォン前後で維持できることだ。

## 1. Micronサプライズは価格に残っているか

Micronは2026年6月24日の米国市場引け後にFY3Q26を発表した。韓国市場での基準価格は6月24日終値とするのが自然だ。

| 銘柄 | 6/24終値 | 6/25終値 | 6/26終値 | 6/29場中 | 6/24比 |
|---|---:|---:|---:|---:|---:|
| Samsung Electronics | 340,500ウォン | 358,500ウォン | 339,500ウォン | 320,500ウォン | -5.9% |
| SK Hynix | 2,580,000ウォン | 2,917,000ウォン | 2,673,000ウォン | 2,568,000ウォン | -0.5% |
| Micron | 1,048.51ドル | 1,213.56ドル | 1,132.33ドル | DB最新6/26 | +8.0% |

出所: KIIローカル日次価格DB、6月29日場中価格はNaver Finance API 13:19 KST。

SKハイニックスは6月25日に+13.1%と最も素直に反応したが、ほぼ元の水準に戻った。サムスン電子は6月25日に+5.3%反応した後、決算前水準を下回った。Micronは6月26日時点でも+8.0%を維持した。したがって現在価格では、Micronのread-throughは韓国メモリー株に十分残っていない。

## 2. Micronが確認したこと

Micron FY3Q26はAI memory cycleの強さを確認した。売上高414.56億ドル、non-GAAP EPS 25.11ドル、non-GAAP gross margin 84.9%、FY4Q26ガイダンスは売上高500億ドル、EPS 31.00ドルだった。 [Micron FY3Q26](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html)

| Micronのシグナル | サムスン・SKハイニックスへの意味 |
|---|---|
| 売上414.56億ドル、GM 84.9% | 価格、ミックス、供給不足によるレバレッジが強い。 |
| FY4Q売上500億ドル、EPS 31ドル | 価格や出荷がすぐに崩れる局面ではない。 |
| データセンター売上250億ドル超 | AI memory需要はHBMだけではない。 |
| HBM4/HBM4E | 2027年配分と顧客認証が次の競争点。 |
| Strategic Customer Agreements | 従来のメモリー循環ディスカウントを下げる可能性。 |

## 3. Reported OPとCore OP

```text
Reported OP = 会計上の営業利益
Core OP = Reported OP + 成果連動報酬のcatch-up引当金
```

| 項目 | Base case |
|---|---:|
| Reported OP | 89.5兆ウォン |
| catch-up引当金 | 15-17兆ウォン |
| Core OP | 104-106兆ウォン |

重要なのは、OP下方修正の理由がDRAM/NANDではないことだ。入力レポートでは、Kiwoomが2Q26 OPを100兆ウォンから89兆ウォンへ下げた一方、DRAM ASP前提は+55% QoQから+58% QoQへ、NANDは+72%から+75%へ上がっている。下方修正は、成果給引当、非メモリー、DXコスト、Foundry/S.LSI損失で説明するのが自然だ。

## 4. 1Q26公式ベース

| 項目 | 1Q26 |
|---|---:|
| 全社売上 | 133.9兆ウォン |
| 全社OP | 57.2兆ウォン |
| DS売上 | 81.7兆ウォン |
| DS OP | 53.7兆ウォン |

出所: [Samsung Electronics 1Q26 results](https://news.samsungsemiconductor.com/global/samsung-electronics-announces-first-quarter-2026-results/).

## 5. DRAM価格

| 製品 | 2Q26価格動向 | 解釈 |
|---|---:|---|
| Conventional DRAM | +58-63% QoQ | +58%前提は高すぎない。 |
| PC DDR5 | +43-48% QoQ | PC需要が強くなくても価格は上昇。 |
| PC DDR4 | +35-40% QoQ | DDR5より弱いが十分強い。 |
| Mobile LPDDR4X | +70-75% QoQ | blended ASPを押し上げる。 |
| Mobile LPDDR5X | +78-83% QoQ | サムスンに有利。 |
| Consumer DRAM | +45-50% QoQ | 価格抵抗はあるが上昇。 |

## 6. 解釈マトリクス

| Reported OP | 引当金 | Core OP | 解釈 | アクション |
|---:|---:|---:|---|---|
| 92兆ウォン以上 | 約15兆ウォン | 107兆ウォン以上 | 明確なbeat | Buy可能 |
| 89-92兆ウォン | 約15兆ウォン | 104-107兆ウォン | in-line positive | 弱い日に買い |
| 87-89兆ウォン | 約15兆ウォン | 102-104兆ウォン | コンセンサス圏 | 段階的エントリー |
| 84-87兆ウォン | 約15兆ウォン | 99-102兆ウォン | 弱いmiss | 説明が必要 |
| 84-87兆ウォン | 25-35兆ウォン | 109-122兆ウォン | headline missでも年次前倒しなら中立からポジティブ | 費用の性質を確認 |
| 80-84兆ウォン | 約15兆ウォン | 95-99兆ウォン | bonusだけでは説明困難 | Waitまたは縮小 |
| 80兆ウォン未満 | 任意 | 意味なし | thesis毀損 | Avoid |

## 7. Catalystと無効化条件

| イベント | 時期 | 確認点 |
|---|---|---|
| サムスン2Q26速報 | 7月上旬の可能性 | reported OP 87兆ウォン以上 |
| 確定決算とcall | 7月下旬の可能性 | 引当金、DS core、3Q outlook |
| 3Q DRAM/NAND価格 | 7-8月 | QoQ flatまたは上昇 |
| HBM4E, SOCAMM2, eSSD | 2H26 | share gainの証拠 |
| Micron FY4Q26 | 9月下旬の可能性 | 売上500億ドル、EPS 31ドル達成 |

無効化条件は、Core OPが100兆ウォン未満、3Q outlookが100兆ウォン未満、DRAM/NAND価格のQoQ下落、HBM4/eSSDでのシェア獲得不足、Foundry/S.LSI損失の継続だ。

## 結論

Micronサプライズは6月25日に韓国メモリー株へ反映されたが、ほぼ消えた。特にサムスン電子は、そのread-throughをほとんど織り込まない価格へ戻った。次の勝負所は2Q headline OPではなく、Core OPが100兆ウォンを超えるか、そして3Q OPが100兆ウォン近辺で持続するかだ。
