import re

file1 = 'pg20848.txt'
file2 = 'pg27477.txt'
file3 = 'pg25267.txt'
file4 = 'pg35934.txt'

def get_ebook(gutenberg_file):
	regex_ebook1 = r'(\n\r?){7,}'
	regex_ebook2 = r'(\n\r?){6,}'
	a = clean_list(re.split(regex_ebook1, gutenberg_file, flags=re.M))
	ebook = clean_list(re.split(regex_ebook2, a[1], flags=re.M))
	return ebook[0]


def clean_list(split_list):
	empty_list = [False, '', '\n']
	return [x.strip(' \t\n\r') for x in split_list if x not in empty_list]

def preview(content):
	regex = r'(\n\r?){5,}'
	t = clean_list(re.split(regex, content, flags=re.M))
	for i in t:
	  print i.split('\n')[0]

def test(file_name):
	gutenberg_file = open(file_name, 'r').read()
	result = get_ebook(gutenberg_file)
	preview(result)