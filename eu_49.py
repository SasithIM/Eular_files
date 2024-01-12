import primes

def ifSeries_ari(list1):
    l = len(list1)
    list1 = sorted(list1)
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                if list1[k]-list1[j] == list1[j]-list1[i]:
                    return [list1[i],list1[j],list1[k]]
    else:
        return None


prime_list = primes.primes(10000)[len(primes.primes(1000)):]
id_list = []

for i in prime_list:
    count = 0; temp1=[]
    id = sorted(str(i))
    id_list.append(id)

    for j in range(len(id_list)):
        if id_list[j]==id:
            count+=1
            temp1.append(prime_list[j])

    x = ifSeries_ari(temp1)
    if x!=None:
        print(x)
     