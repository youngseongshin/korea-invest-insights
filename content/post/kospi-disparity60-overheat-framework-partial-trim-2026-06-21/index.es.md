---
title: "KOSPI con dispersión de 60 días en +28,6%: no es techo, es señal de reducir riesgo parcial"
date: 2026-06-21T02:35:00+09:00
description: "Reproducción de un marco de sobrecalentamiento por dispersión del KOSPI que muestra por qué +28,6% sobre la media de 60 días debe leerse como señal de rebalanceo parcial, no como techo confirmado."
categories: ["Exclusive Analysis", "Market-Outlook", "Risk-Management"]
tags: ["KOSPI", "disparity", "market breadth", "risk management", "RSI", "ATR", "Samsung Electronics", "SK Hynix", "narrow market"]
series: ["exclusive-analysis", "korea-market-flow", "risk-management"]
slug: "kospi-disparity60-overheat-framework-partial-trim-2026-06-21"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Contexto
> Esta nota continúa el análisis sobre [lo difícil que es batir al KOSPI puro](/es/post/kospi-benchmark-hard-to-beat-narrow-market-monte-carlo-2026-06-20/), [el mercado liderado por flujos ETF](/es/post/korea-etf-flow-led-market-volatility-strategy-2026-06-13/) y [la liquidez abundante con amplitud débil](/es/post/korea-market-liquidity-foreign-reallocation-adr-narrow-leadership-2026-06-03/).

## TL;DR

- Al 19 de junio de 2026, el KOSPI cerró en **9.052**, su media de 60 días fue **7.039** y la dispersión frente a esa media fue **+28,6%**.
- Esto es sobrecalentamiento, pero no prueba un techo. En 355 sesiones desde enero de 2025, las señales de sobrecalentamiento de 20/60/120 días fueron seguidas por rentabilidades medias positivas a 5 y 20 días.
- La señal sí elevó la probabilidad de una corrección: con dispersión60 superior a +20%, la probabilidad de una caída de -5% en 10 sesiones subió de 16% a **63%**.
- Pero 41 días de señal no son 41 observaciones independientes. Se agrupan en **8 episodios**, de los cuales solo 6 tienen ventana futura completa.
- Conclusión: **la reducción parcial de riesgo tiene sentido, pero no es una señal de salida total**. Dispersión y volatilidad están encendidas; la pendiente de la media de 20 días sigue al alza.

<div class="thesis-callout">
  <div class="thesis-callout__label">Punto clave</div>
  <div class="thesis-callout__body">
    La dispersión60 de +28,6% no dice <strong>“este es el techo”</strong>. Dice que la tendencia subió demasiado rápido y que conviene bajar la persecución, recuperar parte del presupuesto de riesgo y esperar una mejor ventana.
  </div>
</div>

## Qué se reprodujo

| Elemento | Configuración |
|---|---|
| Índice | KOSPI, `^KS11` |
| Periodo | 2025-01-02 a 2026-06-19 |
| Muestra | 355 sesiones |
| Precio | Cierre |
| Dispersión | `cierre / media móvil N días - 1` |
| Ventanas | 20, 60 y 120 días |
| Corrección | Mínimo de -5% o peor dentro de 10 sesiones |

## Estado actual

| Métrica | Reproducción |
|---|---:|
| Cierre KOSPI | **9.052** |
| MA20 / dispersión20 | **8.322 / +8,77%** |
| MA60 / dispersión60 | **7.039 / +28,61%** |
| MA120 / dispersión120 | **6.088 / +48,69%** |
| Pendiente 5D de MA20 | **+4,25%** |
| RSI(14) | **SMA 57,3 / Wilder 65,9** |
| ATR(20)% | **zona 4%** |

La señal no viene de RSI. Viene de una distancia extrema frente a la media de 60 días y de una volatilidad elevada.

## La señal no predijo techos

| Señal | Días | Retorno medio +5D | Retorno medio +20D |
|---|---:|---:|---:|
| Dispersión20 ≥ 7% | 74 | +2,68% | +9,07% |
| Dispersión60 ≥ 12% | 120 | +2,26% | +6,88% |
| Dispersión120 ≥ 20% | 107 | +2,55% | +9,11% |
| Base | 335 | +1,86% | +7,83% |

En una tendencia fuerte, sobrecalentamiento puede significar aceleración antes de significar techo.

## Pero sí elevó la probabilidad de corrección

| Condición | Días | Corrección de -5% en 10 sesiones |
|---|---:|---:|
| Base | todos | **16%** |
| Dispersión60 ≥ 15% | 89 | **36%** |
| Dispersión60 ≥ 18% | 54 | **48%** |
| Dispersión60 ≥ 20% | 41 | **63%** |
| Dispersión60 ≥ 22% | 33 | **67%** |
| Dispersión60 ≥ 25% | 26 | **65%** |

La lectura correcta es “sube el riesgo de pullback”, no “hay que vender todo”.

## La advertencia estadística

Los 41 días de señal se reducen a 8 episodios. Solo 6 tienen ventana futura completa, y los 6 generaron corrección de -5%. Es una señal útil, pero la muestra es demasiado pequeña para fijar umbrales exactos como 20%, 22% o 25% con exceso de confianza.

## Tres compuertas actuales

| Compuerta | Regla | Valor actual | Estado |
|---|---|---:|---|
| Sobrevelocidad media | Dispersión60 ≥ 18-20% | **+28,6%** | Encendida |
| Volatilidad | ATR ≥ 2,2% | **zona 4%** | Encendida |
| Deterioro de tendencia | Pendiente MA20 cae | **+4,25%** | No encendida |

Dos compuertas están encendidas. Eso justifica reducir persecución y algo de riesgo. Pero la tercera aún no. Por tanto, esto no es una señal de salida total.

## Cómo usarlo

| Situación | Lectura | Marco de acción |
|---|---|---|
| Dispersión60 12-18% | Tendencia fuerte | Mantener y verificar |
| 18-20% | Sobrevelocidad | Limitar nuevas compras agresivas |
| 20%+ con ATR alto | Mayor riesgo de pullback | Reducir parte del riesgo |
| 20%+ y pendiente MA20 se frena | Riesgo de distribución | Considerar reducción adicional |
| Enfriamiento a 8-12% | Sobrecalentamiento baja | Revaluar con flujos y beneficios |

## Conclusión

La dispersión60 de KOSPI en +28,6% es un sobrecalentamiento real. Pero los datos no apoyan tratarlo como techo confirmado.

La señal debe usarse como herramienta de rebalanceo: dejar de perseguir, recuperar parte del presupuesto de riesgo y esperar deterioro de tendencia o un pullback más limpio.
