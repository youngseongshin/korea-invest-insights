---
title: "2028 importa más que el boom de 2027: Escenarios integrados para Samsung Electronics y SK Hynix"
description: "Partiendo del escenario base de un boom de memoria en 2027, este análisis incorpora la expansión de oferta en 2028, las ganancias en eficiencia de inferencia y el riesgo de refinanciación de infraestructura de IA. Comparamos Samsung Electronics y SK Hynix sobre una base ponderada por probabilidad en términos de EPS por escenario, PER de valor razonable y valor presente, y examinamos cómo los contratos de largo plazo de HBM y la expansión de la capacidad de memoria china reconfiguran la duración de los beneficios."
date: 2026-07-13T20:39:17+09:00
lastmod: 2026-07-13T20:39:17+09:00
categories: ["Análisis Exclusivo", "Semiconductores", "Macro"]
tags:
  - "Samsung Electronics"
  - "SK Hynix"
  - "HBM"
  - "Semiconductores de Memoria"
  - "Infraestructura de IA"
  - "Análisis de Escenarios"
  - "Valoración"
  - "CXMT"
  - "YMTC"
series: ["exclusive-analysis", "ai-hbm-2026"]
slug: "samsung-sk-hynix-2027-2028-integrated-scenarios-risk-adjusted-valuation-2026-07-13"
image: "/images/posts/samsung-hynix-2027-2028-scenario-map-2026-07-13.png"
valley_cashtags:
  - 삼성전자
  - SK하이닉스
draft: false
---

> Contexto relacionado: Esta publicación es un seguimiento del [Modelo de Oferta-Demanda de HBM 2030: Verificación Cruzada](/es/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/), [Valoración de Samsung Electronics y SK Hynix a través de los Beneficios Estimados para 2028](/es/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/) y el [Análisis de la Caída del Hardware de IA del 13 de julio](/es/post/kospi-9pct-selloff-ai-hardware-derating-korea-leverage-2026-07-13/). Aceptando el boom de 2027 como línea base, cuantifica la probabilidad de que las condiciones de oferta, eficiencia y financiación cambien simultáneamente a partir de 2028.

## TL;DR

- Es probable que la oferta/demanda de HBM se mantenga ajustada durante 2027. Sin embargo, la proyección de `demanda 2030 de 26.7EB frente a oferta de 10.6EB, déficit de 2.52×` no es una previsión de caso base —requiere que múltiples supuestos alcistas se cumplan simultáneamente.
- El año más importante no es 2027 sino <strong>2028</strong>. La expansión de oferta de Samsung Electronics, SK Hynix y Micron, las ganancias en eficiencia de inferencia y la verificación de refinanciación en los centros de datos de IA confluyen en la misma ventana temporal.
- Los contratos de suministro de largo plazo de HBM prolongan la duración de los beneficios pero no eliminan el ciclo. Convierten el riesgo de precio en riesgo de renovación de contrato, riesgo crediticio de los clientes, riesgo de mezcla de productos y riesgo de reajuste de precios.
- Probabilidades condicionales: P1 exceso de demanda sostenido 35%, P2 estrés crediticio localizado con reconcentración en hiperescaladores 40%, P3 ganancias en eficiencia y normalización de la oferta 15%, P4 contracción crediticia sistémica 10%.
- EPS ponderado por probabilidad para 2027: Samsung Electronics 60,750원, SK Hynix 393,000원. Para 2028: Samsung 49,900원, SK Hynix 316,000원.
- Valor presente de los valores terminales de 2028 descontados al 11% anual: Samsung Electronics 317,246원, SK Hynix 1,956,316원 —lo que implica un potencial alcista del 24,7% y el 6,0% respectivamente respecto a los precios de cierre en KRX del 13 de julio. Una vez incorporado el riesgo de normalización de 2028, el margen de seguridad de Samsung es más amplio; SK Hynix es más sensible a si P1 se mantiene.

<div class="thesis-callout">
  <div class="thesis-callout__label">Conclusión</div>
  <div class="thesis-callout__body">
    El boom de 2027 es relativamente visible. La pregunta más difícil es <strong>si los precios elevados de HBM y los beneficios se mantienen durante 2028 y más allá</strong>. Los precios actuales descuentan la duración de los beneficios mucho más allá del pico de 2027.
  </div>
</div>

![Mapa de Escenarios Integrados 2027–2028 para Samsung Electronics y SK Hynix](/images/posts/samsung-hynix-2027-2028-scenario-map-2026-07-13.png)

## 1. Preguntas Analíticas y Calidad de la Evidencia

Este análisis vincula tres preguntas en un único marco.

1. ¿Cuánta confianza podemos depositar en la perspectiva de que la oferta/demanda de HBM se mantendrá ajustada durante 2027?
2. Si las condiciones de oferta, eficiencia y financiación cambian simultáneamente en 2028, ¿en qué difieren los beneficios de Samsung Electronics y SK Hynix entre escenarios?
3. Dados esos cambios, ¿a qué nivel de beneficios implícito cotiza el precio actual de la acción?

Los números de este informe deben leerse por categoría.

| Categoría | Definición | Ejemplo en Este Informe |
|---|---|---|
| Hecho | Verificado a partir de registros públicos o datos de mercado | Precios de cierre en KRX del 13 de julio, FCF de Oracle, endeudamiento de CoreWeave |
| Consenso | Estimaciones de mercado agregadas | EPS e ingreso neto de 2027–2028 |
| Estimación de broker | Previsión de un broker individual | EPS de SK Hynix de Korea Investment & Securities y BNK Investment & Securities |
| Resultado del modelo | Derivado de fórmulas y supuestos divulgados | EPS ponderado por probabilidad P1–P4 y valores presentes |
| Juicio analítico | Juicio analítico no estadístico | Probabilidades de escenario, PER razonable, rentabilidad exigida del 11% |
| Bloqueado | No puede determinarse únicamente a partir de fuentes públicas | Precios de contratos de HBM a nivel de cliente, volúmenes por cliente, rendimiento de producción real |

Las fórmulas principales son las siguientes.

```text
Scenario Terminal Value = Scenario EPS × Scenario Fair PER
Probability-Weighted EPS = Σ(Scenario Probability × Scenario EPS)
Probability-Weighted Terminal Value = Σ(Scenario Probability × Scenario Terminal Value)
Present Value = Terminal Value ÷ (1 + 11%)^Remaining Years
HBM Need/Fleet = Installed and active HBM demand stock ÷ supply capacity that can be served by installed fleet
```

