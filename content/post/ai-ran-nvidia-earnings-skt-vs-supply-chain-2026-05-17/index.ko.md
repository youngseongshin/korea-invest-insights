---
title: "엔비디아 실적과 AI-RAN: SK텔레콤 한 종목 베팅보다 공급망을 봐야 하는 이유"
date: 2026-05-17
description: "다음 주 엔비디아 실적에서 AI-RAN이 언급될 가능성이 있다. 시장은 곧바로 SK텔레콤 매수를 떠올린다. 그러나 AI-RAN의 경제적 가치는 통신사보다 GPU, HBM, vRAN 장비, RU/RF, 광인터커넥트 공급망으로 먼저 흘러간다. SK텔레콤 단일 종목보다 한국 AI-RAN 공급망 바스켓으로 접근하는 편이 더 합리적인 이유를 정리한다."
categories: ["Theme-Analysis"]
tags:
  - "AI-RAN"
  - "엔비디아"
  - "NVIDIA"
  - "SK텔레콤"
  - "017670"
  - "삼성전자"
  - "005930"
  - "SK하이닉스"
  - "000660"
  - "RFHIC"
  - "오이솔루션"
  - "KMW"
  - "한국 주식"
slug: ai-ran-nvidia-earnings-skt-vs-supply-chain-2026-05-17
valley_cashtags:
  - SK텔레콤
  - 삼성전자
  - SK하이닉스
  - RFHIC
  - 오이솔루션
  - KMW
---

> 📚 **관련 시리즈**
> [SK텔레콤 리레이팅: 배당주에서 AI 인프라 기업으로](/ko/post/sk-telecom-rerating-ai-infrastructure-operator-2026-04-25/) / [다음 주 구글 I/O와 NVIDIA 실적 프리뷰](/ko/post/google-io-nvidia-earnings-korea-semi-preview-2026-05-17/) / [AI 후공정 데이터 비교](/ko/post/ai-substrate-test-socket-data-comparison-2026-05-16/) / [삼성전자 TSMC식 리레이팅](/ko/post/samsung-electronics-tsmc-rerating-thesis-2026-05-16/)

*5월 21일 새벽 엔비디아 실적 컨퍼런스콜이 있다. 'AI-RAN'이라는 단어가 거기서 언급될 가능성이 있고, 그러면 한국 시장에서는 자동으로 'SK텔레콤 매수' 반사가 작동한다. SKT는 글로벌 6G 코얼리션 12개사에 들어가 있고, AIDC 매출이 89% YoY 성장했고, 외국인도 사고 있다. 그럼에도 'AI-RAN 테마 = SKT 매수'는 가장 흔하면서 가장 비효율적인 추론이다. 왜인가? MWC 2026에서 엔비디아가 직접 호명한 통신사는 T-Mobile, SoftBank, IOH 셋이었고 SKT는 그 명단에 없었다. 더 본질적으로는, AI-RAN의 '경제적 가치'가 통신사가 아니라 GPU·메모리·RU·광인터커넥트로 흘러간다. 진짜 알파는 'AI-RAN' 단어가 아니라 '돈이 어디로 가는가'를 묻는 데서 시작한다.*

## 핵심 요약

* **다음 주 이벤트**: 5월 21일 목요일 오전 6시(KST) 엔비디아 FY2027 1Q 실적 컨퍼런스콜.
* **AI-RAN 언급 가능성**: telecom/Aerial/wireless 일반 언급 70\~80%, 'AI-RAN' 직접 언급 50\~60%, 특정 통신사 호명 가능성 15\~25%, **SKT 직접 호명 가능성 5\~15%**.
* **시장의 자동 반사 패턴**: AI-RAN 언급 → SKT 매수. 이게 가장 흔한 함정이다.
* **현실**: MWC 2026 엔비디아 직접 호명 통신사 = T-Mobile, SoftBank, IOH. **SKT는 그 명단에 없다.**
* **AI-RAN 경제적 가치 귀속 순서**:
  * **1단계, 가장 큰 풀**: GPU/HBM/메모리 (NVIDIA → SK하이닉스, 삼성전자)
  * **2단계**: vRAN/네트워크 장비 (Samsung Networks, Nokia, Ericsson)
  * **3단계**: RU/RF/전력증폭기 (RFHIC, KMW)
  * **4단계**: 광인터커넥트/CPO (오이솔루션, 빛과전자)
  * **5단계, CAPEX 집행자**: SKT, T-Mobile, SoftBank
