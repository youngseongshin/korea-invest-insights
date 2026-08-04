---
title: "하이퍼스케일러 실적이 증명한 것과 증명하지 않은 것: 메모리 매도의 세 가지 설명"
slug: "hyperscaler-proof-memory-selling-three-hypotheses-2026-08-04"
date: 2026-08-04T18:50:00+09:00
description: "마이크로소프트와 아마존은 AI 자본지출이 실제 매출과 이익으로 전환된다는 것을 처음으로 설득력 있게 보여줬다. 애저는 43% 성장하며 연간 1,000억달러를 넘었고, AWS는 36.7% 성장에 영업이익률 39.4%를 냈으며, 마이크로소프트 수주잔고 순증 510억달러는 전부 프런티어 모델 기업 바깥에서 나왔다. 그런데 같은 기간 외국인은 삼성전자와 SK하이닉스만 11조원 넘게 팔면서 나머지 한국 주식은 순매수했다. 수요가 증명됐는데 왜 메모리는 팔렸나. 시차, 가격 체제, 공급 도착이라는 세 가설을 세워 각각 채점한다. 그리고 엔비디아가 메모리 원가 때문에 베라 루빈의 모듈 용량을 절반으로 줄이고 있다는 사실이 이 채점을 어떻게 바꾸는지 살핀다."
categories: ["Exclusive Analysis", "Market-Outlook", "Korea-Semiconductor"]
tags:
  - "마이크로소프트"
  - "아마존"
  - "엔비디아"
  - "루빈"
  - "HBM"
  - "삼성전자"
  - "SK하이닉스"
  - "외국인 수급"
  - "디레버리징"
  - "창신메모리"
  - "한국 반도체"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> 연결 맥락: [8월 3일 급락과 계약가 감속](/ko/post/memory-price-deceleration-p-holds-thesis-2026-08-03/)에서 메모리 가격의 상승 속도가 꺾였고 투자 질문이 가격 상승에서 가격 유지로 옮겨갔다고 적었다. 이 글은 다른 축을 본다. 같은 주에 마이크로소프트와 아마존이 AI 투자가 실제 매출로 전환된다는 증거를 내놓았는데, 수요가 확인된 그 시점에 외국인은 메모리 2사를 집중적으로 팔았다. 수요 축과 공급 축이 갈라지는 이 지점이 지금 한국 메모리 주가를 설명하는 자리다.

## TL;DR

- 마이크로소프트와 아마존이 바꾼 것은 자본지출이 계속된다는 사실이 아니라 <strong>그 지출이 매출과 이익과 계약잔고로 전환된다는 증거의 강도</strong>다. 애저는 분기 43% 성장했고 회계연도 기준 연간 매출이 처음 1,000억달러를 넘었다(연간 성장률 41%). AWS는 36.7% 성장하며 영업이익률 39.4%를 냈고 영업이익은 64% 늘었다. [Fact: 양사 발표문·어닝콜]
- 가장 강한 한 줄은 마이크로소프트 CFO의 발언이다. 커머셜 수주잔고는 6,780억달러로 84% 늘었는데 <strong>순증 510억달러가 전부 프런티어 모델 기업 바깥의 고객에서 나왔다</strong>. 오픈AI를 제외한 잔고 증가율도 25%다. [Fact: 어닝콜] 잔고가 소수 AI 기업과의 순환계약이라는 의심을 정면으로 낮추는 실측이다.
- 다만 잔고를 현금처럼 읽으면 안 된다. 같은 콜에서 밝혀진 구조는 <strong>가중평균 기간 2.3년, 향후 12개월 내 인식 예정분 약 30%</strong>다. 그 12개월분이 전년 대비 37% 늘었다는 것이 실제로 중요한 숫자다. [Fact: 어닝콜]
- 그런데 수요가 확인된 그 주에 한국 메모리는 팔렸다. 7월 한 달 외국인은 삼성전자와 SK하이닉스에서 11조원 넘게 순매도하면서 <strong>같은 기간 다른 한국 주식은 순매수</strong>했다. LG이노텍을 필두로 반도체 소부장과 자동차를 샀다. [Fact: 언론 종합, 수치는 출처별 편차] 한국을 판 것이 아니라 메모리만 줄인 것이다.
- 여기에 국내 레버리지 청산이 겹쳤다. 신용융자 잔고는 6월 말 38.6조원에서 7월 31일 28.9조원으로 줄었고 그날 하루 감소폭이 사상 최대였다. 단일종목 레버리지 상장지수펀드 순자산은 6월 말 약 16조원에서 7월 30일 약 5.7조원이 됐다. [Fact: 금융투자협회·언론] <strong>7월 31일 외국인 사상 최대 순매수 7.2조원은 그 강제 매물을 받아낸 거래</strong>로 해석된다.
- 수요가 증명됐는데 메모리가 팔린 이유로 세 가설을 세워 채점했다. 시차 가설(확인이 실적에 오기까지 걸리는 시간), 가격 체제 가설(수요가 늘어도 가격 결정권이 이동), 공급 도착 가설(2028년 증설이 겹침)이다. <strong>지금 가격을 지배하는 것은 첫째가 아니라 둘째와 셋째</strong>이고, 그래서 좋은 수요 뉴스만으로는 풀리지 않는다.
- 둘째 가설의 가장 선명한 증거가 이번 주에 나왔다. 엔비디아가 메모리 원가가 시스템 원가의 29%까지 올라 선호 상한 20%를 넘자 <strong>베라 루빈의 모듈 용량을 절반으로 줄이는 중</strong>이다. 랙당 LPDDR5X가 약 55TB에서 약 28TB로 준다. [Fact: 트렌드포스] 가장 강한 수요처조차 가격이 오르면 메모리를 덜 쓰도록 설계를 바꾼다.
- 오늘 코스피는 1.62% 올랐고 삼성전자와 SK하이닉스도 소폭 상승 마감했다. 다만 두 종목은 6월 고점 대비 각각 36%와 47% 낮은 자리에 있다. [Fact: 시장 데이터] 수요 리스크는 내려갔고 공급 리스크는 그대로다. 이 비대칭이 지금 가격의 내용이다.

