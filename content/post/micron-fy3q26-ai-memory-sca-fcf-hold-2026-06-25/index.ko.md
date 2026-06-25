---
title: "마이크론 FY3Q26 실적: AI 메모리 병목이 만든 84.9% 매출총이익률과 500억달러 가이던스"
date: 2026-06-25T15:20:00+09:00
description: "마이크론 FY3Q26 실적을 공식 발표, IR 자료, 준비 발언, Q&A, 컨센서스, 장후 주가 반응, SCA 장기계약, FCF, capex, 목표가 시나리오까지 종합해 분석한다. 결론은 메모리 사이클의 이익 탄력성이 AI/HBM 수요와 장기계약으로 재평가됐지만, 장후 급등 이후 신규 진입은 조정 대기라는 것이다."
categories: ["US-Equities", "Semiconductors", "Earnings"]
tags:
  - "마이크론"
  - "Micron"
  - "MU"
  - "HBM"
  - "DRAM"
  - "NAND"
  - "SCA"
  - "AI 메모리"
  - "미국 반도체"
  - "실적 분석"
series: ["hbm", "exclusive-analysis", "sam-hama-parity"]
slug: "micron-fy3q26-ai-memory-sca-fcf-hold-2026-06-25"
valley_cashtags:
  - Micron
  - NVIDIA
  - SK하이닉스
  - 삼성전자
  - 마이크론
draft: false
---

> 연결 맥락
> 이 글은 [삼하마 패리티: 삼성전자·하이닉스가 마이크론보다 다시 싸진 구간](/ko/post/samsung-hynix-micron-forward-per-parity-memory-catch-up-2026-06-03/), [삼하마 패리티 후속: AI Chip & Memory P/E Map](/ko/post/sam-hama-parity-follow-up-ai-chip-memory-pe-map-2026-06-05/), [SK하이닉스 vs 마이크론](/ko/post/sk-hynix-vs-micron-hbm-premium-ai-memory-platform-2026-05-31/), [젠슨 황의 HBM4 3사 검증 통과 발언](/ko/post/jensen-huang-hbm4-three-vendors-qualified-market-missed-2026-06-05/), [창신메모리 IPO와 메모리 가격 리스크](/ko/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)의 후속 분석이다. 관련 허브는 [AI HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/)와 [Exclusive Analysis 허브](/ko/page/exclusive-analysis-hub/)다.

## TL;DR

마이크론 FY3Q26은 단순한 어닝 서프라이즈가 아니다. 매출 414.56억달러, Non-GAAP EPS 25.11달러, Non-GAAP 매출총이익률 84.9%, FY4Q26 매출 가이던스 500억달러, EPS 가이던스 31달러가 동시에 나왔다. 공식 자료 기준이다. [Micron FY3Q26 실적 발표](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html)

핵심 변화는 세 가지다.

1. 마이크론은 더 이상 전통적인 commodity memory 주식으로만 보기 어렵다. 회사는 AI 시스템에서 메모리 성능과 용량이 병목이라고 설명했고, 데이터센터 매출은 FY3Q에 250억달러를 넘었다.
2. 16개 전략적 고객계약, 즉 SCA가 체결됐다. 회사는 14개 계약의 최소가격 기준 누적 매출을 약 1,000억달러, 현금 예치금과 금융 약정을 220억달러로 제시했다. take-or-pay와 가격 floor가 들어간 구조라 과거 메모리 다운사이클의 이익 붕괴 위험을 일부 낮춘다.
3. 그래도 주식은 이미 많이 반응했다. FY3Q 발표 직후 장후 주가는 데이터벤더 기준 12~18% 급등했다. 실적은 훌륭하지만, 장후 가격을 기준으로 보면 안전마진은 줄었다.

결론은 <strong>HOLD / 보유 유지, 신규 진입은 조정 대기</strong>다. 12개월 기준 수정 목표가는 1,350달러로 본다. 장후 1,214달러 안팎 가격을 기준으로 상승여력은 약 11%다. 정규장 종가 1,048.51달러 기준으로 보면 업사이드가 더 커 보이지만, 실적 정보가 이미 장후 가격에 반영됐기 때문에 장후 가격을 기준으로 보는 편이 보수적이다.

<div class="thesis-callout">
  <div class="thesis-callout__label">핵심 판단</div>
  <div class="thesis-callout__body">
    이 실적은 “메모리 가격이 조금 좋았다”가 아니다. 마이크론은 AI 인프라 병목, HBM4 램프, DRAM·NAND 동시 공급부족, SCA 장기계약, 기록적 FCF를 한 번에 보여줬다. 다만 주가는 이미 그 사실을 빠르게 반영했다. 지금은 추격보다 FY4Q와 FY2027 공급·계약·FCF 가시성을 확인할 구간이다.
  </div>
</div>

## 0. 분석 기준

| 항목 | 내용 |
|---|---|
| 평가 시점 | 2026-06-25 13:59 KST |
| 회사명 | Micron Technology, Inc. |
| 티커 / 거래소 / 통화 | MU / NASDAQ / USD |
| 섹터 | 반도체, 메모리·스토리지 |
| 비교지수 | NASDAQ Composite, S&P 500 |
| 주요 자료 | Micron FY3Q26 실적 발표, Micron IR 프레젠테이션, 준비 발언, MarketBeat/Quartr transcript, Reuters 보도 |
| 정규장 이벤트 수익률 | 발표가 2026-06-24 미국장 장후였으므로 2026-06-25 미국장 종료 후 산출 가능 |

