---
title: "Cadena de valor óptica y CPO en Corea — Solo OE Solutions (138080.KQ) está verdaderamente cerca del CPO; seis de los siete valores acumulan +300–900% en el año con beneficios que no han acompañado"
slug: korea-optical-cpo-value-chain-seven-companies-2026-05-09
date: 2026-05-09T20:00:00+09:00
description: "El próximo cuello de botella en los centros de datos de IA se está desplazando hacia la interconexión óptica. Decenas de miles de GPUs comunicándose entre sí requieren módulos ópticos de 800G y 1.6T, y la Óptica Co-Empaquetada (CPO) —que sitúa el motor óptico junto al ASIC del switch— emerge como la respuesta arquitectónica. Al mapear los siete valores coreanos cotizados —OE Solutions, Optocore, Daehan Optical Communications, BWE, WooriRo, Lycom, Coset— solo OE Solutions está genuinamente cerca del CPO gracias a su fuente láser externa ELSFP y su chip láser EML 100G desarrollado internamente. Los otros seis son beneficiarios indirectos o apuestas temáticas. Y seis de los siete acumulan entre +300% y +905% en el año con pérdidas operativas aún en vigor. El precio se movió antes que los beneficios. La lectura accionable: OE Solutions en lista de seguimiento (con espera de retroceso o confirmación de muestras ELSFP para clientes en 3T26), y el resto hasta que se disipe el sobrecalentamiento."
categories: ["Sector-Deep-Dive", "Korea Market", "Semiconductors"]
tags:
  - "interconexión óptica"
  - "CPO"
  - "óptica co-empaquetada"
  - "OE Solutions"
  - "138080"
  - "Optocore"
  - "Daehan Optical"
  - "BWE"
  - "WooriRo"
  - "Lycom"
  - "Coset"
  - "centro de datos IA"
  - "ELSFP"
  - "fuente láser externa"
  - "EML"
  - "pequeña capitalización coreana"
  - "transceptor óptico"
  - "800G"
  - "1.6T"
---

> 🔗 **Relacionado**: [Centro de PCB e Interposers IA](/page/korea-ai-pcb-substrate-hub/) · [Ecosistema PCB IA en Corea — 10 Empresas](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) · [Tesis PCB IA e Interposers — La BOM del Sistema como Cuello de Botella Común](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) · [Haesung DS — De Lead Frame a Segunda Fuente de Disipadores Térmicos para IA](/post/haesung-ds-leadframe-ai-heat-spreader-second-source-2026-05-07/)

*El [artículo sobre la tesis de interposers](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) planteaba un argumento de "denominador común de la BOM del sistema": la demanda de IA no se compra chip a chip, sino rack a rack, y la demanda de interposers abarca toda la BOM. La misma lógica se extiende ahora hacia la interconexión óptica —y las exposiciones cotizadas coreanas son considerablemente menos maduras. Siete valores se sitúan en el eje óptico / CPO. Solo uno (OE Solutions, 138080.KQ) está genuinamente cerca de la nueva arquitectura CPO gracias a su **fuente láser externa ELSFP**. Los otros seis son beneficiarios indirectos o apuestas temáticas. Y seis de los siete acumulan entre +300% y +905% en el año frente a pérdidas operativas o contratos con clientes no verificados. Este es un mercado de "tesis técnica válida al precio equivocado" —exactamente el tipo de escenario donde mapear la cadena de valor por **distancia al verdadero cuello de botella** resulta más útil que comprar los valores que más han subido.*

---

## Resumen ejecutivo

