---
title: "Por qué los centros de datos de EE. UU. se están retrasando: el manual de ERCOT y el calendario para Big Tech y los semiconductores"
slug: "us-datacenter-power-delay-ercot-renewables-bess-bigtech-semiconductor-2026-07-28"
date: 2026-07-28T21:45:00+09:00
description: "Un análisis verificado con fuentes sobre los retrasos de centros de datos en EE. UU. en conexión a red, transformadores, turbinas y oposición local; por qué ERCOT redujo el riesgo con 40.3 GW de solar, 22.0 GW de baterías y 5.1 GW de respuesta de demanda; y qué implica el cuello de botella para las acciones de Big Tech, GPU, HBM, memoria y equipos eléctricos."
categories: ["Análisis exclusivo", "Perspectivas de mercado", "Análisis tecnológico"]
tags:
  - "centros de datos de EE. UU."
  - "infraestructura de IA"
  - "red eléctrica"
  - "ERCOT"
  - "BESS"
  - "solar"
  - "Big Tech"
  - "Nvidia"
  - "HBM"
  - "Samsung Electronics"
  - "SK hynix"
  - "equipos eléctricos"
  - "Research OS"
draft: false
---

> Contexto: En la [trilogía de resultados de IA de Big Tech](/es/post/big-tech-ai-earnings-capex-roi-memory-2028-fcf-2026-07-22/), la pregunta crítica para 2028 era si el capex de IA podría convertirse en ingresos y flujo de caja libre. Nuestra [clasificación de beneficiarios de centros de datos coreanos](/es/post/korea-ai-datacenter-beneficiaries-power-cooling-operator-flow-ranking-2026-07-23/) y el [mapa del cuello de botella eléctrico de los centros de datos de IA](/es/post/ai-datacenter-power-bottleneck-korea-value-chain-screen-2026-07-04/) sostuvieron que los proveedores de energía, refrigeración y energía de respaldo monetizan antes que los operadores. Este informe aplica ese marco a Estados Unidos.

## TL;DR

- Los retrasos de los centros de datos en EE. UU. son reales, aunque ningún registro nacional único puede ofrecer una tasa definitiva de cancelación. Allianz Research resumió que cerca de 12 GW de capacidad estadounidense prevista para 2026 podría retrasarse o cancelarse, con solo alrededor de 5 GW en construcción activa. NERC confirmó por separado que varias regiones redujeron sus previsiones de grandes cargas porque las interconexiones y terminaciones fueron más lentas de lo esperado.[^allianz][^nerc]
- El cuello de botella tiene cuatro capas: <strong>interconexión a la red, transformadores e interruptores, equipos de generación, y permisos locales y asignación de costes</strong>. A finales de 2025, 1,312 GW de generación y 749 GW de almacenamiento esperaban en las colas de interconexión de EE. UU. Los plazos de entrega de transformadores elevadores de generador superaban las 160 semanas a comienzos de 2026.[^lbl][^reuters-transformer]
- La frase «más de la mitad de los estados de EE. UU. están bajo advertencias de escasez» exagera la evaluación oficial. NERC encontró recursos adecuados en todas las áreas bajo condiciones normales de pico estival, aunque identificó riesgos elevados bajo condiciones extremas en regiones seleccionadas.[^nerc]
- ERCOT es una prueba contundente de la tesis solar más almacenamiento. NERC enumera 40.3 GW de solar y 22.0 GW de almacenamiento en baterías en ERCOT, con contribuciones esperadas al pico de 29.7 GW y 20.7 GW. La probabilidad de una Alerta de Emergencia Energética en la hora de mayor riesgo cayó de 3.1% a 0.43%.[^nerc]
- Pero ERCOT no es una historia de solo solar y baterías. Su resultado también refleja 5.1 GW de respuesta de demanda, cargas computacionales reducibles, reglas de mercado más rápidas y una base existente de generación a gas, nuclear y eólica.
- Solar más BESS es la opción de suministro incremental más rápida para los próximos tres años, no una solución completa 24/7. La arquitectura práctica es <strong>solar+BESS, PPAs existentes de nuclear o gas, motores de gas o celdas de combustible detrás del medidor, y cargas computacionales flexibles</strong>.
- Para Big Tech, los retrasos limitan el crecimiento a corto plazo, pero aumentan el valor de escasez de la capacidad ya energizada. Para los semiconductores, crean tanto un riesgo de calendario de envíos a corto plazo como una posible extensión del ciclo de demanda de 2027-2028.

