---
title: "미국 5월 CPI 프리뷰: 기본값은 Core +0.26%, 방어 전환선은 +0.35%"
date: 2026-06-06T20:40:00+09:00
description: "2026년 5월 미국 CPI는 에너지와 2025년 5월 저베이스 때문에 헤드라인 4.1~4.2%가 가능하다. 그러나 투자 판단의 핵심은 헤드라인이 아니라 Core CPI MoM이다. 확률가중 중심값은 +0.26%, +0.30% 이하 확률은 75%, +0.35% 이상 hot print 확률은 13%로 본다."
categories: ["Macro-Insight", "Market-Outlook"]
tags:
  - "미국 CPI"
  - "Core CPI"
  - "FOMC"
  - "미국 금리"
  - "달러"
  - "원화"
  - "KOSPI"
  - "KOSDAQ"
  - "에너지"
  - "PPI"
  - "한국 증시"
slug: us-may-2026-cpi-preview-core-mom-trigger-korea-market-2026-06-06
valley_cashtags:
  - 삼성전자
  - SK하이닉스
  - NAVER
  - LG에너지솔루션
  - S-Oil
  - 대한항공
  - KB금융
series: ["macro-gates-2026", "korea-rerating-2026"]
draft: false
---

> 📚 연결 맥락
> 이 글은 [강한 고용 뒤 CPI·BOJ·FOMC 이벤트 클러스터](/ko/post/us-cpi-boj-fomc-macro-event-cluster-korea-reaction-function-2026-06-06/)의 후속 CPI 딥다이브입니다. 앞글이 “한국장은 예측보다 반응 함수가 중요하다”고 정리했다면, 이번 글은 그 반응 함수의 첫 관문인 **미국 5월 CPI 자체**를 분해합니다. 함께 읽을 글은 [고용 쇼크와 KOSPI 8,000 관문](/ko/post/us-jobs-rate-hike-shock-kospi-macro-gate-2026-06-06/), [중반을 넘어선 AI 슈퍼사이클](/ko/post/ai-supercycle-midgame-rate-risk-yellow-not-red-2026-06-06/), [복합 risk-off와 회복 조건](/ko/post/macro-snapshot-complex-risk-off-recovery-triggers-2026-05-17/)입니다. 관련 허브는 [한국 데일리 마켓 허브](/ko/page/korea-daily-market-hub/)와 [해외 투자자용 한국 주식 허브](/ko/page/korea-stocks-foreign-investors-hub/)입니다.

## TL;DR

- **헤드라인 CPI는 높게 나올 가능성이 큽니다.** 에너지 가격과 2025년 5월 저베이스가 동시에 작동합니다. 중심 전망은 **Headline CPI +0.43~0.46% MoM / 4.1~4.2% YoY**입니다.
- **핵심 투자 변수는 헤드라인이 아니라 Core MoM입니다.** Cleveland Fed 6월 5일 nowcast 기준 2026년 5월 Core CPI는 **+0.23% MoM / 2.82% YoY**입니다. 업로드 메모의 bottom-up 값 **+0.28%**와 Cleveland nowcast 사이를 반영하면, 확률가중 중심값은 **Core CPI MoM +0.26%**입니다. ([Cleveland Fed][1])
- **중립적 확률분포로 보면 안도 쪽이 기본값입니다.** Core MoM이 **+0.30% 이하일 확률은 75%**, **+0.35% 이상 hot print 확률은 13%**로 봅니다. 즉 headline은 높아도 core 안정으로 해석될 가능성이 더 높지만, +0.35% 이상에서는 바로 방어로 전환해야 합니다.
- **미국·한국 상장주식 투자자는 금리 민감 성장주와 에너지·퀄리티·달러 수혜를 분리해야 합니다.** 한국 투자자는 특히 원화 약세 방어, 반도체 밸류에이션 민감도, 정유·항공·화학·전력 업종의 에너지 비용 전가력을 따로 봐야 합니다.

<div class="thesis-callout">
  <div class="thesis-callout__label">핵심 문장</div>
  <div class="thesis-callout__body">
    이번 CPI의 기본값은 “헤드라인은 높지만 core는 통제권”이다. 확률가중 중심값은 <strong>Core CPI MoM +0.26%</strong>, +0.30% 이하 확률은 75%다. 다만 <strong>+0.35% 이상</strong>에서는 안도 반등 논리를 접고 금리·달러·성장주 멀티플 방어 모드로 전환해야 한다.
  </div>
