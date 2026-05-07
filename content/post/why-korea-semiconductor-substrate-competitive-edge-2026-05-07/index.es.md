---
title: "Por Qué Corea, Parte 1: Por Qué Corea Tiene Tantas Empresas de Sustratos para Semiconductores y EE. UU. / Europa No"
slug: why-korea-semiconductor-substrate-competitive-edge-2026-05-07
date: 2026-05-07T21:45:00+09:00
description: "Corea tiene más de diez empresas cotizadas de sustratos para semiconductores y PCB adyacentes, mientras que EE. UU. y Europa cuentan con muy pocos fabricantes comerciales de sustratos a gran escala. La razón no es que Occidente no sepa fabricarlos. Es que durante 30 años se priorizó el diseño de chips, el software, las herramientas y los materiales, mientras que el enchapado de alto volumen, la laminación, el grabado y el aprendizaje de rendimiento se trasladaron a Asia."
categories: ["Why-Korea"]
tags: ["Por qué Corea", "sustratos para semiconductores", "FC-BGA", "ABF", "infraestructura de IA", "manufactura coreana", "materiales japoneses", "fundición taiwanesa", "acciones coreanas", "PCB de IA"]
---

> **Serie Por Qué Corea, Parte 1.** Esta es la capa estratégica detrás del [Hub de PCB y Sustratos para IA de Corea](/es/page/korea-ai-pcb-substrate-hub/). Léalo junto con [Tesis de PCB y Sustratos para IA](/es/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/), [Ecosistema de PCB para IA en Corea: 10 Empresas](/es/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) y [Samsung Electro-Mechanics: Re-valoración en Infraestructura de IA](/es/post/samsung-electro-mechanics-ai-infrastructure-rerating-2026-04-21/).

Hay una pregunta latente en el trabajo de sustratos de IA coreanos que merece su propio análisis: **¿por qué Corea tiene tantas empresas cotizadas de sustratos y PCB adyacentes en primer lugar?**

EE. UU. tiene Nvidia, AMD, Broadcom, Apple, Qualcomm, Synopsys, Cadence, Applied Materials, Lam Research y KLA. Europa tiene ASML, Infineon, STMicroelectronics, NXP y empresas especializadas en materiales. Pero cuando un inversor busca fabricantes comerciales de sustratos para semiconductores a gran escala, el mapa se inclina rápidamente hacia Japón, Taiwán y Corea.

Eso no se debe a que EE. UU. o Europa carezcan de capacidad de ingeniería. Se debe a que, durante aproximadamente 30 años, eligieron una capa diferente del ecosistema de semiconductores. EE. UU. se concentró en el diseño, el software, la propiedad intelectual y las herramientas. Europa se concentró en la litografía, los semiconductores de potencia, los chips industriales y determinados materiales. El trabajo de alto volumen —complejo, con química húmeda— de enchapado, laminación, perforación, grabado, pruebas y mejora del rendimiento se trasladó a Asia.

El resultado es un efecto de acumulación regional. Los clientes, proveedores de materiales, fabricantes de equipos, técnicos, jefes de línea, bases de datos de fallos y ciclos de aprendizaje de rendimiento se concentraron en Japón, Taiwán y Corea. Por eso este nicho es más difícil de reconstruir de lo que parece en una presentación de diapositivas.

---

## Resumen Ejecutivo

