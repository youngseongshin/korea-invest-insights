---
title: "El cómputo se abarata y la memoria se acumula: por qué la memoria coreana incorpora lógica en la era de los agentes"
date: 2026-10-05T22:20:00+09:00
categories: ["Exclusive Analysis", "AI Infrastructure", "Korean-Equities"]
tags: ["Memoria", "Samsung Electronics", "SK hynix", "HBM", "HBM personalizada", "Agentes", "KV cache", "SSD empresarial", "HBF", "CXL", "Contratos de suministro a largo plazo"]
slug: "agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05"
description: "A medida que más agentes de IA reciben tareas completas, el cómputo se abarata y se acumulan contexto y conocimiento. Este análisis examina la división entre procesamiento por lotes y en tiempo real, la demanda de CPU y redes, la memoria y los SSD con lógica, y los contratos a largo plazo con depósitos; además, calcula qué persistencia de beneficios exige la cotización actual de la memoria coreana."
image: "cover.png"
draft: false
---

Aunque se envíe la misma pregunta al mismo modelo de IA, el precio puede variar mucho según cómo se procese. En la tarifa de Anthropic, Opus 5.5 cuesta la mitad del precio estándar si se usa el procesamiento por lotes, que permite responder dentro de un día. El modo rápido, que garantiza una respuesta veloz, cuesta el doble. Volver a leer contexto ya procesado cuesta una veinteava parte del precio estándar.[^anthropic-pricing]

Esta tarifa resume hacia dónde se dirige la infraestructura de IA. Las tareas que no urgen se procesan a bajo coste y las urgentes, a un precio mayor. Y lo más barato no es calcular de nuevo, sino recuperar algo que ya se había guardado.

<strong>Cuantos más agentes delegados reciben tareas completas, más eficiente se vuelve el cómputo y más se acumulan el contexto y el conocimiento. La memoria y el almacenamiento que los contienen están pasando de productos estandarizados a productos con lógica integrada. Para invertir en memoria coreana, importa más cuánto tiempo perdurarán los beneficios que su magnitud este año.</strong>

La cadena que hay que verificar consta de varios eslabones: si la infraestructura se convierte en computación continua, si el cómputo gana eficiencia de verdad, qué se acumula, si la incorporación de lógica a la memoria se traduce en ingresos y si ese valor queda en empresas coreanas. Al final calculamos qué persistencia de beneficios exige la cotización actual de Samsung Electronics y SK hynix.

La fecha de referencia del análisis es el 5 de octubre de 2026. Las cotizaciones corresponden al cierre del 2 de octubre; el 5 de octubre no hubo registros de negociación en la sesión regular coreana. Distinguimos entre anuncios de las empresas, previsiones de entidades de análisis y supuestos de cálculo de este artículo. La tabla de sensibilidad que sigue es un cálculo para verificación, no un precio objetivo.

<link rel="stylesheet" href="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/thesis.css">

## La infraestructura pasa de responder a solicitudes a mantener objetivos en marcha

Un chatbot solo calcula cuando recibe una pregunta. Un agente delegado funciona de otra manera. Cuando el usuario le encarga un objetivo, el agente planifica, utiliza herramientas, comprueba el resultado y, si hace falta, vuelve a intentarlo. El trabajo continúa aunque el usuario cierre la pantalla.

Por eso cambia la unidad de carga. En la era de los chatbots, la carga se aproximaba al número de usuarios conectados al mismo tiempo. En la era de los agentes, se acerca al número de usuarios multiplicado por los objetivos asignados por usuario y por el tiempo que esos objetivos permanecen activos. Esta estructura es computación continua orientada a objetivos.

Ya hay señales en los productos y sus tarifas. Managed Agents de Anthropic cobra 0,08 dólares por cada hora que una sesión permanece activa, además de la tarifa por tokens. La documentación explica que no se aplica un descuento por procesamiento por lotes porque la sesión conserva su estado.[^anthropic-pricing][^managed-agents]

En el evento para desarrolladores de mayo de 2026, Google presentó un agente personal que funciona todo el día en una máquina virtual dedicada. En la misma presentación indicó que el volumen mensual de tokens procesados pasó de unos 480 billones en mayo de 2025 a más de 3,2 cuatrillones en mayo de 2026, cerca de siete veces más en un año. Son cifras publicadas por la empresa, que no desglosó qué parte correspondía a agentes.[^google-io]

También se alargan las tareas. En la medición de enero de 2026 de METR, Claude Opus 4.5 podía completar con una probabilidad del 50% tareas de 320 minutos de duración, medida en tiempo humano. Desde 2024, esta duración se había duplicado aproximadamente cada 89 días. METR también reconoce que el extremo superior de los conjuntos de tareas es incierto.[^metr]

La figura siguiente muestra la cadena lógica de todo el artículo. Cada flecha representa una relación que hay que verificar, no un hecho.

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/chain.svg" alt="Cadena lógica desde los agentes delegados hasta la computación continua, la eficiencia de cálculo y la acumulación de estado, la memoria con lógica y la persistencia de beneficios"><figcaption>Esquema conceptual. El aumento de la demanda y la retención de su valor por los fabricantes de memoria son eslabones distintos. En móviles, se puede desplazar la imagen horizontalmente para leerla.</figcaption></figure>

## La diferencia de precio entre tareas urgentes y no urgentes llega a cuadruplicarse

No todas las tareas continuas son urgentes. No hay motivo para usar el mismo equipo para ordenar documentos durante la noche y para responder a un usuario que está esperando. Las empresas de modelos han traducido esa diferencia en precios.

| Empresa y modelo | Lotes o baja velocidad | Estándar | Alta velocidad o prioridad | Lectura de contexto en caché |
|---|---:|---:|---:|---:|
| Anthropic Opus 5.5 | 0.5x | 1x | 2x | 0.05x |
| OpenAI gpt-6-astra | 0.5x | 1x | 2x | 0.1x |
| Google Gemini 3.1 Pro Preview | 0.5x | 1x | 1.8x | Tarifa de almacenamiento aparte |

Las tres empresas diferencian el precio del mismo modelo según la velocidad de respuesta. La diferencia entre el nivel más barato y el más caro va de 3,6 a 4 veces. Google también cobra por el tiempo que el contexto permanece almacenado en la caché. El almacenamiento del contexto se ha convertido en un producto separado.[^anthropic-pricing][^openai-pricing][^google-pricing]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/pricing.svg" alt="Gráfico de barras con los múltiplos de precio de procesamiento por lotes, modo rápido y lectura de caché frente al precio estándar de entrada de Anthropic Opus 5.5"><figcaption>Según la tarifa oficial de Anthropic, consultada el 5 de octubre de 2026. Los múltiplos toman como referencia 1 para el precio estándar de entrada. La lectura de caché es el precio de entrada al reutilizar contexto ya procesado.</figcaption></figure>

