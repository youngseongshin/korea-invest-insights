---
title: "메모리 3사의 8월: 회사는 더 좋아졌는데 주가는 왜 갈렸을까"
slug: "memory-big3-august-review-why-prices-diverged-2026-08-30"
date: 2026-08-30T23:50:00+09:00
description: "8월 한 달 동안 삼성전자, SK하이닉스, 마이크론에 무슨 일이 있었는지 차분하게 정리했습니다. 회사 쪽 소식은 대체로 좋았습니다. 엔비디아는 분기 매출이 두 배로 늘었고, 세 회사 모두 장기 공급계약과 차세대 메모리 출하로 수요를 계약서에 묶었습니다. SK하이닉스는 40조원어치 자사주를 사서 전부 없애기로 했고, 삼성전자는 올해 90조에서 110조원을 주주에게 돌려주겠다고 했습니다. 그런데 주가는 셋이 달랐습니다. 8월 한 달 삼성전자는 2.1% 내렸고 SK하이닉스는 3.8% 내렸는데 마이크론은 13.3% 올랐습니다. 인터넷에 도는 마이크론 47% 상승은 사실이 아닙니다. 그 숫자의 정체와, 한국 두 회사가 좋은 소식을 내고도 오르지 못한 이유를 하나씩 살펴봅니다. 마지막으로 싸다는 말이 실제로 무슨 뜻인지, 이익이 꺾여도 지금 가격이 버티는지를 함께 계산해 봅니다."
categories: ["Exclusive Analysis", "Korea-Semiconductor", "Market-Outlook"]
tags:
  - "삼성전자"
  - "SK하이닉스"
  - "마이크론"
  - "메모리"
  - "HBM"
  - "자사주 소각"
  - "주주환원"
  - "엔비디아"
  - "CXMT"
  - "밸류에이션"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스", "MU"]
draft: false
---

> 연결 맥락: 8월에는 [반등의 수급 해부](/ko/post/rebound-flow-anatomy-two-bursts-handover-2026-08-16/)와 [한국 14종목 밸류에이션](/ko/post/kr-14-stocks-valuation-good-companies-not-cheap-stocks-2026-08-23/)을 다뤘습니다. 이번 글은 그 두 가지를 메모리 세 회사에 겹쳐 봅니다. 어렵지 않게 읽히도록 용어는 나올 때마다 풀어서 적었습니다.

## TL;DR

- 8월 한 달 동안 <strong>회사 쪽 소식은 좋아졌습니다</strong>. 수요, 계약, 기술, 주주환원이 모두 앞으로 나아갔습니다.
- 그런데 주가는 셋이 갈렸습니다. 7월 31일부터 8월 28일까지 <strong>삼성전자는 2.1% 내렸고 SK하이닉스는 3.8% 내렸는데, 마이크론은 13.3% 올랐습니다</strong>.
- 먼저 숫자 하나를 바로잡습니다. 마이크론이 8월에 47% 올라 1,211달러가 됐다는 이야기가 돌지만 사실이 아닙니다. <strong>1,211달러대는 6월 25일에 찍은 1년 최고가이고, 8월 28일 종가는 932.86달러</strong>입니다. 연초 대비로도 284%가 아니라 세 배 남짓입니다.
- 한국 두 회사가 좋은 소식을 내고도 못 오른 이유는 환원의 성격에서 잘 드러납니다. SK하이닉스는 40조원어치를 사서 <strong>전부 없애기로</strong> 했고 발표 다음 날 12.7% 올랐습니다. 삼성전자의 15조원 자사주는 <strong>임직원 성과급으로 나가는 몫</strong>이라 주식 수가 줄지 않고, 발표 뒤 첫 거래일에 8.7% 내렸습니다.
- 중국 변수도 커졌습니다. 창신메모리가 7월 말 상장 첫날 466% 오르며 시가총액이 장중 800조원대에 닿았습니다. 다만 지수 편입은 주요 지수가 아니라 보조 지수입니다.
- 지금 가격이 싼지 보려면 <strong>이익이 꺾여도 버티는지</strong>를 봐야 합니다. 2027년 예상 이익을 30% 깎아도 삼성전자는 26.8%, SK하이닉스는 10.8% 여유가 남습니다. 마이크론은 1.4% 부족해 거의 딱 맞습니다.
- 9월에는 확인할 일이 이어집니다. 한국 수출 통계, 마이크론 실적 발표, 그리고 삼성전자가 남은 환원 규모를 정하는 내년 1월까지가 이번 이야기의 시간표입니다.

