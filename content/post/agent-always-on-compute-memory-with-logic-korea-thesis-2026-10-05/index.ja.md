---
title: "計算を節約し、記憶を積み上げる: エージェント時代に韓国メモリーがロジックを取り込む理由"
date: 2026-10-05T22:20:00+09:00
categories: ["Exclusive Analysis", "AI Infrastructure", "Korean-Equities"]
tags: ["メモリー", "Samsung Electronics", "SK hynix", "HBM", "カスタムHBM", "エージェント", "KVキャッシュ", "エンタープライズSSD", "HBF", "CXL", "長期供給契約"]
slug: "agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05"
description: "仕事を丸ごと任せるAIエージェントが増えると、計算コストは下がり、文脈と知識が蓄積します。バッチ処理とリアルタイム処理の分化、CPU・ネットワーク需要、ロジックを取り込むHBM・SSD、長期契約と預託金を手掛かりに、韓国メモリーの投資論点と現在の株価が求める利益の持続性を検討します。"
image: "cover.png"
draft: false
---

同じAIモデルに同じ質問をしても、処理方法によって価格は大きく異なります。Anthropicの価格表では、Opus 5.5は24時間以内に回答すればよいバッチ処理が通常価格の半額で、速い応答を保証する高速モードは通常価格の2倍です。一度読んだ文脈を再び読む料金は通常価格の20分の1です。[^anthropic-pricing]

この価格表は、AIインフラがどこへ向かうのかを端的に示しています。急がない仕事は安く、急ぐ仕事は高く処理します。そして最も安いのは、新たに計算することではなく、記憶しておいたものを再び取り出すことです。

<strong>仕事を丸ごと任せる委任型エージェントが増えるほど、計算は効率化し、文脈と知識は蓄積します。それらを収めるメモリーとストレージは、汎用品からロジックを取り込んだ製品へと変わりつつあります。韓国メモリー投資で重視すべきなのは、今年の利益の大きさより、その利益がどれだけ長く続くかです。</strong>

検証すべきつながりを順にたどります。インフラが常時コンピューティングへ変わるのか、計算が実際に効率化するのか、何が蓄積するのか、メモリーにロジックが入る変化が売上に表れるのか、その価値が韓国企業に残るのかです。最後に、Samsung ElectronicsとSK hynixの現在の株価がどの程度の利益持続性を織り込んでいるかを計算します。

分析基準日は2026年10月5日です。株価は10月2日の終値で、10月5日の韓国通常取引時間中の約定記録はありませんでした。会社発表、調査機関の見通し、本稿の計算上の前提を区別して記します。以下の感応度表は検証用の計算であり、目標株価ではありません。

<link rel="stylesheet" href="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/thesis.css">

## インフラは呼び出しに応える設備から、目標を持続して追う設備へ変わります

チャットボットは質問が届いたときだけ計算します。委任型エージェントは異なります。ユーザーから目標を任されると、計画を立て、ツールを使い、結果を確認し、必要なら再度試します。ユーザーが画面を閉じても作業は続きます。

そのため、負荷の単位が変わります。チャットボット時代の負荷は、同時に接続するユーザー数に近いものでした。エージェント時代の負荷は、ユーザー数に、1人当たりの委任目標数と各目標が稼働する時間を掛けた値に近づきます。これが目標指向型の常時コンピューティングです。

すでに製品や価格表にその兆しがあります。AnthropicのManaged Agentsはトークン料金とは別に、セッションが稼働している時間に対して1時間当たり0.08ドルを課金します。セッションが状態を維持するため、バッチ割引の対象にならないと説明しています。[^anthropic-pricing][^managed-agents]

Googleは2026年5月の開発者イベントで、専用仮想マシン上で一日中動くパーソナルエージェントを紹介しました。同じ発表で、月間処理トークン数が2025年5月の約480兆個から2026年5月には3,200兆個超へ増えたと明らかにしました。1年間で約7倍です。会社公表の数値であり、そのうちエージェントが占める割合は公表されていません。[^google-io]

作業時間も長くなっています。評価機関METRの2026年1月の測定では、Claude Opus 4.5が50%の確率で完了できる課題の長さは人間の作業時間換算で320分でした。2024年以降、この長さは約89日ごとに倍増しました。課題群の上位には不確実性があるとMETR自身も認めています。[^metr]

以下の図は、本稿全体の論理の連鎖です。各矢印は事実ではなく、検証すべきつながりです。

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/chain.svg" alt="委任型エージェントから常時コンピューティング、計算の効率化と状態の蓄積、ロジックを取り込んだメモリー、利益の持続性へ至る論理の連鎖"><figcaption>概念図。需要の増加と、その価値がメモリーメーカーに残ることは別々のつながりです。モバイルでは図を横にスクロールして読めます。</figcaption></figure>

## 急ぐ仕事と急がない仕事の価格差は最大4倍です

常時稼働する仕事がすべて急ぎとは限りません。一晩かけて文書を整理する仕事と、ユーザーが待っている回答に同じ設備を使う必要はありません。モデル各社はこの違いを価格に反映しています。

| 会社・モデル | バッチまたは低速 | 標準 | 高速または優先 | キャッシュ済み文脈の読み込み |
|---|---:|---:|---:|---:|
| Anthropic Opus 5.5 | 0.5倍 | 1倍 | 2倍 | 0.05倍 |
| OpenAI gpt-6-astra | 0.5倍 | 1倍 | 2倍 | 0.1倍 |
| Google Gemini 3.1 Pro Preview | 0.5倍 | 1倍 | 1.8倍 | 別途保存料金 |

