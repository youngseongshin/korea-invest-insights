---
title: "ヒューマノイド比較 — Robotis（アクチュエーター、2026E PSR 79×）vs. Rainbow Robotics（サムスン系列、2025 PSR 476×）。どちらも割高だが、検証可能性には差がある"
slug: robotis-vs-rainbow-robotics-humanoid-comparison-2026-05-12
date: 2026-05-12T23:30:00+09:00
description: "韓国ロボティクス・バリューチェーンの頂点に立つ2銘柄：Robotis（アクチュエーター専業 — 手指・関節駆動）とRainbow Robotics（ヒューマノイドプラットフォーム — Samsung Electronics 35%出資）。Robotisの2025年売上高₩38.9bn、営業利益黒字転換₩3.4bn、時価総額 約₩5.1tn。Rainbow Roboticsの2025年売上高₩34.1bn、営業損失 -₩2.5bn、時価総額 約₩16.2tn。売上高がより小さく赤字であるにもかかわらず、Rainbowの時価総額はRobotisの3倍に達する。その差が「Samsungオプション」の値段だ。問いは二つに分かれる：Robotisは「アクチュエーター・サプライヤーとしての業績トレンドが続くか」、Rainbowは「Samsungのロボティクス戦略が実際の売上に転換するか」。どちらも割高だが、四半期単位で検証できるのは一方だけだ。"
categories: ["Sector-Deep-Dive", "Korea Market"]
tags:
  - "Robotis"
  - "Rainbow Robotics"
  - "ヒューマノイド"
  - "アクチュエーター"
  - "Dynamixel"
  - "Samsung Electronics"
  - "韓国ロボティクス"
  - "韓国株"
---

> 📚 <strong>韓国ロボティクス・シリーズ</strong>
> Part 1: [韓国ロボティクス・バリューチェーン完全マップ](/post/korea-robotics-value-chain-complete-map-2026-05-11/)
> Part 2: [SPG vs. Halla Cast — ロボット部品比較](/post/spg-vs-halla-cast-robot-component-comparison-2026-05-12/)
>
> 🔗 <strong>関連</strong>: [ヒューマノイド／ロボティクス投資ハブ](/page/korea-humanoid-robotics-hub/) · [Hyundai Mobis 詳細分析](/post/kr-deep-dive-hyundai-mobis-2026-04-28/) · [Samsung Electro-Mechanics AIインフラ再評価](/post/samsung-electro-mechanics-ai-infrastructure-rerating-2026-04-21/)

*Part 1では部品全体を俯瞰し、Part 2では減速機（SPG）と構造部品（Halla Cast）を比較した。本稿はバリューチェーンの「頂点」、すなわちヒューマノイド完成品メーカーに焦点を当てる。RobotisとRainbow Roboticsはいずれも韓国ロボティクスの旗手だが、つくるもの・稼ぎ方・株価に織り込まれた期待は大きく異なる。Robotisはロボットの「指」を作り、Rainbowは「全身」を作る。Robotisは黒字、Rainbowは赤字。それでもRainbowの時価総額はRobotisの3倍だ。なぜか、そしてどちらの方が検証しやすいのか。*

---

## TL;DR

* <strong>Robotis ＝ ロボットの「指・関節」。<strong> Dynamixelアクチュエーターが中核製品。2025年売上高₩38.9bn、</strong>営業利益黒字転換₩3.4bn</strong>、時価総額 約₩5.1tn。2026E PSR 79×、2027E PSR 50× — <strong>バリュエーション圧縮の経路は見えている。</strong>
* <strong>Rainbow Robotics ＝ Samsung Electronicsをアンカー株主に持つヒューマノイドプラットフォーム。<strong> 協働ロボット（RBシリーズ）、双腕モバイルロボット（RB-Y1）。2025年売上高₩34.1bn、</strong>営業損失 -₩2.5bn</strong>、時価総額 約₩16.2tn。2025年PSR 476× — <strong>Robotisのバリュエーションに並ぶには、2027年に売上高 約₩330bn・純利益 約₩63bnが必要。</strong>
* <strong>売上高が小さく赤字なのにRainbowの時価総額がRobotisの3倍である理由。</strong> Samsung Electronicsがアンカー株主として35%を保有。市場は「Samsungのロボティクス戦略 ＝ Rainbowの将来収益」を織り込んでいる。
* <strong>比較の結論。<strong> Robotisの方が検証しやすい。業績は既に出始め、2027年までの成長パスは数字で追える。Rainbowのオプション価値は大きいが、現在の時価総額を正当化するには2年で売上高10倍が必要であり、その数字はまだ見えない。</strong>どちらも割高である。</strong>

