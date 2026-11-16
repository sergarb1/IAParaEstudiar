---
title: Módulo 3 · Convierte la IA en tu profesor
description: "Crear un tutor personalizado con GPTs o Gems, aplicar técnicas de estudio y verificar resultados con Compilatio AI."
---

<div class="module-meta">
  <span>2 horas</span>
  <span>Sesión 3</span>
  <span>GPTs · Gems · Compilatio AI</span>
  <span>Requiere cuenta ChatGPT o Gemini</span>
  <a class="module-slides" href="/presentaciones/m03/">Presentación</a>
</div>

<figure class="page-visual is-diagram">
  <div class="page-visual-frame">
    <img src="/imagenes/modulo-3.svg" alt="Secuencia de un tutor: pregunta, intento, pista, explicación y cierre." width="1200" height="630" loading="lazy" />
  </div>
  <figcaption>Esquema propio. El tutor conduce la sesión, pero el esfuerzo y la respuesta son del alumno.</figcaption>
</figure>

## Qué vas a aprender

- Qué es un tutor personalizado y en qué se diferencia de un chat normal.
- Cómo redactar sus instrucciones para que pregunte, corrija y no regale la respuesta.
- Técnicas de estudio que funcionan con IA: recuperación activa, explicación, práctica espaciada.
- Cómo planificar un examen o un trabajo sin delegar el criterio.
- Qué aporta Compilatio AI y qué no puede detectar.

## 1. De chatbot a tutor

Un chat normal responde a lo que le pides. Un **tutor personalizado** (GPT en ChatGPT, Gem en Gemini) es una configuración guardada que define de antemano:

| Componente | Qué se define |
| --- | --- |
| Nombre y descripción | Para qué existe y a quién atiende |
| Instrucciones | Rol, método, tono, qué hace y qué no |
| Conocimiento | Documentos que debe usar (temario, apuntes, rúbricas) |
| Capacidades | Navegación, generación de imágenes, análisis de archivos |
| Conversaciones de prueba | Ejemplos que fijan el comportamiento esperado |

La diferencia es de método: el tutor no espera a que le pidas un resumen, **conduce una sesión de estudio**.

## 2. Instrucciones del tutor

Un tutor útil tiene reglas incómodas a propósito: pregunta antes de explicar, no da la solución, exige la respuesta con palabras propias.

<div class="prompt-box">
<span class="label">Instrucciones del tutor (plantilla)</span>
Eres un tutor de [materia] para [nivel]. Tu objetivo es que el alumno comprenda y recuerde, no que reciba respuestas.

Método de cada sesión:
1. Pregunta qué tema va a trabajar y qué sabe ya.
2. Haz una pregunta de recuperación y espera la respuesta.
3. Si falla, da una pista, no la solución. Si vuelve a fallar, explica en pasos y pide que lo repita con sus palabras.
4. Propón un ejemplo nuevo y una pregunta de aplicación.
5. Cierra con un resumen de tres ideas y dos preguntas para el próximo día.

Reglas:
- Nunca entregues un trabajo listo para copiar; pide primero el intento del alumno.
- Corrige el error concreto y explica por qué está mal.
- Si no sabes algo, dilo y propón cómo comprobarlo.
- Español claro, frases cortas, sin rodeos.
- Adapta el nivel a [curso] y no uses tecnicismos sin explicarlos.

Empieza preguntando por el tema y por el examen o entrega que tiene delante.
</div>

Con ese texto, el tutor deja de ser una máquina de respuestas y se convierte en un examinador paciente.

<figure class="page-visual is-diagram">
  <div class="page-visual-frame">
    <img src="/imagenes/tutor-sesion.svg" alt="Guion de una sesión de tutoría de veinte minutos: diagnóstico, intento, corrección y transferencia." width="1200" height="630" loading="lazy" />
  </div>
  <figcaption>Esquema propio. El tutor no empieza explicando: empieza preguntando y esperando la respuesta.</figcaption>
</figure>

## 3. Técnicas que funcionan

