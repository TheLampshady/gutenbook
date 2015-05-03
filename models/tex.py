__author__ = 'zgoldstein'


class Tex(object):
    doc = u'\\documentclass[11pt]{book}\n'
    indent = u'\\parindent0pt  \parskip10pt\n'
    right = u'\\raggedright\n'
    title = u'\\title{%s}\n'
    author = u'\\author{%s}\n'
    date = u'\\date{%s}\n'
    begin = u'\\begin{document}\n'
    end = u'\\end{document}\n'

    table = u'\\tableofcontents'
    chapter = u'\\chapter{%s}\n'
    part = u'\\part{%s}\n'