---

## 1. まず——何を作っているかが全く違う

### 1.1 Robotis — ロボットの「指・関節」

Robotisの中核製品は<strong>Dynamixelアクチュエーター</strong> — モーター・減速機・センサー・電子回路を一体化した「関節駆動モジュール」だ。[Part 1](/post/korea-robotics-value-chain-complete-map-2026-05-11/)でも触れた通り、ロボットの関節を動かす基幹部品である。

Robotisが重要な理由：

```
1. 20年超のアクチュエーター専業
   - 売上高の約98%がアクチュエーター
   - 内製化率90%超（減速機を含む）

2. 「ロボットハンド」を作る
   - HX5-D20：20自由度の多指ロボットハンド
   - 触覚・形状センシングで精密把持
   - 卵を割らずに掴み、ネジを回し、ドライバーを握れる

3. 小型から大型へのフォームファクター拡張
   - 既存：小型アクチュエーター（Dynamixel X / P / Y）
   - 新規：ヒューマノイド下半身向け大型アクチュエーター（Dynamixel Q = QDD）
   - QDDはウズベキスタン新工場で4Q26より年産20万台を目標
```

<strong>「ロボットハンド」がなぜ重要か</strong>：Part 1で「なぜヒューマノイドは難しいか」のProblem #2として「指」を挙げた。工場の人手を代替するには、歩行よりも<strong>把持・回転・挿入・押下・組立という手の動作</strong>が本質的に重要だ。Robotisはそのボトルネックに直接位置している。

### 1.2 Rainbow Robotics — ロボットの「全身」

Rainbow Roboticsは<strong>ロボット全体を設計・製造するロボットプラットフォーム企業</strong>だ。KAISTのHUBO研究グループから独立し、韓国で最も知名度の高いヒューマノイドロボットブランドである。

主要製品：

```
1. RBシリーズ（協働ロボット）
   - 人間と並んで作業するロボットアーム
   - ドライブ・エンコーダー・ブレーキ・コントローラーを内製
   - 国際安全認証取得（TÜV SÜD）

2. RB-Y1（双腕モバイルロボット）
   - 車輪移動基台＋双腕ヒューマノイド上半身
   - 各アーム3kgペイロード、計24自由度
   - 物流・サービス・製造ライン向け

3. RB-Y2（産業用双腕ロボット）— 開発中
   - より重いペイロード、製造ライン向け

4. Samsung Electronicsとの関係
   - 2024年末にSamsungがコールオプションを行使し35%取得（筆頭株主）
   - Samsung社内にFuture Robotics Officeを設立
   - Samsung半導体・ディスプレイ・家電・物流の現場に順次展開予定
```

### 1.3 一行要約

```
Robotis：ロボットの「部品」— 関節と指を作る
         アクチュエーターは複数のロボットメーカーに供給できる
         例え：エンジン・トランスミッションの部品サプライヤー

Rainbow：ロボットの「完成品」— ロボット全体を設計・組み立てる
         Samsungという巨大顧客を背負っている
         例え：Samsungが出資したEVスタートアップ

Robotisの部品は多くのロボットに入り得る。
Rainbowのロボットは、Rainbow自身の成功に依存する。
```

---

## 2. 数字——乖離の大きさ

5月12日時点。