Las probabilidades de los escenarios no se derivan de distribuciones de frecuencia históricas. Son juicios condicionales que reflejan las condiciones actuales observables de demanda, oferta, eficiencia y financiación. Los valores de PER razonable tampoco se observan mecánicamente en el mercado, sino que son estimaciones analíticas que incorporan la durabilidad de los beneficios, la concentración del negocio, la estructura financiera y el riesgo a largo plazo.

## 2. Precio Actual y Consenso de Mercado

A lo largo del documento se utilizan los precios de cierre en KRX del 13 de julio y las estimaciones de consenso agregadas en la misma fecha.

| Elemento | Samsung Electronics | SK Hynix |
|---|---:|---:|
| Precio de Cierre en KRX 2026-07-13 | 254,500원 | 1,845,000원 |
| EPS de Consenso 2027 | 65,802원 | 444,359원 |
| EPS de Consenso 2028 | 65,907원 | 433,625원 |
| Ingreso Neto de Consenso 2027 | 44.3조원 | 32.4조원 |
| Ingreso Neto de Consenso 2028 | 44.1조원 | 31.9조원 |
| Precio Actual / EPS de Consenso 2027 | 3.87× | 4.15× |
| Precio Actual / EPS de Consenso 2028 | 3.86× | 4.25× |

A primera vista, ambas compañías parecen extraordinariamente baratas. Sin embargo, estos bajos múltiplos PER no significan que el mercado desconozca los beneficios de 2027 —es más probable que sean una señal de que el mercado duda de la durabilidad de los beneficios más allá de 2028.

La dispersión entre las estimaciones de SK Hynix ilustra esto claramente.

| Fuente | EPS 2027 | EPS 2028 | Interpretación |
|---|---:|---:|---|
| Consenso de Mercado | 444,359원 | 433,625원 | Normalización moderada en 2028 |
| Korea Investment & Securities | 415,254원 | 495,696원 | Los beneficios continúan creciendo hasta 2028 |
| BNK Investment & Securities | 214,642원 | 66,989원 | Paso rápido por el pico tras 2027 |

Para la misma compañía, las estimaciones de EPS para 2028 oscilan entre 66,989원 y 495,696원. La divergencia no proviene de las previsiones de demanda de 2026, sino de diferentes supuestos sobre <strong>los precios medios de venta de HBM en 2028, el ritmo de expansión de la oferta y la duración del gasto de capital en IA</strong>.

Recalculando el PER actual usando el EPS ponderado por probabilidad de este informe:

| Año | Samsung Electronics | SK Hynix |
|---|---:|---:|
| 2027 | 4.19× | 4.69× |
| 2028 | 5.10× | 5.84× |

Aplicando en sentido inverso el PER razonable ponderado por probabilidad al precio actual de la acción, el EPS implícito que el mercado está descontando es de aproximadamente 31,700원 para Samsung y aproximadamente 245,000원 para SK Hynix —aproximadamente un 52% y un 45% por debajo del consenso de 2027 respectivo. El mercado no está descontando los beneficios de 2027 en sí, sino cuánto tiempo durarán esos beneficios.

## 3. Qué Ha Cambiado en el Ciclo de Memoria — y Qué No

### Qué Ha Cambiado

1. Los servidores de IA, la HBM y los SSD empresariales han elevado la proporción de la demanda empresarial y de centros de datos dentro de la mezcla total.
2. La HBM requiere calificación por parte del cliente, empaquetado avanzado, escalado de rendimiento y contratos a largo plazo, lo que hace que la respuesta de oferta a corto plazo sea más lenta que en el caso de la DRAM estándar.
3. A medida que la HBM absorbe una proporción creciente de los inicios de obleas, la producción de DRAM estándar en esas mismas fábricas disminuye, lo que puede sostener los precios de la DRAM estándar.
4. La financiación por parte de grandes proveedores de nube y operadores de centros de datos de IA adelanta los pedidos reales de memoria, actuando como acelerador.
5. Por el contrario, cuando surgen problemas crediticios, la demanda no se desvanece gradualmente — puede caer abruptamente mediante renegociaciones de contratos y aplazamientos de inversión.

### Qué No Ha Cambiado

1. Los precios elevados en última instancia incentivan la construcción de nuevas fábricas, la mejora de rendimientos, las transiciones a nodos de proceso y las ampliaciones de capacidad por parte de competidores.
2. Los altos precios y márgenes de la HBM incrementan el incentivo para que un segundo proveedor entre al mercado y para que los clientes presionen para reducir costos.
3. Los contratos a largo plazo no eliminan el riesgo de precio — lo convierten en riesgo de precio de renovación y riesgo crediticio del cliente.
4. Aplicar simultáneamente el BPA máximo a un PER elevado es un error de doble optimismo que sitúa tanto las ganancias como los múltiplos en su punto más favorable.

La afirmación de que la HBM ha convertido la memoria en un negocio superior a la DRAM tradicional y la afirmación de que el ciclo de memoria ha sido abolido no son la misma aseveración.

## 4. Modelo de Oferta y Demanda de HBM y el Punto de Inflexión de 2028

En el [Modelo de Oferta-Demanda de HBM 2030 con Verificación Cruzada](/es/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/), reprodujimos el modelo original con `demanda 26.7EB, oferta 10.6EB, déficit 2.52×` en unidades consistentes. La fórmula en sí misma no compara incorrectamente un flujo de demanda con un stock de oferta. El problema reside en que los supuestos de largo horizonte se multiplican en serie.

Entre ellos se incluyen:
- Crecimiento mensual del consumo de tokens
- Escala del modelo, longitud de contexto y expansión del estado de agente
- Ratios de caché KV y de residencia en memoria
- Eficiencia de throughput, cuantización y enrutamiento
- Vida útil de la HBM y migración de cargas de inferencia a otros tipos de memoria
- Volúmenes de producción alcanzables y rendimiento de empaquetado entre los tres principales fabricantes de memoria

Por este motivo, el déficit 2.52× en 2030 debe tratarse como un escenario de estrés alcista y no como un caso base. Derivar de nuevo los supuestos centrales alineados a cada uno de los caminos P1–P4 arroja los siguientes resultados:

