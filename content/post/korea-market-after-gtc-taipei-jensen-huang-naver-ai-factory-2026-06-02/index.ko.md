---
title: "젠슨 황을 바라보는 한국 증시: 간밤에 무슨 일이 있었나"
date: 2026-06-02T08:45:00+09:00
description: "GTC Taipei 이후 NVIDIA의 메시지를 AI Factory, Vera CPU, Agent Runtime, AI PC, Physical AI로 분해하고, 한국 증시가 삼성전자·전력 인프라·로봇·두산·NAVER Cloud를 어떻게 다시 가격화해야 하는지 점검한다."
categories: ["Market-Outlook", "Company-Deep-Dive"]
tags:
  - "젠슨 황"
  - "NVIDIA"
  - "GTC Taipei"
  - "AI factory"
  - "Physical AI"
  - "Vera Rubin"
  - "Vera CPU"
  - "NAVER"
  - "NAVER Cloud"
  - "Sovereign AI"
  - "삼성전자"
  - "LS ELECTRIC"
  - "두산"
  - "로봇"
  - "한국 증시"
slug: korea-market-after-gtc-taipei-jensen-huang-naver-ai-factory-2026-06-02
valley_cashtags:
  - 삼성전자
  - NAVER
  - LS ELECTRIC
  - LG전자
  - 두산
  - 두산로보틱스
  - 로보티즈
  - 레인보우로보틱스
draft: false
---

> 연결 맥락
> 이 글은 [ADR 18.1%의 좁은 길: 젠슨 황을 바라보는 한국 증시에 필요한 촉매](/ko/post/korea-narrow-market-jensen-huang-catalyst-gtc-taipei-2026-06-01/)와 [네이버 시총 36.7조원: 두나무 결합 현금성자산 8조원, 미래에셋 지분 3조원은 반영됐나](/ko/post/naver-rerating-dunamu-mirae-ai-cloud-stablecoin-turnaround-2026-05-31/)의 후속입니다. 전자는 2026년 6월 1일 한국장의 좁은 수급과 젠슨 황 촉매를 봤고, 후자는 NAVER를 포털주가 아니라 AI cloud·금융자산·스테이블코인 옵션으로 다시 봤습니다. 이어지는 NAVER 전용 후속글은 [젠슨 황은 왜 네이버와 만날까](/ko/post/naver-nvidia-jensen-huang-softbank-ytl-dell-ai-factory-2026-06-05/)입니다. 이번 글은 간밤 NVIDIA GTC Taipei 메시지를 한국 증시의 다음 질문으로 번역합니다. 관련 허브는 [한국 데일리 마켓 허브](/ko/page/korea-daily-market-hub/), [한국 AI 기업 허브](/ko/page/korean-ai-companies-hub/), [한국 반도체 / HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/)입니다.

## TL;DR

간밤 확인된 핵심은 단순합니다. NVIDIA는 GTC Taipei에서 "더 강한 GPU"만 말한 것이 아니라 **AI Factory, Vera CPU, Agent Runtime, AI PC, Physical AI**를 한 번에 전면화했습니다. 한국 증시가 봐야 할 것도 HBM 하나가 아닙니다. 메모리, 전력, 네트워킹, 보안, 스토리지, GPUaaS, sovereign AI, 로봇·공장 자동화가 같은 AI 인프라 스택 안으로 들어왔습니다.

한국 시장의 1차 반응은 이미 나왔습니다. 삼성전자, LG전자, NAVER, 로봇주, LS ELECTRIC이 강했고, 삼성전기·대덕전자·심텍·티엘비 같은 기존 AI 부품주는 차익실현을 맞았습니다. 하지만 이것은 "한국 증시 전체 리스크온"이 아닙니다. 전일 ADR은 18.1%에 불과했습니다. 아직은 **젠슨 황을 바라보는 좁은 시장**입니다.

핵심 질문은 다음으로 바뀌어야 합니다.

> NVIDIA와 누가 만나는가가 아니라, 한국 기업이 NVIDIA AI factory의 어떤 병목을 맡는가?

이 기준에서 가장 구조적인 축은 네 개입니다.

