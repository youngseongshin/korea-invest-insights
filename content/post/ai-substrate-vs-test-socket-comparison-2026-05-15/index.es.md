---
title: "Las Dos Betas del Back-End de IA — Los Sustratos son una 'Beta de Volumen' y los Sockets de Prueba son una 'Beta de Consumibles.' Mismo Viento a Favor de la IA, Estructuras Completamente Distintas"
date: 2026-05-15
description: "¿Quién gana realmente cuando se vende silicio de IA? No son solo los fabricantes de GPU y HBM. El 'back-end' también tiene grandes ganadores. Hay dos segmentos clave: sustratos y sockets de prueba. Ambos se agrupan bajo 'back-end de IA,' pero sus estructuras de inversión son completamente distintas. Los sustratos son una beta directa del CAPEX en la construcción de servidores de IA: más volumen, paquetes más grandes, mayor ASP. El impulso de corto plazo es sólido: Daeduck Electronics OPM de 14,8% en 1T26, ingresos del segmento de soluciones de empaquetado de Samsung Electro-Mechanics +45%. Los sockets de prueba son una beta de consumibles de alto margen sobre la complejidad del chip. A medida que los chips se vuelven más complejos, las pruebas se endurecen y los sockets deben reemplazarse. ISC OPM de 35% en 1T26, ingresos de IA representando el 81% del total. LEENO Industrial OPM de 47%. Mismo viento a favor de la IA, pero los márgenes difieren en ~3x. No agrupe los dos como un único 'tema de IA.' Para momentum de 3 a 6 meses, sustratos. Para una tenencia de 1 a 2 años, sockets de prueba."
categories: ["Industry-Analysis"]
tags:
  - "silicio de IA"
  - "sustrato"
  - "socket de prueba"
  - "FC-BGA"
  - "back-end de IA"
  - "acciones coreanas"
slug: ai-substrate-vs-test-socket-comparison-2026-05-15
---

> 📚 Serie back-end de IA
> Anteriormente: análisis profundo de MLCC y FC-BGA de Samsung Electro-Mechanics, tesis de memoria legacy de Jeju Semiconductor

*¿Quién gana realmente cuando se vende silicio de IA? Nvidia (GPU) y SK hynix (HBM) son los primeros nombres que vienen a la mente. Pero la cadena de suministro tiene grandes ganadores también en su "back-end." Lo llamamos back-end de IA. Dos segmentos importan más: sustratos y sockets de prueba. Ambos son componentes por los que pasa un chip de IA antes de completarse — pero sus estructuras de inversión son completamente distintas. Los sustratos son una apuesta por las "unidades de servidores de IA." Los sockets de prueba son una apuesta por la "complejidad de los chips de IA." Los márgenes son aproximadamente 3 veces más altos en los sockets de prueba, y el momentum es más rápido en los sustratos. Cuál es la mejor inversión depende del horizonte temporal que tenga en mente.*

---

## Conclusiones clave

* **Dos segmentos en el back-end de IA**: sustratos y sockets de prueba.
* **Esencia del sustrato**: una "beta directa de CAPEX" en la construcción de servidores de IA. Más unidades → más ingresos; paquetes más grandes → mayor ASP.
* **Esencia del socket de prueba**: una "beta de consumibles de alto margen" sobre la complejidad del chip. Chips más complejos → pruebas más exigentes → más sockets y más especializados.
* **Brecha de rentabilidad**: en 1T26, Daeduck Electronics 14,8% vs ISC 35% vs LEENO Industrial 47,4%. **Los sockets de prueba dominan**.
* **Brecha de momentum**: las revisiones de estimados de sustratos son más rápidas — alzas de ASP, nuevos LTAs con grandes tecnológicas y escasez de capacidad son catalizadores de corto plazo.
* **Riesgo de ciclo**: los sustratos son un ciclo de CAPEX (escasez → CAPEX → exceso de oferta). Los sockets de prueba, al ser consumibles, tienen menor ciclicidad.
* **Conclusión**: operaciones de momentum de corto plazo → sustratos (Daeduck Electronics, Samsung Electro-Mechanics). Compounding de 1 a 2 años → sockets de prueba (LEENO Industrial, ISC). No son el mismo "tema de IA."

---

## 1. Contexto — qué son realmente los sustratos y los sockets de prueba

