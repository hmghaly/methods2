#!/usr/bin/python
#import practicum4 
#from practicum4 import p1a
from nltk.corpus import gutenberg
from string import punctuation
import time

def tokenize(raw_text): #problem 1a - lower case - split - strip punctuation
	text_lower=raw_text.lower()
	split_str=text_lower.split()
	out_tokens=[v.strip(punctuation) for v in split_str]
	return out_tokens

def vocab(raw_text): #get unique vocabulary items (word types)
	out_tokens=tokenize(raw_text)
	unique_tokens=set(out_tokens)
	print "original number of tokens", len(out_tokens)
	print "number of unique tokens", len(unique_tokens)
	return unique_tokens



def vocab_count(raw_text): #count each vocabulary item -> iterate over unique items and count them from the original list
	counted_vocab=[]
	out_tokens=tokenize(raw_text)
	unique_tokens=set(out_tokens)
	print "original number of tokens", len(out_tokens)
	print "number of unique tokens", len(unique_tokens)
	for token in unique_tokens:
		cur_count=out_tokens.count(token)
		counted_vocab.append((token,cur_count))

	return counted_vocab

def vocab_count_dict(raw_text): #doing the same using dictionaries - much faster
	counted_vocab_dict={}
	out_tokens=tokenize(raw_text)
	for token in out_tokens:
		counted_vocab_dict[token]=counted_vocab_dict.get(token,0)+1
	return counted_vocab_dict

def get_bigrams(raw_text): #a function to list all the bigrams in a list of tokens
	out_tokens=tokenize(raw_text)
	bigrams=[(out_tokens[i],out_tokens[i+1]) for i in range(len(out_tokens)-1)]
	return bigrams

def get_trigrams(raw_text): #and the trigrams
	out_tokens=tokenize(raw_text)
	trigrams=[(out_tokens[i],out_tokens[i+1],out_tokens[i+2]) for i in range(len(out_tokens)-2)]
	return trigrams


def get_bigram_count_dict(raw_text): #then we iterate over each bigram and increment its count in a dictionary
	counted_bigram_dict={}
	cur_bigrams=get_bigrams(raw_text)
	for big in cur_bigrams:
		counted_bigram_dict[big]=counted_bigram_dict.get(big,0)+1
	return counted_bigram_dict



def p1a(): #the main container function
	#lowercase, and tokenize. To tokenize, write a simple function that will separate common punctuation symbols.
	#print "working with Emma text"
	emma_text = gutenberg.raw('austen-emma.txt')
	clean_tokens=tokenize(emma_text)
	#print clean_tokens[:100]
	#print '-----'

	bryant_text = gutenberg.raw('bryant-stories.txt')
	clean_tokens=tokenize(bryant_text)
	#print clean_tokens[:100]

	#print "now getting unique vocabulary"
	bryant_text = gutenberg.raw('bryant-stories.txt')
	clean_tokens=tokenize(bryant_text)
	unique_words=list(set(clean_tokens))
	#print "original number of tokens in the text", len(clean_tokens)
	#print clean_tokens[:100]
	#print "number of unique tokens in the text", len(unique_words)	
	#print unique_words[:100]

	bryant_text = gutenberg.raw('bryant-stories.txt')
	#t0=time.time()
	#bryant_vocab=vocab_count(bryant_text)
	#t1=time.time()
	#print bryant_vocab[:100]
	#print "finished with the list method, time", t1-t0 
	t0=time.time()
	bryant_vocab_dict=vocab_count_dict(bryant_text)
	t1=time.time()
	for key in bryant_vocab_dict.keys()[:100]:
		print key, bryant_vocab_dict[key]
	print "finished with the dictionary method, time", t1-t0

	#our_bigrams=get_bigrams(bryant_text)
	#for big in our_bigrams[:20]:
	#	print big

	bigram_count_dict=get_bigram_count_dict(bryant_text)
	for key in bigram_count_dict.keys()[:100]:
		print key, bigram_count_dict[key]

	our_trigrams=get_trigrams(bryant_text)
	for tri in our_trigrams[:100]:
		print tri


	#emma_text_lower=emma_text.lower()
	#split_str=emma_text_lower.split()

	#print len(emma_text)
	#print emma_text_lower[:100]
	#print len(split_str)
	#print split_str[:20]
	#for ss in split_str[:100]:
	#	print ss, ss.strip(punctuation)
	



if __name__=="__main__":
	print "Hello"
	#p1b()
	p1a()
	#p1b()
