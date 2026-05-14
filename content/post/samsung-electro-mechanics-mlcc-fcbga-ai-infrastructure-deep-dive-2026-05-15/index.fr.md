---
title: "Samsung Electro-Mechanics — L'infrastructure invisible du silicium IA. MLCC (stabilité de l'alimentation), FC-BGA (substrat de puce) et modules caméra disséqués"
date: 2026-05-15
description: "Samsung Electro-Mechanics a franchi pour la première fois le cap des 3 000 milliards de KRW de chiffre d'affaires trimestriel. Au 1T26 : CA de 3 210 milliards KRW, résultat opérationnel de 280,6 milliards KRW. Les MLCC pour serveurs IA et les substrats d'empaquetage FC-BGA entrent dans une phase où prix, volumes et taux d'utilisation progressent simultanément. SEMCO ne fabrique pas de puces. Elle fabrique les « composants de stabilisation de l'alimentation (MLCC) » et les « substrats qui relient les puces aux cartes mères (FC-BGA) » dont le silicium IA a besoin pour fonctionner concrètement dans un serveur. Cet article disséque les trois divisions — Composants, Package Solution et Optique — pour expliquer pourquoi cette société est en train de se rerater, passant de « fabricant de composants pour smartphones » à « plateforme de composants d'infrastructure IA », et quelles anticipations sont déjà intégrées dans le cours actuel de 1,02 million de KRW."
categories: ["Sector-Deep-Dive"]
tags:
  - "Samsung Electro-Mechanics"
  - "009150"
  - "MLCC"
  - "FC-BGA"
  - "silicium IA"
  - "substrat d'empaquetage"
  - "actions coréennes"
slug: samsung-electro-mechanics-mlcc-fcbga-ai-infrastructure-deep-dive-2026-05-15
---

*Samsung Electro-Mechanics (SEMCO, KRX 009150) a franchi pour la première fois le cap des 3 000 milliards de KRW de chiffre d'affaires trimestriel. Au 1T26 : CA de 3 210 milliards KRW, résultat opérationnel de 280,6 milliards KRW. Le chiffre d'affaires des substrats d'empaquetage a progressé de +45 % en glissement annuel, s'imposant comme le moteur principal du rerating. Le titre est passé de 830 000 KRW fin avril à 1 024 000 KRW à la mi-mai — soit une hausse de +23 %. Les objectifs de cours côté sell-side ont bondi de 1,0 M KRW à 1,5 M KRW en quelques semaines. Pourtant, peu d'investisseurs sont en mesure d'expliquer clairement ce que SEMCO fabrique réellement, pourquoi la société est considérée comme un « bénéficiaire de l'IA » et ce que font chacune de ses trois divisions. Cet article disséque SEMCO division par division.*

---

## Points clés à retenir

* **SEMCO n'est pas un fabricant de puces.** Elle fabrique les **composants de stabilisation de l'alimentation (MLCC)** et les **substrats qui relient les puces IA aux cartes mères (FC-BGA)** dont le silicium IA a besoin pour fonctionner dans un serveur.
* **Trois divisions** : Composants (MLCC, 46 % du CA, 67 % du résultat), Package Solution (FC-BGA, 20 % du CA, 15 % du résultat), Optique (modules caméra, 34 % du CA, 18 % du résultat).
* **Changement structurel** : auparavant cataloguée « fabricant de composants pour smartphones », SEMCO est aujourd'hui reratable sur la thèse des **MLCC haut de gamme pour serveurs IA / xEV + FC-BGA pour accélérateurs IA en pénurie structurelle d'offre**.
* **Résultats 1T26** : CA de 3 210 milliards KRW (+17 % en g.a.), résultat opérationnel de 280,6 milliards KRW (+40 % en g.a.). En excluant une charge exceptionnelle de licenciement de 71,4 milliards KRW, le résultat opérationnel sous-jacent ressort à 352,0 milliards KRW.
* **La division qui compte le plus** : les Composants (MLCC) défendent les bénéfices. Package Solution (FC-BGA) tire le cours de bourse. L'Optique est le compartiment d'options.
* **À 1,02 M KRW aujourd'hui** : valorisation élevée sur les chiffres 2026, tenable uniquement si le cycle des substrats IA se poursuit jusqu'en 2027–2028. Une approche patiente — attendre les prochains résultats — est plus raisonnable que de courir après le mouvement.

