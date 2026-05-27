---
title: "Marvell Q1 FY2027 et les semiconducteurs coréens : les goulots d'étranglement sont dans la connectique, les substrats et l'alimentation, pas seulement dans la HBM"
date: 2026-05-28T10:20:00+09:00
description: "Les résultats de Marvell au Q1 FY2027 ne se résument pas à un simple EPS beat. Ils révèlent que les goulots d'étranglement des datacenters IA se propagent vers les XPU custom, l'interconnexion optique, le networking scale-up, les FC-BGA, les MLCC, les condensateurs silicium et les sockets de test. Notre analyse des implications pour les semiconducteurs coréens couvre Samsung Electro-Mechanics, Samsung Electronics, SK Hynix, ISC, Leeno Industrial et TSE."
categories: ["Market-Outlook"]
tags:
  - "Marvell"
  - "MRVL"
  - "마벨"
  - "한국 반도체"
  - "삼성전기"
  - "009150"
  - "삼성전자"
  - "005930"
  - "SK하이닉스"
  - "000660"
  - "ISC"
  - "리노공업"
  - "티에스이"
  - "FC-BGA"
  - "MLCC"
  - "실리콘 커패시터"
  - "HBM"
  - "AI ASIC"
  - "AI 인프라"
slug: marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28
valley_cashtags:
  - Marvell
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - ISC
  - 리노공업
  - 티에스이
  - 대덕전자
  - 이수페타시스
  - 심텍
draft: false
---

