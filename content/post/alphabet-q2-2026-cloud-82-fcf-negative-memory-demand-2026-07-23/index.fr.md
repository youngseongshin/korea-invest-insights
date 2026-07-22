---
title: "Alphabet au T2 : Cloud +82% clôt le débat sur la demande, le FCF négatif ouvre celui du cash"
slug: "alphabet-q2-2026-cloud-82-fcf-negative-memory-demand-2026-07-23"
date: 2026-07-23T11:00:00+09:00
description: "Le T2 d'Alphabet a fortement réduit la probabilité d'une falaise de demande IA après 2028 : Cloud a crû de 82%, le backlog atteint 514 Mds USD et les clients consomment 50% au-delà de leurs engagements. Le même rapport livre le premier FCF trimestriel négatif de l'histoire du groupe, une guidance CAPEX 2026 relevée jusqu'à 205 Mds et la location de compute auprès de SpaceX pour environ 920 M USD par mois faute de capacité. Nous lisons la fin du débat sur la demande et le début du débat sur le cash, le traduisons en HBM, DRAM serveur et eSSD, et préparons les grilles de lecture Microsoft et Amazon de fin juillet."
categories: ["Exclusive Analysis", "Company-Analysis", "Market-Outlook"]
tags: ["Alphabet", "Google Cloud", "CAPEX IA", "TPU", "HBM", "DRAM serveur", "Mémoire IA", "FCF", "Backlog", "Résultats Big Tech", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte : dans [Qui brûle tous ces tokens ?](/fr/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/), nous écrivions que des chiffres avaient commencé à se rattacher à la demande finale, le dernier maillon faible du débat sur le CAPEX IA, et nous avions renvoyé le verdict à la saison des résultats autour du 30 juillet. La première copie notée est arrivée plus tôt que prévu. Alphabet a publié ses résultats du deuxième trimestre dans la nuit du 23 juillet, heure de Corée. Cet article synthétise en un seul texte deux notes d'analyse qui décortiquent ces mêmes résultats sous des angles différents. Pour résumer d'emblée la conclusion : le débat sur la demande est en pratique clos, et la scène du débat s'est déplacée vers le flux de trésorerie et le rendement du capital.

## TL;DR

- Le chiffre d'affaires Cloud atteint 24,8 Mds USD, <strong>+82%</strong> (consensus +64%), portant le taux de croissance à cinq trimestres consécutifs d'accélération : 32%, 34%, 48%, 63% et 82%. Le backlog est passé de 462 Mds USD à <strong>514 Mds USD</strong>, en hausse nette de 52 Mds USD alors même que la reconnaissance de chiffre d'affaires s'accélère.
- La qualité de la demande compte davantage. Les clients Cloud existants dépensent en moyenne <strong>plus de 50% au-delà</strong> de leur engagement initial, et le débit de l'API des modèles Gemini a atteint 22 Mds de tokens par minute, en hausse de 37,5% sur un seul trimestre. Faute de capacité, Alphabet a commencé, dès juin, à louer du compute IA <strong>auprès de SpaceX pour environ 920 M USD par mois</strong>. Une scène inédite : un hyperscaler devenu acheteur net de compute.
- Au verso du même rapport, le FCF trimestriel est tombé à <strong>-5,9 Mds USD, le premier trimestre négatif de l'histoire du groupe</strong>. Le CAPEX de 44,9 Mds USD a dépassé le flux de trésorerie d'exploitation de 39,1 Mds USD, et la guidance CAPEX 2026 a été relevée de 180-190 Mds USD à <strong>195-205 Mds USD</strong>, avec une nouvelle hausse marquée annoncée pour 2027.
- Le jugement se divise en trois volets. La probabilité d'une falaise de demande IA après 2028 a encore baissé. Le retournement du FCF d'Alphabet est repoussé, non plus 2027, mais la fenêtre 2028-2029. Pour la mémoire, la vigueur de la demande en volume est reconfirmée, mais la persistance des prix et de la marge au pic reste une question distincte.
- Nous maintenons les probabilités du scénario de demande 45/35/20. Une nouvelle preuve empirique est toutefois venue étayer le scénario haussier à 35%, et ce rapport affaiblit le ralentissement précoce du CAPEX de la Big Tech qui constituait l'hypothèse centrale du scénario baissier à 20%. Le prochain relevé de notes viendra de Microsoft (30 juillet, heure de Corée) et d'Amazon (31 juillet).

<div class="thesis-callout">
<div class="thesis-callout__label">Thèse principale</div>

Cloud +82% et le premier FCF trimestriel négatif de l'histoire sont les deux faces d'un même rapport. À la question de savoir si la demande est réelle, Alphabet a répondu par une consommation qui dépasse les engagements et par la location, à prix fort, des serveurs d'un tiers. En échange, la facture pour capter cette demande est arrivée plus tôt que prévu. Le critère de notation du marché est passé de l'existence de la demande au rendement du cash après amortissement, et pour l'investisseur en mémoire, ce rapport est un renfort pour les volumes, pas une garantie pour les marges.

</div>

## 1. D'abord les chiffres : ce qui a été publié

| Poste | T2 2026 réel | Base de comparaison | Verdict |
|---|---|---|---|
| Chiffre d'affaires du groupe | 119,8 Mds USD, +24% | Consensus environ 116,9 Mds USD | Au-dessus |
| Chiffre d'affaires Google Cloud | 24,8 Mds USD, +82% | Consensus 22,4 Mds USD, +64% | Largement au-dessus |
| Résultat opérationnel Cloud | 8,8 Mds USD (marge 35,6%) | Année précédente 2,8 Mds USD (marge 20,7%) | Amélioration |
| Chiffre d'affaires Search | 63,3 Mds USD, +17% | Consensus 63,4 Mds USD | Conforme |
| Résultat opérationnel du groupe | 40,8 Mds USD, +30% (marge 34,0%) | Marge sous le consensus | Mitigé |
| BPA ajusté | environ 2,85 USD | Consensus environ 2,89 USD | Légèrement en dessous |
| Flux de trésorerie d'exploitation | 39,1 Mds USD | CAPEX 44,9 Mds USD | Inversion |
| FCF trimestriel | -5,9 Mds USD | Trimestre précédent 10,1 Mds USD | Premier négatif de l'histoire |
| Backlog Cloud | 514 Mds USD | Trimestre précédent 462 Mds USD | +52 Mds USD |
| Guidance CAPEX 2026 | 195-205 Mds USD | Précédemment 180-190 Mds USD | Relevée |

[Fait : publication Alphabet · conférence de résultats]

Les chiffres GAAP comportent un effet d'optique. Le BPA GAAP publié est de 9,11 USD et le résultat net de 112,1 Mds USD, en hausse de +298% sur un an, mais ce chiffre intègre une plus-value latente d'environ 99 Mds USD (avant impôt, soit environ 6,26 USD par action après impôt) sur des participations non cotées comme Anthropic et SpaceX. En retirant cette ligne sans rapport avec l'exploitation, le BPA réel ressort à environ 2,85 USD, légèrement sous les attentes du marché. Le chiffre d'affaires et le Cloud ont largement battu les attentes, mais la qualité du résultat n'était pas aussi solide que le chiffre en surface. [Fait : recalcul à partir de la publication]

## 2. Le débat sur la demande : pourquoi il est en pratique clos

Le précédent article pointait le maillon faible de la demande finale et citait les 3 millions d'utilisateurs supplémentaires de Codex en trois jours comme première preuve empirique. Le rapport d'Alphabet y ajoute quatre nouvelles preuves.

<strong>L'usage devance les contrats.</strong> Le débit de l'API des modèles Gemini est passé de 16 Mds à 22 Mds de tokens par minute, en hausse de 37,5% sur un seul trimestre, et le nombre de développeurs mensuels a dépassé 9 millions. Les clients Cloud existants dépensent en moyenne plus de 50% au-delà de leur engagement initial, et l'écart de dépassement s'est creusé par rapport au trimestre précédent. Le rythme d'acquisition de nouveaux clients a doublé sur un an, et le volume de transactions sur la marketplace a été multiplié par sept. [Fait : lettre du CEO · conférence de résultats] L'hypothèse selon laquelle la demande ne reposerait que sur les contrats de long terme d'une poignée de laboratoires frontières est incompatible avec des données où la consommation réelle après signature dépasse l'engagement.

<strong>La base de clients s'est élargie.</strong> Au-delà de la demande liée au développement de modèles, comme le pré-entraînement à grande échelle de Gemini 4, cinq filières ont été présentées simultanément : l'inférence d'entreprise dans la finance, la pharmacie, la distribution, les télécoms et l'industrie, les charges BigQuery et sécurité, les services grand public comme le mode IA de la recherche et l'application Gemini, et enfin la vente externe de systèmes TPU livrés directement dans les data centers des clients. Environ 90% des entreprises du Fortune 100 utilisent Gemini Enterprise, et les clients Cloud traitant plus de 1 000 milliards de tokens par an sont désormais 500, contre plus de 2 000 pour ceux dépassant 100 milliards. [Fait : lettre du CEO]

<strong>L'offre continue de plafonner la croissance.</strong> Le CFO a explicitement confirmé que l'environnement restait contraint côté offre. Pour combler les manques à court terme, le groupe loue à prix élevé de la capacité de data centers tiers, et il a expliqué qu'accepter environ six mois d'inefficacité valait la peine pour capter de grands clients. C'est dans ce prolongement qu'est tombée la plus grosse nouvelle de cette conférence : depuis juin, Alphabet a signé un contrat pour louer du compute IA auprès de SpaceX, pour environ 920 M USD par mois, soit environ 11 Mds USD en rythme annualisé. [Fait : conférence de résultats · presse] Que l'entreprise qui calcule le plus vite au monde loue les serveurs d'un tiers à prix fort constitue une preuve comportementale directement opposée à l'hypothèse d'une demande surestimée.

<strong>Le backlog a grossi même pendant sa propre reconnaissance en chiffre d'affaires.</strong> Alors que le chiffre d'affaires Cloud du deuxième trimestre a progressé d'environ 23,8% par rapport au trimestre précédent, signe que de gros contrats se convertissent rapidement en chiffre d'affaires, le solde du backlog s'est encore renforcé de 52 Mds USD. Le backlog actuel représente environ 5,2 fois le chiffre d'affaires Cloud annualisé du deuxième trimestre, et la société a indiqué que plus de la moitié serait reconnue sous 24 mois. [Fait : publication · conférence de résultats] C'est une preuve solide de visibilité jusqu'en 2027. La concentration par client et la ventilation annuelle de la reconnaissance après 2028 ne sont toutefois pas divulguées. [Non vérifié : détail du backlog non divulgué]

L'objection tirée de l'efficacité a elle aussi perdu de sa force ce trimestre. Le coût par réponse du mode IA est tombé à son niveau le plus bas depuis le lancement, alors que le nombre d'utilisateurs et le volume de requêtes ont progressé encore plus vite. Le mode IA compte 1 Md d'utilisateurs mensuels, et l'application Gemini 950 M de MAU. La relation selon laquelle la hausse de l'usage dépasse la baisse du coût unitaire se vérifie donc aussi à l'échelle d'Alphabet, dans le même sens que l'effet Jevons observé avec Codex. [Inférence : relation efficacité-usage]

## 3. Le débat sur le cash : la facture est arrivée plus tôt que prévu

À l'opposé de la demande, ce que ce rapport a confirmé, c'est l'ampleur et la durée de la dépense.

Le CAPEX du deuxième trimestre, à 44,9 Mds USD, a doublé sur un an et dépassé le flux de trésorerie d'exploitation de 39,1 Mds USD ; l'intensité capitalistique trimestrielle (CAPEX/flux de trésorerie d'exploitation) atteint environ 115%. L'arithmétique est lourde elle aussi. Le CAPEX du premier semestre s'élevant à environ 80,6 Mds USD, atteindre le haut de la guidance annuelle à 205 Mds USD suppose de dépenser, au second semestre, une moyenne trimestrielle de 57,2-62,2 Mds USD, soit 27-38% de plus qu'au deuxième trimestre. Une reprise significative du FCF au second semestre 2026 et en 2027 est peu probable. [Inférence : arithmétique propre]

Un indice sur 2027 est également apparu. Le CFO a maintenu sa perspective d'une forte hausse du CAPEX en 2027, et le consensus de marché se situe autour de 257 Mds USD. Le passage de 205 à 257 Mds USD représente un taux de croissance d'environ +25%. On reste sur une trajectoire de ralentissement, d'environ +76% cette année à environ +25% l'an prochain, et non pas encore sur un scénario de réaccélération vers les 300 Mds USD. [Fait : conférence de résultats · consensus] Cette distinction compte. Sur une trajectoire de ralentissement, l'ossature de la logique de retournement du FCF tient ; en cas de réaccélération, cette ossature s'effondre.

Calculer une sensibilité pour 2028 permet de clarifier le critère de jugement. Le point de départ est le flux de trésorerie d'exploitation cumulé sur les douze derniers mois (TTM), actuellement à 185,7 Mds USD.

| Hypothèse de CAPEX 2028 | OCF requis pour un FCF nul | Croissance annualisée d'OCF requise | OCF requis pour un FCF de 50 Mds USD | Croissance requise |
|---|---|---|---|---|
| 200 Mds USD | 200 Mds USD | environ 3,8% | 250 Mds USD | environ 16,0% |
| 230 Mds USD | 230 Mds USD | environ 11,3% | 280 Mds USD | environ 22,8% |
| 250 Mds USD | 250 Mds USD | environ 16,0% | 300 Mds USD | environ 27,1% |

[Inférence : sensibilité propre, pas une guidance de l'entreprise]

Si le CAPEX se stabilise autour de 200 Mds USD en 2028, la reprise du FCF n'a rien d'insurmontable. S'il continue de grimper vers 230-250 Mds USD, il faudrait que le flux de trésorerie d'exploitation combiné du Cloud et de Search progresse de plus de 20% par an pour retrouver un FCF de niveau historique. Ce n'est pas un chiffre impossible si le Cloud maintient sa croissance de +82% et sa marge de 35,6% pendant un certain temps, mais l'amortissement, l'électricité, les loyers de capacité externe et un mix de ventes de matériel TPU à marge plus faible tirent dans le sens inverse.

Le basculement du régime d'allocation du capital s'est lui aussi officialisé ce trimestre. Avec 242,5 Mds USD de cash et de titres négociables et 185,7 Mds USD de flux de trésorerie d'exploitation TTM, la solvabilité d'Alphabet n'est pas en soi un sujet de débat. Mais au deuxième trimestre, le groupe a levé environ 30,5 Mds USD en actions ordinaires, environ 19,1 Mds USD en actions préférentielles convertibles et environ 21,1 Mds USD en dette nette, sans aucun rachat d'actions. La dette est passée d'environ 16 Mds USD à environ 100 Mds USD en douze mois. [Fait : publication] Une entreprise qui finançait à la fois son CAPEX et ses rachats d'actions par son flux de trésorerie d'exploitation est devenue une entreprise qui arrête les rachats pour financer son CAPEX et mobilise même la dette et les fonds propres. Ce n'est pas un signal de risque de liquidité mais un signal de changement de régime d'allocation du capital, et le fait que le poids du financement repose davantage sur les actionnaires que sur le marché obligataire est un motif de réconfort du point de vue crédit.

## 4. Notation des trois questions

Face à ce rapport, voici comment se notent les trois questions.

<strong>La demande IA se maintiendra-t-elle après 2028 ? La probabilité d'une falaise a encore baissé.</strong> La demande se propage de l'entraînement vers l'inférence, les données, la sécurité et les usages d'entreprise, la consommation réelle dépasse les engagements, l'usage croît plus vite que les gains d'efficacité, l'essentiel du chiffre d'affaires de vente externe de TPU sera reconnu en 2027, et l'offre reste assez insuffisante pour exiger une forte hausse du CAPEX même en 2027. Il est plus exact de voir 2028 non pas comme le moment où la demande s'arrête, mais comme celui où la nouvelle capacité d'offre entre pleinement en service et passe à l'épreuve des faits.

<strong>Le FCF d'Alphabet va-t-il se retourner ? C'est possible, mais l'échéance a reculé.</strong> Le croisement du FCF trimestriel est arrivé plus tôt que prévu initialement (début 2027), mais même en fixant de façon optimiste le flux de trésorerie d'exploitation 2027 à 230-240 Mds USD, un CAPEX de 257 Mds USD ramène le FCF annuel sous zéro. Le retour au positif suppose 2028, et seulement si la croissance du CAPEX 2028 retombe à un chiffre unique. Une forte réaccélération du FCF reste un scénario conditionnel pour la fenêtre 2028-2029.

<strong>Cela se traduit-il par des achats de mémoire durables ? Franchement positif pour les volumes, neutre pour les prix et les marges.</strong> Nous décortiquons ce point dans la section suivante.

## 5. Traduction en mémoire : un renfort pour les volumes, pas une garantie pour les marges

Au deuxième trimestre, environ 60% du CAPEX d'infrastructure technique est allé aux serveurs, et 40% aux data centers et au réseau. L'investissement serveur englobe à la fois TPU, GPU, CPU, HBM, DRAM serveur, SSD et semi-conducteurs réseau. [Fait : conférence de résultats]

Les éléments qui soutiennent la demande de HBM sont nets : la nouvelle génération de TPU et l'introduction du NVIDIA Vera Rubin, le pré-entraînement à grande échelle de Gemini 4, la hausse des volumes d'inférence d'entreprise, une architecture réseau de nouvelle génération reliant 1 M d'accélérateurs, et la vente externe de systèmes TPU dont l'essentiel sera reconnu à partir de 2027. Point important : même si le TPU maison remplace en partie les GPU NVIDIA, la demande de HBM ne disparaît pas, elle change seulement de canal d'achat, passant de la chaîne d'approvisionnement GPU à celle des systèmes TPU. En y ajoutant la location de compute auprès de tiers, le canal de demande de HBM et de DRAM serveur s'est élargi à trois filières : les data centers propriétaires, la vente externe de TPU et le compute loué. [Inférence : décomposition des canaux de demande]

L'argumentaire pour la DRAM serveur et l'eSSD s'est lui aussi étoffé avec ce rapport. Les agents IA ne se contentent pas des accélérateurs : ils font tourner le prétraitement, la gestion d'état, la sécurité et l'orchestration sur des serveurs CPU. Alphabet a mis en avant à la fois le CPU Axion et la hausse des charges de données et de sécurité. Le chiffre de 500 clients traitant plus de 1 000 milliards de tokens par an montre que la demande de stockage, qui s'étend aux logs, aux checkpoints, aux index de recherche et aux bases de données vectorielles, ne se limite pas à l'entraînement. [Fait : lettre du CEO] Le regain de tension sur la DRAM serveur observé dans l'article précédent (prévision de +13-18% sur les prix contractuels du T3, délais de livraison de 40 semaines) voit ainsi sa toile de fond côté demande reconfirmée par les résultats de la Big Tech.

Cela dit, on ne doit pas relever les estimations de bénéfices 2028 des fabricants de mémoire sur la seule base de ce rapport. À mesure que les achats d'équipement s'envolent, la capacité d'offre de mémoire augmente elle aussi sur 2027-2029. L'expansion des puces maison réduit le pouvoir de fixation des prix de NVIDIA au niveau système, le coût d'inférence par réponse baisse rapidement, et si Alphabet commence à resserrer l'efficacité de son CAPEX, la pression à la baisse sur les prix des composants redescendra le long de la chaîne d'approvisionnement. Les prix élevés du HBM4 et de la génération suivante intègrent une prime de rareté de début de génération et de rendement, ce qui n'en fait pas une valeur permanente. En synthèse, voici ce que cela donne.

| Poste | Jugement avant résultats | Jugement après résultats |
|---|---|---|
| Demande de bits d'accélérateurs IA · HBM | Élevée | Très élevée |
| Demande de DRAM serveur · eSSD | Moyenne-haute | Élevée |
| Packaging avancé · réseau | Élevée | Très élevée |
| Falaise de demande 2028 | Probabilité faible | Probabilité encore plus faible |
| Persistance de l'ASP mémoire | Incertaine | Incertaine |
| Persistance de la marge au pic mémoire | Faible | Faible |
| Reprise anticipée du FCF de la Big Tech | Moyenne | Plus faible |
| Rendement marginal du capital du CAPEX | Non démontré | Partiellement démontré, vérification en cours |

[Inférence : jugement de synthèse]

Le risque pour les semi-conducteurs en 2028 n'est pas l'annulation de commandes, mais la normalisation de l'ASP et de la marge. Cela reste cohérent avec le scénario de demande 45/35/20. Ce rapport ajoute une preuve empirique de plus à l'argumentaire du scénario haussier à 35%, et affaiblit le ralentissement précoce du CAPEX de la Big Tech qui constituait l'hypothèse du scénario baissier à 20%. Les probabilités elles-mêmes seront mises à jour après vérification auprès de Microsoft et d'Amazon. Du point de vue de Samsung Electronics et de SK Hynix, c'est un rapport qui améliore le contexte de demande pour les négociations de prix du HBM 2027, qui débuteront au quatrième trimestre.

## 6. Réaction du cours, et la divergence de jugement entre les deux notes

La réaction du marché résume bien la nature de cette phase. Le titre a d'abord chuté d'environ 2% en après-Bourse dès l'annonce, puis s'est brièvement redressé jusqu'à une légère hausse, avant de rechuter lorsque le relèvement du CAPEX est tombé pendant la conférence, portant le repli jusqu'à une fourchette de 3-5%. Au matin du 23 juillet, heure de Corée, le cours se situait autour de 342 USD, soit environ -1,5% par rapport à la clôture de la veille, à environ 347 USD. [Fait : données de marché] Sur un marché où battre le consensus est devenu la norme, c'est le CAPEX qui détermine la réaction : la règle de 2026 s'est vérifiée pour la cinquième fois. À l'inverse, que le repli soit resté aussi contenu face à une croissance de +82% est aussi un signal que le marché continue d'absorber la dépense tant que la croissance se prouve.

Les deux notes qui ont servi de matière à cette synthèse tirent des conclusions différentes des mêmes faits. L'une a choisi de rester en suspens, au nom d'un critère de preuve structurelle. L'expression exacte n'est pas que le rendement du capital est démontré, mais qu'il est le plus susceptible de l'être, et elle a réservé son calcul d'objectif de cours face au FCF négatif, aux levées de capital et à l'annonce d'une nouvelle hausse en 2027. L'autre a maintenu un achat fondé sur le prix d'entrée. En posant l'hypothèse d'un cours déjà corrigé de 15% depuis son pic, elle propose un objectif à 12 mois de 430 USD, calculé en appliquant un multiple de 28-29x à un BPA 2027E hors plus-values d'environ 15 USD, avec une clause de révision : le calcul sera refait si le CAPEX 2027 se précise à l'approche des 300 Mds USD. [Fait : conclusions des deux notes]

La différence entre les deux jugements ne tient pas à la perception des faits, mais à l'horizon et au critère retenus. Le point de vue structurel fait peser la charge de la preuve sur l'entreprise jusqu'à ce que le rendement du cash après amortissement soit confirmé en chiffres, tandis que le point de vue prix calcule dans quelle mesure ce risque est déjà intégré dans un cours déjà corrigé. Conformément au principe de ce blog, nous ne recommandons aucune direction particulière et présentons les deux cadres côte à côte, mais le dénominateur commun est clair. Dans un cas comme dans l'autre, la prochaine variable de jugement n'est plus la demande, mais le cash.

## 7. Grille de lecture : les deux prochaines semaines vont trancher

Voici les cases que ce rapport a remplies et celles qu'il vient d'ouvrir.

- La part d'Alphabet dans le commentaire CAPEX de la Big Tech est désormais confirmée à la hausse. Restent la première guidance FY27 de Microsoft (conférence dans la nuit du 30 juillet, heure de Corée) et le taux de croissance d'AWS chez Amazon (nuit du 31 juillet). Si Alphabet a clos le débat sur la demande, ces deux publications trancheront le débat sur la marge et le FCF.
- L'indicateur de confirmation à la hausse est de savoir si la croissance du Cloud se maintient au-dessus de 50% sur les 2 à 4 prochains trimestres, et si la marge tient au-dessus de 30%. Si, une fois les contraintes d'offre levées, la croissance retombe sous 30%, il faudra recalculer la probabilité d'une surestimation de la demande.
- Nous surveillons si le backlog continue de croître net même après la reconnaissance de chiffre d'affaires. Une combinaison de baisse du backlog ou d'un simple allongement de la durée des contrats serait un signal de détérioration de la qualité des contrats.
- Le trimestre où le taux de croissance du flux de trésorerie d'exploitation TTM dépasse celui du CAPEX marquera le point de départ du retournement du FCF. À l'inverse, si le CAPEX 2028 dépasse 250 Mds USD sans que le flux de trésorerie d'exploitation suive, nous qualifierons cela de dégradation structurelle du FCF.
- Les points à vérifier côté efficacité du capital sont les suivants : de nouvelles levées d'actions ou de dette à grande échelle se poursuivent-elles, la location externe de type SpaceX se réduit-elle en 2027-2028, et la vente externe de TPU se convertit-elle en consommation Cloud récurrente.
- Le critère de discrimination côté mémoire ne change pas : le prix contractuel de la DRAM, et sa confirmation pour le T3 lors des conférences de résultats de Samsung Electronics et SK Hynix autour du 30 juillet.

---

Les titres mentionnés dans le texte sont des exemples destinés à l'analyse et ne constituent pas une recommandation d'achat ou de vente d'un titre particulier. La décision d'investissement et ses conséquences relèvent de la seule responsabilité de l'investisseur. Alphabet n'a fourni aucune guidance de CAPEX ni de chiffre d'affaires Cloud pour 2028, la répartition par client du backlog de 514 Mds USD, sa ventilation annuelle de reconnaissance et ses conditions d'annulation ne sont pas divulguées, et les volumes d'achat de HBM, de DRAM et de NAND ainsi que leur répartition par fournisseur ne font pas non plus l'objet d'une publication. La sensibilité du FCF 2028 et l'arithmétique du CAPEX du second semestre sont des estimations propres prenant pour point de départ les publications actuelles, non des prévisions de l'entreprise. L'ampleur avant impôt de la plus-value latente sur les participations non cotées et son effet après impôt par action, recalculés à partir des publications, peuvent comporter des écarts d'arrondi. L'objectif de cours de 430 USD est le calcul d'une des deux notes soumises à cette synthèse, et non un objectif de ce blog. Les cours et cotations sont établis à la date du matin du 23 juillet 2026, heure de Corée.

### Articles liés

- [Qui brûle tous ces tokens ? La carte clients de NVIDIA, l'IA souveraine et les 9 millions de Codex commencent à répondre](/fr/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/)
- [La demande de mémoire pour l'IA dépassera-t-elle les attentes ? Lire les probabilités de surcroissance via les scénarios de demande et la carte de l'offre](/fr/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/)
- [Deux mois de déclarations du président de SK Hynix Chey Tae-won : l'entreprise se renforce, le pic de marge est passé](/fr/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/)
- [Le vrai débat des semi-conducteurs : quatre horloges physiques et une horloge boursière](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
