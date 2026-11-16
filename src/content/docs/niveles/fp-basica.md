---
title: FP Básica
description: "Ejemplos de IA en FP Básica con lenguaje claro y apoyo a la comprensión."
---

<div class="module-meta">
  <span>FP Básica</span>
  <span>15–17 años</span>
  <span>Muy guiado</span>
</div>

## Qué cambia en FP Básica

- La dificultad principal no suele ser la herramienta, sino la comprensión de instrucciones escritas.
- Muchas tareas son procedimentales: taller, almacén, instalaciones, servicios.
- El alumnado responde mejor con ejemplos visuales, pasos numerados y frases cortas.
- La IA puede ayudar a **traducir el lenguaje técnico a lenguaje claro**, pero no a sustituir la práctica.

## Ejemplo 1 — Convertir un procedimiento en pasos claros (Módulo 1)

**Contexto:** taller de FP Básica. El procedimiento de cambio de aceite está escrito en un lenguaje que el grupo no termina de seguir.

<div class="prompt-box">
<span class="label">Prompt</span>
Actúa como formador de taller de FP Básica.

Te copio el procedimiento oficial de cambio de aceite. Reescríbelo para un alumno de 16 años:
- máximo 8 pasos, una frase por paso;
- lenguaje de uso diario, sin siglas sin explicar;
- incluye el EPI necesario en cada paso;
- añade una advertencia de seguridad al final.

No omitas ningún paso del original. Si algo no queda claro, pregúntame antes de inventarlo.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Ocho pasos numerados con el EPI al inicio de cada uno, sin tecnicismos innecesarios y con una advertencia final sobre residuos y temperatura del aceite. Debe conservar el orden del procedimiento original.
</div>

<div class="example-answer">
<span class="label">Ejemplo de respuesta</span>
<p><strong>Cambio de aceite · 8 pasos</strong></p>
<ol>
<li>Ponte guantes y gafas, y asegura el vehículo con el freno de mano.</li>
<li>Arranca el motor dos minutos y apágalo: el aceite caliente sale mejor, pero quema.</li>
<li>Coloca el recipiente bajo el tapón y retira el tapón de vaciado.</li>
<li>Cambia el filtro con guantes y gafas.</li>
<li>Limpia el asiento del tapón, pon una junta nueva y colócalo.</li>
<li>Rellena con el aceite indicado y comprueba la varilla.</li>
<li>Arranca, comprueba que no hay fugas, apaga y vuelve a mirar el nivel.</li>
<li>Etiqueta el aceite usado y límpialo todo antes de guardar.</li>
</ol>
<p><strong>Atención:</strong> el aceite usado es residuo peligroso. No lo tires al desagüe y no toques el motor caliente.</p>
<p><em>Antes de usar:</em> compara estos pasos con el procedimiento oficial del taller; si falta una comprobación, se añade a mano.</p>
</div>

**Comprobación:** se compara paso a paso con el procedimiento oficial. Si la IA ha añadido un paso que no existe o ha eliminado una comprobación de seguridad, se corrige a mano.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Este ejercicio sirve para trabajar la lectura comprensiva, no solo el taller. Pide al grupo que detecte qué paso se había perdido en la versión de la IA: encontrar el error es parte del aprendizaje.
</div>

## Ejemplo 2 — Cuaderno de seguridad y materiales (Módulo 2)

**Contexto:** el grupo maneja varias fichas de datos de seguridad y normas del taller. Se quiere un material de repaso con citas.

<div class="prompt-box">
<span class="label">Prompt en NotebookLM</span>
Con las fichas de seguridad y las normas del taller de este cuaderno:

1. Haz una tabla con producto, riesgo principal y EPI obligatorio.
2. Escribe cinco situaciones de riesgo reales del taller y qué hacer en cada una.
3. Indica la fuente de cada respuesta.
4. Si una ficha no dice el EPI, escribe «no consta» y no lo completes.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Una tabla de productos y riesgos con citas, y cinco situaciones redactadas en lenguaje claro. Las casillas sin información deben quedar marcadas, no rellenas por suposición.
</div>

