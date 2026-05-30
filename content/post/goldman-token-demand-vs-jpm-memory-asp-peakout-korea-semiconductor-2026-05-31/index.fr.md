---
title: "La demande de tokens de Goldman face au pic d'ASP mémoire de J.P. Morgan : ces deux prévisions s'opposent-elles vraiment ?"
slug: "goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31"
date: 2026-05-31T11:00:00+09:00
description: "Goldman Sachs prévoit que les agents d'IA multiplient par 24 l'usage de tokens d'ici 2030 tandis que le coût par token baisse de 60-70% par an. J.P. Morgan prévoit que la croissance en glissement annuel de l'ASP de la DRAM et du NAND s'essouffle à partir de 2027. En séparant ces deux prévisions apparemment opposées en P, Q et C, un chemin cohérent apparaît : l'alpha bascule du bêta mémoire de 2026 vers une pile de réduction du coût par token après 2027."
categories: ["Korea Market", "Sector-Deep-Dive", "AI Infrastructure"]
tags:
  - "삼성전자"
  - "SK하이닉스"
  - "HBM"
  - "메모리 ASP"
  - "eSSD"
  - "AI 토큰"
  - "추론비용"
  - "Goldman Sachs"
  - "J.P. Morgan"
  - "AI 인프라"
  - "Research OS"
series: ["Korea Market Regime"]
draft: false
---

> Cet article fait suite à [Contrats à terme de tokens IA et coût par token](/fr/post/ai-token-futures-cost-per-token-korea-semiconductor-thesis-2026-05-30/), [Analyse approfondie de Samsung Electronics 2026](/fr/post/kr-deep-dive-samsung-electronics-2026-04-16/), [SK Hynix : le poids lourd du HBM](/fr/post/kr-deep-dive-sk-hynix-2026-04-16/) et [L'infrastructure IA de la Corée après le T1 FY27 de Nvidia](/fr/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/). Là où les articles précédents examinaient séparément le coût par token, les entreprises individuelles et la diffusion de l'infrastructure IA, celui-ci <strong>fusionne deux prévisions différentes — Goldman sur la demande et J.P. Morgan sur le prix de la mémoire — dans un seul cadre</strong> et ordonne l'horizon d'investissement de 2026 à 2030.

## TL;DR

* Goldman Sachs voit <strong>une explosion de l'usage de tokens (24x d'ici 2030) ainsi qu'une chute marquée du coût par token (60-70% par an)</strong>. J.P. Morgan voit <strong>le taux de croissance en glissement annuel (YoY) de l'ASP de la DRAM et du NAND ralentir à partir de 2027</strong>. Comme ils suivent des variables différentes, les deux prévisions ne s'opposent pas frontalement.
* Combinez-les et un chemin unique apparaît : <strong>2026 est le bêta de l'ASP mémoire, 2027 est un pic (peak-out) du momentum des prix, et 2028-2030 est une bascule de l'alpha vers les composants et systèmes qui abaissent le coût par token</strong>.
* La conclusion d'investissement n'est donc pas « acheter de la mémoire sans limite ». En 2026, le bêta mémoire comme le HBM, la DRAM serveur et l'eSSD est favorable, mais ensuite il faut <strong>sélectionner où se trouvent les goulets d'étranglement</strong> : ASIC, réseaux IA, optique, leaders du HBM, eSSD, packaging avancé et MLCC/FC-BGA.
* Les deux malentendus les plus courants sont : (1) voir le peak-out de J.P. Morgan et conclure que « le cycle de l'infrastructure IA est terminé », et (2) voir la demande de Goldman et conclure que « les prix de la mémoire continueront de flamber jusqu'en 2030 ». Les deux vont trop loin.

---

## 1. Deux géants, deux prévisions apparemment opposées

Devant la même ère de l'IA, deux banques d'investissement mondiales ont dressé des tableaux qui semblent pointer dans des directions opposées.

<strong>Goldman Sachs</strong> (article officiel, 5 mai 2026) regarde le côté de la demande. L'essentiel tient en deux points.

- <strong>L'usage de tokens croît de 24x d'ici 2030.</strong> La prévision est que l'usage mensuel atteint 120 millions de milliards (quadrillion) de tokens en 2030 ; à rebours, cela situe la base de 2026 autour de 5 quadrillion. Soit une croissance annuelle moyenne d'environ 121% sur quatre ans.
- En parallèle, <strong>le coût d'inférence par token baisse de 60-70% par an.</strong> Les moteurs en sont l'amélioration de l'efficacité des puces et une meilleure architecture des centres de données.

![Indice reconstitué de l'économie des tokens IA de Goldman Sachs — l'usage monte de 24x tandis que le coût par token baisse de 39-123x](goldman-ai-token-economics-reconstructed-index.png)