<div class="thesis-callout">
  <div class="thesis-callout__label">Conclusión clave</div>
  <div class="thesis-callout__body">
    El cuello de botella de IA se ha desplazado de los chips a la energía. La lección de ERCOT no es «solo renovables», sino una cartera de incorporaciones rápidas de recursos, baterías, interconexión flexible, respuesta de demanda y generación firme. Los efectos sobre las acciones llegan en tres relojes distintos: un límite de crecimiento a corto plazo para Big Tech, instalaciones de semiconductores diferidas hacia 2027-2028 y pedidos directos para proveedores de equipos eléctricos y almacenamiento.
  </div>
</div>

## 0. Primero, fijemos las definiciones

La «capacidad» de un centro de datos puede referirse a la carga de TI, la potencia total de la instalación o el tamaño final anunciado del campus. Una «cola» de interconexión puede referirse a proyectos de generación o a grandes cargas. Mezclarlos genera cifras impresionantes, pero engañosas.

| Afirmación habitual | Verificación de evidencia | Supuesto de trabajo |
|---|---|---|
| La capacidad actual de centros de datos en EE. UU. es de 50 GW | Las estimaciones varían según el alcance | Wood Mackenzie estima aproximadamente 24 GW actualmente y 110 GW para 2030.[^reuters-transformer] |
| 30-50% de los proyectos de 2026 se retrasan | Estimación del sector, no un censo oficial | Use la dirección, no una falsa estimación puntual. Allianz indica 12 GW previstos frente a alrededor de 5 GW en construcción.[^allianz] |
| La mitad de los estados de EE. UU. enfrenta advertencias de escasez | Más contundente que el lenguaje de NERC | Todas las áreas tienen suficientes recursos en condiciones normales; regiones seleccionadas enfrentan riesgo elevado de condiciones meteorológicas extremas.[^nerc] |
| ERCOT ya ha superado los 90 GW | Más de 92 GW es una previsión | La previsión de verano de ERCOT supera 92 GW; las cifras de planificación de NERC ajustadas por respuesta de demanda son menores.[^kera][^nerc] |
| ERCOT tiene 35 GW solar y 12 GW BESS | Direccionalmente correcto, pero desactualizado | NERC enumera 40.3 GW solar y 22.0 GW BESS para 2026.[^nerc] |
| La cola estadounidense es de 2.6 TW | Depende de la fecha y el alcance | Las colas activas de generación y almacenamiento a finales de 2025 totalizaban 2.061 TW. No es la cola de carga de centros de datos en sí.[^lbl] |

## 1. ¿Qué tan grande es el retraso?

No existe un registro integral de proyectos de centros de datos en EE. UU. Un solo campus puede tener una capacidad final anunciada, una capacidad menor para su primer edificio y múltiples fechas escalonadas de energización. «Retrasado», «cancelado», «pausado» y «reserva de terreno sin energía» no son lo mismo.

Aun así, tres señales independientes coinciden:

1. Allianz Research afirma que cerca de 12 GW de capacidad estadounidense prevista para 2026 puede retrasarse o cancelarse, con solo unos 5 GW en construcción activa.[^allianz]
2. NERC afirma que varias áreas de evaluación revisaron a la baja sus previsiones de grandes cargas porque las interconexiones y terminaciones fueron más lentas de lo esperado previamente.[^nerc]
3. Data Center Watch, citado por informes de prensa, contabilizó 75 proyectos valorados en aproximadamente $130 billion bloqueados o retrasados en el primer trimestre de 2026.[^dcwatch]

