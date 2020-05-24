import json
import numpy as np
import func as f
from timeit import default_timer as timer
from time import time

def concurrency(word):
    with open('Data/information.json', 'r') as info:
        data = json.load(info)

    word_bool = f.createVector(data[word])
    ranking = []
    for key, value in data.items():
        if key!=word:
            data_bool = f.createVector(value)
            intersection = word_bool & data_bool
            union = word_bool | data_bool
            tup = (intersection.sum() / union.sum() * 100, key)
            ranking.append(tup)
            # ranking.append(intersection.sum() / union.sum() * 100)
            ranking.sort(reverse=True)
    # print('sum ',ranking)
    return ranking

def getData():
    filename = f.getFiles()
    lemmas = {}
    aux = []
    
    for i in range(len(filename)):
        print(' Archivo :  ', filename[i])
        fileRead= open('Data/Factorization/'+filename[i],'r')
        lines= fileRead.readlines()
        divide = {}
        print(divide)
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
                    # para no alterar el conteo de id
                    id_ = id_ - 1
                            
    # with open('Data/Information/'+filename[i]+'.json', 'w') as info:
    with open('Data/information.json', 'w') as info:
        json.dump(lemmas, info)
        
    fileRead.close()      
            
def show(word):
    # start = timer()
    start = time()
    ranking = concurrency(word)
    end = time()
    # end = timer()
    # print(ranking[:10])
    for i in range(0,10):
        print(ranking[i])

    print(end - start)

getData()
word = "competition"
# word = "watt"
show(word)