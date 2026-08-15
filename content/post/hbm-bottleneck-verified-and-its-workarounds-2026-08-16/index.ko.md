---
title: "AI의 병목은 GPU가 아니라 HBM이 맞다: 다만 병목은 우회를 부른다"
slug: "hbm-bottleneck-verified-and-its-workarounds-2026-08-16"
date: 2026-08-16T14:30:00+09:00
description: "AI의 병목이 GPU에서 HBM으로 옮겨왔다는 명제를 검증했다. 모건스탠리의 리포트는 병목이 칩에서 전력, 메모리, 네트워킹, 냉각으로 이동한다는 프레임을 제시했고, 시중에 도는 2027년 HBM 수요 약 500억 Gb라는 수치는 그 문서가 아니라 국내 증권사와 리서치 종합에서 나온 것인데 세 갈래 추정이 같은 자리에서 수렴한다. 명제의 몸통은 단단하다. 연산은 세대마다 서너 배 늘고 대역폭은 그보다 느리게 늘며, 에이전트 추론은 KV 캐시로 메모리를 점유하고, HBM은 비트당 웨이퍼를 세 배 먹으면서 16단 수율이 절반 아래로 떨어지는 물건이라 2027년 공급은 사실상 물리적으로 잠겼다. 그런데 같은 계산이 구매자도 움직인다. 엔비디아는 메모리 원가가 시스템의 29%에 이르자 모듈 용량을 절반으로 줄였고, 차기 플래그십의 HBM 사양을 전 세대 아래로 낮추는 방안이 보도되며, 프리필 전용 칩은 HBM을 아예 쓰지 않는다. 병목의 실재와 병목이 부르는 우회를 함께 놓고, 그 사이에서 한국 메모리의 이익이 어떻게 결정되는지 정리한다."
categories: ["Exclusive Analysis", "Korea-Semiconductor", "Macro-Analysis"]
tags:
  - "HBM"
  - "메모리 월"
  - "엔비디아"
  - "SK하이닉스"
  - "삼성전자"
  - "마이크론"
  - "KV 캐시"
  - "AI 에이전트"
  - "모건스탠리"
  - "HBM4"
  - "한국 반도체"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> 연결 맥락: 이 시리즈는 8월 들어 메모리 가격의 감속, 수요 확인과 주가의 괴리, 반등의 조건을 차례로 다뤘다. 이 글은 그 아래에 있는 물리적 토대를 검증한다. AI의 병목이 GPU에서 HBM으로 옮겨왔다는 명제가 어디까지 사실이고, 그 병목이 공급자에게 어떤 이익을 얼마나 오래 보장하는지, 그리고 병목 그 자체가 만들어내는 반대 방향의 힘은 무엇인지다.

## TL;DR

