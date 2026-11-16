---
title: Bachillerato
description: "Ejemplos de IA en Bachillerato: comentario de texto, sistema de estudio de Biología y trabajo de investigación."
---

<div class="module-meta">
  <span>1.º–2.º Bachillerato</span>
  <span>16–18 años</span>
  <span>Autonomía alta</span>
</div>

## Qué cambia en Bachillerato

- El alumnado puede usar varias herramientas a la vez y suele tener cuenta propia.
- La evaluación pesa más: trabajos, comentarios y pruebas de acceso.
- La integridad académica es el punto crítico: la IA puede mejorar un texto hasta hacerlo irreconocible.
- Es el nivel donde tiene más sentido enseñar **verificación de fuentes** y **declaración de uso**.

## Ejemplo 1 — Comentario de texto sin que lo escriba la IA (Módulo 1)

**Contexto:** 2.º de Bachillerato, comentario de un texto argumentativo sobre redes sociales. La tentación es pedir el comentario entero.

<div class="prompt-box">
<span class="label">Prompt</span>
Actúa como profesor de Lengua Castellana de 2.º de Bachillerato.

Te adjunto un texto argumentativo y la rúbrica del comentario.
No escribas el comentario. Hazme preguntas para que lo construya yo:
1. Cinco preguntas sobre estructura y tesis.
2. Tres preguntas sobre recursos expresivos, con la pista de dónde mirar.
3. Dos preguntas de valoración crítica que exijan argumento propio.
Después de que yo responda, corrige solo lo que esté mal y señala qué falta según la rúbrica.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Una batería de preguntas ordenadas por dificultad, sin párrafos redactados. La corrección posterior debe referirse a la rúbrica y no reescribir el comentario.
</div>

<div class="example-answer">
<span class="label">Ejemplo de respuesta</span>
<p><strong>Preguntas sobre estructura y tesis</strong></p>
<ol>
<li>¿Dónde aparece la tesis y con qué fórmula se introduce?</li>
<li>¿Qué párrafo funciona como introducción y cuál como conclusión?</li>
<li>¿Qué dos argumentos sostienen la tesis? Cita la línea donde empieza cada uno.</li>
<li>¿El texto presenta una sola postura o contrasta dos? Señala el giro.</li>
<li>¿La conclusión repite la tesis o añade una consecuencia?</li>
</ol>
<p><strong>Recursos expresivos</strong></p>
<ol>
<li>Busca una metáfora en el segundo párrafo. ¿Qué término real sustituye?</li>
<li>Localiza una interrogación retórica y explica a quién interpela.</li>
<li>¿Hay enumeración o paralelismo? Copia el fragmento y di qué efecto busca.</li>
</ol>
<p><strong>Valoración crítica</strong></p>
<ol>
<li>¿Qué dato o experiencia falta para que el argumento sea convincente?</li>
<li>¿Qué objeción pondrías a la tesis y cómo la responderías con el propio texto?</li>
</ol>
</div>

**Comprobación:** el comentario final se lee en voz alta y se compara con la rúbrica. Si alguna frase no se puede defender, se elimina.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Este patrón sirve para cualquier comentario de texto. La clave está en la orden «no escribas el comentario»: sin ella, la herramienta produce un texto correcto que el alumnado no sabe justificar.
</div>

## Ejemplo 2 — Sistema de estudio de Biología (Módulo 2)

**Contexto:** 1.º de Bachillerato, tema de metabolismo y enzimas. Tres fuentes: apuntes, capítulo del libro e infografía.

<div class="prompt-box">
<span class="label">Prompt en NotebookLM</span>
Usa exclusivamente las tres fuentes de este cuaderno.

1. Resumen de 300 palabras con una cita por idea principal.
2. Tres conceptos que se confunden entre sí y su diferencia en dos líneas.
3. Diez preguntas de respuesta corta ordenadas por dificultad, con la fuente que respalda cada una.
4. Un punto donde las fuentes no coincidan o falte información, si existe.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Resumen con citas, tabla de conceptos confundibles y diez preguntas con referencia. Si las fuentes discrepan en una cifra, debe advertirlo en lugar de sintetizar sin avisar.
</div>

