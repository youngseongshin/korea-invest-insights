---
title: "SemiScope: OpenEdges Technology — Opción de IP LPDDR6 en Samsung 4/5/8nm, No una Apuesta por NPU"
slug: semiscope-openedges-samsung-lpddr6-ip-option-2026-04-30
aliases: ["/en/post/semiscope-openedges-samsung-lpddr6-ip-option-2026-04-30/"]
date: 2026-04-30T12:00:00+09:00
description: "OpenEdges Technology (394280 KQ) debe analizarse menos como una acción coreana de NPU y más como una opción de IP de subsistema de memoria LPDDR5X/LPDDR6 en Samsung 4/5/8nm. Este seguimiento de SemiScope revisa el foso de producto, la estructura de subsidiarias, la dilución, la valoración y los hitos necesarios antes de ampliar la exposición."
categories: ["Cadena de Suministro Tecnológica de Corea", "IP de Semiconductores"]
tags: ["OpenEdges Technology", "394280", "SemiScope", "Samsung Foundry", "LPDDR6", "LPDDR5X", "DDR PHY", "Controlador de Memoria", "NoC", "OpenEdges Square", "Fabless de Corea", "IP de Semiconductores"]
series: ["semiscope-2026"]
---

> **Seguimiento SemiScope.** La primera nota sobre OpenEdges presentó a la empresa como la escasa plataforma coreana de IP de subsistema de memoria con una larga curva J de regalías. Esta segunda entrega reduce el enfoque a la pregunta de inversión concreta: OpenEdges Technology no es principalmente una "acción de NPU". Es una opción de IP de subsistema de memoria LPDDR5X/LPDDR6 en Samsung 4/5/8nm, y la acción solo merece una posición mayor cuando los contratos de licencia, el reconocimiento de ingresos, la mezcla de regalías y el control de costos comiencen a confirmar dicha opción.

---

## Lecturas Relacionadas

- [SemiScope: OpenEdges Technology - La Plataforma Coreana de IP de Subsistema de Memoria con una Opción de Curva J en Regalías](/en/post/semiscope-openedges-technology-ip-platform-2026-04-25/)
- [SemiScope: Tres Nombres Coreanos de ATE e IP de Memoria Reclasificados — Por Qué Exicon es la Apuesta de la Curva J en 2026, No la Reflexión Tardía](/en/post/semiscope-neosem-exicon-openedge-rerank-2026-04-25/)

---

## Resumen Ejecutivo

1. **OpenEdges se comprende mejor como una empresa de IP de subsistema de memoria que como una empresa de NPU.** El enfoque de inversión central es el PHY LPDDR5X/LPDDR6, el controlador de memoria y el NoC integrados para ASICs de IA, IA en el edge, automoción y otros chips con alta demanda de datos.
2. **Samsung Foundry 4/5/8nm es el campo de batalla concreto.** La acción no es una apuesta a que OpenEdges derrote a Synopsys o Cadence en la frontera global de 2/3nm. Es una apuesta a que los nodos intermedios y avanzados de Samsung para el mercado masivo necesitan IP de LPDDR local, con conocimiento del proceso y credibilidad demostrada.
3. **La cadena de valor aún es temprana: portado, licencia, tape-out, prueba en silicio, producción, regalías.** OpenEdges ha superado la fase de I+D pura, pero aún no es una plataforma de regalías madura.
4. **TSS y la unidad de Japón fortalecen la base tecnológica. OpenEdges Square es una opción de mayor riesgo.** TSS y Japón son subsidiarias al 100% vinculadas a la profundidad del PHY DDR y el controlador de memoria. Square es más interesante pero también más dilutiva, ya que la matriz posee aproximadamente el 65%.
5. **La valoración ya descuenta un futuro mejor.** Una capitalización de mercado de aproximadamente KRW 530B frente a ingresos proyectados para 2026 de KRW 30,4B-31,8B implica un múltiplo precio/ventas de unas 16,7x-17,5x. Esto solo funciona si llegan los contratos de LPDDR6/5X, la aceleración de ingresos en 2T-3T, la disciplina de costos y el avance en regalías.

**Conclusión:** OpenEdges sigue siendo candidata a **Lista de Seguimiento / Posición Piloto**. Una posición piloto del 0,3%-0,5% puede justificarse para inversores que deseen exposición a la capa de IP de semiconductores de Corea. Escalar por encima del 1% debería esperar a que se consoliden contratos repetidos de LPDDR6/5X, una aceleración visible de ingresos, menor gasto fijo y mayor visibilidad sobre OpenEdges Square.

