// @ts-check
import { defineConfig } from 'astro/config'
import starlight from '@astrojs/starlight'
import baseLinks from './src/integrations/base-links.mjs'

const base = '/IAParaEstudiar'

export default defineConfig({
  site: 'https://sergarb1.github.io',
  base,
  outDir: './.apuntes-dist',
  integrations: [
    baseLinks({ base }),
    starlight({
      title: 'IA para estudiar',
      description:
        'Curso para docentes: comunicar con la IA, construir un sistema de estudio y enseñar a usarla con criterio. Apuntes, presentaciones y ejemplos por nivel.',
      defaultLocale: 'es',
      locales: {
        root: { label: 'Español', lang: 'es' },
      },
      social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/sergarb1/IAParaEstudiar' }],
      customCss: ['./src/styles/custom.css'],
      lastUpdated: true,
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
      head: [
        {
          tag: 'link',
          attrs: { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        },
        {
          tag: 'link',
          attrs: { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        },
      ],
      sidebar: [
        {
          label: 'El curso',
          items: [
            { label: 'Vista general', link: '/modulos/' },
            { label: 'Módulo 1 · Habla con la IA', link: '/modulos/1-habla-con-la-ia/' },
            { label: 'Módulo 2 · Sistema de estudio', link: '/modulos/2-sistema-de-estudio/' },
            { label: 'Módulo 3 · La IA como profesor', link: '/modulos/3-ia-como-profesor/' },
            { label: 'Módulo 4 · Tutoría y casos', link: '/modulos/4-tutoria-y-casos/' },
            { label: 'Módulo 5 · Agentes para principiantes', link: '/modulos/5-agentes/' },
            { label: 'Presentaciones', link: '/presentaciones/' },
          ],
        },
        {
          label: 'Ejemplos por nivel',
          items: [
            { label: 'Cómo leer estos ejemplos', link: '/niveles/' },
            { label: 'ESO', link: '/niveles/eso/' },
            { label: 'FP Básica', link: '/niveles/fp-basica/' },
            { label: 'Bachillerato', link: '/niveles/bachillerato/' },
            { label: 'Ciclos Formativos · Informática', link: '/niveles/fp-informatica/' },
            { label: 'Ciclos Formativos · Administración', link: '/niveles/fp-administracion/' },
            { label: 'Ciclos Formativos · Comercio', link: '/niveles/fp-comercio/' },
            { label: 'Ciclos Formativos · Turismo', link: '/niveles/fp-turismo/' },
          ],
        },
        {
          label: 'Para el profesorado',
          items: [
            { label: 'Guía didáctica', link: '/docencia/guia-didactica/' },
          ],
        },
        {
          label: 'Recursos',
          items: [
            { label: 'Biblioteca de prompts', link: '/recursos/biblioteca-de-prompts/' },
            { label: 'Formas especiales de aprender', link: '/recursos/formas-especiales/' },
            { label: 'Privacidad, ética y evaluación', link: '/recursos/privacidad-y-etica/' },
          ],
        },
      ],
    }),
  ],
})
