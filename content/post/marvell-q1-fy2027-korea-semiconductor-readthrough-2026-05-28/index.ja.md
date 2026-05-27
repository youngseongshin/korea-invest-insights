---
title: "マーベル Q1 FY2027 決算と韓国半導体：HBMよりも接続・基板・電力ボトルネック"
date: 2026-05-28T10:20:00+09:00
description: "Marvell Q1 FY2027の決算は単純なEPS超過ではなく、AIデータセンターのボトルネックがcustom XPU、optical interconnect、scale-up networking、FCBGA、MLCC、シリコンキャパシタ、テストソケットへと拡散していることを示す。韓国半導体のread-throughはSamsung Electro-Mechanics、Samsung Electronics、SK Hynix、ISC・リノ工業・TSEの順に整理する。"
categories: ["Market-Outlook"]
tags:
  - "Marvell"
  - "MRVL"
  - "マーベル"
  - "韓国半導体"
  - "Samsung Electro-Mechanics"
  - "009150"
  - "Samsung Electronics"
  - "005930"
  - "SK Hynix"
  - "000660"
  - "ISC"
  - "リノ工業"
  - "TSE"
  - "FC-BGA"
  - "MLCC"
  - "シリコンキャパシタ"
  - "HBM"
  - "AI ASIC"
  - "AIインフラ"
slug: marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28
valley_cashtags:
  - Marvell
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - ISC
  - 리노공업
  - 티에스이
  - 대덕전자
  - 이수페타시스
  - 심텍
draft: false
---

> 📚 関連記事の文脈
> [マーベル・ブロードコム決算前：韓国半導体ボトルネック点検](/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/)の続編です。プレビューで掲げた問いは「HBM単一ベットがAI ASIC・ネットワーク・電力安定化へ広がるか」であり、本稿はMarvell Q1 FY2027の決算をもとにその答えを書き直します。関連ハブは[AI HBMハブ](/page/korea-semiconductor-hbm-kospi-hub/)、[AI基板・PCBハブ](/page/korea-ai-pcb-substrate-hub/)、[韓国半導体バリューチェーンハブ](/page/korea-semiconductor-equipment-ip-hub/)です。

## TL;DR

Marvell Q1 FY2027の核心はEPS超過ではない。核心は、同社がFY2027〜FY2028のAIデータセンター成長パスを引き上げ、その理由を<strong>custom XPU、optical interconnect、Ethernet switching、DCI、scale-up/scale-across networking、XPU attach</strong>で説明した点にある。

韓国半導体に翻訳すると、答えは単純な「HBMをもっと買え」ではない。HBMは依然として本流だが、今回の決算が新たに確認したincremental alphaは<strong>GPU周辺の接続・基板・電力インテグリティ・テストのボトルネック</strong>にある。

優先順位は以下の通りだ。

| 優先順位 | 韓国 read-through | 主要銘柄/群 | 判断 |
|---:|---|---|---|
| 1 | FCBGA + AIサーバーMLCC + シリコンキャパシタ | Samsung Electro-Mechanics | 最も直接的。ただし既にリレーティングされた水準であり、SiCap・FCBGAのマージン確認が必要 |
| 2 | HBM4、SOCAMM2、eSSD、アドバンスドパッケージング | Samsung Electronics、SK Hynix | HBM betaは維持。新規alphaはHBM以外のメモリアタッチとパッケージング |
| 3 | Custom ASIC/XPUテストソケット・インターフェース | ISC、リノ工業、TSE | 構造は良好だが、直接売上確認前まではウォッチリスト |
| 4 | AIネットワーキング向け高速PCB/MLB | イスペタシス、テックウィングス、シムテック等 | 選別が必要。「AI PCB」全体が同等の恩恵を受けるわけではない |

Marvell自体は<strong>HOLD / Buy watch</strong>が妥当だ。基準株価$198.70、12ヶ月目標株価$225は約+13%のアップサイドだ。成長パスは力強いが、株価も既に高い期待を織り込んでいる。韓国側ではMarvellそのものより<strong>Marvellが確認したボトルネックがどこへ波及するか</strong>がより重要だ。

