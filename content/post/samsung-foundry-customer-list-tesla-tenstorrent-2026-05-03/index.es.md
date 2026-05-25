---
title: "Lista de clientes de Samsung Foundry 2026 — ¿Quién usa Samsung Foundry? Tesla, Tenstorrent, Qualcomm, Google, Ambarella y el resto del stack confirmado"
slug: samsung-foundry-customer-list-tesla-tenstorrent-2026-05-03
date: 2026-05-03T11:00:00+09:00
description: "Los clientes de Samsung Foundry en 2026 —confirmados mediante calls de resultados, divulgaciones de clientes e informes de cadena de suministro— incluyen a Tesla (HW5/sucesor de Dojo en SF2), Tenstorrent (Wormhole/Blackhole en SF4X), Qualcomm (ciertos nodos de módem y Snapdragon), Google (sucesores de TPU y SoC Pixel en SF4LPP/SF3), Ambarella (ADAS CV3-AD) y el propio System LSI de Samsung (Exynos). La lectura honesta es que Samsung Foundry sigue siendo un #2 creíble frente a TSMC en nodos avanzados, con una cartera de clientes muy orientada hacia aceleradores de IA, SoCs automotrices/ADAS y clientes dispuestos a asumir un diferencial de riesgo de rendimiento a cambio de disponibilidad de capacidad o razones de soberanía de suministro."
categories: ["Sector-Deep-Dive", "Korea Market", "AI Infrastructure"]
tags:
  - "Samsung Foundry"
  - "005930"
  - "Samsung Electronics"
  - "Tesla"
  - "Tenstorrent"
  - "Qualcomm"
  - "Google"
  - "Ambarella"
  - "TSMC"
  - "chip de IA"
  - "foundry"
  - "semiconductores"
  - "SF2"
  - "SF3"
  - "SF4"
  - "renta variable coreana"
---

> 🔗 <strong>Lecturas relacionadas</strong>: [Cuota de mercado HBM de SK hynix](/post/sk-hynix-hbm-market-share-ai-memory-demand-2026/) · [OpenEdges Technology — alpha de IP LPDDR6/5X para centros de datos](/post/openedges-lpddr-datacenter-ip-alpha-thesis-2026-04-30/) · [Big Tech 1T26 → Samsung Electronics vs Samsung Electro-Mechanics](/post/bigtech-1q26-samsung-electronics-vs-electro-mechanics-2026-04-30/)

*Este artículo responde directamente a la pregunta "¿Quién usa Samsung Foundry en 2026?" y explica por qué cada cliente está ahí, en qué nodo opera y qué dice la composición de clientes sobre el posicionamiento de Samsung Foundry frente a TSMC.*

---

## Resumen ejecutivo

<strong>La respuesta corta.</strong> La lista de clientes confirmados de Samsung Foundry en 2026, ordenada por relevancia económica, incluye:

- <strong>Tesla</strong> — cliente de múltiples generaciones (HW3 → trabajo previo en HW4), con el SoC de vehículo autónomo de nueva generación y aceleradores relacionados con Dojo en nodos avanzados de Samsung (SF4 / SF3 / SF2 según informes de prensa especializada).
- <strong>Tenstorrent</strong> — familias de aceleradores de IA Wormhole y Blackhole en nodos avanzados de Samsung Foundry, incluyendo el SF4X de clase 4nm. La casa de ASIC liderada por Jim Keller es un socio público de Samsung Foundry.
- <strong>Qualcomm</strong> — aprovisionamiento dual entre Samsung Foundry y TSMC; ciertos módems (5G/6G) y variantes seleccionadas de SoC Snapdragon se han fabricado históricamente en los nodos avanzados de Samsung.
- <strong>Google</strong> — SoCs Pixel Tensor (clase G3/G4) en los nodos de clase 4nm de Samsung; parte de la producción relacionada con TPU ha utilizado históricamente capacidad de Samsung, aunque TSMC es el principal proveedor en las últimas generaciones de TPU.
- <strong>Ambarella</strong> — SoCs automotrices ADAS CV3-AD en el nodo de clase 5nm de Samsung.
- <strong>Samsung System LSI</strong> — Exynos 2400 / Exynos Auto / lógica de sensores de imagen, la carga de trabajo cautiva que ancla la capacidad de Samsung Foundry.
- <strong>Trabajo NVIDIA-adyacente y de startups de IA</strong> — ciertos chips aceleradores y de redes han utilizado capacidad de Samsung históricamente.
- <strong>Fabless coreanos y japoneses</strong> — Rebellions, FuriosaAI (próxima generación Renegade), clientes del nivel DB HiTek y casas asiáticas de AI-ASIC utilizan las líneas de producción de Samsung Foundry en 4 / 5 / 8 / 12nm.

