---
title: "마벨 트릴리언 스토리와 브로드컴 리드스루: 그렇다면 한국은?"
date: 2026-06-02T20:45:00+09:00
description: "젠슨 황의 마벨 '트릴리언 달러' 발언은 마벨이 엔비디아 GPU를 대체한다는 뜻이 아니라 custom XPU, AI networking, optical interconnect, FC-BGA, 고속 PCB, 실리콘 커패시터가 AI 인프라의 다음 병목으로 올라왔다는 신호다. 브로드컴 Q2 실적 전 체크포인트와 한국 read-through를 삼성전기, 코리아써키트, 이수페타시스 중심으로 정리한다."
categories: ["Market-Outlook"]
tags:
  - "Marvell"
  - "MRVL"
  - "Broadcom"
  - "AVGO"
  - "브로드컴"
  - "마벨"
  - "NVLink Fusion"
  - "custom XPU"
  - "AI networking"
  - "FC-BGA"
  - "고속 PCB"
  - "삼성전기"
  - "코리아써키트"
  - "이수페타시스"
  - "AI 인프라"
slug: marvell-trillion-broadcom-readthrough-korea-ai-connectivity-2026-06-02
valley_cashtags:
  - Marvell
  - Broadcom
  - 삼성전기
  - 코리아써키트
  - 이수페타시스
  - 삼성전자
  - SK하이닉스
  - 한미반도체
draft: false
---

> 📚 연결 맥락
> 이 글은 [마벨·브로드컴 실적 전 한국 반도체 병목 점검](/ko/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/), [마벨 Q1 FY2027 실적과 한국 반도체](/ko/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/), [AI 인프라 멀티플 지도](/ko/post/ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31/)의 후속편입니다. 관련 허브는 [AI 기판·PCB 허브](/ko/page/korea-ai-pcb-substrate-hub/), [한국 반도체 밸류체인 허브](/ko/page/korea-semiconductor-equipment-ip-hub/), [AI HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/)입니다.

## TL;DR

젠슨 황이 Marvell을 차기 “trillion-dollar company” 후보로 언급한 것은 “Marvell이 NVIDIA GPU를 대체한다”는 뜻이 아니다. 더 정확한 해석은 **custom XPU, AI networking, optical interconnect가 NVIDIA AI factory 안으로 흡수될 만큼 중요한 병목이 됐다**는 것이다.

Broadcom에는 **70점짜리 positive read-through**다. 긍정인 이유는 Broadcom의 핵심 사업이 custom XPU, Ethernet switching, optics, SerDes, CPO, 3.5D packaging이기 때문이다. 다만 100점이 아닌 이유는 Marvell은 NVIDIA NVLink Fusion의 직접 파트너로 부각됐고, Broadcom은 hyperscaler custom ASIC과 open Ethernet/UALink 축에 더 가까워 상대 포지션은 혼합적이기 때문이다.

한국 시장 번역은 HBM 단독이 아니다. 1차 read-through는 **FC-BGA, AI network PCB, silicon capacitor, high-speed substrate, power integrity**다. 우선순위는 다음과 같다.

| 우선순위 | 한국 종목/군 | 핵심 이유 | 판단 |
|---:|---|---|---|
| 1 | 삼성전기 | FC-BGA + MLCC + Si-Cap을 함께 가진 AI package power-integrity proxy | 구조적 핵심. 단 가격 규율 필요 |
| 2 | 코리아써키트 | Broadcom AI data-center ASIC용 FC-BGA qualification option | 고베타 옵션. 공식 고객/양산 확인 필요 |
| 3 | 이수페타시스 | AI Ethernet/switch/networking PCB beta | 테마 민감도 높음. 수주·ASP 확인 필요 |
| 4 | 삼성전자·SK하이닉스 | custom XPU 확산의 HBM/eSSD 2차 수혜 | 본류지만 이번 이벤트의 1차 병목은 아님 |
| 5 | 한미반도체 | 2.5D/advanced packaging 장비 derivative | 장비 발주·고객 다변화 확인 필요 |

한 줄 결론은 이렇다.

> Marvell의 trillion story와 Broadcom 실적 체크포인트가 동시에 가리키는 곳은 GPU/HBM 다음의 **연결성·기판·전력무결성 병목**이다. 한국에서는 삼성전기가 가장 깨끗하고, 코리아써키트와 이수페타시스가 더 높은 베타다.

