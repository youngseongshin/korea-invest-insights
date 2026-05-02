---
title: "Liste des clients de Samsung Foundry 2026 — Qui utilise Samsung Foundry ? Tesla, Tenstorrent, Qualcomm, Google, Ambarella, et l'ensemble des clients confirmés"
slug: samsung-foundry-customer-list-tesla-tenstorrent-2026-05-03
date: 2026-05-03T11:00:00+09:00
description: "Les clients de Samsung Foundry en 2026 — confirmés via des appels de résultats, des communications clients et des reportages sur la chaîne d'approvisionnement — comprennent Tesla (HW5/successeur de Dojo sur SF2), Tenstorrent (Wormhole/Blackhole sur SF4X), Qualcomm (certains modems et variantes Snapdragon), Google (successeurs de TPU et SoC Pixel sur SF4LPP/SF3), Ambarella (CV3-AD ADAS pour l'automobile), et le propre System LSI de Samsung (Exynos). En toute honnêteté, Samsung Foundry reste un #2 crédible face à TSMC sur les nœuds avancés, avec une clientèle fortement orientée vers les accélérateurs IA, les SoC automobile/ADAS, et les clients prêts à accepter une prime de risque sur les rendements en échange de la disponibilité de capacité ou d'une logique d'approvisionnement souverain."
categories: ["Sector-Deep-Dive", "Korea Market", "AI Infrastructure"]
tags:
  - "Samsung Foundry"
  - "005930"
  - "Samsung Electronics"
  - "Tesla"
  - "Tenstorrent"
  - "Qualcomm"
  - "Google"
  - "Ambarella"
  - "TSMC"
  - "puce IA"
  - "fonderie"
  - "semiconducteur"
  - "SF2"
  - "SF3"
  - "SF4"
  - "actions coréennes"
---

> 🔗 **À lire également** : [Parts de marché HBM de SK hynix](/post/sk-hynix-hbm-market-share-ai-memory-demand-2026/) · [OpenEdges Technology — alpha IP datacenter LPDDR6/5X](/post/openedges-lpddr-datacenter-ip-alpha-thesis-2026-04-30/) · [Big Tech 1T26 → Samsung Electronics vs Samsung Electro-Mechanics](/post/bigtech-1q26-samsung-electronics-vs-electro-mechanics-2026-04-30/)

*Cet article répond directement à la question « Qui utilise Samsung Foundry en 2026 ? » — et explique pourquoi chaque client est là, sur quel nœud il opère, et ce que la composition de la clientèle révèle sur le positionnement de Samsung Foundry face à TSMC.*

---

## Synthèse

**La réponse courte.** La liste confirmée des clients de Samsung Foundry pour 2026, pondérée par pertinence économique, comprend :

- **Tesla** — client multi-générationnel (HW3 → travaux préparatoires HW4), avec le SoC de prochaine génération pour véhicule autonome et les accélérateurs liés à Dojo sur les nœuds avancés de Samsung (SF4 / SF3 / SF2, selon la presse spécialisée).
- **Tenstorrent** — les familles d'accélérateurs IA Wormhole et Blackhole sur les nœuds avancés de Samsung Foundry, dont le SF4X de classe 4 nm. La maison ASIC dirigée par Jim Keller est un partenaire public de Samsung Foundry.
- **Qualcomm** — approvisionnement dual-source entre Samsung Foundry et TSMC ; certains modems (5G/6G) et variantes Snapdragon sélectionnées ont historiquement été fabriqués sur les nœuds avancés de Samsung.
- **Google** — SoC Pixel Tensor (classe G3/G4) sur les nœuds 4 nm de Samsung ; une partie de la production liée aux TPU a historiquement utilisé la capacité Samsung, TSMC étant également présent dans les dernières générations de TPU.
- **Ambarella** — SoC automobiles ADAS CV3-AD sur le nœud 5 nm de Samsung.
- **Samsung System LSI** — Exynos 2400 / Exynos Auto / logique capteur d'image : la charge de travail captive qui ancre la capacité de Samsung Foundry.
- **Travaux IA adjacents à NVIDIA et startups** — certaines puces accélératrices et de réseau ont historiquement utilisé la capacité Samsung.
- **Fabless coréens et japonais** — Rebellions, FuriosaAI (prochain Renegade), clients du segment DB HiTek, et maisons AI-ASIC asiatiques utilisent les lignes de production 4 / 5 / 8 / 12 nm de Samsung Foundry.

