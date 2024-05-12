from fractions import Fraction

fr_set=set()
for i in range(1,12000):
    for j in range(1,i):
        fr_set.add(Fraction(j,i))

fr_list = list(fr_set)

fr_list = sorted(fr_list)

index = fr_list.index(Fraction(1,3))
count = 0

while fr_list[index]<Fraction(1,2):
    count+=1

print(count)
