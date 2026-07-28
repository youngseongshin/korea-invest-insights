---
title: "为何美国数据中心正在延误：ERCOT 的打法，以及对 Big Tech 和半导体的时间线影响"
slug: "us-datacenter-power-delay-ercot-renewables-bess-bigtech-semiconductor-2026-07-28"
date: 2026-07-28T21:45:00+09:00
description: "基于来源核查的美国数据中心延误分析，涵盖电网并网、变压器、燃气轮机和地方反对；解释 ERCOT 为何凭借 40.3 GW 太阳能、22.0 GW 电池储能和 5.1 GW 需求响应降低风险；以及这一瓶颈对 Big Tech、GPU、HBM、存储器和电力设备股票的含义。"
categories: ["独家分析", "市场展望", "技术分析"]
tags:
  - "美国数据中心"
  - "AI 基础设施"
  - "电网"
  - "ERCOT"
  - "BESS"
  - "太阳能"
  - "Big Tech"
  - "Nvidia"
  - "HBM"
  - "Samsung Electronics"
  - "SK hynix"
  - "电力设备"
  - "研究 OS"
draft: false
---

> 背景：在[Big Tech 的 AI 财报三部曲](/zh/post/big-tech-ai-earnings-capex-roi-memory-2028-fcf-2026-07-22/)中，关键的 2028 年问题是 AI 资本开支能否转化为收入和自由现金流。我们的[韩国数据中心受益者排名](/zh/post/korea-ai-datacenter-beneficiaries-power-cooling-operator-flow-ranking-2026-07-23/)和[AI 数据中心电力瓶颈图谱](/zh/post/ai-datacenter-power-bottleneck-korea-value-chain-screen-2026-07-04/)认为，电力、冷却和备用电源供应商的变现早于运营商。本报告将该框架应用于美国。

## TL;DR

- 美国数据中心延误是真实存在的，尽管没有单一的全国性登记系统能给出确切的取消比例。Allianz Research 概述称，计划于 2026 年投产的约 12 GW 美国容量可能延误或取消，而实际在建的仅约 5 GW。NERC 还确认，多个地区因并网和完工进度慢于预期而下调了大负荷预测。[^allianz][^nerc]
- 瓶颈有四个层面：<strong>电网并网、变压器和断路器、发电设备，以及地方许可和成本分摊</strong>。截至 2025 年末，美国并网队列中等待的发电项目为 1,312 GW，储能项目为 749 GW。2026 年初，发电机升压变压器交付周期超过 160 周。[^lbl][^reuters-transformer]
- “超过半数美国州面临电力短缺警报”的说法夸大了官方评估。NERC 认为，在正常夏季峰值条件下所有地区资源充足，但指出部分地区在极端条件下风险较高。[^nerc]
- ERCOT 是太阳能加储能论点的有力证据。NERC 列出的 ERCOT 太阳能为 40.3 GW，电池储能为 22.0 GW，预期峰值贡献分别为 29.7 GW 和 20.7 GW。最高风险时段发生能源紧急警报的概率从 3.1% 降至 0.43%。[^nerc]
- 但 ERCOT 并非仅靠太阳能和电池的故事。其成果还反映了 5.1 GW 需求响应、可削减的计算负荷、更快的市场规则，以及既有的燃气、核电和风电基础。
- 太阳能加 BESS 是未来三年最快的增量供电选择，但不是完整的 24/7 解决方案。实用架构是<strong>太阳能+BESS、既有核电或燃气 PPA、表后燃气发动机或燃料电池，以及灵活计算负荷</strong>。
- 对 Big Tech 而言，延误限制短期增长，但提高已通电容量的稀缺价值。对半导体而言，这既带来短期出货时点风险，也可能延长 2027-2028 年需求周期。

<div class="thesis-callout">
  <div class="thesis-callout__label">核心结论</div>
  <div class="thesis-callout__body">
    AI 的瓶颈已从芯片转移到电力。ERCOT 的启示不是“仅靠可再生能源”，而是快速新增资源、电池、灵活并网、需求响应和稳定发电的组合。股票影响将在三种不同的时钟下到来：Big Tech 面临短期增长上限，半导体安装推迟至 2027-2028 年，以及电力设备和储能供应商获得直接订单。
  </div>
</div>

## 0. 先厘清定义