</div>

---

## 1. 스코프: 이 글이 답하는 질문

이번 리서치의 출발점은 “2026년 5월 미국 CPI가 에너지 쇼크와 base effect로 컨센서스를 상회할 수 있다”는 발표 전 proxy 기반 분석입니다. 원문은 헤드라인 CPI YoY **4.1~4.2%**, 코어 CPI YoY **2.9~3.0%**, 헤드라인 MoM **+0.4~0.5%**, 코어 MoM **+0.3%**를 제시했습니다.

이 글은 그 메모를 블로그 독자와 포트폴리오 의사결정용으로 재구성합니다. 핵심 질문은 다섯 가지입니다.

| 질문 | 왜 중요한가 |
|---|---|
| 1. 실제 서프라이즈 포인트는 headline인가 core인가? | headline이 높아도 에너지 때문이면 시장 충격은 제한될 수 있습니다. |
| 2. 에너지 가격과 2025년 5월 저베이스는 CPI를 어디까지 끌어올리나? | YoY 숫자의 기계적 상방을 구분해야 합니다. |
| 3. 코어 CPI 2.9~3.0% 전망은 공식 nowcast와 비교해 얼마나 공격적인가? | Cleveland Fed nowcast와 차이가 크면 리스크 시나리오로 봐야 합니다. |
| 4. CPI는 6월 FOMC, 미국 금리, 달러, 위험자산에 어떤 1차 반응을 만들까? | 6월 16~17일 FOMC 전 마지막 큰 인플레 데이터입니다. |
| 5. 미국 및 한국 주식 투자자는 업종·스타일·환노출을 어떻게 조정해야 하나? | 한국 투자자는 주가 beta와 원화 약세 방어를 분리해야 합니다. |

[Fact] BLS 일정상 미국 5월 CPI는 **2026년 6월 10일 08:30 ET**에 발표됩니다. 한국 시간으로는 **2026년 6월 10일 21:30 KST**입니다. ([BLS CPI Schedule][2])

---

## 2. 문서 스냅샷: 무엇은 유지하고, 무엇은 낮춰야 하나

| 항목 | 정제 후 판단 |
|---|---|
| 문서 성격 | 발표 전 CPI nowcasting 메모입니다. 공식 예측이 아니라 proxy 기반 이벤트 리서치입니다. |
| 발표 일정 | 2026년 6월 10일 08:30 ET, 한국시간 21:30 KST. |
| 기존 강점 | 에너지 가격, 2025년 5월 저베이스, 직전 4월 CPI 구조를 제대로 포착했습니다. |
| 기존 약점 | “코어 YoY 3.0%”와 “컨센서스 상회” 프레이밍이 다소 강합니다. CPI YoY는 NSA 지수 기준인데, 원문은 SA MoM 기반 근사에 많이 의존합니다. |
| 최종 정제 방향 | **헤드라인 상방은 유지합니다. 코어 상방은 조건부로 낮춥니다. 시장 함의는 Core MoM trigger 중심으로 재구성합니다.** |

핵심은 “높은 headline”과 “위험한 core”를 분리하는 것입니다. 헤드라인 CPI가 4%대 초반으로 올라오는 것 자체는 충분히 가능합니다. 그러나 Fed와 주식시장이 진짜로 겁내는 것은 에너지 한 달 상승보다 **core 서비스, shelter, core goods가 같이 다시 뜨거워지는지**입니다.

---

## 3. 팩트체크: 유지할 주장과 수정할 주장

### 3-1. 유지할 주장

**첫째, 4월 기준선은 맞습니다.**

[Fact] BLS 2026년 4월 CPI는 headline CPI **+0.6% MoM SA / +3.8% YoY NSA**, core CPI **+0.4% MoM / +2.8% YoY**였습니다. BLS는 4월 CPI에서 에너지 **+3.8% MoM**, gasoline **+5.4% MoM**, shelter **+0.6% MoM**, airline fares **+2.8% MoM**도 함께 발표했습니다. ([BLS CPI Summary][3])

4월 숫자는 두 가지를 말해줍니다. 에너지와 휘발유는 이미 헤드라인 CPI를 밀어올리고 있었고, shelter와 항공요금은 core 쪽에서도 완전히 식지 않았습니다.