---

## 1. Qué Añade Esta Nota a la Primera Entrega de SemiScope sobre OpenEdges

La primera nota de SemiScope presentó el argumento general: OpenEdges Technology (394280 KQ) es la escasa plataforma de IP de semiconductores de Corea, con controlador de memoria, PHY DDR, NPU, NoC, UCIe e IP de memoria adyacente a CXL bajo un mismo techo. Esa visión se mantiene.

Pero el seguimiento más útil es más específico.

El mercado tiende a etiquetar a OpenEdges como una acción de "semiconductores de IA" o "NPU". Eso es demasiado impreciso. El activo más invertible de la empresa no es el NPU en sí mismo. Es el camino de la memoria alrededor del cómputo de IA:

`DRAM - DDR PHY - Controlador de Memoria - NoC - NPU / CPU / Acelerador`

Para un ASIC de IA o un chip de inferencia en el edge, el cómputo no es el único cuello de botella. El movimiento de datos puede ser igual de importante. Si la interfaz de memoria es lenta, consume mucha energía o es inestable, los TOPS teóricos del chip no importan demasiado. Por eso el IP de PHY y controlador LPDDR5X/LPDDR6 puede volverse estratégico.

La tesis revisada es:

> OpenEdges es una opción de compra sobre los clientes de Samsung 4/5/8nm en IA y ASICs en el edge que necesitan IP de subsistema de memoria LPDDR5X/LPDDR6 con prueba en silicio.

Esta formulación importa. Preserva el potencial alcista pero elimina la exageración. La empresa aún no es una campeona global de IP. Aún no es un compounder de ganancias de alta calidad. Es un proveedor de IP con fuerte inversión en I+D con una oportunidad creíble de convertirse en la capa de subsistema de memoria doméstica para una parte de la base de clientes de Samsung Foundry.

---

## 2. Corrigiendo el Marco de Producto: El NPU No Es el Centro

OpenEdges posee y desarrolla varios bloques de IP:

| Familia de producto | Función | Significado para la inversión |
|---|---|---|
| **DDR PHY** | Capa de señal física entre el SoC y la DRAM | Mayor barrera técnica; IP duro específico del nodo; requiere prueba en silicio |
| **Controlador de Memoria DDR** | Controla el acceso a memoria, la programación y el comportamiento del protocolo | Se vuelve más valioso cuando se combina con el PHY |
| **Interconexión en chip / NoC** | Mueve datos dentro del SoC | Más importante a medida que los ASICs de IA agregan más bloques de cómputo |
| **NPU / ENLIGHT** | Aceleración de inferencia de IA | Útil, pero más débil como tesis de inversión independiente |
| **Controlador UCIe / chiplet** | Comunicación entre dies en sistemas chiplet | Opción a largo plazo a medida que se amplíe la adopción de chiplets |
| **IP de memoria adyacente a CXL** | Bloques de controlador de memoria y PHY utilizados por potenciales diseñadores de chips controladores CXL | Exposición indirecta a CXL, sin visibilidad de ingresos como la de equipos |

La versión más sólida de la empresa no es "vendemos un NPU". Es "reducimos los cuellos de botella de memoria en chips de IA vendiendo un subsistema de memoria integrado".

Ahí es también donde aparece el costo de cambio. Un bloque de IP soft independiente a menudo puede ser reemplazado. Una combinación de PHY más controlador más NoC que ha sido integrada, verificada y sincronizada dentro de un chip es mucho más difícil de sustituir. El calendario de tape-out del cliente, el plan de verificación, el presupuesto de energía y el cierre de temporización pueden verse todos afectados.

Por eso la acción debe separarse de los nombres de equipos como NeoSem y Exicon. Esas empresas pueden convertir pedidos en ingresos en aproximadamente seis a nueve meses. OpenEdges vende IP de diseño aguas arriba. Su retorno toma más tiempo, pero el potencial de regalías puede ser más duradero si los chips de los clientes alcanzan producción en masa.

---

## 3. La Cadena de Valor del IP: No Confundir el Portado con las Regalías

La secuencia operativa más importante es:

`Portado - contrato de licencia - tape-out del cliente - prueba en silicio - producción - regalías`

