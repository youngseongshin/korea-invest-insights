---
title: "Les deux bêtas du back-end IA — Les substrats sont un « bêta volume », les sockets de test sont un « bêta consommables ». Même vent porteur IA, structures radicalement différentes"
date: 2026-05-15
description: "Qui gagne vraiment de l'argent quand le silicium IA se vend ? Pas seulement les fabricants de GPU et de HBM. Le « back-end » a aussi ses grands gagnants. Deux segments comptent : les substrats et les sockets de test. Tous deux sont classés sous « back-end IA », mais leurs structures d'investissement sont radicalement différentes. Les substrats sont un bêta CAPEX direct sur la construction de serveurs IA. Les volumes augmentent, les packages grossissent, les ASP montent. Le momentum à court terme est fort : Daeduck Electronics OPM 1T26 14,8 %, Samsung Electro-Mechanics revenus package solutions +45 %. Les sockets de test sont un bêta consommables à haute marge sur la complexité des puces. Plus les puces sont complexes, plus le test est difficile, et les sockets doivent être remplacées. ISC OPM 1T26 35 %, revenus IA 81 % du total. LEENO Industrial OPM 47 %. Même vent porteur IA, mais les structures de marge diffèrent d'un facteur ~3. Ne confondez pas les deux dans un même « thème IA ». Pour un momentum de 3 à 6 mois, les substrats. Pour un horizon d'un à deux ans, les sockets de test."
categories: ["Industry-Analysis"]
tags:
  - "silicium IA"
  - "substrat"
  - "socket de test"
  - "FC-BGA"
  - "back-end IA"
  - "actions coréennes"
slug: ai-substrate-vs-test-socket-comparison-2026-05-15
---

> 📚 Série back-end IA
> Précédemment : analyse approfondie MLCC et FC-BGA de Samsung Electro-Mechanics, thèse mémoire legacy de Jeju Semiconductor

*Qui gagne vraiment de l'argent quand le silicium IA se vend ? Nvidia (GPU) et SK hynix (HBM) sont les premiers noms qui viennent à l'esprit. Mais le « back-end » de la chaîne d'approvisionnement a lui aussi ses grands gagnants. On les regroupe sous le terme back-end IA. Deux segments comptent avant tout : les substrats et les sockets de test. Ce sont deux composants que traverse une puce IA avant d'être finalisée — mais leurs structures d'investissement sont radicalement différentes. Les substrats sont un pari sur les « volumes de serveurs IA ». Les sockets de test sont un pari sur la « complexité des puces IA ». Les marges sont environ 3 fois supérieures dans les sockets de test, et le momentum est plus rapide dans les substrats. Lequel constitue le meilleur investissement dépend de votre horizon de détention.*

---

## Points clés

* <strong>Deux segments dans le back-end IA</strong> : les substrats et les sockets de test.
* <strong>Essence des substrats</strong> : un « bêta CAPEX direct » sur la construction de serveurs IA. Plus de volumes → plus de revenus ; packages plus grands → ASP plus élevés.
* <strong>Essence des sockets de test</strong> : un « bêta consommables à haute marge » sur la complexité des puces. Des puces plus complexes → des tests plus difficiles → davantage de sockets, et plus exigeantes.
* <strong>Écart de rentabilité</strong> : au 1T26, Daeduck Electronics 14,8 % contre ISC 35 % contre LEENO Industrial 47,4 %. <strong>Les sockets de test dominent</strong>.
* <strong>Écart de momentum</strong> : les révisions de résultats des substrats sont plus rapides — hausses d'ASP, nouveaux contrats long terme avec les géants technologiques, tensions sur les capacités sont autant de catalyseurs à court terme.
* <strong>Risque de cycle</strong> : les substrats sont soumis au cycle CAPEX (pénurie → CAPEX → surcapacité). Les sockets de test, étant des consommables, présentent une cyclicité plus faible.
* <strong>Conclusion</strong> : trades de momentum à court terme → substrats (Daeduck Electronics, Samsung Electro-Mechanics). Capitalisation sur 1 à 2 ans → sockets de test (LEENO Industrial, ISC). Ce ne sont pas le même « thème IA ».

---

## 1. Mise en contexte — ce que sont vraiment les substrats et les sockets de test

### 1.1 Comment le silicium IA est fabriqué