| 축 | 한국 번역 | 핵심 확인 |
|---|---|---|
| AI Factory compute | 삼성전자, SK하이닉스 | HBM4E qualification, 서버 DRAM, eSSD, 고객 인증 |
| AI Factory physical layer | LS ELECTRIC, 이수페타시스, 전력·네트워크 부품 | 800VDC, 전력기기, 고속 네트워킹, 광통신 |
| Sovereign AI / GPUaaS | NAVER Cloud, SKT, 삼성SDS, LG CNS | GPU utilization, 장기계약, token revenue, gross margin |
| Physical AI | LG전자, 현대차, 로봇주, 두산그룹 | 실제 공동개발, 로봇·공장·자동차 매출 경로 |

제 판단은 **추격매수보다 확인 후 선별**입니다. 삼성전자는 core exposure지만 급등 후 눌림이 낫고, LS ELECTRIC 같은 전력 인프라는 AI factory의 덜 가짜인 파생축입니다. NAVER는 이번 이벤트로 리레이팅 논거가 더 강해졌지만, 6월 1일 수급은 외국인 매도와 기관 매수가 충돌했습니다. NAVER Cloud의 GPUaaS 매출, utilization, sovereign AI 계약, Enterprise AI 마진이 확인되어야 진짜 리레이팅입니다.

---

## 1. 간밤 NVIDIA 메시지: GPU 제품 발표가 아니라 AI factory 운영체계 발표

[Fact] NVIDIA는 GTC Taipei에서 **Vera Rubin 플랫폼이 full production ramp 단계**에 들어갔다고 발표했습니다. 공식 자료 기준 Vera Rubin은 대만 150개 파트너, 350개 이상 공장, 30개국 공급망을 통해 ramp 중이며, production shipment는 2026년 가을부터 시작될 예정입니다. NVIDIA는 Vera Rubin을 5개 purpose-built rack이 하나의 POD-scale AI supercomputer처럼 작동하는 플랫폼으로 설명했습니다. ([NVIDIA Newsroom][1])

중요한 문장은 "AI factory"입니다. NVIDIA는 Vera Rubin을 단일 GPU 보드가 아니라 다음 요소가 묶인 factory platform으로 제시했습니다.

| 레이어 | NVIDIA 메시지 | 투자 번역 |
|---|---|---|
| Compute | Vera Rubin NVL72, Rubin GPU | HBM, advanced packaging, server DRAM |
| CPU | Vera CPU | AI agent workload에서 CPU 병목 부상 |
| Networking | Spectrum-X Ethernet Photonics, CPO | 광통신, 스위치, 고속 PCB, 전력효율 |
| Storage / security | BlueField-4 STX, DOCA | KV/context, zero-trust, DPU, storage tier |
| Operations | DSX AI Factory platform | 설계, 전력, 냉각, lifecycle, multi-tenant 운영 |

[Fact] NVIDIA 공식 블로그도 GTC Taipei 핵심을 **AI factories, agentic AI, physical AI**로 정리했습니다. 2026년 6월 1일 업데이트에는 Vera Rubin, MGX, 800VDC, RTX Spark, robotics, Isaac GR00T, Cosmos 3, DRIVE Hyperion 같은 항목이 함께 배치됐습니다. ([NVIDIA Blog][2])

즉 간밤 메시지는 "더 많은 GPU를 판다"가 아니라 다음에 가깝습니다.

> AI는 모델을 학습시키는 장비가 아니라, 기업과 국가가 운영하는 생산설비다. 이 생산설비의 병목은 GPU, CPU, 네트워크, 전력, 스토리지, 보안, 운영 소프트웨어, 로봇·공장 데이터까지 퍼진다.

한국 증시가 반응한 이유도 여기에 있습니다. 한국은 HBM만 가진 시장이 아닙니다. 메모리, 패키징, MLCC, 기판, 전력기기, 조선·공장 데이터, 클라우드, 통신, 로봇, 자동차까지 AI factory의 여러 layer를 동시에 갖고 있습니다.

---

## 2. 한국 시장이 잘못 보기 쉬운 지점: "엔비디아 방한 테마"와 "AI factory 병목"은 다르다

Reuters 계열 보도는 젠슨 황 CEO가 한국 경영진과 만날 예정이고, NVIDIA가 Computex 기간 중 Korean Partner Night를 열 계획이라고 전했습니다. 같은 보도는 삼성전자, LG전자, NAVER, SK하이닉스 등 한국 기술주의 급등을 이 기대와 연결했습니다. ([MarketScreener / Reuters][3])

