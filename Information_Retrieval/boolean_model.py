import json
import numpy as np
import func as f
from timeit import default_timer as timer
from time import time

# searches for the word entered
def find_word(word):
    flag = False
    w_ids = 0
    word = f.lemmatization(word)
    with open('Data/information.json', 'r') as info:
        for obj in info:
            data = json.loads(str(obj))
            for key, value in data.items():
                if word == key:
                    # values that contain that search word
                    w_ids = value.values()
                    flag = True
    return w_ids, flag

# semantic similarity
def similarity(word):
    ranking = []

    word_ids, flag = find_word(word)
    if flag == False:
        return False

    with open('Data/information.json', 'r') as info:
        for obj in info:
            data = json.loads(str(obj))
            # create boolean array with lemmas to compare
            for key, value in data.items():
                if word != key:
                    all_ids = value.values()
                    # Jaccard method
                    intersection = len(set(word_ids).intersection(set(all_ids)))
                    union = len(set(word_ids)) + len(set(all_ids)) - intersection
                    tup = (intersection / union * 100, key)
                    ranking.append(tup)
        ranking.sort(reverse=True)   
    return ranking

# save the lemmas with its respective keyword similar to "bigram"
def getData():
    filename = f.getFiles()
    lemmas = {}
    aux = []
    
    for i in range(len(filename)):
        print(' Archivo :  ', filename[i])
        fileRead= open('Data/Factorization/'+filename[i],'r')
        lines= fileRead.readlines()
        
        for l in lines:
            token = f.tokenize(l)

            try:
                id_ = id_ + 1
            except Exception:
                id_ = 0

            if token[0] not in lemmas:
                lemmas[token[0]] = {}       
            if token[1] not in lemmas[token[0]]:
                if token[1] not in aux:
                    aux.insert(id_, token[1])
                    lemmas[token[0]][token[1]] = id_
                else:
                    lemmas[token[0]][token[1]] = aux.index(token[1])
                    # not alter id of the lemmas
                    id_ = id_ - 1

    for key, value in lemmas.items():
        dic_item = {}
        dic_item[key] = value
        with open('Data/information.json', 'a') as info:
           json.dump(dic_item, info)
           info.write("\r\n")
        
    fileRead.close()      
            
def show(word):
    if similarity(word) != False:
        # start = timer()
        start = time()
        ranking = similarity(word)
        end = time()
        # end = timer()
        # print(ranking[:10])
        rank = []
        for i in range(0,100):
            rank.append(ranking[i])
            # print(ranking[i])
        t = end - start
        print(t)
        return rank
    else: 
        return("Search other word")

# getData()
word = "competition"
# word = "watt"
# show(word)