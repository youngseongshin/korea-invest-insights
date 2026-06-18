---
title: "스페이스X 상장은 '우주'가 아니라 'AI 컴퓨트' 이벤트다: 공모자금 활용계획과 최태원·머스크 미팅이 한국 메모리에 주는 의미"
slug: "spacex-ipo-ai-compute-use-of-proceeds-sk-musk-korea-memory-2026-06-18"
date: 2026-06-18T17:30:00+09:00
description: "스페이스X 상장신고서(S-1)의 공모자금 활용계획은 발사체보다 AI 컴퓨트 인프라 확장을 앞에 둔다. 가장 큰 capex·적자처는 로켓이 아니라 xAI다. 즉 750억달러 공모는 AI 인프라 투자를 가속하는 자금이고, 그 수요는 GPU·HBM·메모리·전력으로 흐른다. 오늘 보도된 최태원·머스크 미팅(테슬라 맞춤형 HBM, xAI 데이터센터 메모리)이 그 흐름을 한국 메모리로 잇는 첫 연결고리다."
categories: ["Korea Market", "Macro-Insight", "AI Infrastructure"]
tags:
  - "스페이스X"
  - "SpaceX IPO"
  - "AI 컴퓨트"
  - "xAI"
  - "Starlink"
  - "HBM"
  - "SK하이닉스"
  - "삼성전자"
  - "최태원"
  - "일론 머스크"
  - "AI 인프라"
  - "Research OS"
series: ["Korea Market Regime"]
draft: false
---

> 연결 맥락
> 이 글은 [AI 슈퍼사이클은 왜 더 길어지는가 — IPO 자금과 메모리·스토리지](/ko/post/ai-supercycle-extension-agent-demand-ipo-funding-memory-storage-2026-06-12/), [스페이스X 상장과 한국 증시 유동성](/ko/post/spacex-ipo-korea-market-liquidity-ai-space-readthrough-2026-06-05/), [AI 데이터센터 CapEx 5.3조 달러 시대](/ko/post/ai-datacenter-capex-5p3t-korea-power-substrate-storage-bottleneck-2026-06-05/), [골드만 토큰 수요 vs JP모간 메모리 ASP](/ko/post/goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31/)의 후속 글이다. 앞글들이 "IPO가 AI 자금의 새 릴레이"라는 큰 틀을 봤다면, 이번 글은 <strong>스페이스X 공모자금 활용계획 원문과 오늘의 최태원·머스크 미팅</strong>으로 그 가설을 구체적으로 검증한다.

## TL;DR

* 가설: <strong>스페이스X의 성공적 상장은 AI 인프라 투자를 더 가속한다.</strong> 근거는 단순하다 — 상장신고서(S-1)의 공모자금 활용계획이 발사체가 아니라 <strong>AI 컴퓨트 인프라 확장</strong>을 전면에 둔다.
* 스페이스X의 가장 큰 자본지출·적자처는 로켓이 아니라 <strong>xAI</strong>다. xAI는 2025년 약 60억달러 손실, 2026년 1분기에만 약 25억달러를 소각했다. 즉 750억달러 공모는 <strong>AI 컴퓨트라는 현금 소각처에 연료를 붓는 자금</strong>이다.
* 이 자금이 GPU·HBM·메모리·전력 수요로 흐른다. 그리고 오늘 보도된 <strong>최태원 SK 회장과 일론 머스크의 미팅(6월 말 예정)</strong>이 그 흐름을 한국 메모리로 잇는 첫 연결고리다 — 테슬라 맞춤형 HBM, HBM4 베이스 다이, xAI 데이터센터 메모리, 위성용 저장장치, ESS까지.
* 결론은 <strong>"스페이스X 우주주"가 아니라 "AI 컴퓨트 자금조달 + 한국 HBM·메모리·전력 옵션"</strong>이다. 단, 미팅은 아직 단독 보도이고 맞춤형 HBM은 타진 단계라는 점을 분리해 봐야 한다.

---

## 1. 통념을 깨자: 스페이스X는 '우주주'가 아니다

스페이스X 상장을 "우주 테마 상장"으로만 보면 핵심을 놓친다. [앞선 글](/ko/post/spacex-ipo-korea-market-liquidity-ai-space-readthrough-2026-06-05/)에서 유동성 관점을 봤다면, 이번에는 <strong>그 돈이 어디로 쓰이는가</strong>를 본다. 답은 상장신고서 안에 있다.

