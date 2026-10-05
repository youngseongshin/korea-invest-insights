---
title: "연산은 아끼고 기억은 쌓입니다: 에이전트 시대에 한국 메모리가 로직을 품는 이유"
date: 2026-10-05T22:20:00+09:00
categories: ["Exclusive Analysis", "AI Infrastructure", "Korean-Equities"]
tags: ["메모리", "삼성전자", "SK하이닉스", "HBM", "커스텀 HBM", "에이전트", "KV 캐시", "기업용 SSD", "HBF", "CXL", "장기공급계약"]
slug: "agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05"
description: "일을 통째로 맡기는 AI 에이전트가 늘면 연산은 싸지고 문맥과 지식은 쌓입니다. 배치와 실시간의 분화, CPU·네트워크 수요, 로직을 품는 HBM·SSD, 장기계약과 예치금을 근거로 한국 메모리의 투자 논리와 현재 주가가 요구하는 이익 지속성을 계산합니다."
image: "cover.png"
draft: false
---

같은 AI 모델에 같은 질문을 보내도 가격은 처리 방식에 따라 크게 갈립니다. Anthropic의 가격표에서 Opus 5.5는 하루 안에만 답하면 되는 배치 처리가 정가의 절반이고, 빠른 응답을 보장받는 고속 모드는 정가의 두 배입니다. 이미 읽은 문맥을 다시 읽는 값은 정가의 20분의 1입니다.[^anthropic-pricing]

이 가격표는 AI 인프라가 어디로 가는지를 압축해서 보여줍니다. 급하지 않은 일은 싸게, 급한 일은 비싸게 처리합니다. 그리고 가장 싼 것은 새로 계산하는 일이 아니라 기억해 둔 것을 다시 꺼내는 일입니다.

<strong>일을 통째로 맡기는 위임형 에이전트가 늘수록 연산은 효율화되고, 문맥과 지식은 쌓입니다. 쌓이는 것을 담는 메모리와 저장장치는 규격품에서 로직을 품은 제품으로 바뀌고 있습니다. 한국 메모리 투자의 방점은 올해 이익의 크기보다 그 이익이 얼마나 오래 남는가에 있습니다.</strong>

검증할 연결은 차례로 이어집니다. 인프라가 상시 컴퓨팅으로 바뀌는지, 연산이 실제로 효율화되는지, 무엇이 누적되는지, 메모리에 로직이 들어가는 변화가 매출로 확인되는지, 그 가치가 한국 기업에 남는지입니다. 끝에서는 삼성전자와 SK하이닉스의 현재 주가가 어느 정도의 이익 지속성을 요구하는지 계산합니다.

분석 기준일은 2026년 10월 5일입니다. 주가는 10월 2일 종가이며, 10월 5일에는 한국 정규장 체결 기록이 없었습니다. 회사 발표, 조사기관 전망, 이 글의 계산 가정을 구분해서 적었습니다. 아래 민감도 표는 검증용 계산이며 목표주가가 아닙니다.

<link rel="stylesheet" href="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/thesis.css">

## 인프라는 호출에 답하는 설비에서 목표를 붙들고 도는 설비로 바뀝니다

챗봇은 질문이 들어올 때만 계산합니다. 위임형 에이전트는 다릅니다. 사용자가 목표를 맡기면 계획을 세우고, 도구를 쓰고, 결과를 확인하고, 필요하면 다시 시도합니다. 사용자가 화면을 닫아도 일은 계속됩니다.

그래서 부하의 단위가 달라집니다. 챗봇 시대의 부하는 동시에 접속한 사용자 수에 가까웠습니다. 에이전트 시대의 부하는 사용자 수에 사용자당 맡긴 목표의 수와 그 목표가 살아 있는 시간을 곱한 값에 가깝습니다. 이런 구조가 목적지향형 상시 컴퓨팅입니다.

이미 제품과 가격표에 흔적이 있습니다. Anthropic의 Managed Agents는 토큰 요금과 별도로 세션이 살아 있는 시간에 시간당 0.08달러를 매깁니다. 문서는 이 세션에 배치 할인이 적용되지 않는 이유를 세션이 상태를 유지하기 때문이라고 설명합니다.[^anthropic-pricing][^managed-agents]

Google은 2026년 5월 개발자 행사에서 전용 가상머신에서 하루 종일 도는 개인 에이전트를 소개했습니다. 같은 발표에서 월간 처리 토큰이 2025년 5월 약 480조 개에서 2026년 5월 3,200조 개 이상으로 늘었다고 밝혔습니다. 1년에 약 7배입니다. 회사가 공개한 수치이며, 그중 에이전트의 몫은 따로 공개되지 않았습니다.[^google-io]

작업 시간도 길어지고 있습니다. 평가기관 METR의 2026년 1월 측정에서 Claude Opus 4.5가 절반의 확률로 끝낼 수 있는 과제의 길이는 사람 기준 320분이었고, 2024년 이후 이 길이는 약 89일마다 두 배가 됐습니다. 과제 묶음의 상단이 불확실하다는 한계를 METR도 인정합니다.[^metr]

아래 그림은 이 글 전체의 논리 사슬입니다. 각 화살표는 사실이 아니라 검증할 연결입니다.

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/chain.svg" alt="위임형 에이전트에서 상시 컴퓨팅, 연산 효율화와 상태 누적, 로직을 품은 메모리, 이익 지속성으로 이어지는 논리 사슬"><figcaption>개념도. 수요가 늘어나는 것과 그 가치가 메모리 제조사에 남는 것은 서로 다른 연결입니다. 모바일에서는 그림을 가로로 움직여 읽을 수 있습니다.</figcaption></figure>

## 급한 일과 급하지 않은 일의 가격이 네 배까지 벌어졌습니다

상시로 도는 일은 모두 급하지 않습니다. 밤사이 문서를 정리하는 일과 사용자가 기다리는 답은 같은 설비를 쓸 이유가 없습니다. 모델 회사들은 이 차이를 가격으로 나눴습니다.

| 회사와 모델 | 배치 또는 저속 | 표준 | 고속 또는 우선 | 캐시된 문맥 읽기 |
|---|---:|---:|---:|---:|
| Anthropic Opus 5.5 | 0.5배 | 1배 | 2배 | 0.05배 |
| OpenAI gpt-6-astra | 0.5배 | 1배 | 2배 | 0.1배 |
| Google Gemini 3.1 Pro Preview | 0.5배 | 1배 | 1.8배 | 별도 저장 요금 |

