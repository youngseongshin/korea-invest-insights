---
title: "La subida de ARM — el próximo cuello de botella de la IA está en la CPU, los enlaces ópticos y la estabilidad de energía"
date: 2026-05-22T21:40:00+09:00
description: "La subida de ARM no es solo una historia de renacimiento de la CPU. Es una señal de que los cuellos de botella de la infraestructura de IA se desplazan desde la GPU hacia la coordinación por CPU, el movimiento de memoria, los enlaces ópticos, la estabilidad de energía, los sustratos de alta velocidad y las pruebas. La tesis de ARM es real, pero la acción ya descuenta gran parte del escenario de éxito de largo plazo."
categories: ["Market-Outlook"]
tags:
  - "ARM"
  - "Arm Holdings"
  - "Marvell"
  - "NVIDIA"
  - "Samsung Electro-Mechanics"
  - "Samsung Electronics"
  - "SK hynix"
  - "HBM"
  - "Infraestructura de IA"
  - "Cadena de valor de semiconductores"
slug: arm-ai-cpu-rally-korea-semiconductor-value-chain-2026-05-22
draft: false
---

> Serie relacionada:
> [NVIDIA Q1 FY27 e infraestructura coreana de IA](/es/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [Contrato de condensadores de silicio de Samsung Electro-Mechanics](/es/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [MLCC y condensadores de silicio](/es/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/)

*La subida de ARM no dice solamente que “las CPU vuelven a importar”. Dice algo más grande: el servidor de IA deja de ser una caja de GPU y se convierte en un sistema formado por CPU, XPU, HBM, enlaces ópticos, componentes de estabilidad eléctrica, sustratos de alta velocidad y pruebas. ARM es la señal visible. El alfa puede estar en los cuellos de botella que esa señal revela.*

## Resumen

La subida de ARM es un evento de reclasificación: de empresa de regalías de IP móvil a plataforma de CPU para centros de datos de IA. A medida que los agentes de IA se ejecutan de forma continua, llaman herramientas, mueven datos y coordinan GPU, ASIC y memoria, la CPU se convierte en la capa de coordinación del rack.

El catalizador externo fue NVIDIA. La compañía reportó ingresos trimestrales de <strong>81.600 millones de dólares</strong>, ingresos de Data Center de <strong>75.200 millones</strong> y una guía de <strong>91.000 millones ±2%</strong> para el segundo trimestre fiscal de 2027. El mercado lo leyó como aceleración, no como techo del ciclo. ([NVIDIA][1])

La historia propia de ARM también es sólida. En FY26, los ingresos fueron <strong>4.920 millones de dólares</strong>, con <strong>2.610 millones</strong> de regalías, <strong>2.310 millones</strong> de licencias y EPS no-GAAP de <strong>1,77 dólares</strong>. La CPU Arm AGI se presenta como plataforma para centros de datos de IA, con Meta como socio líder, y ARM dijo que la demanda de clientes para FY27-FY28 ya supera los <strong>2.000 millones de dólares</strong>. ([Arm][2])

El problema es el precio. Según Research OS local DB, ARM cerró el 21 de mayo de 2026 en <strong>298,23 dólares</strong>. Frente al EPS no-GAAP de FY26, esto implica unas <strong>168,5 veces</strong> beneficios. La tesis es correcta, pero la acción no es barata.

Por eso la mejor relación riesgo-retorno puede estar fuera de ARM: Marvell en chips personalizados y enlaces ópticos, Samsung Electro-Mechanics en condensadores de silicio, SK hynix y Samsung Electronics en HBM/DRAM, y los fabricantes de sustratos y sockets de prueba.

---

## 1. Qué significa realmente la subida de ARM

Llamarlo “renacimiento de la CPU” es correcto, pero incompleto. El mensaje más importante es que el cuello de botella se mueve.

```text
Escasez de GPU
→ escasez de HBM y empaquetado avanzado
→ cuello de botella en CPU, movimiento de memoria y enlaces ópticos
→ estabilidad de energía, sustratos y pruebas
```

Un agente de IA no es una simple consulta web. Invoca modelos, llama herramientas, lee documentos, consulta bases de datos y guarda resultados intermedios. La GPU calcula; la CPU coordina orden de tareas, memoria, red, seguridad y operación del sistema.

Por eso la CPU se vuelve el plano de control del rack de IA. Si la GPU es el motor, la CPU es la torre de control.

---

## 2. Arm AGI CPU: de proveedor de IP a plataforma de silicio

ARM ha colocado la <strong>Arm AGI CPU</strong> en el centro de su narrativa. La empresa la describe como silicio de producción para centros de datos de IA agentic. Meta es el socio líder, y sistemas comerciales están disponibles a través de ASRock, Lenovo, Quanta y Supermicro. ([Arm][2])

El modelo anterior era:

```text
licencia de IP
→ el cliente diseña y fabrica el chip
→ ARM recibe licencia y regalías
```

El nuevo modelo añade:

```text
IP + subsistemas de cómputo + silicio propio
→ adopción más rápida a escala de centro de datos
→ más control de plataforma
```

El riesgo es el conflicto con clientes. Si ARM vende su propio chip, algunos licenciatarios podrían verla como competidor. Por eso importa el reporte de Bloomberg sobre una investigación de la FTC sobre prácticas de licencia. ([Bloomberg][3])

---

## 3. Valoración: buena tesis, precio exigente

La matemática es incómoda. A <strong>298,23 dólares</strong>, frente a <strong>1,77 dólares</strong> de EPS no-GAAP FY26:

```text
PER no-GAAP FY26 = 298,23 / 1,77 = ~168,5x
```

Con ingresos FY26 de 4.920 millones y capitalización en la zona baja de 300.000 millones, el múltiplo de ventas está en torno a las 60 veces.

Este no es un precio basado en el beneficio actual. Es un precio que descuenta un escenario de 2030-2031: más penetración en CPU de centro de datos, ingresos de AGI CPU, más regalías y expansión de Armv9/Neoverse.

Nuestra postura: <strong>evitar perseguir el precio actual / esperar</strong>.

---

## 4. Alfa 1: Marvell y el cuello de botella de conectividad

Si ARM representa la coordinación por CPU, Marvell representa <strong>cómputo personalizado + conectividad óptica + switching</strong>.

Marvell reportó ingresos FY26 de <strong>8.195 millones de dólares</strong> y EPS no-GAAP de <strong>2,84 dólares</strong>. La empresa espera que FY27 se acerque a 11.000 millones, con el centro de datos liderando el crecimiento y los ingresos de interconexión creciendo más de 50%. ([Marvell][4])

La adquisición de Celestial AI añade una plataforma óptica de scale-up. Marvell espera que ese negocio alcance un ritmo anualizado de 500 millones en FY28 y 1.000 millones en FY29, si se cumplen los hitos. ([Marvell Celestial][5])

El problema es que MRVL también ha subido mucho. Research OS local DB muestra que cerró en <strong>190,69 dólares</strong> el 21 de mayo de 2026. La lectura es <strong>esperar / comprar en retroceso</strong>.

---

## 5. Alfa 2: Samsung Electro-Mechanics y la estabilidad de energía

En Corea, el segundo cuello de botella más claro es Samsung Electro-Mechanics.

El 20 de mayo de 2026, la empresa anunció un contrato de condensadores de silicio por aproximadamente <strong>1,5 billones de wones</strong> durante dos años. Estos componentes se instalan dentro de paquetes de alto rendimiento, como GPU de IA y HBM, para mejorar la estabilidad de suministro eléctrico. ([Samsung Electro-Mechanics][6])

La tesis no es “más MLCC”. Es:

```text
Antes:
MLCC + cámara + FC-BGA

Después:
componentes de estabilidad eléctrica para paquetes de IA
+ FC-BGA
+ MLCC de IA
```

El condensador de silicio no reemplaza todos los MLCC. Es un complemento de alto rendimiento dentro o muy cerca del paquete AI GPU/HBM. Esto puede reclasificar a Samsung Electro-Mechanics como proveedor de componentes de estabilidad eléctrica para paquetes de IA.

---

## 6. Memoria coreana: SK hynix y Samsung Electronics

La subida de ARM también es positiva para memoria. Más CPU de coordinación significa más memoria del lado CPU, más movimiento de datos hacia HBM, más DRAM de servidor y más memoria LPDDR/DDR/CXL.

SK hynix es el ganador HBM más limpio, pero también es la operación más concurrida. Samsung Electronics es una opción de recuperación: HBM4, SOCAMM2, DRAM de servidor, eSSD, base die HBM4 y opción de foundry.

| Empresa | Papel | Lectura |
|---|---|---|
| SK hynix | ganador HBM probado | mantener / comprar en retroceso |
| Samsung Electronics | recuperación HBM + IDM amplio | observar / comprar con confirmación |

---

## 7. Sustratos de alta velocidad y sockets de prueba

A medida que el rack de IA se vuelve más denso, los sustratos y las pruebas ganan valor.

| Capa | Candidatos | Qué verificar |
|---|---|---|
| PCB de alta velocidad | Isu Petasys, Daeduck, TLB, Korea Circuit, Simmtech | ingresos AI, capas, ASP, margen |
| sockets de prueba | ISC, LEENO, TSE | clientes ASIC/HBM/CXL, mix de productos |
| sustratos de paquete | Samsung Electro-Mechanics, Daeduck, Korea Circuit | utilización FC-BGA, certificación, margen |

La regla: <strong>no comprar solo la palabra “AI”. Comprar clientes, pedidos y márgenes verificados.</strong>

---

## Conclusión

ARM es una señal correcta. Los servidores de IA ya no son cajas de GPU; son sistemas de CPU, XPU, HBM, enlaces ópticos, estabilidad de energía, sustratos y pruebas.

Pero perseguir ARM tras la subida puede confundir la señal con el activo. La pregunta importante es qué cuello de botella aún no está totalmente descontado.

<strong>ARM es la señal. El alfa está en los cuellos de botella.</strong>

---

*Este artículo es análisis y comentario, no asesoramiento de inversión. Los precios de ARM y MRVL proceden de Research OS local DB con cierre del 21 de mayo de 2026. Datos de compañías: NVIDIA, Arm, Marvell y Samsung Electro-Mechanics. Fecha de datos: 22 de mayo de 2026 KST.*

[1]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx "NVIDIA Announces Financial Results for First Quarter Fiscal 2027"
[2]: https://newsroom.arm.com/news/arm-q4-fye26-results "Arm delivers record-breaking quarter and full-year results"
[3]: https://www.bloomberg.com/news/articles/2026-05-15/arm-holdings-said-to-face-us-antitrust-probe-over-chip-tech "Arm Holdings Said to Face US Antitrust Probe Over Chip Tech"
[4]: https://d1io3yog0oux5.cloudfront.net/_cde1ddaaf3189b05accbc0f122d6a0c2/marvell/db/3715/35343/pdf/2026_03_05_Marvell_Q4_FY26_financial_business_results_FINAL.pdf "Marvell FY26 and Q4 FY26 Financial and Business Results"
[5]: https://d1io3yog0oux5.cloudfront.net/_a2ff1b1766821fdbdf60a17efbf050dd/marvell/files/pages/marvell/db/3831/description/2025-12_02-Marvell-to-Acquire-Celestial-AI-vF2.pdf "Marvell to Acquire Celestial AI"
[6]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
