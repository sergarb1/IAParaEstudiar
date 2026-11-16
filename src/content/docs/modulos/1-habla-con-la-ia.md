---
title: Módulo 1 · Habla con la IA
description: "ChatGPT, Gemini, Claude y prompting. Elegir la herramienta adecuada, construir instrucciones precisas y verificar los resultados."
---

<div class="module-meta">
  <span>2 horas</span>
  <span>Sesión 1</span>
  <span>ChatGPT · Gemini · Claude</span>
  <span>Sin conocimientos previos</span>
  <a class="module-slides" href="/presentaciones/m01/">Presentación</a>
</div>

<figure class="page-visual is-diagram">
  <div class="page-visual-frame">
    <img src="/imagenes/modulo-1.svg" alt="Esquema de las cinco piezas de una instrucción: rol, contexto, tarea, formato y restricciones." width="1200" height="630" loading="lazy" />
  </div>
  <figcaption>Esquema propio. La instrucción se decide antes de escribir; el modelo no debería rellenar los huecos.</figcaption>
</figure>

## Qué vas a aprender

- Qué hace realmente un modelo de lenguaje y por qué a veces se equivoca con seguridad.
- Para qué sirve cada herramienta y cuál elegir según la tarea.
- La estructura de una instrucción que produce material utilizable.
- Cómo iterar: convertir una primera respuesta mediocre en una buena respuesta.
- Qué comprobar siempre antes de usar un resultado en clase.

## 1. Qué es (y qué no es) un modelo de lenguaje

Un modelo de lenguaje no busca información en una base de datos: **predice qué texto encaja mejor** con lo que le has pedido, a partir de patrones aprendidos en una enorme cantidad de textos. Eso explica sus dos caras:

| Lo que hace bien | Lo que conviene vigilar |
| --- | --- |
| Redactar, resumir, reformular, traducir | Inventar datos, fechas, citas o referencias |
| Proponer estructuras, ejemplos y variantes | Dar por bueno un dato porque suena plausible |
| Adaptar un texto a un nivel o a un formato | Desconocer lo que pasó después de su fecha de corte |
| Mantener el hilo de una conversación | Perder detalle si el contexto es muy largo |

> La IA no «sabe» historia ni matemáticas: genera la respuesta más probable. Tu trabajo es comprobar que esa respuesta es además verdadera.

## 2. Las cuatro herramientas del curso

| Herramienta | Fortaleza principal | Cuándo usarla |
| --- | --- | --- |
| **ChatGPT** | Modelo generalista con espacio de trabajo, archivos, imágenes y GPTs | Redactar, transformar material, crear un tutor propio |
| **Gemini** | Integración con el ecosistema Google (Drive, Docs, Gmail, YouTube) | Trabajar sobre documentos que ya están en Drive o analizar un vídeo |
| **Claude** | Lectura de documentos largos y redacción cuidada | Analizar un temario extenso, revisar un texto propio |
| **NotebookLM** | Responde **solo** con las fuentes que le subes y cita de dónde sale | Estudiar apuntes y documentos propios (módulo 2) |

Las funciones cambian con frecuencia. A fecha de este curso, todas tienen plan gratuito suficiente; si una función ha cambiado, la lógica de la instrucción sigue siendo la misma.

<div class="teacher-note">
  <strong>Nota para el aula</strong>
  No conviertas la sesión en una comparativa de marcas. La pregunta útil es «¿qué tarea tengo delante?», no «¿cuál es mejor?». Las tres primeras herramientas se solapan mucho: elegir una y dominarla vale más que probar cinco.
</div>

## 3. La instrucción importa más que la herramienta

Compara estas dos peticiones sobre el mismo contenido:

<div class="prompt-box">
<span class="label">Instrucción vaga</span>
Hazme un resumen de la Revolución Industrial.
</div>

<div class="prompt-box">
<span class="label">Instrucción precisa</span>
Actúa como profesor de Historia de 4.º de ESO.

Contexto: hemos trabajado la Revolución Industrial en cuatro sesiones. El examen es el viernes y tengo los apuntes en un documento de dos páginas.

