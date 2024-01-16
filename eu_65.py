import fractions
e=[2]
n=33
for i in range(n):
    e.append(1)
    e.append(2*(i+1))
    e.append(1)

e=e[::-1]
last=1/e[0]

for i in range(3*n):
    next=e[i+1]+fractions.Fraction(1/last)
    last=next

print(sum([int(i) for i in str(next.numerator)]))
# print(next.numerator) 