Esta división importa a los inversores por la utilización de los equipos. La demanda solo en tiempo real genera grandes diferencias de actividad entre el día y la noche. Si se aceptan a bajo precio las tareas no urgentes durante las horas de menor actividad, el mismo equipo funciona todo el día. La computación continua no solo aumenta la demanda: también reduce el tiempo de inactividad.

## Las tareas repetitivas pasan a modelos pequeños y a código

Si un agente realiza decenas de miles de veces al día tareas del mismo tipo, no hay motivo para recurrir siempre al modelo más grande. Las tareas repetitivas y concretas pasan a dos alternativas: un modelo pequeño especializado en esa tarea o código que se ejecuta sin un modelo.

La tarifa respalda el uso de modelos pequeños. Según la tarifa de OpenAI, la entrada de gpt-6-astra cuesta 10 dólares por millón de tokens y la de gpt-6-luna, 0,10 dólares. La diferencia dentro de la misma empresa es de 100 veces. En un artículo de 2025, investigadores de NVIDIA estimaron que entre el 40% y el 70% de las llamadas de agentes podrían sustituirse por modelos pequeños especializados. Es una estimación del artículo, no una proporción medida.[^openai-pricing][^nvidia-slm]

La documentación del producto respalda el uso de código. La documentación Agent Skills de Anthropic explica que los scripts de una habilidad se ejecutan en el shell y que solo su resultado se incorpora al contexto del modelo. El código del script no entra en el contexto. Así, los procedimientos que el modelo infería en cada ocasión se convierten en código fijado una sola vez.[^agent-skills]

La empresa de automatización web Skyvern publicó resultados en los que convirtió en código una tarea realizada una vez por un agente y luego la reprodujo sin modelo. El tiempo de ejecución bajó de 279 a 120 segundos y el coste por ejecución, de 0,11 a 0,04 dólares. Es una medición propia publicada por la empresa.[^skyvern]

Aquí aparece una distinción importante. Disminuye el cómputo por tarea. Sin embargo, hay que almacenar en algún lugar el código fijado, los pesos de los modelos especializados y los registros de ejecución. La eficiencia se logra usando menos cómputo y reutilizando más lo que se ha guardado.

## El trabajo no termina con las GPU

Una tarea de un agente se divide en varias etapas. La GPU se encarga de pensar. La CPU ejecuta herramientas, gestiona archivos y corre código en entornos aislados. La red transporta datos entre etapas.

Este año, varias empresas han hablado en la misma dirección sobre la demanda de CPU. Andy Jassy, consejero delegado de Amazon, dijo en la presentación de resultados de julio que la mayoría de las herramientas que usan los agentes funcionan en CPU, no en aceleradores de IA. Lisa Su, consejera delegada de AMD, pronosticó en agosto que el mercado de CPU para servidores alcanzaría los 220.000 millones de dólares en 2030, y que los agentes y los entornos de ejecución aislados representarían la mayor parte. Ambas son explicaciones y previsiones de directivos.[^amzn-call][^amd-call]

También hay señales físicas. En abril, TrendForce informó de que los precios de las CPU para servidores habían subido entre un 10% y un 20% desde marzo y que los plazos de entrega habían pasado de 1-2 semanas a 8-12 semanas. Es información secundaria que cita medios taiwaneses y japoneses. NVIDIA ya ha enviado su CPU Vera de 88 núcleos, concebida expresamente para ejecutar agentes en entornos aislados.[^tf-cpu][^nvda-vera]

La red tampoco se limita a un solo tipo. Se combinan las conexiones entre chips dentro de un rack, Ethernet entre racks y CXL para ampliar la memoria. En su presentación de resultados de septiembre, Broadcom dijo que los ingresos de redes para IA superaban en 2,5 veces los de un año antes y que la demanda de láseres para comunicaciones ópticas excedía ampliamente la oferta.[^avgo-call]

También han surgido unidades de procesamiento de datos independientes. En marzo, NVIDIA presentó un diseño basado en BlueField-4 que gestiona datos de contexto delante del almacenamiento y anunció que los productos de sus socios llegarían en el segundo semestre de 2026. A 5 de octubre no encontramos datos que confirmaran envíos y funcionamiento reales.[^nvda-stx]

La conclusión no es que las GPU pierdan importancia. Es que se necesitan juntas GPU, CPU, unidades de procesamiento de datos y varios tipos de red. Todos estos dispositivos incorporan memoria.

## El cómputo se puede repetir, pero el contexto y el conocimiento se acumulan

La evolución descrita hasta aquí se resume en una frase: la infraestructura de agentes amplía la memoria para no repetir el mismo cálculo.

Cuando un modelo de lenguaje lee un contexto largo, genera resultados intermedios de cálculo. Se conocen como KV cache. Si se conserva la caché, no hay que volver a calcular desde el principio al leer de nuevo el mismo contexto. Por eso, en la tarifa citada al comienzo, leer contexto en caché cuesta una veinteava parte del precio estándar.

La caché ocupa un espacio considerable. En un documento técnico publicado en junio, IBM estimó que la KV cache de una solicitud ocupa unos 3-10 GB en un modelo mediano y 40-80 GB en uno grande. También informó de que reutilizar la caché redujo a una cincuentiseisava parte el tiempo hasta la primera respuesta con una entrada de 130.000 tokens. Es una medición propia de una empresa.[^ibm-kv]

NVIDIA ha definido un nuevo nivel para guardar esta caché. Ha situado una capa de almacenamiento flash conectada por Ethernet debajo de la HBM dentro de la GPU, la memoria del servidor y los SSD del servidor, y la ha llamado CMX. También presentó el software que decide en qué nivel colocar la caché.[^nvda-cmx][^nvda-dynamo]

En las presentaciones de resultados de las empresas de memoria aparece el mismo tema. Micron informó el 30 de septiembre de que los ingresos trimestrales por SSD para centros de datos se acercaban a 10.000 millones de dólares, más de diez veces los de un año antes. Citó como una de las causas el almacenamiento de contexto que descarga la KV cache.[^mu-remarks]

