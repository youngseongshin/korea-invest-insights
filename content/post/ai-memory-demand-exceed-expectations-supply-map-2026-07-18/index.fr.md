---
title: "La demande de mémoire pour l'IA dépassera-t-elle les attentes ? Lire les probabilités de surcroissance via les scénarios de demande et la carte de l'offre"
slug: "ai-memory-demand-exceed-expectations-supply-map-2026-07-18"
date: 2026-07-18T18:00:00+09:00
description: "La demande de mémoire pour l'IA devrait atteindre ou dépasser les fortes attentes actuelles, mais un large dépassement à la hausse n'est pas encore le scénario de base. Nous pondérons la demande par probabilité en scénarios de base, haussier et baissier (45/35/20), présentons six variables haussières et six risques baissiers, puis relions les goulets d'étranglement de l'offre par couche mémoire, les cartes d'expansion de Samsung, SK Hynix et Micron, et le fond de l'argument d'expansion du président Chey."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["Mémoire IA", "HBM", "DRAM", "Samsung Electronics", "SK Hynix", "Micron", "SOCAMM2", "Offre-Demande mémoire", "Expansion de capacité", "Cycle mémoire"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte
> Cet article traite de front le <strong>segment offre-demande 2026-2028</strong>, entre l'offre-demande de long terme à horizon 2030 traitée par [Recherche approfondie sur l'offre et la demande de HBM 2030](/fr/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/) et la valorisation calculée par [la juste valeur des semi-conducteurs](/fr/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/). À lire avec [Le vrai débat des semi-conducteurs : quatre horloges physiques et une horloge boursière](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/) et [La localisation de la mémoire en Chine et la Corée](/fr/post/china-memory-localization-exposure-samsung-hynix-micron-2026-07-18/). Les hubs associés sont [Hub AI HBM](/fr/page/korea-semiconductor-hbm-kospi-hub/) et [Hub Exclusive Analysis](/fr/page/exclusive-analysis-hub/).

## TL;DR

* <strong>La probabilité que la demande de mémoire pour l'IA atteigne ou dépasse les fortes attentes actuelles est élevée.</strong> Un large dépassement à la hausse n'est cependant pas encore le scénario de base.
* Le jugement probabiliste est le suivant. Conformité aux attentes <strong>45%</strong>, dépassement significatif <strong>35%</strong>, sous-performance <strong>20%</strong>. La probabilité que la croissance forte se poursuive est d'environ <strong>80%</strong>, celle d'un dépassement massif des attentes actuelles d'environ <strong>35%</strong>. \[Inférence : jugement de probabilité propre\]
* La clé d'une surcroissance n'est pas que « les serveurs IA se vendent beaucoup ». Il faut que <strong>le volume d'accélérateurs expédiés et la capacité mémoire par accélérateur augmentent tous deux plus que prévu, simultanément</strong>.
* Le vrai alpha asymétrique n'est pas la croissance du HBM elle-même. Cela, le marché le sait déjà. L'alpha, c'est <strong>de savoir si la demande se propage du HBM vers le DDR serveur, SOCAMM et eSSD, et si sa durée s'étend au-delà de 2028</strong>.
* L'argument d'expansion du président Chey Tae-won n'est pas une déclaration de baisse des prix à court terme, mais un message d'<strong>expansion de type préservation du marché et de prise de position anticipée sur la chaîne d'approvisionnement après 2028</strong>. Les perspectives de shortage 2026-2027 ne sont pas remises en cause, et le vrai risque de surcapacité se situe en 2028-2030, quand les nouvelles fabs atteignent toutes simultanément un rendement normalisé. \[Portée\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Thèse principale</div>
  <div class="thesis-callout__body">
    La mémoire IA connaît une forte croissance. Mais la prochaine condition de hausse du cours n'est pas la croissance des bénéfices de 2027, c'est la preuve que les bénéfices de 2028 ne se retournent pas. Ce qu'il faut regarder maintenant, ce n'est pas la croissance du HBM, mais si la demande se propage vers le DDR serveur, SOCAMM et eSSD tout en se prolongeant au-delà de 2028.
  </div>
</div>

---

## 1. Qu'est-ce qui est déjà attendu

Pour discuter d'un dépassement des attentes, il faut d'abord savoir ce que le marché attend déjà. Le niveau d'attente actuel est déjà élevé. \[Fait : synthèse des prévisions publiques\]