세 회사 모두 같은 모델의 가격을 응답 속도에 따라 나눴습니다. 가장 싼 등급과 가장 비싼 등급의 차이는 3.6배에서 4배입니다. Google은 캐시에 문맥을 보관하는 시간에도 요금을 매깁니다. 문맥의 보관이 별도 상품이 됐다는 뜻입니다.[^anthropic-pricing][^openai-pricing][^google-pricing]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/pricing.svg" alt="Anthropic Opus 5.5의 표준 입력가 대비 배치, 고속, 캐시 읽기 가격 배수 막대그래프"><figcaption>Anthropic 공식 가격표 기준, 2026년 10월 5일 조회. 표준 입력가를 1로 놓은 배수입니다. 캐시 읽기는 이미 처리한 문맥을 다시 쓸 때의 입력가입니다.</figcaption></figure>

투자자에게 이 분화가 중요한 이유는 설비의 이용률 때문입니다. 실시간 수요만 받는 설비는 낮과 밤의 가동률 차이가 큽니다. 급하지 않은 일을 한가한 시간에 싸게 받으면 같은 설비가 하루 종일 돕니다. 상시 컴퓨팅은 수요의 양만 늘리는 것이 아니라 설비가 쉬는 시간을 줄입니다.

## 반복되는 일은 작은 모델과 코드로 내려갑니다

에이전트가 같은 종류의 일을 하루 수만 번 한다면 매번 가장 큰 모델을 부를 이유가 없습니다. 반복되는 세부 작업은 두 방향으로 내려갑니다. 하나는 그 일만 잘하는 작은 모델이고, 다른 하나는 모델 없이 도는 코드입니다.

작은 모델 쪽의 근거는 가격표입니다. OpenAI의 가격표에서 gpt-6-astra의 입력가는 100만 토큰당 10달러, gpt-6-luna는 0.10달러입니다. 같은 회사 안에서 100배 차이입니다. NVIDIA 연구진은 2025년 논문에서 에이전트 호출의 40~70%를 특화된 소형 모델로 바꿀 수 있다고 추정했습니다. 논문의 추정이며 실측 비중은 아닙니다.[^openai-pricing][^nvidia-slm]

코드 쪽의 근거는 제품 문서입니다. Anthropic의 Agent Skills 문서는 스킬 안의 스크립트가 셸에서 실행되고 그 결과만 모델의 문맥에 들어간다고 설명합니다. 스크립트 코드 자체는 문맥에 들어가지 않습니다. 모델이 매번 추론하던 절차를 한 번 굳힌 코드로 바꾸는 구조입니다.[^agent-skills]

웹 자동화 회사 Skyvern은 에이전트가 한 번 수행한 작업을 코드로 바꿔 모델 없이 재생한 결과를 공개했습니다. 실행 시간은 279초에서 120초로, 회당 비용은 0.11달러에서 0.04달러로 줄었습니다. 한 회사가 공개한 자체 측정입니다.[^skyvern]

여기서 중요한 구분이 생깁니다. 업무 한 건에 드는 연산은 줄어듭니다. 그러나 굳힌 코드, 특화 모델의 가중치, 실행 기록은 어딘가에 저장돼야 합니다. 효율화는 연산을 덜 쓰는 대신 저장해 둔 것을 더 많이 쓰는 방식으로 일어납니다.

## GPU만으로는 일이 끝나지 않습니다

에이전트의 한 작업은 여러 단계로 나뉩니다. 생각하는 단계는 GPU가 맡습니다. 도구를 실행하고, 파일을 다루고, 격리된 환경에서 코드를 돌리는 단계는 CPU가 맡습니다. 단계 사이에 데이터를 옮기는 일은 네트워크가 맡습니다.

CPU 수요에 대한 발언은 올해 여러 회사에서 같은 방향으로 나왔습니다. Amazon의 앤디 재시 최고경영자는 7월 실적 발표에서 에이전트의 도구 사용이 대부분 AI 가속기가 아닌 CPU에서 돈다고 말했습니다. AMD의 리사 수 최고경영자는 8월에 서버 CPU 시장이 2030년 2,200억 달러가 되고 에이전트와 격리 실행 환경이 가장 큰 부분이 된다고 전망했습니다. 두 발언 모두 경영진의 설명과 전망입니다.[^amzn-call][^amd-call]

실물 신호도 있습니다. TrendForce는 4월에 서버 CPU 가격이 3월 이후 10~20% 올랐고 납기가 1~2주에서 8~12주로 늘었다고 전했습니다. 대만과 일본 매체를 인용한 2차 보도입니다. NVIDIA는 에이전트 격리 실행을 용도로 명시한 88코어 Vera CPU를 출하했습니다.[^tf-cpu][^nvda-vera]

네트워크도 한 종류로 끝나지 않습니다. 랙 안에서 칩끼리 묶는 연결, 랙과 랙을 잇는 이더넷, 메모리를 넓히는 CXL이 함께 쓰입니다. Broadcom은 9월 실적 발표에서 AI 네트워킹 매출이 1년 전의 2.5배를 넘었고, 광통신용 레이저 수요가 공급을 크게 웃돈다고 말했습니다.[^avgo-call]

데이터 처리 장치도 따로 생겼습니다. NVIDIA는 3월에 저장장치 앞에서 문맥 데이터를 관리하는 BlueField-4 기반 설계를 발표했고, 파트너 제품이 2026년 하반기에 나온다고 밝혔습니다. 10월 5일 현재 실제 출하와 가동을 확인한 자료는 찾지 못했습니다.[^nvda-stx]

이 대목의 결론은 GPU가 덜 중요해진다는 것이 아닙니다. GPU, CPU, 데이터 처리 장치, 여러 종류의 네트워크가 함께 필요해진다는 것입니다. 그리고 이 장치들 모두에 메모리가 붙습니다.

## 연산은 다시 쓸 수 있지만, 문맥과 지식은 쌓입니다

지금까지의 흐름을 한 문장으로 줄이면 이렇습니다. 에이전트 인프라는 같은 연산을 두 번 하지 않으려고 기억을 늘립니다.

언어 모델은 긴 문맥을 읽을 때 중간 계산 결과를 만듭니다. 이것을 KV 캐시라고 부릅니다. 캐시를 보관해 두면 같은 문맥을 다시 읽을 때 처음부터 계산하지 않아도 됩니다. 글머리의 가격표에서 캐시된 문맥이 정가의 20분의 1인 이유가 여기에 있습니다.

캐시는 작지 않습니다. IBM은 6월에 발행한 기술 문서에서 요청 하나의 KV 캐시를 중형 모델에서 약 3~10GB, 대형 모델에서 40~80GB로 추정했습니다. 캐시를 재사용하면 13만 토큰 입력에서 첫 응답까지의 시간이 56분의 1로 줄었다고 보고했습니다. 한 회사의 자체 측정입니다.[^ibm-kv]

