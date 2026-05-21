---
title: "Vera Rubin VR200 BOM 감사 — GPU가 아니라 Memory dollar content가 폭발한다"
date: 2026-05-21T12:15:00+09:00
description: "Morgan Stanley 추정으로 보도된 NVIDIA Vera Rubin VR200 랙 BOM 표를 검산하면 핵심은 GPU가 아니라 Memory dollar content의 폭발이다. GB300 대비 VR200 총 BOM 증가분 380.9만 달러 중 Memory 증가분이 162.8만 달러, 42.7%를 차지한다. GPU 증가분 144.0만 달러, 37.8%보다 크다. PCB는 +232.6%, MLCC는 +182.4%로 증가율은 화려하지만 절대 증분은 각각 전체 증가분의 2.1%, 0.1%에 그친다. 국내 우선순위는 HBM4·LPDDR5X·SOCAMM 메모리 본류, 그다음 direct qualification이 확인되는 PCB/ABF/CCL, 그리고 일반 MLCC가 아니라 silicon capacitor·power integrity다. Vera Rubin은 GPU 랙이 아니라 메모리와 데이터 이동 병목이 재가격화되는 랙이다."
categories: ["Theme-Analysis"]
tags:
  - "Vera Rubin"
  - "VR200"
  - "NVIDIA"
  - "HBM4"
  - "SOCAMM"
  - "LPDDR5X"
  - "삼성전자"
  - "SK하이닉스"
  - "삼성전기"
  - "코리아써키트"
  - "이수페타시스"
  - "AI 인프라"
slug: vera-rubin-vr200-bom-memory-pcb-mlcc-korea-alpha-2026-05-21
valley_cashtags:
  - NVIDIA
  - SK하이닉스
  - 삼성전자
  - 삼성전기
  - 코리아써키트
  - 대덕전자
  - 이수페타시스
  - 티엘비
draft: false
---

