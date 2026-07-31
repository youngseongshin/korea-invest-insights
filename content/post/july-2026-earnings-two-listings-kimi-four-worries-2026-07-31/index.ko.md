---
title: "AI 수요는 진짜였고, 청구서는 메모리로 왔다: 7월 실적 시즌 총결산"
slug: "july-2026-earnings-two-listings-kimi-four-worries-2026-07-31"
date: 2026-07-31T12:40:00+09:00
description: "7월 실적 시즌을 독립 리포트로 결산한다. TSMC부터 삼성전자, SK하이닉스, 마이크로소프트, 메타, 아마존, 애플, IBM까지 열 개의 실적과 어닝콜, SK하이닉스 나스닥 ADR과 창신메모리 상하이라는 두 개의 사상 최대 상장, 그리고 Kimi K3 쇼크를 하나의 그림으로 종합했다. 데이터는 일관된다. 클라우드 성장률은 전부 가속했고 전원이 공급 부족을 말했지만, 시장은 자본지출을 같은 분기의 매출 실증으로 채점하기 시작했다. 숨은 주인공은 메모리 가격이다. 아마존의 자본지출 상향 사유가 됐고 애플은 100년 만의 홍수라 불렀으며, 그 반대편 수취인이 한국 메모리 2사다. 이 실측을 바탕으로 시장의 우려 넷, 즉 토큰 수요와 프런티어랩 수익성, 자본지출 ROI와 공급 확대, 2028년 이후 반도체 수익성에 이번 실적 시즌이 실제로 내놓은 답을 정리했다."
categories: ["Exclusive Analysis", "Market-Outlook", "Macro-Analysis"]
tags:
  - "실적 시즌"
  - "TSMC"
  - "마이크로소프트"
  - "메타"
  - "아마존"
  - "애플"
  - "알파벳"
  - "IBM"
  - "삼성전자"
  - "SK하이닉스"
  - "창신메모리"
  - "Kimi"
  - "FOMC"
  - "HBM"
  - "Research OS"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> 연결 맥락: [반등인가 종점인가](/ko/post/ai-capex-eight-doubts-rebound-or-terminal-48hours-2026-07-29/)에서 판별표의 미정 2칸(정책, 수익화)이 48시간 안에 채워진다고 적었다. 그 48시간이 지났고 칸은 채워졌다. 이 글은 그 판정을 담으면서 7월 한 달 전체를 독립 리포트로 결산한다. 열 개의 실적과 어닝콜, 두 개의 사상 최대 상장, 하나의 중국발 모델 쇼크를 하나의 그림으로 종합하고, 시장이 반복해서 묻는 우려 넷(AI 토큰 수요, 프런티어랩의 수익성, 자본지출 ROI와 반도체 공급 확대, 2028년 이후 반도체 수익성)에 이번 실적 시즌이 실제로 내놓은 답을 가려낸다.

## TL;DR

- 7월의 실적 시즌은 폭락의 한복판에서 진행됐고, 나온 데이터는 한 방향이었다. <strong>수요 실측은 전부 상향, 가격 반응은 조건부</strong>였다. 클라우드 3사의 성장률(구글 클라우드 +82%, 애저 +43%, AWS +36.7%)이 모두 가속했고, 세 회사 모두 어닝콜에서 공급이 수요를 못 따라간다고 말했다.
- 자본지출의 문법이 바뀌었다. 상향 자체는 더 이상 호재가 아니다. <strong>지출 상향과 같은 분기에 매출 가속을 실증한 회사만 상을 받았다</strong>. 마이크로소프트는 +15%로 2008년 이후 최대 상승을, 아마존은 시간외 +7-10%를 받았고, 실증 없이 올린 알파벳(-5-7%)과 메타(-9.7%), TSMC(대만 -7.3%)는 벌을 받았다.
- 7월 실적의 숨은 주인공은 메모리 가격이다. 아마존은 자본지출 2,200억달러 상향의 사유로 메모리 원가를 명시했고, 애플 CEO는 메모리 가격을 "100년 만의 홍수"라 불렀고, IBM은 고객 예산이 메모리 선구매로 넘어가 메인프레임 매출이 42% 밀렸다. <strong>메모리가 전 세계 IT 손익계산서의 원가 항목으로 등장</strong>했고, 그 반대편 수취인이 삼성전자(분기 영업이익 89.5조원)와 SK하이닉스(60.5조원, 마진 76%)다.
- 같은 달에 메모리 자본조달의 사상 최대 기록이 둘 나왔다. SK하이닉스 나스닥 ADR 265억달러(외국 기업의 미국 상장 사상 최대)와 창신메모리 상하이 86억달러(첫날 +466%, 한때 본토 시총 1위)다. 자본시장은 <strong>한국 메모리의 오늘과 중국 메모리의 내일에 같은 달 동시 베팅</strong>했다.
- Kimi K3는 딥시크의 재판이 아니었다. 72시간에 4,700억달러를 지웠지만 대부분 되돌려졌고, 남긴 질문의 방향은 오히려 정반대였다. 단가 파괴가 아니라 <strong>더 큰 모델은 더 많은 메모리를 쓴다</strong>는 쪽이다. 2.8조 파라미터 오픈웨이트 모델의 등장은 추론 인프라, 특히 메모리 수요의 상방 재료로 재해석됐다.
- 우려 넷의 판정. 토큰 수요는 실측이 공포를 반증한다(물량 연 4-7배 성장이 단가 하락을 압도). 프런티어랩 수익성은 갈림길이다(앤스로픽은 2분기 첫 영업흑자 궤도, 오픈AI는 2030년까지 적자 전망). 자본지출 ROI는 역설이다(기업 파일럿 실패율 95%와 하이퍼스케일러 백로그 합산 1.6조달러 이상이 동시에 참). 2028년 이후 수익성은 미정이며, LTA와 선수금이라는 새 구조와 창신메모리 증설이라는 새 변수의 대결이다.
- 직전 글 판별표의 미정 2칸도 채워졌다. 정책은 매파 동결(반대 3인이 전원 인상 주장, 9월 인상 확률 61%)로 역풍 지속. 수익화는 마이크로소프트의 오픈AI 지분법 이익 전환(+4.8억달러)과 애저 서프라이즈로 순풍. 시장의 종합 답안이 7월 31일 코스피 사상 최대 급등(장중 +16.5%)이다.

<div class="thesis-callout">
<div class="thesis-callout__label">핵심 문장</div>

7월의 가격은 1999년을 물었고, 7월의 실적은 1996년으로 답했다. 성장률은 가속했고 백로그는 쌓였고 전원이 공급 부족을 말했다. 그러나 실적은 새 규칙도 함께 냈다. 자본지출은 이제 믿음이 아니라 분기 단위로 채점되는 시험이 됐고, 그 시험의 채점 기준인 메모리 가격은 이번 분기 전 세계 손익계산서에 원가로 처음 등장했다. 슈퍼사이클의 이익이 실재한다는 것과, 그 이익의 지속이 매 분기 재심사된다는 것. 7월이 남긴 것은 이 두 문장이다.