La conclusión defendible no es que exactamente la mitad vaya a desaparecer. Es que la capacidad de IA anunciada avanza más rápido que la entrega de energía y la construcción, desplazando una parte significativa de la oferta de 2026 hacia 2027 y más allá.

## 2. El cuello de botella de cuatro capas

| Capa | Medida verificada | Por qué importa |
|---|---:|---|
| Interconexión de generación y almacenamiento | 2,061 GW activos a finales de 2025; tiempo mediano hasta operación superior a cinco años para las terminaciones de 2025 | La nueva carga no puede escalar sin suministro y transmisión. |
| Interconexión de grandes cargas | 36-48 meses en zonas de crecimiento de centros de datos de PJM | Una estructura terminada no puede monetizar sin una fecha de energización. |
| Transformadores e interruptores | Transformadores elevadores por encima de 160 semanas; interruptores de alta tensión alrededor de 125 semanas | Un componente faltante puede detener una subestación completa. |
| Permisos, tarifas y oposición local | 75 proyectos y $130 billion retrasados o bloqueados en Q1 2026 | El agua, el ruido, el terreno y el traslado de costes pueden detener la construcción. |

La cola de generación y almacenamiento contiene aproximadamente 8,200 proyectos. Solo el 13% de la capacidad que solicitó conexión entre 2000 y 2020 había alcanzado operación comercial a finales de 2025.[^lbl] Por tanto, el volumen de la cola no equivale al suministro futuro.

Los equipos son una restricción física más inmediata. Reuters informó que los plazos de entrega de transformadores elevadores de generador superaron las 160 semanas en el primer trimestre de 2026 y los interruptores de alta tensión alcanzaron 125 semanas. Las empresas de servicios públicos ahora encargan equipos con años de antelación y a veces pagan por adelantado por plazas de fabricación.[^reuters-transformer]

Las turbinas de gas tampoco son una alternativa instantánea. Mitsubishi Power dijo que los pedidos se extienden hasta 2030 y los plazos de instalación han pasado a cinco años o más.[^gas-turbine]

## 3. El cuello de botella se ha movido de los racks a las subestaciones

La cadena de monetización es:

```text
Demanda de IA y contrato de cliente
→ terreno y acuerdo de suministro eléctrico
→ aprobación de generación, transmisión y subestación
→ entrega de transformador, aparamenta e interruptor
→ finalización del edificio, refrigeración y energía de respaldo
→ instalación de GPU, red y memoria
→ puesta en marcha
→ activación de cargas de trabajo de clientes
→ reconocimiento de ingresos de nube e IA
```

Las órdenes de FERC de junio de 2026 a seis operadores regionales de red confirman que la integración de grandes cargas se ha convertido en una cuestión de política nacional.[^ferc]

Pero «no hay suficiente generación» es solo un modo de fallo. Una región puede tener centrales eléctricas, pero no transmisión. Puede tener transmisión, pero no transformadores. Puede tener equipos, pero no un acuerdo sobre quién paga. Y una carga rígida 24/7 requiere más infraestructura que una carga que puede desplazar trabajos de entrenamiento entre momentos o ubicaciones.

## 4. Qué hizo ERCOT de forma diferente

### 4-1. La solar y las baterías realizaron una contribución medible

La evaluación de 2026 de NERC enumera 40.3 GW de solar y 22.0 GW de almacenamiento en baterías en ERCOT. Las contribuciones esperadas al pico son 29.7 GW y 20.7 GW.

| Recurso de ERCOT | Capacidad nominal | Contribución esperada al pico | Tasa de contribución |
|---|---:|---:|---:|
| Eólica | 40.6 GW | 9.45 GW | 23% |
| Solar | 40.3 GW | 29.68 GW | 74% |
| BESS | 22.0 GW | 20.69 GW | 94% |

