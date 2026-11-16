---
title: FP Superior · Turismo
description: "Ejemplos de IA en Turismo: itinerarios verificados, cuaderno de destino y protocolo de incidencias."
---

<div class="module-meta">
  <span>CFGS Turismo</span>
  <span>Nivel profesional</span>
  <span>Datos que caducan</span>
</div>

## Qué cambia en Turismo

- La IA produce itinerarios atractivos con horarios, precios y distancias que suenan bien y pueden ser falsos o estar desactualizados.
- La verificación con fuentes oficiales (web del destino, transporte, museo) es parte del trabajo profesional.
- Los idiomas y el trato con el visitante son centrales: la IA ayuda a preparar y a practicar, no a improvisar en mostrador.
- La accesibilidad y la sostenibilidad deben aparecer en el diseño, no como adorno.

## Ejemplo 1 — Itinerario de tres días verificable (Módulo 1)

**Contexto:** el alumnado diseña un itinerario para un grupo de 20 personas mayores en una ciudad ficticia o real.

<div class="prompt-box">
<span class="label">Prompt</span>
Actúa como técnico de agencia receptiva.

Contexto: grupo de 20 personas de 65 años, tres días, ritmo tranquilo, presupuesto medio. Ciudad: [ciudad]. Adjunto la lista de puntos de interés y los horarios oficiales que hemos consultado.

Tarea: propón un itinerario de tres días con mañana y tarde, tiempos de desplazamiento y una alternativa por lluvia.

Formato: tabla por día con hora, actividad, duración, desplazamiento y observaciones de accesibilidad.

Restricciones: usa solo los puntos y horarios adjuntos. No inventes precios ni horarios; si falta un dato, escribe «verificar». Máximo 4 horas de actividad diaria.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Un itinerario realista con tiempos de desplazamiento, huecos para descanso y alternativa de lluvia. Los datos no comprobados quedan marcados para verificar.
</div>

**Comprobación:** cada horario se contrasta con la web oficial del recurso y cada desplazamiento con un mapa. Las casillas «verificar» se completan antes de la entrega.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Convierte la verificación en una lista de control: museo abierto, transporte disponible, accesibilidad real, duración del trayecto. Un itinerario sin verificar no es un itinerario profesional.
</div>

## Ejemplo 2 — Cuaderno de destino con fuentes oficiales (Módulo 2)

**Contexto:** preparar documentación de un destino para el mostrador: transporte, documentación de viaje y normas locales.

<div class="prompt-box">
<span class="label">Prompt en NotebookLM</span>
Con las fuentes oficiales de este cuaderno (web de turismo, transporte y consulado):

1. Resumen de documentación necesaria para un viajero con nacionalidad española, con cita por punto.
2. Tabla de transporte aeropuerto-centro con precio, duración y fuente.
3. Tres normas locales que un visitante debe conocer.
4. Avisa de cualquier dato que no aparezca o que pueda haber cambiado.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Un resumen con citas, una tabla de transporte con fuente y tres normas concretas. Los datos ausentes se señalan en lugar de completarse con conocimiento general.
</div>

**Comprobación:** se abren las fuentes citadas y se comprueba la fecha de actualización. Si la web oficial no confirma un precio, no se publica la cifra.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Insiste en la fecha: en turismo, un dato de hace seis meses puede estar mal. Pide que cada fuente lleve fecha de consulta.
</div>

## Ejemplo 3 — Protocolo y gestión de una incidencia (Módulo 3)

**Contexto:** simulación de mostrador: un cliente llega con una reserva que no aparece y un vuelo en cuatro horas.

<div class="prompt-box">
<span class="label">Prompt del tutor</span>
Actúa como cliente enfadado en un mostrador de agencia.

Situación: reserva de hotel no confirmada, vuelo en cuatro horas, dos personas. Yo estaré nervioso y elevaré el tono, sin insultos.

Responde como profesional: escucha, haz preguntas para verificar, propón dos alternativas y explica el siguiente paso. Al terminar, evalúa mi protocolo en tres puntos: empatía, verificación y solución. No me des el guion antes de la simulación.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Una simulación con preguntas de verificación, alternativas concretas y una evaluación final. El tutor no debe resolver la incidencia por el alumnado.
</div>

**Comprobación:** la actuación se contrasta con el protocolo del centro o de la agencia. Se repite la simulación aplicando las tres mejoras.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Graba la simulación (con permiso) y revisadla sin sonido: lenguaje corporal, turnos de palabra y tono. La IA evalúa el contenido; el docente, la presencia.
</div>

## Qué evitar en este nivel

| Práctica | Riesgo | Alternativa |
| --- | --- | --- |
| Publicar itinerarios sin verificar | Horarios cerrados, rutas imposibles | Comprobación con fuente oficial |
| Precios y disponibilidad generados | Información comercial falsa | Datos de proveedor o «consultar» |
| Simulaciones sin protocolo | Se aprende a improvisar mal | Protocolo del centro como referencia |
| Traducciones automáticas sin revisar | Errores en documentación de viaje | Revisión humana y glosario |

## Módulos relacionados

- [Módulo 1 · Habla con la IA](/modulos/1-habla-con-la-ia/)
- [Módulo 2 · Sistema de estudio](/modulos/2-sistema-de-estudio/)
- [Módulo 3 · La IA como profesor](/modulos/3-ia-como-profesor/)
