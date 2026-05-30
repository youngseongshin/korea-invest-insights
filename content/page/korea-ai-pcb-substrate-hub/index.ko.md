---
title: "AI 기판·PCB 투자 허브: FC-BGA, CCL, 삼성전기, 대덕전자, 파미셀"
slug: "korea-ai-pcb-substrate-hub"
date: 2026-05-05T23:20:00+09:00
aliases: ["/ko/ai-pcb/", "/ko/pcb/", "/ko/fc-bga/", "/ko/ccl/", "/ko/ai-substrate/", "/ko/page/korea-ai-pcb-substrate-hub/"]
layout: "page"
description: "AI 기판·PCB 투자 허브. FC-BGA, MLB, CCL, 저유전율 소재, 삼성전기, 대덕전자, 두산전자BG, 코오롱인더, 파미셀을 한곳에 묶어 GPU·CPU·NIC·스위치 ASIC이 만드는 AI 시스템 병목을 정리한다."
lastmod: 2026-05-31T09:00:00+09:00
---

## 한 줄 결론

AI 기판 투자는 "GPU 다음 테마"가 아니라 <strong>AI 시스템 전체의 공통 병목</strong>이다. GPU, CPU, DPU, NIC, 스위치 ASIC, 메모리 모듈이 함께 늘어날수록 FC-BGA, MLB, CCL, 저유전율 소재 수요가 같이 커진다.

---

## 이 허브가 답하는 질문

