---
title: Módulo 2 · Construye tu sistema de estudio
description: "NotebookLM y otras funciones de IA para trabajar con documentos y convertir los apuntes en un sistema de estudio con citas y repaso."
---

<div class="module-meta">
  <span>2 horas</span>
  <span>Sesión 2</span>
  <span>NotebookLM</span>
  <span>Requiere cuenta Google</span>
  <a class="module-slides" href="/presentaciones/m02/">Presentación</a>
</div>

<figure class="page-visual is-diagram">
  <div class="page-visual-frame">
    <img src="/imagenes/modulo-2.svg" alt="Esquema de tres fuentes que entran en un cuaderno y salen resumen, cuestionario y mapa con citas." width="1200" height="630" loading="lazy" />
  </div>
  <figcaption>Esquema propio. El cuaderno no busca en internet: responde con las fuentes que le has dado.</figcaption>
</figure>

## Qué vas a aprender

- Qué es un cuaderno de NotebookLM y en qué se diferencia de un chatbot.
- Cómo preparar fuentes que merezcan la pena y descartar las que no.
- Qué materiales se pueden generar y para qué sirve cada uno.
- Cómo integrar esos materiales en una rutina de estudio real.
- Dónde están los límites: fuentes escaneadas, citas mal interpretadas y exceso de confianza.

## 1. Un chatbot que solo lee lo que tú le das

NotebookLM trabaja con **fuentes**: documentos, páginas web, textos o vídeos que tú subes a un cuaderno. Sus respuestas se apoyan en esas fuentes y muestran la cita, de modo que puedes comprobar de dónde sale cada afirmación.

| Chatbot generalista | NotebookLM |
| --- | --- |
| Responde con conocimiento entrenado | Responde con las fuentes del cuaderno |
| No siempre indica de dónde sale un dato | Cita el fragmento y la fuente |
| Puede completar huecos con invención | Debe ceñirse a lo aportado; si no está, lo dice |
| Sirve para crear y transformar | Sirve para estudiar y comprender un corpus |

> Regla práctica: si la pregunta es «¿qué dice mi temario?», NotebookLM. Si es «ayúdame a redactar algo nuevo», un chatbot generalista.

## 2. Preparar las fuentes

La calidad del cuaderno depende de lo que entra en él. Antes de subir nada:

<div class="checklist">

- **Elige fuentes primarias:** temario oficial, apuntes propios, capítulos del libro, normativa, artículos de referencia.
- **Descarta resúmenes de resúmenes:** si una fuente ya es una interpretación, la IA interpretará una interpretación.
- **Comprueba que el PDF tenga texto:** un documento escaneado sin OCR no se puede leer bien. Si es una imagen, pásalo antes por OCR.
- **Nombra los archivos con criterio:** `tema-3-fotosintesis.pdf` se encuentra mejor que `documento1.pdf`.
- **Separa por asignatura o unidad:** un cuaderno por bloque. Mezclar 40 fuentes de cuatro materias degrada las respuestas.
</div>

En el plan gratuito hay un número máximo de fuentes y de cuadernos. Los límites cambian: consulta el plan vigente antes de prometer nada en clase.

<figure class="page-visual is-diagram">
  <div class="page-visual-frame">
    <img src="/imagenes/fuentes-notebook.svg" alt="Tres fuentes pasan por los filtros de fuente primaria, texto legible y una sola unidad antes de entrar en el cuaderno." width="1200" height="630" loading="lazy" />
  </div>
  <figcaption>Esquema propio. Un cuaderno útil empieza por descartar: resúmenes de resúmenes y escaneos sin OCR no deberían entrar.</figcaption>
</figure>

## 3. El flujo de trabajo

<div class="checklist">

1. **Crear el cuaderno** con el nombre de la unidad.
2. **Subir las fuentes** y esperar a que se procesen.
3. **Preguntar en modo conversación**, pidiendo siempre la cita.
4. **Generar materiales** derivados: resumen, guía de estudio, mapa mental, cuestionario, audio.
5. **Exportar y guardar** lo que vayas a usar (documento, PDF, notas).
6. **Estudiar con los materiales**, no con el chat: leer, tapar, responder, corregir.
</div>

## 4. Qué genera y para qué sirve cada cosa

| Material | Para qué sirve | Cuidado |
| --- | --- | --- |
| Resumen | Primera pasada sobre un tema largo | Puede perder matices y ejemplos |
| Guía de estudio | Estructura de lo que hay que saber | No sustituye al temario completo |
| Cuestionario | Recuperación activa y autoevaluación | Revisa que las preguntas no sean triviales |
| Mapa mental | Ver relaciones entre conceptos | Suele simplificar jerarquías complejas |
| Audio (resumen conversado) | Repaso en desplazamientos | Escuchar no es estudiar: exige tomar notas |
| Preguntas al documento | Resolver dudas concretas con cita | Comprueba siempre el fragmento citado |