스페이스X는 2026년 5월 20일 SEC에 Form S-1을 제출하고 6월 1일 수정본을 냈다. 주당 135달러, 약 5억5,560만 주 매각으로 <strong>약 750억달러를 조달</strong>하며 기업가치는 약 1.75조달러를 목표로 한다. 미국 IPO 역사상 최대 규모다. ([CNBC][1])

핵심은 규모가 아니라 <strong>용처</strong>다. 복수의 분석에 따르면 S-1의 공모자금 활용계획은 발사체 사업보다 <strong>"AI 컴퓨트 인프라 확장"을 앞에 두고</strong>, 자금 대부분이 AI 컴퓨트 인프라, 발사 능력, Starlink 구축으로 배분된다. ([KraneShares][2])

---

## 2. 공모자금 활용계획 해부

### 2.1 가장 큰 자본지출·적자처는 xAI다

스페이스X의 지배구조를 보면 그림이 분명해진다. <strong>스페이스X가 xAI를 보유하고, xAI가 X(구 트위터)를 보유</strong>하며, 그 아래에 AI 데이터센터·칩 관련 사업이 붙는다. 그리고 가장 큰 영업손실과 자본지출이 바로 이 AI 세그먼트에 있다. xAI는 <strong>2025년 약 60억달러 손실, 2026년 1분기에만 약 25억달러를 소각</strong>했다. ([Via Satellite][3])

자본지출 자체도 수직 상승했다.

```text
스페이스X 총 capex 추이
2023년: 약 44억달러
2025년: 약 207억달러
2026년 1분기: 약 101억달러 (단일 분기)
```

이 곡선은 "로켓 회사"의 곡선이 아니다. AI 컴퓨트와 위성망을 동시에 짓는 회사의 곡선이다. ([Morningstar][4])

### 2.2 'AI 컴퓨트'는 추상이 아니라 물리적 데이터센터다

스페이스X의 AI 컴퓨트는 두 갈래다.

1. <strong>지상 데이터센터</strong>: xAI의 학습·추론용 GPU 클러스터. 여기서 막대한 GPU·HBM·전력 수요가 발생한다.
2. <strong>궤도 데이터센터(AI1)</strong>: 스페이스X COO 그윈 숏웰은 첫 AI1 유닛을 2027년 말 발사할 계획이며, 그 전에는 Starlink 광대역·모바일 위성에 컴퓨트를 탑재하겠다고 밝혔다. ([DCD][5])

즉 공모자금은 "우주로 가는 돈"인 동시에 <strong>"AI 컴퓨트로 가는 돈"</strong>이다. 둘은 분리된 게 아니라, Starlink 발사 능력 자체가 궤도 컴퓨트 인프라의 운반 수단이 된다.

---

## 3. 왜 이것이 'AI 인프라 가속'인가

여기서 가설이 검증된다. [AI 슈퍼사이클 장기화 글](/ko/post/ai-supercycle-extension-agent-demand-ipo-funding-memory-storage-2026-06-12/)에서 정리한 자금 릴레이 — 빅테크 현금 → 회사채 → <strong>공모 시장</strong> — 의 세 번째 단계가 스페이스X 상장으로 실제로 열린다.

핵심 논리는 이렇다.

* xAI는 지금 <strong>현금을 빠르게 소각</strong>하고 있다(2025년 60억달러 손실). 적자 AI 컴퓨트 사업의 연료는 결국 자금조달이다.
* 그 연료가 비상장 단계에서는 머스크 생태계 내부와 사모에서 나왔다면, <strong>스페이스X 상장은 공모 시장이라는 새 자금줄을 연다.</strong>
* 750억달러 중 일부가 AI 컴퓨트로 흘러가면, 그것은 곧 <strong>GPU·HBM·서버 메모리·eSSD·전력 설비 발주</strong>로 이어진다.

즉 스페이스X 상장이 흥행할수록, AI 컴퓨트 capex를 멈추기 어려운 구조가 강화된다. <strong>이것이 "성공적 상장 → AI 인프라 가속"의 메커니즘</strong>이다.

> 다만 정직하게 구분하자. 공모자금은 새 capex를 만들 수도 있고, 이미 계획된 capex를 재무적으로 뒷받침하는 데 그칠 수도 있다. "가속"의 방향은 맞지만 그 크기는 상장 이후 실제 집행으로 확인해야 한다.

---