**둘째, 2025년 5월 저베이스는 강한 상방 요인입니다.**

[Fact] BLS 2025년 5월 CPI는 headline CPI와 core CPI가 모두 **+0.1% MoM SA**였습니다. 따라서 2026년 5월 MoM이 +0.1%를 넘으면 YoY에는 기계적 상방 압력이 생깁니다. ([BLS May 2025 CPI][4])

이것은 CPI 해석에서 중요합니다. YoY가 올라간다고 해서 반드시 “기조 물가가 재가속”된 것은 아닙니다. 전년 같은 달이 너무 낮았기 때문에 생기는 base effect일 수 있습니다.

**셋째, 에너지 proxy는 헤드라인 상방을 강하게 지지합니다.**

[Fact] EIA weekly regular gasoline price는 2026년 4월 주간 평균 약 **$4.103/gal**, 5월 주간 평균 약 **$4.479/gal**입니다. 계산식은 다음과 같습니다. ([EIA][5])

```text
May gasoline proxy change = 4.479 / 4.103 - 1 = +9.2%
```

단, 6월 1일 가격은 **$4.305/gal**로 내려왔습니다. 그래서 5월 CPI에는 gasoline이 헤드라인 상방 요인이지만, 6월 CPI에는 반대 방향 압력이 생길 수 있습니다.

### 3-2. 수정할 주장

| 원문 표현 | 정제 후 표현 |
|---|---|
| “헤드라인과 코어 모두 컨센서스를 상회할 가능성이 높다.” | **헤드라인 YoY 4.1~4.2%는 타당하지만, 코어 YoY 3.0%는 공격적 상단 시나리오입니다.** |
| “Core CPI YoY 2.9~3.0%” | **Base는 2.8~2.9%, upside는 3.0%.** Cleveland Fed nowcast는 May core CPI **2.82% YoY**입니다. |
| “Core MoM +0.3%면 core YoY 3.0%” | SA MoM과 NSA YoY를 단순 연결하면 오차가 생깁니다. 공식 YoY는 NSA index 기준입니다. |
| “5년 기대인플레 사상 최고” | 삭제해야 합니다. Michigan long-run inflation expectations 3.9%는 높지만, “사상 최고”라고 쓰면 부정확합니다. ([Michigan Surveys of Consumers][6]) |
| “예측시장 확률 65%, 연내 인상 30%” | 출처·계약명·기준시각 없이는 투자 메모 본문에서 쓰지 않는 편이 낫습니다. |

---

## 4. 정제된 Core CPI MoM 확률분포

헤드라인은 에너지와 저베이스 때문에 높게 나올 가능성이 큽니다. 그러나 주식시장의 핵심은 core입니다. 여기서는 Cleveland Fed nowcast **+0.23%**, bottom-up 가중합 **+0.28%**, 4월 core 재가속 위험을 함께 반영해 확률분포를 잡습니다.

| 시나리오 | Core CPI MoM | 확률 | 시장 해석 | 주식시장 반응 |
|---|---:|---:|---|---|
| **Cool** | **≤ +0.20%** | **15%** | 명확한 디스인플레 | 강한 안도 반등 |
| **Soft Base** | **+0.21~0.25%** | **35%** | Cleveland nowcast 부합 | 반등 가능성 높음 |
| **Sticky Base** | **+0.26~0.30%** | **25%** | 점착적이나 통제권 | 하락 후 반등 가능 |
| **Warm** | **+0.31~0.34%** | **12%** | 애매함. 금리 부담 잔존 | 제한적 반등 또는 혼조 |
| **Hot** | **+0.35~0.39%** | **10%** | 2차 파급 우려 | 성장주·테크 압박 |
| **Shock** | **≥ +0.40%** | **3%** | 4월 재가속 반복 | 반등 실패, 금리·달러 상승 |

확률가중 기대값은 다음과 같이 봅니다.

```text
EV = Σ(시나리오 확률 × 구간 중간값) ≈ +0.26%
```

반올림 기준은 Core MoM 소수점 둘째 자리, 확률은 1%p 단위입니다.

이 분포를 세 줄로 줄이면 다음과 같습니다.

| Core CPI MoM 범위 | 확률 | 투자 판단 |
|---|---:|---|
| **+0.30% 이하** | **75%** | headline shock를 에너지발 일시 요인으로 해석할 가능성. 하락장 반등 가능. |
| **+0.31~0.34%** | **12%** | 애매함. 반등하더라도 강하지 않을 가능성. |
| **+0.35% 이상** | **13%** | 위험. 금리 상승·달러 강세·테크 밸류에이션 압박 재개. |

