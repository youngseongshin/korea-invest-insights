---
title: "Ce que change vraiment la convergence des modèles ouverts chinois : redistribution de la chaîne de valeur, pas effondrement de la demande"
slug: "china-open-model-convergence-value-chain-redistribution-2026-07-17"
date: 2026-07-17T22:00:00+09:00
description: "Les modèles ouverts chinois convergent vers la performance frontière américaine tout en étant servis sur une infrastructure d'inférence chinoise. Il s'agit d'une redistribution de la chaîne de valeur plutôt que d'un effondrement de la demande en IA. La valeur de monopole des API de modèles et des GPU de pointe recule, tandis qu'une inférence moins chère augmente le volume de tokens et peut valoriser la mémoire, le stockage, les réseaux, l'énergie et la distribution cloud."
categories: ["Exclusive Analysis", "AI Infrastructure", "Market-Outlook"]
tags: ["Modèles ouverts chinois", "DeepSeek", "Kimi K3", "Qwen", "CXMT", "HBM", "Samsung Electronics", "SK Hynix", "Micron", "NVIDIA", "Politique IA"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte
> Cet article fait suite à [Kimi K3 Réinitialise la Courbe de Prix de l'IA](/fr/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/). Si le précédent article vérifiait le prix et la structure d'<strong>un seul modèle</strong>, celui-ci élargit la focale à la manière dont <strong>l'ensemble de l'écosystème des modèles ouverts chinois</strong> redistribue la chaîne de valeur des semi-conducteurs et de la Big Tech, et à la façon dont la politique américaine et le conflit sino-américain modifient cette lecture. À lire avec [Le vrai débat des semi-conducteurs](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/), [la juste valeur des semi-conducteurs](/fr/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/) et [IPO de CXMT et risque sur les prix mémoire](/fr/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/). Les hubs associés sont le [Hub AI HBM](/fr/page/korea-semiconductor-hbm-kospi-hub/) et le [Hub Exclusive Analysis](/fr/page/exclusive-analysis-hub/).

## TL;DR

* La convergence de performance des modèles ouverts chinois relève davantage d'une <strong>redistribution de la chaîne de valeur que d'un effondrement de la demande en IA</strong>. La valeur de monopole des API de modèles et des GPU de pointe recule, tandis qu'une inférence moins chère augmente les volumes d'usage et peut valoriser la mémoire, le stockage, les réseaux, l'énergie et la distribution cloud.
* Les préférences relatives se répartissent ainsi. Pour la mémoire coréenne, <strong>Samsung Electronics > SK Hynix</strong> ; pour les semi-conducteurs américains, <strong>Micron, SanDisk > NVIDIA</strong> ; pour la Big Tech, <strong>Meta, Amazon > Google, Microsoft > les purs acteurs de modèles</strong>. \[Inférence : jugement relatif\]
* Les modèles ouverts chinois ont démontré une <strong>baisse du coût de calcul et de mémoire par unité d'intelligence</strong>. Ils n'ont pas démontré de <strong>baisse des dépenses totales en silicium</strong>. TSMC a au contraire relevé son CAPEX 2026 de 52-56 à 60-64 milliards de dollars.
* Sur le HBM, CXMT accuse un retard de <strong>1,5-2 générations</strong> en termes de produit et de 2-3 ans en termes de commercialisation par rapport aux trois leaders. La menace de 2028 est donc une <strong>option conditionnelle</strong>, pas un choc d'offre actuel.
* La <strong>diffusion technologique</strong> des modèles chinois et la <strong>diffusion du chiffre d'affaires</strong> des opérateurs d'API chinois sont deux choses distinctes. Le chemin le plus réaliste consiste à réhéberger les modèles chinois sur AWS, Azure ou dans un VPC d'entreprise, puis à les vendre via les dispositifs de sécurité et de contrat occidentaux. \[Portée\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Thèse principale</div>
  <div class="thesis-callout__body">
    Les modèles chinois peuvent ébranler le prix des modèles américains, mais ils ne font pas s'effondrer immédiatement la demande d'AWS, d'Azure, des puces américaines et de la mémoire coréenne. Le dommage direct touche la marge des API de modèles fermés. Ce qui survit durablement, ce sont la couche de distribution cloud et de sécurité, ainsi que l'infrastructure fondée sur l'usage (mémoire, réseau, énergie).
  </div>
</div>

---

## 1. D'abord, vérifier les faits

La direction générale de l'écosystème est la bonne, mais <strong>le matériel d'entraînement de tous les nouveaux modèles n'a pas été rendu public</strong>. Cette distinction compte.

DeepSeek-V3 a été entraîné avec <strong>2 048 NVIDIA H800</strong> et 2,788 millions d'heures GPU. \[Fait : rapport technique DeepSeek V3\] Le H800 est soumis à des restrictions d'exportation, mais ce n'est pas un GPU grand public bas de gamme. Kimi K3, de son côté, a annoncé 2,8 billions de paramètres, un contexte d'un million de tokens et une efficacité d'extension 2,5x supérieure à K2, mais <strong>le rapport technique complet et le matériel d'entraînement ne seront publiés que le 27 juillet</strong>. \[Fait : annonce officielle de Kimi\]

On ne peut donc pas encore affirmer que « Kimi K3 a lui aussi été entraîné sur des GPU NVIDIA bas de gamme ». \[Non vérifié\]

### Les gains d'efficacité sont réels

DeepSeek V4-Pro n'active que <strong>49 milliards de paramètres</strong> sur un total de 1,6 billion. Sur une fenêtre de 1 million de tokens, le calcul par token tombe à <strong>27%</strong> et le KV cache à <strong>10%</strong> du niveau de V3.2. \[Fait : fiche modèle DeepSeek V4\] C'est une preuve directe qu'il est possible de réduire fortement l'usage de GPU et de HBM par token tout en maintenant la performance.

### Mais l'autre versant est tout aussi réel

Le CloudMatrix384 de Huawei assemble 384 Ascend 910C pour servir DeepSeek-R1. Selon les données compilées par JPMAM, CloudMatrix consomme 49 To de HBM et 599 kW, contre 21 To et 145 kW pour le GB300 NVL72 utilisé en comparaison. \[Fait : article CloudMatrix, données comparatives JPMAM\]

Ce n'est pas une comparaison de performance strictement équivalente, mais la direction est claire : la Chine compense la faiblesse de la puce unitaire par <strong>davantage de puces, de mémoire et d'énergie</strong>. Une puce individuelle moins chère ne signifie pas nécessairement moins de silicium, de réseau et d'énergie au total. \[Inférence : interprétation structurelle\]

---

## 2. L'équation clé : que faut-il regarder

La réponse à ce débat ne se trouve pas dans les scores de benchmark, mais dans deux équations.

```text
Demande de calcul totale = nombre total de tokens × calcul par token

Demande de mémoire totale = nombre total de tokens × usage mémoire par token
                           + volume stocké de modèle, de KV cache et de données de recherche
```

Si un modèle ouvert fait baisser le prix du token de 70% tout en multipliant l'usage par 5, la <strong>demande totale augmente</strong> malgré le gain d'efficacité. À l'inverse, si le HBM par token diminue de 70% pendant que l'usage ne fait que doubler, <strong>la demande de HBM recule</strong>.

L'indicateur à surveiller se résume donc à une seule question : <strong>de combien le taux de croissance des tokens dépasse-t-il le taux de baisse de la mémoire par token.</strong>

### Le verdict à ce jour

La dépense totale est déterminée par l'équation suivante.

```text
Dépense totale en silicium = nombre de sessions d'entraînement × coût par session
                            + nombre de tokens d'inférence × coût par token
```

Lors de son call du 2T26, TSMC a relevé son CAPEX 2026 de 52-56 à <strong>60-64 milliards de dollars</strong>. Microsoft, de son côté, a augmenté son débit d'inférence de 40%, mais l'usage de tokens de ses grands clients a progressé de <strong>30%</strong> en séquentiel, et l'entreprise a maintenu son CAPEX 2026 à environ 190 milliards de dollars. \[Fait : call 2T26 de TSMC, call T3 FY26 de Microsoft\]

<strong>À ce jour, la croissance de l'usage l'emporte sur les gains d'efficacité.</strong> \[Inférence : synthèse des données\]

---

## 3. Impact sur les semi-conducteurs : la dispersion par valeur

| Valeur / groupe | Impact sur le cours | Lecture clé |
|---|---|---|
| Samsung Electronics | Positif | Bénéficie le plus largement : pas seulement le HBM, mais aussi la DRAM serveur, le NAND/eSSD et la mémoire générique |
| SK Hynix | Mixte à positif | La hausse des tokens est favorable, mais la compression MoE/KV réduit le HBM par token, ce qui pèse sur le multiple de rareté |
| Micron | Positif | Exposition combinée DRAM, HBM, NAND dans la chaîne d'approvisionnement américaine. Bénéfice broad-memory comparable à Samsung |
| SanDisk | Positif | Le déploiement local, les poids de modèles et la hausse du RAG/cache alimentent la demande d'eSSD et de NAND |
| NVIDIA | Négatif à court terme, mixte à long terme | Recul de la part de marché chinoise et de la valeur de monopole des GPU haut de gamme. La hausse du volume total de tokens et les livraisons de H200 compensent en volume |
| AMD | Relativement positif | Les modèles ouverts facilitent la portabilité vers du matériel hétérogène. ROCm et la part de marché réelle de service seront déterminants |
| Broadcom, Marvell, Arista | Positif à moyen terme | Demande croissante d'ASIC sur mesure occidentaux, d'Ethernet, d'optique et de SerDes |
| TSMC | Neutre à positif | La demande de puces d'entraînement NVIDIA/AMD/ASIC se maintient, mais l'inférence chinoise se déplace vers Ascend et SMIC |

### Pourquoi Samsung est relativement avantagé par rapport à SK Hynix

Bien qu'elles appartiennent au même trio des grands acteurs de la mémoire, <strong>Samsung Electronics et SK Hynix divergent</strong>. L'inférence bon marché et la diffusion des modèles ouverts n'augmentent pas seulement le HBM : elles augmentent aussi le volume total de DRAM serveur, de NAND et de mémoire générique. Samsung Electronics, dont l'exposition est plus large, capte une plus grande part de cette diffusion.

À l'inverse, le MoE et la compression KV réduisent le <strong>HBM par token</strong>. SK Hynix, dont l'exposition est concentrée sur le HBM pur, subit à la fois le bénéfice de la hausse des tokens et le poids de la baisse du HBM par token. C'est le <strong>multiple de rareté</strong>, plus que la demande absolue, qui est comprimé en premier. \[Inférence : analyse de la structure d'exposition\]

Samsung Electronics fait toutefois face à un risque inverse : elle est la première exposée à la montée en volume de la DRAM générique de CXMT.

### NVIDIA et le H200

Les États-Unis ont récemment commencé à autoriser des expéditions limitées de H200 vers la Chine, mais les volumes restent faibles pour l'instant. C'est positif pour le chiffre d'affaires de NVIDIA à court terme, mais pas au point d'inverser la bascule vers une infrastructure domestique centrée sur Huawei. \[Fait : article Reuters, juillet 2026\] \[Inférence : évaluation d'impact\]

---

## 4. Impact sur la Big Tech

| Entreprise | Jugement | Raison |
|---|---|---|
| Meta | Le plus positif | Sa stratégie d'écosystème ouvert est validée ; elle capte la valeur de l'IA via la publicité et les recommandations plutôt que via les API |
| Amazon | Positif | Quel que soit le modèle gagnant, AWS vend de l'inférence, du stockage et du réseau |
| Google | Mixte à positif | TPU et cloud en bénéficient, mais la prime de prix de l'API Gemini est sous pression |
| Microsoft | Mixte | L'usage d'Azure progresse, mais la redevance des modèles OpenAI et le taux de retour sur CAPEX sont sous pression |
| Apple | Positif | Les petits modèles ouverts bon marché réduisent le coût de l'on-device et du Private Cloud |
| OpenAI, Anthropic | Négatif | Réduction de l'écart de performance et de la prime de prix des API, pression sur des valorisations et des levées de fonds élevées |

<strong>Contrairement à une idée reçue, Meta n'est pas la plus grande perdante.</strong> L'entreprise gagne de l'argent via la publicité et les recommandations plutôt que via la vente de modèles, et utilise les modèles ouverts pour réduire ses coûts, ce qui lui donne un potentiel de gain relatif. La pression se situe plutôt du côté du CAPEX et de l'amortissement. \[Inférence : analyse du modèle économique\]

### La leçon du choc DeepSeek de 2025

Lors du choc DeepSeek de 2025, NVIDIA a perdu <strong>17% de sa capitalisation boursière en une seule journée, soit environ 593 milliards de dollars</strong>. La réaction initiale a été une vente généralisée touchant l'ensemble de l'infrastructure GPU, énergie et data centers, avant un rebond partiel. \[Fait : couverture médiatique, 2025\]

Cette fois encore, il est probable que <strong>le cours réagisse à court terme à la peur de l'efficacité, et les résultats à moyen terme à la hausse de l'usage</strong>. \[Inférence : schéma historique\]

---

## 5. Verdict sur les thèses relatives aux modèles ouverts chinois

Voici, un par un, le verdict sur les arguments avancés par les haussiers comme par les baissiers.

| Argument | Verdict |
|---|---|
| Les GPU haut de gamme sont indispensables à la performance frontière | Affaibli, mais non réfuté |
| L'intelligence IA est un bien rare | Largement invalidé au niveau du prix brut des modèles et des tokens |
| L'échelle du capital constitue une douve | La douve du pré-entraînement s'affaiblit ; elle se déplace vers le déploiement, les données, l'énergie et la distribution |
| Le coût marginal de l'open source est nul | Seul le prix des poids tend vers zéro, le coût d'inférence continue de courir |
| Un entraînement à 1 milliard de dollars dépasserait un investissement de 100 milliards de dollars | Argument inexact qui compare deux catégories de coûts différentes |

Ce dernier point est particulièrement souvent mal utilisé. Le coût d'entraînement et l'investissement total en infrastructure ne sont pas des catégories comparables.

---

## 6. Où en est vraiment le HBM de CXMT

C'est le point le plus souvent exagéré dans le débat sur la menace chinoise. Décomposé étape par étape, le tableau réel apparaît.

| Étape | Verdict actuel | Base du jugement |
|---|---|---|
| Procédé de cellule DRAM | Commercialisé, progression rapide | Vente de DDR5/LPDDR5X ; Apple teste aussi de la DRAM chinoise pour ses produits |
| Empilement TSV | HBM2 en petits volumes, HBM3 à un stade précoce | Une production de HBM2 est rapportée, mais volumes et rendement restent non divulgués |
| Packaging et base die | En cours de construction | L'écosystème chinois se forme, mais les données de rendement en production de masse, thermiques et de fiabilité manquent |
| Qualification client | HBM non confirmé | Le contrat avec Tencent et les tests d'Apple ne prouvent que la capacité en DRAM générique |
| Écart avec les leaders | 1,5-2 générations | Les trois leaders sont déjà en montée en cadence sur le HBM4, alors que CXMT n'a même pas encore validé la production de masse du HBM3 |

Au 17 juillet 2026, la gamme de produits officiellement publiée par CXMT se limite à DDR5, LPDDR5/5X, DDR4 et LPDDR4X : <strong>il n'y a pas de HBM</strong>. TrendForce classe également le HBM3 de CXMT en phase de validation précoce et estime que les barrières technologiques et l'obligation d'utiliser des équipements domestiques retardent la production de masse. \[Fait : documents officiels de CXMT, TrendForce\]

Les estimations de capacité divergent elles aussi. Un plateau autour de 240 000 wafers par mois s'oppose à une prévision de 350 000 en fin d'année. Mais ce chiffre de 350 000 provient d'un modèle privé et non d'une guidance de l'entreprise, ce qui le rend difficile à retenir comme valeur confirmée. \[Non vérifié\]

### Comment corriger l'hypothèse sur la DRAM legacy

- <strong>2026-2027</strong> : les investissements HBM de CXMT <strong>retardent</strong> le relâchement de l'offre de DRAM legacy chinoise.
- <strong>2028</strong> : si le HBM3/3E obtient la qualification des clients accélérateurs chinois et des volumes significatifs, il pourrait d'abord remplacer le marché chinois du HBM ancienne génération.
- <strong>2029 et après</strong> : il faudra que le HBM4, le base die et le rendement de packaging suivent pour que la pression touche directement le marché mondial leader et la marge de SK Hynix.

Autrement dit, l'affirmation la plus juste n'est pas « CXMT va immédiatement aggraver la pénurie de legacy », mais plutôt <strong>« CXMT ne libère pas l'offre de legacy aussi vite qu'espéré »</strong>. \[Inférence : jugement par étapes\]

---

## 7. Comment la politique américaine modifie cette lecture

Les États-Unis traitent l'IA moins comme une technologie commerciale que comme une <strong>infrastructure critique de leur bloc d'alliances</strong>. C'est pourquoi une analyse purement technique ne suffit pas à trancher.

L'AI Action Plan américain et le décret présidentiel 14320 précisent l'intention d'exporter vers les pays alliés une <strong>pile IA « Made in USA »</strong> intégrant matériel, cloud, réseau, modèles et applications, tout en réduisant la dépendance technologique envers les pays adverses. Même si les modèles chinois sont supérieurs en performance et en prix, la pile américaine conserve un avantage politique dans les marchés publics et les industries stratégiques des pays alliés. \[Fait : White House AI Action Plan, EO 14320\]

### Ce n'est cependant pas un découplage complet

En janvier 2026, le BIS américain a soumis les exportations de H200 et de MI325X vers la Chine à un examen au cas par cas, sous conditions de clients agréés et d'exigences de sécurité. C'est un compromis qui vise à maintenir un levier de contrôle tout en gardant la Chine partiellement rattachée à l'écosystème des puces américaines. \[Fait : BIS, 13 janvier 2026\]

L'usage de modèles chinois par les entreprises privées américaines n'est pas non plus interdit de façon générale. Le `No DeepSeek on Government Devices Act` n'en est encore qu'au stade de proposition législative. En revanche, le gouvernement australien a ordonné le retrait de DeepSeek de ses systèmes publics, et l'autorité italienne de protection des données a restreint le traitement des données des utilisateurs. \[Fait : mesures officielles de plusieurs pays\]

<strong>Il est probable que l'interdiction de fait imposée par les services d'achats publics et de sécurité s'impose avant même toute loi.</strong> \[Inférence : ordre de mise en œuvre des politiques\]

---

## 8. Les entreprises occidentales peuvent-elles utiliser les API de modèles chinois ?

Le potentiel de diffusion varie entièrement selon la voie empruntée. Ce tableau répond à la question.

| Mode d'adoption | Potentiel de diffusion | Jugement |
|---|---|---|
| Appel direct à une API hébergée en Chine continentale | Faible | Risques de données, de juridiction et de conformité aux achats |
| API de Qwen (États-Unis, UE, Japon, Singapour) | Moyen | La localisation des données est possible, mais le risque lié à l'opérateur chinois subsiste |
| Modèles chinois réhébergés par AWS ou Azure | Moyen-élevé à élevé | Le contrat, la sécurité et le contrôle des données relèvent du cloud occidental |
| Poids ouverts en VPC d'entreprise ou on-premise | Élevé | Aucune donnée n'a besoin d'être envoyée vers des serveurs chinois |
| Gouvernement, défense, infrastructures critiques | Très faible | Les restrictions d'achat peuvent remonter jusqu'à la lignée même du modèle |

Le chemin le plus réaliste est le suivant.

```text
Développement du modèle en Chine
→ Réhébergement sur AWS, Azure ou dans un VPC d'entreprise
→ Vente via les dispositifs occidentaux de sécurité, de contrat et d'audit
```

Autrement dit, <strong>la diffusion technologique des modèles chinois et la diffusion du chiffre d'affaires des opérateurs d'API chinois sont deux choses distinctes</strong>. \[Inférence : analyse des voies d'adoption\]

### Les limites de l'API directe

La politique de confidentialité de DeepSeek indique que les données personnelles, y compris les données saisies, sont <strong>collectées, traitées et stockées directement en Chine</strong>, et peuvent être utilisées pour améliorer le service et le modèle. \[Fait : DeepSeek Privacy Policy\] C'est une condition rédhibitoire pour toute entreprise qui manipule du code source, des données clients, des données médicales ou financières, ou des technologies soumises au contrôle des exportations.

Qwen se distingue quelque peu. Alibaba Cloud Model Studio propose des régions aux États-Unis, en Allemagne, au Japon et à Singapour, permet de restreindre les données et l'inférence à une zone géographique donnée, et précise ne pas utiliser les données clients pour l'entraînement de ses modèles. \[Fait : politique régionale et de sécurité d'Alibaba Cloud\] L'adoption directe de l'API pourrait donc progresser dans les secteurs non régulés, ainsi qu'en Asie du Sud-Est, au Moyen-Orient et en Amérique latine.

La localisation des données et la certification SOC 2 ne suppriment cependant pas <strong>le risque d'interruption de service, de sanctions ou de restriction des achats lié au conflit sino-américain</strong>. \[Inférence : risque résiduel\]

---

## 9. Révision de la thèse : ce qui change et ce qui reste

<strong>Premièrement, la logique d'un effondrement des hyperscalers américains s'affaiblit.</strong> AWS et Azure hébergent directement DeepSeek et fournissent isolation des données, SLA et évaluation de sécurité. Le cloud américain peut absorber l'innovation de coût des modèles chinois et la transformer en chiffre d'affaires. \[Fait : annonces officielles d'AWS et d'Azure\]

<strong>Deuxièmement, la pression sur les prix touche d'abord les API de modèles fermés.</strong> C'est un poids sur le prix du token et la marge d'OpenAI, d'Anthropic et de Google, mais le volume d'inférence et l'usage d'AWS et d'Azure peuvent, eux, augmenter. C'est relativement favorable à la stratégie de modèles ouverts de Meta.

<strong>Troisièmement, la séparation sino-américaine soutient l'investissement total en infrastructure.</strong> Les deux blocs construisent en <strong>doublon</strong> des accélérateurs, de la mémoire, des réseaux et des réseaux électriques. La probabilité que les gains d'efficacité se traduisent directement par une baisse des dépenses mondiales en silicium diminue d'autant.

<strong>Quatrièmement, la prime HBM de SK Hynix peut se maintenir plus longtemps dans le bloc allié.</strong> Le HBM de CXMT pénétrera vraisemblablement d'abord les accélérateurs et les data centers chinois. L'adoption par les CSP occidentaux exige, au-delà de la qualification technique, une validation politique et une certification de chaîne d'approvisionnement. Le contrôle des exportations accélère toutefois l'investissement chinois vers l'autonomie, ce qui constitue un risque pour la part de marché de SK Hynix en Chine à partir de 2028.

<strong>Cinquièmement, Samsung Electronics constitue une couverture relative.</strong> L'inférence bon marché et la diffusion des modèles ouverts peuvent augmenter le volume total non seulement de HBM, mais aussi de DRAM serveur, de NAND et de mémoire générique. À l'inverse, le risque existe que Samsung Electronics soit la première exposée à la montée en volume de la DRAM générique de CXMT.

---

## 10. L'ordre des dommages et des bénéfices

1. <strong>Dommage maximal</strong> : les surprofits des API de modèles fermés, les opérateurs de location de GPU à fort effet de levier
2. <strong>Risque intermédiaire</strong> : les acteurs à investissement anticipé massif et à clientèle concentrée, comme Oracle
3. <strong>Meta</strong> : n'est pas la plus grande perdante. Elle utilise les modèles ouverts pour réduire ses coûts, d'où un potentiel de gain relatif. La pression se situe du côté du CAPEX et de l'amortissement
4. <strong>NVIDIA</strong> : le multiple et le mix produit sont comprimés avant l'EPS à court terme. La substitution en Chine est un risque, mais la douve CUDA, réseau, efficacité énergétique et délai de développement subsiste
5. <strong>Mémoire</strong> : le scénario de base n'est pas un recul de la demande absolue de HBM, mais une <strong>contraction de la prime de rareté du HBM, combinée à un élargissement de la couche vers la DDR, le CXL et l'eSSD</strong>

---

## 11. Mise à jour des scénarios

Il est justifié d'ajuster provisoirement les probabilités établies dans [la juste valeur des semi-conducteurs](/fr/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/).

| Scénario | Avant | Après |
|---|---:|---:|
| Poursuite de la surdemande | 30% | 30% |
| Reconcentration des actifs | 40% | 40% |
| Normalisation de l'offre et de l'efficacité | 20% | <strong>25%</strong> |
| Rupture systémique de la demande | 10% | <strong>5%</strong> |

La performance des modèles chinois <strong>réduit la probabilité d'une disparition pure et simple de la demande d'IA</strong> (rupture : de 10% à 5%). En contrepartie, les gains d'efficacité et le matériel chinois font baisser la prime de rareté de NVIDIA et du HBM (normalisation : de 20% à 25%).

Le scénario en axe temporel reste valable également : l'usage l'emporte sur l'efficacité jusqu'en 2027 (70%), normalisation du mix et des prix à partir de 2028 (25%), contraction totale du CAPEX (5%). Toutefois, <strong>le moteur du scénario à 70% n'est plus un écosystème mondial unique, mais un double investissement, dans le bloc américain et dans le bloc chinois.</strong> \[Inférence : recalibrage des scénarios\]

---

## 12. Ce qui pourrait changer le jugement

- <strong>Rapport technique de Kimi K3 (27 juillet)</strong> : si le matériel d'entraînement est révélé, la validité de la thèse « entraînement frontière sur GPU bas de gamme » sera tranchée
- <strong>Taux de croissance des tokens contre taux de baisse de la mémoire par token</strong> : l'écart entre ces deux valeurs est la vraie réponse à ce débat
- <strong>Qualification de la production de masse du HBM3E de CXMT et volumes réels de packaging</strong> : si confirmé, il faudra abaisser à la fois l'EPS 2028 et le multiple de SK Hynix
- <strong>Ralentissement du prix et du contenu en HBM</strong> : premier signal d'une contraction de la prime de rareté
- <strong>Extension du réhébergement de modèles chinois par les CSP occidentaux</strong> : preuve de la hausse de valeur de la distribution cloud
- <strong>Application réelle de la réglementation américaine sur les achats et la sécurité</strong> : l'étendue de l'interdiction de fait, qui précède la loi

Ce n'est pas encore le moment de <strong>mélanger risque terminal et résultats du trimestre en cours</strong>. Il suffira d'ajuster la trajectoire de SK Hynix au-delà de 2028 lorsque la qualification de la production de masse du HBM3E de CXMT sera confirmée. \[Inférence : ordre du jugement\]

---

## Conclusion

Pour revenir à la question posée, voici la réponse.

Il est vrai que les modèles ouverts chinois convergent vers la frontière américaine, et il est vrai que le coût par unité d'intelligence a chuté rapidement. Mais cela ne signifie pas une baisse des dépenses totales en silicium. Le relèvement du CAPEX de TSMC et la hausse de 30% des tokens chez Microsoft sont, à ce jour, la réponse la plus fiable.

La politique américaine modifie profondément cette lecture. La séparation sino-américaine engendre un <strong>investissement en doublon</strong> dans les deux blocs, ce qui soutient la demande totale d'infrastructure, et protège politiquement, dans le bloc allié, la place de la pile américaine et de la mémoire coréenne.

L'adoption des API de modèles chinois par les entreprises occidentales doit être vue en <strong>séparant le modèle de l'opérateur</strong>. La technologie se diffuse via les poids ouverts, mais l'entité qui la vend sera vraisemblablement AWS, Azure ou un VPC d'entreprise, plutôt qu'un opérateur d'API chinois.

La conclusion est donc une redistribution. Ce qui s'effondre, ce sont les surprofits des API de modèles fermés. Ce qui subsiste, c'est l'infrastructure fondée sur l'usage.

---

_Cet article est une synthèse analytique fondée sur des articles publics (DeepSeek V3/V4, Huawei CloudMatrix384), des annonces officielles d'entreprises (Kimi, call 2T26 de TSMC, call T3 FY26 de Microsoft, CXMT, Alibaba Cloud, politique de confidentialité de DeepSeek), des documents du gouvernement américain (AI Action Plan, décret 14320, BIS), des mesures réglementaires de plusieurs pays et des études de marché (TrendForce, JPMAM). Le matériel d'entraînement de Kimi K3 reste non confirmé jusqu'à la publication du rapport technique du 27 juillet. Les estimations de capacité de CXMT et les probabilités de scénarios sont des estimations de l'auteur au moment de la rédaction, et non une guidance de l'entreprise. Les valeurs mentionnées sont des exemples destinés à illustrer la structure de la chaîne de valeur, et non une recommandation d'achat ou de vente sur un titre en particulier. Les décisions d'investissement et leurs conséquences relèvent de la seule responsabilité de l'investisseur._

---

### Articles associés

- [Kimi K3 Réinitialise la Courbe de Prix de l'IA : De Kimi Linear à HBM et la Stratégie des Grandes Tech](/fr/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/)
- [Les semi-conducteurs sont-ils cycliques et quelle est la juste valeur ? Valoriser Samsung, SK Hynix et Micron avec le FCFE et les bénéfices normalisés](/fr/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [Le vrai débat des semi-conducteurs : quatre horloges physiques et une horloge boursière](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [IPO de CXMT et risque sur les prix mémoire : HBM n’est pas le premier point de rupture](/fr/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)
- [Recherche approfondie sur l'offre et la demande de HBM 2030 : disséquer le modèle de demande de 26,7EB face au calendrier de capacité](/fr/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