---

## 1. 무슨 일이 있었나

[Fact] Reuters는 2026년 6월 2일 Computex 주간에 Jensen Huang이 Marvell CEO Matt Murphy와 함께 무대에 올라 Marvell을 차기 “trillion-dollar company” 후보로 언급했고, 이후 Marvell 주가가 미국 프리마켓에서 24% 이상 급등했다고 보도했다. Reuters는 Marvell 시가총액이 직전 종가 기준 약 1,920억 달러에 못 미쳤고, NVIDIA가 앞서 Marvell에 20억 달러를 투자한 점도 함께 언급했다. ([Reuters via Investing.com][1])

[Fact] Marvell과 NVIDIA는 2026년 3월 31일 NVLink Fusion 기반 협력을 발표했다. Marvell은 custom XPU와 NVLink Fusion 호환 scale-up networking을 제공하고, NVIDIA는 Vera CPU, ConnectX NIC, BlueField DPU, NVLink interconnect, Spectrum-X switches, rack-scale AI compute를 제공하는 구조다. ([Marvell 8-K / EX-99.1][2])

[Fact] NVIDIA의 NVLink Fusion 페이지는 이 플랫폼을 hyperscaler와 custom ASIC 설계사가 custom CPU/XPU를 NVLink scale-up interconnect 및 OCP MGX rack-scale architecture와 통합할 수 있게 하는 rack-scale AI infrastructure platform으로 설명한다. 기술 포트폴리오에는 NVIDIA GPU, Vera CPU, NVLink networking, CPO switches, ConnectX SuperNIC, BlueField DPU, Mission Control software가 포함된다. ([NVIDIA][3])

즉 이번 발언은 Marvell 단독 호재이기도 하지만, 더 큰 층위에서는 **custom silicon을 NVIDIA 생태계 밖에 놓지 않고 rack-scale architecture 안으로 끌어들이는 전략**이다.

---

## 2. Marvell “트릴리언” 스토리의 진짜 의미

Marvell의 핵심 메시지는 “AI scaling depends on connectivity”다. 회사는 Computex 2026 키노트 제목 자체를 “The Future of AI Scaling Depends on Connectivity”로 잡았고, AI 인프라가 단일 랙을 넘어 캠퍼스·지역 데이터센터 단위로 확장될수록 data movement가 더 높은 bandwidth, 더 낮은 latency, 더 낮은 power로 이뤄져야 한다고 설명했다. ([Marvell][4])

여기서 투자적으로 중요한 변화는 세 가지다.

| 변화 | 의미 | 투자 해석 |
|---|---|---|
| GPU-only에서 heterogeneous compute로 | GPU, custom XPU, CPU, DPU가 한 rack 안에서 공존 | “NVIDIA vs ASIC”이 아니라 “ASIC도 NVIDIA fabric 안으로” |
| Compute bottleneck에서 connectivity bottleneck으로 | 칩 자체보다 칩 간 연결·랙 간 연결이 중요 | Ethernet, NVLink, optics, SerDes, switch ASIC 재평가 |
| Board-level에서 package-level 병목으로 | 전력·신호·기판·패키지가 성능을 좌우 | FC-BGA, high-speed PCB, Si-Cap, MLCC 수요 확대 |

[Fact] Marvell은 FY2027 1분기 매출 24.18억 달러, 전년 대비 +28%를 기록했고, 2분기 매출 가이던스를 27.0억 달러 중간값으로 제시했다. 데이터센터 매출은 18.33억 달러로 총매출의 76%였다. ([Marvell Q1 FY2027][5])

[Inference] Marvell이 trillion story로 재평가되는 이유는 EPS 몇 센트가 아니라 **AI 데이터센터 매출의 순도와 connectivity 병목의 pure-play 성격**이다. 하지만 이것은 Marvell이 GPU를 대체한다는 뜻이 아니라, custom XPU와 networking이 NVIDIA AI factory architecture의 일부가 될 만큼 중요해졌다는 뜻이다.

---

## 3. Broadcom에는 왜 70점짜리 긍정인가

Broadcom은 이번 사건의 직접 주인공은 아니다. 그래도 read-through는 강하다. 이유는 Broadcom의 AI thesis가 정확히 다음 축에 걸려 있기 때문이다.