다만 이것은 아직 **공식 수주**가 아닙니다. Korea JoongAng Daily도 젠슨 황의 한국 방문 가능성을 보도했지만, 투자자가 확인해야 할 것은 사진이나 회동 자체가 아닙니다. ([Korea JoongAng Daily][4])

구분은 이렇게 해야 합니다.

| 항목 | 낮은 확신 | 높은 확신 |
|---|---|---|
| 회동 | 누구를 만나는가 | 어떤 공동개발·공급계약·투자계획이 나오는가 |
| 테마 | NVIDIA 관련주 | AI factory 병목을 실제로 해결하는 기업 |
| 주가 반응 | 하루 가격 급등 | 외국인·기관 수급 지속 + EPS revision |
| NAVER | 회동 기대 | GPUaaS utilization, sovereign AI 계약, Enterprise AI 마진 |
| 로봇주 | physical AI 키워드 | 고객·매출·부품 레이어의 반복성 |

그래서 6월 1일 장세의 의미는 "한국 시장이 좋아졌다"가 아니라 **한국 시장이 NVIDIA ecosystem 안에서 자신을 다시 분류하기 시작했다**는 것입니다.

---

## 3. 한국 증시의 네 가지 번역

### 3.1 삼성전자: HBM4E catch-up이 AI factory core exposure로 다시 가격화

삼성전자는 2026년 6월 1일 +10.09% 상승했습니다. Reuters 계열 보도는 삼성전자가 최신 HBM 샘플 출하를 시작했고, AI data center에 중요한 제품에서 경쟁력을 회복할 수 있다는 기대가 주가를 지지했다고 설명했습니다. ([MarketScreener / Reuters][3])

삼성전자 thesis는 이제 단순히 "HBM을 판다"가 아닙니다.

| 레이어 | 삼성전자 노출 |
|---|---|
| HBM4E | NVIDIA qualification과 고객 인증 |
| HBM base die / foundry | advanced logic, packaging optionality |
| server DRAM / SOCAMM | AI server memory hierarchy |
| eSSD / storage | KV cache와 AI storage 병목 |
| 파운드리 | LPU/NPU/custom ASIC 가능성 |

다만 삼성전자는 이미 전일 급등했습니다. 추격매수의 기대값은 낮아졌습니다. 더 좋은 확인은 HBM4E qualification, 외국인 순매수 지속, DS 이익 추정 상향, 그리고 AI storage·server DRAM 쪽의 추가 수주입니다.

### 3.2 LS ELECTRIC·전력 인프라: 가장 덜 가짜인 AI factory 파생축

NVIDIA가 MGX, DSX, 800VDC를 같이 말하는 이유는 명확합니다. AI factory는 전기를 먹는 공장입니다. GPU가 늘수록 전력변환, 배전, 차단, 전력효율, 냉각이 병목이 됩니다.

6월 1일 LS ELECTRIC은 가격과 수급이 모두 좋았습니다. 전일 글에서 본 것처럼 외국인 +991억원, 기관 +282억원이 붙었습니다. 이 축은 젠슨 황과 사진을 찍는 테마보다 더 단순합니다.

> AI factory는 전력이 없으면 지어지지 않는다.

전력 인프라 주식의 리스크는 이미 많이 올랐다는 점입니다. 하지만 AI factory capex의 물리적 병목이라는 점에서는 로봇 키워드주보다 실적 확인 경로가 더 뚜렷합니다.

### 3.3 Physical AI: LG전자·현대차·로봇주·두산의 기회와 함정

NVIDIA가 physical AI를 전면화하면서 한국 시장은 LG전자, 현대차, 두산로보틱스, 로보티즈, 레인보우로보틱스를 즉각적으로 재평가했습니다. NVIDIA 공식 블로그도 Isaac GR00T reference humanoid, robotics, DRIVE Hyperion, Cosmos 3 등 physical AI 축을 GTC Taipei 핵심 업데이트로 배치했습니다. ([NVIDIA Blog][2])

다만 physical AI는 가장 흥미롭지만 가장 위험한 축이기도 합니다.

