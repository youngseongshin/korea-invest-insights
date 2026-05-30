---
title: "AI 인프라 멀티플 지도: 왜 삼성전자는 싸고 삼성전기는 비싸 보이는가"
date: 2026-05-31T09:00:00+09:00
description: "GPU, HBM, CPU, MLCC, FC-BGA가 모두 같은 AI 인프라 사이클에 있어도 같은 멀티플을 받지는 않는다. 가격 결정권, LTA, 고객 lock-in, capex 부담, 피크이익 의심으로 멀티플 차이를 분해하고 삼성전자와 삼성전기를 상대가치로 연결한다."
categories: ["Market-Outlook"]
tags:
  - "AI 인프라"
  - "멀티플"
  - "HBM"
  - "GPU"
  - "CPU"
  - "MLCC"
  - "FC-BGA"
  - "삼성전자"
  - "005930"
  - "삼성전기"
  - "009150"
  - "SK하이닉스"
  - "000660"
  - "Nvidia"
  - "Broadcom"
  - "AMD"
  - "Intel"
  - "Murata"
  - "Ibiden"
  - "한국 반도체"
slug: ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31
valley_cashtags:
  - 삼성전자
  - 삼성전기
  - SK하이닉스
draft: false
---

> 후속 글 맥락
> 이 글은 [삼성전자 특별성과급·슈퍼사이클 글](/ko/post/samsung-electronics-stock-bonus-supercycle-buyback-2026-05-27/)과 [삼성전기 시총 138조원 peer premium 글](/ko/post/samsung-electro-mechanics-market-cap-murata-ibiden-premium-2026-05-28/)을 연결하는 글입니다. 앞선 글들이 각각 "삼성전자 DS 이익 duration"과 "삼성전기 MLCC·FC-BGA·Si-Cap 프리미엄"을 봤다면, 이번 글은 같은 AI 인프라 사이클 안에서 왜 서로 다른 멀티플을 받아야 하는지 정리합니다. 관련 허브는 [AI HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/), [AI 기판·PCB 허브](/ko/page/korea-ai-pcb-substrate-hub/), [한국 반도체 밸류체인 허브](/ko/page/korea-semiconductor-equipment-ip-hub/)입니다.

## TL;DR

같은 AI 인프라 사이클 안에 있어도 시장은 같은 멀티플을 주지 않습니다. 멀티플은 단순한 "AI 노출도"가 아니라 <strong>이익 지속기간, 가격 결정권, 고객 lock-in, 증설 리스크, 피크이익 의심</strong>의 함수입니다.

현재 가장 위험한 구간은 MLCC·FC-BGA 병목주를 GPU/HBM급 구조적 독점처럼 재평가하는 부분입니다. 병목은 맞지만, 모든 병목이 NVIDIA 같은 플랫폼 멀티플을 받을 수는 없습니다.

가장 강한 상대가치 아이디어는 <strong>삼성전자</strong>입니다. HBM catch-up, 메모리 가격, 파운드리 옵션을 갖고도 입력 자료의 2026-05-29~30 공개 데이터 스냅샷 기준 forward P/E 약 7.8배, P/B 약 4.4배 수준입니다. 반대로 삼성전기는 방향은 맞지만 가격이 이미 여러 해의 성공을 요구합니다. ([Yahoo Finance][1])

---

## 1. 핵심 산식

AI 인프라 멀티플 차이는 "누가 같은 수요 사이클에 노출되어 있는가"가 아니라, <strong>누가 초과이익을 더 오래, 더 적은 재투자로, 더 확실한 계약 구조 아래 가져가는가</strong>의 차이입니다.

```text
Multiple Premium
= 가격 결정권 × 수요 지속성 × 고객 lock-in × FCF 전환율

Multiple Discount
= 증설 capex 부담 × 공급 과잉 가능성 × 피크이익 의심 × 고객 집중 리스크
```

이 산식으로 보면 GPU, HBM, CPU, MLCC, FC-BGA는 모두 AI capex 사이클 안에 있지만 서로 다른 자산입니다.