<div class="thesis-callout">
<div class="thesis-callout__label">핵심 문장</div>

이번 실적이 증명한 것은 AI 투자가 매출로 돌아온다는 사실이고, 증명하지 않은 것은 그 매출 중 얼마가 메모리 회사의 마진으로 남느냐다. 앞의 질문은 마이크로소프트와 아마존의 손익계산서가 답했고, 뒤의 질문은 계약 구조와 2028년 증설이 답한다. 외국인이 메모리만 팔면서 소부장을 산 것은 한국에서 나간 것이 아니라 이 두 질문을 분리해서 가격을 매긴 것이다. 그러므로 수요 확인을 근거로 메모리를 사는 논리는 절반만 맞다. 나머지 절반은 가격 결정권이 어디로 가는지에 달렸다.

</div>

## 1. 무엇이 실제로 증명됐나

두 회사의 숫자부터 놓는다. 마이크로소프트는 회계연도 4분기에 매출 900억달러, 영업이익 406억달러를 냈고 주당순이익은 32% 늘었다. 애저는 분기 43% 성장해 직전 분기 40%에서 가속했고, 회계연도 기준 애저 연간 매출이 처음으로 1,000억달러를 넘었다. 이때 연간 성장률은 41%다. 아마존은 AWS 매출 422억달러로 36.7% 성장했는데 이는 18개 분기 만의 최고 성장률이고, AWS 영업이익은 166억달러로 64% 늘어 영업이익률이 39.4%가 됐다. [Fact: 양사 발표문·어닝콜]

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 212" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="196.0" y1="18" x2="196.0" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="196.0" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">0</text>
<line x1="282.3" y1="18" x2="282.3" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="282.3" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">25</text>
<line x1="368.6" y1="18" x2="368.6" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="368.6" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">50</text>
<line x1="454.9" y1="18" x2="454.9" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="454.9" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">75</text>
<text x="184" y="40.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">애저 매출 성장률</text>
<rect x="196" y="28.0" width="148.5" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="353.5" y="40.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+43.0%</text>
<text x="688.0" y="40.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">직전 분기 40%</text>
<text x="184" y="76.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">AWS 매출 성장률</text>
<rect x="196" y="64.0" width="126.7" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="331.7" y="76.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+36.7%</text>
<text x="688.0" y="76.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">18개 분기 최고</text>
<text x="184" y="112.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">AWS 영업이익 성장률</text>
<rect x="196" y="100.0" width="219.6" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="424.6" y="112.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+63.6%</text>
<text x="688.0" y="112.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">마진 39.4%</text>
<text x="184" y="148.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">MS 수주잔고 성장률</text>
<rect x="196" y="136.0" width="290.0" height="16" rx="4" fill="var(--kii-cat-2)"/>
<text x="495.0" y="148.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+84.0%</text>
<text x="688.0" y="148.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">6,780억달러</text>
<line x1="196" y1="18" x2="196" y2="162.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="360.0" y="204" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">2026년 2분기 전년 대비 성장률(%)</text>
</svg>
</div>
<figcaption><strong>2026년 2분기 성장률.</strong> 애저와 AWS는 매출이 가속했고, AWS는 지출을 늘리는 와중에 영업이익률을 39.4%로 끌어올렸다. 수주잔고 증가율은 다른 축의 지표라 색을 달리했다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 항목 | 전년 대비 |
|---|---|
| 애저 매출 | +43% |
| AWS 매출 | +36.7% |
| AWS 영업이익 | +63.6% |
| 마이크로소프트 커머셜 수주잔고 | +84% |

