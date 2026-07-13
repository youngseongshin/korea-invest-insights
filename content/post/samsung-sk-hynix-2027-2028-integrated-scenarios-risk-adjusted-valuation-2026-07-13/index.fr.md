---
title: "2028 compte plus que le boom de 2027 : scénarios intégrés pour Samsung Electronics et SK Hynix"
description: "Partant du scénario de base d'un boom mémoire en 2027, cette analyse intègre l'expansion de l'offre en 2028, les gains d'efficacité à l'inférence et le risque de refinancement des infrastructures d'IA. Nous comparons Samsung Electronics et SK Hynix sur une base pondérée par les probabilités à travers le BPA par scénario, le PER de juste valeur et la valeur actuelle, et examinons comment les contrats HBM à long terme et l'expansion des capacités mémoire chinoises redéfinissent la durabilité des résultats."
date: 2026-07-13T20:39:17+09:00
lastmod: 2026-07-13T20:39:17+09:00
categories: ["Analyse Exclusive", "Semi-conducteurs", "Macro"]
tags:
  - "Samsung Electronics"
  - "SK Hynix"
  - "HBM"
  - "Semi-conducteurs de mémoire"
  - "Infrastructure d'IA"
  - "Analyse de scénarios"
  - "Valorisation"
  - "CXMT"
  - "YMTC"
series: ["exclusive-analysis", "ai-hbm-2026"]
slug: "samsung-sk-hynix-2027-2028-integrated-scenarios-risk-adjusted-valuation-2026-07-13"
image: "/images/posts/samsung-hynix-2027-2028-scenario-map-2026-07-13.png"
valley_cashtags:
  - 삼성전자
  - SK하이닉스
draft: false
---

> Contexte connexe : Ce billet fait suite à la [Vérification croisée du modèle offre-demande HBM 2030](/fr/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/), à la [Valorisation de Samsung Electronics et SK Hynix sur la base des résultats 2028E](/fr/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/), et à l'[Analyse du repli du secteur matériel IA du 13 juillet](/fr/post/kospi-9pct-selloff-ai-hardware-derating-korea-leverage-2026-07-13/). En acceptant le boom de 2027 comme référence, il quantifie la probabilité que les conditions d'offre, d'efficacité et de financement évoluent simultanément à partir de 2028.

## TL;DR

- L'offre et la demande de HBM resteront probablement tendues tout au long de 2027. Cependant, la projection `2030 demand 26.7EB vs. supply 10.6EB, 2.52× deficit` n'est pas une prévision de scénario de base — elle exige que plusieurs hypothèses haussières se maintiennent simultanément.
- L'année la plus importante n'est pas 2027 mais <strong>2028</strong>. L'expansion de l'offre de Samsung Electronics, SK Hynix et Micron, les gains d'efficacité à l'inférence, et la vérification du refinancement des centres de données IA convergent tous dans la même fenêtre temporelle.
- Les contrats d'approvisionnement HBM à long terme prolongent la durée des résultats mais n'éliminent pas le cycle. Ils convertissent le risque de prix en risque de renouvellement de contrat, risque de crédit client, risque de mix produits et risque de renégociation tarifaire.
- Probabilités conditionnelles : P1 excès de demande soutenu 35 %, P2 stress de crédit localisé avec recentrage sur les hyperscalers 40 %, P3 gains d'efficacité et normalisation de l'offre 15 %, P4 gel systémique du crédit 10 %.
- BPA pondéré par les probabilités pour 2027 : Samsung Electronics 60,750원, SK Hynix 393,000원. Pour 2028 : Samsung 49,900원, SK Hynix 316,000원.
- Valeur actuelle des valeurs terminales 2028 actualisées à 11 % par an : Samsung Electronics 317,246원, SK Hynix 1,956,316원 — impliquant respectivement une hausse potentielle de 24,7 % et 6,0 % par rapport aux cours de clôture KRX du 13 juillet. Une fois le risque de normalisation 2028 intégré, la marge de sécurité de Samsung est plus large ; SK Hynix est plus sensible au maintien de P1.

<div class="thesis-callout">
  <div class="thesis-callout__label">Conclusion</div>
  <div class="thesis-callout__body">
    Le boom de 2027 est relativement prévisible. La question plus difficile est de savoir <strong>si les prix élevés du HBM et les résultats se maintiennent jusqu'en 2028 et au-delà</strong>. Les cours actuels anticipent une durée des résultats bien au-delà du pic de 2027.
  </div>
</div>

![Carte de scénarios intégrés 2027–2028 pour Samsung Electronics et SK Hynix](/images/posts/samsung-hynix-2027-2028-scenario-map-2026-07-13.png)

## 1. Questions analytiques et qualité des données probantes

Cette analyse relie trois questions dans un cadre unique.

1. Quelle confiance peut-on accorder à l'hypothèse selon laquelle l'offre et la demande de HBM resteront tendues jusqu'en 2027 ?
2. Si les conditions d'offre, d'efficacité et de financement évoluent simultanément en 2028, comment les résultats de Samsung Electronics et SK Hynix diffèrent-ils selon les scénarios ?
3. Compte tenu de ces évolutions, à quel niveau de résultat implicite le cours actuel de l'action se négocie-t-il ?

Les chiffres de ce rapport doivent être lus par catégorie.

| Catégorie | Définition | Exemple dans ce rapport |
|---|---|---|
| Fait | Vérifié à partir de documents publics ou de données de marché | Cours de clôture KRX du 13 juillet, FCF d'Oracle, emprunts de CoreWeave |
| Consensus | Estimations de marché agrégées | BPA et résultat net 2027–2028 |
| Estimation de courtier | Prévision d'un courtier individuel | BPA SK Hynix de Korea Investment & Securities et BNK Investment & Securities |
| Résultat de modèle | Dérivé de formules et hypothèses divulguées | BPA pondéré par probabilités P1–P4 et valeurs actuelles |
| Jugement d'analyste | Jugement analytique non statistique | Probabilités de scénarios, PER de juste valeur, rendement requis de 11 % |
| Non disponible | Ne peut être déterminé à partir de sources publiques seules | Prix au niveau du contrat HBM, volumes par client, rendement de production réel |

Les formules de base sont les suivantes.

