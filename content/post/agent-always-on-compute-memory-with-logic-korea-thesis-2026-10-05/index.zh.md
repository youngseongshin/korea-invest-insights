---
title: "节省计算，积累记忆：代理时代韩国存储器为何融入逻辑"
date: 2026-10-05T22:20:00+09:00
categories: ["Exclusive Analysis", "AI Infrastructure", "Korean-Equities"]
tags: ["存储器", "Samsung Electronics", "SK hynix", "HBM", "定制 HBM", "代理", "KV cache", "企业级 SSD", "HBF", "CXL", "长期供货合同"]
slug: "agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05"
description: "当把整项工作交给 AI 代理的场景增多，计算成本会下降，上下文和知识则会积累。本文依据批处理与实时处理的分化、CPU 和网络需求、融入逻辑的 HBM 与 SSD、长期合同及保证金，分析韩国存储器投资逻辑，并测算当前股价所要求的盈利持续性。"
image: "cover.png"
draft: false
---

即使向同一个 AI 模型提出同一个问题，价格也会因处理方式而大幅不同。按 Anthropic 的价格表，Opus 5.5 的批处理只需在一天内返回结果，价格是标准价的一半；保证快速响应的高速模式则是标准价的两倍。再次读取已读过的上下文，费用仅为标准价的二十分之一。[^anthropic-pricing]

这张价格表浓缩呈现了 AI 基础设施的发展方向。不紧急的任务低价处理，紧急任务高价处理。最便宜的不是重新计算，而是再次取用已保存的记忆。

<strong>把整项工作委托出去的代理越多，计算就越有效率，上下文和知识也越会积累。承载这些积累的存储器与存储设备，正从标准化产品转向融入逻辑的产品。韩国存储器投资的重点，不在于今年盈利有多高，而在于这些盈利能持续多久。</strong>

需要依次验证这条逻辑链：基础设施是否转向持续计算，计算是否真正提效，什么在积累，逻辑融入存储器是否转化为可确认的收入，以及价值是否留在韩国企业。最后，我们将测算 Samsung Electronics 和 SK hynix 当前股价要求的盈利持续性。

分析基准日为 2026年10月5日。股价采用10月2日收盘价，10月5日没有韩国正规市场的成交记录。文中区分公司发布的信息、研究机构预测和本文的计算假设。下方敏感性表是用于检验的计算，不是目标价。

<link rel="stylesheet" href="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/thesis.css">

## 基础设施正从响应调用的设备转向持续执行目标的设备

聊天机器人只在收到问题时计算。委托型代理则不同。用户交付目标后，代理会制定计划、使用工具、检查结果，并在必要时重试。即使用户关闭界面，任务仍会继续。

因此，负载的计量单位也变了。聊天机器人时代的负载接近同时在线用户数。代理时代的负载更接近用户数乘以每位用户委托的目标数，再乘以目标持续运行的时间。这就是面向目标的持续计算。

产品和价格表上已经出现了痕迹。Anthropic 的 Managed Agents 除了按 token 收费，还按会话存续时间收取每小时 0.08美元。文档解释说，这类会话保留状态，因此不适用批处理折扣。[^anthropic-pricing][^managed-agents]

Google 在2026年5月的开发者活动上介绍了运行于专用虚拟机、全天工作的个人代理。同一场发布还称，每月处理的 token 从2025年5月约480万亿个，增至2026年5月超过3.2 quadrillion个。一年约增长7倍。这是公司公开的数据，代理所占份额没有单独披露。[^google-io]

任务时长也在延长。评估机构 METR 在2026年1月测得，Claude Opus 4.5 有一半概率完成的任务，相当于人类工作320分钟。自2024年以来，这个时长约每89天翻一倍。METR 也承认，任务集合高端部分的结果存在不确定性。[^metr]

下图展示本文的整体逻辑链。每个箭头都是需要验证的联系，而非既定事实。

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/chain.svg" alt="从委托型代理到持续计算、计算提效与状态累积、融入逻辑的存储器，再到盈利持续性的逻辑链"><figcaption>概念图。需求增加与价值留在存储器制造商手中，是两条不同的逻辑联系。在移动设备上可横向滑动查看图片。</figcaption></figure>

## 紧急与非紧急任务的价格差距最高达到四倍

持续运行的任务并非都很紧急。夜间整理文件与用户等待中的答复，没有理由必须使用同一套设备。模型公司已通过定价区分这两类任务。

| 公司与模型 | 批处理或低速 | 标准 | 高速或优先 | 读取缓存上下文 |
|---|---:|---:|---:|---:|
| Anthropic Opus 5.5 | 0.5倍 | 1倍 | 2倍 | 0.05倍 |
| OpenAI gpt-6-astra | 0.5倍 | 1倍 | 2倍 | 0.1倍 |
| Google Gemini 3.1 Pro Preview | 0.5倍 | 1倍 | 1.8倍 | 另收存储费 |

三家公司都按响应速度为同一模型设置不同价格。最低档与最高档之间相差3.6至4倍。Google 还对上下文保存在缓存中的时长收费。这意味着保存上下文本身已成为独立商品。[^anthropic-pricing][^openai-pricing][^google-pricing]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/pricing.svg" alt="Anthropic Opus 5.5 相对于标准输入价格的批处理、高速和缓存读取价格倍数柱状图"><figcaption>依据 Anthropic 官方价格表，查询日期为2026年10月5日。以标准输入价格为1倍。缓存读取指再次使用已处理上下文时的输入价格。</figcaption></figure>