- 명제의 출처부터 정리한다. 모건스탠리의 6월 리포트는 <strong>"병목은 공급망을 따라 이동한다. 처음엔 칩, 다음 전력, 다음 메모리, 다음 네트워킹, 다음 냉각"</strong>이라는 프레임과 "메모리는 2026년 말까지 공급 부족"이라는 판단을 담았다. [Fact: 모건스탠리, 6월 9일] 다만 함께 인용되곤 하는 <strong>2027년 HBM 수요 약 500억 Gb는 이 문서에 없는 숫자</strong>다. 실제 출처는 키움증권(534억 Gb)과 국내 리서치 종합(6.20엑사바이트, 환산 약 496억 Gb)이고, 트렌드포스의 비트 점유율 전망으로 역산해도 같은 자리가 나온다. 세 갈래가 수렴하므로 숫자는 쓸 만하되 귀속은 바로잡아야 한다.
- 병목의 첫 번째 근거는 연산과 대역폭의 속도 차이다. GPU 한 장의 연산은 세대마다 서너 배씩 늘었는데 HBM 용량은 <strong>GB300과 차기 루빈이 똑같이 288GB</strong>다. 늘어난 것은 대역폭(8에서 20테라바이트급)인데 그마저 연산 증가율(약 3.5배)에 못 미친다. [Fact: 엔비디아 사양·세미어낼리시스] 칩을 더 사도 메모리가 안 따라오면 연산은 대기한다.
- 두 번째 근거는 추론의 성격 변화다. 에이전트가 긴 컨텍스트를 들고 장시간 작업하면 <strong>KV 캐시라는 중간 기억이 세션 내내 메모리를 점유</strong>한다. 캐시에 있는 토큰과 없는 토큰의 처리 원가가 10배 갈린다는 실무 데이터가 있고, 엔비디아가 올해 초 캐시 전용 저장 계층을 별도 제품으로 내놓았을 정도다. [Fact: 업계 자료] 다만 에이전트가 HBM 수요를 몇 기가바이트 늘리는지의 정량 추정은 아직 공개된 것이 없다. [Blocked: 공개 추정 부재]
- 세 번째 근거는 공급의 산수다. HBM은 같은 용량을 만드는 데 <strong>일반 D램의 약 3배 웨이퍼</strong>를 쓰고, 다이 하나의 수율이 95%여도 8단 적층 누적 수율은 66%, 16단은 44%로 떨어진다. 팹은 착공에서 양산까지 3년에서 5년, 신규 캐파의 본격 기여는 2028년이다. [Fact: 업계 자료·트렌드포스] 그래서 2027년의 타이트함은 전망이 아니라 물리에 가깝다. 마이크론은 데이터센터 수요의 절반도 못 채운다며 <strong>"2027년은 2026년보다 더 타이트할 것"</strong>이라 했고, 곽노정 SK하이닉스 대표이사는 2027년을 공급 관점에서 업계 역사상 가장 타이트한 해로 표현했다. [Fact: 각사 발언]
- 그런데 같은 계산이 구매자도 움직인다. 엔비디아는 메모리 원가가 시스템 원가의 29%에 이르자 <strong>베라 루빈의 CPU측 메모리 모듈을 절반으로 줄였고</strong>, 루빈 울트라의 HBM을 전 세대(288GB)보다 낮은 192GB로 조정하는 방안이 보도됐으며, 프리필 전용 칩(루빈 CPX)은 HBM 대신 GDDR7을 쓴다. 샌디스크와 SK하이닉스가 표준화한 고대역폭 플래시는 HBM 아래에 값싼 용량 계층을 만드는 기술이다. [Fact: 트렌드포스·각사 발표] <strong>병목이 깊을수록 우회의 보상이 커진다.</strong>
- 병목의 이익이 어디로 가는지는 계약이 정한다. 마이크론은 전략 고객 16곳과 2030년경까지 매출의 절반을 계약으로 묶었고, 2027년 HBM 계약가는 "여러 배" 상승이 거론되며, 고객별 맞춤 베이스 다이(커스텀 HBM)는 공급자와 고객을 서로 잠근다. [Fact: 각사·트렌드포스] 지대는 현물 폭등이 아니라 다년 계약의 형태로 고정되는 중이다.
- 한국 시사점. 3사 과점 중 둘이 한국이고 SK하이닉스의 HBM 점유율은 50%대 중후반이다. 2027년까지의 이익 가시성은 병목의 물리학이 뒷받침한다. 열려 있는 것은 2028년이다. 신규 캐파가 그해에 착륙하고, 창신메모리의 HBM도 수율 문제를 안은 채 그 무렵 들어온다. 위에서 본 우회 기술들의 효과가 누적되는 시점도 그때다. 병목 명제는 맞다. 다만 그것은 <strong>2027년까지의 명제</strong>이고, 그 너머는 계약 구조와 공급 규율의 문제로 돌아간다.

<div class="thesis-callout">
<div class="thesis-callout__label">핵심 문장</div>

AI의 병목이 GPU에서 HBM으로 옮겨왔다는 진단은 검증을 통과한다. 연산과 대역폭의 격차, 에이전트 추론의 메모리 점유, 3배의 웨이퍼와 절반의 수율, 3년의 리드타임이 전부 실측이다. 그러나 병목은 정지 화면이 아니다. 메모리가 시스템 원가의 3할에 이르자 가장 큰 구매자가 설계에서 메모리를 덜어내기 시작했고, 병목의 소유자들 스스로 다년 계약으로 가격을 고정해 다음 하강기의 진폭을 줄이고 있다. 병목에서 나오는 이익은 실재하되, 그 크기는 시장가격이 아니라 계약 조항이 정하고, 그 수명은 2028년 공급 도착 전까지다. 투자자가 물어야 할 것은 병목이 있느냐가 아니라, 병목의 지대가 누구 장부에 어떤 형태로 잡히느냐다.

</div>

## 1. 명제와 숫자의 출처부터

모건스탠리 자산운용의 6월 리포트 "Big Picture: 인공지능, 열 가지 투자 진실"은 이 명제의 원전으로 인용되는 문서다. 문서의 실제 주장은 이렇다. AI 인프라의 병목은 한 자리에 머물지 않고 공급망을 따라 이동한다. 처음에는 칩이었고, 다음이 전력, 지금이 메모리이며, 다음은 네트워킹과 냉각이다. 메모리는 2026년 말까지 공급 부족이고, 2027년 증분 메모리 수요는 75에서 100엑사바이트로 2028년에 다시 두 배가 된다. 에이전트 AI는 원래의 대화형 모델 대비 약 100만 배의 컴퓨트를 요구하고, 토큰 소비는 2025년 한 해에만 10배 넘게 늘었다. [Fact: 모건스탠리, 2026년 6월 9일]

