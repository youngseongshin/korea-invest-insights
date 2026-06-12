---
title: "테마 ETF 리밸런싱 수급: 반도체 소부장에는 재배분 매수, 대장주에는 비중 상한 압력"
date: 2026-06-12T17:40:00+09:00
description: "Thesis OS의 KR Theme ETF Rebalance Flow v1 첫 실행 결과를 바탕으로 한국 테마 ETF 정기변경·비중 상한 재조정 수급을 점검한다. 6월 12일 기준 리노공업, 이오테크닉스, 솔브레인, DB하이텍, 한미반도체 등 반도체 소부장 재배분 매수 후보가 강했고, SK하이닉스·삼성전기·LS ELECTRIC 등은 cap trim 압력 후보로 잡혔다."
categories: ["Korean-Equities", "Market-Flow", "ETF-Flow"]
tags:
  - "ETF 리밸런싱"
  - "테마 ETF"
  - "수급 분석"
  - "반도체 소부장"
  - "SK하이닉스"
  - "삼성전기"
  - "한미반도체"
  - "리노공업"
  - "이오테크닉스"
  - "원익IPS"
  - "LS ELECTRIC"
series: ["korea-rerating-2026", "korea-market-flow"]
slug: "kr-theme-etf-rebalance-flow-semicap-cap-trim-2026-06-12"
valley_cashtags:
  - 리노공업
  - 이오테크닉스
  - 솔브레인
  - DB하이텍
  - 한미반도체
  - ISC
  - 원익IPS
  - HPSP
  - SK하이닉스
  - 삼성전자
  - 삼성전기
  - LS ELECTRIC
draft: false
---

> 연결 맥락  
> 이 글은 [외국인은 돌아왔나](/ko/post/foreign-return-after-24-day-kospi-selling-memory-rebalance-2026-06-12/), [Real Money 수급 프레임워크](/ko/post/real-money-flow-framework-korea-institution-quality-2026-06-03/), [유동성은 많은데 시장 폭은 무너졌다](/ko/post/korea-market-liquidity-foreign-reallocation-adr-narrow-leadership-2026-06-03/), [한국 ADR 67과 좁은 주도주 장세](/ko/post/korea-adr-breadth-narrow-leadership-kospi-kosdaq-2026-05-27/), [삼성물산 삼성전자 proxy / NAV gap trade](/ko/post/samsung-ct-samsung-electronics-proxy-nav-gap-trade-2026-06-01/), [젠슨 황의 HBM4 3사 검증 통과](/ko/post/jensen-huang-hbm4-three-vendors-qualified-market-missed-2026-06-05/)의 후속 수급 분석이다. 관련 허브는 [한국 데일리 마켓 허브](/ko/page/korea-daily-market-hub/)와 [AI HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/)다.

## TL;DR

- Thesis OS에 새로 붙인 **KR Theme ETF Rebalance Flow v1**은 한국 테마 ETF의 정기변경·비중 상한 재조정에서 나올 수 있는 기계적 수급을 추적하는 보조 신호다.
- 2026년 6월 12일 첫 실행 결과는 ETF **31개 스캔**, 유효 ETF **30개**, 구성종목 row **291개**, 후보 **69개**였다. 재배분 매수 후보 **60개**, 비중 상한 축소 매도 후보 **9개**가 잡혔다.
- 가장 강한 신호는 원전/SMR보다 **반도체 소부장 ETF 내부 재배분**이었다. 리노공업, 이오테크닉스, 솔브레인, DB하이텍, 한미반도체, ISC, 원익IPS가 상위권에 잡혔다.
- 반대로 SK하이닉스, 삼성전기, LS ELECTRIC, 두산에너빌리티 등은 일부 테마 ETF에서 **비중 상한 축소 압력** 후보로 포착됐다.
- 결론은 **매수 지시가 아니라 이벤트 체크리스트**다. 공식 PCF/PDF, 기초지수 방법론, 실제 cap rule, 종가·동시호가 거래대금, T+1/T+5 성과가 확인되어야 매매 신호로 승격할 수 있다.

<div class="thesis-callout">
  <div class="thesis-callout__label">Core Point</div>
  <div class="thesis-callout__body">
    이번 신호의 핵심은 “좋은 종목을 찾았다”가 아니라 <strong>테마 ETF가 너무 오른 대장주를 줄이고 같은 테마 안의 2선으로 비중을 재배분할 수 있는 구간</strong>을 찾았다는 점이다. 6월 12일 기준 가장 선명한 곳은 반도체 소부장이다.
  </div>
