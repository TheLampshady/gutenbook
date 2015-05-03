from roman import fromRoman, toRoman
import re
from tex import Tex


class Chapter(object):

    def __init__(self, chapter_number, text):
        self.id = fromRoman(chapter_number)
        self.name = ''
        self.content = ''

        self.build_chapter(text)

    def build_chapter(self, text):
        regex = r'(?:[^\n]+)\n\n([^\n]+)\n\n(.+)'
        result = re.findall(regex, text, flags=re.M|re.S)
        self.name = result[0][0]
        self.content = result[0][1]

    def texify(self):
        tex_content = u''
        #tex_content += Tex.part % 'CHAPTER '+toRoman(self.id)
        tex_content += Tex.chapter % self.name
        tex_content += '%s\n' % unicode('test', errors='replace')

        return tex_content