```
Flux de production du silicium IA :

1. Conception (Nvidia, AMD, Google, Meta, etc.)
2. Fabrication des wafers (TSMC, Samsung Foundry)
3. Découpe
4. Packaging (assemblage HBM, interposeur, substrat de package)
   ← les « substrats » interviennent ici
5. Test (performance / fiabilité / burn-in)
   ← les « sockets de test » interviennent ici
6. Expédition

Substrat      = « le socle sur lequel repose la puce »
Socket de test = « le logement dans lequel la puce s'insère brièvement pour être testée »

Les deux sont des composants que traverse le silicium IA avant finalisation,
mais leurs rôles et modes d'utilisation sont radicalement différents.
```

### 1.2 Le substrat — qu'est-ce que c'est

```
Un substrat relie les circuits microscopiques à l'intérieur d'une puce
(échelle nanométrique) au monde extérieur (échelle millimétrique).

Son rôle :
1. Connexion électrique (des milliers de broches → carte mère)
2. Support mécanique (montage stable de grands packages)
3. Gestion thermique (chemin d'évacuation de la chaleur hors de la puce)
4. Intégrité du signal (signaux haute vitesse sans perte)

Pourquoi l'IA change la donne :
- Les puces IA sont bien plus grandes que le silicium ordinaire
  (Nvidia H100 = 814 mm², 2 à 3 fois un CPU classique)
- Des milliers à des dizaines de milliers de broches
- Transferts de données à haute vitesse
- Budget thermique élevé (700W+)

→ Des substrats spécialisés (FC-BGA) sont nécessaires
→ Plus difficiles à fabriquer et plus coûteux que les substrats ordinaires
→ Acteurs coréens : Samsung Electro-Mechanics, Daeduck Electronics,
  Isu Petasys.
```

### 1.3 La socket de test — qu'est-ce que c'est

```
Une socket de test est un logement utilisé brièvement pour tester une puce finie.

Son rôle :
1. Connecte électriquement chaque broche de la puce au testeur
2. Vérifie le bon fonctionnement sous contraintes de signal, d'alimentation et de température
3. Filtre les unités défaillantes
4. Validation de la fiabilité (tests longue durée)

Analogie :
Puce          = voiture
Socket de test = la prise de diagnostic au contrôle technique
→ Connectée brièvement lors du contrôle, puis déconnectée
→ La même prise sert pour de nombreuses voitures différentes
→ Les prises s'usent avec le temps et doivent être remplacées

Pourquoi l'IA change la donne :
- Les puces IA sont coûteuses (\~30 000 USD pour un H100)
- Une seule unité défaillante représente un coût élevé → l'intensité des tests augmente
- Environnements à forts courants, hautes vitesses, hautes températures
  → spécifications de socket plus exigeantes
- Chaque génération de puce nécessite de nouvelles sockets → revenus récurrents

Acteurs coréens : LEENO Industrial, ISC, TSE.
```

### 1.4 Pourquoi ils ne constituent pas le même « thème IA »

```
Substrat :
- Fabriqué une fois, livré avec la puce (caractère de bien d'équipement)
- Environ un substrat par serveur IA
- Revenu = volume × ASP
- L'ajout de capacité représente une charge en CAPEX

Socket de test :
- Réutilisée de nombreuses fois, puis remplacée (caractère de consommable)
- Environ 50 à 200 sockets pour tester 10 000 puces
- Revenu = production de puces × intensité de test × remplacement de sockets
- Les ajouts de capacité sont plus modestes

Structure de marge :
Substrat :     OPM \~10–15 % (poids du CAPEX et des amortissements)
Socket de test : OPM \~30–50 % (conception sur mesure, économie de consommable)

→ Les deux bénéficient de l'IA,
→ mais le mix de revenus, le profil de marge et la sensibilité au cycle diffèrent.
```

---

## 2. Le côté substrats — « bêta volume serveurs IA »

### 2.1 Ce que le 1T26 a révélé