**Lecture honnête.** Samsung Foundry en 2026 n'est **pas** l'égal de TSMC sur le front de pointe — TSMC remporte toujours les travaux d'accélérateurs IA les plus en pointe et les plus volumiques (NVIDIA, AMD, Apple silicon). Ce qu'est Samsung Foundry en 2026, c'est un **#2 crédible** avec une clientèle fortement orientée vers (a) les accélérateurs IA qui ont besoin de capacité hors TSMC, (b) les SoC automobile/ADAS, (c) les clients prêts à payer une prime de risque sur les rendements pour des raisons de capacité, d'approvisionnement souverain, ou de prix. La composition de la clientèle est exactement celle qu'on attendrait d'une « fonderie challenger dotée d'une vraie capacité sur nœuds avancés, mais avec des questions de rendement persistantes ».

---

## 1. Pourquoi « Qui utilise Samsung Foundry ? » est la bonne question

Le positionnement de Samsung Foundry a fait l'objet d'une couverture presse contradictoire, plus que presque tout autre sujet dans les semiconducteurs. Une semaine, le titre annonce « Samsung remporte Tesla / Qualcomm / Google » — la suivante, « Samsung perd [X] au profit de TSMC ».

Pour couper à travers ce bruit, il faut poser une question différente. Non pas « Samsung Foundry est-il en train de gagner ? » — cette question ne peut pas être tranchée nettement, car la réponse dépend du modèle retenu. La vraie question est : **qui utilise concrètement Samsung Foundry en 2026, et que révèle la composition de la clientèle ?**

La composition de la clientèle est la seule lecture honnête du positionnement d'une fonderie, parce que :

1. **L'allocation de capacité est observable.** Les communications clients, les références dans les appels de résultats, et les reportages presse sur la chaîne d'approvisionnement révèlent qui grave réellement des wafers dans quel fab.
2. **La composition de la clientèle encode les arbitrages entre rendement, capacité et prix.** Une fonderie qui remporte un client sur un nœud avancé soit a résolu le problème de rendement, soit dispose d'un avantage capacitaire que TSMC ne peut égaler, soit pratique une politique de prix agressive. La composition de la clientèle vous dit lequel des trois.
3. **La composition prédit l'utilisation 2027–2028.** Le portefeuille clients de Samsung Foundry en 2026 définit en grande partie ses volumes de production 2027. Les clients visibles aujourd'hui *sont* les deux prochaines années de revenus.

---

## 2. La clientèle confirmée — Qui, où, et pourquoi

### 2.1 Tesla — L'ancre multi-générationnelle

**Situation.** Tesla est client de Samsung Foundry sur plusieurs générations. La puce FSD Hardware 3 (HW3) a été produite sur le nœud 14 nm de Samsung. La puce Hardware 4 (HW4) est passée au nœud 7 nm de Samsung. Le Hardware 5 / SoC de prochaine génération pour véhicule autonome est associé, dans la presse spécialisée, aux nœuds SF4 et à la feuille de route aval de Samsung (SF3 / SF2), avec une utilisation continue de la capacité Samsung à travers 2026 et au-delà.

**Pourquoi Samsung.** Tesla a systématiquement opéré avec un approvisionnement dual-source en wafers — TSMC pour la production GPU/accélérateur IA de classe Dojo, Samsung pour le SoC FSD/HW. L'engagement Samsung reflète probablement une combinaison de (a) disponibilité de capacité que TSMC ne pouvait pas offrir aux volumes de Tesla, (b) levier tarifaire extrait de la position challenger de Samsung, et (c) la continuité de la plateforme FSD construite dans la relation depuis HW3.

**Ce que cela signifie pour Samsung.** Tesla est ce qui s'approche le plus d'un « client trophée » pour Samsung Foundry — une grande entreprise cotée aux États-Unis dont les véhicules dépendent de silicium gravé par Samsung. Perdre Tesla au profit de TSMC serait l'un des signaux les plus négatifs possible ; garder Tesla jusqu'à HW5 est l'un des signaux positifs les plus forts.

