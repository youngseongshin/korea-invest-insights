---
title: "La divergencia entre la infraestructura de inferencia agente en EE. UU. y China, y la oportunidad de SRAM"
date: 2026-07-09T17:20:00+09:00
description: "Por qué las pilas de inferencia de IA de EE. UU. y China se están separando, y cómo energía, HBM, SRAM/LPU, empaquetado avanzado y empresas coreanas encajan en el mapa."
categories: ["Theme-Analysis", "Korea Semiconductors", "AI Infrastructure"]
tags: ["inferencia de IA", "IA agente", "SRAM", "LPU", "HBM", "Vera Rubin", "LPX", "Samsung Electronics", "SK hynix", "HD Hyundai Electric", "Hanmi Semiconductor"]
slug: us-china-agentic-inference-stack-sram-opportunity-2026-07-09
series: ["hbm", "exclusive-analysis"]
valley_cashtags: ["005930.KS", "000660.KS", "267260.KS", "010120.KS", "298040.KS", "042700.KS", "NVDA"]
draft: false
---

## Resumen

EE. UU. y China están escalando la inferencia de IA, pero no están resolviendo el mismo cuello de botella. En EE. UU. el límite está en energía, densidad de racks, HBM, empaquetado avanzado y rendimiento por megavatio. En China el límite está en acceso a lógica de última generación y HBM, por lo que la respuesta pasa por Ascend, mallas ópticas, escala paralela y jerarquías de memoria domésticas.

Para acciones coreanas, la oportunidad más clara no es asumir automáticamente que las mallas ópticas chinas benefician a proveedores coreanos. La lectura más directa está en la pila estadounidense: HBM4/HBM4E, equipos eléctricos, equipos de empaquetado HBM y la opción menos valorada de Samsung Electronics en fundición SRAM/LPU, almacenamiento de IA y jerarquía de memoria.

## 1. Qué parte de la tesis es verificable

El punto de partida es el artículo de YS-VC sobre la divergencia entre pilas de inferencia de EE. UU. y China. La idea central es correcta: la inferencia ya no es una historia genérica de GPU. Los límites físicos son distintos por región.

| Afirmación | Evaluación | Lectura para inversores |
|---|---|---|
| Las pilas de inferencia de EE. UU. y China se están separando | Mayormente cierto | EE. UU. optimiza energía y eficiencia de rack; China rodea restricciones de lógica y HBM |
| EE. UU. se mueve hacia inferencia con GPU/HBM/SRAM a escala rack | Cierto | Vera Rubin, LPX, HBM4 y SRAM/LPU se integran en un sistema |
| China usa Ascend, malla óptica y jerarquías de memoria propias | Parcialmente cierto | La dirección es plausible, pero CloudMatrix necesita pruebas independientes |
| Los controles de exportación limitan el acceso chino a compute de NVIDIA | Cierto | China no puede depender de acceso estable a GPU y HBM de punta |
| HBM sigue siendo un punto de control clave | Cierto | BIS trata HBM como relevante para entrenamiento e inferencia de IA a escala |

## 2. Por qué se separan las arquitecturas

La IA agente aumenta los tokens. Un agente de código o investigación lee contexto largo, llama herramientas, interpreta resultados y genera nuevas respuestas. Esto hace que prefill, decode, KV cache, almacenamiento, red y energía sean todos relevantes.

| Área | EE. UU. | China |
|---|---|---|
| Límite principal | Energía, densidad de rack, transformadores, HBM4, empaquetado | Lógica avanzada, acceso a HBM, controles de exportación |
| Dirección | Vera Rubin, LPX/LPU, HBM4, racks de alta potencia | Huawei Ascend, malla óptica, escala paralela |
| Fortaleza | Acceso a GPU, HBM y empaquetado líderes | Expansión eléctrica más rápida, infraestructura estatal |
| Debilidad | Conexión a red, tiempo hasta energía, transformadores | Sin lógica EUV de punta, HBM limitado |
| Aterrizaje coreano | HBM, equipos eléctricos, herramientas HBM, fundición | Limitado sin proveedores verificados |

La IEA estima que la demanda eléctrica de centros de datos puede alcanzar unos 945 TWh en 2030. ([IEA][1]) BloombergNEF, citado por Energy Connects, espera que China agregue más de 3,4 TW de capacidad en cinco años, casi seis veces EE. UU. ([Energy Connects][2]) Por eso EE. UU. debe maximizar tokens por megavatio, mientras China puede apoyarse más en expansión paralela de infraestructura.

