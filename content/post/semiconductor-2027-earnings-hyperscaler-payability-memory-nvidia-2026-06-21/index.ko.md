---
title: "2027년 반도체 컨센서스는 누가 지불하는가: 하이퍼스케일러 지불능력으로 본 삼성·하이닉스·마이크론·엔비디아"
slug: "semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21"
date: 2026-06-21T20:00:00+09:00
description: "2027년 삼성전자·SK하이닉스·마이크론·엔비디아의 실적 컨센서스가 단순 sell-side 낙관인지, 수요자가 실제로 지불 가능한 수준인지 같은 프레임에서 검증한다. 결론은 분리된다. 하이퍼스케일러는 조건부 지불 가능, 정부·주권 AI는 보조 수요, PC·스마트폰 OEM은 이미 지불불능 구간이다. 핵심은 'AI 수요가 있느냐'가 아니라 '2027년 이후에도 CAPEX를 정당화할 만큼 AI 매출과 GPU 활용률이 오르느냐'다."
categories: ["Exclusive Analysis", "Korean-Equities", "Market-Outlook"]
tags:
  - "삼성전자"
  - "SK하이닉스"
  - "마이크론"
  - "엔비디아"
  - "HBM"
  - "하이퍼스케일러"
  - "AI CAPEX"
  - "메모리"
  - "2027 실적"
  - "주권 AI"
  - "Research OS"
series: ["Korea Market Regime"]
draft: false
---

> 연결 맥락
> 이 글은 [AI 슈퍼사이클은 왜 더 길어지는가: IPO 자금과 메모리·스토리지](/ko/post/ai-supercycle-extension-agent-demand-ipo-funding-memory-storage-2026-06-12/), [AI 데이터센터 CapEx 5.3조 달러 시대](/ko/post/ai-datacenter-capex-5p3t-korea-power-substrate-storage-bottleneck-2026-06-05/), [골드만 토큰 수요 vs JP모간 메모리 ASP](/ko/post/goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31/), [삼하마 패리티: 한국 메모리가 다시 싸진 구간](/ko/post/samsung-hynix-micron-forward-per-parity-memory-catch-up-2026-06-03/)의 종합편이다. 앞글들이 수요·가격·밸류에이션을 따로 봤다면, 이번 글은 <strong>"2027년 실적 컨센서스를 수요자가 실제로 지불할 수 있는가"</strong>라는 하나의 질문으로 묶는다.

## TL;DR

* 2027년 컨센서스는 <strong>전자제품 수요</strong>가 아니라 <strong>하이퍼스케일러·AI 클라우드·주권 AI가 HBM·GPU·서버 DRAM 가격을 계속 받아주는지</strong>에 걸려 있다.
* 결론은 분리된다. <strong>하이퍼스케일러는 조건부 지불 가능</strong>, <strong>정부·주권 AI는 정치적으로 지불 의지가 있으나 ROI 불투명</strong>, <strong>PC·스마트폰 OEM은 이미 지불불능 구간</strong>이다.
* 숫자로 보면, 빅테크 4사(MS·구글·메타·아마존)의 2027E CAPEX 합계만 약 <strong>7,822억달러</strong>, FCF 합계는 약 <strong>1,199억달러</strong>다. 회계상 지불은 가능하지만 잔여 현금 완충은 얇다.
* 엔비디아 FY2028 매출 컨센서스 약 5,517억달러는 빅테크 4사 CAPEX의 약 <strong>70.5%</strong>다. 이 숫자가 맞으려면 4사만이 아니라 Oracle·OpenAI·주권 AI·중국·엔터프라이즈까지 포함한 <strong>전 세계 AI CAPEX 풀</strong>이 필요하다.
* 메모리 3사의 2027E 이익은 하이퍼스케일러 CAPEX보다도 <strong>메모리 ASP 유지와 HBM 공급부족의 지속성</strong>에 더 민감하다. 그래서 가장 흥미로운 비대칭성은 <strong>삼성전자(피크 할인이 과도할 수 있는 조건부 후보)</strong>다.