| 검색 질문 | 빠른 답 | 읽을 글 |
|---|---|---|
| 왜 한국에 반도체 기판 회사가 이렇게 많나요? | 미국·유럽이 설계·소프트웨어·장비에 집중하는 동안, 고객 인증과 수율 데이터가 필요한 기판 양산은 한국·일본·대만에 축적됐다. 한국의 강점은 삼성전자·SK하이닉스 고객 기반, 모바일·메모리 양산 경험, 빠른 투자 실행력이다. | [Why Korea 1편: 한국 반도체 기판 경쟁력](/ko/post/why-korea-semiconductor-substrate-competitive-edge-2026-05-07/) |
| AI 기판 투자의 핵심은 무엇인가요? | GPU 하나가 아니라 rack-scale 시스템 전체가 칩과 보드를 늘린다. 기판은 모든 칩 확장의 공통 분모다. | [AI PCB와 기판 thesis](/ko/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) |
| AI 칩 설계에서 왜 FC-BGA와 고속 PCB가 중요해졌나요? | AI 칩 성능은 초당 연산량보다 데이터를 덜 움직이고, 메모리와 연산칩을 더 가까이 붙이는 데 달려 있다. 그래서 HBM 아래에서 FC-BGA, 고다층 PCB, 전력 안정화 부품이 성능 병목으로 올라온다. | [엔비디아 이후 AI 반도체 병목](/ko/post/ai-chip-design-data-movement-fcbga-bottleneck-2026-05-24/) |
| 마벨 Q1 FY2027 실적은 AI 기판 thesis를 강화했나요? | 그렇다. Marvell이 custom XPU, 51.2T Ethernet switch, 800G/1.6T optics, scale-up networking을 성장축으로 제시하면서 GPU용 기판뿐 아니라 network ASIC·XPU attach용 FCBGA와 고속 PCB 난이도가 같이 올라간다. | [마벨 Q1 FY2027 실적과 한국 반도체](/ko/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/) |
| 메모리 ASP가 2027년 꺾이면 AI 기판도 같이 피크아웃인가요? | 아니다. JP모간 피크아웃은 주로 범용 메모리 가격 상승률에 적용된다. 골드만의 2030년 토큰 수요가 맞으면 서버·랙 복잡도는 계속 올라가, 기판 면적·전력 안정화·FC-BGA·MLCC 수요는 메모리 가격 모멘텀과 별개로 이어질 수 있다. | [골드만 토큰 수요 vs JP모간 메모리 ASP 피크아웃](/ko/post/goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31/) |
| 한국 AI 기판 생태계에서 어떤 회사를 비교해야 하나요? | 기판 제조사만 보면 부족하다. 삼성전기·대덕전자·이수페타시스·심텍·코리아써키트에 두산전자BG, 코오롱인더, 파미셀, 티엘비, 태성까지 같이 봐야 한다. | [한국 AI 기판·PCB 생태계 10개사](/ko/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) |
| 삼성전기는 AI 기판주인가요? | 삼성전기는 FC-BGA와 MLCC를 함께 가진 한국 대형 부품주다. AI 서버가 고성능 기판과 전력 안정 부품을 더 많이 쓰면서 수혜를 받는다. | [삼성전기 AI 인프라 리레이팅](/ko/post/samsung-electro-mechanics-ai-infrastructure-rerating-2026-04-21/) |
| 삼성전기 목표가 130만원은 어떤 의미인가요? | 미래에셋의 130만원은 2028F EPS에 2017년 MLCC 쇼티지 초기 멀티플 37배를 적용한 리레이팅 프레임이다. 현재가는 이미 정상 업사이클 상단을 넘어선 만큼 MLCC 가격 인상과 FC-BGA 마진 확인이 중요하다. | [삼성전기 목표가 130만원 분석](/ko/post/samsung-electro-mechanics-mirae-tp-1300000-valuation-frame-shift-2026-05-07/) |
| 삼성전기는 무라타·이비덴 중 누구와 비교해야 하나요? | 한쪽 피어로만 보면 답이 어긋난다. 삼성전기는 MLCC와 FC-BGA를 동시에 가진 하이브리드 챌린저이고, 현 주가 101만원은 2027E OP 2.7조원 이상과 패키지 OPM 20% 접근을 요구한다. | [삼성전기 하이브리드 챌린저](/ko/post/samsung-electro-mechanics-hybrid-challenger-2026-05-17/) |
| 삼성전기 실리콘 커패시터 1.5조원 계약은 뭘 바꿉니까? | '수주 한 건'이 아니라 <strong>MLCC·기판 회사 → AI 패키지 전력 안정화 부품사로 분류가 바뀌는 사건</strong>. 2년 1.557조원(연환산 7,785억원, 2025년 매출의 6.9%), 2027년부터 2028년까지 인식. FC-BGA·MLCC·Si-Cap 통합 공급자가 글로벌에서 삼성전기 한 곳. 다만 5/21 프리마켓 1,109,000원은 이미 상당히 반영. | [Si-Cap 1.5조원 — 분류가 바뀌는 사건](/ko/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) |
| 인텔 EMIB-T와 삼성전기 실리콘 커패시터는 어떻게 연결되나요? | EMIB-T는 칩렛·HBM 연결에 TSV 기반 전력 전달까지 더하는 2.5D 패키징이고, Si-Cap은 AI 패키지 내부 전압 흔들림을 줄이는 die-near PDN 부품이다. 공식 확인은 1.5조원 Si-Cap 계약이고, 구글 TPU·EMIB-T 연결은 아직 추정 영역이다. | [삼성전기 Si-Cap과 인텔 EMIB-T](/ko/post/samsung-electro-mechanics-silicon-capacitor-emib-t-ai-package-pdn-2026-05-28/) |
| 삼성전기 시총 100조원은 AI 기판 thesis에 어떤 의미인가요? | 삼성전기가 단순 기판주가 아니라 <strong>AI 패키지 전력무결성 + FC-BGA 플랫폼</strong>으로 재분류됐다는 신호다. 현대차 시총 추월은 가능하지만, 150조원 유지에는 2028년 OP 4조원대와 전사 OPM 20% 접근이 필요하다. | [삼성전기 시총 100조 돌파](/ko/post/samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26/) |
| 삼성전기가 현대차 체급에 도달한 뒤 무라타·이비덴보다 프리미엄을 받을 수 있나요? | 논거는 있다. Si-Cap 장기계약, MLCC/FC-BGA/Si-Cap bundle, AI package PDN supplier 재분류가 프리미엄을 만든다. 다만 시총 138조원은 이미 무라타의 94%이고, 추가 상승은 반복 수주와 2027~2028년 이익 bridge가 필요하다. | [삼성전기 시총 138조원과 peer premium](/ko/post/samsung-electro-mechanics-market-cap-murata-ibiden-premium-2026-05-28/) |
| MLCC·FC-BGA는 GPU/HBM처럼 높은 멀티플을 받아야 하나요? | 병목은 맞지만 플랫폼 독점은 아니다. FC-BGA와 MLCC는 capex, 감가상각, 범용 제품 사이클, 고객별 qualification 리스크가 있어 GPU/HBM 멀티플을 그대로 적용하면 위험하다. 삼성전기 thesis는 맞지만 현재 가격은 반복 수주와 고마진을 요구한다. | [AI 인프라 멀티플 지도](/ko/post/ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31/) |
| AI 서버 수동소자 병목은 기판 thesis와 어떻게 연결되나요? | AI 서버 기판은 칩을 얹는 바닥판이고, MLCC·실리콘 커패시터·인덕터는 그 위에서 전압 흔들림을 잡는 전력 안정화 층이다. GPU/HBM 패키지가 커질수록 FC-BGA와 전력무결성 부품은 같은 시스템 병목이 된다. | [AI 서버 수동소자 병목: 삼성전기 기술 설명](/ko/post/ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26/) |
| MLCC와 실리콘 커패시터는 같은 부품인가요? | 둘 다 커패시터의 한 종류지만 위치와 용도가 다르다. MLCC는 PCB 위와 칩 주변에 넓게 쓰이는 초소형 세라믹 전원 안정 부품이고, 실리콘 커패시터는 AI GPU·HBM 패키지 내부 또는 칩 바로 근처에서 순간 전력 흔들림을 잡는 고성능 보완재다. | [MLCC와 실리콘 커패시터 이해하기](/ko/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/) |
| 파미셀은 왜 AI CCL 소재주로 보나요? | 파미셀은 PCB 제조사가 아니라 두산전자BG의 고부가 CCL 사이클에 연결된 저유전율 소재 공급사다. | [파미셀 1편](/ko/post/pamicell-doosan-electro-bg-proxy-rediscovery-2026-04-30/) |
| 파미셀 논거는 단기 이벤트인가요, 산업 사이클인가요? | KRX 업종 재분류, 두산전자BG OPM, CCL 공급 부족 논의가 겹치면서 단일 분기가 아니라 12-24개월 산업 사이클로 읽어야 한다. | [파미셀 2편](/ko/post/pamicell-four-layer-progress-and-fifth-cycle-layer-2026-05-03/) |
| 파미셀은 이미 AI 기판 소재주로 재분류됐나요? | 펀더멘털은 전자소재주에 가깝지만 수급은 아직 아니다. 5/4~5/18 파미셀은 -17.9%, 외인+기관 +16억에 그친 반면 대덕전자는 +22.7%, 외인+기관 +648억을 받았다. 이 재분류 갭이 핵심이다. | [파미셀 수급분석](/ko/post/pamicell-supply-demand-analysis-recognition-gap-2026-05-18/) |
| 해외 개인투자자는 한국 AI 기판주를 어떻게 발견하게 되나요? | IBKR·해외 증권사 접근성이 개선되면 AI 기판은 국내 공급망 테마를 넘어 해외 검색 수요가 붙는 중소형주 클러스터가 될 수 있다. | [해외 투자자용 한국 주식 허브](/ko/page/korea-stocks-foreign-investors-hub/) |
| 삼성전자·SK하이닉스 HBM과 기판은 어떻게 연결되나요? | HBM은 메모리 병목이고, 기판은 GPU·CPU·네트워크 칩을 모두 실장하는 물리적 병목이다. 두 레이어는 경쟁이 아니라 같은 AI 시스템의 다른 층이다. | [HBM·한국 반도체 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/) |
| 해성디에스는 왜 PCB 클러스터에 같이 보나요? | 해성디에스는 PCB·기판 회사가 아니라 리드프레임 글로벌 2위 + DDR 패키지 기판 + AI 데이터센터 Heat Spreader second-source 옵션이 결합된 11번째 종목이다. 클러스터 내에서 유일한 비-PCB axis다. | [해성디에스: 자동차 LF에서 AI 방열부품 second-source까지](/ko/post/haesung-ds-leadframe-ai-heat-spreader-second-source-2026-05-07/) |
| 한국 광통신·CPO 관련주는 어떻게 정리되나요? | 7개사 중 진짜 CPO에 가까운 회사는 오이솔루션 하나뿐이고, 나머지는 후방 수혜이거나 테마다. 그리고 7개 중 대부분이 올해 +300~900% 올랐다. 기판 클러스터와 달리 실적이 아직 안 따라온 과열 구간이다. | [한국 광통신·CPO 밸류체인 7개사](/ko/post/korea-optical-cpo-value-chain-seven-companies-2026-05-09/) |
| 기판과 테스트 소켓을 같이 묶어도 되나요? | 안 된다. 둘 다 'AI 후공정' 수혜지만 기판은 CAPEX·물량 베타(OPM 약 12-15%), 테스트 소켓은 소모품·복잡도 베타(OPM 약 35-47%) — 마진 구조가 약 3배 차이. 보유 기간이 짧으면 기판, 1-2년이면 테스트 소켓. | [기판 vs 테스트 소켓 비교](/ko/post/ai-substrate-vs-test-socket-comparison-2026-05-15/) |

