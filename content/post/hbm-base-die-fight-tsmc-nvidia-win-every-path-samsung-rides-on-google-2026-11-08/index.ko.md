---
title: "HBM 싸움터가 스택의 2.7%짜리 부품으로 옮겨 갔습니다: TSMC와 엔비디아는 어느 길에서도 이기고, 삼성의 운명은 구글의 결정 하나에 걸려 있습니다"
date: 2026-11-08T20:35:00+09:00
lastmod: 2026-11-08T20:35:00+09:00
categories: ["semiconductors", "market-analysis"]
tags: ["HBM", "베이스다이", "NVHBM", "NV링크 퓨전", "TSMC", "엔비디아", "브로드컴", "구글 TPU", "삼성전자", "SK하이닉스", "마이크론"]
series: ["Korea Semiconductor Watch"]
slug: "hbm-base-die-fight-tsmc-nvidia-win-every-path-samsung-rides-on-google-2026-11-08"
description: "HBM 베이스다이는 스택의 2.7%이지만, 이를 설계하는 쪽이 나머지 97%의 가격을 정합니다. 엔비디아·TSMC와 브로드컴 진영이 구매자를 가르고, 삼성의 2028년 영업이익 위험은 어느 경로에서도 4% 미만이며 최악 경로는 구글에 달렸습니다."
image: "cover.ko.png"
draft: false
---

HBM 스택을 열면 주목받는 쪽은 D램 칩입니다. 그 아래에는 GPU와의 연결을 맡는 로직 칩, <strong>베이스다이</strong>가 있습니다. 지금까지는 메모리 업체가 이 칩을 설계했고, 업체 간 경쟁은 D램 코어의 용량·수율·속도에서 벌어졌습니다. 이제 엔비디아, JEDEC(표준화 기구), TSMC, 마벨, 삼성이 모두 베이스다이에 로직을 더 넣고 있고, 경쟁의 무대도 함께 옮겨 가고 있습니다.

그런데 이 부품은 작습니다. 2028년 베이스다이 시장은 약 <strong>76억달러</strong>로, 저희가 가정한 HBM 시장 2,820억달러의 2.7%입니다. 이 부품이 쥐고 있는 것은 더 큽니다. 엔비디아 HBM 물량의 가격이 10% 움직이면 <strong>105억~164억달러</strong>입니다. 베이스다이는 지렛대이고, 상금은 가격을 누가 정하느냐입니다.

<strong>저희 판단: TSMC와 엔비디아는 저희가 그릴 수 있는 모든 경로에서 이깁니다. SK하이닉스는 엔비디아 프리미엄의 일부를 잃고, AMD는 모든 경로에서 불리합니다. 브로드컴·구글·삼성은 하나의 변수에 함께 걸려 있습니다. 구글이 TPU 메모리를 엔비디아 NV링크 퓨전 밖에 두느냐입니다. 저희 가정으로 삼성은 HBM의 51~76%를 비엔비디아 구매자에게 팔고, 이는 세 회사 중 가장 높으며 구글 한 곳이 그 가운데 23~47%입니다. 그래서 엔비디아 표준이 엔비디아 자기 물량 안에 머물면 삼성의 손실은 작고, 구글이 넘어가면 큽니다. 2028년 계산으로 기본 경로는 -3.8조~-6.4조원이고 최악 경로는 -23.3조원(영업이익의 3.8%)입니다. 최악 경로에서도 삼성 이익을 정하는 1차 변수는 범용 D램 가격입니다.</strong>

- 베이스다이 시장은 76억달러입니다. 엔비디아 HBM 물량의 가격 10%는 그보다 크고, 엔비디아가 설계를 가져가려는 이유가 여기에 있습니다.
- 비엔비디아는 더 이상 하나의 진영이 아닙니다. 엔비디아가 마벨에 20억달러를 투자했고(3월 31일), 미디어텍 전환사채 35억달러를 샀습니다(8월 31일). 실제 분기선은 엔비디아 생태계와 브로드컴 진영 사이에 있습니다.
- 2028년 구조에 대한 저희 주관 확률은 이원화 지속 55%, 설계 파트너·TSMC 맞춤 확산 25%, 엔비디아 표준의 구글·메타 확산 20%입니다.
- 메모리 업체가 가격 10% 인하를 점유율로 메우려면 SK하이닉스는 5.8%p, 삼성은 3.1%p, 마이크론은 2.2%p가 필요합니다. 셋을 더하면 111%여서 누군가는 점유율을 잃습니다.
- 삼성의 최악 경로 손실은 기본 경로의 약 4~6배이고, 이 비대칭은 구글에 있습니다.

## 아무도 보지 않던 칩이 싸움터가 되었습니다

HBM 스택은 로직 칩 위에 D램 칩을 쌓은 탑입니다. HBM4까지는 메모리 업체가 이 로직 칩을 설계했습니다. 지금은 여러 설계가 이 자리를 가져가려고 경쟁합니다.

- 엔비디아의 NVHBM(8월 26일 발표)은 메모리 컨트롤러를 베이스다이로 옮깁니다. JEDEC 표준의 넓은 병렬 버스를 좁은 직렬 다이 간 연결로 바꾸고, 엔비디아가 다른 회사 칩을 자기 네트워크에 연결하는 프로그램인 NV링크 퓨전 안에서 제공됩니다. 아마존 트레이니엄4가 첫 협력사입니다. 성능 수치는 회사 주장입니다.
- JEDEC의 SPHBM4(7월 13일)도 같은 방향입니다. HBM4와 같은 D램 다이에 새 인터페이스 베이스다이를 붙이고, 512개 신호를 4:1로 직렬화하며, 유기 기판을 쓸 수 있습니다.
- TSMC·GUC는 N3P 공정의 맞춤 베이스다이를 내놓았고 효율이 약 2배라고 합니다(회사 자료를 전한 보도). 마벨은 베이스다이에 2~3나노급 로직을 넣은 맞춤 HBM4E를 일괄 제공합니다. 삼성은 자체 4나노 베이스다이를 만듭니다.