数据中心“容量”可以指 IT 负荷、设施总用电功率，或最终公布的园区规模。“并网队列”可以指发电项目，也可以指大型负荷。混用这些概念会产生看似惊人但具有误导性的数字。

| 常见说法 | 证据核查 | 工作假设 |
|---|---|---|
| 美国当前数据中心容量为 50 GW | 估计值因范围而异 | Wood Mackenzie 估计当前约为 24 GW，到 2030 年为 110 GW。[^reuters-transformer] |
| 2026 年项目中有 30-50% 延误 | 行业估计，并非官方普查 | 关注方向，而非虚假的点估计。Allianz 称计划容量为 12 GW，而在建容量约为 5 GW。[^allianz] |
| 半数美国州面临短缺警报 | 比 NERC 的表述更强烈 | 正常条件下所有地区资源充足；部分地区面临较高的极端天气风险。[^nerc] |
| ERCOT 已超过 90 GW | 超过 92 GW 是预测值 | ERCOT 夏季预测超过 92 GW；NERC 经需求响应调整的规划数字更低。[^kera][^nerc] |
| ERCOT 有 35 GW 太阳能和 12 GW BESS | 方向正确但数据陈旧 | NERC 列出 2026 年为 40.3 GW 太阳能和 22.0 GW BESS。[^nerc] |
| 美国队列规模为 2.6 TW | 取决于日期和范围 | 截至 2025 年末，活跃的发电和储能队列合计为 2.061 TW。这并非数据中心负荷队列本身。[^lbl] |

## 1. 延误规模有多大？

美国没有完整的数据中心项目登记册。单个园区可能有已公布的最终容量、较小的首栋建筑容量，以及多个分阶段通电日期。“延误”“取消”“暂停”和“持有土地但没有电力”并不相同。

不过，三个独立信号一致：

1. Allianz Research 表示，计划于 2026 年投产的约 12 GW 美国容量可能延误或取消，而实际在建容量仅约 5 GW。[^allianz]
2. NERC 表示，多个评估区域因并网和完工慢于此前预期而下调大负荷预测。[^nerc]
3. 媒体报道援引 Data Center Watch 的统计称，2026 年第一季度有 75 个项目、价值约 $130 billion 被阻止或延误。[^dcwatch]

可辩护的结论并非恰好有一半项目会消失，而是已宣布的 AI 容量推进速度快于电力交付和建设速度，从而将相当一部分 2026 年供给推迟至 2027 年及以后。

## 2. 四层瓶颈

| 层级 | 已验证指标 | 重要原因 |
|---|---:|---|
| 发电和储能并网 | 2025 年末活跃容量 2,061 GW；2025 年完工项目的投运时间中位数超过五年 | 没有供给和输电，新增负荷无法扩张。 |
| 大负荷并网 | PJM 数据中心增长区域为 36-48 months | 完工的建筑壳体在没有通电日期时无法变现。 |
| 变压器和断路器 | 升压变压器超过 160 周；高压断路器约 125 周 | 缺少一个组件就可能拖住整座变电站。 |
| 许可、电价和地方反对 | 2026 年 Q1 有 75 个项目和 $130 billion 被延误或阻止 | 用水、噪声、土地和成本转嫁都可能中止建设。 |

发电和储能队列约含 8,200 个项目。截至 2025 年末，2000 至 2020 年申请容量中仅有 13% 已实现商业运营。[^lbl] 因此，队列规模不等于未来供给。

设备是更紧迫的物理约束。Reuters 报道称，2026 年第一季度发电机升压变压器交付周期超过 160 周，高压断路器达到 125 周。公用事业公司如今提前数年订购，有时还会预付制造产能档期。[^reuters-transformer]

燃气轮机也不是即时替代方案。Mitsubishi Power 表示，订单已排至 2030 年，安装交付周期已延长至五年或更久。[^gas-turbine]

## 3. 瓶颈已从机架转向变电站

变现链条如下：

```text
AI 需求和客户合同
→ 土地和电力协议
→ 发电、输电和变电站审批
→ 变压器、开关设备和断路器交付
→ 建筑、冷却和备用电源完工
→ GPU、网络和存储器安装
→ 调试
→ 客户工作负载激活
→ 云服务和 AI 收入确认
```

FERC 于 2026 年 6 月对六家区域电网运营商发布的命令证实，大负荷接入已成为全国性政策议题。[^ferc]

