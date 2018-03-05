from nltk.corpus import wordnet as wn
import nltk

ID_FIX = "ind";

class WordSimi:
	wordA = {}
	wordB = {}
	fails = False

	def __init__(self, wordA, wordB):
		self.wordA = wn.synsets(wordA, lang=ID_FIX);
		self.wordB = wn.synsets(wordB, lang=ID_FIX);
		if len(self.wordA) == 0 or len(self.wordB) == 0:
			self.fails = True

	def getSimi(self):
		if self.fails:
			return 0

		score = self.wordA[0].path_similarity(self.wordB[0]);
		return 0 if score == None else score