### 2.2 Tenstorrent — Le pari Samsung public de Jim Keller

**Situation.** L'accélérateur IA Wormhole de Tenstorrent et la prochaine génération Blackhole sont publiquement déclarés en production chez Samsung Foundry. Jim Keller, PDG de Tenstorrent, a donné plusieurs interviews publiques évoquant le partenariat avec Samsung Foundry, avec un déplacement de la production sur nœuds avancés vers le SF4X 4 nm de Samsung.

**Pourquoi Samsung.** Le positionnement de Tenstorrent est celui d'« un fournisseur d'accélérateurs IA qui parie contre la pile NVIDIA/CUDA ». Choisir Samsung plutôt que TSMC pour la production sur nœuds avancés est cohérent avec ce positionnement à contre-courant. La disponibilité de capacité Samsung et un modèle d'engagement plus flexible que le cadre priorité-client-tier-1 de TSMC seraient des facteurs déterminants.

**Ce que cela signifie pour Samsung.** Tenstorrent est la validation publique la plus explicite que Samsung Foundry ait dans le secteur des accélérateurs IA. À mesure que les expéditions de Tenstorrent augmentent, l'exposition de Samsung Foundry aux accélérateurs IA non-NVIDIA s'accroît — une diversification significative au-delà du « Samsung Foundry = charge de travail captive de Samsung System LSI ».

### 2.3 Qualcomm — Dual-source entre Samsung et TSMC

**Situation.** Les SoC Snapdragon flagship de Qualcomm ont historiquement été répartis entre Samsung Foundry et TSMC selon les générations. Le Snapdragon 8 Gen 1 a été un gain notable pour Samsung sur son nœud 4 nm ; les flagships suivants (Snapdragon 8 Gen 2, Gen 3, Snapdragon 8 Elite) sont passés principalement à TSMC. Néanmoins, Qualcomm continue de produire certains modems et variantes Snapdragon de gamme inférieure sur la capacité Samsung Foundry.

**Pourquoi Samsung.** Le dual-source protège Qualcomm contre les contraintes de capacité et le levier tarifaire de TSMC. La relation Samsung donne à Qualcomm une position de négociation crédible vis-à-vis de TSMC. Pour Samsung Foundry, cette relation — même à volume sous-flagship — est un client de référence important qui signale que « les nœuds de Samsung sont à l'état de l'art en production commerciale ».

**Ce que cela signifie pour Samsung.** Le volume Qualcomm chez Samsung Foundry n'est pas le travail flagship Snapdragon très médiatisé ; c'est la production régulière qui remplit la capacité intermédiaire. À surveiller : un retour du Snapdragon 8 Gen 5 ou d'un futur flagship vers Samsung Foundry — ce serait un signal positif majeur.

### 2.4 Google — SoC Pixel Tensor et travaux TPU sélectifs

**Situation.** Les SoC Google Pixel Tensor (G1, G2, G3, G4) ont été produits chez Samsung Foundry, en s'appuyant sur la propriété intellectuelle de conception dérivée de l'Exynos de Samsung System LSI et la production sur nœuds 5 nm / 4 nm. Une partie de la production de TPU (anciennes générations, capacité supplémentaire) a historiquement utilisé Samsung ; les dernières générations de TPU sont principalement chez TSMC.

**Pourquoi Samsung.** La lignée de conception du Pixel Tensor issue de la propriété intellectuelle de Samsung System LSI fait de Samsung Foundry le partenaire de production naturel. Pour les travaux TPU, Samsung a été un complément de capacité plutôt qu'un partenaire principal.

**Ce que cela signifie pour Samsung.** Le volume Google Pixel n'est pas énorme en termes absolus de fonderie, mais la relation est de premier plan et crée une demande entraînée pour le nœud 4 nm de Samsung. Le facteur de basculement majeur serait que les TPU de prochaine génération reviennent de façon significative sur la capacité Samsung.

### 2.5 Ambarella — SoC ADAS pour l'automobile

