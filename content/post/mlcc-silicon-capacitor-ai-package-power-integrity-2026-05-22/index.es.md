---
title: "MLCCs y Condensadores de Silicio: Lo que el Contrato de ₩1,5 Billones de Samsung Electro-Mechanics Revela sobre el Cuello de Botella de Energía en los Paquetes de IA"
date: 2026-05-22
description: "Un MLCC es un componente cerámico ultracompacto presente en casi cualquier dispositivo electrónico que estabiliza la alimentación eléctrica. Un condensador de silicio es un componente de alto rendimiento colocado dentro o inmediatamente junto a los paquetes de GPU e HBM de IA para suprimir fluctuaciones instantáneas de potencia. La clave no es que los condensadores de silicio reemplacen a los MLCCs, sino que el campo de batalla de los componentes pasivos se está expandiendo desde la superficie de la PCB hacia el interior de los paquetes de semiconductores de IA. El contrato de suministro de ₩1,5 billones de Samsung Electro-Mechanics es una señal de que las empresas de MLCCs y sustratos podrían reclasificarse como actores de la cadena de suministro de integridad de potencia en paquetes de IA. Dicho esto, los tres valores principales de MLCC subieron un promedio de +35,6% esta semana y Samsung Electro-Mechanics cotiza ahora a 73x PER 2026E. Un cambio sectorial convincente y un precio de entrada atractivo son dos cosas distintas."
categories: ["Stock-Analysis"]
tags:
  - "MLCC"
  - "Condensador de Silicio"
  - "Samsung Electro-Mechanics"
  - "009150"
  - "Empaquetado de IA"
  - "Integridad de Potencia"
  - "Cadena de Valor de Semiconductores"
  - "Sustrato"
slug: mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22
---