SK hynix dijo en su presentación de resultados de julio que los ingresos por SSD empresariales se habían duplicado respecto al trimestre anterior, y señaló como nuevos usos el almacenamiento de KV cache y el almacenamiento cercano a las GPU. Samsung Electronics prevé que los SSD para servidores superen el 60% de sus ingresos de NAND en 2026. Estas dos declaraciones se verificaron en transcripciones de llamadas de resultados republicadas por medios.[^skh-call][^sec-call]

En agosto, el consejero delegado del fabricante de discos duros Western Digital expresó la diferencia así: los ciclos de cómputo pueden repetirse, pero los datos se acumulan con interés compuesto. Los agentes dejan registros en cada etapa, y esos registros sirven de material para la siguiente tarea.[^wdc-call]

Sin embargo, hay que separar la tasa de crecimiento de la cuantía de ingresos. La memoria de un agente personal no ocupa mucho espacio. El factor que puede elevar los ingresos es que todo el servicio de inferencia pase a descargar la caché a flash para conservarla. Esta transición aún está en sus primeras etapas.

## La memoria está pasando de producto estándar a producto con lógica integrada

Cuando se acumulan más datos, cambian las exigencias del cliente. Ya no pregunta solo por la capacidad: quiere saber si podrá recuperar los datos a tiempo, cuánta energía se consumirá y cómo encajarán con su chip. Para responder, la memoria debe incorporar lógica.

SK hynix describió directamente este cambio en el folleto de su cotización en Estados Unidos, publicado en julio. Escribió que, en el pasado, las empresas de memoria suministraban componentes estándar, pero que en la era de la IA la memoria desempeña un papel central en la optimización del rendimiento. Presentó su visión como creador de memoria de IA de pila completa. Es la caracterización de la propia empresa y debe distinguirse de hechos demostrados por sus resultados.[^skh-424b4]

El ejemplo más avanzado es el dado base de HBM. HBM apila varias capas de chips de memoria, y el dado base, situado en la parte inferior, gestiona señales y energía. Hasta la generación anterior se fabricaba con procesos de memoria. Desde HBM4 se fabrica con procesos lógicos. Samsung Electronics utiliza su propio proceso de 4 nm. En 2024, SK hynix anunció una colaboración para fabricar el dado base de HBM4 con el proceso lógico de TSMC.[^sec-hbm4][^skh-tsmc]

El siguiente paso es la HBM personalizada, que integra la lógica del cliente en el dado base. El 26 de agosto, NVIDIA presentó NVHBM, que incorpora sus circuitos de control de memoria al dado base de HBM. Según NVIDIA, aumenta el ancho de banda un 30% y reduce el consumo un 15% frente a HBM4E estándar. El 30 de septiembre, Micron dijo que desarrollaría este producto junto con NVIDIA.[^nvda-nvhbm][^mu-remarks]

En agosto, Samsung Electronics presentó en la conferencia de semiconductores Hot Chips el paso siguiente: trasladar los circuitos de control; incorporar elementos de cálculo al dado base para asumir parte de los cálculos del procesador; y apilar la memoria directamente sobre el chip de cálculo. No indicó fechas de lanzamiento.[^sec-hotchips]

También aparecen productos con la misma orientación en almacenamiento y otros tipos de memoria. Sin embargo, su grado de madurez varía mucho.

| Producto | Lógica incorporada | Etapa actual |
|---|---|---|
| Dado base de HBM4 | Control de señales y energía fabricado con proceso lógico | Producción en serie, ingresos generados |
| SOCAMM2 | Módulo de memoria de bajo consumo para servidores | Producción en serie, ventas en aumento |
| SSD empresarial | Chip de control y firmware, diseño para almacenamiento de contexto | Producción en serie, fuerte aumento de ingresos |
| HBM personalizada, NVHBM | Circuitos de control de memoria del cliente | En desarrollo, prevista para futuras GPU |
| Módulo de memoria CXL | Circuito de supervisión que identifica los datos de uso frecuente | Se informó de que Samsung apunta a producción en serie a finales de 2026; puede retrasarse |
| HBF | Interfaz de gran ancho de banda que sitúa NAND cerca del chip de cálculo | Primera especificación técnica publicada en agosto de 2026; aún sin producto |
| PIM, HBM con elementos de cálculo | Circuitos de cálculo dentro de la memoria | Prototipos y hojas de ruta |

Los productos que figuran en producción en serie están reflejados en los resultados de este año. El informe de resultados del segundo trimestre de Samsung Electronics atribuyó parte del desempeño de su negocio de fundición al aumento de la demanda de dados base de HBM. Desde la HBM personalizada hacia abajo, los productos aún no se han confirmado en ingresos. SK hynix dijo que mantendrá el método de unión actual hasta HBM4E; en un evento del sector de septiembre se evaluó CXL como una capa complementaria, no como sustituto de HBM.[^sec-ir][^skh-q2][^tf-cxl][^hbf-ocp][^sec-fms][^skh-hybrid][^tf-cxl-doubt]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/maturity.svg" alt="Clasificación de los productos de memoria con lógica en tres etapas: ingresos generados, desarrollo y muestras, y hoja de ruta"><figcaption>Etapas clasificadas a partir de anuncios de empresas y datos de resultados. Cuanto más a la izquierda, más evidencia hay en los resultados de este año; cuanto más a la derecha, menos definida está la fecha. A 5 de octubre de 2026.</figcaption></figure>

Por tanto, decir que la memoria incorpora lógica es correcto como dirección, pero todavía tiene un alcance limitado. Los ingresos confirmados hoy corresponden a HBM4, módulos para servidores y SSD empresariales. DRAM y NAND estándar siguen compitiendo por especificaciones y precio.

## La hipótesis de que la memoria será el centro de la computación solo se confirma en su dirección

La hipótesis más lejana es que cambie la propia estructura de la computación. En los ordenadores actuales, el centro es la unidad de cálculo, que recibe datos de la memoria. Si los datos crecen más rápido que el cómputo, el coste de moverlos puede superar al de procesarlos. En ese caso, conviene calcular donde están los datos.

Hay iniciativas en esta dirección. La última etapa de la hoja de ruta de Samsung Electronics apila la memoria directamente sobre el chip de cálculo. Qualcomm anunció que incorporará una estructura que integra en tres dimensiones cálculo y memoria a un producto de 2027. SK hynix y Sandisk desarrollaron con Google y Tenstorrent un estándar que coloca NAND junto al chip de cálculo.[^sec-hotchips][^qcom-hbc][^hbf-ocp]

