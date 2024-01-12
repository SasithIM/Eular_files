import math
num_list = [i for i in range(10)]
per = []
place = 0

while len(per)<9:
    f = math.factorial(len(num_list)-1)
    n = math.ceil((1000000-place)/f)-1
    c = num_list[n]
    per.append(c)
    num_list.remove(c)
    place += f*n
    if place == 1000000:
        print(len(per))
        break


[per.append(i) for i in num_list]
print(str(per).removeprefix('[').removesuffix(']').replace(',','').replace(' ',''))

# this one works 