</div>

## 1. 7월의 사건 지도

한 달 동안 벌어진 일을 시간순으로 놓아야 뒤의 분석이 선다. 이 지도의 요점은 사건들의 밀도다. 사상 최대 상장 두 건, 사상 최악의 하루(IBM)와 사상 최대의 하루(마이크로소프트 시총, 코스피 상승률)가 3주 안에 몰렸다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 720 582" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="122" y1="26" x2="122" y2="504" stroke="var(--kii-chart-axis)" stroke-width="1.5"/>
<text x="96" y="34" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">7/10</text>
<circle cx="122" cy="30" r="6.5" fill="var(--kii-cat-2)"/>
<circle cx="122" cy="30" r="9.5" fill="none" stroke="var(--kii-cat-2)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="34" fill="var(--card-text-color-main)" font-size="13" font-weight="600">SK하이닉스 나스닥 ADR 상장(SKHY)</text>
<text x="144" y="51" fill="var(--card-text-color-tertiary)" font-size="11.5">265억달러 조달, 외국 기업 미국 상장 사상 최대</text>
<text x="96" y="86" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">7/14</text>
<circle cx="122" cy="82" r="6.5" fill="var(--kii-cat-1)"/>
<circle cx="122" cy="82" r="9.5" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="86" fill="var(--card-text-color-main)" font-size="13" font-weight="600">IBM 사전 경고</text>
<text x="144" y="103" fill="var(--card-text-color-tertiary)" font-size="11.5">하루 -25.2%, 회사 역사상 최악의 하루</text>
<text x="96" y="138" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">7/16</text>
<circle cx="122" cy="134" r="6.5" fill="var(--kii-cat-1)"/>
<circle cx="122" cy="134" r="9.5" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="138" fill="var(--card-text-color-main)" font-size="13" font-weight="600">TSMC 실적, Kimi K3 공개</text>
<text x="144" y="155" fill="var(--card-text-color-tertiary)" font-size="11.5">사상 최대 실적에 자본지출 상향, 같은 날 2.8조 파라미터 모델</text>
<text x="96" y="190" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">7/17-20</text>
<circle cx="122" cy="186" r="6.5" fill="var(--kii-cat-4)"/>
<circle cx="122" cy="186" r="9.5" fill="none" stroke="var(--kii-cat-4)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="190" fill="var(--card-text-color-main)" font-size="13" font-weight="600">Kimi 쇼크</text>
<text x="144" y="207" fill="var(--card-text-color-tertiary)" font-size="11.5">72시간에 미국 AI·반도체 시총 약 4,700억달러 증발</text>
<text x="96" y="242" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">7/22</text>
<circle cx="122" cy="238" r="6.5" fill="var(--kii-cat-1)"/>
<circle cx="122" cy="238" r="9.5" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="242" fill="var(--card-text-color-main)" font-size="13" font-weight="600">알파벳 실적</text>
<text x="144" y="259" fill="var(--card-text-color-tertiary)" font-size="11.5">클라우드 +82%에도 자본지출 3차 상향에 주가 -5-7%</text>
<text x="96" y="294" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">7/27</text>
<circle cx="122" cy="290" r="6.5" fill="var(--kii-cat-2)"/>
<circle cx="122" cy="290" r="9.5" fill="none" stroke="var(--kii-cat-2)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="294" fill="var(--card-text-color-main)" font-size="13" font-weight="600">창신메모리 상하이 상장</text>
<text x="144" y="311" fill="var(--card-text-color-tertiary)" font-size="11.5">첫날 +466%, 한때 중국 본토 시총 1위. 엔비디아 CDS는 사상 최고</text>
<text x="96" y="346" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">7/28</text>
<circle cx="122" cy="342" r="6.5" fill="var(--kii-cat-4)"/>
<circle cx="122" cy="342" r="9.5" fill="none" stroke="var(--kii-cat-4)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="346" fill="var(--card-text-color-main)" font-size="13" font-weight="600">검은 화요일</text>
<text x="144" y="363" fill="var(--card-text-color-tertiary)" font-size="11.5">삼성전자 -13%, SK하이닉스 -14% 장중</text>
<text x="96" y="398" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">7/29</text>
<circle cx="122" cy="394" r="6.5" fill="var(--kii-cat-3)"/>
<circle cx="122" cy="394" r="9.5" fill="none" stroke="var(--kii-cat-3)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="398" fill="var(--card-text-color-main)" font-size="13" font-weight="600">FOMC 매파 동결(9대3), 실적 삼중주</text>
<text x="144" y="415" fill="var(--card-text-color-tertiary)" font-size="11.5">SK하이닉스 미스, 마이크로소프트 서프라이즈, 메타 쇼크</text>
<text x="96" y="450" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">7/30</text>
<circle cx="122" cy="446" r="6.5" fill="var(--kii-cat-1)"/>
<circle cx="122" cy="446" r="9.5" fill="none" stroke="var(--kii-cat-1)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="450" fill="var(--card-text-color-main)" font-size="13" font-weight="600">삼성전자 확정 실적, 아마존과 애플</text>
<text x="144" y="467" fill="var(--card-text-color-tertiary)" font-size="11.5">마이크로소프트 +15%, 2008년 이후 최대 상승</text>
<text x="96" y="502" fill="var(--card-text-color-secondary)" font-size="12" font-weight="600" text-anchor="end">7/31</text>
<circle cx="122" cy="498" r="6.5" fill="var(--kii-cat-4)"/>
<circle cx="122" cy="498" r="9.5" fill="none" stroke="var(--kii-cat-4)" stroke-opacity="0.35" stroke-width="2"/>
<text x="144" y="502" fill="var(--card-text-color-main)" font-size="13" font-weight="600">코스피 사상 최대 일간 급등</text>
<text x="144" y="519" fill="var(--card-text-color-tertiary)" font-size="11.5">+16.5% 장중, 삼성전자 +21.5%, SK하이닉스 +23.5%</text>
<circle cx="113" cy="564" r="5.5" fill="var(--kii-cat-1)"/>
<text x="124" y="568" fill="var(--card-text-color-secondary)" font-size="11.5">실적</text>
<circle cx="161.4" cy="564" r="5.5" fill="var(--kii-cat-2)"/>
<text x="172.4" y="568" fill="var(--card-text-color-secondary)" font-size="11.5">상장·자본</text>
<circle cx="243.4" cy="564" r="5.5" fill="var(--kii-cat-3)"/>
<text x="254.4" y="568" fill="var(--card-text-color-secondary)" font-size="11.5">정책·모델</text>
<circle cx="325.4" cy="564" r="5.5" fill="var(--kii-cat-4)"/>
<text x="336.4" y="568" fill="var(--card-text-color-secondary)" font-size="11.5">시장</text>
</svg>
</div>
<figcaption><strong>7월의 사건 지도.</strong> 하락(Kimi 쇼크, 검은 화요일)은 실적 발표 전에, 사상 최대 반등은 실적 발표 후에 왔다. 7월 31일 수치는 장중 기준이다.</figcaption>
</figure>