* **Entre los valores coreanos cotizados, solo OE Solutions (138080.KQ) está verdaderamente cerca del CPO.** Ha revelado un producto de **fuente láser externa ELSFP** (compatible con CPO, estándar OIF, 8 canales, 23dBm/200mW por canal, con refrigeración TEC, muestras para clientes previstas en 3T26) y ha desarrollado un **chip láser EML 100G**, el primero de fabricación nacional. Los otros seis no están en la ruta central del CPO. OE Solutions tampoco figura aún en la lista pública de socios CPO de Nvidia ni de Broadcom.
* **Optocore tiene contratos reales de transceptores ópticos para centros de datos de IA** por un importe total de \~₩16.700M — pero el cliente no ha sido revelado y la cotización está suspendida por una auditoría de empresa en funcionamiento en 1T26. **No es invertible.**
* **Daehan Optical Communications acumula +905% en el año sobre una narrativa de "más fibra óptica para IA" — no es una apuesta CPO en absoluto.** Es una empresa de integración vertical de preformas a fibra, no un proveedor de motores ópticos ni láseres. La Bolsa de Corea (KRX) ya la ha señalado para escalar la advertencia de inversión.
* **Seis de los siete valores acumulan +300% o más en el año frente a cuentas de resultados aún deficitarias.** Daehan +905%, BWE +778%, WooriRo +616%, OE Solutions +307%. El precio se adelantó con mucho a los beneficios. Comprar ahora es apostar a que **el precio alcance sus propias expectativas futuras**, no a que la tecnología sea correcta.
* **La lectura limpia para el asignador es OE Solutions en lista de seguimiento con espera, y los otros seis en pausa.** OE Solutions cotiza a más de 100× el beneficio operativo estimado para 2026 al precio actual — la entrada óptima está en el **retroceso a 47.000–50.000 wones** o tras la **confirmación de muestras ELSFP para clientes en 3T**, no persiguiendo el precio.

---

## 1. Por qué la óptica es el próximo cuello de botella en los centros de datos de IA

### 1.1 La misma lógica que los interposers, en la capa de red

La tesis de los interposers era un argumento de "denominador común": cada chip adicional en un rack de IA —GPU, CPU, DPU, NIC, ASIC de switch, módulo de memoria— genera demanda de interposer. La interconexión óptica responde a la misma lógica en la capa de red. Decenas de miles de GPUs en un único clúster de entrenamiento requieren un ancho de banda de red que la señalización eléctrica no puede suministrar con una potencia aceptable. Por eso el enlace se vuelve óptico.

```
Cadena de demanda óptica en centros de datos de IA:

Clúster de decenas de miles de GPUs
   ↓
ASICs de switch (conectividad de red)
   ↓
Transceptores ópticos 800G → 1.6T (eléctrico → óptico → eléctrico)
   ↓
Fibra óptica y planta de cable (el camino que recorre la luz)
   ↓
Componentes: láseres, fotodetectores, amplificadores ópticos, fibra de baja pérdida
```

Broadcom ha indicado que los plazos de entrega de PCBs para transceptores ópticos se han extendido de 6 semanas a 6 meses — una señal temprana de que los componentes ópticos se están convirtiendo en la capa con restricciones.

### 1.2 Qué es realmente el CPO

La arquitectura tradicional utilizaba **módulos ópticos enchufables** en el panel frontal del chasis del switch. Fáciles de sustituir, pero con alto consumo energético, y la señal eléctrica recorre un largo camino desde el ASIC del switch hasta el panel frontal.

**La Óptica Co-Empaquetada (CPO)** es una arquitectura diferente: el motor óptico se sitúa **justo al lado del ASIC del switch en el mismo substrato de encapsulado**. La distancia de recorrido de la señal eléctrica se contrae drásticamente. La potencia consumida por bit cae de forma pronunciada.

* Nvidia ha declarado que su switch basado en CPO es **5× más eficiente energéticamente** y ofrece **10× más fiabilidad de red** que los equivalentes enchufables.
* Broadcom ha presentado un switch Ethernet CPO de 51,2 Tbps con una reducción declarada de **>70% en el consumo energético del enlace óptico**.

### 1.3 Por qué importa la "fuente láser externa" dentro del CPO

El problema difícil dentro del CPO: **los láseres son sensibles a la temperatura, y los ASICs de switch son calientes.** Colocar el láser dentro del encapsulado, junto a un ASIC caliente, acorta la vida útil del láser y degrada su rendimiento.

La solución: **separar el láser del encapsulado.** Sacar el láser al panel frontal, introducir únicamente la luz dentro del encapsulado mediante fibra, y mantener el cuerpo del láser aislado térmicamente.

