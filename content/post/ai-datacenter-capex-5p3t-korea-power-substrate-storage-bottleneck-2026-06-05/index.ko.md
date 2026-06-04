---
title: "AI 데이터센터 CapEx 5.3조 달러 시대: 한국 증시는 GPU보다 전력·기판·스토리지 병목을 봐야 한다"
date: 2026-06-05T10:45:00+09:00
description: "Goldman은 4대 하이퍼스케일러 FY2025~2030 CapEx 전망을 5.3조 달러로 올렸고, Alphabet은 2026년 CapEx 1,800~1,900억 달러와 2027년 추가 증가를 공식화했다. 한국 주식에서는 GPU보다 전력기기, 삼성전기 MLCC·FC-BGA·Si-Cap, 고다층 PCB, 광통신, eSSD 병목의 가격 전가력을 봐야 한다."
categories: ["Market-Outlook"]
tags:
  - "AI data center"
  - "CapEx"
  - "Alphabet"
  - "Google"
  - "Goldman Sachs"
  - "AI 인프라"
  - "전력기기"
  - "삼성전기"
  - "009150"
  - "LS ELECTRIC"
  - "010120"
  - "이수페타시스"
  - "007660"
  - "오이솔루션"
  - "138080"
  - "파두"
  - "440110"
  - "한국 증시"
  - "매크로"
slug: ai-datacenter-capex-5p3t-korea-power-substrate-storage-bottleneck-2026-06-05
valley_cashtags:
  - Alphabet
  - Google
  - 삼성전기
  - LS ELECTRIC
  - HD현대일렉트릭
  - 효성중공업
  - 이수페타시스
  - 오이솔루션
  - 파두
draft: false
---

> 📚 연결 맥락
> 이 글은 [유동성은 많은데 시장 폭은 무너졌다](/ko/post/korea-market-liquidity-foreign-reallocation-adr-narrow-leadership-2026-06-03/), [Real Money 수급 프레임워크](/ko/post/real-money-flow-framework-korea-institution-quality-2026-06-03/), [미국 비반도체 리레이팅의 한국장 번역](/ko/post/us-nonsemi-rerating-ai-power-software-korea-translation-2026-05-31/), [젠슨 황을 바라보는 한국 증시](/ko/post/korea-market-after-gtc-taipei-jensen-huang-naver-ai-factory-2026-06-02/), [브로드컴 2027년 AI 반도체 1,000억 달러 재확인](/ko/post/broadcom-ai-semiconductor-100b-2027-korea-value-chain-2026-06-05/)의 후속 매크로·밸류체인 글입니다. 관련 허브는 [데일리 마켓 허브](/ko/page/korea-daily-market-hub/), [해외 투자자용 한국 주식 허브](/ko/page/korea-stocks-foreign-investors-hub/), [한국 반도체 밸류체인 허브](/ko/page/korea-semiconductor-equipment-ip-hub/), [AI 기판·PCB 허브](/ko/page/korea-ai-pcb-substrate-hub/)입니다.

## TL;DR

- AI 데이터센터 투자는 이제 단순한 빅테크 설비투자가 아니라 **전력·부동산·사모 인프라 자금·채권·주식 발행이 함께 들어가는 거대한 인프라 자산군**으로 바뀌고 있다.
- Goldman은 Meta, Microsoft, Amazon, Alphabet의 FY2025~2030 CapEx 전망을 기존 **4.5조 달러에서 5.3조 달러**로 올렸다. Alphabet도 2026년 CapEx를 **1,800억~1,900억 달러**로 제시하고, 2027년에는 2026년보다 의미 있게 늘어난다고 밝혔다. ([Reuters/Goldman][1], [Alphabet][2])
- 한국장 번역은 “AI 테마 전체 매수”가 아니다. **전력기기 → 삼성전기 MLCC·FC-BGA·Si-Cap → 고다층 PCB → 광통신/CPO → eSSD·스토리지** 순서로 P×Q×C를 봐야 한다.
- 서버 조립·저마진 SI는 후순위다. 매출이 커져도 현금흐름과 반복 매출이 안 보이면 멀티플을 주기 어렵다.

