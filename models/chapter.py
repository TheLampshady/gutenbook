from roman import fromRoman, toRoman
import re
from tex import Tex
from util import clean_list

class Chapter(object):

    def __init__(self, chapter_number, text):
        self.id = fromRoman(chapter_number)
        self.name = ''
        self.content = ''

        self.build_chapter(text)

    def build_chapter(self, text):
		regex_content = r'(\r?\n){3,}'
		regex_title = r'(\r?\n){2,}'

		result = clean_list(re.split(regex_content, text, flags=re.M|re.S))
		self.content = result[1]
		result = clean_list(re.split(regex_title, result[0], flags=re.M|re.S))
		self.name = result[1]

    def texify(self):
        tex_content = u''
        #tex_content += Tex.part % 'CHAPTER '+toRoman(self.id)
        tex_content += Tex.chapter % self.name
        tex_content += '%s\n' % Tex.tex_it(self.content)
        #tex_content += '%s\n' % unicode('text', errors='replace')
		
        return tex_content