</div>

## 1. 이 모니터가 찾는 것

새로 붙인 `KR Theme ETF Rebalance Flow v1`은 테마 ETF의 구성종목 비중을 기준으로 **비중 상한에 걸린 종목과, 그 초과분을 받을 수 있는 종목**을 계산한다.

기본 산식은 단순하다.

```text
ETF별 예상 flow = ETF NAV × target weight delta
종목별 예상 flow = 여러 ETF에서 나온 예상 flow 합산
수급 강도 = 예상 flow / 20일 평균 거래대금
```

모니터는 Naver mobile ETF surface의 `constituentList`와 `totalNav`를 사용한다. 각 ETF에서 현재 구성비가 assumed cap을 넘는 종목은 cap까지 낮춘다고 가정하고, 초과분은 cap 미만 구성종목에 현재 비중 비례로 재배분한다고 본다.

중요한 점은 이것이 **공식 PCF 기반 확정 수급이 아니라 cap-redistribution proxy**라는 점이다. 실제 매매 신호로 쓰려면 운용사 공식 PDF/PCF, 기초지수 방법론, 실제 cap rule, 동시호가 체결 데이터를 확인해야 한다.

| 구분 | 내용 |
|---|---|
| 작업명 | KR Theme ETF Rebalance Flow v1 |
| 기준일 | 2026-06-12 |
| 스캔 ETF | 31개 |
| 유효 ETF | 30개 |
| 구성종목 row | 291개 |
| 전체 후보 | 69개 |
| 재배분 매수 후보 | 60개 |
| 비중 상한 축소 후보 | 9개 |
| 신뢰도 | medium-low |
| 원자료 | Thesis OS local DB, Naver ETF surface |

## 2. 가장 강한 신호: 반도체 소부장으로 재배분

6월 12일 기준 Top Redistribution Buy Pressure는 반도체 소부장 쪽에 집중됐다.

| 순위 | 종목 | 신호 | 예상 flow | Flow/ADV20 | 당일 등락 | 주요 ETF |
|---:|---|---|---:|---:|---:|---|
| 1 | 리노공업 | 재배분 매수 | 2,704.3억 | +2.68x | +4.7% | TIGER 반도체TOP10, KODEX AI반도체TOP2플러스 |
| 2 | 이오테크닉스 | 재배분 매수 | 1,978.0억 | +2.49x | +21.4% | TIGER 반도체TOP10 |
| 3 | 솔브레인 | 재배분 매수 | 694.2억 | +2.44x | +24.4% | TIGER 반도체TOP10 |
| 4 | DB하이텍 | 재배분 매수 | 2,643.2억 | +2.02x | +12.3% | TIGER 반도체TOP10, KODEX AI반도체TOP2플러스 |
| 5 | 한미반도체 | 재배분 매수 | 7,210.0억 | +1.81x | +24.1% | TIGER 반도체TOP10, KODEX AI반도체TOP2플러스, ACE AI반도체TOP3+ |
| 6 | ISC | 재배분 매수 | 920.4억 | +1.76x | +20.7% | TIGER 반도체TOP10, SOL AI반도체TOP2플러스 |
| 7 | 원익IPS | 재배분 매수 | 2,111.1억 | +1.63x | +30.0% | TIGER 반도체TOP10 |
| 8 | HPSP | 재배분 매수 | 1,437.4억 | +0.66x | +30.0% | TIGER 반도체TOP10, KODEX AI반도체TOP2플러스 |

이 표에서 중요한 것은 한미반도체의 절대 flow가 가장 크다는 점만이 아니다. 더 중요한 것은 **리노공업, 이오테크닉스, 솔브레인, ISC, 원익IPS처럼 20일 평균 거래대금 대비 수급 충격이 큰 종목**이 여럿 포착됐다는 점이다.

테마 ETF 리밸런싱은 대형주보다 중형 소부장에 더 민감하게 작동할 수 있다. SK하이닉스나 삼성전자는 예상 flow가 커도 20일 거래대금이 압도적으로 크기 때문에 가격 충격은 제한될 수 있다. 반대로 리노공업·이오테크닉스·솔브레인처럼 유동성 대비 flow가 2배 이상으로 잡히는 종목은 단기 가격 반응이 더 클 수 있다.