| 項目 | Robotis | Rainbow Robotics |
|---|---:|---:|
| 株価 | ₩345,000 | ₩837,000 |
| 時価総額 | <strong>約₩5.1tn</strong> | <strong>約₩16.2tn</strong> |
| 2025年売上高 | <strong>₩38.9bn</strong> | ₩34.1bn |
| 2025年営業利益 | <strong>+₩3.4bn（黒字）</strong> | -₩2.5bn（赤字） |
| 2025年OPM | <strong>約8.7%</strong> | 約-7.3% |
| 2025年PSR | 約130× | <strong>約476×</strong> |
| <strong>2026E売上高</strong> | <strong>₩64.0bn</strong> | 未確定（推定₩130〜210bn必要） |
| <strong>2026E営業利益</strong> | <strong>₩9.0bn</strong> | ₩32.0bn（コンセンサス） |
| <strong>2026E PSR</strong> | <strong>79×</strong> | 78〜130×（売上高前提による） |
| <strong>2026E PER</strong> | <strong>496×</strong> | 約518× |
| <strong>2027E売上高</strong> | <strong>₩101.0bn</strong> | 未確定（推定₩330bn必要） |
| <strong>2027E PSR</strong> | <strong>50×</strong> | 未確定 |
| <strong>2027E PER</strong> | <strong>264×</strong> | 未確定 |
| バリューチェーン上の位置 | 部品（アクチュエーター） | 完成品（プラットフォーム） |
| コアプレミアム | 純粋アクチュエーター | <strong>Samsung Electronicsアンカー株主</strong> |
| 主要顧客 | LG Electronics（第2株主）、世界のロボットメーカー | Samsung Electronics（筆頭株主） |
| 2025年売上高成長率 | +30% | <strong>+76%</strong> |

クロスチェック：

* Robotis PSR = ₩5.06tn / ₩38.9bn = 約130× ✓
* Rainbow PSR = ₩16.24tn / ₩34.1bn = 約476× ✓

### 2.1 表が示すもの

<strong>Rainbowの時価総額はRobotisの3.2倍だが、売上高は小さく赤字だ。</strong> Robotis売上高₩38.9bn > Rainbow売上高₩34.1bn。Robotisは黒字、Rainbowは赤字。それでも時価総額はRobotis ₩5.1tn < Rainbow ₩16.2tn。

この乖離を生んでいるのは一語：<strong>Samsung</strong>。Samsung Electronicsが35%をアンカー株主として保有し、Samsungの半導体・ディスプレイ・家電・物流にRainbowのロボットを展開するという戦略が、既に株価に織り込まれている。

シンプルに整理すると：

* Robotisの株価 = <strong>現在の業績 ＋ 将来のアクチュエーター成長期待</strong>
* Rainbowの株価 = <strong>Samsungがロボティクスで成功するという期待</strong>

---

## 3. Robotis — 業績が現れ始めている

### 3.1 黒字転換の意味

Part 1で「韓国のロボット関連上場企業28社のうち、黒字は3〜4社のみ」と触れた。Robotisはその一社だ。2025年売上高₩38.9bn、営業利益₩3.4bn、OPM 約8.7%。

黒字のロボット企業とは<strong>「ビジネスモデルが実際に稼げることを意味する」</strong>。韓国ロボット銘柄の多くはR&Dで資金を燃やし続けているが、RobotisはDynamixelアクチュエーターを販売し、リアルなキャッシュフローを生んでいる。

### 3.2 成長軌道

ハナ証券レポートのConsensus Dataセクションより：

| 期間 | 2025年（実績） | 2026E | 2027E |
|---|---:|---:|---:|
| 売上高 | ₩38.9bn | <strong>₩64.0bn（+65%）</strong> | <strong>₩101.0bn（+58%）</strong> |
| 営業利益 | ₩3.3bn | <strong>₩9.0bn</strong> | <strong>₩20.0bn</strong> |
| OPM | 8.5% | <strong>14.1%</strong> | <strong>19.8%</strong> |
| EPS | 約₩380 | <strong>₩696</strong> | <strong>₩1,306</strong> |

証券会社間のばらつきは大きい。Samsung証券の2026年売上高₩51bn（保守的）、Daol Investment & Securities₩80bn（積極的）。コンセンサス中央値₩64bnはその間に位置する。決め手となる変数は<strong>大型アクチュエーターQDD（Dynamixel Q）の量産化速度</strong>だ。

```
QDDが重要な理由：

既存Dynamixel X / P / Y：小型アクチュエーター
→ 教育・研究用ロボット、ロボットハンド、小型関節
→ 既に販売中でキャッシュを生んでいる

Dynamixel Q（QDD）：大型アクチュエーター
→ ヒューマノイドの腰・膝・肩など大型関節
→ ウズベキスタン工場で4Q26より年産20万台目標
→ 量産が始まれば売上高が段階的に跳ね上がる

例え：
既存品 = スマートフォン部品（小さいが安定した市場）
QDD = EV部品（大きな市場だが、量産が関門）
```

### 3.3 需要はある、ボトルネックは供給

