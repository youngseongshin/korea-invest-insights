---
title: "Pourquoi la Corée, partie 1 : Pourquoi la Corée compte autant d'entreprises de substrats pour semiconducteurs, là où les États-Unis et l'Europe en ont si peu"
slug: why-korea-semiconductor-substrate-competitive-edge-2026-05-07
date: 2026-05-07T21:45:00+09:00
description: "La Corée recense plus d'une dizaine d'entreprises cotées spécialisées dans les substrats pour semiconducteurs et le PCB, tandis que les États-Unis et l'Europe n'ont quasiment pas de fabricants commerciaux à grande échelle dans ce domaine. La raison n'est pas que l'Occident serait incapable de produire des substrats. C'est qu'il a privilégié, pendant trente ans, la conception de puces, les logiciels, les outils et les matériaux, pendant que le galvanoplastie, la stratification, la gravure et l'apprentissage du rendement migrait vers l'Asie."
categories: ["Why-Korea"]
tags: ["Pourquoi la Corée", "substrats pour semiconducteurs", "FC-BGA", "ABF", "infrastructure IA", "industrie coréenne", "matériaux japonais", "fonderie taïwanaise", "actions coréennes", "PCB IA"]
---

> **Série Pourquoi la Corée, partie 1.** Voici la couche stratégique qui sous-tend le [Hub PCB et substrats IA](/page/korea-ai-pcb-substrate-hub/). À lire en parallèle avec [La thèse PCB et substrats IA](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/), [L'écosystème PCB IA coréen : 10 entreprises](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) et [Samsung Electro-Mechanics : réévaluation infrastructure IA](/post/samsung-electro-mechanics-ai-infrastructure-rerating-2026-04-21/).

Une question de fond traverse toute notre analyse des substrats IA coréens et mérite sa propre note : **pourquoi la Corée compte-t-elle autant d'entreprises cotées dans les substrats et le PCB au départ ?**

Les États-Unis ont Nvidia, AMD, Broadcom, Apple, Qualcomm, Synopsys, Cadence, Applied Materials, Lam Research et KLA. L'Europe a ASML, Infineon, STMicroelectronics, NXP et des spécialistes des matériaux. Mais dès qu'un investisseur cherche des fabricants commerciaux de substrats semiconducteurs à grande échelle, la carte bascule rapidement vers le Japon, Taïwan et la Corée.

Ce n'est pas faute de compétences d'ingénierie aux États-Unis ou en Europe. C'est parce que, sur une trentaine d'années environ, ils ont choisi une couche différente de la chaîne semiconducteur. Les États-Unis se sont concentrés sur la conception, les logiciels, la propriété intellectuelle et les outils. L'Europe s'est concentrée sur la lithographie, les semiconducteurs de puissance, les puces industrielles et certains matériaux. Le travail délicat, humide et à fort volume — galvanoplastie, stratification, perçage, gravure, test et amélioration du rendement — a migré vers l'Asie.

Il en résulte un effet d'accumulation régionale. Clients, fournisseurs de matériaux, équipementiers, techniciens, chefs de ligne, bases de données de défaillances et boucles d'apprentissage du rendement se sont concentrés au Japon, à Taïwan et en Corée. C'est pourquoi cette niche est bien plus difficile à reconstituer que ce qu'un diaporama laisse croire.

---

## En bref

1. Les États-Unis et l'Europe n'ont pas échoué à fabriquer des substrats semiconducteurs. Ils ont, en grande partie, choisi de ne pas construire la base industrielle de fabrication commerciale à grande échelle que l'Asie a bâtie.
2. Les substrats ne sont pas de simples dessins. Ce sont des données de rendement. Les grands substrats IA exigent de nombreuses couches, un câblage fin, des micro-vias, un contrôle du gauchissement, une stabilité chimique et une qualification fiabilité.
3. Le Japon est fort grâce à ses matériaux et à son ancienneté : l'Ajinomoto Build-up Film, Ibiden, Shinko et trente ans d'apprentissage sur les substrats CPU haut de gamme.
4. Taïwan est fort parce que TSMC, ASE, SPIL et le cluster OSAT / fonderie ont créé la base clients naturelle pour Unimicron, Nan Ya et Kinsus.
5. La Corée est forte parce que Samsung Electronics et SK Hynix ont généré une demande locale de premier rang, tandis que la fabrication de smartphones, de mémoires et d'écrans a forgé la culture de procédé nécessaire aux substrats.
6. La Corée n'est pas au premier rang partout. Les substrats mémoire sont un point fort structurel coréen, mais le marché FC-BGA des accélérateurs IA les plus avancés reste dominé par les acteurs historiques japonais et taïwanais.
7. L'implication pour l'investissement n'est pas « acheter toutes les actions de substrats coréens ». C'est que le cluster de substrats coréen a une base historique réelle, mais la position au niveau de l'entreprise varie fortement selon le produit, le client, la dépendance aux matériaux et l'historique de rendement.

---

## 1. Qu'est-ce qu'un substrat semiconducteur ?

Une puce semiconducteur est minuscule et extrêmement dense. Un circuit imprimé est bien plus grand et plus grossier. Les bornes de la puce ne peuvent pas être connectées directement à la carte sans une couche intermédiaire.

Cette couche intermédiaire, c'est le substrat de boîtier.

```text
Puce semiconducteur
  |
Substrat de boîtier
  |
Carte mère / carte système
```

Le substrat remplit trois fonctions :

| Fonction | Ce que cela signifie |
|---|---|
| Acheminement des signaux | Transporte les données entre la puce et la carte système |
| Alimentation électrique | Fournit une puissance stable aux puces à haute consommation |
| Support mécanique | Protège la puce de la chaleur, de l'humidité, du gauchissement et des chocs |

Le principe est simple, mais la fabrication ne l'est pas. Les substrats avancés nécessitent de nombreuses couches, des pistes fines, des vias précisément alignés, un placage cuivre serré, des matériaux à faibles pertes, un contrôle du gauchissement et une haute fiabilité. Dans les accélérateurs IA et les processeurs serveur, le substrat peut être grand, à nombre de couches élevé et extrêmement peu tolérant aux défauts.

Cette industrie n'est pas une question de savoir si on peut produire un échantillon. Elle porte sur la capacité à produire des millions d'unités à un rendement économiquement viable.

---

## 2. Le vrai obstacle, c'est le rendement, pas le dessin

Pour un non-spécialiste, l'erreur la plus facile est de voir les substrats comme de simples cartes plates sur lesquelles des motifs sont imprimés. Cela passe à côté du vrai problème.

Un substrat FC-BGA haut de gamme est une structure multicouche. Chaque couche comporte du câblage. Les couches sont empilées. Des trous sont percés et galvanisés pour relier les couches entre elles. Les matériaux se dilatent et se contractent avec la chaleur. L'ensemble de la structure peut se gauchir. Le moindre défaut peut détruire le boîtier.

Plus le substrat est grand et plus le nombre de couches augmente, plus le nombre d'occasions de défaillance s'accroît rapidement. Un procédé qui fonctionne pour un petit boîtier peut devenir non rentable quand le boîtier est quatre fois plus grand et deux fois plus épais.

```text
La vraie question n'est pas :
« Pouvez-vous en fabriquer un ? »

La vraie question est :
« Pouvez-vous le fabriquer à rendement stable, avec une qualité
reproductible, malgré les changements de lots de matériaux,
les évolutions de conception clients, la dérive des équipements
et les tests de fiabilité ? »
```

Ce type de savoir ne s'acquiert pas en lisant un manuel. Il s'apprend au fil des années d'échantillonnage, de qualification, d'échecs de production, d'audits clients, de variations de matériaux et de réglages de ligne. C'est pourquoi les compétences en substrats se concentrent géographiquement. Une fois que les boucles client, matériau, équipement et personnel se trouvent dans une même région, cette région ne cesse de progresser.

---

## 3. Pourquoi les États-Unis et l'Europe se sont retirés

Le modèle américain des semiconducteurs s'est concentré sur les couches à plus fort rendement :

| Force américaine | Exemples | Profil économique |
|---|---|---|
| Conception de puces | Nvidia, AMD, Broadcom, Qualcomm, Apple | Marges brutes élevées, peu capitalistique par rapport à la fabrication |
| EDA et propriété intellectuelle | Synopsys, Cadence, Ansys | Économie proche du logiciel |
| Équipements semiconducteurs | Applied Materials, Lam Research, KLA | Équipements en capital à haute valeur ajoutée |

La fabrication de substrats présente un profil différent :

| Caractéristique de la fabrication de substrats | Pourquoi cela a compté |
|---|---|
| Procédé chimique intensif | Galvanoplastie, gravure, nettoyage et gestion des eaux usées |
| Capex élevé | Usines dédiées, longues périodes de qualification |
| Intensité en main-d'œuvre et en procédé | Les opérateurs qualifiés et les ingénieurs de procédé sont essentiels |
| Marges moins attractives | Moins séduisant pour les préférences des marchés actions américains |
| Contraintes environnementales | Les procédés humides font face à des réglementations locales plus strictes |

Ce fut une division du travail rationnelle pendant longtemps. Les entreprises américaines pouvaient concevoir la puce, contrôler le logiciel et détenir la couche équipements, pendant que les partenaires asiatiques géraient le PCB, le substrat, l'assemblage et le boîtier. Le problème, c'est qu'une décision rationnelle de chaîne d'approvisionnement est devenue une dépendance stratégique.

IPC a été explicite sur ce fossé. Ses travaux sur le packaging avancé en Amérique du Nord indiquent que les États-Unis n'ont quasiment aucune capacité à produire les substrats CI les plus avancés — comme les FCBGA et FCCSP — et que la capacité en substrats bas de gamme est également limitée. Le rapport IPC décrit également des obstacles tels que des exigences d'investissement de l'ordre du milliard de dollars par usine, de larges lacunes de savoir-faire, une chaîne d'approvisionnement de second rang insuffisante, des pénuries de matières premières et de main-d'œuvre.

L'Europe est légèrement différente, mais la conclusion est similaire. L'Europe a AT&S, une vraie entreprise de PCB haut de gamme et de substrats CI. Mais même la carte de production d'AT&S est mondiale et très orientée Asie, avec de grands sites de production en Chine et en Malaisie et un centre de compétence en Autriche. L'Europe a les compétences, mais elle ne dispose pas d'un cluster de substrats large, dense et à fort volume comparable au Japon, à Taïwan ou à la Corée.

---

## 4. Japon : matériaux et trente ans d'apprentissage du rendement

La force du Japon dans les substrats commence par les matériaux.

Le mot clé est **ABF**, l'Ajinomoto Build-up Film. L'ABF est un film isolant intercouche utilisé dans les substrats de boîtier haute performance. L'historique officiel des innovations d'Ajinomoto décrit l'ABF comme un matériau standard pour les CPU haute performance, adopté pour la première fois par un grand fabricant de semiconducteurs en 1999, et développé à partir de l'expertise en chimie fine de l'entreprise.

Cela compte parce que le substrat n'est pas seulement du câblage cuivre. Le matériau isolant entre les couches détermine la finesse possible du circuit, la stabilité de la structure et le comportement du substrat sous la chaleur et les contraintes mécaniques.

Le Japon a ensuite ajouté trois décennies d'apprentissage des procédés :

| Acteur japonais | Pourquoi cela compte |
|---|---|
| Ajinomoto | Référence matériau ABF pour les substrats haute performance |
| Ibiden | Longue histoire avec Intel et les clients CPU haut de gamme / substrats IA |
| Shinko Electric | Acteur historique des substrats de boîtier haut de gamme |
| Écosystème matériaux japonais | CCL, cuivre, produits chimiques, outils et composants de précision |

Des médias spécialisés et des articles relayés par Bloomberg ont décrit Ibiden comme un fournisseur dominant de substrats pour les puces IA de Nvidia. Que l'on retienne les estimations de parts de marché les plus agressives ou une formulation plus prudente, la direction est claire : à la couche substrat des accélérateurs IA les plus avancés, le Japon conserve la position historique la plus solide.

L'avantage du Japon n'est pas simplement « un bon niveau d'ingénierie ». C'est la combinaison du contrôle des matériaux, de l'historique de qualification clients et des données de rendement accumulées depuis l'ère CPU, qui se prolongent désormais dans les accélérateurs IA.

---

## 5. Taïwan : l'attraction du cluster fonderie et OSAT

Le chemin de Taïwan est différent. Le Japon part des matériaux et d'une longue histoire CPU. Taïwan part du cluster de fabrication semiconducteurs.

```text
TSMC : fonderie
ASE / SPIL : assemblage et test
Unimicron / Nan Ya / Kinsus : substrats
```

Les entreprises de substrats ne croissent pas isolément. Elles se développent à proximité de clients exigeants. Un client fonderie ou OSAT a besoin d'échantillons, de lots de qualification, de tests de fiabilité, d'ajustements de procédé et de retours rapides. Quand le client est proche, le cycle d'apprentissage se raccourcit.

C'est le cœur de l'avantage taïwanais en substrats. TSMC, ASE et SPIL ont créé la traction de production locale. Unimicron, Nan Ya et Kinsus ont grandi dans ce sillage.

Les estimations des cabinets d'études de marché montrent Taïwan et la Corée très proches en termes de part de production totale de substrats de boîtier, Taïwan étant souvent cité autour de 28 % de la production 2024 et la Corée autour de 27 %. Les chiffres exacts varient selon les sources et les définitions, mais la tendance est stable : Taïwan et la Corée ne sont pas des acteurs de niche. Ce sont des nœuds de production centraux.

Le risque de Taïwan est géopolitique. Son avantage tient au fait que le cluster clients est l'un des écosystèmes de fabrication semiconducteurs les plus denses au monde.

---

## 6. Corée : clients, production de masse et rapidité d'exécution

L'avantage coréen part d'un fait simple : Samsung Electronics et SK Hynix sont locaux.

Cela compte bien plus qu'il n'y paraît. Des clients forts forgent des fournisseurs forts. Samsung et SK Hynix ont entraîné les fournisseurs locaux à travers les cycles mémoire, mobile, écrans et composants avancés. Les entreprises coréennes de substrats ont appris à opérer dans des transitions de nœuds rapides, des systèmes qualité stricts et des cycles de réduction de coûts implacables.

Les racines coréennes dans les substrats ne se limitent pas aux semiconducteurs :

| Base industrielle coréenne | Ce qui a été transféré vers les substrats |
|---|---|
| Semiconducteurs mémoire | Discipline de production à fort volume, transitions générationnelles rapides |
| Smartphones | Exigences de cartes fines, denses et haute fiabilité |
| Écrans | Contrôle des procédés sur grande surface, chimie, galvanoplastie et manutention de précision |
| Chaînes d'approvisionnement électroniques | Réactivité clients rapide et ajustement des procédés |

La Corée a aussi la vitesse d'investissement. Quand les substrats pour serveurs IA sont devenus une priorité, les entreprises coréennes ont déployé des capitaux rapidement. Samsung Electro-Mechanics, Daeduck Electronics, Korea Circuit et d'autres entreprises adjacentes au PCB et aux substrats s'inscrivent dans un système où grands clients, ingénieurs locaux, fournisseurs de matériaux et décisions d'investissement peuvent s'aligner plus vite que dans beaucoup d'environnements occidentaux.

Cela ne signifie pas que chaque entreprise coréenne sera gagnante. Cela signifie que la Corée dispose des conditions industrielles préalables à l'émergence de gagnants dans les substrats.

---

## 7. Le point faible de la Corée : les substrats d'accélérateurs IA très haut de gamme

Une version honnête de la thèse doit le dire clairement : la Corée est forte dans les substrats, mais pas de façon uniforme dans toutes les catégories.

| Catégorie de substrat | Position de la Corée | Lecture |
|---|---|---|
| Substrats mémoire | Très forte | Liée aux écosystèmes mémoire de Samsung et SK Hynix |
| Substrats mobiles | Forte base historique | La croissance est plus lente, mais la base industrielle reste |
| FC-BGA PC / grand public | Capable, mais cyclique | Plus exposé à la surproduction et aux cycles PC |
| FC-BGA serveur | En rattrapage | Les fournisseurs coréens entrent dans des cycles de qualification plus sérieux |
| FC-BGA accélérateur IA très haut de gamme | Encore en retrait par rapport au Japon / Taïwan | La qualification historique et l'historique de rendement comptent le plus |

La raison, c'est le temps. Les fournisseurs coréens ont un historique FC-BGA grand serveur plus court que les leaders japonais et taïwanais. Dans les substrats d'accélérateurs IA les plus avancés, la qualification clients, le contrôle du gauchissement, le rendement sur grands formats, le comportement des matériaux et les données fiabilité sur le long terme sont déterminants.

C'est pourquoi l'opportunité n'est pas « la Corée prend tout ». L'opportunité réside dans l'entrée en tant que deuxième source, la croissance des ASIC personnalisés et la tension capacitaire chez les acteurs historiques.

Les puces personnalisées des Big Tech sont importantes ici. Google, Amazon, Meta et Microsoft cherchent tous à réduire leur dépendance exclusive à un seul fournisseur d'accélérateurs IA. Ces puces personnalisées ont toujours besoin de substrats. Si les leaders japonais et taïwanais sont saturés, les clients ont besoin d'alternatives qualifiées. C'est là que se situe l'ouverture pour la Corée.

---

## 8. Le retour des États-Unis : la voie des substrats en verre et du packaging avancé

Les États-Unis ont désormais pris conscience de la dépendance.

Le NIST et CHIPS for America ont annoncé des financements majeurs pour le packaging avancé, dont 1,4 milliard de dollars d'attributions finales dans le cadre du National Advanced Packaging Manufacturing Program et 300 millions de dollars pour la recherche sur les substrats avancés et les matériaux. La page Absolics du NIST décrit également jusqu'à 75 millions de dollars de financement direct pour une installation de substrats en verre en Géorgie liée à Absolics de SKC.

La stratégie est révélatrice. Les États-Unis n'essaient pas simplement de reproduire du jour au lendemain trente ans de base de substrats ABF asiatique. Ils cherchent à construire :

| Voie de retour américaine | Signification |
|---|---|
| R&D en packaging avancé | Développer des capacités domestiques de procédé et de pilote |
| Substrats en verre | Tenter d'entrer par une transition vers un matériau de nouvelle génération |
| Packaging avancé HBM | Utiliser le packaging mémoire IA comme point d'entrée stratégique |
| Écosystème universités / lignes pilotes | Reconstituer la boucle de personnel et de procédé |

C'est à la fois une opportunité et un risque pour la Corée.

L'opportunité tient au fait que l'ère actuelle des substrats ABF / FC-BGA favorise encore les acteurs historiques asiatiques. Le rendement, les clients et les matériaux sont déjà en Asie. Le risque est qu'une transition de matériaux — notamment vers les substrats en verre — pourrait rebattre une partie des cartes.

La Corée n'est pas mal placée pour cette réinitialisation. Le pays dispose d'une profonde expérience dans le traitement des écrans et du verre, et Absolics est elle-même liée à SKC. Mais le constat demeure : l'avantage dans les substrats est durable, non permanent.

---

## 9. Pourquoi cela compte pour la carte des actions coréennes

Le fait que la Corée compte de nombreuses entreprises de substrats n'est pas, en soi, une thèse d'investissement. La question utile est de comprendre pourquoi ces entreprises existent et où leur avantage s'arrête.

La réponse permet de construire une meilleure carte des actions :

| Couche | Noms coréens | Pourquoi la Corée compte |
|---|---|---|
| Ancre grande capitalisation | Samsung Electro-Mechanics | Exposition FC-BGA et MLCC pertinente pour les serveurs IA |
| Équilibre FC-BGA / MLB | Daeduck Electronics | Exposition substrats / cartes plus concentrée |
| Exposition FC-BGA / SoCAMM optionnelle | Korea Circuit, Simmtech, TLB | Plus dépendant du produit spécifique et de la qualification |
| MLB haut de gamme | Isu Petasys | Exposition cartes réseau / serveur |
| CCL et matériaux | Doosan Electronic BG, Kolon Industries, Pamicell | Goulot d'étranglement amont et exposition matériaux à faibles pertes |

La [thèse PCB et substrats IA](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) explique pourquoi les substrats sont un goulot d'étranglement du système. La [note sur l'écosystème des 10 entreprises](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) compare les noms coréens cotés. Cette note Pourquoi la Corée ajoute la base historique : la Corée a ces entreprises parce que les boucles clients, fabrication et apprentissage des procédés s'y sont accumulées.