| 세부축 | 기회 | 함정 |
|---|---|---|
| LG전자 | 로봇, 공장, 가전, edge device, physical AI 접점 | 전일 가격은 강했지만 외국인·기관 매도 |
| 현대차 | DRIVE Hyperion, AV, 제조·모빌리티 데이터 | 실제 NVIDIA 공동개발 범위 확인 필요 |
| 두산로보틱스·로보티즈·레인보우 | 이벤트 베타와 수급 집중 | 매출·마진보다 키워드가 앞설 위험 |
| 두산그룹 | 로봇보다 CCL, 공장 digital twin, 에너지 인프라까지 확장 가능 | 회사별 직접 수혜 경로가 다름 |

두산 쪽에서는 특히 "두산로보틱스만 보는 해석"이 좁을 수 있습니다. physical AI가 공장과 산업현장으로 내려오면 로봇 완제품뿐 아니라 CCL, 에너지, 공장 디지털 트윈, 산업 데이터 쪽이 같이 중요해집니다. 다만 이 부분은 아직 [Inferred]입니다. 구체 수주와 고객 공개 전까지는 테마 프리미엄을 과하게 주면 안 됩니다.

### 3.4 NAVER: 왜 NVIDIA가 NAVER Cloud를 필요로 할 수 있나

NAVER는 이번 이벤트의 가장 중요한 후속 질문입니다. 전일 NAVER는 +16.03% 상승했지만, 수급은 복합적이었습니다. 기관은 샀고 외국인은 크게 팔았습니다. 그래서 단기적으로는 과열과 확인 부족이 동시에 있습니다.

하지만 전략적 논거는 강해졌습니다. NVIDIA는 2025년 한국 AI 인프라 발표에서 NAVER Cloud가 enterprise와 physical AI workloads를 위해 **60,000개 이상 GPU**로 NVIDIA AI 인프라를 확장한다고 명시했습니다. NAVER Cloud는 Blackwell 계열 GPU를 포함한 인프라로 sovereign·physical AI를 준비하고, 조선·보안 같은 산업별 AI 모델을 개발할 계획이라고 설명됐습니다. ([NVIDIA Newsroom][5])

또 NAVER Cloud는 SK하이닉스와 차세대 AI 메모리 검증·최적화를 통해 AI 서비스 성능과 비용 효율을 함께 높이는 협업을 발표한 바 있습니다. ([NAVER][6])

이 조합이 중요합니다.

| NAVER 자산 | NVIDIA 관점의 의미 |
|---|---|
| NAVER Cloud | 한국·아시아 sovereign AI cloud 채널 |
| 60,000+ GPU 계획 | 단순 고객이 아니라 regional AI infrastructure operator |
| HyperCLOVA X | 한국어·로컬 데이터·공공/기업용 모델 |
| 공공·금융 클라우드 | 규제 산업의 AI deployment 경로 |
| 1784·NAVER Labs | physical AI와 로봇 테스트베드 |
| SK하이닉스 협업 | 메모리·GPU 최적화, 비용 효율 |

NAVER를 "한국판 ChatGPT"로 보면 틀립니다. 더 정확한 표현은 이것입니다.

> NAVER는 NVIDIA GPU를 사는 포털회사가 아니라, 한국과 일부 해외 시장에서 sovereign AI factory를 운영할 수 있는 지역 플랫폼 후보입니다.

하지만 여기서 바로 Buy로 가면 안 됩니다. NAVER는 6월 1일 기준으로 이미 단기 급등했고, 외국인 수급은 아직 확인되지 않았습니다. 투자자가 봐야 할 KPI는 다음입니다.

| 확인 지표 | 왜 중요한가 |
|---|---|
| GPUaaS 매출과 utilization | 60,000+ GPU가 비용인지 수익자산인지 구분 |
| sovereign AI 장기계약 | 정부·공공·금융 수요의 반복성 확인 |
| Enterprise AI gross margin | LLM/API 비용을 이기는지 확인 |
| HyperCLOVA X 외부 매출 | 내부 서비스 개선인지 B2B 제품인지 구분 |
| 해외 sovereign AI 계약 | 한국 내수 story를 넘어서는지 확인 |
| 외국인 수급 전환 | 기관 이벤트 매수를 넘어 글로벌 재평가인지 확인 |

---

## 4. 지금 사야 할 것은 키워드가 아니라 "병목 + 숫자"다