</details>
</figure>

성장률보다 눈여겨볼 대목은 <strong>지출과 수익이 같은 분기에 함께 움직였다</strong>는 것이다. AWS는 자본지출을 늘리는 와중에 영업이익률을 전년 32.9%에서 39.4%로 끌어올렸다. 투자가 마진을 갉아먹는 국면이 아니라 투자가 마진을 만드는 국면이라는 뜻이다.

계약잔고 쪽이 더 결정적이다. 마이크로소프트의 커머셜 수주잔고는 6,780억달러로 84% 늘었다. 그런데 이 수치보다 중요한 것이 구성이다. 직전 분기 6,270억달러에서 늘어난 510억달러에 대해 CFO는 순차 증가분 전부가 프런티어 모델 기업 바깥 고객의 약정에서 나왔다고 밝혔다. 오픈AI를 제외한 잔고 증가율은 25%, 수주 증가율은 18%다. [Fact: 어닝콜]

이 한 줄이 왜 중요한지는 지난달의 의심을 떠올리면 분명해진다. 잔고가 커 보여도 그 대부분이 오픈AI 한 곳과의 약정이라면 순환 거래에 가깝고, 오픈AI의 자금 사정이 흔들리면 함께 흔들린다. 순증이 전부 그 바깥에서 나왔다는 것은 <strong>수요의 저변이 실제로 넓어졌다</strong>는 뜻이다.

## 2. 계약잔고를 어디까지 믿을 것인가

다만 잔고를 매출과 같은 것으로 읽으면 안 된다. 같은 콜에서 회사가 밝힌 구조가 그 절제를 강제한다. 마이크로소프트 잔고의 가중평균 기간은 2.3년이고, 약 30%가 향후 12개월 내에 매출로 인식될 예정이다. [Fact: 어닝콜]

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 180" xmlns="http://www.w3.org/2000/svg" role="img">
<rect x="40" y="64" width="186.0" height="44" rx="4" fill="var(--kii-cat-1)"/>
<rect x="228.0" y="64" width="432.0" height="44" rx="4" fill="var(--kii-cat-1)" fill-opacity="0.28"/>
<text x="133.0" y="91.0" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">2,034억달러</text>
<text x="444.0" y="91.0" fill="var(--card-text-color-main)" font-size="13" font-weight="600" text-anchor="middle">4,746억달러</text>
<text x="40" y="30" fill="var(--card-text-color-main)" font-size="13.5" font-weight="700">커머셜 수주잔고 6,780억달러</text>
<text x="40" y="50" fill="var(--card-text-color-tertiary)" font-size="11.5">가중평균 기간 2.3년. 약 30%가 12개월 내 매출로 인식</text>
<rect x="40" y="128" width="11" height="11" rx="3" fill="var(--kii-cat-1)"/>
<text x="56" y="138" fill="var(--card-text-color-secondary)" font-size="11.5">12개월 내 인식 예정</text>
<rect x="202" y="128" width="11" height="11" rx="3" fill="var(--kii-cat-1)" fill-opacity="0.28"/>
<text x="218" y="138" fill="var(--card-text-color-secondary)" font-size="11.5">그 이후 인식</text>
</svg>
</div>
<figcaption><strong>수주잔고의 기간 구조.</strong> 6,780억달러 가운데 약 30%만 12개월 안에 매출이 된다. 실제로 볼 숫자는 총액이 아니라 그 12개월분이 전년 대비 37% 늘었다는 사실이다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 구분 | 금액 | 비고 |
|---|---|---|
| 12개월 내 인식 예정 | 약 2,034억달러 | 전년 대비 37% 증가 |
| 그 이후 인식 | 약 4,746억달러 | 가중평균 기간 2.3년 |
| 합계 | 6,780억달러 | 전년 대비 84% 증가 |

