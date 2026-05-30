---
title: "La demanda de tokens de Goldman frente al pico de ASP de memoria de J.P. Morgan: ¿de verdad chocan las dos visiones?"
slug: "goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31"
date: 2026-05-31T11:00:00+09:00
description: "Goldman Sachs prevé que los agentes de IA multipliquen por 24 el uso de tokens hasta 2030 mientras el coste por token cae entre un 60-70% anual. J.P. Morgan prevé que el crecimiento interanual del ASP de DRAM y NAND se modere desde 2027. Si separamos ambas visiones aparentemente opuestas en P, Q y C, surge un camino coherente: el alfa rota desde el beta de memoria de 2026 hacia un stack de reducción de coste por token a partir de 2027."
categories: ["Korea Market", "Sector-Deep-Dive", "AI Infrastructure"]
tags:
  - "삼성전자"
  - "SK하이닉스"
  - "HBM"
  - "메모리 ASP"
  - "eSSD"
  - "AI 토큰"
  - "추론비용"
  - "Goldman Sachs"
  - "J.P. Morgan"
  - "AI 인프라"
  - "Research OS"
series: ["Korea Market Regime"]
draft: false
---

> Este artículo es la continuación de [Futuros de tokens de IA y coste por token](/es/post/ai-token-futures-cost-per-token-korea-semiconductor-thesis-2026-05-30/), [Análisis profundo de Samsung Electronics 2026](/es/post/kr-deep-dive-samsung-electronics-2026-04-16/), [SK Hynix: el peso pesado del HBM](/es/post/kr-deep-dive-sk-hynix-2026-04-16/) y [La infraestructura de IA de Corea tras el Q1 FY27 de Nvidia](/es/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/). Si los artículos anteriores miraban por separado el coste por token, las empresas individuales y la difusión de la infraestructura de IA, este <strong>une dos visiones distintas — Goldman sobre la demanda y J.P. Morgan sobre el precio de la memoria — en un solo marco</strong> y ordena el horizonte de inversión de 2026 a 2030.

## TL;DR

* Goldman Sachs ve <strong>una explosión del uso de tokens (24x hasta 2030) más una caída pronunciada del coste por token (60-70% anual)</strong>. J.P. Morgan ve que <strong>la tasa de crecimiento interanual (YoY) del ASP de DRAM y NAND se modera desde 2027</strong>. Como observan variables distintas, las dos visiones no chocan de frente.
* Si las combinamos, aparece un único camino: <strong>2026 es beta de ASP de memoria, 2027 es un pico (peak-out) del momentum de precios, y 2028-2030 es una rotación del alfa hacia los componentes y sistemas que reducen el coste por token</strong>.
* Por eso la conclusión de inversión no es "comprar memoria sin límite". En 2026 el beta de memoria como HBM, DRAM de servidor y eSSD es favorable, pero después hay que <strong>seleccionar dónde están los cuellos de botella</strong>: ASIC, redes de IA, óptica, líderes en HBM, eSSD, empaquetado avanzado y MLCC/FC-BGA.
* Los dos malentendidos más comunes son: (1) ver el peak-out de J.P. Morgan y concluir que "el ciclo de la infraestructura de IA ha terminado", y (2) ver la demanda de Goldman y concluir que "los precios de la memoria seguirán disparándose hasta 2030". Ambos exageran.

---

## 1. Dos gigantes, dos visiones aparentemente opuestas

Ante la misma era de la IA, dos bancos de inversión globales han pintado cuadros que parecen apuntar en direcciones contrarias.

<strong>Goldman Sachs</strong> (artículo oficial, 5 de mayo de 2026) mira el lado de la demanda. El núcleo son dos puntos.

- <strong>El uso de tokens crece 24x hasta 2030.</strong> La previsión es que el uso mensual alcance los 120 billones largos (quadrillion) de tokens en 2030; haciendo el cálculo a la inversa, eso sitúa la base de 2026 en torno a 5 quadrillion. Eso supone un crecimiento medio anual de cerca del 121% en cuatro años.
- Al mismo tiempo, <strong>el coste de inferencia por token cae un 60-70% al año.</strong> Los motores son la mejora de la eficiencia de los chips y una mejor arquitectura de los centros de datos.

![Índice reconstruido de la economía de tokens de IA de Goldman Sachs — el uso sube 24x mientras el coste por token cae 39-123x](goldman-ai-token-economics-reconstructed-index.png)

<small>Fuente: un gráfico reconstruido que simplemente indexa las cifras del artículo oficial de Goldman Sachs (2026-05-05). No es el gráfico original, sino los números originales — "24x tokens hasta 2030, coste por token con caída anual del 60-70%" — trasladados a una escala logarítmica.</small>