### 1.1 Cómo se fabrica el silicio de IA

```
Flujo de producción del silicio de IA:

1. Diseño (Nvidia, AMD, Google, Meta, etc.)
2. Fabricación de obleas (TSMC, Samsung Foundry)
3. Corte en dados
4. Empaquetado (unión de HBM, interposer y sustrato del paquete)
   ← los "sustratos" se utilizan aquí
5. Prueba (rendimiento / fiabilidad / burn-in)
   ← los "sockets de prueba" se utilizan aquí
6. Envío

Sustrato     = "el pedestal sobre el que descansa el chip"
Socket de prueba = "la ranura en la que el chip se conecta brevemente para ser probado"

Ambos son componentes por los que pasa el silicio de IA antes de completarse,
pero sus funciones y patrones de uso son completamente distintos.
```

### 1.2 Sustrato — qué es

```
Un sustrato conecta los circuitos microscópicos dentro de un chip
(escala de nanómetros) con el mundo exterior (escala de milímetros).

Sus funciones:
1. Conexión eléctrica (miles de pines → tarjeta)
2. Soporte mecánico (montaje estable de paquetes grandes)
3. Gestión térmica (vía de disipación del calor del chip)
4. Integridad de señal (señales de alta velocidad sin pérdida)

Por qué importa la IA:
- Los chips de IA son mucho más grandes que el silicio típico
  (Nvidia H100 = 814 mm², 2–3x un CPU convencional)
- Miles a decenas de miles de pines
- Movimiento de datos a alta velocidad
- Gran presupuesto térmico (700W+)

→ Se requieren sustratos especializados (FC-BGA)
→ Más difíciles de fabricar y más costosos que los sustratos ordinarios
→ Fabricantes coreanos: Samsung Electro-Mechanics, Daeduck Electronics,
  Isu Petasys.
```

### 1.3 Socket de prueba — qué es

```
Un socket de prueba es una ranura que se usa brevemente para probar un chip terminado.

Sus funciones:
1. Conecta eléctricamente cada pin del chip al equipo de prueba
2. Verifica que el chip funcione bajo estrés de señal / energía / temperatura
3. Filtra las unidades defectuosas
4. Validación de fiabilidad (pruebas de larga duración)

Analogía:
Chip          = automóvil
Socket de prueba = el puerto de diagnóstico en la bahía de inspección
→ Se conecta brevemente durante la inspección, luego se desconecta
→ El mismo puerto se usa para muchos autos diferentes
→ Los puertos se desgastan con el tiempo y deben reemplazarse

Por qué importa la IA:
- Los chips de IA son costosos (\~USD 30k por un H100)
- Una sola unidad defectuosa tiene un alto costo → la intensidad de prueba aumenta
- Entornos de alta corriente / alta velocidad / alta temperatura
  → especificaciones de socket más exigentes
- Cada generación de chip requiere nuevos sockets → ingresos recurrentes

Fabricantes coreanos: LEENO Industrial, ISC, TSE.
```

### 1.4 Por qué no son el mismo "tema de IA"

```
Sustrato:
- Se fabrica una vez y se envía con el chip (carácter de bien de capital)
- Aproximadamente un sustrato por servidor de IA
- Ingresos = volumen × ASP
- Agregar capacidad = carga de CAPEX

Socket de prueba:
- Se reutiliza muchas veces y luego se reemplaza (carácter de consumible)
- Aproximadamente 50–200 sockets para probar 10.000 chips
- Ingresos = producción de chips × intensidad de prueba × reemplazo de sockets
- Las ampliaciones de capacidad son menores

Estructura de márgenes:
Sustrato:       OPM \~10–15% (arrastre de CAPEX y depreciación)
Socket de prueba: OPM \~30–50% (diseño personalizado, economía de consumibles)

→ Ambos se benefician de la IA,
→ pero la mezcla de ingresos, el perfil de márgenes y la sensibilidad al ciclo difieren.
```

---

## 2. El lado del sustrato — "beta de volumen del servidor de IA"

### 2.1 Lo que mostró el 1T26

