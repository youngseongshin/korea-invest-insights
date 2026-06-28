---
title: "NVIDIA 변곡점으로 본 전닉: 실적은 강한데 주가 탄성은 언제 꺾이나"
date: 2026-06-28T22:00:00+09:00
slug: "nvidia-earnings-elasticity-hbm-cycle-samsung-hynix-2026-06-28"
canonical: "https://koreainvestinsights.com/ko/post/nvidia-earnings-elasticity-hbm-cycle-samsung-hynix-2026-06-28/"
description: "NVIDIA의 실적 성장률과 주가 탄성 변곡점을 사례로 삼아 삼성전자와 SK하이닉스, 즉 전닉의 HBM 사이클을 점검한다. 핵심은 실적 피크가 아니라 EPS revision 피크와 주가 탄성 둔화이며, 본격 판별 구간은 2026년 4분기부터 2027년 1분기다."
categories: ["Exclusive Analysis", "한국 반도체", "한국 시장"]
tags: ["NVIDIA", "삼성전자", "SK하이닉스", "전닉", "HBM", "AI 메모리", "마이크론", "반도체 사이클", "EPS revision"]
series: ["hbm", "exclusive-analysis", "sam-hama-parity"]
valley_cashtags:
  - NVIDIA
  - 삼성전자
  - SK하이닉스
  - Micron
draft: false
---

# NVIDIA 변곡점으로 본 전닉: 실적은 강한데 주가 탄성은 언제 꺾이나

이 글은 “전닉”, 즉 삼성전자와 SK하이닉스의 AI 메모리 사이클을 NVIDIA 사례로 다시 읽는 단독 분석이다. 연결해서 읽을 글은 [마이크론 FY3Q26 실적 분석](/ko/post/micron-fy3q26-ai-memory-sca-fcf-hold-2026-06-25/), [삼하마 패리티](/ko/post/samsung-hynix-micron-forward-per-parity-memory-catch-up-2026-06-03/), [삼하마 패리티 후속](/ko/post/sam-hama-parity-follow-up-ai-chip-memory-pe-map-2026-06-05/), [HBM4E 12단 경쟁](/ko/post/samsung-sk-hynix-hbm4e-12h-sample-allocation-battle-2026-06-18/), [삼성전자우 괴리율과 삼성물산 NAV 갭](/ko/post/samsung-electronics-catchup-preferred-share-samsung-ct-nav-spread-2026-06-22/)이다. 관련 허브는 [AI HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/)와 [Exclusive Analysis 허브](/ko/page/exclusive-analysis-hub/)다.

핵심 질문은 단순하다. 삼성전자와 SK하이닉스의 실적은 아직 강하다. 그렇다면 주가도 계속 같은 탄성으로 오를까. NVIDIA 사례를 보면 답은 “아니다”에 가깝다. 주가는 실적 레벨보다 실적 증가율, EPS revision, 기대치 상회 폭에 더 민감하다. 실적이 좋아도 기대가 더 앞서가면 주가는 먼저 멈춘다.

## TL;DR

- NVIDIA의 주가 상승률 둔화는 1차로 2024년 3분기, 구조적 정체는 2025년 4분기부터 2026년 1분기에 시작됐다고 본다. 매출은 계속 폭증했지만, 주가는 “실적 증가”보다 “증가율의 둔화와 기대치 상회 폭”에 반응했다.
- 전닉의 실적 사이클은 아직 꺾였다고 보기 어렵다. SK하이닉스, 삼성전자, 마이크론의 최근 실적은 모두 AI 메모리 수요가 아직 강하다는 쪽을 가리킨다.
- 다만 전닉의 주가 탄성은 이미 2026년 6월 전후 1차 과열 구간에 들어왔다. 본격 변곡 판단 구간은 2026년 4분기부터 2027년 1분기다.
- 핵심 체크포인트는 2027년 HBM 계약 가격과 물량, HBM4 점유율, NVIDIA와 빅테크 AI capex 둔화 여부, 삼성전자·SK하이닉스 메모리 영업이익률 피크아웃이다.
- 투자 판단은 삼성전자 조건부 Buy, SK하이닉스 Wait다. SK하이닉스는 HBM winner지만 crowded trade가 됐다. 삼성전자는 HBM4와 Vera Rubin catch-up 선택권 가치가 남아 있다.

