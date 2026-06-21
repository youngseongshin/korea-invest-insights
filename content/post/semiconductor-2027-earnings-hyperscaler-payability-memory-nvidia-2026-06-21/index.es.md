---
title: "¿Quién paga el consenso de semiconductores de 2027? Samsung, Hynix, Micron y Nvidia vistos desde la capacidad de pago de los hyperscalers"
slug: "semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21"
date: 2026-06-21T20:00:00+09:00
description: "Verificamos, bajo un mismo marco, si el consenso de resultados de Samsung Electronics, SK hynix, Micron y Nvidia para 2027 es mero optimismo del sell-side o un nivel que la demanda puede pagar realmente. La conclusión se bifurca. Los hyperscalers pueden pagar de forma condicional, el gobierno y la IA soberana son demanda complementaria, y los OEM de PC y smartphones ya están en zona de impago. La clave no es 'si hay demanda de IA', sino 'si los ingresos de IA y la utilización de las GPU suben lo suficiente para justificar el CAPEX también después de 2027'."
categories: ["Exclusive Analysis", "Korean-Equities", "Market-Outlook"]
tags:
  - "Samsung Electronics"
  - "SK hynix"
  - "Micron"
  - "Nvidia"
  - "HBM"
  - "Hyperscalers"
  - "AI CAPEX"
  - "Memoria"
  - "Resultados 2027"
  - "IA soberana"
  - "Research OS"
series: ["Korea Market Regime"]
draft: false
---

> Contexto de conexión
> Este artículo es la síntesis de [Por qué el superciclo de la IA se alarga aún más: financiación vía IPO y memoria/almacenamiento](/es/post/ai-supercycle-extension-agent-demand-ipo-funding-memory-storage-2026-06-12/), [La era del CapEx de 5,3 billones de dólares en centros de datos de IA](/es/post/ai-datacenter-capex-5p3t-korea-power-substrate-storage-bottleneck-2026-06-05/), [Demanda de tokens de Goldman vs. ASP de memoria de JP Morgan](/es/post/goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31/) y [Paridad Sam-Hy-Mi: el tramo en que la memoria coreana vuelve a estar barata](/es/post/samsung-hynix-micron-forward-per-parity-memory-catch-up-2026-06-03/). Si los artículos anteriores miraban la demanda, el precio y la valoración por separado, este los une bajo una sola pregunta: <strong>"¿puede la demanda pagar realmente el consenso de resultados de 2027?"</strong>.

## TL;DR

* El consenso de 2027 no depende de la <strong>demanda de productos electrónicos</strong>, sino de <strong>si los hyperscalers, la nube de IA y la IA soberana siguen absorbiendo los precios de HBM, GPU y DRAM de servidor</strong>.
* La conclusión se bifurca. <strong>Los hyperscalers pueden pagar de forma condicional</strong>, <strong>el gobierno y la IA soberana tienen voluntad política de pago pero un ROI opaco</strong>, y <strong>los OEM de PC y smartphones ya están en zona de impago</strong>.
* En cifras, solo la suma del CAPEX 2027E de las cuatro grandes (Microsoft, Google, Meta, Amazon) ronda los <strong>782.200 millones de dólares</strong>, y la suma de FCF ronda los <strong>119.900 millones de dólares</strong>. Contablemente pueden pagar, pero el colchón de caja remanente es delgado.
* El consenso de ingresos FY2028 de Nvidia, de unos 551.700 millones de dólares, equivale a cerca del <strong>70,5%</strong> del CAPEX de las cuatro grandes. Para que esa cifra cuadre se necesita no solo a las cuatro, sino un <strong>pool global de CAPEX de IA</strong> que incluya a Oracle, OpenAI, la IA soberana, China y las empresas.
* El beneficio 2027E de las tres compañías de memoria es aún más sensible al <strong>mantenimiento del ASP de memoria y a la persistencia de la escasez de HBM</strong> que al CAPEX de los hyperscalers. Por eso la asimetría más interesante es <strong>Samsung Electronics (candidata condicional cuyo descuento por pico podría ser excesivo)</strong>.