En su presentación de resultados de agosto, el consejero delegado de Sandisk describió la IA como un problema fundamentalmente centrado en la memoria y con uso intensivo de almacenamiento. Conviene tener presente que la declaración procede del consejero delegado de una empresa de memoria.[^sndk-call]

Dejemos clara la evaluación de esta hipótesis. En 2026, la computación centrada en memoria es una opción estratégica, no una base de inversión. No cuenta con verificación independiente del rendimiento, calendario de producción en serie ni adopción confirmada por clientes. No sirve para explicar las cotizaciones actuales. Si esta dirección resulta acertada, las empresas que combinen memoria, procesos lógicos y apilamiento serán las más beneficiadas.

## La tesis de inversión en memoria coreana pasa de la magnitud de los beneficios a su duración

Pasemos ahora a las empresas coreanas. Los beneficios de este año ya son elevados. En el segundo trimestre, el beneficio operativo del negocio de semiconductores de Samsung Electronics fue de KRW 89,2 billones, el 70% de los ingresos. El de SK hynix fue de KRW 60,5 billones, el 76% de los ingresos.[^sec-ir][^skh-q2]

Sin embargo, la cotización no asigna un múltiplo alto a esos beneficios. Al cierre del 2 de octubre, Samsung Electronics cotizaba a 5,85 veces los beneficios previstos para 2026 y SK hynix, a 5,25 veces. Los beneficios previstos son el promedio de las estimaciones de analistas recopiladas por Naver Finance.[^naver-sec][^naver-skh]

Los múltiplos bajos pueden interpretarse como una señal de que el mercado aún ve la memoria como un sector cíclico. La preocupación es que los beneficios actuales procedan de la escasez de oferta y que caigan con fuerza cuando terminen las ampliaciones de capacidad. Es una interpretación, pero tiene fundamento: SK hynix incluyó en los factores de riesgo de su folleto la recurrente sobreoferta del sector de memoria.[^skh-424b4]

Aquí es donde la memoria con lógica integrada cobra importancia para la inversión. Este cambio no aumenta necesariamente los beneficios de este año. Puede crear razones para que no caigan tanto como antes cuando se normalice la oferta. Esas razones están en los costes de cambio y la estructura de los contratos.

La primera es que al cliente le resulte más difícil cambiar de proveedor. Un dado base diseñado para el chip de un cliente no se sustituye fácilmente por el de otra empresa. El tiempo necesario para el diseño, la validación y la certificación se convierte en un coste de cambio. La magnitud real de ese coste y su efecto en los precios siguen siendo hipótesis no verificadas.

La segunda es la estructura contractual. Micron anunció el 30 de septiembre que había firmado 26 contratos con clientes estratégicos. Los clientes pagan incluso si no compran los volúmenes comprometidos a lo largo de varios años; las garantías financieras que han aportado suman 32.000 millones de dólares y consisten en su mayoría en depósitos en efectivo. Micron dijo que esta visibilidad le permite aumentar la inversión en capacidad.[^mu-remarks]

Las dos empresas coreanas avanzan en la misma dirección. SK hynix dijo que en el segundo trimestre había concluido negociaciones de contratos de suministro a largo plazo con unos 10 clientes y explicó en la llamada que incluían mecanismos financieros como depósitos. Samsung Electronics dijo que planea asignar entre el 60% y el 70% de su capacidad a contratos a largo plazo, con un plazo base de cinco años y renovación anual. No se han publicado los precios ni las condiciones de cancelación de cada contrato.[^skh-q2][^skh-lta][^sec-lta]

Un sector donde los clientes adelantan dinero y se comprometen con volúmenes funciona de forma distinta a otro donde se compran y venden productos estándar en el mercado al contado. Sin embargo, los contratos a largo plazo tienen dos caras. TrendForce indicó que, debido a los mecanismos de precios de estos contratos, algunos proveedores subieron los precios de DRAM para servidores menos que la media del mercado. A cambio de un suelo durante las caídas, ceden parte del techo durante las subidas.[^tf-memory]

## Samsung Electronics y SK hynix afrontan el mismo cambio desde posiciones distintas

Las dos empresas tienen fortalezas y debilidades diferentes ante el mismo cambio: la incorporación de lógica a la memoria.

| Aspecto | Samsung Electronics | SK hynix |
|---|---|---|
| Margen operativo de semiconductores en el segundo trimestre | 70% | 76% |
| Dado base de HBM4 | Proceso propio de 4 nm | Proceso de TSMC |
| Captura del valor de la lógica, análisis de este artículo | Puede quedar dentro gracias a los resultados de la fundición | Coste pagado a un proveedor externo |
| Amplitud de productos | HBM, módulos para servidores, SSD, fundición y empaquetado | HBM, módulos para servidores, SSD y liderazgo de estándares HBF |
| Contratos a largo plazo | Plan de asignar entre el 60% y el 70% de la capacidad | Negociaciones concluidas con unos 10 clientes |
| Retribución al accionista | Plan de dividendos de unos KRW 30 billones en el tercer trimestre | Aprobada la cancelación de acciones propias por KRW 40 billones |
| Cotización frente a beneficios previstos para 2026 | 5,85 veces | 5,25 veces |

La fortaleza de SK hynix está en su rentabilidad actual y sus relaciones con clientes. Su margen operativo es mayor y ya concluyó negociaciones de suministro a largo plazo con unos 10 clientes. Su debilidad es que paga fuera de la empresa por el valor de la lógica. Según TrendForce, que citó a medios coreanos, el coste del dado base de HBM4 fabricado por TSMC equivale a 3-4 veces el de los chips de memoria. La empresa no confirmó esa cifra.[^tf-basedie]

La fortaleza de Samsung Electronics es que el valor de la lógica puede permanecer dentro de la empresa. Samsung se describe como la única empresa que reúne memoria, diseño lógico, fundición y empaquetado.[^sec-fms] La debilidad es que esa estructura todavía no ha demostrado suficientemente su rentabilidad. No debemos contar dos veces los ingresos de un dado base producido internamente como si fueran ingresos obtenidos de un cliente externo. Hay que comprobarlo en los costes consolidados y el efectivo.

La retribución al accionista es la vía por la que los beneficios llegan a los accionistas. En agosto, SK hynix aprobó comprar y cancelar todas sus acciones propias por un valor de KRW 40 billones y elevó a más del 50% el objetivo de distribución del flujo de caja libre. Samsung Electronics planea distribuir unos KRW 30 billones en efectivo en el tercer trimestre y lo confirmará en el consejo de administración de finales de octubre. Los dos datos proceden de noticias de prensa; no contrastamos los documentos regulatorios originales.[^skh-return][^sec-return]