| 레이어 | 멀티플을 올리는 요인 | 멀티플을 누르는 요인 | 핵심 질문 |
|---|---|---|---|
| GPU / 플랫폼 | CUDA, rack-scale system, software lock-in, asset-light 구조 | custom ASIC, 중국 규제, hyperscaler bargaining power | 고객이 시간을 사는가, 칩을 사는가 |
| HBM / 메모리 | HBM4, sold-out, LTA, GPU당 탑재량 증가 | 메모리 피크이익 의심, capex, 공급 다변화 | 이익이 사이클인가, 계약 기반 franchise인가 |
| CPU | AI 서버 attach 증가, orchestration 수요 | 대체 가능성, ARM/custom CPU, 낮은 scarcity | primary bottleneck인가, 필수 보조재인가 |
| FC-BGA | 대면적·고다층 기판, 고객 인증, 긴 리드타임 | capex-heavy, 감가상각, ABF 과잉 기억 | capex가 LTA/선급금으로 underwritten 되는가 |
| MLCC / Si-Cap | 전력무결성 병목, 고신뢰 제품, 작은 BOM이라 가격 저항 낮음 | AI 매출 순도 부족, 범용 MLCC 사이클, 경쟁 공급 | shipment blocker인가, 단순 수동부품인가 |

---

## 2. GPU: 최고 멀티플을 받는 이유

GPU는 단순 반도체 부품이 아닙니다. NVIDIA는 GPU, networking, rack-scale system, CUDA, software stack, reference architecture를 함께 지배합니다. 고객은 칩 하나를 사는 것이 아니라 AI factory 구축 시간을 삽니다.

NVIDIA FY2027 1분기 매출은 816억 달러, 데이터센터 매출은 752억 달러였고, 다음 분기 매출 가이던스는 910억 달러입니다. 이 정도 성장률과 gross margin 구조라면, 시가총액이 크다는 사실만으로 "과열"이라고 보기 어렵습니다. ([NVIDIA Investor Relations][2])

GPU 멀티플의 본질은 다음입니다.

| 항목 | 해석 |
|---|---|
| P | GPU·랙·시스템 단위 ASP를 유지하거나 올릴 수 있음 |
| Q | AI 데이터센터 capex가 accelerator 수요로 직접 연결 |
| C | fabless 구조와 플랫폼 프리미엄으로 capex 부담이 공급망에 분산 |

Red Team도 있습니다. hyperscaler custom ASIC, 전력·부지·냉각 병목, 중국 수출 규제, 고객 bargaining power가 모두 리스크입니다. Broadcom의 AI 매출도 Q1 84억 달러, Q2 AI semiconductor revenue 가이던스 107억 달러로 빠르게 커지고 있습니다. ([Broadcom Inc.][3])

그래도 GPU 플랫폼은 여전히 AI 인프라에서 가장 높은 quality multiple을 받을 수 있는 레이어입니다. 이유는 "GPU라서"가 아니라 <strong>AI factory operating system을 장악하기 때문</strong>입니다.

---

## 3. HBM: 이익은 뜨겁지만 피크이익 의심을 받는 이유

HBM은 GPU와 custom ASIC의 성능을 결정하는 메모리 대역폭 병목입니다. HBM 없이는 GPU도 제대로 출하되지 않습니다. 그런데도 SK하이닉스·Micron 같은 HBM 기업의 forward P/E는 NVIDIA나 Broadcom보다 낮게 보입니다.

이것은 수요가 약해서가 아닙니다. 시장이 HBM 이익을 아직 "구조적 이익"으로 완전히 인정하지 않고, 여전히 메모리 사이클의 피크이익으로 할인하기 때문입니다.

| 항목 | 해석 |
|---|---|
| P | HBM ASP는 범용 DRAM 대비 강한 프리미엄 |
| Q | GPU·ASIC당 HBM 탑재량, stack 수, HBM4/HBM4E 전환이 성장축 |
| C | TSV, stacking, packaging, yield, wafer allocation 부담이 큼 |

HBM의 핵심은 LTA입니다. 전통 DRAM은 spot 가격과 재고 사이클에 노출됐지만, HBM은 고객별 qualification, allocation, 장기 계약, 가격·물량 확정 구조가 강해지고 있습니다. LTA가 강할수록 시장은 HBM을 단순 commodity DRAM이 아니라 <strong>계약 기반 high-value memory franchise</strong>로 볼 수 있습니다.

다만 P/B를 같이 봐야 합니다. 입력 자료 기준 SK하이닉스와 Micron의 forward P/E는 낮지만 P/B는 이미 상당히 높습니다. 이것은 "싸다"와 "피크이익 의심이 크다"가 동시에 존재하는 상태입니다. ([Yahoo Finance][4], [Yahoo Finance][5])

