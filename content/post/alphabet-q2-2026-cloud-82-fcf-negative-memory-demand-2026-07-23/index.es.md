---
title: "Alphabet en el segundo trimestre: Cloud +82% cierra el debate de la demanda, el FCF negativo abre el del efectivo"
slug: "alphabet-q2-2026-cloud-82-fcf-negative-memory-demand-2026-07-23"
date: 2026-07-23T11:00:00+09:00
description: "El segundo trimestre de Alphabet redujo con fuerza la probabilidad de un precipicio de demanda de IA después de 2028: Cloud creció 82%, el backlog llegó a 514.000 millones USD y los clientes consumen 50% por encima de sus compromisos. El mismo informe trajo el primer FCF trimestral negativo, una guía de CAPEX 2026 elevada hasta 205.000 millones y el alquiler de cómputo a SpaceX por unos 920 millones al mes. Leemos el fin del debate de demanda y el inicio del debate de caja, lo traducimos a HBM, DRAM de servidor y eSSD, y preparamos las tarjetas de puntuación de Microsoft y Amazon."
categories: ["Exclusive Analysis", "Company-Analysis", "Market-Outlook"]
tags: ["Alphabet", "Google Cloud", "CAPEX de IA", "TPU", "HBM", "DRAM de servidor", "Memoria IA", "FCF", "Backlog", "Resultados Big Tech", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexto
> En [¿Quién quema todos esos tokens?](/es/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/) escribimos que el último eslabón débil del debate del CAPEX de IA, la demanda final, empezaba a tener números, y dejamos el veredicto para la temporada de resultados de alrededor del 30 de julio. La primera hoja de calificación llegó antes de lo previsto. Alphabet presentó sus resultados del segundo trimestre de madrugada, hora de Corea, el 23 de julio. Este artículo sintetiza en uno dos notas de análisis que diseccionan el mismo informe desde ángulos distintos. Dicho por adelantado, el debate de la demanda terminó en la práctica y el escenario de la discusión se trasladó al flujo de caja y al retorno de capital.

## TL;DR

- Los ingresos de Cloud llegaron a 24.800 millones USD, <strong>+82%</strong> (consenso +64%), con lo que la tasa de crecimiento marcó una aceleración de cinco trimestres consecutivos: 32%, 34%, 48%, 63% y 82%. El backlog pasó de 462.000 millones USD a <strong>514.000 millones USD</strong>, un aumento neto de 52.000 millones USD incluso mientras se reconocía más ingreso.
- La calidad de la demanda importa más todavía. Los clientes de Cloud ya existentes están gastando en promedio <strong>50% o más por encima de su compromiso inicial</strong>, y el volumen de procesamiento de la API de los modelos Gemini subió a 22.000 millones de tokens por minuto, un incremento de 37,5% en un solo trimestre. Como la oferta no alcanza, desde junio Alphabet empezó a pagarle <strong>a SpaceX unos 920 millones USD al mes</strong> por alquilar cómputo de IA. Es la primera vez que se ve a un hyperscaler convertirse en comprador neto de cómputo.
- En la otra cara del mismo informe, el FCF trimestral quedó en <strong>-5.900 millones USD, la primera vez en negativo</strong>. El CAPEX de 44.900 millones USD superó al flujo de caja operativo de 39.100 millones USD, la guía de CAPEX 2026 se revisó al alza desde 180.000-190.000 millones USD hasta <strong>195.000-205.000 millones USD</strong>, y se anticipó también un aumento considerable para 2027.
- El juicio se divide en tres. La probabilidad de un precipicio de demanda de IA después de 2028 bajó todavía más. El giro a FCF positivo de Alphabet se corrió del horizonte de 2027 al tramo 2028-2029. Para la memoria se reconfirmó la fortaleza de la demanda en volumen, pero la persistencia del precio y del margen pico sigue siendo una cuestión aparte.
- Mantenemos la probabilidad de los escenarios de demanda 45/35/20. Aun así, se sumó otra vía de evidencia real a favor del escenario al alza del 35%, y este informe debilitó la desaceleración temprana del CAPEX de las grandes tecnológicas, la premisa central del escenario a la baja del 20%. La próxima calificación llega con Microsoft (30 de julio, hora de Corea) y Amazon (31 de julio).

<div class="thesis-callout">
<div class="thesis-callout__label">Marco clave</div>

Cloud +82% y el primer FCF trimestral negativo son las dos caras del mismo informe. A la pregunta de si la demanda es real, Alphabet respondió con un uso que supera los compromisos contractuales y con la decisión de pagar de más por alquilar servidores ajenos. A cambio, la factura por atender esa demanda llegó antes de lo previsto. El criterio de calificación del mercado pasó de la existencia de la demanda al retorno de caja después de la depreciación, y para el inversor de memoria este informe es un refuerzo de volumen, no una garantía de margen.

</div>

## 1. Primero los números: qué se reportó

| Concepto | 2T26 real | Base de comparación | Veredicto |
|---|---|---|---|
| Ingresos totales | 119.800 millones USD, +24% | Consenso de unos 116.900 millones USD | Supera |
| Ingresos de Google Cloud | 24.800 millones USD, +82% | Consenso de 22.400 millones USD, +64% | Supera ampliamente |
| Beneficio operativo de Cloud | 8.800 millones USD (margen 35,6%) | Año previo 2.800 millones USD (margen 20,7%) | Mejora |
| Ingresos de Search | 63.300 millones USD, +17% | Consenso de 63.400 millones USD | En línea |
| Beneficio operativo total | 40.800 millones USD, +30% (margen 34,0%) | El margen queda por debajo del consenso | Mixto |
| BPA ajustado | Unos 2,85 USD | Consenso de unos 2,89 USD | Ligeramente por debajo |
| Flujo de caja operativo | 39.100 millones USD | CAPEX de 44.900 millones USD | Se invierte |
| FCF trimestral | -5.900 millones USD | Trimestre previo 10.100 millones USD | Primera vez en negativo |
| Backlog de Cloud | 514.000 millones USD | Trimestre previo 462.000 millones USD | +52.000 millones USD |
| Guía de CAPEX 2026 | 195.000-205.000 millones USD | Anterior 180.000-190.000 millones USD | Revisada al alza |

[Hecho: divulgación de Alphabet y llamada de resultados]

Los números GAAP tienen una ilusión óptica. El BPA GAAP divulgado fue de 9,11 USD y el beneficio neto de 112.100 millones USD, un aumento de 298% interanual, pero ahí dentro hay una ganancia no realizada de unos 99.000 millones USD antes de impuestos (unos 6,26 USD por acción después de impuestos) sobre participaciones no cotizadas como Anthropic y SpaceX. Si se retira esta partida ajena a la operación, el BPA real queda en aproximadamente 2,85 USD, un poco por debajo de lo que esperaba el mercado. Los ingresos y Cloud ganaron con holgura, pero la calidad del beneficio no fue tan fuerte como sugiere el número de superficie. [Hecho: recálculo sobre la divulgación]

## 2. El debate de la demanda: por qué consideramos que terminó en la práctica

En el artículo anterior señalamos el eslabón débil de la demanda final y citamos como primera evidencia real los 3 millones de usuarios que sumó Codex en tres días. El informe de Alphabet añadió cuatro vías más de evidencia real sobre esa base.

<strong>El uso va por delante del contrato.</strong> El volumen de procesamiento de la API de los modelos Gemini subió de 16.000 millones a 22.000 millones de tokens por minuto, un 37,5% en un solo trimestre, y los desarrolladores mensuales superaron los 9 millones. Los clientes de Cloud ya existentes gastan en promedio 50% o más por encima de su compromiso inicial, y ese exceso fue mayor que en el trimestre anterior. La velocidad de captación de nuevos clientes duplica la del año anterior, y el volumen del Marketplace es siete veces mayor. [Hecho: carta del CEO y llamada de resultados] La hipótesis de que la demanda descansa solo en contratos de largo plazo de un puñado de laboratorios de frontera no es compatible con datos donde el consumo real después de firmado el contrato supera lo comprometido.

<strong>La base de clientes se amplió.</strong> Además de la demanda de desarrollo de modelos, como el gran preentrenamiento de Gemini 4, se presentaron a la vez cinco frentes: inferencia empresarial en finanzas, farmacéutica, retail, telecomunicaciones y manufactura; cargas de trabajo de BigQuery y seguridad; servicios de consumo como AI Mode de Search y la app de Gemini; y la venta externa de sistemas TPU entregados directamente a los centros de datos de los clientes. Cerca del 90% de las empresas del Fortune 100 usan Gemini Enterprise, y ya son 500 los clientes de Cloud que procesan más de 1 billón de tokens al año, y más de 2.000 los que superan los 100.000 millones. [Hecho: carta del CEO]

<strong>La oferta todavía limita el crecimiento.</strong> El CFO insistió en que el entorno sigue siendo de restricción de oferta. Para cubrir el déficit de corto plazo, la compañía está alquilando capacidad de centros de datos de terceros a precios altos, y explicó que, para quedarse con clientes grandes, vale la pena aceptar unos seis meses de ineficiencia. En esa misma línea llegó la noticia más importante de la llamada: desde junio Alphabet firmó un contrato para alquilarle a SpaceX cómputo de IA por unos 920 millones USD al mes, unos 11.000 millones USD anualizados. [Hecho: llamada de resultados y prensa] Que la empresa que mejor calcula del mundo pague de más por alquilar servidores ajenos es una evidencia de comportamiento que choca de frente con la hipótesis de una demanda sobreestimada.

<strong>El backlog creció incluso mientras se reconocía.</strong> Los ingresos de Cloud del segundo trimestre subieron cerca de 23,8% frente al trimestre anterior, señal de que los contratos grandes se están convirtiendo en ingreso a buen ritmo, y aun así el saldo del backlog sumó otros 52.000 millones USD. El backlog actual equivale a unas 5,2 veces los ingresos anualizados de Cloud del segundo trimestre, y la compañía informó que más de la mitad se reconocerá dentro de 24 meses. [Hecho: divulgación y llamada de resultados] Como evidencia de visibilidad hasta 2027 es sólida. Sin embargo, no se divulgó la concentración por cliente ni el monto de reconocimiento año por año más allá de 2028. [Sin verificar: detalle del backlog no divulgado]

El contraargumento de la eficiencia también perdió fuerza este trimestre. El costo por respuesta de AI Mode bajó a su nivel más bajo desde el lanzamiento, y aun así los usuarios y el volumen de consultas crecieron todavía más rápido. AI Mode tiene 1.000 millones de usuarios mensuales, y la app de Gemini llega a 950 millones de MAU. La relación según la cual el aumento de uso supera la caída del costo unitario, ya vista en Codex, se confirmó también a la escala de Alphabet, en la misma dirección que el patrón de Jevons. [Inferencia: relación entre eficiencia y uso]

## 3. El debate de la caja: la factura llegó antes de lo previsto

En el lado opuesto de la demanda, lo que este informe confirmó fue la magnitud y la duración del gasto.

El CAPEX del segundo trimestre, 44.900 millones USD, duplicó el del año anterior y superó al flujo de caja operativo de 39.100 millones USD; la intensidad de capital trimestral (CAPEX sobre flujo de caja operativo) quedó en aproximadamente 115%. La aritmética también pesa. El CAPEX del primer semestre fue de unos 80.600 millones USD, así que para llegar al extremo superior de la guía anual de 205.000 millones USD hace falta gastar en el segundo semestre un promedio trimestral de 57.200-62.200 millones USD, es decir, 27-38% más que en el segundo trimestre. Es poco probable que el FCF se recupere de forma significativa en el segundo semestre de 2026 y en 2027. [Inferencia: aritmética propia]

También apareció una pista sobre 2027. El CFO mantuvo la previsión de un aumento considerable del CAPEX en 2027, y el consenso de mercado ronda los 257.000 millones USD. La trayectoria de 205.000 a 257.000 millones USD implica una tasa de crecimiento de aproximadamente +25%. Eso está sobre una senda de desaceleración que va de un +76% este año a un +25% el próximo, todavía no sobre un escenario de reaceleración hacia los 300.000 millones USD. [Hecho: llamada de resultados y consenso] Esta distinción importa. Si es una senda de desaceleración, el esqueleto de la lógica de giro a FCF sigue en pie; si es reaceleración, el esqueleto mismo se derrumba.

Calcular una sensibilidad para 2028 deja más nítido el criterio de juicio. El punto de partida es el flujo de caja operativo acumulado de los últimos 12 meses, 185.700 millones USD.

| Supuesto de CAPEX 2028 | OCF necesario para FCF cero | Crecimiento anual compuesto necesario | OCF necesario para FCF de 50.000 millones USD | Crecimiento necesario |
|---|---|---|---|---|
| 200.000 millones USD | 200.000 millones USD | ~3,8% | 250.000 millones USD | ~16,0% |
| 230.000 millones USD | 230.000 millones USD | ~11,3% | 280.000 millones USD | ~22,8% |
| 250.000 millones USD | 250.000 millones USD | ~16,0% | 300.000 millones USD | ~27,1% |

[Inferencia: sensibilidad propia, no es guía de la compañía]

Si el CAPEX se estabiliza en torno a 200.000 millones USD en 2028, la recuperación del FCF no es difícil. Si sigue subiendo hacia 230.000-250.000 millones USD, el flujo de caja operativo combinado de Cloud y Search tendría que crecer más de 20% anual para volver al nivel histórico de FCF. No es un número imposible si Cloud sostiene por un tiempo el +82% y el margen de 35,6%, pero la depreciación, la energía, el alquiler externo y una mezcla de ventas de hardware TPU de menor margen empujan en sentido contrario.

El giro en el régimen de asignación de capital también se formalizó este trimestre. Con 242.500 millones USD en efectivo y valores negociables y 185.700 millones USD de flujo de caja operativo de los últimos 12 meses, la capacidad de pago de Alphabet no es en sí un tema de debate. Pero en el segundo trimestre la compañía captó unos 30.500 millones USD en acciones ordinarias, unos 19.100 millones USD en acciones preferentes convertibles y unos 21.100 millones USD en deuda neta, y no hubo recompras de acciones. La deuda pasó de unos 16.000 millones USD a unos 100.000 millones USD en 12 meses. [Hecho: divulgación] Una compañía que antes cubría con su flujo de caja operativo tanto el CAPEX como las recompras se transformó en una que detiene las recompras y moviliza deuda y capital accionario para financiar el CAPEX. No es una señal de riesgo de liquidez sino de que cambió el régimen de asignación de capital, y que el peso del financiamiento recaiga más sobre los accionistas que sobre el mercado de deuda es, desde la óptica crediticia, un consuelo.

## 4. Calificación de tres preguntas

Si calificamos tres preguntas frente a este informe, el resultado es el siguiente.

<strong>¿Se sostiene la demanda de IA después de 2028? La probabilidad de un precipicio bajó todavía más.</strong> La demanda se está difundiendo del entrenamiento hacia la inferencia, los datos, la seguridad y el trabajo empresarial; el consumo real supera lo comprometido; el aumento de uso es más rápido que la mejora de eficiencia; la mayor parte de los ingresos por venta externa de TPU se reconocerá en 2027; y la oferta es tan escasa que hace falta seguir aumentando mucho el CAPEX incluso en 2027. Es más preciso ver 2028 no como el momento en que termina la demanda, sino como el momento en que la nueva capacidad de oferta entra en pleno funcionamiento y sube al banco de pruebas.

<strong>¿El FCF de Alphabet da un giro? Es posible, pero el momento se corrió hacia atrás.</strong> El cruce del FCF trimestral a negativo llegó antes de lo previsto originalmente (inicios de 2027), y aun proyectando de forma optimista un flujo de caja operativo 2027 de 230.000-240.000 millones USD, con un CAPEX de 257.000 millones USD el FCF anual queda en cero o menos. El regreso a positivo se ubica en 2028, y solo si la tasa de crecimiento del CAPEX 2028 baja a un dígito. Una reaceleración fuerte del FCF es un escenario condicional para el tramo 2028-2029.

<strong>¿Se traduce en compras sostenidas de memoria? Fuerte señal positiva en volumen, neutral en precio y margen.</strong> Lo desglosamos en la siguiente sección.

## 5. Traducción a la memoria: refuerzo de volumen, no garantía de margen

Del CAPEX de infraestructura técnica del segundo trimestre, aproximadamente 60% fue a servidores y 40% a centros de datos y red. La inversión en servidores incluye a la vez TPU, GPU, CPU, HBM, DRAM de servidor, SSD y semiconductores de red. [Hecho: llamada de resultados]

Los factores que sostienen la demanda de HBM son claros: la nueva generación de TPU y la adopción de NVIDIA Vera Rubin, el gran preentrenamiento de Gemini 4, el aumento del volumen de inferencia empresarial, la arquitectura de red de próxima generación que conecta 1 millón de aceleradores, y la venta externa de sistemas TPU que se reconocerá de lleno a partir de 2027. Importa que, aunque el TPU propio sustituya en parte a la GPU de NVIDIA, la demanda de HBM no desaparece, solo se traslada el canal de compra de la cadena de suministro de GPU a la de sistemas TPU. Si a esto se suma el alquiler de cómputo de terceros, el canal de demanda de HBM y DRAM de servidor se amplió a tres vías: centro de datos propio, venta externa de TPU y cómputo alquilado. [Inferencia: descomposición de canales de demanda]

El argumento a favor de la DRAM de servidor y el eSSD también se reforzó con este informe. Los agentes de IA no usan solo aceleradores, también corren preprocesamiento, gestión de estado, seguridad y orquestación en servidores CPU. Alphabet destacó a la vez el CPU Axion y el aumento de las cargas de trabajo de datos y seguridad. La cifra de 500 clientes de Cloud que procesan más de 1 billón de tokens al año muestra que la demanda de almacenamiento, que se extiende a logs, checkpoints, índices de búsqueda y bases de datos vectoriales, no se limita al entrenamiento. [Hecho: carta del CEO] El trasfondo de demanda detrás del reagravamiento de la DRAM de servidor visto en el artículo anterior (previsión de +13-18% en el precio de contrato del 3T, plazos de entrega de 40 semanas) quedó reconfirmado con los resultados de una gran tecnológica.

Aun así, no hay que subir la estimación de beneficio 2028 de las memoreras solo con base en este informe. Igual que se dispara la compra de equipos, la capacidad de oferta de memoria también crecerá en 2027-2029. La expansión de los chips propios reduce el poder de fijación de precios de NVIDIA a nivel de sistema, el costo de inferencia por respuesta cae con rapidez, y si Alphabet empieza a ajustar la eficiencia del CAPEX, la presión a la baja sobre el precio de los componentes bajará por la cadena de suministro. El precio alto de HBM4 y de la próxima generación de HBM incorpora una prima de escasez inicial de generación y de rendimiento de producción, así que no es un valor permanente. En conjunto, queda así.

| Concepto | Juicio antes del informe | Juicio después del informe |
|---|---|---|
| Demanda de bits de aceleradores de IA y HBM | Alta | Muy alta |
| Demanda de DRAM de servidor y eSSD | Media-alta | Alta |
| Empaquetado avanzado y red | Alta | Muy alta |
| Precipicio de demanda en 2028 | Poco probable | Aún menos probable |
| Persistencia del ASP de memoria | Incierta | Incierta |
| Persistencia del margen pico de memoria | Baja | Baja |
| Recuperación temprana del FCF de las grandes tecnológicas | Media | Más baja |
| Retorno de capital incremental del CAPEX | No demostrado | Parcialmente demostrado, verificación en curso |

[Inferencia: juicio de síntesis]

El riesgo para los semiconductores en 2028 no es la cancelación de pedidos, sino la normalización del ASP y del margen. Esto es coherente con los escenarios de demanda 45/35/20. Este informe sumó una evidencia real más al argumento del 35% al alza, y debilitó la desaceleración temprana del CAPEX de las grandes tecnológicas, la premisa del 20% a la baja. La probabilidad en sí se actualizará después de confirmar también con Microsoft y Amazon. Desde la óptica de Samsung Electronics y SK Hynix, es un informe que mejora el trasfondo de demanda de cara a la negociación de precios de HBM para 2027 que arrancará en el cuarto trimestre.

## 6. La reacción de la acción y la diferencia de juicio entre las dos notas

La reacción del mercado resume el carácter de esta fase. Nada más difundirse el informe, la acción abrió en el fuera de horario con una caída de alrededor de 2%, llegó a recuperarse hasta terreno levemente positivo, y volvió a caer cuando en la llamada se conoció el alza del CAPEX, con lo que la caída se amplió hasta un rango de 3-5%. A la mañana del 23 de julio, hora de Corea, la acción cotizaba en torno a 342 USD, cerca de 1,5% por debajo del cierre del día anterior, de unos 347 USD. [Hecho: datos de cotización] Se repitió por quinta vez la regla de 2026 según la cual, en un mercado donde superar el consenso ya es el escenario base, lo que decide la reacción es el CAPEX. Leído al revés, que la caída se quedara en este rango frente a un crecimiento de +82% es también una señal de que, mientras el crecimiento se demuestre, el mercado sigue digiriendo el gasto.

Las dos notas que sirvieron de material para esta síntesis llegaron a conclusiones distintas a partir de los mismos hechos. Una optó por la espera con el criterio de la prueba estructural. La expresión exacta no es que el retorno de capital ya esté demostrado, sino que es lo más probable que llegue a demostrarse, y ante el FCF negativo, el financiamiento de capital y el aviso de un aumento en 2027, dejó en suspenso el cálculo de un precio objetivo. La otra mantuvo una recomendación de compra en función del precio de entrada. Sobre la premisa de un precio ya ajustado 15% desde el máximo, propuso un objetivo a 12 meses de 430 USD aplicando un múltiplo de 28-29 veces a un BPA 2027E sin plusvalías de unos 15 USD, con la condición de retirarlo si el CAPEX 2027 se cuantifica cerca de 300.000 millones USD. [Hecho: conclusiones de las dos notas]

La diferencia entre los dos juicios no está en el reconocimiento de los hechos, sino en el horizonte y el criterio. La óptica estructural le carga a la empresa la responsabilidad de probar, hasta que el retorno de caja después de la depreciación se confirme en números; la óptica de precio calcula cuánto de ese riesgo ya está incorporado en una cotización ya ajustada. Siguiendo el principio de este blog, no recomendamos una dirección concreta y presentamos ambos marcos en paralelo, pero el denominador común es claro. Sea cual sea el marco, la siguiente variable de juicio ya no es la demanda, sino la caja.

## 7. Tarjeta de puntuación: las próximas dos semanas deciden

Repasamos qué casillas llenó este informe y cuáles quedaron recién abiertas.

- La parte de Alphabet en los comentarios de CAPEX de las grandes tecnológicas quedó confirmada al alza. Lo que falta es la primera guía de FY27 de Microsoft (llamada de madrugada del 30 de julio, hora de Corea) y la tasa de crecimiento de AWS de Amazon (madrugada del 31 de julio). Si Alphabet cerró el debate de la demanda, estas dos empresas van a decidir el debate del margen y del FCF.
- El indicador de confirmación al alza es si la tasa de crecimiento de Cloud se mantiene por encima de 50% durante los próximos 2-4 trimestres y si el margen aguanta por encima de 30%. Si, una vez aliviada la restricción de oferta, la tasa de crecimiento cae por debajo de 30%, habrá que recalcular la posibilidad de una demanda sobreestimada.
- Vigilamos si el backlog sigue sumando de forma neta incluso después del reconocimiento de ingresos. Una combinación de backlog en descenso, o de que solo aumente la extensión del plazo de los contratos, es señal de deterioro en la calidad contractual.
- El trimestre en que la tasa de crecimiento del flujo de caja operativo a 12 meses supere la tasa de crecimiento del CAPEX será el punto de partida del giro del FCF. En sentido contrario, si el CAPEX 2028 supera los 250.000 millones USD y el flujo de caja operativo no lo alcanza, lo calificaremos como un daño estructural al FCF.
- Los ítems de verificación del lado de la eficiencia de capital son si continúan nuevas rondas grandes de captación de acciones o deuda, si el alquiler externo de tipo SpaceX se reduce en 2027-2028, y si la venta externa de TPU se traduce en consumo recurrente de Cloud.
- El factor decisivo del lado de la memoria no cambia. Es el precio de contrato del DRAM, y su confirmación para el tercer trimestre en las llamadas de resultados de Samsung Electronics y SK Hynix de alrededor del 30 de julio.

---

Las acciones mencionadas en el texto son ejemplos para el análisis y no constituyen una recomendación de compra o venta de ningún valor en particular. La decisión de inversión y la responsabilidad por sus resultados recaen en cada inversor. Alphabet no presentó guía de CAPEX ni de ingresos de Cloud para 2028, no se divulgó la concentración por cliente del backlog de 514.000 millones USD ni el monto de reconocimiento año por año ni las condiciones de cancelación, y tampoco están sujetos a divulgación el volumen de compra de HBM, DRAM y NAND ni su reparto por proveedor. La sensibilidad de FCF 2028 y la aritmética de CAPEX del segundo semestre son estimaciones propias que toman como punto de partida la divulgación actual, no una previsión de la compañía. La magnitud antes de impuestos de la ganancia no realizada sobre participaciones no cotizadas y su efecto después de impuestos por acción son un recálculo hecho sobre la divulgación y pueden tener diferencias de redondeo. El precio objetivo de 430 USD es el cálculo de una de las notas que se sintetizaron, no un precio objetivo de este blog. Los precios y las cotizaciones corresponden a la mañana del 23 de julio de 2026, hora de Corea.

### Publicaciones relacionadas

- [¿Quién quema todos esos tokens? El mapa de clientes de NVIDIA, la IA soberana y los 9 millones de Codex empiezan a responder](/es/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/)
- [¿Superará la demanda de memoria para IA las expectativas? Las probabilidades de sobrecrecimiento según los escenarios de demanda y el mapa de oferta](/es/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/)
- [Dos meses de declaraciones del presidente de SK Hynix, Chey Tae-won: la empresa se fortalece, el pico de margen queda atrás](/es/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/)
- [El verdadero debate en semiconductores: cuatro relojes físicos y un reloj bursátil](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
