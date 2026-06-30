---
title: "Revisión H1 2026: Los Cuellos de Botella de la Infraestructura de IA se Ampliaron, pero el Mercado No"
date: 2026-06-30T22:35:00+09:00
description: "Revisión detallada del H1 2026 de los mercados de valores de Corea y EE.UU.: concentración en megacaps del KOSPI, debilidad del KOSDAQ, venta extranjera absorbida por liquidez doméstica, cuellos de botella en infraestructura de IA en EE.UU., y rotación hacia HBM, memoria, almacenamiento, servidores, equipos y energía."
categories: ["Análisis Exclusivo", "Macro", "Semiconductores de Corea"]
tags:
  - "H1 2026"
  - "infraestructura de IA"
  - "HBM"
  - "memoria"
  - "KOSPI"
  - "KOSDAQ"
  - "amplitud del mercado"
  - "flujos extranjeros"
  - "Micron"
  - "Samsung Electronics"
  - "SK Hynix"
series: ["exclusive-analysis", "macro-gates-2026", "hbm"]
slug: "h1-2026-ai-infra-bottleneck-korea-narrow-market-postmortem-2026-06-30"
valley_cashtags:
  - Samsung Electronics
  - SK Hynix
  - Micron
  - NVIDIA
  - Samsung Electro-Mechanics
draft: false
---

> Contexto relacionado
> Este es un seguimiento semestral de [la previsión 2T26 de Samsung](/post/samsung-2q26-preview-micron-surprise-erased-core-op-hbm-2026-06-29/), [los resultados FY3Q26 de Micron](/post/micron-fy3q26-ai-memory-sca-fcf-hold-2026-06-25/), [el marco de elasticidad de NVIDIA para Samsung y SK Hynix](/post/nvidia-earnings-elasticity-hbm-cycle-samsung-hynix-2026-06-28/), [la dificultad de superar el benchmark del KOSPI](/post/kospi-benchmark-hard-to-beat-narrow-market-monte-carlo-2026-06-20/), [el marco de disparidad a 60 días del KOSPI](/post/kospi-disparity60-overheat-framework-partial-trim-2026-06-21/), [el marco de flujo real de dinero](/post/real-money-flow-framework-korea-institution-quality-2026-06-03/), y [la nota del punto medio del superciclo de IA](/post/ai-supercycle-midgame-rate-risk-yellow-not-red-2026-06-06/).

## TL;DR

El H1 2026 parecía un período amplio de apetito por el riesgo a nivel de índice. Por debajo de la superficie, fue mucho más estrecho. Corea fue un mercado de concentración en megacaps del KOSPI. EE.UU. fue un mercado de infraestructura de IA donde el liderazgo se desplazó desde las plataformas de IA de megacap hacia la memoria, el almacenamiento, los servidores, los equipos de semiconductores y la energía. Ningún mercado fue un mercado amplio donde "todo subió".

El índice coreano principal fue extraordinario. El KOSPI subió de 4.214,17 el 30 de diciembre de 2025 a 8.476,48 el 30 de junio de 2026, un +101,1%. El KOSDAQ cayó de 925,47 a 916,18, un -1,0%. De aproximadamente 2.700 acciones coreanas, 856 subieron y 1.788 cayeron. La rentabilidad mediana de las acciones fue del -12,6%. El índice se duplicó, pero la acción promedio estuvo en un mercado débil.

La historia de EE.UU. también fue más específica de lo que el índice sugiere. El S&P 500 ganó un 9,2% y el Nasdaq un 11,1%, pero la historia real fue la de los cuellos de botella en infraestructura de IA. SanDisk, Micron, Western Digital, Dell, Marvell, ARM, Applied Materials y Lam Research fueron mucho más sólidos que NVIDIA. El mercado compraba los puntos donde la fábrica de IA realmente tiene cuellos de botella.

