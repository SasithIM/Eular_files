import primes,math

lim = 50*10**6 + 1
prime_list = primes.primes(int(math.sqrt(lim)))

count=set()
for i in prime_list:
    four = i**4
    if four>lim:
        break
    for j in prime_list:
        three = j**3
        if three+four>lim:
            break
        for k in prime_list:
            two = k**2
            num=two+three+four
            if num < lim:
                count.add(num)
                # print(two+three+four,i,j,k)
            else:
                break
print(len(count))