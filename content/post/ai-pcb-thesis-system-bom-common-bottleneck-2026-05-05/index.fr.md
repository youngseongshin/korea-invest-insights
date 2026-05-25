---
title: "Thèse PCB et substrats IA : GPU, CPU, NIC et CCL partagent le même goulot d'étranglement"
slug: ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05
date: 2026-05-05T23:15:00+09:00
description: "Le marché présente souvent le matériel IA comme une séquence : d'abord le GPU, puis la mémoire, puis les substrats. C'est partiellement juste. L'infrastructure IA est désormais un système à l'échelle du rack composé de GPU, CPU, DPU, NIC, switch ASIC, modules mémoire, cartes d'alimentation et CCL faible perte. Chaque extension de puce nécessite une carte. Cette thèse sectorielle relie Samsung Electro-Mechanics, Daeduck Electronics, Doosan Electronic BG, Kolon Industries et Pamicell au même goulot d'étranglement au niveau système."
categories: ["Sector-Deep-Dive", "Korea Market"]
tags:
  - "PCB IA"
  - "substrats IA"
  - "FC-BGA"
  - "MLB"
  - "CCL"
  - "IA agentique"
  - "IA physique"
  - "demande CPU"
  - "NVIDIA Vera Rubin"
  - "IA rack-scale"
  - "Samsung Electro-Mechanics"
  - "Daeduck Electronics"
  - "Doosan"
  - "Kolon Industries"
  - "Pamicell"
  - "actions coréennes"
series: ["ai-pcb-substrate-thesis-2026"]
---