**Situation.** La famille CV3-AD d'Ambarella — l'accélérateur IA automobile phare de la société pour les applications ADAS et de conduite autonome — est produite sur le nœud 5 nm de Samsung Foundry. Ambarella a publiquement désigné Samsung Foundry comme son partenaire 5 nm.

**Pourquoi Samsung.** Les clients automobiles valorisent (a) la continuité de l'approvisionnement — l'engagement de Samsung dans une production automobile de long terme, (b) la disponibilité de capacité — la capacité automobile 5 nm de TSMC est fortement surchargée par Apple/AMD/NVIDIA, (c) la certification qualité automobile de Samsung.

**Ce que cela signifie pour Samsung.** Ambarella est le client de référence le plus clair que Samsung ait sur le « 5 nm automobile ». À mesure que l'ADAS / L2+ / L3 d'autonomie se déploie chez les constructeurs mondiaux, la demande sur la capacité avancée automobile de Samsung augmente structurellement.

### 2.6 Samsung System LSI — L'ancre de la charge de travail captive

**Situation.** La propre division System LSI de Samsung — SoC mobiles Exynos, Exynos Auto pour l'automobile, logique capteur d'image, circuits intégrés modem — est le plus grand client captif de Samsung Foundry. Exynos 2400 (série Galaxy S24), Exynos Auto V920 (partenariats Hyundai Pleos / Kia), et la logique capteur d'image sont tous sur les nœuds avancés de Samsung Foundry.

**Pourquoi Samsung.** Captif — par définition.

**Ce que cela signifie pour Samsung.** C'est le plancher. Même si tous les clients externes disparaissaient demain, Samsung System LSI maintiendrait les fabs de nœuds avancés de Samsung Foundry en activité. La charge de travail captive est également la source d'une grande partie du développement de propriété intellectuelle de Samsung Foundry, de la courbe d'apprentissage des rendements, et de la maturation des processus. L'interprétation honnête : les gains de clients externes représentent **une hausse au-dessus** de la base captive.

### 2.7 La couche fabless coréenne et asiatique

**Situation.** Une longue liste de clients fabless coréens et asiatiques utilise Samsung Foundry sur les nœuds 4 / 5 / 8 / 12 / 14 nm. Les clients confirmés et publiquement évoqués incluent :

- **Rebellions** — startup coréenne d'accélérateurs IA (REBEL-Quad / accélérateur de prochaine génération sur les nœuds avancés de Samsung).
- **FuriosaAI** — puce Renegade sur le 5 nm de Samsung Foundry ; prochaines générations en développement.
- **DeepX** — startup coréenne d'IA en périphérie, Samsung Foundry.
- **OpenEdges Technology** — IP de sous-système mémoire coréen (PHY/contrôleur LPDDR6/5X silicon-proven sur Samsung SF5A ; en développement sur 4 nm Samsung).
- **Divers fabless japonais** — charges de travail automobile, capteur d'image, et IA.

**Pourquoi Samsung.** Proximité géographique, support IR/ingénierie en coréen et japonais, écosystème de partenaires IP Samsung SAFE (Cadence, Synopsys, OpenEdges en tant que partenaire sous-licence), et accessibilité tarifaire pour les clients non-tier-1.

**Ce que cela signifie pour Samsung.** Cette couche est peu glamour mais durable. C'est elle qui rend viable l'utilisation des nœuds 4 / 5 / 8 nm de Samsung Foundry en volume. C'est aussi la couche qui bénéficie le plus directement d'une vague de startups AI ASIC originaires de Corée ou d'Asie.

### 2.8 L'ensemble des « anciens clients »

Par souci d'exactitude, plusieurs grandes entreprises ne sont **plus** des clients principaux de Samsung Foundry malgré des références plus anciennes dans la presse :

- **NVIDIA** — Les GPU Ampere A8000 / GA100 ont partiellement utilisé le 8 nm de Samsung, mais le marché s'est rapidement tourné vers TSMC pour Hopper, Blackwell et Rubin. NVIDIA aujourd'hui est à très grande majorité chez TSMC.
- **Apple** — N'est plus client significatif de Samsung Foundry pour le silicon avancé iPhone/Mac depuis l'ère A9. Tout le silicon Apple actuel est chez TSMC.
- **AMD** — Les CPU/GPU AMD de pointe sont chez TSMC ; certains travaux AMD historiques ont utilisé GlobalFoundries ; Samsung n'est pas l'actuel partenaire AMD à l'échelle sur les nœuds avancés.

