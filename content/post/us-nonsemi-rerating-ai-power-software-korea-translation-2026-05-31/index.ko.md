---
title: "미국 비반도체 리레이팅 2개월 점검: AI 전력·소프트웨어·스테이블코인 rails의 한국장 번역"
date: 2026-05-31T16:20:00+09:00
description: "2026년 3월 말부터 5월 말까지 미국 비반도체 리레이팅을 양자, 연료전지, AI 소프트웨어, 스테이블코인 rails, 우주·방산, 전력망으로 나누고, 이를 한국장 NHN KCP, 더존비즈온, 한화시스템, 세명전기, LG CNS, NAVER 관점으로 번역한다."
categories: ["Market-Outlook"]
tags:
  - "미국 주식"
  - "비반도체 리레이팅"
  - "AI power"
  - "AI software"
  - "스테이블코인"
  - "양자컴퓨팅"
  - "우주 방산"
  - "한국 주식"
  - "NHN KCP"
  - "더존비즈온"
  - "한화시스템"
  - "세명전기"
  - "LG CNS"
  - "NAVER"
slug: us-nonsemi-rerating-ai-power-software-korea-translation-2026-05-31
valley_cashtags:
  - NHN KCP
  - 더존비즈온
  - 한화시스템
  - 세명전기
  - LG CNS
  - NAVER
draft: false
---

> 연결 맥락
> 이 글은 [AI 토큰 선물과 토큰당 비용](/ko/post/ai-token-futures-cost-per-token-korea-semiconductor-thesis-2026-05-30/), [중국·홍콩 AI 과열의 한국장 전이 가능성](/ko/post/china-hong-kong-ai-overheat-korea-ai-cloud-llm-proxy-2026-05-31/), [HD현대중공업 SMR 옵션](/ko/post/hd-hyundai-heavy-industries-smr-terrapower-natrium-option-2026-05-27/)의 후속입니다. 앞선 글이 AI 인프라를 반도체·LLM·전력 관점에서 봤다면, 이번 글은 미국 비반도체 리레이팅이 한국장 2선 후보로 어떻게 번역되는지 봅니다. 관련 허브는 [한국 데일리 마켓 허브](/ko/page/korea-daily-market-hub/)와 [해외 투자자를 위한 한국 주식 허브](/ko/page/korea-stocks-foreign-investors-hub/)입니다.

## TL;DR

최근 2개월 미국장에서 반도체를 제외하고 가장 강하게 재평가된 축은 **양자컴퓨팅, 온사이트 전력·연료전지, AI 소프트웨어, 크립토·스테이블코인 인프라, 우주·드론·방산 2선**입니다.

다만 투자 가능성이 가장 좋은 축은 수익률 1등 테마가 아닙니다. 제 판단은 **AI power/grid + AI software/data operations**입니다. 전자는 AI factory 병목이 GPU에서 전력으로 이동한 결과이고, 후자는 "AI가 SaaS를 죽인다"는 공포가 Snowflake·Datadog 실적으로 되돌려진 결과입니다.

한국장 번역은 조금 다릅니다.

| 미국 테마 | 한국장 해석 | 가격 반영도 |
|---|---|---|
| AI power/grid | 전력기기, 케이블, busduct, HVDC, 전력 2선 | 대장주는 이미 반영, 2선 선별 |
| AI software/data apps | ERP, AX, cloud, 업무 데이터, AI 운영 플랫폼 | 아직 덜 반영 |
| Stablecoin/payment rails | PG, 은행, 간편결제, 원화 스테이블코인 | 아직 덜 반영, 정책 이벤트 |
| Space/defense/drones | 방산전자, 위성, 드론, 우주 시스템 | 2선은 덜 반영 |
| Quantum/security | 양자컴퓨팅보다 양자보안·PQC | 이미 과열 |
| Fuel cell/on-site power | 데이터센터 독립전원, SOFC, PAFC | 고베타, 선별 필요 |

실전 후보는 네 개만 우선 추적합니다.

