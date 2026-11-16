---
title: FP Superior · Informática
description: "Ejemplos de IA en ciclos superiores de Informática: depuración guiada, documentación técnica y agentes."
---

<div class="module-meta">
  <span>CFGS Informática</span>
  <span>DAW · DAM · ASIR</span>
  <span>Nivel profesional</span>
</div>

## Qué cambia en Informática

- El alumnado ya usa asistentes de código y suele confiar en que «si compila, está bien».
- El riesgo no es el plagio evidente, sino el código que nadie entiende y que no se puede mantener.
- La IA es especialmente útil para explicar errores, proponer pruebas y documentar; es peligrosa cuando sustituye el diseño.
- La evaluación debe centrarse en la autoría técnica: explicar decisiones, defender el código y cubrir casos límite.

## Ejemplo 1 — Depuración guiada sin regalar la solución (Módulos 1 y 3)

**Contexto:** un módulo de Python falla al procesar un fichero CSV con campos vacíos. El alumnado pega el error y pide la solución.

<div class="prompt-box">
<span class="label">Prompt</span>
Actúa como tutor de programación de FP Superior.

Te adjunto el código, el mensaje de error y un fragmento del CSV.
No me des la solución ni reescribas el archivo.
1. Hazme tres preguntas que me obliguen a mirar el flujo de datos.
2. Pídeme que formule una hipótesis y que la compruebe con una prueba concreta.
3. Si mi hipótesis es correcta, indícame qué línea revisar; si no, dame una pista distinta.
4. Al final, pídeme que explique la causa en dos frases.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Preguntas sobre el tratamiento de valores vacíos y el tipo de dato, sin código corregido. La sesión termina con una explicación del alumnado, no con un parche copiado.
</div>

**Comprobación:** el alumnado añade una prueba que reproduzca el fallo antes del arreglo y demuestra que el arreglo no rompe los casos anteriores.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Si el tutor reescribe el código, la instrucción ha fallado. Prueba antes la conversación y ajusta («no muestres código hasta que te lo pida»). El objetivo es que el alumnado aprenda a leer un error, no a pegar uno nuevo.
</div>

## Ejemplo 2 — Documentación técnica con citas (Módulo 2)

**Contexto:** el grupo trabaja con un framework y necesita una tabla de compatibilidad de versiones para el proyecto intermodular.

<div class="prompt-box">
<span class="label">Prompt en NotebookLM</span>
Con la documentación oficial y las notas de versión de este cuaderno:

1. Haz una tabla de compatibilidad entre las versiones del framework y la versión mínima del lenguaje.
2. Resume los tres cambios que más afectan a un proyecto pequeño.
3. Indica la fuente y la sección de cada fila.
4. Si hay versiones sin información, escribe «no consta».
5. No propongas código que no aparezca en las fuentes.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Una tabla con filas respaldadas por las notas de versión y tres cambios explicados en lenguaje claro. Las casillas sin dato quedan marcadas; no se rellenan por analogía.
</div>

**Comprobación:** se abre la sección citada de la documentación y se comprueba la versión mínima. La tabla se contrasta con el entorno real del proyecto.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Aprovecha para distinguir «documentación oficial», «notas de versión» y «entradas de blog». No tienen la misma fiabilidad y la tabla debe reflejarlo.
</div>

## Ejemplo 3 — Agente de novedades técnicas (Módulo 5)

**Contexto:** el docente quiere mantener actualizados los apuntes sin revisar manualmente cada semana.

<div class="prompt-box">
<span class="label">Objetivo del agente</span>
Cada viernes a las 18:00:
1. Revisa las notas de versión y los anuncios oficiales del framework indicado.
2. Selecciona solo cambios que afecten a los temas del módulo (lista adjunta).
3. Prepara un resumen de 200 palabras con enlace a cada fuente.
4. Añade un ejemplo mínimo por cada cambio relevante.
5. Guarda el resultado en la carpeta «novedades». No modifiques los apuntes.
6. Si no hay cambios relevantes, escribe «sin cambios» y termina.

Permisos: lectura de las fuentes y escritura solo en «novedades». No envíes correos ni publiques.
</div>

<div class="example-result">
<strong>Resultado esperado</strong>
Un documento semanal de tres o cuatro cambios, cada uno con enlace y ejemplo. Si no hay cambios que afecten al temario, una línea lo indica. Nada se publica sin revisión.
</div>

**Comprobación:** el docente abre los enlaces, ejecuta el ejemplo y decide si entra en los apuntes. Si el agente ha inventado una función, se descarta el documento entero y se revisa la lista de fuentes.

<div class="teacher-note">
  <strong>Nota docente</strong>
  Este es el caso de uso más rentable de un agente en FP: tareas de vigilancia, no de producción. Empieza con permisos de lectura y una carpeta de salida separada.
</div>

## Qué evitar en este nivel

| Práctica | Riesgo | Alternativa |
| --- | --- | --- |
| Aceptar código que compila | Deuda técnica y nula autoría | Explicar decisiones y cubrir casos límite |
| Pedir la solución completa | Se pierde el aprendizaje del error | Tutor que pregunta y da pistas |
| Documentar con texto generado sin revisar | Errores de versión y enlaces muertos | Citas a documentación oficial |
| Agente con acceso total al repositorio | Cambios no revisados | Permisos mínimos y rama de pruebas |

## Módulos relacionados

- [Módulo 1 · Habla con la IA](/modulos/1-habla-con-la-ia/)
- [Módulo 2 · Sistema de estudio](/modulos/2-sistema-de-estudio/)
- [Módulo 3 · La IA como profesor](/modulos/3-ia-como-profesor/)
- [Módulo 5 · Agentes para principiantes](/modulos/5-agentes/)