La estrategia del H2 no es simplemente "encontrar acciones baratas". La mejor regla es comprar cuellos de botella probados con ingresos reales y contratos en las correcciones. Los nombres de equipos con carácter de opción, videojuegos y eventos de biotecnología deben tener un peso menor. Los cuellos de botella con ingresos recurrentes en memoria, eSSD, MLCC, sustratos, energía, construcción naval, defensa y grandes plataformas de biotecnología merecen mayor atención.

<div class="thesis-callout">
  <div class="thesis-callout__label">Conclusión en Una Línea</div>
  <div class="thesis-callout__body">
    El H1 fue de apetito por el riesgo, pero no fue amplio. Corea estuvo dominada por la concentración en Samsung Electronics y SK Hynix, mientras que EE.UU. premió los cuellos de botella físicos bajo la computación de IA. El H2 consiste en separar los cuellos de botella con ingresos recurrentes de las historias con carácter de opción y el riesgo de flujos apalancados.
  </div>
</div>

## 0. Base de Datos y Reconciliación

La base de datos es:

| Área | Base |
|---|---|
| Índices y acciones de Corea | Cierre del 30 de junio de 2026 |
| Índices y acciones de EE.UU. | Cierre del 29 de junio de 2026 |
| Flujos de Corea | DB local KR, base de montos Kiwoom |
| Rentabilidades de acciones de EE.UU. | DB local EE.UU. y cierre ajustado de yfinance |
| Datos secundarios | Naver Finance, screeners locales y análisis de flujo de sesión |

Algunas cifras difieren ligeramente según el conjunto de datos y la fecha de referencia. Por ejemplo, la rentabilidad final del KOSPI es del +101,1% usando el cierre del 30 de junio, mientras que algunas instantáneas de cestas locales muestran +96,7%, y la revisión intermedia del 23 de junio mostró +90,4%. Las rentabilidades de las acciones de IA en EE.UU. también difieren según el tratamiento del cierre ajustado y la gestión por parte del proveedor.

Este artículo reconcilia esas diferencias de la siguiente manera.

| Tipo de dato | Cómo se utiliza |
|---|---|
| Cierre de Corea del 30 de junio | Benchmark principal de rendimiento del H1 |
| Cierre de EE.UU. del 29 de junio | Benchmark principal de rendimiento del H1 en EE.UU. |
| Instantánea intermedia del 23 de junio | Evidencia de apoyo para la amplitud y la estructura de compradores |
| Diferencias entre cierre ajustado y DB local | Usadas de manera direccional cuando las conclusiones no cambian |
| Cifras individuales menos verificadas | Tratadas como elementos de seguimiento del H2, no como prueba central |

El objetivo no es una falsa precisión. La conclusión es estable: los índices fueron sólidos, la amplitud fue débil, y las rentabilidades de la infraestructura de IA se desplazaron desde las GPU hacia la memoria, el almacenamiento, los servidores, los equipos y la energía.

## 1. Rendimiento de los Índices: el KOSPI se Duplicó, el KOSDAQ Cayó

| Mercado | Base | Rentabilidad H1 |
|---|---:|---:|
| KOSPI | 4.214,17 el 30-12-2025 a 8.476,48 el 30-06-2026 | +101,1% |
| KOSDAQ | 925,47 a 916,18 | -1,0% |
| S&P 500 | 31-12-2025 al 29-06-2026 | +9,2% |
| Nasdaq | 31-12-2025 al 29-06-2026 | +11,1% |
| Russell 2000 | 31-12-2025 al 29-06-2026 | +21,3% |
| ETF de semiconductores SMH | 31-12-2025 al 29-06-2026 | +75,5% |
| ETF de semiconductores SOXX | 31-12-2025 al 29-06-2026 | +104,2% |

A nivel de índice, Corea fue espectacular. El KOSPI se duplicó en seis meses. Pero el KOSDAQ cayó. Dentro del mismo mercado coreano, las acciones de gran capitalización de infraestructura de IA y de crecimiento vivieron en mundos completamente diferentes.

