---
title: "Futuros de tokens de IA y coste por token: ahora es una carrera de costes, no de rendimiento"
date: 2026-05-30T09:00:00+09:00
description: "La Bolsa de Futuros de Shanghái está diseñando en fase temprana futuros vinculados al precio de los tokens de IA, mientras CME e ICE preparan futuros de cómputo GPU. Cuando el uso de IA tiene un precio de mercado, la industria pasa de una carrera de rendimiento a una de coste por token. La conclusión: no compre acciones genéricas de IA, sino las piezas, chips y plataformas cuello de botella que reducen el coste por token del cliente. La lectura para Corea pasa por Samsung Electronics (HBM, eSSD, KV-cache) y Samsung Electro-Mechanics (FC-BGA, MLCC, condensador de silicio)."
categories: ["Market-Outlook"]
tags:
  - "AI token futures"
  - "cost per token"
  - "tokens per watt"
  - "한국 반도체"
  - "삼성전자"
  - "005930"
  - "SK하이닉스"
  - "000660"
  - "삼성전기"
  - "009150"
  - "Broadcom"
  - "Marvell"
  - "TSMC"
  - "Nvidia"
  - "CME"
  - "ICE"
  - "HBM"
  - "eSSD"
  - "KV-cache"
  - "FC-BGA"
  - "MLCC"
  - "실리콘 커패시터"
  - "AI 인프라"
slug: ai-token-futures-cost-per-token-korea-semiconductor-thesis-2026-05-30
valley_cashtags:
  - 삼성전자
  - SK하이닉스
  - 삼성전기
  - 대덕전자
draft: false
---

> 📚 Contexto de la serie
> Es la continuación de [La sorpresa de resultados de Dell y los semiconductores coreanos](/post/dell-q1-fy2027-earnings-korea-ai-server-margin-readthrough-2026-05-29/) y [Marvell Q1 FY2027 y los semiconductores coreanos](/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/). Si los dos posts anteriores sostenían que "el cuello de botella de la IA baja del GPU hacia la memoria, la interconexión, el sustrato y la energía, y quién captura el margen ahí", este va un paso más allá. Cuando el propio uso de IA tiene precio de mercado, el campo de batalla pasa de "un chip más rápido" a "un token más barato". Hubs relacionados: [Hub HBM de IA](/page/korea-semiconductor-hbm-kospi-hub/), [Hub de la cadena de valor de semiconductores de Corea](/page/korea-semiconductor-equipment-ip-hub/), [Hub de PCB y sustratos de IA](/page/korea-ai-pcb-substrate-hub/).

## TL;DR

Hasta ahora, invertir en IA ha sido una pelea por "quién fabrica el chip más potente". Pero acaba de encenderse una señal silenciosa. <strong>El propio uso de IA empieza a tener un precio de mercado.</strong>

Según Reuters, la Bolsa de Futuros de Shanghái (SHFE) está diseñando en fase temprana futuros vinculados al precio de los tokens de IA. En EE. UU., CME Group (con Silicon Data) e ICE (con Ornn) anunciaron planes para futuros de cómputo GPU. Ninguno es todavía un producto cotizado y confirmado. Pero la dirección es clara.

> Cuando el cómputo y los tokens de IA tienen un "precio de mercado", el eje de la industria pasa de una <strong>carrera de rendimiento a una carrera de costes.</strong>

Es lo mismo que cuando el petróleo tuvo un precio de futuros: refino, transporte y generación se alinearon por "coste por barril". Una vez que el precio por token de la IA es visible, todos se hacen la misma pregunta: <strong>"¿cuánto me cuesta producir un token?"</strong>

La respuesta no son las "acciones de IA" genéricas. Son las <strong>piezas, chips y plataformas cuello de botella que realmente reducen el coste por token del cliente</strong>. El orden de prioridad:

| Prioridad | Qué comprar | Nombres clave | Visión |
|---:|---|---|---|
| 1 | ASIC personalizado / redes de IA | Broadcom, Marvell, TSMC | Lo más directo a la pila de coste de tokens. Pero es un consenso largo: disciplina de valoración, riesgo de concentración de clientes |
| 2 | HBM + eSSD + almacenamiento KV-cache | Samsung Electronics, SK Hynix, Micron | El ancho de banda de memoria y la gestión de caché son el cuello de botella de la inferencia. eSSD/KV-cache reducen el cómputo repetido y alivian el HBM |
| 3 | Empaquetado avanzado / FC-BGA / MLCC / condensador de silicio | Samsung Electro-Mechanics, Daeduck Electronics, Murata, Ibiden | Integridad de potencia y señal → rendimiento efectivo de tokens. Riesgo de "dirección correcta, precio equivocado" |
| 4 | Riel de precios de cómputo | CME, ICE | La financiarización misma. Valor de opción, prelanzamiento, liquidez incierta. La idea de segundo orden menos concurrida |
| 5 | Pila completa Nvidia / AMD | Nvidia, AMD | Sigue siendo central. Pero la tesis pasa a ser "más tokens por vatio y economía de la fábrica de IA", no "escasez de GPU" |
| 6 | Equipos eléctricos | HD Hyundai Electric, LS Electric | No es un corto directo. La demanda eléctrica sigue subiendo (IEA: ~945 TWh de centros de datos para 2030). Solo como cobertura de valor relativo frente a una prima de escasez eléctrica sobreestirada |

La conclusión para Corea primero: <strong>Samsung Electronics es la elección práctica más equilibrada.</strong> HBM4E (recuperación) + DDR5 + SOCAMM2 + eSSD PCIe Gen6 + almacenamiento KV-cache le dan la exposición más amplia en toda la pila de coste de tokens. SK Hynix es el nombre de mejor calidad pero está concurrido. Samsung Electro-Mechanics tiene alta pureza de tesis pero el precio importa. Daeduck Electronics es un candidato beta de FC-BGA de segundo orden.

---

## 1. Qué está pasando: la financiarización del uso de IA

Primero, separemos los hechos.

- <strong>[Hecho]</strong> Según Reuters, la SHFE está <strong>diseñando en fase temprana</strong> futuros vinculados al precio de los tokens de IA. La especificación del contrato, la definición del subyacente (qué token), el método de liquidación y el calendario de aprobación/lanzamiento están todos <strong>sin confirmar</strong>.
- <strong>[Hecho]</strong> CME Group anunció planes para lanzar futuros de cómputo con Silicon Data; ICE anunció planes de contratos de futuros de cómputo GPU con Ornn.

Lo importante aquí no es que "los futuros ya cotizan". No es así. Lo importante es que <strong>la industria ha empezado a intentar ponerle precio al uso de IA</strong>.

Una analogía: imagine usar electricidad sin un precio estándar de "X por kilovatio-hora". En cuanto abre una bolsa eléctrica y se cotizan precios, cada fábrica empieza a calcular "¿cuánta electricidad usamos por unidad de producto?". La IA está ahora justo en ese umbral.

> Cuando el precio se hace visible, el coste se hace visible. Cuando el coste se hace visible, gana quien lo reduce.

---

## 2. Por qué cambia las reglas: carrera de rendimiento → carrera de costes

Durante años, la carrera de la IA fue de "puntuaciones de benchmark": quién corre un modelo mayor en un chip más rápido. La inversión siguió la misma lógica: "compra la empresa que fabrica el GPU más potente".

Cuando el uso tiene precio, la pregunta cambia.

El coste por token, en su forma más simple:

```text
Coste por token = coste total de cómputo / tokens procesados
```

Se reduce achicando el numerador (coste de cómputo) o aumentando el denominador (tokens procesados). Gana quien extrae más tokens de la misma electricidad y el mismo capital. Así que dos métricas se convierten en el nuevo campo de batalla:

```text
Tokens por vatio = tokens/seg / potencia (W)
Tokens por dólar = tokens / coste total ($)
```

Según Reuters, TSMC ve que el foco del diseño de chips se desplaza del rendimiento bruto a la eficiencia energética por la demanda eléctrica de la IA, lo que convierte a los <strong>tokens por vatio</strong> en una métrica clave.

En lenguaje de inversión, es claro:

> No "compra acciones de IA", sino <strong>"compra las empresas que reducen el coste por token del cliente".</strong>

---

## 3. La analogía de la cocina: el chef caro está parado

Hagámoslo más concreto.

Un GPU es un chef muy caro. Sus manos son rápidas, pero solo cocina si los ingredientes llegan a tiempo. La cinta transportadora que trae los ingredientes es la memoria (HBM).