<div class="thesis-callout">
<div class="thesis-callout__label">핵심 문장</div>

8월은 회사와 주식이 따로 움직인 달이었습니다. 회사가 버는 힘은 분명히 세졌습니다. 고객은 계약서에 도장을 찍었고 차세대 제품은 실제로 출하됐습니다. 번 돈을 주주에게 돌려주겠다는 약속도 커졌습니다. 그런데 시장은 그 약속을 종류별로 다르게 쳐줬습니다. 주식 수를 실제로 줄이는 소각에는 값을 지불했고, 이름만 자사주인 쪽에는 지불하지 않았습니다. 여기에 중국의 새 경쟁자와 외국인 수급이 겹치면서 한국 두 회사만 제자리에 남았습니다. 좋은 소식이 곧바로 주가가 되지는 않는다는 흔한 이야기지만, 이번에는 그 이유가 하나씩 눈에 보이게 갈렸습니다.

</div>

## 1. 8월에 세 회사 주가는 이렇게 움직였습니다

먼저 그림부터 보겠습니다. 7월 31일 종가를 0으로 놓고 8월 28일까지의 움직임을 겹쳐 그린 것입니다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 380" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="60" y1="295.3" x2="582.0" y2="295.3" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="52" y="299.3" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">-15%</text>
<line x1="60" y1="264.7" x2="582.0" y2="264.7" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="52" y="268.7" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">-10%</text>
<line x1="60" y1="234.0" x2="582.0" y2="234.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="52" y="238.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">-5%</text>
<line x1="60" y1="203.4" x2="582.0" y2="203.4" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="52" y="207.4" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">+0%</text>
<line x1="60" y1="172.7" x2="582.0" y2="172.7" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="52" y="176.7" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">+5%</text>
<line x1="60" y1="142.1" x2="582.0" y2="142.1" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="52" y="146.1" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">+10%</text>
<line x1="60" y1="111.4" x2="582.0" y2="111.4" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="52" y="115.4" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">+15%</text>
<line x1="60" y1="80.8" x2="582.0" y2="80.8" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="52" y="84.8" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">+20%</text>
<line x1="60" y1="50.1" x2="582.0" y2="50.1" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="52" y="54.1" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">+25%</text>
<line x1="60" y1="203.4" x2="582.0" y2="203.4" stroke="var(--kii-chart-axis)" stroke-width="1.3"/>
<line x1="84.9" y1="44" x2="84.9" y2="326.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="84.9" y="345" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">7/31</text>
<line x1="234.0" y1="44" x2="234.0" y2="326.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="234.0" y="345" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">8/10</text>
<line x1="432.9" y1="44" x2="432.9" y2="326.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="432.9" y="345" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">8/20</text>
<line x1="582.0" y1="44" x2="582.0" y2="326.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="582.0" y="345" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">8/28</text>
<path d="M 84.9 203.4 L 109.7 257.1 L 134.6 255.9 L 159.4 242.0 L 184.3 278.1 L 209.1 277.0 L 234.0 279.3 L 258.9 257.1 L 283.7 219.8 L 308.6 190.5 L 333.4 175.4 L 383.1 189.4 L 408.0 238.4 L 432.9 183.5 L 457.7 159.0 L 482.6 216.3 L 507.4 216.3 L 532.3 205.7 L 557.1 195.2 L 582.0 216.3" fill="none" stroke="var(--kii-cat-2)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="582.0" cy="216.3" r="4.5" fill="var(--kii-cat-2)"/>
<text x="592.0" y="207.3" fill="var(--card-text-color-main)" font-size="12" font-weight="700">삼성전자</text>
<text x="592.0" y="223.3" fill="var(--card-text-color-tertiary)" font-size="11">-2.1%</text>
<path d="M 84.9 203.4 L 109.7 257.3 L 134.6 253.7 L 159.4 221.2 L 184.3 283.0 L 209.1 309.0 L 234.0 309.8 L 258.9 307.9 L 283.7 279.8 L 308.6 248.0 L 333.4 229.4 L 383.1 223.4 L 408.0 281.2 L 432.9 213.0 L 457.7 199.1 L 482.6 220.2 L 507.4 217.7 L 532.3 214.1 L 557.1 199.1 L 582.0 226.6" fill="none" stroke="var(--kii-cat-1)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="582.0" cy="226.6" r="4.5" fill="var(--kii-cat-1)"/>
<text x="592.0" y="242.6" fill="var(--card-text-color-main)" font-size="12" font-weight="700">SK하이닉스</text>
<text x="592.0" y="258.6" fill="var(--card-text-color-tertiary)" font-size="11">-3.8%</text>
<path d="M 60.0 165.0 L 84.9 203.4 L 109.7 198.5 L 134.6 151.5 L 159.4 151.2 L 184.3 159.9 L 209.1 162.7 L 234.0 175.1 L 258.9 169.5 L 283.7 137.7 L 308.6 108.9 L 333.4 92.7 L 358.3 62.8 L 383.1 115.7 L 408.0 118.4 L 432.9 90.7 L 457.7 96.3 L 482.6 138.3 L 507.4 121.5 L 532.3 117.4 L 557.1 119.7 L 582.0 121.6" fill="none" stroke="var(--kii-cat-3)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="582.0" cy="121.6" r="4.5" fill="var(--kii-cat-3)"/>
<text x="592.0" y="123.6" fill="var(--card-text-color-main)" font-size="12" font-weight="700">MU</text>
<text x="592.0" y="139.6" fill="var(--card-text-color-tertiary)" font-size="11">+13.3%</text>
<text x="60" y="28" fill="var(--card-text-color-tertiary)" font-size="11.5">7월 31일을 0으로 둔 8월 주가 경로(%)</text>
</svg>
</div>
<figcaption><strong>8월, 셋은 같이 빠졌다가 따로 끝났습니다.</strong> 7월 31일 종가를 0으로 놓고 그린 경로입니다. 8월 10일 바닥까지는 함께 움직였고, 마이크론만 중순에 크게 올랐습니다. 한국 두 회사는 8월 20일과 21일에 반등했지만 마지막 주에 되밀렸습니다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 종목 | 7월 31일 | 8월 28일 | 한 달 등락 | 8월 최저 | 8월 최고 |
|---|---:|---:|---:|---:|---:|
| 삼성전자 | 262,500원 | 257,000원 | -2.10% | -12.4% (8/10) | +7.2% (8/21) |
| SK하이닉스 | 1,718,000원 | 1,653,000원 | -3.78% | -17.3% (8/10) | +0.7% (8/21) |
| 마이크론 | 823.03달러 | 932.86달러 | +13.34% | 0.0% (7/31) | +22.9% (8/17) |