---

## 1. La pregunta central y el ajuste por año fiscal

El objetivo de este análisis es uno: juzgar si las previsiones de resultados de 2027 de Samsung Electronics, SK hynix, Micron y Nvidia son mero optimismo del sell-side o un nivel verificable mediante la capacidad de pago del comprador final.

Cinco preguntas centrales:

1. ¿Cuánto suman las previsiones de ingresos y beneficio 2027E y qué imagen queda al ajustar las diferencias de año fiscal?
2. ¿Se pueden sumar sin más las previsiones de las tres compañías de memoria y de Nvidia, o se genera doble contabilización?
3. ¿Pueden el CAPEX, el FCF y la capacidad de financiación externa 2027E de los hyperscalers soportar esos ingresos?
4. ¿Son el gobierno y la IA soberana lo bastante grandes para sostener los resultados de 2027 por sí solos?
5. ¿Pueden los OEM de PC y smartphones trasladar la subida del precio de la memoria al consumidor final?

<strong>Aviso sobre el año fiscal:</strong> Samsung Electronics y SK hynix cierran en diciembre, por lo que coinciden con CY2027. El FY2027 de Micron termina en agosto de 2027. El FY2027 de Nvidia termina en enero de 2027, por lo que recoge principalmente resultados de 2026; para ver "2027" hay que mirar también el <strong>FY2028 (cierre en enero de 2028)</strong>.

---

## 2. Instantánea del consenso de resultados 2027E

Lo siguiente no es la guía de las compañías, sino <strong>consenso externo y datos de mercado</strong> (según MarketScreener, cierre del 19 de junio de 2026). El KRW se anota de forma aproximada a 1 dólar = 1.454 wones para facilitar la comparación.

| Empresa | Periodo comparado | Ingresos 2027E | EBIT/Beneficio operativo 2027E | Beneficio neto 2027E | Valoración | Veredicto preliminar |
|---|---|---|---|---|---|---|
| <strong>Samsung Electronics</strong> | CY2027 | 856,8 bill. KRW (unos 589.000 mill. USD) | 460,1 bill. KRW | 373,4 bill. KRW | 354.000 KRW, P/E 2027E 6,12x | El consenso es agresivo; la acción descuenta un "pico transitorio" |
| <strong>SK hynix</strong> | CY2027 | 483,8 bill. KRW (unos 333.000 mill. USD) | 377,1 bill. KRW | 297,1 bill. KRW | 2.764.000 KRW, P/E 2027E 6,71x | El liderazgo en HBM ya está bastante reflejado. Un P/E de pico de 6-7x es señal de desconfianza en la persistencia |
| <strong>Micron</strong> | FY2027 | 190.980 mill. USD | 157.200 mill. USD | 122.920 mill. USD (BPA unos 111 USD) | 1.133,99 USD, P/E FY2027E unos 10,2x | Máxima beta de memoria; con la desaceleración de 2028 ya visible, el margen de seguridad para una compra nueva es el más bajo |
| <strong>Nvidia</strong> | FY2028 | 551.690 mill. USD | 362.000 mill. USD | 304.840 mill. USD (BPA unos 12,85 USD) | 210,69 USD, P/E FY2028E unos 16,4x | Si las cifras cuadran, no está cara. El problema es el tamaño de CAPEX de cliente necesario para esas cifras |

<strong>La dispersión de previsiones es grande.</strong> En particular, el beneficio operativo 2027E estimado por KB para SK hynix era cerca de un <strong>71% superior</strong> al consenso de FnGuide de entonces (209,3 bill. KRW). Que la imagen de 2027 del mercado difiera tanto para una misma compañía significa que el consenso no es "un futuro fijado", sino "una hipótesis de alta intensidad sobre la persistencia de los precios".

Y los márgenes operativos 2027E de las tres compañías de memoria incluyen niveles del 70%. Eso no es un ciclo de memoria normal, sino una cifra <strong>solo posible cuando se mantienen una escasez estructural de oferta y los contratos a largo plazo</strong>.

