---
title: "Apple va-t-il vraiment utiliser CXMT ? Tests mémoire limités à la Chine et risque de prix pour les fabricants coréens de DRAM"
date: 2026-07-14T22:10:00+09:00
description: "Une vérification des faits sur les tests DRAM CXMT d'Apple, couvrant la technologie, les coûts, la réglementation et les risques de chaîne d'approvisionnement. Le scénario le plus plausible est une utilisation limitée dans les appareils standard vendus en Chine, le levier de négociation comptant potentiellement plus que les volumes directs."
categories: ["Analyse Exclusive", "Semi-conducteurs", "Vérification des Faits"]
tags: ["Apple", "CXMT", "LPDDR5X", "DRAM mobile", "Samsung Electronics", "SK Hynix", "Micron", "HBM", "Contrôles américano-chinois sur les semi-conducteurs"]
series: ["exclusive-analysis", "ai-hbm-2026"]
slug: "apple-cxmt-dram-china-test-memory-pricing-korea-2026-07-14"
valley_cashtags: ["Samsung Electronics", "SK Hynix", "Apple", "Micron"]
draft: false
---

Apple testerait actuellement des DRAM fabriquées par ChangXin Memory Technologies, ou CXMT, pour des appareils vendus en Chine. Aucun contrat de fourniture n'a été annoncé. Ces deux faits doivent être lus ensemble : CXMT a bien intégré le processus de qualification d'Apple, mais n'est pas devenu le principal fournisseur de mémoire pour les iPhone ou Mac à l'échelle mondiale.