La historia de los índices de EE.UU. también subestima la rotación interna. El S&P 500 y el Nasdaq subieron alrededor de dos dígitos bajos, mientras que los ETF de semiconductores subieron mucho más. El SOXX ganó un 104,2%, cercano a la ganancia del KOSPI, lo que muestra cuán concentrado se volvió el comercio global de hardware de IA.

## 2. Corea: el Índice se Duplicó, la Acción Mediana Cayó

| Elemento | Valor |
|---|---:|
| Acciones coreanas observadas | aproximadamente 2.700 |
| Valores alcistas en H1 | 856 |
| Valores bajistas en H1 | 1.788 |
| Rentabilidad mediana de acciones | -12,6% |
| Rentabilidad H1 del KOSPI | +101,1% |
| Rentabilidad H1 del KOSDAQ | -1,0% |

Esta es una combinación inusual. El índice estaba en un mercado alcista histórico, mientras que la acción mediana era débil. Por eso la experiencia vivida por los inversores fue tan diferente del titular del índice.

Los principales líderes del H1 fueron:

| Acción | Rentabilidad H1 |
|---|---:|
| Samsung Electro-Mechanics | +756% |
| Jusung Engineering | +626% |
| SK Square | +361% |
| SK Hynix | +307% |
| Jeju Semiconductor | +294% |
| Daeduck Electronics | +226% |
| Simmtech | +201% |
| Samsung Electronics | +179% |

La estructura del mercado coreano fue:

```text
Samsung Electronics y SK Hynix
→ Samsung Electro-Mechanics, MLCC y FC-BGA
→ sustratos, PCB y equipos de semiconductores
→ equipos de energía, industriales y algunos financieros
```

El KOSDAQ, muchos nombres de biotecnología, plataformas y parte de las baterías secundarias quedaron rezagados. Corea fue sólida, pero la mayoría de las acciones coreanas no lo fueron.

## 3. Corea No Fue un Mercado de Compras Extranjeras

Datos de flujo acumulado del año en la base de montos Kiwoom local:

| Grupo de inversores | Acumulado en el año |
|---|---:|
| Extranjeros | -KRW 142T |
| Instituciones | +KRW 45T |
| Minoristas | +KRW 77,7T |
| Inversión financiera | +KRW 75,4T |
| Fondos de inversión | -KRW 1,7T |
| Fondos privados | -KRW 3,8T |
| Fondos de pensiones y otros | -KRW 7,0T |

El punto clave es que Corea no fue un simple mercado de compras extranjeras. Los extranjeros vendieron Samsung Electronics y SK Hynix de manera significativa. Los minoristas domésticos, las cuentas de inversión financiera y las instituciones absorbieron el flujo.

| Acción | Rentabilidad acumulada en el año | Flujo acumulado extranjero |
|---|---:|---:|
| Samsung Electronics | alrededor de +160% | -KRW 72,6T |
| SK Hynix | alrededor de +291% | -KRW 57,1T |
| SK Square | alrededor de +333% | -KRW 7,6T |
| Samsung Electronics preferred | alrededor de +125% | -KRW 3,2T |

Los extranjeros vendieron las principales megacaps mientras esas acciones subían. Eso no es un repunte normal liderado por extranjeros. Fue un mercado de absorción doméstica.

Los extranjeros no vendieron todo. Rotaron hacia cuellos de botella selectos y activos favorables para los fondos globales, como Samsung Electro-Mechanics, Doosan Enerbility, Samsung SDI, FADU, Hanwha Ocean y Sanil Electric. La descripción correcta no es "los extranjeros compraron Corea". Es "los extranjeros vendieron las mayores megacaps de memoria, la liquidez doméstica las absorbió, y los extranjeros reasignaron hacia cuellos de botella selectos de segunda capa".

## 4. El Comprador Oculto Fue la Inversión Financiera, No el Dinero Real Long-Only

