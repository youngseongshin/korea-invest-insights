---
title: "Marvell Q1 FY2027 y semiconductores coreanos: el cuello de botella está en interconexión, sustratos y potencia, no en HBM"
date: 2026-05-28T10:20:00+09:00
description: "Los resultados de Marvell Q1 FY2027 no son simplemente un beat de EPS: muestran que el cuello de botella de los centros de datos de IA se está extendiendo hacia XPU personalizados, interconexión óptica, networking scale-up, FC-BGA, MLCC, condensadores de silicio y sockets de test. El read-through para semiconductores coreanos se ordena por Samsung Electro-Mechanics, Samsung Electronics, SK Hynix e ISC·Rhino Industrial·TSE."
categories: ["Market-Outlook"]
tags:
  - "Marvell"
  - "MRVL"
  - "마벨"
  - "한국 반도체"
  - "삼성전기"
  - "009150"
  - "삼성전자"
  - "005930"
  - "SK하이닉스"
  - "000660"
  - "ISC"
  - "리노공업"
  - "티에스이"
  - "FC-BGA"
  - "MLCC"
  - "실리콘 커패시터"
  - "HBM"
  - "AI ASIC"
  - "AI 인프라"
slug: marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28
valley_cashtags:
  - Marvell
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - ISC
  - 리노공업
  - 티에스이
  - 대덕전자
  - 이수페타시스
  - 심텍
draft: false
---

> 📚 Contexto del artículo anterior
> Este texto es la continuación de [Vista previa de cuellos de botella en semiconductores coreanos antes de resultados de Marvell y Broadcom](/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/). La pregunta planteada en el preview era: "¿La apuesta única en HBM se amplía hacia AI ASIC, redes y estabilización de potencia?" Este artículo responde esa pregunta con base en los resultados de Marvell Q1 FY2027. Los hubs relacionados son [AI HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/), [AI Sustratos y PCB Hub](/page/korea-ai-pcb-substrate-hub/) y [Hub de la cadena de valor de semiconductores coreanos](/page/korea-semiconductor-equipment-ip-hub/).

## TL;DR

Lo más importante de Marvell Q1 FY2027 no es el beat de EPS. Lo importante es que la compañía ha revisado al alza su trayectoria de crecimiento en centros de datos de IA para FY2027–FY2028, y ha explicado ese crecimiento a través de <strong>XPU personalizados, interconexión óptica, switching Ethernet, DCI, networking scale-up/scale-across y XPU attach</strong>.

Traducido al universo de semiconductores coreanos, la respuesta no es simplemente "comprar más HBM". HBM sigue siendo el eje central, pero el alpha incremental que estos resultados han confirmado está en los <strong>cuellos de botella de interconexión, sustratos, integridad de potencia y test alrededor de la GPU</strong>.

El orden de prioridades es el siguiente:

| Prioridad | Read-through coreano | Valores/segmento clave | Valoración |
|---:|---|---|---|
| 1 | FC-BGA + MLCC para servidores IA + condensadores de silicio | Samsung Electro-Mechanics (SEMCO) | El más directo. Sin embargo, ya refleja gran parte del re-rating; se requiere confirmar márgenes en SiCap y FC-BGA |
| 2 | HBM4, SOCAMM2, eSSD, advanced packaging | Samsung Electronics, SK Hynix | Beta en HBM se mantiene. El nuevo alpha está en el memory attach y packaging fuera del HBM |
| 3 | Sockets de test e interfaces para custom ASIC/XPU | ISC, Rhino Industrial, TSE | Estructura favorable, pero watchlist hasta confirmar ingresos directos |
| 4 | PCB/MLB de alta velocidad para AI networking | ISU Petasys, Daeduck Electronics, Simtech, etc. | Selección necesaria. No todo el "AI PCB" se beneficia por igual |

En cuanto a Marvell en sí, la postura es <strong>HOLD / Buy watch</strong>. Precio de referencia $198,70; precio objetivo a 12 meses $225, lo que implica un upside de aproximadamente +13%. La trayectoria de crecimiento es sólida, pero la valoración ya descuenta expectativas elevadas. Desde la perspectiva coreana, importa más <strong>hacia dónde se trasladan los cuellos de botella que Marvell ha identificado</strong> que el propio valor de Marvell.

---

## 1. Lo que realmente importa de los resultados de Marvell

Marvell publicó sus resultados del Q1 FY2027 en el aftermarket del 27 de mayo de 2026. Las cifras oficiales son las siguientes. ([Marvell][1])

