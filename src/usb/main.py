from __future__ import annotations

import re
import sys
from pathlib import Path

from usb.data import Registers

REGISTER_DATA_SOURCE_FILE = Path.cwd() / "src" / "usb" / "data" / "registers.yaml"
REGISTER_MARKDOWN_DIRECTORY = Path.cwd() / "docs" / "port-controller" / "registers"
REGISTER_HYPERLINKS_PATH = Path() / "usbc-pd-guide" / "port-controller" / "registers"
REGISTER_HYPERLINKS_FILE = Path.cwd() / "includes" / "port-controller" / "register-hyperlinks.md"


def run() -> None:
    with REGISTER_DATA_SOURCE_FILE.open("r") as file:
        registers = Registers.load(file)

    hyperlinks = registers.hyperlinks(REGISTER_HYPERLINKS_PATH)

    def hyperlink(match: re.Match[str]) -> str:
        for line in hyperlinks.splitlines():
            if len(kv := line.split(": ", 1)) == 2:
                key, link = kv
                if match.group("link") == key:
                    return f"[{match.group('text')}]({link})"

        raise KeyError(f"No hyperlink with key: {match.group('link')}")

    match sys.argv[1:2][0]:
        case "--hyperlinks":
            with REGISTER_HYPERLINKS_FILE.open("w") as file:
                file.write("<!-- WARNING -- This file is auto-generated and changes will not be saved -->\n\n")  # fmt: skip
                file.write(hyperlinks)
        case "--registers":
            for register in registers:
                register_file = f"{register.name.lower().replace('_', '-')}.md"
                with REGISTER_MARKDOWN_DIRECTORY.joinpath(register_file).open("w") as file:
                    page = register.markdown_page()
                    page = re.sub(r"(?:\[(?P<text>[^]]+)\]\((?P<link>\[[^]]+\])\))", hyperlink, page)  # fmt: skip

                    file.write("<!-- WARNING -- This file is auto-generated and changes will not be saved -->\n\n")  # fmt: skip
                    file.write(page)
        case opt1:
            print(f"Invalid option: {opt1}")


if __name__ == "__main__":
    run()
