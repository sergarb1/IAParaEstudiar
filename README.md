# IA para estudiar

Curso para docentes sobre cómo comunicarse con la inteligencia artificial y cómo enseñar a usarla con criterio. Incluye **apuntes** (Astro + Starlight), **presentaciones de apoyo** (Slidev, una por módulo, con esquemas y ejemplos resueltos) y **ejemplos del tema por nivel educativo**.

Sitio publicado: **https://sergarb1.github.io/IAParaEstudiar/**

Presentaciones: **https://sergarb1.github.io/IAParaEstudiar/presentaciones/**

## Contenido

| Módulo | Tema | Duración |
| --- | --- | --- |
| 1 | Habla con la IA: ChatGPT, Gemini, Claude y prompting | 2 h |
| 2 | Construye tu sistema de estudio con NotebookLM | 2 h |
| 3 | Convierte la IA en tu profesor: GPTs, Gems y técnicas | 2 h |
| 4 | Ponlo a prueba: tutoría, dudas y casos prácticos | 2 h |
| 5 | Usa agentes para principiantes | 2 h |

Además: ejemplos adaptados a ESO, FP Básica, Bachillerato y Ciclos Formativos de Informática, Administración, Comercio y Turismo; biblioteca de prompts; guía didáctica; formas especiales de aprender con analogías; criterios de privacidad y ética.

## Requisitos

- Node.js 22 (ver `.nvmrc`)
- `npm`

## Puesta en marcha

```bash
npm install

# Sitio de apuntes (http://localhost:4321/IAParaEstudiar/)
npm run apuntes:dev

# Una presentación concreta (http://localhost:3030)
npm run dev -- m01-habla-con-la-ia.md
```

## Estructura

```text
.
├── AGENTS.md                   # Reglas de contenido y estilo
├── HANDOFF.md                  # Estado actual y traspaso operativo
├── astro.config.mjs            # Configuración de Astro + Starlight
├── src/
│   ├── content.config.ts       # Colección «docs»
│   ├── content/docs/           # Apuntes
│   │   ├── index.mdx           # Portada
│   │   ├── modulos/            # Los 5 módulos
│   │   ├── niveles/            # Ejemplos por nivel educativo
│   │   ├── docencia/           # Guía didáctica
│   │   └── recursos/           # Prompts y privacidad
│   ├── integrations/           # Prefijo de base para enlaces internos
│   └── styles/custom.css       # Tema del sitio
├── input/                      # Markdown fuente de las presentaciones
├── m01-…m05-….md               # Entradas Slidev (tema, fuentes, src)
├── layouts/                    # Portada y cierre de las presentaciones
├── global-bottom.vue           # Reproductor de narración por diapositiva
├── styles/index.css            # Estilos compartidos de las diapositivas
├── public/                     # Favicon, imágenes y audio de la narración
├── scripts/generar-narracion.py # Genera los MP3 con Edge TTS
└── package.json
```

## Comandos

| Comando | Descripción |
| --- | --- |
| `npm run apuntes:dev` | Sirve los apuntes en desarrollo |
| `npm run apuntes:build` | Genera el sitio y las cinco presentaciones en `.apuntes-dist/` |
| `npm run presentaciones:build` | Genera solo los decks Slidev en `.apuntes-dist/presentaciones/` |
| `npm run narracion:generar` | Genera la narración de cada diapositiva con Edge TTS (`es-ES-AlvaroNeural`) |
| `npm run apuntes:preview` | Previsualiza el sitio generado |
| `npm run dev -- <entrada>.md` | Abre una presentación en desarrollo |
| `npm run build -- <entrada>.md --out dist/<nombre>` | Genera una presentación estática |
| `npm run export -- <entrada>.md --format pdf --output output/<nombre>.pdf` | Exporta a PDF |

## Publicación

GitHub Actions compila el sitio con Node 22 y lo publica en GitHub Pages mediante `.github/workflows/deploy.yml`. Cada push a `main` actualiza **https://sergarb1.github.io/IAParaEstudiar/**.

El sitio se sirve en el subdirectorio `/IAParaEstudiar/`; ese valor está en `base` dentro de `astro.config.mjs` y los enlaces internos se prefijan automáticamente con `src/integrations/base-links.mjs`.

La narración se genera con `npm run narracion:generar` (requiere `edge-tts`) y se guarda en `public/audio/m01`…`m05`. El botón **Narración** de cada deck reproduce el MP3 de la diapositiva actual y sigue avanzando con ella.

## Licencia

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) © Sergi García Barea.
