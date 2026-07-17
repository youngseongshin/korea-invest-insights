---
title: "La localisation de la mémoire en Chine et la Corée : décomposer l'exposition à la Chine de Samsung, SK Hynix et Micron"
slug: "china-memory-localization-exposure-samsung-hynix-micron-2026-07-18"
date: 2026-07-18T15:00:00+09:00
description: "Les semi-conducteurs ont représenté 38,7% des exportations coréennes du premier semestre et la Chine en est le premier marché. Le HBM étant restreint, les exportations vers la Chine se concentrent sur la DRAM et la NAND grand public, précisément le segment visé par CXMT et YMTC. Nous décomposons l'exposition à la Chine de chaque société à partir des publications et montrons que le vrai risque n'est pas la perte de chiffre d'affaires en Chine mais l'effet de second tour des volumes déplacés qui pèsent sur l'ASP mondial."
categories: ["Exclusive Analysis", "Korean-Equities", "Market-Outlook"]
tags: ["Samsung Electronics", "SK Hynix", "Micron", "CXMT", "YMTC", "Localisation chinoise", "DRAM grand public", "NAND", "Exportations de semi-conducteurs", "Contrôles à l'exportation"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte
> Cet article fait suite à [IPO de CXMT et risque sur les prix mémoire](/fr/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/), qui posait qu'il fallait « séparer le risque HBM du risque DRAM client ». Cette note décompose ce risque de façon quantitative en <strong>exposition à la Chine des trois sociétés</strong>. À lire avec [le prix des API d'IA chinoises est-il soutenable](/fr/post/china-ai-api-pricing-sustainability-cost-structure-2026-07-18/), [la redistribution de la chaîne de valeur des modèles ouverts chinois](/fr/post/china-open-model-convergence-value-chain-redistribution-2026-07-17/) et [la juste valeur des semi-conducteurs](/fr/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/). Les hubs associés sont le [Hub AI HBM](/fr/page/korea-semiconductor-hbm-kospi-hub/) et le [Hub Exclusive Analysis](/fr/page/exclusive-analysis-hub/).

## TL;DR

