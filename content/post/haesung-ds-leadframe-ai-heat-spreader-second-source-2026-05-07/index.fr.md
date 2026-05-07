---
title: "Haesung DS (195870.KS) — Lead-Frame coréen #2 en pivot vers la seconde source de dissipateurs thermiques pour l'IA : choc de marges au 1T26, taux d'utilisation DDR5, et pourquoi la revalorisation repose sur la compression des multiples, pas sur le chiffre d'affaires"
slug: haesung-ds-leadframe-ai-heat-spreader-second-source-2026-05-07
date: 2026-05-07T20:00:00+09:00
description: "Haesung DS n'est pas un proxy HBM pur. C'est un candidat à la revalorisation sur trois axes : reprise du lead-frame automobile (≈75 % du chiffre d'affaires), normalisation du taux d'utilisation des substrats mémoire DDR5 (1S25 ~30 % → 2026 ~70 %), et l'option d'entrée en tant que seconde source de dissipateurs thermiques pour data centers IA. Le 1T26 a affiché un chiffre d'affaires de ₩188,7 Mds (+37,2 % en glissement annuel), mais la marge opérationnelle s'est effondrée à 5,8 % en raison du décalage de répercussion des coûts matières. Le marché des dissipateurs de boîtiers CI — Shinko, Honeywell/Solstice, Jentech, I-Chiun représentant ~85 % de concentration, TAM 2024 ~567 M USD, TCAC 9,7 % — présente des tensions de capacité alors que la puissance des accélérateurs IA dépasse 700 W+. Haesung DS qualifie des échantillons de heat slugs au 2T26 avec un potentiel de revenus au 2S26. Scénario de base : seconde source de heat slugs flat, contribution 2026 de ₩5–20 Mds montant à ₩20–50 Mds en 2027 — trop modeste pour peser sur le compte de résultat, mais suffisant pour déclencher une reclassification des multiples, de fournisseur automobile de lead-frames vers la chaîne d'approvisionnement thermique IA. La clôture à 86 000 wons (capitalisation ₩1,46 kMds) intègre déjà une partie de l'axe 3 ; la question opérationnelle est de savoir s'il faut acheter ici ou attendre le retest des 82 000–84 000."
categories: ["Sector-Deep-Dive", "Korea Market", "Semiconductors"]
tags:
  - "Haesung DS"
  - "195870"
  - "lead frame"
  - "dissipateur thermique"
  - "heat slug"
  - "gestion thermique IA"
  - "packaging IA"
  - "substrat de boîtier"
  - "DDR5"
  - "Shinko"
  - "Honeywell"
  - "Solstice"
  - "Jentech"
  - "I-Chiun"
  - "semiconducteurs coréens"
  - "semiconducteurs automobiles"
  - "seconde source"
---

> 🔗 **Connexe** : [Hub PCB & substrats IA](/page/korea-ai-pcb-substrate-hub/) · [Hub Semi coréens · HBM](/page/korea-semiconductor-hbm-kospi-hub/) · [Écosystème PCB IA coréen — 10 entreprises](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/)

*L'[article de thèse sur les PCB IA](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) a posé la demande en substrats IA comme un goulet d'étranglement à l'échelle du système — non pas une histoire de puce unique, mais une nomenclature à l'échelle du rack. Cet article ajoute le onzième nom à ce groupe : **Haesung DS (195870.KS)**, dont l'angle d'entrée pour les allocateurs étrangers est inhabituel. Contrairement aux dix autres — tous des acteurs PCB, substrat ou CCL — Haesung DS occupe un nœud différent : **un composeur de lead-frames automobiles potentiellement en pivot vers la seconde source de dissipateurs thermiques IA**, dans un marché que les acteurs en place (Shinko, Honeywell/Solstice, Jentech, I-Chiun) contrôlent à \~85 %, sans pour autant disposer de la capacité nécessaire pour satisfaire la demande.*

---

## TL;DR

