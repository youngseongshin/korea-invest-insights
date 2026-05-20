---
title: "Google I/O 2026 이후 — 검색은 죽지 않았다. 문제는 agentic OS가 만드는 AI 인프라 병목이다"
date: 2026-05-21T10:35:00+09:00
description: "Google I/O 2026의 핵심은 Gemini 3.5, Gemini Omni, Spark, Antigravity, AI Search, Universal Cart를 통해 Google 전체 제품을 agentic OS로 재구성한 것이다. 검색이 AI에 죽는다는 단순 내러티브와 달리 Alphabet 1Q26 Search & other 매출은 19% 성장했다. 진짜 변화는 AI 사용량이다. Google은 월간 처리 토큰이 2024년 5월 9.7조 개에서 2026년 5월 3.2경 개 이상으로 늘었다고 밝혔다. 이 흐름의 한국 알파는 Alphabet 추격이 아니라 HBM, 패키징, 실리콘 커패시터, 고다층 PCB, 데이터센터 전력 병목에 있다."
categories: ["Market-Outlook"]
tags:
  - "Google I/O"
  - "Alphabet"
  - "Gemini"
  - "AI Search"
  - "삼성전자"
  - "삼성전기"
  - "SK하이닉스"
  - "HBM"
  - "AI 인프라"
  - "한국 반도체"
slug: google-io-2026-agentic-os-korea-ai-infra-2026-05-21
valley_cashtags:
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - 이수페타시스
  - 대덕전자
  - 티엘비
  - 코리아써키트
  - HD현대일렉트릭
  - LS ELECTRIC
  - 효성중공업
---