| Técnica | Qué hace la IA | Qué hace el alumnado |
| --- | --- | --- |
| **Recuperación activa** | Formula preguntas, no las responde | Responde de memoria y corrige |
| **Explicación (Feynman)** | Escucha y señala lagunas o imprecisiones | Explica con palabras propias |
| **Práctica espaciada** | Programa repasos en días crecientes | Cumple el calendario |
| **Intercalado** | Mezcla tipos de problemas | Distingue qué estrategia aplicar |
| **Simulacro** | Genera un examen con tiempo y criterios | Lo hace sin apuntes y lo corrige |
| **Autoevaluación** | Compara la respuesta con la rúbrica | Ajusta lo que falta |

<div class="warning">
  La IA puede generar preguntas y corregir, pero la memoria se construye al responder, no al leer. Si el tutor te da la respuesta antes de que lo intentes, la sesión no cuenta.
</div>

<div class="teacher-note">
  <strong>Cuando el tema no entra</strong>
  Una explicación ordenada no siempre basta. Puedes abrir el tema con una analogía cercana (un deporte, una serie, una receta) y volver después al concepto. Tienes ejemplos, prompts y límites en <a href="/recursos/formas-especiales/">Formas especiales de aprender</a>.
</div>

## 4. Preparar un examen

Un plan de examen realista tiene cuatro piezas:

1. **Inventario:** qué entra y con qué peso.
2. **Diagnóstico:** un simulacro inicial para saber qué falla.
3. **Calendario:** repasos distribuidos, no una noche antes.
4. **Corrección:** qué se repite y por qué.

<div class="prompt-box">
<span class="label">Prompt de planificación</span>
Actúa como tutor de [materia] de [nivel].

Contexto: examen el [fecha]. Temario: [lista de bloques]. Dispongo de [minutos] al día y [días] en total. Adjunto la rúbrica o los criterios de calificación.

Tarea: diseña un plan de estudio con repasos espaciados y un simulacro por bloque.
Formato: tabla por día con bloque, técnica, tiempo y pregunta de control.
Restricciones: no planifiques sesiones de más de [minutos]; deja un día libre antes del examen; incluye un día de repaso de errores. Si el plan no cabe, recorta contenido y dilo.
</div>

<figure class="page-visual is-diagram">
  <div class="page-visual-frame">
    <img src="/imagenes/examen-plan.svg" alt="Plan de examen hacia atrás: inventario, bloques débiles, simulacro, errores, descanso y examen." width="1200" height="630" loading="lazy" />
  </div>
  <figcaption>Esquema propio. El plan se construye desde el examen hacia hoy, no desde la urgencia de la última noche.</figcaption>
</figure>

## 5. Documentos académicos

Para un trabajo, la IA sirve sobre todo para **estructurar y revisar**, no para escribir por ti.

- **Antes:** generar un esquema de secciones y una lista de preguntas que el trabajo debe responder.
- **Durante:** revisar coherencia, detectar párrafos repetidos y comprobar el registro.
- **Después:** simular preguntas de defensa y señalar afirmaciones sin fuente.

<div class="checklist">

- Las referencias se comprueban una a una en el catálogo o en la web oficial.
- El marco teórico no se acepta sin leer las fuentes citadas.
- Las conclusiones deben ser tuyas y estar conectadas con los datos.
- El texto final se revisa con corrector y se lee en voz alta.
- Si la IA ha intervenido, se declara según la norma del centro.
</div>

## 6. Compilatio AI y la verificación

Compilatio es un servicio de similitud y detección de contenido generado por IA. Su uso responsable en el aula:

| Uso adecuado | Uso inadecuado |
| --- | --- |
| Herramienta de prevención y diálogo | Prueba única de culpabilidad |
| Revisión formativa con el alumnado | Publicar resultados sin contexto |
| Apoyo a la política de integridad del centro | Sustituir la corrección docente |

