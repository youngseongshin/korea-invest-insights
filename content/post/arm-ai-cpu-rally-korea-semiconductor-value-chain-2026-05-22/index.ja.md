---
title: "ARM急騰が示すもの — GPUの次のボトルネックはCPU制御、光接続、電源安定性"
date: 2026-05-22T21:40:00+09:00
description: "ARMの急騰は単なるCPU復権の物語ではない。AIインフラのボトルネックがGPUからCPU制御、メモリ移動、光インターコネクト、電源安定性、高速基板、テストソケットへ移っていることを示すシグナルだ。ARMの論理は正しいが、株価は長期成功シナリオをかなり織り込んでいる。"
categories: ["Market-Outlook"]
tags:
  - "ARM"
  - "Marvell"
  - "NVIDIA"
  - "Samsung Electro-Mechanics"
  - "Samsung Electronics"
  - "SK hynix"
  - "HBM"
  - "AIインフラ"
slug: arm-ai-cpu-rally-korea-semiconductor-value-chain-2026-05-22
draft: false
---

> 関連シリーズ：
> [NVIDIA Q1 FY27と韓国AIインフラ](/ja/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [Samsung Electro-Mechanicsのシリコンキャパシタ契約](/ja/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [MLCCとシリコンキャパシタ](/ja/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/)

*ARMの急騰は「CPUが再び重要になった」というだけではない。AIサーバーがGPUボックスから、CPU、XPU、HBM、光接続、電源安定化部品、高速基板、テストを組み合わせたシステムへ変わっているというシグナルだ。ARMは目に見える価格反応だが、実際のアルファはその先のボトルネックにある。*

## 要約

ARMの急騰は再分類イベントだ。モバイルIPロイヤルティ企業から、AIデータセンターCPUプラットフォーム企業へ市場の見方が変わりつつある。AIエージェントが継続的に動き、ツールを呼び出し、データを移動し、GPU・ASIC・メモリを制御するほど、CPUはAIラックの制御層になる。

外部の触媒はNVIDIAだった。NVIDIAはQ1 FY27売上 <strong>816億ドル</strong>、Data Center売上 <strong>752億ドル</strong>、Q2売上ガイダンス <strong>910億ドル ±2%</strong> を発表した。市場はこれをAIインフラ需要のピークアウトではなく加速と読んだ。([NVIDIA][1])

ARM自身のストーリーも強い。FY26売上は <strong>49.2億ドル</strong>、ロイヤルティ <strong>26.1億ドル</strong>、ライセンス <strong>23.1億ドル</strong>、Non-GAAP EPS <strong>1.77ドル</strong>。Arm AGI CPUはMetaをリードパートナーとするAIデータセンターCPUプラットフォームで、FY27-FY28の顧客需要は <strong>20億ドル超</strong> とされる。([Arm][2])

問題は株価だ。Research OS local DBでは、ARMの2026年5月21日終値は <strong>298.23ドル</strong>。FY26 Non-GAAP EPSに対するPERは約 <strong>168.5倍</strong>。論理は正しいが、株価は安くない。

したがって実戦的なアルファはARMそのものより、Marvellのカスタムチップ・光接続、Samsung Electro-Mechanicsのシリコンキャパシタ、SK hynixとSamsung ElectronicsのHBM/DRAM、高速基板・テストソケットにある。

---

## 1. ARM急騰の本当の意味

これを「CPU復権」と呼ぶのは正しいが不十分だ。より重要なのは、制約条件が移動していることだ。

```text
GPU不足
→ HBM / 先端パッケージ不足
→ CPU制御 / メモリ移動 / 光接続の制約
→ パッケージ内電源安定性 / 高速基板 / テストの制約
```

AIエージェントは単純なウェブリクエストではない。複数のモデルを呼び、ツールを使い、文書を読み、データベースを検索し、中間結果を保存する。GPUは計算を担うが、CPUはタスク順序、メモリ、ネットワーク、セキュリティ、システム運用を制御する。

つまりCPUはAIラックの管制塔になる。GPUがエンジンなら、CPUはそのエンジン群を動かす制御層だ。

---

## 2. Arm AGI CPU — IP企業からシリコンプラットフォームへ

ARMは <strong>Arm AGI CPU</strong> を前面に出している。これはagentic AIデータセンター向けの生産シリコンであり、Metaがリードパートナーだ。ASRock、Lenovo、Quanta、Supermicroから商用システムを注文できると説明されている。([Arm][2])

従来モデル：

```text
IPライセンス
→ 顧客がチップを設計・製造
→ ARMはライセンス料とロイヤルティを受け取る
```

新モデル：

```text
IP + コンピュートサブシステム + 生産シリコン
→ 顧客はデータセンター規模でArmを早く導入
→ ARMはプラットフォーム支配力を高める
```

ただし、これは顧客との競合リスクも生む。ARMが自社チップを売れば、ライセンシーはARMを潜在的競争相手として見る可能性がある。Bloombergが報じたFTC調査はこの点に関わる。([Bloomberg][3])

---

## 3. バリュエーション — 正しい話だが高い株

298.23ドル、FY26 Non-GAAP EPS 1.77ドルなら：

```text
FY26 Non-GAAP PER = 298.23 / 1.77 = 約168.5倍
```

FY26売上49.2億ドルに対して時価総額が3,000億ドル台前半なら、売上倍率は60倍台だ。

これは現在の利益を買う価格ではない。2030-2031年のデータセンターCPU浸透、AGI CPU売上、ロイヤルティ上昇、Armv9/Neoverse拡大を前倒しで払っている価格だ。

判断は <strong>現在価格では追わない / 待つ</strong>。

---

## 4. より良いアルファ 1 — Marvellと接続ボトルネック

ARMがCPU制御なら、Marvellは <strong>カスタム計算 + 光接続 + スイッチング</strong> だ。

MarvellはFY26売上 <strong>81.95億ドル</strong>、Non-GAAP EPS <strong>2.84ドル</strong>を発表した。FY27売上は110億ドルに近づき、データセンターが成長を主導し、インターコネクト売上は50%超成長するとしている。([Marvell][4])

Marvellは単なるネットワークチップ企業ではない。カスタムAIチップ、光接続、PCIe/CXLスイッチング、NVLink Fusion協力を持つ。Celestial AI買収はPhotonic Fabricを加えるもので、条件達成時にはFY28に5億ドル、FY29に10億ドルの年率売上を目標にする。([Marvell Celestial][5])

ただしMRVLも大きく上昇した。Research OS local DBでは2026年5月21日終値が <strong>190.69ドル</strong>。判断は <strong>待つ / 押し目買い</strong>。

---

## 5. より良いアルファ 2 — Samsung Electro-Mechanicsと電源安定性

韓国で最も明確な二次ボトルネックの一つはSamsung Electro-Mechanicsだ。

同社は2026年5月20日、約 <strong>1.5兆ウォン</strong> のシリコンキャパシタ供給契約を発表した。期間は2027年1月から2028年12月まで。AIサーバーGPUやHBMなど高性能半導体パッケージ内に搭載され、電源供給の安定性を高める部品だ。([Samsung Electro-Mechanics][6])

ポイントは「MLCCが増える」ではない。

```text
従来：
MLCC + カメラモジュール + FC-BGA

新しい見方：
AIパッケージ内の電源安定化部品
+ FC-BGA
+ AI向けMLCC
```

シリコンキャパシタはMLCCを全面的に置き換えるものではない。AI GPU/HBMパッケージ内、またはその近くに置かれる高性能補完部品だ。これによりSamsung Electro-MechanicsはAIパッケージ電源部品企業として再分類される可能性がある。

---

## 6. 韓国メモリ — SK hynixとSamsung Electronics

ARM急騰は韓国メモリにもプラスだ。CPU制御が増えれば、CPU側メモリ、HBMへのデータ移動、サーバーDRAM、LPDDR/DDR/CXLメモリプール需要も増える。

| 企業 | 役割 | 見方 |
|---|---|---|
| SK hynix | 実証済みHBM勝者 | 保有 / 押し目買い |
| Samsung Electronics | HBMキャッチアップ + 広いIDMオプション | 監視 / 確認後買い |

SamsungにはHBM4認証、数量、マージン、ファウンドリ損失縮小の確認が必要だ。

---

## 7. 高速基板とテストソケット

AIラックが高密度化すると、基板とテストも重要になる。

| レイヤー | 候補 | 確認点 |
|---|---|---|
| 高速PCB | Isu Petasys, Daeduck, TLB, Korea Circuit, Simmtech | AI売上、層数、ASP、営業利益率 |
| テストソケット | ISC, LEENO, TSE | ASIC/HBM/CXL顧客、製品ミックス |
| パッケージ基板 | Samsung Electro-Mechanics, Daeduck, Korea Circuit | FC-BGA稼働率、認証、マージン |

原則は一つ。<strong>「AI関連」という言葉ではなく、顧客・受注・利益率を買う。</strong>

---

## 結論

ARMは正しいシグナルだ。AIサーバーはGPUボックスではなく、CPU、XPU、HBM、光接続、電源安定性、基板、テストのシステムになっている。

しかし急騰後のARMを追うことは、シグナルと資産を混同する可能性がある。重要なのは、まだ十分に価格に織り込まれていないボトルネックを探すことだ。

<strong>ARMはシグナルであり、アルファはボトルネックにある。</strong>

---

*本記事はリサーチとコメントであり、投資助言ではありません。ARMとMRVLの価格はResearch OS local DBの2026年5月21日米国終値基準です。企業データはNVIDIA、Arm、Marvell、Samsung Electro-Mechanicsの公式資料に基づきます。データ基準日：2026年5月22日 KST。*

[1]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx "NVIDIA Announces Financial Results for First Quarter Fiscal 2027"
[2]: https://newsroom.arm.com/news/arm-q4-fye26-results "Arm delivers record-breaking quarter and full-year results"
[3]: https://www.bloomberg.com/news/articles/2026-05-15/arm-holdings-said-to-face-us-antitrust-probe-over-chip-tech "Arm Holdings Said to Face US Antitrust Probe Over Chip Tech"
[4]: https://d1io3yog0oux5.cloudfront.net/_cde1ddaaf3189b05accbc0f122d6a0c2/marvell/db/3715/35343/pdf/2026_03_05_Marvell_Q4_FY26_financial_business_results_FINAL.pdf "Marvell FY26 and Q4 FY26 Financial and Business Results"
[5]: https://d1io3yog0oux5.cloudfront.net/_a2ff1b1766821fdbdf60a17efbf050dd/marvell/files/pages/marvell/db/3831/description/2025-12_02-Marvell-to-Acquire-Celestial-AI-vF2.pdf "Marvell to Acquire Celestial AI"
[6]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