</details>
</figure>

6,780억달러 가운데 1년 안에 매출이 되는 것은 2,000억달러 남짓이라는 계산이 나온다. 나머지는 2년에서 3년에 걸쳐 인식된다. 그러므로 잔고 84% 증가를 두고 내년 매출이 84% 는다고 읽으면 틀린다.

실제로 봐야 할 숫자는 따로 있다. <strong>12개월 내 인식 예정분이 전년 대비 37% 늘었다</strong>는 것이다. 이것이 근시일 매출로 전환되는 속도를 보여주는 지표이고, 애저의 실제 성장률 43%와 다음 분기 가이던스 45%가 그 숫자와 정합한다. 잔고와 매출이 따로 노는 것이 아니라 같은 방향으로 움직이고 있다는 확인이다.

자금 부담이 사라진 것은 아니라는 점도 함께 기록한다. 마이크로소프트는 다음 회계연도에도 잉여현금흐름 흑자를 유지할 것으로 예상한다고 밝혔지만, 아마존의 최근 12개월 잉여현금흐름은 마이너스 76억달러로 전년 같은 기간의 플러스 182억달러에서 뒤집혔다. 유형자산 순취득이 1년 사이 661억달러 늘어난 결과다. [Fact: 양사 공시] 같은 사이클에서도 재무 여력은 회사마다 갈린다.

## 3. 그런데 왜 메모리는 팔렸나

수요가 확인된 바로 그 주에 한국 메모리는 팔렸다. 누가 팔았는지는 주체 단위까지 확인된다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 140" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="236.0" y1="18" x2="236.0" y2="90.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="236.0" y="108.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">-10</text>
<line x1="318.5" y1="18" x2="318.5" y2="90.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="318.5" y="108.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">-5</text>
<line x1="401.0" y1="18" x2="401.0" y2="90.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="401.0" y="108.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+0</text>
<line x1="483.5" y1="18" x2="483.5" y2="90.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="483.5" y="108.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+5</text>
<text x="158" y="40.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">메모리 2사</text>
<rect x="214.5" y="28.0" width="186.5" height="16" rx="4" fill="var(--kii-cat-4)"/>
<text x="205.5" y="40.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="end">-11.3</text>
<text x="688.0" y="40.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">삼성전자·SK하이닉스</text>
<text x="158" y="76.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">나머지 코스피</text>
<rect x="401.0" y="64.0" width="41.2" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="451.2" y="76.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+2.5</text>
<text x="688.0" y="76.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">소부장·자동차 등</text>
<line x1="401.0" y1="18" x2="401.0" y2="90.0" stroke="var(--kii-chart-axis)" stroke-width="1.4"/>
<text x="335.0" y="132" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">2026년 7월 외국인 순매수(조원). 역산 포함 근사치</text>
</svg>
</div>
<figcaption><strong>2026년 7월 외국인 순매수.</strong> 메모리 2사만 집중적으로 줄이면서 나머지 한국 주식은 순매수했다. 메모리 2사 수치는 출처별로 11.3조원에서 13.1조원까지 편차가 있고, 나머지 코스피는 역산치다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 구분 | 순매수 | 비고 |
|---|---|---|
| 삼성전자·SK하이닉스 | 약 -11조원 이상 | 출처별 11.3조-13.1조 |
| 나머지 코스피 | 약 +2.5조원 | 역산치 |

</details>
</figure>

7월 한 달 동안 외국인은 삼성전자와 SK하이닉스에서 11조원을 넘게 순매도했다. 출처에 따라 11.3조원에서 13.1조원 사이로 집계가 갈린다. 그런데 같은 기간 코스피 전체 외국인 순매도는 그보다 작았다. 두 종목을 빼면 <strong>외국인은 다른 한국 주식을 순매수했다</strong>는 뜻이다. [Fact: 언론 종합, 수치는 출처별 편차 있음] 실제로 7월 외국인 순매수 상위에는 LG이노텍이 올랐고 DB하이텍, 리노공업, 한미반도체, 삼성전기 같은 반도체 소부장과 현대차, 네이버가 이어졌다.

이 사실이 해석을 좁혀 준다. 외국인은 한국에서 나간 것도 아니고 반도체를 버린 것도 아니다. <strong>메모리 대형주만 줄이고 같은 산업의 다른 자리로 옮겨간 것</strong>이다.

