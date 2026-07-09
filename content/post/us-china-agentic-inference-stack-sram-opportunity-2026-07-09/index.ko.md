---
title: "미국과 중국의 에이전트 추론 인프라 분화와 SRAM의 기회"
date: 2026-07-09T17:20:00+09:00
description: "미국과 중국의 AI 추론 인프라가 왜 다른 방향으로 갈라지는지, 전력·HBM·SRAM/LPU 병목이 한국 상장사에 어떤 기회를 만드는지 점검합니다."
categories: ["Theme-Analysis", "Korea Semiconductors", "AI Infrastructure"]
tags:
  - "AI 추론"
  - "에이전트 AI"
  - "SRAM"
  - "LPU"
  - "HBM"
  - "Vera Rubin"
  - "LPX"
  - "삼성전자"
  - "SK하이닉스"
  - "HD현대일렉트릭"
  - "한미반도체"
  - "전력장비"
  - "중국 AI"
  - "미국 AI"
slug: us-china-agentic-inference-stack-sram-opportunity-2026-07-09
series: ["hbm", "exclusive-analysis"]
valley_cashtags:
  - 005930.KS
  - 000660.KS
  - 267260.KS
  - 010120.KS
  - 298040.KS
  - 042700.KS
  - NVDA
draft: false
---

> 연결해서 읽을 글:
> [NVIDIA Vera Rubin 추론 스택](/ko/post/nvidia-vera-rubin-lpx-cmx-inference-stack-samsung-hbm-2026-05-28/) /
> [AI 토큰 가치와 메모리 부가가치](/ko/post/ai-token-value-memory-value-added-2026-07-09/) /
> [AI 데이터센터 전력 병목 지도](/ko/post/ai-datacenter-power-bottleneck-korea-value-chain-screen-2026-07-04/) /
> [AI HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/) /
> [단독 분석 허브](/ko/page/exclusive-analysis-hub/)

## TL;DR

미국과 중국의 AI 추론 인프라는 같은 목표를 향하지만 다른 병목을 풀고 있다. 미국은 전력, 랙 밀도, HBM, 고급 패키징이 병목이다. 그래서 NVIDIA Vera Rubin, HBM4, SRAM 기반 LPU, 전력장비, 고밀도 패키징으로 간다. 중국은 첨단 로직과 HBM 접근이 막혀 있다. 그래서 Huawei Ascend, 병렬 확장, 광메시, 자체 메모리 계층으로 우회한다.

한국 상장사 기회는 중국 광모듈 쪽보다 미국형 AI 인프라 병목에 더 크다. 가장 직접적인 축은 <strong>HBM4/HBM4E, 전력장비, HBM 패키징 장비</strong>다. 여기에 하나 더 붙는 옵션이 <strong>삼성전자의 SRAM/LPU 파운드리와 AI 스토리지</strong>다.

투자 결론은 단순하지 않다. SK하이닉스는 HBM4 리더지만 이미 crowded winner다. HD현대일렉트릭은 미국 데이터센터 전력 병목의 순도 높은 수혜주지만 주문 모멘텀이 많이 알려졌다. 한미반도체는 HBM 장비 병목이지만 고객 집중과 밸류에이션을 봐야 한다. 가장 비대칭적인 후보는 삼성전자다. 다만 조건이 있다. HBM4E, 파운드리 LPU/AI ASIC, AI 스토리지 논리가 실제 숫자로 이어져야 한다.

## 1. 원문 주장의 핵심: 맞지만 landing은 조정해야 한다

이번 분석의 출발점은 YS-VC의 글 <a href="https://www.ys-vc.com/blog/us-china-ai-inference-stack-divergence">「전력이냐 칩이냐: 미국과 중국의 AI 추론 스택이 갈라선 이유」</a>다. 핵심 주장은 대체로 맞다. 미국과 중국은 모두 AI 추론 수요를 처리해야 하지만, 제약 조건이 다르기 때문에 하드웨어 스택이 다르게 진화한다.

