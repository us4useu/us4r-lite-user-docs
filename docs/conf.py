# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime

html_theme = 'sphinx_rtd_theme'
html_logo = "_static/us4us-logo-white.png"

current_year = datetime.now().year

# -- Project information -----------------------------------------------------

project = 'us4R™ User Manual'
copyright = f"{current_year}, us4us Ltd"
author = 'us4us Ltd'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinxcontrib.jquery"
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

html_theme_options = {
    'logo_only': True,
    # Set the name of the project to appear in the sidebar
}

html_css_files = [
    'custom.css',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

numfig = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'

latex_documents = [('index', 'user_manual.tex', project, author, 'manual')]


warning_color = "{RGB}{242,222,166}"
error_color = "{RGB}{242,159,151}"
info_color = "{RGB}{231,242,250}"

latex_elements = {
    'preamble': r"""
\makeatletter
   \fancypagestyle{normal}{
% this is the stuff in sphinx.sty
    \fancyhf{}
    \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
% we comment this out and
    %\fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
    %\fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
% add copyright stuff
    \fancyfoot[LO,RE]{{\textcopyright\ 2023, us4us Ltd.}}
% again original stuff
    \fancyhead[LE,RO]{{\py@HeaderFamily \@title\sphinxheadercomma\py@release}}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
    }
% this is applied to each opening page of a chapter
   \fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0.4pt}
% add copyright stuff for example at left of footer on odd pages,
% which is the case for chapter opening page by default
    \fancyfoot[LO,RE]{{\textcopyright\ 2023, us4us Ltd.}}
    }
\makeatother
""",
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',
    'sphinxsetup': f'attentionBgColor={warning_color}, '
                   f'warningBgColor={warning_color}, '
                   f'cautionBgColor={warning_color}, '
                   f'importantBgColor={warning_color}, '
                   f'dangerBgColor={error_color}, '
                   f'errorBgColor={error_color}, '
                   f'noteBgColor={info_color}, '
                   f'hintBgColor={info_color}, '
                   f'tipBgColor={info_color} '

}