---

## 3. "No se debe sumar": la trampa de la doble contabilización

Empecemos por la interpretación más importante. Los ingresos de HBM, DRAM y NAND de las tres compañías de memoria y los ingresos de GPU de Nvidia <strong>se solapan en parte desde la óptica del gasto del comprador final</strong>.

Los ingresos de Nvidia incluyen el coste del sistema, la placa y el networking, HBM incluido. Los ingresos de HBM de las fabricantes de memoria entran como upstream de ese coste de sistema y luego se reflejan en el precio del servidor de IA que compra el hyperscaler. Por tanto, <strong>sumar sin más "ingresos de Nvidia + ingresos de las tres compañías de memoria" como gasto final cuenta el mismo dinero dos veces</strong>.

Desde la óptica de inversión, los ingresos de cada nodo pueden ser todos reales. Sin embargo, el comprador final debe pagar <strong>todo</strong> —GPU, HBM, DRAM general, SSD, networking, servidor, electricidad, refrigeración y coste de construcción— dentro del mismo presupuesto de centro de datos de IA. Por eso es más riguroso <strong>comparar con el "pool total de CAPEX de centros de datos de IA"</strong> que sumar ingresos.

---

## 4. Verificación de la capacidad de pago por tipo de comprador

### 4.1 Hyperscalers: pueden pagar de forma condicional

Al sumar el CAPEX y el FCF 2027E de las cuatro grandes resulta lo siguiente (según consenso).

| Comprador | CAPEX 2027E | FCF 2027E | Interpretación |
|---|---:|---:|---|
| Microsoft | 170.400 mill. USD | 59.300 mill. USD | Gran capacidad de inversión, pero dilución del FCF |
| Alphabet | 231.100 mill. USD | 25.200 mill. USD | El CAPEX absorbe la mayor parte del FCF |
| Meta | 159.500 mill. USD | 11.400 mill. USD | Estructura en la que el FCF remanente se vuelve muy delgado |
| Amazon | 221.200 mill. USD | 24.000 mill. USD | Inversión simultánea en AWS, logística e IA |
| <strong>Total</strong> | <strong>782.200 mill. USD</strong> | <strong>119.900 mill. USD</strong> | Contablemente pueden pagar, pero el colchón es limitado |

La fórmula es sencilla. <strong>Proxy de CFO = CAPEX + FCF = 782.200 mill. + 119.900 mill. = unos 902.100 millones de dólares.</strong> Es decir, la afirmación de que "los hyperscalers no tienen flujo de caja alguno para pagar el coste de IA en 2027" es falsa. El problema es el contrario: <strong>se está reasignando demasiado flujo de caja al CAPEX de IA</strong>. En esta estructura, la recompra de acciones, los dividendos, las fusiones y adquisiciones, la sustitución de la infraestructura existente, los contratos de electricidad y el alquiler de centros de datos compiten todos por el mismo efectivo.

Y con las cuatro grandes no basta. <strong>Los ingresos FY2028 de Nvidia, de 551.690 millones de dólares, equivalen a cerca del 70,5% del CAPEX de las cuatro grandes, de 782.200 millones</strong> (551.690 / 782.200 = 70,5%). Para que los ingresos de Nvidia se materialicen según el consenso, las cuatro grandes no solo deben gastar en GPU, sino pagar a la vez la infraestructura no-GPU (electricidad, refrigeración, servidor, red, construcción), por lo que se necesita un <strong>pool global de CAPEX de IA que incluya a Oracle, CoreWeave, OpenAI/Stargate, xAI, la nube china, la IA soberana de Oriente Medio y las empresas</strong>.

Goldman Sachs estima el CAPEX de IA de 2026-2031 en unos 7,6 billones de dólares, y Morgan Stanley estima el gasto global en centros de datos para 2027E en unos 812.700 millones de dólares. El tamaño está dentro del rango que puede explicar el consenso, pero ambos presentan a la vez un financing gap: <strong>el flujo de caja de los hyperscalers no basta por sí solo y se necesita financiación externa</strong> como bonos corporativos, ABS y private credit.