```
Samsung Electro-Mechanics (009150) — segmento Package Solution
(liderado por FC-BGA):
Ingresos 1T26: KRW 725B
Variación interanual: +45%
Variación intertrimestral: +12%

Daeduck Electronics (353200):
Ingresos 1T26: KRW 346,3B (variación interanual +61%)
OP 1T26:       KRW 51,3B (retorno a números positivos)
OPM:           14,8%

Mezcla de productos:
- FCCSP (sustrato de paquete grado móvil): 39%
- FCBGA (grado PC / servidor):             23%
- CSP (memoria):                           22%
- MLB (tarjeta multicapa, servidor de IA): 16%

Crecimiento interanual:
- Sustratos de paquete: +65%
- MLB:                  +43%

→ Sustratos de paquete para servidores de IA + tarjetas de red creciendo juntos
→ Una beta directa en infraestructura de IA.
```

### 2.2 Por qué los sustratos escasean

```
Características del FC-BGA para servidores de IA:
- Área superficial 2–3x un FC-BGA para PC
- Multicapa (20–30 capas)
- Señalización de alta velocidad (PCIe 5.0 / 6.0)
- Gestión térmica estricta

Empresas capaces de fabricarlos:
- Corea: Samsung Electro-Mechanics, Daeduck, LG Innotek, Isu Petasys
- Taiwán: Unimicron, Nan Ya PCB
- Japón: Ibiden, Shinko Denki

El problema: la capacidad (CAPA) no puede seguir el ritmo de la demanda
- Los pedidos de servidores de IA de las grandes tecnológicas se han disparado
- Construir fábricas de sustratos desde cero toma 2–3 años
- Escasez de oferta → alza de ASP

Prensa citada:
"La demanda de FC-BGA de Samsung Electro-Mechanics supera la capacidad en \~50%;
 negociaciones de alza de precios en curso."

→ Por eso las acciones de sustratos han tenido un comportamiento sólido.
```

### 2.3 Riesgo de ciclo del sustrato

```
El sustrato es una industria clásica de ciclo CAPEX:

Ciclo alcista (hoy):
escasez → alza de ASP → expansión de márgenes → fortaleza de acciones
→ las empresas anuncian CAPEX significativo

Fase de construcción (2026–2027):
fábricas en construcción → ingresos subiendo, carga de CAPEX subiendo
→ acciones aún en tendencia positiva

Construcción completa (2027–2028):
nuevas fábricas entran en operación → la oferta se dispara
→ si la demanda no acompaña, los precios caen
→ los márgenes se comprimen → las acciones se debilitan

Patrones históricos:
Ciclo de memoria 2017–2018: misma forma
Ciclo MLCC 2021–2022:       misma forma

→ Para invertir en sustratos, la clave es "en qué punto del ciclo CAPEX estamos"
→ Hoy: etapa inicial a intermedia de un ciclo alcista
→ Hasta que se complete la construcción, el potencial alcista está intacto.
```

---

## 3. El lado del socket de prueba — "beta de complejidad del chip"

### 3.1 Lo que mostró el 1T26

```
ISC (095340):
Ingresos 1T26: KRW 68,3B
OP 1T26:       KRW 23,6B
OPM:           35%
Cálculo: 23,6 / 68,3 = 34,55%

Mezcla de ingresos:
- Ingresos de IA:             KRW 55,3B (81% del total)
- Ingresos de centros de datos: KRW 54,2B (79% del total)
→ Ya es una "empresa de centros de datos de IA."

LEENO Industrial (058470):
Ingresos 1T26: KRW 99,77B
OP 1T26:       KRW 47,30B
OPM:           47,4%
Cálculo: 47,30 / 99,77 = 47,41%

Mezcla de ingresos:
- Sockets de prueba de IC:    64,10%
- Pines LEENO (pogo):         24,65%
- Componentes médicos:        10,46%

→ Sockets de diseño personalizado + fabricación integrada verticalmente de pines
→ Un OPM del 47% está en la cima de la manufactura coreana.
```

### 3.2 Por qué los márgenes son tan altos

```
Características estructurales de la industria de sockets de prueba:

1. Diseños específicos para cada cliente
   → la disposición de pines, el tamaño y las condiciones de señal varían por chip
   → difícil de estandarizar → poder de fijación de precios

2. Alto costo de calificación
   → cada nuevo chip requiere diseño / prueba / calificación del socket
   → una vez calificado, queda comprometido hasta el fin de vida de ese chip
   → competencia por fiabilidad, no por precio

3. Naturaleza de consumible
   → los sockets se desgastan / degradan y necesitan reemplazo periódico
   → ingresos recurrentes

4. Renovación con cada generación de chip
   → nuevo chip = nuevo socket
   → ciclo de chips más rápido = ciclo de ingresos más rápido

5. TAM pequeño (decenas de miles de millones de USD)
   → demasiado pequeño para que entren grandes corporaciones
   → oligopolio de especialistas

Las cinco condiciones en conjunto permiten un OPM del 30–50%.
```