이번 장세에서 가장 조심해야 할 것은 "NVIDIA 관련"이라는 단어 하나로 모든 종목을 같은 멀티플로 보는 것입니다. AI infrastructure 안에서도 지속성과 멀티플은 완전히 다릅니다.

| 유형 | 멀티플 성격 | 지속성 | 확인할 숫자 |
|---|---|---|---|
| HBM / memory | EPS revision형 | 높지만 사이클 존재 | qualification, ASP, margin |
| 전력기기 | backlog / capacity형 | 높음 | 수주잔고, lead time, OPM |
| FC-BGA / MLCC / CCL | design-in형 | 중상 | LTA, 고객 수, ASP, 수율 |
| GPUaaS / sovereign AI | utilization형 | 검증 필요 | 가동률, 장기계약, gross margin |
| 로봇 / physical AI | event + optionality형 | 아직 낮음 | 매출, 반복 고객, 부품 attach |
| 단순 SI / 서버 유통 | 낮은 멀티플 | 낮음 | resale margin, 반복매출 |

이 표가 이번 글의 결론입니다. AI factory라는 큰 말 안에서도 **메모리, 전력, 부품, 클라우드, 로봇의 멀티플은 달라야 합니다.** NAVER가 재평가를 받으려면 "AI를 한다"가 아니라 GPUaaS와 sovereign AI가 매출·마진으로 내려와야 합니다. 로봇주는 "NVIDIA가 physical AI를 말한다"가 아니라 실제 고객과 부품 매출이 필요합니다.

---

## 5. 실전 전략

### Buy now

없습니다. 전일 장세는 너무 급했고, breadth는 좁았습니다. 추격보다 확인이 우선입니다.

### Watch / 조건부 Buy 후보

| 종목군 | 판단 | 조건 |
|---|---|---|
| 삼성전자 | Core watch | HBM4E qualification, 외국인 순매수 지속, 급등 후 눌림 |
| LS ELECTRIC·전력 인프라 | Pullback buy 후보 | 전력 capex 수주와 OPM 유지, 20일선 재확인 |
| NAVER | 조건부 Buy 후보 | 250,000~260,000원 지지 또는 270,000원 위 안착 + 외국인 매도 완화 |
| 이수페타시스·AI networking | Watch | 고속 네트워킹 수요와 고객 mix 확인 |
| 두산그룹 | Watch | 로봇보다 CCL·에너지·공장 digital twin 경로 확인 |

### Event-driven / 추격 금지

| 종목군 | 이유 |
|---|---|
| LG전자 | 가격은 강했지만 전일 외국인·기관 동반 매도. 실제 협력 발표 필요 |
| 두산로보틱스·로보티즈·레인보우 | 수급은 강하지만 이벤트 민감도 큼. 회동 이후 sell-on 위험 |
| 삼성전기·대덕전자·심텍·티엘비 | 기존 AI 부품 thesis는 남아 있지만 단기 수급은 차익실현 |

### Invalidation

| 조건 | 의미 |
|---|---|
| 젠슨 황 방한이 사진·회동으로만 종료 | physical AI·LG·로봇주 sell-on 위험 |
| NAVER 외국인 매도 지속 | 기관 이벤트 매수에 그칠 가능성 |
| 삼성전자 HBM4E qualification 지연 | 한국 AI factory core thesis 약화 |
| 전력 인프라 수주·마진 둔화 | AI factory 물리 병목 thesis 둔화 |
| ADR 회복 실패 | 시장 전체 확산 없이 소수 종목만 과열 |

---

## 6. 최종 판단

간밤 NVIDIA 메시지는 한국 증시에 우호적입니다. 하지만 그 우호성은 "NVIDIA가 한국을 좋아한다"가 아니라 **AI factory의 병목이 한국 기업의 여러 사업부와 겹친다**는 데서 나옵니다.

삼성전자는 core입니다. HBM4E와 server memory가 확인되면 한국 AI factory exposure의 중심입니다. LS ELECTRIC과 전력 인프라는 가장 현실적인 파생축입니다. NAVER는 이번 이벤트로 포털주가 아니라 sovereign AI factory operator 후보로 다시 봐야 합니다. 두산과 로봇주는 physical AI 옵션이 붙었지만, 실적 확인 전에는 이벤트 베타입니다.

그래서 결론은 이렇습니다.