* **SKT의 진짜 투자 포인트**: AI-RAN이 아니라 **AIDC + GPUaaS + sovereign AI**. 이미 1Q26 매출 1,314억원으로 가시화되고 있다.
* **실전 결론**:
  * SKT: Hold / 신규는 Wait. 이미 YTD 강세이고 추격은 비효율적이다.
  * 공급망 우선순위: **삼성전자 core > RFHIC 조건부 > 오이솔루션 옵션 > KMW 대기 > 광통신 소형주 투기성**.
  * 가장 합리적 구조: 메모리 대형주 core + RFHIC/오이솔루션 satellite.

## 1. 시작 — 시장의 '자동 반사' 패턴이 만드는 함정

### 1.1 '엔비디아 → AI-RAN → SKT'라는 추론 사슬

시장에서 자주 보이는 사고 흐름은 단순하다.

```text
1. 엔비디아 실적 임박
   ↓
2. Jensen Huang이 'telecom is next' 발언 가능성
   ↓
3. AI-RAN 테마 부각
   ↓
4. "한국 AI-RAN 대표주는 SKT다"
   ↓
5. SKT 매수
```

이 사슬의 문제는 각 단계가 모두 그럴듯해 보인다는 점이다. 엔비디아는 실제로 통신과 AI-RAN을 말해왔고, SK텔레콤은 실제로 AI 인프라와 6G를 이야기해왔다. 그러나 4번이 사실인지, 5번이 투자로 효율적인지는 별도 검증이 필요하다.

대부분의 테마 매매는 여기서 멈춘다. "단어가 맞다"와 "돈이 간다"를 같은 말로 처리한다. 하지만 두 문장은 다르다.

### 1.2 SKT가 매력적으로 보이는 이유 — 사실관계

SKT가 AI-RAN 대표주처럼 보이는 근거는 분명히 있다.

```text
✓ NVIDIA 글로벌 6G 코얼리션 12개사에 포함
✓ MWC 2026에서 'AI Native' 전략 발표
✓ Supermicro Haein 클러스터 1,000+ AI 서버
✓ DOCOMO와 vRAN/AI-RAN 백서 공동 발간
✓ Ericsson과 2031년까지 6G 표준화 협력 MOU
✓ 1Q26 AIDC 매출 1,314억원 (+89% YoY)
✓ 최근 1주일 외국인 +878억원 순매수
✓ 5/11\~5/13 주가 강세
```

표면적으로는 매력적이다. 통신 본업의 방어력에 AI 인프라 스토리가 붙고, 글로벌 6G 협력 네트워크에도 들어가 있다. 단기 수급도 좋다.

### 1.3 그러나 시장이 자주 놓치는 것

같은 사실을 다르게 읽으면 그림이 달라진다.

```text
✗ 6G 코얼리션 12개사 = '코얼리션 멤버' (그룹 멘션)
✗ NVIDIA 직접 호명 field trial 통신사 ≠ SKT
   (T-Mobile, SoftBank, IOH가 marquee)
✗ MWC 2026 SKT 발표 = AI Native 전략 (AI-RAN은 한 줄)
✗ 1Q26 AIDC 매출 1,314억원 = 연결 매출의 약 3.0%
✗ 외국인 매수 = 이미 5/11\~5/13 강세에 반영
✗ 주가는 52주 저점 대비 약 +101%
```

즉 직접도는 약하고 이미 반영된 부분은 많다. 그래서 SKT 단일 베팅은 thin thesis에 가깝다. 주제는 맞지만, 가격과 가치 귀속 위치가 문제다.

## 2. MWC 2026에서 실제 무슨 일이 있었나 — 명확한 팩트

### 2.1 NVIDIA가 직접 호명한 3개 통신사

NVIDIA가 MWC 2026에서 first-name field trial로 직접 호명한 통신사는 셋이다.

**1. T-Mobile US**

Nokia AirScale Massive MIMO와 GH200 1대로 비디오 스트리밍, 생성형 AI 쿼리, 비디오 캡션을 동시에 처리하는 실증을 진행했다. Seattle AI-RAN Innovation Center와 OTA(over-the-air) 환경 검증이 핵심이다.

**2. SoftBank (AITRAS)**

세계 최초 16-layer Multi-User MIMO 다운링크, fully software-defined 5G vRAN, 기존 4-layer 대비 spectral efficiency 3배를 강조했다. 통신사 중 AI-RAN 상용화 스토리가 가장 앞서 보이는 쪽이다.

**3. Indosat Ooredoo Hutchison (IOH)**

동남아 최초 AI-RAN-powered Layer 3 5G call, 라이브 5G 네트워크를 통한 로봇 강아지 원격 제어, pre-commercial validation 단계가 핵심이었다.