---

## 1. Par où commencer — pourquoi SEMCO est-elle un « bénéficiaire de l'IA » ?

### 1.1 L'infrastructure invisible du silicium IA

Dans un article précédent consacré à Samsung Electronics, j'avais qualifié la HBM d'« établi du silicium IA ». Mais même le meilleur établi (la mémoire) et le meilleur ordinateur (le GPU) ne fonctionneront pas si **l'alimentation est instable (le système plante) ou si la puce n'est pas correctement raccordée à la carte mère (le flux de données se rompt).**

Ce que SEMCO fabrique, c'est précisément ce type d'« infrastructure invisible ».

```
Ce que font les composants SEMCO dans un serveur IA :

1. MLCC — le petit barrage électrique
   → Stocke l'électricité un instant et la restitue de façon lissée
   → Les puces IA connaissent des pics de consommation sous charge ;
     les MLCC absorbent ces variations
   → Un seul serveur IA utilise des dizaines de milliers de MLCC

2. FC-BGA — l'assise de la puce
   → Un substrat de circuit haute densité qui relie les puces IA
     (GPU, CPU) à la carte mère
   → Assure à la fois l'alimentation et le signal entre la puce et la carte
   → À mesure que les puces IA grossissent et se complexifient,
     les substrats s'agrandissent et empilent plus de couches

3. Modules caméra — les yeux
   → Caméras pour téléphones, voitures, robots
   → Pas directement lié à l'IA, mais une vraie option à mesure que
     la franchise s'étend vers l'automobile et la robotique
```

### 1.2 Pourquoi l'offre est-elle tendue en ce moment ?

Dans l'article sur Samsung Electronics, j'avais noté que la HBM « absorbe la capacité de fab ». Un phénomène similaire se déroule pour les MLCC et le FC-BGA.

```
MLCC :
→ Les serveurs IA consomment beaucoup d'énergie avec de fortes variations
→ Le contenu en MLCC par serveur a bondi
→ Dans le même temps, la demande xEV explose
→ L'offre ne peut pas être augmentée rapidement — les composants
  haute tension, haute température, haute fiabilité requièrent
  de longs cycles de qualification
→ Les prix commencent à monter

FC-BGA :
→ Les puces IA plus grandes nécessitent des substrats plus grands
→ Substrats plus grands → plus de couches → rendements plus faibles
   (la proportion de substrats produits sans défaut chute)
→ Les panneaux plus grands font aussi entrer moins d'unités par ligne
→ La construction d'une fab de substrats greenfield prend 2 à 3 ans
→ La demande monte maintenant ; une offre supplémentaire significative
  est un événement post-2028
→ De maintenant jusqu'en 2027, c'est la fenêtre de « pénurie d'offre »
```

**Résumé en une ligne** : SEMCO n'est pas un fabricant de puces IA ; elle fabrique les **composants d'alimentation et de connectivité sans lesquels les puces IA ne peuvent pas fonctionner** — et ces composants sont en pénurie aujourd'hui.

---

## 2. Dissection des trois divisions

### 2.1 La structure de SEMCO

| Division | Produits clés | CA 2025 | Mix | Résultat 2025 | Mix résultat | Marge |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| **Composants** | **MLCC, inductances, résistances chip** | **5 200 Mds KRW** | **46 %** | **609,4 Mds KRW** | **67 %** | **11,7 %** |
| Package Solution | Substrats FC-BGA | 2 300 Mds KRW | 20 % | 135,2 Mds KRW | 15 % | 5,9 % |
| Optique | Modules caméra | 3 810 Mds KRW | 34 % | 168,7 Mds KRW | 18 % | 4,4 % |
| **Total** | | **11 310 Mds KRW** | **100 %** | **913,3 Mds KRW** | **100 %** | **8,1 %** |

```
Répartition des rôles au sein de SEMCO :
Composants (MLCC)         = défend les bénéfices (67 % du résultat opérationnel)
Package Solution (FC-BGA) = fait bouger le cours (+45 % de croissance en g.a.)
Optique (caméras)         = construit le volume de CA + options futures
```

---

## 3. Composants (MLCC) — le fossé de rentabilité

### 3.1 Qu'est-ce qu'un MLCC ?