## 4. 오늘의 연결고리: 최태원·머스크 미팅

가설이 한국으로 연결되는 지점이 오늘 보도됐다. 디지털데일리는 <strong>최태원 SK 회장과 일론 머스크가 6월 말 미국에서 회동할 예정</strong>이라고 단독 보도했다. SK그룹 관계자는 "확인이 어렵다"는 입장이다. ([디지털데일리][6])

보도된 의제는 정확히 위 메커니즘의 한국 쪽 끝단이다.

| 협력 분야 | 내용 | 한국 메모리 연결 |
|---|---|---|
| 반도체 | 테슬라 자체 칩 AI5·AI6용 맞춤형 HBM 타진, HBM4 베이스 다이 협력 | SK하이닉스·삼성전자 HBM |
| AI 인프라 | xAI 데이터센터 확장에 필요한 메모리반도체 | 서버 DRAM·HBM·eSSD |
| 우주·통신 | 스페이스X 우주선·저궤도 위성용 메모리·저장장치 | 고신뢰성 메모리·스토리지 |
| 에너지 | 데이터센터·전력망 ESS(에너지저장장치) | 전력·배터리 밸류체인 |

한 관계자는 "SK그룹이 차기 AI 인프라 주도권을 잡기 위한 협력 범위를 넓히는 중"이라고 평가했다. ([디지털데일리][6])

핵심은 이것이다. 스페이스X 상장이 만든 <strong>"AI 컴퓨트로 가는 공모 자금"</strong>과, SK가 가진 <strong>"AI 컴퓨트가 필요로 하는 HBM·메모리"</strong>가 한 테이블에서 만난다. 자금의 출발점(상장)과 도착점(한국 메모리)이 같은 그림 안에 들어온다.

---

## 5. 한국 read-through (예시·관찰 포인트)

아래는 종목 추천이 아니라, 위 메커니즘이 실제로 작동할 때 어디를 먼저 볼지에 대한 <strong>예시</strong>다.

* <strong>SK하이닉스</strong> — 이번 연결고리의 가장 직접적인 종목. HBM 선두이고, 미팅 의제(테슬라 맞춤형 HBM, xAI 데이터센터 메모리)의 핵심 공급 후보다. 다만 맞춤형 HBM은 아직 "타진" 단계이지 수주가 아니다.
* <strong>삼성전자</strong> — HBM4 베이스 다이, 맞춤형 칩 파운드리, 데이터센터 eSSD라는 복합 옵션. 머스크 생태계의 칩(AI5·AI6)이 외부 파운드리를 쓴다면 옵션 가치가 커진다.
* <strong>전력·ESS·냉각</strong> — AI 컴퓨트는 결국 전력 문제다. 미팅 의제에 ESS가 포함된 것은 [데이터센터 CapEx 글](/ko/post/ai-datacenter-capex-5p3t-korea-power-substrate-storage-bottleneck-2026-06-05/)에서 본 "GPU 다음 병목은 전력"과 정확히 겹친다.

> 공통 조건: 이 종목들이 후보가 되려면 "스페이스X 상장 흥행"만으로는 부족하다. <strong>실제 use-of-proceeds 집행, 미팅의 공식 확인, 맞춤형 HBM의 수주화</strong>가 함께 와야 한다.

---

## 6. Red Team: 이 가설이 약해지는 경우

* <strong>자본 재배치 vs 신규 capex</strong>: 공모자금이 이미 계획된 투자를 재무적으로 메우는 데 그치면, "가속"의 증분은 작다.
* <strong>xAI 적자 리스크</strong>: AI 컴퓨트는 거대한 현금 소각처다(2025년 60억달러 손실). 상장 자금이 이를 메우더라도 수익화가 늦으면 후속 자금조달 부담이 커진다.
* <strong>미팅 미확인</strong>: 최태원·머스크 회동은 단독 보도이고 SK는 "확인 어렵다"는 입장이다. 의제의 맞춤형 HBM도 타진 단계다. 사실로 가격을 매기기엔 이르다.
* <strong>궤도 데이터센터는 장기</strong>: AI1은 2027년 말 발사 계획이다. "위성 컴퓨트"의 한국 메모리 수혜는 옵션이지 단기 실적이 아니다.
* <strong>IPO 자금 흡수 역효과</strong>: [앞선 글](/ko/post/spacex-ipo-korea-market-liquidity-ai-space-readthrough-2026-06-05/)에서 봤듯, 대형 IPO가 기존 AI 포지션을 파는 funding source가 되면 단기적으로 삼성전자·SK하이닉스가 매도 대상이 될 수도 있다. 가속의 재료가 단기 변동성의 재료이기도 하다.

