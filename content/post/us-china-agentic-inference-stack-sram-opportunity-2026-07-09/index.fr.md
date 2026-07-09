---
title: "La divergence des infrastructures d’inférence agentique aux États-Unis et en Chine, et l’opportunité SRAM"
date: 2026-07-09T17:20:00+09:00
description: "Pourquoi les infrastructures d’inférence IA américaines et chinoises divergent, et comment l’électricité, le HBM, SRAM/LPU, le packaging avancé et les actions coréennes s’insèrent dans cette carte."
categories: ["Theme-Analysis", "Korea Semiconductors", "AI Infrastructure"]
tags: ["inférence IA", "IA agentique", "SRAM", "LPU", "HBM", "Vera Rubin", "LPX", "Samsung Electronics", "SK hynix", "HD Hyundai Electric", "Hanmi Semiconductor"]
slug: us-china-agentic-inference-stack-sram-opportunity-2026-07-09
series: ["hbm", "exclusive-analysis"]
valley_cashtags: ["005930.KS", "000660.KS", "267260.KS", "010120.KS", "298040.KS", "042700.KS", "NVDA"]
draft: false
---

## Synthèse

Les États-Unis et la Chine développent tous deux l’inférence IA, mais ils ne résolvent pas le même goulot d’étranglement. Aux États-Unis, la contrainte porte sur l’électricité, la densité des racks, le HBM, le packaging avancé et le débit de tokens par mégawatt. En Chine, la contrainte porte sur l’accès aux puces logiques de pointe et au HBM, ce qui pousse vers Ascend, les maillages optiques, l’expansion parallèle et des hiérarchies mémoire domestiques.

Pour les actions coréennes cotées, l’opportunité la plus propre n’est pas de supposer automatiquement un bénéfice sur les modules optiques chinois. Le meilleur point d’entrée est plutôt la pile américaine: HBM4/HBM4E, équipements électriques, outils de packaging HBM et option moins bien valorisée de Samsung Electronics dans la fonderie SRAM/LPU, le stockage IA et la hiérarchie mémoire.

## 1. Ce qui est vérifié

Cette note part de l’article de YS-VC sur la divergence des piles d’inférence entre les États-Unis et la Chine. L’idée principale est correcte: l’inférence n’est plus une simple histoire de GPU, et les limites physiques diffèrent selon les régions.

| Affirmation | Évaluation | Lecture investisseur |
|---|---|---|
| Les piles d’inférence américaines et chinoises divergent | Largement vrai | Les États-Unis optimisent énergie et rack, la Chine contourne les limites de logique et de HBM |
| Les États-Unis vont vers GPU/HBM/SRAM à l’échelle du rack | Vrai | Vera Rubin, LPX, HBM4 et SRAM/LPU deviennent un système intégré |
| La Chine utilise Ascend, maillage optique et hiérarchie mémoire propre | Partiellement vrai | Direction plausible, mais CloudMatrix demande des preuves indépendantes |
| Les contrôles export US limitent l’accès chinois au compute NVIDIA | Vrai | La Chine ne peut pas compter sur un accès stable aux GPU et HBM de pointe |
| Le HBM reste un point de contrôle clé | Vrai | Le BIS le considère comme important pour l’entraînement et l’inférence IA à grande échelle |

## 2. Pourquoi les piles divergent

L’IA agentique augmente fortement le nombre de tokens. Les agents de code, de recherche, de voix ou d’entreprise lisent de longs contextes, appellent des outils, interprètent les résultats et génèrent de nouvelles réponses. Prefill, decode, KV cache, stockage, réseau et électricité deviennent donc tous importants.

| Zone | États-Unis | Chine |
|---|---|---|
| Contrainte principale | Électricité, densité rack, transformateurs, HBM4, packaging | Logique avancée, accès HBM, contrôles export |
| Direction | Vera Rubin, LPX/LPU, HBM4, racks haute puissance | Huawei Ascend, maillage optique, expansion parallèle |
| Force | Accès aux meilleurs GPU, HBM et packaging | Expansion électrique plus rapide, infrastructure publique |
| Faiblesse | Connexion réseau, délai d’alimentation, transformateurs | Absence de logique EUV de pointe, HBM limité |
| Actions coréennes | HBM, équipements électriques, outils HBM, fonderie | Limité sans fournisseurs vérifiés |

L’IEA estime que la demande électrique des data centers pourrait atteindre environ 945TWh en 2030. ([IEA][1]) BloombergNEF, cité par Energy Connects, prévoit que la Chine pourrait ajouter plus de 3,4TW de capacité en cinq ans, presque six fois les États-Unis. ([Energy Connects][2]) Les États-Unis doivent donc optimiser les tokens par mégawatt, alors que la Chine peut s’appuyer davantage sur l’expansion physique.

