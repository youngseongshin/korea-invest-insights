---
title: "OpenEdges Technology : potentiel des IP mémoire LPDDR6 et LPDDR5X sur Samsung 4/5/8nm"
slug: semiscope-openedges-samsung-lpddr6-ip-option-2026-04-30
aliases: ["/en/post/semiscope-openedges-samsung-lpddr6-ip-option-2026-04-30/"]
date: 2026-04-30T12:00:00+09:00
description: "OpenEdges Technology (394280 KQ) offre un angle ciblé pour analyser la demande d'IP de sous-système mémoire LPDDR5X/LPDDR6 sur les nœuds Samsung 4/5/8nm. Ce suivi SemiScope passe en revue le fossé produit, la structure des filiales, la dilution, la valorisation et les jalons nécessaires avant tout renforcement de position."
categories: ["Chaîne d'approvisionnement tech coréenne", "IP semi-conducteur"]
tags: ["OpenEdges Technology", "394280", "SemiScope", "Samsung Foundry", "LPDDR6", "LPDDR5X", "DDR PHY", "Contrôleur mémoire", "NoC", "OpenEdges Square", "Fabless coréen", "IP semi-conducteur"]
series: ["semiscope-2026"]
---

> **Suivi SemiScope.** La première note consacrée à OpenEdges présentait la société comme la rare plateforme d'IP de sous-système mémoire coréenne, adossée à une longue courbe en J de redevances. Cette deuxième analyse resserre la question investissable : OpenEdges Technology n'est pas avant tout une « valeur NPU ». C'est une option sur IP de sous-système mémoire LPDDR5X/LPDDR6 pour les nœuds Samsung 4/5/8nm, et le titre ne mérite une pondération plus élevée que lorsque les victoires de licences, la reconnaissance de revenus, la progression des redevances et la maîtrise des coûts commencent à valider cette option.

---

## Lectures associées