이 지도에서 읽히는 리듬이 있다. 하락은 늘 실적 발표 전에 왔고, 반등은 실적 발표 후에 왔다. Kimi 쇼크(7월 17-20일)와 검은 화요일(7월 28일)은 모두 빅테크 실적이 나오기 전의 사건이었고, 사상 최대 반등(7월 30-31일)은 마이크로소프트와 아마존의 숫자가 나온 뒤에 찾아왔다. 폭락의 원인이 정보가 아니라 포지셔닝이었다면 실적이 그것을 되돌리는 흐름은 자연스러운 수순이었고, 실제로 그렇게 됐다. 같은 기간 자본과 가격은 정반대로 움직이기도 했다. 주가가 무너지던 바로 그 주에 창신메모리 청약에는 942만 계좌가 몰렸고(경쟁률 244배), SK하이닉스 ADR은 상장 나흘 만에 서울 보통주 대비 51% 프리미엄까지 벌어졌다. [Fact: 보도 종합] 유통시장의 공포와 발행시장의 탐욕이 같은 주에 나란히 있었던 셈이다.

## 2. 수요의 실측: 성장률, 토큰, 백로그

시장의 첫째 우려는 AI 토큰 수요다. 단가가 계속 떨어지는데 물량이 그것을 메꿀 만큼 크느냐는 질문이고, 이번 시즌은 이 질문에 실측으로 답한 최초의 시즌이다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 166" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="150.0" y1="16" x2="150.0" y2="118.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="150.0" y="136.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+0%</text>
<line x1="266.7" y1="16" x2="266.7" y2="118.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="266.7" y="136.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+30%</text>
<line x1="383.3" y1="16" x2="383.3" y2="118.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="383.3" y="136.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+60%</text>
<line x1="500.0" y1="16" x2="500.0" y2="118.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="500.0" y="136.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">+90%</text>
<text x="138" y="37.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">구글 클라우드</text>
<rect x="150" y="25.0" width="318.9" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="477.9" y="37.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+82%</text>
<text x="529.9" y="37.0" fill="var(--card-text-color-tertiary)" font-size="11">영업이익은 3.1배</text>
<text x="138" y="71.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">애저</text>
<rect x="150" y="59.0" width="167.2" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="326.2" y="71.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+43%</text>
<text x="378.2" y="71.0" fill="var(--card-text-color-tertiary)" font-size="11">가이던스 39-40% 상회</text>
<text x="138" y="105.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">AWS</text>
<rect x="150" y="93.0" width="142.7" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="301.7" y="105.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">+36.7%</text>
<text x="353.7" y="105.0" fill="var(--card-text-color-tertiary)" font-size="11">18개 분기 만의 최고</text>
<line x1="150" y1="16" x2="150" y2="118.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="325.0" y="158" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">2026년 2분기(마이크로소프트는 4-6월 분기) 매출 성장률, 전년 대비</text>
</svg>
</div>
<figcaption><strong>클라우드 3사 성장률.</strong> 셋 모두 전분기보다 가속했고, 셋 모두 콜에서 공급 제약을 말했다. 애저는 다음 분기 가이드가 45%다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 사업 | 성장률(전년 대비) | 비고 |
|---|---|---|
| 구글 클라우드 | +82% | 영업이익 3.1배, 백로그 5,139억달러 |
| 애저 | +43% | 가이던스 39-40% 상회, 다음 분기 45% 가이드 |
| AWS | +36.7% | 18개 분기 최고, 백로그 4,960억달러 |

</details>
</figure>

성장률이라는 표면 아래에는 근거가 세 겹 더 있다. 토큰 물량부터 보면, 구글은 월 3,200조 토큰을 처리한다고 밝혔다. 1년 전의 약 7배다. 실적콜 기준으로는 분당 220억 토큰으로 한 분기 전(160억)보다 38% 늘었다. 마이크로소프트 파운드리에서는 연 1조 토큰 이상을 쓰는 고객이 1년 새 4배로 늘었고, 제3자 집계인 오픈라우터의 처리량은 6개월 만에 5배가 됐다. [Fact: 각사 공개, 오픈라우터 집계] 단가는 같은 기간 계속 내렸다(앤스로픽 최상위 모델 기준 약 67% 인하). 물량이 연 4-7배로 크고 단가는 연 절반 수준으로만 내리면, 둘을 곱한 값은 여전히 큰 폭의 플러스다. 갭 비율 프레임으로 말하면 분자(최종 AI 매출)가 분모(자본지출)보다 빠르게 크고 있다는 뜻이다.

백로그로 넘어가면 그림이 더 커진다. 마이크로소프트 커머셜 RPO 6,780억달러(+84%), 구글 클라우드 백로그 5,139억달러(한 분기 만에 약 520억달러 증가), AWS 백로그 4,960억달러(전분기 3,640억). 셋을 합치면 1조7,000억달러에 육박한다. [Fact: 각사 공시] 그런데 이번 시즌 백로그에서 가장 중요한 디테일은 따로 있다. 마이크로소프트의 RPO 순증 약 510억달러는 <strong>전부 프런티어 모델 기업 바깥의 고객에서 나왔다</strong>. 오픈AI를 제외한 RPO 증가율이 +25%, 수주 증가율이 +18%다. [Fact: CFO 에이미 후드, 어닝콜] 백로그가 오픈AI 하나로 만들어진 신기루라는, 순환 매출을 둘러싼 의심에 이번 분기가 내놓은 직접적인 반증이다.

마지막으로 공급 제약을 말하는 목소리는 한결같았다. 피차이는 "우리는 계속 공급 제약 상태"라 했고, 후드는 "수요가 가용 공급을 계속 초과한다"고 했고, 메타의 수전 리는 "컴퓨트가 있다면 투입할 ROI 플러스 자리가 여전히 많다"고 했고, 아마존의 제시는 한 발 더 나가 "2,200억달러로도 2026년 수요를 못 채우고 2027년도 같을 것이며, 2028년에 이미 들어와 있는 수요가 놀랍다"고 했다. [Fact: 각사 어닝콜] 넷 중 누구도 수요를 걱정하지 않았다. 전원이 공급을 걱정했다.

## 3. 자본지출의 새 문법: 채점표

