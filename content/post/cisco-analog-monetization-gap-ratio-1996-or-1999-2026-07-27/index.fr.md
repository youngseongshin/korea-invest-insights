---
title: "Cisco n'est pas mort d'un manque de demande : réécrire la comparaison dot-com/IA avec le ratio d'écart de monétisation"
slug: "cisco-analog-monetization-gap-ratio-1996-or-1999-2026-07-27"
date: 2026-07-27T10:00:00+09:00
description: "La version populaire de la comparaison, demande factice hier contre demande réelle aujourd'hui, est fausse. La demande finale était réelle en 1999 aussi. Ce qui a fait chuter Cisco de 89%, ce n'est pas l'absence de demande mais le séquencement : un financement qui courait cinq à dix ans devant elle. Le ratio d'écart de monétisation, dépenses d'infrastructure divisées par revenus finaux de l'IA, s'est resserré de 8x à 4,6x et évoque 1996, tandis que la pile d'engagements de 1 400 Mds USD d'OpenAI et l'arrivée du financement fournisseur de NVIDIA évoquent 1999. Dans un système où les deux signaux sont allumés, le pont qui décide de la rupture est le marché des capitaux. Nous auditons les preuves du remplacement du travail par les agents et les implications pour la mémoire coréenne."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["Cisco", "Bulle dot-com", "Bulle IA", "Écart de monétisation", "Financement fournisseur", "OpenAI", "NVIDIA", "CAPEX IA", "IA agentique", "Semi-conducteurs coréens", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte : dans [Disséquer 950 milliards de dollars](/fr/post/sf-ai-declaration-950bn-korea-equity-deep-analysis-2026-07-26/), nous écrivions que la Corée venait de s'intégrer dans la structure de financement circulaire de NVIDIA, et dans [Qui brûle tous ces tokens ?](/fr/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/), que des chiffres commençaient enfin à s'attacher à la demande finale. Cet article réunit ces deux observations en une seule question. Quelle année sommes-nous, 1996 ou 1999 ? Nous réécrivons la comparaison avec Cisco la plus invoquée du marché, non comme un lieu commun mais comme un indicateur, et faisons converger le juge de paix vers un seul ratio.

## TL;DR

- Corrigeons d'abord le lieu commun. La comparaison qui veut que Cisco reposait sur une demande factice et qu'aujourd'hui la demande soit réelle est fausse. <strong>La demande finale était réelle en 1999 aussi</strong>. Les utilisateurs d'Internet augmentaient de 50% par an, le trafic de 100% par an, et la fibre optique posée à cette époque a plus tard transporté YouTube et Netflix. Le pari sur l'infrastructure était juste en lui-même. Ce qui a fait chuter Cisco de 89%, ce n'est pas l'absence de demande, mais <strong>un séquencement où le financement a couru cinq à dix ans devant la demande</strong>.
- Les ingrédients de la mort étaient au nombre de trois. Le mythe du "doublement tous les 100 jours" pour le trafic (en réalité, il doublait chaque année), le crédit de l'acheteur marginal qui achetait son équipement à coups d'obligations pourries et de financement fournisseur, et la trahison du chiffre d'affaires par la déflation des prix unitaires : le prix de la bande passante a chuté de 90% sans que les revenus ne suivent. Le taux d'allumage de la fibre noire était inférieur à 5%.
- Comme seul chiffre séparant les deux époques, nous proposons <strong>le ratio d'écart de monétisation (dépenses d'infrastructure divisées par revenus finaux de l'IA)</strong>. Le dot-com est resté à 6-10x, s'est élargi, puis a rompu. L'IA était à environ 8x en 2024, environ 6,5x en 2025, et environ 4,6x en 2026, elle <strong>se resserre</strong>. Sur ce seul axe, nous sommes en 1996.
- Mais si l'on regarde les engagements plutôt que l'exécution, l'image s'inverse. La pile d'engagements d'achat d'OpenAI atteint environ <strong>1 400 Mds USD</strong>, x10 en 18 mois, pour une couverture d'environ 35x par rapport à un chiffre d'affaires annualisé d'environ 40 Mds USD. Et le financement fournisseur de NVIDIA vient tout juste d'apparaître. Sur ce seul axe, nous sommes en 1999.
- Auditer avec des preuves le dernier saut de la demande, le remplacement du travail par les agents, sépare trois propositions. Le remplacement de professions spécifiques est démontré (23% des licenciements américains du premier semestre attribués à l'IA), la conversion de ce remplacement en profit n'est pas démontrée (Gartner : aucune différence de rentabilité entre les entreprises qui licencient le plus et celles qui licencient le moins), et le remplacement total du travail intellectuel reste au stade du récit. Pourtant, <strong>la seule masse salariale étroite déjà démontrée offre un potentiel de croissance de 3-5x pour le chiffre d'affaires actuel des tokens</strong>, ce qui suffit à justifier le capex 2026-2028 sans rien de plus.
- Le verdict global est celui d'une analogie avec le milieu de 1999. Historiquement, il s'est écoulé 12-18 mois entre l'apparition du financement fournisseur et la rupture. Mais ceux qui ont acheté au milieu de 1999 ont aussi beaucoup gagné jusqu'en mars 2000, c'est l'autre face de cette analogie, et les trois indicateurs réels, le taux d'utilisation, le ratio d'écart et l'élasticité, vont tous dans la direction opposée au dot-com.

<div class="thesis-callout">
<div class="thesis-callout__label">Thèse principale</div>

La leçon de Cisco n'est pas que la demande était factice, mais que même une demande réelle fait d'abord perdre 89% aux actionnaires lorsque le financement la précède de cinq à dix ans. Du point de vue de la demande finale, l'IA d'aujourd'hui diffère radicalement du dot-com. La machine à facturer tourne déjà, le taux d'utilisation des GPU est de 100%, le portefeuille du payeur est une masse salariale et non un budget de loisirs, et le ratio d'écart de monétisation se resserre. Mais l'apparition du financement fournisseur est exactement la signature du milieu de 1999. Le juge de paix converge vers un seul verdict. Tant que le chiffre d'affaires des tokens croît plus vite que le capex promis, nous sommes en 1996, et dès qu'il fléchit, nous sommes en 1999.

</div>

## 1. Corriger le lieu commun : la vraie cause de la mort de Cisco

La demande finale d'Internet entre 1999 et 2001 était réelle et explosive. Les utilisateurs augmentaient de 50% par an, le trafic de 100% par an. Sur la fibre optique posée à cette époque ont ensuite grandi YouTube, Netflix et le cloud. L'histoire a tranché : la décision de mettre de l'argent dans l'infrastructure était juste en elle-même. Et pourtant, les actionnaires de Cisco ont perdu 89% par rapport au sommet. [Fait : données historiques]

Ce qui a tué Cisco, ce n'est pas la demande, mais la combinaison suivante.

<strong>L'indicateur mythique.</strong> L'affirmation selon laquelle le trafic doublait tous les 100 jours (venue d'UUNet, filiale de WorldCom) est devenue une prémisse standard du secteur, alors que le trafic réel doublait chaque année. Un indicateur de demande exagéré a tiré le capex cinq à dix ans devant la demande réelle. [Fait : données historiques] Même si la demande est réelle, si l'indicateur de demande est faux, le capital court à la mauvaise vitesse.

<strong>Le crédit de l'acheteur marginal.</strong> Les commandes incrémentales ne venaient pas d'opérateurs générant du cash, mais de nouveaux opérateurs (CLEC) qui achetaient leur équipement à coups d'obligations pourries et de financement fournisseur. Le financement fournisseur atteignait environ 25 Mds. Quand les marchés de capitaux se sont fermés en 2000, les commandes de ces acheteurs sont mortes sur le coup, et Cisco a déprécié 2,2 Mds de stocks tandis que ses revenus chutaient de 30%. [Fait : données historiques] Ce n'est pas l'ampleur de la demande qui s'est effondrée en premier, mais <strong>la source de l'argent qui achetait cette demande</strong>.

<strong>La trahison du chiffre d'affaires par la déflation des prix unitaires.</strong> Le prix de la bande passante a chuté de 90%. Côté volume, l'effet Jevons a fonctionné : le trafic a continué d'augmenter. Mais le Jevons du chiffre d'affaires en dollars n'a pas fonctionné. Le taux de baisse des prix a dépassé le taux de croissance des volumes, faisant tomber l'élasticité du chiffre d'affaires sous 1, et le taux d'allumage de la fibre noire posée est resté sous 5%. [Fait : données historiques] La demande physique et la demande en dollars sont deux variables différentes, et le cours de bourse suit les dollars.

C'est en gardant ces trois éléments en tête, et en les confrontant au présent, que la comparaison devient utile.

## 2. Comparaison précise : sept axes

| Axe | Dot-com (1999-2000) | IA (2026) | Verdict |
|---|---|---|---|
| Utilisateurs finaux | ~280 M, en croissance | ~1 Md (niveau ChatGPT), en croissance | Réels des deux côtés |
| Substance de la facturation | Dial-up à 20 USD par mois et publicité embryonnaire | Abonnements 20-200 USD par mois, API à l'usage, sièges entreprise. Labos frontière combinés ~50-60 Mds annualisés, croissance 2-3x/an | Avantage IA. Une machine à facturer tourne, absente en 1999 |
| Portefeuille du payeur | Budget loisirs du consommateur et publicité | Substitution de charges salariales en entreprise (masse salariale mondiale de dizaines de milliers de milliards), budgets souverains, consommateurs | Catégorie différente. Mais le saut du remplacement du travail reste à vérifier |
| Taux d'utilisation | Taux d'allumage de la fibre noire sous 5% | GPU à quasiment 100%, tout vendu et listes d'attente | La différence la plus décisive |
| Déflation des prix unitaires | Bande passante -90%, élasticité du chiffre d'affaires sous 1 | Prix du token en chute rapide, mais élasticité du chiffre d'affaires encore supérieure à 1 | Même risque, résultat encore opposé. Axe de surveillance maximale |
| Indicateur mythique | Trafic doublant tous les 100 jours | Lois d'échelle, calendriers de l'AGI, remplacement total du travail | Les deux existent. Différence : l'IA a un chiffre d'affaires mesuré en parallèle |
| Crédit de l'acheteur marginal | Obligations pourries des CLEC et financement fournisseur, 25 Mds | Le FCF des hyperscalers, 300-400 Mds/an, est l'acheteur principal. Mais la financiarisation fournisseur de l'acheteur marginal commence | Signal de convergence clé |

[Fait : synthèse de données historiques et de notes fournies]

Sur les sept axes, cinq favorisent l'IA, un (la déflation des prix unitaires) présente le même risque mais un résultat encore opposé, et le dernier (le crédit de l'acheteur marginal) commence à converger dans le mauvais sens. C'est ce dernier axe qui domine la suite de cet article.

## 3. Le ratio d'écart de monétisation : le seul chiffre qui distingue les deux cas

Voici l'essence du cas Cisco réduite à un seul ratio. <strong>À combien de fois le chiffre d'affaires de la demande finale les dépenses d'infrastructure courent-elles, et ce multiple se resserre-t-il ou s'élargit-il ?</strong>

| Période | Dépenses d'infrastructure | Chiffre d'affaires final | Ratio d'écart | Direction |
|---|---|---|---|---|
| Dot-com 1999-2000 | Capex télécoms ~220 Mds | Chiffre d'affaires final Internet ~20-40 Mds | 6-10x | Maintenu, élargi, puis rupture |
| IA 2024 | ~250 Mds | ~30 Mds | ~8x | Point de départ |
| IA 2025 | ~450 Mds | ~70 Mds | ~6,5x | Resserrement |
| IA 2026 (projection) | ~600 Mds | ~130 Mds (labos, IA cloud, copilotes combinés) | ~4,6x | Resserrement |

[Inférence : fourchette d'estimation propre, frontière d'attribution IA du numérateur et du dénominateur floue]

Dans le dot-com, pendant que le capex accélérait, le chiffre d'affaires par bit s'est effondré et l'écart s'est élargi. Dans l'IA, c'est l'inverse jusqu'à présent. Les tokens rapportent plus vite que l'argent ne sort. Cela concorde avec la hiérarchie observée au premier trimestre chez les Big Tech (la croissance du backlog dépasse celle du capex, et la croissance du capex dépasse celle du chiffre d'affaires, lequel accélère pourtant), et cela concorde aussi avec le Cloud +82% et l'usage dépassant les engagements de 50% observés dans [l'article sur le T2 d'Alphabet](/fr/post/alphabet-q2-2026-cloud-82-fcf-negative-memory-demand-2026-07-23/). La proposition centrale de cet article est que <strong>la direction de ce ratio est le seul chiffre qui distingue les deux cas</strong>.

## 4. Le remplacement du travail par les agents : un audit des preuves

Dans le tableau comparatif, l'axe selon lequel le portefeuille du payeur serait une masse salariale portait la réserve d'un saut non démontré. Auditer ce saut sur la base des calls de résultats et des publications sépare trois propositions.

<strong>Proposition 1, les agents remplacent des professions spécifiques. Démontré.</strong>

| Acteur | Preuve | Chiffres |
|---|---|---|
| Salesforce | Réduction du personnel de support, confirmée par le CEO en call | 4 000 postes supprimés, l'IA traite ~50% des interactions clients |
| Amazon | Investissement IA explicitement cité lors des suppressions de postes de janvier | 16 000 postes, dans la continuité de la plus grande vague de suppressions de postes corporate de son histoire |
| Intuit | Réallocation des ressources vers l'IA mentionnée directement | 17% des effectifs, ~3 000 postes |
| Meta, Oracle, Block, etc. | Cumul des suppressions de postes citant explicitement l'IA comme motif | 184 000 |
| Monday.com | Présenté non comme une réduction de coûts mais comme une réorganisation centrée sur les agents IA | 630 postes, un type qualitativement nouveau |
| Recensement Challenger | Part des licenciements américains attribués à l'IA au premier semestre 2026 | 23% (101 743), premier motif de licenciement pendant 4 mois consécutifs |
| Mesure fonctionnelle | Traitement du support Tier-1 par l'IA | ~80% à un coût ~80% moindre |

[Fait : publications, calls, statistiques sectorielles, sur la base des liens sources des notes fournies]

À cela s'ajoute un découplage au niveau des états financiers. Le chiffre d'affaires par salarié des Fortune 500, 687 000 USD, et le bénéfice par salarié, 68 700 USD, atteignent des sommets historiques, alors que l'emploi a reculé pendant deux années consécutives, avec 301 000 postes en moins, pendant que le bénéfice total augmentait de 12%. [Fait : recensement Fortune] Le découplage entre croissance et emploi commence à s'inscrire dans les statistiques officielles.

<strong>Proposition 2, ce remplacement se convertit en profit. Non démontré. C'est ici la vraie découverte de cet audit.</strong> Gartner a interrogé 350 dirigeants et a constaté que la rentabilité financière des entreprises ayant le plus licencié et de celles ayant le moins licencié était en pratique identique. [Fait : enquête Gartner rapportée] Les licenciements sont réels, mais aucune preuve n'indique encore qu'ils aient amélioré les marges. Cela signifie que les coûts de licenciement et de réaffectation, les coûts des outils IA et la dégradation de la qualité (le cas Klarna, qui avait déclaré l'IA capable de faire le travail de 700 personnes avant de réembaucher une partie d'entre elles) compensent les économies réalisées. Les preuves côté marché du travail abondent, mais les preuves côté compte de résultat sont absentes. S'y ajoute un biais d'AI washing. Le marché récompense les licenciements liés à l'IA et pénalise ceux liés à une faiblesse de la demande, ce qui crée une forte incitation à rebaptiser IA un simple ajustement du sureffectif de l'ère Covid. Une partie de ce taux d'attribution de 23% relève du récit.

<strong>Proposition 3, le remplacement total du travail intellectuel. Stade du récit.</strong> Aucune preuve publiée. C'est une prémisse pour les engagements après 2029, pas une mesure du présent.

Mais la conclusion de cet audit est que la proposition 3 n'est pas nécessaire pour justifier le capex. Calculons seulement le pool étroit déjà démontré. La masse salariale mondiale des centres d'appels, du BPO, du back-office et de l'assistance au développement junior représente environ 1 500-2 500 Mds USD par an. Si seulement 10% de ce montant bascule vers des dépenses IA, cela donne 150-250 Mds par an, ce qui place <strong>une marge de croissance de 3-5x le chiffre d'affaires actuel des labos frontière (~50-60 Mds annualisés) dans une catégorie déjà démontrée</strong>. [Inférence : arithmétique de la masse salariale, fourchette d'estimation] Le resserrement du ratio d'écart pour 2026-2028 est possible avec la seule proposition 1. La proposition 3 ne devient nécessaire que pour les engagements postérieurs à 2029.

## 5. Flux et stock : 1996 et 1999 sont allumés en même temps

C'est ici que se loge la tension centrale de cet article. Dans le même système, deux horloges pointent vers deux années différentes.

<strong>Flux contre flux. Les tokens gagnent.</strong> Le chiffre d'affaires des tokens des labos frontière croît de 150-250% par an. OpenAI est à environ 40 Mds annualisés (contre environ 15 Mds un an plus tôt), Anthropic a environ triplé (~3x), et Codex a gagné 3 millions d'utilisateurs en trois jours. Le chiffre d'affaires IA au sens large (labos, IA cloud et copilotes combinés) croît de 85-100% par an (~70 → ~130 Mds). Le capex exécuté, lui, croît de 40-60% par an. La croissance du chiffre d'affaires est 2-4x celle des dépenses. C'est ce qui resserre le ratio d'écart de 8x à 4,6x. [Fait : synthèse des mesures des notes fournies] Sur ce seul axe, nous sommes en 1996.

<strong>Stock contre stock. Les engagements gagnent.</strong> Si l'on regarde non plus l'exécution mais les obligations futures contractées, l'image s'inverse. La pile d'engagements d'achat d'OpenAI atteint environ 250 Mds avec Azure, environ 300 Mds avec Oracle, environ 350 Mds avec Broadcom (10GW d'accélérateurs sur mesure), 10GW liés à l'investissement NVIDIA, 6GW avec AMD, et avec AWS et CoreWeave, un total d'environ <strong>1 400 Mds USD</strong>, en hausse de plus de 10x en 18 mois. La couverture est d'environ 35x par rapport à un chiffre d'affaires annualisé d'environ 40 Mds. Si ces engagements sont facturés à raison d'environ 250 Mds par an à partir de 2027, le chiffre d'affaires devrait être multiplié par 6 en deux ans pour que l'exploitation puisse absorber la facture. [Fait : synthèse de reportages publics] Deux réserves s'imposent. D'une part, les 1 400 Mds USD sont le chiffre d'engagements cumulés jusqu'au milieu des années 2030 tel qu'Altman lui-même l'a communiqué, et certains reportages récents indiquent qu'il oriente désormais les investisseurs vers une dépense réelle abaissée à environ 600 Mds d'ici 2030. [Fait : presse] Autrement dit, la couverture de 35x correspond à la définition la plus défavorable, et retombe autour de 15x sur la base de la guidance de dépense. Quelle que soit la définition retenue, le fait demeure qu'elle dépasse d'un ordre de grandeur le 4,6x du flux. Sur ce seul axe, nous sommes en 1999.

Et c'est exactement le financement externe qui construit le pont entre ces deux courbes. Le rapport publié dimanche par le Wall Street Journal sur les discussions entre NVIDIA et OpenAI en est le tablier le plus récent. Pour le campus de data centers de 10GW du comté de Pike, dans l'Ohio (développé par SB Energy, filiale de SoftBank, phase 1 d'environ 800MW visant 2028), NVIDIA négocierait <strong>une garantie d'environ 250 Mds pour le bail et la dette de construction</strong>, et séparément <strong>un financement de puces de 350 Mds</strong>. Ces discussions en sont encore au stade préliminaire, et les articles ont aussi rapporté un risque d'échec. [Fait : WSJ, Reuters, CNBC, stade de discussion] La structure est limpide une fois posée : le vendeur garantit à la fois le financement d'achat de ses propres puces et la dette du bâtiment qui les hébergera, c'est du financement fournisseur. L'investissement de NVIDIA dans Naver, vu la semaine dernière dans [l'article sur les 950 milliards de dollars](/fr/post/sf-ai-declaration-950bn-korea-equity-deep-analysis-2026-07-26/), relève de la même famille. Le simple fait que le financement fournisseur ait fait son apparition constitue le premier allumage de signature de l'horloge Cisco.

Les implications de cette structure se résument en trois points. 2026-2027 relève de l'arithmétique. Le capex exécuté est physiquement lié à l'électricité et à la chaîne d'approvisionnement en puces, ce qui rend difficile une croissance supérieure à 50% par an, tandis que le chiffre d'affaires croît à un rythme à trois chiffres, si bien que l'écart continue de se resserrer. La probabilité de rupture est faible sur cette période. 2028-2029 est conditionnel. Pour que la couverture se normalise avant que la vague d'engagements de 1 400 Mds USD n'atterrisse, le chiffre d'affaires doit composer à 80-100% par an pendant deux à trois années supplémentaires. C'est atteignable si la croissance actuelle ralentit graduellement, et catastrophique si elle est divisée par deux chaque année. <strong>La vraie contrainte active n'est donc ni le chiffre d'affaires ni le capex, mais le pont, c'est-à-dire le marché des capitaux</strong>. Tant que le financement reste ouvert, les deux courbes ont le temps de converger, et s'il se ferme, la pile d'engagements s'effondre en ne laissant que la part déjà financée. C'est pourquoi la baisse du taux de couverture de la demande obligataire (d'environ 5x en début d'année à environ 2x récemment) et la diffusion du financement fournisseur constituent une alerte précoce qui précède le ratio d'écart lui-même.

## 6. Le verdict de l'horloge : quelle année sommes-nous ?

Voici, sous forme de tableau, l'état d'allumage de chaque signature de la mort de Cisco.

| Signature | Moment dans le dot-com | État actuel | Allumage |
|---|---|---|---|
| Apparition du financement fournisseur | 1999 | Discussions rapportées sur la garantie de dette et le financement de puces de NVIDIA pour OpenAI | Allumé. Analogie 1999 |
| Fatigue des marchés de capitaux | Début 2000 | Baisse du taux de couverture obligataire, concessions en hausse | Signal précoce |
| Renversement vers un élargissement du ratio d'écart | 1999-2000 | Encore en resserrement | Éteint |
| Effondrement du taux d'utilisation | 2000-2001 (fibre noire) | GPU tout vendu et listes d'attente | Éteint |
| Passage sous une élasticité du chiffre d'affaires de 1 | 2000 (bande passante) | Encore supérieure à 1 | Éteint |
| Falaise des commandes | 2001 | Croissance du backlog dans la fourchette haute à deux chiffres | Éteint |

[Inférence : cadre de signatures, sur la base des notes fournies]

Voici le verdict. Nous ne sommes pas fin 2000, mais dans <strong>une analogie avec le milieu de 1999</strong>. Le financement fournisseur vient d'apparaître (historiquement un signal 12-18 mois avant la rupture), les autres signatures restent éteintes, et surtout les trois indicateurs réels, taux d'utilisation, ratio d'écart et élasticité, vont tous dans la direction opposée au dot-com. Mais il faut garder à l'esprit les deux faces de cette analogie. Ceux qui ont acheté au milieu de 1999 ont eux aussi beaucoup gagné jusqu'en mars 2000, avant de tout rendre ensuite. Si l'analogie est juste, le gain restant sur cette période est important, mais la difficulté de gérer la sortie l'est tout autant.

Précisons aussi clairement les conditions qui feraient rejoindre la trajectoire de Cisco. Que l'élasticité du chiffre d'affaires des tokens tombe sous 1 (la baisse des prix unitaires l'emportant sur la croissance de l'usage), que le ratio d'écart se renverse vers un élargissement (le capex engagé atterrissant pendant que le chiffre d'affaires stagne), ou que la contamination du crédit de l'acheteur marginal se propage jusqu'au cœur des hyperscalers. Aucune de ces trois conditions n'est encore allumée, et toutes les trois sont mesurables trimestre par trimestre.

## 7. Implications pour les semi-conducteurs coréens : les fournisseurs sont tombés plus bas

Conformément à l'usage de cette série, ajoutons la perspective coréenne. Ce que les investisseurs coréens doivent retenir de la rupture du dot-com, ce n'est pas l'ampleur de la chute de Cisco. C'est le fait que <strong>les entreprises qui vendaient des composants à Cisco sont tombées plus bas que Cisco lui-même</strong>. JDS Uniphase et Nortel, dans les composants optiques, ont perdu environ 99% par rapport à leur sommet. [Fait : données historiques] La rupture du séquencement se transmet en s'amplifiant vers l'amont de la chaîne de valeur. Les commandes de biens intermédiaires fléchissent avant que la demande finale ne fléchisse, parce que c'est en amont que l'effet coup de fouet sur les stocks se manifeste avec le plus d'ampleur. La dépréciation de 2,2 Mds de stocks chez Cisco signifiait aussi que le chiffre d'affaires de ces fournisseurs en amont avait disparu en premier.

La mémoire coréenne d'aujourd'hui se tient précisément dans cet amont. En traduisant le cadre du ratio d'écart en perspective mémoire, un indicateur de surveillance supplémentaire apparaît. <strong>La qualité de crédit du mix acheteur.</strong> Aujourd'hui, les acheteurs principaux de mémoire sont les hyperscalers, qui génèrent 300-400 Mds de FCF par an, ce qui les distingue fondamentalement du Cisco de 1999 qui vendait à des CLEC. Mais à mesure que la financiarisation fournisseur progresse, c'est-à-dire à mesure que la part des néoclouds, des acheteurs financés par la dette et des commandes adossées à des garanties augmente, le crédit type 1999 s'infiltre aussi dans les carnets de commandes de mémoire. L'entrée de la Corée dans la boucle de financement circulaire vue la semaine dernière (NVIDIA investissant dans Naver, Naver utilisant cet argent pour acheter du NVIDIA) signifie que cette porte s'est aussi ouverte du côté coréen.

Les deux faces des contrats d'approvisionnement long terme (LTA) s'éclairent aussi dans ce cadre. Un LTA offre de la visibilité sur les prix et les volumes, mais Cisco disposait lui aussi, en 2000, d'un solide carnet de commandes, qui s'est achevé en 2001 par des annulations et des dépréciations. <strong>Ce qu'un LTA protège, c'est le prix dans un monde où la capacité de paiement de la contrepartie reste intacte, pas ce monde lui-même.</strong> Quand le président de SK Hynix, Chey Tae-won, cite l'interruption du financement de l'IA comme sa plus grande inquiétude à cinq ans, il pointe exactement cette structure.

La conclusion pratique est simple. Ajoutons deux indicateurs au prix contractuel de la DRAM, qui a longtemps été le juge de paix des investisseurs en mémoire. La direction du ratio d'écart de monétisation trimestriel, et la part des acheteurs FCF par rapport aux acheteurs financés par la dette dans le mix des acheteurs finaux de mémoire. Tant que les deux premiers restent sains, toute correction est une opportunité, et si les trois se dégradent ensemble, ce sera alors 1999.

## 8. Grille de lecture : les indicateurs à surveiller

- <strong>Le ratio d'écart de monétisation trimestriel.</strong> Chiffre d'affaires des labos et de l'IA cloud contre capex IA. Le suivi trimestriel commence dès cette saison de résultats. Chez Microsoft le 30 juillet à 06h30 KST et Amazon le 31 juillet à 06h00 KST, la question qui tranchera le prochain trimestre est de savoir si le ratio de flux (accélération du chiffre d'affaires IA contre incrément de la guidance capex) reste au-dessus de 1.
- <strong>La mesure de l'élasticité du chiffre d'affaires.</strong> Le suivi simultané du prix du token et du chiffre d'affaires des tokens. Tant que le chiffre d'affaires augmente malgré la baisse des prix unitaires, la trajectoire diverge de celle de la bande passante.
- <strong>La prochaine édition des enquêtes type Gartner sur licenciements et rentabilité.</strong> C'est l'indicateur qui tranchera la proposition 2 (la conversion du remplacement en profit). Si elle cède, l'arithmétique de la masse salariale basculera dans le compte de résultat.
- <strong>La publication chiffrée du chiffre d'affaires agentique.</strong> À surveiller lors de cette saison de calls : si des montants contractuels type Salesforce Agentforce commencent à être publiés de façon chiffrée. Le taux mensuel de licenciements attribués à l'IA selon Challenger sera suivi en parallèle.
- <strong>L'état du pont.</strong> Les spreads de crédit IA, le taux de couverture de la demande obligataire, et la ligne de mise en équivalence de Microsoft (qui reflète le résultat d'OpenAI). Puisque la conclusion de cet article est que la vitesse de diffusion du financement fournisseur est une alerte précoce qui devance le ratio d'écart lui-même, la couverture du prochain deal obligataire d'un hyperscaler sera le signal le plus précoce.
- <strong>La qualité du backlog.</strong> Plus la part des nouveaux engagements hors labos (entreprises, souverains) augmente, plus la qualité de crédit de la pile d'engagements s'améliore.