这种分化对投资者重要，因为它影响设备利用率。只承接实时需求的设备，昼夜开工率差异很大。如果在空闲时段以低价处理不紧急任务，同一套设备就能全天运行。持续计算不仅扩大需求，也减少设备闲置时间。

## 重复任务会转向小模型和代码

如果代理每天要重复数万次同类工作，就没有必要每次都调用最大模型。重复的细分任务会沿两个方向转移：一种是擅长特定任务的小模型，另一种是不调用模型、直接运行的代码。

小模型方向的依据是价格表。OpenAI 价格表显示，gpt-6-astra 的输入价格为每100万 token 10美元，gpt-6-luna 为0.10美元。同一家公司内部相差100倍。NVIDIA 研究人员在2025年的论文中估计，代理调用中有40~70%可由专用小模型替代。这是论文估算，不是实测比例。[^openai-pricing][^nvidia-slm]

代码方向的依据是产品文档。Anthropic 的 Agent Skills 文档说明，技能中的脚本在 shell 中运行，只有运行结果进入模型上下文，脚本代码本身不会进入上下文。这相当于把模型每次都要推理的步骤，固化为一次编写、反复执行的代码。[^agent-skills]

网页自动化公司 Skyvern 公布了一项结果：把代理执行过一次的任务转成代码，并在不调用模型的情况下重放。执行时间从279秒降至120秒，每次成本从0.11美元降至0.04美元。这是该公司自行公布的测量结果。[^skyvern]

这里需要区分两件事。每项工作的计算量会减少，但固化的代码、专用模型权重和执行记录仍需保存在某处。提效是通过减少计算、增加对已存内容的重复使用来实现的。

## 任务并非只靠 GPU 就能完成

代理的一项工作分为多个步骤。思考由 GPU 负责。运行工具、处理文件、在隔离环境中执行代码由 CPU 负责。步骤之间的数据传输由网络负责。

今年多家公司都对 CPU 需求作出了同方向的表述。Amazon 首席执行官 Andy Jassy 在7月业绩会上表示，代理使用工具时，大部分工作运行在 CPU 而非 AI 加速器上。AMD 首席执行官 Lisa Su 在8月预测，到2030年服务器 CPU 市场将达到2,200亿美元，代理和隔离执行环境将是其中最大的部分。这两项都是管理层的说明和预测。[^amzn-call][^amd-call]

也有实物层面的信号。TrendForce 在4月报道称，服务器 CPU 价格自3月以来上涨10~20%，交货期从1~2周延长至8~12周。这是转引台湾和日本媒体的二手报道。NVIDIA 已出货88核 Vera CPU，并明确将代理隔离执行列为用途。[^tf-cpu][^nvda-vera]

网络也不止一种。机架内连接芯片、机架间连接的以太网，以及扩展内存的 CXL 会同时使用。Broadcom 在9月业绩会上表示，AI 网络收入超过一年前的2.5倍，光通信激光器需求远超供应。[^avgo-call]

数据处理单元也开始独立出现。NVIDIA 在3月发布了基于 BlueField-4、用于在存储设备前管理上下文数据的设计，并称合作伙伴产品将在2026年下半年推出。截至10月5日，尚未找到可确认实际出货和运行的资料。[^nvda-stx]

结论不是 GPU 变得不重要，而是 GPU、CPU、数据处理单元和多种网络都将被需要。所有这些设备也都需要存储器。

## 计算可以重复使用，上下文和知识则会积累

把前面的逻辑浓缩成一句话：代理基础设施通过增加记忆，避免重复执行相同计算。

语言模型读取长上下文时会生成中间计算结果，这称为 KV cache。保存缓存后，再次读取相同上下文时就不必从头计算。这也是开篇提到的缓存上下文读取价格仅为标准价二十分之一的原因。

缓存的容量并不小。IBM 在6月发布的技术文档估计，中型模型每个请求的 KV cache 约为3~10GB，大型模型约为40~80GB。该文档报告称，重复使用缓存后，输入13万个 token 到首次响应的时间缩短至原来的五十六分之一。这是公司的自行测量。[^ibm-kv]

NVIDIA 为这类缓存定义了新的存储层级：GPU 内的 HBM、服务器内存、服务器中的 SSD，以及通过以太网连接、位于 SSD 下层的闪存存储层，并将其命名为 CMX。公司还推出了决定缓存应放在哪个层级的软件。[^nvda-cmx][^nvda-dynamo]

存储器公司的业绩发布也出现了同样的表述。Micron 在9月30日的发布中称，数据中心 SSD 季度收入接近100亿美元，超过一年前的10倍。公司将把 KV cache 下沉保存的上下文存储列为原因之一。[^mu-remarks]

SK hynix 在7月业绩会上称，企业级 SSD 收入达到上一季度的两倍，并将 KV cache 保存和放在 GPU 附近的存储设备列为新用途。Samsung Electronics 预计服务器 SSD 将占2026年 NAND 收入的60%以上。这两项说法通过转载业绩会实录的媒体核对。[^skh-call][^sec-call]