자본지출 ROI의 우려로 간다. 이번 시즌의 진짜 뉴스는 지출 규모가 아니라 시장 반응의 분화다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 720 234" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="150.0" y1="16" x2="150.0" y2="186.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="150.0" y="204.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">0</text>
<line x1="240.0" y1="16" x2="240.0" y2="186.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="240.0" y="204.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">60</text>
<line x1="330.0" y1="16" x2="330.0" y2="186.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="330.0" y="204.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">120</text>
<line x1="420.0" y1="16" x2="420.0" y2="186.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="420.0" y="204.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">180</text>
<line x1="510.0" y1="16" x2="510.0" y2="186.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="510.0" y="204.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">240</text>
<text x="138" y="37.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">아마존</text>
<rect x="150" y="25.0" width="330.0" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="489.0" y="37.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">220</text>
<text x="541.0" y="37.0" fill="var(--card-text-color-tertiary)" font-size="11">발표 후 +7-10%</text>
<text x="138" y="71.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">알파벳</text>
<rect x="150" y="59.0" width="300.0" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="459.0" y="71.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">200</text>
<text x="511.0" y="71.0" fill="var(--card-text-color-tertiary)" font-size="11">발표 후 -5-7%</text>
<text x="138" y="105.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">마이크로소프트</text>
<rect x="150" y="93.0" width="262.5" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="421.5" y="105.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">175</text>
<text x="473.5" y="105.0" fill="var(--card-text-color-tertiary)" font-size="11">발표 후 +15%</text>
<text x="138" y="139.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">메타</text>
<rect x="150" y="127.0" width="206.2" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="365.2" y="139.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">137.5</text>
<text x="417.2" y="139.0" fill="var(--card-text-color-tertiary)" font-size="11">발표 후 -9.7%</text>
<text x="138" y="173.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">TSMC</text>
<rect x="150" y="161.0" width="93.0" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="252.0" y="173.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">62</text>
<text x="304.0" y="173.0" fill="var(--card-text-color-tertiary)" font-size="11">발표 후 -7.3%(대만)</text>
<line x1="150" y1="16" x2="150" y2="186.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="330.0" y="226" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">2026년 자본지출 가이던스(십억달러)와 발표 직후 주가 반응</text>
</svg>
</div>
<figcaption><strong>자본지출 채점표.</strong> 금액의 크기와 반응은 무관했다. 같은 분기의 매출 실증 여부가 갈랐다. 마이크로소프트의 1,750억달러는 회계 재분류를 반영한 캘린더 2026년 기준이다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 회사 | 2026년 자본지출 가이던스 | 발표 직후 주가 |
|---|---|---|
| 아마존 | 약 2,200억달러 | +7-10% |
| 알파벳 | 1,950억-2,050억달러 | -5-7% |
| 마이크로소프트 | 약 1,750억달러(캘린더) | +15% |
| 메타 | 1,300억-1,450억달러 | -9.7% |
| TSMC | 600억-640억달러 | -7.3%(대만) |

</details>
</figure>

다섯 반응을 나란히 놓으면 규칙이 보인다. 지출 금액의 크기는 반응과 무관했다. 가장 많이 쓰는 아마존이 상을 받고 가장 적게 쓰는 TSMC가 벌을 받았다. 갈린 것은 하나, <strong>지출 상향과 같은 분기에 매출 가속과 현금흐름을 실증했는가</strong>다. 마이크로소프트는 애저 +43%(가이던스 39-40% 상회)에 다음 분기 45% 가이드를 얹었고, 아마존은 AWS 성장률을 18개 분기 만의 최고로 가속시키며 영업이익률 39.4%를 찍었다. 반면 알파벳은 클라우드 +82%라는 최고의 성장률을 내고도 잉여현금흐름이 마이너스 58억달러로 돌아선 것이 부각됐고, 메타는 자본지출이 분기 영업현금흐름의 98%를 삼키며 잉여현금흐름이 7.8억달러로 전년 대비 91% 붕괴한 데다 2027년 지출 가이던스를 거부하면서 목표가 10여 곳 하향을 받았다. [Fact: 각사 공시·보도]

여기에 각주를 둘 달아 둔다. 먼저 마이크로소프트의 "자본지출 하향"(캘린더 2026년 약 1,900억달러에서 약 1,750억달러로)은 실제 축소가 아니라 회계 재분류다. 데이터센터·건물의 내용연수를 15년에서 25년으로 늘리고 일부 금융리스를 운용리스로 돌린 결과이며, CFO 스스로 "이 영향을 제외하면 투자 기대치는 변함없다"고 했다. [Fact: 어닝콜] 시장은 그 사실을 알면서도 상을 줬다. 감가상각 논쟁의 관점에서는 눈여겨볼 대목이지만, 상각 대상이 건물이라는 점에서 4년짜리 GPU를 6년으로 잡는 것 같은 더 심각한 우려와는 성격이 다르다. 또 하나는 2027년의 그림자다. 골드만삭스는 2027년 하이퍼스케일러 자본지출을 기본 1.1조달러로 보고, 그중 약 3분의 1이 부채 조달일 것으로 추정한다. [Fact: 보도] 지출이 이미 영업현금흐름의 100%까지 차오른 상태라, 더 늘리는 돈은 전부 자본시장을 거쳐야 한다. 채점은 분기가 지날수록 더 엄격해질 것이다.

기업 도입 쪽의 실측은 여전히 차갑다. 파일럿의 95%가 측정 가능한 ROI를 못 낸다는 MIT 조사가 계속 인용되고, BCG의 2026년 조사에서 유의미한 재무 가치를 만든 기업은 26%, 가트너는 에이전틱 AI 프로젝트의 40% 이상이 2027년 말까지 취소될 것으로 본다. [Fact: 각 기관] 그런데 같은 시즌에 백로그는 1조7,000억달러다. 이 역설의 해소는 둘 중 하나다. 백로그가 미래의 취소로 판명되거나, 도입 실패율이 소수 성공 기업의 지출 집중으로 상쇄되거나. 지금까지의 실측(백로그의 비프런티어 확산, 토큰 물량의 기업 비중 증가)은 후자 쪽을 가리키지만, 이것은 판정이 아니라 추세다. [Inference: 자체 종합]

## 4. 메모리의 이중 실적: 원가의 등장