但“发电不足”只是其中一种失效模式。一个地区可能有发电厂但没有输电线路；可能有输电线路但没有变压器；可能有设备但未就谁承担费用达成协议。而刚性的 24/7 负荷，比能够跨时间或地点转移训练任务的负荷需要更多基础设施。

## 4. ERCOT 有何不同

### 4-1. 太阳能和电池作出了可量化贡献

NERC 的 2026 年评估列出，ERCOT 拥有 40.3 GW 太阳能和 22.0 GW 电池储能。预期峰值贡献分别为 29.7 GW 和 20.7 GW。

| ERCOT 资源 | 铭牌容量 | 预期峰值贡献 | 贡献率 |
|---|---:|---:|---:|
| 风电 | 40.6 GW | 9.45 GW | 23% |
| 太阳能 | 40.3 GW | 29.68 GW | 74% |
| BESS | 22.0 GW | 20.69 GW | 94% |

得州在 2025 年夏季创下 29.3 GW 太阳能输出纪录和 7.2 GW 电池放电纪录。随着 2025 年新增 8.78 GW BESS、截至 2026 年 3 月再新增 2.68 GW，最高风险时段的能源紧急警报模型概率从 3.1% 降至 0.43%。[^nerc]

电池并非连续数日为整个州供电。它们将午间太阳能转移至傍晚，应对突发失衡，并稳定频率。

### 4-2. 供给只占答案的一半

ERCOT 在 2026 年夏季可用需求响应为 5.1 GW，同比增长 54.9%。NERC 称，更多计算负荷可在紧急情况下削减，使其净内部需求预测减少 3.7 GW。[^nerc]

```text
太阳能满足日间需求
→ 电池衔接傍晚爬坡
→ 燃气、核电和风电支持稳定及夜间供给
→ 大型计算负荷在压力情景下削减
→ 快速市场信号和并网规则吸引资源
```

ERCOT 风险下降反映了预期资源增加 12%、更多 BESS、更多需求响应和灵活大型负荷。这不是单一技术的故事。

### 4-3. 尚存的弱点

- 最高风险时段是晚上 9 点，此时太阳能输出正在消退。
- 得州远西部仍面临输电约束。
- 大型电子负荷同时跳闸可能破坏频率和电压稳定。
- 92 GW 数字是夏季预测，并非实际纪录。
- 以 GW 衡量的电池功率容量，若没有以 GWh 衡量的储能时长数据，几乎无法说明能否度过多日低风或低太阳能事件。

## 5. 太阳能加 BESS 是最快解决方案吗？

对于未来三年的增量电力，是。对于完整的 24/7 供给，不是。

| 选项 | 首次供电速度 | 24/7 稳定性 | 主要约束 | 最佳角色 |
|---|---|---|---|---|
| Solar+BESS | 快 | 中等 | 土地、变压器、时长、夜间 | 快速增量供电和峰值支持 |
| 现场燃气发动机或小型燃气轮机 | 中等 | 高 | 燃气管道、空气许可、燃料成本 | 过渡电力和绕过队列 |
| 燃料电池+BESS | 中等 | 高 | 燃料供应、设备成本、维护 | 模块化表后供电 |
| 既有核电或燃气 PPA | 快至中等 | 高 | 输电和合同结构 | 稳定供给 |
| 新建联合循环燃气 | 慢 | 高 | 燃气轮机交付周期、管道、许可 | 大规模长期供给 |
| 新建输电线路 | 很慢 | 高 | 许可、土地、成本分摊 | 结构性解决方案 |
| SMR 或新建核电 | 很慢 | 高 | 许可、建设成本、进度 | 2030 年代稳定电力 |
| 灵活计算负荷 | 最快 | 非供给来源 | SLA 和软件 | 在相同电网下更快接入 |

S&P Global 对一个 627 MW 数据中心建模后发现，太阳能加储能设计的成本超过联合循环电厂的两倍，同时仍无法保证在多日低太阳能期间持续供电。[^spp-solar-gas] 这并未否定 solar+BESS，而是界定了其作为快速增量和峰值容量、而非独立全年解决方案的角色。

实用架构应分阶段推进：

