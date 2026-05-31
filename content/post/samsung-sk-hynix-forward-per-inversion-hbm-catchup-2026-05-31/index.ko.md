---
title: "삼성전자 vs SK하이닉스 Forward PER 역전: HBM 프리미엄은 뉴노멀인가"
date: 2026-05-31T11:30:00+09:00
description: "SK하이닉스의 forward PER이 삼성전자를 넘어선 현상을 HBM 병목 프리미엄, 삼성전자 HBM4E catch-up, DRAM/NAND ASP 상승, 2027년 EPS revision으로 분해한다."
categories: ["Market-Outlook"]
tags:
  - "삼성전자"
  - "005930"
  - "SK하이닉스"
  - "000660"
  - "HBM"
  - "HBM4E"
  - "AI 메모리"
  - "Forward PER"
  - "메모리 슈퍼사이클"
  - "한국 반도체"
slug: samsung-sk-hynix-forward-per-inversion-hbm-catchup-2026-05-31
valley_cashtags:
  - 삼성전자
  - SK하이닉스
draft: false
---

> 후속 글 맥락
> 이 글은 [삼성전자 특별성과급·슈퍼사이클 글](/ko/post/samsung-electronics-stock-bonus-supercycle-buyback-2026-05-27/), [AI 인프라 멀티플 지도](/ko/post/ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31/), [NVIDIA Vera Rubin 추론 스택 글](/ko/post/nvidia-vera-rubin-lpx-cmx-inference-stack-samsung-hbm-2026-05-28/)의 연결 글입니다. 앞선 글들이 삼성전자 DS 이익 duration, HBM 아래 밸류체인, 추론 memory hierarchy를 봤다면, 이번 글은 삼성전자와 SK하이닉스의 forward PER 역전이 실제로 어떤 투자 신호인지 정리합니다. 관련 허브는 [AI HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/)입니다.
> 다음 연결 글은 [SK하이닉스 vs 마이크론: HBM 기술 프리미엄인가, 미국 상장 프리미엄인가](/ko/post/sk-hynix-vs-micron-hbm-premium-ai-memory-platform-2026-05-31/)입니다.

## TL;DR

SK하이닉스의 forward PER이 삼성전자보다 높아진 현상은 과거 기준으로는 이례적입니다. 전통적으로 메모리 pure-play인 SK하이닉스는 삼성전자보다 사이클·고객집중·재무안정성 디스카운트를 받는 것이 자연스러웠습니다.

그러나 지금은 단순한 오류라기보다 <strong>HBM 병목 프리미엄</strong>과 <strong>삼성전자 HBM laggard discount</strong>가 충돌하는 구간입니다. SK하이닉스는 AI HBM 리더로 재분류됐고, 삼성전자는 HBM4E catch-up과 DRAM/NAND 전면 가격 상승이 아직 valuation에 다 반영되지 않았을 가능성이 있습니다.

결론은 <strong>SK하이닉스 추격매수보다 삼성전자 catch-up trade</strong>가 더 강하다는 쪽입니다. 단, 이 판단은 HBM4E 고객 인증, 2027년 EPS revision, DS margin 방어가 확인될 때 더 강해집니다.

---

## 1. 데이터 기준: 연간 PER은 역전, 12MF는 parity 접근

정확한 월별 12개월 선행 PER 시계열은 Bloomberg, FactSet, LSEG, FnGuide 같은 단말 데이터가 필요합니다. 공개 자료만으로는 완전한 3년 시계열을 재현하기 어렵습니다. 그래서 이번 글은 세 종류의 데이터를 분리합니다.

| 기준 | 현재 해석 |
|---|---|
| FnGuide 2026E PER | 삼성전자 6.77배, SK하이닉스 6.79배로 SK하이닉스가 근소하게 역전한 것으로 보도 |
| 2026-05-29 종가와 2026E EPS proxy | 삼성전자 약 7.55배, SK하이닉스 약 8.02배로 SK하이닉스 프리미엄 약 6.2% |
| 미래에셋 2026-05-22 12MF PER | 삼성전자 6.2배, SK하이닉스 5.9배로 12개월 선행 기준은 아직 삼성전자가 더 높거나 parity 접근 |

보수적 표현은 이것입니다.