Le renouvellement de la clientèle est réel. La composition de Samsung Foundry en 2026 est structurellement différente de celle de 2020.

---

## 3. Ce que la composition de la clientèle révèle

### 3.1 Lecture par patterns de la composition client

En lisant la liste confirmée 2026 comme un tableau d'ensemble, quatre tendances se dégagent :

| Tendance | Ce qu'elle dit de Samsung Foundry |
| --- | --- |
| **Forte pondération accélérateurs IA (Tenstorrent, Tesla, Rebellions, FuriosaAI, Ambarella)** | La position challenger est réelle. Samsung est la fonderie des « accélérateurs IA qui ne vont pas chez TSMC ». |
| **Forte exposition automobile/ADAS (Tesla, Ambarella, Samsung Auto, Hyundai Pleos)** | L'automobile est un avantage structurel où l'engagement long terme, la capacité et les systèmes qualité de Samsung surpassent le statut de tier-2 automobile de TSMC. |
| **Samsung System LSI captif comme plancher** | Le plancher d'utilisation du fab est indépendant des gains de clients externes. |
| **Mobile intermédiaire (Qualcomm sous-flagship, Google Pixel, fabless coréens/asiatiques)** | Samsung est compétitif sur le « point optimal de volume de production » des nœuds 4 / 5 / 8 / 12 nm plutôt qu'au front de pointe absolu. |

### 3.2 Ce qui n'est *pas encore* sur la liste (et pourquoi c'est important)

Tout aussi instructif : qui n'est **pas** sur la liste de clients de Samsung Foundry à partir de 2026.

- **Aucun hyperscaler IA de pointe** — NVIDIA, AMD, Apple silicon, Microsoft Maia (TSMC), Meta MTIA (TSMC) sont tous chez TSMC. L'effort de Samsung sur le nœud 2 nm (SF2) est incertain en matière de rendements et de clients jusqu'en 2027.
- **Aucun Snapdragon flagship signalé sur SF3 / SF2.** Tant que cela ne change pas, l'écart de volume mobile flagship de Samsung persiste.

Ces absences ne sont *pas* un échec. Elles représentent le fossé que les nœuds SF2 et SF1.4 de Samsung doivent combler en 2027–2028 pour passer de « #2 crédible » à « parité commerciale avec TSMC ».

### 3.3 La lecture challenger

En une phrase : **Samsung Foundry en 2026 remporte les clients qui ont besoin de capacité, souhaitent éviter une concentration chez TSMC, ou valorisent l'engagement long terme de qualité automobile — et ne remporte pas encore le volume d'accélérateurs IA hyperscaler de pointe.**

C'est exactement le profil client d'un #2 crédible dans un duopole, avec une optionnalité challenger soutenue sur les prochains nœuds.

---

## 4. Implications pour l'action Samsung Electronics

Ce n'est pas un article de recommandation d'investissement, mais la composition de la clientèle a des implications directes sur la lecture de Samsung Electronics (KS : 005930) :

1. **Samsung Foundry n'est pas la ligne de revenus de pointe.** La hausse de la mémoire IA pour Samsung Electronics passe par DS Memory (expansion des clients HBM4 vers NVIDIA, DRAM serveurs IA), pas par les gains de clients externes de Samsung Foundry. Confondre les deux mène à des erreurs de lecture.
2. **Les gains de clients de Samsung Foundry sont durables, pas explosifs.** Tesla, Tenstorrent, Ambarella, Google Pixel, et la couche fabless coréenne/asiatique composent régulièrement. Ils ne génèrent pas un seul trimestre qui réévalue le titre.
3. **L'inflexion des nœuds 2 nm (SF2) est la vraie variable de basculement.** La capacité de Samsung Foundry à remporter au moins un grand client IA externe sur SF2 en 2027–2028 est le résultat binaire qui repositionne matériellement la trajectoire de revenus de Samsung Foundry et le profil de marge du segment fonderie de Samsung.
4. **La couche AI ASIC coréenne/asiatique devient significative avec plusieurs clients montant en puissance simultanément.** Un seul gain Rebellions ou FuriosaAI est modeste. Cinq à dix startups d'accélérateurs IA coréennes/asiatiques montant en cadence simultanément sur la capacité Samsung 4 / 5 nm devient matériel.

