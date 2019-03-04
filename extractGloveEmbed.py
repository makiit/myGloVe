import os
import numpy as np
import nltk
import cPickle as pickle
from nltk.corpus import stopwords
from operator import itemgetter
from nltk.stem import WordNetLemmatizer

preTrainedEmbedPath = "/home/mak/Desktop/NLP/glove.6B/glove.6B.100d.txt"

f = open(preTrainedEmbedPath,"r")
i = 0
a = np.zeros((400000,100))
words = []

for x in f:
	# print x
	s = x.split()
	# print type(s)
	w = s[0]
	e = s[1:]
	e = np.array(e)
	try:
		e = e.astype(np.float)
	except ValueError:
		print x
	a[i]=e
	words.append(w)
	# if(i>10):
	# 	break
	i+=1
	print i
# print i
print a[0]
print words
pickle.dump(a, open("GloveEmbeddings.p", "wb"))
pickle.dump(words,open("GloveVocab.p","wb")) 
