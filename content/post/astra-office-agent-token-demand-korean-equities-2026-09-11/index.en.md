---
title: "Office Work Could Drive the Next Token Wave: Translating Astra's Gains into Korean Equity Earnings"
date: 2026-09-11T12:00:00+09:00
categories: ["Korean-Equities", "AI-Infrastructure", "Semiconductors"]
tags: ["Astra", "AI Agents", "Computer Use", "Inference", "HBM", "Enterprise SSD", "Samsung Electronics", "SK hynix", "LS ELECTRIC", "Samsung SDS", "005930", "000660", "010120", "018260"]
slug: "astra-office-agent-token-demand-korean-equities-2026-09-11"
description: "Computer use and long-horizon execution could expand delegated office work. A conditional investment framework with 1.5x, 15x and 70x token scenarios, task economics, Korean equity exposures and falsification tests."
draft: false
---

GPT-6 Astra, introduced on September 3, and the financial-work and data-analysis products announced on September 10 suggest a change in the next competitive question for AI. It is moving from the quality of an answer toward how reliably a system can stay with a delegated assignment until it is finished. OpenAI's financial product connects data, sources and company document templates; its data product connects enterprise information and permissions.[^astra][^finance][^data]

This could extend intensive usage associated with developers into office work more broadly. A launch, however, is not evidence of a token-demand explosion. Multiplying the office workforce by a developer's token consumption is not a defensible market forecast.

<strong>The thesis is conditional: better computer use and long-horizon execution can reduce human intervention, increasing the number of tasks people actually delegate. Korean equity investors must then identify which companies convert that demand into memory shipments and pricing, electrical-equipment orders, or recurring software profit.</strong>

## Coding offered an environment for execution and verification

Software work provides code repositories to read, tools to execute and tests against which to check results. A system can modify a program, examine what failed and try again. Not every software outcome is easy to verify. The narrower inference is that connecting execution with evaluation was often easier to organize in development than in fragmented office workflows.

An April 2026 study of coding agents found substantial variation in token usage across models and execution paths, including repeated runs on the same task. Spending more did not consistently improve accuracy. This is another reason not to extrapolate developers' usage mechanically to office workers.[^coding]

Office work faces different frictions. A promise in an email, a customer record, an Excel calculation and an internal policy may reside in separate systems. A correct answer does not compensate for an incorrectly updated record. Permissions and approvals must be connected before an answer becomes completed work.

“Office work after coding” therefore does not mean one market opens only after the other finishes. The markets already overlap. The claim is that the intensity of repeat usage in non-developer roles could become the next source of growth.

## Computer use expands reach; long-horizon capability changes delegation economics

Computer use means reading screens, clicking controls and entering information. Long-horizon capability means preserving objectives and evidence across steps, recovering from failures and checking the result. The former broadens accessible workflows; the latter reduces the need for a person to supervise continuously.

The two can reinforce each other. Reliable clicking is insufficient if the agent loses the objective at step ten. Extended reasoning is insufficient if a person must transfer every result into the operating system of the business. This is an economic interpretation, not a verified mathematical property of the model architecture.

Published evaluations should be separated from evidence of production adoption.

| Published measure | Astra | GPT-5.6 Sol | Appropriate interpretation |
|---|---:|---:|---|
| AutomationBench | 41.4% | 18.1% | Improvement on an automation evaluation, not the share of all office work automated |
| OSWorld 2.0 partial score | 72.6% | 65.7% | Partial credit on an offline subset, not fully autonomous completion probability |
| OSWorld latency simulation | 40 minutes | 75 minutes | Time under particular evaluation conditions, not measured labor savings in companies |

Source: OpenAI. OSWorld uses the v2026.08.08 offline subset. Evaluation settings and tool environments can differ from production; improvements in the execution environment also matter.[^astra]

Small improvements in step reliability can produce larger changes in the feasibility of delegation. In an illustrative workflow requiring all 50 independent steps to succeed, 98% reliability per step yields 0.98 to the power of 50, or 36.4%. At 99.5%, the corresponding figure is 77.8%. Real failures are correlated, and checkpoints, retries and recovery change the result. These numbers illustrate compounding; they are not estimates of Astra's real-world success rate.

Nor should a company implement every task through screen clicks. A stable application programming interface, or API, should generally be preferred when available, with computer use bridging unsupported gaps. The opportunity is to connect a workflow without replacing every legacy system.