---

## 1. 핵심 질문과 회계연도 보정

이번 분석의 목적은 하나다. 2027년 삼성전자·SK하이닉스·마이크론·엔비디아의 실적 전망이 단순 sell-side 낙관인지, 아니면 최종 수요자의 지불능력으로 검증 가능한 수준인지 판단한다.

핵심 질문 다섯 개:

1. 2027E 매출·이익 전망은 얼마이며, 회계연도 차이를 보정하면 어떤 그림인가?
2. 메모리 3사와 엔비디아 전망을 단순 합산해도 되는가, 아니면 중복계산이 생기는가?
3. 하이퍼스케일러의 2027E CAPEX·FCF·외부금융 여력으로 이 매출을 감당할 수 있는가?
4. 정부·주권 AI가 2027년 실적을 독립적으로 지탱할 만큼 큰가?
5. PC·스마트폰 OEM이 메모리 가격 상승을 최종 소비자에게 전가할 수 있는가?

<strong>회계연도 주의:</strong> 삼성전자·SK하이닉스는 12월 결산이라 CY2027과 맞는다. 마이크론은 FY2027이 2027년 8월 종료다. 엔비디아는 FY2027이 2027년 1월 종료라 대부분 2026년 실적을 담으므로, "2027년"을 보려면 <strong>FY2028(2028년 1월 종료)</strong>을 함께 봐야 한다.

---

## 2. 2027E 실적 컨센서스 스냅샷

아래는 회사 가이던스가 아니라 <strong>외부 컨센서스·시장 데이터</strong>다(MarketScreener 기준, 2026년 6월 19일 종가). KRW는 비교 편의를 위해 대략 1달러=1,454원으로 병기한다.

| 기업 | 비교 기간 | 2027E 매출 | 2027E 영업이익/EBIT | 2027E 순이익 | 밸류에이션 | 1차 판정 |
|---|---|---|---|---|---|---|
| <strong>삼성전자</strong> | CY2027 | 856.8조원 (약 5,890억달러) | 460.1조원 | 373.4조원 | 354,000원, 2027E P/E 6.12배 | 컨센서스는 공격적, 주가는 "일시적 피크"로 할인 |
| <strong>SK하이닉스</strong> | CY2027 | 483.8조원 (약 3,330억달러) | 377.1조원 | 297.1조원 | 2,764,000원, 2027E P/E 6.71배 | HBM 리더십은 이미 상당 반영. 6-7배 피크 P/E는 지속성 불신 신호 |
| <strong>마이크론</strong> | FY2027 | 1,909.8억달러 | 1,572.0억달러 | 1,229.2억달러 (EPS 약 111달러) | 1,133.99달러, FY2027E P/E 약 10.2배 | 메모리 베타 최대, 2028년 둔화 가시화로 신규 매수 안전마진 최저 |
| <strong>엔비디아</strong> | FY2028 | 5,516.9억달러 | 3,620억달러 | 3,048.4억달러 (EPS 약 12.85달러) | 210.69달러, FY2028E P/E 약 16.4배 | 숫자가 맞으면 비싸지 않음. 문제는 그 숫자에 필요한 고객 CAPEX 규모 |

<strong>전망 분산이 크다.</strong> 특히 SK하이닉스는 KB 추정 2027E 영업이익이 당시 FnGuide 컨센서스(209.3조원)보다 약 <strong>71% 높았다.</strong> 같은 회사를 두고도 시장의 2027년 그림이 이렇게 갈린다는 것은, 컨센서스가 "확정된 미래"가 아니라 "가격 지속성에 대한 고강도 가정"이라는 뜻이다.

