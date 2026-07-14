---
title: "La brecha de suministro que se extiende más allá del HBM: tres informes de Hana Securities leídos como una sola historia"
slug: "memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14"
date: 2026-07-14T16:00:00+09:00
description: "Tres informes de Hana Securities sintetizados en un solo marco. La brecha de suministro creada por el giro de los tres grandes hacia HBM y DDR5 se extiende a sustratos de encapsulado (Daeduck Electronics, Simmtech, Haesung DS), controladores eSSD (ASICLAND, FADU) y memoria legacy (GigaDevice). Es evidencia de que el auge de la memoria se ha ampliado más allá del HBM. Resumen de informes, no recomendación de inversión."
categories: ["Exclusive Analysis", "Tech-Analysis", "Market-Outlook"]
tags: ["Memory", "Package Substrate", "eSSD", "Legacy Memory", "Daeduck Electronics", "ASICLAND", "FADU", "GigaDevice", "CXMT", "SK Hynix", "Hana Securities"]
valley_cashtags: ["SK하이닉스", "대덕전자"]
draft: false
---

> Contexto
> Este artículo es la continuación del marco de concentración en HBM y riesgo de DRAM legacy que se trató en [SK Hynix recorta beneficios del 2T, ¿por qué se mantuvo el precio objetivo?](/es/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/) y en [La IPO de CXMT y el riesgo de precios de memoria](/es/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/). El eje de eSSD de FADU conviene leerlo junto con [Previsión de resultados de FADU 2T26](/es/post/fadu-2q26-earnings-preview-essd-controller-moderate-beat-2026-07-04/), y el eje de sustratos junto con [La tesis del cuello de botella de sistema en PCB de IA](/es/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/). Los hubs relacionados son el [Hub de IA y HBM](/es/page/korea-semiconductor-hbm-kospi-hub/) y el [Hub de Exclusive Analysis](/es/page/exclusive-analysis-hub/).

## TL;DR

