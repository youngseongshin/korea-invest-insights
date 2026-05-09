---
title: "Chaîne de valeur optique & CPO en Corée — Seul OE Solutions (138080.KQ) est véritablement proche du CPO ; six des sept valeurs ont progressé de +300 à +900 % depuis le début de l'année sans que les bénéfices suivent"
slug: korea-optical-cpo-value-chain-seven-companies-2026-05-09
date: 2026-05-09T20:00:00+09:00
description: "Le prochain goulot d'étranglement des centres de données IA se déplace vers l'interconnexion optique. Des dizaines de milliers de GPU communicant entre eux exigent des modules optiques 800G et 1.6T, et la Co-Packaged Optics (CPO) — qui place le moteur optique directement à côté de l'ASIC de commutation — s'impose comme la réponse architecturale. En cartographiant les sept valeurs coréennes cotées — OE Solutions, Optocore, Daehan Optical Communications, BWE, WooriRo, Lycom, Coset — seule OE Solutions est genuinement proche du CPO grâce à son source laser externe ELSFP et à sa puce laser EML 100G développée en interne. Les six autres sont des bénéficiaires en aval ou des paris thématiques. Et six sur sept affichent +300 % à +905 % depuis le début de l'année avec des pertes opérationnelles toujours en place. Le prix a bougé avant les résultats. La lecture actionnable : OE Solutions en liste de surveillance (en attendant soit un repli soit la confirmation de l'envoi d'échantillons clients ELSFP en 3T26), les autres mis en attente jusqu'à ce que la surchauffe se dissipe."
categories: ["Sector-Deep-Dive", "Korea Market", "Semiconductors"]
tags:
  - "interconnexion optique"
  - "CPO"
  - "co-packaged optics"
  - "OE Solutions"
  - "138080"
  - "Optocore"
  - "Daehan Optical"
  - "BWE"
  - "WooriRo"
  - "Lycom"
  - "Coset"
  - "centre de données IA"
  - "ELSFP"
  - "source laser externe"
  - "EML"
  - "petites capitalisations coréennes"
  - "émetteur-récepteur optique"
  - "800G"
  - "1.6T"
---