</details>
</figure>

세 회사가 8월 초에는 같이 내렸습니다. 8월 10일에 삼성전자는 12.4%, SK하이닉스는 17.3%까지 빠졌습니다. 여기까지는 함께였습니다.

갈라진 것은 그 뒤입니다. 마이크론은 8월 중순에 22.9%까지 올랐다가 13.3% 상승으로 마쳤습니다. 한국 두 회사는 8월 20일과 21일에 크게 반등했지만 마지막 주에 다시 밀려 결국 마이너스로 끝났습니다.

한 달 성적만 따로 적으면 이렇습니다. 삼성전자는 262,500원에서 257,000원으로 2.10% 내렸고, SK하이닉스는 1,718,000원에서 1,653,000원으로 3.78% 내렸습니다. 마이크론은 823.03달러에서 932.86달러로 13.34% 올랐습니다.

## 2. 먼저 숫자 하나를 바로잡습니다

마이크론에 대해 널리 도는 이야기가 있습니다. 8월에 47% 올라 1,211달러가 됐고 연초 대비로는 284% 올랐다는 것입니다. 확인해 보니 사실이 아닙니다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 212" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="132.0" y1="18" x2="132.0" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="132.0" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">$0</text>
<line x1="254.8" y1="18" x2="254.8" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="254.8" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">$400</text>
<line x1="377.6" y1="18" x2="377.6" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="377.6" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">$800</text>
<line x1="500.5" y1="18" x2="500.5" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="500.5" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">$1,200</text>
<text x="120" y="40.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">6월 25일 고점</text>
<rect x="132.0" y="28.0" width="372.6" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="513.6" y="40.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">$1,213</text>
<text x="688.0" y="40.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">52주 최고가</text>
<text x="120" y="76.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">8월 최고</text>
<rect x="132.0" y="64.0" width="310.6" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="451.6" y="76.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">$1,012</text>
<text x="688.0" y="76.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">8월 17일</text>
<text x="120" y="112.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">8월 28일 종가</text>
<rect x="132.0" y="100.0" width="286.4" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="427.4" y="112.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">$933</text>
<text x="688.0" y="112.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">8월 마지막 거래일</text>
<text x="120" y="148.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">7월 31일 종가</text>
<rect x="132.0" y="136.0" width="252.7" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="393.7" y="148.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">$823</text>
<text x="688.0" y="148.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">8월 출발점</text>
<line x1="132.0" y1="18" x2="132.0" y2="162.0" stroke="var(--kii-chart-axis)" stroke-width="1.4"/>
<text x="350.0" y="204" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">마이크론 주가(달러). 널리 인용된 1,211달러는 8월 종가가 아니라 6월 고점이다</text>
</svg>
</div>
<figcaption><strong>널리 인용된 1,211달러는 8월 가격이 아닙니다.</strong> 그 부근 값은 6월 25일에 기록한 1년 최고가이고, 8월 28일 종가는 932.86달러입니다. 8월 중 가장 높았던 날도 1,011달러대에 그쳤습니다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 구분 | 가격 | 날짜 |
|---|---:|---|
| 1년 최고가 | 1,213.37달러 | 2026년 6월 25일 |
| 8월 최고 | 1,011.75달러 | 2026년 8월 17일 |
| 8월 마지막 종가 | 932.86달러 | 2026년 8월 28일 |
| 8월 출발점 | 823.03달러 | 2026년 7월 31일 |