Texas estableció un récord de producción solar de 29.3 GW y un récord de descarga de baterías de 7.2 GW en el verano de 2025. Con 8.78 GW de BESS añadidos durante 2025 y otros 2.68 GW hasta marzo de 2026, la probabilidad modelada de una Alerta de Emergencia Energética en la hora de mayor riesgo cayó de 3.1% a 0.43%.[^nerc]

Las baterías no alimentan todo el estado durante días. Desplazan la solar del mediodía hacia la tarde, responden a desequilibrios súbitos y estabilizan la frecuencia.

### 4-2. El suministro fue solo la mitad de la respuesta

ERCOT dispone de 5.1 GW de respuesta de demanda para el verano de 2026, un aumento de 54.9% interanual. NERC afirma que más cargas computacionales pueden reducirse durante emergencias, disminuyendo su previsión de demanda interna neta en 3.7 GW.[^nerc]

```text
La solar atiende la demanda diurna
→ las baterías cubren la rampa vespertina
→ gas, nuclear y eólica respaldan el suministro firme y nocturno
→ las grandes cargas computacionales se reducen durante el estrés
→ señales rápidas de mercado y reglas de interconexión atraen recursos
```

El menor riesgo de ERCOT refleja un aumento de 12% en los recursos previstos, más BESS, más respuesta de demanda y grandes cargas flexibles. No es una historia de una sola tecnología.

### 4-3. Debilidades restantes

- La hora de mayor riesgo es las 9 p.m., después de que la producción solar disminuye.
- El extremo oeste de Texas sigue enfrentando restricciones de transmisión.
- La desconexión simultánea de grandes cargas electrónicas puede desestabilizar la frecuencia y el voltaje.
- La cifra de 92 GW es una previsión de verano, no un récord realizado.
- La capacidad de potencia de baterías en GW dice poco sobre sobrevivir eventos de varios días con poco viento o poca solar sin datos de duración energética en GWh.

## 5. ¿Es solar más BESS la solución más rápida?

Para potencia incremental durante los próximos tres años, sí. Para suministro completo 24/7, no.

| Opción | Velocidad hasta la primera energía | Firmeza 24/7 | Principal restricción | Mejor función |
|---|---|---|---|---|
| Solar+BESS | Rápida | Media | Terreno, transformadores, duración, noche | Potencia incremental rápida y apoyo al pico |
| Motores de gas o pequeñas turbinas in situ | Media | Alta | Gasoducto, permisos de aire, coste del combustible | Energía puente y elusión de la cola |
| Celdas de combustible+BESS | Media | Alta | Suministro de combustible, coste de equipos, servicio | Suministro modular detrás del medidor |
| PPA existente de nuclear o gas | Rápida a media | Alta | Transmisión y estructura contractual | Suministro firme |
| Nuevo ciclo combinado de gas | Lenta | Alta | Plazo de turbinas, gasoductos, permisos | Gran suministro a largo plazo |
| Nueva transmisión | Muy lenta | Alta | Permisos, terreno, asignación de costes | Solución estructural |
| SMR o nueva nuclear | Muy lenta | Alta | Licencias, coste de construcción, calendario | Energía firme de la década de 2030 |
| Carga computacional flexible | La más rápida | No es una fuente de suministro | SLA y software | Conexión más rápida con la misma red |

S&P Global modeló un centro de datos de 627 MW y encontró que un diseño solar más almacenamiento costaba más del doble que una planta de ciclo combinado, mientras seguía sin garantizar electricidad durante períodos de varios días con baja producción solar.[^spp-solar-gas] Eso no invalida solar+BESS. Define su papel como capacidad incremental rápida y de pico, en lugar de una solución anual independiente.

La arquitectura práctica es escalonada:

