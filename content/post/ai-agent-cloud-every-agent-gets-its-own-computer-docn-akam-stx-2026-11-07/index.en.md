---
title: "Every AI Agent Needs Its Own Computer. The Four Stocks Behind That Are Down 43-60%"
date: 2026-11-07T21:55:00+09:00
lastmod: 2026-11-07T21:55:00+09:00
categories: ["ai-infrastructure", "market-analysis"]
tags: ["AI Agents", "Agent Cloud", "DigitalOcean", "Akamai", "Seagate", "Micron", "AMD", "Cloudflare", "CPU", "Storage", "AI Infrastructure"]
series: ["Korea Semiconductor Watch"]
slug: "ai-agent-cloud-every-agent-gets-its-own-computer-docn-akam-stx-2026-11-07"
description: "AI agents run on throwaway computers, one per task. That shifts demand toward CPUs, memory and storage. Four stocks tied to it fell 43-60%. We explain what each company does, why there is a chance, and where the price already moved."
image: "cover.en.png"
draft: false
---

On November 5, the Philadelphia Semiconductor Index (SOX) fell 12.25% in one day. By the November 6 close, DigitalOcean was <strong>60.0%</strong> below its 12-month high, Seagate <strong>57.9%</strong>, Akamai <strong>48.4%</strong> and Micron <strong>43.1%</strong>.

Now look at what these companies sell. DigitalOcean says revenue from its AI customers is running at <strong>$376 million</strong> a year, up 288%. Akamai signed a seven-year, $11.6 billion deal with Anthropic. AMD's data center sales rose 97% in the third quarter, and Intel's rose 78%. The demand is showing up in the numbers, and the stocks fell anyway.

The reason is a change in what a cloud computer is. When millions of people use a website, they all share one program. AI agents do not work that way. Each agent job gets a small sealed computer of its own, for a few seconds or a few days. That needs more server chips, more memory and more storage, and it needs them on top of the graphics chips (GPUs) that investors already watch.

<strong>Our call: the new layers of software that agents need (sealed computers, model routers, training arenas) mostly belong to private companies and the big cloud providers. Public-market investors have a chance in two places. One is older cloud platforms that are rebuilding themselves as agent clouds, DigitalOcean and Akamai. The other is storage and memory suppliers, Seagate and Micron. AMD and Cloudflare sell the right product, but their prices already count on it.</strong>

We start with the idea in plain words, then go company by company, then say what would prove us wrong. At the end we ask which side you take.

## An agent cloud, in plain words

Think of a restaurant. The old cloud is one kitchen that feeds thousands of diners from the same stoves. Its goal is to keep every burner busy. An agent cloud is closer to a workshop that hands each contractor a locked workbench. The contractor finishes the job, the bench is wiped and taken away, and the next contractor gets a fresh one.

The locks matter because of what the contractor does. An AI agent writes code a few seconds before it runs it, and no human has read that code. If it misbehaves, it must not touch anyone else's data. So each job runs inside its own sealed virtual computer. Amazon's agent service, for example, gives each session its own isolated processor, memory and file system. A session can last up to eight hours and is shut down after 15 idle minutes ([AWS documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html)).

Making this cheap is an engineering feat. Firecracker, the open-source technology behind Amazon's serverless services, boots a sealed computer in under 125 milliseconds and adds less than 5 MB of memory overhead to each one ([Firecracker paper](https://www.usenix.org/system/files/nsdi20-paper-agache.pdf)).

![From one shared app to one sealed computer per job. In the traditional cloud one program serves millions of people at once, the code is written and reviewed by developers, and the scarce thing is server utilization. In the agent cloud each job gets a sealed computer for seconds to days, the code was written by a model seconds ago, and the scarce things are isolation, memory and start-up time.](/post-assets/ai-agent-cloud-every-agent-gets-its-own-computer-docn-akam-stx-2026-11-07/old-vs-new.en.svg)

The idea comes from Jamin Ball's [Clouded Judgement issue of November 6](https://cloudedjudgement.substack.com/p/clouded-judgement-11626-the-agent), which argues that agent cloud infrastructure will end up dwarfing classic cloud infrastructure. That is his opinion. The issue gives no usage numbers.

The old cloud was built to squeeze more work out of each server. The agent cloud is built to keep jobs apart, which uses more CPU, memory and storage for the same work.

## Why this needs chips, and which ones

Here is how that turns into chip demand.

First, a sealed computer needs processor cores (CPUs) and server memory (DRAM). It does not need a GPU. The GPU is busy somewhere else, running the AI model itself.

Second, when an agent pauses, its memory is written out to fast flash storage (SSD) so the job can resume later. Pausing does not remove the need for processors and memory. It moves part of it to storage. Logs, saved sessions and the traces used to train agents pile up in bulk storage.

