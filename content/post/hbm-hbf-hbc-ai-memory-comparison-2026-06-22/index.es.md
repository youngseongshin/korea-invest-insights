---
title: "HBM, HBF y HBC: Cómo distinguir las tres tecnologías de memoria para IA"
slug: "hbm-hbf-hbc-ai-memory-comparison-2026-06-22"
date: 2026-06-22T10:00:00+09:00
description: "HBM, HBF y HBC no son del mismo tipo. Este análisis mapea el ancho de banda, la capacidad y el costo de inferencia como tres obstáculos distintos, compara la madurez con honestidad y explica por qué son complementarios."
categories: ["Exclusive Analysis", "Tech-Analysis"]
tags: ["HBM", "HBF", "HBC", "AI Memory", "Semiconductor", "SK Hynix", "Samsung Electronics", "Micron", "Qualcomm", "NAND", "DRAM"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexto
> Este artículo es el trasfondo técnico de [¿Quién pagará el consenso semiconductor de 2027?](/es/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/), [El IPO de CXMT y el riesgo de precios de memoria](/es/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/) y [Por qué el superciclo de la IA se alarga](/es/post/ai-supercycle-extension-agent-demand-ipo-funding-memory-storage-2026-06-12/). Si los artículos anteriores cubrieron demanda, precios y valoración, este texto examina <strong>qué son realmente las tres tecnologías de memoria para IA, cuánto está demostrado cada una y cuál es su relación mutua</strong>. Los hubs relacionados son el [Hub HBM de semiconductores coreanos](/es/page/korea-semiconductor-hbm-kospi-hub/) y el [Hub de Análisis Exclusivo](/es/page/exclusive-analysis-hub/).

## TL;DR

* HBM, HBF y HBC no son el mismo tipo de memoria. <strong>HBM y HBF son componentes de memoria</strong>, mientras que <strong>HBC es el nombre de la arquitectura de acelerador de Qualcomm</strong>. Alinear los tres y comparar solo cifras en TB/s conduce inevitablemente a lecturas erróneas.
* Cada tecnología ataca un obstáculo diferente: <strong>HBM ataca el muro del ancho de banda</strong>, <strong>HBF ataca el muro de la capacidad</strong> y <strong>HBC apunta al costo de inferencia y al consumo energético</strong>.
* La brecha de madurez es enorme: <strong>HBM está en producción en masa total (★★★★★)</strong>, <strong>HBF está en fase de simulación (★★, con muestras previstas para el segundo semestre de 2026)</strong> y <strong>HBC es un plano de diseño (★, con muestras previstas para 2027)</strong>.
* Los tres son complementarios, no sustitutos. La "temperatura" de los datos determina el lugar de cada uno: los datos calientes (caché KV) van a HBM, los datos fríos (pesos de modelo congelados) van a HBF, y la inferencia de bajo costo apunta a la dirección de HBC.
* Ninguna tecnología amenaza hoy la posición de HBM como memoria de trabajo. La contribución de ingresos significativa de HBF y HBC llegará, en el mejor de los casos, en 2027-2028. \[Inferencia\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Marco clave</div>
  <div class="thesis-callout__body">
    En la guerra de la memoria para IA, solo HBM está demostrado. HBF es una promesa y HBC es un plano de diseño. Los tres no son competidores; son componentes complementarios que ocupan diferentes niveles de la jerarquía de memoria.
  </div>
</div>

---

## 1. El cuello de botella de la IA no es el cómputo, sino la memoria

La capacidad de cómputo de las GPU creció aproximadamente 80 veces en la última década, pero el ancho de banda de la memoria apenas lo hizo 17 veces. \[Hecho: comparación de especificaciones por generación de NVIDIA\] Esa brecha es el verdadero cuello de botella de los aceleradores de IA actuales. Los chips de IA caros pasan cada vez más tiempo esperando datos, y la velocidad a la que un LLM genera un token depende casi por completo de la rapidez con la que la memoria puede transportar esos datos.

Este cuello de botella se divide en dos muros.

<strong>El muro del ancho de banda:</strong> el problema de no poder transportar datos con suficiente rapidez. La fase de decodificación en la inferencia de LLM debe leer desde la memoria los enormes pesos del modelo en cada token generado, lo que la encadena permanentemente a la velocidad de la memoria.

<strong>El muro de la capacidad:</strong> el problema de no poder almacenar suficientes datos. El caché KV generado en un contexto de 128 000 tokens alcanza aproximadamente 343 GB, superando ya la capacidad HBM de 192 GB de las GPU más recientes (B200). \[Hecho: cálculo a partir de especificaciones públicas\]

HBM, HBF y HBC son tecnologías que atacan estos dos muros de formas distintas. Y una de las tres no es un componente de memoria, sino la arquitectura de acelerador de una empresa. Perder de vista esa distinción invalida cualquier comparación.

---

## 2. HBM: la única tecnología demostrada, resuelve el muro del ancho de banda

### Concepto

La idea del HBM (High Bandwidth Memory) es sencilla. Se apilan 8 a 16 capas de chips DRAM verticalmente, se colocan justo al lado de la GPU y se conectan mediante miles de electrodos diminutos (TSV), ampliando el canal de transferencia a 1 024 o 2 048 bits de una sola vez. La velocidad no viene de que cada pin sea más rápido, sino de que el canal es extremadamente ancho. Una carretera de 2 048 carriles, aunque cada carril sea algo más lento, mueve un volumen total de tráfico muy superior a una autopista de un solo carril.

### Rendimiento y madurez

El ancho de banda de una sola pila HBM3E es de aproximadamente 1,2 TB/s y el de HBM4 ronda los 2 TB/s. \[Hecho: especificaciones JEDEC\] Eso supone 20-30 veces el ancho de banda de DDR5. Prácticamente todos los aceleradores de IA, desde el NVIDIA H100, H200 y B200 hasta el AMD MI300, utilizan HBM.

<strong>Madurez ★★★★★:</strong> de las tres tecnologías, solo HBM está en producción en masa completa. Años de fabricación a gran escala han validado el rendimiento y la fiabilidad. SK Hynix mantiene una cuota de mercado de aproximadamente el 57-62 % y conserva su posición como proveedor principal de NVIDIA. \[Hecho: IR corporativo y estimaciones de mercado\]

### Hoja de ruta y actores

La hoja de ruta avanza de HBM4 (producción en masa en 2026, con adopción de die base lógico) a HBM4E (personalizado) y HBM5 (objetivo para 2029, ~4 TB/s). A partir de HBM4, SK Hynix fabricará el die base con el proceso de 12 nm de TSMC, lo que consolida una estructura de diseño conjunto entre fabricantes de memoria y fundición. \[Hecho: anuncios corporativos\] \[Inferencia: los 4 TB/s de HBM5 son un objetivo en la hoja de ruta, aún sin medición real\]

El mercado es un oligopolio de SK Hynix, Samsung Electronics y Micron, con TSMC apuntalando la base mediante el die base y el interposer. El mercado de memoria para IA es una estructura de colaboración entre los tres fabricantes de memoria, TSMC y NVIDIA. \[Inferencia: el tamaño del mercado se estima en unos 35 000 millones de dólares en 2025, subiendo a 45 000-58 000 millones en 2026, con considerable variación entre fuentes\]

---

## 3. HBF: el aspirante que ataca el muro de la capacidad, aún en fase de promesa

### Concepto

La idea de HBF (High Bandwidth Flash) es ingeniosa. Toma prestado el método de apilado e interfaz de HBM, pero reemplaza la DRAM cara del interior por flash NAND de menor precio. La NAND almacena varios bits por celda, lo que permite capacidades mayores y un costo por gigabyte mucho más bajo. En agosto de 2025, SanDisk y SK Hynix anunciaron su colaboración en la estandarización. SanDisk describió la tecnología como "un complemento de HBM, no un sustituto". \[Hecho: anuncio conjunto de SanDisk y SK Hynix\]

SanDisk afirma que una pila puede albergar aproximadamente 512 GB (8-16 veces más que HBM) con un ancho de banda de alrededor de 1,6 TB/s. \[Hecho: ficha técnica de SanDisk\]

### Una evaluación honesta de la madurez

Aquí hay que detenerse.

<strong>Madurez ★★:</strong> HBF aún no está en producción en masa ni cuenta con un benchmark independiente de un chip físico real. Las cifras de 512 GB y 1,6 TB/s provienen de simulaciones internas de SanDisk, y las notas al pie de la ficha técnica lo confirman explícitamente: "pruebas internas y simulaciones con supuestos de modelo específicos". \[Hecho: notas al pie de la ficha técnica de SanDisk\] El objetivo de primera muestra física es el segundo semestre de 2026, y la adopción en dispositivos de inferencia está prevista para 2027 en adelante. Apilar 238 capas de NAND en 16 niveles supone una dificultad de apilado que supera las 5 000 capas en total.

### Las limitaciones de la NAND determinan su uso

HBF tiene dos restricciones fundamentales.

Primera, <strong>la latencia:</strong> la NAND lee más lento que la DRAM, por lo que la latencia de HBF es unas 100 veces mayor que la de HBM (HBF ~10 µs frente a HBM en decenas de nanosegundos). \[Hecho: características físicas del medio\]

Segunda, <strong>la durabilidad de escritura:</strong> la NAND tiene un límite en el número de ciclos de escritura, lo que la hace inadecuada para cargas de trabajo que se actualicen con frecuencia.

Estas dos limitaciones definen el caso de uso de HBF: <strong>almacenamiento de gran capacidad para los pesos del modelo</strong>, que apenas cambian y solo se leen. En ese uso, las limitaciones apenas suponen un problema.

### La variable decisiva: la adopción por parte de NVIDIA

<strong>NVIDIA no muestra actualmente un gran interés por HBF.</strong> Las señales apuntan a que prefiere resolver el problema de capacidad mediante SSD de alta velocidad conectados directamente a la GPU (eSSD), y el principal cliente que ha mostrado interés en HBF es principalmente Google. \[Inferencia: síntesis de observaciones del sector y publicaciones públicas\] La decisión del cliente más importante es la mayor incógnita que determinará el éxito o fracaso de HBF.

Los actores son SanDisk como líder, SK Hynix como colaborador y Samsung con participación en el proyecto, mientras que Kioxia ha optado por la vía del eSSD. El campo aún no ha tomado forma definitiva.

---

## 4. HBC: no es memoria, sino la arquitectura de acelerador de Qualcomm

### Aclaración terminológica

'HBC' es un acrónimo con trampa. Aparece junto a HBM y HBF, pero <strong>HBC es el nombre de la arquitectura del acelerador de IA que Qualcomm presentó en su Día del Inversor en junio de 2026</strong> ('High Bandwidth Compute'). No es un término estándar acordado entre múltiples empresas, sino la marca de una sola compañía. \[Hecho: anuncio oficial de Qualcomm\]

El mismo acrónimo 'HBC' colisiona con el 'High Bandwidth Cache (HBCC)' de AMD y también se confunde con HBF. Los tres son conceptos completamente distintos.

Por lo tanto, la comparación "HBM vs HBF vs HBC" es en rigor una comparación entre <strong>dos componentes de memoria y un diseño de sistema de acelerador</strong>. Sin entender esa asimetría, es fácil caer en afirmaciones erróneas como "HBC tiene 18 veces más ancho de banda que HBM" (las bases de medición son distintas).

### Concepto y tecnología

El medio de memoria que usa HBC no es HBM, sino <strong>LPDDR</strong> (la DRAM de bajo consumo que se usa en smartphones). La idea es apilar esta LPDDR de bajo costo directamente sobre el chip de lógica de cómputo en 3D, reduciendo casi a cero la distancia entre el cómputo y la memoria. El enfoque no requiere un costoso interposer de silicio ni HBM caro, y apunta a reducir el costo y el consumo energético de la inferencia.

Qualcomm presenta cifras como 6 veces el ancho de banda por vatio frente a HBM y 200 veces la capacidad por vatio frente a SRAM. \[Hecho: anuncio de Qualcomm\] Sin embargo, estas cifras son afirmaciones propias de Qualcomm normalizadas a nivel de tarjeta o rack, y compararlas directamente con las cifras de HBM a nivel de pila produce confusiones de base.

### Madurez y realidad

<strong>Madurez ★:</strong> el acelerador AI250 de Qualcomm que incorpora HBC no existe físicamente; el objetivo es comenzar el muestreo a mediados de 2027. Todas las cifras de rendimiento publicadas son objetivos de diseño. \[Hecho: anuncio de Qualcomm\] Si HBF está en fase de simulación, HBC está en fase de plano de diseño. Existen informes de que Microsoft y Meta habrían realizado pedidos del acelerador de Qualcomm, pero no están confirmados. \[Inferencia: informes secundarios, sin verificar\]

El marco correcto para leer HBC no es el de 'memoria competidora de HBM', sino <strong>'la estrategia de sistema de una empresa para ejecutar inferencia de forma económica sin usar HBM'</strong>. Si tiene éxito, podría afectar al segmento de inferencia de bajo costo dentro de la demanda de HBM, pero no presenta un escenario de sustitución total de HBM. Los actores son prácticamente solo Qualcomm.

---

## 5. Complementarios, no sustitutos: la temperatura de los datos determina el lugar de cada uno

Los titulares de "HBF matará a HBM" o "HBC reemplazará a HBM" aparecen con frecuencia. La conclusión tras la verificación es que son exageraciones. Los tres son esencialmente complementarios.

El fundamento no procede de una lógica de mercado abstracta, sino de las propiedades físicas de los datos.

En la inferencia de LLM, los datos que se cargan en memoria son de dos tipos.

<strong>Pesos del modelo (datos fríos):</strong> una vez completado el entrenamiento, casi no cambian; en la inferencia solo se leen. Pueden almacenarse en memoria grande y barata aunque sea más lenta (HBF), sin que ello suponga una penalización relevante. La limitación de ciclos de escritura de la NAND tampoco es un problema cuando los datos "solo se leen".

<strong>Caché KV (datos calientes):</strong> se actualiza en cada momento a medida que avanza la conversación. Debe alojarse en la memoria más rápida disponible (HBM). Usar una memoria más lenta ralentizaría todo el sistema.

HBM y HBF, con una diferencia de latencia de unas 100 veces, no pueden ocupar físicamente el mismo puesto de "memoria de trabajo". HBF no desplaza a HBM; es el nivel inferior que almacena lo que HBM no puede contener. HBC opera en un carril completamente diferente, apuntando a la inferencia de bajo costo.

Es probable que los futuros aceleradores de IA no sean una elección entre "HBM o HBF", sino una <strong>jerarquía de tres niveles: HBM + HBF + SSD de alta velocidad</strong>. \[Inferencia: análisis de hojas de ruta tecnológicas\]

No obstante, existe competencia parcial real. Si el problema de capacidad se resuelve con HBF o con eSSD sigue siendo una disputa abierta. En el mercado de inferencia de bajo costo, los aceleradores HBC y los aceleradores HBM también se solapan en parte. Si HBF y HBC tienen éxito en ofrecer "gran capacidad a bajo costo", los clientes tendrán incentivos para comprar menos HBM caro, lo que podría generar un escenario de erosión marginal. Sin embargo, toda esa competencia es una historia que se desarrollará a partir de 2027.

---

## 6. Los hitos que hay que seguir ahora

Las tres tecnologías cruzan el umbral de la "promesa" a la "realidad" en momentos distintos.

<strong>HBM es un proceso en curso.</strong> Los próximos puntos de observación son el rendimiento de producción de HBM4, la expansión del HBM personalizado para clientes y la transición al hybrid bonding. SK Hynix, Samsung, Micron y TSMC captarán la mayor parte del valor de la memoria IA en el futuro previsible. \[Inferencia: estimaciones de cuota de mercado\]

<strong>Para HBF, los dos hitos más importantes son los siguientes.</strong> Primero, la primera muestra física real y el benchmark independiente en el segundo semestre de 2026. Hasta ahora, todas las cifras han sido simulaciones, por lo que el momento en que aparezca el chip físico será decisivo. Segundo, la decisión de adopción de NVIDIA. Si adopta HBF, el campo se consolidará rápidamente; si no lo hace, HBF quedará como una solución de nicho.

<strong>Para HBC, el primer umbral es la muestra física del Qualcomm AI250 en 2027 y su verificación independiente.</strong> La confirmación de los pedidos de Microsoft y Meta también servirá de barómetro para la expansión del ecosistema HBC.

---

## Verificación de afirmaciones exageradas

Algunas afirmaciones frecuentes en este ámbito merecen cautela.

<strong>"HBF y HBC reemplazarán a HBM":</strong> la diferencia de latencia y de función hace que la relación sea complementaria. La narrativa de sustitución es una exageración.

<strong>"16x de capacidad, 4 TB de VRAM, 6x de eficiencia energética":</strong> la mayoría de estas cifras son simulaciones internas o metas de diseño de las propias empresas, no mediciones independientes.

<strong>"HBM estará amenazado en 2026":</strong> la contribución de ingresos significativa de HBF y HBC llegará, en el mejor de los casos, en 2027-2028.

<strong>"HBC es memoria de próxima generación":</strong> error de categoría. HBC no es memoria; es la arquitectura de acelerador de Qualcomm.

Reconocer el potencial no implica aceptar los titulares de marketing. Separar las afirmaciones de marketing de los hechos verificados es el punto de partida de cualquier análisis serio.

---

_Este artículo es un análisis técnico de comprensión elaborado a partir de fuentes primarias, secundarias y terciarias públicas y de anuncios corporativos. No constituye una recomendación de inversión en ningún valor o producto específico. La mayoría de las cifras de rendimiento de HBF y HBC son afirmaciones propias de las empresas, simulaciones u objetivos de diseño, y no han sido verificadas de forma independiente. Dado que el campo evoluciona con rapidez, se recomienda contrastar con las fuentes primarias más actualizadas._

---

### Artículos relacionados

- [¿Quién pagará el consenso semiconductor de 2027?](/es/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/)
- [El IPO de CXMT y el riesgo de precios de memoria](/es/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)
- [Análisis de TechWing HBM Cube Prober](/es/post/techwing-hbm-cube-prober-big3-conditional-buy-2026-06-21/)
- [Por qué el superciclo de la IA se alarga](/es/post/ai-supercycle-extension-agent-demand-ipo-funding-memory-storage-2026-06-12/)
- [Samsung y SK Hynix representan el 90,8% de los ETF de semiconductores coreanos](/es/post/korea-semiconductor-etf-exposure-marketcap-gap-strategy-2026-06-13/)
