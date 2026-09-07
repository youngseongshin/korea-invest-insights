---
title: "한국 퀄리티 리레이팅 워치 2026-09-07: 핵심 입력 차단 — 스크리너 갱신 후 업데이트 예정"
date: 2026-09-07T16:30:00+09:00
categories: ["daily-wrap"]
tags: ["KOSPI", "Korea stocks", "Quality Compounder", "Smart Money", "Cycle Rerating", "한국증시", "수급분석", "데이터점검"]
series: ["korea-quality-rerating-watch"]
slug: "kr-daily-wrap-2026-09-07"
description: "2026-09-07 한국 퀄리티 리레이팅 워치 — 스크리너·파생 입력 차단으로 레짐 및 후보 판단 보류. 갱신 후 업데이트 예정."
draft: false
---

## 1. 매크로 대시보드

| 항목 | 수치 | 비고 |
|------|------|------|
| KOSPI | — | 당일 데이터 미수신 |
| KOSDAQ | — | 당일 데이터 미수신 |
| USD/KRW | — | 당일 데이터 미수신 |
| VIX | — | 당일 데이터 미수신 |
| Brent | — | 당일 데이터 미수신 |
| US 10Y | — | 당일 데이터 미수신 |

**레짐 판단: 차단됨**

오늘(2026-09-07) 매크로 레짐 산출 시스템이 핵심 입력 3종(`kr_screener`, `us_screener`, `kr_derivative:10d`)의 기본값·노후화·커버리지 문제를 감지해 판단을 생성하지 않았다. 현재 입력 상태는 10개 중 7개 정상, 3개 갱신 필요. 원천 스크리너와 파생·패시브 스냅샷을 갱신한 뒤 재실행할 예정이다.

한국 시장(KR) 및 미국 시장(US) 레짐 모두 **UNKNOWN** 상태다. 이 판단이 복원되기 전까지 방향성 해석을 보류한다.

---

## 2. 당일 시장 요약

**⚠️ 당일 종가 브리핑(KR Close Briefing) 미수신**

오늘 일자로 기록된 `KR CLOSE BRIEFING` 또는 `KR MARKET SNAPSHOT` 소스가 없다. 당일 KOSPI·KOSDAQ 등락, 섹터별 강약, 외국인·기관 수급 흐름을 정확히 전달할 수 없는 상황이다.

시장 성격(광폭 랠리·섹터 로테이션·위험 선호·위험 회피 등)을 이 회차에서 판단하는 것은 데이터 없이 추론을 만들어 내는 것과 다르지 않다. 오늘 랩은 데이터 복원 후 갱신하거나, 내일 회차에서 전일 시장 성격을 간략히 되짚는 방식으로 보완할 예정이다.

---

## 3. 퀄리티 재평가 후보

**⚠️ 스크리너 소스 미수신**

당일 `KR META SCREENER`, `KR QUALITY COMPOUNDER`, `KR SMART MONEY QUALITY`, `KR CYCLE RERATING` 등 핵심 스크리너 데이터가 없다. 후보군 테이블과 3계층 분석(퀄리티·수급·재평가 촉매)을 이번 회차에서 제공할 수 없다.

스크리너 프레임워크는 아래 4개 계층으로 작동한다.

1. **KR Quality Compounder** — 지속 가능한 이익 구조를 가진 기업을 1차로 거른다
2. **KR Smart Money Quality** — 기관·외국인 수급이 실제로 들어오는지 확인한다
3. **KR Cycle Rerating** — 실적 레버리지가 재평가되는 시점의 기업을 포착한다
4. **KR Smart Money Earnings / KR PEAD** — 실적 개선 신호와 어닝 서프라이즈 이후 지속 상승(Post-Earnings Announcement Drift)을 더한다

이 4개 층 중 2개 이상 교차되는 종목이 주요 블로그 후보이며, 3개 이상 교차되면 리드 후보로 올린다. 오늘은 교차 분석을 실행할 원천 데이터가 없으므로 후보 추천을 보류한다.

---

**다음 업데이트 조건**

- `kr_screener`, `us_screener` 갱신 완료
- `kr_derivative:10d` 스냅샷 복원
- 매크로 레짐 재산출 → 당일 또는 익일 회차에 반영