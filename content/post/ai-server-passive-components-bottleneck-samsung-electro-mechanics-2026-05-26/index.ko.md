---
title: "AI 서버 수동소자 병목: GPU보다 작은 전력 안정화 부품이 왜 중요해졌나"
date: 2026-05-26
description: "AI 서버 수동소자 병목은 GPU가 순간적으로 먹는 전기를 안정적으로 공급·완충·필터링하는 MLCC, 실리콘 커패시터, 인덕터 같은 부품이 고스펙화되는 현상이다. 삼성전기의 MLCC·FC-BGA·실리콘 커패시터 리레이팅을 비전공자 눈높이에서 설명한다."
categories: ["Stock-Analysis"]
tags:
  - "삼성전기"
  - "009150"
  - "AI 서버"
  - "수동소자"
  - "MLCC"
  - "실리콘 커패시터"
  - "FC-BGA"
  - "전력무결성"
  - "HBM"
  - "GPU"
  - "AI 인프라"
slug: ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26
valley_body_mode: teaser
valley_cashtags:
  - 삼성전기
valley_cashtag_exclude:
  - 삼성전자
  - SK하이닉스
---

> 삼성전기 시리즈 후속편입니다. 이전 글은 [삼성전기 시총 100조 돌파](/ko/post/samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26/), [실리콘 커패시터 1.5조원 계약](/ko/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/), [MLCC와 실리콘 커패시터 이해하기](/ko/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/), [엔비디아 이후 AI 반도체 병목](/ko/post/ai-chip-design-data-movement-fcbga-bottleneck-2026-05-24/)을 참고하세요. 관련 허브는 [AI HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/), [AI 기판·PCB 허브](/ko/page/korea-ai-pcb-substrate-hub/), [반도체 밸류체인 허브](/ko/page/korea-semiconductor-equipment-ip-hub/)입니다.

## TL;DR

- <strong>AI 서버 수동소자 병목은 GPU가 부족해서가 아니라, GPU가 먹는 전기를 안정적으로 공급·완충·필터링하는 작은 부품들이 고스펙화되며 부족해지는 현상</strong>입니다.
- 쉽게 말하면 AI 서버는 초고성능 엔진이고, <strong>MLCC·실리콘 커패시터·인덕터는 연료펌프·충격흡수장치·정수필터</strong>입니다.
- NVIDIA DGX GB200 랙은 랙당 약 <strong>120kW</strong>를 소비하고, Lenovo의 GB300 NVL72 구성은 랙당 <strong>135kW TDP, 최대 155kW 피크</strong>를 언급합니다. AI 서버는 이제 일반 서버가 아니라 전기 먹는 공장 설비에 가깝습니다. ([NVIDIA][1], [Lenovo][2])
- 투자 관점에서는 <strong>MLCC 전체가 아니라 AI 서버용 고용량·저저항·저노이즈·초박형 부품</strong>이 병목입니다.
- 삼성전기가 주목받는 이유는 <strong>MLCC + FC-BGA + 실리콘 커패시터</strong>를 한 회사 안에서 연결할 수 있기 때문입니다. 다만 이것은 좋은 회사 논리이지, 모든 가격에서 좋은 주식이라는 뜻은 아닙니다.

## 1. 한 문장 설명

<strong>AI 서버 수동소자 병목은 GPU가 순간적으로 엄청난 전기를 빨아먹을 때 전압이 흔들리지 않도록 막아주는 전기 완충재가 더 많이, 더 고성능으로 필요해진다는 이야기입니다.</strong>

AI 성능 경쟁은 보통 GPU, HBM, 네트워크 칩으로 설명됩니다. 맞는 말입니다. 그런데 이 칩들이 제대로 작동하려면 더 아래층의 전기 문제가 먼저 해결돼야 합니다.

GPU는 연산할 때 전력을 일정하게 쓰지 않습니다. 연산 부하가 바뀌면 전류가 순간적으로 튑니다. 이때 전압이 흔들리면 연산 오류, 성능 저하, 시스템 불안정이 생깁니다. 그래서 GPU와 HBM 주변에는 전압을 잡아주는 작은 부품이 촘촘하게 필요합니다.

그 작은 부품이 바로 <strong>MLCC, 실리콘 커패시터, 인덕터, 필터, 페라이트, VRM 주변 부품</strong>입니다.

## 2. 수동소자는 무엇인가