여기서 중요한 것은 단순하다. **SKT는 위 셋에 포함되지 않았다.** SKT는 그룹 멘션에는 들어가지만, 엔비디아가 구체적 field trial 사례로 직접 호명한 통신사는 아니었다.

### 2.2 NVIDIA의 한국 관련 marquee 발표는 따로 있었다

NVIDIA의 한국 관련 핵심 발표는 AI-RAN보다 두 갈래로 나뉜다.

첫째는 **Supermicro의 SKT Haein 클러스터**다. 1,000대 이상의 AI 서버 deploy가 핵심이다. 그러나 이것은 AI-RAN이라기보다 AIDC와 sovereign AI 인프라에 가깝다.

둘째는 **Samsung Electronics vRAN 데모**다. 삼성전자 자체 vRAN 소프트웨어, NVIDIA Grace CPU, L4 GPU를 활용한 AI-MIMO beamforming 데모와 multi-cell test 환경이 핵심이었다.

즉 AI-RAN 관점에서 NVIDIA가 명시적으로 협력 강조한 한국 회사는 Samsung Networks 쪽에 더 가깝다. SKT는 AIDC 관점에서 더 강하게 연결된다. 둘은 다른 thesis다.

### 2.3 함의 — SKT의 위치 재정의

NVIDIA AI-RAN 생태계 안에서 SKT의 실제 위치는 이렇게 보는 게 더 정확하다.

```text
Policy/Governance 레이어: 강함
- AI-RAN Alliance 보드 멤버
- 6G 코얼리션 멤버
- 표준화 협력

Field/Implementation 레이어: Follower
- T-Mobile, SoftBank, IOH가 marquee
- SKT는 그룹 멘션 수준

Commercial/Monetization 레이어: 검증 전
- AI-RAN으로 어떻게 돈을 벌 것인가
- '실증'과 '매출 인식' 사이 간극
```

SKT는 미래 비전 리더에 가깝다. 그러나 단기 매출 베타로는 약하다. 시장은 보통 후자에 더 빠르게 반응한다.

## 3. AI-RAN의 경제적 가치 — 어디로 흘러가는가

### 3.1 5단계 가치 귀속 구조

AI-RAN 인프라를 한 단위 깔 때 들어가는 돈은 대략 다섯 단계로 흘러간다.

**1단계 — GPU/HBM/메모리, 가장 큰 풀**

NVIDIA GB200/GB300, L4, RTX Pro 같은 GPU와 Grace CPU, 그리고 그 안의 HBM과 DRAM이 핵심이다. 수익은 NVIDIA, 그리고 SK하이닉스와 삼성전자 같은 메모리 공급망으로 간다. AI-RAN 총 CAPEX의 약 40\~50%가 여기에 걸릴 수 있다.

**2단계 — vRAN/네트워크 소프트웨어**

5G/6G vRAN 스택, AI 채널 추정, 스케줄러, 네트워크 최적화 소프트웨어가 여기에 들어간다. Samsung Networks, Nokia, Ericsson이 핵심 플레이어다. 비중은 약 15\~20%로 볼 수 있다.

**3단계 — RU/RF/전력증폭기**

Radio Unit, GaN PA, 필터, 안테나, mMIMO가 들어간다. RFHIC, KMW, Nokia·Ericsson RU 부문이 관련된다. 비중은 약 10\~15%다.

**4단계 — 광인터커넥트/CPO**

800G/1.6T 광트랜시버, ELSFP, CPO, Spectrum-X, ConnectX와 연결되는 영역이다. NVIDIA와 오이솔루션, 빛과전자, 라이콤 같은 광부품 회사가 연결된다. 비중은 약 5\~10%다.

**5단계 — 운영자/CAPEX 집행자**

SKT, T-Mobile, SoftBank, IOH 같은 통신사가 여기에 있다. 역할은 위 1\~4단계를 사주는 buyer다. 수익 귀속은 네트워크 운영 효율 개선과 미래 edge AI 서비스 과금에서 나올 수 있지만, AI-RAN 자체 CAPEX 관점에서는 cost center다.

이게 가장 중요한 통찰이다. **통신사는 돈을 받는 쪽이 아니라 돈을 쓰는 쪽이다.**

### 3.2 왜 통신사는 cost center에 가까운가

2G, 3G, 4G, 5G 사이클은 반복적으로 같은 것을 가르쳐줬다.

통신사가 한 일은 대규모 신규망 구축, 서비스 제공, ARPU 증가 노력, 다음 세대 표준 전환 때 다시 신규망 구축이었다. 반면 세대가 바뀔 때마다 돈을 먼저 번 쪽은 장비 회사, 칩 회사, 메모리, 스마트폰 제조사였다.