> 🔗 **À lire aussi** : [Hub PCB & Substrat IA](/page/korea-ai-pcb-substrate-hub/) · [Écosystème PCB IA coréen — 10 sociétés](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) · [Thèse PCB & Substrat IA — La nomenclature système comme goulot d'étranglement commun](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) · [Haesung DS — Du lead frame au second-source de heat spreader IA](/post/haesung-ds-leadframe-ai-heat-spreader-second-source-2026-05-07/)

*Le [billet sur la thèse substrat](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) défendait un argument de dénominateur commun : la demande IA ne s'achète pas puce par puce, elle s'achète rack par rack, et la demande de substrat traverse l'intégralité de la nomenclature. La même logique s'étend désormais à l'interconnexion optique — et les expositions coréennes cotées sont bien moins matures. Sept valeurs se positionnent sur l'axe optique / CPO. Une seule (OE Solutions, 138080.KQ) est genuinement proche de la nouvelle architecture CPO via son **source laser externe ELSFP**. Les six autres sont des bénéficiaires en aval ou des paris thématiques. Et six sur sept affichent +300 % à +905 % depuis le début de l'année face à des pertes opérationnelles ou des victoires clients non vérifiées. C'est un marché du type « thèse technique valide, mauvais prix » — exactement le genre de configuration où cartographier la chaîne de valeur par **distance au véritable goulot d'étranglement** est plus utile qu'acheter les valeurs les plus en hausse.*

---

## En résumé

* **Parmi les valeurs coréennes cotées, seule OE Solutions (138080.KQ) est véritablement proche du CPO.** Elle a communiqué sur un produit **source laser externe ELSFP** compatible CPO (standard OIF, 8 canaux, 23 dBm/200 mW par canal, refroidissement TEC, échantillons clients prévus pour 3T26) et a développé une **puce laser EML 100G**, une première sur le marché domestique. Les six autres ne sont pas sur la trajectoire cœur du CPO. OE Solutions ne figure pas encore sur la liste publique des partenaires CPO de Nvidia ou Broadcom.
* **Optocore détient de vrais contrats d'émetteurs-récepteurs optiques pour centres de données IA** totalisant environ ₩16,7 mds — mais le client n'est pas divulgué et le titre est suspendu sur un audit de continuité d'exploitation en 1T26. **Non investissable.**
* **Daehan Optical Communications progresse de +905 % depuis le début de l'année sur un récit "plus de fibre optique pour l'IA" — ce n'est pas du tout un dossier CPO.** C'est un fabricant intégré verticalement de préforme à câble, non un fournisseur de moteurs optiques ou de lasers. La Korea Exchange l'a signalé pour escalade vers le statut d'avertissement d'investissement.
* **Six valeurs sur sept affichent +300 %+ depuis le début de l'année face à des comptes de résultat toujours déficitaires.** Daehan +905 %, BWE +778 %, WooriRo +616 %, OE Solutions +307 %. Le prix a bougé bien avant que les résultats suivent. Acheter ici revient à parier sur le **rattrapage du prix par rapport à ses propres anticipations prospectives**, et non sur la validité de la technologie.
* **La lecture claire pour un allocataire est OE Solutions en liste de surveillance avec attente, les six autres en pause.** OE Solutions se traite à >100× le bénéfice opérationnel 2026E au prix actuel — le point d'entrée se situe au **repli vers 47 000–50 000 wons** ou après **la confirmation de l'envoi des échantillons clients ELSFP en 3T26**, pas en momentum.

---

## 1. Pourquoi l'optique est le prochain goulot d'étranglement des centres de données IA

### 1.1 Même logique que le substrat — au niveau de la couche réseau

La thèse substrat était un argument de « dénominateur commun » : chaque puce supplémentaire dans un rack IA — GPU, CPU, DPU, NIC, ASIC de commutation, module mémoire — accroît la demande de substrat. L'interconnexion optique obéit à la même logique au niveau de la couche réseau. Des dizaines de milliers de GPU dans un seul cluster d'entraînement nécessitent une bande passante réseau que la signalisation électrique ne peut pas fournir à une consommation d'énergie acceptable. Le lien devient donc optique.

```
Chaîne de demande optique pour centres de données IA :

Cluster de GPU à plusieurs dizaines de milliers d'unités
   ↓
ASICs de commutation (connectivité réseau)
   ↓
Émetteurs-récepteurs optiques 800G → 1.6T (électrique → optique → électrique)
   ↓
Fibre optique et infrastructure câblée (le chemin emprunté par la lumière)
   ↓
Composants : lasers, photodétecteurs, amplificateurs optiques, fibre à faibles pertes
```

Broadcom a indiqué que les délais de livraison des PCB pour émetteurs-récepteurs optiques sont passés de 6 semaines à 6 mois — signal précoce que les composants optiques deviennent la couche contrainte.

### 1.2 Ce qu'est réellement le CPO

L'architecture historique utilisait des **modules optiques enfichables** installés en façade du châssis de commutation. Faciles à remplacer, mais énergivores, avec un signal électrique parcourant un long chemin depuis l'ASIC de commutation jusqu'au panneau avant.

La **Co-Packaged Optics (CPO)** est une architecture différente : le moteur optique est placé **directement à côté de l'ASIC de commutation sur le même substrat de boîtier**. La distance de propagation du signal électrique s'effondre. La puissance par bit chute fortement.

* Nvidia a déclaré que son commutateur à base de CPO offre une efficacité énergétique **5× supérieure** et une **fiabilité réseau 10× meilleure** par rapport aux équivalents enfichables.
* Broadcom a présenté un commutateur Ethernet CPO à 51,2 Tbps affichant **>70 % de réduction de la consommation d'énergie des liaisons optiques**.

### 1.3 Pourquoi la « source laser externe » est cruciale dans le CPO

Le problème fondamental du CPO : **les lasers sont sensibles à la température, les ASICs de commutation sont chauds.** Placer le laser dans le boîtier, à côté d'un ASIC chaud, réduit sa durée de vie et dégrade ses performances.

La solution : **séparer le laser du boîtier.** Déplacer le laser vers le panneau avant, n'acheminer que la lumière dans le boîtier via une fibre, et maintenir le corps du laser thermiquement isolé.

Le format standard de ce laser externe est l'**ELSFP — External Laser Small Form-factor Pluggable**, défini par l'OIF (Optical Internetworking Forum). Lorsque le CPO montera en puissance, l'ELSFP deviendra une catégorie de composants fondamentale.

```
Position de l'ELSFP dans le CPO :

ASIC de commutation (chaud)
   ↓ (lumière entrante)
Moteur optique (adjacent à l'ASIC, lumière ↔ électrique)
   ↑ (lumière sortante)
Source laser externe ELSFP (panneau avant, isolée thermiquement)
   ↑
Laser (haute puissance, stable)
```

**L'ELSFP d'OE Solutions est exactement ce composant.** C'est la seule société coréenne cotée ayant divulgué ce produit spécifique.

---

## 2. Les sept valeurs coréennes — distinguer « exposition CPO réelle » de « thématique optique IA »

| # | Société (ticker) | Position dans la chaîne de valeur | Pertinence optique IA | Performance YTD | Lecture |
|---:|---|---|---|---:|---|
| 1 | **OE Solutions (138080.KQ)** | CPO ELSFP / émetteur-récepteur optique / puce laser | **La plus directe** | +307 % | Liste de surveillance cœur |
| 2 | Optocore | Émetteurs-récepteurs pour DC IA | Preuves contractuelles ; suspendu | +106 % | Non investissable |
| 3 | Daehan Optical Communications | Fibre et câble (matériaux en amont) | Bénéficiaire en aval, pas CPO | **+905 %** | Surchauffe ; avertissement KRX en escalade |
| 4 | BWE | Gamme d'émetteurs-récepteurs 800G / 1.6T | Produit divulgué ; client non confirmé | **+778 %** | Thématique haute volatilité |
| 5 | WooriRo | Photodétecteurs (composant cœur des émetteurs-récepteurs) | Stade développement technologique | **+616 %** | Option composant |
| 6 | Lycom | Amplificateurs optiques / connectivité DC | Bénéficiaire en aval | +98 % | En attente de catalyseur |
| 7 | Coset | Composants optiques (TOSA/ROSA) | Option petite capitalisation | -5 % | Liquidité insuffisante |

### 2.1 Ce que ce tableau révèle

**Premièrement, exposition CPO réelle et thématique optique IA sont deux objets distincts.** Seul OE Solutions dispose du produit source laser externe ELSFP. Les autres proposent des émetteurs-récepteurs (Optocore, BWE), de la fibre (Daehan Optical), des photodétecteurs (WooriRo), des amplificateurs (Lycom) ou des composants génériques (Coset). Tous se positionnent quelque part dans la chaîne de valeur optique IA au sens large, mais « fournisseur cœur CPO » et « valeur optique thématique » ne méritent pas le même multiple.

**Deuxièmement, six des sept affichent plusieurs centaines de pourcents de hausse YTD face à des pertes opérationnelles ou des victoires clients non vérifiées.** Daehan +905 %, BWE +778 %, WooriRo +616 %, OE Solutions +307 %. Le prix a bougé avant les résultats. Acheter ici n'est pas « la technologie est-elle juste ? » — c'est « le prix n'a-t-il pas déjà dépassé ce que les résultats peuvent jamais délivrer ? »

---

## 3. OE Solutions — la seule valeur véritablement proche du CPO

### 3.1 Structure commerciale

OE Solutions fabrique des émetteurs-récepteurs optiques et des puces laser. Fondée en 2003 par d'anciens de Bell Labs et Samsung Electronics avec une expérience en fabrication optique à grande échelle. Présence internationale : New Jersey et Californie (États-Unis), Pays-Bas, Japon.

Compétence cœur : **intégration verticale de la puce laser → sous-ensemble optique → émetteur-récepteur fini.** Dans un émetteur-récepteur optique, le laser est le « moteur » — la stabilité de sortie lumineuse, la gestion thermique et la durée de vie définissent le produit. OE Solutions développe la puce laser en interne.

### 3.2 Pourquoi l'ELSFP est le produit clé

Divulgué à l'OFC 2026 (mars) :

```
ELSFP compatible CPO d'OE Solutions :

- 23 dBm / 200 mW de puissance optique de sortie par canal
- TEC (refroidisseur thermoélectrique) intégré → stabilité de longueur d'onde + durée de vie du laser
- Configuration 8 canaux
- Échantillons clients prévus à partir de 3T26
```

Ce produit répond directement au problème d'isolation thermique du CPO — en éloignant le laser d'un ASIC de commutation chaud pour le placer sur le panneau avant. L'OIF définit le standard, et OE Solutions est la seule valeur coréenne cotée disposant du produit divulgué.

OE Solutions a également présenté à l'AI EXPO 2026 une **puce laser EML de classe 100G**, une première sur le marché domestique, source lumineuse fondamentale pour les émetteurs-récepteurs 800G/1.6T.

### 3.3 Les résultats n'ont pas rattrapé la technologie

C'est l'écart qui définit le trade.

| Indicateur | 2024 | 2025 | 2026E |
|---|---:|---:|---:|
| Chiffre d'affaires (mds KRW) | 32,0 | 57,4 | 81,6–83,5 |
| Bénéfice opérationnel (mds KRW) | -30,4 | -16,0 | 6,1–6,5 |
| Marge opérationnelle | -95 % | -28 % | 7–8 % |
| Part du revenu Datacom | — | **2 %** | encore faible |

Le chiffre d'affaires 2025 a rebondi de +79 % en glissement annuel mais est resté déficitaire. Le consensus 2026E table sur un retour aux bénéfices (BO ₩6,1–6,5 mds), mais la capitalisation boursière est d'environ ₩660 mds. Vérification rapide :

* Valeur d'entreprise ≈ capitalisation + dette nette = 660 + 20 = \~₩680 mds
* Sur un BO 2026E de ₩6,5 mds → **VE/EBIT ≈ 105×**

**Au prix actuel, vous payez environ 105× le bénéfice opérationnel 2026E.** Ce n'est pas une valorisation de « retour aux bénéfices en 2026 ». C'est une valorisation d'« inflexion des revenus optiques IA en 2027–2028 ».

### 3.4 La structure du chiffre d'affaires n'est pas encore centrée sur l'IA

Structure du chiffre d'affaires 2025 (estimations sell-side) :

| Segment | Part | Lecture |
|---|---:|---|
| Sans fil | 48 % | Cœur historique ; en reprise après le ralentissement post-5G |
| FTTH / MSO (accès filaire) | 23 % | Lié aux dépenses d'accès filaire japonaises / américaines |
| Longue distance (Télécom) | 21 % | Émetteurs-récepteurs longue distance 100G/400G |
| **Datacom** | **2 %** | **L'histoire IA n'est pas encore dans le chiffre d'affaires** |
| Puces laser | 6 % | Option technologique, volume encore contraint |

Qualifier ce dossier d'« entreprise CPO pour centres de données IA » va trop loin par rapport au compte de résultat actuel. Le cadrage exact est **« retournement de la reprise télécom avec une option d'appel CPO attachée ».**

### 3.5 Pourquoi est-elle numéro 1 ?

```
Ce que seule OE Solutions possède, par rapport aux six autres :

1. Produit CPO ELSFP divulgué — la seule
2. Puce laser EML 100G développée en interne — la seule
3. Intégration verticale : puce laser → sous-ensemble → module — la plus profonde du groupe
4. Historique avec des clients mondiaux d'équipements télécom (Cisco, Nokia, Ciena, etc.)
5. Empreinte opérationnelle internationale (États-Unis / Pays-Bas / Japon)
```

La mise en garde : la liste divulguée des partenaires CPO de Nvidia (TSMC, Coherent, Corning, Foxconn, Lumentum, Senko, Sumitomo, etc.) **n'inclut pas OE Solutions**. L'état exact est « la technologie est là, l'inclusion dans l'écosystème pas encore confirmée ».

### 3.6 Variables à surveiller

* **3T26** : Les échantillons clients ELSFP ont-ils été expédiés dans les délais ?
* **4T26 → 2027** : La qualification progresse-t-elle ? Des noms de clients sont-ils mentionnés ?
* **Part du Datacom** : Passe-t-elle matériellement au-dessus de 2 % ?
* **Marge brute** : Reprise depuis les 10,5 % de 2025 vers 20 %+ ?
* **Bénéfice opérationnel** : Le retour aux bénéfices 2026E s'est-il réellement concrétisé ?

---

## 4. Les six autres valeurs

### 4.1 Daehan Optical Communications — +905 % YTD, escalade vers l'avertissement d'investissement KRX

Daehan **n'est pas une société CPO.** C'est un fabricant intégré verticalement de préforme → fibre → câble — des matériaux en amont, non des moteurs optiques. Les centres de données IA consomment effectivement davantage de fibre haute densité, mais c'est une thèse de bénéficiaire en aval, pas du cœur CPO.

L'action sur le prix est le problème :

```
Daehan Optical Communications :
YTD : +905 %
3 mois : +610 %
1 semaine : +47 %
KRX : désigné valeur à surveiller le 2026-05-08 ; escalade vers l'avertissement en attente
```

Les flux étrangers ont été soutenus, mais le régulateur signale déjà le mouvement. **Acheter ici une valeur qui a décuplé YTD n'est pas un pari sur la demande de fibre — c'est parier sur « le prix peut-il encore s'étendre depuis une base ×10 ».**

### 4.2 BWE — +778 %, -36 % depuis le sommet

BWE a divulgué une gamme d'émetteurs-récepteurs 800G / 1.6T à l'AI EXPO. **Produit divulgué ≠ client qualifié.** Aucun client principal confirmé. En hausse de +778 % YTD, en baisse de -36 % depuis le sommet (8 100 → 5 200 wons). Actuellement en zone de digestion.

### 4.3 WooriRo — +616 %, poussée portée par le retail

A divulgué une technologie de photodétecteur 200 Gbps — composant potentiellement cœur pour les émetteurs-récepteurs 800G / 1.6T. Encore au stade développement ; qualification par un client mondial non vérifiée. Les achats nets cumulés penchent vers le retail. C'est un trade de momentum thématique, non une accumulation institutionnelle.

### 4.4 Lycom — +98 %, volume mort

Amplificateurs optiques pour la connectivité intra et inter-centres de données. Rapports de croissance des commandes à l'étranger. Plus proche de la périphérie optique IA que du cœur CPO. En hausse de +98 % YTD (la moins surchauffée des sept), mais le volume s'établit à 34 % de la moyenne sur 3 mois — sans nouveau catalyseur, elle stagne.

### 4.5 Optocore — suspension de cotation, non investissable

Les contrats d'émetteurs-récepteurs optiques pour centres de données IA d'environ ₩16,7 mds au total sont réels. Mais la cotation a été suspendue en mars 2026 sur une qualification d'audit de continuité d'exploitation, avec un risque de radiation. **Aucune action possible en tant que valeur cotée aujourd'hui.**

### 4.6 Coset — cotée sur KONEX, liquidité insuffisante

Fabricant de composants optiques TOSA/ROSA 400G+. Cotée sur le KONEX (le compartiment des plus petites capitalisations coréennes) ; le volume est trop faible pour une allocation normale. Liste de surveillance uniquement.

---

## 5. La surchauffe, en chiffres

### 5.1 Performance YTD

| Valeur | YTD | 3 mois | 1 semaine | Statut |
|---|---:|---:|---:|---|
| Daehan Optical | **+905 %** | +610 % | +47 % | Avertissement KRX en attente |
| BWE | **+778 %** | +321 % | +2 % | -36 % depuis le sommet, décélération |
| WooriRo | **+616 %** | +513 % | +7 % | Poussée portée par le retail |
| OE Solutions | **+307 %** | +232 % | +38 % | Ré-entrée institutionnelle ; encore cher |
| Optocore | +106 % | +14 % | — | Suspendu |
| Lycom | +98 % | +114 % | +2 % | Pas de volume |
| Coset | -5 % | +11 % | -13 % | Liquidité insuffisante |

### 5.2 La lecture en une ligne

**Quatre des sept valeurs progressent de plus de +300 % YTD sans aucun soutien des bénéfices.** OE Solutions a encore enregistré une perte opérationnelle de ₩16 mds en 2025. Daehan est rentable, mais pas suffisamment pour justifier un mouvement ×10 YTD. Le prix a largement devancé les fondamentaux.

Dans ce régime, la question déterminante n'est pas « la technologie est-elle juste ? » — c'est **« le prix n'a-t-il pas déjà anticipé plus que les bénéfices ne pourront jamais délivrer ? »**

---

## 6. Valorisation d'OE Solutions — ce que vous achetez réellement au prix actuel

### 6.1 Ce que le prix actuel implique

Capitalisation boursière \~₩660 mds, dette nette \~₩20 mds, VE \~₩680 mds.

Avec un multiple de sortie VE/EBIT de 30×, le bénéfice opérationnel requis pour justifier chaque niveau de prix :

| Prix | BO requis (à 30× VE/EBIT) | Vs. BO 2026E consensus |
|---:|---:|---|
| 53 300 (actuel) | **\~₩22,7 mds** | 3,5× le consensus |
| 60 000 (objectif sell-side) | \~₩25,4 mds | 3,9× le consensus |
| 70 000 | \~₩29,5 mds | 4,5× le consensus |
| 100 000 | \~₩41,9 mds | 6,4× le consensus |

**Même le prix actuel requiert un BO \~3,5× le consensus 2026E** pour se réconcilier avec un multiple de 30×. Ce n'est pas un chiffre 2026. C'est une inflexion des revenus optiques IA en 2027–2028.

### 6.2 Fourchettes de juste valeur par scénario

| Scénario | Hypothèse clé | Bénéfice opérationnel | Fourchette de juste valeur (KRW) |
|---|---|---:|---:|
| Baissier | Reprise télécom retardée, échantillons ELSFP décalés | ₩0–5 mds | 25 000–35 000 |
| Central | Retour aux bénéfices 2026, ELSFP au stade échantillon seulement | ₩6,1–6,5 mds | 30 000–45 000 |
| Haussier 1 | Montée en puissance des revenus Datacom 2027–2028 | ₩20–25 mds | 47 000–59 000 |
| Haussier 2 | Adoption clients ELSFP, marge brute 15 %+ | ₩30–40 mds | 71 000–111 000 |
| Ultra-haussier | Inclusion directe dans la chaîne CPO IA mondiale | ₩40 mds+ | 110 000+ |

**Le cours de clôture à 53 300 se situe entre Haussier 1 et Haussier 2** — prix intégrant déjà une valeur optionnelle CPO significative au-dessus de la base de reprise télécom. Si l'engagement clients ELSFP se matérialise en 3T, le prix s'étend. Dans le cas contraire, le niveau est exposé.

---

## 7. Cadre de positionnement — comment gérer les sept valeurs

| # | Valeur | Lecture | Justification |
|---:|---|---|---|
| 1 | **OE Solutions** | **Liste de surveillance cœur, attendre** | La pureté CPO la plus élevée ; prix déjà riche. Attendre le repli vers 47 000–50 000 ou la confirmation ELSFP en 3T |
| 2 | Lycom | En attente de catalyseur | Moins surchauffée, mais sans volume — nécessite un catalyseur commande ou divulgation client |
| 3 | Daehan Optical | **Ne pas courir après** | +905 % avec avertissement KRX en attente. Les détenteurs allègent ; nouvelles entrées inappropriées |
| 4 | BWE | Attendre le ré-dépassement | -36 % depuis le sommet ; pause jusqu'à confirmation client |
| 5 | WooriRo | Pas de nouvelle entrée | Retail-led ; technologie non vérifiée |
| 6 | Optocore | **Non investissable** | Cotation suspendue, risque de radiation |
| 7 | Coset | Observation uniquement | KONEX, liquidité insuffisante |

### 7.1 Conditions d'entrée sur OE Solutions

**Prix** : Premier intérêt dans la zone 47 000–50 000. Second intérêt à 43 000–45 000 (retest plus profond).

**Confirmation des résultats** :

* Impression de bénéfice opérationnel en 2T ou 3T (confirmation du retour aux bénéfices)
* Divulgation de l'expédition des échantillons clients ELSFP en 3T
* Part du Datacom en hausse matérielle

**Confirmation des flux** :

* Achats nets étrangers + institutionnels concomitants ≥ 3 séances
* Stabilisation de la cotation au-dessus du plus haut 52 semaines (57 900)

### 7.2 Conditions d'invalidation

* 2026 ne parvient pas à dégager un bénéfice
* Le calendrier des échantillons ELSFP en 3T est décalé
* Aucune mention de qualification client avant 4T
* La part du Datacom reste sous 10 %
* La marge brute ne parvient pas à dépasser 20 %

---

## 8. Trois points à dire sans détour

### 8.1 La plupart des sept sont des valeurs thématiques

Honnêtement : parmi les sept, presque aucune n'a de dossier validé par les résultats. OE Solutions était déficitaire en 2025, et les autres sont en position encore plus faible. **Des valeurs en hausse de plusieurs centaines de pourcents sans bénéfice opérationnel sont valorisées sur des anticipations, pas sur des réalisations.** Quand les anticipations ne se transforment pas en résultats, le prix rend les gains.

### 8.2 Aucune petite capitalisation coréenne ne figure sur la liste des partenaires CPO de Nvidia

Les partenaires CPO nommés de Nvidia : TSMC, Coherent, Corning, Foxconn, Lumentum, Senko, Sumitomo. Aucune petite capitalisation coréenne. Affirmer que « les sociétés coréennes sont dans la chaîne d'approvisionnement CPO » va trop loin. OE Solutions est la plus proche mais reste un **candidat**, pas une inclusion confirmée.

### 8.3 L'investissement dans l'optique a de longs délais de production

Les cycles de qualification des émetteurs-récepteurs optiques fonctionnent comme les semi-conducteurs : échantillon → qualification → adoption en conception → commande en volume → comptabilisation du chiffre d'affaires peuvent prendre 1 à 2 ans. Même si les échantillons 3T26 sont livrés dans les délais, les revenus en volume pourraient être de 2027–2028. Savoir si le cours de bourse attendra patiemment à travers cette fenêtre n'est pas prévisible à l'avance.

---

## 9. Rattachement à la série substrat

Ce billet s'inscrit dans le même cadre que la [série substrat](/page/korea-ai-pcb-substrate-hub/). La [thèse système-BOM](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) formulait l'argument structurel selon lequel **la demande IA est achetée sous forme de systèmes, pas de puces.** Ce système contient des couches de substrat, d'optique, de thermique et d'alimentation — toutes sous tension.

```
Goulots d'étranglement communs des systèmes IA :

Substrat (FC-BGA, MLB, CCL) — traité dans les billets sur 5 et 10 sociétés
Optique (modules 800G/1.6T, CPO ELSFP, fibre) — ce billet
Thermique (heat spreader, heat slug) — traité dans le billet Haesung DS
Alimentation (transformateurs, semi-conducteurs de puissance) — futur billet
Refroidissement (immersion, dissipateurs) — futur billet
```

Le [cadre des 10 sociétés](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) soutenait que la thèse de pénurie de substrat remonte vers les matériaux en amont. La même distinction s'applique ici — la fibre et le câble (Daehan Optical) sont des bénéficiaires en aval, tandis que le laser / la source laser externe (OE Solutions) se situe plus près du véritable goulot d'étranglement CPO.

La différence cruciale : **le cluster substrat a des résultats qui rattrapent le prix. Le cluster optique, non.** Le substrat, c'est « sélectionner les valeurs validées se traitant à des prix acceptables ». L'optique, c'est **« séparer le signal du bruit dans un rally pré-résultats surchauffé ».**

[Haesung DS](/post/haesung-ds-leadframe-ai-heat-spreader-second-source-2026-05-07/) offre le même contraste sur l'axe thermique : là, l'optionalité heat spreader IA repose sur une base réelle d'activités automotive-LF et de substrat DDR. Ici, cinq des sept valeurs optiques n'ont pas de base comparable — l'optionalité est essentiellement toute la thèse.

---

## 10. La conclusion

Que l'interconnexion optique soit le prochain goulot d'étranglement des centres de données IA est structurellement correct. Des dizaines de milliers de GPU ont besoin d'optiques 800G / 1.6T, et le CPO est la réponse architecturale crédible. La Corée compte sept expositions cotées.

Mais seule **une** des sept est genuinement proche du cœur CPO. OE Solutions dispose de la source laser externe ELSFP et de la puce laser EML 100G développée en interne. Les six autres sont des bénéficiaires en aval ou des paris thématiques. Et six sur sept affichent +300 % à +905 % depuis le début de l'année — Daehan Optical avec une escalade vers l'avertissement d'investissement KRX en plus.

OE Solutions elle-même se traite à \~105× le BO 2026E. La part du Datacom est de 2 %. 2025 était déficitaire. **Au prix actuel, vous pariez sur l'adoption clients CPO en 2027–2028, pas sur les résultats 2026.** Le point d'entrée propre se situe après la confirmation des échantillons clients ELSFP en 3T26 ou un repli vers 47 000–50 000 — observation plutôt que momentum.

« La technologie est juste » et « le prix est juste aujourd'hui » sont deux questions différentes. L'optique s'avérera très probablement être un véritable goulot d'étranglement des systèmes IA. Mais si le prix a déjà anticipé plusieurs centaines de pourcents, le rendement d'un allocataire est déterminé par le prix auquel il a acheté, non par la validité de la technologie.

---

## FAQ

**Q : Qu'est-ce que le CPO en une phrase ?**
R : Une nouvelle architecture de packaging qui place le moteur optique **directement à côté de l'ASIC de commutation** sur le même boîtier, réduisant drastiquement le chemin du signal électrique et la puissance par bit. Remplace les modules optiques enfichables en façade dans les commutateurs haute performance des centres de données IA.

**Q : Quelle valeur coréenne cotée est genuinement une société CPO ?**
R : **OE Solutions (138080.KQ)** est la seule à disposer d'un produit CPO-compatible divulgué — sa source laser externe ELSFP — ainsi que d'une puce laser EML 100G développée en interne. Elle **ne figure pas encore** sur la liste publique des partenaires CPO de Nvidia ou Broadcom, donc l'état exact est « candidat le plus proche », non « inclusion confirmée ».

**Q : Daehan Optical Communications n'est-elle pas un dossier CPO ?**
R : Non. Daehan est un fabricant de fibre optique et de câble intégré verticalement (préforme → fibre → câble). Les centres de données IA consomment effectivement davantage de fibre haute densité — c'est une thèse de bénéficiaire en aval — mais Daehan ne produit pas de composants cœur CPO (moteurs optiques, lasers, circuits intégrés photoniques).

**Q : Faut-il courir après OE Solutions à 53 300 ?**
R : Pas pour une position pleine. Le prix actuel représente \~105× le BO 2026E. Les entrées asymétriques sont : (a) un repli dans la zone 47 000–50 000, ou (b) la confirmation que les échantillons clients ELSFP 3T26 sont expédiés dans les délais. Courir après ici, c'est au plus une position pilote de 30 à 50 points de base.

**Q : Quelle valeur du groupe présente le risque le plus élevé ?**
R : Optocore est **non investissable** aujourd'hui (cotation suspendue sur audit de continuité d'exploitation). Daehan Optical affiche +905 % YTD avec une escalade vers l'avertissement KRX en attente. BWE et WooriRo progressent de plusieurs centaines de pourcents sur des bases clients non vérifiées. Aucune de ces valeurs ne convient comme nouvelle entrée.