</details>
</figure>

1,213달러대는 <strong>6월 25일에 기록한 1년 최고가</strong>입니다. 8월에는 그 근처에도 가지 않았습니다. 8월 중 가장 높았던 날은 8월 17일의 1,011달러대였고, 8월 28일 종가는 932.86달러입니다. 지금 가격은 6월 고점보다 오히려 23% 아래에 있습니다.

연초 대비 284%라는 숫자도 계산의 착오로 보입니다. 6월 고점을 1월 초 가격으로 나누면 약 285%가 나오는데, 그 값을 지금 수익률로 옮겨 적은 것으로 보입니다. 지난해 마지막 거래일 종가를 기준으로 하면 8월 28일까지 약 227% 올랐습니다. 큰 상승인 것은 맞지만 284%는 아닙니다.

이런 착오는 흔합니다. 최고가와 현재가를 한 표에 놓고 쓰다 보면 줄이 바뀌기 쉽습니다. 다만 이 숫자 하나로 결론이 달라집니다. 47% 올랐다면 마이크론은 명백히 비싸 보이고, 13% 올랐다면 이야기가 훨씬 조심스러워집니다.

## 3. 회사 쪽 소식은 좋았습니다

주가와 별개로 8월에 확인된 사실을 정리하면 방향은 한쪽입니다.

<strong>수요가 커졌습니다.</strong> 엔비디아는 8월 26일 분기 매출 962억달러를 발표했습니다. 1년 전보다 106% 늘어난 숫자이고, 이 중 데이터센터가 890억달러입니다. 다음 분기 전망치는 1,080억달러입니다.

<strong>그 수요가 메모리 회사의 협상력이라는 증거도 나왔습니다.</strong> 엔비디아가 앞으로 사기로 약정한 금액은 한 분기 만에 1,190억달러에서 2,790억달러로 늘었습니다. 그리고 회사는 메모리 가격 때문에 내년 회계연도 4분기 매출총이익률이 71%에서 72%까지 내려갈 수 있다고 설명했습니다. 사는 쪽이 마진을 깎아 가며 메모리를 확보하고 있다는 뜻입니다.

<strong>수요가 주문에서 계약으로 옮겨 갔습니다.</strong> 여기서 잠깐 용어를 풀겠습니다. 장기공급계약은 몇 년치 물량과 가격의 하한을 미리 정해 두는 계약입니다. 그때그때 시세로 파는 것보다 이익이 덜 흔들립니다. SK하이닉스는 11개 고객과 이런 계약을 맺었다고 공식적으로 밝혔습니다. 마이크론은 16개의 전략고객계약을 확보했고, 그중 14개 계약의 최소 매출이 약 1,000억달러입니다. 고객이 미리 맡긴 돈과 재무 약정도 220억달러입니다.

<strong>기술도 계획에서 매출로 넘어갔습니다.</strong> SK하이닉스는 2분기에 차세대 고대역폭 메모리인 HBM4 양산 출하를 시작했습니다. 삼성전자도 HBM4 판매를 늘리고 다음 세대 샘플을 내보냈다고 밝혔습니다. 삼성전자의 HBM4 수율이 80% 수준이라는 보도도 나왔는데, 이것은 회사가 공식 발표한 숫자가 아니라 업계발 보도입니다.

