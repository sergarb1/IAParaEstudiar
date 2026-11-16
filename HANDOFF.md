# HANDOFF — IA para estudiar

Traspaso operativo para quien continúe el proyecto. Las reglas de contenido y estilo están en [`AGENTS.md`](AGENTS.md); los comandos y la estructura, en [`README.md`](README.md).

## Estado actual

- **Rama:** `main`, sincronizada con `origin/main`.
- **Último commit de referencia:** `634c96c Refuerza las presentaciones y añade narración con voz masculina`.
- **Web publicada:** <https://sergarb1.github.io/IAParaEstudiar/>
- **Presentaciones:** <https://sergarb1.github.io/IAParaEstudiar/presentaciones/>
- **Build:** correcto. Genera 31 archivos HTML, 5 decks y 84 MP3 en `.apuntes-dist/`.
- **Audio:** 84 pistas en `public/audio/m01`…`m05` (unos 11 MB).
- **Estado del árbol:** limpio tras el push.

## Qué está terminado

### Web

- Portada con entrada en tres pasos: nivel, método y aula.
- Cinco módulos numerados y siete ejemplos por nivel.
- Materiales en tarjetas, sin tabla apretada en móvil.
- Tablas desplazables en pantallas pequeñas.
- Barra lateral con etiquetas cortas.
- Terminología «Ciclos Formativos»; no usar «CFGS» ni «FP Superior».

### Presentaciones

| Deck | Diapositivas | Audio |
| --- | ---: | ---: |
| m01 · Habla con la IA | 18 | 18 |
| m02 · Sistema de estudio | 16 | 16 |
| m03 · IA como profesor | 17 | 17 |
| m04 · Tutoría y casos | 16 | 16 |
| m05 · Agentes | 17 | 17 |

- Sin diapositivas vacías ni desbordes en la última revisión.
- Los cierres incluyen resumen; no hay diapositiva «Gracias».
- Tres esquemas nuevos: `ciclo-prompt.svg`, `caso-tres-preguntas.svg` y `decidir-agente.svg`.

### Narración

- Voz de Edge TTS: `es-ES-AlvaroNeural`, ritmo `+5%`.
- Reproductor global en `global-bottom.vue`, visible desde la portada.
- El botón sigue el cambio de diapositiva y no bloquea las flechas del teclado.
- Los prompts largos no se leen literalmente: el script los resume para el audio.
- Documentación de regeneración en `README.md` y `AGENTS.md`.

## Cómo trabajar

```bash
export PATH=/tmp/node22/bin:$PATH   # Solo si Node 22 no es el Node activo

npm install
npm run apuntes:dev                 # http://localhost:4321/IAParaEstudiar/
npm run dev -- m01-habla-con-la-ia.md
npm run apuntes:build
```

La fuente de verdad del contenido son los apuntes de `src/content/docs/`. Las presentaciones de `input/` son un resumen y deben mantenerse coherentes con ellos.

## Verificación antes de publicar

1. Compilar el sitio completo:

   ```bash
   npm run apuntes:build
   ```

2. Comprobar que existen `.apuntes-dist/presentaciones/m01`…`m05` y que el número de MP3 coincide con el de diapositivas.
3. Revisar portada, página de presentaciones y un módulo en escritorio y móvil.
4. Abrir un deck compilado, pulsar **Narración**, avanzar una diapositiva y comprobar que cambia el MP3.
5. Si están disponibles los chequeadores externos de `PresentacionesEducativas`, pasar `check-empty.mjs` y `measure.mjs` a los cinco decks. No están versionados en este repositorio.

## Reglas que no se deben romper

- No añadir trabajo final, boletines ni ejercicios: el material práctico son ejemplos por nivel.
- Cada ejemplo debe incluir prompt, resultado esperado, comprobación y nota docente.
- No inventar enlaces, capturas ni datos de alumnado.
- No usar atribución de herramientas generativas en los commits.
- La verificación es parte del método: ningún resultado de IA se acepta sin contrastar la fuente.
- Si cambia el texto de una diapositiva, regenerar su audio y volver a compilar.

## Dónde continuar

- **Revisión humana de la narración completa:** la reproducción y el cambio de pista están probados, pero conviene escuchar los cinco decks seguidos antes de una sesión real.
- **Mantenimiento de recuentos:** al añadir o quitar diapositivas, actualizar la tabla de este handoff, la página de presentaciones y el audio.
- **Nuevos esquemas:** mantener el lenguaje visual propio y citar autoría/licencia cuando se use una imagen externa.
- **Publicación:** cada push a `main` ejecuta `.github/workflows/deploy.yml` y actualiza GitHub Pages.
