---
title: FP Superior · Administración
description: "Ejemplos de IA en Administración y Finanzas: documentos, plazos administrativos y tutor de normativa."
---

<div class="module-meta">
  <span>CFGS Administración y Finanzas</span>
  <span>Nivel profesional</span>
  <span>Normativa y plazos</span>
</div>

## Qué cambia en Administración

- El resultado debe ser **jurídicamente correcto**, no solo estar bien redactado.
- La IA puede confundir normativa vigente con derogada, o aplicar una regla de otra administración.
- Los datos de empresas y personas son sensibles: se trabaja siempre con supuestos ficticios o anonimizados.
- La evaluación debe exigir la norma aplicable y el cálculo del plazo, no la plantilla bonita.

## Ejemplo 1 — Borrador de requerimiento con plantilla (Módulo 1)

**Contexto:** el alumnado debe redactar un requerimiento de subsanación a una empresa ficticia por documentación incompleta.

<div class="prompt-box">
<span class="label">Prompt</span>
Actúa como técnico de administración de una oficina de subvenciones.

Contexto: adjunto la plantilla oficial, la lista de documentación exigida y el expediente ficticio de la empresa «Ejemplo S. L.». Falta el certificado de estar al corriente de pagos y la memoria económica está sin firmar.

Tarea: redacta un borrador de requerimiento de subsanación de 250 palabras.

Formato: membrete, datos del expediente, hechos, documentación que falta, plazo y advertencia de archivo.

Restricciones: usa solo la plantilla y la normativa adjunta; no inventes artículos ni plazos. Si el plazo no consta, escribe «plazo según normativa aplicable» y avísame.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Un borrador con los datos del expediente, la lista exacta de documentos, el plazo respaldado por la norma adjunta y una advertencia de archivo. Ninguna referencia legal inventada.
</div>

**Comprobación:** cada plazo y cada artículo se contrasta con la normativa adjunta. El documento se compara con la plantilla oficial antes de darlo por válido.

<div class="teacher-note">
  <strong>Nota docente</strong>
  La IA tiende a rellenar el hueco del plazo con una cifra plausible. Ese es el error que hay que cazar en clase: que el alumnado localice la regla y la cite.
</div>

## Ejemplo 2 — Tutor de plazos y silencio administrativo (Módulo 3)

**Contexto:** preparación de un examen de «Gestión de documentación jurídica» con supuestos prácticos.

<div class="prompt-box">
<span class="label">Prompt del tutor</span>
Actúa como tutor de Gestión de Documentación Jurídica de FP Superior de Administración.

Usa solo la normativa y los apuntes adjuntos. Empieza con un supuesto práctico de plazos. Corrige mi respuesta, indica el artículo o la regla aplicable y no me des la solución antes de que responda.

Cuando acierte, sube la dificultad con un caso de silencio administrativo. Al final, hazme tres preguntas de repaso y dime qué debo volver a estudiar.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Preguntas encadenadas, correcciones con la norma aplicable y un cierre con tres puntos débiles. Debe negarse a resolver el supuesto antes del intento del alumnado.
</div>

**Comprobación:** cada corrección se contrasta con el texto legal adjunto. Si el tutor cita un artículo inexistente, se descarta la corrección y se anota el fallo.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Grábate esta regla: un tutor que cita artículos con seguridad pero sin fuente es más peligroso que uno que dice «no lo sé». Enseña a preguntar «¿en qué artículo te basas?».
</div>

## Ejemplo 3 — Cuaderno de normativa para toda la unidad (Módulo 2)

**Contexto:** la unidad mezcla una ley, un reglamento y varios modelos oficiales. El grupo se pierde entre fuentes.

<div class="prompt-box">
<span class="label">Prompt en NotebookLM</span>
Con la ley, el reglamento y los modelos de este cuaderno:

1. Haz un mapa de qué regula cada norma y cómo se relacionan.
2. Lista los plazos que aparecen, con el artículo y la fuente.
3. Prepara cinco supuestos breves y la norma que se aplicaría en cada uno.
4. Señala las contradicciones o remisiones que no se puedan resolver con estas fuentes.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Un mapa de normas con citas, una tabla de plazos con artículo y cinco supuestos con la norma aplicable. Las remisiones sin respuesta se marcan como pendientes.
</div>

**Comprobación:** se abren los artículos citados y se comprueba el plazo. Los supuestos se resuelven en grupo y se comparan con la solución del docente.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Este cuaderno ahorra tiempo de búsqueda, pero no sustituye la lectura de la norma. Pide que cada grupo localice el artículo en el BOE o en el boletín correspondiente.
</div>

## Qué evitar en este nivel

| Práctica | Riesgo | Alternativa |
| --- | --- | --- |
| Aceptar artículos sin abrir la norma | Errores jurídicos graves | Cita obligatoria y verificación |
| Usar expedientes reales | Protección de datos | Supuestos ficticios o anonimizados |
| Confundir plantilla con fundamento | Documento correcto por fuera, vacío por dentro | Exigir hecho, norma y plazo |
| Automatizar el envío de requerimientos | Comunicación oficial sin control | Borrador + revisión humana |

## Módulos relacionados

- [Módulo 1 · Habla con la IA](/modulos/1-habla-con-la-ia/)
- [Módulo 2 · Sistema de estudio](/modulos/2-sistema-de-estudio/)
- [Módulo 3 · La IA como profesor](/modulos/3-ia-como-profesor/)
