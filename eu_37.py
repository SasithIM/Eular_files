import primes as prm

prm_ls = {i:str(i) for i in prm.primes(1000000)}
total=0

for i in prm_ls.values():
    for j in range(len(i)-1,0,-1):
        if int(i[:j]) in prm_ls and int(i[len(i)-j:]) in prm_ls:
            pass
        else:
            break
        if j==1:
            total+=int(i)

print(total)