¿Qué pasa si la cinta es lenta? El chef caro se queda esperando ingredientes. El reloj del salario sigue corriendo. No salen tokens. El coste por token se dispara.

Así que el verdadero cuello de botella muchas veces no es "contratar otro chef" (= un GPU más potente). Es más eficaz <strong>acelerar la cinta y apilar de antemano los ingredientes más usados junto al chef</strong> (= ancho de banda de memoria + caché).

El almacenamiento KV-cache es justamente "apilar de antemano los ingredientes más usados". Evita rehacer el mismo cálculo y ahorra tiempo del chef caro. El eSSD hace esa despensa barata y grande. Esto también reduce la carga sobre el HBM.

Esta analogía es el mapa de inversión de este post. <strong>El dinero fluye hacia donde baja el coste por token.</strong>

---

## 4. Prioridad 1: ASIC personalizado / redes de IA — Broadcom, Marvell, TSMC

La pila global más directa para reducir el coste de tokens es el ASIC personalizado y las redes de IA.

Cuando un hiperescalador usa un chip a medida para su carga de trabajo (un ASIC personalizado), hace el mismo trabajo más barato y con menos energía que un GPU genérico. Las redes de IA son lo que une esos chips en un clúster. Ambos elevan los tokens por vatio directamente.

| Empresa | Hechos confirmados | Visión |
|---|---|---|
| Broadcom | Ingresos de IA Q1 FY2026 de 8.400 M$ (+106 % interanual); guía de ingresos de semiconductores de IA del Q2 ~10.700 M$ | El núcleo del ASIC personalizado / redes. Consenso largo: disciplina de valoración |
| Marvell | Ingresos Q1 FY2027 de 2.418 M$; según Reuters, objetivo de ingresos de chips personalizados >10.000 M$ para FY2029 | Senda de crecimiento de silicio personalizado. La concentración de clientes es la variable clave |
| TSMC | Según Reuters, la demanda eléctrica de la IA desplaza el foco del diseño de chips del rendimiento a la eficiencia → "tokens por vatio" como métrica clave | La fundición por la que pasa al final todo ASIC / GPU. El suelo de la pila de coste de tokens |

Una advertencia: este es ya el consenso largo que más gusta al mercado. Una gran empresa y un gran precio no son lo mismo. Y los ingresos de ASIC personalizado están concentrados en pocos clientes grandes, así que el vaivén de pedidos de un solo cliente puede mover mucho las cifras.

---

## 5. Prioridad 2: HBM + eSSD + almacenamiento KV-cache — Samsung Electronics, SK Hynix, Micron

En la inferencia, el verdadero cuello de botella no es el cómputo bruto sino el <strong>ancho de banda de memoria y la gestión de caché</strong>. Es exactamente la analogía chef-cinta de la Sección 3.

- El HBM es la cinta ultrarrápida justo al lado del chef.
- El eSSD y el almacenamiento KV-cache son la despensa donde se apilan de antemano los ingredientes más usados. Evitan repetir el mismo cálculo, ahorran tiempo de GPU caro y alivian la carga sobre el HBM.

Los materiales de resultados del 1T26 de Samsung Electronics citaron demanda de DDR5, SOCAMM2, eSSD PCIe Gen6 y almacenamiento KV-cache. Esa gama encaja con precisión en la tesis de coste de tokens.

| Empresa | Exposición al coste de tokens | Visión |
|---|---|---|
| Samsung Electronics | HBM4E (recuperación) + DDR5 + SOCAMM2 + eSSD PCIe Gen6 + almacenamiento KV-cache | La exposición más amplia. Cubre varias capas de la pila de coste de tokens |
| SK Hynix | Exposición pura a HBM de la mejor calidad | La mejor empresa en sí, pero la posición más concurrida del mercado |
| Micron | Uno de los tres líderes globales de HBM/memoria | El comparable estadounidense. Exposición al ciclo HBM/DRAM |

Para una discusión más profunda de Samsung Electronics, véase [Análisis de la recompra por bonos extraordinarios de Samsung](/post/samsung-electronics-stock-bonus-supercycle-buyback-2026-05-27/) y el [Análisis a fondo de Samsung Electronics](/post/kr-deep-dive-samsung-electronics-2026-04-14/); para SK Hynix, véase el [Análisis a fondo de SK Hynix](/post/kr-deep-dive-sk-hynix-2026-04-16/).