| Camino | Multiplicador de Tokens | Escala del Modelo | Eficiencia de Throughput | Eficiencia KV | Residencia HBM | Demanda | Necesidad/Flota |
|---|---:|---:|---:|---:|---:|---:|---:|
| P1 Exceso de Demanda Ordenado | 20× | 4.0× | 12× | 5.0× | 65% | 16.1EB | 1.52× |
| P2 Estrés Crediticio Localizado y Reconcentración | 18× | 3.5× | 12× | 5.5× | 60% | 12.8EB | 1.21× |
| P3 Ganancias de Eficiencia y Expansión de Oferta | 12× | 2.0× | 14× | 6.0× | 50% | 6.5EB | 0.62× |
| P4 Contracción Crediticia Sistémica | 8× | 2.0× | 14× | 7.0× | 45% | 2.6EB | 0.25× |

A efectos de comparabilidad, la capacidad de oferta se mantiene fija en 10.6EB. Los inicios de obleas de HBM reales, la mezcla de productos, el rendimiento de dados buenos y la capacidad de empaquetado no son públicos, por lo que los valores absolutos no pueden confirmarse.

Al observar el eje temporal, el juicio se simplifica considerablemente.

| Período | Valoración | Confianza |
|---|---|---|
| 2026–2027 | La transición a HBM4 y la demanda de IA superan las ampliaciones de oferta de nuevas fábricas | Alta |
| 2028 | La Línea 1 de SK Hynix en Yongin, Micron ID1/Tongluo y la expansión de HBM de Samsung comienzan a aliviar la oferta | Media-Alta |
| 2029–2030 | Es más probable que el déficit restante se estreche que que se profundice | Media |
| Déficit 2.5× en 2030 | Requiere que múltiples supuestos alcistas se cumplan simultáneamente | Baja |

La decisión de inversión no depende, por tanto, de si se produce el auge de 2027. El punto de inflexión es si la oferta adicional que entre en funcionamiento en 2028 supera las calificaciones de los clientes, y si ese momento coincide con ganancias de eficiencia en inferencia y con un endurecimiento de la financiación de los centros de datos de IA.

## 5. Contratos a Largo Plazo de SK Hynix y la Curva de Beneficios

El informe de SK Hynix de Korea Investment & Securities del 13 de julio atribuye el incumplimiento del consenso del segundo trimestre no al colapso de la demanda, sino a un desfase temporal en la forma en que los cambios en la mezcla de productos HBM y la fijación de precios de los contratos de suministro a largo plazo se trasladan a los resultados reportados.

| Partida | 2026F | 2027F | 2028F |
|---|---:|---:|---:|
| Ingresos | 32.83조원 | 48.77조원 | 58.53조원 |
| Beneficio Operativo | 24.51조원 | 37.45조원 | 44.70조원 |
| BPA | 292,068원 | 415,254원 | 495,696원 |
| ROE | 94.5% | 65.4% | 46.5% |

Los supuestos sobre HBM también son agresivos.

| Métrica HBM | 2026F | 2027F |
|---|---:|---:|
| Crecimiento en Bits | +23.0% | +31.2% |
| PVM | $1.60/Gb | $2.82/Gb |
| Crecimiento PVM | -2.5% | +76.3% |
| Ingresos | 3.71조원 | 8.30조원 |
| Crecimiento de Ingresos | +28.0% | +123.6% |

Los principales ajustes de estimaciones dentro del informe incluyen:

- Las ventas de HBM4 comienzan en el tercer trimestre de 2026, pero la mayor inflexión en beneficios se modela en el cuarto trimestre, cuando el PVM de HBM sube un `+52% intertrimestral`.
- En comparación con las estimaciones de mayo, el PVM de DRAM estándar no-HBM para 2026–2027 se recortó aproximadamente un 16%.
- Los ingresos por HBM de 2026 se elevaron un 17%.
- El volumen de envíos de HBM de 2027 se mantuvo sin cambios mientras el PVM se redujo un 5%.
- Los volúmenes de envío de NAND y sus precios fueron revisados al alza.

Este informe no es una retractación de la tesis de crecimiento a largo plazo de la HBM. Es una revisión que reduce la elasticidad de precio a corto plazo de la DRAM estándar y retrasa el momento en que la economía del HBM4 se refleja en los resultados reportados.

### Por Qué los Contratos a Largo Plazo No Deben Tomarse al Pie de la Letra

1. Los suelos y techos de precio a nivel contractual, las obligaciones mínimas de compra y las condiciones de pago anticipado no se divulgan públicamente.
2. Los informes que señalan que los contratos no tienen "techo de precio" no pueden por sí solos confirmar que los precios suban cada año — es necesario saber si la fijación de precios está vinculada a las tasas al contado y con qué frecuencia se reajusta.
3. Los contratos a largo plazo aseguran volúmenes y relaciones con clientes, pero no eliminan el riesgo de renegociación, incumplimiento o deterioro crediticio del cliente.
4. La DRAM estándar no-HBM y la NAND fuera de esos contratos siguen plenamente expuestas al ciclo de precios de los productos básicos.
5. Si el rendimiento del HBM4 es bajo, los envíos y las ganancias incrementales de SK Hynix podrían igualmente quedarse cortos incluso si el mercado permanece con oferta insuficiente.

El mayor beneficio de los contratos a largo plazo no es la eliminación del ciclo, sino <strong>extender la duración de los beneficios y convertir la forma del riesgo</strong>.

## 6. Cómo los Flujos de Financiamiento de Infraestructura de IA Se Traducen en Pedidos de Memoria

La demanda de memoria en IA no está impulsada únicamente por el tirón tecnológico. La actividad de financiamiento de los operadores de centros de datos genera pedidos anticipados, y cuando las condiciones financieras se endurecen, las brechas en los pedidos pueden surgir de forma abrupta.

```text
Expectativas crecientes sobre IA
  -> Inversión en centros de datos cloud/IA y expansión de contratos a largo plazo
  -> Capex anticipado en GPU, HBM, energía y centros de datos
  -> Apreciación de activos, ingresos y valor empresarial
  -> Financiamiento adicional mediante deuda y capital
  -> Programas de capex de mayor envergadura

Dirección inversa
Demora en la monetización o mayores costos de refinanciamiento
  -> Renegociación de contratos / retrasos en la expansión
  -> Brechas en los pedidos de memoria
  -> Caída de ASP y precio de la acción
  -> Deterioro del valor colateral y las condiciones de financiamiento
  -> Mayor reducción del capex
```

