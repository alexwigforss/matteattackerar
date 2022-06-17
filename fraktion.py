from fractions import Fraction as frac

reslist = []
for x in range(1,11):
    for y in range(1,11):
        #reslist.append(float(x/y))
        z = frac(float(x/y)).limit_denominator(10)
        reslist.append(z)
        print(z,"\t",end=" ")
    print()
#print(reslist,len(reslist))
print(len(reslist))
print()
shortlist = list(dict.fromkeys(reslist))

print(shortlist)