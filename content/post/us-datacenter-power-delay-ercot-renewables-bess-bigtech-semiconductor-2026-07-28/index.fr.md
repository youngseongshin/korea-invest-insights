---
title: "Pourquoi les centres de données américains prennent du retard : la stratégie d’ERCOT et le calendrier pour la Big Tech et les semi-conducteurs"
slug: "us-datacenter-power-delay-ercot-renewables-bess-bigtech-semiconductor-2026-07-28"
date: 2026-07-28T21:45:00+09:00
description: "Une analyse vérifiée par les sources des retards des centres de données américains liés au raccordement au réseau, aux transformateurs, aux turbines et à l’opposition locale ; pourquoi ERCOT a réduit le risque avec 40.3 GW de solaire, 22.0 GW de batteries et 5.1 GW de réponse à la demande ; et ce que le goulot d’étranglement implique pour les actions Big Tech, GPU, HBM, mémoire et équipements électriques."
categories: ["Analyse exclusive", "Perspectives de marché", "Analyse technologique"]
tags:
  - "centres de données américains"
  - "infrastructure IA"
  - "réseau électrique"
  - "ERCOT"
  - "BESS"
  - "solaire"
  - "Big Tech"
  - "Nvidia"
  - "HBM"
  - "Samsung Electronics"
  - "SK hynix"
  - "équipements électriques"
  - "Research OS"
draft: false
---

> Contexte : Dans [la trilogie des résultats IA de la Big Tech](/fr/post/big-tech-ai-earnings-capex-roi-memory-2028-fcf-2026-07-22/), la question critique pour 2028 était de savoir si les dépenses d’investissement dans l’IA pouvaient se convertir en revenus et en flux de trésorerie disponible. Notre [classement des bénéficiaires coréens des centres de données](/fr/post/korea-ai-datacenter-beneficiaries-power-cooling-operator-flow-ranking-2026-07-23/) et notre [carte des goulots d’étranglement électriques des centres de données IA](/fr/post/ai-datacenter-power-bottleneck-korea-value-chain-screen-2026-07-04/) soutenaient que les fournisseurs d’électricité, de refroidissement et d’alimentation de secours monétisent plus tôt que les opérateurs. Ce rapport applique ce cadre aux États-Unis.

## TL;DR

- Les retards des centres de données américains sont réels, bien qu’aucun registre national unique ne puisse fournir un taux définitif d’annulation. Allianz Research a résumé qu’environ 12 GW de capacité américaine prévus pour 2026 pourraient être retardés ou annulés, avec seulement environ 5 GW en construction active. NERC a confirmé séparément que plusieurs régions avaient réduit leurs prévisions de grandes charges, car les raccordements et les mises en service progressaient moins vite que prévu.[^allianz][^nerc]
- Le goulot d’étranglement comporte quatre couches : <strong>le raccordement au réseau, les transformateurs et disjoncteurs, les équipements de production, ainsi que les permis locaux et la répartition des coûts</strong>. À la fin de 2025, 1,312 GW de production et 749 GW de stockage attendaient dans les files de raccordement américaines. Les délais de livraison des transformateurs élévateurs de générateurs dépassaient 160 semaines début 2026.[^lbl][^reuters-transformer]
- L’affirmation selon laquelle « plus de la moitié des États américains font l’objet d’alertes de pénurie » exagère l’évaluation officielle. NERC a constaté des ressources suffisantes dans toutes les zones dans des conditions normales de pointe estivale, tout en identifiant des risques élevés dans des conditions extrêmes dans certaines régions.[^nerc]
- ERCOT constitue une preuve solide en faveur de la thèse solaire-plus-stockage. NERC recense 40.3 GW de solaire et 22.0 GW de stockage par batteries chez ERCOT, avec des contributions attendues à la pointe de 29.7 GW et 20.7 GW. La probabilité d’une Energy Emergency Alert durant l’heure à risque maximal est passée de 3.1% à 0.43%.[^nerc]
- Mais ERCOT n’est pas une histoire de solaire et de batteries uniquement. Son résultat reflète également 5.1 GW de réponse à la demande, des charges de calcul interruptibles, des règles de marché plus rapides et une base existante de production au gaz, nucléaire et éolienne.
- Le solaire plus BESS est l’option d’approvisionnement incrémental la plus rapide pour les trois prochaines années, mais pas une solution complète 24/7. L’architecture pratique combine <strong>solaire+BESS, PPA nucléaires ou gaziers existants, moteurs à gaz ou piles à combustible derrière le compteur, et charges de calcul flexibles</strong>.
- Pour la Big Tech, les retards plafonnent la croissance à court terme mais augmentent la valeur de rareté de la capacité déjà mise sous tension. Pour les semi-conducteurs, ils créent à la fois un risque de calendrier des expéditions à court terme et une extension possible du cycle de demande 2027-2028.