| 우선순위 | 종목 | 판단 | 핵심 이유 |
|---:|---|---|---|
| 1 | NHN KCP | **Conditional Buy** | 스테이블코인 결제 PoC, 1Q 실적 성장, PER 13배권, 최근 외국인·기관 동반 매수 |
| 2 | 더존비즈온 | **Watchlist** | 한국판 AI software/data operations 후보. 주가는 거의 안 갔고 실적 성장률은 높음 |
| 3 | 한화시스템 | **Watchlist** | 우주·방산전자 옵션은 덜 반영. 다만 PER과 필리조선소 리스크 |
| 4 | 세명전기 | **Watchlist / 고변동** | 전력 대장 조정 이후 볼 2선. 밸류 부담은 낮지만 유동성 리스크 |

Buy now는 제한적입니다. 지금은 급등 대장 추격장이 아니라 **20일선 회복, 박스 상단 돌파, 외국인·질적기관 수급 동반 유입**이 붙는 2선만 고르는 장입니다.

---

## 1. 데이터 기준

미국 데이터는 `yfinance` adjusted close 기준입니다. 기간은 **2026년 3월 31일 종가부터 2026년 5월 29일 종가**까지입니다. 반도체, 반도체 장비, 메모리 직접주는 제외했고, SOXX와 SMH는 비교 기준으로만 사용했습니다.

한국 데이터는 Research OS local DB 기준입니다.

```text
/Users/youngseongshin/agents/Stock_Research/agents/KR_Crawler/data/screener_kr.db
```

가격 기준은 **2026년 3월 31일 종가부터 2026년 5월 29일 종가**까지이고, 수급은 최근 20거래일과 5거래일의 `investor_flow_raw_daily`, `amount_unit='million_krw'` 기준입니다.

[Blocked] 개별 종목별 최신 forward EV/Sales, forward PER, 컨센서스 EPS 리비전, 모든 DART 세부 항목은 전수 재검증하지 않았습니다. 따라서 여기서 말하는 리레이팅은 **최근 가격·수급·공개 촉매 기반의 시장 재평가**입니다.

---

## 2. 미국 비반도체 2개월 리레이팅 순위

| 순위 | 세부테마 | 바스켓 수 | 2개월 중앙값 | 1개월 중앙값 | 고점 대비 중앙값 | 상위 종목 |
|---:|---|---:|---:|---:|---:|---|
| 1 | Quantum computing | 5 | **+81.9%** | +45.9% | -2.8% | IONQ +150.0%, QBTS +108.9%, RGTI +81.9% |
| 2 | Clean hydrogen / fuel cell | 7 | **+74.8%** | +12.5% | -4.6% | FCEL +231.7%, BLDP +159.9%, BE +110.3% |
| 3 | AI software / data apps | 10 | **+34.0%** | +30.3% | 0.0% | DDOG +109.5%, CRWD +87.2%, SNOW +69.4% |
| 4 | Crypto / stablecoin / brokerage rails | 9 | **+27.5%** | -1.2% | -10.4% | RIOT +119.3%, CLSK +114.9%, MARA +76.2% |
| 5 | Space / defense / drones | 10 | **+22.6%** | +14.2% | -1.9% | LUNR +136.2%, RKLB +123.4%, PL +83.0% |
| 6 | Software broad | 8 | **+21.3%** | +14.8% | 0.0% | SKYY +32.2%, IGV +27.0%, CLOU +24.5% |
| 7 | Copper / electrification metals | 7 | **+15.4%** | +12.5% | -2.1% | TECK +27.8%, BHP +22.2%, XME +15.9% |
| 8 | Grid / electrical equipment / EPC | 10 | **+15.0%** | -4.9% | -9.9% | GNRC +42.3%, FIX +32.6%, PWR +29.7% |
| 9 | AI power / data-center electricity | 11 | **+12.3%** | -4.6% | -7.4% | BE +110.3%, OKLO +34.9%, PWR +29.7% |

비교 기준은 다음과 같습니다.

| 지수/ETF | 2개월 | 1개월 | 고점 대비 |
|---|---:|---:|---:|
| SPY | +16.3% | +5.0% | 0.0% |
| QQQ | +27.9% | +9.5% | 0.0% |
| IWM | +17.1% | +4.0% | -0.5% |
| SOXX | +73.2% | +22.2% | -0.2% |
| SMH | +56.2% | +17.5% | -0.5% |

해석은 세 가지입니다.

