---
title: "Les 40 Tenbaggers américains de 2023-2026 : La Full Stack IA-Infrastructure, et sa Corrélation avec les 27 Coréens"
slug: us-tenbagger-census-2023-2026-2026-04-23
date: 2026-04-23T21:00:00+09:00
description: "Recensement complet sur 3 ans des tenbaggers américains : 40 valeurs sur 1 690 titres, 33 % appartiennent à la full stack IA-infra, médiane 15,7× contre 13,8× pour la Corée. Là où les États-Unis ouvrent la voie, la Corée suit avec un décalage de 3 à 6 mois — voici la carte des pair-trades."
categories: ["Marché américain", "Marché coréen"]
tags: ["tenbagger", "marché-américain", "IA-infrastructure", "pair-trade", "biotechnologie", "quantique", "série"]
series: ["tenbagger-analysis-2026"]
---

> **Série — Tenbagger Analysis 2026 (Partie 2 sur 2)**
> ① [Les 27 Tenbaggers coréens de 2023-2026](/en/post/kr-tenbagger-census-2023-2026-2026-04-23/) — le volet KOSPI + KOSDAQ
> ② **Cet article** — le volet américain : 40 valeurs, la colonne vertébrale IA-infra, et le pair-trade avec la Corée

---

## Pipeline de données — Posons les bases

- **Univers** : 5 843 tickers américains. Historique reconstitué du 2023-01-01 au 2026-04-23 via yfinance avec `auto_adjust=True` (ajusté des splits et dividendes → correspond aux rendements effectivement réalisés par les investisseurs).
- **Couverture après reconstitution** : 1 690 tickers disposant d'un historique antérieur à juin 2023. Les IPO post-2024 et les valeurs radiées de la cote sont naturellement exclues.
- **Filtre** : premier cours de clôture dans les 30 jours suivant le 2023-04-24, détenu jusqu'au 2026-04-23, rendement total ≥ 10×.
- **Résultat** : **40 tenbaggers** confirmés.

---

## La distribution — 40 valeurs, moyenne 19,3×

| Multiple | Nombre | Valeurs représentatives |
|---|:-:|---|
| **≥50×** | 3 | AAOI (69,5×), DAVE (50,7×), CVNA (49,8×) |
| 20–50× | 10 | RGC, TSSI, RGTI, APP, PSIX, AXTI, RKLB, CRDO, ALM, PRAX, BWAY |
| 15–20× | 9 | ASTS, PLTR, POWL, LITE, SYRE, CRVS, SMMT, WDC, RCAT |
| 10–15× | 17 | ROOT, WULF, SLNO, IESC, ONDS, STRL, CELC, IREN, AMSC, STX, LPTH, APLD, REAL, HYMC, TTMI, TSHA, KINS |

- **Multiple moyen** : 19,3× (Corée : 17,4×)
- **Multiple médian** : 15,7× (Corée : 13,8×)
- **Maximum** : AAOI à 69,5×
- **Rendement médian sur 3 ans** : ~1 480 % (médiane coréenne ~900 %, soit un ratio US/KR de ~1,6×)

Les États-Unis ne font pas que produire plus de tenbaggers que la Corée — les gagnants vont plus loin. La queue droite de la distribution est plus épaisse.

---

## La carte structurelle — 9 catégories

| Thème | Nombre | Part | Fourchette |
|---|:-:|---:|---|
| **IA Infrastructure Full Stack** | **13** | **33 %** | 10–69,5× |
| Biotechnologie mono-actif | 8 | 20 % | 10,1–21,2× |
| Value profonde / redressement | 6 | 15 % | 10,6–50,7× |
| Espace / Défense / Drone | 4 | 10 % | 13,5–23× |
| Mineur crypto → Calcul IA | 3 | 8 % | 10,9–14,4× |
| Logiciel IA / Plateforme | 2 | 5 % | 18,8–30,5× |
| **Redressement assurance** | **2** | **5 %** | 13,4–14,8× |
| Quantique | 1 | 3 % | 38,5× |
| Minéraux de spécialité | 1 | 3 % | 21,9× (ALM) |

Trois enseignements se détachent.