<strong>La lectura honesta.</strong> Samsung Foundry en 2026 <strong>no</strong> es el igual de TSMC en el extremo más avanzado — TSMC sigue ganando el trabajo de aceleradores de IA de mayor volumen en el filo tecnológico (NVIDIA, AMD, Apple silicon). Lo que Samsung Foundry <strong>sí es</strong> en 2026 es un #2 creíble con una cartera de clientes muy orientada hacia (a) aceleradores de IA que necesitan capacidad fuera de TSMC, (b) SoCs automotrices / ADAS, (c) clientes dispuestos a asumir un diferencial de riesgo de rendimiento por razones de capacidad, soberanía de suministro o precio. La composición de clientes es exactamente la que cabría esperar de una "foundry retadora con capacidad real en nodos avanzados y preguntas persistentes sobre rendimiento."

---

## 1. Por qué "¿Quién usa Samsung Foundry?" es la pregunta correcta

El posicionamiento de Samsung Foundry ha sido objeto de más cobertura contradictoria en la prensa especializada que casi cualquier otro tema en semiconductores. Una semana el titular es "Samsung gana a Tesla / Qualcomm / Google" — la semana siguiente es "Samsung pierde [X] frente a TSMC."

Para cortar el ruido hace falta una pregunta diferente. No "¿está ganando Samsung Foundry?" — esa pregunta no tiene una respuesta limpia porque depende del modelo que se adopte. En cambio: <strong>¿quién usa realmente Samsung Foundry en 2026, y qué dice la mezcla de clientes?</strong>

La mezcla de clientes es la única lectura honesta del posicionamiento de una foundry, porque:

1. <strong>La asignación de capacidad es observable.</strong> Las divulgaciones de clientes, las referencias en calls de resultados y los informes de cadena de suministro de la prensa especializada revelan quién está fabricando obleas en qué fab.
2. <strong>La composición de clientes codifica las compensaciones de rendimiento, capacidad y precio.</strong> Una foundry que gana un cliente en un nodo avanzado o bien tiene resuelto el problema de rendimiento de ese nodo, o bien tiene una ventaja de capacidad que TSMC no puede igualar, o bien está fijando precios de forma agresiva. La mezcla de clientes indica cuál de las tres se aplica.
3. <strong>La mezcla de clientes predice la utilización en 2027–2028.</strong> La cartera de clientes de Samsung Foundry en 2026 define en gran medida sus volúmenes de producción en 2027. Los clientes visibles hoy *son* los dos próximos años de ingresos.

---

## 2. El stack de clientes confirmados — quién, dónde y por qué

### 2.1 Tesla — el ancla multigeneracional

<strong>Estado.</strong> Tesla ha sido cliente de Samsung Foundry en múltiples generaciones. El chip FSD Hardware 3 (HW3) se fabricó en el nodo de 14nm de Samsung. El chip Hardware 4 (HW4) pasó al nodo de clase 7nm de Samsung. El Hardware 5 / SoC de vehículo autónomo de próxima generación ha sido asociado en la prensa especializada con el SF4 de Samsung y los nodos del roadmap futuro (SF3 / SF2), con uso continuo de capacidad Samsung a lo largo de 2026 y más allá.

<strong>Por qué Samsung.</strong> Tesla ha operado sistemáticamente con aprovisionamiento de obleas de doble proveedor — TSMC para la producción de aceleradores GPU/IA de clase Dojo, Samsung para el SoC FSD/HW. El compromiso con Samsung refleja probablemente una combinación de (a) disponibilidad de capacidad que TSMC no podía igualar para los volúmenes de Tesla, (b) apalancamiento de precios que Tesla extrajo de la posición retadora de Samsung, y (c) la continuidad de la plataforma FSD construida en la relación desde el HW3.