> 📚 관련 시리즈
> [엔비디아 Q1 FY27 이후 한국 AI 인프라](/ko/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [Google I/O 2026과 한국 AI 인프라](/ko/post/google-io-2026-agentic-os-korea-ai-infra-2026-05-21/) / [삼성전기 Si-Cap 1.5조원 계약](/ko/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [AI HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/) / [반도체 밸류체인 허브](/ko/page/korea-semiconductor-equipment-ip-hub/)

*Morgan Stanley 추정으로 보도된 NVIDIA Vera Rubin VR200 랙 BOM 표를 검산하면 핵심은 GPU가 아니라 Memory dollar content의 폭발이다. GB300 대비 VR200 총 BOM 증가분 380.9만 달러 중 Memory 증가분이 162.8만 달러, 42.7%를 차지한다. GPU 증가분 144.0만 달러, 37.8%보다 크다. PCB는 +232.6%, MLCC는 +182.4%로 증가율은 화려하지만 절대 증분은 각각 전체 증가분의 2.1%, 0.1%에 그친다. 국내 우선순위는 HBM4·LPDDR5X·SOCAMM 메모리 본류, 그다음 direct qualification이 확인되는 PCB/ABF/CCL, 그리고 일반 MLCC가 아니라 silicon capacitor·power integrity다. Vera Rubin은 GPU 랙이 아니라 메모리와 데이터 이동 병목이 재가격화되는 랙이다.*

---

## 핵심 요약

이 표의 핵심은 **Memory dollar content**다. VR200 총 BOM 증가분 **+$380.9만** 중 Memory 증가분은 **+$162.8만**, 전체 증가분의 <strong>42.7%</strong>다. GPU 증가분 **+$144.0만**, <strong>37.8%</strong>보다 크다. GPU가 여전히 랙 BOM의 절반 이상을 차지하지만, 증분을 움직이는 더 큰 축은 Memory다.

국내 투자 우선순위는 **HBM4·LPDDR5X·SOCAMM > PCB/ABF/CCL > silicon capacitor·power integrity > 일반 MLCC**다. 다만 이 순위는 "증가율"이 아니라 **증분 dollar content × 직접 공급 가능성 × ASP pass-through × LTA 기반 증설**을 기준으로 한 순위다.

PCB는 +232.6%, MLCC는 +182.4%로 headline 증가율이 강하다. 그러나 PCB 증가액은 Memory 증가액의 약 **5.0%**, MLCC 증가액은 Memory 증가액의 약 <strong>0.17%</strong>다. 즉 "PCB/MLCC가 Memory보다 더 큰 수혜"라는 해석은 틀리고, "작은 dollar content라도 고난도·고마진·공급 집중도가 있으면 특정 종목에는 강한 영업 레버리지가 생길 수 있다"가 맞다.

삼성전기는 이 표의 MLCC row보다 **silicon capacitor** 관점이 더 중요하다. 삼성전기의 1.5조원 규모 AI 칩 부품 계약은 일반 MLCC가 아니라 AI 패키지 내부 전력 안정화 부품이라는 새 병목을 보여준다. 따라서 삼성전기 thesis는 "MLCC +182%"가 아니라 **FC-BGA + silicon capacitor + AI용 MLCC**의 복합 exposure다.

코리아써키트·대덕전자·이수페타시스·티엘비·심텍 같은 PCB/기판주는 모두 후보군이지만, 이제부터는 단순 AI 테마가 아니라 **Rubin/SOCAMM/AI switch/FC-BGA direct qualification**을 확인해야 한다. 이미 많이 오른 종목은 "좋은 산업"과 "좋은 진입 가격"을 분리해야 한다.

---

## 1. 팩트 감사 — 신뢰도는 중

먼저 신뢰도부터 정리해야 한다. NVIDIA 공식 자료로는 Vera Rubin NVL72의 구조와 메모리 스펙이 확인된다. NVIDIA는 Vera Rubin NVL72가 **72개 Rubin GPU, 36개 Vera CPU, NVLink 6, ConnectX-9, BlueField-4**를 통합한 rack-scale platform이라고 설명한다. 공식 스펙에는 **20.7TB HBM4**와 **54TB LPDDR5X**가 제시된다. 다만 NVIDIA는 해당 수치를 preliminary, subject to change로 명시한다.

첨부 BOM 표는 Wccftech가 Morgan Stanley Research 추정치로 보도한 표와 일치한다. 그러나 원문 Morgan Stanley 리포트는 직접 확인하지 못했다. 따라서 이 글의 표는 **Morgan Stanley 원문 확인 완료**가 아니라 **사용자 제공 이미지 + Wccftech 2차 보도 기준 추정치**로 다룬다.

이 차이가 중요하다. 투자 판단에서 BOM은 방향성 자료이지 공식 원가표가 아니다. NVIDIA의 실제 판매가격, 고객별 할인, supplier allocation, gross margin은 공개되어 있지 않다. 그래서 이 표를 "정확한 계약 원가"로 보면 안 되고, **GB300에서 VR200으로 넘어갈 때 어떤 부품군의 dollar content가 커지는가**를 보는 도구로 써야 한다.

---

## 2. 숫자 검산 — 증가율보다 증분 기여도

산식은 단순하다.

```text
증가액 = VR200 BOM - GB300 BOM
증가율 = VR200 BOM / GB300 BOM - 1
총 증가액 기여도 = 항목별 증가액 / Total 증가액
```

단위는 **USD per rack**이고, 반올림은 소수점 첫째 자리 기준이다.

| 항목 | GB300 | VR200 | 증가액 | 증가율 | VR200 BOM 비중 | 총 증가액 기여도 |
|---|---:|---:|---:|---:|---:|---:|
| GPU | $2,520,000 | $3,960,000 | $1,440,000 | +57.1% | 50.7% | 37.8% |
| Memory | $373,939 | $2,001,600 | $1,627,661 | +435.3% | 25.7% | 42.7% |
| NVLink Switch chip | $64,800 | $144,000 | $79,200 | +122.2% | 1.8% | 2.1% |
| Other networking chips | $261,000 | $576,000 | $315,000 | +120.7% | 7.4% | 8.3% |
| PCB | $35,100 | $116,730 | $81,630 | +232.6% | 1.5% | 2.1% |
| ABF Substrate | $11,160 | $20,340 | $9,180 | +82.3% | 0.3% | 0.2% |
| MLCC | $1,530 | $4,320 | $2,790 | +182.4% | 0.1% | 0.1% |
| Others | $402,412 | $623,278 | $220,866 | +54.9% | 8.0% | 5.8% |
| Total | $3,994,551 | $7,803,148 | $3,808,597 | +95.3% | 100.0% | 100.0% |

가장 중요한 결론은 세 가지다.

첫째, **Memory가 GPU보다 더 큰 incremental BOM driver**다. VR200에서 GPU는 여전히 총액 기준 1위지만, GB300 대비 증가분만 보면 Memory가 더 크다.

둘째, <strong>GPU + Memory만으로 총 증가분의 80.5%</strong>가 설명된다. 이 표는 "AI 서버 부품 전반이 다 같이 오른다"보다 "GPU와 Memory가 대부분의 dollar content를 가져간다"에 가깝다.

셋째, PCB와 MLCC는 증가율 착시가 크다. PCB는 +232.6%지만 총 증가액 기여도는 2.1%다. MLCC는 +182.4%지만 총 증가액 기여도는 0.1%다. 이 숫자를 보고 PCB/MLCC 전체를 Memory와 같은 본류로 보면 안 된다.

---

## 3. Memory row를 전부 HBM으로 보면 틀린다

Memory 증가분은 이 표의 가장 중요한 line item이다. 그러나 이 row를 전부 HBM으로 해석하면 틀린다. NVIDIA 공식 스펙상 Vera Rubin NVL72는 GPU memory로 **20.7TB HBM4**를 쓰고, CPU memory로 **54TB LPDDR5X**를 쓴다.

즉 이 Memory row는 대략 다음 세 축으로 나눠 봐야 한다.

```text
HBM4
→ Rubin GPU 쪽 고대역폭 메모리
→ SK하이닉스·삼성전자·Micron의 본류 경쟁

LPDDR5X / SOCAMM
→ Vera CPU 쪽 system memory
→ 삼성전자·SK하이닉스의 LPDDR, SOCAMM2
→ 코리아써키트·티엘비 등 모듈 PCB/기판 후보군

기타 memory-adjacent content
→ storage, controller, module, board-level integration 가능성
→ 세부 supplier allocation은 미확인
```

국내 수혜의 1차 결론은 여전히 SK하이닉스와 삼성전자다. SK하이닉스는 HBM 실행력이 가장 선명하고, 삼성전자는 HBM4·LPDDR5X·SOCAMM·base die·foundry option을 함께 가진 복합 exposure다.

하지만 "Memory +435%"를 "HBM 대장주만 사면 끝"으로 읽는 것도 부족하다. Vera Rubin은 GPU만 강해지는 랙이 아니라 Vera CPU, LPDDR5X, 데이터 이동, memory hierarchy가 같이 커지는 랙이다. 그래서 SOCAMM과 LPDDR 서버 메모리 모듈까지 같이 봐야 한다.

---

## 4. PCB/ABF/CCL — 상승률은 크지만 절대액을 봐야 한다

PCB row는 투자자 눈에 가장 쉽게 들어온다. **$35,100 → $116,730**, 증가율 <strong>+232.6%</strong>다. headline만 보면 대단히 강하다.

하지만 절대액으로 보면 다르다.

```text
PCB 증가액 = $81,630/rack
Memory 증가액 = $1,627,661/rack
PCB 증가액 / Memory 증가액 = 5.0%
```

따라서 "PCB가 Memory보다 더 큰 수혜"라는 해석은 틀린다. 맞는 해석은 이렇다.

```text
PCB dollar content는 작다
→ 그러나 고다층·저손실·고속 신호·열·전력 설계 난도가 올라간다
→ 공급 가능한 업체가 제한될 수 있다
→ 직접 인증 업체에는 작은 BOM row가 큰 영업 레버리지로 바뀔 수 있다
```

국내 후보군은 삼성전기, 대덕전자, 코리아써키트, 티엘비, 심텍, 이수페타시스다. 다만 이 그룹은 가장 조심해야 한다. 시장은 이미 "AI PCB"라는 말에 빠르게 반응했고, 일부 종목은 목표가가 주가를 뒤따라 올라가는 구간에 들어갔다.

이제부터 봐야 할 것은 세 가지다.

1. **Direct qualification**: Rubin, SOCAMM, AI switch, FC-BGA, high-layer MLB에서 실제 인증이 있는가.
2. **ASP pass-through**: T-Glass, CCL, 동박 등 원재료 상승을 고객에게 전가할 수 있는가.
3. **LTA 기반 증설**: 고객 LTA 없이 선증설하는가, 아니면 고객 commitment가 있는가.

이 세 가지가 없으면 PCB는 "BOM 증가율 +233%"라는 좋은 headline만 남고, 실적은 따라오지 않을 수 있다.

---

## 5. MLCC row보다 중요한 것은 silicon capacitor

MLCC row도 비슷하다. 증가율은 <strong>+182.4%</strong>로 높다. 그러나 증가액은 **+$2,790/rack**뿐이다. 총 증가분 기여도는 0.1% 안팎이다. 이 표만 놓고 "MLCC 단독 thesis"를 세우기에는 약하다.

오히려 봐야 할 것은 **silicon capacitor**다.

삼성전기는 2026년 5월 20일 글로벌 대형기업과 약 **1.5조원 규모 silicon capacitor 공급계약**을 체결했다. 공급 기간은 2027~2028년이다. 이 부품은 AI 서버 GPU와 HBM 패키지에 사용되는 고성능 패키지 부품으로 설명된다.

silicon capacitor의 의미는 일반 MLCC와 다르다.

```text
AI GPU/HBM 패키지 전력 밀도 상승
→ 순간 전류 변동, 전압 droop, ripple/noise 관리 필요
→ 패키지 내부 또는 근접부의 low ESL/low ESR capacitor 필요
→ silicon capacitor / advanced MLCC / power integrity 부품 수요 증가
```

따라서 삼성전기 thesis는 "MLCC +182%"가 아니다. **FC-BGA + silicon capacitor + AI용 MLCC + 전력무결성 부품사 재분류**가 핵심이다. 이 부분은 NVIDIA GPU, Google TPU, Broadcom/Marvell ASIC 중 누가 이기든 공통으로 필요한 vendor-agnostic bottleneck에 가깝다.

---

## 6. 국내 레이어별 우선순위

이 표를 국내 상장사 관점으로 번역하면 다음과 같다.

| 레이어 | 국내 후보 | 확신도 | 해석 |
|---|---|---:|---|
| HBM4 / AI DRAM | SK하이닉스, 삼성전자 | High | 총 증가분 42.7%가 Memory에서 발생. 가장 직접적인 dollar-content winner |
| LPDDR5X / SOCAMM | 삼성전자, SK하이닉스, 코리아써키트, 티엘비 | Medium | Vera CPU memory 54TB LPDDR5X. HBM만 보던 시장의 추가 memory content |
| Silicon capacitor / power integrity | 삼성전기 | High | 일반 MLCC보다 AI 패키지 내부 전력 안정화 부품이 핵심. 1.5조원 계약은 proof |
| 고다층 PCB / MLB | 이수페타시스, 코리아써키트, 대덕전자, 티엘비, 심텍 | Medium | PCB 증가율은 크지만 총 증분 기여도 2.1%. direct qualification 확인 필요 |
| ABF / FC-BGA | 삼성전기, 대덕전자, 코리아써키트, 심텍 | Low~Medium | 표상 증분은 작지만 전략적 중요도는 높다. NVIDIA 최상위 GPU direct exposure는 공개자료로 확정 어려움 |
| 테스트·소켓·검사 | ISC, 리노공업, 티에스이, 인텍플러스 | Indirect | BOM에는 안 잡히지만 패키지 복잡도 상승의 2차 수혜. Rubin 직접 수혜로 단정하면 안 됨 |

가장 좋은 종목은 네 조건을 동시에 만족해야 한다.

| 조건 | 의미 | 왜 중요한가 |
|---|---|---|
| Dollar content 증가 | rack당 부품 금액이 커진다 | 매출 민감도의 출발점 |
| Direct qualification | NVIDIA/ODM/hyperscaler 인증 | 테마와 실적을 가르는 지점 |
| Capacity scarcity | 공급이 쉽게 늘지 않는다 | ASP와 마진 방어 |
| Margin leverage | 고부가 mix가 올라간다 | 매출 증가가 OP로 연결 |

이 기준으로 보면 메모리는 구조적이고, PCB는 선별적이고, 일반 MLCC는 과장되기 쉽다. 삼성전기는 MLCC가 아니라 silicon capacitor·FC-BGA를 같이 볼 때 의미가 커진다.

---

## 7. 코리아써키트와 SOCAMM 앵글

이 표에서 흥미로운 부분은 Memory row 안에 숨은 **LPDDR5X/SOCAMM**이다. 시장은 Memory +435%를 보면 자연스럽게 HBM과 SK하이닉스를 떠올린다. 그 자체는 맞다. 하지만 Vera Rubin의 CPU memory 구조는 LPDDR5X와 SOCAMM 모듈까지 끌고 온다.

코리아써키트 thesis가 여기서 나온다.

```text
Vera Rubin CPU memory = LPDDR5X 기반 system memory
→ SOCAMM2 모듈 필요
→ HDI/모듈 PCB 필요
→ 코리아써키트·티엘비 등 후보군 등장
```

다만 여기서도 단정은 금물이다. 코리아써키트가 SOCAMM2와 FC-BGA 양쪽에서 직접 수혜를 받을 가능성은 흥미롭지만, 투자 판단은 다음 조건으로 좁혀야 한다.

1. SOCAMM2 매출이 실제 분기 실적에 잡히는가.
2. FC-BGA 고객 qualification이 확인되는가.
3. 2026~2027년 증설이 고객 LTA와 같이 움직이는가.
4. 매출 증가가 OPM 개선으로 이어지는가.

이 조건이 충족되면 코리아써키트는 "PCB 테마주"가 아니라 Memory row 안에 가려진 **SOCAMM 모듈 기판 알파**가 된다. 반대로 조건이 안 나오면 단순 theme premium이다.

---

## 8. 이수페타시스와 삼성전기 — 좋은 회사와 좋은 진입 가격

이수페타시스는 AI networking, high-layer MLB, switch/router board 관점에서 가장 직관적인 후보 중 하나다. Vera Rubin 세대로 갈수록 scale-out networking, switch board, 고속 신호 routing이 중요해지는 것은 맞다.

문제는 이미 시장이 그 이야기를 알고 있다는 점이다. PCB/MLB 쪽은 좋은 산업이지만 일부 종목은 이미 강하게 리레이팅됐다. 그래서 이수페타시스는 "좋은 회사"와 "좋은 진입 가격"을 분리해야 한다.

삼성전기도 마찬가지다. silicon capacitor 1.5조원 계약은 분명히 중요하다. 그러나 단기 주가가 이미 크게 반응한 상태에서는 추격 매수보다 **매출 인식, 마진, 후속 고객, 증설 CAPEX**를 확인해야 한다.

이 두 종목의 차이는 이렇다.

```text
이수페타시스
→ high-layer MLB / AI networking PCB
→ 수혜 방향은 명확
→ valuation과 crowdedness 확인 필요

삼성전기
→ FC-BGA + silicon capacitor + MLCC
→ 전력무결성 재분류 가능성
→ 계약 마진과 후속 고객 확인 필요
```

둘 다 후보지만 "표를 봤으니 무조건 매수"는 아니다. Vera Rubin BOM 표는 종목 매수 신호가 아니라 **체크리스트를 좁혀주는 지도**다.

---

## 9. 실전 매매 전략

| 종목/축 | 판단 | 한 줄 thesis | Entry 조건 | Invalidation |
|---|---|---|---|---|
| SK하이닉스 / 삼성전자 | Watchlist / 조정 매수 후보 | VR200 BOM 증가분의 42.7%가 Memory에서 발생. HBM4·LPDDR5X·SOCAMM이 1차 병목 | HBM4 allocation, SOCAMM 수주, DRAM ASP 상승이 실적으로 확인될 때 | HBM4 qualification 지연, Rubin 램프 지연, 메모리 가격 급락 |
| 삼성전기 | Wait / Buy on pullback | ABF/FC-BGA + silicon capacitor + MLCC까지 AI 패키지 부품 포트폴리오 보유 | 1.5조원 silicon capacitor 계약의 매출·마진 가시성 확인, 과열 후 조정 | 계약 gross margin이 낮거나 고객·제품 mix가 기대보다 약할 때 |
| 코리아써키트 | Watchlist / catalyst 확인형 | SOCAMM2와 FC-BGA 양쪽 옵션. Memory row 안에 숨은 모듈 기판 알파 | SOCAMM2 매출 인식, FC-BGA qualification, OPM 개선 | SOCAMM 볼륨 부진, FC-BGA 인증 실패, 단순 테마 수급으로 종료 |
| 대덕전자 / 심텍 / 티엘비 | Watchlist | AI 서버 기판·모듈 PCB 2차 수혜 후보 | 직접 고객사·제품 인증, ASP 인상, LTA 기반 증설 | direct exposure 부재, 증설이 수주 없이 선투자로 끝날 때 |
| 이수페타시스 | Wait | high-layer MLB와 AI networking PCB 본류 후보지만 이미 기대가 높음 | 과열 해소, AI switch/networking 매출과 마진 재확인 | valuation 부담 확대, OPM 훼손, 고객 order 지연 |

핵심은 단순하다. **Memory는 구조적, PCB는 선별적, MLCC는 silicon capacitor와 분리**해야 한다.

---

## 10. 리스크와 체크포인트

### 리스크 1 — BOM 추정 오류

이 표는 공식 BOM이 아니다. Morgan Stanley 원문 확인도 아직 blocked다. 외부 보도마다 VR200 rack 가격과 BOM 추정은 다를 수 있다. 따라서 정확한 금액보다 **증분 방향성**에 집중해야 한다.

### 리스크 2 — Memory row 오해

Memory가 전부 HBM은 아니다. HBM4, LPDDR5X, SOCAMM, 기타 system memory가 섞여 있을 가능성이 높다. HBM 업체만으로 해석하면 과도하게 단순화된다.

### 리스크 3 — Direct supplier 여부

국내 PCB, ABF, MLCC, 기판 업체가 모두 Rubin 공급망에 들어가는 것은 아니다. "산업 방향성"과 "개별 회사 매출" 사이에는 고객 인증이라는 좁은 문이 있다.

### 리스크 4 — NVIDIA의 value capture

NVIDIA가 rack-scale system 통합을 강화할수록 ODM과 일부 부품사의 bargaining power가 낮아질 수 있다. 매출은 늘어도 마진이 따라오지 않는 구간이 생길 수 있다.

### 체크포인트

| 체크포인트 | 보면 결론이 바뀌는 지표 |
|---|---|
| HBM4 allocation | SK하이닉스·삼성전자·Micron의 Rubin HBM4 공급 비중 |
| LPDDR5X / SOCAMM | SOCAMM2 실제 매출 인식, module PCB 공급사 확인 |
| 삼성전기 Si-Cap | 2027~2028 계약 외 추가 고객, 증설, gross margin 가이던스 |
| PCB 업체 수주 | 800G/1.6T, AI accelerator, switch board 신규 수주 |
| Rubin 양산 일정 | 2026년 하반기 shipment ramp 속도 |
| NVIDIA 통합 전략 | L10 tray 확대 여부와 부품사/ODM margin 변화 |

---

## 11. 마지막 한 줄

Vera Rubin VR200 BOM 표는 "AI 서버 부품 전부를 사라"는 자료가 아니다. 숫자를 검산하면 더 냉정한 결론이 나온다. 총 증가분 **+$380.9만** 중 Memory가 **+$162.8만, 42.7%**, GPU가 <strong>+$144.0만, 37.8%</strong>다. 둘이 합쳐 증가분의 <strong>80.5%</strong>를 설명한다.

PCB와 MLCC는 증가율이 예쁘다. PCB +232.6%, MLCC +182.4%. 그러나 절대 증가액은 각각 전체 증가분의 2.1%, 0.1% 수준이다. 따라서 "PCB/MLCC 전체 매수"가 아니라 **direct qualification이 있는 고부가 부품사만 선별**해야 한다.

국내 1차 본류는 여전히 **SK하이닉스·삼성전자 Memory**다. 다만 Memory row는 HBM4만이 아니라 LPDDR5X·SOCAMM까지 포함한다. 그래서 코리아써키트·티엘비 같은 모듈 기판 후보가 2차로 등장한다. 삼성전기는 일반 MLCC보다 **silicon capacitor와 AI package power integrity**로 봐야 한다.

진짜 알파는 증가율 headline이 아니라 **rack당 dollar content × 직접 납품 가능성 × 증설 병목 × 마진 레버리지**를 곱하는 데 있다. Vera Rubin은 GPU 랙이 아니라 메모리와 데이터 이동 병목이 재가격화되는 랙이다. 이 표가 말하는 결론은 간단하다. Memory는 구조적, PCB는 선별적, MLCC는 silicon capacitor와 분리해서 봐야 한다.

---

## 데이터와 출처

- NVIDIA Vera Rubin NVL72 공식 스펙: 72 Rubin GPU, 36 Vera CPU, 20.7TB HBM4, 54TB LPDDR5X, preliminary / subject to change. [NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
- Morgan Stanley 추정 BOM 표 2차 보도: VR200 memory bill 약 200만 달러, total BOM 약 780만 달러. [Wccftech](https://wccftech.com/nvidia-vera-rubin-rack-hit-with-memory-price-surge-pushing-hbm4-lpddr5x-bill-to-2m-of-7-8m-total/)
- 삼성전자 GTC 2026 AI 메모리 포트폴리오: HBM4E, NVIDIA 파트너십, AI 솔루션. [Samsung Semiconductor Newsroom](https://news.samsungsemiconductor.com/global/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026/)
- SK하이닉스 GTC 2026 전시 및 NVIDIA 파트너십. [SK hynix Newsroom](https://news.skhynix.co.kr/gtc-2026-exhibition-booth/)
- 삼성전기 silicon capacitor 1.5조원 AI 칩 부품 계약 보도. [Yonhap News Agency](https://en.yna.co.kr/view/AEN20260520008200320)

*이 글은 리서치와 논평으로만 활용해야 하며 투자 조언이 아닙니다. Vera Rubin NVL72 공식 스펙은 NVIDIA 자료 기준이며 preliminary / subject to change입니다. BOM 표는 사용자 제공 이미지와 Wccftech의 Morgan Stanley 추정치 2차 보도를 기준으로 계산했으며, Morgan Stanley 원문 리포트는 직접 확인하지 못했습니다. 표의 금액은 공식 BOM·공식 판매가격·실제 계약 원가가 아닙니다. 국내 종목별 직접 공급 여부, gross margin, LTA, qualification은 공개자료로 완전히 확인되지 않은 항목이 많습니다. 분석이 틀릴 수도 있습니다. 데이터 기준일: 2026년 5월 21일 KST.*