Tarea: prepara un plan de repaso de 45 minutos que cubra las causas, los inventos principales y las consecuencias sociales.

Formato: una tabla con tres columnas (bloque, qué repasar, pregunta para comprobar que lo sé).

Restricciones: no inventes fechas ni datos que no aparezcan en el documento que te adjunto; si falta algo, indícalo. Nivel de lengua: claro, frases cortas, sin tecnicismos innecesarios.
</div>

La segunda instrucción no es más larga por lucirse: cada frase elimina una decisión que, si no tomas tú, toma el modelo por su cuenta.

<figure class="page-visual is-diagram">
  <div class="page-visual-frame">
    <img src="/imagenes/prompt-diagnostico.svg" alt="Comparación entre una petición vaga, con cinco decisiones sin resolver, y una petición precisa con nivel, objetivo, formato, límites y prueba." width="1200" height="630" loading="lazy" />
  </div>
  <figcaption>Esquema propio. La petición vaga deja cinco decisiones en manos del modelo; la precisa las toma el docente.</figcaption>
</figure>

## 4. Anatomía de una buena instrucción

| Pieza | Pregunta que responde | Ejemplo |
| --- | --- | --- |
| **Rol** | ¿Desde qué perspectiva habla? | «Actúa como profesor de FP de Administración» |
| **Contexto** | ¿Qué necesita saber para responder? | Curso, materia, nivel, qué se ha dado ya |
| **Tarea** | ¿Qué tiene que producir exactamente? | «Convierte este temario en 20 preguntas de repaso» |
| **Formato** | ¿Cómo lo quiero recibir? | Tabla, lista numerada, guion, 300 palabras |
| **Restricciones** | ¿Qué no puede hacer? | No inventar, no usar tecnicismos, citar fuente |
| **Ejemplo** | ¿Cómo es «bueno»? | «Así es una pregunta bien formulada: …» |

Una plantilla que funciona para casi todo:

<div class="prompt-box">
<span class="label">Plantilla RCTFR</span>
Actúa como [rol concreto].

Contexto: [nivel, materia, qué se ha trabajado, qué material adjunto].

Tarea: [verbo de acción + producto + cantidad].

Formato: [estructura de salida].

Restricciones: [qué evitar, qué citar, longitud, tono].

Antes de responder, hazme dos preguntas si falta información.
</div>

Esa última línea —**pedir que pregunte antes de responder**— es una de las mejoras más rentables. Evita que el modelo rellene los huecos inventando.

## 5. Del prompt al diálogo

Un prompt no es una apuesta única. La conversación es parte del método:

1. **Primera respuesta:** pide el borrador sin obsesionarte con la perfección.
2. **Señala el defecto concreto:** «el apartado 3 es demasiado genérico», no «no me gusta».
3. **Pide variantes:** «dame dos versiones alternativas del apartado 3, una más breve y otra con un ejemplo cotidiano».
4. **Fija lo que funciona:** «conserva la estructura y el tono; cambia solo los ejemplos».
5. **Cierra con una comprobación:** «enumera qué afirmaciones de tu respuesta podrían ser inexactas y cómo verificarlas».

## 6. Verificación: la parte que no se delega

<div class="checklist">

- **Datos y fechas:** contrástalos con el libro de texto, los apuntes o una fuente oficial.
- **Citas y referencias:** abre la fuente. Si no existe o no dice eso, elimínala.
- **Cálculos:** rehazlos a mano o con una calculadora; no aceptes el resultado por bueno.
- **Nombres propios y normativa:** comprueba la denominación actual.
- **Coherencia interna:** ¿el texto se contradice? ¿Promete algo que no cumple?
- **Voz propia:** si no puedes explicarlo sin leerlo, no lo has entendido.
</div>

<figure class="page-visual is-diagram">
  <div class="page-visual-frame">
    <img src="/imagenes/verificacion-datos.svg" alt="Cinco comprobaciones: fecha, cita, cálculo, norma y explicación con palabras propias." width="1200" height="630" loading="lazy" />
  </div>
  <figcaption>Esquema propio. Verificar no es releer: es abrir la fuente, rehacer la cuenta y explicar sin apoyo.</figcaption>