### 4.2 Capacidad de pago económica: distinta de la de caja

Una cosa es poder pagar en efectivo y otra es poder asumirlo económicamente. Goldman Sachs sitúa la vida útil efectiva de un chip de IA habitualmente en <strong>4-6 años</strong>. Si el CAPEX de IA de 2027 es de 900.000 millones a 1,1 billones de dólares, solo la amortización supone un coste económico anual de <strong>unos 150.000 a 275.000 millones de dólares al año</strong> (900.000 mill. ÷ 6 años = 150.000 mill. / 1,1 bill. ÷ 4 años = 275.000 mill.). A esto se suman electricidad, refrigeración, alquiler, networking, operación, coste de entrenamiento de modelos y coste financiero.

Por tanto, la capacidad de pago de los hyperscalers depende, en última instancia, de cuán rápido absorban esa amortización <strong>los ingresos por inferencia de IA, la expansión de asientos de IA empresarial, la mejora en publicidad/búsqueda/comercio y los ingresos por alquiler de GPU en la nube</strong>. Hasta 2027 pueden aguantar con flujo de caja y mercados financieros. Pero para invertir al mismo ritmo en 2028-2029, la monetización de la IA debe ser más clara.

<strong>Veredicto: la capacidad de pago en efectivo es VERDADERA de forma condicional; la capacidad de pago según el ROIC económico es MIXTA.</strong>

### 4.3 Gobierno e IA soberana: demanda complementaria, no pagador único

La demanda es real. La UE anunció con InvestAI una movilización total de inversión en IA del orden de 200.000 millones de euros, y la saudí HUMAIN proyecta con Nvidia una AI factory de hasta 500 MW y cientos de miles de GPU (se menciona una primera fase con 18.000 GB300). El Stargate de OpenAI también es de 500.000 millones de dólares y 10 GW en 4 años (liderazgo privado, no presupuesto puramente gubernamental).

[Inferencia] El gobierno y la IA soberana tienen menor elasticidad-precio que la nube privada (con fines de defensa, soberanía de datos y política industrial). Por ello actúan como <strong>amortiguador de demanda</strong> para Nvidia, HBM y la infraestructura eléctrica. Sin embargo, por tamaño y velocidad de ejecución, están más cerca de <strong>subsidios, contratos eléctricos a largo plazo, mejora crediticia y cliente ancla</strong> que de un sustituto del CAPEX de los hyperscalers. No se deben tomar los importes anunciados directamente como ingresos. En particular, en China los controles de exportación y la localización limitan el beneficio directo de Nvidia y Micron.

<strong>Veredicto: la afirmación de que solo la demanda gubernamental sostiene el superciclo de 2027 es FALSA. Es importante como downside protection cuando se combina con los hyperscalers.</strong>

### 4.4 OEM de productos electrónicos: cerca del impago

[Hecho] Gartner previó para 2026 unos envíos de PC del <strong>-10,4%</strong>, de smartphones del <strong>-8,4%</strong> y un precio de DRAM+SSD del <strong>+130%</strong>, lo que llevaría a subidas de precio del PC del +17% y del smartphone del +13%, y a que el peso de la memoria en el BOM del PC suba del 16% en 2025 al 23% en 2026. IDC también previó que, a medida que los centros de datos de IA absorben obleas, los smartphones y PC responderán con subidas de precio, recortes de especificaciones y retrasos de lanzamiento.

[Inferencia] Los OEM de productos electrónicos no "pagan" el precio de la memoria, sino que reaccionan con <strong>caída de envíos, reducción de capacidad instalada, subida de precio de venta y degradación del mix de modelos</strong>. Los dispositivos premium absorben la subida del ASP, pero el segmento de gama media-baja tiene alta elasticidad-precio y aparece destrucción de demanda. Es decir, quien justifica el consenso de memoria de 2027 no son los PC ni los smartphones. Ese consenso depende en realidad de la demanda de <strong>servidores de IA, HBM, SSD empresarial y DDR5 RDIMM</strong>.