Las compras institucionales no fueron lo mismo que la acumulación long-only. La subcategoría institucional más sólida fue la inversión financiera, no los fondos de inversión, los fondos privados ni los fondos de pensiones.

| Categoría de flujo | Interpretación |
|---|---|
| Inversión financiera | ETF, derivados, flujo de programas y reequilibrio vinculado |
| Fondos de inversión | Más probablemente representa demanda de fondos long-only, pero débil en H1 |
| Fondos privados | Flujo temático mixto, long-short y orientado a eventos, pero acumulación neta débil |
| Fondos de pensiones y otros | Dinero real a largo plazo, pero vendedor neto en H1 |
| Minoristas | Absorbente clave del flujo de infraestructura de IA de megacap y el apalancamiento |

Esto importa. El dinero real puede sostener una tendencia. El flujo de inversión financiera y de programas puede ser poderoso, pero es más vulnerable al vencimiento de futuros, los límites de los ETF, el posicionamiento en derivados y la mecánica del apalancamiento.

El H1 coreano fue tanto un mercado de revaluación fundamental como un mercado de derivados y ETF. Confundir ambos lleva a errores repetidos.

## 5. Al KOSDAQ le Faltaron Compradores, No Historias

El KOSDAQ tenía muchas historias: biotecnología, robótica, CPO, SOCAMM, equipos de semiconductores, videojuegos y software de IA. El índice igualmente quedó rezagado porque la base de compradores era débil.

La instantánea intermedia del 23 de junio ya era clara:

| Índice | Acumulado en el año | Desde el máximo |
|---|---:|---:|
| KOSPI | +90,4% | -10,0% |
| KOSDAQ | -5,7% | -27,3% |

La estructura final del 30 de junio fue la misma: KOSPI +101,1%, KOSDAQ -1,0%.

El KOSDAQ tuvo dificultades porque:

1. El capital minorista estaba ocupado absorbiendo Samsung Electronics, SK Hynix y los grandes nombres de infraestructura de IA.
2. El dinero real institucional no compró el KOSDAQ de manera amplia.
3. La compra extranjera fue estrecha, centrada en nombres como FADU, Jeju Semiconductor y Simmtech.
4. La presión de las tasas y el tipo de cambio pesó sobre los múltiplos de biotecnología y crecimiento no rentable.

La condición para la recuperación del KOSDAQ es:

```text
Recuperación del KOSDAQ =
retorno del capital minorista
+ compras de dinero real institucional
+ Samsung Electronics y SK Hynix moviéndose de lado en lugar de caer
+ estabilización de las revisiones de ganancias del KOSDAQ
```

Si Samsung y SK Hynix colapsan, el dinero no rota automáticamente hacia el KOSDAQ. El modo de aversión al riesgo llega primero. El mejor entorno para el KOSDAQ no es el colapso de las megacaps. Es la consolidación de las megacaps.

## 6. El Mercado de EE.UU. No Fue Solo NVIDIA

La señal real de EE.UU. no fue "la IA subió". Fue:

> Los cuellos de botella físicos después de la GPU superaron al líder de GPU.

Rangos representativos de rentabilidad del H1:

| Acción | Rango de rentabilidad H1 |
|---|---:|
| SanDisk | +645-764% |
| Micron | +263-301% |
| Western Digital | +247-279% |
| Intel | +235-257% |
| Dell | +224-232% |
| Marvell | +211-227% |
| ARM | +200-214% |
| Applied Materials | +171% |
| AMD | +152% |
| Lam Research | +141% |

Las grandes tecnológicas tuvieron resultados mixtos:

| Acción | Rentabilidad H1 |
|---|---:|
| Google | +13% |
| Amazon | +4% |
| Apple | +4% |
| NVIDIA | +3-5% |
| Broadcom | +7% |
| Meta | -15% |
| Microsoft | -22% a -23% |
| Oracle | -25% |
| Palantir | -31% |

