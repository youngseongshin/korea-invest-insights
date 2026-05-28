---
title: "NVIDIA GTC 2026 이후 추론 스택: CPX보다 LPX·CMX가 전면에 선 이유"
date: 2026-05-28T15:30:00+09:00
description: "GTC 2026 이후 NVIDIA의 추론 전략은 GPU 단독 확장이 아니라 Vera Rubin GPU/CPU, Groq 3 LPX/LPU, BlueField-4 STX·CMX KV-cache storage, Spectrum-X/SPX networking을 묶은 heterogeneous AI factory로 이동했다. LPX는 HBM을 대체하지 않고 Rubin GPU/HBM의 저지연 decode 약점을 보완한다. 삼성전자는 HBM4·SOCAMM2·Groq LPU foundry·eSSD/KV-cache까지 걸리는 inference memory hierarchy supplier로 재분류될 수 있다."
categories: ["Theme-Analysis"]
tags:
  - "NVIDIA"
  - "엔비디아"
  - "Vera Rubin"
  - "Groq"
  - "LPX"
  - "LPU"
  - "CPX"
  - "CMX"
  - "BlueField"
  - "삼성전자"
  - "005930"
  - "SK하이닉스"
  - "000660"
  - "삼성전기"
  - "009150"
  - "HBM"
  - "AI 추론"
  - "AI 인프라"
slug: nvidia-vera-rubin-lpx-cmx-inference-stack-samsung-hbm-2026-05-28
valley_cashtags:
  - NVIDIA
  - 삼성전자
  - SK하이닉스
  - 삼성전기
draft: false
---