```
Samsung Electro-Mechanics (009150) — segment Package Solution
(à dominante FC-BGA) :
Revenus 1T26 : 725 milliards KRW
Variation annuelle :  +45 %
Variation trimestrielle : +12 %

Daeduck Electronics (353200) :
Revenus 1T26 : 346,3 milliards KRW (g.a. +61 %)
Résultat opérationnel 1T26 : 51,3 milliards KRW (retour à la rentabilité)
OPM :          14,8 %

Mix produits :
- FCCSP (substrat de package grade mobile) : 39 %
- FCBGA (grade PC / serveur) :              23 %
- CSP (mémoire) :                           22 %
- MLB (carte multicouche, serveur IA) :     16 %

Croissance annuelle :
- Substrats de package : +65 %
- MLB :                  +43 %

→ Substrats de package pour serveurs IA + cartes réseau en croissance simultanée
→ Un bêta direct sur l'infrastructure IA.
```

### 2.2 Pourquoi les substrats sont en pénurie

```
Caractéristiques du FC-BGA pour serveurs IA :
- Surface 2 à 3 fois supérieure à un FC-BGA PC
- Multicouche (20 à 30 couches)
- Signalisation haute vitesse (PCIe 5.0 / 6.0)
- Gestion thermique stricte

Entreprises capables de les fabriquer :
- Corée : Samsung Electro-Mechanics, Daeduck, LG Innotek, Isu Petasys
- Taïwan : Unimicron, Nan Ya PCB
- Japon : Ibiden, Shinko Denki

Le problème : les capacités (CAPA) ne suivent pas la demande
- Les commandes de serveurs IA des géants technologiques ont explosé
- La construction d'une nouvelle usine de substrats prend 2 à 3 ans
- Pénurie → hausses d'ASP → négociations en cours

Source citée dans la presse :
« La demande de FC-BGA de Samsung Electro-Mechanics dépasse les capacités
 d'environ 50 % ; des négociations tarifaires sont en cours. »

→ C'est pourquoi les valeurs liées aux substrats ont été solides.
```

### 2.3 Le risque de cycle des substrats

```
Le substrat est une industrie classique soumise au cycle CAPEX :

Phase haussière (aujourd'hui) :
pénurie → hausse d'ASP → expansion des marges → hausse des cours
→ les entreprises annoncent des CAPEX significatifs

Phase de construction (2026–2027) :
usines en construction → revenus en hausse, charge CAPEX en hausse
→ cours toujours orientés à la hausse

Phase d'achèvement (2027–2028) :
nouvelles usines opérationnelles → l'offre explose
→ si la demande ne suit pas, les prix chutent
→ compression des marges → cours en baisse

Précédents historiques :
Cycle mémoire 2017–2018 : même schéma
Cycle MLCC 2021–2022 :    même schéma

→ Pour investir dans les substrats, « où en sommes-nous dans le cycle CAPEX » est la question clé
→ Aujourd'hui : début à mi-phase d'un cycle haussier
→ Tant que la construction n'est pas achevée, le potentiel haussier est intact.
```

---

## 3. Le côté sockets de test — « bêta complexité des puces »

### 3.1 Ce que le 1T26 a révélé

```
ISC (095340) :
Revenus 1T26 : 68,3 milliards KRW
Résultat opérationnel 1T26 : 23,6 milliards KRW
OPM :          35 %
Calcul : 23,6 / 68,3 = 34,55 %

Mix de revenus :
- Revenus IA :              55,3 milliards KRW (81 % du total)
- Revenus data center :     54,2 milliards KRW (79 % du total)
→ Déjà une « entreprise IA data center ».

LEENO Industrial (058470) :
Revenus 1T26 : 99,77 milliards KRW
Résultat opérationnel 1T26 : 47,30 milliards KRW
OPM :          47,4 %
Calcul : 47,30 / 99,77 = 47,41 %

Mix de revenus :
- Sockets de test IC :       64,10 %
- Broches LEENO (pogo) :     24,65 %
- Composants médicaux :      10,46 %

→ Sockets conçues sur mesure + fabrication intégrée des broches
→ Un OPM de 47 % place LEENO au sommet de l'industrie manufacturière coréenne.
```

### 3.2 Pourquoi les marges sont aussi élevées