여기서 바로잡을 것이 하나 있다. 이 리포트와 함께 널리 인용되는 "2027년 AI 관련 HBM 수요 약 500억 Gb"라는 수치는 <strong>이 문서에 없다</strong>. 문서에는 HBM 고유의 수치도, 공급 3사의 이름도 등장하지 않는다. 이 숫자의 실제 출처를 추적하면 두 갈래가 나온다. 키움증권은 2027년 HBM 수요를 534억 Gb로 추정하며 전년 대비 56% 증가를 전망했고, 트렌드포스와 매킨지 등을 종합한 국내 리서치는 6.20엑사바이트, 기가비트로 환산하면 약 496억 Gb를 제시했다. [Fact: 키움증권·VLSI리서치코리아]

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="240.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">0</text>
<line x1="60" y1="196.8" x2="676.0" y2="196.8" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="200.8" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">120</text>
<line x1="60" y1="157.6" x2="676.0" y2="157.6" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="161.6" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">239</text>
<line x1="60" y1="118.4" x2="676.0" y2="118.4" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="122.4" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">359</text>
<line x1="60" y1="79.2" x2="676.0" y2="79.2" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="83.2" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">478</text>
<line x1="60" y1="40.0" x2="676.0" y2="40.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="44.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">598</text>
<rect x="111.3" y="61.0" width="102.7" height="175.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="162.7" y="53.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">534</text>
<text x="162.7" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">키움증권</text>
<text x="162.7" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">+56% 전망</text>
<rect x="316.7" y="73.5" width="102.7" height="162.5" rx="4" fill="var(--kii-cat-1)"/>
<text x="368.0" y="65.5" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">496</text>
<text x="368.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">리서치 종합</text>
<text x="368.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">6.20EB 환산</text>
<rect x="522.0" y="72.1" width="102.7" height="163.9" rx="4" fill="var(--kii-cat-3)"/>
<text x="573.3" y="64.1" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">500</text>
<text x="573.3" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">비중 역산(자체)</text>
<text x="573.3" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">비트 13% 가정</text>
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="60" y="24" fill="var(--card-text-color-tertiary)" font-size="11.5">2027년 HBM 수요 추정(억 Gb). 방법이 다른 세 추정이 같은 자리에 온다</text>
</svg>
</div>
<figcaption><strong>500억 Gb의 세 갈래 검증.</strong> 키움증권의 추정, 트렌드포스·매킨지 등을 종합한 리서치의 환산치, 그리고 비트 점유율 13%로 푼 자체 역산이 같은 자리에서 만난다. 이 수치는 모건스탠리 문서에는 없다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 경로 | 2027년 HBM 수요 | 방법 |
|---|---|---|
| 키움증권 | 534억 Gb | 전년 대비 +56% 전망 |
| 국내 리서치 종합 | 약 496억 Gb | 6.20엑사바이트 환산 |
| 자체 역산 | 약 500억 Gb | 트렌드포스 비트 점유율 13% 가정 |

</details>
</figure>

숫자 자체는 튼튼하다. 서로 다른 방법을 쓴 두 추정이 500억 Gb 부근에서 수렴하고, 세 번째 경로로도 검증된다. 트렌드포스는 2027년 HBM이 전체 D램 비트 공급의 약 13%가 된다고 보는데, 500억 Gb가 13%라면 전체 D램은 약 3,800억에서 4,400억 Gb라는 계산이 나오고 이는 업계의 통상적인 규모 추정과 맞는다. [Inference: 자체 역산] 결론은 이렇다. 숫자는 쓸 만하다. 다만 출처는 모건스탠리가 아니라 국내 증권사와 리서치 종합이며, 인용할 때는 그렇게 인용해야 한다.

## 2. 왜 GPU가 아니라 HBM인가: 속도의 격차

