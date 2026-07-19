---
title: "Informe semanal de semiconductores: beneficios sólidos, múltiplos más bajos y el giro hacia 2028"
slug: "weekly-semiconductor-deep-dive-strong-earnings-lower-multiple-2028-pivot-2026-07-19"
date: 2026-07-19T15:53:00+09:00
description: "Un análisis semanal que conecta los resultados de TSMC y ASML, los precios contractuales de DRAM y NAND, los acuerdos a largo plazo de HBM, la memoria china, Kimi K3 y la fuerte caída de las acciones coreanas de semiconductores entre el 13 y el 19 de julio de 2026. Los beneficios de 2026-2027 siguen siendo sólidos, pero el mercado ya descuenta la expansión de la oferta en 2028, las mejoras de eficiencia y la rentabilidad de los clientes."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags:
  - "Semiconductores"
  - "Memoria"
  - "HBM"
  - "Samsung Electronics"
  - "SK Hynix"
  - "Micron"
  - "TSMC"
  - "ASML"
  - "CXMT"
  - "Kimi K3"
  - "CAPEX de IA"
  - "Valuación"
  - "2028"
series: ["exclusive-analysis", "ai-hbm-2026"]
valley_cashtags:
  - 삼성전자
  - SK하이닉스
draft: false
---

El 13 de julio, el KOSPI cayó un 9.05% y SK Hynix bajó un 15.37%. Sin embargo, en la misma semana, TSMC informó que sus ingresos del segundo trimestre fueron de $40.2 mil millones y su margen bruto fue del 67.7%, mientras que ASML elevó su perspectiva anual de ingresos a €43-45 mil millones. Los precios de los contratos DRAM y NAND comunes también subieron significativamente. Fue una semana en la que las órdenes físicas y los precios de las acciones se movieron en direcciones opuestas.

Esta divergencia no es un signo de que el boom de los semiconductores haya terminado, sino más bien un indicio de que la pregunta del mercado ha cambiado. Los inversores ya no solo miran cuánto ganarán en 2026 y 2027. Primero calculan cuánta expansión de oferta habrá en 2028, si los clientes podrán soportar precios altos de la memoria y el CAPEX de los data centers, y qué tan rápido las ganancias de inferencia eficiente erosionarán el premio por escasez del HBM.

> Contexto Conectado
> Este post integra [Los Cinco Relojes del Bull y Bear Case de los Semiconductores](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/), [Valor Justo de la Memoria a Través de FCFE y Ganancias Normalizadas](/es/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/), [Samsung Electronics y SK Hynix: Escenarios 2027-2028 Integrados con Valoración Ajustada al Riesgo](/es/post/samsung-sk-hynix-2027-2028-integrated-scenarios-risk-adjusted-valuation-2026-07-13/), y [Modelo de Oferta-Demanda HBM 2030 Revisado (26.7 EB)](/es/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/) en un análisis semanal actualizado con datos nuevos del tercer semana de julio. Los posts relacionados están disponibles en el [Hub AI HBM](/es/page/korea-semiconductor-hbm-kospi-hub/) y el [Hub de Análisis Exclusivo](/es/page/exclusive-analysis-hub/).

## TL;DR

* Los datos oficiales confirmados del 13 al 19 de julio no respaldan la afirmación de que la demanda de semiconductores para IA haya alcanzado su punto máximo. Los resultados y las guías de TSMC y ASML, los precios de contrato DRAM y NAND, así como la demanda de memoria para servidores reafirman la tesis de ganancias fuertes para 2026-2027.
* Los mismos datos también amplifican el riesgo de expansión de oferta en 2028. Las planificaciones de expansión de capacidad de ASML y los altos niveles de CAPEX de TSMC son evidencias de órdenes actuales — y simultáneamente reservas de futura oferta y depreciación.
* Los acuerdos a largo plazo para HBM pueden elevar el piso en volumen y ganancias, pero podrían ralentizar la velocidad con que los picos de precios spot se traducen en ASPs promedios. La estabilidad del volumen y un límite al alza de precios coexisten.
* China juega tres roles simultáneamente: destino final de demanda, competidor en memoria comunes, y mercado que podría ser decuplado políticamente. Su mayor impacto es sobre los techo de precios de DRAM y NAND comunes para 2028 y la disciplina global de oferta, no sobre el reemplazo a corto plazo de HBM.
* Los aumentos en eficiencia de modelos abiertos como Kimi K3 no eliminan simplemente la demanda de semiconductores. Pueden desplazar el valor de algunos HBM hacia DRAM para servidores, eSSD, redes y potencia. La pregunta clave no es si el costo por tarea disminuye, sino cuánto se expandirá la carga total de trabajo y qué proporción será implementada en infraestructura autoconstruida.
* Las probabilidades del escenario base actual: Escasez Extendida 25%, Ganancias Fuertes / Multiples Comprimidos 40%, Normalización de Eficiencia y Oferta 25%, Desajuste Financiero / Demanda 10%. El camino más probable es uno donde las ganancias fuertes en 2026-2027 y la descontación de duración para 2028 coexisten.

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Declaración Clave de la Semana</div>
  <div class="thesis-callout__body">
    La evidencia física que respalda el ciclo supercíclico de la memoria ha pasado su primera prueba de estrés a gran escala. Sin embargo, los precios de las acciones han comenzado a preguntar no sobre la magnitud de la escasez sino sobre cuánto tiempo durarán las ganancias excedentes. 2026-2027 es el período para la entrega de ganancias; 2028 es el período que simultáneamente prueba la oferta, la eficiencia y la rentabilidad del cliente.
  </div>
</div>

---

## 1. Alcance y Reglas de Evidencia

El análisis cubre los días del 13 al 19 de julio de 2026. Se categorizaron los materiales de relaciones con inversores (IR) de las empresas, informes de presentaciones gubernamentales y legislativas, datos de la industria, estimaciones de corredores y figuras de oferta-demanda del mercado extraídas de dos documentos de análisis semanales. Donde múltiples posts citaban el mismo origen subyacente, no se incrementó el conteo de confirmaciones.