* **Haesung DS n'est pas un pur jeu IA. C'est un candidat à la revalorisation sur trois axes.** Axe 1 : reprise du lead-frame automobile (≈75 % du mix de revenus). Axe 2 : normalisation du taux d'utilisation des substrats mémoire DDR5 (1S25 \~30 % → 2026 \~70 % selon KB Securities). Axe 3 : optionnalité d'entrée en tant que seconde source de dissipateurs thermiques pour data centers IA. Les trois axes n'ont pas besoin de se déclencher simultanément — ils s'accumulent séquentiellement, ce qui rend l'asymétrie intéressante.
* **Le 1T26 a été un choc de timing entre revenus solides et marges dégradées, pas une rupture structurelle.** Chiffre d'affaires de ₩188,7 Mds (+37,2 % en glissement annuel, quasi-record), mais résultat opérationnel de ₩11,0 Mds à 5,8 % de marge opérationnelle — contre 12,1 % au 4T25. L'explication est le décalage d'environ un trimestre entre la hausse des coûts d'intrants Cu/Au/Ag/Pd et la répercussion sur les ASP clients. Le résultat opérationnel du 2T26 est le premier jalon de vérification. Le consensus sell-side table sur un CA de ₩208,5 Mds et une marge opérationnelle de 10 % au 2T.
* **L'entrée dans les dissipateurs thermiques IA est « techniquement plausible » — mais l'interpréter comme une fourniture directe de couvercles GPU haut de gamme est un excès.** Le marché des dissipateurs de boîtiers CI est concentré à \~85 % entre Shinko (Japon), Honeywell/Solstice (États-Unis), Jentech (Taïwan) et I-Chiun (Taïwan). La capacité de Shinko serait saturée à mesure que la puissance des accélérateurs IA dépasse 700 W+, et les acteurs coréens du lead-frame reçoivent des demandes de développement de grands groupes technologiques. Scénario de base réaliste : **seconde source de heat slugs / dissipateurs plats**, et non des couvercles à chambre à vapeur ou à micro-canaux (ces produits restent chez Jentech / I-Chiun).
* **La contribution directe au chiffre d'affaires est trop faible pour peser sur le compte de résultat. Le mécanisme de revalorisation passe par la compression des multiples, pas par la puissance bénéficiaire.** Le TAM est d'environ 567 M USD en 2024, avec un TCAC de 9,7 %. Une part de 3 % sur le TAM 2026 (\~682 M USD) au cours USD/KRW 1 450,98 implique \~₩29,7 Mds — soit environ 4,5 % du chiffre d'affaires FY25 de ₩653,4 Mds. La valeur de l'investissement réside dans la **reclassification** de la société — de « cyclique lead-frame automobile + substrat DDR » à « seconde source dans la chaîne thermique IA » — et dans la compression de la décote vers les pairs coréens spécialisés substrats IA.
* **86 000 wons (capitalisation ₩1,46 kMds) est une zone "bon dossier / mauvais prix".** Clôture +10,3 %, rendement 20J +65,4 %, 26 % au-dessus de la MMA20, RSI14 à 71,9. Acheter à la poursuite n'est pertinent que comme position pilote de 30–50 pb. L'entrée asymétrique se situe au retest des 82 000–84 000, niveau du précédent sommet à 83 800. Cassure des 76 000 = réévaluation de la thèse technique.

---

## 1. Ce qu'est réellement Haesung DS — pour l'allocateur étranger qui ne connaît pas ce nom

Haesung DS **n'est pas un fabricant de puces**. Ce n'est ni une fonderie, ni un fabricant de mémoire, ni un OSAT. Il fabrique les **pièces métalliques et les substrats qui se trouvent à l'intérieur du boîtier semiconducteur** — le lead-frame qui relie la puce au PCB, et le substrat de boîtier mémoire qui relie les puces DRAM à la carte mère.

| Élément | Détail |
|---|---|
| Société | Haesung DS / HAESUNG DS |
| Ticker | KOSPI 195870 |
| Siège / Sites | Siège à Gangnam (Séoul) + usine de Changwon + présence commerciale et de production en Chine / Japon / Philippines |
| Segments d'activité | Lead frame + Substrat de boîtier mémoire + Substrat sur bande + Graphène |
| Date de référence | 2026-05-07 |
| Cours de clôture / capitalisation boursière | KRW 86 000 / \~KRW 1,46 billion |
| Positionnement sectoriel | **Lead-frame #2 mondial** (Mitsui High-Tec est #1) |

Les deux piliers de revenus sont le Lead Frame et le Substrat de boîtier. Le chiffre d'affaires FY25 était de ₩653,4 Mds — Lead Frame \~₩493,8 Mds (75,6 %) et Substrat de boîtier \~₩159,6 Mds (24,4 %) selon les estimations sectorielles de Kyobo Securities (la société publie un chiffre d'affaires et un résultat opérationnel consolidés, sans ventilation complète par segment).

