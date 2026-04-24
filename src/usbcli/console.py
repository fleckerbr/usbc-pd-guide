from __future__ import annotations

from enum import IntEnum
from typing import Any

import rich
from rich.console import Console, JustifyMethod, OverflowMethod
from rich.style import Style


class LoggingLevel(IntEnum):
    ERROR = 0  # --quiet :: only errors
    INFO = 1  # <default> :: errors, warnings, and info
    DEBUG = 2  # --verbose :: errors, warnings, info, and debug


logging_level = LoggingLevel.ERROR
stdout: Console = rich.console.Console(stderr=False)
stderr: Console = rich.console.Console(stderr=True)


def init_logging(level: LoggingLevel) -> None:
    global logging_level
    logging_level = level


def write(
    *objects: Any,
    sep: str = " ",
    end: str = "\n",
    style: str | Style | None = None,
    justify: JustifyMethod | None = None,
    overflow: OverflowMethod | None = None,
    no_wrap: bool | None = None,
    emoji: bool | None = None,
    markup: bool | None = None,
    highlight: bool | None = None,
    width: int | None = None,
    height: int | None = None,
    crop: bool = True,
    soft_wrap: bool | None = None,
    new_line_start: bool = False,
) -> None:
    """Write objects to standard output."""
    stdout.print(
        *objects,
        sep=sep,
        end=end,
        style=style,
        justify=justify,
        overflow=overflow,
        no_wrap=no_wrap,
        emoji=emoji,
        markup=markup,
        highlight=highlight,
        width=width,
        height=height,
        crop=crop,
        soft_wrap=soft_wrap,
        new_line_start=new_line_start,
    )


def debug(
    *objects: Any,
    sep: str = " ",
    end: str = "\n",
    style: str | Style | None = None,
    justify: JustifyMethod | None = None,
    overflow: OverflowMethod | None = None,
    no_wrap: bool | None = None,
    emoji: bool | None = None,
    markup: bool | None = None,
    highlight: bool | None = None,
    width: int | None = None,
    height: int | None = None,
    crop: bool = True,
    soft_wrap: bool | None = None,
    new_line_start: bool = False,
) -> None:
    """Log debug to standard error."""
    if logging_level >= LoggingLevel.DEBUG:
        stderr.print(
            "[dim]Debug:[/]",
            *objects,
            sep=sep,
            end=end,
            style=style,
            justify=justify,
            overflow=overflow,
            no_wrap=no_wrap,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            width=width,
            height=height,
            crop=crop,
            soft_wrap=soft_wrap,
            new_line_start=new_line_start,
        )


def info(
    *objects: Any,
    sep: str = " ",
    end: str = "\n",
    style: str | Style | None = None,
    justify: JustifyMethod | None = None,
    overflow: OverflowMethod | None = None,
    no_wrap: bool | None = None,
    emoji: bool | None = None,
    markup: bool | None = None,
    highlight: bool | None = None,
    width: int | None = None,
    height: int | None = None,
    crop: bool = True,
    soft_wrap: bool | None = None,
    new_line_start: bool = False,
) -> None:
    """Log info to standard error."""
    if logging_level >= LoggingLevel.INFO:
        stderr.print(
            "[cyan]Info:[/]",
            *objects,
            sep=sep,
            end=end,
            style=style,
            justify=justify,
            overflow=overflow,
            no_wrap=no_wrap,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            width=width,
            height=height,
            crop=crop,
            soft_wrap=soft_wrap,
            new_line_start=new_line_start,
        )


def warning(
    *objects: Any,
    sep: str = " ",
    end: str = "\n",
    style: str | Style | None = None,
    justify: JustifyMethod | None = None,
    overflow: OverflowMethod | None = None,
    no_wrap: bool | None = None,
    emoji: bool | None = None,
    markup: bool | None = None,
    highlight: bool | None = None,
    width: int | None = None,
    height: int | None = None,
    crop: bool = True,
    soft_wrap: bool | None = None,
    new_line_start: bool = False,
) -> None:
    """Log warning to standard error."""
    if logging_level >= LoggingLevel.INFO:
        stderr.print(
            "[yellow]Warning:[/]",
            *objects,
            sep=sep,
            end=end,
            style=style,
            justify=justify,
            overflow=overflow,
            no_wrap=no_wrap,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            width=width,
            height=height,
            crop=crop,
            soft_wrap=soft_wrap,
            new_line_start=new_line_start,
        )


def error(
    *objects: Any,
    sep: str = " ",
    end: str = "\n",
    style: str | Style | None = None,
    justify: JustifyMethod | None = None,
    overflow: OverflowMethod | None = None,
    no_wrap: bool | None = None,
    emoji: bool | None = None,
    markup: bool | None = None,
    highlight: bool | None = None,
    width: int | None = None,
    height: int | None = None,
    crop: bool = True,
    soft_wrap: bool | None = None,
    new_line_start: bool = False,
) -> None:
    """Log error to standard error."""
    if logging_level >= LoggingLevel.ERROR:
        stderr.print(
            "[red]Error:[/]",
            *objects,
            sep=sep,
            end=end,
            style=style,
            justify=justify,
            overflow=overflow,
            no_wrap=no_wrap,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            width=width,
            height=height,
            crop=crop,
            soft_wrap=soft_wrap,
            new_line_start=new_line_start,
        )
