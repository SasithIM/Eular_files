n = int(input())
list1 = [0]*(n) 

def printn(list1):
    print(''.join(map(str,list1[::-1])))

printn(list1)

for i in range(n):
    list1[i]= 1 if list1[i]==0 else 0
    printn(list1)
    for j in range(i):
        list1[j]= 1 if list1[j]==0 else 0
        printn(list1)

