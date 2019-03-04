import cPickle as pickle
import nltk
import numpy as np

pathGloveEmbed = "/home/mak/Desktop/Projects/FRIENDS/GloveEmbeddings.p"
pathGloveVocab = "/home/mak/Desktop/Projects/FRIENDS/GloveVocab.p"
pathFriendsVocabDict = "/home/mak/Desktop/Projects/FRIENDS/subtitles/vocabDict.p"
pathCorpus = "/home/mak/Desktop/Projects/FRIENDS/subtitles/AllSeasons.txt"
gloveEmbed = pickle.load(open(pathGloveEmbed,"rb"))
gloveVocab = pickle.load(open(pathGloveVocab,"rb"))
vocabDict = pickle.load(open(pathFriendsVocabDict,"rb"))
friendWords = vocabDict.keys()
newWords = [w for w in friendWords if w not in gloveVocab]
# freq = [vocabDict[w] for w in newWords]
# freq = np.array(freq)
# freq = freq.astype(np.int)
newVocab = gloveVocab+newWords
l = len(newWords)
embedFriends = np.random.randn(l,100)
newEmbed = np.vstack((gloveEmbed,embedFriends))
corpus = open(pathCorpus,"r")
print np.shape(newEmbed)
print len(newVocab)

def sentenceGenerator():
	for x in corpus:
		yield x

def getIndex(word):
	i = newVocab.index(word)


sentenceGen = sentenceGenerator()
print next(sentenceGen)
print next(sentenceGen)