---

## 먼저 읽을 순서

| 순서 | 질문 | 글 |
|---:|---|---|
| 1 | 왜 한국에 기판 회사가 이렇게 많은가 | [Why Korea 1편: 한국 반도체 기판 경쟁력](/ko/post/why-korea-semiconductor-substrate-competitive-edge-2026-05-07/) |
| 2 | 왜 AI 기판은 "다음 테마"가 아니라 공통 병목인가 | [AI PCB와 기판 thesis](/ko/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) |
| 2+ | AI 칩 설계 관점에서 왜 데이터 이동·FC-BGA·고속 PCB가 병목인가 | [엔비디아 이후 AI 반도체 병목](/ko/post/ai-chip-design-data-movement-fcbga-bottleneck-2026-05-24/) |
| 2++ | 마벨 실적은 custom XPU·network ASIC용 기판 병목을 어떻게 확인했나 | [마벨 Q1 FY2027 실적과 한국 반도체](/ko/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/) |
| 2+++ | AI 사용량에 가격이 붙으면 FC-BGA·기판은 토큰당 비용 테제에 어떻게 연결되나 | [AI 토큰 선물과 토큰당 비용 투자 논거](/ko/post/ai-token-futures-cost-per-token-korea-semiconductor-thesis-2026-05-30/) |
| 2++++ | 같은 AI 인프라 안에서도 MLCC·FC-BGA는 왜 GPU/HBM과 다른 멀티플을 받나 | [AI 인프라 멀티플 지도](/ko/post/ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31/) |
| 3 | 한국 AI 기판 생태계 10개사를 어떻게 나눠 봐야 하나 | [한국 AI 기판·PCB 생태계 10개사](/ko/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) |
| 4 | 한국 대형주 중 기판·MLCC 앵커는 어디인가 | [삼성전기 주가가 90일 만에 두 배 오른 이유](/ko/post/samsung-electro-mechanics-ai-infrastructure-rerating-2026-04-21/) |
| 5 | 미래에셋 130만원 목표가는 어떤 멀티플 전환을 말하나 | [삼성전기 목표가 130만원 분석](/ko/post/samsung-electro-mechanics-mirae-tp-1300000-valuation-frame-shift-2026-05-07/) |
| 6 | 삼성전기는 무라타·이비덴 중 어디에 가까운가 | [삼성전기 하이브리드 챌린저: 101만원이 묻는 2027E OP 2.7조원](/ko/post/samsung-electro-mechanics-hybrid-challenger-2026-05-17/) |
| 6+ | 삼성전기 실리콘 커패시터 1.5조원 — 분류가 바뀌는 사건 | [Si-Cap 1.5조원 공급계약 분석 (5/21)](/ko/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) |
| 6++ | MLCC와 실리콘 커패시터는 어떻게 다르고 왜 AI 패키지 전력 병목인가 | [MLCC와 실리콘 커패시터 이해하기](/ko/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/) |
| 6+++ | 삼성전기 100조원은 현대차·무라타 추월의 시작인가, 이미 선반영된 가격인가 | [삼성전기 시총 100조 돌파](/ko/post/samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26/) |
| 6++++ | GPU보다 작은 수동소자가 왜 AI 서버 병목이 되는가 | [AI 서버 수동소자 병목: 삼성전기 기술 설명](/ko/post/ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26/) |
| 6+++++ | 인텔 EMIB-T와 실리콘 커패시터는 AI 패키지 전력망 병목을 어떻게 바꾸나 | [삼성전기 Si-Cap과 인텔 EMIB-T](/ko/post/samsung-electro-mechanics-silicon-capacitor-emib-t-ai-package-pdn-2026-05-28/) |
| 6++++++ | 현대차 체급에 도달한 삼성전기는 무라타·이비덴보다 높은 프리미엄을 받을 수 있나 | [삼성전기 시총 138조원과 peer premium](/ko/post/samsung-electro-mechanics-market-cap-murata-ibiden-premium-2026-05-28/) |
| 7 | 파미셀은 왜 두산전자BG CCL 소재 프록시인가 | [파미셀 분석: 두산전자BG AI CCL 소재 재평가](/ko/post/pamicell-doosan-electro-bg-proxy-rediscovery-2026-04-30/) |
| 8 | 파미셀 논거가 12-24개월 사이클로 확장됐는가 | [파미셀 2편: AI CCL 소재 전환과 산업 사이클](/ko/post/pamicell-four-layer-progress-and-fifth-cycle-layer-2026-05-03/) |
| 9 | 파미셀의 펀더멘털 전환과 수급 재분류는 왜 아직 어긋나 있나 | [파미셀 수급분석: 두산과 에스티팜 사이, 대덕전자는 아직 멀다](/ko/post/pamicell-supply-demand-analysis-recognition-gap-2026-05-18/) |
| 10 | 빅테크 AI 투자지출은 한국 공급망에 어떻게 전달되나 | [삼성전자 vs 삼성전기: 빅테크 AI 투자 재가속](/ko/post/bigtech-1q26-samsung-electronics-vs-electro-mechanics-2026-04-30/) |
| 11 | 클러스터 11번째 종목, 리드프레임에서 AI 방열부품으로 가는 unique angle | [해성디에스: 자동차 LF에서 AI Heat Spreader second-source까지](/ko/post/haesung-ds-leadframe-ai-heat-spreader-second-source-2026-05-07/) |
| 12 | AI 데이터센터의 다음 병목 — 광통신·CPO 7개사 중 진짜는 누구인가 | [한국 광통신·CPO 밸류체인 7개사 — 진짜 가까운 회사는 오이솔루션 하나뿐](/ko/post/korea-optical-cpo-value-chain-seven-companies-2026-05-09/) |
| 13 | 같은 'AI 후공정 수혜주'라도 기판과 테스트 소켓을 같이 묶으면 안 되는 이유 | [기판 vs 테스트 소켓: AI 후공정 두 가지 베타](/ko/post/ai-substrate-vs-test-socket-comparison-2026-05-15/) |

