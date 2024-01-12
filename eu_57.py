from fractions import Fraction as fr

def n_sums(n):
    x = 2
    for i in range(n):
        x = fr(2+(1/x))
    return (x-1)

count=0
for i in range(1000):
    num = n_sums(i)
    if len(str(num.numerator))>len(str(num.denominator)):
        count+=1
print(count)