1. <strong>Energización inicial:</strong> solar, BESS, motores in situ o celdas de combustible, servicio parcial de red y cargas de trabajo por lotes flexibles.
2. <strong>Estabilización:</strong> PPAs a largo plazo con nuclear, gas o hidro existentes; mejoras de subestaciones y transmisión; almacenamiento de mayor duración.
3. <strong>Suministro estructural:</strong> nueva generación de ciclo combinado, transmisión, reinicios nucleares, geotermia, almacenamiento de larga duración y, finalmente, nuclear avanzada.

## 6. Las reglas y el software importan tanto como los equipos

Las órdenes de junio de FERC piden a PJM, MISO, SPP, CAISO, ISO-NE y NYISO justificar o reformar las tarifas para grandes cargas. Las opciones incluyen generación ubicada conjuntamente, servicio de transmisión flexible, generación detrás del medidor y servicio temporal de generadores cercanos.[^ferc]

El activo emergente es la computación reducible.

| Carga de trabajo | Flexibilidad eléctrica | Motivo |
|---|---:|---|
| Inferencia en tiempo real | Baja | Los costes de latencia e interrupciones son altos. |
| Nube empresarial | Baja a media | Los SLA de clientes deben protegerse. |
| Entrenamiento entre puntos de control | Media | Pueden ser posibles pausas y reinicios cortos. |
| Entrenamiento por lotes y preprocesamiento | Alta | El trabajo puede desplazarse entre momentos y regiones. |
| Minería de criptomonedas | Muy alta | La reducción es relativamente sencilla. |

No toda la demanda de IA es flexible. Pero si una parte de un campus puede reducirse, la red ya no tiene que construir cada mejora para un pico coincidente de peor caso totalmente rígido antes de la primera energización.

## 7. Impacto sobre las acciones de Big Tech

### 7-1. Canal negativo: la demanda contratada se convierte más lentamente en ingresos

```text
Retraso en la entrega de energía
→ retraso en la activación del centro de datos
→ la capacidad de servicio de GPU sigue limitada
→ la cartera de pedidos y RPO se convierten más lentamente
→ el crecimiento de nube a corto plazo queda limitado
→ la depreciación puede comenzar antes de que la utilización sea óptima
```

Si se pagan terrenos, edificios y depósitos de equipos antes de que llegue la energía, el flujo de caja libre queda bajo presión. Por tanto, la cuestión del FCF de 2028 no se limita al capex. Es capacidad energizada y utilización.

### 7-2. Canal positivo: valor de escasez de la capacidad activa

Cuando la oferta crece más lentamente que la demanda, la capacidad de GPU ya energizada se vuelve más valiosa:

- Los descuentos pueden disminuir.
- Los compromisos a largo plazo y los pagos anticipados pueden aumentar.
- La alta utilización absorbe la depreciación.
- Los operadores con energía asegurada y diversificación geográfica ganan cuota.

Los retrasos de centros de datos no son igualmente negativos para todos los hyperscalers. Perjudican a las empresas con grandes planes sin energía, mientras fortalecen los precios para las empresas con capacidad energizada.

### 7-3. El nuevo marcador de Big Tech

| Métrica | Señal positiva | Señal negativa |
|---|---|---|
| Potencia energizada | MW/GW específicos y fechas | Solo tamaño final del campus |
| Abastecimiento eléctrico | PPAs multirregionales, energía in situ, contratos de red | Una sola empresa eléctrica y una fecha lejana |
| Contratos de clientes | Compromisos a largo plazo, pagos anticipados, uso mínimo | Interés no vinculante |
| Fases de capex | Inversión alineada con energización | Edificios y chips esperando energía |
| Flexibilidad | Las cargas se desplazan entre momentos y regiones | Cada carga se trata como demanda rígida 24/7 |
| Flujo de caja | Los ingresos y la utilización superan la depreciación | La depreciación y los intereses suben primero |

La próxima pregunta en la llamada de resultados debería ser: ¿cuántos gigavatios pueden encenderse, cuándo y cuántos ingresos de clientes están asociados?

## 8. Impacto sobre las acciones de semiconductores