<div class="example-answer">
<span class="label">Ejemplo de respuesta</span>
<p><strong>Tabla de productos</strong></p>
<ul>
<li><strong>Disolvente:</strong> inflamable e irritante. EPI: guantes y gafas; trabajar con ventilación.</li>
<li><strong>Aceite hidráulico:</strong> irrita piel y ojos. EPI: guantes y gafas.</li>
<li><strong>Batería:</strong> ácido corrosivo. EPI: guantes, gafas y pantalla facial.</li>
</ul>
<p><strong>Situaciones de riesgo</strong></p>
<ol>
<li>Derrame de disolvente: alejar fuentes de ignición, ventilar y absorber con material adecuado.</li>
<li>Salpicadura en los ojos: lavar con agua abundante y avisar al formador.</li>
<li>Fuga de batería: no tocar el líquido, usar EPI y seguir el protocolo de residuos.</li>
</ol>
<p><em>No consta:</em> el EPI del producto de limpieza de suelos no aparece en la ficha; queda marcado para preguntar al formador.</p>
</div>

**Comprobación:** cada EPI se contrasta con la ficha original. Las situaciones se representan en el taller o se dramatizan para comprobar que se entienden.

<div class="teacher-note">
  <strong>Nota docente</strong>
  No uses este cuaderno como única fuente de seguridad. La norma del taller y la ficha física mandan. La IA organiza la información; la validación es del formador.
</div>

## Ejemplo 3 — Repaso guiado antes de una prueba (Módulo 3)

**Contexto:** prueba de «Operaciones auxiliares de almacén». El grupo necesita practicar preguntas cortas.

<div class="prompt-box">
<span class="label">Prompt del tutor</span>
Eres un tutor de Operaciones Auxiliares de Almacén para FP Básica.

Hazme una pregunta cada vez sobre: tipos de palés, señalización, orden y limpieza, y EPI. Espera mi respuesta. Si fallo, dame una pista y luego explícame la respuesta en dos frases. Si acierto, dime por qué está bien y pasa a otra pregunta.

No me des la lista de respuestas al principio. Al final, dime tres cosas que debo repasar.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Preguntas cortas, pistas antes de la solución y un cierre con tres puntos débiles. Debe evitar tecnicismos que no aparezcan en los apuntes.
</div>

<div class="example-answer">
<span class="label">Ejemplo de respuesta</span>
<p><strong>Tutor:</strong> ¿Qué tipo de palé se usa para carga ligera y apilable?</p>
<p><strong>Alumno:</strong> El europeo.</p>
<p><strong>Tutor:</strong> Bien. ¿Por qué ese y no uno de madera más grande?</p>
<p><strong>Alumno:</strong> Porque es más pequeño y se puede apilar.</p>
<p><strong>Tutor:</strong> Correcto: medidas estándar y buen aprovechamiento del espacio. Siguiente: ¿qué significa una zona rayada en el suelo del almacén?</p>
<p><strong>Alumno:</strong> No lo sé.</p>
<p><strong>Tutor:</strong> Pista: no se puede dejar nada encima. Es una zona de paso o de seguridad.</p>
<p><strong>Cierre:</strong> repasa los tipos de palé, la señalización de zonas y el EPI en el muelle. Mañana te pregunto las tres.</p>
</div>

**Comprobación:** las tres cosas que el tutor manda repasar se buscan en los apuntes y se explican al grupo. Si el tutor se ha inventado un tipo de palé, se corrige y se anota.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Funciona bien en gran grupo con la pantalla proyectada: el tutor pregunta, el grupo responde y el docente modera. Así se evita que cada alumno necesite una cuenta.
</div>

## Qué evitar en este nivel

| Práctica | Riesgo | Alternativa |
| --- | --- | --- |
| Instrucciones largas y técnicas | El grupo abandona la tarea | Frases cortas, ejemplos y pasos numerados |
| Pedir textos extensos | Se copia sin comprender | Pedir preguntas, tablas y comprobaciones |
| Sustituir la práctica de taller | No se adquiere destreza manual | IA para preparar y repasar, no para hacer |
| Cuentas individuales sin control | Edad y privacidad | Cuenta del aula o del centro |

## Módulos relacionados

- [Módulo 1 · Habla con la IA](/modulos/1-habla-con-la-ia/)
- [Módulo 2 · Sistema de estudio](/modulos/2-sistema-de-estudio/)
- [Módulo 3 · La IA como profesor](/modulos/3-ia-como-profesor/)
