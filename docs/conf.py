# Only for bootstrap theme. comment it when using other themes
# import sphinx_bootstrap_theme

# -*- coding: utf-8 -*-
#
# theoretical-physics documentation build configuration file, created by
# sphinx-quickstart on Sun Sep  6 19:27:27 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('exts'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.pngmath', "math_dollar"]

pngmath_use_preview = True

latex_preamble = r"""
\usepackage{dsfont}
\usepackage{slashed}
\usepackage{yfonts}
\usepackage{mathrsfs}
\def\degrees{^\circ}
\def\d{{\rm d}}

\usepackage{color}
\setcounter{tocdepth}{2}

\def\sign{\mathop{\mathrm{sign}}}
\def\L{{\mathcal L}}
\def\H{{\mathcal H}}
\def\M{{\mathcal M}}
\def\matrix{}
\def\fslash#1{#1 \!\!\!/}
\def\F{{\bf F}}
\def\R{{\bf R}}
\def\J{{\bf J}}
\def\x{{\bf x}}
\def\y{{\bf y}}
\def\h{{\rm h}}
\def\a{{\rm a}}
\newcommand{\bfx}{\mbox{\boldmath $x$}}
\newcommand{\bfy}{\mbox{\boldmath $y$}}
\newcommand{\bfz}{\mbox{\boldmath $z$}}
\newcommand{\bfv}{\mbox{\boldmath $v$}}
\newcommand{\bfu}{\mbox{\boldmath $u$}}
\newcommand{\bfF}{\mbox{\boldmath $F$}}
\newcommand{\bfJ}{\mbox{\boldmath $J$}}
\newcommand{\bfU}{\mbox{\boldmath $U$}}
\newcommand{\bfY}{\mbox{\boldmath $Y$}}
\newcommand{\bfR}{\mbox{\boldmath $R$}}
\newcommand{\bfg}{\mbox{\boldmath $g$}}
\newcommand{\bfc}{\mbox{\boldmath $c$}}
\newcommand{\bfxi}{\mbox{\boldmath $\xi$}}

\newcommand{\bra}[1]{\left\langle #1\right|}
\newcommand{\ket}[1]{\left| #1\right\rangle}
\newcommand{\braket}[2]{\langle #1 \mid #2 \rangle}
\newcommand{\avg}[1]{\left< #1 \right>}

%\def\back{\!\!\!\!\!\!\!\!\!\!}
\def\back{}
\def\col#1#2{\left(\matrix{#1#2}\right)}
\def\row#1#2{\left(\matrix{#1#2}\right)}
\def\mat#1{\begin{pmatrix}#1\end{pmatrix}}
\def\matd#1#2{\left(\matrix{#1\back0\cr0\back#2}\right)}
\def\p#1#2{{\partial#1\over\partial#2}}
\def\cg#1#2#3#4#5#6{({#1},\,{#2},\,{#3},\,{#4}\,|\,{#5},\,{#6})}
\def\half{{\textstyle{1\over2}}}
\def\jsym#1#2#3#4#5#6{\left\{\matrix{
{#1}{#2}{#3}
{#4}{#5}{#6}
}\right\}}
\def\diag{\hbox{diag}}

\font\dsrom=dsrom10
\def\one{\hbox{\dsrom 1}}

\def\res{\mathop{\mathrm{Res}}}

\def\mathnot#1{\text{"$#1$"}}


%See Character Table for cmmib10:
%http://www.math.union.edu/~dpvc/jsmath/download/extra-fonts/cmmib10/cmmib10.html
\font\mib=cmmib10
\def\balpha{\hbox{\mib\char"0B}}
\def\bbeta{\hbox{\mib\char"0C}}
\def\bgamma{\hbox{\mib\char"0D}}
\def\bdelta{\hbox{\mib\char"0E}}
\def\bepsilon{\hbox{\mib\char"0F}}
\def\bzeta{\hbox{\mib\char"10}}
\def\boldeta{\hbox{\mib\char"11}}
\def\btheta{\hbox{\mib\char"12}}
\def\biota{\hbox{\mib\char"13}}
\def\bkappa{\hbox{\mib\char"14}}
\def\blambda{\hbox{\mib\char"15}}
\def\bmu{\hbox{\mib\char"16}}
\def\bnu{\hbox{\mib\char"17}}
\def\bxi{\hbox{\mib\char"18}}
\def\bpi{\hbox{\mib\char"19}}
\def\brho{\hbox{\mib\char"1A}}
\def\bsigma{\hbox{\mib\char"1B}}
\def\btau{\hbox{\mib\char"1C}}
\def\bupsilon{\hbox{\mib\char"1D}}
\def\bphi{\hbox{\mib\char"1E}}
\def\bchi{\hbox{\mib\char"1F}}
\def\bpsi{\hbox{\mib\char"20}}
\def\bomega{\hbox{\mib\char"21}}

\def\bvarepsilon{\hbox{\mib\char"22}}
\def\bvartheta{\hbox{\mib\char"23}}
\def\bvarpi{\hbox{\mib\char"24}}
\def\bvarrho{\hbox{\mib\char"25}}
\def\bvarphi{\hbox{\mib\char"27}}

%how to use:
%$$\alpha\balpha$$
%$$\beta\bbeta$$
%$$\gamma\bgamma$$
%$$\delta\bdelta$$
%$$\epsilon\bepsilon$$
%$$\zeta\bzeta$$
%$$\eta\boldeta$$
%$$\theta\btheta$$
%$$\iota\biota$$
%$$\kappa\bkappa$$
%$$\lambda\blambda$$
%$$\mu\bmu$$
%$$\nu\bnu$$
%$$\xi\bxi$$
%$$\pi\bpi$$
%$$\rho\brho$$
%$$\sigma\bsigma$$
%$$\tau\btau$$
%$$\upsilon\bupsilon$$
%$$\phi\bphi$$
%$$\chi\bchi$$
%$$\psi\bpsi$$
%$$\omega\bomega$$
%
%$$\varepsilon\bvarepsilon$$
%$$\vartheta\bvartheta$$
%$$\varpi\bvarpi$$
%$$\varrho\bvarrho$$
%$$\varphi\bvarphi$$

%small font
\font\mibsmall=cmmib7
\def\bsigmasmall{\hbox{\mibsmall\char"1B}}

\def\Tr{\hbox{Tr}\,}
\def\Arg{\hbox{Arg}}
\def\atan{\hbox{atan}}
"""

pngmath_latex_preamble = latex_preamble
latex_elements = {"preamble": latex_preamble}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Intelligence'
copyright = u'2016, Lei Ma'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.3'
# The full version, including alpha/beta/rc tags.
release = '0.0.3'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Intelligence'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "favicon.png"


# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.

html_theme_path = ["_themes",]
html_theme = 'sphinx_bootstrap_theme'
# html_theme = 'alabaster'

# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
html_logo = "_static/images/intelligence.png"

# Theme options are theme-specific and customize the look and feel of a
# theme further.
html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': html_title,

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Chapters",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    'navbar_links': [
        # ("Examples", "examples"),
        # ("Link", "http://example.com", True),
    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': True,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': True,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Sections",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 2,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    # 'navbar_class': "navbar navbar-inverse",
    'navbar_class': "navbar navbar-inverse",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "false",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "footer",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    'bootswatch_theme': "readable",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}



# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'Intelligence'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'intelligence.tex', u'Intelligence',
   u'OctoMiao', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