</figure>

## Ejemplo práctico del módulo

**Situación:** una profesora de 4.º de ESO quiere que su alumnado prepare el examen de la Revolución Industrial sin limitarse a releer.

<div class="prompt-box">
<span class="label">Prompt completo</span>
Actúa como profesor de Historia de 4.º de ESO.

Contexto: adjunto los apuntes de la unidad «Revolución Industrial». El examen incluye causas, inventos y consecuencias sociales. Tengo 45 minutos hoy y 30 mañana.

Tarea: diseña un plan de repaso en dos sesiones y, para cada bloque, escribe una pregunta de recuperación activa (sin mirar los apuntes) y la respuesta esperada en dos líneas.

Formato: tabla con columnas bloque, tiempo, pregunta, respuesta esperada.

Restricciones: usa solo la información del documento adjunto. Si un dato no aparece, escribe «no consta en los apuntes» en lugar de completarlo. Español claro, sin siglas.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Una tabla de 6–8 filas con tiempos realistas (por ejemplo, 15 minutos para causas, 15 para inventos, 15 para consecuencias), preguntas que obligan a recordar y respuestas breves que permiten autocorregirse. Si el documento no menciona la mortalidad infantil, la tabla debe decirlo en vez de inventar una cifra.
</div>

<div class="example-answer">
<span class="label">Ejemplo de respuesta</span>
<p><strong>Plan de repaso · Revolución Industrial</strong></p>
<ul>
<li><strong>Causas (15 min).</strong> Pregunta: «¿Qué dos cambios agrícolas favorecieron el crecimiento de la población?» Respuesta: la rotación de cultivos y las mejoras técnicas.</li>
<li><strong>Inventos (15 min).</strong> Pregunta: «¿Qué aportó la máquina de vapor?» Respuesta: una fuente de energía continua que sustituyó la fuerza humana y animal.</li>
<li><strong>Consecuencias (15 min).</strong> Pregunta: «¿Qué dos cambios sociales trajo la fábrica?» Respuesta: crecimiento urbano y aparición de una clase obrera con jornadas duras.</li>
<li><strong>Segunda sesión (30 min).</strong> Repaso oral de las tres preguntas y una pregunta de control sobre el aumento de la producción.</li>
</ul>
<p><em>No consta en los apuntes:</em> mortalidad infantil. No se inventa ninguna cifra.</p>
</div>

**Enlace al resultado desarrollado:** [Ejemplo de ESO · preparar un examen de Historia](/niveles/eso/).

**Comprobación:** el alumnado debe marcar en los apuntes la línea exacta que respalda cada respuesta esperada. Las filas que no se puedan respaldar se eliminan.

## Dos ejemplos más, en otras materias

### Bachillerato · Física: pistas antes que solución

<div class="prompt-box">
<span class="label">Prompt</span>
Actúa como profesor de Física de 1.º de Bachillerato.

Contexto: un alumno ha resuelto mal un problema de plano inclinado y no sé en qué paso se ha perdido. Adjunto el enunciado y su solución.

Tarea: hazme tres preguntas de diagnóstico, de la más básica a la más específica, y una pista para cada una. No escribas la solución completa.

Formato: tabla con pregunta, pista y error que permite detectar.

Restricciones: usa solo el enunciado y la solución adjuntos; si falta un dato, dilo.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Tres preguntas que localizan el fallo —descomposición de fuerzas, signo de la componente o conversión de unidades— y pistas que permiten corregirlo sin entregar el resultado. El alumno vuelve a intentarlo y explica el paso que había fallado.
</div>

### Ciclos Formativos · Comercio: ficha de producto

<div class="prompt-box">
<span class="label">Prompt</span>
Actúa como responsable de una tienda de deporte.

Contexto: quiero preparar una ficha para una mochila de 24 litros dirigida a estudiantes de 16 a 18 años. Adjunto las características reales del fabricante.

Tarea: escribe tres beneficios concretos, dos objeciones habituales con su respuesta y una frase de cierre para la conversación de venta.

Formato: ficha breve con apartados.