1. custom AI accelerator / XPU
2. AI networking
3. Ethernet switch
4. optical DSP / CPO
5. SerDes / retimer / PCIe Gen6
6. 3.5D package

[Fact] Broadcom은 FY2026 1분기 매출 193.11억 달러, 전년 대비 +29%를 기록했다. Q1 AI revenue는 84억 달러, 전년 대비 +106%였고, 회사는 Q2 AI semiconductor revenue를 107억 달러로 전망했다. Q2 전체 매출 가이던스는 220억 달러, adjusted EBITDA margin 가이던스는 약 68%다. ([Broadcom Q1 FY2026][6])

검산은 다음이다.

```text
Broadcom Q2 AI semiconductor QoQ growth
= 10.7 / 8.4 - 1
= +27.4%

Q2 AI semiconductor share of total revenue guide
= 10.7 / 22.0
= 48.6%

Q1 AI revenue share of total revenue
= 8.4 / 19.311
= 43.5%
```

[Fact] Broadcom Q2 FY2026 실적 콜은 미국 동부시간 2026년 6월 3일 17:00, 한국시간 2026년 6월 4일 06:00에 예정돼 있다. 따라서 이 글은 **실적 발표 전 체크리스트**다. ([Broadcom Q2 Event][7])

### 3.1 Broadcom 콜에서 들어야 할 5개 문장

| 체크포인트 | 강한 신호 | 한국 read-through |
|---|---|---|
| Q2 AI semiconductor | 107억 달러 상회 | custom XPU/AI ASIC 수요 확인 |
| Q3 AI guide | QoQ 증가 제시 | 2026 하반기 기판·패키지 수요 지속 |
| AI networking | Ethernet switch, optics, SerDes 강세 | 이수페타시스·코리아써키트·삼성전기 |
| Tomahawk 6 / CPO | production volume, supply constraint, lead time 언급 | high-speed PCB, FC-BGA, optical ecosystem |
| EBITDA margin | 68% 방어 | custom silicon이 저마진 수탁이 아니라는 신호 |

[Fact] Broadcom은 OFC 2026에서 3.5D XPU, 102.4T Ethernet switch with CPO, 400G/lane optical DSP, 200G/lane Ethernet retimers/AEC, PCIe Gen6 switches/retimers를 포함한 gigawatt-scale AI cluster 포트폴리오를 제시했다. ([Broadcom OFC][8])

[Fact] Broadcom의 Tomahawk 6 family switch series는 production volume shipping 상태로 발표됐고, 회사는 AI scale-out networks에서 128K-XPU network를 two switch tiers로 구성할 수 있다고 설명했다. ([Broadcom Tomahawk 6][9])

그래서 Broadcom에 대한 결론은 이렇다.

> Marvell shot-out은 Broadcom에 “카테고리 긍정”이다. 하지만 NVIDIA NVLink Fusion 내부의 직접 수혜는 Marvell 쪽이 더 선명하고, Broadcom은 hyperscaler custom ASIC + open Ethernet 생태계의 숫자로 증명해야 한다.

---

## 4. 두 회사가 함께 말하는 것: GPU/HBM 다음은 연결성

Marvell과 Broadcom을 따로 보면 경쟁 구도가 보인다. 같이 보면 병목 이동이 보인다.

| AI infra layer | 기존 시장의 초점 | 이번 이벤트가 강조한 다음 병목 |
|---|---|---|
| Compute | NVIDIA GPU | GPU + custom XPU 혼합 구조 |
| Memory | HBM | HBM + eSSD + memory attach + KV/cache hierarchy |
| Interconnect | NVLink / Ethernet | scale-up, scale-out, scale-across 연결 |
| Package | CoWoS / HBM stack | 2.5D/3.5D, FC-BGA, high-layer substrate |
| Board | server PCB | AI networking board, low-loss material, high-speed MLB |
| Power integrity | rack power | package-level Si-Cap, MLCC, PDN 부품 |

[Inference] 그래서 한국 투자자가 이번 이벤트를 “HBM 수요가 더 좋아진다”로만 읽으면 절반만 읽은 것이다. HBM은 여전히 본류다. 그러나 Marvell/Broadcom 이벤트가 새로 부각시킨 병목은 **HBM 옆에서 칩과 칩을 연결하고, 패키지 안에서 전압 흔들림을 잡고, 랙 안팎에서 데이터를 옮기는 부품**이다.

---