3社とも、同じモデルの価格を応答速度に応じて分けています。最安プランと最高プランの差は3.6倍から4倍です。Googleはキャッシュに文脈を保存する時間にも料金を課します。文脈の保存が独立した商品になったことを示します。[^anthropic-pricing][^openai-pricing][^google-pricing]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/pricing.svg" alt="Anthropic Opus 5.5の標準入力価格を基準にしたバッチ、高速、キャッシュ読み込みの価格倍率を示す棒グラフ"><figcaption>Anthropic公式価格表に基づく。2026年10月5日閲覧。標準入力価格を1とした倍率です。キャッシュ読み込みは、処理済みの文脈を再利用する際の入力価格です。</figcaption></figure>

この価格差が投資家にとって重要なのは、設備稼働率に関わるためです。リアルタイム需要だけを受ける設備は、昼夜で稼働率の差が大きくなります。急がない仕事を空いている時間に安く受ければ、同じ設備を一日中動かせます。常時コンピューティングは需要量を増やすだけでなく、設備の休止時間を減らします。

## 繰り返す仕事は小型モデルとコードに移ります

エージェントが同種の仕事を1日に数万回行うなら、そのたびに最大モデルを呼び出す必要はありません。繰り返す細かな作業は2つの方向に移ります。1つはその作業に特化した小型モデル、もう1つはモデルを使わずに動くコードです。

小型モデルを裏付けるのは価格表です。OpenAIの価格表では、gpt-6-astraの入力価格は100万トークン当たり10ドル、gpt-6-lunaは0.10ドルです。同じ会社のモデルで100倍の差があります。NVIDIAの研究者は2025年の論文で、エージェント呼び出しの40～70%を特化型小型モデルに置き換えられると推定しました。論文上の推定であり、実測比率ではありません。[^openai-pricing][^nvidia-slm]

コードについては製品文書が根拠です。AnthropicのAgent Skills文書によると、スキル内のスクリプトはシェルで実行され、その結果だけがモデルの文脈に入ります。スクリプトのコード自体は文脈に入りません。モデルが毎回推論していた手順を、一度固定したコードに置き換える仕組みです。[^agent-skills]

ウェブ自動化企業Skyvernは、エージェントが一度実行した作業をコードに変換し、モデルなしで再生した結果を公表しました。実行時間は279秒から120秒に、1回当たりの費用は0.11ドルから0.04ドルに減りました。企業による独自測定です。[^skyvern]

ここでは重要な区別があります。仕事1件当たりの計算量は減ります。しかし、固定したコード、特化型モデルの重み、実行記録はどこかに保存する必要があります。効率化は計算を減らす一方で、保存したものをより多く使うことで進みます。

## GPUだけでは仕事は完結しません

エージェントの仕事はいくつもの段階に分かれます。考える段階はGPUが担います。ツールの実行、ファイルの操作、隔離環境でのコード実行はCPUが担います。段階間のデータ転送はネットワークが担います。

CPU需要については、今年、複数社から同じ方向の発言がありました。AmazonのAndy Jassy CEOは7月の決算説明会で、エージェントのツール利用の大半はAIアクセラレーターではなくCPU上で動くと述べました。AMDのLisa Su CEOは8月、サーバーCPU市場が2030年に2,200億ドルとなり、エージェントと隔離実行環境が最大の部分を占めると予想しました。いずれも経営陣の説明と見通しです。[^amzn-call][^amd-call]

実物のシグナルもあります。TrendForceは4月、サーバーCPU価格が3月以降10～20%上昇し、納期が1～2週間から8～12週間に延びたと伝えました。台湾と日本のメディアを引用した二次報道です。NVIDIAはエージェントの隔離実行を用途に明記した88コアのVera CPUを出荷しました。[^tf-cpu][^nvda-vera]

ネットワークも一種類ではありません。ラック内でチップ同士を接続する仕組み、ラック間をつなぐイーサネット、メモリーを拡張するCXLが併用されます。Broadcomは9月の決算説明会で、AIネットワーキング売上が前年の2.5倍を超え、光通信レーザーの需要が供給を大幅に上回ると述べました。[^avgo-call]

データ処理装置も独立して登場しています。NVIDIAは3月、ストレージの前段で文脈データを管理するBlueField-4ベースの設計を発表し、パートナー製品は2026年下半期に登場すると明らかにしました。10月5日時点で実際の出荷と稼働を確認できる資料は見つかりませんでした。[^nvda-stx]

ここでの結論は、GPUの重要性が下がるということではありません。GPU、CPU、データ処理装置、複数種類のネットワークが一緒に必要になるということです。そして、これらすべての装置にメモリーが搭載されます。

## 計算は再利用できますが、文脈と知識は積み上がります

ここまでの流れを一文にまとめると、エージェントインフラは同じ計算を二度行わないために記憶を増やします。

言語モデルは長い文脈を読む際に中間計算結果を作ります。これをKVキャッシュと呼びます。キャッシュを保存しておけば、同じ文脈を再び読むときに最初から計算する必要がありません。冒頭の価格表でキャッシュ済み文脈が通常価格の20分の1である理由はここにあります。

キャッシュの容量は小さくありません。IBMは6月発行の技術文書で、1リクエスト当たりのKVキャッシュを中型モデルで約3～10GB、大型モデルで40～80GBと推定しました。キャッシュの再利用によって、13万トークンの入力から初回応答までの時間が56分の1になったと報告しています。企業独自の測定です。[^ibm-kv]

NVIDIAはこのキャッシュを保存する階層を新たに定義しました。GPU内のHBM、サーバーのメモリー、サーバー内のSSDの下に、イーサネットで接続したフラッシュストレージ層を設け、CMXと名付けました。キャッシュをどの階層に置くかを決めるソフトウェアも公開しました。[^nvda-cmx][^nvda-dynamo]