NVIDIA는 이 캐시를 보관할 계층을 새로 정의했습니다. GPU 안의 HBM, 서버의 메모리, 서버 안의 SSD 아래에 이더넷으로 연결된 플래시 저장 계층을 두고 CMX라는 이름을 붙였습니다. 캐시를 어느 계층에 둘지 정하는 소프트웨어도 함께 내놨습니다.[^nvda-cmx][^nvda-dynamo]

메모리 회사들의 실적 발표에도 같은 말이 등장합니다. Micron은 9월 30일 발표에서 데이터센터 SSD 매출이 분기에 100억 달러에 가까웠고 1년 전의 10배를 넘었다고 밝혔습니다. 그 이유의 하나로 KV 캐시를 내려 보관하는 문맥 저장을 꼽았습니다.[^mu-remarks]

SK하이닉스는 7월 실적 발표에서 기업용 SSD 매출이 전 분기의 두 배가 됐다고 밝혔고, 새 용도로 KV 캐시 보관과 GPU 가까이에 두는 저장장치를 들었습니다. 삼성전자는 서버 SSD가 2026년 낸드 매출의 60%를 넘을 것으로 예상했습니다. 두 발언은 콜 전사본을 재게시한 매체로 확인했습니다.[^skh-call][^sec-call]

하드디스크 회사 Western Digital의 최고경영자는 8월에 이 차이를 이렇게 표현했습니다. 연산 주기는 다시 쓸 수 있지만 데이터는 복리로 쌓인다는 것입니다. 에이전트는 단계마다 기록을 남기고, 그 기록은 다음 작업의 재료가 됩니다.[^wdc-call]

다만 증가율과 금액은 나눠서 봐야 합니다. 개인 에이전트 한 사람의 기억은 용량으로 보면 크지 않습니다. 금액을 키우는 것은 추론 서비스 전체가 캐시를 플래시에 내려 보관하는 설계로 바뀌는지입니다. 이 전환은 아직 초기입니다.

## 메모리는 규격품에서 로직을 품은 제품으로 바뀌고 있습니다

쌓이는 데이터가 많아지면 고객이 메모리에 요구하는 것이 달라집니다. 용량만 묻던 고객이 제때 꺼낼 수 있는지, 전력을 얼마나 쓰는지, 자기 칩과 얼마나 잘 맞는지를 묻습니다. 그 요구에 답하려면 메모리 안에 로직이 들어가야 합니다.

SK하이닉스는 7월 미국 상장 투자설명서에 이 변화를 직접 적었습니다. 과거 메모리 회사는 범용 부품을 공급했지만 AI 시대의 메모리는 성능 최적화에 핵심 역할을 한다고 썼고, 회사의 비전을 풀스택 AI 메모리 크리에이터로 제시했습니다. 회사의 자기 규정이며 실적으로 입증된 사실과는 구분해야 합니다.[^skh-424b4]

가장 앞선 사례는 HBM의 베이스 다이입니다. HBM은 메모리 칩을 여러 층 쌓은 제품이고, 베이스 다이는 맨 아래에서 신호와 전력을 다루는 칩입니다. 이전 세대까지는 메모리 공정으로 만들었습니다. HBM4부터는 로직 공정으로 만듭니다. 삼성전자는 자체 4나노 공정을 씁니다. SK하이닉스는 2024년에 HBM4 베이스 다이를 TSMC의 로직 공정으로 만드는 협업을 발표했습니다.[^sec-hbm4][^skh-tsmc]

다음 단계는 고객의 로직을 베이스 다이에 넣는 커스텀 HBM입니다. NVIDIA는 8월 26일 자사의 메모리 제어 회로를 HBM 베이스 다이에 넣는 NVHBM을 발표했습니다. 표준 HBM4E보다 대역폭이 30% 늘고 전력이 15% 준다는 것이 NVIDIA의 주장입니다. Micron은 9월 30일 이 제품을 NVIDIA와 함께 개발한다고 밝혔습니다.[^nvda-nvhbm][^mu-remarks]

삼성전자는 8월 반도체 학회 Hot Chips에서 그다음 단계까지 제시했습니다. 제어 회로를 옮기는 단계, 베이스 다이에 연산 소자를 넣어 프로세서의 계산 일부를 나눠 맡는 단계, 메모리를 연산 칩 위에 직접 쌓는 단계입니다. 출시 일정은 제시하지 않았습니다.[^sec-hotchips]

저장장치와 다른 메모리에서도 같은 방향의 제품이 나오고 있습니다. 다만 성숙도는 제품마다 크게 다릅니다.

| 제품 | 들어가는 로직 | 현재 단계 |
|---|---|---|
| HBM4 베이스 다이 | 로직 공정으로 만든 신호·전력 제어 | 양산, 매출 발생 |
| SOCAMM2 | 서버용 저전력 메모리 모듈 | 양산, 판매 증가 |
| 기업용 SSD | 제어칩과 펌웨어, 문맥 저장용 설계 | 양산, 매출 급증 |
| 커스텀 HBM, NVHBM | 고객의 메모리 제어 회로 | 개발, 차세대 GPU 적용 예정 |
| CXL 메모리 모듈 | 자주 쓰는 데이터를 가려내는 감시 회로 | 삼성 2026년 말 양산 목표로 보도, 지연 가능성 |
| HBF | 낸드를 연산 칩 가까이 붙이는 고대역 인터페이스 | 2026년 8월 첫 기술 규격 공개, 제품 전 |
| PIM, 연산 소자 내장 HBM | 메모리 안의 연산 회로 | 시제품과 로드맵 |

양산 단계로 적은 제품은 올해 실적 자료에서 확인됩니다. 삼성전자의 2분기 실적 자료는 파운드리 사업의 실적 요인으로 HBM 베이스 다이 수요 증가를 적었습니다. 커스텀 HBM부터 그 아래에 적은 제품은 아직 매출로 확인되지 않습니다. SK하이닉스는 HBM4E까지 기존 접합 방식을 유지한다고 밝혔고, CXL은 HBM의 대체가 아닌 보조 계층이라는 평가가 9월 업계 행사에서 나왔습니다.[^sec-ir][^skh-q2][^tf-cxl][^hbf-ocp][^sec-fms][^skh-hybrid][^tf-cxl-doubt]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/maturity.svg" alt="로직을 품은 메모리 제품을 매출 발생, 개발과 샘플, 로드맵의 세 단계로 나눈 그림"><figcaption>회사 발표와 실적 자료로 분류한 단계. 왼쪽으로 갈수록 올해 실적에서 확인되고, 오른쪽으로 갈수록 일정이 정해지지 않았습니다. 2026년 10월 5일 기준.</figcaption></figure>