그리고 메모리 3사의 2027E 영업이익률에는 70%대가 포함돼 있다. 이는 일반적인 메모리 사이클이 아니라 <strong>구조적 공급부족 + 장기계약이 유지될 때만 가능한 숫자</strong>다.

---

## 3. "합산하면 안 된다": 이중계산 함정

가장 중요한 해석부터 짚는다. 메모리 3사의 HBM·DRAM·NAND 매출과 엔비디아의 GPU 매출은 <strong>최종 수요자 지출 관점에서 일부 중복</strong>된다.

엔비디아 매출에는 HBM을 포함한 시스템·보드·네트워킹 원가가 들어 있다. 메모리 업체의 HBM 매출은 그 시스템 원가의 upstream으로 들어간 뒤, 하이퍼스케일러가 사는 AI 서버 가격에 반영된다. 따라서 <strong>"엔비디아 매출 + 메모리 3사 매출"을 최종 지출액으로 단순 합산하면 같은 돈을 두 번 세게 된다.</strong>

투자 관점에서 각 노드의 매출은 모두 실재할 수 있다. 다만 최종 구매자는 같은 AI 데이터센터 예산 안에서 GPU, HBM, 일반 DRAM, SSD, 네트워킹, 서버, 전력, 냉각, 건설비를 <strong>모두</strong> 지불해야 한다. 그래서 매출 합산보다 <strong>"AI 데이터센터 총 CAPEX 풀"과 비교</strong>하는 것이 엄밀하다.

---

## 4. 수요자별 지불능력 검증

### 4.1 하이퍼스케일러: 조건부 지불 가능

빅테크 4사의 2027E CAPEX·FCF를 합산하면 다음과 같다(컨센서스 기준).

| 수요자 | 2027E CAPEX | 2027E FCF | 해석 |
|---|---:|---:|---|
| Microsoft | 1,704억달러 | 593억달러 | 투자 여력은 크나 FCF 희석 |
| Alphabet | 2,311억달러 | 252억달러 | CAPEX가 FCF 대부분을 흡수 |
| Meta | 1,595억달러 | 114억달러 | 잔여 FCF가 매우 얇아지는 구조 |
| Amazon | 2,212억달러 | 240억달러 | AWS·물류·AI 동시 투자 |
| <strong>합계</strong> | <strong>7,822억달러</strong> | <strong>1,199억달러</strong> | 회계상 지불 가능, 단 완충은 제한적 |

산식은 단순하다. <strong>CFO proxy = CAPEX + FCF = 7,822억 + 1,199억 = 약 9,021억달러.</strong> 즉 "하이퍼스케일러가 2027년 AI 비용을 지불할 현금흐름이 전혀 없다"는 주장은 틀렸다. 문제는 반대다. <strong>너무 많은 현금흐름이 AI CAPEX로 재배치되고 있다.</strong> 이 구조에서는 자사주 매입, 배당, M&A, 기존 인프라 교체, 전력계약, 데이터센터 임차료까지 모두 같은 현금을 두고 경쟁한다.

그리고 4사만으로는 부족하다. <strong>엔비디아 FY2028 매출 5,516.9억달러는 4사 CAPEX 7,822억달러의 약 70.5%</strong>(5,516.9 / 7,822 = 70.5%)다. 엔비디아 매출이 컨센서스대로 실현되려면 4사가 GPU에만 쓰는 게 아니라 비-GPU 인프라(전력·냉각·서버·네트워크·건설)도 동시에 지불해야 하므로, <strong>Oracle·CoreWeave·OpenAI/Stargate·xAI·중국 클라우드·중동 주권 AI·엔터프라이즈까지 포함한 전 세계 AI CAPEX 풀</strong>이 필요하다.

골드만삭스는 2026-2031년 AI CAPEX를 약 7.6조달러로, 모건스탠리는 2027E 글로벌 데이터센터 지출을 약 8,127억달러로 추정한다. 규모는 컨센서스를 설명할 수 있는 범위지만, 둘 다 <strong>하이퍼스케일러 현금흐름만으로는 부족해 회사채·ABS·private credit 등 외부금융이 필요</strong>하다는 financing gap을 함께 제시한다.