El mercado compraba los puntos donde la fábrica de IA tiene cuellos de botella:

```text
GPU
→ HBM y DRAM
→ eSSD y almacenamiento
→ servidores y racks
→ óptica e interconexión
→ equipos de semiconductores
→ energía y refrigeración
```

Esto es directamente relevante para Corea. HBM mapea a Samsung y SK Hynix. eSSD y NAND mapean a Samsung, FADU y Jeju Semiconductor. MLCC y FC-BGA mapean a Samsung Electro-Mechanics y nombres de sustratos. La energía mapea a Doosan Enerbility y equipos eléctricos. Los equipos mapean a HPSP, TES, VM y Jusung.

## 7. El Macro No Fue un Viento de Cola Puro

| Activo o indicador | Movimiento H1 |
|---|---:|
| Índice del dólar | +3,1% |
| USD/KRW | +7,9% |
| Rendimiento del bono a 10 años de EE.UU. | 4,16% a 4,39% |
| Petróleo WTI | +24,1% |
| Oro | -6,8% |
| Bitcoin | -33,2% |

Este no fue un entorno macro de expansión pura de múltiplos. El dólar subió, el won se debilitó, los rendimientos de EE.UU. subieron y el petróleo subió. El oro y el Bitcoin cayeron.

Las acciones subieron de todas formas porque el ciclo de ganancias de la infraestructura de IA superó la presión macro. Eso es importante para el H2. Si las tasas, el dólar y el petróleo vuelven a subir juntos, las acciones de cuellos de botella más concentradas pueden sufrir una compresión de múltiplos incluso si la demanda sigue siendo sólida.

El riesgo realista es:

```text
La demanda de IA sigue siendo fuerte
+ las ganancias siguen siendo buenas
+ las tasas, el dólar y el petróleo se mantienen firmes
+ la valoración y los flujos apalancados se rompen primero
```

Este es el mismo problema de elasticidad de acciones discutido en el marco NVIDIA/Samsung/SK Hynix.

## 8. Verdad No Consensuada 1: el Liderazgo se Desplazó de la Computación a la Memoria

El primer punto no consensuado es el liderazgo de IA en EE.UU. NVIDIA sigue siendo el centro de la IA. Pero la rentabilidad incremental de las acciones se desplazó hacia Micron, SanDisk, Western Digital, Dell, Marvell y ARM.

Eso no significa que la computación ya no importe. Significa que el retorno marginal se desplazó hacia abajo en la cadena.

| Pregunta | Significado |
|---|---|
| ¿Es esta empresa un elemento de costo en el capex de IA? | Puede verse presionada cuando los clientes optimizan costos. |
| ¿Es esta empresa un cuello de botella en el capex de IA? | Puede repriciarse si los clientes necesitan suministro. |
| ¿Es esta empresa solo una narrativa? | Es vulnerable durante las brechas de catalizadores. |

Los elementos de costo se ven presionados. Los cuellos de botella se revalúan. Las narrativas requieren disciplina de timing.

## 9. Verdad No Consensuada 2: el Máximo Real Llegó Antes del Máximo del Índice

La amplitud se debilitó antes que el índice. El máximo del índice en junio fue impulsado por Samsung Electronics, SK Hynix y un pequeño conjunto de nombres de infraestructura de IA. El KOSDAQ y la acción mediana ya se habían debilitado antes.

```text
Acción mediana débil
+ KOSDAQ débil
+ megacaps de memoria del KOSPI fuertes
= máximo del índice y mercado vivido débil al mismo tiempo
```

Para el H2, los indicadores clave son la amplitud, el ADR, la fortaleza relativa KOSDAQ/KOSPI, la participación del volumen negociado de las megacaps de memoria, y la compra conjunta de minoristas e institucionales en el KOSDAQ.

## 10. Verdad No Consensuada 3: los Múltiplos se Movieron Antes de que los Fundamentales Llegaran Completamente