### 3.3 Por qué la IA hizo más importantes a los sockets de prueba

```
Características de los chips de IA:

1. Costosos (USD 10k–30k por unidad)
   → el costo de una sola unidad defectuosa es alto
   → intensidad de prueba ↑

2. Alto conteo de pines (miles a decenas de miles)
   → sockets más complejos
   → ASP ↑

3. Alta corriente / temperatura / velocidad
   → requisitos de durabilidad del socket más exigentes
   → ciclo de reemplazo más corto

4. Mayor participación del SLT (System-Level Test)
   → de prueba funcional simple → prueba de sistema completo
   → tiempos de prueba más largos
   → mayor uso de sockets

5. Nuevos módulos: HBM, SOCAMM2, etc.
   → nuevas categorías de sockets
   → nuevas líneas de ingresos

→ En la era de la IA, la demanda de sockets de prueba crece
   más rápido que la producción de chips.
```

### 3.4 ISC vs LEENO Industrial

```
Ambas son "empresas de sockets de prueba," pero sus estructuras difieren.

ISC (fortaleza en sockets de caucho):
- Tecnología central: sockets de caucho de silicona
- Fortaleza: pruebas de producción masiva de centros de datos de IA, SLT
- Clientes: grandes fabricantes globales de GPU / ASIC
- Exposición: centros de datos de IA al 81%
- Perfil: beta directa de IA (mayor volatilidad)
- OPM 1T26: 35%

LEENO Industrial (fortaleza en pines pogo):
- Tecnología central: pines pogo, fabricación propia de pines
- Fortaleza: I+D, AP móvil, RF, desarrollo de ASIC
- Clientes: diversificados (cientos de cuentas)
- Exposición: muchas categorías de chips (menor exposición a IA que ISC)
- Perfil: compounder de calidad (más estable)
- OPM 1T26: 47,4%

→ No los agrupe como "la misma acción de sockets de prueba."
→ ISC      = beta de centros de datos de IA
→ LEENO    = plataforma diversificada de alto margen

Son complementarios, no sustitutos.
```

---

## 4. Comparación directa

### 4.1 Márgenes operativos del 1T26

```
Los mismos "beneficiarios del back-end de IA," distintos perfiles de márgenes:

Daeduck Electronics (sustrato):        14,8%  ████
Samsung E-M Package Solutions:         \~12%   ███
ISC (socket de prueba):                35,0%  █████████
LEENO Industrial (socket):             47,4%  ████████████

KRW 100 de ingresos → OP:
Daeduck:  KRW 14,8
ISC:      KRW 35,0
LEENO:    KRW 47,4

→ Brecha de \~3x sobre los mismos ingresos
→ El resultado de diferencias estructurales en la industria.
```

### 4.2 Ritmo de crecimiento vs estabilidad de márgenes

| Métrica | Sustrato (Daeduck) | Socket de prueba (ISC) | Socket de prueba (LEENO) |
| --- | ---: | ---: | ---: |
| Ingresos 1T26 interanual | +61% | Sólido interanual | +18% |
| OP 1T26 interanual | retorno a positivo | Sólido interanual | +35% |
| OPM | 14,8% | 35,0% | 47,4% |
| Exposición a IA | Media–alta | Muy alta (81%) | Media |
| Volatilidad | Alta | Media | Baja |
| Sensibilidad al ciclo | Alta | Media | Baja |

```
Resumen:
- Crecimiento de ingresos: sustrato (Daeduck) > socket de prueba
- Nivel de márgenes:       socket de prueba > sustrato
- Estabilidad de márgenes: LEENO > ISC > sustrato
- Beta directa de IA:      ISC > Daeduck > LEENO.
```

### 4.3 Riesgo de ciclo