정제된 핵심 문장은 이렇습니다.

> 현재 분포로 보면 **“headline은 높지만 core MoM은 안정화될 가능성이 더 높고, 그래서 하락장 반등이 가능하다”**가 기본값입니다. 다만 이 판단은 조건부입니다. **Core MoM +0.35% 이상에서는 반등 논리를 폐기하고 방어로 전환**해야 합니다.

---

## 5. 가중합 재계산: 왜 headline +0.45%, core +0.28%가 중심인가

[Fact] BLS 2026년 4월 relative importance 기준 주요 가중치는 energy **7.090%**, food **13.560%**, core CPI **79.351%**, commodities less food & energy **19.002%**, shelter **35.320%**입니다. ([BLS CPI Table 1][7])

원문 부문별 가정을 최신 BLS 가중치에 대입하면 headline은 다음과 같이 계산됩니다.

```text
Headline CPI MoM proxy
= 0.07090 × 2.8
 + 0.13560 × 0.2
 + 0.19002 × 0.1
 + 0.35320 × 0.32
 + 0.25028 × 0.35
= 0.445% ≈ +0.45%
```

Core는 food와 energy를 제외한 부분으로 다시 나눠 계산합니다.

```text
Core CPI MoM proxy
= (0.19002 × 0.1 + 0.35320 × 0.32 + 0.25028 × 0.35) / 0.79351
= 0.277% ≈ +0.28%
```

해석은 명확합니다.

| 항목 | 산식이 말하는 것 |
|---|---|
| Headline | +0.43%보다 **+0.43~0.46% range**로 쓰는 편이 안전합니다. |
| Core | Cleveland Fed nowcast +0.23%와 bottom-up +0.28% 사이를 반영하면 확률가중 중심값은 **+0.26%**입니다. |
| 투자 의미 | headline high는 기본값입니다. **core +0.30% 이하가 기본 안도 분포**, **+0.35% 이상은 방어 전환 분포**입니다. |

이 산식만 놓고 보면 core +0.28%가 자연스럽습니다. 여기에 Cleveland Fed의 +0.23% nowcast를 같이 반영하면, +0.23~0.28% 사이가 중심 분포가 됩니다. 그래서 “core 3.0% YoY”를 기본값으로 두기보다, **Core MoM +0.26% 전후**를 중심으로 보는 편이 더 중립적입니다.

---

## 6. Macro transmission map: CPI가 자산가격으로 넘어가는 경로

| CPI 구성 요소 | 1차 자산 반응 | 2차 확인 지표 | 투자 해석 |
|---|---|---|---|
| Energy CPI 상방 | Headline CPI 상승, 유가·휘발유 민감 업종 변동성 확대 | EIA gasoline, crude, diesel, airline fuel | Headline shock만으로는 Fed가 즉시 반응하지 않을 가능성. |
| Shelter 정상화 | Core MoM 안정 | Rent, OER, lodging away from home | Core가 +0.25~0.30%면 주식시장 안도 가능. |
| Supercore 재가속 | 장기금리 상승, USD 강세, 성장주 압박 | Airline fares, insurance, medical services | Core +0.35~0.40% 이상이면 hawkish repricing. |
| PPI 후행 확인 | 마진 압박·가격 전가 확인 | 6/11 PPI | 4월 PPI가 이미 강했기 때문에 5월 PPI가 재차 강하면 CPI 안도 효과가 약해집니다. |

[Fact] BLS 2026년 4월 PPI final demand는 **+1.4% MoM / +6.0% YoY**였습니다. 4월 전월비 상승률은 2022년 3월 이후 가장 컸고, 전년비 상승률도 다시 높아졌습니다. ([BLS PPI][8])

따라서 CPI가 다소 안도적이어도, 다음 날 PPI가 다시 뜨거우면 시장은 “기업 원가 압박이 아직 소비자물가로 덜 넘어갔을 뿐”이라고 해석할 수 있습니다.

---

## 7. 학계·연구자 관점: SA MoM과 NSA YoY를 섞으면 안 된다

