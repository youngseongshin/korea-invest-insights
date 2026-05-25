---
title: "OpenEdges Technology (394280) — L'alpha coté en Corée le plus direct sur la conversion de la LPDDR en mémoire pour serveurs d'inférence IA"
slug: openedges-lpddr-datacenter-ip-alpha-thesis-2026-04-30
date: 2026-04-30T22:00:00+09:00
description: "Le lancement de SOCAMM2 par Samsung, la mise en production de masse du SOCAMM2 192 Go par SK hynix pour la plateforme NVIDIA Vera Rubin, et la standardisation JEDEC du LPDDR6 SOCAMM2 / LPDDR6 PIM redéfinissent collectivement la LPDDR — d'une mémoire mobile vers une mémoire pour serveurs d'inférence IA. L'alpha coté le plus direct sur ce changement de catégorie est OpenEdges Technology (394280), qui intègre le Memory Controller LPDDR6 / LPDDR5X, le PHY et le NoC IP — le goulot d'étranglement que tout SoC d'inférence IA doit franchir pour connecter une mémoire de type SOCAMM2. Le vrai fossé concurrentiel n'est pas « sans alternative » mais repose sur quatre avantages précis : validation silicium LPDDR5X sur Samsung Foundry SF5A, statut de partenaire Sub-Licencié SAFE, bundle intégré Controller + PHY + NoC, et la niche de production des AI ASIC asiatiques."
categories: ["Company-Deep-Dive", "Korea Market"]
tags:
  - "OpenEdges Technology"
  - "394280"
  - "LPDDR6"
  - "LPDDR5X"
  - "SOCAMM2"
  - "inférence IA"
  - "IP sous-système mémoire"
  - "Samsung Foundry"
  - "AI ASIC"
  - "actions coréennes"
  - "KOSDAQ"
  - "IP semi-conducteur"
  - "Cadence"
  - "Synopsys"
series: ["semiscope-2026"]
---