> <strong>Carte sectorielle :</strong> Cette note constitue la thèse PCB et substrats IA de niveau supérieur qui sous-tend les travaux sur Pamicell. À lire conjointement avec le [hub PCB IA](/page/korea-ai-pcb-substrate-hub/), [Pamicell Partie 1](/post/pamicell-doosan-electro-bg-proxy-rediscovery-2026-04-30/), [Pamicell Partie 2](/post/pamicell-four-layer-progress-and-fifth-cycle-layer-2026-05-03/), et la précédente [note de revalorisation de Samsung Electro-Mechanics dans l'infrastructure IA](/post/samsung-electro-mechanics-ai-infrastructure-rerating-2026-04-21/).

Les analyses précédentes au niveau des entreprises posaient une question plus ciblée : quels noms coréens sont le mieux positionnés dans le PCB IA, le FC-BGA et l'approvisionnement en matériaux faible perte ? Cette note prend de la hauteur. Elle cherche à comprendre pourquoi le capital devrait entrer dans l'ensemble de cet écosystème en premier lieu.

La réponse n'est pas « les substrats sont le prochain thème après les GPU ». Ce raisonnement est trop linéaire. L'infrastructure IA n'est plus une carte GPU. C'est un système à l'échelle du rack. Un rack IA moderne embarque des GPU, des CPU, des DPU, des NIC, des switch ASIC, des modules mémoire, des systèmes de distribution d'alimentation, des contrôleurs de refroidissement et des cartes haute vitesse. Chaque couche ajoute du silicium. Chaque composant silicium a besoin d'un substrat de boîtier, d'une carte module, d'une carte mère, d'une carte de commutation ou d'un empilement de matériaux faible perte.

C'est le point central : la couche PCB et substrats n'est pas la prochaine étape d'une simple rotation sectorielle. C'est le dénominateur commun de toute la nomenclature système de l'IA.

---

## Résumé

1. La séquence « GPU → mémoire → substrats » que privilégie le marché est utile dans les grandes lignes, mais incomplète. Le bon cadre d'analyse est celui d'une expansion système simultanée : GPU, HBM, CPU, DPU, NIC, switch ASIC et modules mémoire progressent ensemble, et tous nécessitent substrats ou cartes.
2. Le NVIDIA Vera Rubin NVL72 illustre concrètement ce point. La plateforme combine 72 GPU Rubin, 36 CPU Vera, la commutation NVLink 6, des SuperNIC ConnectX-9, des DPU BlueField-4 et une mise à l'échelle Ethernet Spectrum-X / Spectrum-6. Le ratio CPU:GPU est de 0,5, soit un CPU pour deux GPU. Il ne s'agit plus d'une histoire à une seule puce.
3. L'IA agentique accroît l'intensité CPU à l'inférence. L'orchestration d'outils, la récupération de données, l'exécution de code, l'accès aux bases de données, la gestion de la mémoire et l'isolation de sécurité reposent toutes sur les CPU, la DRAM, les NIC et les DPU. Si la part CPU augmente, les FC-BGA pour CPU serveur, les cartes module mémoire, les SoCAMM, les cartes mères et les CCL faible perte se trouvent tous entraînés dans le mouvement.
4. L'IA physique étend la thèse hors des centres de données. Les véhicules autonomes, les humanoïdes, les robots industriels et l'électronique spatiale utilisent davantage de cartes, davantage de capteurs, davantage de modules IA embarqués et des matériaux PCB à plus haute fiabilité. Le calendrier diffère : les centres de données d'abord, la conduite autonome ensuite, les humanoïdes plus tard, et le spatial comme prime de fiabilité haut de gamme.
5. Pour la Corée, la cartographie investissable devient étagée. Samsung Electro-Mechanics est le nœud FC-BGA haut de gamme et MLCC. Daeduck Electronics est le candidat FC-BGA / MLB / SoCAMM. Doosan Electronic BG est l'ancre CCL. Kolon Industries et Pamicell se situent en amont dans les matériaux faible permittivité. Pamicell n'est pas seulement une idée autonome ; c'est un proxy compressé au sein d'un système de substrats IA plus large.

---

## 1. Le cadre linéaire : utile, mais trop étroit

Le marché aime les séquences parce qu'elles sont faciles à trader.

Les GPU sont venus en premier : NVIDIA a capté les budgets parce que les accélérateurs étaient rares. Puis l'HBM : les GPU ne pouvaient pas monter en charge sans bande passante mémoire, ce qui a mis SK hynix, Samsung Electronics et Micron au cœur des discussions. L'étape suivante est généralement décrite comme les substrats ou le packaging avancé : si les GPU et l'HBM s'étendent, le FC-BGA, les interposeurs, les MLB et le CCL devraient suivre.

Ce cadre n'est pas faux. Un GPU plus grand nécessite un substrat de boîtier plus grand et plus complexe. L'expansion de l'HBM intensifie le packaging. Les cartes serveur deviennent plus denses et plus rapides. Sous cet angle, les substrats viennent effectivement après les GPU et l'HBM dans le cycle de reconnaissance.

Mais ce cadre passe à côté du changement le plus important dans l'architecture système. L'infrastructure IA en 2026 n'est pas un empilement de GPU. C'est une plateforme rack-scale qui co-conçoit le calcul, la mémoire, la connectique, la sécurité et le contrôle système.

La configuration NVIDIA Vera Rubin NVL72 en est l'illustration la plus nette. Les documents publics NVIDIA décrivent un système construit autour de 72 GPU Rubin et 36 CPU Vera, avec la commutation NVLink 6, des SuperNIC ConnectX-9 et des DPU BlueField-4. Les documents NVIDIA sur la plateforme Rubin définissent également la plateforme comme une co-conception de six puces : CPU Vera, GPU Rubin, switch NVLink, SuperNIC ConnectX-9, DPU BlueField-4 et switch Ethernet Spectrum-6.

L'arithmétique a son importance :

```text
CPU Vera  = 36
GPU Rubin = 72
CPU:GPU   = 36 / 72 = 0,5
```

Un CPU pour deux GPU n'est pas une note de bas de page anodine sur le processeur hôte. Cela signifie que le rack est un système, pas une étagère à GPU. Dès lors, la thèse sur les substrats cesse d'être un écho en aval de la demande GPU. Elle devient une thèse sur un système multi-puces.

---

## 2. Pourquoi chaque puce entraîne une carte

Le moyen le plus simple de visualiser la couche substrats est de parcourir la nomenclature système.

| Couche système | Puce ou module | Demande carte / substrat |
|---|---|---|
| Accélération IA | GPU, ASIC personnalisé, TPU | Grand FC-BGA, substrat de boîtier avancé, carte haute densité |
| Hôte et orchestration | CPU serveur, CPU Vera, CPU x86 / Arm | Grand FC-BGA, carte socket CPU, MLB carte mère |
| Bande passante mémoire | HBM, DDR5, modules serveur LPDDR, SoCAMM | Interposeur / substrat, PCB module mémoire, matériau intégrité signal |
| Réseau | NIC, SuperNIC, switch ASIC Ethernet, switch InfiniBand | Carte de commutation, PCB module optique, MLB faible perte |
| Transfert de données et sécurité | DPU, SmartNIC | Substrat de boîtier, PCB carte accélérateur |
| Alimentation et contrôle | VRM, modules d'alimentation, BMC et cartes de contrôle | PCB alimentation, MLCC, carte haute fiabilité |

C'est pourquoi « la demande GPU » est trop restrictive. Un hyperscaler n'achète pas un GPU isolément. Il achète un rack fonctionnel. Ce rack contient des puces de calcul, des puces mémoire, des puces réseau, des puces de contrôle et de l'électronique de puissance. Plus le système s'étend, plus la couche carte est sollicitée pour transporter des signaux haute vitesse, la chaleur, l'alimentation et la fiabilité.

La traduction en actions coréennes est également plus claire sous ce prisme :

| Couche coréenne | Entreprises à suivre | Ce qu'elles représentent |
|---|---|---|
| Substrat de boîtier haut de gamme | Samsung Electro-Mechanics, Daeduck Electronics, Korea Circuit | Exposition FC-BGA et substrat de boîtier |
| Carte multicouche et PCB module | Isu Petasys, Daeduck Electronics, TLB, Simmtech, Korea Circuit | Exposition carte mère serveur, carte de commutation, module mémoire et SoCAMM |
| Ancre CCL | Doosan Electronic BG | Stratifié cuivré haute performance pour serveurs IA et réseaux |
| Matériaux faible perte | Kolon Industries, Pamicell | Résine mPPO / faible permittivité et intrants durcisseurs |
| Stabilité de l'alimentation | Samsung Electro-Mechanics et pairs MLCC | Contenu MLCC par serveur IA et mix composants haute tension |

Pamicell appartient à cette carte en tant que proxy en amont sur les matériaux vers Doosan Electronic BG. Samsung Electro-Mechanics s'y inscrit comme le nœud coréen coté premium sur FC-BGA et MLCC. Daeduck y figure comme le candidat facteur FC-BGA / MLB / SoCAMM au sens large. Ce ne sont pas des histoires séparées. Ce sont des points différents sur la même nomenclature système.

---

## 3. L'IA agentique fait grossir la couche CPU

L'inférence LLM traditionnelle semblait simple d'un point de vue matériel :

```text
prompt
  -> passe avant GPU
  -> réponse
```

L'IA agentique transforme la charge de travail. Le modèle ne se contente plus de répondre. Il planifie, appelle des outils, effectue des recherches, lit des fichiers, exécute du code, interroge des bases de données, gère la mémoire, vérifie les sorties et peut coordonner d'autres agents. Le GPU reste central, mais la charge non-GPU devient bien plus lourde.

| Fonction agentique | Matériel principalement sollicité |
|---|---|
| Passe avant LLM | GPU + HBM |
| Orchestration d'outils | CPU |
| Récupération et recherche | CPU + DRAM + stockage |
| Exécution de code | CPU, sandbox, compilateur / interpréteur |
| Mémoire de session et état | CPU + DRAM |
| Appels d'outils en réseau | NIC + switch ASIC + PCB |
| Sécurité et isolation | CPU + DPU |

TrendForce a été explicite sur cette orientation. Son rapport d'avril 2026 sur l'IA agentique et les commentaires publics associés décrivent un changement structurel dans les ratios CPU:GPU, une offre tendue en CPU serveur et des hausses de prix chez Intel et AMD. Tom's Hardware a rapporté la même tendance côté industrie : des configurations de serveurs IA qui utilisaient autrefois un CPU pour quatre à huit GPU peuvent évoluer vers une intensité CPU bien plus élevée dans les scénarios d'inférence agentique.

Le ratio exact variera selon la charge de travail. Un cluster d'agents de code n'est pas le même qu'un cluster de génération vidéo. Un agent d'entreprise intensif en récupération n'est pas le même qu'un système d'inférence batch pur. Mais c'est la direction qui compte pour les investisseurs en substrats : plus de CPU signifie davantage de boîtiers CPU, plus de mémoire autour du CPU, plus de réseau, et des exigences d'intégrité signal plus élevées au niveau de la carte.

Le chemin de l'IA agentique aux substrats coréens ressemble à ceci :

```text
Adoption de l'IA agentique
  -> la charge de travail d'orchestration CPU augmente
  -> le contenu CPU serveur, DPU, NIC et switch ASIC progresse
  -> la demande FC-BGA pour CPU serveur et MLB haute couche augmente
  -> la complexité des modules mémoire, SoCAMM et cartes mères s'accroît
  -> le CCL faible perte et les matériaux faible permittivité deviennent plus importants
  -> les entreprises coréennes de substrats et matériaux captent une part de l'expansion de la nomenclature
```

Cette dernière ligne est importante. La Corée ne détient pas le marché des CPU. Intel, AMD, Arm, NVIDIA et les CPU personnalisés des fournisseurs de cloud captent la valeur des puces. Les sociétés cotées coréennes captent le contenu carte et matériaux autour de la puce. C'est néanmoins significatif parce que le contenu substrat croît avec le système, pas avec une seule ligne de produits.

---

## 4. L'IA physique : hors des centres de données

Le centre de données est le premier et le plus grand moteur à court terme. L'IA physique est le second vecteur d'expansion. Le calendrier est plus lent, mais la direction est cohérente : quand l'intelligence s'implante dans les véhicules, les robots, les usines et les satellites, davantage de calcul se rapproche de la périphérie. Plus de calcul en périphérie signifie plus de cartes.

### Conduite autonome

La conduite autonome est le second pilier le plus réaliste parce que les véhicules utilisent déjà d'importants composants électroniques. Un véhicule doté d'une assistance à la conduite avancée ou de fonctions autonomes contient un calculateur central, une fusion de capteurs, des modules caméra, du radar, du lidar, un Ethernet véhicule et des contrôleurs de sécurité redondants.

| Système véhicule | Demande PCB et matériaux |
|---|---|
| Calculateur central | Carte haute densité, substrat de boîtier processeur |
| ECU fusion capteurs | PCB multicouche, carte signal haute vitesse |
| Caméra / lidar / radar | Rigide-flexible, carte RF, PCB module |
| Ethernet véhicule | CCL faible perte et PCB communication haute vitesse |
| Redondance sécurité | Plus d'ECU et plus de surface de carte |

Cela n'affecte pas les résultats aussi rapidement que les centres de données IA. Les programmes automobiles prennent du temps, la qualification est lente et la courbe de revenus dépend du cycle de modèle. Mais la direction est sans ambiguïté : un véhicule plus intelligent intègre plus de contenu carte qu'un véhicule traditionnel.

### Humanoïdes et robotique industrielle

Le NVIDIA Jetson Thor donne à l'argument de l'IA physique un point de référence matériel concret. NVIDIA positionne le Jetson Thor pour l'IA physique et la robotique, avec jusqu'à 2 070 TFLOPS FP4, 128 Go de mémoire et une plage de puissance configurable de 40 W à 130 W. Ce type de module IA embarqué nécessite des cartes haute densité, des cartes d'alimentation, des interconnexions de capteurs et des PCB flexibles.

Les humanoïdes ne stimuleront pas les résultats des substrats coréens demain. Ils ne constituent pas encore un marché à gros volumes. Mais ils étendent la valeur optionnelle de la thèse. Si les modules IA embarqués se standardisent dans les robots, les usines et les machines industrielles, le contenu carte passe d'une histoire centrée sur les centres de données à une histoire de calcul distribué.

### Électronique spatiale et de défense

Le spatial est différent. Ce n'est pas une histoire de volume. C'est une histoire de fiabilité et de marge. Les documents NASA et IPC relatifs au matériel de mission insistent sur les exigences PCB à haute fiabilité, la qualification des fournisseurs et les normes de type Classe 3 / addenda spatiaux. Pour les noms PCB coréens cotés, la pertinence n'est pas « le spatial absorbera une capacité massive ». C'est que l'électronique pour environnements sévères peut justifier des normes de fiabilité plus élevées et potentiellement de meilleures marges.

La courbe temporelle se présente ainsi :

| Marché final | Calendrier revenus | Intensité PCB | Confiance pratique |
|---|---|---|---|
| Centre de données IA | Rapide | Très élevée | Élevée |
| Conduite autonome | Moyen terme | Élevée | Moyenne à élevée |
| Humanoïdes / robotique | Lent | Moyenne à élevée | Moyenne |
| Électronique spatiale / défense | Lent | Spécification élevée, faible volume | Moyenne |

Cet ordonnancement est important. Le modèle à court terme doit rester dominé par les centres de données. L'IA physique n'est pas une raison d'étirer chaque valorisation aujourd'hui. C'est une raison de penser que le marché terminal pourrait être plus large que ce que le cycle actuel des serveurs IA laisse entendre.

---

## 5. Ce que cette thèse ajoute au dossier Pamicell

Le travail sur Pamicell a commencé par un écart de reconnaissance propre à l'entreprise. Le marché se souvenait d'une société de cellules souches. Le compte de résultat ressemblait de plus en plus à un fournisseur de matériaux CCL pour l'IA. Le lien avec Doosan Electronic BG, les preuves répétées de contrats d'approvisionnement, les produits biochimiques à haute marge et la reclassification sectorielle KRX allaient tous dans le même sens.

Cette thèse sectorielle fait évoluer la question de « pourquoi Pamicell ? » vers « pourquoi la couche de matériaux CCL en amont compte-t-elle du tout ? »

La réponse est que le CCL et les matériaux faible perte ne sont pas liés à une génération de GPU. Ils se situent sous la couche système :

```text
Expansion GPU / CPU / DPU / NIC / switch ASIC
  -> les contraintes de signal haute vitesse et thermiques augmentent
  -> la demande de CCL faible perte progresse
  -> les fabricants CCL ont besoin de matériaux faible permittivité
  -> les fournisseurs en amont comme Pamicell deviennent des proxies compressés
```

Pamicell n'est toujours pas l'équivalent de Doosan Electronic BG, et ce n'est pas un fabricant de PCB. L'entreprise est plus en amont. Cela signifie que la concentration des clients et le risque de qualification sont réels. Mais cela signifie aussi que sa petite taille peut amplifier la même demande de niveau système en pourcentage si les commandes continuent de s'accumuler.

Autrement dit : la thèse de Pamicell devient plus durable si le cycle des cartes IA n'est pas seulement un cycle de substrats GPU, mais un cycle de substrats système multi-puces.

---

## 6. Ce que cette thèse ajoute au dossier Samsung Electro-Mechanics

Samsung Electro-Mechanics avait déjà été revalorisée autour de deux idées : le FC-BGA haut de gamme et le MLCC pour serveurs IA. Ce cadre plus ancien tient toujours. La thèse de la nomenclature système le clarifie davantage.

Si le seul moteur était les GPU, Samsung Electro-Mechanics serait une histoire de substrat de boîtier haut de gamme avec le MLCC en complément. Si le moteur est l'expansion système rack-scale, l'entreprise occupe plusieurs couloirs à la fois :

| Couloir | Pourquoi c'est important |
|---|---|
| FC-BGA | Les CPU, GPU, ASIC et puces réseau plus grands et plus complexes nécessitent des substrats de boîtier haut de gamme |
| MLCC | Les serveurs IA, les plateaux réseau et la distribution d'alimentation augmentent tous la densité des composants |
| Option substrat verre | Les architectures de grands boîtiers futures pourraient requérir de nouveaux matériaux et procédés de substrat |
| Électronique automobile et robotique | L'IA physique accroît la demande de composants et cartes haute fiabilité dans le temps |

Cela ne supprime pas la discipline de valorisation. Samsung Electro-Mechanics a déjà été reconnu par le marché davantage que Pamicell ou certains noms PCB plus petits. La question factorielle n'est pas « est-ce une bonne entreprise ? ». C'est « quelle part de l'expansion des substrats au niveau système est déjà dans le cours, et quelle part reste à confirmer par des commandes, des marges et des guidances ? »

C'est pourquoi cette note traite Samsung Electro-Mechanics comme l'ancre premium plutôt que l'idée à bêta le plus élevé. C'est l'expression large capitalisation coréenne la plus propre sur FC-BGA et MLCC, mais son rendement futur dépend de révisions continues des estimations plutôt que de la simple découverte du thème.

---

## 7. Cadre portefeuille : ancre, haltère, options

Le classement des entreprises peut changer avec le prix, mais la carte factorielle est stable.

| Rôle | Exposition candidate | Raison |
|---|---|---|
| Ancre premium | Samsung Electro-Mechanics | FC-BGA + MLCC + qualification client + échelle |
| Facteur PCB core | Daeduck Electronics | FC-BGA, MLB et sensibilité potentielle SoCAMM / carte module |
| Ancre CCL | Doosan Electronic BG au sein de Doosan | Corps CCL haut de gamme de la chaîne domestique |
| Haltère matériaux en amont | Kolon Industries et Pamicell | Exposition résine / matériaux faible permittivité, base plus petite et levier opérationnel plus élevé |
| Optionnalité | Korea Circuit, TLB, Simmtech, Isu Petasys | Module mémoire, MLB, réseau et bêta PCB IA plus large |

L'objectif n'est pas d'imposer une réponse unique. L'objectif est d'éviter de traiter tous les noms « PCB IA » comme le même actif. Les substrats de boîtier, les cartes multicouches, le CCL et la chimie faible permittivité ont des structures de marges, des périodes de qualification et des risques clients différents.

Une vue portefeuille utile est la suivante :

```text
Ancre premium :
  Samsung Electro-Mechanics

Facteur substrat / carte core :
  Daeduck Electronics, noms MLB sélectionnés

Haltère matériaux en amont :
  Kolon Industries + Pamicell

Options à bêta plus élevé :
  Korea Circuit, TLB, Simmtech, Isu Petasys
```

Quand le marché dit « le cycle PCB est terminé », la thèse de la nomenclature système aide à tester si c'est vrai. Si les livraisons GPU ralentissent mais que le contenu CPU, les ASIC réseau, les DPU et la complexité des modules mémoire continuent de progresser, le cycle carte peut se refroidir dans un couloir tout en restant tendu dans un autre.

---

## 8. Ce qui pourrait briser la thèse

Le cadre du dénominateur commun n'affirme pas que le cycle dure indéfiniment. Quatre risques importent.

Premièrement, le capex IA des hyperscalers peut ralentir. Si AWS, Microsoft, Google ou Meta abaissent leurs prévisions sur plus d'un trimestre, l'ensemble de la chaîne d'approvisionnement matériel le ressentira.

Deuxièmement, la technologie des substrats peut évoluer. Le substrat verre ou d'autres nouvelles architectures pourraient modifier le cycle FC-BGA plus rapidement que prévu. Cela ne supprime pas la demande de cartes, mais cela peut déplacer les gagnants.

Troisièmement, des capacités peuvent arriver. Si la capacité en CCL haut de gamme, fibres de verre ou matériaux faible perte entre sur le marché plus rapidement que prévu, le pouvoir de fixation des prix peut se normaliser avant que les volumes n'arrivent pleinement à maturité.

Quatrièmement, l'IA physique peut prendre plus de temps que ce que le marché souhaite. Les véhicules autonomes, les humanoïdes et l'électronique spatiale ont tous de longs cycles de qualification et d'adoption. Ce ne sont pas des substituts aux revenus des centres de données à court terme.

Ces risques ne tuent pas la thèse. Ils définissent la liste de vérification.

---

## 9. Liste de vérification

La thèse doit être suivie au niveau système, pas seulement à travers les chiffres trimestriels d'une seule entreprise.

| Signal | Pourquoi c'est important |
|---|---|
| Feuille de route rack-scale NVIDIA | Plus de types de puces et une densité de rack plus élevée étendent le cycle de substrats dénominateur commun |
| Commentaires sur le ratio CPU:GPU | Un ratio CPU plus élevé renforce le pilier FC-BGA pour CPU et MLB carte mère |
| Guidance capex des hyperscalers | La source de demande de premier ordre pour les cartes des centres de données IA |
| Délais de livraison CCL et fibres de verre | Confirme si la tension des matériaux est réelle ou se détend |
| Marges emballage et composants Samsung Electro-Mechanics | Teste si les prix premium des substrats et MLCC tiennent toujours |
| Commentaires sur les commandes Daeduck / MLB | Teste si le bêta PCB plus large se convertit en revenus |
| Cadence des contrats Pamicell et Doosan Electronic BG | Teste si la demande de matériaux CCL en amont continue de s'accumuler |
| Commentaires PCB automobile / robotique dans les IR des sociétés coréennes | Premier signe que l'IA physique passe de l'optionnalité aux revenus |

Si ces signaux restent alignés, le cycle des substrats n'est pas simplement un thème 2025-2027. Il devient un changement d'architecture système pluriannuel.

---

## FAQ

### Qu'est-ce que la thèse PCB IA ?

La thèse PCB IA soutient que la demande en infrastructure IA ne se limite plus aux GPU et à l'HBM. Les systèmes rack-scale ont besoin de GPU, CPU, NIC, DPU, switch ASIC, modules mémoire et cartes d'alimentation. Chaque couche nécessite des substrats de boîtier, des cartes multicouches ou des matériaux faible perte.

### Pourquoi l'IA agentique augmente-t-elle la demande en CPU ?

L'IA agentique utilise des outils, la récupération de données, l'exécution de code, la gestion de la mémoire et l'orchestration. Ces tâches ajoutent de la charge CPU, DRAM, réseau et DPU autour du GPU. Une part CPU plus élevée peut accroître la demande en FC-BGA pour CPU serveur, cartes mères, cartes module mémoire et CCL faible perte.

### Pourquoi Samsung Electro-Mechanics et Pamicell figurent-ils sur la même carte sectorielle ?

Ils se situent à des points différents de la même chaîne de substrats IA. Samsung Electro-Mechanics est un nœud FC-BGA et MLCC premium. Pamicell est un fournisseur de matériaux faible permittivité en amont lié au cycle CCL de Doosan Electronic BG. La même demande de cartes IA au niveau système peut affecter les deux, mais avec des profils de risque et de valorisation différents.

### Pamicell est-elle une entreprise PCB ?

Non. Pamicell n'est pas un fabricant de PCB. La thèse pertinente est l'exposition aux matériaux en amont : intrants faible permittivité / faible perte utilisés par les producteurs de CCL tels que Doosan Electronic BG.

### S'agit-il de conseils en investissement ?

Non. Il s'agit d'un cadre de recherche sectorielle. La bonne conclusion dépend de la valorisation, de la cadence des commandes, de la confirmation des marges, de la concentration des clients et de la tolérance au risque de chaque investisseur.

---

## Sources publiques sélectionnées

- Page produit NVIDIA Vera Rubin NVL72 : https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/
- Blog technique NVIDIA, aperçu de la plateforme Vera Rubin : https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
- TrendForce, commentaires sur l'IA agentique et le ratio CPU:GPU : https://insights.trendforce.com/p/agentic-ai-cpu-gpu
- Page rapport TrendForce, Vague IA agentique 2026 : https://www.trendforce.com/research/download/RP260408AD
- Tom's Hardware, IA agentique et demande CPU : https://www.tomshardware.com/pc-components/cpus/shifting-need-for-cpus-in-ai-workloads-drives-intensifying-shortages-price-hikes
- Page produit NVIDIA Jetson Thor : https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- Guide qualité NASA pour les normes PCB haute fiabilité : https://sma.nasa.gov/sma-disciplines/quality
- Norme PCB haute fiabilité NASA GSFC-STD-8001 : https://standards.nasa.gov/sites/default/files/standards/GSFC/Baseline/0/gsfc-std-8001.pdf

---

## Note de conclusion

La version la plus épurée de la thèse est simple :

L'IA n'achète pas des GPU seuls. Elle achète des systèmes.

Les systèmes ajoutent des puces. Les puces ont besoin de substrats, de cartes et de matériaux faible perte.

C'est pourquoi la couche substrats doit être lue comme un goulot d'étranglement commun plutôt que comme une pensée de fin de cycle. L'implication n'est pas que chaque action PCB ou matériaux coréenne mérite le même multiple. C'est que l'écosystème doit être évalué comme une chaîne d'approvisionnement de niveau système : Samsung Electro-Mechanics au nœud FC-BGA / MLCC premium, Daeduck et les noms MLB au niveau carte, Doosan Electronic BG au corps CCL, et Kolon Industries et Pamicell en amont dans les matériaux faible permittivité.

Le travail à partir d'ici n'est pas de répéter le thème. C'est de surveiller si la nomenclature système continue de s'épaissir, si le contenu CPU et réseau continue de progresser, et si les entreprises coréennes convertissent cette complexité en commandes et en marges.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