## Capability is being packaged with data access and operating infrastructure

ChatGPT Financial Services, announced September 10, attempts to connect financial data and document work with business templates and controls. The data-analysis offering connects approved data with business context. Both demonstrate why a capable model alone is insufficient: access and validation must accompany it.[^finance][^data]

The Agents API public beta offers infrastructure for context management, tool execution and coordination between agents. Reducing the need for every enterprise to build durable execution infrastructure could lower the cost of turning model improvements into paid workflows. The launch and described features are observable; aggregate customer spending and deployment returns remain separate questions.[^agents]

The likely initial opportunity is not the unsupervised replacement of every office role. Bounded, inspectable activities such as document comparisons, sales preparation, recurring reports and expense reconciliation are more plausible candidates for habitual delegation. Payments, binding contracts and employment decisions should retain appropriate human authorization because the cost of an error is much higher.

## A short instruction can initiate a long chain of computation

“Compare three suppliers and prepare the next meeting pack” is a short request. Carrying it out may require finding emails and quotations, normalizing commercial terms, building a table, verifying figures and sources, and formatting the result. Missing information can trigger another pass through part of the process.

The final answer need not be long for the model to be called many times. Retrieved material, tool responses, intermediate checks and revisions consume tokens. Tokens are units of model input and output, not counts of user questions or sentences.

Anthropic reported in June 2025 that, in its own research-system data, agents typically used around four times the tokens of chat interactions and multi-agent systems around fifteen times. This was a comparison within a particular company's systems, not a universal multiplier for business work. It nevertheless provides evidence for the mechanism through which conversation can become substantially more intensive execution.[^anthropic]

The durable opportunity is not inefficiently spending longer on the same task. It is undertaking work previously omitted because preparation was too costly: more customer-specific proposals, more frequent inventory reconciliations or broader competitor research. Retry loops that merely inflate consumption do not establish sustainable willingness to pay.

## Delegation frequency matters more than a headline workforce number

A useful decomposition is:

> Monthly tokens = eligible workers × active-use share × delegated tasks per active user per day × working days × cumulative tokens per task.

Cumulative tokens per task include all input and output across model calls, retries and verification. Calls made by additional agents belong in this total. Multiplying again by the number of agents or a retry factor would double-count the workload.

The following sensitivity analysis keeps the organization at 1,000 employees and the month at 22 working days. These are assumptions, not observations from a customer or forecasts for 2027.

| Alternative operating state | Active-use share | Daily activity | Cumulative tokens per interaction/task | Monthly total | Relative to chat baseline |
|---|---:|---:|---:|---:|---:|
| Chat baseline | 20% | 10 questions | 2,000 | 88 million | 1.0x |
| Limited delegation | 30% | 1 task | 20,000 | 132 million | 1.5x |
| Routine delegation | 50% | 3 tasks | 40,000 | 1.32 billion | 15.0x |
| Broad delegation | 70% | 5 tasks | 80,000 | 6.16 billion | 70.0x |

The baseline calculation is 1,000 × 20% × 10 × 22 × 2,000 = 88,000,000 tokens. Routine delegation is 1,000 × 50% × 3 × 22 × 40,000 = 1,320,000,000. The rows are alternative operating states, not increments to add to the baseline. A chat interaction and a completed assignment also do not represent identical output.

The 15x result does not require fifteen times as many users. It combines 2.5 times as many active users with six times as many daily tokens per active user, rising from 20,000 to 120,000. Conversely, adoption that stops at one daily summary would generate a much smaller increase.

A larger non-developer population alone cannot establish when office demand overtakes coding demand. Adoption, delegation frequency and tokens per task must be sufficient. Classification also needs care: code created by a business user and documentation produced by a developer should not be counted twice.

## A $0.56 model-cost example illustrates the economic threshold

Astra Standard API pricing is $10 per million input tokens and $50 per million output tokens. Consider an uncached task using 36,000 input tokens and 4,000 output tokens.[^astra]

> Model cost = 36,000 / 1,000,000 × $10 + 4,000 / 1,000,000 × $50 = $0.56.

The 4,000 output tokens are the billable total across all calls, not the length of the final report. Where reasoning tokens are billed as output, they must be included. Caching, cheaper-model routing and separate tool fees change the actual bill.