## 5. 한국 1순위: 삼성전기

삼성전기는 이번 read-through의 가장 깨끗한 한국 대형주다. 이유는 단순하다. Marvell/Broadcom thesis가 말하는 병목이 삼성전기의 두 핵심 제품군과 맞닿아 있다.

1. **FC-BGA**: custom XPU, switch ASIC, server CPU, network chip은 고다층·대면적·고신뢰 패키지 기판을 필요로 한다.
2. **MLCC / silicon capacitor**: AI package 전력 밀도가 올라갈수록 die-near power integrity 부품이 중요해진다.
3. **AI server/customer qualification**: 단순 소비재 부품보다 인증 장벽과 고객 lock-in이 높다.

[Fact] 삼성전기는 2026년 1분기 매출 3조 2,091억원, 영업이익 2,806억원을 기록했다. Component Solution 매출은 1조 4,085억원, 전년 대비 +16%였고, Package Solution 매출은 7,250억원, 전년 대비 +45%였다. 회사는 AI 서버/ADAS용 MLCC와 AI accelerator/server CPU용 FCBGA 공급 증가를 성장 요인으로 설명했다. ([Samsung Electro-Mechanics Q1][10])

[Fact] 삼성전기는 글로벌 대형기업과 약 1.5조원 규모 실리콘 커패시터 공급계약을 체결했다. 계약기간은 2027년 1월 1일부터 2028년 12월 31일까지다. 회사는 실리콘 커패시터가 AI 서버용 GPU·HBM 같은 고성능 반도체 패키지 내부에 탑재되어 전력 공급 안정성을 높인다고 설명했다. ([Samsung Electro-Mechanics Si-Cap][11])

따라서 삼성전기의 논리는 이제 이렇게 바뀐다.

| 과거 분류 | 이번 이벤트 이후의 더 정확한 분류 |
|---|---|
| MLCC 경기민감주 | AI server / network power-integrity supplier |
| 패키지기판 업체 | custom XPU·AI network ASIC용 FC-BGA platform |
| 스마트폰 부품주 | AI package inside component supplier |

다만 삼성전기는 이미 크게 리레이팅됐다. 그래서 결론은 “무조건 매수”가 아니다.

**다음 확인 지표**

- Package Solution 매출 성장률과 OPM
- AI accelerator / network application 기판 mix
- Si-Cap 양산 수율과 고객 다변화
- 추가 장기공급계약 여부
- 2027~2029년 이익 지속성이 메모리보다 길다는 증거

관련해서는 [삼성전기 Si-Cap과 인텔 EMIB-T](/ko/post/samsung-electro-mechanics-silicon-capacitor-emib-t-ai-package-pdn-2026-05-28/)와 [삼성전기 280만원 리포트 후속](/ko/post/samsung-electro-mechanics-mirae-tp-2800000-2029-memory-duration-proof-2026-06-01/)에서 더 자세히 다뤘다.

---

## 6. 한국 고베타 옵션: 코리아써키트

코리아써키트는 삼성전기보다 규모와 확신도는 낮지만, Broadcom surprise에 대한 베타는 더 클 수 있다.

[Inference] 사용자 제공 SK증권 리서치 기준으로 코리아써키트는 Broadcom향 통신용 FC-BGA 공급 경험이 있고, 2026년 상반기 AI data center ASIC용 FC-BGA qualification test, 2026년 하반기 소량 공급, 2027년 본격 효과 가능성이 언급됐다. P3 FC-BGA 전용공장 가동률도 핵심 변수다.

여기서 중요한 경계가 있다.

| 항목 | 현재 상태 |
|---|---|
| Broadcom 관련 통신용 FC-BGA 경험 | 리서치 기반 추정/보도 영역 |
| AI data-center ASIC qualification | 공식 공시로 확인 전까지 [Inference] |
| 2026년 하반기 소량 공급 | [Speculation]에 가까움 |
| 2027년 본격 실적 기여 | 확인 필요 |

따라서 코리아써키트는 “확정 수혜주”가 아니라 **Broadcom AI DC FC-BGA option**이다. Broadcom 콜에서 custom XPU와 AI networking이 동시에 강하고, 이후 코리아써키트의 고객 인증·P3 가동률·수주가 확인되면 리레이팅 여지가 생긴다.