## 3. La pile américaine: HBM plus SRAM/LPU

NVIDIA décrit LPX comme un accélérateur d’inférence pour Vera Rubin. Il combine des GPU Rubin utilisant le HBM avec Groq 3 LPX utilisant des LPU fondés sur SRAM. ([NVIDIA LPX][3])

| Mesure | Donnée NVIDIA LPX |
|---|---:|
| Charge de tokens agentiques | Jusqu’à 15 fois plus |
| Vera Rubin NVL72 + LPX | Jusqu’à 35 fois plus de débit par MW |
| SRAM par accélérateur LPU | 500MB |
| Bande passante SRAM par accélérateur | 150TB/s |
| Rack LPX | 256 puces LPU |
| SRAM par rack LPX | 128GB |
| DDR5 par rack LPX | 12TB |
| Bande passante SRAM par rack | 40PB/s |

Ce n’est pas un remplacement du HBM. Le HBM reste central pour le GPU Rubin. SRAM/LPU complète HBM en traitant les tâches de decode sensibles à la latence.

## 4. La Chine est un signal concurrentiel, pas une exposition coréenne directe

Si la Chine n’a pas accès aux GPU et HBM les plus avancés, il est logique de relier davantage de puces, d’améliorer l’interconnexion et d’utiliser des maillages optiques. Mais cela ne crée pas automatiquement des revenus pour les sociétés coréennes. La chaîne chinoise devient plus locale, et la performance, le taux d’erreur et le coût total des systèmes de type CloudMatrix restent à vérifier.

## 5. Carte des actions coréennes

| Couche | Goulot | Sociétés coréennes | Vue |
|---|---|---|---|
| HBM4/HBM4E | Mémoire pour Vera Rubin et serveurs IA | SK hynix, Samsung Electronics | Bénéfice structurel. SK hynix mène, Samsung est l’option de rattrapage |
| Fonderie SRAM/LPU | Accélérateurs decode à faible latence | Samsung Electronics | Peu visible en revenus, mais option importante |
| Stockage IA/KV cache | Mémoire d’agent, eSSD, PCIe 6.0 | Samsung Electronics, FADU | Extension de la hiérarchie mémoire |
| Outils HBM | TC bonders, packaging avancé | Hanmi Semiconductor | Vrai goulot, mais clients et valorisation comptent |
| Équipements électriques | Transformateurs, switchgear, connexion réseau | HD Hyundai Electric, LS ELECTRIC, Hyosung Heavy | Exposition directe au goulot électrique des data centers |
| Maillage optique chinois | Modules optiques pour clusters chinois | Exposition coréenne limitée | À éviter sans preuve fournisseur |

## 6. Vue pratique

| Priorité | Exposition | Vue |
|---:|---|---|
| 1 | Samsung Electronics | Achat conditionnel si HBM4E, SRAM/LPU et stockage IA deviennent visibles |
| 2 | HD Hyundai Electric | Attente, bonne qualité mais momentum de commandes déjà visible |
| 3 | SK hynix | Attente, leader HBM mais trade encombré |
| 4 | Hanmi Semiconductor | Liste de suivi, besoin de commandes répétées et diversification |
| 5 | Bénéficiaires du maillage optique chinois | À éviter sans preuve directe |

L’opportunité coréenne n’est pas le “maillage optique chinois”. Elle réside dans le goulot de l’usine IA américaine: électricité, HBM, SRAM/LPU, packaging avancé et stockage. SK hynix peut avoir la meilleure position industrielle, HD Hyundai Electric l’exposition électrique la plus pure, mais l’option de revalorisation la plus asymétrique reste Samsung Electronics si le marché cesse de le voir uniquement comme un retardataire du HBM.

## Sources

- [YS-VC](https://www.ys-vc.com/blog/us-china-ai-inference-stack-divergence)
- [IEA](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
- [Energy Connects](https://www.energyconnects.com/news/renewables/2026/february/china-ramps-up-energy-boom-flagged-by-musk-as-key-to-ai-race/)
- [NVIDIA LPX](https://www.nvidia.com/en-us/data-center/lpx/)
- [Samsung Newsroom](https://news.samsung.com/global/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026)
- [BIS](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military)
- [Yonhap](https://en.yna.co.kr/view/AEN20260128002800320)
- [The Elec](https://www.thelec.net/news/articleView.html?idxno=11132)
- [Seoul Economic Daily](https://en.sedaily.com/finance/2026/07/06/hd-hyundai-electric-raises-2026-order-target-23-percent-on)
