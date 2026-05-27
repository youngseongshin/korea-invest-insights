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
