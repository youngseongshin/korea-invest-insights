---
title: "Carte des multiples de l'infrastructure IA : pourquoi Samsung Electronics paraît bon marché et Samsung Electro-Mechanics chère"
date: 2026-05-31T09:00:00+09:00
description: "GPU, HBM, CPU, MLCC et FC-BGA appartiennent au même cycle d'infrastructure IA, mais ne méritent pas le même multiple. L'analyse décompose l'écart par pouvoir de prix, contrats de long terme, lock-in client, capex et doute sur les profits de pic."
categories: ["Market-Outlook"]
tags:
  - "infrastructure IA"
  - "multiples"
  - "HBM"
  - "GPU"
  - "MLCC"
  - "FC-BGA"
  - "Samsung Electronics"
  - "Samsung Electro-Mechanics"
  - "SK hynix"
  - "Nvidia"
  - "semi-conducteurs coréens"
slug: ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31
valley_cashtags:
  - 삼성전자
  - 삼성전기
  - SK하이닉스
draft: false
---

> Contexte
> Ce billet relie la thèse [Samsung Electronics et le supercycle mémoire](/fr/post/samsung-electronics-stock-bonus-supercycle-buyback-2026-05-27/) à la thèse [Samsung Electro-Mechanics face à Murata et Ibiden](/fr/post/samsung-electro-mechanics-market-cap-murata-ibiden-premium-2026-05-28/). Même cycle IA, mais multiples différents : c'est la question centrale.

## TL;DR

Le marché ne paie pas simplement "l'exposition à l'IA". Il paie la <strong>durée des profits, le pouvoir de prix, le lock-in client, le risque de capacité et la réduction du doute de pic de cycle</strong>.

Le risque actuel est de valoriser les fournisseurs MLCC / FC-BGA comme des monopoles structurels de type GPU/HBM. Ce sont de vrais goulets d'étranglement, mais tous les goulets ne méritent pas un multiple de plateforme.

La meilleure idée relative reste <strong>Samsung Electronics</strong>. L'entreprise combine rattrapage HBM, prix mémoire et option foundry, tout en affichant dans le snapshot public 2026-05-29/30 environ 7,8x de P/E forward et 4,4x de P/B. Samsung Electro-Mechanics a la bonne histoire, mais le prix anticipe déjà beaucoup. ([Yahoo Finance][1])

## 1. La formule

```text
Prime de multiple
= pouvoir de prix × durée de demande × lock-in client × conversion en FCF

Décote de multiple
= capex d'expansion × risque de surcapacité × doute de profit de pic × concentration client
```

| Couche | Ce qui soutient le multiple | Ce qui le plafonne | Question clé |
|---|---|---|---|
| GPU / plateforme | CUDA, systèmes rack-scale, software, asset-light | ASIC propriétaires, Chine, pouvoir des hyperscalers | le client achète-t-il du temps ou une puce? |
| HBM | HBM4, sold-out, LTA, plus de contenu par accélérateur | cycle mémoire, capex, diversification fournisseurs | profit cyclique ou franchise contractualisée? |
| CPU | serveurs IA, orchestration | substituabilité ARM / CPU internes | goulet principal ou composant auxiliaire? |
| FC-BGA | grands substrats multicouches, qualification | capex, amortissement, souvenir de surcapacité ABF | capex couvert par LTA / prépaiements? |
| MLCC / Si-Cap | intégrité de puissance, haute fiabilité | cycle MLCC générique, concurrence | bloqueur d'expédition ou composant passif? |

## 2. Lecture par couche

NVIDIA reçoit le multiple le plus élevé parce que la société ne vend pas seulement des GPU : elle contrôle GPU, networking, logiciel, architectures de référence et systèmes d'AI factory. Son T1 FY2027 a atteint 81,6 Md$ de revenus, dont 75,2 Md$ en Data Center, avec une guidance T2 de 91,0 Md$. ([NVIDIA Investor Relations][2])

HBM génère des profits très élevés mais reste valorisé avec une décote de mémoire cyclique. Les LTA sont donc décisifs : si prix, volumes et récupération du capex sont sécurisés, HBM peut devenir une franchise mémoire de haute valeur, pas seulement de la DRAM commodity.

CPU est nécessaire mais pas le goulet principal. AMD progresse en Data Center, mais son multiple exige succès simultané d'EPYC et d'Instinct. Intel a besoin de preuves d'exécution.

FC-BGA et MLCC sont des thèses justes. Samsung Electro-Mechanics a cité la demande MLCC serveurs IA et FC-BGA accélérateurs / CPU serveur comme moteurs du T1 2026, et a signé un contrat Si-Cap d'environ 1,5 billion de wons pour 2027-2028. ([Samsung Electro-Mechanics][7], [Samsung Electro-Mechanics][8])

Mais le prix compte. ResearchAndMarkets estime que le marché FC-BGA passe de 2,46 Md$ en 2026 à 3,74 Md$ en 2032, soit 7,1% de CAGR. Cela ne suffit pas à justifier durablement des P/E de 100x. ([Research and Markets][9])

## 3. Samsung Electronics vs Samsung Electro-Mechanics

Samsung Electronics offre une exposition plus large à la hiérarchie mémoire de l'inférence IA : HBM4E, DDR5, SOCAMM2, eSSD / KV-cache et foundry.

Samsung Electro-Mechanics est rare avec MLCC + FC-BGA + Si-Cap. Cela peut la reclasser comme fournisseur d'intégrité de puissance pour package IA. Mais à ce prix, il faut des preuves : nouveaux clients Si-Cap, marges, ASP MLCC IA, utilisation FC-BGA et LTA.

## 4. Vue pratique

| Nom | Vue | Raison |
|---|---|---|
| Samsung Electronics | Under / candidat à l'achat | multiple bas face au rattrapage HBM et à l'option mémoire |
| NVIDIA | Fair à relativement under | croissance et marge soutiennent encore le multiple |
| SK hynix | under fondamental, timing à attendre | HBM pur mais P/B et rally élevés |
| Samsung Electro-Mechanics | over / ne pas poursuivre | bonne thèse, prix exigeant |
| Murata / Ibiden | over | goulet réel, mais valorisation quasi monopolistique |

La grande erreur serait d'attribuer un multiple de plateforme à tout fournisseur simplement parce qu'il touche la chaîne NVIDIA.

[1]: https://finance.yahoo.com/quote/005930.KS/key-statistics/ "Samsung Electronics valuation"
[2]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx "NVIDIA FY2027 Q1 results"
[7]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Q1 2026"
[8]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics silicon capacitor contract"
[9]: https://www.researchandmarkets.com/reports/6128754/fc-bga-market-global-forecast "FC-BGA market forecast"