**Premier.** L'infrastructure IA représente un tiers de la liste. Non pas « IA » au sens large — l'*infrastructure* IA : transceivers optiques, disques durs nearline pour les données d'entraînement, PCB haute-densité multicouches, appareillages et transformateurs pour centres de données, construction électrique hyperscale. Ce sont des fournisseurs d'outils et d'équipements qui ont livré la marchandise.

**Deuxième.** Les thèses biotechnologie mono-actif ont produit 8 valeurs — toutes au départ entre 1 $ et 16 $, avec des binaires essai clinique « tout ou rien ». C'est un profil structurel que le marché coréen ne génère pratiquement pas à cette échelle.

**Troisième.** Le quantique, les redressements d'assureurs et les minéraux de spécialité ont chacun produit un gagnant autonome qui échappe au récit consensuel. La liste 2023 n'était pas uniquement « IA ».

---

## IA Infrastructure — La Full Stack

Voici la décomposition des 13 valeurs IA-infra par sous-couche :

| Sous-couche | Valeurs | Moteur |
|---|---|---|
| **Transceivers optiques IA** | AAOI 69,5× / CRDO 22,5× / LITE 18,4× / AXTI 28,6× / LPTH 11× | Transition 800G / 1,6T + adoption NVIDIA GB200 |
| **Stockage (DC IA)** | WDC 15,7× / STX 11× | Explosion des HDD nearline pour les données d'entraînement IA |
| **PCB (accélérateurs IA)** | TTMI 10,3× | PCB haute densité multicouches pour cartes IA |
| **Alimentation centres de données** | POWL 18,6× / AMSC 11,8× | Appareillages + transformateurs |
| **Construction électrique DC** | STRL 13× / IESC 13,5× / TSSI 38,8× | Répercussion des dépenses capex hyperscale |

C'est la **carte exacte des pair-trades coréens** :

| Primaire US | Dérivé coréen | Relation |
|---|---|---|
| AAOI / CRDO / LITE | Isu Petasys, DAP | Optique IA → PCB haute densité |
| POWL / AMSC | HD Hyundai Electric, BHI, Boseong Powertech | Alimentation DC → transformateurs |
| STX / WDC | SK Hynix, Samsung Electronics | Stockage IA → HBM |
| STRL / IESC / TSSI | Contractants électriques KOSPI | Capex hyperscale US → EPC coréen suit |

Le schéma est le suivant : **les primaires US ouvrent la voie, la Corée suit avec un décalage de 3 à 6 mois.** Quand le primaire US dépasse ses fondamentaux, le dérivé coréen atteint son pic. Quand le primaire US corrige, le dérivé coréen surréagit à la baisse.

Ce n'est pas une affirmation narrative — c'est visible dans la dispersion des multiples. Isu Petasys a atteint son pic *après* AAOI. HD Hyundai Electric a atteint son pic *après* POWL. Le décalage est réel.

---

## Contrôle qualité — Qui a déjà dépassé son objectif

Les données d'objectifs du côté vendeur sont déterminantes ici. Sur les 40 valeurs :

| Catégorie | Objectif analyste vs cours actuel | Lecture |
|---|---|---|
| Primaires IA-infra (AAOI, AXTI, POWL, IESC, LITE, WDC, STX, TTMI, RKLB, BWAY) | **Déjà sous l'objectif** (−11 à −40 %) | Ont dépassé les fondamentaux — zone de prise de bénéfices |
| Pivots crypto→IA (IREN, APLD, WULF) | +27 à +54 % de potentiel résiduel | Encore de la marge |
| Biotechnologie (PRAX, CRVS, SMMT, SLNO) | +15 à +97 % de potentiel résiduel | Événement-dépendant — asymétrie favorable |
| Quantique (RGTI) | +72 % de potentiel résiduel | Beta thématique toujours en expansion |
| Value profonde (CVNA, DAVE, ROOT) | +14 à +48 % de potentiel résiduel | Pas encore entièrement revalorisés |

**Lecture clé** : les primaires IA-infrastructure sont ceux pour lesquels le côté vendeur *a déjà rattrapé* le marché. Si vous avez manqué le mouvement, acheter ici revient à acheter une action qui traite au-dessus du consensus analyste. C'est rarement le trade asymétrique.