<strong>Qué significa para Samsung.</strong> Tesla es lo más parecido que tiene Samsung Foundry a un "cliente trofeo" — un nombre cotizado en EE.UU. de alto perfil cuyos vehículos dependen del silicio fabricado por Samsung. Perder Tesla frente a TSMC sería una de las señales más dañinas posibles; mantener a Tesla a través del HW5 es una de las señales positivas más fuertes disponibles.

### 2.2 Tenstorrent — la apuesta pública de Jim Keller por Samsung

<strong>Estado.</strong> El acelerador de IA Wormhole de Tenstorrent y la próxima generación Blackhole están públicamente declarados como producción de Samsung Foundry. El CEO de Tenstorrent, Jim Keller, ha dado múltiples entrevistas públicas sobre la asociación con Samsung Foundry, con la empresa trasladando trabajo de producción en nodos avanzados al SF4X de clase 4nm de Samsung.

<strong>Por qué Samsung.</strong> El posicionamiento de Tenstorrent es "el startup de aceleradores de IA que apuesta contra el stack NVIDIA/CUDA." Elegir Samsung sobre TSMC para producción en nodos avanzados es coherente con ese posicionamiento contrario. La disponibilidad de capacidad de Samsung y un modelo de colaboración más flexible que el marco de prioridad de clientes tier-1 de TSMC se consideran factores relevantes.

<strong>Qué significa para Samsung.</strong> Tenstorrent es el respaldo más público de acelerador de IA que tiene Samsung Foundry. A medida que escalan los envíos de Tenstorrent, aumenta la exposición de ingresos de Samsung Foundry a aceleradores de IA distintos de NVIDIA. Esto representa una diversificación significativa respecto a la imagen de "Samsung Foundry = carga de trabajo cautiva de Samsung System LSI."

### 2.3 Qualcomm — doble aprovisionamiento entre Samsung y TSMC

<strong>Estado.</strong> Los SoCs Snapdragon de gama alta de Qualcomm se han dividido históricamente entre Samsung Foundry y TSMC a lo largo de las generaciones. El Snapdragon 8 Gen 1 fue una victoria notable de Samsung en clase 4nm; los flagships posteriores (Snapdragon 8 Gen 2, Gen 3, Snapdragon 8 Elite) se trasladaron principalmente a TSMC. Sin embargo, Qualcomm sigue produciendo ciertos módems y variantes Snapdragon de nivel inferior en capacidad de Samsung Foundry.

<strong>Por qué Samsung.</strong> El doble aprovisionamiento protege a Qualcomm contra las restricciones de capacidad y el apalancamiento de precios de TSMC. La relación con Samsung otorga a Qualcomm una posición negociadora creíble frente a TSMC. Para Samsung Foundry, la relación con Qualcomm — incluso a volumen sub-flagship — es un cliente de referencia importante que señala que "los nodos de Samsung tienen grado de producción comercial."

<strong>Qué significa para Samsung.</strong> El volumen de Qualcomm en Samsung Foundry no es el trabajo estrella de Snapdragon flagship; es el trabajo de producción estable que llena la capacidad de nivel medio. Hay que estar atentos al Snapdragon 8 Gen 5 o futuros flagships que regresen a Samsung Foundry — eso sería una señal positiva importante.

### 2.4 Google — SoCs Pixel Tensor y trabajo seleccionado de TPU

<strong>Estado.</strong> Los SoCs Google Pixel Tensor (G1, G2, G3, G4) se han fabricado en Samsung Foundry, aprovechando la IP de diseño derivada del Exynos de Samsung System LSI y la producción en clase 5nm/4nm. Parte de la producción de TPU (generaciones anteriores, capacidad suplementaria) ha utilizado históricamente Samsung; las últimas generaciones de TPU están predominantemente en TSMC.

<strong>Por qué Samsung.</strong> El linaje de diseño del Pixel Tensor a partir de la IP de Samsung System LSI convierte a Samsung Foundry en el socio de producción natural. Para el trabajo de TPU, Samsung ha sido un complemento de capacidad más que un socio principal.

<strong>Qué significa para Samsung.</strong> El volumen de Google Pixel no es enorme en términos absolutos de foundry, pero la relación tiene alto perfil y genera demanda de arrastre para el nodo de clase 4nm de Samsung. El factor de variación más relevante es si los TPU de próxima generación retornan significativamente a capacidad de Samsung.

### 2.5 Ambarella — SoCs ADAS automotrices

