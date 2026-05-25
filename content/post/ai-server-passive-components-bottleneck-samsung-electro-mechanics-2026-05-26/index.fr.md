---
title: "Le goulot d’étranglement des composants passifs dans les serveurs IA"
date: 2026-05-26
description: "Le goulot d’étranglement des serveurs IA vient aussi des composants passifs: MLCC, condensateurs silicium, inductances et filtres capables de stabiliser l’alimentation des GPU/HBM. Lecture pour Samsung Electro-Mechanics."
categories: ["Stock-Analysis"]
tags: ["Samsung Electro-Mechanics", "009150", "AI Server", "MLCC", "Silicon Capacitor", "FC-BGA", "Power Integrity", "HBM", "GPU"]
slug: ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26
valley_body_mode: teaser
valley_cashtags: ["삼성전기"]
valley_cashtag_exclude: ["삼성전자", "SK하이닉스"]
---

> Suite de la série Samsung Electro-Mechanics. Voir aussi [SEMCO à 100 000 milliards de KRW](/fr/post/samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26/), [le contrat de condensateurs silicium](/fr/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) et [MLCC vs condensateurs silicium](/fr/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/).

## TL;DR

- Le problème n’est pas seulement le manque de GPU. C’est aussi la montée en gamme des petites pièces qui stabilisent l’énergie consommée par les GPU.
- Un rack NVIDIA DGX GB200 consomme environ **120kW**; Lenovo cite **135kW TDP** et jusqu’à **155kW de pic** pour GB300 NVL72. ([NVIDIA][1], [Lenovo][2])
- Les MLCC, condensateurs silicium et inductances sont les amortisseurs électriques du serveur IA.
- L’opportunité concerne les composants haute capacité, faible ESR/ESL, faible bruit et très bas profil, pas les MLCC génériques.
- Samsung Electro-Mechanics est intéressant car il relie **MLCC + FC-BGA + condensateurs silicium**.

## Explication simple

Un serveur IA ressemble à un moteur de course. Le GPU est le moteur, HBM le réservoir rapide, le substrat la route, et les MLCC/condensateurs silicium stabilisent la pression électrique pour éviter les à-coups.

TDK décrit la chaîne d’alimentation d’un data center comme **UPS → PSU → IBC → VRM → tension CPU/GPU**, avec efficacité, faible ripple, résistance thermique et fiabilité à chaque étape. ([TDK][3])

Samsung Electro-Mechanics explique que les GPU/CPU fonctionnent sous 1V et que le courant peut varier immédiatement de dizaines à centaines d’ampères. Les MLCC de forte capacité proches du GPU servent donc de buffers de courant. ([Samsung Electro-Mechanics][4])

## MLCC vs condensateur silicium

| Composant | Emplacement | Rôle |
|---|---|---|
| MLCC | Carte et zones proches des puces | Stabilisation large de l’alimentation |
| Condensateur silicium | Dans ou juste à côté du package GPU/HBM | Suppression ultraproche des transitoires |

Samsung Electro-Mechanics a annoncé un contrat d’environ **1 500 milliards de KRW** pour des condensateurs silicium sur **2027-2028**. Ces composants améliorent la stabilité d’alimentation dans les packages de semi-conducteurs haute performance pour serveurs IA. ([Samsung Electro-Mechanics][8])

## Lecture investissement

La thèse n’est pas “tous les MLCC montent”. La thèse est:

```text
Puissance par rack en hausse
  → transitoires plus violents
  → besoin de power integrity près des GPU/HBM
  → MLCC haut de gamme, FC-BGA et condensateurs silicium gagnent en valeur
```

À surveiller: ASP des MLCC IA, revenus des condensateurs silicium à partir de 2027, nouveaux clients, croissance FC-BGA serveur/réseau et marge opérationnelle du groupe.

[1]: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[2]: https://lenovopress.lenovo.com/lp2357-lenovo-nvidia-gb300-nvl72-rack-scale-ai
[3]: https://product.tdk.com/en/techlibrary/applicationnote/mlcc-solution-for-data-center-psu.html
[4]: https://product.samsungsem.com/product-news/view.do?idx=3622&language=en
[5]: https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/
[6]: https://www.thelec.net/news/articleView.html?idxno=5588
[7]: https://product.samsungsem.com/product-news/view.do?idx=3742&language=en
[8]: https://m.samsungsem.com/kr/newsroom/news/view.do?id=10309