| Calificación | Fuente | Usada en este informe |
|---|---|---|
| A | Informes IR de la empresa, presentaciones gubernamentales / legislativas / regulatorias, revelaciones del SEC | Basado para hechos y planes oficiales |
| B | Investigación de la industria como TrendForce, informes primarios de corredores | Evidencia de apoyo para precios, participación en el mercado y estimaciones de la empresa |
| C | Resúmenes de verificaciones de canales, reportes cruzados | Usado solo para confirmación directiva; no usado como señales de inversión independientes |
| D | Redes sociales, imágenes resumidas que circulan | Usadas solo para identificar preguntas que requieren verificación adicional |

Las órdenes de TSMC, ASML y fabricantes de memoria pueden reflejar múltiples veces el mismo plan de CAPEX de hyperscalers. Los planes oficiales indican la intención de demanda pero no garantizan la utilización real o el flujo de efectivo. Las caídas drásticas en los precios de las acciones no se atribuyeron únicamente a dinámicas de oferta-demanda técnicas. Desajustes de flujo pueden amplificar las caídas, pero no pueden eliminar una revaluación fundamental del período de duración de ganancias.

## 2. Mapa de los Desarrollos de la Semana

| Fecha | Desarrollamientos Confirmados | Preguntas que el Mercado Comenzó a Hacer | Evaluación Actual |
|---|---|---|---|
| 13 de julio | Modelo de demanda HBM 2030 revalidado en 26.7 EB; estimación del segundo trimestre de SK Hynix ajustada; fuerte caída en el KOSPI | ¿Es una escasez a largo plazo o una extrapolación excesiva? | La escasez para 2027 tiene un fuerte respaldo; la magnitud de la escasez para 2030 carece de convicción |
| 14 de julio | Estimaciones ajustadas de SK Hynix reflejan acuerdos a largo plazo de HBM; IBM y Ericsson señalan el costo de memoria como carga; informes sobre pruebas de Apple con chips CXMT | ¿Son los acuerdos a largo plazo un piso para ganancias o un techo de precios? | La visibilidad del volumen es alta, pero las restricciones en el alza de ASPs y la carga de costos para los clientes emergen junto |
| 15 de julio | Resultados financieros del segundo trimestre de ASML y plan de expansión de capacidad para 2027-2028 | ¿Ordenes fuertes o el inicio de una respuesta de oferta? | Ambas son correctas — reafirman simultáneamente la demanda actual y amplifican el riesgo de oferta en 2028 |
| 16 de julio | Resultados financieros del segundo trimestre y guía para el tercer trimestre de TSMC; carta del Congreso de los Estados Unidos solicitando restricciones en la compra de memoria china | La demanda de IA es fuerte — ¿por qué las acciones de la memoria son débiles? | El debate se centra en la atribución de ganancias, la oferta y el costo del capital — no en una colapso de la demanda |
| 17 de julio | Lanzamiento de Kimi K3; eficiencia abierta y ganancias de API reprecionadas | ¿Reduce la eficiencia la demanda de semiconductores? | El costo por tarea disminuye, pero el uso agregado y las implementaciones en infraestructura autoconstruida pueden expandirse |
| 18 de julio | Análisis del costo de API de IA; revisión de exposición china de los tríos de memoria | ¿China es un cliente o una competencia? | Ambos roles simultáneamente; impacta más el valor normalizado para 2028 que la EPS para 2026 |
| 19 de julio | Verificaciones de canales circulando sobre fuertes órdenes de DRAM para servidores y HBM4 | ¿El descenso en las acciones incorporó un colapso de ganancias en el tercer trimestre? | La probabilidad parece menor, pero la fuente primaria no está confirmada — mantenido en grado C |

La mayor transformación en esta tabla no es la dirección individual de los eventos, sino el horizonte temporal. Hasta principios de julio, el debate se centraba en si las ganancias del segundo semestre de 2026 superarían las expectativas. Ahora se ha desplazado a si las ganancias para 2028 representan un nivel normalizado de ganancias y cuánto tiempo pueden mantenerse los precios elevados y margenes.

## 3. La Evidencia Se Afirmó Esta Semana

### 3.1 TSMC y ASML Mostraron que las Ordenes de IA se Han Traducido en Actividad Real

Los resultados del segundo trimestre de TSMC demuestran que la demanda de IA ha avanzado más allá de la etapa de planificación.

| Item | Perspectivas Financieras de TSMC para el Segundo y Tercer Trimestres de 2026 |
|---|---:|
| Ingresos del segundo trimestre | $40.2 mil millones |
| Margen bruto del segundo trimestre | 67.7% |
| Margen operativo del segundo trimestre | 60.3% |
| Guía de ingresos para el tercer trimestre | $44.6-45.8 mil millones |
| Guía de margen bruto para el tercer trimestre | 65-67% |