* L'hypothèse selon laquelle « le premier poste d'exportation coréen se fait remplacer, sur son plus grand marché, par des fournisseurs locaux de ce pays » est <strong>fondée dans sa direction</strong>. Mais le stade actuel relève moins d'un risque sur les résultats 2026 que d'un <strong>risque structurel qui abaisse, à partir de 2028, l'ASP, la part de marché et le multiple approprié de la mémoire grand public</strong>.
* Le canal le plus dangereux n'est pas la baisse du chiffre d'affaires en Chine elle-même. L'effet de second tour, à savoir <strong>la baisse de l'ASP mondial provoquée par le déplacement des volumes excédentaires vers l'étranger</strong>, pèse davantage.
* L'exposition à la Chine lue dans les publications repose sur des bases différentes selon les sociétés, ce qui rend toute comparaison directe impossible. Samsung Electronics <strong>30,1%</strong> (base tous segments confondus), SK Hynix <strong>24,3%</strong> (siège de la filiale de vente), Micron <strong>10,1%</strong> (siège social du client) : chacun de ces chiffres est un <strong>proxy</strong> qui mesure une chose différente.
* Deux idées reçues méritent d'être corrigées. La part Chine+Hong Kong (~45%) dans les exportations de semi-conducteurs repose sur un <strong>critère de destination douanière</strong> : en tenant compte des réexportations via Hong Kong, elle peut surestimer la demande finale réelle. L'affirmation « le HBM n'entre absolument pas en Chine » est elle aussi trop catégorique : les produits dont la densité de bande passante mémoire est inférieure à 3,3 Go/s/mm² bénéficient d'une exception conditionnelle.
* Ce qui distingue CXMT du passé, ce n'est pas la taille du financement mais sa structure. Sur une levée de <strong>~57,9 Mds RMB (8,1 Mds USD)</strong>, <strong>des acheteurs sont entrés au capital en tant qu'actionnaires</strong>. Le financement et la sécurisation de clients avancent donc de front. \[Portée\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Thèse principale</div>
  <div class="thesis-callout__body">
    La localisation chinoise n'est pas un déclencheur unique justifiant de vendre immédiatement Samsung Electronics et SK Hynix, mais la variable de décote la plus importante à intégrer au bénéfice 2028 et au multiple terminal. Le signal discriminant n'est pas la part de marché en Chine, mais le fait qu'elle se propage ou non à une baisse des prix contractuels mondiaux.
  </div>
</div>

---

## 1. Hypothèse et verdict

Reformulons d'abord l'hypothèse avec précision. Les semi-conducteurs représentent 38,7% des exportations coréennes du premier semestre, et la Chine est le premier marché de cette industrie. Le HBM étant bloqué par les sanctions, l'essentiel des exportations vers la Chine se compose de DRAM et de NAND grand public, exactement le segment que visent CXMT (ChangXin Memory) et YMTC (Yangtze Memory). En intégrant la production et les ventes locales en Chine, qui n'apparaissent pas dans les statistiques d'exportation, l'exposition réelle est encore plus grande. Avec l'afflux massif de financements publics chinois qui s'y ajoute, la localisation va se poursuivre.

<strong>La direction est fondée.</strong> Mais il faut distinguer le calendrier de la trajectoire.

Le canal le plus dangereux n'est pas la disparition du chiffre d'affaires en Chine.

```text
Substitution par l'offre domestique chinoise
→ Transfert des volumes excédentaires de Samsung, SK Hynix et Micron vers l'étranger
→ Baisse de l'ASP mondial du DRAM et du NAND
→ Chute brutale des profits sous l'effet de coûts fixes élevés
```

Cet <strong>effet de second tour</strong> pèse plus lourd que l'effet de premier tour. Les volumes non écoulés en Chine ne disparaissent pas : ils se redirigent vers d'autres marchés. Comme la part de coûts fixes de la mémoire est élevée, un léger recul de l'ASP suffit à ébranler fortement les profits. \[Inférence : analyse du canal de transmission\]

---

## 2. L'exposition à la Chine des trois sociétés : décomposition par les publications

| Société | Part du chiffre d'affaires lié à la Chine (publications) | Base de publication | Site de production en Chine | Lecture |
|---|---:|---|---|---|
| Samsung Electronics | 2025 : <strong>30,1%</strong> | CA Chine 71,6 billions KRW ÷ CA social 238,0 billions KRW | Xi'an NAND | Smartphones, électroménager et semi-conducteurs confondus ; la part mémoire seule n'est pas publiée |
| SK Hynix | 2026 T1 : <strong>24,3%</strong>, 2025 : 19,7% | Siège de la filiale de vente en Chine | Wuxi DRAM, Dalian NAND | Des trois sociétés, l'exposition mémoire à la Chine la plus directement vérifiable |
| Micron | FY2025 Chine 7,1% + Hong Kong 3,0% = <strong>10,1%</strong> | Siège social du client | La Chine n'héberge que le back-end | Déjà en net repli, contre 16,4% en 2024 |

\[Fait : publications de chaque société\]

### Samsung Electronics : un chiffre important, mais la part mémoire reste inconnue

En 2025, le chiffre d'affaires en Chine s'est élevé à 71,6 billions KRW, soit 30,1% du chiffre d'affaires social (comptes non consolidés). Mais <strong>le chiffre d'affaires chinois du seul segment mémoire n'est pas publié</strong>. Le chiffre d'affaires mémoire consolidé de la même année atteint 104,1 billions KRW, mais on ne peut pas croiser ces deux données, l'une en comptes sociaux et l'autre en comptes consolidés, pour en déduire le chiffre d'affaires mémoire en Chine. Diviser des chiffres qui reposent sur des périmètres comptables différents donne une réponse fausse. \[Non vérifié\]

### SK Hynix : l'indicateur le plus direct, mais en rebond

La trajectoire de la part du chiffre d'affaires de la filiale de vente chinoise est instructive.

| Période | Part |
|---|---:|
| 2023 | 30,9% |
| 2024 | 23,5% |
| 2025 | 19,7% |
| 2026 T1 | <strong>24,3%</strong> |

Le ratio a baissé avant de remonter (30,9% → 23,5% → 19,7% → 24,3%). Mais cette fluctuation intègre aussi l'effet de la hausse de la part américaine tirée par le HBM, et ne doit donc pas être lue comme un pur changement de l'exposition à la Chine. \[Inférence : effet de composition\]

### Micron : un cas déjà vécu

La part Chine+Hong Kong est passée de 16,4% en 2024 à 10,1% en 2025. C'est le résultat, déjà intégré, de l'interdiction prononcée en 2023 par les autorités chinoises de cybersécurité, qui a bloqué l'achat de produits Micron par les opérateurs d'infrastructures d'information critiques. La Chine n'héberge aucun fab de front-end, seulement des installations d'assemblage et de test.

<strong>Les trois chiffres reposent sur des bases différentes et ne se comparent pas directement.</strong> Base tous segments confondus (Samsung), siège de la filiale de vente (SK Hynix), siège social du client (Micron) : chacun mesure quelque chose de différent. Plus précisément, ce sont des <strong>proxys d'exposition à la Chine</strong>. \[Inférence : différence de base\]

---

## 3. Les données d'exportation coréennes : ce qui est confirmé, ce qui appelle la prudence

<strong>Ce qui est confirmé</strong> : sur des exportations totales de 496,7 Mds USD au premier semestre, les semi-conducteurs représentent 192,4 Mds USD, soit très précisément 38,7% une fois le calcul fait. \[Fait : ministère du Commerce, de l'Industrie et de l'Énergie\]

```text
192,4 Mds USD ÷ 496,7 Mds USD = 38,7%
```

<strong>Ce qu'il faut noter</strong> : la part Chine+Hong Kong des exportations de semi-conducteurs, ~45%, repose sur un <strong>critère de destination douanière</strong>. Hong Kong étant une plaque tournante de réexportation et de distribution, interpréter ce chiffre tel quel comme « 45% de demande finale chinoise » peut conduire à une surestimation. \[Inférence : interprétation de la base statistique\]

Cette correction ne change toutefois pas l'orientation d'ensemble. Le fait que la Chine reste le premier pôle de demande et d'assemblage pour la mémoire coréenne demeure inchangé.

---

## 4. Les restrictions sur le HBM : « n'entre absolument pas » est une formule trop forte

L'affirmation « le HBM n'entre pas en Chine à cause des sanctions américaines » est légèrement excessive. Les HBM les plus avancés nécessitent aujourd'hui une licence d'exportation vers la Chine et sont de fait fortement restreints, mais <strong>une partie des produits dont la densité de bande passante mémoire est inférieure à 3,3 Go/s/mm² bénéficie d'une exception conditionnelle</strong>. \[Fait : réglementation du BIS américain\]

Plus précisément :

| Produit | Exportation vers la Chine |
|---|---|
| HBM3E, HBM4 et gammes équivalentes | Restreinte de fait |
| HBM d'entrée de gamme (densité de bande passante inférieure à 3,3 Go/s/mm²) | Possible, de façon limitée |

En conséquence, le chiffre d'affaires vers la Chine présente vraisemblablement une part relativement élevée de DDR4, DDR5, LPDDR, NAND grand public et SSD. Le cœur de l'hypothèse (les exportations vers la Chine se concentrent sur le grand public) reste valable même après cette correction. Mais aucun tableau croisé produit/région par société n'est publié. \[Non vérifié\]

---

## 5. Ce qui distingue la localisation chinoise du passé

C'est là le vrai changement dans ce dossier. CXMT a dépassé le simple stade de projet soutenu par l'État.

- Selon les conditions finales de l'offre de juillet 2026, une levée d'environ <strong>57,9 Mds RMB, 8,1 Mds USD</strong> est prévue
- Parmi les investisseurs stratégiques figurent <strong>Alibaba Cloud, Xiaomi, ZTE, Transsion, TCL, NIO et Chery</strong>
- Une structure où, au-delà des fournisseurs, <strong>de véritables acheteurs entrent au capital en tant qu'actionnaires</strong>

\[Fait : documents d'introduction en bourse de CXMT, Bourse de Shanghai\]

Le dernier point est décisif. Cela signifie que le financement et la sécurisation de clients avancent <strong>simultanément</strong>. Si le soutien chinois passé aux semi-conducteurs pouvait se résumer à « l'argent est là, mais pas les débouchés », cette fois, les actionnaires sont directement les clients. \[Inférence : implications de la composition actionnariale\]

YMTC a lui aussi inscrit à son catalogue officiel du Gen4/Gen5 TLC/QLC 3D NAND. Sur les marchés chinois du SSD grand public, du mobile et de l'embarqué au moins, l'entreprise semble avoir dépassé le stade du simple « substitut low-cost ». \[Fait : catalogue produits YMTC\]

---

## 6. Impact par société

### Samsung Electronics : l'exposition la plus large, mais aussi la plus forte capacité d'absorption

Samsung Electronics présente vraisemblablement l'exposition absolue la plus large des trois, à la fois en DRAM et en NAND grand public. Avec son fab NAND de Xi'an, l'entreprise <strong>se trouve exposée des deux côtés</strong>, à la localisation chinoise comme aux restrictions américaines sur les équipements.

Mais avec le HBM, la DRAM serveur, le NAND, la fonderie et le mobile réunis dans un même portefeuille, sa capacité d'absorption du choc est également la plus forte des trois. Le risque chinois n'est pas tant un facteur d'effondrement global des résultats de Samsung Electronics qu'<strong>une variable qui abaisse à la fois la marge de pic de la mémoire et le plafond du multiple</strong>. \[Inférence : effet de portefeuille\]

### SK Hynix : le HBM comme bouclier, mais des actifs de front-end exposés

En 2026-2027, la part élevée du HBM dans les profits devrait permettre à SK Hynix de mieux résister que quiconque à la substitution en mémoire grand public. Mais la part du chiffre d'affaires chinois est remontée à 24,3%, et l'entreprise détient aussi des <strong>actifs de front-end en DRAM à Wuxi et en NAND à Dalian</strong>.

Le BIS américain a posé le principe d'autoriser les équipements destinés à l'exploitation courante des fabs chinois existants, tout en <strong>n'autorisant ni extension de capacité ni montée en gamme technologique</strong>. \[Fait : réglementation du BIS\] Si Wuxi et Dalian restent enfermés dans des procédés anciens tout en devant concurrencer CXMT et YMTC, l'efficacité des actifs pourrait se dégrader sur le long terme. \[Inférence : trajectoire de vieillissement des actifs\]

### Micron : exposition directe faible, mais pas sans risque

Le chiffre d'affaires direct en Chine et le risque sur les actifs de front-end chinois sont, des trois, les plus faibles pour Micron. Cela ne signifie pas pour autant une position sans risque.

Micron est déjà exclu du marché chinois des infrastructures critiques, et sa pureté d'activité en DRAM et NAND fait que <strong>sa sensibilité aux profits est élevée dès lors que les volumes chinois pèsent sur l'ASP mondial</strong>. Micron indique elle-même, dans son 10-K, que le soutien de l'État chinois à CXMT et YMTC pourrait déclencher une surcapacité en DRAM et en NAND ainsi qu'une concurrence agressive sur les prix. \[Fait : 10-K de Micron\]

Même sans vendre en Chine, on ne peut échapper à l'effet des volumes fabriqués en Chine s'ils pèsent sur les prix mondiaux. Micron a beau afficher l'exposition directe la plus faible des trois, elle se révèle la plus vulnérable face à l'effet de second tour.

---

## 7. Lecture temporelle

| Période | Impact chinois attendu | Lecture pour l'investissement |
|---|---|---|
| 2026-2027 | Extension de la substitution en mémoire grand public pour le consommateur, le mobile et le PC en Chine | Plafonnement du multiple plus qu'effondrement des résultats |
| 2027-2028 | Montée en capacité de CXMT et YMTC et stabilisation des rendements | <strong>La question clé est la contagion ou non à l'ASP mondial</strong> |
| Après 2028 | Extension possible des qualifications serveur, automobile, SSD haute performance et HBM | Risque structurel sur la part de marché de Samsung, SK Hynix et Micron |

\[Inférence : estimation temporelle\]

Les entreprises chinoises doivent encore franchir les barrières de qualification et de rendement sur la DRAM serveur haute performance pour les hyperscalers mondiaux, le SSD d'entreprise, la fiabilité de qualité automobile et le HBM avancé. <strong>Le financement lui-même est donc un signal d'alerte, mais pas encore un signal confirmé de surcapacité.</strong>

---

## 8. Verdict final : comment l'intégrer au cours

L'hypothèse est juste dans sa direction. Mais son intégration au cours actuel exige de faire des distinctions.

| Élément | Jugement |
|---|---|
| EPS 2026-2027 | L'argument d'un effondrement direct reste pour l'instant insuffisant |
| EPS 2028 | Nécessite d'intégrer prudemment la part de marché chinoise et l'ASP mondial |
| Multiple approprié | Justifie la difficulté croissante à accorder un multiple élevé au bénéfice de pic, comme par le passé |
| Signal de confirmation le plus important | La hausse de part de marché de CXMT et YMTC reste-t-elle confinée au marché intérieur chinois, ou <strong>se propage-t-elle à une baisse des prix contractuels mondiaux de DRAM et de NAND</strong> |

En définitive, la localisation chinoise ne doit pas être traitée comme un déclencheur unique justifiant de vendre immédiatement Samsung Electronics ou SK Hynix, mais élevée au rang de <strong>variable de décote la plus importante à intégrer au bénéfice 2028 et au multiple terminal</strong>. \[Inférence : jugement synthétique\]

Cette conclusion s'articule précisément avec la structure calculée dans [la juste valeur des semi-conducteurs](/fr/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/), où le cours était défini comme le FCFE 2026-2028 additionné d'une terminal value normalisée de 2029. La localisation chinoise est précisément <strong>la variable qui relève le taux d'actualisation de cette terminal value</strong>.

---

## 9. Signaux à surveiller

- <strong>Contagion aux prix contractuels mondiaux</strong> : les volumes de CXMT et YMTC exercent-ils une pression sur les prix contractuels de DDR5, LPDDR et consumer NAND hors de Chine
- <strong>Extension des qualifications de CXMT</strong> : l'entreprise obtient-elle des qualifications auprès de clients serveur et automobile mondiaux, au-delà du marché intérieur chinois
- <strong>SK Hynix, Wuxi et Dalian</strong> : ces sites restent-ils enfermés dans des procédés anciens sous la réglementation du BIS, et comment évolue leur efficacité d'actifs
- <strong>Samsung Electronics, Xi'an</strong> : la double pression des restrictions sur les équipements et de la localisation chinoise se reflète-t-elle dans les résultats
- <strong>Part chinoise de Micron</strong> : continue-t-elle de reculer sous les 10,1%, avec en contrepartie une sensibilité croissante à l'ASP mondial

---

## Conclusion

Le cœur de l'hypothèse est juste. Une dynamique où le premier poste d'exportation coréen se fait remplacer, sur son plus grand marché, par des fournisseurs locaux de ce marché est en train de s'enclencher. L'entrée d'acheteurs au capital de CXMT en est la preuve.

Mais la décision d'investissement exige de distinguer <strong>le calendrier de la trajectoire</strong>. L'argument d'un effondrement des résultats causé par une chute brutale du chiffre d'affaires chinois en 2026 reste, à ce stade, insuffisant. Le risque le plus précis est l'effet de second tour de 2027-2028, quand les volumes évincés de Chine basculent vers le marché mondial et pèsent sur l'ASP ; il se manifeste d'abord dans <strong>la pérennité du bénéfice après 2028 et le multiple terminal</strong>, avant d'apparaître dans les résultats eux-mêmes.

Ce qu'il faut donc surveiller aujourd'hui, ce ne sont pas les nouvelles de part de marché en Chine, mais <strong>les prix contractuels mondiaux</strong>. Tant que la contagion n'est pas confirmée, la localisation chinoise n'est pas une perte actée, mais une variable de décote.

---

_Cette publication est une analyse fondée sur les documents de chaque société (rapport annuel 2025 de Samsung Electronics, formulaire F-1/A de SK Hynix, 10-K FY2025 de Micron), les statistiques d'import-export du ministère du Commerce, de l'Industrie et de l'Énergie, les documents d'introduction en bourse de CXMT à la Bourse de Shanghai, le catalogue produits de YMTC et la réglementation du BIS américain. Les parts de chiffre d'affaires chinois des trois sociétés reposent sur des bases de publication différentes (tous segments confondus, siège de la filiale de vente, siège social du client) et constituent des proxys qui ne se comparent pas directement. Le chiffre d'affaires chinois du seul segment mémoire de Samsung Electronics et les tableaux croisés produit/région par société ne sont pas publiés ; la lecture temporelle et le canal de transmission sont des estimations arrêtées au moment de la rédaction. Les titres mentionnés sont des exemples destinés à illustrer une structure industrielle et ne constituent pas une recommandation d'achat ou de vente d'un titre particulier. La décision d'investissement et sa responsabilité incombent à l'investisseur lui-même._

---

### Articles associés

- [IPO de CXMT et risque sur les prix mémoire : HBM n'est pas le premier point de rupture](/fr/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)
- [Le prix des API d'IA chinoises est-il soutenable ? Vérifier la structure de coûts par les publications financières](/fr/post/china-ai-api-pricing-sustainability-cost-structure-2026-07-18/)
- [Ce que change vraiment la convergence des modèles ouverts chinois : redistribution de la chaîne de valeur, pas effondrement de la demande](/fr/post/china-open-model-convergence-value-chain-redistribution-2026-07-17/)
- [Les semi-conducteurs sont-ils cycliques et quelle est la juste valeur ? Valoriser Samsung, SK Hynix et Micron avec le FCFE et les bénéfices normalisés](/fr/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [Le vrai débat des semi-conducteurs : quatre horloges physiques et une horloge boursière](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