```
Caractéristiques structurelles de l'industrie des sockets de test :

1. Conceptions spécifiques à chaque client
   → disposition des broches, taille, conditions de signal varient selon la puce
   → difficile à standardiser → pouvoir de fixation des prix

2. Coût de qualification élevé
   → chaque nouvelle puce nécessite conception, test et qualification de la socket
   → une fois qualifiée, verrouillée jusqu'à la fin de vie de cette puce
   → compétition sur la fiabilité, pas sur le prix

3. Nature consommable
   → les sockets s'usent et se dégradent, nécessitant un remplacement périodique
   → revenus récurrents

4. Renouvellement à chaque génération de puce
   → nouvelle puce = nouvelle socket
   → cadence d'évolution des puces plus rapide = cadence des revenus plus rapide

5. TAM réduit (quelques dizaines de milliards USD)
   → trop petit pour attirer les méga-capitalisations
   → oligopole de spécialistes

Ces cinq conditions réunies permettent d'atteindre un OPM de 30 à 50 %.
```

### 3.3 Pourquoi l'IA a rendu les sockets de test plus importantes

```
Caractéristiques des puces IA :

1. Coûteuses (10 000 à 30 000 USD par unité)
   → le coût d'une seule unité défaillante est élevé
   → intensité des tests ↑

2. Nombre de broches élevé (des milliers à des dizaines de milliers)
   → sockets plus complexes
   → ASP ↑

3. Forts courants / températures / vitesses
   → exigences de durabilité des sockets plus strictes
   → cycle de remplacement plus court

4. Part croissante du SLT (System-Level Test)
   → du simple test fonctionnel → au test système complet
   → durées de test plus longues
   → utilisation accrue des sockets

5. Nouveaux modules : HBM, SOCAMM2, etc.
   → nouvelles catégories de sockets
   → nouvelles lignes de revenus

→ À l'ère de l'IA, la demande de sockets de test croît
   plus vite que la production de puces.
```

### 3.4 ISC vs LEENO Industrial

```
Les deux sont des « entreprises de sockets de test », mais leurs structures diffèrent.

ISC (force : sockets en caoutchouc) :
- Technologie de base : sockets en caoutchouc silicone
- Point fort : tests en production de masse pour data centers IA, SLT
- Clients : grands fabricants mondiaux de GPU / ASIC
- Exposition : data center IA 81 %
- Profil : bêta IA direct (volatilité plus élevée)
- OPM 1T26 : 35 %

LEENO Industrial (force : broches pogo) :
- Technologie de base : broches pogo, fabrication intégrée
- Point fort : R&D, AP mobile, RF, développement ASIC
- Clients : diversifiés (des centaines de comptes)
- Exposition : nombreuses catégories de puces (exposition IA plus faible qu'ISC)
- Profil : compounder de qualité (plus stable)
- OPM 1T26 : 47,4 %

→ Ne les regroupez pas comme « la même valeur socket de test ».
→ ISC      = bêta data center IA
→ LEENO    = plateforme diversifiée à haute marge

Ce sont des compléments, pas des substituts.
```

---

## 4. Comparaison directe

### 4.1 Marges opérationnelles au 1T26

```
Mêmes « bénéficiaires du back-end IA », profils de marge très différents :

Daeduck Electronics (substrat) : 14,8 %  ████
Samsung E-M Package Solutions :  \~12 %   ███
ISC (socket de test) :           35,0 %  █████████
LEENO Industrial (socket) :      47,4 %  ████████████

Pour 100 KRW de revenus → résultat opérationnel :
Daeduck :  14,8 KRW
ISC :      35,0 KRW
LEENO :    47,4 KRW

→ Écart d'environ 3x sur les mêmes revenus
→ Le résultat de différences structurelles sectorielles.
```

### 4.2 Rythme de croissance vs stabilité des marges

| Indicateur | Substrat (Daeduck) | Socket de test (ISC) | Socket de test (LEENO) |
| --- | ---: | ---: | ---: |
| Revenus 1T26 g.a. | +61 % | Forte croissance g.a. | +18 % |
| Résultat opérationnel 1T26 g.a. | retour à la rentabilité | Forte croissance g.a. | +35 % |
| OPM | 14,8 % | 35,0 % | 47,4 % |
| Exposition IA | Moyenne–élevée | Très élevée (81 %) | Moyenne |
| Volatilité | Élevée | Moyenne | Faible |
| Sensibilité au cycle | Élevée | Moyenne | Faible |

```
Synthèse :
- Croissance des revenus : substrat (Daeduck) > socket de test
- Niveau de marge :        socket de test > substrat
- Stabilité des marges :   LEENO > ISC > substrat
- Bêta IA direct :         ISC > Daeduck > LEENO.
```

### 4.3 Risque de cycle

