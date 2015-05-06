import logging
import re

from util import clean_list
from models import Tex
from models import Chapter
from models import Contents
import codecs

class GutenbergEBook(object):
    def __init__(self, book_id, directory='books/'):
        self.ebook = None
        self.gutenberg_text = None
        self.contents = None
        self.chapters = []
        self.author_list = []

        file_name = '%spg%s.txt' % (directory, book_id)
        try:
            gutenberg_file = codecs.open(file_name, 'r', "utf-8")
            self.gutenberg_text = gutenberg_file.read()
        except IOError:
            logging.exception("File Error: Cannot open '%s'" % file_name)
            raise

    def build_book(self):
        regex_ebook1 = r'(\r?\n){7,}'
        regex_ebook2 = r'(\r?\n){6,}'

        result = clean_list(re.split(regex_ebook1, self.gutenberg_text, flags=re.M))
        self.build_meta(result[0])

        result_clean = clean_list(re.split(regex_ebook2, result[1], flags=re.M))
        self.ebook = result_clean[0]

        self.build_sections()

    def build_meta(self, content):
        author_regex = 'Author:\s((.*)(?!\n\r?\n\r?)'


        #self.author_list = clean_list(re.findall(author_regex, content, flags=re.M|re.S))

    def build_sections(self):
        regex = r'(\r?\n){5,}'
        result = clean_list(re.split(regex, self.ebook, flags=re.M))
        for text in result:
            title = text.split('\n')[0]
            if 'CHAPTER' in title:
                self.chapters.append(Chapter(title.split()[1], text))
            elif 'CONTENTS' in title:
                self.contents = Contents(text)

    def texify(self):
        tex_content = u''
        tex_content += Tex.doc
        tex_content += '\\usepackage[T1]{fontenc}\n'
        tex_content += '\\usepackage{textcomp}\n'
        tex_content += '\\usepackage{lmodern}\n'
        tex_content += Tex.indent
        tex_content += Tex.right
        tex_content += Tex.title % 'i'
        tex_content += Tex.author % 'i'
        tex_content += Tex.date % 'i'
        tex_content += Tex.begin
        tex_content += Tex.table
        for chapter in self.chapters:
            tex_content += chapter.texify()

        tex_content += Tex.end

        return tex_content