Pour l'allocateur qui ne détenait pas ce titre jusqu'ici, le résumé en deux lignes :

* **Le lead-frame est le « squelette métallique » à l'intérieur d'un boîtier de puce** : la structure qui soutient la puce, achemine les signaux vers le PCB, transporte le courant et dissipe la chaleur. Les lead-frames automobiles en particulier sont difficiles à substituer sur le critère du prix, car les circuits intégrés automobiles exigent des qualifications sur cycles longs, une traçabilité complète, des données de fiabilité AEC-Q100 et des taux de défauts très faibles en PPM. C'est le premier niveau de fossé concurrentiel.
* **Le substrat de boîtier est un petit circuit imprimé entre les puces mémoire et la carte mère**. L'avantage de Haesung DS est son **procédé de lamination en continu bobine à bobine (R2R)** — plus proche d'une fabrication en volume rouleau par rouleau que d'un traitement panneau par panneau. Le R2R ne concurrence pas les FC-BGA à haute densité de couches pour l'IA (ce domaine appartient à Samsung Electro-Mechanics, Daeduck, Ibiden, AT&S, etc.), mais il présente des avantages de coût et de rendement sur les substrats mémoire DDR4/DDR5 en volume.

La nouvelle couche optionnelle intégrée dans le cours de clôture à 86 000 wons est l'opportunité dans les **dissipateurs thermiques / heat slugs pour data centers IA**.

---

## 2. Les résultats du 1T26 — chiffre d'affaires solide, marges dégradées

### 2-1. Évolution trimestrielle du compte de résultat

(Mds KRW)

| Période | Chiffre d'affaires | Marge brute | Résultat opérationnel | Marge op. | Δ |
|---|---:|---:|---:|---:|---|
| FY24 | 603,0 | 18,5 % | 56,9 | 9,4 % | base |
| FY25 | 653,4 | 15,0 % | 46,5 | 7,1 % | CA +8,4 % / RO -18,3 % |
| 4T25 | 179,9 | 19,7 % | 21,8 | 12,1 % | RO T/T +35 % |
| **1T26** | **188,7** | **12,3 %** | **11,0** | **5,8 %** | **CA +37,2 % a/a / RO T/T -49,6 %** |
| 1T26 TTM | 704,6 | 15,3 % | 57,1 | 8,1 % | CA +7,8 % / RO +22,8 % vs. FY25 |

Le choc est marqué. Le chiffre d'affaires a atteint un quasi-record — le seul segment automobile a livré \~₩91,0 Mds (≈48 % du total). Mais le résultat opérationnel a été divisé par deux séquentiellement, et la marge opérationnelle est passée de 12,1 % au 4T25 à 5,8 % au 1T26.

### 2-2. La cause est mécanique, pas structurelle — mais la vérification est nécessaire

Les prix des intrants Cu, Au, Ag et Pd ont progressé avant la répercussion sur les ASP clients, avec un décalage d'environ un trimestre. Le 1T26 s'est clôturé avec des matières premières coûteuses encore dans le coût des ventes et des ASP pas encore réajustés. C'est le schéma classique de « pression des coûts sur les marges » dans une société de composants à capitalisation moyenne.

Trois lectures, par ordre de probabilité :

1. **Problème de timing (haute probabilité)** — Les ASP du 2T26 rattrapent leur retard, la marge opérationnelle se normalise à \~10 %. Le 1T est un accident ponctuel. C'est ce que le consensus intègre.
2. **Pression structurelle sur les marges (probabilité moyenne)** — Les clients résistent aux hausses de prix, ou les entrants chinois à bas coût réduisent l'écart. La marge opérationnelle se stabilise à 7–8 %.
3. **Ralentissement de la demande (faible probabilité)** — Le chiffre d'affaires du 2T lui-même se retourne. La progression de +37,2 % en glissement annuel au 1T rend ce scénario le moins probable à court terme, mais les cycles d'inventaire VE / CI automobiles ne sont pas à exclure.

Le consensus sell-side (Meritz) table sur un CA de ₩208,5 Mds au 2T26, un résultat opérationnel de ₩20,8 Mds et une marge opérationnelle de \~10 %. **La clôture à 86 000 wons est valorisée pour le scénario 1.** Si le résultat opérationnel du 2T ressort en dessous de ₩15 Mds, la thèse de redressement est invalidée et un repli des cours serait rationnel.

