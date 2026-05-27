---
title: "Marvell Q1 FY2027业绩与韩国半导体：比HBM更关键的互连、基板与电源瓶颈"
date: 2026-05-28T10:20:00+09:00
description: "Marvell Q1 FY2027业绩不只是EPS超预期，更揭示AI数据中心瓶颈正向custom XPU、光互连、scale-up网络、FCBGA、MLCC、硅电容、测试插座扩散。韩国半导体read-through依次梳理三星电机、三星电子、SK海力士、ISC·Leeno·TSE。"
categories: ["Market-Outlook"]
tags:
  - "Marvell"
  - "MRVL"
  - "马维尔"
  - "韩国半导体"
  - "三星电机"
  - "009150"
  - "三星电子"
  - "005930"
  - "SK海力士"
  - "000660"
  - "ISC"
  - "Leeno"
  - "TSE"
  - "FC-BGA"
  - "MLCC"
  - "硅电容"
  - "HBM"
  - "AI ASIC"
  - "AI基础设施"
slug: marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28
valley_cashtags:
  - Marvell
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - ISC
  - 리노공업
  - 티에스이
  - 대덕전자
  - 이수페타시스
  - 심텍
draft: false
---

> 📚 后续文章背景
> 本文是[Marvell·Broadcom业绩前韩国半导体瓶颈梳理](/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/)的续篇。预览文章提出的问题是"HBM单一押注能否扩展至AI ASIC、网络与电源稳定化"，本文以Marvell Q1 FY2027业绩为基准重新作答。相关枢纽页面：[AI HBM枢纽](/page/korea-semiconductor-hbm-kospi-hub/)、[AI基板·PCB枢纽](/page/korea-ai-pcb-substrate-hub/)、[韩国半导体价值链枢纽](/page/korea-semiconductor-equipment-ip-hub/)。

## TL;DR

Marvell Q1 FY2027的核心不是EPS超预期，而是公司将FY2027\~FY2028 AI数据中心的成长路径再度上调，并以<strong>custom XPU、光互连、以太网交换、DCI、scale-up/scale-across网络、XPU attach</strong>来解释其原因。

翻译为韩国半导体，答案并非简单的"多买HBM"。HBM依然是主线，但本次业绩新确认的incremental alpha在于<strong>GPU周边的互连、基板、电源完整性与测试瓶颈</strong>。

优先级如下：

| 优先级 | 韩国read-through | 核心标的/板块 | 判断 |
|---:|---|---|---|
| 1 | FCBGA + AI服务器MLCC + 硅电容 | 三星电机 | 最为直接。但已处于重估区间，需确认SiCap·FCBGA利润率 |
| 2 | HBM4、SOCAMM2、eSSD、先进封装 | 三星电子、SK海力士 | HBM beta维持。新alpha在HBM以外的内存attach与封装 |
| 3 | Custom ASIC/XPU测试插座·接口 | ISC、Leeno、TSE | 结构良好，但在直接营收确认前列入观察名单 |
| 4 | AI网络用高速PCB/MLB | Isu Petasys、Daeduck Electronics、Simtech等 | 需精选。"AI PCB"并非全部同等受益 |

Marvell本身定位为<strong>HOLD / Buy watch</strong>。基准股价$198.70，12个月目标价$225，上行空间约+13%。成长路径强劲，但股价已反映较高预期。韩国方面，比Marvell本身更重要的是<strong>Marvell所确认的瓶颈将向何处蔓延</strong>。

---

## 1. Marvell业绩真正值得关注的是什么

Marvell于2026年5月27日美股盘后发布Q1 FY2027业绩，官方数据如下。（[Marvell][1]）