Si hubiera que elegir uno, <strong>la exposición coreana más equilibrada a la tesis de coste de tokens es Samsung Electronics</strong>. SK Hynix es más limpio como beta pura de HBM, pero a lo largo de KV-cache, eSSD y SOCAMM2, Samsung cubre más capas, y la concentración del mercado es menor en Samsung que en SK Hynix.

---

## 6. Prioridad 3: empaquetado avanzado / FC-BGA / MLCC / condensador de silicio — Samsung Electro-Mechanics, Daeduck

Por bueno que sea un chip, si la potencia tiembla y la señal se rompe, el rendimiento efectivo de tokens cae. El empaquetado avanzado, los sustratos y los componentes de estabilización de potencia protegen la integridad de potencia y de señal.

- El FC-BGA es el sustrato de alto rendimiento que conecta el chip a la placa.
- Los MLCC y los condensadores de silicio amortiguan las oscilaciones de tensión transitorias dentro del paquete GPU/HBM.

Una capa sólida aquí permite que el chef caro funcione a plena velocidad, produciendo más tokens. Así que aunque estas piezas son indirectas, afectan claramente al coste por token.

| Empresa | Exposición | Visión |
|---|---|---|
| Samsung Electro-Mechanics | Paquete de FC-BGA + MLCC de gama alta + condensador de silicio | Alta pureza de tesis. Pero la valoración ya está estirada: un punto de "dirección correcta, precio equivocado" |
| Daeduck Electronics | Candidato beta de FC-BGA de segundo orden | El siguiente asiento tras SEMCO. La cualificación / volumen directos son condición previa |
| Murata, Ibiden | Comparables japoneses de MLCC / empaquetado | Se siguen juntos como pares globales |

Para análisis detallado de SEMCO, véase [Cuello de botella de componentes pasivos en servidores de IA: explicación técnica de SEMCO](/post/ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26/).

> La dirección es correcta. Pero el precio es alto.

La tesis de coste de tokens sí apunta al empaquetado y los sustratos, pero Samsung Electro-Mechanics ya ha descontado buena parte de eso. Así que en Corea, una beta de FC-BGA de segundo orden como Daeduck Electronics puede ser la alternativa de "misma dirección, precio menos estirado", siempre que se confirmen antes la cualificación directa y el volumen.

---

## 7. Prioridad 4: riel de precios de cómputo — CME, ICE

El punto de partida de este post, y su idea de segundo orden menos concurrida, es el riel de precios de cómputo.

Si la financiarización del uso de IA realmente arraiga, las bolsas donde ocurre ese trading se benefician estructuralmente, igual que las bolsas disfrutaron de flujos de comisiones estables cuando arraigaron los futuros del petróleo.

| Empresa | Exposición | Visión |
|---|---|---|
| CME | Planes para lanzar futuros de cómputo con Silicon Data | Una opción sobre la financiarización misma. Prelanzamiento, liquidez incierta |
| ICE | Planes de contratos de futuros de cómputo GPU con Ornn | Igualmente un valor de opción de prelanzamiento |

Pero esto es valor de opción, no ingresos confirmados. No se sabe si los contratos realmente cotizan ni si se construye volumen. Trátelo como una "rama lateral de la financiarización de la IA": la idea de segundo orden de menor peso.

---

## 8. Prioridad 5: pila completa Nvidia / AMD — la tesis cambia

Nvidia y AMD siguen siendo centrales. No se quedan fuera. Pero la tesis cambia.

La tesis antigua era "los GPU escasean, así que gana quien los fabrica". La tesis de la era del coste de tokens es distinta.

> No "escasez de GPU", sino <strong>"quién ofrece la pila completa con más tokens por vatio y la mejor economía de fábrica de IA".</strong>

Nvidia es fuerte no solo porque sus chips son rápidos, sino porque agrupa GPU, redes y software para reducir el coste por token de toda la fábrica de IA. En este marco, la pregunta clave no es "qué tan rápido es el próximo chip" sino "qué tan barato produce tokens el próximo sistema".

---

## 9. Prioridad 6: equipos eléctricos — una cobertura de valor relativo, no un corto