El factor de forma estándar para ese láser externo es el **ELSFP — External Laser Small Form-factor Pluggable**, definido por el OIF (Optical Internetworking Forum). Cuando el CPO escale, el ELSFP se convertirá en una categoría de componente central.

```
Posición del ELSFP dentro del CPO:

ASIC del switch (caliente)
   ↓ (luz entrante)
Motor óptico (junto al ASIC, luz ↔ eléctrico)
   ↑ (luz saliente)
Fuente láser externa ELSFP (panel frontal, aislada térmicamente)
   ↑
Láser (alta potencia, estable)
```

**El ELSFP de OE Solutions es exactamente este componente.** Es la única empresa coreana cotizada con este producto específico revelado públicamente.

---

## 2. Los siete valores coreanos — separando "exposición CPO real" de "temática óptica IA"

| # | Empresa (ticker) | Posición en la cadena de valor | Relevancia óptica IA | Rentabilidad YTD | Lectura |
|---:|---|---|---|---:|---|
| 1 | **OE Solutions (138080.KQ)** | CPO ELSFP / transceptor óptico / chip láser | **Más directa** | +307% | Lista de seguimiento principal |
| 2 | Optocore | Transceptores para centros de datos IA | Evidencia contractual; suspendida | +106% | No invertible |
| 3 | Daehan Optical Communications | Fibra y cable (materiales aguas arriba) | Beneficiario indirecto, no CPO | **+905%** | Sobrecalentada; advertencia KRX escalando |
| 4 | BWE | Gama de transceptores 800G / 1.6T | Producto revelado; cliente sin confirmar | **+778%** | Temática de alta volatilidad |
| 5 | WooriRo | Fotodetectores (componente central de transceptor) | Fase de desarrollo tecnológico | **+616%** | Opción de componente |
| 6 | Lycom | Amplificadores ópticos / conectividad DC | Beneficiario indirecto | +98% | Pendiente de catalizador |
| 7 | Coset | Componentes ópticos (TOSA/ROSA) | Opción de pequeña capitalización | -5% | Liquidez insuficiente |

### 2.1 Lo que muestra esta tabla

**Primero, la exposición CPO real y la temática óptica IA son objetos distintos.** Solo OE Solutions tiene el producto de láser externo ELSFP. El resto son transceptores (Optocore, BWE), fibra (Daehan Optical), fotodetectores (WooriRo), amplificadores (Lycom) o componentes genéricos (Coset). Todos se sitúan en algún punto de la cadena de valor óptica de IA más amplia, pero "proveedor CPO central" y "nombre óptico temático" no merecen el mismo múltiplo.

**Segundo, seis de los siete acumulan varios cientos de puntos porcentuales en el año frente a pérdidas operativas o contratos con clientes no verificados.** Daehan +905%, BWE +778%, WooriRo +616%, OE Solutions +307%. El precio se movió antes que los beneficios. Comprar ahora no es "¿es correcta la tecnología?" — es "¿ya se ha excedido el precio en lo que los beneficios pueden llegar a entregar?"

---

## 3. OE Solutions — el único valor verdaderamente cerca del CPO

### 3.1 Estructura del negocio

OE Solutions fabrica transceptores ópticos y chips láser. Fundada en 2003 por antiguos de Bell Labs y Samsung Electronics con experiencia en fabricación óptica en volumen. Presencia internacional: Nueva Jersey y California (EE. UU.), Países Bajos, Japón.

Capacidad central: **integración vertical desde el chip láser → sub-ensamblaje óptico → transceptor terminado.** En un transceptor óptico, el láser es el "motor" — la estabilidad de la potencia óptica, la gestión térmica y la vida útil determinan el producto. OE Solutions desarrolla el chip láser internamente.

### 3.2 Por qué el ELSFP es el producto clave

Presentado en OFC 2026 (marzo):

```
ELSFP compatible con CPO de OE Solutions:

- 23 dBm / 200 mW de potencia óptica por canal
- TEC (refrigerador termoeléctrico) integrado → estabilidad de longitud de onda + vida útil del láser
- Configuración de 8 canales
- Muestras para clientes previstas desde 3T26
```