| Concepto | Q1 FY2027 | Interpretación |
|---|---:|---|
| Ingresos | <strong>$2,418M</strong> | +28% interanual; +$18M sobre el punto medio de la guía |
| EPS GAAP | <strong>$0,04</strong> | Reducido por impacto contable de las adquisiciones de Celestial AI y XConn |
| EPS non-GAAP | <strong>$0,80</strong> | En línea con el consenso |
| Margen bruto GAAP | <strong>52,1%</strong> | Mejora interanual |
| Margen bruto non-GAAP | <strong>58,9%</strong> | Se mantiene en la banda alta del 58% a pesar de mayor mix de IA |
| Flujo de caja operativo | <strong>$638,8M</strong> | Récord de cash flow operativo |
| Guía de ingresos Q2 | <strong>$2.700M ±5%</strong> | Rango: $2.565M–$2.835M |
| Guía EPS non-GAAP Q2 | <strong>$0,93 ±$0,05</strong> | Línea base de rentabilidad para el próximo trimestre |

Los resultados en sí se acercan a un "ligero beat / EPS en línea". Sin embargo, lo relevante para la cotización y el read-through en semiconductores coreanos no son los pocos centavos del Q1, sino <strong>la trayectoria de ingresos para FY2027–FY2028 que la dirección ha comunicado</strong>.

Según transcripts de terceros, la dirección situó los ingresos de FY2027 en torno a $11.500M y los de FY2028 en torno a $16.500M, y revisó al alza la previsión de crecimiento de interconexión en FY2027 desde aproximadamente el 50% hasta más del 70%. Aunque estas cifras no proceden del transcript oficial de IR, su dirección es coherente con el comunicado oficial. El press release oficial de Marvell también identifica explícitamente como motores de crecimiento la óptica 800G/1.6T, los switches Ethernet de 51,2T, la óptica scale-up para NPO/CPO, los módulos DCI, los XPU personalizados y el XPU attach. ([Marvell][1], [StockAnalysis transcript][2])

En una sola frase:

> Marvell ha confirmado con cifras que el capex de los centros de datos de IA está migrando desde la compra de GPU hacia la infraestructura de interconexión de clústeres.

---

## 2. El eje central es la arquitectura de interconexión, no SOCAMM

El error de lectura más peligroso para un inversor coreano que analiza este earnings call sería reducirlo al "tema SOCAMM". SOCAMM es relevante, pero no es el centro del discurso de Marvell.

El orden de prioridades es el siguiente:

| Eje estratégico de Marvell | Por qué importa | Traducción al ecosistema coreano |
|---|---|---|
| XPU / ASIC personalizados | Señal de que los hyperscalers están ampliando su silicon de IA propio más allá de las GPU de NVIDIA | Diversificación de la base de clientes HBM, sustratos de packaging, sockets de test |
| Interconexión óptica | 800G/1.6T, DCI, scale-up optics son el cuello de botella en la expansión de clústeres de IA | PCB de alta velocidad y comunicaciones ópticas (selectivo); FC-BGA y estabilización de potencia de SEMCO son estructurales |
| Switching Ethernet | Hoja de ruta de 51,2T, 100T y 200T implica mayor dollar content en silicon de AI networking | FC-BGA para ASIC de red, placas de alta velocidad, inspección y test |
| XPU attach | CXL, NIC, memory attach e inferencia con KV cache | SOCAMM2 y eSSD de Samsung Electronics, DRAM para servidor, opciones de IP de memoria tipo OpenEdges |
| NVLink Fusion | Vía para que el silicon personalizado coexista dentro del ecosistema de NVIDIA | Expansión de la cadena de suministro más allá de la dicotomía "NVIDIA vs. ASIC" |

El anuncio conjunto NVIDIA-Marvell apunta en la misma dirección. NVIDIA invertirá $2.000M en Marvell, que a su vez suministrará XPU personalizados compatibles con NVLink Fusion y networking scale-up, además de colaborar en silicon photonics y AI-RAN. ([Marvell NVIDIA][3])

El mensaje es claro:

> Un centro de datos de IA no es una caja de GPU: es un sistema donde GPU, XPU personalizados, HBM, óptica, switches, retimers, CXL, NIC, FC-BGA y MLCC funcionan como un único organismo.

En consecuencia, la inversión en semiconductores coreanos debe pasar de "¿compro solo los grandes de memoria?" a "¿qué cuellos de botella por debajo de la memoria se van a materializar en cifras?"