## 5. Tu sistema de estudio

Un sistema no es una colección de herramientas: es una rutina con entradas y salidas claras. Este es el que se propone en el curso.

| Momento | Acción | Herramienta |
| --- | --- | --- |
| Antes de clase | Subir el tema y pedir un mapa general | NotebookLM |
| Durante la clase | Tomar apuntes propios y marcar dudas | Cuaderno y móvil |
| Después de clase | Añadir los apuntes al cuaderno y pedir un resumen con citas | NotebookLM |
| Dos días después | Cuestionario y repaso de fallos | NotebookLM + papel |
| Una semana después | Explicar el tema en voz alta sin mirar | Sin IA |
| Antes del examen | Simulacro cronometrado y corrección | Chatbot o tutor del módulo 3 |

La IA aparece en los extremos (preparar y comprobar). El centro del sistema sigue siendo **leer, escribir y explicar**.

<figure class="page-visual is-diagram">
  <div class="page-visual-frame">
    <img src="/imagenes/rutina-repaso.svg" alt="Línea de tiempo de repaso a los cero, dos, siete y catorce días, con la técnica y la herramienta de cada momento." width="1200" height="630" loading="lazy" />
  </div>
  <figcaption>Esquema propio. La IA prepara los materiales y el calendario; la memoria se construye al cumplir los repasos.</figcaption>
</figure>

## Ejemplo práctico del módulo

**Situación:** el alumnado de 1.º de Bachillerato tiene un tema de Biología con tres fuentes: apuntes de clase, un capítulo del libro y una infografía del profesor.

<div class="prompt-box">
<span class="label">Prompt dentro del cuaderno</span>
A partir exclusivamente de las tres fuentes de este cuaderno:

1. Haz un resumen del tema en 300 palabras, con una cita por cada idea principal.
2. Señala los tres conceptos que más se confunden entre sí y explica la diferencia en dos líneas cada uno.
3. Genera 10 preguntas de respuesta corta, de menor a mayor dificultad, e indica junto a cada una la fuente que la respalda.
4. Marca explícitamente cualquier punto en el que las fuentes no coincidan.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Un resumen con citas clicables, una tabla de conceptos confundibles y diez preguntas con referencia. Si las fuentes discrepan en una cifra o en una definición, debe aparecer una advertencia en lugar de una síntesis silenciosa.
</div>

<div class="example-answer">
<span class="label">Ejemplo de respuesta</span>
<p><strong>Extracto del resumen</strong></p>
<p>El metabolismo agrupa las reacciones químicas de la célula. El catabolismo degrada moléculas y libera energía; el anabolismo construye moléculas y la consume <em>[cita: apuntes, p. 3]</em>. Las enzimas aceleran las reacciones y son específicas de cada sustrato <em>[cita: libro, cap. 6]</em>.</p>
<p><strong>Tres conceptos confundibles</strong></p>
<ul>
<li><strong>Catabolismo / anabolismo:</strong> degradar y liberar energía frente a construir y consumirla.</li>
<li><strong>Enzima / coenzima:</strong> proteína catalizadora frente a molécula que ayuda a la enzima.</li>
<li><strong>Aerobio / anaerobio:</strong> con oxígeno y más energía frente a sin oxígeno y menos energía.</li>
</ul>
<p><strong>Pregunta con fuente</strong></p>
<p>¿Por qué una enzima es específica? <em>(libro, cap. 6)</em></p>
<p><em>Aviso:</em> la infografía no indica el rendimiento energético; se marca «no consta» en lugar de completarlo.</p>
</div>

**Enlace al resultado desarrollado:** [Ejemplo de Bachillerato · sistema de estudio de Biología](/niveles/bachillerato/).

**Comprobación:** elegir dos citas al azar y abrir el fragmento original. Si la cita no respalda la frase, el material no se usa.

## Dos ejemplos más, en otras materias

### ESO · Inglés: vocabulario en contexto

<div class="prompt-box">
<span class="label">Prompt dentro del cuaderno</span>
Con la lista de vocabulario, el diálogo del libro y mis apuntes de clase:
1. Prepara 12 preguntas de recuperación: seis de significado y seis de uso en una frase nueva.
2. Marca junto a cada pregunta la fuente que la respalda.
3. Señala tres palabras que se confunden fácilmente y explica la diferencia en una línea.
No inventes ejemplos que no aparezcan en las fuentes.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Doce preguntas graduadas, cada una con su cita, y una tabla de tres confusiones habituales. Las preguntas de uso obligan a producir una frase, no solo a reconocer la palabra.
</div>

### Ciclos Formativos · Informática: revisar un repositorio