The routine-delegation scenario produces 500 active users × 3 tasks × 22 days = 33,000 monthly tasks. At this assumed cost, the model bill would be $18,480 a month, or $36.96 per active user. Browser execution, data licensing, integration, security, training and incident response are excluded.

The more important equation is:

> Net value of delegation = realized labor savings or additional commercial value − model and tool costs − human review and rework − error losses − allocated operating and integration costs.

Suppose a low-risk task with equivalent output takes a person 30 minutes and their time is worth $50 an hour. The original cost is $25. If AI requires five minutes of review, and the failed 20% of assignments must be redone from scratch, expected additional rework is six minutes. Human cost is about $9.17; adding $0.56 in model cost produces $9.73, leaving approximately $15.27 per task for other costs and error losses. The 80% success assumption is illustrative and is not derived from a benchmark score.

If review takes 25 minutes instead, expected cost rises to $26.39. Cheap inference does not rescue the workflow. Saved time is also not automatically a cash reduction in payroll: it must translate into redeployment, higher throughput or avoided additional hiring.

The decisive long-horizon metric is therefore not how long an agent can keep running. It is how much human intervention remains per completed assignment.

## Tokens, revenue, compute and memory are different quantities

The easiest analytical mistake is to convert 15x token growth into 15x semiconductor demand. Several transformations intervene.

| Measure | What it captures | Why it diverges from token growth |
|---|---|---|
| Logical tokens | Input and output across all calls | Reused input can still appear in the total |
| Actual bill | Spending at input, cache and output rates | Discounts, subscriptions and cheaper models change realized pricing |
| Physical computation | The calculations actually performed | Model architecture, size, reuse and efficiency differ |
| Memory and storage | Capacity and bandwidth for models, working state and data | Concurrency, context length, retention and storage tier matter |

Holding the workload mix fixed for illustration, 15x more logical tokens with an 80% reduction in computation per token implies 3x compute demand. With a 95% reduction, it implies 0.75x. The calculations are 15 × 0.20 and 15 × 0.05. These are sensitivities, not forecasts of engineering progress.

Lower cost can induce more usage, but it does not automatically increase total spending. Other things equal, quantity must rise sufficiently to offset the lower unit price. New uses unlocked by affordability must be assessed alongside reductions in computation needed for existing work.

Concurrency deserves separate treatment. The same daily volume can require more capacity if requests cluster at the start of the working day. Conversely, batching delay-tolerant overnight jobs can improve utilization and postpone new construction. Multiplying agent count by 24 hours does not create demand by itself.

## The memory thesis spans tiers, not HBM alone

AI systems retain both model weights and intermediate results from earlier context. Reusable intermediate attention state is commonly called the KV cache. Long-running work and concurrent users can increase the importance of where this state is stored and how quickly it can be retrieved.

Not all of it needs to remain continuously in expensive high-bandwidth memory, or HBM. NVIDIA's March 2026 STX and CMX announcements describe an additional context-storage layer. The objective includes expanding accessible context while improving utilization of existing GPUs. Vendor performance figures are configuration-dependent claims, not measured efficiency gains across the entire industry.[^nvidia]

HyMCache, first submitted in July and revised in August under the title A CXL Memory Rack for Multi-Turn LLM Serving, explores combining DRAM and SSD capacity for reusable state. One comparison traded some performance for substantially less DRAM. This is research rather than evidence of large-scale commercial adoption, but it is a counterexample to one-for-one extrapolation from tokens to a particular memory product.[^cache]

The relevant Korean investment hypothesis is not that long-running agents either eliminate HBM or guarantee an explosion in it. It is that fast HBM, server DRAM and high-capacity enterprise SSDs divide the workload, and suppliers may capture value across those tiers. Tokens and stored documents are not interchangeable either: rereading the same file increases logical token volume without necessarily increasing the amount of source data stored.

## Four distinct earnings mechanisms in Korean listed equities

This is an exposure map and research sequence, not a valuation-adjusted buy ranking.

