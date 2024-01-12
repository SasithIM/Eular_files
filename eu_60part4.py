import eu_60part3
import primes
# prime_set = set(primes.primes(10**9))

con_prime = eu_60part3.con_prime

prime_fours = eu_60part3.prime_fours
prime_fives = dict()

for pr1 in prime_fours:
    prime_fives[pr1]=dict()
    for pr2 in prime_fours[pr1]:
        prime_fives[pr1][pr2]=dict()
        prl = prime_fours[pr1][pr2]
        for pr3 in prl:
            prime_fives[pr1][pr2][pr3]=dict()
            prl2 = prime_fours[pr1][pr2][pr3]
            l = len(prime_fours[pr1][pr2][pr3])
            for i in range(l-1):
                prime_fives[pr1][pr2][pr3][prl2[i]]=[]
                for j in range(i,l):
                    if con_prime(prl2[i],prl2[j]):
                        prime_fives[pr1][pr2][pr3][prl2[i]].append(prl2[j])
                if len(prime_fives[pr1][pr2][pr3][prl2[i]])<1:
                    del(prime_fives[pr1][pr2][pr3][prl2[i]])
            if prime_fives[pr1][pr2][pr3]==dict():
                del(prime_fives[pr1][pr2][pr3])
        if prime_fives[pr1][pr2]==dict():
            del(prime_fives[pr1][pr2])
    if prime_fives[pr1]==dict():
        del(prime_fives[pr1])

print(prime_fives)