---

## AI 기판 밸류체인 지도

| 레이어 | 한국 기업 | 투자 논점 |
|---|---|---|
| 패키지 기판 | 삼성전기, 대덕전자, 코리아써키트 | GPU·CPU·ASIC용 FC-BGA와 고성능 패키지 기판. 데이터 이동 거리를 줄이고 HBM·연산칩을 묶는 핵심 바닥판 |
| 고다층 PCB / 모듈 기판 | 이수페타시스, 대덕전자, 티엘비, 심텍, 코리아써키트 | 서버 보드, 네트워크 스위치 보드, 메모리 모듈, SoCAMM. 랙 안팎의 고속 데이터 이동을 맡는 도로 |
| 메모리 패키지 기판 + 리드프레임 | 해성디에스 | DDR4·DDR5 R2R 기판 + 글로벌 LF 2위, 자동차 + 메모리 양 축 |
| CCL 본체 | 두산전자BG | AI 서버와 고속 네트워크용 고부가 동박적층판 |
| 저유전율 소재 | 코오롱인더, 파미셀 | mPPO, 저손실 수지, 경화제 등 상류 소재 |
| 전력 안정 부품 | 삼성전기, 삼화콘덴서, 아모텍, Murata 등 | AI 서버와 네트워크 장비의 MLCC 탑재량 증가. 실리콘 커패시터는 MLCC 대체가 아니라 AI GPU·HBM 패키지 내부의 초근접 전원 안정화 보완재. [수동소자 병목 설명](/ko/post/ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26/) 참조 |
| AI 패키지 방열부품 | 해성디에스 (option) | Heat slug / Heat spreader second-source 진입 옵션, Shinko·Honeywell·Jentech·I-Chiun 과점 영역 |
| AI 광통신·CPO | 오이솔루션 (핵심), 옵티코어·대한광통신·빛과전자·우리로·라이콤·코셋 (테마) | 800G/1.6T 광전송 모듈, CPO 외부 광원(ELSFP), 광섬유 — 기판처럼 시스템 부품 원가와 공급을 좌우하는 병목, 다만 실적이 아직 안 따라온 과열 구간 |

