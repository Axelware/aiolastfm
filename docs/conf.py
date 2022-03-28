# Future
from __future__ import annotations

# Standard Library
import os
import re
import sys
from typing import Any


#######################
# Project Information #
#######################

project: str = "aiolastfm"
author: str = "Axel#3456"
copyright: str = "2022 Axelancerr"

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../aiolastfm/__init__.py'))) as file:
    version: str = re.search(r"^__version__: [^=]* = \"([^\"]*)\"", file.read(), re.MULTILINE).group(1)
    release: str = version


#########################
# General Configuration #
#########################

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("extensions"))

extensions: list[str] = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinxcontrib_trio",
    "resource_links",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]

needs_sphinx: str = "4.5.0"


###########################
# Options for HTML output #
###########################

html_theme: str = "furo"
html_theme_options: dict[str, Any] = {
    "dark_css_variables": {
        "color-brand-primary": "#ba0000",
        "color-brand-content": "#ba0000",
    },
    "footer_icons":       [
        {
            "name":  "Discord",
            "url":   "https://discord.com/invite/w9f6NkQbde",
            "html":  """<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M6.552 6.712c-.456 0-.816.4-.816.888s.368.888.816.888c.456 0 .816-.4.816-.888.008-.488-.36-.888-.816-.888zm2.92 0c-.456 0-.816.4-.816.888s.368.888.816.888c.456 0 .816-.4.816-.888s-.36-.888-.816-.888z"></path><path d="M13.36 0H2.64C1.736 0 1 .736 1 1.648v10.816c0 .912.736 1.648 1.64 1.648h9.072l-.424-1.48 1.024.952.968.896L15 16V1.648C15 .736 14.264 0 13.36 0zm-3.088 10.448s-.288-.344-.528-.648c1.048-.296 1.448-.952 1.448-.952-.328.216-.64.368-.92.472-.4.168-.784.28-1.16.344a5.604 5.604 0 0 1-2.072-.008 6.716 6.716 0 0 1-1.176-.344 4.688 4.688 0 0 1-.584-.272c-.024-.016-.048-.024-.072-.04-.016-.008-.024-.016-.032-.024-.144-.08-.224-.136-.224-.136s.384.64 1.4.944c-.24.304-.536.664-.536.664-1.768-.056-2.44-1.216-2.44-1.216 0-2.576 1.152-4.664 1.152-4.664 1.152-.864 2.248-.84 2.248-.84l.08.096c-1.44.416-2.104 1.048-2.104 1.048s.176-.096.472-.232c.856-.376 1.536-.48 1.816-.504.048-.008.088-.016.136-.016a6.521 6.521 0 0 1 4.024.752s-.632-.6-1.992-1.016l.112-.128s1.096-.024 2.248.84c0 0 1.152 2.088 1.152 4.664 0 0-.68 1.16-2.448 1.216z"></path></svg>""",
            "class": "",
        },
    ],
}
html_title: str = "aiolastfm"


##############
# Extensions #
##############

napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True

autodoc_typehints = "description"
autodoc_member_order = "bysource"

extlinks = {
    "issue": ("https://github.com/Axelware/aiolastfm/issues/%s", "GH-"),
}

intersphinx_mapping = {
    'aiohttp': ('https://docs.aiohttp.org/en/stable/', None),
    'python':  ('https://docs.python.org/3.10', None),
    'discord': ('https://discordpy.readthedocs.io/en/latest', None),
}

resource_links = {
    "github":      "https://github.com/Axelware/aiolastfm",
    "issues":      "https://github.com/Axelware/aiolastfm/issues",
    "discussions": "https://github.com/Axelware/aiolastfm/discussions",

    "examples":    "https://github.com/Axelware/aiolastfm/tree/main/examples",

    "discord":     "https://discord.com/invite/w9f6NkQbde",

}