---

## 3. Décomposition de l'activité entre axes « core » et axes « optionnels »

Le modèle mental le plus clair pour Haesung DS — et celui qui rend l'asymétrie visible — consiste à séparer ce qui est déjà en cours de ce qui est intégré comme optionnalité.

### Axe 1 — Core : reprise déjà amorcée

| Élément | Situation 1T26 | Trajectoire 2026 |
|---|---|---|
| Lead-frame automobile | \~₩91 Mds trimestriels (48 % du total, quasi-record) | Reprise VE / CI auto → stabilisation du rythme trimestriel à \~₩90 Mds |
| Taux d'utilisation substrat de boîtier | 1S25 \~30 % → reprise en cours au 1T26 | KB Securities modélise 70 %+ en 2026 → effet levier sur coûts fixes |
| Substrat DDR5 / D1b / D1y | Clients coréens / chinois / américains anonymes en qualification ou début de ramp | Le 4T25 a été le premier trimestre substrat rentable en sept ; mix 2026 en hausse |

Cet axe seul soutient un CA 2026 de ₩733–784 Mds et un résultat opérationnel de ₩79–109 Mds (fourchette sell-side : iM ₩733,5 Mds / ₩79,0 Mds / 10,8 % de marge opérationnelle, conservateur ; KB ₩784,3 Mds / ₩108,9 Mds / 13,9 % de marge opérationnelle, agressif). Le scénario haussier de KB repose sur un taux d'utilisation substrat atteignant 70 %.

### Axe 2 — Optionnel : entrée dans les dissipateurs thermiques pour data centers IA

C'est l'axe qui a motivé la réaction de +10,3 % le 7 mai.

* L'espace des dissipateurs de boîtiers CI est concentré à \~85 % entre **Shinko (Japon), Honeywell/Solstice (États-Unis, à la suite du spin-off Honeywell Advanced Materials en octobre 2025), Jentech (Taïwan), I-Chiun (Taïwan)**. Shinko est l'acteur historique dans les dissipateurs thermiques de CPU serveur — l'emboutissage et la finition de surface constituent son socle de compétences.
* La puissance des accélérateurs IA a dépassé 700 W+ (classe Blackwell, MI300) et continue d'augmenter. Les exigences thermiques des dissipateurs de boîtiers progressent avec la taille des packages, le gauchissement et les contraintes de contact TIM. **La capacité de Shinko serait saturée**, et les acheteurs big-tech sollicitent explicitement des fournisseurs de lead-frames comme secondes sources potentielles.
* La chaîne de fabrication de lead-frames de Haesung DS — gravure chimique, emboutissage, placage Ag, placage PPF, down-set, outillage à ±2 μm/m, deep down-set, traitement de surface AEC-Q100 Grade 0 — est le point de départ **nécessaire**. La question est de savoir s'il est **suffisant**.
* Selon les informations disponibles (EBN, commentaires de Lim Eun-young de Samsung Securities), Haesung DS conduit des tests qualité de heat slugs chez un client au 2T26, avec une contribution au chiffre d'affaires au 2S26 si la commande est confirmée.

Cet axe **n'est pas encore le scénario central pour le compte de résultat**. Mais il **est déjà partiellement intégré dans le cours**.

---

## 4. Cartographie de ce qu'Haesung DS peut — et ne peut pas — réaliser dans le thermique IA

### 4-1. Chaîne de valeur thermique des serveurs IA en quatre niveaux

| Niveau | Composant | Concurrents clés | Probabilité de pénétration Haesung DS |
|---|---|---|---:|
| **Couvercle métallique de boîtier / dissipateur thermique** | Heat slug, dissipateur, lid, raidisseur | Shinko, Honeywell/Solstice, Jentech, I-Chiun | **Moyenne** |
| Couvercle avancé | Couvercle à chambre à vapeur, couvercle à micro-canaux | Jentech, I-Chiun | Faible |
| TIM | TIM1/1,5/2, film graphite, métal liquide, indium | Solstice, Henkel, Indium Corp | Faible |
| Refroidissement système | Plaque froide, module de refroidissement liquide, CDU, manifold | Delta, AVC, Auras, Jentech, Vertiv | Très faible |

**Seul le niveau 1 est dans le périmètre.** La thèse d'investissement est qu'Haesung DS devient une **seconde source de dissipateurs thermiques métalliques au niveau du boîtier**, et non qu'il devance les acteurs en place dans le refroidissement liquide ou les matériaux TIM.

