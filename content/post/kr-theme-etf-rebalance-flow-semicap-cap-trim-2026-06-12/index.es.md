---
title: "Flujo de rebalanceo de ETF temáticos en Corea: compra por redistribución en semiconductores y presión de recorte en líderes"
date: 2026-06-12T17:40:00+09:00
description: "La primera ejecución de KR Theme ETF Rebalance Flow v1 detectó posible flujo mecánico por rebalanceo y límites de peso en ETF temáticos coreanos. El 12 de junio de 2026, las señales más fuertes aparecieron en equipos y materiales de semiconductores."
categories: ["Korean-Equities", "Market-Flow", "ETF-Flow"]
tags: ["ETF Corea", "rebalanceo ETF", "semiconductores", "flujo pasivo", "SK Hynix", "Samsung Electro-Mechanics"]
series: ["korea-rerating-2026", "korea-market-flow"]
slug: "kr-theme-etf-rebalance-flow-semicap-cap-trim-2026-06-12"
draft: false
---

## TL;DR

- Thesis OS añadió **KR Theme ETF Rebalance Flow v1**, un monitor para estimar flujos mecánicos por rebalanceo de ETF temáticos coreanos.
- La primera ejecución analizó **31 ETF**, encontró **30 válidos**, procesó **291 filas de constituyentes** y generó **69 candidatos**.
- Hubo **60 candidatos de compra por redistribución** y **9 candidatos de recorte por límite de peso**.
- La señal más fuerte no fue nuclear/SMR, sino **equipos y materiales de semiconductores**.
- Leeno Industrial, EO Technics, Soulbrain, DB HiTek, Hanmi Semiconductor, ISC y Wonik IPS fueron los candidatos principales de compra por redistribución.

## 1. Qué mide el monitor

El monitor estima un proxy de redistribución de pesos:

```text
Flujo por ETF = NAV del ETF × cambio de peso objetivo
Flujo por acción = suma de flujos de varios ETF
Intensidad = flujo estimado / valor negociado promedio de 20 días
```

Usa datos públicos de Naver ETF surface, como `constituentList` y `totalNav`, junto con ADV20 de la base local. Si un constituyente supera el límite supuesto, el modelo lo reduce hasta el límite y redistribuye el exceso entre los nombres por debajo del límite.

No es PCF oficial. Antes de tratarlo como señal operativa, hay que comprobar PDF/PCF oficiales, metodología del índice, regla real de límite y volumen de cierre.

| Métrica | Valor |
|---|---:|
| Fecha | 2026-06-12 |
| ETF analizados | 31 |
| ETF válidos | 30 |
| Filas de constituyentes | 291 |
| Candidatos totales | 69 |
| Compra por redistribución | 60 |
| Recorte por límite | 9 |
| Confianza | media-baja |

## 2. Principales candidatos de compra por redistribución

| Nombre | Flujo estimado | Flujo/ADV20 | Rentabilidad diaria |
|---|---:|---:|---:|
| Leeno Industrial | 270.4 mil millones KRW | +2.68x | +4.7% |
| EO Technics | 197.8 mil millones KRW | +2.49x | +21.4% |
| Soulbrain | 69.4 mil millones KRW | +2.44x | +24.4% |
| DB HiTek | 264.3 mil millones KRW | +2.02x | +12.3% |
| Hanmi Semiconductor | 721.0 mil millones KRW | +1.81x | +24.1% |
| ISC | 92.0 mil millones KRW | +1.76x | +20.7% |
| Wonik IPS | 211.1 mil millones KRW | +1.63x | +30.0% |

El dato clave es la intensidad frente a liquidez. Los nombres medianos pueden reaccionar más que los líderes, aunque el flujo absoluto sea menor.

## 3. Candidatos de recorte por límite de peso

| Nombre | Flujo estimado | Flujo/ADV20 | Lectura |
|---|---:|---:|---|
| SK Hynix | -1.76 billones KRW | -0.15x | presión técnica, no tesis bajista |
| Samsung Electronics | -49.4 mil millones KRW | -0.00x | impacto relativo bajo |
| Samsung Electro-Mechanics | -514.9 mil millones KRW | -0.21x | vigilar presión técnica |
| LS ELECTRIC | -47.0 mil millones KRW | -0.15x | no perseguir sin confirmación |
| Doosan Enerbility | -26.5 mil millones KRW | -0.07x | caso nuclear a vigilar |

Cap-trim no significa venta automática. Si el precio resiste pese a la presión mecánica, puede señalar demanda real.

## 4. Disciplina de uso

| Paso | Confirmación necesaria |
|---|---|
| 1 | PDF/PCF oficial del ETF |
| 2 | Metodología del índice y regla real de límite |
| 3 | Volumen de cierre y subasta final |
| 4 | Fuerza relativa T+1/T+3 |
| 5 | Coincidencia con flujos de programa, extranjeros o instituciones |

## Conclusión

La primera lectura de KR Theme ETF Rebalance Flow apunta a **redistribución hacia semiconductores de segunda línea**. Es una señal útil para priorizar vigilancia, pero todavía de confianza media-baja hasta que se confirme con datos oficiales y ejecución real.