---

## 1. Marvell決算で本当に見るべきこと

Marvellは2026年5月27日の米国市場引け後にQ1 FY2027の決算を発表した。公式数値は以下の通りだ。([Marvell][1])

| 項目 | Q1 FY2027 | 解釈 |
|---|---:|---|
| 売上高 | <strong>$2.418B</strong> | 前年比+28%、ガイダンス中間値比+$18M |
| GAAP EPS | <strong>$0.04</strong> | Celestial AI・XConn買収の会計処理により低く表示 |
| Non-GAAP EPS | <strong>$0.80</strong> | コンセンサス付近 |
| GAAP粗利益率 | <strong>52.1%</strong> | 前年比改善 |
| Non-GAAP粗利益率 | <strong>58.9%</strong> | AIミックス拡大にも58%後半を維持 |
| 営業キャッシュフロー | <strong>$638.8M</strong> | 過去最高の営業キャッシュフロー |
| Q2売上ガイダンス | <strong>$2.70B ±5%</strong> | レンジは$2.565B〜$2.835B |
| Q2 Non-GAAP EPSガイダンス | <strong>$0.93 ±$0.05</strong> | 次四半期収益性の基準線 |

決算自体は「小幅beat / EPS inline」に近い。しかし株価と韓国半導体のread-throughに重要なのはQ1の数セントではなく、<strong>同社が語ったFY2027〜FY2028の売上パス</strong>だ。

サードパーティのトランスクリプトによれば、経営陣はFY2027売上を約$11.5B、FY2028売上を約$16.5Bと示し、FY2027のinterconnect成長率見通しも従来の約50%から70%以上へ引き上げた。公式IRトランスクリプトではないという限界はあるが、方向性は同社の公式リリースの文言と一致する。Marvellの公式リリースも成長の源泉として800G・1.6T optics、51.2T Ethernet switches、NPO/CPO向けscale-up optical、DCI modules、custom XPU、XPU-attachを明示した。([Marvell][1]、[StockAnalysis transcript][2])

一言でまとめると以下のようになる。

> MarvellはAIデータセンターのcapexがGPU購入からクラスター接続構造へ移行していることを数字で確認した。

---

## 2. 核心はSOCAMMではなく接続構造だ

今回のカンファレンスコールを韓国の投資家が読む際の最大の誤読リスクは、「SOCAMMテーマ」としてのみ捉えることだ。SOCAMMは重要だが、Marvellのコールの中心はそこにはない。

中心は以下の順序だ。

| Marvellの核心軸 | なぜ重要か | 韓国半導体への翻訳 |
|---|---|---|
| Custom XPU / custom ASIC | ハイパースケーラーがNVIDIA GPU以外の自社AI siliconを増やすシグナル | HBM顧客基盤の多様化、パッケージ基板、テストソケット |
| Optical interconnect | 800G/1.6T、DCI、scale-up opticsがAIクラスター拡張のボトルネック | 高速PCB・光通信は選別、Samsung Electro-Mechanics FCBGA・電力安定化は構造的 |
| Ethernet switching | 51.2T、100T、200Tロードマップはnetworking silicon dollar contentの増加を示す | network ASIC向けFCBGA、高速ボード、検査・テスト |
| XPU attach | CXL、NIC、memory attach、inference KV cacheと連動 | Samsung Electronics SOCAMM2・eSSD・サーバーDRAM、OpenEdges類のメモリIPオプション |
| NVLink Fusion | NVIDIAエコシステム内でcustom siliconが共存する道 | 「NVIDIA対ASIC」の二項対立よりサプライチェーンの拡張 |

NVIDIA-Marvellの発表も同じ方向を向いている。NVIDIAはMarvellに20億ドルを投資し、MarvellはNVLink Fusion互換のcustom XPUとscale-up networkingを提供する。また両社はsilicon photonicsとAI-RANでも協力する。([Marvell NVIDIA][3])