수동소자는 스스로 계산하지 않습니다. 대신 전기 흐름을 안정화합니다.

| 부품 | 비전공자용 비유 | AI 서버에서 하는 일 |
|---|---|---|
| <strong>커패시터 / MLCC</strong> | 물탱크, 쇼크업소버 | GPU가 순간적으로 전기를 더 달라고 할 때 바로 공급하고 전압 흔들림을 흡수 |
| <strong>실리콘 커패시터</strong> | GPU 바로 옆 초소형 비상 배터리 | GPU·HBM 패키지 안쪽 또는 바로 근처에서 전력 노이즈를 가장 가까운 위치에서 제거 |
| <strong>인덕터</strong> | 전기 흐름을 부드럽게 만드는 관성 장치 | 전압 변환 과정에서 전류를 안정적으로 흐르게 함 |
| <strong>저항·필터·페라이트</strong> | 속도 제한기, 잡음 제거 필터 | 고속 신호와 전력선의 노이즈를 줄임 |
| <strong>VRM 주변 부품</strong> | GPU용 전력 조리기 | 48V·12V 전원을 GPU가 먹는 1V 이하 전압으로 변환 |

TDK는 데이터센터 전원 구조를 <strong>UPS → PSU → IBC → VRM → CPU/GPU 전압</strong>으로 설명합니다. 각 단계에서 고효율, 낮은 리플, 내열성, 장기 신뢰성이 필요합니다. ([TDK][3])

투자자에게 중요한 포인트는 이것입니다. AI 서버가 커질수록 전원 경로의 모든 단계가 커지지만, <strong>가장 고부가가치가 붙는 곳은 GPU와 가장 가까운 위치</strong>입니다.

## 3. 왜 AI 서버에서 갑자기 병목이 되는가

### 3.1 GPU는 낮은 전압으로 엄청난 전류를 먹습니다

GPU와 CPU는 보통 <strong>1V 이하의 낮은 전압</strong>에서 동작합니다. 그런데 연산 부하가 바뀔 때 전류는 <strong>수십~수백 암페어 단위로 즉시 변동</strong>할 수 있습니다. 삼성전기는 이 때문에 GPU 근처의 고용량 MLCC가 전류 버퍼 역할을 해야 안정적인 시스템 동작이 가능하다고 설명합니다. ([Samsung Electro-Mechanics][4])

비유하면 이렇습니다.

```text
일반 서버: 수도꼭지를 일정하게 틀어놓는 수준
AI 서버: 소방호스를 수십 개 묶어놓고 동시에 열었다 닫았다 하는 수준
```

물압이 출렁이면 배관이 흔들립니다. 전압이 출렁이면 GPU가 흔들립니다. 그래서 전력 안정화 부품이 AI 서버 성능의 일부가 됩니다.

### 3.2 평균 전력보다 더 무서운 것은 순간 피크입니다

NVIDIA는 GB300 NVL72에서 에너지 저장 기능을 가진 PSU를 통해 AI 워크로드의 전력 피크를 완화한다고 설명합니다. 대규모 학습에서는 수천 개 GPU가 동시에 움직이기 때문에 전력 수요가 갑자기 변동하고, 이 변동은 전력망에도 부담이 됩니다. NVIDIA는 새 PSU가 AI 워크로드의 전력 스파이크를 완화하고 피크 그리드 수요를 최대 30% 줄인다고 설명합니다. ([NVIDIA Developer][5])

이 말은 간단합니다.

<strong>진짜 문제는 평균 전력만이 아니라 순간 피크입니다.</strong>

전력 피크를 잡으려면 GPU 가까이에 커패시터가 촘촘히 깔려 있어야 합니다. 멀리 있는 전원장치는 반응이 늦습니다. 그래서 <strong>GPU 바로 옆</strong>, <strong>HBM 바로 옆</strong>, <strong>패키지 내부</strong> 부품의 가치가 올라갑니다.

### 3.3 부품 개수도 늘고, 사양도 올라갑니다

The Elec은 일반 스마트폰에는 MLCC가 1,000개 이상 들어가며, AI 서버 보드는 그 <strong>10~20배</strong> 수준의 MLCC를 사용한다고 보도했습니다. 단순 적용하면 스마트폰 1,000개 기준 AI 서버 보드는 <strong>10,000~20,000개 이상</strong>입니다. ([The Elec][6])