Los detectores **no son infalibles**: dan falsos positivos y falsos negativos, y no distinguen por sí solos una ayuda legítima de una copia. La decisión siempre requiere revisar el proceso, el borrador y una conversación con el autor.

> Un porcentaje no es una prueba. La evidencia es el proceso: borradores, fuentes, explicación oral.

## Ejemplo práctico del módulo

**Situación:** el alumnado de Ciclos Formativos de Administración prepara un examen de «Gestión de documentación jurídica» con supuestos de plazos y silencio administrativo.

<div class="prompt-box">
<span class="label">Prompt del tutor</span>
Actúa como tutor de Gestión de Documentación Jurídica (Ciclos Formativos de Administración).

Usa solo la normativa y los apuntes que te adjunto. Empieza preguntándome un supuesto práctico de plazos. Corrige mi respuesta y, si me equivoco, explícame el artículo o la regla que se aplica. No me des la solución antes de que responda. Cuando acierte, sube la dificultad con un caso de silencio administrativo. Al final, hazme tres preguntas de repaso y dime qué debo volver a estudiar.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Una secuencia de preguntas encadenadas, correcciones con la norma aplicable y un cierre con tres puntos débiles concretos. El tutor debe negarse a resolver el supuesto antes de que el alumno lo intente.
</div>

<div class="example-answer">
<span class="label">Ejemplo de respuesta</span>
<p><strong>Tutor:</strong> Supuesto: una solicitud llega incompleta. ¿Qué plazo tiene la persona interesada para subsanar?</p>
<p><strong>Alumno:</strong> Diez días hábiles.</p>
<p><strong>Tutor:</strong> Correcto si la base adjunta lo confirma. Cita el artículo.</p>
<p><strong>Alumno:</strong> Artículo 68.4 de la Ley 39/2015.</p>
<p><strong>Tutor:</strong> Bien. Ahora, solicitud de acceso a información pública sin resolución expresa. ¿Qué efecto produce el silencio?</p>
<p><strong>Alumno:</strong> Depende de la norma sectorial.</p>
<p><strong>Tutor:</strong> Exacto: no se inventa un sentido único. Cierre: repasa el plazo de subsanación, el artículo que lo regula y la regla de silencio de cada procedimiento.</p>
</div>

**Enlace al resultado desarrollado:** [Ejemplo de Ciclos Formativos · Administración](/niveles/fp-administracion/).

**Comprobación:** cada corrección se contrasta con el texto de la norma o con los apuntes. Si el tutor cita un artículo que no existe, se descarta y se anota el fallo.

## Dos ejemplos más, en otras materias

### ESO · Inglés: el tutor que espera

<div class="prompt-box">
<span class="label">Sesión de tutoría</span>
Actúa como tutor de Inglés de 3.º ESO. Hoy trabajamos el past simple.
Hazme una pregunta de recuperación y espera mi respuesta. Si fallo, dame una pista sobre la forma verbal, no la respuesta. Después pídeme una frase nueva con un verbo irregular y cierra con dos preguntas para mañana.
No corrijas la frase entera: señala solo el error concreto.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Una conversación de cuatro o cinco turnos en la que el alumno produce las frases. El tutor señala el error, da una pista y vuelve a pedir el intento; no escribe la frase correcta antes de que el alumno lo intente.
</div>

### Ciclos Formativos · Informática: depuración guiada

<div class="prompt-box">
<span class="label">Sesión de tutoría</span>
Actúa como tutor de Entornos de Desarrollo. Te adjunto un fragmento de código y el mensaje de error.
No me des la corrección. Pregúntame qué esperaba que hiciera el código, pídeme una hipótesis y dame una pista sobre el caso límite. Cuando lo corrija, pídeme explicar por qué funciona y qué prueba añadiría.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Una hipótesis del alumno, una pista que apunta al caso límite y una explicación final propia. El tutor no entrega código completo ni acepta «funciona» como explicación.
</div>

## Cuatro preguntas para comprobar que lo entiendes