### 4-2. Probabilité de pénétration par difficulté de produit

| Produit | Difficulté | Probabilité de pénétration | Raisonnement |
|---|---:|---:|---|
| Dissipateur CPU/GPU générique | Moyenne | **Moyenne–Élevée** | Fort chevauchement avec le procédé lead-frame existant |
| Heat slug ASIC IA / IA embarquée | Moyenne-Élevée | **Moyenne** | Co-conception client requise ; plus accessible que le GPU haut de gamme |
| Couvercle grand accélérateur IA classe Blackwell / MI300 | Élevée | **Faible–Moyenne** | Qualification incumbent + barrière gauchissement / optimisation TIM |
| Couvercle à chambre à vapeur | Très élevée | **Faible** | Jentech / I-Chiun en avance |
| Couvercle à micro-canaux | Très élevée | **Très faible** | Requiert l'intégration fluidique / refroidissement liquide |
| Matériaux TIM | Élevée | **Très faible** | Domaine Solstice / Honeywell |
| Plaque froide / système de refroidissement liquide | Élevée | **Très faible** | Hors du périmètre actuel |

**Lecture réaliste pour 2026** : « entrée dans le thermique IA » doit être interprétée comme une **seconde source de heat slugs plats**, et non comme un contrat de couvercles GPU haut de gamme.

### 4-3. Pourquoi un couvercle IA n'est pas simplement un « grand lead-frame »

La maîtrise du lead-frame est nécessaire mais pas suffisante. Les couvercles de boîtiers IA ajoutent des exigences absentes des spécifications lead-frame automobiles :

| Exigence | Pourquoi c'est important |
|---|---|
| Contrôle de la planéité / du gauchissement | Une mauvaise planéité fait chuter la résistance thermique au contact die-TIM |
| Uniformité de surface / de placage | Détermine la qualité de contact TIM1/TIM2 |
| Gestion du désaccord CTE | Les différences de dilatation thermique entre silicium, substrat et couvercle cuivre créent des contraintes dans le boîtier |
| Contrôle du dégazage et de la contamination | Affecte le rendement d'assemblage des boîtiers haut de gamme |
| Rendement d'usinage grande surface | Les boîtiers IA sont grands — les déformations infimes sont critiques |
| Co-conception client | Optimisation simultanée avec le fournisseur Nvidia / AMD / ASIC / fonderie / OSAT / TIM |

La planéité, l'uniformité de placage et la fiabilité du traitement de surface sont des domaines déjà maîtrisés par Haesung DS dans les lead-frames automobiles. La gestion du désaccord CTE, le rendement sur grande surface et la co-conception avec les équipes ASIC hyperscaler constituent un territoire propre à l'IA où **la qualification des acteurs en place est un résultat binaire**.

---

## 5. Scénarios de revenus — base / haussier / baissier

### 5-1. Calcul du TAM

Dissipateurs thermiques de boîtiers CI : \~567 M USD en 2024, TCAC \~9,7 % (étude de marché tierce ; à traiter comme ordre de grandeur).

```
TAM 2026E ≈ 567 M USD × 1,097² ≈ 682 M USD
TAM 2028E ≈ 567 M USD × 1,097⁴ ≈ 821 M USD
```

Au cours USD/KRW 1 450,98 (cours du 7 mai) :

| Hypothèse de part de marché | Traduction en revenus |
|---|---:|
| 1 % du TAM 2026E | \~₩9,9 Mds |
| 3 % du TAM 2026E | \~₩29,7 Mds |
| 5 % du TAM 2026E | \~₩49,5 Mds |
| 5 % du TAM 2028E | \~₩59,6 Mds |

**La contribution directe au chiffre d'affaires ne changera pas la donne sur le compte de résultat en 2026.** ₩29,7 Mds à une part de 3 % représentent \~4,5 % du CA FY25 de ₩653,4 Mds. La valeur de l'investissement réside dans la **compression des multiples**, pas dans la marge sur contribution.

### 5-2. Trois scénarios

