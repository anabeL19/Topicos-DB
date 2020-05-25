import numpy as np

def getFiles():
    files = ["2gm-0000", "2gm-0001", "2gm-0002", "2gm-0003", "2gm-0004", "2gm-0005",
             "2gm-0006", "2gm-0007", "2gm-0008", "2gm-0009", "2gm-0010", "2gm-0011",
             "2gm-0012", "2gm-0013", "2gm-0014", "2gm-0015", "2gm-0016", "2gm-0017",
             "2gm-0018", "2gm-0019", "2gm-0020", "2gm-0021", "2gm-0022", "2gm-0023",
             "2gm-0024", "2gm-0025", "2gm-0026", "2gm-0027", "2gm-0028", "2gm-0029",
             "2gm-0030", "2gm-0031"]
    # files = ["2gm-0007", "2gm-0008", "2gm-0009"]
    # files = ["test", "test1"]
    return files

def tokenize(str_line):
    list_token = str_line.split()
    return list_token

def createVector(d):
    vbool = np.zeros(56221482, dtype = bool) #56221481
    # vbool = np.zeros(7018900, dtype = bool)
    # vbool = np.zeros(400, dtype = bool)
    for v in d.values():
        vbool[v] = 1
    return vbool