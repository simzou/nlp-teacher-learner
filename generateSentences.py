from collections import defaultdict
import random

PL0 = [('A',0),('B',1)]
P0 = [('S','A','B'),('S','A','R'),('R','S','B')]
#P1 = [('S','A','B'),('S','A','R'),('R','S','B'),('S','C','D')]

#print accepts((PL0,P0),w0)

"""
Returns a default dictionary given a grammar
For example, ('S','A','R') in input turns into a key value pair with 
'S' as key and a tuple of ('A','R') as value
"""
def processGrammar(PL,P):
	# lexical productions
	res = defaultdict(list)
	for tup in PL:
		res[tup[0]].append([tup[1]])
	for tup in P:
		res[tup[0]].append(tup[1:])
	return res

"""
Takes a grammar (as a dictionary) and a key and returns 
a list with just the key if the key is not in the grammar (so it is terminal)
or a random choice of all the possibilities for that key (which is a tuple)
"""
def selectRandomPath(grammar, key):
	if key in grammar and len(grammar[key]) > 0:
		return random.choice(grammar[key])
	else:
		return [key]

"""
Checks to see if a given sentence (which is a list of elements) contains all terminal elements
and return true if yes, false otherwise
grammar is a dictionary as defined above
"""
def isFinishedSentence(sentence,grammar):
	for elem in sentence:
		if elem in grammar:
			return False
	return True

"""Generates a random string given a grammar"""
def generateSentence(PL,P):
	grammar = processGrammar(PL,P)
	start = list(selectRandomPath(grammar,'S'))
	while True:
		sentence = []
		for elem in start:
			sentence = sentence + list(selectRandomPath(grammar, elem))
		if isFinishedSentence(sentence, grammar):
			break
		else:
			start = sentence
	sentence = [str(elem) for elem in sentence]
	return ''.join(sentence)

# testing
for i in range(20):
	print generateSentence(PL0,P0)