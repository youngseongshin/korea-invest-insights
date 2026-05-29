---
title: "Cómo se crea este blog: presentamos Thesis OS, nuestro sistema operativo de investigación de código abierto"
date: 2026-05-30T11:00:00+09:00
description: "Las publicaciones de Korea Invest Insights no se escriben una a una desde cero: se producen a través de una estructura llamada Thesis Investment OS. Alpha reúne la evidencia, Lattice convierte esa evidencia en juicio y Arki mantiene sano todo el sistema. Juntos, estos tres roles forman un sistema operativo de investigación de código abierto. Este artículo explica esa estructura en términos sencillos y te invita a visitar el repositorio de GitHub."
categories: ["Tools"]
tags:
  - "Thesis OS"
  - "código abierto"
  - "metodología de investigación"
  - "investigación de inversiones"
  - "Alpha"
  - "Lattice"
  - "Arki"
  - "Research OS"
  - "GitHub"
slug: thesis-os-open-source-research-operating-system-2026-05-30
draft: false
---

> 🔗 <strong>Ir al repositorio</strong>: <strong>[github.com/youngseongshin/thesis-investment-os](https://github.com/youngseongshin/thesis-investment-os)</strong> — el sistema de código abierto que impulsa la investigación de este blog

El artículo de hoy es un poco distinto de lo habitual. No trata de una acción, sino de <strong>cómo se crean realmente las publicaciones de este blog</strong>. Permíteme correr el telón por un momento.

![Arquitectura de Thesis Investment OS — un sistema operativo de investigación donde Alpha, Lattice y Arki se entrelazan](thesis-os-architecture.png)

## Lo que hace falta para producir una sola publicación

Las publicaciones de Korea Invest Insights no las improvisa una persona frente a una pantalla en blanco. Detrás de ellas funciona un pequeño sistema operativo llamado <strong>Thesis Investment OS</strong>. El nombre suena grandioso, pero la idea es simple.

> Hacer que el juicio de inversión sea <strong>visible, comprobable y honesto sobre su propio historial.</strong>

No es un bot de trading automático, ni un servicio que vende señales, ni una "IA que elige acciones por ti". Es un <strong>marco de trabajo</strong> que reúne información de mercado dispersa en una tesis, y que te permite volver más tarde para comprobar si esa tesis resultó acertada o equivocada.

La estructura se divide en tres roles. Imagínalos como tres personas de un mismo equipo.

---

## 1. Alpha — quien reúne la evidencia

Alpha es el rol que <strong>recopila y verifica los hechos.</strong>

- <strong>Datos cuantitativos</strong>: precios, volumen, flujos, fundamentales, informes regulatorios
- <strong>Datos cualitativos</strong>: noticias, informes, transcripciones de resultados, señales de la comunidad
- Filtrar candidatas con escáneres y luego añadir contexto para destacar valores que merecen seguimiento

Lo que produce Alpha son registros de evidencia, instantáneas de mercado, alertas intradía, candidatas de escáner y paquetes de investigación. En resumen, es quien <strong>apila con honestidad "lo que pasó."</strong> Todavía no juzga. Solo reúne la materia prima.

---

## 2. Lattice — quien construye el juicio a partir de la evidencia

El nombre Lattice viene de la idea de Charlie Munger sobre una <strong>"red de modelos mentales" (latticework of mental models)</strong>: una mente formada por muchos marcos entrelazados.

Su rol es tomar el material que reunió Alpha y convertirlo en una decisión de inversión real.

- Registrar una tesis y organizarla en una tarjeta de decisión
- Ejecutar una revisión de <strong>abogado del diablo</strong> que argumenta deliberadamente la otra cara
- Anotar predicciones en un registro de predicciones y volver a revisarlas más tarde para ver si se sostuvieron

La estructura que lees en el blog — "esta es la conclusión", "esto es un hecho y esto es especulación" — sale directamente de Lattice. La clave es <strong>tomar una decisión, pero dejarla en una forma que puedas calificar después.</strong>

---

## 3. Arki — quien mantiene el sistema en marcha

Arki es el rol menos visible y quizá el más importante. Es quien <strong>mantiene sano todo el sistema.</strong>

- Definir los esquemas que contienen los datos y la disposición del repositorio (vault) que los almacena
- Gestionar los trabajos recurrentes y ejecutar chequeos de salud
- Llevar registros de migración y gobernar los permisos y las reglas de cada rol

Si el sistema fuera una casa, Arki es quien se asegura de que la electricidad, el agua y la calefacción sigan funcionando mientras Alpha y Lattice trabajan. No es glamoroso, pero sin Arki los otros dos no durarían mucho.

---

## Lo que han producido estos tres roles — ejemplos reales

En palabras suena abstracto, así que aquí tienes dos publicaciones recientes que pasaron por este sistema.

- [Resultados del 1T de Dell y la lectura del margen de servidores de IA en Corea](/es/post/dell-q1-fy2027-earnings-korea-ai-server-margin-readthrough-2026-05-29/) — Alpha reunió las cifras de resultados de Dell y Lattice las conectó con la cadena de valor de semiconductores y servidores de Corea para formar una visión.
- [Resultados de Marvell del 1T FY2027 y la lectura para los semiconductores coreanos](/es/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/) — el mismo flujo: partiendo de las cifras de silicio personalizado de Marvell y llevándolas a una lectura para Corea.

Ambas publicaciones separan "esto es un Hecho, esto es una Inferencia, esto es Especulación". Ese hábito es exactamente la estructura que impone Lattice, y los hechos que la sostienen son los que reunió Alpha.

---

## Por qué publicar esto

Cuando investigas durante el tiempo suficiente, lo más aterrador es <strong>"no recordar lo que dijiste antes."</strong> Abundan las tesis que lucen bien; volver a comprobar si de verdad acertaron es tedioso e incómodo. Por eso la mayoría de los análisis se escriben una vez y se olvidan.

Thesis OS incorpora esa incomodidad al sistema a propósito. A cada juicio se le adjunta evidencia, cada predicción se registra y todo se califica después. No porque sea perfecto, sino porque está construido para que <strong>cuando se equivoque, puedas verlo.</strong>

El sistema está diseñado para ejecutarse de forma local. Puedes probarlo con los datos de muestra incluidos: no se requieren claves de API, accesos de bróker ni fuentes de pago. La licencia es MIT y necesita Python 3.10 o más reciente.

Y los tres canales por los que este sistema publica son justamente estos: el <strong>blog (Korea Invest Insights)</strong> que estás leyendo, <strong>Telegram @korea_invest_insights</strong> y <strong>Substack</strong>.

---

## Ven a echar un vistazo

El objetivo de este artículo no es presumir, sino invitar. Si alguna vez te has preguntado cómo hacer que la investigación de inversiones sea más honesta y más comprobable, asómate.

> No tienes que leer todo el código. Incluso hojear el README debería darte una idea de "ah, así es como se crean estas publicaciones del blog."

👉 <strong>[github.com/youngseongshin/thesis-investment-os](https://github.com/youngseongshin/thesis-investment-os)</strong>

Una estrella es bienvenida, pero solo curiosear la estructura también está bien. Hay una sola razón para correr el telón: <strong>para que puedas ver por ti mismo de dónde y cómo salen los juicios de este blog.</strong>

---

*Aviso: solo con fines de investigación e información. No es asesoramiento de inversión personalizado. El sistema de código abierto descrito es una herramienta de investigación; los lectores son responsables de sus propias decisiones de inversión y de sus resultados.*