```text
Scenario Terminal Value = Scenario EPS × Scenario Fair PER
Probability-Weighted EPS = Σ(Scenario Probability × Scenario EPS)
Probability-Weighted Terminal Value = Σ(Scenario Probability × Scenario Terminal Value)
Present Value = Terminal Value ÷ (1 + 11%)^Remaining Years
HBM Need/Fleet = Installed and active HBM demand stock ÷ supply capacity that can be served by installed fleet
```

Les probabilités de scénarios ne sont pas dérivées de distributions de fréquences historiques. Ce sont des jugements conditionnels reflétant les conditions observables actuelles en matière de demande, d'offre, d'efficacité et de financement. Les valeurs de PER de juste valeur ne sont pas non plus mécaniquement observées sur le marché, mais constituent des estimations analytiques intégrant la durabilité des résultats, la concentration des activités, la structure financière et le risque à long terme.

## 2. Cours actuel et consensus de marché

Les cours de clôture KRX du 13 juillet et les estimations de consensus agrégées à la même date sont utilisés tout au long de cette analyse.

| Élément | Samsung Electronics | SK Hynix |
|---|---:|---:|
| Cours de clôture KRX 2026-07-13 | 254,500원 | 1,845,000원 |
| BPA consensus 2027 | 65,802원 | 444,359원 |
| BPA consensus 2028 | 65,907원 | 433,625원 |
| Résultat net consensus 2027 | 44.3조원 | 32.4조원 |
| Résultat net consensus 2028 | 44.1조원 | 31.9조원 |
| Cours actuel / BPA consensus 2027 | 3.87× | 4.15× |
| Cours actuel / BPA consensus 2028 | 3.86× | 4.25× |

En apparence, les deux sociétés semblent remarquablement bon marché. Mais ces faibles multiples PER ne signifient pas que le marché ignore les résultats 2027 — il s'agit plutôt d'un signal que le marché doute de la durabilité des résultats au-delà de 2028.

La dispersion des estimations concernant SK Hynix illustre clairement ce phénomène.

| Source | BPA 2027 | BPA 2028 | Interprétation |
|---|---:|---:|---|
| Consensus de marché | 444,359원 | 433,625원 | Normalisation modérée en 2028 |
| Korea Investment & Securities | 415,254원 | 495,696원 | La croissance des résultats se poursuit jusqu'en 2028 |
| BNK Investment & Securities | 214,642원 | 66,989원 | Passage rapide du pic après 2027 |

Pour la même société, les estimations de BPA 2028 s'échelonnent de 66,989원 à 495,696원. Cette divergence ne provient pas des prévisions de demande 2026 mais d'hypothèses différentes concernant <strong>les prix de vente moyens du HBM en 2028, le rythme d'expansion de l'offre et la durée des dépenses capex en IA</strong>.

Recalcul du PER actuel à l'aide du BPA pondéré par les probabilités de ce rapport :

| Année | Samsung Electronics | SK Hynix |
|---|---:|---:|
| 2027 | 4.19× | 4.69× |
| 2028 | 5.10× | 5.84× |

En appliquant à rebours le PER de juste valeur pondéré par les probabilités au cours actuel de l'action, le BPA implicite que le marché intègre est d'environ 31,700원 pour Samsung et d'environ 245,000원 pour SK Hynix — soit respectivement environ 52 % et 45 % en dessous du consensus 2027. Le marché n'actualise pas les résultats 2027 en tant que tels, mais la durée pendant laquelle ces résultats se maintiendront.

## 3. Ce qui a changé dans le cycle mémoire — et ce qui n'a pas changé

### Ce qui a changé

1. Les serveurs IA, la HBM et les SSD entreprise ont accru la part de la demande enterprise et data center dans l'ensemble du mix.
2. La HBM nécessite une qualification auprès des clients, un packaging avancé, des montées en rendement et des contrats à long terme, ce qui rend la réponse de l'offre à court terme plus lente que pour la DRAM classique.
3. Comme la HBM absorbe une part croissante des lancements de plaquettes, la production de DRAM classique issue des mêmes fabs diminue, ce qui peut soutenir les prix de la DRAM classique.
4. Le financement par les grands fournisseurs cloud et les opérateurs de data centers IA anticipe les commandes de mémoire effectives, jouant un rôle d'accélérateur.
5. À l'inverse, lorsque des problèmes de crédit émergent, la demande ne s'effrite pas progressivement — elle peut chuter brutalement via des renégociations de contrats et des reports d'investissements.

### Ce qui n'a pas changé

1. Des prix élevés finissent par attirer de nouvelles fabs, des améliorations de rendement, des transitions vers de nouveaux nœuds de procédé et des ajouts de capacité par les concurrents.
2. Les prix et marges élevés de la HBM renforcent l'incitation pour un fournisseur alternatif à entrer sur le marché et pour les clients à exercer une pression à la réduction des coûts.
3. Les contrats à long terme n'éliminent pas le risque de prix — ils le convertissent en risque de renouvellement tarifaire et en risque de crédit client.
4. Appliquer simultanément un BPA de pic à un PER élevé est une erreur de double optimisme qui valorise à la fois les bénéfices et les multiples à leur niveau le plus favorable.

L'affirmation selon laquelle la HBM a fait de la mémoire un secteur plus solide que la DRAM traditionnelle, et l'affirmation que le cycle mémoire a été aboli, ne constituent pas la même thèse.

## 4. Modèle offre-demande HBM et l'inflexion de 2028

Dans le [modèle de vérification croisée offre-demande HBM 2030](/fr/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/), nous avons reproduit le modèle original `demande 26.7EB, offre 10.6EB, déficit 2.52×` en unités cohérentes. La formule elle-même ne compare pas incorrectement un flux de demande à un stock d'offre. Le problème est que les hypothèses à long horizon se multiplient en série.

Celles-ci comprennent :
- La croissance mensuelle de la consommation de tokens
- La taille des modèles, la longueur du contexte et l'expansion de l'état des agents
- Les ratios de cache KV et de résidence mémoire
- L'efficacité du débit, de la quantification et du routage
- La durée de vie des HBM et la migration des charges de travail d'inférence vers d'autres types de mémoire
- Les volumes de production atteignables et le rendement de packaging auprès des trois principaux fabricants de mémoire