| Scénario | Produit / client | Calendrier | Contribution 2026 | Contribution 2027 | Implication pour l'investissement |
|---|---|---|---:|---:|---|
| **Base** | Heat slug / dissipateur plat, seconde source anonyme big-tech ou packaging | Qualification 2T26 → petits revenus 2S26 | ₩5–20 Mds | ₩20–50 Mds | « Entrée confirmée dans la chaîne thermique IA » → compression de la décote |
| **Haussier** | Seconde source dissipateur ASIC IA / GPU, ≥2 qualifications clients | Fin 2026 → volumes 2027 | ₩10–30 Mds | ₩50–100 Mds | Reclassification de fournisseur lead-frame à fournisseur thermique IA — revalorisation significative des multiples |
| **Baissier** | Bloqué au stade échantillon / développement ; retards de tests client ; manque de rendement ; normalisation de la capacité incumbent | Revenus 2026 avortés | ₩0–5 Mds | ₩0–10 Mds | Repli du rally récent ; thèse abandonnée |

Les heat slugs **ressemblent** à de simples pièces métalliques. Ce sont en réalité des composants de fiabilité du boîtier. Échec à la qualification client = aucun revenu. Le scénario baissier est loin d'être négligeable.

---

## 6. Positionnement d'Haesung DS dans le cluster coréen de substrats IA

Ajout d'Haesung DS comme onzième nom au [cadre des 10 entreprises de l'écosystème PCB IA coréen](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) :

| Société | Exposition principale | Exposition directe IA | Angle distinctif |
|---|---|---|---|
| Samsung Electro-Mechanics | FC-BGA + MLCC | Très forte | Double exposition substrat IA + MLCC |
| Daeduck Electronics | FC-BGA / MLB | Forte | #2 coréen en volume FC-BGA |
| Isu Petasys | MLB | Forte | MLB pour cartes GPU IA |
| Simmtech | Substrat de boîtier mémoire | Moyenne | Substrat mémoire DDR5 |
| Korea Circuit | Substrat de boîtier | Moyenne | Mémoire + mobile |
| Doosan Electro-BG | CCL | Forte | CCL Low-Dk |
| Kolon Industries | Matériaux | Moyenne | Polyimide / film |
| Pamicell | Matériaux CCL | Moyenne | Proxy Doosan Electro-BG |
| TLB | PCB module mémoire | Moyenne | PCB module DDR5 |
| Taesung | Équipements | Moyenne | Équipements PCB |
| **Haesung DS (nouveau)** | **Lead frame + substrat DDR** | **Moyenne (avec forte optionnalité)** | **LF automobile + seconde source thermique IA** |

**L'angle distinctif d'Haesung DS dans le cluster** : c'est le seul nom qui **ne se situe pas** sur la ligne PCB / substrat / CCL. Les dix autres acteurs sont tous sur l'axe substrat ou alimentation substrat. Haesung DS suit une trajectoire évolutive parallèle — lead frame → thermique IA — que personne d'autre dans le cluster ne détient.

C'est aussi la raison structurelle de la réaction de +10,3 % le 7 mai. L'axe 1 (reprise LF auto) et l'axe 2 (substrat DDR5) sont largement anticipés par le marché, dans la continuité de la [synthèse du rally coréen des semi-conducteurs du 6 mai](/post/korean-semis-rally-may-6-samsung-sk-hynix-substrate-equipment-2026-05-07/). L'axe 3 (dissipateur thermique) **n'est pas encore pleinement intégré dans les chiffres de consensus** — et c'est ce que les multiples commencent à refléter.

---

## 7. Stratégie d'entrée à 86 000 wons

### 7-1. Situation technique du cours

| Indicateur | Valeur | Lecture |
|---|---:|---|
| Variation journalière | +10,3 % | Cassure à 52 semaines |
| Rendement 20J | +65,4 % | Pic court terme |
| Écart à la MMA20 | +26,2 % | Risque élevé à l'achat en poursuite |
| Écart à la MMA50 | +41,9 % | Surchauffe |
| RSI14 | 71,9 % | Proche de la zone de surachat |
| Volume | 1,7× moyenne 20J | Confirmation en volume de la cassure |
| Clôture dans la plage journalière | 81 % depuis le bas | Achats solides en fin de séance |

### 7-2. Vérification des multiples

Pour un résultat opérationnel 2026E de ₩79–109 Mds face à une capitalisation de ₩1,46 kMds, le ratio cap/RO est de **13,4–18,5×**. Les pairs coréens sur les substrats (Simmtech, Daeduck) se négocient à 17–22× le résultat opérationnel. **La borne supérieure est tendue, mais la borne inférieure reste raisonnable** — le multiple n'est pas encore à la moyenne des pairs.

### 7-3. Zones d'entrée