1. EE. UU. y Europa no fracasaron en la fabricación de sustratos para semiconductores. En gran medida, optaron por no construir la base de fabricación comercial de sustratos a gran escala que Asia sí construyó.
2. Los sustratos no son solo planos. Son datos de rendimiento. Los sustratos de IA de gran tamaño requieren muchas capas, cableado fino, microvías, control de deformación, estabilidad química y calificación de confiabilidad.
3. Japón es fuerte gracias a los materiales y al tiempo: la Película de Construcción ABF de Ajinomoto, Ibiden, Shinko y tres décadas de aprendizaje en sustratos de CPU de alto rendimiento.
4. Taiwán es fuerte porque TSMC, ASE, SPIL y el clúster OSAT/fundición crearon la base de clientes natural para Unimicron, Nan Ya y Kinsus.
5. Corea es fuerte porque Samsung Electronics y SK Hynix generaron una demanda local de clase mundial, mientras que la manufactura de smartphones, memoria y pantallas creó la cultura de proceso necesaria para los sustratos.
6. Corea no es fuerte en todo. Los sustratos de memoria son una fortaleza estructural coreana, pero el mercado FC-BGA de aceleradores de IA de más alto rendimiento sigue siendo liderado por los operadores históricos japoneses y taiwaneses.
7. La implicación para la inversión no es "comprar todas las acciones coreanas de sustratos." Es que el clúster de sustratos de Corea tiene una base histórica real, pero la posición a nivel de empresa difiere marcadamente según el producto, el cliente, la dependencia de materiales y el historial de rendimiento.

---

## 1. ¿Qué Es un Sustrato para Semiconductores?

Un chip semiconductor es diminuto y extremadamente denso. Una placa de circuito impreso es mucho más grande y más gruesa. Los terminales del chip no pueden conectarse directamente a la placa sin una capa intermedia.

Esa capa intermedia es el sustrato del encapsulado.

```text
Chip semiconductor
  |
Sustrato del encapsulado
  |
Placa principal / placa del sistema
```

El sustrato del encapsulado cumple tres funciones:

| Función | Descripción |
|---|---|
| Enrutamiento de señal | Transporta datos entre el chip y la placa del sistema |
| Distribución de energía | Suministra energía estable a chips de alto consumo |
| Soporte mecánico | Protege el chip del calor, la humedad, la deformación y los golpes |

La función es simple, pero la fabricación no lo es. Los sustratos avanzados requieren muchas capas, trazados finos, vías alineadas con precisión, enchapado de cobre ajustado, materiales de baja pérdida, control de deformación y alta confiabilidad. En los aceleradores de IA y las CPU de servidor, el sustrato puede ser grande, con un alto número de capas, y extremadamente exigente.

Esta industria no se trata de si alguien puede fabricar una muestra. Se trata de si puede producir millones de unidades con un rendimiento que tenga sentido económico.

---

## 2. La Barrera Real Es el Rendimiento, No el Diseño

Para un no especialista, el error más fácil es pensar en los sustratos como placas planas con patrones impresos. Eso pasa por alto el problema real.

Un sustrato FC-BGA de alto rendimiento es una estructura multicapa. Cada capa tiene cableado. Las capas se apilan. Se perforan orificios y se enchapan para conectar las capas. Los materiales se expanden y contraen con el calor. Toda la estructura puede deformarse. Un defecto diminuto puede arruinar el encapsulado.

A medida que el sustrato crece y aumenta el número de capas, la cantidad de oportunidades de defecto aumenta rápidamente. Un proceso que funciona para un encapsulado pequeño puede fallar económicamente cuando el encapsulado es cuatro veces más grande y el doble de grueso.

```text
La pregunta difícil no es:
"¿Puedes fabricar uno?"

La pregunta difícil es:
"¿Puedes fabricarlo con un rendimiento estable, calidad repetible,
a través de cambios de lote de materiales, cambios en el diseño del cliente,
deriva del equipo y pruebas de confiabilidad?"
```

Ese tipo de conocimiento no se descarga de un manual. Se aprende a través de años de muestreo, calificación, fallos de producción, auditorías de clientes, variaciones de materiales y ajuste de líneas. Por eso la capacidad en sustratos se agrupa geográficamente. Una vez que los ciclos de clientes, materiales, equipos y personas se instalan en una región, la región sigue mejorando.

---

## 3. Por Qué EE. UU. y Europa Se Retiraron

El modelo de semiconductores de EE. UU. se concentró en las capas de mayor retorno:

| Fortaleza de EE. UU. | Ejemplos | Perfil económico |
|---|---|---|
| Diseño de chips | Nvidia, AMD, Broadcom, Qualcomm, Apple | Alto margen bruto, relativamente ligero en activos respecto a manufactura |
| EDA y propiedad intelectual | Synopsys, Cadence, Ansys | Economía similar a la del software |
| Herramientas para semiconductores | Applied Materials, Lam Research, KLA | Equipos de capital de alto valor |

La fabricación de sustratos tiene un perfil diferente:

| Característica de la fabricación de sustratos | Por qué importó |
|---|---|
| Proceso químico intensivo | Enchapado, grabado, limpieza y gestión de aguas residuales |
| Alto gasto de capital | Fábricas dedicadas, largos períodos de calificación |
| Intensidad de mano de obra y proceso | Los operadores cualificados y los ingenieros de proceso son fundamentales |
| Menor margen similar al software | Menos atractivo para las preferencias del mercado de valores estadounidense |
| Carga ambiental | Los procesos húmedos enfrentan restricciones locales más estrictas |

Esta fue una división racional del trabajo durante mucho tiempo. Las empresas estadounidenses podían diseñar el chip, controlar el software y ser dueñas de la capa de equipos, mientras que los socios asiáticos se encargaban del PCB, el sustrato, el ensamblaje y el encapsulado. El problema es que una decisión racional de cadena de suministro se convirtió en una dependencia estratégica.

IPC ha sido explícito sobre esta brecha. Su trabajo de empaquetado avanzado en América del Norte sostiene que EE. UU. no tiene prácticamente ninguna capacidad para producir los sustratos de CI más avanzados, como FCBGA y FCCSP, y que la capacidad de sustratos de gama baja también es limitada. El informe de IPC también describe barreras como requisitos de fábrica de aproximadamente mil millones de dólares, largas brechas de conocimiento, débil suministro de proveedores de segundo nivel, falta de materias primas y escasez de mano de obra.

Europa es algo diferente, pero la conclusión es similar. Europa tiene AT&S, y AT&S es una empresa real de PCB de alto rendimiento y sustratos de CI. Pero incluso el mapa de manufactura de AT&S es global y con fuerte presencia en Asia, con grandes sitios de producción en China y Malasia y un centro de competencia europeo en Austria. Europa tiene experiencia, pero no tiene un clúster de sustratos amplio, denso y de alto volumen comparable al de Japón, Taiwán o Corea.

---

## 4. Japón: Materiales Más 30 Años de Aprendizaje en Rendimiento

La fortaleza de Japón en sustratos comienza con los materiales.

La palabra clave es **ABF**, la Película de Construcción de Ajinomoto. ABF es una película aislante entre capas utilizada en sustratos de encapsulado de alto rendimiento. La historia oficial de innovación de Ajinomoto describe ABF como un material estándar para CPU de alto rendimiento, adoptado por primera vez por un importante fabricante de semiconductores en 1999, y desarrollado a partir de la experiencia en química fina de la empresa.

Eso importa porque el sustrato no es solo cableado de cobre. El material aislante entre las capas determina cuán finos pueden ser los circuitos, cuán estable es la estructura y cómo se comporta el sustrato bajo el calor y el estrés.

Japón añadió luego tres décadas de aprendizaje de proceso:

| Nodo japonés | Por qué importa |
|---|---|
| Ajinomoto | Estándar de material ABF para sustratos de alto rendimiento |
| Ibiden | Historia profunda con Intel y clientes de sustratos de CPU / IA de alto rendimiento |
| Shinko Electric | Actor establecido desde hace tiempo en sustratos de encapsulado de alto rendimiento |
| Ecosistema de materiales japonés | CCL, cobre, productos químicos, herramientas y componentes de precisión |

Los medios nacionales y la cobertura vinculada a Bloomberg han descrito a Ibiden como un proveedor dominante de sustratos para los chips de IA de Nvidia. Independientemente de si se utilizan las estimaciones de cuota de mercado más agresivas o una redacción más conservadora, la dirección es clara: en la capa de sustratos de aceleradores de IA de más alto rendimiento, Japón sigue teniendo la posición de incumbente más fuerte.

