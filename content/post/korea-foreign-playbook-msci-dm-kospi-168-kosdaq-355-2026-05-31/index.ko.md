---
title: "외국인 플레이북 KOSPI 168·KOSDAQ 355: MSCI DM 편입은 한국 전체보다 Quality에 온다"
slug: korea-foreign-playbook-msci-dm-kospi-168-kosdaq-355-2026-05-31
date: 2026-05-31T23:45:00+09:00
description: "2026년 YTD 외국인 순매수 proxy로 KOSPI 168개, KOSDAQ 355개 핵심 거래대상을 분류하고 MSCI EM→DM 전환 효과가 왜 한국 전체보다 AI memory, 주주환원 금융, 조선·방산·전력기기 같은 DM long-only가 이해하는 quality 바스켓에 집중될지 분석한다."
categories: ["Korea Market", "Macro-Insight", "Market Structure"]
tags:
  - "외국인 수급"
  - "KOSPI"
  - "KOSDAQ"
  - "MSCI"
  - "DM 편입"
  - "한국증시"
  - "삼성전자"
  - "SK하이닉스"
  - "외국인 플레이북"
  - "Korea rerating"
series: ["korea-rerating-2026", "macro-gates-2026"]
draft: false
---

> 이 글은 [한국증시 외국인 수급 분석](/ko/post/korea-foreign-investor-flow-memory-megacap-rotation-2026-05-24/), [KOSPI 외국인 지분율 vs 삼성전자·SK하이닉스](/ko/post/korea-foreign-ownership-kospi-samsung-hynix-divergence-2026-05-26/), [한국 ADR 67과 KOSPI·KOSDAQ 브레드스](/ko/post/korea-adr-breadth-narrow-leadership-kospi-kosdaq-2026-05-27/)의 후속편이다. 앞선 글들이 외국인이 얼마나 팔았는지와 평균 종목의 약세를 봤다면, 이번 글은 더 근본적인 질문을 던진다. <strong>외국인이 실제로 거래대상으로 보는 한국 주식은 몇 개인가?</strong>

## TL;DR