メモリー各社の決算発表にも同じ言葉が登場します。Micronは9月30日の発表で、データセンターSSDの売上が四半期に100億ドル近くとなり、前年の10倍を超えたと明らかにしました。理由の一つとして、KVキャッシュを下位層に移して保存する文脈ストレージを挙げました。[^mu-remarks]

SK hynixは7月の決算説明会で、エンタープライズSSDの売上が前四半期の2倍になったと述べ、新たな用途としてKVキャッシュの保存とGPU近傍に置くストレージを挙げました。Samsung ElectronicsはサーバーSSDが2026年のNAND売上の60%を超えると予想しました。両社の発言は決算説明会の書き起こしを再掲載したメディアで確認しました。[^skh-call][^sec-call]

ハードディスク企業Western DigitalのCEOは8月、この違いを次のように表現しました。計算サイクルは再利用できる一方、データは複利で蓄積するというものです。エージェントは各段階で記録を残し、その記録が次の仕事の材料になります。[^wdc-call]

ただし、増加率と金額は分けて考える必要があります。個人エージェント1人分の記憶は、容量で見れば大きくありません。金額を押し上げるのは、推論サービス全体がキャッシュをフラッシュに移して保存する設計へ変わるかどうかです。この移行はまだ初期段階です。

## メモリーは汎用品からロジックを取り込んだ製品へ変わっています

蓄積するデータが増えると、顧客がメモリーに求めるものも変わります。容量だけでなく、必要なときに取り出せるか、消費電力はどの程度か、自社チップとの適合性は高いかを問うようになります。こうした要求に応えるには、メモリーにロジックを組み込む必要があります。

SK hynixは7月、米国上場の目論見書にこの変化を直接記しました。従来のメモリー企業は汎用部品を供給してきたが、AI時代のメモリーは性能最適化で重要な役割を果たすとし、会社のビジョンを「フルスタックAIメモリークリエーター」と表現しました。会社による自己定義であり、業績で立証された事実とは区別する必要があります。[^skh-424b4]

最も進んだ事例はHBMのベースダイです。HBMはメモリーチップを複数層積み重ねた製品で、ベースダイは最下層で信号と電力を扱うチップです。前世代まではメモリープロセスで製造していました。HBM4からはロジックプロセスで製造します。Samsung Electronicsは自社の4ナノプロセスを使います。SK hynixは2024年、HBM4のベースダイをTSMCのロジックプロセスで製造する協業を発表しました。[^sec-hbm4][^skh-tsmc]

次の段階は、顧客のロジックをベースダイに組み込むカスタムHBMです。NVIDIAは8月26日、自社のメモリー制御回路をHBMベースダイに組み込むNVHBMを発表しました。標準HBM4Eに比べて帯域幅が30%増え、電力が15%減るというのはNVIDIAの主張です。Micronは9月30日、この製品をNVIDIAと共同開発すると明らかにしました。[^nvda-nvhbm][^mu-remarks]

Samsung Electronicsは8月、半導体学会Hot Chipsでさらに先の段階を示しました。制御回路を移す段階、ベースダイに演算素子を組み込んでプロセッサの計算の一部を担わせる段階、メモリーを演算チップ上に直接積層する段階です。発売時期は示しませんでした。[^sec-hotchips]

ストレージや他のメモリーにも同じ方向の製品が登場しています。ただし、成熟度は製品ごとに大きく異なります。

| 製品 | 組み込むロジック | 現在の段階 |
|---|---|---|
| HBM4ベースダイ | ロジックプロセスによる信号・電力制御 | 量産、売上発生 |
| SOCAMM2 | サーバー向け低消費電力メモリーモジュール | 量産、販売増加 |
| エンタープライズSSD | 制御チップとファームウェア、文脈保存向け設計 | 量産、売上急増 |
| カスタムHBM、NVHBM | 顧客のメモリー制御回路 | 開発中、次世代GPUへの搭載予定 |
| CXLメモリーモジュール | 頻繁に使うデータを識別する監視回路 | Samsungは2026年末の量産目標と報道、遅延の可能性 |
| HBF | NANDを演算チップ近くに配置する高帯域インターフェース | 2026年8月に初の技術仕様を公開、製品化前 |
| PIM、演算素子内蔵HBM | メモリー内の演算回路 | 試作品とロードマップ |

量産段階と記した製品は、今年の業績資料で確認できます。Samsung Electronicsの第2四半期業績資料は、ファウンドリー事業の業績要因としてHBMベースダイ需要の増加を挙げました。カスタムHBMから下の製品は、まだ売上として確認できません。SK hynixはHBM4Eまで従来の接合方式を維持すると述べました。また、CXLはHBMの代替ではなく補完的な階層だという評価が9月の業界イベントで示されました。[^sec-ir][^skh-q2][^tf-cxl][^hbf-ocp][^sec-fms][^skh-hybrid][^tf-cxl-doubt]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/maturity.svg" alt="ロジックを取り込んだメモリー製品を、売上発生、開発・サンプル、ロードマップの3段階に分けた図"><figcaption>会社発表と業績資料に基づく段階分類です。左に行くほど今年の業績で確認でき、右に行くほど日程が定まっていません。2026年10月5日時点。</figcaption></figure>

したがって、メモリーがロジックを取り込むという見方は方向としては正しく、対象範囲はまだ限られています。現在売上で確認できるのはHBM4、サーバーモジュール、エンタープライズSSDです。汎用DRAMとNANDは依然として規格と価格で競争しています。

## メモリーがコンピューティングの中心になる仮説は、方向性だけ確認されています

さらに先の仮説は、コンピューティングの構造そのものが変わるというものです。現在のコンピューターでは演算装置が中心にあり、メモリーがデータを運びます。データが演算より速く増えると、データを移動するコストが計算コストを上回ります。その場合、データがある場所で計算する方が合理的です。