<strong>Estado.</strong> La familia CV3-AD de Ambarella — el acelerador de IA automotriz flagship de la empresa para aplicaciones ADAS y conducción autónoma — se fabrica en el nodo de clase 5nm de Samsung Foundry. Ambarella ha declarado públicamente a Samsung Foundry como su socio en 5nm.

<strong>Por qué Samsung.</strong> Los clientes automotrices valoran (a) la continuidad de suministro — el compromiso de Samsung con la producción de grado automotriz a largo plazo, (b) la disponibilidad de capacidad — la capacidad automotriz de 5nm de TSMC está muy sobreasignada por Apple/AMD/NVIDIA, (c) la acreditación del sistema de calidad de grado automotriz de Samsung.

<strong>Qué significa para Samsung.</strong> Ambarella es el cliente de referencia más claro en "5nm automotriz" que tiene Samsung. A medida que ADAS / L2+ / L3 de autonomía escala entre los fabricantes de automóviles globales, la demanda de capacidad automotriz de grado avanzado de Samsung aumenta.

### 2.6 Samsung System LSI — el ancla de carga de trabajo cautiva

<strong>Estado.</strong> La propia división System LSI de Samsung — SoCs móviles Exynos, Exynos Auto para automoción, lógica de sensores de imagen, ICs de módem — es el mayor cliente interno de Samsung Foundry. El Exynos 2400 (serie Galaxy S24), el Exynos Auto V920 (asociaciones Hyundai Pleos / Kia) y la lógica de sensores de imagen están todos en nodos avanzados de Samsung Foundry.

<strong>Por qué Samsung.</strong> Cautivo — por definición.

<strong>Qué significa para Samsung.</strong> Este es el suelo. Incluso si todos los clientes externos desaparecieran mañana, Samsung System LSI mantendría operativas las fabs de nodos avanzados de Samsung Foundry. La carga de trabajo cautiva es también la fuente de gran parte del desarrollo de IP de Samsung Foundry, la curva de aprendizaje de rendimiento y la maduración del proceso. La interpretación honesta: las victorias de clientes externos importan como <strong>crecimiento adicional sobre</strong> la base cautiva.

### 2.7 La capa fabless coreana y asiática

<strong>Estado.</strong> Una larga cola de clientes fabless coreanos y asiáticos utiliza Samsung Foundry en los nodos de 4 / 5 / 8 / 12 / 14nm. Los clientes confirmados y mencionados públicamente incluyen:

- <strong>Rebellions</strong> — startup coreano de aceleradores de IA (REBEL-Quad / acelerador de próxima generación en nodos avanzados de Samsung).
- <strong>FuriosaAI</strong> — chip Renegade en el 5nm de Samsung Foundry; componentes de próxima generación en desarrollo.
- <strong>DeepX</strong> — startup coreano de IA en el borde, Samsung Foundry.
- <strong>OpenEdges Technology</strong> — IP de subsistema de memoria coreano (PHY/Controlador LPDDR6/5X con silicon-proven en Samsung SF5A; en desarrollo en 4nm de Samsung).
- <strong>Varios fabless japoneses</strong> — cargas de trabajo automotrices, de sensores de imagen y de IA.

<strong>Por qué Samsung.</strong> Proximidad geográfica, soporte de IR/ingeniería en coreano, ecosistema de socios IP Samsung SAFE (Cadence, Synopsys, OpenEdges como socio Sub-License) y accesibilidad de precios para clientes no tier-1.

<strong>Qué significa para Samsung.</strong> Esta capa carece de glamour pero es duradera. Es la que hace viable la utilización de procesos de volumen de Samsung Foundry en los nodos de 4 / 5 / 8nm. Es también la capa que más se beneficia directamente de cualquier ola de startups de ASIC de IA originada en Corea o Asia.

### 2.8 El conjunto de "ex clientes"

Por precisión, varios nombres importantes <strong>ya no son</strong> clientes principales de Samsung Foundry a pesar de referencias antiguas en la prensa especializada:

- <strong>NVIDIA</strong> — Las GPUs A8000 / GA100-era Ampere se fabricaron parcialmente en Samsung 8nm, pero el mercado migró rápidamente a TSMC para Hopper, Blackwell y Rubin. NVIDIA hoy es abrumadoramente TSMC.
- <strong>Apple</strong> — No ha sido un cliente significativo de Samsung Foundry para silicio avanzado de iPhone/Mac desde la era del A9. Todo el silicon actual de Apple es TSMC.
- <strong>AMD</strong> — Las CPUs/GPUs de AMD en el filo tecnológico son TSMC; parte del trabajo legacy de AMD usó GlobalFoundries; Samsung no es actualmente un socio de nodos avanzados de AMD de escala relevante.

La rotación de clientes es real. La mezcla de Samsung Foundry en 2026 es estructuralmente diferente de la de 2020.

---

## 3. Lo que dice la composición de clientes

### 3.1 Reconocimiento de patrones en la mezcla de clientes

Al leer la lista confirmada de 2026 como una imagen única, emergen cuatro patrones:

| Patrón | Lo que dice sobre Samsung Foundry |
| --- | --- |
| <strong>Fuerte peso en aceleradores de IA (Tenstorrent, Tesla, Rebellions, FuriosaAI, Ambarella)</strong> | La posición retadora es real. Samsung es la foundry de los "aceleradores de IA que no van a TSMC." |
| <strong>Fuerte exposición automotriz/ADAS (Tesla, Ambarella, Samsung Auto, Hyundai Pleos)</strong> | El sector automotriz es una ventaja estructural donde el compromiso a largo plazo, la capacidad y los sistemas de calidad de Samsung superan el estatus tier-2 automotriz de TSMC. |
| <strong>Samsung System LSI cautivo como suelo</strong> | El suelo de utilización de la fab es independiente de las victorias de clientes externos. |
| <strong>Móvil de nivel medio (Qualcomm sub-flagship, Google Pixel, fabless coreano/asiático)</strong> | Samsung es competitivo en el "punto óptimo de volumen de producción" de 4 / 5 / 8 / 12nm más que en el filo tecnológico. |

### 3.2 Lo que *aún no* aparece en la lista (y por qué importa)

Igualmente informativo: quién <strong>no</strong> está en la lista de clientes de Samsung Foundry a fecha de 2026.

- <strong>Ningún hiperscaler de IA en el filo tecnológico</strong> — NVIDIA, AMD, Apple silicon, Microsoft Maia (TSMC), Meta MTIA (TSMC) son todos TSMC. El esfuerzo de clase 2nm de Samsung (SF2) presenta incertidumbre de rendimiento y clientes hacia 2027.
- <strong>No se reporta ningún Snapdragon flagship en SF3 / SF2.</strong> Hasta que eso cambie, persiste la brecha de volumen de flagship móvil de Samsung.

Estas ausencias *no* son un fracaso. Son la brecha que los nodos SF2 y SF1.4 de Samsung deben cerrar en 2027–2028 para pasar de "un #2 creíble" a "paridad comercial con TSMC."

### 3.3 La lectura de foundry retadora

Reducido a una frase: <strong>Samsung Foundry en 2026 está ganando a los clientes que necesitan capacidad, quieren evitar la concentración en TSMC, o valoran el compromiso a largo plazo de grado automotriz — y aún no está ganando el volumen de aceleradores de IA de hiperscaladores en el filo tecnológico.</strong>

Ese es exactamente el perfil de clientes de un #2 creíble en un duopolio, con opcionalidad retadora sostenida en los próximos nodos.

---

## 4. Implicaciones para la renta variable de Samsung Electronics

Este artículo no es una recomendación de inversión, pero la composición de clientes tiene implicaciones directas sobre cómo interpretar Samsung Electronics (KS: 005930):

1. <strong>Samsung Foundry no es la línea de ingresos del filo tecnológico.</strong> El crecimiento en memoria de IA para Samsung Electronics fluye a través de DS Memory (expansión de clientes HBM4 hacia NVIDIA, DRAM de servidor de IA), no a través de las victorias de clientes externos de Samsung Foundry. Confundir ambas líneas lleva a lecturas erróneas.
2. <strong>Las victorias de clientes de Samsung Foundry son duraderas, no explosivas.</strong> Tesla, Tenstorrent, Ambarella, Google Pixel y la capa fabless coreana/asiática componen de forma sostenida. No generan un trimestre único que revalorice la acción.
3. <strong>La inflexión de clase 2nm (SF2) es la verdadera variable determinante.</strong> Si Samsung Foundry puede ganar al menos un gran cliente externo de IA en SF2 en 2027–2028 es el resultado binario que reposiciona materialmente la trayectoria de ingresos de Samsung Foundry y el perfil de margen global del segmento foundry de Samsung.
4. <strong>La capa de AI ASIC coreana / asiática se vuelve relevante con el escalado de múltiples clientes.</strong> Una sola victoria de Rebellions o FuriosaAI es pequeña. Cinco a diez startups de aceleradores de IA coreanos / asiáticos escalando simultáneamente en capacidad de Samsung de 4 / 5nm se vuelve material.

