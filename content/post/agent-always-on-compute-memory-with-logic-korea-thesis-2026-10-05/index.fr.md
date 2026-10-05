---
title: "Le calcul s'économise, la mémoire s'accumule : pourquoi la mémoire coréenne intègre la logique à l'ère des agents"
date: 2026-10-05T22:20:00+09:00
categories: ["Exclusive Analysis", "AI Infrastructure", "Korean-Equities"]
tags: ["Mémoire", "Samsung Electronics", "SK hynix", "HBM", "HBM personnalisée", "Agents", "KV cache", "SSD d'entreprise", "HBF", "CXL", "Contrats d'approvisionnement à long terme"]
slug: "agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05"
description: "À mesure que les agents d'IA auxquels on délègue des tâches entières se multiplient, le calcul coûte moins cher tandis que le contexte et les connaissances s'accumulent. À partir de la séparation entre traitement par lots et temps réel, de la demande en CPU et en réseau, de la mémoire HBM et des SSD intégrant de la logique, ainsi que des contrats à long terme et des dépôts, cet article examine la thèse d'investissement dans la mémoire coréenne et la pérennité des bénéfices qu'exigent les cours actuels."
image: "cover.png"
draft: false
---

Même lorsqu'on soumet la même question au même modèle d'IA, le prix varie fortement selon le mode de traitement. Dans la grille tarifaire d'Anthropic, Opus 5.5 coûte la moitié du tarif standard en traitement par lots, qui permet de répondre dans la journée, et le double en mode rapide, qui garantit une réponse accélérée. Relire un contexte déjà traité coûte un vingtième du tarif standard.[^anthropic-pricing]

Cette grille résume la direction prise par les infrastructures d'IA. Les tâches non urgentes sont traitées à bas prix, les tâches urgentes à un prix élevé. Et ce qui coûte le moins cher, ce n'est pas de recalculer, mais de ressortir ce qui a été mémorisé.

<strong>Plus les agents auxquels on délègue des tâches entières se multiplient, plus le calcul gagne en efficacité et plus le contexte et les connaissances s'accumulent. La mémoire et le stockage qui les conservent passent de produits standardisés à des produits intégrant de la logique. Pour investir dans la mémoire coréenne, l'enjeu est moins le montant des bénéfices cette année que leur durée.</strong>

Les liens à vérifier s'enchaînent. L'infrastructure devient-elle un système de calcul permanent ? Le calcul gagne-t-il réellement en efficacité ? Qu'est-ce qui s'accumule ? L'intégration de logique dans la mémoire se traduit-elle par des ventes ? Cette valeur revient-elle aux entreprises coréennes ? Enfin, nous calculons le niveau de pérennité des bénéfices qu'impliquent les cours actuels de Samsung Electronics et SK hynix.

La date de référence de l'analyse est le 5 octobre 2026. Les cours correspondent à la clôture du 2 octobre ; aucune transaction n'a été enregistrée pendant la séance régulière coréenne du 5 octobre. Les annonces des entreprises, les prévisions des organismes d'étude et les hypothèses de calcul de cet article sont distinguées. Le tableau de sensibilité ci-dessous est un calcul de vérification, et non un objectif de cours.

<link rel="stylesheet" href="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/thesis.css">

## L'infrastructure passe de systèmes qui répondent aux requêtes à des systèmes qui poursuivent un objectif

Un chatbot ne calcule qu'à la réception d'une question. Un agent auquel on délègue une tâche fonctionne autrement. Une fois l'objectif confié par l'utilisateur, il établit un plan, utilise des outils, vérifie le résultat et recommence si nécessaire. Le travail continue même lorsque l'utilisateur ferme l'écran.

L'unité de charge change donc. À l'ère des chatbots, la charge se rapprochait du nombre d'utilisateurs connectés simultanément. À l'ère des agents, elle correspond davantage au nombre d'utilisateurs multiplié par le nombre d'objectifs confiés par utilisateur et par la durée pendant laquelle ces objectifs restent actifs. C'est le calcul permanent orienté vers un objectif.

Les produits et les tarifs en portent déjà la trace. Managed Agents d'Anthropic facture 0.08 dollar par heure de session active, en plus du prix des jetons. La documentation explique que ces sessions ne bénéficient pas de la remise pour traitement par lots parce qu'elles conservent leur état.[^anthropic-pricing][^managed-agents]

Lors de sa conférence développeurs de mai 2026, Google a présenté un agent personnel fonctionnant toute la journée sur une machine virtuelle dédiée. La même présentation indiquait que le volume mensuel de jetons traités était passé d'environ 480 trillions en mai 2025 à plus de 3.2 quadrillions en mai 2026, soit environ sept fois plus en un an. Ces chiffres sont ceux publiés par l'entreprise ; la part imputable aux agents n'a pas été communiquée.[^google-io]

La durée des tâches augmente elle aussi. Dans la mesure de janvier 2026 de l'institut d'évaluation METR, la durée des tâches que Claude Opus 4.5 pouvait achever avec une probabilité de 50 % était de 320 minutes en équivalent humain. Depuis 2024, cette durée doublait environ tous les 89 jours. METR reconnaît également l'incertitude qui concerne le haut de la distribution des tâches.[^metr]

La figure ci-dessous présente la chaîne logique de l'article. Chaque flèche représente un lien à vérifier, et non un fait établi.

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/chain.svg" alt="Chaîne logique reliant les agents délégués au calcul permanent, à l'efficacité de calcul et à l'accumulation d'états, puis à la mémoire intégrant de la logique et à la pérennité des bénéfices"><figcaption>Schéma conceptuel. L'augmentation de la demande et la captation de cette valeur par les fabricants de mémoire sont deux liens distincts. Sur mobile, faites défiler l'image horizontalement.</figcaption></figure>

## L'écart de prix entre tâches urgentes et non urgentes atteint un facteur quatre

Les tâches qui tournent en continu ne sont pas toutes urgentes. Il n'y a aucune raison d'utiliser la même infrastructure pour classer des documents pendant la nuit et pour répondre à un utilisateur qui attend. Les entreprises de modèles ont traduit cette différence dans leurs tarifs.

| Entreprise et modèle | Par lots ou lent | Standard | Rapide ou prioritaire | Lecture du contexte en cache |
|---|---:|---:|---:|---:|
| Anthropic Opus 5.5 | 0.5x | 1x | 2x | 0.05x |
| OpenAI gpt-6-astra | 0.5x | 1x | 2x | 0.1x |
| Google Gemini 3.1 Pro Preview | 0.5x | 1x | 1.8x | Frais de stockage distincts |