<div class="thesis-callout">
  <div class="thesis-callout__label">핵심 문장</div>
  <div class="thesis-callout__body">
    전닉은 아직 실적이 꺾인 구간이 아니다. 그러나 주가 기준으로는 이미 1차 과열권이다. 이제부터 볼 것은 “HBM이 좋은가”가 아니라 “2027년 EPS revision이 주가 상승보다 빠른가”다.
  </div>
</div>

## 1. 왜 NVIDIA 사례를 먼저 봐야 하나

NVIDIA는 AI 반도체 사이클의 가장 선명한 선행 사례다. 2023년 초 주가는 실적보다 먼저 움직였고, 이후 실적이 그 기대를 따라왔다. 그러나 2024년 하반기부터는 실적이 계속 좋아도 주가가 실적 증가율만큼 반응하지 않았다.

이 패턴은 한국 HBM 주식에도 중요하다. SK하이닉스와 삼성전자의 실적이 좋아지는 것만으로는 충분하지 않다. 주가가 더 오르려면 시장이 아직 덜 믿는 추가 EPS 상향 여지가 있어야 한다.

아래 표의 실적 수치는 NVIDIA 공식 발표를 기준으로 정리했다. 주가 상승률은 Digrin의 월말 split-adjusted 가격을 사용해, 실적 발표가 속한 캘린더 분기의 단순 주가 변화율로 계산한 값이다. 정확한 발표일 기준 D+1, D+5, D+30 이벤트 수익률은 원자료 일별 다운로드가 없어 보류한다. [NVIDIA Investor Relations](https://investor.nvidia.com/financial-info/quarterly-results/default.aspx), [Digrin NVIDIA price](https://www.digrin.com/stocks/detail/NVDA/price)

| NVIDIA 실적 발표 분기 | 매출 성장률 | 데이터센터 성장률 | 발표 포함 캘린더 분기 주가 상승률 | 판정 |
|---|---:|---:|---:|---|
| FY23 Q4, 2023년 2월 발표 | YoY -21%, QoQ +2% | n/a | 2023 Q1 +90.1% | 실적보다 AI 기대 선반영 |
| FY24 Q1, 2023년 5월 발표 | YoY -13%, QoQ +19% | DC 매출 42.8억달러 | 2023 Q2 +52.3% | Q2 가이던스 쇼크로 리레이팅 |
| FY24 Q2, 2023년 8월 발표 | YoY +101%, QoQ +88% | YoY +171%, QoQ +141% | 2023 Q3 +2.8% | 첫 과열 후 숨고르기 |
| FY24 Q3, 2023년 11월 발표 | YoY +206%, QoQ +34% | YoY +279%, QoQ +41% | 2023 Q4 +13.8% | 실적 강하나 주가 탄성 둔화 |
| FY24 Q4, 2024년 2월 발표 | YoY +265%, QoQ +22% | YoY +409%, QoQ +27% | 2024 Q1 +82.5% | Blackwell과 AI capex 확신 구간 |
| FY25 Q1, 2024년 5월 발표 | YoY +262%, QoQ +18% | YoY +427%, QoQ +23% | 2024 Q2 +36.7% | 10대1 split, AI 리더 프리미엄 |
| FY25 Q2, 2024년 8월 발표 | YoY +122%, QoQ +15% | YoY +154%, QoQ +16% | 2024 Q3 -1.7% | 1차 변곡점 |
| FY25 Q3, 2024년 11월 발표 | YoY +94%, QoQ +17% | YoY +112%, QoQ +17% | 2024 Q4 +10.6% | 상승 재개, 그러나 기울기 둔화 |
| FY25 Q4, 2025년 2월 발표 | YoY +78%, QoQ +12% | YoY +93%, QoQ +16% | 2025 Q1 -19.3% | 기대치 과잉과 차익실현 |
| FY26 Q1, 2025년 5월 발표 | YoY +69%, QoQ +12% | YoY +73%, QoQ +10% | 2025 Q2 +45.8% | 조정 후 리바운드 |
| FY26 Q2, 2025년 8월 발표 | YoY +56%, QoQ +6% | YoY +56%, QoQ +5% | 2025 Q3 +18.1% | 성장 재가속 전 기대 |
| FY26 Q3, 2025년 11월 발표 | YoY +62%, QoQ +22% | YoY +66%, QoQ +25% | 2025 Q4 약 0.0% | 구조적 정체 시작 |
| FY26 Q4, 2026년 2월 발표 | YoY +73%, QoQ +20% | YoY +75%, QoQ +22% | 2026 Q1 -6.5% | 실적은 강하나 주가 무반응 |
| FY27 Q1, 2026년 5월 발표 | YoY +85%, QoQ +20% | YoY +92%, QoQ +21% | 2026 Q2, 6월 26일 기준 +10.4% | 실적 추종, 멀티플 확장 제한 |

NVIDIA FY27 Q1 매출은 816억달러, 데이터센터 매출은 752억달러였다. 전년 대비 각각 +85%, +92%였다. FY27 Q2 매출 가이던스도 910억달러 ±2%였다. 중국 데이터센터 compute 매출은 가이던스에 포함하지 않았다고 회사가 밝혔다. [NVIDIA FY27 Q1 실적 발표](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027)

그런데 주가는 이미 다른 국면에 들어갔다. 2023년 12월 말 49.49달러에서 2024년 6월 말 123.48달러까지 급등한 뒤, 2024년 6월 말부터 2026년 6월 말 192.53달러까지 상승률은 약 +56%로 둔화됐다. 특히 2025년 9월 186.56달러에서 2026년 6월 192.53달러까지는 약 +3.2%에 그쳤다. 이 기간 NVIDIA의 실적은 여전히 강했다.

결론은 분명하다. 주가는 실적 레벨에 반응하는 것이 아니라 실적 서프라이즈의 지속 가능성과 멀티플 확장 여지에 반응한다.

## 2. NVIDIA의 변곡점은 실적 둔화가 아니라 기대치 포화였다

NVIDIA의 첫 변곡점은 실적이 나빠진 순간이 아니었다. 오히려 실적은 너무 좋았다. 문제는 시장이 이미 그 좋음을 알고 있었다는 점이다.

2023년 초에는 실적이 아직 부진했지만 주가는 AI 가이던스와 capex 기대를 먼저 반영했다. FY24 Q2부터 실제 매출이 폭증하면서 주가 상승은 정당화됐다. 그러나 FY25 Q2, 즉 2024년 8월 발표 이후부터는 매출 성장률이 높아도 주가 탄성이 낮아졌다. 2025년 말부터 2026년 초에는 더 분명해졌다. FY26 Q3, FY26 Q4, FY27 Q1 모두 강한 실적이었지만 주가는 이전처럼 폭발하지 않았다.

투자자 언어로 바꾸면 이렇다.

| 구분 | 초기 국면 | 중반 국면 | 후기 국면 |
|---|---|---|---|
| 시장 질문 | AI가 실제 수요인가 | 실적이 기대를 따라오나 | 기대보다 얼마나 더 좋아지나 |
| 주가 반응 | 기대 선반영 | 실적 확인과 멀티플 확장 | EPS revision 둔화에 민감 |
| 중요한 숫자 | 다음 분기 가이던스 | 매출·데이터센터 성장률 | EPS revision, gross margin, capex 효율 |
| 투자 위험 | thesis가 틀릴 위험 | 실행 리스크 | 좋은 실적에도 주가가 멈추는 위험 |

이 표가 전닉에 중요하다. SK하이닉스와 삼성전자의 HBM 실적은 아직 강할 수 있다. 그러나 주가는 실적 피크가 아니라 기대치 피크에서 먼저 꺾일 수 있다.

## 3. 전닉의 실적 사이클은 아직 꺾였나

결론부터 말하면 아직 아니다. 수요는 깨지지 않았다.

SK하이닉스는 2026년 1분기 매출 52.5763조원, 영업이익 37.6103조원, 순이익 40.3459조원을 발표했다. 회사는 AI 메모리 수요가 실적을 견인했다고 밝혔다. [SK하이닉스 1Q26 실적 발표](https://news.skhynix.com/q1-2026-business-results/)

삼성전자는 2026년 1분기 연결 매출 133.9조원, 영업이익 57.2조원을 기록했다. DS 부문 매출은 81.7조원, 영업이익은 53.7조원이었다. 회사는 AI 수요와 가격 상승으로 메모리 매출이 사상 최대를 기록했고, HBM4와 SOCAMM2의 NVIDIA Vera Rubin 플랫폼향 양산 판매도 언급했다. [Samsung Semiconductor Global Newsroom](https://news.samsungsemiconductor.com/global/samsung-electronics-announces-first-quarter-2026-results/)

마이크론도 같은 방향을 확인했다. FY3Q26 매출은 414.56억달러, Non-GAAP EPS는 25.11달러, Non-GAAP 매출총이익률은 84.9%였다. FY4Q26 가이던스는 매출 500억달러 ±10억달러, Non-GAAP EPS 31달러 ±1달러였다. 회사는 DRAM과 NAND 수요가 공급을 크게 초과하고 있다고 설명했다. [Micron FY3Q26 실적 발표](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-record-results-third-quarter)

따라서 “전닉 실적이 꺾였다”는 말은 아직 맞지 않다. 더 정확한 표현은 “실적은 강하지만 주가가 실적보다 먼저 기대를 반영한 구간”이다.

## 4. 그런데 왜 꺾임을 경계해야 하나

전닉의 문제는 실적이 약해서가 아니다. 주가가 너무 빨리 좋아진 미래를 반영했다는 점이다.

SK하이닉스는 2026년 6월 삼성전자를 제치고 한국 시가총액 1위에 올랐고, Reuters는 SK하이닉스 주가가 2026년 들어 340% 이상 상승했다고 보도했다. 같은 보도는 2025년 HBM 시장점유율을 SK하이닉스 61%, 삼성전자 17%, Micron 21%로 인용했다. [Reuters](https://www.reuters.com/world/asia-pacific/sk-hynix-overtakes-samsung-become-koreas-most-valuable-company-2026-06-22/)

이 지점에서 시장의 질문이 바뀐다.

| 과거 질문 | 현재 질문 |
|---|---|
| SK하이닉스가 HBM winner인가 | winner인 것은 알겠는데 2027년 EPS가 더 올라갈 수 있나 |
| 삼성전자가 HBM에서 늦었나 | 늦었지만 HBM4/Rubin으로 discount가 줄어들 수 있나 |
| NVIDIA 수요가 강한가 | 수요 강세가 이미 주가와 컨센서스에 얼마나 들어갔나 |
| 메모리 가격이 좋은가 | 2027년 가격과 물량이 현재 기대보다 더 좋아질 수 있나 |

연합인포맥스는 SK하이닉스가 삼성전자를 제치고 시총 1위에 오른 것을 두고, 일부에서 강세장 종료 신호로 해석하는 논쟁도 소개했다. 이 자체가 매도 신호는 아니다. 그러나 시장이 peak earnings를 의심하기 시작했다는 점에서는 경고등이다. [연합인포맥스](https://news.einfomax.co.kr/news/articleView.html?idxno=4421219)

## 5. 전닉은 언제 꺾였다고 볼 것인가

지금 바로 “끝났다”고 보는 것은 빠르다. 그러나 2026년 4분기부터는 매수 논리보다 매도 조건을 더 엄격하게 관리해야 한다.

| 구분 | 예상 시점 | 판단 | 핵심 신호 |
|---|---:|---|---|
| 1차 주가 탄성 둔화 | 이미 2026년 6월 전후 시작 | 과열 구간 진입 | SK하이닉스 시총 1위, 개인 FOMO, 목표가 상향 러시 |
| EPS revision 피크 | 2026년 4분기부터 2027년 1분기 | 가장 중요한 구간 | 2027년 HBM 계약 가격과 물량이 기대 이하인지 확인 |
| 실적 피크아웃 | 2027년 상반기부터 하반기 | 기본 시나리오 | HBM ASP 상승률 둔화, 메모리 영업이익률 하락 |
| 완전한 메모리 다운사이클 | 2027년 하반기부터 2028년 | 아직 확정 불가 | 공급 증설이 수요를 따라잡고 재고가 쌓이는 경우 |

주가는 보통 실적보다 먼저 움직인다. 따라서 주가 기준 변곡점은 2026년 4분기부터 2027년 1분기, 펀더멘털 기준 변곡점은 2027년 상반기부터 하반기로 보는 것이 합리적이다.

## 6. 꺾임을 판정하는 5개 조건

### 6.1 HBM 가격이 더 이상 오르지 않을 때

전닉의 핵심은 HBM이다. 주가가 꺾이는 첫 번째 신호는 HBM 수요 감소가 아니라 HBM 가격 상승률 둔화일 가능성이 높다.

판정 기준은 단순하다. HBM ASP가 전분기 대비 flat 또는 하락하고, 동시에 HBM4 공급 경쟁이 심화되면 전닉은 1차로 꺾였다고 봐야 한다.

### 6.2 SK하이닉스 영업이익률이 먼저 꺾일 때

SK하이닉스의 2026년 1분기 영업이익률은 매출 52.5763조원, 영업이익 37.6103조원을 단순 계산하면 약 71.5%다. 이 숫자는 정상적인 메모리 사이클의 이익률이 아니다. 초과이익 구간이다.

그래서 매출 감소보다 마진 피크아웃이 먼저 중요하다.

판정 기준은 다음과 같다. SK하이닉스 영업이익률이 2개 분기 연속 하락하고, 매출은 증가하는데 영업이익 증가율이 둔화되면 주가는 먼저 꺾일 가능성이 높다.

### 6.3 삼성전자 HBM4 catch-up이 SK하이닉스 프리미엄을 잠식할 때

삼성전자의 HBM4 진입은 삼성전자에는 호재다. 그러나 SK하이닉스에는 독점 프리미엄 축소 리스크다.

삼성전자는 1Q26 실적 발표에서 HBM4와 SOCAMM2의 Vera Rubin 플랫폼향 양산 판매를 언급했다. 이 문장은 삼성전자 HBM discount를 줄이는 데 중요하다. 하지만 동시에 SK하이닉스의 “독점적 winner” 프리미엄을 낮출 수 있다.

판정 기준은 다음과 같다. 삼성전자와 Micron의 HBM4 qualification이 확대되면서 SK하이닉스의 HBM 점유율 또는 ASP 프리미엄이 낮아지면, 이는 SK하이닉스 단독 피크 신호다. 반대로 메모리 가격 자체가 꺾이면 삼성전자와 SK하이닉스 모두 방어주가 아니다.

### 6.4 NVIDIA 데이터센터 성장률이 정상 성장으로 내려올 때

NVIDIA는 아직 수요 붕괴 신호를 주지 않았다. FY27 Q1 매출 816억달러, 데이터센터 매출 752억달러, FY27 Q2 매출 가이던스 910억달러 ±2%는 여전히 강하다.

하지만 주식시장은 절대 매출보다 성장률 둔화를 먼저 본다.

판정 기준은 다음과 같다. NVIDIA 데이터센터 매출의 전분기 성장률이 2개 분기 연속 한 자릿수로 내려가거나, Microsoft, Amazon, Google, Meta 같은 대형 클라우드 업체가 AI capex 증가율을 낮추면 전닉도 위험 구간에 들어간다.

### 6.5 2027년 공급 증설이 수요를 따라잡는 신호

Micron은 공급 부족이 2027년 이후까지 이어질 수 있다고 말했다. 그러나 동시에 대규모 capex도 진행 중이다. SK하이닉스, 삼성전자, Micron의 HBM4와 HBM4E ramp-up이 겹치면 2027년부터 수급의 기울기가 바뀔 수 있다.

판정 기준은 다음과 같다. 2027년 HBM 계약이 장기계약이더라도 가격 floor가 낮아지거나, 고객이 물량 재협상을 요구하기 시작하면 피크아웃으로 봐야 한다.

## 7. 밸류체인과 choke point 이동

NVIDIA 초기 사이클의 병목은 GPU와 CUDA, 시스템 통합이었다. 시간이 지나면서 병목은 일부 HBM, advanced packaging, 전력, 냉각, 고객 ROI 검증으로 이동했다.

| 단계 | 병목 | 투자자 관심 |
|---|---|---|
| 2023년 | GPU 공급, CUDA, AI training 수요 | NVIDIA |
| 2024년 | Blackwell, CoWoS, HBM 공급 | NVIDIA, TSMC, SK하이닉스 |
| 2025년 | HBM, 패키징, 전력, AI capex 지속성 | SK하이닉스, 마이크론, 장비·기판 |
| 2026년 | 2027년 EPS revision, HBM4 배정, capex ROI | 삼성전자 catch-up, SK하이닉스 crowding, 마이크론 SCA |

이동의 핵심은 하위 병목으로 알파가 내려온다는 점이다. NVIDIA가 멈춘다고 AI capex가 끝난다는 뜻은 아니다. 다만 GPU leader의 추가 멀티플 확장이 제한되면, 투자자는 HBM, 패키징, 전력, 냉각, eSSD처럼 아직 덜 반영된 병목으로 이동한다.

## 8. 삼성전자: HBM laggard discount가 깨지는 쪽

삼성전자는 아직 SK하이닉스보다 늦게 반영된 부분이 있다. 투자 논리는 “삼성도 메모리가 좋아진다”가 아니다. 삼성전자의 알파는 HBM laggard discount가 HBM4와 Vera Rubin 공급으로 줄어드는가에 있다.

| 항목 | 삼성전자에 중요한 이유 |
|---|---|
| HBM4 / SOCAMM2 | NVIDIA Vera Rubin 플랫폼향 공급이 실제 매출과 마진으로 이어지는지 확인 |
| DS 영업이익률 | HBM mix 개선이 이익률로 반영되는지 확인 |
| Forward P/E | 낮은 멀티플이 EPS 상향과 함께 유지되는지 확인 |
| 파운드리 손실 | 메모리 이익 개선을 희석할 수 있는 가장 큰 리스크 |
| 주주환원 | FCF 50% 환원과 DS 성과급 자사주 매수 플로우가 수급에 미치는 영향 |

판단은 조건부 Buy다. 다만 “지금 전액 매수”가 아니라 분할 접근이 맞다. 2026년 2분기와 3분기 실적에서 HBM4, SOCAMM2, DS margin 개선이 확인될 때 비중 확대 근거가 생긴다.

무효화 조건은 명확하다.

| 무효화 조건 | 의미 |
|---|---|
| HBM4/Rubin 매출이 의미 있는 규모로 확인되지 않음 | narrative는 있으나 실적 반영이 약함 |
| DS margin이 AI memory 가격 상승에도 개선되지 않음 | mix 개선이 이익으로 연결되지 않음 |
| 파운드리 손실이 메모리 이익 개선을 흡수 | 복합 사업 discount 재확대 |
| 삼성전자 주가 상승이 EPS 상향보다 빠름 | catch-up 알파 소진 |

## 9. SK하이닉스: 최고 품질이지만 crowded trade

SK하이닉스는 좋은 회사다. HBM 선두이고, 고객 lock-in도 강하다. 그러나 좋은 회사와 좋은 신규 매수 가격은 다르다.

SK하이닉스의 핵심은 HBM winner인지 여부가 아니다. 그건 이미 시장이 알고 있다. 이제 핵심은 2027년 HBM 계약 가격과 물량이 현재 기대보다 더 좋아질 수 있는지다.

| 항목 | SK하이닉스에 중요한 이유 |
|---|---|
| HBM4 점유율 | winner 프리미엄 유지 여부 |
| 2027년 장기계약 가격 | EPS revision 지속성 |
| HBM ASP premium | 삼성전자·Micron 추격에도 가격 방어가 되는지 |
| 영업이익률 | peak earnings 착시 여부 |
| 수급 | 시총 1위, 개인 FOMO, ETF 쏠림 이후 피로도 |

판단은 Wait다. 기존 보유자는 조건부 Hold가 가능하지만, 신규 추격매수는 효율이 낮다.

신규 진입 조건은 다음과 같다.

| 진입 조건 | 해석 |
|---|---|
| 주가 15~25% 조정 | 단순 낮은 forward P/E가 아니라 가격 부담 완화 |
| 2027년 EPS 추가 상향 | peak earnings 착시를 줄이는 조건 |
| HBM4 장기 공급 계약 확인 | 2027년 이후 visibility 확보 |
| 삼성전자·Micron 추격에도 ASP premium 유지 | 독점 프리미엄이 리더십 프리미엄으로 전환 |

무효화 조건은 HBM ASP 둔화, 삼성전자·Micron의 HBM4 점유율 상승, SK하이닉스 영업이익률 2개 분기 연속 하락, capex 확대가 2027년 이후 oversupply로 바뀌는 경우다.

## 10. 전닉 전체 매매 전략

전닉을 지금 바로 끝났다고 보는 것은 성급하다. 그러나 2026년 4분기부터는 매수 논리보다 매도 조건을 더 엄격하게 관리해야 한다.

| 구분 | 판단 | 이유 |
|---|---|---|
| 삼성전자 | Conditional Buy | HBM4/Rubin catch-up 선택권 가치, 낮은 상대 멀티플, DS margin 개선 가능성 |
| SK하이닉스 | Wait / 기존 보유자는 Hold | HBM winner는 맞지만 crowded trade, 2027년 EPS 추가 상향이 필요 |
| NVIDIA | Watchlist | AI leader이나 실적 성장 대비 주가 탄성은 둔화 |
| HBM 장비·기판 | Selective Watch | 대형주 탄성이 둔화될 때 하위 병목으로 알파가 이동 가능 |

보유자가 줄여야 할 조건은 다음과 같다. 아래 중 2개 이상이 동시에 나오면 전닉 비중을 줄이는 것이 합리적이다.

1. 2027년 HBM 계약 가격이 시장 기대보다 낮다.
2. SK하이닉스 또는 삼성전자 DS 영업이익률이 전분기 대비 하락한다.
3. NVIDIA 데이터센터 성장률이 한 자릿수로 둔화된다.
4. Micron·삼성전자의 HBM4 ramp-up으로 SK하이닉스 프리미엄이 축소된다.
5. DRAM/NAND contract price가 상승률 둔화가 아니라 하락으로 전환된다.

## 11. 결론

NVIDIA 사례에서 배울 점은 명확하다. 주가는 실적이 좋아지는 순간보다, 시장이 실적 개선의 지속성을 새로 믿기 시작하는 순간에 가장 크게 움직인다. 그 다음부터는 실적이 좋아도 주가 탄성은 낮아질 수 있다.

전닉은 아직 실적 사이클이 꺾인 구간이 아니다. 오히려 2026년 실적은 강할 가능성이 높다. 그러나 주가 기준으로는 이미 1차 과열 구간이다. 본격 꺾임 여부는 2026년 4분기부터 2027년 1분기에 판단해야 한다.

SK하이닉스는 먼저 꺾일 가능성이 더 크다. 이유는 기대가 가장 많이 반영됐기 때문이다. 삼성전자는 HBM4 catch-up이 숫자로 확인되면 상대적으로 더 버틸 수 있다. 다만 메모리 가격 자체가 꺾이면 삼성전자도 방어주가 아니다.

최종 판단은 이렇다.

| 종목 | 결론 |
|---|---|
| 삼성전자 | 조건부 Buy. HBM4/Rubin이 DS margin으로 확인될 때 비중 확대 |
| SK하이닉스 | Wait. 품질은 좋지만 신규 추격은 비효율 |
| 전닉 전체 | 2026년 4분기부터 EPS revision과 HBM 계약 조건을 기준으로 트림 조건 관리 |
| 하위 병목 | 대형주 탄성 둔화 후 HBM 장비·기판·eSSD로 알파 이동 가능 |

## 근거 분류

### Fact

- NVIDIA FY27 Q1 매출은 816억달러, 데이터센터 매출은 752억달러였다. 회사는 FY27 Q2 매출 가이던스를 910억달러 ±2%로 제시했다. [NVIDIA FY27 Q1 실적 발표](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027)
- NVIDIA FY26 Q4 매출은 681억달러, 데이터센터 매출은 623억달러였다. [NVIDIA FY26 Q4 실적 발표](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026)
- SK하이닉스는 2026년 1분기 매출 52.5763조원, 영업이익 37.6103조원, 순이익 40.3459조원을 발표했다. [SK하이닉스 1Q26 실적 발표](https://news.skhynix.com/q1-2026-business-results/)
- 삼성전자는 2026년 1분기 매출 133.9조원, 영업이익 57.2조원을 발표했고, DS 부문 매출 81.7조원, 영업이익 53.7조원을 기록했다. [Samsung Semiconductor Global Newsroom](https://news.samsungsemiconductor.com/global/samsung-electronics-announces-first-quarter-2026-results/)
- 마이크론은 FY3Q26 매출 414.56억달러, Non-GAAP EPS 25.11달러, Non-GAAP 매출총이익률 84.9%를 발표했다. [Micron FY3Q26 실적 발표](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-record-results-third-quarter)

### Inference

- NVIDIA의 1차 주가 탄성 둔화는 2024년 3분기, 구조적 정체는 2025년 4분기부터 2026년 1분기부터 시작됐다고 판단한다.
- 전닉의 실적 사이클은 아직 꺾이지 않았지만, 주가 탄성은 2026년 6월 전후 1차 과열권에 들어왔다.
- SK하이닉스는 HBM winner 프리미엄이 상당 부분 주가에 반영됐을 가능성이 크다.
- 삼성전자는 HBM4/Rubin 공급이 실제 DS margin 개선으로 확인될 경우 narrative reversal 여지가 더 크다.

### Speculation

- 삼성전자의 HBM4/SOCAMM2가 2026년 하반기부터 NVIDIA향 매출과 DS margin에 의미 있게 기여할 가능성
- SK하이닉스의 2027년 HBM 계약 visibility가 시장 예상보다 더 길게 유지될 가능성
- NVIDIA의 주가 plateau가 AI capex cycle의 top signal이 아니라 GPU leader에서 하위 병목으로 알파가 이동하는 신호일 가능성

### Blocked

- NVIDIA 실적 발표일 기준 D+1, D+5, D+30 정확한 이벤트 수익률
- 삼성전자·SK하이닉스의 최신 기관 컨센서스 EPS와 목표주가 분포
- 고객별 HBM 계약 단가, 물량, 마진
- 삼성전자 HBM4/Rubin 공급의 고객별 비중과 장기 계약 조건

<small>Disclaimer: 이 글은 정보 제공과 리서치 목적의 분석이다. 특정 증권의 매수·매도 권유가 아니며, 실제 투자 판단은 각자의 투자기간, 위험 감내도, 세금, 환율, 포트폴리오 상황을 반영해 내려야 한다.</small>
