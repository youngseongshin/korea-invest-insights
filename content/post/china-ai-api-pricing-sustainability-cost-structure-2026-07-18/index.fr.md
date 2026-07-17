---
title: "Le prix des API d'IA chinoises est-il soutenable ? Vérifier la structure de coûts par les publications financières"
slug: "china-ai-api-pricing-sustainability-cost-structure-2026-07-18"
date: 2026-07-18T11:00:00+09:00
description: "La sortie de DeepSeek V4-Pro coûte 34 fois moins que celle de GPT-5.6 Sol. S'agit-il d'un prix soutenable ou de la route vers le winner-take-all comme pour les véhicules électriques ? Les publications hongkongaises de Zhipu et MiniMax tranchent : les API payantes haut de gamme couvrent désormais le coût marginal d'inférence, mais aucune ne récupère le coût complet incluant l'entraînement."
categories: ["Exclusive Analysis", "AI Infrastructure", "Tech-Analysis"]
tags: ["IA chinoise", "DeepSeek", "Zhipu", "MiniMax", "Alibaba", "Huawei", "Tarification API", "Structure de coûts", "HBM", "Samsung Electronics", "SK Hynix"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte
> Cet article fait suite à [Ce que change vraiment la convergence des modèles ouverts chinois](/fr/post/china-open-model-convergence-value-chain-redistribution-2026-07-17/). Si l'article précédent traitait des <strong>implications de la convergence de performance sur la chaîne de valeur</strong>, celui-ci vérifie, à partir des publications financières hongkongaises, si ces API à bas prix sont <strong>soutenables du point de vue de la structure de coûts</strong>. À lire avec [Kimi K3 Réinitialise la Courbe de Prix de l'IA](/fr/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/) et [Le vrai débat des semi-conducteurs](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/). Les hubs associés sont le [Hub AI HBM](/fr/page/korea-semiconductor-hbm-kospi-hub/) et le [Hub Exclusive Analysis](/fr/page/exclusive-analysis-hub/).

## TL;DR

