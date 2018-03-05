from word_simi import WordSimi

class SentenceSimi:
	wordsLeft 			= []
	wordsRight 			= []
	countLeft			= 0
	countRight			= 0
	tokenizer_spliter 	= ' '

	def __init__(self, sentA, sentB):
		self.wordsLeft 	= self.preprocessSentence(sentA)
		self.wordsRight = self.preprocessSentence(sentB)
		self.countLeft	= len(self.wordsLeft)
		self.countRight	= len(self.wordsRight)

	def preprocessSentence(self, sent):
		return sent.split(self.tokenizer_spliter)

	def getMinCount(self):
		return float(self.countLeft) if self.countLeft < self.countRight else float(self.countRight)

	def doOneGridPair(self, word, words):
		result_simi = 0;
		for w in words:
			score = WordSimi(word, w).getSimi()
			if result_simi < score:
				result_simi = score

		return result_simi

	def getAllGridPairScore(self):
		total_score = 0
		for w in self.wordsLeft:
			score = self.doOneGridPair(w, self.wordsRight)
			total_score += score

		return float(total_score)

	def getSimilarityScore(self):
		return self.getAllGridPairScore() / self.getMinCount();