<strong>실적 자체도 좋았습니다.</strong> SK하이닉스의 2분기 매출은 79.3조원, 영업이익은 60.5조원으로 영업이익률이 76%입니다. 100원어치를 팔면 76원이 이익으로 남았다는 뜻입니다. 마이크론도 직전 분기 매출 414억6,000만달러에 조정 주당순이익 25.11달러를 기록했고, 다음 분기에는 매출 500억달러와 매출총이익률 86%를 전망했습니다.

## 4. 그런데 한국 두 회사는 왜 못 올랐을까요

8월에 두 회사 모두 큰 주주환원을 발표했습니다. 그런데 시장의 반응이 정반대였습니다. 이 대목이 8월에서 가장 배울 것이 많은 장면입니다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 212" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="186.0" y1="18" x2="186.0" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="186.0" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">-10</text>
<line x1="246.0" y1="18" x2="246.0" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="246.0" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">-5</text>
<line x1="306.0" y1="18" x2="306.0" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="306.0" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+0</text>
<line x1="366.0" y1="18" x2="366.0" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="366.0" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+5</text>
<line x1="426.0" y1="18" x2="426.0" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="426.0" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+10</text>
<line x1="486.0" y1="18" x2="486.0" y2="162.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="486.0" y="180.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+15</text>
<text x="138" y="40.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">SK하이닉스 8/20</text>
<rect x="306.0" y="28.0" width="152.8" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="467.8" y="40.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+12.73%</text>
<text x="688.0" y="40.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">40조 전량 소각 발표 다음 날</text>
<text x="138" y="76.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">삼성전자 8/20</text>
<rect x="306.0" y="64.0" width="113.9" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="428.9" y="76.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+9.49%</text>
<text x="688.0" y="76.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">같은 날 동반 상승</text>
<text x="138" y="112.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">SK하이닉스 8/24</text>
<rect x="265.1" y="100.0" width="40.9" height="16" rx="4" fill="var(--kii-cat-4)"/>
<text x="256.1" y="112.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="end">-3.41%</text>
<text x="688.0" y="112.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">같은 날 낙폭은 절반 이하</text>
<text x="138" y="148.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">삼성전자 8/24</text>
<rect x="201.6" y="136.0" width="104.4" height="16" rx="4" fill="var(--kii-cat-4)"/>
<text x="192.6" y="148.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="end">-8.70%</text>
<text x="688.0" y="148.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">110조 환원 발표 다음 거래일</text>
<line x1="306.0" y1="18" x2="306.0" y2="162.0" stroke="var(--kii-chart-axis)" stroke-width="1.4"/>
<text x="330.0" y="204" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">주주환원 발표 전후 하루 등락률(%), 한국거래소</text>
</svg>
</div>
<figcaption><strong>시장은 규모가 아니라 성격에 답했습니다.</strong> 다만 8월 20일은 두 회사가 함께 오른 날이라 소각 발표만의 효과로 보기는 어렵습니다. 차이가 분명해진 것은 8월 24일로, 같은 날 삼성전자의 낙폭이 SK하이닉스의 두 배가 넘었습니다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 날짜 | 삼성전자 | SK하이닉스 | 그날의 배경 |
|---|---:|---:|---|
| 8월 20일 | +9.49% | +12.73% | SK하이닉스가 전날 40조원 전량 소각을 결의 |
| 8월 24일 | -8.70% | -3.41% | 삼성전자가 직전 거래일에 90조에서 110조원 환원을 결의 |

</details>
</figure>

<strong>SK하이닉스</strong>는 8월 19일 이사회에서 40조원어치 자사주를 사서 전량 소각하기로 했습니다. 주식 수로는 2,407만주, 발행주식의 약 3.3%입니다. 국내 상장사 가운데 가장 큰 소각 규모입니다.

여기서 소각이 무엇인지 짚고 넘어가겠습니다. 회사가 자기 주식을 사서 없애면 시장에 남은 주식 수가 줄어듭니다. 같은 이익을 더 적은 주식이 나눠 갖게 되므로 주당 이익이 올라갑니다. 발표 당일 정규장은 공시 전이라 오히려 내렸지만, 다음 거래일인 8월 20일에 12.73% 올랐습니다.

<strong>삼성전자</strong>는 8월 21일 이사회에서 올해 90조원에서 110조원을 주주에게 돌려주겠다고 밝혔습니다. 규모만 보면 SK하이닉스보다 큽니다. 그런데 다음 거래일인 8월 24일 주가는 8.70% 내렸습니다.