1. <strong>初始通电：</strong>太阳能、BESS、现场发动机或燃料电池、部分电网服务，以及灵活的批处理工作负载。
2. <strong>稳定阶段：</strong>与既有核电、燃气或水电签订长期 PPA；变电站和输电升级；更长时长储能。
3. <strong>结构性供给：</strong>新建联合循环发电、输电、核电重启、地热、长时储能，以及最终的先进核电。

## 6. 规则和软件与设备同样重要

FERC 在 6 月的命令中要求 PJM、MISO、SPP、CAISO、ISO-NE 和 NYISO 为大负荷电价机制作出说明或进行改革。选项包括共址发电、灵活输电服务、表后发电，以及来自附近发电机的临时服务。[^ferc]

正在形成的新型资产是可削减计算。

| 工作负载 | 电力灵活性 | 原因 |
|---|---:|---|
| 实时推理 | 低 | 延迟和中断成本高。 |
| 企业云服务 | 低至中等 | 必须保障客户 SLA。 |
| 检查点之间的训练 | 中等 | 短暂停顿和重启可能可行。 |
| 批量训练和预处理 | 高 | 工作可跨时间和地区转移。 |
| 加密货币挖矿 | 极高 | 削减相对简单。 |

并非所有 AI 需求都具有灵活性。但如果一个园区的部分负荷可以削减，电网就不必在首次通电前，为完全同时发生的最坏情形峰值建设每一项升级。

## 7. 对 Big Tech 股票的影响

### 7-1. 负面渠道：已签约需求更慢转化为收入

```text
电力交付延误
→ 数据中心激活延误
→ GPU 服务容量仍受限制
→ 积压订单和 RPO 转化更慢
→ 短期云业务增长受限
→ 利用率达到最优前可能已开始折旧
```

如果土地、建筑和设备订金在电力到位前就已支付，自由现金流将面临压力。因此，2028 年 FCF 问题不只是资本开支，而是已通电容量和利用率。

### 7-2. 正面渠道：在线容量的稀缺价值

当供给增长慢于需求时，已经通电的 GPU 容量更有价值：

- 折扣力度可以下降。
- 长期承诺和预付款可以增加。
- 高利用率吸收折旧。
- 拥有已锁定电力和地域多元化的运营商获得份额。

数据中心延误对所有 hyperscaler 并非同等负面。它们会伤害拥有大量未通电计划的公司，同时强化拥有已通电容量公司的定价能力。

### 7-3. 新的 Big Tech 评分卡

| 指标 | 正面信号 | 负面信号 |
|---|---|---|
| 已通电电力 | 明确的 MW/GW 和日期 | 仅披露最终园区规模 |
| 电力来源 | 多地区 PPA、现场电力、电网合同 | 单一公用事业公司和遥远日期 |
| 客户合同 | 长期承诺、预付款、最低使用量 | 无约束力的兴趣 |
| 资本开支分期 | 投资与通电进度一致 | 建筑和芯片等待电力 |
| 灵活性 | 工作负载跨时间和地区转移 | 所有负荷均被视为刚性 24/7 需求 |
| 现金流 | 收入和利用率快于折旧 | 折旧和利息先上升 |

下一次财报电话会应询问：多少 GW 能够上线、何时上线，以及附带多少客户收入？

## 8. 对半导体股票的影响

### 8-1. 短期风险：订购与安装之间存在缺口

hyperscaler 可以在电力尚未就绪前接收 GPU 和 HBM，形成客户库存；也可以延迟交付以匹配通电进度，形成季度出货缺口。

预警信号包括：

- GPU 和服务器的客户库存天数上升
- 预付款下降和交付排期延长
- 更多提及“等待电力”
- 服务器 ODM 出货增长快于在线云容量
- HBM 合同保持不变，但季度交付日期后移

“延后需求”并不自动利好。

### 8-2. 中期机会：更长的周期尾部

如果项目是后移而非消失，需求曲线可能变得更平缓并延长。

```text
2026 年数据中心容量延后
→ GPU 和 HBM 安装移至 2027-2028 年
→ 2026 年出货增长放缓
→ 延后安装与替换和扩张需求重叠
→ 峰值可能更低，但周期持续更久
```

这需要三个条件：

1. 最终 AI 需求没有恶化。
2. hyperscaler 融资能力和信用保持完好。
3. 电力解决方案正在建设，而非仅仅公布。

反复延误加上 AI 变现走弱，会令延后转变为取消。

