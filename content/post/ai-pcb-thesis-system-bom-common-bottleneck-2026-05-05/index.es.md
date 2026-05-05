---
title: "Tesis de PCB y Sustratos para IA: GPU, CPU, NIC y CCL Son un Solo Cuello de Botella del Sistema"
slug: ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05
date: 2026-05-05T23:15:00+09:00
description: "El mercado suele presentar el hardware de IA como una secuencia: primero GPU, luego memoria, luego sustratos. Eso es solo parcialmente correcto. La infraestructura de IA es hoy un sistema a escala de rack compuesto por GPUs, CPUs, DPUs, NICs, ASICs de switch, módulos de memoria, placas de potencia y CCL de baja pérdida. Cada expansión de chips necesita una placa. Esta tesis sectorial conecta a Samsung Electro-Mechanics, Daeduck Electronics, Doosan Electronic BG, Kolon Industries y Pamicell con el mismo cuello de botella a nivel de sistema."
categories: ["Sector-Deep-Dive", "Korea Market"]
tags:
  - "PCB para IA"
  - "sustratos para IA"
  - "FC-BGA"
  - "MLB"
  - "CCL"
  - "IA agéntica"
  - "IA física"
  - "demanda de CPU"
  - "NVIDIA Vera Rubin"
  - "IA a escala de rack"
  - "Samsung Electro-Mechanics"
  - "Daeduck Electronics"
  - "Doosan"
  - "Kolon Industries"
  - "Pamicell"
  - "acciones de Corea"
series: ["ai-pcb-substrate-thesis-2026"]
---

> **Mapa sectorial:** Esta es la tesis de nivel superior sobre PCB y sustratos para IA que sustenta el análisis de Pamicell. Léela junto con el [hub de PCB para IA](/page/korea-ai-pcb-substrate-hub/), [Pamicell Parte 1](/post/pamicell-doosan-electro-bg-proxy-rediscovery-2026-04-30/), [Pamicell Parte 2](/post/pamicell-four-layer-progress-and-fifth-cycle-layer-2026-05-03/), y la anterior [nota de re-valoración de Samsung Electro-Mechanics en infraestructura de IA](/post/samsung-electro-mechanics-ai-infrastructure-rerating-2026-04-21/).

Los análisis previos a nivel de empresa planteaban una pregunta más acotada: ¿qué nombres coreanos tienen la mejor posición en suministro de PCB para IA, FC-BGA y materiales de baja pérdida? Esta nota sube un nivel. Se pregunta por qué el capital debería entrar al ecosistema completo en primer lugar.

La respuesta no es "los sustratos son el próximo tema después de las GPUs." Eso es demasiado lineal. La infraestructura de IA ya no es una tarjeta GPU. Es un sistema a escala de rack. Un rack de IA moderno contiene GPUs, CPUs, DPUs, NICs, ASICs de switch, módulos de memoria, distribución de potencia, control de refrigeración y placas de alta velocidad. Cada capa añade silicio. Cada pieza de silicio necesita un sustrato de encapsulado, una placa de módulo, una placa base, una placa de switch o un apilado de material de baja pérdida.

Ese es el punto central: la capa de PCB y sustratos no es la siguiente parada en una rotación simple. Es el denominador común de toda la lista de materiales del sistema de IA.

---

## Resumen ejecutivo

