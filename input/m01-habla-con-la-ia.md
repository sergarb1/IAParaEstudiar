---
layout: cover
---

# Habla con la IA

## ChatGPT, Gemini, Claude y prompting

---
class: visual-slide
---

<img src="/imagenes/modulo-1.svg" alt="Esquema del módulo" />

<div class="visual-caption">Rol, contexto, tarea, formato y restricciones: lo que decides antes de escribir.</div>

---
class: compact-slide
---

## Un modelo no busca: predice

- No consulta una base de datos: **genera el texto más probable**.
- Escribe, resume, reformula y traduce muy bien.
- También **inventa** datos, fechas y citas con total seguridad.
- Su conocimiento tiene una fecha de corte.

<div class="info">
La IA no «sabe» historia ni matemáticas: produce la respuesta más plausible. Comprobar que además es verdadera es tu trabajo.
</div>

---
class: compact-slide
---

## Cuatro herramientas, cuatro tareas

| Herramienta | Fortaleza | Úsala para |
| --- | --- | --- |
| **ChatGPT** | Generalista, archivos, GPTs | Redactar, transformar, crear un tutor |
| **Gemini** | Ecosistema Google | Trabajar con Drive, Docs, vídeos |
| **Claude** | Documentos largos | Analizar un temario extenso |
| **NotebookLM** | Solo tus fuentes, con citas | Estudiar apuntes propios |

<div class="teacher-note">
<strong>En clase</strong> La pregunta útil no es «¿cuál es mejor?», sino «¿qué tarea tengo delante?». Mejor dominar una que probar cinco.
</div>

---

## La instrucción importa más que la herramienta

<div class="comparison-grid">
<div class="comparison-item bad">

### Petición vaga

«Hazme un resumen de la Revolución Industrial.»

El modelo decide nivel, extensión y enfoque por ti.

</div>
<div class="comparison-item good">

### Petición precisa

«Actúa como profesor de Historia de 4.º de ESO. Prepara un plan de repaso de 45 minutos con una pregunta de control por bloque. Usa solo los apuntes adjuntos.»

Tú tomas las decisiones.

</div>
</div>

---
layout: image-right
image: /imagenes/nivel-eso.jpg
---

## Del aula al prompt

- La misma estructura sirve para Historia, Física o un módulo de FP.
- Cambia el contexto y el material; no cambies el método.
- La comprobación sigue siendo tuya.