| Zone | Action |
|---|---|
| 85 000–87 000 (niveau actuel) | Achat uniquement comme position pilote de 30–50 pb |
| 82 000–84 000 | Première entrée préférentielle — retest du précédent sommet à 83 800 |
| 78 000–80 000 | Meilleur rapport risque/rendement — bas de la zone de cassure des 6–7 mai |
| 88 000+ en clôture | Renforcement uniquement si le volume se réexpanse et si les flux étrangers / institutionnels confirment |
| Cassure des 76 000 | Réévaluation de la structure technique |

ATR14 \~5 843 wons (\~6,8 % de volatilité journalière). Un repli normal d'1 ATR ramène autour de 80 000. La zone de retest des 82 000–84 000 est la zone asymétrique.

### 7-4. Pourquoi ne pas prendre une position pleine maintenant

1. **Le 1T26 a été un manquement, pas un dépassement.** Le chiffre d'affaires était bon, mais un résultat opérationnel de ₩11,0 Mds est inférieur aux attentes. Le cours actuel intègre déjà une reprise au 2T et une partie de l'optionnalité dissipateurs thermiques.
2. **La reprise n'a pas encore été confirmée.** Un résultat opérationnel 2T ≥ ₩20 Mds justifie le niveau. ≤ ₩15 Mds signifie l'échec de la cassure.
3. **Le graphique est solide mais étiré.** « Les bons dossiers vont plus loin » fonctionne comme biais tactique, mais pas en taille pleine depuis cette zone d'entrée.

Cadrage opérationnel pour un livre institutionnel : **bon dossier, mauvais prix**. Le retest est l'entrée de meilleure qualité.

---

## 8. Points de vérification et invalidation

| Fenêtre | Point de vérification | Lecture |
|---|---|---|
| Résultats 2T26 | Redressement de la marge opérationnelle + mention de la qualification heat slug | Reprise + axe 3 en progression |
| 2T–3T26 | Communication de nouveaux CAPEX ou conversion de ligne | Signal de montée en volume |
| 3T26 | Nouvelle ligne de revenus | Thème → chiffres |
| 2S26 | ≥2 clients en qualification | Risque de concentration client unique réduit |
| 2027 | Revenus dissipateurs thermiques ≥ ₩30 Mds | Preuve minimale de revalorisation |
| 2027 | Mention de couvercle avancé / chambre à vapeur / micro-canaux | Signal d'entrée dans le scénario haussier |
| À tout moment | Marge opérationnelle 2T26 persistant ≤ 7 % / blocage de la démarche heat slug | Repli du rally, thèse invalidée |

---

## 9. Risques

### Technologie
* **Le substrat R2R n'est structurellement pas adapté au FC-BGA haute densité / packaging 2,5D.** Interpréter Haesung DS comme bénéficiaire direct de la tendance packaging IA est un excès.
* **La qualification thermique IA est binaire.** Le heat slug / dissipateur est une optionnalité attractive, mais le client, la taille et les marges ne sont pas encore publiquement vérifiés.

### Activité / clients
* **La concentration client est opaque.** Le chiffre d'affaires par client n'est pas divulgué ; quantifier la dépendance envers les fabricants de mémoire ou les IDM automobiles est difficile.
* **Exposition automobile \~75–77 %.** Un ralentissement de la VE / conduite autonome impacte directement. Le mix mémoire est le plus faible du groupe de quatre pairs — le bénéfice direct du supercycle mémoire est le plus limité.
* **Décalage de répercussion des coûts matières.** Des pics sur Cu / Au / Ag / Pd peuvent reproduire le type de dégradation de marges observé au 1T26.

### Macro / réglementaire
* **La demande VE et la volatilité réglementaire** pilotent l'axe LF automobile.
* **Rééquilibrage de la chaîne d'approvisionnement sino-américaine** — affecte le mix client mondial, les contrôles à l'exportation et les devises.

### Valorisation
* **La décote est à double tranchant.** Le « bon marché pour de bonnes raisons » est en partie structurel (poids automobile + retardataire sur les substrats) et pourrait ne pas se comprimer en un seul trimestre.

---

## 10. Questions fréquentes

**Q : Haesung DS est-il un proxy HBM pur ?**
R : Non. Haesung DS ne produit pas de piles HBM. L'expansion de l'infrastructure IA tire la demande en substrats DDR4 / DDR5, ce qui constitue un **bénéfice de second ordre**. Pour une exposition directe au HBM, voir l'[analyse des parts de marché HBM de SK Hynix](/post/sk-hynix-hbm-market-share-ai-memory-demand-2026/).

