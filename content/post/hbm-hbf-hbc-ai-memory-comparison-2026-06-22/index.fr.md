---
title: "HBM, HBF et HBC : Comment distinguer les trois technologies de mémoire pour l'IA"
slug: "hbm-hbf-hbc-ai-memory-comparison-2026-06-22"
date: 2026-06-22T10:00:00+09:00
description: "HBM, HBF et HBC ne sont pas du même type. Cette analyse cartographie la bande passante, la capacité et le coût d'inférence comme trois obstacles distincts et explique pourquoi ces technologies sont complémentaires."
categories: ["Exclusive Analysis", "Tech-Analysis"]
tags: ["HBM", "HBF", "HBC", "Mémoire IA", "Semi-conducteurs", "SK Hynix", "Samsung Electronics", "Micron", "Qualcomm", "NAND", "DRAM"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte
> Cet article constitue le volet technique de trois analyses précédentes : [Qui paiera le consensus semiconducteurs 2027](/fr/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/), [L'IPO de CXMT et le risque de prix mémoire](/fr/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/), et [Pourquoi le supercycle IA dure plus longtemps](/fr/post/ai-supercycle-extension-agent-demand-ipo-funding-memory-storage-2026-06-12/). Ces articles traitaient de la demande, des prix et de la valorisation. Celui-ci se concentre sur <strong>ce que sont réellement les trois technologies de mémoire IA côté offre, à quel stade de maturité elles en sont, et quelle relation elles entretiennent entre elles</strong>. Les hubs connexes sont le [hub HBM IA](/fr/page/korea-semiconductor-hbm-kospi-hub/) et le [hub Exclusive Analysis](/fr/page/exclusive-analysis-hub/).

## TL;DR

* HBM, HBF et HBC ne sont pas des mémoires de même nature. <strong>HBM et HBF sont des composants mémoire</strong>, tandis que <strong>HBC est le nom d'une architecture d'accélérateur de Qualcomm</strong>. Les aligner sur une seule ligne et ne comparer que les chiffres de TB/s conduit inévitablement à une mauvaise lecture.
* Les trois technologies s'attaquent chacune à un obstacle différent. <strong>HBM vise le mur de la bande passante</strong>, <strong>HBF vise le mur de la capacité</strong>, <strong>HBC vise le coût et la consommation énergétique de l'inférence</strong>.
* L'écart de maturité est considérable. <strong>HBM est en production de masse complète (★★★★★)</strong>, <strong>HBF est au stade de simulation (★★, objectif premier échantillon second semestre 2026)</strong>, <strong>HBC est à l'état de plan (★, objectif échantillonnage 2027)</strong>.
* Les trois sont complémentaires, non concurrentes. La "température" des données détermine leur place : les données chaudes (cache KV) vont vers HBM, les données froides (poids figés) vers HBF, l'inférence à faible coût vers HBC.
* Aucune technologie ne menace actuellement la position de mémoire de travail de HBM. La contribution significative de HBF et HBC aux revenus n'est pas attendue avant 2027-2028 au plus tôt. \[Inférence\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Thèse principale</div>
  <div class="thesis-callout__body">
    Dans la guerre des mémoires IA, seul le HBM est aujourd'hui démontré. HBF est une promesse et HBC est un plan. Les trois ne sont pas en concurrence : ils remplissent des niveaux différents dans la hiérarchie de la mémoire.
  </div>
</div>

---

## 1. Le goulot d'étranglement de l'IA n'est pas le calcul mais la mémoire

La puissance de calcul des GPU a été multipliée par environ 80 au cours des dix dernières années, mais la bande passante mémoire n'a progressé que d'un facteur 17. \[Fait : comparaison des spécifications par génération NVIDIA\] Cet écart constitue le véritable goulot d'étranglement des accélérateurs IA actuels. Les puces IA coûteuses passent de plus en plus de temps à attendre les données, et la vitesse à laquelle un LLM génère un token dépend presque entièrement de la rapidité avec laquelle la mémoire achemine les données.

Ce goulot d'étranglement se décompose en deux murs distincts.

<strong>Le mur de la bande passante :</strong> l'incapacité à déplacer les données assez rapidement. La phase de décodage de l'inférence LLM exige que les poids du modèle soient lus en mémoire à chaque token, ce qui lie en permanence les performances à la vitesse mémoire.

<strong>Le mur de la capacité :</strong> l'incapacité à stocker suffisamment de données. Le cache KV généré par un contexte de 128 000 tokens représente déjà environ 343 Go, ce qui dépasse la capacité HBM de 192 Go du dernier GPU en date (B200). \[Fait : calcul sur la base des spécifications publiques\]

HBM, HBF et HBC sont trois technologies qui s'attaquent à ces deux murs de manières différentes. Et l'une des trois n'est pas un composant mémoire mais l'architecture d'accélérateur propriétaire d'une entreprise. Ignorer cette distinction fait s'effondrer toute comparaison.

---

## 2. HBM : la seule technologie prouvée, qui résout le mur de la bande passante

### Concept

Le principe de la HBM (High Bandwidth Memory) est élégant. Des puces DRAM sont empilées verticalement sur 8 à 16 couches et placées directement à côté du GPU, reliées par des milliers d'électrodes fines (TSV), ce qui élargit le bus de données à 1 024 ou 2 048 bits. Ce n'est pas la vitesse d'une broche individuelle qui fait la différence, mais l'extrême largeur du bus. De la même façon qu'une autoroute à 2 048 voies, même à vitesse modérée, transporte bien plus de trafic qu'une voie rapide à une seule file.

### Performances et niveau de preuve

La bande passante d'une stack HBM3E est d'environ 1,2 To/s, et HBM4 atteint environ 2 To/s. \[Fait : spécifications JEDEC\] C'est 20 à 30 fois supérieur au DDR5. Pratiquement tous les accélérateurs IA majeurs, dont les NVIDIA H100, H200, B200 et AMD MI300, intègrent du HBM.

<strong>Niveau de preuve ★★★★★ :</strong> parmi les trois technologies, seul le HBM est en production de masse complète. Des années de fabrication à grande échelle ont permis de valider les rendements et la fiabilité. SK Hynix détient environ 57 à 62 % du marché et reste le fournisseur principal de NVIDIA. \[Fait : IR entreprises et estimations de marché\]

### Feuille de route et acteurs

La trajectoire va du HBM4 (production 2026, adoption d'un die de base logique) vers le HBM4E (personnalisé), puis vers le HBM5 (objectif 2029, 4 To/s). À partir du HBM4, SK Hynix fabrique le die de base en procédé 12 nm chez TSMC, ce qui fait évoluer la structure vers une co-conception entre fabricant de mémoire et fondeur. \[Fait : annonces officielles des entreprises\] \[Inférence : les 4 To/s du HBM5 sont un objectif de feuille de route, non un chiffre mesuré\]

Le marché est un oligopole à trois acteurs : SK Hynix, Samsung Electronics et Micron, avec TSMC en soutien critique pour le die de base et l'interposeur. Le marché de la mémoire IA repose sur une structure conjointe entre ces trois fabricants de mémoire, TSMC et NVIDIA. \[Inférence : taille du marché estimée à environ 35 milliards USD en 2025, 45 à 58 milliards USD en 2026, avec un écart significatif selon les sources\]

---

## 3. HBF : le nouvel entrant qui vise le mur de la capacité, encore au stade de promesse

### Concept

L'idée derrière la HBF (High Bandwidth Flash) est ingénieuse. Elle emprunte la méthode d'empilement et l'interface du HBM, mais remplace la DRAM coûteuse à l'intérieur par de la flash NAND bon marché. La NAND stocke plusieurs bits par cellule, ce qui lui confère une grande capacité et un coût par Go bien inférieur. En août 2025, SanDisk et SK Hynix ont annoncé un accord de standardisation. SanDisk a décrit la HBF comme venant "augmenter, non remplacer le HBM". \[Fait : annonce conjointe SanDisk et SK Hynix\]

SanDisk affirme pouvoir loger environ 512 Go par stack (8 à 16 fois le HBM) tout en délivrant une bande passante d'environ 1,6 To/s. \[Fait : fiche technique SanDisk\]

### Un niveau de preuve mesuré

Il convient de s'arrêter ici.

<strong>Niveau de preuve ★★ :</strong> la HBF n'est pas encore en production de masse. Il n'existe même pas de benchmark indépendant d'une puce réelle. Les chiffres de 512 Go et 1,6 To/s proviennent de simulations internes de SanDisk, et les notes de bas de page de la fiche technique précisent explicitement : "tests internes et simulations, sous hypothèses de modèles spécifiques". \[Fait : notes de bas de page de la fiche technique SanDisk\] L'objectif de premier échantillon réel est fixé au second semestre 2026, et l'adoption dans des dispositifs d'inférence est attendue au plus tôt en 2027. Il faudra également relever le défi technique d'empiler plus de 5 000 couches en superposant 16 niveaux de NAND à 238 couches.

### Les limites de la NAND définissent l'usage

La HBF présente deux contraintes fondamentales.

Premièrement, <strong>la latence :</strong> la NAND est plus lente que la DRAM en lecture, ce qui donne à la HBF une latence environ 100 fois supérieure à celle du HBM (HBF environ 10 µs contre quelques dizaines de ns pour le HBM). \[Fait : caractéristiques physiques des technologies\]

Deuxièmement, <strong>l'endurance en écriture :</strong> la NAND supporte un nombre limité de cycles d'écriture, ce qui la rend inadaptée aux workloads à mises à jour fréquentes.

Ces deux contraintes définissent l'usage de la HBF : un <strong>stockage haute capacité pour les poids de modèle</strong>, qui ne changent pratiquement jamais et ne font l'objet que de lectures. Dans ce rôle, ses faiblesses ne posent guère de problème.

### La variable décisive : l'adoption par NVIDIA

<strong>NVIDIA ne manifeste pas d'intérêt majeur pour la HBF à ce stade.</strong> Les signaux indiquent que l'entreprise préfère résoudre le problème de capacité par des SSD haute performance connectés directement au GPU (eSSD). Parmi les grands clients ayant montré de l'intérêt pour la HBF, Google figure en tête. \[Inférence : synthèse de l'observation du secteur et des communications publiques\] La décision du principal client est la plus grande inconnue qui déterminera le succès ou l'échec de la HBF.

Les acteurs sont SanDisk à la tête, SK Hynix en partenaire, Samsung en participant, tandis que Kioxia a choisi la voie alternative des eSSD. Le camp n'est pas encore consolidé.

---

## 4. HBC : pas une mémoire, mais l'architecture d'accélérateur de Qualcomm

### Clarification terminologique

"HBC" est un acronyme piégeux. Placé aux côtés de HBM et HBF, il semble appartenir à la même catégorie, mais <strong>HBC désigne le nom de l'architecture d'accélérateur IA que Qualcomm a annoncée lors de sa journée investisseurs de juin 2026</strong> ("High Bandwidth Compute"). Ce n'est pas un terme standardisé par plusieurs acteurs du secteur, mais une marque propre à une entreprise. \[Fait : annonce officielle de Qualcomm\]

Le même acronyme "HBC" entre en collision avec "High Bandwidth Cache Controller (HBCC)" d'AMD, et prête également à confusion avec HBF. Les trois désignent des concepts entièrement différents.

Ainsi, la comparaison "HBM vs HBF vs HBC" est en réalité <strong>une comparaison de 2 composants mémoire contre 1 conception de système d'accélérateur</strong>. Ignorer cette asymétrie conduit à des équations erronées, comme "HBC offre 18 fois plus de bande passante que HBM" (les bases de mesure sont différentes).

### Concept et technologie

Le support mémoire utilisé par HBC n'est pas le HBM mais <strong>le LPDDR</strong> (DRAM basse consommation utilisée dans les smartphones). L'idée consiste à empiler cette LPDDR économique en 3D directement au-dessus du die logique de calcul, ramenant quasi à zéro la distance entre calcul et mémoire. L'approche cherche à réduire le coût de l'inférence et la consommation électrique sans recourir à un interposeur silicium coûteux ni au HBM.

Qualcomm avance des chiffres tels que 6 fois plus de bande passante par watt par rapport au HBM et 200 fois plus de capacité par watt par rapport à la SRAM. \[Fait : annonce Qualcomm\] Ces chiffres sont cependant normalisés par carte ou par rack selon la propre méthodologie de Qualcomm, et leur comparaison directe avec les chiffres par stack du HBM crée des bases de référence différentes propices à l'erreur d'interprétation.

### Niveau de preuve et réalité

<strong>Niveau de preuve ★ :</strong> l'accélérateur AI250 de Qualcomm intégrant HBC n'existe pas encore en version physique, et l'objectif d'échantillonnage est fixé à mi-2027. Toutes les performances annoncées sont des objectifs de conception. \[Fait : annonce Qualcomm\] Si HBF est au stade de simulation, HBC est au stade du plan. Des rapports font état de commandes de Microsoft et Meta pour des accélérateurs Qualcomm, mais ces informations ne sont pas encore confirmées. \[Inférence : rapports de presse secondaires, non vérifiés\]

Le cadre correct pour lire HBC n'est pas celui d'une "mémoire concurrente au HBM", mais celui d'<strong>une stratégie système d'une entreprise qui cherche à proposer une inférence moins coûteuse sans utiliser de HBM</strong>. En cas de succès, cela pourrait affecter une partie des segments d'inférence bas de gamme de la demande en HBM, mais ne constitue pas un scénario de remplacement total du HBM. Les acteurs se résument en pratique à Qualcomm seul.

---

## 5. Complémentaires, non concurrentes : la température des données détermine la place

Les titres "HBF va tuer HBM" ou "HBC va remplacer HBM" reviennent fréquemment. La conclusion de l'analyse est que ce discours est exagéré. Les trois technologies sont fondamentalement complémentaires.

Ce constat ne repose pas sur une logique de marché abstraite, mais sur les propriétés physiques des données elles-mêmes.

Dans l'inférence LLM, les données chargées en mémoire sont de deux types.

<strong>Les poids du modèle (données froides) :</strong> une fois l'entraînement terminé, ils ne changent pratiquement plus et ne sont que lus à chaque inférence. Les placer dans une mémoire lente mais grande et bon marché (HBF) n'entraîne pas de perte. La contrainte d'endurance en écriture de la NAND ne pose pratiquement aucun problème pour des poids qui ne font l'objet que de lectures.

<strong>Le cache KV (données chaudes) :</strong> il est mis à jour à chaque instant au fil de la conversation. Il doit impérativement résider dans la mémoire la plus rapide disponible (HBM). Le remplacer par une mémoire plus lente dégrade l'ensemble du système.

Avec une latence 100 fois supérieure, HBM et HBF ne peuvent physiquement pas occuper le même niveau de "mémoire de travail". HBF ne chasse pas HBM ; il constitue un niveau inférieur qui accueille ce que HBM ne peut pas contenir. HBC opère sur une toute autre piste, en ciblant une inférence à faible coût.

L'architecture future des accélérateurs IA ne sera pas un choix "HBM ou HBF", mais vraisemblablement <strong>une hiérarchie à trois niveaux : HBM + HBF + SSD haute performance</strong>. \[Inférence : analyse des feuilles de route technologiques\]

Une concurrence partielle existe néanmoins. La question de savoir si le problème de capacité sera résolu par HBF ou par eSSD reste ouverte. Les accélérateurs HBC et HBM se chevauchent également partiellement sur le segment de l'inférence bas de gamme. Si HBF et HBC réussissent à offrir une solution "haute capacité à faible coût", les clients pourraient être incités à acheter moins de HBM coûteux, créant un scénario d'érosion marginale. Toutefois, toute cette concurrence concerne 2027 et au-delà.

---

## 6. Les jalons à surveiller maintenant

Pour chacune des trois technologies, le passage de la "promesse" à la "réalité" interviendra à des moments différents.

<strong>HBM est en cours d'exécution.</strong> Les prochains points d'observation sont : le rendement de production du HBM4, la diffusion du HBM personnalisé pour les clients, et la transition vers le hybrid bonding. SK Hynix, Samsung, Micron et TSMC continueront de capter la majeure partie de la valeur de la mémoire IA dans un avenir proche. \[Inférence : estimations de parts de marché\]

<strong>Pour HBF, deux jalons sont décisifs.</strong> Premièrement, le premier échantillon physique et les benchmarks indépendants au second semestre 2026. Tous les chiffres actuels étant issus de simulations, l'arrivée d'une puce réelle représente un moment charnière. Deuxièmement, la décision d'adoption par NVIDIA. Si NVIDIA adopte HBF, le camp se consolide rapidement ; sinon, HBF reste une technologie de niche.

<strong>Pour HBC, le premier jalon est l'échantillonnage réel de l'AI250 de Qualcomm en 2027 et sa validation indépendante.</strong> La confirmation ou non des commandes de Microsoft et Meta sera également un indicateur de l'expansion de l'écosystème HBC.

---

## Vérification des discours marketing

Certaines affirmations fréquemment avancées dans ce domaine méritent d'être examinées avec prudence.

<strong>"HBF et HBC vont remplacer HBM" :</strong> les différences de latence et de rôle en font des technologies complémentaires. Le discours de remplacement est une exagération.

<strong>"Capacité 16 fois supérieure, 4 To de VRAM, 6 fois moins d'énergie" :</strong> la plupart de ces chiffres proviennent de simulations internes ou d'objectifs de conception, non de mesures indépendantes.

<strong>"HBM sera menacé dès 2026" :</strong> la contribution significative de HBF et HBC aux revenus ne s'attend pas avant 2027-2028 au plus tôt.

<strong>"HBC est la mémoire de prochaine génération" :</strong> c'est une erreur de catégorie. HBC n'est pas une mémoire, c'est une architecture d'accélérateur signée Qualcomm.

Reconnaître le potentiel de ces technologies est légitime, mais distinguer les titres marketing des faits vérifiés reste le point de départ de toute analyse sérieuse.

---

_Cet article est une analyse technique basée sur des sources primaires, secondaires et tertiaires publiques ainsi que sur les communications officielles des entreprises. Il ne constitue pas une recommandation d'investissement dans un titre ou un produit spécifique. La plupart des chiffres de performances relatifs à HBF et HBC sont des affirmations d'entreprises, des simulations ou des objectifs, et n'ont pas encore été vérifiés de manière indépendante. Ce domaine évolue rapidement ; il est recommandé de vérifier les informations auprès des sources primaires les plus récentes._

---

### Articles connexes

- [Qui paiera le consensus semiconducteurs 2027](/fr/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/)
- [L'IPO de CXMT et le risque de prix mémoire](/fr/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)
- [Analyse TechWing HBM Cube Prober](/fr/post/techwing-hbm-cube-prober-big3-conditional-buy-2026-06-21/)
- [Pourquoi le supercycle IA dure plus longtemps](/fr/post/ai-supercycle-extension-agent-demand-ipo-funding-memory-storage-2026-06-12/)
- [Samsung et SK Hynix représentent 90,8% des ETF semiconducteurs coréens](/fr/post/korea-semiconductor-etf-exposure-marketcap-gap-strategy-2026-06-13/)