この方向の試みは各所で始まっています。Samsung Electronicsのロードマップ最終段階では、メモリーを演算チップ上に直接積層します。Qualcommは2027年の製品に演算とメモリーを3次元で統合した構造を採用すると発表しました。SK hynixとSandiskはNANDを演算チップのすぐ隣に配置する規格をGoogle、Tenstorrentと共同で策定しています。[^sec-hotchips][^qcom-hbc][^hbf-ocp]

SandiskのCEOは8月の決算説明会で、AIは本質的にメモリー中心でストレージ集約型の問題だと表現しました。メモリー企業のCEOによる発言である点は考慮が必要です。[^sndk-call]

この仮説に対する判断を明確にしておきます。2026年現在、メモリー中心コンピューティングは投資根拠ではなく、将来の選択肢です。独立した性能検証も量産日程もなく、顧客の採用も確認されていません。現在の株価を説明する材料にはなりません。ただし、この方向が正しければ、最大の恩恵を受けるのはメモリー、ロジックプロセス、積層技術を併せ持つ企業です。

## 韓国メモリーの投資論点は利益の大きさから持続期間へ移ります

ここから韓国企業に移ります。今年の利益はすでに大きくなっています。Samsung Electronicsの半導体部門の第2四半期営業利益はKRW 89.2 trillionで、売上高の70%でした。SK hynixの第2四半期営業利益はKRW 60.5 trillionで、売上高の76%でした。[^sec-ir][^skh-q2]

しかし株価はこの利益を高く評価していません。10月2日終値を基準にすると、Samsung Electronicsは2026年予想利益の5.85倍、SK hynixは5.25倍で取引されています。予想利益はNaver Financeが集計した証券会社平均です。[^naver-sec][^naver-skh]

低い倍率は、市場がメモリーを依然として景気循環産業と見ていると解釈できます。現在の利益は供給不足から生まれ、増設が終われば以前のように急減するという懸念です。これは解釈ですが、根拠はあります。SK hynix自身が目論見書のリスク要因に、メモリー産業で供給過剰が繰り返されてきたことを記しています。[^skh-424b4]

ロジックを取り込んだメモリーが投資上重要になるのはここです。この変化が今年の利益をさらに押し上げるわけではありません。供給が正常化した後も、利益が過去ほど落ち込まない理由を作れるかが核心です。その理由は切り替えコストと契約構造にあります。

第一に、顧客が供給先を変えにくくなることです。顧客のチップに合わせて設計したベースダイは、他社製に簡単には置き換えられません。設計、検証、認証にかかる時間が切り替えコストになります。実際の切り替えコストの大きさと、それが価格に反映されるかは、まだ確認されていない仮説です。

第二に、契約構造です。Micronは9月30日、戦略顧客との契約を26件締結したと発表しました。複数年にわたり、約束した数量を購入しなくても支払いが生じる構造です。顧客から受けた金融上のコミットメントは320億ドルで、その大半は現金預託金です。Micronはこの見通しを根拠に設備投資を増やすと述べました。[^mu-remarks]

韓国の2社も同じ方向に進んでいます。SK hynixは第2四半期に約10社の顧客と長期供給契約の交渉を終えたと発表し、決算説明会では預託金などの金融的な仕組みが含まれると説明しました。Samsung Electronicsは生産能力の60～70%を長期契約に割り当てる計画で、基本契約は5年、以後は毎年延長する方式だと述べました。契約ごとの価格と解約条件は公表されていません。[^skh-q2][^skh-lta][^sec-lta]

顧客が先に資金を預け、数量を約束する産業は、汎用品をスポット市場で売買する産業とは異なる動きをします。ただし長期契約には両面があります。TrendForceは長期契約の価格設定によって、一部供給企業のサーバーDRAM値上げ幅が市場平均を下回ると記しました。下落局面の下支えを得る代わりに、上昇局面の上値を譲った形です。[^tf-memory]

## Samsung ElectronicsとSK hynixは同じ変化に異なる立場で向き合います

両社は、ロジックを取り込むメモリーという同じ変化に対し、異なる強みと弱みを持っています。

| 項目 | Samsung Electronics | SK hynix |
|---|---|---|
| 第2四半期半導体営業利益率 | 70% | 76% |
| HBM4ベースダイ | 自社4ナノプロセス | TSMCプロセス |
| ロジック価値の帰属、本稿の分析 | ファウンドリー利益として社内に残る可能性 | 外部に支払うコスト |
| 製品の幅 | HBM、サーバーモジュール、SSD、ファウンドリー、パッケージング | HBM、サーバーモジュール、SSD、HBF規格を主導 |
| 長期契約 | 生産能力の60～70%を割り当てる計画 | 約10社の顧客と交渉完了 |
| 株主還元 | 第3四半期に約KRW 30 trillionの配当を計画 | KRW 40 trillionの自社株消却を決議 |
| 2026年予想利益に対する株価 | 5.85倍 | 5.25倍 |

SK hynixの強みは、現在の収益性と顧客との関係です。営業利益率が高く、約10社の顧客と長期供給契約の交渉をすでに終えています。弱みはロジックの価値を社外に支払う点です。TrendForceが韓国メディアを引用して伝えたところでは、TSMC製HBM4ベースダイのコストはメモリーチップの3～4倍です。会社が確認した数値ではありません。[^tf-basedie]

Samsung Electronicsの強みは、ロジックの価値が社内に残る構造です。同社はメモリー、ロジック設計、ファウンドリー、パッケージングをすべて持つ唯一の企業だと自ら紹介しています。[^sec-fms]弱みは、その構造がまだ利益として十分に実証されていないことです。社内製ベースダイの売上を、外部顧客から得た収入のように二重計上してはいけません。連結ベースのコストとキャッシュで確認する必要があります。