모두 병렬 인터페이스를 줄이므로 베이스다이에 로직이 더 많이 들어갑니다. 그 로직을 누가 설계하느냐가 마진과 사양의 통제권을 정합니다.

## 베이스다이를 누가 설계하느냐가 마진의 주인을 정합니다

![베이스다이를 누가 설계하느냐가 마진의 주인을 정합니다. 구매자 진영 다섯 곳. 엔비디아: 2027년까지 메모리 업체, 2028년부터 엔비디아가 설계, TSMC·하이닉스 12나노급·삼성 4나노에서 제조, 메모리 업체 협상력 가장 약함. 브로드컴 진영(구글 TPU, 메타 MTIA, 오픈AI 타이탄): 메모리 업체가 표준 HBM4/4E 설계, 삼성 4·2나노 또는 TSMC의 하이닉스, 협상력 강함. 설계 하우스(AWS 트레이니엄, MS 마이아): 설계 파트너가 설계, TSMC N3P·마벨 2·3나노, 협상력 중간. AMD: 메모리 업체 설계, 삼성 4나노, 협상력 강함. HBM 회피(퀄컴, 인텔): 해당 없음, HBM 가격 밖.](/post-assets/hbm-base-die-fight-tsmc-nvidia-win-every-path-samsung-rides-on-google-2026-11-08/control.ko.svg)

누가 펜을 쥐느냐의 문제입니다. 구매자가 설계하면, 2028년의 엔비디아가 그렇듯 메모리 업체는 정해진 설계에 맞춰 코어 다이를 대는 공급자가 되고 교체하기 쉽습니다. 설계 파트너가 설계하면 로직의 가치는 파트너와 TSMC로 갑니다. 메모리 업체가 설계를 지키면, 표준 HBM4·4E나 삼성의 일괄 공급처럼 협상력이 메모리 업체에 남습니다.

TSMC는 세 경우 모두에서 대가를 받습니다. NVHBM 베이스다이, 하이닉스의 12나노급 베이스다이, 마이크론 HBM4E, N3P 기반 C-HBM4E, CoWoS 패키징이 모두 TSMC를 지납니다. TSMC를 비켜 가는 길은 삼성의 4·2나노 베이스다이, 인텔 EMIB-T 패키징, 유기 기판의 SPHBM4뿐이고, 셋 다 비엔비디아 쪽에 있습니다.

## 걸린 돈: 76억달러짜리 부품이 나머지의 가격을 정합니다

![베이스다이 시장은 76억달러이고, 엔비디아 물량 가격 10%는 그보다 큽니다. 2028년, 억달러. 베이스다이 시장 전체 76, HBM 스택 가치의 2.7%. 구글 HBM 구매가 10% 변동 102, 2027 수요의 36%. 엔비디아 HBM 구매가 10% 변동 105~164, 2027 수요의 37~58%.](/post-assets/hbm-base-die-fight-tsmc-nvidia-win-every-path-samsung-rides-on-google-2026-11-08/stake.ko.svg)

HBM 시장 2,820억달러(JP모건, 2차 인용)에 베이스다이 가치 비중 2.7%를 곱하면 76억달러입니다. 엔비디아는 수요 비중 37~58%로 2028년에 HBM을 1,050억~1,640억달러어치 사므로, 가격 10%는 105억~164억달러입니다. 구글은 비중 36%이고 가격 10%는 102억달러입니다.

엔비디아가 설계를 가져가려는 이유에 대한 저희 해석은 이렇습니다. 상금은 베이스다이 매출에 있지 않습니다. 공급사 셋이 같은 부품을 만들게 하고 가격으로 경쟁시키는 힘에 있습니다. 엔비디아가 쥐려는 가격 협상력은 TSMC의 베이스다이 시장 전체보다 큽니다.

## 엔비디아의 수: 표준을 소유한다

엔비디아의 순서는 이렇게 읽힙니다.

1. <strong>2026~27년, 표준 HBM4·4E.</strong> 메모리 업체가 베이스다이를 설계합니다. 하이닉스와 TSMC의 협업이 성능 우위를 만들었고, 하이닉스는 2026년 엔비디아 HBM의 54%를 가졌습니다(JP모건, 2차 인용).
2. <strong>2028년, NVHBM.</strong> 엔비디아가 컨트롤러와 다이 간 연결을 설계하고, 서울 언론 보도에 따르면 3사가 같은 설계를 TSMC 3나노로 만듭니다(2차). 하이닉스의 TSMC 협업 우위와 삼성의 4나노 우위가 엔비디아 물량에서 함께 사라집니다. 남는 경쟁 변수는 코어 1c 수율, 적층, 생산능력입니다. 저희 모델에서 엔비디아 물량 가격 10% 인하는 2028년 영업이익을 삼성 4.9조원, 하이닉스 6.3조원, 마이크론 2.8조원 줄입니다.
3. <strong>2029년 이후, 메모리 아래의 로직.</strong> 11월 6일 보도는 TSMC가 3D D램을 검토한다고 전합니다(사업 확정은 미확인). 하이닉스도 산호세에서 3D D램 온 로직 인력을 뽑고 미국 고객과 로직 다이를 공동 설계합니다(2차). 셀 아래 로직 층을 엔비디아와 TSMC가 설계·제조하면 메모리 업체의 몫은 셀 배열로 좁아집니다.

엔비디아는 HBM 밖의 계층도 키웁니다. 추론용 SOCAMM(LPDDR), KV 플래시, 그록 계열 SRAM 설계가 그 예입니다. 설계 통제권과 대체 수단을 함께 쥔 구매자가 협상에서 유리합니다.

