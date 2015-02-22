from __future__ import division
from utils import *

class PlagiarismDetector(object):
	'''
	This class performs plagiarism detection using a N-tuple
	comparison algorithm allowing for synonyms in the text.

	Attributes:
	_synonyms_file: file name for a list of synonyms
	_source_file: file name for the source file to be detected
	_reference_file: file name for the reference file
	_n: size of tuple
	_synonyms_dict: a dictionary matching all synonyms to the first synonym

	'''

	def __init__(self, synonyms_file, source_file, reference_file, n):
		self._synonyms_file = synonyms_file
		self._source_file = source_file
		self._reference_file = reference_file
		self._n = n
		self._synonyms_dict = self._generate_synonym_dictionary()

	'''
		Generate normalized n-grams for source file and reference file.
		Calculate the percentage of n-grams in source file that appear
		in reference file.
	'''
	def run(self):
		source_file_n_grams = self._generate_n_grams_from_file(self._source_file)
		reference_file_n_grams = self._generate_n_grams_from_file(self._reference_file)
		print "{:.2f}%".format(
			len(source_file_n_grams.intersection(reference_file_n_grams)) \
			/ len(source_file_n_grams) * 100)

	'''
		Match all synonyms to the first synonym
		For example, given [run sprint jog] as a synonym list
		we match "run" -> "run"
				 "sprint" -> "run"
				 "jog" -> "run"		
	'''
	def _generate_synonym_dictionary(self):
		synonyms_dict = {}
		check_empty_file(self._synonyms_file)
		with open(self._synonyms_file) as syno:
			for line in syno:
				words = line.split()
				for word in words:
					synonyms_dict[word.lower()] = words[0].lower()
		return synonyms_dict

	def _generate_n_grams_from_file(self, file_name):
		norm_tokens = self._generate_normalized_tokens_from_file(file_name)
		return self._generate_n_grams_from_tokens(norm_tokens)

	'''
		Normalize all synonyms with the first word appears
		in each synonyms list
	'''
	def _generate_normalized_tokens_from_file(self, file_name):
		tokens = self._tokenize_text_file(file_name)
		norm_tokens = [t.lower() for t in tokenize( \
			replace_all(' '.join(tokens), self._synonyms_dict))]
		return norm_tokens

	def _tokenize_text_file(self, file_name):
		check_empty_file(file_name)
		with open(file_name) as input_file:
			return tokenize(input_file.read())

	def _generate_n_grams_from_tokens(self, tokens):
		n_grams = set()
		for i in range(len(tokens) - self._n + 1):
			n_gram = " ".join(tokens[i : i + self._n])
			n_grams.add(n_gram)
		return n_grams