Les trois entreprises différencient le prix d'un même modèle selon sa vitesse de réponse. L'écart entre l'offre la moins chère et la plus chère va de 3.6 à 4 fois. Google facture aussi la durée de conservation du contexte dans le cache. La conservation du contexte est ainsi devenue un produit à part entière.[^anthropic-pricing][^openai-pricing][^google-pricing]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/pricing.svg" alt="Graphique en barres des multiples tarifaires du traitement par lots, du mode rapide et de la lecture du cache par rapport au tarif standard des entrées d'Anthropic Opus 5.5"><figcaption>Selon la grille tarifaire officielle d'Anthropic, consultée le 5 octobre 2026. Le tarif standard des entrées est fixé à 1. La lecture du cache correspond au tarif des entrées lorsque le contexte déjà traité est réutilisé.</figcaption></figure>

Cette différenciation compte pour les investisseurs en raison du taux d'utilisation des infrastructures. Une installation qui ne répond qu'à la demande en temps réel connaît de grands écarts d'activité entre le jour et la nuit. Si elle accepte à bas prix les tâches non urgentes pendant les périodes creuses, elle peut fonctionner toute la journée. Le calcul permanent augmente la demande, mais réduit aussi les périodes d'inactivité des installations.

## Les tâches répétitives passent aux petits modèles et au code

Si un agent effectue des dizaines de milliers de fois par jour le même type de tâche, il n'a pas de raison d'appeler à chaque fois le plus grand modèle. Les sous-tâches répétitives évoluent dans deux directions : de petits modèles spécialisés dans ces tâches, ou du code qui s'exécute sans modèle.

Les tarifs étayent le cas des petits modèles. Selon la grille d'OpenAI, les entrées de gpt-6-astra coûtent 10 dollars par million de jetons, contre 0.10 dollar pour gpt-6-luna. L'écart est de 100 fois au sein d'une même entreprise. Dans un article de 2025, des chercheurs de NVIDIA ont estimé que 40 à 70 % des appels d'agents pourraient être remplacés par de petits modèles spécialisés. Il s'agit d'une estimation de l'article, et non d'une proportion mesurée.[^openai-pricing][^nvidia-slm]

La documentation produit étaye le cas du code. La documentation Agent Skills d'Anthropic indique que les scripts intégrés aux compétences s'exécutent dans un shell et que seul leur résultat entre dans le contexte du modèle. Le code du script lui-même n'y entre pas. Une procédure que le modèle devait inférer à chaque fois est ainsi transformée en code fixé une fois pour toutes.[^agent-skills]

Skyvern, une entreprise d'automatisation Web, a publié les résultats d'une méthode qui transforme une tâche accomplie une première fois par un agent en code, puis la rejoue sans modèle. Le temps d'exécution est passé de 279 secondes à 120 secondes, et le coût par exécution de 0.11 dollar à 0.04 dollar. Il s'agit d'une mesure publiée par l'entreprise elle-même.[^skyvern]

Une distinction importante apparaît ici. Le calcul nécessaire à chaque tâche diminue. Mais le code figé, les poids des modèles spécialisés et les journaux d'exécution doivent être stockés quelque part. Le gain d'efficacité consiste à moins calculer et à davantage réutiliser ce qui a été conservé.

## Le GPU ne suffit pas à terminer le travail

Une tâche d'agent se divise en plusieurs étapes. Le GPU prend en charge la réflexion. Le CPU exécute les outils, manipule les fichiers et fait tourner le code dans un environnement isolé. Le réseau transfère les données entre ces étapes.

Cette année, plusieurs entreprises ont tenu des propos convergents sur la demande en CPU. Andy Jassy, directeur général d'Amazon, a déclaré lors de la présentation des résultats de juillet que la plupart des usages des outils par les agents s'exécutaient sur des CPU, et non sur des accélérateurs d'IA. Lisa Su, directrice générale d'AMD, a prévu en août que le marché des CPU pour serveurs atteindrait 220 milliards de dollars en 2030, les agents et les environnements d'exécution isolés en constituant la plus grande part. Ces deux déclarations sont des commentaires et des prévisions de dirigeants.[^amzn-call][^amd-call]

Des signaux concrets existent aussi. TrendForce a rapporté en avril que les prix des CPU pour serveurs avaient augmenté de 10 à 20 % depuis mars et que les délais de livraison étaient passés de 1 à 2 semaines à 8 à 12 semaines. Il s'agit d'une information de seconde main citant des médias taïwanais et japonais. NVIDIA a expédié le CPU Vera à 88 cœurs, explicitement destiné à l'exécution isolée d'agents.[^tf-cpu][^nvda-vera]

Le réseau n'est pas non plus limité à une seule catégorie. Les connexions entre puces au sein d'une baie, l'Ethernet entre baies et CXL pour étendre la mémoire sont utilisés ensemble. Lors de sa présentation des résultats de septembre, Broadcom a déclaré que le chiffre d'affaires de la mise en réseau pour l'IA dépassait 2.5 fois son niveau d'un an plus tôt et que la demande de lasers pour les communications optiques dépassait largement l'offre.[^avgo-call]

Des unités de traitement de données distinctes apparaissent également. En mars, NVIDIA a présenté une architecture fondée sur BlueField-4 pour gérer les données de contexte en amont du stockage et indiqué que les produits partenaires seraient commercialisés au second semestre 2026. Au 5 octobre, nous n'avons trouvé aucune donnée confirmant leur expédition et leur mise en service réelles.[^nvda-stx]

La conclusion n'est pas que le GPU perd de son importance. C'est que les GPU, CPU, unités de traitement des données et différents types de réseaux deviennent nécessaires ensemble. Et chacun de ces équipements s'accompagne de mémoire.

## Le calcul peut être réutilisé, tandis que le contexte et les connaissances s'accumulent

On peut résumer le raisonnement jusqu'ici en une phrase : l'infrastructure des agents augmente la mémoire pour éviter de refaire deux fois le même calcul.

Lorsqu'un modèle de langage lit un long contexte, il crée des résultats intermédiaires de calcul. On les appelle KV cache. En conservant ce cache, il n'est pas nécessaire de tout recalculer depuis le début lorsqu'on relit le même contexte. C'est pourquoi, dans la grille tarifaire évoquée au début, la lecture du contexte en cache coûte un vingtième du tarif standard.

Le cache n'est pas négligeable. Dans un document technique publié en juin, IBM a estimé qu'un cache KV par requête représentait environ 3 à 10 GB pour un modèle moyen et 40 à 80 GB pour un grand modèle. IBM a rapporté que la réutilisation du cache réduisait d'un facteur 56 le délai avant la première réponse pour une entrée de 130 000 jetons. Il s'agit d'une mesure propre à l'entreprise.[^ibm-kv]

NVIDIA a défini un nouvel étage de stockage pour ce cache. Sous la HBM du GPU et la mémoire du serveur, puis le SSD à l'intérieur du serveur, l'entreprise a placé une couche de stockage flash reliée par Ethernet, baptisée CMX. Elle a également publié un logiciel qui détermine à quel étage placer le cache.[^nvda-cmx][^nvda-dynamo]

