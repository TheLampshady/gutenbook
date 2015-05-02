import logging

class GutenbergEBook(object):
	
	def __init(self, file_name):
		try:
			gutenberg_file = open(file_name, 'r')
			self.gutenberg_text = gutenberg_file.read()
		except IOError:
			logging.exception("File Error: Cannot open '%s'" % file_name)
		gutenberg_file.read()
		


	def build_book(self):
		regex_ebook1 = r'(\n\r?){7,}'
		regex_ebook2 = r'(\n\r?){6,}'
		result = clean_list(re.split(regex_ebook1, self.gutenberg_text, flags=re.M))
		result_clean = clean_list(re.split(regex_ebook2, result[1], flags=re.M))
		self.ebook = result_clean[0]