반대로 Broadcom 숫자가 좋아도 한국 업체로의 pass-through가 공시·실적으로 확인되지 않으면, 단기 주가는 테마성으로 끝날 수 있다.

---

## 7. 한국 네트워크 PCB 베타: 이수페타시스

이수페타시스는 이번 이벤트에서 가장 “테마 반응”이 빠를 수 있는 이름이다. 이유는 Broadcom/Marvell 이벤트의 언어가 AI Ethernet, switch ASIC, optical interconnect, 800G/1.6T, CPO/NPO 같은 네트워크 키워드로 구성돼 있기 때문이다.

하지만 투자 논리는 삼성전기와 다르다.

| 구분 | 삼성전기 | 이수페타시스 |
|---|---|---|
| 핵심 노출 | FC-BGA + MLCC + Si-Cap | AI networking PCB / MLB |
| 확신도 | 상대적으로 높음 | 고객·제품 mix 확인 필요 |
| 주가 성격 | 구조주 + valuation discipline | 테마 beta + 실적 확인 |
| 확인 지표 | 패키지 매출/OPM/Si-Cap | 수주잔고, 고다층 MLB ASP, 고객 mix |

[Inference] Broadcom이 Tomahawk 6, AI Ethernet switch, optical DSP 수요를 강하게 말하면 이수페타시스 같은 고속 네트워크 PCB 기업에는 긍정적이다. 다만 “Broadcom이 좋다 → 모든 PCB가 좋다”는 결론은 틀릴 수 있다. 고속 신호용 저손실 소재, 고다층 수율, 고객 인증, ASP 상승이 같이 확인돼야 한다.

---

## 8. HBM과 한미반도체는 왜 2차인가

이번 이벤트가 HBM에 나쁘다는 뜻은 전혀 아니다. 오히려 custom XPU가 늘면 HBM 고객 기반은 NVIDIA GPU 단일 구조에서 hyperscaler custom accelerator로 넓어진다.

다만 **Marvell/Broadcom 이벤트의 1차 신호는 HBM이 아니라 connectivity**다.

| 레이어 | 이번 이벤트의 직접성 |
|---|---|
| custom XPU / AI networking | 매우 높음 |
| FC-BGA / high-speed substrate | 높음 |
| Si-Cap / MLCC / power integrity | 높음 |
| HBM / eSSD | 중간, 2차 수혜 |
| TC bonder / advanced package equipment | 중간, 장비 발주 확인 필요 |

한미반도체는 좋은 후행 옵션이다. 특히 회사가 최근 IR에서 HBM용 TC본더에서 2.5D package, AI 시스템반도체, OSAT, HBF로 TAM을 확장하겠다는 메시지를 제시한 것은 Broadcom/Marvell custom XPU 확산과 방향이 맞다. 다만 장비주는 실제 주문, 고객명, 납기, 마진 확인 전까지 내러티브와 실적 사이의 간격이 크다. 관련 글은 [한미반도체 IR 공시와 TC본더 TAM 확장](/ko/post/hanmi-semiconductor-ir-tc-bonder-tam-expansion-watchlist-2026-06-02/)을 참고하면 된다.

---

## 9. Broadcom 콜 이후 시나리오

### Bull case

조건:

1. Q2 AI semiconductor revenue가 107억 달러 이상
2. Q3도 QoQ 성장 가이던스
3. AI networking, Tomahawk 6, optical DSP, CPO 관련 강한 언급
4. custom XPU 고객 또는 2027 visibility 확대
5. adjusted EBITDA margin 68% 방어

해석:

- 삼성전기는 구조주로 재확인
- 코리아써키트는 Broadcom FC-BGA option으로 부각 가능
- 이수페타시스는 AI networking PCB beta로 반응 가능
- HBM과 한미반도체는 2차 확산

### Base case

조건:

1. Q2 AI semiconductor revenue가 107억 달러 부근
2. Q3 성장이나 가속은 제한적
3. networking은 긍정적이나 공급제약 언급은 약함
4. margin 안정

해석:

- 삼성전기 중심의 quality exposure 유지
- 코리아써키트·이수페타시스는 이벤트성 추격보다 실적 확인
- HBM 대형주는 기존 thesis 유지

### Bear case

조건:

1. Q2 AI semiconductor가 107억 달러 미달
2. Q3 가이던스 둔화
3. custom XPU 고객 ramp 지연
4. AI mix로 margin 훼손
5. networking보다 재고/고객 일정 이슈 부각

