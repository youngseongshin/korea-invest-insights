---
title: "韓国クオリティ・リレーティングWatch 2026-09-07: マクロデータ更新待ち"
date: 2026-09-07T16:30:00+09:00
categories: ["daily-wrap"]
tags: ["KOSPI", "KOSDAQ", "韓国株", "Quality Compounder", "Smart Money", "Cycle Rerating", "PEAD", "韓国市場"]
series: ["korea-quality-rerating-watch"]
slug: "kr-daily-wrap-2026-09-07"
description: "2026年9月7日の韓国株。マクロレジームのデータソース更新中のためKOSPI・スクリーナー判断を保留。フレームワーク概要と更新予定を掲載。"
draft: false
---

## 1. マクロダッシュボード

本日（2026-09-07）のレジーム判定は生成されていません。

| 指標 | 値 | 状態 |
|---|---|---|
| KOSPI | — | 取得中 |
| KOSDAQ | — | 取得中 |
| USD/KRW | — | — |
| VIX | — | — |
| Brent | — | — |
| 米国10年債利回り | — | — |
| レジーム（KR / US） | UNKNOWN | データ不足で判定保留 |

**判定保留の理由：** `kr_screener`・`us_screener`・`kr_derivative:10d` の3データソースについて、デフォルト値への後退・データ鮮度不足・カバレッジ欠損が確認されました。7入力中7つは現行値を取得できていますが、上記3ソースの品質問題によりレジーム判定を生成しない設計になっています。原典スクリーナーとデリバティブ・パッシブスナップショットの更新後に再実行します。

---

## 2. マーケットラップ

本日は同日付けの `KR CLOSE BRIEFING` および `KR MARKET SNAPSHOT` が提供されていません。

KOSPI・KOSDAQの引値、セクター騰落率、外国人・機関の売買動向については当日データが確認できないため、本セクションの詳細記述を省略します。データソースの更新後、本稿を速やかに改訂します。

---

## 3. 本日のクオリティ・リレーティング候補

`KR META SCREENER` が本日未取得のため、銘柄ランキングを生成できません。

以下は、本シリーズが通常使用するスクリーニング・フレームワークの概要です。

### スクリーニング・フレームワーク

| 層 | スクリーナー | 役割 |
|---|---|---|
| コア | KR Quality Compounder | 高収益・継続的競争優位を持つ企業を選別 |
| 需給確認 | KR Smart Money Quality | 機関・外国人資金の流入を確認 |
| 再評価シグナル | KR Cycle Rerating | 業績レバレッジが市場に再評価される局面を補足 |
| 触媒 | KR Smart Money Earnings | 業績改善トレンドに資金が乗っている銘柄 |
| 触媒 | KR PEAD | 決算発表後のドリフトが継続している銘柄 |

**候補の優先順位（スクリーナー重複数基準）：**

1. Quality Compounder ＋ Smart Money Quality ＋ Cycle Rerating（3重複）
2. Quality Compounder ＋ Smart Money Quality
3. Quality Compounder ＋ Cycle Rerating
4. Smart Money Quality ＋ Smart Money Earnings / PEAD

2スクリーナー以上で重複する銘柄が本シリーズの主な分析対象です。3重複以上の銘柄は、「良いビジネスに資金が入り、市場が再評価を始めている」ケースとして最優先で取り上げます。スクリーナーデータが更新され次第、上位10銘柄のランキング表（ティッカー・重複数・主要指標）を掲載します。

---

*本記事は公開市場データに基づく情報提供を目的としており、特定銘柄の売買推奨を含みません。*