ハナ証券によれば、2026年のアクチュエーター受注は<strong>100万台超</strong>と見積もられる。2025年の実際の生産台数は<strong>22万台</strong>だった。需要はある、供給能力が足りない。

2026年の生産目標：

* 既存Dynamixel X / P / Y：30万台
* 新規QDD：20万台（4Q26、ウズベキスタン工場）
* 合計：約50万台

100万台超の受注に対して生産できるのは50万台 = <strong>需要は十分、供給制約</strong>。悪くない分析構造だ — 作れれば売れる。

注意点：「100万台受注」が<strong>確定発注（PO）</strong>なのか<strong>問い合わせ・引き合いレベル</strong>なのかは開示されていない。その区別は重要だ。

### 3.4 Robotisの強みと弱み

| 強み | 弱み |
|---|---|
| 黒字転換済み — 業績が出始めている | 時価総額₩5.1tnに対し売上高₩38.9bn — PSR 130×は割高 |
| アクチュエーター純度98% — ロボット需要への直接エクスポージャー | QDD量産はまだ始まっていない |
| ロボットハンド（HX5-D20）— ヒューマノイドのボトルネックに直結 | 中国系QDDメーカーとの価格競争リスク |
| LG Electronics第2株主 — 大手顧客確保 | モーター外部調達 — レアアース供給リスク |
| 内製化率90%超 — コスト競争力 | DataFactory新規事業はまだ売上ゼロ |

---

## 4. Rainbow Robotics — 巨大なSamsungオプション

### 4.1 SamsungがなぜRainbowに入ったか

Samsung Electronicsは2024年12月にコールオプションを行使し、Rainbow Roboticsの株式35%を取得、筆頭株主となった。Samsung社内にはFuture Robotics Officeも設立された。

Samsungがロボティクスに進出する理由はPart 1で触れた — 「Physical AI」だ。Samsungは<strong>製造（半導体・ディスプレイ）の自動化を皮切りに、家庭・小売へと展開</strong>する構想を持つ。

Rainbowはその戦略の中核執行者になり得る：

```
Samsungのロボティクス・ロードマップ（推定）：

フェーズ1：Samsung工場の自動化
  → RB-Y1/Y2を半導体後工程・ディスプレイラインに展開
  → Rainbow製ロボットがSamsungの内部顧客を先に確保

フェーズ2：Samsung物流・サービス
  → Samsung物流センター・店舗にサービスロボットを展開

フェーズ3：外部市場への拡張
  → SamsungブランドとRainbow技術でグローバルロボット市場に進出

このロードマップが実現すれば、Rainbowの売上高は兆ウォン規模になり得る。
現在の₩16tn時価総額には、そのシナリオのかなりの部分が既に織り込まれている。
```

### 4.2 Samsung関連売上高 — まだ初期段階

3Q25時点で、Samsung ElectronicsのRainbow Roboticsへの発注累計は約<strong>₩6.9bn</strong>。年換算すると約<strong>₩10bn</strong>のSamsung関連売上高だ。

時価総額₩16.2tnの企業が、筆頭株主顧客から得ているのが約₩10bn = まだ<strong>テスト・パイロット段階</strong>だ。Samsungが実際の工場に数百〜数千台規模で大量発注する段階には至っていない。

```
Rainbowの現実の位置：

時価総額：₩16.2tn → 「Samsungがロボティクスで成功する」を織り込み済み
売上高：₩34.1bn → まだ「初期納入段階」
Samsung関連：約₩10bn → 「始まったが小さい」

ギャップを埋めるには：
→ Samsung関連売上高が年間数百億〜数千億円規模に拡大する必要
→ 外部顧客も取り込む必要
→ 営業利益を黒字転換させる必要

三つとも現時点では「可能性」であり「確定」ではない。
```

### 4.3 Rainbow Roboticsの強みと弱み

| 強み | 弱み |
|---|---|
| Samsung Electronics筆頭株主（35%）— 戦略的顧客確保 | 時価総額₩16.2tnに対し売上高₩34.1bn — PSR 476×は極端 |
| KAIST HUBO由来 — 歩行・制御アルゴリズム | 営業赤字継続 — まだ稼げていない |
| 主要部品の内製開発 — コスト優位性を主張 | Samsung関連売上高 約₩10bn — パイロット段階 |
| RB-Y1は現場展開可能なレベルに到達 | 外部顧客拡大は不透明 |
| セジョン製造施設を整備中 | セジョン工場の歩留まり・稼働率はこれから |