```
Riesgo de ciclo del sustrato (alto):
- Escasez → CAPEX → exceso de oferta, en ciclo repetido
- Plazo de construcción de 2–3 años
- Cuando el ciclo gira, la utilización y el ASP caen juntos
- La depreciación presiona los márgenes

Riesgo de ciclo del socket de prueba (bajo):
- La economía de consumibles amortigua la volatilidad de ingresos
- El diseño específico para cada cliente mantiene estables los precios
- Los nuevos chips siguen lanzándose continuamente
- La volatilidad trimestral aún existe

Perspectiva de tenencia larga:
→ Los sockets de prueba son mucho más estables
→ evita el ciclo CAPEX de los sustratos

Perspectiva de momentum de corto plazo:
→ El momentum del sustrato es más fuerte
→ Los titulares de alza de ASP / escasez de capacidad son más frecuentes.
```

---

## 5. Prioridad de inversión — distintas respuestas para distintos horizontes

### 5.1 Momentum de corto plazo (3–6 meses) — los sustratos ganan

```
Por qué:
- El ritmo de revisión de estimados es más rápido
- Flujo constante de titulares sobre alzas de ASP
- Probabilidad de nuevos LTAs con grandes tecnológicas
- Los envíos de servidores de IA se aceleran

Orden de preferencia:
1. Daeduck Electronics: retorno a positivo + beta MLB / FC-BGA de IA
2. Samsung Electro-Mechanics: combo FC-BGA de IA + MLCC
3. Isu Petasys (complemento): fortaleza en MLB de capas ultra-altas

Advertencias:
- Los sustratos ya se han movido bastante
- Verificar la posición en el ciclo CAPEX
- Esperar a que se despeje la barrera macro (ver publicación anterior).
```

### 5.2 Tenencia de 1–2 años (crecimiento de calidad) — los sockets de prueba ganan

```
Por qué:
- La estructura de márgenes es estructuralmente superior
- Menor riesgo de ciclo
- La diversificación de chips de IA = más categorías de sockets = diversificación de ingresos
- Expansión activa de capacidad (nuevas fábricas)

Orden de preferencia:
1. LEENO Industrial: la más alta calidad, pero el múltiplo es exigente
2. ISC: beta directa de centros de datos de IA
3. TSE (complemento): crecimiento a un precio más razonable

Advertencias:
- LEENO enfrenta riesgo de impacto en márgenes durante la mudanza a la nueva fábrica
- ISC tiene volatilidad trimestral (1T26 intertrimestral -6%)
- Ambas cotizan a 30–45x PER.
```

### 5.3 Un portafolio combinado de back-end de IA

```
Agresivo (orientado al momentum):
- Daeduck Electronics        40%
- ISC                        30%
- Samsung Electro-Mechanics  20%
- LEENO Industrial           10%

Equilibrado (crecimiento + estabilidad):
- LEENO Industrial           30%
- Samsung Electro-Mechanics  25%
- ISC                        25%
- Daeduck Electronics        20%

Defensivo (orientado a calidad):
- LEENO Industrial           40%
- Samsung Electro-Mechanics  30%
- ISC                        20%
- Daeduck Electronics        10%

→ Si debe elegir solo una, por horizonte y tolerancia a la volatilidad:
→ Tenencia 1 año+:         LEENO Industrial
→ 3–6 meses:               Daeduck Electronics
→ Beta directa de centros de datos de IA: ISC.
```

---

## 6. Cuatro conceptos erróneos comunes

### 6.1 #1: "Ambos son apuestas por la IA, así que son iguales"

```
Como se ha demostrado:
- El OPM difiere en 3x
- La sensibilidad al ciclo difiere
- La mezcla de ingresos difiere

Agruparlos en un solo bloque debilita la diversificación.
→ La volatilidad se mueve en conjunto
→ Combinarlos con otro sector es más efectivo.
```

### 6.2 #2: "Los sockets pogo están siendo reemplazados por sockets de caucho"

```
Solo parcialmente cierto:

Dónde ocurre el cambio:
- Chips de gran die de GPU / ASIC de IA
- Pruebas de señal de alta corriente / alta velocidad
- SLT (System-Level Test)
→ La penetración de sockets de caucho aumenta (fortaleza de ISC)

Dónde no ocurre:
- Pruebas de I+D de alta precisión
- APs móviles, chips RF
- Producción de pequeños lotes / múltiples SKUs
→ El pogo mantiene participación (fortaleza de LEENO)

→ No es "todo el mercado se convierte" — es "segmentación del mercado"
→ Por lo tanto ISC y LEENO son complementarios
→ Es raro que solo uno de ellos tenga un buen desempeño.
```