---

## 5. Preguntas frecuentes

<strong>P: ¿Samsung Foundry es lo mismo que Samsung Electronics?</strong>
R: Samsung Foundry es la división de fabricación de chips por contrato de Samsung Electronics (KOSPI: 005930). Se encuadra dentro de la división DS (Device Solutions) de Samsung junto con Memory y System LSI. No es una entidad cotizada por separado.

<strong>P: ¿Cotiza Samsung Foundry en bolsa?</strong>
R: No por separado. Para obtener exposición, se compran acciones de Samsung Electronics (005930). Los ingresos y el beneficio operativo de Samsung Foundry se reportan como parte del segmento DS Foundry dentro de las cuentas consolidadas de Samsung Electronics.

<strong>P: ¿Sobre qué nodos de proceso produce actualmente Samsung Foundry?</strong>
R: A fecha de 2026, Samsung Foundry está en producción en nodos de clase 14 / 8 / 7 / 5 / 4 / 3nm. El nodo GAA (gate-all-around) de clase 3nm ha estado en producción desde 2022, con continua rampa de rendimiento y clientes. El nodo de clase 2nm (SF2) es el siguiente gran objetivo.

<strong>P: ¿Quién es el mayor cliente de Samsung Foundry?</strong>
R: En cuanto a carga de trabajo interna, Samsung System LSI (Exynos, sensor de imagen, módem) es la mayor. Entre los clientes externos, Tesla y Qualcomm han sido históricamente los de mayor volumen; Tenstorrent y Google Pixel también son significativos.

<strong>P: ¿Fabrica Samsung Foundry chips para NVIDIA?</strong>
R: No en la generación actual de 2026. Los aceleradores de IA de última generación de NVIDIA (Hopper, Blackwell, Rubin) están en TSMC. Samsung produjo las GPUs de generación Ampere de NVIDIA en 8nm, pero NVIDIA migró a TSMC en generaciones posteriores.

<strong>P: ¿Compite Samsung Foundry con TSMC?</strong>
R: Sí — Samsung es ampliamente considerado el retador #2 de TSMC en nodos avanzados. TSMC mantiene la base de clientes hiperscaladores de IA en el filo tecnológico; Samsung compite eficazmente en automoción, startups de aceleradores de IA, nivel medio móvil y segmentos fabless coreanos/asiáticos.

<strong>P: ¿Está Samsung Foundry perdiendo clientes frente a TSMC?</strong>
R: La rotación de clientes ocurre en ambas direcciones. Samsung perdió volumen significativo de Apple / NVIDIA / AMD en el filo tecnológico durante el período 2018–2024. Ha ganado la continuidad multigeneracional de Tesla, Tenstorrent, Ambarella y una base creciente de clientes fabless coreanos / asiáticos. La mezcla de clientes de 2026 es estructuralmente diferente de la de 2020.

<strong>P: ¿Qué es el nodo SF2?</strong>
R: SF2 es el proceso de clase 2nm de Samsung Foundry, incluido en el roadmap publicado por la empresa para la rampa de producción a finales de 2025/2026. Si Samsung gana al menos un gran cliente externo en SF2 — en particular algún acelerador de IA en el filo tecnológico — es la inflexión más vigilada de 2026–2027 para el posicionamiento de Samsung Foundry.

---

## 6. Marco de cierre

Lo más informativo que se puede hacer con la pregunta "¿Quién usa Samsung Foundry?" es <strong>dejar que la respuesta cambie la forma de enmarcar a Samsung Foundry en sí misma</strong>. Leída como una lista de nombres, la cartera de clientes de 2026 dice "Samsung Foundry es una foundry seria con clientes serios." Leída como un *patrón* — fuerte peso en aceleradores de IA + automoción + fabless coreano / asiático + Samsung System LSI cautivo — la misma lista dice "Samsung Foundry es el retador creíble de TSMC, con la mezcla de clientes que cabría esperar de un #2 en un duopolio."