* Le prix actuel des API d'IA chinoises est <strong>un mélange de coûts structurellement réduits et de concurrence stratégique à perte</strong>. Il est difficile que tous les prix ultra-bas se maintiennent, tout comme il est difficile qu'ils reviennent au niveau des modèles frontière américains.
* Les publications financières hongkongaises tranchent la question. La marge brute de l'API de Zhipu s'est améliorée à <strong>18,9%</strong> (contre 3,3% l'année précédente), signe qu'elle a <strong>commencé à dépasser le coût marginal d'inférence</strong>. Mais le total de la marge brute ne représente que <strong>9,3%</strong> du R&D, ce qui signifie que <strong>le coût complet n'est pas recouvré</strong>.
* L'avantage de coût chinois est réel, mais ce ne sont ni les puces Huawei ni l'électricité bon marché qui l'expliquent. L'ordre est le suivant : <strong>structure du modèle et réduction des paramètres actifs > traitement par lots, caching et quantification > taux d'utilisation des GPU cloud > faible marge cible > électricité et NPU domestiques</strong>.
* Même en surestimant largement l'effet de l'électricité, celui-ci ne représente <strong>qu'environ 2%</strong> du prix du calcul. Le fait que Qwen 3.5 Flash affiche le même prix à Pékin, Francfort et en Virginie le confirme.
* Contrairement aux véhicules électriques, les modèles d'IA ont des <strong>coûts de changement faibles</strong>. Si un scénario winner-take-all doit émerger, ce sera au niveau du cloud et de la distribution, pas des modèles. Le chemin le plus probable est un <strong>oligopole à bas prix (60%)</strong>. \[Portée\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Thèse principale</div>
  <div class="thesis-callout__body">
    Si les prix des API chinoises sont bas, ce n'est pas parce qu'il s'agit déjà d'un prix normal et autosuffisant, mais parce que l'amélioration de l'efficacité d'inférence et un financement en capital massif les soutiennent conjointement. Cela pèse sur la marge API des opérateurs de modèles occidentaux, mais comme les fonds levés sont réinjectés dans l'entraînement et l'infrastructure de calcul, cela ne signifie pas un recul de la demande totale de semi-conducteurs.
  </div>
</div>

---

## 1. À quel point les prix sont-ils bas ?

Prix par million de tokens, à juillet 2026. \[Fait : grilles tarifaires officielles de chaque entreprise\]

| Modèle | Entrée | Sortie |
|---|---:|---:|
| DeepSeek V4 Flash | 0,14 USD | 0,28 USD |
| DeepSeek V4 Pro | 0,435 USD | 0,87 USD |
| Gemini 3.5 Flash | 1,50 USD | 9 USD |
| GPT-5.6 Sol | 5 USD | 30 USD |

DeepSeek V4-Pro est environ <strong>11 fois</strong> moins cher que GPT-5.6 Sol en entrée et environ <strong>34 fois</strong> moins cher en sortie. Cela ne signifie évidemment pas que la performance, la latence, le SLA, la sécurité et le niveau d'outillage soient identiques.

### L'écart de prix est important même à l'intérieur de la Chine

- Qwen 3.7 Max : entrée RMB 12, sortie RMB 36, actuellement en remise de 50%
- Doubao Seed 2.1 Pro : entrée RMB 6, sortie RMB 30
- DeepSeek V4-Pro : bien plus agressif que ses concurrents chinois eux-mêmes

Il ne faut donc pas considérer <strong>le prix de DeepSeek comme le prix normal de l'ensemble du marché chinois</strong>. \[Inférence : interprétation de la dispersion des prix\]

---

## 2. Ce qui est soutenable : le coût marginal

DeepSeek V4-Pro est un modèle MoE avec <strong>1,6 billion de paramètres au total, dont seulement 49 milliards sont activés</strong>. En combinant un taux d'utilisation élevé, le traitement par lots et le caching, le coût de calcul réel par token peut être fortement réduit. Le prix des hits de cache pour les entrées répétées n'est que de <strong>0,003625 USD</strong> par million de tokens. \[Fait : documentation officielle DeepSeek\]

Pour ce type de trafic, les prix actuels peuvent donc être soutenables sur une base de coût marginal.

- Traitement par lots
- Hits de cache
- Trafic sans garantie de latence
- Usage massif permettant de maintenir un taux d'utilisation élevé

---

## 3. Ce qui est difficile à soutenir : le coût complet

Les prix publics actuels seuls peinent à couvrir le coût d'entraînement des modèles, le R&D, les expériences ratées, la capacité inutilisée, ainsi que la sécurité, les ventes et le SLA entreprise.

La normalisation des prix a d'ailleurs déjà commencé. \[Fait : mesures des entreprises et couverture médiatique\]

- DeepSeek a baissé le prix de V4 de 75%, puis <strong>doublé le prix aux heures de pointe</strong>
- Alibaba a également relevé le prix de certains services d'IA de <strong>jusqu'à 34%</strong>
- Le débit dédié aux entreprises et les services à faible latence sont facturés plus cher que l'API publique

C'est la preuve que les prix ultra-bas ne se maintiennent pas sur tous les créneaux horaires ni pour tous les segments de clientèle.

| Service | Soutenabilité |
|---|---|
| Cache, lots, trafic non prioritaire | Élevée |
| Heures de pointe, faible latence, forte concurrence | Faible |
| Sécurité et SLA entreprise | Tarification premium distincte, désormais établie |
| Recouvrement du coût complet pour une activité API indépendante | Difficile aux prix actuels |

---

## 4. Vérification par les publications financières : Zhipu et MiniMax

C'est ici le cœur de l'article. Plutôt que de spéculer, on peut vérifier grâce aux <strong>publications financières de sociétés cotées à Hong Kong</strong>.

| 2025 | Zhipu (02513) | MiniMax (00100) |
|---|---:|---:|
| Chiffre d'affaires | RMB 724 millions | 79,04 M USD |
| Part API/plateforme dans le CA | 26,3% | 32,8% |
| Marge brute API ou groupe | API 18,9% | Groupe 25,4% |
| Marge brute année précédente | API 3,3% | Groupe 12,2% |
| R&D / CA | 439% | 320% |
| Perte nette ajustée / CA | 439% | 317% |
| Marge brute / R&D | <strong>9,3%</strong> | <strong>7,9%</strong> |

\[Fait : résultats 2025 de Zhipu, rapport annuel 2025 de MiniMax\]

### Zhipu : le recouvrement du coût marginal est confirmé

Le chiffre d'affaires API et plateforme ouverte est passé de RMB 48,48 M à <strong>RMB 190,4 M, soit une hausse de 293%</strong>, et la marge brute est passée de 3,3% à 18,9%. L'entreprise attribue cette évolution à l'efficacité d'inférence, aux économies d'échelle et aux hausses de prix.

Un fait plus important encore : en mars 2026, bien que le prix de l'API ait été <strong>relevé de 83% par rapport à fin d'année précédente, la demande a continué de dépasser l'offre</strong>. Le prix officiel actuel de GLM-5 est de RMB 4 en entrée et RMB 18 en sortie par million de tokens. L'API haut de gamme semble donc être sortie d'une structure de dumping en dessous du coût direct d'inférence. \[Inférence : implication de la hausse de prix et de la demande excédentaire\]

### MiniMax : probable, mais non confirmé

La marge brute de l'API seule n'a pas été divulguée. La marge brute au niveau du groupe s'est améliorée de 12,2% à <strong>25,4%</strong>, et l'entreprise l'attribue à l'efficacité du modèle et du système ainsi qu'à l'optimisation de l'allocation d'infrastructure.

Le prix actuel de M2.5 est de 0,30 USD en entrée et 1,20 USD en sortie par million de tokens, avec 0,60 USD/2,40 USD pour la version rapide. Cependant, comme M2.5 a été lancé en 2026 et que les résultats publiés ne couvrent que jusqu'à 2025, <strong>le ratio de coût de l'API seule aux prix actuels n'est pas encore vérifié</strong>. \[Non vérifié\]

### Le coût complet n'est recouvré par aucune des deux entreprises

La marge brute totale de Zhipu, RMB 297 M, ne représente que <strong>9,3%</strong> de son R&D de RMB 3,18 Mds. MiniMax non plus : sa marge brute de 20,08 M USD n'a couvert que <strong>7,9%</strong> de son R&D de 253 M USD, et sa sortie de trésorerie opérationnelle s'est élevée à 280 M USD.

Les services achetés par MiniMax auprès du groupe Alibaba en 2025 se sont élevés à <strong>75,88 M USD, soit 96% de son chiffre d'affaires</strong>. Ce montant mélange cloud d'entraînement et cloud de service, donc on ne peut pas l'assimiler directement au coût de l'API, mais c'est la preuve d'une forte dépendance à une infrastructure de calcul externe. Alibaba détient 17,06% du capital de MiniMax.

Un point important : la publication indique que les transactions avec les parties liées ont été réalisées <strong>aux prix et conditions publics offerts aux clients ordinaires</strong>. On peut reconnaître un accès facilité à la capacité et une intégration facilitée du fait de la relation stratégique, mais <strong>rien ne permet d'affirmer qu'il y a eu une subvention de prix cachée</strong>. \[Inférence : interprétation du texte de la publication\]

Même après leur introduction en bourse, Zhipu a levé net 31,375 Mds HK$ et MiniMax a levé net 15,957 Mds HK$ au total via de nouvelles actions et des obligations convertibles. L'essentiel de ces fonds va au R&D et à l'infrastructure de calcul. Le financement en lui-même n'est pas une preuve de pertes sur l'API, mais <strong>la compétition entre modèles frontière n'en est pas au stade où elle peut être soutenue par la seule trésorerie interne</strong>. \[Fait : publication financière\]

### Verdict

1. Soutenabilité du coût marginal pour l'API payante haut de gamme : <strong>confirmée</strong> pour Zhipu, probable mais non confirmée pour MiniMax
2. Soutenabilité du coût complet incluant l'entraînement : <strong>non satisfaite</strong> pour les deux entreprises
3. Soutenabilité de la guerre des prix : <strong>élevée</strong>. Le financement par les marchés de capitaux permet de maintenir longtemps des prix déficitaires
4. Structure de marché : plutôt qu'un winner-take-all, un <strong>oligopole par segment</strong> est probable, Zhipu sur les entreprises chinoises et l'on-premise, MiniMax sur l'international, le grand public et le multimodal

---

## 5. Décomposer l'avantage de coût : quelle est la vraie raison ?

L'avantage de coût chinois dans le service des API est réel. Mais l'essentiel ne tient pas à l'électricité bon marché ou aux seules puces Huawei : c'est la combinaison suivante.

```text
Peu de paramètres actifs · quantification
+ Taux élevé de traitement par lots · utilisation du cache
+ Taux d'utilisation des GPU des grands clouds comme Alibaba
+ Faible marge cible
+ Électricité bon marché dans l'ouest de la Chine
```

| Facteur | Avantage de coût | Jugement |
|---|---:|---|
| Structure du modèle, quantification, caching | Très fort | Cœur de la compétitivité prix des API chinoises |
| Échelle et taux d'utilisation du cloud | Fort | La douve la plus solide d'Alibaba |
| Faible marge cible | Fort | Explique le bas prix, mais fragilise la rentabilité à long terme |
| Huawei Ascend | Moyen, conditionnel | Avantageux sur des charges de travail optimisées, faible polyvalence |
| Électricité de l'ouest chinois | Moyen | Efficace pour l'inférence par lots, limité pour les API mondiales en temps réel |
| Subventions publiques, financement politique | Présent | Favorable au développement industriel, mais le montant par service reste opaque |

---

## 6. L'électricité est-elle vraiment décisive ?

Il est vrai que l'électricité chinoise est bon marché. Le prix de l'électricité livrée au data center de Zhongwei, dans le Ningxia, s'établit en 2026 à <strong>RMB 0,36/kWh</strong>, soit environ 45% du niveau de la Chine de l'Est. La moyenne industrielle américaine de 2025 est de <strong>8,62 cents/kWh</strong>, soit environ RMB 0,62/kWh avec un taux de change supposé de 7,2 RMB/USD. Zhongwei est donc environ <strong>42% moins cher</strong>. \[Fait : données des autorités locales chinoises, EIA américaine\]

Mais l'électricité seule n'explique pas que le prix des API soit 5 ou 10 fois plus bas. En <strong>surestimant largement</strong> l'effet de l'électricité, avec une charge IT de 1 kW par carte et un PUE de 1,1, voici ce que cela donne.

```text
Zhongwei :          1 kW × 1,1 × 0,36 RMB = 0,40 RMB/heure
Moyenne américaine : 1 kW × 1,1 × 0,62 RMB = 0,68 RMB/heure
Différence :                                environ 0,29 RMB/heure
```

Comme le prix à la demande du L20 proposé par Alibaba est de RMB 14,4/heure, même dans cette hypothèse haute, l'écart d'électricité ne représente <strong>qu'environ 2%</strong> du prix du calcul. \[Inférence : calcul propre à l'auteur\]