<div class="thesis-callout">
  <div class="thesis-callout__label">Conclusion essentielle</div>
  <div class="thesis-callout__body">
    Le goulot d’étranglement de l’IA est passé des puces à l’électricité. La leçon d’ERCOT n’est pas « les renouvelables seules », mais un portefeuille d’ajouts rapides de ressources, de batteries, de raccordements flexibles, de réponse à la demande et de production garantie. Les effets sur les actions interviennent selon trois calendriers différents : un plafond de croissance à court terme pour la Big Tech, des installations de semi-conducteurs reportées à 2027-2028, et des commandes directes pour les fournisseurs d’équipements électriques et de stockage.
  </div>
</div>

## 0. Clarifions d’abord les définitions

La « capacité » d’un centre de données peut désigner la charge IT, la puissance totale de l’installation ou la taille finale annoncée du campus. Une « file d’attente » de raccordement peut concerner des projets de production ou de grandes charges. Les mélanger produit des chiffres impressionnants mais trompeurs.

| Affirmation courante | Vérification des éléments probants | Hypothèse de travail |
|---|---|---|
| La capacité actuelle des centres de données américains est de 50 GW | Les estimations varient selon le périmètre | Wood Mackenzie estime environ 24 GW actuellement et 110 GW d’ici 2030.[^reuters-transformer] |
| 30-50% des projets de 2026 sont retardés | Estimation sectorielle, pas un recensement officiel | Utiliser la direction, et non une estimation ponctuelle trompeuse. Allianz évoque 12 GW prévus contre environ 5 GW en construction.[^allianz] |
| La moitié des États américains fait face à des alertes de pénurie | Formulation plus forte que celle de NERC | Toutes les zones disposent de ressources suffisantes dans des conditions normales ; certaines régions font face à un risque élevé de conditions météorologiques extrêmes.[^nerc] |
| ERCOT a déjà dépassé 90 GW | Plus de 92 GW est une prévision | La prévision estivale d’ERCOT dépasse 92 GW ; les chiffres de planification de NERC ajustés de la réponse à la demande sont plus bas.[^kera][^nerc] |
| ERCOT dispose de 35 GW de solaire et 12 GW de BESS | Correct directionnellement mais obsolète | NERC recense 40.3 GW de solaire et 22.0 GW de BESS pour 2026.[^nerc] |
| La file d’attente américaine atteint 2.6 TW | Dépend de la date et du périmètre | Les files actives de production et de stockage atteignaient 2.061 TW à fin 2025. Il ne s’agit pas de la file d’attente des charges de centres de données elle-même.[^lbl] |

## 1. Quelle est l’ampleur du retard ?

Il n’existe pas de registre exhaustif des projets de centres de données américains. Un même campus peut avoir une capacité finale annoncée, une capacité plus faible pour le premier bâtiment et plusieurs dates de mise sous tension par phases. « Retardé », « annulé », « suspendu » et « terrain réservé sans alimentation » ne désignent pas la même chose.

Néanmoins, trois signaux indépendants convergent :

1. Allianz Research indique qu’environ 12 GW de capacité américaine prévus pour 2026 pourraient être retardés ou annulés, alors que seulement environ 5 GW sont en construction active.[^allianz]
2. NERC indique que plusieurs zones d’évaluation ont révisé à la baisse leurs prévisions de grandes charges parce que les raccordements et les mises en service étaient plus lents qu’attendu auparavant.[^nerc]
3. Data Center Watch, cité par des médias, a comptabilisé 75 projets représentant environ $130 billion bloqués ou retardés au premier trimestre 2026.[^dcwatch]

