import divisors

def rel_prime(num):
    count=1
    fc_num = set(divisors.divisors(num)[1:-1])
    for i in range(2,num):
        if num%i:
            fc_i=divisors.divisors(i)[1:]
            for j in fc_i:
                if j in fc_num:
                    break
            else:
                count+=1
        if count>num/3:
            break
    return count

max_x=0;max_i=0;max_n=0
for i in range(2,100):
    # print(i),
    n=rel_prime(i)
    x = i/n
    if max_x<x:
        max_x=x
        max_i=i
        max_n=n

    
print(max_x,max_i,max_n)

# print(rel_prime(999998))