따라서 메모리가 로직을 품는다는 말은 방향으로는 맞고, 범위로는 아직 좁습니다. 지금 매출로 확인되는 것은 HBM4와 서버용 모듈, 기업용 SSD입니다. 범용 DRAM과 낸드는 여전히 규격과 가격으로 경쟁합니다.

## 메모리가 컴퓨팅의 중심이 된다는 가설은 방향만 확인됐습니다

더 먼 미래의 가설은 컴퓨팅의 구조 자체가 바뀐다는 것입니다. 지금의 컴퓨터는 연산 장치가 중심이고 메모리가 데이터를 가져다줍니다. 데이터가 연산보다 빨리 늘면 데이터를 옮기는 비용이 계산하는 비용보다 커집니다. 그러면 데이터가 있는 곳에서 계산하는 편이 낫습니다.

이 방향의 시도는 여러 곳에서 나옵니다. 삼성전자의 로드맵 마지막 단계는 메모리를 연산 칩 위에 직접 쌓습니다. Qualcomm은 2027년 제품에 연산과 메모리를 3차원으로 합친 구조를 넣겠다고 밝혔습니다. SK하이닉스와 Sandisk는 낸드를 연산 칩 바로 옆에 붙이는 규격을 Google, Tenstorrent와 함께 만들었습니다.[^sec-hotchips][^qcom-hbc][^hbf-ocp]

Sandisk의 최고경영자는 8월 실적 발표에서 AI를 근본적으로 메모리 중심이고 저장 집약적인 문제라고 표현했습니다. 메모리 회사의 최고경영자가 한 말이라는 점은 감안해야 합니다.[^sndk-call]

이 가설의 판단은 분명히 해 두겠습니다. 2026년 현재 메모리 중심 컴퓨팅은 투자 근거가 아니라 선택권입니다. 독립된 성능 검증이 없고, 양산 일정이 없고, 고객의 채택도 확인되지 않았습니다. 지금의 주가를 설명하는 데 쓸 재료가 아닙니다. 다만 이 방향이 맞다면 가장 큰 수혜는 메모리, 로직 공정, 적층 기술을 함께 가진 회사에 돌아갑니다.

## 한국 메모리의 투자 논리는 이익의 크기에서 지속기간으로 옮겨갑니다

이제 한국 기업으로 옮기겠습니다. 올해 이익은 이미 큽니다. 삼성전자 반도체 부문의 2분기 영업이익은 89.2조 원으로 매출의 70%였습니다. SK하이닉스의 2분기 영업이익은 60.5조 원으로 매출의 76%였습니다.[^sec-ir][^skh-q2]

그런데 주가는 이 이익을 높게 쳐주지 않습니다. 10월 2일 종가 기준으로 삼성전자는 2026년 예상 이익의 5.85배, SK하이닉스는 5.25배에 거래됩니다. 예상 이익은 네이버 금융이 집계한 증권사 평균입니다.[^naver-sec][^naver-skh]

낮은 배수는 시장이 메모리를 여전히 경기순환 산업으로 본다는 뜻으로 읽을 수 있습니다. 지금의 이익이 공급 부족에서 나왔고, 증설이 끝나면 예전처럼 급락한다는 우려입니다. 이것은 해석이지만 근거가 있습니다. SK하이닉스 스스로 투자설명서의 위험 요인에 메모리 산업의 반복된 공급 과잉을 적었습니다.[^skh-424b4]

로직을 품은 메모리가 투자에서 중요해지는 지점이 여기입니다. 이 변화가 올해 이익을 더 키우는 것은 아닙니다. 공급이 정상화된 뒤에도 이익이 예전만큼 꺼지지 않을 이유를 만들 수 있다는 것이 핵심입니다. 그 이유는 전환 비용과 계약 구조에 있습니다.

첫째는 고객이 공급사를 바꾸기 어려워지는 것입니다. 고객의 칩에 맞춰 설계한 베이스 다이는 다른 회사의 것으로 쉽게 바꿀 수 없습니다. 설계, 검증, 인증에 드는 시간이 전환 비용이 됩니다. 실제 전환 비용의 크기와 그것이 가격에 남는지는 아직 확인되지 않은 가설입니다.

둘째는 계약의 구조입니다. Micron은 9월 30일 전략 고객 계약 26건을 체결했다고 밝혔습니다. 여러 해에 걸쳐 약속한 물량을 사지 않아도 대금을 내는 구조이고, 고객이 맡긴 재무 약정은 320억 달러이며 대부분 현금 예치금입니다. Micron은 이 가시성을 근거로 설비투자를 늘린다고 했습니다.[^mu-remarks]

한국 두 회사도 같은 방향입니다. SK하이닉스는 2분기에 약 10개 고객과 장기공급계약 협상을 마쳤다고 밝혔고, 콜에서 예치금 같은 재무적 장치가 포함됐다고 설명했습니다. 삼성전자는 생산능력의 60~70%를 장기계약으로 배정할 계획이며 5년 기본에 매년 연장하는 방식이라고 말했습니다. 계약별 가격과 취소 조건은 공개되지 않았습니다.[^skh-q2][^skh-lta][^sec-lta]

고객이 돈을 먼저 맡기고 물량을 약속하는 산업은 규격품을 현물로 사고파는 산업과 다르게 움직입니다. 다만 장기계약은 양날입니다. TrendForce는 장기계약의 가격 장치 때문에 일부 공급사의 서버 DRAM 인상폭이 시장 평균에 못 미친다고 적었습니다. 하락기의 바닥을 얻는 대신 상승기의 꼭대기를 내준 셈입니다.[^tf-memory]

## 삼성전자와 SK하이닉스는 같은 변화를 다른 자리에서 맞습니다

두 회사는 로직을 품은 메모리라는 같은 변화에서 서로 다른 강점과 약점을 갖습니다.

| 항목 | 삼성전자 | SK하이닉스 |
|---|---|---|
| 2분기 반도체 영업이익률 | 70% | 76% |
| HBM4 베이스 다이 | 자체 4나노 공정 | TSMC 공정 |
| 로직 가치의 귀속, 이 글의 분석 | 파운드리 실적으로 내부에 남을 수 있음 | 외부에 지급하는 원가 |
| 제품 폭 | HBM, 서버 모듈, SSD, 파운드리, 패키징 | HBM, 서버 모듈, SSD, HBF 규격 주도 |
| 장기계약 | 생산능력의 60~70% 배정 계획 | 약 10개 고객과 협상 완료 |
| 주주환원 | 3분기 약 30조 원 배당 계획 | 40조 원 자사주 소각 결의 |
| 2026년 예상 이익 대비 주가 | 5.85배 | 5.25배 |