다만 이 숫자는 범용 BOM처럼 고정된 값이 아닙니다. 서버 플랫폼, 보드 구성, 전력 아키텍처에 따라 달라집니다. 핵심은 숫자의 정확한 개수보다 방향입니다.

<strong>AI 서버는 더 많은 MLCC를 쓰고, 그 MLCC의 사양도 더 높아진다.</strong>

## 4. 병목의 본질은 “작은 부품이 많이 필요하다”가 아닙니다

더 정확히는 네 가지가 동시에 발생합니다.

| 병목 요인 | 쉬운 설명 | 투자적 의미 |
|---|---|---|
| <strong>수량 증가</strong> | 서버 한 대당 들어가는 부품 수가 폭증 | 출하량 증가 |
| <strong>사양 상승</strong> | 아무 MLCC나 안 되고 고성능품이 필요 | ASP 상승 가능 |
| <strong>위치 변화</strong> | GPU에서 더 가까운 곳에 배치해야 함 | 실리콘 커패시터·임베디드 기판 가치 상승 |
| <strong>검증 난이도 상승</strong> | 한번 서버에 들어가면 고장 나면 안 됨 | 고객 인증, 공급망 락인 강화 |

Samsung Electro-Mechanics는 AI 서버 전력 아키텍처에서 알루미늄 폴리머 커패시터를 MLCC로 대체하는 흐름이 확대되고 있다고 설명합니다. MLCC는 더 낮은 높이와 작은 면적에서 필요한 용량을 구현할 수 있고, 낮은 ESR·ESL 덕분에 빠른 전압 응답에 유리합니다. ([Samsung Electro-Mechanics][7])

즉 병목은 “MLCC가 많이 들어간다”가 아닙니다.

<strong>AI 서버에 맞는 고성능 MLCC가 필요해진다</strong>가 핵심입니다.

## 5. MLCC와 실리콘 커패시터의 차이

### MLCC: 보드 위의 대량 전기 완충재

MLCC는 메인보드와 GPU 보드 곳곳에 깔립니다. 역할은 전압 안정화, 노이즈 제거, 순간 전류 보완입니다. AI 서버에서는 48V 전원 아키텍처, GPU 보드, 네트워크 보드, PCIe, NIC 주변까지 넓게 쓰입니다.

비유하면 <strong>건물 곳곳에 놓인 소화기</strong>입니다. 하나하나가 서버 전체 원가에서 차지하는 비중은 작아 보여도, 전체 시스템 안정성에는 필수입니다.

### 실리콘 커패시터: GPU 패키지 안쪽의 초근접 전기 안정화 장치

실리콘 커패시터는 더 고급 영역입니다. GPU와 HBM 같은 고성능 반도체 패키지 내부 또는 아주 가까운 위치에 들어갑니다.

삼성전기는 2026년 5월 20일 글로벌 대형 기업과 약 <strong>1.5조원 규모</strong>의 실리콘 커패시터 공급계약을 체결했다고 발표했습니다. 계약기간은 <strong>2027년 1월 1일~2028년 12월 31일</strong>입니다. 삼성전기는 이 부품이 AI 서버용 고성능 반도체 패키지 내부에서 전력 공급 안정성을 높인다고 설명했습니다. ([삼성전기][8])

핵심 차이는 거리입니다.

| 구분 | 위치 | 역할 | 비유 |
|---|---|---|---|
| MLCC | 보드 위 여러 곳 | 전원 안정화의 대량 기본재 | 건물 곳곳의 소화기 |
| 실리콘 커패시터 | GPU·HBM 바로 옆 또는 패키지 내부 | 초고속 전력 흔들림 억제 | 엔진 실린더 바로 옆 연료 압력 조절기 |

삼성전기는 실리콘 커패시터가 기존 MLCC 대비 ESL/ESR이 <strong>100배 이상 낮다</strong>고 설명합니다. 여기서 ESL/ESR은 쉽게 말해 전기가 빠르게 오갈 때 생기는 방해 요소입니다. 낮을수록 고속 GPU 주변에서 유리합니다. ([삼성전기][8])

## 6. 왜 아무 회사나 못 하나

수동소자는 겉보기에는 단순해 보입니다. 하지만 AI 서버용 고급 부품은 다릅니다.

첫째, <strong>작아야 합니다.</strong> GPU 주변 공간은 매우 좁습니다. 부품이 커지면 패키지와 기판 설계가 어려워집니다.

