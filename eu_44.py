lim = 1000
pent_list = [int(n*(3*n-1)/2) for n in range(1,lim)]
pent_set = set(pent_list);print('list done')
l = len(pent_list)-2
min_d = 0   

for x in range(l):
    for y in range(x+1,l+1):
        diff = abs(pent_list[x]-pent_list[y]);print(diff)
        if diff > min_d:
            continue
        if ((pent_list[x]+pent_list[y]) in pent_set) and (diff in pent_set):
            if min_d == 0 or diff<min_d:
                min_d=diff;print(x,y,x-y,x+y)

print(min_d)


# takes too long 
# check v2