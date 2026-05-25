---
title: "El cuello de botella de componentes pasivos en servidores de IA: por qué las piezas pequeñas de energía importan"
date: 2026-05-26
description: "El cuello de botella no es solo la falta de GPU, sino la necesidad de MLCC, capacitores de silicio, inductores y filtros de mayor especificación para estabilizar la energía de sistemas GPU/HBM. La nota explica la tesis para Samsung Electro-Mechanics."
categories: ["Stock-Analysis"]
tags: ["Samsung Electro-Mechanics", "009150", "AI Server", "MLCC", "Silicon Capacitor", "FC-BGA", "Power Integrity", "HBM", "GPU"]
slug: ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26
valley_body_mode: teaser
valley_cashtags: ["삼성전기"]
valley_cashtag_exclude: ["삼성전자", "SK하이닉스"]
---

> Continuación de la serie sobre Samsung Electro-Mechanics. Ver también [SEMCO a KRW 100 billones](/es/post/samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26/), [el contrato de capacitores de silicio](/es/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) y [MLCC vs capacitores de silicio](/es/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/).

## TL;DR

- El cuello de botella de componentes pasivos en servidores de IA no es una historia de GPU, sino de **estabilidad eléctrica**.
- Un rack NVIDIA DGX GB200 consume alrededor de **120kW**, mientras Lenovo cita **135kW TDP** y hasta **155kW pico** para GB300 NVL72. ([NVIDIA][1], [Lenovo][2])
- Los MLCC, capacitores de silicio e inductores actúan como amortiguadores eléctricos: estabilizan, filtran y suavizan la energía que consumen GPU y HBM.
- La oportunidad no está en MLCC genéricos, sino en componentes de servidor de IA con alta capacitancia, bajo ESR/ESL, bajo ruido y perfil ultrabajo.
- Samsung Electro-Mechanics importa porque combina **MLCC + FC-BGA + capacitores de silicio**.

## La idea simple

Un servidor de IA es como un motor de carreras. La GPU es el motor, HBM es el tanque de combustible rápido, el sustrato es la carretera y los MLCC/capacitores de silicio son el control de presión que evita que el motor falle.

TDK describe la ruta de energía de un centro de datos como **UPS → PSU → IBC → VRM → voltaje CPU/GPU**. Cada etapa necesita eficiencia, bajo ripple, tolerancia térmica y confiabilidad. ([TDK][3])

Samsung Electro-Mechanics explica que GPU y CPU operan por debajo de 1V y que la corriente puede cambiar por decenas o cientos de amperios. Por eso los MLCC de alta capacitancia cerca de la GPU funcionan como buffers de corriente. ([Samsung Electro-Mechanics][4])

## MLCC vs capacitor de silicio

| Componente | Ubicación | Función |
|---|---|---|
| MLCC | Placa y zonas cercanas al chip | Estabilización amplia de voltaje |
| Capacitor de silicio | Dentro o muy cerca del paquete GPU/HBM | Supresión ultracercana de transientes |

Samsung Electro-Mechanics anunció un contrato de aproximadamente **KRW 1.5 billones** para capacitores de silicio entre **2027 y 2028**. La empresa afirma que estos componentes mejoran la estabilidad de energía dentro de paquetes de semiconductores de alto rendimiento para servidores de IA. ([Samsung Electro-Mechanics][8])

## Lectura para Samsung Electro-Mechanics

La tesis no es “sube todo MLCC”. La tesis es:

```text
Mayor potencia por rack
  → más picos de corriente
  → más necesidad de power integrity cerca de GPU/HBM
  → MLCC de alta gama, FC-BGA y capacitores de silicio ganan valor
```

Indicadores clave: ASP de MLCC para IA, ramp-up de capacitores de silicio desde 2027, clientes adicionales, crecimiento de FC-BGA para servidores/redes y margen operativo consolidado.

[1]: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[2]: https://lenovopress.lenovo.com/lp2357-lenovo-nvidia-gb300-nvl72-rack-scale-ai
[3]: https://product.tdk.com/en/techlibrary/applicationnote/mlcc-solution-for-data-center-psu.html
[4]: https://product.samsungsem.com/product-news/view.do?idx=3622&language=en
[5]: https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/
[6]: https://www.thelec.net/news/articleView.html?idxno=5588
[7]: https://product.samsungsem.com/product-news/view.do?idx=3742&language=en
[8]: https://m.samsungsem.com/kr/newsroom/news/view.do?id=10309