Samsung, SK Hynix, Micron y Samsung Electro-Mechanics tuvieron fundamentales sólidos. Pero las rentabilidades de las acciones se movieron más rápido que las ganancias a corto plazo. El mercado cambió el múltiplo.

```text
Marco antiguo:
memoria = ciclo de commodities = descuento en ganancias pico

Marco del H1:
memoria = cuello de botella de infraestructura de IA = escasez de oferta más prima de contrato
```

El riesgo del H2 no es solo malas ganancias. Es buenas ganancias con múltiplos más bajos si el mercado empieza a tratar la memoria como un commodity nuevamente. Los inversores deben vigilar la velocidad de revisión del EPS, la magnitud de las sorpresas positivas y la visibilidad del FY2027, no solo el próximo batimiento trimestral.

## 11. Verdad No Consensuada 4: la Fontanería del Apalancamiento Amplificó el Riesgo de Cola

Las megacaps de memoria coreanas se vieron afectadas no solo por los fundamentales, sino también por la mecánica del apalancamiento: ETFs 2x y 3x de Samsung/SK Hynix listados en el extranjero, productos de apalancamiento e inversos domésticos, futuros y flujo de programas.

Ciclo de subida simplificado:

```text
acción sube
→ reequilibrio de compra de ETF apalancado
→ soporte de futuros y programas
→ más subida de megacaps
→ más capital de momentum
```

Ciclo de bajada:

```text
acción baja
→ reequilibrio de venta de ETF apalancado
→ presión de futuros y programas
→ riesgo de margen minorista y ventas forzadas
→ mayor caída
```

Por lo tanto, Corea puede moverse más violentamente que Micron incluso cuando la dirección fundamental es similar.

## 12. Verdad No Consensuada 5: el Suministro Pasó de Manos Fuertes a Manos Más Débiles

La pregunta importante no es solo quién vendió. Es quién compró.

En el H1, los extranjeros y algunas cuentas institucionales redujeron su exposición en megacaps de memoria mientras los minoristas y las cuentas de inversión financiera absorbían el flujo.

| Lectura positiva | Lectura negativa |
|---|---|
| La liquidez doméstica es fuerte | Las acciones pueden haber pasado a manos más débiles y apalancadas |
| El KOSPI aguantó a pesar de la venta extranjera | El riesgo de ventas forzadas aumenta si el margen se deshace |
| La base de compradores de grandes capitalizaciones se amplió | También puede representar distribución desde cuentas mejor informadas |

El seguimiento del H2 debe combinar el flujo de caja extranjero, el margen minorista, los depósitos, los saldos de ETF y el flujo de programas.

## 13. Verdad No Consensuada 6: los Extranjeros Compraron Activos Coreanos Globalmente Explicables

Los extranjeros no compraron todos los temas coreanos. Las acciones que compraron eran globalmente explicables.

| Acción | Compra neta extranjera acumulada en el año |
|---|---:|
| Samsung Electro-Mechanics | +KRW 2,28T |
| Doosan Enerbility | +KRW 1,71T |
| Celltrion | +KRW 1,52T |
| Samsung SDI | +KRW 1,33T |
| Doosan | +KRW 1,11T |
| APR | +KRW 1,08T |
| Hyundai Rotem | +KRW 0,85T |
| LG Energy Solution | +KRW 0,85T |
| FADU | +KRW 0,80T |
| Hanwha Ocean | +KRW 0,76T |

Características comunes:

```text
energía, nuclear, construcción naval y defensa
industriales de calidad global
grandes nombres de baterías
grandes plataformas de biotecnología
cuellos de botella directos de infraestructura de IA
```

Para el H2, el capital long-only extranjero tiene más probabilidades de comprar activos que puede explicar ante un comité de inversión que historias oscuras de pequeña capitalización.

## 14. Verdad No Consensuada 7: el Patrón de Ingresos Superó la Calidad de la Empresa