이번 시즌에서 가장 덜 보도되고 가장 중요한 패턴이다. 메모리 가격이 처음으로 <strong>메모리 회사 바깥의 실적 변수</strong>가 됐다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 720 306" xmlns="http://www.w3.org/2000/svg" role="img">
<rect x="16" y="16" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-4)" stroke-width="1.6"/>
<rect x="16" y="16" width="4" height="58" rx="2" fill="var(--kii-cat-4)"/>
<text x="30" y="37" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">아마존</text>
<text x="30" y="54" fill="var(--card-text-color-tertiary)" font-size="11">자본지출 2,000억 → 2,200억달러, 사유는 메모리 원가</text>
<line x1="256" y1="45.0" x2="261.0" y2="153.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<rect x="16" y="88" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-4)" stroke-width="1.6"/>
<rect x="16" y="88" width="4" height="58" rx="2" fill="var(--kii-cat-4)"/>
<text x="30" y="109" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">애플</text>
<text x="30" y="126" fill="var(--card-text-color-tertiary)" font-size="11">“100년 만의 홍수”, 다음 분기 마진 하락분 전부</text>
<line x1="256" y1="117.0" x2="261.0" y2="153.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<rect x="16" y="160" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-4)" stroke-width="1.6"/>
<rect x="16" y="160" width="4" height="58" rx="2" fill="var(--kii-cat-4)"/>
<text x="30" y="181" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">IBM</text>
<text x="30" y="198" fill="var(--card-text-color-tertiary)" font-size="11">고객 예산이 메모리 선구매로, Z 매출 -42%</text>
<line x1="256" y1="189.0" x2="261.0" y2="153.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<rect x="16" y="232" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-4)" stroke-width="1.6"/>
<rect x="16" y="232" width="4" height="58" rx="2" fill="var(--kii-cat-4)"/>
<text x="30" y="253" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">삼성전자 DX</text>
<text x="30" y="270" fill="var(--card-text-color-tertiary)" font-size="11">부문 출범 후 첫 적자 -0.8조원</text>
<line x1="256" y1="261.0" x2="261.0" y2="153.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<rect x="271.0" y="105.0" width="178" height="96" rx="10" fill="var(--kii-cat-1)" fill-opacity="0.12" stroke="var(--kii-cat-1)" stroke-width="2"/>
<text x="360.0" y="131.0" fill="var(--card-text-color-main)" font-size="13.5" font-weight="700" text-anchor="middle">메모리 가격</text>
<text x="360.0" y="152.0" fill="var(--card-text-color-secondary)" font-size="11.5" text-anchor="middle">분기 계약가 상승</text>
<text x="360.0" y="169.0" fill="var(--card-text-color-secondary)" font-size="11.5" text-anchor="middle">D램 +30-45%</text>
<text x="360.0" y="186.0" fill="var(--card-text-color-secondary)" font-size="11.5" text-anchor="middle">낸드 +50-68%</text>
<rect x="468" y="88.0" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-1)" stroke-width="1.6"/>
<rect x="468" y="88.0" width="4" height="58" rx="2" fill="var(--kii-cat-1)"/>
<text x="482" y="109.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">삼성전자 DS</text>
<text x="482" y="126.0" fill="var(--card-text-color-tertiary)" font-size="11">분기 영업이익 89.2조원</text>
<line x1="459.0" y1="153.0" x2="462" y2="117.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<path d="M 462 117.0 l -7 -4 l 0 8 z" fill="var(--kii-chart-axis)"/>
<rect x="468" y="160.0" width="236" height="58" rx="8" fill="none" stroke="var(--kii-cat-1)" stroke-width="1.6"/>
<rect x="468" y="160.0" width="4" height="58" rx="2" fill="var(--kii-cat-1)"/>
<text x="482" y="181.0" fill="var(--card-text-color-main)" font-size="12.5" font-weight="600">SK하이닉스</text>
<text x="482" y="198.0" fill="var(--card-text-color-tertiary)" font-size="11">분기 영업이익 60.5조원, 마진 76%</text>
<line x1="459.0" y1="153.0" x2="462" y2="189.0" stroke="var(--kii-chart-grid)" stroke-width="1.4"/>
<path d="M 462 189.0 l -7 -4 l 0 8 z" fill="var(--kii-chart-axis)"/>
</svg>
</div>
<figcaption><strong>메모리 원가의 전이 지도.</strong> 이번 분기 메모리 가격은 지불자 넷의 실적 변수로 등장했고, 수취인은 둘이다. 계약가 상승률은 양사 공시의 분기 ASP 기준이다.</figcaption>
</figure>

지도의 왼쪽부터 읽는다. 아마존은 자본지출을 2,000억달러에서 2,200억달러로 올리며 사유로 메모리 원가 상승을 명시했다. 애플 CEO 팀 쿡은 메모리 가격 급등을 "100년 만의 홍수"라 불렀고, CFO는 다음 분기 가이던스에 담긴 마진 하락의 100% 이상이 메모리 원가라고 했다. IBM은 사상 최악의 하루(-25%)를 겪었는데, 원인 중 하나가 기업 고객들이 6월 말 예산을 가격 인상 전의 서버·스토리지·메모리 선구매로 돌리면서 메인프레임 구매가 이연된 것이었다. IBM CFO의 표현대로 "파괴가 아니라 이연"이지만, 메모리가 남의 실적을 흔든 첫 사례군이다. 삼성전자조차 예외가 아니어서, 세트를 파는 DX부문이 부품 원가 상승으로 부문 출범 후 첫 적자(-0.8조원)를 냈다. TSMC의 스마트폰 플랫폼이 유일하게 역성장(-4%)한 이유도 부품 가격 상승발 세트 수요 둔화였다. [Fact: 각사 공시·어닝콜]

지도의 오른쪽, 수취인의 실적은 이렇다. 삼성전자는 매출 171.5조원에 영업이익 89.5조원(마진 52.2%), 3개 분기 연속 사상 최대이고 DS부문이 그 99.7%를 벌었다. 컨센서스를 6.3% 상회했다. SK하이닉스는 매출 79.3조원에 영업이익 60.5조원, 영업이익률 76%라는 제조업 바깥의 숫자를 냈다. 순이익은 93.9조원인데 이는 키옥시아 지분 관련 일회성 이익 63조원이 얹힌 것이라 본업 지표는 영업이익으로 읽는 것이 맞다. [Fact: 양사 공시]

그런데 SK하이닉스는 이 실적으로도 어닝 미스(-4%)를 냈고, 발표일 주가는 10% 안팎 밀렸다. 미스를 뜯어볼 필요가 있다. 원인은 수요 부진이 아니라 다른 데 있었다. 분기 ASP 상승폭이 둔화됐고(D램 +30% 전분기 대비, 1분기의 +60%대에서), 매출의 약 50%가 LTA 고정가라 현물 급등분이 실적에 반영되지 않았고, HBM4 일부 출하를 하반기로 미뤘다. [Fact: 보도·컨콜 종합] 셋 다 나쁜 뉴스는 아니다. LTA는 정확히 사이클 하강에서 실적을 지키라고 설계된 장치이니, 그 대가로 상승기에 상방이 깎이는 것은 설계상 당연한 대칭이다. 컨콜에서 확인된 구조는 이렇다. SK하이닉스는 10여 개 고객과 통상 5년의 LTA를 마무리했고 매출의 절반을 고정했다. 삼성전자는 캐파의 60-70%를 장기계약으로 운영하는 것을 목표로 하고, 전체 선수금의 약 4분의 1을 이미 수취했으며, 계약에 가격 하한선을 넣었다고 밝혔다. 2027년 HBM 물량·가격 협의는 진행 중이다("견조한 수요로 순조롭게 진행"). [Fact: 양사 컨콜] 계약부채의 절대액은 양사 모두 미공시라 8월 중순 분기보고서가 확인 창구다. [Blocked: 분기보고서 미제출]