![AI 데이터센터 CapEx와 한국 병목 지도](ai-datacenter-capex-korea-bottleneck-map-2026-06-05.png)

<div class="thesis-callout">
  <div class="thesis-callout__label">핵심 문장</div>
  <div class="thesis-callout__body">
    AI 데이터센터 CapEx 5.3조 달러의 한국식 번역은 GPU가 아니라 전력, 기판, 전원 안정화, 광연결, 스토리지 병목이다. 중요한 질문은 “AI 수요가 크다”가 아니라, 그 병목에서 누가 단가(P), 물량(Q), 비용(C)을 동시에 증명하느냐다.
  </div>
</div>

---

## 1. 무엇이 바뀌었나: AI CapEx가 금융시장 이벤트가 됐다

[Fact] Reuters는 Goldman Sachs 보고서를 인용해, 사모 인프라와 부동산 자본이 AI 데이터센터 붐의 더 큰 자금 조달 역할을 맡을 것이라고 보도했다. 같은 보도에서 Goldman은 Meta, Microsoft, Amazon, Alphabet의 FY2025~2030 합산 CapEx 전망을 **4.5조 달러에서 5.3조 달러**로 올렸다. ([Reuters/Goldman][1])

증가분만 계산해도 큽니다.

```text
상향 전 전망: 4.5조 달러
상향 후 전망: 5.3조 달러
증가분: 0.8조 달러
상향률: 0.8 / 4.5 = 약 17.8%
```

원화 환산을 단순히 1달러 1,500원으로 잡으면 5.3조 달러는 약 **7,950조원**입니다. 물론 이 돈이 한 번에 집행되는 것도 아니고, 한국 기업에 그대로 귀속되는 것도 아닙니다. 하지만 AI 데이터센터가 더 이상 “엔비디아 GPU 몇 개 더 사는 문제”가 아니라, 전력망, 토지, 냉각, 건설, 광통신, 스토리지, 금융 구조가 붙는 자산군이라는 점은 분명합니다.

[Fact] Alphabet은 2026년 6월 투자자 프레젠테이션에서 2026년 CapEx를 **1,800억~1,900억 달러**로 제시했고, 2027년에는 2026년보다 의미 있게 증가할 것이라고 설명했다. 이 지출의 대부분은 기술 인프라에 들어간다고 밝혔다. ([Alphabet][2])

[Fact] 같은 프레젠테이션에서 Alphabet은 Google Cloud의 성장과 backlog를 강조했다. Q1 Cloud 매출은 전년 대비 63% 증가했고, backlog는 전분기 대비 거의 두 배 늘어 **4,600억 달러 이상**이라고 설명했다. ([Alphabet][2])

여기서 중요한 변화는 세 가지입니다.

| 변화 | 의미 |
|---|---|
| CapEx 규모 확대 | GPU만이 아니라 전력·냉각·광연결·스토리지까지 병목이 넓어진다 |
| 외부 자금 조달 확대 | 데이터센터가 빅테크 내부 투자에서 인프라 금융 상품으로 이동한다 |
| Cloud backlog 증가 | 공급이 부족해서 투자가 늘어나는 구조가 유지된다 |

즉 AI 데이터센터는 이제 기술주 이벤트이자, 인프라·전력·부동산·금융 이벤트입니다.

---

## 2. 왜 한국 매크로와 연결되나

최근 한국장은 유동성은 많지만 시장 폭은 약합니다. [유동성은 많은데 시장 폭은 무너졌다](/ko/post/korea-market-liquidity-foreign-reallocation-adr-narrow-leadership-2026-06-03/)에서 정리했듯이, 예탁금과 CMA는 커졌지만 20일 ADR은 KOSPI와 KOSDAQ 모두 50 안팎까지 내려왔습니다.