해석:

- 국내 고베타 기판주는 먼저 조정 가능
- 삼성전기만 장기 구조주로 남고 valuation discipline이 더 중요
- Broadcom/Marvell read-through trade는 보류

---

## 10. 최종 판단

이번 사건을 “Marvell 급등”으로만 보면 너무 좁다. Jensen Huang이 Marvell을 공개적으로 띄운 이유는 custom XPU와 connectivity가 NVIDIA AI factory의 바깥이 아니라 안쪽으로 들어올 만큼 중요해졌기 때문이다.

Broadcom에는 좋은 신호다. 하지만 Broadcom이 이 신호를 자기 숫자로 증명하려면 2026년 6월 3일 미국 장마감 Q2 콜에서 AI semiconductor 107억 달러, Q3 성장, AI networking/optics/CPO, EBITDA 68% 방어가 함께 나와야 한다.

한국 시장에서는 더 명확하다.

**이번 read-through의 1차 수혜 언어는 HBM이 아니라 FC-BGA, high-speed PCB, Si-Cap, MLCC, power integrity다.**

실전 우선순위는 다음이다.

| 판단 | 종목/군 | 이유 |
|---|---|---|
| Core watch | 삼성전기 | 가장 깨끗한 AI package power-integrity proxy |
| High-beta watch | 코리아써키트 | Broadcom AI DC FC-BGA option |
| Theme beta watch | 이수페타시스 | AI networking PCB beta |
| Secondary | 삼성전자·SK하이닉스 | custom XPU 확산의 HBM/eSSD 2차 수혜 |
| Derivative | 한미반도체 | advanced packaging 장비 발주 확인 필요 |

한 줄로 정리하면:

> 마벨 트릴리언 스토리는 한국에서 “HBM 더 간다”보다 “AI 인프라의 연결성·기판·전력무결성 병목이 더 비싸진다”로 읽어야 한다.

---

## 근거 분류 Appendix

### [Fact]

- Reuters는 Jensen Huang이 Marvell을 차기 “trillion-dollar company” 후보로 언급했고, Marvell 주가가 프리마켓에서 24% 이상 급등했다고 보도했다. ([Reuters via Investing.com][1])
- Marvell과 NVIDIA는 2026년 3월 31일 NVLink Fusion 기반 협력을 발표했다. Marvell은 custom XPU와 compatible scale-up networking을 제공하고 NVIDIA는 Vera CPU, ConnectX, BlueField, NVLink, Spectrum-X 등을 제공한다. ([Marvell 8-K / EX-99.1][2])
- NVIDIA NVLink Fusion은 custom CPU/XPU를 NVLink scale-up interconnect와 OCP MGX rack-scale architecture에 통합하는 플랫폼이다. ([NVIDIA][3])
- Marvell FY2027 Q1 매출은 24.18억 달러, 데이터센터 매출 비중은 76%, Q2 매출 가이던스 중간값은 27.0억 달러다. ([Marvell Q1 FY2027][5])
- Broadcom FY2026 Q1 AI revenue는 84억 달러, Q2 AI semiconductor revenue 가이던스는 107억 달러, Q2 revenue guide는 220억 달러, adjusted EBITDA margin guide는 68%다. ([Broadcom Q1 FY2026][6])
- Broadcom Q2 FY2026 실적 콜은 2026년 6월 3일 17:00 ET, 한국시간 6월 4일 06:00에 예정돼 있다. ([Broadcom Q2 Event][7])
- 삼성전기는 Q1 2026에 Component Solution 1조 4,085억원, Package Solution 7,250억원 매출을 기록했고, AI 서버용 MLCC와 AI accelerator/server CPU용 FCBGA 공급 증가를 언급했다. ([Samsung Electro-Mechanics Q1][10])
- 삼성전기는 약 1.5조원 규모 실리콘 커패시터 공급계약을 체결했고, 계약 기간은 2027년 1월 1일부터 2028년 12월 31일까지다. ([Samsung Electro-Mechanics Si-Cap][11])

### [Inference]