株主還元は利益が株主に戻る経路です。SK hynixは8月、KRW 40 trillion規模の自社株取得と全株消却を決議し、フリーキャッシュフロー還元目標を50%以上に引き上げました。Samsung Electronicsは第3四半期に約KRW 30 trillionの現金配当を計画し、10月末の取締役会で確定します。いずれも報道で確認し、開示原文とは照合できていません。[^skh-return][^sec-return]

私の見立ては次のとおりです。メモリーにロジックが入る変化が深まるほど、構造的に有利なのはロジックを内製する企業です。現在の業績と顧客基盤ではSK hynixが先行しています。変化の初期段階ではSK hynixの実行力が、カスタムHBMとその先の段階が本格化するほどSamsung Electronicsの統合構造が、より大きな価値を持つ可能性があります。転換点は、Samsung Foundry製ベースダイが外部顧客の設計を受けて量産される時です。

## 現在の株価は今年の利益の半分強が残ると想定しています

株価を単純化すると、市場が持続可能と考える利益に評価倍率を掛けた値です。市場がメモリー企業に10倍を付けると仮定して逆算すれば、現在の株価が求める利益水準が分かります。

Samsung Electronicsの10月2日終値はKRW 276,000です。10倍を適用すると、株価が求める1株利益はKRW 27,600です。2026年予想1株利益KRW 47,142の58.5%に当たります。SK hynixの終値はKRW 1,842,000で、同じ計算による必要1株利益はKRW 184,200です。予想1株利益KRW 350,576の52.5%です。[^naver-sec][^naver-skh]

つまり現在の株価は、2026年利益の半分強だけが今後も残るという想定と整合します。これが市場の正確な考えだという意味ではありません。倍率と利益の組み合わせは複数あります。ただし、問いは明確になります。ロジックを取り込んだ製品と長期契約は、正常化後の利益を今年の半分より高い水準に維持できるでしょうか。

以下の表は、2026年予想利益のうち残る割合と評価倍率を変えたものです。括弧内は10月2日終値に対する変化率です。残存割合と倍率はいずれも本稿の計算上の仮定で、確率を付与していません。配当は含みません。

Samsung Electronics、基準株価KRW 276,000

| 2026年予想利益の残存割合 | 8倍 | 10倍 | 12倍 |
|---|---:|---:|---:|
| 40% | KRW 151,000 (-45.3%) | KRW 189,000 (-31.7%) | KRW 226,000 (-18.0%) |
| 55% | KRW 207,000 (-24.8%) | KRW 259,000 (-6.1%) | KRW 311,000 (+12.7%) |
| 70% | KRW 264,000 (-4.3%) | KRW 330,000 (+19.6%) | KRW 396,000 (+43.5%) |

SK hynix、基準株価KRW 1,842,000

| 2026年予想利益の残存割合 | 8倍 | 10倍 | 12倍 |
|---|---:|---:|---:|
| 40% | KRW 1,122,000 (-39.1%) | KRW 1,402,000 (-23.9%) | KRW 1,683,000 (-8.6%) |
| 55% | KRW 1,543,000 (-16.3%) | KRW 1,928,000 (+4.7%) | KRW 2,314,000 (+25.6%) |
| 70% | KRW 1,963,000 (+6.6%) | KRW 2,454,000 (+33.2%) | KRW 2,945,000 (+59.9%) |

表の両端が論点を示しています。利益が40%しか残らなければ、倍率が12倍に上がっても株価は現在より低くなります。良好な業界ストーリーだけでは利益減少を補えません。逆に利益の70%が残ると市場が信じれば、倍率が10倍のままでも株価は20～33%高くなります。

SK hynixの数字には注意が必要です。第2四半期純利益はKRW 93.9 trillionで、営業利益KRW 60.5 trillionを上回りました。原因は確認できていません。営業外項目による利益なら、通期予想1株利益にも再現性のない利益が含まれている可能性があり、その場合は残存割合をさらに低く見積もる必要があります。[^skh-q2]

再評価の鍵は評価倍率ではなく、利益の残存割合です。ロジックを取り込んだメモリーと長期契約は、その割合を高める要素になり得ます。実際に高めるかどうかは、供給が増える2027年と2028年に明らかになります。

## 最も強い反論はロジックの価値が設計者に帰属することです

この論理には強い反論があります。重要度の高い順に記します。

第一は価値の帰属です。NVHBMでベースダイに入る制御回路を設計したのはNVIDIAです。NVIDIAは複数のメモリー企業が同じ規格を供給すると発表しました。Micronはそのベースダイの製造を外部ファウンドリーに委託します。この構造では設計の価値はNVIDIAに、製造の価値はファウンドリーに帰属し、メモリー企業は再び同じ規格で競争する可能性があります。[^nvda-nvhbm][^mu-foundry]

ストレージでも似たことが起こります。NVIDIAの文脈ストレージ設計では、データ管理の演算はSSD内ではなくNVIDIAのデータ処理装置に置かれます。キャッシュをどの階層に置くか決めるソフトウェアもNVIDIAのものです。データが蓄積する場所と、顧客が離れにくくなる場所は異なる可能性があります。[^nvda-cmx][^nvda-dynamo]

この反論は本稿の論理を最も大きく揺るがします。メモリーにロジックが入ることと、メモリー企業がそのロジックの主導権を持つことは別です。Samsung Electronicsの統合構造を重視する理由もここにあります。ロジックを自ら作れないメモリー企業は、製品の高度化が進むほど、かえって狭い立場に置かれる可能性があります。