Cela signifie que l'électricité compte, mais qu'elle n'est pas la cause principale de l'écart de prix des API.

### Contre-preuve décisive

L'avantage de l'électricité de l'ouest convient bien à l'inférence par lots et à l'entraînement, mais les API à faible latence doivent être déployées dans des régions proches des utilisateurs, à l'est ou à l'étranger. Or le prix de Qwen 3.5 Flash chez Alibaba est <strong>identique non seulement à Pékin, mais aussi à Francfort et en Virginie : 0,029 USD en entrée et 0,287 USD en sortie par million de tokens</strong>. \[Fait : grille tarifaire Alibaba Model Studio\]

C'est la preuve la plus directe que les API à bas prix ne sont pas seulement le résultat de l'électricité chinoise. \[Inférence : implication de la parité tarifaire entre régions\]

---

## 7. La vraie douve d'Alibaba, c'est le taux d'utilisation

Alibaba Cloud tire sa force moins de l'électricité que de sa <strong>capacité à ne jamais laisser les GPU inactifs</strong>. \[Fait : documentation officielle Alibaba\]

- Inférence par lots : <strong>remise de 50%</strong> sur le prix catalogue
- Instance spot L20 : d'un prix à la demande de RMB 14,4 à généralement environ RMB 2,88, soit une économie d'environ <strong>80%</strong>
- GPU inactifs : tarif de 0,000007 USD/CU pour les GPU inactifs contre 0,000018 USD/CU pour les GPU actifs
- Combinaison d'instances à la demande, spot et d'autoscaling pour absorber les pics de trafic