<strong>Veredicto: no es el pagador clave, sino la víctima de la subida de precios. FALSO.</strong>

---

## 5. Cuello de botella de oferta: 2027 es un problema de P más que de Q

[Hecho] Gartner prevé unos ingresos de semiconductores de 1,320 billones de dólares en 2026 y de 1,555 billones en 2027, y unos ingresos de memoria de 633.300 millones en 2026 y de 748.100 millones en 2027. Considera un precio de DRAM del +125% y de NAND del +234% en 2026, y que una relajación significativa de precios podría ser limitada hasta finales de 2027.

[Hecho] TrendForce considera que el peso de las obleas destinadas a HBM puede subir del 18% a finales de 2025 al 22% a finales de 2026 y hasta el 30% a finales de 2027, pero que el peso del HBM en el bit supply podría quedarse en torno al 13% incluso en 2027. Significa que <strong>el HBM consume muchas obleas de DRAM, pero la oferta total de bits crece de forma limitada</strong>.

Por eso los resultados de 2027 son menos una cuestión de "cantidad demandada Q" y más de <strong>precio P y mix de producto</strong>, y de a quién se atribuye el incremental margin que surge de una oferta limitada. Por ello, aunque la demanda genérica de PC y smartphones se desacelere, la escasez de HBM y DDR5 de servidor —cuya wafer allocation ya se ha desplazado hacia los servidores de IA— no se resuelve de inmediato.

---

## 6. Read-through coreano y veredicto por valor (ejemplos y puntos de observación)

Los nombres de valores que siguen son <strong>ejemplos de cesta y puntos de observación</strong>. No son recomendación de compra, sino ordenación de hipótesis de inversión.

| Valor | Juicio | Tesis en una línea | Riesgo clave |
|---|---|---|---|
| <strong>Samsung Electronics</strong> | Watchlist → Buy condicional | Si se confirman el catch-up de HBM4/HBM4E y el apalancamiento operativo de DS, un P/E 2027E en la franja baja de 6x podría suponer un "descuento por pico" excesivo | Retraso en la oferta de HBM4, falta de allocation de clientes clave, desplome del margen operativo de DS |
| <strong>SK hynix</strong> | Wait | El liderazgo en HBM es el más seguro, pero la acción ya lo refleja bastante. La persistencia del beneficio es atractiva, pero el margen de seguridad para una entrada nueva es bajo | Caída de cuota y margen por la mejora de rendimiento de HBM4 de la competencia, ajuste de pedidos |
| <strong>Nvidia</strong> | Watchlist | Un P/E FY2028E en la franja de 16x es bajo si las cifras cuadran, pero ha crecido la carga de verificar el CAPEX de cliente y el ROI de la IA | Penetración de ASIC propios, regulación china, caída de ingresos por alquiler de GPU, cuello de botella eléctrico |
| <strong>Micron</strong> | Evitar compra nueva | La beta de memoria es grande, pero con un P/E FY2027E en la franja de 10x más el riesgo de desaceleración de 2028, la asimetría frente a la memoria coreana es baja | Pico anticipado de DRAM/NAND, inferioridad en cuota de HBM, revisión a la baja del BPA FY2028E |

La mejor estructura es <strong>"un nodo cuello de botella con poder de fijación de precios y que aún cotiza con descuento por pico"</strong>. Bajo este criterio, lo más interesante ahora es Samsung Electronics. Como el mercado todavía descuenta la persistencia de los precios de HBM4, packaging y memoria como un "ciclo de pico", existe la asimetría de que un P/E en la franja baja de 6x se revalúe si se confirma el catch-up de HBM4. SK hynix es de calidad, pero el precio de entrada es el problema; Nvidia es un activo de calidad, pero requiere primero la verificación del ROI de cliente; y Micron es donde la asimetría para una compra nueva es la más débil.