Este producto aborda directamente el problema de aislamiento térmico del CPO — sacando el láser de un ASIC de switch caliente y situándolo en el panel frontal. El OIF define el estándar, y OE Solutions es el único valor coreano cotizado con el producto revelado públicamente.

OE Solutions también presentó en AI EXPO 2026 el primer **chip láser EML de clase 100G** desarrollado en Corea, la fuente de luz fundamental para los transceptores 800G/1.6T.

### 3.3 Los beneficios no han alcanzado a la tecnología

Esta es la brecha que define la operación.

| Métrica | 2024 | 2025 | 2026E |
|---|---:|---:|---:|
| Ingresos (miles de millones KRW) | 32,0 | 57,4 | 81,6–83,5 |
| Beneficio operativo (miles de millones KRW) | -30,4 | -16,0 | 6,1–6,5 |
| Margen operativo | -95% | -28% | 7–8% |
| Mix de ingresos datacom | — | **2%** | aún bajo |

Los ingresos de 2025 se recuperaron un +79% interanual pero siguieron en pérdidas. El 2026E pivota a beneficios (₩6.100–6.500M de BO), pero la capitalización de mercado es de \~₩660.000M. Comprobación rápida:

* Valor empresa ≈ capitalización + deuda neta = 660 + 20 = \~₩680.000M
* Sobre el BO estimado para 2026 de ₩6.500M → **VE/EBIT ≈ 105×**

**Al precio actual se pagan \~105× el BO estimado para 2026.** No es una valoración de "giro a beneficios en 2026". Es una valoración de "inflexión en ingresos ópticos de IA en 2027–2028".

### 3.4 El mix de ingresos aún no es céntrico en IA

Mix de ingresos 2025 (estimaciones de casas de análisis):

| Segmento | Participación | Lectura |
|---|---:|---|
| Wireless | 48% | Núcleo heredado; recuperándose tras la ralentización post-5G |
| FTTH / MSO (acceso cableado) | 23% | Ligado al gasto en acceso cableado de Japón / EE. UU. |
| Larga distancia (Telecom) | 21% | Transceptores 100G/400G de larga distancia |
| **Datacom** | **2%** | **La historia IA aún no está en los ingresos** |
| Chips láser | 6% | Opción tecnológica, escala aún limitada |

Calificar esto de "empresa CPO de centros de datos de IA" va más allá de lo que muestra la cuenta de resultados actual. El encuadre preciso es **"recuperación de equipos de telecomunicaciones con una opción de compra CPO adjunta."**

### 3.5 Entonces, ¿por qué ocupa el puesto nº 1?

```
Lo que solo OE Solutions tiene frente a los otros seis:

1. Producto ELSFP para CPO revelado — único en el grupo
2. Chip láser EML 100G de fabricación propia — único en el grupo
3. Integración vertical: chip láser → sub-ensamblaje → módulo — la más profunda del grupo
4. Historial con clientes globales de equipos de telecomunicaciones (Cisco, Nokia, Ciena, etc.)
5. Presencia operativa internacional (EE. UU. / Países Bajos / Japón)
```

La nota de precaución: la lista pública de socios CPO de Nvidia (TSMC, Coherent, Corning, Foxconn, Lumentum, Senko, Sumitomo, etc.) **no incluye a OE Solutions**. El estado preciso es "la tecnología existe, pero la inclusión en el ecosistema aún no está confirmada."

### 3.6 Variables a seguir

* **3T26**: ¿Se enviaron las muestras ELSFP para clientes según el calendario previsto?
* **4T26 → 2027**: ¿Avanza la cualificación? ¿Se mencionan nombres de clientes?
* **Mix datacom**: ¿Sube de forma material por encima del 2%?
* **Margen bruto**: ¿Recuperación desde el 10,5% de 2025 hacia el 20%+?
* **Beneficio operativo**: ¿Se materializó realmente el giro a beneficios en el ejercicio 2026?

---

## 4. Los otros seis valores

### 4.1 Daehan Optical Communications — +905% en el año, advertencia KRX escalando

Daehan **no es una empresa CPO.** Es un fabricante de integración vertical de preforma → fibra → cable — materiales aguas arriba, no motores ópticos. Los centros de datos de IA sí consumen más fibra de alta densidad, pero eso es una tesis de beneficiario indirecto, no de núcleo CPO.