Third, more of these computers sit next to every AI chip. [TrendForce](https://insights.trendforce.com/p/agentic-ai-cpu-gpu) wrote in April that today's ratio of server CPUs to AI chips is roughly 1 to 4 up to 1 to 8, and that agentic AI is expected to push it to between 1 to 1 and 1 to 2. We take the end of each range with the fewest CPUs, 1 to 8 and 1 to 2, so the arithmetic is not the most generous reading. For every million AI chips, that is 125,000 CPUs before and 500,000 after. The difference, 375,000 CPUs, is about 188,000 two-socket servers.

![Server CPUs needed per 1 million AI chips. Before, at 1 CPU per 8 AI chips, 125,000. In the agent era, at 1 CPU per 2 AI chips, 500,000. The difference is 375,000 CPU sockets, about 188,000 two-socket servers. Ratios from TrendForce (April 14, 2026): today about 1 to 4 up to 1 to 8, expected 1 to 1 to 1 to 2. We use the ends with the fewest CPUs. Arithmetic ours, assuming 2 CPU sockets per server.](/post-assets/ai-agent-cloud-every-agent-gets-its-own-computer-docn-akam-stx-2026-11-07/cpu-attach.en.svg)

A size check keeps the story honest. If 10 million consumer agents each held an 8 GB computer at the same moment, that would be 80 petabytes of server memory. That is small next to the chip market. The big numbers come from the ratio above and from always-on agents that work for companies around the clock.

That last piece is the largest gap in our analysis. The CPU ratio rides on the number of AI chips installed, so if AI chip spending slows, this demand slows with it. Always-on company agents are the only part that can grow independently, and nobody has measured how big they are.

## Who gets the money

The new layers of software that agents need are mostly outside the stock market.

| Layer | What it does, in plain words | Who captures the value | Listed stocks tied to it |
|---|---|---|---|
| Sealed computers (sandboxes) | Give each job an isolated computer | Amazon, Microsoft and Google's own services; private start-ups E2B, Daytona and Modal | Cloudflare, Akamai, DigitalOcean (their own versions) |
| Saved state | Pause, resume and copy a job's memory and files | Private start-ups and the big clouds' storage | Dropbox (buying Tigris), Cloudflare; flash and disk makers Sandisk, Micron, Seagate, Western Digital |
| Running the AI model | Generate the answers | Big clouds, private inference firms | Nvidia, AMD, CoreWeave, Nebius, Oracle |
| Routers | Pick the best model for each job on cost and quality | Private gateways such as OpenRouter, Cloudflare | Cloudflare (a small revenue pool) |
| Training arenas | Practice grounds where agents learn by running code and tests | The AI labs themselves, private firms | AMD, Intel, Arm (the CPUs); Seagate, Western Digital (logs) |
| Base layer | Servers, storage and network for everything above | Suppliers with pricing power while supply is tight | AMD, Intel, Arm, Micron, Sandisk, Seagate, Western Digital, Arista, Astera Labs |

Private companies are already priced richly. Press reports say Modal raised $750 million at a $15.75 billion valuation this fall (secondary source). Public investors are left with two routes. The first is platform companies that already own servers, customers and networks, and are adding agent products on top. The second is suppliers that sell scarce chips and storage to everyone in the table.

The November 5 sell-off helped the first route get cheaper. Our reading, written up on November 6, is that the drop re-priced how long supplier profits can last and unwound leverage. It did not cut earnings. Agent demand lengthens that duration. Yet the market sold the platform companies together with the suppliers and the borrowers. DigitalOcean fell 7.2% on November 4 and about 16% on November 5.

## A big drop is not the same as cheap

![A big drop is not the same as cheap. Fall from the 12-month high to the November 6 close. Look-first group: DigitalOcean minus 60.0 percent, 4.4 times 2027 sales (our estimate); Seagate minus 57.9 percent, 12.5 times annualized profit guidance; Akamai minus 48.4 percent, 12.6 times 2026 profit guidance; Micron minus 43.1 percent, 4.5 times annualized profit guidance. Fell too, but price or another risk is the issue: Arm minus 60.3 percent, 84 times; Intel minus 60.1 percent, 56 times; AMD minus 30.9 percent, about 42 times (our estimate); Cloudflare minus 25.5 percent, 28 times annualized revenue.](/post-assets/ai-agent-cloud-every-agent-gets-its-own-computer-docn-akam-stx-2026-11-07/drop-vs-value.en.svg)

Arm and Intel fell as much as DigitalOcean, and they are not cheap. A drop tells you what happened to the price. The valuation check tells you what the price now asks of the company. The next section goes through the first four.

## The four we would look at first

This is the order in which we would study them. It is not a recommendation to buy.

### DigitalOcean (DOCN): the plain cloud for small developers

<strong>What it does.</strong> DigitalOcean rents cloud servers by the hour to developers, start-ups and small businesses. Its pitch is simple prices and simple tools, against Amazon's huge menu. It now sells Managed Agents and Agent Droplets, its name for ready-made sealed computers for agents.

<strong>Why there is a chance.</strong> The people building AI agents are mostly start-ups and small teams, the customers DigitalOcean already serves. In its third quarter report, AI customers (those using one or more of its AI offerings) ran at $376 million of annual revenue, up 288%, and the volume of AI tokens handled by its inference service grew roughly tenfold from the previous quarter. The CEO says the company expects 60% or more revenue growth in 2027. The market value is $8.55 billion, about 4.4 times our estimate of 2027 revenue of $1.94 billion (the middle of its 2026 guidance, $1.21 billion, grown by exactly 60%). The stock is 60.0% below its high and fell 41.5% in a month, because it was sold with AI-infrastructure borrowers although it mostly rents ordinary servers.

<strong>What could go wrong.</strong> Its finance-lease obligations, the contracts it uses to pay for equipment over time, rose to $719 million from $99 million at the start of the year for the long-term part alone. With the part due within a year, they are about $924 million against $131 million. That is debt-like. If AI start-up customers leave or cut spending, the equipment stays and the payments continue.

### Akamai (AKAM): the network company that became a cloud

<strong>What it does.</strong> Akamai started by speeding up websites and protecting them from attacks, using servers placed close to users around the world. It then bought the cloud provider Linode in 2022 to rent out servers too. It has now launched Agent Sandbox, a sealed computer for agents, and inference services.

<strong>Why there is a chance.</strong> At $83.09 the stock trades at 12.6 times the profit it guides for 2026 ($6.47 to $6.68 per share). Cloud infrastructure revenue grew 34% to $109 million in the quarter, and the company aims for $1.1 billion to $1.3 billion in 2027. The Anthropic deal, announced September 24, is $11.6 billion over seven years. Akamai expects to spend about $5.5 billion on equipment for it, and Anthropic receives a warrant for up to about 5% of Akamai's shares, which vests in steps as its purchases grow. Akamai's CEO says total revenue is projected to exceed $7 billion in 2028.

<strong>What could go wrong.</strong> One customer carries much of the growth, and the build cost will show up as depreciation. We do not judge the size of the Anthropic deal. Anthropic is the maker of the AI model that helped us write this post, so treat the Akamai view with that in mind and check the contract terms yourself.

### Seagate (STX): the cheapest place to keep what agents write down

<strong>What it does.</strong> Seagate makes hard disk drives, the spinning-disk storage in data centers. Most of the world's data sits on disks because they cost the least per terabyte.

<strong>Why there is a chance.</strong> Agents leave a trail: logs, saved sessions and the traces used to train the next agent. That data has to be kept, and it is not worth paying flash prices for. On its October 27 call it said it shipped a record 198 exabytes of data center drives in the quarter (secondary transcript). It guides fiscal second-quarter earnings of $9.20 per share, plus or minus $0.20. Multiplied by four, that is $36.8, and at $460.99 the stock trades at 12.5 times. It is 57.9% below its high and fell 40.5% in a month.

<strong>What could go wrong.</strong> A low multiple on a peak profit is how cyclical stocks look near the top. If the profit lasts, the price is cheap. If it fades soon, it is not. Pricing gains Seagate has made could reverse if demand cools.

### Micron (MU): the memory every sealed computer needs

<strong>What it does.</strong> Micron makes DRAM, the working memory of servers, and NAND flash, the memory in SSDs.

<strong>Why there is a chance.</strong> Every sealed computer needs working memory, and paused ones are written to flash. At $690.00 and its guidance of $38.15 of earnings per share (plus or minus $1.00) for the November quarter, the stock trades at 4.5 times the annualized figure. Micron said on its June 24 call that its long-term supply agreements are take-or-pay with binding volume commitments, typically five years from 2026 through 2030. Take-or-pay means the customer pays for the agreed volume even if it does not take delivery.

<strong>What could go wrong.</strong> Memory prices swing, and the high-bandwidth memory part of Micron's business rides on AI chip spending. Micron also moves with the same drivers as Samsung Electronics and SK hynix, so it adds little if you already hold Korean memory.

## The price already counts on the story: AMD and Cloudflare

<strong>AMD</strong> designs the CPUs inside servers (EPYC) and AI chips. Third-quarter data center revenue was $8.546 billion, up 97%. At $449.04 and our estimate of $10.6 in annualized earnings, the stock trades near 42 times. For the stock to rise 50% at a 30-times multiple, earnings per share would need to reach $22.5, 2.1 times our estimate. The agent CPU story can be true and still be mostly in the price.

<strong>Cloudflare</strong> has the best product fit of any listed name. It sells sealed computers, storage, AI model access, a model gateway and a global network. But its enterprise value is about $95 billion by our calculation, or 28 times its fourth-quarter revenue guidance annualized (the guidance range is $845 million to $846 million). It has fallen the least, 25.5%, and the price carries the product lead.

## Real demand, but another risk decides the outcome

<strong>Intel</strong> grew its data center and AI segment 78% to $7.3 billion. Its CEO says the priority is to unlock more supply for "extraordinary demand" for its Xeon server chips, and its CFO said on the October 29 call that supply stays tight through at least the first half of 2027 (secondary transcript). The result depends on whether Intel can make enough chips, not on demand. At $56.28 the stock trades at 56 times its annualized profit guidance.

<strong>Arm</strong> licenses CPU designs. It trades at 84 times annualized profit guidance (secondary source). Press reports say SoftBank has a $25 billion margin loan backed by Arm shares. SoftBank's May filings showed about 769 million Arm shares, which the November 6 close values at about $134 billion, so the loan is about 19% of that value (the share count is a May figure). That risk has nothing to do with agent demand, and we pass.

<strong>CoreWeave, Nebius and Oracle</strong> rent AI chips and depend on a small number of AI labs and on financing. Our October 26 view on them has not changed. CoreWeave reports on November 10 and Nebius on November 12.

## What would prove us wrong

| If this happens | Then |
|---|---|
| The big cloud providers bundle agent computers into their standard plans | DigitalOcean and Akamai lose their edge. Only the chip and storage suppliers keep their chance. |
| DigitalOcean's AI-customer revenue grows less than 10% from the previous quarter in its February report | We drop it from the first group. |
| Akamai lowers its $1.1 billion to $1.3 billion 2027 cloud infrastructure outlook | We drop it from the first group. |
| Lead times for server CPUs return to 20 weeks or less | The CPU path weakens. |

The first row is the test that matters most. If agent jobs stay on independent platforms and customers keep paying, the platform companies earn the profit. If the big clouds absorb them, the chance moves to the suppliers.

## What to check next

| When | What | Why it matters |
|---|---|---|
| November 10 | CoreWeave third-quarter results | Cuts or financing delays would harden our view on AI-chip renters, and we keep them apart from the platform companies |
| November 12 | Nebius third-quarter results. Check how DigitalOcean and Akamai trade the next day | Shows whether the market still sells the platform companies together with the borrowers |
| Late November to early December | Everpure (formerly Pure Storage) and NetApp earnings | Any wording on demand for saved agent state |
| Mid-December | Micron fiscal first-quarter results | Number of long-term agreements and server DRAM wording |
| Late January to early February | Intel and AMD fourth-quarter results | 2027 server CPU guidance and lead times |
| February 2027 | DigitalOcean and Akamai fourth-quarter results | The two tests in the table above |

## What this means for Korean investors

Micron and the two Korean memory makers share the same drivers, so Micron is a read-through for them, not a separate bet. The agent path adds a source of ordinary server DRAM demand that does not depend on high-bandwidth memory. It also makes the 2028 oversupply risk we have written about a little smaller. We do not treat it as a reason to change that view.

## Data notes

- Prices are US regular-session closes on November 6, 2026. "Annualized" means the latest company quarterly guidance multiplied by four. We used no analyst consensus, because we could not find a dated source.
- The AMD earnings figure is our estimate: its fourth-quarter revenue guidance times the third-quarter profit margin, divided by shares outstanding.
- DigitalOcean's value is market value, because we could not confirm its convertible debt. Its 2027 revenue is our assumption.
- Seagate's and Micron's guidance comes from their 8-K press releases. Seagate's exabyte figure and Intel's remark that supply is tight come from secondary call transcripts, and Arm's results from a secondary summary. The Modal figure and the SoftBank loan come from press reports.
- We did not read the question-and-answer part of AMD's third-quarter call.
- A single AI vendor reviewed this analysis. No second vendor checked it.

<strong>Where does the money end up? Reply with A, B or C, and one data point that backs your pick.</strong>

<strong>A. In agent clouds: DigitalOcean and Akamai keep the customers.</strong>

<strong>B. In storage and memory: Seagate and Micron sell to everyone.</strong>

<strong>C. In neither: the big cloud providers bundle it and the chance disappears.</strong>

This is for research and information only, not investment advice. Estimates and scenarios are analytical assumptions, not trading instructions or individual portfolio decisions. Figures are dated data, and some reported figures are secondary compilations. We used Anthropic's Claude for research and editing. Anthropic appears in this post as Akamai's largest contract counterparty. We report the contract as announced and do not weigh its size.