硬盘公司 Western Digital 的首席执行官在8月这样描述这一差异：计算周期可以重复使用，数据却会复利式积累。代理会在每个步骤留下记录，这些记录又会成为下一项工作的材料。[^wdc-call]

但增长率和金额需要分开看。单个用户的个人代理记忆从容量上看并不大。决定金额规模的是整个推理服务是否改为把缓存下沉到闪存中保存。这种转变仍处于早期阶段。

## 存储器正从标准化产品转向融入逻辑的产品

随着积累的数据增加，客户对存储器的要求也会改变。客户不再只问容量，还会问能否及时取用、功耗多少，以及与自家芯片的匹配程度。要满足这些要求，逻辑就需要进入存储器。

SK hynix 在7月提交的美国上市招股说明书中直接写到了这种变化。文件称，过去存储器公司供应通用部件，而 AI 时代的存储器在性能优化中发挥核心作用，并将公司的愿景表述为全栈 AI 存储器创造者。这是公司对自身的定位，需要与已由业绩证明的事实区分。[^skh-424b4]

最靠前的案例是 HBM 的基底裸片。HBM 是多层堆叠的存储芯片，基底裸片位于最底层，负责信号和电力。前几代产品采用存储器工艺制造。从 HBM4 开始，则改用逻辑工艺。Samsung Electronics 使用自有4纳米工艺。SK hynix 在2024年宣布与 TSMC 合作，使用 TSMC 的逻辑工艺制造 HBM4 基底裸片。[^sec-hbm4][^skh-tsmc]

下一步是将客户的逻辑放入基底裸片的定制 HBM。NVIDIA 于8月26日发布 NVHBM，将自家的存储器控制电路置入 HBM 基底裸片。NVIDIA 称，与标准 HBM4E 相比，带宽增加30%，功耗降低15%。Micron 在9月30日表示将与 NVIDIA 共同开发该产品。[^nvda-nvhbm][^mu-remarks]

Samsung Electronics 在8月的半导体学术会议 Hot Chips 上提出了更进一步的阶段：迁移控制电路、在基底裸片中加入计算单元以分担处理器的部分计算，以及将存储器直接堆叠在计算芯片上。公司没有给出产品上市时间。[^sec-hotchips]

存储设备和其他存储器也出现了方向相同的产品，但各产品的成熟度差异很大。

| 产品 | 融入的逻辑 | 当前阶段 |
|---|---|---|
| HBM4 基底裸片 | 通过逻辑工艺实现信号和电力控制 | 量产，已有收入 |
| SOCAMM2 | 服务器低功耗存储器模组 | 量产，销售增长 |
| 企业级 SSD | 控制芯片、固件及上下文存储设计 | 量产，收入大增 |
| 定制 HBM、NVHBM | 客户的存储器控制电路 | 开发中，计划用于下一代 GPU |
| CXL 存储器模组 | 识别常用数据的监测电路 | 据报道 Samsung 目标于2026年底量产，可能延迟 |
| HBF | 将 NAND 靠近计算芯片的高带宽接口 | 2026年8月公布首个技术规范，产品尚未推出 |
| PIM、内置计算单元的 HBM | 存储器中的计算电路 | 原型和路线图阶段 |

列为量产阶段的产品可在今年业绩资料中得到确认。Samsung Electronics 第二季度业绩资料将 HBM 基底裸片需求增加列为晶圆代工业务的业绩因素。从定制 HBM 开始及其下方列出的产品，尚未有收入证据。SK hynix 表示 HBM4E 之前仍将沿用现有键合方式；9月行业活动上也有人评价 CXL 是 HBM 的补充层，而非替代品。[^sec-ir][^skh-q2][^tf-cxl][^hbf-ocp][^sec-fms][^skh-hybrid][^tf-cxl-doubt]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/maturity.svg" alt="将融入逻辑的存储器产品分为已有收入、开发与样品、路线图三个阶段的图示"><figcaption>依据公司发布和业绩资料划分阶段。越靠左，越能在今年业绩中确认；越靠右，时间表越不确定。基准日为2026年10月5日。</figcaption></figure>

因此，存储器融入逻辑的方向判断成立，但目前覆盖范围仍窄。目前能够从收入中确认的是 HBM4、服务器模组和企业级 SSD。通用 DRAM 与 NAND 仍按规格和价格竞争。

## 存储器成为计算中心的假设目前只验证了方向

更远期的假设是计算架构本身会改变。当前计算机以计算设备为中心，由存储器提供数据。如果数据增长快于计算，搬运数据的成本就会超过计算成本。这时，在数据所在位置计算会更合适。

多个公司正在尝试这个方向。Samsung Electronics 路线图的最后阶段是把存储器直接堆叠在计算芯片上。Qualcomm 表示将在2027年产品中采用三维融合计算与存储器的架构。SK hynix 和 Sandisk 则与 Google、Tenstorrent 共同制定标准，把 NAND 放在计算芯片旁边。[^sec-hotchips][^qcom-hbc][^hbf-ocp]

Sandisk 首席执行官在8月业绩会上称，AI 从根本上说是以存储器为中心、对存储有大量需求的问题。需要考虑到这句话出自存储器公司的首席执行官。[^sndk-call]