Les présentations de résultats des fabricants de mémoire font état de la même tendance. Dans sa présentation du 30 septembre, Micron a déclaré que les ventes de SSD pour centres de données approchaient les 10 milliards de dollars sur le trimestre, soit plus de dix fois leur niveau un an plus tôt. L'entreprise a cité parmi les facteurs le stockage du contexte, qui consiste à transférer le KV cache vers des couches de stockage inférieures.[^mu-remarks]

Lors de la présentation de ses résultats de juillet, SK hynix a indiqué que les ventes de SSD d'entreprise avaient doublé par rapport au trimestre précédent et cité comme nouveaux usages le stockage du KV cache et les solutions de stockage proches des GPU. Samsung Electronics prévoit que les SSD pour serveurs représenteront plus de 60 % de son chiffre d'affaires NAND en 2026. Ces deux déclarations ont été vérifiées dans des médias qui ont republié les transcriptions des conférences téléphoniques.[^skh-call][^sec-call]

En août, le directeur général du fabricant de disques durs Western Digital a décrit cette différence ainsi : les cycles de calcul peuvent être réutilisés, mais les données s'accumulent de manière composée. Les agents conservent une trace à chaque étape, et cette trace devient la matière première de la tâche suivante.[^wdc-call]

Il faut toutefois distinguer le taux de croissance du montant. La mémoire d'un agent individuel ne représente pas un grand volume. Ce qui accroît les montants, c'est le passage de l'ensemble des services d'inférence à une architecture qui transfère le cache vers la mémoire flash. Cette transition en est encore à ses débuts.

## La mémoire passe des produits standardisés aux produits intégrant de la logique

À mesure que les données s'accumulent, les exigences des clients envers la mémoire changent. Ils ne demandent plus seulement quelle est sa capacité, mais s'ils peuvent récupérer les données à temps, quelle quantité d'énergie elle consomme et dans quelle mesure elle s'adapte à leurs puces. Répondre à ces exigences suppose d'intégrer de la logique dans la mémoire.

Dans son prospectus américain de juillet, SK hynix a décrit directement cette évolution. L'entreprise y écrit qu'autrefois les fabricants de mémoire fournissaient des composants à usage général, alors que la mémoire joue un rôle central dans l'optimisation des performances à l'ère de l'IA. Elle présente sa vision comme celle d'un créateur de mémoire d'IA complète. Il s'agit de la caractérisation de l'entreprise, à distinguer des faits démontrés par ses résultats.[^skh-424b4]

L'exemple le plus avancé est la puce de base de la HBM. La HBM est constituée de plusieurs couches de puces mémoire ; la puce de base, tout en bas, gère les signaux et l'alimentation électrique. Jusqu'à la génération précédente, elle était fabriquée avec un procédé mémoire. À partir de HBM4, elle est fabriquée avec un procédé logique. Samsung Electronics utilise son propre procédé de 4 nanomètres. En 2024, SK hynix a annoncé une collaboration pour fabriquer la puce de base HBM4 avec le procédé logique de TSMC.[^sec-hbm4][^skh-tsmc]

L'étape suivante est la HBM personnalisée, qui intègre la logique du client à la puce de base. Le 26 août, NVIDIA a annoncé NVHBM, qui intègre ses circuits de contrôle mémoire dans la puce de base de la HBM. NVIDIA affirme que le produit offre une bande passante supérieure de 30 % et consomme 15 % d'énergie en moins que la HBM4E standard. Le 30 septembre, Micron a déclaré développer ce produit avec NVIDIA.[^nvda-nvhbm][^mu-remarks]

En août, lors de la conférence Hot Chips, Samsung Electronics a présenté l'étape suivante : déplacer les circuits de contrôle, intégrer des éléments de calcul dans la puce de base pour prendre en charge une partie des calculs du processeur, puis empiler directement la mémoire au-dessus de la puce de calcul. Aucun calendrier de commercialisation n'a été communiqué.[^sec-hotchips]

Des produits suivant la même orientation apparaissent dans le stockage et d'autres types de mémoire. Leur niveau de maturité varie toutefois fortement.

| Produit | Logique intégrée | Stade actuel |
|---|---|---|
| Puce de base HBM4 | Contrôle des signaux et de l'alimentation par procédé logique | Production de masse, chiffre d'affaires généré |
| SOCAMM2 | Module mémoire basse consommation pour serveurs | Production de masse, ventes en hausse |
| SSD d'entreprise | Puce de contrôle, micrologiciel et conception pour le stockage du contexte | Production de masse, forte hausse du chiffre d'affaires |
| HBM personnalisée, NVHBM | Circuits de contrôle mémoire du client | En développement, application prévue aux prochains GPU |
| Module mémoire CXL | Circuit de surveillance identifiant les données fréquemment utilisées | Samsung viserait une production de masse fin 2026 selon la presse ; retard possible |
| HBF | Interface à large bande passante rapprochant la NAND de la puce de calcul | Première spécification technique publiée en août 2026, avant le produit |
| PIM, HBM avec éléments de calcul intégrés | Circuits de calcul à l'intérieur de la mémoire | Prototypes et feuille de route |

Les produits indiqués en production de masse sont confirmés par les documents de résultats de cette année. Les documents de résultats du deuxième trimestre de Samsung Electronics mentionnent la hausse de la demande en puces de base HBM comme facteur de performance de l'activité fonderie. Les produits à partir de la HBM personnalisée ne sont pas encore confirmés par le chiffre d'affaires. SK hynix a indiqué qu'elle conserverait la méthode d'assemblage actuelle jusqu'à HBM4E, et une analyse présentée lors d'un événement sectoriel en septembre a décrit CXL comme une couche complémentaire, et non comme un substitut à la HBM.[^sec-ir][^skh-q2][^tf-cxl][^hbf-ocp][^sec-fms][^skh-hybrid][^tf-cxl-doubt]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/maturity.svg" alt="Produits mémoire intégrant de la logique répartis en trois étapes : chiffre d'affaires généré, développement et échantillons, feuille de route"><figcaption>Classification des étapes à partir des annonces et des documents de résultats des entreprises. Les éléments à gauche sont confirmés dans les résultats de cette année ; plus on va vers la droite, moins les calendriers sont définis. Situation au 5 octobre 2026.</figcaption></figure>

Ainsi, dire que la mémoire intègre de la logique décrit bien une tendance, mais sa portée reste limitée. Les ventes actuellement confirmées concernent HBM4, les modules pour serveurs et les SSD d'entreprise. La DRAM et la NAND standard restent en concurrence sur les spécifications et les prix.

## L'hypothèse d'une mémoire au cœur du calcul n'est confirmée que dans son orientation

Une hypothèse plus lointaine est que la structure même du calcul change. Aujourd'hui, l'ordinateur est centré sur les unités de calcul, auxquelles la mémoire apporte les données. Si les données augmentent plus vite que le calcul, leur transfert peut coûter plus cher que leur traitement. Il devient alors préférable de calculer là où se trouvent les données.

