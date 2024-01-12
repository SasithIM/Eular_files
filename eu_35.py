import primes

prime_list = primes.primes(120)
prime_dict = {}

for i in prime_list:
    id = ''.join(sorted([j for j in str(i)]))
    # if str(i)==str(i)[::-1]:
    #     prime_dict[id]=len(str(i))
    if id in prime_dict:
        prime_dict[id]+=1
    else:
        prime_dict[id]=1

count=0
for x,y in prime_dict.items():
    if len(x) == y and ('0' not in x):
        count+=y
    elif x == x[::-1]:
        count+=1

print(count,prime_dict)