Cependant, les instances spot comportent un risque de reprise, ce qui empêche de faire tourner l'ensemble d'une API en temps réel à SLA strict sur du spot. La structure consiste à placer la demande de base sur des ressources à la demande ou dédiées, et à ne traiter que la demande élastique en spot. \[Inférence : contrainte opérationnelle\]

---

## 8. Le Huawei Ascend est-il forcément bon marché ?

À strictement parler, Ascend n'est pas un GPU mais un <strong>NPU</strong>.

Huawei avance les éléments suivants pour CloudMatrix 384. \[Fait : documentation officielle Huawei\]

- Débit d'inférence équivalent par carte : 2 300 tokens/s
- Environ 4x par rapport aux configurations non-supernode existantes
- Amélioration du MFU de plus de 50%
- Performance d'inférence moyenne par carte 3-4x supérieure au H20

C'est une approche qui compense par la conception système, via la mise en pool des ressources et la parallélisation des experts MoE, la faiblesse des puces individuelles bas de gamme.

### Mais il ne faut pas y voir directement un coût faible

- Huawei <strong>n'a pas publié de TCO vérifié de manière externe, à modèle, latence et électricité identiques</strong>. \[Non vérifié\]
- CloudMatrix augmente le débit en assemblant de nombreux NPU et réseaux, donc <strong>le débit par carte et le coût total du cluster sont deux choses différentes</strong>.
- Une étude de terrain de 2026 sur Ascend 910 a montré qu'une inférence stable nécessitait 12 correctifs du code source, la désactivation de certaines fonctions à haut débit, et des dispositifs pour gérer des pannes récurrentes. Même si le matériel est bon marché, <strong>les coûts d'ingénierie et d'exploitation peuvent augmenter</strong>. \[Fait : étude de terrain sur Ascend\]