---

## 3. Read-through coreano prioritario 1: Samsung Electro-Mechanics (SEMCO)

La traducción más directa de los resultados de Marvell al universo bursátil coreano es Samsung Electro-Mechanics. Hay tres razones.

Primero, los XPU personalizados, los switches Ethernet, la interconexión óptica y el XPU attach que Marvell ha destacado requieren todos packaging de alta velocidad y alta densidad, lo que enlaza con la demanda de FC-BGA.

Segundo, los servidores de IA operan con voltajes bajos y corrientes instantáneas elevadas. Para reducir la fluctuación de tensión alrededor del packaging de GPU, HBM y XPU se necesitan componentes de estabilización de potencia como MLCC y condensadores de silicio.

Tercero, Samsung Electro-Mechanics ya posee ambas capas. En los resultados del Q1 2026, la compañía informó que los ingresos de Package Solution alcanzaron 725.000 millones de KRW, con un crecimiento del 45% interanual y del 12% secuencial, y mencionó la ampliación del suministro de sustratos de alto valor añadido para aceleradores de IA, CPU de servidor y aplicaciones de red. ([Samsung Electro-Mechanics Q1][4])

Además, Samsung Electro-Mechanics ha firmado un contrato de suministro de condensadores de silicio por valor de 1,557 billones de KRW con una gran empresa global, con vigencia del 1 de enero de 2027 al 31 de diciembre de 2028. Estos componentes se describen como destinados a mejorar la estabilidad del suministro de potencia dentro del packaging de GPU y HBM para servidores de IA. ([Samsung Electro-Mechanics SiCap][5])

El marco de inversión en Samsung Electro-Mechanics ha cambiado de la siguiente manera:

| Marco anterior | Marco actual |
|---|---|
| Valor cíclico de MLCC y módulos de cámara para smartphone | Plataforma de integridad de potencia en packaging de IA + FC-BGA |
| Recuperación de la demanda móvil | Demanda de aceleradores de IA, CPU de servidor y ASIC de red |
| Ciclo de MLCC de uso general | Mix de MLCC/SiCap de alta capacidad, baja resistencia, ultrafino y alta fiabilidad |
| Comparación con Ibiden o Murata por separado | Comparativa híbrida MLCC + FC-BGA + SiCap |

Sin embargo, esta conclusión no equivale a "comprar a cualquier precio". Samsung Electro-Mechanics ya ha reflejado en buena medida el contrato de condensadores de silicio, la capitalización bursátil en torno a los 100 billones de KRW y el re-rating como infraestructura de IA. Las próximas variables de confirmación no son el momentum de la cotización, sino <strong>el margen bruto, el margen operativo de Package Solution, el rendimiento de producción de SiCap y la diversificación de clientes adicionales</strong>.

---

## 4. Samsung Electronics y SK Hynix: beta en HBM se mantiene; nuevo alpha en la periferia del HBM

Los resultados de Marvell no son negativos para el HBM. Al contrario. Aunque crezcan los XPU personalizados y el networking scale-up, el dollar content de memoria no disminuye. Conforme los modelos de IA evolucionan hacia agentic AI, razonamiento y mixture-of-experts, el movimiento de datos y los requisitos de memoria aumentan.

Desde el punto de vista de inversión, "HBM es positivo" ya es la tesis central. Lo nuevo que ha aportado el earnings call de Marvell es lo siguiente:

1. La base de clientes de HBM se amplía desde una estructura concentrada en GPU de NVIDIA hacia XPU personalizados de hyperscalers.
2. El XPU attach, conectado a CXL, NIC, memory attach y KV cache, influye también en DRAM para servidor, SOCAMM y eSSD.
3. A medida que los clústeres de IA crecen, aumenta el valor del packaging, los sustratos y la estabilización de potencia que conectan memoria y chips de cómputo.

Samsung Electronics tiene en este punto opciones múltiples. HBM4, HBM4E, SOCAMM2, SSD PM1763, foundry y advanced packaging forman parte del mismo stack de infraestructura de IA. Samsung Electronics presentó HBM4E, SOCAMM2 y el SSD PM1763 como productos de infraestructura de IA colaborativos con NVIDIA en el GTC 2026. ([Samsung Semiconductor][6])

