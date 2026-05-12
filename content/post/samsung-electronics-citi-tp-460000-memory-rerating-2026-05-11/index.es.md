---
title: "Samsung Electronics Citi TP ₩460.000 — La tesis real no es 'Samsung sube más'. Es que 'el marco del ciclo de memoria está equivocado esta vez'."
slug: samsung-electronics-citi-tp-460000-memory-rerating-2026-05-11
date: 2026-05-11T22:30:00+09:00
description: "Citi elevó el precio objetivo de Samsung Electronics de ₩300.000 a ₩460.000, un potencial alcista del +61% frente al cierre de ₩285.500. El fondo del informe no es 'Samsung es una buena acción', sino que la creencia de 30 años de que 'los precios de la memoria suben y luego caen' puede estar equivocada esta vez, porque la IA ha cambiado estructuralmente la naturaleza de la demanda de memoria. Este artículo explica qué es la memoria, qué es el HBM, por qué la IA consume tanto, y si la lógica de Citi se sostiene. El beneficio operativo del 1T26 fue de ₩57,2 billones con un margen del 65,7% en la división DS — no es el perfil financiero de una empresa de semiconductores, es el de una plataforma monopolística. La pregunta clave es si este número es sostenible, y la respuesta llega con los precios del 2T26 y las cualificaciones de clientes para HBM4E."
categories: ["Sector-Deep-Dive", "Korea Market"]
tags:
  - "Samsung Electronics"
  - "Citi"
  - "ciclo de memoria"
  - "HBM"
  - "HBM4"
  - "HBM4E"
  - "SOCAMM"
  - "memoria para IA"
  - "renta variable coreana"
  - "DRAM"
  - "NAND"
---

> 🔗 **Lecturas relacionadas**: [Samsung Electronics 2026 — IA / HBM / Foundry en profundidad](/post/kr-deep-dive-samsung-electronics-2026-04-16/) · [Samsung Electronics vs. Samsung Electro-Mechanics — Reaceleración del capex de IA en Big Tech](/post/bigtech-1q26-samsung-electronics-vs-electro-mechanics-2026-04-30/) · [El peso de Samsung Electronics en el índice KOSPI](/post/samsung-electronics-weight-in-kospi-index-2026/) · [SK hynix: cuota de mercado en HBM 2026](/post/sk-hynix-hbm-market-share-ai-memory-demand-2026/) · [Por qué Corea, Parte 3 — Samsung / SK hynix y el re-rating de la economía coreana](/post/samsung-sk-hynix-korea-ai-economy-rerating-2026-05-09/) · [Centro de inversión HBM / KOSPI](/page/korea-semiconductor-hbm-kospi-hub/)

*Citi elevó el precio objetivo de Samsung Electronics de ₩300.000 a ₩460.000. Frente al cierre del 11 de mayo de ₩285.500, eso representa un potencial del +61%, lo que implicaría \~₩1.020 billones de capitalización adicional. Parece agresivo. Pero el fondo del informe no es "Samsung sube más". Es que la creencia de 30 años —"los precios de la memoria suben y luego caen"— puede estar equivocada esta vez, porque la IA ha cambiado estructuralmente la naturaleza de la demanda de memoria. Que esa tesis sea correcta o no importa más que el titular del precio objetivo. Para juzgarlo, primero hay que entender qué es la memoria y qué cambió la IA.*

---

## Resumen ejecutivo

