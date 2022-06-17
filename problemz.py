from random import randint
from fractions import Fraction as frac

run = True
# TODO Refaktorisera denna till en eller flera klass ist börja med sub/add kanske
# TODO bygg om till återanvändbara klasser med parametrar MIN/MAX

multiList = []
divList = []

for x in range(1,11):
    for y in range(1,11):
        multiList.append(x*y)

def ListOfMulti(fr,to):
    # global inList
    multiList = []
    # genererar en lista över alla multiplikationer möjliga med talen x och y
    for x in range(fr,to+1):
        for y in range(fr,to+1):
            multiList.append(x*y)
    noDupList = list(dict.fromkeys(multiList))
    #inList = noDupList
    return noDupList
multiList = ListOfMulti()

# TODO generera en lista över alla fraktioner möjliga med talen x och y
def ListofDivi(fr,to):
    divlist = []
    for x in range(fr,to+1):
        for y in range(fr,to+1):
            z = frac(float(x/y)).limit_denominator(10)
            divlist.append(z)
    divlist = list(dict.fromkeys(divlist))    # kastar den genom dict och tillbaka för att få bort alla dubletter
    return divlist
divList = ListofDivi()

# Funktioner som returnerar tal från listorna med "lösningar"
def getRandomMulti():
    r = multiList[randint(0,41)]
    return r

def getRandomDiv():
    r = divList[randint(0,41)]
    return r

# TODO Bygg om så att listan kan skickas in utifrån och med dynamisk längd
def getRandFromMulti(l):
    r = multiList[randint(0,41)]
    return r


# while run:
#     r = randint(0,41)
#     print(shortlist[r],end="")
#     i = input()
#     if i == "exit":
#         run=False
