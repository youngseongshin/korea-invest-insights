---
title: "Recherche approfondie sur l'offre et la demande de HBM 2030 : disséquer le modèle de demande de 26,7EB face au calendrier de capacité"
slug: "hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13"
date: 2026-07-13T11:00:00+09:00
description: "Nous reproduisons de façon indépendante l'affirmation de 26,7EB de demande contre 10,6EB d'offre de HBM en 2030 (un déficit de 2,5x), puis la confrontons à la prévision de 24x de tokens de Goldman, aux contre-preuves d'efficacité DeepSeek MLA et TurboQuant, et au calendrier de capacité des Big 3. Analyse de structure, pas un conseil d'investissement."
categories: ["Exclusive Analysis", "Tech-Analysis", "Market-Outlook"]
tags: ["HBM", "Offre-Demande mémoire", "AI Memory", "SK Hynix", "Samsung Electronics", "Micron", "KV Cache", "Infrastructure IA", "Capacité semi-conducteurs"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte
> Si [Comparaison des technologies mémoire IA HBM, HBF, HBC](/fr/post/hbm-hbf-hbc-ai-memory-comparison-2026-06-22/) traitait de l'identité technique, cet article mène une recherche approfondie sur <strong>la façon dont l'offre et la demande de cette technologie se rencontrent d'ici 2030</strong>. À lire avec [Valeur du token IA et valeur ajoutée mémoire](/fr/post/ai-token-value-memory-value-added-2026-07-09/), [Les résultats de la Big Tech fin juillet et les scénarios de thèse mémoire](/fr/post/big-tech-july-earnings-call-memory-thesis-scenarios-2026-07-07/), et [Le consensus semi-conducteurs 2027 : qui paie la facture](/fr/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/). Les hubs associés sont [le hub AI HBM](/fr/page/korea-semiconductor-hbm-kospi-hub/) et [le hub Exclusive Analysis](/fr/page/exclusive-analysis-hub/).

## TL;DR

* Nous avons reproduit de façon indépendante, par calcul ouvert, le récit qui circule sur le marché : <strong>demande de HBM 2030 de 26,7EB, offre de 10,6EB, déficit de 2,5x</strong>. L'arithmétique elle-même se reproduit. La question est de savoir sur quelles hypothèses ce chiffre repose.
* 26,7EB n'est pas une erreur de comparaison entre stock et flux. C'est une valeur où la demande et l'offre sont toutes deux converties en <strong>stock de HBM installé et en service</strong>, puis comparées. Mais cela n'apparaît que si plusieurs hypothèses haussières, tokens x24, empreinte modèle x5, contexte x4, taux de rétention KV de 70 %, se vérifient simultanément.
* Nous avons croisé trois angles de vérification : (1) la structure du modèle de demande, (2) les fondements haussiers des hypothèses de demande et les contre-preuves d'efficacité technique, (3) le calendrier de capacité des Big 3. Les trois angles convergent <strong>vers une seule conclusion, sans contradiction</strong>.
* La conclusion <strong>sépare la direction de l'ampleur</strong>. `Tension jusqu'en 2027` est une hypothèse à confiance élevée, `amélioration de l'offre à partir de 2028` est cohérente avec les calendriers officiels de capacité, mais `un déficit exactement de 2,5x encore en 2030` est un scénario à biais haussier.
* Cet article ne formule aucun jugement d'achat ou de conservation sur un titre particulier. C'est une analyse qui dissèque la structure de l'offre et de la demande du secteur. \[Portée\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Thèse principale</div>
  <div class="thesis-callout__body">
    Le vrai débat sur l'offre et la demande de HBM n'est pas de savoir si le déficit atteindra 2,5x en 2030, mais que la direction du déficit est robuste tandis que son ampleur est sensible aux hypothèses. La tension de 2027 et l'amélioration de l'offre en 2028 sont soutenues par les données, tandis que le chiffre de 2,5x est un scénario à biais haussier qui ne tient que si plusieurs hypothèses de demande se vérifient toutes en même temps.
  </div>
</div>

---

## 1. Cadrage du débat : que vérifie-t-on

Un récit puissant circule sur le marché de la mémoire IA. Il affirme qu'en 2030, la demande de HBM atteindra 26,7 exaoctets (EB) alors que l'offre plafonnera à 10,6EB, laissant un <strong>déficit structurel d'environ 2,5x</strong>. Ce chiffre provient d'un modèle d'analyse indépendant (Memory Analyst) et s'est diffusé à travers de nombreuses vidéos YouTube et rapports.

Cette recherche approfondie répond à quatre questions. \[Questions de vérification\]

1. La formule `26,7EB contre 10,6EB` est-elle cohérente en interne ?
2. Les hypothèses de demande sont-elles justifiées par des sources publiques et par la structure du modèle ?
3. Le déficit de 2030 subsiste-t-il même en tenant compte des extensions de capacité de Samsung Electronics, SK Hynix et Micron ?
4. Comment le marché absorbe-t-il réellement ce chiffre en pratique ?

Avant d'entrer dans le vif du sujet, une précision pour ne pas brouiller la conclusion : cet article ne recalcule ni le cours actuel ni un multiple raisonnable. Il traite uniquement <strong>de la fiabilité de la direction et de l'ampleur de l'offre et de la demande</strong>.

---

## 2. Premier angle : disséquer le modèle de demande de 26,7EB

### 2.1 Une comparaison de stock à stock (dissiper un malentendu courant)

Le premier malentendu à écarter est l'idée que « comparer une demande de 26,7EB à une offre de 10,6EB revient à comparer, à tort, une consommation annuelle à une production annuelle ». La vérification montre que <strong>ce n'est pas une erreur</strong>. Le modèle d'origine compare deux stocks. \[Fait\]

- <strong>Need (besoin)</strong> : le stock de HBM qui doit être installé et allumé pour traiter la charge de travail d'inférence IA de l'année considérée
- <strong>Serving fleet (flotte en service)</strong> : le stock de HBM produit au cours des cinq dernières années environ, affecté à l'inférence, ajusté de l'efficacité liée au vieillissement, et non encore mis hors service

Autrement dit, les deux chiffres ne sont pas des flux mais des stocks. La structure du modèle d'origine, `fleet = output des ~5 dernières années × part d'inférence − frictions`, rend cette conversion explicite. Sur le plan stock-flux, c'est cohérent. \[Inférence\] Cela dit, le taux d'allocation à l'inférence qui convertit le flux en stock, la durée de vie de 5 ans, et l'efficacité par génération ne sont pas des standards industriels vérifiés de façon indépendante, mais des <strong>hypothèses du modèle</strong>.

### 2.2 Reproduire telle quelle la formule de demande de 26,7EB

Nous avons repris tels quels la formule simplifiée publiée par le modèle d'origine et les valeurs d'entrée du scénario de base 2030, pour une reproduction indépendante.

```text
traffic = 24  (24x par rapport à 2026, 120 quadrillions de tokens mensuels)
replicaIndex = 24^0.90 / 11 = 1.5878

weights = 1.75 × 1.5878 × 5 / 1.75 = 7.939EB
contextBucket = 4 × 1.5 / 4 × 0.70 = 1.05
kv = 1.27 × 24^0.55 × 1.05 = 7.658EB
scratch = (7.939 + 7.658) × 0.15 = 2.340EB

need = (7.939 + 7.658 + 2.340) × 1.10 / 0.74 = 26.66EB ≈ 26.7EB
```

En décomposant la demande par composante, on obtient :

| Composante de la demande 2030 | EB | Part |
|---|---:|---:|
| Resident weights (poids résidents) | 7,94 | 44,3 % |
| KV cache | 7,66 | 42,7 % |
| Scratch (mémoire de travail temporaire) | 2,34 | 13,0 % |
| Sous-total (avant redondance et utilisation) | 17,94 | 100,0 % |
| Besoin d'installation final (×1,10 / 0,74) | 26,66 | - |

\[Fait\] L'arithmétique du 26,7EB se reproduit par la formule publique. Il est important de noter que les poids résidents et le cache KV représentent respectivement 44 % et 43 %, soit l'essentiel de la demande. Ce sont précisément ces deux postes qui constituent la cible directe des gains d'efficacité technique évoqués plus loin.

\[Non vérifié\] Le calculateur comporte cependant une valeur d'entrée distincte, `frontier/HBM-served share 70 %`, dont l'intégration précise dans la formule simplifiée publiée n'est pas clairement établie. Tant qu'un audit au niveau du code n'aura pas été mené, nous ne validons pas le 26,7EB comme un modèle indépendant complet.

### 2.3 Lire correctement le taux de croissance

Le `CAGR sur 5 ans` fréquemment cité comporte une erreur de comptage de période. De 2026 à 2030, il y a 5 points d'observation mais <strong>seulement 4 périodes de capitalisation</strong>.

| Poste | 2026 | 2030 | Multiple | CAGR exact sur 4 périodes |
|---|---:|---:|---:|---:|
| Besoin d'installation HBM | 4,8EB | 26,7EB | 5,56x | <strong>53,6 %</strong> |
| Serving fleet | 3,75EB | 10,6EB | 2,83x | <strong>29,7 %</strong> |

Par ailleurs, la trajectoire de production annuelle de HBM du modèle d'origine, `de 2,8EB en 2024 à 7,6EB en 2030`, correspond à un CAGR sur 6 périodes de <strong>18,1 %</strong>. Le `serving fleet de 10,6EB` n'est pas une production annuelle mais un stock cumulé et déprécié de plusieurs années de production ; il ne faut pas confondre les deux. \[Fait\]

Si la demande croît de 53,6 % par an tandis que le stock d'offre croît de 29,7 % par an, la direction dans laquelle l'écart se creuse est, en soi, arithmétiquement évidente. La vraie question est la robustesse des hypothèses d'entrée de ces deux taux de croissance.

---

## 3. Deuxième angle : les fondements haussiers des hypothèses de demande et leurs contre-preuves

### 3.1 Fondements haussiers confirmés de la demande

Les preuves d'une demande forte existent réellement. \[Fait\]

- Goldman Sachs Research prévoit que la consommation mensuelle de tokens augmentera de <strong>24x</strong> entre 2026 et 2030, pour atteindre 120 quadrillions.
- Le même document estime que les requêtes LLM quotidiennes atteindront 11 milliards d'ici 2030, avec une croissance annuelle moyenne d'environ 40 %.
- La capacité HBM par accélérateur a augmenté à chaque génération de NVIDIA.
- Micron a indiqué, en juin 2026, que la demande de DRAM et de NAND dépasse largement l'offre et que cette tension <strong>persistera au-delà de 2027</strong>.
- Micron a signé 16 accords stratégiques clients (SCA) et a déclaré que le revenu cumulé au prix plancher de 14 de ces contrats s'élève à environ 100 milliards de dollars, avec 22 milliards de dollars d'engagements de trésorerie et de financement associés. Toutefois, le HBM ne représente qu'une partie de ces contrats, pas la totalité.

### 3.2 Des contre-arguments présents dans la même source

Un point intéressant : la source même citée comme preuve haussière, le document de Goldman, contient aussi des arguments contraires. \[Fait\]

- Goldman anticipe une pénurie de puces à court terme, tout en précisant explicitement que <strong>lorsque de nouvelles capacités de production arrivent, le secteur peut rattraper son retard en environ deux ans</strong>.
- Goldman explique que le coût par token d'inférence baisse de 60 à 70 % par an. Cette baisse des prix augmente l'usage, mais elle réduit aussi la charge mémoire physique d'une même charge de travail.
- Point déterminant : le facteur 24x de Goldman n'est pas une prévision de demande en bits de HBM, mais une prévision de <strong>trafic de tokens</strong>. La conversion « des tokens vers les sessions simultanées, le contexte, le KV et les poids, puis vers la rétention en HBM » repose entièrement sur des hypothèses de modèle distinctes.

\[Inférence\] Les prévisions de Goldman soutiennent donc la croissance de l'usage de l'IA, mais ne soutiennent pas directement `un déficit de HBM de 2,5x en 2030`. Cette distinction est souvent omise lorsque le récit haussier cite Goldman.

### 3.3 Contre-preuves de structure de modèle et d'efficacité

Les poids et le cache KV, cœur de la formule de demande, sont la cible directe des progrès techniques. \[Fait\]

- L'exemple du modèle d'origine, environ <strong>504 Ko/token</strong> pour le cache KV, provient du cas de <strong>Llama 3.1 405B</strong>. Ce n'est pas une valeur universelle pour tous les frontier models.
- La série DeepSeek-V3/R1 augmente considérablement l'efficacité KV et de calcul grâce à la Multi-head Latent Attention (MLA) et au Mixture-of-Experts (MoE).
- TurboQuant, de Google Research, présente des résultats de benchmarks publics montrant une réduction de la mémoire KV d'<strong>au moins 6x</strong>.

\[Inférence\] Cependant, TurboQuant est un résultat de recherche portant sur le cache KV. Cela ne réduit pas de 6x les poids, le scratch et la redondance, et ce n'est pas non plus une moyenne industrielle validée en environnement de production à grande échelle en termes de latence, de débit et de qualité.

La conclusion honnête consiste donc à exclure les deux extrêmes. `504 Ko/token × toutes les charges de travail futures` est une surestimation, et `compression KV de 6x × HBM total` est une sous-estimation. La demande future se situe entre ces deux extrêmes, et l'élément clé est <strong>la façon dont évolue la composition entre poids et KV</strong>.

---

## 4. Troisième angle : croiser le calendrier de capacité des Big 3

### 4.1 La capacité de fab et l'offre effective de HBM sont deux choses différentes

Une erreur courante dans l'analyse de l'offre consiste à convertir directement les annonces de démarrage ou d'achèvement de fab en HBM vendable. Cinq écarts séparent les deux. \[Fait/Inférence\]

1. <strong>Hausse de la die intensity</strong> : lorsque le nombre de die par stack passe de 12 à 16 couches, le nombre de die nécessaire pour un même nombre de stacks augmente d'environ 33 %. Même si le nombre de wafers augmente, le taux de croissance des stacks vendables peut être inférieur.
2. <strong>Trade ratio du HBM</strong> : le HBM consomme davantage de ressources de wafer et de procédé que la DRAM standard. Micron a lui-même indiqué que ce ratio augmente à chaque génération, ce qui comprime l'offre de mémoire non-HBM.
3. <strong>Back-end, rendement et certification</strong> : good die, empilement TSV, base die, advanced packaging, spécifications thermiques et de puissance, certification client, toutes ces étapes doivent être franchies pour constituer une offre effective.
4. <strong>Décalage de montée en cadence</strong> : l'ouverture d'une salle blanche ou le premier wafer diffèrent du volume qualifié pouvant être comptabilisé en revenu.
5. <strong>Coût d'opportunité entre produits</strong> : l'augmentation de la production de HBM peut empiéter sur les wafers de DRAM standard. Même si le HBM augmente, rien ne garantit une stabilisation immédiate du prix global de la DRAM.

### 4.2 Calendrier officiel de capacité

Voici le calendrier des Big 3 et du secteur dans son ensemble, tel que confirmé par des sources primaires publiques.

| Entreprise / poste | Confirmation officielle | Interprétation de la contribution réelle à l'offre |
|---|---|---|
| SK Hynix M15X | Achèvement visé en novembre 2025, production de DRAM et HBM nouvelle génération | Axe d'extension le plus rapide pour 2026-27. La montée en cadence pourrait être rapide grâce à l'infrastructure existante |
| SK Hynix Yongin phase 1 | 21 600 milliards de wons d'investissement en équipement, première salle blanche visée pour février 2027, ouverture anticipée | Début de l'installation en 2027, possibilité d'un effet d'offre élargi à partir de 2028 |
| SK Hynix Yongin, ensemble | Première salle blanche des 4 fabs visée pour 2033 | L'hypothèse que les 4 fabs de Yongin contribuent tous à l'offre 2030 est erronée |
| Samsung Electronics HBM4 | Début de production de masse et d'expédition commerciale en février 2026, revenu HBM 2026 anticipé en hausse de plus de 3x | Le retour de Samsung comme second-source en 2026-27 est le principal facteur d'assouplissement de l'offre |
| Investissement long terme de Samsung Electronics | Environ 2 100 000 milliards de wons dans les semi-conducteurs sur 2026-2040, environ 1 650 000 milliards de wons à Yongin et sur les sites existants, fabs HBM à Onyang et Cheonan | Orientation forte mais enveloppe jusqu'en 2040. Non directement convertible en volume d'offre 2030 |
| Micron ID1 | Premier wafer mi-2027 | En tenant compte de la certification client, une commercialisation significative n'interviendra que fin 2027 début 2028 |
| Micron ID2 | Premier wafer fin 2028 | Contribue à l'assouplissement de l'offre à partir de 2029 |
| Micron Tongluo et packaging | Expéditions significatives de Tongluo au FY2028, extension du packaging HBM dès le premier semestre 2027 | Assouplit simultanément les goulots d'étranglement du front-end et du back-end |
| SEMI, mémoire globale | Capacité mémoire 300mm anticipée à 4,1 M WPM en 2026, 4,2 M WPM en 2027 | La croissance globale de la capacité wafer reste modérée, environ 2,4 %. La bascule du mix HBM et la croissance des bits par nœud sont plus déterminantes |

### 4.3 Verdict côté offre

- \[Fait\] Les Big 3 mènent tous des investissements à grande échelle.
- \[Fait\] 2027 est l'année où les salles blanches et les premiers wafers commencent à se multiplier, mais ce n'est pas l'année où tout ce volume bascule en output qualifié.
- \[Inférence\] L'assouplissement de l'offre devient probablement visible à partir de 2028 et s'accentue vraisemblablement en 2029-30.
- \[Non vérifié\] Les sources publiques ne permettent pas de trancher si le serving fleet 2030 sera de 10,6EB ou de 15EB. Le WPM précis, le mix produit, le rendement et la capacité de packaging ne sont pas publics.

---

## 5. Analyse de sensibilité combinant les trois angles

Nous avons rassemblé la direction indiquée par les trois angles dans un seul tableau de sensibilité. Le serving fleet côté offre est fixé à 10,6EB, et seules les hypothèses de demande sont recalculées de façon indépendante avec la formule publique.

| Scénario | Hypothèse modifiée | Demande 2030 | Demande/offre | Verdict |
|---|---|---:|---:|---|
| Base du modèle d'origine | Tokens x24, modèle x5, efficacité KV x4, taux de rétention 70 % | 26,7EB | 2,52x | Déficit fort |
| Empreinte modèle assouplie | Multiple modèle de 5x à 2x | 18,5EB | 1,75x | Déficit |
| Amélioration efficacité KV | Efficacité KV de 4x à 6x | 22,3EB | 2,10x | Déficit |
| Baisse du taux de rétention HBM | De 70 % à 50 % | 22,9EB | 2,16x | Déficit |
| Croissance des tokens divisée par deux | De 24x à 12x | 16,2EB | 1,53x | Déficit |
| Bear composite | Tokens x12, modèle x2, efficacité KV x6, rétention 50 %, throughput x14 | 6,5EB | 0,62x | Excédent d'offre |
| Bull composite | Tokens x36, modèle x8, efficacité KV x3, rétention 80 %, throughput x8 | 67,9EB | 6,41x | Déficit extrême |

Les scénarios bear et bull composites ne sont pas des scénarios officiels du modèle d'origine, mais des tests de résistance indépendants destinés à observer la covariance entre hypothèses.

L'interprétation de ce tableau est le cœur de cette recherche approfondie.

<strong>Premièrement, modifier une seule variable ne fait pas disparaître facilement le déficit.</strong> Même en abaissant le multiple modèle de 5x à 2x, même en divisant par deux la croissance des tokens, un déficit subsiste (1,5 à 1,75x). C'est l'argument sur lequel s'appuie le récit haussier : « quelle que soit l'hypothèse que l'on secoue, le déficit persiste ».

<strong>Deuxièmement, les variables ne sont cependant pas indépendantes entre elles.</strong> Le ralentissement de la croissance des tokens, l'essor des petits modèles et du MoE, la compression KV, l'offload HBM, l'amélioration du throughput, <strong>plusieurs de ces facteurs évoluent simultanément dès que l'efficacité technique s'améliore</strong>. C'est pourquoi, dans le scénario bear composite, la demande chute à 6,5EB et la situation bascule en excédent d'offre.

<strong>Troisièmement, le chiffre de 2,5x, bien qu'étiqueté comme scénario de base, doit donc en réalité être traité comme un scénario à biais haussier.</strong> Une analyse de sensibilité à une seule variable (one-way sensitivity), poussée jusqu'au bout sur un seul paramètre, ne peut pas démontrer la robustesse du 2,5x. Le vrai risque réside dans la covariance, c'est-à-dire dans le fait que les hypothèses s'effondrent ensemble.

---

## 6. Le point de vue de l'équilibre de marché : comment lire le 2,5x

Il ne faut pas lire littéralement `demande 26,7EB, offre 10,6EB` comme 16,1EB de commandes non satisfaites. En réalité, le marché s'équilibre dans cet ordre.

```text
Hausse de la charge de travail IA potentielle
→ goulot d'étranglement du HBM qualifié
→ hausse des prix, contrats long terme, acomptes
→ allocation par client et report des charges à faible ROI
→ essor des SLM, MoE, quantification, réutilisation KV, offload
→ capex additionnel et certification de second-source
→ convergence entre volume expédié réalisé et demande apurée
```

\[Inférence\] Autrement dit, le 2,5x se lit plus justement non pas comme une prévision précise d'un déficit de volume qui se matérialisera, mais comme un scénario exprimant <strong>l'intensité du pouvoir de fixation des prix et de la pression d'allocation</strong>. Un déficit important ne signifie pas que « 16EB ne seront jamais comblés », mais que « cet écart subit une forte pression d'apurement via les prix, les contrats et la substitution technologique ».

Sous cet angle, les points d'observation que l'analyse de l'offre et de la demande doit réellement surveiller ne sont pas le chiffre en EB lui-même, mais les éléments suivants. \[Points de surveillance\]

1. Le plancher de prix des contrats pluriannuels se maintient-il
2. La prime d'ASP du HBM4/4E reste-t-elle suffisamment longtemps
3. La hausse du mix HBM rend-elle aussi la DRAM standard plus tendue en offre
4. L'amélioration du rendement et de l'advanced packaging permet-elle à la marge du revenu incrémental de revenir au fournisseur
5. Combien de profit et de cash-flow peuvent s'accumuler avant que la nouvelle offre de 2028 ne normalise les prix

---

## 7. Perspectives par horizon temporel : Base / Bull / Bear

En superposant les trois angles et l'analyse de sensibilité sur l'axe du temps, voici la synthèse.

| Période | Base | Bull | Bear |
|---|---|---|---|
| 2026-2027 | La montée en cadence du HBM4 et la demande IA dépassent la nouvelle offre greenfield. Tension persistante | Retard de certification chez Samsung, goulot d'étranglement du packaging persistant, demande de tokens et d'ASIC supérieure aux attentes | L'offre massive de HBM4 de Samsung et la diversification du mix client arrivent plus vite que prévu |
| 2028 | Les effets de SK Yongin phase 1, Micron ID1, Tongluo et packaging démarrent. L'ampleur du déficit s'atténue | L'effet de l'offre est limité par des retards initiaux de rendement et de certification | La nouvelle capacité se stabilise rapidement, amélioration simultanée de l'efficacité KV et du routing |
| 2029-2030 | Même si un déficit subsiste, l'atténuation est plus probable que l'expansion. Le pouvoir de fixation des prix dure plus longtemps que lors des cycles passés | L'empreinte des modèles et la concurrence des agents dépassent les gains d'efficacité, prime de rareté et contrats long terme se maintiennent | Montée en cadence simultanée de Micron ID2, Samsung et SK, chevauchement de l'efficacité et de l'offload, normalisation de la prime HBM |

### Verdict final par horizon temporel

- `Tension jusqu'en 2027` : <strong>probabilité élevée</strong>
- `Amélioration de l'offre à partir de 2028` : <strong>probabilité moyenne-haute</strong>
- `Atténuation du déficit en 2029-30` : <strong>probabilité moyenne</strong>
- `Élargissement du déficit de 2,5x encore en 2030` : <strong>probabilité faible / scénario haussier</strong>

---

## 8. Ce qu'il faut surveiller : déclencheurs de réévaluation

Fixer à l'avance les signaux qui indiquent un renforcement ou un affaiblissement du récit d'offre et de demande évite de se laisser ballotter par l'actualité.

<strong>Signaux d'un renforcement du biais haussier sur l'offre et la demande</strong>

1. Les fournisseurs confirment officiellement un statut sold-out, des contrats long terme ou des planchers de prix au-delà de 2028
2. La prime d'ASP et la marge se maintiennent à mesure que le rendement et la capacité de packaging du HBM4/4E s'améliorent
3. Malgré les extensions de Samsung et Micron, les indications de tension du secteur s'étendent au-delà de 2028
4. Les tokens réels, le contexte résident et la concurrence des charges de travail agentiques se rapprochent de la trajectoire x24

<strong>Signaux d'un affaiblissement du biais haussier sur l'offre et la demande</strong>

1. Une réduction combinée d'au moins 6x de la mémoire KV et des poids se généralise en environnement de production
2. La majorité de l'inférence incrémentale bascule vers des architectures memory-light : SLM, ASIC, offload
3. Le HBM4E de Samsung et les nouvelles capacités de Micron obtiennent une certification en volume plus vite que prévu
4. Les fournisseurs retirent leur guidance de « tension au-delà de 2027 » et le plancher des contrats clients s'affaiblit
5. La prime d'ASP du HBM, les prix contractuels et la marge DRAM se dégradent structurellement à mesure que l'offre augmente

---

## Conclusion : la direction est robuste, l'ampleur doit rester modeste

La conclusion en une phrase de cette recherche approfondie est la suivante. <strong>`Le HBM sera tendu jusqu'en 2027, avec une amélioration de l'offre à partir de 2028` est soutenu par les données et les calendriers officiels, mais `un déficit de 2,5x en 2030` est un scénario haussier qui exige que plusieurs hypothèses de demande se vérifient toutes en même temps.</strong>

Le chiffre de 26,7EB se reproduit avec précision, mais cette précision n'équivaut pas à une certitude. Il ne s'obtient que si tokens x24, modèle x5, contexte x4 et rétention KV à 70 % se vérifient <strong>simultanément</strong>, et ces hypothèses s'effondrent ensemble dès que l'efficacité technique progresse. À l'inverse, l'offre se convertit en output qualifié bien plus lentement que ne le laissent penser les annonces de fabs. Le point où ces deux forces se rencontrent constitue le point d'inflexion de 2028.

Le cadre utile pour analyser l'offre et la demande n'est pas de croire un chiffre unique, mais de <strong>séparer la confiance dans la direction de l'incertitude sur l'ampleur</strong>. La direction est robuste. L'ampleur doit rester modeste.

---

_Cet article synthétise des sources primaires publiques (Goldman Sachs, SK Hynix, Samsung Electronics, Micron, SEMI, Google Research, rapports techniques DeepSeek) et un modèle secondaire (Memory Analyst) pour produire une analyse de structure d'offre et de demande reproduite et croisée de façon indépendante. Les titres mentionnés sont des exemples destinés à illustrer la structure du secteur et ne constituent pas un conseil d'investissement. Des chiffres comme 26,7EB, 10,6EB ou 2,5x sont pour la plupart des hypothèses ou des scénarios de modèle, et non des prévisions officielles d'entreprise. Ce domaine évoluant rapidement, il est recommandé de vérifier ces chiffres auprès des sources primaires les plus récentes._

---

### Articles associés

- [HBM, HBF, HBC : comment distinguer précisément les trois technologies de mémoire IA](/fr/post/hbm-hbf-hbc-ai-memory-comparison-2026-06-22/)
- [Valeur du token IA aujourd'hui et demain : analyse de la valeur ajoutée des fournisseurs de mémoire](/fr/post/ai-token-value-memory-value-added-2026-07-09/)
- [Résultats de la Big Tech fin juillet et analyse des scénarios de thèse mémoire](/fr/post/big-tech-july-earnings-call-memory-thesis-scenarios-2026-07-07/)
- [Le consensus semi-conducteurs 2027 : qui paie la facture](/fr/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/)
- [Valorisation des profits 2028E de Samsung Electronics et SK Hynix : chiffres qui semblent bon marché et vérification du cycle](/fr/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/)
