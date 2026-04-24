from __future__ import annotations

import re
from functools import partial
from pathlib import Path
from re import Match

from mkdocs.plugins import get_plugin_logger
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

from usbdoc.resolve import resolve_path

log = get_plugin_logger(__name__)


class Autolinker:
    def __init__(self, file: Path) -> None:
        with file.open("r") as textio:
            text = textio.read()

        self.links: dict[str, str] = {
            match.group("text"): match.group("link")
            for match in re.finditer(
                pattern=r"^\[\[(?P<text>.+)\]\]\s*:\s*(?P<link>.+)$",
                string=text,
                flags=re.MULTILINE,
            )
        }

    def autolink(self, markdown: str, page: Page, files: Files) -> str:
        page_links = self.page_links(page, files)
        markdown = re.sub(
            pattern=r"\[\[(?P<text>.+)\]\]\((?P<autolink>.+?)\)",
            repl=partial(self._replace_helperlink, page_links),
            string=markdown,
        )
        markdown = re.sub(
            pattern=r"\[\[(?P<autolink>.+)\]\]",
            repl=partial(self._replace_autolink, page_links),
            string=markdown,
        )
        return markdown

    def page_links(self, page: Page, files: Files) -> dict[str, str]:
        return {key: resolve_path(link, page, files) for key, link in self.links.items()}

    def _replace_autolink(self, links: dict[str, str], match: Match[str]) -> str:
        link = links.get(autolink := match.group("autolink"), None)
        if link is None:
            log.warning(f"Unrecognized autolink: {repr(autolink)}")
            return f"[[{autolink}]]"
        return f"[{autolink}]({link})"

    def _replace_helperlink(self, links: dict[str, str], match: Match[str]) -> str:
        link = links.get(autolink := match.group("autolink"), None)
        if link is None:
            log.warning(f"Unrecognized autolink: {repr(autolink)}")
            return f"[[{match.group('text')}]]({autolink})"
        return f"[{match.group('text')}]({link})"