둘째, <strong>빠르게 반응해야 합니다.</strong> GPU 전류가 순간적으로 튀면 커패시터가 즉시 전기를 내줘야 합니다. 반응이 느리면 전압이 떨어지고 연산 오류가 납니다.

셋째, <strong>열을 버텨야 합니다.</strong> AI 서버 내부는 고온·고전력 환경입니다. 성능이 좋아도 열에서 버티지 못하면 탈락입니다.

넷째, <strong>고객 인증이 어렵습니다.</strong> 삼성전기는 실리콘 커패시터 시장이 높은 기술 진입장벽과 까다로운 고객 인증 절차 때문에 소수 기업 중심으로 과점되어 왔다고 설명합니다. ([삼성전기][8])

투자자 언어로 번역하면 이렇습니다.

<strong>일단 들어가면 쉽게 바뀌지 않는 부품입니다.</strong>

AI 서버용 수동소자는 단가가 서버 전체 BOM에서 압도적으로 크지는 않아도, 고장 나면 전체 서버 안정성을 무너뜨릴 수 있습니다. 그래서 고객은 검증된 공급사를 선호합니다.

## 7. 병목이 생기는 위치를 아주 쉽게 그리면

```text
전력망
  ↓
데이터센터 전원장치
  ↓
서버 랙 전원공급장치 PSU
  ↓
48V / 12V 전원 변환
  ↓
VRM: GPU가 먹는 1V 이하 전압으로 변환
  ↓
MLCC·인덕터·필터가 전압 흔들림 제거
  ↓
GPU / HBM 바로 옆 실리콘 커패시터가 마지막으로 안정화
  ↓
AI 연산 정상 수행
```

병목은 아래쪽으로 갈수록 강해집니다.

<strong>전원장치 병목 → 보드 전력부품 병목 → GPU 패키지 내부 수동소자 병목</strong>

가장 고부가가치 영역은 GPU와 가장 가까운 곳입니다.

## 8. 삼성전기 투자 해석

삼성전기가 주목받는 이유는 단순히 MLCC를 만들기 때문이 아닙니다. <strong>MLCC, FC-BGA, 실리콘 커패시터를 동시에 연결할 수 있는 한국 대형 상장사</strong>이기 때문입니다.

| 레이어 | 삼성전기 노출 | AI 서버에서의 의미 |
|---|---|---|
| MLCC | 컴포넌트 사업부 | 보드와 칩 주변 전력 안정화 |
| FC-BGA | 패키지솔루션 | GPU·CPU·ASIC을 실장하는 고성능 패키지 기판 |
| 실리콘 커패시터 | 신규 고부가 부품 | GPU·HBM 패키지 내부 초근접 전력 안정화 |
| 카메라모듈 | 광학통신솔루션 | AI thesis에는 직접 핵심은 아니며 전사 마진 희석 변수 |

이전 글에서 정리했듯, 삼성전기 시총 100조원은 이미 단순 MLCC 사이클보다 훨씬 높은 기대를 반영합니다. 따라서 오늘 글의 결론은 “무조건 사자”가 아닙니다. 더 정확한 결론은 다음입니다.

<strong>삼성전기 리레이팅의 기술적 전제는 유효하다. 그러나 주가가 더 오르려면 이 전제가 전사 OPM과 2027~2028년 이익 추정치로 확인되어야 한다.</strong>

봐야 할 지표는 다섯 가지입니다.

1. AI 서버용 MLCC ASP 상승과 고객 인증
2. 실리콘 커패시터 매출 인식 속도
3. 실리콘 커패시터 추가 고객·추가 플랫폼 수주
4. FC-BGA의 AI 서버·네트워크향 매출 성장
5. 전사 OPM이 15%를 넘어 20%에 접근하는지

## 9. 비전공자용 최종 비유

AI 서버를 <strong>초고성능 레이싱카 72대가 한 차고 안에서 동시에 급가속·급제동하는 구조</strong>라고 보면 됩니다.

GPU는 엔진입니다.
HBM은 고속 연료통입니다.
기판은 도로입니다.
전원장치는 주유소입니다.
MLCC와 실리콘 커패시터는 <strong>엔진이 덜컥거리지 않게 해주는 초정밀 연료압 조절 장치</strong>입니다.

예전에는 엔진만 좋으면 됐습니다.
이제는 엔진이 너무 강해져서, 주변의 연료압·진동·열·전기 노이즈를 잡는 부품이 성능의 일부가 됐습니다.