La acción del precio es el problema:

```
Daehan Optical Communications:
YTD: +905%
3 meses: +610%
1 semana: +47%
KRX: designada el 2026-05-08 como valor de precaución inversora; advertencia escalando
```

El flujo extranjero ha sido fuerte, pero la capa regulatoria ya está señalando el movimiento. **Comprar aquí un valor que ha multiplicado por 10 en el año no es una apuesta sobre la demanda de fibra — es una apuesta sobre si el precio puede extenderse aún más desde una base 10×.**

### 4.2 BWE — +778%, -36% desde máximos

BWE presentó una gama de transceptores 800G / 1.6T en AI EXPO. **Producto revelado ≠ cliente cualificado.** No se ha confirmado ningún nombre de cliente central. Sube un +778% en el año, pero cae un -36% desde máximos (8.100 → 5.200 wones). Actualmente en zona de digestión.

### 4.3 WooriRo — +616%, subida liderada por minoristas

Ha revelado tecnología de fotodetector a 200 Gbps — un potencial componente central para transceptores 800G / 1.6T. Aún en fase de desarrollo; cualificación con clientes globales sin verificar. La compra neta acumulada se inclina hacia el minorista. Es una operación de momentum temático, no acumulación institucional.

### 4.4 Lycom — +98%, volumen muerto

Amplificadores ópticos para conectividad intra e inter centros de datos. Informes de crecimiento de pedidos en el exterior. Más cercana a la periferia óptica de IA que al núcleo CPO. Sube un +98% en el año (la menos sobrecalentada de las siete), pero el volumen se sitúa en el 34% de la media de los 3 últimos meses — sin un nuevo catalizador, se mueve de lado.

### 4.5 Optocore — cotización suspendida, no invertible

Los contratos de transceptores ópticos para centros de datos de IA por un importe agregado de \~₩16.700M son reales. Pero la cotización fue suspendida en marzo de 2026 por una cualificación de auditoría de empresa en funcionamiento, con posible exclusión de bolsa. **No es posible actuar sobre este valor en el mercado de renta variable pública hoy.**

### 4.6 Coset — cotizada en KONEX, liquidez insuficiente

Fabricante de componentes ópticos TOSA/ROSA de 400G+. Cotizada en KONEX (el mercado de valores más pequeño de Corea); la rotación es demasiado escasa para una asignación normal. Solo lista de seguimiento.

---

## 5. El sobrecalentamiento, en números

### 5.1 Rentabilidad acumulada en el año

| Valor | YTD | 3 meses | 1 semana | Estado |
|---|---:|---:|---:|---|
| Daehan Optical | **+905%** | +610% | +47% | Advertencia KRX pendiente |
| BWE | **+778%** | +321% | +2% | -36% desde máximos, desacelerando |
| WooriRo | **+616%** | +513% | +7% | Subida liderada por minoristas |
| OE Solutions | **+307%** | +232% | +38% | Reentrada institucional; aún cara |
| Optocore | +106% | +14% | — | Suspendida |
| Lycom | +98% | +114% | +2% | Sin volumen |
| Coset | -5% | +11% | -13% | Liquidez insuficiente |

### 5.2 La lectura en una sola línea

**Cuatro de los siete acumulan más del 300% en el año sin apoyo de beneficios en la práctica.** OE Solutions registró aún una pérdida operativa de ₩16.000M en 2025. Daehan es rentable, pero no lo suficiente como para justificar una subida 10× en el año. El precio se ha adelantado considerablemente a los fundamentales.

En este entorno, la pregunta decisiva no es "¿es correcta la tecnología?" — sino **"¿ya ha descontado el precio más de lo que los beneficios podrán jamás entregar?"**

---

## 6. Valoración de OE Solutions — qué se compra realmente al precio actual

### 6.1 Lo que requiere el precio actual

Se asume capitalización de mercado de \~₩660.000M, deuda neta de \~₩20.000M, VE de \~₩680.000M.

Con un múltiplo de salida VE/EBIT de 30×, el BO necesario para justificar cada nivel de precio:

