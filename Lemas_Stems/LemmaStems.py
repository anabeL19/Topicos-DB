import nltk
import spacy
#Stemming
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
#Lemmatization
from es_lemmatizer import lemmatize

spanishStemmer=SnowballStemmer("spanish")
sp = spacy.load("es_core_news_sm")
sp.add_pipe(lemmatize, after="tagger")

def Stemming(sentence):
    token_words=word_tokenize(sentence)
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(spanishStemmer.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

def Lemmatization(sentence):
    token_words = sp(sentence)
    lemma_sentence=[]
    for word in token_words:
        lemma_sentence.append(word.lemma_)
        lemma_sentence.append(" ")
    return "".join(lemma_sentence)






