---
title: Biblioteca de prompts
description: "Prompts listos para adaptar a cualquier materia y nivel, agrupados por tarea."
---

Cada prompt está pensado para copiarse y cambiar lo que va entre corchetes. No son fórmulas mágicas: funcionan porque incluyen rol, contexto, tarea, formato y una restricción de verificación.

> Si un prompt te da una respuesta genérica, añade contexto antes de pedir otra cosa.

## Para preparar una sesión

**1. Explicar un concepto a un nivel concreto**

```text
Actúa como profesor de [materia] de [nivel].
Explica [concepto] en tres niveles: una frase para alguien que no sabe nada, un párrafo con un ejemplo cotidiano y una definición técnica.
Termina con una pregunta que compruebe si se ha entendido.
No uses tecnicismos sin explicarlos.
```

**2. Convertir el temario en una secuencia**

```text
Tengo estos contenidos: [lista].
Ordénalos en [n] sesiones de [duración] para [nivel].
Para cada sesión: objetivo, actividad inicial, explicación, práctica y cierre.
Señala qué contenidos son prerrequisito de otros.
Si el tiempo no alcanza, dime qué recortar.
```

**3. Detectar ideas previas erróneas**

```text
Sobre el tema [tema] en [nivel], enumera los cinco errores conceptuales más frecuentes del alumnado.
Para cada uno: por qué se produce, cómo detectarlo y una actividad breve para corregirlo.
No inventes datos; si no estás seguro, dilo.
```

## Para estudiar y comprender

**4. Preguntas de recuperación activa**

```text
Actúa como examinador de [materia] de [nivel].
Hazme [n] preguntas de respuesta corta sobre [tema], de fácil a difícil.
Haz una pregunta cada vez y espera mi respuesta.
No me des la solución hasta que lo intente. Al final, dime qué debo repasar.
```

**5. Explicación tipo Feynman**

```text
Voy a explicarte [tema] como si tuviera que enseñárselo a un compañero.
Escucha mi explicación y señala: qué es impreciso, qué falta y qué sobra.
Después hazme dos preguntas que demuestren si lo he entendido.
No reescribas mi explicación.
```

**6. Resumen con citas desde un documento**

```text
Con el documento adjunto:
1. Resume en [n] palabras con una cita por idea principal.
2. Señala los tres conceptos que más se confunden.
3. Escribe cinco preguntas cuya respuesta esté en el documento.
4. Marca lo que no aparezca como «no consta».
```

## Para planificar

**7. Plan de estudio con repasos**

```text
Examen de [materia] el [fecha]. Temario: [bloques]. Tengo [minutos] al día.
Diseña un plan con repasos espaciados, un simulacro por bloque y un día de repaso de errores.
Formato: tabla por día con bloque, técnica, tiempo y pregunta de control.
Si no cabe, recorta y dilo.
```

**8. Planificar un trabajo largo**

```text
Trabajo de [asignatura] sobre [tema], entrega el [fecha], [extensión].
Divide el trabajo en hitos semanales con una tarea concreta por hito.
Incluye una revisión de fuentes y una revisión de formato.
No escribas el trabajo.
```

## Para escribir y revisar

**9. Revisar sin reescribir**

```text
Revisa este texto mío para [nivel y destinatario].
Señala: frases confusas, repeticiones, saltos de lógica y afirmaciones sin fuente.
No lo reescribas entero. Propón una corrección por problema y explica por qué.
```

**10. Estructura de un documento académico**

```text
Propón el esquema de un trabajo sobre [tema] para [nivel].
Incluye secciones, qué debe responder cada una y [n] fuentes por tipo.
No inventes títulos ni autores: indica qué buscar y dónde.
```

**11. Preparar una defensa oral**

```text
Voy a defender un trabajo sobre [tema] durante cinco minutos.
Hazme las cinco preguntas más difíciles que podría recibir y valora mis respuestas.
Señala qué argumento me falta y qué dato debería llevar preparado.
```

## Para el aula

**12. Adaptar una actividad a un nivel**

```text
Tengo esta actividad: [descripción].
Adáptala para [nivel o perfil], manteniendo el objetivo de aprendizaje.
Indica qué cambias, qué mantienes y qué apoyos añades.
Señala posibles barreras de accesibilidad.
```

**13. Generar un caso práctico con datos ficticios**

```text
Crea un caso práctico de [materia] para [nivel] con datos ficticios y realistas.
Incluye el enunciado, los datos, la solución razonada y los errores típicos.
No uses nombres de personas reales ni empresas existentes.
```

**14. Rúbrica de una tarea**

```text
Diseña una rúbrica de [tarea] para [nivel] con cuatro criterios y cuatro niveles.
Cada nivel debe describir una conducta observable, no una impresión.
Incluye un criterio sobre verificación de fuentes.
```

## Para trabajar con documentos

**15. Preguntas sobre un temario**

```text
Con las fuentes de este cuaderno:
1. ¿Qué tres ideas son imprescindibles?
2. ¿Qué relación hay entre [concepto A] y [concepto B]?
3. ¿Qué punto queda poco explicado?
Cita siempre la fuente y el fragmento.
```

**16. Comparar dos fuentes**

```text
Compara lo que dicen estas dos fuentes sobre [tema].
Haz una tabla: coincidencias, diferencias y posibles causas.
No elijas una como correcta sin indicar por qué.
```

**17. Convertir apuntes en material de repaso**

```text
Con estos apuntes, genera:
- un resumen de [n] palabras con citas,
- diez preguntas de respuesta corta,
- un mapa de relaciones entre los conceptos principales.
Marca lo que no esté en los apuntes.
```

## Para docencia y gestión

**18. Comunicación con familias**

```text
Redacta un correo breve a las familias de [grupo] sobre [tema].
Tono cercano y claro, sin tecnicismos, [n] palabras.
Incluye qué se ha hecho en clase, qué se pide en casa y a quién contactar.
No incluyas datos personales.
```

**19. Acta o resumen de reunión**

```text
Con estas notas de reunión, redacta un acta de una página:
asistentes, temas, acuerdos, responsables y fechas.
No inventes acuerdos que no aparezcan en las notas.
```

**20. Diseñar un agente sencillo**

```text
Ayúdame a diseñar un agente para esta tarea repetitiva: [tarea].
Define: objetivo, entradas, pasos, salidas, permisos mínimos, criterio de parada y revisión humana.
Señala qué podría salir mal y cómo limitarlo.
No lo configures todavía: primero el diseño.
```

## Cómo adaptar cualquier prompt

| Pieza | Si falta… | Añade… |
| --- | --- | --- |
| Rol | La respuesta es genérica | «Actúa como…» |
| Contexto | El resultado no encaja con tu grupo | Nivel, materia, qué se ha trabajado |
| Tarea | No sabes qué va a producir | Verbo + producto + cantidad |
| Formato | Texto largo e inmanejable | Tabla, lista, palabras |
| Restricción | Inventa o se pasa de tono | «No inventes», «cita la fuente», «sin tecnicismos» |
| Verificación | Se usa sin comprobar | «Señala qué habría que comprobar» |