### 6.3 #3: "Las acciones de sustratos ya subieron demasiado"

```
La pregunta correcta no es el nivel absoluto,
sino "en qué punto del ciclo CAPEX estamos."

Ahora:
- La escasez aún continúa
- Negociaciones de alza de ASP en curso
- LTAs con grandes tecnológicas en discusión
- Los anuncios de CAPEX han comenzado, pero las rampas tardan 2–3 años

→ Etapa inicial a intermedia de un ciclo alcista
→ Los precios se movieron, pero el ciclo no ha tocado techo.

Dicho esto, desde estos niveles:
- Se recomiendan entradas escalonadas
- Esperar a que se despeje la barrera macro
- Perseguir el precio es ineficiente.
```

### 6.4 #4: "El TAM de los sockets de prueba es demasiado pequeño"

```
Cierto en términos nominales, pero la lectura es incorrecta:

TAM de sockets de prueba:
- \~USD 3–4 mil millones
- Menos del 2% del mercado de memoria (\~USD 200B)
- Pequeño en términos absolutos

Por qué eso es en realidad una ventaja:
- Demasiado pequeño para que entren grandes corporaciones
- Mantiene el oligopolio de especialistas
- La competencia por precios se mantiene moderada
- OPM del 30–50% alcanzable

Comparación:
Un negocio de USD 200B con OPM del 5% vs
un negocio de USD 4B con OPM del 45%
→ OP absoluto comparable en términos de dólares
→ El segundo es más estable y más predecible.

Esta es la estructura de la que se benefician LEENO e ISC.
```

---

## 7. Los próximos seis meses — lista de verificación

### 7.1 Sustratos (confirmación de ciclo intacto)

```
Señales positivas:
□ Las alzas de ASP del FC-BGA continúan
□ Samsung E-M / Daeduck agregan nuevos clientes de grandes tecnológicas
□ La mezcla de die grande / alta capa sube en los ingresos
□ La demanda de MLB persiste en redes 800G / 1,6T
□ La utilización se mantiene por encima del 90% incluso con el aumento de CAPEX

Señales negativas:
□ Las negociaciones de alza de ASP se retrasan / fracasan
□ Los pedidos de servidores de IA de grandes tecnológicas se desaceleran
□ El ritmo de nuevos anuncios de CAPEX se acelera (preocupación por exceso de oferta)
□ La utilización cae por debajo del 80%

Frecuencia: resultados trimestrales + comentarios de IR entre trimestres.
```

### 7.2 Sockets de prueba (confirmación de crecimiento intacto)

```
ISC:
□ Reaceleración de ingresos en 3T26 (2T puede ser un trimestre de preparación de rampa)
□ Inicio del primer volumen de nuevos clientes de infraestructura de centros de datos
□ Comienzo de ingresos por pruebas de producción masiva de SOCAMM2
□ La mezcla de SLT se mantiene por encima del 70%
□ La mezcla de ingresos de IA se mantiene por encima del 80%

LEENO Industrial:
□ Avance en la mudanza a la nueva fábrica
□ Sin deterioro de márgenes durante la mudanza (OPM 45%+ se mantiene)
□ Diversificación de clientes (expansiones en Apple / TI / HPC / ASIC)
□ Sólida demanda de sockets de I+D
□ Sin exceso de acciones / problemas de gobierno corporativo

Frecuencia: resultados trimestrales.
```

### 7.3 El contexto macro

```
La barrera macro de la publicación anterior:
- Bono del Tesoro a 10 años de EE.UU. por debajo de 4,45%
- Brent por debajo de 105
- USD/KRW por debajo de 1.480
- VIX por debajo de 18

Estas condiciones deben despejarse para:
- Una recuperación amplia de activos de riesgo
- Que las acciones de back-end sigan la tendencia
- Que buenos resultados se traduzcan en buenos precios.

Si la barrera no se despeja:
- Los múltiplos permanecen comprimidos independientemente de los fundamentos
- Esperar a un cierre / volumen confirmatorio antes de escalar posiciones.
```

---

## 8. Cómo se conecta con otras publicaciones

