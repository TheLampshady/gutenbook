import argparse
from ebook import GutenbergEBook

def parse_args():
	parser = argparse.ArgumentParser(description='Process ebooks.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+',
					   help='an integer for the accumulator')
	parser.add_argument('--sum', dest='accumulate', action='store_const',
					   const=sum, default=max,
					   help='sum the integers (default: find the max)')

	return parser.parse_args()
	print(args.accumulate(args.integers))

if __name__ == "__main__":
   args = parse_args()