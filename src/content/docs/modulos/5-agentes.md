---
title: Módulo 5 · Agentes para principiantes
description: "Qué son los agentes de IA, cómo funcionan y cómo empezar a usarlos sin programar para estudiar y para tareas de aula."
---

<div class="module-meta">
  <span>2 horas</span>
  <span>Sesión 5</span>
  <span>Agentes · Automatización</span>
  <span>Sin programar</span>
</div>

## Qué vas a aprender

- Qué distingue un agente de un chatbot.
- Qué piezas necesita un agente para funcionar sin supervisión constante.
- Cómo montar un primer agente sencillo para una tarea de estudio o de gestión.
- Qué riesgos aparecen cuando el agente puede actuar, no solo responder.
- Cómo decidir cuándo un agente no merece la pena.

## 1. Qué es un agente

Un chatbot responde a un mensaje. Un **agente** recibe un objetivo, planifica pasos, usa herramientas y repite hasta cumplirlo.

| Chatbot | Agente |
| --- | --- |
| Una pregunta, una respuesta | Un objetivo, varios pasos |
| No actúa fuera de la conversación | Puede buscar, leer, escribir, enviar o programar |
| Tú decides cada paso | Decide el siguiente paso con tus límites |
| El contexto es el hilo | Mantiene memoria y estado entre pasos |

La diferencia práctica: al agente no le dices «resume esto», le dices «cada viernes revisa las novedades de este tema, prepara un resumen con fuentes y déjalo en esta carpeta».

## 2. Anatomía de un agente

| Pieza | Pregunta | Ejemplo |
| --- | --- | --- |
| **Objetivo** | ¿Qué resultado debe existir al final? | Un resumen semanal con cinco fuentes |
| **Herramientas** | ¿Con qué puede actuar? | Navegador, Drive, correo, calendario, notas |
| **Contexto** | ¿Qué información necesita? | Carpeta de apuntes, lista de fuentes fiables |
| **Permisos** | ¿Qué puede tocar? | Solo lectura de una carpeta; escritura en otra |
| **Criterio de parada** | ¿Cuándo termina? | Cinco fuentes o 15 minutos |
| **Revisión humana** | ¿Quién valida? | El docente antes de publicar |

Sin objetivo claro, el agente deambula. Sin permisos limitados, el agente puede romper cosas. Sin parada, puede gastar tiempo y cuota indefinidamente.

## 3. Dónde encontrarlos sin programar

A fecha de este curso, las funciones de agente aparecen en tres formas:

- **Dentro de los asistentes:** tareas programadas, navegación web, conectores con Drive o Calendar, ejecución de pasos.
- **En herramientas de automatización:** flujos sin código que conectan formularios, correo, hojas de cálculo e IA.
- **En asistentes especializados:** aplicaciones que investigan, transcriben o clasifican documentos con un objetivo concreto.

Empieza por la opción más simple que resuelva el problema. Muchas tareas que parecen de agente se resuelven con un cuaderno bien organizado y un recordatorio.

## 4. Primer agente: rutina semanal de estudio

**Objetivo:** cada domingo, tener un resumen de la semana y tres preguntas de repaso por asignatura.

<div class="checklist">

1. **Define la entrada:** una carpeta donde el alumnado deja sus apuntes de la semana.
2. **Define el proceso:** agrupar por asignatura, resumir con citas, generar preguntas.
3. **Define la salida:** un documento por asignatura en una carpeta compartida.
4. **Limita permisos:** lectura de la carpeta de entrada, escritura solo en la de salida.
5. **Añade parada:** máximo de documentos por ejecución y tiempo límite.
6. **Prueba con datos ficticios** antes de usar material real.
7. **Revisa la primera salida** antes de automatizar la siguiente.

</div>

## 5. Ejemplo práctico del módulo

**Situación:** un docente de FP Superior de Informática quiere seguir las novedades de un framework y tener material para actualizar sus apuntes.

<div class="prompt-box">
<span class="label">Objetivo del agente</span>
Cada viernes a las 18:00:
1. Revisa las notas de la versión y los anuncios oficiales del framework indicado.
2. Selecciona solo cambios que afecten a lo que se imparte en el módulo (lista adjunta de temas).
3. Prepara un resumen de 200 palabras con enlace a cada fuente.
4. Añade una propuesta de ejemplo de código mínimo para cada cambio relevante.
5. Guarda el resultado en la carpeta «novedades» y no modifiques ningún apunte existente.
6. Si no encuentras cambios relevantes, escribe «sin cambios» y termina.