이런 장에서는 “AI 관련주 전체”를 사면 안 됩니다. 돈은 넓게 퍼지지 않고, **가격 전가력이 있는 병목**으로만 들어갑니다.

AI 데이터센터 CapEx가 커질 때 한국에서 봐야 할 기준은 다음입니다.

| 기준 | 질문 |
|---|---|
| P, 가격 | 단가를 올릴 수 있는가? 고부가 제품 믹스가 올라가는가? |
| Q, 물량 | backlog, 장기계약, 고객 인증, 증설이 실제 매출로 연결되는가? |
| C, 비용 | 원재료·감가·운전자본을 통제해 이익과 현금흐름을 남기는가? |

이 프레임으로 보면 한국 AI 인프라의 우선순위는 꽤 명확해집니다.

---

## 3. 한국 밸류체인 우선순위

| 우선순위 | 레이어 | 한국 관찰 대상 | 투자 해석 |
|---:|---|---|---|
| 1 | 전력기기·전력망 | HD현대일렉트릭, 효성중공업, LS ELECTRIC | 가장 숫자가 빠르게 붙는 레이어. 수주잔고와 ASP가 핵심 |
| 2 | MLCC·FC-BGA·Si-Cap | 삼성전기 | AI 패키지 내부 전력망과 기판을 동시에 가진 희소 종목 |
| 3 | 고다층 PCB·네트워크 보드 | 이수페타시스, 대덕전자, 코리아써키트 | AI 네트워크·스위치·서버 보드 수요의 2차 병목 |
| 4 | 광통신·CPO | 오이솔루션, 쏠리드, RFHIC 등 | AI 데이터센터 내부 연결이 전기에서 광으로 이동할 때의 옵션 |
| 5 | eSSD·스토리지 | 파두 등 | AI 추론·KV-cache·데이터센터 SSD 수요가 커질 때의 새 병목 |
| 6 | 냉각·서버 통합 | GST, LG전자, M83/P&T Link류 | 수요는 크지만 마진·현금흐름 검증이 필요 |

한 줄로 압축하면 이렇습니다.

> 한국 증시에서 AI 데이터센터 CapEx는 “GPU 수요”가 아니라 “전력과 패키지, 광연결과 스토리지의 가격 전가력”으로 번역해야 한다.

---

## 4. 아이디어 1: 전력기기, 가장 먼저 숫자가 붙는 병목

AI 데이터센터는 전기를 먹습니다. GPU가 좋아도 전력망이 늦으면 데이터센터가 늦습니다. 그래서 전력기기 레이어는 AI 데이터센터 CapEx에서 가장 먼저 숫자로 검증되는 축입니다.

[Fact] HD현대일렉트릭은 2026년 1분기 수주가 17.97억 달러, 수주잔고가 78.88억 달러라고 발표했다. 회사는 북미·중동·유럽 전력기기 수요 강세를 언급했다. ([HD현대][4])

[Fact] The Elec은 LS ELECTRIC의 1Q26 매출이 1.3766조원, 영업이익이 1,266억원으로 증가했고, 데이터센터 수요가 전력기기 실적을 끌었다고 보도했다. 또한 AWS 관련 전력기기 계약과 5조원대 수주잔고를 언급했다. ([The Elec][5])

전력기기 투자의 장점은 P와 Q가 동시에 보인다는 점입니다.

- P: 변압기·차단기·전력기기 ASP 상승
- Q: 북미 데이터센터, 전력망 교체, 재생에너지 접속 수요
- C: 원재료 가격 전가와 증설 가동률이 마진을 좌우

다만 주가가 이미 많이 오른 대장주는 추격보다 조정을 기다려야 합니다. 여기서도 핵심은 “AI 데이터센터가 좋다”가 아니라 **수주잔고가 매출과 이익으로 전환되는 속도**입니다.