Pour cette raison, le déficit 2.52× en 2030 doit être traité comme un scénario de stress haussier plutôt que comme un cas de base. La redérivation des hypothèses centrales alignées sur chacun des scénarios P1–P4 donne les résultats suivants :

| Scénario | Multiplicateur de tokens | Échelle du modèle | Efficacité du débit | Efficacité KV | Résidence HBM | Demande | Besoin/Flotte |
|---|---:|---:|---:|---:|---:|---:|---:|
| P1 Orderly Excess Demand | 20× | 4.0× | 12× | 5.0× | 65% | 16.1EB | 1.52× |
| P2 Localized Credit Stress & Re-concentration | 18× | 3.5× | 12× | 5.5× | 60% | 12.8EB | 1.21× |
| P3 Efficiency Gains & Supply Expansion | 12× | 2.0× | 14× | 6.0× | 50% | 6.5EB | 0.62× |
| P4 Systemic Credit Seizure | 8× | 2.0× | 14× | 7.0× | 45% | 2.6EB | 0.25× |

Pour la comparabilité, la capacité d'offre est maintenue fixe à 10.6EB. Les lancements de plaquettes HBM réels, le mix produit, le rendement des puces conformes et la capacité de packaging ne sont pas publics, de sorte que les valeurs absolues ne peuvent pas être confirmées.

En examinant l'axe temporel, l'appréciation se simplifie considérablement.

| Période | Appréciation | Confiance |
|---|---|---|
| 2026–2027 | La transition HBM4 et la demande IA dépassent les ajouts de capacité des nouvelles fabs | Élevée |
| 2028 | La ligne 1 de SK Hynix à Yongin, Micron ID1/Tongluo, et l'expansion HBM de Samsung commencent à détendre l'offre | Moyen-Élevé |
| 2029–2030 | Le déficit résiduel a plus de chances de se réduire que de s'approfondir | Moyenne |
| Déficit 2.5× en 2030 | Nécessite que plusieurs hypothèses haussières se vérifient simultanément | Faible |

La décision d'investissement ne dépend donc pas de la question de savoir si le boom de 2027 se produit. Le pivot est de savoir si les capacités d'offre supplémentaires entrant en ligne en 2028 obtiennent les qualifications clients, et si ce calendrier coïncide avec les gains d'efficacité de l'inférence et un financement plus strict des data centers IA.

## 5. Contrats à long terme de SK Hynix et la courbe des bénéfices

Le rapport SK Hynix de Korea Investment & Securities du 13 juillet attribue la déception par rapport au consensus du T2 non pas à un effondrement de la demande, mais à un décalage temporel dans la façon dont les changements de mix produit HBM et la tarification des contrats d'approvisionnement à long terme se répercutent sur les résultats publiés.

| Élément | 2026F | 2027F | 2028F |
|---|---:|---:|---:|
| Chiffre d'affaires | 32.83조원 | 48.77조원 | 58.53조원 |
| Résultat d'exploitation | 24.51조원 | 37.45조원 | 44.70조원 |
| BPA | 292,068원 | 415,254원 | 495,696원 |
| ROE | 94.5% | 65.4% | 46.5% |

Les hypothèses HBM sont également agressives.

| Indicateur HBM | 2026F | 2027F |
|---|---:|---:|
| Croissance en bits | +23.0% | +31.2% |
| ASP | $1.60/Gb | $2.82/Gb |
| Croissance de l'ASP | -2.5% | +76.3% |
| Chiffre d'affaires | 3.71조원 | 8.30조원 |
| Croissance du CA | +28.0% | +123.6% |

Les principaux ajustements d'estimations au sein du rapport comprennent :

- Les ventes de HBM4 débutent au T3 2026, mais l'inflexion des bénéfices la plus importante est modélisée au T4 lorsque l'ASP HBM augmente de `+52% QoQ`.
- Par rapport aux estimations de mai, l'ASP de la DRAM non-HBM pour 2026–2027 a été réduit d'environ 16%.
- Le chiffre d'affaires HBM 2026 a été relevé de 17%.
- Le volume d'expéditions HBM 2027 a été maintenu stable tandis que l'ASP a été réduit de 5%.
- Les volumes d'expéditions et les prix du NAND ont été relevés.

Ce rapport ne constitue pas un reniement de la thèse de croissance à long terme de la HBM. C'est une révision qui abaisse l'élasticité-prix à court terme de la DRAM classique et repousse le moment où l'économie de la HBM4 se reflète dans les résultats publiés.

### Pourquoi les contrats à long terme ne doivent pas être pris au pied de la lettre

1. Les planchers de prix, les plafonds, les obligations d'achat minimum et les modalités de prépaiement au niveau contractuel ne sont pas divulgués publiquement.
2. Les rapports indiquant que les contrats ne comportent « aucun plafond de prix » ne peuvent à eux seuls confirmer que les prix augmentent chaque année — il faut savoir si la tarification est indexée sur les taux spot et à quelle fréquence elle est révisée.
3. Les contrats à long terme verrouillent les volumes et les relations clients, mais n'éliminent pas le risque de renégociation, de défaut ou de détérioration du crédit client.
4. La DRAM non-HBM et le NAND en dehors de ces contrats restent pleinement exposés au cycle des prix des composants.
5. Si le rendement de la HBM4 est faible, les expéditions de SK Hynix et les bénéfices marginaux pourraient tout de même manquer leurs objectifs même si le marché reste en situation de sous-approvisionnement.

Le principal avantage des contrats à long terme n'est pas l'élimination du cycle mais <strong>l'allongement de la durée des bénéfices et la conversion de la forme du risque</strong>.

## 6. Comment le financement des infrastructures IA se traduit en commandes de mémoire

La demande de mémoire pour l'IA n'est pas uniquement tirée par la technologie. L'activité de financement des opérateurs de centres de données génère des commandes anticipées, et lorsque les conditions financières se resserrent, des écarts de commandes peuvent apparaître brutalement.

```text
Hausse des anticipations IA
  -> Investissement dans les centres de données cloud/IA et expansion des contrats à long terme
  -> Capex anticipé en GPU, HBM, énergie et centres de données
  -> Appréciation des actifs, des revenus et de la valeur d'entreprise
  -> Financements supplémentaires par dette et capital
  -> Programmes d'investissement plus importants

Sens inverse
Retard de monétisation ou hausse des coûts de refinancement
  -> Renégociation des contrats / retards d'expansion
  -> Écarts de commandes de mémoire
  -> Baisse du prix de vente moyen (ASP) et du cours de bourse
  -> Détérioration de la valeur des garanties et des conditions de financement
  -> Nouvelle réduction des capex
```