SK Hynix sigue siendo el pure beta de HBM más puro. Sin embargo, si el análisis se limita a los resultados de Marvell, el nuevo alpha es mayor en <strong>Samsung Electro-Mechanics, sockets de test y sustratos de alta velocidad que crecen junto al HBM</strong> que en SK Hynix. SK Hynix es el eje principal, pero ya es también el valor con mayor atención del mercado.

---

## 5. Sockets de test: beneficiario silencioso de la proliferación de ASIC personalizados

La razón por la que el custom revenue importa en el earnings call de Marvell no es simplemente el volumen de chips. La clave son los <strong>SKU y los ciclos de cualificación</strong>.

Si los aceleradores de IA se estandarizaran en torno a una única GPU de NVIDIA, la demanda de componentes de test sería relativamente predecible. Por el contrario, si proliferan los XPU personalizados por hyperscaler, el XPU attach, CXL, NIC, switch ASIC y DPU, las condiciones de test y el diseño de sockets se fragmentarán.

En ese escenario, los sockets de test y los componentes de interfaz podrían beneficiarse simultáneamente en tres dimensiones:

| Variable | Dirección | Motivo |
|---|---|---|
| Volumen | Aumento | Crecimiento de SKU: custom ASIC, network ASIC, memory attach |
| ASP | Alza | Mayor dificultad de test: más pines, señales de alta velocidad, alta potencia |
| Ciclo de reposición | Estructural | Cambios generacionales y cualificaciones repetidas por cliente |

En Corea, ISC, Rhino Industrial y TSE son watchlist. Aquí corresponde ser cauteloso: con información pública disponible no es posible confirmar si las empresas coreanas de sockets de test están directamente integradas en la cadena de XPU personalizados de Marvell o de un hyperscaler concreto. Por tanto, en este momento se trata de una <strong>"posibilidad de beneficio"</strong>, no de un <strong>"mapeo confirmado de clientes"</strong>.

Los indicadores a vigilar en los resultados trimestrales son: ingresos de lógica AI/HPC, número de nuevos clientes, mix de sockets de alto valor y defensa del margen operativo.

---

## 6. El PCB general no es un activo de compra indiscriminada

Los resultados de Marvell son positivos para el AI networking y la interconexión óptica. Sin embargo, la conclusión "AI networking es bueno → todo el PCB es bueno" es errónea.

El beneficio se concentra en empresas que cumplen las siguientes condiciones:

1. Capacidad para trabajar con materiales de baja pérdida para señales de alta velocidad.
2. Exposición a MLB multicapa o sustratos de packaging de alto valor añadido.
3. Homologación como proveedor de clientes de servidores de IA o equipos de red.
4. Confirmación de crecimiento en ASP, número de capas y área, más que en volumen.

El hecho de que crezca el número de GPU y XPU no implica que el volumen de sustratos aumente en la misma proporción. En una arquitectura donde múltiples chips se integran más densamente en un único packaging y placa de alto rendimiento, lo que importa más que el volumen son <strong>el área del sustrato, el número de capas, la dificultad de los materiales y el rendimiento de producción</strong>.

Por ello, agrupar ISU Petasys, Daeduck Electronics, Simtech, TLB y Korea Circuit en una misma cesta resulta impreciso. El read-through real de los resultados de Marvell se acerca más a "seleccionar a quienes tienen sustratos multicapa para aplicaciones de red y materiales aptos para señales de alta velocidad".

---

## 7. Valoración de MRVL: una buena empresa no garantiza un buen precio de entrada

La postura sobre Marvell en sí es HOLD / Buy watch.

| Concepto | Detalle |
|---|---:|
| Precio de referencia | $198,70, cierre de mercado regular del 27-05-2026 |
| Precio objetivo a 12 meses | $225 |
| Potencial alcista | \~+13,2% |
| Marco de valoración | EV/Sales FY2028E |
| Valoración clave | La trayectoria de crecimiento ha sido revisada al alza, pero la valoración ya es elevada |

La fórmula del caso base es la siguiente:

```text
Precio objetivo = (Ingresos FY2028E × EV/Sales objetivo - Deuda neta) ÷ Acciones diluidas
```

Los supuestos son: ingresos FY2028E de $16.500M, EV/Sales objetivo de 12,5x, deuda neta de \~$1.117M y acciones diluidas de 915M. El resultado es un precio objetivo de aproximadamente $224, redondeado a $225.

Para que Marvell obtenga un re-rating comparable al de Broadcom se necesitan tres cosas:

1. Que los ingresos de silicon personalizado se confirmen como programas recurrentes y no como eventos de cliente único.
2. Que el margen bruto non-GAAP se defienda en la banda del 58–59% a pesar del crecimiento en interconexión y switching.
3. Que los prepagos para asegurar la cadena de suministro se traduzcan en un ramp de ingresos y en flujo de caja libre.

En definitiva: que Marvell sea ya una buena empresa es indiscutible; que sea un buen precio de entrada es una cuestión aparte.

---

## 8. Próximos puntos de control

| Punto de control | Señal fuerte | Señal débil |
|---|---|---|
| Ingresos Q2 FY2027 | Cerca o por encima del límite superior de $2.835M | Por debajo del punto medio de $2.700M |
| Ingresos Data Center | Crecimiento secuencial de high-teens o más | Desaceleración del crecimiento secuencial |
| Margen bruto non-GAAP | ≥59,25% o defensa del límite superior | Por debajo del 58,25% |
| Interconexión | Mantenimiento o revisión al alza de la previsión de +70% en FY2027 | Desaceleración del ramp de 800G/1.6T |
| XPU personalizados | Visibilidad de crecimiento ×2 o más en FY2028 y +$10.000M en FY2029 | Retrasos en el ramp por cliente |
| Switching scale-up | Confirmación de producción en serie con cliente tier-1 | Muchos engagements pero sin ingresos |
| Read-through coreano | Confirmación de cifras de Package Solution, SiCap y FC-BGA de SEMCO | Tema sólido pero sin márgenes ni pedidos confirmados |

Las variables de confirmación por valor coreano son más sencillas:

| Valor/segmento | Qué verificar |
|---|---|
| Samsung Electro-Mechanics (SEMCO) | Tasa de crecimiento de Package Solution, ingresos de FC-BGA para AI networking, rendimiento y margen de SiCap, contratos a largo plazo adicionales |
| Samsung Electronics | Homologación de clientes para HBM4, envíos reales de SOCAMM2, precio y volumen de eSSD, clientes de foundry/packaging |
| SK Hynix | Ramp de HBM4, diversificación de clientes, riesgo de sobreoferta en 2027 |
| ISC, Rhino Industrial, TSE | Ingresos de sockets de test para lógica de IA, nuevos clientes, mix de alto valor añadido, margen operativo |
| PCB/MLB | Homologación de cliente AI networking, subida de ASP, materiales de baja pérdida y mayor número de capas |

---

## 9. Condiciones de invalidación de la tesis

Las condiciones que debilitarían esta tesis son claras:

1. Los ingresos del Q2 de Marvell quedan por debajo del punto medio de $2.700M y el crecimiento de Data Center se desacelera.
2. El margen bruto non-GAAP cae por debajo del 58,25%, confirmando que el mix de custom/interconnect diluye márgenes.
3. La previsión de ingresos de FY2028 de $16.500M es revisada a la baja.
4. El XPU personalizado y el XPU attach quedan atados a retrasos en el calendario de clientes específicos.
5. El SiCap de Samsung Electro-Mechanics se confirma como ingreso de bajo margen o la tasa de crecimiento de FC-BGA se desacelera.
6. Los resultados de las empresas coreanas de sockets de test no muestran crecimiento en ingresos de lógica AI/HPC.
7. El lead time de HBM se acorta y aparecen señales de sobreoferta en 2027.

---

## Conclusión final

Los resultados de Marvell Q1 FY2027 no son una señal de "comprar solo HBM" para los semiconductores coreanos. El mensaje más preciso es:

> A medida que los clústeres de IA crecen, el cuello de botella migra desde la GPU hacia la interconexión, los sustratos, la estabilización de potencia y el test.

Desde esta perspectiva, el valor coreano más directamente expuesto es Samsung Electro-Mechanics. En SEMCO, los MLCC, el FC-BGA y los condensadores de silicio convergen en el mismo cuello de botella del packaging de IA. Samsung Electronics y SK Hynix siguen siendo esenciales como eje del HBM, pero el alpha incremental que han revelado los resultados de Marvell es mayor en la periferia del HBM. ISC, Rhino Industrial y TSE son candidatos a un beneficio de segundo orden por la proliferación de ASIC personalizados, pero permanecen en watchlist hasta confirmar ingresos directos.

La conclusión no es una compra indiscriminada. Incluso una buena tesis termina siendo solo un tema si no se confirma con cifras. Lo que hay que vigilar en los semiconductores coreanos este trimestre no es la cotización, sino <strong>los ingresos de Package Solution, el margen de SiCap, los ingresos de test de lógica de IA y el ASP de sustratos de alta velocidad</strong>.