| 项目 | Q1 FY2027 | 解读 |
|---|---:|---|
| 营收 | <strong>$2.418B</strong> | 同比+28%，高于指引中值$18M |
| GAAP EPS | <strong>$0.04</strong> | 受Celestial AI·XConn收购会计影响偏低 |
| Non-GAAP EPS | <strong>$0.80</strong> | 接近共识预期 |
| GAAP毛利率 | <strong>52.1%</strong> | 同比改善 |
| Non-GAAP毛利率 | <strong>58.9%</strong> | AI产品组合扩大下维持58%后段 |
| 经营现金流 | <strong>$638.8M</strong> | 创纪录经营现金流 |
| Q2营收指引 | <strong>$2.70B ±5%</strong> | 区间$2.565B\~$2.835B |
| Q2 Non-GAAP EPS指引 | <strong>$0.93 ±$0.05</strong> | 下季度盈利基准线 |

业绩本身接近"小幅超预期/EPS符合预期"。然而对股价和韩国半导体read-through真正重要的，不是Q1的几分钱，而是<strong>公司描述的FY2027\~FY2028营收路径</strong>。

根据第三方电话会议记录，管理层将FY2027营收指引至约$11.5B、FY2028约$16.5B，并将FY2027互连成长率预测从原来的约50%上调至70%以上。虽非官方IR记录，但方向与公司官方新闻稿的措辞一致。Marvell官方新闻稿同样将成长来源明确为800G·1.6T光学、51.2T以太网交换机、NPO/CPO用scale-up光学、DCI模块、custom XPU及XPU attach。（[Marvell][1]、[StockAnalysis transcript][2]）

一句话总结：

> Marvell用数字确认了AI数据中心capex正从GPU采购转向集群互连架构。

---

## 2. 核心在于互连架构，而非SOCAMM

韩国投资者解读本次电话会议时最危险的误读，是将其仅视为"SOCAMM主题"。SOCAMM固然重要，但Marvell电话会议的中心并不在此。

核心顺序如下：

| Marvell核心轴 | 为何重要 | 韩国半导体翻译 |
|---|---|---|
| Custom XPU / custom ASIC | 超大规模云厂商在NVIDIA GPU之外增加自有AI芯片的信号 | HBM客户基础多元化、封装基板、测试插座 |
| 光互连 | 800G/1.6T、DCI、scale-up光学是AI集群扩展的瓶颈 | 高速PCB·光通信需精选，三星电机FCBGA·电源稳定化具结构性 |
| 以太网交换 | 51.2T、100T、200T路线图意味着AI网络芯片dollar content提升 | 网络ASIC用FCBGA、高速板、检测·测试 |
| XPU attach | CXL、NIC、内存attach、推理KV cache关联 | 三星电子SOCAMM2·eSSD·服务器DRAM，OpenEdges类内存IP选项 |
| NVLink Fusion | custom芯片在NVIDIA生态内共存的路径 | 与其"NVIDIA vs ASIC"二元论，不如关注供应链扩张 |

NVIDIA-Marvell的合作公告也指向同一方向。NVIDIA向Marvell投资20亿美元，Marvell提供兼容NVLink Fusion的custom XPU与scale-up网络，双方同时在硅光子和AI-RAN领域合作。（[Marvell NVIDIA][3]）

这句话的含义很简单：

> AI数据中心不是GPU机箱，而是GPU、custom XPU、HBM、光学、交换机、retimer、CXL、NIC、FCBGA、MLCC如同一体运作的系统。

因此韩国半导体投资也应从"是否只看内存大盘股"，下沉至"内存之下哪个瓶颈会转化为数字"。

---

## 3. 韩国半导体read-through第一优先：三星电机

将Marvell业绩翻译为韩国标的，最直接的是三星电机，理由有三。

第一，Marvell强调的custom XPU、以太网交换机、光互连、XPU attach均需要高速、高集成度的封装与基板，这与FC-BGA需求直接相关。

第二，AI服务器在低电压下瞬间需要大电流。为抑制GPU·HBM·XPU封装周围的电压波动，需要MLCC和硅电容等电源稳定化元器件。

第三，三星电机已同时覆盖上述两个层面。公司在2026年Q1业绩中披露，Package Solution营收达7250亿韩元，同比增长45%、环比增长12%，并提及AI加速器、服务器CPU及网络用高附加值基板供应扩大。（[Samsung Electro-Mechanics Q1][4]）