Les chiffres confirmés par les publications officielles sont significatifs.

| Élément | Valeur confirmée | Interprétation |
|---|---:|---|
| Oracle FY2026 Free Cash Flow | -$23.7B | Les capex IA à grande échelle dépassent la génération de trésorerie |
| Oracle Debt Financing | $43B | Financement externe massif pour l'investissement IA |
| Oracle Equity Financing | $5B | La dette seule est insuffisante pour couvrir l'investissement |
| Oracle RPO | $638B | Les contrats à long terme offrent une forte visibilité sur les revenus |
| Oracle Customer Prepayments & Direct GPU Provision | $75B | Les clients finaux partagent le risque d'investissement |
| CoreWeave Total Debt (End 2025) | $21.6B | Levier financier élevé dans les centres de données IA |
| CoreWeave New DDTL 4.0 | $8.5B | Financement supplémentaire pour poursuivre l'expansion |
| CoreWeave DSCR Threshold | Minimum 1.15× | La vérification complète du refinancement commence au plus tard après le 30 juin 2027 |

Les emprunts détaillés de CoreWeave fin 2025 comprenaient la DDTL 2.0 pour environ $5.04B, la DDTL 2.1 pour environ $2.74B, la DDTL 1.0 pour environ $1.55B, la DDTL 3.0 pour environ $0.34B, et des contrats de location-financement d'équipements/logiciels pour environ $4.17B. La DDTL 4.0, signée en mars 2026, s'élève à $8.5B.

Ces chiffres n'impliquent pas que la demande IA soit fictive. Les contrats, les GPU, les infrastructures électriques et les centres de données sont bien réels. Cependant, si les flux de trésorerie ne suivent pas le rythme des coûts de financement en 2027–2028, les opérateurs les plus fragiles seront probablement amenés à céder leurs actifs, absorbés par les grands fournisseurs cloud.

C'est pourquoi la probabilité attribuée à <strong>P2 — stress localisé suivi d'une reconcentration des actifs chez les hyperscalers</strong> — dépasse celle d'un effondrement systémique P4. Dans le scénario P2, les commandes de mémoire ne disparaissent pas, mais un écart d'un trimestre ou plus est plausible.

## 7. Arbre de probabilités conditionnelles P1–P4

Les probabilités finales sont dérivées de la séquence `demande réelle → vérification financière → offre/efficacité → absorption des actifs`, et non des fréquences historiques des cycles de mémoire.

```text
Vérification de la monétisation IA et du refinancement en 2028
  Réussite 50%
    ├─ P1 Excédent de demande soutenu 70%        = 35%
    └─ P3 Normalisation efficacité/offre 30%     = 15%
  Stress 50%
    ├─ P2 Stress localisé/reconcentration 80%    = 40%
    └─ P4 Crise de crédit systémique 20%         = 10%
```

La première branche 50/50 n'est pas un a priori statistique. C'est un point de départ neutre reflétant le fait que la demande réelle et les contrats sont solides, mais que la vérification financière n'est pas encore achevée. Calculer des probabilités à un point de pourcentage près à partir des données actuelles produirait une fausse précision — les ajustements ne sont effectués que par tranches de 5 points de pourcentage.

### Éléments probants en faveur d'une vérification réussie ou d'un stress financier

| Éléments en faveur d'une vérification réussie | Éléments en faveur d'un stress financier |
|---|---|
| Retard de montée en cadence de la production de masse HBM jusqu'en 2027 | Oracle FY2026 FCF -$23.7B, financement par dette $43B |
| Oracle RPO $638B, prépaiements clients et fourniture directe de GPU $75B | Dette totale CoreWeave $21.6B, nouvelle DDTL $8.5B |
| Les contrats à long terme et les prépaiements HBM améliorent la visibilité des commandes | Vérification du DSCR CoreWeave 1.15× après mi-2027 |
| Investissement réel des grands fournisseurs cloud dans les centres de données | Hausse de la prime de risque sur les obligations IA à long terme |

La répartition 70/30 entre P1 et P3 sur la branche de vérification réussie reflète le fait que jusqu'en 2027, les goulets d'étranglement liés à la qualification, au rendement et au conditionnement persistent, tandis que les optimisations côté mémoire — MoE, MLA, compression KV, routage et déchargement — peuvent toutes évoluer simultanément à partir de 2028.

La répartition 80/20 entre P2 et P4 sur la branche de stress est également claire. Les GPU et les centres de données ne sont pas des actifs qui disparaissent — les hyperscalers disposant de flux de trésorerie solides peuvent les acquérir et les redéployer. Étant donné que des réductions de capex simultanées, de multiples violations de covenants et des dépréciations de contrats à long terme HBM ne se sont pas encore toutes matérialisées ensemble, P4 est traité comme un risque de queue à 10%.

### Registre des éléments probants

| Élément probant | P1 | P2 | P3 | P4 | Évaluation |
|---|---:|---:|---:|---:|---|
| Retard d'approvisionnement HBM jusqu'en 2027 | ++ | + | - | -- | La pénurie persiste |
| Expansion de l'offre mémoire des 3 premiers post-2028 | - | 0 | ++ | 0 | Voie indépendante P3 |
| Expansion client DDR5/LPDDR de CXMT | - | - | ++ | 0 | Plafonne le prix des composants avant le HBM |
| Montée en puissance du NAND haute couche de YMTC et adoption clients | - | - | ++ | 0 | Pression d'abord sur le NAND Samsung et le mix SSD entreprise |
| Qualification clients HBM/mémoire serveur Chine | -- | - | ++ | 0 | Si confirmé, glissement de P1 vers P3 |
| Oracle RPO & GPU fournis par les clients | + | + | 0 | - | La demande est réelle ; tampon contre la contagion |
| FCF négatif d'Oracle & financement important | - | ++ | 0 | + | Risque de stress de crédit localisé |
| Dette CoreWeave & vérification DSCR | - | ++ | 0 | + | Inflexion financière 2027–2028 |
| Hausse de la prime de risque sur les obligations IA à long terme | -- | ++ | 0 | + | Glissement de 5pp de P1 vers P2 |
| Gains d'efficacité de l'inférence & déchargement | - | 0 | ++ | 0 | Preuves insuffisantes au niveau production |
| Capacité d'absorption des actifs par les hyperscalers | 0 | ++ | 0 | -- | Pourquoi P2 l'emporte sur P4 |