MLCC = Multi-Layer Ceramic Capacitor (condensateur céramique multicouche). Le terme est technique, mais la fonction est simple — **stocker l'électricité un instant et la fournir de façon lissée aux puces environnantes**.

```
Analogie : le château d'eau d'un réseau de plomberie

Si la pression de l'eau monte et descend, le débit est instable.
Un château d'eau stocke l'eau et la restitue de façon régulière.

Le MLCC fait la même chose avec l'électricité :
si le courant monte et descend, la puce se comporte mal.
Le MLCC stocke brièvement la charge et la restitue de façon lissée.

Taille : plus petit qu'un grain de riz (0,1 mm – 3 mm)
Quantité : \~1 000 dans un smartphone, des dizaines de milliers
           dans un serveur IA
```

### 3.2 Pourquoi les MLCC SEMCO sont-ils importants ?

```
Structure du marché MLCC :
#1 Murata (Japon)                   \~33 % de part de marché
#2 Samsung Electro-Mechanics        \~23 %
#3 Taiyo Yuden (Japon)
#4 Yageo (Taïwan)

→ Les quatre premiers contrôlent l'essentiel du marché
→ Barrière à l'entrée élevée : des centaines de couches céramiques
   de quelques micromètres d'épaisseur empilées uniformément,
   cuites à haute température sans défaut
→ SEMCO maîtrise une technologie d'empilement jusqu'à 600 couches

Pourquoi les MLCC pour serveurs IA sont particulièrement difficiles :
→ Tension, capacitance et tolérance thermique plus élevées que
  les composants pour téléphones
→ Longs cycles de qualification ; une défaillance sur le terrain
  peut planter tout un serveur
→ La liste des fournisseurs qualifiés est étroite
→ Cette étroitesse se traduit par un pricing power et des marges
```

### 3.3 Résultats 1T26 et perspectives

