---
title: "¿Superará la demanda de memoria para IA las expectativas? Las probabilidades de sobrecrecimiento según los escenarios de demanda y el mapa de oferta"
slug: "ai-memory-demand-exceed-expectations-supply-map-2026-07-18"
date: 2026-07-18T18:00:00+09:00
description: "Es probable que la demanda de memoria para IA cumpla o supere las altas expectativas actuales, pero un gran exceso al alza aún no es el escenario base. Ponderamos por probabilidad la demanda en escenarios base, alcista y bajista (45/35/20), presentamos seis variables al alza y seis riesgos a la baja, y conectamos los cuellos de botella de oferta por capas de memoria, los mapas de expansión de Samsung, SK Hynix y Micron, y el fondo del argumento de expansión del presidente Chey."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["Memoria IA", "HBM", "DRAM", "Samsung Electronics", "SK Hynix", "Micron", "SOCAMM2", "Oferta-Demanda de Memoria", "Expansión de capacidad", "Ciclo de memoria"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexto
> Este artículo aborda de frente <strong>el tramo de oferta y demanda de 2026-2028</strong> que queda entre el largo plazo hasta 2030 tratado en [la investigación profunda de oferta-demanda de HBM 2030](/es/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/) y la valoración calculada en [el valor razonable de los semiconductores](/es/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/). Conviene leerlo junto con [el verdadero debate en semiconductores](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/) y [la localización de memoria en China y Corea](/es/post/china-memory-localization-exposure-samsung-hynix-micron-2026-07-18/). Los hubs relacionados son el [hub de IA y HBM](/es/page/korea-semiconductor-hbm-kospi-hub/) y el [hub de Exclusive Analysis](/es/page/exclusive-analysis-hub/).

## TL;DR

* <strong>Es probable que la demanda de memoria para IA cumpla o supere las altas expectativas actuales.</strong> Sin embargo, superarlas por un margen amplio todavía no es el escenario base.
* El juicio de probabilidad es este: cumplir con las expectativas <strong>45%</strong>, superarlas de forma significativa <strong>35%</strong>, quedar por debajo <strong>20%</strong>. La probabilidad de que el crecimiento fuerte continúe es de ~<strong>80%</strong>, y la probabilidad de superar ampliamente las expectativas actuales es de ~<strong>35%</strong>. [Inferencia: juicio de probabilidad propio]
* La clave del crecimiento por encima de lo esperado no es que "se vendan muchos servidores de IA". <strong>El volumen de envíos de aceleradores y la capacidad de memoria por acelerador deben crecer a la vez más de lo previsto.</strong>
* El verdadero alfa asimétrico no es el crecimiento del HBM en sí mismo. Eso ya lo sabe el mercado. El alfa está en <strong>si la demanda se propaga del HBM hacia la DDR de servidor, SOCAMM y eSSD, y si su duración se extiende más allá de 2028</strong>.
* La tesis de expansión de producción del presidente Chey Tae-won no es una declaración de recorte de precios a corto plazo, sino un mensaje de <strong>ampliación que preserva el mercado y de toma anticipada de posición en la cadena de suministro para después de 2028</strong>. La previsión de shortage para 2026-2027 no se ha visto afectada, y el verdadero riesgo de sobreoferta está en 2028-2030, cuando las nuevas fábricas alcancen a la vez un rendimiento normalizado. [Alcance]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Marco clave</div>
  <div class="thesis-callout__body">
    La memoria para IA crece con fuerza. Pero la condición para la próxima subida de la acción no es el aumento del beneficio de 2027, sino la evidencia de que el beneficio de 2028 no se quiebra. Lo que hay que observar ahora no es el crecimiento del HBM, sino si la demanda se propaga hacia la DDR de servidor, SOCAMM y eSSD, y si se sostiene más allá de 2028.
  </div>
</div>

---

## 1. Lo que el mercado ya espera

Para hablar de un crecimiento por encima de las expectativas, primero hay que saber qué espera ya el mercado. El nivel actual de expectativas ya es alto. [Hecho: síntesis de previsiones públicas]

- Demanda de HBM en 2026: ~2x
- Envíos de servidores de IA en 2026: aumento del 20% o más
- Demanda de bit HBM en 2027: +50-65%
- Proporción de obleas asignadas a HBM en 2027: ~30%
- Demanda total de bit DRAM en 2027: ~+20%

TrendForce prevé que el AI ASIC de 2026, junto con el Rubin Ultra y el AI ASIC de 2027, impulsen en conjunto la demanda de HBM. La capacidad de HBM por AI ASIC también sigue la tendencia de subir de los 96GB/192GB actuales a 216GB/288GB. [Hecho: TrendForce]

Por eso, con solo decir "se venden muchos servidores de IA" no basta para hablar de un crecimiento por encima de lo esperado. <strong>El volumen de envíos de aceleradores y la capacidad de memoria por acelerador deben crecer a la vez más de lo previsto.</strong>

---

## 2. El modelo de demanda base

Es más preciso ver la demanda de memoria con la siguiente fórmula.

```text
Demanda de bit HBM       = Envíos de aceleradores de IA × Stacks de HBM por acelerador × Capacidad por stack
Demanda de DRAM servidor = Envíos de servidores × Capacidad de DRAM por servidor
Demanda de LPDDR         = Envíos de servidores móviles/IA × Capacidad de LPDDR por dispositivo
```

### El escenario base de 2027

A continuación se presenta un modelo propio que conecta las previsiones públicas con la hoja de ruta de productos actual. No es un consenso oficial, sino una estimación. [Inferencia: modelo propio]

| Categoría | Supuesto de participación en bit DRAM | Aumento de dispositivos/sistemas | Aumento de capacidad | Aumento de demanda de bit |
|---|---:|---:|---:|---:|
| HBM | 18% | Aceleradores de IA +35% | Capacidad por acelerador +15% | ~+55% |
| DDR5 de servidor y SOCAMM | 32% | Servidores y CPU +12% | Capacidad por servidor +10% | ~+23% |
| Móvil, PC y automotriz | 50% | Dispositivos +2% | Capacidad por dispositivo +5% | ~+7% |
| <strong>Total ponderado</strong> | 100% | | | <strong>~+21%</strong> |

Si los envíos de aceleradores aumentan 35% y la capacidad de HBM aumenta 15%, el bit de HBM es <strong>1,35 × 1,15 - 1 = +55,3%</strong>. Esta estructura multiplicativa es la razón por la que, incluso con un aumento de solo 20% en los envíos de servidores, la demanda de HBM puede crecer más del 50%.

Micron prevé que el crecimiento de los envíos de bit DRAM de la industria en 2026 sea de un low-to-mid 20% y que el shortage se prolongue más allá de 2027. TrendForce también estima que la demanda de HBM en 2026 aumentará ~2x y que la proporción de obleas asignadas a HBM subirá del 22% en 2026 al ~30% en 2027. [Hecho: Micron y TrendForce]

---

## 3. Tres escenarios de demanda

Las probabilidades no son estadísticas, sino un juicio subjetivo que refleja los pedidos, el CAPEX y la hoja de ruta de productos actuales.

| Escenario | Probabilidad | Bit DRAM 2027 | Bit DRAM 2028 | Demanda de HBM | Momento de alivio de oferta |
|---|---:|---:|---:|---:|---|
| Base | <strong>45%</strong> | +20-23% | +17-21% | 2027 +50-65% | DRAM genérica 2H27, HBM 2028 |
| Demanda por encima | <strong>35%</strong> | +28-32% | +25-30% | 2027 +70-85% | DRAM genérica 2028, HBM 2029-30 |
| Demanda por debajo | <strong>20%</strong> | +12-17% | +8-14% | 2027 +30-40% | DRAM genérica 1H27, HBM 2H27-28 |

[Inferencia: estimación de escenarios]

Si se suma el 45% de probabilidad de cumplir con las expectativas y el 35% de probabilidad de superarlas de forma significativa, <strong>la probabilidad de que el crecimiento fuerte continúe es de ~80%</strong>. Sin embargo, la probabilidad de superar ampliamente las expectativas actuales es de ~35%, por lo que el crecimiento por encima de lo esperado todavía no es el escenario base.

---

## 4. Seis variables al alza que elevan el crecimiento por encima de lo esperado

### ① El crecimiento conjunto de GPU y ASIC (el alza más fuerte)

El mercado ve al ASIC como un sustituto de NVIDIA, pero para los fabricantes de memoria <strong>ambos son clientes</strong>. Aunque el TPU y el Trainium puedan reducir la cuota de las GPU, de todos modos consumen HBM o DRAM de servidor de alta capacidad.

```text
Aumento de GPU NVIDIA + aumento de Google TPU, AWS Trainium y Meta ASIC
→ Diversificación de clientes de HBM
→ Expansión de la demanda total de bit HBM
```

Si a esto se suman el HBM4E de 16 capas y el HBM a medida, el +55% calculado antes podría superarse hasta llegar a +70%. El beneficio más directo es para <strong>SK Hynix > Samsung Electronics > Micron</strong>. Samsung cuenta con la opción adicional del HBM a medida para clientes de ASIC y su propia base die de foundry. [Inferencia: estructura de exposición]

### ② El cuello de botella se propaga del HBM a toda la jerarquía de memoria

Un servidor de IA no funciona solo con HBM.

- GPU y ASIC: HBM
- CPU y memoria host: DDR5 y SOCAMM2
- Caché y almacenamiento de datos: Enterprise SSD
- Red e inferencia de bajo costo: GDDR y LPDDR

En julio de 2026, SK Hynix presentó no solo el HBM sino también SOCAMM2, DDR5, GDDR7, LPDDR y eSSD como un único portafolio de memoria para IA. [Hecho: SK Hynix] <strong>Aunque las expectativas de HBM se desvíen un poco, la SOCAMM, la DDR de servidor y el eSSD pueden crecer por encima de lo esperado en su lugar.</strong> Por eso, la probabilidad de un crecimiento por encima de lo esperado con base en el conjunto de la memoria para IA se estima en ~45%, más alta que la del HBM en solitario. [Inferencia: diversificación de portafolio]

### ③ SOCAMM2 forma una nueva capa de demanda

El SOCAMM2 no es una simple conversión que traslada la LPDDR móvil existente al servidor. Es <strong>un segmento nuevo</strong> que transforma la memoria de CPU y host de los racks de IA hacia una estructura de bajo consumo y alta capacidad. SK Hynix inició la producción en masa del SOCAMM2 de 192GB, y a medida que se expanda su adopción en CPU de servidor y racks de IA, la demanda de LPDDR5X aumentará de forma independiente al HBM. [Hecho: SOCAMM2 de SK Hynix]

### ④ La IA agéntica estimula a la vez la DRAM de servidor y el eSSD

El entrenamiento gira en torno al HBM, pero la inferencia de agentes usa varias capas a la vez.

- HBM: cómputo del modelo
- DDR5 y SOCAMM: memoria de CPU y sistema
- eSSD: base de datos vectorial, KV cache, almacenamiento de datos
- Memoria de buffer de red

Cuando un agente mantiene estado y contexto durante periodos largos, aumenta no solo el número de tokens sino también la capacidad de memoria por sistema. En ese caso, la DDR de servidor y el eSSD pueden resultar más fuertes de lo esperado, incluso más que el HBM. [Inferencia: análisis de carga de trabajo]

### ⑤ La estrategia china de chips de bajo rendimiento en realidad aumenta el volumen de memoria

Si China conecta más chips de bajo rendimiento en lugar de GPU de alto rendimiento, la misma cantidad de cómputo requiere más chips, servidores y memoria. Es probable que el beneficio directo se concentre no tanto en el HBM de gama más alta, sino en <strong>DDR5, LPDDR5X, GDDR7, HBM de especificación media y eSSD</strong>. El crecimiento de la IA china puede reducir el mix de HBM, pero es un factor al alza para la demanda total de bit DRAM. [Inferencia: arquitectura china]

### ⑥ Cuando el aumento del uso es más rápido que la ganancia de eficiencia

La demanda total de memoria es `carga de trabajo total × uso de memoria por tarea`. Incluso si el uso por tarea cae 40%, si el uso de IA se duplica, <strong>2,0 × 0,6 - 1 = +20%</strong>. La variable más importante ahora mismo no es la velocidad de mejora de la eficiencia del modelo, sino <strong>la elasticidad del uso de tokens y agentes frente a la caída de precios</strong>. Es la condición bajo la cual la eficiencia se convierte en un factor de expansión del mercado, y no de caída de la demanda. [Inferencia: efecto Jevons]

---

## 5. Seis riesgos de quedar por debajo de las expectativas

### ① El fracaso en verificar el ROI del CAPEX de IA (la baja más grande)

Si la inversión en centros de datos no se traduce en ingresos y flujo de caja de IA, los hyperscalers podrían reducir sus pedidos en 2027-2028. El momento particularmente riesgoso es 2028, cuando la oferta realmente aumenta.

```text
Desaceleración del CAPEX de IA + puesta en marcha de Samsung P5, Micron ID2 y SK P&T7
→ Caída simultánea del ASP de HBM y del precio de la DRAM genérica
```

### ② La mejora de la eficiencia de inferencia supera al aumento del uso

La cuantización, el MoE, la compresión y reutilización de KV cache, los modelos pequeños especializados, la jerarquización de memoria y el speculative decoding reducen el requerimiento de memoria por acelerador. Si el uso por tarea cae 60% y la carga de trabajo aumenta 30%, <strong>1,3 × 0,4 - 1 = -48%</strong>. En este caso, aunque el uso de tokens aumente, la nueva demanda de HBM y de servidores queda por debajo de las expectativas. [Inferencia: escenario de eficiencia dominante]

### ③ El aumento de la utilización de aceleradores y el reciclaje de cómputo usado

Los centros de datos de IA se construyen rápidamente en la actualidad y la optimización de la utilización todavía no es suficiente. Si mejoran la programación (scheduling) y el comercio de cómputo entre nubes, la oferta efectiva de cómputo aumenta incluso sin nuevas GPU. Esto no elimina la demanda, pero retrasa el momento de instalación de nuevos servidores.

### ④ El cuello de botella de energía, transmisión y refrigeración

Aunque existan pedidos de chips y memoria, si no se conecta la energía, la instalación se retrasa. Esto se parece más a un <strong>aplazamiento de la demanda</strong> que a su desaparición, pero para los fabricantes de memoria se manifiesta como aumento de inventario y ajuste de precios.

### ⑤ La destrucción de demanda de PC y smartphones

Si el precio de la memoria sube demasiado, el precio del producto terminado sube y las ventas de dispositivos caen. Es la razón directa por la que el presidente Chey Tae-won defendió la expansión de la oferta. El orden de magnitud del impacto es <strong>LPDDR móvil > DDR de PC > DDR de servidor > HBM</strong>. Samsung Electronics es la más sensible en términos de volumen absoluto, mientras que SK Hynix, al tener un mix de HBM más alto, es relativamente más defensiva.

### ⑥ El aumento de la oferta china

Si CXMT expande rápidamente la DDR5 y la LPDDR5X, el precio de la DRAM genérica se presiona antes que el del HBM. El orden del impacto es <strong>DDR4/LPDDR4X > DDR5/LPDDR5X > GDDR > SOCAMM > HBM</strong>. Aunque la demanda de HBM se mantenga, el beneficio de la DRAM genérica podría desacelerarse primero.

---

## 6. Cuándo se destrabará realmente la oferta: la verdadera naturaleza de la tesis de expansión de Chey Tae-won

Aunque la demanda sea fuerte, la acción no necesariamente sube. La clave está en la oferta y el precio. Aquí es donde importa la declaración de expansión de producción del presidente Chey Tae-won.

### La definición precisa de "alivio"

El `alivio de la oferta en 2028` del que hablan varios análisis previos <strong>no significa una caída de precios ni el inicio de una sobreoferta</strong>. La definición precisa es esta.

- El plazo de entrega (lead time) se acorta
- Aumenta el volumen de asignación a clientes
- La tasa de aumento del precio de contrato se desacelera
- La tasa de crecimiento de la oferta se acerca a la de la demanda

### La lógica de Chey Tae-won es una expansión que preserva el mercado

La lógica del presidente Chey no es una guerra de precios, sino la preservación del mercado.

```text
Fuerte subida del precio de la memoria
→ Aumento del precio de PC y smartphones
→ Caída de la demanda de productos terminados
→ Reducción del volumen del mercado de memoria
→ Entrada de chips propios de clientes, memoria alternativa y nuevos proveedores
→ A largo plazo, deterioro del valor de mercado de las tres compañías existentes
```

De hecho, Omdia proyectó que, por efecto del aumento del precio de la memoria entre otros factores, los envíos de PC caerán 12% y los de smartphones 7% en 2026. [Hecho: Omdia] El argumento de que, si el precio sube demasiado tiempo, los fabricantes de memoria también terminan enfrentando una caída de volumen, es razonable.

Sin embargo, hay que separar dos afirmaciones. Que <strong>el shortage de 2027 pueda ser más severo que el de 2026</strong> es un hecho, y que <strong>haya que construir nuevas fábricas en EE. UU.</strong> es una inferencia. El CEO de SK Hynix, Kwak Noh-jung, también declaró que la demanda podría superar la capacidad de oferta incluso más allá de 2030, y Omdia sitúa un alivio de oferta significativo a partir de fines de 2027. [Hecho: CEO de SK Hynix y Omdia]

### El supuesto de la tasa de crecimiento de la oferta

Al convertir el calendario de puesta en marcha por sitio en oferta efectiva de bits, el resultado aproximado es este. [Inferencia: conversión propia]

| Año | Aumento estimado de oferta de bit DRAM | Base principal |
|---|---:|---|
| 2026 | +20-24% | Miniaturización de proceso, M15X, Pyeongtaek, Micron 1γ |
| 2027 | +22-26% | Yongin Fab 1 en etapa inicial, Idaho ID1, Tongluo |
| 2028 | +25-30% | Samsung P5, Micron ID2, SK P&T7 e Indiana |

En el escenario de demanda base, la tasa de crecimiento de la oferta en 2028 empieza a superar a la de la demanda por ~5-9pp. Pero si se retrasan el rendimiento (yield) de las nuevas fábricas y la certificación de clientes, esa diferencia desaparece. <strong>Hasta 2027 es posible un tramo de "se amplió la producción y aun así el precio sigue alto".</strong> Esto se debe a que las nuevas obleas de DRAM son absorbidas primero por el alto consumo de obleas del HBM. [Inferencia]

---

## 7. Las capas de memoria compiten por la misma oblea

Este es el núcleo físico del asunto. El HBM, la DDR, la LPDDR y la GDDR <strong>usan de forma competitiva la misma capacidad de obleas de DRAM de vanguardia</strong>. El NAND tiene un proceso y una fábrica separados.

```text
Oblea DRAM de vanguardia ─┬─ Die núcleo de HBM ┐
                          ├─ DDR5 de servidor  │
                          ├─ LPDDR5X/SOCAMM2   ├─ (HBM) TSV, apilado, empaquetado, test ─ HBM4/4E terminado
                          └─ GDDR7             │
Proceso lógico de vanguardia ──── Die base de HBM4 ┘
Fab de oblea NAND ──── Enterprise SSD (línea separada)
```

Micron explicó que, para el mismo número de bits, el HBM3E consume ~<strong>3x</strong> más obleas que la DDR5, y que esta proporción podría subir aún más con el HBM4. SK Hynix también confirmó que, debido a que el TSV agranda el área del die y aumenta la complejidad de rendimiento (yield) y empaquetado, el HBM requiere más obleas que la DRAM genérica. [Hecho: Micron y SK Hynix]

### El impacto en oferta y precio por capa de memoria

| Capa de memoria | Demanda principal | Cuello de botella de oferta | Orden del efecto de expansión | Defensa de precio |
|---|---|---|---|---|
| HBM4/HBM4E | GPU y ASIC de IA | DRAM de vanguardia, base die, TSV, apilado, certificación | El más tardío | La más alta |
| SOCAMM2 | Memoria de CPU de servidor de IA | LPDDR5X 1c, certificación de módulo y servidor | Medio | Alta |
| DDR5 de servidor | CPU y sistemas de servidor de IA | Oblea DRAM de vanguardia | Más rápido que el HBM | Media-alta |
| LPDDR5X móvil | Smartphones e IA on-device | DRAM de vanguardia, elasticidad móvil | Rápido | Media |
| DDR4/LPDDR4X | PC, móvil e industrial heredados (legacy) | Reducción de producción de las tres compañías | Escaso, independientemente de la expansión | Polarizada |
| GDDR7 | GPU y aceleradores de IA de bajo costo | DRAM de vanguardia, certificación de GPU | Medio | Media-alta |
| NAND/eSSD | Almacenamiento de datos de IA y KV cache | Oblea NAND, controlador | Separado de la DRAM | Media |

Hay un giro interesante. Según un análisis de TrendForce, en el primer trimestre de 2026 los ingresos y el margen por oblea del RDIMM DDR5 de 64GB superaron a los del HBM. Producir solo HBM no siempre es lo óptimo, y si el precio sube lo suficiente, surge el incentivo para que los fabricantes devuelvan obleas a la DDR5. <strong>El primer mecanismo para bajar los precios podría ser la normalización de la asignación de obleas existente, más que las nuevas fábricas.</strong> [Inferencia: lógica de asignación de obleas]

---

## 8. El mapa de expansión por compañía y sitio

Lo esencial no es el monto anunciado de la expansión, sino <strong>cuándo, dónde y con qué producto aumenta la capacidad pura de obleas de DRAM</strong>. [Hecho: anuncios y divulgaciones de cada compañía]

| Compañía y sitio | Rol | Calendario | Producto de impacto directo | Interpretación de inversión |
|---|---|---:|---|---|
| SK Cheongju M15X | Front-end de DRAM de vanguardia | Ramp-up 2026 | Core HBM, DDR5, LPDDR | El aumento de volumen más rápido |
| SK Cheongju M15 | Ampliación de capacidad de TSV | En curso | HBM | Se combina con M15X |
| SK Cheongju P&T7 | WLP y test de oblea | WT 2027.10, WLP 2028.2 | Empaquetado de HBM | Alivio del cuello de botella en 2028 |
| SK Yongin Fab 1 | Nueva fábrica de obleas | Finalización prevista 2027.5 | DRAM de vanguardia (estimado) | La producción en masa llega después de la finalización |
| SK Indiana | Empaquetado avanzado de HBM | 2H 2028 | HBM de próxima generación | No es expansión de obleas |
| SK Cheongju M17 | Front-end de NAND | No divulgado | NAND y eSSD | Independiente del HBM |
| Samsung Pyeongtaek existente | DRAM 1c y HBM4 | Producción en masa actual | HBM4 y DDR5 | Meta de triplicar los ingresos de HBM en 2026 |
| Samsung Pyeongtaek P5 | Nuevo núcleo de HBM | Puesta en marcha prevista 2028 | HBM y DRAM de vanguardia | Expansión de oferta desde 2028 |
| Samsung Onyang y Cheonan | Empaquetado y test de HBM | No divulgado | HBM4/4E | Plan de 5 líneas en Onyang |
| Micron Hiroshima | DRAM EUV 1γ | Ya en ramp | HBM4E, DDR5, LPDDR | Mejora de costo de vanguardia |
| Micron Taiwán/Tongluo | Front-end de DRAM | Mediados de 2027 | HBM, DDR, LPDDR | Primer volumen nuevo significativo |
| Micron Singapur | Empaquetado de HBM | 1H 2027 | HBM | Alivio del cuello de botella de empaquetado |
| Micron Idaho ID1/ID2 | Nueva fábrica de DRAM | Primer wafer: mediados de 2027 / fines de 2028 | DRAM de vanguardia | Prima de cadena de suministro estadounidense |
| Micron Virginia | DRAM heredada (legacy) | 2026 | DDR4 | Longevidad industrial y de defensa |

SK P&T7 es una instalación exclusiva de WLP y test de HBM de ~19 billones KRW, e Indiana es una instalación de empaquetado de HBM de 3.870 millones USD. Samsung designó Pyeongtaek P5 como su base de HBM para 2028 y anunció 5 líneas en Onyang y la modernización de Cheonan. Sin embargo, los 140 billones KRW de la región de Chungcheong son <strong>el monto total del grupo</strong>, que incluye pantallas, baterías y sustratos, así que no debe interpretarse como el monto de inversión en HBM. [Hecho: anuncios de cada compañía]

### Cuándo se destraba realmente la oferta

| Periodo | Cambio de oferta | Impacto en el precio |
|---|---|---|
| 2026 | Conversión de fábricas existentes, ramp de nodos de vanguardia en M15X, Pyeongtaek y Micron | El aumento de HBM sigue erosionando la oferta de DDR |
| 2027 | Yongin Fab 1, Idaho ID1, Tongluo, empaquetado de Singapur | Posible normalización parcial de DDR5 y LPDDR |
| 2028 | Samsung P5, SK P&T7 e Indiana, Micron ID2 | Comienza el alivio del shortage de HBM |
| 2029-2030 | Rendimiento normalizado de las nuevas fábricas, inversión adicional en EE. UU. y Honam | Riesgo de sobreoferta si se desacelera la demanda de IA |

<strong>La previsión de shortage de memoria para 2026-2027 no se ha visto afectada.</strong> El verdadero riesgo de sobreoferta está en 2028-2030, cuando las nuevas fábricas alcancen a la vez un rendimiento normalizado.

---

## 9. Qué hay que confirmar

Estos son los indicadores clave para distinguir entre el alza y la baja de la demanda.

| Indicador | Señal de demanda por encima | Señal de demanda por debajo |
|---|---|---|
| Envíos de servidores de IA | YoY +25% o más | +15% o menos |
| Demanda de bit HBM | Se mantiene en +60% o más | +40% o menos |
| Proporción de obleas en HBM | Supera el 30% en 2027 | 27% o menos |
| Demanda de ASIC de IA | Aumento conjunto de TPU, Trainium y Meta ASIC | Se limita a sustituir a NVIDIA |
| CAPEX de hyperscalers | Nuevas revisiones al alza | Revisión a la baja en 2 o más compañías |
| Contratos de HBM | Ampliación de precontratos de volumen para 2028 | Acortamiento del plazo de contrato y renegociación de precio |
| DDR5 RDIMM | Aumento conjunto de precio y volumen | Caída durante 2 trimestres consecutivos |
| SOCAMM2 | Adopción en múltiples CSP y plataformas de CPU | Dependencia de una sola plataforma |
| Calendario de energía y DC | Aceleración de instalaciones | Retraso en conexión y finalización |
| Días de inventario | Inventario de clientes estable | Inventario que crece más rápido que las ventas |

---

## 10. El juicio de inversión sobre Samsung, SK Hynix y Micron

La fecha de referencia de la base de datos local es 2026-07-16 para Samsung Electronics y SK Hynix, y 2026-07-17 para Micron.

| Compañía | Precio actual | PER FY27 / próximo año fiscal | Efecto positivo de la expansión | Riesgo clave |
|---|---:|---:|---|---|
| Samsung Electronics | 255.000 KRW | 3,88x | Recuperación de cuota de HBM, el mix de producto más amplio | Sensibilidad al precio de la DRAM genérica |
| SK Hynix | 1.842.000 KRW | 4,20x | Pureza de HBM y SOCAMM, y apalancamiento de utilización | CAPEX a gran escala y ROIC después de 2028 |
| Micron | 848,95 USD | 5,64x | Localización en EE. UU., crecimiento simultáneo de HBM, DDR y eSSD | Alto costo de las fábricas en EE. UU., prima de múltiplo relativa |

[Hecho: cotización y consenso de la base de datos local]

Estos PER no son una señal de que la acción esté "barata", sino <strong>el descuento que aplica el mercado ante la posibilidad de que el beneficio de 2027 sea el pico</strong>. Un PER 2027E bajo, de 4-6x, significa que el mercado ya incorporó en el precio el pico de beneficio y la normalización de 2028.

Si se ordenan por capacidad, el ranking es este. [Inferencia: ranking relativo]

- Elasticidad de beneficio 2026-2027: <strong>SK Hynix > Micron > Samsung Electronics</strong>
- Margen de revisión al alza de estimaciones por recuperación de cuota de HBM: <strong>Samsung Electronics > Micron > SK Hynix</strong>
- Defensa ante la sobreoferta desde 2028: <strong>Samsung Electronics > Micron > SK Hynix</strong>
- Elasticidad bursátil si el shortage de HBM persiste hasta 2030: <strong>SK Hynix > Micron > Samsung Electronics</strong>

### Conclusión por escenario

- <strong>Si la demanda supera lo esperado</strong>: máximo upside para SK Hynix, máxima elasticidad de revisión al alza para Samsung Electronics
- <strong>Escenario base</strong>: ventaja de atractivo ajustado por riesgo para Samsung Electronics, SK Hynix en Core Hold
- <strong>Si la demanda queda por debajo</strong>: Samsung Electronics con defensa relativa, mayor amplitud de revisión a la baja de beneficios para SK Hynix y Micron
- <strong>Condición de descarte de la tesis</strong>: cuando la previsión de demanda de bit HBM para 2027 caiga por debajo de +40% y se confirmen a la vez una revisión a la baja del CAPEX de los hyperscalers y un aumento del inventario de clientes

### Lo que dice la reacción bursátil

| Acción | 15/7 | 16/7 | Último cierre |
|---|---:|---:|---:|
| Samsung Electronics | +6,27% | -8,77% | 255.000 KRW |
| SK Hynix | +8,83% | -11,53% | 1.842.000 KRW |
| Micron | -8,02% | -5,65% | 848,95 USD |

Como Samsung y Hynix subieron el mismo día de la declaración del presidente Chey y luego cayeron con fuerza al día siguiente, <strong>es difícil considerar que esa declaración fuera el catalizador directo de la venta</strong>. En la caída del 16 de julio actuaron a la vez Kimi K3, las dudas sobre el retorno del CAPEX de IA, la IPO de CXMT y la liquidación de posiciones tras el fuerte repunte previo. [Inferencia: factores combinados]

---

## Cierre

Si volvemos a la pregunta inicial, la respuesta es esta. Es probable que la demanda de memoria para IA cumpla o supere las altas expectativas actuales (crecimiento fuerte ~80%). Pero superarlas por un margen amplio todavía no es el escenario base (exceso ~35%).

La vía más probable es esta. El shortage de HBM se prolonga hasta 2027, la demanda se propaga hacia SOCAMM, DDR5 y eSSD, y en 2028 aumenta la nueva capacidad, pero no se convierte de inmediato en sobreoferta. A partir de 2028 habrá que reverificar la rentabilidad real del CAPEX de IA y la tasa de crecimiento de la oferta.

El núcleo de la perspectiva de inversión no es que "el HBM crece". Eso ya lo sabe el mercado. <strong>El verdadero alfa asimétrico está en si la demanda se propaga del HBM hacia la DDR de servidor, SOCAMM y eSSD, y si su duración se extiende más allá de 2028.</strong>

La lógica de expansión del presidente Chey es válida desde el punto de vista industrial. Preservar el mercado de clientes y el margen de tolerancia política es más favorable para el valor empresarial de largo plazo que maximizar el precio actual. Para los inversores, es de doble filo. Hasta 2027 es una declaración alcista que confirma un shortage severo, y desde 2029 es una declaración bajista que anticipa la normalización del CAPEX, la depreciación y el ASP. No es un motivo para vender ahora, pero también se debilitó el fundamento para valorar a las tres compañías de memoria como negocios de margen alto de forma permanente.

Por eso, <strong>la conclusión actual es mantener la tesis de shortage hasta 2027 y reverificarla a partir de 2028</strong>. La condición para la próxima subida de la acción no es el aumento del beneficio de 2027, sino la evidencia de que el beneficio de 2028 no se quiebra.

---

_Esta publicación es un material de análisis de oferta-demanda e inversión que sintetiza previsiones públicas (TrendForce, Omdia), anuncios y divulgaciones corporativas (Micron, SK Hynix, Samsung Electronics), y la cotización y el consenso de la base de datos local. Las probabilidades de los escenarios de demanda, las tasas de crecimiento de la oferta y el modelo base de 2027 son estimaciones propias al momento de escribir este artículo, no un consenso oficial. Los inicios de oblea mensuales por fábrica, la proporción de asignación de obleas por producto, los precios y volúmenes de los contratos de largo plazo de HBM, y el calendario de las nuevas fábricas en EE. UU. no pueden confirmarse con información pública. Las acciones mencionadas son ejemplos para explicar la estructura de la industria y no constituyen una recomendación de compra o venta de ningún valor en particular. La decisión de inversión y su responsabilidad recaen exclusivamente en cada inversor._

---

### Publicaciones relacionadas

- [Investigación profunda de oferta-demanda de HBM 2030: diseccionando el modelo de demanda de 26,7EB frente al calendario de capacidad](/es/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
- [¿Son cíclicos los semiconductores y cuál es el valor razonable?](/es/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [El verdadero debate en semiconductores: cuatro relojes físicos y un reloj bursátil](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [La localización de memoria en China y Corea: descomponiendo la exposición a China de Samsung, SK Hynix y Micron](/es/post/china-memory-localization-exposure-samsung-hynix-micron-2026-07-18/)
- [SK Hynix recorta beneficios del 2T pero mantiene precios objetivo: síntesis de los informes de Mirae Asset y KIS](/es/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/)