<div class="example-answer">
<span class="label">Ejemplo de respuesta</span>
<p><strong>Extracto del resumen</strong></p>
<p>El metabolismo es el conjunto de reacciones químicas de la célula. Se divide en catabolismo, que libera energía al degradar moléculas, y anabolismo, que la consume al construir otras <em>[cita: apuntes, p. 3]</em>. Las enzimas aceleran estas reacciones y son específicas de cada sustrato <em>[cita: libro, cap. 6]</em>.</p>
<p><strong>Conceptos que se confunden</strong></p>
<ul>
<li><strong>Catabolismo / anabolismo:</strong> degradar y liberar energía frente a construir y consumirla.</li>
<li><strong>Enzima / coenzima:</strong> proteína catalizadora frente a molécula que ayuda a la enzima.</li>
<li><strong>Respiración aerobia / anaerobia:</strong> con oxígeno y mucha energía frente a sin oxígeno y menos energía.</li>
</ul>
<p><strong>Preguntas con fuente</strong></p>
<ol>
<li>¿Qué diferencia hay entre catabolismo y anabolismo? <em>(apuntes, p. 3)</em></li>
<li>¿Por qué una enzima es específica? <em>(libro, cap. 6)</em></li>
<li>¿Qué produce la respiración anaerobia? <em>(infografía)</em></li>
</ol>
<p><em>Aviso:</em> la infografía no indica el rendimiento energético; se escribe «no consta» en lugar de completarlo.</p>
</div>

**Comprobación:** se abren dos citas al azar y se localiza el fragmento. Las preguntas se responden sin mirar y se corrigen con el resumen tapado.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Pide que el alumnado añada a mano una pregunta que la IA no haya hecho. Es una forma rápida de comprobar si ha leído el material o solo lo ha generado.
</div>

## Ejemplo 3 — Trabajo de investigación con fuentes verificadas (Módulos 3 y 4)

**Contexto:** trabajo de investigación de 2.º de Bachillerato. El alumnado tiende a pedir la bibliografía a la IA y a no abrirla.

<div class="prompt-box">
<span class="label">Prompt</span>
Actúa como bibliotecario escolar.

Tema: [tema del trabajo]. Nivel: 2.º de Bachillerato. Extensión: 8 páginas.
1. Propón cinco preguntas de investigación acotadas y distintas entre sí.
2. Para cada pregunta, sugiere dos tipos de fuente (académica, institucional, prensa de referencia) y qué buscar en el catálogo.
3. No inventes títulos, autores ni enlaces. Si no puedes verificar una referencia, escribe «verificar en catálogo».
4. Indica tres criterios para descartar una fuente poco fiable.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Preguntas acotadas, tipos de fuente y criterios de descarte. Ninguna referencia concreta sin verificar. El alumnado debe encontrar las fuentes en el catálogo o en buscadores académicos.
</div>

<div class="example-answer">
<span class="label">Ejemplo de respuesta</span>
<p><strong>Preguntas de investigación</strong></p>
<ol>
<li>¿Cómo se relaciona el uso del móvil antes de dormir con la latencia del sueño en adolescentes?</li>
<li>¿Influye el tipo de contenido (vídeo corto frente a lectura) en la calidad del sueño?</li>
<li>¿Qué diferencias aparecen entre uso pasivo y uso interactivo?</li>
<li>¿Qué papel tienen las notificaciones frente al tiempo total de pantalla?</li>
<li>¿Qué intervenciones escolares han mostrado efecto sobre el descanso?</li>
</ol>
<p><strong>Fuentes y búsqueda</strong></p>
<ul>
<li>Revisión académica: busca en el catálogo «sleep adolescents screen use review».</li>
<li>Organismo oficial: informes de salud pública y guías de sueño.</li>
<li>Prensa de referencia: solo para el contexto social, no para la conclusión.</li>
</ul>
<p><strong>Criterios para descartar una fuente</strong></p>
<ol>
<li>No identifica autor, institución ni fecha.</li>
<li>No explica la muestra o el método.</li>
<li>Confunde correlación con causalidad.</li>
</ol>
<p><em>Referencias concretas:</em> «verificar en catálogo». No se inventan títulos ni enlaces.</p>
</div>

**Comprobación:** cada fuente usada tiene que existir y estar disponible. La bibliografía se revisa con el docente antes de la entrega. Las referencias inventadas eliminan la parte correspondiente.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Convierte la verificación en una entrega intermedia obligatoria: ficha de cada fuente con autor, año, dónde se ha consultado y una frase que aporte al trabajo. Sin ficha, la fuente no cuenta.
</div>

## Qué evitar en este nivel

| Práctica | Riesgo | Alternativa |
| --- | --- | --- |
| Pedir el trabajo completo | Texto correcto sin autoría real | Pedir preguntas, esquemas y revisión |
| Bibliografía generada sin abrir | Referencias inexistentes | Verificar en catálogo y registrar la consulta |
| Declarar la IA solo si se pregunta | Falta de transparencia | Norma clara de declaración desde el inicio |
| Usar detectores como prueba única | Falsos positivos | Proceso, borradores y defensa oral |

## Módulos relacionados

- [Módulo 1 · Habla con la IA](/modulos/1-habla-con-la-ia/)
- [Módulo 2 · Sistema de estudio](/modulos/2-sistema-de-estudio/)
- [Módulo 3 · La IA como profesor](/modulos/3-ia-como-profesor/)
- [Módulo 4 · Tutoría y casos](/modulos/4-tutoria-y-casos/)