### 8-1. Riesgo a corto plazo: una brecha entre pedido e instalación

Los hyperscalers pueden aceptar GPU y HBM antes de que la energía esté lista, creando inventario de clientes, o retrasar las entregas para alinearlas con la energización, creando brechas trimestrales de envíos.

Las señales de advertencia incluyen:

- Aumento de días de inventario de clientes de GPU y servidores
- Menores pagos anticipados y calendarios de entrega más largos
- Más referencias a «esperando energía»
- Envíos de ODM de servidores creciendo más rápido que la capacidad de nube activa
- Contratos de HBM que se mantienen intactos, pero con fechas trimestrales de entrega desplazadas

La «demanda diferida» no es automáticamente alcista.

### 8-2. Oportunidad a medio plazo: una cola de ciclo más larga

Si los proyectos se desplazan en lugar de desaparecer, la curva de demanda puede aplanarse y prolongarse.

```text
La capacidad de centros de datos de 2026 se retrasa
→ las instalaciones de GPU y HBM se trasladan a 2027-2028
→ el crecimiento de envíos de 2026 se modera
→ las instalaciones diferidas se superponen con la demanda de reemplazo y expansión
→ el pico puede ser menor, pero el ciclo dura más
```

Esto requiere tres condiciones:

1. La demanda final de IA no se deteriora.
2. La capacidad de financiación y el crédito de los hyperscalers se mantienen intactos.
3. Las soluciones de energía están en construcción y no meramente anunciadas.

Los retrasos repetidos junto con una monetización de IA más débil convertirían el aplazamiento en cancelación.

### 8-3. El rendimiento por vatio gana valor

| Capa de semiconductores | Efecto de la escasez eléctrica |
|---|---|
| GPU y ASIC de IA | El rendimiento por vatio se vuelve un criterio de compra más relevante. |
| HBM | La menor energía de movimiento de datos y la mayor utilización del acelerador aumentan su valor. |
| DRAM de servidor | El coste total de propiedad, incluida la energía y refrigeración, importa más. |
| SSD empresarial | El almacenamiento de bajo consumo y alto rendimiento reduce el tiempo inactivo de GPU. |
| Redes | Las interconexiones más rápidas obtienen una prima al reducir el tiempo inactivo del clúster. |
| Semiconductores de potencia y sustratos | La distribución y conversión de alta tensión se convierten en partes mayores del valor del sistema. |

Para SK hynix, el canal positivo es la ventaja de rendimiento por vatio de HBM y DRAM de servidor de alto valor. Samsung Electronics combina una potencial recuperación de HBM con una cartera más amplia de DRAM de bajo consumo y SSD empresariales. Pero si los retrasos de energización generan inventario de servidores y clientes, la exposición más amplia a productos básicos también puede aumentar la sensibilidad.

## 9. Evaluación bursátil por grupo

| Grupo | Próximos 0-6 meses | Próximos 1-3 años | Evaluación |
|---|---|---|---|
| Hyperscalers | Los límites de capacidad restringen el crecimiento; la capacidad activa conserva poder de precios | El acceso a energía se convierte en un foso competitivo | Mayor dispersión entre empresas |
| GPU y ASIC de IA | Riesgo de calendario de envíos trimestrales | Rendimiento por vatio y demanda diferida | Positivo a medio plazo, volátil a corto plazo |
| HBM y memoria de servidor | Importan la cadencia de entrega y el inventario de clientes | Posible extensión del ciclo | Positivo condicional |
| Equipos eléctricos | La cartera de pedidos y los precios siguen fuertes | La expansión de capacidad puede generar competencia más adelante | Beneficiario directo; importa la valoración |
| BESS | Demanda de pico y detrás del medidor | Mayor duración y valor del software | Beneficiario estructural |
| Turbinas y motores | Pedidos fuertes, entrega lenta | Restricciones de gasoductos y permisos | Fuerte cartera, ingresos retrasados |
| Nuclear y geotermia | Contribución limitada a corto plazo | Prima de energía firme | Larga duración |

