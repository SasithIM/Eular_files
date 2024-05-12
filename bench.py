import math

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False
    for num in range(2, int(math.sqrt(limit)) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False
    return [num for num in range(2, limit + 1) if primes[num]]

limit = int(1e9) + 1

primes = sieve_of_eratosthenes(limit)

with open('primes.txt', 'w') as f:
    for prime in primes:
        f.write(str(prime)+'\n')