Las cifras confirmadas a partir de divulgaciones públicas son sustanciales.

| Elemento | Valor Confirmado | Interpretación |
|---|---:|---|
| Oracle Free Cash Flow AF2026 | -$23.7B | El capex de IA a gran escala supera la generación de caja |
| Financiamiento mediante deuda de Oracle | $43B | Financiamiento externo intensivo para inversión en IA |
| Financiamiento mediante capital de Oracle | $5B | La deuda sola es insuficiente para cubrir la inversión |
| Oracle RPO | $638B | Los contratos a largo plazo ofrecen alta visibilidad de ingresos |
| Prepagos de clientes y provisión directa de GPU de Oracle | $75B | Los clientes finales comparten el riesgo de inversión |
| Deuda total de CoreWeave (fin de 2025) | $21.6B | Alto apalancamiento financiero en centros de datos de IA |
| Nuevo DDTL 4.0 de CoreWeave | $8.5B | Financiamiento adicional para continuar la expansión |
| Umbral DSCR de CoreWeave | Mínimo 1.15× | La verificación de refinanciamiento completo comienza a más tardar tras el 30 de junio de 2027 |

Los endeudamientos detallados de CoreWeave a fin de 2025 comprendían aproximadamente $5.04B en DDTL 2.0, aproximadamente $2.74B en DDTL 2.1, aproximadamente $1.55B en DDTL 1.0, aproximadamente $0.34B en DDTL 3.0, y aproximadamente $4.17B en arrendamientos financieros de equipos y software. El DDTL 4.0, suscrito en marzo de 2026, asciende a $8.5B.

Estas cifras no implican que la demanda de IA sea ficticia. Los contratos, las GPU, la infraestructura energética y los centros de datos son reales. No obstante, si el flujo de caja no logra mantener el ritmo de los costos de financiamiento en 2027–2028, es probable que los operadores más débiles vendan activos para ser absorbidos por los grandes proveedores de nube.

Esta es la razón por la que la probabilidad asignada a <strong>P2 — estrés localizado seguido de reconcentración de activos entre los hyperscalers</strong> — supera a la del colapso sistémico P4. En P2, los pedidos de memoria no desaparecen, pero una brecha de uno o más trimestres es plausible.

## 7. Árbol de Probabilidad Condicional P1–P4

Las probabilidades finales se derivan de la secuencia `demanda real → verificación financiera → oferta/eficiencia → absorción de activos`, y no de las frecuencias históricas de los ciclos de memoria.

```text
Monetización de IA y Verificación de Refinanciamiento 2028
  Aprobado 50%
    ├─ P1 Exceso de demanda sostenido 70%               = 35%
    └─ P3 Normalización de eficiencia/oferta 30%        = 15%
  Estrés 50%
    ├─ P2 Estrés localizado/reconcentración 80%         = 40%
    └─ P4 Contracción crediticia sistémica 20%          = 10%
```

La división inicial 50/50 no es un prior estadístico. Es un punto de partida neutral que refleja el hecho de que la demanda real y los contratos son sólidos, pero la verificación financiera aún no está completa. Calcular probabilidades con una precisión de un punto porcentual a partir de los datos actuales generaría una falsa precisión — los ajustes se realizan únicamente en incrementos de 5 puntos porcentuales.

### Evidencia que Respalda la Aprobación de la Verificación vs. el Estrés Financiero

| Evidencia a favor de la Aprobación de la Verificación | Evidencia a favor del Estrés Financiero |
|---|---|
| Desfase temporal en la rampa de producción masiva de HBM hasta 2027 | Oracle AF2026 FCF -$23.7B, financiamiento mediante deuda $43B |
| Oracle RPO $638B, prepagos de clientes y provisión directa de GPU $75B | Deuda total de CoreWeave $21.6B, nuevo DDTL $8.5B |
| Los contratos a largo plazo y prepagos de HBM aumentan la visibilidad de pedidos | Verificación del DSCR de CoreWeave 1.15× tras mediados de 2027 |
| Inversión real en centros de datos por parte de los grandes proveedores de nube | Prima de riesgo creciente en bonos de IA a largo plazo |

La división 70/30 entre P1 y P3 en la rama de aprobación de la verificación refleja el hecho de que hasta 2027 persisten cuellos de botella en calificación, rendimiento y empaque, mientras que del lado de la memoria, MoE, MLA, compresión KV, enrutamiento y descarga pueden escalar simultáneamente a partir de 2028.

La división 80/20 entre P2 y P4 en la rama de estrés también es clara. Las GPU y los centros de datos no son activos que desaparecen — los hyperscalers con flujo de caja sólido pueden adquirirlos y redistribuirlos. Dado que las reducciones simultáneas de capex, múltiples incumplimientos de covenants y deterioros de contratos a largo plazo de HBM no se han materializado aún de forma conjunta, P4 se trata como un riesgo de cola del 10%.

### Registro de Evidencias

| Evidencia | P1 | P2 | P3 | P4 | Evaluación |
|---|---:|---:|---:|---:|---|
| Retraso en oferta de HBM hasta 2027 | ++ | + | - | -- | La escasez persiste |
| Expansión de oferta de los 3 principales fabricantes de memoria post-2028 | - | 0 | ++ | 0 | Vía independiente de P3 |
| Expansión de CXMT en DDR5/LPDDR para clientes | - | - | ++ | 0 | Limita el techo de precio de commodities antes del HBM |
| Rampa de NAND de capas altas de YMTC y adopción por clientes | - | - | ++ | 0 | Presión sobre el mix de NAND de Samsung y SSD empresarial primero |
| Calificación de clientes de HBM/memoria para servidores de China | -- | - | ++ | 0 | Si se confirma, desplaza de P1 a P3 |
| RPO de Oracle y GPU provistas por clientes | + | + | 0 | - | La demanda es real; amortigua el contagio |
| FCF negativo de Oracle y gran financiamiento | - | ++ | 0 | + | Riesgo de estrés crediticio localizado |
| Deuda de CoreWeave y verificación del DSCR | - | ++ | 0 | + | Inflexión financiera 2027–2028 |
| Prima de riesgo creciente en bonos de IA a largo plazo | -- | ++ | 0 | + | Desplaza 5pp de P1 a P2 |
| Ganancias de eficiencia en inferencia y descarga | - | 0 | ++ | 0 | Evidencia insuficiente aún a nivel de producción |
| Capacidad de absorción de activos de los hyperscalers | 0 | ++ | 0 | -- | Por qué P2 supera a P4 |

