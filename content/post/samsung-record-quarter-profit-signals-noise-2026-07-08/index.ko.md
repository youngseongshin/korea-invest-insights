---
title: "세계 최대 규모 분기 영업이익을 기록한 삼성전자, 오늘 쏟아진 신호와 소음"
slug: samsung-record-quarter-profit-signals-noise-2026-07-08
date: 2026-07-08T22:35:00+09:00
description: "삼성전자 2Q26 잠정 영업이익 89.4조원, DRAM·NAND 가격 급등, 하이퍼스케일러 CapEx, AI 서버 공급망 신호와 외국인 매도·금리·ASML·TSMC 이벤트 리스크를 분리해 본다. 결론은 투자 논거 강화, 단기 타이밍 훼손, 강한 보유와 추가매수 동결이다."
categories: ["Exclusive Analysis", "한국 반도체", "Earnings"]
tags:
  - "삼성전자"
  - "HBM"
  - "DRAM"
  - "NAND"
  - "eSSD"
  - "AI 메모리"
  - "하이퍼스케일러"
  - "AI CapEx"
  - "ASML"
  - "TSMC"
  - "메모리 가격"
  - "외국인 수급"
  - "금리"
series: ["exclusive-analysis", "hbm", "macro-gates-2026"]
valley_cashtags:
  - 삼성전자
  - SK하이닉스
  - Micron
  - ASML
  - TSMC
  - NVIDIA
draft: false
---

> 연결 맥락
> 이 글은 [삼성전자 2Q26 프리뷰](/ko/post/samsung-2q26-preview-micron-surprise-erased-core-op-hbm-2026-06-29/), [마이크론 FY3Q26 실적 분석](/ko/post/micron-fy3q26-ai-memory-sca-fcf-hold-2026-06-25/), [NVIDIA 변곡점으로 본 전닉/HBM 사이클](/ko/post/nvidia-earnings-elasticity-hbm-cycle-samsung-hynix-2026-06-28/), [7월 말 빅테크 어닝콜과 메모리 테시스](/ko/post/big-tech-july-earnings-call-memory-thesis-scenarios-2026-07-07/), [빅테크 자금조달 릴레이와 메모리 병목](/ko/post/hyperscaler-financing-race-ai-capex-memory-bottleneck-2026-07-07/), [삼성전자 실적 급락과 엔비디아 유사 분기](/ko/post/samsung-earnings-selloff-nvidia-q4fy26-rebound-trigger-2026-07-08/)의 후속 단독 분석이다. 관련 허브는 [Exclusive Analysis 허브](/ko/page/exclusive-analysis-hub/)와 [AI HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/)다.

## TL;DR

삼성전자는 2026년 2분기 잠정 매출 171조원, 영업이익 89.4조원을 제시했다. 삼성전자 공식 뉴스룸 기준 전분기 영업이익 57.23조원, 전년 동기 4.68조원과 비교하면 매우 큰 숫자다. 메모리 가격, AI 서버 수요, 하이퍼스케일러 투자, HBM4 램프업을 함께 보면 삼성전자 투자 논거의 질은 오히려 강해졌다.

그런데 주가는 정반대로 움직였다. 로컬 DB 기준 삼성전자는 7월 7일 296,000원, 7월 8일 277,500원으로 마감했다. 7월 7일 외국인은 약 1.82조원, 7월 8일에는 약 8,741억원을 순매도했다. 개인은 각각 약 2.32조원, 5,847억원을 순매수했다. 좋은 실적이 나왔지만 외국인과 프로그램성 수급은 이익 레벨보다 peak-out, 금리, 환율, 포지션 과밀을 먼저 본 셈이다.

이 글의 결론은 다음이다.

