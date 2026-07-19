---
title: "Expansión de producción de NVIDIA Vera CPU y Simmtech: SoCAMM2 es sobre unidades de módulos, no bits"
slug: "nvidia-vera-cpu-socamm2-simmtech-module-unit-thesis-2026-07-19"
date: 2026-07-19T18:05:00+09:00
description: "Mientras NVIDIA expande Vera CPU en NVL72 y servidores independientes, verificamos si la reducción de capacidad SoCAMM2 es negativa para Simmtech. Conectando materiales oficiales de NVIDIA, TrendForce, SK Hynix y Simmtech con el precio de las acciones del 16 de julio, oferta-demanda y consenso para establecer lógica de inversión basada en unidades de módulos y condiciones de entrada."
categories: ["Análisis Exclusivo", "Análisis Técnico", "Acciones"]
tags:
  - "Simmtech"
  - "NVIDIA"
  - "Vera CPU"
  - "Vera Rubin"
  - "SoCAMM2"
  - "LPDDR5X"
  - "Servidores AI"
  - "PCB de módulo de memoria"
  - "Sustratos de semiconductores"
  - "Oferta y demanda"
series: ["exclusive-analysis", "ai-hbm-2026"]
valley_cashtags:
  - 심텍
draft: false
---

Un NVIDIA Vera Rubin NVL72 contiene 36 CPUs Vera y 54TB de memoria LPDDR5X. Eso es 1.5TB por CPU. Sin embargo, en junio, TrendForce informó que NVIDIA reduciría a la mitad la capacidad de sus próximos módulos Vera SoCAMM mientras aumentaba los envíos totales de módulos y la producción de Vera CPU.

En la superficie, la capacidad de memoria reducida parece negativa para los proveedores de componentes. Al medir la demanda de PCB puramente en términos de bits, lo es. Sin embargo, lo que Simmtech fabrica no son chips DRAM sino PCBs para módulos SoCAMM. El volumen de Simmtech es más sensible al número de CPUs producidas y al número de módulos que a la capacidad total de memoria. Incluso si la escasez de LPDDR fuerza una capacidad menor por CPU, si NVIDIA envía más CPUs Vera y módulos, la demanda de PCB puede no disminuir.

Al observar materiales oficiales, investigaciones de la industria, estimaciones de analistas y precios reales de acciones y datos de oferta-demanda, se muestra que la lógica comercial permanece intacta, pero el precio base aún no ha sido confirmado.

> Contexto conectado
> Este artículo es un seguimiento de [Tesis de inversión en sustrato y PCB de AI: BOM del sistema como cuello de botella común](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/), [Ecosistema de PCB de AI coreano: diez empresas](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/), [Verificación de lista de materiales de Vera Rubin VR200](/post/vera-rubin-vr200-bom-memory-pcb-mlcc-korea-alpha-2026-05-21/), y [Brecha de suministro de memoria derramándose más allá de HBM](/post/memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14/). Los artículos relacionados se pueden encontrar en el [Centro de sustrato y PCB de AI](/page/korea-ai-pcb-substrate-hub/), [Centro de HBM de AI](/page/korea-semiconductor-hbm-kospi-hub/), y [Centro de análisis exclusivo](/page/exclusive-analysis-hub/).

## Resumen ejecutivo

