---
layout: cover
---

# Construye tu sistema de estudio

## De tus apuntes a una forma de estudiar con IA

---
class: visual-slide
---

<img src="/imagenes/modulo-2.svg" alt="Esquema del módulo" />

<div class="visual-caption">Tres fuentes entran; resumen, cuestionario y mapa salen con cita.</div>

---
class: compact-slide
---

## Un chatbot que solo lee lo que tú le das

NotebookLM trabaja con **fuentes** que tú subes y responde citando el fragmento.

| Chatbot generalista | NotebookLM |
| --- | --- |
| Conocimiento entrenado | Tus documentos |
| No siempre cita | Cita fuente y fragmento |
| Puede rellenar huecos | Debe ceñirse a lo aportado |
| Crear y transformar | Estudiar y comprender |

<div class="info">
¿La pregunta es «qué dice mi temario»? NotebookLM. ¿Es «ayúdame a redactar»? Un chatbot generalista.
</div>

---
class: compact-slide
---

## Elegir fuentes que merezcan la pena

- Temario, apuntes propios, capítulos, normativa, artículos de referencia.
- Nada de resúmenes de resúmenes.
- PDF con texto: si es un escaneo, pásalo por OCR.
- Nombres de archivo claros: `tema-3-fotosintesis.pdf`.
- Un cuaderno por unidad, no cuarenta fuentes mezcladas.

<div class="warning">
La calidad del cuaderno depende de lo que entra en él. La IA no arregla una fuente mala.
</div>

---
class: visual-slide
---

<img src="/imagenes/fuentes-notebook.svg" alt="Tres filtros para seleccionar fuentes antes de crear el cuaderno" />

<div class="visual-caption">Tres filtros: fuente primaria, texto legible y una sola unidad. Lo que no pasa, fuera.</div>

---

## El flujo de trabajo

<div class="step">
  <div class="step-number">1</div>
  <div class="step-content">Crear el cuaderno con el nombre de la unidad.</div>
</div>

<div class="step">
  <div class="step-number">2</div>
  <div class="step-content">Subir las fuentes y esperar a que se procesen.</div>
</div>

<div class="step">
  <div class="step-number">3</div>
  <div class="step-content">Preguntar pidiendo siempre la cita.</div>
</div>

<div class="step">
  <div class="step-number">4</div>
  <div class="step-content">Generar materiales: resumen, preguntas, mapa, audio.</div>
</div>

<div class="step">
  <div class="step-number">5</div>
  <div class="step-content">Estudiar con los materiales, no con el chat.</div>
</div>

---
layout: image-right
image: /imagenes/nivel-bachillerato.jpg
---

## Tres fuentes, un cuaderno

- Apuntes, libro y normativa en un solo cuaderno.
- Cada idea con su cita; si falta, «no consta».
- El audio y el mapa no sustituyen la recuperación activa.

[Ver el ejemplo de Bachillerato](https://sergarb1.github.io/IAParaEstudiar/niveles/bachillerato/)

---
class: compact-slide
---

## Qué genera y para qué sirve

| Material | Uso | Cuidado |
| --- | --- | --- |
| Resumen | Primera pasada | Pierde matices |
| Guía de estudio | Qué hay que saber | No sustituye al temario |
| Cuestionario | Recuperación activa | Evita preguntas triviales |
| Mapa mental | Relaciones entre ideas | Simplifica jerarquías |
| Audio | Repaso en movimiento | Escuchar no es estudiar |

---
class: compact-slide
---

## Tu sistema de estudio

| Momento | Acción | Herramienta |
| --- | --- | --- |
| Antes de clase | Mapa general del tema | NotebookLM |
| En clase | Apuntes propios y dudas | Papel o móvil |
| Después | Resumen con citas | NotebookLM |
| Dos días después | Cuestionario y fallos | Cuaderno + papel |
| Una semana después | Explicar sin mirar | Sin IA |
| Antes del examen | Simulacro y corrección | Tutor (módulo 3) |

<div class="teacher-note">
<strong>La clave</strong> La IA aparece en los extremos. El centro del sistema sigue siendo leer, escribir y explicar.
</div>

---
class: visual-slide
---

<img src="/imagenes/rutina-repaso.svg" alt="Línea de tiempo de repaso a los cero, dos, siete y catorce días" />

<div class="visual-caption">La IA prepara los materiales y el calendario; la memoria se construye al cumplir los repasos.</div>

---
class: compact-slide
---

## Ejemplo práctico

<div class="prompt-box">
<span class="label">1.º Bachillerato · Biología</span>
Con las tres fuentes de este cuaderno:
1. Resumen de 300 palabras con una cita por idea principal.
2. Tres conceptos que se confunden, con la diferencia en dos líneas.
3. Diez preguntas de respuesta corta, con la fuente que respalda cada una.
4. Avísame si las fuentes no coinciden en algún dato.
</div>

<div class="success">
Resultado: resumen con citas, tabla de conceptos y diez preguntas con referencia. Si hay discrepancia, debe aparecer una advertencia.
</div>

[Ver el ejemplo completo](https://sergarb1.github.io/IAParaEstudiar/niveles/bachillerato/)

---
class: compact-slide
---

## Ejemplo 2 · ESO: vocabulario en contexto

<div class="prompt-box">
<span class="label">3.º ESO · Inglés</span>
Con la lista de vocabulario, el diálogo y mis apuntes:
1. Doce preguntas: seis de significado y seis de uso en una frase nueva.
2. Cita la fuente de cada pregunta.
3. Tres palabras que se confunden, con la diferencia en una línea.
No inventes ejemplos que no estén en las fuentes.
</div>

<div class="success">
Doce preguntas con cita y una tabla de confusiones. Las de uso obligan a producir, no solo a reconocer.
</div>

---
class: compact-slide
---

## Ejemplo 3 · Informática: revisar un repositorio

<div class="prompt-box">
<span class="label">Ciclos Formativos · Entornos de Desarrollo</span>
Con el README, la guía de estilo y dos issues:
Genera un checklist para revisar un pull request de 10 archivos.
Distingue error, riesgo y preferencia. Cita archivo o sección.
No propongas código completo: solo qué revisar y por qué.
</div>

<div class="info">
Un checklist de 8–10 puntos con gravedad, evidencia y acción. Lo que no esté en el repositorio se marca «no consta».
</div>

---
class: compact-slide
---

## Cuando las fuentes no coinciden

| Situación | Qué pedir | Qué haces |
| --- | --- | --- |
| Dos cifras distintas | «Muéstrame ambas, no las sintetices» | Usar la oficial y anotar la diferencia |
| Norma y resumen chocan | «Cita artículo y fecha de versión» | Gana la versión vigente |
| El libro omite algo | «Marca el hueco y la fuente que lo completa» | Completar con apuntes y señalarlo |

---
class: compact-slide
---

## Límites que hay que conocer

- Un PDF escaneado sin OCR da respuestas pobres.
- Mezclar asignaturas produce respuestas vagas.
- Las citas pueden interpretar mal el fragmento: **ábrelo**.
- El audio no sustituye la recuperación activa.
- Copiar el resumen en un trabajo es plagio, no estudio.

<div class="warning">
Comprueba dos citas al azar en cada sesión. Si no respaldan la frase, el material no se usa.
</div>

---
layout: closing
---
