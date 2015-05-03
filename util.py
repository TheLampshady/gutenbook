import re
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

    outfile = open(output_file, 'w')
    pdf = latex2pdf(tex_file)
    outfile.write(pdf)
    outfile.close()


def build_tex(tex_file, output_file='ebook.tex'):

    outfile = open(output_file, 'w')
    outfile.write(tex_file)
    outfile.close()