La conclusion défendable n’est pas que la moitié exacte disparaîtra. Elle est que la capacité IA annoncée progresse plus vite que la fourniture d’électricité et la construction, repoussant une portion importante de l’offre de 2026 à 2027 et au-delà.

## 2. Le goulot d’étranglement à quatre niveaux

| Niveau | Mesure vérifiée | Pourquoi cela compte |
|---|---:|---|
| Raccordement de production et de stockage | 2,061 GW actifs à fin 2025 ; délai médian jusqu’à l’exploitation supérieur à cinq ans pour les mises en service de 2025 | La nouvelle charge ne peut pas augmenter sans offre et transmission. |
| Raccordement des grandes charges | 36-48 months dans les zones de croissance des centres de données de PJM | Un bâtiment achevé ne peut pas monétiser sans date de mise sous tension. |
| Transformateurs et disjoncteurs | Transformateurs élévateurs au-delà de 160 weeks ; disjoncteurs haute tension autour de 125 weeks | Un seul composant manquant peut retarder toute une sous-station. |
| Permis, tarifs et opposition locale | 75 projets et $130 billion retardés ou bloqués au T1 2026 | L’eau, le bruit, le foncier et le transfert des coûts peuvent interrompre la construction. |

La file d’attente de production et de stockage comprend environ 8,200 projets. Seuls 13% de la capacité ayant déposé une demande entre 2000 et 2020 avait atteint l’exploitation commerciale à fin 2025.[^lbl] Le volume de la file d’attente n’est donc pas équivalent à l’offre future.

Les équipements constituent une contrainte physique plus immédiate. Reuters a rapporté que les délais de livraison des transformateurs élévateurs de générateurs dépassaient 160 semaines au premier trimestre 2026 et que ceux des disjoncteurs haute tension atteignaient 125 semaines. Les services publics commandent désormais des années à l’avance et prépaient parfois des créneaux de fabrication.[^reuters-transformer]

Les turbines à gaz ne constituent pas non plus une alternative instantanée. Mitsubishi Power a indiqué que les commandes s’étendent jusqu’en 2030 et que les délais d’installation sont passés à cinq ans ou plus.[^gas-turbine]

## 3. Le goulot d’étranglement est passé des racks aux sous-stations

La chaîne de monétisation est la suivante :

```text
Demande IA et contrat client
→ terrain et accord d’alimentation électrique
→ approbation de la production, de la transmission et de la sous-station
→ livraison du transformateur, de l’appareillage et du disjoncteur
→ achèvement du bâtiment, du refroidissement et de l’alimentation de secours
→ installation des GPU, du réseau et de la mémoire
→ mise en service
→ activation des charges de travail client
→ comptabilisation des revenus cloud et IA
```

Les ordonnances de juin 2026 de FERC adressées à six opérateurs régionaux de réseaux confirment que l’intégration des grandes charges est devenue un enjeu de politique nationale.[^ferc]

Mais le manque de production n’est qu’un mode de défaillance parmi d’autres. Une région peut disposer de centrales, mais pas de transmission. Elle peut disposer de transmission, mais pas de transformateurs. Elle peut disposer d’équipements, mais d’aucun accord sur la répartition des coûts. Et une charge rigide 24/7 exige davantage d’infrastructures qu’une charge capable de déplacer les tâches d’entraînement dans le temps ou selon les sites.

## 4. Ce qu’ERCOT a fait différemment

### 4-1. Le solaire et les batteries ont apporté une contribution mesurable

L’évaluation 2026 de NERC recense 40.3 GW de solaire et 22.0 GW de stockage par batteries chez ERCOT. Les contributions attendues à la pointe sont de 29.7 GW et 20.7 GW.

