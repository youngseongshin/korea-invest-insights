---
title: "Comment ce blog est fabriqué : présentation de Thesis OS, notre système d'exploitation de recherche open source"
date: 2026-05-30T11:00:00+09:00
description: "Les articles de Korea Invest Insights ne sont pas rédigés un à un à partir de zéro : ils sont produits via une structure appelée Thesis Investment OS. Alpha rassemble les preuves, Lattice transforme ces preuves en jugement, et Arki maintient l'ensemble du système en bonne santé. Ensemble, ces trois rôles forment un système d'exploitation de recherche open source. Cet article explique cette structure en termes simples et vous invite à visiter le dépôt GitHub."
categories: ["Tools"]
tags:
  - "Thesis OS"
  - "open source"
  - "méthodologie de recherche"
  - "recherche d'investissement"
  - "Alpha"
  - "Lattice"
  - "Arki"
  - "Research OS"
  - "GitHub"
slug: thesis-os-open-source-research-operating-system-2026-05-30
draft: false
---

> 🔗 <strong>Aller au dépôt</strong> : <strong>[github.com/youngseongshin/thesis-investment-os](https://github.com/youngseongshin/thesis-investment-os)</strong> — le système open source qui fait tourner la recherche de ce blog

L'article d'aujourd'hui est un peu différent de d'habitude. Il ne parle pas d'une action, mais de <strong>la façon dont les articles de ce blog sont réellement fabriqués</strong>. Laissez-moi lever le rideau un instant.

![Architecture de Thesis Investment OS — un système d'exploitation de recherche où Alpha, Lattice et Arki s'imbriquent](thesis-os-architecture.png)

## Ce qu'il faut pour produire un seul article

Les articles de Korea Invest Insights ne sont pas improvisés par une personne fixant un écran blanc. Derrière eux tourne un petit système d'exploitation appelé <strong>Thesis Investment OS</strong>. Le nom paraît grandiose, mais l'idée est simple.

> Rendre le jugement d'investissement <strong>visible, vérifiable et honnête quant à son propre historique.</strong>

Ce n'est pas un robot de trading automatisé, ni un service qui vend des signaux, ni une « IA qui choisit des actions à votre place ». C'est un <strong>cadre</strong> qui rassemble des informations de marché éparses en une thèse, et qui vous permet de revenir plus tard vérifier si cette thèse s'est révélée juste ou fausse.

La structure se divise en trois rôles. Imaginez-les comme trois personnes d'une même équipe.

---

## 1. Alpha — celui qui rassemble les preuves

Alpha est le rôle qui <strong>collecte et vérifie les faits.</strong>

- <strong>Données quantitatives</strong> : prix, volume, flux, fondamentaux, documents réglementaires
- <strong>Données qualitatives</strong> : actualités, dépôts, transcriptions de résultats, signaux de la communauté
- Filtrer les candidats avec des screeners, puis ajouter du contexte pour faire ressortir les valeurs à surveiller

Ce qu'Alpha produit, ce sont des enregistrements de preuves, des instantanés de marché, des alertes intrajournalières, des candidats de screener et des dossiers de recherche. En bref, c'est celui qui <strong>empile honnêtement « ce qui s'est passé ».</strong> Il ne juge pas encore. Il ne fait que rassembler la matière première.

---

## 2. Lattice — celui qui bâtit le jugement à partir des preuves

Le nom Lattice vient de l'idée de Charlie Munger d'un <strong>« treillis de modèles mentaux » (latticework of mental models)</strong> — un esprit bâti à partir de nombreux cadres imbriqués.

Son rôle est de prendre la matière rassemblée par Alpha et de la transformer en une véritable décision d'investissement.

- Enregistrer une thèse et l'organiser en une carte de décision
- Mener une revue d'<strong>avocat du diable</strong> qui argumente délibérément le camp opposé
- Consigner les prédictions dans un registre de prédictions, puis y revenir plus tard pour voir si elles ont tenu

La structure que vous lisez sur le blog — « voici la conclusion », « ceci est un fait et ceci est une spéculation » — vient directement de Lattice. L'essentiel est de <strong>trancher, mais de le laisser sous une forme que l'on peut noter plus tard.</strong>

---

## 3. Arki — celui qui fait tourner le système

Arki est le rôle le moins visible, et peut-être le plus important. C'est celui qui <strong>maintient l'ensemble du système en bonne santé.</strong>

- Définir les schémas qui contiennent les données et l'agencement du coffre (vault) qui les stocke
- Gérer les tâches récurrentes et exécuter des contrôles de santé
- Tenir les journaux de migration et gouverner les permissions et les règles de chaque rôle

Si le système était une maison, Arki est celui qui veille à ce que l'électricité, l'eau et le chauffage continuent de fonctionner pendant qu'Alpha et Lattice travaillent. Ce n'est pas glamour, mais sans Arki les deux autres ne tiendraient pas longtemps.

---

## Ce que ces trois rôles ont produit — exemples concrets

En mots, cela reste abstrait ; voici donc deux articles récents passés par ce système.

- [Résultats du T1 de Dell et lecture de la marge des serveurs IA en Corée](/fr/post/dell-q1-fy2027-earnings-korea-ai-server-margin-readthrough-2026-05-29/) — Alpha a rassemblé les chiffres de résultats de Dell, et Lattice les a reliés à la chaîne de valeur des semi-conducteurs et des serveurs coréens pour bâtir une vision.
- [Résultats de Marvell au T1 FY2027 et lecture pour les semi-conducteurs coréens](/fr/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/) — même cheminement : partir des chiffres du silicium personnalisé de Marvell pour aboutir à une lecture coréenne.

Les deux articles séparent « ceci est un Fait, ceci est une Inférence, ceci est une Spéculation ». Cette habitude est précisément la structure qu'impose Lattice, et les faits qui la soutiennent sont ceux qu'Alpha a rassemblés.

---

## Pourquoi publier tout cela

Quand on fait de la recherche assez longtemps, le plus effrayant est <strong>« ne plus se souvenir de ce qu'on a dit avant ».</strong> Les thèses qui paraissent belles abondent ; revenir vérifier si elles étaient vraiment justes est fastidieux et inconfortable. Aussi, la plupart des analyses sont écrites une fois puis oubliées.

Thesis OS intègre délibérément cet inconfort dans le système. Chaque jugement reçoit une preuve attachée, chaque prédiction est consignée, et tout est noté plus tard. Non parce qu'il est parfait, mais parce qu'il est conçu pour que <strong>lorsqu'il se trompe, on puisse le voir.</strong>

Le système est conçu pour fonctionner en local. Vous pouvez l'essayer avec les données d'exemple fournies — sans clés d'API, sans identifiants de courtier, sans flux payants. La licence est MIT, et il faut Python 3.10 ou plus récent.

Et les trois canaux par lesquels ce système publie sont précisément ceux-ci : le <strong>blog (Korea Invest Insights)</strong> que vous lisez, <strong>Telegram @korea_invest_insights</strong>, et <strong>Substack</strong>.

---

## Venez jeter un œil

Le but de cet article n'est pas de se vanter — c'est une invitation. Si vous vous êtes déjà demandé comment rendre la recherche d'investissement plus honnête et plus vérifiable, jetez-y un coup d'œil.

> Vous n'avez pas à lire tout le code. Même un survol du README devrait vous donner une idée de « ah, c'est donc comme ça que ces articles de blog sont fabriqués ».

👉 <strong>[github.com/youngseongshin/thesis-investment-os](https://github.com/youngseongshin/thesis-investment-os)</strong>

Une étoile est bienvenue, mais simplement parcourir la structure convient tout autant. Il n'y a qu'une seule raison d'avoir levé le rideau : <strong>pour que vous puissiez voir par vous-même d'où et comment viennent les jugements de ce blog.</strong>

---

*Avertissement : à des fins de recherche et d'information uniquement. Il ne s'agit pas d'un conseil en investissement personnalisé. Le système open source décrit est un outil de recherche ; les lecteurs sont responsables de leurs propres décisions d'investissement et de leurs résultats.*