> <strong>2026E 연간 PER 기준으로는 역전이 확인됐고, 12개월 선행 PER 기준으로는 parity에 접근한 상태입니다.</strong>

따라서 "하이닉스 PER이 삼성전자보다 영구적으로 높아졌다"가 아니라, "시장 일부가 SK하이닉스를 HBM 병목 기업으로 재분류하기 시작했다"가 더 정확합니다.

---

## 2. 왜 이례적인가

과거에는 삼성전자가 SK하이닉스보다 높은 멀티플을 받는 것이 더 자연스러웠습니다.

1. 삼성전자는 메모리 외에도 모바일, 디스플레이, 가전, 파운드리, 시스템LSI를 가진 복합 기업입니다.
2. 재무 안정성과 현금흐름이 SK하이닉스보다 높게 평가됐습니다.
3. SK하이닉스는 pure memory 기업에 가까워 업황 하락 시 이익 변동성이 더 컸습니다.
4. 메모리 업종은 공급 과잉과 ASP 하락 리스크 때문에 전통적으로 낮은 PER을 받았습니다.

그래서 "SK하이닉스 PER > 삼성전자 PER"은 전통 프레임에서는 이상합니다. 하지만 HBM에서는 프레임이 바뀝니다.

HBM은 범용 DRAM이 아닙니다. GPU와 AI ASIC의 성능·전력·패키징 구조를 좌우하는 고객별 인증 부품입니다. 공급자가 한번 검증되면 고객은 쉽게 바꾸기 어렵고, 장기공급계약과 allocation visibility도 커집니다. 이 때문에 SK하이닉스는 "메모리 경기민감주"에서 "AI 메모리 병목 공급자"로 재평가되고 있습니다.

---

## 3. SK하이닉스 프리미엄이 설명되는 이유

SK하이닉스의 2026년 1분기 실적은 전통적 메모리 회사의 수익성으로 보기 어렵습니다. 회사는 1Q26 매출 52.6조원, 영업이익 37.6조원, 영업이익률 72%를 기록했습니다. ([SK hynix Newsroom][8])

이 정도 이익률이 가능한 이유는 단순 DRAM 가격 상승만이 아닙니다. 고부가 HBM과 서버 메모리 믹스가 강해지고, 고객 입장에서는 검증된 HBM 공급자가 GPU 출하 병목을 좌우하기 때문입니다.

SK하이닉스 프리미엄은 다음 조건에서 정당화됩니다.

| 조건 | 의미 |
|---|---|
| HBM 점유율 유지 | AI accelerator memory 병목 지위 지속 |
| HBM4/HBM4E 세대 전환 선도 | 차세대에서도 고객 lock-in 유지 |
| LTA 확대 | 피크이익 의심 완화 |
| 고ROE 지속 | PER뿐 아니라 P/B 프리미엄 정당화 |
| 삼성전자 추격 지연 | 상대 프리미엄 유지 |

즉 SK하이닉스의 프리미엄은 이상한 고평가라기보다, HBM이 commodity DRAM이 아니라 <strong>계약 기반 high-value memory franchise</strong>로 바뀔 수 있다는 시장의 베팅입니다.

---

## 4. 그래도 알파는 삼성전자 catch-up 쪽에 있다

문제는 가격입니다. SK하이닉스는 이미 HBM 리더십을 상당 부분 반영받기 시작했습니다. 반면 삼성전자는 여전히 HBM laggard discount를 받고 있습니다.

삼성전자 catch-up trade의 핵심은 세 가지입니다.

### 4.1 HBM4E 12단 샘플 출하

삼성전자는 2026년 5월 HBM4E 12단 샘플을 주요 글로벌 고객에게 출하했다고 보도됐습니다. 아직은 고객 qualification 전 단계이므로 매출 확정으로 보면 안 됩니다. 하지만 valuation 관점에서는 샘플 자체보다 다음 경로가 중요합니다. ([Reuters][2])

```text
HBM4E sample
→ customer qualification
→ mass production
→ EPS revision
→ HBM laggard discount 축소
```

시장은 아직 이 경로를 완전히 가격에 반영하지 않았을 가능성이 있습니다.

### 4.2 DRAM/NAND 전면 가격 상승