* <strong>KOSPI는 외국인 거래대상이 극단적으로 압축</strong>돼 있다. Research OS local DB 기준 2026년 1월 2일~5월 29일 외국인 활동 proxy의 <strong>73.9%가 42개 A Core 종목</strong>에 몰렸고, A+B <strong>168개가 94.4%</strong>를 차지했다.
* <strong>KOSDAQ은 더 넓지만 질은 낮다.</strong> 88개 A Core가 외국인 활동의 <strong>55.6%</strong>, A+B 355개가 <strong>84.5%</strong>를 차지했다. 바이오, 반도체 장비, 로봇, 2차전지, 광통신 테마 회전 성격이 KOSPI보다 강하다.
* MSCI DM 편입은 아직 확정된 이벤트가 아니다. MSCI는 2025년 시장분류 리뷰에서 한국을 Developed Market으로 올리지 않았고, 한국 시장 접근성 개선 조치의 실제 효과를 계속 모니터링하겠다고 밝혔다. ([MSCI](https://www.msci.com/downloads/documents/press-releases/media-room/MSCI%20Announces%20Results%20of%20the%20MSCI%202025%20Market%20Classification%20Review.pdf))
* 다만 DM 편입이 언젠가 현실화되더라도 수혜는 한국 전체가 아니라 <strong>외국인 플레이북에 이미 올라온 Quality 바스켓</strong>으로 압축될 가능성이 높다. 핵심 후보는 주주환원 금융, 조선, 방산, 전력기기, 글로벌 산업재/NAV, AI memory와 AI 부품이다.
* 실전 결론은 단순하다. “외국인이 사느냐/파느냐”보다 먼저 봐야 할 것은 <strong>그 종목이 외국인 플레이북에 올라와 있는가</strong>다. KOSPI 168개, KOSDAQ 355개 밖의 종목은 외국인 long-only 리레이팅보다 국내 테마·개인 유동성 장세로 분리해서 봐야 한다.

데이터 기준은 Research OS local DB다. 기간은 <strong>2026-01-02~2026-05-29</strong>, 원천은 `investor_flow_raw_daily`, `prices_daily`, `kr_fundamentals_daily`다. 중요한 주의점이 있다. 로컬 DB는 외국인 총매수+총매도 gross 거래대금이 아니라 외국인 순매수금액 중심이다. 따라서 본문에서는 `sum(abs(외국인 순매수금액))`을 <strong>외국인 거래 관심도의 보수적 proxy</strong>로 사용했다.

## 1. MSCI DM 편입은 아직 확정이 아니라 옵션이다

한국의 MSCI Developed Market 편입은 오래된 이야기다. 하지만 2026년 5월 31일 현재 한국은 여전히 MSCI Emerging Market이다. MSCI의 2025년 시장분류 리뷰도 한국에 대해 결론을 내리지 않고, 외환시장 접근성, 외국인 투자자 등록·옴니버스 계좌, 장외거래 사후보고, 투자상품 접근성, 공매도·대차·결제 안정성 등을 계속 평가하겠다는 입장을 냈다. ([MSCI Market Classification](https://www.msci.com/indexes/index-resources/market-classification))

따라서 “MSCI DM 편입 = 곧 대규모 패시브 자금 유입”으로 단순화하면 위험하다. 더 정확한 표현은 이렇다.

> MSCI DM 편입은 한국 주식시장의 할인율을 낮출 수 있는 장기 옵션이다. 하지만 그 옵션의 실제 수혜는 시장 전체가 아니라, 글로벌 long-only가 이미 이해하고 거래할 수 있는 종목으로 먼저 압축된다.

왜냐하면 한국은 이미 AI memory를 통해 글로벌 포트폴리오 안에 깊숙이 들어와 있기 때문이다. MSCI EM Index의 2026년 4월 말 기준 상위 구성종목에는 삼성전자 <strong>6.03%</strong>, SK하이닉스 <strong>4.05%</strong>가 들어간다. ([MSCI EM Index](https://www.msci.com/indexes/index/891800)) MSCI Korea Index에서는 삼성전자 <strong>32.24%</strong>, SK하이닉스 <strong>21.68%</strong>가 합산 절반을 넘는다. ([MSCI Korea Index](https://www.msci.com/indexes/index/941000))

즉 AI memory 랠리는 이미 DM 편입의 “예고편”처럼 일부 작동했다. 문제는 그 힘이 너무 좁게, 너무 강하게 삼성전자와 SK하이닉스에 먼저 붙었다는 점이다.

## 2. 시장별 큰 그림

| 시장 | 종목 수 | 외국인 abs 순매수 proxy | 외국인 순매수 | 전체 거래대금 | 외국인 활동/거래대금 |
|---|---:|---:|---:|---:|---:|
| KOSPI | 835 | 38.2조원 | -9.95조원 | 319.1조원 | 12.0% |
| KOSDAQ | 1,776 | 10.9조원 | +0.44조원 | 137.9조원 | 7.9% |

해석은 명확하다.

KOSPI는 외국인이 많이 거래했지만 순매도다. 특히 삼성전자, SK하이닉스, 현대차 등 이미 크게 오른 글로벌 대형주에서 차익실현이 컸다. 반면 KOSDAQ은 외국인 활동 규모는 작지만 순매수다. 이는 “외국인이 한국을 다 팔았다”가 아니라 <strong>KOSPI 초대형주를 줄이고, 일부 KOSDAQ 성장·테마주를 산 구조</strong>에 가깝다.

## 3. 외국인 거래대상 분류

분류 기준은 다음과 같다.

| 분류 | 기준 |
|---|---|
| A Core | 시장별 외국인 abs 순매수 proxy 상위 5%, 외국인 활동일수 80% 이상 |
| B Active | 시장별 상위 20%, 외국인 활동일수 70% 이상 |
| C Peripheral | 중간권, 이벤트성 거래 가능 |
| D Non-target | 외국인 거래대상 아님 |

결과는 KOSPI와 KOSDAQ이 완전히 다르다.

| 시장 | 분류 | 종목 수 | 외국인 활동 규모 | 시장 내 비중 |
|---|---|---:|---:|---:|
| KOSPI | A Core | 42 | 28.2조원 | 73.9% |
| KOSPI | B Active | 126 | 7.8조원 | 20.5% |
| KOSPI | C Peripheral | 250 | 1.8조원 | 4.7% |
| KOSPI | D Non-target | 417 | 0.3조원 | 0.8% |
| KOSDAQ | A Core | 88 | 6.1조원 | 55.6% |
| KOSDAQ | B Active | 267 | 3.1조원 | 28.9% |
| KOSDAQ | C Peripheral | 530 | 1.4조원 | 12.4% |
| KOSDAQ | D Non-target | 891 | 0.3조원 | 3.0% |

KOSPI는 <strong>A+B 168개 종목이 외국인 활동의 94.4%</strong>를 차지한다. KOSDAQ도 A+B 355개가 84.5%다. 결국 올해 한국장은 외국인이 빠진 장이라기보다, <strong>외국인이 보는 종목과 안 보는 종목의 격차가 더 커진 장</strong>이다.

## 4. KOSPI 외국인 핵심 거래대상

순매수/순매도 방향과 무관하게 외국인이 실제로 만지는 KOSPI 종목은 다음이다.

| 순위 | 종목 | 외국인 활동 | 외국인 순매수 | YTD | 해석 |
|---:|---|---:|---:|---:|---|
| 1 | 삼성전자 | 9.26조원 | -5.18조원 | +146.7% | 외국인 최대 거래대상, 대규모 차익실현 |
| 2 | SK하이닉스 | 6.42조원 | -3.74조원 | +244.6% | AI memory 핵심이나 차익실현 압도 |
| 3 | 현대차 | 1.52조원 | -0.96조원 | +142.2% | 글로벌 auto long-only 대상이나 매도 |
| 4 | 두산에너빌리티 | 0.84조원 | +0.21조원 | +40.4% | 원전·전력·터빈 theme로 매수 |
| 5 | 삼성SDI | 0.47조원 | +0.14조원 | +162.1% | 2차전지 반등 beta |
| 6 | 현대모비스 | 0.45조원 | -0.33조원 | +108.1% | 거래는 많지만 외국인 매도 |
| 7 | SK스퀘어 | 0.44조원 | -0.24조원 | +214.5% | SK하이닉스 proxy 차익실현 |
| 8 | 한화에어로스페이스 | 0.44조원 | +0.05조원 | +24.0% | 방산 core |
| 9 | 삼성전기 | 0.43조원 | -0.01조원 | +687.8% | AI 부품 crowded |
| 10 | 한미반도체 | 0.39조원 | -0.01조원 | +95.2% | HBM 장비 core |

이 표의 핵심은 순매도 종목을 무조건 나쁘게 보면 안 된다는 점이다. 삼성전자, SK하이닉스, 현대차는 외국인이 팔았지만 여전히 글로벌 장부의 핵심 종목이다. 반대로 외국인이 아예 거래하지 않는 종목은 좋은 스토리가 있어도 글로벌 long-only 리레이팅을 기대하기 어렵다.

KOSPI에서 외국인이 보는 테마는 여섯 가지다.

| 테마 | 대표 종목 |
|---|---|
| AI / 반도체 / 기판 | 삼성전자, SK하이닉스, 삼성전기, 한미반도체, 이수페타시스 |
| 자동차 | 현대차, 기아, 현대모비스 |
| 금융 / 지주 / 주주환원 | KB금융, 신한지주, 삼성화재, 삼성물산, HD현대 |
| 전력기기 / 전선 | HD현대일렉트릭, LS ELECTRIC, 효성중공업, 대한전선, 산일전기 |
| 방산 / 조선 | 한화에어로스페이스, 한화오션, HD현대중공업, 현대로템, LIG넥스원 |
| 2차전지 | 삼성SDI, LG에너지솔루션, POSCO홀딩스, 포스코퓨처엠 |

삼성전자·하이닉스 매도만으로 외국인 이탈을 해석하면 틀린다. 외국인은 동시에 두산에너빌리티, 한화오션, 현대로템, POSCO홀딩스, 셀트리온, 두산, 두산로보틱스, 현대건설, 산일전기 같은 다른 종목을 샀다.

## 5. KOSDAQ 외국인 핵심 거래대상

KOSDAQ은 KOSPI보다 더 넓지만, 더 테마 회전적이다.

| 순위 | 종목 | 외국인 활동 | 외국인 순매수 | YTD | 해석 |
|---:|---|---:|---:|---:|---|
| 1 | 에코프로 | 2,725억원 | +284억원 | +57.4% | 2차전지 beta |
| 2 | 우리기술 | 2,620억원 | -149억원 | +307.2% | 원전·전력 테마, 거래는 크나 순매도 |
| 3 | 에이비엘바이오 | 2,163억원 | -14억원 | -42.8% | 바이오 core trading |
| 4 | 알테오젠 | 2,046억원 | +149억원 | -19.3% | 바이오 대장, 외국인 지속 거래 |
| 5 | 레인보우로보틱스 | 1,910억원 | +88억원 | +42.2% | 로봇 대표주 |
| 6 | 삼천당제약 | 1,691억원 | +462억원 | +38.7% | 바이오 매수 강함 |
| 7 | 에코프로비엠 | 1,637억원 | +503억원 | +53.1% | 2차전지 매수 |
| 8 | 리노공업 | 1,580억원 | -802억원 | +50.1% | 반도체 quality 매도 |
| 9 | 대한광통신 | 1,554억원 | -191억원 | +746.1% | 광통신 테마 |
| 10 | HPSP | 1,471억원 | +401억원 | +41.2% | 반도체 장비 매수 |

KOSDAQ에서 외국인이 보는 것은 바이오 대장, 반도체 장비·기판, 로봇, 2차전지, 광통신이다. 알테오젠, 삼천당제약, 에코프로비엠, HPSP, 하나마이크론, 심텍, 파두, 제주반도체, 리노공업, ISC는 외국인 플레이북 안에 들어와 있다.

다만 KOSDAQ은 KOSPI보다 “quality long-only” 성격이 약하다. 외국인이 거래하더라도 장기 보유보다 이벤트·테마·유동성 회전이 섞이는 경우가 많다. 그래서 KOSDAQ A/B는 외국인 관심의 증거이지만, 곧바로 DM long-only core라는 뜻은 아니다.

## 6. D group은 왜 조심해야 하나

외국인 거래대상이 아닌 D group의 특징은 다음이다.

| 시장 | D group 종목 수 | 외국인 활동 비중 | 중앙값 YTD | 중앙값 거래대금 | 중앙값 외국인 활동 |
|---|---:|---:|---:|---:|---:|
| KOSPI | 417 | 0.8% | -6.2% | 561억원 | 65억원 |
| KOSDAQ | 891 | 3.0% | -8.0% | 355억원 | 33억원 |

D group은 가격이 오르더라도 외국인 제도권 장부에 올라온 상승이 아니다. 개인, 국내 테마, 단기 세력 유동성에 가까운 경우가 많다. 단기 매매는 가능하지만, MSCI DM 편입, 해외 접근성 개선, 글로벌 long-only 유입 같은 논리와는 분리해서 봐야 한다.

예를 들어 KOSDAQ에서 YTD 급등했지만 외국인 대상이 아닌 종목도 많다. 이런 종목은 수익률은 강할 수 있지만, “외국인이 한국을 재평가하고 있다”는 증거로 쓰면 안 된다.

## 7. DM long-only가 가장 쉽게 살 바스켓

MSCI DM 편입이 실제로 가까워지거나, 해외 증권사 접근성이 더 열릴 때 가장 먼저 움직일 가능성이 높은 종목은 “한국 테마주”가 아니다. 글로벌 PM이 한 문장으로 설명할 수 있는 종목이다.

| 분류 | Core 후보 | 한 줄 설명 |
|---|---|---|
| 주주환원 금융 | 삼성화재, KB금융 | 밸류업, 배당, 자사주, ROE를 설명하기 쉽다. |
| 조선 | HD현대중공업, 한화오션, HD한국조선해양 | 글로벌 수주, LNG·함정·미국 조선 협력, 턴어라운드가 명확하다. |
| 방산 | LIG넥스원 | 미사일·레이더·수출 방산 pure quality로 설명 가능하다. |
| 글로벌 산업재/NAV | 삼성물산, HD현대 | 그룹 NAV 할인 축소와 주주환원, 조선·전력기기 exposure가 있다. |

반대로 설명은 쉽지만 이미 crowded한 바스켓도 있다.

| 분류 | Pullback 후보 | 판단 |
|---|---|---|
| 전력기기 | HD현대일렉트릭, 효성중공업, LS ELECTRIC | AI data center 전력망 thesis는 선명하지만 valuation과 차익실현 부담이 크다. |
| AI 부품 | 삼성전기, LG이노텍 | 스토리는 강하지만 급등 후 신규 진입 효율은 낮다. |
| 자동차 | 현대차, 현대모비스 | 글로벌 quality지만 외국인 차익실현 부담이 남아 있다. |

이 구분이 중요한 이유는 MSCI DM 편입이 “모든 한국 주식을 사는 이벤트”가 아니기 때문이다. 실제 DM long-only는 유동성, 회계 투명성, 영어 disclosure, governance, 배당, 산업 설명 가능성, peer 비교 가능성을 본다. 이 조건을 통과하는 종목은 많지 않다.

## 8. 실전 적용법

한국 주식을 볼 때 순서는 이렇게 잡는 편이 낫다.

| 순서 | 질문 | 해석 |
|---:|---|---|
| 1 | A/B foreign target인가? | 아니면 외국인 리레이팅 논리를 우선 배제한다. |
| 2 | 외국인 순매수인가, 순매도인가? | 순매수면 accumulation, 순매도면 차익실현·리밸런싱일 수 있다. |
| 3 | 외국인 활동이 가격 상승과 같이 가는가? | 같이 가면 주도주 가능성이 높다. 반대로 가면 손바뀜을 봐야 한다. |
| 4 | 외국인 매도에도 가격이 버티는가? | 버티면 국내 기관·개인의 흡수력을 확인할 수 있다. |
| 5 | D group 급등주인가? | long-only 리레이팅과 단기 테마 매매를 분리한다. |

이 프레임으로 보면 NAVER 같은 소외 대형 플랫폼도 다시 보인다. NAVER는 KOSPI A Core에 들어와 있지만 YTD -5.3%로 주도주 랠리에서 빠져 있었다. 그래서 [NAVER 리레이팅 가능성](/ko/post/naver-rerating-dunamu-mirae-ai-cloud-stablecoin-turnaround-2026-05-31/)은 단순 포털주가 아니라 “외국인 플레이북 안에 있는 소외 성장 플랫폼” 관점에서 봐야 한다.

## 9. 최종 판단

MSCI DM 편입은 한국 시장 전체의 할인율을 낮출 수 있는 장기 옵션이다. 하지만 이미 2026년 한국장은 그 옵션이 얼마나 선별적으로 작동할지를 보여줬다. AI memory는 먼저 폭발했고, 외국인은 그 안에서 차익실현했다. 동시에 조선, 방산, 전력기기, 주주환원 금융, 일부 KOSDAQ 성장주로 자금을 재배치했다.

따라서 다음 문장이 이번 글의 결론이다.

> 한국 리레이팅의 다음 단계는 “외국인이 한국을 사느냐”가 아니라 “외국인이 살 수 있는 한국 종목이 무엇인가”다.

KOSPI 168개와 KOSDAQ 355개는 그 질문에 대한 실무적 답이다. 그 밖의 종목은 나쁘다는 뜻이 아니다. 다만 외국인 long-only 리레이팅, MSCI DM 편입, 해외 증권사 접근성 개선이라는 논리를 붙이려면 먼저 외국인 플레이북에 올라와 있어야 한다.

## Evidence Ledger

| 항목 | 출처 | 확인 내용 |
|---|---|---|
| 외국인 A/B 대상 분류 | Research OS local DB, `investor_flow_raw_daily`, `prices_daily`, `kr_fundamentals_daily`, 2026-05-31 접근 | 2026-01-02~2026-05-29 기준 KOSPI 168개, KOSDAQ 355개 A/B foreign target 산출 |
| 로컬 산출물 | `Thesis OS generated foreign-trading-targets output` | 전체 Markdown, KOSPI 168 CSV, KOSDAQ 355 CSV 생성 확인 |
| MSCI Korea 접근성 | [MSCI 2025 Market Classification Review](https://www.msci.com/downloads/documents/press-releases/media-room/MSCI%20Announces%20Results%20of%20the%20MSCI%202025%20Market%20Classification%20Review.pdf) | 한국 시장 접근성 개선 조치 모니터링 지속, 2025년 DM 재분류 없음 |
| MSCI EM 구성 | [MSCI EM Index](https://www.msci.com/indexes/index/891800) | 2026년 4월 말 기준 삼성전자 6.03%, SK하이닉스 4.05% |
| MSCI Korea 구성 | [MSCI Korea Index](https://www.msci.com/indexes/index/941000) | 2026년 4월 말 기준 삼성전자 32.24%, SK하이닉스 21.68% |

## Fact / Inference / Blocked

### [Fact]

* KOSPI는 835개 종목 중 A Core 42개가 외국인 활동 proxy의 73.9%, A+B 168개가 94.4%를 차지했다.
* KOSDAQ은 1,776개 종목 중 A Core 88개가 외국인 활동 proxy의 55.6%, A+B 355개가 84.5%를 차지했다.
* MSCI는 2025년 시장분류 리뷰에서 한국을 Developed Market으로 재분류하지 않았고, 시장 접근성 개선 조치의 효과를 계속 모니터링한다고 밝혔다.

### [Inference]

* MSCI DM 편입 수혜는 한국 전체보다 외국인 플레이북에 이미 올라온 대형 quality·글로벌 산업재·주주환원·AI infra 종목으로 먼저 압축될 가능성이 크다.
* KOSPI 외국인 순매도는 한국 이탈이라기보다 AI memory 초대형주 차익실현과 일부 산업재·방산·전력기기 재배치로 보는 편이 정확하다.
* KOSDAQ 외국인 A/B는 관심의 증거이지만, 장기 DM long-only core보다 테마 회전과 이벤트 트레이딩이 섞여 있다.

### [Blocked]

* 로컬 DB는 외국인 gross buy/sell가 아니라 순매수금액 중심이므로, 본 분석의 외국인 활동은 `sum(abs(net flow))` proxy다.
* MSCI DM 편입 시점, 실제 편입 여부, passive inflow 금액은 확정되지 않았다.
* 종목별 해외 long-only 실제 보유 의사, mandate별 매수 제한, 종목별 세부 대차·공매도·프로그램 데이터는 이번 글의 범위 밖이다.

*Disclaimer: This article is for research and information only. It is not investment advice.*