학계·연구자 관점의 핵심은 **SA MoM과 NSA YoY를 혼동하지 않는 것**입니다. BLS의 공식 YoY는 NSA index 기반입니다. Cleveland Fed도 CPI YoY nowcast가 NSA CPI inflation 기반이라고 설명합니다. 반면 시장은 headline/core MoM SA를 가장 먼저 봅니다. ([Cleveland Fed][1])

따라서 투자 메모에서는 “YoY가 오른다”와 “MoM이 재가속된다”를 분리해야 합니다.

| 구분 | 의미 |
|---|---|
| YoY 상승 | 전년 저베이스, 에너지, 지수 기준 효과가 섞입니다. |
| MoM 재가속 | 현재 월의 물가 압력이 다시 커지는 신호입니다. |
| Core MoM 재가속 | Fed와 위험자산에 가장 민감한 신호입니다. |

현재 합의된 것은 gasoline과 oil price가 headline CPI nowcasting에 강한 고빈도 proxy라는 점입니다. Cleveland Fed nowcasting 모델도 daily oil price와 weekly retail gasoline price를 사용합니다. ([Cleveland Fed][1])

논쟁 중인 것은 tariff pass-through, airline fare pass-through, shelter catch-up이 5월에 얼마나 남아 있느냐입니다. 만약 5월 core CPI가 Cleveland Fed nowcast **+0.23% MoM**보다 높게 나온다면, 시장은 그 초과분이 shelter인지, airfare인지, goods tariff인지부터 따질 것입니다.

---

## 8. 산업·기업 관점: 같은 CPI라도 업종별 의미가 다르다

| 업종 | CPI hot case 의미 | 봐야 할 변수 |
|---|---|---|
| 에너지 기업 | headline CPI 상방은 원유·정유·gasoline margin 환경을 지지합니다. | 6월 gasoline price 하락이 momentum을 꺾는지 |
| 항공·운송·물류 | fuel cost와 wage cost가 동시에 압박될 수 있습니다. | airline fares 상승이 비용을 얼마나 전가하는지 |
| 소비재·리테일 | gasoline shock는 실질 가처분소득을 압박합니다. | 저소득층 노출, discretionary retail 매출 |
| 금융 | hot core CPI는 금리 상승과 yield curve 재가격을 유발할 수 있습니다. | NII 수혜 vs credit cost와 경기 둔화 |
| 소프트웨어·바이오·고PER 성장주 | 할인율 상승에 가장 취약합니다. | 매출 성장보다 현금흐름·FCF margin |

에너지 기업은 headline CPI 상방을 “나쁜 뉴스”로만 보지 않습니다. 반대로 항공·화학·유틸리티는 에너지 비용 상승이 이익률을 직접 압박할 수 있습니다. 그래서 한국 투자자에게 CPI는 “미국 금리 이벤트”인 동시에 “에너지 비용 이벤트”입니다.

---

## 9. Fed와 6월 FOMC: CPI는 점도표 직전 데이터다

[Fact] Fed의 2026년 4월 FOMC statement는 inflation이 elevated이고 글로벌 에너지 가격 상승을 일부 반영한다고 명시했습니다. 정책금리 target range는 **3.50~3.75%**로 유지했습니다. 추가 정책 조정은 incoming data, outlook, balance of risks에 따라 판단한다고 밝혔습니다. ([Federal Reserve][9])

[Fact] 6월 FOMC는 **2026년 6월 16~17일**이며 Summary of Economic Projections가 동반되는 회의입니다. ([Federal Reserve Calendar][10])

따라서 6월 10일 CPI는 단순한 월간 데이터가 아닙니다. FOMC 점도표와 기자회견 직전에 나오는 인플레이션 데이터입니다. Core CPI가 hot하게 나오면, 시장은 다음을 곧바로 가격에 반영하려 할 수 있습니다.

| CPI 결과 | FOMC 해석 |
|---|---|
| Core ≤ +0.25% | headline은 에너지, core는 안정. Fed easing bias 유지 가능. |
| Core +0.26~0.30% | 점착적이지만 통제권. 금리 첫 반응이 튀어도 되돌림 가능. |
| Core +0.31~0.34% | 애매합니다. PPI와 FOMC 톤 확인 필요. |
| Core ≥ +0.35% | 인플레 재가속 우려. 점도표와 기자회견 hawkish repricing 가능. |
| Core ≥ +0.40% + shelter/supercore 동반 상승 | 기대인플레·서비스 물가 재고착 우려. 장기금리와 달러 상승 압력. |