1. La secuencia del mercado de "GPU a memoria a sustratos" es útil como orientación, pero incompleta. El marco más preciso es la expansión simultánea del sistema: GPU, HBM, CPU, DPU, NIC, ASIC de switch y módulos de memoria crecen juntos, y todos requieren sustratos o placas.
2. El NVIDIA Vera Rubin NVL72 ilustra el punto con claridad. La plataforma combina 72 GPUs Rubin, 36 CPUs Vera, switching NVLink 6, SuperNICs ConnectX-9, DPUs BlueField-4 y escalado Ethernet Spectrum-X / Spectrum-6. La ratio CPU:GPU es 0,5, es decir, una CPU por cada dos GPUs. Esto ya no es una historia de un solo chip.
3. La IA agéntica eleva la intensidad de CPU en inferencia. La orquestación de herramientas, recuperación de información, ejecución de código, acceso a bases de datos, gestión de memoria y aislamiento de seguridad dependen de CPUs, DRAM, NICs y DPUs. Si el contenido de CPU aumenta, el FC-BGA de CPU para servidores, las placas de módulos de memoria, SoCAMM, las placas base y el CCL de baja pérdida se ven arrastrados.
4. La IA física extiende la tesis fuera del centro de datos. Vehículos autónomos, humanoides, robots industriales y electrónica espacial utilizan más placas, más sensores, más módulos de IA en el borde y más materiales PCB sensibles a la fiabilidad. La curva temporal es diferente: primero los centros de datos, después la conducción autónoma, luego los humanoides y, finalmente, el espacio como prima de margen de alta fiabilidad.
5. Para Corea, el mapa de inversión se vuelve estratificado. Samsung Electro-Mechanics es el nodo de FC-BGA de alta gama más MLCC. Daeduck Electronics es el candidato al factor FC-BGA / MLB / SoCAMM. Doosan Electronic BG es el ancla del CCL. Kolon Industries y Pamicell se ubican aguas arriba en materiales de baja dieléctrica. Pamicell no es solo una tesis de inversión aislada; es un proxy comprimido dentro de un sistema más amplio de sustratos para IA.

---

## 1. El Marco Lineal: Útil, Pero Insuficiente

Al mercado le gustan las secuencias porque son fáciles de operar.

Primero llegaron las GPUs: NVIDIA capturó el presupuesto porque los aceleradores escaseaban. Luego llegó HBM: las GPUs no podían escalar sin ancho de banda de memoria, así que SK hynix, Samsung Electronics y Micron pasaron al centro del debate. El siguiente paso suele describirse como sustratos o empaquetado avanzado: si las GPUs y la HBM escalan, entonces FC-BGA, interposers, MLBs y CCL deberían seguir.

Ese marco no está equivocado. Una GPU más grande necesita un sustrato de encapsulado más grande y complejo. La expansión de HBM intensifica el empaquetado. Las placas de servidores se vuelven más densas y rápidas. Desde ese ángulo, los sustratos sí llegan después de las GPUs y la HBM en el ciclo de reconocimiento.

Pero el marco pasa por alto el cambio más importante en la arquitectura del sistema. La infraestructura de IA en 2026 no es una pila de GPUs. Es una plataforma a escala de rack que codiseña cómputo, memoria, redes, seguridad y control del sistema.

La configuración NVIDIA Vera Rubin NVL72 es el ejemplo más claro. Los materiales públicos de NVIDIA describen un sistema construido en torno a 72 GPUs Rubin y 36 CPUs Vera, con switching NVLink 6, SuperNICs ConnectX-9 y DPUs BlueField-4. Los propios materiales de la plataforma Rubin de NVIDIA también enmarcan la plataforma como un codiseño de seis chips: CPU Vera, GPU Rubin, switch NVLink, SuperNIC ConnectX-9, DPU BlueField-4 y switch Ethernet Spectrum-6.

La aritmética importa:

```text
CPUs Vera  = 36
GPUs Rubin = 72
CPU:GPU    = 36 / 72 = 0,5
```

Una CPU por cada dos GPUs no es un detalle trivial del procesador anfitrión. Indica que el rack es un sistema, no un estante de GPUs. Una vez que eso es cierto, la tesis de sustratos deja de ser un eco secundario de la demanda de GPU. Se convierte en una tesis de sistema multichip.

---

## 2. Por Qué Cada Chip Requiere una Placa

La forma más sencilla de ver la capa de sustratos es recorrer la lista de materiales del sistema.

| Capa del sistema | Chip o módulo | Demanda de placa / sustrato |
|---|---|---|
| Aceleración de IA | GPU, ASIC personalizado, TPU | FC-BGA grande, sustrato de encapsulado avanzado, placa de alta densidad |
| Host y orquestación | CPU de servidor, CPU Vera, CPU x86 / Arm | FC-BGA grande, placa de socket CPU, MLB de placa base |
| Ancho de banda de memoria | HBM, DDR5, módulos de servidor basados en LPDDR, SoCAMM | Interposer / sustrato, PCB de módulo de memoria, material de integridad de señal |
| Redes | NIC, SuperNIC, ASIC de switch Ethernet, switch InfiniBand | Placa de switch, PCB de módulo óptico, MLB de baja pérdida |
| Movimiento de datos y seguridad | DPU, SmartNIC | Sustrato de encapsulado, PCB de tarjeta aceleradora |
| Potencia y control | VRM, módulos de potencia, BMC y placas de control | PCB de potencia, MLCC, placa de alta fiabilidad |