| Ressource ERCOT | Capacité nominale | Contribution attendue à la pointe | Taux de contribution |
|---|---:|---:|---:|
| Éolien | 40.6 GW | 9.45 GW | 23% |
| Solaire | 40.3 GW | 29.68 GW | 74% |
| BESS | 22.0 GW | 20.69 GW | 94% |

Le Texas a établi un record de production solaire de 29.3 GW et un record de décharge de batteries de 7.2 GW durant l’été 2025. Avec 8.78 GW de BESS ajoutés en 2025 et 2.68 GW supplémentaires jusqu’en mars 2026, la probabilité modélisée d’une Energy Emergency Alert durant l’heure à risque maximal est tombée de 3.1% à 0.43%.[^nerc]

Les batteries n’alimentent pas l’ensemble de l’État pendant des jours. Elles déplacent la production solaire de midi vers la soirée, réagissent aux déséquilibres soudains et stabilisent la fréquence.

### 4-2. L’offre ne représentait que la moitié de la réponse

ERCOT dispose de 5.1 GW de réponse à la demande disponible pour l’été 2026, en hausse de 54.9% sur un an. NERC indique que davantage de charges de calcul peuvent être réduites lors des urgences, ce qui abaisse sa prévision nette de demande interne de 3.7 GW.[^nerc]

```text
Le solaire couvre la demande diurne
→ les batteries franchissent la montée en charge du soir
→ le gaz, le nucléaire et l’éolien soutiennent l’offre garantie et nocturne
→ les grandes charges de calcul sont réduites lors de tensions
→ les signaux de marché rapides et les règles de raccordement attirent les ressources
```

Le risque plus faible d’ERCOT reflète une augmentation de 12% des ressources anticipées, davantage de BESS, davantage de réponse à la demande et des grandes charges flexibles. Ce n’est pas l’histoire d’une technologie unique.

### 4-3. Faiblesses persistantes

- L’heure à risque maximal est 21 heures, après la baisse de la production solaire.
- L’ouest lointain du Texas fait toujours face à des contraintes de transmission.
- Le déclenchement simultané de grandes charges électroniques peut déstabiliser la fréquence et la tension.
- Le chiffre de 92 GW est une prévision estivale, non un record réalisé.
- La capacité de puissance des batteries en GW ne dit pas grand-chose sur la survie à des épisodes de plusieurs jours de faible vent ou faible ensoleillement sans données de durée énergétique en GWh.

## 5. Le solaire plus BESS est-il la solution la plus rapide ?

Pour une puissance incrémentale au cours des trois prochaines années, oui. Pour une offre complète 24/7, non.

| Option | Vitesse jusqu’à la première alimentation | Fermeté 24/7 | Contrainte principale | Meilleur rôle |
|---|---|---|---|---|
| Solaire+BESS | Rapide | Moyenne | Terrain, transformateurs, durée, nuit | Puissance incrémentale rapide et soutien de pointe |
| Moteurs à gaz ou petites turbines sur site | Moyenne | Élevée | Gazoduc, permis d’air, coût du combustible | Alimentation transitoire et contournement de la file d’attente |
| Piles à combustible+BESS | Moyenne | Élevée | Approvisionnement en combustible, coût des équipements, service | Offre modulaire derrière le compteur |
| PPA nucléaire ou gazier existant | Rapide à moyen | Élevée | Transmission et structure contractuelle | Offre garantie |
| Nouveau cycle combiné au gaz | Lent | Élevée | Délai des turbines, pipelines, permis | Grande offre de long terme |
| Nouvelle transmission | Très lent | Élevée | Permis, foncier, répartition des coûts | Solution structurelle |
| SMR ou nouveau nucléaire | Très lent | Élevée | Autorisation, coût de construction, calendrier | Électricité garantie des années 2030 |
| Charge de calcul flexible | Le plus rapide | Pas une source d’approvisionnement | SLA et logiciels | Raccordement plus rapide sur le même réseau |

S&P Global a modélisé un centre de données de 627 MW et constaté qu’une conception solaire-plus-stockage coûtait plus de deux fois autant qu’une centrale à cycle combiné tout en ne garantissant toujours pas l’alimentation pendant des périodes de plusieurs jours de faible ensoleillement.[^spp-solar-gas] Cela n’invalide pas solaire+BESS. Cela définit son rôle comme capacité incrémentale et de pointe rapide plutôt que comme solution annuelle autonome.