| Precio | BO requerido (a 30× VE/EBIT) | Vs. BO estimado 2026 |
|---:|---:|---|
| 53.300 (actual) | **\~₩22.700M** | 3,5× el consenso |
| 60.000 (TP casas de análisis) | \~₩25.400M | 3,9× el consenso |
| 70.000 | \~₩29.500M | 4,5× el consenso |
| 100.000 | \~₩41.900M | 6,4× el consenso |

**Incluso el precio actual requiere un BO de \~3,5× el consenso para 2026** para reconciliarse con un múltiplo de 30×. Eso no es un número de 2026. Es la inflexión de ingresos ópticos de IA de 2027–2028.

### 6.2 Bandas de valor razonable por escenario

| Escenario | Supuesto clave | Beneficio operativo | Banda de valor razonable (KRW) |
|---|---|---:|---:|
| Bajista | Recuperación telecom retrasada, muestras ELSFP se retrasan | ₩0–5.000M | 25.000–35.000 |
| Base | Giro a beneficios en 2026, ELSFP solo en fase de muestras | ₩6.100–6.500M | 30.000–45.000 |
| Alcista 1 | Rampa de ingresos datacom en 2027–2028 | ₩20.000–25.000M | 47.000–59.000 |
| Alcista 2 | Adopción de clientes ELSFP, margen bruto >15% | ₩30.000–40.000M | 71.000–111.000 |
| Hiper-alcista | Inclusión directa en cadena de suministro CPO global de IA | ₩40.000M+ | 110.000+ |

**El cierre en 53.300 se sitúa entre Alcista 1 y Alcista 2** — ya descontando un valor de opción CPO significativo por encima de la base de recuperación en telecomunicaciones. Si el compromiso con clientes para el ELSFP en 3T se materializa, el precio se extiende. Si no, el nivel queda expuesto.

---

## 7. Marco de posicionamiento — cómo gestionar los siete valores

| # | Nombre | Lectura | Razonamiento |
|---:|---|---|---|
| 1 | **OE Solutions** | **Lista de seguimiento principal, esperar** | Mayor pureza CPO; precio ya elevado. Esperar retroceso a 47.000–50.000 o confirmación ELSFP en 3T |
| 2 | Lycom | Pendiente de catalizador | Menos sobrecalentada, pero sin volumen — necesita un pedido o revelación de cliente |
| 3 | Daehan Optical | **No perseguir** | +905% con advertencia KRX pendiente. Los tenedores recortan; nuevas entradas inapropiadas |
| 4 | BWE | Esperar ruptura al alza | -36% desde máximos; pausa hasta confirmación de cliente |
| 5 | WooriRo | Sin nueva entrada | Liderada por minoristas; tecnología sin verificar |
| 6 | Optocore | **No invertible** | Cotización suspendida, riesgo de exclusión de bolsa |
| 7 | Coset | Solo observación | KONEX, liquidez insuficiente |

### 7.1 Condiciones de entrada en OE Solutions

**Precio**: Primer interés en la zona 47.000–50.000. Segundo interés en 43.000–45.000 (retroceso más profundo).

**Confirmación de beneficios**:

* Impresión de beneficio operativo en 2T o 3T (confirmación del giro a beneficios)
* Comunicación de envío de muestras ELSFP a clientes en 3T
* Mix de ingresos datacom en ascenso

**Confirmación de flujos**:

* Compra neta concurrente de extranjeros e institucionales ≥ 3 sesiones
* Liquidación estable por encima del máximo de 52 semanas (57.900)

### 7.2 Condiciones de invalidación

* El ejercicio 2026 no gira a beneficios
* El calendario de muestras ELSFP en 3T se retrasa
* No se menciona ninguna cualificación de clientes hasta 4T
* El mix datacom se mantiene por debajo del 10%
* El margen bruto no se recupera por encima del 20%

---

## 8. Tres cosas que conviene decir directamente

### 8.1 La mayoría de los siete son valores temáticos

Con franqueza: entre los siete, casi ninguno tiene un caso validado por beneficios. OE Solutions registró pérdidas operativas en 2025, y el resto está en peor posición. **Los valores que suben varios cientos de puntos porcentuales sin beneficio operativo cotizan sobre expectativas, no sobre resultados entregados.** Cuando la expectativa no se convierte en beneficios, el precio retrocede.