此外，三星电机与全球大型企业签订了1兆5570亿韩元规模的硅电容供货合同，合同期为2027年1月1日至2028年12月31日。该元件用于提升AI服务器GPU·HBM封装内部的电源供应稳定性。（[Samsung Electro-Mechanics SiCap][5]）

三星电机的投资逻辑现已演变为：

| 过去框架 | 现在框架 |
|---|---|
| 智能手机MLCC·摄像头模组周期股 | AI封装电源完整性 + FCBGA平台 |
| 移动端需求复苏 | AI加速器·服务器CPU·网络ASIC需求 |
| 通用MLCC周期 | 高容量·低ESR·超薄·高可靠MLCC/SiCap组合 |
| 与揖斐电/村田之一比较 | MLCC + FCBGA + SiCap混合比较 |

但这一结论不等于"以任何价格立即买入"。三星电机已在相当程度上反映了硅电容合同、市值突破100兆韩元及AI基础设施重估。因此下一步确认变量不是股价动能，而是<strong>毛利率、Package Solution OPM、SiCap量产良率及客户多元化进展</strong>。

---

## 4. 三星电子·SK海力士：HBM beta维持，新alpha在HBM周边

Marvell业绩对HBM并非负面信号，恰恰相反。即便custom XPU和scale-up网络增加，内存dollar content也不会减少。随着AI模型向agentic AI、推理、专家混合（MoE）演进，数据移动量与内存需求只会更大。

但从投资角度看，"HBM看好"已是核心thesis。Marvell电话会议新提供的信息如下：

1. HBM客户基础从NVIDIA GPU单一结构扩展至超大规模云厂商custom XPU。
2. XPU attach与CXL、NIC、内存attach、KV cache关联，影响延伸至服务器DRAM·SOCAMM·eSSD。
3. AI集群规模越大，连接内存与计算芯片的封装·基板·电源稳定化价值越高。

三星电子在这一环节拥有复合期权。HBM4、HBM4E、SOCAMM2、PM1763 SSD、代工及先进封装均归属同一AI基础设施堆栈。三星电子在GTC 2026上以NVIDIA合作AI基础设施产品线的形式展示了HBM4E、SOCAMM2、PM1763 SSD等产品。（[Samsung Semiconductor][6]）

SK海力士的HBM pure beta依然最强。但单就Marvell业绩而言，新alpha更多体现在<strong>与HBM并行增长的三星电机、测试插座及高速基板</strong>，而非SK海力士本身。SK海力士是主线，但也是市场关注最为集中的位置。

---

## 5. 测试插座：custom ASIC扩散中的静默受益者

Marvell电话会议中custom revenue之所以重要，不仅是芯片出货量，核心在于<strong>SKU与认证周期</strong>。

若AI加速器以单一NVIDIA GPU为标准化基础，测试元件需求相对可预测。反之，若超大规模云厂商各自的custom XPU、XPU attach、CXL、NIC、交换ASIC、DPU增多，测试条件与插座设计就会更加细分。

这种情况下，测试插座与接口元件的三个变量可能同时向好：

| 变量 | 方向 | 原因 |
|---|---|---|
| 数量 | 增加 | custom ASIC、网络ASIC、内存attach SKU增加 |
| ASP | 上升 | 高针数·高速信号·高功率测试难度提升 |
| 替换周期 | 结构性 | 世代更替与各客户qualification反复进行 |

韩国方面，ISC、Leeno、TSE列入观察名单。但此处需降低确信度。仅凭公开资料难以确认韩国测试插座厂商是否直接进入Marvell或特定超大规模云厂商custom XPU供应链。因此目前是<strong>"潜在受益"</strong>，而非<strong>"已确认客户映射"</strong>。

待确认指标为：季度业绩中AI/HPC logic营收、新客户数量、高附加值插座组合及OPM防御。

---

## 6. 普通PCB并非无差别买入对象

Marvell业绩对AI网络和光互连是正面信号。但"AI网络向好→所有PCB均受益"的结论存在风险。

受益集中于满足以下条件的厂商：