> 📚 NVIDIA·Vera Rubin 후속 시리즈
> [엔비디아 Q1 FY27 이후 한국 AI 인프라](/ko/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [Vera Rubin VR200 부품 원가표 검산](/ko/post/vera-rubin-vr200-bom-memory-pcb-mlcc-korea-alpha-2026-05-21/) / [AI-RAN과 한국 공급망](/ko/post/ai-ran-nvidia-earnings-skt-vs-supply-chain-2026-05-17/) / [마벨 Q1 FY2027과 한국 반도체](/ko/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/)

> 📚 삼성전자·한국 반도체 연결 글
> [삼성전자 PER 15배 리레이팅](/ko/post/samsung-electronics-tsmc-rerating-thesis-2026-05-16/) / [삼성 파운드리 고객사 목록](/ko/post/samsung-foundry-customer-list-tesla-tenstorrent-2026-05-03/) / [AI HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/) / [반도체 밸류체인 허브](/ko/page/korea-semiconductor-equipment-ip-hub/)

![Post-GTC 2026 Inference Stack: Why LPX and CMX moved ahead of CPX](post-gtc-cpx-lpx.png)

## 초심자용 TL;DR

CPX는 <strong>"긴 질문을 처음 읽는 가속기"</strong>이고, LPX는 <strong>"답변을 한 토큰씩 빠르게 뽑는 가속기"</strong>다.

GTC 2026 이후 NVIDIA의 메시지는 한 번 읽는 prefill보다, 계속 반복되는 decode와 KV cache 관리가 더 큰 병목이라는 쪽으로 이동했다. 그래서 전략 중심이 CPX 단일 칩보다 <strong>Rubin GPU + LPX + CMX + Dynamo</strong>로 짜인 추론 시스템으로 바뀐 것이다.

<strong>결론:</strong> CPX보다 LPX·CMX가 전면에 선 이유는 AI 추론의 돈 되는 병목이 "긴 문맥을 처음 읽는 일"에서 <strong>"매 토큰을 빠르게 생성하고, 그 기억을 싸고 빠르게 재사용하는 일"</strong>로 이동했기 때문이다.

한국 반도체 관점에서는 "HBM 수요 약화"가 아니라, <strong>HBM + 고속 네트워크 + 스토리지 계층 + 기판/패키징 + 전력/냉각</strong>까지 보는 추론 인프라 밸류체인으로 해석해야 한다.

## 0. 가장 쉬운 비유: AI 추론은 "책 읽고 말하기"다

AI에게 질문을 던지면 내부적으로 두 단계가 있다.

| 단계 | 아주 쉬운 설명 | 기술 용어 | 병목 |
|---|---|---|---|
| 1단계 | 질문과 자료를 먼저 읽는다 | Prefill / Context phase | 긴 문서를 빨리 읽는 능력 |
| 2단계 | 답변을 한 글자씩 말한다 | Decode / Generation phase | 한 토큰씩 빠르고 안정적으로 생성하는 능력 |
| 기억장치 | 앞에서 읽은 내용을 메모해둔다 | KV cache | 메모를 어디에 저장하고 얼마나 빨리 다시 꺼내느냐 |

CPX는 주로 <strong>1단계: 긴 문맥을 처음 읽는 일</strong>에 맞춘 제품이었다. NVIDIA가 2025년 공개한 Rubin CPX는 1M+ token context workload, 즉 매우 긴 문맥 처리에 맞춘 GPU였고, 30 PFLOPS NVFP4 compute, 128GB GDDR7, 3배 attention acceleration을 내세웠다. ([NVIDIA Developer][2])

반면 LPX와 CMX는 각각 <strong>2단계: 답변 생성</strong>과 <strong>기억장치: KV cache 관리</strong>를 겨냥한다. NVIDIA의 LPX 설명에 따르면 Rubin GPU는 prefill과 decode attention을 맡고, LPX는 decode 안의 FFN/MoE 같은 지연 민감 연산을 가속한다. ([NVIDIA Developer][3]) CMX는 GPU HBM과 일반 스토리지 사이에 KV cache 전용 계층을 만드는 구조다. ([NVIDIA Developer][7])

## 0.1 용어 정리

### GTC 2026

GTC는 NVIDIA가 자사 AI 인프라 전략을 발표하는 가장 중요한 개발자·고객 행사다. 2026년 GTC의 핵심 메시지는 "AI 학습용 GPU 회사"에서 <strong>"AI factory 전체 운영체제와 하드웨어 스택을 파는 회사"</strong>로 확장한다는 것이다.

GTC 2026에서 NVIDIA는 Dynamo 1.0을 공개하며 이를 AI factory의 distributed operating system으로 설명했고, GPU·메모리·스토리지를 클러스터 단위로 오케스트레이션하는 소프트웨어로 포지셔닝했다. ([NVIDIA Newsroom][8])

### 추론, Inference

추론은 AI가 실제로 답변을 생성하는 과정이다. 예전에는 AI 인프라의 핵심이 "모델을 학습시키는 GPU"였다. 그런데 ChatGPT, Claude, coding agent, 검색 agent처럼 실제 사용량이 폭증하면서 이제는 <strong>학습보다 추론 비용과 속도</strong>가 더 중요해졌다.

투자자 관점에서는 이 변화가 중요하다. 학습은 대형 AI lab 중심의 CAPEX이고, 추론은 실제 서비스 사용량에 따라 매일 발생하는 OPEX다. 즉 토큰당 원가, 응답 속도, 전력 효율이 서비스 마진으로 연결된다.

### Token

토큰은 AI가 읽고 쓰는 최소 단위의 조각이다. 한국어로는 한 글자, 한 단어, 단어 일부가 될 수 있다. 사용자가 긴 보고서, 코드베이스, 영상 transcript를 넣으면 토큰 수가 급증한다.

AI 서비스의 매출과 비용은 결국 "얼마나 많은 토큰을 얼마나 싸고 빠르게 처리하느냐"로 수렴한다.

### Prefill / Context phase

Prefill은 AI가 질문과 첨부자료를 처음 읽는 단계다. 예를 들어 200페이지 보고서를 넣고 "요약해줘"라고 하면, 모델은 먼저 전체 보고서를 읽어 내부 상태를 만든다. 이 과정이 prefill이다.

CPX가 원래 겨냥한 영역이 여기에 가깝다. NVIDIA의 CPX 설명도 context phase는 compute-bound이고, generation phase는 memory bandwidth-bound라고 나눠 설명한다. ([NVIDIA Developer][2])

쉽게 말하면:

> CPX = 긴 자료를 처음 읽는 속도를 높이는 전용 독서 보조 장치

### Decode / Generation phase

Decode는 AI가 답변을 한 토큰씩 생성하는 단계다. AI는 답변 전체를 한 번에 뱉지 않는다. "안녕하세요"라는 답도 내부적으로는 작은 조각을 순차적으로 만든다.

여기서 중요한 점은 <strong>decode는 반복 작업</strong>이라는 것이다. 긴 답변, 코딩 agent, reasoning model, tool-use agent는 수천~수만 토큰을 계속 생성한다. 사용자는 이 단계의 속도를 직접 체감한다.

NVIDIA는 LPX 설명에서 interactive inference에서는 time-to-first-token, tokens/sec per user, tail latency가 핵심 지표라고 설명한다. ([NVIDIA Developer][3])

쉽게 말하면:

> LPX = AI가 말을 한 글자씩 빠르고 끊김 없이 하도록 돕는 가속기

### KV cache

KV cache는 AI가 이미 읽은 내용을 다시 계산하지 않기 위해 저장해두는 중간 기억이다.

예를 들어 AI와 30분 대화했다고 가정하자. 매번 답변할 때마다 앞의 30분 대화를 처음부터 다시 읽고 계산하면 비용이 폭증한다. 그래서 모델은 앞에서 읽은 내용을 KV cache라는 형태로 저장해둔다.

NVIDIA는 CMX 설명에서 KV cache를 inference context라고 부르며, agentic system에서는 모델의 장기 기억처럼 재사용된다고 설명한다. ([NVIDIA Developer][7])

쉽게 말하면:

> KV cache = AI가 "아까 무슨 얘기했는지" 기억해두는 작업 메모

### HBM

HBM은 GPU 바로 옆에 붙는 초고속 메모리다. AI 학습과 추론에서 가장 중요한 메모리다. 비싸고, 공급도 제한적이고, 패키징 난도도 높다.

중요한 오해가 있다. <strong>LPX나 CMX가 HBM을 대체한다고 보면 안 된다.</strong> LPX는 SRAM 기반의 저지연 decode 보조 장치이고, CMX는 KV cache용 스토리지 계층이다. HBM은 여전히 Rubin GPU의 핵심 메모리다.

정확한 표현은 이렇다.

> LPX·CMX는 HBM을 "대체"하는 것이 아니라, HBM에 몰리던 일부 병목을 나눠 받아 HBM을 더 효율적으로 쓰게 만드는 구조다.

### SRAM

SRAM은 아주 빠르지만 용량이 작은 메모리다. GPU의 HBM보다 훨씬 가까운 위치에서 빠르게 접근할 수 있지만, 대용량으로 만들기 어렵다.

LPX의 핵심은 이 SRAM이다. NVIDIA 공식 LPX 자료 기준 Groq 3 LPX rack은 256개 칩, 총 128GB SRAM, 40PB/s on-chip SRAM bandwidth, 640TB/s scale-up bandwidth를 제시한다. ([NVIDIA Developer][3])

간단 검산은 다음과 같다.

| 항목 | 산식 | 값 |
|---|---:|---:|
| LPX 칩 수 | 32 trays × 8 chips | 256 chips |
| SRAM 용량 | 32 trays × 4GB | 128GB |

즉 LPX는 대용량 메모리 장치가 아니라, <strong>작은 SRAM을 매우 빠르게 써서 decode 지연을 줄이는 장치</strong>에 가깝다.

### CPX

CPX는 Context Processing X, 즉 긴 문맥 처리용 GPU로 이해하면 된다. 원래 CPX의 존재 이유는 명확했다. 긴 코드베이스, 긴 영상, 긴 보고서, 긴 리서치 자료를 AI가 처음 읽을 때 prefill 비용이 커진다. CPX는 이 "처음 읽기"를 가속하려는 제품이다.

다만 GTC 2026 이후 공개 메시지에서는 CPX보다 LPX와 CMX가 더 전면에 나왔다. Tom's Hardware는 GTC 2026 keynote와 slide에서 Rubin CPX가 빠지고 Groq 3 LPU/LPX rack이 등장한 점을 들어, NVIDIA가 CPX보다 LPU 쪽에 더 집중하는 신호로 해석했다. 단, CPX가 완전히 폐기됐다고 단정하기는 어렵고, 일부 고객용 off-roadmap 제품으로 남을 가능성도 언급했다. ([Tom's Hardware][9])