1. 반도체는 여전히 가장 강한 축입니다. SOXX +73.2%, SMH +56.2%가 기준점입니다.
2. 비반도체 안에서는 양자와 연료전지가 SOXX에 근접했습니다. 그러나 이는 수익률은 강하지만 late-stage 가능성이 큽니다.
3. 질 좋은 리레이팅은 **AI software/data apps**와 **AI power/grid**입니다. 전자는 실적이 붙고, 후자는 AI 데이터센터 병목이 전력으로 이동했다는 구조적 논리가 있습니다.

---

## 3. 미국 테마별 투자 해석

### 3.1 Quantum computing: 수익률 1등이지만 신규 추격은 비효율

양자컴퓨팅은 최근 2개월 중앙값 +81.9%로 최강 테마였습니다. IonQ는 Q1 2026 자료에서 매출 성장, 대규모 현금·투자자산, FY2026 매출 가이던스를 제시했습니다. ([SEC IonQ EX-99.1](https://www.sec.gov/Archives/edgar/data/1824920/000119312526208923/ionq-ex99_1.htm))

[Inference] 리레이팅 본질은 "연구개발 테마"에서 "시스템 판매와 상업 매출이 붙는 테마"로 시장 인식이 바뀐 데 있습니다. 그러나 IONQ, QBTS, RGTI 같은 종목이 이미 2개월에 80~150% 급등한 뒤라, 지금은 초기 돌파가 아니라 확장 후반부일 가능성이 높습니다.

**판단:** Watchlist. 신규 추격 금지. 베이스 재형성 후만 검토.

---

### 3.2 Clean hydrogen / on-site fuel cell power: Bloom만 별도 취급

Bloom Energy는 2026년 4월 28일 Q1 2026 실적에서 매출 **7.511억 달러**, 전년 대비 **+130.4%**, 제품 매출 **+208.4%**, 영업이익 **7,220만 달러**를 발표했습니다. FY2026 매출 성장 가이던스 중간값도 기존 약 +60%에서 약 +80%로 올렸습니다. ([Bloom Energy](https://www.bloomenergy.com/news/bloom-energy-reports-record-first-quarter-2026-results-and-raises-full-year-2026-guidance/))

[Inference] 이 리레이팅은 "수소경제"가 아니라 **AI 데이터센터의 전력 조달 시간 문제**입니다. 전력망 증설은 느리고 AI campus는 빠르게 전기를 필요로 합니다. Bloom은 온사이트 전력 조달 대안으로 다시 가격이 붙었습니다.

**판단:** Bloom 중심으로만 선별. FCEL, BLDP, PLUG 같은 저품질 연료전지주는 숏커버·고베타 성격이 커서 추격 금지.

---

### 3.3 AI software / data apps: 비반도체 중 가장 질이 좋다

Snowflake는 FY2027 Q1에서 제품 매출 **13.34억 달러**, 전년 대비 **+34%**, RPO **92.1억 달러**, 전년 대비 **+38%**를 기록했습니다. ([Snowflake SEC filing](https://www.sec.gov/Archives/edgar/data/1640147/000164014726000027/fy2027q1earnings.htm))

Datadog는 Q1 2026 매출 **10.06억 달러**, 전년 대비 **+32%**, 10만 달러 이상 ARR 고객 약 **4,550개**를 발표했고, GPU Monitoring, Bits AI Security Agent, MCP Server를 GA했습니다. ([Datadog IR](https://investors.datadoghq.com/news-releases/news-release-details/datadog-announces-first-quarter-2026-financial-results/))

[Inference] 이 테마의 본질은 "AI가 SaaS seat를 죽인다"는 공포가 "AI deployment가 observability, data governance, security, workflow 운영 수요를 늘린다"는 쪽으로 뒤집힌 것입니다.

**P×Q×C**

| 축 | 해석 |
|---|---|
| P | AI-native software와 data control plane의 매출 배수 회복 |
| Q | AI agent, GPU fleet, data governance, security observability 수요 증가 |
| C | 기존 SaaS gross margin 위에 AI product attach가 붙으면 incremental margin이 높음 |

**판단:** 비반도체 중 가장 질 좋은 리레이팅. 다만 실적 발표 직후 추격보다 5~10거래일 소화와 20일선 지지를 확인.

---

### 3.4 Crypto / stablecoin / brokerage rails: 거래량 베타에서 결제 rail로 확장

Coinbase는 Q1 2026 자료에서 crypto trading volume market share가 **8.6%**로 사상 최고였고, Coinbase 제품 내 평균 USDC 보유액은 약 **190억 달러**, Base는 글로벌 온체인 스테이블코인 거래량의 **62%**를 처리했다고 밝혔습니다. ([Coinbase IR](https://investor.coinbase.com/news/news-details/2026/Coinbase-Q1-Financial-Results-Show-Resilient-Financial-Performance-Driven-by-New-All-Time-High-Crypto-Trading-Volume-Market-Share/default.aspx))

AP는 2025년 7월 18일 미국에서 GENIUS Act가 법으로 서명되어 스테이블코인 규제 프레임워크가 도입됐다고 보도했습니다. ([AP](https://apnews.com/article/donald-trump-stablecoins-congress-cryptocurrency-94fa3c85e32ec6fd5a55576cf46e58ea))

[Inference] 리레이팅은 비트코인 가격만이 아니라 **스테이블코인·예측시장·agentic commerce rail**로 narrative가 넓어진 결과입니다.

**판단:** COIN과 HOOD는 질 좋은 플랫폼 후보, 채굴주는 고베타 트레이딩 대상.

---

### 3.5 Space / defense / drones: SPAC 테마에서 backlog 산업으로 이동

Rocket Lab은 Q1 2026 실적에서 매출 **2.003억 달러**, 전년 대비 **+63.5%**, backlog **22억 달러**를 발표했고, 신규 Electron/HASTE와 Neutron launch contract를 확보했습니다. ([Rocket Lab IR PDF](https://investors.rocketlabcorp.com/node/12416/pdf))

[Inference] 리레이팅은 "소형 발사체"가 아니라 **space systems + defense payload + vertical integration**으로 옮겨간 결과입니다. 다만 LUNR 같은 이벤트주는 NASA·달 탐사 계약 변동성이 큽니다.

**판단:** RKLB, AVAV, KTOS, ASTS만 선별 관찰. 신규 계약·backlog 확인과 고점 대비 조정 후 OBV 방어가 필요합니다.

---

## 4. 한국장 번역: 무엇은 이미 갔고, 무엇은 덜 갔나

한국에서도 비슷한 축이 움직였습니다. 그러나 미국과 순서가 다릅니다.

| 세부테마 | 종목 수 | 2개월 중앙값 | 1개월 중앙값 | 2개월 고점 대비 | 최근 20D 외국인 | 최근 20D 기관 | 판정 |
|---|---:|---:|---:|---:|---:|---:|---|
| Copper/electrification metals | 9 | **+70.2%** | -19.0% | -26.0% | -980억 | +194억 | 이미 리레이팅, 조정 중 |
| Quantum/security/network | 8 | **+67.4%** | -4.3% | -26.5% | +498억 | -266억 | 이미 과열, 일부 외국인 매수 |
| AI power/grid/electrical | 12 | **+42.8%** | -24.3% | -26.0% | -1.44조 | -1,658억 | 대장군은 가격 반영, 2선만 관찰 |
| On-site power/fuel cell/SMR | 11 | **+26.8%** | -19.3% | -23.0% | -4,356억 | -4,046억 | 일부만 리레이팅, 수급 약함 |
| Space/defense/drones | 12 | **-0.5%** | -19.5% | -24.7% | +1,579억 | +102억 | 아직 덜 반영, 수급 개선 후보 |
| Crypto/stablecoin/payment rails | 12 | **-3.6%** | -17.3% | -25.7% | -326억 | -12억 | 가격 미반영, 종목 선별 필요 |
| AI software/data apps | 12 | **-3.6%** | -14.8% | -21.0% | -3,064억 | -254억 | 가격 미반영, 퀄리티 선별 필요 |

핵심은 이렇습니다.

> 한국의 전력·구리·양자보안은 미국 테마를 이미 선반영했습니다. 반대로 미국에서 강했던 AI software/data apps와 stablecoin/payment rails는 한국에서는 아직 크게 가격화되지 않았습니다.

---

## 5. 한국 후보 1: NHN KCP

**판단:** Conditional Buy
**테마:** 스테이블코인 결제, PG, Payco, 결제 인프라

| 항목 | 값 |
|---|---:|
| 종가 | 17,930원 |
| 2개월 수익률 | +14.3% |
| 1개월 수익률 | -10.6% |
| 2개월 고점 대비 | -15.8% |
| 20D 외국인 | +38.1억원 |
| 20D 기관 | -5.8억원 |
| 20D 질적기관 | +28.9억원 |
| 5D 외국인 | +17.4억원 |
| 5D 기관 | +36.6억원 |
| 5D 질적기관 | +29.7억원 |
| Forward PER | 13.0배 |
| TTM PER | 14.0배 |
| OP YoY | +24.9% |

NHN KCP는 2026년 5월 스테이블코인 온·오프라인 결제 PoC를 진행 중이라고 보도됐습니다. 서울신문 보도에 따르면 아발란체와 협업한 결제 특화 메인넷, PAYCO 연계, 온라인 상품권 구매, 오프라인 카페·구내식당 결제, 가맹점용 관리자 페이지가 함께 검증되고 있습니다. QR 승인 시간은 약 2초로 보도됐습니다. ([서울신문](https://www.seoul.co.kr/news/economy/2026/05/21/20260521500054))

NHN KCP는 NH농협은행과 디지털 지급결제 협력도 체결했습니다. ([파이낸셜뉴스](https://www.fnnews.com/news/202604220917147287)) 1Q26 실적도 나쁘지 않습니다. 연합뉴스는 NHN KCP의 1Q26 연결 영업이익이 **138억원**, 전년 대비 **+26.4%**, 컨센서스를 **+4.4% 상회**했다고 보도했습니다. ([연합뉴스](https://www.yna.co.kr/view/AKR20260512018500527))

**왜 아직 priced-in이 아닌가**

주가는 2개월 +14.3%에 불과하고, 1개월은 -10.6%입니다. 반면 실적은 성장했고 최근 5일 외국인·기관·질적기관 수급이 모두 플러스입니다. 시장은 아직 NHN KCP를 "저마진 PG주"로 보고 있고, "원화 스테이블코인 결제 인프라"로는 충분히 재분류하지 않았습니다.

**Entry**

| 조건 | 기준 |
|---|---|
| 1차 지지 매수 | 17,000~18,000원 지지 + 외국인·질적기관 동반 순매수 유지 |
| 추세 진입 | 18,500원 돌파 + 거래대금 증가 |

**Invalidation**

- 스테이블코인 PoC가 실증으로 끝나고 상용화 일정이 제시되지 않을 경우
- PG 본업 영업이익 성장률이 10% 이하로 둔화될 경우
- 16,500원 이탈 + 외국인·질적기관 매수 중단

---

## 6. 한국 후보 2: 더존비즈온

**판단:** Watchlist / breakout candidate
**테마:** AI ERP, 업무 데이터, AI software/data operations

| 항목 | 값 |
|---|---:|
| 종가 | 120,000원 |
| 2개월 수익률 | +0.8% |
| 1개월 수익률 | 0.0% |
| 2개월 고점 대비 | -0.2% |
| 20D 외국인 | +243.7억원 |
| 20D 기관 | -137.9억원 |
| 5D 외국인 | +61.1억원 |
| TTM PER | 36.8배 |
| OP YoY | +44.9% |

BusinessPost는 더존비즈온의 2026년 1분기 실적이 AI·클라우드 솔루션 매출 성장과 수익성 개선으로 증가할 전망이라고 보도했습니다. ([BusinessPost](https://www.businesspost.co.kr/BP?command=mobile_view&num=429250))

[Inference] 미국에서 Snowflake와 Datadog이 재평가된 논리는 한국에서 더존비즈온으로 가장 자연스럽게 번역됩니다. 기업 내부 업무 데이터, ERP, 결재, 문서, 그룹웨어는 AI agent가 실제 기업 업무에 들어갈 때 필요한 운영 표면입니다.

**왜 아직 덜 갔나**

2개월 수익률은 +0.8%에 불과합니다. 외국인은 20일 기준 순매수이고, 실적 성장률은 높지만 시장은 아직 더존을 "ERP·그룹웨어주"로 보는 경향이 있습니다.

**Entry**

- 118,000~120,000원 지지 후 거래량 감소
- 123,000~125,000원 돌파 + 외국인 매수 유지

**Invalidation**

- AI·클라우드 매출 성장률 둔화
- 영업이익 성장률 20% 하회
- 115,000원 이탈 + 외국인 매수 중단

---

## 7. 한국 후보 3: 한화시스템

**판단:** Watchlist / 조건부 편입 후보
**테마:** 우주, 방산전자, 위성, 레이더, ICT

| 항목 | 값 |
|---|---:|
| 종가 | 105,000원 |
| 2개월 수익률 | -8.0% |
| 1개월 수익률 | -12.3% |
| 2개월 고점 대비 | -23.4% |
| 20D 외국인 | +628.2억원 |
| 20D 기관 | -51.6억원 |
| 5D 외국인 | +329.4억원 |
| 5D 질적기관 | +98.1억원 |
| Forward PER | 82.0배 |

한화시스템은 1Q26 매출 **8,071억원**, 영업이익 **343억원**을 기록했고, 방산 부문은 중동 수출과 국내 양산 사업이 매출 성장을 견인한 것으로 보도됐습니다. 조선비즈는 1Q26 수주잔고가 **12조1963억원**이라고 보도했습니다. ([조선비즈](https://biz.chosun.com/industry/company/2026/04/27/4KHWSH5GKZAULGV5V5MVF65MSM/))

[Inference] 미국의 Space/defense/drones 리레이팅은 한국에서 LIG넥스원·한화에어로스페이스 일부에 먼저 반영됐습니다. 한화시스템은 필리조선소 손실과 고PER 부담 때문에 주가가 눌려 있지만, 방산전자·위성·SAR·AI 영상 분석 옵션은 남아 있습니다.

**왜 아직 priced-in이 아닌가**

주가는 2개월 -8.0%, 고점 대비 -23.4%입니다. 반면 20일 외국인 순매수는 +628억원입니다. 시장은 방산전자와 우주 옵션보다 연결 손익 리스크와 PER 부담을 더 크게 보고 있습니다.

**Entry**

- 102,000~105,000원 지지 + 외국인 매수 지속
- 112,000원 돌파 + 기관 매도 완화

**Invalidation**

- 필리조선소 손실이 2Q에도 확대될 경우
- 방산 부문 수익성 둔화
- 100,000원 이탈 + 외국인 매수 중단

---

## 8. 한국 후보 4: 세명전기

**판단:** Watchlist / 고변동 2선
**테마:** 전력망 2선, HVDC, 전력 설비

| 항목 | 값 |
|---|---:|
| 종가 | 9,890원 |
| 2개월 수익률 | +14.3% |
| 1개월 수익률 | -37.3% |
| 2개월 고점 대비 | -40.3% |
| 20D 외국인 | +20.4억원 |
| 20D 기관 | +1.2억원 |
| TTM PER | 11.4배 |
| OP YoY | +393.3% |

[Inference] 전력 대장군은 이미 가격 반영됐지만, 세명전기는 1개월 조정이 깊고 밸류에이션 부담이 상대적으로 낮습니다. 다만 소형주라 수급 신뢰도와 변동성 리스크가 큽니다.

**Entry**

- 9,500~10,000원 지지 + 거래대금 감소
- 11,000원 회복 + 외국인·기관 동반 순매수

**Invalidation**

- HVDC·전력망 관련 실적 반복성 훼손
- 9,000원 이탈 + 거래대금 급감

---

## 9. 제외 또는 추격 금지

| 종목군 | 이유 |
|---|---|
| 엑스게이트, 아이윈플러스, 드림시큐리티 | 2개월 +100~278% 급등. 미국 Quantum 리레이팅과 같은 질이 아니라 테마 과열 성격 |
| LS ELECTRIC, 효성중공업, 산일전기 | 사업 퀄리티는 강하지만 이미 리레이팅 후 1개월 조정. 현재는 수급 이탈 검증 구간 |
| 두산퓨얼셀 | 2개월 +173.7%. 연료전지 테마는 붙었지만 밸류에이션·적자 리스크 큼 |
| 대한전선, KBI메탈, 가온전선 | 구리·전선 베타 급등 후 깊은 조정. 기술적 베이스 재형성 전 추격 비효율 |

---

## 10. 실행 전략

**Buy now:** 없음.

**Wait / Watchlist**

| 축 | 종목 | 조건 |
|---|---|---|
| AI software | SNOW, DDOG, CRWD, APP, MDB, NET | 실적 발표 후 5~10거래일 소화, 20일선·직전 박스 상단 지지, 거래량 감소 후 재상승 |
| AI power/grid | GEV, PWR, ETN, BE, CEG, VST | 고점 대비 8~15% 눌림 후 거래량 감소, 다음 수주·가이던스 확인 |
| 한국 stablecoin rails | NHN KCP | 18,500원 돌파 또는 17,000~18,000원 지지 + 수급 유지 |
| 한국 AI software | 더존비즈온 | 123,000~125,000원 돌파 + 외국인 매수 유지 |
| 한국 우주·방산 2선 | 한화시스템 | 112,000원 돌파 + 기관 매도 완화 |
| 한국 전력 2선 | 세명전기 | 11,000원 회복 + 외국인·기관 동반 순매수 |

**Avoid / 추격 금지**

- IONQ, RGTI, QBTS 등 양자 pure play: 베이스 재형성 전 추격 금지
- FCEL, BLDP, PLUG 등 저품질 연료전지주: 숏커버·베타 성격이 커서 코어 편입 부적합
- RIOT, MARA, CLSK 등 채굴주: 장기 thesis보다 트레이딩 대상
- 한국 양자보안 급등주: 실적보다 테마 베타

---

## 11. 결론

미국 비반도체 리레이팅은 "AI가 반도체에서 끝나지 않는다"는 증거입니다. 다만 모든 후행 테마를 같은 질로 보면 안 됩니다.

가장 중요한 변화는 **AI factory의 병목이 GPU에서 전력·운영 소프트웨어·데이터센터 주변 인프라로 확산**됐다는 점입니다. 미국에서는 Bloom, Snowflake, Datadog, Coinbase, Rocket Lab이 각각 전력·데이터·보안·결제 rail·우주 인프라의 언어로 재평가됐습니다.

한국장에서는 이미 전력·구리·양자보안 대장군이 먼저 갔습니다. 아직 덜 반영된 쪽은 **스테이블코인 결제, AI software/data operations, 우주·방산전자 2선**입니다.

제 최종 결론은 단순합니다.

> 지금은 대장주 추격장이 아니라 2선 후보의 첫 수급·거래대금 확인장입니다. NHN KCP, 더존비즈온, 한화시스템, 세명전기만 우선 추적합니다.

---

## Evidence Ledger

| 항목 | 출처 | 확인 내용 |
|---|---|---|
| 가격 성과 | yfinance, 2026-05-31 접근 | 2026-03-31~2026-05-29 adjusted close 기준 테마 바스켓 수익률 |
| 한국 가격·수급 | Research OS local DB | 2026-03-31~2026-05-29 가격, 최근 20D·5D 세부주체 수급 |
| IonQ | [SEC EX-99.1](https://www.sec.gov/Archives/edgar/data/1824920/000119312526208923/ionq-ex99_1.htm) | Q1 2026 매출·현금·가이던스 확인용 |
| Bloom Energy | [회사 IR](https://www.bloomenergy.com/news/bloom-energy-reports-record-first-quarter-2026-results-and-raises-full-year-2026-guidance/) | Q1 2026 매출 7.511억 달러, +130.4% YoY, FY2026 가이던스 상향 |
| Snowflake | [SEC EX-99.1](https://www.sec.gov/Archives/edgar/data/1640147/000164014726000027/fy2027q1earnings.htm) | FY2027 Q1 제품 매출 13.34억 달러, +34% YoY, RPO 92.1억 달러 |
| Datadog | [회사 IR](https://investors.datadoghq.com/news-releases/news-release-details/datadog-announces-first-quarter-2026-financial-results/) | Q1 2026 매출 10.06억 달러, +32% YoY, GPU Monitoring·MCP Server 등 |
| Rocket Lab | [회사 IR PDF](https://investors.rocketlabcorp.com/node/12416/pdf) | Q1 매출 2.003억 달러, backlog 22억 달러 |
| Coinbase | [회사 IR](https://investor.coinbase.com/news/news-details/2026/Coinbase-Q1-Financial-Results-Show-Resilient-Financial-Performance-Driven-by-New-All-Time-High-Crypto-Trading-Volume-Market-Share/default.aspx) | USDC, Base, stablecoin, agentic commerce 지표 |
| GENIUS Act | [AP](https://apnews.com/article/donald-trump-stablecoins-congress-cryptocurrency-94fa3c85e32ec6fd5a55576cf46e58ea) | 2025년 7월 stablecoin 규제법 서명 |
| NHN KCP PoC | [서울신문](https://www.seoul.co.kr/news/economy/2026/05/21/20260521500054) | 온·오프라인 스테이블코인 결제 PoC, PAYCO 연계, QR 승인 약 2초 |
| NHN KCP 실적 | [연합뉴스](https://www.yna.co.kr/view/AKR20260512018500527) | 1Q26 OP 138억원, YoY +26.4%, 컨센서스 상회 |
| 한화시스템 | [조선비즈](https://biz.chosun.com/industry/company/2026/04/27/4KHWSH5GKZAULGV5V5MVF65MSM/) | 1Q26 매출·영업이익·수주잔고 보도 |

## Fact / Inference / Speculation / Blocked

### [Fact]

- 미국 비반도체 바스켓 중 최근 2개월 중앙값이 가장 강한 축은 Quantum computing, Clean hydrogen/fuel cell, AI software/data apps였습니다.
- Bloom Energy, Snowflake, Datadog, Coinbase, Rocket Lab은 각각 공식 IR·SEC 자료에서 리레이팅 촉매가 확인됩니다.
- 한국 전력·구리·양자보안 바스켓은 최근 2개월 중앙값 기준 이미 크게 상승했습니다.
- AI software/data apps와 Crypto/stablecoin/payment rails 한국 바스켓은 최근 2개월 중앙값 기준 -3.6%로 가격 반영이 약했습니다.
- NHN KCP는 스테이블코인 결제 PoC와 1Q26 영업이익 성장이 보도됐습니다.

### [Inference]

- 한국에서 가장 덜 반영된 미국식 비반도체 리레이팅은 스테이블코인 결제와 AI software/data operations입니다.
- 전력 대장주는 신규매수보다 조정 후 2선 선별이 합리적입니다.
- 한화시스템은 방산전자·우주 옵션 대비 가격은 눌렸지만 PER과 연결 손익 리스크 때문에 "저평가"보다 "옵션 미반영" 후보입니다.

### [Speculation]

- 원화 스테이블코인 제도화가 NHN KCP의 결제 인프라 economics로 연결될 가능성.
- 더존비즈온이 미국 AI software 리레이팅과 유사한 multiple 확장을 받을 가능성.
- 한화시스템의 우주·방산전자 옵션이 필리조선소 손실을 덮고 재평가될 가능성.

### [Blocked]

- 개별 종목별 최신 컨센서스 목표가, NTM EPS 리비전, forward EV/Sales는 전수 재검증하지 않았습니다.
- NHN KCP 스테이블코인 PoC의 상용화 일정과 수익 모델은 아직 확정되지 않았습니다.
- 더존비즈온 AI 매출의 제품별 반복매출 비중은 공개자료만으로 확정하기 어렵습니다.
- 세명전기 세부 수주·제품별 매출 반복성은 추가 DART·IR 확인이 필요합니다.

## Follow-up Queue

- [ ] AI software 10개 종목의 forward EV/Sales, NTM revenue growth, FCF margin 비교.
- [ ] AI power/grid 10개 종목의 backlog growth, 2026/2027 EPS revision 비교.
- [ ] 한국 번역 후보군의 최근 5일·20일 거래대금 증가와 외국인·기관 세부주체 수급 재점검.
- [ ] Quantum·연료전지 급등주의 late-stage 필터 적용: 60D 급등률, 50일선 과이격, 52주 저점 대비 상승률.
- [ ] NHN KCP 스테이블코인 PoC의 상용화 일정, 은행·PG·간편결제 economics 귀속 구조 추적.

*본 글은 정보와 분석 목적이며 개인 맞춤형 투자자문이 아닙니다. 언급된 종목은 리서치 예시이며, 투자 결정 전 각자의 검증과 전문가 상담이 필요합니다.*