この意味するところは単純だ。

> AIデータセンターはGPUボックスではなく、GPU、custom XPU、HBM、optical、switch、retimer、CXL、NIC、FCBGA、MLCCが一体となって動くシステムだ。

したがって韓国半導体投資も「メモリ大型株だけを見るか」から「メモリの下でどのボトルネックが数字に変わるか」へ視点を下げる必要がある。

---

## 3. 韓国半導体 read-through 第1位：Samsung Electro-Mechanics

Marvellの決算を韓国銘柄に最も明快に翻訳するならSamsung Electro-Mechanicsだ。理由は三つある。

第一に、Marvellが強調したcustom XPU、Ethernet switch、optical interconnect、XPU attachはいずれも高速・高集積パッケージと基板を必要とする。これはFC-BGA需要と直結する。

第二に、AIサーバーは低電圧で瞬間的に大電流を消費する。GPU・HBM・XPUパッケージ周辺の電圧変動を抑えるには、MLCCやシリコンキャパシタなどの電力安定化部品が必要だ。

第三に、Samsung Electro-Mechanicsはこの二つのレイヤーをすでに両方持っている。同社はQ1 2026の決算で、Package Solution売上が7,250億ウォンと前年比45%・前四半期比12%増加し、AIアクセラレーター、サーバーCPU、ネットワーク向け高付加価値基板の供給拡大を言及した。([Samsung Electro-Mechanics Q1][4])

さらにSamsung Electro-Mechanicsは、グローバル大手企業と1兆5,570億ウォン規模のシリコンキャパシタ供給契約を締結した。契約期間は2027年1月1日から2028年12月31日までだ。この部品はAIサーバー向けGPU・HBMパッケージ内部の電力供給安定性を高める用途として説明されている。([Samsung Electro-Mechanics SiCap][5])

Samsung Electro-Mechanicsの投資ロジックは今や次のように変わっている。

| 過去のフレーム | 現在のフレーム |
|---|---|
| スマートフォンMLCC・カメラモジュールの景気敏感株 | AIパッケージ電力インテグリティ + FCBGAプラットフォーム |
| モバイル需要の回復 | AIアクセラレーター・サーバーCPU・network ASICの需要 |
| 汎用MLCCサイクル | 高容量・低ESR・超薄型・高信頼性MLCC/SiCapミックス |
| イビデン/村田のどちらかとの比較 | MLCC + FCBGA + SiCapハイブリッドとの比較 |

ただしこの結論は「今すぐどんな価格でも買う」とは異なる。Samsung Electro-Mechanicsはすでにシリコンキャパシタ契約、時価総額100兆ウォン規模、AIインフラのリレーティングをかなりの程度織り込んでいる。したがって次の確認変数は株価モメンタムではなく、<strong>売上総利益率、Package Solution OPM、SiCap量産歩留まり、追加顧客の多様化</strong>だ。

---

## 4. Samsung Electronics・SK Hynix：HBM betaは維持、新規alphaはHBM周辺

Marvellの決算はHBMに対してネガティブではない。むしろ逆だ。custom XPUとscale-up networkingが増えてもメモリのdollar contentは減らない。AIモデルがagentic AI、reasoning、mixture-of-expertsへ進化するほど、データ移動とメモリ要求量はむしろ増大する。

ただし投資の観点から「HBMは良い」は既に中心的なthesisだ。Marvellのコールが新たに与えた情報は以下だ。

1. HBMの顧客基盤がNVIDIA GPU単一構造からハイパースケーラーのcustom XPUへ広がる。
2. XPU attachがCXL、NIC、memory attach、KV cacheと連動し、サーバーDRAM・SOCAMM・eSSDにまで影響する。
3. AIクラスターが大規模化するほど、メモリと演算チップをつなぐパッケージング・基板・電力安定化の価値が上昇する。