이유는 구성에 있습니다. 발표에 포함된 15조원 자사주 매입은 <strong>임직원 성과급으로 지급하기 위한 것</strong>입니다. 회사가 주식을 사기는 하지만 없애지 않고 직원에게 나눠 주므로 시장에 도는 주식 수가 줄지 않습니다. 주당 이익이 올라가는 효과가 제한적이라는 뜻입니다. 그리고 나머지 60조원에서 80조원을 어떻게 나눌지는 내년 1월에 정해집니다. 증권사 한 곳은 금융산업의 구조개선에 관한 법률상 지분 규제 때문에 대규모 소각이 어려워 실제 소각은 10조원에서 20조원 수준일 것으로 추정했습니다. 회사가 확정한 숫자는 아직 없습니다.

<strong>시장은 규모가 아니라 성격에 값을 지불했습니다.</strong> 주식 수를 실제로 줄이는 쪽에는 두 자릿수 상승으로 답했고, 이름만 자사주인 쪽에는 하락으로 답했습니다.

다만 하나 덧붙일 것이 있습니다. SK하이닉스가 12.73% 오른 8월 20일에 삼성전자도 9.49% 올랐습니다. 그날은 두 회사가 함께 오른 날이라, 소각 발표만의 효과로 보기는 어렵습니다. 성격의 차이가 더 분명하게 드러난 것은 8월 24일입니다. 그날 삼성전자가 8.70% 내리는 동안 SK하이닉스는 3.41% 내리는 데 그쳤습니다.

## 5. 중국이라는 새 변수

7월 27일 중국의 창신메모리가 상장했습니다. 첫날 466% 올랐고 시가총액이 장중 800조원대에 닿았습니다. 종가 기준으로는 700조원대입니다. 상장으로 조달한 자금은 12조원대입니다.

8월에는 지수 편입 소식도 있었습니다. 다만 여기에는 단서가 필요합니다. 편입된 것은 <strong>주요 지수가 아니라 폭넓게 담는 보조 지수</strong>이고, 주요 지수 편입은 2027년쯤으로 예상됩니다.

이 회사가 당장 한국 두 회사의 고대역폭 메모리를 위협하는 단계는 아닙니다. 기술 격차가 남아 있습니다. 그런데 주식시장에서는 조금 다른 방식으로 작동합니다. 국가 자본이 뒤에 있는 대형 경쟁자가 생겼다는 사실 자체가, 지금의 높은 이익이 얼마나 오래갈지에 대한 의심을 유지시킵니다. 그리고 지수에 들어간 만큼 아시아 반도체에 투자하는 돈의 일부가 그쪽으로 나뉩니다.

## 6. 싸다는 말이 실제로 무슨 뜻일까요

메모리 주식을 보면 주가수익배수가 아주 낮게 나옵니다. 주가를 주당 이익으로 나눈 값인데, 낮을수록 싸다는 뜻으로 흔히 씁니다. 2027년 예상 이익으로 계산하면 삼성전자가 3.9배, SK하이닉스가 3.8배입니다. 보통 시장에서 10배에서 20배가 흔한 것을 생각하면 눈에 띄게 낮습니다.

그런데 이 숫자를 그대로 믿으면 곤란합니다. 메모리는 좋을 때와 나쁠 때의 이익 차이가 아주 큰 산업입니다. 지금은 좋은 구간이라 분모인 이익이 커져 있습니다. 이익이 정점이면 배수는 자동으로 낮아 보입니다.

