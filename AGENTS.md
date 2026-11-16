# AGENTS.md — IA para estudiar

## Propósito del proyecto

Curso de formación docente sobre comunicación con IA y uso académico responsable. Dos materiales que deben mantenerse coherentes:

1. **Apuntes** en `src/content/docs/` (Astro 7 + Starlight). Son la fuente de verdad del contenido.
2. **Presentaciones resumen** en `input/` + entradas raíz `m01-…md` a `m05-…md` (Slidev). Una por módulo.

Cada módulo incluye, al final de su página, un apartado **Para el docente** con guion, tiempos, dudas previsibles y evaluación.

## Estilo de escritura

- Castellano de España, segunda persona del plural para el alumnado («vais a», «tenéis») y trato directo en las notas al profesorado.
- Frases cortas. Un concepto por párrafo. Ejemplos concretos antes que definiciones abstractas.
- Nada de promesas comerciales ni afirmaciones sobre herramientas que puedan caducar sin fecha. Indicar «a fecha de este curso» al describir una función de una plataforma.
- Nombres de herramientas como los usa el fabricante: ChatGPT, Gemini, Claude, NotebookLM, GPTs, Gems, Compilatio.
- Español inclusivo sin artificios: «el alumnado», «el profesorado», «quien».

## Reglas de contenido

- **No hay boletines ni ejercicios.** El material práctico son **ejemplos del tema por nivel educativo**, agrupados en `src/content/docs/niveles/`.
- Todo ejemplo debe incluir: **prompt completo**, **resultado esperado**, **cómo comprobarlo** y **nota docente**.
- No se inventan enlaces a resultados compartidos. Los enlaces apuntan a páginas del propio curso donde se muestra el resultado o a documentación oficial.
- No se incluyen capturas de cuentas personales ni datos reales de estudiantes. Los ejemplos usan datos ficticios.
- Cada módulo declara objetivos, duración, materiales y criterios de evaluación.
- La verificación es obligatoria en el discurso: ningún resultado de IA se da por bueno sin contraste con una fuente.

## Estructura de los apuntes

```text
src/content/docs/
├── index.mdx           # Portada (template: doc, con hero y barra lateral)
├── modulos/
│   ├── index.md
│   ├── 1-habla-con-la-ia.md
│   ├── 2-sistema-de-estudio.md
│   ├── 3-ia-como-profesor.md
│   ├── 4-tutoria-y-casos.md
│   └── 5-agentes.md
├── niveles/            # ESO, FPB, Bachillerato y cuatro ciclos formativos
├── docencia/           # Guía didáctica
└── recursos/           # Biblioteca de prompts, privacidad y ética
```

Cada módulo de apuntes sigue este orden:

1. Ficha del módulo (duración, objetivos, materiales).
2. Contenido con ejemplos y tablas.
3. Ejemplo práctico completo y enlace a la página de nivel.
4. Errores frecuentes.
5. Adaptación por niveles (enlaces a `niveles/`).
6. **Para el docente**: guion con tiempos, dudas previsibles, evaluación y materiales.

## Presentaciones Slidev

- Entrada raíz: frontmatter con `theme: seriph`, `title`, `author`, `fonts`, `codeCopy: false` y `src: ./input/<archivo>.md`.
- Fuente en `input/`: sin `theme:`; solo `layout:` de cada diapositiva.
- Usar `layout: cover` únicamente en la primera diapositiva y `layout: closing` en la última.
- Una idea por diapositiva. Máximo aproximado: 6 líneas de texto o una tabla de 6 filas.
- Clases disponibles: `.info`, `.warning`, `.success`, `.step`, `.comparison-grid`, `.prompt-box`, `.teacher-note`, `.checklist`, `.two-cols`, `.badge`, `compact-slide`, `sparse-slide`.
- No dejar líneas en blanco dentro de un `<div>` de componente: el bloque HTML termina y el contenido queda fuera.
- El cierre va vacío: el layout ya compone el fondo.
- Cada presentación incluye el esquema del módulo, dos esquemas de apoyo y una foto de contexto, además de ejemplos resueltos. El build de los decks se hace con `npm run presentaciones:build`; `npm run apuntes:build` lo ejecuta después de Astro para publicarlos en `/presentaciones/m01/` a `/presentaciones/m05/`.

## Verificación

Antes de dar por terminado un cambio:

```bash
npm run apuntes:build
npm run build -- m01-habla-con-la-ia.md --out dist/m01
```

El sitio debe generar 20 páginas y cinco decks en `.apuntes-dist/presentaciones/`, con Node 22, y no debe haber enlaces internos rotos. El curso se sirve en `/IAParaEstudiar/`: comprobar que los enlaces Markdown llevan el prefijo (lo aplica `src/integrations/base-links.mjs`) y que no quedan rutas al sistema de archivos ni enlaces `TODO`.

## Licencia y autoría

- Licencia CC BY-SA 4.0. El contenido puede reutilizarse citando autoría.
- En los commits no se añaden nombres de terceros ni pies de herramientas generativas.