<small>Source : un graphique reconstitué qui se contente d'indexer les chiffres de l'article officiel de Goldman Sachs (2026-05-05). Ce n'est pas le graphique original, mais les chiffres originaux — « 24x tokens d'ici 2030, coût par token en baisse de 60-70% par an » — reportés sur une échelle logarithmique.</small>

Dans le graphique ci-dessus, la ligne bleue (usage) monte fortement, et les lignes orange et verte (coût par token) descendent encore plus fortement. À une baisse annuelle de 60%, le coût quatre ans plus tard est d'environ 2,6% du niveau de 2026 (une amélioration d'environ 39x) ; à 70%, environ 0,8% (une amélioration d'environ 123x).

À l'inverse, le matériel de <strong>J.P. Morgan</strong> regarde le prix. Le tableau est que l'ASP de la DRAM et du NAND monte fortement en 2026 mais que, <strong>de la fin 2026 au début 2027, le taux de croissance en glissement annuel décélère rapidement.</strong>

![Variation en glissement annuel de l'ASP de la DRAM et du NAND selon J.P. Morgan — pic en 2026 et ralentissement à partir de 2027](jpm-dram-nand-asp-yoy-peakout-chart.png)

<small>Source : image téléversée en session (DRAM d'après WSTS / J.P. Morgan estimates, NAND d'après Gartner / J.P. Morgan estimates). Les chiffres détaillés tels que FY26 DRAM +53% et NAND +30%, FY27 DRAM +1% et NAND -6% reposent sur un résumé secondaire ; le tableau original n'est pas vérifié.</small>

En surface, « la demande explose » (Goldman) et « la hausse des prix de la mémoire s'essouffle » (J.P. Morgan) semblent s'opposer. Mais en y regardant de près, les deux prévisions <strong>parlent de choses différentes.</strong>

---

## 2. Pourquoi ce n'est pas une opposition — séparer P, Q et C

Le profit d'une entreprise de mémoire se décompose en une simple multiplication.

> Chiffre d'affaires = volumes (Q) × prix de vente moyen (P), et l'économie des tokens = usage (Q) × coût par token (C).

À travers ce prisme, il devient clair que les deux prévisions surveillent des variables différentes.

| Dimension | Goldman Sachs | J.P. Morgan |
|---|---|---|
| Variable suivie | Usage de tokens (Q), coût par token (C) | Variation YoY de l'ASP DRAM/NAND (momentum de P) |
| Message central | L'usage de l'IA explose à long terme, le coût par token plonge | Le taux de hausse du prix de la mémoire ralentit à partir de 2027 |
| Horizon temporel | 2026-2030 | Fin 2026 à début 2027 |

Il y a ici un piège à signaler. <strong>L'axe vertical du graphique de J.P. Morgan n'est pas le niveau absolu du prix, mais le « taux de croissance en glissement annuel (YoY %) ».</strong> Les deux sont totalement différents.

Prenons un exemple.

| Moment | Indice d'ASP | YoY |
|---|---:|---:|
| T4 25 | 100 | – |
| T4 26 | 300 | +200% |
| T4 27 | 315 | +5% |

Du T4 26 au T4 27, l'indice de prix <strong>monte encore</strong>, de 300 à 315. Pourtant le taux de croissance en glissement annuel plonge de +200% à +5%. Autrement dit, le « peak-out » de 2027 de J.P. Morgan peut ne pas signifier que les prix s'effondrent, mais que <strong>le rythme de la hausse ralentit.</strong> Le marché boursier intègre d'ordinaire cette <strong>direction du taux de croissance</strong> avant le « bénéfice record » lui-même. C'est pourquoi le cours peut se refroidir d'abord, juste au moment où le bénéfice est à son sommet.

En résumé, Goldman surveille <strong>Q (usage) et C (coût)</strong>, tandis que J.P. Morgan surveille <strong>le rythme de P (prix).</strong> Comme ce sont des variables différentes, les deux peuvent avoir raison en même temps.

---

## 3. Le coût total d'inférence peut même baisser

Ici surgit une conclusion contre-intuitive. Même si l'usage croît de 24x, si le coût par token baisse de 60-70% par an, alors <strong>la charge totale du coût d'inférence pourrait même être inférieure à celle de 2026.</strong>

C'est de l'arithmétique simple. En supposant la même composition de tokens et la même complexité de modèle, le coût total en 2030 est l'indice d'usage × l'indice de coût par token.

- À une baisse annuelle de 60% : 24 × 2,6% ≈ <strong>61% de 2026</strong>
- À une baisse annuelle de 70% : 24 × 0,8% ≈ <strong>19% de 2026</strong>

![Charge totale du coût d'inférence, sensibilité simple — même 24x d'usage est absorbé par la forte baisse du coût par token](goldman-total-inference-cost-burden-index.png)

<small>Il s'agit d'un calcul de sensibilité très simplifié. Il ne reflète pas la composition des tokens, la taille du modèle, la longueur du contexte, la hausse des tokens de raisonnement (reasoning), la multimodalité, le traitement redondant, les contraintes de latence ni les goulets de bande passante mémoire. En pratique, ces facteurs pourraient repousser le coût à la hausse.</small>

Ce graphique est le cœur de la logique de Goldman. <strong>Celui qui abaisse le coût par token finit par gagner l'argent.</strong> Plus que la hausse de l'usage elle-même, c'est la réduction de coût qui rend cet usage supportable qui maintient en vie le flux de trésorerie du secteur. Cela dit, comme le note la mise en garde, si la longueur du contexte ou les tokens de raisonnement augmentent vite, la courbe de coût réelle peut baisser moins que ne le suggère ce graphique.

---

## 4. C'est pourquoi l'horizon temporel change

En combinant les deux prévisions, le chemin suivant est logiquement cohérent.

| Période | Ce qui se passe | Où c'est favorable |
|---|---|---|
| <strong>2026</strong> | L'usage des agents bondit → l'allocation de HBM, DRAM serveur, eSSD et NAND se tend → l'ASP de la DRAM et du NAND flambe | Le bêta de l'ASP mémoire fonctionne fortement |
| <strong>2027</strong> | Une base plus haute, plus quelques ajouts d'offre et des contrats à long terme (LTA), ralentissent le taux YoY de l'ASP. La mémoire IA B2B reste solide ; la mémoire grand public B2C rencontre une résistance de prix | Les cours intègrent un « taux de croissance qui ralentit » avant le « bénéfice maximal ». La divergence par segment commence |
| <strong>2028-2030</strong> | L'usage continue de croître, mais la baisse du coût par token l'absorbe | L'alpha bascule du bêta mémoire générique vers la <strong>pile de réduction du coût par token</strong> |

Le message central est unique. À partir de 2027, « de combien les prix de la DRAM et du NAND montent encore » importe moins que <strong>« quels composants et systèmes abaissent le coût par token. »</strong>

---

## 5. Exemples d'idées d'investissement (points d'observation, pas des recommandations)

Ci-dessous, il ne s'agit pas de recommandations de valeurs, mais d'<strong>exemples</strong> de « où regarder en premier » le long de l'horizon ci-dessus. Les valeurs IA et mémoire se sont déjà revalorisées rapidement, donc ce n'est pas un appel à acheter tout de suite, mais une carte pour le moment où les conditions seront réunies.

### Exemple 1 — Bêta de l'ASP mémoire 2026

La phase où l'allocation de HBM, DRAM serveur et eSSD se tend et où les prix de la DRAM et du NAND flambent. Les grandes capitalisations mémoire comme <strong>SK Hynix, Samsung Electronics et Micron</strong> en profitent directement. Le contre-argument est qu'une fois le ralentissement du taux de croissance de 2027 amorcé, le cours peut subir une compression de multiples d'abord, même si le bénéfice est élevé.

### Exemple 2 — Pile de réduction du coût par token

Le vrai cœur de la logique de Goldman n'est pas la hausse de l'usage mais la <strong>baisse du coût par token.</strong> Les clients paieront plus cher des puces et systèmes qui abaissent leur coût par token. Les <strong>ASIC sur mesure, les réseaux IA et l'optique, et les leaders du HBM</strong> s'y prêtent le mieux. (Les goulets d'interconnexion, de substrat et d'énergie vus dans le [read-through Marvell](/fr/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/) relèvent de ce même fil.)

### Exemple 3 — eSSD / NAND d'entreprise

L'inférence des agents exige bien plus de stockage de récupération (RAG), de journaux, de contexte, de KV cache et de checkpoints que le simple entraînement. S'il est vrai que les serveurs IA utilisent environ 3x la capacité SSD d'un serveur ordinaire, alors le NAND peut être reclassé non comme un actif de cycle générique, mais comme un <strong>goulet de stockage IA.</strong> Le contre-argument est la possibilité que la résistance de prix des SSD grand public dilue la vigueur de l'entreprise.

### Exemple 4 — Packaging avancé / MLCC / FC-BGA

Si la prévision de tokens de Goldman pour 2030 se réalise, la complexité de l'architecture des serveurs et des racks continue d'augmenter. Ce ne sont pas seulement les GPU, les ASIC et le HBM qui croissent ; la demande de surface de substrat, de stabilisation de l'alimentation, de condensateurs de découplage et de qualité de signal à haute vitesse croît de concert. Des fournisseurs de MLCC et FC-BGA haut de gamme comme <strong>Samsung Electro-Mechanics</strong> relèvent de cette catégorie.

### Des peak-outs différents selon le segment

L'important n'est pas « la mémoire dans son ensemble », mais les différences par segment. La logique du peak-out de J.P. Morgan ne s'applique pas de la même manière à toute la mémoire.

| Segment | Probabilité que le peak-out s'applique | Tension avec la demande à long terme |
|---|---|---|
| HBM | Faible-Moyenne | Élevée (la demande renforce sans cesse le mur de bande passante) |
| DRAM serveur | Moyenne | Moyenne |
| eSSD / NAND d'entreprise | Moyenne | Élevée (demande structurelle possible) |
| DRAM mobile | Élevée | Faible (résistance de prix grand public rapide) |
| DRAM/NAND générique | Élevée | Faible (la logique du peak-out s'applique le mieux) |

> Condition commune : les exemples ci-dessus exigent plus que « survendu » ou « parce que c'est de l'IA ». Un candidat doit se situer là où <strong>les commandes réelles, les prix contractuels et les estimations de bénéfice repartent à la hausse, et où les goulets et les barrières à l'entrée sont confirmés.</strong>

---

## 6. Les deux malentendus les plus courants

Dans cette phase, le marché est enclin à deux erreurs pointant dans des directions opposées.

<strong>Malentendu 1 — « J.P. Morgan dit peak-out, donc le cycle de l'infrastructure IA est terminé. »</strong> Non. Un peak-out est un ralentissement du <strong>taux de croissance</strong> du prix, pas un effondrement du <strong>niveau</strong> du prix. Et il s'applique le mieux à la mémoire générique et moins aux goulets comme le HBM, l'eSSD, l'ASIC et le packaging.

<strong>Malentendu 2 — « Goldman dit 24x tokens, donc les prix de la DRAM et du NAND continueront aussi de flamber jusqu'en 2030. »</strong> Cela aussi va trop loin. Goldman dit un usage explosif et une <strong>chute marquée du coût par token</strong> en même temps. Si le coût baisse vite, le taux de croissance en glissement annuel des prix de la mémoire peut ralentir même si l'usage augmente.

La lecture juste est entre les deux. <strong>Un super-cycle de la mémoire en 2026, un peak-out du momentum des prix en 2027, et une expansion à long terme de la pile de réduction du coût par token en 2028-2030.</strong>

---

## 7. Commentaire du gérant de fonds

Les deux prévisions ne sont pas ennemies mais deux axes d'un même tableau. Goldman parle de « combien, et à quel point bon marché, nous en viendrons à utiliser l'IA » ; J.P. Morgan parle de « jusqu'à quand les prix de la mémoire continueront de monter vite dans ce processus ». Le travail de l'investisseur n'est pas de choisir l'une des deux, mais de <strong>ne pas manquer les points d'inflexion de l'horizon temporel.</strong>

Les deux choix les plus dangereux sont les suivants.

* <strong>Jeter toute l'infrastructure IA à la vue du seul mot peak-out</strong> — l'erreur de brader même les gagnants dotés de goulets d'étranglement.
* <strong>Poursuivre la mémoire générique jusqu'au bout sur la seule demande de tokens</strong> — l'erreur de subir de plein fouet la compression de multiples dans la phase où le taux de hausse des prix s'essouffle.

Les signaux à vérifier maintenant, dits simplement, sont les suivants.

| Ce que vous surveillez | Renforce Goldman (demande) | Renforce J.P. Morgan (peak-out) |
|---|---|---|
| Usage de tokens | Forte croissance maintenue | Le taux de croissance ralentit |
| Coût par token | Continue de baisser de plus de 60% par an | Le rythme de baisse ralentit, le coût de latence monte |
| Contrats à long terme HBM | Prix tenus ou relevés | Renégociation, report de volumes |
| Prix contractuel DRAM serveur | Hausse supplémentaire | Le taux de hausse ralentit, remises au comptant |
| SSD d'entreprise | Les contrats à long terme avec les CSP s'élargissent | La résistance de prix du SSD grand public se propage |

En somme, <strong>reconnaître le bêta mémoire en 2026 tout en se préparant, à partir de 2027, à déplacer le poids vers les goulets qui abaissent le coût par token</strong> est la posture la plus raisonnable disponible aujourd'hui. Ni poursuivre la mémoire jusqu'au bout, ni tout jeter par peur du peak-out.

<small>Cet article est une analyse reconstituée à partir de l'article officiel de Goldman Sachs (2026-05-05), de graphiques et résumés secondaires liés à J.P. Morgan, et des prévisions officielles de TrendForce. Le texte intégral du rapport original de J.P. Morgan, ses tableaux d'ASP trimestriels et son détail par segment n'ont pas pu être vérifiés, et les noms d'entreprises sont des exemples illustrant le fil de l'analyse, non des recommandations d'investissement. Les décisions d'investissement réelles et leur responsabilité incombent à l'investisseur lui-même.</small>
