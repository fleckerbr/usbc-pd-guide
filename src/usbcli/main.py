from __future__ import annotations

import traceback
from importlib import metadata
from typing import Annotated, NoReturn

import rich
from cyclopts import App, Parameter

from usbcli import console
from usbcli.console import LoggingLevel

app = App(version=metadata.version("usb"), help_format="rich")


@app.default
def main(
    *,
    verbose: Annotated[
        bool | None,
        Parameter(
            name=["--verbose", "-v"],
            negative=["--quiet", "-q"],
            help="Logging output verbosity.",
        ),
    ] = None,
) -> None:
    match verbose:
        case True:
            logging_level = LoggingLevel.DEBUG
        case None:
            logging_level = LoggingLevel.INFO
        case False:
            logging_level = LoggingLevel.ERROR

    console.init_logging(logging_level)
    console.info(f"{verbose=}")


def run() -> NoReturn:
    try:
        app()
    except KeyboardInterrupt:
        rich.print("[red]Aborted![/]")
    except Exception as error:
        traceback.print_exception(error)
        raise error

    exit(0)


if __name__ == "__main__":
    run()