여기에 국내 레버리지 청산이 겹쳤다. 신용융자 잔고는 6월 말 38.6조원에서 7월 31일 28.9조원으로 줄었고, 그날 하루 감소폭은 사상 최대였다. 삼성전자와 SK하이닉스를 추종하는 단일종목 레버리지 상장지수펀드의 순자산은 6월 말 약 16조원에서 7월 30일 약 5.7조원으로 3분의 1 수준이 됐다. 한 달 평균 수익률은 마이너스 47%였다. [Fact: 금융투자협회·언론]

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="240.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">0.0</text>
<line x1="60" y1="196.8" x2="676.0" y2="196.8" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="200.8" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">8.6</text>
<line x1="60" y1="157.6" x2="676.0" y2="157.6" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="161.6" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">17.3</text>
<line x1="60" y1="118.4" x2="676.0" y2="118.4" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="122.4" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">25.9</text>
<line x1="60" y1="79.2" x2="676.0" y2="79.2" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="83.2" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">34.6</text>
<line x1="60" y1="40.0" x2="676.0" y2="40.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="51" y="44.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">43.2</text>
<rect x="98.5" y="61.0" width="77.0" height="175.0" rx="4" fill="var(--kii-cat-3)"/>
<text x="137.0" y="53.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">38.6</text>
<text x="137.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">신용융자 6월말</text>
<text x="137.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">정점</text>
<rect x="252.5" y="105.0" width="77.0" height="131.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="291.0" y="97.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">28.9</text>
<text x="291.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">신용융자 7/31</text>
<text x="291.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">사상 최대 감소</text>
<rect x="406.5" y="163.5" width="77.0" height="72.5" rx="4" fill="var(--kii-cat-3)"/>
<text x="445.0" y="155.5" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">16.0</text>
<text x="445.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">레버리지 ETF 6월말</text>
<text x="445.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">순자산</text>
<rect x="560.5" y="210.2" width="77.0" height="25.8" rx="4" fill="var(--kii-cat-1)"/>
<text x="599.0" y="202.2" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600" text-anchor="middle">5.7</text>
<text x="599.0" y="256.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">레버리지 ETF 7/30</text>
<text x="599.0" y="274.0" fill="var(--card-text-color-tertiary)" font-size="10.5" text-anchor="middle">3분의 1 수준</text>
<line x1="60" y1="236.0" x2="676.0" y2="236.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="60" y="24" fill="var(--card-text-color-tertiary)" font-size="11.5">규모(조원). 신용융자 잔고와 단일종목 레버리지 ETF 순자산</text>
</svg>
</div>
<figcaption><strong>7월의 레버리지 청산.</strong> 신용융자 잔고와 단일종목 레버리지 상장지수펀드 순자산이 한 달 사이 크게 줄었다. 7월 31일 신용융자 하루 감소폭은 사상 최대였다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 구분 | 6월 말 | 7월 말 |
|---|---|---|
| 신용융자 잔고 | 38.6조원 | 28.9조원(7/31) |
| 단일종목 레버리지 ETF 순자산 | 약 16조원 | 약 5.7조원(7/30) |

</details>
</figure>

7월 31일 외국인이 사상 최대인 7조2,000억원을 순매수한 것도 이 맥락에서 읽어야 한다. 국내 증권사들은 이를 강제 청산 물량이 상당 부분 소화된 자리에서 나온 매수로 해석한다. [Inference: 증권사 코멘트 종합] 그리고 8월 3일에 한 차례 더 큰 매도가 나온 뒤, 오늘 코스피는 1.62% 올랐고 삼성전자와 SK하이닉스도 각각 0.21%와 0.64% 오르며 마감했다. 두 종목은 6월 고점 대비 각각 36%와 47% 낮은 자리에 있다. [Fact: 시장 데이터]

## 4. 세 가지 설명과 채점

수요가 확인됐는데 메모리가 팔린 이유를 설명하는 가설은 셋이다. 각각을 놓고 지금 어느 것이 가격을 지배하는지 판단한다.

