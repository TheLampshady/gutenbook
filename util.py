import re
import sys
import codecs
from tex import latex2pdf


def clean_list(split_list):
    empty_list = [False, '', '\n']
    return [x.strip(' \t\n\r') for x in split_list if x not in empty_list]


def preview(content):
    regex = r'(\n\r?){5,}'
    t = clean_list(re.split(regex, content, flags=re.M))
    for i in t:
        print i.split('\n')[0]


def build_pdf(tex_file, output_file):
    if not output_file:
        output_file = 'ebook.pdf'
		
	if sys.platform != 'win32':
		outfile = codecs.open(output_file, 'w', 'utf-8')
		pdf = latex2pdf(tex_file)
		outfile.write(pdf)
		outfile.close()
	else:
		build_tex(tex_file)
		from subprocess import check_output
		check_output("pdflatex %s" % tex_file, shell=True)

def build_tex(tex_file, output_file='ebook.tex'):

    outfile = codecs.open(output_file, 'w', 'utf-8')
    outfile.write(tex_file)
    outfile.close()