정리하면:

> CPX = 긴 자료를 처음 읽는 데 특화된 가속기
> 현재 메시지상 우선순위는 낮아진 것으로 보이나, 완전 폐기 여부는 확정하기 어렵다.

### LPX / LPU

LPX는 Groq LPU를 NVIDIA Vera Rubin 플랫폼에 붙인 저지연 추론 rack이다. LPU는 Language Processing Unit, 즉 언어모델 추론에 특화된 프로세서로 이해하면 된다.

LPX의 강점은 세 가지다.

| 강점 | 쉬운 설명 |
|---|---|
| 낮은 지연시간 | 답변이 끊기지 않고 빨리 나옴 |
| 예측 가능한 실행 | 사용자별 응답 속도 편차가 줄어듦 |
| SRAM 기반 고속 처리 | 작지만 매우 빠른 메모리로 decode 작업을 처리 |

NVIDIA는 LPX를 Rubin GPU와 함께 쓰는 구조로 설명한다. Rubin GPU는 prefill과 decode attention을 맡고, LPX는 decode 중 FFN/MoE 같은 지연 민감 연산을 맡는다. ([NVIDIA Developer][3])

쉽게 말하면:

> Rubin GPU = 무거운 범용 엔진
> LPX = 답변 생성 속도를 끌어올리는 초고속 보조 엔진

### CMX

CMX는 KV cache 전용 메모리/스토리지 계층이다.

AI agent 시대에는 대화, 코드, 툴 호출, 검색 결과, 작업 히스토리가 길어진다. 이때 KV cache가 폭증한다. 모든 KV cache를 GPU HBM에만 넣으면 너무 비싸다. 반대로 일반 SSD나 object storage에 넣으면 너무 느리다. CMX는 그 중간에 놓는 계층이다.

| 위치 | 쉬운 비유 | 특징 |
|---|---|---|
| GPU HBM | 책상 위 메모 | 가장 빠르지만 비쌈 |
| CMX | 바로 옆 캐비닛 | 꽤 빠르고 훨씬 큼 |
| 일반 스토리지 | 창고 | 크지만 느림 |

NVIDIA는 CMX를 GPU HBM과 일반 스토리지 사이의 G3.5 계층으로 설명하며, KV cache를 pod 단위에서 공유·재사용하게 해 긴 context와 agentic inference의 병목을 줄이는 구조로 제시한다. ([NVIDIA Developer][7])

쉽게 말하면:

> CMX = AI의 대화 기억을 싸고 빠르게 보관하는 전용 캐시 창고

### Dynamo

Dynamo는 NVIDIA 추론 인프라의 교통 관제 시스템이다. GPU, LPX, CMX, KV cache, storage가 아무리 좋아도 요청을 어디로 보낼지, 어떤 캐시를 재사용할지, 어떤 GPU가 이미 필요한 기억을 갖고 있는지 모르면 효율이 떨어진다.

Dynamo는 이걸 조율한다. NVIDIA는 Dynamo 1.0이 inference work를 GPU와 lower-cost storage 사이에서 나누고, agentic AI와 long prompt에서 관련 KV cache를 이미 가진 GPU로 요청을 라우팅할 수 있다고 설명한다. ([NVIDIA Newsroom][8])

쉽게 말하면:

> Dynamo = "이 요청은 저 GPU로 보내라. 그 GPU가 이미 관련 기억을 갖고 있다"고 판단하는 AI factory 운영체제

## 0.2 왜 CPX보다 LPX·CMX인가

### CPX는 "처음 읽기"를 잘하지만, LPX는 "계속 말하기"를 잘한다

CPX의 타깃은 prefill이다. 긴 문서를 처음 읽을 때는 유용하다.

하지만 실제 AI 서비스에서 사용자가 체감하는 병목은 자주 decode에 있다. 답변이 늦게 나오거나, 코딩 agent가 다음 파일 수정까지 오래 걸리거나, voice assistant가 말이 끊기면 사용자는 바로 불편함을 느낀다.

NVIDIA도 LPX 설명에서 긴 reasoning output, prefix caching, longer context 때문에 workload가 decode 쪽으로 더 많이 이동한다고 설명한다. ([NVIDIA Developer][3])

따라서 CPX보다 LPX가 전면에 서는 논리는 단순하다.

> 한 번 읽는 속도보다, 매 토큰을 반복해서 생성하는 속도가 서비스 품질과 과금에 더 직접적이다.

### Agentic AI에서는 KV cache가 핵심 자산이 된다

일반 챗봇은 질문 하나에 답 하나를 주고 끝난다. 하지만 agent는 다르다. 예를 들어 coding agent는 코드 읽기, 수정안 생성, 테스트 실행, 에러 읽기, 다시 수정, 다시 테스트, 결과 보고를 반복한다.

이 과정에서 이전 context를 계속 기억해야 한다. 그러면 KV cache가 단순한 임시 메모가 아니라 <strong>agent의 작업 기억</strong>이 된다.

NVIDIA는 CMX 설명에서 long context와 agentic workflow가 커질수록 KV cache 용량 요구가 비례적으로 증가하고, 이를 재사용·저장하는 것이 성능과 효율에 필수라고 설명한다. ([NVIDIA Developer][7])