```
Risque de cycle des substrats (élevé) :
- Pénurie → CAPEX → surcapacité, en boucle
- Délai de construction de 2 à 3 ans
- Quand le cycle s'inverse, utilisation et ASP chutent ensemble
- Les amortissements pèsent sur les marges

Risque de cycle des sockets de test (faible) :
- L'économie de consommable amortit la volatilité des revenus
- La conception spécifique au client stabilise les prix
- De nouvelles puces continuent d'être lancées
- Une volatilité trimestrielle subsiste néanmoins

Perspective long terme :
→ Les sockets de test sont bien plus stables
→ Évite le cycle CAPEX des substrats

Perspective momentum court terme :
→ Le momentum des substrats est plus fort
→ Les titres sur les hausses d'ASP / tensions de capacité sont plus fréquents.
```

---

## 5. Priorité d'investissement — des réponses différentes selon l'horizon

### 5.1 Momentum à court terme (3 à 6 mois) — les substrats l'emportent

```
Pourquoi :
- Le rythme des révisions de résultats est plus rapide
- Flux continu d'annonces de hausses d'ASP
- Probabilité de nouveaux contrats long terme avec les géants technologiques
- Livraisons de serveurs IA en accélération

Ordre de préférence :
1. Daeduck Electronics : retournement + bêta AI MLB / FC-BGA
2. Samsung Electro-Mechanics : combo FC-BGA IA + MLCC
3. Isu Petasys (complément) : force sur les MLB ultra-haute densité de couches

Mises en garde :
- Les substrats ont déjà beaucoup progressé
- Vérifier la position dans le cycle CAPEX
- Attendre que la porte macro se dégage (voir article précédent).
```

### 5.2 Détention 1 à 2 ans (croissance de qualité) — les sockets de test l'emportent

```
Pourquoi :
- Structure de marge structurellement supérieure
- Risque de cycle plus faible
- Diversification des puces IA = davantage de catégories de sockets = diversification des revenus
- Expansion active des capacités (nouvelles usines)

Ordre de préférence :
1. LEENO Industrial : qualité la plus élevée, mais multiple déjà riche
2. ISC : bêta direct sur le data center IA
3. TSE (complément) : croissance à un prix plus raisonnable

Mises en garde :
- LEENO est exposée à un risque d'impact sur les marges lors du déménagement de la nouvelle usine
- ISC affiche une volatilité trimestrielle (g.t. 1T26 -6 %)
- Les deux se négocient à des PER de 30 à 45x.
```

### 5.3 Un portefeuille back-end IA combiné

```
Offensif (biais momentum) :
- Daeduck Electronics        40 %
- ISC                        30 %
- Samsung Electro-Mechanics  20 %
- LEENO Industrial           10 %

Équilibré (croissance + stabilité) :
- LEENO Industrial           30 %
- Samsung Electro-Mechanics  25 %
- ISC                        25 %
- Daeduck Electronics        20 %

Défensif (biais qualité) :
- LEENO Industrial           40 %
- Samsung Electro-Mechanics  30 %
- ISC                        20 %
- Daeduck Electronics        10 %

→ Si vous ne deviez en choisir qu'une, selon l'horizon et la tolérance à la volatilité :
→ Détention 1 an+ :   LEENO Industrial
→ 3 à 6 mois :        Daeduck Electronics
→ Bêta direct data center IA : ISC.
```

---

## 6. Quatre idées reçues courantes

### 6.1 #1 : « Les deux sont des valeurs IA, donc c'est pareil »

```
Comme démontré :
- L'OPM diffère d'un facteur 3
- La sensibilité au cycle diffère
- Le mix de revenus diffère

Les regrouper dans un même panier affaiblit la diversification.
→ La volatilité évolue de concert
→ Les associer à un autre secteur est plus efficace.
```

### 6.2 #2 : « Les sockets pogo sont remplacées par les sockets en caoutchouc »

```
Seulement en partie :

Là où la substitution s'opère :
- Grandes puces GPU / ASIC IA
- Tests haute intensité de courant et de signal rapide
- SLT (System-Level Test)
→ La pénétration des sockets en caoutchouc augmente (point fort d'ISC)

Là où elle ne s'opère pas :
- Tests de R&D haute précision
- AP mobiles, puces RF
- Production en petites séries / nombreuses références
→ Les broches pogo maintiennent leur position (point fort de LEENO)

→ Ce n'est pas « l'ensemble du marché bascule » — c'est « une segmentation du marché »
→ ISC et LEENO sont donc complémentaires
→ Il est rare que l'une performe nettement sans l'autre.
```