2026년 1분기 메모리 가격 급등은 HBM만의 이야기가 아닙니다. TrendForce는 삼성전자 메모리 ASP가 2025년 평균 대비 146% 상승했고, SK하이닉스도 DRAM ASP mid-60%, NAND ASP mid-70% QoQ 상승을 기록했다고 정리했습니다. ([TrendForce][3])

이 점은 삼성전자에 중요합니다. SK하이닉스는 HBM beta가 더 깨끗하지만, 삼성전자는 DRAM, NAND, HBM, eSSD, SOCAMM까지 포트폴리오가 넓습니다. 범용 메모리 squeeze가 커질수록 삼성전자 EPS revision 폭이 더 넓어질 수 있습니다.

### 4.3 DS 이익 규모와 파운드리 옵션

삼성전자 1Q26 DS 부문은 매출 81.7조원, 영업이익 53.7조원을 기록했습니다. 절대 이익 규모만 보면 이미 거대합니다. ([Samsung Global Newsroom][5])

여기에 HBM4E가 logic base die와 advanced packaging을 필요로 한다면, 삼성전자는 단순 메모리 업체가 아니라 메모리·base die·패키징을 함께 가져가는 옵션을 가집니다. 이 옵션은 아직 SK하이닉스의 HBM pure-play 프리미엄만큼 선명하게 가격화되지 않았습니다.

---

## 5. 상대가치 전략: Long Samsung / Neutral Hynix

현재 가장 실용적인 전략은 "SK하이닉스가 나쁘다"가 아니라, <strong>삼성전자 catch-up의 기대수익이 더 좋아 보인다</strong>입니다.

| SK하이닉스 PER premium vs 삼성전자 | 해석 | 전략 |
|---:|---|---|
| 0~5% | HBM 리더십 감안 시 허용 가능 | 양사 보유 가능 |
| 5~10% | 삼성전자 catch-up 매력 증가 | 삼성전자 비중 확대 |
| 10~15% | SK하이닉스 premium 과도 가능성 | 삼성전자 long / SK하이닉스 neutral |
| 15% 이상 + EPS 상향 둔화 | mean reversion 가능성 큼 | 삼성전자 우선 |

입력 자료의 2026-05-29 종가와 2026E EPS proxy 기준 SK하이닉스 premium은 약 6.2%입니다. 이미 삼성전자 catch-up 논리가 작동하기 시작하는 구간입니다.

---

## 6. 삼성전자 upside bridge

삼성전자 2026E EPS proxy를 41,972원으로 두고, 2026-05-29 종가 317,000원을 적용하면 단순 PER은 약 7.55배입니다.

| EPS 추가 상향 | 수정 EPS | 현재가 317,000원 기준 PER |
|---:|---:|---:|
| 0% | 41,972원 | 7.55배 |
| +10% | 46,169원 | 6.87배 |
| +15% | 48,268원 | 6.57배 |
| +20% | 50,366원 | 6.29배 |

만약 삼성전자 EPS가 15% 상향되고 시장이 SK하이닉스에 가까운 8.0배 PER을 부여한다면:

```text
48,268원 × 8.0배 = 386,144원
```

현재가 317,000원 대비 upside는 약 21.8%입니다. 이 산식은 목표주가가 아니라, <strong>EPS revision + PER parity 회복</strong>이 얼마나 강한 조합인지 보여주는 민감도입니다.

---

## 7. 리스크와 깨지는 조건

이 thesis가 깨지는 조건은 명확합니다.

| 리스크 | 의미 |
|---|---|
| 삼성전자 HBM4E 고객 인증 지연 | HBM laggard discount가 유지 |
| HBM4E 수율 부진 | EPS revision이 나오지 않음 |
| DRAM/NAND 가격 둔화 | 삼성전자 포트폴리오 breadth thesis 약화 |
| 파운드리·LSI 손실 확대 | 메모리 이익을 비메모리 drag가 상쇄 |
| SK하이닉스 2027E EPS 추가 상향 | HBM 리더 premium이 더 정당화 |
| AI capex 둔화 | HBM 전반의 피크이익 의심 재부상 |

특히 삼성전자 HBM4E 샘플은 [Fact]이지만, 고객 인증과 양산은 아직 [Blocked]입니다. 이 구분이 중요합니다.