- Jensen Huang의 Marvell 발언은 custom XPU를 NVIDIA 생태계 밖의 경쟁축이 아니라 NVLink Fusion 안의 구성요소로 흡수하려는 전략 신호다.
- Broadcom에는 category positive read-through지만, NVIDIA ecosystem 내부 직접 수혜는 Marvell 쪽이 더 선명하다.
- 한국 1차 수혜 언어는 HBM보다 FC-BGA, high-speed PCB, Si-Cap, MLCC, power integrity다.
- 삼성전기는 가장 깨끗한 구조주, 코리아써키트는 Broadcom FC-BGA 고베타 옵션, 이수페타시스는 AI networking PCB beta로 해석할 수 있다.

### [Speculation]

- 코리아써키트가 Broadcom AI data-center ASIC용 FC-BGA qualification을 통과하고 2026년 하반기부터 의미 있는 공급을 시작한다는 주장은 공식 공시가 아니라 사용자 제공 리서치 기반 추정이다.
- Broadcom 콜 이후 국내 기판주가 즉시 리레이팅될지는 Q3 guide, 고객 ramp, networking/optics 언급 강도에 달려 있다.
- Si-Cap과 FC-BGA가 삼성전기 전사 OPM을 구조적으로 끌어올릴지는 2027년 이후 양산 수율과 고객 다변화 확인이 필요하다.

### [Blocked]

- Broadcom Q2 FY2026 실제 실적은 이 글 작성 시점인 2026년 6월 2일 20:45 KST 기준 아직 발표 전이다.
- 코리아써키트의 최종 고객명, 제품별 ASP, AI DC FC-BGA 매출 인식 시점은 공개자료만으로 확정할 수 없다.
- 이수페타시스의 Broadcom/Marvell 직접 고객 노출, 제품별 AI networking 매출 비중은 공개자료만으로 확정하기 어렵다.
- 삼성전기 Si-Cap 계약 고객명, 제품별 마진, 수율, 2029년 이후 반복계약 여부는 비공개다.

## Coverage Health

- 미국 기업 이벤트와 실적 가이던스는 공식 IR/공시와 Reuters 보도로 확인했다.
- 한국 기업 수치 중 삼성전기는 공식 보도자료로 확인했다.
- 코리아써키트·이수페타시스의 고객별 pass-through는 리서치/추론 단계로 낮은 확신도를 적용했다.
- 이 글은 투자 권유가 아니라 리서치 메모다. 실적 발표 후 Broadcom Q2 실제 숫자와 Q3 guide로 후속 업데이트가 필요하다.

[1]: https://www.investing.com/news/stock-market-news/marvell-technology-surges-after-nvidias-huang-calls-it-next-trilliondollar-company-4721040 "Marvell Technology surges after Nvidia’s Huang calls it 'next trillion-dollar company' | Reuters via Investing.com"
[2]: https://investor.marvell.com/sec-filings/all-sec-filings/content/0001193125-26-134462/d113606dex991.htm "NVIDIA AI Ecosystem Expands as Marvell Joins Forces Through NVLink Fusion | Marvell 8-K EX-99.1"
[3]: https://www.nvidia.com/en-us/data-center/nvlink-fusion/ "Build Semi-Custom AI Infrastructure | NVIDIA NVLink Fusion"
[4]: https://www.marvell.com/company/newsroom/marvell-keynote-computex-2026-future-of-scaling-ai-depends-on-connectivity.html "Marvell Keynote at COMPUTEX 2026: The Future of AI Scaling Depends on Connectivity"
[5]: https://investor.marvell.com/news-events/press-releases/detail/1023/marvell-technology-inc-reports-first-quarter-of-fiscal-year-2027-financial-results "Marvell Technology, Inc. Reports First Quarter of Fiscal Year 2027 Financial Results"
[6]: https://www.broadcom.com/company/news/financial-releases/63976 "Broadcom Inc. Announces First Quarter Fiscal Year 2026 Financial Results"
[7]: https://www.prnewswire.com/news-releases/broadcom-inc-to-announce-second-quarter-fiscal-year-2026-financial-results-on-wednesday-june-3-2026-302761260.html "Broadcom Inc. to Announce Second Quarter Fiscal Year 2026 Financial Results"
[8]: https://www.broadcom.com/company/news/product-releases/64036 "Broadcom Showcases Industry-Leading Solutions for Scaling AI Infrastructure at OFC 2026"
[9]: https://www.broadcom.com/company/news/product-releases/64031 "Broadcom Now Shipping World's First 102.4 Tbps Switch in Production Volume"
[10]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Announces Q1 2026 Business Performance"
[11]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