Le juge de paix converge vers un seul verdict. <strong>Tant que le chiffre d'affaires des tokens croît plus vite que le capex engagé, nous sommes en 1996, et dès qu'il fléchit, nous sommes en 1999.</strong> Et jusqu'à ce que ce verdict tombe, le juge de paix de la mémoire coréenne reste, sans changement, le prix contractuel de la DRAM et la qualité de crédit du mix acheteur.

---

Les titres mentionnés dans le texte sont des exemples destinés à l'analyse et ne constituent pas une recommandation d'achat ou de vente d'un titre particulier. La décision d'investissement et ses conséquences relèvent de la seule responsabilité de l'investisseur. Le numérateur et le dénominateur du ratio d'écart de monétisation sont des fourchettes d'estimation dont la frontière d'attribution au chiffre d'affaires IA reste floue, et les chiffres de l'époque dot-com sont des approximations fondées sur des données historiques. La pile d'engagements d'OpenAI résulte de l'addition de reportages publics et de déclarations de dirigeants, ce n'est pas une publication officielle de l'entreprise, et elle peut différer du plan de dépense réel. La garantie de NVIDIA et le financement de puces relèvent de reportages au stade de la discussion, dont le risque d'échec a également été rapporté. L'attribution des licenciements à l'IA comporte un biais narratif intrinsèque, et l'arithmétique de la masse salariale est une fourchette d'estimation. Les données de marché telles que le taux de couverture obligataire peuvent varier selon la méthode d'agrégation. Le verdict de l'horloge et les années de scénario constituent un cadre de jugement, non une prévision statistique.

### Articles liés

- [Disséquer 950 milliards de dollars : trois choses que la Déclaration IA de San Francisco a changées, et une qu'elle n'a pas changée](/fr/post/sf-ai-declaration-950bn-korea-equity-deep-analysis-2026-07-26/)
- [Alphabet au T2 : Cloud +82% clôt le débat sur la demande, le FCF négatif ouvre celui du cash](/fr/post/alphabet-q2-2026-cloud-82-fcf-negative-memory-demand-2026-07-23/)
- [Qui brûle tous ces tokens ? La carte clients de NVIDIA, l'IA souveraine et les 9 millions de Codex commencent à répondre](/fr/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/)
- [Le vrai débat des semi-conducteurs : quatre horloges physiques et une horloge boursière](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
