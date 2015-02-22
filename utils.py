import os
import re
import sys
import string

TOKENIZE_PATTERN = re.compile(r'\W+')
PUNCTUATION = set(string.punctuation)

def check_empty_file(file_name):
	if not os.path.getsize(file_name):
		sys.exit('File ' + file_name + ' is empty!')

def replace_all(text, dictionary):
	for word, word_root in dictionary.items():
		text = text.replace(word, word_root)
	return text

def tokenize(text):
	return TOKENIZE_PATTERN.split(text)