- Demande de HBM 2026, environ 2x
- Volume d'expéditions de serveurs IA 2026, hausse de plus de 20%
- Demande bit HBM 2027, +50-65%
- Part des wafers investis en HBM 2027, environ 30%
- Demande bit DRAM totale 2027, environ +20%

TrendForce estime que l'AI ASIC tirera la demande de HBM en 2026, puis que Rubin Ultra et l'AI ASIC la tireront ensemble en 2027. La capacité HBM par AI ASIC est elle aussi en hausse, passant de 96 Go · 192 Go à 216 Go · 288 Go. \[Fait : TrendForce\]

Un simple « les serveurs IA se vendent beaucoup » ne constitue donc pas un dépassement des attentes. Il faut que <strong>le volume d'accélérateurs expédiés et la capacité mémoire par accélérateur augmentent tous deux plus que prévu, simultanément</strong>.

---

## 2. Modèle de demande de base

Il est plus précis d'appréhender la demande de mémoire à travers la formule suivante.

```text
Demande bit HBM      = Volume d'accélérateurs IA expédiés × Nombre de stacks HBM par accélérateur × Capacité par stack
Demande DRAM serveur = Volume de serveurs expédiés × Capacité DRAM par serveur
Demande LPDDR        = Volume de mobiles · serveurs IA expédiés × Capacité LPDDR par appareil
```

### Scénario de base 2027

Le tableau ci-dessous est un modèle propre reliant les prévisions publiques à la feuille de route produit actuelle. Ce n'est pas un consensus officiel mais une estimation. \[Inférence : modèle propre\]

| Catégorie | Hypothèse de part DRAM bit | Hausse appareils·systèmes | Hausse capacité embarquée | Hausse demande bit |
|---|---:|---:|---:|---:|
| HBM | 18% | Accélérateurs IA +35% | Capacité par accélérateur +15% | environ +55% |
| DDR5 serveur · SOCAMM | 32% | Serveurs · CPU +12% | Capacité par serveur +10% | environ +23% |
| Mobile · PC · automobile | 50% | Appareils +2% | Capacité par appareil +5% | environ +7% |
| <strong>Somme pondérée</strong> | 100% | | | <strong>environ +21%</strong> |

Si le volume d'accélérateurs expédiés augmente de 35% et la capacité HBM de 15%, le bit HBM devient <strong>1,35 × 1,15 - 1 = +55,3%</strong>. C'est cette structure multiplicative qui explique pourquoi une hausse de seulement 20% des expéditions de serveurs peut suffire à faire croître la demande de HBM de plus de 50%.

Micron prévoit une croissance des expéditions de bits DRAM de l'industrie de l'ordre de low-to-mid 20% en 2026, avec une pénurie d'offre qui se prolongera au-delà de 2027. TrendForce estime également que la demande de HBM augmentera d'environ 2x en 2026 et que la part des wafers investis en HBM passera de 22% en 2026 à environ 30% en 2027. \[Fait : Micron · TrendForce\]

---

## 3. Trois scénarios de demande

Ces probabilités ne sont pas des probabilités statistiques, mais un jugement subjectif reflétant les commandes, le CAPEX et la feuille de route produit actuels.

| Scénario | Probabilité | DRAM bit 2027 | DRAM bit 2028 | Demande HBM | Moment d'assouplissement de l'offre |
|---|---:|---:|---:|---:|---|
| Base | <strong>45%</strong> | +20-23% | +17-21% | 2027 +50-65% | DRAM générique 2H27, HBM 2028 |
| Demande supérieure | <strong>35%</strong> | +28-32% | +25-30% | 2027 +70-85% | DRAM générique 2028, HBM 2029-30 |
| Demande inférieure | <strong>20%</strong> | +12-17% | +8-14% | 2027 +30-40% | DRAM générique 1H27, HBM 2H27-28 |

\[Inférence : estimation de scénarios\]

En additionnant la probabilité de conformité aux attentes (45%) et celle d'un dépassement significatif (35%), <strong>la probabilité que la croissance forte se poursuive est d'environ 80%</strong>. Mais la probabilité d'un dépassement massif des attentes actuelles n'est que d'environ 35%, ce qui signifie que la surcroissance n'est pas le scénario de base.

---

## 4. Six variables haussières qui accroissent la surcroissance

### ① Croissance conjointe des GPU et des ASIC (facteur haussier le plus fort)

Le marché considère l'ASIC comme un substitut à NVIDIA, mais pour les fabricants de mémoire, <strong>les deux sont des clients</strong>. Même si le TPU et Trainium peuvent réduire la part de marché des GPU, ils consomment tout de même du HBM ou de la DRAM serveur haute capacité.

