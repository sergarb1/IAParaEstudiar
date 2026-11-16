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