```text
매 세대 누가 돈을 벌었나:
- 장비 회사: Nokia, Ericsson, Samsung, Huawei
- 칩 회사: Qualcomm, MediaTek
- 메모리: Samsung, SK하이닉스, 마이크론
- 폰 제조사: Apple, Samsung

매 세대 통신사 ROE:
- 4G 사이클 (2010\~2015): 한국 통신사 ROE 5\~10%
- 5G 사이클 (2019\~2024): 한국 통신사 ROE 5\~9%
- 6G 사이클 (2027\~?): 아직 미확인
```

통신사 ROE는 5G 사이클에도 크게 올라오지 못했다. AI-RAN이 이 패턴을 바꿀 수는 있지만, 아직 증거는 부족하다. 따라서 "AI-RAN = 통신사 재평가"라는 thesis는 현재로서는 약하다.

### 3.3 통신사가 이익을 가져갈 수 있는 시나리오

통신사가 AI-RAN으로 진짜 돈을 벌려면 단순 망 운영자를 넘어야 한다.

```text
1. 단순 '망 운영' → 'edge AI 서비스 운영자'
   - 망 위에 AI 워크로드를 돌리고 과금
   - AI as a service 모델
   - 통신 + 컴퓨팅의 융합

2. sovereign AI infrastructure operator
   - 정부·기업 대상 데이터 주권 보장
   - 한국 영토 내 AI 인프라 운영
   - 수주 단위 큰 사업

3. B2B AI 솔루션 통합사
   - 자율주행, 스마트시티, 스마트팩토리
   - 5G/6G + AI 결합 솔루션
   - 통신·플랫폼·솔루션 동시
```

이런 모델로 가야 통신사 이익이 올라간다. SKT가 추구하는 방향도 여기에 가깝다. 다만 매출 인식까지는 시간이 필요하다. 가장 빠른 모델은 AIDC + GPUaaS이고, 이게 SKT의 진짜 thesis다. AI-RAN이 아니다.

## 4. 시장의 4가지 오해 — 정면으로 해소

### 4.1 오해 1 — "AI-RAN 테마 = SKT 매수"

이건 근거 없는 자동 반사다.

```text
"엔비디아가 telecom 언급" → "한국 통신주 사자"
```

문제는 세 가지다. 한국 통신주를 SKT로 자동 매핑하는 것, 통신사 자체를 이익 귀속처로 보는 것, SKT를 글로벌 marquee field trial 통신사로 보는 것이다.

수정된 사고 흐름은 이렇다.

```text
엔비디아가 telecom 언급
  ↓
telecom CAPEX 사이클 가속
  ↓
통신 인프라 부품 회사 수혜
  ↓
Samsung Networks, RFHIC, 오이솔루션
```

SKT는 5단계에 등장한다. 우선순위는 후순위다. CAPEX 집행자라는 위치를 명확히 해야 한다.

### 4.2 오해 2 — "SKT는 글로벌 AI-RAN 리더다"

부분적으로 맞고, 부분적으로 틀리다.

맞는 부분은 정책과 R&D 레벨이다. SKT는 AI-RAN Alliance 보드 멤버이고, 6G 표준화 활동에 적극적이며, AI Native 비전을 명확히 제시하고 있다.

틀린 부분은 field implementation 레벨이다. 글로벌 marquee field trial은 T-Mobile, SoftBank, IOH가 앞서 있다. 특히 SoftBank는 상용화 스토리에서 더 앞선 위치다.

비유하면 SKT는 AI-RAN 학회의 의장에 가깝고, T-Mobile과 SoftBank는 AI-RAN의 첫 고객에 가깝다. 학회의 의장 역할은 가치 있지만, 시장은 첫 고객에게 더 빠르게 반응한다.

### 4.3 오해 3 — "AIDC 매출이 89% 성장했으니 매수"

숫자만 보면 그럴듯하다. 1Q26 AIDC 매출은 1,314억원이고 전년 대비 89% 증가했다.

그러나 비중 계산이 필요하다.

```text
연결 매출 4.3923조원
AIDC 매출 1,314억원
AIDC 비중 = 1,314 / 43,923 = 약 3.0%
```

AIDC가 빠르게 성장 중인 것은 사실이다. 그러나 전체 매출의 약 3%다. 전사 EPS 영향은 이보다 더 작을 수 있다.

물론 89% 성장이 지속되면 그림은 달라진다. 2년 후에는 약 10%대, 3년 후에는 20%대 비중도 가능하다. 하지만 의미 있는 전사 비중까지는 2\~3년이 걸린다. 단기 AI 베타로 SKT를 사기에는 아직 약하다.