> Contexte : Cet article fait suite à [l'introduction en bourse de CXMT et le risque de prix mémoire](/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/). Ce rapport soutenait que la capacité de CXMT est plus susceptible de plafonner les prix des DRAM client et LPDDR avant de perturber le marché HBM. Cet article examine comment un acheteur aussi important qu'Apple pourrait tirer parti de cette offre émergente. Les collections associées sont le [Hub AI HBM](/page/korea-semiconductor-hbm-kospi-hub/) et le [Hub Analyse Exclusive](/page/exclusive-analysis-hub/).

## Résumé

* Apple pourrait finalement qualifier CXMT comme fournisseur commercial. Le premier pas le plus plausible est un volume limité dans des appareils standard vendus en Chine. Un passage rapide vers les produits phares mondiaux reste peu probable.
* Les spécifications publiques LPDDR5X de CXMT sont suffisantes pour entrer en qualification. Ses produits à 8 533 Mbps et 9 600 Mbps sont en production de masse, tandis que la version à 10 667 Mbps reste en phase d'échantillonnage client. La consommation électrique, les performances thermiques, l'épaisseur du boîtier, les taux de défauts, la fiabilité à long terme et le rendement en gros volumes aux normes Apple demeurent non divulgués.
* Une décote de prix de vente moyen rapportée entre 5 % et 10 % ne règle pas la question économique. Cette estimation couvre le portefeuille DRAM mixte de CXMT, et non une offre LPDDR5X spécifique à Apple. La double nomenclature de composants, la séparation des stocks, la qualification et le risque de remplacement réglementaire réduisent les économies nettes.
* Le levier de négociation pourrait compter plus que les volumes directs. Un quatrième fournisseur capable de satisfaire une commande commerciale réelle pourrait faire pression sur Samsung, SK Hynix et Micron sur l'ensemble du carnet d'achats DRAM d'Apple, bien plus important.
* La pression concurrentielle de CXMT à court terme est concentrée dans la DRAM mobile et client, et non dans les HBM de pointe. Traiter ce rapport comme un signal négatif généralisé pour toutes les valeurs mémoire ignore la composition des produits.
* Les évaluations liées à cet événement sont : Watchlist pour SK Hynix, Attente pour Samsung Electronics et Attente pour Apple. Les preuves actuelles soutiennent des tests et des démarches réglementaires, non un contrat, un produit, un volume ou une durée divulgués.

## 1. Ce qui est confirmé et ce qui ne l'est pas

### 1.1 Les tests sont rapportés ; un contrat ne l'est pas

Le Financial Times a rapporté qu'Apple teste des DRAM de CXMT pour des appareils vendus en Chine. Des rapports antérieurs indiquaient qu'Apple avait sollicité une clarification réglementaire auprès du gouvernement américain. Apple, la Maison Blanche et CXMT n'ont pas répondu aux demandes de commentaires de Reuters à l'époque.

| Question | Évaluation au 14 juillet 2026 | Niveau de preuve |
|---|---|---|
| Apple teste-t-il des DRAM CXMT ? | Rapporté pour les appareils destinés au marché chinois | Reporting secondaire crédible |
| Un contrat de fourniture a-t-il été signé ? | Non confirmé | Bloqué |
| Quel produit est concerné ? | iPhone, iPad ou Mac ne peuvent être identifiés | Bloqué |
| Les puces seront-elles utilisées hors de Chine ? | Aucune preuve à l'appui | Ne pas inférer |
| Le gouvernement américain a-t-il approuvé l'utilisation ? | Une clarification réglementaire aurait été demandée | Aucune décision officielle |
| Les allocations des fournisseurs existants ont-elles été réduites ? | Non confirmé | Bloqué |

La formulation exacte est qu'Apple qualifie CXMT comme fournisseur potentiel, et non qu'il l'a déjà adopté. [Couverture Reuters](https://www.marketscreener.com/news/apple-seeks-approval-to-buy-chips-from-blacklisted-chinese-company-ft-reports-ce7f5fd9d08df72d), [résumé du rapport sur les tests](https://www.macrumors.com/2026/07/08/apple-begins-testing-controversial-chinese-memory/)

### 1.2 CXMT n'est plus un producteur expérimental

Counterpoint Research a estimé la part de revenus DRAM mondiale de CXMT à environ 8 % au T1 2026, le plaçant en quatrième position derrière Samsung, SK Hynix et Micron. Les chiffres de parts de marché varient selon que le dénominateur est le chiffre d'affaires, les expéditions en bits ou l'utilisation de tranches, mais la direction est claire : CXMT n'est plus un fournisseur de laboratoire à petite échelle. [Counterpoint Research](https://counterpointresearch.com/en/insights/global-dram-revenue-surges-to-near-dollar-100-billion-mark-in-q1-2026)

L'échelle ne prouve pas la maturité aux normes Apple. Fournir des DRAM de commodité à de grands clients chinois n'établit pas la consommation électrique, la fiabilité et le rendement requis dans les appareils premium d'Apple.

## 2. Performances : la qualification est plus difficile qu'atteindre une vitesse annoncée

CXMT indique que son portefeuille LPDDR5X comprend des puces de 12 Gb et 16 Gb, des boîtiers de 12 Go, 16 Go et 24 Go, et des débits de données allant jusqu'à 10 667 Mbps. Ses produits à 8 533 Mbps et 9 600 Mbps sont entrés en production de masse en mai 2025 ; la version à 10 667 Mbps reste en phase d'échantillonnage client. [Annonce CXMT](https://www.cxmt.com/en/news/info_19.html)

| Élément | Statut confirmé | Interprétation investissement |
|---|---|---|
| Densité de puce | 12 Gb et 16 Gb | Répond à une exigence d'entrée de gamme mobile et PC |
| Capacité du boîtier | 12 Go, 16 Go et 24 Go | Compatible avec les configurations d'appareils standard |
| Débit de données | 8 533, 9 600 et 10 667 Mbps | La pièce la plus rapide est encore en échantillonnage |
| Consommation | CXMT revendique 30 % d'économies vs son LPDDR5 | Pas une comparaison directe avec les trois grands |
| Qualification Apple | Non divulguée | L'adoption commerciale ne peut être établie |
| Rendement en gros volume | Non divulgué | Une fourniture de dizaines de millions d'unités ne peut être établie |

Les spécifications publiques réfutent l'affirmation selon laquelle la DRAM chinoise serait automatiquement trop lente pour Apple. Les vrais obstacles sont la consommation en veille et lors du rafraîchissement, la stabilité thermique, l'épaisseur du boîtier, les taux de défauts, la variation lot à lot, la fiabilité à long terme, le rendement en gros volume et l'intégration avec les processeurs et le firmware de gestion d'alimentation d'Apple.

CXMT a obtenu une place dans le processus de qualification. Les preuves publiques ne montrent pas qu'il peut maintenir la qualité aux normes Apple à grande échelle.

## 3. Prix : une décote de 5 % à 10 % ne règle pas la question économique

SemiAnalysis a estimé que le prix de vente moyen mixte des DRAM de CXMT au T1 2026 était environ 5 % à 10 % inférieur à celui du trio des fournisseurs établis, tandis que son coût par bit en DDR5 pourrait être supérieur de plus de 30 %. Ce sont des estimations sur l'ensemble du portefeuille de l'entreprise, et non des offres LPDDR5X spécifiques à Apple. [SemiAnalysis](https://newsletter.semianalysis.com/p/chinas-cxmt-is-set-to-challenge-dram)

| Coût supplémentaire | Charge pour Apple |
|---|---|
| Séparation des chaînes d'approvisionnement Chine et mondiale | Références distinctes, planification d'assemblage et logistique |
| Double inventaire | Décalage de la demande régionale et rotation plus lente |
| Ingénierie de qualification | Validation répétée du processeur, du firmware et thermique |
| Risque de remplacement réglementaire | Changement de fournisseur d'urgence et requalification |
| Défaillance qualité | Garantie, rappel et atteinte à la marque |

Une décote nominale se réduit après ces coûts. La tarification de CXMT ne doit pas non plus être interprétée comme la preuve d'un leadership structurel en matière de coûts. Le soutien de l'État, des exigences de marge inférieures, la composition des produits et la stratégie sur le marché domestique peuvent y contribuer.

## 4. Le levier de négociation peut compter plus que les volumes

L'avantage économique d'Apple ne se limite pas à la décote sur les puces achetées à CXMT. Qualifier un quatrième fournisseur capable de satisfaire une véritable commande commerciale pourrait influencer le prix de l'ensemble du carnet d'achats DRAM d'Apple.

```text
Maintenir la qualification CXMT
→ permettre une petite commande de production
→ démontrer une capacité de changement crédible
→ limiter les hausses de prix contractuels du trio des fournisseurs établis
```

Cet effet peut se manifester avant que CXMT ne gagne une part de marché visible. Une petite allocation supprime l'hypothèse des fournisseurs établis selon laquelle Apple n'a pas d'alternative.

Les seuls échantillons ne suffisent pas. L'option ne devient crédible que si CXMT peut livrer un volume commercial minimum dans un produit expédié. Sans contrat et sans volonté de changer, les fournisseurs établis ont peu de raisons de modifier leur tarification.

## 5. Réglementation : achetabilité légale et sécurité d'approvisionnement pluriannuelle sont deux choses différentes

### 5.1 Une désignation Section 1260H n'interdit pas automatiquement les achats commerciaux ordinaires

Le Département américain de la Défense a inclus CXMT dans sa liste Section 1260H du 8 juin 2026 des entreprises militaires chinoises. La désignation crée des risques liés aux contrats gouvernementaux et à la sécurité nationale, mais elle n'est pas une interdiction absolue de toutes les transactions commerciales privées ordinaires. [Communiqué du Département de la Défense américain](https://www.war.gov/News/Releases/Release/Article/4511232/dow-releases-list-of-chinese-military-companies-in-accordance-with-section-1260/)

### 5.2 Le risque de liste des entités compte surtout par la continuité de la production

Reuters a rapporté qu'un comité interagences avait approuvé l'ajout de CXMT à la liste des entités, mais que la publication restait en suspens à la mi-juin 2026. Une désignation sur la liste des entités imposerait de sévères restrictions de licences sur les exportations, réexportations ou transferts d'équipements, logiciels, technologies et services américains vers CXMT. L'achat d'une puce DRAM finie est légalement distinct de l'exportation de technologie américaine vers le producteur.

La conséquence commerciale reste importante. Des pièces de rechange restreintes, des mises à jour logicielles et un support d'ingénierie limité pourraient compromettre le rendement, la capacité et la migration vers des procédés avancés. Apple a besoin d'une continuité d'approvisionnement pluriannuelle, pas seulement de la capacité à effectuer un achat aujourd'hui. [Rapport Reuters sur le délai](https://www.investing.com/news/stock-market-news/us-holds-off-on-adding-deepseek-cxmt-to-trade-blacklist-reuters-reports-4746250)

### 5.3 La restriction fédérale des achats de 2027 n'est pas une interdiction à la consommation

Un règlement fédéral d'acquisition proposé mettrait en œuvre des restrictions à compter du 23 décembre 2027 sur les achats des agences fédérales de produits électroniques et de services contenant des puces visées provenant de CXMT, YMTC et SMIC. Il n'interdit pas aux consommateurs ordinaires d'acheter des iPhone. Il pourrait toutefois contraindre Apple à maintenir des configurations séparées sans CXMT pour les canaux gouvernementaux et certains canaux d'entreprise. La proposition comprend une exception jusqu'au 23 décembre 2028 pour les produits commerciaux sans alternatives. [Règle FAR proposée](https://public-inspection.federalregister.gov/2026-03065.pdf)

### 5.4 YMTC est le précédent politique pertinent

Apple avait exploré l'utilisation de NAND YMTC en 2022, mais avait abandonné le projet face à l'opposition du Congrès et au durcissement des restrictions. CXMT n'est pas dans la même position réglementaire aujourd'hui, mais cet épisode montre que la pression politique peut interrompre un plan d'approvisionnement techniquement plausible.

## 6. Le scénario le plus plausible : utilisation limitée dans les appareils standard vendus en Chine

Les modèles standard réservés à la Chine offrent un compromis entre ingénierie, économie et politique.

| Variable | Adoption limitée au marché chinois | Adoption mondiale principale |
|---|---|---|
| Qualification | Les produits standard peuvent être testés en premier | Longue validation sur l'ensemble des produits premium |
| Exposition réglementaire | Peut être séparé des canaux gouvernementaux américains | Conflits sur les ventes gouvernementales et d'entreprise |
| Opérations de la chaîne d'approvisionnement | Nomenclature Chine distincte | Perte plus importante de la mutualisation mondiale |
| Volume | Limité | Dizaines de millions d'appareils |
| Charge politique | Potentiellement gérable | Opposition américaine et risque de sanctions bien plus importants |
| Probabilité actuelle | Conditionnelle | Faible |

Quatre conditions doivent être réunies : qualification fiabilité Apple, rendement et volume chinois suffisants, continuité réglementaire sur la durée du contrat, et bénéfices nets supérieurs au coût du double approvisionnement.

## 7. Flux de capitaux et points d'étranglement

```text
Les investissements dans les centres de données IA augmentent
→ HBM et DRAM serveur reçoivent la priorité
→ l'offre de DRAM mobile et PC devient moins élastique
→ la facture mémoire d'Apple augmente
→ l'incitation à qualifier CXMT s'intensifie
```

La chaîne va des équipements et matériaux à la production de tranches CXMT, en passant par l'encapsulation et le test LPDDR5X, la qualification Apple, l'assemblage des appareils et la distribution en Chine. Les quatre points d'étranglement sont : qualité et rendement aux normes Apple, durabilité réglementaire, coût des configurations régionales séparées, et accès de CXMT aux équipements et au support technique américains.

## 8. Impact sur le secteur mémoire : distinguer HBM et DRAM mobile

La position concurrentielle actuelle de CXMT est plus proche de la DDR5 et LPDDR que des HBM de pointe. Extrapoler les tests d'Apple à un effondrement de l'ensemble du bassin de profits DRAM ignore l'économie par produit.

| Entreprise | Exposition directe à CXMT | Variable plus importante |
|---|---|---|
| Samsung Electronics | Pression potentielle sur les prix et parts de marché LPDDR chez Apple | Qualification HBM, composition produits, pertes fonderie |
| SK Hynix | Certaine exposition mobile, mais une plus grande partie de la thèse centrale vient du HBM | Rendement HBM4, parts, ASP, et capex IA |
| Micron | Pression potentielle sur la DRAM mobile et PC | DRAM serveur, montée en puissance HBM, accords long terme |
| Apple | Coût d'approvisionnement réduit et diversification des fournisseurs | Coût double-BOM, réglementation, marge brute totale |
| CXMT | La qualification Apple améliorerait la crédibilité mondiale | Rendement, coûts, accès aux équipements, sécurité réglementaire |

Une plus grande capacité CXMT dans le mobile pourrait inciter le trio des fournisseurs établis à allouer encore plus de capital aux HBM et à la DRAM serveur. Cela ferait pression sur les prix des produits de commodité sans éliminer les barrières de qualification, de rendement d'empilement, d'encapsulation et de feuille de route client propres au HBM.

Le risque à long terme est réel. Si CXMT améliore rapidement le rendement DDR5 avancé et LPDDR5X et absorbe les chocs du contrôle des exportations grâce à un écosystème d'équipements domestiques, les flux de trésorerie des produits de commodité des fournisseurs établis pourraient s'affaiblir. S'il parvient ensuite à atteindre un rendement HBM commercial, la frontière de produits actuelle s'éroderait. Les preuves publiques ne montrent pas encore ce résultat.

## 9. Trois cadres d'investissement et leurs équipes du diable

### Cadre 1 : adoption limitée au marché chinois

Classification : alpha événementiel idiosyncratique

* Prix : un prix d'approvisionnement CXMT inférieur
* Quantité : appareils sélectionnés vendus en Chine
* Coût : qualification, double inventaire, réglementation et risque de garantie

Les bénéficiaires incluent l'organisation des achats d'Apple, CXMT et la chaîne d'encapsulation et de matériaux en Chine. Les prix de la DRAM mobile Apple chez les fournisseurs établis feraient face à des pressions.

Équipe du diable : un accord durable États-Unis-Chine, un refuge réglementaire et une qualification sur les appareils premium pourraient briser l'hypothèse Chine uniquement. Un test de fiabilité raté invaliderait même l'adoption limitée.

### Cadre 2 : impact sur la négociation avant l'impact sur la part de marché

Classification : alpha événementiel idiosyncratique

* Prix : prix des contrats Apple avec le trio des fournisseurs établis
* Quantité : carnet d'achats DRAM complet d'Apple
* Coût : maintenir la qualification CXMT

Les investisseurs peuvent observer les parts des fournisseurs, mais le fournisseur marginal peut influencer les prix contractuels bien avant de gagner de larges parts.

Équipe du diable : un surplus mémoire forcerait les fournisseurs établis à baisser les prix sans CXMT. Un échec de qualification Apple rendrait également l'option non crédible.

### Cadre 3 : le risque CXMT est concentré dans la DRAM mobile et client

Classification : trading de composition de produits

* Prix : le plafond des prix de la DRAM mobile et PC
* Quantité : capacité CXMT et expéditions domestiques
* Coût : rendement sur nœud avancé et restrictions d'équipements américains

Les acheteurs de DRAM mobile et les fournisseurs à forte proportion de HBM sont des bénéficiaires relatifs. Les fournisseurs dépendants de la DRAM mobile Apple ou des hausses de prix des produits de commodité font face à plus de risques.

Équipe du diable : une progression rapide du rendement sur nœuds avancés et du HBM commercial affaiblirait la séparation des produits. Un effondrement des investissements dans les centres de données IA supprimerait également la défense relative du HBM.

## 10. Portes de surveillance spécifiques aux titres

Il s'agit d'évaluations événementielles conditionnelles, et non de recommandations d'achat indépendantes.

| Titre | Vue | P/E affiché au 14 juillet 2026 | Interprétation de l'événement |
|---|---|---:|---|
| SK Hynix | Watchlist | 16,97x | HBM4 et investissement IA comptent plus que le risque direct CXMT |
| Samsung Electronics | Attente | 20,99x | La pression sur les prix mobiles doit être pesée face à la reprise HBM |
| Apple | Attente | 38,38x | iPhone, services et marge brute totale comptent plus que les économies CXMT non prouvées |

Les chiffres P/E sont des valeurs affichées par [Google Finance pour Samsung](https://www.google.com/finance/quote/005930:KRX), [SK Hynix](https://www.google.com/finance/quote/000660:KRX) et [Apple](https://www.google.com/finance/quote/AAPL:NASDAQ). Le P/E historique peut surestimer le bon marché pour les entreprises mémoire cycliques proches d'un pic de profits.

### SK Hynix

Portes de confirmation : le calendrier de qualification et de production du HBM4 reste intact, les estimations de rendement et d'ASP HBM ne chutent pas, et la faiblesse du cours liée à CXMT survient sans dégradation des résultats HBM.

Invalidation : retard de qualification HBM4, diversification des clients réduisant les parts, ou CXMT atteignant un rendement commercial dans la DRAM serveur avancée ou le HBM.

### Samsung Electronics

Portes de confirmation : statut de fournisseur principal dans la prochaine génération d'Apple, utilisation de CXMT limitée au volume des appareils du marché chinois, et amélioration visible du rendement HBM et de la qualification client.

Invalidation : une allocation pluriannuelle matérielle des appareils Chine à CXMT, perte simultanée de parts LPDDR et de tarification, ou une reprise HBM trop lente pour compenser la pression mobile.

### Apple

Portes de confirmation : les prévisions de marge brute tiennent malgré l'inflation mémoire, la réglementation offre une clarté durable, et les estimations iPhone et services augmentent indépendamment de la diversification des fournisseurs.

Invalidation : la réglementation supprime l'option CXMT, l'inflation mémoire entraîne à la fois des hausses de prix et une faiblesse de la demande, ou un ralentissement de la croissance iPhone et services ne justifie plus la valorisation.

## 11. Preuves qui changeraient la thèse

Les preuves positives incluent une confirmation officielle de fournisseur Apple, une preuve de démontage de DRAM CXMT, une qualification au-delà des produits du marché chinois, un refuge durable aux États-Unis, ou un rendement en gros volume pour les produits à 10 667 Mbps et la prochaine génération de CXMT.

Les preuves négatives incluent un échec des tests de fiabilité Apple, une action de liste des entités interrompant le support des équipements, la fin de la qualification sans contrat, des coûts de double approvisionnement supérieurs aux économies, ou un surplus de DRAM supprimant le besoin d'un quatrième fournisseur pour Apple.

## 12. Classification des preuves

### Fait

* Apple testerait des DRAM CXMT pour les appareils du marché chinois.
* Apple aurait sollicité une clarification réglementaire américaine concernant CXMT.
* CXMT produit en masse du LPDDR5X à 8 533 Mbps et 9 600 Mbps et propose en échantillonnage un produit à 10 667 Mbps.
* Counterpoint a estimé la part mondiale de revenus DRAM de CXMT au T1 2026 à environ 8 %.
* CXMT figure sur la liste Section 1260H de juin 2026.
* La Section 1260H n'interdit pas en elle-même automatiquement les achats privés ordinaires.
* CXMT n'avait pas été formellement ajouté à la liste des entités à la mi-juin 2026.
* La règle FAR proposée met en œuvre une restriction d'achat fédéral le 23 décembre 2027 pour les semi-conducteurs visés.

### Inférence

* L'utilisation commerciale initiale se limiterait très probablement aux appareils standard vendus en Chine.
* Le plus grand avantage économique d'Apple pourrait être le levier de négociation avec les fournisseurs établis plutôt que des réductions directes sur les puces.
* La menace à court terme de CXMT est concentrée dans la DRAM mobile et client plutôt que dans le HBM.
* Des configurations séparées Chine et mondiales sont plus plausibles qu'un basculement mondial total.

### Spéculation

* Si les tests concernent iPhone, iPad ou Mac
* Calendrier de lancement commercial
* Volume initial et durée du contrat
* Si Washington fournira un refuge durable

### Bloqué

* Résultats internes de qualification d'Apple
* Tarification spécifique à Apple et décote par rapport aux fournisseurs établis
* Consommation électrique, épaisseur du boîtier, taux de défauts et fiabilité aux normes Apple
* Rendement au volume Apple et capacité mensuelle de CXMT
* Durée du contrat et volume minimum
* Parts et tarification exactes par produit chez les fournisseurs établis chez Apple

## Conclusion

Apple peut utiliser CXMT, mais le seul chemin rapporté aujourd'hui est celui des tests pour les appareils vendus en Chine. Les spécifications publiques justifient la qualification, tandis que la qualité aux normes Apple, le rendement en gros volume et la sécurité réglementaire pluriannuelle restent non prouvés.

La première variable de marché à surveiller n'est pas la part d'Apple chez CXMT. C'est de savoir si un quatrième fournisseur commercialement crédible modifie la tarification des contrats DRAM mobile pour le trio des fournisseurs établis. Cette pression est plus susceptible d'apparaître dans les segments LPDDR et DRAM client avant le HBM.

Il n'y a aucune raison de traiter toutes les valeurs mémoire coréennes de manière identique. Samsung doit équilibrer la pression sur les prix mobiles avec la reprise du HBM. Pour SK Hynix, le rendement HBM4 et la durabilité des investissements IA restent plus importants que CXMT. La prochaine décision devrait faire suite à une confirmation officielle de fournisseur, des démontages de produits, une décision sur la liste des entités et un volume commercial divulgué.