SK하이닉스의 강점은 지금의 수익성과 고객 관계입니다. 영업이익률이 더 높고, 약 10개 고객과 장기공급계약 협상을 이미 마쳤습니다. 약점은 로직의 값을 밖에 낸다는 점입니다. TrendForce가 한국 매체를 인용해 전한 바로는 TSMC가 만든 HBM4 베이스 다이의 원가가 메모리 칩의 3~4배입니다. 회사가 확인한 수치는 아닙니다.[^tf-basedie]

삼성전자의 강점은 로직의 값이 회사 안에 남는 구조입니다. 삼성전자는 메모리, 로직 설계, 파운드리, 패키징을 모두 가진 유일한 회사라고 스스로 소개합니다.[^sec-fms] 약점은 그 구조가 아직 수익으로 충분히 입증되지 않았다는 점입니다. 내부에서 만든 베이스 다이의 매출을 외부 고객에게서 번 돈처럼 두 번 세면 안 됩니다. 연결 기준 원가와 현금으로 확인해야 합니다.

주주환원은 이익이 주주에게 돌아오는 경로입니다. SK하이닉스는 8월에 40조 원 규모의 자사주 취득과 전량 소각을 결의했고, 잉여현금흐름 환원 목표를 50% 이상으로 올렸습니다. 삼성전자는 3분기에 약 30조 원의 현금배당을 계획하며 10월 말 이사회에서 확정합니다. 두 건 모두 언론 보도로 확인했고 공시 원문은 대조하지 못했습니다.[^skh-return][^sec-return]

제 판단은 이렇습니다. 메모리에 로직이 들어가는 변화가 깊어질수록 구조적으로 유리한 쪽은 로직을 안에서 만드는 회사입니다. 지금의 실적과 고객 지위로 보면 앞선 쪽은 SK하이닉스입니다. 변화의 초입에서는 SK하이닉스의 실행력이, 커스텀 HBM과 그다음 단계가 본격화될수록 삼성전자의 통합 구조가 더 큰 값을 가질 가능성이 높습니다. 그 전환점은 삼성 파운드리가 만든 베이스 다이가 외부 고객의 설계를 받아 양산되는 때입니다.

## 현재 주가는 올해 이익의 절반 남짓만 남는다고 가정합니다

주가를 단순하게 보면 시장이 믿는 지속 가능한 이익에 평가배수를 곱한 값입니다. 시장이 메모리 회사에 10배를 준다고 가정하고 거꾸로 계산하면, 현재 주가가 요구하는 이익 수준이 나옵니다.

삼성전자의 10월 2일 종가는 276,000원입니다. 10배를 적용하면 주가가 요구하는 주당이익은 27,600원입니다. 2026년 예상 주당이익 47,142원의 58.5%입니다. SK하이닉스의 종가는 1,842,000원이고, 같은 계산으로 요구 주당이익은 184,200원입니다. 예상 주당이익 350,576원의 52.5%입니다.[^naver-sec][^naver-skh]

즉 현재 주가는 2026년 이익의 절반 남짓만 앞으로도 남는다는 가정과 맞습니다. 이것이 시장의 정확한 생각이라는 뜻은 아닙니다. 배수와 이익의 조합은 여러 가지입니다. 다만 질문은 분명해집니다. 로직을 품은 제품과 장기계약이 정상화된 이익을 올해의 절반보다 높게 붙들 수 있는가입니다.

아래 표는 2026년 예상 이익 중 남는 비율과 평가배수를 바꿔 본 것입니다. 괄호 안은 10월 2일 종가 대비 변화율입니다. 남는 비율과 배수는 모두 이 글의 계산 가정이며, 확률을 매기지 않았습니다. 배당은 포함하지 않았습니다.

삼성전자, 기준 주가 276,000원

| 2026년 예상 이익 중 남는 비율 | 8배 | 10배 | 12배 |
|---|---:|---:|---:|
| 40% | 151,000원 (-45.3%) | 189,000원 (-31.7%) | 226,000원 (-18.0%) |
| 55% | 207,000원 (-24.8%) | 259,000원 (-6.1%) | 311,000원 (+12.7%) |
| 70% | 264,000원 (-4.3%) | 330,000원 (+19.6%) | 396,000원 (+43.5%) |

SK하이닉스, 기준 주가 1,842,000원

| 2026년 예상 이익 중 남는 비율 | 8배 | 10배 | 12배 |
|---|---:|---:|---:|
| 40% | 1,122,000원 (-39.1%) | 1,402,000원 (-23.9%) | 1,683,000원 (-8.6%) |
| 55% | 1,543,000원 (-16.3%) | 1,928,000원 (+4.7%) | 2,314,000원 (+25.6%) |
| 70% | 1,963,000원 (+6.6%) | 2,454,000원 (+33.2%) | 2,945,000원 (+59.9%) |

표의 양쪽 끝이 논점을 보여줍니다. 이익이 40%만 남으면 배수가 12배로 올라도 주가는 지금보다 낮습니다. 좋은 산업 이야기가 이익 감소를 메워 주지 못합니다. 반대로 이익이 70% 남는다는 믿음이 생기면 배수가 그대로 10배여도 주가는 20~33% 높습니다.

SK하이닉스의 숫자에는 주의할 점이 있습니다. 2분기 순이익은 93.9조 원으로 영업이익 60.5조 원보다 컸습니다. 그 원인은 확인하지 못했습니다. 영업 외 항목에서 나온 이익이라면 연간 예상 주당이익에도 반복되지 않는 이익이 섞였을 수 있고, 그 경우 남는 비율을 더 낮게 잡아야 합니다.[^skh-q2]

재평가의 열쇠는 평가배수가 아니라 남는 이익의 비율입니다. 로직을 품은 메모리와 장기계약은 그 비율을 올릴 수 있는 재료입니다. 올리는지의 여부는 공급이 늘어나는 2027년과 2028년에 판가름 납니다.

## 가장 강한 반론은 로직의 값이 설계한 쪽으로 간다는 것입니다

이 논리에는 강한 반론이 있습니다. 가장 무거운 것부터 적습니다.