### 8-3. 每瓦性能变得更有价值

| 半导体层级 | 电力稀缺的影响 |
|---|---|
| GPU 和 AI ASIC | 每瓦性能成为更重要的采购标准。 |
| HBM | 降低数据移动能耗和提高加速器利用率，提升其价值。 |
| 服务器 DRAM | 包括电力和冷却在内的总拥有成本变得更重要。 |
| 企业级 SSD | 低功耗、高吞吐存储减少 GPU 空闲时间。 |
| 网络 | 更快的网络互连通过减少集群空闲时间获得溢价。 |
| 功率半导体和衬底 | 高压配电和转换在系统价值中的占比上升。 |

对 SK hynix 而言，正面渠道是 HBM 和高价值服务器 DRAM 的每瓦性能优势。Samsung Electronics 则兼具潜在的 HBM 复苏，以及低功耗 DRAM 和企业级 SSD 的更广泛产品组合。但若通电延误造成服务器和客户端库存，其更广泛的通用产品敞口也可能提高敏感性。

## 9. 按群组的股票判断

| 群组 | 未来 0-6 个月 | 未来 1-3 年 | 判断 |
|---|---|---|---|
| Hyperscalers | 容量限制增长；在线容量维持定价 | 电力获取成为护城河 | 公司间分化扩大 |
| GPU 和 AI ASIC | 季度出货时点风险 | 每瓦性能和延后需求 | 中期正面，短期波动 |
| HBM 和服务器存储器 | 交付节奏和客户库存重要 | 潜在周期延长 | 有条件正面 |
| 电力设备 | 积压订单和定价保持强劲 | 后续产能扩张可能带来竞争 | 直接受益者，估值重要 |
| BESS | 峰值和表后需求 | 更长时长和软件价值 | 结构性受益者 |
| 燃气轮机和发动机 | 订单强劲，交付缓慢 | 管道和许可约束 | 积压强劲，收入延后 |
| 核电和地热 | 短期贡献有限 | 稳定电力溢价 | 长周期 |

电力设备是最直接、最纯粹的受益者，因为变压器、断路器、开关设备、电缆和电池解决了延误的成因。但长积压订单并不自动意味着股票便宜。制造扩张、投入成本、订金和 2028 年后的竞争仍然重要。

韩国上市公司敞口包括：

- 电网和配电：LS ELECTRIC、HD Hyundai Electric、Hyosung Heavy Industries
- 电缆：Iljin Electric、Gaon Cable
- BESS 和电能质量：LG Energy Solution、Samsung SDI、Vinatech
- 冷却：LG Electronics、GST
- 稳定电力：Doosan Enerbility、SK Gas、GNC Energy

请参阅[7 月 23 日受益者排名](/zh/post/korea-ai-datacenter-beneficiaries-power-cooling-operator-flow-ranking-2026-07-23/)，获取基于价格和资金流的股票筛选。本报告聚焦美国瓶颈的持续时间。

## 10. 月度仪表盘

| 指标 | 正面解读 | 负面解读 |
|---|---|---|
| 数据中心首次供电 MW | 计划转化为在线容量 | 最终规模增长但日期延后 |
| 大型变压器交付周期 | 瓶颈和定价持续 | 因取消而交付周期骤降 |
| ERCOT 和 PJM 大负荷审批 | 电力交付加速 | 研究时间线再次延长 |
| BESS 部署和时长 | 傍晚峰值覆盖改善 | GW 很高但 GWh 不足 |
| 需求响应参与规模 | 更多负荷接入同一电网 | SLA 顾虑降低参与度 |
| Big Tech 利用率和 RPO 转化 | 电力和客户同步到位 | RPO 增长但转化放缓 |
| GPU 和 HBM 客户库存 | 延后需求依然健康 | 芯片在无电力支持下累积 |
| 云增长相对折旧 | 收入快于成本基础增长 | 折旧快于增长 |

## 11. 反方压力测试

建设性情景将在以下情况下失效：

1. 延误反映的是 AI 需求走弱，而非电力时点问题。
2. 云服务积压订单和客户预付款下降。
3. GPU 和 HBM 库存累积，签约量被取消。
4. 变压器和 BESS 制造扩张导致 2028 年价格崩塌。
5. 地方反对同时阻止输电、现场发电和可再生能源。