La ventaja de Japón no es simplemente "buena ingeniería." Es la combinación de control de materiales, historial de calificación de clientes y datos de rendimiento que comenzaron en la era de las CPU y ahora se extienden a los aceleradores de IA.

---

## 5. Taiwán: El Tirón del Clúster de Fundición y OSAT

El camino de Taiwán es diferente. Japón parte de los materiales y de una larga historia en CPU. Taiwán parte del clúster de fabricación de semiconductores.

```text
TSMC: fundición
ASE / SPIL: ensamblaje y pruebas
Unimicron / Nan Ya / Kinsus: sustratos
```

Las empresas de sustratos no crecen de forma aislada. Crecen cerca de clientes exigentes. Un cliente de fundición o OSAT necesita muestras, lotes de calificación, pruebas de confiabilidad, cambios de proceso y retroalimentación rápida. Cuando el cliente está cerca, el ciclo de aprendizaje se acorta.

Este es el núcleo de la ventaja de Taiwán en sustratos. TSMC, ASE y SPIL crearon el tirón de producción local. Unimicron, Nan Ya y Kinsus crecieron dentro de ese tirón.

Las estimaciones de investigación de mercado muestran a Taiwán y Corea muy próximas en la cuota total de producción de sustratos para encapsulados, con Taiwán citada a menudo en torno al 28% de la producción de 2024 y Corea en torno al 27%. Los números exactos varían según la fuente y la definición, pero la dirección es estable: Taiwán y Corea no son participantes de nicho. Son nodos de producción centrales.

El riesgo de Taiwán es geopolítico. La ventaja de Taiwán es que el clúster de clientes es uno de los clústeres de fabricación de semiconductores más densos del planeta.

---

## 6. Corea: Clientes, Producción en Masa y Velocidad

La ventaja de Corea parte de un hecho simple: Samsung Electronics y SK Hynix son empresas locales.

Eso importa más de lo que parece. Los clientes fuertes generan proveedores fuertes. Samsung y SK Hynix impulsaron a los proveedores locales a través de ciclos de memoria, móviles, pantallas y componentes avanzados. Las empresas coreanas de sustratos aprendieron a operar dentro de transiciones rápidas entre nodos, sistemas de calidad estrictos y ciclos agresivos de reducción de costos.

Las raíces de los sustratos coreanos no están solo en los semiconductores:

| Base manufacturera coreana | Lo que transfirió a los sustratos |
|---|---|
| Semiconductores de memoria | Disciplina de producción de alto volumen, transiciones rápidas entre generaciones |
| Smartphones | Requisitos de placas delgadas, densas y de alta confiabilidad |
| Pantallas | Control de procesos de gran área, productos químicos, enchapado y manejo de precisión |
| Cadenas de suministro electrónico | Respuesta rápida al cliente y ajuste de proceso |

Corea también tiene velocidad de inversión. Cuando los sustratos para servidores de IA se convirtieron en una prioridad, las empresas coreanas movilizaron capital rápidamente. Samsung Electro-Mechanics, Daeduck Electronics, Korea Circuit y otras empresas de PCB/sustratos adyacentes se encuentran dentro de un sistema donde grandes clientes, ingenieros locales, proveedores de materiales y decisiones de capital pueden alinearse más rápido que en muchos entornos occidentales.

Eso no significa que todas las empresas coreanas vayan a ganar. Significa que Corea tiene las condiciones industriales previas para que existan ganadores en sustratos.

---

## 7. El Punto Débil de Corea: Los Sustratos de Aceleradores de IA de Altísimo Rendimiento

La versión honesta de esta tesis debe decirlo claramente: Corea es fuerte en sustratos, pero no igualmente fuerte en todas las categorías.

