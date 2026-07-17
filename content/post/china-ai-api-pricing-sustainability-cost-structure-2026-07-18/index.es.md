---
title: "¿Es sostenible el precio de las API de IA chinas? Verificando la estructura de costes con las divulgaciones"
slug: "china-ai-api-pricing-sustainability-cost-structure-2026-07-18"
date: 2026-07-18T11:00:00+09:00
description: "La salida de DeepSeek V4-Pro cuesta 34 veces menos que la de GPT-5.6 Sol. ¿Es un precio sostenible o el camino hacia el ganador se lo lleva todo como en los vehículos eléctricos? Las divulgaciones de Hong Kong de Zhipu y MiniMax dividen la respuesta: las API de pago de gama alta ya cubren el coste marginal de inferencia, pero ninguna recupera el coste completo incluido el entrenamiento."
categories: ["Exclusive Analysis", "AI Infrastructure", "Tech-Analysis"]
tags: ["IA china", "DeepSeek", "Zhipu", "MiniMax", "Alibaba", "Huawei", "Precios de API", "Estructura de costes", "HBM", "Samsung Electronics", "SK Hynix"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexto
> Este artículo es la continuación de [Lo que realmente cambia la convergencia de los modelos abiertos chinos](/es/post/china-open-model-convergence-value-chain-redistribution-2026-07-17/). Si el artículo anterior abordó las <strong>implicaciones para la cadena de valor</strong> de esa convergencia de rendimiento, este verifica con las divulgaciones de Hong Kong si esas API baratas son <strong>sostenibles en su estructura de costes</strong>. Conviene leerlo junto con [Kimi K3 redefine la curva de precios de la IA](/es/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/) y [El verdadero debate entre el argumento alcista y bajista de los semiconductores](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/). Los hubs relacionados son el [Hub de IA y HBM](/es/page/korea-semiconductor-hbm-kospi-hub/) y el [Hub de Exclusive Analysis](/es/page/exclusive-analysis-hub/).

## TL;DR

* El precio actual de las API de IA chinas es <strong>una mezcla de costes estructuralmente más bajos y competencia estratégica a pérdida</strong>. Es difícil que todos los precios ultrabajos se mantengan, y también es difícil que vuelvan al nivel de la frontera estadounidense.
* Las divulgaciones de Hong Kong dividen la respuesta. El margen bruto de la API de Zhipu mejoró a <strong>18,9%</strong> (frente al 3,3% del año anterior), lo que indica que <strong>empieza a superar el coste marginal de inferencia</strong>. Pero el beneficio bruto total equivale a solo <strong>9,3%</strong> del I+D, por lo que <strong>el coste completo no se recupera</strong>.
* La ventaja de costes de China es real, pero no se debe a los chips de Huawei ni a la electricidad barata. El orden es <strong>estructura del modelo y reducción de parámetros activos > procesamiento por lotes, caché y cuantización > utilización de GPU en la nube > márgenes objetivo bajos > electricidad y NPU nacional</strong>.
* Incluso sobrestimando el efecto de la electricidad, este se queda en <strong>apenas un 2%</strong> del precio del cómputo. El hecho de que Qwen 3.5 Flash tenga el mismo precio en Pekín, Fráncfort y Virginia respalda esta conclusión.
* A diferencia de los vehículos eléctricos, los modelos de IA tienen <strong>costes de cambio bajos</strong>. Si aparece un ganador que se lo lleva todo, no será en el modelo, sino en la capa de nube y distribución. La vía más probable es un <strong>oligopolio de precios bajos (60%)</strong>. [Alcance]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Marco clave</div>
  <div class="thesis-callout__body">
    Los precios bajos de las API chinas no se deben a que ya sean un precio normal autosuficiente, sino a que la mejora de la eficiencia de inferencia y una enorme captación de capital los sostienen juntos. Esto presiona el margen de las API de los operadores de modelos occidentales, pero como el capital captado vuelve a entrenamiento e infraestructura de cómputo, no implica una caída de la demanda total de semiconductores.
  </div>
</div>

---

## 1. ¿Cuánto más barato es?

Precios por millón de tokens a julio de 2026. [Hecho: tablas de precios oficiales de cada empresa]

| Modelo | Entrada | Salida |
|---|---:|---:|
| DeepSeek V4 Flash | 0,14 USD | 0,28 USD |
| DeepSeek V4 Pro | 0,435 USD | 0,87 USD |
| Gemini 3.5 Flash | 1,50 USD | 9 USD |
| GPT-5.6 Sol | 5 USD | 30 USD |

DeepSeek V4-Pro es aproximadamente <strong>11 veces</strong> más barato que GPT-5.6 Sol en entrada y <strong>34 veces</strong> más barato en salida. Por supuesto, esto no significa que el rendimiento, la latencia, el SLA, la seguridad y el nivel de herramientas sean equivalentes.

### La dispersión de precios también es amplia dentro de China

- Qwen 3.7 Max: RMB 12 de entrada, RMB 36 de salida, actualmente con 50% de descuento
- Doubao Seed 2.1 Pro: RMB 6 de entrada, RMB 30 de salida
- DeepSeek V4-Pro: mucho más agresivo que sus rivales chinos

Por eso <strong>no hay que tomar el precio de DeepSeek como el precio normal de toda China</strong>. [Inferencia: interpretación de la dispersión de precios]

---

## 2. La parte sostenible: el coste marginal

DeepSeek V4-Pro es una arquitectura MoE que <strong>activa solo 49.000 millones</strong> de sus 1,6 billones de parámetros totales. Combinando una alta tasa de utilización con procesamiento por lotes y caché, el coste de cómputo real por token puede reducirse considerablemente. El precio de un acierto de caché para entradas repetidas es de apenas <strong>0,003625 USD</strong> por millón de tokens. [Hecho: material oficial de DeepSeek]

Por eso, para el siguiente tipo de tráfico, incluso el precio actual puede ser sostenible en términos de coste marginal.

- Procesamiento por lotes
- Aciertos de caché
- Tráfico sin garantía de latencia
- Uso masivo capaz de mantener una alta tasa de utilización

---

## 3. La parte difícil de sostener: el coste completo

Con los precios públicos actuales, es difícil recuperar el coste de entrenamiento del modelo, el I+D, los experimentos fallidos, la capacidad ociosa, y la seguridad, las ventas y el SLA empresarial.

La normalización de precios ya ha comenzado. [Hecho: medidas y cobertura de cada empresa]

- DeepSeek bajó el precio de V4 un 75% y luego <strong>duplicó el precio en las horas pico</strong>
- Alibaba también subió el precio de algunos servicios de IA hasta <strong>34%</strong>
- El rendimiento dedicado empresarial y los servicios de baja latencia tienen precios más altos que la API pública

Es una prueba de que el precio ultrabajo no se mantiene en todas las franjas horarias ni para todos los segmentos de clientes.

| Servicio | Sostenibilidad |
|---|---|
| Tráfico de caché, por lotes y no prioritario | Alta |
| Horas pico, baja latencia, alta concurrencia | Baja |
| Seguridad y SLA empresarial | Se asienta una tarifa separada y más alta |
| Recuperación del coste completo del negocio de API independiente | Difícil con los precios actuales |

---

## 4. Verificación con las divulgaciones: Zhipu y MiniMax

A partir de aquí está el núcleo de este artículo. En lugar de especular, esto se puede confirmar con las <strong>divulgaciones de las empresas que cotizan en Hong Kong</strong>.

| 2025 | Zhipu (02513) | MiniMax (00100) |
|---|---:|---:|
| Ingresos | RMB 724 millones | 79,04 millones de USD |
| Proporción de ingresos de API/plataforma | 26,3% | 32,8% |
| Margen bruto de API o de toda la empresa | API 18,9% | Empresa 25,4% |
| Margen bruto del año anterior | API 3,3% | Empresa 12,2% |
| I+D / Ingresos | 439% | 320% |
| Pérdida neta ajustada / Ingresos | 439% | 317% |
| Beneficio bruto / I+D | <strong>9,3%</strong> | <strong>7,9%</strong> |

[Hecho: resultados 2025 de Zhipu, informe anual 2025 de MiniMax]

### Zhipu: la recuperación del coste marginal está confirmada

Los ingresos de API y plataforma abierta pasaron de RMB 48,48 millones a <strong>RMB 190,4 millones, un aumento del 293%</strong>, y el margen bruto también subió de 3,3% a 18,9%. La empresa atribuyó esto a la eficiencia de inferencia, las economías de escala y las subidas de precio.

Hay un hecho más importante todavía. A marzo de 2026, aunque <strong>subió el precio de la API un 83% respecto a finales del año anterior, la demanda superó a la oferta</strong>. El precio oficial actual de GLM-5 es RMB 4 de entrada y RMB 18 de salida por millón de tokens. Todo indica que las API de gama alta han dejado atrás la estructura de dumping por debajo del coste directo de inferencia. [Inferencia: implicación de la subida de precios y el exceso de demanda]

### MiniMax: alta probabilidad, pero sin confirmar

No ha revelado el margen bruto exclusivo de la API. El margen bruto de toda la empresa mejoró de 12,2% a <strong>25,4%</strong>, y la empresa lo atribuyó a la eficiencia del modelo y del sistema, y a la optimización de la asignación de infraestructura.

El precio actual de M2.5 es 0,30 USD de entrada y 1,20 USD de salida por millón de tokens, y la versión de alta velocidad es 0,60/2,40 USD. Sin embargo, como M2.5 se lanzó en 2026 y los resultados divulgados solo llegan hasta 2025, <strong>la relación de costes exclusiva de la API a los precios actuales todavía no está verificada</strong>. [Bloqueado]

### El coste completo no se recupera en ninguna de las dos empresas

El beneficio bruto total de Zhipu, RMB 297 millones, cubre apenas el <strong>9,3%</strong> de su I+D de RMB 3.180 millones. MiniMax tampoco: su beneficio bruto de 20,08 millones de USD cubrió solo el <strong>7,9%</strong> de su I+D de 253 millones de USD, y su salida de caja operativa fue de 280 millones de USD.

Los servicios que MiniMax compró al grupo Alibaba en 2025 sumaron <strong>75,88 millones de USD, el 96% de sus ingresos</strong>. Es una cifra que mezcla nube para entrenamiento y para servicio, así que no se puede tomar directamente como el coste de la API, pero es evidencia de una alta dependencia de infraestructura de cómputo externa. Alibaba posee el 17,06% de MiniMax.

Un punto importante es que las divulgaciones afirman que las transacciones con partes relacionadas se realizaron <strong>según los precios y condiciones públicos ofrecidos a los clientes generales</strong>. Se puede reconocer que la relación estratégica facilitó el aseguramiento de capacidad y la integración, pero <strong>no hay base para afirmar que existió un subsidio de precios oculto</strong>. [Inferencia: interpretación del texto de la divulgación]

Incluso después de cotizar, Zhipu captó de forma neta HK$31.375 millones, y MiniMax, entre acciones nuevas y bonos convertibles, un total de HK$15.957 millones. La mayor parte del capital captado se destina a I+D e infraestructura de cómputo. La captación de capital en sí no es prueba de pérdidas en la API, pero <strong>indica que la competencia de modelos de frontera no se sostiene solo con caja interna</strong>. [Hecho: divulgaciones]

### Veredicto

1. Sostenibilidad del coste marginal de las API de pago de gama alta: en Zhipu está <strong>confirmada</strong>; en MiniMax, alta probabilidad pero sin confirmar
2. Sostenibilidad del coste completo, incluido el entrenamiento: <strong>no se cumple</strong> en ninguna de las dos empresas
3. Sostenibilidad de la guerra de precios: <strong>alta</strong>. La captación de capital en los mercados permite mantener precios deficitarios durante mucho tiempo
4. Estructura de mercado: más que un ganador que se lo lleva todo, es probable un <strong>oligopolio por segmento</strong>, como Zhipu en empresas chinas y on-premise, y MiniMax en el extranjero, consumidores y multimodal

---

## 5. Descomponiendo la ventaja de costes: ¿cuál es la razón real?

La ventaja de costes de China en el servicio de API es real. Pero la clave no es solo la electricidad barata o los chips de Huawei, sino la siguiente combinación.

```text
Parámetros activos reducidos y cuantización
+ Alta tasa de procesamiento por lotes y uso de caché
+ Utilización de GPU en una nube a gran escala como la de Alibaba
+ Márgenes objetivo bajos
+ Electricidad barata del oeste de China
```

| Factor | Ventaja de costes | Evaluación |
|---|---:|---|
| Estructura del modelo, cuantización y caché | Muy grande | El núcleo de la competitividad de precios de las API chinas |
| Escala y utilización de la nube | Grande | El foso más sólido de Alibaba |
| Márgenes objetivo bajos | Grande | La razón de los precios bajos, pero una debilidad para la rentabilidad a largo plazo |
| Huawei Ascend | Medio, condicional | Favorable en cargas de trabajo optimizadas, baja versatilidad |
| Electricidad del oeste de China | Medio | Válido para inferencia por lotes, limitado para API globales en tiempo real |
| Subsidios estatales y financiamiento de política | Existe | Favorable para el fomento industrial, pero el monto por servicio no es transparente |

---

## 6. ¿Es la electricidad realmente decisiva?

Es cierto que la electricidad china es barata. El precio de la electricidad entregada en el centro de datos de Zhongwei, en Ningxia, es de <strong>RMB 0,36/kWh</strong> en 2026, alrededor del 45% del nivel del este de China. El promedio industrial de Estados Unidos en 2025 fue de <strong>8,62 centavos/kWh</strong>, lo que equivale a aproximadamente RMB 0,62/kWh suponiendo un tipo de cambio de 7,2 RMB/USD. Zhongwei es alrededor de <strong>42% más barato</strong>. [Hecho: datos de gobiernos locales chinos, EIA de Estados Unidos]

Pero la electricidad por sí sola no explica que el precio de la API sea 5 o 10 veces más barato. Si se <strong>sobrestima</strong> el efecto de la electricidad, asumiendo una carga de TI de 1kW por tarjeta y un PUE de 1,1, el resultado es el siguiente.

```text
Zhongwei:          1kW × 1,1 × RMB 0,36 = RMB 0,40/hora
Promedio EE. UU.:   1kW × 1,1 × RMB 0,62 = RMB 0,68/hora
Diferencia:                                aprox. RMB 0,29/hora
```

Dado que el precio on-demand de la L20 que ofrece Alibaba es de RMB 14,4/hora, incluso bajo este supuesto de límite superior, la diferencia de electricidad representa <strong>alrededor del 2%</strong> del precio del cómputo. [Inferencia: cálculo propio]

Esto significa que la electricidad es importante, pero no es la principal responsable de la brecha de precios de las API.

### El contraargumento decisivo

La ventaja de la electricidad del oeste encaja bien con la inferencia y el entrenamiento por lotes, pero las API de baja latencia deben desplegarse en regiones del este o del extranjero, cerca del usuario. Y el precio de Qwen 3.5 Flash de Alibaba es <strong>idéntico no solo en Pekín, sino también en Fráncfort y Virginia: 0,029 USD de entrada y 0,287 USD de salida por millón de tokens</strong>. [Hecho: tabla de precios de Alibaba Model Studio]

Es la evidencia más directa de que el precio bajo de las API no es solo resultado de la electricidad china. [Inferencia: implicación de la paridad de precios entre regiones]

---

## 7. El verdadero foso de Alibaba es la utilización

Alibaba Cloud es fuerte no tanto por la electricidad como por su <strong>capacidad de mantener las GPU siempre ocupadas</strong>. [Hecho: documentación oficial de Alibaba]

- Inferencia por lotes: <strong>50% de descuento</strong> sobre el precio de lista
- Instancias spot L20: desde RMB 14,4 on-demand hasta cerca de RMB 2,88 habitualmente, un ahorro de alrededor del <strong>80%</strong>
- GPU ociosas: precio unitario activo de 0,000018 USD/CU frente a precio unitario ocioso de 0,000007 USD/CU
- Combina on-demand, spot y autoescalado para responder a picos de tráfico

Sin embargo, las instancias spot tienen riesgo de interrupción, por lo que no se puede pasar toda una API en tiempo real con SLA estricto a spot. La estructura consiste en dejar la demanda base en recursos on-demand o dedicados, y atender solo la demanda elástica con spot. [Inferencia: restricción operativa]

---

## 8. ¿Es el Ascend de Huawei barato sin condiciones?

En rigor, el Ascend no es una GPU, sino una <strong>NPU</strong>.

Huawei afirma lo siguiente sobre el CloudMatrix 384. [Hecho: material oficial de Huawei]

- Rendimiento de inferencia equivalente por tarjeta individual: 2.300 tokens/s
- Alrededor de <strong>4x</strong> frente a los sistemas no supernodo anteriores
- Mejora del MFU de más del 50%
- Rendimiento de inferencia promedio por tarjeta de <strong>3-4x frente al H20</strong>

Es un método que compensa con el diseño del sistema las debilidades de un chip individual de gama baja, mediante la agrupación de recursos y el paralelismo de expertos de MoE.

### Pero no hay que leerlo de inmediato como un coste bajo

- Huawei <strong>no ha publicado un TCO verificado externamente bajo el mismo modelo, la misma latencia y la misma energía</strong>. [Bloqueado]
- Como el CloudMatrix agrupa muchas NPU y red para elevar el rendimiento, <strong>el rendimiento por tarjeta y el coste total del clúster son cosas distintas</strong>.
- Un estudio de campo de 2026 sobre el Ascend 910 encontró que, para lograr una inferencia estable, se necesitaron 12 parches de código fuente, la desactivación de algunas funciones de alto rendimiento y mecanismos para lidiar con fallos recurrentes. Aunque el hardware sea barato, <strong>la ingeniería y el coste operativo pueden subir</strong>. [Hecho: estudio de campo del Ascend]

### Veredicto condicional

| Condición | Veredicto |
|---|---|
| Modelos profundamente optimizados para Ascend, como Qwen, DeepSeek y GLM | Posible competitividad de costes |
| Migración directa de modelos basados en CUDA | Ventaja de costes incierta |
| Inferencia por lotes a gran escala dentro de China | Favorable |
| Servicio empresarial global en tiempo real | Sin confirmar si se incluye el coste de software y SLA |

---

## 9. ¿En qué se diferencia de los vehículos eléctricos?

Los puntos en común son la industria estratégica, la inversión a gran escala, los subsidios a grandes empresas y la captura de cuota de mercado mediante recortes de precio.

La diferencia es que <strong>el coste de cambio de los modelos de IA es mucho más bajo</strong>. Las especificaciones de las API son similares, y los clientes pueden enrutar entre varios modelos a la vez u operar modelos de código abierto por su cuenta. Si un operador sube el precio, los modelos rivales y el hospedaje propio crean un techo de precio.

En cambio, las plataformas que combinan nube, datos, seguridad, pagos, publicidad y herramientas de trabajo tienen costes de cambio altos. <strong>Si aparece un ganador que se lo lleva todo, será en la capa de distribución y nube, más que en el modelo</strong>. [Inferencia: estructura de costes de cambio]

La estructura más probable es esta.

- Alibaba: nube, comercio electrónico y clientes empresariales
- ByteDance: tráfico de consumidores, publicidad y contenido
- Tencent: WeChat y servicios empresariales
- Huawei y Baidu: infraestructura nacional y clientes públicos y empresariales
- DeepSeek y otras 1-2 empresas de modelos independientes: referencia del precio técnico

---

## 10. La trayectoria esperada

| Escenario | Probabilidad estimada | Resultado |
|---|---:|---|
| Oligopolio de precios bajos | <strong>60%</strong> | Se reduce a 3-5 actores, se mantiene el precio bajo de la API básica, suben los precios de pico y SLA |
| Comoditización completa | 25% | El código abierto, MoE y los chips propios impulsan más caídas de precio |
| Normalización pronunciada | 15% | Los precios suben 2-5 veces por la carga de chips, electricidad y financiamiento |

[Inferencia: estimación de escenarios]

Incluso si el precio subiera 5 veces, el precio de salida de DeepSeek V4-Pro sería de apenas <strong>~4,35 USD</strong>. Seguiría siendo más bajo que el de los modelos de frontera estadounidenses. <strong>Puede que el precio actual no sea el piso, pero la dirección hacia precios más bajos es difícil de revertir.</strong>

---

## 11. Implicaciones para los semiconductores

Las API baratas aumentan el uso de inferencia, lo que favorece la demanda de DRAM de servidor, NAND, red y electricidad. Por otro lado, reducen el cómputo por token y la intensidad de contenido de HBM, lo que presiona la economía unitaria de las GPU premium y el HBM.

| Objetivo | Evaluación |
|---|---|
| Samsung Electronics | Amortiguado en términos relativos gracias a su alta proporción de DRAM y NAND de propósito general |
| SK Hynix | Advertencia a largo plazo para la prima de escasez del HBM |
| NVIDIA | Presión sobre el precio unitario de las GPU premium, pero el aumento del volumen total de inferencia actúa como factor de defensa |
| Alibaba, Tencent | Se benefician más de la expansión del ecosistema de nube y distribución que del margen de la API |

La clave no es la tasa de caída del precio de la API, sino <strong>la tasa de crecimiento del uso total de tokens</strong>. Si el uso crece más rápido que la caída de precios, gana el efecto Jevons; si no, el múltiplo empieza a bajar primero en las GPU premium y el HBM. [Inferencia: juicio direccional]

---

## 12. La verificación decisiva llegará con las divulgaciones del primer semestre de 2026

- Si el <strong>margen bruto de la API de Zhipu</strong> sube a 25-30% o más tras la subida de precio del 83%
- Si <strong>MiniMax revela su relación de costes de la API</strong>
- Si <strong>la tasa de crecimiento de los ingresos sigue superando a la tasa de crecimiento del gasto en cómputo</strong>
- Si la brecha entre las tarifas de pico y SLA y las tarifas públicas de la API se consolida
- Si Huawei publica un TCO verificado externamente en condiciones equivalentes

Estos cinco puntos separan un "coste sostenible" de un "precio sostenido con capital".

---

## Cierre

Los precios bajos de las API chinas <strong>no se deben a que ya sean un precio normal autosuficiente</strong>. Se deben a que la mejora de la eficiencia de inferencia y una enorme captación de capital los sostienen juntos.

China tiene una ventaja de costes estructural en el servicio de modelos doméstico, por lotes y optimizado. Pero los precios de API extremadamente bajos que se observan actualmente no se pueden explicar solo con los chips de Huawei y la electricidad barata. La mayor ventaja de costes, en orden, es la reducción del tamaño del modelo y los parámetros activos, el procesamiento por lotes, la caché y la cuantización, la utilización de GPU en la nube, y los márgenes objetivo bajos; la electricidad y la NPU doméstica vienen después.

Desde la perspectiva de inversión, que China tenga API baratas no significa directamente que "la IA china haya asegurado un foso de costes abrumador". La interpretación más precisa es que <strong>a medida que el servicio de inferencia se convierte rápidamente en una commodity, el margen de las empresas de modelos baja, y crece la probabilidad de que el valor se desplace hacia la infraestructura de nube, energía y semiconductores</strong>.

Esto presiona el margen de la API de los operadores de modelos occidentales, pero como el capital captado se reinvierte en entrenamiento e infraestructura de cómputo, <strong>no implica una caída de la demanda total de semiconductores</strong>.

---

_Esta publicación es un análisis que integra divulgaciones de empresas que cotizan en Hong Kong (resultados 2025 y colocación de nuevas acciones de Zhipu 02513; informe anual 2025 y captación de capital de MiniMax 00100), tablas de precios oficiales de cada empresa (DeepSeek, OpenAI, Google, Alibaba Model Studio, Volcano Engine, BigModel de Zhipu, Platform de MiniMax), material oficial de Huawei e investigaciones relacionadas con CloudMatrix, datos de gobiernos locales chinos sobre electricidad, y estadísticas de la EIA de Estados Unidos. La relación de costes exclusiva de la API de MiniMax y el TCO de Huawei verificado externamente en condiciones equivalentes no están divulgados, y las probabilidades de los escenarios y los cálculos de electricidad son estimaciones basadas en supuestos del autor al momento de escribir. Los valores mencionados son ejemplos para explicar la estructura de costes y no constituyen una recomendación de compra o venta de ningún valor en particular. Los precios y las cifras de las divulgaciones corresponden al momento de su publicación y pueden cambiar después. La decisión de inversión y su responsabilidad recaen en el propio inversor._

---

### Publicaciones relacionadas

- [Lo que realmente cambia la convergencia de los modelos abiertos chinos: redistribución de la cadena de valor, no colapso de la demanda](/es/post/china-open-model-convergence-value-chain-redistribution-2026-07-17/)
- [Kimi K3 redefine la curva de precios de la IA: de Kimi Linear al HBM y la estrategia de las grandes tecnológicas](/es/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/)
- [El verdadero debate entre el argumento alcista y bajista de los semiconductores: cuatro relojes físicos y un reloj bursátil](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [¿Son cíclicos los semiconductores? ¿Cuál es su valor razonable?](/es/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [El valor actual y futuro del token de IA: análisis del valor agregado de las empresas de memoria](/es/post/ai-token-value-memory-value-added-2026-07-09/)