그래서 방법을 하나 바꿔 봅니다. 예상 이익을 일부러 깎은 다음 다시 계산하는 것입니다. 이익이 꺾여도 지금 가격이 버티는지를 보는 방법입니다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 356" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="223.0" y1="18" x2="223.0" y2="306.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="223.0" y="324.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">-40</text>
<line x1="271.3" y1="18" x2="271.3" y2="306.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="271.3" y="324.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">-20</text>
<line x1="319.5" y1="18" x2="319.5" y2="306.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="319.5" y="324.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+0</text>
<line x1="367.7" y1="18" x2="367.7" y2="306.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="367.7" y="324.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+20</text>
<line x1="415.9" y1="18" x2="415.9" y2="306.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="415.9" y="324.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+40</text>
<line x1="464.2" y1="18" x2="464.2" y2="306.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="464.2" y="324.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+60</text>
<line x1="512.4" y1="18" x2="512.4" y2="306.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="512.4" y="324.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+80</text>
<line x1="560.6" y1="18" x2="560.6" y2="306.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="560.6" y="324.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+100</text>
<text x="158" y="38.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">삼성전자 · 이익 그대로</text>
<rect x="319.5" y="26.0" width="226.9" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="555.4" y="38.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+94.1%</text>
<text x="158" y="70.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">삼성전자 · 이익 -30%</text>
<rect x="319.5" y="58.0" width="64.6" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="393.1" y="70.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+26.8%</text>
<text x="158" y="102.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">삼성전자 · 이익 -50%</text>
<rect x="265.5" y="90.0" width="54.0" height="16" rx="4" fill="var(--kii-cat-4)"/>
<text x="256.5" y="102.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="end">-22.4%</text>
<text x="158" y="134.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">SK하이닉스 · 이익 그대로</text>
<rect x="319.5" y="122.0" width="236.0" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="564.5" y="134.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+97.9%</text>
<text x="158" y="166.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">SK하이닉스 · 이익 -30%</text>
<rect x="319.5" y="154.0" width="26.0" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="354.5" y="166.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+10.8%</text>
<text x="158" y="198.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">SK하이닉스 · 이익 -50%</text>
<rect x="237.5" y="186.0" width="82.0" height="16" rx="4" fill="var(--kii-cat-4)"/>
<text x="228.5" y="198.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="end">-34.0%</text>
<text x="158" y="230.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">마이크론 · 이익 그대로</text>
<rect x="319.5" y="218.0" width="99.6" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="428.1" y="230.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="start">+41.3%</text>
<text x="158" y="262.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">마이크론 · 이익 -30%</text>
<rect x="316.1" y="250.0" width="3.4" height="16" rx="4" fill="var(--kii-cat-4)"/>
<text x="307.1" y="262.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="end">-1.4%</text>
<text x="158" y="294.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">마이크론 · 이익 -50%</text>
<rect x="238.7" y="282.0" width="80.8" height="16" rx="4" fill="var(--kii-cat-4)"/>
<text x="229.7" y="294.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600" text-anchor="end">-33.5%</text>
<line x1="319.5" y1="18" x2="319.5" y2="306.0" stroke="var(--kii-chart-axis)" stroke-width="1.4"/>
<text x="387.0" y="348" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">현재가 대비 여유(%). 2027년 예상 이익을 그대로 두거나 깎았을 때</text>
</svg>
</div>
<figcaption><strong>이익을 깎아도 버티는지 보는 계산입니다.</strong> 2027년 예상 이익을 그대로 두거나 30%, 50% 깎은 뒤 업종별로 정상이라 볼 만한 배수를 적용해 지금 가격과 비교했습니다. 목표가가 아니라 이익이 정점에서 꺾일 때의 여유를 보는 도구입니다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 종목 | 이익 그대로 | 이익 30% 감소 | 이익 50% 감소 |
|---|---:|---:|---:|
| 삼성전자 | +94.1% | +26.8% | -22.4% |
| SK하이닉스 | +97.9% | +10.8% | -34.0% |
| 마이크론 | +41.3% | -1.4% | -33.5% |

</details>
</figure>

이익을 그대로 두면 셋 다 크게 오를 여지가 있습니다. 그런데 <strong>2027년 예상 이익을 30% 깎으면 삼성전자는 26.8%, SK하이닉스는 10.8%의 여유가 남고, 마이크론은 1.4% 모자랍니다</strong>. 이익을 절반으로 깎으면 셋 다 지금 가격이 비싸집니다.

읽는 법은 이렇습니다. 삼성전자는 이익이 상당히 꺾여도 견딜 여유가 가장 큽니다. SK하이닉스는 회사의 질은 셋 중 가장 좋은데 여유는 삼성전자보다 작습니다. 이익률이 76%까지 올라와 있어서 정상으로 돌아올 때 줄어드는 폭도 그만큼 크기 때문입니다. 마이크론은 계약을 가장 투명하게 공개했고 미국 상장 프리미엄도 받고 있지만, 그 장점이 이미 가격에 들어가 있어 여유가 가장 작습니다.

한 가지 더 봐 둘 것이 있습니다. 주가를 순자산으로 나눈 값으로 보면 순서가 뒤집힙니다. 이 기준에서 한국 두 회사는 역사적으로 높은 편입니다. 같은 회사를 두고 이익 기준으로는 싸고 자산 기준으로는 비싸다는 결과가 동시에 나오는 것인데, 이것은 시장이 지금의 이익 증가를 일시적이라고 보고 있다는 신호로 읽을 수 있습니다.

