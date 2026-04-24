from __future__ import annotations

import errno
import os
import posixpath

from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page


def resolve_path(path: str, page: Page, files: Files) -> str:
    path, anchor, *_ = f"{path}#".split("#")
    if (file := files.get_file_from_path(path)) is None:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
    path = resolve_file(file, page)
    return "#".join([path, anchor]) if anchor else path


def resolve_file(file: File, page: Page) -> str:
    """Resolve the path to a file from a given page

    Args:
    - `file` - The target file
    - `page` - The page that the link should be relative to

    Returns:
    - A posix path to the file for use on the given page
    """
    path = posixpath.relpath(file.src_uri, page.file.src_uri)
    return posixpath.sep.join(path.split(posixpath.sep)[1:])
