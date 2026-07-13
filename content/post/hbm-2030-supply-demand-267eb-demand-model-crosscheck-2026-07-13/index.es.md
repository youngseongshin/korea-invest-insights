---
title: "Investigación profunda de oferta-demanda de HBM 2030: diseccionando el modelo de demanda de 26,7EB frente al calendario de capacidad"
slug: "hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13"
date: 2026-07-13T11:00:00+09:00
description: "Reproducimos de forma independiente la afirmación de 26,7EB de demanda frente a 10,6EB de oferta de HBM en 2030 (un déficit de 2,5x), y la contrastamos con la previsión de 24x de tokens de Goldman, la contraevidencia de eficiencia de DeepSeek MLA y TurboQuant, y el calendario de capacidad de los Big 3. Análisis de estructura, no recomendación de inversión."
categories: ["Exclusive Analysis", "Tech-Analysis", "Market-Outlook"]
tags: ["HBM", "Oferta-Demanda de Memoria", "AI Memory", "SK Hynix", "Samsung Electronics", "Micron", "KV Cache", "Infraestructura de IA", "Capacidad de Semiconductores"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexto
> Si [HBM, HBF y HBC: Cómo distinguir las tres tecnologías de memoria para IA](/es/post/hbm-hbf-hbc-ai-memory-comparison-2026-06-22/) trató la identidad de esa tecnología, este artículo investiga en profundidad <strong>cómo se encuentran la demanda y la oferta de esa tecnología hasta 2030</strong>. Conviene leerlo junto con [El valor actual y futuro del token de IA: análisis del valor agregado de las empresas de memoria](/es/post/ai-token-value-memory-value-added-2026-07-09/), [Las llamadas de resultados de las grandes tecnológicas de finales de julio y los escenarios para la tesis de memoria](/es/post/big-tech-july-earnings-call-memory-thesis-scenarios-2026-07-07/) y [¿Quién paga el consenso de semiconductores de 2027?](/es/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/). Los hubs relacionados son el [Hub HBM de semiconductores coreanos](/es/page/korea-semiconductor-hbm-kospi-hub/) y el [Hub de Análisis Exclusivo](/es/page/exclusive-analysis-hub/).

## TL;DR

* Reprodujimos de forma independiente, con la fórmula pública, la narrativa que circula en el mercado sobre <strong>una demanda de HBM de 26,7EB en 2030 frente a una oferta de 10,6EB, un déficit de 2,5x</strong>. La aritmética en sí se reproduce. El problema es sobre qué supuestos se sostiene esa cifra.
* 26,7EB no es un error de comparar stock con flujo. Es un valor que convierte tanto la demanda como la oferta en <strong>stock de HBM instalado y en funcionamiento</strong> para compararlas. Pero solo se obtiene si varios supuestos alcistas se cumplen a la vez: token 24x, footprint del modelo 5x, contexto 4x, tasa de retención de KV del 70%.
* Lo verificamos de forma cruzada con tres lentes: (1) la estructura del modelo de demanda, (2) la evidencia alcista de los supuestos de demanda y la contraevidencia de eficiencia tecnológica, y (3) el calendario de ampliación de capacidad de los Big 3. Las tres lentes convergen <strong>sin contradicciones en una sola conclusión</strong>.
* La conclusión <strong>separa la dirección de la magnitud</strong>. `Tensionado hasta 2027` tiene una confiabilidad alta, `mejora de la oferta desde 2028` es coherente con el calendario oficial de ampliación de capacidad, y `un déficit de exactamente 2,5x incluso en 2030` es un escenario con sesgo alcista.
* Este artículo no emite un juicio de compra o mantenimiento sobre ningún valor concreto. Es un análisis que diseca la estructura de oferta y demanda de la industria. \[Alcance\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Marco clave</div>
  <div class="thesis-callout__body">
    El verdadero punto de debate sobre la oferta y demanda de HBM no es "¿habrá un déficit de 2,5x en 2030?", sino que "la dirección del déficit es sólida, pero su magnitud es sensible a los supuestos". Los datos respaldan la tensión de 2027 y la mejora de la oferta en 2028, mientras que la cifra de 2,5x es un escenario alcista que solo se cumple si varios supuestos de demanda coinciden a la vez.
  </div>
</div>

---

## 1. Planteamiento del problema: qué verificamos

En el mercado de memoria para IA circula una narrativa poderosa. Sostiene que la demanda de HBM en 2030 será de 26,7EB (exabytes), mientras que la oferta se quedará en 10,6EB, dejando <strong>un déficit estructural de unas 2,5x</strong>. Esta cifra proviene de un modelo de análisis independiente (Memory Analyst) y se difundió a través de numerosos videos de YouTube e informes.

Esta investigación profunda responde a cuatro preguntas. \[Verificación\]

1. ¿Es internamente consistente la fórmula `26,7EB frente a 10,6EB`?
2. ¿Son razonables los supuestos de demanda a la luz de la evidencia pública y de la estructura del modelo?
3. ¿Persiste el déficit de 2030 incluso al incorporar la ampliación de capacidad de Samsung Electronics, SK Hynix y Micron?
4. ¿Cómo liquida realmente el mercado esta cifra?

Antes de avanzar, para no diluir la conclusión, dejamos algo claro. Este artículo no recalcula el precio actual de la acción ni el múltiplo justo. Solo aborda <strong>la confiabilidad de la dirección y la magnitud de la oferta y la demanda</strong>.

---

## 2. Primera lente: disección del modelo de demanda de 26,7EB

### 2.1 Es una comparación de stock contra stock (despejando un malentendido común)

El primer malentendido que hay que despejar es la crítica de que "la demanda de 26,7EB y la oferta de 10,6EB comparan erróneamente el consumo anual con la producción anual". La verificación muestra que <strong>esto no es un error.</strong> El modelo original compara dos stocks. \[Hecho\]

- <strong>Need</strong>: el stock de HBM que debe estar instalado y encendido para procesar la carga de trabajo de inferencia de IA de ese año.
- <strong>Serving fleet</strong>: el stock de HBM producido en los últimos aproximadamente 5 años que se destina a inferencia, tras aplicar la eficiencia por antigüedad, y que aún no se ha retirado.

Es decir, ambas cifras son stock, no flujo (flow). La estructura del modelo original, `fleet = output de los últimos ~5 años × cuota de inferencia - fricción`, deja explícita esta conversión. En la dimensión stock-flujo, es consistente. \[Inferencia\] Sin embargo, la cuota de asignación a inferencia que convierte el flujo en stock, la vida útil de 5 años y la eficiencia por generación no son estándares de la industria verificados de forma independiente, sino <strong>supuestos del modelo</strong>.

### 2.2 Reproducción directa de la fórmula de demanda de 26,7EB

Reprodujimos de forma independiente la fórmula simplificada publicada por el modelo original, introduciendo tal cual los valores de entrada del caso base (base-case) de 2030.

```text
traffic = 24  (24x frente a 2026, 120 quadrillion de tokens al mes)
replicaIndex = 24^0.90 / 11 = 1.5878

weights = 1.75 × 1.5878 × 5 / 1.75 = 7.939EB
contextBucket = 4 × 1.5 / 4 × 0.70 = 1.05
kv = 1.27 × 24^0.55 × 1.05 = 7.658EB
scratch = (7.939 + 7.658) × 0.15 = 2.340EB

need = (7.939 + 7.658 + 2.340) × 1.10 / 0.74 = 26.66EB ≈ 26.7EB
```

Al desglosar la demanda por componente, el resultado es el siguiente.

| Composición de la demanda 2030 | EB | Proporción |
|---|---:|---:|
| Resident weights (pesos residentes) | 7,94 | 44,3% |
| KV cache | 7,66 | 42,7% |
| Scratch (memoria de trabajo temporal) | 2,34 | 13,0% |
| Subtotal (antes de redundancy/utilization) | 17,94 | 100,0% |
| Necesidad final instalada (×1,10 / 0,74) | 26,66 | - |

\[Hecho\] La aritmética de 26,7EB se reproduce con la fórmula pública. Es importante que los pesos residentes y la caché KV concentren la mayor parte de la demanda, con un 44% y un 43% respectivamente, porque son precisamente estos dos componentes los que serán el blanco directo de las mejoras de eficiencia tecnológica que se analizan más adelante.

\[Bloqueado\] Sin embargo, la calculadora incluye un valor de entrada separado, `frontier/HBM-served share 70%`, y no queda claro en la fórmula simplificada publicada cómo se refleja este valor en los pesos. Hasta que no se realice una auditoría a nivel de código, no damos por aprobado el 26,7EB como un modelo completamente independiente.

### 2.3 Cómo leer correctamente la tasa de crecimiento

El `CAGR a 5 años` que suele citarse habitualmente es un error de cálculo del periodo. De 2026 a 2030 hay 5 observaciones, pero <strong>los periodos de capitalización compuesta son 4</strong>.

| Ítem | 2026 | 2030 | Múltiplo | CAGR correcto a 4 periodos |
|---|---:|---:|---:|---:|
| Necesidad de HBM instalada | 4,8EB | 26,7EB | 5,56x | <strong>53,6%</strong> |
| Serving fleet | 3,75EB | 10,6EB | 2,83x | <strong>29,7%</strong> |

Además, la trayectoria de producción anual de HBM del modelo original, `de 2,8EB en 2024 a 7,6EB en 2030`, arroja un CAGR a 6 periodos del <strong>18,1%</strong>. Como el `serving fleet de 10,6EB` no es producción anual sino un stock acumulado y depreciado de la producción de varios años, ambos conceptos no deben mezclarse. \[Hecho\]

Si la demanda crece un 53,6% anual y el stock de oferta crece un 29,7% anual, la dirección en la que se amplía la brecha es aritméticamente evidente. El problema es cuán sólidos son los supuestos de entrada detrás de estas dos tasas de crecimiento.

---

## 3. Segunda lente: el lado alcista de los supuestos de demanda y su contraevidencia

### 3.1 Evidencia confirmada del lado alcista de la demanda

Existe evidencia real de que la demanda es fuerte. \[Hecho\]

- Goldman Sachs Research proyectó que el consumo mensual de tokens crecerá <strong>24x</strong> entre 2026 y 2030, hasta alcanzar los 120 quadrillion.
- El mismo informe estimó que las consultas diarias a LLM crecerán a una tasa media anual de cerca del 40%, hasta unos 11.000 millones en 2030.
- A medida que evolucionan las generaciones de NVIDIA, la capacidad de HBM por acelerador ha ido en aumento.
- Micron, a fecha de junio de 2026, guio que la demanda de DRAM y NAND supera ampliamente a la oferta y que este estado de tensión <strong>se prolongará más allá de 2027</strong>.
- Micron informó que firmó 16 Acuerdos Estratégicos con Clientes (SCA), que 14 de esos contratos garantizan ingresos acumulados mínimos por unos 100.000 millones de dólares, y que los depósitos de efectivo y compromisos financieros asociados suman 22.000 millones de dólares. No obstante, el HBM es solo una parte de estos contratos, no la totalidad.

### 3.2 Evidencia contraria dentro de la misma fuente

Lo interesante es que el propio informe de Goldman, usado como evidencia alcista, contiene también evidencia en sentido contrario. \[Hecho\]

- Goldman anticipa una escasez de chips a corto plazo, pero también señaló explícitamente que <strong>la industria podría ponerse al día en unos 2 años una vez entre la nueva capacidad de producción</strong>.
- Goldman explicó que el costo por token de inferencia cae un 60-70% al año. La caída de precios aumenta el uso, pero también reduce la carga física de memoria de la misma carga de trabajo.
- De forma decisiva, el 24x de Goldman no es una previsión de demanda de bits de HBM, sino una previsión de <strong>tráfico de tokens</strong>. La conversión `de tokens a sesiones simultáneas, contexto, KV y pesos, y retención en HBM` depende enteramente de supuestos de modelo independientes.

\[Inferencia\] Por lo tanto, la previsión de Goldman respalda el aumento del uso de IA, pero no respalda directamente `un déficit de HBM de 2,5x en 2030`. Esta distinción se omite con frecuencia cuando la narrativa alcista cita a Goldman.

### 3.3 Contraevidencia de la estructura del modelo y de la eficiencia

Los pesos y la caché KV, el núcleo de la fórmula de demanda, son el blanco directo de las mejoras tecnológicas. \[Hecho\]

- El ejemplo de caché KV de `aproximadamente 504 KB por token` del modelo original corresponde al caso de <strong>Llama 3.1 405B</strong>. No es un valor universal para todos los frontier models.
- La familia DeepSeek-V3/R1 eleva considerablemente la eficiencia de KV y de cómputo mediante Multi-head Latent Attention (MLA) y Mixture-of-Experts (MoE).
- TurboQuant, de Google Research, presentó resultados que reducen la memoria KV en <strong>al menos 6x</strong> en benchmarks públicos.

\[Inferencia\] Sin embargo, TurboQuant es un resultado de investigación centrado en la caché KV. No reduce 6x los pesos, el scratch ni la redundancy, y tampoco es un promedio de la industria verificado en cuanto a latencia, throughput y calidad en entornos de producción a gran escala.

Por eso, la conclusión honesta es descartar ambos extremos. `504 KB/token × toda carga de trabajo futura` es una sobreestimación, y `compresión KV de 6x × la totalidad del HBM` es una subestimación. Entre ambos extremos, lo esencial para la demanda futura es <strong>cómo evoluciona la composición entre pesos y KV</strong>.

---

## 4. Tercera lente: verificación cruzada del calendario de ampliación de capacidad de los Big 3

### 4.1 La capacidad de fábrica y la oferta efectiva de HBM son cosas distintas

Un error común al analizar la oferta es convertir directamente las noticias de inicio o finalización de una fábrica en HBM vendible. Entre ambos existen cinco brechas. \[Hecho/Inferencia\]

1. <strong>Aumento del die intensity</strong>: si los dies por stack suben de 12 a 16 capas, los dies necesarios para el mismo número de stacks aumentan cerca de un 33%. Aunque las obleas aumenten, la tasa de crecimiento de los stacks vendibles puede quedar por debajo de eso.
2. <strong>HBM trade ratio</strong>: el HBM consume más recursos de oblea y de proceso que el DRAM de propósito general. Micron también señaló que este ratio aumenta con cada generación, presionando la oferta de non-HBM.
3. <strong>Back-end, rendimiento y certificación</strong>: para convertirse en oferta efectiva hay que superar todo el proceso: good die, apilamiento TSV, base die, empaquetado avanzado (advanced packaging), especificaciones térmicas y de potencia, y certificación del cliente.
4. <strong>Desfase del ramp-up</strong>: la apertura de una cleanroom o el first wafer son distintos del qualified volume que permite reconocer ingresos.
5. <strong>Costo de oportunidad entre productos</strong>: ampliar la producción de HBM puede canibalizar obleas de DRAM de propósito general. Que el HBM aumente no garantiza que el precio total del DRAM se estabilice de inmediato.

### 4.2 Calendario oficial de ampliación de capacidad

Este es el calendario de los Big 3 y de la industria en su conjunto, confirmado con fuentes primarias públicas.

| Empresa/ítem | Confirmación oficial | Interpretación de la contribución real a la oferta |
|---|---|---|
| SK Hynix M15X | Finalización prevista para noviembre de 2025, producción de DRAM y HBM de próxima generación | El eje de ampliación más rápido en 2026-27. El ramp podría ser veloz al aprovechar infraestructura existente |
| SK Hynix Yongin fase 1 | Inversión en equipos de 21,6 billones de wones, apertura anticipada de la primera cleanroom en febrero de 2027 | Instalación desde 2027, con posible expansión del efecto en la oferta desde 2028 |
| SK Hynix Yongin completo | La meta de la primera cleanroom de la cuarta fase es 2033 | Es incorrecto suponer que las 4 fábricas de Yongin en su totalidad entrarán en la oferta de 2030 |
| Samsung Electronics HBM4 | Inicio de producción en masa y envíos comerciales en febrero de 2026, se espera que los ingresos de HBM se tripliquen o más en 2026 | El regreso de Samsung como second-source en 2026-27 es la variable de mayor alivio de oferta |
| Inversión de largo plazo de Samsung Electronics | Unos 2.100 billones de wones en semiconductores entre 2026-2040, unos 1.650 billones en Yongin y complejos existentes, fábricas de HBM en Onyang y Cheonan | La dirección es firme, pero es un envelope hasta 2040. No se traduce directamente en volumen de oferta de 2030 |
| Micron ID1 | First wafer a mediados de 2027 | Considerando la certificación de clientes, las ventas significativas llegarían a fines de 2027-2028 |
| Micron ID2 | First wafer a fines de 2028 | Contribución al alivio de la oferta desde 2029 |
| Micron Tongluo y packaging | Tongluo alcanza envíos significativos en FY2028, la ampliación de HBM packaging comienza en el primer semestre de 2027 | Alivia simultáneamente los cuellos de botella de front-end y back-end |
| SEMI, memoria total | La capacidad de memoria de 300 mm pasaría de 4,1 millones de WPM en 2026 a 4,2 millones de WPM en 2027 | El crecimiento total de la capacidad de obleas es moderado, de apenas un 2,4%. El giro del mix hacia HBM y el crecimiento de bits por nodo importan más |

### 4.3 Veredicto del lado de la oferta

- \[Hecho\] Los Big 3 están realizando, todos ellos, inversiones a gran escala.
- \[Hecho\] 2027 es el año en que empiezan a aumentar las cleanrooms y los first wafers, no el año en que todo el volumen se convierte en qualified output.
- \[Inferencia\] Es probable que el alivio de la oferta se haga visible a partir de 2028 y se intensifique en 2029-30.
- \[Bloqueado\] Con la información pública disponible no se puede determinar si el serving fleet de 2030 será de 10,6EB o de 15EB. El WPM exacto, el mix de productos, el rendimiento (yield) y la capacidad de packaging no son públicos.

---

## 5. Análisis de sensibilidad que integra las tres lentes

Reunimos en una sola tabla de sensibilidad la dirección que señalan las tres lentes. Fijamos el serving fleet de oferta en 10,6EB y recalculamos de forma independiente, con la fórmula pública, solo los supuestos de demanda.

| Escenario | Supuesto modificado | Demanda 2030 | Demanda/oferta | Veredicto |
|---|---|---:|---:|---|
| Base del modelo original | Token 24x, modelo 5x, eficiencia KV 4x, tasa de retención 70% | 26,7EB | 2,52x | Déficit fuerte |
| Footprint del modelo moderado | Múltiplo del modelo de 5x a 2x | 18,5EB | 1,75x | Déficit |
| Mejora de eficiencia KV | Eficiencia KV de 4x a 6x | 22,3EB | 2,10x | Déficit |
| Caída de la tasa de retención de HBM | De 70% a 50% | 22,9EB | 2,16x | Déficit |
| Crecimiento de tokens a la mitad | De 24x a 12x | 16,2EB | 1,53x | Déficit |
| Bear compuesto | Token 12x, modelo 2x, eficiencia KV 6x, retención 50%, throughput 14x | 6,5EB | 0,62x | Holgura de oferta |
| Bull compuesto | Token 36x, modelo 8x, eficiencia KV 3x, retención 80%, throughput 8x | 67,9EB | 6,41x | Déficit extremo |

El bear y el bull compuestos no son escenarios oficiales del modelo original, sino un stress test independiente para observar la covarianza entre los supuestos.

La interpretación de esta tabla es el corazón de esta investigación profunda.

<strong>Primero, cambiar una sola variable no hace que el déficit desaparezca fácilmente.</strong> Aunque el múltiplo del modelo baje de 5x a 2x, o el crecimiento de tokens se reduzca a la mitad, sigue quedando un déficit (1,5-1,75x). Esta es la base con la que la narrativa alcista sostiene que "el déficit persiste sin importar qué supuesto se mueva".

<strong>Segundo, sin embargo, las variables no son independientes entre sí.</strong> La desaceleración del crecimiento de tokens, la expansión de modelos más pequeños y MoE, la compresión de KV, el offload de HBM y la mejora del throughput <strong>se mueven varios a la vez cuando mejora la eficiencia tecnológica</strong>. Por eso, en el bear compuesto, la demanda cae a 6,5EB y el cuadro se invierte hacia una holgura de oferta.

<strong>Tercero, por lo tanto, aunque el 2,5x lleve la etiqueta de base-case, en la práctica debe tratarse como un escenario con sesgo alcista.</strong> Una sensibilidad de una sola vía (one-way sensitivity), que mueve una única variable hasta el extremo, no puede demostrar la solidez del 2,5x. El riesgo real está en la covarianza, en que los supuestos se derrumben juntos.

---

## 6. La perspectiva de liquidación de mercado: cómo leer el 2,5x

No hay que leer `demanda de 26,7EB, oferta de 10,6EB` literalmente como 16,1EB de pedidos no atendidos. El mercado real se liquida en este orden.

```text
Aumento del workload potencial de IA
→ cuello de botella de HBM qualified
→ subida de precios, contratos de largo plazo, anticipos
→ allocation por cliente y retraso de workloads de bajo ROI
→ expansión de SLM, MoE, cuantización, reutilización de KV, offload
→ capex adicional y certificación de second-source
→ convergencia entre el volumen de envíos realizado y la demanda liquidada
```

\[Inferencia\] Es decir, es más preciso leer el 2,5x no como una predicción exacta del déficit de volumen que se materializará, sino como un escenario que expresa <strong>la intensidad del poder de fijación de precios y de la presión de racionamiento</strong>. Que el déficit sea grande no significa que "los 16EB nunca se llenarán", sino que "esa brecha recibe una fuerte presión de liquidación a través de precios, contratos y sustitución tecnológica".

Desde esta perspectiva, lo que realmente debe observar un análisis de oferta y demanda no es la cifra de EB en sí, sino lo siguiente. \[Puntos de observación\]

1. Si se mantiene el price floor de los contratos plurianuales.
2. Si la prima de ASP de HBM4/4E se sostiene el tiempo suficiente.
3. Si el aumento del mix de HBM también tensiona la oferta de DRAM de propósito general.
4. Si la mejora del rendimiento (yield) y del advanced packaging hace que el margen de los ingresos incrementales quede en manos del proveedor.
5. Cuánta utilidad y flujo de caja se acumulan antes de que la nueva oferta de 2028 normalice los precios.

---

## 7. Perspectiva por horizonte temporal: Base / Bull / Bear

Al proyectar las tres lentes y la sensibilidad sobre el horizonte temporal, el panorama se resume así.

| Periodo | Base | Bull | Bear |
|---|---|---|---|
| 2026-2027 | El ramp de HBM4 y la demanda de IA superan a la nueva oferta greenfield. Continúa la tensión | Retraso en la certificación de Samsung, cuello de botella de packaging persistente, la demanda de tokens y ASIC supera las previsiones | La oferta masiva de HBM4 de Samsung y la diversificación del mix de clientes llegan antes de lo esperado |
| 2028 | Comienzan los efectos de SK Yongin fase 1, Micron ID1, Tongluo y packaging. Se modera la magnitud del déficit | El efecto en la oferta queda limitado por retrasos iniciales de rendimiento (yield) y certificación | La nueva capacidad se estabiliza rápidamente y mejoran a la vez la eficiencia de KV y de routing |
| 2029-2030 | Aunque persista el déficit, es más probable que se modere que se amplíe. El poder de fijación de precios dura más que en ciclos pasados | El footprint del modelo y la concurrencia de agentes superan a las mejoras de eficiencia, se sostienen los contratos de largo plazo y la prima de escasez | El ramp simultáneo de Micron ID2, Samsung y SK, sumado a la eficiencia y el offload, normaliza la prima de HBM |

### Veredicto final por horizonte temporal

- `Tensionado hasta 2027`: <strong>probabilidad alta</strong>
- `Mejora de la oferta desde 2028`: <strong>probabilidad media-alta</strong>
- `Moderación del déficit en 2029-30`: <strong>probabilidad media</strong>
- `Ampliación del gap de 2,5x incluso en 2030`: <strong>probabilidad baja / escenario alcista</strong>

---

## 8. Qué hay que vigilar: disparadores de reevaluación

Definir de antemano las señales que indican si la narrativa de oferta y demanda se fortalece o se debilita evita dejarse llevar por titulares sueltos.

<strong>Señales de que se fortalece la tesis alcista de oferta y demanda</strong>

1. Los proveedores confirman oficialmente estar sold-out, o mantienen contratos de largo plazo y price floor, incluso más allá de 2028.
2. El rendimiento (yield) y la capacidad de packaging de HBM4/4E mejoran mientras se sostienen la prima de ASP y el margen.
3. La guía de tensión de la industria se extiende más allá de 2028 pese a la ampliación de capacidad de Samsung y Micron.
4. Los tokens reales, el contexto residente y la concurrencia de las cargas de trabajo agentic se acercan a la trayectoria de 24x.

<strong>Señales de que se debilita la tesis alcista de oferta y demanda</strong>

1. Se generaliza en entornos de producción un ahorro combinado de 6x o más en memoria de KV y de pesos.
2. Más de la mitad de la inferencia incremental migra hacia estructuras memory-light de SLM, ASIC y offload.
3. El HBM4E de Samsung y la nueva capacidad de Micron obtienen certificación masiva antes de lo previsto.
4. Los proveedores retiran su guía de `tensión más allá de 2027` y se debilita el price floor de los contratos con clientes.
5. La prima de ASP de HBM, el precio de los contratos y el margen de DRAM caen de forma estructural junto con el aumento de la oferta.

---

## Conclusión: la dirección es sólida, la magnitud debe ser humilde

La conclusión en una línea de esta investigación profunda es esta. <strong>Los datos y el calendario oficial respaldan que `el HBM estará tensionado hasta 2027 y la oferta mejorará desde 2028`, pero `un déficit de 2,5x en 2030` es un escenario alcista que exige que varios supuestos de demanda se cumplan simultáneamente.</strong>

La cifra de 26,7EB se reproduce con precisión, pero esa precisión no equivale a certeza. Es un valor que solo se obtiene si token 24x, modelo 5x, contexto 4x y retención de KV del 70% se cumplen <strong>a la vez</strong>, y si mejora la eficiencia tecnológica, estos supuestos se derrumban juntos. Por el lado contrario, la oferta se convierte en qualified output mucho más lentamente que lo que sugieren las noticias sobre fábricas. El punto donde se encuentran ambas fuerzas es el punto de inflexión de 2028.

El marco útil para analizar la oferta y la demanda no es confiar en una sola cifra, sino <strong>separar la confiabilidad de la dirección de la incertidumbre de la magnitud</strong>. La dirección es sólida. La magnitud debe ser humilde.

---

_Esta publicación es un material de análisis de la estructura de oferta y demanda elaborado combinando fuentes primarias públicas (Goldman Sachs, SK Hynix, Samsung Electronics, Micron, SEMI, Google Research, informes técnicos de DeepSeek) y un modelo secundario (Memory Analyst), que reproducimos y verificamos de forma cruzada e independiente. Los valores mencionados son ejemplos para explicar la estructura de la industria y no constituyen una recomendación de inversión. Cifras como 26,7EB, 10,6EB y 2,5x son, en su mayoría, supuestos y escenarios del modelo, no previsiones oficiales de las empresas. Como este es un campo que cambia con rapidez, se recomienda verificar y actualizar con las fuentes primarias más recientes._

---

### Artículos relacionados

- [HBM, HBF y HBC: Cómo distinguir las tres tecnologías de memoria para IA](/es/post/hbm-hbf-hbc-ai-memory-comparison-2026-06-22/)
- [El valor actual y futuro del token de IA: análisis del valor agregado de las empresas de memoria](/es/post/ai-token-value-memory-value-added-2026-07-09/)
- [Las llamadas de resultados de las grandes tecnológicas de finales de julio y los escenarios para la tesis de memoria](/es/post/big-tech-july-earnings-call-memory-thesis-scenarios-2026-07-07/)
- [¿Quién paga el consenso de semiconductores de 2027?](/es/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/)
- [Samsung y SK Hynix con beneficios 2028E: números baratos y prueba de ciclo](/es/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/)