第二は需要の適応です。メモリーが高くなれば、顧客は使用量を減らす方法を探します。TrendForceは9月29日、GPUとカスタムチップ企業が装置当たりのHBM容量を減らす方法を検討し、2027年には8層構成を優先して評価すると記しました。Googleの研究者は3月、KVキャッシュのメモリー使用量を6分の1以下にする圧縮技術を公開しました。Anthropicの文書は文脈が長いほど精度が低下すると説明し、古い会話を要約に置き換える機能を提供しています。[^tf-hbm][^turboquant][^anthropic-context]

蓄積の速度が削減技術を上回るか、まだ答えはありません。Micronも、価格の影響でサーバー1台当たりのメモリー搭載量の増加率がやや低下したと認めました。[^mu-remarks]

第三は供給と資金です。TrendForceは7月30日、NAND供給が2027年下半期に緩み、価格下落圧力が生じると予想しました。TrendForceの報道によれば、中国CXMTの第2四半期DRAM売上シェアは9.5%に上昇しました。国際決済銀行（BIS）総裁は9月10日の講演で、大手テクノロジー企業の設備投資がキャッシュフローを上回っていると警告しました。顧客の資金が尽きれば、長期契約の約束も試されます。[^tf-supply][^tf-china][^bis]

Micronは反対に、2027年と2028年の需給は2026年より逼迫すると見ています。調査機関と供給企業の見通しが分かれていること自体が、2027年を断定すべきでない理由です。[^mu-remarks]

需要の前提も検証が必要です。本稿の出発点は、人々がエージェントに仕事を継続して任せることです。Anthropicが2月に公表した自社利用データでは、一度に45分を超えて続いた作業は上位0.1%でした。ほとんどの作業はそれより大幅に短いものです。委任が習慣として定着しなかったり、ユーザーが権限を預けなかったりすれば、常時コンピューティングの普及速度は本稿の想定を下回ります。[^anthropic-autonomy]

## 次の四半期は株価ではなく、利益が残る根拠を確認します

この論理が正しいかは、今後公表される数字で確認できます。確認項目と判断を変える条件を示します。

| 確認項目 | 論理を支持するシグナル | 論理を弱めるシグナル |
|---|---|---|
| 第3四半期決算、10月 | HBM4とエンタープライズSSDの数量増、製品構成の改善 | 利益増の大半が汎用品の価格上昇によるもの |
| 長期契約 | 預託金と最低購入条件の開示、契約更新 | 価格上限による利益の放棄、条件の非開示が続く |
| カスタムHBM | Samsung Foundryのベースダイが外部顧客向けに量産 | 単一規格で3社が価格競争 |
| 文脈ストレージ | CMXパートナー製品の出荷、専用ストレージサーバー契約 | 圧縮技術の普及、出荷遅延 |
| 2027年の供給 | 契約価格の上昇継続、顧客投資計画の上方修正 | NAND価格下落、HBM搭載量の縮小 |

Samsung Electronicsの第3四半期速報値は10月8日と報じられました。FnGuide集計の営業利益平均はKRW 108.1 trillionです。SK hynixは10月末の発表が予想され、営業利益平均はKRW 77.2 trillionです。いずれも10月5日時点の報道に基づき、会社の公式日程は確認できていません。[^consensus]

数字そのものより内容を見る必要があります。営業利益が平均を上回っても、理由が汎用品の価格上昇だけなら本稿の論理とは関係ありません。営業利益が平均を下回っても、HBM4の数量と長期契約の質が改善していれば、利益が残る根拠はむしろ強まります。

判断を変える条件も記しておきます。カスタムHBMが単一規格となってメモリー3社が同じ製品で競争し、同時に2027年の契約価格が下がり始めた場合、本稿の論理は一段階引き下げる必要があります。その場合、韓国メモリー企業はより高度な製品を作っても、依然として循環産業として評価されるでしょう。

<strong>エージェントは計算を節約するために記憶を使います。その記憶を収める製品にロジックが入り、一部の顧客は先に資金を預け始めました。韓国メモリーの再評価は、供給増加後もこの変化が利益を支えるかにかかっています。現在の株価は、まだ今年の利益の半分強しか織り込んでいません。</strong>

## 出典と計算の範囲

会社発表、開示資料、調査機関の資料は2026年10月5日に照合しました。決算説明会の書き起こしを再掲載したメディアで確認した発言は、脚注に記しました。会社公表の性能値は独立検証ではありません。感応度表の残存割合と評価倍率は計算上の仮定であり、予測ではありません。予想1株利益はNaver Financeの集計値をそのまま使用し、2027年予想は確認できていません。