첫째는 가치의 귀속입니다. NVHBM에서 베이스 다이에 들어가는 제어 회로를 설계한 쪽은 NVIDIA입니다. NVIDIA는 여러 메모리 회사가 같은 규격을 공급한다고 밝혔습니다. Micron은 그 베이스 다이의 생산을 외부 파운드리에 맡깁니다. 이 구조에서는 설계의 값이 NVIDIA에, 제조의 값이 파운드리에 놓이고 메모리 회사는 다시 같은 규격으로 경쟁할 수 있습니다.[^nvda-nvhbm][^mu-foundry]

저장장치에서도 비슷한 일이 벌어집니다. NVIDIA의 문맥 저장 설계에서 데이터를 관리하는 연산은 SSD 안이 아니라 NVIDIA의 데이터 처리 장치에 놓입니다. 캐시를 어느 계층에 둘지 정하는 소프트웨어도 NVIDIA의 것입니다. 데이터가 쌓이는 곳과 고객이 떠나기 어려워지는 곳은 다를 수 있습니다.[^nvda-cmx][^nvda-dynamo]

이 반론이 이 글의 논리를 가장 크게 흔듭니다. 메모리에 로직이 들어가는 것과 메모리 회사가 그 로직의 주인이 되는 것은 별개입니다. 삼성전자의 통합 구조에 방점을 둔 이유도 이 반론 때문입니다. 로직을 직접 만들지 못하는 메모리 회사는 제품이 고도화될수록 오히려 더 좁은 자리에 설 수 있습니다.

둘째는 수요의 적응입니다. 메모리가 비싸지면 고객은 덜 쓰는 방법을 찾습니다. TrendForce는 9월 29일 GPU와 맞춤형 칩 업체들이 장치당 HBM 용량을 줄이는 방안을 검토하며 2027년에는 8단 구성을 우선 평가한다고 적었습니다. Google 연구진은 3월에 KV 캐시의 메모리 사용을 6분의 1 이하로 줄이는 압축 기법을 공개했습니다. Anthropic의 문서는 문맥이 길수록 정확도가 떨어진다고 적고, 오래된 대화를 요약으로 바꾸는 기능을 제공합니다.[^tf-hbm][^turboquant][^anthropic-context]

쌓이는 속도가 줄이는 기술보다 빠른지는 아직 답이 없습니다. Micron도 서버 한 대에 들어가는 메모리의 증가율이 가격 때문에 다소 낮아졌다고 인정했습니다.[^mu-remarks]

셋째는 공급과 자금입니다. TrendForce는 7월 30일 낸드의 공급이 2027년 하반기에 완화되고 가격 하락 압력이 생긴다고 전망했습니다. TrendForce 보도에 따르면 중국 CXMT의 2분기 DRAM 매출 점유율은 9.5%로 올랐습니다. 국제결제은행 총재는 9월 10일 연설에서 대형 기술기업의 설비투자가 현금흐름을 넘어서고 있다고 경고했습니다. 고객의 돈이 마르면 장기계약의 약속도 시험받습니다.[^tf-supply][^tf-china][^bis]

Micron은 정반대로 2027년과 2028년의 수급이 2026년보다 더 빡빡하다고 봅니다. 조사기관과 공급사의 전망이 갈린다는 사실 자체가 2027년을 단정하지 말아야 할 이유입니다.[^mu-remarks]

수요의 전제도 시험받습니다. 이 글의 출발점은 사람들이 에이전트에게 일을 계속 맡긴다는 것입니다. Anthropic이 2월에 공개한 자사 사용 데이터에서 한 번에 45분 넘게 이어진 작업은 상위 0.1%였습니다. 대부분의 작업은 훨씬 짧습니다. 위임이 습관으로 자리 잡지 못하거나 사용자가 권한을 맡기지 않으면 상시 컴퓨팅의 속도는 이 글의 가정보다 느려집니다.[^anthropic-autonomy]

## 다음 분기에는 가격이 아니라 남는 이익의 근거를 확인합니다

이 논리가 맞는지는 앞으로 나올 숫자에서 확인할 수 있습니다. 확인할 항목과 판단을 바꿀 조건을 적습니다.

| 확인할 것 | 논리를 지지하는 신호 | 논리를 약하게 하는 신호 |
|---|---|---|
| 3분기 실적, 10월 | HBM4와 기업용 SSD 물량 증가, 제품 구성 개선 | 이익 증가 대부분이 범용 가격 상승 |
| 장기계약 | 예치금과 최소 구매 조건의 공개, 계약 연장 | 가격 상한에 따른 이익 포기, 조건 비공개 지속 |
| 커스텀 HBM | 삼성 파운드리 베이스 다이의 외부 고객 양산 | 단일 규격으로 3사가 가격 경쟁 |
| 문맥 저장 | CMX 파트너 제품 출하, 전용 저장 서버 계약 | 압축 기술 확산, 출하 지연 |
| 2027년 공급 | 계약가 상승 지속, 고객 투자 계획 상향 | 낸드 가격 하락, HBM 탑재량 축소 |

삼성전자의 3분기 잠정실적은 10월 8일로 보도됐습니다. 에프앤가이드가 집계한 영업이익 평균은 108.1조 원입니다. SK하이닉스는 10월 말 발표가 예상되며 영업이익 평균은 77.2조 원입니다. 둘 다 10월 5일 보도 기준이며 회사의 공식 일정 공지는 확인하지 못했습니다.[^consensus]

숫자 자체보다 내용을 봐야 합니다. 영업이익이 평균을 넘어도 그 이유가 범용 가격 상승뿐이라면 이 글의 논리와는 무관합니다. 영업이익이 평균에 못 미쳐도 HBM4 물량과 장기계약의 질이 좋아졌다면 남는 이익의 근거는 오히려 늘어납니다.

판단을 내릴 조건도 적어 둡니다. 커스텀 HBM이 단일 규격으로 굳어 메모리 3사가 같은 제품으로 경쟁하고, 동시에 2027년 계약가격이 내려가기 시작하면 이 글의 논리는 한 단계 낮춰야 합니다. 그 경우 한국 메모리는 더 정교한 제품을 만들지만 여전히 순환하는 산업으로 평가받게 됩니다.

<strong>에이전트는 연산을 아끼기 위해 기억을 씁니다. 그 기억을 담는 제품에 로직이 들어가고, 일부 고객은 돈을 먼저 맡기기 시작했습니다. 한국 메모리의 재평가는 그 변화가 공급이 늘어난 뒤에도 이익을 붙드는지에 달려 있으며, 현재 주가는 아직 올해 이익의 절반 남짓만 믿고 있습니다.</strong>

## 출처와 계산의 경계

