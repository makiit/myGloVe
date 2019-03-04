import os
import numpy as np
import nltk
import cPickle as pickle
from nltk.corpus import stopwords
from operator import itemgetter
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


stop_words = set(stopwords.words('english'))
stop_words = [w.encode('utf-8') for w in stop_words]
stop_words.append("I")
vocabDict ={"ALI":1}

def wordDict(a):
	print a
	tokens = nltk.word_tokenize(a)
	words = [w for w in tokens if w.isalpha()]
	words = [w for w in words if not w in stop_words]
	words = [lemmatizer.lemmatize(w) for w in words]
	words = [w.encode('utf-8') for w in words]
	return words

def updateDict(words,word_dict):
	for w in words:
		if(w in word_dict):
			word_dict[w]+=1
		else:
			word_dict[w]=1

	return word_dict

def create():
	path = "/home/mak/Desktop/Projects/FRIENDS/subtitles/AllSeasons.txt"

	f = open(path,"r")
	i=0
	for x in f:
		x = x.decode('utf-8')
		x = x.lower()
		words = wordDict(x)
		updateDict(words,vocabDict)
		# print vocabDict
		i+=1

	pickle.dump(vocabDict, open("vocabDict.p", "wb")) 

def load():
	f= open("vocabDict.p","rb")
	vocab = pickle.load(f)
	print len(vocab.keys())
	items = vocab.items()
	for key,value in items:
		if(value <5):
			print key,"-",value
	# vocab = sorted(vocab.items(), key=itemgetter(1))	# print "Ross - ",vocab["Ross"]
	# print "Monica - ",vocab["Monica"]+vocab["Mon"]
	# print "Rachel - ",vocab["Rachel"]+vocab["Rach"]
	# print "Chandler - ",vocab["Chandler"]
	# print "Joey - ",vocab["Joey"]
	# print "Phoebe - ",vocab["Phoebe"]+vocab["Pheebs"]
	# print "Bing - ",vocab["Bing"]
	# print "Julie - ",vocab["Julie"]
	# print "Richard - ",vocab["Richard"]
	# print "Marcel - ",vocab["Marcel"]

# create()
load()