---
title: "Dans une bulle de bénéfices, les estimations sont rabotées en dernier : la concentration sur l'infrastructure IA et la valeur d'une analyse approfondie"
slug: "ai-infra-earnings-bubble-deep-dive-research-thesis-os-2026-05-31"
date: 2026-05-31T14:00:00+09:00
description: "BCA Research estime que la bulle de l'IA n'est pas une bulle de valorisation mais une bulle de bénéfices. Dans une bulle de bénéfices, le cours chute bien avant que les estimations de bénéfices ne soient rabotées. C'est pourquoi, alors que les capitaux affluent vers l'infrastructure IA, il importe davantage de lire directement la structure du système et les indicateurs avancés par une analyse approfondie que d'attendre le consensus. Cette note expose cette méthode avec sobriété, à travers Thesis OS et le travail réel de notre blog."
categories: ["Korea Market", "Research Process"]
tags:
  - "AI 인프라"
  - "이익 버블"
  - "딥다이브 리서치"
  - "Thesis OS"
  - "반도체 사이클"
  - "컨센서스"
  - "선행지표"
  - "AI PCB"
  - "Research OS"
draft: false
---

> Ceci est une note méthodologique. Pour les textes qui ont nourri l'analyse, il est utile de les lire en parallèle : [la thèse sur les substrats/PCB d'IA (le goulet d'étranglement commun de la BOM système)](/fr/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/), [la demande de tokens de Goldman face au pic d'ASP mémoire de J.P. Morgan](/fr/post/goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31/), et [la note publique sur Thesis OS](/fr/post/thesis-os-open-source-research-operating-system-2026-05-30/) qui explique la structure faisant tourner l'ensemble de ce travail.

## TL;DR

* Dans un rapport récent, BCA Research estime que <strong>la bulle de l'IA n'est pas une bulle de valorisation mais une bulle de bénéfices (earnings)</strong>. Ce n'est pas le PER qui gonfle, mais les bénéfices eux-mêmes. Et comme toute bulle, elle finit par se dégonfler, BCA ajoutant toutefois que ses propres indicateurs de demande d'IA ne montrent encore aucun signal imminent.
* La caractéristique essentielle d'une bulle de bénéfices est le <strong>décalage temporel</strong>. Pour reprendre les mots de BCA, dans presque tous les cas « les actions ont commencé à chuter bien avant que les estimations de bénéfices ne soient rabotées ». Les estimations de consensus sont un signal retardé.
* C'est pourquoi, précisément dans une phase où l'argent afflue ainsi vers l'infrastructure IA, ce qui compte davantage, c'est une <strong>analyse approfondie qui lit directement la structure du système et les indicateurs avancés de la demande, au lieu d'attendre le BPA de consensus</strong>. Une fois les estimations rabotées, il est déjà trop tard.
* Cette note expose, sans exagération, ce que cette analyse approfondie observe réellement, et comment nous l'avons menée au moyen d'une structure appelée <strong>Thesis OS</strong>.

---

## 1. Ce que signifie qualifier la bulle de l'IA de « bulle de bénéfices »

Quand on dit « bulle », on imagine d'ordinaire des PER qui s'envolent — une bulle de valorisation, où le prix monte bien plus vite que les bénéfices. BCA Research voit l'IA comme un type un peu différent. C'est une <strong>bulle de bénéfices, où ce sont les bénéfices eux-mêmes qui gonflent, et non le prix</strong>.

Ce n'est pas un schéma nouveau. Les constructeurs de logements et les banques ont fait exactement cela juste avant la crise financière. Leurs PER paraissaient faibles, mais seulement parce que des bénéfices insoutenables gonflaient le dénominateur (B) et faisaient paraître le multiple bon marché. Les secteurs qui oscillent fortement entre expansion et récession — ressources naturelles, compagnies aériennes, transport maritime, et les semi-conducteurs d'aujourd'hui — sont vulnérables à ce type de bulle de bénéfices.

En ce moment, la courbe de chiffre d'affaires des semi-conducteurs ressemble à cette image.