Restricciones: no inventes precios, medidas ni materiales; usa solo la ficha adjunta. Tono cercano, sin exageraciones.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Una ficha usable en mostrador, con beneficios ligados a características reales y objeciones respondidas sin promesas falsas. El precio y la garantía se dejan como «consultar» si no constan en la ficha.
</div>

## Errores frecuentes

| Error | Por qué falla | Alternativa |
| --- | --- | --- |
| Pedir «un resumen» sin más | El modelo elige extensión, nivel y enfoque por ti | Indica curso, objetivo, extensión y destinatario |
| Aceptar la primera respuesta | Suele ser genérica y optimista | Itera con defectos concretos |
| Pegar datos del alumnado | Riesgo de privacidad y de tratamiento indebido | Anonimiza siempre |
| Copiar citas sin abrirlas | Las referencias inventadas son el fallo más típico | Verifica cada fuente |
| Usar la IA para evitar pensar | El resultado no se retiene ni se defiende | Usa la IA para practicar y comprobar |

## Adaptación por niveles

- [ESO](/niveles/eso/): plan de repaso de Historia y vocabulario.
- [FP Básica](/niveles/fp-basica/): instrucciones de taller y comprensión lectora.
- [Bachillerato](/niveles/bachillerato/): comentario de texto y problemas de Física.
- [Ciclos Formativos · Informática](/niveles/fp-informatica/): revisión de código y depuración guiada.
- [Ciclos Formativos · Administración](/niveles/fp-administracion/): modelos de documentos y plazos.
- [Ciclos Formativos · Comercio](/niveles/fp-comercio/): fichas de producto y guiones de venta.
- [Ciclos Formativos · Turismo](/niveles/fp-turismo/): itinerarios y atención al visitante.

## Para el docente

<div class="teacher-note">
  <strong>Idea que debe quedar clara</strong>
  La herramienta no piensa por ti: ejecuta lo que le pides. Mejorar la instrucción es mejorar el resultado. Y ningún resultado se usa sin verificar.
</div>

### Guion de la sesión (120 min)

| Tiempo | Actividad | Notas |
| --- | --- | --- |
| 10 min | Pregunta inicial: «¿quién ha usado IA para estudiar esta semana? ¿para qué?» | Sin juicios; sirve para diagnóstico |
| 15 min | Demostración: misma petición vaga y precisa en dos herramientas | Proyectar y comparar en vivo |
| 20 min | Anatomía RCTFR y plantilla | Entregar la plantilla en papel o documento |
| 25 min | Reescribir una instrucción propia en parejas | Cada pareja mejora un prompt real de su materia |
| 20 min | Puesta en común y ejecución de dos prompts | Elegir los que cubran niveles distintos |
| 15 min | Verificación y alucinaciones | Buscar un dato falso a propósito y cazarlo |
| 10 min | Cierre: tres reglas de uso y dudas | Dejar por escrito las reglas del grupo |

### Dudas previsibles

- **«¿Hay que pagar?»** No para este curso. Los planes gratuitos cubren las tareas planteadas; los límites de uso pueden obligar a esperar o cambiar de herramienta.
- **«¿Se puede usar en un examen?»** Depende de la normativa del centro y del diseño de la prueba. La regla del curso: si la actividad evalúa el proceso, la IA puede ayudar; si evalúa lo que sabes sin apoyo, no.
- **«¿Me va a sustituir?»** Sustituye tareas mecánicas, no el criterio docente. La parte que no se automatiza es decidir qué merece aprenderse y cómo comprobarlo.
- **«Mi alumnado la usa a escondidas.»** Mejor enseñar a usarla con condiciones que prohibirla sin más.

### Evaluación formativa

- Cada participante entrega **un prompt antes y después** de aplicar RCTFR, con una frase explicando qué cambió.
- Se valora que la instrucción incluya contexto, formato y una restricción de verificación.
- No se evalúa la «calidad» de la respuesta de la IA, sino la capacidad de detectar sus fallos.

### Materiales

- Ordenador con proyector y conexión.
- Cuenta gratuita creada antes de la sesión en al menos una herramienta.
- Documento de apuntes de una unidad real (anonimizado) para practicar.
