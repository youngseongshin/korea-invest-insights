---
title: "米中エージェント推論インフラの分岐とSRAMの機会"
date: 2026-07-09T17:20:00+09:00
description: "米国と中国のAI推論インフラがなぜ別の方向へ進むのか、電力、HBM、SRAM/LPU、先端パッケージング、韓国上場企業への影響を整理する。"
categories: ["Theme-Analysis", "Korea Semiconductors", "AI Infrastructure"]
tags: ["AI推論", "エージェントAI", "SRAM", "LPU", "HBM", "Vera Rubin", "LPX", "Samsung Electronics", "SK hynix", "HD Hyundai Electric", "Hanmi Semiconductor"]
slug: us-china-agentic-inference-stack-sram-opportunity-2026-07-09
series: ["hbm", "exclusive-analysis"]
valley_cashtags: ["005930.KS", "000660.KS", "267260.KS", "010120.KS", "298040.KS", "042700.KS", "NVDA"]
draft: false
---

## 要約

米国と中国はどちらもAI推論を拡大しているが、解こうとしている制約は同じではない。米国の制約は電力、ラック密度、HBM、先端パッケージング、1MWあたりのトークン処理能力である。中国の制約は先端ロジックとHBMへのアクセスであり、そのためAscend、光メッシュ、並列拡張、国内メモリ階層で迂回する方向に進んでいる。

韓国上場株にとって、直接的な投資機会は中国の光モジュールではない。より明確なのは米国型AI factoryのボトルネックである。HBM4/HBM4E、電力機器、HBMパッケージング装置、そしてSamsung ElectronicsのSRAM/LPUファウンドリ、AIストレージ、メモリ階層のオプションだ。

## 1. 検証できる論点

出発点はYS-VCの記事である。中心的な主張はおおむね正しい。AI推論はもはや単純なGPUの話ではなく、地域ごとに違う物理制約を解く段階に入っている。

| 主張 | 判定 | 投資家向け解釈 |
|---|---|---|
| 米中のAI推論スタックは分岐している | おおむね正しい | 米国は電力とラック効率、中国はロジックとHBM制約を迂回 |
| 米国はGPU/HBM/SRAMのrack-scale推論へ向かう | 正しい | Vera Rubin、LPX、HBM4、SRAM/LPUが一つのシステムになる |
| 中国はAscend、光メッシュ、独自メモリ階層を使う | 一部正しい | 方向性は妥当だがCloudMatrixの性能は独立検証が必要 |
| 米国の輸出規制は中国のNVIDIA computeへのアクセスを制限する | 正しい | 中国は最先端GPUとHBMを安定的に受け取れない |
| HBMは依然として重要な管理点である | 正しい | BISはHBMを大規模AI trainingとinferenceに重要と見ている |

## 2. なぜ分岐するのか

エージェントAIはトークン数を大きく増やす。コードエージェントやリサーチエージェントは長い文脈を読み、ツールを呼び、結果を解釈し、再び回答を作る。したがってprefill、decode、KV cache、ストレージ、ネットワーク、電力がすべて重要になる。

| 項目 | 米国 | 中国 |
|---|---|---|
| 主要制約 | 電力、ラック密度、変圧器、HBM4、先端パッケージング | 先端ロジック、HBMアクセス、輸出規制 |
| 方向性 | Vera Rubin、LPX/LPU、HBM4、高電力AIラック | Huawei Ascend、光メッシュ、並列拡張 |
| 強み | 最高水準のGPU、HBM、パッケージング | 電力増設、国家主導インフラ |
| 弱み | 系統接続、電力確保までの時間、変圧器 | EUV先端ロジック不足、HBM制限 |
| 韓国株への接点 | HBM、電力機器、HBM装置、ファウンドリ | 供給証拠がなければ限定的 |

IEAはデータセンターの電力需要が2030年に945TWh程度へ増える可能性を示す。([IEA][1]) Energy Connectsが引用したBloombergNEFによれば、中国は今後5年で3.4TW超の発電容量を追加する見通しで、米国の約6倍に近い。([Energy Connects][2]) このため米国は1MWあたりのトークン処理を重視し、中国はインフラの物量拡張を使いやすい。

## 3. 米国型スタック: HBMにSRAM/LPUを足す

