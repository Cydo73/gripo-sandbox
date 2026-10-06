# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "GripoFlow Sandbox Guides"
copyright = "2026, Mumpe Cydrone"
author = "Mumpe Cydrone"
release = "1.0"

# -- General configuration ---------------------------------------------
extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output ---------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]

html_title = "GripoFlow Sandbox Guides"

html_theme_options = {
    "sidebar_hide_name": False,
}