> 🔗 <strong>À lire aussi — série OpenEdges</strong> : [OpenEdges Technology : la plateforme IP mémoire coréenne et l'option royalties (25 avril)](/post/semiscope-openedges-technology-ip-platform-2026-04-25/)

> 📚 <strong>Série LPDDR Data-Center — épisode 1/N</strong> : Ce billet ouvre un sous-fil à l'intérieur de la série SemiScope, dédié au suivi du pivot LPDDR vers les serveurs d'inférence IA en tant que source d'alpha sur l'IP mémoire. Les prochains billets suivront les résultats trimestriels, les nouvelles licences LPDDR6/5X, et l'avancement de la validation silicium sur Samsung Foundry.

*Ce billet répond simultanément à trois questions : (1) le thème LPDDR-vers-data-center est-il réel, (2) pourquoi OpenEdges Technology (394280) est-il l'alpha coté coréen le plus direct, et (3) quel est précisément le fossé concurrentiel, une fois qu'on cesse de prétendre qu'il n'existe « aucune alternative » ?*

---

## Synthèse

- <strong>Le thème LPDDR-dans-le-data-center est réel.</strong> Samsung a lancé SOCAMM2 comme module de mémoire serveur IA basé sur LPDDR5X. SK hynix a annoncé la mise en production de masse du SOCAMM2 192 Go à base de LPDDR5X 1c le 20 avril, optimisé pour la plateforme NVIDIA Vera Rubin. JEDEC développe activement le <strong>LPDDR6 SOCAMM2</strong> (standard module serveur) et le <strong>LPDDR6 PIM</strong> (standard PIM pour data-center et calcul accéléré). La LPDDR n'est plus « seulement une mémoire mobile ».
- <strong>OpenEdges Technology (394280) est l'alpha coté coréen le plus direct sur ce changement de catégorie.</strong> Samsung et SK hynix vendent les modules. OpenEdges vend l'IP de sous-système mémoire (Memory Controller + PHY + NoC) que les SoC d'inférence IA *doivent impérativement traverser* pour connecter une mémoire de type SOCAMM2. Position différente dans la pile, mécanique de P&L différente, architecture de multiple différente.
- <strong>Le cadre honnête n'est pas « sans alternative ».</strong> Cadence, Synopsys, Innosilicon, M31 et Rambus sont tous en concurrence sur le Controller + PHY LPDDR6/5X. Synopsys est lui-même partenaire IP SAFE de Samsung Foundry. Le vrai fossé d'OpenEdges repose sur quatre avantages précis : <strong>validation silicium LPDDR5X sur Samsung SF5A</strong>, <strong>statut de partenaire Sub-Licencié SAFE</strong>, <strong>bundle intégré Controller + PHY + NoC</strong>, et <strong>la niche des AI ASIC 4–12 nm sur Samsung Foundry en Asie, que les majors mondiaux de l'IP ne ciblent pas activement</strong>.
- <strong>La valorisation intègre déjà une part significative de l'optionnalité.</strong> Référence au 30 avril : capitalisation boursière ~₩538,8 Mds ; chiffre d'affaires 2025A ₩16,06 Mds → PSR ~33,6× ; PSR 2026E ~16,9× ; PSR 2027E ~10,6× (estimations Yuanta). La question n'est pas de savoir si l'action est « bon marché » — c'est de savoir si la prochaine phase du cadre (validation client, validation fonderie, validation financière) se concrétise assez vite pour justifier un multiple qui est déjà un multiple de re-rating.

---

## 1. La question centrale du re-rating — décomposée

Trois niveaux que toute analyse de ce nom doit traiter séparément :

| Question | Statut au 30 avril |
| --- | --- |
| <strong>La LPDDR migre-t-elle vers le data-center ?</strong> | Oui — Samsung SOCAMM2 (basé LPDDR5X, +70 % d'efficacité énergétique vs DDR5 RDIMM, jusqu'à 153,6 GB/s par module), mise en production de masse du SOCAMM2 192 Go de SK hynix pour NVIDIA Vera Rubin, et standardisation JEDEC du LPDDR6 SOCAMM2 + LPDDR6 PIM. |
| <strong>Qui est l'alpha coté coréen le plus direct ?</strong> | OpenEdges Technology — Controller + PHY + NoC IP LPDDR6 / LPDDR5X intégrés ; LPDDR5X 8 533 Mbps validé silicium sur SF5A ; première licence LPDDR6/5X annoncée en avril 2026. |
| <strong>Quel est le régime de multiple aujourd'hui ?</strong> | PSR ~33,6× sur le chiffre d'affaires 2025A. La valorisation est tournée vers l'avenir — elle exige des gains clients, des références de fonderie et une progression trimestrielle du chiffre d'affaires pour se justifier. |

<strong>En une phrase :</strong> le thème est réel, l'alpha coté coréen le plus direct est OpenEdges, et l'action entre désormais dans une phase de « vérification du cadre » plutôt que de découverte.

---

## 2. Le thème LPDDR-vers-data-center — plus seulement du mobile

### 2.1 Samsung SOCAMM2 — la LPDDR entre dans le serveur

Samsung a introduit SOCAMM2 comme <strong>module de mémoire serveur IA de nouvelle génération basé sur LPDDR5X</strong> :

| Spécification | SOCAMM2 (Samsung) | Versus DDR5 RDIMM |
| --- | --- | --- |
| Mémoire sous-jacente | LPDDR5X | — |
| Efficacité énergétique | — | <strong>+70 %</strong> d'amélioration |
| Bande passante par module | jusqu'à <strong>153,6 GB/s</strong> | jusqu'à <strong>2,6×</strong> |

L'implication est directe. <strong>Les serveurs d'inférence IA ne tariffent plus « la performance à tout prix » — ils tariffent l'efficacité énergétique et le TCO.</strong> La LPDDR entre dans le serveur à cause des factures d'électricité et des coûts de refroidissement.

### 2.2 SK hynix — la LPDDR5X 1c 192 Go SOCAMM2 entre en production de masse

SK hynix a annoncé le 20 avril la <strong>mise en production de masse du SOCAMM2 192 Go à base de LPDDR5X 1c</strong>, optimisé pour la plateforme NVIDIA Vera Rubin. L'annonce citait une bande passante >2× et une amélioration de l'efficacité énergétique >75 % par rapport au RDIMM.

L'expression qui compte est « production de masse ». À partir de ce moment, la LPDDR comme mémoire serveur n'est plus une thèse — c'est du chiffre d'affaires.

### 2.3 JEDEC — la standardisation nomme explicitement le data-center

JEDEC a indiqué que les prochaines mises à jour de la LPDDR6 ciblent <strong>certaines charges de travail data-center et calcul accéléré</strong> au-delà du mobile, avec deux standards en développement actif :

- <strong>LPDDR6 SOCAMM2</strong> — standard de module serveur
- <strong>LPDDR6 PIM</strong> — standard Processing-In-Memory pour les charges d'inférence edge et data-center

C'est la première fois que l'organisme de standardisation nomme explicitement « data center » dans la feuille de route LPDDR. Cela fait passer le thème d'une communication marketing mono-fournisseur à une <strong>redéfinition des standards à l'échelle de l'industrie</strong>.

### 2.4 Trois signaux, une même direction

```
Samsung (lancement SOCAMM2) + SK hynix (production de masse) + JEDEC (standardisation)
        ↓
Trois vecteurs indépendants pointent tous : LPDDR → data-center
        ↓
Il s'agit d'un cycle industriel, pas d'un récit mono-fournisseur
```

L'énoncé correct du thème est précis :

> <strong>Pas une substitution à la HBM — la LPDDR se propage à côté du CPU et à côté de l'accélérateur dans les serveurs d'inférence IA, en tant que niveau de mémoire basse consommation et haute bande passante.</strong>

Cette précision compte. C'est *dans* cette définition qu'OpenEdges devient un candidat alpha de premier plan.

---

## 3. La position d'OpenEdges — pourquoi c'est l'alpha coté coréen le plus direct

### 3.1 Ce que « société IP » signifie concrètement ici

OpenEdges vend de l'<strong>IP de sous-système mémoire</strong>. Elle ne fabrique pas de puces. Tout concepteur fabless de SoC d'inférence IA qui souhaite connecter une mémoire de type LPDDR a besoin de trois blocs IP :

```
Le SoC doit communiquer avec la mémoire LPDDR →
  ① Memory Controller (ordonnancement des commandes, ECC, QoS)
  ② DDR PHY (la signalisation électrique effective)
  ③ Interconnexion NoC (chemin de données à l'intérieur du SoC)
```

OpenEdges est la seule maison IP coréenne qui possède et intègre <strong>les trois</strong>.

### 3.2 L'insight décisif — les modules vs. « l'IP qui connecte les modules »

Cartographier la chaîne de valeur LPDDR-data-center rend la position d'OpenEdges explicite :

```
Demande des serveurs d'inférence IA
     ↓
Prolifération des mémoires serveurs SOCAMM2 / LPDDR5X·6   ← Samsung, SK hynix
     ↓
Conception accrue de CPU / NPU / ASIC sur mesure IA        ← Gaonchips, ASICs captifs
     ↓
Memory Controller / PHY / NoC interne au SoC nécessaire    ← créneau d'OpenEdges
     ↓
IP OpenEdges licenciée → revenus de licence + royalties post-production
```

Le cadre est net : <strong>Samsung et SK hynix vendent les modules. OpenEdges vend l'IP qui permet à un SoC de se connecter à ces modules.</strong> Position différente dans la chaîne de valeur, comptabilité différente, et architecture de multiple différente.

### 3.3 Validation technologique — validé silicium, pas seulement sur une feuille de route

État des validations annoncées :

| Procédé | IP | Performance | Statut |
| --- | --- | --- | --- |
| Samsung SF5A | LPDDR5X Combo PHY | 8 533 Mbps (largeur de données 16/32 bits) | <strong>validé silicium</strong> |
| Samsung 4 nm | LPDDR6 / LPDDR5X | LPDDR6 14,4 Gbps, LPDDR5X 10,7 Gbps | en développement |
| Samsung 5/8 nm, TSMC 6/7/12/16 nm | PHY LPDDR6/5X/5 | — | couvre les marchés de volume en production |

« Validé silicium » a une signification précise : <strong>le client ne porte plus le risque de tape-out</strong> sur cet IP à ce nœud. Pour une maison AI ASIC fabless, une IP déjà en production au nœud cible l'emporte sur une IP théoriquement plus rapide qui n'a pas encore été validée silicium au même nœud.

### 3.4 La première licence LPDDR6/5X — le thème entre en phase de commercialisation

OpenEdges a annoncé le <strong>premier accord de licence pour un IP de sous-système mémoire supportant simultanément LPDDR6 et LPDDR5X</strong> le 9 avril 2026. La société a encadré cette victoire dans le contexte de l'expansion des charges de travail IA vers l'automobile, la robotique et les plateformes edge-server — où les designs SoC se heurtent au mur mémoire, et les architectures basées sur LPDDR6 s'accélèrent en réponse.

La hiérarchie de signaux que cela crée :

- <strong>Première licence</strong> = signal « la technologie est commercialisable ».
- <strong>Deuxième et troisième licences</strong> = signal « un marché se forme ».
- <strong>Royalties post-production</strong> = signal « c'est une société d'IP plateforme » — déclencheur du changement de régime de multiple.

Au 30 avril, on se situe juste après le premier signal. Les deux suivants sont ce que le cadre doit désormais imprimer.

---

## 4. Le fossé honnête — pas « sans alternative », quatre avantages précis

C'est la section que le récit consensuel se trompe le plus souvent. Le raccourci « aucune alternative en Corée → potentiel de monopole » saute deux étapes importantes et finit par surestimer la défensabilité. Le fossé réel est plus étroit et, en fait, *plus utile* pour suivre la thèse.

### 4.1 Le paysage concurrentiel mondial est lourd

Sur le Controller + PHY LPDDR6/5X :

| Concurrent | Directness | Niveau de menace | Terrain de bataille |
| --- | --- | --- | --- |
| <strong>Cadence</strong> | Très élevée | Très élevé | PHY+Controller LPDDR6/5X 14,4 Gbps, positionné infrastructure IA, framework chiplet |
| <strong>Synopsys</strong> | Très élevée | Très élevé | Controller+PHY LPDDR6/5X, support SOCAMM / LPCAMM2, ECC / Link ECC / chiffrement inline |
| <strong>Innosilicon</strong> | Élevée | Élevé (Chine notamment) | PHY Combo LPDDR6/5X, 14,4 Gbps ; vent porteur de la politique d'approvisionnement domestique en Chine |
| <strong>M31</strong> | Moyen-élevé | Moyen-élevé | LPDDR5/5X/5T, écosystème TSMC |
| <strong>Rambus</strong> | Moyen | Moyen | Controller LPDDR5T / 5X / 5 |
| <strong>Arteris</strong> | Partielle (NoC seulement) | Élevé | Interconnexion NoC ; AMD a adopté Arteris pour ses prochains chiplets IA |

Deux points méritent une attention particulière.

<strong>Cadence</strong> a annoncé en juillet 2025 un tape-out de solution système d'IP mémoire LPDDR6/5X 14,4 Gbps, explicitement cadré pour « l'infrastructure IA de nouvelle génération », avec plusieurs engagements clients IA / HPC / data-center en cours.

<strong>Synopsys</strong>, depuis 2023, élargit sa coopération avec Samsung Foundry sur un portefeuille IP SF8LPU / SF5 / SF4 / SF3 incluant LPDDR / DDR / PCIe / UCIe — ce qui signifie que <strong>Synopsys est déjà à l'intérieur de Samsung Foundry</strong>.

La mauvaise façon d'énoncer la thèse est donc :

> ❌ « Il n'existe pas d'IP LPDDR comme OpenEdges à l'intérieur de Samsung Foundry, donc potentiel de monopole. »

Ce n'est pas ce que reflète la liste des partenaires IP SAFE.

### 4.2 Même chez Samsung, des alternatives existent couche par couche

Poser la question avec précision change la réponse :

| Angle | Substitut interne à Samsung ? | Lecture |
| --- | --- | --- |
| Les SoC propres de Samsung (Exynos, etc.) | <strong>Probablement oui</strong> | System LSI dispose de groupes de conception internes pour processeurs / modems / capteurs d'image ; une capacité Controller / PHY LPDDR interne est presque certainement présente, même si elle n'est jamais vendue en externe. |
| Clients externes de Samsung Foundry | <strong>L'IP SAFE externe est le vrai ensemble de substituts</strong> | OpenEdges, Cadence, Synopsys, Innosilicon, M31, Rambus figurent tous sur la liste des partenaires IP SAFE. |
| Division mémoire de Samsung | <strong>Pas un substitut</strong> | LPDDR / SOCAMM2 sont des modules DRAM — une couche différente du Controller / PHY d'OpenEdges. |

La troisième ligne est décisive. <strong>Le SOCAMM2 de Samsung Memory n'est pas le concurrent d'OpenEdges — c'est l'amont qui fait croître la demande pour OpenEdges.</strong> Toute puce qui veut se connecter à SOCAMM2 a besoin d'un Controller / PHY à l'intérieur du SoC.

### 4.3 Alors quel est le *vrai* fossé ?

Exprimé de façon étroite — et donc traçable — le fossé repose sur quatre avantages :

<strong>Avantage 1 — Validation sur le procédé Samsung Foundry.</strong> PHY LPDDR5X validé silicium sur SF5A. Les clients fabless préfèrent structurellement « a déjà tourné dans notre nœud cible » à « l'IP la plus rapide sur un slide ».

<strong>Avantage 2 — Statut de partenaire Sub-Licencié.</strong> Dans le programme SAFE de Samsung, OpenEdges ne figure pas seulement sur la liste des partenaires IP mais aussi sur la liste des partenaires Sub-Licenciés. Ce statut implique une profondeur d'engagement — modification IP, support technique, et accompagnement au démarrage de production lors du développement de la puce cliente. Pour les maisons fabless de taille intermédiaire, cette profondeur est un différenciateur.

<strong>Avantage 3 — Bundle intégré Controller + PHY + NoC.</strong> Cadence et Synopsys sont forts sur Controller+PHY ; Arteris est la référence standalone sur le NoC. OpenEdges intègre les trois sous un même toit. Pour certains clients, le temps de vérification intégrée économisé l'emporte sur le prix unitaire.

<strong>Avantage 4 — La niche des AI ASIC d'inférence sur Samsung Foundry 4–12 nm.</strong> Cadence et Synopsys se concentrent largement sur les hyperscalers mondiaux et les nœuds à la pointe. Le coin d'OpenEdges est précisément <strong>les SoC d'inférence IA de taille intermédiaire sur les procédés de volume 4 / 5 / 8 / 12 nm de Samsung Foundry, plus les clients fabless coréens / japonais / asiatiques, plus la rapidité de mise en production, plus des tarifs compétitifs</strong>.

L'énoncé honnête du fossé en une ligne :

> <strong>La thèse d'OpenEdges n'est pas « nous battons Cadence et Synopsys ». C'est « nous devenons l'IP standard dans le segment que Cadence et Synopsys ne ciblent pas activement ».</strong>

C'est une thèse plus défendable — et c'est celle que les jalons du cadre testent réellement.

---

## 5. La progression du cadre en quatre phases (grille d'observation)

L'action passe de « société IP pour IA on-device » à « société IP goulot d'étranglement mémoire pour SoC d'inférence IA » à travers quatre phases d'évidence, pas un seul événement médiatique.

### 5.1 Phase 1 — Validation du thème industriel (acquise)

- Lancement du SOCAMM2 Samsung ✓
- Mise en production de masse du SOCAMM2 192 Go SK hynix ✓
- Standardisation JEDEC LPDDR6 SOCAMM2 / PIM en développement ✓

<strong>État :</strong> complet. C'est la couche que le marché a déjà digérée.

### 5.2 Phase 2 — Validation client (tout juste débutée)

L'observation décisive ici n'est *pas* la première licence. Ce sont les <strong>deuxième et troisième licences</strong>, et le libellé à l'intérieur de l'annonce.

| Formulation dans l'annonce | Lecture du marché |
| --- | --- |
| « Première licence IP LPDDR6/5X » | commercialisation précoce (actuel) |
| « Licence de suivi client SoC IA / HPC » | connexion data-center en formation |
| « Client edge server / accélérateur d'inférence / ASIC sur mesure » | pas une IP mobile — une IP d'inférence IA |
| « Engagements de suivi multi-clients » | possible standardisation, pas du one-off |
| « Design en production avec royalties » | régime IP plateforme — re-rating du multiple |

Le prochain point de vérification trimestriel est de savoir si les annonces introduisent des formulations comme « suivi SoC IA/HPC » ou « edge-server ».

### 5.3 Phase 3 — Validation par la fonderie

Hiérarchie des signaux :

| Force | Événement |
| --- | --- |
| <strong>S</strong> | IP LPDDR6/5X d'OpenEdges ajoutée au flux SAFE ou de référence design-house de Samsung Foundry |
| A | Annonce de validation silicium LPDDR6/5X sur Samsung SF4 / SF5 / SF8 |
| A | Victoire sur un SoC IA turnkey auprès d'une design-house nationale ou internationale sélectionnant l'IP OpenEdges |
| B | Montée du nombre de clients Samsung Foundry se traduisant par une hausse des licences OpenEdges |
| C | Récit générique « bénéficiaire de Samsung Foundry » |

La signification du signal de niveau S est directe : <strong>le marché commence à reconnaître que « utiliser cette IP permet de mettre en production un SoC d'inférence IA rapidement sur Samsung Foundry ».</strong>

### 5.4 Phase 4 — Validation par les chiffres

Le compte de résultat est le filtre final.

| Indicateur | Signification |
| --- | --- |
| Revenus de licence IP sous-système mémoire en hausse | Adoption croissante par les SoC clients |
| Part croissante des contrats serveur / stockage / AI-HPC | Pas du mobile / industriel — connecté au data-center |
| Hausse des passifs contractuels / revenus différés | Carnet de commandes reconnu en avance en croissance |
| <strong>Hausse des revenus de royalties</strong> | <strong>Puces clients entrant en production — déclencheur du changement de régime de multiple</strong> |
| Annonces de contrats à achat unique / d'approvisionnement | La taille des commandes devient vérifiable par le marché |

<strong>Les royalties sont décisives.</strong> Les revenus de licence sont ponctuels. Les royalties se répètent à chaque expédition de puce cliente. Les revenus de royalties 2025A s'élevaient à <strong>₩102 millions</strong> — faibles. Un passage trimestriel des royalties au-dessus de ~₩1,0 Md marquerait le changement de régime.

---

## 6. Valorisation — déjà un multiple de re-rating

### 6.1 Instantané actuel

```
Prix de référence       = ₩20 450
Capitalisation boursière = ~₩538,8 Mds
Chiffre d'affaires 2025A = ₩16,06 Mds
  - Licences            = ₩10,86 Mds (67,6 %)
  - Maintenance         = ₩4,20 Mds (26,1 %)
  - Royalties           = ₩0,10 Md (0,6 %)
Perte opérationnelle 2025A = ₩28,91 Mds (marge opérationnelle -180 %)
R&D 2025A               = ₩37,05 Mds (R&D / CA = 230 %)
```

La R&D à 2,3× du chiffre d'affaires résume le stade de la société en un seul chiffre. <strong>Il s'agit d'une phase d'investissement R&D pré-levier.</strong> L'inflexion de levier opérationnel n'interviendra que lorsque le chiffre d'affaires atteindra la classe ~₩30–50 Mds.

### 6.2 Multiples PSR

```
PSR 2025A = ₩538,8 Mds / ₩16,06 Mds = 33,55× ≈ 33,6×
PSR 2026E = ₩538,8 Mds / ₩31,8 Mds  = 16,94× ≈ 16,9×
PSR 2027E = ₩538,8 Mds / ₩51,0 Mds  = 10,56× ≈ 10,6×
```

(Chiffre d'affaires 2026E / 2027E selon les estimations Yuanta : ₩31,8 Mds et ₩51,0 Mds.)

<strong>Vérification arithmétique :</strong> atteindre le chiffre d'affaires 2026E de ₩31,8 Mds exige un chiffre d'affaires trimestriel moyen de ₩7,95 Mds. Un T1 faible impose alors une accélération plus marquée au second semestre.

L'objectif de référence de Yuanta (₩28 000) utilisait le chiffre d'affaires 2027E avec un PSR cible de ~15,5×. Par rapport au prix de référence :

```
Potentiel de hausse vers ₩28 000 = (28 000 − 20 450) / 20 450 = 36,9 %
```

### 6.3 Lire le multiple honnêtement

Un PSR de 33,6× n'est pas un « multiple bon marché ». Mais les re-ratings des sociétés IP passent rarement par une compression du PER. Ils passent par <strong>une montée en puissance du chiffre d'affaires sur une petite base, tandis que licences, royalties et nombre de clients s'élargissent simultanément, ce qui fait mécaniquement baisser le PSR forward même à capitalisation boursière inchangée</strong>.

```
Si le cadre s'imprime :
  CA ↑ → dénominateur PSR ↑ → PSR forward baisse automatiquement
  Royalties ↑ → le régime de multiple lui-même se déplace (IP-licence → IP-plateforme)
```

Le multiple effectue donc un travail analytique utile : <strong>il tarifie le chemin, et ce chemin exige des jalons spécifiques — que les Phases 2, 3 et 4 du cadre sont conçues pour suivre</strong>.

---

## 7. Référence croisée — la pile LPDDR-vers-data-center coréenne cotée

À titre cartographique — sans connotation de recommandation — les expositions coréennes cotées se regroupent ainsi :

| Couche | Société cotée | Fonction dans la pile | Directness |
| --- | --- | --- | --- |
| <strong>IP sous-système mémoire</strong> | <strong>OpenEdges Technology (394280)</strong> | Controller + PHY + NoC LPDDR6/5X | Élevée |
| Module mémoire / DRAM | SK hynix | SOCAMM2 / mémoire serveur LPDDR | Élevée |
| Mémoire + fonderie | Samsung Electronics | SOCAMM2 + procédé Samsung Foundry | Élevée |
| Service de design fonderie | Gaonchips | Productisation AI ASIC Samsung Foundry | Moyen-élevé |
| IP interface haute vitesse | Qualitas Semiconductor | IP PCIe / UCIe / SerDes | Moyen |
| Fabless LPDDR | Jeju Semiconductor | Fabless LPDDR | Plus faible |
| Panier DSP / service de design | A&D Technology / Coasia | Panier service de design / DSP | Plus faible |

OpenEdges occupe le <strong>créneau IP sous-système mémoire</strong>. Il est complémentaire plutôt que substituable à n'importe laquelle des autres couches — ce qui explique également pourquoi isoler son alpha nécessite le cadre en quatre phases plutôt qu'un encadrement générique « semi IA coréen ».

---

## 8. Contre-argumentation — où la thèse pourrait se briser

### 8.1 Échec macro — ralentissement de l'adoption LPDDR dans les serveurs

La mémoire serveur est conservatrice : RAS, stabilité de service, conception thermique et qualification de la chaîne d'approvisionnement comptent tous. Si DDR5 RDIMM, CXL, HBM et les dérivés GDDR maintiennent leurs positions, la pénétration du LPDDR6 dans le data-center pourrait être plus lente que le lancement SOCAMM2 ne le laisse entendre. SOCAMM2 lui-même peut survivre sans devenir un « standard général de serveur », restant un niveau lié à la plateforme NVIDIA plutôt qu'un standard universel.

### 8.2 Échec micro — SOCAMM2 croît mais ne se connecte pas à OpenEdges

Même avec SOCAMM2 en expansion, les revenus d'OpenEdges ne suivront pas si les SoC IA qui s'y connectent choisissent :

- L'IP Synopsys / Cadence / ARM-ecosystem
- Un PHY / Controller captif conçu en interne par le client
- Innosilicon (clients chinois) / M31 (clients TSMC / Taïwan)

Un discours solide sur les procédés de volume 4–8 nm de Samsung Foundry ne suffit pas ; <strong>sans tape-out clients confirmés et royalties post-production, le changement de régime ne peut pas se maintenir</strong>.

### 8.3 Zones d'information non confirmée

> <strong>Note de confiance.</strong> Les seules annonces publiques ne permettent pas encore de déterminer si le premier client de licence LPDDR6/5X d'OpenEdges est un vrai SoC d'inférence data-center, ou un SoC mobile / automobile / robotique / industriel. Chemins de vérification : (1) annonces de contrat à fournisseur unique sur DART, (2) notes sur les segments de revenus / passifs contractuels / royalties dans les dépôts trimestriels, (3) commentaires sur la segmentation client lors des conférences IR. La lecture intérimaire honnête est : <strong>la connexion data-center doit être traitée comme valeur optionnelle, la validation par le cadre (gains de suivi + progression trimestrielle du CA) constituant la véritable porte de confirmation.</strong>

---

## 9. La synthèse en un cadre

OpenEdges Technology est <strong>l'alpha coté coréen le plus direct sur la redéfinition de la LPDDR en mémoire pour serveurs d'inférence IA.</strong> Plus petite que Samsung et SK hynix ; plus proche du goulot d'étranglement SoC que Jeju Semiconductor ; meilleure architecture de marges IP que Gaonchips.

La façon la plus claire de suivre l'action est de tracer la <strong>progression en quatre phases</strong> plutôt que tout niveau de prix unique : validation du thème industriel (largement acquise), validation client (tout juste débutée), validation par la fonderie (l'observation à fort levier au second semestre 2026), et validation par les chiffres (le compte de résultat convertissant le cadre en multiple).

La valorisation reflète déjà une part significative de l'optionnalité. C'est une caractéristique, pas un défaut — cela signifie simplement que l'action doit désormais *imprimer* le cadre plutôt que le revendiquer. Chaque nouvelle annonce de licence mentionnant « SoC IA / HPC » ou « edge-server » ; chaque inclusion dans le flux de référence de Samsung Foundry ; chaque progression significative des royalties trimestrielles — ce sont les événements qui font passer le régime de « IP-licence » à « IP-plateforme ».

Le prochain billet de ce sous-fil LPDDR data-center paraîtra lorsque (1) les résultats trimestriels 1S26 seront publiés, (2) des annonces de licences LPDDR6/5X de suivi auront été faites, et (3) la progression de la validation silicium de Samsung Foundry sur SF4 / SF5 / SF8 sera confirmable.

---

## Annexe — Niveaux d'évidence

### [Fait]

- Samsung a lancé SOCAMM2 comme module de mémoire serveur IA basé sur LPDDR5X, avec une efficacité énergétique déclarée +70 % vs DDR5 RDIMM et jusqu'à 153,6 GB/s par module.
- SK hynix a annoncé la mise en production de masse du SOCAMM2 192 Go à base de LPDDR5X 1c le 20 avril 2026, optimisé pour NVIDIA Vera Rubin.
- JEDEC développe les standards LPDDR6 SOCAMM2 (module serveur) et LPDDR6 PIM (data-center / calcul accéléré).
- OpenEdges intègre le Memory Controller LPDDR6 / LPDDR5X, le DDR PHY et le NoC IP sous un même toit.
- Le PHY Combo LPDDR5X sur Samsung SF5A à 8 533 Mbps est validé silicium selon les annonces d'OpenEdges.
- OpenEdges a annoncé le premier accord de licence d'IP de sous-système mémoire supportant LPDDR6/5X le 9 avril 2026.
- Chiffre d'affaires 2025A ₩16,06 Mds (Licences ₩10,86 Mds / Maintenance ₩4,20 Mds / Royalties ₩0,10 Md) ; perte opérationnelle 2025A ₩28,91 Mds ; R&D 2025A ₩37,05 Mds.
- Cadre d'estimations Yuanta : CA 2026E ₩31,8 Mds, CA 2027E ₩51,0 Mds ; objectif de référence ₩28 000 dérivé du CA 2027E × PSR cible ~15,5×.
- Cadence a annoncé en juillet 2025 un tape-out de solution système d'IP mémoire LPDDR6/5X 14,4 Gbps, avec plusieurs engagements clients IA / HPC / data-center.
- Synopsys a annoncé en 2023 un élargissement de sa coopération avec Samsung Foundry sur SF8LPU / SF5 / SF4 / SF3 couvrant les IP LPDDR / DDR / PCIe / UCIe.

### [Inférence]

- La LPDDR devient un niveau de mémoire data-center structurel plutôt qu'un événement mémoire mobile incrémental.
- OpenEdges est la valeur coréenne cotée la plus directement positionnée sur le goulot d'étranglement côté SoC du cycle SOCAMM2 / LPDDR6.
- Le récit de défensabilité est mal formulé sous « aucune alternative ». Un cadre plus précis est : « devient l'IP standard dans la niche que les majors mondiaux ne ciblent pas activement ».
- La valorisation est déjà un multiple de re-rating ; les jalons du cadre (client / fonderie / chiffres) sont les éléments déclencheurs permettant au multiple de se compoundre plutôt que de se comprimer.

### [Spéculation]

- Des annonces de licences LPDDR6/5X de suivi nommant des clients SoC IA / HPC ou edge-server pourraient se matérialiser en 2026.
- Une inclusion dans le flux de référence de Samsung Foundry sur SF4 / SF5 / SF8 déplacerait le régime de IP-licence à IP-plateforme.
- Un passage des royalties trimestrielles au-dessus de ~₩1,0 Md marquerait le début du changement de régime du multiple.

### [Bloqué]

- Si le premier client de licence LPDDR6/5X d'OpenEdges est un SoC d'inférence data-center ou un SoC mobile / automobile / robotique / industriel.
- La profondeur du partenariat IP SAFE de Samsung Foundry sur SF4 / SF5 / SF8 pour la pile LPDDR6/5X d'OpenEdges.
- L'économie des frais de licence par client et les structures de taux de royalties.
- La décomposition détaillée de la marge brute par famille IP (LPDDR vs DDR vs lié HBM vs NoC).

---

<strong>Avertissement</strong> : Ce billet est un commentaire de recherche, pas un conseil en investissement. Les cadres d'estimation sont tirés de documents sell-side accessibles au public (Yuanta) et d'annonces de la société ; leur exactitude dépend de ces sources sous-jacentes. Les tickers cités sont illustratifs pour le cadre, pas des recommandations. Effectuez votre propre due diligence et consultez des conseillers agréés avant toute décision.