그래서 AI 서버 시대의 수동소자는 더 이상 “싸고 흔한 주변 부품”이 아닙니다.

<strong>GPU가 제 성능을 내기 위한 전력 안정성 병목 부품</strong>입니다.

투자 관점에서는 이것이 삼성전기, 무라타, TDK 같은 고급 수동소자 업체의 리레이팅 논리입니다.

## 근거 분류

### [Fact]

- NVIDIA DGX GB200 랙은 약 <strong>120kW</strong>의 랙 전력 소비를 사용합니다. ([NVIDIA][1])
- Lenovo GB300 NVL72 구성은 랙당 <strong>135kW TDP</strong>, 워크로드와 EDP 동작에 따라 최대 <strong>155kW 피크</strong>를 언급합니다. ([Lenovo][2])
- TDK는 데이터센터 전원 경로를 <strong>UPS → PSU → IBC → VRM → CPU/GPU 전압</strong>으로 설명합니다. ([TDK][3])
- Samsung Electro-Mechanics는 GPU와 CPU가 1V 이하에서 동작하고 전류가 수십~수백 암페어 단위로 즉시 변할 수 있어 고용량 MLCC가 전류 버퍼 역할을 해야 한다고 설명합니다. ([Samsung Electro-Mechanics][4])
- 삼성전기는 2027~2028년 약 <strong>1.5조원</strong> 규모의 실리콘 커패시터 공급계약을 발표했습니다. ([삼성전기][8])

### [Inference]

- AI 서버 수동소자 병목은 단순 부품 수량 증가보다 <strong>수량 증가 + 사양 상승 + GPU 근접 배치 + 고객 인증 난이도 상승</strong>의 결합입니다.
- 삼성전기 리레이팅은 MLCC 단일 사이클보다 <strong>MLCC + FC-BGA + 실리콘 커패시터</strong>를 묶은 AI 패키지 전력무결성 thesis에 가깝습니다.

### [Speculation]

- 실리콘 커패시터가 삼성전기 전사 OPM을 20% 근처로 끌어올릴지는 아직 검증 전입니다.
- AI 서버용 MLCC ASP 상승과 공급 부족이 몇 년 지속될지는 hyperscaler CapEx, GPU 플랫폼 전환, 경쟁사 증설에 따라 달라질 수 있습니다.

### [Blocked]

- 삼성전기 실리콘 커패시터 계약의 정확한 고객명, 제품별 마진, 제품별 백로그는 공개되지 않았습니다.
- AI 서버 보드당 MLCC 탑재 수량은 플랫폼마다 다르므로, 10~20배 수치는 산업 보도 기반의 방향성 지표로만 써야 합니다.

---

Disclaimer: 이 글은 정보 제공과 리서치 목적입니다. 특정 종목의 매수·매도 추천이 아닙니다. 언급된 기업과 수치는 투자 판단의 예시이며, 실제 의사결정에는 본인의 리스크 허용도와 추가 실사를 반영해야 합니다.

[1]: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html "Hardware — NVIDIA DGX GB Rack Scale Systems User Guide"
[2]: https://lenovopress.lenovo.com/lp2357-lenovo-nvidia-gb300-nvl72-rack-scale-ai "Lenovo NVIDIA GB300 NVL72 Rack Scale AI Product Guide"
[3]: https://product.tdk.com/en/techlibrary/applicationnote/mlcc-solution-for-data-center-psu.html "MLCC Solutions for Data Center (AI Server) Power Systems | TDK"
[4]: https://product.samsungsem.com/product-news/view.do?idx=3622&language=en "MLCC: The Key Component for Power, Computing, Network and the New Era of AI Servers | Samsung Electro-Mechanics"
[5]: https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/ "How New GB300 NVL72 Features Provide Steady Power for AI | NVIDIA Technical Blog"
[6]: https://www.thelec.net/news/articleView.html?idxno=5588 "Samsung Electro-Mechanics mulls MLCC price increase | The Elec"
[7]: https://product.samsungsem.com/product-news/view.do?idx=3742&language=en "The Shift of AI Server Power Architectures | Samsung Electro-Mechanics"
[8]: https://m.samsungsem.com/kr/newsroom/news/view.do?id=10309 "삼성전기, 글로벌 대형기업과 1.5조 규모 실리콘 캐패시터 공급계약 체결 | 삼성전기"