Mi evaluación es la siguiente. Cuanto más avance la incorporación de lógica a la memoria, más favorable será estructuralmente la posición de quien fabrique la lógica internamente. En resultados actuales y posición frente a clientes, SK hynix va por delante. En la etapa inicial del cambio, importa más su capacidad de ejecución; cuando la HBM personalizada y los pasos siguientes cobren escala, es probable que la estructura integrada de Samsung Electronics adquiera más valor. El punto de inflexión llegará cuando los dados base fabricados por Samsung Foundry entren en producción en serie con diseños de clientes externos.

## La cotización actual supone que apenas algo más de la mitad de los beneficios de este año perdurará

En una aproximación sencilla, la cotización equivale a los beneficios sostenibles que el mercado espera multiplicados por un múltiplo. Si suponemos que el mercado asigna 10 veces los beneficios a las empresas de memoria, podemos calcular qué nivel de beneficios exige la cotización actual.

El cierre de Samsung Electronics el 2 de octubre fue de KRW 276.000. Con un múltiplo de 10, el beneficio por acción que exige la cotización es KRW 27.600, el 58,5% de los KRW 47.142 previstos para 2026. SK hynix cerró a KRW 1.842.000; con el mismo cálculo, el beneficio por acción exigido es KRW 184.200, el 52,5% de los KRW 350.576 previstos.[^naver-sec][^naver-skh]

En otras palabras, la cotización actual es compatible con el supuesto de que perdure algo más de la mitad de los beneficios de 2026. Esto no significa que esa sea exactamente la opinión del mercado. Hay muchas combinaciones de múltiplos y beneficios. Pero la pregunta queda clara: ¿pueden los productos con lógica integrada y los contratos a largo plazo sostener los beneficios normalizados por encima de la mitad de los de este año?

La tabla siguiente cambia la proporción de los beneficios previstos para 2026 que perdura y el múltiplo asignado. Entre paréntesis aparece la variación frente al cierre del 2 de octubre. Tanto la proporción restante como el múltiplo son supuestos de cálculo de este artículo, no probabilidades. No se incluyen dividendos.

Samsung Electronics, cotización de referencia: KRW 276.000

| Proporción de beneficios previstos para 2026 que perdura | 8x | 10x | 12x |
|---|---:|---:|---:|
| 40% | KRW 151.000 (-45.3%) | KRW 189.000 (-31.7%) | KRW 226.000 (-18.0%) |
| 55% | KRW 207.000 (-24.8%) | KRW 259.000 (-6.1%) | KRW 311.000 (+12.7%) |
| 70% | KRW 264.000 (-4.3%) | KRW 330.000 (+19.6%) | KRW 396.000 (+43.5%) |

SK hynix, cotización de referencia: KRW 1.842.000

| Proporción de beneficios previstos para 2026 que perdura | 8x | 10x | 12x |
|---|---:|---:|---:|
| 40% | KRW 1.122.000 (-39.1%) | KRW 1.402.000 (-23.9%) | KRW 1.683.000 (-8.6%) |
| 55% | KRW 1.543.000 (-16.3%) | KRW 1.928.000 (+4.7%) | KRW 2.314.000 (+25.6%) |
| 70% | KRW 1.963.000 (+6.6%) | KRW 2.454.000 (+33.2%) | KRW 2.945.000 (+59.9%) |

Los extremos de la tabla muestran el argumento. Si solo perdura el 40% de los beneficios, la cotización queda por debajo de la actual incluso con un múltiplo de 12 veces. Una buena historia sectorial no compensa la caída de beneficios. En cambio, si el mercado cree que perdurará el 70%, la cotización subiría entre un 20% y un 33% aunque el múltiplo siguiera en 10 veces.

Hay que tener en cuenta un aspecto de las cifras de SK hynix. Su beneficio neto del segundo trimestre fue de KRW 93,9 billones, mayor que el beneficio operativo de KRW 60,5 billones. No hemos podido confirmar la causa. Si los beneficios procedentes de partidas no operativas no se repiten, las previsiones anuales de beneficio por acción podrían incluir ingresos no recurrentes; en ese caso habría que reducir la proporción que se considera sostenible.[^skh-q2]

La clave de una revalorización no es el múltiplo, sino la proporción de beneficios que perdura. La memoria con lógica integrada y los contratos a largo plazo pueden elevar esa proporción. Sabremos si lo consiguen cuando aumente la oferta en 2027 y 2028.

## La objeción más fuerte es que el valor de la lógica queda en manos de quien la diseña

Esta tesis tiene objeciones importantes. Las presentamos empezando por la más significativa.

La primera es quién captura el valor. NVIDIA diseñó los circuitos de control incorporados al dado base de NVHBM. NVIDIA dijo que varias empresas de memoria suministrarán la misma especificación. Micron encarga la fabricación de ese dado base a una fundición externa. En esta estructura, el valor del diseño queda en NVIDIA y el de la fabricación, en la fundición; las empresas de memoria aún pueden acabar compitiendo entre sí con la misma especificación.[^nvda-nvhbm][^mu-foundry]

Algo parecido ocurre con el almacenamiento. En el diseño de NVIDIA para guardar contexto, el procesamiento que gestiona los datos reside en la unidad de procesamiento de datos de NVIDIA, no dentro del SSD. El software que decide en qué nivel se guarda la caché también es de NVIDIA. El lugar donde se acumulan los datos puede ser distinto del lugar que dificulta al cliente cambiar de proveedor.[^nvda-cmx][^nvda-dynamo]

Esta objeción es la que más debilita la tesis. Que la memoria incorpore lógica y que la empresa de memoria sea dueña de esa lógica son cosas distintas. Esta objeción también explica por qué destacamos la estructura integrada de Samsung Electronics. Una empresa de memoria que no fabrique la lógica directamente podría quedar en una posición más estrecha a medida que los productos se sofisticaran.

La segunda objeción es la adaptación de la demanda. Cuando la memoria se encarece, los clientes buscan formas de utilizar menos. El 29 de septiembre, TrendForce indicó que los fabricantes de GPU y chips personalizados estudiaban reducir la HBM por dispositivo y que, para 2027, daban prioridad a evaluar configuraciones de ocho capas. En marzo, investigadores de Google publicaron una técnica de compresión que reduce el uso de memoria de KV cache a menos de una sexta parte. La documentación de Anthropic señala que la precisión disminuye a medida que aumenta la longitud del contexto y ofrece una función que resume conversaciones antiguas.[^tf-hbm][^turboquant][^anthropic-context]