다만 한국 상장사로 옮겨올 때는 조심해야 한다. 중국이 광메시와 병렬 확장을 쓴다고 해서 한국 상장 광부품주가 곧바로 수혜를 받는다는 뜻은 아니다. 중국 AI 인프라 공급망은 폐쇄적이고, 핵심 부품 국산화 압력이 강하다. 한국의 직접 기회는 중국식 광메시보다 미국식 AI factory의 병목, 즉 전력, HBM, 패키징, SRAM/LPU, 스토리지 쪽에 더 가깝다.

| 주장 | 판정 | 투자자용 해석 |
|---|---|---|
| 미국과 중국의 AI 추론 스택은 갈라지고 있다 | 대체로 사실 | 미국은 전력과 랙 효율, 중국은 첨단 로직·HBM 제약을 먼저 푼다 |
| 미국은 GPU/HBM/SRAM을 묶은 고밀도 rack-scale 추론으로 간다 | 사실 | Vera Rubin, LPX, HBM4, SRAM/LPU가 한 스택 안으로 들어간다 |
| 중국은 Ascend, 광메시, 자체 메모리 계층으로 우회한다 | 일부 사실 | 방향은 맞지만 CloudMatrix 세부 성능과 장애율은 독립 검증이 부족하다 |
| 미국 수출통제는 중국의 NVIDIA 데이터센터 compute 접근을 제한한다 | 사실 | 중국은 HBM과 최첨단 GPU를 안정적으로 받기 어렵다 |
| HBM은 계속 핵심 통제점이다 | 사실 | BIS도 HBM을 AI training과 inference at scale에 중요한 품목으로 본다 |
| 한국 기회는 중국 광모듈이다 | 과도한 해석 | 한국에는 미국형 HBM·전력·패키징·삼성 파운드리 옵션이 더 중요하다 |

## 2. 왜 미국과 중국은 다른 길로 가나

AI 추론의 공통 문제는 토큰 폭증이다. coding agent, research agent, voice agent, enterprise workflow agent는 한 번 답하고 끝나는 챗봇과 다르다. 긴 문맥을 읽고, 도구를 호출하고, 결과를 다시 읽고, 다시 답을 만든다. 이 과정에서 prefill, decode, KV cache, storage, network, power가 모두 병목이 된다.

하지만 미국과 중국이 막힌 곳은 다르다.

| 구분 | 미국 | 중국 |
|---|---|---|
| 가장 큰 제약 | 전력, 랙 밀도, 변압기, HBM4, 고급 패키징 | 첨단 로직, HBM 접근, 수출통제, 소프트웨어 최적화 |
| 대표 방향 | Vera Rubin, LPX/LPU, HBM4, 고전력 AI rack | Huawei Ascend, 광메시, 병렬 확장, 자체 메모리 계층 |
| 장점 | 최첨단 GPU·HBM·패키징 접근성 | 전력 증설 속도, 국가 주도 인프라, 내수 클라우드 |
| 약점 | time-to-power, 송전망, 변압기 lead time | EUV 없는 선단 로직, HBM 수급, 생태계 폐쇄성 |
| 한국 상장사 landing | HBM, 전력장비, HBM 장비, 파운드리 옵션 | 제한적. 직접 공급망 확인 필요 |

IEA는 데이터센터 전력 수요가 2030년 945TWh 수준까지 늘 수 있다고 본다. ([IEA][1]) 전력은 이제 부수 비용이 아니라 AI 인프라의 상한을 정하는 변수다.

