---
title: "삼성전기 실리콘 커패시터와 인텔 EMIB-T: AI 패키지 전력망 안쪽으로 들어간 부품"
date: 2026-05-28T17:20:00+09:00
description: "삼성전기의 실리콘 커패시터 1.5조원 계약을 인텔 EMIB-T와 AI 패키지 PDN 관점에서 재해석한다. 공식 확인된 것은 글로벌 대형 고객과의 Si-Cap 계약이고, 구글 TPU v8e·인텔 EMIB-T 최종 탑재는 아직 추정 영역이다. 핵심은 삼성전기가 MLCC·FC-BGA를 넘어 AI 패키지 내부 전력 무결성 부품으로 들어가기 시작했다는 점이다."
categories: ["Stock-Analysis"]
tags:
  - "삼성전기"
  - "009150"
  - "실리콘 커패시터"
  - "Silicon Capacitor"
  - "EMIB-T"
  - "Intel Foundry"
  - "AI 패키징"
  - "PDN"
  - "MLCC"
  - "FC-BGA"
  - "HBM"
  - "Ibiden"
  - "Murata"
slug: samsung-electro-mechanics-silicon-capacitor-emib-t-ai-package-pdn-2026-05-28
valley_body_mode: teaser
valley_cashtags:
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - 대덕전자
  - 이수페타시스
valley_cashtag_exclude:
  - Intel
  - Google
draft: false
---