따라서 CMX가 중요해진다.

> Agentic AI 시대의 병목은 "계산"만이 아니라 "기억을 어디에 두고 얼마나 빨리 다시 꺼내느냐"다.

### LPX는 사용자 체감 성능을 직접 개선한다

AI 서비스에서 중요한 것은 평균 처리량만이 아니다. 사용자는 "내 답변이 지금 바로 나오느냐"를 본다.

LPX는 SRAM, compiler-orchestrated execution, deterministic execution을 통해 latency와 jitter를 줄이는 방향이다. NVIDIA는 LPU의 deterministic execution이 time-to-first-token과 per-token latency를 안정적으로 유지하는 데 도움이 된다고 설명한다. ([NVIDIA Developer][3])

쉽게 말하면:

> GPU만으로는 대형 식당의 총 조리량은 크지만, 특정 손님의 음식이 늦게 나올 수 있다. LPX는 VIP 주문을 빠르게 처리하는 전용 라인이다.

### CMX는 비싼 GPU가 놀지 않게 만든다

GPU가 가장 비싸다. 그런데 GPU가 데이터를 기다리느라 쉬고 있으면 돈이 샌다.

CMX는 KV cache를 GPU 가까운 곳에 보관하고 미리 가져오는 방식으로 GPU idle과 재계산을 줄이는 역할을 한다. NVIDIA는 CMX가 전통적 스토리지 대비 최대 5배 tokens-per-second와 5배 power efficiency 개선을 목표로 한다고 설명한다. ([NVIDIA Developer][7])

투자자 언어로 바꾸면:

> CMX는 GPU CAPEX의 가동률을 높여 토큰당 원가를 낮추는 인프라다.

### NVIDIA 입장에서는 "칩 하나"보다 "시스템 전체"가 더 강한 락인이다

CPX는 개별 가속기 성격이 강하다. 반면 LPX·CMX·Dynamo는 NVIDIA가 AI factory 전체를 장악하는 구조다.

| 계층 | 역할 |
|---|---|
| Rubin GPU | 대형 계산, prefill, attention, training/inference 범용 처리 |
| LPX / LPU | 저지연 decode 가속 |
| CMX | KV cache 전용 context memory tier |
| Spectrum-X / NVLink | 데이터 이동 |
| BlueField-4 DPU | storage/network I/O 처리 |
| Dynamo | 요청 라우팅, KV cache 이동, GPU/메모리 오케스트레이션 |

이 구조가 강한 이유는 고객이 단순히 GPU를 사는 것이 아니라, <strong>추론 서비스 운영 전체를 NVIDIA 방식으로 최적화</strong>하게 되기 때문이다.

## 0.3 CPX, LPX, CMX를 한 문장으로 비교

| 용어 | 한 문장 설명 | 비유 | 핵심 병목 |
|---|---|---|---|
| CPX | 긴 문맥을 처음 읽는 가속기 | 두꺼운 책을 빨리 읽는 독서기 | Prefill |
| LPX | 답변을 한 토큰씩 빠르게 생성하는 가속기 | 말을 빠르고 일정하게 해주는 발성 엔진 | Decode latency |
| CMX | AI의 이전 기억을 저장·재사용하는 KV cache 계층 | 대화 메모 전용 캐비닛 | KV cache capacity / movement |
| Dynamo | 전체 추론 작업을 배치·라우팅하는 운영체제 | 관제탑 | GPU utilization / routing |
| Rubin GPU | 대형 범용 AI 엔진 | 메인 엔진 | Training, prefill, attention, general inference |

## 0.4 가장 중요한 오해 교정

### 오해 1. "LPX가 HBM을 대체한다"

부정확하다. LPX는 HBM을 대체하는 것이 아니라, <strong>HBM 기반 GPU가 잘 못하는 일부 decode latency 영역을 보완</strong>한다.

HBM은 여전히 Rubin GPU의 핵심이다. LPX는 SRAM 기반으로 작고 빠른 작업을 맡고, CMX는 KV cache를 HBM 바깥으로 일부 확장한다.

정확한 표현은 다음이다.

> LPX·CMX는 HBM 수요를 없애는 구조가 아니라, HBM을 더 비싼 계산에 집중시키고 주변 병목을 분산시키는 구조다.

### 오해 2. "CPX는 의미가 없어졌다"

그 정보에 대해서는 확실하지 않다. 불확실한 지점은 <strong>CPX가 완전히 취소된 것인지, 아니면 공개 로드맵 우선순위에서 내려간 것인지</strong>다.