### 6.3 #3 : « Les valeurs substrats ont trop monté »

```
La bonne question n'est pas le niveau absolu,
c'est « où en sommes-nous dans le cycle CAPEX ».

Aujourd'hui :
- La pénurie se poursuit
- Négociations de hausses d'ASP en cours
- Contrats long terme avec les géants technologiques en discussion
- Les annonces de CAPEX ont débuté, mais les montées en puissance prennent 2 à 3 ans

→ Début à mi-phase d'un cycle haussier
→ Les cours ont progressé, mais le cycle n'a pas encore atteint son sommet.

Cela dit, à ces niveaux :
- Des entrées échelonnées sont recommandées
- Attendre que la porte macro se dégage
- Courir après les cours n'est pas efficace.
```

### 6.4 #4 : « Le TAM des sockets de test est trop petit »

```
Vrai en valeur absolue, mais l'interprétation est erronée :

TAM des sockets de test :
- \~3 à 4 milliards USD
- Moins de 2 % du marché de la mémoire (\~200 milliards USD)
- Faible en termes absolus

Pourquoi c'est en réalité un avantage :
- Trop petit pour attirer les méga-capitalisations
- Maintient l'oligopole de spécialistes
- La concurrence par les prix reste limitée
- OPM de 30 à 50 % atteignable

Comparaison :
Une entreprise à 200 milliards USD de revenus avec 5 % d'OPM vs
une entreprise à 4 milliards USD de revenus avec 45 % d'OPM
→ Résultat opérationnel absolu comparable
→ La seconde est plus stable et plus prévisible.

C'est la structure dont bénéficient LEENO et ISC.
```

---

## 7. Les six prochains mois — liste de contrôle

### 7.1 Substrats (confirmation du cycle intact)

```
Signaux positifs :
□ Les hausses d'ASP FC-BGA se poursuivent
□ Samsung E-M / Daeduck ajoutent de nouveaux clients géants technologiques
□ Le mix grandes dalles / haute densité de couches progresse dans les revenus
□ La demande MLB se maintient sur les réseaux 800G / 1,6T
□ L'utilisation reste au-dessus de 90 % malgré la hausse du CAPEX

Signaux négatifs :
□ Les négociations de hausse d'ASP sont retardées ou échouent
□ Les commandes de serveurs IA des géants technologiques décélèrent
□ Le rythme des nouvelles annonces de CAPEX s'accélère (risque de surcapacité)
□ L'utilisation tombe sous 80 %

Fréquence : résultats trimestriels + commentaires IR en cours de trimestre.
```

### 7.2 Sockets de test (confirmation de la croissance intacte)

```
ISC :
□ Réaccélération des revenus au 3T26 (le 2T peut être un trimestre de montée en puissance)
□ Premier lancement en volume avec un nouveau client d'infrastructure data center
□ Début des revenus issus des tests de production de masse SOCAMM2
□ Le mix SLT reste au-dessus de 70 %
□ Le mix revenus IA reste au-dessus de 80 %

LEENO Industrial :
□ Avancement du déménagement de la nouvelle usine
□ Pas de dégradation des marges pendant le déménagement (OPM 45 %+ maintenu)
□ Diversification clients (Apple / TI / HPC / expansions ASIC)
□ Forte demande de sockets R&D
□ Absence de pression au capital / problèmes de gouvernance

Fréquence : résultats trimestriels.
```

### 7.3 La toile de fond macroéconomique

```
La porte macro de l'article précédent :
- Taux 10 ans américain sous 4,45 %
- Brent sous 105 USD
- USD/KRW sous 1 480
- VIX sous 18

Ces conditions doivent être réunies pour :
- Un rebond général des actifs risqués
- Que les valeurs back-end suivent la tendance
- Que de bons résultats se traduisent par de bonnes performances boursières.

Si la porte ne se dégage pas :
- Les multiples restent sous pression indépendamment des fondamentaux
- Attendre une clôture de confirmation / un retournement de volume avant de renforcer.
```

---

## 8. Liens avec les autres articles