`++` et `--` indiquent uniquement la direction et ne constituent pas des ratios de vraisemblance statistiques.

### Historique des révisions de probabilités

| Étape | P1 | P2 | P3 | P4 | Justification |
|---|---:|---:|---:|---:|---|
| Initial | 40% | 35% | 15% | 10% | Dominance de la pénurie physique d'offre, risque financier localisé, voie offre/efficacité |
| Faiblesse des obligations IA longue durée intégrée | 35% | 40% | 15% | 10% | Glissement de P1 vers P2 de 5pp ; absence de preuve de contagion |
| Révision des capex des hyperscalers | 35% | 40% | 15% | 10% | Les effets d'exécution de la demande et de concentration des actifs se compensent |
| Révision des scénarios IA à long terme | 35% | 40% | 15% | 10% | 2027–2028 inchangé ; seule la probabilité P3 post-2030 s'élargit |
| Révision de la trajectoire d'offre Chine | 35% | 40% | 15% | 10% | Risque d'offre de composants intégré ; preuves de qualification clients HBM insuffisantes |

### Plages d'incertitude des probabilités et règles de révision

| Scénario | Centrale | Plage d'incertitude | Signaux forts susceptibles de modifier l'estimation centrale |
|---|---:|---:|---|
| P1 | 35% | 25–45% | Deux hyperscalers ou plus relèvent leurs prévisions de capex ; les coûts de financement se stabilisent ; les contrats à long terme se renforcent |
| P2 | 40% | 30–50% | Un événement de stress d'un opérateur fragile avec absorption des actifs par un hyperscaler |
| P3 | 15% | 10–25% | Expansion de l'offre des 3 premiers ou de la Chine confirmée en volume ; la consommation HBM par token diminue |
| P4 | 10% | 5–15% | Défauts multiples d'opérateurs, deux réductions de capex ou plus et dépréciations de contrats à long terme surviennent simultanément |

- Un seul article de presse ou une anecdote ne justifie qu'un ajustement de 0 à 2pp.
- Un seul signal fort issu d'un document déposé par une entreprise ou d'un rapport de résultats justifie au maximum un ajustement de 5pp.
- Deux signaux forts indépendants ou plus dans la même direction justifient un glissement de 5 à 10pp.
- Un stress de crédit localisé déplace la probabilité de P1 vers P2 ; des preuves de contagion la déplacent de P2 vers P4 ; des preuves d'offre/efficacité la déplacent de P1 vers P3.

## 8. Scénarios Finaux et Pression sur les Prix HBM

| Scénario | Prob. | État 2028 | Besoin/Parc 2030 | Pression Prix HBM | Issue Principale |
|---|---:|---|---:|---:|---|
| P1 Excès de Demande Ordonné | 35% | Tendu ou équilibré | 1,3–1,8× | Stable à -10% | Le plancher des prix contractuels tient ; les bénéfices HBM atteignent un plateau |
| P2 Stress Crédit Localisé & Reconcentration | 40% | Écart de commandes, légère surcapacité | 0,9–1,3× | -15 à -30% | Les opérateurs faibles sortent ; les hyperscalers absorbent les actifs |
| P3 Gains d'Efficience & Expansion de l'Offre | 15% | Surplus d'offre croissant | 0,6–0,9× | -20 à -35% | L'utilisation des tokens progresse mais la prime HBM se comprime |
| P4 Crise Systémique du Crédit | 10% | Coupes capex et correction des stocks | 0,3–0,6× | -40 à -55% | Renégociation des contrats LT, réductions de production, annulations de capex, intervention réglementaire |

Toutes les autres variables étant constantes, un déplacement de 10 points de pourcentage hors de P2 modifie les valeurs terminales 2028 comme suit :

| Déplacement de Probabilité | Variation Valeur Terminale Samsung | Variation Valeur Terminale SK Hynix | Signification |
|---|---:|---:|---|
| 10pp de P2 vers P1 | +21 800원 | +227 000원 | Probabilité plus élevée d'une sous-offre soutenue |
| 10pp de P2 vers P3 | -7 500원 | -70 000원 | L'économie IA progresse mais la prime HBM se comprime |
| 10pp de P2 vers P4 | -16 800원 | -132 000원 | Contagion du stress localisé vers le risque systémique |

SK Hynix est plus sensible à chaque déplacement de probabilité. Même avec les probabilités centrales identiques, les marges d'erreur de valorisation et la volatilité du cours de SK Hynix sont plus importantes en raison de sa concentration plus élevée sur le HBM.

## 9. L'Expansion de l'Offre Chinoise est une Variable dans Tous les Scénarios, Non un Scénario Distinct

La croissance des capacités de CXMT et YMTC ne constitue pas un cinquième scénario indépendant de P1–P4. Il s'agit d'une variable d'offre qui modifie la tarification au niveau des produits et les parts de marché dans chaque scénario.

| Stade d'Avancement Chine | Marché Affecté en Premier | Samsung Electronics | SK Hynix | Correspondance Scénario |
|---|---|---|---|---|
| Expansion CXMT DDR4/DDR5/LPDDR domestique | DRAM commodité | Pression sur les ASP et le mix produit | Impact direct relativement limité | BPA réduit dans tous les scénarios ; probabilités inchangées |
| Qualification clients PC mondiaux CXMT | DDR5/LPDDR client mondial | Plafonnement des ASP et pression sur les parts simultanément | Exposition client à risque | Risque haussier P3 |
| Pénétration chinoise RDIMM serveur bas de gamme | DRAM serveur standard | Pression partielle sur le mix serveur | DRAM hors serveurs IA à risque | Revue haussière P3 |
| Montée en puissance NAND haute couche YMTC et adoption clients | NAND grand public/SSD entreprise | Plus forte pression sur les parts NAND et les marges | Solidigm et SSD entreprise à risque | Réduction BPA et multiple P3 |
| Production en masse HBM Chine et qualification clients IA | HBM | Rattrapage HBM partiel compensé | Risque important sur la prime de rareté et les parts | Déplacement de 5–10pp de P1 vers P3 |
| Montée en puissance Chine et ralentissement simultané capex IA mondial | Toute la mémoire | Pression combinée commodité/NAND/HBM | Pression combinée HBM/DRAM | Surveiller la contagion P3 vers P4 |

