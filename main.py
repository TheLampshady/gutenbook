#!/usr/local/bin/python

import argparse
from ebook import GutenbergEBook
from util import build_pdf, build_tex


def parse_args():
    parser = argparse.ArgumentParser(description='Process ebooks.')
    parser.add_argument('-b', '--book',
                        dest='book_id', type=int,
                        required=True,
                        help='Book Number for EBook')
    parser.add_argument('-r', '--remote',
                        dest='remote', action='store_true',
                        help='Retrieves the ebook from gutenberg.org')
    parser.add_argument('-o', '--output',
                        dest='output', type=str,
                        help='Output file for pdf')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    try:
        gutenbook = GutenbergEBook(args.book_id)
    except Exception as e:
        gutenbook = None
        exit(1)

    gutenbook.build_book()

    tex_file = gutenbook.texify()
    build_pdf(tex_file, args.book_id)