L’architecture pratique est échelonnée :

1. <strong>Mise sous tension initiale :</strong> solaire, BESS, moteurs sur site ou piles à combustible, service réseau partiel et charges de travail batch flexibles.
2. <strong>Stabilisation :</strong> PPA à long terme avec du nucléaire, du gaz ou de l’hydroélectricité existants ; modernisation des sous-stations et de la transmission ; stockage de plus longue durée.
3. <strong>Offre structurelle :</strong> nouvelle production à cycle combiné, transmission, redémarrages nucléaires, géothermie, stockage de longue durée et, à terme, nucléaire avancé.

## 6. Les règles et les logiciels comptent autant que les équipements

Les ordonnances de juin de FERC demandent à PJM, MISO, SPP, CAISO, ISO-NE et NYISO de justifier ou de réformer les tarifs applicables aux grandes charges. Les options incluent la production colocalisée, le service de transmission flexible, la production derrière le compteur et le service temporaire de générateurs voisins.[^ferc]

L’actif émergent est le calcul interruptible.

| Charge de travail | Flexibilité électrique | Raison |
|---|---:|---|
| Inférence en temps réel | Faible | Les coûts de latence et d’interruption sont élevés. |
| Cloud d’entreprise | Faible à moyenne | Les SLA clients doivent être protégés. |
| Entraînement entre points de contrôle | Moyenne | De courtes pauses et des redémarrages peuvent être possibles. |
| Entraînement batch et prétraitement | Élevée | Le travail peut être déplacé dans le temps et entre les régions. |
| Minage de cryptomonnaies | Très élevée | La réduction de charge est relativement simple. |

Toute la demande IA n’est pas flexible. Mais si une partie d’un campus peut réduire sa charge, le réseau n’a plus besoin de construire chaque amélioration pour une pointe maximale entièrement coïncidente avant la première mise sous tension.

## 7. Impact sur les actions Big Tech

### 7-1. Canal négatif : la demande contractée se convertit plus lentement en revenus

```text
Retard de livraison d’électricité
→ retard d’activation du centre de données
→ la capacité de service GPU demeure contrainte
→ le backlog et les RPO se convertissent plus lentement
→ la croissance cloud à court terme est plafonnée
→ l’amortissement peut commencer avant une utilisation optimale
```

Si les terrains, les bâtiments et les acomptes sur équipements sont payés avant l’arrivée de l’électricité, le flux de trésorerie disponible est mis sous pression. La question du FCF de 2028 ne concerne donc pas seulement les dépenses d’investissement. Elle concerne la capacité mise sous tension et l’utilisation.

### 7-2. Canal positif : la valeur de rareté de la capacité active

Lorsque l’offre progresse moins vite que la demande, la capacité GPU déjà sous tension devient plus précieuse :

- Les remises peuvent diminuer.
- Les engagements à long terme et les prépaiements peuvent augmenter.
- Un taux d’utilisation élevé absorbe l’amortissement.
- Les opérateurs disposant d’une alimentation sécurisée et d’une diversification géographique gagnent des parts de marché.

Les retards de centres de données ne sont pas également négatifs pour tous les hyperscalers. Ils pénalisent les entreprises ayant d’importants projets non alimentés, tout en renforçant le pouvoir de fixation des prix des entreprises disposant de capacité sous tension.

### 7-3. Le nouveau tableau de bord de la Big Tech

| Indicateur | Signal positif | Signal négatif |
|---|---|---|
| Puissance mise sous tension | MW/GW et dates précis | Taille finale du campus uniquement |
| Approvisionnement électrique | PPA multirégionaux, production sur site, contrats réseau | Une seule utility et une date lointaine |
| Contrats clients | Engagements à long terme, prépaiements, utilisation minimale | Intérêt non contraignant |
| Phasage du capex | Investissement aligné sur la mise sous tension | Bâtiments et puces en attente d’électricité |
| Flexibilité | Charges de travail déplacées dans le temps et entre régions | Chaque charge traitée comme une demande rigide 24/7 |
| Flux de trésorerie | Les revenus et l’utilisation dépassent l’amortissement | L’amortissement et les intérêts augmentent d’abord |

