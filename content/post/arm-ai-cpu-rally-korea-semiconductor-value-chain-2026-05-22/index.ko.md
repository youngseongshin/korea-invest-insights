---
title: "ARM 급등이 말하는 것 — GPU 다음 병목은 CPU 조율, 광연결, 전력무결성이다"
date: 2026-05-22T21:40:00+09:00
description: "ARM 급등의 본질은 모바일 IP 로열티 회사가 AI 데이터센터 CPU 플랫폼 회사로 재분류되는 사건이다. NVIDIA Q1 FY27 매출 816억 달러, Data Center 752억 달러, Q2 가이던스 910억 달러가 외부 촉매였고, ARM AGI CPU는 Meta를 리드 파트너로 둔 데이터센터 CPU 옵션이다. 그러나 ARM은 FY26 매출 49.2억 달러, Non-GAAP EPS 1.77달러 대비 현재 주가가 FY26 P/S 60배대, PER 160배대를 반영한다. thesis는 맞지만 주식은 싸지 않다. 더 좋은 위험보상은 Marvell의 커스텀칩·광연결, 삼성전기의 실리콘 커패시터, SK하이닉스·삼성전자의 HBM/DRAM, 고속기판·테스트 소켓에 있다."
categories: ["Market-Outlook"]
tags:
  - "ARM"
  - "Arm Holdings"
  - "Marvell"
  - "MRVL"
  - "NVIDIA"
  - "엔비디아"
  - "삼성전기"
  - "009150"
  - "삼성전자"
  - "005930"
  - "SK하이닉스"
  - "HBM"
  - "AI 인프라"
  - "반도체 밸류체인"
slug: arm-ai-cpu-rally-korea-semiconductor-value-chain-2026-05-22
valley_cashtags:
  - ARM
  - Marvell
  - NVIDIA
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - ISC
  - 리노공업
  - 티엘비
  - 코리아써키트
  - 대덕전자
draft: false
---