OpenEdges ha avanzado más allá de "tecnología sin interés de clientes". Su material de IR de 2026 apunta a más de 30 clientes, 71 contratos de licencia acumulados, más de 20 productos de IP comercializables y una plantilla de unas 170 personas, incluidos aproximadamente 149 empleados de I+D. Ese no es el perfil de una empresa de papel.

Pero es igualmente importante no saltar demasiado rápido de "portado" a "plataforma de regalías".

| Etapa | Qué demuestra | Qué aún no demuestra |
|---|---|---|
| Portado | El IP puede adaptarse al nodo de proceso objetivo | Que un cliente de pago lo haya adoptado |
| Contrato de licencia | El cliente se ha comprometido a usar o evaluar el IP | Que el chip llegará al tape-out con éxito |
| Tape-out | El diseño del cliente ha pasado a fabricación | Que el silicio cumplirá los requisitos de producción |
| Prueba en silicio | El IP funciona en silicio real | Que el cliente enviará alto volumen |
| Producción | El chip del cliente es comercial | La escala de regalías depende aún del volumen unitario |
| Regalías | El modelo tiene economía de capitalización compuesta | La sostenibilidad depende de diseños repetidos |

La mezcla de regalías aún es pequeña. Los materiales previos de OpenEdges y análisis de firmas de venta apuntan a que los ingresos por regalías representan solo una fracción mínima de las ventas recientes. Una proyección de 2026 sitúa los ingresos por regalías en torno a KRW 1,7B frente a KRW 30,4B de ingresos totales, es decir, aproximadamente el 5,6%.

Ese rango del 5%-6% es un avance respecto al nivel del 1S25, pero aún no es la curva al estilo ARM que los inversores aspiran a ver. Para que esta acción se revalorice hasta convertirse en un verdadero compounder de IP de alta calidad, querría ver la mezcla de regalías moviéndose hacia el 20% de los ingresos trimestrales y aún en ascenso.

---

## 4. Por Qué Importa Samsung 4/5/8nm

La expresión "Samsung 4/5/8nm" no debe leerse como una historia vaga del ecosistema Samsung. Es específica.

El atajo incorrecto es:

> OpenEdges tiene LPDDR6 pre-portado en todos los nodos Samsung de 4-8nm.

La versión correcta es:

> OpenEdges está expandiendo su cobertura en torno a Samsung 4nm LPDDR6 y Samsung 4/5/8nm LPDDR5X de alta velocidad, apuntando a clientes de IA, edge, automoción y otros ASICs que necesitan mejores interfaces de memoria en los nodos de mercado masivo de Samsung Foundry.

Según el mapa de ruta de IR de 2026 citado en el material fuente, OpenEdges ya provee cobertura Samsung 5nm LPDDR5X/LPDDR5/LPDDR4X/LPDDR4. Samsung 8nm LPDDR5X aparece como elemento de desarrollo del 1S26, mientras que Samsung 4nm LPDDR5X a 10,7 Gbps y LPDDR6 a 14,4 Gbps aparecen como elementos de desarrollo del 2S26.

Este es el campo de batalla correcto para OpenEdges.

La frontera de 2/3nm es donde dominan los gigantes globales. Synopsys, Cadence, Arm, Rambus y otros líderes en IP de interfaces tienen mayor soporte en campo, relaciones más amplias con las fundidoras y más referencias en nodos avanzados. No es realista apostar por OpenEdges como ganadora global a corto plazo en esa capa.

La oportunidad más realista está en el mercado masivo intermedio y avanzado:

- IA en dispositivo;
- chips de IA automotriz;
- controladores de IA para robots e industria;
- chips de IoT y hogar inteligente;
- ASICs de cámara de seguridad y visión;
- chips de defensa y propósito especial;
- proyectos domésticos de aceleradores de IA;
- programas de ASIC llave en mano liderados por casas de diseño.

Estos clientes no siempre necesitan el proceso de 2/3nm más caro. Puede que les importe más el costo, el consumo energético, el ancho de banda de memoria, el soporte local, la reducción de riesgos y la disponibilidad del proceso Samsung. Ahí es donde puede importar un proveedor doméstico de IP de subsistema de memoria.

La pregunta central es:

> ¿Crece suficientemente el grupo de clientes de Samsung de 8nm y por debajo que necesitan LPDDR5X o LPDDR6 como para generar contratos de licencia repetidos para OpenEdges?