### Verdict conditionnel

| Condition | Verdict |
|---|---|
| Modèles profondément optimisés pour Ascend, comme Qwen, DeepSeek, GLM | Compétitivité de coût possible |
| Migration directe de modèles fondés sur CUDA | Avantage de coût incertain |
| Inférence par lots à grande échelle en Chine | Favorable |
| Service en temps réel pour entreprises mondiales | Non confirmé une fois inclus le coût logiciel et SLA |

---

## 9. En quoi est-ce différent des véhicules électriques ?

Les points communs sont l'industrie stratégique, les investissements massifs, les subventions aux grandes entreprises et la conquête de parts de marché par la baisse des prix.

La différence, c'est que <strong>le coût de changement des modèles d'IA est bien plus faible</strong>. Les spécifications d'API sont similaires, et les clients peuvent router simultanément vers plusieurs modèles ou héberger eux-mêmes des modèles open source. Si un opérateur relève ses prix, les modèles concurrents et l'auto-hébergement créent un plafond de prix.

En revanche, une plateforme combinant cloud, données, sécurité, paiement, publicité et outils métier a un coût de changement élevé. <strong>Si un scénario winner-take-all émerge, ce sera davantage au niveau de la distribution et du cloud qu'à celui des modèles</strong>. \[Inférence : structure des coûts de changement\]

La structure la plus probable est la suivante.

- Alibaba : cloud, e-commerce, clients entreprises
- ByteDance : trafic grand public, publicité, contenu
- Tencent : WeChat, services aux entreprises
- Huawei, Baidu : infrastructure domestique, clients publics et entreprises
- DeepSeek et 1 à 2 autres opérateurs de modèles indépendants : fixent le prix de référence technologique

---

## 10. Trajectoire attendue

| Scénario | Probabilité estimée | Résultat |
|---|---:|---|
| Oligopole à bas prix | <strong>60%</strong> | Concentration à 3-5 acteurs, prix bas maintenu sur l'API de base, hausse des prix aux heures de pointe et pour le SLA |
| Commoditisation totale | 25% | L'open source, le MoE et les puces propriétaires entraînent de nouvelles baisses de prix |
| Normalisation marquée | 15% | Hausse des prix de 2 à 5 fois sous la pression des puces, de l'électricité et du financement |

\[Inférence : estimation de scénario\]

Même si les prix étaient multipliés par 5, le prix de sortie de DeepSeek V4-Pro serait d'environ 4,35 USD, ce qui resterait inférieur à celui des modèles frontière américains. <strong>Le prix actuel n'est peut-être pas un plancher, mais la tendance à la baisse des prix sera difficile à inverser.</strong>

---

## 11. Implications pour les semi-conducteurs

Des API bon marché augmentent l'usage de l'inférence, ce qui est favorable à la demande de DRAM serveur, de NAND, de réseau et d'électricité. En revanche, elles réduisent le volume de calcul par token et l'intensité d'intégration de HBM, ce qui pèse sur l'économie unitaire des GPU premium et du HBM.

| Cible | Jugement |
|---|---|
| Samsung Electronics | Relativement amorti grâce à une forte exposition à la DRAM et au NAND génériques |
| SK Hynix | Signal d'alerte à long terme sur la prime de rareté du HBM |
| NVIDIA | Pression sur le prix unitaire des GPU premium, compensée par la hausse du volume total d'inférence |
| Alibaba, Tencent | Bénéficient davantage de l'expansion de l'écosystème cloud et de distribution que de la marge API |

