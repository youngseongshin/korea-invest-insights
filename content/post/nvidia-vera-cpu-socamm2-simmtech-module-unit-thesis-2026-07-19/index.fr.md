---
title: "Extension de la production du CPU NVIDIA Vera et Simmtech : SoCAMM2 concerne les unités de modules, pas les bits"
slug: "nvidia-vera-cpu-socamm2-simmtech-module-unit-thesis-2026-07-19"
date: 2026-07-19T18:05:00+09:00
description: "Au fur et à mesure qu'NVIDIA étend le CPU Vera aux serveurs NVL72 et autonomes, nous vérifions si la réduction de capacité de SoCAMM2 est négative pour Simmtech. En reliant les matériels officiels d'NVIDIA, TrendForce, SK Hynix et Simmtech avec le prix des actions du 16 juillet, l'offre-demande et le consensus, nous établissons une logique d'investissement basée sur les unités de modules et les conditions d'entrée."
categories: ["Analyse exclusive", "Analyse technologique", "Actions"]
tags:
  - "Simmtech"
  - "NVIDIA"
  - "CPU Vera"
  - "Vera Rubin"
  - "SoCAMM2"
  - "LPDDR5X"
  - "Serveurs IA"
  - "PCB de module mémoire"
  - "Substrats semi-conducteurs"
  - "Offre et demande"
series: ["exclusive-analysis", "ai-hbm-2026"]
valley_cashtags:
  - 심텍
draft: false
---

Un NVIDIA Vera Rubin NVL72 contient 36 CPU Vera et 54 TB de mémoire LPDDR5X. Cela représente 1,5 TB par CPU. Cependant, en juin, TrendForce a rapporté qu'NVIDIA réduirait de moitié la capacité de ses prochains modules Vera SoCAMM tout en augmentant les expéditions totales de modules et la production de CPU Vera.

À première vue, une capacité mémoire réduite semble négative pour les fournisseurs de composants. Lorsqu'on mesure la demande de PCB uniquement en termes de bits, c'est le cas. Cependant, ce que fabrique Simmtech n'est pas des puces DRAM mais des PCB pour les modules SoCAMM. Le volume de Simmtech est plus sensible au nombre de CPU produits et au nombre de modules qu'à la capacité mémoire totale. Même si la pénurie de LPDDR force une capacité inférieure par CPU, si NVIDIA expédie plus de CPU Vera et de modules, la demande de PCB peut ne pas diminuer.

L'examen des matériels officiels, de la recherche industrielle, des estimations des analystes, ainsi que des prix réels des actions et des données d'offre-demande montre que la logique commerciale reste intacte, mais le plancher des prix n'a pas encore été confirmé.