Plusieurs initiatives suivent cette direction. La dernière étape de la feuille de route de Samsung empile directement la mémoire au-dessus de la puce de calcul. Qualcomm a annoncé l'intégration en trois dimensions du calcul et de la mémoire dans un produit prévu pour 2027. SK hynix et Sandisk élaborent avec Google et Tenstorrent une norme qui place la NAND juste à côté de la puce de calcul.[^sec-hotchips][^qcom-hbc][^hbf-ocp]

En août, lors de la présentation des résultats, le directeur général de Sandisk a décrit l'IA comme un problème fondamentalement centré sur la mémoire et très demandeur en stockage. Il faut tenir compte du fait que ces propos viennent du dirigeant d'un fabricant de mémoire.[^sndk-call]

Je précise clairement mon appréciation de cette hypothèse. En 2026, le calcul centré sur la mémoire constitue une option, et non un argument d'investissement. Il n'existe ni validation indépendante des performances, ni calendrier de production de masse, ni adoption confirmée par les clients. Ce n'est pas un élément permettant d'expliquer les cours actuels. Si cette orientation se confirme, les entreprises réunissant mémoire, procédés logiques et empilement devraient toutefois en être les principales bénéficiaires.

## La thèse d'investissement dans la mémoire coréenne passe du montant des bénéfices à leur durée

Passons maintenant aux entreprises coréennes. Les bénéfices de cette année sont déjà élevés. Au deuxième trimestre, la division semi-conducteurs de Samsung Electronics a dégagé un résultat opérationnel de 89.2 trillions KRW, soit 70 % de son chiffre d'affaires. Le résultat opérationnel de SK hynix était de 60.5 trillions KRW, soit 76 % de son chiffre d'affaires.[^sec-ir][^skh-q2]

Les cours accordent pourtant une faible valeur à ces bénéfices. À la clôture du 2 octobre, Samsung Electronics se négociait à 5.85 fois les bénéfices prévus pour 2026, et SK hynix à 5.25 fois. Ces bénéfices prévisionnels correspondent à la moyenne des analystes compilée par Naver Finance.[^naver-sec][^naver-skh]

Ces faibles multiples peuvent être interprétés comme le signe que le marché considère encore la mémoire comme un secteur cyclique. La crainte est que les bénéfices actuels proviennent d'une pénurie d'offre et s'effondrent comme auparavant une fois les capacités supplémentaires mises en service. Cette interprétation repose sur un élément concret : SK hynix mentionne elle-même dans les facteurs de risque de son prospectus les épisodes répétés de surcapacité dans le secteur de la mémoire.[^skh-424b4]

C'est là que la mémoire intégrant de la logique devient importante pour l'investissement. Cette évolution n'augmente pas les bénéfices de cette année. L'enjeu est qu'elle puisse créer des raisons pour lesquelles les bénéfices ne retomberaient pas autant qu'auparavant une fois l'offre normalisée. Ces raisons tiennent aux coûts de changement et à la structure des contrats.

Premièrement, il devient plus difficile pour le client de changer de fournisseur. Une puce de base conçue pour la puce du client ne peut pas être remplacée facilement par celle d'une autre entreprise. Le temps consacré à la conception, à la validation et à la certification crée un coût de changement. Le montant réel de ce coût et sa répercussion sur les prix restent des hypothèses non vérifiées.

Deuxièmement, la structure des contrats. Le 30 septembre, Micron a déclaré avoir conclu 26 contrats avec des clients stratégiques. Les clients doivent payer même s'ils n'achètent pas les volumes promis sur plusieurs années. Les engagements financiers confiés par les clients s'élèvent à 32 milliards de dollars, principalement sous forme de dépôts en espèces. Micron affirme que cette visibilité justifie une hausse des investissements en capacité.[^mu-remarks]

Les deux entreprises coréennes suivent la même orientation. SK hynix a déclaré avoir achevé au deuxième trimestre des négociations de contrats d'approvisionnement à long terme avec une dizaine de clients et précisé lors de sa conférence téléphonique que ces accords comprenaient des mécanismes financiers tels que des dépôts. Samsung Electronics prévoit d'allouer 60 à 70 % de sa capacité à des contrats à long terme, sur une base initiale de cinq ans renouvelée chaque année. Les prix et les conditions d'annulation propres à chaque contrat n'ont pas été divulgués.[^skh-q2][^skh-lta][^sec-lta]

Un secteur où les clients déposent de l'argent à l'avance et s'engagent sur des volumes fonctionne différemment d'un marché où les produits standardisés s'échangent au comptant. Les contrats à long terme ont toutefois deux faces. TrendForce indique que, du fait de leurs mécanismes de prix, les hausses du prix de la DRAM pour serveurs de certains fournisseurs sont inférieures à la moyenne du marché. En échange d'un plancher en période de baisse, ils cèdent une partie du sommet en période de hausse.[^tf-memory]

## Samsung Electronics et SK hynix occupent des positions différentes face à la même évolution

Les deux entreprises ont des forces et des faiblesses différentes face à cette même évolution vers une mémoire intégrant de la logique.

| Élément | Samsung Electronics | SK hynix |
|---|---|---|
| Marge opérationnelle des semi-conducteurs au T2 | 70 % | 76 % |
| Puce de base HBM4 | Procédé maison de 4 nm | Procédé TSMC |
| Captation de la valeur de la logique, analyse de cet article | Peut rester en interne via l'activité fonderie | Coût payé à l'extérieur |
| Étendue de l'offre | HBM, modules pour serveurs, SSD, fonderie, assemblage | HBM, modules pour serveurs, SSD, leadership sur la norme HBF |
| Contrats à long terme | Projet d'allocation de 60 à 70 % de la capacité | Négociations achevées avec une dizaine de clients |
| Rémunération des actionnaires | Dividende d'environ 30 trillions KRW prévu au T3 | Annulation décidée d'actions propres pour 40 trillions KRW |
| Cours rapporté aux bénéfices prévus pour 2026 | 5.85 fois | 5.25 fois |

La force de SK hynix réside dans sa rentabilité actuelle et ses relations avec les clients. Sa marge opérationnelle est plus élevée et ses négociations de contrats à long terme avec une dizaine de clients sont achevées. Sa faiblesse tient au fait qu'elle paie la valeur de la logique à l'extérieur. Selon TrendForce, qui cite des médias coréens, le coût de la puce de base HBM4 fabriquée par TSMC représente 3 à 4 fois celui de la puce mémoire. Ce chiffre n'a pas été confirmé par l'entreprise.[^tf-basedie]