---

## 5. 아이디어 2: 삼성전기, 전력 안정화와 패키지 기판을 동시에 가진 희소 종목

AI 데이터센터가 커지면 GPU와 ASIC만 늘어나는 것이 아닙니다. 칩이 커지고 HBM이 늘어나면 패키지 내부 전원망과 기판이 복잡해집니다.

여기서 삼성전기의 논리가 강해집니다.

[Fact] 삼성전기는 글로벌 대형기업과 2027~2028년 약 1.5조원 규모의 실리콘 커패시터 공급계약을 체결했다. 회사는 실리콘 커패시터가 AI 서버용 GPU와 HBM 패키지 내부 전력 안정화에 쓰인다고 설명했다. ([삼성전기 Si-Cap][6])

[Fact] 삼성전기는 1Q26 실적에서 AI 서버·데이터센터용 고부가 MLCC, AI 가속기·서버 CPU용 고성능 패키지 기판 수요를 언급했다. Q1 패키지솔루션 매출은 전년 대비 크게 증가했다. ([삼성전기 Q1][7])

삼성전기의 강점은 하나의 제품이 아니라 조합입니다.

| 제품 | AI 데이터센터 CapEx와의 연결 |
|---|---|
| MLCC | 서버 보드와 패키지 주변 전력 안정화 |
| FC-BGA | AI GPU·ASIC·서버 CPU 패키지 기판 |
| Si-Cap | GPU·HBM 패키지 내부 전원 안정화 |

이 조합은 좋습니다. 다만 투자 판단에서는 가격이 중요합니다. 삼성전기는 이미 AI 패키지 전력무결성 회사로 상당 부분 재평가됐습니다. 그래서 추가 프리미엄은 후속 수주, 2027년 매출 인식, 마진, 고객 다변화가 증명해야 합니다.

---

## 6. 아이디어 3: 고다층 PCB와 AI 네트워크 보드

AI 데이터센터 CapEx가 늘면 네트워크도 같이 늘어납니다. 브로드컴, 마벨, 엔비디아 Spectrum-X 같은 흐름은 결국 고속 신호를 다루는 기판과 PCB 수요로 내려옵니다.

이수페타시스, 대덕전자, 코리아써키트 같은 종목은 이 레이어에 걸려 있습니다. 다만 모두 같은 기판주가 아닙니다.

| 구분 | 예시 | 봐야 할 것 |
|---|---|---|
| MLB / 네트워크 보드 | 이수페타시스 | AI 스위치·서버 보드 수요, 고객 집중도, 수주잔고 |
| FC-BGA | 삼성전기, 대덕전자, 코리아써키트 | 패키지 기판 ASP, 수율, 고객 인증 |
| 메모리 모듈 기판 | 심텍, 티엘비 등 | SOCAMM·DDR5·HBM 주변 모듈 수요 |

기판주는 수요가 맞아도 CAPA와 수율, 감가상각이 이익을 흔듭니다. 그래서 “AI 네트워크가 커진다”만으로는 부족합니다. 고객, 제품 믹스, 영업이익률을 같이 봐야 합니다.

---

## 7. 아이디어 4: 광통신과 CPO, 전기 연결의 한계를 넘는 옵션

AI 데이터센터가 커질수록 랙과 랙, 스위치와 가속기 사이의 연결은 더 빨라져야 합니다. 전기 신호만으로는 전력과 발열 부담이 커집니다. 그래서 광연결, CPO, EML, CW-DFB 같은 레이어가 중요해집니다.

[Fact] TrendForce는 AI 데이터센터 확대로 EML과 CW-DFB 레이저다이오드 월간 합산 생산능력이 2026년 **5,070만개**에 이를 것으로 봤다. ([TrendForce][8])