Si la respuesta es sí, la acción tiene un camino claro hacia una narrativa de mayor calidad. Si es no, la empresa seguirá siendo un proveedor de IP técnicamente interesante pero con dificultades financieras.

---

## 5. Foso Dentro de la Cadena de Valor de Samsung

El problema de Samsung Foundry no es solo la tecnología de proceso. También necesita un ecosistema más sólido: IP, EDA, casas de diseño, referencias de verificación y soporte al cliente. OpenEdges puede ayudar a fortalecer una capa de esa estructura.

| Nodo de la cadena de valor de Samsung | Necesidad de Samsung | Rol de OpenEdges |
|---|---|---|
| Samsung Memory | Adopción de DRAM LPDDR5X/LPDDR6 | Beneficiario indirecto de una mayor adopción de LPDDR |
| Samsung Foundry | Más contratos de clientes en 4/5/8nm | Provee IP de interfaz de memoria consciente del proceso |
| SAFE / ecosistema de IP | Menor riesgo de diseño para el cliente | Agrega opciones domésticas de PHY, controlador y NoC |
| Casas de diseño | Paquetes ASIC llave en mano | Puede insertarse en flujos de diseño repetidos |
| Clientes fabless / ASIC | Tape-out más rápido con menor riesgo de memoria | Resuelve cuellos de botella de memoria de alta velocidad y bajo consumo |

La primera capa del foso es el **portado del PHY DDR**. El PHY no es software genérico. Es un bloque de IP duro con complejidad analógica y de señal mixta. A velocidades de 8,5-14,4 Gbps, importan la integridad de señal, el jitter, el ruido, la variación de voltaje/temperatura, el margen de temporización y los algoritmos de entrenamiento. Un bloque de IP basado solo en simulación no es suficiente. Los clientes quieren prueba en silicio.

La segunda capa del foso es la **integración de PHY + controlador + NoC**. Los clientes de ASICs de IA no necesitan simplemente una disposición de pines de interfaz. Necesitan un sistema de movimiento de datos que funcione. Si OpenEdges puede vender el camino de memoria como un paquete integrado, crea un costo de cambio mayor que cualquier bloque individual por separado.

La tercera capa del foso es el **aprovechamiento del canal de casas de diseño**. Si una casa de diseño usa repetidamente el IP de OpenEdges en proyectos Samsung llave en mano, OpenEdges no necesita vender a cada cliente de forma independiente. El IP puede convertirse en parte de un paquete replicable.

El foso no es absoluto. Es local y específico al proceso. Pero los fosos locales y específicos al proceso pueden generar atractivos retornos en mercados públicos cuando la base de ingresos es pequeña.

---

## 6. Subsidiarias: ¿Qué Pertenece a los Accionistas?

La estructura de subsidiarias importa porque OpenEdges no es solo una entidad cotizada con una línea de producto limpia. El material de IR de 2026 desglosa el grupo en la matriz y las subsidiarias clave.

| Entidad | Participación de la matriz | Función principal | Lectura para la inversión |
|---|---:|---|---|
| **Matriz OpenEdges Technology** | - | I+D de IP, ventas y estrategia de plataforma integrada | Negocio cotizado principal |
| **The Six Semiconductor (TSS)** | 100% | I+D de IP de PHY DDR | Fortalece el foso técnico clave |
| **OpenEdges Technology Japan** | 100% | I+D de IP de Controlador de Memoria y capacidad orientada a Japón | Refuerza la profundidad del controlador y el acceso a talento regional |
| **OpenEdges Square** | aprox. 65% | Plataforma de ventas de IP en línea, CC NoC y futuras opciones de plataforma | Opción de mayor riesgo; el potencial alcista no pertenece íntegramente a la matriz |

TSS debe verse como un activo de foso, no como dilución. El PHY DDR es la parte más difícil del conjunto. Si TSS profundiza la capacidad de PHY de alta velocidad, la economía repercute en la matriz porque es de propiedad total.

La unidad de Japón es similar. El IP de controlador de memoria es menos intensivo en analógica que el PHY, pero está próximo a la arquitectura del cliente y los requisitos del producto. Japón también tiene profundidad en ingeniería de semiconductores y relaciones con clientes relevantes. De nuevo, dado que esta unidad es 100% propiedad de la matriz, el problema es el costo, no la pérdida de valor.