미국은 이 병목이 특히 크다. BloombergNEF가 Energy Connects를 통해 인용한 전망에 따르면 중국은 향후 5년간 3.4TW가 넘는 발전 설비를 더할 것으로 예상된다. 이는 미국 추가 규모의 거의 6배다. 같은 보도는 2024~2030년 미국 전력 수요 증가에서 데이터센터가 38%를 차지하지만, 중국에서는 6%라고 정리했다. ([Energy Connects][2]) 미국은 AI 수요가 전력망을 더 직접적으로 압박하고, 중국은 전력 증설 여력이 상대적으로 크다.

그래서 미국은 "같은 전력으로 더 많은 토큰을 처리하는 구조"가 중요해진다. 중국은 "최첨단 칩이 부족해도 많은 칩과 네트워크로 밀어붙이는 구조"가 중요해진다.

## 3. 미국형 추론 스택: HBM만이 아니라 SRAM/LPU다

미국형 스택을 이해하려면 NVIDIA의 Vera Rubin과 LPX를 봐야 한다. NVIDIA는 LPX를 Vera Rubin용 추론 가속기라고 설명한다. 구조는 단순 GPU 확장이 아니다. Rubin GPU는 HBM을 쓰고, Groq 3 LPX는 SRAM 기반 LPU를 붙인다. ([NVIDIA LPX][3])

NVIDIA 설명에서 중요한 숫자는 다음과 같다.

| 항목 | NVIDIA LPX 공식 설명 |
|---|---:|
| agentic system 토큰 증가 | 최대 15배 더 많은 토큰 |
| Vera Rubin NVL72 + LPX 효율 | MW당 throughput 최대 35배 |
| LPU accelerator 1개 | 500MB SRAM |
| LPU accelerator SRAM bandwidth | 150TB/s |
| LPU accelerator scale-up bandwidth | 2.5TB/s |
| LPX rack | 256개 LPU chip |
| LPX rack SRAM | 128GB |
| LPX rack DDR5 | 12TB |
| LPX rack SRAM bandwidth | 40PB/s |

이 숫자가 말하는 것은 "HBM이 필요 없어졌다"가 아니다. 정반대다. HBM은 여전히 Rubin GPU의 핵심 메모리다. 다만 decode와 지연시간이 중요한 작업에서는 작은 SRAM을 아주 빠르게 쓰는 LPU가 HBM GPU를 보완한다.

쉽게 나누면 이렇다.

| 단계 | 쉬운 설명 | 필요한 병목 |
|---|---|---|
| Prefill | 질문과 문서를 처음 읽는다 | GPU compute, HBM bandwidth |
| Decode | 답을 한 토큰씩 만든다 | 낮은 지연시간, SRAM, LPU |
| KV cache | 앞에서 읽은 내용을 기억한다 | HBM, DDR, SSD, cache 계층 |
| Serving | 수많은 사용자 요청을 안정적으로 처리한다 | rack network, scheduler, power |

그래서 SRAM의 기회는 "대용량 메모리 교체"가 아니라 "추론 속도와 전력 효율을 높이는 가까운 메모리"에 있다. 이것이 삼성전자에 옵션을 만든다. 삼성전자는 HBM4E뿐 아니라 파운드리, advanced packaging, SOCAMM2, PCIe 6.0 SSD, BlueField-4 STX reference architecture의 PM1753 같은 스토리지까지 한 번에 설명할 수 있는 회사다. 삼성전자는 GTC 2026에서 HBM4 양산, HBM4E, SOCAMM2 양산, PM1763 PCIe 6.0 SSD를 공개했다. ([Samsung Newsroom][4])

## 4. 중국형 스택: 광메시와 병렬 확장, 그러나 한국 landing은 약하다

중국의 방향은 다르다. 첨단 GPU와 HBM을 자유롭게 받기 어렵기 때문에, Huawei Ascend 계열, 자체 클라우드, 광메시, 많은 칩을 묶는 병렬 확장 쪽으로 간다. 이 방향은 논리적으로 맞다. 선단 로직과 HBM이 제한되면, 더 많은 칩을 연결하고, 데이터 이동을 줄이고, 네트워크로 병목을 우회해야 한다.