Por eso "demanda de GPU" es demasiado estrecho. Un hiperescalador no compra una GPU de forma aislada. Compra un rack funcional. Ese rack contiene chips de cómputo, chips de memoria, chips de red, chips de control y electrónica de potencia. Cuanto más crece el sistema, más se exige a la capa de placas para transportar señales de alta velocidad, calor, potencia y fiabilidad.

La traducción para la renta variable coreana también es más clara bajo este marco:

| Capa coreana | Empresas a seguir | Lo que representan |
|---|---|---|
| Sustrato de encapsulado de alta gama | Samsung Electro-Mechanics, Daeduck Electronics, Korea Circuit | Exposición a FC-BGA y sustrato de encapsulado |
| Placa multicapa y PCB de módulo | Isu Petasys, Daeduck Electronics, TLB, Simmtech, Korea Circuit | Exposición a placa base de servidor, placa de switch, módulo de memoria y SoCAMM |
| Ancla de CCL | Doosan Electronic BG | Laminado recubierto de cobre de alta gama para servidores de IA y redes |
| Materiales de baja pérdida | Kolon Industries, Pamicell | Insumos de resina mPPO / de baja dieléctrica y endurecedores |
| Estabilidad de potencia | Samsung Electro-Mechanics y pares de MLCC | Contenido de MLCC por servidor de IA y mix de componentes de alta tensión |

Pamicell pertenece a este mapa como un proxy de material aguas arriba de Doosan Electronic BG. Samsung Electro-Mechanics pertenece como el nodo coreano de gran capitalización premium en FC-BGA y MLCC. Daeduck pertenece como el candidato al factor más amplio de FC-BGA / MLB / SoCAMM. No son historias separadas. Son puntos distintos en la misma lista de materiales del sistema.

---

## 3. La IA Agéntica Amplía la Capa de CPU

La inferencia de LLM tradicional lucía simple desde la óptica del hardware:

```text
prompt
  -> paso hacia adelante en GPU
  -> respuesta
```

La IA agéntica cambia la carga de trabajo. El modelo no solo responde. Planifica, llama herramientas, busca, lee archivos, ejecuta código, consulta bases de datos, gestiona memoria, verifica resultados y puede coordinarse con otros agentes. La GPU sigue siendo central, pero el trabajo fuera de la GPU se vuelve mucho más pesado.

| Función agéntica | Principal tirón de hardware |
|---|---|
| Paso hacia adelante del LLM | GPU + HBM |
| Orquestación de herramientas | CPU |
| Recuperación y búsqueda | CPU + DRAM + almacenamiento |
| Ejecución de código | CPU, sandbox, compilador / intérprete |
| Memoria de sesión y estado | CPU + DRAM |
| Llamadas a herramientas en red | NIC + ASIC de switch + PCB |
| Seguridad y aislamiento | CPU + DPU |

TrendForce ha sido explícito sobre esta dirección. Su informe de IA agéntica de abril de 2026 y comentarios públicos relacionados describen un cambio estructural en las ratios CPU:GPU, ajuste en el suministro de CPU para servidores y aumentos de precios por parte de Intel y AMD. Tom's Hardware reportó la misma tendencia desde el lado de la industria: configuraciones de servidores de IA que antes usaban una CPU por cada cuatro a ocho GPUs pueden evolucionar hacia una intensidad de CPU mucho mayor en escenarios de inferencia agéntica.

La ratio exacta variará según la carga de trabajo. Un clúster de agentes de código no es igual a un clúster de generación de vídeo. Un agente empresarial con mucha recuperación de información no es igual a un sistema de inferencia por lotes puro. Pero la dirección es lo que importa para los inversores en sustratos: más trabajo de CPU significa más encapsulados de CPU, más memoria en torno a la CPU, más redes y más requisitos de integridad de señal a nivel de placa.

El camino de la IA agéntica a los sustratos coreanos luce así:

```text
Adopción de IA agéntica
  -> la carga de trabajo de orquestación en CPU aumenta
  -> el contenido de CPU de servidor, DPU, NIC y ASIC de switch crece
  -> la demanda de FC-BGA de CPU de servidor y MLB de alta capa sube
  -> la complejidad de módulos de memoria, SoCAMM y placas base aumenta
  -> el CCL de baja pérdida y los materiales de baja dieléctrica ganan importancia
  -> las empresas coreanas de sustratos y materiales reciben una porción de la expansión de la lista de materiales
```

Esa última línea es importante. Corea no es dueña del mercado de CPUs. Intel, AMD, Arm, NVIDIA y las CPUs personalizadas de proveedores de servicios en la nube capturan el valor del chip. Las empresas coreanas cotizadas capturan el contenido de placa y material en torno al chip. Esto sigue siendo significativo porque el contenido de sustrato crece con el sistema, no con una sola línea de productos.

---

## 4. IA Física: Fuera del Centro de Datos

El centro de datos es el primer y más grande impulsor a corto plazo. La IA física es la segunda vía de expansión. El horizonte temporal es más largo, pero la dirección es consistente: cuando la inteligencia se traslada a vehículos, robots, fábricas y satélites, más cómputo se acerca al borde. Más cómputo en el borde significa más placas.

### Conducción autónoma

La conducción autónoma es la segunda fase más realista porque los vehículos ya utilizan grandes pilas electrónicas. Un vehículo con asistencia avanzada al conductor o funciones autónomas contiene cómputo central, fusión de sensores, módulos de cámara, radar, lidar, Ethernet vehicular y controladores de seguridad redundantes.

| Sistema del vehículo | Tirón de PCB y material |
|---|---|
| Cómputo central | Placa de alta densidad, sustrato de encapsulado del procesador |
| ECU de fusión de sensores | PCB multicapa, placa de señal de alta velocidad |
| Cámara / lidar / radar | Rígido-flexible, placa RF, PCB de módulo |
| Ethernet vehicular | CCL de baja pérdida y PCB de comunicación de alta velocidad |
| Redundancia de seguridad | Más ECUs y más área de placa |

Esto no impacta los resultados tan rápido como los centros de datos de IA. Los programas de vehículos requieren tiempo, la calificación es lenta y la curva de ingresos depende del ciclo de modelo. Pero la dirección no es ambigua: un vehículo más inteligente lleva más contenido de placa que uno tradicional.

### Robótica humanoide e industrial

NVIDIA Jetson Thor aporta una referencia concreta de hardware para el argumento de IA física. NVIDIA posiciona Jetson Thor para IA física y robótica, con hasta 2.070 FP4 TFLOPS, 128 GB de memoria y un rango de potencia configurable de 40 W a 130 W. Ese tipo de módulo de IA en el borde necesita placas de alta densidad, placas de potencia, interconexión de sensores y PCBs flexibles.

Los humanoides no impulsarán las ganancias coreanas de sustratos mañana. Todavía no son un mercado de volumen masivo. Pero amplían el valor opcional de la tesis. Si los módulos de IA en el borde se estandarizan en robots, fábricas y máquinas industriales, el contenido de placas pasa de ser una historia exclusiva de centros de datos a una historia de cómputo distribuido.

### Electrónica espacial y de defensa

El espacio es diferente. No es una historia de volumen. Es una historia de fiabilidad y margen. Los materiales de NASA e IPC para hardware de misión enfatizan los requisitos de PCB de alta fiabilidad, calificación de proveedores y estándares tipo Clase 3 / adéndum espacial. Para los nombres coreanos de PCB cotizados, la relevancia no es que el espacio absorba capacidad masiva. Es que la electrónica para entornos exigentes puede justificar mayores estándares de fiabilidad y potencialmente mejores márgenes.

La curva temporal luce así:

| Mercado final | Timing de ganancias | Intensidad de PCB | Confianza práctica |
|---|---|---|---|
| Centro de datos de IA | Rápido | Muy alta | Alta |
| Conducción autónoma | Medio | Alta | Media a alta |
| Humanoides / robótica | Lento | Media a alta | Media |
| Electrónica espacial / defensa | Lento | Alta especificación, bajo volumen | Media |