La prochaine question lors des conférences de résultats devrait être : combien de gigawatts peuvent être activés, à quelle date, et quels revenus clients y sont attachés ?

## 8. Impact sur les actions de semi-conducteurs

### 8-1. Risque à court terme : un décalage entre commande et installation

Les hyperscalers peuvent soit accepter les GPU et HBM avant que l’électricité ne soit disponible, créant des stocks chez les clients, soit reporter les livraisons pour les aligner sur la mise sous tension, créant des creux trimestriels d’expédition.

Les signaux d’alerte incluent :

- L’augmentation des jours de stocks clients de GPU et de serveurs
- La baisse des prépaiements et l’allongement des calendriers de livraison
- Davantage de références à « l’attente d’électricité »
- Des expéditions d’ODM de serveurs progressant plus vite que la capacité cloud active
- Des contrats HBM restant intacts mais avec des dates de livraison trimestrielles reportées

La « demande différée » n’est pas automatiquement haussière.

### 8-2. Opportunité à moyen terme : une queue de cycle plus longue

Si les projets sont déplacés plutôt qu’annulés, la courbe de demande peut s’aplatir et s’allonger.

```text
La capacité des centres de données de 2026 glisse
→ les installations de GPU et HBM passent à 2027-2028
→ la croissance des expéditions en 2026 ralentit
→ les installations différées se superposent à la demande de remplacement et d’expansion
→ le pic peut être plus bas, mais le cycle dure plus longtemps
```

Cela exige trois conditions :

1. La demande finale en IA ne se détériore pas.
2. La capacité de financement et le crédit des hyperscalers restent intacts.
3. Les solutions électriques sont en construction plutôt que simplement annoncées.

Des retards répétés accompagnés d’une monétisation plus faible de l’IA transformeraient le report en annulation.

### 8-3. La performance par watt devient plus précieuse

| Couche de semi-conducteurs | Effet de la rareté électrique |
|---|---|
| GPU et AI ASIC | La performance par watt devient un critère d’achat plus important. |
| HBM | La baisse de l’énergie consacrée au mouvement des données et une utilisation accrue des accélérateurs augmentent sa valeur. |
| DRAM serveur | Le coût total de possession, y compris l’électricité et le refroidissement, compte davantage. |
| SSD d’entreprise | Un stockage basse consommation et à haut débit réduit le temps d’inactivité des GPU. |
| Réseaux | Les fabrics plus rapides commandent une prime en réduisant le temps d’inactivité des clusters. |
| Semi-conducteurs de puissance et substrats | La distribution et la conversion haute tension deviennent des parts plus importantes de la valeur système. |

Pour SK hynix, le canal positif réside dans l’avantage de performance par watt du HBM et de la DRAM serveur à forte valeur ajoutée. Samsung Electronics combine une reprise potentielle du HBM avec un portefeuille plus large de DRAM basse consommation et de SSD d’entreprise. Mais si les retards de mise sous tension créent des stocks de serveurs et de clients, l’exposition plus large aux produits de commodité peut également accroître la sensibilité.

## 9. Jugement boursier par groupe

| Groupe | Prochains 0-6 mois | Prochaines 1-3 années | Jugement |
|---|---|---|---|
| Hyperscalers | Les limites de capacité freinent la croissance ; la capacité active conserve son pouvoir de prix | L’accès à l’électricité devient une barrière défensive | Dispersion accrue entre entreprises |
| GPU et AI ASIC | Risque de calendrier des expéditions trimestrielles | Performance par watt et demande différée | Positif à moyen terme, volatil à court terme |
| HBM et mémoire serveur | Le rythme de livraison et les stocks clients comptent | Extension potentielle du cycle | Positif sous conditions |
| Équipements électriques | Backlog et pouvoir de prix demeurent solides | L’expansion des capacités peut créer de la concurrence plus tard | Bénéficiaire direct, la valorisation compte |
| BESS | Demande de pointe et derrière le compteur | Valeur de la durée plus longue et des logiciels | Bénéficiaire structurel |
| Turbines et moteurs | Commandes solides, livraisons lentes | Contraintes de pipelines et de permis | Backlog solide, revenus retardés |
| Nucléaire et géothermie | Contribution limitée à court terme | Prime de l’électricité garantie | Longue durée |