En 2026–2027, CXMT est plus susceptible de plafonner les prix DDR5 client et LPDDR que de fragiliser directement les prix HBM. YMTC pourrait de même intensifier d'abord la concurrence par les prix dans le NAND grand public et certains SSD entreprise.

Pour que la Chine devienne une menace directe sur le HBM, la seule production de dies DRAM est insuffisante. Le collage TSV, l'empilement, l'intégration du die de base, le packaging avancé, et des qualifications répétées en production de masse par les clients IA sont tous nécessaires.

Les signaux suivants doivent être confirmés avant que l'expansion des capacités chinoises soit intégrée numériquement en quantités significatives :

1. Le DDR5/LPDDR de CXMT est adopté en volume par les fabricants mondiaux de PC à des prix supérieurs de plus de 20 % en dessous de ceux des trois premiers fournisseurs de mémoire.
2. CXMT obtient une qualification au-delà des PC grand public vers les PC entreprise et les RDIMM serveur.
3. Le NAND haute couche de YMTC est confirmé par des volumes d'expédition réels et des gains de clients SSD entreprise — et non de simples objectifs déclarés.
4. Le HBM chinois dépasse la qualification sur échantillons pour atteindre des qualifications répétées en production de masse par les clients de processeurs d'accélération IA.
5. Une croissance de l'offre et une baisse des prix DRAM/NAND commodité chez les trois premiers fournisseurs sont observées conjointement pendant deux trimestres consécutifs ou plus.

## 10. Samsung Electronics : BPA et Juste Valeur par Scénario

| Année | Scénario | BPA | PER Juste | Valeur Terminale |
|---|---|---:|---:|---:|
| 2027 | P1 | 65 000원 | 8,5× | 552 500원 |
| 2027 | P2 | 62 000원 | 8,0× | 496 000원 |
| 2027 | P3 | 58 000원 | 7,5× | 435 000원 |
| 2027 | P4 | 45 000원 | 7,0× | 315 000원 |
| 2028 | P1 | 68 000원 | 8,5× | 578 000원 |
| 2028 | P2 | 45 000원 | 8,0× | 360 000원 |
| 2028 | P3 | 38 000원 | 7,5× | 285 000원 |
| 2028 | P4 | 24 000원 | 8,0× | 192 000원 |

Un PER de base supérieur à 9× n'est pas attribué à Samsung car la réduction des pertes de la fonderie n'a pas encore été confirmée. Un multiple de 8,5× en P1 ne devient atteignable que si la reconquête des parts HBM, la tarification DRAM/NAND commodité, et la normalisation de la fonderie opèrent simultanément.

Un multiple de 8,0× en P4 est appliqué pour éviter l'erreur de double décote consistant à multiplier un BPA de creux par un PER lui aussi déprimé. Dans un scénario de récession effective, le BPA normalisé, la trésorerie nette et la valeur comptable doivent tous être examinés conjointement.

## 11. SK Hynix : BPA et Juste Valeur par Scénario

| Année | Scénario | BPA | PER Juste | Valeur Terminale |
|---|---|---:|---:|---:|
| 2027 | P1 | 430 000원 | 9,0× | 3 870 000원 |
| 2027 | P2 | 405 000원 | 7,0× | 2 835 000원 |
| 2027 | P3 | 370 000원 | 6,0× | 2 220 000원 |
| 2027 | P4 | 250 000원 | 5,5× | 1 375 000원 |
| 2028 | P1 | 470 000원 | 9,0× | 4 230 000원 |
| 2028 | P2 | 280 000원 | 7,0× | 1 960 000원 |
| 2028 | P3 | 210 000원 | 6,0× | 1 260 000원 |
| 2028 | P4 | 80 000원 | 8,0× | 640 000원 |

Le multiple P1 de 9× présuppose des parts de marché HBM, des conditions contractuelles à long terme, un ROE élevé, et une réévaluation structurelle de SK Hynix en tant qu'actif IA stratégique. Le maintien de ce multiple jusqu'en 2028 exige une défense confirmée des parts HBM4E, une révision des prix sur les contrats à long terme, et des actions de retour aux actionnaires.

L'objectif de cours de Korea Investment & Securities à 3 800 000원 applique un PBR de 6,0× au BPA prévisionnel sur 12 mois — au-dessus du pic historique de la fourchette de 5,0× cité dans le même rapport. Un objectif à 3 800 000원 requiert donc non seulement la réalisation des bénéfices, mais aussi une réévaluation structurelle du secteur mémoire.

En P2 et P3, la concentration HBM se transforme d'avantage en vulnérabilité. Lorsque les ASP baissent, les bénéfices et les multiples peuvent se comprimer simultanément.

## 12. Résultats Pondérés par les Probabilités et Comparaison Ajustée au Risque

| Année | Société | BPA Pondéré | PER Blendé Juste | Valeur Terminale Pondérée | VA au Taux d'Actualisation Annuel de 11% | vs. Cours Actuel |
|---|---|---:|---:|---:|---:|---:|
| 2027 | Samsung Electronics | 60 750원 | 8,04× | 488 525원 | 421 385원 | +65,6% |
| 2027 | SK Hynix | 393 000원 | 7,53× | 2 959 000원 | 2 552 333원 | +38,3% |
| 2028 | Samsung Electronics | 49 900원 | 8,18× | 408 250원 | 317 246원 | +24,7% |
| 2028 | SK Hynix | 316 000원 | 7,97× | 2 517 500원 | 1 956 316원 | +6,0% |

Quatre observations découlent de ces résultats :

1. Appréciées sur l'horizon 2027 seul, les deux sociétés affichent des valeurs ajustées au risque supérieures aux cours actuels.
2. Une fois actualisée la probabilité de normalisation 2028, la marge de sécurité de Samsung est plus importante.
3. La valeur actuelle 2028 de SK Hynix n'est supérieure que de 6 % au cours actuel de l'action. Une large part du rendement attendu dépend du maintien de P1.
4. La mémoire commodité de Samsung, la fonderie et la position de trésorerie nette constituent un amortisseur partiel à la baisse en P2 et P3.