그러나 여기서 바로 한국 광부품주 수혜로 가면 논리 비약이다.

첫째, 중국 AI 인프라 공급망은 전략적으로 폐쇄적이다. 둘째, 미국 수출통제가 HBM과 첨단 AI 반도체를 겨냥하고 있어 중국은 자체 조달과 국산화를 더 강하게 밀 수밖에 없다. 셋째, CloudMatrix 같은 시스템의 세부 성능, 장애율, 총소유비용은 독립 검증이 충분하지 않다.

따라서 중국 스택은 투자자에게 중요한 "경쟁 구조"이지만, 한국 상장사 landing은 아직 약하다. 중국 광메시가 커진다는 주장은 한국 기업에 자동으로 매출이 생긴다는 뜻이 아니다. 한국 포트폴리오 관점에서는 중국식 우회보다 미국식 병목에 파는 기업을 먼저 봐야 한다.

## 5. 한국 상장사 landing map

| 축 | 핵심 병목 | 한국 상장사 후보 | 판단 |
|---|---|---|---|
| HBM4/HBM4E | NVIDIA Vera Rubin, AI server memory | SK하이닉스, 삼성전자 | 구조적 수혜. SK하이닉스는 리더, 삼성전자는 catch-up 옵션 |
| SRAM/LPU 파운드리 | 저지연 decode, inference accelerator | 삼성전자 | 아직 숫자는 작거나 미확인. 하지만 가장 덜 반영된 옵션 |
| AI 스토리지/KV cache | agent memory, eSSD, PCIe 6.0 | 삼성전자, 파두 등 | HBM 아래 메모리 계층으로 확장 가능 |
| HBM 패키징 장비 | TC bonder, advanced packaging | 한미반도체 | 병목은 맞지만 고객 집중과 가격 반영 주의 |
| 전력장비 | transformer, switchgear, grid connection | HD현대일렉트릭, LS ELECTRIC, 효성중공업 | 미국 AI 데이터센터 전력 병목의 직접 수혜 |
| 중국 광메시 | optical module, China AI cluster | 국내 직접 후보 제한적 | 확인된 공급망 없으면 Avoid |

핵심은 "AI 수혜"라는 말이 너무 넓다는 점이다. 미국형 추론 인프라에서는 전력, HBM, SRAM/LPU, advanced packaging, storage가 함께 움직인다. 이 중 한국이 가장 잘하는 것은 HBM과 전력장비다. 아직 시장이 충분히 가격에 넣지 않은 것은 삼성전자의 SRAM/LPU 파운드리 옵션이다.

## 6. 아이디어 1: 전력장비가 미국형 AI 병목의 앞단이다

미국은 전력이 병목이다. 데이터센터 수요가 빠르게 늘고, 송전망 접속과 변압기 조달은 느리다. 그래서 AI capex가 유지되면 가장 먼저 확인되는 숫자는 GPU 주문만이 아니라 변압기, 배전반, 초고압 설비, 현장 전력 인프라 주문이다.

HD현대일렉트릭은 이 축에서 가장 선명하다. 회사는 2026년 수주 목표를 42.22억달러에서 51.85억달러로 23% 올렸다. 보도에 따르면 북미 전력 인프라, 765kV 변압기, 북미 데이터센터, 데이터센터용 onshore generator 수요가 배경이다. ([Seoul Economic Daily][5])

| 항목 | 투자 해석 |
|---|---|
| P | 전력장비 가격, 고압 변압기 수익성, 북미 premium |
| Q | 데이터센터, 송전망, 765kV 프로젝트, 교체 수요 |
| C | 원자재, 생산능력, 납기, 품질 비용 |
| 확인 지표 | book-to-bill, 북미 신규 수주, 마진, 2027년 capacity 확장 |
| 실패 조건 | AI capex 지연, 송전망 허가 지연, 현지 조달 압박, margin compression |

