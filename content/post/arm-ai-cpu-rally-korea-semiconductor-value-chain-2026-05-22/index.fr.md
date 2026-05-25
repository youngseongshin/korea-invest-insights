---
title: "La flambée d'ARM — le prochain goulot d'étranglement de l'IA se situe dans l'orchestration CPU, les liens optiques et l'intégrité d'alimentation"
date: 2026-05-22T21:40:00+09:00
description: "La hausse d'ARM n'est pas seulement une histoire de renaissance du CPU. Elle signale que les goulots d'étranglement de l'infrastructure IA se déplacent des GPU vers l'orchestration CPU, le mouvement de mémoire, les interconnexions optiques, l'intégrité d'alimentation, les substrats à haute vitesse et les sockets de test."
categories: ["Market-Outlook"]
tags:
  - "ARM"
  - "Marvell"
  - "NVIDIA"
  - "Samsung Electro-Mechanics"
  - "Samsung Electronics"
  - "SK hynix"
  - "HBM"
  - "Infrastructure IA"
slug: arm-ai-cpu-rally-korea-semiconductor-value-chain-2026-05-22
draft: false
---

> Série liée :
> [NVIDIA Q1 FY27 et infrastructure IA coréenne](/fr/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [Contrat de condensateurs au silicium de Samsung Electro-Mechanics](/fr/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [MLCC et condensateurs au silicium](/fr/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/)

*La hausse d'ARM ne signifie pas simplement que « les CPU redeviennent importants ». Elle indique que les serveurs IA ne sont plus de simples boîtes de GPU, mais des systèmes combinant CPU, XPU, HBM, liens optiques, composants d'alimentation, substrats à haute vitesse et test. ARM est le signal visible. L'alpha peut se trouver dans les goulots d'étranglement qu'il révèle.*

## Résumé

La hausse d'ARM est une reclassification : d'une société de redevances IP mobile vers une plateforme CPU pour centres de données IA. Quand les agents IA s'exécutent en continu, appellent des outils, déplacent des données et coordonnent GPU, ASIC et mémoire, le CPU devient la couche d'orchestration du rack IA.

Le catalyseur externe a été NVIDIA. La société a publié un chiffre d'affaires trimestriel de <strong>81,6 milliards de dollars</strong>, un chiffre d'affaires Data Center de <strong>75,2 milliards</strong>, et une guidance Q2 de <strong>91,0 milliards ±2%</strong>. Le marché y a vu une accélération de la demande IA, non un pic de cycle. ([NVIDIA][1])

L'histoire propre d'ARM est solide. FY26 : chiffre d'affaires <strong>4,92 milliards de dollars</strong>, redevances <strong>2,61 milliards</strong>, licences <strong>2,31 milliards</strong>, EPS non-GAAP <strong>1,77 dollar</strong>. Arm AGI CPU est présenté comme une plateforme CPU de centre de données IA, avec Meta comme partenaire principal; la demande client FY27-FY28 dépasse déjà <strong>2 milliards de dollars</strong>. ([Arm][2])

Le problème est le prix. Research OS local DB indique qu'ARM a clôturé le 21 mai 2026 à <strong>298,23 dollars</strong>. Rapporté à l'EPS non-GAAP FY26, cela donne environ <strong>168,5x</strong> les bénéfices. La thèse est juste, mais l'action n'est pas bon marché.

La meilleure asymétrie peut donc se situer ailleurs : Marvell pour les puces sur mesure et les liens optiques, Samsung Electro-Mechanics pour les condensateurs au silicium, SK hynix et Samsung Electronics pour la mémoire, et les substrats / sockets de test.

---

## 1. Ce que signifie vraiment la hausse d'ARM

La lecture « renaissance du CPU » est correcte mais incomplète. Le message principal est le déplacement du goulot d'étranglement.

```text
Pénurie de GPU
→ pénurie de HBM et de packaging avancé
→ orchestration CPU, mouvement de mémoire, liens optiques
→ intégrité d'alimentation, substrats, test
```

Un agent IA n'est pas une simple requête web. Il appelle des modèles, utilise des outils, lit des documents, interroge des bases de données et conserve des résultats intermédiaires. Le GPU calcule; le CPU coordonne l'ordre des tâches, la mémoire, le réseau, la sécurité et l'opération système.

Le CPU devient donc le plan de contrôle du rack IA.

---

## 2. Arm AGI CPU : de l'IP au silicium

ARM a placé <strong>Arm AGI CPU</strong> au centre de son récit. L'entreprise le décrit comme un produit silicium pour centres de données agentic AI, avec Meta comme partenaire de référence. Des systèmes commerciaux peuvent être commandés via ASRock, Lenovo, Quanta et Supermicro. ([Arm][2])

Ancien modèle :

```text
licence IP
→ le client conçoit et fabrique la puce
→ ARM reçoit frais de licence et redevances
```

Nouveau modèle :

```text
IP + sous-systèmes + silicium de production
→ déploiement plus rapide de la plateforme Arm à l'échelle data center
→ plus de contrôle de plateforme
```

Mais cela crée un risque de conflit avec les clients. Si ARM vend ses propres puces, certains licenciés peuvent la voir comme concurrente. C'est pourquoi l'enquête FTC rapportée par Bloomberg sur les pratiques de licence doit être surveillée. ([Bloomberg][3])

---

## 3. Valorisation : bonne thèse, prix exigeant

À <strong>298,23 dollars</strong>, avec un EPS non-GAAP FY26 de <strong>1,77 dollar</strong> :

```text
PER non-GAAP FY26 = 298,23 / 1,77 = environ 168,5x
```

Avec un chiffre d'affaires FY26 de <strong>4,92 milliards</strong>, la capitalisation dans la zone basse des 300 milliards implique un multiple ventes supérieur à 60x.

Ce prix n'achète pas les bénéfices actuels. Il achète un scénario 2030-2031 : pénétration des CPU data center, revenus AGI CPU, hausse des royalties, expansion Armv9/Neoverse.

Notre lecture : <strong>ne pas poursuivre au prix actuel / attendre</strong>.

---

## 4. Alpha 1 : Marvell et le goulot de connectivité

Si ARM représente l'orchestration CPU, Marvell représente <strong>compute sur mesure + optique + switching</strong>.

Marvell a publié un chiffre d'affaires FY26 de <strong>8,195 milliards de dollars</strong> et un EPS non-GAAP de <strong>2,84 dollars</strong>. La société prévoit un FY27 proche de 11 milliards, avec la data center en moteur de croissance et une hausse de plus de 50% des revenus d'interconnexion. ([Marvell][4])

Marvell n'est pas seulement une société de puces réseau. Elle combine puces IA sur mesure, interconnexions optiques, switching PCIe/CXL et partenariat NVLink Fusion. L'acquisition de Celestial AI apporte une plateforme Photonic Fabric, avec des objectifs de run-rate annualisé de 500 millions en FY28 et 1 milliard en FY29 si les jalons sont atteints. ([Marvell Celestial][5])

Mais MRVL a déjà fortement monté. Research OS local DB indique une clôture à <strong>190,69 dollars</strong> le 21 mai 2026. Lecture : <strong>attendre / acheter sur repli</strong>.

---

## 5. Alpha 2 : Samsung Electro-Mechanics et l'intégrité d'alimentation

En Corée, le second goulot d'étranglement le plus clair est Samsung Electro-Mechanics.

Le 20 mai 2026, la société a annoncé un contrat de condensateurs au silicium d'environ <strong>1,5 billion de wons</strong> sur deux ans. Ces composants sont installés dans des packages hautes performances comme les GPU IA et la HBM afin de stabiliser l'alimentation. ([Samsung Electro-Mechanics][6])

Le point clé n'est pas « plus de MLCC ». C'est :

```text
Avant :
MLCC + module caméra + FC-BGA

Après :
composants d'intégrité d'alimentation pour packages IA
+ FC-BGA
+ MLCC IA
```

Le condensateur au silicium ne remplace pas tous les MLCC. C'est un complément hautes performances placé dans ou très près du package AI GPU/HBM. Il peut reclassifier Samsung Electro-Mechanics comme fournisseur de composants d'alimentation pour packages IA.

---

## 6. Mémoire coréenne : SK hynix et Samsung Electronics

La hausse d'ARM est également positive pour la mémoire. Plus de CPU d'orchestration signifie plus de mémoire côté CPU, plus de mouvement vers HBM, plus de DRAM serveur et plus de mémoire LPDDR/DDR/CXL.

| Société | Rôle | Lecture |
|---|---|---|
| SK hynix | gagnant HBM confirmé | conserver / acheter sur repli |
| Samsung Electronics | option de rattrapage HBM + IDM large | surveiller / acheter avec confirmation |

Samsung doit prouver la qualification HBM4, les volumes, les marges et l'amélioration de la fonderie.

---

## 7. Substrats à haute vitesse et sockets de test

Quand le rack IA devient plus dense, les substrats et le test prennent de la valeur.

| Couche | Candidats | À vérifier |
|---|---|---|
| PCB haute vitesse | Isu Petasys, Daeduck, TLB, Korea Circuit, Simmtech | revenus IA, nombre de couches, ASP, marge |
| sockets de test | ISC, LEENO, TSE | clients ASIC/HBM/CXL, mix produits |
| substrats package | Samsung Electro-Mechanics, Daeduck, Korea Circuit | utilisation FC-BGA, qualification, marge |

La règle : <strong>ne pas acheter seulement le mot IA; acheter clients, commandes et marges vérifiés.</strong>

---

## Conclusion

ARM est un bon signal. Les serveurs IA sont des systèmes CPU, XPU, HBM, optique, alimentation, substrats et test.

Mais acheter ARM après la hausse peut confondre le signal et l'actif. La vraie question est : quel goulot d'étranglement n'est pas encore totalement valorisé ?

<strong>ARM est le signal. L'alpha est dans les goulots.</strong>

---

*Cet article est un commentaire de recherche, pas un conseil d'investissement. Les prix ARM et MRVL proviennent de Research OS local DB, clôture US du 21 mai 2026. Données sociétés : NVIDIA, Arm, Marvell, Samsung Electro-Mechanics. Date des données : 22 mai 2026 KST.*

[1]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx "NVIDIA Announces Financial Results for First Quarter Fiscal 2027"
[2]: https://newsroom.arm.com/news/arm-q4-fye26-results "Arm delivers record-breaking quarter and full-year results"
[3]: https://www.bloomberg.com/news/articles/2026-05-15/arm-holdings-said-to-face-us-antitrust-probe-over-chip-tech "Arm Holdings Said to Face US Antitrust Probe Over Chip Tech"
[4]: https://d1io3yog0oux5.cloudfront.net/_cde1ddaaf3189b05accbc0f122d6a0c2/marvell/db/3715/35343/pdf/2026_03_05_Marvell_Q4_FY26_financial_business_results_FINAL.pdf "Marvell FY26 and Q4 FY26 Financial and Business Results"
[5]: https://d1io3yog0oux5.cloudfront.net/_a2ff1b1766821fdbdf60a17efbf050dd/marvell/files/pages/marvell/db/3831/description/2025-12_02-Marvell-to-Acquire-Celestial-AI-vF2.pdf "Marvell to Acquire Celestial AI"
[6]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