`++` y `--` indican solo dirección y no son razones de verosimilitud estadística.

### Historial de Revisión de Probabilidades

| Paso | P1 | P2 | P3 | P4 | Fundamento |
|---|---:|---:|---:|---:|---|
| Inicial | 40% | 35% | 15% | 10% | Predominio de la escasez física de oferta, riesgo financiero localizado, vía oferta/eficiencia |
| Debilidad de bonos de IA a largo plazo reflejada | 35% | 40% | 15% | 10% | Desplazamiento de 5pp de P1 a P2; sin evidencia de contagio |
| Revisión de capex de hyperscalers | 35% | 40% | 15% | 10% | La ejecución de demanda y los efectos de concentración de activos se compensan |
| Revisión de escenario de IA a largo plazo | 35% | 40% | 15% | 10% | 2027–2028 sin cambios; solo la probabilidad de P3 post-2030 se amplía |
| Revisión de la vía de oferta de China | 35% | 40% | 15% | 10% | Riesgo de oferta de commodities reflejado; evidencia de calificación de clientes HBM insuficiente |

### Rangos de Incertidumbre de Probabilidades y Reglas de Revisión

| Vía | Central | Rango de Incertidumbre | Señales Fuertes que Desplazarían la Estimación Central |
|---|---:|---:|---|
| P1 | 35% | 25–45% | Dos o más hyperscalers elevan la guía de capex; los costos de financiamiento se estabilizan; los contratos a largo plazo se refuerzan |
| P2 | 40% | 30–50% | Evento de estrés de un operador débil con absorción de activos por parte de un hyperscaler |
| P3 | 15% | 10–25% | Expansión de oferta de los 3 principales o de China confirmada en volumen; el consumo de HBM por token disminuye |
| P4 | 10% | 5–15% | Múltiples defaults de operadores, dos o más recortes de capex, y deterioros de contratos a largo plazo ocurren simultáneamente |

- Un solo artículo de prensa o anécdota justifica solo un ajuste de 0–2pp.
- Una única señal fuerte proveniente de un filing o reporte de resultados corporativo justifica como máximo un ajuste de 5pp.
- Dos o más señales fuertes independientes en la misma dirección justifican un desplazamiento de 5–10pp.
- El estrés crediticio localizado desplaza la probabilidad de P1 a P2; la evidencia de contagio la desplaza de P2 a P4; la evidencia de oferta/eficiencia la desplaza de P1 a P3.

## 8. Escenarios Finales y Presión sobre el Precio del HBM

| Trayectoria | Prob. | Estado 2028 | Necesidad/Flota 2030 | Presión sobre Precio HBM | Resultado Clave |
|---|---:|---|---:|---:|---|
| P1 Exceso de Demanda Ordenado | 35% | Ajustado o equilibrado | 1,3–1,8× | Plano a -10% | El precio contractual mínimo se mantiene; las ganancias por HBM se estabilizan |
| P2 Estrés Crediticio Localizado y Reconcentración | 40% | Brecha de pedidos, holgura moderada de oferta | 0,9–1,3× | -15 a -30% | Los operadores débiles salen; los hiperescaladores absorben activos |
| P3 Ganancias de Eficiencia y Expansión de Oferta | 15% | Creciente superávit de oferta | 0,6–0,9× | -20 a -35% | El uso de tokens crece pero la prima HBM se comprime |
| P4 Contracción Crediticia Sistémica | 10% | Recortes de capex y corrección de inventarios | 0,3–0,6× | -40 a -55% | Renegociación de contratos de largo plazo, recortes de producción, cancelaciones de capex, intervención de política |

Manteniendo constantes todas las demás variables, desplazar 10 puntos porcentuales fuera de P2 modifica los valores terminales de 2028 de la siguiente manera:

| Desplazamiento de Probabilidad | Variación en Valor Terminal Samsung | Variación en Valor Terminal SK Hynix | Significado |
|---|---:|---:|---|
| 10pp de P2 a P1 | +21.800원 | +227.000원 | Mayor probabilidad de suboferta sostenida |
| 10pp de P2 a P3 | -7.500원 | -70.000원 | La economía de IA crece pero la prima HBM se comprime |
| 10pp de P2 a P4 | -16.800원 | -132.000원 | Contagio del estrés localizado hacia riesgo sistémico |

SK Hynix es más sensible a cada desplazamiento de probabilidad. Incluso utilizando las mismas probabilidades centrales, las bandas de error de valoración y la volatilidad del precio de la acción de SK Hynix son mayores debido a su mayor concentración en HBM.

## 9. La Expansión de Oferta China es una Variable en Todas las Trayectorias, No un Escenario Independiente

El crecimiento de capacidad de CXMT y YMTC no constituye un quinto escenario independiente de P1–P4. Es una variable de oferta que altera los precios a nivel de producto y la cuota de mercado dentro de cada trayectoria.

| Etapa de Avance China | Mercado Afectado Primero | Samsung Electronics | SK Hynix | Asignación de Escenario |
|---|---|---|---|---|
| Expansión doméstica CXMT de DDR4/DDR5/LPDDR | DRAM de commodity | Presión sobre ASP y mezcla de producto | Impacto directo relativamente limitado | BPA recortado en todas las trayectorias; probabilidades sin cambio |
| Calificación de clientes PC globales por CXMT | DDR5/LPDDR de cliente global | Presión sobre techo de ASP y cuota simultáneamente | Exposición a clientes en riesgo | Riesgo al alza en P3 |
| Penetración china de RDIMM de servidor de gama baja | DRAM de servidor estándar | Presión parcial en la mezcla de servidores | DRAM fuera de servidores de IA en riesgo | Revisión al alza de P3 |
| Rampa NAND de alta capa YMTC y adopción por clientes | NAND de consumo/SSD empresarial | Mayor presión en cuota NAND y margen | Solidigm y SSD empresarial en riesgo | Reducción de BPA y múltiplo en P3 |
| Producción en masa de HBM chino y calificación por clientes de IA | HBM | Compensación parcial por recuperación de cuota HBM | Gran riesgo sobre prima de escasez y cuota | Desplazamiento de 5–10pp de P1 a P3 |
| Rampa china y desaceleración global del capex en IA concurrentes | Toda la memoria | Presión combinada en commodity/NAND/HBM | Presión combinada en HBM/DRAM | Vigilar contagio de P3 a P4 |

