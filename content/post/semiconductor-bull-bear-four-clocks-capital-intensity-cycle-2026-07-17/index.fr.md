---
title: "Le vrai débat des semi-conducteurs : quatre horloges physiques et une horloge boursière"
slug: "semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17"
date: 2026-07-17T11:00:00+09:00
description: "Les haussiers et les baissiers des semi-conducteurs ne débattent plus de l'existence de la demande en IA. Les vraies questions sont de savoir si la demande dépasse l'offre et les gains d'efficacité, si les décalages entre prix, commandes, construction et monétisation se resserrent, et si le chiffre d'affaires incrémental survit à l'amortissement et au coût du capital pour atteindre le flux de trésorerie actionnarial. La trajectoire centrale est un haussier fondamental coexistant avec un baissier de valorisation."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["Semi-conducteurs", "Mémoire", "HBM", "AI CAPEX", "TSMC", "Samsung Electronics", "SK Hynix", "Micron", "Packaging avancé", "Intensité capitalistique", "Valorisation"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte
> Cet article est la synthèse qui réunit dans un même cadre les axes traités séparément jusqu'ici. La preuve de la demande a été traitée dans [La raison pour laquelle IBM a manqué ses résultats est une preuve de la vigueur de la mémoire](/fr/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/), la diffusion de l'offre dans [Le vide d'approvisionnement qui se propage au-delà du HBM](/fr/post/memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14/), l'ampleur de l'offre et de la demande dans [Recherche approfondie sur l'offre et la demande de HBM à l'horizon 2030](/fr/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/), la capacité de paiement dans [Qui paie le consensus semi-conducteurs de 2027](/fr/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/), et la valorisation dans [Le pire scénario est-il déjà dans le prix](/fr/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/). Les hubs associés sont le [Hub IA HBM](/fr/page/korea-semiconductor-hbm-kospi-hub/) et le [Hub Exclusive Analysis](/fr/page/exclusive-analysis-hub/).

## TL;DR

* Les haussiers (bull) et les baissiers (bear) des semi-conducteurs ne se disputent plus sur l'existence ou non de la demande en IA. Les commandes officielles, la pénurie de TSMC en procédés de pointe et en packaging avancé, les contraintes d'approvisionnement en mémoire chez Dell et HPE, et le CAPEX des hyperscalers penchent tous vers l'idée que <strong>la demande réelle en IA est forte</strong>.
* Le vrai débat porte sur trois points. La croissance de la demande dépasse-t-elle l'offre et les gains d'efficacité. Les décalages entre prix, commandes, construction et monétisation se resserrent-ils. Le chiffre d'affaires additionnel survit-il à l'amortissement, au coût du financement et à la concurrence pour se transformer en flux de trésorerie actionnarial.
* Le bull le plus solide soutient que « l'IA devient la nouvelle couche de base de tout le calcul, les goulots d'étranglement physiques durent plus longtemps que prévu, et les contrats de long terme combinés à l'oligopole créent un <strong>plancher</strong> de profits élevé ».
* Le bear le plus solide soutient que « la demande en IA continue de croître, mais dès que <strong>le taux de croissance franchit son pic</strong>, l'offre, l'amortissement et le coût du capital augmentent simultanément, ce qui normalise les prix, les marges, le ROIC et les multiples ».
* La trajectoire la plus probable actuellement est hybride. <strong>L'industrie peut être haussière tandis que l'action est baissière sur le plan de la valorisation</strong> (probabilité de 55%). Même si les résultats 2026-2027 sont solides, l'action actualise d'abord la réaction de l'offre et le retard de retour sur investissement de 2027-2028. \[Portée\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Thèse principale</div>
  <div class="thesis-callout__body">
    L'industrie des semi-conducteurs pour l'IA n'est pas encore brisée. Mais le scarcity cycle est en train de basculer vers un capital-intensity cycle. La prochaine phase de hausse ne commencera pas avec une annonce de CAPEX, mais lorsque le raccordement électrique, le taux d'utilisation et les flux de trésorerie liés à l'IA rattraperont l'amortissement et le coût du capital.
  </div>
</div>

---

## 1. Principe d'analyse : ne pas mélanger les quatre questions

Le débat sur les semi-conducteurs se trompe souvent parce qu'il fusionne quatre questions distinctes en une seule phrase.

1. <strong>Industrie</strong> : la demande en calcul IA et en mémoire croît-elle sur le long terme.
2. <strong>Profits des entreprises</strong> : les fournisseurs actuels maintiennent-ils des prix et des marges élevés sur cette demande.
3. <strong>Cours de l'action</strong> : dans quelle mesure le prix actuel intègre-t-il déjà les profits et les risques futurs.
4. <strong>Portefeuille</strong> : même pour une bonne entreprise, est-il justifié d'en détenir davantage compte tenu du niveau de concentration et de liquidités actuel.

Le fait que « la demande en IA est forte » répond à la question industrielle, mais pas aux questions de cours de bourse et de portefeuille. À l'inverse, le fait que « le SOXX a chuté brutalement » concerne le timing du cours de bourse, sans démontrer immédiatement un effondrement de la demande industrielle.

Sans respecter cette distinction, les haussiers achètent une bonne industrie à n'importe quel prix, et les baissiers déclarent la fin de l'industrie après une seule journée de chute.

<strong>Avertissement sur le périmètre</strong> : le périmètre central de cet article couvre la mémoire, la fonderie de pointe, le packaging avancé, les fabless IA, le réseau, ainsi que les équipements et matériaux associés, tous tirés par l'IA. L'automobile, l'industriel, l'analogique et les procédés matures classiques ne sont traités que dans la mesure où ils se connectent à la chaîne d'approvisionnement IA. Ce jugement ne doit donc pas être appliqué uniformément à tous les sous-secteurs des semi-conducteurs.

---

## 2. Quatre horloges physiques et une horloge boursière

Sur ce marché, cinq horloges avancent à des vitesses différentes. Ce cadre est l'ossature de cet article.

| Horloge | Ce qu'elle mesure | Signification actuelle |
|---|---|---|
| Horloge des prix | ASP des contrats mémoire, mix, prix fonderie et packaging | Se reflète le plus vite dans les résultats actuels |
| Horloge des investissements | Commandes GPU, wafers, équipements, fabs, CAPEX | Réserve l'offre future et la volonté du client |
| Horloge de construction | Raccordement électrique, achèvement des data centers, installation des racks, montée en cadence des fabs | Convertit l'investissement annoncé en capacité opérationnelle réelle |
| Horloge de monétisation | Chiffre d'affaires IA/cloud, marge brute, FCF | Récupère les dépenses d'investissement, l'amortissement et les charges financières |
| Horloge boursière | Anticipe les quatre horloges précédentes de 6 à 12 mois | Bouge en premier et actualise le taux de variation |

Lorsque les horloges des prix et des investissements avancent tandis que celles de la construction et de la monétisation traînent, <strong>de bons résultats et un CAPEX relevé peuvent en réalité devenir un motif de vente.</strong> Le marché regarde moins le profit actuel que la capacité future inutilisée, l'amortissement, la dette et le vide de retour sur investissement.

À l'inverse, lorsque les quatre horloges se resserrent, la phase haussière repart. C'est le cas quand les GW annoncés se traduisent en raccordement électrique réel et en taux d'utilisation des GPU, quand la croissance de la marge brute IA dépasse l'amortissement et les charges d'intérêts, et quand les achats anticipés des clients s'écoulent en usage réel plutôt qu'en stock.

Avec ce cadre, des questions jusque-là traitées séparément s'expliquent dans une même structure. Pourquoi les résultats sont bons mais l'action baisse. Pourquoi le CAPEX augmente mais l'action du client reste faible. Pourquoi, en cas de pénurie d'offre, les valeurs d'équipement reculent les premières.

---

## 3. Les prémisses communes aux bulls et aux bears

Les bulls et les bears les plus rigoureux s'accordent globalement sur les points suivants.

1. La demande d'entraînement et d'inférence IA est réelle aujourd'hui.
2. Des goulots d'étranglement physiques existent dans les procédés de pointe, le HBM, le packaging avancé, l'électricité et le réseau.
3. Les résultats de la chaîne d'approvisionnement en 2026-2027 seront probablement solides.
4. Le cours de bourse regarde toujours en premier le taux de variation des estimations de profit et la prochaine phase d'offre, avant même les résultats absolus.
5. Tous les semi-conducteurs ne bénéficient pas également de cette dynamique.
6. Une bonne industrie et un bon moment d'achat sont deux choses différentes.

Le débat entre les deux camps ne porte donc pas sur l'existence de la demande, mais sur <strong>sa durée et sa qualité, la vitesse de la réaction de l'offre, la rentabilité du chiffre d'affaires incrémental, et la valorisation et le positionnement actuels</strong>.

---

# Partie I. La thèse haussière (Bull Case)

> <strong>À mesure que l'IA devient la nouvelle couche de base de tout le calcul et non plus une simple fonctionnalité logicielle, la demande en puissance de calcul, en capacité mémoire, en bande passante, en réseau et en électricité augmente conjointement. L'offre ne peut pas suivre immédiatement en raison des longs délais de mise en œuvre des fabs, du packaging, de l'électricité et de la qualification client, et l'oligopole des fournisseurs combiné aux contrats de long terme crée un plancher de profits plus élevé et plus durable que par le passé.</strong>

L'essentiel de la thèse haussière n'est pas que les prix accélèrent indéfiniment. C'est que même si le taux de hausse des prix ralentit, la combinaison d'un ASP plus élevé qu'avant, d'un mix premium, d'une meilleure visibilité des volumes et d'une discipline capitalistique peut élargir <strong>la surface totale des profits</strong>.

### 4. La demande se vérifie par des commandes physiques, pas par des annonces

Dans la conférence TSMC du T2 2026, l'élément le plus important n'est pas le discours optimiste de long terme, mais <strong>le changement réel de CAPEX et d'allocation de capacité</strong>. \[Fait/Grade B : documents de la conférence et recoupement de plusieurs analyses, contrôle direct limité sur le texte original de l'IR officielle\]

- Relèvement de la guidance de croissance du chiffre d'affaires de l'exercice 2026 à plus de 40%
- Relèvement du CAPEX 2026 à 60-64 Mds USD
- Explication d'un large écart entre l'offre et la demande pour les procédés de pointe sous N3 et le packaging avancé
- Indication que les commandes clients ne sont pas simplement additionnées, mais vérifiées jusqu'à l'emplacement du data center, l'avancement de la construction, la sécurisation de l'électricité et l'installation des racks

Cette combinaison affaiblit la thèse baissière faible des « commandes fantômes » et de « toute la demande IA n'est que du double comptage ». La décision de TSMC d'acheter des équipements et de construire des fabs est difficile à prendre sans signaux de demande de long terme, d'acomptes et de feuilles de route de co-développement de la part des clients.

Le fait que Dell et HPE désignent le DRAM et le NAND comme la contrainte numéro un de l'approvisionnement serveur, et que Teradyne confirme une forte demande de second semestre pour les tests HBM et DRAM, vont dans le même sens. \[Fait/Grade C-B : vérification de canal par des brokers\] La demande ne se trouve pas seulement dans des diapositives, elle apparaît dans les expéditions de serveurs, l'allocation de mémoire, les équipements de test et la capacité de packaging.

<strong>Lecture haussière</strong> : la preuve la plus importante de la demande en IA n'est pas les prévisions de chiffre d'affaires, mais le fait que les fournisseurs engagent un <strong>capital difficile à annuler</strong>.

<strong>Condition de réfutation</strong> : les hyperscalers réduisent réellement leur CAPEX. TSMC et les fabricants de mémoire retardent la livraison des équipements et la montée en cadence des fabs. Des retards de contrats clients et une baisse du taux d'utilisation apparaissent simultanément.

### 5. La demande se diffuse d'un seul type de GPU vers l'ensemble de la nomenclature serveur

Les premiers investissements en IA se concentraient sur les GPU et le HBM, mais à mesure que l'échelle grandit, le goulot d'étranglement se déplace vers le CPU, le réseau, le stockage, la gestion de l'alimentation, les substrats et les composants passifs.

- L'IA agentique sollicite simultanément non seulement le GPU, mais aussi le CPU, la mémoire, le réseau et le stockage.
- L'inférence à grande échelle accroît les besoins en KV cache et en bande passante mémoire.
- Plus l'extension passe de scale-up à scale-out puis à scale-across, plus la demande en commutateurs haute vitesse, en optique et en connexions cohérentes augmente.
- Dans les data centers IA, les eSSD, les circuits de gestion d'alimentation, les MLCC, l'ABF, le CCL et les PCB haute densité de couches deviennent des goulots d'étranglement retardés.

Ainsi, même si la croissance d'un seul titre comme NVIDIA ralentit, le marché adressable total des semi-conducteurs IA peut s'élargir vers d'autres composants. Les ASIC propriétaires n'invalident pas non plus totalement cette logique. Les TPU et Trainium peuvent réduire la part de marché des GPU, mais ils consomment toujours des procédés de pointe, du HBM ou du DRAM haute performance, du packaging avancé et du réseau.

<strong>Lecture haussière</strong> : l'investissement en IA évolue du cycle du GPU vers <strong>le cycle de la nomenclature du data center IA</strong>. Le leadership peut changer de mains, mais la demande totale en silicium, mémoire et packaging se maintient.

<strong>Condition de réfutation</strong> : les gains d'efficacité augmentent le débit, mais les dépenses en dollars pour les serveurs, la mémoire et le réseau diminuent, et ce phénomène se répète chez plusieurs clients.

### 6. Le HBM est un produit qui grignote sa propre offre

Le HBM nécessite davantage de surface de wafer, du TSV et de l'empilement, du packaging, des tests et de la qualification client. Quand le mix HBM augmente, le nombre de bits productibles pour un même volume de wafers en entrée diminue, ce qui contraint aussi la capacité DRAM classique.

Cela crée deux effets haussiers. Premièrement, l'offre de HBM elle-même a du mal à croître rapidement. Deuxièmement, la conversion vers le HBM réduit l'offre effective de DRAM classique, ce qui soutient conjointement les prix du DRAM serveur et du DRAM standard.

Les nouvelles fabs ne deviennent pas non plus des sources d'offre dès leur annonce. L'électricité, l'eau, les salles blanches, l'installation des équipements, la montée en cadence des procédés, le rendement et la qualification client sont nécessaires, dans cet ordre. Il existe un décalage avant que le site Y1 de SK Hynix et les nouvelles installations de Samsung Electronics et Micron ne contribuent réellement à l'offre de bits.

<strong>Lecture haussière</strong> : la pénurie de ce cycle est une <strong>pénurie composite exigeant simultanément de bons wafers, un empilement à haut rendement, un packaging validé et la qualification client</strong>. C'est pourquoi elle ne se résout pas immédiatement, même à coups d'argent.

<strong>Condition de réfutation</strong> : le rendement du HBM et la productivité du packaging progressent plus vite que prévu, et la qualification client chez Samsung Electronics et Micron se traduit par des volumes massifs, faisant dépasser le taux de croissance de l'offre sur celui de la demande.

### 7. L'oligopole et les contrats de long terme peuvent réduire l'amplitude du cycle

L'industrie de la mémoire compte moins de fournisseurs qu'avant, et le HBM implique une co-conception et une qualification approfondies avec chaque client. Les LTA (contrats de long terme) obligent à renoncer à une partie de la flambée des prix spot, mais ils augmentent la visibilité des volumes, le lock-in client et la confiance dans l'investissement.

Les cycles passés suivaient une structure où les fournisseurs augmentaient leurs capacités en réaction au prix spot, les clients accumulaient des stocks, puis les prix s'effondraient. Si les contrats de long terme incluent des volumes minimums, des formules d'ajustement de prix et une nature take-or-pay, <strong>le pic de profit peut être plus bas, mais le plancher et la durée peuvent être plus élevés.</strong>

Ce que le camp haussier achète, ce n'est pas l'hypothèse que « les prix continueront de monter toujours plus vite », mais que « des profits élevés dureront plus longtemps ».

<strong>Point clé non vérifié</strong> : les bornes basse et haute des prix, les volumes minimums, les clauses de renégociation et d'annulation des LTA restent en grande partie non publiques. Il ne faut pas élever les LTA au rang de garantie inconditionnelle de profit. \[Non vérifié\]

### 8. Le fossé concurrentiel des procédés de pointe réside dans la courbe d'apprentissage, pas dans les équipements

La déclaration du président de TSMC C.C. Wei selon laquelle « choisir une fonderie n'est pas comme choisir du lait dans une supérette » décrit avec précision le coût de changement des procédés de pointe.

Le client passe plusieurs années avec le fournisseur, du choix du procédé à la conception PDK/IP, en passant par les puces de test, la co-optimisation, l'apprentissage du rendement, la sécurisation de la capacité et jusqu'à la production de masse. Posséder les mêmes équipements ASML ne suffit pas à faire migrer un client immédiatement. Le packaging avancé exige lui aussi de résoudre conjointement le substrat, la thermique, l'alimentation, l'intégrité du signal et les tests.

<strong>Lecture haussière</strong> : même si les semi-conducteurs de pointe ressemblent à une commodité, ils n'en sont pas vraiment une, en raison du coût de changement pour le client et de l'apprentissage conjoint. Même si l'offre augmente, le surprofit d'un leader éprouvé peut durer plus longtemps que prévu. En période de pénurie, le client choisit <strong>le fournisseur qui tient les délais et le rendement</strong> plutôt que le moins cher.

### 9. La pénurie d'électricité et de permis retarde la demande, mais ne la détruit pas nécessairement

Les retards de raccordement électrique et de construction des data centers constituent l'argument central du camp baissier. Mais le camp haussier y voit non pas une absence de demande, mais <strong>un arriéré en attente de mise en service</strong>.

Les opérateurs qui ont sécurisé l'électricité, le terrain, les postes de transformation et le refroidissement détiennent des actifs rares. Tant que la demande se maintient, les retards de construction peuvent se traduire par un report de livraison et une prime de prix plutôt que par des annulations de commandes. Le fait que TSMC vérifie l'emplacement des data centers de ses clients et leur sécurisation électrique prouve qu'au moins pour les clients de premier rang, l'horloge de construction ne s'est pas complètement arrêtée.

<strong>Condition haussière</strong> : les projets retardés ne doivent pas être annulés mais mis en service séquentiellement, et cette mise en service doit se traduire par un taux d'utilisation élevé et du chiffre d'affaires cloud.

### 10. Le rattrapage chinois est un risque sur le segment généraliste, mais ne peut pas remplacer la frontière technologique à court terme

L'introduction en bourse de CXMT et sa levée de capitaux massive constituent un risque d'approvisionnement en DRAM classique à moyen et long terme. Mais pour le HBM, les procédés de pointe et le packaging avancé, des barrières subsistent en matière de rendement, d'équipements, de matériaux, d'écosystème de conception et de qualification client.

La réglementation américaine sur les équipements destinés à la Chine et les discussions sur des restrictions d'achat visant CXMT et YMTC pourraient ralentir l'expansion internationale des acteurs chinois et renforcer la position de marché ex-Chine des fournisseurs coréens, américains et taïwanais.

<strong>Lecture haussière</strong> : l'offre chinoise est moins un problème d'« effondrement du HBM aujourd'hui » qu'un problème de <strong>« plafond des prix du DRAM classique après 2028 »</strong>. Le décalage technologique et de qualification est trop long pour compromettre la thèse haussière à court terme.

### 11. Les données d'exportation réelles confirment la vigueur

Selon les chiffres provisoires du Service des douanes coréen pour le 1er au 10 juillet 2026, les exportations de semi-conducteurs sont restées solides à 11,2 Mds USD. Le proxy HBM ajusté de la ligne de base sur les exportations de DRAM/HBM de la Corée vers Taïwan en juin est lui aussi resté constructif. \[Fait/Grade A-B : Service des douanes officiel, le proxy est de qualité moyenne\]

Ces données ne prouvent pas directement le chiffre d'affaires HBM par entreprise, mais elles réfutent au moins l'idée que le momentum des expéditions de semi-conducteurs coréens se serait brutalement retourné.

<strong>Avertissement</strong> : les chiffres provisoires à dix jours ne sont qu'une alerte précoce. Tant que l'attribution par produit et par entreprise ainsi que l'effet de base de fin de mois ne sont pas confirmés, il ne faut pas les élever au rang de thèse de long terme.

### 12. Un multiple bas peut déjà intégrer une normalisation partielle des profits

Les actions mémoire appartiennent à une industrie où un P/E bas s'applique aux profits de pic. Un P/E bas n'est donc pas en soi la preuve d'un titre bon marché. Mais si le marché actualise excessivement la persistance des profits de 2027 alors que le plancher réel des profits s'est élevé par rapport au passé, l'action peut monter grâce à une <strong>normalisation du multiple</strong> même sans nouvelle hausse de l'EPS.

L'asymétrie haussière ne repose pas sur l'idée que « le prix ne peut monter que si l'accélération continue ». Elle repose sur l'idée que si les prix contractuels se stabilisent à un niveau élevé, si les LTA et le mix premium maintiennent le FCF, et si la discipline des fournisseurs est confirmée, le marché pourrait attribuer non pas un multiple de pic, mais un <strong>multiple de profits durables (durable earnings multiple)</strong>.

---

# Partie II. La thèse baissière (Bear Case)

> <strong>La demande en IA ne disparaît pas. Mais lorsque le taux de croissance de la demande franchit son pic et que la normalisation des achats anticipés, la nouvelle offre, l'amortissement et le coût du capital des clients apparaissent simultanément, la marge incrémentale des fournisseurs et le multiple boursier se compriment ensemble. L'industrie peut croître tandis que les actionnaires subissent de faibles rendements.</strong>

L'essentiel de la thèse baissière n'est pas l'effondrement du chiffre d'affaires, mais <strong>la baisse de rentabilité du chiffre d'affaires incrémental</strong>. Même si de bonnes nouvelles continuent de tomber, si l'ampleur des révisions à la hausse de l'EPS se réduit et que la valorisation baisse, l'action recule en premier.

### 13. Le cours de bourse lit toujours le taux de variation avant les résultats absolus

Le pic du T4 2026 dans les documents de Morgan Stanley se lit plus justement comme <strong>le pic du taux de croissance en glissement annuel des prix contractuels</strong> que comme un pic de prix mémoire absolu. \[Grade C/faible-moyen : définition du prix et hypothèses originales non directement vérifiées\] Même si les prix continuent de monter et que l'EPS augmente, si l'ampleur de la hausse se réduit, l'action peut se retourner en premier.

Les actions de semi-conducteurs sont plus sensibles à la dérivée seconde qu'à la dérivée première.

- Hausse du chiffre d'affaires : peut être un fait déjà connu.
- Hausse de l'EPS : peut être déjà intégrée au consensus.
- Ralentissement de l'ampleur des révisions à la hausse de l'EPS : c'est une information nouvelle, et elle est négative pour l'action.

La faiblesse des semi-conducteurs en juillet 2026 ne confirme pas un effondrement de l'industrie, mais le fait que l'action n'ait pas réagi à de bons résultats de TSMC et à des commentaires positifs sur la demande en IA montre que <strong>l'utilité marginale des attentes a disparu</strong>.

### 14. Les rush orders et les contraintes d'approvisionnement peuvent anticiper la demande future

Les contraintes d'approvisionnement en DRAM et NAND chez Dell et HPE, ainsi que les rush orders des OEM serveurs, sont la preuve d'une demande actuellement forte. \[Grade C-B : documents transmis par BofA\] Mais ils peuvent aussi constituer un signal de fin de cycle, les clients avançant leurs commandes par crainte de la pénurie et de la hausse des prix.

Face à la hausse du coût de la mémoire, Cisco a pris les mesures suivantes. \[Grade C-B : documents transmis par JPM\]

- Engagements d'achat anticipé de mémoire
- Hausse des prix des produits
- Réduction de la quantité de mémoire embarquée dans les commutateurs
- Arrêt de certaines transactions serveur

Il s'agit là d'un <strong>comportement précoce de destruction de la demande</strong>, plus significatif qu'une simple accumulation de stocks. Dans le [cas d'IBM](/fr/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/) également, les clients ont redirigé leur budget vers des achats anticipés de serveurs, de stockage et de mémoire, ce qui a retardé une partie des contrats logiciels et systèmes. \[Fait/Grade A : formulaire 8-K d'IBM\]

Si les expéditions actuelles correspondent à la consommation finale, les commandes se maintiendront même après la normalisation de l'offre. Si en revanche il s'agit d'achats anticipés, un vide de commandes apparaîtra pendant la période d'écoulement des stocks.

### 15. Une hausse de prix excessive détruit elle-même la demande

La hausse des prix de la mémoire profite aux résultats des fournisseurs, mais elle augmente la nomenclature et le prix des produits chez les clients. Les clients sensibles au prix, dans le PC, le smartphone et les serveurs génériques, peuvent réduire les spécifications ou reporter leurs achats.

Les documents de la conférence TSMC expliquaient que la hausse des prix des composants pèse sur les marchés finaux grand public et sensibles au prix. Même si la demande la plus haut de gamme des data centers IA reste forte, une demande IT généraliste faible accentue la polarisation interne de l'industrie.

Le risque perçu par le camp baissier n'est pas que « la demande en HBM disparaisse ». C'est que les prix élevés du HBM et du DRAM serveur poussent les clients vers <strong>des conceptions alternatives, l'optimisation de la mémoire, l'ajustement du calendrier d'achat et une contraction de la demande pour les produits génériques</strong>.

### 16. La réaction de l'offre est la plus forte lorsque la pénurie est la plus intense

Le relèvement du CAPEX de TSMC, l'expansion des trois fabricants de mémoire et l'élargissement de la capacité de packaging avancé et de test sont à la fois la preuve de la demande actuelle et <strong>la graine de l'offre future</strong>.

En 2027-2028, les éléments suivants pourraient converger.

- Augmentation des mises en wafer dans les nouvelles fabs
- Amélioration du rendement du HBM et de la productivité de l'empilement
- Atténuation du goulot d'étranglement du packaging avancé
- Hausse de la part de marché de Samsung Electronics et Micron sur le HBM4
- Expansion de l'offre de DRAM classique par CXMT

Une fois le goulot d'étranglement résorbé, les expéditions totales de l'industrie augmentent, mais la scarcity premium des gagnants actuels diminue. Même si SK Hynix vend davantage de volumes, la prime de prix du HBM et la marge incrémentale pourraient baisser.

<strong>La résorption du goulot d'étranglement est une bonne nouvelle pour les clients et l'industrie, mais elle peut être une mauvaise nouvelle pour le surprofit des fournisseurs en place.</strong>

### 17. Le goulot d'étranglement du CAPEX IA se déplace de la puce vers le coût du capital

Le CAPEX cumulé 2027 de 801 Mds USD estimé par Citi pour Alphabet, Meta et Amazon n'est pas une guidance d'entreprise, mais une estimation agressive d'analystes. \[Grade C-B\] Ce chiffre importe moins par son ampleur que par l'implication du modèle selon laquelle <strong>le FCF des trois entreprises basculerait en déficit en 2027-2028</strong>.

Selon les documents officiels de l'exercice 2026 d'Oracle, voici la situation. \[Fait/Grade A : formulaire 10-K SEC\]

| Poste | Montant |
|---|---:|
| CAPEX | 55,7 Mds USD |
| Flux de trésorerie opérationnel | 32,0 Mds USD |
| FCF simple | environ -23,7 Mds USD |
| Dette totale | 129,5 Mds USD |

Même en présence d'une demande en IA, la capacité d'investissement des clients n'est pas infinie. Un CAPEX qui dépasse le flux de trésorerie dépend des obligations, du leasing, du financement de projet et des augmentations de capital. Si les taux d'intérêt, les spreads de crédit et le cours de l'action se dégradent simultanément, les plans à partir de 2027 pourraient être les premiers ajustés.

Le Take-or-Pay et le RPO ne constituent pas non plus une protection totale. Ils garantissent le chiffre d'affaires du client tout en alourdissant l'obligation de construction d'installations et la charge de financement du fournisseur.

<strong>Correction importante</strong> : le goulot d'étranglement du coût du capital ne constitue pas, à ce stade, un effondrement confirmé de la demande. Puisque TSMC et les hyperscalers continuent de relever leur CAPEX, il doit être classé comme <strong>un risque futur</strong>.

### 18. La croissance de l'usage de l'IA et la croissance du chiffre d'affaires en dollars des semi-conducteurs ne sont pas la même chose

La quantification, la sparsity, la réutilisation de cache, le speculative decoding, le CXL et le pooling mémoire, ainsi que l'optimisation logicielle, réduisent le coût matériel nécessaire « par unité d'intelligence ».

Si l'usage total croît plus vite que les gains d'efficacité, la demande en semi-conducteurs continue de croître. Mais si les deux vitesses se rapprochent, même si les tokens et le volume d'inférence explosent, <strong>le taux de croissance du chiffre d'affaires en dollars des fabricants de puces peut ralentir</strong>.

Les ASIC propriétaires constituent un risque direct de part de marché pour NVIDIA et les accélérateurs génériques. Pour la mémoire, le risque est moins direct, mais en optimisant la hiérarchie mémoire et la bande passante par client, ils peuvent réduire la quantité de HBM embarquée ou l'élasticité-prix.

### 19. La monétisation de l'IA peut ne pas suivre l'amortissement et les charges financières

Les GPU et les data centers génèrent du chiffre d'affaires <strong>après la mise en service</strong>, pas au moment de la commande. Si le raccordement électrique et l'installation des racks prennent du retard, le capital est engagé en premier et le revenu arrive plus tard.

Plus l'horloge de monétisation est en retard, plus les coûts suivants s'accumulent.

- Amortissement des nouvelles fabs, serveurs et installations électriques
- Intérêts sur obligations, leasing et financement de projet
- Obsolescence économique des anciens GPU et risque de dépréciation
- Affaiblissement du pouvoir de négociation dû à la concentration client
- Faible rotation des actifs liée à la capacité inutilisée

CoreWeave illustre le fait que même avec une forte demande en IA, le coût du capital peut détruire de la valeur actionnariale. \[Fait/Grade A : SEC\]

| Poste | T1 2026 |
|---|---:|
| Chiffre d'affaires | 2,078 Mds USD |
| Investissements (capex) | 7,695 Mds USD |
| Charges d'intérêts nettes | 536 M USD |
| Part des deux premiers clients dans le chiffre d'affaires | 65% |

Même un RPO élevé n'élimine pas le coût de financement élevé ni l'obligation de construction. Rien ne prouve encore que cette fragilité se propage à l'ensemble des hyperscalers. Mais si les acteurs périphériques à effet de levier, comme les néo-clouds et Oracle, vacillent en premier, la demande marginale de commandes de semi-conducteurs pourrait s'affaiblir.

### 20. Le capital chinois peut affaiblir la discipline d'offre du bas de cycle

L'introduction en bourse massive de CXMT n'est pas un événement qui crée immédiatement une compétitivité HBM. Le point le plus important est que <strong>l'entreprise s'est assuré le capital nécessaire pour poursuivre le développement technologique et l'expansion même en phase de bas de cycle</strong>.

Un fournisseur d'économie de marché réduit son CAPEX quand les prix et la rentabilité baissent. Un fournisseur dont la priorité est un objectif politique et la localisation nationale peut choisir d'étendre sa part de marché même à faible rentabilité. Si CXMT remplace le DRAM classique sur le marché intérieur chinois, les fournisseurs mondiaux pourraient allouer davantage de volumes aux marchés hors Chine, ce qui pèserait sur le plafond des prix.

### 21. Le chiffre d'affaires peut croître tandis que la marge incrémentale se retourne

En phase haussière, le prix, le taux d'utilisation et le mix HBM font tous monter la marge simultanément. En phase baissière, le même effet de levier joue en sens inverse.

- Hausse de l'amortissement des nouvelles fabs et des équipements
- Coûts initiaux de montée en cadence pour N2 et les fabs à l'étranger
- Réduction de la prime de prix du HBM sous l'effet de l'amélioration du rendement et de l'intensification de la concurrence
- Réduction des spécifications et résistance aux prix côté clients
- Augmentation de l'offre de DRAM et de NAND classiques
- Réduction de la scarcity rent liée à la résorption du goulot d'étranglement du packaging et des tests

La question la plus forte du camp baissier n'est pas « le chiffre d'affaires augmente-t-il », mais <strong>« chaque dollar de chiffre d'affaires supplémentaire génère-t-il le même résultat opérationnel qu'auparavant »</strong>. Si la marge opérationnelle incrémentale a franchi son pic, l'EPS peut continuer d'augmenter tandis que l'action subit un de-rating.

### 22. La rotation de leadership du marché suggère un ajustement des attentes propre aux semi-conducteurs

Au 16 juillet 2026, le SOXX avait chuté d'environ 19% depuis son pic de juin, et sa performance relative face au SPY sur les vingt dernières séances s'était nettement détériorée. Tandis que la tendance de court terme du QQQ et de l'indice des semi-conducteurs se détériorait, le Dow et le S&P 500 à pondération égale sont restés relativement solides. \[Grade B+ : recoupement Yahoo/TradingView\]

Cela ressemble davantage à une <strong>rotation sélective</strong>, où les capitaux se déplacent des positions surchargées en tech et semi-conducteurs vers la finance, la santé, l'énergie et les valeurs décotées, plutôt qu'à un effondrement généralisé de l'ensemble du marché américain.

Ce n'est pas la preuve que l'industrie est finie, mais c'est <strong>la preuve que le marché n'achète plus un bon récit industriel à n'importe quel prix</strong>. Si les semi-conducteurs ne montent plus malgré de bonnes nouvelles, tandis que d'autres secteurs se renforcent, le coût d'opportunité de détenir l'action augmente.

### 23. La concentration est un risque distinct de la thèse haussière

Même si la thèse centrale sur les semi-conducteurs se vérifie sur le long terme, une exposition concentrée sur la mémoire et l'infrastructure IA signifie qu'un seul facteur commun peut ébranler l'ensemble.

- Samsung Electronics, SK Hynix et Micron sont des titres distincts, mais ils restent liés par <strong>un facteur commun : le prix du DRAM et le CAPEX IA</strong>.
- L'optique et les équipements, matériaux et composants réagissent eux aussi conjointement au CAPEX des hyperscalers et aux mouvements risk-on/risk-off.
- Un manque de liquidités transforme une chute brutale en action forcée plutôt qu'en décision réfléchie.

Il faut donc séparer le principe consistant à « détenir longtemps de bonnes entreprises » du problème consistant à « détenir de manière excessive des titres fortement corrélés entre eux ». <strong>Une thèse haussière de long terme ne justifie pas la concentration.</strong>

---

## 24. Comment les bulls et les bears lisent-ils différemment les mêmes preuves

Ce tableau est la partie la plus pratique de cet article. Les deux camps lisent les mêmes nouvelles de façon diamétralement opposée, et la dernière colonne indique la véritable variable de discrimination.

| Preuve | Lecture haussière | Lecture baissière | Véritable variable de discrimination |
|---|---|---|---|
| CAPEX TSMC de 60-64 Mds USD | Vérification physique de la demande IA de long terme | Hausse de l'offre et de l'amortissement en 2027-2028 | Taux d'utilisation, prix, ROIC incrémental |
| Rush order sur le DRAM serveur | Pénurie et demande réelle fortes | Anticipation de la demande future | Stocks clients/canal et réorganisation des commandes |
| Amélioration du rendement HBM | Expansion des expéditions et baisse des coûts | Réduction de la prime et de la scarcity rent | L'amélioration des coûts est-elle plus rapide que la baisse des prix |
| Extension des LTA | Visibilité des volumes, plancher de profit plus élevé | Plafond de prix limité, transfert du risque de crédit client | Volume minimum, formule de prix, clauses d'annulation |
| Extension des ASIC propriétaires | Diffusion du TAM du silicium IA au-delà du GPU | Baisse de la part de marché et de l'ASP des accélérateurs génériques | Consommation totale de HBM, de wafers et de packaging |
| Retards d'électricité et de construction | Demande en attente et valeur d'actifs rares | Retard de chiffre d'affaires, capacité inutilisée, accumulation d'intérêts | Taux d'annulation, raccordement électrique réel, taux d'utilisation |
| IPO de CXMT | Substitution difficile du HBM à court terme | Poursuite de l'expansion généraliste même en bas de cycle | Mises en wafer, rendement DDR5, qualification client |
| RPO et Take-or-Pay élevés | Visibilité du chiffre d'affaires de long terme | Obligation de financement et de construction, concentration client | Marge contractuelle, garanties, clauses d'annulation/crédit |
| Explosion de l'usage de l'IA | Croissance structurelle de la demande totale en semi-conducteurs | Ralentissement de l'élasticité du chiffre d'affaires en dollars sous l'effet des gains d'efficacité | Taux de croissance de l'usage contre taux de baisse du coût par token |
| P/E bas de la mémoire | Les craintes de pic sont déjà intégrées | Pas bon marché si le dénominateur est un EPS de pic | Plancher de profit et durée du FCF |
| Chute brutale du SOXX | Divergence temporaire entre l'industrie et le cours de bourse | Disparition de l'utilité marginale des bonnes nouvelles | Révision de l'EPS et reconquête de la moyenne mobile à 50 jours |

---

## 25. Carte bull / bear par maillon de la chaîne de valeur

| Maillon de la chaîne de valeur | Logique haussière | Logique baissière | Observation clé |
|---|---|---|---|
| Leaders du HBM | Qualification client, écart technologique, mix élevé, pénurie d'offre | Concentration client, rattrapage des concurrents, normalisation de la prime | Rendement, prix, part de marché et volumes par client du HBM4 |
| DRAM et NAND classiques | Crowding-out par le HBM, demande serveur et eSSD, oligopole | Normalisation des achats anticipés, CXMT, expansion des capacités, élasticité-prix | Ampleur de la hausse des prix contractuels, stocks, expéditions en bits |
| Fonderie de pointe | Bénéficient tous : ASIC IA, CPU, GPU ; coût de changement élevé | Amortissement N2 et fabs à l'étranger, pouvoir de négociation via la conception propriétaire des clients | Taux d'utilisation, ASP des wafers, marge par nœud |
| Packaging avancé et OSAT | Pénurie type CoWoS, diffusion des chiplets et des grands packages | Atténuation du goulot d'étranglement après expansion des capacités, internalisation client | Carnet de commandes, livraison d'équipements, valeur par package |
| Fabless IA | Croissance du calcul IA et cycle produit | ASIC propriétaires, concentration client, échecs de conception | Design wins, fossé logiciel, conversion du chiffre d'affaires |
| Optique et réseau | Explosion de la bande passante scale-out/scale-across | Changement de standards, internalisation, concurrence, ajustement des stocks | Vitesse des ports, ASP, production en série par client |
| Équipements et tests | Bénéficiaire secondaire du CAPEX mémoire et fonderie | Pull-in des commandes, vide de CAPEX, book-to-bill au pic | Carnet de commandes, taux d'annulation, CAPEX client |
| Matériaux et substrats | Hautes spécifications, haute pureté, délai de qualification, diffusion de la BOM | Multi-sourcing client, expansion des capacités, variation des matières premières | Part du chiffre d'affaires liée à l'IA, répercussion des prix, qualification |
| Néo-clouds | Le calcul comme produit indépendant, rareté de l'électricité et du foncier | Effet de levier, valeur résiduelle des GPU, concentration client | Intérêts/EBITDA, taux d'utilisation, FCF après CAPEX |
| Hyperscalers | Croissance du chiffre d'affaires IA, de la publicité et du cloud, accès au capital | Dégradation du CAPEX, de l'amortissement et du FCF | Marge brute IA, FCF, dette et leasing |

<strong>Qualité relative</strong> : le maillon de la plus haute qualité est celui des leaders éprouvés du HBM, des procédés de pointe et du packaging avancé, mais les attentes y sont élevées et le risque de timing important. Les maillons les plus sensibles au cycle sont le DRAM/NAND classique et les équipements/tests. Les maillons présentant le plus grand risque financier sont les néo-clouds à effet de levier et les data centers à clientèle concentrée. Les maillons offrant le plus d'optionalité sont le redressement de la fonderie de Samsung et les nouveaux design wins en optique et matériaux, à traiter comme des options gratuites tant qu'aucune commande réelle n'est confirmée.

---

## 26. Les arguments faibles à écarter

Voici des arguments fréquemment utilisés des deux côtés, mais qui ne résistent pas à la vérification.

<strong>Bull faible</strong>

| Argument | Pourquoi il est faux |
|---|---|
| « L'IA a 4 ans, donc la mémoire ne peut que monter » | La demande finale de long terme et le surprofit des fournisseurs actuels ne sont pas la même chose |
| « Si le CAPEX augmente, tous les semi-conducteurs montent » | Le CAPEX inclut le terrain, les bâtiments, l'électricité et le leasing, et la capture de valeur diffère selon le produit et le client |
| « Un P/E bas est forcément bon marché » | Si le dénominateur est un EPS de pic, un P/E bas peut être normal |
| « Avec un LTA, le prix et le volume sont garantis » | Il faut vérifier les conditions contractuelles et le crédit du client |
| « CXMT est technologiquement en retard, on peut l'ignorer » | La menace à court terme sur le HBM est faible, mais l'enjeu est important pour le plafond de prix du DRAM classique |
| « Pour une bonne entreprise, le prix et le poids en portefeuille n'ont pas d'importance » | Même une qualité élevée n'élimine pas le risque de de-rating et de concentration |

<strong>Bear faible</strong>

| Argument | Pourquoi il est faux |
|---|---|
| « La demande en IA est fausse » | Cela contredit les commandes officielles, le CAPEX et la pénurie d'offre |
| « Le pic du T4 2026 signifie une baisse imminente des prix » | Le niveau des prix et le pic du taux de hausse des prix sont deux choses différentes |
| « CXMT va bientôt remplacer le HBM » | Cela ignore le temps nécessaire au rendement, au packaging et à la qualification client |
| « Les ASIC propriétaires suppriment la demande en mémoire » | Les ASIC consomment eux aussi des procédés de pointe et de la mémoire/réseau haute performance |
| « Le dead cross confirme la fin de l'industrie » | Les indicateurs techniques sont retardés et doivent être lus avec la tendance de long terme et l'EPS |
| « Le RPO et le Take-or-Pay ne sont que des illusions » | Une véritable visibilité contractuelle existe ; le problème réside dans la marge et la structure de financement |

---

## 27. Scénarios intégrés

Les probabilités ci-dessous ne sont pas des fréquences historiques, mais des estimations de jugement établies au 17 juillet 2026. \[Inférence : estimation de scénario\]

| Probabilité | Scénario | Industrie | Profits | Cours de bourse | Condition clé |
|---:|---|---|---|---|---|
| 25% | Reprise haussière structurelle / bear trap | Demande IA et goulots d'étranglement persistants | Révisions à la hausse de l'EPS et marges élevées maintenues | Reprise de la tendance après un retour du SOXX à 565-590 | Le taux d'utilisation, le chiffre d'affaires IA et le FCF suivent le CAPEX |
| <strong>55%</strong> | <strong>Fundamental bull / valuation bear</strong> | La demande croît | Les profits restent élevés mais l'ampleur des révisions ralentit | Longue consolidation, range latéral, rotation de leadership | La réaction de l'offre et l'amortissement limitent le multiple |
| 20% | Hard cycle bear | Retard des commandes, ralentissement de la demande | Baisse des prix et de l'EPS | Rupture du plus bas précédent et réduction de risque généralisée | Stocks d'achats anticipés + frein sur le CAPEX + hausse de l'offre |

Le scénario le plus probable est un <strong>mélange d'une industrie haussière et d'une action baissière sur le plan de la valorisation</strong>. Dans ce cas, la perte de l'investisseur provient moins d'un effondrement des profits que <strong>du temps et du coût d'opportunité</strong>.

---

## 28. Portes de bascule : qu'est-ce qui changerait le jugement

Un seul indicateur ne suffit pas. La direction ne change que lorsque <strong>au moins deux axes distincts</strong> sont confirmés.

<strong>Renforcement du bull (au moins deux axes)</strong>

1. Relèvement du CAPEX des hyperscalers accompagné d'une hausse conjointe de la marge brute IA/cloud
2. Amélioration du raccordement électrique, du taux d'utilisation des data centers et du taux d'usage des GPU
3. Poursuite des révisions à la hausse des prix HBM/DRAM et de l'EPS 12MF de Samsung Electronics, SK Hynix et Micron
4. Retour du SOXX à 565-590 et retournement de la force relative face au SPY

<strong>Maintien du valuation bear</strong>

- Les résultats sont bons mais l'ampleur des révisions à la hausse de l'EPS ralentit
- Le niveau des prix du DRAM reste élevé mais le taux de hausse ralentit
- Le CAPEX se maintient mais le FCF et les marges s'affaiblissent
- Le SOXX évolue latéralement dans la fourchette 470-565 tandis que d'autres secteurs affichent une force relative supérieure

<strong>Passage au hard bear (au moins deux axes)</strong>

1. Réduction du CAPEX des hyperscalers, retard de contrats, baisse du taux d'utilisation
2. Hausse des stocks clients/canal et ralentissement de l'ampleur de la hausse des prix contractuels du DRAM
3. Basculement à la baisse de l'EPS 12MF des trois fabricants de mémoire
4. Rupture du SOXX sous 520, échec de reconquête de 565, et contagion généralisée au marché

<strong>Affaiblissement du bear</strong>

- Après les rush orders, les stocks ne s'accumulent pas et s'écoulent en usage réel
- Le prix, le rendement et les volumes du HBM4 se maintiennent, et l'entrée de concurrents est absorbée par la croissance du marché
- La hausse du chiffre d'affaires et des flux de trésorerie IA dépasse l'amortissement et les charges d'intérêts
- Le CAPEX se maintient tandis que les spreads obligataires et la qualité de crédit restent stables

---

## 29. Registre des preuves : que croire, et avec quel degré de confiance

Voici, source par source, la fiabilité de cette analyse rendue publique. Le principe est de ne pas construire une confiance élevée sur des données de qualité faible.

| Affirmation | Source | Grade | Fiabilité | Limite |
|---|---|---|---|---|
| Relèvement de la croissance FY26 de TSMC, CAPEX 60-64 Mds USD | Documents de la conférence T2 2026, recoupement de plusieurs analyses | B | moyenne-haute | Accès direct partiellement limité au texte original de l'IR officielle |
| Contraintes mémoire chez Dell/HPE, réponse de Cisco | Documents JPM en quiet-period | C/B | moyenne | Vérification de canal par des brokers, pas de communication officielle |
| Rush order sur le DRAM serveur | Documents BofA | C/B | moyenne | Accès public limité au rapport original |
| CAPEX, flux de trésorerie opérationnel et dette d'Oracle | Formulaire 10-K SEC (FY2026) | <strong>A</strong> | haute | Cas plus fragile qu'un hyperscaler riche en liquidités |
| Achats anticipés et retards de contrats des clients d'IBM | Formulaire 8-K SEC (14-07-2026) | <strong>A</strong> | haute | Impossible de généraliser le cas unique d'IBM à l'ensemble de l'IT |
| Chiffre d'affaires, CAPEX, intérêts et concentration client de CoreWeave | Dépôts SEC (T1 2026) | <strong>A</strong> | haute | Cas fragile de néo-cloud, structure différente des géants de la tech |
| CAPEX cumulé 2027 de 801 Mds USD pour les trois entreprises (Citi) | Citi mega-cap preview | C/B | moyenne | Estimation agressive, pas une guidance d'entreprise |
| Pic du taux de hausse des prix mémoire au T4 2026 | Graphique et citation indirecte de Morgan Stanley | C | faible-moyenne | Définition du prix et hypothèses originales non vérifiées |
| Capacité de levée de fonds et d'expansion de l'offre de CXMT | Recoupement de l'annonce d'émission et des résultats de souscription | B | moyenne-haute | Décalage jusqu'à la capacité, au rendement et à la qualification client réels |
| Exportations coréennes de semi-conducteurs et proxy HBM | Chiffres provisoires du Service des douanes, 1-10 juillet | A/B | totaux : haute ; proxy : moyenne | Attribution par entreprise du HBM impossible |
| SOXX en baisse d'environ -19% depuis son pic | Recoupement Yahoo/TradingView | B+ | haute | Pas une valeur brute officielle de bourse |

<strong>Non vérifié</strong> : conditions économiques détaillées des LTA, prix/volumes/rendement du HBM4 par client, mises en wafer réelles de nouvelles capacités chez CXMT, rentabilité des charges de travail IA par hyperscaler individuel.

---

## 30. Ce qu'il faut vérifier ensuite

<strong>Résultats et communications officielles</strong>

1. Alphabet, Meta, Amazon : plus que le CAPEX, surveiller <strong>la marge brute IA, l'amortissement, le FCF, la nouvelle dette et le leasing</strong>
2. SK Hynix, Samsung Electronics, Micron : expéditions, rendement et prix du HBM4, croissance des bits du DRAM classique, structure des LTA, révisions de l'EPS FY2027
3. TSMC : dilution de marge liée à N2 et aux fabs à l'étranger, capacité de packaging avancé, vérification des commandes clients et taux d'utilisation réel
4. CXMT : allocation des fonds levés, commandes d'équipements pour les nouvelles fabs, rendement DDR5 et qualification client, calendrier HBM

<strong>Données mensuelles et hebdomadaires</strong>

1. Ampleur de la hausse des prix contractuels du DRAM et stocks clients/canal
2. Chiffres définitifs de fin de mois pour les exportations coréennes de semi-conducteurs et le proxy HBM
3. Delta des révisions de l'EPS 12MF des trois fabricants de mémoire
4. Zones 520, 565 et 590 du SOXX et force relative face au SPY
5. Spreads obligataires des hyperscalers et coût de financement des néo-clouds

---

## Conclusion : du scarcity cycle au capital-intensity cycle

L'argument le plus solide du camp haussier des semi-conducteurs est que la demande en IA est réelle, qu'elle se diffuse en goulots d'étranglement physiques dans la mémoire, les procédés de pointe, le packaging et le réseau, et que la valeur temporelle de l'offre ainsi que la qualification client créent des barrières à l'entrée.

L'argument le plus solide du camp baissier des semi-conducteurs est que cette demande réelle a déjà fait grimper brutalement les prix et le CAPEX, et qu'à l'étape suivante, la normalisation des achats anticipés, la réaction de l'offre, l'amortissement et le coût du capital pourraient simultanément peser sur les marges et les multiples.

En combinant les deux, une conclusion unique se dégage. <strong>L'industrie des semi-conducteurs pour l'IA n'est pas encore brisée. Mais le scarcity cycle est en train de basculer vers un capital-intensity cycle.</strong> La prochaine phase de hausse ne commencera pas avec une annonce de CAPEX, mais lorsque le raccordement électrique, le taux d'utilisation et les flux de trésorerie liés à l'IA rattraperont l'amortissement et le coût du capital.

L'attitude la plus rationnelle aujourd'hui consiste donc à ne pas abandonner la thèse industrielle de long terme, tout en <strong>gérant séparément le timing du cours de bourse et la concentration</strong>. Ne pas changer de direction sur un seul signal, et agir seulement lorsqu'au moins deux axes distincts sont confirmés. Selon les probabilités actuelles, la trajectoire centrale est celle où la croissance structurelle de l'industrie coexiste avec un long ajustement de valorisation de l'action : le <strong>Fundamental Bull / Valuation Bear</strong>.

---

_Cet article est une analyse qui synthétise les communications officielles (SEC, Service des douanes), les données de marché et les documents de scénarios de brokers, développe la thèse haussière et la thèse baissière des semi-conducteurs chacune sous sa forme la plus solide, puis les fait converger vers des variables observables. Le degré de fiabilité de chaque source est indiqué dans le corps du texte. Les chiffres de la conférence TSMC sont des valeurs recoupées avec un accès direct partiellement limité au texte original de l'IR officielle, et les estimations de CAPEX de Citi ainsi que le moment du pic selon Morgan Stanley ne constituent pas des guidances d'entreprise. Les probabilités de scénarios sont des estimations de jugement établies au moment de la rédaction, et non des fréquences historiques. Les titres mentionnés sont des exemples destinés à illustrer la structure de l'industrie et ne constituent pas une recommandation d'achat ou de vente d'un titre particulier. La décision d'investissement et sa responsabilité incombent à l'investisseur lui-même._

---

### Articles associés

- [La raison pour laquelle IBM a manqué ses résultats est une preuve de la vigueur de la mémoire](/fr/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/)
- [Le vide d'approvisionnement qui se propage au-delà du HBM : trois rapports de Hana Securities qui racontent une même histoire](/fr/post/memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14/)
- [Recherche approfondie sur l'offre et la demande de HBM à l'horizon 2030 : disséquer le modèle de demande de 26,7 EB face au calendrier des capacités](/fr/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
- [Qui paie le consensus semi-conducteurs de 2027](/fr/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/)
- [Samsung Electronics et SK Hynix sont-ils vraiment survendus au regard du consensus 2027](/fr/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/)