Ambas lecturas son correctas. Cuál importa para tu decisión depende de si haces la pregunta por razones de aprovisionamiento, de asignación de renta variable, o para entender el mapa global de semiconductores. Para los tres casos, la respuesta es más útil de lo que sugiere el ruido de los titulares.

---

## Apéndice — Nivel de evidencia

### [Hecho]

- Samsung Foundry es la división de fabricación de chips por contrato de Samsung Electronics (KOSPI: 005930), encuadrada dentro de la división DS (Device Solutions) junto con Memory y System LSI.
- Tesla ha sido cliente multigeneracional de Samsung Foundry (HW3 en 14nm, HW4 en clase 7nm, compromiso continuo en generaciones posteriores).
- Los aceleradores Wormhole y Blackhole de Tenstorrent se producen en nodos avanzados de Samsung Foundry incluyendo SF4X.
- Qualcomm ha realizado doble aprovisionamiento entre Samsung Foundry y TSMC, con el Snapdragon 8 Gen 1 notablemente fabricado en el 4nm de Samsung.
- Los SoCs Google Pixel Tensor (G1–G4) se han fabricado en Samsung Foundry.
- La familia ADAS CV3-AD de Ambarella está en el nodo de clase 5nm de Samsung.
- Samsung System LSI (Exynos, lógica de sensores de imagen, módem) es la carga de trabajo cautiva en Samsung Foundry.
- Clientes fabless coreanos incluyendo Rebellions, FuriosaAI (Renegade), DeepX y OpenEdges Technology utilizan los nodos de 4 / 5 / 8 / 12nm de Samsung Foundry.
- Las generaciones Hopper / Blackwell / Rubin de NVIDIA están en TSMC, no en Samsung.
- El silicon de Apple está en TSMC, no en Samsung, desde la era del A9.

### [Inferencia]

- La relación con Tesla a través del HW5 es la señal de continuidad de cliente externo individual más vigilada de Samsung Foundry.
- La asociación con Tenstorrent representa el respaldo de acelerador de IA no NVIDIA más claro de Samsung Foundry.
- La concentración de la mezcla de clientes en aceleradores de IA, automoción y fabless coreano/asiático refleja el posicionamiento retador de Samsung — disponibilidad de capacidad, valor de doble proveedor y flexibilidad de precios — más que paridad de rendimiento en el filo tecnológico con TSMC.
- La cartera de clientes externos del nodo SF2 (2nm) será el mayor factor de entrada para cómo se reposicione Samsung Foundry en el duopolio global de foundries a lo largo de 2027–2028.

### [Especulación]

- El retorno de un Snapdragon flagship a Samsung Foundry en SF3 o SF2 sería una señal importante de revalorización positiva para el segmento foundry de Samsung.
- El compromiso continuo de Tesla a través del HW5 y más allá anclaría los ingresos de nodos avanzados de grado automotriz de Samsung a escala significativa hasta 2028.
- Una victoria de Samsung Foundry sobre al menos un acelerador hiperscalador de IA externo en SF2 desplazaría materialmente el actual encuadre de "un #2 creíble" hacia "competitivo comercialmente en el filo tecnológico."

### [Bloqueado]

- Contribuciones de volumen de obleas por cliente a los ingresos trimestrales del segmento DS Foundry de Samsung Foundry.
- Curvas de rendimiento por nodo de Samsung Foundry y trayectorias de tasa de aprendizaje.
- Términos de precios confidenciales de clientes tier-1 que comparen directamente TSMC y Samsung Foundry en el mismo nodo.
- La lista completa de clientes externos para los design starts de SF2 de Samsung Foundry.

---

<strong>Aviso legal</strong>: Este artículo es comentario de investigación, no asesoramiento de inversión. Las descripciones de la mezcla de clientes se basan en referencias de clientes divulgadas públicamente, comentarios en calls de resultados e informes de cadena de suministro de la prensa especializada; las asignaciones específicas de volumen de obleas no son públicas. La lista de clientes de Samsung Foundry cambia continuamente. Los tickers citados son ilustrativos para el marco analítico, no recomendaciones. Realice su propia diligencia debida y consulte a asesores con licencia antes de cualquier decisión de inversión.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