Este ordenamiento importa. El modelo a corto plazo aún debe estar liderado por centros de datos. La IA física no es una razón para estirar cada valoración hoy. Es una razón por la que el mercado terminal puede ser más amplio de lo que el ciclo actual de servidores de IA implica.

---

## 5. Lo Que Esto Añade a la Tesis de Pamicell

El trabajo sobre Pamicell comenzó con una brecha de reconocimiento específica de la empresa. El mercado recordaba una compañía de células madre. El estado de resultados empezaba a parecerse cada vez más a un proveedor de materiales CCL para IA. El vínculo con Doosan Electronic BG, la reiterada evidencia de contratos de suministro, los bioquímicos de alto margen y la reclasificación industrial por parte de KRX apuntaban todos en la misma dirección.

Esta tesis sectorial cambia la pregunta de "¿por qué Pamicell?" a "¿por qué importa la capa de material CCL aguas arriba?"

La respuesta es que el CCL y los materiales de baja pérdida no están ligados a una sola generación de GPU. Se ubican bajo la capa del sistema:

```text
Expansión de GPU / CPU / DPU / NIC / ASIC de switch
  -> las restricciones de señal de alta velocidad y térmicas aumentan
  -> la demanda de CCL de baja pérdida crece
  -> los productores de CCL necesitan materiales de baja dieléctrica
  -> los proveedores aguas arriba como Pamicell se convierten en proxies comprimidos
```

Pamicell sigue sin ser igual a Doosan Electronic BG, y tampoco es un fabricante de PCB. Está más aguas arriba. Eso significa que la concentración de clientes y el riesgo de calificación son reales. Pero también significa que el pequeño tamaño de la empresa puede hacer que la misma demanda a nivel de sistema luzca más poderosa en términos porcentuales si los pedidos siguen acumulándose.

Dicho de otra manera: la tesis de Pamicell se vuelve más duradera si el ciclo de placas para IA no es simplemente un ciclo de sustratos para GPU, sino un ciclo de sustratos de sistema multichip.

---

## 6. Lo Que Esto Añade a la Tesis de Samsung Electro-Mechanics

Samsung Electro-Mechanics ya fue re-valorada en torno a dos ideas: FC-BGA de alta gama y MLCC para servidores de IA. Ese marco anterior sigue funcionando. La tesis del BOM de sistema lo hace más claro.

Si el único motor fueran las GPUs, Samsung Electro-Mechanics sería una historia de sustrato de encapsulado de alta gama con MLCC adjunto. Si el motor es la expansión de sistema a escala de rack, la empresa ocupa más de un carril:

| Carril | Por qué importa |
|---|---|
| FC-BGA | Las CPUs, GPUs, ASICs y chips de red más grandes y complejos necesitan sustratos de encapsulado de alta gama |
| MLCC | Los servidores de IA, bandejas de redes y distribución de potencia aumentan la densidad de componentes |
| Opción de sustrato de vidrio | La futura arquitectura de encapsulado grande puede requerir nuevos materiales y procesos de sustrato |
| Electrónica automotriz y de robótica | La IA física aumenta la demanda de componentes y placas de alta fiabilidad con el tiempo |

Esto no elimina la disciplina de valoración. Samsung Electro-Mechanics ya ha sido reconocida por el mercado más que Pamicell o algunos nombres más pequeños de PCB. La pregunta del factor no es "¿es esta una buena empresa?" Es "¿cuánto de la expansión de sustratos a nivel de sistema ya está en el precio, y cuánto debe confirmarse a través de pedidos, márgenes y guidance?"

Por eso esta nota trata a Samsung Electro-Mechanics como el ancla premium en lugar de la idea de mayor beta. Es la expresión coreana de gran capitalización más limpia de FC-BGA más MLCC, pero su retorno futuro depende de continuas revisiones al alza de estimados en lugar de simplemente descubrir el tema.

---

## 7. Marco de Cartera: Ancla, Barra y Opciones

El ranking de empresas puede cambiar con el precio, pero el mapa de factores es estable.