Samsung Electronicsはこの点で複合的なオプションを持つ。HBM4、HBM4E、SOCAMM2、PM1763 SSD、ファウンドリ、アドバンスドパッケージングがすべて同じAI infrastructure stackに入る。Samsung ElectronicsはGTC 2026でHBM4E、SOCAMM2、PM1763 SSDをNVIDIA協力のAIインフラ製品群として提示した。([Samsung Semiconductor][6])

SK HynixはHBM純粋betaとして依然として最も強い。ただしMarvellの決算だけを見れば、新規alphaはSK Hynixよりも<strong>HBMの隣で同時に伸びるSamsung Electro-Mechanics、テストソケット、高速基板</strong>に大きい。SK Hynixは本流だが、すでに市場の目が最も集まっているポジションでもある。

---

## 5. テストソケット：custom ASIC拡散の静かな受益者

Marvellのコールでcustom revenueが重要な理由は、単純なチップ数量ではない。核心は<strong>SKUとqualificationサイクル</strong>だ。

AIアクセラレーターがNVIDIA GPU一つに標準化される構造なら、テスト部品の需要も相対的に予測しやすい。逆にハイパースケーラーごとのcustom XPU、XPU attach、CXL、NIC、switch ASIC、DPUが増えると、テスト条件とソケット設計はより細分化される。

このケースでテストソケットとインターフェース部品には次の三つが同時に好転し得る。

| 変数 | 方向 | 理由 |
|---|---|---|
| 数量 | 増加 | custom ASIC、network ASIC、memory attach SKUの増加 |
| ASP | 上昇 | 高ピン数・高速信号・高電力テストの難易度上昇 |
| 交換サイクル | 構造的 | 世代交代と顧客ごとのqualification繰り返し |

韓国ではISC、リノ工業、TSEがウォッチリストだ。ただしここでは確信度を下げる必要がある。韓国のテストソケット企業がMarvellまたは特定ハイパースケーラーのcustom XPUチェーンに直接入っているかどうかは、公開情報だけでは確定できない。したがって現時点では<strong>「受益の可能性」</strong>であり、<strong>「確定した顧客マッピング」</strong>ではない。

確認すべき指標は四半期決算におけるAI/HPC logic売上、新規顧客数、高付加価値ソケットミックス、OPMの維持だ。

---

## 6. 一般PCBは無差別買いの対象ではない

Marvellの決算はAI networkingとoptical interconnectにポジティブだ。しかし「AIネットワーキングが好調→全PCBが好調」という結論は危険だ。

恩恵は一般PCBではなく、以下の条件を満たす企業に集中する。

1. 高速信号向け低損失材料を扱える。
2. 高多層MLBまたは高付加価値パッケージ基板への露出がある。
3. AIサーバー・ネットワーク機器顧客の認証を持つ。
4. 数量増加よりASP・層数・面積の増加が確認される。

GPUとXPUの数が増えても基板数量が同じ比率で増えるわけではない。一つの高性能パッケージとボードに複数のチップがより高密度に搭載される構造では、数量より<strong>基板面積、層数、材料難易度、歩留まり</strong>がより重要だ。

したがってイスペタシス、テックウィングス、シムテック、TLB、コリアサーキットを同一バスケットとして単純に括るのは不正確だ。Marvell決算の実際のread-throughは「ネットワーク向け高層基板と高速信号対応材料を持つ企業を選別せよ」に近い。

---

## 7. MRVL自体のバリュエーション：良い会社と良い価格は別物だ

Marvell自体に対する判断はHOLD / Buy watchだ。

| 項目 | 内容 |
|---:|---|
| 基準株価 | $198.70、2026-05-27 通常取引終値 |
| 12ヶ月目標株価 | $225 |
| 上昇余地 | 約+13.2% |
| 算定フレーム | FY2028E EV/Sales |
| 核心判断 | 成長パスは上方修正されたがバリュエーションも既に高い |

Base caseの算式は以下の通りだ。

```text
目標株価 = (FY2028E 売上 × 目標 EV/Sales - 純負債) ÷ 希薄化後株式数
```