En el H1, la calidad del patrón de ingresos importó más que la calidad abstracta de la empresa.

Nombres con patrón de ingresos débil:

| Tipo | Debilidad |
|---|---|
| Equipos | Las brechas de pedidos pueden crear brechas de ganancias. |
| Videojuegos | La visibilidad de ingresos se rompe alrededor de los ciclos de lanzamiento. |
| Acciones de eventos de biotecnología | Las brechas de ensayos y licencias crean brechas narrativas. |
| Algunos nombres de robótica y software de IA | Las expectativas se mueven antes que los ingresos. |

Nombres con patrón de ingresos sólido:

| Tipo | Fortaleza |
|---|---|
| Memoria | Los precios y el volumen mejoraron juntos. |
| eSSD y almacenamiento | Revaluación del cuello de botella de almacenamiento en servidores de IA. |
| MLCC y sustratos | Cuellos de botella en servidores y paquetes. |
| Equipos de energía | Demanda de energía de centros de datos más capital de política. |
| Construcción naval | Visibilidad de cartera de pedidos a largo plazo. |
| Defensa | Cartera de exportaciones y presupuestos gubernamentales. |
| Grandes plataformas de biotecnología | Los contratos, la producción y el valor de plataforma son explicables. |

La regla del H2 es simple:

> Dar menor peso a los nombres con carácter de opción. Dar mayor peso a los cuellos de botella con ingresos recurrentes.

## 15. Hipótesis Adicional: Corea se Convirtió en un Proxy Apalancado de IA de EE.UU.

La identidad del mercado coreano cambió en el H1. Históricamente, Samsung y SK Hynix eran proxies de los mercados emergentes, China y los ciclos globales de inventario de TI. En el H1 2026, el vínculo con el capex de IA de EE.UU. se volvió mucho más fuerte.

El análisis de sesiones sugirió una relación más fuerte entre los movimientos del día anterior de IA/semi en EE.UU. y las megacaps de memoria de Corea al día siguiente, incluyendo una estimación de correlación intermedia de 0,42. Esa cifra necesita revalidación formal, pero la acción del precio es consistente con la dirección.

El problema es la diversificación. Si Corea se comporta como un proxy apalancado del capex de IA de EE.UU., los amortiguadores domésticos se debilitan cuando el factor global de IA se enfría.

Otro elemento a vigilar es el capex. El análisis de sesiones clasificó el gran compromiso de capex de SK Hynix como un punto de control de máxima confianza. El monto exacto y el alcance deben verificarse contra los registros antes de que se convierta en un argumento central. Pero históricamente, los anuncios de capex pico suelen llegar cuando la demanda parece más fuerte.

Preguntas clave sobre el capex del H2:

| Pregunta | Significado |
|---|---|
| ¿Los contratos con clientes respaldan el capex? | Reduce el riesgo de exceso de oferta. |
| ¿El capex deteriora el FCF? | Las ganancias pueden verse bien mientras el flujo de caja se debilita. |
| ¿La oferta llega cerca del pico de demanda? | Aumenta el riesgo de ciclo en 2027. |
| ¿El capex está enfocado en HBM y memoria de IA? | Debe separarse del riesgo de exceso de oferta de DRAM convencional. |

## 16. Lista de Verificación del H2

| Punto de control | Por qué importa |
|---|---|
| Samsung Core OP 2T26 | El poder de beneficio central importa más que el OP titular reportado. |
| Asignación HBM de SK Hynix en 2T y 3T | Determina si el ganador concentrado puede reacelerarse. |
| Entrega de guía FY4Q26 de Micron | Prueba si la prima de memoria de IA de EE.UU. puede persistir. |
| Precios de DRAM y NAND | Confirma la defensa de márgenes más allá del HBM. |
| Compras minoristas e institucionales en KOSDAQ | Necesarias para la recuperación del KOSDAQ. |
| Flujo de inversión financiera y programas | Fontanería real detrás de la volatilidad de megacaps. |
| USD/KRW, rendimientos a 10 años de EE.UU. y petróleo | Ponen un techo en los múltiplos de los cuellos de botella de IA. |
| Contratos de capex de IA y FCF | Muestra si la demanda está pagada por flujo de caja, no solo por narrativa. |