[^anthropic-pricing]: [Anthropic公式価格表](https://platform.claude.com/docs/en/about-claude/pricing)、2026-10-05閲覧。Opus 5.5の標準入力4ドル、バッチ2ドル、高速8ドル、キャッシュ読み込み0.20ドル（100万トークン当たり）。Managed Agentsのセッション料金を含む。

[^managed-agents]: [Claude Managed Agents概要文書](https://platform.claude.com/docs/en/managed-agents/overview)、2026-10-05閲覧。ベータ製品の文書です。

[^google-io]: [Google I/O 2026 Sundar Pichai基調講演まとめ](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)、2026-05。会社公表の数値。

[^metr]: [METR Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/)、2026-01-29。成功率50%を基準とする時間軸。

[^openai-pricing]: [OpenAI API価格表](https://developers.openai.com/api/docs/pricing)、2026-10-05閲覧。gpt-6-astra標準10ドル、Flex 5ドル、Fast 20ドル、キャッシュ入力1ドル。gpt-6-luna入力0.10ドル。

[^google-pricing]: [Gemini API価格表](https://ai.google.dev/gemini-api/docs/pricing)、2026-10-01更新。Gemini 3.1 Pro Preview標準2ドル、バッチ1ドル、Priority 3.60ドル、キャッシュ保存の時間料金。

[^nvidia-slm]: [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153)、NVIDIA研究者、2025-06-02提出。見解を示す論文であり、40～70%は推定値です。

[^agent-skills]: [Anthropic Agent Skills概要文書](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)、2026-10-05閲覧。

[^skyvern]: [Skyvernブログのコード再生測定](https://www.skyvern.com/blog/asking-ai-to-build-scrapers-should-be-easy-right/)、2025-10-17公開、2026-08-24更新。企業独自の測定。

[^amzn-call]: [Amazon 2026年第2四半期決算説明会の再掲載書き起こし](https://www.investing.com/news/transcripts/earnings-call-transcript-amazon-tops-q2-2026-estimates-as-aws-growth-accelerates-93CH-4826442)、2026-07-30。経営陣の発言。

[^amd-call]: [AMD 2026年第2四半期決算説明会の再掲載書き起こし](https://www.fool.com/earnings/call-transcripts/2026/08/11/amd-amd-q2-2026-earnings-call-transcript/)、2026-08-04の説明会。市場規模は会社見通し。

[^tf-cpu]: [TrendForceサーバーCPU価格報道](https://www.trendforce.com/news/2026/04/22/news-server-cpu-prices-up-as-much-as-20-since-march-intel-may-raise-prices-another-8-10-in-2h26/)、2026-04-22。台湾・日本メディアの引用。

[^nvda-vera]: [NVIDIA Vera CPU出荷発表](https://blogs.nvidia.com/blog/vera-cpu-delivery/)、2026-05-18。

[^avgo-call]: [Broadcom FY2026第3四半期決算説明会の再掲載書き起こし](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)、2026-09-02の説明会。経営陣の発言。

[^nvda-stx]: [NVIDIA BlueField-4 STXストレージ構造発表](https://nvidianews.nvidia.com/news/nvidia-launches-bluefield-4-stx-storage-architecture-with-broad-industry-adoption)、2026-03-16。性能値は会社の主張。

[^ibm-kv]: [IBM Redbooks KVキャッシュ技術文書](https://www.redbooks.ibm.com/docs/MD260021/MD260021.html)、2026-06-05発行。会社独自の測定と推定。

[^nvda-cmx]: [NVIDIA CMX製品説明](https://www.nvidia.com/en-us/data-center/ai-storage/cmx/)、2026-10-05閲覧。公開日記載なし。

[^nvda-dynamo]: [NVIDIA Dynamo KVキャッシュ階層化文書](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/kv-cache-offloading)、2026-10-05閲覧。性能値の記載はありません。

[^mu-remarks]: [Micron FY2026第4四半期準備発言](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)、2026-09-30。データセンターSSD売上は原文で「nearly $10 billion」。戦略顧客契約、預託金、NVHBM、需給見通しをこの文書で照合しました。

[^skh-call]: [SK hynix 2026年第2四半期決算説明会の再掲載書き起こし](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q2-2026-results-as-shares-fall-93CH-4818480)、2026-07の説明会。会社公式の書き起こしではありません。

[^sec-call]: [Samsung Electronics 2026年第2四半期決算説明会の再掲載書き起こし](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q2-2026-profit-as-ai-demand-surges-93CH-4822292)、2026-07の説明会。会社公式の書き起こしではありません。

[^wdc-call]: [Western Digital FY2026第4四半期決算説明会まとめ](https://finance.biggo.com/news/US_WDC_2026-08-05)、2026-08-05。二次資料で確認した発言。

[^skh-424b4]: [SK hynix米国上場目論見書、SEC 424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm)、2026-07-09。戦略の節、用語定義のCustom HBM、リスク要因を原文で照合しました。

[^sec-hbm4]: [Samsung Electronics HBM4量産出荷発表](https://news.samsungsemiconductor.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/)、2026-02-12。プロセスと性能は会社説明。

[^skh-tsmc]: [SK hynix・TSMC HBM4協業発表](https://www.prnewswire.com/news-releases/sk-hynix-partners-with-tsmc-to-strengthen-hbm-technological-leadership-302120755.html)、2024-04-18。当時の開発方針の発表です。

[^tf-basedie]: [TrendForceのSK hynix HBM4Eベースダイ報道](https://www.trendforce.com/news/2026/08/31/news-sk-hynix-reportedly-weighs-intel-for-hbm4e-base-dies-amid-tsmc-cost-pressure-and-supply-diversification/)、2026-08-31。韓国メディアの引用で、会社は確認していません。

[^nvda-nvhbm]: [NVIDIA NVHBM発表](https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory/)、2026-08-26。帯域幅と電力の数値は会社の主張。

[^sec-hotchips]: [ServeTheHomeによるSamsung Electronics Hot Chips 2026発表まとめ](https://www.servethehome.com/samsung-evolving-hbm-base-die-at-hot-chips-2026/)、2026-08-23。ロードマップは会社発表で、日程はありません。

[^sec-ir]: [Samsung Electronics 2026年第2四半期業績説明資料](https://images.samsung.com/kdp/ir/events/2026/2026_2Q_conference_kor.pdf)、2026-07-30。半導体部門売上KRW 127.5 trillion、営業利益KRW 89.2 trillion。ファウンドリー業績要因としてHBMベースダイを記載。

[^skh-q2]: [SK hynix 2026年第2四半期業績発表](https://news.skhynix.com/en/q2-2026-business-results/)、2026-07-29。売上KRW 79.3 trillion、営業利益KRW 60.5 trillion、純利益KRW 93.9 trillion、長期供給契約、SOCAMM2。

[^tf-cxl]: [TrendForceのSamsung・SK hynix CXL 3.2報道](https://www.trendforce.com/news/2026/07/21/news-samsung-reportedly-targets-2026-cxl-3-2-mass-production-sk-hynix-advances-new-ai-memory-architecture/)、2026-07-21。二次報道。

[^hbf-ocp]: [Sandisk・SK hynix HBF初のOCP仕様公開](https://www.storagenewsletter.com/2026/08/05/fms-2026-sandisk-and-sk-hynix-advance-global-standardization-of-high-bandwidth-flash-with-release-of-first-ocp-technical-specification/)、2026-08-05。

[^sec-fms]: [StorageReviewによるSamsung Electronics FMS 2026発表まとめ](https://www.storagereview.com/news/samsung-outlines-3d-memory-roadmap-for-ai-infrastructure-at-fms-2026)、2026-08-04。PIM搭載低消費電力メモリーを公開、量産時期は未確認。

[^skh-hybrid]: [Tom's HardwareによるSK hynix Hot Chips 2026発表報道](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling)、2026-08-24。

[^tf-cxl-doubt]: [TrendForce AI Infrastructure Summit報道](https://www.trendforce.com/news/2026/09/18/news-openai-intel-reportedly-downplay-cxl-as-hbm-replacement-citing-use-case-and-data-transfer-limits/)、2026-09-18。二次報道。

[^qcom-hbc]: [Qualcommデータセンターロードマップ発表](https://www.qualcomm.com/news/releases/2026/06/qualcomm-unveils-comprehensive-data-center-roadmap-for-the-agent)、2026-06。性能値は会社基準で、独立検証前です。

[^sndk-call]: [Sandisk FY2026第4四半期決算説明会の再掲載書き起こし](https://www.fool.com/earnings/call-transcripts/2026/08/12/sandisk-sndk-q4-2026-earnings-call-transcript/)、2026-08-05の説明会。

[^naver-sec]: [Naver Finance Samsung Electronics日次価格](https://m.stock.naver.com/api/stock/005930/price?pageSize=5&page=1)と[年間業績集計](https://m.stock.naver.com/api/stock/005930/finance/annual)、2026-10-05閲覧。10-02終値KRW 276,000、2026年予想1株利益KRW 47,142。

[^naver-skh]: [Naver Finance SK hynix日次価格](https://m.stock.naver.com/api/stock/000660/price?pageSize=5&page=1)と[年間業績集計](https://m.stock.naver.com/api/stock/000660/finance/annual)、2026-10-05閲覧。10-02終値KRW 1,842,000、2026年予想1株利益KRW 350,576。

[^skh-lta]: [NewspimによるSK hynix第2四半期決算説明会報道](https://www.newspim.com/news/view/20260729000198)、2026-07-29。預託金に関する発言は報道で確認。

[^sec-lta]: [The ElecによるSamsung Electronics第2四半期決算説明会全文](https://www.thelec.kr/news/articleView.html?idxno=60316)、2026-07-30。長期契約の比率と方式は経営陣の計画。

[^tf-memory]: [TrendForce 2026年第4四半期メモリー契約価格見通し](https://www.trendforce.com/presscenter/news/20260930-13258.html)、2026-09-30。見通しであり実現価格ではありません。

[^skh-return]: [ZDNet KoreaによるSK hynix自社株消却報道](https://zdnet.co.kr/view/?no=20260819161157)、2026-08-19。開示原文とは未照合。

[^sec-return]: [Samsung Electronics 2026年株主還元発表報道](https://v.daum.net/v/20260821172850433)、2026-08-21。計画であり、支払い済みの金額ではありません。

[^mu-foundry]: [The ElecによるMicronベースダイ外注報道](https://www.thelec.net/news/articleView.html?idxno=14372)、2026-10-02。Micronの準備発言原文にファウンドリー名はありません。

[^tf-hbm]: [TrendForce 2027年HBM見通し](https://www.trendforce.com/presscenter/news/20260929-13255.html)、2026-09-29。調査機関の見通し。

[^turboquant]: [Google Research TurboQuant紹介](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)、2026-03-24。研究結果であり、商用サービスへの適用範囲は確認できていません。

[^anthropic-context]: [Anthropicコンテキストウィンドウ文書](https://platform.claude.com/docs/en/build-with-claude/context-windows)と[コンパクション文書](https://platform.claude.com/docs/en/build-with-claude/compaction)、2026-10-05閲覧。

[^anthropic-autonomy]: [Anthropicのエージェント自律性測定研究](https://www.anthropic.com/research/measuring-agent-autonomy)、2026-02-18。自社利用データの99.9パーセンタイル値。

[^tf-supply]: [TrendForce 2026～2027年メモリー需給見通し](https://www.trendforce.com/presscenter/news/20260730-13158.html)、2026-07-30。調査機関の見通し。

[^tf-china]: [TrendForceによるCXMT・YMTC増産報道](https://www.trendforce.com/news/2026/09/24/news-cxmt-ymtc-ramp-memory-capacity-but-chinas-ai-cloud-boom-could-soak-up-new-supply-through-2027/)、2026-09-24。二次報道。

[^bis]: [国際決済銀行総裁講演](https://www.bis.org/speeches/20260910-artificial-intelligence-growth-and-financial-stability-challenges-central-banks)、2026-09-10。

[^consensus]: [MoneyTodayによる第3四半期業績見通し報道](https://www.mt.co.kr/amp/stock/2026/10/05/2026100217315021825)、2026-10-05。FnGuide集計の引用。

*免責事項: 本資料は調査および情報提供を目的としています。銘柄、倍率、シナリオは分析例であり、投資判断には読者自身による別途の検討が必要です。*
