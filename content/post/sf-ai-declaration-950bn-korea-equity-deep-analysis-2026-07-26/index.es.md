---
title: "Diseccionando 950.000 millones de dólares: tres cosas que cambió la Declaración de IA de San Francisco y una que no"
slug: "sf-ai-declaration-950bn-korea-equity-deep-analysis-2026-07-26"
date: 2026-07-26T21:00:00+09:00
description: "Descomponemos la Declaración de IA de San Francisco y los 950.000 millones de dólares de cooperación Corea-EE.UU. en contratos frente a intenciones, y calculamos qué está ya en el precio de las acciones coreanas y qué es realmente nuevo. Cerca del 20-25% de cada dólar de capex en IA acaba en Corea, y casi todo es memoria. El peso real de esta semana está en fijar esa cuota hasta 2030, en que Samsung Foundry logre a Broadcom como cliente ancla, y en que Corea entre en el circuito de financiación circular de NVIDIA. Que ninguno de los cuatro pilares de la declaración reclame la capa de modelos es lo que limita el múltiplo."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["Declaración de IA de San Francisco", "Samsung Electronics", "SK Hynix", "Naver", "Broadcom", "NVIDIA", "Samsung Foundry", "HBM", "IA soberana", "Semiconductores coreanos", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스", "네이버"]
draft: false
---

> Contexto
> Hace tres días, en [El petróleo es el gatillo, los tipos son el arma](/es/post/oil-war-premium-rates-ai-multiple-korea-memory-2026-07-23/), señalamos que un Brent a 100 USD sería el punto de inflexión que forzaría un giro duro de la Reserva Federal, y escribimos que en el escenario de escalada ni siquiera un múltiplo bajo funciona como escudo. En 24 horas ese nivel se hizo realidad. El viernes 24 de julio, con el recrudecimiento de las tensiones en Medio Oriente, el Brent superó los 100 USD y el KOSPI cerró con un desplome de 5,72%, en 6.690,62 puntos, mientras Samsung Electronics cayó 7,59% y SK Hynix, 8,34%. Y esa misma noche, ya cerrado el mercado coreano, se anunció en San Francisco una cooperación entre Corea y Estados Unidos en IA por 950.000 millones de USD. Este artículo calcula qué cambió realmente en el punto donde se cruzaron esos dos hechos.

## TL;DR

- Primero hay que corregir los hechos. La Declaración de IA de San Francisco no es una declaración del gobierno estadounidense ni de la industria, sino <strong>una declaración del gobierno de Corea presentada por el presidente Lee Jae-myung</strong>. La cumbre también la organizó el gobierno coreano, y en la lista de asistentes confirmados no figura ningún funcionario del gobierno federal de EE.UU., del estado de California ni de la ciudad de San Francisco. Es un acto en el que Corea declaró su propia posición en pleno Silicon Valley, no un acuerdo entre dos países.
- Los 950.000 millones de USD no son un dato para analizar, sino una cifra para desarmar. Es la suma de 750.000 millones de USD del Grupo SK y 200.000 millones de USD de Samsung Electronics-Broadcom: el primero es una carta de intención (LOI), y sobre el segundo, Reuters y Fortune precisaron que se trata de <strong>una manifestación de intención, no de un contrato vinculante</strong>. El jefe de la Oficina de Política del despacho presidencial también lo describió como "de naturaleza de MOU y esquema de cooperación".
- Un contraste para dimensionar la cifra. La proyección del mercado global de memoria para 2026 es de 889.300 millones de USD. El monto total de cooperación anunciado esta vez <strong>supera un año entero del mercado global de memoria</strong>. Eso significa que es un monto nominal acumulado a varios años, y lo único que importa en el análisis es la conversión anual y la tasa de conversión real.
- Así se calcula el valor real. La HBM representa entre 35% y 55% del costo de fabricación de un acelerador, y Corea concentra cerca de 79% de las ventas globales de HBM y cerca de 67% de las de DRAM. La memoria representa cerca de 30% del capex de los hiperescaladores en 2026. Al multiplicar, <strong>de cada dólar de capex en IA, Corea se queda con aproximadamente 20-25%, y casi todo es memoria</strong>. La lógica de la GPU, el empaquetado CoWoS, la electricidad y el terreno, el networking y la construcción apenas le dejan algo a Corea.
- Lo que realmente cambió esta semana son tres cosas. Que ese 20-25% quedó fijado contractualmente hasta 2030; que <strong>Samsung Foundry consiguió en Broadcom un segundo cliente ancla</strong>; y que Corea se incorporó a una estructura de financiación circular en la que NVIDIA invierte en Naver y Naver usa ese dinero para comprarle a NVIDIA. Lo segundo es lo que el mercado menos ha incorporado en el precio.
- Hay una cosa que no cambió. En ninguno de los cuatro pilares de la declaración aparece la capa de modelos y plataformas. HyperCLOVA X, de Naver, quedó descalificado en enero de este año en la primera evaluación gubernamental por usar pesos de Qwen de Alibaba, y ahora se reconstruye sobre Nemotron, el modelo abierto de NVIDIA. <strong>Haber pasado de pesos abiertos chinos a pesos abiertos estadounidenses es, en la práctica, lo que significa la IA soberana de Corea</strong>.
- El momento en que ocurrió esto es peculiar. La cumbre fue el viernes hora local, de madrugada del sábado en hora de Corea. <strong>La bolsa coreana todavía no ha incorporado esta noticia ni una sola vez en el precio</strong>. El primer reflejo llega el lunes 27 de julio, y el mercado se encuentra con esta noticia justo después del desplome de 5,72% provocado por el petróleo, desde un nivel ya deprimido.

<div class="thesis-callout">
<div class="thesis-callout__label">Marco clave</div>

Esta semana Corea declaró oficialmente que quiere convertirse en el armero de la era de la IA. Los cuatro pilares de la declaración son hub de la cadena de suministro, país líder en el uso de la IA, red de cooperación y política social interna. En ninguno se menciona construir modelos. Esto no es una derrota, es un cálculo. Capturar de forma estable el 20-25% del capex de IA a través de la memoria, la foundry y los equipos eléctricos es algo que la mayoría de los países no puede hacer. Pero la ganancia de un armero sigue la escala de la guerra, no su desenlace. Por eso este anuncio amplió la visibilidad de ingresos de las empresas coreanas hasta 2030, pero dejó intacto el techo del múltiplo.

</div>

## 1. Qué ocurrió: primero, la verdadera naturaleza de la declaración

En la prensa y las redes sociales coreanas, este evento a menudo se consume como si fuera una declaración conjunta entre Corea y Estados Unidos. La estructura real es otra.

[Hecho: Reuters y Korea Policy Briefing] El presidente Lee Jae-myung presentó la Declaración de IA de San Francisco el 24 de julio, hora local, en The Midway, en el barrio de Dogpatch de San Francisco. La cumbre fue organizada por el gobierno de Corea, y la lista de asistentes que recopiló Reuters no incluye a ningún funcionario del gobierno federal de EE.UU., del estado de California ni de la ciudad de San Francisco. [Sin verificar: participación del gobierno de EE.UU.] No se agotaron todas las fuentes posibles para confirmarlo, pero en ninguna de las coberturas disponibles aparece la participación del gobierno estadounidense.

Los cuatro pilares de la declaración son estos. Primero, convertirse en un país clave de la cadena de suministro global como base de producción confiable de semiconductores de IA y socio de esa cadena. Segundo, ser el país que usa la IA de forma más rápida y eficaz, es decir, convertirse en el banco de pruebas global de la IA. Tercero, construir una red de cooperación horizontal que incluya a los países en desarrollo. Cuarto, construir, con base en la Ley Marco de IA que entró en vigor en enero de este año, una sociedad de base de IA centrada en el ser humano. [Hecho: Korea Policy Briefing]

La composición de los asistentes resume la naturaleza del evento. Por el lado coreano asistieron el presidente de Samsung Electronics, Lee Jae-yong; el presidente de SK, Chey Tae-won; el presidente de Hyundai Motor Group, Chung Eui-sun; y el fundador y presidente del consejo de Naver, Lee Hae-jin. Por el lado estadounidense asistieron Jensen Huang, de NVIDIA; Sam Altman, de OpenAI; Dario Amodei, de Anthropic; y Hock Tan, de Broadcom, mientras que Microsoft envió en su lugar al responsable de hardware de Azure. [Hecho: comunicados de las empresas y prensa] Es decir, fue un encuentro entre capitalistas coreanos y vendedores de tecnología estadounidenses, sin reguladores ni tomadores de decisiones de política presentes. Esta composición también determinó la naturaleza del resultado. Lo que salió de ahí no fueron tratados, sino intenciones de compra y compromisos de suministro.

## 2. Desarmando los 950.000 millones de USD: qué es contrato y qué es intención

Desglosamos uno por uno los acuerdos de cooperación anunciados.

| Parte coreana | Contraparte | Contenido | Monto | Naturaleza |
|---|---|---|---|---|
| Samsung Electronics | Broadcom | Suministro de HBM4 y HBM4E, foundry de 2nm o menos, empaquetado avanzado | Más de 200.000 millones USD, hasta 2030 | MOU estratégico |
| SK Telecom y SK Hynix | NVIDIA | Fábrica de IA de 2GW, asignación prioritaria de Vera Rubin, desarrollo conjunto de HBM de próxima generación | Más de 500.000 millones USD | Carta de intención (LOI) |
| SK Hynix | Microsoft | Suministro de memoria de servidor a largo plazo | No revelado | Carta de intención |
| SK Telecom y SK Hynix | Anthropic | Cooperación en centro de datos de IA de 5GW, hasta 2029 | No revelado | MOU |
| Naver | NVIDIA | Inversión estratégica de capital, cooperación en GPU y tecnología | 1.000 millones USD | Contrato de inversión |
| Naver | Brookfield | Financiación de infraestructura para la fábrica de IA de Sejong | Hasta 9.000 millones USD | Acuerdo de condiciones no vinculante |
| Samsung SDS | Anthropic | IA empresarial basada en Claude, formación de talento | No revelado | MOU |
| Hyundai Motor Group | NVIDIA | Plataforma de referencia robótica, 50.000 GPU Blackwell | No revelado | Alianza |
| Servicio Nacional de Pensiones | 6 fondos de VC de Silicon Valley | Cooperación en inversión | No revelado | MOU |

[Hecho: síntesis de anuncios corporativos, presentaciones regulatorias y prensa]

Aquí hay varios puntos que llaman la atención.

Primero, en la práctica el único contrato vinculante es la inversión de capital de NVIDIA en Naver. El resto son cartas de intención, MOU y acuerdos de condiciones no vinculantes. Fortune y Reuters escribieron explícitamente que el acuerdo Samsung-Broadcom es una manifestación de intención y no un contrato vinculante, y Kim Yong-beom, jefe de la Oficina de Política del despacho presidencial, también lo describió como "de naturaleza de MOU y esquema de cooperación". [Hecho: prensa y briefing] Esto no es un defecto, sino la forma normal que toman los acuerdos en esta etapa. Aun así, hay que reflejar en el precio que se trata de un nivel de documento distinto del reconocimiento de ingresos.

Segundo, la definición del monto varía según la fuente. La sala de prensa oficial de SK Hynix, CNBC y NVIDIA registran los más de 500.000 millones USD como la cifra exclusiva del acuerdo con NVIDIA, mientras que la mayoría de la prensa coreana reportó 750.000 millones USD sumando también Microsoft y Anthropic. [Hecho: diferencias de cifras según la fuente] Si al citar la cifra no se aclara la definición, se termina contando dos veces lo mismo.

Tercero, hay que dimensionar la magnitud. La proyección de TrendForce para el mercado global de memoria en 2026 es de 889.300 millones USD. El monto total de cooperación anunciado esta vez, 950.000 millones USD, supera un año entero del mercado global de memoria. [Inferencia: contraste de magnitud] Esto no significa que la cifra esté mal, sino que es un monto nominal acumulado a varios años. Si el acuerdo Samsung-Broadcom se reparte en 5 años, equivale a 40.000 millones USD anuales, una cifra significativa frente a los ingresos anuales de la división de semiconductores de Samsung Electronics, pero no una magnitud que redefina a la empresa. El acuerdo de SK tiene una naturaleza similar: es un monto de proyecto total que mezcla el costo de construcción del centro de datos, la compra de GPU y el suministro de memoria.

El valor real del análisis no está en el monto total, sino en la conversión anual y la tasa de conversión real. Y esta semana es la primera ventana para observar esa tasa de conversión.

## 3. Lo que ya está en el precio: de cada dólar de capex en IA, Corea se queda con 20-25%

Al calcular cuánto se queda Corea realmente del capex de IA, se ve con claridad qué añade este anuncio.

La participación de la HBM en el costo de fabricación de un acelerador varía por producto: cerca de 41% en el H100, 35% en el H200, 45% en el B200 y 43% en el superchip GB200. [Hecho: informe de análisis de semiconductores, cifra direccional de una sola fuente] Y, con corte al primer trimestre de 2026, Corea concentra cerca de 79% de las ventas globales de HBM (SK Hynix 58%, Samsung Electronics 21%), cerca de 67% de las de DRAM (Samsung 38,5%, SK 28,8%) y cerca de 47% de las de NAND. [Hecho: Counterpoint y TrendForce]

A esto se suma la participación de la memoria en el capex de los hiperescaladores. SemiAnalysis la estima en cerca de 30% para 2026, un salto frente al cerca de 8% de 2023-2024. Morgan Stanley proyecta que la participación de la memoria sobre el capex de la nube pasará de 12% en 2023 a 40% en 2027. [Hecho: estimaciones de cada firma]

Al multiplicar, aparece la respuesta. <strong>De cada dólar de capex en IA, la memoria coreana se queda con aproximadamente 20-25%</strong>. [Inferencia: cálculo propio] Este es el esqueleto cuantitativo de la tesis de inversión en semiconductores coreanos, y al mismo tiempo es su techo. ¿A dónde va el 75-80% restante? A la lógica de la GPU que diseña NVIDIA y fabrica TSMC, al empaquetado avanzado CoWoS que TSMC controla casi en monopolio, y a la electricidad, el terreno, el networking, la construcción y la mano de obra. De todo esto, a Corea le corresponde solo una parte de las exportaciones de equipos eléctricos y una porción todavía incipiente del empaquetado avanzado.

Esa participación ya está dentro de los resultados. El resultado preliminar de Samsung Electronics del segundo trimestre de 2026 fue de 171 billones KRW en ingresos y 89,4 billones KRW en beneficio operativo, con la división de semiconductores en 89,6 billones KRW (DRAM 71 billones, NAND 21,3 billones). Se espera que SK Hynix registre 84,1 billones KRW en ingresos y 64,1 billones KRW en beneficio operativo, con un margen operativo cercano a 76%. La suma del beneficio operativo trimestral de ambas empresas supera los 150 billones KRW. [Hecho: resultados preliminares y consenso] Las exportaciones de semiconductores de Corea en el primer semestre alcanzaron 192.400 millones USD, un alza de 162,6% interanual que ya superó el récord de todo el año pasado.

Es decir, lo que este anuncio generó de nuevo no es el volumen en sí. El volumen ya está en el estado de resultados. Lo que generó de nuevo es que <strong>extendió documentalmente la duración de ese volumen hasta 2030</strong>. En la distinción, repetida en artículos anteriores, entre volumen y duración del margen, esta semana añadió peso al lado de la duración.

## 4. Lo nuevo, uno: Samsung Foundry consiguió un cliente ancla

Aquí está el punto que el mercado menos ha incorporado en el precio. Leer el acuerdo con Broadcom solo como un contrato de suministro de memoria deja fuera la mitad de la historia.

El segundo trimestre de 2026 de Samsung Electronics fue el mejor de su historia, pero dentro de ese resultado, las divisiones de System LSI y Foundry registraron una pérdida operativa trimestral de cerca de 2,8 billones KRW. Aun así, junio fue el primer mes con ganancias desde 2023. [Hecho: resultados preliminares y estimaciones de casas de bolsa] La cuota global de Foundry, con corte al primer trimestre de 2026, es de 6,5%, once veces menor que el 72,3% de TSMC. El rendimiento (yield) en 2nm se reporta en un rango de 50-60%, con una meta interna de 70% para fin de año. Las cifras varían según el medio, entre 55% y más de 60%. [Hecho: TrendForce y otros, cifras en disputa]

En este contexto, la llegada de Broadcom significa lo siguiente. Broadcom es el líder en el diseño de chips de IA a medida, incluidos el TPU de Google y el MTIA de Meta. El chip propio de OpenAI también se diseña junto con Broadcom. Y esa misma Broadcom dijo que le confiará a Samsung, hasta 2030, un paquete conjunto de memoria, foundry de 2nm o menos y empaquetado avanzado. Samsung ya empezó a producir el Tesla AI5 en 2nm en la planta de Taylor, que además elevará toda su línea a 2nm y duplicará su capacidad inicial hasta 50.000 obleas al mes. [Hecho: empresas y prensa]

<strong>Samsung Foundry consiguió esta semana un segundo cliente ancla.</strong> El primero fue Tesla (16.500 millones USD, hasta 2033), y el segundo es Broadcom. Para una foundry, un cliente ancla es a la vez el volumen que hace girar la curva de aprendizaje del rendimiento y la referencia que convence a otros clientes. El orden importa porque Qualcomm está evaluando ahora mismo el proceso de 2nm de Samsung para parte de su volumen de Snapdragon de 2027.

¿Por qué es tan relevante desde la óptica de la valoración? Ahora mismo, Foundry está reflejada en el precio de la acción de Samsung Electronics prácticamente como un valor negativo, porque es una división que pierde 2,8 billones KRW por trimestre. Si el volumen de Broadcom se convierte en obleas realmente procesadas y el rendimiento llega a 70%, esta división cambia de signo: de destruir valor a crearlo. El boom de la memoria ya está en el precio, pero el giro a ganancias de Foundry no lo está. [Inferencia: valoración del segmento] Aun así, el momento de ese giro a ganancias también se discute puertas adentro. Algunas coberturas hablan de una meta para el cuarto trimestre, el jefe de la división de Foundry dijo que unas ganancias dentro de 2026 son difíciles y que 2028 es más realista, y hay quienes apuntan a 2027. [Hecho: cifras varían según el medio]

Si se juntan las coberturas que dicen que TSMC está prácticamente agotada hasta el año 2028 con el hecho de que el lead time de 3nm supera el año, lo más probable es que el volumen de Broadcom no se le haya quitado a TSMC, sino que sea demanda excedente que TSMC no puede absorber. [Inferencia: estructura de oferta y demanda] TSMC anunció esa misma semana una inversión adicional de 100.000 millones USD en Arizona. Esto significa que ambas empresas están en fase de expansión, una señal negativa para el debate sobre la disciplina de oferta de 2028.

## 5. Lo nuevo, dos: la financiación circular llegó a Corea

En el caso de Naver, importa más la estructura que el monto.

NVIDIA invierte 1.000 millones USD en Naver. Brookfield aporta hasta 9.000 millones USD en financiación de infraestructura mediante un acuerdo de condiciones no vinculante. Con ese capital, Naver ampliará el centro de datos de Sejong de 55MW a 200MW para 2028 y comprará cerca de 100.000 GPU de NVIDIA. [Hecho: sala de prensa de NVIDIA y comunicados de las empresas]

Esta estructura, en una frase, es así: NVIDIA le pone el capital al cliente, y el cliente usa ese capital para comprar productos de NVIDIA. Es exactamente la estructura que ha sido blanco de la crítica sobre financiación circular en torno a OpenAI y CoreWeave durante el último año. Esta semana Corea se convirtió en participante de esa estructura. Es decir, importó a la vez el lado alcista y el bajista.

El lado alcista es claro. Hasta antes de este anuncio, Naver era la gran acción más rezagada del rally de IA. Su precio, en 185.900 KRW al 20 de julio, estaba 28% por debajo de los cerca de 250.000 KRW de un mes antes, y muy lejos de su máximo histórico de 450.000 KRW. Las razones eran el riesgo sindical y la lenta monetización de la IA. Esa misma empresa consiguió de un día para otro una vía de financiación de infraestructura por 10.000 millones USD y un socio de capital como NVIDIA. Es material suficiente para que su estatus pase de acción rezagada a poseedor de infraestructura. [Inferencia: cambio de estatus]

El lado bajista también es claro. Primero, los 9.000 millones USD de Brookfield no son vinculantes. Segundo, la carga de capital que implican 200MW y 100.000 GPU no es en absoluto liviana para el tamaño de Naver. Tercero, el momento. El ratio de cobertura de demanda de los bonos de los hiperescaladores bajó de cerca de 5x en febrero de este año a menos de 2x en julio, y se proyecta que la emisión de bonos ligados a la IA en 2026 llegue a 570.000 millones USD, de los cuales ya se habían colocado 236.000 millones USD hacia fines de mayo, cerca de cuatro veces más que en el mismo período del año pasado. [Hecho: estimaciones de Morgan Stanley y prensa] El momento en que Corea entra al mercado de financiación de infraestructura coincide con el momento en que ese mercado se está ajustando. El tipo real de 2,95% y la subida de la prima por plazo que tratamos en el artículo de hace tres días son, precisamente, el precio de este capital.

Esa misma semana hubo una escena que contrasta. Anthropic anunció, en un evento de AMD el 22-23 de julio, el despliegue de hasta 2GW de AMD MI455X, una cobertura frente a su dependencia de NVIDIA. [Hecho: anuncio de AMD] En cambio, los anuncios de Corea esta semana, tanto de SK como de Naver y Hyundai, convergieron todos en una única hoja de ruta de NVIDIA. En términos de estabilidad de abastecimiento, se aseguraron una asignación prioritaria, pero en términos de dependencia de proveedor, es una apuesta sin cobertura.

## 6. Lo que no cambió: la ausencia de la capa de modelos

Volvamos a los cuatro pilares de la declaración: hub de la cadena de suministro, país líder en el uso de la IA, red de cooperación y sociedad de base de IA. Al desglosarlos uno por uno, son, respectivamente, proveedor de componentes, consumidor, distribuidor y regulación interna. <strong>En ninguno de ellos hay un pilar que hable de construir modelos o plataformas.</strong>

La prueba de que esto no es un problema retórico sino sustantivo está dentro del propio anuncio de esta semana. HyperCLOVA X, de Naver, se perfeccionará sobre Nemotron, el modelo abierto de NVIDIA. Pero HyperCLOVA X quedó descalificado en enero de este año en la primera evaluación gubernamental de modelos nacionales de IA, porque montó su codificador de visión multimodal sobre los pesos de Qwen 2.5, de la china Alibaba, y el gobierno determinó que reutilizar pesos externos no podía reconocerse como un modelo propio. [Hecho: prensa nacional, enero de 2026] Es decir, el modelo insignia de la IA soberana de Corea trasladó su base de pesos abiertos chinos a pesos abiertos estadounidenses.

La brecha de desempeño también queda registrada en números. En el índice de inteligencia de Artificial Analysis, EXAONE 4.0 32B, del LG AI Research, obtiene 43 puntos, el puesto 7 a nivel mundial, el más alto entre los modelos coreanos, frente a los 73 puntos de Gemini 3 Pro, de Google, y GPT-5.0, de OpenAI. [Hecho: benchmark] Es una brecha de poco más de 40%.

Los indicadores del ecosistema son todavía más fríos. Corea es el país número 1 del mundo en registro de patentes de IA por cada 100.000 habitantes. Y aun así, el número de unicornios cayó de 10 en 2022 a 0 en 2023, y a solo 1 tanto en 2024 como en 2025. Corea tiene la cuarta peor fuga neta de talento en IA entre los 38 países de la OCDE, y la Universidad Nacional de Seúl no logró cubrir el 75% de las plazas de sus programas de posgrado en ciencia e ingeniería del año académico 2025. [Hecho: estadísticas diversas] Es una estructura con la densidad de ingeniería más alta del mundo, pero con la capacidad de crear empresas y de retener talento completamente rota.

El MOU que firmó el Servicio Nacional de Pensiones con seis fondos de capital de riesgo de Silicon Valley hay que leerlo en este contexto. El propósito declarado fue "formar al próximo Samsung o SK". Significa que, como el ecosistema local no logra producir al próximo campeón, esa búsqueda se subcontrata a Sand Hill Road. Es una decisión razonable, pero al mismo tiempo es un diagnóstico. [Inferencia: interpretación de política]

Así que la conclusión queda así. Corea fijó documentalmente, hasta 2030, su estatus de proveedor de componentes que se queda con 20-25% del capex de IA. Es un activo formidable que la mayoría de los países no tiene. Pero la ganancia de un proveedor de componentes sigue el ciclo, mientras que la ganancia del dueño de la plataforma crea valor terminal. En el artículo anterior sobre el [valor razonable de los semiconductores](/es/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/) escribimos que los múltiplos de 3,9x para Samsung Electronics y 4,3x para SK Hynix sobre el consenso de 2028 son un precio que duda de la duración de las ganancias, no de su desaparición. El anuncio de esta semana amplió la evidencia a favor de esa duración, pero no cambió la naturaleza misma del múltiplo.

## 7. El momento: el mercado todavía no incorporó esta noticia

Al revisar el calendario bursátil aparece un punto peculiar.

La cumbre fue el viernes 24 de julio, hora de San Francisco, es decir, de madrugada del sábado 25 de julio en hora de Corea. La última sesión bursátil coreana fue el viernes 24 de julio, y ese cierre ocurrió antes de la noticia. <strong>Es decir, el KOSPI nunca ha incorporado en el precio el anuncio de los 950.000 millones de USD, y el primer reflejo será el lunes 27 de julio.</strong>

La imagen de esa última sesión importa.

| Indicador | 23 jul (jue) | 24 jul (vie) | Variación |
|---|---|---|---|
| KOSPI | 7.096,89 (+4,40%) | 6.690,62 (-5,72%) | Recupera el nivel de 7.000 tras cinco sesiones y lo pierde un día después |
| KOSDAQ | 790,28 (+5,22%) | 748,22 (-5,32%) | Desplome conjunto |
| Samsung Electronics | ~270.000 KRW (+3,65%) | 249.500 KRW (-7,59%) | Devuelve la mayor parte de la subida de tres días |
| SK Hynix | ~1.918.000 KRW (+4,86%) | 1.759.000 KRW (-8,34%) | Cae por debajo de 1,8 millones de KRW |
| USD/KRW | 1.466,80 | 1.466,6 | El tipo de cambio se mantuvo estable pese al desplome bursátil |

[Hecho: bolsa y cierre de mercado según prensa]

El desplome del viernes se debió al Brent superando los 100 USD por el recrudecimiento de las tensiones en Medio Oriente, al debate sobre el flujo de caja frente al capex de IA tras los resultados de las grandes tecnológicas, y a la debilidad de las tecnológicas estadounidenses el jueves. Los extranjeros vendieron en neto 3,283 billones KRW en el KOSPI, con 1,7568 billones KRW en SK Hynix y 873.000 millones KRW en Samsung Electronics. Las dos acciones que hasta el día anterior lideraban la compra neta pasaron a liderar la venta neta. [Hecho: datos de flujos] Sin embargo, en términos semanales los extranjeros fueron compradores netos por 2,0695 billones KRW, lo que deja abierta la posibilidad de que el viernes haya sido más una reversión brusca que un cambio de dirección.

Por eso, la pregunta del lunes no es si continúa el rally, sino <strong>si el anuncio del mayor acuerdo de suministro de la historia puede revertir el desplome de 5,72% provocado por el petróleo</strong>. Estas dos fuerzas actúan sobre variables distintas. El petróleo y los tipos afectan la tasa de descuento; los contratos afectan el tamaño y la duración de las ganancias. El principio que planteamos en el artículo de hace tres días se pone a prueba exactamente esta semana. Vender memoria por los tipos es confundir variables, pero el Brent superando los 100 USD es el umbral del escenario C de ese artículo, el tramo en el que ni siquiera un múltiplo bajo sirve de escudo. Como ambas proposiciones se cumplen a la vez, es difícil determinar la dirección con certeza, y por eso hace falta el cuadro de lectura de más abajo.

## 8. Un mapa por capas desde la óptica de las acciones coreanas

Dividimos este anuncio en tres capas desde la óptica de los valores individuales.

<strong>Capa 1, lo que ya está en buena parte en el precio.</strong> El volumen de HBM y DRAM de Samsung Electronics y SK Hynix. La prueba es la suma de 150 billones KRW de beneficio operativo del segundo trimestre. Lo que este anuncio añade no es volumen, sino visibilidad hasta 2030, lo cual sostiene el piso del múltiplo, pero es distinto de una revisión inmediata al alza de las estimaciones de ganancias.

<strong>Capa 2, lo nuevo y todavía poco incorporado en el precio.</strong> Son tres ramas. Primero, que Samsung Foundry consiguió a Broadcom como cliente ancla: la posibilidad de que una división que pierde 2,8 billones KRW por trimestre cambie de signo, algo que no está en el precio actual. Segundo, la transición de Naver a poseedor de infraestructura: consiguió una vía de financiación de 10.000 millones USD y un socio de capital como NVIDIA, mientras su acción sigue en zona de rezago. Tercero, la materialización de la construcción de centros de datos de IA en Corea. Si los 2GW de SK Telecom y los 200MW de Naver realmente inician obra, los pedidos bajarán hacia los fabricantes de equipos eléctricos, transformadores, refrigeración, construcción y sustratos. Las tres grandes empresas coreanas de equipos eléctricos ya superaron, solo en el primer trimestre, 7 billones KRW en nuevos pedidos y 32 billones KRW en cartera de pedidos, y las exportaciones de transformadores de ultra alta tensión hacia Estados Unidos alcanzaron un récord histórico de 1.300 millones USD en 2025. [Hecho: estadísticas de exportación y pedidos]

<strong>Capa 3, lo que estructuralmente no se consiguió.</strong> La capa de modelos y plataformas. Esta ausencia define el techo del múltiplo, y esta declaración avaló esa ausencia como política de Estado.

Hay un contraste que vigilar en el movimiento de esta semana. En rentabilidad sectorial semanal, semiconductores fue el peor con -9,5% y telecomunicaciones el mejor con +6,1%. Isu Petasys, clasificada durante mucho tiempo como beneficiaria de la IA, cayó 46% en tres meses. [Hecho: datos de mercado] Es una prueba de que la etiqueta de "beneficiario" no se traduce automáticamente en desempeño. Hay que verificar por separado si los pedidos realmente bajan, y en qué empresa y en qué momento aparecen en el estado de resultados.

## 9. Revisión de contraargumentos

Cuanto más fuerte es el catalizador, más hace falta plantear la contraparte.

<strong>La electricidad es la restricción más real.</strong> Los 2GW que anunció SK Telecom superan los 1,5GW que se proyecta que alcanzará toda la demanda eléctrica de centros de datos de Corea dentro de 3 años. La capacidad de centros de datos que solicitó conexión a la red hasta 2029 ronda los 49GW, equivalente a 35 reactores nucleares de 1,4GW, y el 86,3% de esas solicitudes se concentra en el área metropolitana de Seúl. Las líneas de transmisión de 345kV tardan cerca de 9 años en construirse, y más de la mitad de los proyectos planeados está retrasada por la oposición de los residentes. [Hecho: estadísticas de la red eléctrica y prensa] Sin embargo, el sitio de SK está en la región de Yeongnam y el de Naver en Sejong, ubicaciones distintas de la concentración en el área metropolitana de Seúl, por lo que esta crítica se aplica en menor medida a estos dos proyectos en concreto. [Sin verificar: no se confirmó cobertura directa sobre la viabilidad de red de estos dos proyectos]

<strong>Todavía nadie sabe cuál será la tasa de conversión de las cartas de intención.</strong> No se identificó, entre la prensa coreana, un análisis que haya verificado de frente si los 950.000 millones de USD se convertirán realmente en pedidos vinculantes. Hubo disputas políticas, pero no abordaron la tasa de conversión. [Sin verificar: no existe análisis de la tasa de conversión] De hecho, el que el despacho presidencial haya tenido que aclarar en repetidas ocasiones que no se trata de una exageración es, en sí mismo, evidencia indirecta del escepticismo del mercado.

<strong>La dependencia exclusiva de NVIDIA se profundizó.</strong> El beneficio de la asignación prioritaria y el riesgo de quedar atado a su hoja de ruta están en el mismo contrato. Contrasta con que Anthropic, esa misma semana, cubrió 2GW con AMD.

<strong>Es negativo para la disciplina de oferta.</strong> Samsung le dedica a Broadcom 2nm, empaquetado y HBM; SK construye 2GW; TSMC mete 100.000 millones USD adicionales en Arizona. Todo apunta a expansión de capacidad. En artículos anteriores escribimos que el riesgo de 2028 no es la desaparición de la demanda, sino la normalización del ASP y del margen, y el anuncio de esta semana no reduce ese riesgo, sino que más bien lo amplifica. La visibilidad del volumen y la duración del margen son variables distintas.

<strong>La ventana de financiación se está estrechando.</strong> Un ratio de cobertura por debajo de 2x, una emisión anual de bonos de IA de 570.000 millones USD, un tipo real de 2,95%. Que los 9.000 millones USD de Brookfield sean no vinculantes pesa más en este entorno de lo que pesaría en tiempos normales.

<strong>La macro se movió en la dirección adversa.</strong> El Brent superando los 100 USD eleva la probabilidad de una subida en septiembre y presiona el múltiplo a la baja. Los contratos aumentan las ganancias, pero la tasa de descuento recorta el valor presente de esas ganancias.

## 10. Cuadro de lectura: las próximas dos semanas mostrarán la tasa de conversión

- <strong>Apertura del lunes 27 de julio.</strong> Es el primer reflejo. Lo que hay que observar no es la dirección del índice, sino su distribución. Si Samsung Electronics y SK Hynix suben juntas, o si Samsung Electronics, con su apalancamiento de Foundry, y Naver se mueven de forma diferenciada, eso mostrará si el mercado lee este anuncio como volumen o como cambio estructural.
- <strong>Resultados y conference call de Samsung Electronics y SK Hynix, 29-30 de julio.</strong> Aquí está la verdadera prueba. Hay que ver si el volumen de Broadcom se menciona junto con un calendario de procesamiento de obleas, si se adelanta el momento del giro a ganancias de Foundry, y si el alza del precio de contrato del tercer trimestre confirma el rango proyectado de +13-18% para la DRAM de servidor.
- <strong>FOMC y rueda de prensa del presidente Warsh, madrugada del 30 de julio.</strong> Si tratan el Brent por encima de 100 USD como algo transitorio será el veredicto del lado de la tasa de descuento.
- <strong>Resultados de Microsoft, Meta y Amazon, 30-31 de julio.</strong> Alphabet ya demostró la demanda, así que ahora les toca a estas tres demostrar el margen y el flujo de caja. Para que la carta de intención de suministro de SK Hynix a Microsoft cobre sustancia, la guía de capex de Microsoft tiene que respaldarla.
- <strong>Primer proyecto de la Corporación de Inversión Estratégica Corea-EE.UU., durante agosto.</strong> Llegará el primer caso de ejecución del vehículo de inversión de 350.000 millones USD hacia Estados Unidos. Podría convertirse en el primer documento que muestre cómo se conecta esta declaración con los aranceles.
- <strong>Evidencia de conversión.</strong> Hay que ver la divulgación concreta del volumen de Broadcom, la conversión del acuerdo de condiciones de Brookfield en un contrato vinculante, y la confirmación del sitio y la conexión a la red de los 2GW de SK Telecom. Si aparecen dos o más de estos elementos, los 950.000 millones de USD pasan de cifra a realidad. Si pasa el trimestre sin que aparezca ninguno, seguirán siendo solo cartas de intención.

El árbitro, una vez más, no cambia: es el precio de contrato de la DRAM. Por más grandes que sean la declaración y los MOU, si el precio de contrato se quiebra, el mercado descontará esa visibilidad hasta 2030.

---

Las acciones mencionadas en el texto son ejemplos para el análisis y no constituyen una recomendación de compra o venta de ningún valor en particular. La decisión de inversión y la responsabilidad por sus resultados recaen en cada inversor. La mayor parte de la cooperación anunciada se encuentra en etapa de cartas de intención, MOU y acuerdos de condiciones no vinculantes, y no son contratos vinculantes ni pedidos confirmados. Montos totales como los 950.000 millones de USD o los 750.000 millones de USD admiten doble conteo, porque la definición de cifra individual frente a cifra combinada varía según la fuente. La participación de 20-25% de Corea sobre el capex de IA es un cálculo propio que multiplica el peso de la HBM en el costo, la cuota de memoria de Corea y el peso de la memoria en el capex, y no es una estimación oficial de ninguna institución en particular. La participación de la memoria sobre el capex de la nube y el tamaño del mercado de IA soberana, entre otros datos, presentan una dispersión amplia entre las distintas firmas de investigación. El momento del giro a ganancias de Foundry y el rendimiento en 2nm varían según el medio. Las estadísticas relacionadas con la red eléctrica son de alcance nacional y no son datos que verifiquen directamente la viabilidad de proyectos individuales. Los datos de precios y flujos corresponden al cierre del 24 de julio de 2026 y no reflejan variaciones posteriores.

### Publicaciones relacionadas

- [Los fundamentos de la IA son sólidos, el problema son los tipos, el gatillo es el petróleo: la vía de transmisión del Brent a 94 USD a la memoria coreana](/es/post/oil-war-premium-rates-ai-multiple-korea-memory-2026-07-23/)
- [Alphabet en el segundo trimestre: Cloud +82% cierra el debate de la demanda, el FCF negativo abre el del efectivo](/es/post/alphabet-q2-2026-cloud-82-fcf-negative-memory-demand-2026-07-23/)
- [¿Quién quema todos esos tokens? El mapa de clientes de NVIDIA, la IA soberana y los 9 millones de Codex empiezan a responder](/es/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/)
- [¿Son cíclicos los semiconductores y cuál es el valor razonable? Valorando Samsung, SK Hynix y Micron con FCFE y beneficios normalizados](/es/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
