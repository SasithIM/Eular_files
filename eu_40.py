num = ''; i=1
while len(num)<1000000:
    num+=str(i)
    i+=1

total=1
for i in range(7):
    print(num[10**i-1])
    total*=int(num[10**i-1])

print(total)