1. 能够处理高速信号用低损耗材料。
2. 具备高多层MLB或高附加值封装基板敞口。
3. 持有AI服务器·网络设备客户认证。
4. 确认ASP·层数·面积提升，而非仅靠出货量增加。

GPU和XPU数量增加，并不意味着基板数量以相同比例增长。在单一高性能封装与板卡上集成更多芯片的架构下，数量之外，<strong>基板面积、层数、材料难度、良率</strong>更为关键。

因此将Isu Petasys、Daeduck Electronics、Simtech、TLB、Korea Circuit简单归为同一篮子并不准确。Marvell业绩真正的read-through更接近于"精选具备网络用高层基板与高速信号材料能力的厂商"。

---

## 7. MRVL自身估值：好公司与好价格是两回事

对Marvell本身的判断为HOLD / Buy watch。

| 项目 | 内容 |
|---|---:|
| 基准股价 | $198.70，2026-05-27正常交易日收盘价 |
| 12个月目标价 | $225 |
| 上行空间 | 约+13.2% |
| 估算框架 | FY2028E EV/Sales |
| 核心判断 | 成长路径上调，但估值已处于高位 |

Base case计算公式如下：

```text
目标股价 = (FY2028E营收 × 目标EV/Sales - 净负债) ÷ 稀释股份数
```

假设FY2028E营收$16.5B、目标EV/Sales 12.5倍、净负债约$1.117B、稀释股份数915M，计算得目标价约$224，四舍五入为$225。

Marvell要像Broadcom一样完成重估，需要三个条件：

1. Custom silicon营收需确认为可重复的项目，而非单一客户事件。
2. 互连与交换成长的同时，non-GAAP毛利率需守住58\~59%区间。
3. 为保障供应链而预付的款项需切实转化为营收ramp与FCF。

即公司确已成为好公司，但是否是好的买入价格，则是另一个问题。

---

## 8. 下一步检查点

| 检查点 | 强信号 | 弱信号 |
|---|---|---|
| Q2 FY2027营收 | 接近或超越$2.835B上限 | 低于$2.70B中值 |
| 数据中心营收 | 环比high-teens以上增长 | sequential growth放缓 |
| Non-GAAP GM | 59.25%以上或守住上限 | 低于58.25% |
| 互连 | FY2027 +70%以上预测维持或上调 | 800G/1.6T ramp放缓 |
| Custom XPU | FY2028成长2倍以上·FY2029 $10B+能见度 | 各客户ramp延迟 |
| Scale-up交换 | tier-1客户量产具体化 | engagement多但无营收 |
| 韩国read-through | 三星电机Package Solution·SiCap·FCBGA数字确认 | 主题强劲但无利润率·订单 |

各韩国标的确认变量更为简洁：

| 标的/板块 | 待确认事项 |
|---|---|
| 三星电机 | Package Solution增长率、AI网络用FCBGA营收、SiCap量产良率·利润率、追加长期合同 |
| 三星电子 | HBM4客户认证、SOCAMM2实际出货、eSSD价格·出货量、代工/封装客户 |
| SK海力士 | HBM4 ramp、客户多元化、2027年供过于求风险 |
| ISC·Leeno·TSE | AI logic/test socket营收、新客户、高附加值组合、OPM |
| PCB/MLB | AI网络客户认证、ASP提升、低损耗材料·高层化 |

---

## 9. 论点失效条件

本thesis走弱的条件明确如下：

1. Marvell Q2营收低于$2.70B中值，数据中心成长放缓。
2. Non-GAAP毛利率跌破58.25%，custom/互连组合确认产生利润率稀释。
3. FY2028 $16.5B营收预测下调。
4. Custom XPU与XPU attach受特定客户进度延迟拖累。
5. 三星电机SiCap确认为低利润率营收，或FCBGA增长率放缓。
6. 测试插座厂商业绩中未出现AI/HPC logic营收增长。
7. HBM交货期缩短，出现2027年供过于求信号。

---

## 最终解读

Marvell Q1 FY2027对韩国半导体发出的不是"只买HBM"的信号。更准确的信息是：