가격의 다음 좌표는 3분기 계약이다. 트렌드포스는 서버 D램 계약가 +13-18% 전망을 유지하되, 미국 CSP들의 다년 LTA가 해당 고객 가격의 상승을 제한해 인상분이 비LTA·현물 고객에 집중될 것으로 본다. [Fact: 트렌드포스, 7월 9일] 요컨대 이번 사이클의 이익은 점점 계약 구조가 결정하고, 그 구조는 실적 변동성을 양방향으로 눌러 준다. 2018년의 교훈이 회계에 새겨진 형태다.

## 5. 두 개의 상장: 자본의 대이동

7월에는 메모리 산업 자본조달의 사상 최대 기록이 2주 간격으로 둘 나왔다.

먼저 SK하이닉스다. 7월 10일 나스닥에 ADR을 상장(티커 SKHY)해 265억달러를 조달했다. 외국 기업의 미국 상장 사상 최대로 2014년 알리바바를 넘었다. 공모가 149달러는 첫날 +13%로 마감했고, 나흘 뒤 서울 보통주 대비 프리미엄이 51%까지 벌어졌으며, 예탁원의 ADR 전환 한도(발행 주식의 2.5%)는 상장일에 소진됐다. [Fact: 보도 종합] 목적은 명시적으로 HBM 중심 AI 메모리 투자 재원이다. 미국 투자자의 한국 메모리 접근 통로가 뚫린 것 자체가 수급 이벤트이며, 지수 편입(SOX는 3개월 거래 이력 요건) 전에 프리미엄이 형성됐다는 것은 통로의 수요가 공급을 앞선다는 뜻이다.

17일 뒤 반대편에서 창신메모리(CXMT)가 상하이 스타마켓에 상장했다. 공모 조달 86억달러(그린슈 포함 시 최대 98억 상당), 첫날 +466%, 시가총액 3.66조위안(약 4,890억달러)으로 한때 본토 상장사 1위였다. [Fact: 보도 종합] 시장이 이 회사를 어떻게 보는지보다 중요한 것은 이 회사의 실체다. 숫자부터 놓는다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="150.0" y1="16" x2="150.0" y2="152.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="150.0" y="170.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">0%</text>
<line x1="264.5" y1="16" x2="264.5" y2="152.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="264.5" y="170.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">10%</text>
<line x1="379.0" y1="16" x2="379.0" y2="152.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="379.0" y="170.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">20%</text>
<line x1="493.5" y1="16" x2="493.5" y2="152.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="493.5" y="170.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">30%</text>
<line x1="608.0" y1="16" x2="608.0" y2="152.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="608.0" y="170.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="middle">40%</text>
<text x="138" y="37.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">삼성전자</text>
<rect x="150" y="25.0" width="435.1" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="594.1" y="37.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">38%</text>
<text x="138" y="71.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">SK하이닉스</text>
<rect x="150" y="59.0" width="332.1" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="491.1" y="71.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">29%</text>
<text x="138" y="105.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">마이크론</text>
<rect x="150" y="93.0" width="251.9" height="16" rx="4" fill="var(--kii-cat-1)"/>
<text x="410.9" y="105.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">22%</text>
<text x="138" y="139.0" fill="var(--card-text-color-main)" font-size="12.5" text-anchor="end">창신메모리</text>
<rect x="150" y="127.0" width="91.6" height="16" rx="4" fill="var(--kii-cat-4)"/>
<text x="250.6" y="139.0" fill="var(--card-text-color-main)" font-size="12" font-weight="600">8%</text>
<text x="302.6" y="139.0" fill="var(--card-text-color-tertiary)" font-size="11">1년 전 3%</text>
<line x1="150" y1="16" x2="150" y2="152.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<text x="379.0" y="192" fill="var(--card-text-color-tertiary)" font-size="11.5" text-anchor="middle">2026년 1분기 글로벌 D램 매출 점유율</text>
</svg>
</div>
<figcaption><strong>2026년 1분기 글로벌 D램 매출 점유율.</strong> 창신메모리는 1년 만에 3%에서 8%가 됐다. 그 8%가 두 자릿수 가격 인상과 공존했다는 것이 이번 분기의 실측이다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 회사 | 점유율 |
|---|---|
| 삼성전자 | 38% |
| SK하이닉스 | 29% |
| 마이크론 | 22% |
| 창신메모리 | 8%(1년 전 3%) |

</details>
</figure>

창신의 2026년 1분기는 매출 508억위안(+719%)에 순이익 248억위안이다. 2024년만 해도 연간 71억위안 적자였던 회사다. 그런데 흑자로 돌아선 성분을 뜯어보면, 1분기 비트 출하는 +11%인데 ASP는 약 +57% 올랐다. [Fact: 증권신고서·세미어낼리시스] <strong>창신의 이익을 만든 것은 창신 자신이 아니라 이번 사이클의 가격</strong>이라는 뜻이다. 같은 가격 순풍을 한국 2사는 마진 52-76%로 받았는데, 창신은 이제 막 흑자를 낸 정도다. 기술 격차가 회계 숫자로 드러난 셈이다.

