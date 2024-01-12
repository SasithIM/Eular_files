names = {}
alp = {'"':0}
alp_temp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';c = 1
for i in alp_temp:
    alp[i] = c
    c+=1

def name_count(name):
    count = 0
    for i in name:
        count += alp[i]
    return count

with open('0022_names.txt') as file1:
    for i in file1.read().split(','):
        i=i.removeprefix('"').removesuffix('"')
        names[i] = name_count(i)

name_list = sorted(names)

for i in range(len(name_list)):
    names[name_list[i]] *= i+1

print(sum(names.values()))