L'essentiel n'est pas le taux de baisse du prix des API, mais <strong>le taux de croissance de l'usage total de tokens</strong>. Si l'usage croît plus vite que la baisse des prix, l'effet Jevons l'emporte ; sinon, les multiples commencent à baisser d'abord pour les GPU premium et le HBM. \[Inférence : jugement directionnel\]

---

## 12. Le test décisif : les publications du premier semestre 2026

- La <strong>marge brute API de Zhipu</strong> dépasse-t-elle 25-30% après la hausse de prix de 83%
- <strong>MiniMax publie-t-il son ratio de coût API</strong>
- <strong>Le taux de croissance du chiffre d'affaires continue-t-il de dépasser celui des coûts de calcul</strong>
- L'écart entre les tarifs pic/SLA et les tarifs API publics se consolide-t-il
- Huawei publie-t-il un TCO vérifié de manière externe à conditions identiques

Ces cinq éléments détermineront ce qui relève d'un « coût soutenable » et ce qui relève d'un « prix maintenu par le capital ».

---

## Conclusion

Si les prix des API chinoises sont bas, ce <strong>n'est pas parce qu'il s'agit déjà d'un prix normal et autosuffisant</strong>. C'est parce que l'amélioration de l'efficacité d'inférence et un financement en capital massif les soutiennent conjointement.

La Chine dispose d'un avantage de coût structurel pour le service de modèles domestiques, par lots et optimisés. Mais les prix d'API extrêmement bas observés actuellement ne peuvent pas s'expliquer par les seules puces Huawei et l'électricité bon marché. Le principal avantage de coût vient, dans l'ordre, de la taille du modèle et de la réduction des paramètres actifs, du traitement par lots, du caching et de la quantification, du taux d'utilisation des GPU cloud, puis de la faible marge cible ; l'électricité et les NPU domestiques ne viennent qu'ensuite.

Du point de vue de l'investisseur, les API chinoises à bas prix ne signifient pas directement que « l'IA chinoise a acquis une douve de coût écrasante ». L'interprétation la plus juste est plutôt que <strong>le service d'inférence se commoditise rapidement, ce qui comprime la marge des sociétés de modèles et accroît la probabilité que la valeur se déplace vers le cloud, l'électricité et l'infrastructure de semi-conducteurs</strong>.

Cela pèse sur la marge API des opérateurs de modèles occidentaux, mais comme les fonds levés sont réinjectés dans l'entraînement et l'infrastructure de calcul, cela <strong>ne signifie pas un recul de la demande totale de semi-conducteurs</strong>.

---

_Cet article est une synthèse analytique fondée sur les publications de sociétés cotées à Hong Kong (résultats 2025 et placement de nouvelles actions de Zhipu 02513, rapport annuel 2025 et levées de fonds de MiniMax 00100), les grilles tarifaires officielles de chaque entreprise (DeepSeek, OpenAI, Google, Alibaba Model Studio, Volcano Engine, Zhipu BigModel, MiniMax Platform), la documentation officielle de Huawei et des études sur CloudMatrix, des données des autorités locales chinoises sur l'électricité, et des statistiques de l'EIA américaine. Le ratio de coût de l'API seule chez MiniMax et le TCO de Huawei vérifié de manière externe à conditions identiques ne sont pas divulgués ; les probabilités de scénarios et les calculs d'électricité sont des estimations fondées sur des hypothèses au moment de la rédaction. Les valeurs mentionnées sont des exemples destinés à illustrer la structure de coûts, et non une recommandation d'achat ou de vente sur un titre en particulier. Les prix et chiffres des publications sont valables à la date de leur annonce et peuvent évoluer par la suite. Les décisions d'investissement et leurs conséquences relèvent de la seule responsabilité de l'investisseur._

---

### Articles associés

- [Ce que change vraiment la convergence des modèles ouverts chinois : redistribution de la chaîne de valeur, pas effondrement de la demande](/fr/post/china-open-model-convergence-value-chain-redistribution-2026-07-17/)
- [Kimi K3 Réinitialise la Courbe de Prix de l'IA : De Kimi Linear à HBM et la Stratégie des Grandes Tech](/fr/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/)
- [Le vrai débat des semi-conducteurs : quatre horloges physiques et une horloge boursière](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [Les semi-conducteurs sont-ils cycliques et quelle est la juste valeur ? Valoriser Samsung, SK Hynix et Micron avec le FCFE et les bénéfices normalisés](/fr/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [La valeur actuelle et future du token IA : analyse de la valeur ajoutée des acteurs de la mémoire](/fr/post/ai-token-value-memory-value-added-2026-07-09/)