Cela n'élimine pas le risque de valorisation. Cela explique simplement pourquoi le cluster est réel.

---

## 10. Deux points à ne pas perdre de vue

Premièrement, la Corée n'est pas numéro un dans chaque couche. Les substrats mémoire et de production de masse sont une vraie force. La couche substrat des accélérateurs IA les plus avancés reste dominée par des acteurs historiques avec de plus longs antécédents serveur / CPU.

Deuxièmement, les États-Unis et l'Europe ne sont pas définitivement absents. Le financement CHIPS, les programmes de packaging avancé, les substrats en verre et les investissements dans le packaging HBM sont des tentatives explicites de reconstituer les maillons manquants de la chaîne. L'horizon de temps se compte en années, pas en trimestres, mais la direction est réelle.

La bonne conclusion n'est pas « l'Asie possède les substrats pour toujours ». La bonne conclusion est : **l'avantage actuel dans les substrats est le produit de décennies d'apprentissage de production accumulé, ce qui le rend suffisamment durable pour peser sur ce cycle IA.**

---

## Note finale

La Corée compte plus d'une dizaine d'entreprises cotées dans les substrats et le PCB parce que cette compétence n'est pas apparue du jour au lendemain. Les États-Unis et l'Europe ont privilégié la conception, les logiciels, les outils, la lithographie, les puces industrielles et certains matériaux. Le travail humide, intensif en procédé et en capex de fabrication de substrats à rendement commercial a migré vers l'Asie.