| 항목 | 판단 |
|---|---|
| 삼성전자 투자 논거 | 강화. DRAM·NAND 가격, AI 서버, 하이퍼스케일러 CapEx가 모두 우호적이다. |
| 단기 타이밍 | 훼손. 좋은 실적에도 이틀 연속 매도 압력이 나왔다. |
| 수급 | 위험. 외국인 매도와 개인 흡수가 충돌하고, 한국 시장 폭도 약하다. |
| 매도 판단 | 아니다. 현재 데이터는 thesis 훼손보다 기대 소화와 수급 압박에 가깝다. |
| 추가매수 판단 | 아직 아니다. ASML, TSMC, 삼성전자 IR, 외국인 수급, 환율·금리를 확인해야 한다. |
| 행동 | 강한 보유, 추가매수 동결, 다음 관문 확인 후 재판단. |

한 줄로 정리하면, 오늘 나온 정보는 “삼성전자가 나빠졌다”가 아니라 “좋은 숫자를 시장이 이미 너무 많이 들고 있었고, 이제는 다음 숫자와 수급의 질을 요구한다”에 가깝다.

## 1. 왜 신호와 소음을 나눠야 하나

오늘 데이터는 한 방향으로만 읽히지 않는다. 숫자는 좋다. 하지만 주가와 수급은 나쁘다. 메모리 가격 코멘트는 강하다. 하지만 spot 거래는 일부 품목에서 숨을 고른다. 하이퍼스케일러 CapEx는 계속 커진다. 하지만 미국 장기금리도 높다.

이런 날에는 한쪽만 보면 틀린다. “세계 최대 규모급 분기 영업이익이니 무조건 사야 한다”도 성급하고, “좋은 실적에도 빠졌으니 사이클이 끝났다”도 성급하다.

따라서 이 글은 데이터를 네 층으로 나눠 본다.

| 층 | 내용 | 투자 판단에서의 역할 |
|---|---|---|
| 공식 실적 | 삼성전자 2Q26 잠정 매출·영업이익 | 이익 레벨 확인 |
| 산업 신호 | DRAM·NAND 가격, AI 서버, 하이퍼스케일러 CapEx | thesis의 질 확인 |
| 시장 소음 | spot 거래 부진, Morgan Stanley peak 논리, ASML·TSMC high bar | 단기 timing 확인 |
| 수급·매크로 | 외국인 매도, 환율, 금리, 한국 시장 breadth | 포지션 크기 결정 |

핵심은 이익 방향과 주가 방향을 분리하는 것이다. 삼성전자의 본업 이익 방향은 좋아졌다. 그러나 단기 주가의 주인은 이익이 아니라 수급과 할인율이었다.

## 2. 공식 확인값: 매출 171조원, 영업이익 89.4조원