![Les ventes mondiales de semi-conducteurs ont tracé une parabole — reconstruction d'après les agrégats annuels publics du WSTS](global-semiconductor-sales-parabolic.png)

<small>Source : reconstruction approximative d'après les agrégats annuels publics du WSTS, 2025-2026 étant des estimations. À titre illustratif, ce n'est pas un conseil en investissement. La forme des données sous-jacentes va dans le même sens que le graphique des « ventes paraboliques de semi-conducteurs » présenté dans le rapport de BCA Research (2026-05-28).</small>

Une courbe de chiffre d'affaires qui devient parabolique est à la fois une bonne nouvelle et un avertissement. Quand les bénéfices montent vite, le PER paraît faible. Mais si ces bénéfices sont un produit du cycle, le fait même que le multiple paraisse bon marché peut devenir un piège. Le vieil avertissement des secteurs cycliques s'applique ici : <strong>« le moment le plus dangereux, c'est quand les bénéfices sont à leur sommet »</strong>.

Ne nous y trompons pas. Ni BCA ni nous ne disons « cela se dégonfle maintenant ». BCA juge que ses indicateurs de demande d'IA — taux d'adoption, dépenses en tokens, téléchargements d'outils de codage par IA, prix des GPU et de la mémoire — restent pour l'essentiel à des niveaux rassurants. L'enjeu n'est pas le calendrier, mais <strong>la manière dont cette bulle se comporte</strong>.

---

## 2. Le vrai piège d'une bulle de bénéfices, c'est le « décalage »

Ce qui rend une bulle de bénéfices dangereuse, ce n'est pas qu'elle éclate, mais l'<strong>ordre dans lequel elle éclate</strong>.

Le point central que souligne BCA est le suivant : les analystes de Wall Street prévoient mal le moment où une bulle de bénéfices se dégonflera. Et dans presque tous les cas, <strong>« les actions ont commencé à chuter bien avant que les estimations de bénéfices ne soient rabotées »</strong> (BCA Research, 2026-05-28).

Voici ce que cette phrase signifie en pratique, mis en image.

![Dans une bulle de bénéfices, le cours chute avant que les estimations ne soient rabotées — schéma conceptuel](earnings-bubble-price-leads-estimate-cuts.png)

<small>Il s'agit d'un schéma conceptuel, pas de données réelles. Il simplifie la structure de décalage décrite par BCA, où le prix précède et les estimations suivent.</small>

La ligne rouge (le cours) se retourne à la baisse en premier. La ligne bleue pointillée (les estimations de bénéfices de consensus) n'est rabotée que bien plus tard. La bande grise intermédiaire est le décalage. Si vous suivez la règle « je vendrai quand les analystes abaisseront leur objectif de cours ou leurs estimations », vous agirez toujours en retard, exactement de ce décalage.

D'où la conclusion. <strong>Les estimations de consensus sont un signal retardé.</strong> L'action ne paraît pas la plus chère lorsque les bénéfices culminent, et au moment où les estimations sont rabotées, le cours a déjà chuté. Donc, si vous ne regardez que les estimations, vous manquez à la fois le sommet de la bulle et son point d'inflexion.

---

## 3. C'est pourquoi une analyse approfondie est nécessaire — que regarde-t-elle

Si les estimations suivent, que faut-il regarder pour précéder ? Une analyse approfondie observe non pas le BPA en gros titre, mais la <strong>structure et les indicateurs avancés</strong> qui produisent ce BPA. Concrètement, quatre choses.

<strong>① Elle lit la structure du système.</strong> Le récit linéaire — « après le GPU vient la mémoire, puis les substrats » — est facile à trader mais à moitié vrai seulement. La véritable infrastructure IA est un système à l'échelle du rack où GPU, CPU, DPU, NIC, ASIC de commutation, modules mémoire et cartes d'alimentation croissent ensemble. Comme nous l'avons exposé dans [la thèse sur les substrats/PCB d'IA](/fr/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/), les substrats et les PCB ne sont pas le terminus d'une rotation, mais le dénominateur commun de toute la nomenclature (BOM) du système. Connaître la structure révèle où se trouve le vrai goulet d'étranglement.

<strong>② Elle sépare les variables.</strong> Face à la même demande d'IA, Goldman suit l'usage des tokens (Q) et le coût par token (C), tandis que J.P. Morgan suit le rythme de hausse du prix de la mémoire (P). En [décomposant les deux prévisions en P, Q et C](/fr/post/goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31/), il devient clair que les deux visions, qui semblaient s'opposer, parlent en fait de variables différentes et peuvent tenir en même temps. C'est ce qu'occulte le fait de tout regrouper dans un seul chiffre de gros titre.

<strong>③ Elle suit directement les indicateurs avancés.</strong> Au lieu d'attendre que le BPA de consensus soit raboté, elle observe ce qui bouge plus tôt : prix et volumes des contrats long terme de HBM, prix contractuels de la DRAM serveur, dépenses en tokens, prix au comptant des GPU et de la mémoire, taux d'adoption. Ces éléments changent de direction avant les estimations.

<strong>④ Elle sépare le fait, l'inférence et la conjecture.</strong> « Fait confirmé officiellement », « inférence raisonnable » et « simple conjecture » ne vont pas dans la même case. Ce qui n'est pas vérifié — noms de clients, adoption ou non d'un composant, conditions contractuelles — est clairement signalé comme inférence ou conjecture. Sans cette séparation, on se laisse emporter par un récit séduisant et l'on achète des conjectures comme s'il s'agissait de faits.

Ces quatre choses n'attendent pas que les estimations soient rabotées. C'est pourquoi elles souffrent moins du décalage.