**Q : Haesung DS peut-il détrôner Shinko ?**
R : Pas à court terme. Shinko détient la qualification incumbent sur les dissipateurs thermiques de CPU serveur. L'issue réaliste est la **coexistence en tant que seconde source** — absorption d'un écart de capacité, pas remplacement. Les acheteurs big-tech souhaitent diversifier leurs approvisionnements ; Haesung DS répond à cette demande d'allocateur, et non au récit de disruption.

**Q : La marge opérationnelle de 5,8 % au 1T26 est-elle structurelle ?**
R : Probablement pas. La progression de +37,2 % en glissement annuel du chiffre d'affaires et le décalage documenté d'un trimestre dans la répercussion des coûts matières pointent tous deux vers un problème de timing. **Le résultat opérationnel du 2T26 est le jalon de vérification** — un redressement à plus de 10 % tranche la question ; une persistance à ≤ 7 % imposerait une relecture structurelle.

**Q : Une exposition automobile de 75 % n'est-elle pas trop concentrée ?**
R : C'est le principal risque à double sens. Une demande solide en VE / CI auto porte l'axe 1 ; un retournement du cycle automobile impacte directement. La thèse dépend de l'accumulation des axes 2 (utilisation substrat DDR5) et 3 (dissipateur thermique) pour **diluer la dépendance automobile**. En tant que dossier mono-axe, c'est risqué ; en tant que candidat à la revalorisation sur trois axes, c'est viable.

**Q : La clôture à 86 000 est-elle achetable en poursuite ?**
R : Pas pour un livre en taille pleine. L'entrée asymétrique se situe au retest des 82 000–84 000. Achat en poursuite uniquement comme position pilote de 30–50 pb. Cassure des 76 000 = réévaluation de la structure technique. Traduction pour l'allocateur : « bon dossier, mauvais prix ».

**Q : Comment ce titre s'intègre-t-il aux côtés des autres noms de substrats IA coréens ?**
R : Il occupe un créneau qu'aucun des dix autres noms du cluster ne détient. Samsung Electro-Mechanics, Daeduck, Isu Petasys, Simmtech, Korea Circuit, Doosan Electro-BG, Kolon, Pamicell, TLB et Taesung sont tous sur l'axe substrat / CCL / équipements. Haesung DS est le **seul chemin « lead-frame → thermique IA »**. Du point de vue de la construction de portefeuille, cela apporte une véritable diversification d'angle plutôt qu'un proxy supplémentaire corrélé aux substrats IA.

**Q : Et si l'axe 3 (dissipateurs thermiques) échoue totalement ?**
R : L'axe 1 (reprise LF auto) + l'axe 2 (utilisation substrat DDR5) seuls soutiennent un résultat opérationnel 2026 de ₩70–90 Mds et un ratio cap/RO de \~16–21× — un cas autonome défendable. La clôture à 86 000 a partiellement intégré l'axe 3, de sorte qu'un échec pourrait ramener le titre vers \~70 000 — mais la société elle-même ne requiert pas l'axe 3 pour être solvable.

**Q : Quel est le meilleur moment pour renforcer ?**
R : Trois combinaisons permettent de qualifier la thèse de « confirmée » plutôt que de « déjà intégrée dans les cours » :

1. **Marge opérationnelle 2T26 ≥ 10 %** + mention de la qualification heat slug,
2. **Communication de nouveaux CAPEX ou d'une conversion de ligne** au 2T–3T26,
3. **Nouvelle ligne de revenus au 3T26.**

La convergence de deux de ces trois critères est suffisante pour faire passer la position de « watchlist / pilote » à « position core ».

---

*Cet article est publié à des fins de recherche et d'information uniquement et ne constitue pas un conseil en investissement. Tous les chiffres sont issus des documents IR de la société, des rapports sell-side (Kyobo, SK, iM, KB, Meritz, Samsung Securities) et d'études de marché tierces. Les désignations anonymes de clients suivent les conventions des rapports sell-side ; les noms réels de clients, les volumes de commandes et les conditions tarifaires n'ont pas été vérifiés publiquement. Avant toute décision d'investissement, consultez directement les documents IR de la société, le dernier rapport trimestriel et les documents réglementaires applicables.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