## 비엔비디아는 하나의 진영이 아닙니다

![실제 분기선은 엔비디아 생태계 대 브로드컴 진영입니다. 엔비디아 생태계(NV링크 퓨전): AWS 트레이니엄4(NVHBM 첫 협력사), 마벨(지분 20억달러, 3/31), 미디어텍(전환사채 35억달러, 8/31), 알칩(2025년부터 퓨전 협력사). 브로드컴 진영: 구글 TPU(최대 비엔비디아 구매자, 2027 HBM의 36%), 메타 MTIA·TPU 임차, 오픈AI 타이탄, 브로드컴(카운터포인트 평가로 베이스다이 해법 없음). 삼성은 일괄 공급 베이스다이로 그 사이에 있습니다. 분기점은 구글이 TPU 메모리를 퓨전 밖에 두는지입니다.](/post-assets/hbm-base-die-fight-tsmc-nvidia-win-every-path-samsung-rides-on-google-2026-11-08/camps.ko.svg)

저희는 처음에 비엔비디아 수요를 네 갈래로 나눴습니다. 브로드컴 중심 하이퍼스케일러, 설계 하우스 맞춤 칩, AMD, HBM 회피입니다. 그 뒤 두 건의 거래가 지도를 바꿨습니다. 엔비디아는 3월 31일 마벨에 20억달러를 투자했고, 8월 31일에는 미디어텍의 39억달러 전환사채 가운데 35억달러를 샀습니다. 미디어텍은 자기 고객에게 NV링크 퓨전을 제공하기로 했습니다. 알칩·미디어텍·마벨은 2025년 퓨전의 첫 맞춤 연산 협력사 명단에도 있었습니다. JP모건은 마벨 투자가 마벨이 AWS의 퓨전 통합 파트너라는 점을 사실상 확인해 준다고 봅니다(분석가 해석).

그래서 설계 하우스는 더 이상 독립 진영이 아닙니다. 실질적인 분기선은 엔비디아 생태계와 브로드컴 진영 사이에 있습니다.

- <strong>브로드컴 진영이 가장 큰 비엔비디아 수요입니다.</strong> 알파벳 한 곳이 2027년 HBM 수요의 36%입니다(모건스탠리). 브로드컴의 CoWoS 배분은 2027년 23만 장에서 35만 장으로 늘어납니다(JP모건, 보도). 이 진영은 아직 메모리 업체가 설계한 표준 HBM을 쓰고, 삼성의 일괄 공급이 가장 잘 팔리는 곳입니다. 보도로는 삼성이 구글 HBM3E의 60% 이상을 맡았고, 오픈AI 타이탄 HBM4를 독점하며, 미디어텍의 차기 구글 TPU에 2나노 메모리 I/O 다이를 댑니다(모두 2차, 주장). 카운터포인트는 브로드컴을 엔비디아가 붙지 않은 마지막 대형 설계 하우스로 보고 베이스다이 해법이 없다고 평가합니다(분석가 견해). 삼성의 4·2나노 베이스다이가 메울 수 있는 공백입니다.
- <strong>AMD는 표준 HBM의 가장 큰 단일 칩 고객이고 삼성의 1차 고객입니다.</strong> MI455X는 HBM4 12스택 432GB를 씁니다. 3월 18일의 AMD·삼성 합의는 이 이야기에서 1차 출처로 확인된 유일한 공급 관계이며 파운드리 협력 논의를 포함합니다. AMD는 2027년 수요의 12.1%입니다(모건스탠리).
- <strong>HBM 회피는 HBM 프리미엄의 상한을 만듭니다.</strong> 퀄컴 AI200은 카드당 LPDDR 768GB, 인텔 크레센트 아일랜드는 LPDDR5X 160GB를 씁니다. 비트는 D램에 남지만 HBM 가격 구조 밖입니다. 수주 규모는 아직 작습니다.

분기점은 구글입니다. 구글은 공급사(삼성·하이닉스), 설계(브로드컴·미디어텍), 패키징(TSMC, 2027년부터 인텔 EMIB-T, 2028년 TPU 300만 개 이상을 인텔에 예약했다는 보도)을 모두 둘 이상으로 나눕니다. 구글의 차기 TPU를 설계하는 미디어텍이 이제 퓨전 안에 있고, 알파벳도 같은 사채에 참여했습니다. 엔비디아 표준으로 가는 통로가 열린 것이지 결정이 난 것은 아니므로 저희 확률은 그대로 둡니다.

## 삼성은 비엔비디아 구매자 비중이 가장 높습니다

![삼성은 세 회사 중 비엔비디아 비중이 가장 높습니다. 메모리 업체별 HBM 중 비엔비디아 구매자 몫, 가정 네 가지, %. 삼성 51~76, 그중 구글 23~47. SK하이닉스 34~61. 마이크론 31~49. 네 가지 가정 모두 순서는 같습니다.](/post-assets/hbm-base-die-fight-tsmc-nvidia-win-every-path-samsung-rides-on-google-2026-11-08/exposure.ko.svg)

산식은 구매자별 2027년 수요 비중에 그 구매자 안의 공급사 배분을 곱한 값입니다. 배분은 보도로 고정한 가정입니다. 엔비디아(삼성 28%, 하이닉스 52%, 마이크론 20%), 구글(55·40·5), AMD(60·20·20), 기타(35·45·20)입니다. 엔비디아 수요 비중은 37%(모건스탠리)와 58% 두 가지로 돌렸고, 구글 물량이 그대로이거나 하이닉스 쪽으로 옮겨 가는 경우를 나눴습니다.