> 📚 Contexte — article de suivi
> Cet article fait suite à [Marvell & Broadcom : examen des goulots d'étranglement des semiconducteurs coréens avant les résultats](/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/). La question posée en préambule était : « Le pari unique sur la HBM s'élargit-il vers les ASIC IA, le networking et la stabilisation de l'alimentation ? » Cet article répond à cette question à la lumière des résultats de Marvell au Q1 FY2027. Les hubs de référence sont le [Hub IA HBM](/page/korea-semiconductor-hbm-kospi-hub/), le [Hub substrats & PCB IA](/page/korea-ai-pcb-substrate-hub/) et le [Hub chaîne de valeur semiconducteurs coréens](/page/korea-semiconductor-equipment-ip-hub/).

## TL;DR

L'essentiel des résultats de Marvell au Q1 FY2027 n'est pas l'EPS beat. C'est que la société a révisé à la hausse sa trajectoire de croissance pour les datacenters IA sur FY2027–FY2028, en attribuant cette accélération aux <strong>XPU custom, à l'interconnexion optique, au switching Ethernet, au DCI, au networking scale-up/scale-across et à l'XPU attach</strong>.

La traduction pour les semiconducteurs coréens n'est pas « acheter davantage de HBM ». La HBM reste la tendance de fond, mais l'alpha incrémental confirmé par ces résultats se situe dans les <strong>goulots d'étranglement de connectique, de substrats, d'intégrité de l'alimentation et de test autour des GPU</strong>.

Ordre de priorité :

| Priorité | Implication Corée | Valeurs / secteur clé | Évaluation |
|---:|---|---|---|
| 1 | FC-BGA + MLCC serveurs IA + condensateurs silicium | Samsung Electro-Mechanics / SEMCO | Exposition la plus directe. Mais le re-rating est déjà en partie réalisé : vérifier les marges SiCap et FC-BGA |
| 2 | HBM4, SOCAMM2, eSSD, packaging avancé | Samsung Electronics, SK Hynix | Beta HBM maintenu. Nouvel alpha dans les memory attach et le packaging périphériques à la HBM |
| 3 | Sockets de test et interfaces pour ASIC/XPU custom | ISC, Leeno Industrial, TSE | Structure favorable, mais à conserver en watchlist avant confirmation du chiffre d'affaires direct |
| 4 | PCB/MLB haute vitesse pour le networking IA | ISU Petasys, Daeduck Electronics, Simtech, etc. | Sélectivité requise. « PCB IA » n'est pas synonyme d'exposition uniforme |

Sur Marvell lui-même, le verdict est <strong>HOLD / Buy watch</strong>. Cours de référence : $198,70 ; objectif à 12 mois : $225, soit un potentiel d'environ +13 %. La trajectoire de croissance est solide, mais le cours intègre déjà des attentes élevées. Du côté coréen, ce qui importe davantage que Marvell, c'est <strong>vers quels maillons se propagent les goulots d'étranglement identifiés par Marvell</strong>.

---

## 1. Ce qu'il faut vraiment retenir des résultats de Marvell

Marvell a publié ses résultats du Q1 FY2027 après la clôture américaine du 27 mai 2026. Les chiffres officiels sont les suivants. ([Marvell][1])

| Indicateur | Q1 FY2027 | Interprétation |
|---|---:|---|
| Chiffre d'affaires | <strong>$2,418 Md</strong> | +28 % en glissement annuel, +$18 M vs. point médian du guidance |
| BPA GAAP | <strong>$0,04</strong> | Affecté par la comptabilisation des acquisitions Celestial AI & XConn |
| BPA non-GAAP | <strong>$0,80</strong> | Conforme au consensus |
| Marge brute GAAP | <strong>52,1 %</strong> | Amélioration annuelle |
| Marge brute non-GAAP | <strong>58,9 %</strong> | Maintien dans la fourchette haute malgré l'enrichissement du mix IA |
| Flux de trésorerie opérationnel | <strong>$638,8 M</strong> | Record historique |
| Guidance CA Q2 | <strong>$2,70 Md ±5 %</strong> | Fourchette $2,565 Md – $2,835 Md |
| Guidance BPA non-GAAP Q2 | <strong>$0,93 ±$0,05</strong> | Base de rentabilité pour le prochain trimestre |

Les résultats en eux-mêmes s'apparentent à un « léger beat / EPS inline ». Ce qui importe pour le cours et pour les implications coréennes, ce n'est pas quelques centimes de BPA au Q1, mais la <strong>trajectoire de chiffre d'affaires FY2027–FY2028 communiquée par la direction</strong>.

Selon les transcripts de tiers, la direction a évoqué un chiffre d'affaires d'environ $11,5 Md pour FY2027 et d'environ $16,5 Md pour FY2028, et a relevé ses prévisions de croissance pour l'interconnexion FY2027 de près de 50 % à plus de 70 %. Ces éléments ne proviennent pas d'une retranscription IR officielle, mais leur orientation est cohérente avec les termes du communiqué de presse officiel. Celui-ci cite explicitement la croissance de l'optique 800G/1,6T, des switches Ethernet 51,2T, de l'optique scale-up pour NPO/CPO, des modules DCI, des XPU custom et de l'XPU-attach. ([Marvell][1], [StockAnalysis transcript][2])

En une phrase :

> Marvell a confirmé en chiffres que le capex des datacenters IA migre de l'achat de GPU vers l'infrastructure d'interconnexion des clusters.

---

## 2. Le cœur du sujet : l'architecture d'interconnexion, pas seulement SOCAMM

Pour un investisseur coréen, le risque de lecture erronée le plus courant serait de réduire cet appel de résultats au seul thème SOCAMM. SOCAMM est important, mais il n'est pas au centre du message de Marvell.

Les axes prioritaires sont les suivants :

| Axe clé Marvell | Pourquoi c'est important | Traduction semiconducteurs coréens |
|---|---|---|
| XPU custom / ASIC custom | Signal que les hyperscalers diversifient leur silicon IA au-delà des GPU NVIDIA | Diversification de la base clients HBM, substrats de packaging, sockets de test |
| Interconnexion optique | 800G/1,6T, DCI, optique scale-up comme goulot d'étranglement de l'extension des clusters IA | PCB haute vitesse/communications optiques à sélectionner ; FC-BGA et stabilisation de l'alimentation SEMCO structurels |
| Switching Ethernet | Roadmap 51,2T, 100T, 200T = hausse du dollar content des semiconducteurs de networking IA | FC-BGA pour ASIC réseau, cartes haute vitesse, inspection et test |
| XPU attach | CXL, NIC, memory attach, KV cache pour l'inférence | Samsung Electronics SOCAMM2, eSSD, DRAM serveur ; options IP mémoire de type OpenEdges |
| NVLink Fusion | Le silicon custom coexiste dans l'écosystème NVIDIA | Au-delà de l'opposition « NVIDIA vs ASIC », c'est une expansion de la chaîne d'approvisionnement |

L'annonce NVIDIA–Marvell va dans le même sens. NVIDIA investit 2 milliards de dollars dans Marvell ; Marvell fournit des XPU custom compatibles NVLink Fusion et du networking scale-up. Les deux sociétés collaborent également sur la photonique silicium et l'AI-RAN. ([Marvell NVIDIA][3])

Le message est simple :

> Un datacenter IA n'est pas un serveur GPU isolé, mais un système où GPU, XPU custom, HBM, optique, switch, retimer, CXL, NIC, FC-BGA et MLCC forment un tout indissociable.

L'investissement dans les semiconducteurs coréens doit donc évoluer de « faut-il se concentrer uniquement sur les grandes capitalisations mémoire ? » vers « quels goulots d'étranglement se traduisent en chiffres concrets sous la couche mémoire ? ».

---

## 3. Implication coréenne n°1 : Samsung Electro-Mechanics / SEMCO

La traduction la plus directe des résultats de Marvell pour une valeur coréenne est Samsung Electro-Mechanics (SEMCO). Trois raisons l'expliquent.

Premièrement, les XPU custom, les switches Ethernet, l'interconnexion optique et l'XPU attach mis en avant par Marvell requièrent tous des packages et des substrats haute vitesse et haute densité. Cela se traduit directement par une demande de FC-BGA.

Deuxièmement, les serveurs IA absorbent des courants élevés sous de basses tensions. Pour atténuer les fluctuations de tension autour des packages GPU, HBM et XPU, des composants de stabilisation de l'alimentation — MLCC et condensateurs silicium — sont indispensables.

Troisièmement, SEMCO dispose déjà de ces deux briques. La société a annoncé qu'au Q1 2026, son chiffre d'affaires Package Solution s'établissait à 725,0 milliards KRW, en hausse de 45 % en glissement annuel et de 12 % en séquentiel, avec une expansion des livraisons de substrats haute valeur ajoutée pour accélérateurs IA, CPU serveur et applications réseau. ([Samsung Electro-Mechanics Q1][4])

Par ailleurs, SEMCO a signé un contrat de fourniture de condensateurs silicium d'un montant de 1 557,0 milliards KRW, couvrant la période du 1er janvier 2027 au 31 décembre 2028. Ces composants améliorent la stabilité de l'alimentation à l'intérieur des packages GPU et HBM destinés aux serveurs IA. ([Samsung Electro-Mechanics SiCap][5])

Le cadre d'analyse de SEMCO évolue ainsi :

| Ancien prisme | Prisme actuel |
|---|---|
| Valeur cyclique sur MLCC smartphones & modules caméra | Plateforme d'intégrité de l'alimentation IA (packaging) + FC-BGA |
| Reprise de la demande mobile | Demande accélérateurs IA, CPU serveur, ASIC réseau |
| Cycle MLCC généraliste | Mix MLCC haute capacité / faible résistance / ultramince / haute fiabilité + SiCap |
| Comparaison avec Ibiden ou Murata | Comparaison hybride MLCC + FC-BGA + SiCap |

Cette conclusion ne signifie pas « acheter à n'importe quel prix ». Le contrat SiCap, une capitalisation boursière déjà significative et le re-rating IA sont largement intégrés. Les variables à surveiller sont donc non pas le momentum de cours, mais <strong>la marge brute, l'OPM du segment Package Solution, le rendement en production SiCap et la diversification des clients</strong>.

---

## 4. Samsung Electronics & SK Hynix : beta HBM maintenu, nouvel alpha en périphérie

Les résultats de Marvell ne sont pas négatifs pour la HBM — c'est même l'inverse. Même si les XPU custom et le networking scale-up progressent, le dollar content mémoire ne diminue pas. Plus les modèles d'IA évoluent vers l'IA agentique, le raisonnement et le mixture-of-experts, plus les besoins en déplacement de données et en mémoire augmentent.

Du point de vue de l'investisseur, « la HBM est favorable » est déjà la thèse centrale. Ce que l'appel de résultats Marvell ajoute de nouveau est le suivant :

1. La base de clients HBM s'élargit d'une structure monolithique centrée sur les GPU NVIDIA aux XPU custom des hyperscalers.
2. L'XPU attach, couplé au CXL, aux NIC, au memory attach et au KV cache, a des répercussions sur la DRAM serveur, le SOCAMM et l'eSSD.
3. À mesure que les clusters IA s'agrandissent, la valeur du packaging, des substrats et de la stabilisation de l'alimentation reliant mémoire et puces de calcul augmente.

Samsung Electronics dispose ici d'options multiples. La HBM4, la HBM4E, le SOCAMM2, le SSD PM1763, le foundry et le packaging avancé s'inscrivent tous dans la même infrastructure IA. Samsung Electronics a présenté la HBM4E, le SOCAMM2 et le PM1763 comme une gamme de produits IA en partenariat avec NVIDIA lors du GTC 2026. ([Samsung Semiconductor][6])

SK Hynix conserve le beta HBM le plus pur. Mais à l'aune des seuls résultats de Marvell, le nouvel alpha est plus important du côté de <strong>Samsung Electro-Mechanics, des sockets de test et des substrats haute vitesse</strong> qui progressent parallèlement à la HBM. SK Hynix reste la valeur phare, mais c'est aussi celle sur laquelle le marché a déjà le plus les yeux rivés.

---

## 5. Sockets de test : bénéficiaires discrets de la prolifération des ASIC custom

Si le chiffre d'affaires custom est important dans l'appel de résultats Marvell, ce n'est pas simplement une question de volumes. L'enjeu est celui des <strong>SKU et des cycles de qualification</strong>.

Dans un monde où les accélérateurs IA seraient standardisés autour d'un seul GPU NVIDIA, la demande en composants de test serait relativement prévisible. À l'inverse, la multiplication des XPU custom par hyperscaler, de l'XPU attach, du CXL, des NIC, des ASIC switch et des DPU fragmente davantage les conditions de test et la conception des sockets.

Dans ce contexte, les sockets de test et les composants d'interface peuvent bénéficier simultanément de trois tendances :

| Variable | Direction | Raison |
|---|---|---|
| Volumes | Hausse | Multiplication des SKU ASIC custom, ASIC réseau et memory attach |
| ASP | Hausse | Difficulté croissante du test (nombre de broches élevé, signaux haute vitesse, haute puissance) |
| Fréquence de remplacement | Structurelle | Renouvellement générationnel et qualification répétée par client |

En Corée, ISC, Leeno Industrial et TSE sont à surveiller. Il convient cependant de rester prudent : il est difficile, sur la seule base des informations publiques, de confirmer que les fabricants coréens de sockets de test sont directement intégrés dans la chaîne Marvell ou dans celle des XPU custom d'hyperscalers spécifiques. Il s'agit donc pour l'instant d'un <strong>« potentiel de bénéfice »</strong> et non d'un <strong>« mapping client confirmé »</strong>.

Les indicateurs à surveiller dans les publications trimestrielles sont : le chiffre d'affaires IA/HPC logic, le nombre de nouveaux clients, le mix de sockets haute valeur ajoutée et la défense des OPM.

---

## 6. Le PCB généraliste n'est pas un achat indifférencié

Les résultats de Marvell sont favorables au networking IA et à l'interconnexion optique. Mais conclure « le networking IA est bon → tous les PCB sont bons » serait une erreur.

Le bénéfice se concentre sur les acteurs répondant aux critères suivants :

1. Capacité à traiter des matériaux à faibles pertes pour les signaux haute vitesse.
2. Exposition aux MLB multicouches haute densité ou aux substrats de packaging haute valeur ajoutée.
3. Qualification chez des clients en serveurs IA ou équipements réseau.
4. Confirmation non pas d'une hausse des volumes, mais d'une hausse de l'ASP, du nombre de couches et de la complexité des matériaux.

La multiplication des GPU et des XPU ne se traduit pas mécaniquement par une augmentation proportionnelle des volumes de substrats. Dans les architectures où plusieurs puces coexistent de manière plus dense sur un seul package ou une seule carte haute performance, ce qui compte davantage que le volume est <strong>la surface du substrat, le nombre de couches, la complexité des matériaux et le rendement</strong>.

Regrouper ISU Petasys, Daeduck Electronics, Simtech, TLB et Korea Circuit dans un même panier est donc inexact. L'implication réelle des résultats Marvell est : « sélectionner les acteurs disposant de substrats haute couche pour le réseau et de matériaux adaptés aux signaux haute vitesse ».

---

## 7. Valorisation de MRVL : une bonne entreprise ne suffit pas — le prix compte aussi

Le jugement sur Marvell est HOLD / Buy watch.

| Indicateur | Valeur |
|---|---:|
| Cours de référence | $198,70, clôture du 27 mai 2026 |
| Objectif à 12 mois | $225 |
| Potentiel de hausse | \~+13,2 % |
| Méthode de valorisation | EV/Sales FY2028E |
| Conclusion | Trajectoire de croissance rehaussée, mais valorisation déjà élevée |

La formule du scénario de base est la suivante :

```text
Objectif de cours = (CA FY2028E × EV/Sales cible − dette nette) ÷ nombre d'actions dilué
```

Hypothèses : CA FY2028E de $16,5 Md, EV/Sales cible de 12,5x, dette nette d'environ $1,117 Md, nombre d'actions dilué de 915 M. Le calcul donne un objectif d'environ $224, arrondi à $225.

Pour que Marvell bénéficie d'un re-rating comparable à Broadcom, trois conditions doivent être réunies :

1. Le chiffre d'affaires du silicon custom doit se confirmer comme un programme récurrent, et non comme un événement lié à un client unique.
2. La marge brute non-GAAP doit se maintenir dans la fourchette 58–59 % malgré la montée en puissance de l'interconnexion et du switching.
3. Les prépaiements engagés pour sécuriser la chaîne d'approvisionnement doivent se traduire en montée en charge du chiffre d'affaires et en flux de trésorerie disponible.

En résumé, Marvell est devenue une excellente entreprise, mais la question de savoir si le cours est un bon point d'entrée est distincte.

---

## 8. Prochains points de contrôle

| Point de contrôle | Signal fort | Signal faible |
|---|---|---|
| CA Q2 FY2027 | Proche ou au-dessus du plafond de $2,835 Md | En dessous du point médian de $2,70 Md |
| CA Data Center | Croissance séquentielle dans les high-teens ou au-dessus | Ralentissement de la croissance séquentielle |
| Marge brute non-GAAP | ≥59,25 % ou défense du haut de fourchette | <58,25 % |
| Interconnexion | Maintien ou relèvement du +70 % FY2027 | Ralentissement du ramp 800G/1,6T |
| XPU custom | Visibilité ×2 FY2028 et $10 Md+ FY2029 | Retards dans les ramps par client |
| Switching scale-up | Concrétisation de la production en série chez un client Tier 1 | Nombreux engagements mais pas encore de chiffre d'affaires |
| Implications Corée | Confirmation des chiffres Package Solution, SiCap et FC-BGA de SEMCO | Thème fort mais marges et prises de commandes absentes |

Les variables à surveiller par valeur coréenne sont plus simples :

| Valeur / secteur | À surveiller |
|---|---|
| Samsung Electro-Mechanics / SEMCO | Croissance Package Solution, CA FC-BGA pour réseau IA, rendement et marges SiCap en production, nouveaux contrats long terme |
| Samsung Electronics | Qualification client HBM4, expéditions effectives SOCAMM2, prix et volumes eSSD, clients foundry/packaging |
| SK Hynix | Ramp HBM4, diversification clients, risque de surcapacité 2027 |
| ISC, Leeno Industrial, TSE | CA sockets de test IA logic, nouveaux clients, mix haute valeur ajoutée, OPM |
| PCB / MLB | Qualification clients réseau IA, hausse de l'ASP, matériaux à faibles pertes et augmentation du nombre de couches |

---

## 9. Conditions d'invalidation de la thèse

Les conditions qui affaibliraient cette thèse sont clairement définies :

1. Le CA Q2 de Marvell passe en dessous du point médian de $2,70 Md et la croissance Data Center ralentit.
2. La marge brute non-GAAP tombe en dessous de 58,25 %, confirmant que le mix custom/interconnexion dilue les marges.
3. La prévision de CA FY2028 à $16,5 Md est revue à la baisse.
4. Les XPU custom et l'XPU attach sont bloqués par des retards de calendrier propres à certains clients.
5. Le SiCap de SEMCO se révèle être un chiffre d'affaires à faible marge, ou la croissance FC-BGA ralentit.
6. Les résultats des fabricants de sockets de test n'affichent pas de hausse du CA IA/HPC logic.
7. Les délais d'approvisionnement HBM se raccourcissent et des signaux de surcapacité apparaissent pour 2027.

---

## Conclusion

Les résultats de Marvell au Q1 FY2027 ne sont pas un signal « achetez uniquement de la HBM » pour les semiconducteurs coréens. Le message est plus précis :

> Plus les clusters IA grossissent, plus les goulots d'étranglement descendent du GPU vers la connectique, les substrats, la stabilisation de l'alimentation et le test.

Dans cette perspective, la valeur coréenne la plus directement exposée est Samsung Electro-Mechanics / SEMCO, dont les MLCC, FC-BGA et condensateurs silicium s'inscrivent tous dans le même goulot d'étranglement de packaging IA. Samsung Electronics et SK Hynix restent centraux en tant que références HBM, mais l'alpha incrémental révélé par les résultats Marvell est davantage en périphérie de la HBM. ISC, Leeno Industrial et TSE sont des candidats au bénéfice secondaire de la prolifération des ASIC custom, mais doivent rester en watchlist avant confirmation du chiffre d'affaires direct.

La conclusion n'est pas un achat indifférencié. Même une bonne thèse reste un simple thème si elle ne se traduit pas en chiffres. Ce qu'il faut surveiller dans les semiconducteurs coréens après ce trimestre, plus que les cours, c'est le <strong>chiffre d'affaires Package Solution, les marges SiCap, le CA des sockets de test IA logic et l'ASP des substrats haute vitesse</strong>.

---

## Fait / Inférence / Spéculation / Information non disponible

### [Fait]

- Le CA de Marvell au Q1 FY2027 s'est établi à $2,418 Md, soit +28 % en glissement annuel, avec un guidance CA Q2 de $2,70 Md ±5 %. ([Marvell][1])
- La marge brute non-GAAP de Marvell au Q1 était de 58,9 % ; le guidance de marge brute non-GAAP Q2 est de 58,25–59,25 %. ([Marvell][1])
- Marvell a cité comme moteurs de croissance l'optique scale-out 800G/1,6T, les switches Ethernet 51,2T, l'optique scale-up, les modules DCI, les XPU custom et l'XPU-attach. ([Marvell][1])
- NVIDIA investit 2 milliards de dollars dans Marvell ; Marvell fournit des XPU custom compatibles NVLink Fusion et du networking scale-up. ([Marvell NVIDIA][3])
- Le CA Package Solution de Samsung Electro-Mechanics au Q1 2026 s'est établi à 725,0 milliards KRW, soit +45 % en glissement annuel et +12 % en séquentiel. ([Samsung Electro-Mechanics Q1][4])
- Samsung Electro-Mechanics a signé un contrat de fourniture de condensateurs silicium de 1 557,0 milliards KRW pour la période du 1er janvier 2027 au 31 décembre 2028. ([Samsung Electro-Mechanics SiCap][5])

### [Inférence]

- Il est raisonnable de transposer les axes de croissance de Marvell aux valeurs coréennes dans l'ordre suivant : FC-BGA/MLCC/SiCap de SEMCO, memory attach de Samsung Electronics et SK Hynix, sockets de test, puis substrats haute vitesse.
- La HBM reste la tendance de fond, mais l'alpha incrémental mis en évidence par ces résultats est plus important dans les couches connectique, packaging, intégrité de l'alimentation et test que chez les grandes capitalisations mémoire HBM.
- Le re-rating de SEMCO doit être analysé non comme une reprise MLCC, mais comme une transition vers une plateforme passive/substrat pour l'infrastructure IA.

### [Spéculation]

- Le marché suppose que le client du contrat SiCap de SEMCO pourrait être lié à un hyperscaler nord-américain ou à une chaîne d'approvisionnement d'accélérateurs IA, mais la contrepartie n'a pas été divulguée.
- Il n'est pas possible, sur la seule base des informations publiques, de confirmer que les fabricants coréens de sockets de test sont directement intégrés dans les programmes XPU custom de Marvell ou de ses clients.
- L'AI-RAN pourrait à terme créer des opportunités dans les semiconducteurs RF et réseau coréens, mais il est trop tôt pour en faire un catalyseur de résultats à court terme en 2026.

### [Information non disponible]

- Confirmation directe de l'approvisionnement coréen pour chaque programme XPU custom, optique et switch de Marvell.
- Nom du client, marges par produit et rythme mensuel de montée en charge du contrat SiCap de SEMCO.
- Part du CA par client IA logic pour ISC, Leeno Industrial et TSE.
- PER NTM en temps réel, EV/EBITDA et taux de révision à la hausse du BPA consensus pour les valeurs PCB/substrats coréens en mai 2026.

---

## Sources

[1]: https://investor.marvell.com/news-events/press-releases/detail/1023/marvell-technology-inc-reports-first-quarter-of-fiscal-year-2027-financial-results "Marvell Technology, Inc. Reports First Quarter of Fiscal Year 2027 Financial Results"
[2]: https://stockanalysis.com/stocks/mrvl/transcripts/583849-q1-2027/ "Marvell Technology Q1 2027 Earnings Call Transcript & Audio"
[3]: https://investor.marvell.com/news-events/press-releases/detail/1019/nvidia-ai-ecosystem-expands-as-marvell-joins-forces-through-nvlink-fusion "NVIDIA AI Ecosystem Expands as Marvell Joins Forces Through NVLink Fusion"
[4]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Announces Q1 2026 Business Performance"
[5]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
[6]: https://semiconductor.samsung.com/news-events/news/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026/ "Samsung Unveils HBM4E at NVIDIA GTC 2026"

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