* **Citi TP ₩460.000.** Desde ₩300.000 (+53% de revisión). Potencial alcista del +61% frente al cierre del 11 de mayo de ₩285.500.
* **El resultado del 1T es el punto de partida.** Samsung Electronics registró un beneficio operativo consolidado de ₩57,2 billones en el 1T26. Solo la división DS (semiconductores) aportó ₩53,7 billones con un **margen del 65,7%**. Eso no es el perfil financiero de una empresa de semiconductores; es el de una plataforma monopolística.
* **La tesis central de Citi.** No se trata solo de que el HBM (memoria de alto ancho de banda para IA) suba de precio. La demanda de IA está absorbiendo capacidad de fabricación de forma generalizada, **elevando también los precios del DRAM y NAND de commodity junto con el HBM**. El argumento es que se trata de un cambio estructural en la forma de la demanda, no de un ciclo transitorio.
* **Para que ₩460.000 sea alcanzable.** Los beneficios del 1T deben "sostenerse estructuralmente durante el 2S26" en lugar de ser un pico. Las dos variables de verificación son la trayectoria de precios de memoria en el 2T y las cualificaciones de clientes para HBM4E.

---

## 1. Principios básicos — qué es la memoria y por qué importa para la IA

### 1.1 Memoria = el "escritorio de trabajo" de un ordenador

Los ordenadores necesitan dos cosas: **dispositivos de cómputo** (CPU, GPU) y **dispositivos de almacenamiento / preparación** (memoria, almacenamiento).

```
Analogía: un oficinista.
CPU/GPU = el cerebro. Hace cálculos, toma decisiones.
Memoria (DRAM) = el escritorio de trabajo. Contiene los documentos en uso.
                 Un escritorio más grande permite trabajar con más papeles a la vez.
Almacenamiento (NAND) = el archivador. Guarda los archivos que no se están usando.
                        Un archivador más grande permite guardar más documentos en total.
```

**DRAM**: memoria volátil; los datos desaparecen al apagar el equipo. Se usa para "datos en uso en este momento" — lectura/escritura rápida. Se encuentra en smartphones, PCs y servidores.

**NAND**: memoria no volátil; los datos persisten al apagar el equipo. Se usa en SSD. Almacena fotos, vídeos y datos de aplicaciones.

Samsung Electronics es el **número 1 mundial tanto en DRAM como en NAND** por cuota de mercado. SK hynix es el número 2 y Micron (EE. UU.) el número 3. Estos tres concentran la mayor parte del mercado global de memoria.

### 1.2 HBM — el "escritorio enorme" que la IA exigió

El DRAM estándar es el "escritorio de tamaño normal". Basta para navegar por internet, trabajar con documentos o jugar. **La IA necesita que ese escritorio sea gigantesco.** Los grandes modelos de lenguaje al nivel de ChatGPT deben manipular cientos de miles de millones de parámetros simultáneamente.

```
DRAM estándar: 16 GB-64 GB. Suficiente para PCs y smartphones habituales.
HBM: decenas a cientos de GB. Integrado directamente junto al chip de IA (GPU)
     para transferencia de datos de altísimo ancho de banda.

Analogía:
DRAM estándar = un escritorio normal
HBM = una biblioteca entera desplegada sobre un escritorio

Por qué el HBM es caro:
1. Varios chips DRAM apilados verticalmente (8, 12, 16 capas)
2. Cada capa conectada mediante vías a escala de micras (TSVs)
3. Integrado directamente junto al GPU (empaquetado avanzado)
→ Complejidad de fabricación muy superior al DRAM estándar
→ ASP varias veces o decenas de veces superior
```

**Generaciones de HBM**: HBM → HBM2 → HBM2E → HBM3 → HBM3E → **HBM4** → HBM4E. A mayor generación, mayor capacidad, mayor ancho de banda y mejor eficiencia energética. Samsung Electronics **inició los envíos en producción masiva de HBM4 en el 1T** y planea **suministrar muestras de HBM4E en el 2T**.

[SK hynix](/post/sk-hynix-hbm-market-share-ai-memory-demand-2026/) lidera el mercado de HBM (principal proveedor de NVIDIA); Samsung Electronics está cerrando distancias. Parte de lo que Citi está señalando es que "Samsung está recuperando terreno en HBM".

### 1.3 SOCAMM — el nuevo factor de forma de memoria para servidores de IA