회사 발표, 공시, 조사기관 자료는 2026년 10월 5일에 대조했습니다. 콜 전사본을 재게시한 매체로 확인한 발언은 각주에 표시했습니다. 회사가 밝힌 성능 수치는 독립 검증이 아닙니다. 민감도 표의 남는 비율과 평가배수는 계산 가정이며 예측이 아닙니다. 예상 주당이익은 네이버 금융 집계값을 그대로 썼고 2027년 예상치는 확인하지 못했습니다.

[^anthropic-pricing]: [Anthropic 공식 가격표](https://platform.claude.com/docs/en/about-claude/pricing), 2026-10-05 조회. Opus 5.5 표준 입력 4달러, 배치 2달러, 고속 8달러, 캐시 읽기 0.20달러(100만 토큰당). Managed Agents 세션 요금 포함.

[^managed-agents]: [Claude Managed Agents 개요 문서](https://platform.claude.com/docs/en/managed-agents/overview), 2026-10-05 조회. 베타 제품의 문서입니다.

[^google-io]: [Google I/O 2026 순다르 피차이 기조연설 정리](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/), 2026-05. 회사 공개 수치.

[^metr]: [METR Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/), 2026-01-29. 50% 성공 기준 시간 지평.

[^openai-pricing]: [OpenAI API 가격표](https://developers.openai.com/api/docs/pricing), 2026-10-05 조회. gpt-6-astra 표준 10달러, Flex 5달러, Fast 20달러, 캐시 입력 1달러. gpt-6-luna 입력 0.10달러.

[^google-pricing]: [Gemini API 가격표](https://ai.google.dev/gemini-api/docs/pricing), 2026-10-01 갱신. Gemini 3.1 Pro Preview 표준 2달러, 배치 1달러, Priority 3.60달러, 캐시 저장 시간당 요금.

[^nvidia-slm]: [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153), NVIDIA 연구진, 2025-06-02 제출. 입장을 밝히는 논문이며 40~70%는 추정.

[^agent-skills]: [Anthropic Agent Skills 개요 문서](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), 2026-10-05 조회.

[^skyvern]: [Skyvern 블로그의 코드 재생 측정](https://www.skyvern.com/blog/asking-ai-to-build-scrapers-should-be-easy-right/), 2025-10-17 게시, 2026-08-24 갱신. 회사 자체 측정.

[^amzn-call]: [Amazon 2026년 2분기 실적 콜 전사본 재게시](https://www.investing.com/news/transcripts/earnings-call-transcript-amazon-tops-q2-2026-estimates-as-aws-growth-accelerates-93CH-4826442), 2026-07-30. 경영진 발언.

[^amd-call]: [AMD 2026년 2분기 실적 콜 전사본 재게시](https://www.fool.com/earnings/call-transcripts/2026/08/11/amd-amd-q2-2026-earnings-call-transcript/), 2026-08-04 콜. 시장 규모는 회사 전망.

[^tf-cpu]: [TrendForce 서버 CPU 가격 보도](https://www.trendforce.com/news/2026/04/22/news-server-cpu-prices-up-as-much-as-20-since-march-intel-may-raise-prices-another-8-10-in-2h26/), 2026-04-22. 대만·일본 매체 인용.

[^nvda-vera]: [NVIDIA Vera CPU 출하 발표](https://blogs.nvidia.com/blog/vera-cpu-delivery/), 2026-05-18.

[^avgo-call]: [Broadcom FY2026 3분기 실적 콜 전사본 재게시](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/), 2026-09-02 콜. 경영진 발언.

[^nvda-stx]: [NVIDIA BlueField-4 STX 저장 구조 발표](https://nvidianews.nvidia.com/news/nvidia-launches-bluefield-4-stx-storage-architecture-with-broad-industry-adoption), 2026-03-16. 성능 수치는 회사 주장.

[^ibm-kv]: [IBM Redbooks KV 캐시 기술 문서](https://www.redbooks.ibm.com/docs/MD260021/MD260021.html), 2026-06-05 발행. 회사 자체 측정과 추정.

[^nvda-cmx]: [NVIDIA CMX 제품 설명](https://www.nvidia.com/en-us/data-center/ai-storage/cmx/), 2026-10-05 조회. 게시일 미표시.

[^nvda-dynamo]: [NVIDIA Dynamo KV 캐시 계층화 문서](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/kv-cache-offloading), 2026-10-05 조회. 성능 수치는 문서에 없습니다.

[^mu-remarks]: [Micron FY2026 4분기 준비 발언](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf), 2026-09-30. 데이터센터 SSD 매출은 원문 표현으로 "nearly $10 billion". 전략 고객 계약, 예치금, NVHBM, 수급 전망을 이 문서에서 대조했습니다.

[^skh-call]: [SK하이닉스 2026년 2분기 실적 콜 전사본 재게시](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q2-2026-results-as-shares-fall-93CH-4818480), 2026-07 콜. 회사 공식 전사본이 아닙니다.

[^sec-call]: [삼성전자 2026년 2분기 실적 콜 전사본 재게시](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q2-2026-profit-as-ai-demand-surges-93CH-4822292), 2026-07 콜. 회사 공식 전사본이 아닙니다.

[^wdc-call]: [Western Digital FY2026 4분기 실적 콜 정리](https://finance.biggo.com/news/US_WDC_2026-08-05), 2026-08-05. 2차 정리 자료로 확인한 발언.

[^skh-424b4]: [SK하이닉스 미국 상장 투자설명서, SEC 424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm), 2026-07-09. 전략 절, 용어 정의의 Custom HBM, 위험 요인을 원문에서 대조했습니다.

[^sec-hbm4]: [삼성전자 HBM4 양산 출하 발표](https://news.samsungsemiconductor.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/), 2026-02-12. 공정과 성능은 회사 설명.

[^skh-tsmc]: [SK하이닉스·TSMC HBM4 협업 발표](https://www.prnewswire.com/news-releases/sk-hynix-partners-with-tsmc-to-strengthen-hbm-technological-leadership-302120755.html), 2024-04-18. 당시의 개발 방향 발표입니다.

[^tf-basedie]: [TrendForce의 SK하이닉스 HBM4E 베이스 다이 보도](https://www.trendforce.com/news/2026/08/31/news-sk-hynix-reportedly-weighs-intel-for-hbm4e-base-dies-amid-tsmc-cost-pressure-and-supply-diversification/), 2026-08-31. 한국 매체 인용, 회사 미확인.

[^nvda-nvhbm]: [NVIDIA NVHBM 발표](https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory/), 2026-08-26. 대역폭과 전력 수치는 회사 주장.

[^sec-hotchips]: [ServeTheHome의 삼성전자 Hot Chips 2026 발표 정리](https://www.servethehome.com/samsung-evolving-hbm-base-die-at-hot-chips-2026/), 2026-08-23. 로드맵은 회사 발표이며 일정은 없습니다.

[^sec-ir]: [삼성전자 2026년 2분기 실적 설명 자료](https://images.samsung.com/kdp/ir/events/2026/2026_2Q_conference_kor.pdf), 2026-07-30. 반도체 부문 매출 127.5조 원, 영업이익 89.2조 원. 파운드리 실적 요인에 HBM 베이스 다이 기재.

[^skh-q2]: [SK하이닉스 2026년 2분기 실적 발표](https://news.skhynix.com/en/q2-2026-business-results/), 2026-07-29. 매출 79.3조 원, 영업이익 60.5조 원, 순이익 93.9조 원, 장기공급계약, SOCAMM2.

[^tf-cxl]: [TrendForce의 삼성·SK하이닉스 CXL 3.2 보도](https://www.trendforce.com/news/2026/07/21/news-samsung-reportedly-targets-2026-cxl-3-2-mass-production-sk-hynix-advances-new-ai-memory-architecture/), 2026-07-21. 2차 보도.

[^hbf-ocp]: [Sandisk·SK하이닉스 HBF 첫 OCP 규격 공개](https://www.storagenewsletter.com/2026/08/05/fms-2026-sandisk-and-sk-hynix-advance-global-standardization-of-high-bandwidth-flash-with-release-of-first-ocp-technical-specification/), 2026-08-05.

[^sec-fms]: [StorageReview의 삼성전자 FMS 2026 발표 정리](https://www.storagereview.com/news/samsung-outlines-3d-memory-roadmap-for-ai-infrastructure-at-fms-2026), 2026-08-04. PIM 탑재 저전력 메모리 공개, 양산 시점 미확인.

[^skh-hybrid]: [Tom's Hardware의 SK하이닉스 Hot Chips 2026 발표 보도](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling), 2026-08-24.

[^tf-cxl-doubt]: [TrendForce의 AI Infrastructure Summit 보도](https://www.trendforce.com/news/2026/09/18/news-openai-intel-reportedly-downplay-cxl-as-hbm-replacement-citing-use-case-and-data-transfer-limits/), 2026-09-18. 2차 보도.

[^qcom-hbc]: [Qualcomm 데이터센터 로드맵 발표](https://www.qualcomm.com/news/releases/2026/06/qualcomm-unveils-comprehensive-data-center-roadmap-for-the-agent), 2026-06. 성능 수치는 회사 기준이며 독립 검증 전입니다.

[^sndk-call]: [Sandisk FY2026 4분기 실적 콜 전사본 재게시](https://www.fool.com/earnings/call-transcripts/2026/08/12/sandisk-sndk-q4-2026-earnings-call-transcript/), 2026-08-05 콜.

[^naver-sec]: [네이버 금융 삼성전자 일별 시세](https://m.stock.naver.com/api/stock/005930/price?pageSize=5&page=1)와 [연간 실적 집계](https://m.stock.naver.com/api/stock/005930/finance/annual), 2026-10-05 조회. 10-02 종가 276,000원, 2026년 예상 주당이익 47,142원.

[^naver-skh]: [네이버 금융 SK하이닉스 일별 시세](https://m.stock.naver.com/api/stock/000660/price?pageSize=5&page=1)와 [연간 실적 집계](https://m.stock.naver.com/api/stock/000660/finance/annual), 2026-10-05 조회. 10-02 종가 1,842,000원, 2026년 예상 주당이익 350,576원.

[^skh-lta]: [뉴스핌의 SK하이닉스 2분기 콜 보도](https://www.newspim.com/news/view/20260729000198), 2026-07-29. 예치금 발언은 보도로 확인.

[^sec-lta]: [디일렉의 삼성전자 2분기 콜 전문](https://www.thelec.kr/news/articleView.html?idxno=60316), 2026-07-30. 장기계약 비중과 방식은 경영진 계획.

[^tf-memory]: [TrendForce 2026년 4분기 메모리 계약가격 전망](https://www.trendforce.com/presscenter/news/20260930-13258.html), 2026-09-30. 전망이며 실현 가격이 아닙니다.

[^skh-return]: [지디넷코리아의 SK하이닉스 자사주 소각 보도](https://zdnet.co.kr/view/?no=20260819161157), 2026-08-19. 공시 원문 미대조.

[^sec-return]: [삼성전자 2026년 주주환원 발표 보도](https://v.daum.net/v/20260821172850433), 2026-08-21. 계획이며 지급된 금액이 아닙니다.

[^mu-foundry]: [디일렉의 Micron 베이스 다이 외주 보도](https://www.thelec.net/news/articleView.html?idxno=14372), 2026-10-02. Micron 준비 발언 원문에는 파운드리 이름이 없습니다.

[^tf-hbm]: [TrendForce 2027년 HBM 전망](https://www.trendforce.com/presscenter/news/20260929-13255.html), 2026-09-29. 조사기관 전망.

[^turboquant]: [Google Research TurboQuant 소개](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/), 2026-03-24. 연구 결과이며 상용 서비스 적용 범위는 확인하지 못했습니다.

[^anthropic-context]: [Anthropic 문맥 창 문서](https://platform.claude.com/docs/en/build-with-claude/context-windows)와 [컴팩션 문서](https://platform.claude.com/docs/en/build-with-claude/compaction), 2026-10-05 조회.

[^anthropic-autonomy]: [Anthropic의 에이전트 자율성 측정 연구](https://www.anthropic.com/research/measuring-agent-autonomy), 2026-02-18. 자사 사용 데이터의 99.9 백분위 값.

[^tf-supply]: [TrendForce 2026~2027년 메모리 수급 전망](https://www.trendforce.com/presscenter/news/20260730-13158.html), 2026-07-30. 조사기관 전망.

[^tf-china]: [TrendForce의 CXMT·YMTC 증설 보도](https://www.trendforce.com/news/2026/09/24/news-cxmt-ymtc-ramp-memory-capacity-but-chinas-ai-cloud-boom-could-soak-up-new-supply-through-2027/), 2026-09-24. 2차 보도.

[^bis]: [국제결제은행 총재 연설](https://www.bis.org/speeches/20260910-artificial-intelligence-growth-and-financial-stability-challenges-central-banks), 2026-09-10.

[^consensus]: [머니투데이의 3분기 실적 전망 보도](https://www.mt.co.kr/amp/stock/2026/10/05/2026100217315021825), 2026-10-05. 에프앤가이드 집계 인용.

*면책: 연구와 정보 제공을 위한 자료입니다. 종목, 배수, 시나리오는 분석 사례이며 투자 결정은 독자의 별도 검토가 필요합니다.*