### 8.2 Ninguna pequeña capitalización coreana figura en la lista de socios CPO de Nvidia

Los socios CPO nombrados por Nvidia: TSMC, Coherent, Corning, Foxconn, Lumentum, Senko, Sumitomo. Ninguna pequeña capitalización coreana. Afirmar que "las empresas coreanas forman parte de la cadena de suministro CPO" es excesivo. OE Solutions es la más cercana, pero sigue siendo un **candidato**, no una inclusión confirmada.

### 8.3 La inversión en óptica tiene plazos largos

Los ciclos de cualificación de transceptores ópticos funcionan como los semiconductores: muestra → cualificación → adopción en diseño → pedido en volumen → reconocimiento de ingresos puede tardar 1–2 años. Incluso si las muestras de 3T26 se envían a tiempo, los ingresos en volumen podrían llegar en 2027–2028. Si el precio de la acción esperará pacientemente durante ese período es algo que no puede saberse de antemano.

---

## 9. Conexión con la serie de interposers

Este artículo se inscribe en el mismo marco que la [serie de interposers](/page/korea-ai-pcb-substrate-hub/). La [tesis de la BOM del sistema](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) planteaba el argumento estructural de que **la demanda de IA se compra como sistemas, no como chips.** Ese sistema contiene capas de interposer, óptica, térmica y alimentación — todas ellas bajo presión.

```
Cuellos de botella comunes del sistema de IA:

Interposers (FC-BGA, MLB, CCL) — cubiertos en los artículos de 5 y 10 empresas
Óptica (módulos 800G/1.6T, CPO ELSFP, fibra) — este artículo
Térmica (disipadores, heat slugs) — cubierto en el artículo de Haesung DS
Alimentación (transformadores, semiconductores de potencia) — candidato a artículo futuro
Refrigeración (inmersión, disipadores de calor) — candidato a artículo futuro
```

El [marco de 10 empresas](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/) argumentaba que la tesis de escasez de interposers se canaliza de vuelta hacia los materiales aguas arriba. La misma distinción aplica aquí — fibra y cable (Daehan Optical) es un beneficiario indirecto, mientras que el láser / fuente láser externa (OE Solutions) se sitúa más cerca del verdadero cuello de botella CPO.

La diferencia crucial: **el grupo de interposers tiene beneficios que se acercan al precio. El grupo óptico no.** Los interposers son "selecciona los nombres validados que cotizan a precios aceptables." La óptica es **"separa señal de ruido dentro de un rally pre-beneficios sobrecalentado."**

[Haesung DS](/post/haesung-ds-leadframe-ai-heat-spreader-second-source-2026-05-07/) ofrece el mismo contraste en el eje térmico: allí, la opcionalidad del disipador de calor para IA descansa sobre una base real de LF automotriz y substrato DDR. Aquí, cinco de los siete valores ópticos carecen de una base comparable — la opcionalidad es esencialmente toda la tesis.

---

## 10. Conclusión

Que la interconexión óptica sea el próximo cuello de botella en los centros de datos de IA es estructuralmente correcto. Decenas de miles de GPUs necesitan óptica 800G / 1.6T, y el CPO es la respuesta arquitectónica creíble. Corea tiene siete exposiciones cotizadas.

Pero solo **uno** de los siete está genuinamente cerca del núcleo CPO. OE Solutions tiene la fuente láser externa ELSFP y el chip láser EML 100G de fabricación propia. Los otros seis son beneficiarios indirectos o apuestas temáticas. Y seis de los siete acumulan entre +300% y +905% en el año — Daehan Optical con una advertencia de inversión KRX escalando encima.

OE Solutions cotiza en sí misma a \~105× el BO estimado para 2026. El mix datacom es del 2%. 2025 fue un año con pérdidas. **Al precio actual se apuesta por la adopción CPO por parte de clientes en 2027–2028, no por los beneficios de 2026.** La entrada limpia aguarda la confirmación de muestras ELSFP para clientes en 3T26 o un retroceso a 47.000–50.000 wones — observación, no persecución.