| Categoría de sustrato | Posición de Corea | Lectura |
|---|---|---|
| Sustratos de memoria | Muy fuerte | Vinculada a los ecosistemas de memoria de Samsung y SK Hynix |
| Sustratos móviles | Base heredada sólida | El crecimiento es más lento, pero la base manufacturera se mantiene |
| FC-BGA para PC / consumo | Capaz, pero cíclico | Más expuesto a sobreoferta y ciclos de PC |
| FC-BGA para servidores | Alcanzando | Los proveedores coreanos están entrando en ciclos de calificación más serios |
| FC-BGA para aceleradores de IA de altísimo rendimiento | Aún por detrás de Japón / Taiwán | La calificación de incumbentes y el historial de rendimiento son lo que más pesa |

La razón es el tiempo. Los proveedores coreanos tienen un historial más corto en FC-BGA de grandes servidores que los líderes japoneses y taiwaneses. En los sustratos de aceleradores de IA de más alto rendimiento, pesan enormemente la calificación del cliente, el control de deformación, el rendimiento en sustratos de gran tamaño, el comportamiento de los materiales y los registros de confiabilidad a largo plazo.

Por eso la oportunidad no es "Corea lo toma todo." La oportunidad es la entrada como segunda fuente, el crecimiento de ASIC personalizado y la estrechez de capacidad en los incumbentes.

Los chips personalizados de las grandes tecnológicas son importantes aquí. Google, Amazon, Meta y Microsoft intentan reducir la dependencia exclusiva de un único proveedor de aceleradores de IA. Esos chips personalizados siguen necesitando sustratos. Si los líderes japoneses y taiwaneses están al tope, los clientes necesitan alternativas calificadas. Ahí es donde se sitúa la apertura de Corea.

---

## 8. La Re-entrada de EE. UU.: La Ruta del Sustrato de Vidrio y el Empaquetado Avanzado

EE. UU. ahora comprende la dependencia.

NIST y CHIPS for America han anunciado financiación importante para el empaquetado avanzado, incluidos $1.400 millones en adjudicaciones finales bajo el Programa Nacional de Manufactura de Empaquetado Avanzado y $300 millones para investigación en sustratos avanzados y materiales. La página de Absolics de NIST también describe hasta $75 millones en financiación directa para una instalación de sustratos de vidrio en Georgia vinculada a Absolics de SKC.

La estrategia es reveladora. EE. UU. no está simplemente intentando copiar de la noche a la mañana los 30 años de base de sustratos ABF de Asia. Está intentando construir:

| Ruta de re-entrada de EE. UU. | Significado |
|---|---|
| I+D en empaquetado avanzado | Construir capacidad de proceso y pilotos domésticos |
| Sustratos de vidrio | Intentar entrar a través de un cambio de material de próxima generación |
| Empaquetado avanzado de HBM | Usar el empaquetado de memoria de IA como punto de entrada estratégico |
| Ecosistema universitario / líneas piloto | Reconstruir el ciclo de personas y procesos |

Esto representa tanto una oportunidad como un riesgo para Corea.

La oportunidad es que la era actual de sustratos ABF / FC-BGA sigue favoreciendo a los incumbentes asiáticos. El rendimiento, los clientes y los materiales ya están en Asia. El riesgo es que una transición de materiales —especialmente los sustratos de vidrio— puede reiniciar parte del juego.

Corea no está mal posicionada para ese reinicio. El país tiene profunda experiencia en procesamiento de pantallas y vidrio, y Absolics en sí está vinculada a SKC. Pero el punto sigue en pie: la ventaja en sustratos es duradera, no permanente.

---

## 9. Por Qué Esto Importa para el Mapa de Acciones Coreanas

El hecho de que Corea tenga muchas empresas de sustratos no es, en sí mismo, una tesis de inversión. La pregunta útil es por qué existen esas empresas y dónde se detiene su ventaja.

La respuesta genera un mapa de acciones más útil:

| Capa | Nombres coreanos | Por qué importa Corea |
|---|---|---|
| Ancla de gran capitalización | Samsung Electro-Mechanics | Exposición a FC-BGA y MLCC con relevancia en servidores de IA |
| Balance FC-BGA / MLB | Daeduck Electronics | Una exposición más focalizada a sustratos / placas |
| Exposición opcional a FC-BGA / SoCAMM | Korea Circuit, Simmtech, TLB | Más específico por producto y dependiente de la calificación |
| MLB de alto rendimiento | Isu Petasys | Exposición a placas de red / servidor |
| CCL y materiales | Doosan Electronic BG, Kolon Industries, Pamicell | Cuello de botella aguas arriba y exposición a materiales de baja pérdida |