La force de Samsung Electronics tient à une structure où la valeur de la logique peut rester dans l'entreprise. Samsung se présente comme la seule entreprise à réunir mémoire, conception logique, fonderie et assemblage.[^sec-fms] Sa faiblesse est que cette structure n'a pas encore suffisamment démontré sa rentabilité. Il ne faut pas compter deux fois le chiffre d'affaires d'une puce de base fabriquée en interne comme s'il s'agissait d'argent gagné auprès d'un client externe. Il faut examiner les coûts et la trésorerie consolidés.

La rémunération des actionnaires est un moyen de leur restituer les bénéfices. En août, SK hynix a décidé de racheter pour 40 trillions KRW d'actions propres et de les annuler intégralement. Elle a également relevé son objectif de distribution des flux de trésorerie disponibles à au moins 50 %. Samsung Electronics prévoit un dividende en espèces d'environ 30 trillions KRW au troisième trimestre, qui sera confirmé par le conseil d'administration fin octobre. Ces deux éléments ont été vérifiés dans la presse ; les textes originaux des annonces réglementaires n'ont pas été comparés.[^skh-return][^sec-return]

Voici mon appréciation. Plus l'intégration de logique dans la mémoire progresse, plus la structure favorise l'entreprise qui fabrique cette logique en interne. Au vu des résultats et de la position auprès des clients, SK hynix est actuellement en tête. Au début de la transition, sa capacité d'exécution est un avantage. À mesure que la HBM personnalisée et les étapes suivantes prendront de l'ampleur, l'intégration de Samsung Electronics pourrait avoir davantage de valeur. Le point de bascule sera la production de masse de puces de base fabriquées par la fonderie de Samsung à partir de conceptions de clients externes.

## Les cours actuels supposent qu'à peine plus de la moitié des bénéfices de cette année subsistera

On peut simplifier le cours d'une action en le représentant comme le produit des bénéfices durables auxquels croit le marché et d'un multiple de valorisation. En supposant que le marché attribue un multiple de 10 fois à une entreprise de mémoire et en remontant le calcul, on obtient le niveau de bénéfices qu'exige le cours actuel.

Le cours de clôture de Samsung Electronics au 2 octobre était de KRW 276,000. Avec un multiple de 10, le bénéfice par action requis par le cours est de KRW 27,600, soit 58.5 % du bénéfice par action prévu pour 2026, de KRW 47,142. Le cours de SK hynix était de KRW 1,842,000. Le même calcul donne un bénéfice par action requis de KRW 184,200, soit 52.5 % du bénéfice prévu de KRW 350,576.[^naver-sec][^naver-skh]

Autrement dit, les cours actuels sont compatibles avec l'hypothèse que seule un peu plus de la moitié des bénéfices de 2026 subsistera à l'avenir. Cela ne signifie pas que le marché raisonne exactement ainsi. Il existe plusieurs combinaisons de multiples et de bénéfices. Mais la question est claire : les produits intégrant de la logique et les contrats à long terme peuvent-ils maintenir les bénéfices normalisés au-dessus de la moitié de leur niveau de cette année ?

Le tableau ci-dessous fait varier la proportion des bénéfices prévus pour 2026 qui subsiste et le multiple de valorisation. Les pourcentages entre parenthèses indiquent la variation par rapport au cours de clôture du 2 octobre. La proportion conservée et le multiple sont des hypothèses de calcul de cet article ; aucune probabilité ne leur est attribuée. Les dividendes ne sont pas inclus.

Samsung Electronics, cours de référence : KRW 276,000

| Part des bénéfices prévus pour 2026 conservée | 8 fois | 10 fois | 12 fois |
|---|---:|---:|---:|
| 40 % | KRW 151,000 (-45.3%) | KRW 189,000 (-31.7%) | KRW 226,000 (-18.0%) |
| 55 % | KRW 207,000 (-24.8%) | KRW 259,000 (-6.1%) | KRW 311,000 (+12.7%) |
| 70 % | KRW 264,000 (-4.3%) | KRW 330,000 (+19.6%) | KRW 396,000 (+43.5%) |

SK hynix, cours de référence : KRW 1,842,000

| Part des bénéfices prévus pour 2026 conservée | 8 fois | 10 fois | 12 fois |
|---|---:|---:|---:|
| 40 % | KRW 1,122,000 (-39.1%) | KRW 1,402,000 (-23.9%) | KRW 1,683,000 (-8.6%) |
| 55 % | KRW 1,543,000 (-16.3%) | KRW 1,928,000 (+4.7%) | KRW 2,314,000 (+25.6%) |
| 70 % | KRW 1,963,000 (+6.6%) | KRW 2,454,000 (+33.2%) | KRW 2,945,000 (+59.9%) |

Les deux extrêmes du tableau éclairent le débat. Si seuls 40 % des bénéfices subsistent, le cours baisse même si le multiple atteint 12 fois. Un récit favorable sur le secteur ne compense pas la baisse des bénéfices. À l'inverse, si le marché croit que 70 % des bénéfices subsisteront, le cours est supérieur de 20 à 33 % même avec un multiple inchangé de 10 fois.

Les chiffres de SK hynix appellent une réserve. Son bénéfice net du deuxième trimestre, à 93.9 trillions KRW, dépassait son résultat opérationnel de 60.5 trillions KRW. Nous n'avons pas pu en vérifier la cause. Si ce bénéfice provient d'éléments hors exploitation, le bénéfice par action annuel prévisionnel peut inclure des gains non récurrents. Dans ce cas, il faudrait retenir une proportion plus faible des bénéfices.[^skh-q2]

La clé d'une revalorisation n'est pas le multiple, mais la part des bénéfices qui subsistera. La mémoire intégrant de la logique et les contrats à long terme peuvent contribuer à l'augmenter. On saura si c'est le cas lorsque l'offre augmentera en 2027 et 2028.

## La principale objection est que la valeur de la logique revient à celui qui la conçoit

Cette thèse fait face à une objection forte. Je commence par la plus importante.

La première concerne la captation de la valeur. Dans NVHBM, NVIDIA a conçu les circuits de contrôle intégrés à la puce de base. L'entreprise a indiqué que plusieurs fabricants de mémoire fourniraient le même format. Micron confie la fabrication de cette puce de base à une fonderie externe. Dans cette structure, la valeur de la conception revient à NVIDIA, celle de la fabrication à la fonderie, et les fabricants de mémoire peuvent se retrouver à nouveau en concurrence sur le même produit standard.[^nvda-nvhbm][^mu-foundry]

Un phénomène similaire se produit dans le stockage. Dans l'architecture de stockage du contexte de NVIDIA, le calcul qui gère les données est assuré par le processeur de traitement des données de NVIDIA, et non par le SSD. Le logiciel qui détermine l'étage où placer le cache appartient également à NVIDIA. Le lieu où les données s'accumulent peut différer de celui qui rend le client captif.[^nvda-cmx][^nvda-dynamo]