Les équipements électriques sont le bénéficiaire direct le plus évident, car transformateurs, disjoncteurs, appareillage, câbles et batteries résolvent les causes du retard. Mais un long backlog ne signifie pas automatiquement une action bon marché. L’expansion industrielle, les coûts des intrants, les acomptes et la concurrence après 2028 comptent toujours.

L’exposition des sociétés cotées coréennes reste la suivante :

- Réseau et distribution : LS ELECTRIC, HD Hyundai Electric, Hyosung Heavy Industries
- Câbles : Iljin Electric, Gaon Cable
- BESS et qualité électrique : LG Energy Solution, Samsung SDI, Vinatech
- Refroidissement : LG Electronics, GST
- Électricité garantie : Doosan Enerbility, SK Gas, GNC Energy

Consultez le [classement des bénéficiaires du 23 juillet](/fr/post/korea-ai-datacenter-beneficiaries-power-cooling-operator-flow-ranking-2026-07-23/) pour une sélection d’actions fondée sur les prix et les flux. Ce rapport se concentre sur la durée du goulot d’étranglement américain.

## 10. Tableau de bord mensuel

| Indicateur | Interprétation positive | Interprétation négative |
|---|---|---|
| MW de première alimentation pour les centres de données | Les plans deviennent de la capacité active | La taille finale augmente tandis que les dates glissent |
| Délai des grands transformateurs | Le goulot et le pouvoir de prix persistent | Les délais s’effondrent avec les annulations |
| Approbations de grandes charges ERCOT et PJM | Livraison d’électricité plus rapide | Les délais d’étude s’allongent de nouveau |
| Déploiement et durée des BESS | Meilleure couverture de la pointe du soir | GW élevés mais GWh insuffisants |
| Inscription à la réponse à la demande | Davantage de charge se raccorde au même réseau | Les préoccupations liées aux SLA réduisent la participation |
| Utilisation de la Big Tech et conversion des RPO | L’électricité et les clients arrivent ensemble | Les RPO augmentent mais la conversion ralentit |
| Stocks clients de GPU et HBM | La demande différée reste saine | Les puces s’accumulent sans électricité |
| Croissance cloud versus amortissement | Les revenus dépassent la base de coûts | L’amortissement dépasse la croissance |

## 11. Équipe rouge

Le scénario constructif échoue si :

1. Les retards reflètent une demande IA plus faible plutôt qu’un problème de calendrier électrique.
2. Les backlogs cloud et les prépaiements clients diminuent.
3. Les stocks de GPU et HBM s’accumulent et les volumes contractés sont annulés.
4. L’expansion de la production de transformateurs et de BESS crée un effondrement des prix en 2028.
5. L’opposition locale bloque simultanément la transmission, la production sur site et les renouvelables.

Le scénario baissier échoue si :

1. Les règles relatives aux charges flexibles et à la production colocalisée se standardisent rapidement.
2. Les contrats de réduction de charge de type ERCOT se propagent à PJM et MISO.
3. Des systèmes hybrides de solaire, stockage, moteurs et piles à combustible mettent sous tension de grands campus en deux ans.
4. Les hyperscalers publient des contrats clients à long terme assortis de dates fermes d’alimentation électrique.
5. Les contrats HBM et les prépaiements restent intacts malgré le report des calendriers de livraison.

## 12. Vue finale

Les centres de données américains ne sont pas retardés uniquement parce que le pays manque d’énergie. Les institutions et les équipements nécessaires pour raccorder, transformer, réduire la charge et répartir le coût de l’électricité évoluent plus lentement que la demande IA.