Fed의 longer-run goals 문서는 장기 기대인플레가 2%에 잘 고정되는 것이 price stability와 moderate long-term rates에 중요하다고 명시합니다. ([Federal Reserve Longer-Run Goals][11]) 그래서 hot CPI가 “기대인플레가 흔들린다”는 해석으로 연결되면, 시장 반응은 더 커질 수 있습니다.

---

## 10. 미국 상장주식 투자자 관점

### 발표 전 포지셔닝

| 포트폴리오 축 | 권고 해석 |
|---|---|
| Long-duration growth | CPI 전 과도한 레버리지 확대는 비대칭적으로 불리합니다. Core hot 시 할인율 상승 충격이 큽니다. |
| Mega-cap quality tech | 단순 growth보다 방어력은 있으나, 금리 급등 시 multiple compression 노출이 있습니다. 실적 가시성이 높은 종목만 선별해야 합니다. |
| Small cap / unprofitable growth | hot CPI에 가장 취약합니다. 자금조달 비용과 신용스프레드 민감도가 높습니다. |
| Energy / refiners | headline shock 국면의 상대 수혜입니다. 단, 6월 gasoline 하락이 이어지면 단기 momentum은 둔화됩니다. |
| Financials | 금리 상승에는 일부 수혜이나, curve와 credit risk를 함께 봐야 합니다. |
| Staples / Healthcare | hot CPI와 소비심리 악화 국면에서 상대 방어 역할을 할 수 있습니다. |
| Airlines / Transportation | fuel cost와 수요 둔화 리스크가 큽니다. airline fares 상승이 매출에는 긍정적이어도 비용 압력이 병존합니다. |

### 발표 후 액션 트리

| CPI 결과 | 미국 주식시장 해석 | 포트폴리오 액션 |
|---|---|---|
| **Core MoM ≤ +0.25%** | Headline은 에너지, core는 안정. | QQQ·quality growth·select semis 회복 가능. Duration risk 일부 재확대 가능. |
| **Core MoM +0.26~0.30%** | 점착적이나 통제권. | 첫 하락 후 반등 가능. 추격보다 금리 되돌림 확인. |
| **Core MoM +0.31~0.34%** | 애매한 결과. | PPI와 FOMC 확인. 업종 중립, quality bias 유지. |
| **Core MoM ≥ +0.35%** | 2차 파급 우려. | High multiple growth, small cap, REITs 축소. Energy, quality cash-flow, defensive factor 선호. |
| **Core MoM ≥ +0.40% + shelter/supercore 동반 상승** | Fed repricing. | 지수 beta 축소, 현금·단기채·달러 비중 확대. Equity는 earnings visibility 높은 대형주 중심. |

미국 투자자에게 이번 CPI는 **index direction bet**보다 **factor rotation event**입니다. Core가 낮으면 “headline wall of worry”를 넘어 tech·growth가 반등할 수 있습니다. Core가 높으면 valuation duration이 긴 종목부터 압박받고, energy·defensive·quality cash-flow가 상대 우위에 섭니다.

---

## 11. 한국 상장주식 투자자 관점

한국 투자자는 미국 CPI를 두 개의 경로로 받습니다.

| 경로 | 연결 방식 |
|---|---|
| 미국 금리·달러 경로 | Hot core CPI → 미국 장기금리 상승 → 달러 강세·원화 약세 → 외국인 수급 악화 가능성 |
| 실물 비용 경로 | 에너지 가격 상승 → 한국 수입물가·기업 마진 압박 → 항공·화학·전력·운송 등 비용 민감 업종 부담 |

### 한국 주식시장 스타일별 영향