## 17. Estrategia del H2

| Área | Estrategia |
|---|---|
| Núcleo de infraestructura de IA | Mantener exposición, pero comprar correcciones en lugar de perseguir. |
| Megacaps de memoria | Samsung es el candidato con alfa no reflejado. SK Hynix es el candidato de reaceleración tras correcciones. |
| Cuellos de botella de pila inferior de HBM | Comprar solo donde los pedidos, los márgenes y la calificación de clientes sean visibles. |
| KOSDAQ | No comprar todo el índice primero. Comenzar con equipos de semiconductores, pruebas y nombres de crecimiento rentable. |
| Equipos con carácter de opción, videojuegos y biotecnología | Menor ponderación por riesgo de brecha de catalizadores. |
| Cíclicos de calidad global | Seguir monitoreando construcción naval, defensa, energía, nuclear y grandes plataformas de biotecnología. |

La estrategia del H2 en una frase:

> Mantener la exposición central en infraestructura de IA, reducir posiciones con carácter de opción y desplazarse hacia cuellos de botella con ingresos recurrentes y cíclicos de calidad coreanos que el capital global pueda explicar.

## 18. Visión Final

Puede que la multitud recuerde el H1 2026 como el mejor año del superciclo coreano/de semiconductores. Eso no es incorrecto. El KOSPI se duplicó y los líderes de memoria, sustratos, equipos y energía se dispararon.

Pero la historia más importante es:

```text
el liderazgo se volvió extremadamente estrecho
los múltiplos se movieron antes de que los fundamentales llegaran completamente
los extranjeros vendieron las principales megacaps mientras la liquidez doméstica las absorbía
los flujos de inversión financiera y ETF/programas amplificaron el mercado
al KOSDAQ le faltaron compradores, no historias
el liderazgo de IA en EE.UU. se desplazó de las GPU hacia la memoria, el almacenamiento, los servidores y la energía
```

La pregunta del H2 no es solo "¿cuánto más potencial alcista queda?". Las mejores preguntas son:

1. ¿La elasticidad de las acciones sigue siendo positiva incluso después de sólidas ganancias?
2. ¿Puede la liquidez doméstica seguir absorbiendo la venta extranjera?
3. ¿Vuelven los compradores al KOSDAQ?
4. ¿Los cuellos de botella de IA convierten la narrativa en ingresos y contratos?

El H1 fue de apetito por el riesgo, pero no fue amplio. Fue un mercado de liderazgo comprimido. El H2 requiere mayor precisión: cuellos de botella reales sobre acciones baratas, ingresos recurrentes sobre catalizadores puntuales, y Core OP más FCF sobre ganancias titulares.

## Nota sobre los Datos

- Datos de Corea: DB local KR, datos de flujo de inversores Kiwoom y soporte de Naver Finance al cierre del 30 de junio de 2026.
- Datos de EE.UU.: DB local EE.UU. y cierre ajustado de yfinance al cierre del 29 de junio de 2026.
- Instantáneas intermedias: rendimiento relativo KOSPI/KOSDAQ del 23 de junio y análisis de flujo de sesión.
- Los resultados de la sesión regular del 30 de junio en EE.UU. no están incluidos.
- Las cifras individuales de capex menos verificadas se tratan como elementos de seguimiento del H2 en lugar de prueba central.

*Descargo de responsabilidad: Solo para fines de investigación e información. No es asesoramiento de inversión. Los nombres citados son para ilustración analítica; los lectores deben realizar su propia diligencia debida y consultar a asesores autorizados antes de tomar cualquier decisión de inversión.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