순서는 바뀌지 않습니다. 비엔비디아 비중은 삼성, 하이닉스, 마이크론 순으로 큽니다. 이 가정에서 나오는 점유율(삼성 33~43%, 하이닉스 43~50%, 마이크론 15~17%)은 가정의 결과이고 가정을 검증하지는 않습니다.

NVHBM의 도달 범위도 같은 표에서 나옵니다. 엔비디아만이면 수요의 37%이고, 아마존(약 5% 가정)을 더하면 42%, 구글까지 더하면 78%입니다. 구글이 엔비디아 표준을 채택하면 삼성 HBM의 약 75%가 그 아래로 들어갑니다. 엔비디아만일 때는 25%입니다. 네 경우 전체로는 70~81%입니다. 각 구매자의 수요가 모두 옮겨 간다고 가정했습니다.

- <strong>SK하이닉스</strong>는 엔비디아 비중이 커서 엔비디아가 공급사를 중립화할 때 프리미엄을 가장 크게 잃습니다.
- <strong>삼성</strong>의 위험은 구글과 브로드컴의 결정에 몰려 있습니다. 구글의 NVHBM 채택, TPU HBM4·4E 배분의 하이닉스 쏠림, 브로드컴 맞춤 베이스다이의 TSMC N3P 선택이 방아쇠입니다.
- <strong>마이크론</strong>은 엔비디아 노출이 크지만, 3위 공급사라 표준화가 인증 장벽을 낮추는 이득도 있습니다.

## 경로별로 삼성이 치르는 비용

![경로별로 삼성의 2028 영업이익에 미치는 영향. 현 구조 대비 변화, 조원. 이원화 지속(55%): -6.4~-3.8, 영업이익의 0.6~1.0%. 설계 파트너·TSMC 맞춤 확산(25%): -16.0~-8.0, 1.3~2.6%. 엔비디아 표준이 구글로 확산(20%): -23.3, 3.8%. 확률 가중: -10.5, 약 1.7%. 상쇄: 수요 5~10%p가 비엔비디아로 이동하면 +3.1~+6.2.](/post-assets/hbm-base-die-fight-tsmc-nvidia-win-every-path-samsung-rides-on-google-2026-11-08/paths.ko.svg)

| 경로 | 내용 | 저희 확률 | 판단 근거 | 신호 |
|---|---|---:|---|---|
| 이원화 지속 | 엔비디아·아마존은 NVHBM, 구글·메타·오픈AI·AMD는 표준·일괄 공급 HBM | 55% | 구글·브로드컴은 자체 연결망이 있고 브로드컴의 메타 계약이 2029년까지여서 엔비디아에 사양을 넘길 유인이 약합니다. AMD는 경쟁사가 통제하는 표준을 채택할 유인이 약합니다 | 구글·메타의 NVHBM 무발표, 브로드컴 맞춤 HBM이 메모리 업체 설계 유지 |
| 설계 파트너·TSMC 맞춤 확산 | 비엔비디아도 C-HBM4E·마벨형 맞춤으로 가서 메모리 업체가 어디서나 코어 다이 공급자 | 25% | N3P의 약 2배 효율과 마벨의 'HBM이 XPU 원가의 50% 초과'가 구매자의 맞춤 동기를 키웁니다 | 브로드컴·구글의 TSMC N3P 맞춤 베이스다이 채택, 메타 MTIA 맞춤 HBM |
| 엔비디아 표준 확산 | 구글 또는 메타가 NV링크 퓨전과 NVHBM 채택 | 20% | 아마존이 이미 갔고 엔비디아가 구글까지 넓히려 합니다(2차). 반대로 구글은 EMIB-T·미디어텍·삼성 2나노로 공급망을 넓히는 중입니다 | 12월 2일 협력사 발표, 구글 차기 TPU 메모리 사양 |

마벨과 미디어텍이 퓨전 안에 들어갔으므로 둘째 경로의 상당 부분이 엔비디아 생태계 안에서 일어날 수 있습니다. 확률은 유지하지만, 삼성에 불리한 두 경로(합계 45%)는 하나의 위험으로 읽는 것이 맞습니다.

경로별 비용은 삼성 2028년 HBM 매출 990억달러(시장 2,820억달러, 점유율 35%), 점유율 1%p당 영업이익 2.66조원, 영향 물량 가격 10% 인하, 스택의 2.7%·기여이익률 60%인 베이스다이를 가정해 계산했습니다.

- <strong>이원화 지속:</strong> 삼성 HBM의 29~48%(엔비디아·아마존 물량)가 가격 10%를 잃습니다. -3.8조~-6.4조원이고 2028년 영업이익의 0.6~1.0%입니다.
- <strong>설계 파트너 확산:</strong> 위 비용에 베이스다이 파운드리 기여이익 1.55조원을 더하고, 일괄 공급 차별을 잃어 점유율 1~3%p를 잃습니다. -8.0조~-16.0조원이고 1.3~2.6%입니다.
- <strong>엔비디아 표준 확산:</strong> 물량의 75%가 가격 10%를 잃고(10.0조원), 구글 내 삼성 점유율이 55%에서 40%로 떨어지며(시장 5.4%p, 14.4조원), 구글 베이스다이 1.0조원이 사라집니다. 이미 잃은 물량에 가격 손실을 두 번 센 2.1조원은 뺍니다. 약 -23.3조원이고 3.8%입니다.
- <strong>확률 가중:</strong> 범위 중간값 기준 약 -10.5조원이고 1.7%입니다.