### 4.4 오해 4 — "외국인이 사니 따라 사야"

최근 5거래일 외국인 순매수 약 878억원은 분명한 수급 신호다. 5월 11일과 12일에 강한 매수가 나왔고, 이후 조정에도 매수는 유지됐다.

그러나 5월 11\~13일 주가가 이미 강하게 올랐다. 외국인 매수의 가격 영향이 상당 부분 반영된 상태에서 추격하는 것은 뒤늦은 매수자 포지션에 가깝다.

외국인이 왜 사는지는 별도 분석이 필요하다. AIDC 성장, 통신주 방어력, AI-RAN 테마 선반영이 섞였을 수 있다. 외국인 매수는 추격 매수의 충분조건이 아니다.

## 5. 한국 AI-RAN 공급망 — 진짜 우선순위

### 5.1 종목별 직접도 매트릭스

| 순위 | 종목 | 코드 | AI-RAN 직접도 | NVIDIA 베타 | 펀더멘털 | 판단 |
|---:|---|---|---|---|---|---|
| 1 | **삼성전자** | 005930 | 높음 (vRAN + HBM) | 매우 높음 | 강함 | Watchlist → Buy on dip |
| 2 | **SK하이닉스** | 000660 | 중간 (HBM 간접) | 매우 높음 | 강함 | Hold / 추격 자제 |
| 3 | **RFHIC** | 218410 | 매우 높음 (GaN RU) | 간접 | 강함 (1Q26 OPM 18%) | Wait (밸류 부담) |
| 4 | **오이솔루션** | 138080 | 높음 (1.6T 광) | 간접 | 턴어라운드 중 | Watchlist (조건부) |
| 5 | **KMW** | 032500 | 높음 (mMIMO) | 간접 | 약함 (적자) | Avoid until earnings turn |
| 6 | **빛과전자/라이콤류** | - | 중간 (광모듈) | 간접 | 약함 | Speculative only |
| 참고 | **SK텔레콤** | 017670 | 낮음 (operator) | 간접 | AIDC 성장 | Hold / 신규 Wait |

### 5.2 종목별 thesis 요약

**삼성전자 — 1순위**

삼성전자는 AI-RAN에 세 겹으로 노출된다. 첫째, HBM과 DRAM은 NVIDIA 서버에 들어간다. 둘째, Samsung Networks vRAN이 있다. 셋째, AI-MIMO 알고리즘과 NVIDIA 기반 multi-cell test 경험이 있다.

매력은 AI-RAN 전 레이어에 노출된다는 점이다. 메모리 슈퍼사이클이 base이고, AI-RAN은 추가 옵션이다. 2027년 예상 PER 약 5배라는 점도 밸류에이션상 가장 싼 축이다.

리스크는 5월 21일 파업, HBM 점유율에서 SK하이닉스 대비 후순위라는 점, 복합 IDM discount다. 판단은 watchlist에서 매크로 안정 후 분할 매수 쪽이다. 파업 회피와 NVIDIA beat가 동시에 나오면 비중 확대 논리가 강해진다.

**RFHIC — 3순위, 조건부**

RFHIC는 RU 전력증폭기용 GaN 패키지, 삼성전자 네트워크 장비 공급망, 5G/AI-RAN/방산 복합 수혜가 겹친다.

1Q26 매출 431억원, 영업이익 77억원, OPM 18%로 턴어라운드가 확인되고 있다. 최근 12개월 절대수익률도 매우 강했다. AI-RAN 상용화 시 RU 부품 쪽에서는 가장 직접도가 높다.

문제는 밸류에이션이다. 2026E PER 60배대, 2027E PER 40배 안팎이면 이미 많은 기대가 들어갔다. 신규 수주 또는 조정이 확인될 때 진입하는 쪽이 낫다.

**오이솔루션 — 4순위, 옵션**

오이솔루션은 AI 데이터센터 1.6Tbps OSFP 광트랜시버, CPO용 ELSFP, AI-RAN fronthaul/backhaul 광인터커넥트와 연결된다.

2026년 흑자전환 전망, datacom 비중 확대 가능성, AI-RAN과 AI 데이터센터 동시 노출이 장점이다. 그러나 ELSFP 양산은 2027년 이후 가시성이 더 중요하고, 최근 주가 변동성도 크다. 3Q26 ELSFP 샘플링 확인 후 접근하는 편이 더 합리적이다.

**KMW — 5순위, 대기**

KMW는 C-band 64TRx 640W mMIMO, 안테나·필터·RU 베타가 있다. 하지만 1Q26 매출 215억원, 영업손실 57억원으로 아직 실적 검증이 약하다. 적자기업에 높은 PBR이 붙은 상태라 분기 흑자 전환 전 추격은 피하는 게 맞다.

