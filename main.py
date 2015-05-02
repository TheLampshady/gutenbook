#!/usr/local/bin/python

import argparse
from ebook import GutenbergEBook

def parse_args():
	parser = argparse.ArgumentParser(description='Process ebooks.')
	parser.add_argument('-b', '--book', 
						type=int,  dest='book_id',
						required=True, 
					    help='Book Number for EBook')
	parser.add_argument('-r', '--remote', 
						dest='remote', action='store_true',
					    help='Retrieves the ebook from gutenberg.org')

	return parser.parse_args()

if __name__ == "__main__":
   args = parse_args()
   print args.book_id
   print args.remote