| Rol | Exposición candidata | Razón |
|---|---|---|
| Ancla premium | Samsung Electro-Mechanics | FC-BGA + MLCC + calificación de clientes + escala |
| Factor PCB principal | Daeduck Electronics | FC-BGA, MLB y potencial sensibilidad a SoCAMM / placa de módulo |
| Ancla de CCL | Doosan Electronic BG dentro de Doosan | Cuerpo de CCL de alta gama de la cadena doméstica |
| Barra de material aguas arriba | Kolon Industries y Pamicell | Exposición a resina / material de baja dieléctrica, base más pequeña y mayor apalancamiento operativo |
| Opcionalidad | Korea Circuit, TLB, Simmtech, Isu Petasys | Beta más amplio de módulo de memoria, MLB, redes y PCB para IA |

El punto no es forzar una sola respuesta. El punto es evitar tratar todos los nombres de "PCB para IA" como el mismo activo. Los sustratos de encapsulado, las placas multicapa, el CCL y la química de baja dieléctrica tienen estructuras de margen, períodos de calificación y riesgos de cliente diferentes.

Una visión de cartera útil es:

```text
Ancla premium:
  Samsung Electro-Mechanics

Factor principal de sustrato / placa:
  Daeduck Electronics, nombres MLB seleccionados

Barra de material aguas arriba:
  Kolon Industries + Pamicell

Opciones de mayor beta:
  Korea Circuit, TLB, Simmtech, Isu Petasys
```

Cuando el mercado diga "el ciclo de PCB ha terminado," la tesis del BOM de sistema ayuda a verificar si eso es cierto. Si los envíos de GPU se ralentizan pero el contenido de CPU, los ASICs de red, los DPUs y la complejidad de módulos de memoria siguen aumentando, el ciclo de placas puede enfriarse en un carril mientras se mantiene ajustado en otro.

---

## 8. Qué Podría Romper la Tesis

El marco del denominador común no es una afirmación de que el ciclo dura para siempre. Cuatro riesgos son relevantes.

Primero, el capex de IA de los hiperescaladores puede desacelerarse. Si AWS, Microsoft, Google o Meta orientan a la baja durante más de un trimestre, toda la cadena de suministro de hardware lo sentirá.

Segundo, la tecnología de sustratos puede cambiar. El sustrato de vidrio u otras nuevas arquitecturas podrían alterar el ciclo de FC-BGA más rápido de lo esperado. Esto no elimina la demanda de placas, pero puede desplazar a los ganadores.

Tercero, puede llegar capacidad. Si la capacidad de CCL de alta gama, fibra de vidrio o material de baja pérdida entra más rápido de lo esperado, el poder de fijación de precios puede normalizarse antes de que los volúmenes maduren completamente.

Cuarto, la IA física puede tardar más de lo que el mercado desea. La conducción autónoma, los humanoides y la electrónica espacial tienen largos ciclos de calificación y adopción. No son sustitutos de los ingresos a corto plazo de los centros de datos.

Estos riesgos no matan la tesis. Definen la lista de verificación.

---

## 9. Lista de Verificación

La tesis debe rastrearse a nivel del sistema, no solo a través del número trimestral de una sola empresa.

| Señal | Por qué importa |
|---|---|
| Hoja de ruta a escala de rack de NVIDIA | Más tipos de chips y mayor densidad de rack extienden el ciclo de sustrato del denominador común |
| Comentarios sobre la ratio CPU:GPU | Una ratio de CPU más alta fortalece el tramo de FC-BGA de CPU y MLB de placa base |
| Guidance de capex de hiperescaladores | La fuente de demanda de primer orden para las placas de centros de datos de IA |
| Tiempos de entrega de CCL y fibra de vidrio | Confirma si el ajuste de materiales es real o se está relajando |
| Márgenes de encapsulado y componentes de Samsung Electro-Mechanics | Verifica si el precio del sustrato premium y del MLCC se mantiene |
| Comentarios de pedidos de Daeduck / MLB | Verifica si el beta más amplio de PCB se está convirtiendo en ingresos |
| Cadencia de contratos de Pamicell y Doosan Electronic BG | Verifica si la demanda de material CCL aguas arriba sigue acumulándose |
| Comentarios de PCB automotriz / robótica en el IR de empresas coreanas | Señal temprana de que la IA física está pasando de opcionalidad a ingresos |