**광통신 소형주 — 6순위, 투기성**

빛과전자, 라이콤 등은 OFC 2026에서 1.6T 광트랜시버, 100G ER1 Bidi, 6G 프론트홀 제품을 공개했다. 그러나 제품 공개와 양산 매출 사이에는 간극이 크다. 장기 투자는 수주 공시 확인 후가 더 안전하다.

### 5.3 SKT 자체의 진짜 thesis

SKT를 사야 한다면 AI-RAN 때문이 아니라 다음 네 가지 때문이다.

```text
진짜 thesis 1: AIDC 매출 본격화
- 1Q26 1,314억원 (+89%)
- 2026\~2027년 연결 비중 5%+ 가능
- 매출이 실제 손익계산서에 찍힘

진짜 thesis 2: GPUaaS 사업 확대
- NVIDIA GPU 클러스터 임대업
- Haein 클러스터 1,000+ 서버
- B2B 매출 성장

진짜 thesis 3: Sovereign AI 인프라
- 한국 데이터 주권 인프라
- 정부·대기업 향 장기 계약
- 신규 매출 카테고리

진짜 thesis 4: 통신 본업 안정성
- 5G 가입자 안정화
- ARPU 유지
- 배당 수익률 방어력
```

AI-RAN보다 AIDC와 GPUaaS가 훨씬 직접적이다. 다만 현재 가격에서는 1차 베팅보다 조정 후 진입이 합리적이다.

## 6. 엔비디아 실적콜 — 무엇을 들어야 하나

### 6.1 신호 강도별 매핑

| 콜에서 나올 수 있는 문구 | SKT 영향 | 공급망 영향 | 시장 반응 강도 |
|---|---|---|---|
| "telecom is next" (일반론) | 약함 | 미미 | 매우 약함 |
| "future wireless networks as computing platforms" | 약함 | 약함 | 약함 |
| "Aerial RAN Computer commercial deployments" | 중간 | 강함 (삼성전자, RFHIC) | 중간 |
| "AI-RAN deployments with operators" | 중간 | 중간 | 중간 |
| "Samsung Networks validation" | 중간 | 강함 (삼성전자 직접) | 강함 |
| "operator deployment with SoftBank/T-Mobile" | 약함 | 강함 (장비주) | 강함 |
| "operator deployment with SK Telecom" | **매우 강함** | 강함 | 매우 강함 |
| "commercial revenue from AI-RAN" | 강함 | 강함 (전체) | 매우 강함 |

가장 가능성 높은 시나리오는 Aerial, telecom, wireless 일반 언급과 코얼리션 group mention이다. 이 경우 SKT 단기 반응은 노이즈 수준일 수 있고, 공급망 특히 삼성전자 반응이 더 클 가능성이 있다.

낮은 확률이지만 SK Telecom이 직접 호명되면 SKT는 단기적으로 +5\~10% 반응할 수 있다. 다만 sell the news 위험도 커진다.

또 다른 낮은 확률 시나리오는 Samsung Networks 직접 호명이다. 이 경우 삼성전자 가격 영향은 메모리 비중 때문에 제한적일 수 있지만, RFHIC와 오이솔루션 같은 공급망 종목이 더 민감하게 반응할 수 있다.

### 6.2 실전 트레이딩 가이드

**시나리오 A: SKT 직접 호명, 확률 5\~15%**

SKT 단기 +5\~10% 가능성이 있다. 보유자는 일부 차익실현을 검토할 수 있고, 신규는 추격하지 않는 편이 낫다. 매수 적기는 호명 후 조정이 나온 뒤다.

**시나리오 B: AI-RAN 직접 언급, 확률 50\~60%**

공급망 동반 변동성이 커질 수 있다. SKT는 노이즈 수준 반응일 수 있고, 매수 대상은 삼성전자 눌림목이 더 합리적이다. 오이솔루션과 KMW를 급등 직후 추격하는 것은 피하는 쪽이 낫다.

**시나리오 C: telecom 일반 언급, 확률 70\~80%**

시장 무반응 가능성이 크다. 펀더멘털 중심 판단으로 돌아가면 된다. AI-RAN 단어만 보고 매수할 이유는 없다.

**시나리오 D: AI-RAN/telecom 미언급, 확률 10\~20%**

AI-RAN 테마는 일시적으로 식을 수 있다. 이 경우 오히려 조정 시 삼성전자, RFHIC 같은 공급망 종목을 볼 기회가 될 수 있다.

