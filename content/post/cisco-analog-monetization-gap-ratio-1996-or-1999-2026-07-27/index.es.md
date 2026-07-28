---
title: "Cisco no murió por falta de demanda: reescribiendo la comparación puntocom-IA con el ratio de brecha de monetización"
slug: "cisco-analog-monetization-gap-ratio-1996-or-1999-2026-07-27"
date: 2026-07-27T10:00:00+09:00
description: "La versión popular de la comparación, demanda falsa entonces frente a demanda real ahora, es errónea. La demanda final también era real en 1999. Lo que hundió a Cisco un 89% no fue la ausencia de demanda sino la secuenciación: una financiación que corría cinco a diez años por delante. El ratio de brecha de monetización, gasto en infraestructura dividido por ingresos finales de IA, se ha estrechado de 8x a 4,6x y suena a 1996, mientras que la pila de compromisos de 1,4 billones de OpenAI y la llegada de la financiación de proveedor de NVIDIA suenan a 1999. En un sistema con ambas señales encendidas, el puente que decide la ruptura es el mercado de capitales. Auditamos la evidencia del reemplazo laboral por agentes y las implicaciones para la memoria coreana."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["Cisco", "Burbuja puntocom", "Burbuja IA", "Brecha de monetización", "Financiación de proveedor", "OpenAI", "NVIDIA", "CAPEX de IA", "IA agéntica", "Semiconductores coreanos", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexto
> En [Diseccionando 950.000 millones de dólares](/es/post/sf-ai-declaration-950bn-korea-equity-deep-analysis-2026-07-26/) escribimos que Corea quedó incorporada a la estructura de financiación circular de NVIDIA, y en [¿Quién quema todos esos tokens?](/es/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/) escribimos que la demanda final empezó a tener números concretos. Este artículo integra esas dos observaciones en una sola pregunta. ¿En qué año estamos? ¿En 1996 o en 1999? Reescribe la comparación con Cisco, la más invocada del mercado, no como un lugar común sino como un indicador, y converge el criterio decisivo en un único ratio.

## TL;DR

- Corregimos primero el lugar común. La comparación de que Cisco tuvo demanda falsa y ahora tenemos demanda real es errónea. <strong>La demanda final también era real en 1999</strong>. Los usuarios de internet crecían 50% al año, el tráfico 100% al año, y la fibra óptica tendida en ese momento acabó transportando YouTube y Netflix años después. La apuesta de infraestructura en sí fue acertada. Lo que hundió a Cisco un 89% no fue la ausencia de demanda sino <strong>la secuenciación: una financiación que corría cinco a diez años por delante de la demanda</strong>.
- Los ingredientes de la muerte fueron tres. El indicador mítico de que el tráfico se duplicaba cada 100 días (en realidad se duplicaba cada año), el crédito del comprador marginal que compraba equipos con bonos basura y financiación de proveedores, y la traición de ingresos de la deflación de precio unitario, en la que los ingresos no crecieron al ritmo de una caída de 90% en el precio del ancho de banda. La tasa de fibra oscura encendida se mantuvo por debajo de 5%.
- Proponemos el <strong>ratio de brecha de monetización (gasto en infraestructura dividido entre ingresos finales de IA)</strong> como el único número que separa las dos épocas. En la puntocom, el ratio se mantuvo entre 6 y 10 veces, se amplió y después estalló. En la IA fue de unas 8 veces en 2024, unas 6,5 veces en 2025 y unas 4,6 veces en 2026, <strong>y se está estrechando</strong>. Si se mira solo este eje, ahora mismo estamos en 1996.
- Pero si se mira no la ejecución sino los compromisos, la imagen se invierte. La pila de compromisos de compra de OpenAI llega a unos <strong>1,4 billones de dólares</strong>, diez veces más en solo 18 meses, con una cobertura de unas 35 veces frente a los ingresos anualizados de unos 40.000 millones USD. Y a esto se suma que la financiación de proveedores de NVIDIA acaba de aparecer. Si se mira solo este eje, es 1999.
- Al auditar con evidencia el último salto de la demanda, el reemplazo laboral por agentes, aparecen tres proposiciones distintas. El reemplazo de ciertas funciones específicas ya está demostrado (23% de los despidos del primer semestre en EE.UU. se atribuyen a la IA); la conversión de ese reemplazo en beneficios no está demostrada (Gartner: no hay diferencia de rentabilidad entre las empresas que más y las que menos recortaron personal); y el reemplazo total del trabajo del conocimiento sigue en etapa de relato. Aun así, <strong>solo con la franja estrecha de la masa salarial ya demostrada hay margen para que los ingresos actuales por tokens crezcan de 3 a 5 veces</strong>, así que el capex de 2026-2028 queda justificado únicamente con lo ya probado.
- El veredicto conjunto es el análogo de mediados de 1999. Históricamente, desde la aparición de la financiación de proveedores hasta la ruptura pasaron de 12 a 18 meses. Pero las dos caras de esta analogía son que quien compró incluso a mediados de 1999 ganó mucho hasta marzo de 2000, y que los tres indicadores reales, utilización, ratio de brecha y elasticidad, se mueven todos en dirección contraria a la puntocom.

<div class="thesis-callout">
<div class="thesis-callout__label">Marco clave</div>

La lección de Cisco no es que la demanda fuera falsa, sino que incluso la demanda real golpea primero a los accionistas con un menos 89% cuando la financiación corre de cinco a diez años por delante de ella. Desde la óptica de la demanda final, la IA de hoy es decisivamente distinta de la puntocom. La máquina de cobro ya está en marcha, la utilización de GPU es del 100%, el bolsillo que paga no es un presupuesto de ocio sino la masa salarial, y el ratio de brecha de monetización se está estrechando. Pero la aparición de la financiación de proveedores es exactamente la señal de mediados de 1999. El criterio decisivo converge en uno solo. Mientras los ingresos por tokens crezcan más rápido que el capex comprometido, esto es 1996; en el momento en que se inviertan, es 1999.

</div>

## 1. Corrigiendo el lugar común: la verdadera causa de muerte de Cisco

La demanda final de internet de 1999-2001 fue real y explosiva. Los usuarios crecían 50% al año, el tráfico 100% al año. Sobre la fibra óptica tendida en esa época crecieron después YouTube, Netflix y la nube. La historia dictaminó que la decisión de invertir en infraestructura fue, en sí misma, acertada. Y aun así, los accionistas de Cisco perdieron 89% desde el máximo. [Hecho: datos históricos]

Lo que mató a la empresa no fue la demanda, sino la combinación de lo siguiente.

<strong>El indicador mítico.</strong> La afirmación de que el tráfico se duplicaba cada 100 días (procedente de UUNet, del grupo WorldCom) se convirtió en la premisa estándar del sector, pero el tráfico real se duplicaba cada año. El indicador de demanda exagerado arrastró el capex de cinco a diez años por delante de la demanda real. [Hecho: datos históricos] Aunque la demanda sea real, si el indicador de demanda es falso, el capital corre a la velocidad equivocada.

<strong>El crédito del comprador marginal.</strong> Quien generaba los pedidos incrementales no eran las operadoras que generaban caja, sino operadoras de telecomunicaciones nuevas (CLEC) que compraban equipos con bonos basura y financiación de proveedores. La financiación de proveedores llegó a unos 25.000 millones USD. Cuando el mercado de capitales se cerró en 2000, los pedidos de esos compradores murieron al instante, y Cisco amortizó 2.200 millones USD de inventario mientras sus ingresos caían 30%. [Hecho: datos históricos] Antes que el tamaño de la demanda, lo que se derrumbó primero fue <strong>el origen del dinero que compraba esa demanda</strong>.

<strong>La traición de ingresos de la deflación de precio unitario.</strong> El precio del ancho de banda cayó 90%. El efecto Jevons del consumo funcionó: el tráfico siguió creciendo. Pero el Jevons de los ingresos en dólares no funcionó. La tasa de caída de precios superó a la tasa de crecimiento del uso, así que la elasticidad de ingresos cayó por debajo de 1, y la tasa de encendido de la fibra oscura ya tendida se mantuvo por debajo de 5%. [Hecho: datos históricos] La demanda física y la demanda en dólares son variables distintas, y el precio de la acción sigue al dólar.

La comparación solo resulta útil si se recuerdan estos tres factores al contrastarlos con el presente.

## 2. Contraste detallado: siete ejes

| Eje | Puntocom (1999-2000) | IA (2026) | Veredicto |
|---|---|---|---|
| Usuarios finales | Unos 280 millones, en crecimiento | Unos 1.000 millones (nivel ChatGPT), en crecimiento | Ambas son reales |
| Entidad de cobro | Dial-up a 20 USD al mes y publicidad todavía embrionaria | Suscripción de 20-200 USD al mes, pago por uso vía API, licencias empresariales. Los laboratorios frontera suman unos 50.000-60.000 millones USD anualizados, con un crecimiento de 2 a 3 veces al año | Ventaja de la IA. Hay una máquina de cobro en marcha que no existía en 1999 |
| Bolsillo que paga | Presupuesto de ocio del consumidor y publicidad | Sustitución de costo laboral corporativo (masa salarial global de decenas de billones de USD), presupuestos soberanos, consumidores | Categorías distintas. Pero el salto del reemplazo laboral está por verificar |
| Utilización | Tasa de fibra oscura encendida por debajo de 5% | GPU prácticamente al 100%, agotadas con lista de espera | La diferencia más decisiva |
| Deflación de precio unitario | Ancho de banda -90%, elasticidad de ingresos por debajo de 1 | Precio del token en caída libre, pero la elasticidad de ingresos todavía supera 1 | Mismo riesgo, resultado todavía opuesto. El eje que más hay que vigilar |
| Indicador mítico | El tráfico se duplica cada 100 días | Leyes de escalado, cronograma de la AGI, reemplazo laboral total | Ambos existen. La diferencia es que en la IA hay ingresos medidos en paralelo |
| Crédito del comprador marginal | Bonos basura de las CLEC y 25.000 millones USD de financiación de proveedores | El comprador principal es el FCF de los hiperescaladores, de 300.000-400.000 millones USD al año. Pero ya empezó la financiación de proveedores del comprador marginal | La señal clave de convergencia |

[Hecho: síntesis de datos históricos y notas proporcionadas]

De los siete ejes, cinco favorecen a la IA, uno (la deflación de precio unitario) comparte el mismo riesgo pero todavía con resultado opuesto, y el último (el crédito del comprador marginal) empezó a converger en la dirección mala. Este último eje domina la segunda mitad de este artículo.

## 3. El ratio de brecha de monetización: el único número que separa los dos casos

Si se reduce la esencia del caso Cisco a un único ratio, queda así. <strong>¿A cuántas veces los ingresos de la demanda final corre el gasto en infraestructura, y ese múltiplo se estrecha o se amplía?</strong>

| Período | Gasto en infraestructura | Ingresos finales | Ratio de brecha | Dirección |
|---|---|---|---|---|
| Puntocom 1999-2000 | Capex de telecomunicaciones de unos 220.000 millones USD | Ingresos finales de internet de unos 20.000-40.000 millones USD | 6-10 veces | Se mantuvo, se amplió y luego estalló |
| IA 2024 | Unos 250.000 millones USD | Unos 30.000 millones USD | Unas 8 veces | Punto de partida |
| IA 2025 | Unos 450.000 millones USD | Unos 70.000 millones USD | Unas 6,5 veces | Se reduce |
| IA 2026 (previsión) | Unos 600.000 millones USD | Unos 130.000 millones USD (suma de laboratorios, IA en la nube y copilotos) | Unas 4,6 veces | Se reduce |

[Inferencia: banda de estimación propia; el límite de atribución a la IA en el numerador y el denominador es difuso]

En la puntocom, mientras el capex se aceleraba, los ingresos por bit colapsaron y la brecha se amplió. En la IA, hasta ahora, ocurre lo contrario. Los tokens se están generando más rápido de lo que sale el dinero. Esto es coherente con la jerarquía confirmada en las cifras reales del primer trimestre de las grandes tecnológicas (el crecimiento de la cartera de pedidos supera al del capex, y el del capex supera al de los ingresos, aunque estos últimos se están acelerando), y también es coherente con el +82% de la nube y el uso que supera en 50% a lo comprometido que vimos en [Alphabet en el segundo trimestre](/es/post/alphabet-q2-2026-cloud-82-fcf-negative-memory-demand-2026-07-23/). La propuesta central de este artículo es que <strong>la dirección de este ratio es el único número que separa los dos casos</strong>.

## 4. El reemplazo laboral por agentes: una auditoría de la evidencia

En la tabla de contraste, el eje del bolsillo que paga como masa salarial llevaba la advertencia de un salto todavía no demostrado. Al auditar ese salto con base en las llamadas de resultados y las divulgaciones, aparecen tres proposiciones distintas.

<strong>Proposición 1: los agentes reemplazan funciones específicas. Ya demostrado.</strong>

| Actor | Evidencia | Cifra |
|---|---|---|
| Salesforce | Recorte de personal de soporte, confirmado por el CEO en la llamada | 4.000 personas recortadas, la IA gestiona cerca de 50% de las interacciones con clientes |
| Amazon | Mencionó explícitamente la inversión en IA en el recorte de personal corporativo de enero | 16.000 personas, extensión del mayor recorte corporativo de su historia |
| Intuit | Mencionó directamente la reasignación de recursos hacia la IA | 17% de la plantilla, unas 3.000 personas |
| Meta, Oracle, Block, entre otras | Suma de recortes que citaron explícitamente la IA como motivo | 184.000 personas |
| Monday.com | Aclaró que no era ahorro de costos sino una reorganización centrada en agentes de IA | 630 personas, un tipo cualitativamente nuevo |
| Recuento de Challenger | Proporción de despidos atribuidos a la IA sobre el total de EE.UU. en el primer semestre de 2026 | 23% (101.743 personas), motivo número uno de despido durante 4 meses seguidos |
| Medición funcional | Gestión del soporte de clientes de primer nivel por IA | Cerca de 80% del volumen, con un costo cerca de 80% menor |

[Hecho: divulgaciones, llamadas de resultados y estadísticas del sector, con base en los enlaces de fuente de las notas proporcionadas]

A esto se suma una desincronización a nivel de los estados financieros. Los ingresos por empleado de las Fortune 500, en 687.000 USD, y el beneficio por empleado, en 68.700 USD, son máximos históricos, pero mientras el beneficio bruto total crecía 12%, el empleo cayó por segundo año consecutivo, con una reducción de 301.000 personas. [Hecho: recuento de Fortune] La desincronización entre crecimiento y empleo ya empezó a registrarse en las estadísticas oficiales.

<strong>Proposición 2: ese reemplazo se convierte en beneficios. No demostrado. Este es el verdadero hallazgo de esta auditoría.</strong> Gartner encuestó a 350 ejecutivos y encontró que la rentabilidad financiera de las empresas que más recortaron personal y de las que menos recortaron era, en la práctica, la misma. [Hecho: informe de la encuesta de Gartner] Los despidos son reales, pero todavía no hay evidencia de que hayan mejorado el margen de beneficio. Esto significa que los costos de los recortes, la reasignación, el gasto en herramientas de IA y el deterioro de calidad (el caso de Klarna, que declaró que la IA sustituía a 700 personas y después volvió a contratar a parte de ellas) están compensando el ahorro. La evidencia del mercado laboral sobra, pero la evidencia en el estado de resultados está vacía. A esto se suma el sesgo del AI-washing. Como el mercado premia los recortes atribuidos a la IA y castiga los recortes por demanda débil, hay un incentivo fuerte para etiquetar como IA el ajuste del exceso de contratación de la era del COVID. Parte de esa tasa de atribución del 23% es relato.

<strong>Proposición 3: el reemplazo total del trabajo del conocimiento. Etapa de relato.</strong>

No hay evidencia en las divulgaciones. Es una premisa de los compromisos posteriores a 2029, no una medición del presente.

Pero la conclusión de esta auditoría es que la proposición 3 no hace falta para justificar el capex. Basta con calcular solo la franja estrecha ya demostrada. La masa salarial global de los call centers, el BPO, las funciones administrativas de back office y el apoyo a desarrolladores junior tiene un tamaño de 1,5 a 2,5 billones de dólares al año. Si solo 10% de eso se convierte en gasto de IA, ya son 150.000-250.000 millones USD al año, un <strong>margen de crecimiento de 3 a 5 veces que ya está dentro de una categoría demostrada</strong> frente a los ingresos actuales combinados de los laboratorios frontera (unos 50.000-60.000 millones USD anualizados). [Inferencia: aritmética de la masa salarial, banda de estimación] La reducción del ratio de brecha en 2026-2028 es posible solo con la proposición 1, y la proposición 3 solo se vuelve necesaria para los compromisos posteriores a 2029.

## 5. Flujo y acumulado: 1996 y 1999 están encendidos a la vez

Aquí aparece la tensión central de este artículo. En el mismo sistema, dos relojes señalan años distintos.

<strong>Flujo contra flujo. Los tokens están ganando.</strong> Los ingresos por tokens de los laboratorios frontera crecen 150-250% al año. OpenAI ronda los 40.000 millones USD anualizados (frente a los 15.000 millones USD de hace un año), Anthropic crece unas 3 veces, y Codex sumó 3 millones de usuarios en tres días. Los ingresos amplios de IA (laboratorios, IA en la nube y copilotos combinados) crecen 85-100% al año. En cambio, el capex que efectivamente se ejecuta crece 40-60% al año. La tasa de crecimiento de los ingresos es de 2 a 4 veces la del gasto. Por eso el ratio de brecha se estrecha de 8 a 4,6 veces. [Hecho: síntesis de mediciones de las notas proporcionadas] Si se mira solo este eje, es 1996.

<strong>Acumulado contra acumulado. Los compromisos están ganando.</strong> Si se mira no la ejecución sino la obligación futura ya contratada, la imagen se invierte. La pila de compromisos de compra de OpenAI suma cerca de <strong>1,4 billones de dólares</strong> entre Azure (unos 250.000 millones USD), Oracle (unos 300.000 millones USD), Broadcom (unos 350.000 millones USD, por 10GW de aceleradores a medida), la vinculación de 10GW ligada a la inversión de NVIDIA, los 6GW de AMD, y AWS y CoreWeave, y esa pila creció más de 10 veces en solo 18 meses. La cobertura frente a los ingresos anualizados de unos 40.000 millones USD es de unas 35 veces. Si este compromiso empieza a facturarse a razón de 250.000 millones USD al año desde 2027, los ingresos tendrían que multiplicarse por 6 en dos años para poder cubrirlo con la operación. [Hecho: síntesis de reportes públicos] Hay dos matices. Los 1,4 billones de dólares son la cifra de compromisos acumulados hasta mediados de la década de 2030 que el propio Altman ha venido revelando, y también hay reportes recientes de que a los inversionistas se les está guiando con un gasto real hasta 2030 rebajado a unos 600.000 millones USD. [Hecho: reportes] Es decir, la cobertura de 35 veces es la medida bajo el criterio más severo, y con el criterio de la guía de gasto baja a unas 15 veces. Con cualquiera de las dos definiciones, queda el hecho de que sigue siendo un orden de magnitud mayor que las 4,6 veces del flujo. Si se mira solo este eje, es 1999.

Y lo que tiende el puente entre las dos curvas es, precisamente, la financiación externa. La negociación entre NVIDIA y OpenAI que reportó el Wall Street Journal el domingo es el tablero más nuevo de ese puente. Se trata del campus de centros de datos de 10GW en el condado de Pike, Ohio (desarrollado por SB Energy, del grupo SoftBank, con una fase 1 de unos 800MW prevista para 2028), sobre el cual NVIDIA está negociando una <strong>garantía de unos 250.000 millones USD</strong> para el arrendamiento y la deuda de construcción, y por separado una <strong>financiación de compra de chips de 350.000 millones USD</strong>. Todavía está en etapa de negociación, y también se reportó la posibilidad de que se frustre. [Hecho: WSJ, Reuters, CNBC; etapa de negociación] La estructura es clara. Es el vendedor garantizando tanto el dinero para comprar sus propios chips como la deuda del edificio donde entrarán esos chips, es decir, financiación de proveedores. La inversión de NVIDIA en Naver que vimos la semana pasada en [Diseccionando 950.000 millones de dólares](/es/post/sf-ai-declaration-950bn-korea-equity-deep-analysis-2026-07-26/) pertenece a la misma familia. El solo hecho de que haya aparecido la financiación de proveedores es el primer encendido de la señal del reloj de Cisco.

Las implicaciones de esta estructura se resumen en tres puntos. 2026-2027 es aritmética. El capex que se ejecuta está físicamente atado a la cadena de suministro eléctrica y de chips, así que es difícil que crezca más de 50% al año, mientras que los ingresos crecen a un ritmo de tres dígitos, así que la brecha sigue estrechándose. La probabilidad de ruptura en este tramo es baja. 2028-2029 es condicional. Para que la cobertura se normalice hacia el momento en que aterrice la ola de compromisos de 1,4 billones de dólares, los ingresos tienen que mantener un crecimiento compuesto de 80-100% al año durante 2 o 3 años más. Es alcanzable si el ritmo de crecimiento actual desacelera de forma gradual, y sería una catástrofe si se reduce a la mitad cada año. Por lo tanto, <strong>la verdadera restricción vinculante no son ni los ingresos ni el capex, sino el puente, es decir, el mercado de capitales</strong>. Mientras la financiación esté abierta, las dos curvas tienen tiempo para converger; si se cierra, la pila de compromisos se derrumba y solo queda la parte ya financiada. Por eso la caída del ratio de cobertura de la demanda de bonos (de unas 5 veces a comienzos de año a cerca de 2 veces recientemente) y la propagación de la financiación de proveedores son una alerta temprana que se adelanta al propio ratio de brecha.

## 6. Veredicto del reloj: ¿en qué año estamos?

Ponemos en una tabla el estado de encendido de cada señal de la muerte de Cisco.

| Señal | Momento en la puntocom | Estado actual | ¿Encendida? |
|---|---|---|---|
| Aparición de la financiación de proveedores | 1999 | Reportes de la negociación de NVIDIA sobre la garantía de deuda y la financiación de chips de OpenAI | Encendida. Análogo de 1999 |
| Fatiga del mercado de capitales | Principios de 2000 | Caída del ratio de cobertura de bonos, ampliación de las concesiones | Señal inicial |
| Reversión a la ampliación del ratio de brecha | 1999-2000 | Todavía en reducción | Apagada |
| Colapso de la utilización | 2000-2001 (fibra oscura) | GPU agotadas con lista de espera | Apagada |
| Paso de la elasticidad de ingresos por debajo de 1 | 2000 (ancho de banda) | Todavía por encima de 1 | Apagada |
| Precipicio de pedidos | 2001 | La cartera de pedidos crece a un ritmo de dos dígitos altos | Apagada |

[Inferencia: marco de señales, basado en notas proporcionadas]

El veredicto es este. No estamos a finales del año 2000, sino en el <strong>análogo de mediados de 1999</strong>. La financiación de proveedores acaba de aparecer (históricamente fue una señal de 12 a 18 meses antes de la ruptura), el resto de las señales sigue apagado, y en particular los tres indicadores reales, utilización, ratio de brecha y elasticidad, se mueven todos en dirección contraria a la puntocom. Pero hay que recordar juntas las dos caras de esta analogía. Quien compró incluso a mediados de 1999 ganó mucho hasta marzo de 2000, y después lo devolvió todo. Si la analogía es correcta, el retorno del tramo que queda también es grande, y la dificultad de gestionar la salida también lo es.

Dejamos también consignadas con claridad las condiciones para converger en el camino de Cisco. Que la elasticidad de ingresos por tokens caiga por debajo de 1 (que la caída de precio unitario supere al crecimiento del uso), que el ratio de brecha revierta hacia la ampliación (que aterrice el capex comprometido mientras los ingresos se estancan), o que la contaminación de crédito del comprador marginal se propague hasta el núcleo de los hiperescaladores. Ninguna de las tres se ha encendido todavía, y las tres se pueden medir trimestre a trimestre.

## 7. Implicaciones para los semiconductores coreanos: el proveedor cayó más hondo

Siguiendo la costumbre de esta serie, añadimos la óptica coreana. Lo que los inversionistas coreanos deben recordar de la ruptura puntocom no es la caída de Cisco. Es el hecho de que <strong>las empresas que le vendían componentes a Cisco cayeron más hondo que la propia Cisco</strong>. JDS Uniphase y Nortel, de componentes ópticos, perdieron cerca de 99% desde su máximo. [Hecho: datos históricos] La ruptura de la secuenciación se transmite amplificada hacia arriba en la cadena de valor. Los pedidos de bienes intermedios se rompen antes de que caiga la demanda final, porque el látigo de inventario se sacude con más fuerza precisamente en el eslabón más alto de la cadena. La amortización de 2.200 millones USD de inventario de Cisco también significaba que los ingresos de esos proveedores aguas arriba ya habían desaparecido antes.

La memoria coreana de hoy está ubicada en ese eslabón alto. Por eso, al traducir el marco del ratio de brecha a la óptica de la memoria, aparece un indicador adicional que vigilar. <strong>La calidad crediticia de la mezcla de compradores.</strong> El comprador principal de memoria hoy son los hiperescaladores, que generan un FCF de 300.000-400.000 millones USD al año, y esa es la diferencia fundamental frente a la Cisco de 1999, que le vendía a las CLEC. Pero a medida que avanza la financiación de proveedores, es decir, a medida que crece el peso de las neonubes, los compradores financiados con deuda y los pedidos que dependen de garantías, el crédito tipo 1999 también se filtra en los pedidos de memoria. La incorporación de Corea a la financiación circular que vimos la semana pasada (la estructura en la que NVIDIA invierte en Naver y Naver usa ese dinero para comprarle a NVIDIA) significa que esa puerta también se abrió del lado coreano.

Las dos caras del contrato de suministro a largo plazo (LTA) también se vuelven más precisas dentro de este marco. El LTA da visibilidad de precio y de volumen, pero Cisco también tenía en 2000 una cartera de pedidos abultada, y esa cartera terminó en 2001 en cancelaciones y amortizaciones. <strong>Lo que protege el LTA es el precio dentro de un mundo en el que la contraparte contractual mantiene su capacidad de pago, no ese mundo en sí mismo.</strong> Que el presidente de SK Hynix, Chey Tae-won, haya señalado como su mayor preocupación a cinco años la posible ruptura del suministro de financiación de la IA apunta exactamente a esta estructura.

La conclusión práctica es simple. Al precio de contrato del DRAM, que ha sido el criterio decisivo de los inversionistas de memoria, se le añaden dos más. La dirección trimestral del ratio de brecha de monetización, y el peso de los compradores de FCF frente a los compradores financiados con deuda dentro de la mezcla de compradores finales de memoria. Mientras los dos primeros se mantengan sanos, la corrección es una oportunidad; cuando los tres empeoren a la vez, ese será el momento de 1999.

## 8. Cuadro de lectura: los indicadores que se colocan en la compuerta

- <strong>El ratio de brecha de monetización trimestral.</strong> Ingresos de laboratorios e IA en la nube frente al capex de IA. Empezamos el seguimiento trimestral desde esta temporada de resultados. En los resultados de Microsoft, de madrugada (06:30 KST) del 30 de julio, y de Amazon, de madrugada (06:00 KST) del 31 de julio, en hora de Corea, el veredicto del próximo trimestre depende de si el ratio de flujo (aceleración de ingresos de IA frente al incremento de la guía de capex) se mantiene por encima de 1.
- <strong>Medición de la elasticidad de ingresos.</strong> Seguimiento simultáneo del precio del token y de los ingresos por tokens. Mientras los ingresos sigan creciendo pese a la caída del precio unitario, el camino sigue separado del que tomó el ancho de banda.
- <strong>La próxima ronda de encuestas del tipo Gartner sobre despidos y rentabilidad.</strong> Es el indicador que decide la proposición 2 (la conversión del reemplazo en beneficios). Si esto se rompe, la aritmética de la masa salarial pasa al estado de resultados.
- <strong>Divulgación cuantitativa de los ingresos agénticos.</strong> Si en esta temporada de llamadas de resultados empieza a divulgarse en cifras concretas el monto contratado de productos tipo Agentforce de Salesforce. También seguimos en paralelo, mes a mes, la proporción de despidos atribuidos a la IA según Challenger.
- <strong>El estado del puente.</strong> El diferencial de crédito de la IA, el ratio de cobertura de la demanda de bonos, y la línea de método de participación de Microsoft (que refleja el resultado de OpenAI). Como la conclusión de este artículo es que la velocidad de propagación de la financiación de proveedores es una alerta temprana que se adelanta al propio ratio de brecha, la cobertura de la próxima colocación de bonos de un hiperescalador es la señal más temprana.
- <strong>La calidad de la cartera de pedidos.</strong> Cuanto más crezca, dentro de los nuevos compromisos, el peso de lo que no son laboratorios (empresas, soberanos), mejor será la calidad crediticia de la pila de compromisos.

El criterio decisivo converge en uno solo. <strong>Mientras los ingresos por tokens crezcan más rápido que el capex comprometido, esto es 1996; en el instante en que se inviertan, es 1999.</strong> Y hasta que se dicte ese veredicto, el criterio decisivo de la memoria coreana sigue siendo, sin cambios, el precio de contrato del DRAM y la calidad crediticia de la mezcla de compradores.

---

Las acciones mencionadas en el texto son ejemplos para el análisis y no constituyen una recomendación de compra o venta de ningún valor en particular. La decisión de inversión y la responsabilidad por sus resultados recaen en cada inversor. El numerador y el denominador del ratio de brecha de monetización son una banda de estimación en la que el límite de los ingresos atribuidos a la IA es difuso, y las cifras de la época puntocom son aproximaciones basadas en datos históricos. La pila de compromisos de OpenAI es una suma de reportes públicos y declaraciones de directivos, no una divulgación oficial de la empresa, y puede diferir del plan de gasto real; la garantía y la financiación de chips de NVIDIA corresponden a reportes en etapa de negociación, junto con los cuales también se reportó la posibilidad de que se frustren. La atribución de los despidos a la IA lleva implícito un sesgo narrativo, y la aritmética de la masa salarial es una banda de estimación. Datos de mercado como el ratio de cobertura de bonos pueden variar según el método de recopilación. El veredicto del reloj y los años de escenario no son una predicción estadística, sino un marco de juicio.

### Publicaciones relacionadas

- [Diseccionando 950.000 millones de dólares: tres cosas que cambió la Declaración de IA de San Francisco y una que no](/es/post/sf-ai-declaration-950bn-korea-equity-deep-analysis-2026-07-26/)
- [Alphabet en el segundo trimestre: Cloud +82% cierra el debate de la demanda, el FCF negativo abre el del efectivo](/es/post/alphabet-q2-2026-cloud-82-fcf-negative-memory-demand-2026-07-23/)
- [¿Quién quema todos esos tokens? El mapa de clientes de NVIDIA, la IA soberana y los 9 millones de Codex empiezan a responder](/es/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/)
- [El verdadero debate en semiconductores: cuatro relojes físicos y un reloj bursátil](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