Los equipos eléctricos son el beneficiario directo más claro porque transformadores, interruptores, aparamenta, cables y baterías resuelven las causas del retraso. Pero una larga cartera de pedidos no implica automáticamente una acción barata. La expansión de fabricación, los costes de insumos, los depósitos y la competencia posterior a 2028 también importan.

La exposición de empresas cotizadas coreanas sigue siendo:

- Red y distribución: LS ELECTRIC, HD Hyundai Electric, Hyosung Heavy Industries
- Cables: Iljin Electric, Gaon Cable
- BESS y calidad de energía: LG Energy Solution, Samsung SDI, Vinatech
- Refrigeración: LG Electronics, GST
- Energía firme: Doosan Enerbility, SK Gas, GNC Energy

Consulte la [clasificación de beneficiarios del 23 de julio](/es/post/korea-ai-datacenter-beneficiaries-power-cooling-operator-flow-ranking-2026-07-23/) para la selección de acciones basada en precio y flujos. Este informe se centra en la duración del cuello de botella estadounidense.

## 10. Panel mensual

| Indicador | Interpretación positiva | Interpretación negativa |
|---|---|---|
| MW de primera energía para centros de datos | Los planes se convierten en capacidad activa | El tamaño final crece mientras las fechas se retrasan |
| Plazo de grandes transformadores | Persisten el cuello de botella y el poder de precios | Los plazos se desploman con cancelaciones |
| Aprobaciones de grandes cargas de ERCOT y PJM | Entrega de energía más rápida | Los plazos de estudios vuelven a ampliarse |
| Despliegue y duración de BESS | Mejor cobertura del pico vespertino | GW elevados, pero GWh insuficientes |
| Inscripción en respuesta de demanda | Más carga se conecta a la misma red | Las preocupaciones por SLA reducen la participación |
| Utilización de Big Tech y conversión de RPO | La energía y los clientes llegan juntos | El RPO crece, pero la conversión se ralentiza |
| Inventario de clientes de GPU y HBM | La demanda diferida se mantiene saludable | Los chips se acumulan sin energía |
| Crecimiento de nube frente a depreciación | Los ingresos superan la base de costes | La depreciación supera el crecimiento |

## 11. Equipo rojo

El caso constructivo falla si:

1. Los retrasos reflejan una demanda de IA más débil en lugar del calendario eléctrico.
2. Las carteras de pedidos de nube y los pagos anticipados de clientes disminuyen.
3. Se acumula inventario de GPU y HBM y se cancelan los volúmenes contratados.
4. La expansión de fabricación de transformadores y BESS crea un colapso de precios en 2028.
5. La oposición local bloquea simultáneamente la transmisión, la generación in situ y las renovables.

El caso bajista falla si:

1. Las reglas para carga flexible y generación ubicada conjuntamente se estandarizan rápidamente.
2. Los contratos de reducción al estilo ERCOT se extienden a PJM y MISO.
3. Solar híbrida, almacenamiento, motores y celdas de combustible energizan grandes campus en dos años.
4. Los hyperscalers divulgan contratos de clientes a largo plazo junto con fechas firmes de energía.
5. Los contratos de HBM y los pagos anticipados se mantienen intactos pese a calendarios de entrega desplazados.

## 12. Visión final

Los centros de datos de EE. UU. no se retrasan únicamente porque el país carezca de energía. Las instituciones y los equipos necesarios para conectar, transformar, reducir y asignar el coste de la electricidad avanzan más lentamente que la demanda de IA.

Solar más BESS es la respuesta incremental más rápida. ERCOT lo demuestra con 40.3 GW de solar, 22.0 GW de almacenamiento en baterías, 50.4 GW de contribución esperada combinada al pico y una probabilidad modelada de alerta de emergencia de 0.43%. Pero la misma evidencia destaca 5.1 GW de respuesta de demanda y carga computacional reducible.