> 📚 Series Relacionadas
> [Contrato de ₩1,5 Billones en Condensadores de Silicio de Samsung Electro-Mechanics](/es/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [Samsung Electro-Mechanics: Retador Híbrido](/es/post/samsung-electro-mechanics-hybrid-challenger-2026-05-17/) / [Análisis en Profundidad del Negocio MLCC y FC-BGA de Samsung Electro-Mechanics](/es/post/samsung-electro-mechanics-mlcc-fcbga-ai-infrastructure-deep-dive-2026-05-15/) / [Hub de la Cadena de Valor de Semiconductores](/es/page/korea-semiconductor-equipment-ip-hub/) / [Hub de Sustratos y PCB para IA](/es/page/korea-ai-pcb-substrate-hub/)

<figure>
  <img src="/img/posts/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/MLCC_Concept.png" alt="Diagrama conceptual de MLCCs y condensadores de silicio" loading="lazy">
</figure>

*Un MLCC es un tipo de condensador: un componente cerámico ultracompacto presente en prácticamente cualquier dispositivo electrónico que actúa como estabilizador de potencia. Un condensador de silicio se coloca más cerca del chip semiconductor que un MLCC —en algunos casos dentro del propio paquete— para suprimir las fluctuaciones instantáneas de potencia en GPUs de IA y HBM. Desde el punto de vista inversor, lo relevante es la señal de que los "componentes pasivos" están pasando de ser simples piezas de commodity a convertirse en componentes clave para el empaquetado de IA y la integridad de potencia.*

---

## Resumen Ejecutivo

Un condensador almacena carga eléctrica brevemente y la libera cuando se necesita. Para quienes no son ingenieros, puede pensarse como un **depósito de agua, amortiguador o filtro de ruido para un circuito eléctrico**. Un MLCC es la versión cerámica multicapa de mayor volumen de ese condensador. Samsung Electro-Mechanics describe los MLCCs como una "presa" que retiene la electricidad y la libera de forma controlada.[^samsung-mlcc]

Un condensador de silicio es también un tipo de condensador. A diferencia de un MLCC, que apila cientos de capas cerámicas, un condensador de silicio forma capas dieléctricas y de electrodo sobre una oblea de silicio. Según la documentación de productos de Samsung Electro-Mechanics, puede adelgazarse a menos de 100 micrómetros, embeberse dentro de un paquete y se beneficia de una baja inductancia parásita, favorable para la estabilización de potencia.[^samsung-sicap-product]

El punto esencial es **no la sustitución, sino el desplazamiento de ubicación**. Los MLCCs se montan principalmente en la superficie de la PCB o alrededor del chip. Los condensadores de silicio pueden ir dentro del paquete, bajo el sustrato o directamente junto al die. Como las GPUs de IA y la HBM demandan picos de corriente repentinos e intensos, la proximidad importa tanto como la capacitancia bruta: "qué tan rápido puede entregarse la potencia" pasa a ser tan importante como "cuánto puede almacenarse".

El contrato de suministro de condensadores de silicio de Samsung Electro-Mechanics del 20 de mayo de 2026, valorado en aproximadamente ₩1,5 billones, es la primera evidencia a gran escala de este cambio estructural. El contrato va del 1 de enero de 2027 al 31 de diciembre de 2028. La empresa indicó que el producto se embebe dentro de paquetes de semiconductores de alto rendimiento —incluidas GPUs para servidores de IA y HBM— para mejorar la estabilidad del suministro eléctrico.[^samsung-sicap-contract]

El juicio inversor, sin embargo, debe mantenerse frío. Esta semana (18–22 de mayo), los tres valores principales del sector MLCC promediaron <strong>+35,6%</strong>, superando ampliamente a los cinco valores principales de sustratos de IA, que promediaron <strong>+14,0%</strong>. Samsung Electro-Mechanics ganó un +32,7% en la semana; Samwha Capacitor se disparó un +56,4%. El impulso temático es innegable, pero la eficiencia del despliegue de nuevo capital se ha reducido drásticamente.

Conclusión: **la importancia de los condensadores de silicio no reside en que reemplacen a los MLCCs, sino en la expansión del campo de batalla de los componentes pasivos desde la superficie de la PCB hacia el interior de los paquetes de semiconductores de IA**. Las líneas de productos premium de Samsung Electro-Mechanics y Murata podrían reclasificarse como activos de la cadena de suministro de infraestructura de IA. Pero un buen cambio sectorial y un buen precio de entrada siguen siendo preguntas completamente distintas.

---

## 1. La Relación entre Condensadores y MLCCs

Un condensador almacena carga eléctrica y la libera rápidamente cuando se necesita. Cuando un chip semiconductor demanda un repentino pico de corriente, el condensador cercano lo suministra, evitando que el voltaje colapse. A la inversa, cuando el voltaje sube bruscamente, el condensador absorbe parte de él y estabiliza el circuito. Por eso los condensadores desempeñan funciones de almacenamiento de energía, suavizado de voltaje, rechazo de ruido y estabilización de potencia en los circuitos electrónicos.

Un MLCC —**Multi-Layer Ceramic Capacitor**— es un condensador ultracompacto construido apilando cientos de finas capas dieléctricas cerámicas intercaladas con capas de electrodo metálico. Samsung Electro-Mechanics menciona capacidad de producción para MLCCs de alta capacitancia con hasta 600 capas, señalando que su importancia crece con la expansión del 5G, la electrónica de consumo, los vehículos autónomos y el Internet de las Cosas.[^samsung-mlcc]

La jerarquía es sencilla:

```text
Condensador = la categoría completa de componentes de estabilización eléctrica
MLCC = una variante cerámica multicapa de gran volumen dentro de esa categoría
Condensador de silicio = una variante de alto rendimiento basada en oblea de silicio, optimizada para la máxima proximidad
```

Tanto los MLCCs como los condensadores de silicio son condensadores. Difieren en dónde se despliegan y qué exigencias de rendimiento están diseñados para satisfacer.

---

## 2. Condensador vs. MLCC vs. Condensador de Silicio

| | Condensador General | MLCC | Condensador de Silicio |
|---|---|---|---|
| Categoría | Familia amplia | Un tipo de condensador | Un tipo de condensador |
| Analogía simple | Depósito de agua del circuito | Depósito de agua cerámico ultracompacto | Depósito de agua de ultrapróxima colocado junto o dentro del chip |
| Material principal | Cerámica, electrolito de aluminio, tántalo, película, silicio, etc. | Dieléctrico cerámico + electrodos metálicos internos | Estructura basada en oblea de silicio |
| Función principal | Almacenamiento de energía, suavizado de voltaje, rechazo de ruido | Filtrado de ruido de alta frecuencia, estabilización de potencia alrededor de chips, miniaturización | Supresión de transitorios instantáneos de potencia en GPUs de IA, HBM y chips de alto rendimiento |
| Ubicación típica | Etapas de potencia, placas, módulos, motores, inversores | Principalmente en la PCB, alrededor de chips y módulos | Dentro de paquetes, en sustratos, inmediatamente adyacente al die |
| Ventajas | Amplia selección para diferentes aplicaciones | Pequeño, económico y producible en masa | Extremadamente delgado; puede colocarse cerca del die; favorable para la estabilización de potencia |
| Limitaciones | Gran varianza de rendimiento según el tipo | Limitado en estabilización de potencia de paquetes a ultravelocidad y ultraproximidad | Alta complejidad y coste de fabricación; mercado direccionable actual concentrado en semiconductores de alto rendimiento |
| Principales vectores de crecimiento | Automoción, redes eléctricas, industria, servidor de IA | Automoción, servidor de IA, smartphone, 5G, IoT | GPU de IA, HBM, computación de alto rendimiento, chips móviles de alto rendimiento |

Un vistazo al catálogo de productos de condensadores de TDK ilustra la amplitud de la categoría: MLCCs pequeños, condensadores cerámicos de alta tensión, condensadores de película, condensadores electrolíticos de aluminio y condensadores de potencia conviven bajo el mismo paraguas de "condensador".[^tdk-capacitors] "Los condensadores son buenos" es una afirmación demasiado amplia. En términos de inversión, lo que importa es qué condensador, en qué ubicación y para qué aplicación.

---

## 3. Dónde se Utilizan

### 3.1 Condensadores Generales

Los condensadores generales aparecen en prácticamente cualquier circuito eléctrico, desde la electrónica de consumo hasta la infraestructura de potencia.

| Aplicación | Tipo Principal de Condensador | Función |
|---|---|---|
| Smartphone, PC | MLCC, tántalo, polímero | Estabilización de potencia alrededor de procesadores de aplicaciones, memoria y PMIC |
| Servidor, servidor de IA | MLCC, polímero, condensador de silicio | Supresión de transitorios de potencia en CPUs, GPUs y HBM |
| Electrónica de automoción | MLCC, película, electrolítico de aluminio, tántalo | Estabilización de ECUs, ADAS, inversores, cargadores y BMS |
| Sistemas de potencia para VE | Película, MLCC de alta tensión, electrolítico de aluminio | Enlace DC de alta tensión, carga y conversión de potencia |
| Industria y redes eléctricas | Película, electrolítico de aluminio | Corrección del factor de potencia, variadores de motor, almacenamiento de energía |
| Telecomunicaciones, alta frecuencia | Cerámica, condensador de silicio | Filtrado de alta frecuencia, adaptación de impedancia |

### 3.2 MLCC

La aplicación central de los MLCCs es la **estabilización de potencia alrededor de los chips**. Aparecen en smartphones, automóviles, servidores, equipos de red, electrodomésticos y maquinaria industrial. A medida que los dispositivos se reducen, los semiconductores conmutan más rápido y aumenta el número de sensores y módulos de comunicación, los puntos que requieren estabilización de voltaje crecen proporcionalmente.

La importancia de los MLCCs en los servidores de IA también está aumentando. TDK señala que, a medida que la demanda de IA y nube impulsa una mayor densidad de integración y rendimiento en los servidores de centros de datos, la densidad de potencia por rack y por servidor aumenta, lo que convierte el rendimiento y la huella de los componentes pasivos en una limitación real de diseño.[^tdk-capacitors] Por eso la tesis de los MLCCs ha evolucionado más allá de una simple recuperación del ciclo de smartphones hacia la estabilización de potencia en servidores de IA.

### 3.3 Condensadores de Silicio

La aplicación central de los condensadores de silicio es la **estabilización de potencia dentro de los paquetes**. Samsung Electro-Mechanics describe los condensadores de silicio como dispositivos ultracompactos de alto rendimiento construidos sobre obleas de silicio, embebidos dentro de paquetes de semiconductores de alto rendimiento —incluidas GPUs para servidores de IA y HBM— para mejorar la estabilidad del suministro eléctrico.[^samsung-sicap-contract]

La documentación de producto de la empresa lo refuerza: los condensadores de silicio forman el dieléctrico y los electrodos internos sobre silicio, pueden adelgazarse a menos de 100 micrómetros mediante procesado de oblea y son adecuados para su embebido dentro de paquetes. La baja inductancia parásita es la ventaja clave para la estabilización de potencia.[^samsung-sicap-product]

Para desmitificar la terminología:

```text
Inductancia parásita = factor de interferencia que retrasa la respuesta instantánea del flujo de corriente
Resistencia parásita = factor de interferencia que genera pérdidas de energía al paso de la corriente
Integridad de potencia = capacidad de entregar voltaje y corriente estables y sin rizado al chip exactamente cuando se necesitan
```

Los semiconductores de IA consumen potencia en picos repentinos e intensos. Un condensador alejado del die responde demasiado lento. La solución es mover el condensador inmediatamente junto al chip —o dentro del propio paquete—. La tesis de inversión en condensadores de silicio no es "mayor capacitancia" sino **respuesta más rápida desde una ubicación más cercana**.

---

## 4. Principales Proveedores y Base de Clientes

### 4.1 Principales Proveedores de MLCC

| Región | Empresas Principales | Fortalezas |
|---|---|---|
| Japón | Murata, TDK, Taiyo Yuden | Liderazgo en MLCC ultrapequeño, alta fiabilidad y grado automotriz |
| Corea | Samsung Electro-Mechanics | MLCC de alto valor para IT, automoción y servidor de IA; expansión hacia condensadores de silicio |
| Taiwán / Gran China | Yageo, Walsin | Cartera de componentes pasivos commodity, industrial y de precio medio-bajo |
| EE.UU. / Filiales japonesas | KYOCERA AVX, KEMET/Yageo, Vishay | Condensadores especiales, líneas de producto automotriz, industrial y de alta frecuencia |

La base de clientes de MLCC es enormemente amplia: fabricantes de smartphones, productores de PCs y servidores, OEMs de automoción, proveedores Tier-1, fabricantes de equipos de telecomunicaciones y empresas de módulos de semiconductores. Para invertir en MLCCs, **la mezcla de demanda por mercado final y la cuota de productos de alto valor** importan más que la exposición a un cliente concreto.

### 4.2 Principales Proveedores de Condensadores de Silicio

| | Empresas Principales | Posicionamiento |
|---|---|---|
| Murata | Líder en condensadores de silicio y dispositivos pasivos integrados | Condensadores de silicio para móvil de alto rendimiento, telecomunicaciones y computación de alto rendimiento |
| Samsung Electro-Mechanics | Nuevo entrante a gran escala | Ha asegurado un contrato de suministro de aproximadamente ₩1,5 billones para entrega en 2027–2028 |
| KYOCERA AVX y otros | Condensadores MOS especializados | Líneas de producto de alta frecuencia, microondas e industria especializada |
| Ecosistema de empaquetado avanzado | Opciones cautivas o de codiseño | Vinculado a la tecnología de interposer e integridad de potencia dentro del paquete |

La dimensión del cliente es crítica. Los MLCCs tienen una base de clientes amplia y sustituible. Los condensadores de silicio, en cambio, deben diseñarse dentro de un paquete desde el inicio. Requieren cualificación del cliente, integración en la arquitectura del paquete y validación de la integridad de potencia. Una vez diseñados, son difíciles de reemplazar: el coste de cambio es elevado.

La contraparte del contrato de Samsung Electro-Mechanics se revela oficialmente solo como "una gran corporación global". Por tanto, sería incorrecto identificar al cliente como NVIDIA, AMD, Broadcom, Google, Meta, Microsoft, Amazon u otra empresa específica. Eso permanece sin confirmar.

---

## 5. Lo que Realmente Significan los Condensadores de Silicio

### 5.1 Significado Técnico — El Cuello de Botella de Potencia Migra al Interior del Paquete

A medida que las GPUs de IA y la HBM escalan en intensidad de cómputo y movimiento de datos, la demanda de corriente instantánea ha crecido sustancialmente. El problema es que la potencia que llega desde lejos se ralentiza por los elementos parásitos en las trazas de alimentación, el sustrato y el paquete, lo que degrada la respuesta transitoria. La solución es acercar los condensadores al die.

Los MLCCs convencionales se sitúan principalmente en la PCB o alrededor del perímetro del paquete. Los condensadores de silicio pueden ir dentro del paquete o inmediatamente adyacentes al die. Con condensadores de capacitancia equivalente, **la ubicación determina el rendimiento**.

### 5.2 Significado Empresarial — Los Componentes Pasivos se Revalúan como Componentes de Empaquetado de IA

Los MLCCs han sido tradicionalmente valorados como componentes cíclicos. Cuando la demanda de smartphones y PCs se debilita, siguen ajustes de inventario y los productos commodity afrontan competencia de precios. Los condensadores de silicio, en cambio, son componentes de alta complejidad embebidos dentro de paquetes de GPUs de IA y HBM. Requieren cualificación del cliente, integración en el diseño del paquete y validación de la integridad de potencia.

Para Samsung Electro-Mechanics, este contrato tiene un significado estratégico más allá de la cifra de ingresos. La empresa afirmó oficialmente que aprovechó sus capacidades de proceso de precisión acumuladas en los negocios de MLCC y sustrato de paquetes para entrar en la cadena de suministro central de semiconductores de IA.[^samsung-sicap-contract]

### 5.3 Significado de Inversión — Posible Reclasificación como Valores de "Componentes para Servidores de IA"

El mercado ha visto históricamente a Samsung Electro-Mechanics como una empresa de MLCCs, módulos de cámara y sustratos. Si los ingresos por condensadores de silicio escalan hasta niveles de producción masiva, esa clasificación cambia parcialmente.

| Percepción Anterior del Mercado | Posible Percepción Post-Condensador de Silicio |
|---|---|
| Valor de componentes para smartphones | Valor de componentes para servidores de IA |
| Acción cíclica de MLCC | Acción de componentes de integridad de potencia de alto valor |
| Historia de crecimiento en MLCC automotriz | Entrante a la cadena de suministro de empaquetado GPU de IA / HBM |
| Exposición a pasivos commodity | Exposición a componentes de alta complejidad dentro del paquete |

Sin embargo, los riesgos de exagerar persisten. Los condensadores de silicio no reemplazarán el mercado total de MLCCs. El crecimiento llegará primero en el interior de paquetes de IA, computación de alto rendimiento, chips móviles de alto rendimiento y algunas aplicaciones de telecomunicaciones e industria donde se requiere rendimiento extremo. La gran mayoría de la demanda de estabilización de potencia en smartphones convencionales, automóviles y electrodomésticos probablemente seguirá siendo dominio de los MLCCs en el futuro previsible.

---

## 6. La Cinta de Esta Semana — Los MLCCs Superaron a los Sustratos de IA

Esta semana (18–22 de mayo de 2026), el mercado revaluó agresivamente el tema de los MLCCs. Los tres valores principales de MLCC promediaron <strong>+35,6%</strong>; los cinco valores principales de sustratos de IA promediaron <strong>+14,0%</strong>.

### 6.1 Cesta de los Tres Principales Valores de MLCC

| Nombre | Retorno Semanal | 20D | 60D | PER 2026E | Extranjero | Institucional | Extr. + Inst. | Programa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Samwha Capacitor | **+56,4%** | +56,0% | +68,0% | 40,8x | -₩5,88MM | +₩16,09MM | +₩10,21MM | N/A |
| Samsung Electro-Mechanics | **+32,7%** | +65,0% | +200,5% | 73,2x | -₩292,90MM | +₩111,79MM | -₩181,11MM | +₩170,96MM |
| Amotech | +17,6% | -18,4% | +55,2% | 18,9x | +₩4,91MM | -₩0,87MM | +₩4,05MM | +₩5,10MM |

Samsung Electro-Mechanics encadenó tres sesiones consecutivas de fortaleza: +7,5% el 20 de mayo, +13,5% el 21 de mayo y +11,3% el 22 de mayo. Samwha Capacitor fue más extremo: +23,0% el 20 de mayo, +29,9% el 22 de mayo. Esto no es tanto un movimiento impulsado puramente por resultados como **una revaluación de los componentes de integridad de potencia para IA que se originó en Samsung Electro-Mechanics y se irradió hacia el ecosistema MLCC**.

### 6.2 Cesta de los Cinco Principales Valores de Sustratos de IA

| Nombre | Retorno Semanal | 20D | 60D | PER 2026E | Extranjero | Institucional | Extr. + Inst. | Programa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simtech | **+31,4%** | +52,2% | +146,8% | 38,7x | -₩24,58MM | +₩61,81MM | +₩37,22MM | -₩5,35MM |
| TLB | +18,0% | +44,4% | +89,2% | 25,3x | -₩7,80MM | +₩15,30MM | +₩7,50MM | -₩3,98MM |
| Daeduck Electronics | +11,4% | +49,5% | +132,8% | 38,9x | -₩2,93MM | +₩29,05MM | +₩26,12MM | +₩5,28MM |
| Korea Circuit | +10,7% | +5,6% | +66,7% | 25,5x | -₩2,71MM | -₩0,58MM | -₩3,29MM | +₩0,44MM |
| ISU Petasys | -1,5% | -21,9% | +12,7% | 35,6x | -₩119,17MM | -₩0,74MM | -₩119,90MM | -₩125,28MM |

La cesta de sustratos de IA no fue una marea uniformemente al alza. Simtech, TLB y Daeduck Electronics fueron sólidos, pero ISU Petasys cerró la semana en -1,5% en medio de fuertes ventas de extranjeros y programas. Dentro de los sustratos de IA, el mercado pareció favorecer esta semana la **exposición a SoCAMM, módulos de memoria y FC-CSP frente a las placas de red de alto número de capas**.

### 6.3 El Liderazgo de Precio va a los MLCCs; la Calidad del Flujo Favorece a Ciertos Nombres de Sustratos de IA

| Cesta | Extranjero | Institucional | Extr. + Inst. | Minorista | Programa |
|---|---:|---:|---:|---:|---:|
| MLCC principal (3 valores) | -₩293,86MM | +₩127,01MM | -₩166,85MM | +₩159,40MM | +₩176,05MM |
| Sustrato IA principal (5 valores) | -₩157,19MM | +₩104,84MM | -₩52,35MM | +₩52,05MM | -₩128,89MM |
| Sustrato IA ex-ISU Petasys | -₩38,02MM | +₩105,57MM | +₩67,55MM | -₩65,47MM | -₩3,60MM |

En precio, los MLCCs dominaron. En calidad de flujo, **la cesta de sustratos de IA excluyendo ISU Petasys** luce más limpia. Simtech, TLB y Daeduck muestran una clara acumulación institucional con vendedores minoristas o flujo minorista neutro —una configuración más constructiva—. En los valores de MLCC, los ₩292,9MM de ventas de extranjeros solo en Samsung Electro-Mechanics son demasiado grandes para ignorar. El precio de la acción fue fuerte, pero esto parece más una revaluación impulsada por institucionales, programas y minoristas que una acumulación liderada por extranjeros.

---

## 7. Evaluación de Inversión

| Nombre | Visión |
|---|---|
| MLCC | Mayor impulso de precio. Riesgo de sobrecalentamiento y presión vendedora de extranjeros presentes. |
| Sustratos de IA | Retorno absoluto inferior, pero el flujo institucional y la vinculación a resultados son más estables. |
| Samsung Electro-Mechanics | Líder transversal en MLCC, FC-BGA y condensadores de silicio. Mantener es defendible; perseguir, no. |
| Samwha Capacitor | Mayor intensidad de expansión temática. +56% en una semana hace que una nueva entrada sea extremadamente difícil. |
| Daeduck Electronics | Posición central en sustratos de IA. El descuento de valoración frente a Samsung Electro-Mechanics es significativo. |
| Simtech / TLB | Lideraron la expansión de sustratos de IA esta semana. La semana próxima, vigilar una consolidación post-calor antes de reentrar. |
| ISU Petasys | Rezagado relativo dentro de los sustratos de IA. Menor prioridad hasta que el flujo de extranjeros se estabilice. |

El mercado de esta semana fue uno en que **la atención se expandió desde los sustratos de IA hacia los MLCCs**. La tesis de los sustratos de IA no ha quedado invalidada. Más bien, el mercado está desagregando "el próximo cuello de botella después de la memoria" con mayor precisión, extendiendo la revaluación hacia los componentes de integridad de potencia en servidores de IA.

En términos prácticos:

```text
Mantener: Samsung Electro-Mechanics, Daeduck Electronics
No perseguir: Samsung Electro-Mechanics, Samwha Capacitor
Vigilar en corrección: Simtech, TLB
Esperar recuperación del flujo: ISU Petasys
Confirmación clave necesaria: Si las subidas de precio de MLCC y los ingresos de servidores de IA impulsan revisiones de resultados en 2T–3T
```

---

## 8. Conclusión en Una Línea

Un MLCC es el "depósito de agua cerámico ultracompacto" de la industria electrónica. Un condensador de silicio es un "estabilizador de potencia de ultraproximidad" embebido dentro de los paquetes de GPUs de IA y HBM. Los condensadores de silicio no reemplazan a los MLCCs. El campo de batalla de los componentes pasivos se está expandiendo desde la superficie de la PCB hacia el interior de los paquetes de semiconductores de IA.

El verdadero significado del contrato de ₩1,5 billones de Samsung Electro-Mechanics no es "vender un tipo más de condensador". Es la señal de que **un fabricante de componentes pasivos ha entrado en la cadena de suministro de componentes clave dentro de los paquetes de semiconductores de IA**. Este cambio puede reclasificar las líneas de productos premium de Samsung Electro-Mechanics y Murata como activos de la cadena de valor de infraestructura de IA.

El mercado, sin embargo, ya ha respondido con rapidez. Los tres valores principales de MLCC promediaron +35,6% esta semana; Samsung Electro-Mechanics acumula +200,5% en 60 días y cotiza a 73,2x PER 2026E. La empresa es excelente y el cambio sectorial es real. Si el precio actual es también un buen punto de entrada nuevo es una pregunta completamente distinta. El próximo catalizador a seguir no es la acción del precio sino **las revisiones de resultados del 2T–3T, la divulgación desagregada de ingresos en servidores de IA, pedidos adicionales de condensadores de silicio y la recuperación del flujo de extranjeros**.

---

*Este artículo tiene exclusivamente propósitos de investigación y análisis y no constituye asesoramiento de inversión. Las descripciones técnicas de condensadores, MLCCs y condensadores de silicio se basan en materiales oficiales de Samsung Electro-Mechanics, TDK, Murata y otras fuentes técnicas públicamente disponibles. El contrato de suministro de condensadores de silicio de Samsung Electro-Mechanics (aproximadamente ₩1,5 billones, del 1 de enero de 2027 al 31 de diciembre de 2028) refleja el anuncio oficial de la empresa. El cliente no ha sido revelado públicamente; no se ha identificado ninguna GPU, ASIC ni empresa cloud específica como contraparte. Los datos de precio, flujo y valoración del período 18–22 de mayo de 2026 proceden de la base de datos local del Research OS del analista y pueden diferir de los datos oficiales de la bolsa o de los brókers. El PER 2026E, las cifras de flujo extranjero/institucional/programa y los promedios de las cestas de los tres principales valores de MLCC y los cinco principales de sustratos de IA reflejan la clasificación del analista. El análisis puede ser incorrecto. Fecha de referencia de los datos: 22 de mayo de 2026, KST.*

[^samsung-mlcc]: [Samsung Electro-Mechanics, Descripción del Producto MLCC](https://samsungsem.com/kr/product/passive-component/mlcc.do)
[^samsung-sicap-product]: [Samsung Electro-Mechanics, Descripción del Producto Condensador de Silicio](https://www.samsungsem.com/global/product/passive-component/silicon-capacitor.do)
[^samsung-sicap-contract]: [Samsung Electro-Mechanics, Anuncio del Contrato de Suministro de Condensadores de Silicio por ₩1,5 Billones](https://samsungsem.com/global/newsroom/news/view.do?id=10310)
[^tdk-capacitors]: [TDK, Cartera de Productos de Condensadores y Materiales de Aplicación en Sistemas de Potencia para Servidores de IA](https://product.tdk.com/en/products/capacitor/index.html)

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