```
Publicación sobre Samsung Electro-Mechanics:
→ Beneficiario dual de MLCC + FC-BGA en 1T26
→ La acción más detallada en el lado de sustratos de este artículo
→ PERs por escenario sobre qué tan lejos puede estirarse el múltiplo

Publicación sobre Jeju Semiconductor:
→ "Memoria commodity en escasez a causa de la IA"
→ Otra forma del back-end de IA (beta de escasez de memoria)

Publicación sobre la huelga en Samsung Electronics:
→ Variable clave para el superciclo de memoria
→ Silicio de IA → servidor de IA → memoria / sustrato / socket de prueba
→ Una interrupción en uno repercute en el back-end

Publicación sobre el crash del KOSPI + barrera macro:
→ "El ciclo antes que la acción"
→ Los nombres en esta publicación también son racionales solo después de que se despeje la barrera macro.
```

---

## 9. La conclusión en una línea

Cuando se vende silicio de IA, los primeros beneficiarios son los fabricantes de GPU y HBM. Pero el back-end también tiene dos grandes ganadores — **sustratos y sockets de prueba**.

Ambos se agrupan como "back-end de IA," pero sus estructuras son completamente distintas. **Los sustratos son una "beta de volumen del servidor de IA."** El volumen sube, los paquetes crecen, el ASP aumenta — potencial alcista directo. El momentum es rápido y los márgenes operativos se expanden desde una base de \~12–15% en 1T26. Pero esta es una industria de ciclo CAPEX, y la fecha de finalización de la construcción es el riesgo.

**Los sockets de prueba son una "beta de complejidad del chip."** A medida que los chips se vuelven más complejos, las pruebas se endurecen y se necesitan nuevos sockets cada vez. El OPM es del 35% para ISC y del 47% para LEENO — aproximadamente 3 veces los márgenes de los sustratos. La economía de consumibles amortigua la ciclicidad. Los puntos débiles: el TAM es pequeño y los múltiplos ya son exigentes.

**No los agrupe como un único "tema de IA."** Para momentum de corto plazo, los sustratos (Daeduck Electronics, Samsung Electro-Mechanics) lideran. Para una tenencia de 1 a 2 años, los sockets de prueba (LEENO Industrial, ISC) tienen más sentido. La mejor estrategia es mantener ambos como complementos — cuando los sustratos se sacuden en el pico del ciclo, los sockets de prueba actúan como defensa; cuando los sockets de prueba sufren presión de múltiplos, el momentum de los sustratos sostiene la cartera.

**Mismo viento a favor de la IA, estructuras completamente distintas — entender solo eso eleva la calidad de las decisiones de inversión en back-end un peldaño completo.**

---

*Este artículo es solo investigación y comentario, y no constituye asesoramiento de inversión. Las cifras del 1T26 de Samsung Electro-Mechanics corresponden al comunicado oficial de IR de la empresa. Las del 1T26 de Daeduck Electronics (ingresos KRW 346,3B, OP KRW 51,3B, OPM 14,8%) corresponden a sus materiales de IR. Las del 1T26 de ISC (ingresos KRW 68,3B, OP KRW 23,6B, OPM 35%, mezcla de ingresos de IA 81%, mezcla de centros de datos 79%) corresponden a sus materiales de IR. Las del 1T26 de LEENO Industrial (ingresos KRW 99,77B, OP KRW 47,30B, OPM 47,4%) corresponden al reporte preliminar de divulgación; las cifras de mezcla de productos (sockets de prueba de IC 64,10%, pines LEENO 24,65%, componentes médicos 10,46%) corresponden al reporte trimestral. El OPM se calcula dividiendo el beneficio operativo por los ingresos, redondeado a un decimal. Las participaciones de ingresos de IA / centros de datos se derivan de las divulgaciones de las empresas. La comparación de márgenes operativos refleja un solo trimestre (1T26); los promedios anuales pueden diferir. El riesgo de ciclo CAPEX, el riesgo de margen durante la transición a la nueva fábrica y la volatilidad de la demanda de IA son juicios del autor y no certezas. Las variables macro globales (tasas de EE.UU., petróleo, divisas, VIX) pueden mover las acciones de forma independiente. El análisis puede estar equivocado. Corte de datos: 15 de mayo de 2026, hora de Corea.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