Todavía no sabemos si la acumulación avanza más rápido que las técnicas para reducirla. Micron también reconoció que el aumento de memoria por servidor se había moderado algo debido a los precios.[^mu-remarks]

La tercera objeción es la oferta y la financiación. El 30 de julio, TrendForce pronosticó que la oferta de NAND se aliviaría en el segundo semestre de 2027 y que surgiría presión a la baja sobre los precios. Según una noticia de TrendForce, la cuota de CXMT en los ingresos de DRAM del segundo trimestre subió al 9,5%. El director del Banco de Pagos Internacionales advirtió en un discurso del 10 de septiembre que la inversión en capacidad de las grandes tecnológicas superaba su flujo de caja. Si se agota el dinero de los clientes, también se pondrán a prueba sus compromisos de contratos a largo plazo.[^tf-supply][^tf-china][^bis]

Micron, en cambio, considera que la oferta y la demanda de 2027 y 2028 serán más ajustadas que en 2026. La divergencia entre las previsiones de entidades de análisis y proveedores es, por sí misma, un motivo para no dar por sentado lo que ocurrirá en 2027.[^mu-remarks]

También debe ponerse a prueba el supuesto de demanda. El punto de partida de este artículo es que las personas seguirán delegando tareas a agentes. En los datos de uso propios publicados por Anthropic en febrero, las tareas que duraron más de 45 minutos seguidos representaban el 0,1% superior. La mayoría eran mucho más cortas. Si la delegación no se convierte en un hábito o los usuarios no ceden permisos, la computación continua avanzará más despacio de lo que supone este análisis.[^anthropic-autonomy]

## En el próximo trimestre comprobaremos los fundamentos de los beneficios que perduran, no los precios

Los próximos datos permitirán comprobar esta tesis. Indicamos qué observar y qué podría cambiar la evaluación.

| Qué comprobar | Señal que respalda la tesis | Señal que la debilita |
|---|---|---|
| Resultados del tercer trimestre, octubre | Aumento del volumen de HBM4 y SSD empresariales, mejora de la combinación de productos | La mayor parte del aumento de beneficios procede de la subida de precios de productos estándar |
| Contratos a largo plazo | Publicación de depósitos y compras mínimas, renovación de contratos | Sacrificio de beneficios por topes de precios, condiciones que siguen sin publicarse |
| HBM personalizada | Producción en serie para clientes externos de dados base de Samsung Foundry | Tres empresas compiten por precio con una sola especificación |
| Almacenamiento de contexto | Envíos de productos de socios de CMX, contratos para servidores de almacenamiento dedicados | Difusión de tecnologías de compresión, retrasos en envíos |
| Oferta en 2027 | Continúan las subidas de precios contractuales, clientes elevan sus planes de inversión | Caen los precios de NAND, se reduce la HBM por dispositivo |

Según informaciones de prensa, los resultados preliminares del tercer trimestre de Samsung Electronics se publicarán el 8 de octubre. La media del beneficio operativo recopilada por FnGuide es de KRW 108,1 billones. Se espera que SK hynix publique sus resultados a finales de octubre; la media del beneficio operativo es de KRW 77,2 billones. Ambas cifras se basan en noticias publicadas a 5 de octubre. No hemos confirmado los calendarios oficiales de las empresas.[^consensus]

Importa más la composición que la cifra por sí sola. Aunque el beneficio operativo supere la media, si se debe únicamente a la subida de precios de productos estándar, no respalda la tesis de este artículo. Aunque quede por debajo de la media, si mejora el volumen de HBM4 y la calidad de los contratos a largo plazo, aumentan los fundamentos para que perduren los beneficios.

También dejamos fijada la condición que cambiaría nuestra evaluación. Si la HBM personalizada se convierte en una única especificación y las tres empresas de memoria compiten con el mismo producto, mientras los precios contractuales de 2027 empiezan a bajar, habría que rebajar un nivel la tesis. En ese caso, la memoria coreana fabricaría productos más sofisticados, pero seguiría valorándose como un sector cíclico.

<strong>Los agentes utilizan memoria para ahorrar cómputo. Los productos que contienen esos recuerdos incorporan lógica y algunos clientes ya empiezan a adelantar dinero. La revalorización de la memoria coreana depende de que este cambio sostenga los beneficios incluso después de que aumente la oferta. La cotización actual todavía solo descuenta algo más de la mitad de los beneficios de este año.</strong>

## Fuentes y límites de los cálculos

Contrastamos los anuncios de empresas, documentos regulatorios y materiales de entidades de análisis a 5 de octubre de 2026. Las declaraciones verificadas en transcripciones de llamadas republicadas por medios se indican en las notas. Las cifras de rendimiento comunicadas por empresas no cuentan con verificación independiente. La proporción de beneficios que perdura y los múltiplos de la tabla de sensibilidad son supuestos de cálculo, no previsiones. Utilizamos sin cambios las estimaciones de beneficio por acción recopiladas por Naver Finance y no pudimos confirmar las estimaciones de 2027.