我对这一假设的判断很明确：截至2026年，以存储器为中心的计算是一个选择权，而不是投资依据。目前没有独立性能验证、量产时间表或已确认的客户采用情况。它不能用来解释当前股价。不过，如果方向判断正确，最大受益者将是同时拥有存储器、逻辑工艺和堆叠技术的公司。

## 韩国存储器的投资逻辑从盈利规模转向盈利持续时间

现在转向韩国企业。今年的盈利已经很高。Samsung Electronics 半导体部门第二季度营业利润为89.2万亿韩元，相当于营收的70%。SK hynix 第二季度营业利润为60.5万亿韩元，相当于营收的76%。[^sec-ir][^skh-q2]

但股价并未给予这些盈利很高的估值。按10月2日收盘价，Samsung Electronics 的股价相当于2026年预期盈利的5.85倍，SK hynix 为5.25倍。预期盈利采用 Naver Finance 汇总的券商平均值。[^naver-sec][^naver-skh]

低估值可以解读为市场仍把存储器视为周期性行业。市场担心当前盈利来自供应短缺，扩产完成后盈利会像过去一样大幅下滑。这是一种解读，但有依据。SK hynix 自己也在招股说明书风险因素中列出了存储器行业反复出现的供过于求。[^skh-424b4]

融入逻辑的存储器之所以对投资重要，原因就在这里。这种变化不会让今年盈利进一步扩大。关键在于，它可能为供应恢复正常后盈利不再像过去那样大幅下降提供理由。理由来自转换成本和合同结构。

第一，客户更难更换供应商。根据客户芯片设计的基底裸片，无法轻易换成另一家公司的产品。设计、验证和认证所需时间构成转换成本。实际转换成本有多高，以及能否体现为价格，目前仍是未经验证的假设。

第二，合同结构。Micron 于9月30日表示已签订26份战略客户合同。客户即使没有购买多年约定的数量，也需要支付相应款项。客户提供的财务承诺为320亿美元，其中大部分是现金保证金。Micron 表示，将依据这种可见度增加资本开支。[^mu-remarks]

韩国两家公司也朝同一方向发展。SK hynix 表示第二季度已与约10家客户完成长期供货合同谈判，并在业绩会上说明合同包含保证金等财务安排。Samsung Electronics 表示计划将60~70%的产能分配给长期合同，基本期限为5年并逐年续约。合同价格和取消条件没有公开。[^skh-q2][^skh-lta][^sec-lta]

客户预先交钱并承诺采购的行业，与按现货交易标准化商品的行业会有不同表现。但长期合同有两面性。TrendForce 指出，长期合同中的价格机制使部分供应商的服务器 DRAM 涨价幅度低于市场平均水平。供应商以放弃上涨周期的顶部，换取下跌周期的底部支撑。[^tf-memory]

## Samsung Electronics 与 SK hynix 在不同位置面对同一变化

两家公司面对融入逻辑的存储器这一相同变化，各有不同优势和短板。

| 项目 | Samsung Electronics | SK hynix |
|---|---|---|
| 第二季度半导体营业利润率 | 70% | 76% |
| HBM4 基底裸片 | 自有4纳米工艺 | TSMC 工艺 |
| 逻辑价值归属，本文分析 | 可能通过晶圆代工业务留在公司内部 | 成为对外支付的成本 |
| 产品范围 | HBM、服务器模组、SSD、晶圆代工、封装 | HBM、服务器模组、SSD、主导 HBF 规范 |
| 长期合同 | 计划分配60~70%产能 | 已与约10家客户完成谈判 |
| 股东回报 | 计划第三季度派发约30万亿韩元股息 | 决议回购并注销40万亿韩元股份 |
| 相对于2026年预期盈利的股价 | 5.85倍 | 5.25倍 |

SK hynix 的优势在于当前盈利能力和客户关系。其营业利润率更高，并已与约10家客户完成长期供货合同谈判。短板是逻辑价值支付给外部。TrendForce 援引韩国媒体称，TSMC 制造的 HBM4 基底裸片成本是存储芯片的3~4倍。公司没有确认这个数字。[^tf-basedie]

Samsung Electronics 的优势在于逻辑价值可能留在公司内部。公司自称是唯一同时拥有存储器、逻辑设计、晶圆代工和封装业务的企业。[^sec-fms]短板是这种结构尚未充分转化为利润。不能把内部制造的基底裸片收入，当作从外部客户赚取的钱重复计算。必须以合并口径成本和现金来确认。

股东回报是盈利返回股东的途径。SK hynix 于8月决议回购并注销价值40万亿韩元的股份，并将自由现金流回报目标提高到50%以上。Samsung Electronics 计划在第三季度派发约30万亿韩元现金股息，并将在10月底由董事会最终确定。两项信息均由媒体报道确认，尚未核对公告原文。[^skh-return][^sec-return]

我的判断是，存储器融入逻辑的趋势越深入，结构上越有利于在内部制造逻辑的公司。以当前业绩和客户地位看，SK hynix 领先。在变化初期，SK hynix 的执行力更突出；随着定制 HBM 及后续阶段逐渐成熟，Samsung Electronics 的整合架构可能更有价值。转折点将是 Samsung Foundry 制造的基底裸片采用外部客户设计并实现量产。

