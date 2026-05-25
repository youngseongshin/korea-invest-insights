---
title: "Tras NVIDIA, el cuello de botella en semiconductores de IA es el movimiento de datos, HBM, FC-BGA e integridad de potencia"
date: 2026-05-24T19:20:00+09:00
description: "Una síntesis de la entrevista de Dwarkesh Patel con Reiner Pope sobre diseño de chips, la discusión de All-In sobre NVIDIA e infraestructura de IA, y el debate de 20VC sobre los mercados de capital en torno a Anthropic, Cerebras y SpaceX. El punto clave: la infraestructura de IA ya no es solo una historia de GPUs. Los inversores deben seguir el movimiento de datos, HBM, sustratos de encapsulado, Ethernet, enlaces ópticos, integridad de potencia y pruebas. En Corea, la cadena de valor va desde la memoria de Samsung Electronics y SK Hynix hasta los sustratos FC-BGA y condensadores de silicio de Samsung Electro-Mechanics, y de ahí a Daeduck, Isu Petasys, Simmtech, Korea Circuit, TLB y los zócalos de prueba."
categories: ["Market-Outlook"]
tags:
  - "NVIDIA"
  - "Marvell"
  - "Samsung Electro-Mechanics"
  - "Samsung Electronics"
  - "SK Hynix"
  - "HBM"
  - "FC-BGA"
  - "Sustratos para IA"
  - "Infraestructura de IA"
  - "Cadena de valor semiconductora"
slug: ai-chip-design-data-movement-fcbga-bottleneck-2026-05-24
valley_cashtags:
  - NVIDIA
  - Marvell
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - 대덕전자
  - 이수페타시스
  - 심텍
  - 코리아써키트
  - 티엘비
draft: false
---

