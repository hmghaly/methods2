#!/usr/bin/python
import nltk
from nltk.corpus import brown



brown_tagged_sents = brown.tagged_sents(categories="news")
brown_tagged_sents=list(brown_tagged_sents)
brown_tagged_learned=list(brown.tagged_sents(categories="learned"))
brown_train = brown_tagged_sents[:4000]
brown_test= brown_tagged_sents[4000:]

t0 = nltk.DefaultTagger("??")
#affix_tagger=nltk.UnigramTagger(brown_train, backoff=t0)
#affix_tagger=nltk.AffixTagger(brown_train,min_stem_length=0, affix_length=-1, backoff=t0)
affix_tagger=nltk.AffixTagger(brown_train, backoff=t0)

our_sent=["I","want","us", "to","realize","how","dangerous","calmly", "coordination"]
print "tagging stuff - using affix tagger"
print affix_tagger.tag(our_sent)


bigram_tagger = nltk.BigramTagger(brown_train)
print "tagging with bigram tagger"
print bigram_tagger.tag(our_sent)

#print "Bigram tagger test performance on the same data`"
#print bigram_tagger.evaluate(brown_train)
#print "and on test data"
#print bigram_tagger.evaluate(brown_test)

 	
fd = nltk.FreqDist(brown.words(categories='news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
most_freq_words = fd.most_common(100)
likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
#for lt in likely_tags:
#	print lt, likely_tags[lt]
baseline_tagger = nltk.UnigramTagger(model=likely_tags)
evaluation=baseline_tagger.evaluate(brown_tagged_sents)
#print "result of baseline_tagger", evaluation
print "tagging with UnigramTagger/lookup"
print baseline_tagger.tag(our_sent)


bigram_affix_tagger = nltk.BigramTagger(brown_train, backoff=affix_tagger)
print "tagging with bigram tagger + affix tagger"
print bigram_affix_tagger.tag(our_sent)

print "evaluating affix tagger"
affix_eval= affix_tagger.evaluate(brown_test)
print affix_eval

print "evaluating unigram tagger"
unigram_eval= baseline_tagger.evaluate(brown_test)
print unigram_eval

print "evaluating unigram tagger"
bigram_eval= bigram_tagger.evaluate(brown_test)
print bigram_eval

print "evaluating combined bigram + affix tagger"
bigram_affix_eval= bigram_affix_tagger.evaluate(brown_test)
print bigram_affix_eval



fd = nltk.FreqDist(brown.words(categories='news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
most_freq_words = fd.most_common(1000)
for mw in most_freq_words:
	cur_word=mw[0]
	cur_word_count=mw[1]
	word_cfd=dict(cfd[cur_word])
	max_tag=cfd[cur_word].max()
	max_tag_count=word_cfd[max_tag]
	ratio=float(max_tag_count)/cur_word_count
	num_possible_tags=len(word_cfd.keys())
	#if num_possible_tags==1:
	#	print mw, word_cfd, max_tag, max_tag_count, ratio, num_possible_tags

min_word_count=5
brown_train = brown_tagged_sents[:4000]
new_brown_train=[]
for sent in brown_train:
	#print "original sent", sent
	new_sent_list=[]
	for word_tag in sent:
		word,tag=word_tag
		word_dict=dict(cfd[word])
		word_count=sum(word_dict.values())
		if word_count<min_word_count:
			new_sent_list.append(("UNK",tag))
		else:
			new_sent_list.append(word_tag)
	#print "sent with UNK", new_sent_list
	new_brown_train.append(new_sent_list)

min_word_count=5
brown_test= brown_tagged_sents[4000:]
new_brown_test=[]
for sent in brown_test:
	#print "original sent", sent
	new_sent_list=[]
	for word_tag in sent:
		word,tag=word_tag
		word_dict=dict(cfd[word])
		word_count=sum(word_dict.values())
		if word_count<min_word_count:
			new_sent_list.append(("UNK",tag))
		else:
			new_sent_list.append(word_tag)
	#print "sent with UNK", new_sent_list
	new_brown_test.append(new_sent_list)


new_bigram_tagger = nltk.BigramTagger(new_brown_train)

new_bigram_eval= new_bigram_tagger.evaluate(new_brown_test)
print "tagging with bigram tagger"
print bigram_eval, new_bigram_eval
#print bigram_tagger.tag(our_sent)