## 3. 대장주는 반대로 비중 상한 축소 압력을 받을 수 있다

같은 반도체 테마 안에서도 대장주는 다른 방향의 신호가 나온다. 비중이 cap을 넘었거나 상단에 가까워지면 ETF는 해당 종목 비중을 줄이고 다른 구성종목으로 초과분을 돌리는 구조가 될 수 있다.

| 순위 | 종목 | 신호 | 예상 flow | Flow/ADV20 | 당일 등락 | 주요 ETF |
|---:|---|---|---:|---:|---:|---|
| 1 | SK하이닉스 | 비중 상한 축소 | -1.76조 | -0.15x | +2.3% | TIGER 반도체TOP10, ACE AI반도체TOP3+ |
| 2 | 삼성전자 | 비중 상한 축소 | -493.5억 | -0.00x | +7.9% | TIGER 반도체TOP10, KODEX AI반도체TOP2플러스 |
| 3 | 삼성전기 | 비중 상한 축소 | -5,149.1억 | -0.21x | -5.0% | KODEX AI반도체TOP2플러스, SOL AI반도체TOP2플러스 |
| 4 | LS ELECTRIC | 비중 상한 축소 | -469.7억 | -0.15x | -3.0% | KODEX AI전력핵심설비, TIGER 코리아AI전력기기TOP3플러스 |
| 5 | HD현대중공업 | 비중 상한 축소 | -218.3억 | -0.06x | +0.6% | SOL 조선TOP3플러스, TIGER 조선TOP10 |
| 6 | 한화오션 | 비중 상한 축소 | -77.6억 | -0.04x | +7.8% | SOL 조선TOP3플러스 |
| 7 | 두산에너빌리티 | 비중 상한 축소 | -264.7억 | -0.07x | +5.1% | TIGER 코리아원자력 |

이 숫자를 곧바로 “매도”로 읽으면 안 된다. 예를 들어 SK하이닉스의 -1.76조 proxy는 절대금액으로 크지만, Flow/ADV20은 -0.15x에 불과하다. 삼성전자는 -493.5억원으로 잡혀도 20일 평균 거래대금 대비 영향은 사실상 0에 가깝다.

반면 삼성전기와 LS ELECTRIC은 다르다. 두 종목은 이미 AI 인프라와 전력기기 테마의 핵심 대장으로 급등했고, ETF 내부 비중 상한 압력이 일부 가격에 부담을 줄 수 있다. 이것은 thesis 훼손이 아니라 **기계적 수급 부담**이다.

## 4. 원전/SMR은 Priority Watch지만, 6월 12일 주도 신호는 아니었다

사용자가 처음 요청한 케이스는 원전/SMR이었다. 모니터에서도 원전 관련 종목은 Priority Watch에 잡혔다.

| 종목 | 신호 | 예상 flow | Flow/ADV20 | 당일 등락 | 주요 ETF |
|---|---|---:|---:|---:|---|
| 한전기술 | 재배분 매수 | 28.5억 | +0.13x | +30.0% | TIGER 코리아원자력 |
| 두산에너빌리티 | 비중 상한 축소 | -264.7억 | -0.07x | +5.1% | TIGER 코리아원자력 |
| 현대건설 | 재배분 매수 | 87.5억 | +0.06x | +28.4% | TIGER 코리아원자력 |
| 비에이치아이 | 재배분 매수 | 15.7억 | +0.06x | +30.0% | TIGER 코리아원자력 |
| 우리기술 | 재배분 매수 | 29.1억 | +0.04x | +30.0% | TIGER 코리아원자력 |

다만 6월 12일 데이터만 놓고 보면 원전/SMR은 “관찰 케이스”이고, 실제 강한 수급 충격은 반도체 소부장 쪽이었다. 원전주는 가격 상한가가 여럿 나왔지만, ETF 재배분 proxy의 절대 규모와 유동성 대비 강도는 반도체 소부장이 더 컸다.

## 5. 밸류업 ETF는 완만한 재배분 신호

밸류업 ETF에서는 SK스퀘어, 신한지주, 하나금융지주, KB금융, 기아, 현대차, 현대모비스 등이 재배분 매수 후보로 잡혔다.