<figure class="kii-figure">
<div class="kii-figure__frame">
<svg viewBox="0 0 700 290" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="54" y1="238.0" x2="682.0" y2="238.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="45" y="242.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">0</text>
<line x1="54" y1="187.0" x2="682.0" y2="187.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="45" y="191.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">150</text>
<line x1="54" y1="136.0" x2="682.0" y2="136.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="45" y="140.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">300</text>
<line x1="54" y1="85.0" x2="682.0" y2="85.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="45" y="89.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">450</text>
<line x1="54" y1="34.0" x2="682.0" y2="34.0" stroke="var(--kii-chart-grid)" stroke-width="1"/>
<text x="45" y="38.0" fill="var(--card-text-color-tertiary)" font-size="11" text-anchor="end">600</text>
<rect x="98.0" y="147.9" width="69.1" height="90.1" rx="4" fill="var(--kii-cat-1)"/>
<text x="132.5" y="141.9" fill="var(--card-text-color-main)" font-size="11.5" font-weight="600" text-anchor="middle">265</text>
<text x="132.5" y="257.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">2025년 말</text>
<rect x="255.0" y="119.0" width="69.1" height="119.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="289.5" y="113.0" fill="var(--card-text-color-main)" font-size="11.5" font-weight="600" text-anchor="middle">350</text>
<text x="289.5" y="257.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">2026년 말</text>
<rect x="412.0" y="95.2" width="69.1" height="142.8" rx="4" fill="var(--kii-cat-1)"/>
<text x="446.5" y="89.2" fill="var(--card-text-color-main)" font-size="11.5" font-weight="600" text-anchor="middle">420</text>
<text x="446.5" y="257.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">2027년</text>
<rect x="569.0" y="51.0" width="69.1" height="187.0" rx="4" fill="var(--kii-cat-1)"/>
<text x="603.5" y="45.0" fill="var(--card-text-color-main)" font-size="11.5" font-weight="600" text-anchor="middle">550</text>
<text x="603.5" y="257.0" fill="var(--card-text-color-secondary)" font-size="12" text-anchor="middle">2028년</text>
<line x1="54" y1="238.0" x2="682.0" y2="238.0" stroke="var(--kii-chart-axis)" stroke-width="1"/>
<rect x="54" y="267" width="11" height="11" rx="3" fill="var(--kii-cat-1)"/>
<text x="70" y="276" fill="var(--card-text-color-secondary)" font-size="11.5">창신메모리 웨이퍼 투입(천장/월)</text>
<text x="54" y="20" fill="var(--card-text-color-tertiary)" font-size="11">천장/월. 2028년은 전망 범위 500-600의 중간값</text>
</svg>
</div>
<figcaption><strong>창신메모리 웨이퍼 투입 로드맵.</strong> 2027년 약 42만장은 글로벌 D램 캐파의 약 17%다. 마이크론의 현재 투입은 약 38만5,000장이다. 세미어낼리시스 로드맵 기준이며, 노무라는 더 공격적으로, 모닝스타는 훨씬 보수적으로 본다.</figcaption>
<details class="kii-figure__table"><summary>표로 보기</summary>

| 시점 | 웨이퍼 투입(천장/월) |
|---|---|
| 2025년 말 | 약 265 |
| 2026년 말 | 약 350 |
| 2027년 | 약 420 |
| 2028년 | 500-600 |

</details>
</figure>

증설 로드맵은 위와 같고, 2027년 약 42만장이면 글로벌 D램 캐파의 약 17%다. 연간 증설분(+7만-8.5만장)은 한국·미국 3사의 연간 증설분을 웃돈다. [Fact: 세미어낼리시스 로드맵] 다만 실체의 경계도 분명하다. 주력은 아직 1z급(G4) 공정으로 EUV 없이 DUV 멀티패터닝이며 다음 노드(G5)의 난이도 상승을 증권신고서 스스로 인정한다. HBM은 웨이퍼 소트 수율이 약 35%(업계 85-90%)로 추정되고 캐파의 2% 미만이며, 증권신고서의 자금 용도에 HBM 전용 항목이 없다는 보도까지 있다. [Fact: 보도, 일부 상충] 전망은 극단적으로 갈린다. 노무라는 2028년 점유율 18%(목표가는 공모가의 12배), 세미어낼리시스는 2027년 12%, 모닝스타는 적정가를 시장가의 3분의 1 이하로 본다. [Fact: 각 기관]

한국 메모리 쪽에서 읽어야 할 대목이 있다. 위협의 시간표부터 제품마다 다르다. 범용 D램(DDR5)은 이미 현실이 됐고(델·HP가 채택, 한국 대비 최대 10% 저가) 그만큼 삼성전자의 노출이 더 크다. 반면 HBM은 빨라야 2027-2028년의 이야기다. 지배구조는 가격 규율의 반대편에 서 있다. 허페이시와 국가 펀드가 지배하는 국가 전략 자산이다 보니, 가격이 꺾여도 증설은 계속될 수 있다. 창신의 이익이 가격의 함수라면, 2028년 캐파가 착륙하는 시점과 가격 하강이 겹치는 순간 이 회사는 적자를 내면서도 증설하는 플레이어로 돌아갈 수 있다. 그것이 한국 메모리의 진짜 꼬리 리스크다. 다만 이번 사이클 안에서는 창신의 존재가 가격을 무너뜨리지는 못했다. 점유율 8%가 두 자릿수 가격 인상과 나란히 갔다는 사실 자체가 이번 분기의 실측이다. [Inference: 자체 종합]

## 6. Kimi K3와 프런티어랩의 갈림길

7월 16일 문샷AI가 공개한 Kimi K3는 2.8조 파라미터 MoE, 100만 토큰 컨텍스트의 역대 최대 오픈웨이트 모델이다. 종합 지능 지수에서 미국 프런티어 최상위(60, 59) 바로 아래(57)에 붙었고 일부 코딩 벤치마크에서는 1위를 가져갔으며, API 가격은 미국 최상위 모델의 절반에서 3분의 1 수준이다. [Fact: 벤치마크 집계·가격표] 발표 후 72시간 동안 미국 AI·반도체 시총 약 4,700억달러가 지워졌다. 딥시크의 기억이 만든 조건반사였다.

이번에는 그 서사가 사흘을 못 버텼다. 반등의 논리를 뜯어보면 딥시크 때와는 정반대다. 딥시크 쇼크가 "효율이 컴퓨트 수요를 죽인다"는 공포였다면, K3는 효율 모델이 아니라 <strong>거대 모델</strong>이다. 자체 호스팅에 최소 1.4TB의 가속기 메모리가 필요하고, 그래서 블룸버그는 이 사건을 "컴퓨트보다 메모리 이야기"로 정리했다. 엔비디아의 젠슨 황은 "월가가 이번에도 Kimi의 영향을 오해했다. 공짜 AI는 하드웨어와 칩과 데이터센터에 좋다"고 반박했다. [Fact: 보도·인터뷰] 실제로 쇼크 당일 장중에 마이크론이 플러스로 돌아섰다는 것이 이 재해석의 가격 증거다. 오픈웨이트 모델의 확산은 추론의 총량을 늘리고, 추론의 병목은 메모리다. 오픈라우터에서 중국계 모델이 처리 물량의 46%를 차지한다는 실측도 같은 방향이다. 토큰은 국적을 가리지 않고 메모리를 쓴다.

프런티어랩 수익성 우려는 이번 시즌에 처음으로 양방향 실측을 얻었다. 한쪽에서 앤스로픽은 런레이트 470억달러(연초 90억에서)와 함께 2분기 첫 영업흑자 궤도에 올라섰고 API 마진이 70-80%로 추정된다. 다른 쪽에서 오픈AI는 1분기 매출 57억달러에 순손실 37억달러, 2030년까지 양의 현금흐름을 기대하지 않는다고 투자자들에게 밝혔다. [Fact: 보도 종합] 즉 "프런티어랩은 돈을 못 번다"는 명제는 이제 틀렸고, "프런티어랩의 사업 모델에 따라 갈린다"가 맞다. 기업·API 중심이면 흑자가 이미 가능하고, 소비자 무료 사용자 9억 명을 이고 가면 적자가 구조다. 마이크로소프트 장부의 간접 증거도 이번 분기에 나왔다. 오픈AI 지분법이 4.8억달러 이익으로 전환됐고(직전 글에서 세운 판독 기준으로는 "손실 확대" 시나리오의 기각), 별도로 앤스로픽 투자에서 32억달러 이익을 인식했다. 가상청산(HLBV) 회계의 노이즈를 감안해도, 감사된 장부 두 줄이 모두 이익 방향이었다는 것은 기록할 만하다. [Fact: 마이크로소프트 어닝콜]