**Q : Comment cela se compare-t-il aux valeurs coréennes du substrat IA ?**
R : Le cluster substrat a **des résultats qui rattrapent le prix**, donc le trade actionnable consiste à sélectionner des valeurs validées à des multiples acceptables. Le cluster optique a **le prix en avance sur les résultats**, donc le trade actionnable consiste à filtrer le signal du bruit thématique et à attendre les points de vérification. Même thèse système-BOM, deux stades différents du cycle.

**Q : Quand le dossier OE Solutions passe-t-il de « liste de surveillance » à « position cœur » ?**
R : Quand **deux des trois** conditions suivantes sont réunies : (1) 2026 dégager effectivement un bénéfice opérationnel, (2) les échantillons ELSFP 3T26 sont expédiés avec une mention de qualification client, (3) la part du Datacom progresse matériellement au-dessus de 2 %. Deux sur trois bascule ce dossier de l'observation à la position.

---

*Cet article est publié à des fins de recherche et d'information uniquement et ne constitue pas un conseil en investissement. Les données de prix, de flux et de résultats pour les sept valeurs ont été vérifiées auprès de KRX, Hankyung, Alpha Square et WiseReport. Les détails sur l'ELSFP et la puce laser d'OE Solutions sont issus des communications officielles de la société (OFC 2026, AI EXPO 2026), de la documentation standard OIF et de rapports sell-side (iM Securities, Meritz, Hana). Les références CPO de Nvidia et Broadcom proviennent des communications respectives adressées aux investisseurs. Optocore est actuellement suspendu sur un audit de continuité d'exploitation et n'est pas investissable. Daehan Optical Communications est en statut de vigilance d'investissement KRX avec escalade vers l'avertissement en attente. L'analyse peut se révéler incorrecte. Données arrêtées au 2026-05-08–09 KST.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