### 4.2 경제적 지불가능성: 현금과 다르다

현금으로 낼 수 있는 것과 경제적으로 감당 가능한 것은 다르다. 골드만삭스는 AI 칩의 유효수명을 통상 <strong>4-6년</strong>으로 본다. 2027년 AI CAPEX가 9,000억-1.1조달러라면, 감가상각만으로 연간 경제비용은 <strong>약 1,500억-2,750억달러/년</strong>이다(9,000억÷6년 = 1,500억 / 1.1조÷4년 = 2,750억). 여기에 전력·냉각·임대·네트워킹·운영·모델 학습비·금융비용이 더해진다.

따라서 하이퍼스케일러의 지불가능성은 결국 <strong>AI 추론 매출, 엔터프라이즈 AI 좌석 확대, 광고·검색·커머스 개선, 클라우드 GPU 임대수익</strong>이 이 감가상각을 얼마나 빨리 흡수하느냐에 달려 있다. 2027년까지는 현금흐름과 금융시장으로 버틸 수 있다. 그러나 2028-2029년에도 같은 속도로 투자하려면 AI 매출화가 더 명확해야 한다.

<strong>판정: 현금 지불능력은 조건부 TRUE, 경제적 ROIC 기준 지불가능성은 MIXED.</strong>

### 4.3 정부·주권 AI: 보조 수요, 단독 지불자는 아니다

수요는 실재한다. EU는 InvestAI로 총 2,000억유로 규모 AI 투자 mobilization을 발표했고, 사우디 HUMAIN은 엔비디아와 최대 500MW급 AI factory와 수십만 개 GPU 구축을 구상한다(1단계 GB300 1.8만 개 언급). OpenAI의 Stargate도 4년 5,000억달러·10GW 규모다(순수 정부 예산이 아니라 민간 주도).

[Inference] 정부·주권 AI는 민간 클라우드보다 가격 탄력성이 낮다(국방·데이터 주권·산업정책 목적). 따라서 엔비디아·HBM·전력 인프라에 <strong>수요 완충장치</strong>가 된다. 그러나 규모·집행속도 면에서 이들은 하이퍼스케일러 CAPEX의 <strong>대체재라기보다 보조금·장기전력계약·신용보강·앵커 고객</strong>에 가깝다. 발표 금액을 곧바로 매출로 보면 안 된다. 특히 중국은 수출통제·국산화로 엔비디아·마이크론 직접 수혜가 제한된다.

<strong>판정: 정부 수요만으로 2027 슈퍼사이클을 지탱한다는 주장은 FALSE. 하이퍼스케일러와 결합될 때 downside protection으로 중요.</strong>

### 4.4 전자제품 OEM: 지불 불가능에 가깝다

[Fact] 가트너는 2026년 PC 출하 <strong>-10.4%</strong>, 스마트폰 <strong>-8.4%</strong>, DRAM+SSD 가격 <strong>+130%</strong>를 전망했고, 이로 인해 PC 가격 +17%·스마트폰 가격 +13% 상승, PC BOM 내 메모리 비중이 2025년 16%에서 2026년 23%까지 오른다고 봤다. IDC도 AI 데이터센터가 웨이퍼를 흡수하면서 스마트폰·PC가 가격 인상·사양 축소·출시 지연으로 대응할 것으로 봤다.

[Inference] 전자제품 OEM은 메모리 가격을 "지불"하는 게 아니라 <strong>출하량 감소·탑재량 축소·판가 인상·모델 mix 하향</strong>으로 반응한다. 프리미엄 기기는 ASP 상승을 흡수하지만 중저가 시장은 가격 탄력성이 높아 수요 파괴가 나타난다. 즉 2027년 메모리 컨센서스를 정당화하는 주체는 PC·스마트폰이 아니다. 이 컨센서스는 사실상 <strong>AI 서버·HBM·엔터프라이즈 SSD·DDR5 RDIMM</strong> 수요에 의존한다.

