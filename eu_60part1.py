import primes

n=100000
prime_list = primes.primes(n)
prime_set = set(primes.primes(10**8))
prime_pairs = dict()
l=len(prime_list)
# count=0

for i in range(1,l-2):
    prime_pairs[prime_list[i]]=[]
    for j in range(i+1,l-1):
        if int(str(prime_list[i])+str(prime_list[j])) in prime_set and int(str(prime_list[j])+str(prime_list[i])) in prime_set:
            prime_pairs[prime_list[i]].append(prime_list[j])
            # count+=1
    if len(prime_pairs[prime_list[i]])<2:
        del(prime_pairs[prime_list[i]])

with open("prime_pairs.txt",'w') as f1:
    f1.writelines(f'{i} : {prime_pairs[i]}\n' for i in prime_pairs)