병목 명제의 첫 번째 토대는 연산과 메모리의 증가 속도 차이다. GPU 세대별 사양을 나란히 놓으면 격차가 그대로 보인다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="240.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">0</text>
<line x1="60" y1="196.8" x2="676.0" y2="196.8" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="200.8" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">4.48</text>
<line x1="60" y1="157.6" x2="676.0" y2="157.6" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="161.6" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">8.96</text>
<line x1="60" y1="118.4" x2="676.0" y2="118.4" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="122.4" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">13.44</text>
<line x1="60" y1="79.2" x2="676.0" y2="79.2" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="83.2" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">17.92</text>
<line x1="60" y1="40.0" x2="676.0" y2="40.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="44.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">22.4</text>
<rect x="98.5" y="206.7" width="77.0" height="29.3" rx="4" fill="var(--kii-cat-1)"/>
<text x="137.0" y="198.7" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">3.35</text>
<text x="137.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">H100</text>
<text x="137.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">HBM 80GB</text>
<rect x="252.5" y="166.0" width="77.0" height="70.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="291.0" y="158.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">8</text>
<text x="291.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">B200</text>
<text x="291.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">HBM 192GB</text>
<rect x="406.5" y="166.0" width="77.0" height="70.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="445.0" y="158.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">8</text>
<text x="445.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">GB300</text>
<text x="445.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">HBM 288GB</text>
<rect x="560.5" y="61.0" width="77.0" height="175.0" rx="4" fill="var(--kii-cat-3)"/>
<text x="599.0" y="53.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">20</text>
<text x="599.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">베라 루빈</text>
<text x="599.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">HBM 288GB, 용량 동결</text>
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="60" y="24" fill="var(--card-text-color-tertiary)" font-size="11.5">GPU당 HBM 대역폭(TB/s). 루빈은 목표 22, 초기 출하 약 20 보도</text>
</svg>
</div>
<figcaption><strong>연산은 뛰고 용량은 멈췄다.</strong> GB300과 베라 루빈의 HBM 용량은 288GB로 같다. 세대 교체의 증분은 대역폭이고, 그마저 같은 기간 연산 증가율(약 3.5배)에 못 미치는 약 2.75배다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| GPU | HBM 용량 | 대역폭 |
|---|---|---|
| H100 | 80GB | 3.35TB/s |
| B200 | 192GB | 약 8TB/s |
| GB300 | 288GB | 약 8TB/s |
| 베라 루빈 | 288GB | 목표 22, 초기 약 20TB/s 보도 |

</details>
</figure>

H100의 HBM은 80GB에 초당 3.35테라바이트였다. B200에서 192GB에 8테라바이트가 됐고, GB300에서 용량이 288GB로 올라섰다. 그런데 차기 베라 루빈의 HBM4도 <strong>용량은 똑같이 288GB</strong>다. 늘어난 것은 대역폭으로, 목표 기준 초당 22테라바이트, 실제 초기 출하는 20테라바이트 수준으로 보도된다. GB300 대비 약 2.75배다. 같은 기간 GPU의 연산 성능은 약 3.5배 늘었다. [Fact: 엔비디아 사양, 세미어낼리시스 분석, 보도] 연산이 대역폭보다 빨리 늘어나는 구조가 세대를 거듭하며 반복되고 있고, 이것이 메모리 월이라 불리는 현상의 실체다.

이 격차가 실제 비용으로 나타나는 곳이 추론이다. 추론은 두 단계로 나뉜다. 프롬프트 전체를 한 번에 처리하는 프리필 단계는 연산 집약적이라 GPU의 연산 성능이 병목이다. 그러나 토큰을 하나씩 생성하는 디코드 단계는 매 토큰마다 모델 가중치와 중간 기억 전체를 메모리에서 다시 읽어야 해서 <strong>연산이 아니라 메모리 대역폭이 병목</strong>이 된다. 이 단계에서 GPU는 상당 시간을 메모리를 기다리며 논다. 비싼 칩을 더 사도 HBM이 안 따라오면 처리량이 늘지 않는 이유가 여기에 있다.

## 3. 에이전트가 바꾸는 것: 기억의 상주

두 번째 토대는 워크로드의 변화다. 질문 하나에 답 하나를 내는 챗봇과 달리, 에이전트는 웹을 검색하고 코드를 짜고 테스트하고 고치는 작업을 수십 분에서 수 시간 단위로 수행한다. 이때 모델이 지금까지의 맥락을 기억하기 위해 유지하는 것이 KV 캐시라는 중간 기억이고, 이 캐시는 컨텍스트가 길수록, 세션이 오래갈수록, 동시에 도는 에이전트가 많을수록 커진다. 에이전트 하나의 작업이 라우팅, 검색, 도구 선택, 검증 같은 여러 모델 호출로 갈라지고 각 호출이 캐시를 들고 있는 구조라, 동시 상주 메모리가 대화형 시절과 다른 차원으로 늘어난다.

