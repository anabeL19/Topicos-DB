import json
import numpy as np
import func as f
from timeit import default_timer as timer
from time import time

# searches for the word entered
def find_word(word):
    flag = False
    word_bool = 0
    with open('Data/information.json', 'r') as info:
        for obj in info:
            data = json.loads(str(obj))
            for key in data.keys():
                if word == key:
                    word_bool = f.createVector(data[word])
                    flag = True
    return word_bool, flag

# semantic similarity
def similarity(word):
    ranking = []

    word_bool, flag = find_word(word)
    if flag == False:
        return False

    with open('Data/information.json', 'r') as info:
        for obj in info:
            data = json.loads(str(obj))
            # create boolean array with lemmas to compare
            for key, value in data.items():
                if word != key:
                    data_bool = f.createVector(value)
                    # Jaccard method
                    intersection = word_bool & data_bool
                    union = word_bool | data_bool
                    tup = (intersection.sum() / union.sum() * 100, key)
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
        for i in range(0,10):
            print(ranking[i])

        print(end - start)
    else: 
        print("Search other word")

getData()
word = "competition"
# word = "watt"
show(word)