## 3. La pila estadounidense: HBM más SRAM/LPU

NVIDIA describe LPX como un acelerador de inferencia para Vera Rubin. Combina GPU Rubin con HBM y LPX de Groq 3 con LPU basados en SRAM. ([NVIDIA LPX][3])

| Métrica | Divulgación de NVIDIA LPX |
|---|---:|
| Carga de tokens en sistemas agentes | Hasta 15 veces más tokens |
| Vera Rubin NVL72 + LPX | Hasta 35 veces más throughput por MW |
| SRAM por acelerador LPU | 500MB |
| Ancho de banda SRAM por acelerador | 150TB/s |
| Rack LPX | 256 chips LPU |
| SRAM por rack LPX | 128GB |
| DDR5 por rack LPX | 12TB |
| Ancho de banda SRAM por rack | 40PB/s |

Esto no reemplaza HBM. HBM sigue siendo central para Rubin GPU. SRAM/LPU complementa HBM al acelerar la fase de decode, donde la latencia pesa más.

## 4. China es una señal competitiva, no un trade coreano limpio

Si China no tiene acceso libre a las GPU y HBM más avanzadas, tiene sentido unir más chips, mejorar interconexión y usar mallas ópticas. Pero eso no crea automáticamente ingresos para empresas coreanas. La cadena china es cada vez más local, y los datos de rendimiento y coste total de sistemas como CloudMatrix necesitan verificación externa.

## 5. Mapa de acciones coreanas

| Capa | Cuello de botella | Nombres coreanos | Vista |
|---|---|---|---|
| HBM4/HBM4E | Memoria para Vera Rubin y servidores IA | SK hynix, Samsung Electronics | Beneficio estructural. SK hynix lidera, Samsung es opción de recuperación |
| Fundición SRAM/LPU | Aceleradores de decode de baja latencia | Samsung Electronics | Todavía poco visible en ingresos, pero opción importante |
| Almacenamiento IA/KV cache | Memoria de agentes, eSSD, PCIe 6.0 | Samsung Electronics, FADU | Extensión de la jerarquía de memoria |
| Herramientas HBM | TC bonders, empaquetado avanzado | Hanmi Semiconductor | Cuello real, pero importan clientes y valoración |
| Equipos eléctricos | Transformadores, switchgear, conexión a red | HD Hyundai Electric, LS ELECTRIC, Hyosung Heavy | Exposición directa al cuello de energía de data centers |
| Malla óptica china | Módulos ópticos para clusters chinos | Exposición coreana limitada | Evitar sin pruebas de proveedor |

## 6. Conclusión práctica

| Prioridad | Exposición | Vista |
|---:|---|---|
| 1 | Samsung Electronics | Compra condicional si HBM4E, SRAM/LPU y almacenamiento IA se vuelven visibles |
| 2 | HD Hyundai Electric | Esperar, por calidad alta pero momentum de pedidos ya visible |
| 3 | SK hynix | Esperar, por liderazgo HBM pero trade concurrido |
| 4 | Hanmi Semiconductor | Lista de seguimiento, necesita pedidos repetidos y diversificación |
| 5 | Beneficiarios de malla óptica china | Evitar sin evidencia directa |

La oportunidad coreana no es “malla óptica china”. Es el cuello de botella de la fábrica de IA estadounidense: energía, HBM, SRAM/LPU, empaquetado avanzado y almacenamiento. SK hynix puede tener la mejor posición de negocio, y HD Hyundai Electric la exposición eléctrica más pura. La opción más asimétrica es Samsung Electronics si el mercado deja de verla solo como rezagada en HBM.

## Fuentes

- [YS-VC](https://www.ys-vc.com/blog/us-china-ai-inference-stack-divergence)
- [IEA](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
- [Energy Connects](https://www.energyconnects.com/news/renewables/2026/february/china-ramps-up-energy-boom-flagged-by-musk-as-key-to-ai-race/)
- [NVIDIA LPX](https://www.nvidia.com/en-us/data-center/lpx/)
- [Samsung Newsroom](https://news.samsung.com/global/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026)
- [BIS](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military)
- [Yonhap](https://en.yna.co.kr/view/AEN20260128002800320)
- [The Elec](https://www.thelec.net/news/articleView.html?idxno=11132)
- [Seoul Economic Daily](https://en.sedaily.com/finance/2026/07/06/hd-hyundai-electric-raises-2026-order-target-23-percent-on)
