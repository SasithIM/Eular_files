from fractions import Fraction

fr_set=list()
for i in range(1,12000):
    for j in range(1,i):
        fr_set.append(Fraction(j,i))

print(len(fr_set))