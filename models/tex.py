__author__ = 'zgoldstein'
import unicodedata


class Tex(object):
    doc = u'\\documentclass[11pt]{book}\n'
    indent = u'\\parindent0pt  \parskip10pt\n'
    right = u'\\raggedright\n'
    import_title = u'\\usepackage{titling}'

    title = u'\\title{%s}\n'
    author = u'\\author{%s}\n'
    date = u'\\date{%s}\n'

    begin = u'\\begin{document}\n'
    end = u'\\end{document}\n'

    make_title = u'\\maketitle'

    table = u'\\tableofcontents\n'
    chapter = u'\\chapter{%s}\n'
    part = u'\\part{%s}\n'

    @classmethod
    def tex_it(cls, text):
        char_set = ['\\', '&', '%', '$', '#', '_', '{', '}', '^']
        result = text

        for c in char_set:
            result = result.replace(c, "\\" + c)

        result = result.replace('~', '\\textasciitilde{}')
        #result.replace('^', '\\textasciicircum')
        #result.replace('\\', '\\textbackslash')

        return result