---

## 5. FAQ

**Q : Samsung Foundry est-il la même chose que Samsung Electronics ?**
R : Samsung Foundry est la division de fabrication de puces à façon de Samsung Electronics (KOSPI : 005930). Elle est intégrée dans la division DS (Device Solutions) de Samsung aux côtés de la Mémoire et de System LSI. Ce n'est pas une entité cotée séparément.

**Q : Samsung Foundry est-il coté en bourse ?**
R : Non, pas séparément. Pour s'y exposer, on achète Samsung Electronics (005930). Les revenus et le résultat opérationnel de Samsung Foundry sont reportés dans le segment DS Foundry à l'intérieur des états financiers consolidés de Samsung Electronics.

**Q : Sur quels nœuds de procédé Samsung Foundry produit-il actuellement ?**
R : À partir de 2026, Samsung Foundry est en production sur les nœuds 14 / 8 / 7 / 5 / 4 / 3 nm. Le nœud GAA (gate-all-around) de classe 3 nm est en production depuis 2022, avec une montée en cadence continue en rendements et en clientèle. Le nœud 2 nm (SF2) est la prochaine cible majeure.

**Q : Quel est le plus grand client de Samsung Foundry ?**
R : En interne — Samsung System LSI (Exynos, capteur d'image, modem) est la charge de travail interne la plus importante. Parmi les clients externes, Tesla et Qualcomm ont historiquement représenté les volumes les plus élevés ; Tenstorrent et Google Pixel sont également significatifs.

**Q : Samsung Foundry fabrique-t-il des puces NVIDIA ?**
R : Pas dans la génération actuelle de 2026. Les accélérateurs IA de pointe de NVIDIA (Hopper, Blackwell, Rubin) sont chez TSMC. Samsung a produit les GPU Ampere de NVIDIA en 8 nm, mais NVIDIA a migré vers TSMC pour les générations suivantes.

**Q : Samsung Foundry est-il en concurrence avec TSMC ?**
R : Oui — Samsung est largement considéré comme le challenger #2 de TSMC sur les nœuds avancés. TSMC conserve la base de clients hyperscaler IA de pointe ; Samsung concurrence efficacement dans les segments automobile, startups d'accélérateurs IA, mobile intermédiaire, et fabless coréens/asiatiques.

**Q : Samsung Foundry perd-il des clients au profit de TSMC ?**
R : Le renouvellement de la clientèle se fait dans les deux sens. Samsung a perdu un volume significatif Apple / NVIDIA / AMD de pointe entre 2018 et 2024. Il a gagné la continuité multi-générations avec Tesla, Tenstorrent, Ambarella, et une base de clients fabless coréens/asiatiques croissante. La composition de la clientèle 2026 est structurellement différente de 2020.

**Q : Qu'est-ce que le nœud SF2 ?**
R : SF2 est le procédé 2 nm de Samsung Foundry, inscrit sur la feuille de route publiée de la société pour une montée en production fin 2025 / 2026. La question de savoir si Samsung remporte des clients externes majeurs sur SF2 — en particulier pour un accélérateur IA de pointe — est l'inflexion 2026–2027 la plus suivie pour le positionnement de Samsung Foundry.

---

## 6. Cadrage final

La chose la plus instructive qu'on puisse faire avec la question « Qui utilise Samsung Foundry ? » est de **laisser la réponse changer la façon dont on appréhende Samsung Foundry lui-même**. Lu comme une liste de noms, le portefeuille clients 2026 dit « Samsung Foundry est une fonderie sérieuse avec des clients sérieux ». Lu comme un *pattern* — forte pondération accélérateurs IA + automobile + fabless coréen/asiatique + Samsung System LSI captif — la même liste dit « Samsung Foundry est le challenger crédible de TSMC, avec la composition de clientèle qu'on attendrait d'un #2 dans un duopole ».

Les deux lectures sont justes. Celle qui compte pour votre décision dépend de si vous posez la question dans une optique d'approvisionnement, d'allocation actions, ou de compréhension de la carte mondiale des semiconducteurs. Pour les trois, la réponse est plus utile que le bruit médiatique ambiant ne le laisse entendre.

---

## Annexe — Niveau de preuve

### [Fait]

- Samsung Foundry est la division de fabrication de puces à façon de Samsung Electronics (KOSPI : 005930), intégrée dans la division DS (Device Solutions) aux côtés de la Mémoire et de System LSI.
- Tesla est client multi-générationnel de Samsung Foundry (HW3 en 14 nm, HW4 en 7 nm, engagement continu sur les générations suivantes).
- Les accélérateurs Wormhole et Blackhole de Tenstorrent sont produits sur les nœuds avancés de Samsung Foundry, dont SF4X.
- Qualcomm s'approvisionne en dual-source chez Samsung Foundry et TSMC, le Snapdragon 8 Gen 1 ayant notamment été produit sur le 4 nm Samsung.
- Les SoC Google Pixel Tensor (G1–G4) ont été produits chez Samsung Foundry.
- La famille ADAS CV3-AD d'Ambarella est sur le nœud 5 nm de Samsung.
- Samsung System LSI (Exynos, logique capteur d'image, modem) est la charge de travail captive chez Samsung Foundry.
- Les clients fabless coréens, dont Rebellions, FuriosaAI (Renegade), DeepX, et OpenEdges Technology, utilisent les nœuds 4 / 5 / 8 / 12 nm de Samsung Foundry.
- Les générations Hopper / Blackwell / Rubin de NVIDIA sont chez TSMC, pas chez Samsung.
- Apple silicon est chez TSMC, pas chez Samsung, depuis l'ère A9.

### [Inférence]

- La relation avec Tesla à travers HW5 est le signal de continuité client externe le plus surveillé de Samsung Foundry.
- Le partenariat Tenstorrent représente la validation la plus claire de Samsung Foundry en tant qu'accélérateur IA non-NVIDIA.
- La concentration de la clientèle sur les accélérateurs IA, l'automobile, et le fabless coréen/asiatique reflète le positionnement challenger de Samsung — disponibilité de capacité, valeur du dual-source, et flexibilité tarifaire — plutôt qu'une parité de rendements au front de pointe avec TSMC.
- Le portefeuille de clients externes du nœud SF2 (2 nm) sera le principal facteur déterminant de comment Samsung Foundry sera repositionné dans le duopole mondial des fonderies jusqu'en 2027–2028.

### [Spéculation]

- Un retour d'un Snapdragon flagship vers Samsung Foundry sur SF3 ou SF2 serait un signal de réévaluation majeur et positif pour le segment fonderie de Samsung.
- Un engagement continu de Tesla à travers HW5 et au-delà ancrerait les revenus de nœuds avancés automobile de Samsung à une échelle significative jusqu'en 2028.
- Un gain de Samsung Foundry sur au moins un accélérateur hyperscaler IA externe sur SF2 déplacerait matériellement le cadrage actuel de « #2 crédible » vers « compétitif commercialement au front de pointe absolu ».

### [Non disponible]

- Contributions volumétriques wafer par client aux revenus trimestriels du segment DS Foundry de Samsung.
- Courbes de rendement par nœud et trajectoires d'apprentissage de Samsung Foundry.
- Conditions tarifaires confidentielles tier-1 permettant une comparaison directe TSMC / Samsung Foundry sur le même nœud.
- La liste complète des clients externes pour les démarrages de conception SF2 de Samsung Foundry.

---

**Avertissement** : Cet article est un commentaire de recherche, pas un conseil en investissement. Les descriptions de la composition de la clientèle sont fondées sur des références clients publiquement divulguées, des commentaires d'appels de résultats, et des reportages presse sur la chaîne d'approvisionnement ; les allocations spécifiques en volume de wafers ne sont pas divulguées publiquement. La liste de clients de Samsung Foundry évolue en permanence. Les tickers cités sont illustratifs du cadre d'analyse, et non des recommandations. Effectuez votre propre due diligence et consultez des conseillers agréés avant toute décision d'investissement.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