| 한국 시장 스타일 | CPI hot case 영향 | CPI cool case 영향 |
|---|---|---|
| 반도체 / AI supply chain | 달러 매출 환산에는 우호적이나, 미국 tech multiple 압박이 더 크면 단기 조정 가능. | 미국 growth 반등과 함께 수급 회복 가능. |
| 자동차 / 조선 / 기계 수출주 | 원화 약세는 매출 환산에 긍정적. 단, 미국 수요 둔화와 원자재 비용은 부담. | 원화 안정·수요 우려 완화. 실적주 중심 우호. |
| 2차전지 / 인터넷 / 바이오 | 할인율 상승에 취약. 고PER·적자 성장주는 특히 불리. | 금리 하락 시 낙폭 회복 가능. |
| 정유 | 유가·정제마진 상승 시 상대 수혜. 다만 정부 가격통제·수요 둔화 확인 필요. | 유가 하락 시 momentum 둔화. |
| 화학 | feedstock 비용 상승과 글로벌 수요 둔화가 동시에 부담. | 유가 안정 시 margin 회복 가능. |
| 항공 / 여행 | jet fuel 비용과 환율 부담. 항공료 전가가 가능해야 방어. | 유가·환율 안정 시 반등 후보. |
| 전력 / 유틸리티 | 에너지 수입비용 상승이 부담. 요금 전가 지연 시 부정적. | 에너지 안정 시 비용 부담 완화. |
| 은행 / 보험 | 금리 상승에는 일부 긍정적이나, 원화 약세·신용위험·부동산 부담을 같이 봐야 함. | 금리 하락 시 보험 할인율에는 부담, 은행 NIM에는 중립~부정적. |

### 한국 투자자용 포트폴리오 대응

**1) 미국 주식 보유 한국 투자자**

Hot CPI에서는 미국 주식 가격은 하락할 수 있지만, 원화 약세가 USD 비헤지 보유분의 원화 기준 손실을 일부 완충할 수 있습니다. 따라서 CPI 전후에는 **주식 beta와 환헤지 비율을 분리해서 판단**해야 합니다. 주가 하락을 우려한다고 무조건 환헤지를 높이면, hot CPI 시 원화 약세 방어력을 잃을 수 있습니다.

**2) 한국 주식 중심 투자자**

미국 CPI가 hot하게 나오면 KOSPI 전체보다 **업종 차별화**가 중요합니다. 반도체는 원화 약세 수혜와 미국 tech de-rating 위험이 충돌합니다. 정유는 에너지 가격 상승 수혜가 있으나, 화학·항공·유틸리티는 비용 압박이 우선합니다. 인터넷·바이오·2차전지처럼 할인율 민감도가 높은 섹터는 core CPI가 높은 경우 방어력이 낮습니다.

**3) 외국인 수급 관점**

Hot core CPI → 미국 금리 상승 → 달러 강세 → 신흥국 risk budget 축소로 연결되면 한국 주식의 외국인 수급은 단기적으로 약해질 수 있습니다. 반대로 core가 낮고 headline만 높은 경우, “에너지 일시 충격”으로 해석되면서 외국인 수급은 빠르게 복원될 수 있습니다.

---

## 12. 발표 직후 체크리스트

| 우선순위 | 확인 항목 | 판단 기준 |
|---:|---|---|
| 1 | **Core CPI MoM** | +0.25% 이하 안도, +0.26~0.30% 통제권, +0.31~0.34% 애매, +0.35% 이상 위험, +0.40% 이상 hawkish shock. |
| 2 | Shelter / OER / Rent | shelter가 +0.3% 전후면 안도, +0.5% 이상이면 core stickiness. |
| 3 | Supercore | airline fares, insurance, medical services가 동반 상승하면 2차 파급. |
| 4 | Core goods | apparel, household furnishings, vehicles 상승 시 tariff pass-through 우려. |
| 5 | Energy CPI | headline 설명용. Fed 반응의 핵심은 아님. |
| 6 | 6/11 PPI | 4월 PPI가 이미 강했으므로 5월 PPI가 재차 강하면 CPI 안도 효과 훼손. |
| 7 | 6/16~17 FOMC | SEP와 statement에서 inflation expectations 문구 변화 확인. |

---

## 최종 투자 결론

이번 CPI preview의 정제된 결론은 다음과 같습니다.

<div class="thesis-callout">
  <div class="thesis-callout__label">Final Take</div>
  <div class="thesis-callout__body">
    헤드라인 CPI 4.1~4.2%는 충분히 가능한 base case다. 그러나 확률가중 중심값은 Core MoM +0.26%이고, +0.30% 이하 확률은 75%다. 기본값은 안도 반등 가능성이다. 다만 <strong>Core CPI MoM +0.35% 이상</strong>부터는 반등 논리를 접고 방어로 전환해야 한다.
  </div>
</div>

미국 상장주식 투자자는 **high multiple growth와 small cap의 금리 민감도**를 줄이고, CPI 결과에 따라 quality tech와 defensive cash-flow 간 rotation을 준비해야 합니다.