* Las especificaciones oficiales de NVIDIA muestran que Vera Rubin NVL72 utiliza 36 CPUs Vera y 54TB de LPDDR5X. Los racks independientes de Vera CPU admiten hasta 4 nodos por bandeja de 1U, expandiéndose a un máximo de 256 CPUs por rack. La evolución de Vera de CPU de apoyo en racks de GPU a plataforma de servidor independiente está confirmada.
* La reducción de capacidad SoCAMM reportada por TrendForce es una respuesta a la escasez de suministro de LPDDR, no al ralentizamiento de la demanda. NVIDIA tiene la intención de reducir la capacidad por módulo mientras aumenta los envíos totales de módulos y la producción de Vera CPU.
* Simmtech lista PCB SoCAMM en su página oficial de productos. Sin embargo, el suministro simultáneo de tres proveedores de memoria y la alta participación de mercado son estimaciones de analistas, no divulgaciones de la empresa. El ingreso por cliente específico y la participación de mercado reales permanecen sin divulgar.
* El 16 de julio, Simmtech cerró a 107.400 KRW, bajando 11,68% en un solo día. Durante 20 días de negociación, las instituciones compraron 236.200 millones de KRW en neto, y el dinero real (pensión, fondos mutuales, seguros) compró 186.400 millones de KRW, mientras que inversores extranjeros vendieron 161.100 millones de KRW y programas vendieron 185.900 millones de KRW. La presión de compra institucional a mediano plazo choca con la presión de venta a corto plazo.
* El PER 2026E de 27,1x no es barato. Aplicando el EPS esperado 2027E de 6.655 KRW se obtiene 16,1x, pero solo si los ingresos de SoCAMM y los márgenes de ganancia se expanden según lo planeado.
* El veredicto es **Compra Condicional**. Un enfoque más seguro confirma soporte cerca de 104.000 KRW con la reducción de venta de inversores extranjeros y programas, o recuperación a través de 113.800 KRW en mayor volumen.

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Veredicto de este artículo</div>
  <div class="thesis-callout__body">
    Conectar directamente la reducción de capacidad SoCAMM2 a la caída de demanda de PCB de Simmtech utiliza la unidad incorrecta. La fórmula de ingresos de Simmtech se aproxima más a unidades de Vera CPU × módulos por CPU × PCBs por módulo × participación de mercado de Simmtech que a conteos de bits DRAM. Sin embargo, los últimos dos elementos de esta fórmula aún no han sido confirmados por divulgaciones de la empresa.
  </div>
</div>

---

## 1. Números para descartar y números para mantener

El tamaño del mercado de CPU de servidor de 2030 de 170 mil millones de dólares, la relación CPU-GPU de 1:1 y la escasez de DRAM de 2027 que aparecen en el análisis adjunto ya están reflejados en declaraciones importantes de múltiples casas de bolsa y presentaciones corporativas. Son útiles para entender la dirección de la industria pero no son fuentes de rendimientos excesivos específicos de Simmtech.

Cuatro números son más importantes al evaluar Simmtech:

| Elemento | Por qué importa |
|---|---|
| CPUs Vera enviadas | Determina la base instalada para la plataforma SoCAMM |
| Módulos SoCAMM por CPU | Variable de volumen directo para PCBs de módulo de Simmtech |
| Participación de suministro específica del cliente de Simmtech | Determina la porción de Simmtech del crecimiento de la industria |
| Precio unitario y costo de PCB de módulo | Determina la tasa a la que el crecimiento de ingresos se convierte en ganancia operativa |

Usando suposiciones de 5 a 6 millones de CPUs Vera y 8 módulos por CPU se obtienen 40 a 48 millones de módulos anuales. A 5,5 millones de unidades, eso son 44 millones de módulos. Sin embargo, este cálculo no es un plan oficial de envío de NVIDIA. Es un escenario derivado de estimaciones de envío de CPU de la industria y analistas y configuraciones de sistema divulgadas públicamente.

Por lo tanto, la cifra de 44 millones de unidades no debe usarse directamente como proyección de ingresos. Es solo un ejemplo para calibrar el orden de magnitud.

## 2. Materiales oficiales de NVIDIA confirman la trayectoria de expansión de Vera

### 2.1 NVL72 contiene 36 CPUs Vera

La [página oficial de Vera Rubin NVL72 de NVIDIA](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) presenta la siguiente configuración:

| Elemento | Especificación oficial |
|---|---:|
| GPUs Rubin | 72 |
| CPUs Vera | 36 |
| Memoria de CPU | LPDDR5X 54TB |
| Memoria por Vera CPU | 1.5TB |
| Núcleos Vera CPU | 88 |

La estructura no es simplemente una CPU por GPU. En NVL72, una Vera CPU admite dos GPUs. Sin embargo, un rack de 72 GPU requiere 36 CPUs. Esto muestra que la capa de CPU y LPDDR han subido a componentes importantes en la estructura de costos del sistema de AI.

### 2.2 Vera se vende más allá de racks de GPU