| 가설 | 내용 | 함의 | 현재 채점 |
|---|---|---|---|
| 시차 | 하이퍼스케일러 이익 가시성이 메모리 계약을 거쳐 실적에 오기까지 두세 분기 걸린다. 시장이 그 사이를 못 기다린다 | 기다리면 해소되므로 지금이 기회 | 부분적으로 참. 다만 이것만으로는 소부장을 사면서 메모리만 판 행동이 설명되지 않는다 |
| 가격 체제 | 수요가 늘어도 가격 결정권이 소수 대형 구매자로 이동하면 물량은 늘고 마진은 눌린다 | 할인이 정당하며 수요 뉴스로 풀리지 않는다 | 지배적. 계약가 상승률 감속과 장기계약 확대가 증거이고, 이번 주 엔비디아 사례가 결정적 |
| 공급 도착 | 2028년에 한국 신팹과 창신메모리 증설이 같은 해에 겹친다 | 수요 확인은 2026-27년에 대한 것이라 2028년 논쟁을 못 푼다 | 지배적. 오늘 오전 약세의 직접 원인도 창신메모리의 베이징 신규 공장 검토 보도였다 |

[Inference: 가설 구성과 채점은 자체 판단]

세 번째 줄에 오늘의 실제 사례가 있다. 오늘 오전 반도체가 밀린 직접적인 계기는 창신메모리가 베이징에 새 D램 공장 건설을 검토한다는 보도였다. [Fact: 언론 보도] 미국 빅테크의 수요 증거가 나온 지 사흘 만에 중국의 증설 뉴스 하나로 다시 밀린 것이다. 이 대비가 지금 시장이 어느 축을 보고 있는지 보여준다.

국내 증권사들의 목표가 조정도 같은 축을 가리킨다. 여러 증권사가 최근 목표가를 낮추면서 든 사유는 낸드 계약가 하락, 중국 노광장비 국산화 진전, 창신메모리 상장이었다. 수요 부진을 사유로 든 곳은 찾기 어렵다. [Fact: 증권사 리포트 종합] 다만 목표가를 내린 증권사들도 대체로 투자의견은 유지하며 현재 조정이 펀더멘털 대비 과하다는 평가를 붙였다.

## 5. 엔비디아가 메모리를 덜어내고 있다

두 번째 가설을 뒷받침하는 가장 선명한 증거가 이번 주에 나왔다. 그리고 이것은 강세론에 대한 가장 강한 반론이기도 하다.

엔비디아는 베라 루빈 시스템에 들어가는 SOCAMM 모듈의 용량을 모듈당 192GB에서 96GB로 절반 줄이는 방향을 추진하고 있다. 이유는 메모리 원가가 약 210만달러인 시스템 원가의 29%까지 올라 회사가 선호하는 20% 상한을 넘었기 때문이다. 이 조정이 실행되면 NVL72 랙 하나에 들어가는 LPDDR5X가 약 55TB에서 약 28TB로 줄고, 랙당 해당 메모리 원가는 약 120만달러에서 약 59만달러가 된다. [Fact: 트렌드포스, 7월 28일]

<strong>가격이 오르자 가장 강한 수요처가 메모리를 덜 쓰도록 설계를 바꾸고 있다.</strong> 어제 글에서 다룬 소비자 세트의 지불 여력 한계와 같은 메커니즘이 AI 서버 안에서 나타난 것이다. 이것은 수요가 사라진다는 뜻이 아니라 가격이 스스로를 제한한다는 뜻이고, 물량 성장과 단가 상승을 곱해서 매출을 그리는 계산이 어디서 멈추는지 보여준다.

같은 방향의 신호가 하나 더 있다. HBM4의 증분은 용량이 아니라 대역폭이다. 직전 세대인 GB300도 GPU당 HBM3E 288GB였고 베라 루빈의 HBM4도 288GB로 용량은 같으며, 달라진 것은 대역폭이 8TB/s에서 최대 22TB/s로 약 2.75배가 된 점이다. [Fact: 엔비디아 기술자료] HBM4 전환이 곧 탑재 용량 증가라는 통념과 다르다. 물론 랙당 GPU 수와 출하 대수가 늘면 총량은 늘지만, 세대 교체 자체가 자동으로 물량을 늘려 주지는 않는다.

## 6. 루빈의 시간표