<strong>판정: 핵심 지불자가 아니라 가격 상승의 피해자. FALSE.</strong>

---

## 5. 공급 병목: 2027년은 Q보다 P의 문제

[Fact] 가트너는 2026년 반도체 매출 1.320조달러, 2027년 1.555조달러, 메모리 매출 2026년 6,333억달러, 2027년 7,481억달러를 전망한다. 2026년 DRAM 가격 +125%, NAND +234%, 의미 있는 가격 완화는 2027년 말까지 제한적일 수 있다고 본다.

[Fact] 트렌드포스는 HBM 웨이퍼 투입 비중이 2025년 말 18%, 2026년 말 22%, 2027년 말 30%까지 오를 수 있지만, HBM bit supply 비중은 2027년에도 13% 수준에 그칠 수 있다고 본다. <strong>HBM이 DRAM 웨이퍼를 많이 잡아먹지만 전체 bit 공급은 제한적으로 증가</strong>한다는 뜻이다.

그래서 2027년 실적은 "수요량 Q"보다 <strong>가격 P와 제품 mix</strong>, 그리고 제한된 공급에서 발생하는 incremental margin이 누구에게 귀속되는가의 문제다. 그래서 PC·스마트폰의 범용 수요가 둔화돼도, AI 서버향 wafer allocation이 이미 이동한 HBM·서버 DDR5 부족은 즉시 해소되지 않는다.

---

## 6. 한국 read-through와 종목 판정 (예시·관찰 포인트)

아래 종목명은 <strong>바스켓 예시·관찰 포인트</strong>다. 매수 추천이 아니라 투자 가설 정리다.

| 종목 | 판단 | 한 줄 thesis | 핵심 리스크 |
|---|---|---|---|
| <strong>삼성전자</strong> | Watchlist → 조건부 Buy | HBM4/HBM4E catch-up과 DS 영업레버리지가 확인되면, 2027E P/E 6배 초반은 "피크 할인"이 과도할 수 있다 | HBM4 공급 지연, 주요 고객 allocation 미확보, DS 영업이익률 급락 |
| <strong>SK하이닉스</strong> | Wait | HBM 리더십은 가장 확실하나 주가가 이미 상당 반영. 이익 지속성은 매력적이나 신규 진입 안전마진은 낮다 | 경쟁사 HBM4 수율 개선으로 share·margin 하락, 주문 조정 |
| <strong>엔비디아</strong> | Watchlist | FY2028E P/E 16배대는 숫자가 맞으면 낮지만, 고객 CAPEX·AI ROI 검증 부담이 커졌다 | 자체 ASIC 침투, 중국 규제, GPU 임대수익 하락, 전력 병목 |
| <strong>마이크론</strong> | 신규 매수 Avoid | 메모리 베타는 크나 FY2027E P/E 10배대 + 2028년 둔화 리스크로 한국 메모리 대비 비대칭성이 낮다 | DRAM/NAND 조기 피크아웃, HBM share 열위, FY2028E EPS 하향 |

가장 좋은 구조는 <strong>"가격 결정권이 있고 아직 피크로 할인받는 병목 노드"</strong>다. 이 기준에서 현재 가장 흥미로운 것은 삼성전자다. 시장이 HBM4·패키징·메모리 가격 지속성을 아직 "피크 사이클"로 할인하고 있어, HBM4 catch-up이 확인되면 6배 초반 P/E가 재평가될 비대칭성이 있기 때문이다. SK하이닉스는 우량하나 진입가가 문제이고, 엔비디아는 품질자산이나 고객 ROI 검증이 선행되어야 하며, 마이크론은 신규 매수 비대칭성이 가장 약하다.

---

