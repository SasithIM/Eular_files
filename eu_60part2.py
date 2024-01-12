import primes
prime_set = set(primes.primes(10**9))

def list_str(str1):
    list1=[]
    for i in str1:
        try:
            list1.append(int(i))
        except:
            pass
    return list1

def strip_str(str1):
    temp = str1.split(':')
    pr1 = int(temp[0].strip())
    temp[1] = temp[1].strip().removeprefix('[').removesuffix(']')
    list1 = [int(i) for i in temp[1].split(',')]
    return pr1,list1

def con_prime(x,y):
    if int(str(x)+str(y)) in prime_set:
        if int(str(y)+str(x)) in prime_set:
            return True
    else:
        return False


prime_threes = dict()

with open('prime_pairs.txt') as f1:
    for line in f1.readlines():
        pr, pr_list= strip_str(line)
        l1 = len(pr_list)
        if l1>1:
            prime_threes[pr] = dict()
            for i in range(l1-1):
                prime_threes[pr][pr_list[i]] = []
                for j in range(i+1,l1):
                    if con_prime(pr_list[i],pr_list[j]):
                        # prime_threes[pr][pr_list[i]].append(pr_list[i])
                        prime_threes[pr][pr_list[i]].append(pr_list[j])
                if len(prime_threes[pr][pr_list[i]])<=1:
                    del(prime_threes[pr][pr_list[i]])
            if prime_threes[pr]==dict():
                del(prime_threes[pr])
    
print('part2 done.')
# with open('prime_threes.txt','w') as f2:
#     f2.writelines(f'{i} : {prime_threes[i]} \n' for i in prime_threes)