Là où le consensus *accuse encore du retard* : les pivots crypto→calcul IA, les biotechs mono-actif, le beta quantique. Ce sont les candidats à la continuation 2026-2027, pas les primaires infrastructure.

---

## Décomposition factorielle — Profils de point d'entrée

Au point de départ d'avril 2023 :

| Facteur | IA Infra (11) | Crypto→IA (3) | Biotech (8) | Value profonde (6) | Espace/Drone (4) |
|---|---|---|---|---|---|
| Rentable en avril 2023 | Majoritairement oui | Non | **Tous non** | Tous non | Tous non |
| CA YoY (actuel) | +20–50 % | En forte hausse | Porté par les essais | +10–20 % | +30–100 % |
| P/E prospectif actuel | 25–50× | 45–685× | Déficitaire | 18–59× | Déficitaire |

Deux enseignements pratiques :

1. **Les valeurs IA-infra étaient déjà bénéficiaires en 2023.** Elles n'étaient pas des billets de loterie. Un filtre « qualité + visibilité des bénéfices » les aurait identifiées. Les tenbaggers biotech et espace n'auraient pas passé ce filtre — c'étaient des trades purement narratifs/catalyseurs.
2. **Le prix d'entrée compte.** Chaque tenbagger biotech est parti de 1 $ à 16 $. Les redressements value profonde ont démarré sous les 5 $. Le bas prix nominal était un facteur réel dans la réalisation du 10× — non pas parce qu'un bas prix est magique, mais parce qu'il signale un prix pré-catalyseur.

---

## Ce que la liste coréenne ne contient *pas*

Croisement avec la Partie 1. Deux archétypes entiers sont structurellement absents de la Corée :

**1. Biotechnologie mono-actif 10× à grande échelle.** Les États-Unis ont produit 8 valeurs partant de 1 $ à 16 $ sur des binaires cliniques. La Corée compte Peptron et HLB à 7× — mais rien qui ait progressé de 1 $ à 337 $ comme PRAX. Pourquoi ? La biotech coréenne est revalorisée *pendant* la phase 2 (avant les données) et se replie *avant* la lecture de phase 3. Le marché américain permet la montée en puissance complète jusqu'à l'homologation. Microstructure de marché différente, distribution des résultats différente.

**2. Redressement après survie 10×.** CVNA est passé de 3,55 $ et des rumeurs de faillite à plus de 180 $. La Corée ne produit pas ce profil, car les valeurs sous surveillance administrative tendent à être directement radiées plutôt que restructurées. Le marché américain du Chapter 11 et les spreads de crédit négociables créent un ensemble de valeurs « quasi-faillite → survie » qui n'existent tout simplement pas sur le KOSDAQ.

Pour un investisseur coréen souhaitant s'exposer à ces profils : **XBI** pour une exposition large à la biotech, ou des positions directes en ADR sur SMMT / DAVE / CVNA pour les paris concentrés. Ces profils ne sont pas reproductibles via des valeurs cotées en Corée.

---

## Le cluster Redressement Assurance (ajouté après la reconstitution)

Quand la reconstitution du pipeline de données a été complétée (de 1 479 à 1 690 tickers), un nouveau tenbagger est apparu : **KINS (Kingstone Companies)** à 13,4×, un assureur dommages régional de l'État de New York passé de 1,3 $ à 17 $.

Combiné à ROOT (assurance auto par IA, 14,8×), cela constitue un mini-thème discret de **Redressement Assurance**. La montée des combined ratios au-dessus de 110 % en 2022-23 a imposé de la discipline en dommages — les taux de réassurance se sont durcis, la souscription s'est resserrée, et le ROE 2024-25 s'est normalisé au-dessus de 20 %.

- ROOT → maturité de la télématique
- KINS → bénéficiaire de la consolidation régionale

Équivalent coréen : **Meritz Fire, Hanwha General Insurance** — normalisation du ROE similaire, mais les multiples n'ont progressé que de 3 à 4× (pas d'équivalent tenbagger domestique).

---

## Actionnable — Trois angles pour un gérant basé en Corée

