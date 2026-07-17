---
title: "¿Son cíclicos los semiconductores y cuál es el valor razonable? Valorando Samsung, SK Hynix y Micron con FCFE y beneficios normalizados"
slug: "memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17"
date: 2026-07-17T20:00:00+09:00
description: "Samsung a 3,9x y SK Hynix a 4,3x sobre el consenso de 2028 significa que el mercado duda de la duración de esos beneficios, no de su existencia. Este análisis recorre si los semis son cíclicos, qué múltiplo corresponde a qué BPA, si el debate actual afecta al BPA de 2028 o solo al múltiplo, por qué 2029 no está tan lejos, y a dónde va realmente la caja de 2026-2028, para después calcular valores razonables ponderados por probabilidad con FCFE más un valor terminal normalizado."
categories: ["Exclusive Analysis", "Valuation", "Tech-Analysis"]
tags: ["Samsung Electronics", "SK Hynix", "Micron", "Memoria", "HBM", "Valoración", "FCFE", "Cíclico", "Beneficios normalizados", "Valor razonable"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexto
> Este artículo es la continuación cuantitativa de [El verdadero debate entre alcistas y bajistas de los semiconductores](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/), que concluyó que "la industria es alcista, pero la acción cotiza en territorio bajista de valoración", y ahora calcula de forma cuantitativa <strong>cuál es entonces el valor razonable</strong>. Si [Valoración de beneficios 2028E de Samsung Electronics y SK Hynix](/es/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/) trató "los números que parecen baratos", este artículo calcula el valor razonable con FCFE y un valor terminal normalizado. Conviene leerlo junto con [El peor escenario ya está en el precio](/es/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/) y [El recorte de beneficios del segundo trimestre de SK Hynix](/es/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/). Los hubs relacionados son el [Hub de IA y HBM](/es/page/korea-semiconductor-hbm-kospi-hub/) y el [Hub de Exclusive Analysis](/es/page/exclusive-analysis-hub/).

## TL;DR

* Si se aplica el precio de cierre en KRX del 17 de julio (Samsung Electronics 255.000 KRW, SK Hynix 1.842.000 KRW) al BPA de consenso de 2028 del 16 de julio, el PER resultante es <strong>3,9x y 4,3x</strong> respectivamente. El mercado no está asumiendo que el beneficio de 2028 desaparezca, sino incorporando en el precio <strong>la posibilidad de que ese beneficio no dure mucho tiempo</strong>.
* Los semiconductores no pueden agruparse en una sola industria. La memoria sigue siendo cíclica, y HBM no es un producto que haya eliminado el ciclo, sino uno que <strong>alarga su duración y reduce la elasticidad de la oferta</strong>.
* El debate actual sacude en la superficie primero al múltiplo. Sin embargo, dado que el significado económico de la caída del múltiplo anticipa la normalización del BPA posterior a 2028, el problema del múltiplo y el problema del BPA no pueden separarse por completo.
* La premisa de "¿es 2028 o es 2029?" es errónea desde el inicio. El precio de la acción es <strong>el valor presente de los flujos de caja atribuibles al accionista que se generarán de forma perpetua a partir de 2026</strong>. Aplicar un PER bajo al BPA de 2028 y aplicar un PER normal al BPA normalizado de 2029 dan la misma respuesta si los supuestos son consistentes.
* El valor razonable ponderado por probabilidad calculado con FCFE y un valor terminal normalizado es <strong>385.000 KRW para Samsung Electronics (+51%), 1.950.000 KRW para SK Hynix (+6%) y 1.140 USD para Micron (+34%)</strong>. El atractivo ajustado por riesgo sigue el orden Samsung Electronics, Micron, SK Hynix. \[Inferencia: cálculo propio\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Marco clave</div>
  <div class="thesis-callout__body">
    La premisa de fijar el precio de la acción en el BPA de 2028 o en el BPA de 2029 ya es incorrecta desde el inicio. Lo correcto es sumar el FCFE de 2026-2028 al valor terminal normalizado de 2029, y al calcularlo de esta manera, el margen de seguridad de los tres valores se ordena de mayor a menor como Samsung Electronics, Micron y SK Hynix.
  </div>
</div>

---

## 1. ¿Son cíclicos los semiconductores?

No hay una única respuesta. La intensidad del ciclo difiere según el segmento.

| Área | Naturaleza del ciclo | Razón |
|---|---|---|
| DRAM y NAND de propósito general | Muy fuerte | Homogeneidad del producto, inventarios, ampliaciones de capacidad y variación del ASP |
| HBM | De media a fuerte | La certificación, el apilado y los LTA son barreras de entrada, pero el alto margen provoca ampliaciones de capacidad y multiplicidad de proveedores |
| Foundry y equipos | De media a fuerte | CAPEX de los clientes y ciclos de transición de proceso |
| Fabless y plataformas | Gran dispersión según el producto | Existe foso competitivo, pero hay exposición al recambio generacional y al CAPEX de los clientes |

La expresión más precisa es <strong>"una industria que crece estructuralmente, pero cuyo precio y beneficio son cíclicos"</strong>.

La exposición difiere según el valor. SK Hynix tiene la exposición más pura a memoria y HBM. Samsung Electronics tiene una alta sensibilidad de beneficios en los auges de memoria, pero el móvil, los paneles, la foundry y la caja amortiguan parcialmente la parte baja.

### Qué dicen las propias compañías

Este juicio no es la interpretación de un observador, sino que se basa en <strong>documentos oficiales de las propias compañías</strong>. \[Hecho: presentación ante la SEC\]

SK Hynix calificó la industria de memoria como <strong>highly cyclical</strong> en su F-1 ante la autoridad estadounidense. Micron señaló en su 10-Q que, si bien HBM requiere más obleas y más salas blancas que la DRAM de propósito general para producir la misma cantidad de bits, <strong>si la demanda de HBM se debilita y esa capacidad de producción regresa a la DRAM de propósito general, la oferta de DRAM podría dispararse</strong>.

Al combinar estas dos frases se obtiene la conclusión. HBM solo retrasa la respuesta de la oferta, no elimina el ciclo. \[Inferencia: síntesis de ambas presentaciones\]

---

## 2. ¿Cuál es el múltiplo razonable?

Para discutir el PER razonable primero hay que definir <strong>a qué BPA se aplica</strong>. Un mismo 8x resulta caro si se aplica al beneficio pico y razonable si se aplica al beneficio normalizado.

| BPA aplicado | Samsung Electronics | SK Hynix | Interpretación |
|---|---:|---:|---|
| BPA pico 2027-2028 | 5,5-7,5x | 5-7x | Descuenta la normalización posterior del beneficio |
| BPA normalizado | 8-10x | 7-9x | Aplicado al beneficio promedio de 3-5 años |
| Confirmación de meseta estructural | 9-11x | 8-10x | Solo se permite si el beneficio se mantiene incluso después de 2029 |

Para que Samsung Electronics supere 9x deben confirmarse a la vez la recuperación de cuota en HBM y la reducción de las pérdidas de foundry. Para SK Hynix, el rango de 8-10x requiere cuota en HBM4E, la renegociación de precios de los LTA, retorno al accionista y defensa del margen tras el aumento de la oferta.

Por eso, <strong>aplicar directamente 9-12x al consenso de 2028 es un escenario fuertemente alcista que usa a la vez el beneficio pico y el múltiplo estructural</strong>. En una empresa cíclica, el PER no necesariamente es el más bajo en el pico y el más alto en la recesión, o simplemente no es calculable en ese momento. El valor de continuidad debe calcularse con el beneficio normalizado, no con el pico ni con el mínimo. \[Hecho: metodología de valoración cíclica de McKinsey\]

---

## 3. ¿El debate actual sacude el BPA o solo el múltiplo?

Separando el debate por tipo, la respuesta cambia.

| Debate | Impacto inmediato | Condición que también dañaría el BPA |
|---|---|---|
| Liquidación de apalancamiento en un solo valor | Múltiplo y flujos de mercado | Ninguna, es un factor técnico |
| Preocupación por tipos de interés, deuda de IA y ROI | Múltiplo primero | Recorte de CAPEX en dos o más big tech |
| Resistencia de precio de los compradores | Múltiplo + riesgo de BPA | Caída del precio de contrato y descenso de pedidos simultáneos |
| Ampliación de capacidad de los tres fabricantes de memoria | BPA 2028 y múltiplo | Aumento real de producción calificada y de la oferta de bits |
| CXMT y YMTC | Múltiplo a largo plazo primero | Certificación global, envíos masivos y presión de precios |
| Cuellos de botella de LTA y empaquetado de HBM | Defensa de BPA y múltiplo | Mantenimiento del precio mínimo y del volumen contratado |

### Los números de los analistas todavía no se han movido

Según WiseReport local, el BPA 2028 de Samsung Electronics es idéntico, 65.907 KRW, tanto el 13 como el 16 de julio. El de SK Hynix bajó de 433.625 a 427.332 KRW, un <strong>-1,5%</strong>. \[Hecho: consenso de WiseReport\]

Es decir, los números de los analistas apenas se han movido y <strong>el precio de la acción se movió primero</strong>.

### Pero tampoco se ha bajado solo el múltiplo

Si se resuelve a la inversa un PER normalizado de 8x, se obtiene el BPA que el mercado está permitiendo en realidad.

| Valor | BPA implícito a 8x | Consenso 2028 | Brecha |
|---|---:|---:|---:|
| Samsung Electronics | 31.875 KRW | 65.907 KRW | -52% |
| SK Hynix | 230.250 KRW | 427.332 KRW | -46% |

El mercado está mezclando los dos casos siguientes.

1. El BPA de 2028 se mantiene cerca del consenso, pero cae rápido a partir de 2029.
2. El propio BPA de 2028 se reduce por la expansión de la oferta y la resistencia de precios de los compradores.

Los datos confirmados hasta ahora están <strong>más cerca del caso 1</strong>. Todavía no se han confirmado conjuntamente cancelaciones de CAPEX, caídas de precios de contrato, aumento de inventarios ni renegociación de LTA. Sin embargo, la ampliación de capacidad y la resistencia de los compradores son variables reales que podrían desplazar el panorama hacia el caso 2. \[Inferencia: interpretación de datos\]

El ajuste actual todavía no es un mercado de rebajas de resultados, sino <strong>una reevaluación de la duración del beneficio</strong>. Sin embargo, el objeto real de la ansiedad que el mercado expresa a través del múltiplo es el BPA posterior a 2028, y si el precio de contrato, los inventarios y el CAPEX empeoran, esto se convertirá en un mercado de rebajas del BPA de 2028.

---

## 4. ¿Es 2028 o es 2029?

La premisa misma de esta pregunta es incorrecta desde el inicio. El precio de la acción no se determina por uno de los dos años. Es <strong>el valor presente de los flujos de caja atribuibles al accionista que se generarán de forma perpetua a partir de 2026</strong>.

```text
Valor presente
= valor presente del FCFE 2026-2028
+ valor presente del valor terminal a fines de 2028

Valor terminal a fines de 2028 ≈ BPA normalizado de 2029 × PER normalizado
```

Usar el BPA de 2028 no significa ignorar lo que viene después de 2029. Es una forma de <strong>comprimir el riesgo de caída posterior a 2029 dentro de un PER bajo aplicado al BPA de 2028</strong>. Si se usa directamente el BPA normalizado de 2029, se puede aplicar un PER más normal. Si los supuestos son consistentes, ambos métodos deberían llegar a resultados similares.

Se trata de decir lo mismo de dos formas distintas, y sin embargo con frecuencia se discute cuál de las dos es la correcta.

---

## 5. ¿Está 2029 demasiado lejos en el futuro?

Tres años no es un plazo lejano en la valoración de acciones. Con una tasa de retorno exigida del 11%, 1 won de 2029 vale hoy aproximadamente 0,731 won.

```text
1/(1,11)^3 = 0,731
```

Aunque un inversor venda la acción dentro de un año, <strong>el comprador de ese momento mirará los flujos de caja posteriores a 2029</strong>. Como el precio de venta final vuelve a determinarse por los flujos de caja futuros, un horizonte de inversión corto no permite evitar el beneficio de largo plazo. El modelo FCFE de Damodaran también calcula el valor de la acción como la suma del FCFE del período de proyección explícito más el valor terminal que le sigue. \[Hecho: modelo FCFE de NYU Stern\]

---

## 6. ¿No se considera la caja de 2026-2028?

Sí se considera. Solo que <strong>el BPA y la caja que efectivamente vuelve al accionista son cosas distintas</strong>.

Sumando el consenso de WiseReport del 16 de julio se obtiene lo siguiente. \[Hecho: agregación de consenso\]

| Valor | BPA 2026E | BPA 2027E | BPA 2028E | BPA acumulado a 3 años | Sobre el precio actual |
|---|---:|---:|---:|---:|---:|
| Samsung Electronics | 46.664 KRW | 65.802 KRW | 65.907 KRW | 178.373 KRW | 70% |
| SK Hynix | 314.787 KRW | 438.114 KRW | 427.332 KRW | 1.180.233 KRW | 64% |

Si el consenso se cumple, el beneficio acumulado de 3 años equivale al 64-70% del precio actual, una magnitud que no puede ignorarse.

El problema es que el beneficio contable no es, tal cual, caja para el accionista.

```text
FCFE = beneficio neto - CAPEX neto - aumento del capital de trabajo + endeudamiento neto
```

Las empresas de memoria aumentan fuertemente la inversión en fábricas, EUV y empaquetado durante los auges. Si de un beneficio neto de 100 se destinan 60 a ampliación de capacidad, la caja que se atribuye de inmediato es 40. Los otros 60 tampoco desaparecen, pero <strong>solo se convierten en valor si la nueva capacidad genera un retorno superior al costo de capital</strong>.

El beneficio de 2026-2028 se traslada al precio de la acción a través de dividendos y recompras, aumento de la caja neta, reducción de deuda, incremento del valor en libros y ampliaciones de capacidad de alto retorno. A la inversa, si justo después de la ampliación llega un exceso de oferta, esa caja se convierte en equipo y hasta el ROE futuro se reduce. Esta es la razón por la que el mercado no valora el beneficio neto de un auge a razón de 1 won por cada 1 won.

### Las dos rutas que refleja el precio actual

El precio actual equivale, sobre el consenso de 2028, a 3,9x para Samsung Electronics y 4,3x para SK Hynix. El mercado mezcla lo siguiente.

1. Una parte considerable del beneficio de 2026-2028 se reinvierte en ampliación de capacidad.
2. El ASP y el margen se normalizan a partir de 2029.

Por eso, la variable de juicio no es tanto "si el BPA de 2029 se reduce", sino <strong>la magnitud de esa reducción</strong> y <strong>la proporción del beneficio de 2026-2028 que efectivamente queda como FCFE o caja neta</strong>.

| Ruta 2029 | Método de valoración |
|---|---|
| BPA -10% a -20%, luego estable | FCFE explícito + PER normalizado 8-10x |
| BPA -30% a -50%, luego recuperación | FCFE explícito + múltiplo de BPA normalizado 7-9x |
| BPA -50% o peor, exceso de oferta persistente | PBR normalizado, caja neta y valor de recorte de producción, antes que PER |

McKinsey también sostiene que en las empresas cíclicas hay que ponderar por probabilidad los escenarios de ciclo normal y de cambio estructural, y calcular el valor terminal con el flujo de caja normalizado, no con el pico ni con el mínimo. \[Hecho: metodología de McKinsey\]

---

## 7. Calculado con precisión, ¿cuál es el valor razonable?

Se aplicó el marco anterior a números reales. El valor razonable ponderado por probabilidad con fecha 17 de julio de 2026 es el siguiente. \[Inferencia: cálculo propio, con los supuestos indicados abajo\]

### Método de cálculo

```text
Valor razonable = FCF restante de 2026 + FCF 2027 + FCF 2028 + valor terminal a fines de 2028
Valor terminal = BPA normalizado de 2029 × PER razonable
```

- <strong>Tasa de descuento</strong>: Samsung Electronics 10,5%, SK Hynix 11,5%, Micron 10,5%
- <strong>Probabilidades</strong>: demanda excedente 30%, vacío de pedidos y reconcentración 40%, normalización de la oferta 20%, cortocircuito crediticio 10%
- <strong>PER terminal</strong>: Samsung Electronics 7,5-8,5x, SK Hynix 6-9x, Micron 7-9,5x
- <strong>Tratamiento del ciclo bajista</strong>: se refleja en el FCF el 45-90% de la caída del beneficio, aplicando a la vez el CAPEX fijo y la posibilidad de recortarlo

### Resultado

| Valor | Precio actual | Valor razonable ponderado por probabilidad | Potencial de subida | Rango de sensibilidad |
|---|---:|---:|---:|---:|
| Samsung Electronics | 255.000 KRW | <strong>385.000 KRW</strong> | +51% | 316.000-461.000 KRW |
| SK Hynix | 1.842.000 KRW | <strong>1.950.000 KRW</strong> | +6% | 1.480.000-2.480.000 KRW |
| Micron | 853,20 USD | <strong>1.140 USD</strong> | +34% | 905-1.410 USD |

El rango de sensibilidad resulta de mover 10 puntos porcentuales las probabilidades de demanda excedente y de normalización de la oferta, y de variar simultáneamente la tasa de descuento en ±1,5 puntos porcentuales y el PER terminal en ±1x.

### Valor presente por escenario

| Escenario | Probabilidad | Samsung Electronics | SK Hynix | Micron |
|---|---:|---:|---:|---:|
| Demanda excedente sostenida | 30% | 548.000 KRW | 3.415.000 KRW | 1.735 USD |
| Vacío de pedidos y reconcentración | 40% | 347.000 KRW | 1.581.000 KRW | 1.086 USD |
| Normalización de oferta y eficiencia | 20% | 283.000 KRW | 1.064.000 KRW | 674 USD |
| Cortocircuito crediticio sistémico | 10% | 241.000 KRW | 732.000 KRW | 505 USD |

Esta tabla revela la diferencia de carácter entre los tres valores. <strong>Samsung Electronics se mantiene por encima del precio actual incluso en el escenario de normalización de la oferta (283.000 KRW).</strong> En cambio, <strong>SK Hynix ya queda por debajo del precio actual desde el segundo escenario (1.581.000 KRW).</strong> Esto significa que el retorno esperado actual de SK Hynix depende en mayor medida de que la demanda excedente se sostenga.

---

## 8. La diferencia que crea el FCF

Aunque el beneficio se desacelere en 2029, la caja generada en los tres años anteriores no desaparece. El tamaño de este colchón difiere según el valor.

| Valor | FCF 2026F | FCF 2027F | FCF 2028F | Peso del FCF de 3 años en el valor ponderado por probabilidad |
|---|---:|---:|---:|---:|
| Samsung Electronics | 158,2 billones KRW | 385,0 billones KRW | 412,7 billones KRW | <strong>26%</strong> |
| SK Hynix | 74,7 billones KRW | 177,4 billones KRW | 172,0 billones KRW | 17% |
| Micron | 50,6 miles de millones USD | 124,3 miles de millones USD | 145,9 miles de millones USD | 18% |

\[Hecho: informe de Samsung Securities (Samsung Electronics), recopilación de informes de Korea Investment & Securities (SK Hynix), estimaciones de FactSet (Micron)\]

<strong>En Samsung Electronics, el 26% del valor ponderado por probabilidad proviene del FCF de 2026-2028.</strong> Es decir, incluso si el escenario posterior a 2029 empeora, es la que tiene la mayor proporción de caja ya asegurada. SK Hynix es la más baja, con 17%, por lo que la mayor parte de su valor depende del valor terminal posterior a 2029.

---

## 9. Prioridad final

<strong>1º, Samsung Electronics</strong>: el mayor margen de seguridad. El precio actual está cerca del valor del escenario bajista duro. La caja neta y la diversificación de negocio amortiguan la parte baja del valor terminal, y el peso del 26% del FCF de 3 años añade un colchón adicional.

<strong>2º, Micron</strong>: atractivo según el valor razonable central, pero sensible a la nueva oferta de 2028. También hay que considerar que el valor razonable de Morningstar, como ancla bajista externa, es de 850 USD, similar al precio actual. \[Hecho: Morningstar\]

<strong>3º, SK Hynix</strong>: el momentum de negocio más fuerte, pero el margen de seguridad de precio más delgado. Un nuevo juicio requiere confirmar el precio y el rendimiento de HBM4E y el LTA de 2028.

Por lo tanto, en el precio actual el <strong>atractivo ajustado por riesgo sigue el orden Samsung Electronics, Micron, SK Hynix</strong>. El hallazgo central de este cálculo es que el orden de calidad del negocio (SK Hynix es el más fuerte por su exposición pura a HBM) es inverso al orden de atractivo del precio. \[Inferencia: juicio integrado\]

---

## 10. Resumen del método de valoración por valor

- <strong>Samsung Electronics</strong>: se suma el FCFE de 2026-2028 por separado y se descuenta aplicando 8-10x al BPA normalizado de 2029. La caja neta y la diversificación de negocio amortiguan la parte baja del valor terminal.
- <strong>SK Hynix</strong>: se suma el FCFE de 2026-2028 reflejando la ampliación de capacidad y la dilución, y se aplica 7-9x al BPA normalizado de 2029. Solo se permite el extremo superior cuando se confirme la meseta de HBM.

Tanto valorar el consenso de 2028 a un simple 4x como aplicar mecánicamente 9-12x son enfoques incompletos. Lo correcto es <strong>sumar el valor terminal normalizado de 2029 al FCFE de 2026-2028 y agregarlo por escenario</strong>.

---

## Conclusión

Resumiendo las respuestas a cada pregunta en una línea.

¿Son cíclicos los semiconductores? La memoria sí lo es. HBM no eliminó el ciclo, solo lo alargó, y esto lo dicen por sí mismos el F-1 de SK Hynix y el 10-Q de Micron.

¿Cuál es el múltiplo razonable? Primero hay que definir a qué BPA se aplica. 5-7x en el pico, 7-10x en la normalización.

¿Qué sacude el debate actual? En la superficie es el múltiplo, pero lo que ese múltiplo expresa es el BPA posterior a 2028. Los números de los analistas se han movido hasta ahora apenas un 1,5%, y el precio de la acción se adelantó.

¿2028 o 2029? Ninguno de los dos. Se suma el valor terminal normalizado de 2029 al FCFE de 2026-2028.

¿Está 2029 demasiado lejos? Dentro de tres años, 1 won vale hoy 0,73 won. Aunque se venda dentro de un año, ese comprador mirará 2029.

¿Se refleja la caja de 2026-2028? Se refleja, pero no como el BPA tal cual. Hay que restar lo que sale hacia la ampliación de capacidad, y esa capacidad solo se convierte en valor si gana más que el costo de capital.

Entonces, ¿cuánto es? 385.000 KRW para Samsung Electronics, 1.950.000 KRW para SK Hynix y 1.140 USD para Micron. El valor con el momentum de negocio más fuerte y el valor con el mayor margen de seguridad de precio no son el mismo.

---

_Esta publicación es un análisis calculado de forma propia con base en las cotizaciones de KIS KRX (2026-07-17), el consenso de WiseReport (2026-07-16), presentaciones ante la SEC (F-1 de SK Hynix, 10-Q de Micron), estimaciones de FCF de casas de bolsa, y las metodologías de valoración públicas de McKinsey y NYU Stern. El valor razonable ponderado por probabilidad, las probabilidades de cada escenario, el PER terminal y la tasa de descuento son todos estimaciones basadas en los supuestos del autor al momento de escribir este artículo, y no son guía de la compañía ni consenso. Los cambios en las estimaciones de los analistas posteriores a la fuerte caída del 17 de julio todavía no están reflejados. El BPA acumulado es la suma del beneficio contable y no es una estimación de FCFE. Los valores mencionados son ejemplos para explicar la metodología de valoración y no constituyen una recomendación de compra o venta de ningún valor en particular. La decisión de inversión y su responsabilidad recaen únicamente en el inversor._

---

### Publicaciones relacionadas

- [El verdadero debate entre alcistas y bajistas de los semiconductores: cuatro relojes reales y un reloj de precio](/es/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [Valoración de beneficios 2028E de Samsung Electronics y SK Hynix: números que parecen baratos y verificación del ciclo](/es/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/)
- [¿Están realmente sobrevendidas Samsung Electronics y SK Hynix según el consenso de 2027?](/es/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/)
- [El recorte de beneficios del segundo trimestre de SK Hynix, ¿por qué se mantuvo el precio objetivo?](/es/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/)
- [Por qué el fallo de resultados de IBM es evidencia de la fortaleza de la memoria](/es/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/)