> Series relacionadas
> [NVIDIA Q1 FY27 e infraestructura de IA coreana](/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [Previsión de resultados de Marvell y Broadcom](/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/) / [Contrato de condensadores de silicio de Samsung Electro-Mechanics por KRW 1,5 billones](/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [MLCC y condensadores de silicio explicados](/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/) / [Tesis de re-valoración de Samsung Electronics](/post/samsung-electronics-tsmc-rerating-thesis-2026-05-16/) / [Hub de PCB y sustratos para IA en Corea](/page/korea-ai-pcb-substrate-hub/)

## Resumen ejecutivo

El más importante de los tres vídeos es la entrevista de Dwarkesh Patel con Reiner Pope. No comienza con titulares de mercado, sino con lo que ocurre realmente dentro de un chip: por dónde fluye la electricidad, dónde residen los datos y con qué frecuencia el chip tiene que moverlos.[^dwarkesh]

El punto clave es sencillo. El rendimiento de la IA no depende solo de los FLOPS. El verdadero cuello de botella está en <strong>de dónde vienen los datos, dónde se almacenan y cuán corto es el camino entre la memoria y el cómputo</strong>. Bajo ese enfoque, NVIDIA sigue siendo central, pero la cadena de inversión se extiende hacia HBM, sustratos de encapsulado, FC-BGA, PCBs de alta densidad de capas, Ethernet, enlaces ópticos, componentes de estabilidad de potencia y pruebas.

Para los inversores coreanos, la lectura es clara. <strong>Samsung Electronics y SK Hynix son el núcleo de memoria. Samsung Electro-Mechanics es el nodo de FC-BGA y condensadores de silicio para la integridad de potencia. Daeduck, Isu Petasys, Simmtech, Korea Circuit y TLB son candidatos de diversificación en sustratos y PCB.</strong> Este no es un mercado para perseguir huecos alcistas del lunes. La clave está en si el volumen de negociación y el flujo extranjero/institucional aguantan hasta la sesión de tarde.

---

## 1. Por qué importa la entrevista con Reiner Pope

Un error frecuente al invertir en semiconductores de IA es leer el rendimiento de un chip como "más FLOPS equivale a un chip mejor." La explicación de Reiner Pope desmonta esa idea desde los fundamentos.

Gran parte del cómputo de IA es multiplicación matricial repetida: multiplicar muchos números, sumarlos y volver a empezar. Acelerar la unidad aritmética importa, pero a nivel de chip la pregunta más relevante suele ser <strong>de dónde vienen los números</strong>.

Un chip de IA tiene varias capas de almacenamiento y movimiento de datos.

| Ubicación | Descripción en lenguaje llano | Traducción a inversión |
|---|---|---|
| Registros y SRAM | El banco de trabajo dentro del chip | Muy rápidos, pero el área es cara |
| HBM | El almacén de alta velocidad junto a la GPU | Cuello de botella de ancho de banda; SK Hynix y Samsung Electronics |
| Sustrato de encapsulado / interposer | El suelo que conecta chips y memoria | FC-BGA, ABF, sustratos avanzados |
| Placa de servidor y red | Las carreteras dentro y fuera del rack | PCB de alta densidad de capas, Ethernet, enlaces ópticos |
| Potencia en el centro de datos | La electricidad de todo el sistema | Transformadores, distribución, refrigeración, coste operativo total |

Si la unidad aritmética espera datos, el chip está infrautilizado. Así que la pregunta real sobre chips de IA no es solo "¿podemos añadir más cómputo?" Es: <strong>"¿podemos mover menos datos, mantenerlos más cerca y alimentar el chip sin desperdiciar potencia?"</strong>

Por eso HBM, FC-BGA, condensadores de silicio y PCBs de alta velocidad forman parte de la misma conversación. Todos resuelven el mismo problema físico: <strong>mantener los chips de IA alimentados con datos y con potencia estable</strong>.

---

## 2. Por qué el cómputo de baja precisión conduce a sustratos y potencia

El argumento de Reiner Pope sobre la baja precisión no es simplemente que FP8 o FP4 dupliquen la velocidad. Una precisión menor también cambia el área, el número de conductores y la potencia consumida. Menos bits implican circuitos más pequeños, menos conmutaciones y menos energía por operación.

Esto importa para los inversores porque la baja precisión no es solo una característica de las GPUs de NVIDIA. Si se empaqueta más cómputo dentro del mismo presupuesto de potencia, todo el sistema debe evolucionar.

| Cambio tecnológico | Requisito del sistema | Vínculo con la cadena de suministro coreana |
|---|---|---|
| Adopción de FP8 y FP4 | Más cómputo dentro del mismo presupuesto de potencia | HBM4, DRAM de servidor, SOCAMM |
| Diseños estilo Tensor Core / systolic-array | Menos movimiento de datos dentro del chip | HBM e interconexión de encapsulado |
| GPUs y ASICs de mayor tamaño | Formatos de die y encapsulado más grandes | FC-BGA, ABF, sustratos avanzados |
| Expansión a escala de rack | Mayor ancho de banda chip a chip y rack a rack | PCB de alta densidad de capas, Ethernet, enlaces ópticos |
| Mayor densidad de potencia | Respuesta más rápida a variaciones de corriente y ruido de tensión | MLCC, condensadores de silicio |

Así, el valor en semiconductores de IA no termina en el proveedor de GPUs. NVIDIA ancla el sistema. Marvell y Broadcom se sitúan en chips de IA personalizados, conectividad, Ethernet y enlaces ópticos. La memoria, los sustratos y los componentes de estabilidad de potencia coreanos se conectan por debajo.

---

## 3. Los números de NVIDIA son sólidos. La pregunta del mercado ha cambiado

NVIDIA comunicó ingresos de <strong>$81.600 millones</strong> en el primer trimestre del ejercicio FY27, ingresos del segmento Data Center de <strong>$75.200 millones</strong> y una guía de ingresos para el segundo trimestre de <strong>$91.000 millones ±2%</strong>. Según los datos oficiales, la demanda de infraestructura de IA no ha dado señales de agotamiento.[^nvidia]

Pero el mercado ya no pregunta únicamente "¿es buena NVIDIA?" Eso ya está descontado. Las nuevas preguntas son:

1. ¿Se convertirá este capex en ingresos y flujo de caja libre para los clientes en la nube?
2. ¿Pueden resolverse los cuellos de botella de potencia y refrigeración en los centros de datos?
3. ¿Podrán las compañías de modelos seguir pagando facturas elevadas por tokens?
4. ¿El rechazo a la IA y la regulación ralentizarán el despliegue?

El episodio de All-In encaja en este cubo. Anthropic, Karpathy, SpaceX, los resultados de NVIDIA y la regulación de la IA son parte de un problema mayor: <strong>la IA no ha terminado, pero ahora tiene que demostrar eficiencia de capital</strong>.[^allin]

En lenguaje de mercado:

| Marco 2023-2025 | Marco 2026 en adelante |
|---|---|
| Las GPUs escasean | El movimiento de datos y la potencia a escala de rack escasean |
| El HBM escasea | HBM + sustratos + integridad de potencia + redes escasean conjuntamente |
| Los modelos de IA mejoran | El uso de la IA debe convertirse en ingresos y flujo de caja |
| Compra NVIDIA | Sigue los cuellos de botella debajo de NVIDIA |

---

## 4. Marvell y Broadcom: la conectividad se convierte en la próxima prueba

Marvell y Broadcom son los próximos eventos de resultados que hay que observar desde este enfoque. Ninguno de los dos es simplemente un "competidor de NVIDIA." A medida que los centros de datos de IA escalan, ambas se conectan a <strong>conectividad, switching, señales ópticas y silicio de IA personalizado</strong>.

Para Marvell, la pregunta central es si el silicio de IA personalizado y la conectividad óptica están acelerando hacia ingresos reales. Para Broadcom, la pregunta central es si los ASICs de IA y las redes Ethernet para IA están escalando conjuntamente. Si ambas compañías suenan sólidas, la lectura coreana debería ampliarse más allá del HBM puro.

| Señal de EE. UU. | Lectura coreana |
|---|---|
| Demanda de chips de IA personalizados | HBM, sustratos de encapsulado, pruebas |
| Crecimiento de Ethernet y switches para IA | Isu Petasys, PCB de alta velocidad, materiales de baja pérdida |
| Enlaces ópticos y fotónica de silicio | Exposición óptica selectiva; beneficios indirectos en sustratos y potencia |
| Expansión a escala de rack | Equipos de potencia, refrigeración, coste operativo del centro de datos |
| Encapsulados de mayor tamaño | FC-BGA de Samsung Electro-Mechanics, Daeduck, Korea Circuit |

La traducción correcta no es "si Broadcom / Marvell van bien, todos los semis coreanos van bien." Es: <strong>el crecimiento en chips de IA beneficia a los proveedores de los cuellos de botella que alimentan, conectan, estabilizan y prueban esos chips</strong>.

---

## 5. Lo que confirma la noticia de AT&S

El 21 de mayo de 2026, AT&S anunció una expansión de capacidad para sustratos IC de alta gama destinados a IA en su planta de Chongqing, China. La inversión se sitúa en la parte alta de los dos dígitos en millones de euros y está respaldada por acuerdos a largo plazo con clientes. AT&S espera un efecto positivo en el EBIT de la misma magnitud durante el ejercicio 2026/27.[^ats-capacity]

El punto clave no es el nombre del cliente. El punto clave es que <strong>la capacidad de sustratos para IA está siendo ampliada ya bajo acuerdos a largo plazo</strong>.

AT&S también encuadró en abril los sustratos de núcleo de vidrio como la base de próxima generación para IA, computación de alto rendimiento, comunicaciones de alta velocidad y fotónica. A medida que los encapsulados se vuelven más grandes y complejos, la estabilidad dimensional, la calidad de la señal, la eficiencia de potencia y el movimiento de datos se convierten en factores limitantes.[^ats-glass]

Esto encaja directamente con la entrevista de Reiner Pope. Si el cuello de botella de la IA es el movimiento de datos, los sustratos y encapsulados avanzados ya no son componentes pasivos. Se convierten en infraestructura de rendimiento.

---

## 6. Traducción al mercado bursátil coreano

### 6.1 Samsung Electronics y SK Hynix: el núcleo de memoria

Reducir el coste del movimiento de datos requiere HBM y memoria de servidor. Sea cual sea el acelerador, una GPU o un ASIC personalizado, el silicio de IA de alto rendimiento consume ancho de banda de memoria.

SK Hynix es la exposición más directa a HBM. Samsung Electronics es una opción más amplia: recuperación de HBM, HBM4, DRAM de servidor, SOCAMM, eSSD y opcionalidad en fundición. Pero Samsung sigue necesitando pruebas de ejecución: cualificación con clientes, rendimiento de fabricación y victorias visibles en silicio de IA.

### 6.2 Samsung Electro-Mechanics: FC-BGA más condensadores de silicio

Samsung Electro-Mechanics es uno de los cuellos de botella coreanos de segundo orden más claros en este marco.

Primero, el FC-BGA es el sustrato de encapsulado que conecta los chips de alto rendimiento a la placa. GPUs más grandes, CPUs, chips de IA personalizados y ASICs de switching necesitan sustratos avanzados.

Segundo, los condensadores de silicio estabilizan la potencia dentro del encapsulado AI GPU / HBM. Samsung Electro-Mechanics anunció en mayo de 2026 un contrato de suministro de condensadores de silicio por aproximadamente KRW 1,5 billones con un gran cliente global, y describió el producto como un componente que mejora la estabilidad de potencia dentro de encapsulados de semiconductores de alto rendimiento como GPUs para servidores de IA y HBM.[^semco-sicap]

El punto no es "más contenido de MLCC." El punto es que Samsung Electro-Mechanics podría ser reclasificada como <strong>una compañía de sustratos con componentes de integridad de potencia dentro del encapsulado</strong>.

### 6.3 Daeduck, Isu Petasys, Simmtech, Korea Circuit y TLB

Estos nombres no deben agruparse de forma demasiado laxa.

| Grupo | Qué observar | Riesgo |
|---|---|---|
| Daeduck Electronics | FC-BGA, sustratos de encapsulado, sustratos para chips de IA | Pruebas con clientes, rendimiento, utilización |
| Isu Petasys | PCB de networking de alta densidad de capas | Confirmación de flujo tras un rally pronunciado |
| Simmtech / TLB | Módulos de memoria, SoCAMM, PCB de servidor | Mix de ingresos de IA y prueba de márgenes |
| Korea Circuit | Opcionalidad en SoCAMM y FC-BGA | Cualificación y calendario de ingresos reales |

La etiqueta "exposición a servidores de IA" no es suficiente. La evidencia que necesitan los inversores es <strong>suministro directo, incremento de precio medio de venta, acuerdos a largo plazo y resiliencia de márgenes</strong>.

---

## 7. Lo que muestra 20VC sobre la temperatura del mercado de capitales

El episodio de 20VC debatió sobre Anthropic, la incorporación de Karpathy a Anthropic, Cerebras, SpaceX y el coste de los tokens de IA.[^twentyvc] Esto tiene menos que ver con la física de los semiconductores y más con la temperatura del mercado de capitales.

La señal positiva es que los inversores siguen dispuestos a financiar historias de infraestructura de IA y hardware de IA. El apetito por la financiación de laboratorios de modelos, las OPVs de hardware de IA y las expectativas de grandes OPVs tecnológicas siguen vivos.

La señal negativa es el riesgo de concentración. Demasiado capital se está agrupando alrededor de un número pequeño de megacompañías de IA e infraestructura. El gasto privado en modelos de IA tendrá que pasar, en última instancia, por el escrutinio de los mercados públicos, los presupuestos de capex de las grandes tecnológicas o ingresos reales.

Por tanto, la conclusión de 20VC no es "compra exposición privada a IA." Es: <strong>el apetito por el riesgo en IA está vivo, pero el mercado exigirá cada vez más pruebas de monetización y generación de flujo de caja</strong>.

---

## 8. Lista de verificación práctica

Para el mercado coreano la semana que viene, la pregunta no es solo si Samsung Electronics y SK Hynix suben. La mejor señal es si el dinero se mueve hacia los escalones inferiores de la cadena.

| Orden | Punto de control | Significado |
|---:|---|---|
| 1 | Samsung Electronics y SK Hynix aguantan con volumen | Núcleo de memoria confirmado |
| 2 | Samsung Electro-Mechanics y Daeduck aguantan tras la apertura | Re-valoración de FC-BGA e integridad de potencia |
| 3 | Isu Petasys, Simmtech, TLB y Korea Circuit participan | Diversificación hacia PCB y SoCAMM |
| 4 | El flujo extranjero e institucional aguanta hasta la tarde | Dinero real, no solo operativa temática |
| 5 | Equipos de potencia e infraestructura de centros de datos se unen | Extensión plena del cuello de botella de infraestructura de IA |

La disciplina de entrada es fundamental.

| Condición | Lectura |
|---|---|
| Hueco alcista en apertura con volumen débil | No perseguir |
| Aguante por la tarde con compras extranjeras/institucionales | Ampliar la lista de seguimiento |
| PCBs suben mientras las megacaps de memoria caen | Más probable que sea temático |
| Secuencia memoria → sustratos → equipos de potencia | Señal de extensión del cuello de botella |
| Etiqueta "IA" sin ingresos ni pedidos | Evitar |

---

## 9. Conclusión

Los tres vídeos se condensan en una sola frase:

<strong>El trade de IA no ha terminado. Se está desplazando hacia los escalones inferiores de la cadena.</strong>

2023-2025 fue la fase de GPUs y HBM. A partir de 2026, las siguientes capas son el movimiento de datos, el encapsulado, el FC-BGA, Ethernet y los enlaces ópticos, la integridad de potencia, las pruebas y el coste operativo de los centros de datos. NVIDIA sigue siendo el centro. Pero la pregunta del inversor ahora es: "¿qué cuello de botella coreano convierte el crecimiento de ingresos de NVIDIA en sus propios beneficios?"

El orden actual es:

1. <strong>Núcleo de memoria:</strong> Samsung Electronics, SK Hynix
2. <strong>Encapsulado e integridad de potencia:</strong> Samsung Electro-Mechanics, Daeduck Electronics
3. <strong>PCB de alta velocidad y módulos:</strong> Isu Petasys, Simmtech, Korea Circuit, TLB
4. <strong>Pruebas y zócalos:</strong> ISC, LEENO Industrial, TSE
5. <strong>Potencia y operaciones de centros de datos:</strong> equipos de potencia e infraestructura de refrigeración

La frase de inversión más importante es esta: <strong>la competencia en rendimiento de IA es una competencia en coste de movimiento de datos, y ese coste se traduce en HBM, encapsulado, sustratos, redes y potencia.</strong>

Si esa extensión se confirma con volumen y flujo extranjero/institucional, el FC-BGA y el PCB de alta velocidad deben tratarse como cuellos de botella de infraestructura de IA, no como un simple tema de moda.

---

## Clasificación de evidencias

### [Hecho]

- La entrevista de Dwarkesh Patel con Reiner Pope explica el diseño de chips de IA a través de operaciones MAC, movimiento de datos, aritmética de baja precisión, estructuras Tensor Core / systolic-array y coste operativo total.[^dwarkesh]
- NVIDIA comunicó ingresos de $81.600 millones en el primer trimestre del ejercicio FY27, ingresos del segmento Data Center de $75.200 millones y una guía de ingresos para el segundo trimestre de $91.000 millones ±2%.[^nvidia]
- AT&S anunció el 21 de mayo de 2026 la expansión de capacidad de sustratos IC de alta gama para IA basada en acuerdos a largo plazo con clientes.[^ats-capacity]
- Samsung Electro-Mechanics anunció un contrato de suministro de condensadores de silicio por aproximadamente KRW 1,5 billones y describió los condensadores de silicio como componentes de estabilidad de potencia para encapsulados de GPU de servidor de IA y HBM.[^semco-sicap]

### [Inferencia]

- El cuello de botella en chips de IA está migrando desde las unidades aritméticas hacia el movimiento de datos y la integridad de potencia.
- Los sólidos resultados de NVIDIA podrían fluir hacia Corea no solo a través del HBM, sino también del FC-BGA, el PCB de alta velocidad, los condensadores de silicio y los zócalos de prueba.
- Los resultados de Marvell y Broadcom son verificaciones clave para determinar si "chips de IA personalizados + cuellos de botella de conectividad" se están convirtiendo en números reales.

### [Sin confirmar]

- El nombre del cliente clave de AT&S y el mix exacto de productos.
- Si compañías específicas de sustratos y PCB coreanas suministran directamente a los programas de NVIDIA, Marvell o Broadcom.
- El cliente, el margen del producto y la ubicación exacta dentro del encapsulado del condensador de silicio de Samsung Electro-Mechanics.
- Confirmación oficial de varias valoraciones de compañías privadas y cifras de financiación comentadas en All-In y 20VC.

[^dwarkesh]: Dwarkesh Patel, "Chip design from the bottom up / Reiner Pope," YouTube, 2026-05-22. https://www.youtube.com/watch?v=oIk3R-sMX5o
[^allin]: All-In Podcast, "SpaceX's $2T case, Nvidia's shock selloff, America turns on AI," YouTube, 2026-05-22. https://www.youtube.com/watch?v=HGbA6ze0_3M
[^twentyvc]: 20VC, "Andrej Karpathy joins Anthropic / Cerebras / SpaceX," YouTube, 2026-05-21. https://www.youtube.com/watch?v=z94zlbVn048
[^nvidia]: NVIDIA Investor Relations, "NVIDIA Announces Financial Results for First Quarter Fiscal 2027," 2026-05-20. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027
[^ats-capacity]: I-Connect007, "AT&S Expands Capacity for AI Substrates," 2026-05-21. https://iconnect007.com/article/150109/ats-expands-capacity-for-ai-substrates/150106/pcb
[^ats-glass]: AT&S, "AT&S advances glass core substrates for AI, high-performance computing and photonics," 2026-04-22. https://ats.net/en/press/ats-advances-glass-core-substrates-for-ai-high-performance-computing-and-photonics/
[^semco-sicap]: Samsung Electro-Mechanics, "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract with Global Large-Scale Company," 2026-05-20. https://samsungsem.com/global/newsroom/news/view.do?id=10310

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
