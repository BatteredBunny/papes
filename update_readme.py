#!/usr/bin/env python3
from pathlib import Path
import re

IMAGE_DIR = Path("images")
README = Path("README.md")
COLS = 2

MARK_START = "<!-- WALLPAPER_GALLERY -->"
MARK_END = "<!-- END_WALLPAPER_GALLERY -->"


def generate_table() -> str:
    images = sorted(IMAGE_DIR.iterdir(), key=lambda p: (p.suffix.lower(), p.name))

    rows = [images[i : i + COLS] for i in range(0, len(images), COLS)]

    markdown = f"{MARK_START}\n# Wallpaper Gallery\n"

    # Table header
    markdown += "| " * (COLS + 1) + "\n"
    markdown += "|" + "---|" * COLS + "\n"

    for row in rows:
        row_md = (
            "| " + " | ".join(f'<img src="{img}" width="400">' for img in row) + " |\n"
        )
        markdown += row_md

    markdown += f"{MARK_END}\n"

    return markdown


def upsert_gallery(readme: str) -> str:
    block_re = re.compile(rf"{MARK_START}\n(.+\n)+{MARK_END}\n", flags=re.DOTALL)

    new_block = generate_table()
    if block_re.search(readme):
        return block_re.sub(new_block, readme)
    else:
        return readme.rstrip() + "\n\n" + new_block


def main():
    text = README.read_text()
    updated = upsert_gallery(text)
    if text != updated:
        README.write_text(updated)
        print("README.md updated.")
    else:
        print("README.md already up to date.")


if __name__ == "__main__":
    main()