[Ver el ejemplo de ESO](https://sergarb1.github.io/IAParaEstudiar/niveles/eso/)

---

## Anatomía de una buena instrucción

<div class="step">
  <div class="step-number">1</div>
  <div class="step-content"><strong>Rol:</strong> ¿desde qué perspectiva habla? «Actúa como profesor de FP de Administración».</div>
</div>

<div class="step">
  <div class="step-number">2</div>
  <div class="step-content"><strong>Contexto:</strong> nivel, materia, qué se ha trabajado, qué adjuntas.</div>
</div>

<div class="step">
  <div class="step-number">3</div>
  <div class="step-content"><strong>Tarea:</strong> verbo de acción + producto + cantidad.</div>
</div>

<div class="step">
  <div class="step-number">4</div>
  <div class="step-content"><strong>Formato:</strong> tabla, lista, guion, 300 palabras.</div>
</div>

<div class="step">
  <div class="step-number">5</div>
  <div class="step-content"><strong>Restricciones:</strong> no inventar, citar fuente, tono y límites.</div>
</div>

---
class: visual-slide
---

<img src="/imagenes/prompt-diagnostico.svg" alt="Comparación entre una petición vaga y una precisa" />

<div class="visual-caption">La petición vaga deja cinco decisiones al modelo; la precisa las toma el docente.</div>

---
class: compact-slide
---

## Plantilla RCTFR

<div class="prompt-box">
<span class="label">Copiar y adaptar</span>
Actúa como [rol concreto].
Contexto: [nivel, materia, qué se ha trabajado, material adjunto].
Tarea: [verbo de acción + producto + cantidad].
Formato: [estructura de salida].
Restricciones: [qué evitar, qué citar, longitud, tono].
Antes de responder, hazme dos preguntas si falta información.
</div>

<div class="success">
Pedir que pregunte antes de responder evita que rellene los huecos inventando.
</div>

---
class: compact-slide
---

## Del prompt al diálogo

1. Pide un **borrador**, sin buscar la perfección.
2. Señala el **defecto concreto**: «el apartado 3 es genérico».
3. Pide **variantes**: más breve, con ejemplo cotidiano.
4. **Fija** lo que funciona: «conserva la estructura».
5. Cierra con una **comprobación**: «¿qué debería verificar?».

<div class="info">
Un prompt no es una apuesta única. La conversación es parte del método.
</div>

---
class: compact-slide
---

## Tres ejemplos, tres materias

| Materia | Petición | Comprobación |
| --- | --- | --- |
| **4.º ESO · Historia** | Plan de repaso de 45 min con preguntas | Cada respuesta, en los apuntes |
| **1.º Bach · Física** | Tres pistas para un plano inclinado | Rehacer el cálculo a mano |
| **Comercio** | Ficha de una mochila para 16–18 años | Precio y medidas reales |

<div class="success">
El patrón es el mismo. Cambia la materia y el material; no cambia la estructura ni la comprobación.
</div>

---
class: compact-slide
---

## Verifica antes de usar

- **Datos y fechas:** contrástalos con el libro o una fuente oficial.
- **Citas:** abre la fuente. Si no existe, elimínala.
- **Cálculos:** rehazlos a mano.
- **Normativa:** comprueba la versión vigente.
- **Voz propia:** si no puedes explicarlo, no lo has aprendido.

<div class="warning">
Las referencias inventadas son el fallo más frecuente y el más difícil de detectar sin abrir la fuente.
</div>

---
class: visual-slide
---

<img src="/imagenes/verificacion-datos.svg" alt="Cinco comprobaciones: fecha, cita, cálculo, norma y explicación propia" />

<div class="visual-caption">Verificar no es releer: es abrir la fuente, rehacer la cuenta y explicar sin apoyo.</div>

---
class: compact-slide
---

## Ejemplo práctico

<div class="prompt-box">
<span class="label">4.º ESO · Historia</span>
Actúa como profesor de Historia de 4.º de ESO.
Contexto: apuntes adjuntos de la Revolución Industrial. Examen de causas, inventos y consecuencias. Hoy 45 minutos, mañana 30.
Tarea: plan de repaso en dos sesiones con una pregunta de recuperación por bloque y su respuesta en dos líneas.
Formato: tabla con bloque, tiempo, pregunta, respuesta esperada.
Restricciones: usa solo el documento. Si falta un dato, escribe «no consta».
</div>

Resultado: tabla de 6–8 filas con tiempos realistas y preguntas que obligan a recordar.

[Ver el ejemplo completo](https://sergarb1.github.io/IAParaEstudiar/niveles/eso/)

---
class: compact-slide
---

## Ejemplo 2 · Física: pista, no solución

<div class="prompt-box">
<span class="label">1.º Bachillerato · plano inclinado</span>
Actúa como profesor de Física.
Contexto: el alumno falla un plano inclinado. Adjunto enunciado y solución.
Tarea: tres preguntas de diagnóstico y una pista para cada una.
Formato: tabla pregunta / pista / error que detecta.
Restricciones: no des la solución; usa solo lo adjunto.
</div>

<div class="success">
El alumno localiza el fallo y vuelve a intentarlo. La IA no resuelve por él.
</div>

---
class: compact-slide
---

## Ejemplo 3 · Comercio: ficha de producto

<div class="prompt-box">
<span class="label">Ciclos Formativos · tienda de deporte</span>
Actúa como responsable de tienda.
Contexto: ficha de una mochila de 24 litros para estudiantes de 16 a 18 años. Adjunto características reales.
Tarea: tres beneficios, dos objeciones con respuesta y una frase de cierre.
Formato: ficha breve por apartados.
Restricciones: no inventes precio, medidas ni materiales.
</div>

<div class="info">
Si el precio no consta, se escribe «consultar». Una ficha útil no necesita inventar nada.
</div>

---
class: compact-slide
---

## Errores frecuentes

| Error | Alternativa |
| --- | --- |
| «Hazme un resumen» sin más | Curso, objetivo, extensión, destinatario |
| Aceptar la primera respuesta | Iterar con defectos concretos |
| Pegar datos del alumnado | Anonimizar siempre |
| Copiar citas sin abrirlas | Verificar cada fuente |
| Usar la IA para no pensar | Practicar, comprobar, explicar |

---
layout: closing
---