En el gráfico de arriba, la línea azul (uso) sube con fuerza, y las líneas naranja y verde (coste por token) bajan aún más bruscamente. Con una caída anual del 60%, el coste cuatro años después es cerca del 2,6% del nivel de 2026 (una mejora de unas 39 veces); con el 70%, cerca del 0,8% (una mejora de unas 123 veces).

En cambio, el material de <strong>J.P. Morgan</strong> mira el precio. El cuadro es que el ASP de DRAM y NAND sube con fuerza en 2026 pero que, <strong>desde finales de 2026 hasta principios de 2027, la tasa de crecimiento interanual se desacelera con rapidez.</strong>

![Variación interanual del ASP de DRAM y NAND de J.P. Morgan — pico en 2026 y desaceleración desde 2027](jpm-dram-nand-asp-yoy-peakout-chart.png)

<small>Fuente: imagen subida en la sesión (DRAM de WSTS / J.P. Morgan estimates, NAND de Gartner / J.P. Morgan estimates). Cifras detalladas como FY26 DRAM +53% y NAND +30%, FY27 DRAM +1% y NAND -6% se basan en un resumen secundario; la tabla original está sin verificar.</small>

En la superficie, "la demanda explota" (Goldman) y "las subidas de precio de la memoria se frenan" (J.P. Morgan) parecen chocar. Pero, mirando de cerca, las dos visiones <strong>hablan de cosas distintas.</strong>

---

## 2. Por qué no es un choque — separar P, Q y C

El beneficio de una empresa de memoria se descompone en una simple multiplicación.

> Ingresos = envíos (Q) × precio medio de venta (P), y la economía de tokens = uso (Q) × coste por token (C).

Con esta óptica, queda claro que las dos visiones observan variables distintas.

| Dimensión | Goldman Sachs | J.P. Morgan |
|---|---|---|
| Variable observada | Uso de tokens (Q), coste por token (C) | Variación YoY del ASP de DRAM/NAND (momentum de P) |
| Mensaje central | El uso de IA explota a largo plazo, el coste por token se desploma | La tasa de subida del precio de la memoria se modera desde 2027 |
| Horizonte temporal | 2026-2030 | Finales de 2026 a principios de 2027 |

Aquí hay una trampa que conviene señalar. <strong>El eje vertical del gráfico de J.P. Morgan no es el nivel absoluto del precio, sino la "tasa de crecimiento interanual (YoY %)".</strong> Ambas cosas son totalmente distintas.

Pongamos un ejemplo.

| Momento | Índice de ASP | YoY |
|---|---:|---:|
| 4T25 | 100 | – |
| 4T26 | 300 | +200% |
| 4T27 | 315 | +5% |

De 4T26 a 4T27 el índice de precios <strong>todavía sube</strong>, de 300 a 315. Sin embargo, la tasa de crecimiento interanual se desploma del +200% al +5%. Es decir, el "peak-out" de 2027 de J.P. Morgan puede no significar que los precios se hundan, sino que <strong>el ritmo de subida se ralentiza.</strong> El mercado bursátil suele descontar esta <strong>dirección de la tasa de crecimiento</strong> antes que el "beneficio récord" en sí. Por eso la cotización puede enfriarse primero, justo cuando el beneficio está en su máximo.

En resumen, Goldman observa <strong>Q (uso) y C (coste)</strong>, mientras que J.P. Morgan observa <strong>el ritmo de P (precio).</strong> Como son variables distintas, ambas pueden acertar al mismo tiempo.

---

## 3. El coste total de inferencia puede incluso bajar

Aquí surge una conclusión contraintuitiva. Aunque el uso crezca 24x, si el coste por token cae un 60-70% al año, entonces <strong>la carga total del coste de inferencia podría ser incluso menor que en 2026.</strong>

Es aritmética simple. Suponiendo la misma composición de tokens y la misma complejidad de modelo, el coste total en 2030 es el índice de uso × el índice de coste por token.

- Con una caída anual del 60%: 24 × 2,6% ≈ <strong>61% de 2026</strong>
- Con una caída anual del 70%: 24 × 0,8% ≈ <strong>19% de 2026</strong>

![Carga total del coste de inferencia, sensibilidad simple — incluso 24x de uso queda absorbido por la fuerte caída del coste por token](goldman-total-inference-cost-burden-index.png)