기본 경로의 손실이 작은 이유는 손실이 삼성 비중이 가장 작은 곳(엔비디아 물량의 28%)에 몰리고 성장은 삼성 비중이 가장 큰 곳(비엔비디아 물량의 51%)에서 나오기 때문입니다. 수요가 엔비디아에서 비엔비디아로 5%p 옮겨 가면 삼성 점유율이 1.2%p, 영업이익이 3.1조원 늘고, 10%p면 2.3%p와 6.2조원입니다. 카운터포인트는 ASIC용 HBM 수요가 2028년까지 여러 배로 늘 것으로 봅니다(2차). 이 이동이 실제로 일어나면 기본 경로의 가격 손실을 일부 또는 전부 상쇄합니다. 일어나지 않으면 기본 경로의 순효과는 음수입니다.

꼬리는 최악 경로입니다. 구글이 엔비디아 표준으로 넘어가거나 HBM4E 배분을 하이닉스 쪽으로 기울이면 피해는 기본 경로의 약 4~6배입니다.

파운드리 쪽 영향도 있습니다. 기본 경로에서 삼성은 비엔비디아 물량의 베이스다이 파운드리를 유지해 2028년 사내 매출 약 2.6조원(아마존 제외)과 기여이익 약 1.55조원을 얻습니다. 저희 추정 2026년 파운드리·LSI 손실 3.92조원의 약 40%에 해당합니다. 둘째·셋째 경로에서는 이 매출이 줄어 파운드리 흑자 전환의 근거 하나가 약해집니다.

세 경로 모두 2028년 영업이익의 0~4% 안에 있습니다. 삼성 이익을 정하는 1차 변수는 여전히 범용 D램 가격이고 HBM 구조는 2차 변수입니다. 다만 삼성과 하이닉스의 상대 평가를 가르는 항목 가운데서는 가장 큰 축에 듭니다.

삼성의 HBM 논리는 조준점이 바뀝니다. HBM4에서 삼성은 1c 코어와 자체 4나노 베이스다이로 하이닉스의 TSMC 12나노급보다 선단 로직을 내세웠고, HBM 점유율은 1Q26 21%에서 2Q26 33%로 올랐습니다(카운터포인트). NVHBM에서는 베이스다이가 모두 TSMC 3나노로 통일되고 하이닉스도 HBM4E부터 1c로 옮깁니다. 엔비디아 물량에서 삼성의 무기는 코어 수율, 생산능력, 적층으로 좁아집니다. 이제 이야기의 중심은 비엔비디아 구매자에게 하는 표준·일괄 공급이고, 이 사업은 엔비디아 밖에서만 성립합니다.

## 어느 경로에서 누가 이기나

![어느 경로에서 누가 이기나. 저희 판단, 큰 수혜에서 큰 위협까지. 엔비디아: +, 0, ++. TSMC: +, ++, +. 브로드컴: +, -, --. 마벨·미디어텍: 0, +, +. 구글: +, +, -. 아마존: +, 0, +. 삼성: -, --, ---. SK하이닉스: -, 0, -. 마이크론: 0, 0, +. AMD: 세 경로 모두 -.](/post-assets/hbm-base-die-fight-tsmc-nvidia-win-every-path-samsung-rides-on-google-2026-11-08/scorecard.ko.svg)

TSMC와 엔비디아는 어느 경로에서도 잃지 않습니다. AMD는 세 경로 모두에서 불리합니다. 브로드컴과 삼성은 같은 방향으로 움직입니다. 두 회사 모두 기본 경로에서는 지키고 나머지 두 경로에서는 잃습니다.

