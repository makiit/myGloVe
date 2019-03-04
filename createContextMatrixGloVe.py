import nltk
import numpy as np
import cPickle as pickle

path = "/home/mak/Desktop/Projects/FRIENDS/subtitles/AllSeasons.txt"
vocabPath = "/home/mak/Desktop/Projects/FRIENDS/subtitles/vocabDict.p"
vocabDict = pickle.load(open(vocabPath,"rb"))
vocab = vocabDict.keys()

def create():
	f = open(path,"r")
	corpus = f.read()
	words = corpus.split()
	l =  len(vocab)
	contextM = np.zeros((l,l))
	c = 100 #contextSize
	m = len(words)
	for i in range (0,m):
		print i
		w = words[i]
		fl = w in vocab
		if fl==False :
			continue

		ind = vocab.index(w)
		start = ind - c
		end = ind+c
		if start<0:
			start=0
		if end>=m:
			end = m-1

		prevContext = words[start:ind]
		nextContext = words[ind+1:end+1]
		lpc = len(prevContext)
		npc = len(nextContext)
		for j in range(0,lpc):
			cw = prevContext[j]
			if (cw in vocab)==False:
				continue

			weight = 1/(c-j)
			cind = vocab.index(cw)
			contextM[ind][cind] +=weight

		for j in range(0,npc):
			cw = nextContext[j]
			if (cw in vocab)==False:
				continue

			weight = 1/(c-j)
			cind = vocab.index(cw)
			contextM[ind][cind] +=weight

	print "Done..Saving"
	pickle.dump(contextM,open("contextMatrixGlove.p","wb"))
	print "Saved"


def load():
	path = "/home/mak/Desktop/Projects/FRIENDS/contextMatrixGlove.p"
	f = open(path,"rb")
	matrix = pickle.load(f)
	print np.shape(matrix)


load()