---

## FAQ — AI 기판과 한국 PCB

### AI 기판이란 무엇인가요?

AI 가속기, 서버 CPU, 네트워크 ASIC, DPU, 메모리 모듈을 실장하고 연결하는 패키지 기판과 PCB를 통칭해 부르는 투자 용어다. 대표 키워드는 FC-BGA, MLB, CCL, 저유전율 소재다.

### FC-BGA와 CCL은 같은 건가요?

아니다. FC-BGA는 반도체 칩을 실장하는 고성능 패키지 기판이고, CCL은 PCB를 만드는 기본 소재인 동박적층판이다. 고속 신호 환경에서는 저손실 CCL과 저유전율 소재가 중요해진다.

### 파미셀은 기판을 직접 만드나요?

아니다. 파미셀은 기판 제조사가 아니다. 이 허브에서 파미셀을 다루는 이유는 두산전자BG의 고부가 CCL 사이클에 연결된 상류 저유전율 소재 공급사로 보기 때문이다.

### 파미셀은 시장에서 이미 AI 기판 소재주로 거래되나요?

아직 아니다. 1Q26 저유전율 전자소재 매출 비중과 KRX 업종 변경만 보면 전자소재주가 맞지만, 5/4~5/18 수급과 가격 동조성은 여전히 두산·에스티팜·코오롱인더 쪽에 더 가깝다. 대덕전자와의 상관계수가 올라가고 외인+기관 매수가 거래대금 대비 3% 이상으로 붙어야 재분류가 시작됐다고 볼 수 있다.

### 삼성전기는 왜 이 허브의 핵심인가요?

삼성전기는 FC-BGA와 MLCC를 동시에 가진 한국 대형 전자부품사다. AI 서버가 고성능 기판과 전력 안정 부품을 더 많이 요구할수록 양쪽 모두에서 수혜를 받을 수 있다. 다만 현재 가격대에서는 단순 테마가 아니라 패키지 OPM 20% 접근과 2027E 영업이익 2.7조원 이상으로의 상향 여부가 핵심이다.

---

*이 허브는 AI 기판·PCB·CCL 분석이 새로 발행될 때마다 갱신됩니다. 메모리 제품과 KOSPI 쏠림은 [HBM 허브](/ko/page/korea-semiconductor-hbm-kospi-hub/), 반도체 장비·IP는 [반도체 장비·IP 허브](/ko/page/korea-semiconductor-equipment-ip-hub/)를 참고하세요.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