[^anthropic-pricing]: [Tarifa oficial de Anthropic](https://platform.claude.com/docs/en/about-claude/pricing), consultada el 2026-10-05. Precio estándar de entrada de Opus 5.5: 4 dólares; lotes: 2 dólares; modo rápido: 8 dólares; lectura de caché: 0,20 dólares por millón de tokens. Incluye la tarifa de sesión de Managed Agents.

[^managed-agents]: [Documentación general de Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), consultada el 2026-10-05. Documentación de un producto beta.

[^google-io]: [Resumen de la ponencia principal de Sundar Pichai en Google I/O 2026](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/), 2026-05. Cifras publicadas por la empresa.

[^metr]: [METR Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/), 2026-01-29. Horizonte temporal con un criterio de éxito del 50%.

[^openai-pricing]: [Tarifa de la API de OpenAI](https://developers.openai.com/api/docs/pricing), consultada el 2026-10-05. gpt-6-astra estándar: 10 dólares, Flex: 5 dólares, Fast: 20 dólares, entrada en caché: 1 dólar. Entrada de gpt-6-luna: 0,10 dólares.

[^google-pricing]: [Tarifa de Gemini API](https://ai.google.dev/gemini-api/docs/pricing), actualizada el 2026-10-01. Gemini 3.1 Pro Preview: estándar 2 dólares, lotes 1 dólar, Priority 3,60 dólares; tarifa por hora de almacenamiento en caché.

[^nvidia-slm]: [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153), equipo de investigación de NVIDIA, presentado el 2025-06-02. El artículo expone una tesis y el 40-70% es una estimación.

[^agent-skills]: [Documentación general de Anthropic Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), consultada el 2026-10-05.

[^skyvern]: [Medición de reproducción de código en el blog de Skyvern](https://www.skyvern.com/blog/asking-ai-to-build-scrapers-should-be-easy-right/), publicado el 2025-10-17 y actualizado el 2026-08-24. Medición propia de la empresa.

[^amzn-call]: [Transcripción republicada de la llamada de resultados del segundo trimestre de Amazon de 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-amazon-tops-q2-2026-estimates-as-aws-growth-accelerates-93CH-4826442), 2026-07-30. Declaraciones de directivos.

[^amd-call]: [Transcripción republicada de la llamada de resultados del segundo trimestre de AMD de 2026](https://www.fool.com/earnings/call-transcripts/2026/08/11/amd-amd-q2-2026-earnings-call-transcript/), llamada del 2026-08-04. Previsión de la empresa sobre el tamaño del mercado.

[^tf-cpu]: [Noticia de TrendForce sobre precios de CPU para servidores](https://www.trendforce.com/news/2026/04/22/news-server-cpu-prices-up-as-much-as-20-since-march-intel-may-raise-prices-another-8-10-in-2h26/), 2026-04-22. Cita medios taiwaneses y japoneses.

[^nvda-vera]: [Anuncio de envíos de CPU Vera de NVIDIA](https://blogs.nvidia.com/blog/vera-cpu-delivery/), 2026-05-18.

[^avgo-call]: [Transcripción republicada de la llamada de resultados del tercer trimestre FY2026 de Broadcom](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/), llamada del 2026-09-02. Declaraciones de directivos.

[^nvda-stx]: [Anuncio de la arquitectura de almacenamiento NVIDIA BlueField-4 STX](https://nvidianews.nvidia.com/news/nvidia-launches-bluefield-4-stx-storage-architecture-with-broad-industry-adoption), 2026-03-16. Las cifras de rendimiento son afirmaciones de la empresa.

[^ibm-kv]: [Documento técnico de IBM Redbooks sobre KV cache](https://www.redbooks.ibm.com/docs/MD260021/MD260021.html), publicado el 2026-06-05. Mediciones y estimaciones propias de la empresa.

[^nvda-cmx]: [Descripción del producto NVIDIA CMX](https://www.nvidia.com/en-us/data-center/ai-storage/cmx/), consultada el 2026-10-05. No indica fecha de publicación.

[^nvda-dynamo]: [Documentación de NVIDIA Dynamo sobre jerarquización de KV cache](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/kv-cache-offloading), consultada el 2026-10-05. La documentación no incluye cifras de rendimiento.

[^mu-remarks]: [Comentarios preparados para el cuarto trimestre FY2026 de Micron](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf), 2026-09-30. Los ingresos de SSD para centros de datos aparecen en el original como "nearly $10 billion". Se contrastaron en este documento los contratos con clientes estratégicos, depósitos, NVHBM y previsiones de oferta y demanda.

[^skh-call]: [Transcripción republicada de la llamada de resultados del segundo trimestre de 2026 de SK hynix](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q2-2026-results-as-shares-fall-93CH-4818480), llamada del 2026-07. No es una transcripción oficial de la empresa.

[^sec-call]: [Transcripción republicada de la llamada de resultados del segundo trimestre de 2026 de Samsung Electronics](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q2-2026-profit-as-ai-demand-surges-93CH-4822292), llamada del 2026-07. No es una transcripción oficial de la empresa.

[^wdc-call]: [Resumen de la llamada de resultados del cuarto trimestre FY2026 de Western Digital](https://finance.biggo.com/news/US_WDC_2026-08-05), 2026-08-05. Declaración verificada en una fuente secundaria resumida.

[^skh-424b4]: [Folleto de cotización estadounidense de SK hynix, SEC 424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm), 2026-07-09. Se contrastaron el apartado de estrategia, la definición de Custom HBM y los factores de riesgo en el original.

[^sec-hbm4]: [Anuncio de Samsung Electronics sobre el envío de HBM4 de producción en serie](https://news.samsungsemiconductor.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/), 2026-02-12. El proceso y el rendimiento son información de la empresa.

[^skh-tsmc]: [Anuncio de colaboración entre SK hynix y TSMC en HBM4](https://www.prnewswire.com/news-releases/sk-hynix-partners-with-tsmc-to-strengthen-hbm-technological-leadership-302120755.html), 2024-04-18. Anuncio de la orientación de desarrollo de entonces.

[^tf-basedie]: [Noticia de TrendForce sobre dados base HBM4E de SK hynix](https://www.trendforce.com/news/2026/08/31/news-sk-hynix-reportedly-weighs-intel-for-hbm4e-base-dies-amid-tsmc-cost-pressure-and-supply-diversification/), 2026-08-31. Cita medios coreanos; la empresa no lo confirmó.

[^nvda-nvhbm]: [Anuncio de NVIDIA NVHBM](https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory/), 2026-08-26. Las cifras de ancho de banda y consumo son afirmaciones de la empresa.

[^sec-hotchips]: [Resumen de ServeTheHome de la presentación de Samsung Electronics en Hot Chips 2026](https://www.servethehome.com/samsung-evolving-hbm-base-die-at-hot-chips-2026/), 2026-08-23. La hoja de ruta procede de la empresa y no incluye calendario.

[^sec-ir]: [Material explicativo de resultados del segundo trimestre de 2026 de Samsung Electronics](https://images.samsung.com/kdp/ir/events/2026/2026_2Q_conference_kor.pdf), 2026-07-30. Ingresos del negocio de semiconductores: KRW 127,5 billones; beneficio operativo: KRW 89,2 billones. Se cita la demanda de dados base de HBM entre los factores de resultados de la fundición.

[^skh-q2]: [Resultados del segundo trimestre de 2026 de SK hynix](https://news.skhynix.com/en/q2-2026-business-results/), 2026-07-29. Ingresos: KRW 79,3 billones; beneficio operativo: KRW 60,5 billones; beneficio neto: KRW 93,9 billones; contratos de suministro a largo plazo y SOCAMM2.

[^tf-cxl]: [Noticia de TrendForce sobre CXL 3.2 en Samsung y SK hynix](https://www.trendforce.com/news/2026/07/21/news-samsung-reportedly-targets-2026-cxl-3-2-mass-production-sk-hynix-advances-new-ai-memory-architecture/), 2026-07-21. Información secundaria.

[^hbf-ocp]: [Primera especificación OCP de HBF publicada por Sandisk y SK hynix](https://www.storagenewsletter.com/2026/08/05/fms-2026-sandisk-and-sk-hynix-advance-global-standardization-of-high-bandwidth-flash-with-release-of-first-ocp-technical-specification/), 2026-08-05.

[^sec-fms]: [Resumen de StorageReview de la presentación de Samsung Electronics en FMS 2026](https://www.storagereview.com/news/samsung-outlines-3d-memory-roadmap-for-ai-infrastructure-at-fms-2026), 2026-08-04. Presentación de memoria de bajo consumo con PIM; no se confirmó la fecha de producción en serie.

[^skh-hybrid]: [Noticia de Tom's Hardware sobre la presentación de SK hynix en Hot Chips 2026](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling), 2026-08-24.

[^tf-cxl-doubt]: [Noticia de TrendForce sobre AI Infrastructure Summit](https://www.trendforce.com/news/2026/09/18/news-openai-intel-reportedly-downplay-cxl-as-hbm-replacement-citing-use-case-and-data-transfer-limits/), 2026-09-18. Información secundaria.

[^qcom-hbc]: [Anuncio de la hoja de ruta de centros de datos de Qualcomm](https://www.qualcomm.com/news/releases/2026/06/qualcomm-unveils-comprehensive-data-center-roadmap-for-the-agent), 2026-06. Las cifras de rendimiento son de la empresa y aún no cuentan con verificación independiente.

[^sndk-call]: [Transcripción republicada de la llamada de resultados del cuarto trimestre FY2026 de Sandisk](https://www.fool.com/earnings/call-transcripts/2026/08/12/sandisk-sndk-q4-2026-earnings-call-transcript/), llamada del 2026-08-05.

[^naver-sec]: [Cotización diaria de Samsung Electronics en Naver Finance](https://m.stock.naver.com/api/stock/005930/price?pageSize=5&page=1) y [estimaciones de resultados anuales](https://m.stock.naver.com/api/stock/005930/finance/annual), consultadas el 2026-10-05. Cierre del 10-02: KRW 276.000; beneficio por acción previsto para 2026: KRW 47.142.

[^naver-skh]: [Cotización diaria de SK hynix en Naver Finance](https://m.stock.naver.com/api/stock/000660/price?pageSize=5&page=1) y [estimaciones de resultados anuales](https://m.stock.naver.com/api/stock/000660/finance/annual), consultadas el 2026-10-05. Cierre del 10-02: KRW 1.842.000; beneficio por acción previsto para 2026: KRW 350.576.

[^skh-lta]: [Noticia de Newspim sobre la llamada de resultados del segundo trimestre de SK hynix](https://www.newspim.com/news/view/20260729000198), 2026-07-29. La declaración sobre depósitos se verificó en esta noticia.

[^sec-lta]: [Transcripción completa de la llamada de resultados del segundo trimestre de Samsung Electronics en The Elec](https://www.thelec.kr/news/articleView.html?idxno=60316), 2026-07-30. La proporción y la estructura de contratos a largo plazo son planes de la dirección.

[^tf-memory]: [Previsión de TrendForce de los precios contractuales de memoria para el cuarto trimestre de 2026](https://www.trendforce.com/presscenter/news/20260930-13258.html), 2026-09-30. Es una previsión, no un precio realizado.

[^skh-return]: [Noticia de ZDNet Korea sobre la cancelación de acciones propias de SK hynix](https://zdnet.co.kr/view/?no=20260819161157), 2026-08-19. No se contrastó el documento regulatorio original.

[^sec-return]: [Noticia sobre el anuncio de retribución al accionista de Samsung Electronics para 2026](https://v.daum.net/v/20260821172850433), 2026-08-21. Es un plan, no una cantidad ya distribuida.

[^mu-foundry]: [Noticia de The Elec sobre la externalización del dado base de Micron](https://www.thelec.net/news/articleView.html?idxno=14372), 2026-10-02. Los comentarios preparados por Micron no indican el nombre de la fundición.

[^tf-hbm]: [Previsión de TrendForce sobre HBM en 2027](https://www.trendforce.com/presscenter/news/20260929-13255.html), 2026-09-29. Previsión de una entidad de análisis.

[^turboquant]: [Presentación de Google Research sobre TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/), 2026-03-24. Resultado de investigación; no se ha confirmado el alcance de su aplicación comercial.

[^anthropic-context]: [Documentación de Anthropic sobre ventanas de contexto](https://platform.claude.com/docs/en/build-with-claude/context-windows) y [documentación sobre compactación](https://platform.claude.com/docs/en/build-with-claude/compaction), consultadas el 2026-10-05.

[^anthropic-autonomy]: [Estudio de Anthropic sobre la medición de autonomía de agentes](https://www.anthropic.com/research/measuring-agent-autonomy), 2026-02-18. Percentil 99,9 de datos de uso propios.

[^tf-supply]: [Previsión de TrendForce sobre oferta y demanda de memoria para 2026-2027](https://www.trendforce.com/presscenter/news/20260730-13158.html), 2026-07-30. Previsión de una entidad de análisis.

[^tf-china]: [Noticia de TrendForce sobre ampliaciones de capacidad de CXMT y YMTC](https://www.trendforce.com/news/2026/09/24/news-cxmt-ymtc-ramp-memory-capacity-but-chinas-ai-cloud-boom-could-soak-up-new-supply-through-2027/), 2026-09-24. Información secundaria.

[^bis]: [Discurso del director del Banco de Pagos Internacionales](https://www.bis.org/speeches/20260910-artificial-intelligence-growth-and-financial-stability-challenges-central-banks), 2026-09-10.

[^consensus]: [Noticia de MoneyToday sobre las previsiones de resultados del tercer trimestre](https://www.mt.co.kr/amp/stock/2026/10/05/2026100217315021825), 2026-10-05. Cita estimaciones recopiladas por FnGuide.

*Aviso: Este material se ofrece con fines de investigación e información. Las empresas, los múltiplos y los escenarios son ejemplos de análisis; cada lector debe evaluar por separado sus decisiones de inversión.*