사용자가 입력한 “마이크론”은 Micron Technology, Inc.로 해석한다. 회사 실적자료도 Micron을 “Nasdaq: MU”로 표기한다. Micron은 DRAM, NAND, NOR 메모리와 스토리지 제품을 제공하는 기업이다. 회사 IR의 회사 설명과 FY3Q26 발표 자료 기준이다. [Micron IR](https://investors.micron.com/)

이번 분석은 투자 정보와 시나리오 분석이다. 개인 맞춤형 투자자문이 아니다. 숫자는 확인 가능한 공식 자료를 우선 사용했고, 컨센서스·장후 가격·다음 실적 예상일은 데이터벤더별 차이가 있어 별도로 표시했다.

## 1. 이벤트 체크

| 항목 | 판단 | KST 기준 | 근거 |
|---|---|---:|---|
| 지난 실적 발표 | 확정 | 2026-06-25 05:01 | GlobeNewswire 기준 2026-06-24 16:01 ET 발표. FY3Q26은 2026-05-28 종료 분기. |
| 실적 콜 / 웹캐스트 | 확정 | 2026-06-25 05:30 | Micron은 2026-06-24 2:30 PM Mountain time, 즉 4:30 PM ET 실적 콜을 예고했다. [Micron 실적 콜 예고](https://investors.micron.com/news-releases/news-release-details/micron-technology-report-fiscal-third-quarter-results-june-24) |
| 준비 발언과 프레젠테이션 | 확인 | 실적 발표 직후 | FY3Q26 프레젠테이션과 준비 발언이 IR 페이지에 공개됐다. [Micron Quarterly Results](https://investors.micron.com/quarterly-results) |
| Post Earnings Analyst Call | 확인 | 2026-06-25 07:00 | 사용자 제공 분석 기준. 공식 IR 이벤트 페이지의 추가 애널리스트 콜 항목 기준 |
| 다음 실적 발표 | 공식 미확정 | 미정 | Micron 공식 IR에는 FY4Q26 날짜가 아직 보이지 않는다. 데이터벤더는 9월 22일, 9월 23일 장후, 9월 29일 등으로 엇갈린다. |

정리하면 FY3Q26 실적은 이미 확정 이벤트다. 반대로 FY4Q26 발표일은 아직 공식 확정 전이다. 따라서 이 글에서는 2026년 9월 하순 미국장 장후 가능성만 사용하고, 정확한 KST 시각은 확정하지 않는다.

## 2. FY3Q26 실적 요약

이번 실적은 “beat”라는 단어만으로 부족하다. 매출, EPS, 매출총이익률, 영업현금흐름, FCF, 다음 분기 가이던스가 모두 강했다.

| 항목 | FY3Q26 실제 | FY2Q26 | FY3Q25 | 해석 | 출처 |
|---|---:|---:|---:|---|---|
| 매출 | 414.56억달러 | 238.60억달러 | 93.01억달러 | 전분기 대비 +73.7%, 전년 대비 +345.7% | Micron 실적 발표 |
| GAAP 순이익 / EPS | 282.43억달러 / 24.67달러 | 137.85억달러 / 12.07달러 | 18.85억달러 / 1.68달러 | 영업 레버리지 극단적 확대 | Micron 실적 발표 |
| Non-GAAP 순이익 / EPS | 288.57억달러 / 25.11달러 | 140.21억달러 / 12.20달러 | 21.81억달러 / 1.91달러 | Non-GAAP EPS 전분기 대비 +105.8%, 전년 대비 +1,214.7% | Micron 실적 발표 |
| GAAP 매출총이익률 | 84.6% | 74.4% | 37.7% | 가격·믹스·공급부족 효과 | Micron 실적 발표 |
| Non-GAAP 매출총이익률 | 84.9% | 74.9% | 39.0% | 전분기 대비 +10.0%p, 전년 대비 +45.9%p | Micron 실적 발표 |
| Non-GAAP 영업이익 / 마진 | 336.81억달러 / 81.2% | 164.55억달러 / 69.0% | 24.90억달러 / 26.8% | 전년 대비 13배 이상 | Micron 실적 발표 |
| 영업현금흐름 | 253.9억달러 | 119.0억달러 | 46.1억달러 | 손익 개선이 현금흐름으로 연결 | Micron 실적 발표 |
| Capex, net | 70.84억달러 | 50.04억달러 | 26.60억달러 | 공급부족 대응 투자 증가 | Micron 실적 발표 |
| Adjusted FCF | 183.04억달러 | 68.99억달러 | 19.49억달러 | 기록적 잉여현금흐름 | Micron 실적 발표 |
| 현금·투자자산·제한현금 | 302억달러 | not provided | not provided | 투자와 환원 여력의 버퍼 | Micron 실적 발표 |

공식 발표에서 가장 중요한 줄은 매출 414.56억달러, Non-GAAP EPS 25.11달러, 영업현금흐름 253.9억달러, adjusted FCF 183.04억달러다. 손익계산서만 좋은 것이 아니라 현금흐름도 같이 따라왔다. [Micron FY3Q26 실적 발표](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html)

## 3. 사업부별 매출과 마진

FY3Q26은 HBM만 좋았던 분기가 아니다. Cloud Memory, Core Data Center, Mobile and Client, Automotive and Embedded가 모두 고마진으로 급팽창했다.

| 사업부 | FY3Q26 매출 | FY2Q26 매출 | FY3Q25 매출 | FY3Q26 매출총이익률 | FY3Q26 영업마진 | 해석 |
|---|---:|---:|---:|---:|---:|---|
| Cloud Memory | 137.69억달러 | 77.49억달러 | 33.86억달러 | 83% | 78% | HBM·고부가 DRAM 중심의 핵심 성장축 |
| Core Data Center | 115.24억달러 | 56.87억달러 | 15.30억달러 | 87% | 83% | 데이터센터 DRAM·SSD 수요가 강함 |
| Mobile and Client | 115.21억달러 | 77.11억달러 | 32.55억달러 | 87% | 86% | PC·모바일도 가격과 믹스가 강함 |
| Automotive and Embedded | 46.34억달러 | 27.08억달러 | 11.27억달러 | 79% | 75% | 자동차·산업용까지 가격이 받쳐줌 |

Cloud Memory와 Core Data Center를 합치면 약 253억달러다. Micron 준비 발언의 “data center revenue exceeded 25 billion dollars”와 맞는다. 회사는 이 매출을 연율화하면 1,000억달러 이상 run-rate라고 설명했다. [Micron FY3Q26 프레젠테이션](https://investors.micron.com/static-files/2354ecda-77a0-4ddd-8462-a631eb491356)

이 표가 중요한 이유는 하나다. 이번 실적이 HBM 한 제품군의 일시적 초과수익이 아니라 DRAM, NAND, SSD, 모바일·클라이언트, 자동차·산업용까지 번지는 가격·공급부족 이벤트였다는 점이다.

## 4. FY4Q26 가이던스

회사는 FY4Q26도 더 강하게 봤다.

| 항목 | FY4Q26 회사 가이던스 | 해석 | 출처 |
|---|---:|---|---|
| 매출 | 500억달러 ± 10억달러 | 490억~510억달러 범위 | Micron 실적 발표 |
| GAAP 매출총이익률 | 약 86% | 회사 기준으로 기록적 수준 유지 | Micron 실적 발표 |
| Non-GAAP 매출총이익률 | 약 86% | FY3Q 84.9%에서 추가 상승 | Micron 실적 발표 |
| GAAP EPS | 30.73달러 ± 1.00달러 | Non-GAAP와 차이가 작음 | Micron 실적 발표 |
| Non-GAAP EPS | 31.00달러 ± 1.00달러 | 30~32달러 범위 | Micron 실적 발표 |
| Non-GAAP opex | 약 16.5억달러 | 매출 대비 비용 레버리지 유지 | Micron 실적 발표 |
| diluted shares | 약 11.5억주 | EPS 계산 기준 | Micron 프레젠테이션 |

Reuters 보도는 FY4Q 매출 가이던스 500억달러가 LSEG 평균 예상 435.8억달러를 크게 웃돌았다고 전했다. [Investing.com Reuters 보도](https://m.investing.com/news/stock-market-news/micron-forecasts-quarterly-revenue-above-estimates-4758884?ampMode=1)

이 가이던스의 의미는 “3분기가 피크였을 수 있다”보다 “4분기에도 더 높은 이익률이 가능하다”에 가깝다. 다만 CFO는 FY4Q 매출총이익률 전망과 관련해 가격 상승률이 완만해지는 점도 언급했다. 즉 가격 상승이 계속되더라도 증가 속도는 둔화될 수 있다. [Micron 준비 발언](https://investors.micron.com/static-files/631b1a32-5537-46ae-8f40-82e42fc79dfe)

## 5. 컨센서스 대비

컨센서스는 공급자별로 조금씩 다르다. 따라서 “정확한 한 숫자”보다 범위를 보는 것이 맞다.

| 항목 | 실제 또는 회사 가이던스 | 컨센서스 / 예상 | 차이 | 판단 | 출처 |
|---|---:|---:|---:|---|---|
| FY3Q 매출 | 414.6억달러 | 356.9억달러, Investing.com 기준 | +16.2% | Beat | 사용자 제공 분석, Reuters/Investing 보도 |
| FY3Q Adjusted EPS | 25.11달러 | 20.49달러, Investing.com 기준 | +22.6% | Beat | 사용자 제공 분석, Business Insider 보도 |
| FY3Q 매출 | 414.6억달러 | 359.1억달러, MarketBeat 기준 | +55.4억달러 | Beat | MarketBeat/Quartr |
| FY3Q EPS | 25.11달러 | 20.98달러, MarketBeat 기준 | +4.13달러 | Beat | MarketBeat/Quartr |
| Non-GAAP 매출총이익률 | 84.9% | LSEG preview 81.6% | +3.3%p | Beat | 사용자 제공 분석 |
| FY4Q 매출 가이던스 | 500억달러 ± 10억달러 | LSEG 평균 435.8억달러 | 큰 폭 상회 | Beat and raise | Reuters/Investing |
| FY4Q EPS 가이던스 | 31.00달러 ± 1.00달러 | Reuters 보도 기준 예상 25.84달러 | 상회 | 기대치 상향 필요 | 사용자 제공 분석 |

MarketBeat/Quartr 페이지는 FY3Q 실제 EPS 25.11달러, 컨센서스 EPS 20.98달러, 실제 매출 414.6억달러, 예상 매출 359.1억달러를 표시했다. [MarketBeat/Quartr transcript page](https://www.marketbeat.com/earnings/reports/2026-6-24-micron-technology-inc-stock/)

컨센서스별 차이는 있지만 결론은 같다. 이번 실적은 매출, EPS, 매출총이익률, 가이던스가 모두 시장 기대를 웃돌았다.

## 6. EPS 품질 점검

EPS가 너무 크게 뛰었기 때문에 품질 점검이 필요하다. 결론은 “headline EPS만 좋은 것이 아니라 영업이익과 FCF도 같이 좋았다”다.

| 점검 항목 | 결과 | 해석 | 출처 |
|---|---|---|---|
| GAAP EPS vs Non-GAAP EPS | GAAP 24.67달러, Non-GAAP 25.11달러 | 차이는 0.44달러로 크지 않다. 조정 EPS가 GAAP와 같은 방향이다. | Micron 실적 발표 |
| 매출과 영업이익 | 매출 +345.7% YoY, Non-GAAP 영업이익 336.81억달러 | EPS 개선이 영업단 개선과 일치한다. | Micron 실적 발표 |
| 영업현금흐름 | 253.9억달러 | 현금흐름이 손익을 뒷받침한다. | Micron 실적 발표 |
| Adjusted FCF | 183.04억달러 | Capex 증가에도 잉여현금흐름이 크게 남았다. | Micron 실적 발표 |
| 조정 항목 | GAAP와 Non-GAAP 차이 존재 | non-GAAP reconciliations는 공식 발표 부록에 제공된다. | Micron 실적 발표 |

이 실적에는 EPS 품질 경고가 일부 존재할 수 있다. 이유는 Non-GAAP 기준을 사용하고, SCA 고객예치금은 financing cash flow로 들어가며, FY2027 capex가 크게 늘 수 있기 때문이다. 그러나 FY3Q만 놓고 보면 GAAP와 Non-GAAP 모두 같은 방향이고, 영업현금흐름과 FCF도 강하다. 따라서 이번 EPS 서프라이즈는 단순 회계상 이익이라기보다 가격, 믹스, 공급부족, 영업 레버리지의 결과로 보는 것이 맞다.

## 7. 실적의 핵심 긍정 신호

### 7.1 수요보다 공급이 병목이다

경영진은 DRAM과 NAND 수요가 산업 공급을 크게 초과하고, 타이트한 수급이 2027년 이후까지 이어질 것으로 봤다. 준비 발언에서는 공급이 2028년에 점진적으로 개선되더라도 메모리 공급이 수요를 언제 따라잡을지 아직 가시성이 없다고 설명했다. [Micron 준비 발언](https://investors.micron.com/static-files/631b1a32-5537-46ae-8f40-82e42fc79dfe)

이 말은 주식에 중요하다. 메모리 주식은 보통 가격 상승 후 공급이 늘며 다시 무너진다. 그런데 회사가 말하는 현재 병목은 단순 재고 부족이 아니라 greenfield fab 건설, 숙련 인력, 인허가, 전력 인프라, 공정 복잡도, HBM trade ratio가 모두 얽힌 공급 병목이다.

### 7.2 HBM4 상업화가 실제 매출로 들어왔다

실적 발표는 HBM4가 lead customer 플랫폼용으로 high-volume shipment 중이고, 여러 end customer에 qualification sample이 출하됐다고 밝혔다. [Micron FY3Q26 실적 발표](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html)

준비 발언은 더 구체적이다. Micron은 HBM4 12-high 램프가 HBM3E 12-high보다 두 배 빠르게 진행되고 있으며, HBM4 매출을 이미 10억달러 이상 출하했다고 설명했다. HBM4E는 1-gamma DRAM 기반으로 개발 중이고, calendar 2027 양산을 목표로 한다. [Micron 준비 발언](https://investors.micron.com/static-files/631b1a32-5537-46ae-8f40-82e42fc79dfe)

### 7.3 SCA가 메모리 사이클의 이익 붕괴 위험을 낮춘다

SCA는 Strategic Customer Agreement, 즉 전략적 고객계약이다. 핵심은 장기 물량, take-or-pay, 가격 floor, 일부 가격 ceiling, 고객 예치금이다.

| SCA 항목 | 회사 설명 | 투자 해석 | 출처 |
|---|---|---|---|
| 체결 계약 수 | 16개 | 단일 고객이 아니라 여러 end market에 걸친 구조 | Micron 준비 발언 |
| 기간 | 보통 2026년부터 2030년 말까지 5년, 자동차는 보통 3년 | 사이클 가시성 상승 | Micron 준비 발언 |
| 물량 범위 | DRAM 물량 약 20%, NAND 물량 약 3분의 1 | 현재 체결분만으로도 의미 있는 규모 | Micron 준비 발언 |
| 매출 커버리지 | 완료 시 회사 매출 절반 이상이 SCA 아래 들어갈 수 있음 | commodity discount 축소 가능성 | Micron 준비 발언 |
| 가격 구조 | take-or-pay, floor/ceiling, 일부 fixed price 또는 market price | 하방 방어와 상방 제한이 동시에 존재 | Micron 준비 발언 |
| RPO | FY3Q 말 50억달러 초과, signed SCA 기준 약 1,000억달러 | 최소 물량·최소 가격 기준이라 실제 매출은 더 클 수 있음 | Micron 준비 발언, Q&A |
| 현금 예치금·금융 약정 | 약 220억달러, 이 중 현금 예치금 약 180억달러 | 고객 commitment의 강도 | Micron 준비 발언, Q&A |

SCA는 마이크론에 두 가지를 준다. 첫째, 메모리 기업 특유의 다운사이클 이익 붕괴를 낮추는 floor다. 둘째, 고객이 장기 공급을 확보하려고 돈과 약정을 넣을 만큼 메모리 병목이 크다는 증거다.

단, SCA는 완전한 무료 옵션이 아니다. price ceiling이 있는 계약은 시장가격이 더 치솟을 때 일부 upside를 제한할 수 있다. 고객 예치금도 free cash flow가 아니라 financing cash flow로 잡힌다. CFO는 Q&A에서 고객 예치금이 선지급 매출이 아니며, 계약 수행에 따라 후반부에 고객에게 반환된다고 설명했다. [MarketBeat/Quartr transcript](https://www.marketbeat.com/earnings/reports/2026-6-24-micron-technology-inc-stock/)

### 7.4 FCF가 이익을 뒷받침한다

FY3Q26 adjusted FCF는 183억달러였다. 회사는 FY4Q에도 FCF가 다시 크게 증가할 것으로 전망했다. [Micron 프레젠테이션](https://investors.micron.com/static-files/2354ecda-77a0-4ddd-8462-a631eb491356)

이 점은 중요하다. 메모리 호황에서 투자자는 종종 “좋은 이익이 모두 capex로 빨려 들어가는가”를 걱정한다. FY3Q에는 capex가 71억달러로 컸지만, 영업현금흐름 254억달러가 훨씬 컸다. 그래서 FCF가 남았다.

### 7.5 HBM 외 제품군도 고부가 전환 중이다

실적 발표는 245TB QLC SSD 출하, PCIe Gen6 SSD high-volume production, LP5X SOCAMM2 high-volume production, 1-gamma LPDDR5X ramp 등을 제시했다. [Micron FY3Q26 실적 발표](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html)

이것은 한국 투자자에게도 중요하다. 마이크론의 리레이팅이 HBM 하나에만 걸려 있으면 SK하이닉스·삼성전자와의 비교는 HBM 점유율 싸움이 된다. 그러나 데이터센터 SSD, SOCAMM, 고용량 DDR5, NAND shortage까지 같이 움직이면 한국 메모리 thesis도 “HBM 단일”에서 “AI memory hierarchy 전체”로 넓어진다.

## 8. 부정 신호와 리스크

### 8.1 주가가 이미 많이 반영했다

MarketBeat는 2026년 6월 24일 정규장 종가를 1,037.93달러, 장후 1,221.62달러로 표시했다. 같은 페이지 기준 장후 상승률은 +17.70%였다. 사용자가 제공한 StockAnalysis/finance 기준 장후 가격은 1,213.97달러, 상승률은 +15.78%다. [MarketBeat](https://www.marketbeat.com/earnings/reports/2026-6-24-micron-technology-inc-stock/)

데이터벤더별 장후 가격이 조금 다르지만 결론은 같다. 실적이 나온 뒤 주가는 이미 두 자릿수 급등했다. 정규장 종가 기준으로는 업사이드가 커 보이지만, 실적 정보가 반영된 가격 기준으로는 기대수익률이 낮아진다.

### 8.2 Capex 부담이 커진다

FY3Q capex, net은 71억달러였다. 회사는 FY4Q capex를 약 100억달러로 봤고, FY2026 전체 capex는 약 270억달러로 제시했다. FY2027에는 분기별 capex가 FY4Q 수준을 웃돌 수 있다고 설명했다. [Micron 프레젠테이션](https://investors.micron.com/static-files/2354ecda-77a0-4ddd-8462-a631eb491356)

MarketWatch도 CFO 발언을 인용해 FY4Q capex 약 100억달러, FY2026 capex 약 270억달러, FY2027 분기별 capex가 FY4Q보다 높아질 수 있다고 보도했다. [MarketWatch](https://www.marketwatch.com/livecoverage/micron-earnings-stock-results-memory-guidance/card/micron-s-spending-is-moving-higher-in-the-face-of-booming-demand-mLjzhU62y5AJfaUStOEC)

Capex가 나쁜 것은 아니다. 수요가 공급을 초과하기 때문에 투자가 필요하다. 하지만 주식 관점에서는 “좋은 이익이 좋은 현금흐름으로 남는가”가 계속 중요하다. FY2027 capex가 너무 커지고 가격 상승이 둔화되면 FCF와 자사주 매입 기대가 흔들릴 수 있다.

### 8.3 SCA는 floor이면서 cap일 수 있다

SCA의 floor price는 다운사이클 방어다. 하지만 일부 대형 계약에는 ceiling price도 들어간다. 회사는 largest agreements의 기존 제품 가격 상단이 current CQ2 market price에 가까운 구조라고 설명했다. [Micron 준비 발언](https://investors.micron.com/static-files/631b1a32-5537-46ae-8f40-82e42fc79dfe)

따라서 SCA는 “무조건 상방 옵션”이 아니다. 시장가격이 더 치솟으면 일부 upside는 제한될 수 있다. 대신 바닥 마진이 과거 피크 마진보다 높다는 회사 설명이 사실이라면, 메모리 cyclicality discount는 줄어든다.

### 8.4 공급 회복 시 pricing power가 먼저 훼손될 수 있다

Reuters 보도는 bull case의 핵심이 tightness라고 정리했다. 공급이 완화되면 가격 결정력이 먼저 훼손될 수 있다는 시장 코멘트도 포함했다. [The Star Reuters 보도](https://www.thestar.com.my/tech/tech-news/2026/06/25/micron-forecasts-strong-quarterly-results-on-soaring-memory-chip-demand)

이 리스크는 메모리 주식의 본질이다. SCA가 cyclicality를 낮춰도 제거하지는 못한다.

### 8.5 고급 메모리 대체 리스크

AI 칩 설계가 일부 워크로드에서 더 저렴한 메모리 구조를 쓰는 방향으로 움직이면, HBM과 premium DRAM의 가격 결정력은 제한될 수 있다. 아직 확인된 큰 훼손은 아니지만, AI accelerator 고객이 memory hierarchy를 어떻게 설계하는지는 FY2027 이후 핵심 리스크다.

## 9. 어닝콜과 Q&A 핵심

공식 준비 발언은 Micron IR에 공개됐다. Q&A는 공식 transcript가 아니라 MarketBeat/Quartr transcript를 참고했다. transcript는 웹 fallback이며, 숫자는 가능한 공식 발표와 준비 발언으로 교차 확인했다.

| 주제 | 질문자 | 답변자 | 핵심 내용 | 왜 중요한가 | 출처 |
|---|---|---|---|---|---|
| SCA floor 매출과 RPO | Timothy Arcuri, UBS | Sanjay Mehrotra, Mark Murphy | floor price 기준 약 1,000억달러 RPO는 최소 계약 가능 금액이고 실제 매출은 더 클 수 있음. 현재 체결분은 DRAM 20%, NAND 30%, 매출 약 25%에 가까운 범위 | SCA가 얼마나 실적을 고정하는지 시장이 가장 먼저 물었다 | MarketBeat/Quartr |
| SCA layering | Timothy Arcuri, UBS | Mark Murphy | FY3Q RPO 50억달러 초과, 다음 12개월 관련 매출 약 18억달러. FY4Q에는 14개 계약 기준 약 1,000억달러 RPO가 K에 공개될 예정 | FY2027 모델에 언제 반영할지 판단하는 핵심 | MarketBeat/Quartr |
| 고객 예치금 | Joseph Moore, Morgan Stanley | Mark Murphy | 220억달러 commitment 중 약 180억달러가 cash deposit. 선급 매출이 아니라 별도 commitment이며 financing cash flow로 처리 | FCF와 현금성 commitment를 구분해야 한다 | MarketBeat/Quartr |
| 예치금의 사용 가능성 | CJ Muse, Cantor Fitzgerald | Mark Murphy | cash deposit은 unrestricted. 다만 계약 이행 후 후반부에 고객에게 반환될 수 있음 | capex와 capital return에 얼마나 쓸 수 있는지 판단 | MarketBeat/Quartr |
| HBM 매출과 점유율 | CJ Muse, Cantor Fitzgerald | Sanjay Mehrotra | HBM4는 이미 10억달러 이상 출하. HBM share는 DRAM share에 가까운 수준을 전략적으로 추구 | HBM이 단발이 아니라 전략적 제품군인지 확인 | MarketBeat/Quartr |
| SCA와 장기 매출총이익률 | Vivek Arya, BofA Securities | Mark Murphy | FY4Q 이후 가이던스는 제공하지 않지만 tightness는 2027년 이후까지 이어질 것으로 봄. 가격 상승률은 둔화될 수 있음 | 86% 매출총이익률이 피크인지 지속 가능한지 시장이 봤다 | MarketBeat/Quartr |
| 2027 공급부족 | Krish Sankar, TD Cowen | Sanjay Mehrotra | 2027년에도 tight하고, 2028년 공급 개선이 시작돼도 수요도 계속 강할 것으로 봄 | 다음 멀티플은 FY2027 tightness 지속 여부에 달림 | MarketBeat/Quartr |

Q&A의 핵심은 EPS가 아니었다. 시장은 SCA가 얼마나 실적을 고정하는지, 예치금이 실제 현금으로 어떤 의미인지, 86% 매출총이익률이 지속 가능한지, HBM4가 얼마나 큰지, 2027년 공급부족이 계속되는지를 집요하게 물었다.

## 10. 주가 트리거

### 상방 트리거

| 트리거 | 확인 시점 | 주가 메커니즘 |
|---|---|---|
| FY4Q26 매출 510억달러 상단 초과 또는 EPS 32달러 초과 | 2026년 9월 FY4Q26 발표 | FY2027 EPS run-rate 재상향, forward P/E 부담 완화 |
| HBM3E/HBM4 2027 allocation 추가 고정, HBM4E qualification 가속 | FY4Q26 콜과 2026년 하반기 제품 업데이트 | 공급부족 기간이 길어질수록 매출총이익률 지속성에 프리미엄 부여 |
| SCA revenue coverage가 회사 매출 절반 이상에 가까워짐 | 다음 1~2개 분기 SCA 업데이트 | 메모리 cyclicality discount 축소 |
| FY4Q FCF 대폭 증가와 buyback 규모 명확화 | FY4Q26 발표와 10-K | EPS accretion, FCF yield 재평가 |
| Non-HBM DRAM/NAND pricing 강세 유지 | 분기 ASP와 segment margin 업데이트 | HBM 편중 우려 완화 |
| 데이터센터 매출 run-rate 1,000억달러 이상 유지 | FY4Q26과 FY2027 초 | Micron을 AI infrastructure beneficiary로 재분류 |

### 하방 트리거

| 트리거 | 확인 시점 | 주가 메커니즘 |
|---|---|---|
| FY4Q26 매출/EPS가 회사 가이던스 중간값 미달 | FY4Q26 발표 | 이번 beat and raise의 지속성 훼손 |
| 매출총이익률 86%에서 peak-out 신호 | FY4Q26과 FY2027 가이던스 | memory supercycle 멀티플 압축 |
| FY2027 capex가 FCF를 크게 잠식 | FY2026 10-K와 FY2027 capex guide | FCF multiple 하락, buyback 기대 약화 |
| SCA ceiling price가 upside를 제한한다는 증거 | 계약·마진 commentary | 장기계약이 floor보다 cap으로 해석될 위험 |
| AI 고객이 저가 메모리 구조로 이동 | AI accelerator 고객 제품 발표 | HBM·premium DRAM pricing power 축소 |
| 중국 메모리 업체의 고성능 제품 침투 | 2026년 하반기~2027년 | 공급 증가와 가격 경쟁 우려 |

## 11. 주가 반응

FY3Q26 실적은 2026년 6월 24일 16:01 ET, 즉 미국 정규장 마감 후 발표됐다. 따라서 정보가 완전히 반영되는 첫 정규 거래일은 2026년 6월 25일 미국장이다. 이 글의 평가 시점 2026년 6월 25일 13:59 KST에는 미국 정규장이 아직 열리지 않았기 때문에 1D, 2D, 5D 정규장 이벤트 수익률은 산출하지 않는다.

| 구분 | MU 수익률 또는 가격 | 해석 | 출처 |
|---|---:|---|---|
| 2026-06-24 정규장 | 1,048.51달러, -0.31% | 발표 전 정규장 움직임. 이벤트 반응으로 보기는 어렵다. | 사용자 제공 StockAnalysis/finance 기준 |
| 2026-06-24 MarketBeat 정규장 종가 | 1,037.93달러, -1.32% | 데이터벤더별 차이 존재 | MarketBeat |
| 2026-06-24 장후 | 1,213.97달러, +15.78% | 사용자 제공 기준 장후 반응 | 사용자 제공 StockAnalysis/finance 기준 |
| 2026-06-24 MarketBeat 장후 | 1,221.62달러, +17.70% | MarketBeat 기준 04:50 AM ET 표시 | MarketBeat |
| 1D 정규장 | 산출 대기 | 2026-06-25 미국장 종료 후 가능 | not available |
| 2D 정규장 | 산출 대기 | 2026-06-26 미국장 종료 후 가능 | not available |
| 5D 정규장 | 산출 대기 | 다음 주 중 가능 | not available |

반응을 만든 것은 단순 EPS beat만이 아니다. 더 큰 트리거는 FY4Q 500억달러 매출 가이던스, 31달러 EPS 가이던스, 16개 SCA, 220억달러 commitment, 2027년 이후까지 이어질 공급부족, 그리고 FY4Q FCF 추가 증가 가능성이다.

## 12. 투자의견과 목표가

### 결론

| 항목 | 판단 |
|---|---|
| 투자의견 | HOLD / 보유 유지 |
| 신규 진입 | 조정 대기 |
| 수정 12개월 목표가 | 1,350달러 |
| 기준가격 | 장후 1,213.97달러 기준 |
| 상승여력 | 약 +11.2% |
| 정규장 종가 기준 업사이드 | 약 +28.8%, 다만 실적 정보가 미반영된 가격이라 보수적으로 보지 않는다 |

### 밸류에이션 프레임

밸류에이션은 forward P/E를 사용한다.

FY2026 Non-GAAP EPS 중간값은 Q1 4.78달러, Q2 12.20달러, Q3 25.11달러, Q4 가이던스 중간값 31.00달러를 더해 73.09달러다. Q4 가이던스는 회사 공식 자료 기준이다. Q1과 Q2는 사용자 제공 분석의 이전 분기 데이터이며, FY3Q와 FY4Q는 이번 공식 발표 기준이다.

기준 시나리오는 FY2027 EPS 약 100달러를 적용한다. FY4Q26 EPS run-rate보다 보수적으로 낮춘 숫자다. 이유는 FY2027 capex, startup cost, 가격 정상화 리스크를 반영하기 위해서다. 기준 멀티플은 13.5배다. SCA가 cyclicality를 낮추는 점은 프리미엄 요인이지만, 메모리 산업의 공급 회복과 가격 리스크는 할인 요인이다.

| 시나리오 | EPS 가정 | 멀티플 | 목표가 범위 | 핵심 조건 |
|---|---:|---:|---:|---|
| Bear | 70~80달러 | 11~12배 | 800~950달러 | 공급 완화, ASP 하락, capex·FCF 압박 |
| Base | 약 100달러 | 13.5배 | 1,350달러 | FY4Q 가이던스 달성, HBM/SCA 견조, FCF 유지 |
| Bull | 110~120달러 | 15배 | 1,650~1,800달러 | 2027년 supply sold-out 확대, buyback 본격화, SCA coverage 증가 |

### 의견 변경 조건

| 변경 | 조건 |
|---|---|
| BUY로 상향 | 주가가 1,100달러 이하로 조정되거나, FY4Q26에서 매출 510억달러 이상과 EPS 32달러 이상이 확인되고 FY2027 capex 대비 FCF visibility가 유지될 때 |
| SELL 또는 감축 | 매출총이익률이 80% 아래로 빠르게 훼손되거나, HBM4/HBM4E qualification 지연, SCA 추가 체결 부진, 고객의 저가 메모리 대체가 확인될 때 |
| 목표가 상향 | SCA로 묶인 매출 비중이 절반 이상으로 올라가고 FY2027 EPS visibility가 110달러 이상으로 올라갈 때 |
| 목표가 하향 | FY2027 capex가 현금환원을 실질적으로 제약하고, FY4Q FCF 대폭 증가가 달성되지 않을 때 |

## 13. 다음 실적 프리뷰

FY4Q26 공식 발표일은 아직 확인되지 않았다. 데이터벤더 예상은 엇갈린다.

| 항목 | 일정 | 확정성 | 코멘트 |
|---|---|---|---|
| FY4Q26 실적 발표 | 공식 미확정 | 미확정 | Micron IR에는 아직 날짜가 보이지 않는다. |
| 데이터벤더 예상 1 | 2026-09-22 | 예상 | Public.com 기준 사용자 제공 분석 |
| 데이터벤더 예상 2 | 2026-09-23 after market | inferred | Wall Street Horizon 기준 사용자 제공 분석 |
| 데이터벤더 예상 3 | 2026-09-29 | 예상 | Investing.com 기준 사용자 제공 분석 |

공식 확정 전까지는 “2026년 9월 하순 미국장 장후 가능성” 정도만 신뢰한다. 발표가 미국장 장후라면 KST로는 보통 다음날 새벽 5시 전후가 된다. 하지만 공식 시간대가 나오기 전에는 KST 시각을 확정하지 않는다.

## 14. 다음 분기 핵심 쟁점

1. FY4Q26 매출 500억달러와 EPS 31달러가 실제로 달성되는가.
2. HBM3E/HBM4가 2027년까지 fully booked 상태를 유지하고, HBM4E qualification이 계획대로 진행되는가.
3. SCA가 실제 revenue visibility를 얼마나 높이며, 가격 floor가 margin downside를 얼마나 방어하는가.
4. FY2027 capex가 mid-40B dollar range를 넘어갈 때도 FCF와 buyback 여력이 유지되는가.
5. Non-HBM DRAM/NAND 가격 강세가 HBM 외 포트폴리오에서도 지속되는가.
6. AI 고객들이 메모리 용량과 대역폭 요구를 계속 높이는가, 아니면 저가 메모리 구조로 이동하는가.
7. 중국 메모리 업체와 대형 고객의 협상력이 Micron의 pricing power를 훼손하지 않는가.

## 15. 한국 반도체로의 파급 신호

마이크론 실적은 삼성전자·SK하이닉스에 직접 비교 기준이 된다. 이번 분기의 핵심은 마이크론이 단순히 “미국 메모리 proxy”로 비싸진 것이 아니라, 실제 숫자로 그 프리미엄을 방어했다는 점이다.

| 한국 관점 질문 | 이번 마이크론 실적의 답 |
|---|---|
| 삼성전자·SK하이닉스의 EPS 훼손 우려가 커졌나 | 아니다. 마이크론 실적은 DRAM·NAND·HBM·SSD 가격과 수요가 여전히 강하다는 신호다. |
| 마이크론 프리미엄은 정당화됐나 | 일부 정당화됐다. Non-GAAP 매출총이익률 84.9%, FY4Q 86% 가이던스, SCA 구조는 commodity memory discount를 낮춘다. |
| SK하이닉스 독점 프리미엄은 약해지나 | 마이크론 HBM4 매출과 SCA는 경쟁 강도를 높인다. 하지만 HBM 전체 TAM이 커지는 효과도 크다. |
| 삼성전자 catch-up에는 어떤 의미인가 | 마이크론이 HBM4와 SCA로 리레이팅을 받는다면, 삼성전자는 HBM4E·DS margin·고객 allocation을 증명해야 할인 축소가 가능하다. |
| 한국 소부장에는 어떤 의미인가 | HBM, SSD, SOCAMM, 고용량 DDR5, 테스트·패키징·전력 안정화 수요가 지속될 가능성을 높인다. |

마이크론이 강할수록 한국 메모리의 상대 PER 할인 논리는 단순해지지 않는다. 한편으로는 “미국 상장 AI 메모리 proxy가 숫자로 프리미엄을 증명했다”는 의미다. 다른 한편으로는 “한국 메모리도 EPS가 훼손되지 않았다면 마이크론 대비 할인 폭이 과도할 수 있다”는 의미다.

따라서 한국 투자자에게 다음 체크포인트는 명확하다.

1. SK하이닉스가 HBM4/HBM4E allocation과 ASP를 방어하는가.
2. 삼성전자가 HBM4E qualification과 DS margin 회복을 보여주는가.
3. 메모리 본주가 쉬는 동안 테스트·검사·기판·패키징 소부장으로 수급이 확산되는가.
4. 마이크론의 SCA 모델이 삼성전자·SK하이닉스에도 비슷한 장기계약 구조로 번지는가.

## 16. 데이터와 출처

| 자료 | 사용 내용 |
|---|---|
| [Micron FY3Q26 공식 실적 발표](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html) | 실적표, GAAP/Non-GAAP 수치, segment revenue, FY4Q26 가이던스, FCF reconciliation, 제품 업데이트 |
| [Micron Quarterly Results](https://investors.micron.com/quarterly-results) | FY3Q26 프레젠테이션, 준비 발언, 발표 자료 위치 확인 |
| [Micron FY3Q26 프레젠테이션](https://investors.micron.com/static-files/2354ecda-77a0-4ddd-8462-a631eb491356) | 데이터센터 run-rate, SCA 구조, capex, 제품·시장 전망, FY4Q guidance |
| [Micron FY3Q26 준비 발언](https://investors.micron.com/static-files/631b1a32-5537-46ae-8f40-82e42fc79dfe) | supply tightness, SCA 세부, HBM4 매출, DRAM/NAND pricing, FY2027 capex commentary |
| [MarketBeat/Quartr transcript](https://www.marketbeat.com/earnings/reports/2026-6-24-micron-technology-inc-stock/) | Q&A, 장후 가격, MarketBeat 컨센서스, transcript web fallback |
| [Reuters 보도, The Star](https://www.thestar.com.my/tech/tech-news/2026/06/25/micron-forecasts-strong-quarterly-results-on-soaring-memory-chip-demand) | 220억달러 customer commitments, 공급부족, AI HBM 수요, 시장 코멘트 |
| [Reuters 보도, Investing.com](https://m.investing.com/news/stock-market-news/micron-forecasts-quarterly-revenue-above-estimates-4758884?ampMode=1) | FY4Q 매출 가이던스와 LSEG 평균 예상 비교 |
| [MarketWatch capex 보도](https://www.marketwatch.com/livecoverage/micron-earnings-stock-results-memory-guidance/card/micron-s-spending-is-moving-higher-in-the-face-of-booming-demand-mLjzhU62y5AJfaUStOEC) | FY4Q capex, FY2026 capex, FY2027 capex 방향 |
| [MarketWatch supply tightness 보도](https://www.marketwatch.com/livecoverage/micron-earnings-stock-results-memory-guidance/card/micron-has-no-clue-when-memory-supply-will-finally-catch-up-with-demand-cKcl56PcCiQzIAvLYTnx) | 2027년 이후 tightness와 greenfield fab 제약 |

## 17. 한계와 면책

1. 정규장 1D, 2D, 5D 이벤트 수익률은 아직 산출하지 않았다. 발표가 미국장 장후였고, 평가 시점에는 2026년 6월 25일 미국 정규장이 열리기 전이었다.
2. FY4Q26 공식 발표일은 미확정이다. 데이터벤더 예상일이 9월 22일, 9월 23일 장후, 9월 29일로 엇갈린다.
3. 컨센서스 데이터는 공급자별로 차이가 있다. 본문에서는 Reuters/LSEG, Investing.com, MarketBeat, 사용자 제공 데이터를 병기했다.
4. MarketBeat/Quartr transcript는 공식 회사 transcript가 아니라 web fallback이다. Q&A 숫자는 가능한 공식 발표와 준비 발언으로 교차 확인했다.
5. 목표가는 개인 맞춤형 투자자문이 아니다. 실제 투자 판단은 리스크 허용도, 환율, 세금, 포트폴리오, 투자기간을 반영해야 한다.
6. Micron은 메모리 산업 특성상 가격, 재고, capex cycle에 민감하다. SCA가 cyclicality를 낮추더라도 제거하지는 못한다.

## 18. Machine-readable Summary

```json
{
  "as_of_kst": "2026-06-25 13:59",
  "company": {
    "name": "Micron Technology, Inc.",
    "ticker": "MU",
    "exchange": "NASDAQ",
    "currency": "USD"
  },
  "recent_earnings_release": {
    "release_datetime_kst": "2026-06-25 05:01",
    "confirmed": true
  },
  "recent_call": {
    "exists": true,
    "call_datetime_kst": "2026-06-25 05:30"
  },
  "upcoming_earnings_release": {
    "release_datetime_kst": null,
    "confirmed": false
  },
  "upcoming_call": {
    "exists": false,
    "call_datetime_kst": null,
    "confirmed": false
  },
  "recommendation": {
    "rating": "HOLD",
    "target_price": 1350,
    "horizon_months": 12,
    "upside_pct": 11.2
  },
  "key_triggers_up": [
    "FY4Q26 revenue above $51B or non-GAAP EPS above $32",
    "Additional FY2027 HBM3E/HBM4 allocation locked in",
    "SCA revenue coverage approaches half or more of company revenue",
    "FY4Q free cash flow rises sharply and buyback scale becomes explicit",
    "Non-HBM DRAM and NAND pricing remains strong"
  ],
  "key_triggers_down": [
    "FY4Q26 results miss the midpoint of company guidance",
    "Gross margin rolls over materially from the 86% guide",
    "FY2027 capex reduces free cash flow and limits buybacks",
    "SCA ceiling prices cap upside more than floor prices protect downside",
    "AI customers shift toward cheaper memory architectures",
    "Supply catches up earlier than expected and pricing power weakens"
  ],
  "key_watch_items_next_release": [
    "FY4Q26 revenue and EPS versus guidance",
    "Gross margin sustainability above 86%",
    "HBM4 and HBM4E qualification and booking status",
    "Strategic Customer Agreement coverage and remaining performance obligations",
    "FY2027 capex and free cash flow outlook",
    "Share repurchase plan and capital return cadence"
  ]
}
```

## 19. 드러켄밀러식 코멘트

1. 이건 평범한 메모리 사이클 반등이 아니라, AI 인프라 병목에 붙은 가격결정력이다.
2. 숫자는 훌륭하다. 특히 EPS보다 중요한 것은 매출총이익률과 FCF의 질이다.
3. 다만 시장은 이미 그 사실을 알아챘고, 장후 급등으로 안전마진은 줄었다.
4. SCA는 Micron을 과거의 순수 commodity memory보다 나은 사업으로 만든다.
5. 그래도 공급이 늘면 메모리 주식은 다시 잔인해질 수 있다.
6. 지금 매수 논리는 “수요가 계속 과소추정되고 있다”는 데 달려 있다.
7. Capex가 너무 커지면 좋은 이익이 나쁜 현금흐름으로 바뀔 수 있다.
8. 그래서 추격매수보다 보유와 조정 매수가 더 합리적이다.
9. 다음 승부처는 FY4Q 실적 그 자체보다 FY2027 공급, 계약, FCF visibility다.
10. 이 주식은 싸서 사는 주식이 아니다. 숫자가 계속 올라갈 때만 살 수 있는 주식이다.
