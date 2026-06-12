---
title: "Flux de rééquilibrage des ETF thématiques coréens : redistribution vers les semicap semi, pression de cap sur les leaders"
date: 2026-06-12T17:40:00+09:00
description: "La première exécution de KR Theme ETF Rebalance Flow v1 a détecté des flux mécaniques potentiels liés aux rééquilibrages et aux plafonds de pondération des ETF thématiques coréens. Le signal le plus fort du 12 juin 2026 se situe dans les équipements et matériaux semi-conducteurs."
categories: ["Korean-Equities", "Market-Flow", "ETF-Flow"]
tags: ["ETF coréens", "rééquilibrage ETF", "semi-conducteurs", "flux passifs"]
series: ["korea-rerating-2026", "korea-market-flow"]
slug: "kr-theme-etf-rebalance-flow-semicap-cap-trim-2026-06-12"
draft: false
---

## TL;DR

- Thesis OS a ajouté **KR Theme ETF Rebalance Flow v1**, un moniteur des flux mécaniques possibles dans les ETF thématiques coréens.
- La première exécution a scanné **31 ETF**, dont **30 valides**, avec **291 lignes de constituants** et **69 candidats**.
- Le modèle a identifié **60 candidats à l'achat par redistribution** et **9 candidats à la réduction de pondération**.
- Le signal le plus fort n'était pas nucléaire/SMR, mais **équipements et matériaux semi-conducteurs**.
- Leeno Industrial, EO Technics, Soulbrain, DB HiTek, Hanmi Semiconductor, ISC et Wonik IPS ressortent en tête.

## 1. Ce Que Mesure Le Moniteur

Le moniteur estime un proxy de redistribution:

```text
Flux ETF = NAV de l'ETF × variation de pondération cible
Flux titre = somme des flux par ETF
Intensité = flux estimé / volume moyen 20 jours
```

Il utilise les données publiques Naver ETF surface (`constituentList`, `totalNav`) et les données locales de prix. Si un titre dépasse un cap supposé, le modèle le ramène au cap et redistribue l'excédent vers les autres constituants.

Ce n'est pas un PCF officiel. Il faut vérifier les PDF/PCF des émetteurs, la méthodologie d'indice, les règles de cap et les volumes de clôture.

| Mesure | Valeur |
|---|---:|
| Date | 2026-06-12 |
| ETF scannés | 31 |
| ETF valides | 30 |
| Lignes de constituants | 291 |
| Candidats | 69 |
| Achats de redistribution | 60 |
| Réductions de cap | 9 |
| Confiance | moyenne-faible |

## 2. Candidats D'Achat Par Redistribution

| Nom | Flux estimé | Flow/ADV20 | Performance jour |
|---|---:|---:|---:|
| Leeno Industrial | 270,4 md KRW | +2,68x | +4,7% |
| EO Technics | 197,8 md KRW | +2,49x | +21,4% |
| Soulbrain | 69,4 md KRW | +2,44x | +24,4% |
| DB HiTek | 264,3 md KRW | +2,02x | +12,3% |
| Hanmi Semiconductor | 721,0 md KRW | +1,81x | +24,1% |
| ISC | 92,0 md KRW | +1,76x | +20,7% |
| Wonik IPS | 211,1 md KRW | +1,63x | +30,0% |

L'intensité par rapport à la liquidité est le point clé. Les semicap peuvent être plus sensibles aux flux que les mégacaps.

## 3. Surveillance Des Réductions De Pondération

| Nom | Flux estimé | Flow/ADV20 | Lecture |
|---|---:|---:|---|
| SK Hynix | -1,76 tn KRW | -0,15x | pression technique, pas une thèse short |
| Samsung Electronics | -49,4 md KRW | -0,00x | impact relatif faible |
| Samsung Electro-Mechanics | -514,9 md KRW | -0,21x | pression technique à surveiller |
| LS ELECTRIC | -47,0 md KRW | -0,15x | éviter de poursuivre sans confirmation |
| Doosan Enerbility | -26,5 md KRW | -0,07x | cas nucléaire à suivre |

## 4. Discipline D'Utilisation

| Étape | Confirmation requise |
|---|---|
| 1 | PDF/PCF officiel de l'ETF |
| 2 | Méthodologie d'indice et règle réelle de cap |
| 3 | Volume de clôture et enchère finale |
| 4 | Force relative T+1/T+3 |
| 5 | Alignement des flux programme, étrangers ou institutionnels |

## Conclusion

La première lecture indique que le signal passif le plus net est **la redistribution vers les semicap semi-conducteurs**. C'est un bon outil de tri, mais pas encore un signal de transaction confirmé.
