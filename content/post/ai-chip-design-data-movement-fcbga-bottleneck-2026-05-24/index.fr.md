---
title: "Après NVIDIA, le goulot d'étranglement des semi-conducteurs IA se trouve dans le transfert de données, la HBM, les substrats FC-BGA et l'intégrité de l'alimentation"
date: 2026-05-24T19:20:00+09:00
description: "Une synthèse de l'interview de Reiner Pope par Dwarkesh Patel sur la conception de puces, de la discussion All-In sur NVIDIA et l'infrastructure IA, et du débat de 20VC sur les marchés de capitaux autour d'Anthropic, Cerebras et SpaceX. Le point clé : l'infrastructure IA ne se résume plus à une histoire de GPU. Les investisseurs doivent suivre le transfert de données, la HBM, les substrats de boîtier, l'Ethernet, les liaisons optiques, l'intégrité de l'alimentation et les tests. En Corée, la lecture s'étend de Samsung Electronics et SK Hynix pour la mémoire aux substrats FC-BGA et condensateurs silicium de Samsung Electro-Mechanics, puis à Daeduck, Isu Petasys, Simmtech, Korea Circuit, TLB et les prises de test."
categories: ["Market-Outlook"]
tags:
  - "NVIDIA"
  - "Marvell"
  - "Samsung Electro-Mechanics"
  - "Samsung Electronics"
  - "SK Hynix"
  - "HBM"
  - "FC-BGA"
  - "Substrats IA"
  - "Infrastructure IA"
  - "Chaîne de valeur des semi-conducteurs"
slug: ai-chip-design-data-movement-fcbga-bottleneck-2026-05-24
valley_cashtags:
  - NVIDIA
  - Marvell
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - 대덕전자
  - 이수페타시스
  - 심텍
  - 코리아써키트
  - 티엘비
draft: false
---