---

## 4. CPU: 필수지만 primary choke point는 아니다

CPU는 AI 서버에 필수입니다. host CPU, orchestration, storage/network control, preprocessing, inference serving에 필요합니다. AMD의 Q1 데이터센터 매출도 58억 달러로 전년 대비 57% 증가했습니다. ([Advanced Micro Devices, Inc.][6])

하지만 AI 인프라 투자에서 primary bottleneck은 GPU, HBM, networking, advanced packaging 쪽에 더 가깝습니다. CPU는 필요하지만 대체 가능성이 큽니다. x86, ARM, hyperscaler internal CPU, NVIDIA Vera CPU, Intel Xeon, AMD EPYC 사이에서 고객 선택권이 있습니다.

그래서 CPU 멀티플은 조심해야 합니다.

| 회사 | 해석 |
|---|---|
| AMD | 서버 CPU 점유율 상승은 사실이나, 높은 forward P/E는 EPYC share gain과 Instinct GPU ramp를 동시에 요구 |
| Intel | 턴어라운드 옵션은 있으나, foundry·공정·AI accelerator 중 최소 하나의 실행 증거가 필요 |

CPU는 AI 사이클의 수혜를 받지만, standalone CPU thesis는 GPU/HBM/FC-BGA/MLCC보다 알파 강도가 낮습니다.

---

## 5. FC-BGA와 MLCC: 맞는 테마지만 현재 가격은 병목을 독점으로 오인할 수 있다

삼성전기, Murata, Ibiden이 부각되는 이유는 분명합니다. AI accelerator, server CPU, networking ASIC이 커질수록 대형·고다층 FC-BGA와 고신뢰 MLCC 수요가 늘어납니다. AI 서버는 전력 피크가 커지고, 전압 마진은 줄어들며, 순간 전압강하를 잡는 전력무결성 부품의 가치가 올라갑니다.

삼성전기는 Q1 2026 매출 3.209조원, 영업이익 2,806억원을 기록했고, AI 서버용 MLCC와 AI accelerator/server CPU용 FC-BGA 공급 증가를 실적 개선 요인으로 제시했습니다. ([Samsung Electro-Mechanics][7])

또한 삼성전기는 글로벌 대형 기업과 약 1.5조원 규모의 실리콘 커패시터 공급계약을 체결했습니다. 계약 기간은 2027년 1월 1일부터 2028년 12월 31일까지입니다. ([Samsung Electro-Mechanics][8])

이것은 강한 팩트입니다. 문제는 가격입니다.

| 레이어 | 왜 병목인가 | 왜 GPU/HBM 멀티플과 같을 수 없는가 |
|---|---|---|
| FC-BGA | 칩이 커질수록 면적·층수·신호무결성 난이도 상승 | capex-heavy, 감가상각 부담, ABF 과잉 기억 |
| MLCC | 작은 부품이지만 전력 안정화 실패 시 서버 출하 차질 가능 | 범용 MLCC 사이클과 섞이고, AI 매출 순도가 낮음 |
| Si-Cap | AI GPU·HBM 패키지 내부 die-near PDN 부품 | 고객·마진·수율·반복 수주가 아직 대부분 미공개 |

ResearchAndMarkets는 글로벌 FC-BGA 시장이 2026년 24.6억 달러에서 2032년 37.4억 달러로 증가하고, CAGR 7.1%를 기록할 것으로 제시합니다. 이 시장 성장률만으로 일부 FC-BGA 주식의 100배 P/E를 장기 정당화하기는 어렵습니다. ([Research and Markets][9])

따라서 MLCC·FC-BGA thesis의 결론은 "틀렸다"가 아닙니다. 정확히는 <strong>방향은 맞지만, 가격은 LTA·선급금·마진·AI 매출 순도 확인을 요구한다</strong>입니다.

---

## 6. 삼성전자 vs 삼성전기: 같은 AI 사이클, 다른 가격

### 삼성전자: 메모리 사이클주가 아니라 AI memory hierarchy option

삼성전자의 상대가치가 가장 흥미로운 이유는 HBM 순도만이 아닙니다. 삼성전자는 HBM4E catch-up, DDR5, SOCAMM2, eSSD/KV-cache storage, 파운드리 option을 동시에 갖습니다. [NVIDIA Vera Rubin 추론 스택 글](/ko/post/nvidia-vera-rubin-lpx-cmx-inference-stack-samsung-hbm-2026-05-28/)에서 정리했듯, AI 추론은 HBM만이 아니라 SRAM, eSSD, KV-cache, networking이 결합된 memory hierarchy 문제로 바뀌고 있습니다.