수혜의 크기를 따지기 전에 시점을 정확히 해야 한다. 베라 루빈과 루빈 울트라는 다른 제품이고 시간표도 다르다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 326" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="118" y1="20" x2="118" y2="282" stroke="var(--kii-chart-axis)" stroke-width="1.5"/>
<text x="102" y="30" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">2026-06</text>
<circle cx="118" cy="26" r="6" fill="var(--kii-cat-1)"/>
<circle cx="118" cy="26" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="138" y="30" fill="var(--card-text-color-main)" font-size="13" font-weight="600">베라 루빈 풀 프로덕션</text>
<text x="138" y="48" fill="var(--card-text-color-tertiary)" font-size="11.5">HBM4는 삼성·SK하이닉스·마이크론 3사 인증 통과</text>
<text x="102" y="84" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">2026 3분기</text>
<circle cx="118" cy="80" r="6" fill="var(--kii-cat-1)"/>
<circle cx="118" cy="80" r="9" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.32" stroke-width="2"/>
<text x="138" y="84" fill="var(--card-text-color-main)" font-size="13" font-weight="600">파트너 출하 시작</text>
<text x="138" y="102" fill="var(--card-text-color-tertiary)" font-size="11.5">클라우드 8곳이 1차 물결</text>
<text x="102" y="138" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">2026-08-26</text>
<circle cx="118" cy="134" r="6" fill="var(--kii-cat-3)"/>
<circle cx="118" cy="134" r="9" fill="none" stroke="var(--kii-cat-3)" stroke-opacity="0.32" stroke-width="2"/>
<text x="138" y="138" fill="var(--card-text-color-main)" font-size="13" font-weight="600">엔비디아 회계 2분기 실적</text>
<text x="138" y="156" fill="var(--card-text-color-tertiary)" font-size="11.5">이 발표는 아직 블랙웰 중심</text>
<text x="102" y="192" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">2026 4분기</text>
<circle cx="118" cy="188" r="6" fill="var(--kii-cat-3)"/>
<circle cx="118" cy="188" r="9" fill="none" stroke="var(--kii-cat-3)" stroke-opacity="0.32" stroke-width="2"/>
<text x="138" y="192" fill="var(--card-text-color-main)" font-size="13" font-weight="600">물량 램프</text>
<text x="138" y="210" fill="var(--card-text-color-tertiary)" font-size="11.5">실제 루빈 매출은 11월 발표부터 반영</text>
<text x="102" y="246" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">2027 하반기</text>
<circle cx="118" cy="242" r="6" fill="var(--kii-cat-4)"/>
<circle cx="118" cy="242" r="9" fill="none" stroke="var(--kii-cat-4)" stroke-opacity="0.32" stroke-width="2"/>
<text x="138" y="246" fill="var(--card-text-color-main)" font-size="13" font-weight="600">루빈 울트라 공식 일정</text>
<text x="138" y="264" fill="var(--card-text-color-tertiary)" font-size="11.5">카이버 랙 2028년 지연설, 사양 하향 보도 지속</text>
</svg>
</div>
<figcaption><strong>루빈의 시간표.</strong> 지금 공급망 실적에 반영할 수 있는 것은 베라 루빈이고, 루빈 울트라는 기대에 넣되 기본 시나리오로 삼기 이르다. 8월 26일 실적은 아직 블랙웰 중심이다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 시점 | 내용 |
|---|---|
| 2026년 6월 | 베라 루빈 풀 프로덕션, HBM4 3사 인증 통과 |
| 2026년 3분기 | 파트너 출하 시작 |
| 2026년 8월 26일 | 엔비디아 회계 2분기 실적 |
| 2026년 4분기 | 물량 램프, 루빈 매출은 11월 발표부터 |
| 2027년 하반기 | 루빈 울트라 공식 일정, 지연설 병존 |

</details>
</figure>

베라 루빈은 6월 1일 풀 프로덕션에 들어갔고 파트너 출하는 올해 3분기, 물량 램프는 4분기다. HBM4는 삼성전자와 SK하이닉스, 마이크론 세 곳 모두 6월 초 기준 인증을 통과하고 양산에 들어간 것으로 확인됐다. [Fact: 엔비디아·언론] 즉 <strong>지금 공급망 실적에 반영할 수 있는 것은 베라 루빈</strong>이다.

루빈 울트라는 공식 로드맵상 2027년 하반기인데 두 가지 지연 신호가 겹쳐 있다. 카이버 랙이 기판 제조 문제로 2028년까지 밀린다는 보도가 7월 초에 나왔고, GPU당 HBM 용량도 최초 발표한 1TB에서 384GB로, 다시 192GB 수준으로 하향 보도가 이어졌다. 엔비디아는 로드맵이 온전하다고 밝혔지만 그 해명은 올해 하반기 출하하는 표준 제품에 대한 것이라 두 주장이 동시에 참일 수 있다. [Fact: 보도, 엔비디아 미확인] 따라서 루빈 울트라와 HBM4E는 기대에 넣되 기본 시나리오로 삼기는 이르다.

