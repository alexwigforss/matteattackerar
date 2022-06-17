from random import randint
from fractions import Fraction as frac

run = True
# TODO Ekvationer
# TODO bygg om till återanvändbara klasser med parametrar MIN/MAX

def ListOfSubAdd(fr,to):
    # global inList
    subList = []
    addList = []
    for x in range(fr,to+1):
        for y in range(fr,to+1):
            subList.append(x-y)
            addList.append(x+y)
    subList = list(dict.fromkeys(subList))
    return subList,addList
subbs, adds = ListOfSubAdd()

def ListOfMulti(fr,to):
    multiList = []
    for x in range(fr,to+1):
        for y in range(fr,to+1):
            multiList.append(x*y)
    noDupList = list(dict.fromkeys(multiList))
    return noDupList
multiList = ListOfMulti()

# TODO generera en lista över alla fraktioner möjliga med talen x och y
def ListofDivi(fr,to):
    divlist = []
    for x in range(fr,to+1):
        for y in range(fr,to+1):
            z = frac(float(x/y)).limit_denominator(10)
            divlist.append(z)
    divlist = list(dict.fromkeys(divlist))
    return divlist
divList = ListofDivi()

# TODO UNDER CONSTRUCTION TODO
def ListofEkvation(fr,to):
    ekvlist = []
    for x in range(fr,to+1):
        for y in range(fr,to+1):
            z = frac(float(x/y)).limit_denominator(10)
            ekvlist.append(z)
    ekvlist = list(dict.fromkeys(ekvlist))
    return ekvlist
ekvlist = ListofDivi()
# TODO UNDER CONSTRUCTION TODO

# Funktioner som returnerar tal från listorna med "lösningar"
def getRandomMulti():
    r = multiList[randint(0,41)]
    return r

def getRandomMulti(str,end):
    r = multiList[randint(str,end)]
    return r

def getRandomDiv():
    r = divList[randint(0,41)]
    return r

def getRandomDiv(str,end):
    r = divList[randint(str,end)]
    return r

def getRandomMulti():
    r = multiList[randint(0,41)]
    return r

def getRandomMulti(str,end):
    r = multiList[randint(str,end)]
    return r

def getRandomSubAdd():
    rsub = subbs[randint(0,41)]
    radd = subbs[randint(0,41)]
    return rsub, radd

def getRandomSubAdd(str,end):
    rsub = subbs[randint(str,end)]
    radd = subbs[randint(str,end)]
    return rsub, radd

def getRandomEkv():
    ekv = ekvlist[randint(0,41)]
    return ekv

def getRandomEkv(str,end):
    ekv = ekvlist[randint(str,end)]
    return ekv


# while run:
#     r = randint(0,41)
#     print(shortlist[r],end="")
#     i = input()
#     if i == "exit":
#         run=False