입력 자료 기준 삼성전자는 forward P/E 약 7.8배, P/B 약 4.4배입니다. SK하이닉스보다 HBM 순도는 낮지만, valuation gap과 HBM catch-up option 때문에 risk/reward가 더 좋습니다. ([Yahoo Finance][1])

삼성전자 thesis의 핵심 체크포인트는 다음입니다.

| 체크포인트 | 의미 |
|---|---|
| HBM4E qualification | SK하이닉스와의 valuation gap 축소 조건 |
| DDR5·server DRAM 가격 | 범용 메모리 supercycle duration 확인 |
| eSSD/KV-cache | AI inference memory hierarchy 노출 |
| Samsung Foundry | custom ASIC option이 살아나는지 확인 |

### 삼성전기: thesis는 맞지만 가격이 먼저 갔다

삼성전기는 MLCC + FC-BGA + Si-Cap을 동시에 가진 희소한 한국 부품사입니다. [삼성전기 Si-Cap과 EMIB-T 글](/ko/post/samsung-electro-mechanics-silicon-capacitor-emib-t-ai-package-pdn-2026-05-28/)과 [시총 138조원 peer premium 글](/ko/post/samsung-electro-mechanics-market-cap-murata-ibiden-premium-2026-05-28/)에서 본 것처럼, 삼성전기는 AI 패키지 전력무결성 supplier로 재분류될 수 있습니다.

하지만 재분류 가능성과 현재 주가의 매력은 다릅니다. 입력 자료 기준 삼성전기는 TTM P/E 약 195배, forward P/E 100배 이상, P/B 약 16배 구간입니다. 이 가격은 "좋은 회사"가 아니라 <strong>반복 수주, 고마진, 2027~2028년 이익 레벨업이 모두 확인되는 회사</strong>를 요구합니다.

삼성전기에서 지금 봐야 할 것은 스토리가 아니라 숫자입니다.

| 필요 증거 | 왜 중요한가 |
|---|---|
| 추가 Si-Cap 고객 | 단일 대형 계약인지, 플랫폼화인지 구분 |
| Si-Cap margin | 고부가 thesis 검증 |
| AI 서버용 MLCC ASP | 범용 MLCC와 차별화 확인 |
| FC-BGA 가동률·OPM | capex-heavy 리스크 흡수 여부 |
| LTA/선급금 | capex 회수 확실성 확인 |

---

## 7. 실전 판단

| 구분 | 판단 | 이유 |
|---|---|---|
| Samsung Electronics | Under / Buy now 후보 | HBM catch-up + 범용 메모리 가격 + 파운드리 option 대비 멀티플 낮음 |
| NVIDIA | 상대적 Fair~Under | forward P/E는 높지 않지만, 시총·규제·custom ASIC 리스크 때문에 position sizing 필요 |
| SK hynix | Fundamental Under, Tactical Wait | HBM pure alpha는 강하지만 P/B와 단기 급등 부담 |
| Micron | Fair~Under, 변동성 큼 | HBM·DRAM cycle upside와 P/B re-rating이 동시에 존재 |
| Broadcom | Fair~소폭 Over | AI ASIC visibility는 강하나 이미 높은 valuation |
| AMD | Over | CPU share gain만으로는 높은 멀티플 방어 어려움 |
| Intel | Over / Avoid | 턴어라운드 기대가 실행 증거보다 먼저 감 |
| Samsung Electro-Mechanics | Over / Avoid chasing | thesis는 맞지만 가격이 반복 수주와 고마진을 선반영 |
| Murata / Ibiden | Over | AI passive/substrate 병목은 맞지만 멀티플이 이미 독점 수준 |

결론은 단순합니다.

> 이 사이클에서 가장 위험한 실수는 "NVIDIA 공급망에 들어갔다"는 이유만으로 모든 부품주에 플랫폼 멀티플을 주는 것입니다.

GPU, HBM, MLCC, FC-BGA는 모두 중요합니다. 그러나 margin capture 구조는 다릅니다. 현재 가격 기준으로는 삼성전자와 NVIDIA는 아직 논리적 매수 근거가 있고, SK하이닉스·Micron은 구조적으로 싸지만 진입 타이밍이 문제입니다. 반대로 삼성전기, Murata, Ibiden은 좋은 회사일 수 있으나 현재 주식은 좋지 않을 수 있습니다. 가격이 이미 완벽한 실행을 요구합니다.

