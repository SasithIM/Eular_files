import primes as prm

def isPandigi(num):
    s1=sorted(str(num))
    s0=[str(i) for i in range(1,len(s1)+1)]
    if s1 == s0:
        return True
    else:
        return False
    
prmls = prm.primes(999999999)       #;print(len(prmls))
max1=0
for i in prmls:
    if isPandigi(i):
        max1=i

print(max1)

# more efficient the otherway around 
# i.e. look for prims in pandigital numbers