前提はFY2028E売上$16.5B、目標EV/Sales 12.5倍、純負債約$1.117B、希薄化後株式数915Mだ。計算すると目標株価は約$224、四捨五入基準で$225となる。

MarvellがBroadcomのようにre-ratingされるには三つが必要だ。

1. Custom silicon revenueが単一顧客イベントではなく繰り返しプログラムとして確認される。
2. InterconnectとSwitchingの成長にもnon-GAAP gross marginが58〜59%台で維持される。
3. サプライチェーン確保のためのprepaymentが実際の売上rampとFCFとして返ってくる。

すなわち良い会社になったことは確かだが、良い買い場かどうかは別の問題だ。

---

## 8. 次のチェックポイント

| チェックポイント | 強いシグナル | 弱いシグナル |
|---|---|---|
| Q2 FY2027 売上 | $2.835B上限に接近または上回る | $2.70B中間値を下回る |
| Data Center 売上 | 前四半期比high-teens以上の成長 | sequential growth の鈍化 |
| Non-GAAP GM | 59.25%以上または上限を維持 | 58.25%を下回る |
| Interconnect | FY2027 +70%以上の見通し維持・上方修正 | 800G/1.6T rampの鈍化 |
| Custom XPU | FY2028 2倍以上の成長・FY2029 $10B+の視認性 | 顧客ごとのramp遅延 |
| Scale-up switching | tier-1顧客の量産具体化 | engagementは多いが売上なし |
| 韓国 read-through | Samsung Electro-Mechanics Package Solution・SiCap・FCBGA数値確認 | テーマは強いがマージン・受注なし |

韓国銘柄ごとの確認変数はよりシンプルだ。

| 銘柄/群 | 確認すべきこと |
|---|---|
| Samsung Electro-Mechanics | Package Solution成長率、AIネットワーク向けFCBGA売上、SiCap量産歩留まり・マージン、追加長期契約 |
| Samsung Electronics | HBM4顧客認証、SOCAMM2の実出荷、eSSD価格・数量、ファウンドリ/パッケージング顧客 |
| SK Hynix | HBM4 ramp、顧客多様化、2027年の供給過剰有無 |
| ISC・リノ工業・TSE | AI logic/テストソケット売上、新規顧客、高付加価値ミックス、OPM |
| PCB/MLB | AIネットワーク顧客認証、ASP上昇、低損失材料・高層化 |

---

## 9. 破棄条件

このthesisが弱まる条件は明確だ。

1. Marvell Q2売上が$2.70B中間値を下回り、Data Center growthが鈍化する。
2. Non-GAAP gross marginが58.25%を下回り、custom/interconnect mixがマージン希薄化として確認される。
3. FY2028 $16.5B売上見通しが下方修正される。
4. Custom XPUとXPU attachが特定顧客のスケジュール遅延に縛られる。
5. Samsung Electro-Mechanics SiCapが低マージン売上として確認されるか、FCBGA成長率が鈍化する。
6. テストソケット企業の決算にAI/HPC logic売上の増加が現れない。
7. HBMのリードタイムが短縮し、2027年の供給過剰シグナルが出る。

---

## 最終解釈

Marvell Q1 FY2027は韓国半導体に対して「HBMだけ買え」というシグナルではない。より正確なメッセージはこうだ。

> AIクラスターが大規模化するほど、ボトルネックはGPUから接続、基板、電力安定化、テストへと降りてくる。

この観点から最も直接的な韓国銘柄はSamsung Electro-Mechanicsだ。Samsung Electro-MechanicsはMLCC、FC-BGA、シリコンキャパシタがすべて同じAIパッケージのボトルネックに入る。Samsung ElectronicsとSK HynixはHBM本流として引き続き重要だが、Marvellの決算が新たに生み出したalphaはHBM周辺部により大きい。ISC・リノ工業・TSEはcustom ASIC拡散の2次受益候補だが、直接売上確認前まではウォッチリストが適切だ。