NVIDIAはLPXをVera Rubin向けの推論アクセラレータと説明している。Rubin GPUはHBMを使い、Groq 3 LPXはSRAMベースのLPUを使う。([NVIDIA LPX][3])

| 指標 | NVIDIA LPXの説明 |
|---|---:|
| エージェント型システムのトークン増加 | 最大15倍 |
| Vera Rubin NVL72 + LPX | MWあたりthroughput最大35倍 |
| LPU acceleratorあたりSRAM | 500MB |
| SRAM帯域 | 150TB/s |
| LPX rack | 256 LPU chips |
| LPX rack SRAM | 128GB |
| LPX rack DDR5 | 12TB |
| rack SRAM帯域 | 40PB/s |

これはHBMを置き換える話ではない。HBMはRubin GPUの中核であり続ける。SRAM/LPUは低遅延のdecode処理を担い、HBMを補完する。

## 4. 中国スタックは競争上のシグナルであり、韓国株の直接トレードではない

中国が最先端GPUとHBMを自由に使えないなら、より多くのチップを接続し、光メッシュや並列拡張を使うのは合理的である。ただし、それは韓国企業の売上に自動的につながるわけではない。中国のAI供給網は国内化が進み、CloudMatrixの性能、障害率、総所有コストはまだ十分な独立検証がない。

## 5. 韓国上場企業の地図

| 層 | ボトルネック | 韓国企業 | 見方 |
|---|---|---|---|
| HBM4/HBM4E | Vera RubinとAIサーバー向けメモリ | SK hynix, Samsung Electronics | 構造的恩恵。SK hynixが先行、Samsungはキャッチアップ |
| SRAM/LPUファウンドリ | 低遅延decodeアクセラレータ | Samsung Electronics | 売上はまだ見えにくいが重要なオプション |
| AIストレージ/KV cache | eSSD、PCIe 6.0、エージェントメモリ | Samsung Electronics, FADU | HBM下のメモリ階層拡張 |
| HBM装置 | TC bonder、先端パッケージング | Hanmi Semiconductor | 本物のボトルネックだが顧客と評価が重要 |
| 電力機器 | 変圧器、switchgear、系統接続 | HD Hyundai Electric, LS ELECTRIC, Hyosung Heavy | 米国データセンター電力制約への直接露出 |
| 中国光メッシュ | 中国AI cluster向け光モジュール | 韓国直接露出は限定的 | 供給証拠なしでは避ける |

## 6. 実践的な見方

| 優先 | エクスポージャー | 見方 |
|---:|---|---|
| 1 | Samsung Electronics | HBM4E、SRAM/LPU、AIストレージが数字に見えれば条件付き買い候補 |
| 2 | HD Hyundai Electric | 待ち。質は高いが受注モメンタムは見えている |
| 3 | SK hynix | 待ち。HBMリーダーだが混雑したwinner |
| 4 | Hanmi Semiconductor | ウォッチリスト。継続受注と顧客分散が必要 |
| 5 | 中国光メッシュ関連 | 直接証拠なしでは避ける |

韓国の機会は「中国の光メッシュ」ではなく、米国AI factoryのボトルネックにある。電力、HBM、SRAM/LPU、先端パッケージング、ストレージである。事業ポジションではSK hynixが最も強いかもしれない。電力機器の純度ではHD Hyundai Electricが分かりやすい。だが、最も非対称な再評価候補は、Samsung ElectronicsがHBM後発企業だけでなく、HBM4E、SRAM/LPUファウンドリ、AIストレージを持つ企業として見直される場合だ。

## 出典

- [YS-VC](https://www.ys-vc.com/blog/us-china-ai-inference-stack-divergence)
- [IEA](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
- [Energy Connects](https://www.energyconnects.com/news/renewables/2026/february/china-ramps-up-energy-boom-flagged-by-musk-as-key-to-ai-race/)
- [NVIDIA LPX](https://www.nvidia.com/en-us/data-center/lpx/)
- [Samsung Newsroom](https://news.samsung.com/global/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026)
- [BIS](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military)
- [Yonhap](https://en.yna.co.kr/view/AEN20260128002800320)
- [The Elec](https://www.thelec.net/news/articleView.html?idxno=11132)
- [Seoul Economic Daily](https://en.sedaily.com/finance/2026/07/06/hd-hyundai-electric-raises-2026-order-target-23-percent-on)