```
Memoria de servidor convencional:
Módulos en formato DIMM insertados en la placa base del servidor.
Mayor huella física, mayor consumo energético.

SOCAMM (System On Chip Attached Memory Module):
Memoria situada más cerca de la CPU/GPU, más pequeña y eficiente.
Ahorra espacio y energía en servidores de IA mejorando el rendimiento.

Analogía:
DIMM = un disco duro externo grande conectado por USB
SOCAMM = memoria soldada directamente junto al procesador
```

Samsung Electronics **inició los envíos en producción masiva de SOCAMM2 (segunda generación) en el 1T**. Este factor de forma se conecta a las próximas plataformas de IA de NVIDIA (Vera Rubin y sucesores).

### 1.4 Por qué la IA consume tanta memoria

Cuando se le hace una pregunta a ChatGPT se produce una "inferencia": el modelo genera una respuesta. Cada paso de inferencia mueve cantidades masivas de datos a través de la memoria.

```
Por qué la IA devora memoria:

1. Los modelos crecieron
   GPT-3: 175.000 millones de parámetros
   GPT-4: billones de parámetros (estimado)
   → un modelo más grande requiere más memoria

2. La longitud del contexto aumentó
   Antes: preguntas y respuestas cortas
   Ahora: leer y analizar decenas de páginas
   → el contexto de la conversación debe guardarse en memoria (caché KV)

3. Los agentes de IA se multiplicaron
   Antes: los humanos escribían consultas directamente
   Ahora: los agentes de IA consultan a otros agentes y agregan respuestas
   → un agente de IA suele consumir más memoria que un usuario humano

4. Los usuarios se multiplicaron
   ChatGPT, Claude y Gemini sirven colectivamente a cientos de millones
   → usuarios simultáneos × tamaño del modelo × longitud del contexto = demanda de memoria astronómica
```

**El "crecimiento de tokens de IA" — la expresión de Citi** — es exactamente esto. A medida que el número de tokens (fragmentos de palabras) que procesan los modelos de IA se dispara, la demanda de memoria se expande de forma estructural.

---

## 2. La creencia de 30 años sobre el ciclo de memoria — y por qué Citi intenta revertirla

### 2.1 El patrón que se repitió durante tres décadas

La industria de la memoria tiene un patrón bien establecido: **"los precios suben → las fábricas se expanden → la oferta se dispara → los precios se desploman."**

```
Ciclo de memoria convencional:
Sube la demanda → suben los precios → los márgenes se disparan
→ Samsung / SK hynix / Micron aumentan el capex
→ 1-2 años después, sobreoferta
→ caída de precios → pérdidas
→ recorte del capex → escasez
→ suben los precios otra vez (bucle)

Este ciclo de 3-4 años se ha repetido durante 30 años.
```

Los inversores conocen bien este patrón. Por eso, cuando suben los precios de la memoria, el mercado asume "pronto se romperán" y asigna un PER bajo. "Los beneficios están en el pico, por lo que el múltiplo no puede subir" es la lógica. Por eso Samsung Electronics genera ₩57 billones de beneficio operativo y sigue cotizando a PER 9-10×.

### 2.2 La tesis de Citi — "Esta vez puede ser diferente"

El argumento central de Citi es que **"el ciclo convencional puede no funcionar esta vez."** Dos razones:

**Primera, la demanda de memoria para IA es estructural, no cíclica.** Los ciclos pasados de precios de memoria venían impulsados por ciclos de renovación de PCs, oleadas de adopción de smartphones, expansión de centros de datos — picos de demanda temporales. La IA es diferente. Los modelos siguen creciendo, los usuarios siguen aumentando y los agentes de IA consumen más memoria por "usuario" que los humanos. La demanda no "sube y baja" — **sigue creciendo**.

**Segunda, el HBM absorbe capacidad de fabricación.** El HBM se fabrica en las mismas plantas que el DRAM estándar, pero cada stack de HBM consume 3-4 veces más superficie de oblea que el DRAM de commodity equivalente. A medida que la demanda de IA redirige asignaciones de fábrica hacia el HBM, la producción de DRAM de commodity se reduce. Por tanto, **no solo el HBM se encarece — los precios del DRAM y NAND de commodity también suben.**