"La tecnología es correcta" y "el precio es correcto hoy" son preguntas distintas. La óptica probablemente demostrará ser un cuello de botella real del sistema de IA. Pero si el precio ya se ha adelantado varios cientos de puntos porcentuales, el retorno del asignador lo determina el precio de compra, no si la tecnología resultó ser correcta.

---

## Preguntas frecuentes

**P: ¿Qué es el CPO en una frase?**
R: Una nueva arquitectura de encapsulado que sitúa el motor óptico **directamente junto al ASIC del switch** en el mismo encapsulado, acortando drásticamente el recorrido de la señal eléctrica y reduciendo la potencia consumida por bit. Reemplaza a la óptica enchufable de panel frontal en los switches de centros de datos de IA de gama alta.

**P: ¿Qué valor coreano cotizado es genuinamente una empresa CPO?**
R: **OE Solutions (138080.KQ)** es el único con un producto relevante para CPO revelado públicamente — su fuente láser externa ELSFP — además de un chip láser EML 100G de fabricación propia. **Aún no** figura en la lista pública de socios CPO de Nvidia ni de Broadcom, por lo que el estado preciso es "candidato más próximo", no "inclusión confirmada."

**P: ¿No es Daehan Optical Communications una apuesta CPO?**
R: No. Daehan es un fabricante de integración vertical de fibra y cable óptico (preforma → fibra → cable). Los centros de datos de IA sí consumen más fibra de alta densidad — esa es una tesis de beneficiario indirecto — pero Daehan no produce componentes CPO centrales (motores ópticos, láseres, circuitos integrados fotónicos).

**P: ¿Debo perseguir OE Solutions a 53.300?**
R: No para una posición completa. El precio actual es de \~105× el BO estimado para 2026. Las entradas asimétricas son: (a) un retroceso a la zona 47.000–50.000, o (b) confirmación de que las muestras ELSFP para clientes en 3T26 se han enviado según el calendario. Perseguir aquí es, como máximo, un piloto de 30–50 pb.

**P: ¿Qué valor presenta el mayor riesgo en el grupo?**
R: Optocore **no es invertible** hoy (cotización suspendida por auditoría de empresa en funcionamiento). Daehan Optical acumula +905% en el año con advertencia KRX escalando. BWE y WooriRo han subido varios cientos de puntos porcentuales sobre bases de clientes no verificadas. Ninguno de ellos es apropiado como nueva entrada.

**P: ¿Cómo se compara esto con los valores coreanos de interposers para IA?**
R: El grupo de interposers tiene **beneficios que se acercan al precio**, por lo que la operación accionable consiste en seleccionar nombres validados a múltiplos aceptables. El grupo óptico tiene **el precio por delante de los beneficios**, por lo que la operación accionable es filtrar señal del ruido temático y esperar puntos de verificación. La misma tesis de BOM del sistema, dos etapas distintas del ciclo.

**P: ¿Cuándo pasa el caso de OE Solutions de "lista de seguimiento" a "posición central"?**
R: Cuando se confirmen **dos de tres**: (1) el ejercicio 2026 gira realmente a beneficio operativo, (2) las muestras ELSFP en 3T26 se envían y se menciona una cualificación de clientes, (3) el mix datacom sube de forma material por encima del 2%. Dos de tres transforma esto de observación a posición.

---

*Este artículo tiene únicamente fines de investigación e información y no constituye asesoramiento de inversión. Los datos de precio, flujos y beneficios de los siete valores se contrastaron con KRX, Hankyung, Alpha Square y WiseReport. Los detalles del ELSFP y el chip láser de OE Solutions proceden de comunicaciones oficiales de la empresa (OFC 2026, AI EXPO 2026), la documentación del estándar OIF e informes de casas de análisis (iM Securities, Meritz, Hana). Las referencias CPO de Nvidia y Broadcom proceden de las comunicaciones con inversores de cada empresa. Optocore está actualmente suspendida por una auditoría de empresa en funcionamiento y no es invertible. Daehan Optical Communications está en estado de precaución inversora de KRX con advertencia escalando. El análisis puede estar equivocado. Datos actualizados a 2026-05-08–09 KST.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