C'est l'objection qui fragilise le plus la thèse de cet article. L'intégration de logique dans la mémoire et la propriété de cette logique par le fabricant de mémoire sont deux choses distinctes. Cette objection explique pourquoi l'article met l'accent sur l'intégration de Samsung Electronics. Un fabricant de mémoire incapable de produire directement la logique pourrait se retrouver dans une position encore plus étroite à mesure que les produits se sophistiquent.

La deuxième objection concerne l'adaptation de la demande. Lorsque la mémoire devient chère, les clients cherchent à en utiliser moins. Le 29 septembre, TrendForce a indiqué que les fabricants de GPU et de puces personnalisées envisageaient de réduire la capacité HBM par appareil et privilégiaient l'évaluation de configurations à 8 couches pour 2027. En mars, des chercheurs de Google ont présenté une méthode de compression réduisant à un sixième ou moins l'utilisation mémoire du KV cache. La documentation d'Anthropic indique qu'une fenêtre de contexte plus longue peut réduire la précision et propose de résumer les conversations anciennes.[^tf-hbm][^turboquant][^anthropic-context]

Nous ne savons pas encore si l'accumulation sera plus rapide que les technologies de réduction. Micron a également reconnu que le taux de croissance de la mémoire par serveur avait quelque peu diminué sous l'effet des prix.[^mu-remarks]

La troisième objection concerne l'offre et le financement. Le 30 juillet, TrendForce a prévu un assouplissement de l'offre de NAND au second semestre 2027 et une pression à la baisse sur les prix. Selon TrendForce, la part de CXMT dans les ventes de DRAM au deuxième trimestre a atteint 9.5 %. Le 10 septembre, le directeur général de la Banque des règlements internationaux a averti dans un discours que les investissements des grandes entreprises technologiques dépassaient leurs flux de trésorerie. Si les clients manquent de liquidités, leurs engagements dans les contrats à long terme seront eux aussi mis à l'épreuve.[^tf-supply][^tf-china][^bis]

Micron prévoit au contraire un équilibre offre-demande plus tendu en 2027 et 2028 qu'en 2026. Le désaccord entre les prévisions des organismes d'étude et celles des fournisseurs est en lui-même une raison de ne pas tirer de conclusion définitive sur 2027.[^mu-remarks]

L'hypothèse de demande doit également être éprouvée. Cet article part du principe que les utilisateurs continueront de confier des tâches aux agents. Dans les données d'utilisation internes publiées par Anthropic en février, les tâches durant plus de 45 minutes d'affilée se situaient dans le 0.1 % supérieur. La plupart des tâches sont beaucoup plus courtes. Si la délégation ne devient pas une habitude ou si les utilisateurs ne confient pas leurs autorisations, le développement du calcul permanent sera plus lent que ne le suppose cet article.[^anthropic-autonomy]

## Au prochain trimestre, nous vérifierons les preuves de bénéfices durables, pas seulement les prix

Les prochains chiffres permettront de vérifier cette thèse. Voici les éléments à suivre et les conditions susceptibles de modifier l'appréciation.

| Élément à vérifier | Signal favorable à la thèse | Signal qui l'affaiblit |
|---|---|---|
| Résultats du T3, octobre | Hausse des volumes de HBM4 et de SSD d'entreprise, amélioration de la composition des ventes | La hausse des bénéfices provient surtout des prix des produits standardisés |
| Contrats à long terme | Divulgation des dépôts et des achats minimaux, renouvellement des contrats | Abandon de bénéfices en raison de plafonds de prix, maintien de l'opacité des conditions |
| HBM personnalisée | Production de masse par la fonderie Samsung pour des clients externes | Concurrence par les prix entre trois fournisseurs sur une norme unique |
| Stockage du contexte | Expédition des produits partenaires CMX, contrats de serveurs de stockage dédiés | Diffusion des technologies de compression, retards d'expédition |
| Offre en 2027 | Poursuite de la hausse des prix contractuels, hausse des investissements prévus par les clients | Baisse des prix de la NAND, réduction de la capacité HBM par appareil |

La presse a annoncé les résultats préliminaires du troisième trimestre de Samsung Electronics pour le 8 octobre. La moyenne du résultat opérationnel compilée par FnGuide est de 108.1 trillions KRW. Les résultats de SK hynix sont attendus fin octobre et la moyenne de son résultat opérationnel est de 77.2 trillions KRW. Ces deux informations sont rapportées par la presse au 5 octobre ; nous n'avons pas vérifié les annonces de calendrier officielles des entreprises.[^consensus]

Le contenu compte davantage que le chiffre lui-même. Même si le résultat opérationnel dépasse la moyenne, une hausse due uniquement aux prix des produits standardisés n'a aucun rapport avec la thèse de cet article. À l'inverse, même si le résultat opérationnel est inférieur à la moyenne, une amélioration des volumes HBM4 et de la qualité des contrats à long terme renforcerait les raisons de croire à des bénéfices durables.

Je précise également les conditions qui me feraient changer d'avis. Si la HBM personnalisée se fige en une norme unique, que les trois fabricants de mémoire se font concurrence sur le même produit et que les prix contractuels de 2027 commencent à baisser, il faudra abaisser d'un cran la conviction portée par cette thèse. La mémoire coréenne serait alors valorisée comme un secteur cyclique, malgré des produits plus sophistiqués.

<strong>Les agents utilisent la mémoire pour économiser du calcul. De la logique entre dans les produits qui conservent cette mémoire, et certains clients commencent à déposer des fonds à l'avance. La revalorisation de la mémoire coréenne dépendra de la capacité de ces évolutions à préserver les bénéfices après l'augmentation de l'offre ; les cours actuels ne reflètent encore qu'un peu plus de la moitié des bénéfices de cette année.</strong>

## Sources et limites des calculs

Les annonces des entreprises, les publications réglementaires et les documents des organismes d'étude ont été comparés au 5 octobre 2026. Les déclarations vérifiées dans des médias ayant republié des transcriptions d'appels sont signalées dans les notes. Les performances annoncées par les entreprises ne constituent pas une validation indépendante. Les proportions de bénéfices conservées et les multiples du tableau de sensibilité sont des hypothèses de calcul, et non des prévisions. Les bénéfices par action prévisionnels reprennent tels quels les chiffres compilés par Naver Finance ; nous n'avons pas vérifié les prévisions pour 2027.