| 회사 | 얻는 것 | 잃을 수 있는 것 | 판정을 뒤집는 신호 |
|---|---|---|---|
| 엔비디아 | 베이스다이 사양 통제. 3사가 같은 설계를 만들어 교체 비용이 낮아짐. 퓨전으로 아마존·마벨·미디어텍·알칩을 묶음 | TSMC 3나노 의존 확대. 비엔비디아가 메모리 업체 설계나 SPHBM4에 남으면 NVHBM은 자기 진영에 갇힘. 첫 세대 직렬 인터페이스 실행 위험 | 12월 2일 협력사 명단에 구글·메타가 없으면 수혜가 자기 물량으로 한정 |
| TSMC | NVHBM 3나노, 하이닉스 12나노급, 마이크론 HBM4E, C-HBM4E N3P, CoWoS. 베이스다이로 고객이 더 고착 | 구글 EMIB-T·인텔 패키징, 유기 기판 SPHBM4, 삼성 2나노 I/O 다이. 모두 비엔비디아 쪽 | 인텔의 구글 EMIB-T 확정, 브로드컴 맞춤 베이스다이의 삼성 채택 |
| 브로드컴 | 엔비디아가 붙지 않은 마지막 대형 설계 하우스(카운터포인트 견해). 구글·메타·오픈AI가 엔비디아 밖에 남는 주된 선택지 | 베이스다이 해법 없음. 베이스다이가 차별점이 되면 삼성 일괄 공급이나 TSMC에 의존. 구글의 두 번째 TPU 설계사 미디어텍이 퓨전 안으로 들어감 | 구글·메타의 퓨전 참여. 브로드컴 회계 4분기 콜의 베이스다이 파트너 언급 |
| 마벨·미디어텍·알칩·GUC | 마벨·미디어텍은 엔비디아 자본과 퓨전 접근권을 얻고도 다른 고객용 맞춤 칩을 계속 설계. GUC는 C-HBM4E | 마벨의 자체 맞춤 HBM이 같은 고객을 놓고 NVHBM과 경쟁. 미디어텍은 구글과 엔비디아 사이 신뢰 관리 필요 | 미디어텍 Icefish의 연결 방식(퓨전 대 구글 자체망) |
| 구글 | 공급 계층을 모두 둘 이상으로 나눈 최대 비엔비디아 구매자라 협상력이 큼 | NVHBM이 사실상 표준이 되면 독자 사양 유지 비용 증가. 공급 부족기 배정 우선순위 | 퓨전에 참여하면 원가는 얻고 사양 독립성은 잃음 |
| 메타 | 엔비디아 GPU, 구글 TPU(임차 보도, 2027 구매 협상), 브로드컴 MTIA(2029년까지) 세 선택지 | MTIA 물량이 작아 맞춤 HBM 배정에서 약함 | TPU 구매 확정이면 브로드컴 진영 확대. 퓨전 채택이면 엔비디아 경로 |
| 마이크로소프트 | 얻는 것이 적음. 엔비디아의 HBM 원가 절감이 GPU 가격에 반영될지는 불확실 | 마이아 200은 하이닉스 HBM3E 단독(보도). 자체 칩 물량이 작아 하이퍼스케일러 중 맞춤 HBM 협상력이 가장 약함. 마이아 300은 2027년 HBM4 8스택 288GB, 공급사 미공개 | 마이아 300 공급사·설계 파트너 공개 |
| 아마존 | 트레이니엄4가 퓨전·NVHBM 채택. 공급 안정, 원가, 엔비디아 랙 호환 | 메모리 컨트롤러 설계를 엔비디아에 넘겨 사양 독립성 상실. UALink 병행으로 일부 보완 | 트레이니엄5의 NVHBM 유지 여부 |
| 삼성 | 비엔비디아 비중 51~76%. 브로드컴의 베이스다이 공백을 메울 수 있는 유일한 메모리 업체. AMD 합의(1차). 중립화되면 엔비디아 물량의 점유율 회복 여지 | 구글의 선택(-23.3조원 경로). 설계 파트너 경로의 일괄 공급 차별 상실. 미디어텍의 퓨전 편입 | 브로드컴의 삼성 베이스다이 채택(수혜), 구글·메타 퓨전 채택(위협) |
| SK하이닉스 | 엔비디아 1위(54%, 2026). TSMC 협업. 마이크로소프트 단독 공급 보도. 3D D램 온 로직 공동 설계 | NVHBM이 TSMC 우위를 지움. 엔비디아 물량 가격 10%가 55억~85억달러. 점유율이 생산능력·수율 순으로 수렴해 52% 유지가 어려움 | 구글 HBM4E의 하이닉스 쏠림, 1c 수율 우위 |
| 마이크론 | 표준화가 인증 장벽을 낮춤. TSMC 베이스다이로 어느 진영에도 대응 | 구글·브로드컴 진영 노출이 작아 비엔비디아 성장 몫이 작음. 엔비디아 물량 가격 하락 | 12월 콜의 구글 맞춤 HBM4E 진입 언급 |
| AMD | 삼성과 1차 공시로 확인된 공급 관계. 표준 HBM4 12스택 | NVHBM의 주장 대역폭 30%↑·전력 15%↓와 원가 절감이 엔비디아와의 격차를 벌림. 공급사 협상력이 강해 구매자로서 불리 | AMD의 삼성 베이스다이 맞춤 HBM 채택 |

인텔은 구글 EMIB-T로 패키징 우회로를 얻지만 규모가 작고 하이닉스 인증을 기다립니다. 퀄컴은 LPDDR 설계로 HBM 프리미엄을 피하므로 HBM이 비쌀수록 이득이지만, 엔비디아가 HBM 원가를 낮추면 그 이점이 줄어듭니다.

## 메모리 3사: 중립화의 부담은 고르지 않습니다

![가격 10% 인하를 점유율로 메우려면: 합계가 맞지 않습니다. 엔비디아 HBM 물량 안의 현재 점유율 대 매출을 지키는 데 필요한 점유율. 삼성 28에서 31.1. SK하이닉스 52에서 57.8. 마이크론 20에서 22.2. 세 회사 합계 100에서 111.1로 100% 상한을 넘습니다.](/post-assets/hbm-base-die-fight-tsmc-nvidia-win-every-path-samsung-rides-on-google-2026-11-08/offset.ko.svg)

NVHBM에서는 3사가 같은 설계를 만들기 때문에 엔비디아 안의 점유율이 코어 1c 수율과 생산능력 쪽으로 수렴합니다. 엔비디아 물량 가격 10% 인하는 수요 비중 37~58% 범위에서 삼성에 30억~46억달러, 하이닉스에 55억~85억달러, 마이크론에 21억~33억달러의 손실입니다. 이를 점유율만으로 메우려면 삼성은 3.1%p, 하이닉스는 5.8%p, 마이크론은 2.2%p가 더 필요합니다.

세 필요치를 더하면 111.1%입니다. 점유율의 합은 100%이므로 이 일은 일어날 수 없습니다. 누군가는 점유율을 내놓아야 하고, 수율·생산능력 수렴은 가장 큰 점유율(52%)을 가진 하이닉스를 가리킵니다. 그래서 하이닉스는 가격과 점유율을 모두 잃을 가능성이 크고, 삼성과 마이크론은 작은 점유율 증가로 가격 인하를 메울 수 있습니다. 매출 기준 계산이며 마진과 생산능력 제약은 넣지 않았습니다. 2027~28년 공급 부족기에는 배정이 점유율을 정합니다.

## 저희 판단을 바꿀 조건

![다음 확인 일정. 2026년 12월 2일 엔비디아 GTC DC: 구글·메타·미디어텍 고객의 퓨전·NVHBM 참여. 12월 중순(추정) 브로드컴 회계 4분기: 맞춤 HBM 베이스다이 제작사. 12월 17일(추정) 마이크론 회계 1분기: 맞춤 HBM4E 고객. 2027년 1월 14일(관행) TSMC 4분기. 1월 27~28일 SK하이닉스·삼성 4분기. 수시: 메타 TPU 구매 확정, MS 마이아 300 공급사 공개.](/post-assets/hbm-base-die-fight-tsmc-nvidia-win-every-path-samsung-rides-on-google-2026-11-08/calendar.ko.svg)