看空情景将在以下情况下失效：

1. 灵活负荷和共址发电规则迅速标准化。
2. ERCOT 式削减合同扩展至 PJM 和 MISO。
3. 混合太阳能、储能、发动机和燃料电池在两年内为大型园区通电。
4. hyperscaler 在披露稳定电力日期的同时披露长期客户合同。
5. 尽管交付时间表发生变化，HBM 合同和预付款仍保持完好。

## 12. 最终观点

美国数据中心延误并非只是因为该国缺乏能源。连接、变换、削减和分摊电力成本所需的制度与设备，其推进速度慢于 AI 需求。

太阳能加 BESS 是最快的增量回应。ERCOT 以 40.3 GW 太阳能、22.0 GW 电池储能、50.4 GW 合计预期峰值贡献，以及 0.43% 的紧急警报模型概率证明了这一点。但同一证据也凸显了 5.1 GW 需求响应和可削减计算负荷的作用。

股票影响必须按时间区分：

- <strong>Big Tech，短期：</strong>电力交付限制云业务增长，而已通电容量获得稀缺价值。
- <strong>Big Tech，中期：</strong>电力、利用率和客户合同决定 2028 年自由现金流能否恢复。
- <strong>半导体，短期：</strong>交付调整和客户库存带来波动。
- <strong>半导体，中期：</strong>若延后未变成取消，GPU 和 HBM 需求可扩展至 2027-2028 年并延长周期。
- <strong>直接受益者：</strong>变压器、断路器、开关设备、电缆、电池和现场发电解决了延误的物理原因。

决定性的区别在于：项目是否拥有确定的供电日期而非无电力支撑的公告，以及延后需求是否有客户合同支持而非最终消失。

> [事实] 公开来源验证了延误指标、NERC 风险分类、ERCOT 资源、并网队列和设备交付周期。  
> [推断] 周期延长和稀缺定价的论点要求客户合同和最终 AI 需求保持稳固。  
> [受阻] 项目层面的通电日期、表后电力经济性以及确切的 GPU 安装时间表大多仍属私有信息。

相关研究汇集于[独家分析中心](/zh/page/exclusive-analysis-hub/)和[AI HBM 中心](/zh/page/korea-semiconductor-hbm-kospi-hub/)。

[^allianz]: [Allianz Research, Thinking fast, building slow: AI and the energy supply crunch](https://www.allianz.com/content/dam/onemarketing/azcom/Allianz_com/economic-research/publications/specials/en/2026/may/2026-05-12-ai-energy-AZ.pdf), May 12, 2026.
[^nerc]: [NERC, 2026 Summer Reliability Assessment](https://www.nerc.com/globalassets/our-work/assessments/nerc_sra_2026.pdf), May 2026.
[^lbl]: [Lawrence Berkeley National Laboratory, Queued Up: 2026 Edition](https://emp.lbl.gov/queues), July 2026.
[^reuters-transformer]: [Reuters, US power companies scramble to secure equipment as surging data center demand strains supplies](https://www.investing.com/news/stock-market-news/us-power-companies-scramble-to-secure-equipment-as-surging-data-center-demand-strains-supplies-4783319), July 9, 2026.
[^dcwatch]: [Tom's Hardware report citing Data Center Watch](https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-75-data-center-build-outs-worth-usd130-billion-have-been-successfully-blocked-in-the-first-four-months-of-2026-bipartisan-opposition-mounts-nationwide-over-fears-of-soaring-power-and-water-costs), June 13, 2026.
[^gas-turbine]: [S&P Global, Mitsubishi Power gas turbine orders stretch to 2030](https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/070326-interview-mitsubishi-power-gas-turbine-orders-stretch-to-2030-amid-ai-security-demand), July 3, 2026.
[^kera]: [KERA News, ERCOT predicts record summer energy demand](https://www.keranews.org/energy-environment/2026-06-04/ercot-predicts-record-summer-energy-demand), June 4, 2026.
[^ferc]: [FERC, FERC Launches Aggressive Targeted Action to Speed Large Load Integration](https://www.ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration), June 18, 2026.
[^spp-solar-gas]: [S&P Global Market Intelligence, Data center power: Combined-cycle plant outperforms solar plus battery](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/03/data-center-power-combined-cycle-plant-outperforms-solar-plus-battery), March 2026.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