공통 원칙은 같다. 콜 직전 추격 매수는 피하고, 콜 결과와 1\~2일의 가격 정리를 본 뒤 움직이는 편이 낫다. 매크로 게이트도 함께 확인해야 한다.

## 7. 자주 묻는 질문

### 7.1 "엔비디아 콜에서 SKT가 호명되면 +10% 가능한가?"

가능하다. 그러나 sell the news 위험도 크다.

호명 당일에는 +3\~8%, 다음 날에는 추가 상승 또는 차익실현이 나올 수 있다. 5거래일 뒤에는 일부 반락할 수 있고, 10\~30일 뒤에는 실제 매출과 수주 여부가 방향을 결정한다.

따라서 "호명 + 추격"은 단기 변동성 노출이다. "호명 + 1주 대기 + 조정 시 매수"가 더 안전하다. 또 호명 자체가 매출로 연결되어야 진짜 알파다. 그룹 멘션이면 정보 가치가 작다.

### 7.2 "그래도 SKT가 가장 직접적인 AI-RAN 한국 종목 아닌가?"

정의에 따라 다르다.

운영자/실증 차원에서는 SKT가 가장 적극적이다. KT나 LG유플러스보다 AI-RAN과 6G 내러티브가 더 분명하다.

그러나 경제적 가치 귀속 차원에서는 삼성전자가 더 앞선다. vRAN과 HBM을 동시에 갖고 있기 때문이다. NVIDIA가 첫 번째로 협력하는 한국 회사라는 관점에서도 Samsung Networks validation이 더 직접적이다.

투자 관점에서 중요한 것은 경제적 가치 귀속이다. 그래서 SKT는 한국 AI-RAN 대표주라는 표현이 가능하더라도, 그 표현은 운영자 기준에 한정된다.

### 7.3 "SKT를 아예 사지 말라는 건가?"

아니다. SKT는 충분히 좋은 회사다. 다만 왜 사는지를 명확히 해야 한다.

좋은 매수 이유는 AIDC 매출 성장, GPUaaS 확대, 통신 본업 + 배당 + 방어주 매력, sovereign AI 인프라 옵션이다.

나쁜 매수 이유는 "엔비디아가 AI-RAN을 언급할 것 같아서", "외국인이 사니까", "AI 테마주니까", "통신주 중 가장 AI 같아서"다.

현재 주가가 52주 저점 대비 크게 오른 상태라 신규 매수는 조정 후가 더 합리적이다. 또는 AIDC 2분기 매출 가시화 후 접근하는 것이 낫다.

### 7.4 "공급망 바스켓을 어떻게 구성하나?"

보유 기간과 변동성 감내 수준에 따라 다르다.

방어형은 삼성전자와 SK하이닉스 중심이다. AI-RAN 직접도는 낮지만 가장 안전하다.

균형형은 삼성전자 core에 오이솔루션, RFHIC, SK하이닉스를 일부 섞는 구조다. AI-RAN 직접도와 안정성을 같이 본다.

공격형은 RFHIC, 오이솔루션, 삼성전자, KMW 또는 광통신 소형주를 섞는 구조다. 다만 이 경우 매크로 게이트 통과와 분할 매수가 필수다.

공통 원칙은 단일 종목 비중을 과하게 높이지 않는 것이다. AI-RAN은 아직 상용화 초기이므로 단일 종목 승부보다 가치 귀속 레이어별 바스켓이 더 합리적이다.

## 8. 다른 글과의 연결

**구글 I/O + NVIDIA 실적 프리뷰 글**은 다음 주 이벤트 일정과 NVIDIA Q2 가이던스의 의미를 다뤘다. 이 글은 그중 AI-RAN 부분만 따로 떼어 한국 공급망 관점으로 확장한 후속 분석이다.

**SK텔레콤 리레이팅 글**은 SKT의 본질을 배당주가 아니라 AIDC, GPUaaS, sovereign AI 인프라 오퍼레이터로 봤다. 이 글은 그 thesis를 유지하되, AI-RAN 단일 테마로 SKT를 추격하는 것은 비효율적이라는 점을 보완한다.

**AI 후공정 데이터 비교 글**은 메모리, 기판, 테스트 소켓의 구조적 차이를 정리했다. AI-RAN 공급망에서도 같은 원리가 작동한다. 단어보다 돈이 어디에 붙는지가 중요하다.

**삼성전자 TSMC 리레이팅 글**은 삼성전자를 메모리 사이클주에서 AI 통합 플랫폼으로 재분류할 수 있는지 검토했다. Samsung Networks vRAN은 그 재분류 논리의 작은 옵션 중 하나다.

## 9. 마지막 한 줄