| 종목 | 예상 flow | Flow/ADV20 | 주요 ETF |
|---|---:|---:|---|
| SK스퀘어 | 725.6억 | +0.07x | RISE 코리아밸류업, KODEX 코리아밸류업 |
| 신한지주 | 197.1억 | +0.13x | RISE 코리아밸류업, KODEX 코리아밸류업 |
| 하나금융지주 | 141.0억 | +0.12x | RISE 코리아밸류업, KODEX 코리아밸류업 |
| KB금융 | 227.8억 | +0.10x | RISE 코리아밸류업, KODEX 코리아밸류업 |
| 기아 | 188.2억 | +0.07x | RISE 코리아밸류업, KODEX 코리아밸류업 |
| 현대차 | 402.4억 | +0.03x | RISE 코리아밸류업, KODEX 코리아밸류업 |

이 축은 반도체 소부장처럼 단기 가격 충격이 크지는 않다. 대신 밸류업 ETF의 규모가 커지고, 주주환원 대형주 수요가 이어질 경우 **저강도 지속 매수**로 해석할 수 있다.

## 6. 실전 매매 프레임: 바로 사는 것이 아니라 4단계 확인

이 신호는 바로 매수 버튼을 누르는 신호가 아니다. 정확한 사용법은 “후보군을 좁히는 1차 필터”다.

### 6.1 Buy Pressure 후보의 승격 조건

재배분 매수 후보는 아래 네 가지 중 최소 두 가지가 확인될 때 매매 후보로 승격한다.

| 확인 항목 | 의미 |
|---|---|
| 공식 PDF/PCF에서 구성비 변화 확인 | Naver surface proxy가 실제 운용사 데이터와 맞는지 검증 |
| 종가·동시호가 거래대금 증가 | 실제 ETF/AP 리밸런싱성 체결 확인 |
| T+1 또는 T+3 상대강도 유지 | 단순 하루짜리 계산 신호가 아닌지 확인 |
| 외국인·기관 또는 프로그램 동반 매수 | ETF 재배분과 실제 수급이 같은 방향인지 확인 |

### 6.2 Cap Trim 후보의 해석

비중 상한 축소 후보는 무조건 매도 후보가 아니다. 대형주는 cap trim 압력보다 실적·외국인·기관 수급이 훨씬 클 수 있다. 따라서 cap trim 후보는 다음처럼 본다.

| 유형 | 해석 |
|---|---|
| Flow/ADV20이 작고 펀더멘털 강함 | 보유 유지. 기계적 압력은 소음일 수 있음 |
| Flow/ADV20이 크고 주가 과열 | 단기 추격 금지 또는 일부 trim 검토 |
| cap trim 후에도 가격이 버팀 | 강한 실수요 확인 |
| cap trim과 외국인·기관 매도 동시 발생 | 수급 부담 확대 |

## 7. 종목별 1차 판단

| 그룹 | 종목 | 1차 판단 |
|---|---|---|
| 재배분 매수 강도 상위 | 리노공업, 이오테크닉스, 솔브레인 | 유동성 대비 flow가 강하다. 공식 구성비와 T+1/T+3 상대강도 확인 필요 |
| 절대 flow 대형 | 한미반도체, DB하이텍, 원익IPS | 반도체 장비·후공정 베타와 ETF 재배분이 겹친다. 단, 이미 당일 급등 후라 추격보다 눌림 확인 |
| 중간 강도 | ISC, HPSP, 피에스케이 | 반도체 장비/소켓/검사 축. 프로그램·기관 동행 여부 확인 |
| cap trim watch | SK하이닉스, 삼성전기, LS ELECTRIC | thesis 훼손은 아니지만 단기 기계적 매물 가능성. 가격이 버티면 오히려 강한 실수요 신호 |
| 원전/SMR watch | 한전기술, 현대건설, 비에이치아이, 우리기술 | 이벤트성 가격 반응은 강하지만 ETF proxy 강도는 반도체보다 낮다 |
| 밸류업 완만한 수급 | SK스퀘어, 신한지주, KB금융, 하나금융, 기아 | 단기 급등 신호보다 구조적 저강도 재배분 후보 |

## 8. 실패 조건

이 전략이 실패하는 조건은 명확하다.

1. 운용사 공식 PDF/PCF에서 실제 구성비 변화가 Naver surface proxy와 다르게 확인된다.
2. 예상 buy pressure 후보가 T+1/T+3에서 상대강도를 유지하지 못한다.
3. 종가·동시호가 거래대금 증가가 없고, 장중 개인 추격만 확인된다.
4. cap trim 후보가 실제로는 설정·환매 또는 신규 자금 유입으로 상쇄된다.
5. ETF 전체 자금이 유입되는 것이 아니라 테마 ETF에서 환매가 발생한다.

