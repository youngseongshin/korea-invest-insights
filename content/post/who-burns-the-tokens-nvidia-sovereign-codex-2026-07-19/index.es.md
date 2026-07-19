---
title: "¿Quién quema todos esos tokens? El mapa de clientes de NVIDIA, la IA soberana y los 9 millones de Codex empiezan a responder"
slug: "who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19"
date: 2026-07-19T19:00:00+09:00
description: "La pregunta que nunca desapareció del debate sobre el CAPEX de IA era quién usaría toda esa infraestructura. En los libros de NVIDIA, los ingresos no-hyperscale alcanzaron la paridad con los hyperscale y su tasa de crecimiento trimestral ya se invirtió. Los ingresos de IA soberana se triplicaron en un año, el equipo de semiconductores de Meritz rebatió el marco estrecho del mercado con un DRAM de servidor que vuelve a tensarse, y Codex sumó tres millones de usuarios en tres días. Verificamos de forma cruzada la evidencia del lado de la demanda y su significado para los escenarios 45/35/20."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["NVIDIA", "IA soberana", "Codex", "Memoria IA", "DRAM de servidor", "HBM", "Samsung Electronics", "SK Hynix", "CAPEX de IA", "IA agéntica", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexto
> En [¿Superará la demanda de memoria para IA las expectativas?](/es/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/) pusimos en probabilidad la demanda en escenario base 45%, al alza 35% y a la baja 20%, y en [Dos meses de declaraciones del presidente de SK Hynix, Chey Tae-won](/es/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/) leímos la voz y la mano de la cúpula de la oferta. El eslabón débil que queda es la demanda final. Con tanta GPU y tanto HBM desplegándose, ¿quién quema todos esos tokens? Este artículo registra la semana en que esa pregunta empezó a tener números.

## TL;DR

- En los ingresos de centro de datos de NVIDIA, la proporción de hyperscale lleva siete trimestres seguidos rondando el 50%. La proporción no se ha derrumbado todavía. Lo que cambió es la composición. En el trimestre de febrero-abril de 2026, <strong>los ingresos no-hyperscale (ACIE) de 37.000 millones USD alcanzaron una paridad de facto con los 38.000 millones USD de hyperscale</strong>, y la tasa de crecimiento trimestral ya se invirtió, 31% frente a 12%. En la próxima divulgación, la proporción misma podría voltearse por primera vez.
- En el mismo período, la tasa de crecimiento interanual de los ingresos de centro de datos se reaceleró de +56% a +66%, +75% y +92%. Que la proporción se mantenga mientras el conjunto vuelve a acelerar significa que <strong>el crecimiento incremental lo está impulsando lo que queda fuera de hyperscale</strong>. La propia NVIDIA escribió en su divulgación que el crecimiento lo lideró el resto de los clientes.
- Los ingresos de IA soberana superaron los 30.000 millones USD en todo el año fiscal 2026, más que triplicando el año anterior, y en el trimestre más reciente también crecieron más de 80% interanual. Es el comprador que se le escapó a un mercado que solo miraba la boca de los hyperscalers.
- El equipo de semiconductores de Meritz Securities señaló en su informe dominical que la compra soberana se está intensificando y que la escasez de DRAM de servidor volvió a agravarse desde mediados de julio. La previsión de TrendForce de +13-18% intertrimestral en el precio de contrato de DRAM de servidor para el tercer trimestre, el testimonio de la taiwanesa Inventec sobre plazos de más de 40 semanas, y la declaración de Micron de que solo cubre 50-66% de la demanda de sus clientes clave lo confirman de forma cruzada desde fuera.
- También aparecieron números del lado de la demanda final. Codex de OpenAI pasó de 1 millón en febrero a 5 millones a finales de mayo, y de 6 millones el 12 de julio, justo tras el lanzamiento de GPT-5.6, a 9 millones alrededor del 15 de julio, <strong>sumando 3 millones de usuarios en tres días</strong>. Es el tramo en que la unidad de la demanda pasa de número de suscriptores a horas de ejecución de agentes.
- La conclusión no es subir las probabilidades de forma apresurada. Es que, antes de discutir el exceso de oferta, llegó el momento de reverificar si <strong>dibujamos la demanda con demasiada modestia</strong>, y que ese veredicto lo dictarán la temporada de resultados de alrededor del 30 de julio y la divulgación de NVIDIA de finales de agosto.

<div class="thesis-callout">
<div class="thesis-callout__label">Marco clave</div>

El mercado ha dudado de la sostenibilidad del CAPEX de IA mirando solo la boca de cuatro grandes tecnológicas. Mientras tanto, en los libros de NVIDIA los ingresos no-hyperscale alcanzaron la paridad con los hyperscale, los ingresos soberanos se triplicaron en un año, y Codex sumó 3 millones de usuarios en tres días. Mientras el precio de la acción reflejaba primero el miedo al exceso de oferta, la base de la demanda acumulaba evidencia en la dirección contraria. Esta asimetría es la esencia de esta fase de corrección.

</div>

## 1. Qué tipo de semana fue: entre el límite a la baja y los informes

Primero, confirmamos el escenario. El jueves 16 de julio, en el mercado estadounidense, el índice de semiconductores de Filadelfia (SOX) se desplomó cerca de -4% y entró en territorio de mercado bajista, más de 20% por debajo de su máximo, mientras el Nasdaq cayó -1,47%. El viernes 17, el Nasdaq bajó otro -1,40%, con lo que la caída semanal llegó a -2,90%. [Hecho: datos de mercado] Ese mismo día, en Tokio, Kioxia se hundió en el límite a la baja nada más abrir y cayó -16,1%. La acción quedó a la mitad de su máximo del 22 de junio y se esfumaron cerca de 30 billones JPY de capitalización bursátil. El disparador directo fue el veredicto de un jurado estadounidense que reconoció una indemnización de patentes a Viasat de unos 229 millones USD, pero la esencia era el desapalancamiento de todo el rally de IA, como mostró la caída conjunta en la misma sesión de TSMC -7,29%, el ADR de SK Hynix -13,69% y SanDisk -12,63%. [Hecho: informes de Nikkei y Korea Economic Daily]

El mercado coreano esquivó ese viernes. El 17 de julio fue día festivo por el Día de la Constitución, redesignado como feriado por primera vez en 18 años. Pero justo antes ya había sufrido caídas fuertes: el 13 de julio, SK Hynix -15,37% y Samsung Electronics -10,70%; el 16 de julio, SK Hynix -12,34% y Samsung Electronics -9,47%. [Hecho: datos de la bolsa] El relato que el mercado está incorporando al precio es claro. Que la oferta aumenta, que China se acerca, que el beneficio de 2027 se está revisando a la baja, y que no se sabe cuándo va a quebrar el CAPEX de las grandes tecnológicas.

En esta fase, el domingo salieron a la vez los informes de los analistas Kim Sun-woo, Yang Seung-su y Kim Dong-kwan, del equipo de semiconductores de Meritz Securities. El momento de publicación reacciona de frente a la caída del viernes y al episodio de Kioxia. El argumento va en dirección contraria. Que la demanda de memoria actual no viene solo de los hyperscalers, que la compra del bloque soberano, incluido Oriente Medio, se está intensificando, y que desde mediados de julio la escasez de DRAM de servidor vuelve a agravarse. Es una refutación a la mirada que da por hecho el alivio del shortage en 2028 sin incorporar esta demanda al cálculo. [Hecho: síntesis del informe de Meritz Securities, 19-07-2026]

En lugar de dejarlo en una discusión verbal, dividimos este argumento en tres piezas verificables y las contrastamos una por una con evidencia real: la composición de clientes de NVIDIA, la compra soberana, y el uso final.

## 2. El mapa de clientes de NVIDIA: la proporción se queda en 50%, el crecimiento viene de fuera

Empezamos por verificar con precisión la premisa de que la proporción de los hyperscalers se está reduciendo. Si ordenamos en serie temporal el texto que NVIDIA divulga cada trimestre, esto es lo que se ve.

| Trimestre fiscal | Período | Ingresos DC | Interanual | Proporción de grandes CSP y hyperscale (texto de la divulgación) |
|---|---|---|---|---|
| FY25 T3 | ago-oct 2024 | 30.770 millones USD | +112% | ~50% |
| FY25 T4 | nov 2024-ene 2025 | 35.580 millones USD | +93% | ~50% |
| FY26 T1 | feb-abr 2025 | 39.110 millones USD | +73% | justo por debajo del 50% |
| FY26 T2 | may-jul 2025 | 41.100 millones USD | +56% | ~50% |
| FY26 T3 | ago-oct 2025 | 51.220 millones USD | +66% | no divulgado |
| FY26 T4 | nov 2025-ene 2026 | 62.310 millones USD | +75% | ligeramente por encima del 50%, crecimiento liderado por el resto de clientes |
| FY27 T1 | feb-abr 2026 | 75.200 millones USD | +92% | hyperscale 38.000 millones USD (~50%) frente a ACIE 37.000 millones USD |

[Hecho: comentario del CFO de NVIDIA y llamada de resultados]

Se ven dos cosas a la vez. Primero, <strong>la cifra de proporción en sí no se ha salido de la banda del 50% en siete trimestres seguidos</strong>. El relato de que los hyperscalers ya quedaron desplazados no es evidencia real. Segundo, aun así, la dirección de la composición cambió con claridad. La divulgación del FY26 T4 dejó explícito que el crecimiento lo lideró el resto de los clientes y que los ingresos se diversificaron, y desde el FY27 T1 NVIDIA empezó a divulgar el centro de datos separando hyperscale de ACIE (nube de IA, industria, empresa). En ese primer trimestre, ACIE llegó a 37.000 millones USD, casi a la par de los 38.000 millones USD de hyperscale, y la tasa de crecimiento trimestral se invirtió a <strong>ACIE +31% frente a hyperscale +12%</strong>. Los ingresos de nube de IA dentro de ACIE superaron el triple interanual. El CEO Jensen Huang remarcó en la llamada que, a largo plazo, la segunda categoría crecerá más rápido. [Hecho: llamada de resultados]

Si superponemos aquí la reaceleración de la tasa de crecimiento, el cuadro queda completo. La tasa de crecimiento interanual de los ingresos de centro de datos tocó un mínimo de +56% en el FY26 T2 y volvió a subir a +66%, +75% y +92%. Que la proporción se mantenga mientras el crecimiento total se acelera significa, aritméticamente, que <strong>más de la mitad del incremento lo está generando lo que queda fuera de hyperscale</strong>. [Inferencia: aritmética de la divulgación] Si esta tendencia continúa un trimestre más, la divulgación del FY27 T2 de finales de agosto marcará la primera vez que ACIE supere a hyperscale. A partir de ese momento, el propio marco de juzgar la sostenibilidad de la demanda de IA mirando solo la guía de CAPEX de cuatro grandes tecnológicas quedará obsoleto.

Conviene aclarar una posible confusión. La concentración de clientes directos del 10-Q (Cliente A 22%, Cliente B 14%) en realidad aumentó, pero ese es un indicador de la etapa de distribución que agrupa a socios de placas, OEM y grandes compras directas, una capa distinta de la diversificación del usuario final. [Hecho: 10-K] Que la distribución se concentre y que la demanda final se amplíe son dos fenómenos que se cumplen a la vez.

## 3. IA soberana: el comprador que se le escapó al mercado que solo miraba la boca

El bloque más grande de la demanda no-hyperscale es el soberano. El CFO de NVIDIA informó que los ingresos de IA soberana del FY2026 <strong>superaron los 30.000 millones USD</strong>, más del triple del año anterior. Lo lideraron Canadá, Francia, Países Bajos, Singapur y el Reino Unido, y en el FY27 T1 los ingresos soberanos también crecieron más de 80% interanual; la infraestructura de NVIDIA ya está desplegada en cerca de 40 países que suman 50 billones USD de PIB. [Hecho: llamada de resultados de NVIDIA]

También hay sustancia física detrás. La saudí HUMAIN confirmó un plan para desplegar hasta 600.000 GPU de NVIDIA a lo largo de 3 años y ya recibió el primer lote de 18.000 GB300. En los Emiratos, Stargate UAE está construyendo la fase 1 de 200MW de un clúster de 1GW con meta de puesta en marcha en el tercer trimestre de este año; solo esa fase 1 incorporará hasta 35.000 GB300, y el operador G42 recibió la aprobación de exportación de Estados Unidos a mediados de julio. La UE avanza en su programa de gigafábricas de IA de 20.000 millones EUR, India apunta a 100.000 GPU públicas para fin de año, y SoftBank de Japón tiene como meta la comercialización de su nube soberana de GPU en octubre. [Hecho: anuncios de cada empresa y cada país]

¿Cómo se conecta esto con la memoria? Ya hay dos vías públicas. El programa global Stargate de OpenAI firmó en octubre de 2025 con Samsung Electronics y SK Hynix una carta de intención (LOI) por <strong>hasta 900.000 obleas de DRAM al mes</strong>, un volumen equivalente a cerca del 40% de la capacidad global de DRAM. Queda claro el límite de que se trata de una carta de intención no vinculante. [Hecho: prensa, LOI] Y SK Hynix formalizó en junio de este año una asociación plurianual de HBM4 con NVIDIA que atraviesa la próxima generación Vera Rubin. [Hecho: anuncio de NVIDIA] Del lado de los fondos soberanos, ha habido informes continuos de cooperación entre el capital emiratí, como Mubadala, MGX, G42 y Khazna, y el bando de SK Hynix.

También hay un vacío que hay que dejar consignado con honestidad. En junio y julio no se confirma ninguna divulgación nueva de que una entidad soberana haya comprado DRAM directamente y en volumen a Samsung Electronics o SK Hynix. [Sin verificar: contrato directo no divulgado] La demanda de memoria soberana entra a través de OEM de servidores e integradores de sistemas, así que en las divulgaciones de clientes de las memoreras queda mezclada con la de los hyperscalers. [Inferencia: estructura de distribución] No ver algo no es lo mismo que no exista. No hay escenario en el que se confirmen 600.000 GPU sin que se les sume memoria, así que el problema no es si existe, sino la visibilidad de la divulgación en cuanto a escala y momento.

## 4. La escasez de DRAM de servidor se agrava: el argumento de Meritz y la evidencia externa

El reagravamiento de la escasez de DRAM de servidor desde mediados de julio que señaló el equipo de Meritz no es un argumento exclusivo de esa casa de bolsa. Cuatro piezas de evidencia externa apuntan en la misma dirección.

| Evidencia | Contenido | Fuente y fecha |
|---|---|---|
| Previsión de precio de contrato | Previsión de +13-18% intertrimestral en el precio de contrato de DRAM de servidor del 3T. Como no se puede subir a los CSP estadounidenses atados a contratos de largo plazo (LTA), el alza se concentra en los clientes no-LTA | TrendForce, 9/7 |
| Tasa de crecimiento de la oferta | La oferta de bits de RDIMM crece 15-20% anual, por debajo del crecimiento de envíos de CPU. Acumulación de inventario anticipado por los CSP que prevén escasez en 2027. Los módulos se mueven a la baja de 96/128GB hacia 32/64GB | TrendForce, 9/7 |
| Plazos de entrega | Los plazos de DRAM de servidor superan las 40 semanas, los precios suben cerca de +90% frente a finales de 2025, y la validez de las cotizaciones se acorta a 1-30 días | Declaraciones de Inventec, 16/7 |
| Testimonio de proveedor | Solo puede cubrir 50-66% de la demanda de sus clientes clave, el HBM está agotado hasta el cupo de 2027, y la escasez de oferta continuará más allá de 2027 | Llamada de resultados de Micron, julio |

[Hecho: cada fuente]

El nivel absoluto de los precios también está emitiendo señales anómalas. El precio fijo de contrato del DRAM de PC de uso general (DDR4 8Gb) marcó en junio un récord de 21 USD desde que se lleva el registro, y el precio spot supera al precio fijo en 72%. También circuló la noticia de que Samsung Electronics notificó a sus clientes chinos que subiría hasta 20% el precio del DRAM en el tercer trimestre. [Hecho: prensa del sector] La combinación de un precio de contrato al alza con una prima spot que supera 70% significa que, fuera del canal de contrato, existe de verdad una demanda dispuesta a pagar sobreprecio con tal de asegurar volumen urgente. Quien paga el precio caro no es el hyperscaler atado al LTA, sino lo que queda fuera de eso: el soberano, la empresa y la nube de segundo nivel. La frase de TrendForce de que el alza se concentra en los clientes no-LTA y la frase de Meritz de que la compra soberana se intensifica son dos expresiones del mismo fenómeno. [Inferencia: interpretación cruzada]

El analista Kim Sun-woo va un paso más allá. Su previsión es que el mercado está atrapado en un marco estrecho de contratos de largo plazo sacrificados y de rebaja de resultados de 2027, y que ese malentendido se disipará con rapidez a medida que se sucedan eventos como la ejecución anticipada de retorno al accionista y asociaciones que incluyan inversión de participación por parte de grandes tecnológicas. [Hecho: argumento del informe] Esto no es un hecho verificado sino una previsión de la casa de bolsa, así que el criterio de calificación es si se confirma como evento real durante la temporada de resultados de esta semana. Aun así, la dirección es coherente con los fondos de la salida a bolsa en el Nasdaq y los movimientos de asociación del presidente de SK Hynix, Chey Tae-won, que vimos en el artículo anterior, y con el contrato plurianual entre SK Hynix y NVIDIA.

## 5. Codex y sus 9 millones: empiezan a aparecer los números de la demanda final

En el debate sobre el CAPEX de IA, el punto más atacado no fue la infraestructura sino su extremo final. Que los centros de datos se están construyendo pero la evidencia de que el uso final crece en la misma medida es débil. En este eslabón débil empezaron a aparecer números llamativos.

| Momento | Número de usuarios | Nota |
|---|---|---|
| Febrero de 2026 | 1 millón | Usuarios activos exclusivos de Codex |
| 8 de abril | 3 millones | Activos semanales, con anuncio de reinicio del límite de uso cada millón adicional |
| 21 de abril | 4 millones | 1 millón más en dos semanas |
| Finales de mayo-inicios de junio | Supera los 5 millones | 6 veces el nivel de febrero |
| 9 de julio | Lanzamiento oficial de GPT-5.6 | Los tres modelos Sol, Terra y Luna; Codex se integra con el escritorio de ChatGPT |
| 12 de julio | 6 millones | Desde aquí el indicador combina Codex y ChatGPT Work |
| Alrededor del 15 de julio | 9 millones | Aumento de 3 millones en tres días |

[Hecho: declaraciones públicas de directivos de OpenAI y prensa]

Para ser justos hay que hacer dos advertencias. La cifra posterior al 9 de julio ya no es Codex en solitario sino un indicador que suma ChatGPT Work, así que la comparación estricta y continua con el tramo anterior es difícil. Y una extrapolación externa que simplemente prolonga el ritmo de crecimiento de finales de mayo calculaba que se llegaría a 10 millones en octubre, pero en la realidad ya se llegó a 9 millones a mediados de julio. Se deja constancia de que esta línea de extrapolación no es una proyección oficial de OpenAI. [Hecho: verificación de la fuente de la extrapolación] Aun teniendo en cuenta el cambio de definición del indicador, queda el hecho de que se midió en la realidad una aceleración que adelanta la línea esperada en unos tres meses, durante los tres días inmediatamente posteriores al lanzamiento de GPT-5.6.

Codex importa no por el tamaño del número sino por la naturaleza de la demanda. Es un producto que convierte horas de trabajo humano en horas de inferencia. El agente puede trabajar más tiempo sin que la persona esté conectada más tiempo, y si una sola persona corre varias tareas en paralelo, <strong>el volumen de trabajo crece más rápido que el número de usuarios</strong>. A partir de este tramo, la unidad de la demanda ya no es el usuario activo mensual sino el total de horas de ejecución de agentes. Es exactamente la misma estructura que, en el artículo anterior, reescribió el techo del modelo de demanda de memoria para IA como número de cargas de trabajo por memoria por carga de trabajo por frecuencia de ejecución.

El debate sobre eficiencia también se invierte aquí. La propia OpenAI informó que GPT-5.6 Sol mejoró la eficiencia de tokens en 54% frente a la generación anterior. Que los usuarios y el uso se dispararan justo después de la salida de un modelo cuyo costo por token baja es un caso real que confirma la hipótesis de Jevons en el terreno de los agentes de código: la mejora de eficiencia no reduce la demanda de cómputo, sino que <strong>amplía el rango de tareas que se le pueden delegar a la IA</strong>. [Inferencia: efecto Jevons] Lo que hay que mirar no es la tasa de caída del precio del token, sino el volumen de trabajo que esa caída de precio acaba de abrir.

## 6. Entonces, ¿cómo se traduce esto a la memoria?

También hace falta moderación. Un solo número, los 9 millones de Codex, no puede explicar el ciclo de memoria. Para que el número de usuarios se traduzca en demanda de bits de memoria, tiene que pasar por cuatro coeficientes de conversión: el volumen de ejecución simultánea, la longitud de contexto, la memoria instalada por acelerador, y la tasa de crecimiento de la oferta. [Inferencia: modelo de demanda] Si cualquiera de estos es débil, el indicador de titular y la demanda real se separan.

Sin embargo, si contrastamos las variables al alza que el artículo anterior de escenarios de demanda planteó como argumento del 35% de sobrecrecimiento con la evidencia de esta semana, se ve un alineamiento.

- La ampliación de la base de demanda de aceleradores obtuvo evidencia real con la inversión de la tasa de crecimiento de ACIE y la triplicación de los ingresos soberanos.
- La inferencia continua de agentes obtuvo su primer número con los 3 millones de Codex en tres días y el cambio de unidad del indicador.
- La difusión más allá del HBM ya apareció en los precios, con la previsión de +13-18% intertrimestral en el precio de contrato de DRAM de servidor, los plazos de 40 semanas y la prima spot de 72%.
- La hipótesis de que el uso vence a la eficiencia obtuvo una evidencia contraintuitiva: el uso se disparó justo después de una mejora de 54% en la eficiencia de tokens.

La implicación para el relato de alivio de oferta en 2028 también se bifurca aquí. La fórmula de la tesis de alivio, en general, toma la desaceleración del crecimiento del CAPEX de los hyperscalers como techo de la tasa de crecimiento de la demanda. Pero si la mitad de la demanda incremental empezó a venir de fuera de ese grupo, hay que recalcular el propio supuesto de techo. Es exactamente ahí donde apunta la refutación de Meritz. No cambiamos las probabilidades de inmediato. Mantenemos el esqueleto de base 45%, al alza 35% y a la baja 20%, pero dejamos consignado que el argumento al alza empezó a recibir evidencia real por tres vías. La actualización de probabilidad se hará cuando se complete el cuadro de verificación de abajo. [Inferencia: gestión de escenarios]

## 7. Revisión de contraargumentos

Cuanto más sólido parece un argumento, más vale plantar enfrente su contraparte.

- <strong>La calidad de la demanda no-hyperscale.</strong> ACIE incluye a las neocloud. Los pedidos de nubes de segundo nivel con costo de capital frágil son la demanda que primero se cancela cuando se aprietan las tasas de interés y las condiciones de financiamiento. Que se invierta la tasa de crecimiento no garantiza la durabilidad de la demanda.
- <strong>La volatilidad política de lo soberano.</strong> Los proyectos nacionales se tambalean con elecciones, presupuestos y controles de exportación. La convocatoria de las gigafábricas de la UE ya se pospuso dos veces, y el volumen de Oriente Medio depende de un solo interruptor: la aprobación de exportación de Estados Unidos.
- <strong>La trampa del indicador.</strong> Los 9 millones de Codex son un número justo después del cambio de definición hacia el indicador combinado, y ni siquiera se divulgó el criterio de qué cuenta como activo. La dirección del crecimiento es evidencia real, pero la magnitud todavía no está separada del marketing.
- <strong>La autodestrucción del alza de precios.</strong> El reagravamiento del DRAM de servidor es un argumento alcista, pero a la vez, como se vio en el caso de IBM, es un riesgo que erosiona el presupuesto de TI y crea un vacío de demanda después de la compra anticipada. El propio presidente Chey advirtió sobre la destrucción de demanda por precios excesivos.
- <strong>La distinción entre previsión y evidencia real.</strong> Las previsiones de eventos de Meritz (ejecución anticipada de retorno al accionista, asociaciones de participación con grandes tecnológicas) siguen siendo previsiones. Si no se cumplen, la mirada estrecha habrá tenido razón.

## 8. Cuadro de verificación: qué va a confirmar la respuesta

- Si en las llamadas de resultados de Samsung Electronics y SK Hynix de alrededor del 30 de julio, el alza del precio de contrato del 3T confirma el rango de +13-18% de TrendForce, y si aparecen menciones a los clientes no-LTA y al volumen soberano.
- Si la ejecución anticipada de retorno al accionista y las asociaciones de tipo inversión de participación de SK Hynix se materializan en divulgaciones reales. Es el ítem de calificación directa de la previsión de Meritz.
- Si en la divulgación del FY27 T2 de NVIDIA de finales de agosto, ACIE supera a hyperscale por primera vez. Si lo hace, la ampliación de la base de demanda deja de ser relato y se convierte en cifra divulgada.
- Si un contrato directo de memoria de origen soberano, o un pedido grande a través de un OEM de servidores, llega a nivel de divulgación. El primer candidato es si la carta de intención de Stargate se convierte en contrato vinculante.
- Si los indicadores de uso de Codex y de los agentes competidores empiezan a divulgarse en función de horas de ejecución, junto con la superación de los 10 millones.

El criterio decisivo no cambia. Si el precio de contrato del DRAM se quiebra, el mercado desestimará todo este relato de demanda; si se sostiene, se volverá a dibujar la curva de demanda que se había trazado con demasiada modestia.

---

Las acciones mencionadas en el texto son ejemplos para el análisis y no constituyen una recomendación de compra o venta de ningún valor en particular. La decisión de inversión y la responsabilidad por sus resultados recaen en cada inversor. El informe de Meritz Securities se cita reconstruyendo su idea central, y la responsabilidad por las cifras detalladas y las previsiones del texto original corresponde a esa casa de bolsa. El número de usuarios de Codex cambió de definición después del 9 de julio hacia un indicador combinado con ChatGPT Work, lo que dificulta una comparación estricta con el tramo anterior, y la línea de extrapolación que calcula 10 millones en octubre no es una proyección oficial de OpenAI. La compra directa de memoria por parte de entidades soberanas no se ha confirmado mediante divulgación, y el volumen relacionado con Stargate sigue en la etapa de carta de intención no vinculante. Los datos de precios de acciones, índices y mercancías corresponden a información pública hasta el 17 de julio de 2026 y no reflejan variaciones posteriores.

### Publicaciones relacionadas

- [¿Superará la demanda de memoria para IA las expectativas? Las probabilidades de sobrecrecimiento según los escenarios de demanda y el mapa de oferta](/es/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/)
- [Dos meses de declaraciones del presidente de SK Hynix, Chey Tae-won: la empresa se fortalece, el pico de margen queda atrás](/es/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/)
- [El verdadero debate en semiconductores: cuatro relojes físicos y un reloj bursátil](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [¿Son cíclicos los semiconductores y cuál es el valor razonable? Valorando Samsung, SK Hynix y Micron con FCFE y beneficios normalizados](/es/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
