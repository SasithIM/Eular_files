import permutations as pm

perm_ls = pm.permute_str('0123456789')
sum1=0
for i in perm_ls:
    if not(int(i[1:4])%2) and not(int(i[2:5])%3) and not(int(i[3:6])%5) and not(int(i[4:7])%7) and not(int(i[5:8])%11) and not(int(i[6:9])%13) and not(int(i[7:10])%17):
        sum1+=int(i)

print(sum1)