```text
Hausse des GPU NVIDIA + hausse des TPU Google · Trainium AWS · ASIC Meta
→ Diversification de la clientèle HBM
→ Expansion de la demande bit HBM totale
```

Si l'on y ajoute le HBM4E à 16 couches et le HBM personnalisé (custom HBM), le chiffre peut dépasser les +55% calculés plus haut pour atteindre +70%. Les bénéficiaires les plus directs sont, dans l'ordre, <strong>SK Hynix > Samsung Electronics > Micron</strong>. Samsung Electronics dispose d'une option supplémentaire avec le HBM personnalisé pour les clients ASIC et sa propre base die de fonderie. \[Inférence : structure d'exposition\]

### ② Le goulot d'étranglement se propage du HBM à l'ensemble de la hiérarchie mémoire

Un serveur IA ne fonctionne pas avec le seul HBM.

- GPU · ASIC : HBM
- CPU · mémoire hôte : DDR5 · SOCAMM2
- Cache · stockage de données : Enterprise SSD
- Réseau · inférence bas coût : GDDR · LPDDR

En juillet 2026, SK Hynix a présenté non seulement le HBM, mais aussi SOCAMM2, DDR5, GDDR7, LPDDR et eSSD comme un portefeuille mémoire IA unifié. \[Fait : SK Hynix\] <strong>Même si les attentes sur le HBM déçoivent quelque peu, SOCAMM, le DDR serveur et l'eSSD peuvent croître davantage que prévu à sa place.</strong> C'est pourquoi nous estimons la probabilité de dépassement des attentes sur l'ensemble de la mémoire IA à environ 45%, un niveau supérieur au HBM seul. \[Inférence : diversification du portefeuille\]

### ③ SOCAMM2 forme une nouvelle strate de demande

SOCAMM2 n'est pas une simple bascule du LPDDR mobile existant vers le serveur. C'est un <strong>segment entièrement nouveau</strong> qui transforme la mémoire CPU et hôte des racks IA en une structure basse consommation et haute capacité. SK Hynix a démarré la production de masse du SOCAMM2 192 Go, et à mesure que son adoption se diffuse dans les CPU serveur et les racks IA, la demande de LPDDR5X augmente indépendamment du HBM. \[Fait : SK Hynix SOCAMM2\]

### ④ L'IA agentique stimule simultanément la DRAM serveur et l'eSSD

L'entraînement reste centré sur le HBM, mais l'inférence agentique sollicite plusieurs couches à la fois.

- HBM : calcul du modèle
- DDR5 · SOCAMM : mémoire CPU et système
- eSSD : base vectorielle, KV cache, stockage de données
- Mémoire tampon réseau

Lorsqu'un agent maintient un état et un contexte sur une longue durée, ce n'est pas seulement le nombre de tokens qui augmente, mais aussi la capacité mémoire embarquée par système. Dans ce cas, la DRAM serveur et l'eSSD peuvent se révéler plus fortes que prévu, davantage même que le HBM. \[Inférence : analyse de la charge de travail\]

### ⑤ La stratégie chinoise de puces basse performance augmente en réalité les volumes de mémoire

Si la Chine connecte davantage de puces basse performance à la place de GPU haute performance, il faut plus de puces, de serveurs et de mémoire pour un même volume de calcul. Le bénéfice direct pourrait se concentrer non pas sur le HBM haut de gamme, mais sur <strong>DDR5 · LPDDR5X · GDDR7 · HBM de milieu de gamme · eSSD</strong>. La croissance de l'IA chinoise peut abaisser le mix HBM, mais elle constitue un facteur haussier pour la demande bit DRAM totale. \[Inférence : architecture chinoise\]

### ⑥ Quand la hausse de l'usage dépasse les gains d'efficacité

La demande totale de mémoire est `charge de travail totale × usage mémoire par tâche`. Même si l'usage par tâche baisse de 40%, si l'usage de l'IA double, on obtient <strong>2,0 × 0,6 - 1 = +20%</strong>. La variable la plus déterminante aujourd'hui n'est pas la vitesse d'amélioration de l'efficacité des modèles, mais <strong>l'élasticité de l'usage des tokens et des agents face à la baisse des prix</strong>. C'est la condition sous laquelle l'efficacité devient un facteur d'expansion du marché plutôt qu'un facteur de baisse de la demande. \[Inférence : effet Jevons\]

---

## 5. Six risques de sous-performance par rapport aux attentes