Le solaire plus BESS constitue la réponse incrémentale la plus rapide. ERCOT le démontre avec 40.3 GW de solaire, 22.0 GW de stockage par batteries, 50.4 GW de contribution attendue combinée à la pointe et une probabilité modélisée d’alerte d’urgence de 0.43%. Mais les mêmes éléments soulignent 5.1 GW de réponse à la demande et de charge de calcul interruptible.

Les implications boursières doivent être séparées dans le temps :

- <strong>Big Tech, court terme :</strong> la livraison d’électricité plafonne la croissance du cloud, tandis que la capacité sous tension bénéficie d’une valeur de rareté.
- <strong>Big Tech, moyen terme :</strong> l’électricité, l’utilisation et les contrats clients déterminent si le flux de trésorerie disponible de 2028 se redresse.
- <strong>Semi-conducteurs, court terme :</strong> les ajustements de livraison et les stocks clients créent de la volatilité.
- <strong>Semi-conducteurs, moyen terme :</strong> si le report ne devient pas une annulation, la demande de GPU et HBM peut s’étendre à 2027-2028 et prolonger le cycle.
- <strong>Bénéficiaires directs :</strong> transformateurs, disjoncteurs, appareillage, câbles, batteries et production sur site s’attaquent à la cause physique du retard.

La distinction décisive se situe entre les projets disposant de dates fermes d’alimentation et les annonces sans électricité, ainsi qu’entre la demande différée soutenue par des contrats clients et la demande qui disparaît.

> [Fait] Les sources publiques vérifient les indicateurs de retard, les classifications de risque de NERC, les ressources d’ERCOT, les files de raccordement et les délais des équipements.  
> [Inférence] Les arguments d’extension du cycle et de prix de rareté exigent que les contrats clients et la demande finale en IA se maintiennent.  
> [Bloqué] Les dates de mise sous tension au niveau des projets, l’économie de l’électricité derrière le compteur et les calendriers exacts d’installation des GPU restent largement privés.

Les travaux connexes sont regroupés dans le [hub Analyse exclusive](/fr/page/exclusive-analysis-hub/) et le [hub IA HBM](/fr/page/korea-semiconductor-hbm-kospi-hub/).

[^allianz]: [Allianz Research, Thinking fast, building slow: AI and the energy supply crunch](https://www.allianz.com/content/dam/onemarketing/azcom/Allianz_com/economic-research/publications/specials/en/2026/may/2026-05-12-ai-energy-AZ.pdf), May 12, 2026.
[^nerc]: [NERC, 2026 Summer Reliability Assessment](https://www.nerc.com/globalassets/our-work/assessments/nerc_sra_2026.pdf), May 2026.
[^lbl]: [Lawrence Berkeley National Laboratory, Queued Up: 2026 Edition](https://emp.lbl.gov/queues), July 2026.
[^reuters-transformer]: [Reuters, US power companies scramble to secure equipment as surging data center demand strains supplies](https://www.investing.com/news/stock-market-news/us-power-companies-scramble-to-secure-equipment-as-surging-data-center-demand-strains-supplies-4783319), July 9, 2026.
[^dcwatch]: [Tom's Hardware report citing Data Center Watch](https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-75-data-center-build-outs-worth-usd130-billion-have-been-successfully-blocked-in-the-first-four-months-of-2026-bipartisan-opposition-mounts-nationwide-over-fears-of-soaring-power-and-water-costs), June 13, 2026.
[^gas-turbine]: [S&P Global, Mitsubishi Power gas turbine orders stretch to 2030](https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/070326-interview-mitsubishi-power-gas-turbine-orders-stretch-to-2030-amid-ai-security-demand), July 3, 2026.
[^kera]: [KERA News, ERCOT predicts record summer energy demand](https://www.keranews.org/energy-environment/2026-06-04/ercot-predicts-record-summer-energy-demand), June 4, 2026.
[^ferc]: [FERC, FERC Launches Aggressive Targeted Action to Speed Large Load Integration](https://www.ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration), June 18, 2026.
[^spp-solar-gas]: [S&P Global Market Intelligence, Data center power: Combined-cycle plant outperforms solar plus battery](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/03/data-center-power-combined-cycle-plant-outperforms-solar-plus-battery), March 2026.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