---

## 7. 모니터링 체크리스트

| 체크포인트 | 왜 중요한가 | 판단 |
|---|---|---|
| 스페이스X 공모가·흥행 | 자금조달 규모와 risk-on 강도 결정 | 흥행 시 AI 컴퓨트 capex 가속 논리 강화 |
| use-of-proceeds 실제 집행 | "AI 컴퓨트 우선"이 말이 아니라 발주로 확인되는가 | GPU·HBM·전력 발주 데이터 |
| xAI capex·데이터센터 증설 | AI 컴퓨트 수요의 선행 신호 | 증설 가속 시 메모리 수요 확대 |
| 최태원·머스크 미팅 공식화 | 단독 보도 → investable event 전환 | 공식 발표·MOU 여부 |
| 맞춤형 HBM·베이스 다이 수주 | 타진 → 실적 전환 | SK하이닉스·삼성전자 공시 |
| Starlink·AI1 위성 컴퓨트 | 궤도 데이터센터의 실체화 | 2027년 발사 일정 |

---

## 8. 결론

<div class="thesis-callout">
  <div class="thesis-callout__label">핵심 문장</div>
  <div class="thesis-callout__body">
    스페이스X 상장은 우주 이벤트가 아니라 AI 컴퓨트 자금조달 이벤트다. 그 자금이 GPU·HBM·메모리·전력으로 흐르고, 오늘의 최태원·머스크 미팅은 그 흐름을 한국 메모리로 잇는 첫 연결고리다.
  </div>
</div>

가설 "성공적 상장 → AI 인프라 가속"은 S-1의 공모자금 활용계획(AI 컴퓨트 인프라 전면)과 xAI의 자본지출·적자 구조로 <strong>방향성은 분명히 뒷받침</strong>된다. 다만 그 크기와 타이밍, 그리고 한국 메모리로의 전이는 ① use-of-proceeds 실제 집행, ② 미팅의 공식 확인, ③ 맞춤형 HBM의 수주화라는 세 관문을 통과해야 한다.

실전 자세는 한 문장이다. <strong>스페이스X를 우주주가 아니라 "AI 컴퓨트 자금조달 + 한국 HBM·메모리·전력 옵션"으로 보되, 단독 보도와 타진 단계를 실적과 분리해 단계별로 확인한다.</strong>

<small>이 글의 사실관계는 본문에 표기한 보도·공시·분석 자료를 인용한 것이다. 스페이스X 상장은 진행 중이며, 최태원·머스크 미팅은 단독 보도(SK "확인 어렵다") 단계이고 맞춤형 HBM은 타진 단계다. 종목명은 투자 추천이 아니라 분석 흐름을 보여주는 예시이며, 실제 투자 판단과 책임은 투자자 본인에게 있다.</small>

## Sources

[1]: https://www.cnbc.com/2026/05/20/spacex-ipo-live-updates.html "SpaceX's historic IPO plans: Billions in losses and Musk's massive ownership — CNBC"
[2]: https://kraneshares.com/spacex-ipo-5-key-takeaways-from-the-s-1-filing-and-how-to-get-exposure-today-with-agix/ "SpaceX IPO: 5 Key Takeaways From the S-1 Filing — KraneShares"
[3]: https://www.satellitetoday.com/finance/2026/06/03/assessing-spacex-finances-addressable-market-and-the-ai-pitch-ahead-of-ipo/ "Assessing SpaceX Finances, Addressable Market, and the AI Pitch Ahead of IPO — Via Satellite"
[4]: https://www.morningstar.com/stocks/6-charts-spacexs-s-1-financials "6 Charts on SpaceX's Pre-IPO Financials — Morningstar"
[5]: https://www.datacenterdynamics.com/en/news/spacex-ipo-musks-firm-set-to-launch-first-orbital-data-center-ai1-satellites-in-2027-will-put-compute-on-starlink-craft/ "SpaceX set to launch first 'orbital data center' AI1 satellites in 2027 — DCD"
[6]: https://www.ddaily.co.kr/page/view/2026061815040502328 "최태원·머스크 회동 예정: 전사적 반도체·AI 인프라 협력 — 디지털데일리"