[Fact] 삼성전자는 2026년 7월 7일 공식 뉴스룸을 통해 2분기 잠정실적을 발표했다. 연결 매출은 약 171조원, 영업이익은 약 89.4조원이다. 한국 공시 규정상 회사는 범위가 아니라 중간값을 제시했고, 실제 추정 범위는 매출 170조~172조원, 영업이익 89.3조~89.5조원이라고 설명했다. 출처: [Samsung Electronics 공식 뉴스룸](https://news.samsung.com/global/samsung-electronics-announces-earnings-guidance-for-second-quarter-2026)

| 항목 | 2Q26 잠정치 | 1Q26 | 2Q25 | 전분기 대비 | 전년 동기 대비 |
|---|---:|---:|---:|---:|---:|
| 매출 | 171.0조원 | 133.87조원 | 74.57조원 | +27.7% | +129.3% |
| 영업이익 | 89.4조원 | 57.23조원 | 4.68조원 | +56.2% | +1,810.3% |

이 숫자는 단일 분기 영업이익 기준으로 매우 드문 규모다. “세계 최대 규모”라는 표현은 비교 대상과 회계 기준에 따라 따져볼 여지가 있지만, 적어도 글로벌 mega-cap의 정상 분기 이익과 비교해도 압도적으로 큰 숫자라는 점은 분명하다.

중요한 것은 영업이익 89.4조원 자체가 아니라 그 안의 질이다. 첨부 리서치에서 제시한 해석은 다음이다.

| 항목 | 해석 |
|---|---|
| reported 영업이익 | 89.4조원 |
| DS 성과급 등 일회성 충당금 조정 | 본업 이익을 더 높게 봐야 한다는 논리 |
| Core OP 추정 | 충당금 제외 시 100조원 이상 가능성 |
| DRAM ASP | 전분기 대비 +47% |
| NAND ASP | 전분기 대비 +66% |
| HBM4 | 램프업 기대 유지 |

[Inference] reported OP 89.4조원만 봐도 강하지만, DRAM과 NAND 가격이 동시에 크게 올랐고 충당금 효과가 있었다면 본업 체력은 reported 숫자보다 더 강할 수 있다. 이 지점이 삼성전자 thesis의 가장 중요한 신호다.

## 3. 주가와 수급: 좋은 숫자 뒤에 외국인이 팔았다

좋은 실적에도 주가는 빠졌다. 로컬 DB 기준 가격과 수급은 다음과 같다.

| 날짜 | 종가 | 일간 등락 | 외국인 순매수 추정 | 기관 순매수 추정 | 개인 순매수 추정 |
|---|---:|---:|---:|---:|---:|
| 2026-07-03 | 309,500원 |  | -3,872억원 | +1조3,063억원 | -9,184억원 |
| 2026-07-06 | 318,000원 | +2.75% | -6,409억원 | +58억원 | +5,964억원 |
| 2026-07-07 | 296,000원 | -6.92% | -1조8,207억원 | -5,475억원 | +2조3,232억원 |
| 2026-07-08 | 277,500원 | -6.25% | -8,741억원 | +2,827억원 | +5,847억원 |

출처는 로컬 Kiwoom 기반 `prices_daily`, `investor_flow_daily` 테이블이다. 7월 8일 외국인 보유율은 46.58%로 기록됐다.

이 표의 메시지는 분명하다. 시장은 삼성전자 이익이 약해졌다고 본 것이 아니라, 이미 오른 주식에서 외국인이 위험을 줄이고 개인이 받아낸 구조였다. 7월 7일에는 외국인과 기관이 함께 팔고 개인이 크게 샀다. 7월 8일에는 기관이 일부 받았지만 외국인 매도는 계속됐다.

따라서 오늘의 판단은 “실적은 좋지만 수급이 나쁘다”다. 매도 근거가 아니라 추가매수 동결 근거다.

## 4. 삼성전자 thesis의 네 축

삼성전자 투자 논거는 네 개 축으로 정리할 수 있다.

| 축 | 내용 | 현재 판단 |
|---|---|---|
| AI 서버 DRAM·HBM | AI 서버와 GPU·ASIC 시스템의 고대역폭·고용량 메모리 수요 | 강화 |
| eSSD·NAND 믹스 | AI 서버 스토리지와 enterprise SSD 수요 | 강화 |
| 하이퍼스케일러 CapEx | 클라우드와 AI 데이터센터 투자 장기화 | 강화 |
| 파운드리 턴어라운드 | 선단 로직·패키징·고객 회복 옵션 | 아직 옵션 |

이 중 핵심은 1~3번이다. 파운드리는 valuation upside option이다. 지금 주가가 버티려면 파운드리가 바로 좋아질 필요는 없다. 메모리, eSSD, 하이퍼스케일러 투자만으로도 이익 체력은 설명된다. 하지만 추가 리레이팅에는 파운드리 적자 축소와 HBM4·HBM4E 고객 확인이 필요하다.

## 5. 신호 1: legacy DRAM과 NAND 가격은 생각보다 더 강하다

첨부 리서치에서 가장 중요한 강세 신호는 메리츠증권 김선우 위원 코멘트로 정리된 메모리 가격 흐름이다. 원자료 전문을 직접 대조한 것은 아니므로 이 글에서는 “시장 코멘트 기반 해석”으로 분류한다. 그래도 수치와 방향은 삼성전자 투자 논거를 해석하는 데 중요하다.

핵심은 7월부터 하반기 계절 수요가 들어오고, B2B 서버 수요가 공급을 흡수하는 가운데 B2C 스마트폰·PC 고객도 물량 확보 압력을 받기 시작했다는 점이다.

### Legacy DRAM

| 항목 | 수치와 내용 |
|---|---|
| Nanya 3Q26 DRAM 가격 제안 | DDR4·LPDDR4 +50~90% QoQ |
| Consumer DRAM 가격 | $3/Gb 이상, 상승 가속 |
| 공급 확장 | 2027년 전까지 의미 있는 공급 확대가 어렵다는 판단 |
| 원인 | 2023년 손실 이후 2023~2025년 투자 감소, cleanroom 부족 |

### Legacy NAND

| 항목 | 수치와 내용 |
|---|---|
| Windbond·MXIC SLC NAND 제안 | 3Q26 +70~100% QoQ |
| 가격대 | $1.9~2.0/Gb |
| 수요 변화 | MLC NAND 부족으로 SLC NAND 주문 증가 |
| 해석 | 고성능 AI NAND만이 아니라 legacy NAND까지 가격 압력이 확산 |

### 공급 구조

| 항목 | 내용 |
|---|---|
| 2027년 DRAM 총 공급 성장률 | 20~25% 예상 |
| 내년 서버 수요 성장률 | 50~70% 예상 |
| 병목 원인 | high-end memory 집중으로 low-end·legacy shortage 발생 |

[Inference] 이 데이터가 맞다면 삼성전자 bull case는 SK하이닉스식 HBM 순수 노출보다 넓다. 삼성전자는 HBM에서 뒤처졌다는 할인 요인이 있지만, 일반 DRAM, server DRAM, eSSD, NAND, legacy 제품 가격 상승까지 함께 받는다. 즉 “HBM만 봐서 삼성전자를 깎아내리는 프레임”이 약해진다.

## 6. 신호 2: AI CapEx는 아직 꺾였다고 보기 어렵다

하이퍼스케일러 투자도 삼성전자 thesis를 지지한다. Goldman Sachs 차트로 공유된 숫자에 따르면 hyperscaler CapEx는 다음처럼 커진다.

| 연도 | Hyperscaler CapEx |
|---|---:|
| 2024 | 2,270억달러 |
| 2025 | 4,060억달러 |
| 2026E | 7,400억달러 |
| 2027E | 9,960억달러 |

2027년 예상치는 2024년의 약 4.4배다. 이 숫자는 [빅테크 자금조달 릴레이](/ko/post/hyperscaler-financing-race-ai-capex-memory-bottleneck-2026-07-07/)에서 다룬 채권·증자 흐름과도 맞물린다. 아마존, 알파벳, 메타는 내부 현금흐름만으로 감당하기 어려운 수준의 AI 인프라 투자를 위해 회사채와 주식 발행까지 쓰고 있다.

삼성전자에 중요한 것은 “AI CapEx가 GPU에서 끝나지 않는다”는 점이다. AI 데이터센터 투자는 GPU만 사는 것이 아니다. 서버 DRAM, HBM, eSSD, NAND, 기판, 전력, 네트워크, 냉각까지 같이 늘어난다.

| AI CapEx 항목 | 삼성전자와의 연결 |
|---|---|
| GPU·ASIC 서버 | HBM, server DRAM |
| 데이터센터 저장장치 | eSSD, NAND |
| 고밀도 서버 확산 | 고용량 DDR5, LPDDR 계열, storage |
| 랙 단위 AI factory | 메모리 탑재량 증가 |
| 장기 투자 사이클 | 2026년 단기 실적보다 2027년 visibility 강화 |

[Inference] 하이퍼스케일러 CapEx가 2027년까지 커진다면 삼성전자 메모리 이익이 한 분기 peak에서 바로 꺾인다고 단정하기 어렵다. 문제는 수요가 없느냐가 아니라, 시장이 그 수요를 이미 얼마만큼 가격에 반영했느냐다.

## 7. 신호 3: AI 서버 공급망도 아직 깨지지 않았다

첨부 리서치에 포함된 대만 AI 서버 공급망 데이터도 중요하다.

| 기업 | 최신 신호 | 해석 |
|---|---|---|
| Wistron | 6월 매출 +10.9% MoM, +53.8% YoY | GB300 NVL72, B300 shipment 증가 |
| Wiwynn | 6월 매출 +32.5% MoM, +29.8% YoY | AMD Helios 진입, 3Q ASIC AI 서버 대량 출하 준비 |
| Unimicron | ABF·HDI substrate revenue record high | ABF 확장 CapEx 증가 언급 |

이 데이터는 “AI 서버 수요가 꺾였다”는 주장과 맞지 않는다. 서버 OEM, ODM, 기판 업체가 여전히 강한 출하와 매출을 보이면 메모리 수요도 쉽게 사라지기 어렵다.

물론 이 데이터만으로 삼성전자 실적을 바로 산출할 수는 없다. 하지만 방향은 명확하다. AI 서버 공급망은 아직 멈추지 않았다. 오히려 GPU, ASIC, 서버, 기판, 메모리, storage가 함께 움직이는 구조다.

## 8. 소음 1: TrendForce spot 데이터는 약하지만 붕괴는 아니다

반대 신호도 있다. TrendForce spot 시장 코멘트는 거래가 한산하고 구매자가 기다리는 분위기라고 정리됐다.

| 품목 | spot 변화 |
|---|---:|
| DDR5 16Gb | +0.50% |
| DDR5 eTT | 0.00% |
| DDR4 16Gb 3200 | +3.42% |
| DDR4 eTT | -1.51% |
| DDR4 8Gb 3200 | +2.88% |

이 표를 보고 “메모리 가격이 꺾였다”고 말하는 것은 과하다. 대부분은 상승 또는 보합이고, 일부 eTT 품목만 하락했다. 더 정확한 표현은 “거래는 한산하고, spot 시장은 가격 발견 중”이다.

중요한 구분은 spot과 contract다.

| 구분 | 의미 | 삼성전자 thesis와의 관련성 |
|---|---|---|
| Spot | 유통·모듈 시장의 단기 거래 가격 | 심리와 단기 재고를 빠르게 반영 |
| Contract | 대형 고객 장기 계약 가격 | 서버 DRAM, HBM, eSSD 이익에 더 중요 |

삼성전자 thesis의 핵심은 spot이 아니다. 핵심은 contract 가격, server DRAM, HBM, eSSD 주문, hyperscaler 수요다. 진짜 위험 신호는 spot 거래 부진 자체가 아니라 다음 네 가지가 함께 나오는 경우다.

1. Contract price cut
2. Server DRAM 주문 둔화
3. HBM·eSSD order slowdown
4. 주요 고객의 inventory correction 코멘트

현재는 이 네 가지가 모두 확인된 상태가 아니다. 그래서 TrendForce 데이터는 bear confirmation이 아니라 기대 소화와 가격 발견 신호로 보는 것이 맞다.

## 9. 소음 2: Morgan Stanley peak 논리는 일부만 맞다

Morgan Stanley류 peak thesis도 무시하면 안 된다. 핵심은 메모리 지표 개선 속도가 peak에 가까워지고, 재고 정상화와 가격 인상 속도 둔화가 나타날 수 있다는 것이다. AI trade 안에서는 반도체보다 Alphabet, Amazon 같은 AI cloud 쪽을 선호한다는 관점도 제시됐다.

이 주장은 일부 맞다. 특히 단기 주가에는 중요하다.

| Morgan Stanley식 경고 | 인정할 부분 |
|---|---|
| 개선 속도 peak 가능성 | 주가는 레벨보다 기울기에 민감하다. |
| 가격 인상 속도 둔화 | 3Q 이후 상승률이 낮아지면 멀티플 압박 가능 |
| 반도체 과밀 포지션 | 좋은 실적에도 sell-the-news가 가능 |
| AI cloud 선호 | 반도체보다 수요자 쪽으로 rotation 가능성 |

그러나 이것을 구조적 매도 논리로 확대하는 것은 약하다. 반대 데이터가 너무 많다.

| 반대 논리 | 근거 |
|---|---|
| AI 투자 확대 지속 | 2027년까지 hyperscaler CapEx 증가 전망 |
| 공급 부족 장기화 | cleanroom·고부가 제품 전환으로 legacy shortage 심화 |
| 서버 수요 성장 | 내년 server demand +50~70% 전망 |
| 국내 증권사 buy 유지 | KB 600,000원, 다올 585,000원, NH 530,000원, 하나·iM 480,000원 등 목표가 유지 또는 상향 |

[Inference] Morgan Stanley peak thesis는 “지금 추격하지 말라”는 경고로는 유효하다. 그러나 “삼성전자 thesis를 폐기하라”는 근거로는 부족하다.

## 10. 소음 3: ASML과 TSMC는 high bar 이벤트다

다음 관문은 ASML과 TSMC다. ASML 공식 financial calendar는 2026년 7월 15일 Q2 2026 financial results를 표시하고 있다. TSMC 공식 IR 페이지는 2026년 7월 16일 2Q26 earnings conference를 안내한다. 출처: [ASML financial calendar](https://www.asml.com/investors/financial-calendar), [TSMC 2Q26 quarterly results](https://investor.tsmc.com/english/quarterly-results/2026/q2)

문제는 좋은 실적이 나와도 주가가 오를지 알 수 없다는 점이다. 삼성전자 2Q26 잠정실적이 이미 그 예고편이다. high bar가 높으면 좋은 숫자도 부족해 보인다.

ASML과 TSMC에서 봐야 할 것은 다음이다.

| 이벤트 | 체크포인트 | 삼성전자와의 연결 |
|---|---|---|
| ASML 2Q26 | bookings, EUV·High-NA 수요, 중국 규제 코멘트 | 반도체 capex 기대와 장비 수요 확인 |
| TSMC 2Q26 | AI/HPC revenue, CoWoS·advanced packaging, CapEx 가이던스 | AI accelerator와 HBM 패키징 병목 확인 |
| 시장 반응 | SOXX, NVDA, MU, TSM, ASML 주가 반응 | 좋은 실적에 팔리는지, 안도하는지 확인 |

Mizuho 코멘트처럼 삼성전자의 좋은 잠정실적에도 주가가 빠진 것은 global IT momentum shift 가능성을 보여준다. 그래서 ASML과 TSMC는 “숫자 확인”이 아니라 “시장이 좋은 숫자를 어떻게 소화하는지”를 보는 이벤트다.

## 11. 소음 4: 금리와 환율은 멀티플을 누른다

삼성전자 thesis가 좋아도 할인율이 올라가면 주가는 눌릴 수 있다. 첨부 리서치 기준 금리 환경은 다음과 같다.

| 항목 | 수준 |
|---|---:|
| 미국 10년물 | 약 4.58% |
| 미국 30년물 | 약 5.07% |
| 일본 10년물 | 약 2.88% |
| 일본 40년물 | 약 4.01% |

이 숫자는 수요 thesis를 훼손하지는 않는다. 하지만 PER을 낮출 수 있다. 강한 이익에도 주가가 빠지는 전형적인 구간은 “EPS는 올라가지만 multiple이 더 빨리 내려가는 구간”이다.

환율도 마찬가지다. 원화 약세는 삼성전자 실적에는 우호적일 수 있다. 그러나 외국인 입장에서는 환손실, 환헤지 비용, 한국 비중 위험을 키운다. 7월 8일 외국인 보유율 46.58%와 연속 매도는 이 부분을 확인해야 한다는 신호다.

## 12. 소음 5: 외국인 outflow와 레버리지 배관

첨부 리서치에는 Bloomberg·텔레그램 기반으로 외국인 outflow와 레버리지 배관 관련 코멘트가 포함돼 있다. 여기서 제시된 수치, 예컨대 연초 이후 한국 시장 외국인 outflow -1,001.6억달러, 3월 외국인 증권 outflow -365.5억달러, USD/KRW 1,554원 등은 공식 통계와 집계 범위별 대조가 필요하다. 따라서 이 글에서는 방향성 신호로만 쓴다.

그럼에도 메시지는 중요하다.

| 관찰 | 해석 |
|---|---|
| 외국인이 한국을 줄였다 | 한국 회피라기보다 memory peak-out bet일 수 있다. |
| 국내 기관·개인이 반등을 흡수했다 | 외국인 주도 랠리라기보다 국내 유동성 흡수 장세다. |
| 단일종목 레버리지·short gamma 구조 | 하락 때 강제 매도와 헤지 플로우가 가격을 과장할 수 있다. |
| 환율 상승 | 외국인 추가매수의 장벽이다. |

[Inference] 단기 급락은 삼성전자 본업 붕괴보다 memory peak-out 베팅, 레버리지 포지션 청산, 외국인 위험 축소가 겹친 결과일 가능성이 높다. 그러나 이것이 구조적 위험이 아니라고 단정할 수도 없다. 외국인 현물 매도가 멈추는지 확인해야 한다.

## 13. 한국 시장 폭도 좋지 않다

삼성전자만의 문제가 아니다. 7월 8일 06:10 기준 로컬 KR integrated screener는 한국 시장을 NEUTRAL로 분류했다.

| 항목 | 수치 |
|---|---:|
| 50일선 위 종목 비중 | 15.6% |
| 200일선 위 종목 비중 | 21.5% |
| 통과 종목 | 17개 |
| 신규 통과 | 5개 |
| 이탈 | 7개 |
| Breakout | 0개 |

신규 통과 종목은 에이피알, 한섬, GS리테일, 하나금융지주, KT&G였다. 이탈 종목에는 티에스이, 와이지-원, 삼성전자우 등이 포함됐다.

Quality compounder 스크린은 13개가 통과했고, 상위에는 기가비스, SK하이닉스, 브이엠, 에이피알, 피에스케이가 있었다. Smart money + quality 조건은 에이피알, 씨젠, 한국콜마 3개만 통과했다.

이 데이터의 의미는 간단하다. 시장 폭이 약하다. 삼성전자 thesis가 좋아도 한국 시장 전체가 넓게 받아주는 장은 아니다. 이런 환경에서 추가매수는 이익 데이터만 보고 하면 안 된다. 수급과 시장 폭이 돌아오는지 함께 봐야 한다.

## 14. 그러면 무엇을 해야 하나

현재 결론은 “강한 보유, 추가매수 동결”이다.

| 행동 | 판단 |
|---|---|
| 보유 | 가능. thesis는 훼손되지 않았다. |
| 추가매수 | 아직 대기. 수급·ASML·TSMC·IR 확인 필요 |
| 매도 | 지금 데이터만으로는 아님. 이익 방향은 오히려 좋아졌다. |
| 단기 트레이딩 | 외국인 매도 둔화와 7월 15~16일 글로벌 반도체 반응 확인 후 |

추가매수 조건은 다음 네 가지다.

1. 외국인 삼성전자 현물 매도가 둔화되고, 프로그램성 매도 압력이 줄어든다.
2. ASML bookings와 TSMC AI/HPC·CoWoS·CapEx 코멘트가 AI 투자 둔화를 말하지 않는다.
3. 삼성전자 IR에서 DS core profit, DRAM·NAND contract price, HBM4·HBM4E 고객 진행, eSSD 주문이 확인된다.
4. Spot 시장 부진이 contract price cut이나 server DRAM 주문 둔화로 번지지 않는다.

무효화 조건은 다음이다.

| 무효화 조건 | 의미 |
|---|---|
| Contract DRAM/NAND 가격 하락 전환 | 가격 thesis 훼손 |
| Server DRAM·HBM·eSSD order slowdown | AI 메모리 수요 thesis 훼손 |
| ASML·TSMC가 CapEx 둔화를 강하게 말함 | 하이퍼스케일러 투자 thesis 약화 |
| 외국인 매도와 원화 약세가 동시에 심해짐 | 한국 비중 축소 압력 |
| 시장 breadth 추가 악화 | 삼성전자만 좋아도 수급 흡수 약화 |

## 15. 결론

삼성전자의 2Q26 잠정실적은 thesis를 약하게 만든 숫자가 아니다. 오히려 반대다. 89.4조원 영업이익, DRAM ASP +47%, NAND ASP +66%, legacy memory 가격 급등, 2027년까지 이어지는 하이퍼스케일러 CapEx, AI 서버 공급망 매출은 모두 삼성전자 투자 논거를 강화한다.

하지만 오늘 주가와 수급은 타이밍을 훼손했다. 외국인은 팔았고, 개인이 받았다. 금리는 높고, 환율은 부담이며, ASML과 TSMC라는 high bar 이벤트가 남았다. 시장 폭도 약하다.

그래서 결론은 명확하다.

삼성전자는 나빠진 것이 아니다. 다만 오늘 시장은 “좋은 숫자”보다 “다음 좋은 숫자와 그 숫자를 믿고 살 수급”을 요구했다. 지금은 thesis를 버릴 때가 아니라, 포지션을 지키되 추가매수는 멈추고 다음 관문을 확인할 때다.

## 근거 구분

| 구분 | 내용 |
|---|---|
| Fact | 삼성전자 공식 2Q26 잠정 매출 171조원, 영업이익 89.4조원. 1Q26·2Q25 비교 수치. ASML 7월 15일, TSMC 7월 16일 실적 일정. 로컬 DB의 삼성전자 가격·수급·외국인 보유율. |
| Inference | 삼성전자 thesis는 강화됐지만 단기 timing은 훼손됐다는 판단. TrendForce spot 데이터는 bear confirmation이 아니라 가격 발견이라는 해석. Morgan Stanley peak thesis는 추격 경고이지 구조적 매도 근거는 아니라는 판단. |
| Speculation | 하이퍼스케일러 CapEx가 2027년까지 약 1조달러로 커지며 삼성전자 메모리 수요를 더 오래 지지할 수 있다는 시나리오. |
| Blocked | Bloomberg 외국인 outflow 수치의 공식 통계 대조, Meritz·TrendForce 원문 보고서 전문 확인, 삼성전자 DS 부문별 2Q26 실제 이익, HBM4·HBM4E 고객별 물량과 마진. |

## Evidence Ledger

| 항목 | 출처 |
|---|---|
| 삼성전자 2Q26 잠정실적 | [Samsung Electronics 공식 뉴스룸](https://news.samsung.com/global/samsung-electronics-announces-earnings-guidance-for-second-quarter-2026) |
| ASML 2Q26 일정 | [ASML financial calendar](https://www.asml.com/investors/financial-calendar) |
| TSMC 2Q26 일정 | [TSMC 2Q26 quarterly results](https://investor.tsmc.com/english/quarterly-results/2026/q2) |
| 삼성전자 가격·수급 | 로컬 Research DB: `prices_daily`, `investor_flow_daily`, `foreign_ownership_daily`, 2026-07-08 기준 |
| 메모리 가격·AI 서버·외국인 outflow 코멘트 | 첨부 리서치 패킷. 원문 전문 미대조 항목은 본문에서 시장 코멘트 또는 방향성 신호로 분리 |
| 관련 선행 분석 | Korea Invest Insights의 삼성전자 2Q26 프리뷰, 마이크론 FY3Q26, 빅테크 어닝콜, 빅테크 자금조달, 엔비디아 유사 분기 분석 |
