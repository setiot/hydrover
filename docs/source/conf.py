# -*- coding: utf-8 -*-

project = u'hydrover'
copyright = u'2020, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'1.0'
release = u'https://github.com/setiot/hydrover/releases/'
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'hydroverdoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'hydrover.tex', u'hydrover Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(master_doc, 'hydrover', u'hydrover Documentation', [author], 1)]
texinfo_documents = [(
    master_doc, 'hydrover', u'hydrover Documentation', author, 'hydrover',
    'One line description of project.', 'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
