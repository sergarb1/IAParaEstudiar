---
layout: cover
---

# Usa agentes para principiantes

## Qué son, cómo funcionan y cómo empezar sin programar

---
class: visual-slide
---

<img src="/imagenes/modulo-5.svg" alt="Esquema del módulo" />

<div class="visual-caption">Objetivo, herramientas, contexto, permisos, parada y revisión humana.</div>

---
class: compact-slide
---

## Un chatbot responde; un agente actúa

<div class="comparison-grid">
<div class="comparison-item">

### Chatbot

Una pregunta, una respuesta. Tú decides cada paso y el contexto es el hilo de la conversación.

</div>
<div class="comparison-item good">

### Agente

Un objetivo, varios pasos. Busca, lee, escribe y decide el siguiente paso dentro de tus límites.

</div>
</div>

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
class: visual-slide
---

<img src="/imagenes/agente-flujo.svg" alt="Flujo del agente: disparador, lectura, filtro, escritura y revisión humana" />

<div class="visual-caption">Cada paso tiene un permiso distinto; el último paso siempre es una persona.</div>

---
layout: image-right
image: /imagenes/nivel-fp-informatica.jpg
---

## Un agente en el aula

- Vigila fuentes, no produce apuntes finales.
- Permisos mínimos y una carpeta de salida.
- Si no hay cambios, escribe «sin cambios» y termina.

[Ver el ejemplo de Informática](https://sergarb1.github.io/IAParaEstudiar/niveles/fp-informatica/)

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

<div class="two-cols">
<div class="left">

1. Define la **entrada**: carpeta con los apuntes de la semana.
2. Define el **proceso**: agrupar, resumir con citas, generar preguntas.
3. Define la **salida**: un documento por asignatura.
4. **Limita permisos**: lectura de entrada, escritura solo en salida.
5. Añade **parada**: máximo de documentos y tiempo.
6. Prueba con **datos ficticios** y revisa la primera salida.

</div>
<div class="right">

### Antes de activar

- ¿Qué puede leer y qué puede escribir?
- ¿Cuándo termina aunque no haya acabado?
- ¿Quién revisa la primera salida?

<div class="warning">
Un agente sin carpeta de salida ni revisión puede tocar más de lo que quieres. Empieza con permisos de lectura.
</div>

</div>
</div>

---
class: compact-slide
---

## Ejemplo práctico

<div class="two-cols">
<div class="left">

<div class="prompt-box">
<span class="label">Ciclos Formativos · Informática</span>
Cada viernes a las 18:00:
1. Revisa notas de versión y anuncios oficiales del framework.
2. Selecciona solo cambios que afecten al temario adjunto.
3. Resumen de 200 palabras con enlace a cada fuente.
4. Un ejemplo mínimo por cambio relevante.
5. Guarda en «novedades». No modifiques los apuntes.
6. Si no hay cambios relevantes, escribe «sin cambios» y termina.
Permisos: lectura de fuentes y escritura solo en «novedades».
</div>

</div>
<div class="right">

### Qué observar

- Que cite cada fuente y no invente versiones.
- Que no escriba fuera de «novedades».
- Que sepa terminar con «sin cambios».

[Ver el ejemplo completo](https://sergarb1.github.io/IAParaEstudiar/niveles/fp-informatica/)

</div>
</div>

---
class: compact-slide
---

## Ejemplo 2 · Administración: plazos

<div class="two-cols">
<div class="left">

<div class="prompt-box">
<span class="label">Ciclos Formativos · Administración</span>
Cada lunes a las 8:00:
1. Revisa calendario y expedientes.
2. Marca los que vencen en 10 días.
3. Prepara un aviso con norma, fecha y expediente.
4. Guarda en «vencimientos».
5. No envíes correos ni modifiques el calendario.
6. Si no hay plazos, escribe «sin vencimientos».
Permisos: lectura del calendario; escritura solo en «vencimientos».
</div>

</div>
<div class="right">

### Límites del ejemplo

- No envía correos.
- No cambia fechas del calendario.
- No decide si un plazo es urgente: avisa.

<div class="success">
Tres a cinco vencimientos con norma y fecha. Nada sale del centro sin revisión.
</div>

</div>
</div>

---
class: compact-slide
---

## Ejemplo 3 · Turismo: alertas de destino

<div class="prompt-box">
<span class="label">Ciclos Formativos · Turismo</span>
Cada mañana:
1. Revisa la web oficial del destino y la documentación del viaje.
2. Si hay una alerta, resume el cambio en 80 palabras.
3. Propón dos alternativas y enlaza la fuente oficial.
4. Guarda en «incidencias».
5. No contactes con proveedores ni cambies reservas.
6. Si no hay alertas, escribe «sin incidencias».
Parada: 10 minutos y tres fuentes.
</div>

<div class="info">
El agente no reserva ni promete disponibilidad. El guía valida la alternativa antes de comunicarla.
</div>

---
class: compact-slide
---

## Prueba de fallo antes de activar

<div class="two-cols">
<div class="left">

<div class="checklist">

- **Quita una fuente:** debe escribir «no consta».
- **Duplica una fuente:** no debe repetir el dato.
- **Mete una orden en un documento:** debe tratarla como texto.
- **Corta la conexión:** debe parar y marcar lo que quedó a medias.
</div>

</div>
<div class="right">

### Qué demuestra cada prueba

- Que no rellena huecos con invenciones.
- Que el contenido externo no cambia sus órdenes.
- Que sabe parar cuando falta una herramienta.

<div class="warning">
Si falla una de las cuatro pruebas, el agente no está listo para datos reales.
</div>

</div>
</div>

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

<div class="warning">
El riesgo no es solo que el agente falle: es que falle en silencio y nadie revise la salida.
</div>

---
class: visual-slide
---

<img src="/imagenes/riesgos-agente.svg" alt="Seis riesgos de los agentes y su medida de control" />

<div class="visual-caption">Menos permisos, más revisión y un proceso manual documentado.</div>

---
class: visual-slide
---

<img src="/imagenes/decidir-agente.svg" alt="Decisión entre hacer la tarea a mano, usar un chatbot o montar un agente con permisos y revisión" />

<div class="visual-caption">Un agente es un becario incansable sin criterio: objetivo estrecho, permisos limitados y revisión obligatoria.</div>

---
layout: closing
---

# Tres ideas para llevarte

1. **Un agente es un objetivo con herramientas y límites.** No es un chat más largo.
2. **Permisos mínimos y parada explícita.** Lectura primero; escritura después.
3. **La revisión humana no se automatiza.** Sin revisión, no se publica.

<p class="closing-meta">IA para estudiar · Sergi García Barea · CC BY-SA 4.0</p>