한국에서는 오이솔루션이 가장 직접적인 광모듈 기술 proxy입니다. 다만 최근 수급은 순수 광모듈보다 쏠리드·RFHIC 같은 AI-RAN/RU·통신장비 쪽이 더 살아 있었습니다. 그래서 광통신은 구조적 관심은 유지하되, 진입은 수급 전환 확인이 필요합니다.

---

## 8. 아이디어 5: eSSD와 스토리지, 추론 시대의 덜 본 병목

AI 훈련은 HBM과 GPU가 먼저 보입니다. 하지만 AI 추론이 커지면 데이터 저장과 호출, KV-cache, 엔터프라이즈 SSD가 더 중요해질 수 있습니다.

[Fact] The Elec은 파두가 eSSD 컨트롤러 관련 신규 계약을 확보했고, 2026년 계약 규모가 과거 매출보다 크게 커졌다고 보도했다. ([The Elec/Fadu][9])

파두의 핵심은 “주가가 많이 올랐다”가 아니라 **새 세그먼트가 실제 매출과 마진으로 열리는지**입니다. 이 부분은 [파두가 증명해야 할 단가·물량·새 시장](/ko/post/fadu-ai-infra-storage-bottleneck-p-q-new-segment-2026-06-02/)에서 따로 정리했습니다.

eSSD는 흥미로운 병목입니다. 다만 아직 고객명, 반복 계약, 원가 구조, 현금흐름이 더 필요합니다.

---

## 9. 후순위: 서버 통합과 냉각은 수요보다 마진이 문제

AI 데이터센터 CapEx가 크면 서버 통합, 랙 조립, 냉각도 커집니다. 하지만 이 레이어는 조심해야 합니다.

델 실적에서 확인했듯이 서버 조립은 매출이 커져도 마진이 낮을 수 있습니다. 따라서 한국의 서버 통합·SI·냉각주는 다음을 증명해야 합니다.

1. 일회성 구축이 아니라 반복 매출인가
2. 운전자본 부담이 통제되는가
3. 영업현금흐름이 실제로 남는가
4. 고객이 가격을 올려줄 만큼 병목인가

수요가 크다고 모두 좋은 주식은 아닙니다. AI 인프라에서 가장 위험한 곳은 **매출은 늘지만 현금흐름이 안 남는 레이어**입니다.

---

## 10. 실행 전략

지금은 broad beta 매수장이 아닙니다. [Real Money 수급 프레임워크](/ko/post/real-money-flow-framework-korea-institution-quality-2026-06-03/)에서 본 것처럼, 기관 합계보다 투신·사모·연기금의 지속성이 중요하고, [유동성 글](/ko/post/korea-market-liquidity-foreign-reallocation-adr-narrow-leadership-2026-06-03/)에서 본 것처럼 시장 폭은 아직 약합니다.

따라서 실행은 다음과 같습니다.

| 액션 | 조건 |
|---|---|
| 전력기기 대장 | 추격보다 수주잔고와 OPM 확인 후 눌림 |
| 삼성전기 | 후속 Si-Cap/FC-BGA 고객, 2027 매출 인식, 마진 가시성 |
| PCB·기판 | 고객·제품 믹스·수율 확인. 단순 AI 테마 추격 금지 |
| 광통신 | TrendForce 구조는 긍정적이나 수급 전환 전 대기 |
| eSSD | 계약 규모보다 반복성·고객·마진 확인 |
| 저마진 통합 | OCF와 반복 매출 증명 전 core 편입 금지 |

---

## 최종 결론

AI 데이터센터 CapEx 5.3조 달러 시대의 핵심은 “GPU가 더 필요하다”가 아닙니다. 그것은 이미 시장이 알고 있습니다.

진짜 질문은 다음입니다.

> GPU 이후의 병목이 어디로 옮겨가고, 그 병목에서 누가 가격을 올리고 물량을 받고 비용을 통제할 수 있는가?

