---
title: "这个博客是怎么做出来的：开源研究操作系统 Thesis OS 正式公开"
date: 2026-05-30T11:00:00+09:00
description: "Korea Invest Insights 的文章并不是一篇篇手写出来的，而是通过一个名为 Thesis Investment OS 的结构生成的。Alpha 负责收集证据，Lattice 把证据转化为判断，Arki 维护整个系统的健康——这三个角色环环相扣，构成了一个开源的研究操作系统。本文用通俗的语言介绍这一结构，并邀请你访问其 GitHub 仓库。"
categories: ["Tools"]
tags:
  - "Thesis OS"
  - "开源"
  - "研究方法论"
  - "投资研究"
  - "Alpha"
  - "Lattice"
  - "Arki"
  - "Research OS"
  - "GitHub"
slug: thesis-os-open-source-research-operating-system-2026-05-30
draft: false
---

> 🔗 <strong>前往仓库</strong>：<strong>Thesis Investment OS repository</strong> —— 驱动本博客研究的开源系统

今天这篇文章和平时有点不一样。它不讲某只股票，而是讲<strong>本博客的文章究竟是怎么做出来的</strong>。让我把幕后掀开一角给你看看。

![Thesis Investment OS 架构图 —— Alpha、Lattice、Arki 三个角色环环相扣的研究操作系统结构](thesis-os-architecture.png)

## 一篇文章的诞生过程

Korea Invest Insights 的文章，并不是有人对着空白屏幕即兴敲出来的。它们背后运行着一个名为 <strong>Thesis Investment OS</strong> 的小型操作系统。名字听起来很大，但想法很简单。

> 让投资判断<strong>看得见、可检验，并对自己的历史成绩保持诚实。</strong>

它不是自动交易机器人，不是卖信号的服务，也不是"用 AI 帮你选股"的东西。它是一个<strong>框架</strong>，把零散的市场信息汇成一个论点（thesis），并让你日后能回头检验这个论点最终是对还是错。

这一结构分为三个角色。若以人来比喻，可以看成一支团队里的三个人。

---

## 1. Alpha —— 收集证据的人

Alpha 的角色是<strong>收集并核实事实。</strong>

- <strong>定量数据</strong>：价格、成交量、资金流、基本面、披露文件
- <strong>定性数据</strong>：新闻、披露、财报电话纪要、社区信号
- 用筛选器（screener）缩小候选范围，再叠加背景信息，把值得关注的标的浮现出来

Alpha 产出的是证据记录、市场快照、盘中提醒、筛选器候选名单，以及研究包（research packet）。一句话，它是<strong>诚实地把"发生了什么"堆积起来的人</strong>。它还不做判断，只负责收集原料。

---

## 2. Lattice —— 用证据构建判断的人

Lattice 这个名字取自查理·芒格所说的<strong>"思维模型的格栅（latticework of mental models）"</strong>——一颗由众多框架彼此咬合而成的头脑。

它的角色是把 Alpha 收集来的原料，转化为真正的投资决策。

- 登记一个论点，并整理成决策卡（decision card）
- 进行<strong>魔鬼代言人（devil's advocate）</strong>式的审视，刻意站在对立面去推敲
- 把预测记入预测台账（prediction ledger），过些时日再回头检验它是否站得住

你在博客上读到的那种结构——"结论是这样""这是事实，这是推测"——正是出自 Lattice。关键在于<strong>做出判断，但要以一种日后可以打分的形式留存下来。</strong>

---

## 3. Arki —— 维护系统运转的人

Arki 是最不起眼的角色，却也许是最重要的。它负责<strong>让整个系统保持健康运转。</strong>

- 定义承载数据的结构（schema）以及存储的布局（vault layout）
- 管理周期性任务（recurring jobs），并执行健康检查（health check）
- 保留变更记录（migration log），并治理各角色的权限与规则

若把系统比作一栋房子，在 Alpha 和 Lattice 干活的时候，Arki 就是那个确保水电暖气不断供的人。它并不光鲜，但没有 Arki，另外两位也撑不了多久。

---

## 这三个角色的成果 —— 真实示例

光说很抽象，这里给你看两篇最近经由这套系统产出的文章。

- [戴尔一季度财报与韩国 AI 服务器利润率的延伸解读](/zh/post/dell-q1-fy2027-earnings-korea-ai-server-margin-readthrough-2026-05-29/) —— Alpha 收集戴尔的财报数字，Lattice 把它们接入韩国半导体与服务器价值链，从而构建观点。
- [Marvell Q1 FY2027 财报与韩国半导体的延伸解读](/zh/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/) —— 同样的流程：从 Marvell 的定制硅数字出发，引向对韩国的延伸解读。

两篇文章都把"这是事实（Fact）、这是推论（Inference）、这是推测（Speculation）"分开来写。这一习惯正是 Lattice 强制的结构，而支撑这些事实的数据，则是 Alpha 收集来的。

---

## 为什么要公开这一切

做研究做久了，最可怕的是<strong>"想不起自己以前说过什么"</strong>。看起来漂亮的论点有的是；回头核实它们是否真的应验，却既麻烦又难受。所以大多数分析写一次就被遗忘。

Thesis OS 故意把这种"难受"内置进了系统。每个判断都附上证据，每个预测都被记录，所有内容日后都会被打分。不是因为它完美，而是因为它被设计成<strong>当它出错时，你看得见。</strong>

这套系统被设计为在本地运行。你可以用随附的样本数据先跑一遍——无需 API 密钥、无需券商登录、无需付费数据源。许可证为 MIT，需要 Python 3.10 或更高版本。

而这套系统对外发布的渠道，正是这三处：你正在阅读的<strong>博客（Korea Invest Insights）</strong>、<strong>Telegram @korea_invest_insights</strong>，以及 <strong>Substack</strong>。

---

## 欢迎进来看看

这篇文章的目的不是炫耀，而是邀请。如果你曾想过，怎样让投资研究更诚实、更可检验，不妨进来瞧一瞧。

> 你不必读完全部代码。哪怕只是浏览一下 README，也足以让你感受到"哦，原来这些博客文章是这样做出来的"。

👉 <strong>Thesis Investment OS repository</strong>

点个星（star）当然好，纯粹逛逛结构也无妨。我之所以掀开幕后，只有一个理由：<strong>让你亲眼看清，这个博客的判断究竟从何而来、如何生成。</strong>

---

*免责声明：本文仅供研究与信息参考之用，并非个性化投资建议。所介绍的开源系统是一项研究工具；投资决策及其结果由投资者自行承担责任。*