OpenEdges Square es diferente.

Square no es simplemente una rama de ingeniería. Se lanzó con ambiciones de plataforma de ventas de IP en línea y el desarrollo del CC NoC. El CC NoC, o red en chip con coherencia de caché, puede volverse valioso si los ASICs de IA multinúcleo requieren un movimiento de datos interno más sofisticado y comportamiento de coherencia de caché.

La opción es interesante. La propiedad es menos clara. Si la matriz posee aproximadamente el 65,4% de Square, la exposición efectiva de un accionista de OpenEdges a Square es solo el 65,4% de su participación en la empresa matriz.

Ejemplo:

`1,0% de participación en la matriz x 65,4% de propiedad de Square = 0,654% de exposición efectiva a Square`

Eso no es automáticamente malo. El capital externo puede reducir la carga de caja de la matriz y acelerar el desarrollo. Pero significa que el éxito de Square no repercute al 100% en los accionistas cotizados.

Trataría a Square como una opción de compra con dos preguntas:

1. ¿Puede el CC NoC convertirse en un producto comercial real en lugar de seguir siendo una historia de desarrollo?
2. ¿Pueden las necesidades de costo y financiación de Square mantenerse lo suficientemente controladas como para que la opción no debilite el estado financiero de la matriz?

---

## 7. Dilución y Financiación: La Emisión de CPS de 2026

OpenEdges captó aproximadamente KRW 20,0B en marzo de 2026 mediante una asignación a terceros de acciones preferentes convertibles. Las cifras clave del material fuente son:

| Concepto | Cifra |
|---|---:|
| Nuevas acciones preferentes | 1.145.278 |
| Acciones ordinarias existentes antes de la emisión | 26.276.655 |
| Aumento potencial de acciones ordinarias | 1.145.278 |
| Impacto declarado sobre el número de acciones | 4,18% |
| Precio de emisión | KRW 17.463 |
| Precio de referencia | KRW 17.054 |
| Prima sobre el precio de referencia | 2,4% |
| Período de conversión | 8 abr. 2027 al 8 abr. 2031 |
| Suelo del precio de conversión | KRW 12.225 |

El cálculo de la dilución es:

`1.145.278 / (26.276.655 + 1.145.278) = 4,18%`

Esta es dilución real. No debe ignorarse. Los puntos más favorables son que la emisión se realizó con prima sobre el precio de referencia y que el efectivo amplía el horizonte de I+D.

El riesgo es el reajuste. Si el precio de la acción cae y el precio de conversión se ajusta a la baja hacia el suelo, la dilución efectiva puede aumentar. Para una empresa que aún financia I+D antes de alcanzar regalías maduras, el costo de capital sigue siendo parte de la tesis.

---

## 8. Valoración: La Acción Ya Descuenta un Futuro Mejor

Usando la instantánea de mercado en torno al 29 de abril de 2026, OpenEdges cotizaba cerca de KRW 20.150 con una capitalización de mercado de aproximadamente KRW 530,9B. Frente a supuestos de ingresos para 2026 de aproximadamente KRW 30,4B-31,8B, el múltiplo precio/ventas es elevado.

| Base de ingresos | Cálculo | PSR implícito |
|---|---:|---:|
| Ingresos 2026F KRW 30,4B | KRW 530,9B / KRW 30,4B | **17,5x** |
| Ingresos 2026F KRW 31,8B | KRW 530,9B / KRW 31,8B | **16,7x** |

No es una pequeña empresa cíclica barata. Es una opción costosa sobre un modelo de negocio futuro mejor.

El mercado ya está descontando varias cosas:

- los ingresos de 2026 superan los KRW 30B;
- la empresa se aproxima al punto de equilibrio en 2S26 o 2027;
- los contratos de LPDDR6/5X se vuelven recurrentes;
- la actividad de clientes de Samsung 4/5/8nm mejora;
- OpenEdges Square aporta valor como opción más que solo como costo;
- los ingresos por regalías se vuelven gradualmente visibles.

Eso es un punto de partida exigente. La conclusión correcta no es "evitar". La conclusión correcta es "no escalar hasta que la empresa demuestre suficiente parte del mapa de ruta".

---

## 9. Marco de Inversión

### Idea 1 — IP de subsistema de memoria LPDDR para Samsung 4/5/8nm