---

## 5. 比較——どちらの方が検証しやすいか

### 5.1 コア比較

| 項目 | Robotis | Rainbow | 優位 |
|---|---|---|---|
| <strong>業績</strong> | 黒字、OPM 8.7% | 赤字 | <strong>Robotis</strong> |
| 売上高成長率 | +30% | <strong>+76%</strong> | Rainbow |
| <strong>2025年PSR</strong> | 130× | 476× | <strong>Robotis</strong> |
| <strong>2026E PSR</strong> | <strong>79×</strong> | 78〜130×（推定） | <strong>Robotis（数字確定）</strong> |
| <strong>2027E PSR</strong> | <strong>50×</strong> | 未確定（₩330bn売上高が必要） | <strong>Robotis</strong> |
| <strong>2026E PER</strong> | <strong>496×</strong> | 約518× | 大差なし；Robotisの方が視認性高い |
| <strong>2027E PER</strong> | <strong>264×</strong> | 未確定（純利益 約₩63bn必要） | <strong>Robotis</strong> |
| 主要顧客 | LG Electronics（第2株主） | <strong>Samsung Electronics（筆頭株主）</strong> | Rainbow |
| <strong>検証可能性</strong> | 高い（受注・生産・マージンが追跡可能） | 低い（Samsungの社内戦略依存） | <strong>Robotis</strong> |
| 業界レバレッジ | 部品 → 多くのロボットに入れる | 完成品 → Rainbow自身の成功依存 | Robotis |
| オプションの大きさ | 中（アクチュエーター市場） | <strong>大（Samsungのロボティクス全体戦略）</strong> | Rainbow |
| 技術的競争優位 | 20年のアクチュエーター、ロボットハンド、部品統合 | 歩行アルゴリズム、部品内製、Samsung囲い込み | 同等 |

### 5.2 全く異なる二つの分析フレーム

```
Robotisを見ることは =
「アクチュエーター需要の成長 → 売上高への反映」を検証すること
→ 検証可能：受注、生産、ASP、マージン — 四半期ごと
→ 顧客分散（LG、Tesla、Unitreeなど）が可能

Rainbowを見ることは =
「Samsungがロボティクスで成功するか」を検証すること
→ 検証困難：Samsungの社内戦略は選択的にしか開示されない
→ Samsungへの集中度が高い
→ 当たれば大きい、遅れれば長い待ちとなる
```

<strong>自動車業界の例え</strong>：Robotisは複数OEMにエンジンとトランスミッションを供給するBosch型サプライヤー — 業界と共に成長する。RainbowはSamsungが出資したEVスタートアップ — 当たれば巨大だが、失敗すれば資本を失う。

### 5.3 相対評価 — Robotisの方が検証しやすい

三つの理由：

<strong>一：業績が既に出ている。</strong> Robotisは黒字転換済み。セルサイド推計によれば2026年のOPMは約15%に達する可能性がある。Rainbowは赤字継続中だ。

<strong>二：検証が可能だ。</strong> Robotisは「100万台受注のうち何台を生産したか、ASPはいくらか、マージンは」を四半期ごとに確認できる。Rainbowの「Samsungが実際に何台発注したか」は外部から把握しにくい。

<strong>三：バリュエーション圧縮の経路が見える分、割高感が相対的に低い。</strong> Robotisの2026E PSR 79× → 2027E 50×は<strong>バリュエーション圧縮の道筋</strong>を示している。Rainbowの2026E PSRは売上高前提がなければ計算すらできず、2027E公開コンセンサスも存在しない。視認性が異なる。

<strong>注意：「Robotisの方が検証しやすい」≠「Robotisが割安」。</strong> どちらも割高だ。Robotisの2027E PSR 50×・PER 264×でも、売上高₩101bnかつOPM 20%が実現してはじめて理屈が通る。

---

## 6. フェアバリュー — 数字が示すもの

### 6.1 Robotis — コンセンサスベース、2027年まで数字が見える

セルサイドコンセンサス（ハナ証券レポートConsensus Dataセクション）：