| Company | Exposure to office-agent demand | Evidence of conversion to profit | What weakens the thesis |
|---|---|---|---|
| SK hynix (000660) | HBM, server DRAM and enterprise SSDs | Product shipments, average selling prices, premium mix and cash flow after investment | Customer efficiency offsets volume growth, or supply expansion lowers prices |
| Samsung Electronics (005930) | Broad HBM, server DRAM and enterprise SSD exposure | Customer production ramps, yields, mix and memory earnings versus other divisions | Technical progress fails to become profitable volume, or losses elsewhere deepen |
| LS ELECTRIC (010120) | Data-center power distribution and electrical equipment | Signed orders, delivery schedules, backlog conversion, project margins and cash collection | Higher utilization replaces new construction, or projects are delayed or cancelled |
| Samsung SDS (018260) | Enterprise data integration, agent operation and controls, workflow platforms | Paid repeat usage, renewals, earnings after model costs and external customers | Usage grows but resale costs and integration labor absorb the revenue |

### SK hynix: look beyond HBM without ignoring the cycle

SK hynix's August 26 product presentation included HBM, server DRAM and enterprise SSDs. The portfolio provides multiple ways to address a more differentiated memory hierarchy. A displayed product is not evidence that every offering contributes equal revenue on the same schedule.[^hynix]

Investors should track product-level volumes and prices rather than aggregate revenue labelled AI. Higher HBM supply does not fully describe the outcome if server DRAM or NAND pricing weakens. Operating cash flow should also be assessed after capital expenditure and working-capital requirements.

SK hynix is a direct research candidate for this thesis, but direct exposure is not the same as undervaluation. Attractive industry conditions can produce poor returns when expectations already reflect the supply advantage.

### Samsung Electronics: broad exposure, with offsetting business effects

In its July 30 second-quarter results, Samsung connected its second-half outlook for agentic AI with server DRAM, enterprise SSD and HBM demand. This establishes that a supplier is advancing a similar demand hypothesis. It remains management's outlook rather than independent proof of future supply-demand conditions.[^samsung]

The breadth of Samsung's memory business offers several channels of exposure, but shareholder earnings depend on profitable production after customer qualification, yields and product mix. Other semiconductor and consumer businesses also influence consolidated results.

Astra's launch should therefore not simply be added to an earnings model. Investors must identify demand beyond the AI spending already assumed, and establish whether it changes volume, pricing or profitability. A new narrative describing an existing order is not incremental earnings.

### LS ELECTRIC: invest in construction and orders, not a token royalty

On August 24, LS ELECTRIC announced an expanded North American AI data-center power-equipment contract with a total value of approximately KRW 230.9 billion. That is the amended total, not an entirely additional order to add to the earlier contract. It supports the business connection to data centers, but predates Astra's announcement and cannot be attributed to Astra.[^ls]

If office inference merely raises utilization of existing infrastructure, new electrical-equipment orders may not increase immediately. Persistent demand must lead to financed construction with access to electricity. High financing costs and construction delays can coexist with a favorable long-term demand outlook.

The checks are new orders, conversion of backlog into revenue, project profit and cash collection. Treating the company as earning a royalty every time an AI token is processed ignores both the time lag and execution risk.

### Samsung SDS: operating responsibility matters more than model resale

Samsung SDS describes FabriX as a platform connecting multiple models with enterprise systems and supporting agent creation, operation and governance. Brity Copilot connects AI to collaboration work such as email and meetings. Data access, permissions and operational responsibility provide plausible exposure to office adoption.[^sds][^sdsagent]

Frontier-model vendors, however, are also expanding their own enterprise products and data connections. A chat interface or resold model access may face pricing pressure. Defensibility is more likely where a provider manages legacy exceptions, permissions, audit records and incident response while earning recurring renewals.[^finance][^agents]

Higher paid usage does not ensure higher shareholder profit when model costs and integration labor rise faster. Investors should ask for repeat external-customer contracts, retention after implementation and margins after inference costs. The product material examined here does not establish a standalone AI-business profit margin.

## A correct industry thesis can still lose money in equities

A simple decomposition is:

> Share-price factor = earnings-per-share factor × valuation-multiple factor.

If earnings per share rise 30% but the price/earnings ratio falls from 20x to 15x, the share price becomes 1.30 × 15 / 20 = 0.975 of its previous value, a 2.5% decline. These are illustrative numbers, not current valuations of any named company. The comparison assumes a consistent definition and horizon for earnings.

Peak quarterly memory earnings should not be multiplied by four and treated as permanent. Evaluation requires normalized pricing, supply additions, depreciation, investment and cash flow. Equipment contract value is not immediate profit, and software revenue must be considered after resale costs.