---

## 최종 판단

SK하이닉스의 forward PER이 삼성전자를 넘어선 현상은 이례적이지만, 비정상은 아닙니다. HBM이 commodity memory에서 AI 인프라 병목으로 바뀌면서 SK하이닉스가 더 높은 멀티플을 받을 수 있는 조건은 생겼습니다.

다만 현재 투자 알파는 SK하이닉스 추격보다 삼성전자 catch-up 쪽이 더 강합니다. 이유는 세 가지입니다.

1. SK하이닉스는 이미 HBM 리더십을 가격에 반영받기 시작했습니다.
2. 삼성전자는 HBM4E, DRAM/NAND ASP 상승, DS 이익 규모가 valuation에 덜 반영됐을 가능성이 있습니다.
3. PER spread가 5~10% 이상 벌어질수록 상대가치상 삼성전자 매력이 커집니다.

따라서 결론은 <strong>삼성전자: 조건부 Buy / SK하이닉스: Hold-Wait</strong>입니다. 핵심 확인 변수는 HBM4E qualification, 2027년 EPS revision, DS margin, 그리고 SK하이닉스 HBM4/HBM4E 점유율 방어입니다.

---

## 근거 구분

### [Fact]

- FnGuide 기준 2026E PER은 삼성전자 6.77배, SK하이닉스 6.79배로 역전됐다고 보도됐습니다. ([Seoul Economic Daily][1])
- 삼성전자는 HBM4E 12단 샘플을 주요 글로벌 고객에게 출하했다고 보도됐습니다. ([Reuters][2])
- 2026년 1분기 메모리 가격은 급등했고, 삼성전자 메모리 ASP와 SK하이닉스 DRAM/NAND ASP 모두 강했습니다. ([TrendForce][3])
- 삼성전자 1Q26 DS 부문은 매출 81.7조원, 영업이익 53.7조원을 기록했습니다. ([Samsung Global Newsroom][5])
- SK하이닉스 1Q26은 매출 52.6조원, 영업이익 37.6조원, 영업이익률 72%를 기록했습니다. ([SK hynix Newsroom][8])

### [Inference]

- SK하이닉스는 commodity memory pure-play에서 AI HBM bottleneck supplier로 재평가되고 있습니다.
- 삼성전자는 HBM laggard discount가 줄어들 경우 PER parity 회복 여지가 있습니다.
- 상대수익률 관점의 알파는 SK하이닉스보다 삼성전자 catch-up trade에 더 있습니다.

### [Blocked]

- 정확한 최신 12개월 선행 PER 월별 시계열.
- 삼성전자 HBM4E 고객별 qualification, 수율, 양산 물량, ASP.
- 2027년 HBM LTA의 가격 하방 방어력.

## Sources

[1]: https://en.sedaily.com/finance/2026/05/13/sk-hynix-valuation-overtakes-samsung-electronics-for-first "SK hynix valuation overtakes Samsung Electronics for first"
[2]: https://www.reuters.com/world/asia-pacific/samsung-electronics-ships-hbm4e-chip-samples-global-customers-2026-05-28/ "Samsung Electronics ships faster HBM4E chip samples to customers"
[3]: https://www.trendforce.com/news/2026/05/18/news-memory-supercycle-drives-1q26-price-surge-samsung-flags-146-asp-jump-sk-hynix-sees-mid-60-dram-gains/ "Memory supercycle drives 1Q26 price surge"
[4]: https://www.businesskorea.co.kr/news/articleView.html?idxno=270382 "Samsung Electronics market cap surges past ..."
[5]: https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results "Samsung Electronics announces first quarter 2026 results"
[6]: https://securities.miraeasset.com/bbs/download/2144785.pdf?attachmentId=2144785 "Mirae Asset Securities strategy report"
[7]: https://www.reuters.com/world/asia-pacific/sk-hynix-market-capitalisation-tops-1-trln-2026-05-27/ "SK Hynix joins $1 trillion club"
[8]: https://news.skhynix.co.kr/q1-2026-business-results/ "SK하이닉스, 2026년 1분기 경영실적 발표"

*Disclaimer: For research and information purposes only. Not investment advice.*
