
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

# with open('primes3.txt', 'w+') as f1:
#     for prime in primes(10**9):
#         f1.write(str(prime)+'\n')
#     f1.close()

print(primes(10**9)[-1]) 