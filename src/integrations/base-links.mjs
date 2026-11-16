import { readdir, readFile, writeFile } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

/**
 * GitHub Pages sirve el curso en /IAParaEstudiar/. Astro aplica la base a
 * sus propios enlaces y recursos, pero no a los href escritos en Markdown.
 * Esta integración los prefija en la build y en el servidor de desarrollo.
 */
export default function baseLinks(options = {}) {
  const base = (options.base || '').replace(/\/$/, '')

  const prefix = (url) => {
    if (!url.startsWith('/') || url.startsWith('//')) return url
    if (url === base || url.startsWith(`${base}/`)) return url
    return `${base}${url}`
  }

  const rewriteHtml = (html) =>
    html.replace(/\b(href|src)="(\/[^"]*)"/g, (_, attribute, url) => `${attribute}="${prefix(url)}"`)

  const rewriteDirectory = async (directory) => {
    const entries = await readdir(directory, { withFileTypes: true })
    for (const entry of entries) {
      const fullPath = path.join(directory, entry.name)
      if (entry.isDirectory()) {
        await rewriteDirectory(fullPath)
      } else if (entry.name.endsWith('.html')) {
        const html = await readFile(fullPath, 'utf8')
        const rewritten = rewriteHtml(html)
        if (rewritten !== html) await writeFile(fullPath, rewritten)
      }
    }
  }

  return {
    name: 'ia-para-estudiar:base-links',
    hooks: {
      'astro:build:done': async ({ dir }) => {
        if (!base) return
        await rewriteDirectory(fileURLToPath(dir))
      },
      'astro:server:setup': ({ server }) => {
        if (!base) return
        server.middlewares.use((request, _response, next) => {
          const url = request.url || '/'
          const isInternalAsset = /^\/(@|_|node_modules|src\/|favicon\.ico)/.test(url)
          if (url === base || url.startsWith(`${base}/`) || isInternalAsset) {
            next()
            return
          }
          request.url = `${base}${url}`
          next()
        })
      },
    },
  }
}
