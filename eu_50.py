import primes

n=10**6;pre = 21
prime_list = primes.primes(n); l = len(prime_list)-1
prime_set = set(prime_list)
max_chain=0;max_sum=0

for chain in range(pre,l):
    for index in range(l-chain):
        prime_sum = sum(prime_list[index:index+chain])
        if prime_sum>n:
            break
        elif prime_sum in prime_set:
            if max_chain<chain:
                max_chain = chain; max_sum = prime_sum

print(max_chain,max_sum)