Vale la pena abordar una idea errónea común. "Si importa la eficiencia de coste de tokens, la demanda eléctrica baja, así que basta con cortar las eléctricas, ¿no?".

<strong>No.</strong> La demanda eléctrica en sí sigue subiendo.

> La IEA prevé que el consumo eléctrico global de los centros de datos alcance ~945 TWh para 2030 (aproximadamente 2x respecto a 2024).

Eso no es base para un corto directo sobre equipos eléctricos. Cortar sin más nombres como HD Hyundai Electric o LS Electric es peligroso.

Solo hay una manera de usar los equipos eléctricos aquí: una <strong>cobertura de valor relativo</strong>. Úsela solo, y con moderación, cuando se cumplan las tres condiciones a la vez:

1. Las estimaciones de BPA de semiconductores se revisan al alza, mientras
2. Las estimaciones de BPA de equipos eléctricos se estancan, y
3. Las valoraciones de equipos eléctricos están en máximos históricos.

En otras palabras, solo tiene sentido como cobertura de valor relativo frente a una "prima de escasez eléctrica sobreestirada". No un corto directo.

---

## 10. Disciplina: "financiarización = comprar todo" es codicia

Esta tesis es atractiva. Pero su tamaño y la decisión de inversión son cosas distintas. Hay que separar tres cosas.

1. <strong>[Hecho]</strong>: se anunciaron los planes de futuros de cómputo CME-Silicon Data e ICE-Ornn. Se publicaron las cifras de Broadcom, Marvell y TSMC. La previsión de 945 TWh de la IEA es pública.
2. <strong>[Inferencia]</strong>: una vez que el uso tiene precio, la industria pasa de una carrera de rendimiento a una de coste por token. Entonces los cuellos de botella que reducen el coste de tokens (ASIC personalizado, memoria, empaquetado) quedan estructuralmente favorecidos. Es una inferencia razonable a partir de los hechos.
3. <strong>[Especulación]</strong>: la especificación del contrato de futuros de la SHFE, la definición del token subyacente, el método de liquidación y el calendario de aprobación están todos sin confirmar. Qué fabricante coreano de componentes suministra a qué cliente, y con qué cuota de ingresos, tampoco se ha divulgado.

En particular, los futuros de tokens de IA de la SHFE deben tratarse no como "un producto ya cotizado y confirmado", sino como una <strong>señal temprana y un valor de opción</strong>. Y las afirmaciones específicas de cliente/cuota — "Samsung suministra el almacenamiento KV-cache de este cliente", "Daeduck tiene el X % de este FC-BGA" — no son verificables con fuentes públicas.

> Incluso una tesis sólida termina como un tema si no se valida en las cifras.

La conclusión no es "la IA se financiariza → comprar todas las acciones relacionadas". Es <strong>elegir selectivamente los cuellos de botella que realmente reducen el coste por token del cliente, a un precio defendible</strong>.

---

## 11. Próximos puntos de control

| Punto de control | Señal fuerte | Señal débil |
|---|---|---|
| Financiarización del uso de IA | SHFE / CME / ICE cotiza realmente y construye volumen en al menos uno | Se estanca en la fase de diseño, liquidez insuficiente |
| ASIC personalizado | Sube la visibilidad de ingresos personalizados de Broadcom / Marvell | Retrasos de pedidos de un solo cliente / riesgo de concentración |
| Memoria / KV-cache | Confirmados volumen y precio de eSSD / SOCAMM2 / KV-cache de Samsung | Se intensifica la competencia en HBM, se debilita el precio |
| Empaquetado / sustrato | Confirmado el margen de paquete de SEMCO; cualificación / volumen de Daeduck | El crecimiento se desacelera mientras la valoración sigue alta |
| Tokens por vatio | TSMC / Nvidia ponen al frente las métricas de eficiencia energética | Solo se repiten titulares de rendimiento |
| Equipos eléctricos | BPA de semis↑ + BPA eléctrico estancado + valoración eléctrica en máximos históricos a la vez | Si cualquiera de las tres falla → esperar para la cobertura |

---

## Interpretación final

Los futuros de tokens de IA y de cómputo GPU son todavía tempranos. Nada cotiza; no se ha construido volumen. Pero la dirección es clara.

