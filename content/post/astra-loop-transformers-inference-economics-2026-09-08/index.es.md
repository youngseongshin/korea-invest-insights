---
title: "Después de Astra: Cómo los Transformers en Bucle Cambian la Economía de la Infraestructura de IA"
slug: "astra-loop-transformers-inference-economics-2026-09-08"
date: 2026-09-08T18:00:00+09:00
description: "Partiendo del ensayo del CEO de Lablup, Jeongkyu Shin, analizamos las investigaciones sobre Huginn, Ouro y MoR para separar la eficiencia de parámetros de los costes de cómputo, memoria y servicio."
categories: ["Tech-Analysis", "Exclusive Analysis"]
tags: ["IA", "Transformers en Bucle", "Astra", "HBM", "Inferencia", "Lablup"]
draft: false
---

¿Puede un modelo pequeño resolver problemas más complejos pasando repetidamente por la misma red neuronal? El CEO de Lablup, Jeongkyu Shin, retoma esta pregunta en su [ensayo de Facebook sobre los transformers en bucle tras Astra](https://www.facebook.com/jeongkyu.shin/posts/pfbid02jm4iibHsgU11P7gY8e4SZKtKYNNdtHF6wdTQK2EdyDeTMEwxiDvHnHyhyAKphLml). Detrás de la cuestión arquitectónica hay una decisión de infraestructura: cuántos aceleradores y cuánta memoria adquirir, y cómo operarlos.

La investigación pública demuestra que un modelo puede mejorar la resolución de problemas manteniendo sus pesos almacenados intactos, ejecutando repetidamente un bloque computacional compartido. Pero la repetición consume tiempo y energía. Un modelo más pequeño no implica automáticamente un servicio más barato.

Este es un análisis independiente motivado por el ensayo de Shin, complementado con artículos originales y tarjetas de modelo. Separamos la interpretación del ensayo sobre Astra de los hechos públicamente establecidos, y tratamos las implicaciones para la industria como análisis condicional. Las fuentes fueron verificadas el 8 de septiembre de 2026.

## Los resultados de Astra no revelan su arquitectura

El anuncio de OpenAI del 3 de septiembre confirma el lanzamiento de GPT-6 Astra y sus mejoras de capacidad. Sin embargo, el [anuncio](https://openai.com/index/gpt-6-astra/) y la [tarjeta del sistema](https://deploymentsafety.openai.com/gpt-6-astra) aquí revisados no revelan una arquitectura de transformer en bucle, el número de recursiones ni los recuentos totales y activos de parámetros.

Por tanto, no tratamos la conexión entre Astra y un diseño al estilo Huginn como un hecho establecido. Las afirmaciones sobre tamaños de 10T/1T del ensayo y la cita sobre AGI también quedan excluidas de las premisas de este análisis. Un mejor rendimiento por sí solo no permite identificar la arquitectura interna.

Aun así, hay razones sólidas para examinar la recurrencia. Los modelos públicos ya muestran intentos de variar la capacidad de parámetros almacenados y el cómputo de inferencia de forma independiente. Ese desarrollo puede evaluarse sin depender del diseño no revelado de un modelo de frontera.

## Almacenar más y computar más tiempo son decisiones distintas

Los parámetros son los pesos numéricos ajustados durante el entrenamiento. Ampliar un modelo generalmente aumenta la cantidad almacenada. La Mezcla de Expertos, o MoE, selecciona algunos módulos expertos para cada entrada, con el objetivo de ejecutar menos cómputo en relación con la capacidad total del modelo.

MoE no surgió únicamente con Switch Transformer. El [artículo de MoE con puertas dispersas de 2017](https://arxiv.org/abs/1701.06538) precedió a [Switch Transformer en 2021](https://arxiv.org/abs/2101.03961), que simplificó el enrutamiento y el entrenamiento a escala. Un recuento total mayor de parámetros tampoco implica necesariamente más capas.

La cadena de pensamiento (CoT) genera tokens intermedios que extienden el contexto para el cómputo posterior. Un modelo en bucle pasa su estado interno de nuevo a través de un bloque con pesos compartidos. El cómputo intermedio no tiene que convertirse en una palabra en cada paso. Estos enfoques también pueden combinarse.

Comparar lo que aporta cada enfoque aclara el compromiso.

| Enfoque | Qué aumenta | Coste potencial |
|---|---|---|
| Modelo más grande | Pesos o capacidad de expertos | Almacenamiento, cómputo activo, comunicación |
| Cadena de pensamiento | Tokens de razonamiento intermedio | Tiempo de generación, contexto y caché |
| Profundidad recurrente | Pasadas a través de un bloque compartido | Cómputo repetido, latencia, gestión de estado |

Esta es una comparación conceptual. La economía real requiere mediciones a precisión, longitud de entrada y condiciones de hardware equivalentes.

## La investigación sobre pensar antes de hablar utiliza mecanismos distintos

Los [tokens de pausa](https://arxiv.org/abs/2310.02226) proporcionan cómputo adicional antes de dar una respuesta. [Quiet-STaR](https://arxiv.org/abs/2403.09629) aprende a generar razonamientos intermedios que ayudan a predecir los tokens siguientes. Su nombre no debe interpretarse como prueba de que utiliza razonamiento continuo no verbal en estado continuo.

[Coconut](https://arxiv.org/abs/2412.06769) retroalimenta el estado oculto final como entrada sin convertirlo en una palabra. Explora la posibilidad de retener alternativas en una representación interna antes de comprometerse con el lenguaje. Esto no es evidencia de conciencia humana ni de pensamiento autónomo continuamente activo.

La investigación sobre profundidad recurrente incluye el [Universal Transformer de 2018](https://arxiv.org/abs/1807.03819), que repite una transformación y puede asignar cómputo de forma diferente entre posiciones. La dificultad está en entrenar una repetición útil: un bloque compartido debe manejar estados de diferentes etapas, y otra pasada debe mejorar el resultado. Los roles de capa en conflicto son una intuición útil, no una explicación universal para cada fallo.

## Copiar capas es distinto a compartir los mismos pesos

[SOLAR 10.7B](https://arxiv.org/abs/2312.15166) de Upstage introdujo el escalado de profundidad, o DUS: copiar capas existentes, eliminar algunas, conectarlas en un modelo más profundo y continuar el entrenamiento. Las copias que comienzan siendo idénticas pueden desarrollar pesos distintos. El modelo resultante almacena más parámetros.

Un modelo recurrente sigue compartiendo los mismos pesos. DUS reutiliza el entrenamiento previo para construir un modelo más profundo; el bucle aumenta la profundidad de ejecución sin una expansión correspondiente en los pesos almacenados. Tratar ambas técnicas como la misma técnica de ahorro de memoria conduce a un modelo de costes incorrecto.

## Leer los números de Huginn y Ouro con sus condiciones de comparación

La [investigación Huginn](https://arxiv.org/abs/2502.05171) de Geiping y colaboradores separa el procesamiento de entrada, un núcleo recurrente y el procesamiento de salida. El núcleo refina el estado interno mediante ejecución repetida. Los autores entrenaron un modelo de 3.500 millones de parámetros con 800.000 millones de tokens e informaron de una mejora en el rendimiento en tareas de razonamiento al aumentar el cómputo recurrente.

La cifra de 50B del resumen requiere atención. Describe mejoras hasta una carga computacional equivalente a 50.000 millones de parámetros. No garantiza la calidad de un modelo de 50B en cada tarea, ni que dicha calidad se obtenga al mismo coste. Un conjunto pequeño de pesos que utiliza más cómputo es un resultado de investigación; la economía del servicio requiere medición por separado.

[Ouro](https://arxiv.org/abs/2510.25741), de ByteDance y colaboradores, se publicó en octubre de 2025. El artículo abarca una familia de modelos de 1.400 y 2.600 millones de parámetros e informa de comparaciones con modelos de hasta 12.000 millones en distintos benchmarks. Sin embargo, la [tarjeta oficial del modelo Ouro-1.4B](https://huggingface.co/ByteDance/Ouro-1.4B) describe ese modelo particular como equivalente a modelos convencionales de 3 a 4B. Afirmar que 1.4B siempre reemplaza a 12B sería exagerar la comparación.

Los recuentos de parámetros deben leerse junto con los datos de entrenamiento, los recuentos de recurrencia y las tareas de evaluación. La aparente eficiencia de inferencia también puede ser consecuencia de una inversión sustancial en preentrenamiento.

## Menos pesos almacenados no eliminan los cuellos de botella de memoria

Consideremos un cálculo ilustrativo. Almacenar 3.500 millones de parámetros a 2 bytes cada uno requiere aproximadamente 7 GB para los pesos. El uso repetido de esos pesos no multiplica su requisito de almacenamiento por el número de recursiones. Esto es aritmética, no una medición del uso total de memoria GPU de Huginn.

La memoria total de inferencia también incluye la caché KV utilizada para reutilizar el contexto previo, los estados intermedios y el espacio de trabajo de ejecución. La [guía de optimización de inferencia de NVIDIA](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/) distingue los pesos y la caché KV como los principales componentes de memoria. Los contextos más largos y un mayor número de solicitudes concurrentes aumentan la presión sobre la caché. Si las cachés pueden compartirse entre pasos recurrentes depende del diseño.

La reutilización de pesos también es diferente a reducir el movimiento de datos. Si los pesos no pueden permanecer en la memoria rápida en chip, otra pasada puede requerir leerlos de HBM de nuevo. La repetición puede incrementar la demanda de ancho de banda junto con el cómputo. Sin examinar la jerarquía de memoria y la implementación, no se puede declarar que el bucle sea la razón por la que HBM se vuelve innecesario.

## El software debe materializar los ahorros de la salida anticipada

[Mixture-of-Recursions (MoR)](https://arxiv.org/abs/2507.10524) varía la profundidad recursiva por token y gestiona el cómputo y el almacenamiento en caché en torno a los tokens aún activos a una profundidad determinada. El objetivo es dirigir el cómputo hacia los tokens más difíciles en lugar de gastarlo en los sencillos.

El servicio hace esto más difícil. Los distintos requisitos de recurrencia entre solicitudes pueden reducir la eficiencia del procesamiento por lotes. Los planificadores necesitan dejar que otro trabajo use los recursos liberados al completarse antes. Este es un desafío operativo anticipado, no un resultado medido para un producto comercial concreto.

La tarjeta del modelo Ouro ofrece un ejemplo concreto. El modelo admite salida anticipada, pero la tarjeta indica que vLLM no admite esta función y en su lugar ejecuta el número completo de recursiones configurado. Una capacidad arquitectónica no se implementa automáticamente en un motor de servicio.

Esto plantea preguntas concretas para empresas de software de infraestructura de IA como Lablup: ¿puede la plataforma procesar en lotes trabajos con distintas profundidades de recurrencia, reutilizar cachés y reducir el tiempo de finalización y el coste energético con calidad equivalente? Estas son preguntas para evaluar una oportunidad, no afirmaciones de que Lablup ya admita esas funciones o haya demostrado crecimiento de ingresos gracias a ellas.

## Los semiconductores coreanos enfrentan tanto el ahorro de recursos como la expansión del uso

Los siguientes son escenarios condicionales para una adopción más amplia de modelos en bucle, no previsiones de resultados.

| Condición | Posible efecto en la industria | Evidencia necesaria |
|---|---|---|
| Menos pesos y menos caché con calidad equivalente | Menor presión de memoria por solicitud | Memoria medida con contexto y concurrencia iguales |
| Más recurrencia en problemas difíciles | Mayor demanda de tiempo de acelerador y energía | Tiempo de GPU y energía por tarea completada con éxito |
| Menor coste amplía el uso | Demanda de infraestructura agregada estable o mayor | Uso real de clientes y planes de compra |
| La recurrencia y la gestión de caché reducen la eficiencia del procesamiento por lotes | Comercialización retrasada | Rendimiento al mismo objetivo de latencia |

Para los proveedores de memoria como Samsung Electronics y SK hynix, la demanda agregada depende tanto de los recursos por solicitud como del número de solicitudes. La eficiencia puede estimular la adopción, pero no puede asumirse que ese crecimiento supere los ahorros. Este análisis por sí solo no es suficiente para revisar las previsiones de demanda de HBM ni los pronósticos de beneficios de las empresas.

Una comparación más útil es el coste de completar una tarea exitosa. Las puntuaciones altas en benchmarks pueden seguir siendo costosas si la repetición lleva demasiado tiempo o los reintentos son frecuentes. Por el contrario, el cómputo adicional puede reducir el coste total si mejora lo suficiente el éxito en el primer intento.

## La próxima prueba es el coste por tarea, no el recuento de parámetros

Verificar el caso industrial requiere comparar la memoria total, el tiempo de finalización, la energía y el rendimiento concurrente con precisión equivalente. La latencia en cola importa tanto como los promedios para las preguntas sencillas. Si más recurrencia deja de mejorar la calidad, o las pérdidas por procesamiento en lotes superan los ahorros de recursos, el argumento de comercialización se debilita.

Una mayor divulgación arquitectónica podría establecer si Astra pertenece a esta línea de investigación. Mientras tanto, un cambio verificable permanece: la planificación de infraestructura debe considerar cuánto tiempo calcular sobre cada problema y cuándo detenerse, junto con el tamaño del modelo almacenado. Convertir esa flexibilidad en costes reales más bajos es una prueba conjunta de hardware y software.
