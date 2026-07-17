---
title: "Lo que realmente cambia la convergencia de los modelos abiertos chinos: redistribución de la cadena de valor, no colapso de la demanda"
slug: "china-open-model-convergence-value-chain-redistribution-2026-07-17"
date: 2026-07-17T22:00:00+09:00
description: "Los modelos abiertos chinos convergen hacia el rendimiento de frontera estadounidense mientras se sirven sobre infraestructura de inferencia china. Esto es redistribución de la cadena de valor más que un colapso de la demanda de IA. El valor monopolístico de las API de modelos y de las GPU de vanguardia cae, mientras que una inferencia más barata eleva el volumen de tokens y puede aumentar el valor de la memoria, el almacenamiento, las redes, la energía y la distribución en la nube."
categories: ["Exclusive Analysis", "AI Infrastructure", "Market-Outlook"]
tags: ["Modelos abiertos chinos", "DeepSeek", "Kimi K3", "Qwen", "CXMT", "HBM", "Samsung Electronics", "SK Hynix", "Micron", "NVIDIA", "Política de IA"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexto
> Este artículo es la continuación de [Lo que Kimi K3 cambió en el precio de la IA](/es/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/). Si el artículo anterior verificó el precio y la estructura de <strong>un solo modelo</strong>, este se extiende a cómo <strong>todo el ecosistema de modelos abiertos chinos</strong> redistribuye la cadena de valor de los semiconductores y las Big Tech, y a cómo la política estadounidense y el conflicto entre Estados Unidos y China cambian esa interpretación. Conviene leerlo junto con [El verdadero debate entre el argumento alcista y bajista de los semiconductores](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/), [Valor justo de los semiconductores](/es/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/) y [La IPO de CXMT y el riesgo de precios de memoria](/es/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/). Los hubs relacionados son el [Hub de IA y HBM](/es/page/korea-semiconductor-hbm-kospi-hub/) y el [Hub de Exclusive Analysis](/es/page/exclusive-analysis-hub/).

## TL;DR

* La convergencia de rendimiento de los modelos abiertos chinos se parece más a una <strong>redistribución de la cadena de valor que a un colapso de la demanda de IA</strong>. El valor monopolístico de las API de modelos y de las GPU de vanguardia cae, mientras que una inferencia más barata eleva el uso y puede aumentar el valor de la memoria, el almacenamiento, las redes, la energía y la distribución en la nube.
* La preferencia relativa se divide así. En memoria coreana, <strong>Samsung Electronics > SK Hynix</strong>; en semiconductores estadounidenses, <strong>Micron y SanDisk > NVIDIA</strong>; en Big Tech, <strong>Meta y Amazon > Google y Microsoft > operadores de modelos puros</strong>. [Inferencia: juicio relativo]
* Los modelos abiertos chinos han demostrado una <strong>caída del costo de cómputo y memoria por unidad de inteligencia</strong>. No han demostrado una <strong>caída del gasto total en silicio</strong>. De hecho, TSMC elevó su CAPEX de 2026 de 52.000-56.000 a 60.000-64.000 millones de dólares.
* CXMT tiene una diferencia de <strong>1,5-2 generaciones</strong> en producto y de 2-3 años en comercialización respecto a las tres líderes en HBM. Por lo tanto, la amenaza de 2028 no es un shock de oferta actual, sino una <strong>opción condicional</strong>.
* La <strong>difusión tecnológica</strong> de los modelos chinos y la <strong>difusión de ingresos</strong> de los operadores de API chinos son cosas distintas. La vía más realista es rehospedar los modelos chinos en AWS, Azure o una VPC empresarial y venderlos bajo el marco de seguridad y contratos de Occidente. [Alcance]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Marco clave</div>
  <div class="thesis-callout__body">
    Los modelos chinos pueden sacudir el precio de los modelos estadounidenses, pero no derrumban de inmediato la demanda de AWS, Azure, los chips estadounidenses o la memoria coreana. El daño directo recae en el margen de las API de modelos cerrados, mientras que lo que sobrevive a largo plazo es la infraestructura basada en uso: la capa de distribución y seguridad en la nube, junto con la memoria, la red y la energía.
  </div>
</div>

---

## 1. Primero, confirmemos los hechos

La dirección del ecosistema es real, pero <strong>no todos los modelos nuevos han revelado su hardware de entrenamiento</strong>. Esta distinción importa.

DeepSeek-V3 se entrenó con <strong>2.048 GPU NVIDIA H800</strong> y 2,788 millones de GPU-horas. [Hecho: informe técnico de DeepSeek V3] La H800 está sujeta a restricciones de exportación, pero no es una GPU de consumo de gama baja. Kimi K3, en cambio, reveló 2,8 billones de parámetros, una ventana de contexto de 1M de tokens y una eficiencia de escalado 2,5x superior a K2, pero <strong>el informe técnico completo y el hardware de entrenamiento se publicarán el 27 de julio</strong>. [Hecho: anuncio oficial de Kimi]

Por lo tanto, todavía no se puede confirmar que "Kimi K3 también se entrenó con GPU NVIDIA de gama baja". [Bloqueado]

### La mejora de eficiencia es real

DeepSeek V4-Pro <strong>activa solo 49.000 millones</strong> de sus 1,6 billones de parámetros. En el rango de 1M de tokens, el cómputo (FLOPs) por token cae al <strong>27%</strong> y la KV cache al <strong>10%</strong> respecto a V3.2. [Hecho: ficha del modelo DeepSeek V4] Es evidencia directa de que el uso de GPU y HBM por token puede reducirse drásticamente mientras se mantiene el rendimiento.

### Pero el lado opuesto también es real

El CloudMatrix384 de Huawei conecta 384 Ascend 910C para servir DeepSeek-R1. Según los datos agregados de JPMAM, CloudMatrix usa 49TB de HBM y 599kW de energía, mientras que el sistema comparado, el GB300 NVL72, usa 21TB y 145kW respectivamente. [Hecho: paper de CloudMatrix, material comparativo de JPMAM]

No es una comparación de rendimiento perfectamente equivalente, pero la dirección es clara: China compensa un chip individual más débil con <strong>más chips, más memoria y más energía</strong>. Un chip individual más barato no significa necesariamente menos silicio, red o energía en total. [Inferencia: interpretación estructural]

---

## 2. La ecuación clave: qué hay que observar

La respuesta a este debate no está en los puntajes de benchmark, sino en dos ecuaciones.

```text
Demanda total de cómputo = Número total de tokens × Cómputo por token

Demanda total de memoria = Número total de tokens × Uso de memoria por token
                          + Almacenamiento de datos de modelo, KV y búsqueda
```

Si los modelos abiertos bajan el precio del token un 70% y el uso se multiplica por 5, la <strong>demanda total aumenta</strong> a pesar de la mejora de eficiencia. Por el contrario, si el HBM por token cae un 70% mientras el uso simplemente se duplica, la <strong>demanda de HBM disminuye</strong>.

Por eso el indicador que hay que vigilar de ahora en adelante se reduce a uno solo. <strong>Cuánto supera la tasa de crecimiento de tokens a la tasa de caída de memoria por token.</strong>

### El veredicto hasta ahora

El gasto total se determina con la siguiente ecuación.

```text
Gasto total en silicio = Número de entrenamientos × Costo por entrenamiento
                        + Tokens de inferencia × Costo por token
```

TSMC elevó su CAPEX de 2026 de 52.000-56.000 a <strong>60.000-64.000 millones de dólares</strong> en su call del 2T26. Microsoft también aumentó su rendimiento de inferencia un 40%, pero el uso de tokens de sus grandes clientes <strong>creció un 30%</strong> frente al trimestre anterior, y mantuvo un CAPEX de 2026 de unos 190.000 millones de dólares. [Hecho: call del 2T26 de TSMC, call del 3T del FY26 de Microsoft]

<strong>Hasta ahora, el crecimiento del uso le está ganando a la mejora de eficiencia.</strong> [Inferencia: síntesis de datos]

---

## 3. Impacto en semiconductores: la divergencia es por acción

| Acción/Grupo | Impacto en la acción | Interpretación clave |
|---|---|---|
| Samsung Electronics | Positivo | Se beneficia de forma más amplia, no solo en HBM sino también en DRAM de servidor, NAND/eSSD y memoria de propósito general |
| SK Hynix | De mixto a positivo | El aumento de tokens es favorable, pero la compresión de MoE y KV reduce el HBM por token, lo que presiona el múltiplo de escasez |
| Micron | Positivo | Exposición combinada en DRAM, HBM y NAND dentro de la cadena de suministro estadounidense. Beneficio de memoria amplia similar al de Samsung Electronics |
| SanDisk | Positivo | El despliegue local, los pesos de modelo y el aumento de RAG y caché se traducen en demanda de eSSD y NAND |
| NVIDIA | Negativo a corto plazo, mixto a largo plazo | Cae el valor monopolístico de la cuota china y de las GPU de gama más alta. El aumento del total de tokens y los envíos de H200 compensan el volumen |
| AMD | Relativamente positivo | Los modelos abiertos facilitan la migración a hardware heterogéneo. ROCm y la cuota real de serving son las variables clave |
| Broadcom, Marvell, Arista | Positivo a mediano plazo | Mayor demanda de custom ASIC, Ethernet y óptica/SerDes en Occidente |
| TSMC | De neutral a positivo | La demanda de chips de entrenamiento de NVIDIA, AMD y ASIC se mantiene, pero la inferencia china migra hacia Ascend y SMIC |

### Por qué Samsung Electronics tiene la ventaja relativa sobre SK Hynix

Entre las mismas tres grandes de memoria, <strong>las direcciones de Samsung Electronics y SK Hynix se separan</strong>. La inferencia barata y la difusión de modelos abiertos no solo aumentan el HBM, sino también el volumen total de DRAM de servidor, NAND y memoria de propósito general. Samsung Electronics, con una exposición más amplia, capta más de esta expansión.

Por el contrario, MoE y la compresión de KV reducen el <strong>HBM por token</strong>. SK Hynix, con una exposición pura más fuerte a HBM, recibe al mismo tiempo el beneficio del aumento de tokens y la carga de la caída de HBM por token. Es una estructura en la que el <strong>múltiplo de escasez</strong>, más que la demanda absoluta, es lo primero que se presiona. [Inferencia: análisis de estructura de exposición]

Sin embargo, Samsung Electronics también tiene un riesgo del lado opuesto. Es la primera en exponerse al aumento de producción de DRAM de propósito general de CXMT.

### NVIDIA y la H200

Estados Unidos comenzó recientemente a permitir envíos limitados de H200 a China, pero el volumen todavía es pequeño. Es positivo para los ingresos de NVIDIA en el corto plazo, pero no lo suficiente como para revertir la transición hacia infraestructura doméstica centrada en Huawei. [Hecho: reportaje de Reuters de julio de 2026] [Inferencia: evaluación de impacto]

---

## 4. Impacto en las Big Tech

| Empresa | Evaluación | Motivo |
|---|---|---|
| Meta | La más positiva | Se valida la estrategia de ecosistema abierto y recupera el valor de la IA en publicidad y recomendaciones más que en API |
| Amazon | Positivo | Gane el modelo que gane, vende inferencia, almacenamiento y red de AWS |
| Google | De mixto a positivo | TPU y la nube se benefician, pero la prima de precio de la API de Gemini está bajo presión |
| Microsoft (Azure) | Mixto | El uso de Azure crece, pero el alquiler de los modelos de OpenAI y la tasa de recuperación del CAPEX están bajo presión |
| Apple | Positivo | Los modelos abiertos y pequeños más baratos reducen el costo del on-device y de Private Cloud |
| OpenAI, Anthropic | Negativo | Se reduce la brecha de rendimiento y la prima de precio de la API, lo que presiona la elevada valoración y el financiamiento |

<strong>A diferencia de un error de percepción común, Meta no es la mayor perjudicada.</strong> Gana dinero con publicidad y recomendaciones más que con la venta de modelos, y usa los modelos abiertos para reducir costos, por lo que existe la posibilidad de un beneficio relativo. La carga recae, en cambio, en el CAPEX y la depreciación. [Inferencia: análisis de modelo de negocio]

### La lección del shock de DeepSeek de 2025

Durante el shock de DeepSeek de 2025, NVIDIA perdió <strong>un 17% en un día, cerca de 593.000 millones de dólares</strong> de capitalización de mercado. La reacción inicial fue una venta masiva de toda la infraestructura de GPU, energía y centros de datos, pero luego hubo un rebote parcial. [Hecho: cobertura de mercado de 2025]

Es probable que esta vez también <strong>el precio de la acción a corto plazo reaccione al miedo por la eficiencia, y los resultados a mediano plazo, al aumento del uso</strong>. [Inferencia: patrón histórico]

---

## 5. Veredictos sobre la tesis de los modelos abiertos chinos

Evaluando uno por uno los argumentos que vienen tanto del lado alcista como del bajista, el resultado es el siguiente.

| Argumento | Veredicto |
|---|---|
| Las GPU de gama más alta son imprescindibles para el rendimiento de frontera | Debilitado, pero no refutado |
| La inteligencia de IA es un bien escaso | Colapso considerable en el precio de los modelos y tokens en bruto |
| La escala de capital es el foso defensivo | El foso del preentrenamiento se debilita y se desplaza hacia el despliegue, los datos, la energía y la distribución |
| El costo marginal del código abierto es cero | Solo el precio de los pesos se acerca a cero; el costo de inferencia sigue existiendo |
| Un entrenamiento de 1.000 millones de dólares supera a una inversión de 100.000 millones | Afirmación imprecisa que compara rangos de costo distintos |

El último punto es el que más se usa mal con frecuencia. El costo de entrenamiento y la inversión total en infraestructura no son comparables.

---

## 6. Hasta dónde ha llegado realmente el HBM de CXMT

Es la parte que más se suele exagerar al hablar de la amenaza china. Al desglosarla etapa por etapa, la realidad queda al descubierto.

| Etapa | Veredicto actual | Base del juicio |
|---|---|---|
| Proceso de celda DRAM | Comercializado, mejora rápida | Venta de DDR5 y LPDDR5X; Apple también está probando DRAM de CXMT para productos del mercado chino |
| Apilado TSV | HBM2 en volumen bajo, HBM3 inicial | Hay reportes de producción de HBM2, pero el volumen y la tasa de rendimiento no se han revelado |
| Empaquetado y base die | En construcción | El ecosistema dentro de China se está formando, pero faltan datos de rendimiento de producción en masa, térmicos y de confiabilidad |
| Calificación de clientes | HBM no confirmado | El contrato con Tencent y las pruebas de Apple son evidencia de capacidad en DRAM general, no de HBM |
| Brecha con los líderes | 1,5-2 generaciones | Las tres líderes ya están en la rampa de HBM4, mientras que CXMT ni siquiera ha verificado la producción en masa de HBM3 |

En el portafolio de productos oficial de CXMT, a fecha del 17 de julio de 2026, solo figuran DDR5, LPDDR5/5X, DDR4 y LPDDR4X, y <strong>no hay HBM</strong>. TrendForce también clasifica el HBM3 de CXMT en etapa de verificación inicial, y evalúa que las barreras técnicas y la condición de usar equipos domésticos retrasan la producción en masa. [Hecho: material oficial de CXMT, TrendForce]

Las estimaciones de capacidad también son contradictorias. Hay un choque entre el estancamiento en torno a 240.000 obleas/mes y la proyección de 350.000 para fin de año, pero esta última cifra proviene de un modelo privado, no de guía de la empresa, por lo que es difícil tomarla como un valor confirmado. [Bloqueado]

### Así hay que corregir la hipótesis de la DRAM legacy

- <strong>2026-2027</strong>: la inversión de CXMT en HBM <strong>retrasa</strong> el alivio de la oferta de DRAM legacy china.
- <strong>2028</strong>: si el HBM3/3E logra la calificación de clientes de aceleradores chinos y un volumen significativo, podría empezar a reemplazar primero el mercado de HBM de generación anterior dentro de China.
- <strong>2029 en adelante</strong>: solo cuando el HBM4, el base die y el rendimiento de empaquetado se pongan al día, se presionará directamente el mercado líder global y el margen de SK Hynix.

Es decir, es más válido decir que <strong>"CXMT no libera la oferta de legacy tanto como se esperaba"</strong> que decir que "por CXMT, la escasez de legacy empeora de inmediato". [Inferencia: evaluación por etapas]

---

## 7. Cómo la política estadounidense cambia esta interpretación

Estados Unidos trata la IA menos como una tecnología comercial y más como <strong>infraestructura central del bloque aliado</strong>. Por eso el análisis puramente técnico no basta para responder esta pregunta.

El AI Action Plan de Estados Unidos y la orden ejecutiva 14320 establecen explícitamente que se exportará a los países aliados un <strong>stack de IA estadounidense</strong> que integra hardware, nube, red, modelos y aplicaciones, reduciendo así la dependencia tecnológica de las naciones adversarias. Aunque un modelo chino sea superior en rendimiento y precio, el stack estadounidense mantiene una ventaja política en la contratación gubernamental y las industrias estratégicas de los países aliados. [Hecho: AI Action Plan de la Casa Blanca, EO 14320]

### Sin embargo, no es un desacople total

En enero de 2026, la BIS de Estados Unidos dispuso que la exportación de H200 y MI325X a China se revise caso por caso, bajo clientes aprobados y requisitos de seguridad. Es un compromiso que busca mantener el control mientras deja a China parcialmente dentro del ecosistema de chips estadounidense. [Hecho: BIS 2026-01-13]

Tampoco está prohibido por completo que las empresas privadas estadounidenses usen modelos chinos. La `No DeepSeek on Government Devices Act` todavía está solo en etapa de propuesta legislativa. Sin embargo, el gobierno de Australia ordenó eliminar DeepSeek de los sistemas gubernamentales, y la autoridad de protección de datos de Italia restringió el procesamiento de datos de usuarios. [Hecho: medidas oficiales de cada país]

<strong>Es probable que la prohibición de facto de los departamentos de adquisiciones y seguridad opere antes que la legislación.</strong> [Inferencia: orden de aplicación de la política]

---

## 8. ¿Pueden las empresas occidentales usar realmente las API de modelos chinos?

La probabilidad de adopción es completamente distinta según la vía. Esta tabla es la respuesta a la pregunta.

| Método de adopción | Probabilidad de difusión | Evaluación |
|---|---|---|
| Llamada directa a la API alojada en territorio chino | Baja | Riesgo de datos, jurisdicción y adquisiciones |
| API de Qwen en EE. UU., UE, Japón y Singapur | Media | La localización de datos es posible, pero persiste el riesgo del operador chino |
| Modelos chinos rehospedados por AWS o Azure | De media-alta a alta | El contrato, la seguridad y el control de datos quedan en manos de la nube occidental |
| Open-weight en VPC empresarial u on-premise | Alta | No hace falta enviar datos a servidores chinos |
| Gobierno, defensa e infraestructura crítica | Muy baja | La restricción de adquisiciones puede alcanzar incluso el linaje del modelo |

La vía más realista es la siguiente.

```text
Desarrollo del modelo chino
→ Rehospedado en AWS, Azure o una VPC empresarial
→ Vendido bajo el marco de seguridad, contratos y auditoría de Occidente
```

Es decir, <strong>la difusión tecnológica de los modelos chinos y la difusión de ingresos de los operadores de API chinos son cosas distintas</strong>. [Inferencia: análisis de vías]

### Los límites de la API directa

La política de privacidad de DeepSeek establece que los datos personales, incluidos los datos de entrada, se <strong>recopilan, procesan y almacenan directamente en China</strong>, y que pueden usarse para mejorar el servicio y el modelo. [Hecho: Política de Privacidad de DeepSeek] Es una condición fatal para empresas que manejan código fuente, información de clientes, datos médicos o financieros, o tecnología sujeta a control de exportación.

Qwen es un poco diferente. Alibaba Cloud Model Studio ofrece regiones en Estados Unidos, Alemania, Japón y Singapur, permite restringir los datos y la inferencia a una región específica, y establece explícitamente que no usa los datos del cliente para entrenar el modelo. [Hecho: política regional y de seguridad de Alibaba Cloud] Por eso, la adopción directa de la API podría aumentar en industrias no reguladas y en el sudeste asiático, Medio Oriente y América Latina.

Sin embargo, la localización de datos y el cumplimiento de SOC 2 <strong>no eliminan el riesgo de interrupción del servicio, sanciones o exposición en las adquisiciones derivado del conflicto entre Estados Unidos y China</strong>. [Inferencia: riesgo residual]

---

## 9. Ajuste de la tesis: qué cambia y qué permanece

<strong>Primero, se debilita la lógica del colapso de los hiperescaladores estadounidenses.</strong> AWS y Azure alojan DeepSeek directamente, ofreciendo aislamiento de datos, SLA y evaluación de seguridad. La nube estadounidense puede absorber la innovación de costos de los modelos chinos y convertirla en ingresos. [Hecho: anuncios oficiales de AWS y Azure]

<strong>Segundo, la presión de precios llega primero a las API de modelos cerrados.</strong> Es una carga para el precio del token y el margen de OpenAI, Anthropic y Google, pero el volumen de inferencia y el uso de AWS y Azure pueden aumentar. Es relativamente favorable para la estrategia de modelos abiertos de Meta.

<strong>Tercero, la separación entre Estados Unidos y China respalda la inversión total en infraestructura.</strong> Ambos bloques <strong>construyen de forma redundante</strong> aceleradores, memoria, redes y redes eléctricas. Disminuye la probabilidad de que la mejora de eficiencia se traduzca directamente en una caída del gasto global en silicio.

<strong>Cuarto, la prima de HBM de SK Hynix puede mantenerse más tiempo dentro del bloque aliado.</strong> Es probable que el HBM de CXMT penetre primero en los aceleradores y centros de datos chinos. La adopción por parte de los CSP occidentales requiere, además de la calificación técnica, una calificación política y de cadena de suministro. Sin embargo, el control de exportaciones acelera la inversión de autosuficiencia de China, lo que representa un riesgo para la cuota de mercado de SK Hynix dentro de China a partir de 2028.

<strong>Quinto, Samsung Electronics es una cobertura relativa.</strong> La inferencia barata y la difusión de modelos abiertos pueden aumentar no solo el HBM, sino también el volumen total de DRAM de servidor, NAND y memoria de propósito general. Del lado opuesto está el riesgo de ser la primera en exponerse al aumento de producción de DRAM de propósito general de CXMT.

---

## 10. El orden de los perjudicados y los beneficiados

1. <strong>Mayor perjuicio</strong>: las ganancias excedentes de las API de modelos cerrados, los operadores de alquiler de GPU con alto apalancamiento
2. <strong>Riesgo intermedio</strong>: operadores con gran inversión previa y concentración de clientes, como Oracle
3. <strong>Meta</strong>: no es la mayor perjudicada. Usa los modelos abiertos para reducir costos, por lo que hay posibilidad de beneficio relativo. La carga recae en el CAPEX y la depreciación
4. <strong>NVIDIA</strong>: el múltiplo y el mix de productos se presionan antes que el EPS de corto plazo. La sustitución dentro de China es un riesgo, pero el foso de CUDA, la red, la eficiencia energética y el tiempo de desarrollo se mantiene
5. <strong>Memoria</strong>: el escenario base no es una caída de la demanda absoluta de HBM, sino <strong>la reducción de la prima de escasez de HBM sumada a la expansión por capas hacia DDR, CXL y eSSD</strong>

---

## 11. Actualización de escenarios

Es razonable ajustar de forma provisional las probabilidades utilizadas en [Valor justo de los semiconductores](/es/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/).

| Escenario | Anterior | Nuevo |
|---|---:|---:|
| Continuación del exceso de demanda | 30% | 30% |
| Reconcentración de activos | 40% | 40% |
| Normalización de oferta y eficiencia | 20% | <strong>25%</strong> |
| Cortocircuito de la demanda sistémica | 10% | <strong>5%</strong> |

El rendimiento de los modelos chinos <strong>reduce la probabilidad de que la demanda de IA misma desaparezca</strong> (de un cortocircuito del 10% al 5%). En cambio, la mejora de eficiencia y el hardware chino reducen la prima de escasez de NVIDIA y del HBM (de una normalización del 20% al 25%).

El escenario en el eje temporal también se puede mantener. El uso le gana a la eficiencia hasta 2027 con 70%, la normalización de mix y precio se produce desde 2028 con 25%, y la contracción del CAPEX total queda en 5%. Sin embargo, <strong>el motor del escenario del 70% cambia de un único ecosistema global a la inversión dual del bloque estadounidense y el bloque chino.</strong> [Inferencia: reajuste de escenario]

---

## 12. Qué confirmaría un cambio de juicio

- <strong>El informe técnico de Kimi K3 (27 de julio)</strong>: si se revela el hardware de entrenamiento, se decide la veracidad de la premisa "entrenamiento de frontera con GPU de gama baja"
- <strong>La tasa de crecimiento de tokens frente a la tasa de caída de memoria por token</strong>: la diferencia entre estos dos valores es la respuesta real a este debate
- <strong>La calificación de producción en masa del HBM3E de CXMT y el volumen real de empaquetado</strong>: si se confirma, hay que bajar juntos el EPS 2028 y el múltiplo de SK Hynix
- <strong>La desaceleración del precio y el contenido de HBM</strong>: la primera señal de reducción de la prima de escasez
- <strong>La expansión del rehosting de modelos chinos por parte de los CSP occidentales</strong>: evidencia del aumento de valor de la distribución en la nube
- <strong>La aplicación real de la regulación de adquisiciones y seguridad de Estados Unidos</strong>: el alcance de la prohibición de facto que opera antes que la legislación

Ahora <strong>no es el momento de mezclar el riesgo terminal con los resultados del período actual</strong>. Basta con ajustar el 2028 en adelante de SK Hynix cuando se confirme la calificación de producción en masa del HBM3E de CXMT. [Inferencia: orden de evaluación]

---

## Cierre

Volviendo a la pregunta, la respuesta es esta.

Es un hecho que los modelos abiertos chinos convergen hacia la frontera estadounidense, y también es un hecho que el costo por unidad de inteligencia se ha desplomado. Pero eso no significa una caída del gasto total en silicio. El alza del CAPEX de TSMC y el aumento del 30% en tokens de Microsoft son la respuesta hasta ahora.

La política estadounidense cambia radicalmente esta interpretación. La separación entre Estados Unidos y China genera una <strong>inversión redundante</strong> en ambos bloques, lo que respalda la demanda total de infraestructura, y dentro del bloque aliado protege políticamente el lugar del stack estadounidense y de la memoria coreana.

La adopción de las API de modelos chinos por parte de la empresa occidental hay que verla <strong>separando el modelo del operador</strong>. La tecnología se difunde como open-weight, pero es probable que quien la venda no sea el operador de API chino, sino AWS, Azure y la VPC empresarial.

Por eso la conclusión es redistribución. Lo que se derrumba son las ganancias excedentes de las API de modelos cerrados, y lo que permanece es la infraestructura basada en uso.

---

_Esta publicación es un análisis que integra papers públicos (DeepSeek V3/V4, Huawei CloudMatrix384), anuncios oficiales de empresas (Kimi, call del 2T26 de TSMC, call del 3T del FY26 de Microsoft, CXMT, Alibaba Cloud, Política de Privacidad de DeepSeek), material del gobierno de Estados Unidos (AI Action Plan, EO 14320, BIS), medidas regulatorias de distintos países e investigación de mercado (TrendForce, JPMAM). El hardware de entrenamiento de Kimi K3 permanece sin confirmar hasta la publicación del informe técnico del 27 de julio, y las estimaciones de capacidad de CXMT y las probabilidades de los escenarios son estimaciones del autor al momento de escribir, no guía de la empresa. Los valores mencionados son ejemplos para explicar la estructura de la cadena de valor y no constituyen una recomendación de compra o venta de ningún valor en particular. La decisión de inversión y su responsabilidad recaen en el propio inversor._

---

### Publicaciones relacionadas

- [Lo que Kimi K3 cambió en el precio de la IA: de Kimi Linear a la estrategia de HBM y las Big Tech](/es/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/)
- [¿Son los semiconductores cíclicos? ¿Cuál es su valor justo?](/es/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [El verdadero debate entre el argumento alcista y bajista de los semiconductores: cuatro relojes reales y un reloj bursátil](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [La IPO de CXMT y el riesgo de precios de memoria: hay que separar el riesgo de HBM del riesgo de DRAM cliente](/es/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)
- [Investigación profunda de oferta y demanda de HBM 2030: disecamos el modelo de demanda de 26,7EB y lo verificamos cruzadamente con el calendario de ampliación](/es/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