---

## 7. Red Team: en qué casos esta conclusión se equivoca

* <strong>Riesgo de tipos y crédito</strong>: si suben los tipos o se amplía el credit spread, el CAPEX de los hyperscalers es lo primero que se tambalea, justamente por su gran dependencia de la financiación externa.
* <strong>Internalización de ASIC</strong>: el TPU de Google, el Trainium de Amazon y los chips propios de Meta cambian, después de 2027, el ASP ceiling de Nvidia y la estructura de demanda de HBM.
* <strong>Ampliación de capacidad de memoria</strong>: si Samsung y Micron aumentan agresivamente la capacidad de HBM y el spread de SK hynix se estrecha, el margen 2027E se desploma.
* <strong>"Ingresos sostenidos, FCF/monetización flojos"</strong>: la señal más peligrosa no es el recorte de CAPEX, sino mantener el CAPEX con una conversión débil en ingresos de IA. Los ingresos de 2027 pueden aguantar, pero la intensidad de pedidos de 2028 puede caer bruscamente.

---

## 8. Checklist de monitorización

| Indicador | Por qué importa |
|---|---|
| Revisión del CAPEX de las cuatro grandes | Proxy de demanda de mayor nivel para los resultados de Samsung, Hynix, Micron y Nvidia |
| FCF tras restar el CAPEX | La clave que separa "puede pagar" de "gasto excesivo" |
| Backlog y lead time del segmento de centros de datos de Nvidia | Visibilidad de ingresos FY2028 de más de 550.000 mill. USD |
| LTA, prepago y capacity reservation de HBM | La evidencia más directa de la persistencia del ASP de memoria |
| Precio de contrato vs. precio spot de DRAM/NAND | Juicio sobre sobrecalentamiento y techo del superciclo de memoria genérica |
| Ingresos por alquiler de GPU en la nube | Proxy de la monetización real de la infraestructura de IA |
| Coste de inferencia y margen de servicios de IA | Capacidad de pago económica de los hyperscalers |
| Elasticidad unitaria de PC y smartphones | Si hay destrucción de la demanda de electrónica de consumo |
| Permisos eléctricos y PPA de centros de datos | Riesgo de retraso de oferta y diferimiento de CAPEX |

---

## 9. Conclusión final

<div class="thesis-callout">
  <div class="thesis-callout__label">Frase clave</div>
  <div class="thesis-callout__body">
    Quien paga el consenso de semiconductores de 2027 no es el consumidor, sino el CAPEX de los hyperscalers. Por tanto, la pregunta central no es "si hay demanda de IA", sino "si los ingresos de IA y la utilización de las GPU suben con la rapidez suficiente para justificar el CAPEX también después de 2027".
  </div>
</div>

Las previsiones de altos resultados de las cuatro compañías en 2027 no son matemáticamente imposibles. El CAPEX de los hyperscalers y del ecosistema de infraestructura de IA ya ha entrado en el rango de 800.000 millones a 1 billón de dólares y, si se incluye la financiación externa, puede pagar los ingresos de la cadena de suministro de 2027. Pero deben cumplirse <strong>tres condiciones a la vez</strong>.

1. Que el CAPEX de los hyperscalers se mantenga en 2027 en un mínimo de 800.000 millones a 1,1 billones de dólares, y que los actores fuera de las cuatro grandes (Oracle, OpenAI, IA soberana, China, empresas) cubran junto a ellos los ingresos de Nvidia y los costes no-GPU.
2. Que el precio de la memoria quede fijado por contratos a largo plazo, prepagos y capacity reservation, y no como una "prima de escasez transitoria".
3. Que la infraestructura de IA se convierta en ingresos reales. Para invertir al mismo ritmo también en 2028-2029, los ingresos por inferencia, el AI SaaS, la mejora en publicidad/búsqueda y la utilización de las GPU deben justificar la amortización y el coste eléctrico.