---

## 8. 근거 구분

### [Fact]

- NVIDIA FY2027 1분기 매출은 816억 달러, 데이터센터 매출은 752억 달러, Q2 매출 가이던스는 910억 달러입니다. ([NVIDIA Investor Relations][2])
- Broadcom Q1 AI revenue는 84억 달러, 전년 대비 106% 증가했고, Q2 AI semiconductor revenue 가이던스는 107억 달러입니다. ([Broadcom Inc.][3])
- AMD Q1 2026 데이터센터 매출은 58억 달러, 전년 대비 57% 증가했습니다. ([Advanced Micro Devices, Inc.][6])
- 삼성전기 Q1 2026 매출은 3.209조원, 영업이익은 2,806억원이며, AI 서버용 MLCC와 AI accelerator/server CPU용 FC-BGA 공급 증가를 실적 개선 요인으로 제시했습니다. ([Samsung Electro-Mechanics][7])
- 삼성전기는 약 1.5조원 규모 silicon capacitor 공급계약을 체결했고, 계약기간은 2027년 1월 1일부터 2028년 12월 31일까지입니다. ([Samsung Electro-Mechanics][8])

### [Inference]

- NVIDIA는 GPU supplier라기보다 AI factory platform owner에 가까워 일반 반도체 부품주보다 높은 멀티플을 받을 수 있습니다.
- HBM 업체의 낮은 forward P/E는 수요 부진이 아니라 메모리 업황 피크아웃 의심을 반영합니다.
- 삼성전자는 SK하이닉스보다 HBM 순도는 낮지만, valuation gap과 HBM catch-up optionality 때문에 risk/reward가 더 좋습니다.
- MLCC·FC-BGA는 병목 가치가 있으나, CUDA 같은 software/platform lock-in이 아니므로 100배 P/E를 장기 정당화하려면 반복 수주와 마진 증거가 필요합니다.

### [Speculation]

- 2027년 이후 HBM LTA가 fixed-price 또는 prepayment-backed 구조로 확대되면, SK하이닉스와 Micron은 과거 메모리 평균보다 높은 구조적 멀티플을 받을 수 있습니다.
- 삼성전자가 HBM4E 고객 qualification을 빠르게 통과하면, 2026년 하반기 핵심 alpha는 SK하이닉스보다 삼성전자가 될 수 있습니다.
- 삼성전기의 Si-Cap 사업이 두 번째·세 번째 AI ASIC 고객으로 확장되면 현재 valuation 부담 일부가 사후적으로 설명될 수 있습니다.

### [Blocked]

- NVIDIA Vera Rubin향 MLCC/FC-BGA BOM, Murata·삼성전기 납품 비율, 개별 고객별 LTA/선급금 조건, FC-BGA 공급계약의 가격 escalator 조항은 공개자료로 확인되지 않습니다.
- 삼성전기 Si-Cap의 ASP, 수량, 수율, OPM, 고객명, take-or-pay 여부는 공개되지 않았습니다.
- 입력 자료의 멀티플은 2026-05-29~30 공개 데이터 스냅샷 기준이며 실시간 시세가 아닙니다.

[1]: https://finance.yahoo.com/quote/005930.KS/key-statistics/ "Samsung Electronics Co., Ltd. (005930.KS) Valuation Measures & Financial Statistics"
[2]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx "NVIDIA Announces Financial Results for First Quarter Fiscal 2027"
[3]: https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-first-quarter-fiscal-year-2026-financial "Broadcom Inc. Announces First Quarter Fiscal Year 2026 Financial Results"
[4]: https://finance.yahoo.com/quote/000660.KS/key-statistics/ "SK hynix Inc. (000660.KS) Valuation Measures & Financial Statistics"
[5]: https://finance.yahoo.com/quote/MU/key-statistics/ "Micron Technology, Inc. (MU) Valuation Measures & Financial Statistics"
[6]: https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results "AMD Reports First Quarter 2026 Financial Results"
[7]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Announces Q1 2026 Business Performance"
[8]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
[9]: https://www.researchandmarkets.com/reports/6128754/fc-bga-market-global-forecast "FC BGA Market - Global Forecast 2026-2032"
