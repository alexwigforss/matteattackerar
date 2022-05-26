from random import randint
from fractions import Fraction as frac

run = True
# TODO Refaktorisera denna till en eller flera klass ist börja med sub/add kanske

# genererar en över alla divisioner möjliga med talen 1 till 10

# reslist = []
# for x in range(1,11):
#     for y in range(1,11):
#         #reslist.append(float(x/y))
#         z = frac(float(x/y)).limit_denominator(10)
#         reslist.append(z)
#         print(z,"\t",end=" ")
#     print()
# #print(reslist,len(reslist))
# print(len(reslist))
# print()
# shortlist = list(dict.fromkeys(reslist))

# TODO bygg om till återanvändbara klasser med parametrar MIN/MAX

#   från main
# genererar en lista över alla multiplikationer möjliga med talen x och y

reslist = []
for x in range(1,11):
    for y in range(1,11):
        reslist.append(x*y)

# TODO generera en lista över alla divisioner möjliga med talen x och y

# kastar den genom dict för att få bort alla dubletter
shortlist = list(dict.fromkeys(reslist))
# print(shortlist,len(shortlist))
# print()

# input("Listan är skapad, tryck enter för att fortsätta")

# genererar för varje varv ett slumptal och visar värdet på den korta listan via slumptal/index
def getRand():
    r = shortlist[randint(0,41)]
    return r

# while run:
#     r = randint(0,41)
#     print(shortlist[r],end="")
#     i = input()
#     if i == "exit":
#         run=False