한국장에서는 전력기기, 삼성전기, 고다층 PCB, 광통신, eSSD가 그 후보입니다. 다만 현재 시장은 폭이 좁습니다. 그래서 지금 해야 할 일은 AI 관련주를 넓게 사는 것이 아니라, **P×Q×C를 숫자로 증명하는 병목만 골라서 눌림에서 보는 것**입니다.

---

## 근거 분류

### [Fact]

- Goldman은 4대 하이퍼스케일러 FY2025~2030 CapEx 전망을 4.5조 달러에서 5.3조 달러로 올렸다고 Reuters가 보도했다. ([Reuters/Goldman][1])
- Alphabet은 2026년 CapEx를 1,800억~1,900억 달러로 제시했고, 2027년에는 2026년보다 의미 있게 증가할 것으로 밝혔다. ([Alphabet][2])
- Alphabet은 Google Cloud backlog가 4,600억 달러를 넘었다고 설명했다. ([Alphabet][2])
- HD현대일렉트릭은 1Q26 수주와 수주잔고를 공식 발표했다. ([HD현대][4])
- 삼성전기는 2027~2028년 약 1.5조원 규모 실리콘 커패시터 공급계약을 발표했다. ([삼성전기 Si-Cap][6])
- TrendForce는 EML과 CW-DFB 레이저다이오드 월간 합산 생산능력이 2026년 5,070만개에 이를 것으로 전망했다. ([TrendForce][8])

### [Inference]

- AI 데이터센터 CapEx는 GPU 단품 수요보다 전력, 냉각, 광연결, 기판, 스토리지 병목으로 확산된다.
- 한국에서는 전력기기와 삼성전기, 고다층 PCB가 가장 먼저 가격 전가력을 검증할 가능성이 높다.
- eSSD와 광통신은 구조적 후보지만, 아직 수급과 반복 주문 확인이 더 필요하다.

### [Speculation]

- Alphabet의 CapEx 확대가 한국 특정 기업의 직접 수주로 이어질지는 아직 확인되지 않았다.
- 사모 인프라·부동산 자금이 AI 데이터센터 금융 구조를 키우면 전력기기와 냉각, 데이터센터 REIT/인프라 가치도 추가 재평가될 수 있다.

### [Blocked]

- Goldman 원문 보고서는 공개 원문이 아니라 Reuters 보도 기반으로 확인했다.
- Alphabet의 개별 공급사, 한국 기업별 수주액, 구체적 데이터센터 부품 조달 구조는 공개되지 않았다.
- 파두·오이솔루션 등 일부 후보의 고객별 매출, 마진, 반복 주문은 공개자료만으로 완전히 확인할 수 없다.

## Sources

[1]: https://www.reuters.com/business/finance/private-infra-real-estate-capital-play-larger-financing-role-ai-data-center-boom-2026-06-03/ "Reuters: Private infra, real estate capital to play larger financing role in AI data center boom, Goldman says"  
[2]: https://blog.google/alphabet/investor-presentation-june-2026/ "Alphabet investor presentation: June 2026"  
[3]: https://www.sec.gov/Archives/edgar/data/1652044/000119312526251733/d160205dfwp.htm "Alphabet SEC Free Writing Prospectus, June 2026"  
[4]: https://www.hd.com/kr/newsroom/media-hub/press/view?detailsKey=4108 "HD현대 뉴스룸"  
[5]: https://www.thelec.net/news/articleView.html?idxno=6703 "The Elec: LS Electric Posts 45% Jump in First-Quarter Operating Profit on Data Center Demand"  
[6]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Silicon Capacitor Contract"  
[7]: https://samsungsem.com/kr/newsroom/news/view.do?id=10265 "삼성전기 2026년 1분기 경영실적"  
[8]: https://www.trendforce.com/presscenter/news/20260603-13077.html "TrendForce: AI Data Center Expansion to Drive EML and CW-DFB LD Capacity"  
[9]: https://www.thelec.net/news/articleView.html?idxno=10850 "The Elec: Fadu eSSD controller contract coverage"