```
Article Samsung Electro-Mechanics :
→ Double bénéficiaire MLCC + FC-BGA au 1T26
→ La valeur la plus analysée en détail du côté substrats dans cet article
→ PER par scénario pour estimer jusqu'où le multiple peut s'étendre

Article Jeju Semiconductor :
→ « Mémoire classique en pénurie à cause de l'IA »
→ Une autre configuration back-end IA (bêta pénurie mémoire)

Article grève Samsung Electronics :
→ Variable clé pour le supercycle mémoire
→ Silicium IA → serveur IA → mémoire / substrat / socket de test
→ Une perturbation dans un maillon se répercute sur le back-end

Article KOSPI crash + porte macro :
→ « Le cycle avant l'action »
→ Les valeurs de cet article ne sont elles aussi rationnelles qu'après le dégagement de la porte macro.
```

---

## 9. La conclusion en une phrase

Quand le silicium IA se vend, les premiers bénéficiaires sont les fabricants de GPU et de HBM. Mais le back-end compte lui aussi deux grands gagnants — <strong>les substrats et les sockets de test</strong>.

Tous deux sont regroupés sous « back-end IA », mais leurs structures sont radicalement différentes. <strong>Les substrats sont un « bêta volume serveurs IA ».</strong> Les volumes augmentent, les packages grossissent, les ASP montent — upside direct. Le momentum est rapide et les marges opérationnelles s'élargissent à partir d'une base de \~12–15 % au 1T26. Mais c'est une industrie soumise au cycle CAPEX, et la date d'achèvement des constructions constitue le risque majeur.

<strong>Les sockets de test sont un « bêta complexité des puces ».</strong> Plus les puces se complexifient, plus les tests deviennent exigeants, et de nouvelles sockets sont nécessaires à chaque fois. L'OPM s'établit à 35 % pour ISC et 47 % pour LEENO — environ 3 fois les marges des substrats. L'économie de consommable amortit la cyclicité. Les inconvénients : le TAM est restreint et les multiples sont déjà élevés.

<strong>Ne les regroupez pas dans un même « thème IA ».</strong> Pour un momentum à court terme, les substrats (Daeduck Electronics, Samsung Electro-Mechanics) ont l'avantage. Pour une détention de 1 à 2 ans, les sockets de test (LEENO Industrial, ISC) sont plus appropriées. La meilleure approche est de détenir les deux en complémentarité — quand les substrats vacillent à un pic de cycle, les sockets de test amortissent le choc ; quand les sockets de test subissent une pression sur leurs multiples, le momentum des substrats prend le relais.

<strong>Même vent porteur IA, structures radicalement différentes — comprendre cela seul suffit à élever d'un cran la qualité de vos décisions d'investissement dans le back-end.</strong>

---

*Cet article est une analyse et un commentaire de marché uniquement et ne constitue pas un conseil en investissement. Les chiffres Samsung Electro-Mechanics 1T26 sont issus de la publication IR officielle de la société. Les chiffres Daeduck Electronics 1T26 (revenus 346,3 milliards KRW, résultat opérationnel 51,3 milliards KRW, OPM 14,8 %) sont issus de ses documents IR. Les chiffres ISC 1T26 (revenus 68,3 milliards KRW, résultat opérationnel 23,6 milliards KRW, OPM 35 %, mix revenus IA 81 %, mix data center 79 %) sont issus de ses documents IR. Les chiffres LEENO Industrial 1T26 (revenus 99,77 milliards KRW, résultat opérationnel 47,30 milliards KRW, OPM 47,4 %) sont issus du rapport de résultats préliminaire ; les données de mix produits (sockets de test IC 64,10 %, broches LEENO 24,65 %, composants médicaux 10,46 %) sont issues du rapport trimestriel. L'OPM est calculé comme le résultat opérationnel divisé par les revenus, arrondi à une décimale. Les parts de revenus IA / data center sont dérivées des communications des entreprises. La comparaison des marges opérationnelles porte sur un seul trimestre (1T26) ; les moyennes annuelles peuvent différer. Le risque de cycle CAPEX, le risque de marge lié au déménagement de la nouvelle usine et la volatilité de la demande IA sont des jugements de l'auteur et non des certitudes. Les variables macroéconomiques mondiales (taux américains, pétrole, taux de change, VIX) peuvent impacter les cours indépendamment. L'analyse peut être erronée. Données arrêtées au 15 mai 2026, heure coréenne.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