**A. Discipline pair-trade sur la stack IA-infra.** Quand les primaires US traitent sous les objectifs des analystes, les dérivés coréens sont en sursis. Lecture actuelle : AAOI, CRDO, LITE, POWL, IESC tous sous objectif → Isu Petasys, HD Hyundai Electric, complexe coréen des réseaux électriques en zone de prise de bénéfices. C'est l'enseignement le plus actionnable de l'ensemble de données.

**B. Candidats du prochain cycle.** Où le côté vendeur *accuse-t-il encore du retard* ?
- **Semis edge-AI** — noms InP/GaN de taille plus modeste (Navitas, Power Integrations) sous l'échelle d'AXTI
- **Infrastructure quantique** — RGTI seul a imprimé 38,5× ; IONQ / QUBT / QMCO ont encore de la marge multiple
- **IA robotique** — Symbotic et d'autres ne sont pas encore tenbaggers, mais sont des narratives candidates pour 2026-2028
- **Pivots crypto→IA avec potentiel résiduel** — IREN, APLD, WULF

**C. Lacunes structurelles.** L'exposition US à la biotechnologie mono-actif et aux redressements après survie ne peut pas être répliquée via des valeurs cotées en Corée. Soit en ADR direct (SMMT, PRAX, CVNA, DAVE), soit via XBI pour une exposition diversifiée.

---

## Signaux de risque

1. **P/E prospectif au-dessus de 100×** — PLTR 107×, AAOI 100×, LITE 102×, WULF 685×, ASTS 99×. Un déclassement du consensus = risque de −30 à −50 %.
2. **Déjà sous l'objectif analyste** — WDC, STX, LITE, IESC, POWL, AAOI, AXTI, TTMI, BWAY, RKLB. Le marché a pris de l'avance ; les stops suiveurs ont leur importance.
3. **Prix de départ sous 1 $** — vérifier l'intérêt short et les dépôts SEC avant d'extrapoler (RGC présente des signaux de manipulation de type TCM-pump).
4. **Pivots crypto→IA** — double exposition au Bitcoin et aux dépenses capex hyperscaler. Une rupture dans l'un ou l'autre = −50 %.

---

## Conclusion

> 40 tenbaggers américains sur 3 ans. 33 % appartiennent à la full stack IA-infrastructure — optique, stockage, PCB, alimentation, construction électrique. Les 27 tenbaggers coréens sont la **couche dérivée de second ordre** de ce même trade (HBM, PCB haute densité, transformateurs). Les primaires infrastructure américains traitent désormais *au-dessus* des objectifs analystes — zone de prise de bénéfices. La rotation s'oriente vers les **pivots crypto→IA, les biotechs mono-actif, le quantique et les redressements d'assureurs**, où le consensus accuse encore du retard.

La carte des pair-trades est l'enseignement le plus transférable : **les valeurs dérivées coréennes de l'IA suivent les primaires américains avec un décalage de 3 à 6 mois, et surréagissent dans les deux sens.**

---

## La suite

1. **Backtest de cointégration paires KR-US.** AAOI hebdomadaire vs Isu Petasys hebdomadaire aux décalages 0/30/60 jours — la relation est-elle tradeable ?
2. **Reverse-screen Russell 2000** en utilisant le profil tenbagger d'avril 2023 (ROE / P/E prospectif / CA YoY / rendement 2 ans) — identifier les candidats 2026 avant leur breakout.
3. **Calendrier des événements biotech ADR** — lectures prochaines des essais SMMT, PRAX, SLNO, SYRE.
4. **Vérification du pic du cycle capex IA** — guidance capex 2026 de MSFT / META / AMZN / GOOGL vs réalisé 2025. Signal primaire indiquant quand les valeurs infra américaines vont finalement corriger.

---

_Cet article clôt la série Tenbagger Analysis 2026. [Partie 1 : les 27 tenbaggers coréens et pourquoi le réseau électrique a discrètement surpassé l'IA.](/en/post/kr-tenbagger-census-2023-2026-2026-04-23/)_

_Toutes les valeurs mentionnées sont des pistes de réflexion, non des recommandations. Rien dans cet article ne constitue un conseil en investissement._