> Série associée
> [NVIDIA Q1 FY27 et la chaîne d'approvisionnement IA coréenne](/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [Résultats prévisionnels de Marvell et Broadcom](/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/) / [Contrat de condensateurs silicium 1 500 Mds KRW de Samsung Electro-Mechanics](/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [MLCC et condensateurs silicium expliqués](/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/) / [Thèse de revalorisation de Samsung Electronics](/post/samsung-electronics-tsmc-rerating-thesis-2026-05-16/) / [Hub PCB et substrats IA de Corée](/page/korea-ai-pcb-substrate-hub/)

## En résumé

Le plus important des trois contenus est l'interview de Reiner Pope par Dwarkesh Patel. Elle ne commence pas par les manchettes de marché. Elle commence par ce qui se passe réellement à l'intérieur d'une puce : là où circule l'électricité, là où résident les données, et à quelle fréquence la puce doit déplacer ces données.[^dwarkesh]

Le point essentiel est simple. La performance de l'IA ne dépend pas uniquement des FLOPS. Le vrai goulot d'étranglement, c'est **d'où viennent les données, où elles sont stockées, et quelle est la distance entre la mémoire et le calcul**. Dans cette optique, NVIDIA reste incontournable, mais la lecture investisseur s'étend à la HBM, aux substrats de boîtier, au FC-BGA, aux cartes PCB haute densité, à l'Ethernet, aux liaisons optiques, aux composants de stabilité d'alimentation et aux tests.

Pour les investisseurs coréens, la traduction est limpide. **Samsung Electronics et SK Hynix constituent le cœur mémoire. Samsung Electro-Mechanics est le nœud FC-BGA et condensateurs silicium pour l'intégrité de l'alimentation. Daeduck, Isu Petasys, Simmtech, Korea Circuit et TLB sont des candidats à la diversification substrats et PCB.** Ce n'est pas un marché où l'on chasse un gap du lundi matin. La vraie question est de savoir si le volume et les flux étrangers/institutionnels tiennent dans l'après-midi.

---

## 1. Pourquoi l'interview de Reiner Pope est déterminante

L'erreur courante en investissement dans les semi-conducteurs IA est d'assimiler la performance d'une puce à « plus de FLOPS = meilleure puce ». L'explication de Reiner Pope déconstruit ce cadre depuis la base.

L'essentiel du calcul IA repose sur des multiplications matricielles répétées : multiplier de nombreux nombres, les additionner, et recommencer. Accélérer l'unité arithmétique compte, mais au niveau de la puce, la question centrale est souvent **d'où viennent ces nombres**.

Une puce IA comporte plusieurs niveaux de stockage et de transfert.

| Emplacement | Description simple | Traduction investisseur |
|---|---|---|
| Registres et SRAM | Le plan de travail à l'intérieur de la puce | Très rapide, mais la surface coûte cher |
| HBM | L'entrepôt haute vitesse accolé au GPU | Goulot de bande passante ; SK Hynix et Samsung Electronics |
| Substrat de boîtier / interposeur | Le plancher reliant puces et mémoire | FC-BGA, ABF, substrats avancés |
| Carte serveur et réseau | Les routes à l'intérieur et à l'extérieur du rack | PCB haute densité, Ethernet, liaisons optiques |
| Alimentation du datacenter | L'électricité pour l'ensemble du système | Transformateurs, distribution, refroidissement, coût d'exploitation total |

Si l'unité arithmétique attend des données, la puce est sous-exploitée. La vraie question pour une puce IA n'est donc pas seulement « peut-on ajouter davantage de capacité de calcul ? » C'est : **« peut-on transférer moins de données, les garder plus proches et alimenter la puce sans gaspiller d'énergie ? »**

C'est pourquoi la HBM, le FC-BGA, les condensateurs silicium et les PCB haute vitesse font partie du même sujet. Ils répondent tous au même problème physique : **maintenir les puces IA alimentées en données et en énergie stable**.

---

## 2. Pourquoi le calcul basse précision mène aux substrats et à l'alimentation

Le point de Reiner Pope sur la basse précision ne se limite pas à dire que le FP8 ou le FP4 double la vitesse. Une précision réduite modifie aussi la surface, le nombre de fils et la consommation d'énergie. Moins de bits signifient des circuits plus petits, moins de commutations et moins d'énergie par opération.

C'est important pour les investisseurs car la basse précision n'est pas uniquement une fonctionnalité des GPU NVIDIA. Si davantage de calcul est intégré dans la même enveloppe de puissance, l'ensemble du système doit évoluer.

| Évolution technologique | Exigence système | Lien avec la chaîne d'approvisionnement coréenne |
|---|---|---|
| Adoption du FP8 et FP4 | Plus de calcul dans le même budget énergétique | HBM4, DRAM serveur, SOCAMM |
| Tensor Core / architectures de type systolique | Moins de transfert de données dans la puce | HBM et interconnexion de boîtier |
| GPU et ASIC de plus grande taille | Formats de die et de boîtier plus grands | FC-BGA, ABF, substrats avancés |
| Expansion à l'échelle du rack | Plus de bande passante puce-à-puce et rack-à-rack | PCB haute densité, Ethernet, liaisons optiques |
| Densité de puissance accrue | Réponse plus rapide aux transitoires de courant et au bruit de tension | MLCC, condensateurs silicium |

La valeur dans les semi-conducteurs IA ne s'arrête donc pas au fabricant de GPU. NVIDIA ancre le système. Marvell et Broadcom occupent les puces IA personnalisées, la connectivité, l'Ethernet et les liaisons optiques. La mémoire coréenne, les substrats et les composants de stabilité d'alimentation s'y attachent en aval.

---

## 3. Les chiffres de NVIDIA sont solides. La question de marché a changé

NVIDIA a publié un chiffre d'affaires Q1 FY27 de **81,6 milliards de dollars**, un chiffre d'affaires Data Center de **75,2 milliards de dollars**, et des prévisions de chiffre d'affaires Q2 de **91,0 milliards de dollars ±2 %**. Sur la base des chiffres officiels, la demande d'infrastructure IA ne s'est pas retournée.[^nvidia]

Mais le marché ne se demande plus seulement « NVIDIA est-il en forme ? » C'est déjà acquis. Les nouvelles questions sont :

1. Ce capex se convertira-t-il en chiffre d'affaires et en free cash flow pour les clients cloud ?
2. Les goulots d'étranglement liés à l'énergie et au refroidissement des datacenters peuvent-ils être résolus ?
3. Les entreprises de modèles peuvent-elles continuer à payer des factures de tokens élevées ?
4. Le rejet de l'IA et la réglementation vont-ils freiner le déploiement ?

L'épisode All-In s'inscrit dans cette logique. Anthropic, Karpathy, SpaceX, les résultats NVIDIA et la réglementation IA font tous partie d'un même problème plus large : **l'IA n'est pas terminée, mais elle doit désormais prouver son efficacité en capital**.[^allin]

En langage de marché :

| Cadre 2023-2025 | Cadre 2026 et au-delà |
|---|---|
| Les GPU sont rares | Le transfert de données à l'échelle du rack et l'alimentation sont rares |
| La HBM est rare | HBM + substrats + intégrité de l'alimentation + réseau sont rares ensemble |
| Les modèles IA s'améliorent | L'usage de l'IA doit se convertir en chiffre d'affaires et en cash flow |
| Acheter NVIDIA | Suivre les goulots d'étranglement sous NVIDIA |

---

## 4. Marvell et Broadcom : la connectivité devient le prochain test

Marvell et Broadcom sont les prochaines publications de résultats à surveiller dans ce cadre. Ni l'un ni l'autre n'est simplement un « concurrent de NVIDIA ». À mesure que les datacenters IA se développent, les deux s'attachent à la **connectivité, au switching, aux signaux optiques et aux puces IA personnalisées**.

Pour Marvell, la question centrale est de savoir si les puces IA personnalisées et la connectivité optique s'accélèrent pour se concrétiser en chiffre d'affaires réel. Pour Broadcom, la question centrale est de savoir si les ASIC IA et le réseau Ethernet IA progressent de concert. Si les deux sociétés affichent des résultats solides, la lecture coréenne devrait s'élargir au-delà de la pure HBM.

| Signal américain | Lecture coréenne |
|---|---|
| Demande de puces IA personnalisées | HBM, substrats de boîtier, tests |
| Croissance de l'Ethernet IA et des switchs | Isu Petasys, PCB haute vitesse, matériaux à faibles pertes |
| Liaisons optiques et photonique sur silicium | Exposition optique sélective ; bénéfices indirects sur substrats et alimentation |
| Expansion à l'échelle du rack | Équipements d'alimentation, refroidissement, coût d'exploitation des datacenters |
| Boîtiers plus grands | FC-BGA Samsung Electro-Mechanics, Daeduck, Korea Circuit |

La bonne lecture n'est pas « Broadcom / Marvell en forme signifie que tous les semi-coréens sont en forme ». C'est : **la croissance des puces IA bénéficie aux fournisseurs de goulots d'étranglement qui alimentent, connectent, stabilisent et testent ces puces.**

---

## 5. Ce que confirme l'actualité AT&S

Le 21 mai 2026, AT&S a annoncé une extension de capacité pour les substrats CI haut de gamme utilisés dans l'IA, sur son site de Chongqing en Chine. L'investissement se situe dans la fourchette des dizaines de millions d'euros et est adossé à des contrats clients à long terme. AT&S anticipe un effet EBIT positif de plusieurs dizaines de millions d'euros en exercice 2026/27.[^ats-capacity]

Le point clé n'est pas le nom du client. Le point clé est que **les capacités de substrats IA sont désormais étendues sous des accords à long terme**.

AT&S avait également présenté en avril les substrats à cœur de verre comme une fondation de nouvelle génération pour l'IA, le calcul haute performance, les communications haut débit et la photonique. À mesure que les boîtiers deviennent plus grands et plus complexes, la stabilité dimensionnelle, la qualité du signal, l'efficacité énergétique et le transfert de données deviennent des facteurs limitants.[^ats-glass]

Cela rejoint directement l'interview de Reiner Pope. Si le goulot d'étranglement de l'IA est le transfert de données, les substrats et boîtiers avancés ne sont plus des composants passifs. Ils deviennent une infrastructure de performance.

---

## 6. Traduction pour les actions coréennes

### 6.1 Samsung Electronics et SK Hynix : le cœur mémoire

Réduire le coût du transfert de données nécessite de la HBM et de la mémoire serveur. Qu'il s'agisse d'un GPU ou d'un ASIC personnalisé, les puces IA haute performance consomment massivement de la bande passante mémoire.

SK Hynix est l'exposition HBM la plus directe. Samsung Electronics offre une option plus large : reprise de la HBM, HBM4, DRAM serveur, SOCAMM, eSSD et optionnalité fonderie. Mais Samsung doit encore apporter la preuve de son exécution : qualification client, rendement et victoires visibles sur les puces IA.

### 6.2 Samsung Electro-Mechanics : FC-BGA et condensateurs silicium

Samsung Electro-Mechanics est l'un des goulots d'étranglement coréens de second ordre les plus lisibles dans ce cadre.

Premièrement, le FC-BGA est le substrat de boîtier qui relie les puces haute performance à la carte. Les GPU, CPU, puces IA personnalisées et ASIC de switching de plus grande taille en ont tous besoin.

Deuxièmement, les condensateurs silicium stabilisent l'alimentation à l'intérieur du boîtier GPU IA / HBM. Samsung Electro-Mechanics a annoncé en mai 2026 un contrat de fourniture de condensateurs silicium d'environ 1 500 milliards de KRW avec un grand client mondial, en décrivant le produit comme un composant améliorant la stabilité de l'alimentation à l'intérieur des boîtiers semi-conducteurs haute performance tels que les GPU de serveurs IA et la HBM.[^semco-sicap]

L'enjeu n'est pas « davantage de contenu MLCC ». L'enjeu est que Samsung Electro-Mechanics pourrait être reclassifié en **société de substrats dotée de composants d'intégrité de l'alimentation en boîtier**.

### 6.3 Daeduck, Isu Petasys, Simmtech, Korea Circuit et TLB

Ces valeurs ne doivent pas être regroupées trop sommairement.

| Groupe | Ce qu'il faut surveiller | Risque |
|---|---|---|
| Daeduck Electronics | FC-BGA, substrats de boîtier, substrats pour puces IA | Preuve client, rendement, taux d'utilisation |
| Isu Petasys | PCB réseau haute densité | Confirmation des flux après un fort rallye |
| Simmtech / TLB | Modules mémoire, SoCAMM, PCB serveur | Mix de chiffre d'affaires IA et preuve de marge |
| Korea Circuit | Optionnalité SoCAMM et FC-BGA | Calendrier de qualification et de chiffre d'affaires effectif |

L'étiquette « exposition aux serveurs IA » ne suffit pas. Ce que les investisseurs doivent voir, c'est **un approvisionnement direct, une hausse du prix de vente moyen, des accords à long terme et une résilience des marges**.

---

## 7. Ce que 20VC révèle sur la température des marchés de capitaux

L'épisode 20VC a abordé Anthropic, l'arrivée de Karpathy chez Anthropic, Cerebras, SpaceX et le coût des tokens IA.[^twentyvc] Il s'agit moins de physique des semi-conducteurs que de température des marchés de capitaux.

Le signal positif est que les investisseurs restent prêts à financer des histoires d'infrastructure IA et de matériel IA. Le financement des laboratoires de modèles, l'appétit pour les IPO de matériel IA et les attentes autour des méga-IPO tech restent bien vivants.

Le signal négatif est la concentration des risques. Trop de capital se concentre autour d'un petit nombre de méga-acteurs IA et d'infrastructure. Les dépenses des modèles IA privés devront inévitablement passer sous le regard des marchés publics, des budgets de capex des grandes technos ou générer de vrais revenus.

Le message de 20VC n'est donc pas « acheter de l'exposition IA privée ». C'est : **l'appétit pour le risque IA est bien vivant, mais le marché va exiger de plus en plus la preuve de la monétisation et du cash flow.**

---

## 8. Checklist pratique

Pour le marché coréen la semaine prochaine, la question n'est pas seulement de savoir si Samsung Electronics et SK Hynix progressent. Le meilleur signal est de voir si l'argent descend dans la pile.

| Ordre | Point de contrôle | Signification |
|---:|---|---|
| 1 | Samsung Electronics et SK Hynix tiennent sur le volume | Cœur mémoire confirmé |
| 2 | Samsung Electro-Mechanics et Daeduck tiennent après l'ouverture | Revalorisation FC-BGA et intégrité alimentation |
| 3 | Isu Petasys, Simmtech, TLB et Korea Circuit participent | Diffusion PCB et SoCAMM |
| 4 | Les flux étrangers et institutionnels tiennent dans l'après-midi | Argent réel, pas seulement un trade thématique |
| 5 | Les équipements d'alimentation et l'infrastructure datacenter rejoignent le mouvement | Diffusion complète du goulot d'étranglement IA |

La discipline d'entrée est essentielle.

| Condition | Lecture |
|---|---|
| Gap à l'ouverture avec un faible volume | Ne pas courir après |
| Tenue dans l'après-midi avec achats étrangers/institutionnels | Élargir la liste de surveillance |
| Rallye des noms PCB pendant que les méga-valeurs mémoire faiblissent | Probablement thématique |
| Séquence mémoire → substrats → équipements d'alimentation | Signal de diffusion du goulot d'étranglement |
| Label « IA » sans chiffre d'affaires ni commandes | Éviter |

---

## 9. Conclusion

Les trois contenus se résument en une phrase :

**Le trade IA n'est pas terminé. Il descend dans la pile.**

2023-2025, c'était la phase GPU et HBM. À partir de 2026, les prochaines couches sont le transfert de données, le packaging, le FC-BGA, l'Ethernet et les liaisons optiques, l'intégrité de l'alimentation, les tests et le coût d'exploitation des datacenters. NVIDIA reste le centre. Mais la question investisseur est désormais : « quel goulot d'étranglement coréen convertit la croissance du chiffre d'affaires de NVIDIA en ses propres bénéfices ? »

L'ordre actuel est :

1. **Cœur mémoire :** Samsung Electronics, SK Hynix
2. **Boîtier et intégrité alimentation :** Samsung Electro-Mechanics, Daeduck Electronics
3. **PCB haute vitesse et modules :** Isu Petasys, Simmtech, Korea Circuit, TLB
4. **Tests et prises :** ISC, LEENO Industrial, TSE
5. **Alimentation et opérations datacenter :** équipements d'alimentation et infrastructure de refroidissement

La phrase investisseur la plus importante est celle-ci : **la compétition de performance IA est une compétition sur le coût du transfert de données, et ce coût se traduit en HBM, packaging, substrats, réseau et alimentation.**

Si cette diffusion est confirmée par le volume et les flux étrangers/institutionnels, le FC-BGA et les PCB haute vitesse doivent être traités comme des goulots d'étranglement d'infrastructure IA, et non comme un simple thème de plus.

---

## Classification des sources

### [Fait]

- L'interview de Reiner Pope par Dwarkesh Patel explique la conception des puces IA à travers les opérations MAC, le transfert de données, l'arithmétique basse précision, les structures de type Tensor Core / systolique et le coût d'exploitation total.[^dwarkesh]
- NVIDIA a publié un chiffre d'affaires Q1 FY27 de 81,6 milliards de dollars, un chiffre d'affaires Data Center de 75,2 milliards de dollars, et des prévisions de chiffre d'affaires Q2 de 91,0 milliards de dollars ±2 %.[^nvidia]
- AT&S a annoncé le 21 mai 2026 qu'il étendrait ses capacités de substrats CI haut de gamme pour l'IA sur la base d'accords clients à long terme.[^ats-capacity]
- Samsung Electro-Mechanics a annoncé un contrat de fourniture de condensateurs silicium d'environ 1 500 milliards de KRW et décrit les condensateurs silicium comme des composants de stabilité d'alimentation pour les boîtiers GPU de serveurs IA et HBM.[^semco-sicap]

### [Inférence]

- Le goulot d'étranglement des puces IA se déplace des unités arithmétiques vers le transfert de données et l'intégrité de l'alimentation.
- Les solides résultats de NVIDIA pourraient se répercuter en Corée non seulement via la HBM, mais aussi via le FC-BGA, les PCB haute vitesse, les condensateurs silicium et les prises de test.
- Les résultats de Marvell et Broadcom sont des jalons clés pour vérifier si « puces IA personnalisées + goulots de connectivité » se traduisent en chiffres réels.

### [Non confirmé]

- Le nom du client principal d'AT&S et la composition exacte de ses produits.
- Si des sociétés coréennes spécifiques de substrats et PCB approvisionnent directement les programmes NVIDIA, Marvell ou Broadcom.
- Le client, la marge sur produit et l'emplacement exact dans le boîtier des condensateurs silicium de Samsung Electro-Mechanics.
- La confirmation officielle de plusieurs valorisations et montants de financement de sociétés privées évoqués dans All-In et 20VC.

[^dwarkesh]: Dwarkesh Patel, "Chip design from the bottom up / Reiner Pope," YouTube, 2026-05-22. https://www.youtube.com/watch?v=oIk3R-sMX5o
[^allin]: All-In Podcast, "SpaceX's $2T case, Nvidia's shock selloff, America turns on AI," YouTube, 2026-05-22. https://www.youtube.com/watch?v=HGbA6ze0_3M
[^twentyvc]: 20VC, "Andrej Karpathy joins Anthropic / Cerebras / SpaceX," YouTube, 2026-05-21. https://www.youtube.com/watch?v=z94zlbVn048
[^nvidia]: NVIDIA Investor Relations, "NVIDIA Announces Financial Results for First Quarter Fiscal 2027," 2026-05-20. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027
[^ats-capacity]: I-Connect007, "AT&S Expands Capacity for AI Substrates," 2026-05-21. https://iconnect007.com/article/150109/ats-expands-capacity-for-ai-substrates/150106/pcb
[^ats-glass]: AT&S, "AT&S advances glass core substrates for AI, high-performance computing and photonics," 2026-04-22. https://ats.net/en/press/ats-advances-glass-core-substrates-for-ai-high-performance-computing-and-photonics/
[^semco-sicap]: Samsung Electro-Mechanics, "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract with Global Large-Scale Company," 2026-05-20. https://samsungsem.com/global/newsroom/news/view.do?id=10310

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
