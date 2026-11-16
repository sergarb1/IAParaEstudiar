---
title: Presentaciones
description: "Cinco presentaciones de apoyo creadas con Slidev para proyectar en el aula, con esquemas, ejemplos resueltos y fotos."
---

Cada módulo tiene una **presentación de apoyo** para proyectar en clase. Están hechas con Slidev, se abren en el navegador y no necesitan instalar nada. Cada deck incluye entre 15 y 18 diapositivas, tres esquemas propios, una foto de contexto, ejemplos resueltos de distintas materias y **narración en español con voz masculina**.

La narración no lee los prompts largos: explica la idea de la diapositiva y deja el texto completo en pantalla. Se activa con el botón **Narración** de la esquina inferior derecha y, una vez activada, sigue el cambio de diapositiva.

<div class="presentation-grid">
  <a class="presentation-card" href="/presentaciones/m01/">
    <img src="/imagenes/nivel-eso.jpg" alt="Aula de secundaria" width="1280" height="720" loading="lazy" />
    <div class="presentation-card-body">
      <span class="presentation-kicker">Módulo 1</span>
      <h3>Habla con la IA</h3>
      <p>Qué hace un modelo, qué herramienta elegir y cómo construir una instrucción precisa.</p>
      <span class="presentation-open">Abrir presentación →</span>
    </div>
  </a>
  <a class="presentation-card" href="/presentaciones/m02/">
    <img src="/imagenes/nivel-bachillerato.jpg" alt="Biblioteca con mesas de lectura" width="1280" height="720" loading="lazy" />
    <div class="presentation-card-body">
      <span class="presentation-kicker">Módulo 2</span>
      <h3>Construye tu sistema de estudio</h3>
      <p>NotebookLM, fuentes con criterio, citas y una rutina que no depende del chat.</p>
      <span class="presentation-open">Abrir presentación →</span>
    </div>
  </a>
  <a class="presentation-card" href="/presentaciones/m03/">
    <img src="/imagenes/nivel-fp-administracion.jpg" alt="Bandejas de documentación en una oficina" width="1280" height="720" loading="lazy" />
    <div class="presentation-card-body">
      <span class="presentation-kicker">Módulo 3</span>
      <h3>Convierte la IA en tu profesor</h3>
      <p>Tutor personalizado, recuperación activa, simulacros y verificación con criterio.</p>
      <span class="presentation-open">Abrir presentación →</span>
    </div>
  </a>
  <a class="presentation-card" href="/presentaciones/m04/">
    <img src="/imagenes/nivel-fp-comercio.jpg" alt="Interior de una tienda de ropa" width="1280" height="720" loading="lazy" />
    <div class="presentation-card-body">
      <span class="presentation-kicker">Módulo 4</span>
      <h3>Ponlo a prueba</h3>
      <p>Casos reales, afirmaciones que no se sostienen y un plan para llevarlo al aula.</p>
      <span class="presentation-open">Abrir presentación →</span>
    </div>
  </a>
  <a class="presentation-card" href="/presentaciones/m05/">
    <img src="/imagenes/nivel-fp-informatica.jpg" alt="Laboratorio de informática" width="1280" height="720" loading="lazy" />
    <div class="presentation-card-body">
      <span class="presentation-kicker">Módulo 5</span>
      <h3>Agentes para principiantes</h3>
      <p>Objetivo, herramientas, permisos, parada y revisión humana.</p>
      <span class="presentation-open">Abrir presentación →</span>
    </div>
  </a>
</div>

## Cómo usarlas en clase

<div class="checklist">

- **Flechas o espacio:** avanzar. **Shift + flecha:** retroceder.
- **O:** vista general de diapositivas. **F:** pantalla completa. **?:** atajos.
- **Móvil u ordenador:** funcionan en ambos. No requieren cuenta.
- **Narración:** pulsa **Narración** abajo a la derecha. El botón cambia a **Pausar**; al avanzar, la voz continúa en la siguiente diapositiva.
- **Antes de proyectar:** abre el deck en el equipo del aula y comprueba el sonido si vas a usar la narración o un vídeo.
</div>

<div class="teacher-note">
  <strong>Material vivo</strong>
  Las presentaciones se generan con Slidev a partir de los archivos <code>input/m01-…</code> a <code>input/m05-…</code>. Si cambias un módulo, actualiza también su deck y vuelve a compilar: <code>npm run presentaciones:build</code>.
</div>

## Módulos y apuntes

- [Módulo 1 · Habla con la IA](/modulos/1-habla-con-la-ia/)
- [Módulo 2 · Sistema de estudio](/modulos/2-sistema-de-estudio/)
- [Módulo 3 · La IA como profesor](/modulos/3-ia-como-profesor/)
- [Módulo 4 · Ponlo a prueba](/modulos/4-tutoria-y-casos/)
- [Módulo 5 · Agentes](/modulos/5-agentes/)
