#!/usr/bin/python

__author__ = "Hao Luo"

import argparse
from plagiarism_detector import PlagiarismDetector

def create_arg_parser():
	parser = argparse.ArgumentParser(description="A simple plagiarism detector")
	parser.add_argument('-syn', '--synonyms', \
						action='store', \
						dest='synonyms_file', \
						help='file name for a list of synonyms', \
						required=True)
	parser.add_argument('-s', '--source', \
						action='store', \
						dest='source_file', \
						help='file name for the source file', \
						required=True)
	parser.add_argument('-r', '--reference', \
						action='store', \
						dest='reference_file', \
						help='file name for the reference file', \
						required=True)
	parser.add_argument('-n', '--n_gram', \
						action='store', \
						dest='n', \
						help='size of tuple', \
						type=int, \
						default=3, \
						required=False)
	return parser

def main():
	parser = create_arg_parser()
	args = parser.parse_args()
	detector = PlagiarismDetector(args.synonyms_file, args.source_file, args.reference_file, args.n)
	detector.run()

if __name__ == '__main__':
	main()