La [Tesis de PCB y Sustratos para IA](/es/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) explica por qué los sustratos son un cuello de botella sistémico. La [nota del ecosistema de 10 empresas](/es/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) compara los nombres coreanos cotizados. Esta nota de Por Qué Corea añade la base histórica: Corea tiene las empresas porque los ciclos de clientes, manufactura y aprendizaje de proceso se acumularon allí.

Eso no elimina el riesgo de valoración. Solo explica por qué el clúster es real.

---

## 10. Dos Cosas Que Hay Que Tener Claras

Primero, Corea no es el número uno en todas las capas. Los sustratos de memoria y producción en masa son una fortaleza real. La capa de sustratos de aceleradores de IA de más alto rendimiento sigue siendo liderada por incumbentes con historiales más largos en servidor / CPU.

Segundo, EE. UU. y Europa no están ausentes de forma permanente. La financiación de CHIPS, los programas de empaquetado avanzado, los sustratos de vidrio y las inversiones en empaquetado de HBM son intentos explícitos de reconstruir las piezas faltantes del ecosistema. El horizonte temporal es de años, no de trimestres, pero la dirección es real.

La conclusión correcta no es "Asia posee los sustratos para siempre." La conclusión correcta es: **la ventaja actual en sustratos es el producto de décadas de aprendizaje productivo acumulado, y eso la hace lo suficientemente duradera como para importar en este ciclo de IA.**

---

## Nota Final

Corea tiene más de diez empresas cotizadas de sustratos y PCB adyacentes porque esta capacidad no apareció de la noche a la mañana. EE. UU. y Europa priorizaron el diseño, el software, las herramientas, la litografía, los chips industriales y determinados materiales. El trabajo húmedo, intensivo en proceso y capital, de fabricar sustratos con rendimiento comercial se trasladó a Asia.

Japón se fortaleció gracias a los materiales ABF y a 30 años de aprendizaje en sustratos de CPU. Taiwán se fortaleció gracias a TSMC y al clúster OSAT. Corea se fortaleció gracias a Samsung, SK Hynix, la memoria, los móviles, las pantallas y la rápida ejecución inversora.

Esa es la verdadera respuesta a "Por Qué Corea." No es una marca nacional. Es acumulación industrial.

Para los inversores, la conclusión es práctica. No trate todas las acciones coreanas de sustratos como el mismo activo. Pregunte qué capa ocupa, qué cliente la impulsa, qué cuello de botella de materiales importa, cuánto dura el ciclo de calificación y si la fortaleza de la empresa está en memoria, móviles, servidores, aceleradores de IA, CCL o materiales de baja pérdida.

Así es como el mapa de sustratos de Corea se vuelve utilizable: no como un tema de moda, sino como una estructura industrial.

Notas de fuentes: Este artículo utiliza el trabajo de IPC sobre empaquetado avanzado en América del Norte para la brecha de capacidad en sustratos de EE. UU., las publicaciones de NIST / CHIPS for America para el financiamiento de empaquetado avanzado y sustratos, la historia oficial de innovación ABF de Ajinomoto para el contexto de materiales, los materiales del sitio oficial de AT&S para la presencia europea en sustratos de CI, y estimaciones de investigación de mercado para las cuotas regionales de producción de sustratos. Los datos de mercado locales del Research OS también fueron verificados para los nombres coreanos cotizados en sustratos a fecha del 7 de mayo de 2026; la tesis del artículo no depende de la acción del precio a corto plazo.

*Descargo de responsabilidad: Solo con fines de investigación e información. No constituye asesoramiento de inversión. Los nombres citados tienen fines analíticos ilustrativos; los lectores deben realizar su propia diligencia debida y consultar a asesores autorizados antes de tomar cualquier decisión de inversión.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