Le Japon est devenu fort grâce aux matériaux ABF et à trente ans d'apprentissage sur les substrats CPU. Taïwan est devenu fort grâce à TSMC et au cluster OSAT. La Corée est devenue forte grâce à Samsung, SK Hynix, la mémoire, le mobile, les écrans et une exécution rapide des investissements.

C'est la vraie réponse à « Pourquoi la Corée ». Ce n'est pas une question d'image nationale. C'est une question de capitalisation industrielle.

Pour les investisseurs, la conclusion est pratique. Ne traitez pas chaque action coréenne de substrats comme le même actif. Demandez-vous quelle couche elle occupe, quel client la tire, quel goulot d'étranglement en matériaux compte, quelle est la durée du cycle de qualification, et si la force de l'entreprise réside dans la mémoire, le mobile, le serveur, l'accélérateur IA, le CCL ou les matériaux à faibles pertes.

C'est ainsi que la carte des substrats coréens devient utilisable : non comme un thème, mais comme une structure industrielle.

Notes de sources : Cet article s'appuie sur les travaux d'IPC sur le packaging avancé en Amérique du Nord pour le fossé de capacité en substrats américains, les publications du NIST / CHIPS for America pour le financement du packaging avancé et des substrats, l'historique officiel d'innovation ABF d'Ajinomoto pour le contexte matériaux, les documents officiels du site AT&S pour l'empreinte européenne en substrats CI, et des estimations d'études de marché pour les parts de production régionales de substrats. Les données de marché locales du Research OS ont également été vérifiées pour les noms coréens de substrats cotés au 7 mai 2026 ; la thèse de l'article ne dépend pas de l'évolution des prix à court terme.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