엔비디아의 다음 실적은 8월 26일인데, 이 발표는 여전히 블랙웰 중심이고 실제 루빈 매출이 숫자로 잡히는 것은 11월 발표부터다. [Fact: 엔비디아 공시] 그 사이의 공백을 무엇으로 채울지가 8월과 9월의 관전 포인트다.

## 7. 판정과 감시 목록

이번 실적이 낮춘 것은 수요 리스크다. 높이지 않은 것은 공급 리스크이고, 새로 드러난 것은 가격이 수요를 스스로 제한하는 경로다. 그래서 지금 메모리 주가에 대한 판단은 이렇게 정리된다. 하이퍼스케일러 실적을 근거로 메모리를 사는 논리는 절반만 맞다. 수요가 확인됐다는 부분은 맞고, 그 수요가 메모리 회사의 마진으로 얼마나 남을지는 다른 축이 결정한다.

무엇이 확인되면 어느 가설이 기각되는지 적어 둔다.

| 확인 대상 | 시점 | 어느 가설을 움직이나 |
|---|---|---|
| 삼성전자·SK하이닉스 분기보고서의 계약부채 절대액 | 8월 중순 | 선수금이 크게 늘면 가격 체제 가설이 약해진다 |
| 엔비디아 회계 2분기 실적과 루빈 발언 | 8월 26일 | 램프 일정이 앞당겨지면 시차 가설이 강해진다 |
| 3분기 서버 D램 계약가 정산치 | 9월 | 13-18% 전망을 상회하면 가격 체제 가설이 약해진다 |
| 창신메모리 베이징 공장의 실제 착공 여부 | 수시 | 확정되면 공급 도착 가설이 강해진다 |
| 엔비디아 SOCAMM 축소의 실행 여부 | 수시 | 실행되면 가격 탄력성이 확인되고 물량 전망을 낮춰야 한다 |
| 외국인의 메모리 순매수 전환 | 수시 | 수급 요인의 소진을 보여주는 가장 단순한 지표 |

마지막으로 이 글의 판정을 뒤집을 조건을 적는다. 3분기 계약가가 전망을 크게 상회하거나, 엔비디아가 SOCAMM 축소를 철회하거나, 창신메모리의 증설 일정이 지연되는 것이 확인되면 두 번째와 세 번째 가설의 무게는 줄고 시차 가설이 지배적이 된다. 그때는 지금의 할인이 기회였다는 쪽으로 판정이 바뀐다.

---

본문에 언급한 종목은 분석을 위한 예시이며 특정 종목의 매수나 매도를 권유하지 않는다. 투자 판단과 그 결과의 책임은 투자자 본인에게 있다. 마이크로소프트와 아마존의 실적 수치는 각사 발표문과 어닝콜 기준이다. 7월 외국인 수급의 종목별 합산은 출처에 따라 11.3조원에서 13.1조원까지 편차가 있어 본문에서는 11조원 이상으로만 적었고, 메모리를 제외한 순매수 규모는 역산치라 정확도에 한계가 있다. 신용융자와 레버리지 상장지수펀드 수치는 보도 기준이며 일부 항목은 출처 간 소폭 차이가 있다. 엔비디아의 SOCAMM 용량 축소와 루빈 울트라 사양 변경, 카이버 랙 지연은 조사기관과 언론 보도이며 엔비디아가 확인한 내용이 아니다. 세 가설의 구성과 채점은 통계적 추정이 아니라 판단이다. 시세와 지표는 2026년 8월 4일 종가 기준이다.

### 관련 포스팅

- [메모리는 이제 가격이 더 오르지 않아도 된다: 8월 3일 급락과 계약가 감속의 해부](/ko/post/memory-price-deceleration-p-holds-thesis-2026-08-03/)
- [7월 실적 시즌 총결산: AI 수요는 확인됐고, 메모리 가격이 IT 업계 공통 원가가 됐다](/ko/post/july-2026-earnings-two-listings-kimi-four-worries-2026-07-31/)
- [반등인가 종점인가: 여덟 개의 의심, 일곱 개의 판별 변수, 48시간의 판정](/ko/post/ai-capex-eight-doubts-rebound-or-terminal-48hours-2026-07-29/)
- [엔비디아는 왜 오픈AI의 보증인이 되려 하는가: 2,500억달러 백스톱의 해부](/ko/post/nvidia-openai-250bn-backstop-anatomy-two-lenses-2026-07-29/)