Permisos: solo lectura de las fuentes y escritura en la carpeta «novedades». No envíes correos ni publiques nada.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Un documento semanal con tres o cuatro cambios relevantes, cada uno con enlace y ejemplo. Si una versión no afecta al temario, el documento lo dice en una línea. Nada se publica sin revisión del docente.
</div>

**Enlace al resultado desarrollado:** [Ejemplo de FP Superior · Informática](/niveles/fp-informatica/).

## 6. Riesgos que hay que conocer

| Riesgo | Ejemplo | Medida |
| --- | --- | --- |
| **Exceso de permisos** | Un agente con acceso total al Drive borra una carpeta | Permisos mínimos y copia de seguridad |
| **Inyección de instrucciones** | Una web incluye texto que ordena al agente ignorar sus reglas | Tratar el contenido externo como no fiable |
| **Errores silenciosos** | Resume mal una fuente y nadie lo revisa | Revisión humana en el primer mes |
| **Datos personales** | Envía notas con nombres a un servicio externo | Anonimizar y usar cuentas del centro |
| **Coste y cuota** | Se ejecuta en bucle y consume el límite | Parada por tiempo y por número de pasos |
| **Dependencia** | El flujo se rompe y nadie sabe hacerlo a mano | Documentar el proceso alternativo |

<div class="warning">
  Un agente no es más fiable por ser autónomo. La autonomía amplifica los aciertos y también los errores. Empieza con tareas reversibles y revisa siempre la primera ejecución.
</div>

## 7. ¿Cuándo no usar un agente?

- Cuando la tarea se hace en dos minutos a mano.
- Cuando un error no se puede deshacer (enviar notas, borrar archivos, publicar).
- Cuando no puedes explicar el proceso que debería seguir.
- Cuando el resultado no se va a revisar.

## Adaptación por niveles

- [ESO](/niveles/eso/): recordatorios de repaso y resumen semanal.
- [FP Básica](/niveles/fp-basica/): listas de materiales y avisos de taller.
- [Bachillerato](/niveles/bachillerato/): seguimiento de fuentes para el trabajo de investigación.
- [FP Superior · Informática](/niveles/fp-informatica/): novedades técnicas y documentación.
- [FP Superior · Administración](/niveles/fp-administracion/): control de plazos y recordatorios.
- [FP Superior · Comercio](/niveles/fp-comercio/): seguimiento de campañas y precios.
- [FP Superior · Turismo](/niveles/fp-turismo/): avisos de destinos y documentación de viaje.

## Para el docente

<div class="teacher-note">
  <strong>Idea que debe quedar clara</strong>
  Un agente es un becario incansable sin criterio. Se le da un objetivo estrecho, herramientas limitadas y una revisión obligatoria.
</div>

### Guion de la sesión (120 min)

| Tiempo | Actividad | Notas |
| --- | --- | --- |
| 10 min | Repaso del curso y expectativas sobre agentes | Recoger qué tareas repetitivas tienen |
| 15 min | Demostración: chatbot frente a agente | Mismo objetivo, distinto comportamiento |
| 20 min | Anatomía: objetivo, herramientas, permisos, parada | Completar la tabla con un caso propio |
| 25 min | Diseñar un agente en papel | Sin herramienta: solo el flujo y los límites |
| 20 min | Montar un flujo sencillo o una tarea programada | Empezar por lectura y escritura en carpetas |
| 15 min | Riesgos y revisión humana | Analizar un fallo real o simulado |
| 10 min | Cierre del curso y trabajo final | Fechas y rúbrica |
| 5 min | Dudas | — |

### Dudas previsibles

- **«¿Necesito programar?»** No para los flujos de este módulo. Sí hace falta entender la lógica de pasos y permisos.
- **«¿Es seguro darle acceso a mi correo?»** Empieza con lectura y carpetas concretas; evita el envío automático.
- **«¿Qué agente monto primero?»** Uno que ahorre una tarea semanal y cuya salida puedas revisar en dos minutos.
- **«¿Y si falla?»** Debe existir un proceso manual documentado. El agente es una ayuda, no la única vía.

### Evaluación formativa

- Diseño en papel de un agente con objetivo, herramientas, permisos, parada y revisión.
- Prueba de una ejecución con datos ficticios y análisis de lo que salió mal.
- Comparación honesta: ¿aporta más que hacerlo a mano? Si no, se descarta.

### Materiales

- Cuenta con acceso a las funciones de agente o automatización disponibles.
- Carpeta de prueba con documentos ficticios.
- Plantilla de diseño de agente (objetivo, entradas, pasos, salidas, permisos, parada).