<div class="prompt-box">
<span class="label">Prompt dentro del cuaderno</span>
En este cuaderno tienes el README, la guía de estilo y dos issues del proyecto.
Genera un checklist de revisión para un pull request de 10 archivos.
Distingue entre error, riesgo y preferencia de estilo, y cita el archivo o la sección que respalda cada punto.
No propongas código completo: solo qué revisar y por qué.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Un checklist de 8–10 puntos con tres columnas: gravedad, evidencia y acción. Los puntos sin respaldo en el repositorio se marcan como «no consta» y no se convierten en reglas inventadas.
</div>

### Cuando las fuentes no coinciden

| Situación | Qué pedir | Qué haces |
| --- | --- | --- |
| Dos fuentes dan cifras distintas | «Muéstrame ambas y no las sintetices» | Usar la oficial y anotar la diferencia |
| La norma y el resumen no coinciden | «Cita el artículo y la fecha de la versión» | Prevalece la versión vigente; el resumen se descarta |
| El libro omite algo que sí está en tus apuntes | «Marca el hueco y la fuente que lo completa» | Completar con los apuntes y señalarlo |

## 6. Límites y errores frecuentes

| Error | Consecuencia | Solución |
| --- | --- | --- |
| Subir PDFs escaneados sin OCR | Respuestas pobres o vacías | Pasar OCR antes de subir |
| Mezclar demasiadas fuentes | Respuestas vagas y citas cruzadas | Un cuaderno por unidad |
| Confiar en el resumen sin abrir el original | Se estudia una interpretación | Verificar al menos dos citas por sesión |
| Usar solo el audio | Sensación de estudiar sin recuperar | Acompañar con preguntas y escritura |
| Copiar el resumen en un trabajo | Riesgo de plagio y de error | Citar, reformular y aportar análisis |

## Adaptación por niveles

- [ESO](/niveles/eso/): vocabulario y repaso de un tema con el móvil.
- [FP Básica](/niveles/fp-basica/): instrucciones de taller y apoyo a la comprensión.
- [Bachillerato](/niveles/bachillerato/): cuaderno de Biología con tres fuentes y trabajo de investigación.
- [Ciclos Formativos · Informática](/niveles/fp-informatica/): documentación técnica y preguntas sobre un repositorio.
- [Ciclos Formativos · Administración](/niveles/fp-administracion/): normativa y modelos de documentos.
- [Ciclos Formativos · Comercio](/niveles/fp-comercio/): catálogo de producto y análisis de campañas.
- [Ciclos Formativos · Turismo](/niveles/fp-turismo/): destinos, protocolo y guiones de visita.

## Para el docente

<div class="teacher-note">
  <strong>Idea que debe quedar clara</strong>
  El cuaderno es tan bueno como las fuentes que contiene. Antes de preguntar a la IA, hay que decidir qué merece ser leído y qué no.
</div>

### Guion de la sesión (120 min)

| Tiempo | Actividad | Notas |
| --- | --- | --- |
| 10 min | Repaso del módulo 1: ¿qué prompt funcionó? | Recoger un ejemplo y comentarlo |
| 15 min | Demostración: cuaderno con dos fuentes y una pregunta con cita | Proyectar el panel de fuentes |
| 20 min | Criterios para elegir y preparar fuentes | Insistir en OCR y en separar unidades |
| 30 min | Cada participante monta un cuaderno de su materia | Traer material propio anonimizado |
| 20 min | Generar resumen, cuestionario y mapa; comparar | Ver qué material es flojo y por qué |
| 15 min | Diseñar la rutina semanal del sistema de estudio | Plantilla de la tabla del apartado 5 |
| 10 min | Cierre y dudas | Recordar la verificación de citas |

### Dudas previsibles

- **«¿Puedo subir el libro completo?»** Técnicamente puede permitirlo el plan; legalmente depende de los derechos de reproducción. Usa fragmentos que necesites y material propio.
- **«¿Las citas son fiables?»** Suelen ser correctas en cuanto a localización, pero pueden interpretar mal el fragmento. Hay que abrir la fuente.
- **«¿El audio sustituye al resumen?»** No. Es un apoyo para repasar; sin recuperación activa no consolida.
- **«¿Qué hago si mi PDF no se lee?»** Pasar OCR o convertir a texto antes de subirlo.

### Evaluación formativa

- Cada participante presenta **un cuaderno con al menos tres fuentes** y una pregunta respondida con cita verificada.
- Se valora la selección de fuentes y la comprobación, no la cantidad de materiales generados.
- Entregable breve: una tabla con «material generado → cómo lo voy a usar → qué comprobaré».

### Materiales

- Cuenta de Google y acceso a NotebookLM.
- Tres documentos propios de una unidad (apuntes, capítulo, normativa o infografía).
- Plantilla de rutina semanal para completar en la sesión.
