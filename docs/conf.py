# -- Project information -----------------------------------------------------

project = "Enchanted-Book"
copyright = "2024, Enchanted Book Community"
author = "Enchanted Book"


# -- General configuration ---------------------------------------------------

extensions = [
	"myst_parser",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["en", "fr", "_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo-enchanted-book.svg"
html_favicon = "_static/logo-enchanted-book.svg"

html_context = {
	"github_user": "Enchanted-Book",
	"github_repo": "Enchanted-Book",
	"github_version": "main",
	"doc_path": "docs",
}


# -- PyData Theme options ----------------------------------------------------

html_theme_options = {
	"navbar_start": ["navbar-logo"],
	"navigation_with_keys": True,
	"use_edit_page_button": True,
	"header_links_before_dropdown": 4,
	"logo": {
		"text": "Enchanted Book",
	},
	"icon_links": [
		{
			"name": "GitHub",
			"url": "https://github.com/Enchanted-Book/Enchanted-Book",
			"icon": "fa-brands fa-github",
		},
	],
}