[^anthropic-pricing]: [Grille tarifaire officielle d'Anthropic](https://platform.claude.com/docs/en/about-claude/pricing), consultée le 2026-10-05. Pour Opus 5.5 : entrées standard à 4 dollars, traitement par lots à 2 dollars, mode rapide à 8 dollars, lecture du cache à 0.20 dollar par million de jetons. Frais de session Managed Agents inclus.

[^managed-agents]: [Documentation de présentation de Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), consultée le 2026-10-05. Documentation d'un produit en bêta.

[^google-io]: [Résumé du discours d'ouverture de Sundar Pichai à Google I/O 2026](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/), 2026-05. Chiffres publiés par l'entreprise.

[^metr]: [METR Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/), 2026-01-29. Horizon de durée des tâches au seuil de réussite de 50 %.

[^openai-pricing]: [Tarifs de l'API OpenAI](https://developers.openai.com/api/docs/pricing), consultés le 2026-10-05. Pour gpt-6-astra : standard 10 dollars, Flex 5 dollars, Fast 20 dollars et entrées en cache 1 dollar. Entrées gpt-6-luna : 0.10 dollar.

[^google-pricing]: [Tarifs de l'API Gemini](https://ai.google.dev/gemini-api/docs/pricing), mise à jour le 2026-10-01. Pour Gemini 3.1 Pro Preview : standard 2 dollars, traitement par lots 1 dollar, Priority 3.60 dollars et frais horaires de stockage du cache.

[^nvidia-slm]: [Les petits modèles de langage sont l'avenir de l'IA agentique](https://arxiv.org/abs/2506.02153), article de chercheurs de NVIDIA soumis le 2025-06-02. Il expose une position ; la proportion de 40 à 70 % est une estimation.

[^agent-skills]: [Documentation de présentation d'Anthropic Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), consultée le 2026-10-05.

[^skyvern]: [Mesure de rejeu de code publiée sur le blog de Skyvern](https://www.skyvern.com/blog/asking-ai-to-build-scrapers-should-be-easy-right/), publié le 2025-10-17, mis à jour le 2026-08-24. Mesure de l'entreprise.

[^amzn-call]: [Transcription republiée de la conférence téléphonique d'Amazon sur ses résultats du T2 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-amazon-tops-q2-2026-estimates-as-aws-growth-accelerates-93CH-4826442), 2026-07-30. Déclaration de la direction.

[^amd-call]: [Transcription republiée de la conférence téléphonique d'AMD sur ses résultats du T2 2026](https://www.fool.com/earnings/call-transcripts/2026/08/11/amd-amd-q2-2026-earnings-call-transcript/), conférence du 2026-08-04. Prévision de taille de marché de l'entreprise.

[^tf-cpu]: [Article de TrendForce sur les prix des CPU pour serveurs](https://www.trendforce.com/news/2026/04/22/news-server-cpu-prices-up-as-much-as-20-since-march-intel-may-raise-prices-another-8-10-in-2h26/), 2026-04-22. Informations citant des médias taïwanais et japonais.

[^nvda-vera]: [Annonce de NVIDIA sur les livraisons du CPU Vera](https://blogs.nvidia.com/blog/vera-cpu-delivery/), 2026-05-18.

[^avgo-call]: [Transcription republiée de la conférence téléphonique de Broadcom sur ses résultats du T3 FY2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/), conférence du 2026-09-02. Déclaration de la direction.

[^nvda-stx]: [Annonce de NVIDIA sur l'architecture de stockage BlueField-4 STX](https://nvidianews.nvidia.com/news/nvidia-launches-bluefield-4-stx-storage-architecture-with-broad-industry-adoption), 2026-03-16. Les chiffres de performance sont ceux de l'entreprise.

[^ibm-kv]: [Document technique IBM Redbooks sur le KV cache](https://www.redbooks.ibm.com/docs/MD260021/MD260021.html), publié le 2026-06-05. Mesures et estimations propres à l'entreprise.

[^nvda-cmx]: [Présentation du produit NVIDIA CMX](https://www.nvidia.com/en-us/data-center/ai-storage/cmx/), consultée le 2026-10-05. Date de publication non indiquée.

[^nvda-dynamo]: [Documentation NVIDIA Dynamo sur la hiérarchisation du KV cache](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/kv-cache-offloading), consultée le 2026-10-05. Aucun chiffre de performance dans la documentation.

[^mu-remarks]: [Commentaires préparés de Micron pour le T4 FY2026](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf), 2026-09-30. Les ventes de SSD pour centres de données sont décrites dans le texte original comme "nearly $10 billion". Les contrats stratégiques, dépôts, NVHBM et prévisions de l'offre et de la demande ont été comparés à ce document.

[^skh-call]: [Transcription republiée de la conférence téléphonique de SK hynix sur ses résultats du T2 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q2-2026-results-as-shares-fall-93CH-4818480), conférence de 2026-07. Il ne s'agit pas d'une transcription officielle de l'entreprise.

[^sec-call]: [Transcription republiée de la conférence téléphonique de Samsung Electronics sur ses résultats du T2 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q2-2026-profit-as-ai-demand-surges-93CH-4822292), conférence de 2026-07. Il ne s'agit pas d'une transcription officielle de l'entreprise.

[^wdc-call]: [Synthèse de la conférence téléphonique de Western Digital sur ses résultats du T4 FY2026](https://finance.biggo.com/news/US_WDC_2026-08-05), 2026-08-05. Déclaration vérifiée dans une synthèse secondaire.

[^skh-424b4]: [Prospectus américain de SK hynix, SEC 424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm), 2026-07-09. Les sections stratégie, définition de Custom HBM et facteurs de risque ont été comparées à l'original.

[^sec-hbm4]: [Annonce de Samsung Electronics sur l'expédition commerciale de HBM4](https://news.samsungsemiconductor.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/), 2026-02-12. Le procédé et les performances sont décrits par l'entreprise.

[^skh-tsmc]: [Annonce de collaboration HBM4 entre SK hynix et TSMC](https://www.prnewswire.com/news-releases/sk-hynix-partners-with-tsmc-to-strengthen-hbm-technological-leadership-302120755.html), 2024-04-18. Annonce de l'orientation du développement à cette date.

[^tf-basedie]: [Article de TrendForce sur les puces de base HBM4E de SK hynix](https://www.trendforce.com/news/2026/08/31/news-sk-hynix-reportedly-weighs-intel-for-hbm4e-base-dies-amid-tsmc-cost-pressure-and-supply-diversification/), 2026-08-31. Source médiatique coréenne citée, information non confirmée par l'entreprise.

[^nvda-nvhbm]: [Annonce de NVIDIA sur NVHBM](https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory/), 2026-08-26. Les chiffres de bande passante et de consommation sont ceux de l'entreprise.

[^sec-hotchips]: [Compte rendu de la présentation de Samsung Electronics à Hot Chips 2026 par ServeTheHome](https://www.servethehome.com/samsung-evolving-hbm-base-die-at-hot-chips-2026/), 2026-08-23. Feuille de route présentée par l'entreprise, sans calendrier.

[^sec-ir]: [Présentation des résultats du T2 2026 de Samsung Electronics](https://images.samsung.com/kdp/ir/events/2026/2026_2Q_conference_kor.pdf), 2026-07-30. Chiffre d'affaires de la division semi-conducteurs : 127.5 trillions KRW ; résultat opérationnel : 89.2 trillions KRW. La hausse de la demande en puces de base HBM figure parmi les facteurs de performance de la fonderie.

[^skh-q2]: [Annonce des résultats du T2 2026 de SK hynix](https://news.skhynix.com/en/q2-2026-business-results/), 2026-07-29. Chiffre d'affaires : 79.3 trillions KRW ; résultat opérationnel : 60.5 trillions KRW ; bénéfice net : 93.9 trillions KRW ; contrats d'approvisionnement à long terme et SOCAMM2.

[^tf-cxl]: [Article de TrendForce sur CXL 3.2 chez Samsung et SK hynix](https://www.trendforce.com/news/2026/07/21/news-samsung-reportedly-targets-2026-cxl-3-2-mass-production-sk-hynix-advances-new-ai-memory-architecture/), 2026-07-21. Information secondaire.

[^hbf-ocp]: [Première spécification OCP HBF publiée par Sandisk et SK hynix](https://www.storagenewsletter.com/2026/08/05/fms-2026-sandisk-and-sk-hynix-advance-global-standardization-of-high-bandwidth-flash-with-release-of-first-ocp-technical-specification/), 2026-08-05.

[^sec-fms]: [Compte rendu de la présentation de Samsung Electronics à FMS 2026 par StorageReview](https://www.storagereview.com/news/samsung-outlines-3d-memory-roadmap-for-ai-infrastructure-at-fms-2026), 2026-08-04. Présentation de mémoire basse consommation avec PIM ; date de production de masse non vérifiée.

[^skh-hybrid]: [Article de Tom's Hardware sur la présentation de SK hynix à Hot Chips 2026](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling), 2026-08-24.

[^tf-cxl-doubt]: [Article de TrendForce sur les réserves exprimées lors de l'AI Infrastructure Summit](https://www.trendforce.com/news/2026/09/18/news-openai-intel-reportedly-downplay-cxl-as-hbm-replacement-citing-use-case-and-data-transfer-limits/), 2026-09-18. Information secondaire.

[^qcom-hbc]: [Annonce de la feuille de route de Qualcomm pour les centres de données](https://www.qualcomm.com/news/releases/2026/06/qualcomm-unveils-comprehensive-data-center-roadmap-for-the-agent), 2026-06. Performances selon l'entreprise, sans validation indépendante.

[^sndk-call]: [Transcription republiée de la conférence téléphonique de Sandisk sur ses résultats du T4 FY2026](https://www.fool.com/earnings/call-transcripts/2026/08/12/sandisk-sndk-q4-2026-earnings-call-transcript/), conférence du 2026-08-05.

[^naver-sec]: [Cours quotidiens de Samsung Electronics sur Naver Finance](https://m.stock.naver.com/api/stock/005930/price?pageSize=5&page=1) et [résultats annuels compilés](https://m.stock.naver.com/api/stock/005930/finance/annual), consultés le 2026-10-05. Clôture du 10-02 : 276,000 KRW ; bénéfice par action prévu pour 2026 : 47,142 KRW.

[^naver-skh]: [Cours quotidiens de SK hynix sur Naver Finance](https://m.stock.naver.com/api/stock/000660/price?pageSize=5&page=1) et [résultats annuels compilés](https://m.stock.naver.com/api/stock/000660/finance/annual), consultés le 2026-10-05. Clôture du 10-02 : 1,842,000 KRW ; bénéfice par action prévu pour 2026 : 350,576 KRW.

[^skh-lta]: [Article de Newspim sur la conférence téléphonique de SK hynix au T2](https://www.newspim.com/news/view/20260729000198), 2026-07-29. Déclaration sur les dépôts vérifiée dans l'article.

[^sec-lta]: [Transcription intégrale de la conférence téléphonique de Samsung Electronics au T2 par The Elec](https://www.thelec.kr/news/articleView.html?idxno=60316), 2026-07-30. Part et modalités des contrats à long terme : projet de la direction.

[^tf-memory]: [Prévisions de TrendForce sur les prix contractuels de la mémoire au T4 2026](https://www.trendforce.com/presscenter/news/20260930-13258.html), 2026-09-30. Prévisions, et non prix réalisés.

[^skh-return]: [Article de ZDNet Korea sur l'annulation d'actions propres de SK hynix](https://zdnet.co.kr/view/?no=20260819161157), 2026-08-19. Texte réglementaire original non comparé.

[^sec-return]: [Article sur l'annonce de Samsung Electronics concernant la rémunération des actionnaires en 2026](https://v.daum.net/v/20260821172850433), 2026-08-21. Projet, et non montant versé.

[^mu-foundry]: [Article de The Elec sur la sous-traitance par Micron de la puce de base](https://www.thelec.net/news/articleView.html?idxno=14372), 2026-10-02. Le nom de la fonderie ne figure pas dans les commentaires originaux de Micron.

[^tf-hbm]: [Prévisions 2027 de TrendForce sur la HBM](https://www.trendforce.com/presscenter/news/20260929-13255.html), 2026-09-29. Prévisions de l'organisme d'étude.

[^turboquant]: [Présentation de TurboQuant par Google Research](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/), 2026-03-24. Résultat de recherche ; le périmètre d'application dans les services commerciaux n'a pas été vérifié.

[^anthropic-context]: [Documentation d'Anthropic sur les fenêtres de contexte](https://platform.claude.com/docs/en/build-with-claude/context-windows) et [la compaction](https://platform.claude.com/docs/en/build-with-claude/compaction), consultées le 2026-10-05.

[^anthropic-autonomy]: [Étude d'Anthropic sur la mesure de l'autonomie des agents](https://www.anthropic.com/research/measuring-agent-autonomy), 2026-02-18. Valeur au 99.9e percentile des données d'utilisation propres à l'entreprise.

[^tf-supply]: [Prévisions de TrendForce sur l'offre et la demande de mémoire en 2026-2027](https://www.trendforce.com/presscenter/news/20260730-13158.html), 2026-07-30. Prévisions de l'organisme d'étude.

[^tf-china]: [Article de TrendForce sur l'augmentation des capacités de CXMT et YMTC](https://www.trendforce.com/news/2026/09/24/news-cxmt-ymtc-ramp-memory-capacity-but-chinas-ai-cloud-boom-could-soak-up-new-supply-through-2027/), 2026-09-24. Information secondaire.

[^bis]: [Discours du directeur général de la Banque des règlements internationaux](https://www.bis.org/speeches/20260910-artificial-intelligence-growth-and-financial-stability-challenges-central-banks), 2026-09-10.

[^consensus]: [Article de MoneyToday sur les prévisions de résultats du T3](https://www.mt.co.kr/amp/stock/2026/10/05/2026100217315021825), 2026-10-05. Chiffres attribués à FnGuide.

*Disclaimer : document fourni à des fins de recherche et d'information. Les entreprises, multiples et scénarios cités sont des exemples d'analyse ; chaque lecteur doit procéder à sa propre évaluation avant toute décision d'investissement.*