```
Silogismo central de Citi:

Explosión de la demanda de IA
  ↓
Concentración de capacidad en HBM / SOCAMM (productos de alto valor)
  ↓
Reducción de la producción de DRAM / NAND de commodity
  ↓
Subida de precios de memoria de commodity
  ↓
Samsung Electronics experimenta una subida de precios en "toda la memoria"
  ↓
Los beneficios vienen no solo del HBM sino de toda la cartera
  ↓
Si esto es "alto margen estructural" y no "pico de ciclo"
  ↓
El PER debería ser 15× en lugar de 10×
  ↓
Precio objetivo ₩460.000
```

### 2.3 Puede ser cierto, puede ser falso

Para ser honestos — "esta vez es diferente" es la frase más peligrosa en la inversión. Los registros históricos están plagados de tesis de "esta vez es diferente" que terminaron repitiendo el mismo ciclo.

Para que Citi tenga razón, deben cumplirse cuatro condiciones:

* La demanda de IA no se desacelera en el 2S26
* El capex de Big Tech (Google, Amazon, Microsoft, Meta) se sostiene
* Samsung / SK hynix / Micron resisten el impulso histórico de sobreinvertir
* Los precios de la memoria siguen subiendo o al menos se mantienen estables hasta el 2T26

Si falla una sola, el "ciclo convencional" regresa y ₩460.000 se convierte en una historia lejana.

---

## 3. Los números del 1T de Samsung Electronics — por qué estas cifras son extraordinarias

### 3.1 Cifras clave

Samsung Electronics 1T26 (oficial):

| Concepto | Importe |
|---|---:|
| Ingresos consolidados | ₩133,9 billones |
| Beneficio operativo consolidado | **₩57,2 billones** |
| Ingresos DS (semiconductores) | ₩81,7 billones |
| Beneficio operativo DS | **₩53,7 billones** |
| Margen DS | **65,7%** |

Verificación: margen DS = 53,7 / 81,7 = 65,7% ✓

### 3.2 Por qué esto es extraordinario

**Margen operativo del 65,7%** en contexto:

```
Trayectoria del margen DS de Samsung Electronics:
2023: pérdidas (caída de precios de la memoria)
2024: recuperación, márgenes hasta el 20-30%
2025: márgenes hasta el 40-50%
1T26: 65,7% ← aquí

Comparativas:
Margen operativo de Apple: \~30%
Margen operativo de NVIDIA: \~60-65%
Margen operativo de Google: \~25-30%

Los semiconductores de Samsung Electronics ahora producen márgenes al nivel de NVIDIA.
```

Esto no son "buenos resultados" — es un número que obliga a preguntarse **"¿ha cambiado la estructura?"** En el ciclo convencional, un margen del 65% es el "pico del pico" y debe revertir a la media. Si la IA ha cambiado estructuralmente la forma de la demanda, este margen puede mantenerse.

[Por qué Corea, Parte 3](/post/samsung-sk-hynix-korea-ai-economy-rerating-2026-05-09/) enmarcó cómo el pool de beneficios combinado de Samsung / SK hynix está mejorando ahora la capacidad fiscal coreana, los ingresos de los hogares y los activos de pensiones a un nivel distinto al de ciclos anteriores.

### 3.3 Verificación aritmética del TP de ₩460.000

Comprobación mecánica de si ₩460.000 es siquiera plausible:

| Concepto | Valor |
|---|---:|
| Precio actual | ₩285.500 |
| TP Citi | **₩460.000** |
| Potencial alcista | **+61,1%** |
| Capitalización bursátil actual | \~₩1.669 billones |
| Capitalización implícita al TP | \~₩2.689 billones |
| Beneficio operativo 1T26 | ₩57,2 billones |
| Beneficio operativo anualizado simple | ₩228,8 billones (= 57,2 × 4) |
| Estimación post-impuestos (24%) | ₩173,9 billones |
| Cap. actual / post-impuestos | **\~9,6×** |
| Cap. objetivo / post-impuestos | **\~15,5×** |

