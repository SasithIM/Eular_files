from decimal import Decimal , getcontext
getcontext().prec = 100
max = 1; d=0
for i in range(7,1000):
    m = Decimal(1)/Decimal(i)
    n = str(m)[2:]
    n = int(n); n = str(n)
    print(i,n)
    for j in range(1,len(n)-1):
        if max<=j:
            max=j
            d = i
        else:
            pass
        if n[:j] != n[j:j*2]:
            pass
        else:
            break
print(max,d)

# deosn't work!!