---

## 4. Thesis OS — la structure qui fait tourner cette analyse approfondie comme un système

Bien faire les quatre choses ci-dessus une ou deux fois n'est pas difficile. Le difficile, c'est de les faire <strong>à chaque fois, avec la même discipline</strong>. Aussi confions-nous ce travail à une structure plutôt qu'à l'humeur d'une personne un jour donné. Cette structure, c'est [Thesis OS](/fr/post/thesis-os-open-source-research-operating-system-2026-05-30/).

Thesis OS se divise en trois rôles.

| Rôle | Ce qu'il fait |
|---|---|
| <strong>Alpha (알파)</strong> | Collecte de preuves — données de marché, screeners, crawlers, pipelines de vérification des faits |
| <strong>Lattice (격자)</strong> | Jugement — tisser les preuves en une thèse, bâtir des prévisions, les éprouver par la logique contraire |
| <strong>Arki (아키)</strong> | Gouvernance — maintenir l'ensemble cohérent par des schémas, des flux de travail et des contrôles de santé |

L'essentiel n'est pas une automatisation tape-à-l'œil, mais la <strong>répétabilité de la discipline</strong>. Séparer la preuve (Alpha) du jugement (Lattice) réduit le risque qu'un beau récit devance la preuve. Avec la gouvernance (Arki) en place, on sépare le fait, l'inférence et la conjecture selon le même critère à chaque fois, et l'on continue de suivre les indicateurs avancés. Thesis OS est open source, de sorte que le lecteur intéressé peut examiner la structure elle-même directement.

---

## 5. Le travail de notre blog — avec sobriété

Nous l'écrivons comme un relevé, non comme une vantardise. La preuve la plus honnête, c'est quels textes cette méthode a réellement produits.

* <strong>Cartographie de la structure du système</strong> : [la thèse sur les substrats/PCB d'IA](/fr/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) — voir l'IA comme un système à l'échelle du rack et redéfinir les substrats comme le goulet d'étranglement commun.
* <strong>Séparation des variables</strong> : [Goldman vs. J.P. Morgan](/fr/post/goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31/) — décomposer deux prévisions apparemment opposées en P, Q et C.
* <strong>Lecture des résultats (read-through)</strong> : [Marvell T1 EX2027](/fr/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/), [Dell T1 EX2027](/fr/post/dell-q1-fy2027-earnings-korea-ai-server-margin-readthrough-2026-05-29/) — traduire les résultats américains en goulets d'étranglement de composants et matériaux coréens.
* <strong>Suivi de la structure de coûts</strong> : [contrats à terme sur tokens d'IA et coût par token](/fr/post/ai-token-futures-cost-per-token-korea-semiconductor-thesis-2026-05-30/) — l'axe se déplaçant d'une course à la performance vers une course aux coûts.

Le point commun de ces textes est qu'ils ne se précipitent pas vers une conclusion « acheter/vendre ». Ils cartographient plutôt la structure, séparent les variables, présentent les indicateurs avancés et traitent les valeurs non comme des recommandations mais comme des points d'observation. Le but est de donner au lecteur de quoi juger par lui-même. Nous ne prétendons pas pouvoir prédire le sommet du marché ni le moment où la bulle éclate. Comme le conclut BCA, même les analystes y parviennent mal. Ce que nous cherchons à faire est plus modeste : <strong>comprendre la structure avant que les estimations ne soient rabotées, et nous obliger à regarder les signaux avancés plutôt que les signaux retardés</strong>.

---

## 6. Conclusion

Dans une phase où autant de capitaux se sont concentrés sur l'infrastructure IA, l'attitude la plus dangereuse est d'attendre que le consensus tourne pour vous. Dans une bulle de bénéfices, ce signal arrive toujours tard. Le cours bouge avant que les estimations ne soient rabotées.

Aussi une analyse approfondie n'est-elle pas une prévision tape-à-l'œil, mais <strong>une préparation pour être moins en retard</strong>. Comprendre le système, séparer les variables, regarder directement les indicateurs avancés et distinguer le fait de la conjecture. Pour répéter ce travail non pas une fois mais à chaque fois avec la même discipline, nous utilisons une structure appelée [Thesis OS](/fr/post/thesis-os-open-source-research-operating-system-2026-05-30/). Si cela vous intéresse, nous vous encourageons à regarder non seulement les conclusions, mais aussi la structure et le processus qui les sous-tendent.

<small>Ce texte cite brièvement, en l'attribuant, l'argument central publié du rapport « Earnings Bubbles Are Still Bubbles » de BCA Research (Global Investment Strategy, 2026-05-28), et les graphiques sont de notre propre fabrication à partir de données et de concepts publics. Il ne s'agit pas d'une recommandation d'achat ou de vente d'un titre particulier ; les décisions d'investissement et leur responsabilité incombent à l'investisseur lui-même.</small>