1. ¿Qué problema resuelve este concepto?
2. ¿Cómo lo explicarías sin usar la palabra que estás aprendiendo?
3. ¿Dónde está el límite o la excepción?
4. ¿Qué ejemplo nuevo lo demuestra?

Si no puedes responder a las cuatro, vuelve al tema con el tutor. Si las respondes pero necesitas los apuntes, todavía no lo dominas.

## Errores frecuentes

| Error | Por qué falla | Alternativa |
| --- | --- | --- |
| Un tutor que da las respuestas | El alumnado aprende a preguntar, no a saber | Instrucción explícita de no resolver |
| Instrucciones genéricas | Se comporta como un chat cualquiera | Rol, método, reglas y cierre definidos |
| Subir el temario y no probar el tutor | Comportamiento imprevisible en clase | Conversaciones de prueba antes de compartirlo |
| Usar el detector como juez | Falsos positivos y clima de sospecha | Revisar proceso y hablar con el alumnado |
| Planificar sin diagnóstico | Se repasa lo que ya se sabe | Simulacro inicial y repaso de errores |

## Adaptación por niveles

- [ESO](/niveles/eso/): tutor de vocabulario y preguntas de repaso.
- [FP Básica](/niveles/fp-basica/): instrucciones de taller y comprensión paso a paso.
- [Bachillerato](/niveles/bachillerato/): simulacro de examen y comentario de texto.
- [Ciclos Formativos · Informática](/niveles/fp-informatica/): depuración guiada y revisión de código.
- [Ciclos Formativos · Administración](/niveles/fp-administracion/): supuestos de plazos y normativa.
- [Ciclos Formativos · Comercio](/niveles/fp-comercio/): objeciones de venta y análisis de campañas.
- [Ciclos Formativos · Turismo](/niveles/fp-turismo/): protocolo y resolución de incidencias.

## Para el docente

<div class="teacher-note">
  <strong>Idea que debe quedar clara</strong>
  Un tutor personalizado es una metodología disfrazada de herramienta. Si sus instrucciones no obligan a esforzarse, no es un tutor: es un buscador con conversación.
</div>

### Guion de la sesión (120 min)

| Tiempo | Actividad | Notas |
| --- | --- | --- |
| 10 min | Repaso: qué cuaderno funcionó y qué no | Pedir un ejemplo de cita verificada |
| 15 min | Demostración de un GPT/Gem configurado | Mostrar instrucciones y conocimiento |
| 20 min | Escribir las instrucciones del tutor en parejas | Usar la plantilla del apartado 2 |
| 25 min | Probar el tutor con tres preguntas y ajustar | Detectar si regala respuestas |
| 20 min | Técnicas: simulacro cronometrado y corrección | Probar recuperación activa en vivo |
| 15 min | Compilatio AI y política de integridad | Debatir el uso de detectores |
| 10 min | Cierre y transferencia al aula | Cada participante anota una actividad |
| 5 min | Dudas | — |

### Dudas previsibles

- **«¿Se puede compartir el GPT con el alumnado?»** Sí, con enlace y con conocimiento cargado. Revisa antes que no incluya datos personales ni material con derechos.
- **«¿El tutor sustituye mis explicaciones?»** No. Sirve para practicar y detectar lagunas; la explicación docente sigue siendo la referencia.
- **«¿Compilatio detecta todo?»** No. Detecta señales, no intenciones. Úsalo como parte de un proceso.
- **«¿Y si el alumnado copia del tutor?»** Si el tutor pide intentos y el trabajo se defiende oralmente, copiar deja de ser rentable.

### Evaluación formativa

- Entrega de **un tutor configurado** (instrucciones + una fuente) y una transcripción breve de una sesión de prueba.
- Se valora que el tutor pregunte, corrija y cierre con un plan; no que genere materiales bonitos.
- Comprobación: el participante explica por qué su tutor no da respuestas directas.

### Materiales

- Cuenta gratuita de ChatGPT o Gemini.
- Temario o apuntes de una unidad en PDF.
- Rúbrica de una tarea real para probar la corrección.