---

## Hecho / Inferencia / Especulación / Bloqueado

### [Hecho]

- Los ingresos de Marvell en Q1 FY2027 fueron $2.418M, +28% interanual, y la guía de ingresos para Q2 es $2.700M ±5%. ([Marvell][1])
- El margen bruto non-GAAP de Marvell en Q1 fue del 58,9%; la guía de margen bruto non-GAAP para Q2 es del 58,25%–59,25%. ([Marvell][1])
- Marvell citó como motores de crecimiento la óptica scale-out 800G/1.6T, los switches Ethernet de 51,2T, la óptica scale-up, los módulos DCI, los XPU personalizados y el XPU attach. ([Marvell][1])
- NVIDIA invertirá $2.000M en Marvell; Marvell suministrará XPU personalizados compatibles con NVLink Fusion y networking scale-up. ([Marvell NVIDIA][3])
- Los ingresos de Package Solution de Samsung Electro-Mechanics en Q1 2026 alcanzaron 725.000 millones de KRW, con un crecimiento del 45% interanual y del 12% secuencial. ([Samsung Electro-Mechanics Q1][4])
- Samsung Electro-Mechanics ha firmado un contrato de suministro de condensadores de silicio por valor de 1,557 billones de KRW, con vigencia del 1 de enero de 2027 al 31 de diciembre de 2028. ([Samsung Electro-Mechanics SiCap][5])

### [Inferencia]

- Es razonable traducir los ejes de crecimiento de Marvell al universo coreano en el siguiente orden: FC-BGA/MLCC/SiCap de SEMCO, memory attach de Samsung Electronics y SK Hynix, sockets de test y sustratos de alta velocidad.
- El HBM sigue siendo el eje principal, pero el alpha incremental revelado por estos resultados es mayor en las capas de interconexión, packaging, estabilización de potencia y test que en los grandes valores de memoria.
- El re-rating de Samsung Electro-Mechanics debe interpretarse no como recuperación del ciclo de MLCC sino como transición hacia una plataforma de pasivos y sustratos para infraestructura de IA.

### [Especulación]

- Se especula en el mercado con que el cliente del SiCap de Samsung Electro-Mechanics podría estar vinculado a un hyperscaler norteamericano o a la cadena de suministro de aceleradores de IA, pero la contraparte del contrato no ha sido divulgada.
- No es posible determinar con información pública si las empresas coreanas de sockets de test participan directamente en los programas de XPU personalizados de Marvell o de sus clientes.
- El AI-RAN podría generar oportunidades a largo plazo en RF y semiconductores de red en Corea, pero es demasiado pronto para considerarlo como catalizador de resultados a corto plazo en 2026.

### [Bloqueado]

- Participación directa de empresas coreanas en los programas de XPU personalizados, óptica y switching de Marvell.
- Nombre del cliente, margen por producto y velocidad de ramp mensual del contrato de SiCap de Samsung Electro-Mechanics.
- Desglose de ingresos por cliente de lógica de IA en ISC, Rhino Industrial y TSE.
- PER NTM en tiempo real, EV/EBITDA y tasa de revisión al alza del EPS consenso de los valores coreanos de PCB/sustratos en 2026.

---

## Fuentes

[1]: https://investor.marvell.com/news-events/press-releases/detail/1023/marvell-technology-inc-reports-first-quarter-of-fiscal-year-2027-financial-results "Marvell Technology, Inc. Reports First Quarter of Fiscal Year 2027 Financial Results"
[2]: https://stockanalysis.com/stocks/mrvl/transcripts/583849-q1-2027/ "Marvell Technology Q1 2027 Earnings Call Transcript & Audio"
[3]: https://investor.marvell.com/news-events/press-releases/detail/1019/nvidia-ai-ecosystem-expands-as-marvell-joins-forces-through-nvlink-fusion "NVIDIA AI Ecosystem Expands as Marvell Joins Forces Through NVLink Fusion"
[4]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Announces Q1 2026 Business Performance"
[5]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
[6]: https://semiconductor.samsung.com/news-events/news/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026/ "Samsung Unveils HBM4E at NVIDIA GTC 2026"

*Descargo de responsabilidad: Solo para fines de investigación e información. No constituye asesoramiento de inversión. Las empresas mencionadas se citan únicamente con fines analíticos; los lectores deben realizar su propia diligencia debida y consultar a asesores autorizados antes de tomar cualquier decisión de inversión.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