다만 지금은 좋은 회사와 좋은 진입 가격을 분리해야 한다. HD현대일렉트릭의 방향은 좋지만, 시장도 이미 전력장비를 AI 병목으로 인식하고 있다. 신규 진입은 "AI capex 우려로 눌렸지만 수주와 margin은 유지되는 구간"이 더 낫다.

## 7. 아이디어 2: HBM4/HBM4E는 중국보다 미국형 스택에 더 붙는다

BIS는 2024년 12월 발표에서 HBM을 AI training과 inference at scale에 중요한 품목으로 보고 수출통제를 강화했다. ([BIS][6]) 이 말은 간단하다. 중국이 HBM을 자유롭게 받기 어렵다면, 미국과 동맹권 AI 인프라는 한국 HBM에 더 강하게 의존한다.

SK하이닉스는 이 축의 리더다. Yonhap은 SK하이닉스가 NVIDIA 차세대 AI 플랫폼용 HBM 주문의 3분의 2 이상을 확보한 것으로 보도했다. ([Yonhap][7]) 사업 포지션만 보면 가장 강하다.

그러나 투자 판단은 사업 포지션만으로 끝나지 않는다. SK하이닉스는 이미 HBM winner로 인식되어 있다. 최근 미국 상장 관련 수요와 ADR 이벤트까지 겹치며 수급 crowding이 높아졌다. 따라서 지금의 질문은 "좋은 회사인가"가 아니라 "좋은 회사라는 점이 얼마나 가격에 반영됐는가"다.

삼성전자는 반대다. 시장은 삼성전자를 HBM laggard로 봐 왔다. 하지만 삼성전자가 HBM4E, SOCAMM2, PCIe 6.0 SSD, 파운드리, packaging을 동시에 묶어 AI memory hierarchy supplier로 재분류된다면 할인 축소 여지가 생긴다.

| 종목 | 강점 | 약점 | 현재 판단 |
|---|---|---|---|
| SK하이닉스 | HBM4 리더십, NVIDIA allocation, 높은 HBM 순도 | crowding, 높은 기대치, 2027년 공급 과잉 우려 | Wait |
| 삼성전자 | HBM4E catch-up, 파운드리·스토리지·패키징 옵션, 할인 축소 가능성 | HBM 인증 지연 리스크, 파운드리 적자, 고객 신뢰 회복 필요 | Conditional Buy 후보 |

## 8. 아이디어 3: 삼성전자의 SRAM/LPU 파운드리 옵션

이번 글에서 가장 중요한 비합의 포인트는 삼성전자다. 삼성전자를 HBM catch-up으로만 보면 절반만 본다. Vera Rubin 이후 추론 스택에서는 HBM 옆에 SRAM/LPU, KV cache storage, packaging, rack-level memory hierarchy가 붙는다. 이때 삼성전자는 메모리 회사이면서 파운드리 회사이기도 하다.

NVIDIA LPX 구조에서 LPU는 SRAM을 많이 쓰는 저지연 추론 칩이다. SRAM은 DRAM처럼 외부에서 대용량으로 붙는 부품이 아니라 로직 가까이에 있는 on-chip memory에 가깝다. 따라서 기회는 메모리 판매보다 파운드리와 logic 설계 생태계에 걸린다.

삼성전자에 대한 thesis는 다음 세 조건 중 둘 이상이 확인될 때 강해진다.

| 조건 | 확인 방식 |
|---|---|
| HBM4/HBM4E 고객 인증과 양산 출하 | 실적 발표, 고객 언급, HBM 매출 믹스 |
| 파운드리 LPU/AI ASIC 매출 또는 가동률 개선 | 파운드리 적자 축소, HPC 고객, AI accelerator 생산 |
| AI 스토리지와 메모리 계층 매출 확대 | SOCAMM2, PCIe 6.0 SSD, eSSD, KV cache 관련 수요 |