한국 상장주식 투자자는 **원화 약세 방어 효과와 KOSPI 성장주 de-rating 위험을 분리**해야 합니다. Base case에서는 “headline은 높고 core는 통제권”이라는 해석이 가능합니다. 이 경우 미국·한국 모두 단기 변동성은 크지만 구조적 매도 신호는 아닙니다. 오히려 최근 하락장이 CPI를 앞두고 위험을 선반영했다면, **Core +0.30% 이하**에서는 안도 반등이 나올 수 있습니다.

Hot case에서는 미국 장기금리·달러·원화 약세가 동시에 움직일 수 있습니다. 이 경우 한국 투자자는 **반도체·인터넷·2차전지의 beta 축소, 정유·퀄리티 수출주·달러 현금성 자산의 상대 방어력**을 우선 검토해야 합니다.

## 근거 분류

### [Fact]

- BLS 일정상 2026년 5월 CPI는 2026년 6월 10일 08:30 ET에 발표됩니다. ([BLS CPI Schedule][2])
- Cleveland Fed 6월 5일 nowcast 기준 2026년 5월 CPI는 **+0.46% MoM / 4.18% YoY**, core CPI는 **+0.23% MoM / 2.82% YoY**입니다. ([Cleveland Fed][1])
- BLS 2026년 4월 CPI는 headline **+0.6% MoM / +3.8% YoY**, core **+0.4% MoM / +2.8% YoY**였습니다. ([BLS CPI Summary][3])
- 2025년 5월 CPI는 headline과 core 모두 **+0.1% MoM SA**였습니다. ([BLS May 2025 CPI][4])
- 2026년 4월 PPI final demand는 **+1.4% MoM / +6.0% YoY**였습니다. ([BLS PPI][8])
- 2026년 4월 FOMC는 기준금리 target range를 **3.50~3.75%**로 유지했습니다. ([Federal Reserve][9])

### [Inference]

- 5월 CPI는 headline 상방이 유력하지만, 이는 에너지와 저베이스의 영향이 큽니다.
- Core CPI MoM의 확률가중 중심값은 +0.26%로 추정하며, +0.30% 이하 확률 75%, +0.35% 이상 확률 13%로 봅니다.
- Core CPI MoM이 +0.35%를 넘을 때 “Fed repricing”과 성장주 멀티플 압박이 본격화될 가능성이 큽니다.
- 한국 시장에서는 원화 약세 방어와 성장주 de-rating이 동시에 작동할 수 있으므로, 종목·업종별 반응이 크게 갈릴 가능성이 높습니다.

### [Blocked]

- 5월 CPI 실제값, 5월 PPI 실제값, 6월 FOMC 점도표와 기자회견은 아직 발표 전입니다.
- 본문 수치는 사용자 제공 리서치와 공식 통계·nowcast를 결합한 발표 전 이벤트 분석이며, 실제 발표 후 빠르게 업데이트가 필요합니다.
- 개별 한국 업종의 실제 주가 반응은 CPI 발표 직후 미국 금리·달러·원화·외국인 선물 수급을 함께 확인해야 합니다.

[1]: https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting "Cleveland Fed Inflation Nowcasting"
[2]: https://www.bls.gov/schedule/news_release/cpi.htm "BLS CPI Release Schedule"
[3]: https://www.bls.gov/news.release/cpi.nr0.htm "BLS Consumer Price Index Summary - April 2026"
[4]: https://www.bls.gov/news.release/archives/cpi_06112025.pdf "BLS Consumer Price Index - May 2025"
[5]: https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?f=W&n=PET&s=EMM_EPMR_PTE_NUS_DPG "EIA Weekly U.S. Regular Gasoline Prices"
[6]: https://www.sca.isr.umich.edu/ "University of Michigan Surveys of Consumers"
[7]: https://www.bls.gov/news.release/cpi.t01.htm "BLS CPI Table 1"
[8]: https://www.bls.gov/news.release/ppi.nr0.htm "BLS Producer Price Index Summary - April 2026"
[9]: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm "Federal Reserve FOMC Statement - April 29, 2026"
[10]: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm "Federal Reserve FOMC Calendars"
[11]: https://www.federalreserve.gov/monetarypolicy/files/FOMC_LongerRunGoals.pdf "Statement on Longer-Run Goals and Monetary Policy Strategy"