- [SemiScope : OpenEdges Technology — La plateforme d'IP de sous-système mémoire coréenne avec une option sur courbe en J de redevances](/post/semiscope-openedges-technology-ip-platform-2026-04-25/)
- [SemiScope : Trois valeurs coréennes ATE et IP mémoire reclassées — Pourquoi Exicon est le trade de la courbe en J 2026, pas la deuxième chance](/post/semiscope-neosem-exicon-openedge-rerank-2026-04-25/)

---

## En bref

1. **OpenEdges se comprend mieux comme une société d'IP de sous-système mémoire que comme une société NPU.** Le prisme d'investissement central est le PHY LPDDR5X/LPDDR6, le contrôleur mémoire et le NoC, le tout packagé pour les ASIC IA, l'IA embarquée, l'automobile et les puces gourmandes en données.
2. **Le Samsung Foundry 4/5/8nm est le vrai terrain de jeu.** Le titre n'est pas un pari sur la victoire d'OpenEdges face à Synopsys ou Cadence à la frontière mondiale des 2/3nm. C'est un pari sur le fait que les nœuds milieu-avancés à fort volume de Samsung ont besoin d'une IP LPDDR locale, crédible et adaptée au procédé.
3. **La chaîne de valeur est encore précoce : portage, licence, tape-out, validation silicium, production, redevances.** OpenEdges a dépassé le stade de pure R&D, mais n'est pas encore une plateforme de redevances mature.
4. **TSS et la filiale japonaise renforcent la base technologique. OpenEdges Square est une option à risque plus élevé.** TSS et Japan sont des filiales à 100 % dédiées au PHY DDR et à la profondeur du contrôleur mémoire. Square est plus intéressante mais aussi plus dilutive, car la maison mère en détient environ 65 %.
5. **La valorisation anticipe déjà beaucoup.** Une capitalisation boursière d'environ KRW 530 Mds face à un chiffre d'affaires 2026E d'environ KRW 30,4-31,8 Mds implique environ 16,7x-17,5x les ventes. Ce niveau ne se justifie que si les victoires LPDDR6/5X, la montée en charge des revenus au 2T-3T, la discipline sur les coûts et l'avancement des redevances se matérialisent.

**Conclusion :** OpenEdges reste un candidat **Liste de surveillance / Ligne pilote**. Une position pilote de 0,3 %-0,5 % peut se justifier pour les investisseurs souhaitant s'exposer à la couche IP des semi-conducteurs coréens. Passer au-dessus de 1 % devra attendre des victoires répétées sur LPDDR6/5X, une montée en charge visible des revenus, une réduction de la charge de coûts fixes et une meilleure visibilité sur OpenEdges Square.

---

## 1. Ce que cette note ajoute à la première analyse SemiScope d'OpenEdges

La première note SemiScope posait le cadre général : OpenEdges Technology (394280 KQ) est la rare plateforme d'IP semi-conducteur coréenne, regroupant sous un même toit contrôleur mémoire, DDR PHY, NPU, NoC, UCIe et IP mémoire adjacente au CXL. Cette thèse tient toujours.

Mais le suivi le plus utile est plus ciblé.

Le marché voulait souvent étiqueter OpenEdges comme une valeur « semi-conducteur IA » ou « NPU ». C'est trop vague. L'actif le plus investissable de la société n'est pas le NPU en tant que tel. C'est le chemin mémoire autour du calcul IA :

`DRAM - DDR PHY - Contrôleur mémoire - NoC - NPU / CPU / Accélérateur`

Pour un ASIC IA ou une puce d'inférence embarquée, le calcul n'est pas le seul goulot d'étranglement. Le déplacement des données peut être tout aussi déterminant. Si l'interface mémoire est lente, énergivore ou instable, les TOPS théoriques de la puce importent peu. C'est pourquoi l'IP de PHY et de contrôleur LPDDR5X/LPDDR6 peut devenir stratégique.

La thèse révisée est la suivante :

> OpenEdges est une option d'achat sur les clients ASIC IA et embarqués Samsung 4/5/8nm ayant besoin d'une IP de sous-système mémoire LPDDR5X/LPDDR6 éprouvée.

Cette formulation compte. Elle préserve le potentiel haussier tout en éliminant l'exagération. La société n'est pas encore un champion mondial de l'IP. Elle n'est pas encore une capitalisation de qualité à croissance composée. C'est un éditeur d'IP à forte intensité R&D avec une chance crédible de devenir la couche de sous-système mémoire domestique pour une partie de la clientèle Samsung Foundry.

---

## 2. Recadrer le produit : le NPU n'est pas au centre

OpenEdges possède et développe plusieurs blocs d'IP :

| Famille de produits | Fonction | Signification pour l'investisseur |
|---|---|---|
| **DDR PHY** | Couche de signal physique entre le SoC et la DRAM | Barrière technique la plus élevée ; hard IP spécifique au nœud ; nécessite une validation silicium |
| **Contrôleur mémoire DDR** | Contrôle l'accès mémoire, l'ordonnancement et le comportement protocolaire | Plus précieux lorsqu'il est couplé au PHY |
| **Interconnexion sur puce / NoC** | Déplace les données à l'intérieur du SoC | Plus important à mesure que les ASIC IA ajoutent des blocs de calcul |
| **NPU / ENLIGHT** | Accélération de l'inférence IA | Utile, mais thèse d'investissement plus faible en standalone |
| **Contrôleur UCIe / chiplet** | Communication die-to-die pour les systèmes chiplets | Option à long terme avec l'adoption des chiplets |
| **IP mémoire adjacente CXL** | Blocs de contrôleur mémoire et PHY utilisés par de potentiels concepteurs de puces contrôleur CXL | Exposition CXL indirecte, sans visibilité de revenus comparable à l'équipement |

La version la plus forte de la société n'est pas « nous vendons un NPU ». C'est « nous réduisons les goulots d'étranglement mémoire dans les puces IA en vendant un sous-système mémoire packagé ».

C'est aussi là qu'apparaissent les coûts de changement. Un bloc d'IP soft standalone peut souvent être remplacé. Une combinaison PHY + contrôleur + NoC intégrée, vérifiée et temporisée à l'intérieur d'une puce est bien plus difficile à remplacer. Le calendrier de tape-out du client, son plan de vérification, son budget énergétique et la fermeture temporelle peuvent tous en être affectés.

C'est pourquoi ce titre doit être distingué des valeurs d'équipement comme NeoSem et Exicon. Ces sociétés peuvent convertir des commandes en revenus en six à neuf mois environ. OpenEdges vend de l'IP de conception en amont. Son retour prend plus de temps, mais le potentiel de redevances peut être plus durable si les puces clientes atteignent la production de masse.

---

## 3. La chaîne de valeur IP : ne pas confondre portage et redevances

La séquence opérationnelle la plus importante est :

`Portage - victoire de licence - tape-out client - validation silicium - production - redevances`

OpenEdges a progressé au-delà du stade « technologie sans intérêt client ». Son document IR 2026 fait état de plus de 30 clients, 71 contrats de licence cumulés, plus de 20 produits IP commercialisables et un effectif d'environ 170 personnes dont quelque 149 en R&D. Ce n'est pas le profil d'une société fictive.

Mais il est tout aussi important de ne pas passer trop vite de « portage » à « plateforme de redevances ».

| Étape | Ce que cela prouve | Ce que cela ne prouve pas encore |
|---|---|---|
| Portage | L'IP peut être adaptée à un nœud de procédé cible | Un client payant l'a adoptée |
| Victoire de licence | Le client s'est engagé à utiliser ou évaluer l'IP | La puce passera le tape-out avec succès |
| Tape-out | Le design client est passé en fabrication | Le silicium satisfera les exigences de production |
| Validation silicium | L'IP fonctionne en vrai silicium | Le client livrera de forts volumes |
| Production | La puce cliente est commercialisée | L'échelle des redevances dépend encore du volume unitaire |
| Redevances | Le modèle présente une économie composée | La pérennité dépend de design-ins répétés |

La part des redevances reste faible. Les documents antérieurs d'OpenEdges et les analyses sell-side indiquent des revenus de redevances ne représentant qu'une infime part des ventes récentes. Une prévision 2026 place les redevances à environ KRW 1,7 Mds pour KRW 30,4 Mds de revenus totaux, soit environ 5,6 %.

Cette fourchette de 5-6 % est un progrès par rapport au niveau du 1S25, mais n'est pas encore la courbe de type ARM que les investisseurs espèrent in fine. Pour que ce titre se reclasse en véritable capitalisation IP de qualité, je souhaiterais voir la part des redevances progresser vers 20 % des revenus trimestriels et continuer à croître.

---

## 4. Pourquoi le Samsung 4/5/8nm est déterminant

L'expression « Samsung 4/5/8nm » ne doit pas être lue comme une vague histoire d'écosystème Samsung. Elle est précise.

Le raccourci incorrect est :

> OpenEdges a pré-porté LPDDR6 sur l'ensemble des nœuds Samsung 4-8nm.

La version plus juste est :

> OpenEdges élargit sa couverture autour du LPDDR6 Samsung 4nm et du LPDDR5X haute vitesse Samsung 4/5/8nm, ciblant les clients ASIC IA, embarqué, automobile et autres ayant besoin de meilleures interfaces mémoire sur les nœuds à fort volume de Samsung Foundry.

D'après la feuille de route IR 2026 citée dans les sources, OpenEdges couvre déjà le Samsung 5nm LPDDR5X/LPDDR5/LPDDR4X/LPDDR4. Le Samsung 8nm LPDDR5X figurait comme élément de développement pour le 1S26, tandis que le Samsung 4nm LPDDR5X 10,7 Gbps et le LPDDR6 14,4 Gbps étaient indiqués comme éléments de développement pour le 2S26.

C'est le bon terrain de jeu pour OpenEdges.

La frontière des 2/3nm est dominée par les géants mondiaux. Synopsys, Cadence, Arm, Rambus et les autres leaders en IP d'interface bénéficient d'un soutien terrain plus profond, de relations foundry plus larges et de références sur nœuds avancés plus nombreuses. Il n'est pas réaliste de miser sur OpenEdges comme vainqueur mondial à court terme à cette couche.

L'opportunité plus réaliste se situe sur le marché grand volume milieu-avancé :

- IA on-device ;
- puces IA automobiles ;
- contrôleurs IA pour robots et applications industrielles ;
- puces IoT et maison connectée ;
- ASIC de caméra de sécurité et de vision ;
- puces défense et usage spécial ;
- projets domestiques d'accélérateurs IA ;
- programmes ASIC turnkey menés par des design houses.

Ces clients n'ont pas toujours besoin du procédé 2/3nm le plus coûteux. Ils peuvent accorder plus d'importance au coût, à la consommation, à la bande passante mémoire, au support local, à la réduction des risques et à la disponibilité du procédé Samsung. C'est là qu'un éditeur domestique d'IP de sous-système mémoire peut faire la différence.

La question centrale est :

> Le vivier de clients Samsung 8nm et en dessous ayant besoin de LPDDR5X ou LPDDR6 est-il suffisamment large pour générer des victoires de licences répétées pour OpenEdges ?

Si oui, le titre a un chemin clair vers un récit de meilleure qualité. Si non, la société reste un éditeur d'IP techniquement intéressant mais financièrement sous tension.

---

## 5. Le fossé concurrentiel au sein de la chaîne de valeur Samsung

Le problème de Samsung Foundry n'est pas seulement la technologie de procédé. Il lui faut aussi un écosystème plus dense : IP, EDA, design houses, références de vérification et support client. OpenEdges peut contribuer à renforcer une couche de cette pile.

| Maillon de la chaîne de valeur Samsung | Besoin de Samsung | Rôle d'OpenEdges |
|---|---|---|
| Samsung Memory | Adoption DRAM LPDDR5X/LPDDR6 | Bénéficiaire indirect d'une adoption LPDDR plus large |
| Samsung Foundry | Plus de victoires clients sur 4/5/8nm | Fournit une IP d'interface mémoire adaptée au procédé |
| SAFE / écosystème IP | Réduction du risque de conception client | Ajoute des options domestiques de PHY, contrôleur et NoC |
| Design houses | Packages ASIC turnkey | Peut s'insérer dans des flux de conception récurrents |
| Clients fabless / ASIC | Tape-out plus rapide avec risque mémoire réduit | Résout les goulots d'étranglement mémoire haute vitesse basse consommation |

La première couche de fossé est le **portage DDR PHY**. Le PHY n'est pas un logiciel générique. C'est un bloc d'IP dur avec une complexité analogique et mixte. À des vitesses de 8,5-14,4 Gbps, l'intégrité du signal, la gigue, le bruit, la variation de tension et de température, la marge temporelle et les algorithmes d'entraînement comptent. Un bloc d'IP uniquement simulé ne suffit pas. Les clients veulent une validation silicium.

La deuxième couche de fossé est le **bundling PHY + contrôleur + NoC**. Les clients ASIC IA ne cherchent pas simplement un brochage d'interface. Ils ont besoin d'un système de déplacement des données fonctionnel. Si OpenEdges peut vendre le chemin mémoire comme un bundle, cela crée un coût de changement plus élevé qu'un bloc unique ne peut créer seul.

La troisième couche de fossé est **l'effet de levier du canal design house**. Si une design house utilise régulièrement l'IP OpenEdges dans des projets Samsung turnkey, OpenEdges n'a pas besoin de vendre à chaque client individuellement. L'IP peut faire partie d'un package réplicable.

Le fossé n'est pas absolu. Il est local et spécifique au procédé. Mais des fossés locaux et spécifiques peuvent tout de même générer des rendements attractifs sur les marchés publics lorsque la base de revenus est faible.

---

## 6. Filiales : ce qui appartient aux actionnaires ?

La structure des filiales est importante car OpenEdges n'est pas seulement une entité cotée avec une ligne de produit unique et limpide. Le document IR 2026 décompose le groupe entre la maison mère et les principales filiales.

| Entité | Participation de la mère | Rôle principal | Lecture investissement |
|---|---:|---|---|
| **Maison mère OpenEdges Technology** | - | R&D IP, ventes et stratégie de plateforme intégrée | Activité cotée principale |
| **The Six Semiconductor (TSS)** | 100 % | R&D IP DDR PHY | Renforce le fossé technique clé |
| **OpenEdges Technology Japan** | 100 % | R&D IP contrôleur mémoire et capacité orientée Japon | Renforce la profondeur contrôleur et l'accès aux talents régionaux |
| **OpenEdges Square** | environ 65 % | Plateforme de vente d'IP en ligne, CC NoC et options de plateforme futures | Option à risque plus élevé ; la hausse n'appartient pas entièrement à la maison mère |

TSS doit être considérée comme un actif de fossé, non comme une dilution. Le DDR PHY est la partie la plus difficile de la pile. Si TSS approfondit la capacité PHY haute vitesse, les retombées économiques reviennent à la maison mère puisqu'elle est détenue à 100 %.

La filiale japonaise est similaire. L'IP de contrôleur mémoire est moins lourde en analogique que le PHY, mais elle est proche de l'architecture client et des exigences produit. Le Japon dispose également d'une profondeur d'ingénierie semi-conducteur et de relations clients pertinentes. Là encore, la filiale étant détenue à 100 %, le sujet est le coût, non la fuite de valeur.

OpenEdges Square est différente.

Square n'est pas simplement une branche d'ingénierie. Elle a été lancée avec des ambitions de plateforme de vente d'IP en ligne et autour du développement du CC NoC. Le CC NoC, ou réseau sur puce à cohérence de cache, peut devenir précieux si les ASIC IA multicœurs requièrent un déplacement interne des données et un comportement de cohérence de cache plus sophistiqués.

L'option est intéressante. La propriété est moins nette. Si la maison mère détient environ 65,4 % de Square, l'exposition transparente d'un actionnaire d'OpenEdges à Square n'est que 65,4 % de sa participation dans la maison mère.

Exemple :

`1,0 % de participation dans la mère x 65,4 % de participation dans Square = 0,654 % d'exposition transparente à Square`

Ce n'est pas automatiquement négatif. Des capitaux externes peuvent réduire la charge de trésorerie de la mère et accélérer le développement. Mais cela signifie que le succès de Square ne revient pas à 100 % aux actionnaires cotés.

Je traiterais Square comme une option d'achat avec deux questions :

1. Le CC NoC peut-il devenir un vrai produit commercial plutôt qu'une histoire de développement ?
2. Les besoins en coûts et en financement de Square peuvent-ils rester suffisamment maîtrisés pour que l'option n'affaiblisse pas le compte de résultat de la maison mère ?

---

## 7. Dilution et financement : l'émission de CPS 2026

OpenEdges a levé environ KRW 20,0 Mds en mars 2026 via une attribution à des tiers d'actions préférentielles convertibles. Les chiffres clés figurant dans les sources sont :

| Élément | Chiffre |
|---|---:|
| Nouvelles actions préférentielles | 1 145 278 |
| Actions ordinaires existantes avant émission | 26 276 655 |
| Augmentation potentielle du nombre d'actions ordinaires | 1 145 278 |
| Impact déclaré sur le nombre d'actions | 4,18 % |
| Prix d'émission | KRW 17 463 |
| Prix de référence | KRW 17 054 |
| Prime par rapport au prix de référence | 2,4 % |
| Période de conversion | 8 avr. 2027 – 8 avr. 2031 |
| Plancher du prix de conversion | KRW 12 225 |

Le calcul de dilution est :

`1 145 278 / (26 276 655 + 1 145 278) = 4,18 %`

Il s'agit d'une dilution réelle. Elle ne doit pas être ignorée. Les points atténuants sont que l'émission s'est faite avec une prime par rapport au prix de référence et que les liquidités prolongent le runway de R&D.

Le risque réside dans le refixing. Si le cours de l'action baisse et que le prix de conversion s'ajuste vers le plancher, la dilution effective peut augmenter. Pour une société qui finance encore sa R&D en amont de redevances matures, le coût du capital reste un élément central de la thèse.

---

## 8. Valorisation : le titre anticipe déjà un avenir meilleur

Sur la base du snapshot de marché aux alentours du 29 avril 2026, OpenEdges s'échangeait près de KRW 20 150 avec une capitalisation boursière d'environ KRW 530,9 Mds. Rapporté à des hypothèses de revenus 2026E d'environ KRW 30,4-31,8 Mds, le multiple de ventes est élevé.

| Base de revenus | Calcul | PSR implicite |
|---|---:|---:|
| Revenus 2026E KRW 30,4 Mds | KRW 530,9 Mds / KRW 30,4 Mds | **17,5x** |
| Revenus 2026E KRW 31,8 Mds | KRW 530,9 Mds / KRW 31,8 Mds | **16,7x** |

Ce n'est pas une petite capitalisation cyclique bon marché. C'est une option coûteuse sur un modèle économique futur meilleur.

Le marché anticipe déjà plusieurs éléments :

- les revenus 2026 passent au-dessus de KRW 30 Mds ;
- la société approche l'équilibre au 2S26 ou en 2027 ;
- les victoires LPDDR6/5X deviennent répétables ;
- l'activité clients Samsung 4/5/8nm s'améliore ;
- OpenEdges Square contribue en valeur d'option plutôt qu'en pur coût ;
- les redevances deviennent progressivement visibles.

C'est un scénario exigeant. La bonne conclusion n'est pas « éviter ». La bonne conclusion est « ne pas renforcer avant que la société ait prouvé suffisamment de sa feuille de route ».

---

## 9. Cadre d'investissement

### Idée 1 — IP de sous-système mémoire LPDDR Samsung 4/5/8nm

| Élément | Point de vue |
|---|---|
| Logique centrale | Les clients Samsung Foundry 4/5/8nm ont besoin d'une IP PHY et contrôleur LPDDR5X/LPDDR6 haute vitesse |
| Levier prix | Une IP LPDDR avancée peut faire progresser l'ASP |
| Levier volume | Plusieurs nouvelles licences ou une à deux victoires lighthouse majeures |
| Levier coût | La croissance des coûts fixes R&D doit ralentir |
| Point de blocage | Portage PHY spécifique au procédé et validation silicium |
| Erreur de marché | Traiter OpenEdges comme une pure valeur NPU |
| Scénario baissier | Le vivier de clients Samsung ne s'élargit pas suffisamment |
| Confirmation | Victoires répétées LPDDR6/5X, tape-out ou validation silicium sur Samsung 4nm |

### Idée 2 — TSS et DDR PHY comme véritable fossé

| Élément | Point de vue |
|---|---|
| Logique centrale | Le PHY est la partie la plus difficile de la pile de sous-système mémoire |
| Levier prix | Un PHY haute vitesse validé peut commander de meilleures conditions économiques |
| Levier volume | Couverture sur Samsung et certains nœuds TSMC |
| Levier coût | Les talents R&D haut de gamme doivent être retenus sans consommation incontrôlée |
| Point de blocage | PHY validé en silicium sur les nœuds cibles |
| Erreur de marché | Traiter le PHY comme une IP numérique réutilisable ordinaire |
| Scénario baissier | Synopsys/Cadence ripostent agressivement sur les nœuds Samsung grand volume |
| Confirmation | Validation LPDDR6 4nm et LPDDR5X 8nm et adoption client |

### Idée 3 — OpenEdges Square et CC NoC

| Élément | Point de vue |
|---|---|
| Logique centrale | Les ASIC IA multicœurs pourraient avoir besoin de solutions NoC à cohérence de cache |
| Levier prix | Le CC NoC pourrait constituer une couche d'IP à plus haute valeur ajoutée |
| Levier volume | Adoption par les clients ASIC IA et design houses |
| Levier coût | Les dépenses de développement de la plateforme doivent être maîtrisées |
| Point de blocage | Lancement commercial du CC NoC et premières victoires de design |
| Erreur de marché | Voir Square uniquement comme un centre de coûts |
| Scénario baissier | Les revenus sont retardés tandis que la charge de coûts augmente |
| Confirmation | Lancement 2026, premier client, économie claire pour la maison mère |

---

## 10. Positionnement : Liste de surveillance / Ligne pilote

Pour l'instant, je classerais OpenEdges dans le bucket **Liste de surveillance / Ligne pilote**.

Le titre est investissable en petite position exploratoire car le chemin haussier est clair et la couche stratégique adressable est réelle. Mais la valorisation actuelle est trop élevée pour un renforcement aveugle. La société doit démontrer que sa feuille de route technologique peut se transformer en contrats répétables et en revenus reconnus.

### Conditions pour augmenter l'exposition

J'envisagerais de passer d'une position pilote de 0,3 %-0,5 % vers 0,5 %-0,7 % si au moins deux des éléments suivants se produisent :

1. victoires supplémentaires de licences LPDDR6/5X ;
2. revenus trimestriels du 2T26 ou 3T26 supérieurs à KRW 7,0 Mds ;
3. coûts fixes trimestriels se rapprochant de la fourchette KRW 7,0-8,0 Mds ;
4. divulgation d'un tape-out ou d'une validation silicium LPDDR6 Samsung 4nm ;
5. les victoires via le canal design house deviennent plus visibles ;
6. OpenEdges Square montre une maîtrise des coûts et un chemin crédible vers un lancement CC NoC ;
7. le cours de l'action se maintient à KRW 20 000 et récupère la zone KRW 21 500-22 000 sur de vraies nouvelles.

Je n'envisagerais une position supérieure à 1 % qu'après que trois ou davantage de ces jalons soient visibles.

### Catalyseurs

| Catalyseur | Calendrier | Signification |
|---|---|---|
| Projet K-On Device ou initiative similaire liée aux politiques publiques | 2T26-3T26 | La demande publique en semi-conducteurs IA devient plus concrète |
| Divulgation de licences LPDDR6/5X | 2026 | Confirme le chemin vers KRW 30 Mds+ de revenus |
| Montée en charge des revenus 2T-3T | 2S26 | Montre que la reconnaissance de licences rattrape son retard |
| Activité clients Samsung 4/5/8nm | 2026-2027 | Valide la thèse centrale sur le nœud fonderie |
| Lancement CC NoC de Square | Cible 2026 | Teste si la filiale est une option ou un poids mort |

### Invalidation

| Signal d'invalidation | Interprétation |
|---|---|
| Aucune nouvelle victoire LPDDR6/5X | La thèse du pré-portage s'affaiblit |
| Revenus 2T-3T bloqués sous KRW 5,0 Mds | Le chemin vers KRW 30 Mds+ est compromis |
| La perte opérationnelle reste supérieure à KRW 6,0 Mds par trimestre | La structure de coûts est encore trop lourde |
| Le vivier de clients liés à Samsung Foundry se réduit | La thèse centrale sur la chaîne de valeur Samsung est endommagée |
| Square nécessite des financements supplémentaires de la maison mère | La dilution et le risque de coût de la filiale augmentent |
| Le refixing accroît la dilution effective | La fuite de valeur actionnariale s'amplifie |
| La part des redevances reste bloquée aux alentours de quelques pourcents | La qualité de la plateforme IP reste non prouvée |

---

## 11. Note finale

OpenEdges est une bonne option technologique. Ce n'est pas encore une bonne société en termes de bénéfices.

La thèse d'investissement la plus claire n'est pas « le champion coréen du NPU ». C'est **l'IP PHY et contrôleur LPDDR5X/LPDDR6 pour les clients ASIC IA et embarqués Samsung 4/5/8nm**. C'est plus étroit, mais aussi plus solide. Cela identifie le vrai goulot d'étranglement, le vrai vivier de clients et la vraie raison pour laquelle OpenEdges peut compter malgré les géants mondiaux de l'IP.

TSS et la filiale japonaise renforcent la base d'IP principale. OpenEdges Square ajoute une option distincte sur le CC NoC et la plateforme IP, mais cette option n'appartient qu'en partie à la maison mère cotée et doit être surveillée sous l'angle de la discipline des coûts. Le financement CPS 2026 donne à la société du runway, mais ajoute également un risque de dilution.

À une capitalisation boursière supérieure à KRW 500 Mds et environ 17x les revenus 2026E, le titre anticipe déjà un avenir meilleur. La tâche maintenant n'est pas d'admirer la technologie. C'est de vérifier la chaîne de conversion : victoires LPDDR6/5X, tape-out, validation silicium, reconnaissance de revenus, équilibre et enfin redevances.

**Ma conclusion est inchangée mais plus précise : Liste de surveillance / Ligne pilote. Renforcer seulement après que les chiffres commencent à confirmer l'histoire IP.**

---

## Notes sur les sources

- Document IR de la société : OpenEdges Technology IR Book 2026.03 via KIND, comprenant la feuille de route produit, le nombre de clients, l'historique des licences, la composition des effectifs et la structure des filiales.
- Communiqué officiel d'OpenEdges sur le lancement d'OpenEdges Square : [OpenEdges Technology lance la filiale OpenEdges Square](https://www.openedges.com/ko/post/news0816).
- Couverture The Bell sur OpenEdges et Square : [Synergie OpenEdges Technology et Square](https://www.thebell.co.kr/front/newsview.asp?key=202311301141250240104442).
- Couverture DigitalToday sur l'augmentation de capital d'OpenEdges Square et le changement d'actionnariat : [OpenEdges Technology participe à l'augmentation de capital d'OpenEdges Square](https://www.digitaltoday.co.kr/news/articleView.html?idxno=611992).
- Couverture Design-Reuse sur la commercialisation de LPDDR6/5X : [OpenEdges fait progresser la commercialisation de l'IP de sous-système mémoire LPDDR6/5X](https://www.design-reuse.com/news/202530336-openedges-advances-commercialization-of-lpddr6-5x-memory-subsystem-ip-targeting-next-generation-ai-and-hpc-markets/).
- Snapshot de marché utilisé pour la référence de valorisation : [Page boursière Maeil Business pour OpenEdges Technology](https://stock.mk.co.kr/price/home/KR7394280002).

*Avertissement : À des fins de recherche et d'information uniquement. Ne constitue pas un conseil en investissement. Les noms cités le sont à titre d'illustration analytique ; les lecteurs doivent effectuer leur propre diligence raisonnable et consulter des conseillers agréés avant toute décision d'investissement.*

---

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