이 변화는 이미 가격표에 나타나 있다. 캐시에 있는 입력 토큰과 없는 토큰의 처리 단가는 실무에서 10배 차이가 난다는 집계가 있고, 서버 한 대의 D램 한도(통상 1에서 2테라바이트) 때문에 캐시를 한 시간 이상 유지하기 어렵다는 운영 데이터도 있다. 엔비디아가 올해 1월 KV 캐시 전용 저장 계층(CMX)을 별도 제품군으로 내놓은 것 자체가, 이 문제가 하드웨어 제품이 될 만큼 커졌다는 증거다. [Fact: 업계 자료·엔비디아 발표] 트렌드포스는 에이전트 확산으로 서버의 CPU 대 GPU 구성비가 바뀌고 기업 에이전트가 종전의 최대 4배 토큰을 소비한다며, 2027년 글로벌 메모리 시장을 1조2,800억달러로 전망했다. [Fact: 트렌드포스, 5월 29일]

정직한 공백도 적어 둔다. 에이전트 워크로드가 HBM 수요를 정확히 몇 엑사바이트 늘리는지에 대한 공개된 정량 추정은 아직 없다. [Blocked: 공개 추정 부재] 방향은 분명하되 크기는 아직 서사의 영역이다.

## 4. 왜 셋뿐인가: 공급의 산수

세 번째 토대는 공급이 늘기 어려운 구조다. 숫자 셋이 그 구조를 요약한다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="240.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">0%</text>
<line x1="60" y1="196.8" x2="676.0" y2="196.8" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="200.8" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">21%</text>
<line x1="60" y1="157.6" x2="676.0" y2="157.6" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="161.6" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">43%</text>
<line x1="60" y1="118.4" x2="676.0" y2="118.4" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="122.4" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">64%</text>
<line x1="60" y1="79.2" x2="676.0" y2="79.2" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="83.2" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">85%</text>
<line x1="60" y1="40.0" x2="676.0" y2="40.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="44.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">106%</text>
<rect x="111.3" y="61.0" width="102.7" height="175.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="162.7" y="53.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">95%</text>
<text x="162.7" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">다이 하나</text>
<text x="162.7" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">가정 95%</text>
<rect x="316.7" y="114.4" width="102.7" height="121.6" rx="4" fill="var(--kii-cat-3)"/>
<text x="368.0" y="106.4" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">66%</text>
<text x="368.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">8단 적층</text>
<text x="368.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">0.95의 8제곱</text>
<rect x="522.0" y="154.9" width="102.7" height="81.1" rx="4" fill="var(--kii-cat-4)"/>
<text x="573.3" y="146.9" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">44%</text>
<text x="573.3" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">16단 적층</text>
<text x="573.3" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">0.95의 16제곱</text>
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="60" y="24" fill="var(--card-text-color-tertiary)" font-size="11.5">누적 수율(%). 다이 수율 95% 가정의 예시 계산</text>
</svg>
</div>
<figcaption><strong>적층 수율의 산수.</strong> 다이 하나가 95%여도 8단이면 66%, 16단이면 44%다. 다이 하나에 8,000개가 넘는 수직 배선 중 하나만 불량이어도 스택 전체가 버려진다. 이 산수가 3사 과점과 비트당 3배 웨이퍼 소모의 원인이다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 구성 | 누적 수율 | 계산 |
|---|---|---|
| 다이 하나 | 95% | 가정 |
| 8단 적층 | 약 66% | 0.95의 8제곱 |
| 16단 적층 | 약 44% | 0.95의 16제곱 |

</details>
</figure>

같은 용량을 만들 때 HBM은 일반 서버 D램의 약 3배 웨이퍼를 소모한다. 다이가 크고, 적층을 위한 수직 배선(TSV)이 면적을 차지하며, 수율 손실이 겹치기 때문이다. 수율의 산수는 가혹하다. 다이 하나의 수율이 95%라 해도 8단을 쌓으면 누적 수율이 66%, 16단이면 44%로 떨어진다. 다이 하나에 8,000개가 넘는 수직 배선 중 하나만 불량이어도 스택 전체가 죽는다. [Fact: 업계 기술 자료] 이 장벽이 HBM을 3사 과점으로 만들었고, 옴디아는 HBM이 표준 D램보다 훨씬 복잡해 양산 가능한 회사가 셋뿐이며 병목이 최소 2027년까지 간다고 정리했다. [Fact: 옴디아, 7월 30일]

시간의 장벽이 그 위에 얹힌다. 팹은 착공에서 양산까지 3년에서 5년이 걸리고, 노광 장비의 리드타임만 1년에서 1년 반이다. 인증도 시간을 먹는다. 삼성전자의 HBM3E 12단이 엔비디아 인증을 통과하는 데 약 18개월이 걸렸고 그 사이 블랙웰 사이클이 지나갔다. [Fact: 업계 자료] 그래서 지금 공사 중인 캐파(SK하이닉스 청주 M15X 2027년 중반, 삼성 평택 P5 2028년)가 물량으로 기여하는 것은 빨라야 2028년이다. 트렌드포스의 수급 전망도 같은 방향이다. D램 충족률은 2026년 마이너스 1에서 2%이고 2027년에 격차가 더 벌어지며, 의미 있는 신규 공급은 2028년에야 온다. [Fact: 트렌드포스]