En 2026–2027, es más probable que CXMT limite el techo de precio del DDR5 de cliente y el LPDDR que socavar directamente los precios del HBM. YMTC podría de manera similar intensificar la competencia en precios en el NAND de consumo y algunos SSD empresariales primero.

Para que China emerja como una amenaza directa al HBM, la producción de die DRAM por sí sola es insuficiente. Se requieren TSV bonding, apilamiento, integración de base-die, empaquetado avanzado y calificaciones repetidas de producción en masa por parte de clientes de IA.

Las siguientes señales deben confirmarse antes de que la expansión de capacidad china se incorpore numéricamente en cantidades significativas:

1. El DDR5/LPDDR de CXMT es adoptado en volumen por fabricantes globales de PC a precios más de un 20% inferiores a los de los tres principales proveedores de memoria.
2. CXMT obtiene calificación más allá de los PC de consumo hacia PC empresariales y RDIMM de servidor.
3. El NAND de alta capa de YMTC se confirma mediante volúmenes reales de envío y contratos con clientes de SSD empresarial — no solo mediante objetivos declarados.
4. El HBM chino avanza más allá de la calificación de muestras hacia calificaciones repetidas de producción en masa por parte de clientes de aceleradores de IA.
5. Se observa simultáneamente crecimiento de oferta y caída en precios de DRAM/NAND de commodity entre los tres principales proveedores durante dos o más trimestres consecutivos.

## 10. Samsung Electronics: BPA y Valor Razonable por Escenario

| Año | Escenario | BPA | PER Razonable | Valor Terminal |
|---|---|---:|---:|---:|
| 2027 | P1 | 65.000원 | 8,5× | 552.500원 |
| 2027 | P2 | 62.000원 | 8,0× | 496.000원 |
| 2027 | P3 | 58.000원 | 7,5× | 435.000원 |
| 2027 | P4 | 45.000원 | 7,0× | 315.000원 |
| 2028 | P1 | 68.000원 | 8,5× | 578.000원 |
| 2028 | P2 | 45.000원 | 8,0× | 360.000원 |
| 2028 | P3 | 38.000원 | 7,5× | 285.000원 |
| 2028 | P4 | 24.000원 | 8,0× | 192.000원 |

No se asigna a Samsung un PER base superior a 9× porque la reducción de pérdidas en fundición aún no ha sido confirmada. Un múltiplo de 8,5× en P1 solo resulta alcanzable si la recuperación de cuota en HBM, los precios de DRAM/NAND de commodity y la normalización de la fundición operan de forma conjunta.

Se aplica un múltiplo de 8,0× en P4 para evitar el error de doble descuento de multiplicar un BPA de valle por un PER también deprimido. En un escenario de recesión real, el BPA normalizado, el efectivo neto y el valor en libros deben considerarse conjuntamente.

## 11. SK Hynix: BPA y Valor Razonable por Escenario

| Año | Escenario | BPA | PER Razonable | Valor Terminal |
|---|---|---:|---:|---:|
| 2027 | P1 | 430.000원 | 9,0× | 3.870.000원 |
| 2027 | P2 | 405.000원 | 7,0× | 2.835.000원 |
| 2027 | P3 | 370.000원 | 6,0× | 2.220.000원 |
| 2027 | P4 | 250.000원 | 5,5× | 1.375.000원 |
| 2028 | P1 | 470.000원 | 9,0× | 4.230.000원 |
| 2028 | P2 | 280.000원 | 7,0× | 1.960.000원 |
| 2028 | P3 | 210.000원 | 6,0× | 1.260.000원 |
| 2028 | P4 | 80.000원 | 8,0× | 640.000원 |

El múltiplo de 9× en P1 presupone cuota de mercado en HBM, condiciones de contratos de largo plazo, ROE elevado y una reclasificación estructural de SK Hynix como activo estratégico de IA. Mantener este múltiplo hasta 2028 exige la defensa confirmada de cuota en HBM4E, la renegociación de precios en contratos de largo plazo y actividad de retribución al accionista.

El precio objetivo de 3.800.000원 de Korea Investment & Securities aplica un PBR de 6,0× al BPS a 12 meses vista — por encima del máximo histórico de la banda de 5,0× citado en el mismo informe. Un objetivo de 3.800.000원 requiere, por tanto, no solo la entrega de resultados, sino una reclasificación estructural del negocio de memoria.

En P2 y P3, la concentración en HBM pasa de ser una ventaja a convertirse en una vulnerabilidad. Cuando el ASP cae, las ganancias y los múltiplos pueden comprimirse simultáneamente.

## 12. Resultados Ponderados por Probabilidad y Comparación Ajustada por Riesgo

| Año | Compañía | BPA Pond. por Prob. | PER Razonable Combinado | Valor Terminal Pond. por Prob. | VA a Descuento Anual del 11% | vs. Precio Actual |
|---|---|---:|---:|---:|---:|---:|
| 2027 | Samsung Electronics | 60.750원 | 8,04× | 488.525원 | 421.385원 | +65,6% |
| 2027 | SK Hynix | 393.000원 | 7,53× | 2.959.000원 | 2.552.333원 | +38,3% |
| 2028 | Samsung Electronics | 49.900원 | 8,18× | 408.250원 | 317.246원 | +24,7% |
| 2028 | SK Hynix | 316.000원 | 7,97× | 2.517.500원 | 1.956.316원 | +6,0% |

De estos resultados se derivan cuatro observaciones:

1. Considerando únicamente el horizonte de 2027, ambas compañías presentan valores ajustados por riesgo superiores a los precios actuales.
2. Una vez descontada la probabilidad de normalización en 2028, el margen de seguridad de Samsung es más amplio.
3. El valor presente de SK Hynix en 2028 es solo un 6% superior al precio de la acción actual. Una proporción significativa del retorno esperado depende de que P1 se mantenga.
4. La memoria de commodity de Samsung, la fundición y la posición de efectivo neto proporcionan un amortiguador parcial a la baja en P2 y P3.

