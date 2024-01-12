import primes

n=1000
prime_list = primes.primes(10*n)[len(primes.primes(n)):]

# l1 = 2
# prime_d = dict()
# for i in range(l1):

# print(prime_list)
dict1={i:{i:{i:[] for i in range(1,10,2)} for i in range(0,10)} for i in range(1,10)}
for i in prime_list:
    dict1[i//1000][(i//100)%10][i%10].append(i)

for i in dict1:
    for j in dict1[i]:
        print(f'{i}: {j}: {dict1[i][j]}')