그 결과가 지금 공급자들의 발언이다. 마이크론의 최고사업책임자는 8월 10일 데이터센터 고객 수요의 절반도 채우지 못한다며 <strong>"2027년은 2026년보다 더 타이트할 것"</strong>이라고 말했고, 곽노정 SK하이닉스 대표이사는 2027년을 공급 관점에서 업계 역사상 가장 타이트한 해로 표현했다. [Fact: 트렌드포스 전언·보도] HBM 캐파는 D램 웨이퍼 투입의 18%(2025년 말)에서 30%(2027년 말)로 늘어나는데, 비트 기준으로는 8%에서 13%가 될 뿐이다. 웨이퍼를 3배 먹는 구조가 여기서도 확인된다. [Fact: 트렌드포스]

여기까지가 병목 명제의 몸통이다. 속도의 격차, 기억의 상주, 공급의 산수. 셋 다 실측이고, 2027년까지의 타이트함은 전망이라기보다 물리에 가깝다.

## 5. 병목이 부르는 우회

그런데 이 명제에는 나머지 절반이 있다. 병목이 깊어질수록, 병목을 피해 가는 설계의 보상도 커진다. 지난 한 달 사이 그 우회가 실측으로 쌓였다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 326" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="132" y1="20" x2="132" y2="282" stroke="var(--kii-chart-axis)" stroke-width="1.5"/>
<text x="116" y="30" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">1월</text>
<circle cx="132" cy="26" r="6" fill="var(--kii-cat-1)"/>
<circle cx="132" cy="26" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="30" fill="var(--card-text-color-main)" font-size="13" font-weight="600">엔비디아 CMX 발표</text>
<text x="152" y="48" fill="var(--card-text-color-tertiary)" font-size="11.5">KV 캐시 전용 저장 계층이 별도 제품이 됐다</text>
<text x="116" y="84" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">로드맵</text>
<circle cx="132" cy="80" r="6" fill="var(--kii-cat-1)"/>
<circle cx="132" cy="80" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="84" fill="var(--card-text-color-main)" font-size="13" font-weight="600">루빈 CPX는 GDDR7</text>
<text x="152" y="102" fill="var(--card-text-color-tertiary)" font-size="11.5">프리필 전용 칩은 HBM을 쓰지 않는 설계</text>
<text x="116" y="138" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">7월 28일</text>
<circle cx="132" cy="134" r="6" fill="var(--kii-cat-3)"/>
<circle cx="132" cy="134" r="9" fill="none" stroke="var(--kii-cat-3)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="138" fill="var(--card-text-color-main)" font-size="13" font-weight="600">SOCAMM 절반 축소 보도</text>
<text x="152" y="156" fill="var(--card-text-color-tertiary)" font-size="11.5">메모리가 시스템 원가 29%에 이르자 모듈을 반으로</text>
<text x="116" y="192" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">8월 3일</text>
<circle cx="132" cy="188" r="6" fill="var(--kii-cat-3)"/>
<circle cx="132" cy="188" r="9" fill="none" stroke="var(--kii-cat-3)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="192" fill="var(--card-text-color-main)" font-size="13" font-weight="600">고대역폭 플래시 표준 공개</text>
<text x="152" y="210" fill="var(--card-text-color-tertiary)" font-size="11.5">샌디스크·SK하이닉스, 컨소시엄에 구글</text>
<text x="116" y="246" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">8월 초</text>
<circle cx="132" cy="242" r="6" fill="var(--kii-cat-4)"/>
<circle cx="132" cy="242" r="9" fill="none" stroke="var(--kii-cat-4)" stroke-opacity="0.32" stroke-width="2"/>
<text x="152" y="246" fill="var(--card-text-color-main)" font-size="13" font-weight="600">루빈 울트라 192GB 조정 보도</text>
<text x="152" y="264" fill="var(--card-text-color-tertiary)" font-size="11.5">차기 플래그십의 HBM이 전 세대보다 줄어드는 방안</text>
</svg>
</div>
<figcaption><strong>우회의 축적.</strong> 올해 들어 확인된 흐름만 다섯이다. 캐시 전용 저장 계층, HBM 없는 프리필 칩, 모듈 절반 축소, 플래시 기반 용량 계층, 플래그십의 HBM 하향 검토. 가격이 유발한 설계 변화는 가격이 내려도 돌아오지 않는다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 시점 | 사건 | 성격 |
|---|---|---|
| 1월 | 엔비디아 CMX 발표 | KV 캐시를 HBM 밖 계층으로 |
| 로드맵 | 루빈 CPX, GDDR7 채택 | 프리필에서 HBM 제거 |
| 7월 28일 | SOCAMM 절반 축소 보도 | CPU측 메모리 감축 |
| 8월 3일 | 고대역폭 플래시 표준 | HBM 아래 용량 계층 |
| 8월 초 | 루빈 울트라 192GB 보도 | 플래그십 HBM 하향 검토 |