Los altos márgenes brutos y la guía de crecimiento para el próximo trimestre indican que la calidad de las órdenes para nodos de proceso avanzado y empaquetado avanzado permanece intacta. [Resultados Oficiales del Segundo Trimestre 2026 de TSMC](https://investor.tsmc.com/english/quarterly-results/2026/q2)

ASML confirmó la misma dirección. Se informaron ingresos de €9.326 mil millones y un beneficio neto de €2.918 mil millones para el segundo trimestre, y se estableció una perspectiva anual de ingresos de €43-45 mil millones. El mapa de capacidad revela la línea temporal en la que las órdenes actuales se traducen en futura oferta.

| Equipo | Capacidad 2026 | Plan para 2027 | Bajo Revisión para 2028 |
|---|---:|---:|---:|
| EUV de baja NA | ~65 unidades | ~30% expansión | Adicional ~30% expansión bajo revisión |
| DUV inmersivo | ~130 unidades | ~30% expansión | Adicional ~30% expansión bajo revisión |

ASML afirmó que la inversión en IA está impulsando la demanda de lógica y memoria avanzada, y que las compromisos de capacidad del cliente se están convirtiendo en visibilidad a largo plazo. Estos números debilitan el fuerte caso alcista de que todas las órdenes de IA consisten en reservas duplicadas. [Resultados Oficiales del Segundo Trimestre 2026 de ASML](https://www.asml.com/en/news/press-releases/2026/q2-2026-financial-results)

### 3.2 Los Precios de la Memoria Se Mantienen Elevados

TrendForce proyectó que los precios de contrato DRAM comunes para el segundo trimestre de 2026 subirán un 58-63% intertrimestralmente, y los precios de NAND subirán un 70-75%. La proyección de crecimiento de precios de DRAM para servidores en el tercer trimestre fue revisada a un 13-18%, pero la trayectoria ascendente se mantiene. [Proyecciones del Segundo Trimestre para DRAM/NAND](https://www.trendforce.com/presscenter/news/20260331-12995.html), [Proyecciones del Tercer Trimestre para DRAM de Servidores](https://www.trendforce.com/presscenter/news/20260709-13140.html)

Es importante distinguir entre una deceleración en la tasa de aumento de precios y un verdadero descenso de precios. Dado cómo rápidamente subieron los precios en el segundo trimestre, la tasa intertrimestral de crecimiento en el tercer trimestre puede ralentizarse. Sin embargo, si los precios absolutos permanecen elevados, el ingreso operativo de los proveedores puede seguir siendo fuerte. El riesgo que el mercado está calibrando no es una disminución de las ganancias, sino una deceleración en la tasa de crecimiento de las ganancias.

### 3.3 La Escala de HBM Roba Suministro de DRAM Común

El HBM requiere más área de wafer, pila, empaquetado y prueba para producir el mismo número de bits que la memoria común. A medida que los tres fabricantes de memoria aumentan su mix de HBM, las envíos de HBM expanden mientras la efectiva bit supply de DRAM común puede contraerse.

Como resultado, el punto de atasco se amplía en la siguiente secuencia:

```text
GPU / ASIC
-> HBM
-> DRAM para servidores
-> eSSD y NAND
-> Empaquetado / Substrato / Prueba
-> Redes / Potencia / Enfriamiento
```

Los agentes de IA y la inferencia a largo contexto no se basan únicamente en el HBM para los pesos del modelo. También consumen DRAM para servidores y eSSD para caché KV y servicio de datos, y consumen más redes para conectar múltiples aceleradores y modelos de mezcla de expertos esparsos. Esto es por qué los volúmenes agregados de capas de memoria pueden seguir expandiéndose incluso si el precio unitario del HBM se ve bajo presión.

### 3.4 La Escasez para 2027 es una Conclusión Fuerte; la Sobredemanda para 2030 es un Escenario

Comparando la demanda de HBM en 2030 de 26.7 EB contra una oferta de 10.6 EB, se obtiene una demanda de 2.52 veces la oferta. El cálculo es reproducible. El problema no radica en el resultado sino en si las suposiciones subyacentes pueden sostenerse simultáneamente. El modelo base asume un crecimiento de tokens de 24 veces, una expansión del tamaño del modelo de 5 veces, una extensión de la longitud del contexto de 4 veces y una tasa de retención del HBM para caché KV del 70% — todo simultáneamente.

| Cambio en la Suposición | Demanda de HBM en 2030 | vs. Oferta de 10.6 EB |
|---|---:|---:|
| Modelo base | 26.7 EB | 2.52 veces |
| Tamaño del modelo 2× | 18.5 EB | 1.75 veces |
| Eficiencia KV 6× | 22.3 EB | 2.10 veces |
| Retención HBM al 50% | 22.9 EB | 2.16 veces |
| Tokens 12× | 16.2 EB | 1.53 veces |
| Suposiciones alcistas compuestas | 6.5 EB | 0.62 veces |

Reduciendo cualquier variable individual aún deja una escasez, pero si múltiples suposiciones alcistas se sostienen simultáneamente, la sobredemanda es posible. La declaración inversible por lo tanto es: "El mercado probablemente permanecerá apretado hasta 2027." La declaración "La oferta será definitivamente 2.5 veces corta en 2030" no puede ser directamente insertada en un objetivo de precio.
## 4. Risks Strengthened This Week

### 4.1 La Tasa de Crecimiento del Beneficio Operativo Se Ha Volcado Más en la Importancia que el Rendimiento Absoluto del Beneficio

La reducción de la estimación de ingresos operativos de SK Hynix Q2 se originó en ajustes a las suposiciones sobre los precios al por mayor (ASP) y no en una caída en los volúmenes de envío.

| Informe | Estimación del Ingreso Operativo para el 2º Trimestre de 2026 | Ajuste Clave |
|---|---:|---|
| Mirae Asset Securities | De ₩70.7 billones a ₩62.3 billones | ASP DRAM de +40,6% a +32,9%; NAND de +55% a +50% |
| Korea Investment & Securities | ₩60.4 billones | ASP DRAM +28,9%; NAND +50,9% |

Un ingreso operativo en el rango de ₩60 billones es muy grande en términos absolutos. Sin embargo, los precios de las acciones respondieron más al tamaño del ajuste desde las estimaciones previas que al nivel absoluto del beneficio. La caída del 15,37% en SK Hynix el 13 de julio se explica mejor por la combinación de expectativas cambiantes y dinámicas técnicas de oferta y demanda concentradas que por cualquier conclusión de que el ciclo alcista ha terminado.

Esta es la lógica central del análisis semanal. La sola demanda fuerte no eleva los precios de las acciones. La demanda debe superar las expectativas del mercado, y se requiere evidencia de que los beneficios elevados persistirán hasta 2028.

### 4.2 Los Contratos a Largo Plazo Crean Ambos un Piso de Beneficio y un Techo de Precios

Los contratos a largo plazo con HBM proporcionan visibilidad en el volumen, fidelización del cliente, predecibilidad del período de retorno e protección contra la caída de los precios al por menor. Por otro lado, se aplican las siguientes preocupaciones:

* Incluso si los precios al por menor suben, el ASP promedio de una empresa puede aumentar solo gradualmente.
* Las fórmulas de precios, mecanismos de renegociación, compromisos mínimos de compra y términos de cancelación no se divulgan.
* La cumplimiento del cliente con los compromisos mínimos de compra y el riesgo crediticio permanecen con el proveedor.
* Los pagos anticipados y las compromisiones a largo plazo en volumen pueden no fluir al rendimiento contable y al flujo de efectivo operativo de la misma manera.

Interpretar los contratos a largo plazo como un reforzamiento incondicional del poder de precios solo es una mitad de la imagen. Los contratos elevan el piso de beneficios y reducen la volatilidad, pero pueden no capturar todo el alza en caso de que suban los precios al por menor. La revisión de la estimación de ingresos operativos Q2 de SK Hynix fue la primera vez que este agujero apareció en los números reportados. Los detalles se discuten en [SK Hynix Q2 Earnings Cut and Maintained Price Targets](/es/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/).

### 4.3 Las Ordenes de Equipos Son Ambas Demanda Actual y Suministro Futuro

Leer la expansión de capacidad de ASML solo como evidencia alcista a corto plazo omite el dimensionamiento temporal.

```text
Capacidad Low-NA EUV 2027 ≈ 65 unidades × 1.30 = 84,5 unidades
Capacidad DUV inmersión 2027 ≈ 130 unidades × 1.30 = 169 unidades
```

Los fabricantes de equipos reconocen las órdenes como ingresos en 2026-2027 primero. La producción bit real de los fabricantes de memoria puede aumentar a partir del 2028, después de la instalación de equipos, estabilización de rendimiento y agregación de capacidad de empaque. El mismo gasto de capital que inicialmente incrementa los ingresos y el flujo de efectivo operativo de equipos y materiales puede presionar las precios y márgenes de memoria más tarde.

Los indicadores a vigilar para 2028 no son los totales anunciados de inversiones. Son la instalación de equipos, nuevos comienzos de wafers, rampa de rendimiento, flujo de empaque, el aumento en depreciaciones y la producción bit real.

### 4.4 Los Altos Precios de Memoria Pueden Erosionar la Demanda del Cliente

Cuando los precios de memoria suben, los clientes pueden responder de cuatro maneras:

1. Anticipar compras de inventario antes de que los precios suban aún más.
2. Subir los precios de las servidores y productos finales.
3. Reducir el contenido de memoria o descalificar especificaciones.
4. Postergar compras y proyectos.

El primer comportamiento hace que los pedidos a corto plazo parezcan más fuertes, pero simplemente anticipa la demanda futura. Las otras tres representan caminos por los cuales el poder de precios de los proveedores finalmente destruye la demanda del cliente. Los ejemplos de IBM y Ericsson mostraron que las restricciones en la oferta de memoria han comenzado a afectar la asignación presupuestaria y márgenes finales de los clientes. Actualmente estamos en una fase donde el pre-compra y ajustes de especificaciones son visibles antes de grandes cancelaciones de pedidos.

### 4.5 El Bache en el Inversión en IA Se Está Desplazando al Costo del Capital

Incluso si la demanda de IA es real, si los flujos de efectivo de la entidad inversora no pueden mantenerse a la par con el desgaste y los costos de financiamiento, el ritmo de inversión se ralentizará. En adelante, lo siguiente importará más que el monto absoluto de la inversión de hiperscaladores:

* Si las ganancias brutas de IA y nube superan el aumento en el desgaste.
* Si la entrega de potencia de los datos centrales y la utilización de GPU se rigen según el plan.
* Si los retornos de nuevos proyectos, incluyendo costos de financiamiento, superan el costo del capital.
* Si la calidad crediticia y los pagos anticipados de clientes que han firmado contratos a largo plazo con HBM permanecen estables.

La fortaleza en las órdenes en TSMC y ASML no son evidencia de una colapso en la demanda actual. Sin embargo, en las declaraciones de resultados financieros de Big Tech estadounidenses al final de julio, los inversores deben examinar las ganancias brutas de IA, el flujo de efectivo libre y la pendiente de la guía de inversión para 2027 junto — no en lugar de — con los totales de inversión.

## 5. ¿Fue la Caída Brusca del Precio de Acciones un Choque de Oferta-Demanda o una Revaluación Fundamental?

La caída brusca este semana en las acciones de semiconductores coreanas presenta signos de desenganche de deuda, venta programada y una estructura de capitalización de mercado altamente concentrada en pocos nombres de capital grande — todo lo cual amplió la caída. La venta simultánea por parte de inversores extranjeros e institucionales causó movimientos de precios diarios superiores a cualquier cambio en el valor subyacente del negocio.

Sin embargo, concluir que "solo fue un choque de oferta-demanda, así que todo se recuperará" tiene sus propios peligros. Si la fortaleza relativa no recupera incluso después de fuertes resultados financieros y datos de precios, puede indicar que el mercado está bajando sus estimaciones para los beneficios por acción (EPS) normalizados y múltiplos en 2028.

El marco diagnóstico es sencillo.

| Señales apuntando a un choque de oferta-demanda | Señales apuntando a una revaluación fundamental |
|---|---|
| La venta extranjera e institucional se desacelera rápidamente | La venta continúa a pesar de buenas noticias |
| La fortaleza relativa recupera volumen | Los semiconductores siguen subiendo en el mercado general |
| Las revisiones al EPS para 12 meses permanecen positivas | Samsung Electronics, SK Hynix y Micron revisaron simultáneamente sus EPS |
| Los precios de los contratos aumentan y las existencias se estabilizan | Las existencias crecen mientras los precios del contrato disminuyen simultáneamente |
| La CAPEX de Big Tech e la rentabilidad de IA mejoran | Se recortan la CAPEX o las márgenes de rentabilidad de IA deterioran |

Esta distinción es precisamente por qué se deben rastrear juntos los precios y las estimaciones de beneficios. Observar solo dinámicas de oferta-demanda puede dejar pasar riesgos a largo plazo; observar solo resultados puede dejar pasar el adicional de la caída creada por posiciones congestionadas.

## 6. China Es Tres Variables al Mismo Tiempo

### 6.1 China es un Gran Mercado de Demanda

Las cifras de exposición a China en los informes de las empresas usan diferentes definiciones, lo que dificulta las comparaciones directas.

| Empresa | Métrica de Exposición a China | Cautela |
|---|---:|---|
| Samsung Electronics | 30.1% | Basado en el ingreso consolidado independiente — no en la participación en memoria solo |
| SK Hynix | 24.3% del primer trimestre de 2026, 19.7% para todo 2025 | Basado en la ubicación de las ventas |
| Micron | +10.1% de China y Hong Kong en FY25 | Basado en la ubicación de la sede del cliente |

Si el demanda china se contrae, Samsung y SK Hynix están directamente expuestas. La exposición directa de Micron es comparativamente baja, pero no puede escapar del impacto si los precios globales caen. Las cifras de participación en ingresos son insuficientes para evaluar el riesgo de China.

### 6.2 China Es un Competidor de Memoria de Commodity

CXMT ha anunciado la producción en masa de LPDDR5X a 8,533 Mbps y 9,600 Mbps, con su producto de 10,667 Mbps reportado en fase de calificación del cliente. Su participación estimada en los ingresos globales de DRAM para el primer trimestre de 2026 se sitúa aproximadamente en el 8%. Sin embargo, un acuerdo de suministro con Apple, la adopción generalizada en productos globales de gama alta y el rendimiento de HBM aún no han sido confirmados. [Anuncio Oficial de CXMT sobre LPDDR5X](https://www.cxmt.com/en/news/info_19.html)

El peligro a corto plazo se concentra en dos canales en lugar de la desplazamiento de HBM:

1. La localización de DRAM y NAND commodity en teléfonos móviles y PCs chinos.
2. Usar CXMT como una tarjeta de cuarto proveedor en negociaciones de precios con el trío de memoria establecido.

Si el volumen desplazado de China se migra a otros mercados, podría arrastrar los precios del contrato para Samsung, SK Hynix y Micron hacia abajo. Esta contagión de precios puede importar más como un efecto secundario que una disminución directa en los ingresos chinos. Un desglose detallado de la exposición está disponible en [Localización de Memoria China y los Tres Grandes](/es/post/china-memory-localization-exposure-samsung-hynix-micron-2026-07-18/).

### 6.3 China Puede Ser Segmentada por Políticas

El 16 de julio, miembros del Comité Selecto de Congreso sobre China enviaron una carta al Departamento de Comercio solicitando controles más estrictos sobre YMTC, un examen acelerado para la inclusión en la Lista de Entidades de CXMT, restricciones en la compra chino de DRAM y HBM en sistemas de IA, centros de datos, IT federal y infraestructura crítica, y coordinación con Corea del Sur, Japón y la UE. Esta es una demanda política — no un embargo de compras implementado. [Carta Oficial del Comité Selecto de Congreso sobre China](https://chinaselectcommittee.house.gov/media/letters/moolenaar-whitesides-to-secretary-lutnick-hold-firm-on-chinese-memory-chips-ban)

Si se aprueba, el mercado global de memoria podría bifurcarse en las siguientes líneas:

| Mercado | Estructura Posible |
|---|---|
| Estados Unidos y aliados | Cadenas de suministro verificadas, precios más altos, defensa de la participación del mercado por el trío de memoria |
| Mercado doméstico chino | Localización, precios más bajos, riesgo medio plazo de sobreoferta |

Micron se beneficia directamente más que ninguna otra empresa de la política estadounidense. Samsung y SK Hynix llevan tanto la ventaja de ser proveedores de naciones aliadas como la exposición de sus negocios en China. Este factor político es menos un catalizador que eleva los ingresos operativos del HBM para 2026 y más una variable que reduce el descuento de sobreoferta chino incorporado a las valoraciones de 2028.

## 7. Kimi K3 y Eficiencia: Cambio en la Demanda, No Destrucción

Según el anuncio oficial de Kimi, K3 tiene 2,8 trillones de parámetros totales, activa 16 de los 896 expertos por token y soporta una ventana de contexto de un millón de tokens. La arquitectura experta escasa reduce el cálculo por solicitud, pero aún requiere gran memoria y alta ancho de banda para almacenar todos los pesos y rutear la selección del experto. [Anuncio Oficial de Kimi K3](https://www.kimi.com/blog/kimi-k3)

El impacto en semiconductores de las ganancias de eficiencia se entiende mejor a través de la siguiente ecuación:

```text
Demanda total de semiconductores = costo de silicio por tarea × número total de tareas × fracción auto-hospedada
```

* Arquitecturas escasas, caché y cuantización reducen el tiempo GPU y el footprint HBM por tarea.
* Los precios bajos de las API aumentan la utilización de IA y el número de agentes.
* Los modelos de peso abierto pueden aumentar los despliegues de servidores auto-hospedados por parte de empresas e instituciones gubernamentales.
* La jerarquía de memoria cambia algunos trabajos HBM a DRAM del servidor, eSSD y cachés remotas.

Los pedidos actuales y datos de CAPEX sugieren que el crecimiento en volumen supera las ganancias de eficiencia. Sin embargo, a largo plazo, la elasticidad de volumen de DRAM del servidor, eSSD, red y potencia puede ser más favorable que el poder de precios de GPUs premium y HBM. La eficiencia es menos una variable que "reduzca la demanda total de semiconductores" y más una que reconfigure "cual semiconductores capturan los ingresos".

Dos advertencias se aplican aquí. Las tasas de ahorro del caché KV y el rendimiento teórico desde las investigaciones lineales de Kimi no pueden ser aplicadas directamente a K3 en producción. Además, los benchmarks de rendimiento auto-reportados no deben ponderarse igual que la verificación independiente. Los pesos, términos de licencia, resultados de throughput independientes, tokens reales y costo total por tarea requieren confirmación.

## 8. Cinco Relojes — Cuando Se Observan Juntos, las Contradicciones Resuelven

| Reloj | Observación Semanal | Interpretación de la Inversión |
|---|---|---|
| Precios | Aumentos drásticos en los precios DRAM y NAND para el 2º Trimestre; ritmo de ganancias para el 3º Trimestre se desacelera | Los ingresos de 2026 parecen fuertes, pero la tasa de aumento puede disminuir |
| Inversión | TSMC expandiendo inversión; pedidos y capacidad de ASML creciendo | La demanda actual confirmada mientras la respuesta de suministro para 2027-2028 se reserva |
| Construcción | Los desafíos de energía, tierra y empaque persisten | Las inversiones anunciadas se retrasan antes de traducirse en un aumento real de producción |
| Monetización | Uso de IA subiendo; costos del cliente y cargas financieras también aumentando | Se requiere una vigilancia cuidadosa de las ganancias brutas de IA y el flujo de efectivo libre junto con los ingresos |
| Precio de Acción | Reacción lenta a buenas noticias; choque de oferta-demanda concentrado en Corea | El mercado descuenta la duración y la posición más que los beneficios actuales |

Los relojes de precios e inversión están corriendo rápido, mientras que los relojes de construcción y monetización se retrasan. El reloj de precio de acciones es la reflección futura de si esa brecha se estrecha o se amplía por delante. Por eso fuertes resultados y una guía de CAPEX elevada pueden provocar ventas el mismo día.

La "coexistencia de 55% de fuerza industrial / debilidad en la valoración" mencionada anteriormente y "P2 a 40%" abajo no son dos lecturas diferentes de la misma tabla. El 55% era una categoría general en la que los múltiplos permanecen comprimidos incluso mientras el sector se mantiene fuerte. La distribución más granulada aquí divide esa categoría aún más en las fases tempranas de P2 y P3. Debido a que los datos nuevos de TSMC y ASML confirmaron la demanda actual mientras simultáneamente expandían la respuesta implícita de suministro, una porción de la probabilidad de normalización del escaseo a largo plazo se ha movido hacia la normalización del suministro.
## 9. Actualización del Escenario

Las probabilidades a continuación son valores de juicio que reflejan la información confirmada hasta el 19 de julio — no las tasas base históricas.

| Escenario | Probabilidad | Condiciones para la Valididad | Comportamiento del Mercado Esperado |
|---|---:|---|---|
| P1. Sustanciosa Scasez | 25% | El uso de IA, CAPEX y tasas de utilización continúan superar la oferta y los avances en eficiencia; el precio y las órdenes de HBM4 se mantienen | Las empresas de memoria con alto beta como SK Hynix y Micron, junto con el empaque y el equipo, sobresalen |
| P2. Ganancias Fuertes, Compresión de Multiples | 40% | Los beneficios permanecen fuertes en 2026-2027 pero persisten las preocupaciones sobre la oferta para 2028 y la rentabilidad del cliente | Negociación dentro de un rango y volatilidad elevada a pesar del crecimiento de los beneficios; Samsung Electronics mantiene una ventaja relativa |
| P3. Normalización de Eficiencia y Suministro | 25% | La expansión de capacidad para 2027-2028, la oferta de commodities chinas, la resistencia del cliente a los precios y el descenso de los costos de IA convergen | El premio por escasez de HBM se reduce; las órdenes de equipo y materiales alcanzan su pico antes que la memoria en sí |
| P4. Desconexión Financiera o de Demanda | 10% | Corte del CAPEX de las grandes tecnológicas, un evento crediticio, inventarios crecientes y descensos simultáneos en precios de contrato y EPS | Declive sectorial en semiconductores; la diversificación en efectivo y no semiconductoras se vuelve más importante |

La distribución detallada anterior era del 35% / 40% / 15% / 10%. Esta revisión transfiere 10 puntos porcentuales desde P1 a P3. Los datos de pedidos de TSMC y ASML no aumentaron la probabilidad de P4. Por el contrario, la expansión de capacidad del equipo y el costo de precios para los clientes han incrementado la probabilidad de normalización de eficiencia y suministro en comparación con la escasez prolongada.

## 10. Roles por Acciones y Cadena de Valor

### Samsung Electronics: Core con Ajuste al Riesgo

Samsung absorbe el aumento del precio de DRAM y NAND commodity a lo largo de una amplia base de participación del mercado, mientras mantiene la opción de valor para recuperarse en HBM y recuperar su negocio de foundry. También posee características defensivas relativas si los modelos abiertos y las inferencias de bajo costo se propagan, desplazando parte del trabajo HBM hacia memoria commodity.

Los riesgos clave incluyen la exposición a China y memoria commodity, la incertidumbre alrededor de la calificación de clientes para HBM4, y el alto costo capitalario de las operaciones de foundry. Samsung ofrece características defensivas más robustas que SK Hynix en P2 y P3, pero la diversificación no implica rentabilidad si la recuperación en HBM no ha sido validada en los beneficios.

### SK Hynix: Beta Pura sobre Escasez Sustanciosa

SK Hynix posee el mayor mercado de participación para HBM, relaciones de co-desarrollo con clientes y acuerdos de suministro a largo plazo que le otorgan la mayor potencial de ganancias bajo P1. En contraste, también lleva el riesgo más alto de compresión de beneficios y múltiplos si la expansión de capacidad y los avances en eficiencia se aceleran bajo P3.

Se requiere un juicio adicional para rastrear las calificaciones de clientes para HBM4 y HBM4E, rendimiento, términos de precio promedio incorporados a contratos a largo plazo, flujos de inversores extranjeros e inversiones programadas, y la fortaleza del negocio junto con el margen de seguridad incorporado en los precios. La calidad del negocio y el margen de seguridad incorporada en los precios deben evaluarse por separado.

### Micron: Intersección entre la Política de EE.UU. y la Memoria Pura

Micron es el beneficiario más directo de la fabricación basada en EE.UU., el apoyo a la política y las restricciones sobre la adquisición de memoria china. Ofrece una lectura clara del ciclo de HBM, DRAM y NAND. Sin embargo, su diversificación limitada significa que también está expuesta directamente a cualquier normalización de los precios promedio globales. Incluso con una participación baja en China, Micron no puede evitar el impacto si las cantidades excedentes de memoria china reducen los precios globales.

### SanDisk: Beta Táctica sobre NAND y eSSD

SanDisk está directamente expuesto a las restricciones de suministro de NAND y la demanda de eSSD para servidores AI. Beneficia más si el costo de inferencia bajo y la jerarquización de memoria desplazan volúmenes de almacenamiento adicionales hacia memoria commodity. Al mismo tiempo, NAND muestra una mayor volatilidad de precios que DRAM y tiene un exponencial directo en YMTC, lo que le da un carácter más táctico en comparación con posiciones core.

### TSMC y ASML: Validadores de Demanda y Indicadores Líderes del Futuro Suministro

TSMC demuestra la calidad de la demanda de IA y el alcance profundo del mojón de foundry de vanguardia. ASML es el punto de observación más temprano para las intenciones a largo plazo de expansión de capacidad de los clientes. Los resultados de ambas empresas sirven como evidencia adicional para la tesis de memoria, pero no son indicadores coincidentes simples. El CAPEX alto y el crecimiento en la oferta de equipos señalan no solo la futura demanda de memoria sino también la futura expansión del suministro.

### Empresas Coreanas de Equipo y Materiales: Pedidos Reales y Recurring Revenue sobre Planes Publicados

| Categoría | Nombres Candidatos | Datos para Confirmar | Rol Actual |
|---|---|---|---|
| Consumibles Recurrentes | Hana Materials, Wooldex | Tasas de utilización del cliente, canales OEM, correlación entre ingresos y margen operativo | Grupo de investigación prioritario |
| Equipo de Proceso | KC Tech, Nextin | Pedidos reales, calificación del cliente, backlogs | Grupo de confirmación condicional |
| HBM Back-end | Techwing | Pedidos adicionales de Cube Prober y ingresos de producción | Grupo de confirmación de eventos |
| Construcción de Infraestructura | Hanyang E&E, otros | Ganancias de contratos principales, ratio ordenes-ingresos, márgenes | Grupo de eventos de pedidos en lugar del core |

La secuencia de confirmación para las inversiones es: anuncio de capacidad → pedidos reales → construcción de backlogs → reconocimiento de ingresos → consumibles recurrentes. Los nombres de equipos pueden alcanzar sus beneficios antes que la producción de memoria en sí. En lugar de comprar ampliamente basándose solo en planes de fábrica, el enfoque debe enfocarse en empresas donde los pedidos reales y los márgenes se han confirmado.

## 11. Contrarargumentos: Donde Esta Tesis Podría Estar Incorrecta

### La Evidencia de la Demanda Puede Haber Sido Duplicada

Los pedidos de TSMC, ASML y el trío de memoria pueden provenir todos de los mismos planes de CAPEX de las grandes tecnológicas. Agregar pedidos a múltiples niveles de la cadena de suministro como señales de demanda separadas sobreestima la demanda final real. Los puntos de verificación finales incluyen los tiempos de conexión eléctrica, el uso de GPUs, las envíos de servidores y las margen neta de IA en la nube.

### El Modelo de Demanda para 2030 Puede Subestimar los Avances en Eficiencia

Si cualquiera de — conteo de tokens, tamaño del modelo, longitud del contexto o tasa de retención HBM — disminuye, persiste una escasez. Pero si todos disminuyen simultáneamente, un escenario de sobreoferta para 2030 se vuelve plausible. El caso directo a largo plazo de escasez y la magnitud numérica de esa escasez deben evaluarse por separado.

### El CAPEX Puede Crecer Más Rápido que los Retornos

Los proveedores deben gastar más en nuevas fábricas y empaque incluso cuando los libros de pedidos están llenos. Los clientes deben absorber el desgaste del centro de datos y la tasa de interés. Si el crecimiento de ingresos no se traduce en un aumento del flujo de efectivo libre, altos beneficios pueden atraer múltiplos reducidos.

### La Política China Puede No Ser Implementada

La carta del Comité de Representantes es una señal de política — no una orden ejecutiva o una acción coordinada aliada. Si CXMT entra solo en un conjunto limitado de productos consumidores dentro de China y la aplicación sigue siendo suave, el poder de precios para los incumbentes puede erode antes que cualquier cambio significativo en la participación del mercado.

### Las Revelaciones de Empresas con Modelos Abiertos Pueden No Ser Reproducibles Independientemente

Las especificaciones oficiales de Kimi K3 están confirmadas, pero el rendimiento de tasa de salida, el consumo real de tokens y el costo total de servicio requieren una verificación independiente. En contraste, si los avances en eficiencia llegan más rápido de lo esperado y la elasticidad del uso es menor de lo supuesto, el premio por escasez de HBM podría comprimirse con mayor severidad.

### Todo el Descenso de Precios Puede Haber Sido Atribuido a Liquidación Forzada

La desapalancamiento y la venta programada explican la magnitud del descenso. Pero si los precios no recuperan incluso en presencia de noticias positivas, el mercado puede estar activamente reduciendo sus supuestos de ganancias de 2028 y múltiplos normalizados. Una explicación de oferta-demanda no puede reemplazar la validación de la durabilidad de los beneficios.

## 12. Condiciones Observables que Cambiarían la Tesis

En lugar de un solo artículo o una subida en un día, lo importante es si dos ejes de datos independientes se mueven juntos.

### Condiciones que Incrementan la Probabilidad de Un Resultado Bullish

1. El crecimiento del CAPEX de las grandes tecnológicas y el mejoramiento de los márgenes de IA y nube son confirmados simultáneamente.
2. Las conexiones eléctricas de los centros de datos, las tasas de utilización de GPUs y los envíos de servidores aumentan juntos.
3. Los precios de HBM4, DRAM para servidores y eSSD, junto con la revisión a 12 meses del EPS, continúan siendo ajustados al alza.
4. Samsung Electronics, SK Hynix y Micron se recuperan en noticias positivas y recuperan su fortaleza relativa frente al índice de semiconductores.
5. Las ventas de inversores extranjeros e inversiones programadas deceleran, y surge una tendencia de recuperación acompañada por un aumento en el volumen.

### Condiciones que Incrementan la Probabilidad de Normalización P3

1. La entrega de equipo para 2027-2028 y la nueva capacidad bit se ponen en línea más rápido del planeado.
2. Los rendimientos HBM y la productividad de empaque mejoran significativamente mientras la oferta de los tres incumbentes expande simultáneamente.
3. Después de aumentos de precios de memoria, los clientes reducen su contenido por dispositivo y las deferciones de compra se vuelven generalizadas.
4. Las calificaciones y ventas de CXMT DDR5 y LPDDR5X fuera de China aumentan.
5. Los crecimientos de precio de contrato para DRAM y HBM y el EPS para 2028 son simultáneamente ajustados al bajo.

### Condiciones de Alerta para P4

1. Las grandes tecnológicas de EE.UU. cortan su CAPEX o cancelan o retrasan proyectos de centro de datos.
2. Los spreads crediticios y el riesgo de refinanciación para clientes de infraestructura de IA suben de manera drástica.
3. Los inventarios de DRAM y NAND se construyen simultáneamente con descensos en precios de contrato.
4. El EPS a 12 meses para Samsung Electronics, SK Hynix y Micron son ajustados al bajo juntos.
5. La fortaleza relativa del sector de semiconductores y el alcance del mercado (ratio avance-retroceso) se deterioran simultáneamente.

## 13. Datos a Seguir a partir de Julio

| Tiempo | Datos a Seguir | Juicio que Cambia |
|---|---|---|
| Finales de julio | Resultados financieros y llamadas de conferencia de las grandes tecnológicas de EE.UU. | CAPEX, margen neta de IA, flujo de efectivo libre, resistencia de precios de memoria |
| Finales de julio | Disclosures adicionales técnicos de Kimi K3 e evaluaciones independientes | ¿Cuál es más grande — avances en eficiencia o crecimiento del uso |
| Finales de julio | Disclosures detalladas de IR de Samsung Electronics y SK Hynix | HBM4, contratos a largo plazo, ASP DRAM y NAND, envíos, CAPEX |
| Agosto en adelante | Precios de contrato para 3Q y niveles de inventario distribuidos | ¿El ritmo de los aumentos de precios ha alcanzado su punto máximo y el precompra se está normalizando |
| Cuatrimestralmente | Pedidos de ASML, CAPEX de TSMC, órdenes de equipos de memoria | Velocidad de la respuesta de suministro para 2027-2028 |
| Ongoing | Acciones regulatorias y calificaciones de CXMT e YMTC | Contagio de precios de la oferta china a los mercados globales y bifurcación del mercado |

## 14. Juicio Final

Esta semana sirvió como el primer test integral de la narrativa del superciclo de memoria. Los precios de las acciones se movieron significativamente, pero los resultados de TSMC y ASML, los precios de DRAM y NAND y la demanda de memoria para servidores inclinaron la balanza de evidencias hacia la escasez física persistente en 2026-2027.

Al mismo tiempo, el mismo dato hizo que los riesgos para 2028 se definieran con mayor claridad. La expansión de capacidad del equipo y CAPEX, los acuerdos a largo plazo de suministro HBM retrasan la transmisión de aumentos de precios, los clientes deben absorber los precios elevados de memoria junto con los costos de financiamiento de centros de datos, y la memoria commodity china e incrementos en eficiencia de modelos abiertos ejercerán presión sobre los precios y múltiplos para 2028.

La elección entre "el boom está terminado" o "esto es un superciclo permanente" es una falsa alternativa. El camino base actual es el siguiente:

```text
2026-2027: Escasez física y altos beneficios
-> 2027-2028: Respuesta de capacidad, rendimiento y yield
-> La velocidad de los aumentos de precios se desacelera
-> Los beneficios absolutos permanecen por encima del nivel histórico, pero los múltiplos se comprimen
-> La dispersión de retornos entre las empresas se conduce por la mezcla de productos, estructura de contratos y exposición a China
```

Desde este punto, el principal desafío no es volver a probar que existe una demanda de IA. Es medir simultáneamente la velocidad de la respuesta de suministro, la trayectoria de monetización para los clientes, la calidad del contrato, las estimaciones de beneficios para 2028 y cómo reaccionan los precios de las acciones a noticias positivas. Los beneficios hoy hablan de 2026 y 2027. El mercado ya está preguntando sobre 2028.

---

## Fuentes Clave

* [Resultados financieros oficiales de TSMC Q2 2026](https://investor.tsmc.com/english/quarterly-results/2026/q2)
* [Resultados financieros y planes de capacidad de ASML Q2 2026](https://www.asml.com/en/news/press-releases/2026/q2-2026-financial-results)
* [Perspectiva de precios de DRAM y NAND de TrendForce Q2 2026](https://www.trendforce.com/presscenter/news/20260331-12995.html)
* [Perspectiva de precios de DRAM para servidores de TrendForce Q3 2026](https://www.trendforce.com/presscenter/news/20260709-13140.html)
* [Carta del Comité Selecto de EE.UU. sobre China — Llamado a restricciones en la adquisición de memoria china](https://chinaselectcommittee.house.gov/media/letters/moolenaar-whitesides-to-secretary-lutnick-hold-firm-on-chinese-memory-chips-ban)
* [Regulaciones del Registro de Entidades de BIS del Departamento de Comercio de EE.UU.](https://www.bis.gov/ear/title-15/subtitle-b/chapter-vii/subchapter-c/part-744/ss-74416-entity-list)
* [Anuncio oficial de Kimi K3](https://www.kimi.com/blog/kimi-k3)
* [Anuncio oficial de CXMT LPDDR5X](https://www.cxmt.com/en/news/info_19.html)
## Limitaciones de los Datos Públicos

1. Las fórmulas de precios a largo plazo para HBM de Samsung Electronics, SK Hynix y Micron — incluyendo precios mínimos y máximos, volúmenes de compras mínimos, cláusulas de cancelación y términos de crédito específicos para clientes— no han sido divulgados públicamente.
2. No existen cifras oficiales confiables sobre la tasa de producción HBM o el progreso de CXMT hacia la calificación por Apple.
3. Los costos unitarios completos por modelo y los costos reales por acelerador para proveedores chinos de API de inteligencia artificial no se informan públicamente.
4. La cifra estimada de 26,7 EB de demanda de HBM para 2030 no es una proyección consensuada, sino un escenario construido combinando varias suposiciones optimistas.
5. Las comprobaciones del canal en julio de 19 sobre DRAM de servidores y HBM4 no pueden ser verificadas independientemente a partir de documentos primarios y se utilizan solo como referencia directiva.
6. La fecha de corte de la información es el 19 de julio de 2026. Los escenarios deben reevaluarse después de las presentaciones financieras de las grandes empresas tecnológicas de EE.UU. y los fabricantes de memoria esperadas a finales de julio.

> Este artículo es un análisis informativo basado en fuentes públicas y no constituye una recomendación para comprar o vender ninguna seguridad específica. Los precios, dinámicas de oferta y demanda, estimaciones de ganancias y condiciones regulatorias pueden cambiar; los lectores deben verificar las últimas divulgaciones e evaluar los hallazgos según su tolerancia al riesgo.
