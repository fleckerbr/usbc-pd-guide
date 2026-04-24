from __future__ import annotations

import re
from dataclasses import dataclass
from re import Match

from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page


@dataclass(frozen=True, slots=True)
class Anchor:
    value: str
    href: str


def get_anchors(markdown: str, *, page: Page, files: Files) -> list[Anchor]:
    anchors: list[Anchor] = []

    def replace(match: Match[str]) -> str: ...

    markdown = re.sub(r"![[(.+)]]", replace, markdown, flags=re.I)

    return anchors
