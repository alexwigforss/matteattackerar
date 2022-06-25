from random import randint
from fractions import Fraction as frac

class problemz:
    def __init__(my, name, age):
        my.sublist = []
        my.addlist = []
        my.multilist = []
        my.divilist = []
        my.ekvlist = []

    def myfunc(s):
        print("Hello my name is " + s.name)


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
    addlist, sublist = ListOfSubAdd()

    def ListOfMulti(fr,to):
        multiList = []
        for x in range(fr,to+1):
            for y in range(fr,to+1):
                multiList.append(x*y)
        multiList = list(dict.fromkeys(multiList))
        return multiList
    multilist = ListOfMulti()

    def ListofDivi(fr,to):
        diviList = []
        for x in range(fr,to+1):
            for y in range(fr,to+1):
                z = frac(float(x/y)).limit_denominator(10)
                diviList.append(z)
        diviList = list(dict.fromkeys(diviList))
        return diviList
    divilist = ListofDivi()

    # TODO generera en lista över alla fraktioner möjliga med talen x och y
    # TODO UNDER CONSTRUCTION TODO
    def ListofEkvation(fr,to):
        ekvList = []
        for x in range(fr,to+1):
            for y in range(fr,to+1):
                z = frac(float(x/y)).limit_denominator(10)
                ekvList.append(z)
        ekvList = list(dict.fromkeys(ekvList))
        return ekvList
    ekvlist = ListofDivi()
    # TODO UNDER CONSTRUCTION TODO

    # Funktioner som returnerar tal från listorna med "lösningar"
    def getRandomAdd(my):
        r = my.multilist[randint(0,41)]
        return r

    def getRandomSub(my):
        r = my.multilist[randint(0,41)]
        return r

    def getRandomMulti(my,str,end):
        r = my.multilist[randint(str,end)]
        return r

    def getRandomDiv(my):
        r = my.divilist[randint(0,41)]
        return r

    def getRandomDiv(my,str,end):
        r = my.divilist[randint(str,end)]
        return r

    def getRandomMulti(my):
        r = my.multilist[randint(0,41)]
        return r

    def getRandomMulti(my,str,end):
        r = my.multilist[randint(str,end)]
        return r

    def getRandomSubAdd(my):
        rsub = my.sublist[randint(0,41)]
        radd = my.addlist[randint(0,41)]
        return rsub, radd

    def getRandomSubAdd(my,str,end):
        rsub = my.subbs[randint(str,end)]
        radd = my.subbs[randint(str,end)]
        return rsub, radd

    def getRandomEkv(my):
        ekv = my.ekvlist[randint(0,41)]
        return ekv

    def getRandomEkv(my,str,end):
        ekv = my.ekvlist[randint(str,end)]
        return ekv


# while run:
#     r = randint(0,41)
#     print(shortlist[r],end="")
#     i = input()
#     if i == "exit":
#         run=False
