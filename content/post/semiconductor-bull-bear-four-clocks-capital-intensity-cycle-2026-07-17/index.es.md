---
title: "El verdadero debate en semiconductores: cuatro relojes físicos y un reloj bursátil"
slug: "semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17"
date: 2026-07-17T11:00:00+09:00
description: "Los alcistas y bajistas de semiconductores ya no discuten si existe demanda de IA. Las preguntas reales son si la demanda supera a la oferta y las mejoras de eficiencia, si se estrechan los desfases entre precio, pedidos, construcción y monetización, y si los ingresos incrementales sobreviven a la depreciación y al coste de capital hasta llegar al flujo de caja del accionista. La vía central es un alcista fundamental que convive con un bajista de valoración."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["Semiconductores", "Memoria", "HBM", "AI CAPEX", "TSMC", "Samsung Electronics", "SK Hynix", "Micron", "Empaquetado avanzado", "Intensidad de capital", "Valoración"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexto
> Este artículo es la pieza que integra en un solo marco los ejes que hemos tratado por separado hasta ahora. La evidencia de demanda se trató en [Por qué el fallo de resultados de IBM es evidencia de la fortaleza de la memoria](/es/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/), la difusión de la oferta en [La brecha de suministro que se extiende más allá del HBM](/es/post/memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14/), el tamaño de la oferta y la demanda en [Investigación profunda de oferta-demanda de HBM 2030](/es/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/), la capacidad de pago en [¿Quién paga el consenso de semiconductores de 2027?](/es/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/), y la valoración en [El peor escenario ya es el precio](/es/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/). Los hubs relacionados son el [Hub de IA y HBM](/es/page/korea-semiconductor-hbm-kospi-hub/) y el [Hub de Exclusive Analysis](/es/page/exclusive-analysis-hub/).

## TL;DR

* Los alcistas y bajistas de semiconductores ya no discuten si "existe o no demanda de IA". Los pedidos oficiales, la escasez de TSMC en procesos de vanguardia y empaquetado avanzado, las restricciones de suministro de memoria de Dell y HPE, y el CAPEX de los hyperscalers apuntan todos hacia el mismo lado: <strong>la demanda real de IA es fuerte</strong>.
* El verdadero debate tiene tres frentes. Si el crecimiento de la demanda supera a la oferta y a las mejoras de eficiencia. Si se estrechan los desfases entre precio, pedidos, construcción y monetización. Si el aumento de ingresos sobrevive a la depreciación, al coste financiero y a la competencia hasta convertirse en flujo de caja para el accionista.
* El bull más sólido sostiene que "a medida que la IA se convierte en la nueva capa base de toda la computación, los cuellos de botella físicos duran más de lo esperado, y los contratos a largo plazo junto con el oligopolio crean un <strong>suelo</strong> de beneficios elevado".
* El bear más sólido sostiene que "la demanda de IA sigue creciendo, pero en el <strong>momento en que la tasa de crecimiento pasa su punto máximo</strong>, la oferta, la depreciación y el coste de capital suben a la vez, y el precio, el margen, el ROIC y el múltiplo se normalizan".
* La vía con mayor probabilidad hoy es mixta. <strong>La industria puede ser alcista mientras la acción es bajista en valoración</strong> (probabilidad del 55%). Aunque los resultados de 2026-2027 sean sólidos, la acción descuenta primero la respuesta de oferta y el retraso en la recuperación de la inversión de 2027-2028. \[Alcance\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Marco clave</div>
  <div class="thesis-callout__body">
    La industria de semiconductores de IA todavía no está rota. Pero el scarcity cycle se está desplazando hacia un capital-intensity cycle. El próximo repunte no comenzará con un anuncio de CAPEX, sino cuando la conexión eléctrica, la utilización y el flujo de caja de IA logren alcanzar la depreciación y el coste de capital.
  </div>
</div>

---

## 1. Principio de análisis: no mezclar las cuatro preguntas

El debate sobre semiconductores suele equivocarse porque combina cuatro preguntas distintas en una sola frase.

1. <strong>Industria</strong>: ¿crece a largo plazo la demanda de cómputo de IA y de memoria?
2. <strong>Beneficio corporativo</strong>: ¿mantienen los proveedores actuales precios y márgenes altos gracias a esa demanda?
3. <strong>Precio de la acción</strong>: ¿cuánto del beneficio futuro y del riesgo ya descuenta el precio actual?
4. <strong>Cartera</strong>: incluso siendo una buena empresa, ¿tiene sentido seguir aumentando la posición dado el nivel actual de concentración y de caja?

El hecho de que "la demanda de IA es fuerte" responde a la pregunta de industria, pero no responde a las preguntas de precio y de cartera. A la inversa, el hecho de que "el SOXX se desplomó" habla del timing de la acción, pero no demuestra de inmediato el colapso de la demanda de la industria.

Si no se respeta esta distinción, el alcista compra una buena industria a cualquier precio, y el bajista declara el fin de la industria por una caída de un solo día.

<strong>Nota de alcance</strong>: el alcance central de este artículo es la memoria, la fundición de vanguardia, el empaquetado avanzado, los fabless de IA, las redes y sus equipos y materiales relacionados, todos ellos impulsados por la IA. Automoción, industrial, analógico y los procesos maduros generales solo se tratan en la medida en que se conectan con la cadena de suministro de IA. Por lo tanto, este juicio no debe aplicarse por igual a todos los subsegmentos de semiconductores.

---

## 2. Cuatro relojes físicos y un reloj bursátil

En este mercado hay cinco relojes que avanzan a velocidades distintas. Este marco es el esqueleto de todo el artículo.

| Reloj | Qué mide | Significado actual |
|---|---|---|
| Reloj de precio | ASP de contratos de memoria, mix, precios de fundición y empaquetado | Se refleja más rápido en los resultados actuales |
| Reloj de inversión | Pedidos de GPU, obleas, equipos y fábricas; CAPEX | Reserva la oferta futura y la voluntad del cliente |
| Reloj de construcción | Conexión eléctrica, finalización de centros de datos, instalación de racks, ramp de fábricas | Convierte la inversión anunciada en capacidad operativa real |
| Reloj de monetización | Ingresos de IA y de la nube, margen bruto, FCF | Recupera el capital invertido, la depreciación y el coste financiero |
| Reloj bursátil | Se adelanta 6-12 meses a los cuatro relojes anteriores | Se mueve primero y descuenta la tasa de cambio |

Cuando el reloj de precio y el de inversión se adelantan mientras el de construcción y el de monetización se retrasan, <strong>unos buenos resultados y una revisión al alza del CAPEX pueden convertirse en motivo de venta.</strong> Esto ocurre porque el mercado mira más allá del beneficio actual, hacia la capacidad ociosa futura, la depreciación, la deuda y el vacío de retorno sobre la inversión.

A la inversa, cuando los cuatro relojes se estrechan, la fase alcista se reactiva. Esto sucede cuando los GW anunciados se convierten en conexión eléctrica real y en utilización efectiva de GPU, cuando el crecimiento del margen bruto de IA supera a la depreciación y al gasto por intereses, y cuando las compras anticipadas de los clientes se consumen como uso real y no como inventario.

Con este marco, preguntas que antes parecían inconexas se explican dentro de la misma estructura. Por qué los resultados son buenos pero la acción cae. Por qué el CAPEX aumenta pero la acción del cliente se debilita. Por qué, en plena escasez de oferta, las acciones de equipos son las primeras en quebrarse.

---

## 3. Las premisas comunes que comparten bull y bear

Los bulls y bears más sofisticados coinciden, en general, en los siguientes hechos.

1. La demanda de entrenamiento e inferencia de IA es real hoy.
2. Existen cuellos de botella físicos en procesos de vanguardia, HBM, empaquetado avanzado, energía y redes.
3. Es probable que los resultados de la cadena de suministro sean sólidos en 2026-2027.
4. La acción mira antes la tasa de cambio de las estimaciones de beneficio y la siguiente fase de oferta que el resultado absoluto.
5. No todos los semiconductores se benefician por igual.
6. Una buena industria y un buen momento de compra no son lo mismo.

Por lo tanto, el punto en disputa entre ambos bandos no es la existencia de la demanda, sino <strong>su duración y calidad, la velocidad de la respuesta de oferta, la rentabilidad de los ingresos incrementales, y la valoración y el posicionamiento actuales</strong>.

---

# Parte I. La tesis alcista (Bull Case)

> <strong>A medida que la IA deja de ser una función de software más y se convierte en la nueva capa base de toda la computación, crecen a la vez la demanda de cómputo, capacidad de memoria, ancho de banda, redes y energía. La oferta no puede seguir el ritmo de inmediato por los largos plazos de espera en fábricas, empaquetado, energía y certificación de clientes, y los proveedores oligopólicos junto con los contratos a largo plazo generan un suelo de beneficios más alto y más duradero que en el pasado.</strong>

El núcleo del bull no es que el precio se acelere para siempre. El argumento es que, aunque la tasa de subida del precio se desacelere, la combinación de un ASP más alto que en el pasado, un mix premium, visibilidad de volumen y disciplina de capital puede ampliar <strong>el área del beneficio</strong>.

### 4. La demanda se está verificando con pedidos físicos, no con anuncios

En la conferencia del 2T26 de TSMC, lo más importante no son las declaraciones optimistas de largo plazo, sino <strong>el cambio real en el CAPEX y en la asignación de capacidad</strong>. \[Hecho/Grado B: notas trasladadas de la conferencia y cruce con varios informes de research, contraste directo limitado con el texto original de RI\]

- Elevó la guía de crecimiento de ingresos de FY2026 a más del 40%
- Elevó el CAPEX de 2026 a 60.000-64.000 millones USD
- Explicó que la brecha entre oferta y demanda es amplia en procesos de N3 e inferiores y en empaquetado avanzado
- Señaló que no se limita a sumar los pedidos de los clientes, sino que verifica la ubicación del centro de datos, el avance de la construcción, la energía asegurada y la instalación de racks

Esta combinación daña la tesis bajista débil de que se trata de "pedidos fantasma" o de que "toda la demanda de IA es un pedido duplicado". La decisión de TSMC de comprar equipos y construir fábricas es difícil de tomar sin señales de demanda a largo plazo del cliente, anticipos y hojas de ruta de desarrollo conjunto.

Que Dell y HPE señalen la DRAM y la NAND como la principal restricción de oferta de servidores, y que Teradyne confirme una fuerte demanda de test de HBM y DRAM para el segundo semestre, apunta en la misma dirección. \[Hecho/Grado C-B: broker channel check\] La demanda no vive solo en las diapositivas, sino que aparece en los envíos de servidores, la asignación de memoria y la capacidad de equipos de test y empaquetado.

<strong>Lectura bull</strong>: la evidencia más importante de la demanda de IA no es la proyección de ingresos, sino el hecho de que los proveedores están comprometiendo <strong>capital difícil de revertir</strong>.

<strong>Condición de refutación</strong>: que los hyperscalers recorten realmente el CAPEX. Que TSMC y las memoreras retrasen la llegada de equipos y el ramp de fábricas. Que aparezcan a la vez retrasos en contratos de clientes y caída de la utilización.

### 5. La demanda se expande de un solo tipo de GPU al BOM completo del servidor

La inversión inicial en IA se concentró en GPU y HBM, pero a medida que crece la escala, el cuello de botella se desplaza hacia CPU, redes, almacenamiento, gestión de energía, sustratos y componentes pasivos.

- La IA agéntica utiliza a la vez GPU, CPU, memoria, redes y almacenamiento.
- La inferencia a gran escala aumenta la demanda de KV cache y de ancho de banda de memoria.
- A medida que la expansión pasa de scale-up a scale-out y scale-across, crece la demanda de switches de alta velocidad, óptica y conexiones coherentes.
- El eSSD, los IC de gestión de energía, los MLCC y los sustratos ABF, CCL y PCB de alta capa de los centros de datos de IA se convierten en cuellos de botella rezagados.

Por lo tanto, aunque la tasa de crecimiento de NVIDIA como valor individual se desacelere, el mercado total direccionable de semiconductores de IA puede ampliarse hacia otros componentes. Los ASIC propios tampoco anulan del todo esta lógica. TPU y Trainium pueden reducir la cuota de GPU, pero siguen consumiendo procesos de vanguardia, HBM o DRAM de alto rendimiento, empaquetado avanzado y redes.

<strong>Lectura bull</strong>: la inversión en IA evoluciona del ciclo de GPU al <strong>ciclo del BOM del centro de datos de IA</strong>. El liderazgo puede cambiar, pero la demanda total de silicio, memoria y empaquetado se mantiene.

<strong>Condición de refutación</strong>: que la mejora de eficiencia aumente el rendimiento pero reduzca el gasto en dólares de servidores, memoria y redes, y que este fenómeno se repita en múltiples clientes.

### 6. El HBM es un producto que erosiona su propia oferta

El HBM requiere más área de oblea, TSV y apilamiento, empaquetado, test y certificación de clientes. Cuando sube el mix de HBM, se reduce la cantidad de bits que se pueden producir con el mismo input de obleas, y también se restringe la capacidad de DRAM de propósito general.

Esto genera dos efectos alcistas. Primero, la oferta del propio HBM no puede crecer con rapidez. Segundo, la conversión hacia HBM reduce la oferta efectiva de DRAM de propósito general y sostiene a la vez los precios de la DRAM de servidor y de la DRAM convencional.

Tampoco una nueva fábrica se convierte en oferta en cuanto se anuncia. Se necesitan, en secuencia, energía, agua, sala limpia, instalación de equipos, ramp del proceso, rendimiento y certificación de clientes. Existe un desfase hasta que la nueva planta Y1 de SK Hynix y las nuevas instalaciones de Samsung Electronics y Micron contribuyan a la oferta real de bits.

<strong>Lectura bull</strong>: la escasez de este ciclo es una <strong>escasez compuesta que exige a la vez buenas obleas, apilamiento de alto rendimiento, empaquetado verificado y certificación de clientes</strong>. Por eso no se resuelve de inmediato con solo inyectar dinero.

<strong>Condición de refutación</strong>: que el rendimiento del HBM y la productividad del empaquetado suban más rápido de lo esperado, y que la certificación de clientes de Samsung Electronics y Micron se traduzca en volúmenes a gran escala, de modo que la tasa de crecimiento de la oferta supere a la demanda.

### 7. El oligopolio y los contratos a largo plazo pueden reducir la amplitud del ciclo

La industria de memoria tiene menos proveedores que en el pasado, y el HBM implica un desarrollo conjunto y una certificación profundos por cliente. El LTA obliga a renunciar a una parte del repunte del precio spot, pero aumenta la visibilidad de volumen, el lock-in del cliente y la confianza en la inversión.

El ciclo pasado tenía una estructura en la que el proveedor ampliaba capacidad en respuesta al precio spot, el cliente acumulaba inventario y luego el precio colapsaba. Si el contrato a largo plazo incluye volumen mínimo, una fórmula de ajuste de precio y una naturaleza de take-or-pay, <strong>el techo del beneficio puede bajar, pero su suelo y su duración pueden subir.</strong>

Lo que compra el bull no es "el precio sigue subiendo cada vez más rápido", sino el supuesto de que "el beneficio elevado dura más tiempo".

<strong>Punto clave no verificado</strong>: el suelo y el techo de precio del LTA, el volumen mínimo, la renegociación y las cláusulas de cancelación son, en su mayoría, no públicos. No se debe elevar el LTA a una garantía incondicional de beneficio. \[Bloqueado\]

### 8. El foso de los procesos de vanguardia está en la curva de aprendizaje, no en el equipo

La frase del presidente C.C. Wei de TSMC, "elegir una fundición no es como elegir leche en una tienda de conveniencia", describe con precisión el coste de cambio de los procesos de vanguardia.

El cliente recorre junto al proveedor, durante años, la elección del proceso, el diseño de PDK e IP, los chips de prueba, la co-optimización, el aprendizaje del rendimiento, el aseguramiento de capacidad y, finalmente, la producción en volumen. Que dos fundiciones posean el mismo equipo de ASML no hace que el cliente se cambie de inmediato. El empaquetado avanzado también exige resolver a la vez el sustrato, el calor, la energía, la integridad de la señal y el test.

<strong>Lectura bull</strong>: aunque el semiconductor de vanguardia parezca un commodity, no es un producto plenamente genérico debido al coste de cambio del cliente y al aprendizaje conjunto. Aun cuando la oferta aumente, el exceso de beneficio del líder verificado puede durar más de lo esperado. En un período de escasez de oferta, el cliente elige al <strong>proveedor que cumple el calendario y el rendimiento</strong>, más que al proveedor más barato.

### 9. La escasez de energía y de permisos retrasa la demanda, pero puede no destruirla

El retraso en la conexión eléctrica y en la construcción de centros de datos es el argumento central del bear. Pero el bull lo interpreta no como ausencia de demanda, sino como <strong>un backlog que espera para entrar en operación</strong>.

El operador que ha asegurado energía, terreno, subestación y refrigeración posee un activo escaso. Mientras la demanda se mantiene, el retraso en la construcción puede manifestarse como una postergación del plazo de entrega y una prima de precio, más que como una cancelación de pedidos. La explicación de TSMC de que verifica la ubicación del centro de datos y el aseguramiento de energía del cliente es, al menos, evidencia de que el reloj de construcción de los clientes de primer nivel no se ha detenido por completo.

<strong>Condición bull</strong>: que los proyectos retrasados no se cancelen sino que entren en operación de forma secuencial, y que, tras la puesta en marcha, se traduzcan en una alta utilización y en ingresos de nube.

### 10. El avance de China es un riesgo para el segmento general, pero difícilmente sustituya la frontera a corto plazo

La OPV de CXMT y su captación de capital a gran escala son un riesgo de oferta de DRAM convencional a mediano y largo plazo. Pero en HBM, procesos de vanguardia y empaquetado avanzado existen barreras de rendimiento, equipos, materiales, ecosistema de diseño y certificación de clientes.

Las restricciones de Estados Unidos a la exportación de equipos a China y el debate sobre limitar las compras a CXMT y YMTC pueden retrasar la expansión global de clientes de las empresas chinas y reforzar la posición de mercado ex-China de los proveedores de Corea, Estados Unidos y Taiwán.

<strong>Lectura bull</strong>: la oferta china es menos un problema de "colapso del HBM hoy" que de <strong>"techo del precio de la DRAM convencional a partir de 2028"</strong>. El desfase tecnológico y de certificación es demasiado largo para dañar al bull de corto plazo.

### 11. Los datos reales de exportación confirman la fortaleza

Según la cifra preliminar del Servicio de Aduanas de Corea para el 1-10 de julio de 2026, las exportaciones de semiconductores fueron sólidas, con 11.200 millones USD. En las exportaciones de DRAM/HBM de Corea a Taiwán en junio, el proxy de HBM ajustado por línea base también mantuvo una señal constructive. \[Hecho/Grado A-B: dato oficial de aduanas, el proxy es medium\]

Este dato no demuestra de forma directa los ingresos de HBM por empresa, pero al menos refuta la afirmación de que el momentum de los envíos de semiconductores de Corea se quebró de forma abrupta.

<strong>Advertencia</strong>: la cifra preliminar de diez días es una alerta temprana. No debe elevarse a una tesis de largo plazo antes de confirmar la atribución por partida y por empresa, y el efecto base de fin de mes.

### 12. Un múltiplo bajo puede reflejar ya una normalización parcial del beneficio

Las acciones de memoria son una industria a la que el mercado asigna un P/E bajo en su beneficio pico. Por lo tanto, un P/E bajo por sí solo no es prueba de que esté barata. Sin embargo, si el mercado descuenta en exceso la persistencia del beneficio de 2027 y el suelo real del beneficio resulta más alto que en el pasado, la acción puede subir por <strong>normalización del múltiplo</strong> aunque el EPS no siga creciendo.

La asimetría del bull no es "sube solo si el precio sigue acelerando". Es que, si el precio de contrato se estabiliza en un nivel alto, si el LTA y el mix premium sostienen el FCF, y si se confirma la disciplina del proveedor, el mercado puede otorgar no un peak multiple sino un <strong>durable earnings multiple</strong>.

---

# Parte II. La tesis bajista (Bear Case)

> <strong>La demanda de IA no desaparece. Pero cuando la tasa de crecimiento de la demanda pasa su punto máximo, si la normalización de las compras anticipadas, la nueva oferta, la depreciación y el coste de capital del cliente aparecen a la vez, el margen incremental del proveedor y el múltiplo de la acción se comprimen juntos. La industria puede seguir creciendo mientras el accionista experimenta una rentabilidad baja.</strong>

El núcleo del bear no es el colapso de los ingresos, sino <strong>el deterioro de la rentabilidad de los ingresos incrementales</strong>. Aunque sigan llegando buenas noticias, si la magnitud de las revisiones al alza del EPS se reduce y la valoración baja, la acción cae primero.

### 13. La acción juzga primero la tasa de cambio, no el resultado absoluto

El pico del 4T26 en el material de Morgan Stanley se lee con más precisión como <strong>el punto máximo de la tasa de subida interanual del precio de contrato</strong>, no como el precio absoluto de la memoria. \[Grado C/bajo-medio: definición de precio y supuestos del texto original sin verificación directa\] Aunque el precio siga subiendo y el EPS siga creciendo, si la magnitud del alza se reduce, la acción puede quebrarse primero.

Las acciones de semiconductores son más sensibles a la segunda derivada que a la primera.

- Aumento de ingresos: puede ser un hecho ya conocido.
- Aumento del EPS: puede que ya esté reflejado en el consenso.
- Desaceleración de la magnitud de la revisión al alza del EPS: es información nueva y es negativa para la acción.

La debilidad de los semiconductores en julio de 2026 no confirma el colapso de la industria, pero el hecho de que la acción no reaccionara ni siquiera ante buenos resultados de TSMC y comentarios positivos sobre la demanda de IA muestra que <strong>la utilidad marginal de las expectativas ha desaparecido</strong>.

### 14. Los Rush order y las restricciones de oferta pueden adelantar demanda futura

Las restricciones de oferta de DRAM y NAND de Dell y HPE, y los Rush order de los OEM de servidores, son evidencia de la fortaleza actual de la demanda. \[Grado C-B: nota trasladada de BofA\] Al mismo tiempo, pueden ser una señal de fase tardía del ciclo, en la que el cliente adelanta pedidos por temor a la escasez y a la subida de precios.

Cisco, en respuesta al aumento del coste de memoria, tomó las siguientes medidas. \[Grado C-B: nota trasladada de JPM\]

- Compromisos de compra anticipada de memoria
- Subidas de precio de producto
- Reducción de la memoria instalada dentro de los switches
- Suspensión de algunas operaciones de servidores

Esto es más importante que una simple acumulación de inventario: es una <strong>conducta inicial de destrucción de demanda</strong>. En el [caso de IBM](/es/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/) también, a medida que los clientes desviaron presupuesto hacia la compra anticipada de servidores, almacenamiento y memoria, se retrasaron algunos contratos de software y de sistemas. \[Hecho/Grado A: IBM 8-K\]

Si los envíos actuales representan consumo final, los pedidos se mantendrán incluso después de que la oferta se normalice. Si, en cambio, son compras anticipadas, se producirá un vacío de pedidos durante el período de consumo del inventario.

### 15. Si el precio sube demasiado, destruye su propia demanda

La subida del precio de la memoria beneficia los resultados del proveedor, pero eleva el BOM del cliente y el precio del producto. Los clientes de PC, smartphones y servidores generales sensibles al precio pueden reducir especificaciones o postergar la compra.

El material de la conferencia de TSMC explicó que la subida del precio de los componentes está presionando a los mercados finales de consumo y a los sensibles al precio. Aunque la demanda de gama alta de los centros de datos de IA sea fuerte, si la demanda de TI de propósito general es débil, la polarización dentro de la industria se agudiza.

El riesgo que ve el bear no es que "la demanda de HBM desaparezca". Es que el precio elevado del HBM y de la DRAM de servidor impulse en el cliente <strong>diseños alternativos, la optimización de memoria, el ajuste del momento de compra y la contracción de la demanda de productos de propósito general</strong>.

### 16. Cuando la escasez es más intensa, la respuesta de oferta también es mayor

La revisión al alza del CAPEX de TSMC, la ampliación de capacidad de las tres memoreras y la expansión de la capacidad de empaquetado avanzado y test son, a la vez, evidencia de la demanda actual y <strong>semillas de la oferta futura</strong>.

En 2027-2028 podrían coincidir los siguientes factores.

- Aumento del input de obleas de las nuevas fábricas
- Mejora del rendimiento de HBM y de la productividad del apilamiento
- Alivio del cuello de botella del empaquetado avanzado
- Aumento de la cuota de HBM4 de Samsung Electronics y Micron
- Expansión de la oferta de DRAM convencional de CXMT

Cuando se resuelve el cuello de botella, los envíos de toda la industria aumentan, pero la scarcity premium de los ganadores actuales se reduce. Aunque SK Hynix venda más volumen, la prima de precio del HBM y el margen incremental pueden bajar.

<strong>El alivio del cuello de botella es una buena noticia para el cliente y para la industria, pero puede ser una mala noticia para el exceso de beneficio de los proveedores actuales.</strong>

### 17. El cuello de botella del CAPEX de IA se desplaza del chip al coste de capital

La cifra de Citi de 801.000 millones USD de CAPEX combinado de Alphabet, Meta y Amazon para 2027 no es una guía de las empresas, sino una estimación agresiva de analistas. \[Grado C-B\] Esta cifra importa menos por su magnitud que por lo que implica el modelo: <strong>que el FCF de las tres compañías pasa a ser negativo en 2027-2028</strong>.

Según los datos oficiales del FY2026 de Oracle, la situación es esta. \[Hecho/Grado A: SEC 10-K\]

| Partida | Monto |
|---|---:|
| CAPEX | 55.700 millones USD |
| Flujo de caja operativo | 32.000 millones USD |
| FCF simple | ~-23.700 millones USD |
| Deuda total | 129.500 millones USD |

Aunque exista demanda de IA, la capacidad de inversión del cliente no es infinita. El CAPEX que supera el flujo de caja depende de bonos corporativos, leasing, financiación de proyectos y ampliaciones de capital. Si los tipos de interés, los diferenciales de crédito y la acción se deterioran a la vez, los planes a partir de 2027 podrían ser los primeros en ajustarse.

El Take-or-Pay y el RPO tampoco son una red de seguridad completa. Garantizan los ingresos del cliente, pero al mismo tiempo aumentan la obligación de construcción de instalaciones y la carga de financiación del proveedor.

<strong>Corrección importante</strong>: el cuello de botella del coste de capital no es, hoy, un colapso de demanda confirmado. Dado que TSMC y los hyperscalers siguen elevando el CAPEX, debe clasificarse como <strong>riesgo futuro</strong>.

### 18. El aumento del uso de IA y el aumento de los ingresos en dólares de semiconductores no son lo mismo

La cuantización, la sparsity, la reutilización de caché, el speculative decoding, el CXL, la agrupación de memoria (pooling) y la optimización de software reducen el coste de hardware necesario "por unidad de inteligencia".

Si el uso total crece más rápido que la mejora de eficiencia, la demanda de semiconductores sigue creciendo. Pero si la velocidad de ambos se iguala, aunque el volumen de tokens e inferencia explote, <strong>la tasa de crecimiento de los ingresos en dólares de los fabricantes de chips puede desacelerarse</strong>.

Los ASIC propios son un riesgo directo de cuota para NVIDIA y para los aceleradores de propósito general. Para la memoria el riesgo es menos directo, pero cada cliente puede optimizar su jerarquía de memoria y ancho de banda, reduciendo el contenido de HBM o su elasticidad de precio.

### 19. La monetización de IA puede no seguir el ritmo de la depreciación y el coste financiero

Las GPU y los centros de datos generan ingresos <strong>después de entrar en operación</strong>, no en el momento del pedido. Si se retrasa la conexión eléctrica y la instalación de racks, el capital se invierte primero y el ingreso llega después.

Cuanto más se retrasa el reloj de monetización, más se acumulan los siguientes costes.

- Depreciación de nuevas fábricas, servidores e instalaciones de energía
- Intereses de bonos corporativos, leasing y financiación de proyectos
- Obsolescencia económica y riesgo de deterioro de GPU antiguas
- Debilitamiento del poder de negociación por concentración de clientes
- Baja rotación de activos por capacidad ociosa

CoreWeave es un caso que muestra cómo, aun con una demanda de IA fuerte, el coste de capital puede erosionar el valor para el accionista. \[Hecho/Grado A: SEC\]

| Partida | 1T26 |
|---|---:|
| Ingresos | 2.078 millones USD |
| CAPEX | 7.695 millones USD |
| Gasto financiero neto | 536 millones USD |
| Concentración de los dos principales clientes | 65% |

Un RPO elevado no elimina el alto coste de financiación ni la obligación de construir. Todavía no hay evidencia de que esta vulnerabilidad se contagie a todo el conjunto de hyperscalers. Pero si la periferia apalancada, como las neocloud y compañías como Oracle, se tambalea primero, la demanda marginal de pedidos de semiconductores podría debilitarse.

### 20. El capital chino puede debilitar la disciplina de oferta en la fase bajista del ciclo

La gran OPV de CXMT no es, de inmediato, un evento que genere competitividad en HBM. Su significado más importante es que <strong>ha asegurado el capital para continuar el desarrollo tecnológico y la expansión de capacidad incluso en una fase bajista del sector</strong>.

Un proveedor de tipo economía de mercado reduce el CAPEX cuando bajan el precio y la rentabilidad. Un proveedor que prioriza objetivos de política y la sustitución nacional puede optar por ampliar su cuota incluso con baja rentabilidad. Si CXMT sustituye a la DRAM convencional en el mercado interno chino, los proveedores globales pueden asignar más volumen a los mercados fuera de China, lo que presiona el techo del precio.

### 21. Los ingresos pueden seguir creciendo mientras el margen incremental se quiebra

En la fase alcista, el precio, la utilización y el mix de HBM elevan el margen a la vez. En la fase bajista, el mismo apalancamiento opera en sentido contrario.

- Aumento de la depreciación de nuevas fábricas y equipos
- Costes iniciales de ramp de N2 y de fábricas en el extranjero
- Reducción de la prima de precio por la mejora del rendimiento de HBM y la mayor competencia
- Reducción de especificaciones y resistencia de precio por parte del cliente
- Aumento de la oferta de DRAM y NAND convencionales
- Reducción de la scarcity rent por el alivio del cuello de botella de empaquetado y test

La pregunta más contundente del bear no es "si los ingresos crecen", sino <strong>"si cada unidad adicional de ingreso genera el mismo beneficio operativo que en el pasado"</strong>. Si el margen operativo incremental ya pasó su punto máximo, la acción puede sufrir un de-rating aunque el EPS siga aumentando.

### 22. El cambio de liderazgo del mercado sugiere un ajuste de expectativas propio de los semiconductores

A fecha del 16 de julio de 2026, el SOXX había caído cerca de un 19% desde su máximo de junio, y su rendimiento relativo frente al SPY en las últimas 20 sesiones también se había deteriorado con fuerza. Mientras la tendencia de corto plazo del QQQ y del índice de semiconductores se dañaba, el Dow y el S&P 500 de igual ponderación se mantenían relativamente fuertes. \[Grado B+: cruce de Yahoo/TradingView\]

Esto se parece más a una <strong>rotación selectiva</strong> de capital que sale del posicionamiento saturado en tecnología y semiconductores hacia financieras, salud, energía y valores de valor, que a un colapso generalizado de todo el mercado estadounidense.

No es evidencia de que la industria haya fracasado, pero sí es <strong>evidencia de que el mercado ya no compra la buena narrativa de la industria a cualquier precio</strong>. Si los semiconductores no suben ni con buenas noticias y otros sectores se fortalecen, el coste de oportunidad de la acción aumenta.

### 23. La concentración es un riesgo independiente de la tesis bull

Aunque el núcleo de la tesis de semiconductores sea correcto a largo plazo, si la exposición se concentra en memoria e infraestructura de IA, un único factor común puede sacudir toda la posición.

- Samsung Electronics, SK Hynix y Micron son valores distintos, pero están atados a un <strong>factor común: el precio de la DRAM y el CAPEX de IA</strong>.
- La óptica y los proveedores de equipos y materiales también reaccionan juntos al CAPEX de los hyperscalers y al ciclo risk-on/risk-off.
- Si falta liquidez, una caída brusca fuerza una acción, no una decisión.

Por lo tanto, hay que separar el principio de "mantener buenas empresas a largo plazo" del problema de "sobreponderar valores con una correlación alta entre sí". <strong>Ser bull de largo plazo no justifica la concentración.</strong>

---

## 24. Cómo leen bull y bear la misma evidencia de forma distinta

Esta tabla es la parte más práctica de todo el artículo. Ambos bandos leen la misma noticia en sentidos opuestos, y la última columna es la variable que realmente decide.

| Evidencia | Lectura bull | Lectura bear | Variable que realmente decide |
|---|---|---|---|
| CAPEX de TSMC de 60.000-64.000 millones USD | Verificación física de la demanda de IA a largo plazo | Aumento de oferta y depreciación en 2027-2028 | Utilización, precio, ROIC incremental |
| Rush order de DRAM de servidor | Escasez y demanda real fuertes | Adelanto de demanda futura | Inventario de cliente/canal y reórdenes |
| Mejora del rendimiento de HBM | Expansión de envíos y caída de costes | Reducción de la prima y de la scarcity rent | Si la mejora de costes es más rápida que la caída de precio |
| Expansión del LTA | Visibilidad de volumen y suelo de beneficio más alto | Límite al techo de precio y traslado de riesgo de crédito al cliente | Volumen mínimo, fórmula de precio, cláusulas de cancelación |
| Expansión de ASIC propios | El TAM de silicio de IA se expande más allá de la GPU | Caída de cuota y ASP de los aceleradores de propósito general | Consumo total de HBM, obleas y empaquetado |
| Retraso de energía y construcción | Demanda en espera y valor de un activo escaso | Retraso de ingresos, capacidad ociosa, acumulación de intereses | Tasa de cancelación, conexión eléctrica real, utilización |
| OPV de CXMT | Dificultad para sustituir el HBM a corto plazo | Continuidad de la expansión convencional incluso en fase bajista | Input de obleas, rendimiento de DDR5 y certificación de clientes |
| RPO y Take-or-Pay elevados | Visibilidad de ingresos a largo plazo | Obligación de financiación y de construcción, y concentración de clientes | Margen del contrato, garantías, cláusulas de cancelación y crédito |
| Explosión del uso de IA | Crecimiento estructural de la demanda total de semiconductores | Desaceleración de la elasticidad de ingresos en dólares por la mejora de eficiencia | Tasa de crecimiento del uso frente a la caída de coste por token |
| P/E bajo de memoria | La preocupación por el pico ya está reflejada | No es barato si el denominador es el EPS pico | Suelo de beneficio y duración del FCF |
| Caída brusca del SOXX | Desajuste temporal entre la industria y la acción | Desaparición de la utilidad marginal de las buenas noticias | Revisión del EPS y recuperación de la media móvil de 50 días |

---

## 25. Mapa bull / bear por cadena de valor

| Cadena de valor | Lógica bull | Lógica bear | Observable clave |
|---|---|---|---|
| Líderes de HBM | Certificación de clientes, brecha tecnológica, mix alto, escasez de oferta | Concentración de clientes, avance de competidores, normalización de la prima | Rendimiento, precio, cuota y volumen por cliente de HBM4 |
| DRAM y NAND convencionales | Crowding-out de HBM, demanda de servidor y eSSD, oligopolio | Normalización de compras anticipadas, CXMT, expansión de capacidad, elasticidad de precio | Magnitud de la subida del precio de contrato, inventario, bit shipment |
| Fundición de vanguardia | Se benefician ASIC, CPU y GPU de IA por igual, alto coste de cambio | Depreciación de N2 y fábricas en el extranjero, poder de negociación del diseño propio del cliente | Utilización, ASP de oblea, margen por nodo |
| Empaquetado avanzado y OSAT | Escasez del tipo CoWoS, expansión de chiplets y paquetes grandes | Alivio del cuello de botella tras la expansión de capacidad, internalización del cliente | Cartera de pedidos, llegada de equipos, valor por paquete |
| Fabless de IA | Crecimiento del cómputo de IA y del ciclo de producto | ASIC propios, concentración de clientes, fallos de diseño | Design wins, foso de software, conversión de ingresos |
| Óptica y redes | Aumento explosivo del ancho de banda scale-out/across | Cambio de estándares, internalización, competencia, ajuste de inventario | Velocidad de puerto, ASP, producción en volumen por cliente |
| Equipos y test | Beneficiario secundario del CAPEX de memoria y fundición | Pull-in de pedidos, vacío de CAPEX, pico de book-to-bill | Cartera de pedidos, tasa de cancelación, CAPEX del cliente |
| Materiales y sustratos | Alta especificación, alta pureza, período de calificación, expansión del BOM | Multisourcing del cliente, expansión de capacidad, volatilidad de materia prima | Peso de los ingresos ligados a IA, traslado de precio, qualification |
| Neocloud | El cómputo como producto independiente, escasez de energía y de terreno | Apalancamiento, valor residual de las GPU, concentración de clientes | Intereses/EBITDA, utilización, FCF después de CAPEX |
| Hyperscalers | Crecimiento de ingresos de IA, publicidad y nube, acceso a capital | Erosión por CAPEX, depreciación y FCF | Margen bruto de IA, FCF, deuda y leasing |

<strong>Calidad relativa</strong>: el eje de mayor calidad son los líderes verificados en HBM, procesos de vanguardia y empaquetado avanzado, aunque el riesgo de timing es alto porque las expectativas ya son elevadas. El eje de mayor sensibilidad al ciclo es la DRAM y la NAND convencionales, junto con equipos y test. El eje de mayor riesgo financiero es la neocloud apalancada y los centros de datos con clientes concentrados. El eje de mayor opcionalidad es la recuperación de la fundición de Samsung y los nuevos design wins de óptica y materiales, que deben tratarse como una opción gratuita hasta que se confirmen pedidos reales.

---

## 26. Argumentos débiles que hay que descartar

Son afirmaciones que ambos bandos usan con frecuencia, pero que no superan la verificación.

<strong>Bull débil</strong>

| Argumento | Por qué es incorrecto |
|---|---|
| "La IA tiene 4 años, así que la memoria sube sí o sí" | La demanda final a largo plazo y el exceso de beneficio del proveedor actual no son lo mismo |
| "Si el CAPEX sube, suben todos los semiconductores" | El CAPEX incluye terreno, edificios, energía y leasing, y la captura de valor varía por producto y por cliente |
| "Un P/E bajo siempre es barato" | Si el denominador es el EPS pico, un P/E bajo puede ser normal |
| "Como hay LTA, el precio y el volumen están garantizados" | Hay que verificar las condiciones del contrato y el crédito del cliente |
| "CXMT va rezagado en tecnología, se puede ignorar" | La amenaza de corto plazo en HBM es baja, pero importa para el techo de precio de la DRAM convencional |
| "En una buena empresa, el precio y el peso en cartera no importan" | Aunque la calidad sea alta, persisten el riesgo de de-rating y el de concentración |

<strong>Bear débil</strong>

| Argumento | Por qué es incorrecto |
|---|---|
| "La demanda de IA es falsa" | Contradice los pedidos oficiales, el CAPEX y la escasez de oferta |
| "El pico del 4T26 significa una caída de precio inminente" | El nivel de precio y el pico de la tasa de subida del precio son cosas distintas |
| "CXMT sustituirá pronto al HBM" | Ignora el tiempo que exigen el rendimiento, el empaquetado y la certificación de clientes |
| "Los ASIC propios eliminan la demanda de memoria" | Los ASIC también consumen procesos de vanguardia y memoria y redes de alto rendimiento |
| "La cruz de la muerte confirma el fin de la industria" | Los indicadores técnicos son rezagados y hay que mirarlos junto con la tendencia de largo plazo y el EPS |
| "El RPO y el Take-or-Pay son pura ilusión" | La visibilidad contractual real existe, y el problema es la estructura de margen y de financiación |

---

## 27. Escenario integrado

Las siguientes probabilidades no son frecuencias históricas, sino estimaciones de juicio a fecha del 17 de julio de 2026. \[Inferencia: estimación de escenario\]

| Probabilidad | Escenario | Industria | Beneficio | Acción | Condición clave |
|---:|---|---|---|---|---|
| 25% | Reanudación de la fase alcista estructural / bear trap | Continúan la demanda de IA y el cuello de botella | Revisiones al alza del EPS y margen alto sostenido | El SOXX recupera 565-590 y retoma la tendencia | La utilización, los ingresos de IA y el FCF siguen el ritmo del CAPEX |
| <strong>55%</strong> | <strong>Fundamental bull / valuation bear</strong> | La demanda crece | El beneficio es alto pero la magnitud de la revisión al alza se desacelera | Corrección larga y lateralización, rotación de liderazgo | La respuesta de oferta y la depreciación limitan el múltiplo |
| 20% | Hard cycle bear | Retraso de pedidos y desaceleración de la demanda | Rebaja de precio y de EPS | Ruptura del mínimo previo y reducción de riesgo generalizada | Inventario de compras anticipadas + freno al CAPEX + aumento de oferta |

La probabilidad más alta corresponde a <strong>la mezcla de industria bull y acción valuation bear</strong>. En este caso, la pérdida del inversor proviene menos del colapso del beneficio que del <strong>tiempo y el coste de oportunidad</strong>.

---

## 28. Puertas de cambio: qué debe aparecer para cambiar de juicio

Un solo indicador no basta. El juicio solo cambia de dirección cuando se confirman <strong>dos o más ejes distintos</strong>.

<strong>Refuerzo del bull (dos ejes o más)</strong>

1. Revisión al alza del CAPEX de los hyperscalers junto con el aumento del margen bruto de IA y de la nube
2. Mejora de la conexión eléctrica, la utilización de los centros de datos y el uso de GPU
3. Continuidad de las revisiones al alza del precio de HBM/DRAM y del 12MF EPS de Samsung Electronics, SK Hynix y Micron
4. Recuperación del SOXX a 565-590 y reversión de la fortaleza relativa frente al SPY

<strong>Se mantiene el valuation bear</strong>

- Los resultados son buenos pero la magnitud de la revisión al alza del EPS se desacelera
- El nivel de precio de la DRAM es alto pero su tasa de subida se desacelera
- El CAPEX se mantiene pero el FCF y el margen se debilitan
- El SOXX lateraliza en el rango de 470-565 y otros sectores muestran fortaleza relativa

<strong>Escalada a Hard Bear (dos ejes o más)</strong>

1. Recorte del CAPEX de los hyperscalers, retraso de contratos y caída de la utilización
2. Aumento del inventario de cliente/canal y desaceleración de la subida del precio de contrato de DRAM
3. Giro a la baja del 12MF EPS de las tres memoreras
4. Ruptura del nivel 520 del SOXX, fallo en recuperar 565 y contagio amplio al mercado

<strong>Debilitamiento del bear</strong>

- Después de los Rush order, el inventario no se acumula y se consume como uso real
- El precio, el rendimiento y el volumen de HBM4 se mantienen, y la entrada de competidores se absorbe en el crecimiento del mercado
- El aumento de los ingresos y del flujo de caja de IA supera a la depreciación y al gasto por intereses
- El CAPEX se mantiene mientras el diferencial de los bonos corporativos y la calidad crediticia permanecen estables

---

## 29. Registro de evidencia: qué se cree y con qué grado

Se hace pública la fiabilidad de este análisis, fuente por fuente. El principio es no construir una convicción alta sobre una fuente de grado bajo.

| Afirmación | Fuente | Grado | Fiabilidad | Límite |
|---|---|---|---|---|
| Elevación del crecimiento FY26 de TSMC, CAPEX de 60.000-64.000 millones USD | Material de la conferencia del 2T26 y cruce con varios research | B | medium-high | Acceso directo limitado al texto original de RI |
| Restricciones de memoria de Dell/HPE, respuesta de Cisco | Material de quiet-period de JPM | C/B | medium | Broker channel check, no divulgación corporativa |
| Rush order de DRAM de servidor | Material de BofA | C/B | medium | Acceso público limitado al informe original |
| CAPEX, OCF y deuda de Oracle | SEC 10-K (FY2026) | <strong>A</strong> | high | Caso más vulnerable que un hyperscaler rico en caja |
| Compra anticipada y retraso de contratos de clientes de IBM | SEC 8-K (2026-07-14) | <strong>A</strong> | high | No se puede generalizar el caso de una sola empresa, IBM, a toda la TI |
| Ingresos, CAPEX, intereses y concentración de clientes de CoreWeave | SEC filings (1T26) | <strong>A</strong> | high | Caso vulnerable de neocloud, estructura distinta a la de las Big Tech |
| CAPEX combinado de 801.000 millones USD de las 3 compañías para 2027 de Citi | Citi mega-cap preview | C/B | medium | Estimación agresiva, no guía de la empresa |
| Pico de la tasa de subida del precio de memoria en el 4T26 | Gráfico y cita indirecta de Morgan Stanley | C | low-medium | Definición de precio y supuestos originales sin verificar |
| Captación de capital de CXMT y margen para expandir oferta | Cruce de anuncio de emisión y resultado de suscripción | B | medium-high | Desfase hasta la capacidad, el rendimiento y la certificación de clientes reales |
| Exportaciones de semiconductores de Corea y proxy de HBM | Cifra preliminar de aduanas del 1-10 de julio | A/B | Total high, proxy medium | No se puede atribuir por empresa el HBM |
| SOXX cerca de -19% desde el máximo | Cruce de Yahoo/TradingView | B+ | high | No es el valor bruto oficial de la bolsa |

<strong>No verificable (Bloqueado)</strong>: condiciones económicas detalladas del LTA, precio, volumen y rendimiento de HBM4 por cliente, input real de nuevas obleas de CXMT, rentabilidad de las cargas de trabajo de IA por hyperscaler individual.

---

## 30. Qué verificar a continuación

<strong>Resultados y divulgaciones</strong>

1. Alphabet, Meta, Amazon: más que el CAPEX, <strong>el margen bruto de IA, la depreciación, el FCF y la nueva deuda y leasing</strong>
2. SK Hynix, Samsung Electronics, Micron: envíos, rendimiento y precio de HBM4, bit growth de la DRAM convencional, estructura del LTA, revisión del EPS de FY2027
3. TSMC: dilución de margen por N2 y fábricas en el extranjero, capacidad de empaquetado avanzado, verificación de pedidos de clientes y utilización real
4. CXMT: asignación de los fondos de la OPV, pedidos de equipos para la nueva fábrica, rendimiento de DDR5 y certificación de clientes, calendario de HBM

<strong>Datos mensuales y semanales</strong>

1. Magnitud de la subida del precio de contrato de DRAM e inventario de cliente/canal
2. Cifra confirmada de fin de mes de las exportaciones de semiconductores de Corea y del proxy de HBM
3. Delta de revisión del 12MF EPS de las tres memoreras
4. Los niveles 520, 565 y 590 del SOXX y su fortaleza relativa frente al SPY
5. Diferencial de los bonos corporativos de los hyperscalers y coste de financiación de las neocloud

---

## Cierre: del scarcity cycle al capital-intensity cycle

El argumento más sólido del bull de semiconductores es que la demanda de IA es real, que esa demanda se propaga como un cuello de botella físico en memoria, procesos de vanguardia, empaquetado y redes, y que el valor tiempo de la oferta y la certificación de clientes crean barreras de entrada.

El argumento más sólido del bear de semiconductores es que esa demanda real ya elevó con fuerza el precio y el CAPEX, y que, en la siguiente etapa, la normalización de las compras anticipadas, la respuesta de oferta, la depreciación y el coste de capital pueden presionar a la vez el margen y el múltiplo.

Al combinar ambos, la conclusión converge en una sola idea. <strong>La industria de semiconductores de IA todavía no está rota. Pero el scarcity cycle se está desplazando hacia un capital-intensity cycle.</strong> El próximo repunte no comenzará con un anuncio de CAPEX, sino cuando la conexión eléctrica, la utilización y el flujo de caja de IA logren alcanzar la depreciación y el coste de capital.

Por eso, la postura más razonable hoy es no abandonar la tesis de industria a largo plazo, pero <strong>gestionar por separado el timing de la acción y la concentración</strong>. No cambiar de rumbo por una sola señal, sino moverse solo cuando se confirman dos o más ejes distintos. Según las probabilidades actuales, la vía central es <strong>Fundamental Bull / Valuation Bear</strong>, en la que coexisten el crecimiento estructural de la industria y un largo ajuste de valoración en la acción.

---

_Este artículo es un análisis que sintetiza divulgaciones oficiales (SEC, Servicio de Aduanas de Corea), datos de mercado y material de escenarios de brokers, desarrolla la tesis alcista y la tesis bajista de semiconductores en su forma más sólida posible, y las converge hacia variables observables. El grado de fiabilidad de cada fuente se indica en el cuerpo del texto. Las cifras de la conferencia de TSMC son valores de verificación cruzada con acceso directo parcialmente limitado al texto original de relación con inversores, y la estimación de CAPEX de Citi y el momento del pico de Morgan Stanley no son guía de las empresas. Las probabilidades de los escenarios no son frecuencias históricas, sino estimaciones de juicio al momento de la redacción. Los valores mencionados son ejemplos para explicar la estructura de la industria y no constituyen una recomendación de compra o venta de ningún valor en particular. La decisión de inversión y su responsabilidad recaen en el propio inversor._

---

### Publicaciones relacionadas

- [Por qué el fallo de resultados de IBM es evidencia de la fortaleza de la memoria](/es/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/)
- [La brecha de suministro que se extiende más allá del HBM: tres informes de Hana Securities leídos como una sola historia](/es/post/memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14/)
- [Investigación profunda de oferta-demanda de HBM 2030: diseccionando el modelo de demanda de 26,7EB frente al calendario de capacidad](/es/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
- [¿Quién paga el consenso de semiconductores de 2027?](/es/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/)
- [¿Están Samsung Electronics y SK Hynix realmente sobrevendidos frente al consenso de 2027? El peor escenario ya es el precio](/es/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/)
