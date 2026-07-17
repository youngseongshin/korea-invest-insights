---
title: "Les semi-conducteurs sont-ils cycliques et quelle est la juste valeur ? Valoriser Samsung, SK Hynix et Micron avec le FCFE et les bénéfices normalisés"
slug: "memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17"
date: 2026-07-17T20:00:00+09:00
description: "Samsung à 3,9x et SK Hynix à 4,3x sur le consensus 2028 signifie que le marché doute de la durée de ces bénéfices, non de leur existence. Cette analyse traite successivement du caractère cyclique des semis, du multiple qui convient à quel BPA, de savoir si le débat actuel ébranle le BPA 2028 ou seulement le multiple, pourquoi 2029 n'est pas si lointain, et où va réellement la trésorerie de 2026-2028, puis calcule des justes valeurs pondérées par les probabilités avec le FCFE et une valeur terminale normalisée."
categories: ["Exclusive Analysis", "Valuation", "Tech-Analysis"]
tags: ["Samsung Electronics", "SK Hynix", "Micron", "Mémoire", "HBM", "Valorisation", "FCFE", "Cyclique", "Bénéfices normalisés", "Juste valeur"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexte
> Cet article fait suite à [Le vrai débat des semi-conducteurs : quatre horloges physiques et une horloge boursière](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/), qui concluait que « l'industrie est bull mais l'action est valuation bear », et calcule cette fois de façon quantitative <strong>combien vaut donc le titre</strong>. Si [Samsung et SK Hynix sur bénéfices 2028E](/fr/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/) traitait des « chiffres qui semblent bon marché », cet article calcule la juste valeur à l'aide du FCFE et d'une terminal value normalisée. À lire avec [Le pire scénario est déjà dans le prix](/fr/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/) et [SK Hynix abaisse ses bénéfices du T2](/fr/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/). Les hubs associés sont le [Hub AI HBM](/fr/page/korea-semiconductor-hbm-kospi-hub/) et le [Hub Exclusive Analysis](/fr/page/exclusive-analysis-hub/).

## TL;DR

* En appliquant les cours de clôture KRX du 17 juillet (Samsung Electronics 255 000 KRW, SK Hynix 1 842 000 KRW) à l'EPS consensus 2028 du 16 juillet, le PER ressort à <strong>3,9x et 4,3x</strong> respectivement. Le marché ne pense pas que le bénéfice de 2028 va disparaître : il intègre dans le prix <strong>la probabilité que ce bénéfice ne dure pas longtemps</strong>.
* Les semi-conducteurs ne forment pas une industrie unique. La mémoire reste cyclique, et le HBM n'est pas un produit qui a supprimé le cycle, mais un produit qui <strong>allonge sa durée et réduit l'élasticité de l'offre</strong>.
* En surface, le débat actuel ébranle d'abord le multiple. Mais comme la baisse du multiple reflète économiquement, par anticipation, la normalisation de l'EPS après 2028, on ne peut pas séparer complètement la question du multiple de celle de l'EPS.
* La question « faut-il se baser sur 2028 ou sur 2029 » part d'une prémisse fausse. Le cours de l'action est <strong>la valeur actuelle du flux de trésorerie actionnarial perpétuel à partir de 2026</strong>. Appliquer un PER bas à l'EPS 2028 et appliquer un PER normal à l'EPS normalisé 2029 donnent la même réponse si les hypothèses sont cohérentes.
* La juste valeur pondérée par les probabilités, calculée avec le FCFE et une terminal value normalisée, ressort à <strong>385 000 KRW (+51%) pour Samsung Electronics, 1 950 000 KRW (+6%) pour SK Hynix et 1 140 USD (+34%) pour Micron</strong>. L'attrait ajusté du risque se classe dans l'ordre Samsung Electronics, Micron, SK Hynix. \[Inférence : estimation propre\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Thèse principale</div>
  <div class="thesis-callout__body">
    La prémisse même consistant à fixer le cours de l'action sur l'EPS 2028 ou sur l'EPS 2029 est inexacte. Il faut ajouter au FCFE 2026-2028 une terminal value normalisée pour 2029, et avec cette méthode, la marge de sécurité des trois titres se classe dans l'ordre Samsung Electronics, Micron, SK Hynix.
  </div>
</div>

---

## 1. Les semi-conducteurs sont-ils cycliques ?

Il n'y a pas de réponse unique. L'intensité du cycle diffère selon le segment.

| Segment | Nature du cycle | Raison |
|---|---|---|
| DRAM et NAND génériques | Très forte | Homogénéité du produit, stocks, variations de capacité et d'ASP |
| HBM | Moyenne à forte | La qualification, l'empilement et les LTA sont des barrières à l'entrée, mais les marges élevées déclenchent expansion de capacité et multiplication des fournisseurs |
| Fonderie et équipements | Moyenne à forte | CAPEX client et cycles de transition de procédé |
| Fabless et plateformes | Forte dispersion selon le produit | Un fossé concurrentiel existe, mais l'exposition aux changements de génération et au CAPEX client demeure |

La formulation la plus exacte est <strong>« une industrie qui croît structurellement, mais dont les prix et les profits sont cycliques »</strong>.

L'exposition diffère selon le titre. SK Hynix est le plus purement exposé à la mémoire et au HBM. Samsung Electronics a une sensibilité de profit élevée aux phases fastes de la mémoire, mais le mobile, l'affichage, la fonderie et la trésorerie amortissent en partie la baisse.

### Ce que les entreprises disent elles-mêmes

Ce jugement ne repose pas sur l'interprétation d'un observateur, mais sur <strong>les documents officiels des entreprises</strong>. \[Fait : dépôt SEC\]

SK Hynix qualifie l'industrie de la mémoire de <strong>highly cyclical</strong> dans son formulaire F-1 américain. Micron précise dans son 10-Q que le HBM nécessite davantage de wafers et de capacité de salle blanche que le DRAM générique pour produire le même nombre de bits, mais que <strong>si la demande en HBM s'affaiblit et que cette capacité revient vers le DRAM générique, l'offre de DRAM peut augmenter brutalement</strong>.

En combinant ces deux déclarations, la conclusion s'impose. Le HBM ne fait que ralentir la réaction de l'offre, il ne supprime pas le cycle. \[Inférence : synthèse des deux dépôts\]

---

## 2. Quel est le multiple approprié ?

Pour discuter du PER approprié, il faut d'abord déterminer <strong>à quel EPS on l'applique</strong>. Un même 8x est cher s'il s'applique au bénéfice de pic, et raisonnable s'il s'applique au bénéfice normalisé.

| Bénéfice appliqué | Samsung Electronics | SK Hynix | Interprétation |
|---|---:|---:|---|
| EPS de pic 2027-2028 | 5,5-7,5x | 5-7x | Décote la normalisation ultérieure du bénéfice |
| EPS normalisé | 8-10x | 7-9x | Appliqué au bénéfice moyen sur 3-5 ans |
| Plateau structurel confirmé | 9-11x | 8-10x | Autorisé seulement si le bénéfice se maintient après 2029 |

Pour que Samsung Electronics dépasse 9x, il faut confirmer conjointement un redressement de la part de marché HBM et une réduction des pertes de la fonderie. Le 8-10x de SK Hynix exige la part de marché du HBM4E, une renégociation des prix des LTA, le retour aux actionnaires et la défense de la marge après la hausse de l'offre.

<strong>Appliquer directement 9-12x au consensus 2028 revient donc à combiner bénéfice de pic et multiple structurel, ce qui constitue un scénario fortement haussier</strong>. Pour une entreprise cyclique, le PER est au plus bas au pic du cycle, et au plus haut, ou incalculable, en creux de cycle. La valeur de continuité doit être calculée sur le bénéfice normalisé, ni au pic ni au creux. \[Fait : méthodologie de valorisation cyclique de McKinsey\]

---

## 3. Le débat actuel ébranle-t-il l'EPS, ou seulement le multiple ?

La réponse diffère selon le débat considéré.

| Débat | Impact immédiat | Condition pour que l'EPS lui-même soit atteint |
|---|---|---|
| Débouclage de levier sur un titre unique | Multiple, flux acheteurs-vendeurs | Aucune, facteur technique |
| Craintes sur les taux, la dette IA, le ROI | Multiple en priorité | Baisse du CAPEX chez au moins deux big techs |
| Résistance des acheteurs sur les prix | Multiple plus risque EPS | Baisse simultanée des prix contractuels et des commandes |
| Expansion de capacité des trois fabricants de mémoire | EPS 2028 et multiple | Hausse réelle de la production qualifiée et de l'offre en bits |
| CXMT, YMTC | Multiple de long terme en priorité | Qualification mondiale, expéditions massives, pression sur les prix |
| Goulot d'étranglement des LTA HBM et du packaging | Défense de l'EPS et du multiple | Maintien du plancher de prix et des volumes contractuels |

### Les chiffres des analystes n'ont pas encore bougé

Selon WiseReport local, l'EPS 2028 de Samsung Electronics reste identique à 65 907 KRW aux deux dates du 13 et du 16 juillet. Celui de SK Hynix a été abaissé de 433 625 KRW à 427 332 KRW, soit une baisse de <strong>1,5%</strong>. \[Fait : consensus WiseReport\]

Autrement dit, les chiffres des analystes n'ont presque pas bougé, et <strong>c'est le cours de l'action qui a bougé en premier</strong>.

### Mais ce n'est pas non plus seulement le multiple qui a baissé

En calculant à rebours avec un PER normalisé de 8x, on obtient l'EPS que le marché est prêt à accepter.

| Titre | EPS implicite à 8x | Consensus 2028 | Écart |
|---|---:|---:|---:|
| Samsung Electronics | 31 875 KRW | 65 907 KRW | -52% |
| SK Hynix | 230 250 KRW | 427 332 KRW | -46% |

Le marché mélange les deux cas suivants dans son prix.

1. L'EPS 2028 reste proche du consensus, mais chute rapidement à partir de 2029.
2. L'expansion de l'offre et la résistance des prix font baisser l'EPS 2028 lui-même.

Les données confirmées à ce jour se rapprochent <strong>davantage du cas 1</strong>. L'annulation de CAPEX, la baisse des prix contractuels, la hausse des stocks et la renégociation des LTA n'ont pas encore été confirmées conjointement. L'expansion de capacité et la résistance des acheteurs restent cependant des variables réelles susceptibles de faire basculer vers le cas 2. \[Inférence : interprétation des données\]

L'ajustement actuel n'est pas encore un marché baissier de résultats, mais <strong>une réévaluation de la durée du bénéfice</strong>. Cependant, l'inquiétude que le marché exprime à travers le multiple porte, dans le fond, sur l'EPS après 2028, et si les prix contractuels, les stocks et le CAPEX se détériorent, la situation basculera vers un marché baissier de l'EPS 2028.

---

## 4. Faut-il se baser sur 2028 ou sur 2029 ?

La prémisse même de cette question est inexacte. Le cours de l'action n'est pas déterminé par l'un ou l'autre. C'est <strong>la valeur actuelle du flux de trésorerie actionnarial perpétuel à partir de 2026</strong>.

```text
Valeur actuelle
= valeur actuelle des FCFE 2026-2028
+ valeur actuelle de la terminal value de fin 2028

Terminal value de fin 2028 ≈ EPS normalisé 2029 × PER normalisé
```

Utiliser l'EPS 2028 ne revient pas à ignorer la période après 2029. C'est une façon de <strong>compresser le risque de baisse après 2029 dans le PER bas appliqué à l'EPS 2028</strong>. En utilisant directement l'EPS normalisé 2029, on peut appliquer un PER plus normal. Si les hypothèses sont cohérentes, les deux méthodes doivent donner un résultat similaire.

Les deux camps disent souvent la même chose avec des mots différents, et se disputent pourtant fréquemment pour savoir lequel a raison.

---

## 5. 2029 est-il un avenir trop lointain ?

Trois ans, ce n'est pas loin en matière de valorisation boursière. Avec un taux de rendement exigé de 11%, 1 KRW de 2029 vaut aujourd'hui environ 0,73 KRW.

```text
1 / (1,11)^3 = 0,731
```

Même si un investisseur revend l'action dans un an, <strong>l'acheteur de ce moment-là regardera les flux de trésorerie après 2029</strong>. Comme le prix de revente final est lui-même déterminé par les flux de trésorerie futurs, un horizon d'investissement court ne permet pas d'échapper au bénéfice de long terme. Le modèle FCFE de Damodaran calcule lui aussi la valeur de l'action comme la somme du FCFE sur la période de prévision explicite et de la terminal value qui suit. \[Fait : modèle FCFE de NYU Stern\]

---

## 6. Le cash de 2026-2028 n'est-il pas pris en compte ?

Il l'est. Mais <strong>l'EPS et le cash qui revient réellement aux actionnaires sont deux choses différentes</strong>.

En agrégeant le consensus WiseReport du 16 juillet, on obtient ceci. \[Fait : agrégation du consensus\]

| Titre | EPS 2026E | EPS 2027E | EPS 2028E | EPS cumulé sur 3 ans | Par rapport au cours actuel |
|---|---:|---:|---:|---:|---:|
| Samsung Electronics | 46 664 KRW | 65 802 KRW | 65 907 KRW | 178 373 KRW | 70% |
| SK Hynix | 314 787 KRW | 438 114 KRW | 427 332 KRW | 1 180 233 KRW | 64% |

Si le consensus se réalise, le bénéfice cumulé sur 3 ans représente 64 à 70% du cours actuel, une ampleur qu'on ne peut pas ignorer.

Le problème, c'est que le bénéfice comptable n'est pas directement du cash pour l'actionnaire.

```text
FCFE = résultat net - CAPEX net - hausse du besoin en fonds de roulement + emprunts nets
```

Les entreprises mémoire augmentent fortement leurs investissements en fabs, en EUV et en packaging pendant les phases fastes. Si 60 sur 100 de résultat net est utilisé pour l'expansion de capacité, le cash immédiatement disponible n'est que de 40. Les 60 restants ne disparaissent pas non plus, mais <strong>les nouvelles installations ne créent de la valeur que si elles rapportent plus que le coût du capital</strong>.

Le bénéfice 2026-2028 se reflète dans le cours via les dividendes et rachats d'actions, la hausse de la trésorerie nette, la baisse de la dette, la hausse de la valeur comptable et une expansion de capacité à haut rendement. À l'inverse, si une surcapacité survient juste après l'expansion de capacité, le cash se transforme en installations et le ROE futur baisse lui aussi. C'est pourquoi le marché ne valorise pas le résultat net des phases fastes à 1 KRW pour 1 KRW.

### Les deux trajectoires que le prix actuel intègre

Le prix actuel correspond à 3,9x le consensus 2028 pour Samsung Electronics et 4,3x pour SK Hynix. Le marché mélange les éléments suivants dans son prix.

1. Une part importante du bénéfice 2026-2028 est réinvestie dans l'expansion de capacité.
2. L'ASP et les marges se normalisent à partir de 2029.

La variable de jugement n'est donc pas tant « l'EPS 2029 va-t-il baisser » que <strong>l'ampleur de la baisse</strong> et <strong>la proportion du bénéfice 2026-2028 qui reste effectivement en FCFE ou en trésorerie nette</strong>.

| Trajectoire 2029 | Méthode d'évaluation |
|---|---|
| EPS -10% à -20%, puis stabilisation | FCFE explicite + PER normalisé 8-10x |
| EPS -30% à -50%, puis reprise | FCFE explicite + EPS normalisé 7-9x |
| EPS -50% ou plus, surcapacité persistante | PBR normalisé, trésorerie nette et valeur de réduction de capacité plutôt que PER |

McKinsey estime elle aussi que pour une entreprise cyclique, il faut pondérer par les probabilités un scénario de cycle normal et un scénario de changement structurel, et calculer la terminal value à partir d'un flux de trésorerie normalisé, ni au pic ni au creux. \[Fait : méthodologie McKinsey\]

---

## 7. Une fois le calcul affiné, quelle est la juste valeur ?

Le cadre ci-dessus a été appliqué à des chiffres réels. Voici la juste valeur pondérée par les probabilités au 17 juillet 2026. \[Inférence : estimation propre, hypothèses précisées ci-dessous\]

### Méthode de calcul

```text
Juste valeur = FCF restant de 2026 + FCF 2027 + FCF 2028 + terminal value de fin 2028
Terminal value = EPS normalisé 2029 × PER approprié
```

- <strong>Taux d'actualisation</strong> : Samsung Electronics 10,5%, SK Hynix 11,5%, Micron 10,5%
- <strong>Probabilités</strong> : demande excédentaire 30%, vide de commandes et recentrage 40%, normalisation de l'offre 20%, court-circuit de crédit 10%
- <strong>PER terminal</strong> : Samsung Electronics 7,5-8,5x, SK Hynix 6-9x, Micron 7-9,5x
- <strong>Traitement du cycle baissier</strong> : 45-90% de la baisse du bénéfice est reflétée dans le FCF, en appliquant à la fois un CAPEX fixe et une possibilité de réduction

### Résultat

| Titre | Cours actuel | Juste valeur pondérée par les probabilités | Potentiel de hausse | Fourchette de sensibilité |
|---|---:|---:|---:|---:|
| Samsung Electronics | 255 000 KRW | <strong>385 000 KRW</strong> | +51% | 316 000-461 000 KRW |
| SK Hynix | 1 842 000 KRW | <strong>1 950 000 KRW</strong> | +6% | 1 480 000-2 480 000 KRW |
| Micron | 853,20 USD | <strong>1 140 USD</strong> | +34% | 905-1 410 USD |

La fourchette de sensibilité résulte d'un déplacement de 10 points de pourcentage des probabilités de demande excédentaire et de normalisation de l'offre, combiné à une variation du taux d'actualisation de ±1,5 point de pourcentage et du PER terminal de ±1x.

### Valeur actuelle par scénario

| Scénario | Probabilité | Samsung Electronics | SK Hynix | Micron |
|---|---:|---:|---:|---:|
| Demande excédentaire persistante | 30% | 548 000 KRW | 3 415 000 KRW | 1 735 USD |
| Vide de commandes, recentrage | 40% | 347 000 KRW | 1 581 000 KRW | 1 086 USD |
| Normalisation de l'offre et de l'efficacité | 20% | 283 000 KRW | 1 064 000 KRW | 674 USD |
| Court-circuit de crédit systémique | 10% | 241 000 KRW | 732 000 KRW | 505 USD |

Ce tableau révèle la différence de nature entre les trois titres. <strong>Samsung Electronics reste au-dessus du cours actuel même dans le scénario de normalisation de l'offre (283 000 KRW).</strong> À l'inverse, <strong>SK Hynix passe déjà sous le cours actuel dès le deuxième scénario (1 581 000 KRW).</strong> Cela signifie que le rendement attendu actuel de SK Hynix dépend le plus fortement de la persistance de la demande excédentaire.

---

## 8. La différence que crée le FCF

Même si le bénéfice ralentit en 2029, le cash généré pendant les trois années précédentes ne disparaît pas. L'ampleur de cet amortisseur diffère selon le titre.

| Titre | FCF 2026F | FCF 2027F | FCF 2028F | Part du FCF sur 3 ans dans la valeur pondérée par les probabilités |
|---|---:|---:|---:|---:|
| Samsung Electronics | 158,2 Mds KRW | 385,0 Mds KRW | 412,7 Mds KRW | <strong>26%</strong> |
| SK Hynix | 74,7 Mds KRW | 177,4 Mds KRW | 172,0 Mds KRW | 17% |
| Micron | 50,6 Mds USD | 124,3 Mds USD | 145,9 Mds USD | 18% |

\[Fait : rapport Samsung Securities (Samsung Electronics), synthèse de rapport Korea Investment & Securities (SK Hynix), estimations FactSet (Micron)\]

<strong>Pour Samsung Electronics, 26% de la valeur pondérée par les probabilités provient du FCF 2026-2028.</strong> Autrement dit, même si les scénarios se dégradent après 2029, c'est le titre où la part de cash déjà sécurisé est la plus grande. SK Hynix est la plus basse à 17%, ce qui signifie que l'essentiel de sa valeur dépend de la terminal value après 2029.

---

## 9. Classement final

<strong>1er, Samsung Electronics</strong> : la plus grande marge de sécurité. Le cours actuel est proche de la valeur du scénario hard-bear. La trésorerie nette et la diversification des activités amortissent la baisse de la terminal value, et la part de 26% du FCF sur 3 ans constitue un amortisseur supplémentaire.

<strong>2e, Micron</strong> : attractif sur la base de la juste valeur centrale, mais sensible à la nouvelle offre de 2028. Il faut aussi noter que la juste valeur Morningstar, une ancre bear externe, est de 850 USD, un niveau proche du cours actuel. \[Fait : Morningstar\]

<strong>3e, SK Hynix</strong> : le momentum d'activité est le plus fort, mais la marge de sécurité sur le prix est la plus mince. Un nouveau jugement nécessite de confirmer le prix et le rendement du HBM4E ainsi que les LTA 2028.

Au prix actuel, <strong>l'attrait ajusté du risque se classe donc dans l'ordre Samsung Electronics, Micron, SK Hynix</strong>. Le fait que l'ordre de qualité des activités (SK Hynix étant le plus fort du fait de sa pure exposition au HBM) soit inversé par rapport à l'ordre d'attrait du prix constitue la conclusion centrale de ce calcul. \[Inférence : jugement synthétique\]

---

## 10. Synthèse de la méthode d'évaluation par titre

- <strong>Samsung Electronics</strong> : additionner séparément le FCFE 2026-2028, puis actualiser en appliquant 8-10x à l'EPS normalisé 2029. La trésorerie nette et la diversification des activités amortissent la baisse de la terminal value.
- <strong>SK Hynix</strong> : additionner le FCFE 2026-2028 en tenant compte de l'expansion de capacité et de la dilution, puis appliquer 7-9x à l'EPS normalisé 2029. N'autoriser la partie haute que si le plateau du HBM est confirmé.

Évaluer le consensus 2028 à seulement 4x n'est pas satisfaisant, et appliquer mécaniquement 9-12x ne l'est pas davantage. La bonne méthode consiste à <strong>additionner au FCFE 2026-2028 la terminal value normalisée de 2029, puis à sommer par scénario</strong>.

---

## Conclusion

Voici, en une ligne par question, les réponses résumées.

Les semi-conducteurs sont-ils cycliques ? La mémoire l'est. Le HBM n'a pas supprimé le cycle, il l'a seulement allongé, et c'est ce que disent elles-mêmes le F-1 de SK Hynix et le 10-Q de Micron.

Quel est le multiple approprié ? Il faut d'abord déterminer à quel EPS on l'applique. 5-7x au pic, 7-10x en normalisé.

Qu'ébranle le débat actuel ? En surface, le multiple, mais ce que ce multiple exprime, c'est l'EPS après 2028. Les chiffres des analystes n'ont pour l'instant bougé que d'environ 1,5%, et le cours de l'action est parti en premier.

2028 ou 2029 ? Ni l'un ni l'autre. On ajoute au FCFE 2026-2028 la terminal value normalisée de 2029.

2029 est-il un avenir lointain ? 1 KRW de dans trois ans vaut aujourd'hui 0,73 KRW. Même en revendant dans un an, l'acheteur de ce moment-là regardera 2029.

Le cash de 2026-2028 est-il pris en compte ? Il l'est, mais pas comme l'EPS brut. Il faut soustraire ce qui part en expansion de capacité, et ces installations ne créent de la valeur que si elles rapportent plus que le coût du capital.

Alors, combien ? 385 000 KRW pour Samsung Electronics, 1 950 000 KRW pour SK Hynix, 1 140 USD pour Micron. Le titre au momentum d'activité le plus fort et le titre à la marge de sécurité sur le prix la plus large ne sont pas les mêmes.

---

_Cette publication est une analyse calculée en propre à partir des cours KRX de KIS (2026-07-17), du consensus WiseReport (2026-07-16), des dépôts SEC (F-1 de SK Hynix, 10-Q de Micron), des estimations de FCF des courtiers, et des méthodologies de valorisation publiques de McKinsey et de NYU Stern. Les justes valeurs pondérées par les probabilités, les probabilités de scénarios, les PER terminaux et les taux d'actualisation sont tous des estimations fondées sur des hypothèses arrêtées au moment de la rédaction, et non une guidance d'entreprise ni un consensus. Les révisions des estimations d'analystes postérieures à la chute du 17 juillet ne sont pas encore reflétées. L'EPS cumulé est une somme de bénéfices comptables, non une estimation de FCFE. Les titres mentionnés sont des exemples destinés à illustrer la méthodologie de valorisation et ne constituent pas une recommandation d'achat ou de vente d'un titre particulier. La décision d'investissement et sa responsabilité incombent à l'investisseur lui-même._

---

### Articles associés

- [Le vrai débat des semi-conducteurs : quatre horloges physiques et une horloge boursière](/fr/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [Samsung et SK Hynix sur bénéfices 2028E : chiffres bon marché et test de cycle](/fr/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/)
- [Samsung Electronics et SK Hynix sont-ils vraiment survendus face au consensus 2027 ?](/fr/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/)
- [SK Hynix abaisse ses bénéfices du T2, pourquoi l'objectif de cours a-t-il été maintenu ?](/fr/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/)
- [Pourquoi le manque à gagner d'IBM est une preuve de la vigueur de la mémoire](/fr/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/)
