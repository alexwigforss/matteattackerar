from random import randint
from fractions import Fraction as frac

run = True
# TODO Refaktorisera denna till en eller flera klass ist börja med sub/add kanske
# TODO bygg om till återanvändbara klasser med parametrar MIN/MAX


#def __init__(self):
inList = list()

reslist = []
for x in range(1,11):
    for y in range(1,11):
        reslist.append(x*y)

def ListOfMulti(fr,to):
    global inList
    reslist = []
    # genererar en lista över alla multiplikationer möjliga med talen x och y
    for x in range(fr,to+1):
        for y in range(fr,to+1):
            reslist.append(x*y)
    noDupList = list(dict.fromkeys(reslist))
    inList = noDupList
    return noDupList

# TODO generera en lista över alla divisioner möjliga med talen x och y

# kastar den genom dict och tillbaka för att få bort alla dubletter

# Funktion som returnerar tal från listan med lösningar
def getRandFromList():
    r = inList[randint(0,41)]
    return r

# TODO Bygg om så att listan kan skickas in utifrån och med dynamisk längd
def getRandFromList(l):
    r = inList[randint(0,41)]
    return r


# while run:
#     r = randint(0,41)
#     print(shortlist[r],end="")
#     i = input()
#     if i == "exit":
#         run=False