<small>Es un cálculo de sensibilidad muy simplificado. No refleja la composición de tokens, el tamaño del modelo, la longitud del contexto, el aumento de tokens de razonamiento (reasoning), la multimodalidad, el procesamiento redundante, las restricciones de latencia ni los cuellos de botella de ancho de banda de memoria. En la práctica estos factores podrían empujar el coste de nuevo hacia arriba.</small>

Este gráfico es el corazón de la lógica de Goldman. <strong>Quien reduce el coste por token acaba ganando el dinero.</strong> Más que la subida del uso en sí, es la reducción de coste que hace ese uso asumible la que mantiene vivo el flujo de caja del sector. Dicho esto, como advierte la nota, si la longitud del contexto o los tokens de razonamiento suben rápido, la curva de coste real puede bajar menos de lo que sugiere este gráfico.

---

## 4. Por eso cambia el horizonte temporal

Si combinamos las dos visiones, el siguiente camino es lógicamente coherente.

| Periodo | Qué ocurre | Dónde es favorable |
|---|---|---|
| <strong>2026</strong> | El uso de agentes se dispara → la asignación de HBM, DRAM de servidor, eSSD y NAND se tensiona → el ASP de DRAM y NAND se dispara | El beta de ASP de memoria funciona con fuerza |
| <strong>2027</strong> | Una base más alta más algunas ampliaciones de oferta y contratos a largo plazo (LTA) moderan la tasa YoY del ASP. La memoria B2B de IA se mantiene firme; la memoria B2C de consumo encuentra resistencia de precio | Las cotizaciones descuentan "tasa de crecimiento que se modera" antes que "beneficio máximo". Empieza la divergencia por segmentos |
| <strong>2028-2030</strong> | El uso sigue subiendo, pero la caída del coste por token lo absorbe | El alfa rota del beta de memoria genérica hacia el <strong>stack de reducción de coste por token</strong> |

El mensaje central es uno. Desde 2027, "cuánto más suben los precios de DRAM y NAND" importa menos que <strong>"qué componentes y sistemas reducen el coste por token."</strong>

---

## 5. Ejemplos de ideas de inversión (puntos de observación, no recomendaciones)

A continuación no hay recomendaciones de valores, sino <strong>ejemplos</strong> de "dónde mirar primero" a lo largo del horizonte anterior. Los valores de IA y memoria ya se han revalorizado deprisa, así que esto no es una llamada a comprar ahora mismo, sino un mapa para cuando se cumplan las condiciones.

### Ejemplo 1 — Beta de ASP de memoria 2026

La fase en la que la asignación de HBM, DRAM de servidor y eSSD se tensiona y los precios de DRAM y NAND se disparan. Las grandes capitalizaciones de memoria como <strong>SK Hynix, Samsung Electronics y Micron</strong> se benefician directamente. El contraargumento es que, una vez que empieza la desaceleración de la tasa de crecimiento en 2027, la cotización puede sufrir compresión de múltiplos primero, aunque el beneficio sea alto.

### Ejemplo 2 — Stack de reducción de coste por token

El verdadero corazón de la lógica de Goldman no es la subida del uso, sino la <strong>caída del coste por token.</strong> Los clientes pagarán más por chips y sistemas que reduzcan su coste por token. Los <strong>ASIC a medida, las redes de IA y la óptica, y los líderes en HBM</strong> encajan mejor aquí. (Los cuellos de botella de interconexión, sustrato y energía vistos en el [read-through de Marvell](/es/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/) son ese mismo hilo.)

### Ejemplo 3 — eSSD / NAND empresarial

La inferencia de agentes exige mucho más almacenamiento de recuperación (RAG), registros, contexto, KV cache y checkpoints que el simple entrenamiento. Si es cierto que los servidores de IA usan unas 3 veces la capacidad de SSD de un servidor común, entonces el NAND puede reclasificarse no como un activo de ciclo genérico, sino como un <strong>cuello de botella de almacenamiento de IA.</strong> El contraargumento es la posibilidad de que la resistencia de precio de los SSD de consumo diluya la fortaleza empresarial.

### Ejemplo 4 — Empaquetado avanzado / MLCC / FC-BGA

Si la previsión de tokens de Goldman para 2030 acierta, la complejidad de la arquitectura de servidores y racks no deja de subir. No solo crecen las GPU, los ASIC y el HBM; también crece la demanda de área de sustrato, estabilización de la alimentación, condensadores de desacoplo y calidad de señal de alta velocidad. Proveedores de MLCC y FC-BGA de alta especificación como <strong>Samsung Electro-Mechanics</strong> encajan aquí.

### Distintos peak-outs por segmento