다음 주 엔비디아 실적에서 AI-RAN이라는 단어가 언급될 가능성이 있다. 시장은 자동 반사로 SKT 매수를 생각한다. 그러나 이건 가장 흔하면서 가장 비효율적인 추론이다.

왜인가? MWC 2026에서 NVIDIA가 직접 호명한 통신사는 T-Mobile, SoftBank, IOH 셋이었다. SKT는 그 명단에 없었다. 더 본질적으로는 AI-RAN의 **경제적 가치가 통신사가 아니라 GPU·메모리·vRAN 장비·RU·광인터커넥트로 흘러간다**. 통신사는 CAPEX 집행자다. 돈을 받는 쪽이 아니라 돈을 쓰는 쪽이다. 2G·3G·4G·5G 사이클이 매번 가르쳐준 패턴이 6G/AI-RAN에서도 반복될 가능성이 크다.

한국 AI-RAN 공급망 진짜 우선순위는 삼성전자(메모리 + vRAN 동시 노출) > SK하이닉스(HBM 간접) > RFHIC(GaN RU 직접) > 오이솔루션(광인터커넥트 옵션) > KMW(mMIMO 베타) > 광통신 소형주(투기성) 순이다. SKT는 이 순서에서 후순위이고, 운영자 위치다.

SKT 자체의 매력도 있다. 다만 그건 AI-RAN 때문이 아니라 **AIDC + GPUaaS + sovereign AI**다. 1Q26 AIDC 매출 1,314억원이 89% 성장한 게 그 증거다. 다만 연결 매출의 3.0% 수준이라 의미 있는 비중까지는 2\~3년이 걸린다. 현재 가격에서는 신규 매수보다 조정 후 진입이 합리적이다.

가장 실전적인 행동은 다음 세 가지다. 첫째, 엔비디아 콜에서 SK Telecom이 직접 호명되면 보유자는 일부 차익실현, 신규는 추격 금지. 둘째, Samsung Networks validation 또는 AI-RAN commercial deployment 언급 시 삼성전자·RFHIC를 1\~2일 정리 후 검토. 셋째, 단순 telecom is next 수준이면 펀더멘털 중심 판단으로 회귀하고 AI-RAN 테마 추격 자체를 보류.

**진짜 알파는 AI-RAN 단어 자체가 아니라 경제적 가치가 어디에 귀속되는가를 묻는 데서 시작한다.** 이 질문을 정확히 던지면 답은 명확해진다. 통신사가 아니라 공급망이다. 그 안에서도 메모리 대형주 core + RU·광 satellite 구조가 가장 합리적이다. 단순 테마 매수는 가장 빠르게 손해 보는 길이고, 가치 귀속 구조를 이해한 베팅이 가장 길게 가는 길이다.

---

*이 글은 리서치와 논평으로만 활용해야 하며 투자 조언이 아닙니다. 엔비디아 FY2027 1Q 실적콜 일정(2026년 5월 20일 14:00 PT / 5월 21일 06:00 KST)은 NVIDIA 공식 IR 기준입니다. MWC 2026 발표 내용(T-Mobile, SoftBank, IOH의 field trial, Samsung Networks vRAN multi-cell test)은 NVIDIA·Nokia·Samsung 공식 발표 기준입니다. SKT 1Q26 실적(연결 매출 4.3923조원, AIDC 매출 1,314억원, +89.3% YoY)은 회사 공식 실적자료 기준입니다. SKT 6G 코얼리션 멤버십(12개사)은 NVIDIA IR 발표 기준입니다. RFHIC 1Q26 실적(매출 431억원, 영업이익 77억원, OPM 18%), 오이솔루션 1.6T/ELSFP 제품, KMW 1Q26 실적은 회사·증권사 자료 기준입니다. AI-RAN 직접 호명 가능성(SKT 5\~15%, 일반 telecom 70\~80% 등)은 분석가의 주관적 확률 추정이며, 실제 콜 내용과 다를 수 있습니다. AI-RAN 가치 귀속 비중(GPU/HBM 40\~50%, vRAN 15\~20% 등)은 분석가의 추정이며, 실제 구성은 사례별로 다를 수 있습니다. 종목 우선순위(삼성전자 1위, RFHIC 3위 등)는 분석가의 현재 판단이며, 시장 상황·실적 발표에 따라 변동될 수 있습니다. 단기 주가 반응 예측은 역사적 패턴 기반이며 미래를 보장하지 않습니다. 글로벌 매크로 환경(미국 금리, 유가, 환율, VIX)이 종목 가격에 추가 영향을 줄 수 있습니다. 분석이 틀릴 수도 있습니다. 데이터 기준일: 2026년 5월 17일 KST.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