## 7. 9월부터 확인할 것들

앞으로 볼 일정을 순서대로 적어 둡니다.

| 시점 | 확인할 것 | 왜 중요한가 |
|---|---|---|
| 9월 1일 | 8월 한국 수출 통계 | 반도체 수출이 8월 1일부터 20일까지 198.8% 늘었습니다. 월 전체 수치와 단가 흐름을 보면 지금의 가격 강세가 이어지는지 알 수 있습니다 |
| 9월 말 | 마이크론 실적 발표 | 매출 500억달러와 매출총이익률 86% 전망을 실제로 채우는지 확인하는 자리입니다 |
| 11월 21일까지 | 삼성전자 자사주 매입 진행 | 성과급용이라 주식 수는 줄지 않지만 매입 기간에는 사는 힘이 됩니다 |
| 내년 1월 | 삼성전자 잔여 환원 결정 | 60조에서 80조원을 어떻게 나눌지 정합니다. 소각 비중이 커지면 이번 8월의 판정이 바뀔 수 있습니다 |
| 상시 | 중국 창신메모리의 실제 출하 | 기술 격차가 좁혀지는 속도가 이익의 지속 기간을 정합니다 |

위험도 함께 적어 둡니다. 일본은행이 9월에 금리를 올릴 가능성이 거론됩니다. 엔화를 빌려 다른 자산에 투자한 자금이 되돌아오면 한국 주식도 흔들릴 수 있습니다. 메모리 가격이 계속 오르면 사는 쪽의 마진이 줄어 어느 시점에는 주문을 줄이거나 사양을 낮출 수 있습니다. 세 회사와 장비 회사가 지금 늘리는 투자는 2028년 이후에 공급 과잉으로 돌아올 수 있습니다.

## 8. 정리하면

회사와 주식은 다른 이야기입니다. 8월에 회사는 좋아졌고, 그 사실은 실적과 계약서와 출하 기록으로 확인됩니다.

주식이 갈린 이유도 확인됩니다. 환원의 성격, 중국이라는 새 경쟁자, 그리고 미국 시장과 한국 시장의 자금 성격 차이입니다. 이 가운데 두 가지에는 시간표가 있습니다. 삼성전자의 남은 환원 결정은 내년 1월이고, 창신메모리의 실제 실력은 출하가 쌓이면 드러납니다.

그리고 마이크론의 47%처럼 널리 도는 숫자는 한 번 확인해 보는 편이 좋습니다. 결론을 바꾸는 것은 대개 해석이 아니라 숫자 하나입니다.

---

본문에 언급한 종목은 분석을 위한 예시이며 특정 종목의 매수나 매도를 권유하지 않습니다. 투자 판단과 그 결과의 책임은 투자자 본인에게 있습니다. 한국 주가는 한국거래소 자료로 직접 확인했고 마이크론 주가는 두 곳의 시장 데이터로 교차 확인했으며, 모두 2026년 8월 28일 종가 기준입니다. 마이크론의 연초 대비 상승률은 지난해 마지막 거래일 종가를 기준으로 약 227%이며, 올해 첫 거래일 종가를 기준으로 하면 약 196%입니다. 2027년 예상 이익과 이를 깎아 계산한 값은 발행일 기준 컨센서스와 자체 계산이고 증권사와 시점에 따라 달라집니다. 삼성전자의 HBM4 수율 80%는 회사 공식 발표가 아니라 업계발 보도이며, 소각 규모 10조에서 20조원 추정도 증권사 분석입니다. 관세청 자료로 확인된 것은 8월 1일부터 20일까지 반도체 수출 198.8% 증가이며, 제품별 세부 수치는 공개 자료에서 확인하지 못해 본문에 넣지 않았습니다.

### 관련 포스팅

- [한국 14종목 밸류에이션 해부: 좋은 기업 목록과 싼 주식 목록은 겹치지 않는다](/ko/post/kr-14-stocks-valuation-good-companies-not-cheap-stocks-2026-08-23/)
- [반등은 누가 샀나: 두 번에 나뉜 외국인 매수와 같은 두 종목의 손바뀜](/ko/post/rebound-flow-anatomy-two-bursts-handover-2026-08-16/)
- [AI의 병목은 GPU가 아니라 HBM이 맞다: 다만 병목은 우회를 부른다](/ko/post/hbm-bottleneck-verified-and-its-workarounds-2026-08-16/)
