---
title: "KOSPI : écart 60 jours à +28,6% — pas un signal de sommet, mais de réduction partielle du risque"
date: 2026-06-21T02:35:00+09:00
description: "Reproduction d’un cadre de surchauffe du KOSPI montrant pourquoi un écart de +28,6% au-dessus de la moyenne 60 jours doit être lu comme un signal de rebalancement partiel plutôt qu’un appel de sommet."
categories: ["Exclusive Analysis", "Market-Outlook", "Risk-Management"]
tags: ["KOSPI", "disparity", "market breadth", "risk management", "RSI", "ATR", "Samsung Electronics", "SK Hynix", "narrow market"]
series: ["exclusive-analysis", "korea-market-flow", "risk-management"]
slug: "kospi-disparity60-overheat-framework-partial-trim-2026-06-21"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte
> Cette note prolonge les analyses sur [la difficulté de battre le KOSPI pur](/fr/post/kospi-benchmark-hard-to-beat-narrow-market-monte-carlo-2026-06-20/), [le marché guidé par les flux ETF](/fr/post/korea-etf-flow-led-market-volatility-strategy-2026-06-13/) et [la liquidité abondante avec une breadth faible](/fr/post/korea-market-liquidity-foreign-reallocation-adr-narrow-leadership-2026-06-03/).

## TL;DR

- Au 19 juin 2026, le KOSPI clôture à **9 052**, sa moyenne mobile 60 jours est **7 039**, et l’écart 60 jours atteint **+28,6%**.
- C’est une surchauffe claire, mais pas une preuve de sommet. Sur 355 séances depuis janvier 2025, les signaux de surchauffe 20/60/120 jours ont été suivis de rendements moyens positifs à 5 et 20 jours.
- Le signal augmente toutefois la probabilité d’un repli : quand l’écart 60 jours dépasse +20%, la probabilité d’une baisse de -5% dans les 10 séances passe de 16% à **63%**.
- Mais les 41 jours de signal ne sont pas 41 observations indépendantes. Ils se regroupent en **8 épisodes**, dont seulement 6 ont une fenêtre prospective complète.
- Conclusion : **une réduction partielle du risque se justifie, mais ce n’est pas un signal de sortie totale**. Les portes écart et volatilité sont ouvertes; la pente de la moyenne 20 jours reste haussière.

<div class="thesis-callout">
  <div class="thesis-callout__label">Point central</div>
  <div class="thesis-callout__body">
    L’écart 60 jours de +28,6% ne dit pas <strong>« c’est le sommet »</strong>. Il dit que la tendance est devenue trop rapide et qu’il faut réduire la poursuite, récupérer une partie du budget de risque et attendre une meilleure fenêtre.
  </div>
</div>

## Cadre reproduit

| Élément | Paramètre |
|---|---|
| Indice | KOSPI, `^KS11` |
| Période | 2025-01-02 à 2026-06-19 |
| Échantillon | 355 séances |
| Prix | Clôture |
| Écart | `clôture / moyenne mobile N jours - 1` |
| Fenêtres | 20, 60, 120 jours |
| Correction | Point bas de -5% ou plus dans les 10 séances suivantes |

## État actuel

| Mesure | Reproduction |
|---|---:|
| Clôture KOSPI | **9 052** |
| MM20 / écart20 | **8 322 / +8,77%** |
| MM60 / écart60 | **7 039 / +28,61%** |
| MM120 / écart120 | **6 088 / +48,69%** |
| Pente 5J de la MM20 | **+4,25%** |
| RSI(14) | **SMA 57,3 / Wilder 65,9** |
| ATR(20)% | **zone 4%** |

Le signal n’est pas un signal RSI. C’est un signal d’écart extrême par rapport à la moyenne 60 jours et de volatilité élevée.

## La surchauffe ne prédit pas bien les sommets

| Signal | Jours | Rendement moyen +5J | Rendement moyen +20J |
|---|---:|---:|---:|
| Écart20 ≥ 7% | 74 | +2,68% | +9,07% |
| Écart60 ≥ 12% | 120 | +2,26% | +6,88% |
| Écart120 ≥ 20% | 107 | +2,55% | +9,11% |
| Baseline | 335 | +1,86% | +7,83% |

Dans une tendance forte, la surchauffe peut d’abord signifier accélération.

## Mais l’écart60 augmente le risque de repli

| Condition | Jours | Correction de -5% en 10 séances |
|---|---:|---:|
| Baseline | tous | **16%** |
| Écart60 ≥ 15% | 89 | **36%** |
| Écart60 ≥ 18% | 54 | **48%** |
| Écart60 ≥ 20% | 41 | **63%** |
| Écart60 ≥ 22% | 33 | **67%** |
| Écart60 ≥ 25% | 26 | **65%** |

La bonne lecture est donc : le risque de pullback augmente, pas “tout vendre”.

## Limite statistique

Les 41 jours de signal forment seulement 8 épisodes. Les 6 épisodes complétés ont tous produit une correction de -5%, mais l’échantillon est trop petit pour graver des seuils précis. Le cadre est utile pour ajuster le risque, pas pour transformer 20% ou 25% en règle mécanique.

## Trois portes actuelles

| Porte | Règle | Valeur | État |
|---|---|---:|---|
| Survitesse moyenne | Écart60 ≥ 18-20% | **+28,6%** | Ouverte |
| Volatilité | ATR ≥ 2,2% | **zone 4%** | Ouverte |
| Détérioration tendance | Pente MM20 se retourne | **+4,25%** | Pas encore |

Deux portes sont ouvertes. Cela plaide pour moins de poursuite et une réduction partielle du risque. Mais la troisième n’est pas ouverte. Ce n’est donc pas un signal de sortie totale.

## Conclusion

Le KOSPI est en vraie surchauffe d’écart. Mais les données reproduites ne soutiennent pas une lecture “sommet confirmé”.

Le bon usage est un rebalancement : arrêter de courir après le marché, récupérer une partie du budget de risque et attendre soit une détérioration de tendance, soit un repli plus propre.
