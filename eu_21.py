import math
def divisors(num):
    div_list = []
    for i in range(1,int(math.sqrt(int(num)))+1):
        if not(num%i):
            div_list.append(i)
            if int(num/i)!=i:
                div_list.append(int(num/i))
            div_list.sort()
    return div_list[:-1]

num_list = {}; total = 0

for i in range(3,10000):
    sum_dev = sum(divisors(i))
    num_list[i] = sum_dev
    if sum_dev < i:
        if sum_dev in num_list:
            if num_list[sum_dev] == i:
                total += sum_dev + i
print(total)