</details>
</figure>

엔비디아에서 나온 신호가 가장 무겁다. 메모리 원가가 베라 루빈 시스템 원가의 29%까지 올라 회사가 선호하는 20% 상한을 넘자, CPU측 메모리 모듈(SOCAMM) 용량을 192GB에서 96GB로 절반 줄이는 방향이 보도됐다. 랙 하나의 CPU측 메모리가 55테라바이트에서 28테라바이트로 준다. 공급 배분도 이유다. 3사를 합쳐도 엔비디아가 추정 수요의 60% 정도만 받을 수 있어, 사양을 낮추면 같은 배분으로 더 많은 시스템을 출하할 수 있다. [Fact: 트렌드포스, 7월 28일] 루빈 울트라는 더 나갔다. 당초 1테라바이트 HBM4E로 발표됐던 사양이 단계적으로 내려와, 주력 구성을 <strong>현행 루빈(288GB)보다도 낮은 HBM4 192GB로 조정하는 방안</strong>이 보도됐다. 세대가 올라가는데 메모리 탑재가 줄어드는, 플래그십에서 처음 보는 방향이다. [Fact: 보도, 엔비디아 미확인]

우회는 사양 축소만이 아니다. 프리필 단계 전용으로 설계된 루빈 CPX는 HBM을 아예 쓰지 않고 GDDR7을 쓴다. 연산 병목인 프리필과 메모리 병목인 디코드를 하드웨어 차원에서 분리해, HBM이 필요 없는 곳에서는 HBM 값을 치르지 않겠다는 설계다. 샌디스크와 SK하이닉스가 8월 초 표준 사양을 공개한 고대역폭 플래시(HBF)는 낸드를 적층해 최대 512GB 용량에 HBM급 하단 대역폭을 내는 기술로, 컨소시엄에 구글이 들어 있다. HBM 아래에 값싼 용량 계층을 까는 것이다. 소프트웨어 쪽에서는 KV 캐시 자체를 압축하는 기법이 상용 모델에 들어갔다. 딥시크 계열이 쓰는 어텐션 구조는 토큰당 캐시를 기존 방식의 3분의 1에서 5분의 1로 줄인다. 아직 중국계 모델 중심이지만, 방향은 분명하다. [Fact: 각사 발표·기술 문헌]

이 목록에 공급자의 육성을 겹치면 그림이 완성된다. 최태원 SK하이닉스 체어맨은 지난주 CNBC 인터뷰에서 수요를 전쟁에 비유하면서도 <strong>가격이 너무 빨리 올랐다</strong>고 말했다. 병목의 최대 수혜자가 병목의 깊이를 걱정하는 이유는 위의 목록 때문이다. 가격이 유발하는 우회는 한 번 설계에 들어가면 가격이 내려도 돌아오지 않는다.

## 6. 병목의 지대는 어디로 가나

병목이 실재하고 우회가 자란다면, 남는 질문은 병목의 이익이 누구에게 어떤 형태로 귀속되느냐다. 답은 점점 계약이 되고 있다.

수요 쪽은 다년 계약으로 물량을 잠근다. 마이크론은 전략 고객 16곳과 2030년경까지 매출의 약 절반을 계약으로 묶었고, 3사의 2027년 캐파가 사실상 배정 완료 상태라는 보도가 이어진다. 2027년 HBM 계약가는 "여러 배" 상승이 거론되는데, 트렌드포스 원문의 표현은 배수를 특정하지 않는 정성적 서술이라 그 이상으로 옮기면 과잉이다. [Fact: 각사·트렌드포스] 가격 쪽은 커스텀화가 구조를 바꾼다. HBM4부터 베이스 다이가 TSMC의 로직 공정(주력 12나노, 프리미엄 5나노, 차세대 3나노)으로 넘어가고 엔비디아와 구글이 각자 맞춤 사양을 요구하면서, HBM은 범용 부품에서 고객별 비호환 부품으로 바뀌는 중이다. 맞춤 베이스 다이는 공급자를 갈아타기 어렵게 만드는 동시에 공급자도 그 고객에 묶는다. [Fact: 업계 자료]