El cambio más significativo es el sistema Vera CPU independiente. El [blog técnico de NVIDIA](https://developer.nvidia.com/blog/?p=114004) explica que los racks de Vera CPU pueden contener hasta 4 nodos por bandeja de 1U y escalar a 256 CPUs Vera por rack. Los sistemas de un solo socket y doble socket admiten hasta 1.5TB de LPDDR5X por socket.

NVIDIA anunció que Cisco, Dell, HPE, Lenovo y Supermicro planean lanzar sistemas basados en Vera en la segunda mitad de 2026. Si el cronograma se mantiene, las fuentes de demanda de Vera se extienden más allá de volúmenes de ensamblaje de NVL72.

```text
Fuentes de demanda de Vera

Capa de CPU en Vera Rubin NVL72
+ Servidores Vera CPU independientes
+ Racks de CPU para inferencia y agentes
+ Sistemas de un solo y doble socket de principales OEMs
```

Es por esto que la lógica de inversión de Simmtech no depende de la producción de rack de GPU solamente. La expansión de sistemas de CPU independientes amplía la base de demanda para módulos SoCAMM y PCBs.

## 3. ¿Qué significa la reducción de capacidad SoCAMM?

[El análisis del 10 de junio de 2026 de TrendForce](https://www.trendforce.com/presscenter/news/20260610-13090.html) encontró que solo alrededor del 60% de los requisitos de LPDRAM 2027 de NVIDIA podían cumplirse con asignaciones reservadas. Para abordar la escasez de suministro, se reporta que NVIDIA ha elegido los siguientes ajustes:

1. Reducir la capacidad de memoria de cada módulo SoCAMM para Vera.
2. Aumentar los envíos totales de módulos.
3. Producir más CPUs Vera con el mismo suministro de LPDRAM.
4. Aumentar la penetración de mercado de racks Vera CPU independientes.

En esta estructura, dos tipos de demanda pueden moverse en diferentes direcciones.

| Unidad de demanda | Impacto de reducción de capacidad |
|---|---|
| Bits DRAM y GB | La capacidad instalada por CPU puede disminuir |
| Módulos SoCAMM | Puede aumentar si el crecimiento de envío de CPU excede la reducción de capacidad |
| PCBs de módulo | Proporcional a módulos, por lo que puede aumentar |
| Sockets, conectores, prueba de módulo | Aumentar con el recuento de módulos |

Expresar esto en términos de Simmtech da la siguiente fórmula:

```text
Volumen de PCB SoCAMM de Simmtech
= Envío de Vera CPU
× módulos SoCAMM por CPU
× PCBs por módulo
× participación de suministro de Simmtech
```

Inversamente, el ingreso de SoCAMM de proveedores de memoria se aproxima a recuento de CPU × GB instalado por CPU × precio por GB. Las mismas noticias pueden tener diferentes impactos en vendedores de DRAM y vendedores de PCB de módulo.

### Desajuste entre especificaciones oficiales y reportaje de TrendForce

La página oficial actual de NVIDIA muestra un máximo de 1.5TB de LPDDR5X por Vera CPU. TrendForce informó de reducción de capacidad de módulo de próxima generación. Con ambos documentos existiendo simultáneamente, aún no está claro cuál caso se aplica:

* La página de NVIDIA continúa mostrando configuración máxima o diseño existente
* La reducción de capacidad se aplica solo a clientes específicos o configuraciones de producto
* Las especificaciones de producción finales aún no se han finalizado

Esta inconsistencia no es ruido a ser ocultado sino un elemento de verificación para el juicio de inversión. La capacidad real por módulo, módulos por CPU y configuración específica del cliente de sistemas de producción debe ser verificada a través de productos lanzados y divulgaciones de la empresa.

## 4. ¿Qué suministra Simmtech en SoCAMM2?

### 4.1 Lo que la empresa confirma oficialmente

La [página oficial de productos de Simmtech](https://www.simmtech.com/product/board06.aspx) clasifica el PCB SoCAMM como un producto de módulo de memoria de próxima generación para AI. Las especificaciones clave presentadas por la empresa son las siguientes:

| Elemento | Descripción oficial de Simmtech |
|---|---|
| Memoria base | LPDDR |
| Aplicación | Módulos de memoria de próxima generación para AI |
| Cantidad de capas | 10–12 capas |
| Requisitos clave | Constante dieléctrica y pérdida bajas, coeficiente de expansión térmica bajo, control de impedancia |
| Tratamiento de superficie | ENIG selectivo |

La confirmación de que el PCB SoCAMM aparece en la lista de productos de Simmtech está establecida. La empresa también fabrica PCBs de módulo de memoria general y sustratos de paquete de memoria. Cuando la demanda de LPDDR del servidor de AI crece tanto en módulos como en paquetes, la empresa tiene una base de productos para responder.

### 4.2 Lo que solo está confirmado por estimaciones de analistas

La afirmación de que Simmtech participa en la producción de SoCAMM2 de Samsung Electronics, SK Hynix y Micron simultáneamente y mantiene alta participación de mercado no es una divulgación de la empresa. Es un análisis y estimación de mercado en el [reporte de casa de bolsa publicado en la página de inicio de Simmtech](https://www.simmtech.com/upload/media/file/639179687810021917.pdf).

Por lo tanto, estas expresiones deben ser distinguidas:

| Expresión | Nivel de evidencia |
|---|---|
| Simmtech posee productos de PCB SoCAMM | Confirmación oficial de la empresa |
| Simmtech participa en producción de SoCAMM2 de tres proveedores de memoria | Estimación de analistas |
| Simmtech mantiene participación de suministro #1 | Estimación de analistas |
| Ingresos específicos del cliente y participación de mercado real | Sin divulgar |
| Cronograma exacto de contribución de SoCAMM a la ganancia de Simmtech | Sin divulgar |

Esta distinción es necesaria porque la calificación del cliente y el volumen de producción impulsan la economía del negocio de sustrato. La capacidad de fabricar un producto y mantener alta participación de mercado para ingresos recurrentes están separados por etapas de calificación del cliente, rendimiento, precio unitario y tasa de utilización.

### 4.3 La producción en masa de SK Hynix confirma la realidad de la plataforma

Según [el anuncio oficial de SK Hynix](https://news.skhynix.com/mass-production-socamm2-192gb/), la empresa comenzó la producción en masa de SoCAMM2 de 192GB usando LPDDR5X de 1cnm en abril de 2026. El producto se dirige a la plataforma NVIDIA Vera Rubin.

Esto muestra que SoCAMM2 no es un proyecto de investigación a largo plazo sino que ha entrado en producción en masa real. Sin embargo, la producción en masa de módulos de SK Hynix no prueba automáticamente los volúmenes de suministro específicos del cliente de Simmtech. Simmtech demostrando ingresos de SoCAMM, mezcla de placa de capa alta y mejoras en tasa de utilización en resultados del segundo y tercer trimestre es necesario por separado.

## 5. Los resultados se están recuperando pero aún en la etapa de probar expectativas

Simmtech registró 1,41 billones de KRW en ingresos de año completo 2025 y 11,9 mil millones de KRW en ganancia operativa, con pérdida neta de 164,2 mil millones de KRW. En el primer trimestre de 2026, los ingresos consolidados se recuperaron a aproximadamente 422,4 mil millones de KRW y la ganancia operativa a aproximadamente 13,7 mil millones de KRW. El consenso del segundo trimestre espera un ritmo de recuperación más rápido.

| Elemento | 1Q26 real | 2Q26 consenso | Cambio secuencial |
|---|---:|---:|---:|
| Ingresos | \~422,4 mil millones KRW | 466,9 mil millones KRW | \~+10,5% |
| Ganancia operativa | \~13,7 mil millones KRW | 47,3 mil millones KRW | \~+245% |
| Margen operativo | \~3,2% | \~10,1% | +6,9 puntos porcentuales |

Los datos reales del primer trimestre son del [reporte trimestral de Simmtech](https://kind.krx.co.kr/external/2026/05/14/000890/20260514001959/11013.htm); las estimaciones del segundo trimestre son del consenso de Naver y WiseReport recopiladas por la base de datos local de Research OS el 16 de julio.

El crecimiento de ganancia operativa supera en gran medida el crecimiento de ingresos. Esto indica la necesidad de aumentos simultáneos en mezcla de producto de alto margen, utilización de fábrica y absorción de costo fijo. Incluso si el volumen de SoCAMM aumenta, el margen de ganancia puede caer por debajo de las expectativas debido a costos de materia prima y recubrimiento de oro, rendimiento inicial y negociaciones de precio específicas del cliente.

### La ruta de ganancia exigida por consenso anual

| Año | Ingresos | Ganancia operativa | Ingreso neto | EPS | PER 2026E (cierre 16 de julio) |
|---|---:|---:|---:|---:|---:|
| 2026E | 1,932 billones KRW | 189,6 mil millones KRW | 149,3 mil millones KRW | 3.968 KRW | 27,1x |
| 2027E | 2,289 billones KRW | Consenso no agregado | 251,0 mil millones KRW | 6.655 KRW | 16,1x |
| 2028E | 2,566 billones KRW | Consenso no agregado | 322,8 mil millones KRW | 8.588 KRW | 12,5x |

Para que el precio de las acciones actual se vea barato, las ganancias de 2027 y 2028 deben materializarse realmente. El PER 2026E actual de 27,1x y PBR de 5,64x sustancialmente refleja recuperación temprana. Un precio objetivo promedio de 171.250 KRW es 59,5% más alto que el precio actual, pero cuando los objetivos están subiendo rápidamente, es difícil usarlos como margen de seguridad.

## 6. Precio de las acciones del 16 de julio: Sobrecalentamiento reducido pero recuperación de tendencia aún no confirmada

Simmtech cerró a 107.400 KRW el 16 de julio, con caída de 11,68% ese día con mínimo intradía de 103.700 KRW. Esto es 34,6% menor que el máximo del 1 de julio de 164.200 KRW.

| Período e indicador | Valor |
|---|---:|
| Retorno de 1 día | -11,68% |
| 5 días | -8,91% |
| 10 días | -13,87% |
| 20 días | -15,76% |
| 60 días | +40,94% |
| 120 días | +109,77% |
| vs. MA de 5 días | -5,42% |
| vs. MA de 20 días | -12,28% |
| vs. MA de 60 días | -4,48% |
| vs. MA de 120 días | +27,39% |
| RSI14 | 44,4 |

El RSI ha salido del territorio de sobreventa. Sin embargo, el precio permanece por debajo de los promedios móviles de 5, 20 y 60 días. Dado que es 27% por encima de la línea de 120 días, no todo el alza del movimiento a largo plazo ha desaparecido. Tanto "una caída pronunciada significa barato" como "la tendencia se ha recuperado" aún no pueden ser confirmadas.

En base a negociación, el mínimo del 14 de julio de 99.600 KRW y el mínimo del 16 de julio de 103.700 KRW representan la zona de soporte primario. El nivel de 113.800 KRW confirma si el soporte de corto plazo roto se recupera; 121.600 a 124.000 KRW es una zona de resistencia donde se superponen el cierre del 15 de julio y el promedio móvil de 20 días.

## 7. Oferta y demanda: Instituciones compraron pero inversores extranjeros y programas aún venden

Las cantidades de compra neta acumuladas hasta el 16 de julio de la base de datos local de Kiwoom de Research OS son las siguientes. Las unidades están en miles de millones de KRW.

| Período | Extranjero | Instituciones | Individuos | Dinero real | Programas |
|---|---:|---:|---:|---:|---:|
| 1 día | -9,83 | -5,88 | +15,57 | -5,91 | -11,55 |
| 5 días | -25,79 | +6,02 | +18,95 | +7,98 | -28,71 |
| 10 días | -93,39 | +80,32 | +11,79 | +75,77 | -40,78 |
| 20 días | -161,09 | +236,21 | -84,25 | +186,44 | -185,94 |

El dinero real es la suma de fondos de pensión, fondos mutuales y seguros. La tabla revela dos cosas simultáneamente.

Primero, en base de 20 días, la compra institucional y de dinero real es sustancial. Durante la corrección posterior al pico, el capital a largo plazo orientado internamente absorbió volumen.

Segundo, la venta de inversores extranjeros y programas ha continuado en escala similar. En la caída del 16 de julio, inversores extranjeros e instituciones vendieron juntos mientras individuos absorbieron 15,57 mil millones de KRW. Es difícil juzgar el fondo confirmado por compra institucional solamente.

La participación de transacciones de venta en corto también subió a 21,2% el 16 de julio. El promedio de 20 días es 9,3%. El inventario de reembolso de venta en corto es aproximadamente 5,48 millones de acciones o 14,6% de acciones emitidas, pero no todo el inventario de reembolso de venta en corto es inventario de venta en corto. Esta cifra debe ser consultada solo como referencia para volumen de venta disponible.

## 8. Simmtech revisado a través de P × Q × C

### P: Precio unitario de PCB SoCAMM de capa alta

El PCB SoCAMM requiere 10–12 capas, pérdida dieléctrica baja, expansión térmica baja y control de impedancia preciso. Mayor dificultad de fabricación en comparación con PCB de módulo de memoria general puede ayudar a mejorar la mezcla de productos. Sin embargo, precios específicos del cliente y estructuras de aumento de precio permanecen sin divulgar.

### Q: Recuento de CPU Vera y módulo SoCAMM

Q es la variable de alza más grande. Más allá de la producción en masa de NVL72, racks Vera CPU independientes y servidores OEM principales están programados para la segunda mitad de 2026. Si NVIDIA sigue el reporte de TrendForce en reducir la capacidad por módulo mientras aumenta los envíos de módulos, la Q de Simmtech puede crecer más rápido que el recuento de bits DRAM.

### C: Materias primas, recubrimiento de oro, rendimiento, utilización

El elemento que determina si el crecimiento de ingresos se convierte en ganancia operativa. Los PCBs son sensibles a precios de oro y cobre, materiales de BT, costos de recubrimiento y rendimiento inicial. Para lograr el consenso de margen operativo de 10,1% para Q2, aumentos de productos de alto margen y paso de costos deben ser confirmados juntos.

## 9. Tres escenarios

| Escenario | Condiciones | Interpretación de ganancias y precio |
|---|---|---|
| Alcista | Vera Rubin y servidores CPU independientes se envían según lo programado; el recuento total de módulos SoCAMM aumenta; Simmtech mantiene participación de mercado de tres proveedores de memoria | EPS 2027E de 6.655 KRW o superior se vuelve alcanzable y justifica PER líder de \~16x |
| Base | Envíos de Vera crecen pero escasez de LPDDR y rampas específicas del cliente se desalinean; participación y margen de Simmtech permanecen en niveles de consenso | El crecimiento comercial permanece válido pero la acción puede fluctuar ampliamente según ganancias y oferta-demanda |
| Bajista | Retrasos en producción en masa de Vera o SoCAMM; capacidad reducida por módulo no conduce a recuento de módulos aumentado; participación o rendimiento de Simmtech underperforms | PER 2026E de 27x se convierte en una carga y la probabilidad de revisitar los mínimos de julio aumenta |

En estos escenarios, la variable más importante no es el mercado de CPU de servidor de 170 mil millones de dólares. Es el volumen de envío real de Simmtech, ingresos específicos del cliente, mezcla de placa de capa alta y margen operativo. Incluso si los números de industria grandes resultan correctos, si la porción acumulable para la empresa es pequeña, la acción luchará.

## 10. Veredicto de inversión y secuencia de verificación

### Veredicto: Compra Condicional

La lógica comercial se ha vuelto más clara. Los materiales oficiales de NVIDIA confirmaron la expansión del servidor independiente de Vera, y el reporte de TrendForce muestra la reducción de capacidad como respuesta a escasez de suministro, no caída de demanda. Simmtech oficialmente posee productos de PCB SoCAMM.

Sin embargo, la acción permanece bajo presión de venta de inversores extranjeros y programas, y no es barata en base de ganancias 2026. Por lo tanto, es mejor considerar dos rutas de entrada.

| Ruta | Condición de verificación |
|---|---|
| Confirmación de soporte | Mantener el mínimo entre 103.700–106.000 KRW y confirmar alivio de venta de inversores extranjeros y programas |
| Confirmación de tendencia | Recuperarse a través de 113.800 KRW en mayor volumen con instituciones o inversores extranjeros girando compradores netos |

La recuperación a través de 121.600–124.000 KRW sustancialmente revertiría daño de tendencia de corto plazo. Inversamente, romper por debajo de 99.600 KRW en base de cierre sin recuperación requeriría reevaluar hipótesis de precio.

### Catalizadores

* Logro de 466,9 mil millones de KRW de ingresos y 47,3 mil millones de KRW de ganancia operativa en ganancias 2Q26
* Comentario de empresa sobre ingresos de SoCAMM, mezcla de placa de capa alta y tasa de utilización
* Lanzamiento real de mercado de servidores basados en Vera de OEM en segunda mitad de 2026
* Especificaciones de producción finales de NVIDIA y expansión de envíos de rack de CPU Vera independiente
* Actualizaciones de producción en masa y calificación del cliente de SK Hynix, Samsung Electronics y Micron para SoCAMM2

### Condiciones de invalidación

* Pedidos repetidos fallan en seguir volumen inicial de SoCAMM
* Capacidad reducida por módulo no se traduce en aumentos de envío de módulos totales
* La participación de mercado específica del cliente de Simmtech confirma por debajo de estimaciones de analistas
* La ganancia operativa 2Q falla materialmente consenso con cargas recurrentes de materia prima y rendimiento
* Retrasos significativos en lanzamiento de sistema Vera Rubin o Vera CPU independiente
* 99.600 KRW rompe por debajo de soporte con expansión concurrente de venta de inversores extranjeros y programas

## 11. Conclusión final

La expansión de suministro de Vera CPU refuerza la tesis de inversión SoCAMM2 de Simmtech. Particularmente, la trayectoria de reducción de capacidad de módulo debido a escasez de LPDDR mientras se aumentan los envíos totales de módulo y CPU es difícil de caracterizar como desfavorable para vendedores de sustrato. Los vendedores de DRAM venden bits y GB; Simmtech vende PCBs que van en cada módulo. Estas son unidades diferentes.

Sin embargo, muchos elementos permanecen sin confirmar. Volúmenes de envío de Vera, módulos finales por CPU, participación de mercado real específica del cliente de Simmtech, ingresos de SoCAMM y margen de ganancia de placa de capa alta no pueden ser finalizados por materiales públicos solamente. Un cálculo como 44 millones de módulos es un escenario útil pero no orientación oficial.

El precio de las acciones actual se ha corregido casi 35% desde el pico, pero no hay evidencia de que la venta de inversores extranjeros y programas haya terminado. Por lo tanto, esta idea debe ser vista como "un candidato de compra condicional que requiere confirmación de ganancias y oferta-demanda" en lugar de "una acción de crecimiento que ha caído bruscamente". El comentario de ganancia operativa 2Q e ingresos de SoCAMM es la primera verificación, y envíos de servidor Vera independiente de segunda mitad de 2026 representan la segunda verificación.

---

## Evidencia y limitaciones

### Hechos confirmados

* Las especificaciones oficiales de NVIDIA presentan 36 CPUs Vera y 54TB de LPDDR5X en NVL72.
* NVIDIA divulgó sistemas de CPU independientes que acomodan hasta 256 CPUs Vera por rack y planes de lanzamiento de OEM para segunda mitad de 2026.
* TrendForce reportó ajustes para reducir la capacidad por módulo mientras se aumentan los envíos totales de módulos y la producción de Vera CPU debido a escasez de LPDRAM.
* SK Hynix anunció producción en masa de SoCAMM2 de 192GB para Vera Rubin.
* Simmtech lista PCB SoCAMM en su lista de productos oficial.
* Cierre de Simmtech del 16 de julio, oferta-demanda y consenso han sido reverificados de base de datos local.

### Estimaciones

* Cálculo anual de 40 a 48 millones de módulos usando suposiciones de 5 a 6 millones de CPUs Vera y 8 módulos por CPU
* Afirmaciones de que Simmtech suministra simultáneamente a tres proveedores de memoria y mantiene alta participación de mercado
* Magnitud del impacto de reducción de capacidad en ingresos y ganancia de Simmtech siguiendo aumento de recuento de módulos

### Elementos no confirmados por materiales públicos

* Orientación oficial de envío de Vera CPU 2027 de NVIDIA
* Módulos de sistema de producción final por CPU y capacidad por módulo
* Ingresos, participación de mercado, precio unitario y margen de ganancia de SoCAMM específico del cliente de Simmtech
* Fecha de anuncio de ganancias 2Q e orientación de ingresos de SoCAMM de la empresa
* Alcance preciso de aplicación de la reducción de capacidad reportada por TrendForce y especificación 1.5TB oficial de NVIDIA

Análisis informativo basado en materiales públicos y datos de mercado local; no consejo de inversión que refleje cronogramas, precios o tolerancia de riesgo de inversores individuales.

*Descargo de responsabilidad: Solo para propósitos de investigación e información. No es consejo de inversión. Los nombres citados son para ilustración analítica; los lectores deben hacer su propia diligencia debida y consultar asesores con licencia antes de cualquier decisión de inversión.*
