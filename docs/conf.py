project = "pytermux"
author = "MrRare2"
version = "1.0.1"
full = version
desc = "pytermux - interact with Termux:API in Python"
html_short_title = desc
needs_sphinx = "2.0"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

highlight_language = "python3"

add_function_parentheses = False

html_theme_options = {
    "show_powered_by": False,
    "github_user": "MrRare2",
    "github_repo": project,
    "github_banner": True,
    "show_related": False,
}

html_show_sourcelink = False
htmlhelp_basename = project + "doc"
epub_exclude_files = ["search.html"]


