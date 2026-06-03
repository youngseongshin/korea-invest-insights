---
title: "Seguimiento de Marvell: por qué las fuentes láser EML y CW-DFB importan para los centros de datos de IA"
date: 2026-06-03T17:40:00+09:00
description: "La tesis de conectividad de Marvell y Broadcom baja una capa: las fuentes láser EML y CW-DFB se están convirtiendo en un cuello de botella para 800G, 1.6T, silicon photonics y CPO. En Corea, OE Solutions es el proxy técnico más directo, pero aún necesita pruebas de clientes y pedidos repetidos."
categories: ["Market-Outlook", "Semiconductors", "Sector-Deep-Dive"]
tags: ["Marvell", "Broadcom", "EML", "CW-DFB", "CPO", "ELSFP", "OE Solutions", "AI optical interconnect"]
slug: marvell-follow-up-eml-cw-dfb-laser-source-korea-cpo-2026-06-03
draft: false
---

> Contexto: continuación de [la historia de Marvell y la lectura para Broadcom](/post/marvell-trillion-broadcom-readthrough-korea-ai-connectivity-2026-06-02/) y de [la cadena coreana de óptica/CPO](/post/korea-optical-cpo-value-chain-seven-companies-2026-05-09/).

## Resumen

El punto central no es solo que se vendan más módulos ópticos. El cuello de botella se está moviendo hacia la **fuente de luz**: láseres EML y CW-DFB.

Según datos reportados atribuidos a TrendForce, la capacidad mensual combinada de EML y CW-DFB en 2026 sería de **50.7 millones de unidades**, o **608.4 millones anualizadas**. Como la tabla pública exacta no está disponible en la página inglesa de TrendForce, tratamos esta cifra como dato reportado. Lo que sí está confirmado por TrendForce es la dirección: los transceptores 800G+ podrían pasar de 24 millones de unidades en 2025 a cerca de 63 millones en 2026, y el mercado de transceptores ópticos de IA alcanzaría US$26.000 millones en 2026. ([TrendForce][1], [TrendForce][2])

La lectura para Corea:

| Tipo | Nombre coreano | Lectura |
|---|---|---|
| Proxy técnico más directo | OE Solutions | 100G EML, transceptor 1.6T y ELSFP externo para CPO |
| Visibilidad de contratos | Optocore | Contratos 400G/800G para centros de datos de IA, pero con riesgo financiero/auditoría |
| Flujo táctico actual | Solid, RFHIC, Samji Electronics | Mejor cinta de corto plazo, aunque no son exposición pura a fuente láser |
| Evitar por ahora | Daehan Optical, BWE | Líderes de marzo-abril, pero con distribución y caídas fuertes |

<div class="thesis-callout">
  <div class="thesis-callout__label">Idea clave</div>
  <div class="thesis-callout__body">
    Marvell y Broadcom señalan el cuello de botella de conectividad. La capa inferior es la fuente láser: <strong>EML y CW-DFB</strong>. En Corea, OE Solutions es el proxy técnico más directo, pero la señal invertible requiere certificación de cliente, pedidos repetidos y mejora de márgenes.
  </div>
</div>

Silicon photonics y CPO no eliminan la necesidad de láseres. La desplazan hacia fuentes externas estables, módulos ELSFP, láseres InP y empaquetado óptico. NVIDIA también describe una arquitectura CPO donde los motores ópticos se colocan cerca del ASIC de switch y las fuentes láser externas suministran luz. ([NVIDIA][3])

Conclusión: OE Solutions es el nombre estructural a seguir en Corea, pero no es compra automática. La acción necesita una recuperación clara de 36.000-38.200 won y compras simultáneas de extranjeros e instituciones. Mientras tanto, el flujo táctico es más favorable en Solid, RFHIC y Samji Electronics.

[1]: https://www.trendforce.com/presscenter/news/20251208-12823.html
[2]: https://www.trendforce.com/presscenter/news/20260420-13017.html
[3]: https://developer.nvidia.com/blog/how-industry-collaboration-fosters-nvidia-co-packaged-optics/
