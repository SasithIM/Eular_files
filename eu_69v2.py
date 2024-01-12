# FFuuu....
#it's always a product of consecetive primes starting from the beginning
# (sigh)

import primes

prime_list =  primes.primes(20)

n=1
for i in prime_list:
    n*=i
    if n>10**6:
        print(n/i)
        break
else:
    print('prime list not long enough')