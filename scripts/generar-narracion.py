#!/usr/bin/env python3
"""Genera la narración de cada diapositiva con Edge TTS.

Uso:
    python3 scripts/generar-narracion.py            # solo las que faltan
    python3 scripts/generar-narracion.py --force    # regenera todo
    python3 scripts/generar-narracion.py m01 m03    # solo esos decks

Los MP3 se guardan en public/audio/<deck>/<número>.mp3. El componente
global-bottom.vue los reproduce y sigue el cambio de diapositiva.
"""

from __future__ import annotations

import argparse
import asyncio
import html
import re
import sys
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent
VOICE = "es-ES-AlvaroNeural"
RATE = "+5%"
PITCH = "-2Hz"
MAX_CHARS = 820

DECKS = {
    "m01": "input/m01-habla-con-la-ia.md",
    "m02": "input/m02-sistema-de-estudio.md",
    "m03": "input/m03-ia-como-profesor.md",
    "m04": "input/m04-tutoria-y-casos.md",
    "m05": "input/m05-agentes.md",
}


def split_slides(text: str) -> list[tuple[str, str]]:
    """Devuelve [(frontmatter, contenido)] de un Markdown de Slidev."""
    segments = re.split(r"(?m)^---\s*$", text)
    slides: list[tuple[str, str]] = []
    pending = ""
    for segment in segments:
        clean = segment.strip()
        if not clean:
            continue
        # Un bloque solo de claves YAML es el frontmatter de la diapositiva.
        lines = [line for line in clean.splitlines() if line.strip()]
        is_yaml = all(
            not line.startswith(("#", "-", ">", "<", "|", "!"))
            and re.match(r"^[\w-]+\s*:", line)
            for line in lines
        )
        if is_yaml and len(lines) <= 8:
            pending = clean
            continue
        slides.append((pending, clean))
        pending = ""
    return slides


def plain_text(markdown: str) -> str:
    """Convierte el Markdown visible en texto narrable, sin leer código."""
    text = markdown

    # Los prompts largos se resumen: en pantalla ya están completos.
    prompts = re.findall(
        r'<div class="prompt-box">(.*?)</div>', text, flags=re.DOTALL | re.IGNORECASE
    )
    text = re.sub(
        r'<div class="prompt-box">.*?</div>',
        " En pantalla tienes el ejemplo completo. Léelo y adáptalo a tu materia. ",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    # Tablas: cada fila se convierte en una frase corta.
    rows: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", cell) for cell in cells if cell):
            continue
        cells = [cell for cell in cells if cell]
        if cells:
            rows.append(". ".join(cells))
    text = re.sub(r"(?m)^\|.*\|$", "", text)

    # Enlaces, imágenes y HTML.
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)

    # Marcado y símbolos que la voz leería mal.
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"(?m)^\s{0,3}#{1,6}\s*", "", text)
    text = re.sub(r"(?m)^\s*[-*+]\s+", "", text)
    text = re.sub(r"(?m)^\s*\d+[.)]\s+", "", text)
    text = re.sub(r"[*_~>#|]", " ", text)
    text = re.sub(r"[✓✔→←↓↑●•·]", " ", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\s+", " ", text).strip(" .,:;")

    if not text and prompts:
        text = re.sub(r"<[^>]+>", " ", prompts[0])
        text = re.sub(r"\s+", " ", text).strip()

    if rows:
        text = f"{text}. {' '.join(rows)}" if text else " ".join(rows)

    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > MAX_CHARS:
        cut = text[:MAX_CHARS].rsplit(" ", 1)[0]
        text = f"{cut}."
    return text


def narration_for(frontmatter: str, content: str, index: int) -> str:
    text = plain_text(content)
    if not text:
        return ""
    if "layout: cover" in frontmatter:
        return f"Módulo. {text}"
    if "layout: closing" in frontmatter:
        return f"Para terminar. {text}"
    return text


async def synthesize(text: str, destination: Path, semaphore: asyncio.Semaphore) -> None:
    async with semaphore:
        destination.parent.mkdir(parents=True, exist_ok=True)
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        await communicate.save(str(destination))


async def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("decks", nargs="*", choices=sorted(DECKS), help="decks concretos")
    parser.add_argument("--force", action="store_true", help="regenera aunque exista")
    args = parser.parse_args()

    selected = args.decks or list(DECKS)
    semaphore = asyncio.Semaphore(4)
    jobs: list[tuple[str, Path, str]] = []

    for deck in selected:
        source = ROOT / DECKS[deck]
        slides = split_slides(source.read_text(encoding="utf-8"))
        print(f"{deck}: {len(slides)} diapositivas")
        for index, (frontmatter, content) in enumerate(slides, start=1):
            text = narration_for(frontmatter, content, index)
            if not text:
                print(f"  {index:02d}: sin texto, se omite")
                continue
            destination = ROOT / "public" / "audio" / deck / f"{index:02d}.mp3"
            if destination.exists() and not args.force:
                continue
            jobs.append((deck, destination, text))

    if not jobs:
        print("No hay audio que generar.")
        return 0

    print(f"Generando {len(jobs)} pistas con {VOICE}…")
    await asyncio.gather(*(synthesize(text, dest, semaphore) for _, dest, text in jobs))
    for deck, destination, _ in jobs:
        print(f"  {deck}/{destination.name}")
    print("Narración generada.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(asyncio.run(main()))
    except KeyboardInterrupt:
        sys.exit(130)