* Si se agrupan en un solo marco los tres informes que Hana Securities publicó en las últimas dos semanas, son <strong>tres escenas de la misma historia</strong>. La brecha de suministro que crean los tres grandes al desplazarse hacia HBM y DDR5 se está extendiendo a la cadena de valor adyacente.
* <strong>Escena 1, sustratos de encapsulado</strong>: el mayor tamaño y número de capas de DDR5/LPDDR5 erosiona la capacidad real de producción de sustratos. La señal de escasez es la firma de contratos LTA (Daeduck Electronics, Simmtech, Haesung DS).
* <strong>Escena 2, controladores eSSD</strong>: la demanda de los centros de datos de IA dispara el SSD empresarial, y SK Hynix eligió a la casa de diseño local ASICLAND como socio para el controlador Gen6. Se espera que el Gen6 destinado a FADU entre en producción en masa en el segundo semestre de 2027.
* <strong>Escena 3, memoria legacy</strong>: el vacío de DDR4 y SLC NAND que dejan los líderes lo llena la china GigaDevice. En el último año, el ASP de SLC NAND subió cerca de 5 veces y el de DRAM legacy, cerca de 10 veces.
* <strong>El alcance del auge de la memoria se ha ampliado más allá del HBM.</strong> Pero en los tres ejes hay un punto de verificación pendiente: en sustratos, la divulgación de LTA, el precio y la tasa de utilización; en eSSD, los pedidos oficiales y el reconocimiento de ingresos de FADU; en legacy, la velocidad con la que China llena el vacío. \[Alcance: resumen de informes\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Marco clave</div>
  <div class="thesis-callout__body">
    Los tres informes tratan valores distintos, pero convergen en una sola frase. La brecha de suministro que genera la concentración de los tres grandes en HBM y DDR5 se extiende a los sustratos de encapsulado, los controladores eSSD y la memoria legacy, ampliando el alcance del auge de la memoria más allá del HBM.
  </div>
</div>

---

## Marco transversal: un solo vacío, tres ramas de expansión

Leídos por separado, los tres informes parecen historias de valores sin relación entre sí. Pero superpuestos, son tres resultados que se ramifican desde una misma causa.

<strong>Causa</strong>: los tres grandes (Samsung Electronics, SK Hynix, Micron) concentran sus recursos limitados de oblea y de back-end en HBM y DDR5. Como resultado, se genera una brecha de suministro en los componentes adyacentes y en los productos legacy.

<strong>Expansión</strong>: ese vacío se propaga en tres direcciones.

| Escena | Ubicación de la brecha de suministro | Eje beneficiado | Señal de escasez/crecimiento |
|---|---|---|---|
| 1 | Sustratos de encapsulado de memoria | Daeduck Electronics, Simmtech, Haesung DS | Firma de LTA, subida de precios |
| 2 | Controladores eSSD | ASICLAND, FADU | Adopción del Gen6 por SK Hynix, contrato de producción en masa |
| 3 | DRAM legacy, SLC NAND | GigaDevice (China) | ASP se dispara, sorpresa de resultados |

A continuación se detalla cada escena con las cifras originales de los informes.

---

## Escena 1: sustratos de encapsulado, la capacidad se erosiona en silencio

El primer informe es `Recomendación de compra para el sector de sustratos de encapsulado de memoria`, de la analista Kim Min-kyung de Hana Securities (3 de julio de 2026). \[Hecho: informe de Hana Securities\]

### La tesis: el temor a una baja de precios es infundado, el problema real es la escasez de oferta

Daeduck Electronics, Simmtech y Haesung DS sufrieron una fuerte corrección bursátil por el temor a una burbuja de IA tras la noticia de que Meta arrendaría externamente parte de su capacidad de cómputo, sumado a informes de prensa sobre una posible baja de precios de sustratos en el segundo semestre. El informe considera que <strong>esta corrección es, en realidad, una oportunidad de compra</strong>, porque los IDM de memoria, que registran márgenes operativos altos, tienen pocos incentivos para bajar precios.

La lógica central es <strong>la erosión de la capacidad de producción real</strong>.

- La capacidad de los sustratos de encapsulado de memoria está estancada desde la gran expansión de 2020-2022.
- En aquel momento, los productos principales eran DDR4 y LPDDR4; hoy son DDR5 y LPDDR5/5X.
- La mayor prestación de la memoria y el aumento del tamaño del die obligan a <strong>sustratos más grandes y con más capas</strong>, lo que reduce la cantidad de sustratos que se puede fabricar con la misma capacidad.
- Los fabricantes de sustratos de primer nivel, como Unimicron y Samsung Electro-Mechanics, concentran su expansión de capacidad en el FCBGA, un producto de alto margen, lo que agrava la preocupación por el suministro global de sustratos BT.

Ya hubo una subida de precios de sustratos en abril de 2026. Refleja el alza del costo de materias primas como el oro y el cobre, pero el informe estima que también incorpora, en parte, la preocupación por el suministro del segundo semestre. En ese período está previsto el suministro de memoria genérica para el Rubin de NVIDIA y la expansión de los envíos de DDR5 de los fabricantes chinos de memoria, lo que aumentará aún más la demanda de sustratos. \[Inferencia: estimación del informe\]

### Punto de verificación: la señal de escasez es la LTA

La herramienta de observación más útil que ofrece el informe es <strong>la firma de un LTA (contrato de suministro a largo plazo)</strong>. En marzo de 2020, Simmtech firmó un contrato de venta única y suministro con Micron; en un sector de sustratos con plazos de entrega cortos, un contrato de gran tamaño de KRW 100.000 millones o más resultaba inusual. A partir de esa divulgación, la escasez de oferta real se profundizó y el mercado entró en un ciclo de subidas de precio en toda regla. \[Hecho: precedente histórico\]

Por eso, la implicación práctica de este eje es clara: antes que comprar de entrada las acciones beneficiadas, conviene verificar primero <strong>la divulgación de contratos de suministro, el precio y la tasa de utilización</strong>. Si aparece una divulgación de LTA, puede leerse como una señal de entrada de ciclo similar a la de 2020.

---

## Escena 2: controladores eSSD, SK Hynix ya eligió socio

El segundo informe es `ASICLAND: el socio de eSSD que eligió Hynix`, del analista Kwon Tae-woo de Hana Securities (8 de julio de 2026). \[Hecho: informe de Hana Securities\]

### La empresa y el contrato

ASICLAND (445090) es una casa de diseño (design house) fundada en 2016, la única en Corea del Sur que posee de forma simultánea la condición de miembro de TSMC VCA (Value Chain Alliance) y de Total Design Partner de Arm. El negocio se divide entre ASIC no relacionados con memoria (IA, HPC) y memoria (eSSD, eMMC), y más del 80% de la plantilla son ingenieros.

El evento clave es el contrato con SK Hynix.

- El 29 de junio, ASICLAND divulgó un contrato con SK Hynix para el diseño y soporte de tape-out del controlador eSSD de próxima generación.
- El monto es de KRW 31.900 millones (43,7% de los ingresos de 2025), y el período va del 27 de mayo de 2025 al 31 de diciembre de 2027.
- El tape-out, bajo la especificación PCIe Gen6 y el proceso de 5nm, se completó el 1 de julio.
- El escenario base es el inicio de la producción en masa en 2028, aunque el calendario de validación es conservador y existe margen para que se adelante.
- Lo esencial es que <strong>la estructura del contrato no se limita al desarrollo, sino que conecta directamente con la producción en masa</strong>.

La elección de casa de diseño de controladores eSSD de SK Hynix pasó de la Empresa A nacional en el Gen4, a GUC de Taiwán en el Gen5, hasta llegar a <strong>ASICLAND en el Gen6</strong>. \[Hecho: informe\]

### Demanda y resultados

La demanda de eSSD proveniente de los centros de datos de IA es un eje de crecimiento confirmado. Las ventas combinadas del 1T26 de las cinco mayores empresas globales de SSD empresarial alcanzaron US$18.460 millones, +86,1% intertrimestral, un máximo histórico (TrendForce). Se espera que 2026 sea el año en que el SSD empresarial se convierta en la mayor aplicación de NAND. \[Hecho: TrendForce\]

El track de producción en masa de ASICLAND también se activa de forma secuencial.

- El controlador de tarjetas eMMC ya genera ingresos de producción en masa, con una expansión prevista a una escala anual de KRW 40.000-50.000 millones o más.
- <strong>Se espera que el controlador Gen6 destinado a FADU, en proceso de 6nm, entre en producción en masa en el segundo semestre de 2027</strong>.
- Es posible que el desarrollo del próximo Gen7 se contrate dentro del año.

Las ventas del 1T26 fueron de KRW 54.000 millones (+242,4% interanual), y la pérdida operativa se redujo a KRW 3.000 millones. Con este contrato incorporado, la guía de ventas de 2026 se elevó de KRW 160.000 millones a KRW 180.000 millones, y se espera un giro a beneficio operativo anual. \[Hecho: informe\]

### Punto de verificación: el contrato de ASICLAND todavía no es ingresos de FADU

Aquí hay un punto que conviene separar. El informe menciona <strong>la producción en masa en el segundo semestre de 2027 del controlador Gen6 destinado a FADU</strong>, algo que se conecta directamente con la posición actual de FADU. Sin embargo, no hay garantía de que el contrato de ASICLAND se traduzca en demanda de clientes e ingresos para FADU. ASICLAND es la casa de diseño que diseña el controlador, y FADU es la empresa que vende el SSD que lo incorpora. Ambas empresas ocupan posiciones distintas en la cadena de valor. \[Inferencia: distinción de cadena de valor\]

Por eso, al analizar a FADU no basta con la divulgación del contrato de ASICLAND; hay que verificar por separado <strong>los pedidos oficiales de FADU y el calendario de reconocimiento de ingresos</strong>. La dirección ya está definida, pero los ingresos son un evento aparte.

---

## Escena 3: memoria legacy, China llena el vacío que dejan los líderes

El tercer informe es `GigaDevice: la empresa de memoria legacy que crece gracias a la brecha de suministro global`, de la analista Baek Seung-hye de Hana Securities (14 de julio de 2026). \[Hecho: informe de Hana Securities\]

### La empresa: la misma raíz que CXMT

GigaDevice (603986) es la empresa líder en cuota de mercado de China en DRAM legacy, SLC NAND Flash, NOR Flash y MCU. Es otra compañía de memoria fundada en 2005 por Zhu Yiming, el mismo presidente fundador de CXMT (ChangXin Memory), quien hoy también preside su directorio. GigaDevice invirtió una participación minoritaria del 1,8% en CXMT, y la relación de colaboración consiste en que CXMT fabrica por encargo el DRAM de GigaDevice. \[Hecho: informe\]

La división de roles es clara. <strong>CXMT se concentra en DRAM genérica de gama DDR5/LPDDR5 o superior y en HBM, mientras que GigaDevice se encarga de memoria especializada como NOR Flash y SLC NAND, de DRAM legacy de gama DDR4/LPDDR4 o inferior, y de MCU</strong>. Es decir, mientras CXMT persigue a los líderes hacia arriba, GigaDevice absorbe el vacío legacy que queda por debajo.

### Resultados: la sorpresa que creó el vacío

Los resultados preliminares del 2T26 muestran esta estructura en números.

- Ingresos preliminares de RMB 7.300 millones, +226% interanual, un 46% por encima del consenso
- Beneficio neto atribuible a la controladora de RMB 5.400 millones, +1.496% interanual, un 77% por encima del consenso

El buen desempeño se explica por la subida del ASP de los productos principales y la expansión de la cuota de mercado. A medida que los principales fabricantes globales de memoria aumentan su producción centrada en HBM, DDR5 y 3D NAND, la oferta y demanda de DRAM y NAND legacy se ajustó, y <strong>en el último año el ASP de SLC NAND de GigaDevice subió cerca de 5 veces, y el de DRAM legacy, cerca de 10 veces</strong>. \[Hecho: informe\]

### Catalizadores del segundo semestre y punto de verificación

Hay dos motores de subida para el segundo semestre. Primero, la reducción de la producción en masa de NAND legacy por parte de Kioxia y Micron mantiene la tendencia alcista del precio de SLC NAND. Gracias a su colaboración con CXMT, GigaDevice es una de las pocas empresas capaces de ampliar su capacidad de DDR4 en los próximos 2-3 años. El objetivo es elevar la cuota global de NOR Flash del 20% actual al 25% en 3-5 años. Segundo, los envíos masivos de DRAM 3D a medida. Se espera que la DRAM a medida relacionada con IA, para cabinas inteligentes de automóviles, PC con IA y robots, comience a contribuir a los ingresos a partir del segundo semestre de 2026. \[Inferencia: previsión del informe\]

El doble significado de este informe es el punto de verificación. El rápido crecimiento de GigaDevice es <strong>tanto evidencia de que el alcance del auge de la memoria se amplió, como un material para verificar la velocidad con la que las empresas chinas llenan el vacío</strong>. La rapidez con la que China ocupa el lugar que dejan los líderes también incide en el techo de precios de la memoria legacy de los fabricantes coreanos. Esto está en la misma línea que la lógica del techo de precio de la DRAM cliente tratada en [La IPO de CXMT y el riesgo de precios de memoria](/es/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/).

---

## Síntesis: un auge que amplía su alcance, y tres botones de verificación

Al superponer los tres informes, la conclusión es una sola. <strong>El auge de la memoria ya no es solo una historia de HBM.</strong> Cuanto más concentran los tres grandes sus recursos en HBM y DDR5, más se genera una brecha de suministro a los lados y por debajo, y esa brecha crea beneficios independientes. Los sustratos de encapsulado, los controladores eSSD y la memoria legacy montan, cada uno, su propio ciclo.

Sin embargo, en los tres ejes existe <strong>un botón de verificación entre la narrativa y los ingresos</strong>.

| Eje | Narrativa | Botón de verificación a pulsar |
|---|---|---|
| Sustratos de encapsulado | Mayor área y más capas erosionan la capacidad real | Divulgación de LTA, precio, tasa de utilización |
| Controladores eSSD | Adopción del Gen6 por SK Hynix, transición a producción en masa | Pedidos oficiales y calendario de reconocimiento de ingresos de FADU |
| Memoria legacy | China absorbe el vacío de los líderes, el ASP se dispara | Velocidad con la que China llena el vacío |

Es decir, estos tres informes no son <strong>una señal para comprar primero las acciones beneficiadas, sino un mapa que indica qué hay que verificar para determinar si se entró en el ciclo</strong>. ¿Aparece la divulgación de LTA? ¿Se reconocen efectivamente los ingresos de FADU? ¿La ampliación de capacidad legacy de China vuelve a presionar los precios a la baja? Estos tres botones señalan el punto en el que la narrativa se convierte en hecho.

---

_Esta publicación es un material que sintetiza en un solo marco el contenido detallado de tres informes públicos de Hana Securities (sustratos de encapsulado de memoria del 3 de julio de 2026, ASICLAND del 8 de julio, GigaDevice del 14 de julio). Los objetivos y previsiones citados son opiniones de esa casa de bolsa, y los valores mencionados son ejemplos para explicar la estructura de la industria, no una recomendación de compra o venta de ningún valor en particular. Las cifras y previsiones de los informes corresponden al momento de su publicación y pueden cambiar después. La decisión de inversión y su responsabilidad corresponden al propio inversor._

---

### Publicaciones relacionadas

- [SK Hynix recorta beneficios del 2T, ¿por qué se mantuvo el precio objetivo?](/es/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/)
- [La IPO de CXMT y el riesgo de precios de memoria: hay que separar el riesgo de HBM del riesgo de DRAM cliente](/es/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)
- [Previsión de resultados de FADU 2T26: el controlador eSSD](/es/post/fadu-2q26-earnings-preview-essd-controller-moderate-beat-2026-07-04/)
- [PCB y sustratos de IA: el cuello de botella común de la lista de materiales del sistema](/es/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/)
- [Investigación profunda de oferta-demanda de HBM 2030: diseccionando el modelo de demanda de 26,7EB y cruzándolo con el calendario de ampliación](/es/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