| 期間 | 2025年（実績） | 2026E | 2027E |
|---|---:|---:|---:|
| 売上高 | ₩38.9bn | <strong>₩64.0bn</strong> | <strong>₩101.0bn</strong> |
| 売上高成長率 | +30% | <strong>+65%</strong> | <strong>+58%</strong> |
| 営業利益 | ₩3.3bn | <strong>₩9.0bn</strong> | <strong>₩20.0bn</strong> |
| OPM | 8.5% | <strong>14.1%</strong> | <strong>19.8%</strong> |
| EPS | 約₩380 | <strong>₩696</strong> | <strong>₩1,306</strong> |

現在株価₩345,000に対して：

| 基準 | PSR | PER |
|---|---:|---:|
| 2025年（実績） | 130× | 約910× |
| <strong>2026E</strong> | <strong>79×</strong> | <strong>496×</strong> |
| <strong>2027E</strong> | <strong>50×</strong> | <strong>264×</strong> |

クロスチェック：2026E PER = 345,000 / 696 = 495.7× ✓；2027E PER = 345,000 / 1,306 = 264.2× ✓

<strong>読み方</strong>：2026年PER 496×は極端だが、2027年PER 264×・PSR 50×への移行には<strong>バリュエーション圧縮の経路</strong>が見える。売上高₩64.0bn → ₩101.0bn、OPM 14% → 20%は「高成長部品株」としての論拠を支える。

確認すべき変数：2026年売上高₩60bn超・OPM 14%超の維持。

セルサイド目標株価の平均は約₩317,000、最高値（Daol Investment & Securities）は₩435,000。<strong>現在の₩345,000は既に平均目標株価を上回っている。</strong>

### 6.2 Rainbow Robotics — コンセンサスが薄い。逆算アプローチで考える

Rainbowの問題は<strong>信頼できるコンセンサスが少ない</strong>ことだ。確認できるのは2026E営業利益₩32.0bn（FnGuide）のみ。2026年売上高と2027年の数字は公開コンセンサスが存在しない。

そこで、現在の時価総額を正当化するために<strong>必要な数字を逆算</strong>する。

<strong>2026年逆算 — 営業利益₩32.0bnを生むには売上高がいくら必要か：</strong>

| 想定OPM | 必要な2026年売上高 | 2025年比成長率 | 現在時価総額での implied PSR |
|---:|---:|---:|---:|
| 15% | ₩213.3bn | +525% | 78× |
| 20% | ₩160.0bn | +369% | 104× |
| 25% | ₩128.0bn | +275% | 130× |

<strong>1年で売上高を4〜6倍にする必要がある（₩34.1bn比）。</strong> 大規模なSamsung関連売上高なしには事実上不可能だ。

現在時価総額から計算した2026E PERは約<strong>518×</strong>（₩16.6tn / 推定純利益）。Robotisの2026E PER（496×）と近似するが、Robotisの場合は売上高・営業利益の推計が確定的である一方、Rainbowの売上高視認性は低い。

### 6.3 2027年アラインメントの計算

Robotisの2027年バリュエーションはPSR 50×・PER 264×。<strong>Rainbowが同水準に並ぶには2027年に何が必要か：</strong>

| 基準 | Rainbowに必要な数字 |
|---|---:|
| Robotis 2027E PSR（50×） | 売上高 約<strong>₩330bn</strong> |
| Robotis 2027E PER（264×） | 純利益 約<strong>₩63bn</strong> |

クロスチェック：₩16.6tn / 50 = ₩332bn売上高 ✓；₩16.6tn / 264 = ₩62.9bn純利益 ✓

<strong>Rainbowが現在の時価総額をRobotisのバリュエーションに合わせるには、2年間で売上高₩330bn・純利益₩63bnが必要だ。</strong> ₩34.1bnから2年で約10倍 — 年率換算で約+211%。

不可能ではない — Samsungが数千台規模の発注を出せば実現できる。だがその数字は今どこにも見えていない。

### 6.4 シナリオ別株価試算

<strong>Robotis：</strong>

| シナリオ | 2027年売上高 | 適用PSR | 試算株価 | 現在比 |
|---|---:|---:|---:|---:|
| ベア（生産遅延） | ₩80bn | 35× | 約₩190,000 | -45% |
| ベース（コンセンサス通り） | ₩101bn | 45× | 約₩310,000 | -10% |
| ブル（QDD量産大成功） | ₩130bn | 50× | 約₩440,000 | +28% |

<strong>Rainbow Robotics：</strong>

