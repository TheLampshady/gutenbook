import sys
import codecs
import os.path
from tex import latex2pdf
import logging


def clean_list(split_list):
    empty_list = [False, u'', u'\n', u'\r\n']
    return [x.strip(' \t\n\r') for x in split_list if x not in empty_list]


def build_pdf(tex_content, output_file):
    id = str(output_file)
    pdf_file = 'output/'+ id + '.pdf'
    tex_file = 'output/'+ id + '.tex'

    logging.info("PDF Conversion: Outputting to '%s'." % pdf_file)
    build_tex(tex_content, tex_file)

    if sys.platform != 'win32':
        outfile = codecs.open(pdf_file, 'w', 'utf-8')
        pdf = latex2pdf(tex_content)
        outfile.write(pdf)
        outfile.close()
    else:
        logging.info("Windows Mode: Running 'pdflatex %s'." % tex_file)
        from subprocess import check_output

        check_output("pdflatex %s" % tex_file, shell=True)


def build_tex(tex_file, output_file):
    outfile = codecs.open(output_file, 'w', 'utf-8')
    outfile.write(tex_file)
    outfile.close()