## 当前股价假设今年盈利中只有略多于一半能够留存

简单来看，股价等于市场认可的可持续盈利乘以估值倍数。假设市场给予存储器公司10倍估值，反推即可得出当前股价要求的盈利水平。

Samsung Electronics 10月2日收盘价为KRW 276,000。按10倍估值计算，股价所要求的每股盈利为KRW 27,600，相当于2026年预期每股盈利KRW 47,142的58.5%。SK hynix 收盘价为KRW 1,842,000；同样计算，要求每股盈利为KRW 184,200，相当于预期每股盈利KRW 350,576的52.5%。[^naver-sec][^naver-skh]

也就是说，当前股价与2026年盈利中略多于一半可以持续的假设相符。这不代表市场的真实想法只有这一种。估值倍数和盈利水平有多种组合。不过，问题已经很清楚：融入逻辑的产品和长期合同，能否使正常化后的盈利高于今年盈利的一半？

下表调整了2026年预期盈利留存比例和估值倍数。括号内为相对于10月2日收盘价的变动率。留存比例和估值倍数均为本文的计算假设，不代表概率。未计入股息。

Samsung Electronics，基准股价 KRW 276,000

| 2026年预期盈利留存比例 | 8倍 | 10倍 | 12倍 |
|---|---:|---:|---:|
| 40% | 151,000韩元 (-45.3%) | 189,000韩元 (-31.7%) | 226,000韩元 (-18.0%) |
| 55% | 207,000韩元 (-24.8%) | 259,000韩元 (-6.1%) | 311,000韩元 (+12.7%) |
| 70% | 264,000韩元 (-4.3%) | 330,000韩元 (+19.6%) | 396,000韩元 (+43.5%) |

SK hynix，基准股价 KRW 1,842,000

| 2026年预期盈利留存比例 | 8倍 | 10倍 | 12倍 |
|---|---:|---:|---:|
| 40% | 1,122,000韩元 (-39.1%) | 1,402,000韩元 (-23.9%) | 1,683,000韩元 (-8.6%) |
| 55% | 1,543,000韩元 (-16.3%) | 1,928,000韩元 (+4.7%) | 2,314,000韩元 (+25.6%) |
| 70% | 1,963,000韩元 (+6.6%) | 2,454,000韩元 (+33.2%) | 2,945,000韩元 (+59.9%) |

表格两端展示了核心问题。如果盈利只留存40%，即使估值升至12倍，股价也会低于当前水平。行业故事无法弥补盈利下降。相反，如果市场相信盈利能留存70%，即便估值仍为10倍，股价也会高出20~33%。

SK hynix 的数据需要特别注意。第二季度净利润为93.9万亿韩元，高于营业利润60.5万亿韩元。我们未能确认原因。如果这部分盈利来自营业外项目，年度预期每股盈利中也可能包含不可重复的收益，此时应采用更低的留存比例。[^skh-q2]

重估的关键不是估值倍数，而是盈利留存比例。融入逻辑的存储器和长期合同可能提高这一比例。能否提高，要等到2027年和2028年供应增加时才能见分晓。

## 最强反论是逻辑的价值可能归设计方所有

这套逻辑面临强有力的反论。下面从影响最大的问题开始讨论。

第一，价值归属。NVHBM 基底裸片中的控制电路由 NVIDIA 设计。NVIDIA 表示，多家存储器公司将供应相同规格的产品。Micron 则把基底裸片生产外包给晶圆代工厂。在这种结构中，设计价值归 NVIDIA，制造价值归晶圆代工厂，存储器公司可能再次围绕相同规格竞争。[^nvda-nvhbm][^mu-foundry]

存储设备也有类似情况。在 NVIDIA 的上下文存储设计中，管理数据的计算发生在 NVIDIA 的数据处理单元，而不是 SSD 内部。决定缓存放在哪一层的软件也属于 NVIDIA。数据积累的位置与客户难以离开的位置，可能并不相同。[^nvda-cmx][^nvda-dynamo]

这个反论对本文逻辑的冲击最大。逻辑进入存储器，与存储器公司拥有这套逻辑，是两回事。本文强调 Samsung Electronics 的整合架构，原因之一正是这个反论。无法自行制造逻辑的存储器公司，可能随着产品复杂度提高而处于更狭窄的位置。

第二，需求适应。如果存储器变贵，客户会寻找少用存储器的方法。TrendForce 于9月29日称，GPU 和定制芯片厂商正在考虑减少每台设备的 HBM 容量，并优先评估2027年的8层配置。Google 研究人员在3月公布了可将 KV cache 内存占用压缩至六分之一以下的方法。Anthropic 文档指出，上下文越长，准确度可能下降，并提供将旧对话压缩为摘要的功能。[^tf-hbm][^turboquant][^anthropic-context]

积累速度能否快过压缩技术降低需求的速度，目前没有答案。Micron 也承认，由于价格因素，单台服务器搭载存储器的增长率有所放缓。[^mu-remarks]

