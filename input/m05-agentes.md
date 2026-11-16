---
layout: cover
---

# Usa agentes para principiantes

## Qué son, cómo funcionan y cómo empezar sin programar

---
class: compact-slide
---

## Un chatbot responde; un agente actúa

Un agente recibe un **objetivo**, planifica pasos, usa **herramientas** y repite hasta cumplirlo.

<div class="info">
No le dices «resume esto», sino «cada viernes revisa estas fuentes, prepara un resumen y déjalo en esta carpeta».
</div>

---
class: compact-slide
---

## Chatbot frente a agente

| Chatbot | Agente |
| --- | --- |
| Una pregunta, una respuesta | Un objetivo, varios pasos |
| No actúa fuera del chat | Busca, lee, escribe, envía |
| Tú decides cada paso | Decide el siguiente con tus límites |
| El contexto es el hilo | Memoria y estado entre pasos |

<div class="warning">
La autonomía amplifica los aciertos y también los errores. Empieza con tareas reversibles.
</div>

---
class: compact-slide
---

## Anatomía de un agente

| Pieza | Pregunta | Ejemplo |
| --- | --- | --- |
| Objetivo | ¿Qué debe existir al final? | Un resumen semanal con fuentes |
| Herramientas | ¿Con qué actúa? | Navegador, Drive, correo |
| Contexto | ¿Qué necesita? | Apuntes, lista de fuentes |
| Permisos | ¿Qué puede tocar? | Lectura de una carpeta |
| Parada | ¿Cuándo termina? | Cinco fuentes o 15 minutos |
| Revisión | ¿Quién valida? | El docente |

---
class: compact-slide
---

## Dónde encontrarlos sin programar

- **Dentro de los asistentes:** tareas programadas, navegación, conectores con Drive o Calendar.
- **Automatización sin código:** flujos entre formularios, correo, hojas de cálculo e IA.
- **Asistentes especializados:** investigan, transcriben o clasifican con un objetivo concreto.

<div class="success">
Empieza por la opción más simple. Muchas tareas que parecen de agente se resuelven con un cuaderno bien organizado y un recordatorio.
</div>

---
class: compact-slide
---

## Primer agente: rutina semanal de estudio

1. Define la **entrada**: carpeta con los apuntes de la semana.
2. Define el **proceso**: agrupar, resumir con citas, generar preguntas.
3. Define la **salida**: un documento por asignatura.
4. **Limita permisos**: lectura de entrada, escritura solo en salida.
5. Añade **parada**: máximo de documentos y tiempo.
6. Prueba con **datos ficticios** y revisa la primera salida.

---
class: compact-slide
---

## Ejemplo práctico

<div class="prompt-box">
<span class="label">FP Superior · Informática</span>
Cada viernes a las 18:00:
1. Revisa notas de versión y anuncios oficiales del framework.
2. Selecciona solo cambios que afecten al temario adjunto.
3. Resumen de 200 palabras con enlace a cada fuente.
4. Un ejemplo mínimo por cambio relevante.
5. Guarda en «novedades». No modifiques los apuntes.
6. Si no hay cambios relevantes, escribe «sin cambios» y termina.
Permisos: lectura de fuentes y escritura solo en «novedades».
</div>

[Ver el ejemplo completo](https://sergarb1.github.io/IAParaEstudiar/niveles/fp-informatica/)

---
class: compact-slide
---

## Riesgos que hay que conocer

| Riesgo | Medida |
| --- | --- |
| Exceso de permisos | Permisos mínimos y copia de seguridad |
| Inyección de instrucciones | Contenido externo no fiable |
| Errores silenciosos | Revisión humana el primer mes |
| Datos personales | Anonimizar y usar cuentas del centro |
| Coste o cuota | Parada por tiempo y pasos |
| Dependencia | Documentar el proceso manual |

---
class: sparse-slide
---

## ¿Cuándo no usar un agente?

- Cuando la tarea se hace en dos minutos a mano.
- Cuando un error no se puede deshacer.
- Cuando no puedes explicar el proceso.
- Cuando nadie va a revisar el resultado.

<div class="teacher-note">
<strong>Idea final</strong> Un agente es un becario incansable sin criterio: objetivo estrecho, permisos limitados y revisión obligatoria.
</div>

---
layout: closing
---