| シナリオ | ベース事業価値 | Samsungオプション価値 | 合計 | 試算株価 | 現在比 |
|---|---:|---:|---:|---:|---:|
| ベア | ₩2.0tn | ₩3.0tn | ₩5.0tn | 約₩255,000 | <strong>-70%</strong> |
| ベース | ₩4.8tn | ₩6.0tn | ₩10.8tn | 約₩550,000 | <strong>-34%</strong> |
| ブル | ₩10.0tn | ₩8.0tn | ₩18.0tn | 約₩920,000 | +10% |

セルサイド目標株価の平均：Robotis 約₩317,000、Rainbow 約₩580,000。<strong>どちらも現在株価は平均目標株価を上回っている。</strong>

### 6.5 非対称な構造 — 分析の核心

```
Robotis：
→ ベースケース：-10%（やや割高）
→ ブルケース：+28%
→ ベアケース：-45%
→ 上下幅が近い — ニュートラルな非対称性

Rainbow：
→ ブルケースでさえ：+10%のみ
→ ベースへの回帰：-34%
→ ベアケース：-70%
→ 下値リスクが上値の3〜7倍 — 不利な非対称性
```

<strong>RainbowはSamsungオプション実現のベストケースでも+10%しか余地がなく、ベースへの回帰で-34%という構造に置かれている。</strong> 数字の上では新規参入には不利な非対称性だ。

### 6.6 一行の結論

```
Robotis：割高だが、2027年までのバリュエーション圧縮経路は見えている。
Rainbow：現在の時価総額を正当化するには2年で売上高10倍・純利益₩63bnが必要。
         その数字はまだ公式には見えていない。
```

---

## 7. 次に確認すべきこと

### 7.1 Robotis — 決算での検証

| 項目 | タイミング | 重要な理由 |
|---|---|---|
| 1Q決算 | 今月〜来月 | 売上高成長とOPMは維持されているか |
| QDD量産開始 | 2026年4Q | 大型アクチュエーター量産 = 売上高ステップアップの関門 |
| ウズベキスタン工場稼働 | 2026年10月〜 | 生産能力拡大の中核 |
| 100万台受注の実態 | 四半期決算 | 確定発注か引き合いレベルか |
| ロボットハンド（HX5-D20）売上 | 四半期決算 | デモ製品か商用製品か |

### 7.2 Rainbow Robotics — Samsungを通じた検証

| 項目 | タイミング | 重要な理由 |
|---|---|---|
| Samsung関連売上高の規模 | 半期報告 | ₩10bn規模から数百億ウォンへ拡大するか |
| RB-Y2の現場展開 | 2026年下期 | 実際の工場ライン、それともデモのみか |
| 営業利益の黒字転換 | 四半期決算 | 事業として稼げるようになるか |
| セジョン製造施設の稼働 | 2026年下期〜 | 量産能力の実証 |
| 外部顧客の拡大 | 継続的に | Samsung集中度を低下できるか |

---

## 8. 結論

RobotisとRainbow Roboticsはいずれも韓国ロボティクスの象徴だ。しかし分析上は、全く異なる構造を持つ。

Robotisは<strong>「業績が出始めたコンポーネント・サプライヤー」</strong>だ。営業利益は黒字転換済み、アクチュエーター受注は伸び、QDDの量産が売上高を段階的に引き上げる態勢にある。割高だが、数字で検証できる。

Rainbow Roboticsは<strong>「巨大なSamsungオプションを価格に折り込んだ企業」</strong>だ。Samsungのロボティクスの成功がRainbowを成功させる。だが現在の株価には既にその成功の大部分が織り込まれている。ブルケースでも+10%しかなく、ベースへの回帰は-34%を意味する。

二社を比べれば、<strong>Robotisの方が検証しやすい</strong>。ただしRobotisも₩345,000という現在株価はベースケースの試算値（₩310,000）を上回っている。最も規律のある分析アプローチは、<strong>1Q決算での売上高成長とOPM、そしてQDD量産の進捗</strong>を追うことだ。

韓国ロボティクスはまだ「期待の産業」だ。最もクリアな分析の窓が開くのは、期待が業績に転化するときだ。そしてその窓が先に開くのは、RainbowよりもRobotisの方だろう。

---

## FAQ

<strong>Q：RobotisとRainbow Robotics、どちらが良い企業ですか？</strong>
A：事業の質は別の問いだ。どちらも韓国ロボティクスの象徴であり、確かな技術力を持つ。「検証しやすい」のはRobotis — 黒字の財務、四半期ごとに追える受注・生産・マージン、2027年までの可視的なバリュエーション圧縮経路がある。Rainbowのオプションは大きいが、検証可能性は低い。