> 📚 **관련 시리즈**
> [구글 I/O + NVIDIA 실적 프리뷰](/ko/post/google-io-nvidia-earnings-korea-semi-preview-2026-05-17/) / [엔비디아 Q1 FY27 이후 한국 AI 인프라](/ko/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [삼성전자 TSMC식 리레이팅](/ko/post/samsung-electronics-tsmc-rerating-thesis-2026-05-16/) / [삼성전기 하이브리드 챌린저](/ko/post/samsung-electro-mechanics-hybrid-challenger-2026-05-17/) / [5/17 시황 종합](/ko/post/macro-snapshot-complex-risk-off-recovery-triggers-2026-05-17/)

*Google I/O 2026은 단순한 모델 발표회가 아니었다. Gemini 3.5, Gemini Omni, Gemini Spark, Antigravity, AI Search, Universal Cart, Android XR을 한 번에 묶어 Google 전체 제품을 agentic OS로 재구성한 이벤트였다. 검색은 링크를 보여주는 창에서 작업을 실행하는 인터페이스로 이동하고, 쇼핑은 장바구니 agent가 되고, 개발툴은 여러 agent를 병렬로 돌리는 runtime이 된다. 투자 관점에서 핵심은 Alphabet 자체보다 이 변화가 만드는 인프라 병목이다. 토큰 처리량, 추론 트래픽, 데이터센터 CapEx, HBM, 패키징, 전력 무결성, 고다층 PCB, 전력기기. Google I/O 이후 한국 알파는 모델이 아니라 병목에서 나온다.*

## 핵심 요약

* **Google I/O 2026의 본질**: Google은 Gemini 3.5 Flash, Gemini Omni Flash, Search agents, Gemini Spark, Antigravity 2.0, Managed Agents API, Universal Cart, Android XR을 하나의 agentic product layer로 묶었다.
* **검색 붕괴론은 아직 숫자로 확인되지 않았다**: Alphabet 1Q26 Search & other 매출은 603.99억 달러로 전년 동기 507.02억 달러 대비 약 19.1% 성장했다. 현재까지는 AI가 Search를 잠식한 것이 아니라 Google이 Search를 AI interface로 흡수한 쪽에 가깝다.
* **가장 중요한 숫자는 토큰 처리량**: Google은 월간 처리 토큰이 2024년 5월 9.7조 개, 2025년 I/O 약 480조 개, 2026년 5월 3.2경 개 이상으로 증가했다고 밝혔다. agentic OS는 사용량의 단위를 검색 쿼리에서 토큰·작업·agent 실행 횟수로 바꾼다.
* **Alphabet 주식은 방어력 확인, 한국은 병목 추적**: Alphabet은 full-stack AI company라는 방어 논리가 강해졌지만, 시가총액 4조 달러대와 약 30배 전후 이익배수는 상당 부분 기대를 반영한다. 신규 알파는 HBM, 패키징, 전력 무결성, PCB, 데이터센터 전력 쪽이 더 선명하다.
* **한국 우선순위**: 삼성전기 > 삼성전자 > SK하이닉스 > 테스트·소켓·HBM 장비 > 이수페타시스·대덕전자·티엘비·코리아써키트 > 전력기기.
* **가장 강한 단일 아이디어**: 삼성전기. 실리콘 커패시터 1.557조원 계약은 AI 패키지 내부 전력 안정화가 별도 병목으로 부상했다는 증거다.
* **매크로 조건**: 5/17 시황 글의 7개 매크로 게이트가 통과되지 않으면 고PER AI 인프라 종목은 좋은 thesis에도 흔들릴 수 있다. 추격보다 확인 후 분할이 맞다.

---

## 1. Google I/O 2026의 본질 — Google 전체가 agentic OS가 된다

이번 I/O를 "Gemini가 좋아졌다"로 요약하면 너무 작게 보는 것이다. Google이 실제로 한 일은 제품군 전체를 agent interface로 재구성한 것이다.

Google 공식 I/O 컬렉션은 Gemini Omni와 Gemini 3.5를 핵심 신모델로 제시했고, Search agents, Gemini Spark, Universal Cart, intelligent eyewear, Workspace, Antigravity를 모두 agentic experiences로 묶었다. 즉 한두 기능의 업데이트가 아니라 Search, Gemini app, YouTube, Gmail, Docs, Shopping, Android, Cloud developer tools를 하나의 agent layer로 다시 포장한 셈이다.

핵심 발표를 투자 관점으로 재분류하면 다음과 같다.

| 구분 | 발표 | 투자적 의미 |
|---|---|---|
| 모델 | Gemini 3.5 Flash, 3.5 Pro 예정 | AI 경쟁축이 단발 응답에서 장기 작업 실행으로 이동 |
| 멀티모달 생성 | Gemini Omni Flash | 영상 생성·편집·YouTube Shorts·Flow의 creative infra화 |
| 검색 | AI Mode 기본 모델, intelligent Search box, Search agents | 검색창이 query box에서 task interface로 변화 |
| 개인 agent | Daily Brief, Gemini Spark | Gmail·Calendar·Docs·Gemini 데이터를 묶는 개인 운영체제 |
| 개발툴 | Antigravity 2.0, CLI, SDK, Managed Agents API | Cursor류 코딩 보조를 넘어 enterprise agent runtime으로 진입 |
| 커머스 | Universal Cart | 광고·검색·YouTube·Gmail의 구매 funnel 재조립 |
| XR | Android XR, 스마트 안경 | 스마트폰 이후 ambient computing form factor 옵션 |

이 구조에서 Google의 진짜 자산은 모델 하나가 아니다. Search, YouTube, Gmail, Android, Chrome, Workspace, Shopping, Maps, Cloud, TPU를 모두 가진 distribution이다. OpenAI나 Anthropic이 모델 성능에서 앞서는 구간이 있어도, Google은 사용자가 이미 머무는 표면을 agent layer로 바꿀 수 있다. 이게 "Search 방어주"가 아니라 "agentic OS 사업자"라는 표현의 의미다.

---

## 2. 검색은 죽지 않았다 — 하지만 검색의 단위가 바뀐다

시장 내러티브는 지난 2년간 단순했다.

```text
AI 답변이 검색 결과를 대체
→ 사용자가 링크를 덜 클릭
→ Google Search 광고 매출 잠식
→ Alphabet multiple 하락
```

이 논리는 직관적이지만 현재 숫자는 반대로 말한다. Alphabet 1Q26 실적에서 Google Search & other 매출은 603.99억 달러였다. 전년 동기 507.02억 달러 대비 약 19.1% 성장이다.

```text
Search & other 성장률
= 60.399 / 50.702 - 1
= 약 19.1%
```

Google Cloud 매출도 200.28억 달러로 전년 동기 122.60억 달러 대비 약 63.4% 성장했다. Cloud 영업이익은 65.98억 달러, OPM은 32.9%였다.

```text
Cloud 성장률 = 20.028 / 12.260 - 1 = 약 63.4%
Cloud OPM = 6.598 / 20.028 = 약 32.9%
```

현재까지의 팩트는 "AI가 Search를 죽였다"가 아니다. 더 정확한 표현은 "Google이 Search를 AI interface로 바꾸면서 usage를 방어하고 있다"다.

다만 여기서 안심하면 안 된다. 검색의 경제 단위가 바뀌고 있기 때문이다.

| 과거 Search | AI Search / Agentic Search |
|---|---|
| 키워드 입력 | 자연어·파일·이미지·동영상·탭 입력 |
| 링크 클릭 | agent가 정보 수집·요약·행동 제안 |
| CPC 중심 | intent/action auction 가능성 |
| 검색 쿼리 수 | 토큰 처리량·agent 실행 횟수 |
| SEO publisher 트래픽 | Google 표면 내 task completion |

Google은 AI Mode가 1년 만에 월간 10억 사용자 규모를 넘었고, AI Mode query가 출시 이후 분기마다 2배 이상 늘었다고 밝혔다. 또 Search agents가 백그라운드에서 웹·뉴스·소셜·금융·쇼핑·스포츠 데이터를 지속 모니터링하는 구조를 제시했다.

이것은 검색의 파괴가 아니라 검색의 재정의다. 하지만 재정의에는 비용이 따른다. 링크 10개를 보여주는 검색보다 agent가 웹을 읽고, 요약하고, 추론하고, 알림을 보내는 검색은 훨씬 많은 compute를 쓴다. 이게 한국 반도체와 AI 인프라에 중요한 지점이다.

---

## 3. 가장 중요한 숫자 — 토큰 처리량과 CapEx

이번 I/O에서 가장 중요한 숫자는 모델 벤치마크가 아니라 사용량이다.

Google은 월간 처리 토큰이 다음과 같이 증가했다고 밝혔다.

| 시점 | 월간 처리 토큰 | 의미 |
|---|---:|---|
| 2024년 5월 | 9.7조 개 | AI 사용량 초기 구간 |
| 2025년 I/O | 약 480조 개 | Gemini·Cloud·developer 사용량 확대 |
| 2026년 5월 | 3.2경 개 이상 | YoY 약 7배 증가 |

Gemini app도 2025년 I/O 당시 월간 4억 사용자에서 2026년 5월 9억 명 이상으로 늘었다. Google은 daily requests도 1년 사이 7배 이상 증가했다고 설명했다.

더 중요한 것은 CapEx다. Sundar Pichai는 Google이 2022년에 연간 CapEx 310억 달러를 지출했지만, 올해는 약 1,800억~1,900억 달러 수준을 예상한다고 말했다. 이 정도면 Google I/O는 소비자 제품 이벤트가 아니라 글로벌 AI 인프라 수요 이벤트다.

```text
AI agentic OS
→ Search, Gemini, YouTube, Workspace, Android, Shopping 사용량 증가
→ 토큰 처리량 증가
→ inference cluster 증설
→ HBM / 패키징 / 네트워크 / 전력 / 냉각 병목 확대
→ 한국 AI 인프라 밸류체인 수혜
```

즉 "Google이 TPU를 쓰니까 NVIDIA 수혜가 줄어든다"는 1차 해석은 너무 얕다. TPU든 GPU든 ASIC이든 고성능 AI accelerator는 HBM, advanced packaging, high-speed substrate, 전력 안정화 부품, 데이터센터 전력을 필요로 한다. 한국 투자자는 특정 미국 칩 벤더보다 공통 병목을 봐야 한다.

---

## 4. Alphabet 주식 — 방어력은 확인, 신규 알파는 제한

Alphabet은 이번 I/O를 통해 세 가지 방어 논리를 강화했다.

첫째, Search가 AI에 잠식당하기만 하는 플랫폼이 아니라 AI를 흡수하는 플랫폼임을 보여줬다. 1Q26 Search & other 매출 성장률 19%는 이 논리에 힘을 준다.

둘째, Google은 모델, TPU, Cloud, Search, YouTube, Android, Workspace, Ads를 모두 가진 full-stack AI company다. 모델 API만 가진 회사보다 monetization surface가 넓다.

셋째, Google Cloud가 고성장과 고마진을 동시에 보여줬다. Cloud 매출 성장률 63%, Cloud OPM 32.9%는 "AI Cloud가 매출은 커지지만 이익은 안 남는다"는 우려를 줄인다.

그러나 투자 관점에서는 냉정해야 한다. Alphabet은 이미 시가총액 4조 달러대의 회사이고, 입력 기준 P/E는 30배 전후다. Q1 영업이익 단순 연율화 기준으로도 시총/OP가 약 30배 수준이다. 1Q26 순이익에는 비상장 지분평가이익 같은 기타수익 효과도 크게 들어가 있어, GAAP EPS만 보고 싸다고 판단하면 안 된다.

Alphabet의 투자 판단은 다음과 같다.

| 항목 | 판단 |
|---|---|
| 회사 질 | 매우 높음 |
| Search 방어력 | I/O와 1Q26 실적으로 강화 |
| Cloud 성장성 | 강함 |
| 밸류에이션 | 이미 상당 부분 반영 |
| 신규 매수 | Watchlist / 조정 시 |
| 더 좋은 알파 | AI infra second-order beneficiaries |

Alphabet은 좋은 회사다. 하지만 Google I/O 이후 더 좋은 매매는 Alphabet 추격이 아니라 Google이 만들어낼 CapEx 병목의 수혜주를 찾는 것이다.

---

## 5. 한국 밸류체인 매핑 — HBM에서 전력 무결성까지

Google I/O의 한국 투자 시사점은 단순히 "HBM 수요 좋다"가 아니다. Agentic workload가 늘면서 병목이 다음 순서로 확산된다는 점이다.

```text
AI Search / Omni / Antigravity / Spark / Universal Cart
→ 상시 inference traffic 증가
→ TPU/GPU/ASIC cluster 증설
→ HBM·DRAM·eSSD 수요 증가
→ 패키징·기판·전력 안정화 부품 수요 증가
→ optical/networking·데이터센터 전력 수요 증가
```

한국 밸류체인을 노드별로 정리하면 다음과 같다.

| 노드 | 병목 | 한국 후보 | 판단 |
|---|---|---|---|
| HBM / 메모리 | bandwidth, capacity | SK하이닉스, 삼성전자 | 구조적 수혜 지속, 대장은 crowded |
| Advanced packaging | HBM stack, bonding, 검사 | 한미반도체, 인텍플러스, ISC, 리노공업 | 수혜는 맞지만 가격·고객 확인 필요 |
| 전력 무결성 | 실리콘 커패시터, MLCC | 삼성전기 | 가장 선명한 신규 알파 |
| Substrate / PCB | FC-BGA, 고다층 PCB, 메모리 모듈 PCB | 삼성전기, 이수페타시스, 대덕전자, 심텍, 티엘비, 코리아써키트 | 테마보다 실적 확인 필요 |
| 전력 인프라 | 변압기, 배전, 전력품질 | HD현대일렉트릭, LS ELECTRIC, 효성중공업, 일진전기 | 수요는 명확, valuation discipline 필요 |
| 광 / 네트워크 | optical, SerDes, interconnect | 오이솔루션 등 | 수혜 가능, 직접 매출 검증 필요 |

여기서 핵심은 "Google 직접 납품주"를 찾는 것이 아니다. 한국 기업이 Google TPU에 직접 들어가는지 확인되지 않아도, Google·NVIDIA·AWS·Meta·Microsoft의 AI 인프라 확장이 공통으로 먹는 병목은 존재한다. 알파는 그 병목의 귀속처를 찾는 데 있다.

---

## 6. 삼성전기 — Google I/O 이후 가장 선명한 한국 AI 인프라 알파

이번 I/O 이후 한국에서 가장 중요한 종목은 삼성전기다. 이유는 단순하다. AI 인프라 병목이 HBM에서 패키지 내부 전력 안정화로 이동하고 있다는 점이 수주로 확인됐기 때문이다.

삼성전기는 2026년 5월 20일 글로벌 대형 기업과 1조5570억원 규모 실리콘 커패시터 공급계약을 체결했다고 공시했다. 계약 기간은 2027년 1월 1일부터 2028년 12월 31일까지다.

```text
연평균 계약액 = 1조5570억원 / 2년 = 7785억원
공시상 최근 매출 대비 총 계약액 = 13.8%
연평균 기준 매출 기여도 = 13.8% / 2 = 약 6.9%/년
```

이 계약은 매출 숫자 자체보다 분류 변화가 중요하다. 삼성전기는 과거 MLCC, 카메라모듈, 기판 회사로 분류됐다. 하지만 실리콘 커패시터는 AI 반도체 패키지 내부 또는 근접 위치에서 전력 노이즈를 줄이고 전력 공급을 안정화하는 부품이다. 즉 삼성전기가 AI server package BOM 안으로 들어간다는 뜻이다.

삼성전기 공식 기술자료도 AI 서버와 GPU 모듈의 전력 수요 증가로 MLCC 중심 전력 아키텍처가 확대되고 있다고 설명한다. AI GPU는 순간 전력 변동이 크고, 낮은 ESR/ESL, 고주파 ripple 대응, 공간 절감이 중요하다. 이건 단순 MLCC 사이클이 아니라 power integrity cycle이다.

삼성전기의 P×Q×C는 이렇게 볼 수 있다.

| 축 | 변수 | 의미 |
|---|---|---|
| P | 실리콘 커패시터, AI MLCC, FC-BGA ASP | 기존 IT 부품 대비 고부가 mix |
| Q | GPU/TPU/ASIC 패키지 수, HBM stack 수, AI 서버 보드 수 | AI CapEx와 직접 연동 |
| C | 수율, 소재비, 증설 감가상각 | 초기 ramp 리스크 |

왜 아직 완전히 가격에 반영되지 않았을 수 있나.

1. 시장은 삼성전기를 여전히 스마트폰 MLCC·카메라모듈 회사로 보는 관성이 강하다.
2. 실리콘 커패시터는 별도 카테고리라 sell-side 모델에 반영되기까지 시간이 걸린다.
3. 계약 매출 인식이 2027~2028년이어서 단기 EPS에는 늦게 들어온다.
4. 고객사가 비공개라 NVIDIA, Google, Broadcom/Marvell ASIC 중 어느 쪽인지 단정할 수 없다.

따라서 결론은 "추격 매수"가 아니라 "pullback buy"다. 삼성전기는 이번 I/O와 NVIDIA 실적 이후 한국 AI 인프라에서 가장 선명한 재분류 후보지만, 5/17 매크로 글의 게이트가 열리지 않은 상태에서 급등 추격은 효율이 낮다.

---

## 7. 삼성전자와 SK하이닉스 — Google TPU 다극화의 다른 의미

Google I/O는 NVIDIA 독점 약화 이벤트처럼 보일 수 있다. Google은 자체 TPU를 보유하고 있고, Broadcom, Marvell, MediaTek까지 ASIC 생태계가 넓어지는 흐름이 있다. 하지만 한국 메모리 관점에서는 결론이 다르다.

TPU도 HBM을 먹는다. ASIC도 HBM을 먹는다. inference TPU가 늘어도 memory bandwidth와 data movement 병목은 사라지지 않는다.

### SK하이닉스

SK하이닉스는 여전히 HBM 최고 품질 베타다. Google I/O의 agentic workload 증가, NVIDIA Rubin ramp, hyperscaler CapEx 확대는 모두 HBM 수요에 긍정적이다.

다만 알파는 줄었다. 시장은 이미 SK하이닉스를 HBM 대장주로 본다. 좋은 회사인 것과 지금 신규 진입이 좋은 가격인 것은 다르다.

```text
판단: Hold / Buy on pullback
좋은 점: HBM pure beta, 고객 신뢰, 수익성
주의점: crowding, 기대치, HBM4 경쟁 심화
```

### 삼성전자

삼성전자는 더 흥미롭다. 시장은 삼성전자를 "NVIDIA HBM 후발주자"로만 보는 경향이 있다. 그러나 Google/Broadcom/Marvell/ASIC 다극화가 진행되면 HBM 고객 구조도 NVIDIA 단일 프레임에서 벗어난다. 이 구도는 삼성전자의 variant perception에 유리하다.

삼성전자는 HBM, DRAM, eSSD, base die, foundry, advanced packaging을 모두 가진 복합 IDM이다. 문제는 execution이다. HBM4 고객 인증, base die, foundry 손익, 고객 다변화가 실제 숫자로 확인되어야 PER 5배 할인에서 벗어날 수 있다.

```text
판단: Watchlist / 조건부 Buy
좋은 점: HBM4, base die, eSSD, foundry optionality
주의점: execution discount, 파운드리 적자, HBM 인증 지연
```

이전 삼성전자 리레이팅 글의 결론과 동일하다. 삼성전자는 시장이 몰라서 싼 것이 아니다. 시장은 다운사이클 방어력과 고객 중립성을 요구하고 있다. Google I/O는 이 요구를 충족할 수 있는 하나의 경로를 보여줬다. 즉 NVIDIA 단일 체인이 아니라 TPU/ASIC 다극화에서 삼성전자의 HBM·foundry optionality가 살아날 수 있다는 경로다.

---

## 8. Broadcom vs Marvell — 한국 투자자가 봐야 할 것은 승자가 아니다

Google I/O 이후 미국에서는 Broadcom과 Marvell의 상대 성과도 중요하게 해석됐다. 핵심은 Google이 Broadcom을 버리는가가 아니다. Google이 AI ASIC 공급망을 멀티소싱하려 한다는 신호다.

Broadcom은 Google TPU 핵심 파트너이고, Google과 장기 계약을 맺었다는 보도가 있다. Marvell은 Google과 신규 AI chip, memory processing unit, inference TPU 논의 보도로 주목받았다. 이 움직임은 "Google TPU 수요가 약하다"가 아니라 "Google이 공급망 권력을 키우고 있다"는 뜻이다.

한국 투자자에게 중요한 것은 어느 미국 ASIC 벤더가 이기느냐가 아니다. Broadcom이 이기든 Marvell이 이기든 공통으로 필요한 병목이다.

| 미국 ASIC 변화 | 한국 공통 병목 |
|---|---|
| TPU 세대 증가 | HBM, base die, advanced packaging |
| inference TPU 확대 | HBM/LPDDR, eSSD, networking |
| memory processing unit | memory bandwidth, substrate, test socket |
| AI rack 증가 | 고다층 PCB, optical, 전력기기 |
| multi-sourcing | 고객 인증 기업의 가치 상승 |

그래서 한국 우선순위는 특정 미국 chip designer가 아니라 vendor-agnostic bottleneck이다. 삼성전기, 삼성전자, SK하이닉스, 테스트·소켓, 고다층 PCB, 전력 인프라 순으로 봐야 한다.

---

## 9. 실전 매매 전략

### 우선순위

| 순위 | 종목/군 | 판단 | 이유 |
|---:|---|---|---|
| 1 | 삼성전기 | Buy on pullback | 실리콘 커패시터 계약으로 AI 패키지 전력 무결성 병목이 수주로 확인 |
| 2 | 삼성전자 | Watchlist / 조건부 Buy | TPU/ASIC 다극화가 HBM 후발 discount를 줄일 수 있음 |
| 3 | SK하이닉스 | Hold / Buy on pullback | HBM 방향은 맞지만 consensus crowded |
| 4 | 한미반도체·ISC·리노공업·인텍플러스 | Watchlist | HBM·ASIC SKU 증가와 테스트·패키징 복잡도 수혜 |
| 5 | 이수페타시스·대덕전자·심텍·티엘비·코리아써키트 | Watchlist | AI 서버 PCB 수혜 가능하나 고객·제품·마진 확인 필요 |
| 6 | HD현대일렉트릭·LS ELECTRIC·효성중공업·일진전기 | Wait | AI DC 전력 수요는 명확하지만 밸류에이션 부담 가능 |

### Entry 조건

* **삼성전기**: 실리콘 커패시터 후속 고객, 증설 계획, AI MLCC/FC-BGA 매출 분리 가능성 확인.
* **삼성전자**: HBM4 고객 인증, HBM4 base die, Google/Broadcom/ASIC향 물량 또는 foundry 회복 신호.
* **SK하이닉스**: HBM4 pricing 유지, NVIDIA Rubin ramp, 10~15% 조정 또는 수급 과열 완화.
* **PCB/기판**: AI향 매출 비중, ASP premium, OPM 유지가 분기 실적으로 확인될 때.
* **테스트/소켓**: TPU/ASIC/HBM 고객 reference와 신규 socket 매출 확인.
* **전력기기**: 북미 데이터센터 수주잔고 증가율과 OPM 유지가 같이 확인될 때.

### Catalyst

* Gemini 3.5 Pro 출시와 AI Mode/Search agent 확산.
* Google Cloud 다음 분기 매출·backlog·CapEx 업데이트.
* Broadcom·Marvell 실적에서 Google/ASIC pipeline 코멘트.
* NVIDIA Rubin / Vera Rubin NVL72 ramp.
* 삼성전기 실리콘 커패시터 후속 공시.
* 삼성전자 HBM4 인증·base die·foundry 고객 코멘트.
* 한국 PCB/기판사의 2Q~3Q AI 서버향 매출 분리.

### Invalidation

* Google Search & other 성장률이 AI Mode 확대 이후 급격히 둔화.
* Google Cloud 성장률은 높지만 OPM이 20%대 초반 이하로 하락.
* AI CapEx 증가가 감가상각·전력비·networking cost로 이어져 Alphabet margin을 훼손.
* HBM ASP 하락 또는 HBM4 공급 과잉 신호.
* 삼성전기 실리콘 커패시터 계약이 저마진 또는 단일 고객 이벤트로 확인.
* PCB/기판주에서 AI 매출은 늘지만 OPM이 떨어지는 경우.
* 5/17 매크로 게이트가 계속 미통과되어 고PER AI 인프라 멀티플이 압축되는 경우.

---

## 10. 자주 묻는 질문

### "Google I/O가 NVIDIA에 부정적인가?"

단기적으로는 일부 부정적 해석이 가능하다. Google이 TPU를 키우고, Broadcom·Marvell 등 ASIC 생태계를 확대하면 NVIDIA 독점 premium은 일부 낮아질 수 있다. 하지만 한국 공급망 관점에서는 오히려 다극화가 긍정적이다. GPU든 TPU든 ASIC이든 HBM, 패키징, PCB, 전력 인프라가 필요하기 때문이다.

### "Alphabet을 사는 게 더 낫지 않나?"

Alphabet은 좋은 회사다. Search 방어력, Cloud 성장성, full-stack AI 구조가 모두 강하다. 다만 현재 시가총액과 이익배수는 이미 winner premium을 상당 부분 반영한다. 이번 글의 결론은 Alphabet이 나쁘다는 것이 아니라, Google I/O 직후 신규 알파는 Alphabet보다 한국 AI 인프라 병목 쪽이 더 크다는 것이다.

### "왜 삼성전기가 1순위인가?"

HBM은 이미 시장이 알고 있다. 반면 AI 패키지 내부 전력 안정화, 실리콘 커패시터, AI MLCC, FC-BGA를 묶은 power integrity thesis는 아직 시장 분류가 덜 정교하다. 여기에 1.557조원 계약이라는 실제 수주가 붙었다. 스토리와 숫자가 동시에 있는 드문 구간이다.

### "PCB/기판주는 다 사도 되나?"

아니다. 이 구간이 가장 테마 과잉 위험이 크다. AI 서버향이라는 이름은 쉽게 붙지만, 실제 고객, 제품, ASP premium, OPM이 확인되지 않으면 단기 수급으로 끝날 수 있다. 이제부터는 "AI향 매출 증가 + 마진 유지"가 동시에 찍히는 기업만 남긴다.

---

## 11. 마지막 한 줄

Google I/O 2026은 검색이 죽었다는 이벤트가 아니었다. 오히려 Google이 검색, 메일, 문서, 쇼핑, 개발툴, 영상, 안경까지 모두 agent interface로 바꾸겠다고 선언한 이벤트였다. 검색창은 query box에서 task box로 이동하고, 개발툴은 IDE에서 agent runtime으로 이동하며, 쇼핑은 keyword funnel에서 Universal Cart로 이동한다.

Alphabet의 1Q26 숫자는 이 전환이 아직 Search를 훼손하지 않았음을 보여준다. Search & other 매출은 YoY 약 19% 성장했고, Cloud 매출은 약 63% 성장했으며, Cloud OPM은 32.9%까지 올라왔다. 현재까지는 "AI가 Google을 죽인다"보다 "Google이 AI를 기존 distribution에 흡수한다"가 더 맞다.

하지만 진짜 투자 포인트는 Alphabet 자체보다 AI 인프라 병목이다. Google은 월간 처리 토큰이 2024년 5월 9.7조 개에서 2026년 5월 3.2경 개 이상으로 늘었다고 밝혔다. CapEx도 2022년 310억 달러에서 올해 1800억~1900억 달러 수준으로 커질 수 있다고 설명했다. 이 변화는 HBM, 패키징, 전력 무결성, PCB, 전력 인프라의 수요 함수다.

한국 우선순위는 명확하다. **삼성전기**는 실리콘 커패시터 대형 계약으로 AI 패키지 전력 무결성 병목이 수주로 확인됐다. **삼성전자**는 TPU/ASIC 다극화가 HBM 후발 discount를 줄일 수 있는 옵션이다. **SK하이닉스**는 여전히 HBM 최강자지만 이미 crowded trade다. **PCB/기판·테스트·전력기기**는 수혜 가능성이 크지만 실적 확인이 필요하다.

결론은 간단하다. Google I/O 이후의 알파는 "어느 모델이 더 똑똑한가"가 아니라 "agent 사용량 증가가 어느 병목에 돈을 쓰게 만드는가"에서 나온다. 답은 Alphabet만이 아니다. HBM, 패키징, 실리콘 커패시터, 고다층 PCB, 데이터센터 전력이다. 그중 지금 가장 신선한 한국 알파는 삼성전기다. 다만 매크로 게이트가 열리기 전까지는 추격보다 확인 후 분할이 맞다.

---

*이 글은 리서치와 논평으로만 활용해야 하며 투자 조언이 아닙니다. Google I/O 2026 발표 내용(Gemini Omni, Gemini 3.5, Search agents, Gemini Spark, Universal Cart, Antigravity, Android XR)은 Google 공식 I/O 컬렉션 및 Google 공식 블로그 기준입니다. Alphabet 1Q26 실적(매출 1098.96억 달러, 영업이익 396.96억 달러, Search & other 603.99억 달러, Google Cloud 200.28억 달러, Cloud 영업이익 65.98억 달러)은 Alphabet 1Q26 SEC 제출 자료 기준입니다. 월간 처리 토큰 3.2경 개 이상, Gemini app 월간 9억 명 이상, CapEx 1800억~1900억 달러 전망은 Sundar Pichai의 Google I/O 2026 발언 기준입니다. 삼성전기 실리콘 커패시터 1조5570억원 공급계약(기간 2027/01/01~2028/12/31, 최근 매출 대비 13.8%)은 2026년 5월 20일 회사 공시 및 국내 주요 언론 보도 기준입니다. 삼성전기 AI 서버 전력 아키텍처 관련 설명은 삼성전기 공식 기술자료 기준입니다. Broadcom·Marvell·Google ASIC 관련 내용은 Reuters 등 외신 보도 기준이며 확정 계약과 협상 보도가 섞여 있어 구분이 필요합니다. 종목 우선순위, 밸류체인 매핑, 매수 조건, 폐기 조건은 분석가의 현재 framework이며 실제 결과와 다를 수 있습니다. 글로벌 매크로 환경(금리, 유가, 환율, VIX, 외국인 수급)이 종목 가격에 추가 영향을 줄 수 있습니다. 분석이 틀릴 수도 있습니다. 데이터 기준일: 2026년 5월 21일 KST.*
