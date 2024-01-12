import eu_60part2

con_prime = eu_60part2.con_prime
    
prime_threes = eu_60part2.prime_threes
prime_fours = dict()

for pr1 in prime_threes:
    prime_fours[pr1]=dict()
    for pr2 in prime_threes[pr1]:
        prime_fours[pr1][pr2]=dict()
        l = len(prime_threes[pr1][pr2])
        prl = prime_threes[pr1][pr2]
        for i in range(l-1):
            prime_fours[pr1][pr2][prl[i]]=[]
            for j in range(i,l):
                if con_prime(prl[i],prl[j]):
                    prime_fours[pr1][pr2][prl[i]].append(prl[j])
            if len(prime_fours[pr1][pr2][prl[i]])<2:
                del(prime_fours[pr1][pr2][prl[i]])
        if prime_fours[pr1][pr2]==dict():
            del(prime_fours[pr1][pr2])
    if prime_fours[pr1]==dict():
        del(prime_fours[pr1])

# print(prime_fours)
print('part3 done.')