Verificaciones:

* Potencial = 460.000 / 285.500 - 1 = 61,1% ✓
* Cap. TP = 1.669 × (460.000 / 285.500) = \~₩2.689 billones ✓
* Anualizado = 57,2 × 4 = 228,8 × 0,76 = ₩173,9 billones ✓

**Lectura**: al precio actual, Samsung Electronics cotiza a **\~9,6× los beneficios anualizados post-impuestos**. Para que funcione el TP de ₩460.000 de Citi, este múltiplo debe reclasificarse a **\~15,5×**. Pasar de 9,6× a 15,5× requiere un cambio de mentalidad del mercado: "esto no es un pico, es estructuralmente sostenible."

**En síntesis**: TP Citi ₩460.000 = **"resultados como los del 1T persistirán más tiempo"** + **"por lo tanto, el mercado debería pagar un múltiplo más alto."**

---

## 4. Los tres pilares del argumento de Citi

### 4.1 Pilar 1 — El crecimiento de tokens de IA impulsa la demanda de memoria

El volumen de tokens de IA se está disparando. Crecimiento de usuarios + contextos más largos + proliferación de agentes de IA = demanda de memoria en auge.

Esto se traduce en una **demanda de memoria más amplia que la demanda de GPU**. Las GPU calculan; la memoria almacena y transporta los datos que se calculan. A medida que la IA escala, se necesitan más GPU pero se necesita *mucha más* memoria. Como hacer una multiplicación de 1.000 dígitos — se necesita una calculadora (GPU), pero se necesita muchísimo más papel (memoria).

### 4.2 Pilar 2 — HBM4 / HBM4E / SOCAMM2 reestructuran la mezcla de productos

La "mezcla" de memoria que vende Samsung está cambiando. Antes dominaba el DRAM estándar; ahora el HBM y el SOCAMM — **productos caros y de alto margen** — representan una proporción creciente.

```
Niveles de precios de la memoria (aproximados):
DRAM DDR5 de commodity: pocos dólares por chip
HBM3E: decenas a cientos de dólares por stack
HBM4: por encima de HBM3E (Citi: +30% intertrimestral)

Si la misma fábrica produce HBM en lugar de DRAM de commodity:
→ los ingresos por oblea se multiplican
→ el margen sube adicionalmente
```

Samsung Electronics inició los envíos en producción masiva de HBM4 y SOCAMM2 en el 1T; el suministro de muestras de HBM4E comienza en el 2T. A medida que se expande la mezcla de alto valor, el margen total mejora.

### 4.3 Pilar 3 — Los precios de la memoria de commodity también suben

El pilar más importante. **No es solo el HBM el que se encarece — los precios del DRAM y NAND de commodity también suben.**

Por qué: Samsung / SK hynix / Micron fabrican HBM y DRAM de commodity en **líneas de fábrica compartidas**. A medida que explota la demanda de HBM y las fábricas reasignan capacidad a ese producto, la capacidad de producción de DRAM de commodity se reduce. La menor oferta sube el precio.

**Por qué esto importa para Samsung Electronics**: Samsung vende HBM, DRAM de commodity, NAND y eSSD (SSD de alto rendimiento para servidores). Cuando todos estos precios suben simultáneamente, la historia de beneficios no es la de una "monocultura de HBM" — es una **mejora de toda la cartera**. Esta es la tesis de Citi de "revisión al alza del ASP en toda la línea".

---

## 5. Efectos en nombres adyacentes — ¿es solo una historia de Samsung?

### 5.1 Orden de beneficiarios

El informe de Citi es específico sobre Samsung, pero una subida generalizada de precios de la memoria afecta a otros nombres.