第三，供应与资金。TrendForce 于7月30日预测，NAND 供应将在2027年下半年缓解，并带来价格下行压力。据 TrendForce 报道，中国 CXMT 第二季度 DRAM 收入份额升至9.5%。国际清算银行行长在9月10日的演讲中警告，大型科技公司的资本支出已超过其现金流。客户资金紧张时，长期合同的承诺也会受到考验。[^tf-supply][^tf-china][^bis]

Micron 的看法正好相反，认为2027年和2028年的供需将比2026年更紧张。研究机构与供应商预测相互分歧，这本身就是不应对2027年作出确定判断的理由。[^mu-remarks]

需求前提也需要检验。本文的出发点是人们会持续把工作交给代理。Anthropic 在2月公布的自有使用数据中，单次持续超过45分钟的任务只占最高的0.1%。大多数任务短得多。如果委托不能成为习惯，或用户不愿交出权限，持续计算的发展速度就会低于本文假设。[^anthropic-autonomy]

## 下一季度要确认盈利留存的依据，而非只看价格

未来公布的数据可以检验这套逻辑是否成立。下表列出需要跟踪的项目，以及会改变判断的条件。

| 观察项目 | 支持逻辑的信号 | 削弱逻辑的信号 |
|---|---|---|
| 第三季度业绩，10月 | HBM4 和企业级 SSD 出货增加，产品组合改善 | 盈利增长大部分来自通用产品涨价 |
| 长期合同 | 披露保证金和最低采购条件，合同续期 | 价格上限牺牲盈利，持续不披露条件 |
| 定制 HBM | Samsung Foundry 基底裸片获得外部客户订单并量产 | 三家公司按单一规格展开价格竞争 |
| 上下文存储 | CMX 合作伙伴产品出货，签订专用存储服务器合同 | 压缩技术普及，出货延迟 |
| 2027年供应 | 合同价格持续上涨，客户上调投资计划 | NAND 价格下跌，HBM 搭载量减少 |

媒体报道称，Samsung Electronics 第三季度初步业绩将于10月8日公布。FnGuide 汇总的营业利润平均值为108.1万亿韩元。SK hynix 预计在10月底发布业绩，营业利润平均值为77.2万亿韩元。两项均依据截至10月5日的报道，尚未确认公司的正式日程公告。[^consensus]

需要看的是业绩构成，而不是单看数字。如果营业利润超过平均值，但原因只有通用产品涨价，就与本文逻辑无关。即使营业利润低于平均值，只要 HBM4 出货量和长期合同质量提高，盈利留存的依据反而会增加。

也要明确改变判断的条件。如果定制 HBM 固化为单一规格，三家存储器公司以相同产品竞争，同时2027年合同价格开始下降，本文逻辑就应下调一个级别。在这种情况下，韩国存储器虽能制造更精密的产品，仍会被视为周期性行业。

<strong>代理通过使用记忆来节省计算。承载记忆的产品正在融入逻辑，一些客户也开始预先支付资金。韩国存储器的重估取决于供应增加后，这些变化能否继续支撑盈利；当前股价仍只相信今年盈利中略多于一半能够留存。</strong>

## 来源与计算边界

公司发布、公告和研究机构资料均于2026年10月5日核对。通过转载业绩会实录的媒体核实的发言已在脚注标明。公司公布的性能数据未经独立验证。敏感性表中的盈利留存比例和估值倍数均为计算假设，不是预测。预期每股盈利采用 Naver Finance 汇总值，未能确认2027年预期数据。