## 7. Red Team: 이 결론이 틀리는 경우

* <strong>금리·신용 리스크</strong>: 금리 상승 또는 credit spread 확대 시 하이퍼스케일러 CAPEX는 외부금융 의존이 큰 만큼 가장 먼저 흔들린다.
* <strong>ASIC 내재화</strong>: 구글 TPU, 아마존 Trainium, 메타 자체 칩이 2027년 이후 엔비디아 ASP ceiling과 HBM 수요 구조를 바꾼다.
* <strong>메모리 공급 증설</strong>: 삼성·마이크론이 HBM capacity를 공격적으로 늘리고 SK하이닉스 spread가 축소되면 2027E margin이 급락한다.
* <strong>"매출 유지, FCF·매출화 부진"</strong>: 가장 위험한 신호는 CAPEX 삭감보다, CAPEX는 유지하되 AI 매출 전환이 약한 상태다. 2027년 매출은 버텨도 2028년 주문 강도가 급격히 꺾일 수 있다.

---

## 8. 모니터링 체크리스트

| 지표 | 왜 중요한가 |
|---|---|
| 빅테크 4사 CAPEX revision | 삼성·하이닉스·마이크론·엔비디아 실적의 최상위 수요 proxy |
| CAPEX 차감 후 FCF | "지불 가능"과 "무리한 지출"을 가르는 핵심 |
| 엔비디아 데이터센터 backlog·lead time | FY2028 5,500억달러+ 매출 가시성 |
| HBM LTA·선불·capacity reservation | 메모리 ASP 지속성의 가장 직접적 증거 |
| DRAM/NAND 계약가 vs 현물가 | 범용 메모리 슈퍼사이클의 과열·정점 판단 |
| 클라우드 GPU 임대수익 | AI 인프라의 실제 매출화 proxy |
| 추론비용·AI 서비스 마진 | 하이퍼스케일러의 경제적 지불가능성 |
| PC·스마트폰 단위 탄력성 | 소비자 전자 수요 파괴 여부 |
| 데이터센터 전력 인허가·PPA | 공급 지연·CAPEX 이연 리스크 |

---

## 9. 최종 결론

<div class="thesis-callout">
  <div class="thesis-callout__label">핵심 문장</div>
  <div class="thesis-callout__body">
    2027년 반도체 컨센서스를 지불하는 것은 소비자가 아니라 하이퍼스케일러의 CAPEX다. 따라서 핵심 질문은 "AI 수요가 있느냐"가 아니라, "2027년 이후에도 CAPEX를 정당화할 만큼 AI 매출과 GPU 활용률이 빠르게 올라오느냐"다.
  </div>
</div>

2027년 4개사의 고실적 전망은 수학적으로 불가능하지 않다. 하이퍼스케일러와 AI 인프라 생태계의 CAPEX는 이미 8,000억-1조달러 영역에 진입했고, 외부금융까지 포함하면 2027년 공급망 매출을 지불할 수 있다. 그러나 <strong>세 조건이 동시에</strong> 충족되어야 한다.

1. 하이퍼스케일러 CAPEX가 2027년 최소 8,000억-1.1조달러를 유지하고, 4사 밖(Oracle·OpenAI·주권 AI·중국·엔터프라이즈)이 엔비디아 매출과 비-GPU 비용을 함께 메운다.
2. 메모리 가격이 "일시적 shortage premium"이 아니라 장기계약·선불·capacity reservation으로 고정된다.
3. AI 인프라가 실제 매출로 전환된다. 2028-2029년에도 같은 속도로 투자하려면 추론 매출·AI SaaS·광고/검색 개선·GPU 활용률이 감가상각과 전력비를 정당화해야 한다.