| Orden | Nombre | Intensidad del vínculo | Razón |
|---|---|---|---|
| 1 | **Samsung Electronics** | Directo | Es el sujeto. Mejora de precios de memoria en toda la cartera |
| 2 | **SK hynix** | Directo | Número 1 en HBM. La subida de precios de memoria es un positivo sectorial |
| 3 | [Samsung Electro-Mechanics](/post/samsung-electro-mechanics-ai-infrastructure-rerating-2026-04-21/) | Indirecto | Beneficiario de sustratos y MLCC para servidores de IA. Este informe es una tesis sobre precios de memoria, no sobre sustratos |
| 4 | [Daeduck Electronics](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) | Indirecto | Demanda de sustratos para IA. Vínculo débil con los precios de Samsung específicamente |
| 5 | Pamicell | Indirecto débil | El sentimiento positivo en infraestructura de IA ayuda, pero este informe por sí solo no es evidencia suficiente |

**Lectura**: Samsung Electronics > SK hynix > Samsung Electro-Mechanics > sustratos y materiales de segundo nivel. La relación directa disminuye a medida que se baja en la cadena. El reflejo de "suben los precios de la memoria → compra todos los nombres de IA" es un salto lógico.

---

## 6. Qué invalidaría la tesis de Citi

El análisis debe ser falsificable. Si la tesis del "re-rating estructural" se rompe, estas son las señales que aparecerían primero:

```
Señales que dañan la tesis:
1. Precios de memoria en el 2T estables o a la baja → señal de pico de ciclo
2. Cualificaciones de clientes para HBM4E retrasadas → la tesis de re-rating de Samsung se debilita
3. Big Tech anuncia recortes de capex en IA → daño a la forma de la demanda
4. Margen DS cae por debajo del 50% → el 1T confirmado como pico
5. Adopción de SOCAMM2 limitada → la tesis de mejora de mezcla de productos se rompe
```

Por el contrario, lo siguiente refuerza el caso:

```
Señales que confirman la tesis:
1. Los precios de DRAM/NAND suben más en el 2T intertrimestral
2. Se anuncian cualificaciones de clientes para HBM4E
3. Las previsiones de capex en IA de Big Tech se revisan al alza
4. El margen DS se mantiene por encima del 55%
5. La adopción de SOCAMM2 se expande — vínculo confirmado con la plataforma de próxima generación de NVIDIA
```

---

## 7. Calendario clave — qué verificar y cuándo

| Ventana | Evento | Por qué importa |
|---|---|---|
| A lo largo del 2T | Trayectoria de precios de DRAM / NAND | Pone a prueba la lógica central de Citi. ¿Siguen subiendo los precios? |
| A lo largo del 2T | Suministro de muestras de HBM4E + cualificación de clientes | Confirmación de la competitividad de Samsung en HBM |
| Julio | Resultados del 2T de Samsung Electronics | ¿El margen DS se mantiene por encima del 55%? |
| 2S | Noticias sobre la plataforma de próxima generación de NVIDIA | Verificación de la demanda de SOCAMM2 |
| 2S | Informes adicionales de brókers extranjeros | ¿El consenso revisa al alza de forma generalizada? |

---

## 8. Conclusión

Citi elevó el precio objetivo de Samsung Electronics a ₩460.000. El fondo del informe no es "Samsung es una buena acción". Es que **la creencia de 30 años — 'los precios de la memoria suben y caen' — puede estar equivocada esta vez**, porque la IA ha remodelado la demanda de memoria y el HBM está absorbiendo capacidad de fabricación hasta el punto de que los precios de la memoria de commodity también suben.

Beneficio operativo del 1T de ₩57,2 billones con un margen DS del 65,7% — numéricamente no es un negocio de semiconductores, es una plataforma monopolística. Para que ₩460.000 funcione, este perfil debe sostenerse en lugar de ser un pico.

