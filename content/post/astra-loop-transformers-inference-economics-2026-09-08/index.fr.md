---
title: "Après Astra : comment les transformeurs en boucle bouleversent l'économie de l'infrastructure IA"
slug: "astra-loop-transformers-inference-economics-2026-09-08"
date: 2026-09-08T18:00:00+09:00
description: "En partant de l'essai du PDG de Lablup, Jeongkyu Shin, nous examinons les recherches Huginn, Ouro et MoR pour distinguer l'efficience en paramètres des coûts de calcul, de mémoire et de service."
categories: ["Tech-Analysis", "Exclusive Analysis"]
tags: ["IA", "Transformeurs en boucle", "Astra", "HBM", "Inférence", "Lablup"]
draft: false
---

Un petit modèle peut-il résoudre des problèmes plus complexes en traversant plusieurs fois le même réseau de neurones ? Jeongkyu Shin, PDG de Lablup, reprend cette question dans son [essai Facebook sur les transformeurs en boucle après Astra](https://www.facebook.com/jeongkyu.shin/posts/pfbid02jm4iibHsgU11P7gY8e4SZKtKYNNdtHF6wdTQK2EdyDeTMEwxiDvHnHyhyAKphLml). Derrière la question architecturale se cache une décision d'infrastructure : combien d'accélérateurs et quelle quantité de mémoire acheter, et comment les exploiter.

La recherche publique montre qu'un modèle peut améliorer sa capacité de résolution tout en conservant des poids fixes, en exécutant de manière répétée un bloc de calcul partagé. Mais la répétition consomme du temps et de l'énergie. Un modèle plus petit ne signifie pas automatiquement un service moins coûteux.

Il s'agit d'une analyse indépendante suscitée par l'essai de Shin, complétée par des articles originaux et des fiches de modèles. Nous distinguons l'interprétation d'Astra avancée dans l'essai des faits publiquement établis, et traitons les implications industrielles comme une analyse conditionnelle. Les sources ont été vérifiées le 8 septembre 2026.

## Les résultats d'Astra ne divulguent pas son architecture

L'annonce d'OpenAI du 3 septembre confirme le lancement de GPT-6 Astra et ses améliorations de performance. Cependant, [l'annonce](https://openai.com/index/gpt-6-astra/) et la [fiche système](https://deploymentsafety.openai.com/gpt-6-astra) examinées ici ne divulguent ni une architecture de type transformeur en boucle, ni le nombre de récurrences, ni le total des paramètres actifs.

Nous ne considérons donc pas le lien entre Astra et une conception de type Huginn comme un fait établi. Les affirmations de taille 10T/1T figurant dans l'essai, ainsi que la citation sur l'AGI, sont également exclues des prémisses de cette analyse. De meilleures performances seules ne permettent pas d'identifier l'architecture interne.

Il existe néanmoins une bonne raison d'étudier la récurrence. Des modèles publics montrent déjà des tentatives de dissocier la capacité en paramètres stockés et la quantité de calcul à l'inférence. Cette évolution peut être évaluée sans s'appuyer sur la conception non divulguée d'un modèle de frontière.

## Stocker davantage et calculer plus longtemps sont deux choix distincts

Les paramètres sont les poids numériques ajustés lors de l'entraînement. Agrandir un modèle augmente généralement la quantité stockée. Le Mixture of Experts, ou MoE, sélectionne certains modules experts pour chaque entrée, dans le but d'exécuter moins de calcul relativement à la capacité totale du modèle.

Le MoE ne tire pas son origine du seul Switch Transformer. Le [papier sur le MoE à gating clairsemé de 2017](https://arxiv.org/abs/1701.06538) a précédé le [Switch Transformer de 2021](https://arxiv.org/abs/2101.03961), qui a simplifié le routage et l'entraînement à grande échelle. Un nombre total de paramètres plus élevé ne signifie pas nécessairement plus de couches.

Le raisonnement par chaîne de pensée (CoT) génère des tokens intermédiaires qui étendent le contexte pour les calculs ultérieurs. Un modèle en boucle fait repasser son état interne à travers un bloc à poids partagés. Le calcul intermédiaire n'a pas besoin d'être converti en mot à chaque étape. Ces approches peuvent également être combinées.

Comparer ce qu'apporte chaque approche permet de clarifier les arbitrages.

| Approche | Ce qui augmente | Coût potentiel |
|---|---|---|
| Modèle plus grand | Poids ou capacité des experts | Stockage, calcul actif, communication |
| Chaîne de pensée | Tokens de raisonnement intermédiaire | Temps de génération, contexte et cache |
| Profondeur récurrente | Passages à travers un bloc partagé | Calcul répété, latence, gestion d'état |

Il s'agit d'une comparaison conceptuelle. L'économie réelle nécessite des mesures à précision, longueur d'entrée et conditions matérielles équivalentes.

## La recherche sur « réfléchir avant de répondre » utilise des mécanismes distincts

Les [pause tokens](https://arxiv.org/abs/2310.02226) fournissent un calcul supplémentaire avant une réponse. [Quiet-STaR](https://arxiv.org/abs/2403.09629) apprend à générer des raisonnements intermédiaires qui aident à prédire les tokens suivants. Son nom ne doit pas être lu comme la preuve qu'il recourt à un raisonnement non verbal en état continu.

[Coconut](https://arxiv.org/abs/2412.06769) réinjecte l'état caché final en entrée sans le convertir en mot. Ce mécanisme explore la conservation de possibilités dans une représentation interne avant de s'engager dans le langage. Ce n'est pas une preuve de conscience humaine ni d'une pensée autonome en fonctionnement continu.

La recherche sur la profondeur récurrente inclut le [Universal Transformer de 2018](https://arxiv.org/abs/1807.03819), qui répète une transformation et peut allouer le calcul différemment selon les positions. La difficulté réside dans l'entraînement d'une répétition utile : un bloc partagé doit gérer des états issus d'étapes différentes, et un passage supplémentaire doit améliorer le résultat. Des rôles de couches conflictuels constituent une intuition utile, et non une explication universelle de chaque échec.

## Copier des couches diffère du partage des mêmes poids

Le [SOLAR 10.7B](https://arxiv.org/abs/2312.15166) d'Upstage a introduit le depth up-scaling, ou DUS : copier des couches existantes, en supprimer certaines, les assembler en un modèle plus profond et poursuivre l'entraînement. Des copies initialement identiques peuvent développer des poids différents. Le modèle résultant stocke davantage de paramètres.

Un modèle récurrent continue de partager les mêmes poids. Le DUS réutilise l'entraînement antérieur pour construire un modèle plus profond ; la mise en boucle augmente la profondeur d'exécution sans expansion correspondante des poids stockés. Traiter les deux comme la même technique d'économie de mémoire conduit à un modèle de coût erroné.

## Lisez les chiffres de Huginn et d'Ouro avec leurs conditions de comparaison

La [recherche Huginn](https://arxiv.org/abs/2502.05171) de Geiping et ses collègues sépare le traitement de l'entrée, un noyau récurrent et le traitement de la sortie. Le noyau affine l'état interne par exécutions répétées. Les auteurs ont entraîné un modèle de 3,5 milliards de paramètres sur 800 milliards de tokens et ont rapporté une amélioration des performances sur les tâches de raisonnement à mesure que le calcul récurrent augmentait.

Le chiffre de 50B dans le résumé appelle à la prudence. Il décrit des améliorations jusqu'à une charge computationnelle équivalente à 50 milliards de paramètres. Il ne garantit pas la qualité d'un modèle de 50B sur chaque tâche, ni que cette qualité soit obtenue au même coût. Un petit ensemble de poids utilisant davantage de calcul est un résultat de recherche ; l'économie de service nécessite des mesures séparées.

[Ouro](https://arxiv.org/abs/2510.25741), issu de ByteDance et de collaborateurs, a été publié en octobre 2025. Le papier couvre une famille de modèles de 1,4B et 2,6B paramètres et rapporte des comparaisons avec des modèles allant jusqu'à 12B sur différents benchmarks. La [fiche officielle du modèle Ouro-1.4B](https://huggingface.co/ByteDance/Ouro-1.4B) indique cependant que ce modèle particulier est à la hauteur des modèles conventionnels de 3 à 4B. Affirmer que 1,4B remplace systématiquement 12B serait exagérer la comparaison.

Les nombres de paramètres doivent être lus conjointement avec les données d'entraînement, le nombre de récurrences et les tâches d'évaluation. L'efficience apparente à l'inférence peut également faire suite à un investissement substantiel en pré-entraînement.

## Moins de poids stockés n'élimine pas les goulots d'étranglement mémoire

Considérons un calcul illustratif. Stocker 3,5 milliards de paramètres à 2 octets chacun nécessite environ 7 Go pour les poids. L'utilisation répétée de ces poids ne multiplie pas leur besoin de stockage par le nombre de récurrences. C'est de l'arithmétique, pas une mesure de l'utilisation totale de mémoire GPU de Huginn.

La mémoire totale à l'inférence comprend également le cache KV utilisé pour réutiliser le contexte antérieur, les états intermédiaires et l'espace de travail d'exécution. Le [guide d'optimisation de l'inférence de NVIDIA](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/) distingue les poids et le cache KV comme principaux composants mémoire. Des contextes plus longs et davantage de requêtes concurrentes augmentent la pression sur le cache. La possibilité de partager les caches entre étapes récurrentes dépend de la conception.

La réutilisation des poids est également distincte d'une réduction des mouvements de données. Si les poids ne peuvent pas rester en mémoire rapide sur puce, un nouveau passage peut nécessiter de les relire depuis la HBM. La répétition peut accroître la demande en bande passante en plus du calcul. Sans examiner la hiérarchie mémoire et l'implémentation, il est impossible d'affirmer que la mise en boucle rend la HBM superflue.

## Le logiciel doit concrétiser les économies issues de la sortie anticipée

Le [Mixture-of-Recursions (MoR)](https://arxiv.org/abs/2507.10524) fait varier la profondeur récursive par token et gère le calcul et la mise en cache autour des tokens encore actifs à une profondeur donnée. L'objectif est de diriger le calcul vers les tokens plus difficiles plutôt que de le dépenser sur les tokens faciles.

Le service en production complique les choses. Des exigences de récurrence différentes entre requêtes peuvent réduire l'efficacité du batching. Les ordonnanceurs doivent permettre à d'autres tâches d'utiliser les ressources libérées par l'achèvement anticipé. Il s'agit d'un défi opérationnel anticipé, pas d'un résultat mesuré pour un produit commercial particulier.

La fiche du modèle Ouro en offre un exemple concret. Le modèle prend en charge la sortie anticipée, mais la fiche indique que vLLM ne supporte pas cette fonctionnalité et exécute à la place le nombre complet de récurrences configuré. Une capacité architecturale n'est pas automatiquement implémentée dans un moteur de service.

Cela soulève des questions précises pour les entreprises d'infrastructure logicielle IA telles que Lablup : la plateforme peut-elle grouper des tâches avec des profondeurs de récurrence différentes, réutiliser les caches et réduire le temps de complétion et la consommation énergétique à qualité équivalente ? Ce sont des questions pour évaluer une opportunité, pas des affirmations que Lablup supporte déjà ces fonctionnalités ou a démontré une croissance de ses revenus grâce à elles.

## Les semi-conducteurs coréens font face à la fois à des économies de ressources et à une expansion des usages

Les éléments suivants sont des scénarios conditionnels pour une adoption plus large des modèles en boucle, et non des prévisions de résultats.

| Condition | Effet sectoriel possible | Preuve nécessaire |
|---|---|---|
| Moins de poids et moins de cache à qualité équivalente | Moindre pression mémoire par requête | Mémoire mesurée à contexte et concurrence égaux |
| Plus de récurrence sur les problèmes difficiles | Plus de temps accélérateur et d'énergie demandés | Temps GPU et énergie par tâche réussie |
| Un coût plus bas élargit les usages | Demande agrégée d'infrastructure stable ou plus élevée | Données réelles d'usage et plans d'achat des clients |
| Récurrence et gestion du cache réduisent l'efficacité du batching | Commercialisation retardée | Débit à la même cible de latence |

Pour les fournisseurs de mémoire tels que Samsung Electronics et SK hynix, la demande agrégée dépend à la fois des ressources par requête et du nombre de requêtes. L'efficience peut stimuler l'adoption, mais il ne faut pas supposer que cette croissance dépassera les économies réalisées. Cette seule analyse est insuffisante pour réviser les prévisions de demande de HBM ou les prévisions de résultats des entreprises.

Une comparaison plus pertinente est le coût de réalisation d'une tâche réussie. Des scores élevés sur les benchmarks peuvent rester coûteux si la répétition prend trop de temps ou si les nouvelles tentatives sont fréquentes. À l'inverse, un calcul supplémentaire peut réduire le coût total s'il améliore suffisamment le taux de succès au premier essai.

## Le prochain test porte sur le coût par tâche, pas sur le nombre de paramètres

Valider le cas industriel nécessite de comparer la mémoire totale, le temps de complétion, l'énergie et le débit concurrent à précision équivalente. La latence de queue compte autant que les moyennes pour les questions simples. Si davantage de récurrence cesse d'améliorer la qualité, ou si les pertes de batching dépassent les économies de ressources, le cas de commercialisation s'affaiblit.

De nouvelles divulgations architecturales pourraient établir si Astra appartient à cette lignée de recherche. En attendant, un changement vérifiable demeure : la planification d'infrastructure doit considérer la durée de calcul allouée à chaque problème et le moment où s'arrêter, au même titre que la taille du modèle stocké. Transformer cette flexibilité en coûts réels réduits est un test conjoint du matériel et du logiciel.