<strong>Q：なぜRainbowはRobotisの3倍の時価総額なのですか？</strong>
A：Samsung Electronicsが筆頭株主（35%）だからだ。市場は「Samsungのロボティクス戦略 ＝ Rainbowの将来収益」を織り込んでいる。Robotisは現在の売上高（₩38.9bn対₩34.1bn）と収益性でRainbowを上回るが、Rainbowの時価総額（₩16.2tn）はRobotis（₩5.1tn）を大きく超える。

<strong>Q：PSR 79×・PER 496×は正当化できますか？</strong>
A：韓国市場の基準では極端だ。高成長テーマ（ロボティクス、AI）では、急速な売上高成長が自然にバリュエーションを圧縮し得る。Robotisの2027年PSR 50×・PER 264×への道筋は、売上高₩101bnとOPM 20%が実現すれば見える。

<strong>Q：Rainbowが2027年に₩330bnの売上高に届かなかったら？</strong>
A：市場がバリュエーションを修正する。ベアケース（売上高₩100bn未満）なら時価総額は約₩5tnに縮小 — 現在株価から約-70%の下値。Samsungオプションの部分実現でベースケース（時価総額₩10.8tn、-34%）へ戻る可能性もある。

<strong>Q：Robotisの「100万台受注」は本物ですか？</strong>
A：ハナ証券が引用した推計だ。確定発注（PO）なのか引き合いレベルなのかは開示されていない。検証方法は、四半期の出荷台数と売上高が実際に増加するかどうかを確認することだ。2025年の実際の生産台数は22万台だった。

<strong>Q：QDDがなぜそんなに重要なのですか？</strong>
A：既存Dynamixel（X/P/Y）は教育・研究向け小型市場に向けた製品だ。QDDはヒューマノイドの大型関節（腰・膝・肩）を対象とし、ヒューマノイド市場全体に直接エクスポージャーし、ASPも大幅に高い。ウズベキスタン工場で4Q26に年産20万台を目標としている。

<strong>Q：SamsungがRainbowを完全買収する可能性はありますか？</strong>
A：可能性はあるが、公式に確認されていない。Samsungが35%から持ち分を積み増したり完全子会社化したりすれば、大きなカタリストとなる。ただしTOBシナリオが示唆するプレミアムを市場が先読みするのは難しい。

<strong>Q：どちらか一方のロボット銘柄を選ぶとしたら、分析上の指針は？</strong>
A：特定の推奨は適切でない。[バリューチェーンPart 1](/post/korea-robotics-value-chain-complete-map-2026-05-11/)では、部品サプライヤー（SPG、Robotis、HL Mando、Samsung Electro-Mechanics、LG Innotek、Hyundai Mobis）を取り上げた。これらは堅固なベース事業がロボティクスオプションのリスクを緩和する構造だ。純粋なロボティクス銘柄は株価負担がより高い。分析上、「ベース事業＋ロボットオプション」の構造は「ロボットオプションのみ」の構造より検証しやすい。

---

*本稿はリサーチ・情報提供を目的としており、投資助言を構成するものではありません。Robotisのデータはサムスン証券、ハナ証券、Daol Investment & Securities、KB証券、IBK投資証券、ユジン投資証券の各レポートを参照しています。Robotisの2026E/2027E数値（売上高₩64.0/₩101.0bn、営業利益₩9.0/₩20.0bn、EPS ₩696/₩1,306）はハナ証券レポートのConsensus Dataセクションを参照しています。Rainbow Roboticsの2026E営業利益₩32.0bnはFnGuideコンセンサスを参照しており、2026E売上高と2027E数値は公開コンセンサスが存在しません。Rainbowの「必要業績の逆算」はRobotisのバリュエーションをRainbowの現在時価総額に適用したアナリスト推計です。株価は毎日経済新聞のデータ（5月12日時点）を参照しています。Samsungのロボティクス戦略の詳細は選択的にしか開示されていません。両銘柄とも高バリュエーションのテーマ株であり、ボラティリティは高い。Robotisは5月12日付で投資警告指定予告を受けています。分析は誤り得ます。データカット：2026年5月12日（韓国時間）。*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