El TP ₩460.000 de Citi exige que "esta vez sea diferente" sea realmente verdad. La respuesta llega en el 2T — en la trayectoria de precios de DRAM / NAND y en las cualificaciones de clientes para HBM4E. La capitalización bursátil de Samsung Electronics del 11 de mayo de \~₩1.669 billones (\~1,2 billones de dólares) indica que el mercado ya ha empezado a hacerse esta pregunta; cómo se resuelva marcará la dirección del KOSPI y del clúster de semiconductores en los próximos 6-12 meses.

---

## Preguntas frecuentes

**P: ¿Cómo llegó Citi a ₩460.000?**
R: El modelo exacto no estaba directamente accesible — el análisis se basa en capturas de pantalla del informe. Verificable mecánicamente: beneficio operativo 1T26 de ₩57,2 billones × 4 = ₩228,8 billones anualizados, × 0,76 (post-impuestos) = ₩173,9 billones, × \~15,5× múltiplo de beneficios. El mercado asigna actualmente \~9,6×, por lo que el TP implica un re-rating del múltiplo de \~60%.

**P: ¿Ha terminado realmente el ciclo de memoria?**
R: No puede confirmarse. "Esta vez es diferente" es la frase más peligrosa en la inversión. Para que Citi tenga razón, la demanda de IA no debe desacelerarse en el 2S26, el capex de Big Tech debe mantenerse y los tres fabricantes de memoria deben resistir la sobreinversión. Si falla cualquiera de estas condiciones, el ciclo convencional regresa.

**P: ¿Por qué suben juntos los precios del HBM y del DRAM de commodity?**
R: Por la fabricación en las mismas plantas. La concentración de HBM impulsada por la IA reduce la capacidad de producción de DRAM de commodity, elevando los precios. Samsung vende HBM + DRAM de commodity + NAND + eSSD, por lo que la mejora de precios en toda la cartera acelera los beneficios totales.

**P: Samsung Electronics vs. SK hynix — ¿cuál es mejor?**
R: La exposición pura al HBM es más directa en SK hynix (principal proveedor de NVIDIA). Samsung Electronics es un gran valor multisegmento (memoria + foundry + smartphones). Convicción exclusiva en HBM → SK hynix. Cartera de memoria + opción en foundry → Samsung Electronics. El [Centro de inversión HBM / KOSPI](/page/korea-semiconductor-hbm-kospi-hub/) tiene la comparativa completa.

**P: Con una capitalización de \~1,2 billones de dólares, ¿no está ya cara?**
R: La capitalización absoluta es grande. Por múltiplo de beneficios (\~9,6× PER actual), sigue por debajo de sus pares globales (NVIDIA \~35×, TSMC \~25×). "Cara" depende de la vara con la que se mida.

**P: ¿Cuándo se verifica más rápido la tesis de Citi?**
R: Dentro del 2T, dos confirmaciones simultáneas supondrían una validación sólida — (1) precios de DRAM/NAND subiendo más intertrimestral, y (2) anuncio de cualificación de clientes para HBM4E. La publicación de resultados del 2T en julio establece entonces una segunda verificación: ¿el margen DS se mantiene por encima del 55%?

---

*Este artículo tiene fines únicamente de investigación e información y no constituye asesoramiento de inversión. Los detalles del precio objetivo de Citi se basan en capturas de pantalla del informe facilitadas por el usuario; el modelo completo de 17 páginas, las estimaciones de BPA y la valoración detallada no han sido verificados directamente. Las cifras del 1T26 de Samsung Electronics provienen de comunicaciones oficiales. La verificación aritmética del precio objetivo utiliza supuestos simplificados de tipo impositivo y múltiplo de beneficios, y puede diferir del modelo real de Citi. Las cualificaciones de clientes para HBM4E y los volúmenes de envío de SOCAMM2 permanecen sin confirmar. "Esta vez es diferente" históricamente ha sido cierto en ocasiones, pero erróneo con mayor frecuencia. El análisis puede estar equivocado. Datos a: 11 de mayo de 2026, hora de Corea.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
