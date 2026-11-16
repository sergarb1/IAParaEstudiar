import { execFileSync } from 'node:child_process'
import { mkdirSync, rmSync } from 'node:fs'
import { resolve } from 'node:path'

const base = (process.env.SITE_BASE || '/IAParaEstudiar').replace(/\/$/, '')
const outRoot = '.apuntes-dist/presentaciones'
const decks = [
  ['m01', 'm01-habla-con-la-ia.md'],
  ['m02', 'm02-sistema-de-estudio.md'],
  ['m03', 'm03-ia-como-profesor.md'],
  ['m04', 'm04-tutoria-y-casos.md'],
  ['m05', 'm05-agentes.md'],
]

mkdirSync(outRoot, { recursive: true })
const slidev = resolve('node_modules/@slidev/cli/bin/slidev.mjs')

for (const [slug, entry] of decks) {
  console.log(`\n▶ Presentación ${slug}`)
  execFileSync(
    process.execPath,
    [
      slidev,
      'build',
      entry,
      '--out',
      `${outRoot}/${slug}`,
      '--base',
      `${base}/presentaciones/${slug}/`,
      '--router-mode',
      'hash',
    ],
    { stdio: 'inherit' },
  )
}

console.log(`\nPresentaciones generadas en ${outRoot}`)