### ① Échec de la validation du ROI du CAPEX IA (facteur baissier le plus important)

Si les investissements en data centers ne se convertissent pas en chiffre d'affaires et en flux de trésorerie liés à l'IA, les hyperscalers pourraient réduire leurs commandes en 2027-2028. Le moment le plus risqué est précisément 2028, l'année où l'offre augmente réellement.

```text
Ralentissement du CAPEX IA + mise en service de Samsung Electronics P5 · Micron ID2 · SK Hynix P&T7
→ Baisse simultanée de l'ASP du HBM et du prix de la DRAM générique
```

### ② L'amélioration de l'efficacité d'inférence l'emporte sur la hausse de l'usage

La quantification, le MoE, la compression et la réutilisation du KV cache, les petits modèles spécialisés, la hiérarchisation de la mémoire et le speculative decoding réduisent tous le besoin en mémoire par accélérateur. Si l'usage par tâche baisse de 60% tandis que le volume de tâches augmente de 30%, on obtient <strong>1,3 × 0,4 - 1 = -48%</strong>. Dans ce cas, même si l'usage de tokens augmente, la nouvelle demande de HBM et de serveurs reste sous les attentes. \[Inférence : scénario de dominance de l'efficacité\]

### ③ Hausse du taux d'utilisation des accélérateurs et recyclage du compute d'occasion

Les data centers IA actuels sont construits rapidement et l'optimisation du taux d'utilisation reste insuffisante. Si la planification et les échanges de compute entre clouds s'améliorent, l'offre de compute effectif augmente sans qu'il soit nécessaire d'ajouter de nouveaux GPU. Cela n'élimine pas la demande, mais retarde le moment de l'installation de nouveaux serveurs.

### ④ Goulot d'étranglement de l'électricité, du réseau de transport et du refroidissement

Même avec des commandes de puces et de mémoire, l'installation est retardée si l'alimentation électrique n'est pas raccordée. Cela relève davantage d'un <strong>report de la demande</strong> que de sa disparition, mais se traduit, pour les fabricants de mémoire, par une hausse des stocks et un ajustement des prix.

### ⑤ Destruction de la demande de PC et de smartphones

Si le prix de la mémoire monte trop, le prix des produits finis augmente et les ventes d'appareils reculent. C'est la raison directe pour laquelle le président Chey Tae-won a plaidé pour une expansion de l'offre. L'ordre d'ampleur de l'impact est <strong>LPDDR mobile > DDR PC > DDR serveur > HBM</strong>. Samsung Electronics est le plus sensible en volume absolu, tandis que SK Hynix, dont le mix HBM est plus élevé, est relativement plus défensif.

### ⑥ Hausse de l'offre chinoise

Si CXMT étend rapidement sa production de DDR5 et de LPDDR5X, le prix de la DRAM générique subit une pression avant le HBM. L'ordre d'impact est <strong>DDR4 · LPDDR4X > DDR5 · LPDDR5X > GDDR > SOCAMM > HBM</strong>. Même si la demande de HBM se maintient, les bénéfices de la DRAM générique peuvent ralentir en premier.

---

## 6. Le moment où l'offre se libère réellement : le fond de l'argument d'expansion de Chey Tae-won

Même si la demande est forte, le cours de l'action ne monte pas nécessairement. Ce qui compte, c'est l'offre et le prix. C'est là que les propos du président Chey Tae-won sur l'expansion de la production prennent toute leur importance.

### La définition précise de « l'assouplissement »

L'expression `assouplissement de l'offre 2028` évoquée par plusieurs analyses précédentes <strong>ne signifie pas une baisse des prix ni le début d'une surcapacité</strong>. Voici la définition précise.

- Les délais de livraison se raccourcissent
- Les volumes alloués aux clients augmentent
- Le taux de hausse des prix contractuels ralentit
- Le taux de croissance de l'offre se rapproche de celui de la demande

### La logique de Chey Tae-won est une expansion de préservation du marché

La logique du président Chey n'est pas une guerre des prix, mais la préservation du marché.

```text
Flambée des prix de la mémoire
→ Hausse des prix des PC et smartphones
→ Baisse de la demande de produits finis
→ Contraction du volume du marché mémoire
→ Entrée de puces propriétaires clients · mémoire de substitution · nouveaux fournisseurs
→ Érosion à long terme de la valeur de marché des 3 acteurs historiques
```

Omdia a d'ailleurs anticipé qu'en raison notamment de la hausse des prix de la mémoire, les expéditions de PC reculeraient de 12% et celles de smartphones de 7% en 2026. \[Fait : Omdia\] L'argument selon lequel, si les prix montent trop longtemps, les fabricants de mémoire finissent eux aussi par subir une baisse de volumes, est fondé.

Il faut cependant séparer deux affirmations. <strong>Que la pénurie d'offre 2027 puisse s'aggraver par rapport à 2026</strong> est un fait, tandis que <strong>la nécessité de construire de nouvelles fabs aux États-Unis</strong> relève de l'inférence. Le CEO de SK Hynix, Kwak Noh-jung, a lui-même indiqué que la demande pourrait dépasser la capacité d'offre au-delà de 2030, et Omdia situe un assouplissement significatif de l'offre après la fin de 2027. \[Fait : CEO de SK Hynix · Omdia\]

### Hypothèses de taux de croissance de l'offre

En convertissant le calendrier de mise en service par site en offre bit effective, on obtient approximativement ceci. \[Inférence : conversion propre\]

| Année | Hausse estimée de l'offre bit DRAM | Justification principale |
|---|---:|---|
| 2026 | +20-24% | Miniaturisation des procédés, M15X · Pyeongtaek · Micron 1γ |
| 2027 | +22-26% | Yongin Fab 1 en phase initiale, Idaho ID1, Tongluo |
| 2028 | +25-30% | Samsung Electronics P5, Micron ID2, SK Hynix P&T7 · Indiana |

Dans le scénario de demande de base, le taux de croissance de l'offre commence à dépasser celui de la demande d'environ 5-9 pp en 2028. Mais si le rendement des nouvelles fabs et la certification client prennent du retard, cet écart disparaît. <strong>Jusqu'en 2027, une zone où « les prix restent élevés malgré l'augmentation de la production » reste possible.</strong> C'est parce que les nouveaux wafers DRAM sont d'abord absorbés par la forte consommation de wafers du HBM. \[Inférence\]

---

## 7. Les strates de mémoire se disputent un même wafer

C'est le cœur physique de la question. HBM, DDR, LPDDR et GDDR <strong>se disputent la même capacité de wafer DRAM de pointe</strong>. Le NAND, lui, relève d'un procédé et de fabs séparés.

```text
Wafer DRAM de pointe ─┬─ Core die HBM ─────┐
                      ├─ DDR5 serveur       │
                      ├─ LPDDR5X/SOCAMM2    ├─ (HBM) TSV · empilement · packaging · test ─ HBM4/4E fini
                      └─ GDDR7              │
Procédé logique de pointe ── Base die HBM4 ┘
Fab de wafers NAND ── Enterprise SSD (filière séparée)
```

Micron a expliqué qu'à bit égal, le HBM3E consomme environ <strong>3x</strong> plus de wafers que le DDR5, et que ce ratio pourrait encore augmenter avec le HBM4. SK Hynix a également confirmé que le TSV agrandit la surface des die et accroît la complexité du rendement et du packaging, ce qui fait que le HBM nécessite davantage de wafers que la DRAM générique. \[Fait : Micron · SK Hynix\]

### Impact sur l'offre et les prix par strate

| Strate mémoire | Demande principale | Goulot d'étranglement de l'offre | Ordre de l'effet d'expansion | Résistance des prix |
|---|---|---|---|---|
| HBM4/HBM4E | GPU · ASIC IA | DRAM de pointe, base die, TSV, empilement, certification | Le plus tardif | La plus élevée |
| SOCAMM2 | Mémoire CPU serveur IA | LPDDR5X 1c, certification module · serveur | Intermédiaire | Élevée |
| DDR5 serveur | CPU · systèmes serveur IA | Wafer DRAM de pointe | Plus rapide que le HBM | Moyenne-haute |
| LPDDR5X mobile | Smartphones · IA embarquée | DRAM de pointe, élasticité mobile | Rapide | Moyenne |
| DDR4 · LPDDR4X | PC, mobile et industrie legacy | Réduction de production des 3 acteurs | Pénurie indépendante de l'expansion | Polarisée |
| GDDR7 | GPU · accélérateurs IA bas coût | DRAM de pointe, certification GPU | Intermédiaire | Moyenne-haute |
| NAND/eSSD | Stockage de données IA · KV cache | Wafer NAND, contrôleur | Séparé de la DRAM | Moyenne |

Un retournement intéressant mérite d'être noté. Selon une analyse de TrendForce, le chiffre d'affaires et la marge par wafer du DDR5 64 Go RDIMM ont dépassé ceux du HBM au premier trimestre 2026. Produire uniquement du HBM n'est donc pas toujours optimal, et si les prix montent suffisamment, les fabricants ont intérêt à réorienter des wafers vers le DDR5. <strong>Le premier mécanisme de baisse des prix pourrait être la normalisation de l'allocation existante des wafers, plutôt que l'arrivée de nouvelles fabs.</strong> \[Inférence : logique d'allocation des wafers\]

---

## 8. Carte d'expansion par société et par site

Ce qui compte, ce n'est pas le montant annoncé de l'expansion, mais <strong>quand, où et sous quelle forme de produit la capacité de wafer DRAM pure augmente réellement</strong>. \[Fait : annonces et publications de chaque société\]

| Société · site | Rôle | Calendrier | Produits directement concernés | Interprétation d'investissement |
|---|---|---:|---|---|
| SK Hynix Cheongju M15X | Front-end DRAM de pointe | Montée en cadence 2026 | Core die HBM · DDR5 · LPDDR | Hausse de volume la plus rapide |
| SK Hynix Cheongju M15 | Extension de capacité TSV | En cours | HBM | Combiné avec M15X |
| SK Hynix Cheongju P&T7 | WLP · test de wafers | WT 2027.10, WLP 2028.2 | Packaging HBM | Assouplissement du goulot 2028 |
| SK Hynix Yongin Fab 1 | Nouvelle fab de wafers | Achèvement visé 2027.5 | DRAM de pointe (estimé) | La production de masse suit l'achèvement avec retard |
| SK Hynix Indiana | Packaging HBM avancé | S2 2028 | HBM nouvelle génération | Pas une expansion de wafers |
| SK Hynix Cheongju M17 | Front-end NAND | Non communiqué | NAND · eSSD | Séparé du HBM |
| Samsung Electronics Pyeongtaek (site existant) | DRAM 1c · HBM4 | Production de masse actuelle | HBM4 · DDR5 | Objectif de CA HBM x3 en 2026 |
| Samsung Electronics Pyeongtaek P5 | Nouveau pôle HBM | Mise en service visée 2028 | HBM · DRAM de pointe | Expansion de l'offre après 2028 |
| Samsung Electronics Onyang · Cheonan | Packaging · test HBM | Non communiqué | HBM4/4E | Plan de 5 lignes à Onyang |
| Micron Hiroshima | DRAM EUV 1γ | Déjà en montée en cadence | HBM4E · DDR5 · LPDDR | Amélioration du coût de pointe |
| Micron Taiwan/Tongluo | Front-end DRAM | Mi-2027 | HBM · DDR · LPDDR | Premier volume nouveau significatif |
| Micron Singapore | Packaging HBM | 1S 2027 | HBM | Assouplissement du goulot de packaging |
| Micron Idaho ID1/ID2 | Nouvelle fab DRAM | Mi-2027 / premier wafer fin 2028 | DRAM de pointe | Prime de chaîne d'approvisionnement américaine |
| Micron Virginia | DRAM legacy | 2026 | DDR4 | Longévité industrielle et défense |

SK Hynix P&T7 est une installation dédiée au WLP et au test HBM d'environ 19 billions KRW, et Indiana est une installation de packaging HBM de 3,87 Mds USD. Samsung Electronics a désigné Pyeongtaek P5 comme son pôle HBM pour 2028 et a annoncé 5 lignes à Onyang ainsi que la modernisation de Cheonan. Il faut cependant noter que les 140 billions KRW de la région de Chungcheong constituent <strong>un montant global du groupe</strong>, incluant l'affichage, les batteries et les substrats, et ne doivent donc pas être lus comme un montant d'investissement dédié au HBM. \[Fait : annonces de chaque société\]

### Le moment où l'offre se libère réellement

| Période | Évolution de l'offre | Impact sur les prix |
|---|---|---|
| 2026 | Conversion des fabs existantes, montée en cadence des nœuds de pointe M15X · Pyeongtaek · Micron | La hausse du HBM continue d'empiéter sur l'offre de DDR |
| 2027 | Yongin Fab 1, Idaho ID1, Tongluo, packaging Singapore | Normalisation partielle possible du DDR5 · LPDDR |
| 2028 | Samsung Electronics P5, SK Hynix P&T7 · Indiana, Micron ID2 | Début de l'assouplissement de la pénurie de HBM |
| 2029-2030 | Rendement normalisé des nouvelles fabs, investissements additionnels aux États-Unis et à Honam | Risque de surcapacité si la demande IA ralentit |

<strong>Les perspectives de pénurie de mémoire pour 2026-2027 ne sont pas remises en cause.</strong> Le vrai risque de surcapacité se situe en 2028-2030, lorsque les nouvelles fabs atteignent toutes simultanément un rendement normalisé.

---

## 9. Que faut-il vérifier

Voici les indicateurs clés pour distinguer un scénario haussier d'un scénario baissier de la demande.

| Indicateur | Signal de dépassement de la demande | Signal de sous-performance de la demande |
|---|---|---|
| Volume d'expéditions de serveurs IA | +25% ou plus en glissement annuel | 15% ou moins |
| Demande bit HBM | Maintien au-dessus de +60% | 40% ou moins |
| Part des wafers HBM | Supérieure à 30% en 2027 | 27% ou moins |
| Demande AI ASIC | Hausse conjointe de TPU · Trainium · ASIC Meta | Se limite à une substitution de NVIDIA |
| CAPEX des hyperscalers | Révisions à la hausse supplémentaires | Révisions à la baisse chez 2 sociétés ou plus |
| Contrats HBM | Extension des pré-contrats sur les volumes 2028 | Raccourcissement de la durée des contrats, renégociation des prix |
| DDR5 RDIMM | Hausse conjointe du prix et du volume | Baisse sur 2 trimestres consécutifs |
| SOCAMM2 | Adoption par plusieurs CSP et plateformes CPU | Dépendance à une seule plateforme |
| Calendrier électricité · data centers | Accélération des installations | Retards de raccordement et d'achèvement |
| Jours de stock | Stocks clients stables | Hausse des stocks plus rapide que le chiffre d'affaires |

---

## 10. Jugement d'investissement sur Samsung Electronics, SK Hynix et Micron

La date de référence de la base de données locale est le 2026-07-16 pour Samsung Electronics et SK Hynix, et le 2026-07-17 pour Micron.

| Société | Cours actuel | PER FY27/Next FY | Effet positif de l'expansion de production | Risque clé |
|---|---:|---:|---|---|
| Samsung Electronics | 255 000 KRW | 3,88x | Reconquête de part de marché HBM, mix produit le plus large | Sensibilité au prix de la DRAM générique |
| SK Hynix | 1 842 000 KRW | 4,20x | Pureté HBM · SOCAMM et effet de levier du taux d'utilisation | CAPEX massif et ROIC après 2028 |
| Micron | 848,95 USD | 5,64x | Implantation locale aux États-Unis, croissance simultanée du HBM · DDR · eSSD | Coûts élevés des fabs américaines, prime de multiple relative |

\[Fait : cours et consensus de la base de données locale\]

Ces PER ne sont pas un signal de « valorisation bon marché », mais <strong>la décote appliquée par le marché à l'idée que le bénéfice 2027 pourrait constituer un pic</strong>. Un PER 2027E bas, entre 4 et 6x, signifie que le marché a déjà intégré dans le prix le pic de bénéfice et la normalisation de 2028.

En classant par capacité, voici l'ordre obtenu. \[Inférence : classement relatif\]

- Élasticité des bénéfices 2026-2027 : <strong>SK Hynix > Micron > Samsung Electronics</strong>
- Marge de révision à la hausse des estimations liée à la reconquête de part de marché HBM : <strong>Samsung Electronics > Micron > SK Hynix</strong>
- Capacité de défense face à une surcapacité après 2028 : <strong>Samsung Electronics > Micron > SK Hynix</strong>
- Élasticité du cours si la pénurie de HBM se prolonge jusqu'en 2030 : <strong>SK Hynix > Micron > Samsung Electronics</strong>

### Conclusion par scénario

- <strong>En cas de dépassement de la demande</strong> : upside maximal pour SK Hynix, élasticité de révision à la hausse maximale pour Samsung Electronics
- <strong>Scénario de base</strong> : Samsung Electronics en tête pour l'attrait ajusté du risque, SK Hynix en Core Hold
- <strong>En cas de sous-performance de la demande</strong> : Samsung Electronics relativement défensif, ampleur de révision à la baisse des bénéfices accrue pour SK Hynix et Micron
- <strong>Condition d'abandon de la thèse</strong> : si les prévisions de demande bit HBM 2027 tombent sous +40% tout en confirmant simultanément une baisse du CAPEX des hyperscalers et une hausse des stocks clients

### Ce que dit la réaction du cours

| Titre | 15/07 | 16/07 | Dernier cours de clôture |
|---|---:|---:|---:|
| Samsung Electronics | +6,27% | -8,77% | 255 000 KRW |
| SK Hynix | +8,83% | -11,53% | 1 842 000 KRW |
| Micron | -8,02% | -5,65% | 848,95 USD |

Samsung Electronics et SK Hynix ayant grimpé le jour même des propos du président Chey avant de chuter brutalement le lendemain, <strong>il est difficile de voir dans ces propos un catalyseur de vente direct</strong>. La chute du 16 juillet a résulté de l'action combinée de Kimi K3, des inquiétudes sur le rendement du CAPEX IA, de l'IPO de CXMT et des débouclages de positions consécutifs à la flambée précédente. \[Inférence : facteurs combinés\]

---

## Conclusion

Pour revenir à la question initiale, voici la réponse. La probabilité que la demande de mémoire pour l'IA atteigne ou dépasse les fortes attentes actuelles est élevée (croissance forte, 80%). Mais un large dépassement n'est pas encore le scénario de base (surcroissance, 35%).

La trajectoire la plus probable est la suivante. La pénurie de HBM se prolonge jusqu'en 2027, la demande se propage vers SOCAMM, DDR5 et eSSD, et la nouvelle capacité de 2028 augmente sans basculer immédiatement en surcapacité. Au-delà de 2028, il faudra revérifier la rentabilité réelle du CAPEX IA et le taux de croissance de l'offre.

Le cœur de la perspective d'investissement n'est pas que « le HBM croît ». Cela, le marché le sait déjà. <strong>Le vrai alpha asymétrique réside dans le fait de savoir si la demande se propage du HBM vers le DDR serveur, SOCAMM et eSSD, et si sa durée s'étend au-delà de 2028.</strong>

La logique d'expansion du président Chey est industriellement fondée. Préserver le marché client et la marge de tolérance politique sert mieux la valeur d'entreprise à long terme que de maximiser les prix actuels. Pour l'investisseur, elle est à double tranchant. Jusqu'en 2027, c'est une déclaration haussière qui confirme une pénurie d'offre sévère. Après 2029, c'est en revanche une déclaration baissière qui annonce la normalisation du CAPEX, des amortissements et de l'ASP. Ce n'est pas un motif de vente immédiate, mais l'argument permettant d'évaluer les trois acteurs de la mémoire comme des entreprises à marge élevée permanente s'en trouve lui aussi affaibli.

La conclusion actuelle est donc que <strong>la thèse de shortage est maintenue jusqu'en 2027, avec une réévaluation à partir de 2028</strong>. La prochaine condition de hausse du cours n'est pas la croissance des bénéfices de 2027, c'est la preuve que les bénéfices de 2028 ne se retournent pas.

---

_Cette publication est une analyse d'offre-demande et d'investissement combinant les prévisions publiques (TrendForce, Omdia), les annonces et publications des entreprises (Micron, SK Hynix, Samsung Electronics) et les cours et consensus de la base de données locale. Les probabilités des scénarios de demande, les taux de croissance de l'offre et le modèle de base 2027 sont des estimations propres arrêtées au moment de la rédaction, non un consensus officiel. Les volumes mensuels de wafers investis par fab, les taux d'allocation de wafers par produit, les prix et volumes des contrats long terme de HBM, et le calendrier des nouvelles fabs américaines ne peuvent pas être confirmés par des sources publiques. Les titres mentionnés sont des exemples destinés à illustrer la structure industrielle et ne constituent pas une recommandation d'achat ou de vente d'un titre particulier. La décision d'investissement et sa responsabilité incombent à l'investisseur lui-même._

---

### Articles associés

- [Recherche approfondie sur l'offre et la demande de HBM 2030 : disséquer le modèle de demande de 26,7EB face au calendrier de capacité](/fr/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
- [Les semi-conducteurs sont-ils cycliques et quelle est la juste valeur ? Valoriser Samsung, SK Hynix et Micron avec le FCFE et les bénéfices normalisés](/fr/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [Le vrai débat des semi-conducteurs : quatre horloges physiques et une horloge boursière](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [La localisation de la mémoire en Chine et la Corée : décomposer l'exposition à la Chine de Samsung, SK Hynix et Micron](/fr/post/china-memory-localization-exposure-samsung-hynix-micron-2026-07-18/)
- [SK Hynix abaisse ses bénéfices du T2 mais maintient ses objectifs de cours : synthèse des rapports Mirae Asset et KIS](/fr/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/)