Si estas señales se mantienen alineadas, el ciclo de sustratos no es simplemente un tema de 2025-2027. Se convierte en un cambio de arquitectura de sistema plurianual.

---

## Preguntas Frecuentes

### ¿Qué es la tesis de PCB para IA?

La tesis de PCB para IA sostiene que la demanda de infraestructura de IA ya no se limita a GPUs y HBM. Los sistemas a escala de rack necesitan GPUs, CPUs, NICs, DPUs, ASICs de switch, módulos de memoria y placas de potencia. Cada capa requiere sustratos de encapsulado, placas multicapa o materiales de baja pérdida.

### ¿Por qué la IA agéntica aumenta la demanda de CPU?

La IA agéntica utiliza herramientas, recuperación de información, ejecución de código, gestión de memoria y orquestación. Esas tareas añaden carga de trabajo de CPU, DRAM, redes y DPU en torno a la GPU. Un mayor contenido de CPU puede aumentar la demanda de FC-BGA de CPU para servidores, placas base, placas de módulos de memoria y CCL de baja pérdida.

### ¿Por qué Samsung Electro-Mechanics y Pamicell están en el mismo mapa sectorial?

Están en puntos diferentes de la misma cadena de sustratos para IA. Samsung Electro-Mechanics es un nodo premium de FC-BGA y MLCC. Pamicell es un proveedor aguas arriba de materiales de baja dieléctrica vinculado al ciclo de CCL de Doosan Electronic BG. La misma demanda de placas para IA a nivel de sistema puede afectar a ambas, pero con diferentes perfiles de riesgo y valoración.

### ¿Es Pamicell una empresa de PCB?

No. Pamicell no es un fabricante de PCB. La tesis relevante es la exposición a materiales aguas arriba: insumos de baja dieléctrica / baja pérdida utilizados por productores de CCL como Doosan Electronic BG.

### ¿Es esto asesoramiento de inversión?

No. Este es un marco de investigación sectorial. La conclusión correcta depende de la valoración, la cadencia de pedidos, la confirmación de márgenes, la concentración de clientes y la tolerancia al riesgo de cada inversor.

---

## Fuentes Públicas Seleccionadas

- Página de producto NVIDIA Vera Rubin NVL72: https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/
- Blog técnico de NVIDIA, resumen de la plataforma Vera Rubin: https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
- TrendForce, comentarios sobre IA agéntica y ratio CPU:GPU: https://insights.trendforce.com/p/agentic-ai-cpu-gpu
- Página de informe de TrendForce, Ola de IA Agéntica 2026: https://www.trendforce.com/research/download/RP260408AD
- Tom's Hardware, IA agéntica y demanda de CPU: https://www.tomshardware.com/pc-components/cpus/shifting-need-for-cpus-in-ai-workloads-drives-intensifying-shortages-price-hikes
- Página de producto NVIDIA Jetson Thor: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- Guía de calidad de NASA para estándares de PCB de alta fiabilidad: https://sma.nasa.gov/sma-disciplines/quality
- Estándar de PCB de alta fiabilidad NASA GSFC-STD-8001: https://standards.nasa.gov/sites/default/files/standards/GSFC/Baseline/0/gsfc-std-8001.pdf

---

## Nota Final

La versión más clara de la tesis es simple:

La IA no compra GPUs de forma aislada. Compra sistemas.

Los sistemas añaden chips. Los chips necesitan sustratos, placas y materiales de baja pérdida.

Por eso la capa de sustratos debe leerse como un cuello de botella común en lugar de un rezagado del ciclo tardío. La implicación no es que cada acción coreana de PCB o material merezca el mismo múltiplo. Es que el ecosistema debe evaluarse como una cadena de suministro a nivel de sistema: Samsung Electro-Mechanics en el nodo premium de FC-BGA / MLCC, Daeduck y los nombres de MLB en la capa de placas, Doosan Electronic BG en el cuerpo del CCL, y Kolon Industries y Pamicell aguas arriba en materiales de baja dieléctrica.

El trabajo a partir de aquí no es repetir el tema. Es rastrear si el BOM del sistema sigue engrosándose, si el contenido de CPU y redes continúa aumentando, y si las empresas coreanas convierten esa complejidad en pedidos y márgenes.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