Lo que importa no es "la memoria en su conjunto", sino las diferencias por segmento. La lógica del peak-out de J.P. Morgan no se aplica por igual a toda la memoria.

| Segmento | Probabilidad de que aplique el peak-out | Tensión con la demanda a largo plazo |
|---|---|---|
| HBM | Baja-Media | Alta (la demanda sigue reforzando el muro de ancho de banda) |
| DRAM de servidor | Media | Media |
| eSSD / NAND empresarial | Media | Alta (posible demanda estructural) |
| DRAM móvil | Alta | Baja (resistencia de precio de consumo rápida) |
| DRAM/NAND genérica | Alta | Baja (la lógica del peak-out aplica mejor) |

> Condición común: los ejemplos anteriores necesitan más que "sobrevendido" o "porque es IA". Un candidato debe estar donde <strong>los pedidos reales, los precios de contrato y las estimaciones de beneficio suben de nuevo, y donde se confirman los cuellos de botella y las barreras de entrada.</strong>

---

## 6. Los dos malentendidos más comunes

En esta fase, el mercado es propenso a dos errores que apuntan en direcciones opuestas.

<strong>Malentendido 1 — "J.P. Morgan dice peak-out, así que el ciclo de la infraestructura de IA ha terminado."</strong> No. Un peak-out es una desaceleración de la <strong>tasa de crecimiento</strong> del precio, no un hundimiento del <strong>nivel</strong> del precio. Y aplica mejor a la memoria genérica y menos a cuellos de botella como HBM, eSSD, ASIC y empaquetado.

<strong>Malentendido 2 — "Goldman dice 24x tokens, así que los precios de DRAM y NAND también seguirán disparándose hasta 2030."</strong> Esto también exagera. Goldman dice uso explosivo y <strong>caída pronunciada del coste por token</strong> a la vez. Si el coste baja rápido, la tasa de crecimiento interanual de los precios de la memoria puede moderarse aunque el uso suba.

La lectura correcta está en medio. <strong>Un superciclo de memoria en 2026, un peak-out del momentum de precios en 2027, y una expansión a largo plazo del stack de reducción de coste por token en 2028-2030.</strong>

---

## 7. Comentario del gestor de fondos

Las dos visiones no son enemigas, sino dos ejes de un mismo cuadro. Goldman habla de "cuánto, y cuán barato, llegaremos a usar la IA"; J.P. Morgan habla de "hasta cuándo seguirán subiendo rápido los precios de la memoria en ese proceso". La tarea del inversor no es elegir una de las dos, sino <strong>no perderse los puntos de inflexión del horizonte temporal.</strong>

Las dos elecciones más peligrosas son estas.

* <strong>Tirar toda la infraestructura de IA al ver la sola palabra peak-out</strong> — el error de regalar incluso a los ganadores con cuellos de botella a precio de saldo.
* <strong>Perseguir la memoria genérica hasta el final solo por la demanda de tokens</strong> — el error de encajar de frente la compresión de múltiplos en la fase en que la tasa de subida del precio se frena.

Las señales que conviene vigilar ahora, dicho de forma sencilla, son estas.

| Qué observas | Refuerza a Goldman (demanda) | Refuerza a J.P. Morgan (peak-out) |
|---|---|---|
| Uso de tokens | Alto crecimiento sostenido | La tasa de crecimiento se modera |
| Coste por token | Sigue cayendo más del 60% al año | El ritmo de caída se modera, sube el coste por latencia |
| Contratos a largo plazo de HBM | Precios mantenidos o al alza | Renegociación, aplazamiento de volúmenes |
| Precio de contrato de DRAM de servidor | Subida adicional | La tasa de subida se modera, descuentos al contado |
| SSD empresarial | Se amplían los contratos a largo plazo con CSP | La resistencia de precio del SSD de consumo se contagia |

En resumen, <strong>reconocer el beta de memoria en 2026 y, desde 2027, prepararse para desplazar el peso hacia los cuellos de botella que reducen el coste por token</strong> es la postura más razonable disponible ahora. Ni perseguir la memoria hasta el final, ni tirarlo todo por miedo al peak-out.

<small>Este artículo es un análisis reconstruido a partir del artículo oficial de Goldman Sachs (2026-05-05), gráficos y resúmenes secundarios relacionados con J.P. Morgan, y la previsión oficial de TrendForce. No se pudieron verificar el texto completo del informe original de J.P. Morgan, sus tablas trimestrales de ASP ni su detalle por segmentos, y los nombres de empresas son ejemplos que ilustran el flujo del análisis, no recomendaciones de inversión. Las decisiones de inversión y su responsabilidad recaen en el propio inversor.</small>