특히 마지막이 중요하다. 리밸런싱은 “ETF 내부 비중 조정”이고, ETF 자체로 돈이 들어오는 “설정 증가”와 다르다. 테마 ETF 전체에서 환매가 나오면 재배분 매수 후보도 기대보다 약해질 수 있다.

## 9. 최종 판단

6월 12일 첫 실행 결과만 보면, 테마 ETF 리밸런싱 수급의 핵심은 **원전/SMR보다 반도체 소부장**이었다.

대장주가 급등해 ETF 내부 비중 상한에 닿으면, 초과분은 같은 테마 안의 2선으로 재배분될 수 있다. 이 구조에서 리노공업, 이오테크닉스, 솔브레인, DB하이텍, 한미반도체, ISC, 원익IPS가 가장 먼저 포착됐다.

다만 이건 **medium-low confidence의 보조 신호**다. 공식 PCF와 실제 체결 확인 전에는 “매수 신호”가 아니라 “확인해야 할 수급 후보”다.

실전 액션은 다음과 같다.

| 단계 | 액션 |
|---|---|
| 1 | Top buy pressure 후보의 공식 ETF PDF/PCF 구성비 확인 |
| 2 | T+1/T+3 가격 상대강도와 종가 거래대금 확인 |
| 3 | 프로그램·외국인·기관 수급 방향 확인 |
| 4 | 강한 후보만 watchlist 또는 소액 event trade로 승격 |
| 5 | cap trim 후보는 추격보다 가격 방어력을 확인 |

한 줄로 정리하면 이렇다.

> 이번 모니터는 “ETF가 사줄 종목”을 확정한 것이 아니라, **대장주 쏠림 이후 테마 ETF 내부에서 어디로 물량이 재배분될 수 있는지**를 처음으로 수치화했다. 6월 12일 기준 답은 반도체 소부장이다.

## Evidence Ledger

| 항목 | 출처 | 내용 |
|---|---|---|
| 모니터 구현 | Thesis OS / Alpha | `KR Theme ETF Rebalance Flow v1`, 평일 19:30 KST launchd 등록 |
| 로컬 리포트 | Vault `2026-06-12_theme_etf_rebalance_flow.md` | ETF 31개 스캔, 유효 30개, 후보 69개 |
| External Signal Judge 입력 | Vault `2026-06-12_theme_etf_rebalance_flow_candidates.md` | 후보별 score, flow, intensity, confidence |
| 데이터 소스 | Naver ETF surface + local DB | `constituentList`, `totalNav`, `prices_daily` ADV20 |
| 검증 상태 | System log | `py_compile`, `unittest` 11개, `plutil -lint`, launchd 로드 확인 |

## Fact / Inference / Blocked

### Fact

- 2026년 6월 12일 첫 실행에서 ETF 31개를 스캔했고, 30개 ETF가 유효했다.
- 구성종목 row는 291개, 전체 후보는 69개였다.
- 재배분 매수 후보는 60개, 비중 상한 축소 후보는 9개였다.
- 리노공업, 이오테크닉스, 솔브레인, DB하이텍, 한미반도체, ISC, 원익IPS가 Top Redistribution Buy Pressure 상위에 잡혔다.
- SK하이닉스, 삼성전자, 삼성전기, LS ELECTRIC 등은 cap trim pressure watch로 잡혔다.

### Inference

- 6월 12일 기준 테마 ETF 리밸런싱 수급은 원전/SMR보다 반도체 소부장 쪽이 더 강했다.
- 대장주 쏠림 이후 ETF 내부 재배분이 2선 소부장 가격 반응을 키울 수 있다.
- cap trim 후보가 가격을 버티면, 오히려 ETF 매물보다 강한 실수요가 존재한다는 신호가 될 수 있다.

### Blocked

- 운용사 공식 PDF/PCF 원문과 실제 기초지수 방법론은 전수 검증하지 않았다.
- Naver ETF surface는 공개 proxy이며, 실제 운용사 구성비와 차이가 있을 수 있다.
- 종가·동시호가 체결과 AP 설정·환매 데이터는 아직 반영하지 않았다.
- 따라서 이 글은 매매 지시가 아니라 이벤트 수급 후보군 정리다.