Au 1T26, le CA des Composants s'est établi à 1 410 milliards KRW (+16 % en g.a.), avec un taux d'utilisation de 93 % (contre 70 % pour Package et 66 % pour l'Optique — le plus élevé de la société).

La direction a indiqué que la demande de MLCC haut de gamme pour les serveurs IA et les centres de données reste soutenue à l'entrée du 2T. Les livraisons de MLCC et le prix de vente moyen (ASP) devraient progresser d'un trimestre sur l'autre.

**Le changement le plus important** : certains produits MLCC **commencent à voir leurs prix augmenter**. Murata et Taiyo Yuden ont rapporté des ratios book-to-bill de 1,36 et 1,31 — les plus élevés depuis cinq ans (depuis 2021). Un « BB > 1 » signifie simplement que les commandes excèdent les livraisons ; l'écart est désormais assez large pour parler d'une véritable pénurie.

---

## 4. Package Solution (FC-BGA) — le corps du rerating

### 4.1 Qu'est-ce que le FC-BGA ?

FC-BGA = Flip Chip Ball Grid Array — un **substrat de circuit haute densité** qui relie les puces IA (GPU, CPU) à la carte mère.

```
Analogie : l'assise de la puce

Les puces IA sont petites et denses, avec des dizaines de milliards
de transistors. On ne peut pas les souder directement sur la carte mère
du serveur. Il faut une « assise » intermédiaire qui achemine la puissance
et le signal entre la puce et la carte. Cette assise, c'est le substrat FC-BGA.

Pourquoi c'est difficile :
→ Puces IA plus grandes → substrats plus grands
   (les substrats serveur ont une surface >4× celle des substrats PC grand
   public, avec plus de 20 couches)
→ Des substrats plus grands se déforment → les puces perdent le contact
→ Plus de couches doivent s'aligner précisément → le rendement chute
→ Les pistes fines doivent être gravées à 5–10 micromètres
   (environ 1/10ème de la largeur d'un cheveu humain)

SEMCO est devenue la première société coréenne à produire en série
des FC-BGA pour serveurs, en octobre 2022. En 2025, elle a annoncé
publiquement un partenariat de fourniture de substrats pour centres
de données avec AMD.
```

### 4.2 Pourquoi c'est « le corps du rerating »

Si SEMCO est passée de 830 000 à 1 024 000 KRW, c'est grâce à Package Solution.

```
Package Solution au 1T26 :
CA : 725 Mds KRW (+45 % en g.a., +12 % en g.t.)
Moteurs de croissance : FC-BGA haut de gamme pour accélérateurs IA,
                        CPU serveurs, réseaux

Pourquoi le marché s'est emballé :
1. Les clients demandent plus que la capacité actuelle
   → demande > offre → le pricing power est du côté de SEMCO

2. Un nouveau grand client tech a attribué un programme de substrats
   pour réseaux de centres de données IA
   → plus de clients = CA futur plus important

3. Des discussions d'accords long terme (LTA) sont en cours
   → pas un pic d'un trimestre — demande structurelle → expansion multiple

4. La direction a signalé que les capex 2026 pourraient doubler
   par rapport à 2025
   → investissement en hausse = signal de confiance que la demande
     est réelle
```

### 4.3 Ce que seul SEMCO peut faire

```
Un fabricant de substrats classique : fabrique uniquement des FC-BGA
SEMCO : fabrique des FC-BGA ET des MLCC

Pourquoi c'est important :

Les serveurs IA réduisent les pertes d'énergie en plaçant les
composants de distribution d'alimentation directement sous la puce.
Cela implique d'empiler — ou d'intégrer — des MLCC sur ou dans le substrat.

Parce que SEMCO fabrique les deux, elle peut développer
l'intégration « MLCC dans le substrat » en interne.

Murata (MLCC uniquement) et Ibiden (substrats uniquement)
ne peuvent pas reproduire cela en interne.

→ Cette double compétence est potentiellement le fossé concurrentiel
  le plus durable de SEMCO sur le long terme.
```

### 4.4 Ce qui n'est pas encore prouvé

La marge opérationnelle 2025 de Package Solution n'était **que de 5,9 %**. Le CA a progressé de +13 % en g.a., mais le résultat a reculé de -14 %. Pourquoi ? Les coûts des matières premières (CCL, prepreg) ont augmenté de +19 % tandis que les prix de vente moyens n'ont progressé que de +4 %.

**La question clé : en 2026, la croissance du CA s'accompagnera-t-elle d'une reprise des marges ?** Si seule la ligne supérieure progresse et que les marges stagnent, le cours actuel est difficile à justifier. Savoir si la marge Package Solution au 2T dépassera 12 % est le principal seuil à franchir pour que le rerating se poursuive.

---

## 5. Optique (modules caméra) — gros CA, pas le protagoniste

L'Optique est l'activité de modules caméra pour smartphones et automobiles de SEMCO. CA 2025 : 3 810 milliards KRW (34 % de la société), marge de 4,4 %.

```
État des lieux :
→ CA important (un tiers de la société)
→ Marge la plus basse du portefeuille (4,4 %)
→ Sensible au cycle des smartphones haut de gamme
→ Pas le protagoniste du rerating

Options futures :
→ Caméras ADAS pour véhicules électriques (nombre par véhicule en hausse)
→ Caméras de surveillance du conducteur en habitacle
→ Caméras de vision pour robots et humanoïdes
→ La direction a signalé une montée en production d'un produit
  pour robotaxi à partir du 2T

Part de marché actuelle : \~9 % (contre \~11 % en 2024)
→ Technologie réelle, mais pas la thèse du rerating
```

**Point de vue investisseur** : l'Optique apporte une stabilité au CA mais ne fait pas bouger le titre. Ce sont les MLCC et le FC-BGA qui le font. Les caméras automobile et robotique sont des options à long terme — pas quelque chose pour lequel on paie au multiple actuel.

---

## 6. Valorisation — déjà élevée, mais pour une raison

### 6.1 Où se situe le titre

Au 15 mai, 1 024 000 KRW par action, capitalisation boursière d'environ 76 500 milliards KRW. En hausse de +23 % depuis fin avril.

| Référence | PER | Lecture |
| --- | ---: | --- |
| 12 derniers mois | \~110x | Optiquement très cher |
| Bénéfices estimés 2026 | \~58x | Une fois la reprise des bénéfices intégrée, plus bas |
| Bénéfices estimés 2027 | \~38x | N'a de sens que si le cycle des substrats IA tient jusqu'en 2027 |

### 6.2 Les objectifs de cours sell-side se sont envolés

```
Fév.  : Samsung Sec        1 450 000 KRW (sur la base du BPA 2027)
Mars  : Hana Sec           550 000 KRW (BPA 2026 × 37,5x)
Début avr. : SK Sec        600 000 KRW (PER pairs mondiaux 40x)
Mi-avr. : Hana Sec         810 000 KRW (BPA 2027 × 35x)
Début mai : Hana Sec     1 000 000 KRW (BPA 2027 × 40x)
Mi-mai : KB Sec          1 400 000 KRW
         NH IB / SK Sec  1 500 000 KRW

→ Les objectifs de cours ont plus que triplé en environ trois mois.
```

**Pourquoi si vite ?** Le cadre de valorisation lui-même a changé. SEMCO se traitait auparavant comme un « fabricant coréen de composants électroniques ». Aujourd'hui, le sell-side la compare à ses **pairs mondiaux en substrats IA et composants passifs** — l'Ibiden japonais, l'Unimicron taïwanais, le Murata japonais. Appliquer ces multiples fait bondir les objectifs.

### 6.3 Juste valeur par scénario

| Scénario | BPA estimé 2027 | PER appliqué | Juste valeur | vs. cours spot |
| --- | ---: | ---: | ---: | ---: |
| Baissier (hausse de prix MLCC contenue, capex FC-BGA pèse) | 22 000 KRW | 33x | 730 000 KRW | -29 % |
| **Base** (cycle IA persistant + reprise marge Package) | **26 800 KRW** | **43x** | **1 150 000 KRW** | **+12 %** |
| Haussier (hausses de prix MLCC + FC-BGA simultanées + LTA) | 30 000 KRW | 50x | 1 500 000 KRW | +47 % |

**À 1,02 M KRW aujourd'hui, le potentiel est de +12 % dans le scénario de base** — et de -29 % si le scénario baissier se matérialise, +47 % dans le scénario haussier. À ce cours, attendre la prochaine confirmation des résultats est plus raisonnable que de courir après le rallye.

### 6.4 Le cadrage essentiel : pas « bon marché », mais « cher sans révisions de bénéfices continues »

```
Où se situe SEMCO aujourd'hui :
« Est-ce une bonne société ? »         → Oui
« Le titre est-il bon marché ? »       → Non
« Donc je ne dois pas acheter ? »      → Pas nécessairement — conditionnellement oui

Conditions :
→ Résultat opérationnel 2T supérieur à 400 Mds KRW
  (vs. consensus de 378,8 Mds KRW)
→ Hausse de prix des MLCC se diffusant des distributeurs
  aux clients directs
→ Marge Package Solution passant au-dessus de 12 %
→ LTA ou pré-investissement client se formalisant

Deux de ces conditions réunies = la thèse d'achat fonctionne
au cours actuel.
Zéro de ces conditions = attendre un repli est le bon choix.
```

---

## 7. Ce qu'il faut surveiller désormais

### 7.1 Déclencheurs liés aux résultats

| Déclencheur | Signal haussier | Signal baissier | Quand |
| --- | --- | --- | --- |
| **Résultat opérationnel 2T** | **Supérieur à 400 Mds KRW** | Inférieur à 360 Mds KRW | Fin juillet |
| Hausse de prix MLCC | Se diffuse aux clients IA directs | Reste au niveau du pass-through des coûts | 2T |
| Taux d'utilisation FC-BGA | Pleine utilisation au 2S | Retard dans la montée en charge du nouveau client | 3T |
| Marge Package Solution | 12 %+ au 2T | Inférieure à 10 % | Fin juillet |
| Stocks canal MLCC | \~4 semaines (tendu) | 6+ semaines (en détente) | Trimestriel |

### 7.2 Déclencheurs liés aux multiples

| Déclencheur | Pourquoi c'est important |
| --- | --- |
| Maintien des dépenses d'infrastructure IA | La demande finale, tant pour le FC-BGA que pour les MLCC |
| Accords long terme (LTA) avec les clients | Prouve que ce n'est pas ponctuel — demande structurelle |
| Ratio BB de Murata / Taiyo Yuden | Indicateur avancé du cycle MLCC (plus haut depuis 5 ans aujourd'hui) |
| Plans de capacité mondiale de substrats | Durée de la pénurie d'offre |
| JV substrat Glass Core | Option d'empaquetage de nouvelle génération (2027+) |

### 7.3 Risques à garder à l'œil

| Risque | Description |
| --- | --- |
| **Déjà élevé** | PER 2027 \~38x. Si les estimations de bénéfices se retournent, le titre chute brutalement |
| Charge capex FC-BGA | Doubler les capex double les amortissements ; le CA doit suivre ou les marges se compriment |
| Échec du pass-through | Si l'inflation sur le CCL, l'or et le cuivre ne peut pas être répercutée, les marges souffrent |
| Faiblesse des smartphones | Les modules caméra et certaines références MLCC restent exposés au cycle téléphone |
| Pic des dépenses IA | Si l'investissement en serveurs IA ralentit, les bases de demande FC-BGA + MLCC s'affaiblissent |

---

## 8. Comment cela s'articule avec les autres articles

```
Article Samsung Electronics : « La HBM est l'établi du serveur IA »
→ SEMCO : « Le MLCC est le stabilisateur d'alimentation,
            le FC-BGA est l'assise de la puce »

Article Jeju Semiconductor : « La DRAM commodité est en pénurie
                               à cause de l'IA »
→ SEMCO : « Les composants d'alimentation et les substrats de puces
            sont en pénurie à cause de l'IA »

Article chaîne de valeur robotique : « La partie 1 signalait SEMCO
en montée en charge d'une caméra pour humanoïde au 2S »
→ SEMCO : cette montée en charge vit dans le compartiment
           d'options de l'Optique

Les trois reposent sur la même logique :
Capex IA → pénurie de composants, matériaux, substrats →
pricing power pour le fournisseur en position de goulot d'étranglement.
```

---

## 9. La conclusion en une ligne

SEMCO est la couche d'infrastructure invisible du silicium IA. Les MLCC stabilisent l'alimentation ; le FC-BGA relie la puce à la carte. Les deux sont en pénurie d'offre. Les prix des MLCC ont commencé à monter ; la demande en FC-BGA a dépassé les capacités. Si cette structure tient jusqu'en 2027, SEMCO sera reratable de « fabricant de composants pour smartphones » à « plateforme de composants d'infrastructure IA ».

Mais à 1,02 M KRW, une grande partie de cette thèse est déjà dans le prix. Sur les bénéfices 2027, le PER est de \~38x — « grande société » et « bon prix d'entrée » sont deux questions distinctes. Pour courir après le mouvement depuis ici, les chiffres doivent confirmer : résultat opérationnel 2T supérieur à 400 Mds KRW, diffusion des hausses de prix MLCC, redressement des marges FC-BGA.

**En une ligne : ce n'est pas un titre bon marché — c'est un titre qui n'est « pas cher » que si les révisions de bénéfices à la hausse continuent.** Le rythme de révision importe plus que le flux d'actualités en titre.

---

*Cet article est uniquement de nature analytique et informative ; il ne constitue pas un conseil en investissement. Les chiffres de chiffre d'affaires et de résultat par division sont issus du rapport annuel 2025 de Samsung Electro-Mechanics et de la publication des résultats du 1T26. Le résultat opérationnel du 1T26 de 280,6 milliards KRW inclut une charge exceptionnelle de licenciement de 71,4 milliards KRW. Les taux d'utilisation (Composants 93 %, Package 70 %, Optique 66 %) sont des moyennes annuelles 2025. La part de marché MLCC d'environ 23 % est une estimation de la société. Le partenariat de substrats avec AMD est issu de la communication officielle de SEMCO. Le nom du nouveau grand client tech n'est pas divulgué publiquement. Les scénarios de valorisation (Base 1,15 M KRW, Haussier 1,50 M KRW, Baissier 730 000 KRW) sont des estimations de l'auteur et peuvent être erronées. Les objectifs de cours sell-side (NH / SK 1,5 M KRW, KB 1,4 M KRW, Hana 1,0 M KRW, etc.) reflètent les rapports de chaque courtier et sont susceptibles d'évoluer. La production en série de la JV Glass Core est un plan post-2027 non confirmé. Les hausses de prix MLCC en sont à un stade précoce dans certains canaux distributeurs ; un pass-through plus large n'est pas encore confirmé. L'analyse peut être erronée. Date de coupure des données : 15 mai 2026, heure coréenne.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
