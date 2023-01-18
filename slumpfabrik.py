from random import randint
from fractions import Fraction as frac

run = True
reslist = []
for x in range(1,11):
    for y in range(1,11):
        reslist.append(x*y)
shortlist = list(dict.fromkeys(reslist))

diviList = []
for x in range(1,11):
    for y in range(1,11):
        z = frac(float(x/y)).limit_denominator(10)
        diviList.append(z)
diviList = list(dict.fromkeys(diviList))


def getRandDiv():
    r = diviList[randint(0,41)]
    return r

def getRand():
    r = shortlist[randint(0,41)]
    return r