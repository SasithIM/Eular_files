import math
import primes as prm

pytri_ls = {}
prmls = prm.primes(32)      #the sum gets bigger than 1000 for bigger nums
n=500
w=2

# for i in prmls:
#     for j in range(1,n):
#         x=math.sqrt(i**2+j**2); y=int(x)
#         if not(x-y):
#             pytri_ls[i] = [i,j,y,i+j+y]

# print(pytri_ls)

for i in range(500):
    for j in range(500):
        x=math.sqrt(i**2+j**2); y=int(x); z=i+j+y
        if not(x-y) and z<=1000:
            if z in pytri_ls:
                pytri_ls[z]+=1
            else:
                pytri_ls[z]=1

print(list(pytri_ls.keys())[list(pytri_ls.values()).index(max(pytri_ls.values()))])