> 📚 삼성전기 시리즈 후속
> [실리콘 커패시터 1.5조원 계약](/ko/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [MLCC와 실리콘 커패시터 이해하기](/ko/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/) / [AI 서버 수동소자 병목](/ko/post/ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26/) / [삼성전기 시총 100조 돌파](/ko/post/samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26/) / [마벨 Q1과 한국 반도체](/ko/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/)
> 관련 허브: [AI 기판·PCB 허브](/ko/page/korea-ai-pcb-substrate-hub/) / [한국 반도체 밸류체인 허브](/ko/page/korea-semiconductor-equipment-ip-hub/)

## TL;DR

이번 이슈의 본질은 <strong>삼성전기가 AI 반도체의 안쪽으로 들어가기 시작했다</strong>는 점이다.

기존 MLCC는 스마트폰, 자동차, 서버 보드 곳곳에 붙는 전기 저장 부품이다. 그러나 AI 가속기와 HBM이 들어간 최신 패키지는 순간 전류 변동이 너무 크다. 보드 위에 MLCC를 많이 붙이는 것만으로는 칩 바로 옆에서 발생하는 전압 흔들림을 충분히 잡기 어렵다. 그래서 전기를 저장했다가 아주 빠르게 내보내는 부품을 칩에 더 가깝게 배치해야 한다. 삼성전기의 실리콘 커패시터는 바로 이 역할을 겨냥한다.

인텔 EMIB-T는 이 변화를 설명하기 좋은 기술 프레임이다. 인텔은 EMIB가 로직-로직과 로직-HBM 연결에 쓰이는 2.5D 패키징이고, EMIB-T가 브리지에 TSV를 더해 전력 전달과 신호 라우팅을 강화한다고 설명한다. AI 칩이 커지고 HBM 개수가 늘수록 패키지 내부 전력망은 더 복잡해진다. 실리콘 커패시터 같은 초저 ESL 부품이 중요해질 수밖에 없는 이유다. ([Intel][3])

다만 고객명은 조심해야 한다. 공식 확인된 것은 <strong>삼성전기가 글로벌 대형 기업과 2027~2028년 약 1.5조원 규모의 실리콘 커패시터 계약을 체결했다는 사실</strong>이다. 구글 TPU v8e, MediaTek, Intel EMIB-T 최종 탑재는 산업매체와 증권가의 추정이지, 삼성전기·구글·인텔의 공식 확인이 아니다. ([Samsung Electro-Mechanics][1])

결론은 이렇다. 이번 뉴스는 삼성전기의 밸류에이션 스토리를 바꿀 수 있는 재료다. 과거 삼성전기는 MLCC 사이클, 스마트폰 카메라, 패키지기판 업황의 영향을 받는 전자부품주 성격이 강했다. 그러나 Si-Cap이 2027년부터 대량 양산되고, EMIB-T나 다른 AI ASIC 패키지로 고객이 확장된다면 삼성전기는 <strong>AI 인프라 패키지 전력망 핵심 부품사</strong>로 재평가될 수 있다. 반대로 1.5조원 계약이 단일 고객·단일 프로젝트에 머물거나, 고객 램프가 지연되거나, 듀얼소싱이 강해지면 현재 기대는 빠르게 낮아질 수 있다.

---

## 1. 왜 이 뉴스는 MLCC 뉴스가 아닌가

AI 패키지에서 전력 문제는 단순히 “전기를 많이 쓴다”가 아니다. 문제는 <strong>전류가 갑자기 바뀔 때 전압이 흔들린다</strong>는 점이다. GPU, AI ASIC, HBM은 아주 짧은 시간에 큰 전류를 요구한다. 전압이 흔들리면 클럭 마진이 줄고, 오류 가능성이 커지고, 성능을 보수적으로 잡아야 한다.

그래서 고성능 패키지에서는 전원 안정화 부품을 칩에 최대한 가깝게 둔다. 보드 위 MLCC도 계속 필요하지만, AI GPU·HBM 패키지 내부나 바로 근처에서는 더 얇고, 더 낮은 ESL/ESR을 가진 부품이 필요하다.

삼성전기는 실리콘 커패시터를 다음처럼 설명한다. 실리콘 웨이퍼 위에 유전체와 내부전극을 적층해 만들고, 웨이퍼 그라인딩으로 100㎛ 이하 박막화가 가능하며, Low ESL 특성이 전원 안정화에 유리하다. 적용 방식도 Land-side, Top-side, Embedded 타입으로 나뉜다. 즉 단순 보드 부품이 아니라 패키지 설계 안쪽에 들어갈 수 있는 부품이다. ([Samsung Electro-Mechanics][2])

이것이 삼성전기 투자 스토리의 핵심이다. 회사는 이미 MLCC에서 고온·고압·초고용량 기술을 축적했고, FC-BGA에서는 AI 가속기·서버 CPU용 고다층·대면적 기판으로 이동하고 있다. 여기에 Si-Cap이 붙으면 “AI 서버 전력 안정화 부품 포트폴리오”가 보드 레벨 MLCC에서 패키지 내부 부품까지 확장된다.

---

## 2. EMIB-T는 왜 중요한가

인텔 EMIB는 전체 실리콘 인터포저를 쓰는 대신, 기판 내부에 작은 실리콘 브리지를 넣어 여러 다이를 연결하는 2.5D 패키징이다. 인텔은 EMIB를 로직-로직, 로직-HBM 연결에 쓰는 기술로 설명하고, 2017년부터 고용량 제조에 쓰였다고 밝힌다. ([Intel][4])

EMIB-T의 변화는 더 중요하다. 인텔은 EMIB-M이 브리지 안에 MIM 커패시터를 넣어 전력 전달을 보강하고, EMIB-T는 TSV를 추가해 HBM 수요 증가에 따른 수직 전력 전달 요구에 대응한다고 설명한다. 다시 말하면 브리지가 단순 신호 연결 통로에서 <strong>전력 전달 구조</strong>까지 포함하는 방향으로 진화하는 것이다. ([Intel][4])

Synopsys도 같은 방향으로 설명한다. EMIB-T는 TSV 기반 전력 전달, backside bumping, 더 조밀한 MIM capacitor, 고속 프로토콜 라우팅을 포함한다. 대형 컴퓨트 다이, 차세대 HBM, AI 가속기 클러스터가 커지면서 신호 무결성과 전력 전달을 동시에 해결해야 하기 때문이다. ([Synopsys][5])

여기서 투자 포인트는 “인텔 EMIB가 무조건 뜬다”가 아니다. 더 정확한 문장은 다음이다.

> AI 패키지가 커질수록 패키지 내부 전원망, 즉 PDN 부품이 고도화된다. EMIB-T는 그 흐름을 보여주는 사례이고, 실리콘 커패시터는 그 안에서 부품 단위로 부상하는 영역이다.

---

## 3. 확인된 것과 아직 추정인 것

| 항목 | 판단 | 코멘트 |
|---|---:|---|
| 삼성전기 실리콘 커패시터 1.5조원 계약 | <strong>Fact</strong> | 삼성전기는 글로벌 대형 기업과 약 1.5조원 규모 계약을 체결했고, 기간은 2027년 1월 1일~2028년 12월 31일이라고 밝혔다. ([Samsung Electro-Mechanics][1]) |
| Si-Cap이 AI 서버 GPU·HBM 패키지 내부 전력 안정화에 쓰인다는 설명 | <strong>Fact</strong> | 삼성전기 공식 보도자료와 제품 페이지에서 확인된다. ([Samsung Electro-Mechanics][1], [2]) |
| EMIB가 로직-HBM 연결에 쓰이는 인텔 2.5D 패키징이라는 점 | <strong>Fact</strong> | 인텔 공식 패키징 페이지와 EMIB 기술 브리프에서 확인된다. ([Intel][3], [4]) |
| EMIB-T가 TSV를 추가해 전력 전달과 신호 라우팅을 강화한다는 점 | <strong>Fact</strong> | 인텔과 Synopsys 설명이 일치한다. ([Intel][4], [Synopsys][5]) |
| 이비덴의 AI·고성능 서버용 고성능 IC 패키지 기판 증설 | <strong>Fact</strong> | 이비덴은 FY2026~FY2028 총 5,000억엔 투자, FY2027부터 순차 가동·양산 계획을 밝혔다. ([Ibiden][6]) |
| 삼성전기 계약 상대가 구글이고 TPU v8e에 탑재된다는 주장 | <strong>Unclear</strong> | 시장 추정으로는 가능하지만, 삼성전기·구글·인텔 공식 확인은 아니다. |
| 이비덴 투자금이 EMIB-T 전용이고 특정 빅테크 자금으로 대부분 충당된다는 주장 | <strong>Unclear</strong> | 이비덴 공식 자료는 고성능 IC 패키지 기판 증설을 말하지만 고객명·EMIB-T 전용성은 명시하지 않는다. |

공식 확인과 추정은 반드시 분리해야 한다. 이번 계약의 질은 높지만, “구글 확정 수주”라고 쓰는 순간 글의 신뢰도가 떨어진다. 더 안전한 표현은 다음이다.

> 공식적으로는 삼성전기의 글로벌 대형 고객 Si-Cap 계약이 확인됐다. 시장은 이를 Intel EMIB-T, Google TPU 계열, AI ASIC 패키지 PDN 고도화와 연결해 해석하고 있다.

---

## 4. 삼성전기 thesis: MLCC + FC-BGA + Si-Cap

삼성전기 입장에서 이번 뉴스는 단순히 신규 부품 하나가 추가된 사건이 아니다. 세 개의 축이 하나로 묶인다.

| 축 | 기존 포지션 | AI 패키지에서의 확장 |
|---|---|---|
| MLCC | 보드·서버·전장 전원 안정화 부품 | AI 서버와 네트워크 장비의 고부가 MLCC 수요 |
| FC-BGA | 서버 CPU·AI 가속기용 고다층·대면적 기판 | GPU·ASIC·network ASIC이 커질수록 기판 면적·층수·난도 상승 |
| Si-Cap | 신규 고부가 수동부품 | GPU·HBM·AI ASIC 패키지 내부, die-near PDN 부품 |

이 조합이 중요하다. 삼성전기는 칩을 설계하거나 제조하는 회사가 아니다. 그러나 칩이 실제로 작동하려면 전기를 안정적으로 공급하고, 신호를 잃지 않고 이동시키고, 여러 다이와 HBM을 한 패키지 안에서 묶어야 한다. 바로 그 하부 구조에 삼성전기의 제품이 들어간다.

Si-Cap의 장점은 단가만이 아니다. 패키지 내부 부품은 고객 인증 장벽이 높고, 한 번 설계에 들어가면 교체 비용이 크다. 특정 패키지의 전기적 특성, 열, 신뢰성, 조립 수율까지 검증해야 하기 때문이다. 따라서 첫 대형 디자인윈은 매출보다 <strong>레퍼런스 가치</strong>가 크다.

---

## 5. 밸류체인: 누가 무엇을 가져가는가

| 밸류체인 | 수혜/영향 | 투자 해석 |
|---|---|---|
| Intel Foundry / Advanced Packaging | EMIB-T가 CoWoS 병목의 대안·보완 경로로 부상 | 인텔이 전공정 파운드리에서 TSMC를 바로 따라잡지 못하더라도, 후공정 패키징 슬롯을 확보하면 AI ASIC 고객 접점이 생긴다. |
| Ibiden 등 고성능 기판 업체 | AI 서버·고성능 서버용 IC 패키지 기판 증설 | 이비덴의 5,000억엔 계획은 기판 병목이 구조적임을 보여준다. 단, EMIB-T 전용 고객·물량은 공식 확인 전까지 추정이다. ([Ibiden][6]) |
| 삼성전기 | 1.5조원 Si-Cap 계약 공식 확인 | 고객명은 비공개지만, AI 패키지 내부 전원 안정화 부품이 상업화 단계에 진입했다는 강한 신호다. ([Samsung Electro-Mechanics][1]) |
| Murata | 실리콘 커패시터/IPD 기존 강자 | 무라타는 3D 실리콘 커패시터와 커스텀 IPD 포트폴리오를 보유한다. 삼성전기와의 경쟁·멀티소싱 구도 확인이 필요하다. ([Murata][7]) |
| Synopsys 등 EDA/패키지 설계 생태계 | EMIB-T 설계 복잡도 증가 수혜 | 칩렛, UCIe, HBM, 전력망, 열, 신호무결성을 동시에 검증해야 하므로 3DIC 설계 플로우의 가치가 올라간다. ([Synopsys][5]) |
| TSMC CoWoS | 경쟁이지만 단기 대체보다 병목 완화 | EMIB-T는 CoWoS를 즉시 대체하기보다, CoWoS 공급 부족 속에서 AI ASIC 고객의 second path가 될 가능성이 크다. |

---

## 6. 기술적 해자: 실리콘 커패시터에서 어려운 지점

첫째, <strong>초저 ESL/ESR 구현</strong>이다. AI 패키지에서는 커패시터 자체 성능보다 칩까지의 전류 루프 길이가 중요하다. 부품을 패키지 하부, 상부, 기판 내부에 넣어 전류 경로를 줄이는 설계가 핵심이다.

둘째, <strong>패키지 공동 인증</strong>이다. 실리콘 커패시터는 독립 부품으로만 팔리는 것이 아니라, 특정 AI ASIC 패키지의 PDN 설계에 맞춰 용량, 두께, 패드, 배치, 신뢰성 조건이 정해진다. 삼성전기가 고객 인증과 기술 진입장벽을 강조하는 이유가 여기에 있다. ([Samsung Electro-Mechanics][1])

셋째, <strong>수율과 공급 안정성</strong>이다. 실리콘 커패시터는 웨이퍼 기반 부품이다. 전통 MLCC와 제조 철학이 다르며, 박막화, 그라인딩, 다이싱, 패키지 조립 과정에서 모두 수율 관리가 필요하다.

넷째, <strong>고객 락인</strong>이다. AI 패키지의 PDN에 특정 실리콘 커패시터가 들어가면, 대체 공급사를 넣으려면 전기적 특성, 열, 신뢰성, 조립 수율을 다시 검증해야 한다. 초기 디자인윈 업체가 유리한 이유다.

---

## 7. 투자 판단: 좋은 뉴스와 좋은 가격은 다르다

삼성전기의 방향은 맞다. Si-Cap은 AI 패키지의 전력 무결성 병목을 해결하는 부품이고, 삼성전기는 의미 있는 첫 대형 레퍼런스를 확보했다. 그러나 주식시장은 이미 이 스토리를 빠르게 가격에 반영했다.

그래서 현재 투자 판단은 <strong>Wait / Watchlist</strong>가 더 맞다. 이유는 단순하다.

첫째, 1.5조원 계약은 크지만 2027~2028년 2년에 걸쳐 인식된다. 이번 계약 하나만으로 삼성전기의 전체 시가총액 재평가를 모두 설명하기는 어렵다.

둘째, 진짜 알파는 반복성이다. 이번 계약이 단일 고객·단일 프로젝트라면 re-rating은 오래가기 어렵다. 반대로 2027년 중 두 번째·세 번째 AI ASIC 고객이나 후속 세대 계약이 확인되면 “부품 수주”가 아니라 “플랫폼 공급자” 논리가 생긴다.

셋째, 마진은 아직 공개되지 않았다. Si-Cap이 고부가 부품인 것은 맞지만, 초기 수율, 고객 가격 조건, 공정비, 검사비에 따라 실제 영업이익률은 달라진다.

체크리스트는 다음이다.

| 체크포인트 | 왜 중요한가 |
|---|---|
| 2027년 Si-Cap 매출 인식 시작 | 계약이 실제 손익계산서로 들어오는 첫 증거 |
| 고객 다변화 | 단일 프로젝트가 아니라 반복 가능한 플랫폼인지 판단 |
| 적용 위치 | Top-side, Land-side, Embedded 중 어디냐에 따라 ASP·락인 강도가 달라질 수 있음 |
| 수율과 CAPA | 웨이퍼 기반 초박형 제품이라 초기 수율이 마진을 좌우 |
| MLCC·FC-BGA 동반 성장 | Si-Cap만이 아니라 AI 전력무결성 포트폴리오 전체가 커지는지 확인 |

---

## 8. Red Team: 틀릴 수 있는 지점

첫째, <strong>고객명 과잉 해석</strong>이다. 구글 TPU v8e, MediaTek, Intel EMIB-T 연결은 투자자에게 매력적인 내러티브지만 아직 공식 확인이 아니다. 구글 공식 TPU 페이지는 8세대 TPU의 방향을 설명하지만, 삼성전기 Si-Cap 탑재나 EMIB-T 채택을 확인해주지는 않는다. ([Google Cloud][8])

둘째, <strong>EMIB-T 수율과 일정</strong>이다. EMIB-T는 전력 전달과 신호 라우팅을 동시에 개선해야 하므로 양산 램프업 난도가 높다. 기술 방향이 맞아도 고객 양산이 늦어지면 부품 매출도 늦어진다.

셋째, <strong>경쟁 리스크</strong>다. Murata는 이미 실리콘 커패시터와 IPD 포트폴리오를 보유한 기존 강자다. 삼성전기가 첫 대형 계약을 따냈다고 해서 장기 점유율이 자동으로 고정되는 것은 아니다. ([Murata][7])

넷째, <strong>TSMC CoWoS의 반격</strong>이다. EMIB-T가 뜬다고 해서 CoWoS가 사라지는 것이 아니다. 실제 고객은 수율, 비용, HBM 조달, 패키지 턴어라운드, 장기 capacity를 놓고 여러 옵션을 병행할 가능성이 높다.

---

## 9. 결론

이 뉴스는 AI 반도체 투자 포인트가 전공정 미세화에서 후공정 전력·신호 무결성으로 확장되고 있음을 보여주는 사례다. EMIB-T는 인텔이 TSMC CoWoS 병목을 파고들 수 있는 패키징 카드이고, 실리콘 커패시터는 그 과정에서 부품 단위로 새롭게 부각되는 영역이다.

가장 현실적인 해석은 다음이다.

| 확신도 | 판단 |
|---|---|
| High | AI 패키지에서 die-near, package-embedded 전원 안정화 부품의 중요성은 커진다. |
| Medium | 삼성전기·무라타 같은 실리콘 커패시터 업체는 2027년 이후 고성능 패키지 부품 시장에서 새로운 성장축을 만들 수 있다. |
| Low~Medium | 구글 TPU v8e·아마존 AI ASIC이 대규모로 인텔 EMIB-T를 채택하고, 그 안에 특정 한국 업체의 실리콘 커패시터가 들어간다는 연결고리는 아직 공식 확인이 부족하다. |

비전공자식으로 압축하면, AI칩은 이제 “칩 자체를 잘 만드는 것”만으로 부족하다. 칩과 HBM을 한 패키지 안에 넣고, 그 안에서 전기를 흔들림 없이 공급하는 기술이 성능을 좌우한다. 실리콘 커패시터는 이 전기 흔들림을 칩 바로 옆에서 잡아주는 고급 부품이다.

이번 뉴스가 맞게 전개된다면, 앞으로 AI 패키지 경쟁은 <strong>TSMC CoWoS vs Intel EMIB-T</strong>뿐 아니라 그 안에 들어가는 <strong>기판·브리지·커패시터·EDA 공동설계 생태계 경쟁</strong>으로 확대된다. 삼성전기는 바로 그 생태계 안쪽으로 들어가기 시작했다.

---

## 근거 구분

### [Fact]

- 삼성전기는 글로벌 대형 기업과 약 1.5조원 규모의 실리콘 커패시터 공급계약을 체결했고, 계약 기간은 2027년 1월 1일부터 2028년 12월 31일까지다. ([Samsung Electro-Mechanics][1])
- 삼성전기는 실리콘 커패시터를 AI 서버용 GPU·HBM 등 고성능 반도체 패키지 내부 전력 안정화 부품으로 설명한다. ([Samsung Electro-Mechanics][1])
- 삼성전기 실리콘 커패시터는 100㎛ 이하 박막화, Low ESL, Land-side/Top-side/Embedded 적용이 가능하다. ([Samsung Electro-Mechanics][2])
- 인텔 EMIB는 로직-로직과 로직-HBM 연결에 쓰이는 2.5D 패키징이고, EMIB-T는 TSV를 브리지에 추가한다. ([Intel][3])
- 이비덴은 AI 서버·고성능 서버용 고성능 IC 패키지 기판 생산능력 확대를 위해 FY2026~FY2028 총 5,000억엔 투자를 계획한다. ([Ibiden][6])

### [Inference]

- 삼성전기의 핵심 알파는 “Si-Cap 단품 매출”보다 “AI 패키지 전력 무결성 레퍼런스 확보”다.
- 실리콘 커패시터는 MLCC를 전면 대체하기보다, near-die 고주파 영역을 추가로 담당하는 premium layer로 보는 것이 맞다.
- EMIB-T와 CoWoS 경쟁은 전공정 노드 경쟁보다 패키지 내부 PDN·기판·브리지·EDA 복잡도 경쟁을 키운다.

### [Speculation]

- 삼성전기 제품이 구글 TPU v8e 또는 특정 Intel EMIB-T 패키지에 최종 탑재된다는 주장은 아직 공식 확인되지 않았다.
- 삼성전기 Si-Cap이 2028년 이후 반복 계약으로 확장될지는 추가 고객·추가 모델 확인이 필요하다.
- Si-Cap 마진이 MLCC·FC-BGA보다 구조적으로 높을 가능성은 있지만, 실제 수율과 가격 조건은 비공개다.

### [Blocked]

- 계약 상대방.
- 제품별 ASP, 수량, 원가, 수율.
- 최종 칩과 패키지 내 정확한 실장 위치.
- take-or-pay 여부와 cancellation clause.
- 2029년 이후 반복 계약 여부.

[1]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract with Global Large-Scale Company"
[2]: https://www.samsungsem.com/global/product/passive-component/silicon-capacitor.do "Silicon Capacitor | Samsung Electro-Mechanics"
[3]: https://www.intel.com/content/www/us/en/foundry/packaging.html "Advanced Packaging Innovations | Intel Foundry"
[4]: https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-07/emib-product-brief.pdf "Intel Foundry EMIB Technology Brief"
[5]: https://www.synopsys.com/blogs/chip-design/accelerating-emib-t-packaging-synopsys-intel-foundry.html "Accelerating Next-Generation EMIB-T Packaging | Synopsys"
[6]: https://www.ibiden.com/company/2026/02/notice-regarding-capital-investment-plan-for-high-performance-ic-package-substrates.html "Ibiden Notice Regarding Capital Investment Plan for High-Performance IC Package Substrates"
[7]: https://www.murata.com/products/capacitor/siliconcapacitors "Silicon Capacitors | Murata"
[8]: https://cloud.google.com/tpu "Tensor Processing Units | Google Cloud"

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