This article is not a stock-by-stock valuation report with comprehensively verified same-day prices and consensus forecasts. It does not invent target prices or entry levels. A purchase decision requires reverse-engineering the growth already embedded in enterprise value and checking whether new orders and repeat usage exceed it.

Memory suppliers merit early research because investors need not identify a single winning office application to gain exposure to adoption across models. But diversification across model vendors is not diversification across the memory cycle. Owning both major Korean suppliers still leaves common exposure to AI capital expenditure and memory prices.

## From Q4 2026, watch repeat usage and intervention rather than launches

Q4 2026 and Q1 2027 provide a useful observation window. This is a research timetable, not a promised adoption schedule.

| What to observe | Evidence strengthening the thesis | Evidence requiring a downgrade |
|---|---|---|
| Paid non-developer usage | Persistent growth in repeat assignments and paid usage within the same adoption cohort | More accounts, but declining activity after trials |
| Task economics | Falling review and rework time per completed assignment | Verification takes roughly as long as doing the original work |
| Physical infrastructure | Compute or context-storage demand rises after caching and model routing | Logical token totals rise while physical resource use stagnates |
| Korean memory suppliers | Unexpected incremental orders change product volumes, prices and earnings | Old orders are relabelled; inventories rise and prices decline |
| Electrical equipment and enterprise software | Orders turn into cash; renewals and margins improve | Construction delays, low-margin resale and one-off implementation dominate |

If repeat non-developer use and unit economics remain unproven over two quarters, the timing of the next demand wave should be pushed back. If adoption grows but efficiency offsets hardware requirements, the software-adoption thesis can survive while the semiconductor thesis becomes less powerful. Security incidents that restrict permissions, or continuing dependence on human rescue and approval, are additional falsification signals.

Astra could expand the market for completed assignments more than the market for longer answers. For Korean equities, the buying case emerges when that possibility creates recurring spending and cash flow beyond expectations already embedded in the share price.

---

Information checked as of September 11, 2026. Product and corporate disclosures are issuer statements, distinguished from independent production validation. Token, cost and share-price sensitivities are the author's assumed examples. This is not personalized investment advice.

### Sources

[^astra]: OpenAI, [GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra/), September 2026. Evaluation conditions and Standard API prices.
[^finance]: OpenAI, [Introducing ChatGPT Financial Services](https://openai.com/index/introducing-chatgpt-financial-services/), September 10, 2026.
[^data]: OpenAI, [Put data to work](https://openai.com/index/put-data-to-work/), September 10, 2026.
[^agents]: OpenAI, [Introducing the Agents API](https://openai.com/index/introducing-the-agents-api/), September 10, 2026.
[^coding]: Bai et al., [How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks](https://arxiv.org/abs/2604.22750v2), first submitted April 24 and revised April 29, 2026. Abstract-level evidence, not generalized to all office work.
[^anthropic]: Anthropic, [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), June 13, 2025.
[^nvidia]: NVIDIA, [NVIDIA Launches BlueField-4 STX Storage Architecture With Broad Industry Adoption](https://nvidianews.nvidia.com/news/nvidia-launches-bluefield-4-stx-storage-architecture-with-broad-industry-adoption), March 16, 2026.
[^cache]: Jang et al., [A CXL Memory Rack for Multi-Turn LLM Serving](https://arxiv.org/abs/2607.18141v3), first submitted July 20; v3 August 5, 2026. Experimental results are not commercial adoption evidence.
[^hynix]: SK hynix, [Memory Solutions at DTF 2026](https://news.skhynix.com/en/dtf-2026/), August 26, 2026.
[^samsung]: Samsung Electronics, [Second Quarter 2026 Results](https://news.samsung.com/global/samsung-electronics-announces-second-quarter-2026-results), July 30, 2026.
[^ls]: LS ELECTRIC, [North American AI data-center power-equipment contract announcement](https://www.ls-electric.com/ko/pr/news/view/401457?b_date=&e_date=&k_type=both&k_word=&page=1&rowsPerPage=10&visiblePage=10), August 24, 2026. Amended contract total, not wholly incremental order value.
[^sds]: Samsung SDS, [FabriX](https://www.samsungsds.com/kr/ai-fabrix/fabrix.html), accessed September 11, 2026.
[^sdsagent]: Samsung SDS, [Samsung SDS AI Agent](https://www.samsungsds.com/kr/ai-agent/ai-agent.html), accessed September 11, 2026.