> Contexte connecté
> Cet article est un suivi de [Thèse d'investissement en substrats IA et PCB : BOM système comme goulot commun](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/), [Écosystème coréen des PCB IA : dix entreprises](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/), [Vérification de la nomenclature de Vera Rubin VR200](/post/vera-rubin-vr200-bom-memory-pcb-mlcc-korea-alpha-2026-05-21/), et [L'écart d'approvisionnement en mémoire se déverse au-delà du HBM](/post/memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14/). Les articles connexes peuvent être trouvés dans le [hub substrats et PCB IA](/page/korea-ai-pcb-substrate-hub/), [hub HBM IA](/page/korea-semiconductor-hbm-kospi-hub/), et [hub analyse exclusive](/page/exclusive-analysis-hub/).

## Résumé

* Les spécifications officielles d'NVIDIA montrent que Vera Rubin NVL72 utilise 36 CPU Vera et 54 TB de LPDDR5X. Les racks CPU Vera autonomes prennent en charge jusqu'à 4 nœuds par plateau 1U, s'étendant jusqu'à un maximum de 256 CPU par rack. L'évolution de Vera d'un CPU d'appoint dans les racks GPU vers une plate-forme serveur indépendante est confirmée.
* La réduction de capacité SoCAMM rapportée par TrendForce est une réponse à la pénurie d'LPDDR, non un ralentissement de la demande. NVIDIA a l'intention de réduire la capacité par module tout en augmentant les expéditions totales de modules et la production de CPU Vera.
* Simmtech énumère le PCB SoCAMM sur sa page de produit officielle. Cependant, l'approvisionnement simultané par trois fournisseurs de mémoire et la part de marché élevée sont des estimations d'analystes, non des divulgations d'entreprise. Les revenus spécifiques aux clients réels et la part de marché restent non divulgués.
* Le 16 juillet, Simmtech a clôturé à 107 400 KRW, en baisse de 11,68 % en une seule journée. Sur 20 jours de négociation, les institutions ont acheté 236,2 milliards de KRW nets, et le vrai argent (pensions, fonds mutuels, assurances) a acheté 186,4 milliards de KRW, tandis que les investisseurs étrangers ont vendu 161,1 milliards de KRW et les programmes ont vendu 185,9 milliards de KRW. La pression d'achat institutionnel à moyen terme entre en collision avec la pression de vente à court terme.
* Le PER 2026E de 27,1x n'est pas bon marché. L'application du BPA attendu 2027E de 6 655 KRW donne 16,1x, mais seulement si les revenus et les marges bénéficiaires de SoCAMM se développent comme prévu.
* Le verdict est **Achat conditionnel**. Une approche plus sûre confirme le support près de 104 000 KRW avec un relâchement des ventes étrangères et programmées, ou une reprise à travers 113 800 KRW sur un volume accru.

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Verdict de cet article</div>
  <div class="thesis-callout__body">
    Connecter directement la réduction de capacité de SoCAMM2 au déclin de la demande de PCB Simmtech utilise la mauvaise unité. La formule de revenus de Simmtech s'approche davantage de Vera CPU unités × modules par CPU × PCB par module × part de marché Simmtech que des comptes de bits DRAM. Cependant, les deux derniers éléments de cette formule n'ont pas encore été confirmés par les divulgations d'entreprise.
  </div>
</div>

---

## 1. Nombres à abandonner et nombres à conserver

La taille du marché des CPU serveur 2030 de 170 milliards de dollars, le ratio CPU-GPU 1:1, et la pénurie de DRAM 2027 apparaissant dans l'analyse ci-jointe sont déjà reflétés dans les déclarations majeures de plusieurs courtages et présentations d'entreprises. Ils sont utiles pour comprendre la direction de l'industrie mais ne sont pas sources de rendements excédentaires spécifiques à Simmtech.

Quatre chiffres sont plus importants lors de l'évaluation de Simmtech :

| Élément | Pourquoi c'est important |
|---|---|
| CPU Vera expédiés | Détermine la base installée pour la plate-forme SoCAMM |
| Modules SoCAMM par CPU | Variable de volume directe pour les PCB de modules Simmtech |
| Part d'approvisionnement spécifique au client Simmtech | Détermine la portion de Simmtech de la croissance de l'industrie |
| Prix unitaire et coût du PCB de module | Détermine le taux de conversion de la croissance des revenus en profit d'exploitation |

L'utilisation d'hypothèses de 5 à 6 millions de CPU Vera et 8 modules par CPU donne 40 à 48 millions de modules annuellement. À 5,5 millions d'unités, c'est 44 millions de modules. Cependant, ce calcul n'est pas un plan officiel de livraison d'NVIDIA. C'est un scénario dérivé des estimations d'expédition de CPU des analystes et de l'industrie et des configurations système divulguées publiquement.

Par conséquent, le chiffre de 44 millions d'unités ne doit pas être utilisé directement comme projection de revenus. C'est seulement un exemple pour évaluer l'ordre de grandeur.

## 2. Les matériels officiels d'NVIDIA confirment le chemin d'expansion de Vera

### 2.1 NVL72 contient 36 CPU Vera

La [page officielle NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) présente la configuration suivante :

| Élément | Spécification officielle |
|---|---:|
| GPU Rubin | 72 |
| CPU Vera | 36 |
| Mémoire CPU | LPDDR5X 54TB |
| Mémoire par CPU Vera | 1,5TB |
| Cœurs CPU Vera | 88 |

La structure n'est pas simplement un CPU par GPU. Dans NVL72, un CPU Vera supporte deux GPU. Néanmoins, un seul rack 72-GPU nécessite 36 CPU. Cela montre que les couches CPU et LPDDR se sont élevées à des composants majeurs dans la structure de coûts des systèmes IA.

### 2.2 Vera se vend au-delà des racks GPU

Le changement plus significatif est le système CPU Vera autonome. [Le blog technique d'NVIDIA](https://developer.nvidia.com/blog/?p=114004) explique que les racks CPU Vera peuvent contenir jusqu'à 4 nœuds par plateau 1U et se mettre à l'échelle jusqu'à 256 CPU Vera par rack. Les systèmes à simple et double socket supportent jusqu'à 1,5TB LPDDR5X par socket.

NVIDIA a annoncé que Cisco, Dell, HPE, Lenovo et Supermicro prévoient de lancer des systèmes basés sur Vera au second semestre 2026. Si le calendrier est respecté, les sources de demande de Vera s'étendent au-delà des volumes d'assemblage NVL72.

```text
Sources de demande Vera

Couche CPU dans Vera Rubin NVL72
+ Serveurs CPU Vera autonomes
+ Racks CPU pour l'inférence et les agents
+ Systèmes monoprocesseur et double processeur des principaux OEM
```

C'est pourquoi la logique d'investissement de Simmtech ne dépend pas du seul volume de production des racks GPU. L'expansion des systèmes CPU autonomes élargit la base de demande pour les modules SoCAMM et les PCB.

## 3. Que signifie la réduction de capacité SoCAMM ?

[L'analyse du 10 juin 2026 de TrendForce](https://www.trendforce.com/presscenter/news/20260610-13090.html) a trouvé que seul environ 60 % des exigences en LPDRAM 2027 d'NVIDIA pouvaient être satisfaits par les allocations réservées. Pour résoudre la pénurie d'approvisionnement, NVIDIA aurait choisi les ajustements suivants :

1. Réduire la capacité mémoire de chaque module SoCAMM pour Vera.
2. Augmenter les expéditions totales de modules.
3. Produire plus de CPU Vera avec le même approvisionnement en LPDRAM.
4. Augmenter la pénétration de marché des racks CPU Vera autonomes.

Dans cette structure, deux types de demande peuvent se mouvoir dans des directions différentes.

| Unité de demande | Impact de la réduction de capacité |
|---|---|
| Bits DRAM et GB | La capacité installée par CPU peut diminuer |
| Modules SoCAMM | Peut augmenter si la croissance des expéditions de CPU dépasse la réduction de capacité |
| PCB de modules | Proportionnel aux modules, donc peut augmenter |
| Sockets, connecteurs, tests de modules | Augmentation avec le nombre de modules |

L'expression de ceci en termes Simmtech donne la formule suivante :

```text
Volume PCB SoCAMM Simmtech
= Expédition CPU Vera
× Modules SoCAMM par CPU
× PCB par module
× Part d'approvisionnement Simmtech
```

À l'inverse, le revenu SoCAMM des fournisseurs de mémoire se rapproche de décompte CPU × GB installés par CPU × prix par GB. Les mêmes nouvelles peuvent avoir des impacts différents sur les fournisseurs de DRAM et les fournisseurs de PCB de modules.

### Inadéquation entre les spécifications officielles et les rapports de TrendForce

La page officielle d'NVIDIA affiche actuellement un maximum de 1,5TB LPDDR5X par CPU Vera. TrendForce a rapporté une réduction de capacité des prochains modules. Avec les deux documents existant simultanément, il n'est pas encore certain lequel s'applique :

* La page d'NVIDIA continue d'afficher la configuration maximale ou la conception existante
* La réduction de capacité s'applique uniquement à des clients ou configurations de produits spécifiques
* Les spécifications de production finales ne sont pas encore finalisées

Cette incohérence n'est pas un bruit à cacher mais un élément de vérification pour le jugement d'investissement. La capacité réelle par module, les modules par CPU, et la configuration spécifique au client des systèmes de production doivent être vérifiés par les produits lancés et les divulgations d'entreprise.

## 4. Que fournit Simmtech dans SoCAMM2 ?

### 4.1 Ce que l'entreprise confirme officiellement

[La page officielle des produits de Simmtech](https://www.simmtech.com/product/board06.aspx) classe le PCB SoCAMM comme un produit de module mémoire de nouvelle génération pour l'IA. Les spécifications clés présentées par l'entreprise sont les suivantes :

| Élément | Description officielle de Simmtech |
|---|---|
| Mémoire de base | LPDDR |
| Application | Modules mémoire de nouvelle génération pour l'IA |
| Nombre de couches | 10–12 couches |
| Exigences clés | Constante diélectrique et perte basses, coefficient d'expansion thermique bas, contrôle d'impédance |
| Traitement de surface | ENIG sélectif |

La confirmation que le PCB SoCAMM apparaît sur la liste des produits de Simmtech est établie. L'entreprise fabrique également des PCB généraux de modules mémoire et des substrats de conditionnement de mémoire. Lorsque la demande de serveurs IA LPDDR augmente dans les modules et les emballages, l'entreprise dispose d'une base de produits pour répondre.

### 4.2 Ce qui est confirmé uniquement par les estimations des analystes

L'affirmation selon laquelle Simmtech participe à la production de SoCAMM2 de Samsung Electronics, SK Hynix et Micron simultanément et détient une part de marché élevée n'est pas une divulgation d'entreprise. C'est une analyse et une estimation de marché dans [le rapport de courtage posté sur le site d'accueil de Simmtech](https://www.simmtech.com/upload/media/file/639179687810021917.pdf).

Par conséquent, ces expressions doivent être distinguées :

| Expression | Niveau de preuve |
|---|---|
| Simmtech possède les produits PCB SoCAMM | Confirmation officielle de l'entreprise |
| Simmtech participe à la production de SoCAMM2 de trois fournisseurs de mémoire | Estimation d'analystes |
| Simmtech détient la part de marché n°1 | Estimation d'analystes |
| Revenus spécifiques aux clients et part de marché réelle | Non divulgué |
| Calendrier exact de la contribution de SoCAMM au profit de Simmtech | Non divulgué |

Cette distinction est nécessaire car la qualification des clients et le volume de production conduisent l'économie de l'activité des substrats. La capacité à fabriquer un produit et à maintenir une part de marché élevée pour les revenus répétés sont séparées par les étapes de qualification des clients, de rendement, de prix unitaire et de taux d'utilisation.

### 4.3 La production de masse de SK Hynix confirme la réalité de la plate-forme

Selon [l'annonce officielle de SK Hynix](https://news.skhynix.com/mass-production-socamm2-192gb/), la société a commencé la production de masse de 192GB SoCAMM2 utilisant LPDDR5X 1cnm en avril 2026. Le produit cible la plate-forme NVIDIA Vera Rubin.

Cela montre que SoCAMM2 n'est pas un projet de recherche à long terme mais est entré en production de masse réelle. Cependant, la production de masse de modules de SK Hynix ne prouve pas automatiquement les volumes d'approvisionnement spécifiques aux clients de Simmtech. La démonstration par Simmtech des revenus SoCAMM, de l'amélioration du mix de cartes haute couche et du taux d'utilisation dans les résultats du deuxième et troisième trimestre est séparément nécessaire.

## 5. Les résultats se rétablissent mais restent au stade de prouver les attentes

Simmtech a enregistré 1,41 billion de KRW de chiffre d'affaires pour l'année complète 2025 et 11,9 milliards de KRW de profit d'exploitation, avec une perte nette de 164,2 milliards de KRW. Au premier trimestre 2026, le chiffre d'affaires consolidé s'est rétabli à environ 422,4 milliards de KRW et le profit d'exploitation à environ 13,7 milliards de KRW. Le consensus du deuxième trimestre s'attend à un rythme de rétablissement plus rapide.

| Élément | Actuel 1T26 | Consensus 2T26 | Changement séquentiel |
|---|---:|---:|---:|
| Chiffre d'affaires | ~422,4 milliards KRW | 466,9 milliards KRW | ~+10,5% |
| Profit d'exploitation | ~13,7 milliards KRW | 47,3 milliards KRW | ~+245% |
| Marge d'exploitation | ~3,2% | ~10,1% | +6,9 points de pourcentage |

Les actifs du premier trimestre proviennent du [rapport trimestriel de Simmtech](https://kind.krx.co.kr/external/2026/05/14/000890/20260514001959/11013.htm); les estimations du deuxième trimestre proviennent du consensus Naver et WiseReport collecté par la base de données locale de Research OS le 16 juillet.

La croissance du profit d'exploitation dépasse bien la croissance des revenus. Cela indique la nécessité d'augmentations simultanées dans le mix de produits à marge élevée, l'utilisation de l'usine et l'absorption des coûts fixes. Même si le volume de SoCAMM augmente, la marge bénéficiaire peut chuter en dessous des attentes en raison des coûts des matières premières et du placage or, du rendement initial et des négociations de prix spécifiques aux clients.

### Le chemin des bénéfices exigé par le consensus annuel

| Année | Chiffre d'affaires | Profit d'exploitation | Revenu net | BPA | PER 2026E (clôture 16 juillet) |
|---|---:|---:|---:|---:|---:|
| 2026E | 1,932 billion KRW | 189,6 milliards KRW | 149,3 milliards KRW | 3 968 KRW | 27,1x |
| 2027E | 2,289 billion KRW | Consensus non agrégé | 251,0 milliards KRW | 6 655 KRW | 16,1x |
| 2028E | 2,566 billion KRW | Consensus non agrégé | 322,8 milliards KRW | 8 588 KRW | 12,5x |

Pour que le prix actuel des actions paraisse bon marché, les bénéfices 2027 et 2028 doivent réellement se concrétiser. Le PER 2026E actuel de 27,1x et le PBR de 5,64x reflètent substantiellement le rétablissement précoce. Un prix cible moyen de 171 250 KRW est 59,5 % plus élevé que le prix actuel, mais lorsque les cibles augmentent rapidement, elles sont difficiles à utiliser comme marge de sécurité.

## 6. Prix des actions du 16 juillet : Surchauffe réduite mais reprise tendancielle non encore confirmée

Simmtech a clôturé à 107 400 KRW le 16 juillet, en baisse de 11,68 % ce jour-là avec un bas intrajournalier de 103 700 KRW. C'est 34,6 % inférieur au sommet du 1er juillet de 164 200 KRW.

| Période et indicateur | Valeur |
|---|---:|
| Rendement 1 jour | -11,68% |
| 5 jours | -8,91% |
| 10 jours | -13,87% |
| 20 jours | -15,76% |
| 60 jours | +40,94% |
| 120 jours | +109,77% |
| vs MA 5 jours | -5,42% |
| vs MA 20 jours | -12,28% |
| vs MA 60 jours | -4,48% |
| vs MA 120 jours | +27,39% |
| RSI14 | 44,4 |

Le RSI a quitté le territoire suracheté. Cependant, le prix reste en dessous des moyennes mobiles 5 jours, 20 jours et 60 jours. Puisqu'il est 27 % au-dessus de la ligne 120 jours, toute la hausse du mouvement à long terme n'a pas disparu. À la fois « une baisse nette signifie bon marché » et « la tendance s'est rétablie » ne peuvent pas encore être confirmés.

Sur une base commerciale, le bas du 14 juillet de 99 600 KRW et le bas du 16 juillet de 103 700 KRW représentent la première zone de support. Le niveau 113 800 KRW confirme si le support à court terme cassé se rétablit ; 121 600 à 124 000 KRW est une zone de résistance où la clôture du 15 juillet et la moyenne mobile 20 jours se chevauchent.

## 7. Offre et demande : Les institutions ont acheté mais les investisseurs étrangers et les programmes vendent toujours

Les montants d'achat nets cumulatifs jusqu'au 16 juillet provenant de la base de données locale Kiwoom de Research OS sont les suivants. Les unités sont en milliards de KRW.

| Période | Étrangers | Institutions | Individus | Vrai argent | Programmes |
|---|---:|---:|---:|---:|---:|
| 1 jour | -9,83 | -5,88 | +15,57 | -5,91 | -11,55 |
| 5 jours | -25,79 | +6,02 | +18,95 | +7,98 | -28,71 |
| 10 jours | -93,39 | +80,32 | +11,79 | +75,77 | -40,78 |
| 20 jours | -161,09 | +236,21 | -84,25 | +186,44 | -185,94 |

Le vrai argent est la somme des fonds de pension, des fonds mutuels et des assurances. Le tableau révèle deux choses simultanément.

Premièrement, sur une base de 20 jours, l'achat institutionnel et du vrai argent est substantiel. Pendant la correction après le pic, le capital à long terme orienté domestiquement a absorbé le volume.

Deuxièmement, la vente d'investisseurs étrangers et de programmes s'est poursuivie à l'échelle similaire. Sur la baisse du 16 juillet, les investisseurs étrangers et les institutions ont vendu ensemble tandis que les individus ont absorbé 15,57 milliards de KRW. Il est difficile de juger le bas confirmé par l'achat institutionnel seul.

La part des transactions de vente à découvert a également augmenté à 21,2 % le 16 juillet. La moyenne sur 20 jours est de 9,3 %. L'inventaire de rabais de vente à découvert est d'environ 5,48 millions d'actions ou 14,6 % des actions émises, mais pas tous les inventaires de rabais de vente à découvert sont des inventaires de vente à découvert. Ce chiffre ne doit être consulté que comme référence pour le volume de vente disponible.

## 8. Simmtech revisité via P × Q × C

### P : Prix unitaire du PCB SoCAMM haute couche

Le PCB SoCAMM nécessite 10–12 couches, une perte diélectrique basse, une expansion thermique basse et un contrôle d'impédance précis. Une difficulté de fabrication plus élevée par rapport au PCB général de module mémoire peut aider à améliorer le mix de produits. Cependant, les prix unitaires spécifiques aux clients et les structures d'augmentation des prix sont non divulgués.

### Q : Nombre de CPU Vera et de modules SoCAMM

Q est la plus grande variable haussière. Au-delà de la production de masse NVL72, les racks CPU Vera autonomes et les serveurs OEM majeurs sont prévus pour le second semestre 2026. Si NVIDIA suit le rapport de TrendForce en réduisant la capacité par module tout en augmentant les expéditions de modules, le Q de Simmtech peut croître plus vite que le décompte de bits DRAM.

### C : Matières premières, placage or, rendement, utilisation

L'élément déterminant si la croissance des revenus se convertit en profit d'exploitation. Les PCB sont sensibles aux prix de l'or et du cuivre, aux matériaux BT, aux coûts de placage et au rendement initial. Pour atteindre le consensus de marge d'exploitation de 10,1 % pour le T2, l'augmentation des produits à marge élevée et la transmission des coûts doivent être confirmées ensemble.

## 9. Trois scénarios

| Scénario | Conditions | Interprétation des bénéfices et des prix |
|---|---|---|
| Haussier | Vera Rubin et les serveurs CPU autonomes expédient comme prévu ; le nombre total de modules SoCAMM augmente ; Simmtech maintient la part de marché des trois fournisseurs de mémoire | Le BPA 2027E de 6 655 KRW ou supérieur devient réalisable et justifie le PER directeur de ~16x |
| Base | Les expéditions Vera se développent mais la pénurie d'LPDDR et les rampes spécifiques aux clients ne s'alignent pas ; la part et la marge Simmtech restent aux niveaux du consensus | La croissance commerciale reste valide mais l'action peut fluctuer largement en fonction des bénéfices et de l'offre-demande |
| Baissier | Retards dans la production de masse de Vera ou SoCAMM ; la réduction de capacité par module ne conduit pas à un nombre de modules accru ; la part ou le rendement Simmtech sous-performe | Le PER 27x 2026E devient un fardeau et la probabilité de revoir les bas de juillet augmente |

Dans ces scénarios, la variable la plus importante n'est pas le marché des CPU serveur de 170 milliards de dollars. C'est le volume d'expédition réel de Simmtech, les revenus spécifiques aux clients, le mix de cartes haute couche et la marge d'exploitation. Même si les grands chiffres de l'industrie s'avèrent corrects, si la portion revenant à l'entreprise est faible, l'action aura du mal.

## 10. Verdict et séquence de vérification d'investissement

### Verdict : Achat conditionnel

La logique commerciale est devenue plus claire. Les matériels officiels d'NVIDIA ont confirmé l'expansion du serveur autonome de Vera, et le rapport de TrendForce montre la réduction de capacité comme une réaction à la pénurie d'approvisionnement, non un déclin de la demande. Simmtech possède officiellement les produits PCB SoCAMM.

Cependant, l'action reste sous pression de la vente d'investisseurs étrangers et de programmes, et elle n'est pas bon marché sur la base des bénéfices 2026. Par conséquent, il est préférable de considérer deux chemins d'entrée.

| Chemin | Condition de vérification |
|---|---|
| Confirmation du support | Maintenir le bas entre 103 700–106 000 KRW et confirmer l'assouplissement de la vente d'investisseurs étrangers et de programmes |
| Confirmation de tendance | Récupération à travers 113 800 KRW sur un volume accru avec soit les institutions soit les investisseurs étrangers devenant acheteurs nets |

La récupération à travers 121 600–124 000 KRW inverserait substantiellement les dégâts de tendance à court terme. À l'inverse, rompre en dessous de 99 600 KRW sur une base de clôture sans récupération nécessiterait une réévaluation de l'hypothèse de prix.

### Catalyseurs

* Réalisation d'un chiffre d'affaires de 466,9 milliards de KRW et d'un profit d'exploitation de 47,3 milliards de KRW dans les bénéfices du T2 2026
* Commentaires de l'entreprise sur les revenus de SoCAMM, le mix de cartes haute couche et le taux d'utilisation
* Lancement réel sur le marché de serveurs OEM basés sur Vera au second semestre 2026
* Spécifications de production finale d'NVIDIA et expansion des expéditions de racks CPU Vera autonomes
* Mises à jour de production de masse et de qualification des clients de SK Hynix, Samsung Electronics et Micron pour SoCAMM2

### Conditions d'invalidation

* Les commandes répétées échouent à suivre le volume initial de SoCAMM
* La réduction de capacité par module ne se traduit pas par une augmentation du nombre total de modules expédiés
* La part de marché spécifique au client Simmtech confirme en dessous des estimations des analystes
* Le profit d'exploitation du T2 manque matériellement le consensus avec des fardeaux récurrents de rendement et de matières premières
* Retards importants du lancement du système Vera Rubin ou CPU Vera autonome
* 99 600 KRW casse en dessous du support avec expansion concomitante de la vente d'investisseurs étrangers et de programmes

## 11. Conclusion finale

L'expansion de l'approvisionnement en CPU Vera renforce la thèse d'investissement SoCAMM2 de Simmtech. En particulier, le chemin de réduction de la capacité des modules en raison de la pénurie d'LPDDR tout en augmentant les expéditions totales de modules et de CPU est difficile à caractériser comme défavorable pour les fournisseurs de substrats. Les fournisseurs de DRAM vendent des bits et des GB ; Simmtech vend des PCB qui vont dans chaque module. Ce sont des unités différentes.

Cependant, de nombreux éléments restent non confirmés. Les volumes d'expédition Vera, les modules finaux par CPU, la part de marché réelle spécifique au client Simmtech, les revenus SoCAMM et la marge bénéficiaire de la carte haute couche ne peuvent pas être finalisés par les matériels publics seuls. Un calcul comme 44 millions de modules est un scénario utile mais pas une orientation officielle.

Le prix actuel des actions a chuté de près de 35 % par rapport au pic, mais il n'y a aucune preuve que la vente d'investisseurs étrangers et de programmes a pris fin. Par conséquent, cette idée doit être considérée comme « un candidat achat conditionnel nécessitant la confirmation à la fois des bénéfices et de l'offre-demande » plutôt que « un stock de croissance qui a chuté fortement ». Le profit d'exploitation et le commentaire de revenus SoCAMM du T2 est la première vérification, et les expéditions de serveurs CPU Vera autonomes du second semestre 2026 représentent la deuxième vérification.

---

## Preuves et limitations

### Faits confirmés

* Les spécifications officielles d'NVIDIA présentent 36 CPU Vera et 54TB LPDDR5X dans NVL72.
* NVIDIA a divulgué les systèmes CPU autonomes accueillant jusqu'à 256 CPU Vera par rack et les plans de lancement OEM pour le second semestre 2026.
* TrendForce a rapporté des ajustements pour réduire la capacité par module tout en augmentant les expéditions totales de modules et la production de CPU Vera en raison de la pénurie d'LPDRAM.
* SK Hynix a annoncé la production de masse de 192GB SoCAMM2 pour Vera Rubin.
* Simmtech énumère le PCB SoCAMM sur sa liste officielle de produits.
* La clôture du 16 juillet de Simmtech, l'offre-demande et le consensus ont été revérifiés à partir de la base de données locale.

### Estimations

* Calcul annuel de 40 à 48 millions de modules en utilisant des hypothèses de 5 à 6 millions de CPU Vera et 8 modules par CPU
* Affirmations selon lesquelles Simmtech fournit simultanément à trois fournisseurs de mémoire et maintient une part de marché élevée
* Ampleur de l'impact de la réduction de capacité sur les revenus et le profit de Simmtech suite à l'augmentation du nombre de modules

### Éléments non confirmés par les matériels publics

* Orientation officielle de livraison de CPU Vera NVIDIA 2027
* Modules finaux par CPU et capacité par module des systèmes de production finale
* Revenus SoCAMM spécifiques aux clients Simmtech, part de marché, prix unitaire et marge bénéficiaire
* Date d'annonce des bénéfices du T2 et orientation des revenus SoCAMM de l'entreprise
* Portée précise de l'application de la réduction de capacité rapportée par TrendForce et de la spécification officielle 1,5TB d'NVIDIA

Analyse informationnelle basée sur les matériels publics et les données de marché locales ; non des conseils en investissement reflétant les calendriers individuels d'investisseur, les prix ou la tolérance au risque.

*Avertissement : À des fins de recherche et d'information uniquement. Non des conseils en investissement. Les noms cités sont pour l'illustration analytique ; les lecteurs doivent effectuer leur propre diligence raisonnable et consulter des conseillers agréés avant toute décision d'investissement.*