| Concepto | Visión |
|---|---|
| Lógica central | Los clientes de Samsung Foundry 4/5/8nm necesitan IP de PHY y controlador LPDDR5X/LPDDR6 de alta velocidad |
| Palanca de precio | El IP de LPDDR avanzado puede elevar el ASP |
| Palanca de volumen | Múltiples licencias nuevas o uno o dos grandes contratos de referencia |
| Palanca de costo | El crecimiento del costo fijo de I+D debe desacelerarse |
| Punto crítico | Portado del PHY específico al proceso y prueba en silicio |
| Error del mercado | Tratar a OpenEdges solo como una acción de NPU |
| Caso bajista | El grupo de clientes de Samsung no se expande suficientemente |
| Confirmación | Contratos repetidos de LPDDR6/5X, tape-out o prueba en silicio en Samsung 4nm |

### Idea 2 — TSS y el PHY DDR como el verdadero foso

| Concepto | Visión |
|---|---|
| Lógica central | El PHY es la parte más difícil del conjunto del subsistema de memoria |
| Palanca de precio | El PHY de alta velocidad probado en silicio puede generar mejor economía |
| Palanca de volumen | Cobertura en nodos Samsung y TSMC seleccionados |
| Palanca de costo | El talento de I+D de alto nivel debe retenerse sin un gasto descontrolado |
| Punto crítico | PHY probado en silicio en los nodos objetivo |
| Error del mercado | Tratar el PHY como IP digital reutilizable ordinario |
| Caso bajista | Synopsys/Cadence responden agresivamente en los nodos de mercado masivo de Samsung |
| Confirmación | Validación de LPDDR6 en 4nm y LPDDR5X en 8nm y adopción por clientes |

### Idea 3 — OpenEdges Square y el CC NoC

| Concepto | Visión |
|---|---|
| Lógica central | Los ASICs de IA multinúcleo pueden necesitar soluciones de NoC con coherencia de caché |
| Palanca de precio | El CC NoC podría ser una capa de IP de mayor valor |
| Palanca de volumen | Adopción por clientes de ASICs de IA y casas de diseño |
| Palanca de costo | El gasto en desarrollo de la plataforma debe controlarse |
| Punto crítico | Lanzamiento comercial del CC NoC y primeros contratos |
| Error del mercado | Ver Square solo como un centro de costos |
| Caso bajista | Los ingresos se retrasan mientras crece la carga de costos |
| Confirmación | Lanzamiento en 2026, primer cliente, economía clara para la matriz |

---

## 10. Posicionamiento: Lista de Seguimiento / Posición Piloto

Por ahora, situaría a OpenEdges en el segmento de **Lista de Seguimiento / Posición Piloto**.

La acción es invertible como pequeña posición exploratoria porque el camino alcista es claro y la capa estratégica de mercado potencial es real. Pero la valoración actual es demasiado elevada para escalar a ciegas. La empresa necesita demostrar que su mapa de ruta tecnológico puede traducirse en contratos repetidos e ingresos reconocidos.

### Condiciones para aumentar la exposición

Consideraría pasar de una posición piloto del 0,3%-0,5% hacia el 0,5%-0,7% si se producen al menos dos de los siguientes eventos:

1. contratos adicionales de licencia LPDDR6/5X;
2. ingresos trimestrales del 2T26 o 3T26 superiores a KRW 7,0B;
3. los costos fijos trimestrales se acercan al rango de KRW 7,0B-8,0B;
4. se divulga tape-out o prueba en silicio de Samsung 4nm LPDDR6;
5. los contratos del canal de casas de diseño se vuelven más visibles;
6. OpenEdges Square muestra control de costos y un camino creíble de lanzamiento del CC NoC;
7. el precio de la acción se mantiene en KRW 20.000 y recupera el rango de KRW 21.500-22.000 con noticias reales.

Solo consideraría una posición superior al 1% tras la confirmación de tres o más de esos hitos.

### Catalizadores

| Catalizador | Momento | Significado |
|---|---|---|
| K-On Device u otro proyecto vinculado a política pública | 2T26-3T26 | La demanda pública de semiconductores de IA se vuelve más concreta |
| Divulgación de licencia LPDDR6/5X | 2026 | Confirma el camino de ingresos superiores a KRW 30B |
| Aceleración de ingresos 2T-3T | 2S26 | Muestra que el reconocimiento de licencias está convergiendo |
| Actividad de clientes en Samsung 4/5/8nm | 2026-2027 | Valida la tesis central del nodo de la fundidora |
| Lanzamiento del CC NoC de Square | Objetivo 2026 | Comprueba si la subsidiaria es una opción o un lastre de costos |