> AI集群规模越大，瓶颈就从GPU向下沉至互连、基板、电源稳定化与测试。

从这一视角看，最直接的韩国标的是三星电机。三星电机的MLCC、FC-BGA、硅电容全部处于同一AI封装瓶颈之内。三星电子和SK海力士作为HBM主线持续重要，但Marvell业绩新创造的alpha更多体现在HBM周边。ISC·Leeno·TSE是custom ASIC扩散的二次受益候选，但在直接营收确认前，列入观察名单更为合适。

结论不是无差别买入。再好的thesis，若未经数字验证，终将止步于主题。本季度后韩国半导体值得关注的，比股价更重要的是<strong>Package Solution营收、SiCap利润率、AI logic测试营收及高速基板ASP</strong>。

---

## Fact / Inference / Speculation / Blocked

### [Fact]

- Marvell Q1 FY2027营收$2.418B，同比+28%，Q2营收指引$2.70B ±5%。（[Marvell][1]）
- Marvell Q1 non-GAAP毛利率58.9%，Q2 non-GAAP毛利率指引58.25\~59.25%。（[Marvell][1]）
- Marvell将800G/1.6T scale-out光学、51.2T以太网交换机、scale-up光学、DCI模块、custom XPU、XPU attach列为成长动力。（[Marvell][1]）
- NVIDIA向Marvell投资20亿美元，Marvell宣布提供兼容NVLink Fusion的custom XPU与scale-up网络。（[Marvell NVIDIA][3]）
- 三星电机2026年Q1 Package Solution营收7250亿韩元，同比增长45%、环比增长12%。（[Samsung Electro-Mechanics Q1][4]）
- 三星电机签订1兆5570亿韩元硅电容供货合同，合同期2027年1月1日\~2028年12月31日。（[Samsung Electro-Mechanics SiCap][5]）

### [Inference]

- 将Marvell的成长轴翻译为韩国，依次映射至三星电机FCBGA/MLCC/SiCap、三星电子·SK海力士内存attach、测试插座、高速基板，是合理的。
- HBM依然是主线，但本次业绩新揭示的incremental alpha，比HBM大盘股更多体现在互连·封装·电源稳定化·测试层面。
- 三星电机的重估应理解为从MLCC复苏转向AI基础设施无源元件/基板平台的转型，而非单纯周期回升。

### [Speculation]

- 三星电机SiCap客户与特定北美超大规模云厂商或AI加速器供应链存在关联的可能性在市场上有所推测，但合同对方未予公开。
- 国内测试插座厂商是否直接进入Marvell或Marvell客户的custom XPU项目，仅凭公开资料无法确认。
- AI-RAN长期可能为韩国RF·网络半导体创造机会，但视为2026年短期业绩动能尚为时过早。

### [Blocked]

- Marvell custom XPU·光学·交换机各项目中韩国厂商的直接供货情况。
- 三星电机SiCap合同的客户名称、各产品利润率及月度ramp速度。
- ISC·Leeno·TSE的AI logic各客户营收占比。
- 韩国PCB/基板标的2026年当前实时NTM PER、EV/EBITDA及共识EPS上调率。

---

## Sources

[1]: https://investor.marvell.com/news-events/press-releases/detail/1023/marvell-technology-inc-reports-first-quarter-of-fiscal-year-2027-financial-results "Marvell Technology, Inc. Reports First Quarter of Fiscal Year 2027 Financial Results"
[2]: https://stockanalysis.com/stocks/mrvl/transcripts/583849-q1-2027/ "Marvell Technology Q1 2027 Earnings Call Transcript & Audio"
[3]: https://investor.marvell.com/news-events/press-releases/detail/1019/nvidia-ai-ecosystem-expands-as-marvell-joins-forces-through-nvlink-fusion "NVIDIA AI Ecosystem Expands as Marvell Joins Forces Through NVLink Fusion"
[4]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Announces Q1 2026 Business Performance"
[5]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
[6]: https://semiconductor.samsung.com/news-events/news/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026/ "Samsung Unveils HBM4E at NVIDIA GTC 2026"

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