> 지금 한국 시장에서 중요한 것은 젠슨 황의 동선이 아니라, NVIDIA AI factory 안에서 한국 기업이 맡는 병목의 질과 지속성입니다.

좁은 장세에서는 키워드보다 숫자가 이깁니다. 회동보다 계약, 테마보다 utilization, 가격 급등보다 외국인·기관 수급 지속을 봐야 합니다.

---

## 근거 분류

### [Fact]

- NVIDIA는 Vera Rubin이 full production ramp 단계에 들어갔고, 대만 150개 파트너, 350개 이상 공장, 30개국 공급망을 통해 ramp 중이라고 발표했습니다. ([NVIDIA Newsroom][1])
- NVIDIA 공식 블로그는 GTC Taipei의 핵심을 AI factories, agentic AI, physical AI로 정리했습니다. ([NVIDIA Blog][2])
- Reuters 계열 보도는 젠슨 황 CEO가 한국 경영진과 만날 예정이고, Samsung Electronics, LG Electronics, NAVER가 관련 기대감으로 상승했다고 보도했습니다. ([MarketScreener / Reuters][3])
- NVIDIA는 한국 AI 인프라 발표에서 NAVER Cloud가 60,000개 이상 GPU로 NVIDIA AI 인프라를 확장한다고 밝혔습니다. ([NVIDIA Newsroom][5])
- NAVER Cloud는 SK하이닉스와 AI 서비스 성능·비용 효율 강화를 위한 협업을 발표했습니다. ([NAVER][6])

### [Inference]

- NVIDIA의 GTC Taipei 메시지는 GPU 단품보다 AI factory 운영체계로 해석해야 합니다.
- 한국 시장의 다음 리레이팅은 HBM만이 아니라 전력, 네트워킹, GPUaaS, sovereign AI, physical AI로 확산될 가능성이 있습니다.
- NAVER는 포털주보다 regional sovereign AI cloud operator 후보로 보는 편이 더 정확합니다.
- 로봇주와 LG전자 이벤트 프리미엄은 공식 협력 발표가 없으면 sell-on 위험이 큽니다.

### [Speculation]

- NAVER Cloud가 Southeast Asia 또는 Middle East sovereign AI 수주로 확장될 수 있다는 가설은 아직 공식 확인 전입니다.
- 두산그룹의 CCL·에너지·공장 digital twin이 NVIDIA physical AI와 직접 연결될 수 있다는 해석은 아직 투자 가설입니다.
- LG전자·현대차·NAVER와 NVIDIA 간 구체 공동개발 또는 공급계약 여부는 아직 공개 확정 전입니다.

### [Blocked]

- 젠슨 황 방한 공식 일정과 최종 회동 기업.
- 한국 기업별 NVIDIA 관련 실제 수주액, 투자액, MOU 세부 조건.
- NAVER Cloud GPUaaS utilization, gross margin, 고객별 장기계약.
- 로봇·physical AI 관련 실제 매출 인식 시점.

[1]: https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory "NVIDIA Vera Rubin Ramps Into Full Production to Power Agentic AI Factories Worldwide | NVIDIA Newsroom"
[2]: https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/ "NVIDIA GTC Taipei at COMPUTEX: Live Updates on What’s Next in AI | NVIDIA Blog"
[3]: https://www.marketscreener.com/news/samsung-lg-shares-rally-ahead-of-nvidia-ceo-meetings-with-korean-executives-ce7f5dd8dc81fe2d "Samsung, LG shares rally ahead of Nvidia CEO meetings with Korean executives | Reuters via MarketScreener"
[4]: https://koreajoongangdaily.joins.com/news/2026-05-29/business/industry/Jensen-Huang-expected-to-visit-Korea-raising-hopes-for-investments-partnerships-amid-competition-from-Taiwan/2604218 "Jensen Huang expected to visit Korea, raising hopes for investments, partnerships amid competition from Taiwan | Korea JoongAng Daily"
[5]: https://nvidianews.nvidia.com/news/south-korea-ai-infrastructure "NVIDIA, South Korea Government and Industrial Giants Build AI Infrastructure and Ecosystem | NVIDIA Newsroom"
[6]: https://www.navercorp.com/media/pressReleasesDetail?seq=33277 "네이버클라우드, SK하이닉스와 손잡고 AI 서비스 성능·효율성 동시 강화 | NAVER Corp."