Ce que le marché connaît déjà bien, c'est la sous-offre HBM et la hausse des prix mémoire. Ce qui pourrait être mal valorisé dans les deux sens :

- Si le rattrapage HBM de Samsung coïncide avec une reprise des prix DRAM/NAND commodité, bénéfices et multiples pourraient progresser conjointement.
- Si les contrats à long terme et le HBM4E de SK Hynix défendent les planchers de prix et les parts même après les ajouts d'offre post-2028, la décote de normalisation actuelle pourrait s'avérer excessive.

Inversement, le marché pourrait avoir raison si l'offre, l'efficience et les conditions de crédit s'améliorent toutes simultanément en 2028, écourtant ainsi les bénéfices au pic.

## 13. Comment Appréhender la Demande à Long Terme en IA au-delà de 2030

[AI 2040 Plan A](https://ai-2040.com/?choices=plan-a-root) présente une trajectoire allant d'environ 20 millions d'H100e en 2026 à 60 milliards d'H100e d'ici 2034, avec une consommation électrique dédiée au calcul IA atteignant 5 TW à l'horizon 2034. Toutefois, le document lui-même présente ce scénario comme un cadre de politique, non comme une prévision de référence, et précise que certaines variables ont été ajustées de concert avec la narration.

Les scénarios à long terme ne sont donc pas intégrés directement dans les estimations de BPA 2027–2028.

| Période | P1 Excès de demande | P2 Reconcentration | P3 Croissance des volumes / Normalisation des prix | P4 Défaillance | Statut |
|---|---:|---:|---:|---:|---|
| 2026–2028 | 35 % | 40 % | 15 % | 10 % | Probabilités de l'analyse en cours |
| Référence conditionnelle post-2030 | 25 % | 35 % | 30 % | 10 % | Jugement à long terme ; non une probabilité statistique |

Si l'IA et la robotique améliorent l'efficience de la conception de puces, de la construction de fabs et de la production, la demande totale en bits mémoire pourrait croître tandis que la prime de rareté spécifique à l'HBM se réduirait. <strong>L'expansion du marché HBM et la revalorisation du PER à long terme doivent donc être évaluées séparément.</strong>

À mesure que la demande en mémoire à long terme augmente, l'univers d'opportunités s'élargit non seulement à l'HBM, mais également à la DRAM standard, au NAND, aux SSD d'entreprise, aux contrôleurs, au CXL, à l'alimentation électrique, au refroidissement et aux interconnexions. Cela constitue un avantage relatif pour Samsung, dont le portefeuille produits est plus diversifié.

## 14. Conditions Nécessaires à la Validité de Cette Analyse

### Samsung Electronics

1. Les qualifications clients pour l'HBM4 et l'HBM4E doivent se convertir en volumes réels de production de masse et en parts de revenus.
2. La reprise des prix contractuels de la DRAM standard et du NAND doit compenser les coûts d'investissement HBM, les primes et les provisions.
3. Les pertes de la division Foundry doivent se réduire et commencer à contribuer de manière significative aux résultats 2027–2028.
4. La trésorerie nette et la capacité de retour aux actionnaires doivent être préservées malgré un capex soutenu.

### SK Hynix

1. La part de marché HBM4E et les planchers de prix des contrats à long terme doivent tenir, même à mesure que Samsung et Micron accroissent leur offre.
2. La révision des prix HBM entamée au T4 2026 doit converger vers la moyenne 2027 de 2,82 $/Gb.
3. Les faiblesses de rendement en matière de TSV et d'empilement doivent s'avérer temporaires et imputables aux coûts de transition produit.
4. Le fort flux de trésorerie disponible doit être alloué aux retours aux actionnaires et à la politique de capital, et non exclusivement à l'expansion des capacités.

## 15. Signaux de Risque et Indicateurs Avancés

| Risque | Indicateur avancé | Impact Samsung | Impact SK Hynix | Ajustement d'analyse |
|---|---|---|---|---|
| Renégociation des contrats à long terme HBM | Affaiblissement du plancher de prix, des avances et des minimums d'achat | Modéré | Très élevé | P2/P4 en hausse |
| Réduction des guidances capex des hyperscalers | Deux réductions simultanées ou plus | Élevé | Très élevé | P2/P4 en hausse |
| Événement de refinancement des datacenters IA | Conditions de covenant CoreWeave/coûts de financement, financement Oracle | Modéré | Élevé | P2 en hausse ; P4 en hausse si contagion |
| Expansion accélérée de l'offre | Volumes HBM capables en production chez Samsung/Micron en hausse | Positif pour le rattrapage HBM ; négatif pour les prix | Très négatif | P3 en hausse |
| Amélioration marquée de l'efficience d'inférence | Baisse des bits HBM par jeton | Le portefeuille produits étendu offre un amortisseur partiel | Négatif | Multiple HBM en baisse |
| Expansion de l'offre chinoise en mémoire standard | Prix CXMT/YMTC, parts de marché, qualifications clients mondiaux | Plus négatif pour la DRAM/NAND standard | DRAM client et Solidigm sous pression | Réduction du BPA par segment produit |
| Percée chinoise sur l'HBM | TSV/empilement/die de base/packaging/qualification clients | Compensation partielle de la valeur de rattrapage HBM | Très négatif pour la prime de rareté | Glissement P1 vers P3 |
| Échec de normalisation Foundry | Pertes persistantes, absence d'amélioration des rendements | Risque spécifique à Samsung | Impact limité | Réduction du multiple P1 Samsung |

### Signaux Haussiers

- Contrats à long terme HBM 2028 avec des volumes et des prix plus élevés et une diversification clientèle plus large
- Stabilisation précoce du rendement HBM4E et des volumes de production de masse
- Confirmation simultanée de la progression de la part HBM de Samsung et du rétrécissement des pertes Foundry
- Revenus des services IA et flux de trésorerie croissant plus vite que les contrats en ressources de calcul
- Les délais de livraison et les allocations HBM se maintiennent même si l'expansion de l'offre accuse du retard
- Le plan de retour aux actionnaires de SK Hynix se concrétise

### Signaux Baissiers

- Baisse simultanée du PAM HBM et du volume d'expéditions
- Deux hyperscalers majeurs ou plus abaissent leurs taux de croissance de capex
- Renégociation, rupture ou dépréciation des avances sur contrats à long terme
- Accumulation des stocks mémoire et inversion du prix spot par rapport au prix contractuel
- La consommation réelle de bits HBM par jeton des services IA recule de 20 %+ durant deux trimestres consécutifs
- L'augmentation des volumes de Samsung/Micron coïncide avec le recul de la prime HBM

Sur une base mensuelle, les indicateurs à suivre conjointement sont : les prix contractuels et les avances sur HBM4/4E, les volumes et rendements des trois premiers producteurs de mémoire, les délais de livraison en packaging avancé, le capex et les flux de trésorerie des hyperscalers, les coûts de financement d'Oracle et CoreWeave, le chiffre d'affaires des ODM serveurs taïwanais, ainsi que les prix contractuels et les niveaux de stock de DRAM/NAND.

## 16. Interprétation Relative pour l'Investissement

Les deux valeurs ne constituent pas des expositions équivalentes au même cycle haussier de la mémoire.

| Scénario | Samsung Electronics | SK Hynix |
|---|---|---|
| Renforcement P1 | Rattrapage HBM et vent favorable de la mémoire standard | Levier bénéficiaire maximal via la part HBM et les contrats LT |
| Avertissement P2 | La diversification des activités et la trésorerie nette offrent une défense partielle | Plus sensible aux écarts de commandes et à la compression des multiples |
| Renforcement P3 | La gamme produits mémoire étendue et l'exécution Foundry offrent un amortisseur partiel | Exposition directe à la compression de la prime HBM |
| Avertissement P4 | Un recul absolu est inévitable, mais une défense relative reste possible | Risque le plus élevé de déclin simultané des bénéfices et des multiples |

D'un point de vue ajusté au risque, Samsung offre un choix plus large et plus défensif. SK Hynix affiche un levier bénéficiaire supérieur en P1, mais sa valorisation évolue plus rapidement lorsque les conditions d'offre, d'efficience et de crédit changent.

Les valeurs d'équipementiers et de matériaux ne doivent pas non plus être regroupées indistinctement. Les équipementiers exposés aux écarts de commandes doivent être distingués des fournisseurs de consommables et de pièces dont les revenus suivent les taux d'utilisation. Les équipements bénéficiant de commandes fermes confirmées et les composants/matériaux à revenus récurrents s'intègrent mieux à ce cadre de scénarios qu'un panier thématique HBM pur.

## 17. Conclusion

La dynamique haussière de la mémoire jusqu'en 2027 peut être maintenue comme trajectoire centrale pour les estimations de bénéfices. Mais le véritable test du niveau actuel des cours boursiers n'est pas le BPA 2027 — c'est la durabilité des bénéfices au-delà de 2028. L'argument selon lequel le déficit d'offre HBM a duré plus longtemps que les cycles passés, et celui selon lequel les fabricants de mémoire méritent un multiple de rareté structurellement élevé, ne sont pas interchangeables.

Samsung Electronics cumule simultanément un potentiel de rattrapage HBM, une exposition à la DRAM/NAND standard, des activités Foundry et une trésorerie nette, offrant un potentiel haussier en P1 et une défense relative en P2–P4. La part HBM et les contrats à long terme de SK Hynix offrent le levier bénéficiaire le plus élevé en P1, mais si les conditions d'offre, d'efficience et de financement se normalisent, bénéfices et multiples peuvent se comprimer conjointement.

Les résultats pondérés par les probabilités actuelles indiquent : <strong>jusqu'en 2027, les deux sociétés offrent un potentiel de hausse significatif ; en projetant jusqu'en 2028, la marge de sécurité ajustée au risque de Samsung est plus large.</strong> Pour que SK Hynix bénéficie d'une revalorisation supplémentaire, il faudra la confirmation que le rendement HBM4E, les conditions des contrats à long terme 2028 et le financement de l'infrastructure IA continuent de soutenir le scénario P1.

## Éléments Ne Pouvant Pas Encore Être Confirmés par des Sources Publiques

1. Le BPA par segment de Samsung Electronics pour 2027–2028 et la sensibilité à la normalisation Foundry
2. La pondération clients des contrats à long terme de SK Hynix, la formule de révision des prix et les conditions d'avances/minimums d'achat
3. Les entrées de wafers dédiées à l'HBM, les rendements en dies conformes et en empilements, ainsi que les volumes productibles par client pour les trois premiers fabricants de mémoire
4. La composition du capex 2028 des hyperscalers entre flux de trésorerie internes, obligations corporate et financements de projet
5. Les calendriers de refinancement de CoreWeave et Oracle et les marges de manœuvre sur les covenants
6. Les évolutions de capacité, de bande passante et de taux de résidence en mémoire de l'HBM4E par génération et par accélérateur
7. Les volumes réels d'expédition de CXMT/YMTC, les qualifications clients mondiales et la sensibilité du BPA par segment produit

## Sources Principales

- [Korea Investment & Securities, SK Hynix Preview 2T26, 2026-07-13](https://vo.la/fd9udR9)
- [Korea Investment & Securities, « Le départ commence maintenant », 2026-05-20](https://vo.la/jBPy7zV)
- [Korea Invest Insights, Modèle Offre-Demande HBM 2030 — Vérification croisée](/fr/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
- [AI 2040, Plan A](https://ai-2040.com/?choices=plan-a-root)
- [AI 2040, Supplément Calcul](https://ai-2040.com/supplements/compute-supplement)
- [AI 2040, Économie du Plan A](https://ai-2040.com/supplements/economics-of-plan-a)
- [Oracle Résultats Exercice 2026](https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/)
- [CoreWeave Formulaire 10-K 2025](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm)
- [CoreWeave DDTL 4.0 Formulaire 8-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/crwv-20260330.htm)

Les probabilités de scénarios et les valorisations présentées dans ce rapport sont des estimations analytiques fondées sur des informations accessibles au public et ne constituent pas un conseil en investissement personnalisé. Toute décision d'investissement effective doit tenir compte séparément de la volatilité des cours, de l'horizon de placement, de la fiscalité applicable, du risque de change et de la tolérance individuelle aux pertes.