Lo que el mercado ya conoce bien es la suboferta de HBM y los precios más altos de memoria. Lo que podría estar incorrectamente valorado en dos direcciones:

- Si la recuperación de cuota HBM de Samsung coincide con la recuperación de precios del DRAM/NAND de commodity, tanto las ganancias como los múltiplos podrían mejorar de forma simultánea.
- Si los contratos de largo plazo y el HBM4E de SK Hynix defienden los precios mínimos y la cuota incluso tras las adiciones de oferta posteriores a 2028, el descuento actual por normalización podría ser excesivo.

A la inversa, el mercado podría tener razón si la oferta, la eficiencia y las condiciones crediticias mejoran simultáneamente en 2028, truncando prematuramente las ganancias máximas.

## 13. Cómo Interpretar la Demanda de IA a Largo Plazo Más Allá de 2030

[AI 2040 Plan A](https://ai-2040.com/?choices=plan-a-root) presenta un camino desde aproximadamente 20 millones de H100e en 2026 hasta 60.000 millones de H100e para 2034, con un consumo de potencia de cómputo de IA que alcanzaría los 5TW en 2034. Sin embargo, el propio documento describe esto como un escenario de política, no como una previsión de mejor estimación, y señala que ciertas variables fueron ajustadas en consonancia con la narrativa.

Los escenarios a largo plazo, por lo tanto, no se incorporan directamente a las estimaciones de BPA para 2027–2028.

| Período | P1 Exceso de Demanda | P2 Reconcentración | P3 Crecimiento de Volumen / Normalización de Precios | P4 Colapso | Estado |
|---|---:|---:|---:|---:|---|
| 2026–2028 | 35% | 40% | 15% | 10% | Probabilidades del análisis actual |
| Línea base condicional post-2030 | 25% | 35% | 30% | 10% | Juicio a largo plazo; no es una probabilidad estadística |

Si la IA y la robótica incrementan la eficiencia del diseño de chips, la construcción de fábricas y la producción, la demanda total de bits de memoria podría crecer mientras la prima de escasez específica del HBM se estrecha. <strong>Por lo tanto, la expansión del tamaño de mercado del HBM y la expansión del PER a largo plazo deben evaluarse por separado.</strong>

A medida que la demanda de memoria a largo plazo crece, el universo de oportunidades se amplía no solo para el HBM, sino también para la DRAM de commodities, NAND, SSD empresariales, controladores, CXL, energía, refrigeración e interconexiones. Esto representa una ventaja relativa para Samsung, dada su cartera de productos más amplia.

## 14. Qué Debe Materializarse Para que Este Análisis se Sostenga

### Samsung Electronics

1. Las certificaciones de clientes de HBM4 y HBM4E deben convertirse en volúmenes reales de producción en masa y cuota de ingresos.
2. La recuperación de precios de contrato en DRAM y NAND de commodities debe compensar los costes de inversión en HBM, bonificaciones y provisiones.
3. Las pérdidas de la división de fundición deben reducirse y comenzar a contribuir de forma significativa a los resultados de 2027–2028.
4. La caja neta y la capacidad de retribución al accionista deben mantenerse a pesar del elevado capex.

### SK Hynix

1. La cuota de HBM4E y los suelos de precio de los contratos a largo plazo deben sostenerse incluso cuando Samsung y Micron amplíen su oferta.
2. La revisión de precios del HBM que comienza en el cuarto trimestre de 2026 debe orientarse hacia la media de 2027 de $2,82/Gb.
3. La debilidad en el rendimiento de TSV y apilamiento debe demostrarse temporal y atribuible a los costes de transición de producto.
4. El elevado flujo de caja libre debe destinarse a la retribución al accionista y a la política de capital, no únicamente a la expansión de capacidad.

## 15. Señales de Riesgo e Indicadores Adelantados

| Riesgo | Indicador Adelantado | Impacto en Samsung | Impacto en SK Hynix | Ajuste del Análisis |
|---|---|---|---|---|
| Renegociación de contratos a largo plazo de HBM | Debilitamiento de suelo de precios, pagos anticipados y compras mínimas | Moderado | Muy elevado | P2/P4 al alza |
| Recorte de guidance de capex de los hyperscalers | Dos o más recortes de guidance simultáneos | Elevado | Muy elevado | P2/P4 al alza |
| Evento de refinanciación en centros de datos de IA | Condiciones de los covenants de CoreWeave y coste de financiación, financiación de Oracle | Moderado | Elevado | P2 al alza; P4 al alza si hay contagio |
| Expansión acelerada de la oferta | Incremento de la producción de HBM con capacidad de volumen de Samsung/Micron | Positivo para el alcance de HBM; negativo para precios | Muy negativo | P3 al alza |
| Mejora pronunciada en eficiencia de inferencia | Caída de bits de HBM por token | La amplia cartera de productos ofrece cobertura parcial | Negativo | Múltiplo de HBM a la baja |
| Expansión de la oferta de commodities de China | Precios, cuota y certificaciones de clientes globales de CXMT/YMTC | Más negativo para DRAM/NAND de commodities | Client DRAM y Solidigm bajo presión | Reducción de BPA a nivel de producto |
| Desafío chino en HBM | TSV/apilamiento/die base/envasado/certificación de clientes | Compensación parcial del valor de alcance en HBM | Muy negativo para la prima de escasez | Desplazamiento de P1 a P3 |
| Fracaso en la normalización de fundición | Pérdidas continuadas, sin mejora de rendimiento | Riesgo específico de Samsung | Impacto limitado | Reducción del múltiplo P1 de Samsung |

### Señales Alcistas

- Contratos a largo plazo de HBM para 2028 con mayores volúmenes y precios, y mayor diversificación de clientes
- Estabilización temprana del rendimiento de HBM4E y los volúmenes de producción en masa
- Confirmación simultánea del aumento de cuota de HBM de Samsung y la reducción de pérdidas en fundición
- Ingresos de servicios de IA y flujo de caja creciendo más rápido que los contratos de recursos de cómputo
- Los plazos de entrega y asignaciones de HBM se mantienen incluso cuando la expansión de oferta se retrasa
- El plan de retribución al accionista de SK Hynix adquiere carácter concreto

### Señales Bajistas

- La caída del ASP de HBM y la reducción del volumen de envíos se producen simultáneamente
- Dos o más grandes hyperscalers reducen sus tasas de crecimiento de capex
- Renegociación, incumplimiento o deterioro de pagos anticipados en contratos a largo plazo
- Acumulación de inventario de memoria e inversión del precio spot frente al precio de contrato
- El consumo real de HBM por token de los servicios de IA cae más del 20% durante dos trimestres consecutivos
- El aumento del suministro en volumen de Samsung/Micron coincide con la disminución de la prima del HBM

De forma mensual, los indicadores a seguir conjuntamente son: precios de contrato y pagos anticipados de HBM4/4E, volúmenes y rendimientos de los tres principales fabricantes de memoria, plazos de entrega en packaging avanzado, capex y flujo de caja de los hyperscalers, costes de financiación de Oracle y CoreWeave, ingresos de los ODM de servidores de Taiwán, y precios de contrato e inventario de DRAM/NAND.

## 16. Interpretación de la Inversión en Términos Relativos

Los dos valores no representan vías equivalentes para aprovechar el mismo ciclo alcista de memoria.

| Escenario | Samsung Electronics | SK Hynix |
|---|---|---|
| P1 en Fortalecimiento | Alcance en HBM y viento de cola en memoria de commodities | Mayor apalancamiento en beneficios por cuota de HBM y contratos a largo plazo |
| P2 en Aviso | La diversificación del negocio y la caja neta ofrecen defensa parcial | Mayor sensibilidad a las brechas de pedidos y la compresión de múltiplos |
| P3 en Fortalecimiento | La amplia gama de productos de memoria y la ejecución en fundición ofrecen cobertura parcial | Exposición directa a la compresión de la prima del HBM |
| P4 en Aviso | El deterioro absoluto es inevitable, pero la defensa relativa es posible | Mayor riesgo de caída simultánea de beneficios y múltiplos |

Desde una perspectiva ajustada al riesgo, Samsung ofrece una elección más amplia y defensiva. SK Hynix presenta mayor apalancamiento en beneficios en P1, pero su valoración se ajusta con mayor rapidez cuando cambian las condiciones de oferta, eficiencia y crédito.

Los valores de equipamiento y materiales tampoco deben agruparse indiscriminadamente. Es necesario separar las empresas de equipamiento expuestas a brechas de pedidos de los proveedores de consumibles y piezas cuyos ingresos siguen las tasas de utilización. Las empresas de equipamiento con órdenes de compra confirmadas y los componentes o materiales con flujos de ingresos recurrentes se adaptan mejor a este marco de escenarios que una cesta temática pura de HBM.

## 17. Conclusión

El auge de la memoria hasta 2027 puede mantenerse como la trayectoria central en las estimaciones de beneficios. Sin embargo, la verdadera prueba para las cotizaciones actuales no es el BPA de 2027, sino la duración de los beneficios más allá de 2028. El argumento de que el déficit de oferta de HBM ha durado más que los ciclos anteriores y el argumento de que las empresas de memoria merecen un múltiplo de escasez permanentemente elevado no son lo mismo.

Samsung Electronics combina simultáneamente el potencial de alcance en HBM, la DRAM/NAND de commodities, las operaciones de fundición y la caja neta, ofreciendo el alza de P1 y una defensa relativa a la baja en P2–P4. La cuota de HBM y los contratos a largo plazo de SK Hynix proporcionan el mayor apalancamiento en beneficios en P1, pero si las condiciones de oferta, eficiencia y financiación se normalizan, los beneficios y los múltiplos pueden comprimirse conjuntamente.

Los resultados ponderados por probabilidad actuales señalan: <strong>hasta 2027, ambas compañías ofrecen un alza significativa; con perspectiva hasta 2028, el margen de seguridad ajustado al riesgo de Samsung es más amplio.</strong> Para que SK Hynix experimente una revalorización adicional, se necesita la confirmación de que el rendimiento de HBM4E, los términos de los contratos a largo plazo de 2028 y la financiación de infraestructura de IA continúan sustentando P1.

## Aspectos que Aún No Pueden Confirmarse desde Fuentes Públicas

1. BPA por segmento de Samsung Electronics para 2027–2028 y sensibilidad a la normalización de la fundición
2. Ponderación de clientes en contratos a largo plazo de SK Hynix, fórmula de revisión de precios y términos de pagos anticipados y compras mínimas
3. Inputs de obleas dedicadas a HBM de los tres principales fabricantes de memoria, rendimiento de die buenos y apilamiento, y volúmenes producibles por cliente
4. Composición del capex de los hyperscalers para 2028 entre flujo de caja interno, bonos corporativos y financiación de proyectos
5. Calendarios de refinanciación de CoreWeave y Oracle y margen disponible en los covenants
6. Cambios en capacidad, ancho de banda y tasa de residencia en memoria de HBM4E por generación y por acelerador
7. Volúmenes de envío reales de CXMT/YMTC, certificaciones de clientes globales y sensibilidad de beneficios a nivel de producto

## Fuentes Principales

- [Korea Investment & Securities, SK Hynix Vista Previa 2T26, 2026-07-13](https://vo.la/fd9udR9)
- [Korea Investment & Securities, "El Comienzo Empieza Ahora," 2026-05-20](https://vo.la/jBPy7zV)
- [Korea Invest Insights, Modelo de Oferta y Demanda HBM 2030: Verificación Cruzada](/es/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
- [AI 2040, Plan A](https://ai-2040.com/?choices=plan-a-root)
- [AI 2040, Suplemento de Cómputo](https://ai-2040.com/supplements/compute-supplement)
- [AI 2040, Economía del Plan A](https://ai-2040.com/supplements/economics-of-plan-a)
- [Oracle Resultados FY2026](https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/)
- [CoreWeave Formulario 10-K 2025](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm)
- [CoreWeave DDTL 4.0 Formulario 8-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/crwv-20260330.htm)

Las probabilidades de escenario y los valores razonables contenidos en este informe son estimaciones analíticas basadas en información públicamente disponible y no constituyen asesoramiento de inversión personalizado. Las decisiones de inversión reales deben considerar de forma independiente la volatilidad de precios, el horizonte de inversión, la fiscalidad, el riesgo cambiario y la tolerancia individual a las pérdidas.
