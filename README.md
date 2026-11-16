# IA para estudiar

Curso para docentes sobre cómo comunicarse con la inteligencia artificial y cómo enseñar a usarla con criterio. Incluye **apuntes** (Astro + Starlight), **presentaciones resumen** (Slidev, una por módulo) y **ejemplos del tema por nivel educativo**.

El sitio sigue el estilo de [Apuntes PSP](https://sergarb1.github.io/ApuntesPSP/): documentación navegable, ejemplos por etapa y licencia CC BY-SA.

## Contenido

| Módulo | Tema | Duración |
| --- | --- | --- |
| 1 | Habla con la IA: ChatGPT, Gemini, Claude y prompting | 2 h |
| 2 | Construye tu sistema de estudio con NotebookLM | 2 h |
| 3 | Convierte la IA en tu profesor: GPTs, Gems y técnicas | 2 h |
| 4 | Ponlo a prueba: tutoría, dudas y casos prácticos | 2 h |
| 5 | Usa agentes para principiantes | 2 h |

Además: ejemplos adaptados a ESO, FP Básica, Bachillerato y FP Superior de Informática, Administración, Comercio y Turismo; biblioteca de prompts; guía didáctica; trabajo final con rúbrica y criterios de privacidad y ética.

## Requisitos

- Node.js 20 o superior
- `npm`

## Puesta en marcha

```bash
npm install

# Sitio de apuntes (http://localhost:4321)
npm run apuntes:dev

# Una presentación concreta (http://localhost:3030)
npm run dev -- m01-habla-con-la-ia.md
```

## Estructura

```text
.
├── astro.config.mjs            # Configuración de Astro + Starlight
├── src/
│   ├── content.config.ts       # Colección «docs»
│   ├── content/docs/           # Apuntes
│   │   ├── index.mdx           # Portada
│   │   ├── modulos/            # Los 5 módulos
│   │   ├── niveles/            # Ejemplos por nivel educativo
│   │   ├── docencia/           # Guía didáctica y trabajo final
│   │   └── recursos/           # Prompts y privacidad
│   └── styles/custom.css       # Tema del sitio
├── input/                      # Markdown fuente de las presentaciones
├── m01-…m05-….md               # Entradas Slidev (tema, fuentes, src)
├── layouts/                    # Portada y cierre de las presentaciones
├── styles/index.css            # Estilos compartidos de las diapositivas
├── public/                     # Favicon y recursos servibles
└── package.json
```

## Comandos

| Comando | Descripción |
| --- | --- |
| `npm run apuntes:dev` | Sirve los apuntes en desarrollo |
| `npm run apuntes:build` | Genera el sitio estático en `.apuntes-dist/` |
| `npm run apuntes:preview` | Previsualiza el sitio generado |
| `npm run dev -- <entrada>.md` | Abre una presentación en desarrollo |
| `npm run build -- <entrada>.md --out dist/<nombre>` | Genera una presentación estática |
| `npm run export -- <entrada>.md --format pdf --output output/<nombre>.pdf` | Exporta a PDF |

## Publicación

El sitio de apuntes se publica en GitHub Pages compilando con `npm run apuntes:build` y sirviendo `.apuntes-dist/`.

Si el repositorio se publica en un subdirectorio (`usuario.github.io/repositorio/`), añade `base: '/repositorio/'` en `astro.config.mjs` antes de compilar y ajusta los enlaces de las presentaciones.

## Licencia

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) © Sergi García Barea.
