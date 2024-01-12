import math
def divisors(num):
    div_list = []
    for i in range(1,int(math.sqrt(int(num)))+1):
        if not(num%i):
            div_list.append(i)
            if int(num/i)!=i:
                div_list.append(int(num/i))
            div_list.sort()
    return div_list