En resumen, la previsión de resultados de 2027 se sostiene como un <strong>"escenario de pago condicional liderado por los hyperscalers"</strong>, pero <strong>no se sostiene solo con la demanda gubernamental y la de los OEM de productos electrónicos</strong>. En particular, el beneficio de las tres compañías de memoria es más sensible al mantenimiento del ASP de memoria y a la persistencia de la escasez de HBM que al propio CAPEX de los hyperscalers. Por eso lo que hay que mirar ahora no es una "cesta de semiconductores de IA", sino <strong>un nodo cuello de botella con poder de fijación de precios y que aún cotiza con descuento por pico</strong>.

<small>Las cifras de este artículo citan el consenso de MarketScreener, los resultados oficiales de las compañías y los materiales de Gartner, IDC, Goldman Sachs, Morgan Stanley, TrendForce, Reuters, Mirae Asset y KB indicados en el texto, y todas son expectativas de mercado a mediados de 2026, no resultados reales. Los nombres de valores son ejemplos que ilustran el flujo de análisis, no recomendaciones de inversión; la decisión y la responsabilidad de invertir corresponden al propio inversor.</small>

## Sources

[1]: https://www.marketscreener.com/quote/stock/SAMSUNG-ELECTRONICS-CO-LT-35054473/finances/ "Samsung Electronics: Forecasts/Estimates | MarketScreener"
[2]: https://www.marketscreener.com/quote/stock/SK-HYNIX-INC-6494929/finances/ "SK hynix: Forecasts/Estimates | MarketScreener"
[3]: https://www.marketscreener.com/quote/stock/MICRON-TECHNOLOGY-INC-13639/finances/ "Micron Technology: Forecasts/Estimates | MarketScreener"
[4]: https://www.marketscreener.com/quote/stock/NVIDIA-CORPORATION-103502018/finances/ "NVIDIA: Forecasts/Estimates | MarketScreener"
[5]: https://www.gartner.com/en/newsroom/press-releases/2026-02-26-gartner-says-surging-memory-costs-will-reduce-global-pc-and-smartphone-shipments-in-2026 "Gartner: Surging Memory Costs Will Reduce PC and Smartphone Shipments in 2026"
[6]: https://www.idc.com/resource-center/blog/global-memory-shortage-crisis-market-analysis-and-the-potential-impact-on-the-smartphone-and-pc-markets-in-2026/ "IDC: Global Memory Shortage Crisis: Impact on Smartphone and PC Markets in 2026"
[7]: https://www.gartner.com/en/newsroom/press-releases/2026-04-08-gartner-forecasts-worldwide-semiconductor-revenue-to-exceed-us-dollars-one-point-3-trillion-in-2026 "Gartner: Worldwide Semiconductor Revenue to Exceed $1.3 Trillion in 2026"
[8]: https://www.trendforce.com/presscenter/news/20260602-13074.html "TrendForce: HBM Contract Prices Expected to Surge in 2027"
[9]: https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out "Goldman Sachs: Tracking Trillions: The Scale of the AI Build-Out"
[10]: https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Research_Bridging-Data-Center-Gap.pdf "Morgan Stanley: Bridging the Data Center Gap"
[11]: https://www.reuters.com/world/asia-pacific/nvidia-supplier-sk-hynix-q1-profit-rises-406-meets-forecasts-2026-04-22/ "Reuters: SK hynix says AI chip demand exceeds capacity"
[12]: https://securities.miraeasset.com/bbs/download/2143655.pdf?attachmentId=2143655 "Mirae Asset: Samsung Electronics 2027E"
[13]: https://commission.europa.eu/topics/competitiveness/ai-continent_en "European Commission: AI Continent (InvestAI)"
[14]: https://nvidianews.nvidia.com/news/saudi-arabia-and-nvidia-to-build-ai-factories-to-power-next-wave-of-intelligence-for-the-age-of-reasoning "Saudi Arabia and NVIDIA to Build AI Factories | NVIDIA Newsroom"
[15]: https://openai.com/index/five-new-stargate-sites/ "OpenAI, Oracle, SoftBank expand Stargate | OpenAI"