[^anthropic-pricing]: [Anthropic 官方价格表](https://platform.claude.com/docs/en/about-claude/pricing)，查询于2026-10-05。Opus 5.5 标准输入4美元、批处理2美元、高速8美元、缓存读取0.20美元（每100万 token）。含 Managed Agents 会话费用。

[^managed-agents]: [Claude Managed Agents 概览文档](https://platform.claude.com/docs/en/managed-agents/overview)，查询于2026-10-05。该文档介绍的是 Beta 产品。

[^google-io]: [Google I/O 2026 Sundar Pichai 主题演讲摘要](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)，2026-05。公司公开数据。

[^metr]: [METR Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/)，2026-01-29。成功概率为50%的时间跨度。

[^openai-pricing]: [OpenAI API 价格表](https://developers.openai.com/api/docs/pricing)，查询于2026-10-05。gpt-6-astra 标准价10美元、Flex 5美元、Fast 20美元、缓存输入1美元。gpt-6-luna 输入价0.10美元。

[^google-pricing]: [Gemini API 价格表](https://ai.google.dev/gemini-api/docs/pricing)，更新于2026-10-01。Gemini 3.1 Pro Preview 标准价2美元、批处理1美元、Priority 3.60美元，缓存按小时收费。

[^nvidia-slm]: [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153)，NVIDIA 研究人员，提交于2025-06-02。论文阐述研究观点，40~70%为估算。

[^agent-skills]: [Anthropic Agent Skills 概览文档](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)，查询于2026-10-05。

[^skyvern]: [Skyvern 博客中的代码重放测量](https://www.skyvern.com/blog/asking-ai-to-build-scrapers-should-be-easy-right/)，发布于2025-10-17，更新于2026-08-24。公司自行测量。

[^amzn-call]: [Amazon 2026年第二季度业绩会实录转载](https://www.investing.com/news/transcripts/earnings-call-transcript-amazon-tops-q2-2026-estimates-as-aws-growth-accelerates-93CH-4826442)，2026-07-30。管理层发言。

[^amd-call]: [AMD 2026年第二季度业绩会实录转载](https://www.fool.com/earnings/call-transcripts/2026/08/11/amd-amd-q2-2026-earnings-call-transcript/)，2026-08-04业绩会。市场规模为公司预测。

[^tf-cpu]: [TrendForce 服务器 CPU 价格报道](https://www.trendforce.com/news/2026/04/22/news-server-cpu-prices-up-as-much-as-20-since-march-intel-may-raise-prices-another-8-10-in-2h26/)，2026-04-22。转引台湾和日本媒体。

[^nvda-vera]: [NVIDIA Vera CPU 出货公告](https://blogs.nvidia.com/blog/vera-cpu-delivery/)，2026-05-18。

[^avgo-call]: [Broadcom FY2026 第三季度业绩会实录转载](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)，2026-09-02业绩会。管理层发言。

[^nvda-stx]: [NVIDIA 发布 BlueField-4 STX 存储架构](https://nvidianews.nvidia.com/news/nvidia-launches-bluefield-4-stx-storage-architecture-with-broad-industry-adoption)，2026-03-16。性能数据为公司说法。

[^ibm-kv]: [IBM Redbooks KV cache 技术文档](https://www.redbooks.ibm.com/docs/MD260021/MD260021.html)，发布于2026-06-05。公司自行测量和估算。

[^nvda-cmx]: [NVIDIA CMX 产品说明](https://www.nvidia.com/en-us/data-center/ai-storage/cmx/)，查询于2026-10-05。未标明发布日期。

[^nvda-dynamo]: [NVIDIA Dynamo KV cache 分层文档](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/kv-cache-offloading)，查询于2026-10-05。文档未提供性能数据。

[^mu-remarks]: [Micron FY2026 第四季度准备发言](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)，2026-09-30。数据中心 SSD 收入原文表述为 "nearly $10 billion"。依据此文核对战略客户合同、保证金、NVHBM 和供需预测。

[^skh-call]: [SK hynix 2026年第二季度业绩会实录转载](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q2-2026-results-as-shares-fall-93CH-4818480)，2026-07业绩会。非公司官方实录。

[^sec-call]: [Samsung Electronics 2026年第二季度业绩会实录转载](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q2-2026-profit-as-ai-demand-surges-93CH-4822292)，2026-07业绩会。非公司官方实录。

[^wdc-call]: [Western Digital FY2026 第四季度业绩会摘要](https://finance.biggo.com/news/US_WDC_2026-08-05)，2026-08-05。经二手摘要核实的发言。

[^skh-424b4]: [SK hynix 美国上市招股说明书，SEC 424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm)，2026-07-09。已核对原文中的战略章节、Custom HBM 术语定义及风险因素。

[^sec-hbm4]: [Samsung Electronics 宣布 HBM4 量产出货](https://news.samsungsemiconductor.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/)，2026-02-12。工艺和性能为公司说明。

[^skh-tsmc]: [SK hynix 与 TSMC 宣布 HBM4 合作](https://www.prnewswire.com/news-releases/sk-hynix-partners-with-tsmc-to-strengthen-hbm-technological-leadership-302120755.html)，2024-04-18。当时公布的开发方向。

[^tf-basedie]: [TrendForce 关于 SK hynix HBM4E 基底裸片的报道](https://www.trendforce.com/news/2026/08/31/news-sk-hynix-reportedly-weighs-intel-for-hbm4e-base-dies-amid-tsmc-cost-pressure-and-supply-diversification/)，2026-08-31。转引韩国媒体，公司未确认。

[^nvda-nvhbm]: [NVIDIA 发布 NVHBM](https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory/)，2026-08-26。带宽和功耗数据为公司说法。

[^sec-hotchips]: [ServeTheHome 对 Samsung Electronics Hot Chips 2026 发布的整理](https://www.servethehome.com/samsung-evolving-hbm-base-die-at-hot-chips-2026/)，2026-08-23。路线图来自公司发布，未提供时间表。

[^sec-ir]: [Samsung Electronics 2026年第二季度业绩说明资料](https://images.samsung.com/kdp/ir/events/2026/2026_2Q_conference_kor.pdf)，2026-07-30。半导体部门营收127.5万亿韩元、营业利润89.2万亿韩元。晶圆代工业务业绩因素中提及 HBM 基底裸片。

[^skh-q2]: [SK hynix 2026年第二季度业绩发布](https://news.skhynix.com/en/q2-2026-business-results/)，2026-07-29。营收79.3万亿韩元、营业利润60.5万亿韩元、净利润93.9万亿韩元；另涉及长期供货合同和 SOCAMM2。

[^tf-cxl]: [TrendForce 关于 Samsung 与 SK hynix CXL 3.2 的报道](https://www.trendforce.com/news/2026/07/21/news-samsung-reportedly-targets-2026-cxl-3-2-mass-production-sk-hynix-advances-new-ai-memory-architecture/)，2026-07-21。二手报道。

[^hbf-ocp]: [Sandisk 与 SK hynix 发布首个 HBF OCP 规范](https://www.storagenewsletter.com/2026/08/05/fms-2026-sandisk-and-sk-hynix-advance-global-standardization-of-high-bandwidth-flash-with-release-of-first-ocp-technical-specification/)，2026-08-05。

[^sec-fms]: [StorageReview 整理 Samsung Electronics 在 FMS 2026 的发布](https://www.storagereview.com/news/samsung-outlines-3d-memory-roadmap-for-ai-infrastructure-at-fms-2026)，2026-08-04。发布了搭载 PIM 的低功耗存储器，量产时间未确认。

[^skh-hybrid]: [Tom's Hardware 报道 SK hynix 在 Hot Chips 2026 的发布](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling)，2026-08-24。

[^tf-cxl-doubt]: [TrendForce 关于 AI Infrastructure Summit 的报道](https://www.trendforce.com/news/2026/09/18/news-openai-intel-reportedly-downplay-cxl-as-hbm-replacement-citing-use-case-and-data-transfer-limits/)，2026-09-18。二手报道。

[^qcom-hbc]: [Qualcomm 发布数据中心路线图](https://www.qualcomm.com/news/releases/2026/06/qualcomm-unveils-comprehensive-data-center-roadmap-for-the-agent)，2026-06。性能数据依据公司说法，尚未经独立验证。

[^sndk-call]: [Sandisk FY2026 第四季度业绩会实录转载](https://www.fool.com/earnings/call-transcripts/2026/08/12/sandisk-sndk-q4-2026-earnings-call-transcript/)，2026-08-05业绩会。

[^naver-sec]: [Naver Finance Samsung Electronics 每日股价](https://m.stock.naver.com/api/stock/005930/price?pageSize=5&page=1)及[年度业绩汇总](https://m.stock.naver.com/api/stock/005930/finance/annual)，查询于2026-10-05。10-02收盘价276,000韩元，2026年预期每股盈利47,142韩元。

[^naver-skh]: [Naver Finance SK hynix 每日股价](https://m.stock.naver.com/api/stock/000660/price?pageSize=5&page=1)及[年度业绩汇总](https://m.stock.naver.com/api/stock/000660/finance/annual)，查询于2026-10-05。10-02收盘价1,842,000韩元，2026年预期每股盈利350,576韩元。

[^skh-lta]: [Newspim 关于 SK hynix 第二季度业绩会的报道](https://www.newspim.com/news/view/20260729000198)，2026-07-29。保证金相关发言由报道核实。

[^sec-lta]: [The Elec 发布的 Samsung Electronics 第二季度业绩会全文](https://www.thelec.kr/news/articleView.html?idxno=60316)，2026-07-30。长期合同占比和方式属于管理层计划。

[^tf-memory]: [TrendForce 2026年第四季度存储器合约价格预测](https://www.trendforce.com/presscenter/news/20260930-13258.html)，2026-09-30。属于预测，非已实现价格。

[^skh-return]: [ZDNet Korea 关于 SK hynix 注销库存股的报道](https://zdnet.co.kr/view/?no=20260819161157)，2026-08-19。未核对公告原文。

[^sec-return]: [Samsung Electronics 2026年股东回报公告报道](https://v.daum.net/v/20260821172850433)，2026-08-21。属于计划，非已支付金额。

[^mu-foundry]: [The Elec 关于 Micron 外包基底裸片的报道](https://www.thelec.net/news/articleView.html?idxno=14372)，2026-10-02。Micron 准备发言原文未提及晶圆代工厂名称。

[^tf-hbm]: [TrendForce 2027年 HBM 预测](https://www.trendforce.com/presscenter/news/20260929-13255.html)，2026-09-29。研究机构预测。

[^turboquant]: [Google Research 介绍 TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)，2026-03-24。属于研究成果，商业服务的应用范围尚未确认。

[^anthropic-context]: [Anthropic 上下文窗口文档](https://platform.claude.com/docs/en/build-with-claude/context-windows)及[压缩文档](https://platform.claude.com/docs/en/build-with-claude/compaction)，查询于2026-10-05。

[^anthropic-autonomy]: [Anthropic 关于代理自主性的测量研究](https://www.anthropic.com/research/measuring-agent-autonomy)，2026-02-18。自有使用数据的99.9百分位数。

[^tf-supply]: [TrendForce 2026~2027年存储器供需预测](https://www.trendforce.com/presscenter/news/20260730-13158.html)，2026-07-30。研究机构预测。

[^tf-china]: [TrendForce 关于 CXMT、YMTC 扩产的报道](https://www.trendforce.com/news/2026/09/24/news-cxmt-ymtc-ramp-memory-capacity-but-chinas-ai-cloud-boom-could-soak-up-new-supply-through-2027/)，2026-09-24。二手报道。

[^bis]: [国际清算银行行长演讲](https://www.bis.org/speeches/20260910-artificial-intelligence-growth-and-financial-stability-challenges-central-banks)，2026-09-10。

[^consensus]: [MoneyToday 关于第三季度业绩预测的报道](https://www.mt.co.kr/amp/stock/2026/10/05/2026100217315021825)，2026-10-05。引述 FnGuide 汇总数据。

*免责声明：本文仅用于研究和信息提供。公司、估值倍数和情景均为分析示例，投资决定须由读者另行审慎判断。*
