"""Markdown Extensions"""

from __future__ import annotations

import errno
import os
import posixpath

from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page


# Resolve path of file relative to given page - the posixpath always includes
# one additional level of `..` which we need to remove
def resolve_path(path: str, page: Page, files: Files):
    path, anchor, *_ = f"{path}#".split("#")
    file = files.get_file_from_path(path)
    if file is None:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
    path = resolve(file, page)
    return "#".join([path, anchor]) if anchor else path


# Resolve path of file relative to given page - the posixpath always includes
# one additional level of `..` which we need to remove
def resolve(file: File, page: Page) -> str:
    path = posixpath.relpath(file.src_uri, page.file.src_uri)
    return posixpath.sep.join(path.split(posixpath.sep)[1:])
