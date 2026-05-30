---
title: "Mapa de múltiplos de infraestructura de IA: por qué Samsung Electronics parece barata y Samsung Electro-Mechanics cara"
date: 2026-05-31T09:00:00+09:00
description: "GPU, HBM, CPU, MLCC y FC-BGA pertenecen al mismo ciclo de infraestructura de IA, pero no merecen el mismo múltiplo. El artículo descompone la diferencia por poder de precio, contratos de largo plazo, lock-in, capex y duda de beneficio pico."
categories: ["Market-Outlook"]
tags:
  - "infraestructura IA"
  - "múltiplos"
  - "HBM"
  - "GPU"
  - "CPU"
  - "MLCC"
  - "FC-BGA"
  - "Samsung Electronics"
  - "Samsung Electro-Mechanics"
  - "SK hynix"
  - "Nvidia"
  - "Broadcom"
  - "semiconductores coreanos"
slug: ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31
valley_cashtags:
  - 삼성전자
  - 삼성전기
  - SK하이닉스
draft: false
---

> Contexto
> Este artículo conecta la tesis de [Samsung Electronics y el superciclo de memoria](/es/post/samsung-electronics-stock-bonus-supercycle-buyback-2026-05-27/) con la tesis de [Samsung Electro-Mechanics y su prima frente a Murata / Ibiden](/es/post/samsung-electro-mechanics-market-cap-murata-ibiden-premium-2026-05-28/). La pregunta central es sencilla: dentro del mismo ciclo de infraestructura de IA, ¿por qué unas capas merecen múltiplos altos y otras no?

## TL;DR

La exposición a IA no basta para justificar un múltiplo. El mercado paga por <strong>duración de beneficios, poder de precio, lock-in de cliente, riesgo de capacidad y menor duda de beneficio pico</strong>.

El riesgo actual es tratar a los proveedores de MLCC y FC-BGA como si fueran monopolios estructurales tipo GPU/HBM. Son cuellos de botella reales, pero no todos los cuellos de botella merecen un múltiplo de plataforma.

La idea relativa más fuerte es <strong>Samsung Electronics</strong>: tiene recuperación en HBM, ciclo de memoria y opción de foundry, pero el snapshot público del 29-30 de mayo de 2026 la deja en torno a 7.8x forward P/E y 4.4x P/B. Samsung Electro-Mechanics tiene una tesis correcta, pero el precio ya exige varios años de ejecución perfecta. ([Yahoo Finance][1])

## 1. La fórmula

```text
Prima de múltiplo
= poder de precio × duración de demanda × lock-in de cliente × conversión a FCF

Descuento de múltiplo
= capex de expansión × riesgo de sobreoferta × duda de beneficio pico × concentración de clientes
```

| Capa | Por qué sube el múltiplo | Por qué se limita | Pregunta clave |
|---|---|---|---|
| GPU / plataforma | CUDA, sistemas rack-scale, software, estructura asset-light | ASICs propios, China, poder de hyperscalers | ¿El cliente compra tiempo o solo un chip? |
| HBM | HBM4, suministro vendido, LTAs, más contenido por acelerador | duda de ciclo de memoria, capex, diversificación | ¿Franquicia contratada o beneficio cíclico? |
| CPU | más servidores de IA, control plane | sustitución por ARM / CPU internas | ¿Cuello primario o pieza auxiliar? |
| FC-BGA | substratos grandes, muchas capas, certificación | capex, depreciación, memoria de sobrecapacidad ABF | ¿El capex está cubierto por LTAs? |
| MLCC / Si-Cap | integridad de potencia, piezas de alta fiabilidad | mezcla con MLCC genérico, competencia | ¿Bloquea envíos o es componente común? |

## 2. Lectura por capa

NVIDIA recibe el múltiplo más alto porque no vende solo GPU: controla GPU, networking, software, referencias de sistema y arquitectura de fábrica de IA. En FY2027 Q1 reportó ingresos de 81.6 mil millones de dólares, 75.2 mil millones en Data Center y guía de 91.0 mil millones para Q2. ([NVIDIA Investor Relations][2])

HBM tiene beneficios explosivos, pero sigue bajo la sombra del ciclo de memoria. El punto decisivo son los LTAs: si los contratos fijan precio, volumen y recuperación de capex, el mercado puede empezar a verlo como memoria de alto valor contratada, no DRAM commodity.

CPU se beneficia del ciclo, pero no es el principal cuello de botella. AMD crece en Data Center, pero el múltiplo alto necesita que EPYC e Instinct funcionen a la vez. Intel necesita prueba de ejecución antes de recibir prima.

MLCC y FC-BGA son tesis correctas, especialmente para Samsung Electro-Mechanics. En Q1 2026 la compañía citó MLCC para servidores de IA y FC-BGA para aceleradores / CPUs de servidor como motores del crecimiento. También firmó un contrato de silicon capacitor de aproximadamente 1.5 billones de wones para 2027-2028. ([Samsung Electro-Mechanics][7], [Samsung Electro-Mechanics][8])

Pero el precio importa. ResearchAndMarkets estima que el mercado global de FC-BGA crece de 2.46 mil millones de dólares en 2026 a 3.74 mil millones en 2032, un CAGR de 7.1%. Ese crecimiento por sí solo no justifica múltiplos de 100x P/E. ([Research and Markets][9])

## 3. Samsung Electronics vs Samsung Electro-Mechanics

Samsung Electronics no es solo una acción de memoria cíclica. Combina HBM4E, DDR5, SOCAMM2, eSSD / KV-cache y foundry. Esa amplitud la convierte en una opción sobre la jerarquía de memoria de inferencia de IA.

Samsung Electro-Mechanics combina MLCC, FC-BGA y Si-Cap. Eso puede reclasificarla como proveedor de integridad de potencia para paquetes de IA. Pero con múltiplos ya muy altos, la acción necesita más que narrativa: nuevos clientes, margen de Si-Cap, ASP de MLCC de IA, utilización FC-BGA y LTAs.

## 4. Visión práctica

| Nombre | Visión | Motivo |
|---|---|---|
| Samsung Electronics | Under / candidato a compra | bajo múltiplo frente a HBM catch-up, memoria y foundry |
| NVIDIA | Fair a relativamente under | crecimiento y margen justifican parte del múltiplo |
| SK hynix | fundamentalmente under, esperar timing | HBM puro fuerte, pero P/B y rally pesan |
| Samsung Electro-Mechanics | over / no perseguir | tesis correcta, precio adelantado |
| Murata / Ibiden | over | cuello real, pero múltiplo de monopolio |

El error más peligroso del ciclo es dar múltiplo de plataforma a todos los proveedores que tocan la cadena de NVIDIA.

[1]: https://finance.yahoo.com/quote/005930.KS/key-statistics/ "Samsung Electronics valuation"
[2]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx "NVIDIA FY2027 Q1 results"
[3]: https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-first-quarter-fiscal-year-2026-financial "Broadcom Q1 FY2026 results"
[7]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Q1 2026"
[8]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics silicon capacitor contract"
[9]: https://www.researchandmarkets.com/reports/6128754/fc-bga-market-global-forecast "FC-BGA market forecast"
