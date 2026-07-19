---
title: "Qui brûle tous ces tokens ? La carte clients de NVIDIA, l'IA souveraine et les 9 millions de Codex commencent à répondre"
slug: "who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19"
date: 2026-07-19T19:00:00+09:00
description: "La question qui n'a jamais quitté le débat sur le CAPEX IA : qui utilisera réellement toute cette infrastructure ? Dans les comptes de NVIDIA, le chiffre d'affaires hors hyperscale a atteint la parité avec l'hyperscale et son rythme de croissance trimestriel s'est déjà inversé. Le revenu de l'IA souveraine a triplé en un an, l'équipe semi-conducteurs de Meritz a contesté le cadre étroit du marché avec une DRAM serveur qui se retend, et Codex a ajouté trois millions d'utilisateurs en trois jours. Nous recoupons ces preuves côté demande et leur signification pour les scénarios 45/35/20."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["NVIDIA", "IA souveraine", "Codex", "Mémoire IA", "DRAM serveur", "HBM", "Samsung Electronics", "SK Hynix", "CAPEX IA", "IA agentique", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte : dans [La demande de mémoire pour l'IA dépassera-t-elle les attentes](/fr/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/), nous avions pondéré la demande par probabilité selon un scénario de base à 45%, un scénario haussier à 35% et un scénario baissier à 20% ; dans [Deux mois de déclarations du président de SK Hynix Chey Tae-won](/fr/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/), nous avions lu les mots et les actes du plus haut niveau de l'offre. Le maillon faible qui restait, c'était la demande finale. Avec autant de GPU et de HBM déployés, qui va bien pouvoir brûler tous ces tokens ? Cet article documente la semaine où des chiffres ont commencé à répondre à cette question.

## TL;DR

- Dans le chiffre d'affaires data center de NVIDIA, la part de l'hyperscale oscille autour de 50% depuis sept trimestres. Cette part ne s'est pas encore effondrée. Ce qui a changé, c'est la composition. Au trimestre février-avril 2026, <strong>le chiffre d'affaires non hyperscale (ACIE) de 37 Mds USD a atteint un quasi-équilibre avec les 38 Mds USD de l'hyperscale</strong>, et le taux de croissance trimestriel s'est déjà inversé, 31% contre 12%. La prochaine publication pourrait voir la part elle-même basculer pour la première fois.
- Sur la même période, la croissance en glissement annuel du chiffre d'affaires data center a réaccéléré, de +56% à +66%, +75%, puis +92%. Que la part se maintienne alors que l'ensemble reprend de la vitesse signifie que <strong>la croissance incrémentale est tirée par l'extérieur de l'hyperscale</strong>. NVIDIA a elle-même écrit, dans ses publications, que la croissance avait été menée par le reste de sa clientèle.
- Le chiffre d'affaires de l'IA souveraine a dépassé 30 Mds USD sur l'ensemble du FY2026, triplant par rapport à l'année précédente, et a encore progressé de plus de 80% en glissement annuel au trimestre suivant. C'est l'acheteur que le marché a manqué en ne regardant que les discours des hyperscalers.
- L'équipe semi-conducteurs de Meritz Securities a souligné, dans un rapport publié dimanche, l'entrée en phase active des achats souverains et le regain de tension sur l'offre de DRAM serveur depuis la mi-juillet. La prévision de TrendForce d'une hausse de +13-18% des prix contractuels de la DRAM serveur au T3, le témoignage du taïwanais Inventec sur des délais de 40 semaines, et les propos de Micron selon lesquels seuls 50-66% de la demande des clients clés peuvent être satisfaits, confirment ce constat de façon externe et croisée.
- Des chiffres sont aussi apparus côté demande finale. Codex, d'OpenAI, est passé de 1 million en février à plus de 5 millions fin mai, puis, juste après le lancement de GPT-5.6, de 6 millions le 12 juillet à 9 millions autour du 15 juillet, <strong>soit 3 millions d'utilisateurs supplémentaires en trois jours</strong>. C'est le moment où l'unité de la demande bascule du nombre d'abonnés vers le temps d'exécution des agents.
- La conclusion n'est pas un relèvement hâtif des probabilités. C'est plutôt qu'avant de trancher sur une offre excédentaire, le moment est venu de revérifier si <strong>la demande n'a pas été dessinée de façon trop timide</strong>, et que ce jugement sera rendu par la saison des résultats autour du 30 juillet et par la publication de NVIDIA fin août.

<div class="thesis-callout">
<div class="thesis-callout__label">Thèse principale</div>

Le marché a douté de la durabilité du CAPEX IA en ne regardant que les discours de quatre géants de la tech. Pendant ce temps, dans les comptes de NVIDIA, le chiffre d'affaires non hyperscale a atteint la parité avec l'hyperscale, le chiffre d'affaires souverain a triplé en un an, et Codex a ajouté trois millions d'utilisateurs en trois jours. Tandis que le cours de bourse intégrait d'abord la peur d'une offre excédentaire, le socle de la demande accumulait des données réelles allant dans le sens inverse. Cette asymétrie est l'essence de cette phase de correction.

</div>

## 1. Quelle semaine : entre limit-down et rapports d'analystes

Commençons par planter le décor. Le jeudi 16 juillet, sur le marché américain, l'indice des semi-conducteurs de Philadelphie (SOX) a chuté d'environ 4%, entrant en territoire de marché baissier avec un repli de plus de 20% depuis son sommet, tandis que le Nasdaq reculait de 1,47%. Le vendredi 17, le Nasdaq a encore cédé 1,40%, portant le repli hebdomadaire à 2,90%. [Fait : données de marché] Le même jour à Tokyo, Kioxia a plongé de 16,1%, touchant sa limite basse dès l'ouverture. Son cours est retombé de plus de moitié depuis son sommet du 22 juin, effaçant quelque 30 000 milliards JPY de capitalisation boursière. Le déclencheur direct a été le verdict d'un jury américain accordant à Viasat environ 229 M USD de dommages et intérêts pour violation de brevet, mais comme l'ont montré les chutes simultanées de TSMC (-7,29%), de l'ADR SK Hynix (-13,69%) et de SanDisk (-12,63%) lors de la même séance, l'essentiel tenait au désendettement de l'ensemble du rally de l'IA. [Fait : Nikkei, Korea Economic Daily]

Le marché coréen a échappé à cette séance du vendredi : le 17 juillet était un jour férié, jour de la Constitution réintroduit comme jour chômé pour la première fois en 18 ans. Mais juste avant, il avait déjà essuyé de lourdes chutes : SK Hynix -15,37% et Samsung Electronics -10,70% le 13 juillet, puis SK Hynix -12,34% et Samsung Electronics -9,47% le 16 juillet. [Fait : données boursières] Le récit que le marché intègre dans les prix est clair : l'offre augmente, la Chine rattrape son retard, les bénéfices 2027 sont révisés à la baisse, et personne ne sait quand le CAPEX de la Big Tech va fléchir.

Dans ce contexte, les analystes Kim Sun-woo, Yang Seung-su et Kim Dong-kwan, de l'équipe semi-conducteurs de Meritz Securities, ont publié dimanche des rapports coordonnés. Le moment de publication tient explicitement compte de la chute du vendredi et de l'affaire Kioxia. L'essentiel va dans le sens inverse : la demande de mémoire actuelle ne se limite pas aux hyperscalers, les achats du camp souverain, Moyen-Orient inclus, entrent en phase active, et la pénurie de DRAM serveur s'aggrave de nouveau depuis la mi-juillet. Leur contre-argument : la thèse qui tient pour acquis un assouplissement de la pénurie en 2028 n'a pas intégré cette demande dans son calcul. [Fait : synthèse du rapport de Meritz Securities, 2026-07-19]

Plutôt que d'en rester à une joute verbale, nous découpons cette thèse en trois blocs vérifiables et les confrontons un à un aux données réelles : la composition de la clientèle de NVIDIA, les achats souverains, et l'usage final.

## 2. La carte clients de NVIDIA : une part à 50%, une croissance venue de l'extérieur

Vérifions d'abord précisément l'affirmation selon laquelle la part des hyperscalers diminuerait. Voici, mises bout à bout, les formulations que NVIDIA publie chaque trimestre.

| Trimestre fiscal | Période | CA data center | Glissement annuel | Part CSP majeurs · hyperscale (formulation officielle) |
|---|---|---|---|---|
| FY25 T3 | 08-10/2024 | 30,77 Mds USD | +112% | environ 50% |
| FY25 T4 | 11/2024-01/2025 | 35,58 Mds USD | +93% | environ 50% |
| FY26 T1 | 02-04/2025 | 39,11 Mds USD | +73% | un peu sous 50% |
| FY26 T2 | 05-07/2025 | 41,10 Mds USD | +56% | environ 50% |
| FY26 T3 | 08-10/2025 | 51,22 Mds USD | +66% | non divulgué |
| FY26 T4 | 11/2025-01/2026 | 62,31 Mds USD | +75% | un peu au-dessus de 50%, croissance tirée par le reste de la clientèle |
| FY27 T1 | 02-04/2026 | 75,2 Mds USD | +92% | Hyperscale 38 Mds USD (~50%) contre ACIE 37 Mds USD |

[Fait : commentaire du CFO de NVIDIA · conférence de résultats]

Deux constats apparaissent simultanément. Premièrement, <strong>le chiffre de part lui-même n'est jamais sorti de la bande des 50% en sept trimestres</strong>. Le récit selon lequel les hyperscalers auraient déjà été relégués au second plan n'est pas corroboré par les données. Deuxièmement, la direction de la composition a pourtant clairement changé. La publication du FY26 T4 précisait que la croissance avait été tirée par le reste de la clientèle et que le chiffre d'affaires s'était diversifié, et à partir du FY27 T1, NVIDIA a commencé à ventiler le data center entre Hyperscale et ACIE (cloud IA, industrie, entreprise). Dès ce premier trimestre, ACIE a atteint 37 Mds USD, quasiment à hauteur des 38 Mds USD d'Hyperscale, et le taux de croissance trimestriel s'est inversé : <strong>ACIE +31% contre Hyperscale +12%</strong>. Au sein d'ACIE, le chiffre d'affaires du cloud IA a plus que triplé en glissement annuel. Le CEO Jensen Huang a affirmé, lors de la conférence, qu'à long terme cette seconde catégorie croîtrait plus vite. [Fait : conférence de résultats]

En superposant à cela la réaccélération du taux de croissance, le tableau se complète. La croissance en glissement annuel du chiffre d'affaires data center, après un point bas à +56% au FY26 T2, est remontée à +66%, +75%, puis +92%. Que la part se maintienne alors que la croissance globale accélère signifie, arithmétiquement, que <strong>plus de la moitié de l'incrément est désormais générée en dehors de l'hyperscale</strong>. [Inférence : arithmétique des publications] Si cette tendance se poursuit ne serait-ce qu'un trimestre de plus, la publication du FY27 T2 fin août pourrait afficher, pour la première fois, un ACIE dépassant l'Hyperscale. À partir de cet instant, le cadre même consistant à juger la durabilité de la demande d'IA en ne regardant que les guidances de CAPEX des quatre géants de la tech deviendrait obsolète.

Précisons une confusion possible. La concentration des clients directs dans le 10-Q (Client A 22%, Client B 14%) a au contraire augmenté, mais il s'agit d'un indicateur au niveau de la distribution, qui agrège les partenaires cartes, les OEM et les gros achats directs : un niveau différent de la diversification des utilisateurs finaux. [Fait : 10-K] Concentration de la distribution et élargissement de la demande finale sont deux phénomènes qui coexistent.

## 3. IA souveraine : l'acheteur que le marché a manqué en ne regardant que les discours

Le plus gros bloc de la demande non hyperscale, c'est le souverain. Le CFO de NVIDIA a indiqué que le chiffre d'affaires de l'IA souveraine au FY2026 avait plus que triplé en un an, <strong>franchissant les 30 Mds USD</strong>. Le Canada, la France, les Pays-Bas, Singapour et le Royaume-Uni ont mené la charge ; au FY27 T1 encore, le chiffre d'affaires souverain a progressé de plus de 80% en glissement annuel, et l'infrastructure NVIDIA est désormais déployée dans quelque 40 pays cumulant environ 50 000 milliards USD de PIB. [Fait : conférence de résultats de NVIDIA]

La réalité physique suit. HUMAIN, en Arabie saoudite, a finalisé un plan de déploiement pouvant aller jusqu'à 600 000 GPU NVIDIA sur trois ans et a déjà reçu un premier lot de 18 000 GB300. Aux Émirats arabes unis, Stargate UAE construit la phase 1 (200 MW) de son cluster de 1 GW avec une mise en service visée au T3 de cette année ; cette seule phase 1 accueillera jusqu'à 35 000 GB300, et l'opérateur G42 a obtenu l'autorisation d'exportation américaine à la mi-juillet. L'UE poursuit son programme de gigafactories IA doté de 20 Mds EUR, l'Inde vise 100 000 GPU publics d'ici la fin de l'année, et SoftBank au Japon cible une commercialisation de son cloud GPU souverain en octobre. [Fait : annonces des entreprises et des États concernés]

Comment cela se traduit-il en mémoire ? Deux canaux sont déjà publics. Le programme mondial Stargate d'OpenAI a signé en octobre 2025 avec Samsung Electronics et SK Hynix une lettre d'intention (LOI) portant sur <strong>jusqu'à 900 000 wafers DRAM par mois</strong>, un volume équivalent à environ 40% de la capacité mondiale de production de DRAM. La limite d'une LOI non contraignante demeure clairement posée. [Fait : presse, LOI] Et SK Hynix a officialisé en juin de cette année un partenariat pluriannuel HBM4 avec NVIDIA, couvrant la future génération Vera Rubin. [Fait : annonce de NVIDIA] Du côté des fonds souverains, la presse a continué de rapporter des rapprochements entre les capitaux émiratis, Mubadala, MGX, G42, Kazna, et le camp SK Hynix.

Un vide doit être honnêtement laissé ouvert. Aucune nouvelle publication confirmant un achat direct massif de DRAM par un acteur souverain auprès de Samsung Electronics ou de SK Hynix n'a été identifiée en juin-juillet. [Non vérifié : contrat direct non divulgué] La demande de mémoire souveraine transite par les OEM serveurs et les intégrateurs système, si bien qu'elle se retrouve mélangée aux hyperscalers dans les publications clients des fabricants de mémoire. [Inférence : structure de distribution] Ce qui est invisible n'est pas la même chose que ce qui n'existe pas. Il n'existe aucun scénario où 600 000 GPU confirmés ne s'accompagneraient pas de mémoire ; la question n'est donc pas l'existence, mais la visibilité, en termes d'ampleur et de calendrier, dans les publications.

## 4. Le regain de tension sur la DRAM serveur : la thèse de Meritz et les données externes

Le regain de tension sur l'offre de DRAM serveur depuis la mi-juillet, pointé par l'équipe de Meritz, n'est pas une affirmation isolée de cette seule maison de courtage. Quatre observations externes pointent dans la même direction.

| Donnée observée | Contenu | Source · date |
|---|---|---|
| Prévision de prix contractuel | Prévision de +13-18% pour les prix contractuels de la DRAM serveur au T3. Impossible à répercuter sur les CSP américains liés par des contrats long terme (LTA), donc la hausse se concentre sur les clients hors LTA | TrendForce, 9/7 |
| Taux de croissance de l'offre | Croissance de l'offre bit RDIMM de 15-20% par an, inférieure à la hausse des expéditions de CPU. Constitution de stocks anticipés par les CSP qui anticipent une pénurie en 2027. Les modules migrent de 96/128 Go vers 32/64 Go | TrendForce, 9/7 |
| Délai de livraison | Délais de livraison de la DRAM serveur dépassant 40 semaines, prix en hausse d'environ 90% par rapport à fin 2025, validité des devis raccourcie à 1-30 jours | Propos d'Inventec rapportés, 16/7 |
| Témoignage d'un fournisseur | Capacité de ne satisfaire que 50-66% de la demande des clients clés, HBM déjà épuisée jusqu'en 2027, pénurie d'offre qui se prolongera au-delà de 2027 | Conférence de résultats de Micron, juillet |

[Fait : chaque source]

Le niveau absolu des prix envoie lui aussi des signaux anormaux. Le prix contractuel fixe de la DRAM PC générique (DDR4 8 Gb) a atteint 21 USD en juin, un record depuis le début des relevés, et le prix spot dépasse le prix fixe de 72%. Des articles ont également rapporté que Samsung Electronics aurait notifié à ses clients chinois une hausse pouvant atteindre 20% des prix DRAM au T3. [Fait : presse sectorielle] Cette combinaison, une hausse des prix contractuels et une prime spot supérieure à 70%, signifie qu'une demande réelle en dehors du canal contractuel est prête à payer une surprime pour s'assurer des volumes en urgence. Ce ne sont pas les hyperscalers liés par des LTA, mais ceux qui se trouvent en dehors, à savoir le souverain, l'entreprise et les clouds de second rang, qui paient ce prix élevé. L'affirmation de TrendForce selon laquelle la hausse se concentre sur les clients hors LTA et celle de Meritz sur l'entrée en phase active des achats souverains sont deux expressions d'un même phénomène. [Inférence : lecture croisée]

L'analyste Kim Sun-woo va plus loin. Selon lui, le marché se méprend, enfermé dans un cadre étroit fait de contrats long terme sacrificiels et de révisions à la baisse pour 2027, et cette méprise devrait être rapidement dissipée par une série d'événements : exécution anticipée du retour aux actionnaires, partenariats incluant des prises de participation de la Big Tech. [Fait : argumentaire du rapport] Il ne s'agit pas d'un fait vérifié mais d'une prévision de la maison de courtage ; le critère de notation sera de vérifier si ces événements se concrétisent réellement pendant la saison des résultats de cette semaine. La direction reste néanmoins cohérente avec les mouvements observés dans l'article précédent : les fonds levés par le président de SK Hynix Chey Tae-won lors de l'introduction au Nasdaq, ses démarches de partenariat, et le contrat pluriannuel entre SK Hynix et NVIDIA.

## 5. Codex à 9 millions : les premiers chiffres de la demande finale

Dans le débat sur le CAPEX IA, le point le plus attaqué n'était pas l'infrastructure elle-même, mais son aboutissement : les data centers se construisent, mais les preuves que l'usage final augmente à due proportion restent minces. C'est précisément sur ce maillon faible que des chiffres notables commencent à apparaître.

| Date | Nombre d'utilisateurs | Remarque |
|---|---|---|
| Février 2026 | 1 M | Utilisateurs actifs de Codex seul |
| 8 avril | 3 M | Actifs hebdomadaires, réinitialisation des limites d'usage annoncée à chaque palier d'1 M |
| 21 avril | 4 M | +1 M en deux semaines |
| Fin mai-début juin | Plus de 5 M | 6x par rapport à février |
| 9 juillet | Lancement officiel de GPT-5.6 | 3 variantes Sol, Terra, Luna ; Codex intégré à l'application de bureau ChatGPT |
| 12 juillet | 6 M | À partir de là, métrique combinée Codex + ChatGPT Work |
| Autour du 15 juillet | 9 M | +3 M en trois jours |

[Fait : déclarations publiques des dirigeants d'OpenAI, presse]

Deux réserves s'imposent, par honnêteté. Les chiffres postérieurs au 9 juillet ne représentent plus Codex seul mais une métrique combinée avec ChatGPT Work, ce qui rend une comparaison strictement continue avec la période précédente difficile. Et une extrapolation externe qui prolonge simplement le rythme de croissance de fin mai plaçait le franchissement des 10 millions en octobre, alors qu'en réalité le seuil de 9 millions a été atteint dès la mi-juillet. Précisons que cette ligne d'extrapolation n'est pas une projection officielle d'OpenAI. [Fait : vérification de la source de l'extrapolation] Même en tenant compte du changement de définition de l'indicateur, il reste qu'une accélération avançant la trajectoire attendue d'environ trois mois a été observée sur les trois jours qui ont suivi le lancement de GPT-5.6.

Si Codex compte, ce n'est pas par l'ampleur du chiffre, mais par la nature de la demande. Codex est un produit qui convertit du temps de travail humain en temps d'inférence. L'agent peut travailler plus longtemps sans que l'humain reste connecté plus longtemps, et lorsqu'une seule personne fait tourner plusieurs tâches en parallèle, <strong>le volume de travail augmente plus vite que le nombre d'utilisateurs</strong>. À partir de ce stade, l'unité de la demande n'est plus l'utilisateur actif mensuel, mais le temps d'exécution total des agents. C'est exactement la même structure que celle utilisée dans l'article précédent pour réécrire le plafond du modèle de demande de mémoire IA : nombre de charges de travail multiplié par la mémoire par charge de travail multiplié par la fréquence d'exécution.

Le débat sur l'efficacité s'inverse ici aussi. OpenAI a elle-même indiqué que GPT-5.6 Sol était 54% plus efficace en tokens que la génération précédente. Le fait que les utilisateurs et l'usage aient explosé juste après la sortie d'un modèle moins coûteux par token constitue un cas empirique de l'hypothèse de Jevons dans le domaine des agents de codage : l'amélioration de l'efficacité ne réduit pas la demande de calcul, elle <strong>élargit le périmètre des tâches que l'on peut confier à l'IA</strong>. [Inférence : effet Jevons] Ce qu'il faut regarder, ce n'est pas le taux de baisse du prix des tokens, mais le volume de travail que cette baisse de prix vient d'ouvrir.

## 6. Alors, comment cela se traduit-il en mémoire ?

De la retenue s'impose aussi. Le seul chiffre de 9 millions pour Codex ne saurait expliquer à lui seul le cycle mémoire. Pour que le nombre d'utilisateurs se traduise en demande de bits mémoire, il faut passer par quatre coefficients de conversion : le volume d'exécutions simultanées, la longueur du contexte, la capacité mémoire embarquée par accélérateur, et le taux de croissance de l'offre. [Inférence : modèle de demande] Si l'un seul de ces maillons est faible, l'indicateur médiatique et la demande réelle se dissocient.

Mais en confrontant les variables haussières posées comme arguments du scénario à 35% dans l'article précédent sur les scénarios de demande aux données observées cette semaine, un alignement apparaît.

- L'élargissement de la base de la demande d'accélérateurs s'est vu confirmé par l'inversion du taux de croissance d'ACIE et le triplement du chiffre d'affaires souverain.
- L'inférence agentique permanente a produit ses premiers chiffres avec les 3 millions en trois jours de Codex et le changement d'unité de mesure.
- La diffusion au-delà du HBM s'est déjà manifestée dans les prix, avec la prévision de +13-18% sur les prix contractuels de la DRAM serveur, des délais de 40 semaines et une prime spot de 72%.
- L'hypothèse selon laquelle l'usage l'emporte sur l'efficacité a trouvé une confirmation empirique contre-intuitive dans l'explosion d'usage survenue juste après une amélioration de 54% de l'efficacité en tokens.

L'implication pour le récit d'un assouplissement de l'offre en 2028 se joue aussi ici. La formule des tenants de l'assouplissement pose généralement le ralentissement de la croissance du CAPEX des hyperscalers comme plafond du taux de croissance de la demande. Or, si la moitié de la demande incrémentale commence à provenir de l'extérieur de ce périmètre, l'hypothèse même de plafond doit être recalculée. C'est exactement ce point que vise la contestation de Meritz. Nous ne modifions pas les probabilités dans l'immédiat. Nous conservons l'ossature 45% de base, 35% de dépassement, 20% de sous-performance, tout en actant que l'argumentaire haussier commence à recevoir des données réelles sur trois fronts distincts. La mise à jour des probabilités se fera lorsque le tableau de décision ci-dessous se sera rempli. [Inférence : gestion des scénarios]

## 7. Vérification des contre-arguments

Plus un argument paraît solide, plus il faut lui opposer son contraire.

- <strong>La qualité de la demande non hyperscale.</strong> ACIE inclut les néoclouds. Les commandes de ces clouds de second rang, fragiles en coût du capital, sont les premières annulées dès que les taux d'intérêt et les conditions de financement se resserrent. L'inversion du taux de croissance ne garantit pas la durabilité de la demande.
- <strong>La volatilité politique du souverain.</strong> Les projets nationaux sont exposés aux élections, aux budgets et aux restrictions à l'exportation. L'appel d'offres des gigafactories de l'UE a déjà été reporté à deux reprises, et les volumes du Moyen-Orient dépendent d'un seul interrupteur : l'autorisation d'exportation américaine.
- <strong>Le piège des indicateurs.</strong> Les 9 millions de Codex sont un chiffre publié juste après un changement de définition vers une métrique combinée, et le critère d'activité n'a pas été divulgué. La direction de la croissance est un fait observé, mais son ampleur n'est pas encore dissociée du marketing.
- <strong>L'autodestruction de la flambée des prix.</strong> Le regain de tension sur la DRAM serveur est à la fois un argument haussier et, comme l'a montré le cas d'IBM, un risque : il grignote les budgets IT et crée un vide de demande après les achats anticipés. Le président Chey lui-même a averti qu'une surchauffe des prix pouvait détruire la demande.
- <strong>La distinction entre prévision et fait observé.</strong> Les événements anticipés par Meritz (exécution anticipée du retour aux actionnaires, partenariats avec prise de participation de la Big Tech) restent des prévisions. S'ils ne se matérialisent pas, c'est la vision étroite qui aura eu raison.

## 8. Tableau de décision : qu'est-ce qui tranchera la réponse ?

- Aux conférences de résultats de Samsung Electronics et SK Hynix, autour du 30 juillet, l'ampleur de la hausse des prix contractuels du T3 confirme-t-elle la fourchette de +13-18% de TrendForce, et des mentions des clients hors LTA et des volumes souverains apparaissent-elles ?
- L'exécution anticipée du retour aux actionnaires de SK Hynix et les partenariats avec prise de participation se traduisent-ils en publications officielles ? C'est le critère de notation direct de la prévision de Meritz.
- Dans la publication du FY27 T2 de NVIDIA fin août, ACIE dépasse-t-il pour la première fois l'Hyperscale ? Si oui, l'élargissement de la base de demande cessera d'être un récit pour devenir un chiffre publié.
- Un contrat direct de mémoire d'origine souveraine, ou une commande de grande ampleur transitant par un OEM serveur, remonte-t-il au niveau des publications officielles ? La conversion de la LOI de Stargate en contrat contraignant est la première candidate.
- Les indicateurs d'usage de Codex et des agents concurrents commencent-ils à être publiés sur la base du temps d'exécution, au moment du franchissement des 10 millions ?

Le juge de paix ne change pas. Si les prix contractuels de la DRAM se retournent, tout ce récit de la demande sera rejeté par le marché ; s'ils tiennent, c'est la courbe de demande trop timidement tracée qui devra être redessinée.

---

_Les titres mentionnés dans cet article sont des exemples destinés à l'analyse et ne constituent pas une recommandation d'achat ou de vente d'un titre particulier. La décision d'investissement et sa responsabilité incombent à l'investisseur lui-même. Le rapport de Meritz Securities a été cité sous une forme reconstituée à partir de son essentiel ; la responsabilité du texte original des chiffres détaillés et des prévisions incombe à cette maison de courtage. Le nombre d'utilisateurs de Codex a changé de définition après le 9 juillet pour devenir une métrique combinée avec ChatGPT Work, rendant une comparaison stricte avec la période antérieure difficile, et la ligne d'extrapolation visant 10 millions en octobre n'est pas une projection officielle d'OpenAI. Aucun achat direct de mémoire par un acteur souverain n'a été confirmé par une publication officielle, et les volumes liés à Stargate en sont au stade d'une lettre d'intention non contraignante. Les cours, indices et données de prix sont fondés sur les informations publiques disponibles jusqu'au 17 juillet 2026 et n'intègrent pas les évolutions postérieures._

---

### Articles liés

- [La demande de mémoire pour l'IA dépassera-t-elle les attentes ? Lire les probabilités de surcroissance via les scénarios de demande et la carte de l'offre](/fr/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/)
- [Deux mois de déclarations du président de SK Hynix Chey Tae-won : l'entreprise se renforce, le pic de marge est passé](/fr/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/)
- [Le vrai débat des semi-conducteurs : quatre horloges physiques et une horloge boursière](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [Les semi-conducteurs sont-ils cycliques et quelle est la juste valeur ? Valoriser Samsung, SK Hynix et Micron avec le FCFE et les bénéfices normalisés](/fr/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