## 7. 네 개의 우려, 실적의 답변

시즌 전체를 우려 넷에 대한 답변서로 정리한다.

| 우려 | 실적 시즌의 실측 | 판정 | 남은 변수 |
|---|---|---|---|
| AI 토큰 수요가 실재하는가 | 구글 토큰 1년 7배, 파운드리 1조 토큰 고객 4배, 클라우드 3사 성장률 전원 가속, 전원 공급 제약 발언 | 실측이 공포를 반증 | 단가 하락 속도, 비프런티어 사업자의 마진 압박 |
| 프런티어랩은 돈을 버는가 | 앤스로픽 첫 영업흑자 궤도·API 마진 70-80%, 오픈AI 2030년까지 적자 전망, MSFT 장부의 두 지분법 라인 모두 이익 | 갈림길, 사업 모델이 가른다 | 오픈AI IPO와 자금 조달, 컴퓨트 원가 곡선 |
| 자본지출 ROI와 반도체 공급 확대 | 파일럿 95% 실패 대 백로그 1.7조달러, 시장은 분기 실증으로 채점 시작, 2027년 지출의 3분의 1 부채 조달 전망 | 역설 지속, 채점은 엄격해짐 | 매 분기 매출 가속의 지속, 크레딧 스프레드 |
| 2028년 이후 반도체 수익성 | LTA 5년·캐파 60-70%·가격 하한선·선수금, 공급 부족 2027년 심화 2028년 지속 발언, 창신 2028년 50만-60만장 로드맵 | 미정, 구조 대 변수의 대결 | 창신의 실제 램프, 신팹 착륙 시점, AI 수요의 2028년 형태 |

[Inference: 판정은 자체 종합]

넷째 줄만 부연한다. 2028년 이후를 미정으로 두는 이유는 낙관과 비관의 근거가 모두 이번 시즌에 강화됐기 때문이다. 낙관 쪽에는 업계가 2018년에서 배운 구조가 있다. 5년 LTA, 캐파의 60-70% 장기계약, 가격 하한선, 선수금 선취는 모두 다음 하강의 진폭을 계약으로 누르는 장치이고, 삼성전자는 공급 부족이 "2027년에 더 심해지고 2028년까지 지속"된다고 공식화했다. 신팹 착공에서 양산까지 3년 반이 걸린다는 물리적 시차도 공급 측의 방어다. 비관 쪽에는 창신의 증설 로드맵(2028년 50만-60만장)과 한국 신팹들의 착륙 시점(평택 P5 2028년 하반기, 용인 Y2 2028년 하반기)이 같은 해에 겹친다는 달력이 있다. 뱅크오브아메리카처럼 SK하이닉스의 실제 캐파 인도가 계획의 6분의 1에 그칠 수 있다는 반론도 있어 증설의 실체 자체가 논쟁이다. [Fact: 각 기관·컨콜] 판정을 미루는 것이 아니라, 판정의 재료가 2027년 계약 협상(HBM 가격 2배 전망 대 교착)과 창신의 다음 분기 실적부터 순차적으로 도착한다는 뜻이다.

마지막으로 감시 목록이다. 이 글의 판정을 갱신할 이벤트를 시간순으로 적는다.

| 시점 | 이벤트 | 확인할 것 |
|---|---|---|
| 8월 초 | SK하이닉스 주주환원책 발표 예고 | ADR 상장 후 첫 환원 정책의 규모와 형식 |
| 8월 중순 | 양사 분기보고서 | 계약부채(선수금) 절대액의 첫 확인 |
| 9월 중순 | FOMC(인상 확률 61%) | 매파 사이클의 실행 여부, 30년물 5.2%의 향방 |
| 9월 말 | 마이크론 FY26 4분기 | 가이던스 500억달러의 실증, HBM4E 진도 |
| 10월 | 3분기 실적 시즌 | 서버 D램 +13-18%의 정산 확인, 자본지출 채점 2라운드 |
| 10월 말 | 마이크로소프트 FY27 1분기 | 애저 45% 가이드 실증, 오픈AI 지분법 라인 재확인 |
| 수시 | 창신메모리 분기 공시 | ASP 의존 이익 구조의 지속 여부, HBM 수율 |

---

본문에 언급한 종목은 분석을 위한 예시이며 특정 종목의 매수나 매도를 권유하지 않는다. 투자 판단과 그 결과의 책임은 투자자 본인에게 있다. 실적 수치는 각사 공시와 실적 발표문, 어닝콜 기준이고 주가와 시세는 2026년 7월 31일 장중까지의 보도 기준이며, 코스피와 한국 2사의 7월 31일 수치는 종가가 아닌 장중 시세다. SK하이닉스 발표일 하락률(약 10% 안팎)과 삼성전자 7월 30일 당일 반응은 보도별 편차가 있어 범위로 적었다. 마이크론의 총이익률 등 일부 수치는 보도 종합 기준으로 원문 공시와 대조가 필요할 수 있다. 창신메모리의 캐파·수율·점유율 전망과 하이퍼스케일러 자본지출 합산은 기관별 추정이 크게 갈리는 영역이고, 골드만삭스의 2027-2028년 한국 2사 이익 전망은 단일 기관 전망이다. 백로그(RPO)는 회사별 정의가 달라 단순 합산에 한계가 있다. 판정과 채점은 통계 추정이 아니라 캘리브레이션용 판단이다.

### 관련 포스팅

- [반등인가 종점인가: 여덟 개의 의심, 일곱 개의 판별 변수, 48시간의 판정](/ko/post/ai-capex-eight-doubts-rebound-or-terminal-48hours-2026-07-29/)
- [엔비디아는 왜 오픈AI의 보증인이 되려 하는가: 2,500억달러 백스톱의 해부](/ko/post/nvidia-openai-250bn-backstop-anatomy-two-lenses-2026-07-29/)
- [검은 화요일의 해부: 중국 DUV 양산 보도는 대단한 악재인가, 노이즈인가](/ko/post/china-duv-steelman-verdict-black-tuesday-korea-memory-2026-07-28/)
- [시스코는 수요가 없어서 죽지 않았다: 수익화 갭 비율로 다시 쓰는 닷컴과 AI의 비교](/ko/post/cisco-analog-monetization-gap-ratio-1996-or-1999-2026-07-27/)
