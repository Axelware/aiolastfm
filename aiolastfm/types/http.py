# Future
from __future__ import annotations

# Standard Library
from typing import Literal


Headers = dict[str, str]

HTTPMethod = Literal[
    "GET",
    "POST"
]
APIMethod = Literal[
    "album.addTags",
    "album.getInfo",
    "album.getTags",
    "album.removeTag",
    "album.search",
]