Las implicaciones bursátiles deben separarse por tiempo:

- <strong>Big Tech, corto plazo:</strong> la entrega de energía limita el crecimiento de nube, mientras la capacidad energizada obtiene valor de escasez.
- <strong>Big Tech, medio plazo:</strong> la energía, la utilización y los contratos de clientes determinan si el flujo de caja libre de 2028 se recupera.
- <strong>Semiconductores, corto plazo:</strong> los ajustes de entrega y el inventario de clientes crean volatilidad.
- <strong>Semiconductores, medio plazo:</strong> si el aplazamiento no se convierte en cancelación, la demanda de GPU y HBM puede extenderse a 2027-2028 y prolongar el ciclo.
- <strong>Beneficiarios directos:</strong> transformadores, interruptores, aparamenta, cables, baterías y generación in situ abordan la causa física del retraso.

La distinción decisiva es entre proyectos con fechas firmes de energía y anuncios sin energía, y entre demanda diferida respaldada por contratos de clientes y demanda que desaparece.

> [Hecho] Las fuentes públicas verifican indicadores de retraso, clasificaciones de riesgo de NERC, recursos de ERCOT, colas de interconexión y plazos de entrega de equipos.  
> [Inferencia] Los argumentos de extensión del ciclo y precios por escasez requieren que se mantengan los contratos de clientes y la demanda final de IA.  
> [Bloqueado] Las fechas de energización a nivel de proyecto, la economía de la energía detrás del medidor y los calendarios exactos de instalación de GPU siguen siendo en gran medida privados.

El trabajo relacionado se recopila en el [centro de Análisis exclusivo](/es/page/exclusive-analysis-hub/) y el [centro de IA HBM](/es/page/korea-semiconductor-hbm-kospi-hub/).

[^allianz]: [Allianz Research, Thinking fast, building slow: AI and the energy supply crunch](https://www.allianz.com/content/dam/onemarketing/azcom/Allianz_com/economic-research/publications/specials/en/2026/may/2026-05-12-ai-energy-AZ.pdf), 12 de mayo de 2026.
[^nerc]: [NERC, 2026 Summer Reliability Assessment](https://www.nerc.com/globalassets/our-work/assessments/nerc_sra_2026.pdf), mayo de 2026.
[^lbl]: [Lawrence Berkeley National Laboratory, Queued Up: 2026 Edition](https://emp.lbl.gov/queues), julio de 2026.
[^reuters-transformer]: [Reuters, US power companies scramble to secure equipment as surging data center demand strains supplies](https://www.investing.com/news/stock-market-news/us-power-companies-scramble-to-secure-equipment-as-surging-data-center-demand-strains-supplies-4783319), 9 de julio de 2026.
[^dcwatch]: [Tom's Hardware report citing Data Center Watch](https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-75-data-center-build-outs-worth-usd130-billion-have-been-successfully-blocked-in-the-first-four-months-of-2026-bipartisan-opposition-mounts-nationwide-over-fears-of-soaring-power-and-water-costs), 13 de junio de 2026.
[^gas-turbine]: [S&P Global, Mitsubishi Power gas turbine orders stretch to 2030](https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/070326-interview-mitsubishi-power-gas-turbine-orders-stretch-to-2030-amid-ai-security-demand), 3 de julio de 2026.
[^kera]: [KERA News, ERCOT predicts record summer energy demand](https://www.keranews.org/energy-environment/2026-06-04/ercot-predicts-record-summer-energy-demand), 4 de junio de 2026.
[^ferc]: [FERC, FERC Launches Aggressive Targeted Action to Speed Large Load Integration](https://www.ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration), 18 de junio de 2026.
[^spp-solar-gas]: [S&P Global Market Intelligence, Data center power: Combined-cycle plant outperforms solar plus battery](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/03/data-center-power-combined-cycle-plant-outperforms-solar-plus-battery), marzo de 2026.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