무효화 조건도 분명하다.

| 무효화 조건 | 의미 |
|---|---|
| HBM4 qualification이 2개 분기 이상 지연 | HBM discount 축소 thesis 약화 |
| 파운드리 적자가 줄지 않음 | LPU/AI ASIC 옵션이 숫자로 연결되지 않음 |
| LPX/LPU 관련 매출이 삼성전자에 실질적으로 귀속되지 않음 | SRAM/LPU 옵션을 밸류에이션에 넣기 어려움 |

그래서 삼성전자는 "지금 당장 모든 것이 확인된 종목"이 아니다. 오히려 확인되지 않았기 때문에 비대칭이 있다. 시장이 삼성전자를 여전히 HBM laggard로만 보면, HBM4E와 SRAM/LPU 파운드리 옵션이 숫자로 보이는 순간 할인은 줄 수 있다.

## 9. 아이디어 4: 한미반도체와 HBM 패키징 장비

HBM4로 갈수록 패키징 장비 병목은 더 커진다. 한미반도체는 TC bonder에서 글로벌 선두권으로 평가받아 왔고, The Elec은 한미반도체가 SK하이닉스로부터 HBM4용 TC bonder 첫 주문을 받았다고 보도했다. ([The Elec][8])

논리는 좋다. HBM4 수요가 늘고, stacking 난도가 올라가고, 고객들이 capacity를 늘리면 TC bonder 수요도 늘어난다. 하지만 장비주는 메모리 생산자와 다르게 수주 공백 리스크가 크다. 한 분기 수주가 비면 주가가 먼저 반응한다. 고객 다변화도 중요하다.

| 항목 | 판단 |
|---|---|
| 구조 논리 | HBM4·HBM4E 램프업은 TC bonder 수요를 키운다 |
| 강한 촉매 | SK하이닉스 후속 주문, 삼성전자·마이크론향 공식 수주 |
| 리스크 | 고객 집중, 경쟁 장비사, 주문 공백, 이미 높은 기대 |
| 현재 판단 | Watchlist. 장기 병목은 맞지만 추격보다 수주 확인 |

## 10. 실전 판단: 지금 살 것과 기다릴 것을 나눈다

| 우선순위 | 종목/축 | 판단 | 이유 |
|---:|---|---|---|
| 1 | 삼성전자 | Conditional Buy 후보 | HBM4E, SRAM/LPU 파운드리, AI 스토리지 옵션이 아직 온전히 반영되지 않았을 가능성 |
| 2 | HD현대일렉트릭 | Wait | 미국 데이터센터 전력 병목 직접 수혜. 다만 주문 모멘텀이 이미 알려짐 |
| 3 | SK하이닉스 | Wait | HBM4 리더십은 가장 선명하지만 crowded winner 성격이 강함 |
| 4 | 한미반도체 | Watchlist | HBM 장비 병목은 맞지만 후속 수주와 고객 다변화 확인 필요 |
| 5 | 중국 광메시 직접 수혜주 | Avoid | 한국 상장사 직접 공급망 근거가 약함 |

삼성전자 진입 조건은 다음 3개 중 2개 이상이다.

1. HBM4/HBM4E 고객 인증과 양산 출하가 실적 또는 가이던스에 반영된다.
2. 파운드리 LPU/AI ASIC 매출, 또는 적자 축소와 가동률 개선이 확인된다.
3. HBM4와 파운드리 thesis가 유지되는 상태에서 밸류에이션이 다시 눌린다.

HD현대일렉트릭은 북미 신규 수주와 book-to-bill이 계속 높고, 주문 성장이 매출로 넘어가면서 margin이 꺾이지 않는지 봐야 한다. SK하이닉스는 HBM4 점유율과 margin이 유지되는지, ADR과 capex 이벤트가 수급 부담으로 바뀌지 않는지 확인해야 한다. 한미반도체는 SK하이닉스 후속 주문뿐 아니라 삼성전자·마이크론향 공식 수주가 중요하다.