요약하면, 2027년 실적 전망은 <strong>"하이퍼스케일러 주도의 조건부 지불가능 시나리오"</strong>로는 성립하지만, <strong>정부 수요와 전자제품 OEM 수요만으로는 성립하지 않는다.</strong> 특히 메모리 3사의 이익은 하이퍼스케일러 CAPEX보다도 메모리 ASP 유지와 HBM 공급부족 지속성에 더 민감하다. 그래서 지금 봐야 할 것은 "AI 반도체 바스켓"이 아니라, <strong>가격 결정권이 있고 아직 피크로 할인받는 병목 노드</strong>다.

<small>이 글의 수치는 본문에 표기한 MarketScreener 컨센서스, 기업 공식 실적, 가트너·IDC·골드만삭스·모건스탠리·트렌드포스·로이터·미래에셋·KB 자료를 인용한 것이며, 모두 실제 결과가 아니라 2026년 중반 기준 시장 기대치다. 종목명은 투자 추천이 아니라 분석 흐름을 보여주는 예시이며, 실제 투자 판단과 책임은 투자자 본인에게 있다.</small>

## Sources

[1]: https://www.marketscreener.com/quote/stock/SAMSUNG-ELECTRONICS-CO-LT-35054473/finances/ "Samsung Electronics: Forecasts/Estimates | MarketScreener"
[2]: https://www.marketscreener.com/quote/stock/SK-HYNIX-INC-6494929/finances/ "SK hynix: Forecasts/Estimates | MarketScreener"
[3]: https://www.marketscreener.com/quote/stock/MICRON-TECHNOLOGY-INC-13639/finances/ "Micron Technology: Forecasts/Estimates | MarketScreener"
[4]: https://www.marketscreener.com/quote/stock/NVIDIA-CORPORATION-103502018/finances/ "NVIDIA: Forecasts/Estimates | MarketScreener"
[5]: https://www.gartner.com/en/newsroom/press-releases/2026-02-26-gartner-says-surging-memory-costs-will-reduce-global-pc-and-smartphone-shipments-in-2026 "Gartner: Surging Memory Costs Will Reduce PC and Smartphone Shipments in 2026"
[6]: https://www.idc.com/resource-center/blog/global-memory-shortage-crisis-market-analysis-and-the-potential-impact-on-the-smartphone-and-pc-markets-in-2026/ "IDC: Global Memory Shortage Crisis: Impact on Smartphone and PC Markets in 2026"
[7]: https://www.gartner.com/en/newsroom/press-releases/2026-04-08-gartner-forecasts-worldwide-semiconductor-revenue-to-exceed-us-dollars-one-point-3-trillion-in-2026 "Gartner: Worldwide Semiconductor Revenue to Exceed $1.3 Trillion in 2026"
[8]: https://www.trendforce.com/presscenter/news/20260602-13074.html "TrendForce: HBM Contract Prices Expected to Surge in 2027"
[9]: https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out "Goldman Sachs: Tracking Trillions: The Scale of the AI Build-Out"
[10]: https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Research_Bridging-Data-Center-Gap.pdf "Morgan Stanley: Bridging the Data Center Gap"
[11]: https://www.reuters.com/world/asia-pacific/nvidia-supplier-sk-hynix-q1-profit-rises-406-meets-forecasts-2026-04-22/ "Reuters: SK hynix says AI chip demand exceeds capacity"
[12]: https://securities.miraeasset.com/bbs/download/2143655.pdf?attachmentId=2143655 "Mirae Asset: Samsung Electronics 2027E"
[13]: https://commission.europa.eu/topics/competitiveness/ai-continent_en "European Commission: AI Continent (InvestAI)"
[14]: https://nvidianews.nvidia.com/news/saudi-arabia-and-nvidia-to-build-ai-factories-to-power-next-wave-of-intelligence-for-the-age-of-reasoning "Saudi Arabia and NVIDIA to Build AI Factories | NVIDIA Newsroom"
[15]: https://openai.com/index/five-new-stargate-sites/ "OpenAI, Oracle, SoftBank expand Stargate | OpenAI"