結論は無差別買いではない。優れたthesisも数字で確認されなければテーマで終わる。今四半期以降、韓国半導体で見るべきは株価よりも<strong>Package Solution売上、SiCapマージン、AI logicテスト売上、高速基板ASP</strong>だ。

---

## Fact / Inference / Speculation / Blocked

### [Fact]

- Marvell Q1 FY2027の売上は$2.418Bで前年比+28%、Q2売上ガイダンスは$2.70B ±5%だ。([Marvell][1])
- Marvell Q1 non-GAAP gross marginは58.9%、Q2 non-GAAP gross marginガイダンスは58.25〜59.25%だ。([Marvell][1])
- Marvellは成長ドライバーとして800G/1.6T scale-out optics、51.2T Ethernet switches、scale-up optical、DCI modules、custom XPU、XPU-attachを挙げた。([Marvell][1])
- NVIDIAはMarvellに20億ドルを投資し、MarvellはNVLink Fusion互換のcustom XPUとscale-up networkingを提供すると発表した。([Marvell NVIDIA][3])
- Samsung Electro-Mechanics Q1 2026のPackage Solution売上は7,250億ウォンで前年比45%・前四半期比12%増加した。([Samsung Electro-Mechanics Q1][4])
- Samsung Electro-Mechanicsは1兆5,570億ウォン規模のシリコンキャパシタ供給契約を締結し、契約期間は2027年1月1日〜2028年12月31日だ。([Samsung Electro-Mechanics SiCap][5])

### [Inference]

- Marvellの成長軸は韓国においてSamsung Electro-Mechanics FCBGA/MLCC/SiCap、Samsung Electronics・SK Hynixのmemory attach、テストソケット、高速基板の順に翻訳するのが合理的だ。
- HBMは依然として本流だが、今回の決算が新たに示したincremental alphaはHBM大型株よりも接続・パッケージング・電力安定化・テストレイヤーに大きい。
- Samsung Electro-Mechanicsのre-ratingはMLCC回復ではなく、AIインフラpassive/substrateプラットフォームへの転換として捉えるべきだ。

### [Speculation]

- Samsung Electro-MechanicsのSiCap顧客が特定の北米ハイパースケーラーまたはAIアクセラレーターのサプライチェーンと繋がっている可能性は市場で推測されているが、契約相手方は公開されていない。
- 国内テストソケット企業がMarvellまたはMarvell顧客のcustom XPUプログラムに直接参加しているかどうかは、公開情報のみでは特定できない。
- AI-RANは長期的に韓国のRF・ネットワーク半導体の機会を生み出す可能性があるが、2026年の短期業績モメンタムとして見るには時期尚早だ。

### [Blocked]

- Marvellのcustom XPU・optical・switchプログラムごとの韓国企業への直接供給有無。
- Samsung Electro-MechanicsのSiCap契約の顧客名、製品別マージン、月次ramp速度。
- ISC・リノ工業・TSEのAI logic顧客別売上比率。
- 韓国PCB/基板銘柄の2026年現在のリアルタイムNTM PER、EV/EBITDA、コンセンサスEPS上方修正率。

---

## Sources

[1]: https://investor.marvell.com/news-events/press-releases/detail/1023/marvell-technology-inc-reports-first-quarter-of-fiscal-year-2027-financial-results "Marvell Technology, Inc. Reports First Quarter of Fiscal Year 2027 Financial Results"
[2]: https://stockanalysis.com/stocks/mrvl/transcripts/583849-q1-2027/ "Marvell Technology Q1 2027 Earnings Call Transcript & Audio"
[3]: https://investor.marvell.com/news-events/press-releases/detail/1019/nvidia-ai-ecosystem-expands-as-marvell-joins-forces-through-nvlink-fusion "NVIDIA AI Ecosystem Expands as Marvell Joins Forces Through NVLink Fusion"
[4]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Announces Q1 2026 Business Performance"
[5]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
[6]: https://semiconductor.samsung.com/news-events/news/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026/ "Samsung Unveils HBM4E at NVIDIA GTC 2026"

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
