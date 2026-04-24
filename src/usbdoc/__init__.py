from __future__ import annotations

from pathlib import Path

from mkdocs.config.base import Config
from mkdocs.config.config_options import Type as ConfigType
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import ConfigurationError
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

from usbdoc.autolinks import Autolinker


class USBDocConfig(Config):
    autolinks = ConfigType(str | None, default=None)


class USBDocPlugin(BasePlugin[USBDocConfig]):
    def __init__(self) -> None:
        self.autolinker: Autolinker | None = None

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig | None:
        """
        The `config` event is the first event called on build and is run immediately
        after the user configuration is loaded and validated. Any alterations to the
        config should be made here.

        Parameters:
        - `config` - Global configuration object

        Returns:
        - Global configuration object
        """

        if self.config.autolinks is not None:
            autolinks_file = Path.cwd().joinpath(self.config.autolinks)
            if not autolinks_file.is_file():
                file = autolinks_file.as_posix()
                raise ConfigurationError(f'Autolink definition file does not exist: "{file}"')
            self.autolinker = Autolinker(autolinks_file)

        return config

    def on_page_markdown(
        self,
        markdown: str,
        *,
        page: Page,
        config: MkDocsConfig,
        files: Files,
    ) -> str | None:
        """MkDocs `page_markdown` event handler.

        The `page_markdown` event is called after the page's markdown is loaded from file and can be used to alter the Markdown source text.
        The meta-data has been stripped off and is available as `page.meta` at this point.

        Parameters:
        - `markdown` - Markdown source text of page as string
        - `page` - `mkdocs.structure.pages.Page` instance
        - `config` - Global configuration object
        - `files` - Global files collection

        Returns:
        - Markdown source text of page as string
        """

        if self.autolinker is not None:
            markdown = self.autolinker.autolink(markdown, page, files)

        return markdown