| 시점 | 확인할 것 | 기본값 | 판단이 움직이는 조건 |
|---|---|---|---|
| 2026년 12월 2일 | 엔비디아 GTC DC: NVHBM·퓨전 협력사, 구글·메타·미디어텍 고객 포함 여부, 파인만 메모리 | 신규 대형 협력사 없음 | 구글·메타가 명단에 오르면 엔비디아 표준 확산 경로가 약 15%p 오르고(저희 추정) 브로드컴·삼성을 함께 낮춥니다 |
| 12월 중순(추정) | 브로드컴 회계 4분기: AI 매출, 고객별 맞춤 칩, HBM·패키징 언급 | HBM 구조 무언급 | 삼성 베이스다이 언급은 비엔비디아 표준 진영을 강화하고, TSMC 맞춤 베이스다이는 설계 파트너 경로를 다시 엽니다 |
| 12월 17일(추정) | 마이크론 회계 1분기: 맞춤 HBM4E 고객, ASIC 비중 | ASIC 고객 확대 언급 | 구글 진입 언급이면 배분 가정을 고칩니다 |
| 2027년 1월 14일(관행) | TSMC 4분기: CoWoS 배분, C-HBM4E 채택, 3D D램 질의 | 무언급 | 맞춤 베이스다이 고객이 늘면 설계 파트너 경로가 약 5%p 오릅니다(저희 추정) |
| 2027년 1월 27~28일 | SK하이닉스·삼성 4분기: 맞춤 HBM4E 수주, 2나노 베이스다이 | 고객명 비공개 | 삼성의 구글·브로드컴 수주 언급이면 이원화 경로를 지지합니다 |

## 자료와 한계

- 구매자 안의 공급사 배분은 익명 보도로 고정한 가정입니다. 구글 내 삼성 60%는 HBM3E 시절 보도이고 HBM4·4E 배분은 알 수 없습니다. 결과는 순서와 범위로 읽어 주십시오.
- 2027년 엔비디아 수요 비중 추정은 37~61%로 갈립니다. 비트 수요, 계약 물량, 출하 기준이 섞여 있기 때문입니다. 37%와 58% 두 끝으로 계산했고 중간값을 고르지 않았습니다.
- 페이지를 직접 열지 않고 검색 요약으로 확인한 항목이 많습니다. 1차 출처로 확인된 공급 관계는 AMD·삼성 합의뿐입니다. 엔비디아의 마벨·미디어텍 투자는 원 발표문을 열지 않았고, 마벨과 마이아 300의 관계는 미확인입니다. 메타의 TPU 구매는 보도상 협상 단계입니다.
- 시장 규모, 베이스다이 가치 비중, 수요 분포는 분석 전체에 쓴 가정입니다. 경로, 확률, 판정표의 부호는 저희 주관 판단입니다. 판정표는 단일 모델 계열이 만들었고 교차 검토를 받지 않았습니다. 노출 표 16칸과 가격 인하 금액은 다시 계산해 저희 리서치 노트와 일치함을 확인했습니다.
- 카운터포인트의 ASIC용 HBM 수요 증가 배수는 열지 못한 제목(봇 확인)에서 가져온 것이라 '여러 배'로만 적었습니다.
- 브로드컴의 베이스다이 관련 공식 발언, SPHBM4 지지 기업, 메타·마이아 300의 HBM4 공급사는 찾지 못했습니다.

출처:

- [AMD: 삼성·AMD 전략 협력 확대](https://newsroom.amd.com/news/samsung-and-amd-expand-strategic-collaboratio/)
- [엔비디아 블로그: NV링크 퓨전과 NVHBM(2026-08-26)](https://blogs.nvidia.com/blog/2026/08/26/nvlink-fusion-nvhbm/)
- [Tom's Hardware: 엔비디아 맞춤 NVHBM, 대역폭 30%↑·전력 15%↓](https://www.tomshardware.com/pc-components/dram/nvidia-custom-nvhbm-promises-30-percent-higher-bandwidth-15-percent-lower-power-than-commodity-hbm4e-custom-base-die-and-phy-will-be-available-to-nvlink-fusion-partners)
- [StorageReview: NVHBM은 메모리 컨트롤러를 HBM 스택 안으로 옮기고 트레이니엄4가 첫 고객](https://www.storagereview.com/news/nvidia-nvhbm-moves-the-memory-controller-into-the-hbm-stack-with-amazons-trainium4-first-in-line)
- [카운터포인트: 1조달러 병목, 베이스다이를 둘러싼 엔비디아 NVHBM의 싸움](https://counterpointresearch.com/cn/insights/the-trillion-dollar-bottleneck-nvidias-nvhbm-fight-for-base-die-blog)
- [카운터포인트: AI 서버 연산 ASIC용 HBM 수요](https://counterpointresearch.com/en/insights/HBM-Demand-for-AI-Server-Compute-ASICs-to-Grow-35x-by-2028)
- [Blocks and Files: 엔비디아가 JEDEC HBM 표준을 비켜 가다](https://blocksandfiles.com/ai-ml/2026/10/26/nvidia-sidesteps-jedec-hbm-standard/5305323)
- [Tom's Hardware: JEDEC SPHBM4 표준](https://www.tomshardware.com/pc-components/dram/jedec-releases-new-sphbm4-standard-to-slash-ai-memory-costs-narrow-512-bit-interface-enables-dropping-expensive-interposers-for-organic-substrates)
- [Tom's Hardware: TSMC·GUC의 HBM4·HBM4E·C-HBM4E 베이스다이](https://www.tomshardware.com/pc-components/dram/hbm-undergoes-major-architectural-shakeup-as-tsmc-and-guc-detail-hbm4-hbm4e-and-c-hbm4e-3nm-base-dies-to-enable-2-5x-performance-boost-with-speeds-of-up-to-12-8gt-s-by-2027)
- [Tom's Hardware: 엔비디아의 마벨 20억달러 투자](https://www.tomshardware.com/tech-industry/nvidia-invests-2-billion-in-marvell-to-deepen-nvlink-fusion-partnership)
- [DCD: 엔비디아의 마벨 20억달러 투자](https://datacenterdynamics.com/en/news/nvidia-invests-2bn-in-marvell-as-part-of-wider-nvlink-fusion-deal)
- [Network World: 엔비디아의 미디어텍 35억달러 투자](https://www.networkworld.com/article/4220808/nvidia-invests-3-5b-in-mediatek-to-extend-its-grip-on-ai.html)
- [HotHardware: NV링크 퓨전과 미디어텍 거래](https://hothardware.com/news/nvidia-nvlink-fusion-major-boost-mediatek-deal)
- [ServeTheHome: AWS 트레이니엄4의 NV링크 퓨전 채택](https://www.servethehome.com/nvidia-nvlink-fusion-tapped-for-future-aws-trainium4-deployments/)
- [TechRadar: 엔비디아의 마벨 20억달러 투자](https://www.techradar.com/pro/the-inference-inflection-has-arrived-nvidia-pumps-usd2-billion-into-chipmaker-marvell-to-boost-its-ai-factories-to-the-next-level-so-does-this-mean-itll-be-working-with-amazon-trainium-soon)
- [Tom's Hardware: 마벨 맞춤 HBM 솔루션](https://www.tomshardware.com/pc-components/dram/marvell-develops-custom-hbm-solution-that-offers-higher-performance-in-a-smaller-physical-space)
- [Tom's Hardware: 브로드컴에서 MTIA까지 맞춤 AI ASIC 분석](https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia)
- [Tom's Hardware: 메타의 신규 MTIA 칩 4종](https://www.tomshardware.com/tech-industry/semiconductors/meta-reveals-four-new-mtia-chips-built-for-ai-inference)
- [TechRadar: 메타와 구글의 대형 AI 칩 계약 가능성](https://www.techradar.com/pro/meta-and-google-could-be-about-to-sign-a-mega-ai-chip-deal-and-it-could-change-everything-in-the-tech-space)
- [TechEnclave: 마이크로소프트 마이아 300 발표](https://techenclave.com/news/items/microsoft-announces-maia-300-ai-chip-and-multi-gigawatt-deployment-plans-for-2027)
- [Korea Times: 하이닉스가 MS AI 칩의 HBM 단독 공급사로](https://www.koreatimes.co.kr/business/companies/20260127/sk-hynix-becomes-sole-supplier-of-hbm-for-microsoft-ai-chips-sources)
- [TrendForce: 삼성이 구글 TPU HBM3E의 60% 공급(보도)](https://www.trendforce.com/news/2025/12/01/news-samsung-reportedly-supplies-60-of-google-tpu-hbm3e-set-to-remain-primary-supplier-in-2026/)
- [TrendForce: 삼성 HBM4가 브로드컴 시험에서 기대 초과(보도)](https://www.trendforce.com/news/2025/12/03/news-samsung-hbm4-reportedly-beats-expectations-in-broadcom-test-set-to-lead-2026-google-tpu-supply/)
- [TrendForce: 하이닉스의 맞춤 HBM4E 선도(보도)](https://www.trendforce.com/news/2025/06/20/news-sk-hynix-reportedly-leads-custom-hbm4e-push-with-nvidia-microsoft-samsung-trails-with-hbm4/)
- [TrendForce 보도(2026-09-18)](https://www.trendforce.com/presscenter/news/20260918-13241.html)
- [Tom's Hardware: 구글이 2028년 TPU 300만 개 이상을 인텔에 예약(보도)](https://www.tomshardware.com/tech-industry/google-reportedly-books-intel-for-more-than-3-million-tpus-in-2028)
- [SamMobile: 삼성과 오픈AI의 HBM 공급](https://www.sammobile.com/news/samsung-will-exclusively-power-your-future-chatgpt-conversations/)
- [NAND Research: 퀄컴 AI200·AI250](https://nand-research.com/research-note-qualcomm-introduces-ai200-ai250-for-data-center-inference/)
- [Tom's Hardware: 인텔 크레센트 아일랜드](https://www.tomshardware.com/pc-components/gpus/intel-unveils-crescent-island-an-inference-only-gpu-with-xe3p-architecture-and-160gb-of-memory)
- [Profesional Review: 2027년 엔비디아가 HBM의 37% 통제](https://profesionalreview.com/2026/10/02/nvidia-controlara-37-memoria-hbm-2027)

<strong>독자께 두 가지를 여쭙니다. 댓글로 남겨 주세요.</strong>

<strong>1. 12월 2일 GTC DC에서 엔비디아는 누구를 NVHBM·퓨전 협력사로 올릴까요? A. 구글도 메타도 아님. B. 메타만. C. 구글만. D. 둘 다.</strong>

<strong>2. 베이스다이 표준화로 가장 잃을 메모리 업체는 어디입니까? A. SK하이닉스. B. 삼성. C. 마이크론. D. 없음, 엔비디아의 가격 결정력 문제일 뿐입니다.</strong>

연구와 정보 제공 목적이며 투자 조언이 아닙니다. 확률, 범위, 부호는 분석 가정이지 매매 지시나 개인별 포트폴리오 결정이 아닙니다. 수치는 기준일이 있는 자료입니다. 앤트로픽은 구글 TPU와 AWS 트레이니엄의 대형 사용자이고 둘 다 이 글에서 다룹니다. 자료 수집과 편집에 Anthropic의 Claude를 사용했으며, 공개 자료만 썼고 영향 크기는 판단하지 않았습니다.