## 11. 아직 막혀 있는 데이터

아래 항목은 투자 판단을 더 강하게 만들려면 추가 확인이 필요하다.

| 미확인 항목 | 왜 중요한가 |
|---|---|
| 한국 상장사의 Huawei CloudMatrix 또는 중국 광메시 공급망 | 중국식 스택을 한국 주식으로 살 수 있는지 결정 |
| 삼성전자 Groq 3 LPX/SRAM LPU 관련 실제 매출과 margin | SRAM/LPU 파운드리 옵션의 실체 확인 |
| SK하이닉스·삼성전자 HBM4 고객별 allocation, ASP, yield | HBM4 사이클의 이익 귀속 판단 |
| 전력장비 3사 최신 NTM 밸류에이션과 book-to-bill | 좋은 회사와 좋은 가격을 구분 |
| CloudMatrix 독립 benchmark, 장애율, 총소유비용 | 중국식 우회 구조의 지속 가능성 판단 |

## 최종 결론

미국과 중국의 AI 추론 인프라 분화는 한국 투자자에게 두 가지 메시지를 준다.

첫째, 중국 광메시를 한국 광부품주로 곧바로 연결하면 위험하다. 중국은 자체 공급망을 더 강하게 밀 가능성이 크고, 공개적으로 확인된 한국 상장사 landing은 제한적이다.

둘째, 한국의 더 큰 기회는 미국형 AI factory 병목에 있다. 미국은 전력과 랙 밀도, HBM4, SRAM/LPU, advanced packaging, storage를 동시에 풀어야 한다. 이 병목은 SK하이닉스, 삼성전자, HD현대일렉트릭, LS ELECTRIC, 효성중공업, 한미반도체로 이어진다.

가장 좋은 사업 포지션은 SK하이닉스일 수 있다. 가장 순도 높은 전력 병목은 HD현대일렉트릭일 수 있다. 그러나 가장 비대칭적인 재평가 후보는 삼성전자다. 시장이 삼성전자를 HBM laggard로만 보지만, HBM4E와 SRAM/LPU 파운드리, AI 스토리지까지 묶이면 이야기가 달라진다.

따라서 이번 주제의 한 줄 결론은 이렇다.

<strong>중국의 광메시보다 미국의 전력·HBM·SRAM/LPU 병목을 보자. 그리고 그 안에서 아직 온전히 가격에 반영되지 않은 옵션은 삼성전자다.</strong>

## 참고 출처

- [YS-VC, 전력이냐 칩이냐: 미국과 중국의 AI 추론 스택이 갈라선 이유](https://www.ys-vc.com/blog/us-china-ai-inference-stack-divergence)
- [IEA, Energy demand from AI](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
- [Energy Connects, China ramps up energy boom flagged by Musk as key to AI race](https://www.energyconnects.com/news/renewables/2026/february/china-ramps-up-energy-boom-flagged-by-musk-as-key-to-ai-race/)
- [NVIDIA, NVIDIA LPX](https://www.nvidia.com/en-us/data-center/lpx/)
- [Samsung Newsroom, Samsung unveils HBM4E and AI solutions at NVIDIA GTC 2026](https://news.samsung.com/global/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026)
- [BIS, Commerce strengthens export controls including HBM](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military)
- [Yonhap, SK hynix reportedly wins over two-thirds of Nvidia HBM orders](https://en.yna.co.kr/view/AEN20260128002800320)
- [The Elec, Hanmi Semiconductor receives first HBM4 TC bonder order](https://www.thelec.net/news/articleView.html?idxno=11132)
- [Seoul Economic Daily, HD Hyundai Electric raises 2026 order target](https://en.sedaily.com/finance/2026/07/06/hd-hyundai-electric-raises-2026-order-target-23-percent-on)