> 📚 관련 시리즈
> [엔비디아 Q1 FY27 이후 한국 AI 인프라](/ko/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [삼성전기 실리콘 커패시터 1.5조원](/ko/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [MLCC와 실리콘 커패시터 이해하기](/ko/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/) / [삼성전자 TSMC식 리레이팅](/ko/post/samsung-electronics-tsmc-rerating-thesis-2026-05-16/) / [엔비디아 VR200 부품 원가표 검산](/ko/post/vera-rubin-vr200-bom-memory-pcb-mlcc-korea-alpha-2026-05-21/)

*ARM 급등은 “AI 시대에는 CPU도 필요하다”는 단순한 문장이 아니다. 더 정확히는 AI 서버가 GPU 박스에서 CPU + XPU + HBM + 광연결 + 전력 안정화 + 고속기판 시스템으로 재정의되는 과정이다. ARM 자체는 이 신호의 가장 눈에 띄는 가격 반응이지만, 현재 주가에는 5년 뒤 성공 시나리오가 상당 부분 들어가 있다. 한국 투자자에게 더 중요한 알파는 ARM이 아니라, ARM 급등이 가리키는 다음 병목 — Marvell의 커스텀칩·광연결, 삼성전기의 실리콘 커패시터, SK하이닉스·삼성전자의 메모리, 고속기판과 테스트 소켓 — 에 있다.*

## 핵심 요약

ARM 급등의 본질은 **모바일 IP 로열티 회사에서 AI 데이터센터 CPU 플랫폼 회사로의 재분류**다. AI agent가 계속 실행되고, 도구를 호출하고, 데이터를 옮기고, GPU·ASIC·메모리를 조율할수록 CPU는 단순 보조칩이 아니라 AI 랙의 운영 두뇌가 된다.

외부 촉매는 NVIDIA Q1 FY27이었다. NVIDIA는 2026년 5월 20일 Q1 FY27 매출 **816억 달러**, Data Center 매출 **752억 달러**, Q2 매출 가이던스 **910억 달러 ±2%**를 제시했다. AI 인프라 수요 둔화가 아니라 가속이 확인되자, 시장은 GPU 다음 레이어인 CPU·메모리·연결·전력 부품을 다시 가격에 반영했다. ([NVIDIA][1])

ARM 자체의 논리는 강하다. FY26 매출은 **49.2억 달러**, 로열티 매출 **26.1억 달러**, 라이선스 매출 **23.1억 달러**, Non-GAAP EPS **1.77달러**였다. ARM AGI CPU는 Meta를 리드 파트너로 두고, TSMC 3nm 기반의 데이터센터 CPU 플랫폼으로 제시됐다. 회사는 FY27~FY28 고객 수요가 **20억 달러 이상**이라고 밝혔다. ([Arm][2])

문제는 가격이다. Research OS local DB 기준 ARM은 2026년 5월 21일 미국장 종가 **298.23달러**였다. FY26 Non-GAAP EPS 1.77달러 기준 PER은 약 **168.5배**다. 시가총액 3,100억 달러대와 FY26 매출 49.2억 달러를 단순 비교하면 P/S는 60배대다. thesis는 맞지만 싸지 않다.

따라서 실전 알파는 ARM 자체보다 **ARM 급등이 가리키는 다음 병목**에 있다. 우선순위는 Marvell의 커스텀칩·광연결, 삼성전기의 실리콘 커패시터, SK하이닉스·삼성전자의 HBM/DRAM, 고속기판·테스트 소켓이다.

한 줄 결론은 이렇다. **ARM 급등은 매수 신호라기보다 AI 인프라 병목 이동 신호다. GPU 다음 병목은 CPU 조율, 메모리 이동, 광연결, 전력무결성, 고속기판이다.**

---

## 1. ARM 급등의 본질 — CPU 르네상스가 아니라 병목 이동

ARM 급등을 “CPU 르네상스”로만 읽으면 절반만 맞다. 진짜 핵심은 병목의 위치가 바뀌고 있다는 점이다.

2023~2024년 AI 인프라의 병목은 GPU였다. 2025년에는 HBM과 CoWoS 같은 패키징이 병목으로 올라왔다. 2026년 이후에는 AI 랙 전체가 커지면서 CPU, 메모리 이동, 광연결, 전력 안정화, 기판, 테스트가 동시에 병목이 된다.

```text
GPU 공급 부족
→ HBM / 패키징 부족
→ CPU 조율 / 메모리 이동 / 광연결 병목
→ 패키지 내부 전력 안정화 / 고속기판 / 테스트 병목
```

AI agent는 일반 웹 요청과 다르다. 한 번 답하고 끝나는 것이 아니라, 여러 모델을 호출하고, 외부 도구를 쓰고, 문서를 읽고, 데이터베이스를 조회하고, 결과를 저장한다. 이 과정에서 GPU는 연산을 맡지만, CPU는 작업 순서, 메모리 관리, 네트워크 입출력, 보안, 오류 처리, 시스템 운영을 담당한다.

그래서 CPU는 AI 서버의 “조율 계층”이 된다. GPU가 엔진이라면 CPU는 엔진 여러 개를 실제 작업으로 묶는 관제탑이다. ARM은 이 관제탑 시장에서 전력 효율을 무기로 x86의 일부를 가져올 수 있다고 시장이 다시 가격에 반영한 것이다.

ARM의 FY26 실적도 이 내러티브를 뒷받침했다. 회사는 FY26 매출 49.2억 달러, Q4 매출 14.9억 달러를 발표했고, 로열티 매출과 라이선스 매출 모두 연간 기록을 냈다. 특히 데이터센터 로열티가 전년 대비 두 배 이상 증가했다고 밝혔다. ([Arm][2])

다만 여기서 중요한 질문은 “ARM thesis가 맞는가”가 아니라 “현재 가격에서 새 돈을 넣을 만큼 남은 위험보상이 충분한가”다.

---

## 2. ARM AGI CPU — IP 회사에서 실리콘 플랫폼 회사로

ARM은 2026년 Arm Everywhere 행사와 FY26 실적 발표를 통해 **Arm AGI CPU**를 전면에 세웠다. 회사는 이 제품을 agentic AI 데이터센터용 생산 실리콘으로 설명한다. Meta가 리드 파트너이고, 상용 시스템은 ASRock, Lenovo, Quanta, Supermicro를 통해 주문 가능하다고 밝혔다. ([Arm][2])

ARM의 기존 모델은 IP 라이선스와 로열티였다.

```text
기존 ARM
칩 설계도 제공
→ 고객사가 칩 설계·생산
→ ARM은 라이선스 수수료 + 로열티 수취
```

AGI CPU는 이 모델을 확장한다.

```text
새 ARM
IP + Compute Subsystem + 생산 실리콘
→ 고객은 더 빠르게 ARM 기반 데이터센터 CPU 도입
→ ARM은 플랫폼 주도권 확대
```

이 변화는 양면적이다.

긍정적으로 보면, ARM은 스마트폰 IP 회사에서 AI 데이터센터 CPU 플랫폼 회사로 올라간다. 데이터센터 CPU는 스마트폰 AP보다 단가와 로열티 잠재력이 크고, agentic AI에서는 CPU 코어 수요가 구조적으로 늘 수 있다.

부정적으로 보면, ARM은 기존 고객과 경쟁할 수 있다. Qualcomm, NVIDIA, Amazon, Google, Microsoft, Broadcom, Marvell 같은 고객·파트너는 ARM 아키텍처를 쓰는 동시에 자신만의 칩을 설계한다. ARM이 직접 실리콘을 팔기 시작하면, 시장은 “중립 설계도 공급자”였던 ARM이 “잠재 경쟁자”가 되는 리스크를 가격에 넣어야 한다.

이 지점에서 규제 리스크가 나온다. Bloomberg 보도 기반 기사들은 미국 FTC가 ARM의 라이선스 접근 제한 가능성을 조사하고 있다고 전했다. 핵심 쟁점은 ARM이 자체 칩 사업을 키우면서 라이선시에게 낮은 품질의 설계도만 주거나 접근을 제한할 수 있는지다. ([Bloomberg][3])

따라서 ARM AGI CPU는 장기 콜옵션이지만, 동시에 ARM의 사업 모델을 더 무겁고 복잡하게 만드는 사건이다.

---

## 3. 밸류에이션 — thesis는 맞지만 주식은 싸지 않다

ARM 급등이 불편한 이유는 숫자 때문이다. 방향은 맞다. 하지만 가격이 이미 먼 미래를 당겨왔다.

Research OS local DB 기준 ARM의 2026년 5월 21일 종가는 **298.23달러**였다. FY26 Non-GAAP EPS 1.77달러를 기준으로 계산하면:

```text
FY26 Non-GAAP PER
= 298.23 / 1.77
= 약 168.5배
```

시가총액을 3,100억 달러대, FY26 매출을 49.2억 달러로 놓으면:

```text
FY26 P/S
= 약 3,125억 달러 / 49.2억 달러
= 약 63.5배
```

이 배수는 “올해 실적이 좋다”를 사는 가격이 아니다. 시장은 **2030년 전후 데이터센터 CPU 침투율, AGI CPU 매출, 로열티율 상승, Armv9/Neoverse 확산**을 지금 가격에 반영하고 있다.

만약 ARM이 제시한 장기 시나리오처럼 FY31 매출이 250억 달러, EPS가 9달러 이상으로 올라간다면 현재 가격도 설명은 된다. 그러나 그건 5년 뒤 성공 시나리오다. 투자자는 “맞는 이야기”와 “좋은 진입 가격”을 구분해야 한다.

ARM에 대한 판단은 **Avoid at current price / Wait**다. 주식이 나쁘다는 뜻이 아니다. 급등 직후 현재 가격에서는 두 번째 10억 달러 수요에 대한 생산능력 확보, 데이터센터 로열티 가속, AGI CPU의 실제 매출 전환을 더 확인해야 한다.

---

## 4. 더 좋은 알파 1 — Marvell의 커스텀칩과 광연결

ARM이 AI 랙의 CPU 조율 계층을 말한다면, Marvell은 **커스텀칩 + 광연결 + 스위칭**을 말한다. 이쪽이 실전적으로 더 흥미롭다.

Marvell은 FY26 매출 **81.95억 달러**, Non-GAAP EPS **2.84달러**를 발표했다. FY27 매출은 110억 달러에 접근하고, 데이터센터가 성장을 이끌며, 인터커넥트 매출이 50% 이상 성장할 것으로 제시했다. ([Marvell][4])

핵심은 Marvell이 단순 네트워크 칩 회사가 아니라는 점이다.

| 축 | 의미 |
|---|---|
| 커스텀 AI 칩 | hyperscaler가 NVIDIA 외 자체 XPU를 키울 때 필요한 설계 파트너 |
| 광연결 | 랙 내부·랙 간 데이터 이동 병목을 줄이는 다음 세대 연결 |
| PCIe/CXL 스위칭 | CPU·GPU·ASIC·메모리 풀을 묶는 데이터센터 내부 연결 |
| NVLink Fusion 협력 | NVIDIA 생태계 안에서 타사 XPU를 연결하는 전략적 위치 |

Marvell은 Celestial AI 인수를 통해 Photonic Fabric, 즉 광 기반 scale-up 연결 플랫폼을 확보하려고 한다. 회사는 Celestial AI가 FY28 하반기부터 Non-GAAP 이익에 기여하고, FY29 말에는 10억 달러 연환산 매출 run-rate를 목표로 한다고 제시했다. ([Marvell Celestial][5])

또 XConn 인수를 통해 PCIe/CXL 스위칭과 UALink scale-up switch 역량을 보강하고 있다. AI 랙이 커질수록 “칩 하나”보다 “칩 사이 연결”이 더 중요해진다. 이 점에서 Marvell은 ARM 급등의 파생 알파가 될 수 있다.

다만 Marvell도 이미 많이 올랐다. Research OS local DB 기준 2026년 5월 21일 종가는 **190.69달러**였다. 현재 가격에서는 5월 27일 실적에서 FY27 매출 110억 달러 이상, 데이터센터·커스텀·광연결 수요가 재확인되어야 한다.

판단은 **Wait / Buy on pullback**이다.

---

## 5. 더 좋은 알파 2 — 삼성전기: 전력무결성 병목

한국에서 가장 선명한 2차 병목은 삼성전기다. 이유는 실리콘 커패시터 때문이다.

삼성전기는 2026년 5월 20일 글로벌 대형기업과 약 **1.5조원** 규모의 실리콘 커패시터 공급계약을 체결했다. 계약 기간은 2027년 1월 1일부터 2028년 12월 31일까지 2년이다. 회사는 실리콘 커패시터가 AI 서버용 GPU와 HBM 같은 고성능 반도체 패키지 내부에 설치되어 전원 안정성을 높인다고 설명했다. ([삼성전기][6])

이건 ARM 급등과 같은 방향의 사건이다. AI 랙이 GPU 박스가 아니라 시스템으로 바뀌면, CPU·GPU·HBM·ASIC이 서로 더 촘촘히 붙고 더 빠르게 전류를 요구한다. 이때 전압 흔들림과 노이즈를 잡는 부품이 중요해진다.

삼성전기 포인트는 “MLCC가 많이 팔린다”가 아니다. 정확한 포인트는 다음이다.

```text
기존 삼성전기
MLCC + 카메라모듈 + FC-BGA

새로운 삼성전기
AI 패키지 내부 전원 안정화 부품
+ FC-BGA
+ AI용 MLCC
```

실리콘 커패시터는 MLCC의 완전 대체재가 아니다. AI GPU·HBM 패키지 내부 또는 칩 바로 근처에서 쓰이는 고성능 보완재다. 따라서 삼성전기는 범용 수동부품 회사가 아니라 **AI 패키지 전력무결성 부품사**로 재분류될 수 있다.

Red Team도 필요하다.

| 리스크 | 의미 |
|---|---|
| 고객 비공개 | NVIDIA인지, 북미 빅테크 ASIC인지, 다른 고객인지 확정 불가 |
| 2027년부터 매출 | 2026년 손익에는 거의 기여하지 않음 |
| 마진 미공개 | ASP와 수율, 감가상각에 따라 이익 기여가 달라짐 |
| 급등 이후 진입 부담 | 좋은 이벤트와 좋은 진입 가격은 다름 |

그래서 판단은 **Watchlist → Buy on pullback**이다. 삼성전기는 ARM 급등 이후 한국에서 가장 직접적으로 “AI 랙 시스템화”를 설명할 수 있는 종목 중 하나다.

---

## 6. 더 좋은 알파 3 — SK하이닉스·삼성전자: HBM만이 아니라 CPU-side 메모리

ARM 급등은 한국 메모리에도 긍정적이다. 이유는 단순히 CPU가 늘어서가 아니다. CPU가 늘면 CPU 주변 메모리, HBM과의 데이터 이동, LPDDR·DDR·CXL 메모리 풀, 서버 DRAM 수요가 같이 커진다.

AI 랙은 다음처럼 바뀐다.

```text
GPU 중심 서버
→ GPU + CPU + DPU + NIC + Switch ASIC + HBM + DRAM
→ 랙 전체 메모리 용량과 대역폭 증가
```

SK하이닉스는 HBM과 서버 DRAM의 가장 직접적인 수혜자다. 그러나 이미 시장이 잘 아는 winner다. 방향은 맞지만 crowded trade다. 판단은 **Hold / Pullback Buy**다.

삼성전자는 다른 성격이다. HBM4 catch-up, SOCAMM2, 서버 DRAM, eSSD, HBM4 base die, Foundry optionality가 있다. ARM AGI CPU가 TSMC 3nm로 제조된다는 점 때문에 삼성파운드리 직접 수혜를 과대평가하면 안 된다. 그러나 AI 랙 다극화는 삼성전자의 메모리와 패키징·파운드리 옵션을 다시 보게 만든다.

| 구분 | SK하이닉스 | 삼성전자 |
|---|---|---|
| 투자 성격 | 검증된 HBM winner | HBM catch-up + 복합 option |
| 장점 | HBM 실행력 | HBM4, DDR, eSSD, SOCAMM, base die, Foundry |
| 단점 | 이미 crowding | 실행 할인 |
| 판단 | Hold / Pullback Buy | Watchlist / confirmation buy |

삼성전자에 필요한 것은 스토리가 아니라 확인이다. HBM4 고객 인증, 의미 있는 물량, 마진 개선, Foundry 적자 축소가 따라와야 한다.

---

## 7. 더 좋은 알파 4 — 고속기판과 테스트 소켓

AI 랙이 GPU 단품에서 시스템으로 커지면 기판과 테스트도 따라온다.

**고속기판.** CPU, GPU, ASIC, HBM, NIC, switch ASIC이 늘면 고속 신호가 지나가는 보드와 패키지 기판이 복잡해진다. 이수페타시스, 대덕전자, 티엘비, 코리아써키트, 심텍은 모두 이 흐름의 후보군이다. 다만 직접 수주, 고객 인증, ASP, 마진이 확인되지 않으면 단순 테마다.

**테스트 소켓.** 칩이 고속화되고 핀 수가 늘고 발열·전력 조건이 어려워지면 테스트 소켓과 프로브카드의 난도도 올라간다. ISC, 리노공업, 티에스이 같은 기업이 후보군이다. 이 영역은 기판보다 매출 변동성은 낮고 마진은 높을 수 있지만, 고객·제품 mix 확인이 중요하다.

| 레이어 | 후보 | 확인해야 할 것 |
|---|---|---|
| 고속기판 | 이수페타시스, 대덕전자, 티엘비, 코리아써키트, 심텍 | AI 서버향 매출, 고다층 제품, ASP, OPM |
| 테스트 소켓 | ISC, 리노공업, 티에스이 | ASIC/HBM/CXL 고객, 제품 mix, 신규 소켓 매출 |
| 패키지 기판 | 삼성전기, 대덕전자, 코리아써키트 | FC-BGA 가동률, 고객 인증, 마진 |

여기서 중요한 원칙은 하나다. **“AI향”이라는 단어만으로 사면 늦다. 실제 고객·수주·마진이 찍히는지 확인해야 한다.**

---

## 8. 실전 매매 전략

| 종목/도메인 | 판단 | 왜 |
|---|---|---|
| ARM | Avoid at current price / Wait | thesis는 맞지만 FY26 실적 대비 배수가 너무 높음 |
| Marvell | Wait / Buy on pullback | 커스텀칩 + 광연결 + 스위칭 병목의 중심. 5/27 실적 확인 필요 |
| 삼성전기 | Watchlist → Buy on pullback | 실리콘 커패시터로 AI 패키지 전력무결성 부품사 재분류 가능 |
| 삼성전자 | Watchlist | HBM4·SOCAMM·서버 DRAM·eSSD·Foundry option. 확인 필요 |
| SK하이닉스 | Hold / Pullback Buy | 가장 직접적인 HBM winner지만 이미 crowded |
| 고속기판 | Watchlist | 수혜 가능성은 크지만 고객·마진 확인 전 추격 금지 |
| 테스트 소켓 | Watchlist | 칩 복잡도 소모품 베타. 제품 mix 확인 필요 |

### Entry

- **ARM**: 급등 추격 금지. AGI CPU 실제 매출 전환, 데이터센터 로열티 가속, 규제 리스크 완화 확인 후 재평가.
- **Marvell**: 5월 27일 실적에서 FY27 매출 110억 달러 이상, 데이터센터·커스텀·광연결 수요 재확인 시. 또는 급등 후 밸류에이션 부담 완화 시.
- **삼성전기**: 실리콘 커패시터 추가 고객, 2027~2028 매출·마진 가시성, FC-BGA/AI MLCC 동반 개선 확인 시.
- **삼성전자**: HBM4 인증과 물량, 서버 DRAM 가격, Foundry 손익 개선이 같이 확인될 때.
- **기판/테스트**: AI향 매출이 실제 분기 실적에서 분리되거나, 고객 인증·장기공급계약이 확인될 때.

### Catalyst

- Marvell 2026년 5월 27일 실적.
- ARM AGI CPU 공급능력 확대 및 고객 주문 전환.
- NVIDIA Vera Rubin 하반기 램프.
- 삼성전기 실리콘 커패시터 후속 고객 또는 증설 공시.
- 삼성전자 HBM4 고객 인증.
- 고속기판·테스트 업체의 AI향 매출 분리 공시.

### Invalidation

- ARM AGI CPU가 수요는 있으나 공급·마진·고객 충돌 문제로 지연.
- FTC/규제 이슈가 ARM 라이선스 모델을 훼손.
- Marvell 커스텀칩 design win이 Broadcom으로 쏠리거나 광연결 매출화가 지연.
- 삼성전기 실리콘 커패시터 계약의 마진이 낮거나 후속 고객이 부재.
- 한국 기판·테스트 종목에서 AI 매출은 늘지만 OPM이 유지되지 않음.

---

## 9. 마지막 한 줄

ARM 급등은 맞는 방향의 재평가다. AI 서버는 GPU 박스가 아니라 CPU, XPU, HBM, 광연결, 전력 안정화, 고속기판, 테스트가 함께 움직이는 시스템이 되고 있다. 그러나 ARM 주식은 이미 5년 뒤 성공 시나리오를 상당 부분 반영했다.

따라서 이번 이벤트에서 사야 할 것은 “급등한 ARM”이 아니라 ARM이 가리키는 다음 병목이다. Marvell은 커스텀칩과 광연결, 삼성전기는 실리콘 커패시터와 패키지 전력무결성, SK하이닉스·삼성전자는 HBM과 CPU-side 메모리, 고속기판·테스트 소켓은 시스템 복잡도 증가의 2차 수혜다.

한 문장으로 정리하면 이렇다. **ARM은 신호이고, 알파는 병목에 있다.**

---

## 근거 분류

### [Fact]

- NVIDIA Q1 FY27 매출은 816억 달러, Data Center 매출은 752억 달러, Q2 가이던스는 910억 달러 ±2%였다. ([NVIDIA][1])
- ARM FY26 매출은 49.2억 달러, Q4 매출은 14.9억 달러였고, FY26 로열티 매출은 26.1억 달러, 라이선스 매출은 23.1억 달러였다. ARM은 AGI CPU 고객 수요가 FY27~FY28 20억 달러 이상이라고 밝혔다. ([Arm][2])
- Marvell FY26 매출은 81.95억 달러, Non-GAAP EPS는 2.84달러였고, 회사는 FY27 매출이 110억 달러에 접근할 것으로 제시했다. ([Marvell][4])
- 삼성전기는 2026년 5월 20일 약 1.5조원 규모 실리콘 커패시터 공급계약을 발표했고, 해당 부품이 AI 서버 GPU와 HBM 패키지 내부 전원 안정화에 쓰인다고 설명했다. ([삼성전기][6])
- Research OS local DB 기준 ARM 2026년 5월 21일 종가는 298.23달러, Marvell은 190.69달러였다.

### [Inference]

- ARM 급등은 AI 인프라 병목이 GPU에서 CPU 조율, 메모리 이동, 광연결, 전력 안정화로 이동하고 있음을 보여준다.
- ARM thesis가 맞더라도 현재 주가보다 Marvell, 삼성전기, 메모리, 고속기판·테스트 소켓이 더 나은 위험보상을 제공할 가능성이 있다.
- 한국 반도체에서는 삼성파운드리 직접 수혜보다 HBM/DRAM, 전력무결성, 기판, 테스트가 더 즉각적인 수혜 레이어다.

### [Blocked]

- ARM AGI CPU의 실제 고객별 주문 규모와 마진.
- Marvell의 고객별 커스텀칩 매출 분해.
- 삼성전기 실리콘 커패시터 고객명, 제품별 ASP, 마진율, 적용 패키지 위치.
- 국내 고속기판·테스트 업체의 특정 ARM/NVIDIA/Marvell 직접 노출.

---

*이 글은 리서치와 논평으로만 활용해야 하며 투자 조언이 아닙니다. ARM·Marvell·NVIDIA 가격 데이터는 Research OS local DB의 2026년 5월 21일 미국장 종가 기준이며, 장중·장후 가격과 다를 수 있습니다. ARM FY26 실적과 AGI CPU 관련 수치는 ARM 공식 발표 기준입니다. NVIDIA Q1 FY27 수치는 NVIDIA 공식 발표 기준입니다. Marvell FY26 및 FY27 전망은 Marvell 공식 실적자료 기준입니다. 삼성전기 실리콘 커패시터 계약은 삼성전기 공식 발표 기준입니다. 시나리오와 투자 판단은 분석가의 framework이며 보장되지 않습니다. 데이터 기준일: 2026년 5월 22일 KST.*

[1]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx "NVIDIA Announces Financial Results for First Quarter Fiscal 2027"
[2]: https://newsroom.arm.com/news/arm-q4-fye26-results "Arm delivers record-breaking quarter and full-year results"
[3]: https://www.bloomberg.com/news/articles/2026-05-15/arm-holdings-said-to-face-us-antitrust-probe-over-chip-tech "Arm Holdings Said to Face US Antitrust Probe Over Chip Tech"
[4]: https://d1io3yog0oux5.cloudfront.net/_cde1ddaaf3189b05accbc0f122d6a0c2/marvell/db/3715/35343/pdf/2026_03_05_Marvell_Q4_FY26_financial_business_results_FINAL.pdf "Marvell FY26 and Q4 FY26 Financial and Business Results"
[5]: https://d1io3yog0oux5.cloudfront.net/_a2ff1b1766821fdbdf60a17efbf050dd/marvell/files/pages/marvell/db/3831/description/2025-12_02-Marvell-to-Acquire-Celestial-AI-vF2.pdf "Marvell to Acquire Celestial AI"
[6]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract with Global Large-Scale Company"