이 구조의 의미는 시리즈에서 다뤄 온 결론과 같다. 병목의 지대는 현물 가격의 폭등이 아니라 <strong>다년 계약의 조항으로 고정</strong>되고 있다. 고정된 지대는 상승기의 상방을 깎는 대신 하강기의 하방을 막는다. HBM 시장 규모 전망이 기관마다 크게 갈리는 것(2027년 기준 1,160억달러에서 원화 260조원까지)도 이 전환기의 특징이라, 특정 수치보다 계약 커버리지의 비율을 보는 것이 낫다. [Fact: 각 기관, 편차 큼]

## 7. 한국 시사점: 2027의 물리학, 2028의 달력

한국 메모리에 이 검증이 뜻하는 바를 정리한다.

병목의 소유가 한국의 위치다. 양산 가능한 3사 중 둘이 한국 회사이고, SK하이닉스의 HBM 점유율은 소스에 따라 50%대 중반에서 후반이다. 엔비디아 차기 플랫폼의 초기 HBM4 물량에서 SK하이닉스가 약 70%를 가져간다는 집계도 있다. [Fact: 보도, 점유율은 소스별 편차] 2027년까지의 이익 가시성은 위에서 본 물리학이 뒷받침한다. 리드타임 때문에 2027년 공급은 지금 이 순간 이미 결정돼 있고, 그 물량은 상당 부분 계약으로 팔려 있다.

열려 있는 것은 2028년이다. 신규 팹의 물량 기여가 그해에 시작된다(청주 M15X, 평택 P5). 창신메모리의 HBM 캐파도 계획대로면 그해 10만 장 규모로 올라오는데, 수율 25% 수준과 중국 내수 고객이라는 한계를 안은 채다. 위에서 본 우회 기술들의 효과가 누적되는 시점도 겹친다. [Fact: 각사·세미어낼리시스] 병목 명제는 2027년까지는 물리의 문제지만, 2028년부터는 공급 규율과 계약 조항의 문제로 돌아간다. 이 시리즈가 8월 초에 도달한 결론, 즉 투자 질문은 가격이 더 오르느냐가 아니라 유지되느냐이고 유지는 계약이 보장할 때 가장 단단하다는 판단은, 병목의 물리학을 통과한 뒤에도 그대로 남는다.

마지막으로 모건스탠리 리포트의 문장 하나를 그대로 옮긴다. "인프라가 먼저 온다. 그 건설을 정당화할 애플리케이션은 아직 보이지 않는다." 병목 명제의 가장 강한 지지자조차 이 단서를 달았다. 병목은 수요가 실재할 때만 지대를 낳는다. 수요의 실측은 이번 실적 시즌이 보여줬고, 그 지속은 매 분기 재검증된다.

---

본문에 언급한 종목은 분석을 위한 예시이며 특정 종목의 매수나 매도를 권유하지 않는다. 투자 판단과 그 결과의 책임은 투자자 본인에게 있다. 2027년 HBM 수요 500억 Gb 부근의 수치는 키움증권과 국내 리서치 종합의 추정이며 모건스탠리 문서에는 없고, 전체 D램 대비 비중 역산은 자체 계산이다. GPU 사양과 대역폭은 발표 목표치와 보도를 병기했으며 실제 출하 사양과 다를 수 있다. 수율 수치는 업계 기술 자료의 예시 계산이고 실제 수율은 회사별로 공개되지 않는다. 루빈 울트라 사양 조정과 SOCAMM 축소는 조사기관과 언론 보도로 엔비디아가 확인하지 않았다. HBM 시장 규모 전망은 기관 간 편차가 매우 크다. 에이전트 워크로드의 HBM 수요 기여는 공개된 정량 추정이 없어 방향만 서술했다. 시세와 전망은 2026년 8월 중순 기준이다.

### 관련 포스팅

- [8월 둘째 주 결산: AI 투자금은 월가로 넘어가고, 호재가 이틀을 가기 시작했다](/ko/post/weekly-wrap-wallst-financing-reaction-shift-2026-08-14/)
- [메모리는 이제 가격이 더 오르지 않아도 된다: 8월 3일 급락과 계약가 감속의 해부](/ko/post/memory-price-deceleration-p-holds-thesis-2026-08-03/)
- [하이퍼스케일러 실적이 증명한 것과 증명하지 않은 것: 메모리 매도의 세 가지 설명](/ko/post/hyperscaler-proof-memory-selling-three-hypotheses-2026-08-04/)
- [7월 실적 시즌 총결산: AI 수요는 확인됐고, 메모리 가격이 IT 업계 공통 원가가 됐다](/ko/post/july-2026-earnings-two-listings-kimi-four-worries-2026-07-31/)