### Señales de invalidación

| Señal de invalidación | Interpretación |
|---|---|
| Sin nuevos contratos de LPDDR6/5X | La tesis del pre-portado se debilita |
| Ingresos del 2T-3T persistentemente por debajo de KRW 5,0B | El camino de ingresos superiores a KRW 30B está deteriorado |
| La pérdida operativa supera KRW 6,0B por trimestre | La estructura de costos sigue siendo demasiado pesada |
| El grupo de clientes relacionados con Samsung Foundry se debilita | La tesis central de la cadena de valor Samsung está dañada |
| Square requiere financiación adicional de la matriz | Aumentan el riesgo de dilución y carga de costos de la subsidiaria |
| El reajuste incrementa la dilución efectiva | Crece la pérdida de valor para el accionista |
| La mezcla de regalías permanece estancada en dígitos medios bajos | La calidad de plataforma de IP sigue sin probarse |

---

## 11. Nota Final

OpenEdges es una buena opción tecnológica. Aún no es una buena empresa generadora de ganancias.

La tesis de inversión más clara no es "el ganador coreano de NPU". Es **IP de PHY y controlador LPDDR5X/LPDDR6 para clientes de ASICs de IA y edge en Samsung 4/5/8nm**. Eso es más específico, pero también más sólido. Identifica el verdadero cuello de botella, el verdadero grupo de clientes y la razón real por la que OpenEdges puede importar a pesar de los gigantes globales de IP.

TSS y la unidad de Japón fortalecen la base central de IP. OpenEdges Square agrega una opción separada de CC NoC y plataforma de IP, pero esa opción solo pertenece en parte a la matriz cotizada y debe monitorearse en términos de disciplina de costos. La financiación mediante CPS de 2026 da a la empresa margen de maniobra, pero también añade riesgo de dilución.

Con una capitalización de mercado superior a KRW 500B y aproximadamente 17x las ventas proyectadas para 2026, la acción ya asume un futuro mejor. La tarea ahora no es admirar la tecnología. La tarea es verificar la cadena de conversión: contratos de LPDDR6/5X, tape-out, prueba en silicio, reconocimiento de ingresos, punto de equilibrio y, finalmente, regalías.

**Mi conclusión no cambia, pero es más precisa: Lista de Seguimiento / Posición Piloto. Escalar solo cuando los números comiencen a confirmar la historia del IP.**

---

## Notas de Fuentes

- IR Book de la empresa: OpenEdges Technology 2026.03 IR Book vía KIND, incluyendo mapa de ruta de producto, número de clientes, historial de licencias, composición de la plantilla y estructura de subsidiarias.
- Comunicado oficial de OpenEdges sobre el lanzamiento de OpenEdges Square: [OpenEdges Technology lanza la subsidiaria OpenEdges Square](https://www.openedges.com/ko/post/news0816).
- Cobertura de The Bell sobre OpenEdges y Square: [Historia de sinergias entre OpenEdges Technology y Square](https://www.thebell.co.kr/front/newsview.asp?key=202311301141250240104442).
- Cobertura de DigitalToday sobre el aumento de capital de OpenEdges Square y el cambio de propiedad: [OpenEdges Technology participa en el aumento de capital de OpenEdges Square](https://www.digitaltoday.co.kr/news/articleView.html?idxno=611992).
- Cobertura de Design-Reuse sobre la comercialización de LPDDR6/5X: [OpenEdges avanza en la comercialización del IP de subsistema de memoria LPDDR6/5X](https://www.design-reuse.com/news/202530336-openedges-advances-commercialization-of-lpddr6-5x-memory-subsystem-ip-targeting-next-generation-ai-and-hpc-markets/).
- Instantánea de mercado utilizada como referencia de valoración: [Página de la acción de OpenEdges Technology en Maeil Business](https://stock.mk.co.kr/price/home/KR7394280002).

*Descargo de responsabilidad: Solo para fines de investigación e información. No constituye asesoramiento de inversión. Los nombres citados son para ilustración analítica; los lectores deben realizar su propia diligencia debida y consultar a asesores autorizados antes de tomar cualquier decisión de inversión.*