확인 경로는 NVIDIA의 최신 공식 roadmap, GTC 2026 keynote slide, 차기 실적발표 또는 고객사 시스템 발표다. 현재 공개 보도 기준으로는 CPX가 GTC 2026 keynote와 roadmap slides에서 보이지 않고 LPX가 부각됐다는 해석이 있지만, off-roadmap 고객용 제품 가능성은 남아 있다. ([Tom's Hardware][9])

보수적 판단은 다음이다.

> CPX 완전 폐기보다 "전략적 주력 메시지가 LPX·CMX로 이동했다"가 더 안전한 표현이다.

### 오해 3. "추론은 GPU만 좋으면 된다"

이제는 아니다. 추론 병목은 GPU compute, HBM, SRAM, KV cache, storage, networking, routing software가 결합된 문제다.

그래서 NVIDIA가 GTC 2026 이후 강조하는 구조는 단순 GPU가 아니라 <strong>AI factory stack</strong>이다.

## 0.5 비전공자용 핵심 해석

과거 AI 인프라 경쟁은 "누가 가장 강한 GPU를 갖고 있느냐"였다. 이때 핵심은 학습이었다. 큰 모델을 만들려면 엄청난 GPU와 HBM이 필요했다.

그런데 이제 전장이 바뀌고 있다. AI가 실제 서비스로 들어가면서 매일 수십억~수조 개의 토큰을 처리해야 한다. 사용자는 답변이 늦으면 떠난다. 기업은 토큰당 원가가 높으면 마진이 깨진다. AI agent는 긴 대화와 작업 히스토리를 계속 기억해야 한다.

이 환경에서는 단순히 GPU 하나가 빠른 것만으로 부족하다.

첫째, AI가 긴 자료를 처음 읽어야 한다. 이것은 CPX나 Rubin GPU가 맡을 수 있다. 둘째, AI가 답변을 한 토큰씩 빠르게 생성해야 한다. 이것이 LPX의 영역이다. 셋째, AI가 이전 대화와 작업 상태를 다시 계산하지 않도록 저장해야 한다. 이것이 CMX의 영역이다. 넷째, 어떤 요청을 어느 GPU로 보내고, 어떤 KV cache를 재사용할지 결정해야 한다. 이것이 Dynamo의 영역이다.

따라서 GTC 2026 이후 NVIDIA 전략의 본질은 다음이다.

> "GPU를 더 많이 팔겠다"에서 "AI 추론 공장 전체를 설계하고 운영하겠다"로 이동한 것이다.

이 관점에서 CPX는 좋은 제품일 수 있지만, 전략의 중심이 되기에는 범위가 좁다. CPX는 긴 context를 처음 처리하는 특정 구간에 강하다. 반면 LPX와 CMX는 실제 AI 서비스의 반복적이고 비싼 병목, 즉 decode latency와 KV cache reuse를 직접 겨냥한다.

투자 관점에서는 이 변화가 중요하다. AI 추론 인프라의 수혜는 더 이상 HBM 하나로만 설명되지 않는다. HBM은 계속 중요하지만, 동시에 고속 네트워크, DPU, SSD/스토리지, CXL/메모리 계층, 기판, 패키징, 전력, 냉각까지 같이 봐야 한다. AI 추론 스택이 "GPU 중심 단일 병목"에서 <strong>"메모리·네트워크·스토리지·소프트웨어가 결합된 복합 병목"</strong>으로 바뀌고 있기 때문이다.

*이 글의 결론은 단순하다. 방향성은 맞다. 다만 표현은 정교해야 한다. GTC 2026 이후 NVIDIA의 추론 전략은 Vera Rubin GPU 하나를 더 크게 파는 것이 아니라, Vera Rubin GPU/CPU, Groq 3 LPX/LPU, BlueField-4 STX·CMX, Spectrum-X/SPX, Dynamo를 묶는 heterogeneous AI factory로 이동했다. CPX는 기존에 long-context prefill/context phase를 겨냥한 GPU였지만, GTC 2026의 공식 전면 메시지에서는 LPX·STX·CMX 조합이 올라왔다. 그러나 NVIDIA가 CPX를 공식적으로 폐기했다고 단정할 공개 문장은 아직 부족하다.*

## 핵심 요약

- <strong>[Fact]</strong> NVIDIA는 GTC 2026에서 Vera Rubin platform을 Vera Rubin NVL72 GPU rack, Vera CPU rack, Groq 3 LPX inference accelerator rack, BlueField-4 STX storage rack, Spectrum-6 SPX Ethernet rack으로 구성된 rack-scale AI factory로 제시했다. ([NVIDIA Newsroom][1])
- <strong>[Fact]</strong> CPX는 2025년에 1M+ token long-context processing과 context phase acceleration을 겨냥한 GPU로 소개됐다. 128GB GDDR7, 30 PFLOPS NVFP4, attention acceleration이 핵심 메시지였다. ([NVIDIA Developer][2])
- <strong>[Fact]</strong> LPX는 CPX와 성격이 다르다. NVIDIA는 LPX가 decode loop 안의 latency-sensitive FFN/MoE 실행과 speculative decoding draft generation을 맡고, Rubin GPU가 prefill, decode attention, verification을 계속 담당한다고 설명한다. ([NVIDIA Developer][3])
- <strong>[Inference]</strong> 따라서 LPX는 HBM bearish가 아니다. Rubin GPU/HBM은 large memory와 attention을 담당하고, LPU/SRAM은 저지연 decode 경로를 보완한다. 여기에 CMX/STX가 KV-cache storage tier를 만든다.
- <strong>한국 read-through</strong>는 삼성전자가 가장 넓다. HBM4·SOCAMM2, Groq LPU foundry, PCIe Gen6 eSSD/KV-cache가 한 회사 안에 묶인다. SK하이닉스는 HBM beta가 더 깨끗하지만, 이 글의 incremental alpha는 "HBM만"이 아니라 memory hierarchy 전체다.

## 1. 사용자 가설별 판정

| 주장 | 판정 | 코멘트 |
|---|---:|---|
| GTC 2026 이후 NVIDIA의 전면 전략은 Vera Rubin GPU + Groq 3 LPX/LPU + storage/networking 조합으로 이동했다 | <strong>대체로 맞음</strong> | 공식 Vera Rubin platform 발표가 GPU, CPU, LPX, STX, SPX를 한 platform으로 묶었다. "GPU 단독 확장"보다 pod/rack orchestration에 가깝다. |
| CPX는 prefill/context 병목을 겨냥한 제품이었다 | <strong>맞음</strong> | NVIDIA의 CPX 설명은 long-context context phase와 1M+ token workload를 겨냥했다. |
| 돈이 되는 병목은 prefill보다 decode다 | <strong>조건부로 맞음</strong> | coding agent, voice assistant, multi-turn agentic workflow에서는 decode latency와 tail latency가 과금·체감 품질에 더 가깝다. 다만 long-document ingest, video, codebase 전체 분석에서는 prefill/context도 여전히 고가치 병목이다. |
| NVIDIA가 CPX보다 LPX를 우선시했을 가능성이 있다 | <strong>강한 추론</strong> | GTC 2026 전면 메시지에서 LPX·STX·SPX가 올라왔고 CPX는 주역에서 빠졌다. 다만 "CPX 공식 취소"는 아직 [Blocked]다. |
| CPX 역할이 Vera Rubin + LPX + CMX/STX 조합에 흡수됐다 | <strong>부분적으로 맞음</strong> | CPX의 context 역할 일부는 Rubin GPU와 CMX/STX KV-cache 계층으로 분산되고, CPX가 직접 해결하지 못한 low-latency decode는 LPX가 맡는다. 1:1 대체는 아니다. |
| Groq LPX/LPU는 HBM을 대체한다기보다 HBM GPU의 decode 약점을 보완한다 | <strong>맞음</strong> | Rubin GPU는 HBM 기반 large-memory/attention engine, LPU는 SRAM 기반 low-latency token engine이다. |
| 삼성전자가 Groq LPU 제조 파트너로 들어갔다 | <strong>대체로 맞음</strong> | Samsung Semiconductor는 Jensen Huang이 GTC 2026에서 삼성의 Groq LPU 제조 역할을 언급했다고 설명했다. 정확한 LP30 물량·마진·수율은 공개되지 않았다. ([Samsung Semiconductor][4]) |

## 2. Vera Rubin은 단일 GPU가 아니라 POD-scale AI factory다

NVIDIA의 공식 메시지는 "Vera Rubin GPU가 빠르다"가 아니다. 더 중요한 변화는 AI factory를 다섯 개 rack-scale system으로 쪼개고 다시 묶었다는 점이다.

| 시스템 | 역할 | 투자적 의미 |
|---|---|---|
| Vera Rubin NVL72 GPU rack | pretraining, post-training, prefill, decode attention, verification | HBM4와 GPU compute가 여전히 본류다. |
| Vera CPU rack | agentic AI workload의 CPU orchestration, coherent memory, host-side scheduling | CPU가 AI rack의 조율 계층으로 재평가된다. |
| Groq 3 LPX inference accelerator rack | low-latency decode FFN/MoE, draft generation, deterministic token path | premium interactive inference의 tail latency를 가격화하려는 시도다. |
| BlueField-4 STX / CMX storage rack | KV-cache storage, context memory tier, cache reuse | GPU HBM을 계속 점유하던 KV-cache 비용을 pod-level storage로 내리려는 구조다. |
| Spectrum-6 SPX / Spectrum-X fabric | GPU, LPU, storage, DPU 사이의 deterministic fabric | "칩"보다 rack utilization과 data movement가 병목이 된다. |

이 구조에서 NVIDIA의 moat는 GPU FLOPS만이 아니다. NVIDIA는 token economics 전체, 즉 prefill cost, decode latency, KV-cache reuse, networking jitter, watts/token, rack utilization까지 한 번에 잡으려 한다. 그래서 이번 변화는 "CPX가 빠졌다"보다 "NVIDIA가 inference를 더 잘게 분해해 각각 monetization point를 만들었다"로 읽어야 한다.

## 3. CPX·LPX·CMX의 역할 분해

CPX와 LPX를 같은 "추론 칩"으로 보면 헷갈린다. 둘은 서로 다른 병목을 겨냥했다.

| 구분 | CPX | LPX/LPU | CMX/STX |
|---|---|---|---|
| 기본 성격 | GDDR7 기반 context GPU | SRAM 기반 low-latency decode accelerator | BlueField-4 기반 context memory / KV-cache storage tier |
| 핵심 병목 | long-context prefill, context phase, attention-heavy input processing | decode loop 내 FFN/MoE, pointwise operation, speculative decoding draft generation | multi-turn·long-context에서 커지는 KV-cache 저장·이동·재사용 |
| 주요 자원 | 128GB GDDR7, 30 PFLOPS NVFP4 | LPX rack 기준 256 LPU, 128GB SRAM, 40PB/s SRAM bandwidth | flash/storage + DPU + Spectrum-X + DOCA/Dynamo |
| GPU/HBM과 관계 | Rubin GPU 옆의 context 전용 GPU | Rubin GPU/HBM을 보완하는 SRAM decode tier | GPU HBM을 보완하는 external context memory tier |
| 투자 해석 | "context가 너무 길다"는 문제의 해법 | "interactive token latency가 돈이 된다"는 문제의 해법 | "KV cache가 HBM을 잠식한다"는 문제의 해법 |

NVIDIA의 LPX 기술 블로그는 역할을 꽤 명확히 나눈다. Rubin GPU는 long-context prefill, decode attention, high-concurrency inference를 맡는다. LPX는 latency-sensitive token generation, FFN/MoE expert execution, speculative decoding의 draft path를 맡는다. 즉 LPX는 HBM을 죽이는 칩이 아니라 HBM GPU가 잘 못하는 작은 batch·저지연 decode 경로를 받아주는 보조 엔진이다. ([NVIDIA Developer][3])

## 4. "돈 되는 병목은 decode"라는 말의 강점과 한계

이 문장은 절반 이상 맞다. 특히 다음 workload에서는 decode가 monetization bottleneck에 가깝다.

- agentic coding assistant
- multi-agent workflow
- voice interaction
- real-time translation
- tool-calling loop가 많은 enterprise copilot
- 긴 reasoning output을 요구하는 premium AI service

사용자는 prefill throughput을 직접 느끼지 않는다. 하지만 time-to-first-token, tokens/sec/user, tail latency는 바로 느낀다. 그리고 agentic workflow에서는 한 번의 지연이 아니라 수십 번의 model call 지연이 누적된다. LPX가 전면에 올라온 이유가 여기 있다.

그러나 decode가 항상 prefill보다 돈이 된다고 말하면 과하다. long-context RAG, codebase 전체 분석, 대용량 문서 처리, video understanding, batch summarization에서는 입력 context를 먹고 KV-cache를 만드는 비용이 여전히 크다. CPX가 나온 이유도 이 병목이 실제였기 때문이다. GTC 2026 이후 더 정확한 표현은 다음이다.

> 고부가 interactive/agentic inference에서는 decode latency가 monetization 병목으로 부상했고, NVIDIA는 이를 LPX/LPU로 보완한다. 그러나 long-context AI에서는 prefill과 KV-cache movement도 여전히 핵심 병목이며, 이는 Rubin GPU와 CMX/STX storage/networking 계층이 담당한다.

## 5. 투자 read-through

### NVIDIA: GPU 회사에서 token factory OS로

NVIDIA의 장기 논리는 "더 빠른 GPU"보다 "더 많은 inference attachment"다. Vera Rubin rack에 GPU만 붙는 것이 아니라 LPX, BlueField-4, Spectrum-6, CMX, Dynamo가 붙으면 NVIDIA는 AI factory의 더 많은 층위에서 toll을 받는다.

이것이 좋은 이유는 명확하다. 고객이 필요한 것은 chip benchmark가 아니라 token throughput, low tail latency, watts/token, utilization이다. NVIDIA는 이 네 가지를 rack/POD 단위로 파는 회사가 된다.

반대 논리도 있다. Google TPU, hyperscaler custom ASIC, Cerebras 같은 specialist inference chip은 NVIDIA tax를 줄이려 한다. 또 LPX·CMX가 production workload에서 vendor claim만큼의 TCO 개선을 보여주지 못하면 attachment narrative는 약해진다. 따라서 NVDA의 다음 체크포인트는 GPU 매출만이 아니라 Rubin rack당 LPX·CMX·Spectrum attach rate다.

### 삼성전자: 메모리 사이클주에서 inference memory hierarchy supplier로

삼성전자는 이 변화의 가장 넓은 한국 노출이다. 이유는 네 가지다.

1. <strong>HBM4/HBM4E</strong>: Vera Rubin GPU의 large-memory tier.
2. <strong>SOCAMM2</strong>: Vera CPU와 AI server memory architecture.
3. <strong>Groq LPU foundry</strong>: LPX의 SRAM decode tier에 들어가는 AI logic manufacturing option.
4. <strong>PCIe Gen6 eSSD / KV-cache storage</strong>: CMX/STX가 여는 context memory tier.

Samsung Semiconductor는 GTC 2026에서 HBM4E, HBM5 architecture, SOCAMM2, PM1763 PCIe 6.0 SSD를 전시했고, Jensen Huang이 삼성의 Groq LPU 제조 역할을 언급했다고 밝혔다. ([Samsung Semiconductor][4]) 삼성전자 1Q26 실적 자료도 HBM4와 SOCAMM2의 Vera Rubin platform용 mass product sales, PCIe Gen6 SSD 개발을 언급했다. ([Samsung Newsroom][5])

따라서 삼성전자 thesis는 "HBM 후발주자가 따라잡는다"만으로는 좁다. 더 넓은 문장은 이렇다.

> 삼성전자는 NVIDIA inference stack에서 HBM4, SOCAMM2, LPU foundry, KV-cache SSD가 동시에 걸리는 memory hierarchy supplier로 재분류될 수 있다.

다만 이 thesis는 증거를 요구한다. LPU yield와 margin, HBM4E customer acceptance, SOCAMM2 출하, PCIe Gen6 eSSD의 실제 KV-cache attachment가 확인되어야 한다.

### SK하이닉스·Micron: HBM winner지만 incremental alpha는 좁다

LPX는 HBM bearish가 아니다. 오히려 Rubin GPU/HBM을 premium inference stack의 중심에 남겨두면서, low-latency decode만 SRAM LPU가 나눠 맡는 구조다. 그래서 SK하이닉스와 Micron의 HBM thesis가 훼손되는 것은 아니다.

다만 이 글에서 새로 생긴 알파는 "HBM이 좋다"가 아니다. 그건 이미 시장의 중심부다. 새 알파는 HBM 위와 아래에 SRAM decode tier, KV-cache storage tier, rack networking tier가 추가되는 구조다. 그래서 순수 HBM beta는 SK하이닉스가 강하지만, architecture read-through는 삼성전자가 더 넓다.

### 삼성전기: 직접 주역은 아니지만 전력무결성 read-through는 유지

LPX/CMX 구조는 GPU 숫자만 늘리는 이야기가 아니다. rack 안의 칩 종류가 늘고, low-latency path와 high-bandwidth memory path가 동시에 커지면 전력무결성, 고속기판, SiCap/MLCC, FC-BGA의 중요도도 유지된다.

삼성전기는 이 글의 주인공은 아니다. 그러나 마벨 실적에서 확인된 custom XPU·optical·scale-up networking thesis와 마찬가지로, NVIDIA의 heterogeneous AI factory는 한국 부품주에 "GPU 옆의 작은 병목"이 계속 비싸질 수 있다는 신호를 준다.

## 6. 체크리스트

이 thesis를 유지하려면 아래 항목을 순서대로 확인해야 한다.

| 체크포인트 | 의미 |
|---|---|
| Groq 3 LPX H2 2026 availability | LPX가 slide가 아니라 실제 deployment로 넘어가는지 확인 |
| Samsung LPU mass production | 삼성 파운드리의 AI inference logic reference 확보 여부 |
| HBM4E sample/customer acceptance | 삼성 메모리의 Vera Rubin 후속 플랫폼 침투율 |
| SOCAMM2 출하 지속성 | CPU/agentic AI memory architecture의 실적화 |
| PCIe Gen6 eSSD와 CMX/STX 채택 | KV-cache storage tier가 실제 매출로 이어지는지 |
| CPX 후속 로드맵 | CPX가 보류인지, niche product인지, 재등장하는지 |
| Dynamo/AFD production benchmark | heterogeneous decode가 실제 TCO를 낮추는지 |

## 최종 판단

사용자의 thesis는 방향이 맞다. NVIDIA는 GTC 2026 이후 inference를 GPU 단독 확장이 아니라 <strong>HBM GPU + SRAM LPU + KV-cache storage + high-speed networking + orchestration software</strong>로 분해하고 있다.

다만 가장 안전한 표현은 이렇다.

> GTC 2026 이후 NVIDIA의 inference 전략은 Vera Rubin GPU 중심의 homogeneous scaling에서, Vera Rubin NVL72 + Groq 3 LPX/LPU + BlueField-4 STX/CMX + Spectrum-X/SPX를 결합한 heterogeneous AI factory 구조로 확장됐다. 기존 Rubin CPX는 long-context prefill/context 병목을 겨냥한 GDDR7 기반 context GPU였으나, GTC 2026 공식 플랫폼 메시지에서는 LPX와 KV-cache storage/networking 계층이 전면에 배치됐다. 단, CPX의 공식 취소 여부는 아직 공개자료만으로는 단정하기 어렵다.

투자적으로 더 중요한 문장은 이것이다.

> LPX는 HBM 대체재가 아니다. HBM GPU가 large model, large context, attention, verification을 계속 담당하고, LPX는 GPU가 비효율적인 small-batch·low-latency decode 경로를 보완한다. 그래서 이 변화는 HBM bearish가 아니라 AI inference memory hierarchy가 더 복잡해졌다는 신호다.

## 근거 구분 Appendix

### [Fact]

- NVIDIA Vera Rubin platform은 Vera Rubin NVL72, Vera CPU, Groq 3 LPX, BlueField-4 STX, Spectrum-6 SPX rack을 포함한다. ([NVIDIA Newsroom][1])
- CPX는 2025년에 1M+ token context workload용 GPU로 발표됐다. ([NVIDIA Developer][2])
- LPX는 256개 LPU, 128GB SRAM, 40PB/s on-chip SRAM bandwidth, 640TB/s scale-up bandwidth를 갖는 rack-scale inference accelerator로 제시됐다. ([NVIDIA Developer][3])
- Groq와 NVIDIA의 거래는 비독점 inference technology licensing agreement이며, Groq는 독립 운영을 지속한다고 발표했다. ([Groq][6])
- Samsung은 GTC 2026에서 HBM4E, SOCAMM2, PM1763 PCIe 6.0 SSD를 전시했고, Groq LPU 제조 파트너로 언급됐다. ([Samsung Semiconductor][4])

### [Inference]

- GTC 2026 전면 메시지에서 CPX보다 LPX·CMX/STX·SPX 조합이 우선순위로 올라왔다는 해석은 타당하다.
- LPX는 HBM 수요를 대체하기보다 Rubin GPU/HBM의 utilization과 premium inference economics를 보완할 가능성이 크다.
- 삼성전자의 투자 포인트는 HBM4 단일 thesis보다 HBM4 + SOCAMM2 + LPU foundry + eSSD/KV-cache의 조합에 있다.

### [Speculation]

- CPX가 완전히 폐기됐거나 LPX+CMX에 공식 흡수됐다는 주장은 아직 확인되지 않았다.
- Groq LP30/LPU의 구체 물량, ASP, wafer allocation, gross margin은 공개 자료만으로 확인되지 않는다.
- LPX와 CMX가 NVIDIA가 주장하는 수준의 perf/W, revenue uplift, TPS 개선을 production workload에서 재현할지는 아직 검증 전이다.

### [Blocked]

- CPX의 공식 cancellation 여부.
- Groq 3 LPX rack ASP와 고객별 order quantity.
- 삼성 파운드리의 LPU yield, wafer price, margin contribution.
- CMX/STX의 고객별 KV-cache storage attachment와 실제 TCO 개선폭.

*이 글은 리서치와 논평으로만 활용해야 하며 투자 조언이 아닙니다. 제품 로드맵, 수율, 고객 채택, 가격, 매출 인식은 공개자료와 회사 발표 이후에도 바뀔 수 있습니다.*

[1]: https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform "NVIDIA Vera Rubin Opens Agentic AI Frontier | NVIDIA Newsroom"
[2]: https://developer.nvidia.com/blog/nvidia-rubin-cpx-accelerates-inference-performance-and-efficiency-for-1m-token-context-workloads/ "NVIDIA Rubin CPX Accelerates Inference Performance and Efficiency for 1M+ Token Context Workloads | NVIDIA Technical Blog"
[3]: https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/ "Inside NVIDIA Groq 3 LPX | NVIDIA Technical Blog"
[4]: https://semiconductor.samsung.com/news-events/tech-blog/architecting-the-ai-era-samsung-electronics-and-nvidia-define-the-future-at-gtc-2026/ "Architecting the AI Era: Samsung Electronics and NVIDIA Define the Future at GTC 2026 | Samsung Semiconductor"
[5]: https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results "Samsung Electronics Announces First Quarter 2026 Results | Samsung Global Newsroom"
[6]: https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale "Groq and NVIDIA Enter Non-Exclusive Inference Technology Licensing Agreement | Groq"
[7]: https://developer.nvidia.com/blog/introducing-nvidia-bluefield-4-powered-inference-context-memory-storage-platform-for-the-next-frontier-of-ai/ "Introducing NVIDIA BlueField-4-Powered CMX Context Memory Storage Platform for the Next Frontier of AI | NVIDIA Technical Blog"
[8]: https://nvidianews.nvidia.com/news/dynamo-1-0 "NVIDIA Enters Production With Dynamo, the Broadly Adopted Inference Operating System for AI Factories | NVIDIA Newsroom"
[9]: https://www.tomshardware.com/pc-components/gpus/nvidia-removes-rubin-cpx-accelerators-from-its-roadmap-groq-3-lpus-take-center-stage-as-cpx-is-removed "Nvidia removes Rubin CPX accelerators from its roadmap — Groq 3 LPUs take center stage as CPX is removed | Tom's Hardware"