> En cuanto el uso de IA tiene un precio de mercado, el campo de batalla pasa de "un chip más rápido" a "un token más barato".

Desde este punto de vista, lo que hay que comprar no son acciones genéricas de IA, sino los cuellos de botella que realmente reducen el coste por token del cliente. A nivel global, el ASIC personalizado / redes (Broadcom, Marvell, TSMC) es lo más directo, y la memoria / almacenamiento KV-cache resuelve el cuello de botella de la inferencia. En Corea, la elección práctica más equilibrada es <strong>Samsung Electronics</strong>: su recuperación de HBM4E, DDR5, SOCAMM2, eSSD PCIe Gen6 y almacenamiento KV-cache cubren la pila de coste de tokens de la forma más amplia. SK Hynix es el de mejor calidad pero concurrido; Samsung Electro-Mechanics tiene alta pureza de tesis pero un precio alto; Daeduck Electronics es un candidato beta de FC-BGA de segundo orden. Los equipos eléctricos no son un corto, solo una cobertura de valor relativo usada cuando se alinean las condiciones.

La conclusión es disciplina. Cuanto más se financiariza la IA, más importa "a qué precio" tanto como "qué comprar".

---

## Hecho / Inferencia / Especulación / Bloqueado

### [Hecho]

- Según Reuters, la SHFE está diseñando en fase temprana futuros vinculados al precio de los tokens de IA. La especificación del contrato, la definición del token subyacente, la liquidación y el calendario de aprobación están sin confirmar.
- CME Group anunció planes para lanzar futuros de cómputo con Silicon Data; ICE anunció planes de contratos de futuros de cómputo GPU con Ornn.
- Ingresos de IA de Broadcom Q1 FY2026 de 8.400 M$ (+106 % interanual); guía de ingresos de semiconductores de IA del Q2 ~10.700 M$.
- Ingresos Q1 FY2027 de Marvell de 2.418 M$. Según Reuters, Marvell apunta a ingresos de chips personalizados >10.000 M$ para FY2029.
- Según Reuters, TSMC ve el foco del diseño de chips desplazarse del rendimiento a la eficiencia energética por la demanda eléctrica de la IA, lo que hace de los "tokens por vatio" una métrica clave.
- La IEA prevé que la electricidad global de los centros de datos alcance ~945 TWh para 2030 (~2x respecto a 2024).
- Los materiales de resultados del 1T26 de Samsung Electronics citaron demanda de DDR5, SOCAMM2, eSSD PCIe Gen6 y almacenamiento KV-cache.

### [Inferencia]

- Una vez que el uso de IA tiene precio, la industria pasa de una carrera de rendimiento a una de coste por token.
- Los cuellos de botella que reducen el coste por token (ASIC personalizado / redes de IA → memoria / KV-cache → empaquetado / sustrato) quedan estructuralmente favorecidos.
- En Corea, Samsung Electronics tiene la exposición más equilibrada en toda la pila de coste de tokens; SK Hynix es el de mejor calidad pero muy concurrido.
- Como la demanda eléctrica sigue subiendo, un corto directo sobre equipos eléctricos es inapropiado; úselo solo como cobertura de valor relativo cuando se alineen las condiciones.

### [Especulación]

- Si los futuros de tokens de IA de la SHFE realmente cotizan y se negocian, y cómo se definiría el token subyacente, es incierto.
- El momento de lanzamiento y la liquidez de los futuros de cómputo de CME / ICE no están confirmados.
- A qué clientes globales suministran fabricantes coreanos concretos (Samsung Electronics, Samsung Electro-Mechanics, Daeduck Electronics), y con qué cuota de ingresos, no se ha divulgado.

### [Bloqueado]

- La especificación del contrato, el método de liquidación y el calendario de aprobación de los futuros de la SHFE.
- Tasas de revisión de BPA de consenso en tiempo real y valoraciones NTM de los nombres coreanos.
- La cuota a nivel de cliente y la mezcla de ingresos de los proveedores coreanos en las cadenas de ASIC personalizado / memoria / empaquetado.

---

*Aviso legal: solo para fines de investigación e información. No es asesoramiento de inversión. Los nombres citados son ilustrativos; los lectores deben realizar su propia diligencia y consultar a asesores autorizados antes de cualquier decisión de inversión.*
